# Sharp asymptotic memory for delayed pair-parity revision

Research checkpoint, 22 September 2026.

**Status:** a matching converse and construction have been derived for the model below. The unrestricted first-order rate, previously bounded within a constant factor, is now determined by the written argument. Historical novelty, independent mathematical review, and publication significance remain unresolved. Small checks are not a proof certificate. No efficient implementation of the asymptotic covering codes is claimed.

The previous consolidated note is preserved byte-for-byte as [BASELINE_NOTE.md](BASELINE_NOTE.md). Its exact theorem, affine theorem, and finite examples remain valid. Its statements that the unrestricted rate and existence of a limiting rate are open are superseded by this note. The separate conjunction exploration has not been changed.

The [theorem and contribution brief](docs/THEOREM_BRIEF.md) isolates the operational result: unrestricted summary-dependent addresses and publicly chosen endpoint reads have the same first-order optimum. It also proves an exact finite separation between them and distinguishes this result from its established coding ingredients.

## 1. Unchanged model and error quantifiers

The input is $X\in\{0,1\}^n$, $n\geq3$. Before learning a query, an encoder retains at most $B$ input-dependent bits $M=f_R(X)$. Public randomness $R$ is independent of $X$. The original total parity

$$p(X)=\bigoplus_{i=1}^nX_i$$

must be recoverable exactly from $(M,R)$ without a raw read. A later unordered pair $\{i,j\}$ requests

$$p_{ij}(X)=p(X)\oplus X_i\oplus X_j.$$

The decoder sees the whole summary, seed, and query, and may reread at most one raw coordinate $X_k$. The address can depend on all those available quantities. Local computation and preprocessing time are unrestricted. The immutable external archive still contains $X$ and is not charged to $B$; a read returns one bit, not a word or arbitrary function. Prior transcripts and input-dependent caches are not free. This is an established systematic-data-structure access model, not a proposed new framework.

Write $B_{\rm all}(n,\varepsilon)$ for the least summary size with exact original parity and, for each fixed pair, revised error at most $\varepsilon$ averaged over uniform $X$ and randomness. The converse below needs only average error over uniform pairs as well. The construction attains the stronger guarantee for **every fixed input and fixed pair**, with probability over the public seed. It does not give simultaneous correctness of all pairs, or protect against selecting a pair after observing the seed and summary.

**Finite symmetrization observation.** These three optimal memory sizes are equal even at finite $n$. Given a scheme for input-and-pair average error, publicly choose an independent uniform permutation $\Pi$ and mask $Z$ and encode $Y_a=X_{\Pi(a)}\oplus Z_a$ with the old scheme. Map query $\{i,j\}$ to $\{a,b\}=\{\Pi^{-1}(i),\Pi^{-1}(j)\}$. Simulate a read of $Y_k$ with one read of $X_{\Pi(k)}$ and the known mask bit. Correct the revised output by $p(Z)\oplus Z_a\oplus Z_b$ and the original-parity output by $p(Z)$. For each fixed $X,i,j$, the transformed input is uniform independently of the uniform mapped pair. Error is therefore the old average, with the same worst-case memory size and read budget. The reverse inclusions are immediate. This standard symmetrization deduction also preserves affine encoders for each seed.

Random coins can be fixed when conditioning; revealing private coins for a converse only strengthens the decoder. Fixed-length worst-case summary size, not expected message length, is charged. All entropy is measured in bits; $\ln$ denotes the natural logarithm. Set

$$N=\binom n2,\quad \eta=1-2\varepsilon,\quad
c(b)=1-h_2((1-b)/2),\quad
\Phi_n(r)=nr-r(r-1)/2.$$

## 2. Main theorem

**Theorem S (sharp first-order rate).** Fix $0<\varepsilon<1/2$. Let $a>0$ be the unique solution of

$$\eta=2\int_0^1u\tanh(au)\,du.$$

Then the full limit exists and

$$\boxed{\lim_{n\to\infty}\frac{B_{\rm all}(n,\varepsilon)}n
=\mathcal R(\varepsilon)
=\int_0^1c(\tanh(au))\,du
=\frac{a\eta-\ln\cosh a}{\ln2}.}$$

Equivalently,

