# Objective Revision Memory

**How much information must a system retain to implement a later rule change when it can reread only one original fact?**

This is a classical, theorem-led research project about delayed rule revision under limited factual access. The active model starts with an $n$-bit input and its total parity. After a summary has been stored, a query asks for the same parity with two specified coordinates excluded. The decoder accepts the revision, has free access to the entire summary, and may reread one individual bit from an external archive.

The distinction is between **accepting a correction** and **having the information needed to execute it**. Parity is a finite test case, not a model of human values or natural-language understanding.

**Research status:** written proofs and reproducible finite checks; novelty and publication significance remain under investigation. No manuscript, release, independent expert validation, or proof-assistant certification is claimed. This repository contains AI-assisted exploratory research.

## Main results

Let $B$ be retained input-dependent bits, $N=\binom n2$, $h_2$ binary entropy, and $\Phi_n(B)=nB-B(B-1)/2$. Revised-query error is at most $\varepsilon<1/2$ under the quantifiers in the [model](RESEARCH_NOTE.md#1-model-and-accounting).

| Result | Statement | Evidence |
| --- | --- | --- |
| Exact one-reread optimum | $B=n-\lfloor\log_2(n+1)\rfloor$ | Arbitrary-encoder lower bound and matching affine construction |
| Arbitrary summaries, bounded error | $N[1-h_2(\varepsilon)]\leq\Phi_n(B)$ | Rank-coverage lemma and weighted entropy argument |
| Affine summaries, bounded error | $N(1-2\varepsilon)\leq\Phi_n(B)$ | Uniform-affine-cell converse |
| Sharp affine leading rate | $B_{\mathrm{aff}}=[1-\sqrt{2\varepsilon}]n+O(1)$ | Matching public-random-subset construction |
| Nonlinear advantage | At $n=49$ and error $11/32$, eight nonlinear bits suffice; every affine scheme needs at least nine | Block majority plus exact rational converse arithmetic |
| Two rereads | One retained parity bit suffices with zero error | Read the two excluded input bits |

The unrestricted leading rate is not determined. Known random access coding gives an upper bound within a factor of two of the current converse coefficient. The access model, majority coding, and entropy-rate coding ingredients are established; the [literature comparison](docs/LITERATURE_COMPARISON.md) identifies what remains to be checked for originality.

## Read and check

Start with the [research note](RESEARCH_NOTE.md) for definitions and complete arguments. The [research status and next steps](docs/STATUS.md) separates proof status, computational evidence, and novelty. The [reproduction guide](docs/REPRODUCIBILITY.md) explains every test and its limits. Original verification code and outputs are traced by the [source manifest](docs/SOURCE_MANIFEST.json).

The earlier **conjunction/refinement model is a separate exploration**, not an earlier version of the parity theorem. Its [own note and certificates](explorations/conjunction/research_note.md) are retained separately. The two models must not share memory bounds or error claims without a new argument.

## Reproduce locally

Python 3.10 or newer; standard library only. No installation, network access, training data, GPU, or cloud simulation is needed for the checks.

```sh
python checks/run_all.py
```

This runs the exact parity and bounded-error suites, compares regenerated reports with the committed reports, checks documentation links and source hashes, and tests the raw-read interfaces. Include the separate exploration with:

```sh
python checks/run_all.py --include-conjunction
```

All temporary reports are written outside the checkout. Binary algebra, truth tables, finite probabilities, and the numerical separation examples use exact arithmetic. Entropy evaluations use floating-point logarithms with a stated tolerance. Passing tests is not a proof by finite extrapolation or a novelty certificate.

## Boundaries

The original $n$-bit archive is **not** included in $B$. A reread returns one raw bit, not a word or an arbitrary function. Public randomness is input-independent and is available to both encoder classes; its physical storage is not charged. There is no free cache of earlier query results. Preprocessing and local computation are unrestricted. Guarantees for each fixed input and query over a public seed do not imply simultaneous success, or security against choosing a query after seeing that seed and the memory.

In this project, affine means that the **encoding map is affine over $\mathbb F_2$**. The decoder is unrestricted. This is different from asking whether a reconstruction codebook is linear.

The motivating fiction is not republished here. It motivates the question but does not establish the added compression model or any theorem. Neither consciousness, resistance to shutdown, nor the behavior of contemporary AI systems is proved by this work.

## License

[MIT](LICENSE), Copyright (c) 2026 Ruge Lin. The owner's original license is preserved unchanged. Literature is cited, not relicensed or included as third-party source code.
