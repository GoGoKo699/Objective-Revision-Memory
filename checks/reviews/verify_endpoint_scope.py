#!/usr/bin/env python3
"""Small exact checks separating endpoint probes from unrestricted probes.

These finite enumerations supplement proofs; they do not establish general
memory lower bounds. Only the Python standard library is used. No baseline
verification code or output is imported or modified.
"""

from collections import Counter
from itertools import combinations
import json


def require(condition, message):
    if not condition:
        raise AssertionError(message)


class EndpointOracle:
    def __init__(self, x, pair):
        self.__x = x
        self.__pair = pair
        self.reads = 0

    def read(self, coordinate):
        if coordinate not in self.__pair:
            raise ValueError("raw probe is not a query endpoint")
        if self.reads:
            raise RuntimeError("more than one raw-bit read")
        self.reads += 1
        return (self.__x >> coordinate) & 1


def encode(x):
    # Bit 0 stores X_1 xor X_2; bits 1,...,n-2 store X_3,...,X_n.
    return (x >> 2 << 1) | ((x ^ (x >> 1)) & 1)


def decode(memory, pair, oracle):
    parity = memory.bit_count() & 1
    i, j = pair
    if j == 1:
        pair_parity = memory & 1
    elif i < 2:
        pair_parity = oracle.read(i) ^ ((memory >> (j - 1)) & 1)
    else:
        pair_parity = ((memory >> (i - 1)) ^
                       (memory >> (j - 1))) & 1
    return parity ^ pair_parity


def check_endpoint_encoding():
    results = []
    for n in range(3, 8):
        counts = Counter()
        memories = set()
        for x in range(1 << n):
            memory = encode(x)
            require(0 <= memory < (1 << (n - 1)), "memory exceeds budget")
            require(memory.bit_count() % 2 == x.bit_count() % 2,
                    "exact parity is not recoverable from memory")
            memories.add(memory)
            for pair in combinations(range(n), 2):
                oracle = EndpointOracle(x, pair)
                i, j = pair
                target = (x.bit_count() ^ (x >> i) ^ (x >> j)) & 1
                require(decode(memory, pair, oracle) == target,
                        f"incorrect endpoint answer: n={n}, x={x}, pair={pair}")
                expected_reads = int(i < 2 <= j)
                require(oracle.reads == expected_reads, "wrong raw-read count")
                counts[oracle.reads] += 1
        require(len(memories) == 1 << (n - 1), "missing fixed-length memory")
        results.append({"n": n, "summary_bits_including_parity": n - 1,
                        "distinct_memories": len(memories),
                        "zero_read_executions": counts[0],
                        "one_read_executions": counts[1]})

    # Exercise the oracle's guards, including a rejected first nonendpoint read.
    oracle = EndpointOracle(0, (0, 1))
    try:
        oracle.read(2)
    except ValueError:
        pass
    else:
        raise AssertionError("oracle accepted a nonendpoint read")
    require(oracle.reads == 0, "rejected read consumed the budget")
    oracle.read(0)
    try:
        oracle.read(1)
    except RuntimeError:
        pass
    else:
        raise AssertionError("oracle accepted a second read")
    return results


def endpoint_decodable(cell, pair):
    """Test both addresses and all four Boolean truth tables, constants included."""
    i, j = pair
    return any(
        all(((table >> ((x >> address) & 1)) & 1) ==
            (((x >> i) ^ (x >> j)) & 1) for x in cell)
        for address in pair for table in range(4)
    )


def check_three_point_cells():
    results = []
    for n in range(3, 6):
        triples = pair_tests = impossible_pairs = 0
        for parity in (0, 1):
            inputs = [x for x in range(1 << n) if x.bit_count() % 2 == parity]
            for cell in combinations(inputs, 3):
                failures = 0
                for pair in combinations(range(n), 2):
                    pair_tests += 1
                    failures += not endpoint_decodable(cell, pair)
                require(failures > 0,
                        f"three-point cell has all endpoint decoders: {n}, {cell}")
                triples += 1
                impossible_pairs += failures
        results.append({"n": n, "same_parity_triples": triples,
                        "triple_pair_tests": pair_tests,
                        "impossible_triple_pair_cases": impossible_pairs})
    return results


def span(basis):
    vectors = {0}
    for row in basis:
        vectors |= {vector ^ row for vector in vectors}
    return vectors


def check_weight_enumerator_scope():
    expected = {0: 1, 2: 1, 3: 2, 4: 1, 5: 2, 6: 1}
    results = []
    for basis, expected_coverage in (((117, 13, 3), 6), ((104, 28, 3), 7)):
        vectors = span(basis)
        require(len(vectors) == 8, "basis does not have dimension three")
        enumerator = Counter(vector.bit_count() for vector in vectors)
        require(enumerator == expected, "incorrect full weight enumerator")
        covered = 0
        for i, j in combinations(range(7), 2):
            target = (1 << i) | (1 << j)
            candidates = [target] + [target ^ (1 << k) for k in range(7)]
            covered += any(candidate in vectors for candidate in candidates)
        require(covered == expected_coverage, "incorrect unrestricted coverage")
        results.append({"n": 7, "dimension": 3, "basis": basis,
                        "full_weight_enumerator": dict(sorted(enumerator.items())),
                        "covered_pairs": covered})
    return results


def check_three_bit_separation():
    unrestricted_executions = 0
    endpoint_failures = 0
    for parity in (0, 1):
        cell = [x for x in range(8) if x.bit_count() % 2 == parity]
        require(len(cell) == 4, "wrong parity-cell size")
        for pair in combinations(range(3), 2):
            require(not endpoint_decodable(cell, pair),
                    "endpoint decoder exists on four-point parity cell")
            endpoint_failures += 1
            complement = next(k for k in range(3) if k not in pair)
            for x in cell:
                i, j = pair
                target = (parity ^ (x >> i) ^ (x >> j)) & 1
                require(((x >> complement) & 1) == target,
                        "complement-coordinate decoder is incorrect")
                unrestricted_executions += 1
    return {"n": 3, "unrestricted_summary_bits_including_parity": 1,
            "unrestricted_single_read_executions": unrestricted_executions,
            "endpoint_infeasible_parity_cell_pair_cases": endpoint_failures}


def main():
    encoding = check_endpoint_encoding()
    triples = check_three_point_cells()
    print(json.dumps({
        "status": "passed", "arithmetic": "exact integer",
        "endpoint_encoding": encoding,
        "endpoint_encoding_executions": sum(
            row["zero_read_executions"] + row["one_read_executions"]
            for row in encoding),
        "three_point_cells": triples,
        "same_parity_triples_checked": sum(
            row["same_parity_triples"] for row in triples),
        "weight_enumerator_counterexample": check_weight_enumerator_scope(),
        "three_bit_probe_separation": check_three_bit_separation(),
    }, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
