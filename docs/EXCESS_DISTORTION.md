# A sharp success exponent and worst-input covering theorem

Research deduction, 22 September 2026. Reviewed main:
`0e91f088cd06376458f63a20f76e2d5b507a690a`.
The [research note](../RESEARCH_NOTE.md) defines the original model and rate
$`\mathcal R(\varepsilon)`$. This note develops an excess-distortion formulation,
using the existing exponential-moment bound and ordinary covering codes. The Chernoff
bound, union bound over memory labels, entropy duality, and coding ingredients
are established; this is not a separate historical-novelty claim.

The subsequent [operational reduction](OPERATIONAL_REDUCTION.md) gives an exact
general-distortion coding formulation and attributes the generic conversion to
Kostina–Verdú's finite-block theorems. It isolates the largest one-read strategy
ball as the task-specific quantity, and keeps mandatory parity valid even on
unsuccessful inputs. The theorem below is a coding consequence of that ball
exponent, rather than an additional independent novelty candidate.

## 1. A counterfactual answer table and its distortion

Keep the original resource ledger: an $`n`$-bit uniform archive, a fixed
worst-case $`B`$-bit summary retaining total parity exactly, free independent
randomness, free access to the whole summary, and at most one raw-coordinate
bit read per query. Addresses may depend on summary, seed, and query. No
input-dependent transcript or cache is free.

The resource and exact-parity rules are retained, but the table-distortion
criterion below replaces the original per-fixed-query error promise. Unless
explicitly combined in Section 5, schemes are not additionally required to
meet that earlier error promise. In particular, the success-probability
optimization includes schemes that fail on most inputs or queries.

Fix all random tapes, including decoder coins, independently of the input.
For each input $`x`$, consider the answers the resulting deterministic scheme
would give to each of the $`N=\binom n2`$ possible pair queries, each run from
the same summary with a fresh one-read budget. Define

```math
\Delta_r(x)=\frac1N\sum_{i<j}
\mathbf1\{\widehat p_{ij,r}(x)\ne p(x)\oplus x_i\oplus x_j\}.
```

For a decoder using fresh coins per query, one may sample an independent tape
for every query in advance; this preserves every single-query distribution.
The theorem below holds for any such input-independent coupling of the tapes.

This table is a mathematical error statistic, not a procedure that answers
all queries within one total read. It neither asserts that every pair is
correct nor protects a pair selected adversarially after seeing the summary
and seed. In particular, $`\Delta_r(x)\le\varepsilon`$ permits an
$`\varepsilon`$ fraction of incorrect answers in that table.

## 2. Finite tail bound and a strong converse

**Proposition.** Every scheme in the stated model, with arbitrary nonlinear
preprocessing, satisfies, for $`0\le\varepsilon<1/2`$ and every $`s\ge0`$,

```math
\Pr_{X,R}\{\Delta_R(X)\le\varepsilon\}
\le\min\left\{1,
\exp\left[B\ln2-sN(1-2\varepsilon)
+\sum_{k=1}^n\ln\cosh(sk)\right]\right\}.\qquad\text{(1)}
```

The capped envelope in [rank-profile extensions](RANK_PROFILE_EXTENSIONS.md)
can replace the displayed sum by its smaller finite sum. The simpler form
already gives the sharp first-order statement.

**Proof.** Fix a seed and a reachable memory label $`m`$. The retained original
parity is a constant $`p_m`$ on its memory cell. After XORing a query output with
$`p_m`$, a one-bit decoder is an affine Boolean function of the chosen raw bit.
Its correctness sign, on that cell, therefore has the form

```math
\sigma_{ij,m}(-1)^{a_{ij,m}\cdot x},\qquad
a_{ij,m}=e_i+e_j+\beta_{ij,m}e_{k_{ij,m}}\ne0.
```

The sign and raw address depend on $`m`$, the seed, and the query, but not on
any additional input information. Extend this formula to the whole cube and
write $`S_m(x)`$ for its sum over all pairs. On the actual memory cell,
$`S_m(x)=N[1-2\Delta_r(x)]`$.

