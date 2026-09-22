# Novelty and significance assessment

Completed 22 September 2026 against main
`2b240fa20b9c8d585106edb512a5f18200aafd33`.
The [central proof](PAIR_QUERY_NOTE.md), [comparison ledger](LITERATURE_COMPARISON.md),
and [audit](reviews/SHARP_RATE_AUDIT.md) supply the mathematical and source detail.

## Decision

**Retain the sharp one-read pair-query theorem as the proposed original
contribution of a focused theoretical paper.** The completed comparisons
support that scope: no identified prior implication evaluates the same
extremal quantity with the same resources. The positive significance case is
that a complete optimization over nonlinear summaries and arbitrary read
addresses has a sharp answer attained by a fixed endpoint rule.

This is a bounded research judgment. It does not claim exhaustive historical
knowledge, independent human validation, or guaranteed publication. It does
resolve the project's present proceed/reframe/stop question in favor of the
narrow result. Reopen the decision for a concrete new citation, reduction,
counterexample, or substantive significance objection; another indefinite
general search is not the default next step.

**Manuscript preparation remains on hold.** Potential collaborators are
welcome to contact Ruge Lin at
[gogoko699@gmail.com](mailto:gogoko699@gmail.com). The research decision does
not start manuscript drafting or external correspondence.

## The precise contribution

For each fixed $`0<\varepsilon<1/2`$, let $`m_n(\varepsilon)`$ be the largest
fraction of $`n`$-bit inputs on which one complete decoder strategy answers at
least a $`1-\varepsilon`$ fraction of pair-parity queries correctly. Each query
has its own one-raw-coordinate-read budget. The address and the Boolean
answer function may be different for every pair.

The theorem evaluates

```math
m_n(\varepsilon)=2^{-n\mathcal R(\varepsilon)+o(n)},
```

where an ordered-endpoint weighted Hamming ball attains the same exponent.
The rate $`\mathcal R`$ is defined in the central note. A retained memory label
selects a strategy, which accounts for arbitrary nonlinear encoders and
summary-dependent addresses. The original revision task additionally requires
exact total parity from memory and seed alone; every construction charges
that requirement, including on unsuccessful inputs.

The proposed contribution is this **task-specific extremal evaluation** and
the resulting absence of a leading-rate advantage from unrestricted
addressing. The memory-rate, deterministic worst-input covering rate, and
below-rate success exponent are grouped consequences, obtained through
established coding conversions. They are not three independent discoveries.

The original marginal-error promise and the table-success criterion are
different optimizations. The former requires the stated error for each fixed
pair, averaged over uniform input and independent coins. The latter measures
the chance that an input's whole answer table has at most an $`\varepsilon`$
fraction of errors, with separate read budgets for its entries. Their common
rate does not make their finite guarantees interchangeable. All limiting
claims here keep error fixed in the open interval.

## What the comparison establishes

| Comparison | Established content | What still requires the pair-query argument |
| --- | --- | --- |
| Systematic structures, common bits, and header-based local decoding | Preprocessing plus locally accessed information, including freely read metadata, are established models. | The optimum for all overlapping pair parities at positive distortion. |
| Entropic Chang and elementary quotient bases | Independent-character entropy costs and the geometric count have classical derivations. | Combining the all-subsets incidence envelope with the full bias profile, then showing matching endpoint attainment. |
| Weighted binary source coding | The scalar curve and logistic quality allocation are established. | Proving that arbitrary one-read strategies cannot outperform that weighted problem. |
| General distortion coding and decoder actions | A strategy is a valid reproduction object; general formulas characterize related coding problems. | Evaluating this particular strategy-ball volume. The exact action embedding retains the distinction between repeated fixed archives and one growing archive. |
| Exact rank, matching products, and generic polynomial tails | These give valid ingredients or bounds. | The recorded reductions lose leading-order information; they do not yield the sharp exponent. |

