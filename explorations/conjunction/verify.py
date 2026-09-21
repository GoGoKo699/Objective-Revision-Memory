#!/usr/bin/env python3
"""Exact finite checks for the A1 objective-revision checkpoint.

Requires Python 3.10+ and the standard library only. No network, sampling,
third-party solver, or machine-learning library is used. The finite checks
support, but do not replace, the proofs in research_note.md.

Run: python verify.py
The report and explicit four-feature decoder are written beside this script.
Coordinates are numbered from 1; coordinate 1 is the rightmost displayed bit.
"""
from __future__ import annotations

from functools import lru_cache
from itertools import product
from math import comb
from pathlib import Path
import json


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def conjunction(x: int, subset: int) -> int:
    return int(x & subset == subset)


def truth_mask(n: int, subset: int) -> int:
    return sum(conjunction(x, subset) << x for x in range(1 << n))


def one_probe_cells(n: int) -> list[int]:
    """Exhaust all nonempty cells; a one-probe output is constant or a literal."""
    targets = [truth_mask(n, s) for s in range(1 << n)]
    coordinates = [truth_mask(n, 1 << j) for j in range(n)]
    good = []
    for cell in range(1, 1 << (1 << n)):
        realizable = {0, cell}
        for column in coordinates:
            restricted = column & cell
            realizable.add(restricted)
            realizable.add(cell ^ restricted)
        if all((target & cell) in realizable for target in targets):
            good.append(cell)
    return good


def decoder_for_cell(n: int, states: list[int], subset: int) -> dict:
    values = {conjunction(x, subset) for x in states}
    if len(values) == 1:
        return {"kind": "constant", "value": next(iter(values))}
    for j in range(n):
        for flip in (0, 1):
            if all((((x >> j) & 1) ^ flip) == conjunction(x, subset)
                   for x in states):
                return {"kind": "probe", "coordinate": j + 1, "xor": flip}
    raise AssertionError(f"No one-probe decoder: n={n}, cell={states}, S={subset}")


def check_partition(n: int, string_cells: list[list[str]]) -> tuple[int, list[dict]]:
    cells = [[int(x, 2) for x in cell] for cell in string_cells]
    flattened = [x for cell in cells for x in cell]
    require(sorted(flattened) == list(range(1 << n)), "Partition missing/repeats input")
    checked = 0
    descriptions = []
    for label, cell in enumerate(cells):
        rules = []
        for subset in range(1 << n):
            rule = decoder_for_cell(n, cell, subset)
            rules.append({"subset_mask": format(subset, f"0{n}b"), **rule})
            for x in cell:
                if rule["kind"] == "constant":
                    actual = rule["value"]
                else:
                    actual = ((x >> (rule["coordinate"] - 1)) & 1) ^ rule["xor"]
                require(actual == conjunction(x, subset), "Incorrect one-probe output")
                checked += 1
        descriptions.append({"label": label, "states": string_cells[label], "rules": rules})
    return checked, descriptions


def weight_answer(n: int, x: int, subset: int) -> tuple[int, int]:
    """Only accesses x through the coordinates counted below, after its weight."""
    weight = x.bit_count()  # Preprocessing, not a query-time archive read.
    if subset.bit_count() <= n // 2:
        count = 0
        total = 0
        for j in range(n):
            if subset & (1 << j):
                total += (x >> j) & 1
                count += 1
        return int(total == subset.bit_count()), count
    outside_sum = 0
    count = 0
    for j in range(n):
        if not subset & (1 << j):
            outside_sum += (x >> j) & 1
            count += 1
    return int(weight - outside_sum == subset.bit_count()), count


def subspaces(n: int) -> list[frozenset[int]]:
    """Generate all GF(2) row spaces, avoiding duplicate matrix descriptions."""
    zero = frozenset({0})
    seen = {zero}
    queue = [zero]
    while queue:
        space = queue.pop()
        for vector in range(1 << n):
            if vector in space:
                continue
            extended = space | frozenset(x ^ vector for x in space)
            if extended not in seen:
                seen.add(extended)
                queue.append(extended)
    return sorted(seen, key=lambda s: (len(s), sorted(s)))


