# Reading guide

Start with the [self-contained pair-query note](PAIR_QUERY_NOTE.md). It contains
the complete central proof and is the main technical entry point. This guide
explains the model, provides a small example, and locates supporting material.
It is research onboarding; manuscript preparation comes later under the
[research roadmap](RESEARCH_ROADMAP.md).

## What to bring

A mathematically trained reader needs:

- Binary arithmetic: XOR is addition in $\mathbb F_2$; parity is the XOR of bits.
- Linear algebra: rank, bases, quotient spaces, and invertible coordinate changes.
- Basic probability: expectation, variance, independence, and Chebyshev's inequality.
- Shannon entropy, conditional entropy, and binary entropy
  $h_2(p)=-p\log_2p-(1-p)\log_2(1-p)$.
- Elementary calculus and asymptotics: Riemann sums, integration by parts,
  and the distinction between $o(n)$ bits and a fixed number of bits.

Prior expertise in matroids, coding theory, or data structures is helpful but
not required to follow the note's proof. Its coding constructions are existence
arguments; there is no large simulation or training pipeline to learn.

## A 30-minute orientation

This route is for understanding the question, claim, and evidence boundaries,
not mastering or verifying every proof step in half an hour.

| Time | Read | Question to answer |
| --- | --- | --- |
| 0–5 minutes | [README](../README.md), then the resource table below | What is charged, and what can a query read? |
| 5–10 minutes | The four-bit example below; Sections 1–2 of [PAIR_QUERY_NOTE.md](PAIR_QUERY_NOTE.md) | What does a low-error input set mean? |
| 10–22 minutes | The proof map below; Sections 3–5 of the same note | How do the converse and endpoint construction meet? |
| 22–27 minutes | [Status](STATUS.md) and the conclusions in the [literature comparison](LITERATURE_COMPARISON.md) | Which facts are proved here, which ingredients are established, and what remains uncertain? |
| 27–30 minutes | [Reproducibility](REPRODUCIBILITY.md) and [research roadmap](RESEARCH_ROADMAP.md) | What can be checked locally, and what work remains before writing a manuscript? |

For a proof audit, return to the central note and check its inequalities and
quantifiers in order. The longer audit history is supporting evidence rather
than prerequisite reading.

## Resource accounting

An encoder sees $x\in\{0,1\}^n$ before learning a pair $\{i,j\}$. Write
$p(x)=\bigoplus_{k=1}^n x_k$. The revision query asks for
$p(x)\oplus x_i\oplus x_j$: parity with those two coordinates excluded.

| Resource | Rule |
| --- | --- |
| Retained summary | At most $B$ input-dependent bits in the worst case; arbitrary nonlinear encoding is allowed. |
| Original archive | Remains available externally and is not counted in $B$. The theorem is about summary size, not total physical storage. |
| Query access | At most one raw-coordinate bit per query. Its address may depend on the summary, query, and seed; it need not be a query endpoint. |
| Summary access and computation | The decoder may inspect the whole summary and compute without a time limit. |
| Random seed and codebook | Independent randomness and a fixed input-independent codebook are uncharged. The selected codeword's index is charged. |
| Original parity | Must be recoverable exactly from the summary and seed on every input, including unsuccessful inputs. Appending it costs one bit; some encodings already determine it. |
| Additional caches or transcripts | Input-dependent information is part of the summary budget. A raw read does not return an arbitrary computed Boolean function. |

The matching construction uses a smaller class than the converse permits:
publicly chosen endpoint addresses suffice at the leading rate.

## A four-bit example: why errors have different weights

Use the order $1<2<3<4$. For pair $i<j$, read $x_i$, estimate $x_j$ by a
reconstruction coordinate $z_j$, and return $p(x)\oplus x_i\oplus z_j$.
The reconstruction $z$ is selected from a fixed public codebook. Its index
and exact parity are retained; selecting $z$ does not create free storage.

Take $x=(1,0,1,1)$ and $z=(0,1,1,1)$. Then $p(x)=1$. Each row below is a
separate query execution with its own one-read allowance.

| Pair | Raw read | Correct exclusion parity | Returned answer |
| --- | --- | ---: | ---: |
| $\{1,2\}$ | $x_1=1$ | 0 | **1 (wrong)** |
| $\{1,3\}$ | $x_1=1$ | 1 | 1 |
| $\{1,4\}$ | $x_1=1$ | 1 | 1 |
| $\{2,3\}$ | $x_2=0$ | 0 | 0 |
| $\{2,4\}$ | $x_2=0$ | 0 | 0 |
| $\{3,4\}$ | $x_3=1$ | 1 | 1 |

Coordinate $j$ is estimated on exactly $j-1$ pairs. Therefore the exact
wrong-pair count is

$$6\Delta(x)=0\mathbf1\{x_1\ne z_1\}
+1\mathbf1\{x_2\ne z_2\}
+2\mathbf1\{x_3\ne z_3\}
+3\mathbf1\{x_4\ne z_4\}=1.$$

Here $\Delta(x)=1/6$, even though two reconstruction coordinates are wrong.
The first coordinate is never estimated. An error in the second coordinate
spoils one pair; an error in the fourth would spoil three. This is the
weighted Hamming error underlying the theorem. The example illustrates one
input and reconstruction, not a cover of all four-bit inputs or a finite-size
optimality claim.

