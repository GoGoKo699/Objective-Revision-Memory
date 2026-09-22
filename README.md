# Objective Revision Memory

**How much must a system remember to implement a later rule change when it can reread only one original fact?**

This is a classical, theorem-led project on delayed pair-parity revision. An input has $n$ bits. A stored summary must reproduce their total parity exactly. A later query excludes two specified coordinates; the decoder sees the entire summary and may reread one raw bit from an external archive. It understands and accepts the new rule. The problem is the information needed to execute it.

**Current status:** a matching converse and construction now determine the unrestricted asymptotic memory rate in this model. Written proofs and reproducible small checks are available. Novelty, independent mathematical review, and publication significance remain unresolved. This is AI-assisted exploratory research, not a manuscript release or an AI-safety theorem.

## Main result: a sharp rate, not just bounds

Fix revised-query error $0<\varepsilon<1/2$. Let $a>0$ solve

$$1-2\varepsilon=2\int_0^1u\tanh(au)\,du.$$

Then

$$\lim_{n\to\infty}\frac{B_{\rm all}(n,\varepsilon)}n
=\mathcal R(\varepsilon)
=\frac{a(1-2\varepsilon)-\ln\cosh a}{\ln2}.$$

The achieving principle is **graded storage**: reconstruct some facts more accurately than others, then reread the less accurately represented endpoint of a query. A rank-profile and entropy converse proves that no arbitrary encoding or memory-dependent one-bit address can improve the leading rate.

The scalar curve is an established weighted binary coding law, and the entropy ingredient comes from an entropic proof of Chang's inequality. The candidate contribution is the pair-query problem's equality with that coding optimum despite allowing arbitrary summary-dependent probe addresses. The [proof and novelty audit](docs/reviews/SHARP_RATE_AUDIT.md) found no central proof defect; historical priority remains unresolved.

Start with the compact [theorem and contribution brief](docs/THEOREM_BRIEF.md) for the mathematical claim, proof structure, and limits. It explains why endpoint reads attain the same leading rate, while arbitrary-coordinate reads retain a logarithmic advantage at zero error. Preserving the original total parity adds at most one bit to the corresponding pair-query problem.

| Revised error | Unrestricted rate | Optimal affine rate |
| --- | ---: | ---: |
| 1% | 0.81497 | 0.85858 |
| 10% | 0.42208 | 0.55279 |
| 25% | 0.14392 | 0.29289 |

Rates are limiting summary bits per input bit, not finite-size optima. Affine means an encoding map over $\mathbb F_2$, with unrestricted decoding. The unrestricted rate is strictly smaller for every fixed error in the open interval.

The [current research note](RESEARCH_NOTE.md) contains the complete converse, construction, quantifiers, and limits. The [baseline note](BASELINE_NOTE.md) is preserved unchanged for the exact optimum $n-\lfloor\log_2(n+1)\rfloor$, affine rate $1-\sqrt{2\varepsilon}$, and original finite examples. Its earlier open-rate statements are superseded by the current note. With two raw rereads, one retained parity bit still suffices exactly.

## Evidence and navigation

The [status](docs/STATUS.md) separates mathematical progress from novelty. The [literature comparison](docs/LITERATURE_COMPARISON.md) credits established ingredients and records unfinished comparisons. The [reproduction guide](docs/REPRODUCIBILITY.md) documents exact checks versus numerical checks; the [source manifest](docs/SOURCE_MANIFEST.json) traces the unchanged imported baseline files.

The [rank-profile continuation](docs/RANK_PROFILE_EXTENSIONS.md) isolates the general entropy argument, sharpens low-rank pair coverage, and proves the corresponding matching/cover rate for bipartite query graphs. It distinguishes mathematical deductions from unresolved priority claims.

The new finite certificate says that 529 bits suffice at $n=1024$ and revised error below 10%, whereas every affine summary needs at least 565 bits at the same target. The 529-bit upper bound uses a proved existence bound for Hamming covers; those large covers have not been built.

The [conjunction/refinement exploration](explorations/conjunction/research_note.md) is a separate model, not an earlier version of the parity theorem. It remains unchanged.

## Reproduce

Python 3.10+, standard library only. No installation, network, training, GPU, or large simulation is needed.

```sh
python checks/run_all.py
python checks/run_all.py --include-conjunction
```

The runner reproduces the original exact and bounded-error reports plus the sharp-rate report, checks source hashes and documentation links, and guards raw-read interfaces. Temporary outputs do not overwrite committed evidence. Integer ranks, truth tables, and finite probabilities are exact; entropy and integral evaluations have documented floating-point tolerances. Passing checks is neither proof by finite extrapolation nor a novelty certificate.

## Boundaries and license

The raw archive is not included in the summary size. Public input-independent randomness and unlimited local computation are uncharged. Each read returns one original bit. There is no free cache of earlier queries. The construction guarantees accuracy for each fixed input and fixed pair over the public seed, not simultaneous correctness or an adversarial pair chosen after seeing the seed and summary. The full model is in the research note.

The motivating fiction and private conversation are not republished. The finite parity model does not establish claims about consciousness, human values, or the behavior of deployed language models. Ordinary coding constructions and the systematic access model are credited to prior work.

[MIT](LICENSE), Copyright (c) 2026 Ruge Lin. The original license is unchanged.
