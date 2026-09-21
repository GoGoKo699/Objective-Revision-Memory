# Reproduce and interpret the checks

Use Python 3.10+ with assertions enabled. All scripts use only the standard library. No network, GPU, external solver, or training run is used.

```sh
python checks/run_all.py
python checks/run_all.py --include-conjunction
```

The wrapper checks imported source hashes, local Markdown file links, expected report contents, and raw-probe interfaces. It runs scripts in temporary directories and never overwrites committed reports. Assertions must not be disabled: `python -O` is rejected by the wrapper. The bounded-error source script is preserved unchanged; always use the wrapper for the complete guarded workflow.

## Exact parity

[verify_exact.py](../checks/verify_exact.py) is unchanged from the original exact checkpoint. It enumerates all nonempty fixed-parity memory cells for input lengths 3, 4, and 5, tests exact decodability directly, and checks constructions through length 15. It checks 341,375 coefficient identities over all lengths 3 through 127. The recorded output is [exact_parity.json](../results/exact_parity.json).

The decoder in this script uses one-indexed raw coordinates. It also checks arbitrary parity queries at length 7. All arithmetic is exact.

## Bounded-error parity

[verify_bounded_error.py](../checks/verify_bounded_error.py) is unchanged from checkpoint v2. It checks 32,494 binary subspaces through dimension 7 and 131,610 fixed-parity cells through length 5. It executes 1,540,672 complete majority-decoder input-query cases and another 71,680 public-mask symmetry cases. The report is [bounded_error.json](../results/bounded_error.json).

This script's raw coordinates are zero-indexed. The wrapper tests both conventions rather than silently treating them as identical. Finite separation arithmetic and probabilities use integers and `Fraction`. Entropy computations use ordinary floating point with tolerance $10^{-10}$; they are sanity checks, not interval certificates.

The source verifier's `PASS` is a finite-check result. Neither the general theorems nor historical originality follows from finite enumeration. The covering-code existence upper bound is not implemented as a large-code construction.

## Separate conjunction exploration

[verify.py](../explorations/conjunction/verify.py) is imported unchanged. It writes results beside its script, so the wrapper copies it into a temporary directory before running it. Both its [report](../explorations/conjunction/verification_results.json) and [four-feature decoder](../explorations/conjunction/four_feature_decoder.json) are compared with the committed copies.

It checks 87,380 record-subset pairs for the count-summary construction and every nonempty candidate cell through four features. Its affine tests use exact decision-tree dynamic programming. This is a different query family, not a parity regression test.

## How outputs are compared

Integers, strings, Boolean flags, array lengths, and object keys must agree exactly. JSON floating-point fields may differ by at most $10^{-10}$ relative or absolute tolerance to accommodate platforms' elementary-function rounding. The initial local reruns of both parity suites were additionally byte-identical to the original reports; that is a narrower, environment-specific observation.

Imported source and report provenance is recorded in [SOURCE_MANIFEST.json](SOURCE_MANIFEST.json). The manifest identifies original conversation archives without embedding them. Public research notes consolidate those sources editorially; code and reports listed as unchanged are byte-preserved. The source fiction PDF and private conversation are not published.

## Continuous integration

The [workflow](../.github/workflows/verify.yml) runs the same full wrapper, including the separate exploration, on Ubuntu 24.04. It uses read-only repository permissions and a pinned checkout action. A configured workflow is not evidence of a successful run: consult the actual Actions result for the relevant commit. No scheduled monitoring, benchmarks, or publication automation is installed.
