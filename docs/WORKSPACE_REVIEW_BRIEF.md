# Second workspace: proof and novelty audit

Prepared 22 September 2026 for the Objective Revision Memory project.

Repository: `GoGoKo699/Objective-Revision-Memory`.
Scientific checkpoint at preparation: `cbdcd0fc109c39ee5b5d53c58668695c0f785cbb`.
This brief coordinates work; it does not report a completed review or change any theorem.

**22 September 2026 continuation:** the user subsequently authorized continued research and merging. The initial review was completed in PR #3 and merged at `4e2c579795e2e780e132e3feb8072d2260ab3a7f`. This authorization supersedes the no-self-merge convention below. Continue to use dedicated branches and reviewable pull requests, recheck current heads, preserve intervening work and verification artifacts, and state unresolved novelty. The initial assignment text is retained as historical context.

## Assignment and research goal

You are the fresh-context proof and novelty reviewer working alongside the originating research workspace. The originating workspace handles theory development, responses to findings, and integration. Your immediate job is to determine whether the sharp-rate claim survives detailed scrutiny, and what genuinely remains after comparison with prior work. Do not start by polishing the exposition or extending a theorem whose argument has not been audited.

The user wants publishable, theorem-led research with a clear conceptual contribution and established novelty. Large network/cloud simulations and numerically intensive projects are not appropriate. Small local exact checks are useful supporting evidence, not substitutes for proofs. The user has authorized work in this public repository. Preserve the existing MIT license and attribution. Do not publish private conversations, the motivating fiction, or unrelated personal material.

A fresh model context can help uncover mistakes, but agreement between two model workspaces is not independent human expert validation, peer review, or proof-assistant certification. The aim is a sound, useful result, not defending prior claims or manufacturing disagreement.

## Start from the repository, not the previous answer

Read current `main`, record its full commit SHA, and inspect open issues and pull requests before choosing a working branch. Do not assume the preparation SHA is still current. Pin the exact scientific version reviewed; when `main` changes later, state whether your findings still apply or need a new comparison.

Read the [current proof](../RESEARCH_NOTE.md), [status](STATUS.md), [literature comparison](LITERATURE_COMPARISON.md), [reproduction guide](REPRODUCIBILITY.md), and [baseline note](../BASELINE_NOTE.md). Read issue #1 for the novelty obligations and issue #2 for the written-proof resolution of the former rate gap. Issue closure is a project bookkeeping decision, not evidence that the proof is correct. Baseline open-gap language is historical, not the current claim.

Run `python checks/run_all.py --include-conjunction` when a local execution environment is available. Record the actual command, outcome, and reviewed commit. Read the tests before treating a pass as evidence. Without execution access, distinguish inspection of recorded outputs from a rerun. Do not silently replace the missing capability with a claim of success.

The conjunction/refinement exploration is a separate mathematical model. Do not import its bounds into the parity proof, and do not restart any other branch of the fiction-inspired research.

## Model and claim to audit

An input `X` has `n >= 3` bits. Before knowing the query, an arbitrary encoder retains at most `B` input-dependent bits, with input-independent shared randomness allowed. The original total parity must be exactly recoverable from memory and the seed alone. A later pair `{i,j}` requests total parity with those two coordinates excluded.

The decoder sees the complete summary and seed, performs unrestricted local computation, and may reread at most one original coordinate. The address may depend on the memory, seed, and query. It is not restricted to an endpoint. The original immutable archive is outside `B`; a probe returns one raw bit, not an arbitrary Boolean function or machine word. Prior transcripts and extra input-dependent caches are not free. Preprocessing time and input-independent randomness are uncharged.

The stated optimum uses error at most epsilon for each fixed pair, averaged over uniform inputs and random coins. The converse needs only input-and-pair average error. The construction claims the stronger guarantee for every fixed input and fixed pair over the seed. Neither claim is simultaneous correctness of all pairs or a guarantee for an adversarial query selected after seeing the seed and summary.

For fixed `0 < epsilon < 1/2`, put `eta = 1 - 2 epsilon` and choose positive `a` satisfying

$$\eta=2\int_0^1 u\tanh(au)\,du.$$

The current note claims

$$\lim_{n\to\infty}\frac{B_{\rm all}(n,\varepsilon)}n
=\frac{a\eta-\ln\cosh a}{\ln2},$$

with finite converse, for every positive `s`,

$$B\ln2\geq s\binom n2\eta-\sum_{k=1}^n\ln\cosh(sk).$$

The achieving idea is graded reconstruction accuracy, followed by rereading the weaker endpoint. Treat these as assertions to rederive, not trusted premises. Existing exact and affine results can be audited as dependencies, not assumed merely because earlier tests passed.

## First task: mathematical audit

