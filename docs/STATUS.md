# Research status

Updated 22 September 2026, following the sharp-rate audit and research continuation. Continuation base: `4e2c579795e2e780e132e3feb8072d2260ab3a7f` (merged audit PR #3).

## Mathematical progress

The unrestricted leading-rate gap tracked in issue #2 is resolved by a written converse and matching construction in [RESEARCH_NOTE.md](../RESEARCH_NOTE.md). The proof also establishes existence of the full limiting optimal rate for fixed revised error strictly between zero and one half. It does not claim finite-length optimality.

The converse keeps the complete sequence of greedy independent residual biases. Entropic Chang machinery and scalar conjugacy turn the pair-subset rank envelope into a finite lower bound and its integral limit. The construction assigns graded reconstruction accuracy and rereads the less accurately represented queried endpoint. Its scalar profile is an established weighted binary rate-distortion allocation. The construction respects the previous model. Public permutation/mask symmetrization shows the three stated error optima coincide even at finite length, without extra summary bits or reads.

The [research continuation](RANK_PROFILE_EXTENSIONS.md) adds proofs of a general rank-envelope bound, a capped finite converse, and the exact low-rank pair-coverage maximum $nr-r(r+1)/2$ when $n\ge2r+2$. It also identifies the sharp rate $1-h_2(\varepsilon)$ per matching edge for bipartite query families as matching number grows, under per-edge error. These are deductions from explicit arguments and established ingredients; priority is not certified. The low-rank formula fails outside its stated range, and none of these results asserts the finite optimal memory for all pairs.

The old exact optimum, affine leading optimum, bounded-error inequalities, and explicit majority examples remain valid. They are preserved in [BASELINE_NOTE.md](../BASELINE_NOTE.md). Its open-rate statements and factor-two gap describe the earlier checkpoint, not current status.

## Evidence and limitations

The new standard-library verifier tests every nonempty fixed-parity cell through five bits, exact rank-profile inequalities, numerical entropy/conjugate inequalities, a fully seeded counted-read decoder, finite covering-existence arithmetic, and numerical evaluations of the curve. The old imported scripts and reports remain byte-for-byte unchanged. See [REPRODUCIBILITY.md](REPRODUCIBILITY.md).

The [audit](reviews/SHARP_RATE_AUDIT.md) reconstructed the central proof and found no defect; it did not infer correctness from passing tests. Optional exact checks now cover asymmetric reconstruction errors under public symmetrization and all 3,559 low-rank subspaces through seven bits. The latter also verifies the explicit Hamming-kernel counterexample to extending the new formula to all ranks.

There is no independent expert review, proof-assistant certificate, or efficient implementation of the large covering codes. Numerical integrations illustrate an analytic theorem rather than establish it. The 1024-bit example's 529-bit upper bound is an existence certificate, not a constructed large encoder.

## Publication assessment

The defensible candidate is an operational equality: arbitrary summary-dependent one-probe all-pairs data structures have the same first-order optimum as a specified weighted binary coding problem. The all-subsets pair-rank geometry, together with matching achievability, supplies its possible conceptual contribution. The scalar curve, entropy-bias budget, and generic nonlinear advantage are established ingredients. Publication readiness is not established.

The novelty audit, issue #1, remains open. The original Nisan-Rudich-Saks manuscript has now been read and yields a weaker extensive converse. One-star partial matrices recover the affine-fiber/entropy ingredient, but no inspected theorem supplied the all-pairs threshold weights. The corrected Smal-Talebanfard approximate-prediction theorem was checked: directly lifting all pair parities creates a quadratic entropy deficit and changes locality. Direct query-with-sketch batching also has a specific conditional-support obstruction. These limits on particular reductions do not exclude a stronger indirect subsumption.

## Next decisive work

1. Resolve priority for the pair-specific all-subsets rank envelope and its approximate one-star consequence, using the now explicit generic entropy lemma to isolate exactly what must be found in prior work.
2. Determine whether the full finite pair-coverage envelope has a useful exact characterization; the proved low-rank range and Hamming-kernel example give opposing boundary cases.
3. Assess whether that geometric characterization or efficient explicit constructions adds enough substance for a paper. Large simulations and neural training do not resolve these questions.

The finite-length optimum, second-order terms, algorithmic efficiency, adaptive post-seed query guarantees, and error parameters varying with n are separate open questions. Do not silently expand the current theorem to cover them.

The conjunction/refinement exploration remains separate and unchanged. This repository does not claim a theorem about consciousness, natural-language interpretation, or deployed AI systems. The existing MIT license and source attribution are preserved.
