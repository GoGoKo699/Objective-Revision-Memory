# Research roadmap toward Information Processing Letters

Decision recorded 22 September 2026. Scientific base:
`fe445bf94149b0b9ca3389816ddcc36e883aaf51` (merged PR #8).

**The selected target is Information Processing Letters (IPL). Manuscript
preparation is the final research step.** The current deliverable is a usable
research repository: precise claims, complete proofs, a comparison ledger,
bounded verification, and explicit remaining decisions. The existing
[pair-query note](PAIR_QUERY_NOTE.md) is an internal proof reference.

## Why this target fits

IPL's [publisher description](https://shop.elsevier.com/journals/information-processing-letters/0020-0190)
welcomes focused contributions to fundamental information processing and
theoretical computer science. It states a general limit of nine printed pages
(checked 22 September 2026). This favors one sharp theorem and its closely
connected consequences. The page limit will guide the eventual manuscript;
it does not require compressing the research record or starting a draft now.

Relevant format precedents include Smal and Talebanfard,
[*Prediction from Partial Information and Hindsight, an Alternative Proof*](https://doi.org/10.1016/j.ipl.2018.04.011),
IPL 136 (2018), 102–104, and Rioul and Solé,
[*An Information Theoretic Proof of the Chernoff–Hoeffding Inequality*](https://doi.org/10.1016/j.ipl.2025.106582),
IPL 190 (2025), 106582. These indicate an audience for concise prediction and
entropy arguments. They do not establish this result's originality or predict
acceptance. The latter is a venue precedent here, not a completed theorem-level
priority comparison.

## The result whose contribution we must assess

Fix $0<\varepsilon<1/2$. For a complete one-read strategy $t$, let
$D_n(x,t)$ be the fraction of pair-parity queries it answers incorrectly on
$x$, with each query considered separately under its own one-read budget.
Define

$$m_n(\varepsilon)=\max_t2^{-n}|\{x:D_n(x,t)\le\varepsilon\}|.$$

The candidate theorem is

$$m_n(\varepsilon)=2^{-n\mathcal R(\varepsilon)+o(n)},$$

with the same exponent attained by ordered-endpoint weighted Hamming balls.
The summary selects a strategy, so arbitrary nonlinear preprocessing and
summary-dependent addresses are included. General coding then gives the
memory-rate, covering, and success-exponent consequences. The exact original
parity requirement in the revision task costs at most one additional bit.

The conceptual question is whether this sharp equivalence of unrestricted
and fixed endpoint access is a useful new result for a canonical overlapping
query family. The geometry, entropy budget, scalar curve, and general coding
conversions are established ingredients, as recorded in the
[literature comparison](LITERATURE_COMPARISON.md). Broad claims about objective
preservation are not supported by the one-bit parity overhead.

## Work sequence and completion evidence

| Stage | Current state | Evidence needed to finish |
| --- | --- | --- |
| 1. Furnish the research repository | Complete in this documentation update | One clear reading route, complete model and error ledger, proof map, current status, reproducibility instructions, and preserved provenance |
| 2. Close concrete proof concerns | Complete written argument; recorded internal audit found no central defect | Resolve any specific objection against a pinned commit, with a proof correction or counterexample if needed; preserve all resource and error quantifiers |
| 3. Assess novelty precisely | Bounded primary-source comparisons completed; operational priority remains open | A defensible statement of what the closest inspected theorems imply, what remains beyond those implications, and which material uncertainties persist |
| 4. Decide significance for IPL | Focused contribution identified; publication judgment remains open | Explain why the sharp access equivalence is worth knowing, separately from correctness and search non-detection; record a proceed, reframe, or stop decision |
| 5. Prepare the manuscript | Deferred; final step | Use the settled contribution and evidence to write one coherent paper within the journal's then-current requirements |

Stages 2–4 can inform one another. Repeated automated agreement is not
independent human validation, and exhaustive certification of all historical
priority is not a realistic completion condition. Equally, an unsuccessful
search is not evidence that the theorem is new. A focused specialist assessment
can inform the decision; no external contact is initiated by this roadmap.

If a prior theorem supplies the full result through a checked reduction,
record that implication and assess the value of an attributed worked example.
If the remaining contribution is too slight, record that finding. Neither
outcome should trigger unrelated extensions merely to enlarge a paper.

## The next research action

Use the completed proof packet and comparison ledger to make a bounded
assessment of the **specific decoder-ball theorem**. A useful assessment
answers these questions:

1. Does a close theorem evaluate this same good-input fraction, or imply it
   after charging the whole summary, raw reads, and input-dependent data?
2. Does that implication preserve the growing single-archive limit and the
   relevant error criterion, rather than replacing it with repeated archives,
   independent disjoint queries, or a pooled read budget?
3. What does the arbitrary-address converse establish beyond solving the
   familiar weighted endpoint coding problem?
4. Is that conclusion significant enough for a focused theoretical letter,
   with established ingredients clearly credited?

The [audit](reviews/SHARP_RATE_AUDIT.md), Section 12, and
[literature ledger](LITERATURE_COMPARISON.md), Sections 10–12, are the starting
material. The remaining issue is
[issue #1](https://github.com/GoGoKo699/Objective-Revision-Memory/issues/1).
Its original checklist predates several completed comparisons; read the
latest handoff and ledger before repeating work. Issue #2 records the written
resolution of the rate gap, not an independent correctness certificate.

Do not restart general searches for novelty in elementary basis counting or
standard lossy coding. Follow a concrete candidate implication when one is
identified. An inaccessible paper must remain marked uninspected; absence of
access supports neither subsumption nor non-subsumption.

## Optional extensions and final-step boundary

Finite-length optimality, explicit efficient codes, a full finite pair-coverage
envelope, second-order terms, and error parameters varying with $n$ are
separate research questions. Pursue one only when it resolves a specific
obstruction or strengthens the conceptual contribution. None is automatically
required for an IPL paper. Large simulations do not answer the present
priority or significance question.

The immediate work is research and repository maintenance. Journal-formatted
drafting, a submission package, and a manuscript release belong after the
recorded contribution decision. Submission or correspondence with researchers
is a separate action. The [contribution guide](../CONTRIBUTING.md) describes
the branch, verification, and handoff workflow.
