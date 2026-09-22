# Contributing to Objective Revision Memory

This is a theorem-led research project. Contributions should improve a proof,
resolve a precise literature comparison, clarify the model, or test a concrete
possible failure. Small exact checks support the arguments; passing checks do
not establish a general theorem or historical novelty.

Start with the [reading guide](docs/READING_GUIDE.md) and follow the current
[research roadmap](docs/RESEARCH_ROADMAP.md). Manuscript preparation is on hold.
Potential collaborators can contact Ruge Lin using the email in the
[README](README.md). The completed [contribution assessment](docs/CONTRIBUTION_ASSESSMENT.md)
sets the present scope; specific new proof objections or prior-result
implications should update that assessment. Repository maintenance does not
itself start drafting, submission, or external correspondence.

## Coordinate the work

Inspect current `main`, record its full commit SHA, and read
[status](docs/STATUS.md), [issue #1](https://github.com/GoGoKo699/Objective-Revision-Memory/issues/1),
[issue #2](https://github.com/GoGoKo699/Objective-Revision-Memory/issues/2), and
open pull requests. Issue #2 records the former rate gap; its closure is not
proof evidence. Check current files rather than relying on an older handoff.

Use a dedicated branch and a reviewable pull request. Check for an existing
branch before creating one; resume another workspace's branch only by agreement.
Recheck the branch and its head before writing or pushing, preserve intervening
commits, and coordinate overlapping file ownership. Do not reset, force-push,
or overwrite another workspace's work. Existing user authorization governs
integration; the historical no-self-merge instruction in the
[review brief](docs/WORKSPACE_REVIEW_BRIEF.md) has been superseded by its
continuation notice.

## Make mathematical changes reviewable

Every theorem change should state its model and scope explicitly:

- Identify the input distribution, query family, and what is known before
  encoding and before the raw read.
- Account for fixed worst-case summary bits, exact retained parity where
  required, the one-raw-bit read, and the allowed address dependence. State
  which randomness, computation, code descriptions, and archive storage are
  free; input-dependent caches and transcripts are charged.
- Preserve error quantifiers: input/query averages, fixed-input or fixed-pair
  guarantees, table distortion, and success probability are different criteria.
  State whether a new criterion replaces an earlier one. Specify fixed
  parameters and the order of asymptotic limits.

For a suspected defect, give the reviewed commit, affected statement, and a
minimal counterexample or the precise unsupported proof step in an issue or
pull request. State which conclusions survive. Distinguish a false claim from
an incomplete argument or a wording correction.

For a novelty comparison, identify the primary source, version, and theorem
location. Give an explicit reduction preserving memory, probes, timing,
randomness, and error, or identify the missing step. Record unavailable sources
and unresolved comparisons. Add the result to the
[literature ledger](docs/LITERATURE_COMPARISON.md); search non-detection is not
evidence of priority.

## Preserve and reproduce the evidence

Preserve the [MIT license](LICENSE), attribution, and imported files recorded
in [SOURCE_MANIFEST.json](docs/SOURCE_MANIFEST.json), including their scripts
and reports. Add new checks separately. Do not change an expected result or
tolerance merely to obtain a pass. Keep the conjunction exploration separate
from the parity model.

The standard runner uses Python 3.10 or newer and only the standard library.
Run without `-O`:

```sh
python checks/run_all.py
```

Use `--include-conjunction` when reproducing that separate exploration or the
full historical review command. Targeted scripts under `checks/reviews/` are
optional checks, run separately; they are not silently included in the runner
or CI. Select them to address the changed claim or a concrete uncertainty.
The [reproduction guide](docs/REPRODUCIBILITY.md) lists commands, exact scopes,
and numerical limitations.

Record what actually ran, its outcome, and the reviewed commit. Distinguish a
rerun from inspection of committed results. End a substantive handoff with the
findings, remaining uncertainty, and report commit or pull request identifier.
