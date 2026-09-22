# Research status

Updated 22 September 2026, following repository organization and journal selection. Reviewed main: `fe445bf94149b0b9ca3389816ddcc36e883aaf51` (merged PR #8). The [reading guide](READING_GUIDE.md) introduces the model and maps the proof; the [self-contained pair-query note](PAIR_QUERY_NOTE.md) remains the central proof packet. The [compact brief](THEOREM_BRIEF.md) gives the review question and the [operational reduction](OPERATIONAL_REDUCTION.md) records the general coding comparisons.

**Selected target: Information Processing Letters. Manuscript preparation is the final step.** The current work furnishes a research repository and supports the remaining contribution assessment. The [research roadmap](RESEARCH_ROADMAP.md) records the sequence and completion evidence. Journal selection does not establish novelty, significance, or submission readiness.

## Mathematical progress

The unrestricted leading-rate gap tracked in issue #2 is resolved by a written converse and matching construction in [RESEARCH_NOTE.md](../RESEARCH_NOTE.md). The proof also establishes existence of the full limiting optimal rate for fixed revised error strictly between zero and one half. It does not claim finite-length optimality.

The converse keeps the complete sequence of greedy independent residual biases. Entropic Chang machinery and scalar conjugacy turn the pair-subset rank envelope into a finite lower bound and its integral limit. The construction assigns graded reconstruction accuracy and rereads the less accurately represented queried endpoint. Its scalar profile is an established weighted binary rate-distortion allocation. The construction respects the previous model. Public permutation/mask symmetrization shows the three stated error optima coincide even at finite length, without extra summary bits or reads.

The [research continuation](RANK_PROFILE_EXTENSIONS.md) adds proofs of a general rank-envelope bound, a capped finite converse, and the exact low-rank pair-coverage maximum $nr-r(r+1)/2$ when $n\ge2r+2$. It also identifies the sharp rate $1-h_2(\varepsilon)$ per matching edge for bipartite query families as matching number grows, under per-edge error. These are deductions from explicit arguments and established ingredients; priority is not certified. The low-rank formula fails outside its stated range, and none of these results asserts the finite optimal memory for all pairs.

The latest comparison supplies complete classical derivations of the all-subsets geometric envelope through affine-basis sumsets and fundamental-circuit uniqueness. This is an elementary task-specific lemma, no longer an independent novelty candidate. Erdős–Gallai's matching bound also yields the separate low-rank extremum when $n\ge(5r+3)/2$. None of these attributions identifies a prior statement of the full operational memory theorem.

New endpoint comparisons sharpen the operational interpretation. Arbitrary addresses, endpoint-only addresses, and publicly chosen endpoint addresses all have the same leading rate at fixed interior error. Endpoint-only zero-error memory is exactly $n-1$, exceeding the unrestricted optimum by $\lfloor\log_2(n+1)\rfloor-1$ bits. Retaining original parity adds at most one bit relative to the direct pair-parity task. Full proofs and an endpoint finite converse are in the brief.

The strongest current operational formulation also determines the **success exponent**. Let success mean that at most an $\varepsilon$ fraction of pair queries would be answered incorrectly on an input, with each query considered separately under its own one-read budget. At memory rate $\rho$, the optimum success probability has exponent $(\mathcal R(\varepsilon)-\rho)_+$. Deterministic ordered-endpoint schemes attain it. This optimization keeps the resource and exact-parity rules but replaces the old marginal-error promise; it does not impose that promise below the rate. The same rate also supports a deterministic worst-input guarantee on the fraction of wrong pairs. Full proofs use the existing moment converse and weighted Hamming covers; no optimal failure exponent above the rate is claimed.

The latest reduction isolates the mathematical content of these consequences. The maximum fraction $m_n(\varepsilon)$ of inputs handled with low table distortion by one fixed arbitrary-address strategy is $2^{-n\mathcal R(\varepsilon)+o(n)}$. Ordered-endpoint weighted Hamming balls attain that exponent. XOR translations of a maximizing strategy yield a finite success sandwich within a universal constant factor and a worst-input cover using one fixed address pattern with at most $1+\lceil\log_2(n\ln2+1)\rceil$ extra bits compared with an optimal arbitrary-address cover. That fixed pattern may use nonendpoints. These are standard symmetry/coding deductions, not independent novelty claims or efficient constructions.

The old exact optimum, affine leading optimum, bounded-error inequalities, and explicit majority examples remain valid. They are preserved in [BASELINE_NOTE.md](../BASELINE_NOTE.md). Its open-rate statements and factor-two gap describe the earlier checkpoint, not current status.

The central proof is now self-contained. A direct entropy argument on each
strategy's good-input set proves the finite bound, and independent tilted bits
give the weighted-ball exponent with a strict distortion margin. Random
translations give the covering and success consequences. The expected-error
converse is separately derived by averaging conditional entropy deficits;
it is not inferred from the tail bound alone.

## Evidence and limitations

The new standard-library verifier tests every nonempty fixed-parity cell through five bits, exact rank-profile inequalities, numerical entropy/conjugate inequalities, a fully seeded counted-read decoder, finite covering-existence arithmetic, and numerical evaluations of the curve. The old imported scripts and reports remain byte-for-byte unchanged. See [REPRODUCIBILITY.md](REPRODUCIBILITY.md).

The [audit](reviews/SHARP_RATE_AUDIT.md) reconstructed the central proof and found no defect; it did not infer correctness from passing tests. Optional exact checks now cover asymmetric reconstruction errors under public symmetrization and all 3,559 low-rank subspaces through seven bits. The latter also verifies the explicit Hamming-kernel counterexample to extending the new formula to all ranks.

A new optional check tests the endpoint construction and three-point-cell obstruction, the three-bit probe separation, and two seven-coordinate subspaces with identical full weight enumerators but different pair coverage. That counterexample identifies information lost by an ordinary weight enumerator. These checks support specified finite claims, not the general theorem or priority.

The excess-distortion check adds 2,688 executions of a four-bit-summary block construction and 534 exact rational tail inequalities for explicit nonlinear and summary-dependent decoders. It verifies finite consequences of the proof, not the asymptotic exponent by extrapolation. All original verification artifacts remain unchanged.

The strategy-translation check exhausts all 512 canonical three-bit strategies,
verifying the mask identity, unchanged addresses, uniform translated-ball hit
counts, and the mandatory-parity counterexample with integer arithmetic. The
current full reproduction passes with all five recorded reports byte-identical.
These checks support the finite reductions; they do not settle priority.

The latest optional check verifies the equal-rank/different-ball example on
504 inputs and five sparse parity systems with 986 rows. All checks use exact
integers. At the PR #8 checkpoint, full reproduction passed with 112
documentation links and all five reports byte-identical; no original verifier
or tolerance was changed.

After the repository organization, full reproduction again passed with 170
documentation links and all five reports byte-identical. The new reading
guide's six four-bit answers and weighted error count were checked exactly.
The update preserves 23 existing license, proof, source-manifest, verification,
result, exploration, and workflow files byte-for-byte against the reviewed
main. This is documentation validation; it adds no theorem or novelty finding.

There is no independent expert review, proof-assistant certificate, or efficient implementation of the large covering codes. Numerical integrations illustrate an analytic theorem rather than establish it. The 1024-bit example's 529-bit upper bound is an existence certificate, not a constructed large encoder.

## Publication assessment

Assess the existing internal theorem-led candidate centered on the **extremal one-read decoder-ball exponent and ordered-endpoint attainment**. Group the memory-rate, covering, and success-exponent statements as consequences. The geometry, scalar curve, entropy-bias budget, duality, and general lossy-coding conversions are established ingredients. The specific extremal evaluation is the remaining candidate contribution; publication readiness and historical priority are not established. Journal-formatted drafting remains deferred under the [IPL roadmap](RESEARCH_ROADMAP.md).

The novelty audit, issue #1, remains open for the operational theorem. The original Nisan-Rudich-Saks manuscript gives a weaker extensive converse. One-star partial matrices recover the affine-fiber/entropy ingredient. The corrected Smal-Talebanfard approximate-prediction theorem does not apply directly to the pair-output lift because it loses entropy/locality accounting. Direct query-with-sketch batching has a conditional-support obstruction. Those specific limitations remain valid, but the earlier unresolved attribution of the geometric count is superseded by the complete reductions now recorded.

The latest primary-source comparisons add extremal low-weight vectors, sequential caching, locally decodable source coding, and functional index coding. A computed one-bit cache update solves the task with one cached parity bit, demonstrating why a raw-coordinate restriction cannot be dropped. The direct local-source-code translation charges $n+B$ storage and complete-summary access. The [literature ledger](LITERATURE_COMPARISON.md) records these precise reductions and their limits; none is a global non-subsumption claim.

Kostina–Verdú's general finite-block distortion theorems now give an exact coding comparison: a retained label selects a complete one-read strategy. The strategy-ball exponent must still be evaluated for this task. Permuter–Weissman's indirect-source Theorem 4 also contains the repeated-archive expected-distortion problem under an explicit map; its rate differs from ordinary strategy rate-distortion by at most one bit per archive. This supersedes the earlier comparison based only on model differences. Their repeated-archive limit and the repository's single growing archive have different guarantees. Mandatory parity remains exact even on failed inputs and costs at most one separately retained bit; an infinite distortion penalty does not enforce this in a partial cover.

The bounded follow-up identifies precise losses in three other routes. Legal
strategies with equal residual rank and equal zero-error fiber size can have
different approximate-volume exponents. Matching/direct-product bounds give a
strictly weaker explicit exponent; pooling all pair reads into a global budget
would trivialize the task. A generic polynomial concentration bound also loses
the required scale on an explicit legal strategy. Moreover, dropping pair
labels admits full-rank, degree-three systems whose good fraction is
$2^{-O(n^{2/3})}$. These deductions identify pair incidence as essential;
they do not exclude every prior theorem or certify originality.

## Next decisive work

The self-contained internal proof note and bounded comparison are complete.
The repository now supplies a reading route, resource and error ledgers, proof
map, and contribution guide. The next research decision is a bounded assessment
of the precise decoder-ball theorem's priority and significance for IPL; the
[roadmap](RESEARCH_ROADMAP.md) gives four concrete questions and separates this
decision from final manuscript preparation. A focused specialist assessment can
inform that judgment. Issue #1 remains open. Do not turn inability to certify
all historical priority into an indefinite cycle of broad searches, or add
generic corollaries to inflate the contribution. If a prior implication is
identified, record the result as an attributed worked example and reassess its
publication value. No external contact, submission, or manuscript release has
been made.

The full finite pair-coverage envelope and efficient constructions are secondary research options if they add conceptual substance. Large simulations and neural training do not resolve the present priority question. Keep issue #1 open.

The finite-length optimum, second-order terms, algorithmic efficiency, adaptive post-seed query guarantees, and error parameters varying with n are separate open questions. Do not silently expand the current theorem to cover them.

The conjunction/refinement exploration remains separate and unchanged. This repository does not claim a theorem about consciousness, natural-language interpretation, or deployed AI systems. The existing MIT license and source attribution are preserved.
