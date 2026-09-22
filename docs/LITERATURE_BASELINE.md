# Literature comparison and novelty obligations

Checked 22 September 2026. This is a focused, version-specific audit, not a certification of priority. Source statements and our deductions are distinguished below. Search non-detection is not evidence of originality.

## 1. Systematic data structures and affine geometry

**Source:** S. Natarajan Ramamoorthy and C. Rashtchian, *Equivalence of Systematic Linear Data Structures and Matrix Rigidity*, ITCS 2020, [arXiv:1910.11921v1](https://arxiv.org/abs/1910.11921v1), especially Sections 1.1-1.3.

Their systematic model includes an arbitrary input-dependent index, free access to that index, and charged raw-input probes. Their linear specialization uses a row space close in Hamming distance to the query vectors. Section 1.3 identifies the common-bits connection.

**Implication for this project:** the architecture is not new. The condition $`q\in W+\mathrm{span}\{e_k\}`$ is the one-probe instance of established subspace geometry. The affine converse's potentially distinctive content is the all-pairs coverage count and its quantitative bounded-error consequence, not that condition by itself. Our decoder is unrestricted; the exact-or-balanced argument explains why nonlinear decoding cannot help on a uniform affine cell.

**Still open:** whether the rank-coverage count or stronger equivalent bounds already occur in common-bits, rigidity, or help-bit work. No priority conclusion follows from this comparison.

## 2. Query-with-sketch: a direct application is insufficient

**Source:** S. Garg, S. He, Y. Li, P. A. Papakonstantinou, and X. Yang, *Systematic Data Structure Lower Bounds via the Query-with-Sketch Model*, CCC 2026, [arXiv:2609.18024v1](https://arxiv.org/abs/2609.18024v1), Definitions 2.1-2.4 and Lemma 2.5. The [proceedings version](https://doi.org/10.4230/LIPIcs.CCC.2026.41) is also available.

The definitions permit sketches followed by adaptive raw probes and public random tapes. Lemma 2.5 uses conditional joint min-entropy of the output on specified high-probability good events to obtain a sketch lower bound. Its applications group multiple requested outputs together.

**Our deduction, not a claim made by that paper:** applying the lemma literally to one Boolean pair answer cannot establish our extensive memory bound. At the empty partial assignment, the lemma's good-event assumptions give event mass at least $`0.99-2^{-2r}`$ for its integer parameter $`r\geq2`$. A binary output then has an atom of joint probability at least $`(0.99-2^{-2r})/2`$. Its joint min-entropy is at most

```math
\log_2\frac{2}{0.99-2^{-2r}}<1.11,
```

whereas the lemma requires more than $`2r\geq4`$. This rules out that direct scalar instantiation, not every possible reduction or other result in the paper.

A batched reduction needs additional work. Our guarantee for each separate query does not imply 99% joint success for a long output vector. A union bound provides only $`1-k\varepsilon`$ for $`k`$ queries, and repetition changes both retained information and probe cost. Such costs must be charged, not suppressed.

**Still open:** a careful vector-output, amplification, or information-theoretic reduction may reproduce or improve our bounds. The full paper and its antecedents remain relevant. The observation above narrows one comparison; it does not certify novelty.

## 3. Random access codes

**Source:** J. F. Doriguello and A. Montanaro, *Quantum Random Access Codes for Boolean Functions*, Quantum 5, 402 (2021), [arXiv:2011.06535v4](https://arxiv.org/abs/2011.06535v4), Theorems 1-2 and the function-RAC definitions.

The paper records the classical majority success expression and an entropy-rate classical RAC upper bound, and studies decoding Boolean functions of later-selected coordinates. The cited definitions do not grant a subsequent raw-coordinate read.

**Implication:** majority, block coding, symmetrization, and the entropy-rate achievable memory are established ingredients. Our upper bound is a reduction to that work plus one exact parity bit. Any candidate contribution must concern the additional-probe converse and its comparison of encoding maps. A comparison solely against a no-probe RAC lower bound would be invalid because our decoder has a stronger resource.

For the earlier classical shared-randomness background see A. Ambainis, D. Leung, L. Mancinska, and M. Ozols, *Quantum Random Access Codes with Shared Randomness*, [arXiv:0810.2937](https://arxiv.org/abs/0810.2937).

## 4. Additional comparison queue

These remain comparison targets, not sources of an endorsement of our results:

- Y. K. Ko, *Efficient Linearization Implies the Multiphase Conjecture*, [ECCC TR22-122](https://eccc.weizmann.ac.il/report/2022/122/), and *Lower Bounds for Linear Operators*, [arXiv:2509.02730](https://arxiv.org/abs/2509.02730). Exact linearization statements must not be conflated with our bounded-error comparison.
- R. Kondo and coauthors, *Random Access Codes: Explicit Constructions, Optimality, and Classical-Quantum Gaps*, [arXiv:2604.21274v3](https://arxiv.org/abs/2604.21274v3). Compare restrictions on reconstruction representatives with restrictions on encoding maps. A linear repetition codebook can have a nonlinear majority encoder.
- Nisan, Rudich, and Saks, *Products and help bits in decision trees*, as cited by the query-with-sketch paper. Complete the comparison of per-output decision trees with a shared preprocessing message.

The current audit does not prove that no known theorem subsumes this project. Precise error dependence, a clean proof, and the usefulness of the finite separation must each be assessed independently of terminology.
