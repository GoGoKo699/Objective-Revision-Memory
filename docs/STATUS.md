# Research status

Updated 22 September 2026, following the geometric attribution and excess-distortion continuation. Reviewed main: `0e91f088cd06376458f63a20f76e2d5b507a690a` (merged PR #5). The [compact theorem brief](THEOREM_BRIEF.md) and [excess-distortion theorem](EXCESS_DISTORTION.md) give the current operational claim.

## Mathematical progress

The unrestricted leading-rate gap tracked in issue #2 is resolved by a written converse and matching construction in [RESEARCH_NOTE.md](../RESEARCH_NOTE.md). The proof also establishes existence of the full limiting optimal rate for fixed revised error strictly between zero and one half. It does not claim finite-length optimality.

The converse keeps the complete sequence of greedy independent residual biases. Entropic Chang machinery and scalar conjugacy turn the pair-subset rank envelope into a finite lower bound and its integral limit. The construction assigns graded reconstruction accuracy and rereads the less accurately represented queried endpoint. Its scalar profile is an established weighted binary rate-distortion allocation. The construction respects the previous model. Public permutation/mask symmetrization shows the three stated error optima coincide even at finite length, without extra summary bits or reads.

The [research continuation](RANK_PROFILE_EXTENSIONS.md) adds proofs of a general rank-envelope bound, a capped finite converse, and the exact low-rank pair-coverage maximum $nr-r(r+1)/2$ when $n\ge2r+2$. It also identifies the sharp rate $1-h_2(\varepsilon)$ per matching edge for bipartite query families as matching number grows, under per-edge error. These are deductions from explicit arguments and established ingredients; priority is not certified. The low-rank formula fails outside its stated range, and none of these results asserts the finite optimal memory for all pairs.

The latest comparison supplies complete classical derivations of the all-subsets geometric envelope through affine-basis sumsets and fundamental-circuit uniqueness. This is an elementary task-specific lemma, no longer an independent novelty candidate. Erdős–Gallai's matching bound also yields the separate low-rank extremum when $n\ge(5r+3)/2$. None of these attributions identifies a prior statement of the full operational memory theorem.

New endpoint comparisons sharpen the operational interpretation. Arbitrary addresses, endpoint-only addresses, and publicly chosen endpoint addresses all have the same leading rate at fixed interior error. Endpoint-only zero-error memory is exactly $n-1$, exceeding the unrestricted optimum by $\lfloor\log_2(n+1)\rfloor-1$ bits. Retaining original parity adds at most one bit relative to the direct pair-parity task. Full proofs and an endpoint finite converse are in the brief.

The strongest current operational formulation also determines the **success exponent**. Let success mean that at most an $\varepsilon$ fraction of pair queries would be answered incorrectly on an input, with each query considered separately under its own one-read budget. At memory rate $\rho$, the optimum success probability has exponent $(\mathcal R(\varepsilon)-\rho)_+$. Deterministic ordered-endpoint schemes attain it. This optimization keeps the resource and exact-parity rules but replaces the old marginal-error promise; it does not impose that promise below the rate. The same rate also supports a deterministic worst-input guarantee on the fraction of wrong pairs. Full proofs use the existing moment converse and weighted Hamming covers; no optimal failure exponent above the rate is claimed.

The old exact optimum, affine leading optimum, bounded-error inequalities, and explicit majority examples remain valid. They are preserved in [BASELINE_NOTE.md](../BASELINE_NOTE.md). Its open-rate statements and factor-two gap describe the earlier checkpoint, not current status.

## Evidence and limitations

The new standard-library verifier tests every nonempty fixed-parity cell through five bits, exact rank-profile inequalities, numerical entropy/conjugate inequalities, a fully seeded counted-read decoder, finite covering-existence arithmetic, and numerical evaluations of the curve. The old imported scripts and reports remain byte-for-byte unchanged. See [REPRODUCIBILITY.md](REPRODUCIBILITY.md).

The [audit](reviews/SHARP_RATE_AUDIT.md) reconstructed the central proof and found no defect; it did not infer correctness from passing tests. Optional exact checks now cover asymmetric reconstruction errors under public symmetrization and all 3,559 low-rank subspaces through seven bits. The latter also verifies the explicit Hamming-kernel counterexample to extending the new formula to all ranks.

A new optional check tests the endpoint construction and three-point-cell obstruction, the three-bit probe separation, and two seven-coordinate subspaces with identical full weight enumerators but different pair coverage. That counterexample identifies information lost by an ordinary weight enumerator. These checks support specified finite claims, not the general theorem or priority.

The excess-distortion check adds 2,688 executions of a four-bit-summary block construction and 534 exact rational tail inequalities for explicit nonlinear and summary-dependent decoders. It verifies finite consequences of the proof, not the asymptotic exponent by extrapolation. All original verification artifacts remain unchanged.

There is no independent expert review, proof-assistant certificate, or efficient implementation of the large covering codes. Numerical integrations illustrate an analytic theorem rather than establish it. The 1024-bit example's 529-bit upper bound is an existence certificate, not a constructed large encoder.

## Publication assessment

Proceed with a compact theorem-led candidate: arbitrary summary-dependent one-probe all-pairs data structures match fixed endpoint recovery in rate and success exponent. The elementary basis count explains the converse, and the exact weighted-error identity explains the construction. The geometry, scalar curve, entropy-bias budget, duality, and ordinary covering methods are established ingredients. The operational synthesis is the remaining candidate contribution; publication readiness and its historical priority are not established.

The novelty audit, issue #1, remains open for the operational theorem. The original Nisan-Rudich-Saks manuscript gives a weaker extensive converse. One-star partial matrices recover the affine-fiber/entropy ingredient. The corrected Smal-Talebanfard approximate-prediction theorem does not apply directly to the pair-output lift because it loses entropy/locality accounting. Direct query-with-sketch batching has a conditional-support obstruction. Those specific limitations remain valid, but the earlier unresolved attribution of the geometric count is superseded by the complete reductions now recorded.

The latest primary-source comparisons add extremal low-weight vectors, sequential caching, locally decodable source coding, and functional index coding. A computed one-bit cache update solves the task with one cached parity bit, demonstrating why a raw-coordinate restriction cannot be dropped. The direct local-source-code translation charges $n+B$ storage and complete-summary access. The [literature ledger](LITERATURE_COMPARISON.md) records these precise reductions and their limits; none is a global non-subsumption claim.

## Next decisive work

The originating workspace should assess priority and significance of the **operational rate and success-exponent theorem** in the brief. The elementary geometric mechanism has an adequate classical attribution; another search for independent novelty of that count is not the next task. A specialist comparison with approximate systematic data structures and source coding would now be more informative than further lower-order refinements. No external contact or submission has been made.

The full finite pair-coverage envelope and efficient constructions are secondary research options if they add conceptual substance. Large simulations and neural training do not resolve the present priority question. Keep issue #1 open.

The finite-length optimum, second-order terms, algorithmic efficiency, adaptive post-seed query guarantees, and error parameters varying with n are separate open questions. Do not silently expand the current theorem to cover them.

The conjunction/refinement exploration remains separate and unchanged. This repository does not claim a theorem about consciousness, natural-language interpretation, or deployed AI systems. The existing MIT license and source attribution are preserved.
