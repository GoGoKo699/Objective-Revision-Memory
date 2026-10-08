# Results and limitations

The [self-contained pair-query note](PAIR_QUERY_NOTE.md) gives the complete
central proof. The [reading guide](READING_GUIDE.md) introduces the model,
the [theorem brief](THEOREM_BRIEF.md) compares access restrictions, and the
[operational reduction](OPERATIONAL_REDUCTION.md) gives the general coding
comparisons.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).

The [contribution assessment](CONTRIBUTION_ASSESSMENT.md) supports the sharp
one-read extremal theorem as the proposed original contribution. The
[open questions](OPEN_QUESTIONS.md) describe regimes beyond the proved results.

## Established results

The unrestricted leading rate is determined by a written converse and matching construction in [RESEARCH_NOTE.md](../RESEARCH_NOTE.md). The proof also establishes existence of the full limiting optimal rate for fixed revised error strictly between zero and one half. It does not claim finite-length optimality.

The converse keeps the complete sequence of greedy independent residual biases. Entropic Chang machinery and scalar conjugacy turn the pair-subset rank envelope into a finite lower bound and its integral limit. The construction assigns graded reconstruction accuracy and rereads the less accurately represented queried endpoint. Its scalar profile is an established weighted binary rate-distortion allocation. Public permutation/mask symmetrization shows the three stated error optima coincide even at finite length, without extra summary bits or reads.

The [rank-profile bounds](RANK_PROFILE_EXTENSIONS.md) include proofs of a general rank-envelope bound, a capped finite converse, and the exact low-rank pair-coverage maximum $`nr-r(r+1)/2`$ when $`n\ge2r+2`$. They also identify the sharp rate $`1-h_2(\varepsilon)`$ per matching edge for bipartite query families as matching number grows, under per-edge error. These are deductions from explicit arguments and established ingredients; priority is not certified. The low-rank formula fails outside its stated range, and none of these results asserts the finite optimal memory for all pairs.

The [literature comparison](LITERATURE_COMPARISON.md) supplies complete classical derivations of the all-subsets geometric envelope through affine-basis sumsets and fundamental-circuit uniqueness. This is an elementary task-specific lemma, not an independent novelty claim. Erdős–Gallai's matching bound also yields the separate low-rank extremum when $`n\ge(5r+3)/2`$. None of these attributions identifies a prior statement of the full operational memory theorem.

Endpoint comparisons distinguish leading-rate and finite-length behavior. Arbitrary addresses, endpoint-only addresses, and publicly chosen endpoint addresses all have the same leading rate at fixed interior error. Endpoint-only zero-error memory is exactly $`n-1`$, exceeding the unrestricted optimum by $`\lfloor\log_2(n+1)\rfloor-1`$ bits. Retaining original parity adds at most one bit relative to the direct pair-parity task. Full proofs and an endpoint finite converse are in the brief.

The excess-distortion formulation determines the **success exponent**. Let success mean that at most an $`\varepsilon`$ fraction of pair queries would be answered incorrectly on an input, with each query considered separately under its own one-read budget. At memory rate $`\rho`$, the optimum success probability has exponent $`(\mathcal R(\varepsilon)-\rho)_+`$. Deterministic ordered-endpoint schemes attain it. This optimization keeps the resource and exact-parity rules but replaces the original marginal-error promise; it does not impose that promise below the rate. The same rate also supports a deterministic worst-input guarantee on the fraction of wrong pairs. Full proofs use the existing moment converse and weighted Hamming covers; no optimal failure exponent above the rate is claimed.

The [operational reduction](OPERATIONAL_REDUCTION.md) isolates the mathematical content of these consequences. The maximum fraction $`m_n(\varepsilon)`$ of inputs handled with low table distortion by one fixed arbitrary-address strategy is $`2^{-n\mathcal R(\varepsilon)+o(n)}`$. Ordered-endpoint weighted Hamming balls attain that exponent. XOR translations of a maximizing strategy yield a finite success sandwich within a universal constant factor and a worst-input cover using one fixed address pattern with at most $`1+\lceil\log_2(n\ln2+1)\rceil`$ extra bits compared with an optimal arbitrary-address cover. That fixed pattern may use nonendpoints. These are standard symmetry/coding deductions, not independent novelty claims or efficient constructions.

