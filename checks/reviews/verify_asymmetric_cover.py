#!/usr/bin/env python3
"""Independent exact check of mask/permutation symmetry with an asymmetric cover.

The first three permuted coordinates form a weak block. Its four codewords
have coordinate 2 fixed to zero, so covering errors occur only there. The last
two coordinates form an exact block. Same-block ties reconstruct the smaller
original query label. All seeds and every fixed input/query are enumerated.
"""

from fractions import Fraction
from itertools import combinations, permutations
import json


class RawBitOracle:
    def __init__(self, x: int, n: int) -> None:
        self.__x = x
        self.n = n
        self.reads = 0

    def read(self, coordinate: int) -> int:
        if not 0 <= coordinate < self.n:
            raise IndexError(coordinate)
        if self.reads != 0:
            raise RuntimeError("more than one raw-bit read")
        self.reads += 1
        return (self.__x >> coordinate) & 1


def encode(x: int, permutation: tuple[int, ...], mask: int) -> tuple[int, int]:
    y = sum(
        ((((x >> original) & 1) ^ ((mask >> position) & 1)) << position)
        for position, original in enumerate(permutation)
    )
    # A packed four-bit center index retains positions 0, 1, 3, and 4.
    index = (y & 3) | ((y >> 1) & 12)
    return x.bit_count() & 1, index


def decode(memory: tuple[int, int], permutation: tuple[int, ...], mask: int,
           i: int, j: int, oracle: RawBitOracle) -> int:
    positions = {original: position for position, original in enumerate(permutation)}
    a, b = positions[i], positions[j]
    # i < j. Prefer the exact block; otherwise retain the smaller-label tie.
    estimated = i if a >= 3 or b < 3 else j
    reread = j if estimated == i else i
    position = positions[estimated]
    parity, index = memory
    center = (index & 3) | ((index & 12) << 1)
    estimate = ((center >> position) & 1) ^ ((mask >> position) & 1)
    return parity ^ estimate ^ oracle.read(reread)


def main() -> None:
    if not __debug__:
        raise RuntimeError("run without -O; exact assertions must remain active")
    n = 5
    seeds_per_input_query = 120 * (1 << n)
    total_executions = 0
    fixed_input_query_cases = 0
    perms = tuple(permutations(range(n)))
    for x in range(1 << n):
        for i, j in combinations(range(n), 2):
            errors = 0
            correct = (x.bit_count() & 1) ^ ((x >> i) & 1) ^ ((x >> j) & 1)
            for permutation in perms:
                for mask in range(1 << n):
                    oracle = RawBitOracle(x, n)
                    memory = encode(x, permutation, mask)
                    answer = decode(memory, permutation, mask, i, j, oracle)
                    errors += answer != correct
                    assert oracle.reads == 1
                    total_executions += 1
            error = Fraction(errors, seeds_per_input_query)
            assert error == Fraction(1, 20), (x, i, j, error)
            assert error <= Fraction(1, 10)
            fixed_input_query_cases += 1
    assert total_executions == 1_228_800
    assert fixed_input_query_cases == 320
    print(json.dumps({
        "status": "PASS",
        "input_bits": n,
        "block_sizes": [3, 2],
        "summary_bits_including_parity": 5,
        "fixed_input_query_cases": fixed_input_query_cases,
        "all_seed_decoder_executions": total_executions,
        "error_every_fixed_input_query": "1/20",
        "covering_radius_error_bound": "1/10",
        "raw_reads_per_execution": 1,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