$$\mathcal R(\varepsilon)=\frac1{\ln2}\sup_{a\geq0}
\left\{\frac{a\eta}{2}-\int_0^1\ln\cosh(au)\,du\right\}.$$

A finite converse, valid for every $s>0$, is

$$\boxed{B\ln2\ \geq\ sN\eta-\sum_{k=1}^n\ln\cosh(sk).}$$

This finite inequality is not asserted to be the finite-length optimum. The older finite converses and the exact theorem remain available independently. At $\varepsilon=0$, the baseline exact formula gives limiting rate one; at $\varepsilon=1/2$, one parity bit and a random guess give limiting rate zero. The displayed parameterization concerns the open interval.

**Operational corollary.** The same limit holds if the decoder may read only a query endpoint, even if its address must depend only on the query and public seed. The achieving construction already has this restriction; the unrestricted converse applies to all three classes. At zero error the endpoint-only optimum is instead exactly $n-1$, versus $n-\lfloor\log_2(n+1)\rfloor$ with arbitrary addresses. Thus equality of first-order rates does not assert a finite transformation between arbitrary implementations. The [brief](docs/THEOREM_BRIEF.md) gives the endpoint proof and its stronger finite converse.

The [rank-profile extensions](docs/RANK_PROFILE_EXTENSIONS.md) give a capped finite converse, an exact low-rank coverage formula, and the corresponding sharp result for bipartite query graphs. They do not alter this first-order theorem.

## 3. Converse: preserve the entire independence profile

### 3.1 Pair coverage at a specified rank

For a subset $E$ of distinct pairs, select one residual row for each pair:

$$a_{ij}=e_i+e_j+\beta_{ij}e_{k_{ij}},\qquad\beta_{ij}\in\{0,1\}.$$

All rows are nonzero, including when $k_{ij}$ is an endpoint. If these rows span a space $W$ of binary dimension $r$, then

$$|E|\leq\Phi_n(r).$$

For completeness: in $\mathbb F_2^n/W$, choose $n-r$ coordinate images forming a basis, indexed by $I$. At most $N-\binom{n-r}{2}$ pairs have an endpoint outside $I$. For a selected pair wholly inside $I$, its two independent images must sum to a coordinate image outside $I$. Distinct pairs of basis vectors have distinct sums. Only $r$ coordinates are outside $I$, so at most $r$ such pairs occur. Adding the two counts gives $\Phi_n(r)$. This applies to every subset of the selected pair-labelled rows; it permits repeated residual rows for different pairs. The bound can exceed $N$ and need not be attained at every rank.

The proof also gives $r$ coordinates meeting all selected pairs except at most $r$ exceptions. For endpoint-only residuals there are no exceptions, giving the exact geometric envelope $N-\binom{n-r}{2}$. This explains the leading comparison. For priority, even a prior uniform bound $|E|\le nr-r^2/2+o(n^2)$ would suffice for the sharp asymptotic converse; matching the precise lower-order terms is unnecessary.

### 3.2 Conditional biases and their greedy basis

Fix a seed and a nonempty memory cell. The total parity is known. A deterministic Boolean function of one observed bit is constant, that bit, or its complement. Consequently a cellwise optimal decoder for a pair predicts a residual parity $a_{ij}\cdot X$ by its more likely value. Its conditional bias is

$$b_{ij}=|\mathbb E[(-1)^{a_{ij}\cdot X}\mid M=m,R]|.$$

Optimizing separately on cells cannot increase average error; it does not assume each cell meets the global error target. A randomized decoder cannot beat this optimum on the cell.

Sort these pair-labelled rows by nonincreasing bias and greedily keep a row whenever it increases rank. Let the retained biases be $t_1\geq\cdots\geq t_d$, padded with zeros to length $n$. At every positive threshold $z$, the selected basis rows above threshold span all rows above threshold. Write $q(z)$ and $r(z)$ for their count and rank. The coverage lemma and its increments give

$$\begin{aligned}
\sum_{i<j}b_{ij}
&=\int_0^1q(z)\,dz\leq\int_0^1\Phi_n(r(z))\,dz\\
&=\sum_{\ell=1}^n(n-\ell+1)t_\ell.
\end{aligned}$$

Ties do not affect the threshold-span property. Endpoints of threshold intervals have measure zero.

