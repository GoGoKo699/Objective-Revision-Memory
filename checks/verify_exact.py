#!/usr/bin/env python3
"""Exact checks for delayed pair deletions from a binary parity rule.

Python 3.10+, standard library only. No network, learning, or floating point.
Run: python verify.py --output results.json

The general result is proved in RESEARCH_NOTE.md. These checks do not
independently establish literature novelty or replace the proof.
"""
from __future__ import annotations

import argparse
import itertools
import json
from collections import Counter
from dataclasses import dataclass
from pathlib import Path


def parity(x: int) -> int:
    return x.bit_count() & 1


@dataclass(frozen=True)
class Memory:
    """Only n-d input-dependent bits; n is fixed public metadata."""
    n: int
    bits: tuple[int, ...]


def parameters(n: int) -> tuple[int, int, tuple[int, ...]]:
    if not isinstance(n, int) or isinstance(n, bool) or n < 3:
        raise ValueError("n must be an integer at least 3")
    d = (n + 1).bit_length() - 1
    active = (1 << d) - 1
    stored = tuple(i for i in range(1, n + 1)
                   if i > active or (i & (i - 1)) != 0)
    assert len(stored) == n - d
    return d, active, stored


def encode(x: int, n: int) -> Memory:
    d, active, stored = parameters(n)
    if not isinstance(x, int) or x < 0 or x >= (1 << n):
        raise ValueError("x must encode an n-bit string")
    pivots = sum(((x >> ((1 << a) - 1)) & 1) << a for a in range(d))
    bits = tuple(((x >> (i - 1)) & 1) ^ (parity(i & pivots) if i <= active else 0)
                 for i in stored)
    return Memory(n, bits)


class RawBitOracle:
    """A counted raw-coordinate access interface; positions are one-indexed."""
    __slots__ = ("_x", "n", "reads", "limit")

    def __init__(self, x: int, n: int, limit: int = 1):
        if not (0 <= x < (1 << n)):
            raise ValueError("x must encode an n-bit string")
        self._x = x
        self.n = n
        self.reads = 0
        self.limit = limit

    def read(self, k: int) -> int:
        if not 1 <= k <= self.n:
            raise IndexError("raw coordinate out of range")
        self.reads += 1
        if self.reads > self.limit:
            raise RuntimeError("raw-coordinate budget exceeded")
        return (self._x >> (k - 1)) & 1


class Decoder:
    """Workspace is derived exclusively from persistent Memory and metadata."""
    def __init__(self, memory: Memory):
        self.n = memory.n
        _, self.active, stored = parameters(self.n)
        if len(memory.bits) != len(stored) or any(b not in (0, 1) for b in memory.bits):
            raise ValueError("malformed memory")
        self.z = [0] * (self.n + 1)
        for i, bit in zip(stored, memory.bits):
            self.z[i] = bit
        self.original = sum(memory.bits) & 1

    def pair_deletion(self, i: int, j: int, oracle: RawBitOracle) -> int:
        if not (1 <= i <= self.n and 1 <= j <= self.n and i != j):
            raise ValueError("two distinct valid coordinates required")
        base = self.original ^ self.z[i] ^ self.z[j]
        label = (i if i <= self.active else 0) ^ (j if j <= self.active else 0)
        return base if label == 0 else base ^ oracle.read(label) ^ self.z[label]

    def arbitrary_parity(self, query: int, oracle: RawBitOracle) -> int:
        if not 0 <= query < (1 << self.n):
            raise ValueError("query must be an n-bit coefficient vector")
        label = 0
        base = 0
        for i in range(1, self.n + 1):
            if (query >> (i - 1)) & 1:
                base ^= self.z[i]
                if i <= self.active:
                    label ^= i
        return base if label == 0 else base ^ oracle.read(label) ^ self.z[label]


