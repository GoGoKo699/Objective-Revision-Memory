#!/usr/bin/env python3
"""Small exact checks of two obstructions to proposed priority reductions.

Equal residual rank does not fix a decoder ball's volume. Conversely, merely
requiring distinct nonzero residual rows of weight at most three admits the
core construction below, which is outside the pair-labelled strategy class.
These finite checks support the explicit obstructions; they do not establish
an asymptotic rate or historical novelty. No baseline verifier is imported.
"""

from collections import Counter
from itertools import combinations
import json
from math import comb


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def binary_rank(rows):
    """Compute the binary row rank with integer masks and XOR elimination."""
    pivots = {}
    for row in rows:
        while row:
            pivot = row.bit_length() - 1
            if pivot not in pivots:
                pivots[pivot] = row
                break
            row ^= pivots[pivot]
    return len(pivots)


def check_equal_rank_balls():
    records = []
    counts = Counter()
    for n in range(3, 9):
        pairs = tuple(combinations(range(n), 2))
        N = len(pairs)
        constant_rows = tuple((1 << i) ^ (1 << j) for i, j in pairs)
        endpoint_rows = tuple(pair ^ (1 << i)
                              for pair, (i, _) in zip(constant_rows, pairs))
        for rows in (constant_rows, endpoint_rows):
            require(binary_rank(rows) == n - 1,
                    f"wrong canonical residual rank at n={n}")
            counts["rank_checks"] += 1

        direct_histograms = [Counter(), Counter()]
        formula_histograms = [Counter(), Counter()]
        for x in range(1 << n):
            constant_errors = endpoint_errors = 0
            for i, j in pairs:
                target = ((x >> i) ^ (x >> j)) & 1
                constant_errors += target != 0
                endpoint_errors += target != ((x >> i) & 1)
                counts["direct_pair_error_checks"] += 2
            weight = x.bit_count()
            predicted_constant = weight * (n - weight)
            # Zero-based coordinate j has j lower-labelled partners.
            predicted_endpoint = sum(j * ((x >> j) & 1) for j in range(n))
            require(constant_errors == predicted_constant,
                    f"constant-answer formula failed at n={n}, x={x}")
            require(endpoint_errors == predicted_endpoint,
                    f"ordered-endpoint formula failed at n={n}, x={x}")
            counts["input_distortion_checks"] += 2
            counts["inputs_enumerated"] += 1
            for histogram, errors in zip(
                    direct_histograms, (constant_errors, endpoint_errors)):
                histogram[errors] += 1
            for histogram, errors in zip(
                    formula_histograms, (predicted_constant, predicted_endpoint)):
                histogram[errors] += 1

        for direct, formula in zip(direct_histograms, formula_histograms):
            require(direct == formula, f"full histogram differs at n={n}")
            require(sum(direct.values()) == 1 << n,
                    f"incomplete input enumeration at n={n}")
            require(direct[0] == 2, f"wrong zero-error fiber size at n={n}")
            counts["histogram_checks"] += 1
            counts["zero_error_fiber_checks"] += 1

        constant_balls = []
        endpoint_balls = []
        constant_total = endpoint_total = 0
        for threshold in range(N + 1):
            constant_total += direct_histograms[0][threshold]
            endpoint_total += direct_histograms[1][threshold]
            constant_balls.append(constant_total)
            endpoint_balls.append(endpoint_total)
        differing_threshold = next(
            (threshold for threshold in range(N + 1)
             if 2 * threshold < N
             and constant_balls[threshold] != endpoint_balls[threshold]), None)
        require(differing_threshold is not None,
                f"no differing ball sizes below error one-half at n={n}")
        counts["ball_size_separations"] += 1
        records.append({
            "n": n,
            "pairs": N,
            "residual_rank_both": n - 1,
            "zero_error_inputs_both": 2,
            "constant_error_histogram": [direct_histograms[0][j]
                                         for j in range(N + 1)],
            "endpoint_error_histogram": [direct_histograms[1][j]
                                         for j in range(N + 1)],
            "separating_wrong_pair_threshold": differing_threshold,
            "constant_ball_size": constant_balls[differing_threshold],
            "endpoint_ball_size": endpoint_balls[differing_threshold],
        })
    return {"counts": dict(counts), "records": records}


