# Open questions

The [central proof](PAIR_QUERY_NOTE.md) determines the sharp leading memory
rate at each fixed error strictly between zero and one half. The questions
below concern regimes or guarantees beyond that theorem. The
[results and limitations](STATUS.md) summarize what is established, and the
[contribution assessment](CONTRIBUTION_ASSESSMENT.md) states the bounded
novelty and significance judgment.

## Mathematical directions

| Question | Boundary of the existing result |
| --- | --- |
| What is the finite-length optimum at positive error? | The matching asymptotic rate and finite converse do not determine every finite optimum. The 529-versus-565-bit example is a covering-existence certificate compared with an affine lower bound. |
| Can explicit efficient codes approach the sharp rate? | The attaining covers are existence constructions; efficient encoding, decoding, and codebook construction are not established. |
| What are the second-order terms? | The leading-rate theorem leaves sublinear memory corrections undetermined. |
| What is the full finite pair-coverage envelope? | The low-rank extremum has a specified range, and the Hamming-kernel example disproves extending its formula to all ranks. See the [rank-profile bounds](RANK_PROFILE_EXTENSIONS.md). |
| What happens when error varies with archive size? | Fixed-positive-error asymptotics do not imply uniform vanishing-error or vanishing-advantage results. |
| What changes under stronger query guarantees? | The fixed-pair and table-distortion criteria do not protect against a pair selected after observing the seed and summary. |

Each extension needs explicit resource accounting: worst-case retained bits,
exact total parity for the revision task, one raw-coordinate read per query,
and the permitted dependence of its address. Independent randomness,
codebooks, computation, and the immutable archive are uncharged;
input-dependent caches and transcripts are charged. Changes to the query
family, error criterion, or order of limits define a different problem.

## Novelty and significance

The proposed original contribution is the task-specific extremal evaluation
over all legal one-read strategies. The weighted coding curve, entropy
machinery, geometric count, and general coding conversions have established
antecedents, documented in the [literature comparison](LITERATURE_COMPARISON.md).

Historical coverage is incomplete. A prior theorem could strengthen, narrow,
or overturn the proposed originality claim if an explicit reduction preserves
summary size, raw-read access, the growing single-archive limit, and the error
quantifiers. Inaccessible sources remain uninspected; search failure is not
evidence of originality. Independent specialist review has not been obtained.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