This is the refinement missing from the earlier argument: retain the full list of independent prediction strengths instead of replacing it by a single rank or total entropy deficit.

### 3.3 Entropy budget and scalar conjugacy

Let $D=n-H(X\mid m,R)$. Extend the independent residual rows to a basis of $\mathbb F_2^n$. The resulting invertible linear change of variables preserves entropy. Each selected coordinate has entropy $h_2((1-t_\ell)/2)$ and each remaining coordinate at most one. Subadditivity yields

$$\sum_{\ell=1}^n c(t_\ell)\leq D.$$

This entropy ingredient is established: for a uniform memory cell it is precisely the pre-quadratic entropy inequality in Impagliazzo, Moore, and Russell, *An Entropic Proof of Chang's Inequality*, Eq. (1), together with their Section 2 basis transfer. The argument above also works for arbitrary conditional distributions. See the version-specific [literature comparison](docs/LITERATURE_COMPARISON.md). The pair-subset coverage bound supplies the separate geometric input.

The elementary convex identity

$$zb-\ln2\,c(b)\leq\ln\cosh z\qquad(0\leq b\leq1,\ z\geq0)$$

has equality at $b=\tanh z$: differentiating the left side in $b$ gives $z-\operatorname{atanh}b$. Apply it with $z=s(n-\ell+1)$, and sum:

$$s\sum_{i<j}b_{ij}
\leq D\ln2+\sum_{k=1}^n\ln\cosh(sk).$$

For uniform $X$ independent of the seed,

$$\mathbb ED=I(X;M\mid R)\leq B.$$

Average over cells and seeds. Average revised error at most $\varepsilon$ implies average total optimal bias at least $N\eta$. This proves the finite converse. No affine-encoding assumption, uniform accuracy within cells, fixed probe address, or endpoint-only restriction was used.

### 3.4 Limit and maximizer

Put $s=a/n$ and divide by $n$. Riemann sums show

$$\liminf\frac Bn\geq\frac1{\ln2}
\left[\frac{a\eta}{2}-\int_0^1\ln\cosh(au)\,du\right]$$

for each fixed $a\geq0$. The derivative in $a$ is $\eta/2-\int_0^1u\tanh(au)du$, strictly decreasing from $\eta/2$ to $(\eta-1)/2$. This proves existence and uniqueness of the finite maximizing parameter for $0<\eta<1$.

At that parameter, pointwise conjugate equality and integration by parts give

$$\int_0^1c(\tanh(au))du
=\frac{a\eta/2-\int_0^1\ln\cosh(au)du}{\ln2}
=\frac{a\eta-\ln\cosh a}{\ln2}.$$

## 4. Matching construction: grade stored accuracy and reread the weaker endpoint

### 4.1 An ordinary covering ingredient, credited to prior coding theory

For a block of $m$ bits and Hamming radius $r$, put $V=\sum_{j=0}^r\binom mj$. There exists a cover of the whole cube with at most

$$K_{m,r}=\min\left\{2^m,\left\lceil\frac{(m+1)2^m}{V}\right\rceil\right\}$$

centers. If the second expression is used, independently sampled centers leave expected uncovered points at most $2^m\exp(-K_{m,r}V/2^m)<1$; otherwise use the entire cube. Storing a covering-center index costs $\lceil\log_2K_{m,r}\rceil$ bits and ensures at most $r$ reconstruction errors for every block input. For fixed $0<\delta<1/2$, $r=\lfloor\delta m\rfloor$ gives rate $1-h_2(\delta)+O(\log m/m)$.

Covering existence, entropy-rate coding, and random-access-code symmetrization are established ingredients; see the [literature comparison](docs/LITERATURE_COMPARISON.md). No new cover family or efficient covering algorithm is claimed.

### 4.2 Finitely many quality levels

Partition the permuted input into $L$ blocks. Block $\ell$ has size $m_\ell$, increasing reconstruction bias $b_\ell$, and error allowance $\delta_\ell=(1-b_\ell)/2$. Store a covering index for each block and one exact total parity bit. For a query, reconstruct the endpoint in the more accurate block and reread the other original coordinate exactly. In a same-block tie use the smaller original query label, independently of the data. Then XOR with the retained parity. The decoder uses exactly one raw read and does not need to inspect a third coordinate.