The exact optimum, affine leading optimum, bounded-error inequalities, and explicit majority examples remain valid. They are preserved in [BASELINE_NOTE.md](../BASELINE_NOTE.md). Its open-rate statements and factor-two gap describe the earlier checkpoint, not current status.

The central proof is self-contained. A direct entropy argument on each
strategy's good-input set proves the finite bound, and independent tilted bits
give the weighted-ball exponent with a strict distortion margin. Random
translations give the covering and success consequences. The expected-error
converse is separately derived by averaging conditional entropy deficits;
it is not inferred from the tail bound alone.

## Evidence and limitations

The sharp-rate standard-library verifier tests every nonempty fixed-parity cell through five bits, exact rank-profile inequalities, numerical entropy/conjugate inequalities, a fully seeded counted-read decoder, finite covering-existence arithmetic, and numerical evaluations of the curve. The imported scripts and reports remain byte-for-byte unchanged. See [REPRODUCIBILITY.md](REPRODUCIBILITY.md).

The [audit](reviews/SHARP_RATE_AUDIT.md) reconstructed the central proof and found no defect; it did not infer correctness from passing tests. Optional exact checks cover asymmetric reconstruction errors under public symmetrization and all 3,559 low-rank subspaces through seven bits. The latter also verifies the explicit Hamming-kernel counterexample to extending the low-rank formula to all ranks.

The endpoint-scope check tests the endpoint construction and three-point-cell obstruction, the three-bit probe separation, and two seven-coordinate subspaces with identical full weight enumerators but different pair coverage. That counterexample identifies information lost by an ordinary weight enumerator. These checks support specified finite claims, not the general theorem or priority.

The excess-distortion check adds 2,688 executions of a four-bit-summary block construction and 534 exact rational tail inequalities for explicit nonlinear and summary-dependent decoders. It verifies finite consequences of the proof, not the asymptotic exponent by extrapolation. All original verification artifacts remain unchanged.

The strategy-translation check exhausts all 512 canonical three-bit strategies,
verifying the mask identity, unchanged addresses, uniform translated-ball hit
counts, and the mandatory-parity counterexample with integer arithmetic.
These checks support the finite reductions; they do not settle priority.

The priority-obstruction check verifies the equal-rank/different-ball example
on 504 inputs and five sparse parity systems with 986 rows. It uses exact
integer arithmetic.

Recorded full-suite reproductions and all six optional checks passed, with
all five recorded reports reproduced byte-for-byte in the checked environment.
The [reproduction guide](REPRODUCIBILITY.md) states commands, coverage, and
numerical tolerances. Dated validation records are preserved in the
[audit](reviews/SHARP_RATE_AUDIT.md); these are finite checks, not proof or
novelty certificates.

There is no independent expert review, proof-assistant certificate, or efficient implementation of the large covering codes. Numerical integrations illustrate an analytic theorem rather than establish it. The 1024-bit example's 529-bit upper bound is an existence certificate, not a constructed large encoder.

## Contribution assessment

**Proposed original contribution: the task-specific extremal theorem.**
Arbitrary nonlinear summaries and memory-dependent raw-read
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

The comparisons include Pananjady–Courtade's freely read header model,
Rioul–Solé's entropy proof of ordinary ball bounds, and recent bounded-error
linear-operator and random-access-code results. Header-dependent local reads
and uniform-on-a-ball entropy counting are established ideas. Explicit
substitutions into the inspected theorems do not supply the unrestricted
pair-query optimum. In particular, the dependent pair-output lift is not a
uniform constant-weight source; block-error recovery is not positive table
distortion; and a random dense operator is not the explicit weight-two query
matrix. The ledger records these deductions and their limits.

## Remaining uncertainty

Historical coverage remains incomplete, and a concrete prior implication or
mathematical objection can change the bounded contribution assessment. It
does not claim an efficient construction, finite-length optimality, or broad
technological significance. Independent specialist review has not been
obtained.

The [open questions](OPEN_QUESTIONS.md) include finite-length optima, efficient
explicit codes, second-order terms, the full pair-coverage envelope, and error
varying with archive size. These lie beyond the fixed-positive-error
leading-rate theorem.
