#!/usr/bin/env python3
"""Optional exact checks for counterfactual query-table distortion.

The finite enumerations check consequences of the theorem, not its general
proof. Arithmetic is integral or rational. All retained information, including
exact total parity, is charged; all raw reads pass through a counted oracle.
No baseline verification code or output is imported or modified.
"""

from collections import Counter
from fractions import Fraction
from itertools import combinations
import json


def require(condition, message):
    if not condition:
        raise AssertionError(message)


class RawOracle:
    def __init__(self, x, n, allowed=None):
        self.__x = x
        self.__n = n
        self.__allowed = allowed
        self.reads = 0
        self.address = None

    def read(self, coordinate):
        if not 0 <= coordinate < self.__n:
            raise ValueError("raw coordinate outside archive")
        if self.__allowed is not None and coordinate not in self.__allowed:
            raise ValueError("raw coordinate is not an allowed endpoint")
        if self.reads:
            raise RuntimeError("more than one raw-bit read")
        self.reads += 1
        self.address = coordinate
        return (self.__x >> coordinate) & 1


def check_oracle_guards():
    oracle = RawOracle(0, 3, (0, 1))
    for bad_coordinate in (-1, 2, 3):
        try:
            oracle.read(bad_coordinate)
        except ValueError:
            pass
        else:
            raise AssertionError("oracle accepted an invalid coordinate")
    require(oracle.reads == 0, "rejected read consumed budget")
    oracle.read(0)
    try:
        oracle.read(1)
    except RuntimeError:
        pass
    else:
        raise AssertionError("oracle accepted a second read")


def target(x, pair):
    i, j = pair
    return (x.bit_count() ^ (x >> i) ^ (x >> j)) & 1


BLOCKS = ((3, (0, 7)), (4, (0, 7, 8, 15)))


def cover_encode(x):
    memory = x.bit_count() & 1
    coordinate_offset = 0
    memory_offset = 1
    for size, centers in BLOCKS:
        block = (x >> coordinate_offset) & ((1 << size) - 1)
        index = min(range(len(centers)),
                    key=lambda index: ((block ^ centers[index]).bit_count(), index))
        memory |= index << memory_offset
        memory_offset += (len(centers) - 1).bit_length()
        coordinate_offset += size
    return memory


def cover_decode(memory, pair, oracle):
    reconstruction = 0
    coordinate_offset = 0
    memory_offset = 1
    for size, centers in BLOCKS:
        bits = (len(centers) - 1).bit_length()
        index = (memory >> memory_offset) & ((1 << bits) - 1)
        reconstruction |= centers[index] << coordinate_offset
        memory_offset += bits
        coordinate_offset += size
    i, j = pair
    return (memory & 1) ^ ((reconstruction >> j) & 1) ^ oracle.read(i)


def check_block_construction():
    n = sum(size for size, centers in BLOCKS)
    bits = 1 + sum((len(centers) - 1).bit_length() for size, centers in BLOCKS)
    block_details = []
    coarse_bound = 0
    endpoint = 0
    for size, centers in BLOCKS:
        radius = max(min((word ^ center).bit_count() for center in centers)
                     for word in range(1 << size))
        require(radius == 1, "unexpected explicit-cover radius")
        delta = Fraction(radius, size)
        endpoint += size
        coarse_bound += (endpoint - 1) * (delta * size).__floor__()
        block_details.append({"size": size, "centers": centers,
                              "index_bits": (len(centers) - 1).bit_length(),
                              "covering_radius": radius, "delta": str(delta)})

    executions = 0
    histogram = Counter()
    memories = set()
    for x in range(1 << n):
        memory = cover_encode(x)
        require(0 <= memory < 1 << bits, "summary exceeds fixed bit budget")
        require(memory & 1 == x.bit_count() & 1, "stored parity is incorrect")
        memories.add(memory)
        # Reconstruct independently from the packed indices for the identity.
        reconstruction = BLOCKS[0][1][(memory >> 1) & 1]
        reconstruction |= BLOCKS[1][1][(memory >> 2) & 3] << 3
        error_pattern = x ^ reconstruction
        weighted_errors = sum(j * ((error_pattern >> j) & 1) for j in range(n))
        wrong_pairs = 0
        for pair in combinations(range(n), 2):
            oracle = RawOracle(x, n, pair)
            wrong_pairs += cover_decode(memory, pair, oracle) != target(x, pair)
            require(oracle.reads == 1 and oracle.address == pair[0],
                    "construction did not use its one prescribed endpoint read")
            executions += 1
        require(wrong_pairs == weighted_errors, "weighted-error identity failed")
        require(wrong_pairs <= coarse_bound, "coarse block bound failed")
        histogram[wrong_pairs] += 1
    require(len(memories) == 1 << bits, "not all charged memory values occur")
    return {"n": n, "blocks": block_details,
            "summary_bits_including_parity": bits,
            "distinct_memories": len(memories),
            "input_pair_executions": executions,
            "raw_reads_per_execution": 1,
            "query_table_error_histogram": dict(sorted(histogram.items())),
            "maximum_wrong_pairs": max(histogram),
            "coarse_block_wrong_pair_bound": coarse_bound}


