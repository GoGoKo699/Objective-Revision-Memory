# Objective Revision Memory

**Sharp memory limits for delayed pair-parity queries with one raw-bit read.**

An encoder summarizes an immutable binary archive before knowing which pair of
coordinates will be queried. The decoder can inspect the entire summary and
reread one original bit. How much summary memory is necessary to answer the
pair's parity approximately? In the revision version, the summary must also
recover the archive's total parity exactly, and the query asks for that parity
with the two coordinates excluded.

The written result determines the leading memory rate, allowing arbitrary
nonlinear summaries and summary-dependent read addresses. A fixed endpoint
rule achieves the same rate. Retaining the original total parity adds at most
one bit to the direct pair-parity problem.

**Manuscript preparation is on hold.** Potential collaborators interested in
this project are welcome to contact **Ruge Lin** at
[gogoko699@gmail.com](mailto:gogoko699@gmail.com).

**Research stage:** complete written proof and a completed bounded assessment
of novelty and significance. The [contribution assessment](docs/CONTRIBUTION_ASSESSMENT.md)
supports a focused theoretical contribution: the sharp extremal bound over all
legal one-read strategies. Its precise claim and limits are recorded there.
This repository is an AI-assisted research record.

## Start here

| Your purpose | Entry point |
| --- | --- |
| Understand the question, resources, and a four-bit example | [Reading guide](docs/READING_GUIDE.md) |
| Check the central theorem and its complete proof | [Pair-query proof note](docs/PAIR_QUERY_NOTE.md) |
| Assess novelty and conceptual significance | [Contribution assessment](docs/CONTRIBUTION_ASSESSMENT.md), [literature comparison](docs/LITERATURE_COMPARISON.md), and [audit](docs/reviews/SHARP_RATE_AUDIT.md) |
| See current findings and remaining research decisions | [Status](docs/STATUS.md) and [research roadmap](docs/RESEARCH_ROADMAP.md) |
| Reproduce the small checks | [Reproducibility guide](docs/REPRODUCIBILITY.md) |
| Contribute a proof correction, comparison, or extension | [Contributing](CONTRIBUTING.md) |

The reading guide gives a suggested 30-minute orientation and a map of the
proof dependencies. The full proof requires additional study.

## The model

For an archive $`X\in\{0,1\}^n`$, with $`n\ge3`$, retain at most $`B`$
input-dependent bits before learning an unordered pair $`\{i,j\}`$.
The revision answer is $`p(X)\oplus X_i\oplus X_j`$, where $`p(X)`$ is total
parity and must be exactly recoverable from the summary and seed alone.

| Resource | Accounting |
| --- | --- |
| Retained information | At most $`B`$ bits in the worst case, including exact original parity |
| Immutable original archive | Outside the summary budget; accessible through the raw-read interface |
| Query access | At most one original coordinate bit; address may depend on summary, query, and independent coins |
| Computation and summary access | Unrestricted |
| Codebooks and input-independent randomness | Uncharged |
| Input-dependent caches or earlier transcripts | Charged to memory |

The original error promise is at most $`\varepsilon`$ for **each fixed pair**,
averaged over uniform input and independent coins. The converse needs only
input-and-pair average error. Public symmetrization gives an attaining scheme
with the stronger guarantee for **each fixed input and pair**, averaged over
the seed. Neither guarantee permits an adversarial pair selected after seeing
the seed and summary. A computed one-bit answer from the archive is a different
access resource from a raw coordinate read.

## The sharp result

Fix $`0\lt \varepsilon\lt 1/2`$, and let $`a\gt 0`$ solve

```math
1-2\varepsilon=2\int_0^1u\tanh(au)\,du.
```

Then the optimal revision summary size satisfies

```math
\lim_{n\to\infty}\frac{B_{\rm all}(n,\varepsilon)}n
=\mathcal R(\varepsilon)
=\frac{a(1-2\varepsilon)-\ln\cosh a}{\ln2}.
```

Arbitrary-coordinate reads, endpoint-only reads, and endpoint addresses
chosen using only the query and public seed all have this leading rate.