For blocks of comparable size, each with its own fixed quality, the storage rate approaches the average $c(b_\ell)$. With cumulative sizes $s_\ell=\sum_{j\leq\ell}m_j$, the probability that the better-quality endpoint is in block $\ell$ is exactly

$$w_\ell=\frac{\binom{s_\ell}{2}-\binom{s_{\ell-1}}2}{\binom n2}.$$

The resulting error is at most $\sum_\ell w_\ell\delta_\ell$.

### 4.3 Why this covers every fixed input and pair

Let $\Pi$ be a public uniform coordinate permutation and $R$ an independent uniform mask. At permuted position $a$, encode $Y_a=X_{\Pi(a)}\oplus R_a$. For every fixed original $X$, the vector $Y$ is uniform and independent of $\Pi$. Conditioned on the chosen quality block, the endpoint used for reconstruction is uniform within that block and independent of $Y$. A block's average reconstruction error is at most its covering radius divided by its length. Thus the error bound above holds for every fixed input and fixed pair, averaged over the seed. Unmask the estimated endpoint using its known mask bit. Store the original $p(X)$, not merely parity of the reconstructed vector.

This proof does not require independent reconstruction errors, independence of two queried bits after compression, or per-coordinate accuracy for every covering center. It uses the public permutation and mask explicitly. Input-dependent information in all indices and the parity bit is charged. Quality levels are public, data-independent choices.

### 4.4 Passage to the optimum, including an error margin

