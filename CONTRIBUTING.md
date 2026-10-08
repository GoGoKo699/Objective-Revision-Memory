# Contributing to Objective Revision Memory

This is a theorem-led research project. Contributions should improve a proof,
resolve a precise literature comparison, clarify the model, or test a concrete
possible failure. Small exact checks support the arguments; passing checks do
not establish a general theorem or historical novelty.

Start with the [reading guide](docs/READING_GUIDE.md) and
[open questions](docs/OPEN_QUESTIONS.md). The completed [contribution assessment](docs/CONTRIBUTION_ASSESSMENT.md)
sets the present scope; specific new proof objections or prior-result
implications should update that assessment.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).

## Submit a contribution

Read the current [results and limitations](docs/STATUS.md), then check open
issues and pull requests for related work. Use a dedicated branch and a
reviewable pull request. Preserve intervening commits and coordinate
overlapping changes; do not overwrite another contributor's work.

Identify the base commit, explain the change and its scope, and report the
checks actually run. Issue closure and passing checks do not establish
correctness or priority.

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
full validation suite. Targeted scripts under `checks/reviews/` are
optional checks, run separately; they are not silently included in the runner
or CI. Select them to address the changed claim or a concrete uncertainty.
The [reproduction guide](docs/REPRODUCIBILITY.md) lists commands, exact scopes,
and numerical limitations.

Record what actually ran, its outcome, and the reviewed commit. Distinguish a
rerun from inspection of committed results. Include findings and remaining
uncertainty in the pull request.

## Keep mathematics readable on GitHub

Use [GitHub's protected inline math syntax](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions): a dollar sign and backtick before the expression, then a backtick and dollar sign after it. Use fenced `math` blocks for display equations. These forms preserve TeX escapes such as set braces and spacing commands before math rendering.

Source line breaks do not create equation rows. Use an `aligned` environment for long chains or multiple definitions, and place equation numbers in ordinary mathematical text after the expression. The inspected native MathML layout stacks symbols vertically for `\tag`, so avoid that command. Use upright `\mathrm{Var}` and `\mathrm{rank}` notation where needed; the inspected GitHub renderer rejects `\operatorname` even though ordinary MathJax supports it.

Inspect the rendered preview for missing braces, error boxes, clipped rows, and broken tables. Balanced delimiters and passing numerical checks do not verify layout. Formatting historical notes must preserve their mathematical content and dated scope; the license, source manifest, original verifiers, and recorded reports stay unchanged.

Use `\lt` and `\gt` for strict inequalities, and keep math spans outside surrounding italic-title markers. Put displayed math at paragraph level: the inspected GitHub view leaves indented math fences inside lists as raw code.
