# Research status

Updated 22 September 2026, following the pre-release sanity check. Reviewed main: `a615988c5703d05fbbf96c44b0b08848720ba698` (merged PR #11). The [reading guide](READING_GUIDE.md) introduces the model and maps the proof; the [self-contained pair-query note](PAIR_QUERY_NOTE.md) remains the central proof packet. The [compact brief](THEOREM_BRIEF.md) gives the review question and the [operational reduction](OPERATIONAL_REDUCTION.md) records the general coding comparisons.

**Manuscript preparation is on hold.** Potential collaborators are welcome to
contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
The [contribution assessment](CONTRIBUTION_ASSESSMENT.md) supports the sharp
one-read extremal theorem as the proposed original contribution of a focused
theoretical paper. The [research roadmap](RESEARCH_ROADMAP.md) separates that
completed decision from manuscript status.

## Mathematical progress

The unrestricted leading-rate gap tracked in issue #2 is resolved by a written converse and matching construction in [RESEARCH_NOTE.md](../RESEARCH_NOTE.md). The proof also establishes existence of the full limiting optimal rate for fixed revised error strictly between zero and one half. It does not claim finite-length optimality.

The converse keeps the complete sequence of greedy independent residual biases. Entropic Chang machinery and scalar conjugacy turn the pair-subset rank envelope into a finite lower bound and its integral limit. The construction assigns graded reconstruction accuracy and rereads the less accurately represented queried endpoint. Its scalar profile is an established weighted binary rate-distortion allocation. The construction respects the previous model. Public permutation/mask symmetrization shows the three stated error optima coincide even at finite length, without extra summary bits or reads.

The [research continuation](RANK_PROFILE_EXTENSIONS.md) adds proofs of a general rank-envelope bound, a capped finite converse, and the exact low-rank pair-coverage maximum $`nr-r(r+1)/2`$ when $`n\ge2r+2`$. It also identifies the sharp rate $`1-h_2(\varepsilon)`$ per matching edge for bipartite query families as matching number grows, under per-edge error. These are deductions from explicit arguments and established ingredients; priority is not certified. The low-rank formula fails outside its stated range, and none of these results asserts the finite optimal memory for all pairs.

The latest comparison supplies complete classical derivations of the all-subsets geometric envelope through affine-basis sumsets and fundamental-circuit uniqueness. This is an elementary task-specific lemma, no longer an independent novelty candidate. Erdős–Gallai's matching bound also yields the separate low-rank extremum when $`n\ge(5r+3)/2`$. None of these attributions identifies a prior statement of the full operational memory theorem.

New endpoint comparisons sharpen the operational interpretation. Arbitrary addresses, endpoint-only addresses, and publicly chosen endpoint addresses all have the same leading rate at fixed interior error. Endpoint-only zero-error memory is exactly $`n-1`$, exceeding the unrestricted optimum by $`\lfloor\log_2(n+1)\rfloor-1`$ bits. Retaining original parity adds at most one bit relative to the direct pair-parity task. Full proofs and an endpoint finite converse are in the brief.

The strongest current operational formulation also determines the **success exponent**. Let success mean that at most an $`\varepsilon`$ fraction of pair queries would be answered incorrectly on an input, with each query considered separately under its own one-read budget. At memory rate $`\rho`$, the optimum success probability has exponent $`(\mathcal R(\varepsilon)-\rho)_+`$. Deterministic ordered-endpoint schemes attain it. This optimization keeps the resource and exact-parity rules but replaces the old marginal-error promise; it does not impose that promise below the rate. The same rate also supports a deterministic worst-input guarantee on the fraction of wrong pairs. Full proofs use the existing moment converse and weighted Hamming covers; no optimal failure exponent above the rate is claimed.

The latest reduction isolates the mathematical content of these consequences. The maximum fraction $`m_n(\varepsilon)`$ of inputs handled with low table distortion by one fixed arbitrary-address strategy is $`2^{-n\mathcal R(\varepsilon)+o(n)}`$. Ordered-endpoint weighted Hamming balls attain that exponent. XOR translations of a maximizing strategy yield a finite success sandwich within a universal constant factor and a worst-input cover using one fixed address pattern with at most $`1+\lceil\log_2(n\ln2+1)\rceil`$ extra bits compared with an optimal arbitrary-address cover. That fixed pattern may use nonendpoints. These are standard symmetry/coding deductions, not independent novelty claims or efficient constructions.

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

At the PR #9 repository-organization checkpoint, full reproduction passed with 170
documentation links and all five reports byte-identical. The new reading
guide's six four-bit answers and weighted error count were checked exactly.
The update preserves 23 existing license, proof, source-manifest, verification,
result, exploration, and workflow files byte-for-byte against the reviewed
main. This is documentation validation; it adds no theorem or novelty finding.

At the PR #10 contribution-assessment checkpoint, full reproduction passed again with
all five reports byte-identical. The final documentation check passed with 190
local links, and all 23 protected files remained byte-identical to reviewed
main. Exact enumeration of 504 inputs checked the cut-support examples in
the new local-compression comparison. These findings inform source reductions;
passing checks do not establish novelty.

The subsequent sanity check repaired GitHub math parsing, equation-number
layout, long displays, and stale status wording across the research packet.
All 19 Markdown pages were inspected in GitHub's rendered view: all 1,675
expressions compiled, with no detected math errors or formula overflow at the
inspected desktop width. Full reproduction and all six optional audit scripts
passed; the five recorded reports and 19 protected provenance, verification,
result, license, and workflow files stayed byte-identical. Historical notes
retain their mathematics and content, with normalized Markdown formatting.
Audit Section 15 records the precise scope and checks. Two wording corrections
clarify natural logarithms and the excess-distortion scope of an infinite
parity penalty; no theorem or novelty conclusion changed.

The pre-release rerun found no repository release blocker within its checked
scope. Full reproduction and all six optional checks passed again; all 19
GitHub-rendered Markdown pages and 1,675 expressions passed the desktop
inspection. Internal links, source-archive contents, file syntax, and the
disabled-assertion guard also passed. A stale issue #2 reference to issue #1
being open was corrected. Audit Section 16 records the precise findings and
limits. This check creates no release or tag and does not resume manuscript
preparation.

There is no independent expert review, proof-assistant certificate, or efficient implementation of the large covering codes. Numerical integrations illustrate an analytic theorem rather than establish it. The 1024-bit example's 529-bit upper bound is an existence certificate, not a constructed large encoder.

## Contribution assessment

**Decision: retain the task-specific extremal theorem as the proposed original
contribution.** Arbitrary nonlinear summaries and memory-dependent raw-read
addresses attain no better leading rate than the fixed ordered-endpoint rule.
The [assessment](CONTRIBUTION_ASSESSMENT.md) gives the affirmative significance
case, its strongest objections, and the precise claims those objections limit.
This is a bounded research judgment, not exhaustive historical certification,
independent expert validation, or a prediction of publication acceptance.

The [literature ledger](LITERATURE_COMPARISON.md) credits the established
geometry, entropy, weighted coding, and general distortion conversions.
Its comparisons preserve the original input entropy, the charged summary,
raw-coordinate reads, the growing-archive limit, and error guarantees.
The exact action-model embedding and general coding formulations leave the
pair-specific extremal evaluation to be proved. Matching products, rank alone,
and the inspected generic polynomial bound lose the sharp exponent.

The latest comparisons add Pananjady–Courtade's freely read header model,
Rioul–Solé's entropy proof of ordinary ball bounds, and recent bounded-error
linear-operator and random-access-code results. Header-dependent local reads
and uniform-on-a-ball entropy counting are established ideas. Explicit
substitutions into the inspected theorems do not supply the unrestricted
pair-query optimum. In particular, the dependent pair-output lift is not a
uniform constant-weight source; block-error recovery is not positive table
distortion; and a random dense operator is not the explicit weight-two query
matrix. The ledger records these deductions and their limits.

## Current completion and remaining uncertainty

The proof packet, bounded comparisons, and present significance decision are
complete. Historical coverage remains incomplete, and a concrete prior
implication or mathematical objection can change the decision. The narrow
positive assessment does not claim an efficient construction, finite-length
optimality, or broad technological significance. Specialist feedback is
welcome, without representing it as an unfinished prerequisite for making
the current research judgment.

The manuscript remains on hold. Further work should address concrete new
evidence or a worthwhile extension, following the
[roadmap](RESEARCH_ROADMAP.md). Large simulations and repeated generic searches
are not needed to maintain this completed research packet.