For a fixed number $L$ of asymptotically equal-size blocks, let $u_\ell=(\ell-1/2)/L$ and $b_\ell=\tanh(a'u_\ell)$. As $n\to\infty$,

$$\frac Bn\leq\frac1L\sum_\ell c(b_\ell)+o(1),\qquad
\text{bias}\geq\sum_\ell\frac{2\ell-1}{L^2}b_\ell+o(1).$$

For target $\eta$, first choose $a'>a$ so the continuous bias is strictly larger than $\eta$. Then choose a sufficiently fine but fixed $L$ and take $n\to\infty$. The positive margin absorbs block rounding and finite-size pair weights; covering overhead $O(L\log n)$ is $o(n)$ in this order of limits. Finally let $a'\downarrow a$ and refine $L$. Continuity gives $\limsup B/n\leq\mathcal R(\varepsilon)$.

This works for all sufficiently large $n$ by using block sizes differing by at most one, not only a divisibility subsequence. One must not set $L=n$ while discarding the covering overhead. The construction completes the matching theorem and establishes the existence of the limiting rate.

### 4.5 Identification with an established weighted coding problem

The scalar profile is a specialization of weighted binary rate-distortion coding, not a new coding law. Let a fair binary source have an independent uniform quality label $u\in[0,1]$, public to both encoder and decoder, and distortion $2u\,\mathbf1\{x\ne\widehat x\}$. Its variational rate at distortion $\varepsilon$, optimizing measurable $0\le\delta(u)\le1/2$, is

$$\inf_{\delta}\left\{\int_0^1[1-h_2(\delta(u))]du:
\int_0^1 2u\delta(u)du\le\varepsilon\right\}.$$

Martinian, Wornell, and Zamir, *Source Coding With Distortion Side Information*, Section IV-E, Eqs. (40)-(41), give the finite-label weighted binary formula. Set their distortion offset to zero and their weight to $2u$; the continuum expression follows by finite partitions. Their logistic allocation gives $\delta(u)=(1+e^{2au})^{-1}$, hence $b(u)=\tanh(au)$. The substitutions $b=1-2\delta$ and $\eta=1-2\varepsilon$ identify its objective and constraint exactly with ours. Source/version details are in the [comparison](docs/LITERATURE_COMPARISON.md).

What the pair-query theorem adds, subject to unresolved priority, is equality of its optimal first-order rate with this established coding rate: the weights emerge from pair geometry, and the converse allows arbitrary summary-dependent raw addresses. This is an equality of limiting optima, not a finite-length simulation between all implementations of the two models.

## 5. Consequences and finite certificate

The baseline affine rate is $\mathcal R_{\rm aff}(\varepsilon)=1-\sqrt{2\varepsilon}$. For every fixed $0<\varepsilon<1/2$,

$$\mathcal R(\varepsilon)<\min\{1-h_2(\varepsilon),\mathcal R_{\rm aff}(\varepsilon)\}.$$

To see strictness, the variational problem is to minimize $\int_0^1c(b(u))du$ subject to $2\int_0^1ub(u)du\geq\eta$. Strict convexity and conjugate equality give the unique minimizer $b(u)=\tanh(au)$ almost everywhere. Uniform-quality storage has constant bias $\eta$. An affine random-subset scheme has bias zero below $u=\sqrt{2\varepsilon}$ and one above it. Both satisfy the same constraint but differ from the unique minimizer on a positive-measure set. This comparison is about affine encoding maps over $\mathbb F_2$, not linearity of reconstruction codebooks or real-valued layers.

For success $1/2+\gamma$, first take the large-$n$ limit at fixed $\gamma>0$, then $\gamma\downarrow0$. Expanding the parameter equation and entropy gives

$$\mathcal R(1/2-\gamma)=\frac{3}{2\ln2}\gamma^2+O(\gamma^4),$$

whereas the affine rate is $\gamma+O(\gamma^2)$. This is not a uniform statement for arbitrarily small $\gamma$ depending on $n$.

Illustrative numerical evaluations, not proof inputs:

| Revised error | Sharp unrestricted rate | Best previous upper bound | Affine rate |
| --- | ---: | ---: | ---: |
| 1% | 0.814967475 | 0.858578644 | 0.858578644 |
| 10% | 0.422084894 | 0.531004406 | 0.552786405 |
| 25% | 0.143921819 | 0.188721876 | 0.292893219 |

A finite covering-existence certificate uses $n=1024$, eight blocks of length 128, with radii (weakest to strongest)

$$56,42,29,20,13,8,5,3.$$

The covering bound gives block index lengths $11,21,40,59,78,95,107,117$. Including exact parity, **529 bits suffice**, with error at most $6245/65472<1/10$. At the same 10% target, the baseline affine converse requires **at least 565 bits**. These are exact integer/rational implications of a covering-existence proof; the large covers were not constructed, and 529 is not asserted to be finite-length optimal.

## 6. Evidence, attribution, and remaining work

[verify_sharp_rate.py](checks/verify_sharp_rate.py) and its [recorded report](results/sharp_rate.json) check all 131,610 nonempty fixed-parity memory cells through five input bits, using integer correlations and ranks for the profile tests. They also check the entropy and dual inequalities numerically, execute a four-bit graded decoder on all 36,864 input-query-mask-permutation cases, verify the finite covering certificate with exact arithmetic, and compare numerical quadratures for the limiting curve. The [reproduction guide](docs/REPRODUCIBILITY.md) states counts and tolerances. Original parity and conjunction checks remain unchanged.

The access model, ordinary Hamming covers, classical random access coding, the entropic Chang ingredient, weighted binary coding profile, and convex optimization are established. The [proof and novelty audit](docs/reviews/SHARP_RATE_AUDIT.md) found no central proof defect. It narrowed the candidate contribution to the pair-specific all-subsets rank envelope and its matching application to arbitrary summary-dependent one-bit probes, including the resulting exact affine comparison. Neither the scalar curve nor the generic advantage of nonlinear lossy encoders supplies a novelty claim. The [literature comparison](docs/LITERATURE_COMPARISON.md) records explicit reductions and their limits; historical priority remains unresolved.

Remaining mathematical questions include finite-length optimality, efficient explicit constructions approaching the curve, stronger adversarial query quantifiers, and variable-error finite-size regimes. These are distinct from the first-order rate settled by the written argument. No theorem about consciousness, natural-language interpretation, or present-day AI systems is claimed.

The requirement to preserve original parity is also not an extensive extra resource in this example. If $B_{\rm pair}$ denotes the same model asking directly for $X_i\oplus X_j$ without mandatory parity, then $B_{\rm pair}\le B_{\rm all}\le B_{\rm pair}+1$: use the retained parity to convert a revision answer in one direction, or store one extra parity bit in the other. Both transformations preserve the error and read budgets. The leading theorem concerns late pair queries under a raw-coordinate access constraint.