## Keep the error quantifiers separate

Let $R$ denote independent random tapes and let $\Delta_R(x)$ be the fraction
of wrong pairs in the resulting answer table. Uniform input means all $2^n$
archives are equally likely; uniform pair means all $\binom n2$ pairs are
equally likely.

| Criterion | What is required | Role in the project |
| --- | --- | --- |
| Average query error | Error averaged over uniform input, uniform pair, and tapes is at most $\varepsilon$. | Sufficient hypothesis for the sharp memory converse. |
| Each fixed pair | For every pair, error averaged over uniform input and tapes is at most $\varepsilon$. | The original stated memory optimum. |
| Each fixed input and pair | For every fixed $x$ and pair, error over the public seed is at most $\varepsilon$. | Achieved by permutation and mask symmetrization. |
| Worst-input table distortion | A deterministic scheme has $\Delta(x)\le\varepsilon$ for every input. | Achieved by the weighted-ball covering construction at the same leading rate. |
| Table success probability | Maximize $\Pr_{X,R}\{\Delta_R(X)\le\varepsilon\}$ subject to the resource rules. | The success-exponent problem; it replaces the marginal-error promise rather than additionally imposing it. |

Every row retains exact original parity. A table-distortion bound permits an
$\varepsilon$ fraction of wrong pairs. It does not say that all pairs are
correct, or protect against selecting an erroneous pair after seeing the
seed and summary. The asymptotic statements hold for fixed
$0<\varepsilon<1/2$; they do not automatically cover error tending to zero.

## Proof dependency map

The full proof remains in [PAIR_QUERY_NOTE.md](PAIR_QUERY_NOTE.md).

| Step | Input | What it establishes |
| --- | --- | --- |
| Residual characters | A Boolean function of one observed bit is affine. | Each pair's correctness is a signed binary character, even for arbitrary summary cells. |
| Coverage by rank | Choose a coordinate basis in a quotient space. | Every subset of pair residuals satisfies the necessary rank-versus-pair-count bound. Full-family rank alone is insufficient. |
| Greedy biases and entropy | Sort character biases, retain an independent basis, and use entropy subadditivity. | Bounds the total correctness bias using the entire rank profile and entropy deficit. |
| Scalar optimization | Apply binary entropy conjugacy to the uniform distribution on a strategy's good set. | Gives the finite upper bound on the largest one-strategy ball $m_n(\varepsilon)$. |
| Endpoint attainment | The exact weighted-error identity and independent tilted bits with a strict distortion margin. | Gives a weighted ball with the same leading exponent as the unrestricted upper bound. |
| Coding consequences | Cover by translated balls and charge their indices plus parity; average posterior entropy for expected error. | Gives the memory rate, worst-input covering rate, and success exponent as consequences of the central ball theorem. |

The elementary basis count, entropy ingredients, and general coding conversion
are credited to prior work. The task-specific extremal evaluation is the
remaining contribution under assessment. A proof using established tools may
still establish a new result; these documents do not certify historical priority.

## Source index and preserved history

| Purpose | Canonical location |
| --- | --- |
| Complete central argument | [PAIR_QUERY_NOTE.md](PAIR_QUERY_NOTE.md) |
| Current research decisions and remaining work | [STATUS.md](STATUS.md), [RESEARCH_ROADMAP.md](RESEARCH_ROADMAP.md) |
| Established ingredients and precise prior-theorem comparisons | [LITERATURE_COMPARISON.md](LITERATURE_COMPARISON.md) |
| Exact strategy/coding reductions and resource comparisons | [OPERATIONAL_REDUCTION.md](OPERATIONAL_REDUCTION.md) |
| Earlier full derivation and additional finite accounting | [RESEARCH_NOTE.md](../RESEARCH_NOTE.md), [EXCESS_DISTORTION.md](EXCESS_DISTORTION.md) |
| Endpoint comparison and optional graph/rank refinements | [THEOREM_BRIEF.md](THEOREM_BRIEF.md), [RANK_PROFILE_EXTENSIONS.md](RANK_PROFILE_EXTENSIONS.md) |
| Versioned review findings and corrections | [SHARP_RATE_AUDIT.md](reviews/SHARP_RATE_AUDIT.md) |
| Commands, check scope, and evidence limitations | [REPRODUCIBILITY.md](REPRODUCIBILITY.md) |
| How to contribute | [CONTRIBUTING.md](../CONTRIBUTING.md) |

[BASELINE_NOTE.md](../BASELINE_NOTE.md) and
[LITERATURE_BASELINE.md](LITERATURE_BASELINE.md) preserve the earlier checkpoint.
Their old open-rate language is historical. Original scripts, recorded JSON
reports, and the [source manifest](SOURCE_MANIFEST.json) are preserved; current
proofs and Git history supply later developments. A note's reviewed commit
identifies its own checkpoint, not necessarily the current repository head.

The [conjunction/refinement exploration](../explorations/conjunction/research_note.md)
has different queries and assumptions. It is a separate exploratory model and
is not a lemma used in the parity theorem.

For a local evidence check, run `python checks/run_all.py` from the repository
root; follow the reproduction guide for optional checks. Passing these checks
does not prove a limiting theorem or establish originality. Read the analytic
argument and the stated evidence boundaries together.