def check_sparse_row_relaxation():
    records = []
    counts = Counter()
    for n in (8, 12, 16, 24, 32):
        N = comb(n, 2)
        t = max(t for t in range(n + 1) if comb(t, 3) + n - t <= N)
        require(t < n and comb(t + 1, 3) + n - t - 1 > N,
                f"core size is not maximal at n={n}")
        triples = tuple(sum(1 << i for i in indices)
                        for indices in combinations(range(t), 3))
        outside = tuple(1 << i for i in range(t, n))
        remaining = N - len(triples) - len(outside)
        possible_pairs = tuple((1 << i) | (1 << j)
                               for i, j in combinations(range(t), 2))
        require(0 <= remaining <= len(possible_pairs),
                f"not enough distinct core pairs at n={n}")
        core_pairs = possible_pairs[:remaining]
        rows = triples + outside + core_pairs
        require(len(rows) == N and len(set(rows)) == N,
                f"rows are not N distinct vectors at n={n}")
        require(all(0 < row < (1 << n) and 1 <= row.bit_count() <= 3
                    for row in rows), f"invalid sparse row at n={n}")
        require(binary_rank(rows) == n, f"rows lack full rank at n={n}")
        require(len(triples) > comb(t, 2),
                f"no pair-labelling obstruction at n={n}")
        counts["constructions"] += 1
        counts["rows_checked"] += len(rows)
        counts["full_rank_checks"] += 1
        counts["pair_labelling_obstructions"] += 1

        # Spins are (-1)^x_i. Fixing the core positive means x_i=0 for i<t.
        # Each core row then contributes +1; every outside coordinate appears
        # only in its own singleton. Thus each outside contribution is at
        # least -1 independently, and all negatives attain the lower bound.
        core_mask = (1 << t) - 1
        outside_mask = ((1 << n) - 1) ^ core_mask
        require(all(row & outside_mask == 0 for row in triples + core_pairs),
                f"a core row touches an outside coordinate at n={n}")
        for i in range(t, n):
            touching = tuple(row for row in rows if row & (1 << i))
            require(touching == (1 << i,),
                    f"outside coordinate is not an isolated singleton at n={n}")
            counts["outside_incidence_checks"] += 1
        structural_minimum = len(triples) + len(core_pairs) - len(outside)
        attained_score = sum(1 - 2 * ((row & outside_mask).bit_count() & 1)
                             for row in rows)
        require(structural_minimum == attained_score == N - 2 * (n - t),
                f"conditional score minimum is incorrect at n={n}")
        # Error <=1/4 is score >=N/2. Use integers, including odd N.
        require(2 * structural_minimum >= N,
                f"the whole core-positive event is not accepted at n={n}")
        counts["conditional_minimum_checks"] += 1
        counts["quarter_error_threshold_checks"] += 1
        records.append({
            "n": n,
            "rows": N,
            "rank": n,
            "core_size": t,
            "core_triples": len(triples),
            "available_core_query_pairs": comb(t, 2),
            "added_core_pairs": len(core_pairs),
            "outside_singletons": len(outside),
            "minimum_score_with_positive_core": structural_minimum,
            "maximum_errors_with_positive_core": n - t,
            "accepted_inputs_from_positive_core": 1 << (n - t),
            "total_inputs": 1 << n,
            "accepted_mass_lower_bound_denominator": 1 << t,
        })
    return {"counts": dict(counts), "records": records,
            "large_input_enumeration": False}


def main():
    print(json.dumps({"status": "passed", "arithmetic": "exact integer",
                      "equal_rank_balls": check_equal_rank_balls(),
                      "sparse_row_relaxation": check_sparse_row_relaxation()},
                     sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
