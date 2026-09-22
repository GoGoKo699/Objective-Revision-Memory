#!/usr/bin/env python3
"""Exact three-bit checks of strategy translation and mandatory parity.

This targets translation signs and the parity boundary, not asymptotic rates.
Only the standard library is used; no original verification artifact is changed.
"""

from collections import Counter
from itertools import combinations, product
import json


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def answer(function, x):
    address, truth_table = function
    bit = 0 if address is None else (x >> address) & 1
    return truth_table[bit]


def target(x, pair):
    i, j = pair
    return ((x >> i) ^ (x >> j)) & 1


def wrong_count(strategy, x, pairs):
    return sum(answer(function, x) != target(x, pair)
               for function, pair in zip(strategy, pairs))


def translate(strategy, mask, pairs):
    result = []
    for (address, truth_table), pair in zip(strategy, pairs):
        shift = 0 if address is None else (mask >> address) & 1
        pair_shift = target(mask, pair)
        shifted_table = tuple(truth_table[b ^ shift] ^ pair_shift
                              for b in (0, 1))
        result.append((address, shifted_table))
    return tuple(result)


def check_translation():
    n = 3
    inputs = tuple(range(1 << n))
    pairs = tuple(combinations(range(n), 2))
    functions = ((None, (0, 0)), (None, (1, 1))) + tuple(
        (address, table)
        for address in range(n)
        for table in ((0, 1), (1, 0))
    )
    require(len({tuple(answer(f, x) for x in inputs) for f in functions}) == 8,
            "answer functions are not eight distinct canonical functions")
    counts = Counter()
    for strategy in product(functions, repeat=len(pairs)):
        counts["strategies"] += 1
        original_distances = [wrong_count(strategy, x, pairs) for x in inputs]
        ball_sizes = [sum(wrong <= threshold for wrong in original_distances)
                      for threshold in range(len(pairs) + 1)]
        mask_distances = []
        for mask in inputs:
            shifted = translate(strategy, mask, pairs)
            for old, new in zip(strategy, shifted):
                require(old[0] == new[0], "translation changed a raw address")
                require(new in functions, "translation left the strategy class")
                counts["address_checks"] += 1
            distances = []
            for x in inputs:
                for old, new, pair in zip(strategy, shifted, pairs):
                    old_error = answer(old, x ^ mask) != target(x ^ mask, pair)
                    new_error = answer(new, x) != target(x, pair)
                    require(old_error == new_error,
                            "translation changed a pair's correctness")
                    counts["pair_error_checks"] += 1
                distance = wrong_count(shifted, x, pairs)
                require(distance == original_distances[x ^ mask],
                        "translated total distortion is incorrect")
                distances.append(distance)
                counts["distortion_checks"] += 1
            mask_distances.append(distances)
        for x in inputs:
            for threshold, size in enumerate(ball_sizes):
                hits = sum(distances[x] <= threshold
                           for distances in mask_distances)
                require(hits == size,
                        "uniform-mask hit count does not equal ball size")
                counts["uniform_hit_checks"] += 1
    require(counts["strategies"] == 512, "incomplete strategy enumeration")
    return {"n": n, "canonical_functions_per_query": len(functions),
            "wrong_pair_thresholds": list(range(len(pairs) + 1)), **counts}


def check_mandatory_parity():
    inputs = tuple(range(8))
    pairs = tuple(combinations(range(3), 2))
    # A zero-bit summary has one possible label, not zero labels.
    # The fixed parity flag is 0. The purported pair decoder reads the
    # complementary coordinate. Infinite parity penalty is represented by
    # exclusion from the success set, so arithmetic remains integer-only.
    parity_flag = 0
    good_inputs = []
    pair_checks = 0
    for x in inputs:
        errors = 0
        for pair in pairs:
            complement = next(k for k in range(3) if k not in pair)
            decoded = (x >> complement) & 1
            correct = decoded == target(x, pair)
            require(correct == (x.bit_count() % 2 == 0),
                    "complementary probe parity behavior is incorrect")
            errors += not correct
            pair_checks += 1
        if x.bit_count() % 2 == parity_flag and errors == 0:
            good_inputs.append(x)
    require(good_inputs == [0, 3, 5, 6],
            "infinite-penalty code does not succeed on exactly even inputs")

    # Exhaust every parity decoder of the single zero-bit memory label.
    parity_decoder_checks = 0
    for constant_output in (0, 1):
        errors = 0
        for x in inputs:
            errors += constant_output != x.bit_count() % 2
            parity_decoder_checks += 1
        require(errors == 4, "a zero-bit summary recovered exact parity")
    return {"summary_bits": 0, "memory_labels": 1,
            "pair_checks": pair_checks,
            "infinite_penalty_success_inputs": good_inputs,
            "success_numerator": len(good_inputs), "success_denominator": 8,
            "constant_parity_decoders_rejected": 2,
            "parity_decoder_input_checks": parity_decoder_checks}


def main():
    print(json.dumps({"status": "passed", "arithmetic": "exact integer",
                      "translation": check_translation(),
                      "mandatory_parity": check_mandatory_parity()},
                     sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