MODES = (("parity_no_probe", 1),
         ("parity_address", 1),
         ("parity_and_nonlinear_bit", 2))


def nonlinear_bit(x):
    return (x & 1) & ((x >> 1) & 1)


def summary_encode(x, mode):
    memory = x.bit_count() & 1
    if mode == "parity_and_nonlinear_bit":
        memory |= nonlinear_bit(x) << 1
    return memory


def summary_decode(memory, pair, n, mode, oracle):
    parity = memory & 1
    if mode == "parity_no_probe":
        return parity
    nonlinear = memory >> 1
    outsiders = [k for k in range(n) if k not in pair]
    address = outsiders[(parity + 2 * nonlinear) % len(outsiders)]
    return parity ^ nonlinear ^ oracle.read(address)


def check_finite_tail():
    # An affine bit has zero XOR on this two-coordinate affine square.
    require(nonlinear_bit(0) ^ nonlinear_bit(1) ^
            nonlinear_bit(2) ^ nonlinear_bit(3) == 1,
            "the designated retained bit is affine")
    results = []
    inequalities = nonvacuous = executions = raw_reads = 0
    example = None
    for n in range(3, 9):
        pairs = tuple(combinations(range(n), 2))
        total_pairs = len(pairs)
        for mode, bits in MODES:
            histogram = Counter()
            addresses = {pair: set() for pair in pairs}
            for x in range(1 << n):
                memory = summary_encode(x, mode)
                require(0 <= memory < 1 << bits, "summary exceeds bit budget")
                require(memory & 1 == x.bit_count() & 1, "parity not exact")
                errors = 0
                for pair in pairs:
                    oracle = RawOracle(x, n)
                    answer = summary_decode(memory, pair, n, mode, oracle)
                    errors += answer != target(x, pair)
                    executions += 1
                    raw_reads += oracle.reads
                    require(oracle.reads == int(mode != "parity_no_probe"),
                            "wrong raw-read count")
                    if oracle.reads:
                        require(oracle.address not in pair, "probe is not a nonendpoint")
                        addresses[pair].add(oracle.address)
                histogram[errors] += 1
            varying_pairs = sum(len(values) > 1 for values in addresses.values())
            if n >= 4 and mode != "parity_no_probe":
                require(varying_pairs == total_pairs,
                        "probe address does not actually depend on memory")

            cases = useful = 0
            for z in (Fraction(3, 2), Fraction(n + 1, n)):
                cosh_product = Fraction(1)
                for k in range(1, n + 1):
                    cosh_product *= (z ** k + z ** -k) / 2
                cumulative = 0
                # Outside [0,N], the bound follows from t=0 or t=N trivially.
                for threshold in range(total_pairs + 1):
                    cumulative += histogram[threshold]
                    probability = Fraction(cumulative, 1 << n)
                    bound = (1 << bits) * cosh_product / z ** (total_pairs - 2 * threshold)
                    require(probability <= bound,
                            f"tail bound failed: n={n}, mode={mode}, z={z}, t={threshold}")
                    cases += 1
                    useful += bound < 1
                    if 0 < probability <= bound < 1 and example is None:
                        example = {"n": n, "mode": mode, "summary_bits": bits,
                                   "exp_s": str(z), "wrong_pair_threshold": threshold,
                                   "exact_probability": str(probability),
                                   "exact_upper_bound": str(bound)}
            inequalities += cases
            nonvacuous += useful
            results.append({"n": n, "mode": mode,
                            "summary_bits_including_parity": bits,
                            "inequalities_checked": cases,
                            "upper_bounds_below_one": useful,
                            "pairs_with_summary_dependent_address": varying_pairs})
    require(nonvacuous > 0 and example is not None, "all checked tail bounds are vacuous")
    return {"input_pair_executions": executions, "counted_raw_reads": raw_reads,
            "inequalities_checked": inequalities,
            "upper_bounds_below_one": nonvacuous,
            "nonvacuous_example": example, "cases": results}


def main():
    check_oracle_guards()
    print(json.dumps({"status": "passed", "arithmetic": "exact integer and rational",
                      "block_construction": check_block_construction(),
                      "finite_tail": check_finite_tail()},
                     sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
