# Literature comparison: sharp-rate audit and continuation

Checked 22 September 2026, including the continuation from `4e2c579795e2e780e132e3feb8072d2260ab3a7f`. This is a version-specific primary-source comparison, not an originality certificate. The [baseline audit](LITERATURE_BASELINE.md) is preserved unchanged. The [detailed sharp-rate audit](reviews/SHARP_RATE_AUDIT.md) supplies the full resource ledger and proofs of the reductions summarized here. Source statements and repository deductions are distinguished below.

## 1. Systematic structures: the access model and affine geometry are established

S. Natarajan Ramamoorthy and C. Rashtchian, *Equivalence of Systematic Linear Data Structures and Matrix Rigidity*, ITCS 2020, [arXiv:1910.11921v1](https://arxiv.org/abs/1910.11921v1), Sections 1.1-1.3. The primary [PDF](https://arxiv.org/pdf/1910.11921) was inspected.

Sections 1.1-1.3 and Theorem 1 treat retained linear information, input probes, and matrix-rigidity geometry. Section 1.3 explicitly discusses general systematic structures with arbitrary preprocessing and a freely accessible index, as well as the common-bits connection. Thus neither our access model nor the affine condition $q\in W+\operatorname{span}\{e_k\}$ is new. Their exact linearization questions must not be identified with our approximate affine/nonlinear separation.

**Our candidate addition:** a pair-specific rank-profile inequality followed by a matching bounded-error rate for arbitrary preprocessing. We have not established whether an equivalent all-pairs extremal count or stronger result already occurs in that paper's antecedents. Model comparison is not proof of novelty.

## 2. Classical random access codes supply the covering-rate ingredient

J. F. Doriguello and A. Montanaro, *Quantum Random Access Codes for Boolean Functions*, Quantum 5, 402 (2021), [official article](https://quantum-journal.org/papers/q-2021-03-07-402/), [official PDF](https://quantum-journal.org/papers/q-2021-03-07-402/pdf/), [arXiv:2011.06535](https://arxiv.org/abs/2011.06535).

Theorem 2 explicitly states a classical **private-randomness** random access code with $m\leq[1-h_2(p)]n+7\log_2n$ bits, crediting Ambainis, Nayak, Ta-Shma, and Vazirani (1999), Theorem 2.2. Revealing these coins gives an available public-randomness upper bound here. Definitions 6-7 formalize decoding a selected Boolean function from a code and shared randomness. They do not grant a subsequent raw-coordinate read. The paper also uses block coding for function-RAC constructions.

**Established ingredients used here:** ordinary entropy-rate reconstruction, block concatenation, majority coding, public symmetrization, and standard covering existence. None is presented as a new code family. Ambainis, Leung, Mancinska, and Ozols, [arXiv:0810.2937](https://arxiv.org/abs/0810.2937), is additional shared-randomness background, not the attribution for the displayed Theorem 2 bound.

**Our deduction:** the raw read can be spent on the less accurately represented endpoint, so a hierarchy of reconstruction qualities improves on applying one uniform-quality RAC to all coordinates. The full-model converse, rather than the hierarchy alone, is the potentially distinctive contribution. No-probe RAC lower bounds cannot simply be applied to our stronger decoder.

## 3. Biased RACs are a relevant neighbor, not the same query model

G. Pereira Alves, N. Gigena, and J. Kaniewski, *Biased Random Access Codes*, Physical Review A 108, 042608 (2023), [arXiv:2302.08494](https://arxiv.org/abs/2302.08494), with the [v3 HTML](https://arxiv.org/html/2302.08494v3) inspected for the model definition.

This work varies prior probabilities over encoded strings and/or requested characters. It establishes that nonuniformity is already a meaningful RAC design variable. The standard RAC setup described there has no post-encoding raw-archive probe.

**Difference in this checkpoint:** external pair queries are uniform in the converse, and each fixed query is covered by the randomized construction. Quality grades are internal choices, symmetrized by a public permutation; they do not declare some external questions less important. Distinguishing these definitions does not rule out a reduction through biased RAC or weighted source coding results.

## 4. Query-with-sketch: reassess against the sharp statement

S. Garg, S. He, Y. Li, P. A. Papakonstantinou, and X. Yang, *Systematic Data Structure Lower Bounds via the Query-with-Sketch Model*, CCC 2026, [arXiv:2609.18024v1](https://arxiv.org/html/2609.18024v1), Definitions 2.1-2.4 and Lemma 2.5; [proceedings](https://doi.org/10.4230/LIPIcs.CCC.2026.41).

The paper allows a sketch, adaptive raw probes, and public randomness. Its main lemma uses conditional joint min-entropy of a vector output on high-probability good events. It is a close converse-method neighbor.

**Our limited deduction, retained from the baseline audit:** a literal application to one Boolean output cannot yield the desired extensive lower bound. At the empty partial assignment, the relevant good event has mass at least $0.99-2^{-2r}$ for the lemma's integer $r\geq2$. A binary output has an atom of joint mass at least half that. Its joint min-entropy is therefore below $\log_2[2/(0.99-2^{-2r})]<1.11$, whereas the lemma asks for more than $2r\geq4$.

The detailed audit also checks direct batching. For $k$ exclusion queries, exposing at most $2k$ endpoint bits leaves the entire output dependent only on total parity, so its support has size at most two. The lemma's expected-cost requirement, using the generic $k$-probe bound, requires an exposure budget at least $10k$; the same min-entropy obstruction then applies. Amplification costs additional memory and probes and does not remove this support obstruction. This rules out that direct application, not indirect reductions or a separately proved smaller actual probe cost.

## 5. Help bits: a real lower bound, with a limited scope

S. Beigi, O. Etesami, and A. Gohari, *The Value of Help Bits in Randomized and Average-Case Complexity*, [arXiv:1408.0499v1](https://arxiv.org/html/1408.0499v1), Theorems 6-7, supplies entropy-rate helper coding in computational settings. Theorem 6's finite collection of known language instances has unrestricted input access; Theorem 7 concerns independent instances. Pair parity is polynomial-time computable there, so those hardness hypotheses do not yield our one-read bound directly.

Nisan, Rudich, and Saks, *Products and Help Bits in Decision Trees*: the original [author-hosted manuscript](https://www.cs.cmu.edu/~rudich/papers/helpbits.ps) has now been retrieved and read. Theorem 3.1, printed p.4, gives the product bound used in the audit; Theorem 4.1 and Lemma 4.1 are also compared there. These locations refer to the 12-page manuscript, not uninspected journal numbering.

**Our deduction:** apply Theorem 3.1 to $k=\lfloor n/2\rfloor$ disjoint pair parities after fixing the seed and memory value. An exponential moment and the at-most-$2^B$ possible memories give $B\ge k[1-h_2(\varepsilon)]$. Random matching selection preserves an input-and-pair average-error hypothesis. This is a genuine extensive lower bound, but weaker than Theorem S. The product theorem does not apply directly to overlapping pairs. A direct residual-independence proof and sharp bipartite corollary appear in [rank-profile extensions](RANK_PROFILE_EXTENSIONS.md).

## 6. The entropy ingredient and weighted curve have explicit antecedents

Russell Impagliazzo, Cristopher Moore, and Alexander Russell, *An Entropic Proof of Chang's Inequality*, [arXiv:1205.0263v2](https://arxiv.org/pdf/1205.0263v2), Eq. (1) and Section 2, printed pp.1-2. Their pre-quadratic entropy bound and change to any binary character basis imply exactly the independent-bias budget used here. Set $A$ to a uniform memory cell, $\alpha=|A|/2^n$, and $t_\ell=|\widehat{1_A}(a_\ell)|/\alpha$. Complete the independent residuals to a basis and discard the other nonnegative entropy costs to obtain $\sum_\ell c(t_\ell)\le\log_2(1/\alpha)$. The later quadratic relaxation is unnecessary. This ingredient deserves explicit attribution.

Emin Martinian, Gregory W. Wornell, and Ram Zamir, *Source Coding With Distortion Side Information*, IEEE Transactions on Information Theory 54(10), 4638-4665 (2008), [author PDF](https://sia.mit.edu/wp-content/uploads/2015/04/2008-martinian-wornell-zamir-it.pdf), Theorems 2-3, Section IV-E Eqs. (40)-(41), Appendix II Eq. (121). The finite-label weighted fair-binary formula specializes, with zero offset and weight $2u$, to precisely our scalar variational problem. Its logistic distortion allocation becomes $b(u)=\tanh(au)$; finite partitions give the continuum limit. [RESEARCH_NOTE.md](../RESEARCH_NOTE.md) writes the substitutions explicitly. Neither this curve nor ordinary graded binary coding is claimed new.

The distinction to be proved is operational: their distortion weights are supplied externally; ours arise from the pair-subset rank geometry, while the decoder receives a late query and one raw read. Theorem S equates the optimal first-order rates. An identity of scalar objectives alone would not prove that converse.

## 7. One-star partial matrices and approximate prediction

Jukna and Schnitger, *Min-Rank Conjecture for Log-Depth Circuits*, [arXiv:1005.1009v1](https://arxiv.org/html/1005.1009v1), Remark 1.4 and Lemma 2.3, give exact one-star solution-set bounds and common-bit conditioning. A Boolean function of one bit is affine, so an exact solution fiber has at most $2^{n-r}$ points for a rank-$r$ residual system.

**Our reduction:** fix seed and memory first; the address is then fixed for each pair and each error bit is affine with row $e_i+e_j+\beta e_k$. Independent error rows give an entropy budget by the same fiber bound and subadditivity. This does not require affine encoding cells. Full-matrix min-rank alone does not count high-bias pair labels: the missing input is a bound for **every subset** of the pair-labelled residuals, followed by threshold integration. The audit makes this distinction explicit rather than claiming that different notation establishes novelty.

Meir and Wigderson, *Prediction from Partial Information and Hindsight, with Application to Circuit Lower Bounds*, [ECCC TR17-149 revision 5](https://eccc.weizmann.ac.il/report/2017/149/revision/5/download/), Theorem 1.3 and Corollary 1.5, concern predicting coordinates from other coordinates of a high-entropy binary vector. Smal and Talebanfard's corrected [TR17-191 revision 2](https://eccc.weizmann.ac.il/report/2017/191/revision/2/download/), June 1, 2018, Theorem 3 and Corollary 1, improve the decision-tree bound: entropy deficit $k$ permits at most $k(q+1)/[1-h_2((1+\theta)/2)]$ coordinates with prediction bias $\theta$ using depth $q$.

**Version caveat:** the [ECCC revision history](https://eccc.weizmann.ac.il/report/2017/191/) acknowledges a flaw in the original stronger arbitrary-witness claim. Revision 2 restricts the approximate theorem to pairwise inconsistent witnesses; decision trees satisfy this requirement. We use that corrected result.

**Our obstruction to a direct reduction:** the vector of all $N$ pair parities has entropy at most $n-1$, hence entropy deficit at least $N-n+1$ even without a summary. The coordinate-prediction bound becomes vacuous on this lifted vector. Raw $X_k$ is also not a function of pair parities alone; adding an anchor changes locality, and target-coordinate reads are forbidden by the cited theorem. A basis change removes redundant outputs but loses the all-pairs objective and raw-coordinate access. More elaborate reductions remain possible.

The detailed audit also compares Ko's charged linear-probe theorems, Kondo et al.'s no-shared-randomness RACs, and Permuter-Weissman's decoder-action source coding. Those precise model mismatches have not been promoted into global non-subsumption claims.

## 8. Claim boundary after integration

**Written result:** arbitrary preprocessing, arbitrary memory-dependent one-bit addresses, exact original parity, and a fixed positive error allowance admit the matching rate derived in the [current note](../RESEARCH_NOTE.md). The construction uses only endpoint probes, showing that third-coordinate probes have no first-order rate advantage under the stated randomized fixed-query guarantees.

**Established machinery:** the systematic model, one-star Boolean affinity and fiber counting, the entropic Chang inequality, convex conjugacy, weighted binary rate-distortion coding, Hamming covers, RAC block construction, and symmetrization.

**Candidate contribution requiring priority resolution:** the pair-specific all-subsets rank envelope and its matching application to arbitrary summary-dependent one-bit probes, equating the optimal first-order rate to an established weighted coding problem. The exact affine comparison is a consequence; generic nonlinear superiority is not itself novel. The continuation's general rank-envelope lemma, low-rank refinement, and bipartite theorem are explicit deductions, not certified new results.

**Not established:** historical novelty, uniqueness of optimal implementations, efficient explicit near-optimal codes, finite-length optimality, uniform vanishing-error or vanishing-advantage asymptotics, a computational speedup, or a theorem about AI alignment. The work is now a sharper mathematical object to compare, not a certified new paper.
