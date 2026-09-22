# Research status

Updated 22 September 2026, following the targeted priority decision. Reviewed main: `b9394cd2ea64c45943e66ba7c61ae665f3df77c3` (merged PR #4). The current development decision and proofs are in the [compact theorem brief](THEOREM_BRIEF.md).

## Mathematical progress

The unrestricted leading-rate gap tracked in issue #2 is resolved by a written converse and matching construction in [RESEARCH_NOTE.md](../RESEARCH_NOTE.md). The proof also establishes existence of the full limiting optimal rate for fixed revised error strictly between zero and one half. It does not claim finite-length optimality.

The converse keeps the complete sequence of greedy independent residual biases. Entropic Chang machinery and scalar conjugacy turn the pair-subset rank envelope into a finite lower bound and its integral limit. The construction assigns graded reconstruction accuracy and rereads the less accurately represented queried endpoint. Its scalar profile is an established weighted binary rate-distortion allocation. The construction respects the previous model. Public permutation/mask symmetrization shows the three stated error optima coincide even at finite length, without extra summary bits or reads.

The [research continuation](RANK_PROFILE_EXTENSIONS.md) adds proofs of a general rank-envelope bound, a capped finite converse, and the exact low-rank pair-coverage maximum $nr-r(r+1)/2$ when $n\ge2r+2$. It also identifies the sharp rate $1-h_2(\varepsilon)$ per matching edge for bipartite query families as matching number grows, under per-edge error. These are deductions from explicit arguments and established ingredients; priority is not certified. The low-rank formula fails outside its stated range, and none of these results asserts the finite optimal memory for all pairs.

The latest comparison proves a genuine partial subsumption: Erdős–Gallai's 1959 matching bound already yields this low-rank extremum when $n\ge(5r+3)/2$. It loses leading-order information at larger ranks, so this reduction does not supply the sharp curve. The priority target is any uniform all-subsets envelope $nr-r^2/2+o(n^2)$, not necessarily the exact finite polynomial.

New endpoint comparisons sharpen the operational interpretation. Arbitrary addresses, endpoint-only addresses, and publicly chosen endpoint addresses all have the same leading rate at fixed interior error. Endpoint-only zero-error memory is exactly $n-1$, exceeding the unrestricted optimum by $\lfloor\log_2(n+1)\rfloor-1$ bits. Retaining original parity adds at most one bit relative to the direct pair-parity task. Full proofs and an endpoint finite converse are in the brief.

The old exact optimum, affine leading optimum, bounded-error inequalities, and explicit majority examples remain valid. They are preserved in [BASELINE_NOTE.md](../BASELINE_NOTE.md). Its open-rate statements and factor-two gap describe the earlier checkpoint, not current status.

## Evidence and limitations

The new standard-library verifier tests every nonempty fixed-parity cell through five bits, exact rank-profile inequalities, numerical entropy/conjugate inequalities, a fully seeded counted-read decoder, finite covering-existence arithmetic, and numerical evaluations of the curve. The old imported scripts and reports remain byte-for-byte unchanged. See [REPRODUCIBILITY.md](REPRODUCIBILITY.md).

The [audit](reviews/SHARP_RATE_AUDIT.md) reconstructed the central proof and found no defect; it did not infer correctness from passing tests. Optional exact checks now cover asymmetric reconstruction errors under public symmetrization and all 3,559 low-rank subspaces through seven bits. The latter also verifies the explicit Hamming-kernel counterexample to extending the new formula to all ranks.

A new optional check tests the endpoint construction and three-point-cell obstruction, the three-bit probe separation, and two seven-coordinate subspaces with identical full weight enumerators but different pair coverage. That counterexample identifies information lost by an ordinary weight enumerator. These checks support specified finite claims, not the general theorem or priority.

There is no independent expert review, proof-assistant certificate, or efficient implementation of the large covering codes. Numerical integrations illustrate an analytic theorem rather than establish it. The 1024-bit example's 529-bit upper bound is an existence certificate, not a constructed large encoder.

## Publication assessment

Proceed with a compact theorem-led research candidate: arbitrary summary-dependent one-probe all-pairs data structures have the same first-order optimum as publicly chosen endpoint recovery and a specified weighted binary coding problem. The almost-vertex-cover geometry explains this equality, while the exact zero-error separation shows its limit. The scalar curve, entropy-bias budget, generic duality, and generic nonlinear advantage are established ingredients. The brief is ready for the originating workspace's assessment; publication readiness and historical priority are not established.

The novelty audit, issue #1, remains open. The original Nisan-Rudich-Saks manuscript has now been read and yields a weaker extensive converse. One-star partial matrices recover the affine-fiber/entropy ingredient, but no inspected theorem supplied the all-pairs threshold weights. The corrected Smal-Talebanfard approximate-prediction theorem was checked: directly lifting all pair parities creates a quadratic entropy deficit and changes locality. Direct query-with-sketch batching also has a specific conditional-support obstruction. These limits on particular reductions do not exclude a stronger indirect subsumption.

The latest primary-source comparisons add extremal low-weight vectors, sequential caching, locally decodable source coding, and functional index coding. A computed one-bit cache update solves the task with one cached parity bit, demonstrating why a raw-coordinate restriction cannot be dropped. The direct local-source-code translation charges $n+B$ storage and complete-summary access. The [literature ledger](LITERATURE_COMPARISON.md) records these precise reductions and their limits; none is a global non-subsumption claim.

## Next decisive work

The originating workspace should assess the compact brief and settle priority for the leading all-subsets geometric envelope or an equivalent approximate one-star result. The classical matching reduction is now a required comparison. A specialist assessment of this precise claim would be more valuable than an undirected literature sweep or additional lower-order refinements. No external contact or submission has been made.

The full finite pair-coverage envelope and efficient constructions are secondary research options if they add conceptual substance. Large simulations and neural training do not resolve the present priority question. Keep issue #1 open.

The finite-length optimum, second-order terms, algorithmic efficiency, adaptive post-seed query guarantees, and error parameters varying with n are separate open questions. Do not silently expand the current theorem to cover them.

The conjunction/refinement exploration remains separate and unchanged. This repository does not claim a theorem about consciousness, natural-language interpretation, or deployed AI systems. The existing MIT license and source attribution are preserved.