def check_linear_spaces(n: int) -> dict:
    columns = [truth_mask(n, 1 << j) for j in range(n)]
    all_targets = [truth_mask(n, s) for s in range(1 << n)]

    @lru_cache(None)
    def depth(cell: int, target: int) -> int:
        restricted = target & cell
        if restricted == 0 or restricted == cell:
            return 0
        best = n + 1
        for column in columns:
            one = cell & column
            zero = cell ^ one
            if not one or not zero:
                continue
            candidate = 1 + max(depth(zero, target), depth(one, target))
            best = min(best, candidate)
        require(best <= n, "Nonconstant cell has no valid split")
        return best

    spaces = subspaces(n)
    for space in spaces:
        rank = len(space).bit_length() - 1
        row_list = sorted(space)
        cells: dict[tuple[int, ...], int] = {}
        for x in range(1 << n):
            signature = tuple((x & row).bit_count() % 2 for row in row_list)
            cells[signature] = cells.get(signature, 0) | (1 << x)
        full_and_depth = max(depth(cell, all_targets[-1]) for cell in cells.values())
        all_query_depth = max(depth(cell, target)
                              for cell in cells.values() for target in all_targets)
        require(full_and_depth == n - rank, "Linear full-AND bound mismatch")
        require(all_query_depth == n - rank, "Linear universal bound mismatch")
    return {"n": n, "row_spaces_checked": len(spaces),
            "method": "exact adaptive decision-tree dynamic programming",
            "all_worst_case_depths_equal_n_minus_rank": True}


def main() -> None:
    root = Path(__file__).resolve().parent
    witnesses = {
        2: [["00", "01", "11"], ["10"]],
        3: [["000", "010", "100", "101"], ["001", "110"], ["011", "111"]],
        4: [["0000", "0001", "0010", "0111"],
            ["0011", "0101", "0110", "1011"],
            ["0100", "1100", "1101", "1110"],
            ["1000", "1001", "1010", "1111"]],
    }
    cells_report = []
    for n in (2, 3, 4):
        good = one_probe_cells(n)
        max_size = max(cell.bit_count() for cell in good)
        require(max_size <= sum(comb(n, j) for j in range(2)), "Dimension bound failed")
        checks, description = check_partition(n, witnesses[n])
        lower = ((1 << n) + max_size - 1) // max_size
        justification = "maximum compatible-cell cardinality and covering count"
        if n == 3:
            full = (1 << (1 << n)) - 1
            good_set = set(good)
            require(not any((full ^ cell) in good_set for cell in good),
                    "Unexpected two-label encoding for n=3")
            lower = 3
            justification = "exhaustive absence of two complementary compatible cells"
        require(lower == len(witnesses[n]), "Lower/upper bounds do not meet")
        cells_report.append({"n": n, "cells_examined": (1 << (1 << n)) - 1,
            "compatible_cells": len(good), "maximum_cell_size": max_size,
            "minimum_sketch_labels_for_one_probe": lower,
            "optimality_check": justification, "witness_input_query_checks": checks})
        if n == 4:
            (root / "four_feature_decoder.json").write_text(json.dumps({
                "coordinates": "coordinate 1 is the rightmost displayed bit",
                "empty_subset": "0000; conjunction equals 1",
                "cells": description}, indent=2) + "\n")

    weight_report = []
    for n in range(1, 9):
        worst = 0
        count = 0
        for x, subset in product(range(1 << n), repeat=2):
            answer, reads = weight_answer(n, x, subset)
            require(answer == conjunction(x, subset), "Incorrect weight-based answer")
            require(reads <= n // 2, "Too many weight-based probes")
            worst = max(worst, reads)
            count += 1
        weight_report.append({"n": n, "input_query_pairs": count,
                              "worst_probes": worst, "sketch_labels": n + 1})

    linear_report = [check_linear_spaces(n) for n in range(1, 5)]
    expected_counts = [2, 5, 16, 67]
    require([item["row_spaces_checked"] for item in linear_report] == expected_counts,
            "Subspace enumeration count mismatch")
    report = {"status": "PASS", "arithmetic": "exact integers; no numerical optimization",
        "one_probe_exhaustion": cells_report,
        "hamming_weight_construction": weight_report,
        "parity_linear_sketches": linear_report,
        "scope": "Finite examples only; general theorems are proved in research_note.md.",
        "novelty": "Not established by these checks."}
    (root / "verification_results.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