The all-subsets rank envelope and its
[exponential-moment formulation](RANK_PROFILE_EXTENSIONS.md#equivalent-exponential-moment-formulation)
give, for uniform $`U`$ on the cube,

```math
\mathbb E_U e^{sS_m(U)}\le\prod_{k=1}^n\cosh(sk).
```

No condition on the shape of the memory cell is used. There are at most
$`2^B`$ memory labels, so positivity gives

```math
\begin{aligned}
\mathbb E_U e^{sS_{M(U)}(U)}
&=\sum_m\mathbb E_U\bigl[\mathbf1\{M(U)=m\}e^{sS_m(U)}\bigr]\\
&\le2^B\prod_{k=1}^n\cosh(sk).
\end{aligned}
```

Average the fixed-seed bound over all independent tapes. Markov's inequality
at threshold $`sN(1-2\varepsilon)`$ proves (1). This is the usual Chernoff and
help-label union-bound argument, applied to the existing moment inequality.

There is a precise comparison of the fixed decoder families themselves.
Let $`Z_n(s)`$ be the maximum of $`\mathbb E_Ue^{sS(U)}`$ over all permitted
signed residual families, each extended to the whole cube as above.
For the ordered endpoint family $`a_{ij}=e_j`$ when $`i<j`$, with all signs
positive, $`S(U)=\sum_{j=1}^n(j-1)(-1)^{U_j}`$. Independence gives

```math
\prod_{k=1}^{n-1}\cosh(sk)\le Z_n(s)
\le\prod_{k=1}^{n}\cosh(sk).\qquad\text{(2)}
```

Thus unrestricted and ordered-endpoint moment optima differ by a factor
at most $`\cosh(sn)`$, or at most $`\ln\cosh a`$ in their logarithms at
$`s=a/n`$. This is a finite comparison of a moment objective, not of optimal
memory sizes. Section 4 separately proves sharpness of the resulting
below-rate success exponent.

For fixed $`0<\varepsilon<1/2`$, put $`\eta=1-2\varepsilon`$ and let $`a>0`$
satisfy $`\eta=2\int_0^1u\tanh(au)\,du`$. At $`s=a/n`$, monotonicity of
$`u\mapsto\ln\cosh(au)`$ gives

```math
\sum_{k=1}^n\ln\cosh(ak/n)
\le n\int_0^1\ln\cosh(au)\,du+\ln\cosh a.
```

Consequently (1) implies the explicit asymptotic form

```math
\begin{aligned}
\Pr\{\Delta_R(X)\le\varepsilon\}
&\le\min\{1,\exp[(B-n\mathcal R(\varepsilon))\ln2+C_\varepsilon]\},\\
C_\varepsilon&=\frac{a\eta}{2}+\ln\cosh a.
\end{aligned}\qquad\text{(3)}
```

Thus $`B\le n[\mathcal R(\varepsilon)-\gamma]`$, for a fixed $`\gamma>0`$,
forces the probability of a table with distortion at most $`\varepsilon`$ to
be at most $`e^{C_\varepsilon}2^{-n\gamma}`$. This excludes even a fixed
positive fraction of good inputs below the rate. It is stronger than merely
excluding expected distortion at most $`\varepsilon`$. Section 4 shows that
its leading exponent is optimal; the finite prefactor is not asserted to
be optimal.

## 3. Deterministic covers achieve the rate on every input

**Theorem.** Let $`B_{\rm cov}(n,\varepsilon)`$ be the least summary length
among deterministic schemes satisfying
$`\Delta(x)\le\varepsilon`$ for every input $`x`$. Allow arbitrary addresses
in defining the optimum. For every fixed $`0<\varepsilon<1/2`$,

```math
\lim_{n\to\infty}\frac{B_{\rm cov}(n,\varepsilon)}n
=\mathcal R(\varepsilon).\qquad\text{(4)}
```

The upper bound uses only endpoint addresses fixed by the query, with no
randomness and no dependence on the summary.

**Proof of the lower bound.** A deterministic worst-input cover has
$`\Pr\{\Delta(X)\le\varepsilon\}=1`$. Equation (3) gives
$`B\ge n\mathcal R(\varepsilon)-C_\varepsilon/\ln2`$.

**Construction and finite accounting.** Fix the coordinate order
$`1,\ldots,n`$. Given a reconstruction $`z`$, answer pair $`i<j`$ by estimating
$`x_j`$ with $`z_j`$ and reading $`x_i`$. XOR these with the stored exact parity.
For every input the number of wrong pair answers is exactly

```math
N\Delta(x)=\sum_{j=1}^n(j-1)\mathbf1\{x_j\ne z_j\}.\qquad\text{(5)}
```

Partition the order into $`L`$ consecutive blocks, with positive lengths
$`m_\ell`$, cumulative endpoints $`s_\ell=\sum_{h\le\ell}m_h`$, and covering
radii $`r_\ell=\lfloor\delta_\ell m_\ell\rfloor`$, where
$`0<\delta_\ell<1/2`$. For each block use an ordinary Hamming cover of size
at most

```math
K_{m,r}=\min\left\{2^m,
\left\lceil\frac{(m+1)2^m}{\sum_{j=0}^r\binom mj}\right\rceil\right\}.
```

The [covering existence proof](../RESEARCH_NOTE.md#41-an-ordinary-covering-ingredient-credited-to-prior-coding-theory)
supplies these covers; the codebooks and coordinate order are fixed public
descriptions independent of the input. Retain one covering-center index per
block and one exact original-parity bit. All input-dependent storage is
charged:

```math
\begin{aligned}
B&\le1+\sum_{\ell=1}^L\left\lceil\log_2K_{m_\ell,r_\ell}\right\rceil,\\
\Delta(x)&\le\frac1N\sum_{\ell=1}^L(s_\ell-1)r_\ell
\quad\text{for every }x.
\end{aligned}\qquad\text{(6)}
```

The last bound follows directly from (5): at most $`r_\ell`$ coordinates are
wrong in block $`\ell`$, each with weight at most $`s_\ell-1`$. It makes no
probabilistic or independence assumption about reconstruction errors.

**Passage to the optimum.** Choose $`a'>a`$ and
$`\delta(u)=(1+e^{2a'u})^{-1}`$. Then

```math
\int_0^1 2u\delta(u)\,du<\varepsilon.
```

For a fixed $`L`$, take block lengths differing by at most one and put
$`\delta_\ell=\delta((\ell-1/2)/L)`$. As $`n\to\infty`$, (6) gives

```math
\begin{aligned}
\limsup_n\max_x\Delta(x)
&\le\frac{2}{L^2}\sum_{\ell=1}^L\ell\delta_\ell,\\
\limsup_n\frac Bn
&\le\frac1L\sum_{\ell=1}^L[1-h_2(\delta_\ell)].
\end{aligned}\qquad\text{(7)}
```

The distortion sum differs from its midpoint version
$`L^{-2}\sum_\ell(2\ell-1)\delta_\ell`$ by at most $`1/(2L)`$.
Both therefore converge to the stated weighted distortion integral as
$`L\to\infty`$. Choose a sufficiently fine but fixed $`L`$ to retain the
strict distortion margin. Rounding and covering overhead then vanish as
$`n\to\infty`$: the latter is $`O_{L,\delta}(\log n)`$ bits, besides the
single parity bit. This achieves distortion at most $`\varepsilon`$ for all
inputs and all sufficiently large $`n`$.

Finally let $`a'\downarrow a`$ and refine $`L`$. The rate in (7) approaches
$`\int_0^1[1-h_2(\delta_a(u))]du=\mathcal R(\varepsilon)`$. The order of
limits keeps the covers' index overhead sublinear and works for every
sufficiently large $`n`$, not just a divisibility subsequence. This proves (4).

## 4. The optimal success exponent below the rate

Fix $`0<\varepsilon<1/2`$. Write $`P_n^*(B,\varepsilon)`$ for the supremum
of $`\Pr_{X,R}\{\Delta_R(X)\le\varepsilon\}`$ over all schemes obeying the
stated resource rules with at most $`B`$ retained bits, without a separate
per-query error constraint. The exact-parity requirement
is retained. For any integer sequence $`B_n\ge1`$ with
$`B_n/n\to\rho\ge0`$,

```math
\boxed{\lim_{n\to\infty}-\frac1n\log_2
P_n^*(B_n,\varepsilon)
=\bigl(\mathcal R(\varepsilon)-\rho\bigr)_+.}\qquad\text{(8)}
```

The same exponent holds if the allowed schemes are restricted to
deterministic ordered-endpoint reads. This is a sharp **success** exponent,
or below-rate strong-converse exponent. It is not a theorem identifying
the optimal failure exponent above the rate.

**Weighted-ball volume.** Let

```math
V_n(\varepsilon)=\left|\left\{e\in\{0,1\}^n:
\sum_{j=1}^n(j-1)e_j\le\varepsilon N\right\}\right|,
\qquad v_n=2^{-n}V_n(\varepsilon).
```

We first prove

```math
-\frac1n\log_2v_n\longrightarrow\mathcal R(\varepsilon).\qquad\text{(9)}
```

For the upper bound on $`v_n`$, apply Chernoff to
$`\sum_{j=1}^n(j-1)(-1)^{U_j}`$, whose moment is the left side of (2).
At $`s=a/n`$ this gives
$`\ln v_n\le-n\mathcal R(\varepsilon)\ln2+O_\varepsilon(1)`$.

For the lower bound, choose $`a'>a`$ and a sufficiently fine but fixed
partition exactly as in Section 3. Every error vector with precisely
$`r_\ell=\lfloor\delta_\ell m_\ell\rfloor`$ ones in block $`\ell`$
has weighted cost at most $`\sum_\ell(s_\ell-1)r_\ell\le\varepsilon N`$
for all sufficiently large $`n`$. Therefore

```math
V_n(\varepsilon)\ge\prod_{\ell=1}^L
\binom{m_\ell}{r_\ell},\qquad
\liminf_n\frac1n\log_2V_n(\varepsilon)
\ge\frac1L\sum_{\ell=1}^Lh_2(\delta_\ell).
```

Here the ordinary binomial type bound, or Stirling's formula, has an
$`O(\log m_\ell)`$ error in each block. Let $`L\to\infty`$ and
$`a'\downarrow a`$, retaining the distortion margin before each large-$`n`$
limit. The right side approaches $`1-\mathcal R(\varepsilon)`$. Combined
with the upper bound, this proves (9).

**Partial covering with the charged number of labels.** For an integer
$`B\ge1`$, let $`K=2^{B-1}`$. Sample $`K`$ independent uniform reconstruction
centers. A fixed input lies in each translated weighted ball with
probability $`v_n`$. The expected fraction of inputs covered by their union
is $`1-(1-v_n)^K`$, so some fixed, input-independent codebook covers at least
that fraction. Repeated centers are permitted and do not affect the
argument.

Fix such a codebook once and for all. Given an input in the union, retain
an index of a center whose weighted ball contains it; outside the union,
retain any index. Store the exact total parity as one additional bit.
The index uses exactly $`B-1`$ bits, so total charged storage is $`B`$ bits.
The codebook is a fixed description, not uncharged input-dependent
information. Ordered endpoint decoding has table distortion at most
$`\varepsilon`$ on every covered input by (5). Consequently

```math
P_n^*(B,\varepsilon)\ge1-(1-v_n)^K
\ge1-e^{-Kv_n}
\ge(1-e^{-1})\min\{1,Kv_n\}.\qquad\text{(10)}
```

Since $`v_n=2^{-n\mathcal R(\varepsilon)+o(n)}`$, (10) bounds the
limsup of the exponent in (8) by
$`(\mathcal R(\varepsilon)-\rho)_+`$. The unrestricted converse (3)
bounds its liminf by the same quantity; probabilities never exceed one.
This proves (8), including the matching deterministic endpoint version.

At $`\rho=\mathcal R(\varepsilon)`$, (8) states only that the success
probability is not exponentially small; it does not assert convergence to
one. When $`\rho>\mathcal R(\varepsilon)`$, Section 3's worst-input cover
fits the budget for all sufficiently large $`n`$ and gives success exactly
one. No conclusion about a finite optimal memory gap follows from the
exponent equality.

## 5. Consequences and the quantifiers that remain distinct

Let $`B_{\rm exc}(n,\varepsilon,\zeta)`$ be the least worst-case summary
length for any randomized scheme with
$`\Pr_{X,R}\{\Delta_R(X)>\varepsilon\}\le\zeta`$, for a fixed
$`0\le\zeta<1`$. Equation (3) and the deterministic construction imply

```math
\lim_{n\to\infty}\frac{B_{\rm exc}(n,\varepsilon,\zeta)}n
=\mathcal R(\varepsilon).\qquad\text{(11)}
```

The same limit holds for its endpoint-only and public-address restrictions.
It also remains necessary if the required success probabilities $`p_n>0`$
are allowed to decrease with $`\log(1/p_n)=o(n)`$, since (3) then still gives
$`B\ge n\mathcal R(\varepsilon)-o(n)`$.

Apply the existing independent public permutation and mask to the
deterministic cover. For every fixed input and seed, the transformed query
table is a relabeling of a table whose distortion is at most
$`\varepsilon`$. Thus that bound holds for every input and every seed.
For each fixed input and fixed pair, the transformed input and query are
uniform and independent, so the single-query error over the seed is also at
most $`\varepsilon`$. The scheme consequently attains both guarantees at
once, with the same charged memory and a publicly determined endpoint read.

These strengthened guarantees preserve the same conceptual boundary: they
control the fraction of wrong pairs, not correctness of every pair. They
introduce no free sequence of reads and no guarantee for a pair chosen to
hit an error after seeing the seed. The weighted Hamming quantity (5) gives
a direct explanation for the established weighted coding curve. Its equality
with the unrestricted one-raw-read optimum is the operational theorem; the
present deductions do not independently settle that theorem's historical
priority.
