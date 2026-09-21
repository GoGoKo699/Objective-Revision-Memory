#!/usr/bin/env python3
"""Finite checks for the A1 bounded-error checkpoint.

Python 3.10+, standard library only. Truth tables, GF(2) arithmetic,
subspace enumeration, probabilities and the finite affine separation are exact.
Entropy inequalities use ordinary double precision (tolerance stated below);
they are numerical sanity checks, not interval-arithmetic proof certificates.
The general results are proved separately in RESEARCH_NOTE.md.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
from functools import lru_cache
from itertools import combinations
import json
import math
from pathlib import Path
from typing import Iterator, Sequence

TOL = 1e-10


def parity(x: int) -> int:
    return x.bit_count() & 1


def add_to_basis(basis: dict[int, int], vector: int) -> bool:
    """Insert a vector into a highest-pivot XOR basis; return independence."""
    while vector:
        pivot = vector.bit_length() - 1
        if pivot in basis:
            vector ^= basis[pivot]
        else:
            basis[pivot] = vector
            return True
    return False


def gf2_rank(rows: Sequence[int]) -> int:
    basis: dict[int, int] = {}
    for row in rows:
        add_to_basis(basis, row)
    return len(basis)


def all_subspaces(n: int) -> Iterator[tuple[tuple[int, ...], frozenset[int]]]:
    """Enumerate every subspace exactly once via reduced row echelon bases."""
    for rank in range(n + 1):
        for pivots in combinations(range(n), rank):
            free_cols = [j for j in range(n) if j not in pivots]
            positions = [(a, j) for a, p in enumerate(pivots)
                         for j in free_cols if j > p]
            for assignment in range(1 << len(positions)):
                rows = [1 << p for p in pivots]
                for t, (a, j) in enumerate(positions):
                    if (assignment >> t) & 1:
                        rows[a] |= 1 << j
                space = {0}
                for row in rows:
                    space |= {v ^ row for v in tuple(space)}
                assert len(space) == (1 << rank)
                yield tuple(rows), frozenset(space)


def phi_twice(n: int, rank: int) -> int:
    return rank * (2 * n - rank + 1)


def candidate_rows(n: int, i: int, j: int) -> tuple[int, ...]:
    pair = (1 << i) ^ (1 << j)
    return (pair,) + tuple(pair ^ (1 << k) for k in range(n))


def check_subspaces(max_n: int = 7) -> dict:
    results = {}
    known_totals = {3: 16, 4: 67, 5: 374, 6: 2825, 7: 29212}
    for n in range(3, max_n + 1):
        candidates = [candidate_rows(n, i, j)
                      for i, j in combinations(range(n), 2)]
        max_by_rank = [-1] * (n + 1)
        max_with_parity = [-1] * (n + 1)
        count = 0
        parity_count = 0
        for rows, space in all_subspaces(n):
            count += 1
            rank = len(rows)
            covered = sum(any(v in space for v in query) for query in candidates)
            assert 2 * covered <= phi_twice(n, rank), (n, rows, covered)
            max_by_rank[rank] = max(max_by_rank[rank], covered)
            if ((1 << n) - 1) in space:
                parity_count += 1
                max_with_parity[rank] = max(max_with_parity[rank], covered)
        assert count == known_totals[n], (n, count)
        minimum_exact = next(r for r, q in enumerate(max_with_parity)
                             if q == len(candidates))
        assert minimum_exact == n - ((n + 1).bit_length() - 1)
        results[str(n)] = {
            'subspaces': count,
            'subspaces_containing_total_parity': parity_count,
            'max_recoverable_pairs_by_rank': max_by_rank,
            'max_recoverable_pairs_by_rank_with_total_parity': max_with_parity,
            'minimum_exact_affine_bits': minimum_exact,
        }
    return results


@lru_cache(maxsize=None)
def h2_fraction(numerator: int, denominator: int) -> float:
    if numerator == 0 or numerator == denominator:
        return 0.0
    p = numerator / denominator
    return -p * math.log2(p) - (1 - p) * math.log2(1 - p)


def check_all_cells(max_n: int = 5) -> dict:
    """Check every possible nonempty original-parity-homogeneous cell.

    A decoder is evaluated by exact truth-table comparisons against constants,
    raw bits and their complements; no closure or rank premise is assumed.
    """
    results = {}
    for n in range(3, max_n + 1):
        pairs = list(combinations(range(n), 2))
        rows_for_pair = [candidate_rows(n, i, j) for i, j in pairs]
        count = 0
        min_entropy_slack = float('inf')
        min_phi_slack = float('inf')
        for old_parity in (0, 1):
            inputs = [x for x in range(1 << n) if parity(x) == old_parity]
            patterns = {
                s: sum(parity(s & x) << a for a, x in enumerate(inputs))
                for s in set(v for rows in rows_for_pair for v in rows)
            }
            for cell_mask in range(1, 1 << len(inputs)):
                count += 1
                size = cell_mask.bit_count()
                choices = []
                error_total = 0
                for rows in rows_for_pair:
                    best = (size + 1, -1)
                    for s in rows:
                        ones = (patterns[s] & cell_mask).bit_count()
                        candidate = (min(ones, size - ones), s)
                        best = min(best, candidate)
                    error_count, selected_row = best
                    error_total += error_count
                    choices.append((error_count, selected_row))
                # Equal cell sizes give the same weight ordering as error counts.
                basis: dict[int, int] = {}
                greedy_weight = 0.0
                total_weight = 0.0
                for error_count, selected_row in sorted(choices):
                    weight = 1 - h2_fraction(error_count, size)
                    total_weight += weight
                    if add_to_basis(basis, selected_row):
                        greedy_weight += weight
                deficiency = n - math.log2(size)
                entropy_slack = deficiency - greedy_weight
                phi = n * deficiency - deficiency * (deficiency - 1) / 2
                phi_slack = phi - total_weight
                assert entropy_slack >= -TOL, (n, cell_mask, entropy_slack)
                assert phi_slack >= -TOL, (n, cell_mask, phi_slack)
                min_entropy_slack = min(min_entropy_slack, entropy_slack)
                min_phi_slack = min(min_phi_slack, phi_slack)
                required = len(pairs) * (
                    1 - h2_fraction(error_total, size * len(pairs)))
                assert phi >= required - TOL
        assert count == 2 * ((1 << (1 << (n - 1))) - 1)
        results[str(n)] = {
            'nonempty_cells': count,
            'decoder_comparisons': count * len(pairs) * (n + 1),
            'minimum_entropy_slack_float': min_entropy_slack,
            'minimum_rank_density_entropy_slack_float': min_phi_slack,
            'float_tolerance': TOL,
        }
    return results


def majority_error(k: int) -> Fraction:
    if k < 1 or k % 2 == 0:
        raise ValueError('Block length must be a positive odd integer.')
    return (1 - Fraction(math.comb(k - 1, (k - 1) // 2), 1 << (k - 1))) / 2


def encode_majorities(x: int, n: int, k: int, public_mask: int = 0) -> int:
    if n % k or k < 1 or not (k & 1):
        raise ValueError('Use equal, odd-sized blocks dividing n.')
    y = x ^ public_mask
    memory = parity(x)
    mask = (1 << k) - 1
    for block in range(n // k):
        majority = (((y >> (k * block)) & mask).bit_count() > k // 2)
        memory |= int(majority) << (block + 1)
    return memory


class RawBitOracle:
    def __init__(self, x: int, n: int) -> None:
        self._x, self.n, self.calls = x, n, 0

    def read(self, index: int) -> int:
        if not 0 <= index < self.n:
            raise IndexError(index)
        self.calls += 1
        if self.calls > 1:
            raise AssertionError('Decoder exceeded its one-probe budget.')
        return (self._x >> index) & 1


def decode_majorities(memory: int, i: int, j: int, k: int,
                      raw: RawBitOracle, public_mask: int = 0) -> int:
    if i == j:
        raise ValueError('The revision excludes distinct inputs.')
    estimate_j = ((memory >> (1 + j // k)) & 1) ^ ((public_mask >> j) & 1)
    return (memory & 1) ^ raw.read(i) ^ estimate_j


def check_majority_truth_tables() -> dict:
    results = {}
    for k in (1, 3, 5, 7, 9, 11, 15):
        errors = [0] * k
        for y in range(1 << k):
            majority = int(y.bit_count() > k // 2)
            for j in range(k):
                errors[j] += majority != ((y >> j) & 1)
        expected = majority_error(k)
        assert all(Fraction(c, 1 << k) == expected for c in errors)
        results[str(k)] = {
            'inputs': 1 << k,
            'error_probability': str(expected),
            'wrong_predictions_each_coordinate': errors[0],
        }
    return results


def check_full_majority_decoders() -> dict:
    results = {}
    for n, k in ((6, 3), (7, 7), (10, 5), (14, 7)):
        pairs = list(combinations(range(n), 2))
        errors = [0] * len(pairs)
        messages: set[int] = set()
        decisions = 0
        for x in range(1 << n):
            memory = encode_majorities(x, n, k)
            assert memory < (1 << (n // k + 1))
            assert (memory & 1) == parity(x)
            messages.add(memory)
            for a, (i, j) in enumerate(pairs):
                raw = RawBitOracle(x, n)
                answer = decode_majorities(memory, i, j, k, raw)
                correct = parity(x) ^ ((x >> i) & 1) ^ ((x >> j) & 1)
                assert raw.calls == 1
                errors[a] += answer != correct
                decisions += 1
        expected = majority_error(k)
        assert all(Fraction(c, 1 << n) == expected for c in errors)
        results[f'n{n}_k{k}'] = {
            'input_strings': 1 << n,
            'pairs': len(pairs),
            'decisions': decisions,
            'memory_bits': n // k + 1,
            'distinct_memories': len(messages),
            'error_every_pair': str(expected),
            'max_probes': 1,
        }
    return results


def check_public_mask_symmetry() -> dict:
    results = {}
    for n, k in ((5, 5), (6, 3)):
        pairs = list(combinations(range(n), 2))
        expected = majority_error(k)
        decisions = 0
        for x in range(1 << n):
            counts = [0] * len(pairs)
            for r in range(1 << n):
                memory = encode_majorities(x, n, k, r)
                assert (memory & 1) == parity(x)
                for a, (i, j) in enumerate(pairs):
                    raw = RawBitOracle(x, n)
                    out = decode_majorities(memory, i, j, k, raw, r)
                    correct = parity(x) ^ ((x >> i) & 1) ^ ((x >> j) & 1)
                    counts[a] += out != correct
                    decisions += 1
            assert all(Fraction(c, 1 << n) == expected for c in counts)
        results[f'n{n}_k{k}'] = {
            'input_strings': 1 << n,
            'public_masks_per_input': 1 << n,
            'decisions': decisions,
            'error_for_every_fixed_input_and_pair': str(expected),
        }
    return results


def check_subset_construction() -> dict:
    results = {}
    for n in range(3, 10):
        for b in range(n + 1):
            pairs = list(combinations(range(n), 2))
            subsets = list(combinations(range(n), b))
            both_missing = [0] * len(pairs)
            for subset in subsets:
                s = set(subset)
                for a, (i, j) in enumerate(pairs):
                    both_missing[a] += i not in s and j not in s
            target = Fraction((n - b) * (n - b - 1), 2 * n * (n - 1))
            assert all(Fraction(c, 2 * len(subsets)) == target for c in both_missing)
            results[f'n{n}_b{b}'] = str(target)
    return {'settings': len(results), 'exact_error_probabilities': results}


def affine_integer_lower_bound(n: int, epsilon: Fraction) -> int:
    rhs = Fraction(n * (n - 1), 1) * (1 - 2 * epsilon)
    # Comparing 2*Phi(B) with 2*binom(n,2)*(1-2*epsilon) is exact.
    return next(b for b in range(n + 1) if phi_twice(n, b) >= rhs)


def check_separation() -> dict:
    e = Fraction(11, 32)
    results = {}
    for n in (49, 1001):
        nonlinear_bits = n // 7 + 1
        linear_lower = affine_integer_lower_bound(n, e)
        assert linear_lower > nonlinear_bits
        rhs = Fraction(n * (n - 1), 1) * (1 - 2 * e)
        assert phi_twice(n, nonlinear_bits) < rhs
        results[str(n)] = {
            'error': str(e),
            'nonlinear_achievable_bits': nonlinear_bits,
            'affine_necessary_bits': linear_lower,
            'twice_phi_at_nonlinear_bits': phi_twice(n, nonlinear_bits),
            'twice_required_pair_count': str(rhs),
            'arithmetic': 'exact integer / Fraction; not a floating square root',
        }
    assert results['49']['affine_necessary_bits'] == 9
    assert results['1001']['affine_necessary_bits'] == 171
    return results


def asymptotic_rates() -> dict:
    rows = []
    for e in (Fraction(1,100), Fraction(1,10), Fraction(1,4), Fraction(11,32)):
        h = h2_fraction(e.numerator, e.denominator)
        rows.append({
            'error': str(e),
            'arbitrary_encoder_lower_rate_float': 1 - math.sqrt(h),
            'standard_rac_achievable_rate_float': 1 - h,
            'optimal_affine_rate_float': 1 - math.sqrt(2 * float(e)),
        })
    return {'status': 'algebraic evaluations, not experimental estimates', 'rows': rows}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path('results.json'))
    args = parser.parse_args()
    tests = [
        ('subspaces', check_subspaces),
        ('all_cells', check_all_cells),
        ('majority_truth_tables', check_majority_truth_tables),
        ('full_majority_decoders', check_full_majority_decoders),
        ('public_mask_symmetry', check_public_mask_symmetry),
        ('subset_construction', check_subset_construction),
        ('finite_separation', check_separation),
        ('asymptotic_evaluations', asymptotic_rates),
    ]
    results = {'status': 'PASS', 'standard_library_only': True,
               'entropy_checks': 'double precision only; see stated tolerance',
               'general_proof': 'RESEARCH_NOTE.md, not finite extrapolation'}
    for name, test in tests:
        print(f'Checking {name} ...', flush=True)
        results[name] = test()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(results, indent=2, sort_keys=True) + '\n')
    print(f'PASS: wrote {args.output}', flush=True)


if __name__ == '__main__':
    main()