The proof isolates a more precise object. Fix an entire decoder strategy and
count the inputs on which it gets at most an $`\varepsilon`$ fraction of pairs
wrong. The largest such input set has fraction
$`2^{-n\mathcal R(\varepsilon)+o(n)}`$. An ordered-endpoint strategy attains that
exponent through a weighted Hamming ball. This extremal evaluation is the
proposed original contribution; general lossy coding converts it into the
memory rate, worst-input covering rate, and below-rate success exponent.

The complete argument is in the [pair-query note](docs/PAIR_QUERY_NOTE.md).
The [original sharp-rate proof](RESEARCH_NOTE.md) gives the graded block-cover
construction and the same expected-error theorem. The
[operational reduction](docs/OPERATIONAL_REDUCTION.md) records exact comparisons
with general distortion coding and decoder-controlled side information.

| Revised error | Unrestricted leading rate | Optimal affine leading rate |
| --- | ---: | ---: |
| 1% | 0.81497 | 0.85858 |
| 10% | 0.42208 | 0.55279 |
| 25% | 0.14392 | 0.29289 |

Rates are limiting summary bits per archive bit at fixed error. Affine refers
to the encoding map over $`\mathbb F_2`$, with unrestricted decoding. These
rounded values illustrate the analytic result; they are not finite-size optima.

At zero error, arbitrary reads need exactly
$`n-\lfloor\log_2(n+1)\rfloor`$ bits, while endpoint-only reads need $`n-1`$.
Thus leading-rate equivalence does not imply finite equivalence. The
[preserved baseline](BASELINE_NOTE.md) and
[endpoint comparison](docs/THEOREM_BRIEF.md) contain these proofs.

## What the evidence establishes

The written proof has survived the recorded internal checks without a central
defect being found. The systematic access model, elementary geometric count,
entropy inequality, weighted coding curve, and general coding conversions
have explicit antecedents. The completed assessment identifies concrete
limitations of close prior reductions and gives a positive case for a focused
theoretical paper. This
is a bounded research judgment, not a guarantee of historical priority or
publication. Independent human review has not been obtained.

The deterministic covering result controls the **fraction of wrong pairs on
every input**, each hypothetical query with its own one-read budget. Its
below-rate success criterion replaces the original marginal-error promise.
It does not require a single execution to answer all pairs with one total read.
See the [error-quantifier table](docs/READING_GUIDE.md) and
[excess-distortion proof](docs/EXCESS_DISTORTION.md).

No efficient implementation of the asymptotic covering codes is claimed.
The finite 529-versus-565-bit comparison at $`n=1024`$ and error $`1/10`$ is a
covering-existence certificate versus an affine lower bound; the large cover
has not been constructed. Finite-length optima, second-order behavior, and
error varying with $`n`$ remain separate questions.

## Reproduce

From the repository root, use Python 3.10+ with its standard library:

```sh
python3 checks/run_all.py
python3 checks/run_all.py --include-conjunction
```

No installation, network access, training, GPU, or large simulation is needed.
Run without `-O`. The runner checks imported source hashes, documentation links,
raw-read interfaces, and temporary reproductions of the recorded reports.
The [reproduction guide](docs/REPRODUCIBILITY.md) separates exact checks from
floating-point illustrations and lists the optional audit checks. Passing
finite checks supports specific calculations, not general proof or novelty.

## Research record and scope

The [reading guide](docs/READING_GUIDE.md) indexes the current proof, extensions,
audit history, and preserved baseline. Historical open-gap language in
[BASELINE_NOTE.md](BASELINE_NOTE.md) is superseded by the sharp-rate proof.
The [source manifest](docs/SOURCE_MANIFEST.json) records unchanged imported
artifacts. The [conjunction exploration](explorations/conjunction/research_note.md)
uses a separate model.

The project studies a classical information constraint for a specified query
family. It makes no theorem-level claim about consciousness, human values, or
deployed AI systems. Private conversations and the motivating fiction are not
republished.

[MIT license](LICENSE), Copyright (c) 2026 Ruge Lin.
