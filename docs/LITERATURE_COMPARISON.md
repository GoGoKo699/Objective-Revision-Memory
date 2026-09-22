# Literature comparison: sharp-rate checkpoint

Checked 22 September 2026. This is a version-specific primary-source comparison, not an originality certificate. The [previous audit](LITERATURE_BASELINE.md) is preserved unchanged. This update distinguishes what the sources state from deductions made in this repository.

## 1. Systematic structures: the access model and affine geometry are established

S. Natarajan Ramamoorthy and C. Rashtchian, *Equivalence of Systematic Linear Data Structures and Matrix Rigidity*, ITCS 2020, [arXiv:1910.11921v1](https://arxiv.org/abs/1910.11921v1), Sections 1.1-1.3. The primary [PDF](https://arxiv.org/pdf/1910.11921) was inspected.

Definition 2 and the surrounding discussion treat retained linear information, input probes, and matrix-rigidity geometry. Section 1.3 explicitly discusses general systematic structures with arbitrary preprocessing and a freely accessible index, as well as the common-bits connection. Thus neither our access model nor the affine condition $q\in W+\operatorname{span}\{e_k\}$ is new. Their exact linearization questions must not be identified with our approximate affine/nonlinear separation.

**Our candidate addition:** a pair-specific rank-profile inequality followed by a matching bounded-error rate for arbitrary preprocessing. We have not established whether an equivalent all-pairs extremal count or stronger result already occurs in that paper's antecedents. Model comparison is not proof of novelty.

## 2. Classical random access codes supply the covering-rate ingredient

J. F. Doriguello and A. Montanaro, *Quantum Random Access Codes for Boolean Functions*, Quantum 5, 402 (2021), [official article](https://quantum-journal.org/papers/q-2021-03-07-402/), [official PDF](https://quantum-journal.org/papers/q-2021-03-07-402/pdf/), [arXiv:2011.06535](https://arxiv.org/abs/2011.06535).

Theorem 2 records a classical shared-randomness random access code with $m\leq[1-h_2(p)]n+7\log_2n$ bits, crediting earlier work. Definitions 6-7 formalize decoding a selected Boolean function from a code and shared randomness. Those definitions do not grant the decoder a subsequent raw-coordinate read. The paper also uses block coding for function-RAC constructions.

**Established ingredients used here:** ordinary entropy-rate reconstruction, block concatenation, majority coding, public symmetrization, and standard covering existence. None is presented as a new code family. The historical reference for the classical shared-randomness background is Ambainis, Leung, Mancinska, and Ozols, [arXiv:0810.2937](https://arxiv.org/abs/0810.2937).

**Our deduction:** the raw read can be spent on the less accurately represented endpoint, so a hierarchy of reconstruction qualities improves on applying one uniform-quality RAC to all coordinates. The full-model converse, rather than the hierarchy alone, is the potentially distinctive contribution. No-probe RAC lower bounds cannot simply be applied to our stronger decoder.

## 3. Biased RACs are a relevant neighbor, not the same query model

G. Pereira Alves, N. Gigena, and J. Kaniewski, *Biased Random Access Codes*, Physical Review A 108, 042608 (2023), [arXiv:2302.08494](https://arxiv.org/abs/2302.08494), with the [v3 HTML](https://arxiv.org/html/2302.08494v3) inspected for the model definition.

This work varies prior probabilities over encoded strings and/or requested characters. It establishes that nonuniformity is already a meaningful RAC design variable. The standard RAC setup described there has no post-encoding raw-archive probe.

**Difference in this checkpoint:** external pair queries are uniform in the converse, and each fixed query is covered by the randomized construction. Quality grades are internal choices, symmetrized by a public permutation; they do not declare some external questions less important. Distinguishing these definitions does not rule out a reduction through biased RAC or weighted source coding results.

## 4. Query-with-sketch: reassess against the sharp statement

S. Garg, S. He, Y. Li, P. A. Papakonstantinou, and X. Yang, *Systematic Data Structure Lower Bounds via the Query-with-Sketch Model*, CCC 2026, [arXiv:2609.18024v1](https://arxiv.org/html/2609.18024v1), Definitions 2.1-2.4 and Lemma 2.5; [proceedings](https://doi.org/10.4230/LIPIcs.CCC.2026.41).

The paper allows a sketch, adaptive raw probes, and public randomness. Its main lemma uses conditional joint min-entropy of a vector output on high-probability good events. It is a close converse-method neighbor.

**Our limited deduction, retained from the baseline audit:** a literal application to one Boolean output cannot yield the desired extensive lower bound. At the empty partial assignment, the relevant good event has mass at least $0.99-2^{-2r}$ for the lemma's integer $r\geq2$. A binary output has an atom of joint mass at least half that. Its joint min-entropy is therefore below $\log_2[2/(0.99-2^{-2r})]<1.11$, whereas the lemma asks for more than $2r\geq4$.

This does not rule out batching, amplification, antecedents, or other theorems. A long batch does not inherit 99% simultaneous success from a constant per-query error without additional work; a union bound supplies only $1-k\varepsilon$, and extra memory/probes for amplification must be charged. The new comparison target is the entire sharp profile curve, not merely an extensive lower bound.

## 5. Help bits and unfinished comparisons

S. Beigi, O. Etesami, and A. Gohari, *The Value of Help Bits in Randomized and Average-Case Complexity*, [arXiv:1408.0499v1](https://arxiv.org/html/1408.0499v1), especially the helper-bit rate-distortion discussion and Theorems 6-7. This is another primary-source precedent for entropy-rate help and nontrivial error dependence. Our problem has one common raw vector, pair requests after encoding, and a strict one-bit raw-read budget; a theorem-level reduction remains to be tested.

Nisan, Rudich, and Saks, *Products and Help Bits in Decision Trees*, is a specific outstanding primary-source comparison. The original full text was not retrieved in this round; citations to it in other papers are not a substitute for checking its theorems. The baseline Ko/linearization and Kondo/RAC comparison queue also remains open. No unsuccessful search is treated as evidence of priority.

## 6. Claim boundary after this checkpoint

**Written result:** arbitrary preprocessing, arbitrary memory-dependent one-bit addresses, exact original parity, and a fixed positive error allowance admit the matching rate derived in the [current note](../RESEARCH_NOTE.md). The construction uses only endpoint probes, showing that third-coordinate probes have no first-order rate advantage under the stated randomized fixed-query guarantees.

**Established machinery:** the systematic model, finite-field linear algebra, independent-coordinate entropy bounds, convex conjugacy, Hamming covers, RAC block construction, and symmetrization.

**Candidate contribution requiring audit:** the pair-coverage profile, its entropy-conjugate converse, and its match with graded endpoint recovery for the full model, including strict affine separation at every nontrivial fixed error.

**Not established:** historical novelty, uniqueness of optimal implementations, efficient explicit near-optimal codes, finite-length optimality, uniform vanishing-error or vanishing-advantage asymptotics, a computational speedup, or a theorem about AI alignment. The work is now a sharper mathematical object to compare, not a certified new paper.
