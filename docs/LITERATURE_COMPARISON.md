# Literature comparison: sharp-rate audit and continuation

Checked 22 September 2026, most recently against `2b240fa20b9c8d585106edb512a5f18200aafd33`. This is a version-specific primary-source comparison, not an originality certificate. The [baseline audit](LITERATURE_BASELINE.md) retains its historical content; math formatting is normalized for GitHub. The [detailed sharp-rate audit](reviews/SHARP_RATE_AUDIT.md) supplies the full resource ledger and proofs of the reductions summarized here. Source statements and repository deductions are distinguished below. Sections 9–10 attribute the geometry and general coding conversions. Section 11 gives a bounded comparison of the remaining decoder-ball theorem; the [self-contained note](PAIR_QUERY_NOTE.md) supplies its complete central proof.

## 1. Systematic structures: the access model and affine geometry are established

S. Natarajan Ramamoorthy and C. Rashtchian, *Equivalence of Systematic Linear Data Structures and Matrix Rigidity*, ITCS 2020, [arXiv:1910.11921v1](https://arxiv.org/abs/1910.11921v1), Sections 1.1-1.3. The primary [PDF](https://arxiv.org/pdf/1910.11921) was inspected.

Sections 1.1-1.3 and Theorem 1 treat retained linear information, input probes, and matrix-rigidity geometry. Section 1.3 explicitly discusses general systematic structures with arbitrary preprocessing and a freely accessible index, as well as the common-bits connection. Thus neither our access model nor the affine condition $`q\in W+\mathrm{span}\{e_k\}`$ is new. Their exact linearization questions must not be identified with our approximate affine/nonlinear separation.

**Our candidate addition:** the matching bounded-error rate for arbitrary preprocessing and memory-dependent addresses. The geometric count is an elementary deduction from established basis facts, as Section 9 now makes explicit. The bounded assessment in Section 12 retains this proposed originality claim; model comparison alone is not proof of novelty.

## 2. Classical random access codes supply the covering-rate ingredient

J. F. Doriguello and A. Montanaro, *Quantum Random Access Codes for Boolean Functions*, Quantum 5, 402 (2021), [official article](https://quantum-journal.org/papers/q-2021-03-07-402/), [official PDF](https://quantum-journal.org/papers/q-2021-03-07-402/pdf/), [arXiv:2011.06535](https://arxiv.org/abs/2011.06535).

Theorem 2 explicitly states a classical **private-randomness** random access code with $`m\leq[1-h_2(p)]n+7\log_2n`$ bits, crediting Ambainis, Nayak, Ta-Shma, and Vazirani (1999), Theorem 2.2. Revealing these coins gives an available public-randomness upper bound here. Definitions 6-7 formalize decoding a selected Boolean function from a code and shared randomness. They do not grant a subsequent raw-coordinate read. The paper also uses block coding for function-RAC constructions.

**Established ingredients used here:** ordinary entropy-rate reconstruction, block concatenation, majority coding, public symmetrization, and standard covering existence. None is presented as a new code family. Ambainis, Leung, Mancinska, and Ozols, [arXiv:0810.2937](https://arxiv.org/abs/0810.2937), is additional shared-randomness background, not the attribution for the displayed Theorem 2 bound.

**Our deduction:** the raw read can be spent on the less accurately represented endpoint, so a hierarchy of reconstruction qualities improves on applying one uniform-quality RAC to all coordinates. The full-model converse, rather than the hierarchy alone, is the potentially distinctive contribution. No-probe RAC lower bounds cannot simply be applied to our stronger decoder.

## 3. Biased RACs are a relevant neighbor, not the same query model

G. Pereira Alves, N. Gigena, and J. Kaniewski, *Biased Random Access Codes*, Physical Review A 108, 042608 (2023), [arXiv:2302.08494](https://arxiv.org/abs/2302.08494), with the [v3 HTML](https://arxiv.org/html/2302.08494v3) inspected for the model definition.

This work varies prior probabilities over encoded strings and/or requested characters. It establishes that nonuniformity is already a meaningful RAC design variable. The standard RAC setup described there has no post-encoding raw-archive probe.

**Difference in this checkpoint:** external pair queries are uniform in the converse, and each fixed query is covered by the randomized construction. Quality grades are internal choices, symmetrized by a public permutation; they do not declare some external questions less important. Distinguishing these definitions does not rule out a reduction through biased RAC or weighted source coding results.

## 4. Query-with-sketch: reassess against the sharp statement

S. Garg, S. He, Y. Li, P. A. Papakonstantinou, and X. Yang, *Systematic Data Structure Lower Bounds via the Query-with-Sketch Model*, CCC 2026, [arXiv:2609.18024v1](https://arxiv.org/html/2609.18024v1), Definitions 2.1-2.4 and Lemma 2.5; [proceedings](https://doi.org/10.4230/LIPIcs.CCC.2026.41).

The paper allows a sketch, adaptive raw probes, and public randomness. Its main lemma uses conditional joint min-entropy of a vector output on high-probability good events. It is a close converse-method neighbor.

**Our limited deduction, retained from the baseline audit:** a literal application to one Boolean output cannot yield the desired extensive lower bound. At the empty partial assignment, the relevant good event has mass at least $`0.99-2^{-2r}`$ for the lemma's integer $`r\geq2`$. A binary output has an atom of joint mass at least half that. Its joint min-entropy is therefore below $`\log_2[2/(0.99-2^{-2r})]<1.11`$, whereas the lemma asks for more than $`2r\geq4`$.

The detailed audit also checks direct batching. For $`k`$ exclusion queries, exposing at most $`2k`$ endpoint bits leaves the entire output dependent only on total parity, so its support has size at most two. The lemma's expected-cost requirement, using the generic $`k`$-probe bound, requires an exposure budget at least $`10k`$; the same min-entropy obstruction then applies. Amplification costs additional memory and probes and does not remove this support obstruction. This rules out that direct application, not indirect reductions or a separately proved smaller actual probe cost.

## 5. Help bits: a real lower bound, with a limited scope

S. Beigi, O. Etesami, and A. Gohari, *The Value of Help Bits in Randomized and Average-Case Complexity*, [arXiv:1408.0499v1](https://arxiv.org/html/1408.0499v1), Theorems 6-7, supplies entropy-rate helper coding in computational settings. Theorem 6's finite collection of known language instances has unrestricted input access; Theorem 7 concerns independent instances. Pair parity is polynomial-time computable there, so those hardness hypotheses do not yield our one-read bound directly.

Nisan, Rudich, and Saks, *Products and Help Bits in Decision Trees*: the original [author-hosted manuscript](https://www.cs.cmu.edu/~rudich/papers/helpbits.ps) has now been retrieved and read. Theorem 3.1, printed p.4, gives the product bound used in the audit; Theorem 4.1 and Lemma 4.1 are also compared there. These locations refer to the 12-page manuscript, not uninspected journal numbering.

**Our deduction:** apply Theorem 3.1 to $`k=\lfloor n/2\rfloor`$ disjoint pair parities after fixing the seed and memory value. An exponential moment and the at-most-$`2^B`$ possible memories give $`B\ge k[1-h_2(\varepsilon)]`$. Random matching selection preserves an input-and-pair average-error hypothesis. This is a genuine extensive lower bound, but weaker than Theorem S. The product theorem does not apply directly to overlapping pairs. A direct residual-independence proof and sharp bipartite corollary appear in [rank-profile extensions](RANK_PROFILE_EXTENSIONS.md).

## 6. The entropy ingredient and weighted curve have explicit antecedents

Russell Impagliazzo, Cristopher Moore, and Alexander Russell, *An Entropic Proof of Chang's Inequality*, [arXiv:1205.0263v2](https://arxiv.org/pdf/1205.0263v2), Eq. (1) and Section 2, printed pp.1-2. Their pre-quadratic entropy bound and change to any binary character basis imply exactly the independent-bias budget used here. Set $`A`$ to a uniform memory cell, $`\alpha=|A|/2^n`$, and $`t_\ell=|\widehat{1_A}(a_\ell)|/\alpha`$. Complete the independent residuals to a basis and discard the other nonnegative entropy costs to obtain $`\sum_\ell c(t_\ell)\le\log_2(1/\alpha)`$. The later quadratic relaxation is unnecessary. This ingredient deserves explicit attribution.

Emin Martinian, Gregory W. Wornell, and Ram Zamir, *Source Coding With Distortion Side Information*, IEEE Transactions on Information Theory 54(10), 4638-4665 (2008), [author PDF](https://sia.mit.edu/wp-content/uploads/2015/04/2008-martinian-wornell-zamir-it.pdf), Theorems 2-3, Section IV-E Eqs. (40)-(41), Appendix II Eq. (121). The finite-label weighted fair-binary formula specializes, with zero offset and weight $`2u`$, to precisely our scalar variational problem. Its logistic distortion allocation becomes $`b(u)=\tanh(au)`$; finite partitions give the continuum limit. [RESEARCH_NOTE.md](../RESEARCH_NOTE.md) writes the substitutions explicitly. Neither this curve nor ordinary graded binary coding is claimed new.

The distinction to be proved is operational: their distortion weights are supplied externally; ours arise from the pair-subset rank geometry, while the decoder receives a late query and one raw read. Theorem S equates the optimal first-order rates. An identity of scalar objectives alone would not prove that converse.

## 7. One-star partial matrices and approximate prediction

Jukna and Schnitger, *Min-Rank Conjecture for Log-Depth Circuits*, [arXiv:1005.1009v1](https://arxiv.org/html/1005.1009v1), Remark 1.4 and Lemma 2.3, give exact one-star solution-set bounds and common-bit conditioning. A Boolean function of one bit is affine, so an exact solution fiber has at most $`2^{n-r}`$ points for a rank-$`r`$ residual system.

**Our reduction:** fix seed and memory first; the address is then fixed for each pair and each error bit is affine with row $`e_i+e_j+\beta e_k`$. Independent error rows give an entropy budget by the same fiber bound and subadditivity. This does not require affine encoding cells. Full-matrix min-rank alone does not count high-bias pair labels: the missing input is a bound for **every subset** of the pair-labelled residuals, followed by threshold integration. The audit makes this distinction explicit rather than claiming that different notation establishes novelty.

Meir and Wigderson, *Prediction from Partial Information and Hindsight, with Application to Circuit Lower Bounds*, [ECCC TR17-149 revision 5](https://eccc.weizmann.ac.il/report/2017/149/revision/5/download/), Theorem 1.3 and Corollary 1.5, concern predicting coordinates from other coordinates of a high-entropy binary vector. Smal and Talebanfard's corrected [TR17-191 revision 2](https://eccc.weizmann.ac.il/report/2017/191/revision/2/download/), June 1, 2018, Theorem 3 and Corollary 1, improve the decision-tree bound: entropy deficit $`k`$ permits at most $`k(q+1)/[1-h_2((1+\theta)/2)]`$ coordinates with prediction bias $`\theta`$ using depth $`q`$.

**Version caveat:** the [ECCC revision history](https://eccc.weizmann.ac.il/report/2017/191/) acknowledges a flaw in the original stronger arbitrary-witness claim. Revision 2 restricts the approximate theorem to pairwise inconsistent witnesses; decision trees satisfy this requirement. We use that corrected result.

**Our obstruction to a direct reduction:** the vector of all $`N`$ pair parities has entropy at most $`n-1`$, hence entropy deficit at least $`N-n+1`$ even without a summary. The coordinate-prediction bound becomes vacuous on this lifted vector. Raw $`X_k`$ is also not a function of pair parities alone; adding an anchor changes locality, and target-coordinate reads are forbidden by the cited theorem. A basis change removes redundant outputs but loses the all-pairs objective and raw-coordinate access. More elaborate reductions remain possible.

The detailed audit also compares Ko's charged linear-probe theorems, Kondo et al.'s no-shared-randomness RACs, and Permuter-Weissman's decoder-action source coding. Those precise model mismatches have not been promoted into global non-subsumption claims.

## 8. Targeted priority decision: geometry, caching, and local source coding

This pass reviewed `b9394cd2ea64c45943e66ba7c61ae665f3df77c3`. A prior bound need not reproduce the exact finite formula: a uniform all-subsets envelope $`|E|\le nr-r^2/2+o(n^2)`$ already suffices, together with the established entropy/coding ingredients. The [theorem brief](THEOREM_BRIEF.md) proves that subsumption criterion and states the operational contribution.

**Classical matching extremality gives a partial reduction.** Erdős and Gallai, *On Maximal Paths and Circuits of Graphs* (1959), [original PDF](https://www.renyi.hu/~p_erdos/1959-10.pdf), Theorem (4.1), printed p.354, with the extremal function on p.346. A graph of matching number at most $`r`$ has at most $`\max\{\binom{2r+1}{2},nr-r(r+1)/2\}`$ edges for $`n\ge2r+1`$. Our matching-residual independence proves that this applies to every selected pair subset. It recovers the exact coordinate-subspace extremum when $`n\ge(5r+3)/2`$, a substantial part of the previously proved range $`n\ge2r+2`$. At $`r/n\to0.45`$, however, it permits $`0.405n^2+O(n)`$ edges, while the required profile permits $`0.34875n^2+O(n)`$. Thus this particular classical reduction misses leading-order information.

**Distinct low-weight vectors are a different extremal statistic.** Briggs and Pegden, *Extremal Collections of k-Uniform Vectors*, [arXiv:1801.09609v3](https://arxiv.org/pdf/1801.09609v3), Theorem 1.2 and Lemma 2.1, bound distinct fixed-weight vectors at a specified rank. Pair labels can repeat a residual; direct substitution into $`(n-1)A_1+A_2+3A_3`$ loses the needed bound at linear rank. The audit gives two dimension-three subspaces with identical full weight enumerators but coverage six versus seven, and the precise multiplicity-weighted quotient formulation. This defeats identifying coverage with a weight enumerator; it does not exclude a sophisticated bound using those methods.

**Sequential coding permits a stronger delivery operation.** Wang, Lim, and Gastpar, *Information-Theoretic Caching: Sequential Coding for Computing*, [arXiv:1504.00553v2](https://arxiv.org/pdf/1504.00553v2), Section II and Theorem 1, Eqs. (1)-(2), characterize iid repeated-instance cache/update rates by $`R_c\ge I(X;V\mid Y)`$ and $`R_u\ge H(f(X,Y)\mid V,Y)`$. The update encoder sees the source and requests. Our substitution $`V=p(X)`$, $`Y=\{i,j\}`$ gives rates $`(1,1)`$; directly, one cached parity bit and a computed update $`X_i\oplus X_j`$ solve every query exactly. Our model permits one raw coordinate bit, not that computed update. A reduction that records only its one-bit length discards the essential restriction. The repeated-archive asymptotic parameter also differs from growing one archive.

**Local source decoding charges different storage and access.** Makhdoumi, Huang, Médard, and Polyanskiy, *On Locally Decodable Source Coding*, [arXiv:1308.5239v2](https://arxiv.org/pdf/1308.5239v2), Definition 2, Theorem 5, Proposition 2, and Section III, study average bit distortion with fixed neighborhoods of encoded bits. Their rate-distortion achievability supplies coding background. Representing our scheme literally by $`(M,X)`$ pays $`n+B`$ stored bits and may require $`B`$ summary-bit accesses followed by a summary-dependent raw access. Neither cost is the one charged in this repository; lifting pair outputs also loses the iid source hypothesis. Their quoted bounds therefore do not yield the sharp summary-only converse by this direct translation.

**Fixed functional side information does not optimize the probe choice.** Gupta and Rajan, *Error-Correcting Functional Index Codes, Generalized Exclusive Laws and Graph Coloring*, [arXiv:1510.04820v2](https://arxiv.org/pdf/1510.04820v2), Sections III-IV, Propositions 1-2, characterize exact codes using fixed receiver Has/Want functions and confusion graphs. A fixed address assignment is a special case. With $`k=k(M,i,j)`$, the candidate Has-function depends on the encoder being optimized, so a fixed-instance characterization does not evaluate the required joint choice. Their broadcast-error correction also differs from allowed task error. Gál and Miltersen's [BRICS RS-03-44](https://www.brics.dk/RS/03/44/BRICS-RS-03-44.pdf), Theorem 2 and Section 3, is a historical systematic prefix-parity application of Nisan–Rudich–Saks, rather than an all-pairs approximate profile.

The Gibbs/entropy reformulation is also established machinery: Carlen–Cordero-Erausquin's [October 2007 manuscript](https://webusers.imj-prg.fr/~dario.cordero/Docs/articles/subaddOCT1.pdf), Eq. (2.4) and Theorem 2.1's proof, states the general entropy variational relation. This supplies an explicit primary antecedent for the duality step; it supplies no pair-specific count.

## 9. Complete geometric reductions: elementary basis facts suffice

**Additive formulation.** Chaim Even-Zohar, *On Sums of Generating Sets in $`(\mathbb Z_2)^n`$*, [arXiv:1108.4902v2](https://arxiv.org/pdf/1108.4902v2), Theorem 1, printed p.2, and Example 11 in Section 3.1, printed p.7. For an affine basis $`A=\{0,b_1,\ldots,b_d\}`$, the established independent-points example gives $`|A+A|=1+d+\binom d2`$. Theorem 1 also implies this by setting its $`t=d,k=1,w=0`$; its size hypothesis holds for $`d\ge2`$, and smaller dimensions are immediate. The source's substantial sumset machinery is unnecessary for this elementary specialization.

**Our full reduction.** For any selected residual family spanning $`W`$ of rank $`r`$, let $`d=n-r`$, $`v_i=e_i+W`$, and $`S=\{0,v_1,\ldots,v_n\}`$. Choose basis-coordinate representatives $`b_1,\ldots,b_d`$, so $`A\subseteq S`$ and $`|S|\le n+1`$. A covered pair requires $`v_i+v_j\in S`$. Every element of $`(A+A)\setminus S`$ gives a distinct uncovered pair of basis-coordinate representatives. Hence

```math
\#\{\text{uncovered pairs}\}\ge |A+A|-|S|
\ge\binom d2-r,
```

and therefore $`|E|\le\binom n2-\binom{n-r}{2}+r=nr-r(r-1)/2`$. This is the entire finite envelope, uniformly over ranks and selected pair subsets. Zero images and repeated coordinate images are retained: the argument only identifies distinct missing pairs among a chosen coordinate basis. It does not equate labelled coverage with a support-size statistic.

**Matroid formulation.** Tutte, *Lectures on Matroids*, J. Res. NBS 69B (1965), [primary paper](https://doi.org/10.6028/jres.069B.001), Section 2.2, printed p.3, paragraph between (2.21) and (2.22), proves the uniqueness of a circuit intersecting a minimal circuit-hitting set in a specified singleton. In modern language this is fundamental-circuit uniqueness relative to the complementary basis. Tutte's rank convention must not be substituted for modern rank without translation.

Apply this to the labelled coordinate-image matroid. A covered pair of basis coordinates together with its completing nonbasis coordinate forms a three-element circuit. One nonbasis coordinate can complete at most one such pair, so the $`r`$ nonbasis coordinates complete at most $`r`$ basis pairs. This gives both the numerical envelope and the almost-vertex-cover statement. Loops and parallel elements are not discarded. This is a routine application of fundamental-circuit uniqueness, not a new extremal matroid principle.

**Revised attribution.** These complete reductions replace the earlier unresolved-geometric-priority target. The envelope should be presented as a task-specific elementary lemma with explicit antecedents. Neither source is asserted to have stated the raw-read model or its sharp memory theorem. The remaining historical question concerns the operational synthesis, including its [excess-distortion formulation](EXCESS_DISTORTION.md), not whether independent basis pairs have distinct sums. No further general search for a standalone geometric theorem is required for this attribution decision.

## 10. General lossy coding and an exact decoder-action embedding

**General distortion already includes complete strategies.** Kostina and Verdú,
*Fixed-length lossy compression in the finite blocklength regime*,
[arXiv:1102.3944v3](https://arxiv.org/pdf/1102.3944), 4 February 2014,
Definition 1 and Section IV, Theorems 8–10, Eqs. (60), (65), (70), printed p.6.
Take a whole archive as one source symbol and a complete one-read decoder
strategy as one reproduction symbol. Distortion is the fraction of wrong pair
answers. A $`B`$-bit summary chooses at most $`2^B`$ strategies, including all
summary-dependent addresses, so their general framework applies exactly to
the direct pair-parity task. The sphere bound and random-code formula supply
the success-probability conversion; they do not evaluate the largest strategy
ball. Theorem 12's stationary-memoryless, separable-distortion hypotheses do
not automatically hold for this growing alphabet.

**An explicit indirect-source embedding.** Permuter and Weissman,
*Source Coding with a Side Information “Vending Machine”*,
[arXiv:0904.2311v2](https://arxiv.org/pdf/0904.2311), 30 April 2009,
Section II-F, Theorem 4, Eqs. (49)–(51), printed pp.15–16. For each fixed
archive width, let the hidden source be $`(X,Q)`$ and the encoder observe only
$`X`$. An action is a whole query-to-address map; the channel returns the late
uniform pair $`Q`$ and the selected raw bit. Reconstruction is the pair-parity
answer and every action costs one. This preserves hidden query timing and
the one-raw-bit channel while allowing message-dependent actions.

**Our deductions.** Write $`G_n(D)=\min I(X;T)`$ over stochastic strategy labels
with expected table distortion at most $`D`$, and $`F_n(D)`$ for the repeated-archive
rate characterized by their Theorem 4. Absorb the action into the auxiliary
$`U`$. Their objective is $`I(X;U)-I(U;Y\mid A)`$, and the subtracted quantity lies
in $`[0,1]`$: the query is independent and the remaining observation is one bit.
Collapsing $`U`$ to its induced strategy therefore gives

```math
G_n(D)-1\le F_n(D)\le G_n(D).
```

The existing pair-specific moment bound applies to arbitrary posteriors and
proves $`G_n(D)/n\to\mathcal R(D)`$, hence the same for $`F_n(D)/n`$. The source
does not evaluate this strategy optimization. Its coding limit repeats fixed
archives and controls expected distortion; it does not itself establish our
single-archive success exponent or deterministic worst-input table guarantee.
Exact old parity can be added for one bit per archive, including failed inputs.
Under an excess-distortion/partial-cover criterion, an infinite parity penalty
only enforces parity on successful inputs and is insufficient for that
requirement. Finite expected distortion with an infinite penalty instead
forces zero parity-error probability.

The [operational note](OPERATIONAL_REDUCTION.md) proves these reductions and
the finite XOR-translation bounds. This supersedes a comparison that merely
lists differences from the direct-source Theorem 1. The general coding
conversions are established machinery; the remaining evaluation is
$`m_n(\varepsilon)=2^{-n\mathcal R(\varepsilon)+o(n)}`$, with an ordered-endpoint
strategy attaining the exponent. No independent novelty is assigned to the
covering or success-exponent conversion.

## 11. Bounded comparison of the decoder-ball theorem

**Exact one-star rank bounds leave a weight-distribution problem.** With residual
matrix $`A_t`$, affine offset $`\alpha_t`$, and rank $`r`$, the exact identity is

```math
\Pr[D_n(X,t)\le\varepsilon]
=2^{-r}|(\alpha_t+\mathrm{im}A_t)
\cap B_N(0,\lfloor\varepsilon N\rfloor)|.
```

Jukna–Schnitger's exact fiber count in Section 7 therefore does not by itself
evaluate approximate volume. Two legal strategies demonstrate a leading-order
loss: always answer zero, or answer $`x_i`$ for $`i<j`$. Both have rank $`n-1`$ and
exactly two zero-error inputs. The first has error count $`w(n-w)`$ for
$`w=|x|`$, hence ball exponent
$`1-h_2((1-\sqrt{1-2\varepsilon})/2)`$; the second has exponent
$`\mathcal R(\varepsilon)`$. These are different functions. A union bound over
all allowed error vectors also loses the scale: its logarithmic Hamming-ball
factor is $`\Theta(n^2)`$, while $`r\le n`$. These examples are our deductions,
not results attributed to that source.

**Disjoint products give a genuine weaker ball bound.** The Nisan–Rudich–Saks
matching comparison in Section 5 extends directly to

```math
m_n(\varepsilon)\le
2^{-\lfloor n/2\rfloor[1-h_2(\varepsilon)]}.
```

Choose a uniform maximum matching and apply Jensen to the exponential of its
correct-answer count. Matching residuals are independent even for arbitrary
third-coordinate reads, so the moment is the fair-binomial moment. Optimizing
Chernoff gives the displayed inequality. At error $`0.1`$, its limiting
coefficient is approximately $`0.265502`$, below the sharp $`0.422085`$.
The audit supplies the full derivation; these numbers illustrate an analytic
gap, not a numerical novelty test.

**Threshold direct-product successors preserve independent instances and a
shared query budget.** Drucker, *Improved Direct Product Theorems for Randomized
Query Complexity*, [arXiv:1005.0644v2](https://arxiv.org/pdf/1005.0644),
9 May 2014, Theorem 6.6, printed p.20, bounds threshold success on independent
instances using a global query budget. Ben-David and Blais, *Direct Product
Theorems for Randomized Query Complexity*,
[arXiv:2512.08268v1](https://arxiv.org/pdf/2512.08268), 9 December 2025,
Theorem 2, printed p.5, and Corollary 3, p.6, give list-decoding and threshold
query-complexity bounds. They concern copies of one function on separate input
blocks, not all overlapping pairs of one archive. Replacing our separate
one-read outputs by one algorithm with $`N`$ total reads removes the restriction:
it reads all $`n\le N`$ bits and answers every pair exactly. Conversely, taking
independent pair blocks preserves only a matching-sized part of the objective.
These direct substitutions do not yield the sharp theorem; this is not a
claim that every possible reduction from those works fails.

**A polynomial concentration theorem loses the required scale on a legal
strategy.** Schudy and Sviridenko, *Bernstein-like Concentration and Moment
Inequalities for Polynomials of Independent Random Variables: Multilinear
Case*, [arXiv:1109.5193v2](https://arxiv.org/pdf/1109.5193), 8 June 2012,
Theorem 1.3, Eq. (1.7), printed p.4, bounds a polynomial's tail using its
variance and smoothness parameters $`\mu_r`$ (defined on p.3).
Let $`Y_i=(-1)^{X_i}`$. Read $`j`$ for pair $`\{1,j\}`$, and read coordinate 1
for pairs $`\{i,j\}`$ with $`i,j>1`$, always returning the raw bit. The signed
correctness sum is

```math
S=(n-1)Y_1+Y_1\sum_{2\le i<j\le n}Y_iY_j.
```

It has $`\mathrm{Var}S=(n-1)^2+\binom{n-1}{2}`$ and
$`(\mu_1,\mu_2,\mu_3)=(N,n-2,1)`$. At threshold $`\eta N`$, the theorem's
$`r=1`$ term is $`\exp(-\eta/C^3)`$ for its universal constant $`C`$, independent
of $`n`$. Thus this direct substitution gives no positive exponent on the $`n`$
scale. More structured concentration arguments are not ruled out.

There is a stronger obstruction to forgetting pair labels altogether. A system
of exactly $`N`$ distinct weight-at-most-three rows can have full rank $`n`$ and
still have a good fraction at least $`2^{-O(n^{2/3})}`$ at every fixed positive
error. Put all triples on a core of $`\Theta(n^{2/3})`$ variables, add singleton
rows outside it, and fill the remaining slots with core pairs. All-positive
core inputs suffice. Such a system cannot be assigned distinct query-pair
labels: there are more core triples than available core pairs. The audit gives
the exact construction and proof. Generic degree, equation count, and full rank
therefore cannot replace the pair-incidence hypothesis.

**Bounded conclusion.** None of these inspected theorems yields the sharp
exponent by the explicit substitutions above. This is a finite set of
resource-preserving comparisons, not an originality certificate. The direct
coordinate-prediction obstruction from Section 7 remains, and the generic
coding reductions from Section 10 remain established. The next useful object
is the completed self-contained theorem packet, not another open-ended search
for novelty in its elementary ingredients.

## 12. Claim boundary and development decision

**Written result:** arbitrary preprocessing, arbitrary memory-dependent one-bit addresses, exact original parity, and a fixed positive error allowance admit the matching rate derived in the [current note](../RESEARCH_NOTE.md). The construction uses only endpoint probes. The [excess-distortion deduction](EXCESS_DISTORTION.md) strengthens the operational statement to deterministic worst-input table distortion and the optimal exponential rate of the probability of a low-distortion table below the memory threshold.

**Established machinery:** the systematic model, one-star Boolean affinity and fiber counting, elementary affine-basis sumsets and fundamental circuits, the entropic Chang inequality, convex conjugacy, weighted binary rate-distortion coding, Hamming covers, Chernoff and union bounds, RAC block construction, and symmetrization.

**Proposed original contribution after bounded assessment:** evaluation of the largest low-error input set handled by one arbitrary raw-read strategy, matching an ordered-endpoint weighted Hamming ball in exponential size. General coding converts that evaluation into the operational rate and success exponent. The elementary geometric lemma supports the evaluation and has adequate classical attribution. The exact affine comparison is a consequence. The general rank-envelope lemma, low-rank refinement, bipartite benchmark, finite translation bounds, and excess-distortion deductions are not independently certified new results.

**Not established:** historical novelty, uniqueness of optimal implementations, efficient explicit near-optimal codes, finite-length optimality, uniform vanishing-error or vanishing-advantage asymptotics, a computational speedup, or a theorem about AI alignment. The completed assessment is affirmative at this narrow scope, not an exhaustive priority certificate.

**Decision:** retain this extremal theorem as the proposed original contribution
of a focused theoretical paper. The [completed assessment](CONTRIBUTION_ASSESSMENT.md)
explains the positive significance case and its strongest limitations. The
comparison identifies concrete losses in inspected reductions; unsuccessful
searches are not novelty evidence. The mathematical content is the sharp
absence of a leading-rate advantage from arbitrary raw-coordinate access over
a fixed endpoint rule for a canonical overlapping query family. Established
methods, specialized scope, and nonconstructive codebooks limit the claims but
do not defeat this focused contribution. Reopen for concrete new evidence;
independent specialist feedback is welcome. **Manuscript preparation is on
hold.** No external contact or manuscript release is included.

## 13. Header-based local compression: a closer architectural precedent

**Source statement.** Pananjady and Courtade, *The Effect of Local Decodability
Constraints on Variable-Length Compression*, IEEE Transactions on Information
Theory 64(4), 2593–2608 (2018),
[published author PDF](https://people.eecs.berkeley.edu/~courtade/pdfs/PananjadyCourtade_LocalDecodableTIT2018.pdf),
Definition 1/Theorem 1, p.2595; Definition 6/Theorem 6, p.2599; Section VI-A,
p.2606. Their source is uniform over all weight-$`r`$ binary strings of length
$`m`$. Theorem 1 lower-bounds expected codeword length under exact coordinate
recovery using $`d`$ adaptive encoded-bit probes, with length known to the
decoder. Theorem 6 permits a freely read $`h`$-bit header followed by $`d`$ probes
of a designed fixed-length payload and proves an achievability result.
Section VI-A extends the converse to block error by retaining entirely
correctly decoded source words.

**Our resource comparison.** The freely accessible header is an explicit
precedent for metadata-dependent probing. That architecture is not a novelty
claim. Their header theorem does not lower-bound header length when the
payload must be the unchanged archive. Indeed, coordinate queries on that
payload need no header and one raw read. Our queries are pair parities. In a
literal locally decodable representation $`(M,X)`$, storage is $`n+B`$ bits and
reading the entire summary followed by one archive bit can use $`B+1`$ probes.
Putting $`d=1`$ in Theorem 1 while granting free summary access would change its
resource model.

**Our source-lift check.** Set $`Y_{ij}=X_i\oplus X_j`$ and $`N=\binom n2`$.
The $`2^{n-1}`$ possible vectors $`Y`$ are cut patterns, not a uniform $`N`$-bit
cube. Conditional on $`|X|=w`$, their weight is $`r=w(n-w)`$ but their support
has size $`\binom nw`$, divided by two when $`2w=n`$. It is not the full shell
of size $`\binom Nr`$. Replacing one by the other can change the entropy scale
from $`n`$ to $`n^2`$. For $`n=4,w=1`$ the two counts are 4 and 20; for $`w=2`$
they are 3 and 15. The archive still is $`X`$, so querying a coordinate of
an encoded $`Y`$ is a further change unless its implementation is charged.

**Our error check.** Theorem 1's proof, Section IV, Eqs. (7)–(8), unions
transcripts for the source's one-coordinates and obtains an antichain:
containment would force a decoding error. A positive-distortion table already
permits errors, so that contradiction does not transfer. Section VI-A's block
error extension retains words with zero coordinate errors; our good inputs
may each have $`\varepsilon N`$ wrong pairs. Counting all ambient error
patterns gives the loose factor
$`\sum_{j\le\varepsilon N}\binom Nj=2^{\Theta(n^2)}`$ at fixed interior
error. A fixed strategy actually realizes at most $`2^n`$ patterns, but an
uncontrolled partition can still consume the whole $`n`$-scale entropy budget.
Thus a sharp error-pattern argument would require additional structure; it
is not supplied by the exact antichain or block-error statements. These
explicit substitutions do not yield our bound; more elaborate reductions
are not ruled out.

## 14. Entropy proofs of ball bounds are established

**Source statement.** Rioul and Solé, *An Information Theoretic Proof of the
Chernoff–Hoeffding Inequality* (2025),
[author PDF](https://perso.telecom-paristech.fr/rioul/publis/202502rioulsole.pdf),
DOI [10.1016/j.ipl.2025.106582](https://doi.org/10.1016/j.ipl.2025.106582),
Sections 4–5, Theorem 6 and Corollary 10. The source uses entropy methods for
concentration and ordinary Hamming-ball volume. Taking a uniform distribution
on a constrained set and bounding its entropy by marginal entropies is
established methodology, not a new feature of our proof.

**Our substitution.** A strategy's residual image is an affine binary code
$`C\subseteq\{0,1\}^N`$ of dimension $`d\le n`$. Applying the ordinary ball bound
only yields

```math
\Pr[D_n(X,t)\le\varepsilon]
=2^{-d}|C\cap B_N(0,\lfloor\varepsilon N\rfloor)|
\le 2^{N h_2(\varepsilon)-d}.
```

For fixed positive error and $`N=\Theta(n^2)`$ this upper bound is vacuous.
Selecting $`d`$ independent residuals alone does not bound their error fraction
by that of all $`N`$ dependent residuals. The pair-incidence envelope over all
subsets and the full greedy bias profile supply the missing task-specific
constraint. This is an explicit limitation of the direct substitution, not
an assertion that ordinary entropy cannot prove our theorem: entropy is
precisely an ingredient of our proof.

**Source-proof caveat.** In the inspected PDF, Eq. (34) of the proof of
Corollary 10 is false as printed: $`q=2,n=2,d=1`$ would give
$`3\le2^{4/3}`$, whereas $`3^3=27>16=2^4`$. This does not invalidate the final
ball bound in Eq. (33). It follows directly from entropy subadditivity: for
uniform $`X`$ in the $`q`$-ary ball and $`d'=\mathbb E|X|`$, each coordinate has
nonzero probability $`d'/n`$, hence $`H_q(X)\le n h_q(d'/n)`$, followed by the
usual monotonicity step in the stated radius range. Our central proof uses
valid unconditional entropy subadditivity and does not rely on the printed
intermediate inequality. The source caveat supplies no novelty evidence.

## 15. Recent bounded-error operator and RAC comparisons

**Bounded error is already present in the operator literature.** Young Kun Ko,
*Lower Bounds for Linear Operators*, ECCC TR25-155 (22 October 2025),
[primary PDF](https://eccc.weizmann.ac.il/report/2025/155/download/),
Lemma 4.4, printed p.21, treats random linear operators with $`m=10^9n`$
rows and space $`s=1.01n`$. Its displayed per-output success requirement is at
least $`2/3`$ and the probe lower bound is $`\Omega(\log n)`$. Thus it would be
incorrect to dismiss the whole comparison as exact-only. We do not strengthen
the lemma's probability quantifier to a worst-input guarantee.

**Our substitution check.** The complete pair matrix is explicit and has
weight-two rows; it is not the random dense operator in that lemma. Two raw
reads answer each pair exactly, independently of $`n`$, so a logarithmic probe
lower bound cannot specialize to this matrix. Also, probes to all stored
one-bit cells are charged in that model; there is no arbitrary summary whose
entire contents are free to read. Paying for our summary or treating it as
free changes the compared parameter. The source does not evaluate the
one-raw-read/summary-rate tradeoff for this explicit matrix.

**A dynamic successor screened separately.** Ko,
*An $`\Omega((\log n/\log\log n)^2)`$ Cell-Probe Lower Bound for Dynamic Boolean
Data Structures*, ECCC TR26-047 (26 March 2026),
[current 33-page PDF](https://eccc.weizmann.ac.il/report/2026/047/download/),
Theorem 1.1, printed p.2, concerns the multiphase inner-product problem with
$`m=n^{1+\Omega(1)}`$ and bounds $`\max\{t_u,t_{tot}\}`$. Words have
$`\Theta(\log n)`$ bits and updates are charged. It is not a static
positive-distortion pair theorem. Applying its more general lifting route
would require verifying the communication-hardness hypothesis for the
restricted weight-two query distribution; the paper's general inner-product
statement does not do that. This is a screened neighbor, not an attribution
of our result or a claim about every possible dynamic reduction.

**Recent geometric RAC optimization.** Kondo, Sato, Yano, Maeda, Ito, and
Yamamoto, *Random Access Codes: Explicit Constructions, Optimality, and
Classical–Quantum Gaps*,
[arXiv:2604.21274v3](https://arxiv.org/pdf/2604.21274v3), 16 July 2026,
Definitions 2–3, Theorem 5/Eq. (23), p.6, and Theorem 14/Eq. (121), p.12.
The former reduces average classical RAC success to nearest representatives
on the uniform input cube; the latter gives a convex-hull distance
optimization for worst-case coordinate success. The model decodes from the
message without a raw-archive probe and does not grant shared randomness.

**Our substitution check.** Setting their input length to $`N=\binom n2`$
would replace the dependent cut-pattern source of Section 13 with a uniform
cube and omit our legal raw read. Granting that read also changes the class
of reproduction objects from message-only coordinate reconstructions to
query-dependent strategies. Neither inspected geometric optimization
evaluates the volume of those strategy balls. General strategy-as-reproduction
coding is already credited in Section 10. The comparison supports the narrow
claim boundary, not a global non-subsumption assertion.
