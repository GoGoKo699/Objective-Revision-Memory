# Research status

Updated 22 September 2026, sharp-rate checkpoint.

## Mathematical progress

The unrestricted leading-rate gap tracked in issue #2 is resolved by a written converse and matching construction in [RESEARCH_NOTE.md](../RESEARCH_NOTE.md). The proof also establishes existence of the full limiting optimal rate for fixed revised error strictly between zero and one half. It does not claim finite-length optimality.

The new converse keeps the complete sequence of greedy independent residual biases. A scalar entropy conjugacy gives a finite lower bound and its integral limit. The construction assigns graded reconstruction accuracy and rereads the less accurately represented queried endpoint. Ordinary covering-code ingredients are credited. The construction respects the previous model and achieves a stronger fixed-input/fixed-query randomized guarantee than the converse needs.

The old exact optimum, affine leading optimum, bounded-error inequalities, and explicit majority examples remain valid. They are preserved in [BASELINE_NOTE.md](../BASELINE_NOTE.md). Its open-rate statements and factor-two gap describe the earlier checkpoint, not current status.

## Evidence and limitations

The new standard-library verifier tests every nonempty fixed-parity cell through five bits, exact rank-profile inequalities, numerical entropy/conjugate inequalities, a fully seeded counted-read decoder, finite covering-existence arithmetic, and numerical evaluations of the curve. The old imported scripts and reports remain byte-for-byte unchanged. See [REPRODUCIBILITY.md](REPRODUCIBILITY.md).

There is no independent expert review, proof-assistant certificate, or efficient implementation of the large covering codes. Numerical integrations illustrate an analytic theorem rather than establish it. The 1024-bit example's 529-bit upper bound is an existence certificate, not a constructed large encoder.

## Publication assessment

The previous result gave an exact special case and a bounded-error gap. The current candidate has a matching unrestricted error-memory law and a concrete design principle. This is stronger material for a theoretical paper, but publication readiness is not established.

The novelty audit, issue #1, remains open. It must compare the rank-profile statement and resulting sharp curve against systematic/common-bits, help-bit, RAC, and weighted coding results, not merely note terminology differences. A direct scalar use of one neighboring min-entropy lemma is insufficient; indirect reductions remain possible. The original Nisan-Rudich-Saks text has not yet been audited in full.

## Next decisive work

1. Complete the theorem-level priority comparison for the sharp profile law; record any exact subsumption or standard-corollary reduction.
2. Stress-test the mathematical proof independently, especially entropy conditioning, public-mask/permutation symmetrization, and the fixed-quality-level/order-of-limits argument.
3. Only after those checks, assess whether finite-length bounds or efficient explicit constructions are needed for a publishable contribution. Do not train a neural model to substitute for a missing theorem or novelty argument.

The finite-length optimum, second-order terms, algorithmic efficiency, adaptive post-seed query guarantees, and error parameters varying with n are separate open questions. Do not silently expand the current theorem to cover them.

The conjunction/refinement exploration remains separate and unchanged. This repository does not claim a theorem about consciousness, natural-language interpretation, or deployed AI systems. The existing MIT license and source attribution are preserved.
