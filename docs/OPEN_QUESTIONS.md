# Open questions

The [central proof](PAIR_QUERY_NOTE.md) determines the sharp leading memory
rate at each fixed error strictly between zero and one half. The questions
below concern regimes or guarantees beyond that theorem.

## Mathematical directions

| Question | Boundary of the existing result |
| --- | --- |
| What is the finite-length optimum at positive error? | The matching asymptotic rate and finite converse do not determine every finite optimum. The 529-versus-565-bit example is a covering-existence certificate compared with an affine lower bound. |
| Can explicit efficient codes approach the sharp rate? | The attaining covers are existence constructions; efficient encoding, decoding, and codebook construction are not established. |
| What are the second-order terms? | The leading-rate theorem leaves sublinear memory corrections undetermined. |
| What is the full finite pair-coverage envelope? | The low-rank extremum has a specified range, and the Hamming-kernel example disproves extending its formula to all ranks. See the [rank-profile bounds](RANK_PROFILE_EXTENSIONS.md). |
| What happens when error varies with archive size? | Fixed-positive-error asymptotics do not imply uniform vanishing-error or vanishing-advantage results. |
| What changes under stronger query guarantees? | The fixed-pair and table-distortion criteria do not protect against a pair selected after observing the seed and summary. |

Each question uses the [resource model](READING_GUIDE.md#resource-accounting)
and [error quantifiers](READING_GUIDE.md#keep-the-error-quantifiers-separate)
stated in the reading guide. Changes to the query family, error criterion,
or order of limits define a different problem.
