#!/usr/bin/env python3
"""Optional exact check of pair coverage in the low-rank range.

Enumerates binary subspaces independently of the baseline verification scripts.
All arithmetic is integral; the finite checks supplement the quotient-space
proof and do not prove its general statement. No original-parity constraint is
imposed, because the rank-coverage lemma applies to arbitrary residual spans.
"""

from itertools import combinations, product
import json


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def rref_bases(n, rank):
    """Enumerate unique RREF bases, with the highest set bit as each pivot.

    Pivot columns form an identity matrix. A row may have free entries only
    below its pivot index, which is ordinary RREF after reversing column order.
    This constructs only the ranks being checked, rather than filtering all
    subspaces of the ambient space.
    """
    for pivots in combinations(range(n), rank):
        pivot_set = set(pivots)
        positions = [(row, column)
                     for row, pivot in enumerate(pivots)
                     for column in range(pivot)
                     if column not in pivot_set]
        for values in product((0, 1), repeat=len(positions)):
            rows = [1 << pivot for pivot in pivots]
            for (row, column), value in zip(positions, values):
                rows[row] |= value << column
            yield tuple(reversed(rows))


def in_span(vector, descending_basis):
    for row in descending_basis:
        pivot = row.bit_length() - 1
        if (vector >> pivot) & 1:
            vector ^= row
    return vector == 0


def covered_pair_count(n, contains):
    count = 0
    for i, j in combinations(range(n), 2):
        pair = (1 << i) | (1 << j)
        if contains(pair) or any(contains(pair ^ (1 << k))
                                 for k in range(n)):
            count += 1
    return count


def gaussian_binomial(n, rank):
    numerator = denominator = 1
    for i in range(rank):
        numerator *= (1 << n) - (1 << i)
        denominator *= (1 << rank) - (1 << i)
    require(numerator % denominator == 0, "nonintegral subspace count")
    return numerator // denominator


def low_rank_bound(n, rank):
    return n * rank - rank * (rank + 1) // 2


def check_low_rank():
    results = []
    for n in range(3, 8):
        rank_results = []
        for rank in range((n - 2) // 2 + 1):
            bound = low_rank_bound(n, rank)
            count = 0
            maximum = -1
            for basis in rref_bases(n, rank):
                count += 1
                covered = covered_pair_count(
                    n, lambda vector: in_span(vector, basis))
                require(covered <= bound,
                        f"bound failure: n={n}, rank={rank}, "
                        f"basis={basis}, covered={covered}, bound={bound}")
                maximum = max(maximum, covered)
            require(count == gaussian_binomial(n, rank),
                    f"enumeration count mismatch: n={n}, rank={rank}")
            require(maximum == bound,
                    f"maximum mismatch: n={n}, rank={rank}")

            # A coordinate subspace contains precisely the vectors supported
            # on its first rank coordinates. Check attainment independently
            # of the RREF membership routine.
            coordinate_maximum = covered_pair_count(
                n, lambda vector: vector < (1 << rank))
            require(coordinate_maximum == bound,
                    f"coordinate attainment failure: n={n}, rank={rank}")
            rank_results.append({
                "rank": rank,
                "subspaces": count,
                "maximum_covered_pairs": maximum,
                "coordinate_subspace_covered_pairs": coordinate_maximum,
                "bound": bound,
            })
        results.append({"n": n, "ranks": rank_results})
    return results


def check_global_counterexample():
    """The [7,4,3] Hamming kernel covers all pairs with one extra coordinate.

    Columns of its parity-check matrix are the distinct nonzero 3-bit vectors.
    Compute the entire kernel directly, without using the subspace enumerator.
    """
    n = 7

    def syndrome(vector):
        result = 0
        for column in range(1, n + 1):
            if (vector >> (column - 1)) & 1:
                result ^= column
        return result

    kernel = {vector for vector in range(1 << n) if syndrome(vector) == 0}
    rank = 4
    require(len(kernel) == (1 << rank), "incorrect Hamming kernel size")
    require(all(left ^ right in kernel for left in kernel for right in kernel),
            "Hamming kernel is not a subspace")
    covered = covered_pair_count(n, kernel.__contains__)
    false_global_bound = low_rank_bound(n, rank)
    require(covered == n * (n - 1) // 2 == 21,
            "Hamming kernel does not cover every pair")
    require(covered > false_global_bound == 18,
            "missing counterexample to unrestricted-rank extension")
    return {
        "n": n,
        "rank": rank,
        "kernel_size": len(kernel),
        "covered_pairs": covered,
        "invalid_global_bound": false_global_bound,
    }


def main():
    low_rank = check_low_rank()
    print(json.dumps({
        "status": "passed",
        "arithmetic": "exact integer",
        "range": "3 <= n <= 7; 0 <= rank <= floor((n-2)/2)",
        "subspaces_checked": sum(row["subspaces"]
                                 for result in low_rank
                                 for row in result["ranks"]),
        "low_rank": low_rank,
        "global_extension_counterexample": check_global_counterexample(),
    }, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