Reconstruct the dependency chain from definitions to converse to achievability. Check every quantifier and distinguish a false claim from an incomplete argument, a repairable exposition issue, and a step genuinely checked without finding a gap. A request for more explanation is not a counterexample; a plausible explanation is not a proof.

Pay particular attention to:

- Pair-rank coverage for arbitrary residual rows, including endpoint probes, duplicate residual rows, and subsets; the greedy threshold-span property and the exact coefficients in the bias profile.
- Entropy after conditioning on memory and random tapes, arbitrary nonlinear memory cells, deterministic reduction of one-read Boolean decisions, and the averaging that converts conditional entropy deficit into a `B`-bit budget.
- Convex conjugacy, finite-to-asymptotic passage, uniqueness of the parameter, and whether the result holds for all sufficiently large lengths rather than only a subsequence.
- The graded covering construction: covering existence versus an efficient encoder; mask/permutation independence; same-block ties; fixed-input/fixed-pair accuracy; parity accounting; and whether the reread genuinely stays within one bit.
- The order of limits for quality levels, block sizes, error margins, and coding overhead. Do not infer uniform vanishing-error or vanishing-advantage guarantees from fixed-error asymptotics.

Use tiny independent implementations or explicit examples to target suspected failure points. Avoid merely duplicating the current verifier's derivation. Preserve baseline scripts and reports; do not adjust tolerances or expected outputs to conceal a failure. If a central step fails, write the smallest decisive counterexample or obstruction and identify the strongest statement that survives. Offer a repair only with its changed assumptions and proof obligations visible.

## Second task: theorem-level novelty comparison

Use primary papers, original theorem statements, and version-specific references. Start with the queue in the repository: systematic data structures/common-bits and matrix rigidity, classical/function/biased random access codes, query-with-sketch, help bits in decision trees, and coding with decoder-controlled side information.

Prioritize obtaining and reading the original Nisan-Rudich-Saks *Products and Help Bits in Decision Trees* text, which the current audit explicitly leaves unfinished. Independently verify bibliographic identities and theorem numbers for every source relied upon. Record access failures; do not treat an abstract, secondhand citation, or unsuccessful search as a full comparison.

For each close theorem, record the source/version and theorem location, input distribution, encoding restrictions, paid resources, query timing, randomness and error quantifiers, then either an explicit reduction or the precise missing step. Distinguish established ingredients, immediate corollaries, partial overlap, and genuinely unresolved subsumption. The existing scalar-output objection to one min-entropy lemma does not exclude batched or amplified reductions; charge their extra memory and probes.

Search for the sharp profile law and an equivalent operational problem, not only the project's AI terminology. A correct theorem that is already known is a valuable finding. Novelty alone is also insufficient: explain whether the residual contribution is substantive enough for a theoretical paper, without unsupported venue promises.

## Shared-repository protocol

Use GitHub commits, the audit pull request, and issue #1 as the handoff record. Do not assume another workspace has read an uncommitted file, a chat message, or an in-progress edit. Work occurs when a workspace is invoked; this brief creates no background runner or automatic notification service.

Use a dedicated branch such as `review/sharp-rate-audit`, based on a freshly read `main`. Before creating it, inspect whether it already exists; resume only when it is your established work, otherwise select a distinct suffix. Do not reset, force-push, delete, or overwrite another workspace's branch. Recheck the current branch head before each write and preserve intervening commits.

Keep the scientific claim on `main` unchanged during review. Commit the review report and optional targeted checks to your review branch and open a pull request for integration by the originating workspace. Do not merge your own review or rewrite the central proof/status documents on `main`. Proposed corrections to those documents belong in the pull request and must be identified explicitly. This is a collaboration convention, not a claim of configured branch protection.

For a serious mathematical defect, post the specific obstruction promptly in the review pull request or a linked issue; the lead should triage it on resumption. Do not silently leave a false central claim unflagged, but do not invent external notifications. No external researcher contact, manuscript submission, or release is part of this assignment.

## Deliverable and first response

Maintain one substantive report, `docs/reviews/SHARP_RATE_AUDIT.md`, on the review branch. It should identify the reviewed SHA and scope; give a lemma-by-lemma correctness assessment with supporting reasoning; record counterexamples or repairs; provide the theorem comparison ledger; distinguish test execution from inspection; and finish with the single most important next research action. These are deliverable paths to create, not files presumed already present.

At the end of a work session, provide the report commit and pull request identifier, the actual findings, remaining uncertainty, and any integration action required. The user should not have to carry the whole proof or literature review between workspaces; repository references are the handoff.

Begin actual review in your first working response. Confirm the checked commit, reconstruct the model, rerun the baseline when possible, and inspect the highest-risk proof step. Do not stop after restating this plan. A bounded, well-supported finding is preferable to a broad claim that everything is verified. If the proof and novelty checks support proceeding, identify the narrow defensible paper contribution; if not, preserve the useful result and recommend the next concrete repair or research direction.