def enumerate_cells(n: int) -> dict:
    """Direct decidability test on every nonempty parity-homogeneous cell.

    No linearity restriction is imposed. On a fixed cell, a one-bit decision
    can only be constant, a coordinate function, or its complement. Testing
    this condition is independent of the vector-space cardinality proof.
    """
    checked = 0
    accepted = 0
    largest = 0
    histogram: Counter[int] = Counter()
    universality_checks = 0
    affine_maximum_checks = 0
    upper = 1 << ((n + 1).bit_length() - 1)
    for p in (0, 1):
        states = [x for x in range(1 << n) if parity(x) == p]
        masks = [sum(((x >> k) & 1) << a for a, x in enumerate(states))
                 for k in range(n)]
        pair_masks = [masks[i] ^ masks[j] for i, j in itertools.combinations(range(n), 2)]
        all_linear_masks = [sum(parity(q & x) << a for a, x in enumerate(states))
                            for q in range(1 << n)] if n <= 4 else []
        for cell in range(1, 1 << len(states)):
            checked += 1
            allowed = {0, cell}
            for mask in masks:
                value = mask & cell
                allowed.add(value)
                allowed.add(value ^ cell)
            if not all((mask & cell) in allowed for mask in pair_masks):
                continue
            accepted += 1
            size = cell.bit_count()
            histogram[size] += 1
            largest = max(largest, size)
            assert size <= upper, (n, p, cell, size)
            for mask in all_linear_masks:
                universality_checks += 1
                assert (mask & cell) in allowed, (n, p, cell, mask)
            if size == upper:
                affine_maximum_checks += 1
                members = [x for a, x in enumerate(states) if (cell >> a) & 1]
                origin = members[0]
                differences = {x ^ origin for x in members}
                assert all(a ^ b in differences for a in differences for b in differences)
    assert largest == upper
    return {
        "n": n, "nonempty_parity_homogeneous_cells_checked": checked,
        "admissible_cells": accepted, "largest_admissible_cell": largest,
        "cell_size_histogram": dict(sorted(histogram.items())),
        "arbitrary_parity_decidability_checks": universality_checks,
        "maximal_size_affine_cell_checks": affine_maximum_checks,
    }


def check_construction(n: int, all_parities: bool = False) -> dict:
    pairs = tuple(itertools.combinations(range(1, n + 1), 2))
    pair_checks = 0
    parity_checks = 0
    read_histogram: Counter[int] = Counter()
    memory_histogram: Counter[tuple[int, ...]] = Counter()
    for x in range(1 << n):
        memory = encode(x, n)
        memory_histogram[memory.bits] += 1
        decoder = Decoder(memory)
        assert decoder.original == parity(x)
        for i, j in pairs:
            oracle = RawBitOracle(x, n)
            actual = decoder.pair_deletion(i, j, oracle)
            expected = parity(x) ^ ((x >> (i - 1)) & 1) ^ ((x >> (j - 1)) & 1)
            assert actual == expected, (n, x, i, j, actual, expected)
            pair_checks += 1
            read_histogram[oracle.reads] += 1
        if all_parities:
            for q in range(1 << n):
                oracle = RawBitOracle(x, n)
                assert decoder.arbitrary_parity(q, oracle) == parity(q & x)
                parity_checks += 1
    d, _, _ = parameters(n)
    assert len(memory_histogram) == (1 << (n - d))
    assert set(memory_histogram.values()) == {1 << d}
    return {
        "n": n, "memory_bits": n - d, "raw_inputs_checked": 1 << n,
        "distinct_memories": len(memory_histogram), "inputs_per_memory": 1 << d,
        "pair_deletion_checks": pair_checks, "arbitrary_parity_checks": parity_checks,
        "raw_read_histogram": dict(sorted(read_histogram.items())),
    }


def check_symbolic(max_n: int = 127) -> dict:
    """Exact F2 coefficient identities, not random samples or float numerics."""
    count = 0
    for n in range(3, max_n + 1):
        d, active, stored = parameters(n)
        z = [0] * (n + 1)
        for i in range(1, n + 1):
            z[i] = 1 << (i - 1)
            if i <= active:
                for a in range(d):
                    if (i >> a) & 1:
                        z[i] ^= 1 << ((1 << a) - 1)
        assert all(z[1 << a] == 0 for a in range(d))
        original = 0
        for i in stored:
            original ^= z[i]
        assert original == (1 << n) - 1
        for i, j in itertools.combinations(range(1, n + 1), 2):
            label = (i if i <= active else 0) ^ (j if j <= active else 0)
            output = original ^ z[i] ^ z[j]
            if label:
                output ^= (1 << (label - 1)) ^ z[label]
            target = ((1 << n) - 1) ^ (1 << (i - 1)) ^ (1 << (j - 1))
            assert output == target, (n, i, j)
            count += 1
    return {"n_min": 3, "n_max": max_n, "pair_identities_checked": count,
            "method": "exact integer bitmasks of F2 linear coefficients"}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path("results.json"))
    args = parser.parse_args()
    if not __debug__:
        raise RuntimeError("Run without -O: assertion checks must remain enabled")
    result = {
        "status": "PASS",
        "scope": "finite exact arithmetic; no claim of formal proof-assistant verification or novelty clearance",
        "cell_enumerations": [enumerate_cells(n) for n in (3, 4, 5)],
        "construction_enumerations": [check_construction(n, all_parities=(n == 7)) for n in (3, 4, 5, 7, 8, 15)],
        "symbolic_construction": check_symbolic(),
    }
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