The latest primary-source checks make two boundaries more explicit. Local
compression with a freely read header is a closer precedent than ordinary
encoded-bit locality alone. Counting a ball by the entropy of its uniform
distribution is also established. Neither architectural description nor
entropy-on-a-good-set methodology should be presented as new. The
[ledger](LITERATURE_COMPARISON.md), Sections 13 onward, records the theorem
locations, exact substitutions, and their failures. It also examines the
bounded-error linear-operator literature rather than dismissing that field
as exact-only.

These are bounded statements about inspected results and explicit
reductions. They do not prove that no more elaborate implication exists.
Inaccessible theorem texts remain marked uninspected in the ledger; absence
of access is not favorable novelty evidence.

## Why the result is worth a focused paper

**It settles the stronger optimization.** Designing a graded endpoint scheme
alone would largely be a weighted-coding application. The converse permits
the encoder to partition the cube arbitrarily and the decoder to read any
coordinate selected using the summary. Matching that optimum establishes
which apparent extra freedom does not help at the leading rate.

**It explains why overlapping queries matter.** Full residual rank and
zero-error fiber size do not determine approximate volume: two legal tables
with the same values have different exponential good-set sizes. A matching
uses only a disjoint subset of the queries and yields a strictly weaker
bound. The proof retains the incidence of all overlapping pair labels;
discarding those labels permits the explicit subexponential-tail obstruction
in the audit. Thus the reduction to weighted endpoint errors supplies actual
content beyond naming a familiar rate function.

**Its sharpness has an operational interpretation.** At fixed positive error,
memory-dependent nonendpoint access has no leading advantage. At zero error,
the known finite endpoint and unrestricted optima differ by
$`\lfloor\log_2(n+1)\rfloor-1`$ bits. This distinguishes asymptotic equivalence
from exact simulation. The result can serve as a solved benchmark when
studying approximate systematic queries; that is a mathematical use, not a
demonstrated deployment benefit.

**Its scope fits its proof.** One explicit query family, one central extremal
theorem, and a short chain of coding consequences form a coherent contribution.
Established methods do not disqualify a new sharp result, but their use limits
the methodological claims. Large simulations would not strengthen either the
proof or the historical comparison.

## Strong objections and the claims they rule out

| Objection | Consequence for the assessment |
| --- | --- |
| The query family is specialized. | Claim a canonical model result; no theorem for arbitrary functions, graphs, or objective changes follows. |
| The curve and proof ingredients are established. | Credit them and lead with the unrestricted converse and matching extremum. Do not claim a new entropy method or rate-distortion framework. |
| The codebooks are existence constructions. | Claim no efficient encoder, decoder implementation, or practical memory system. |
| Original total parity costs only one extra bit. | The theorem is not evidence of an extensive cost of retaining an earlier objective. |
| The archive, computation, and independent code descriptions are uncharged. | State the systematic-access resource model visibly; this is not total physical-storage or running-time optimality. |
| Historical coverage is necessarily incomplete. | Use the precise proposed originality claim and respond to specific prior implications; do not infer priority from search failure. |

Taken together, these objections support a compact, carefully attributed
theoretical result. They would defeat a broader claim about general memory,
new coding machinery, or technological superiority. No such broader claim is
needed for the present contribution.

## What is settled, and what can change

The written proof and bounded source comparison are complete at this
checkpoint, and the significance assessment is affirmative at the stated
scope. Independent specialist feedback can strengthen or overturn this
judgment; it is not represented as already obtained or left as a substitute
for making a decision now.

If a resource-preserving prior theorem implies the same extremum, replace
the proposed originality claim with an attributed worked example and reassess
its value. If a mathematical defect is identified, record the smallest
obstruction and revise the affected conclusions. Optional extensions should
answer a concrete scientific question, rather than enlarge a paper to avoid
either outcome. The [roadmap](RESEARCH_ROADMAP.md) keeps collaboration and
manuscript status separate from these scientific judgments.
