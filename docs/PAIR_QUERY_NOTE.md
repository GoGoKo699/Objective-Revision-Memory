# One raw-bit read for approximate pair queries

Internal short-note candidate, 22 September 2026. Reviewed repository base:
`a258ffc130dad5926551aa6c07e6413505d4aeef`.
This is a self-contained proof packet, not a manuscript release or a
historical-priority certificate.

The central conclusion is that an arbitrary one-read decoder strategy handles
no exponentially larger set of low-error inputs than a fixed ordered-endpoint
strategy. Ordinary coding then determines the memory rate, worst-input covering
rate, and success exponent. These consequences belong to one result. The
geometry, entropy argument, and coding conversions use classical ingredients.

## 1. Model and the extremal quantity

Let $`X`$ be uniform on $`\{0,1\}^n`$, with $`n\ge3`$, and put $`N=\binom n2`$.
An encoder sees $`X`$ before an unordered pair query $`q=\{i,j\}`$ and retains at
most $`B`$ input-dependent bits. The immutable archive is uncharged. The decoder
can inspect the entire summary, compute without restriction, and read at most
one **raw coordinate bit**. Its address can depend on the summary, query, and
independent random tapes. Fixed codebooks and independent randomness are free;
input-dependent caches and transcripts are charged.

First consider direct pair parity $`X_i\oplus X_j`$. A fixed decoder strategy is
$`t=((k_q,g_q))_q`$, where $`k_q\in[n]`$ and $`g_q:\{0,1\}\to\{0,1\}`$.
Constant functions include no-read answers. Define

```math
\begin{aligned}
D_n(x,t)&=\frac1N\sum_{q=\{i,j\}}
\mathbf1\{g_q(x_{k_q})\ne x_i\oplus x_j\},\\
m_n(\varepsilon)&=\max_t2^{-n}|\{x:D_n(x,t)\le\varepsilon\}|.
\end{aligned}
```

This distortion considers each query separately with its own one-read budget.
For randomized decoding, include an input-independent tape for each query
among the fixed tapes defining that table.
It is not an execution answering all queries with one total read. A memory
label selects a strategy, so this formulation includes arbitrary nonlinear
preprocessing and summary-dependent addresses.

In the revision model, the summary must additionally recover total parity
$`p(X)`$ exactly on **every** input, and the requested answer is
$`p(X)\oplus X_i\oplus X_j`$. A revision label gives a direct-pair strategy by
XORing its answers with its retained parity. Conversely, one additional parity
bit converts any direct-pair scheme into a revision scheme, including on
inputs outside its low-error set. All coding bounds below charge this bit.

## 2. Central theorem

Fix $`0<\varepsilon<1/2`$, and write $`\eta=1-2\varepsilon`$. There is a unique
$`a>0`$ satisfying

```math
\eta=2\int_0^1u\tanh(au)\,du.
```

Set

```math
\begin{aligned}
\mathcal R(\varepsilon)&=\frac{a\eta-\ln\cosh a}{\ln2},\\
v_n(\varepsilon)&=2^{-n}\left|\left\{e:
\sum_{j=1}^n(j-1)e_j\le\varepsilon N\right\}\right|.
\end{aligned}
```

**Theorem.** For fixed interior error,

```math
v_n(\varepsilon)\le m_n(\varepsilon)
=2^{o(n)}v_n(\varepsilon)
=2^{-n\mathcal R(\varepsilon)+o(n)}.\tag{1}
```

For every $`s\ge0`$ there is also the finite bound

```math
m_n(\varepsilon)\le
\exp\left[-sN\eta+\sum_{k=1}^n\ln\cosh(sk)\right].\tag{2}
```

Equation (1) compares exponential volumes. It does not assert finite equality,
a constant-factor comparison, or uniformity when $`\varepsilon`$ varies with $`n`$.

**Why full residual rank is insufficient.** The constant-zero answer table and
the ordered-endpoint table both have residual rank $`n-1`$ and exactly two
zero-error inputs. But if $`w=|x|`$, the former has distortion
$`w(n-w)/N`$. Counting its two allowed ranges of Hamming weights gives good-set
exponent
$`1-h_2((1-\sqrt{1-2\varepsilon})/2)`$, a different function from
$`\mathcal R(\varepsilon)`$. Thus the complete family's rank and exact kernel
size lose information at leading exponential order. The all-subsets incidence
bound below supplies the missing information.

## 3. Converse: count independent residuals on a good set

Write $`g_q(b)=\alpha_q\oplus\beta_qb`$. Its correctness sign is
$`\sigma_q(-1)^{a_q\cdot x}`$, where $`\sigma_q=(-1)^{\alpha_q}`$ and

```math
a_q=e_i+e_j+\beta_qe_{k_q}\ne0.
```

**Coverage by a rank-$`r`$ residual space.** Take any subset $`J`$ of pair labels,
and let $`W`$ span their selected residual rows, with $`\dim W=r`$.
Choose $`n-r`$ coordinate images forming a basis of $`\mathbb F_2^n/W`$;
call their indices $`I`$ and the remaining $`r`$ indices $`C`$.
A pair wholly in $`I`$ cannot have a zero-read residual in $`W`$. If its residual
uses a read, its two basis images must sum to the image of that read coordinate.
This coordinate belongs to $`C`$, and distinct basis pairs have distinct sums.
Each of the $`r`$ coordinates in $`C`$ therefore accounts for at most one such
pair. All other pairs touch $`C`$. Consequently

```math
|J|\le\binom n2-\binom{n-r}{2}+r
=nr-\frac{r(r-1)}2=:\Phi_n(r).\tag{3}
```

This holds for every subset, with repeated residual rows allowed. It is the
elementary basis-pair count, equivalently fundamental-circuit uniqueness;
no standalone geometric novelty is claimed.

**An entropy inequality for any input distribution.** Let $`P`$ be any law on
the cube and $`b_q=|\mathbb E_P(-1)^{a_q\cdot X}|`$. Sort rows by decreasing
bias and greedily retain independent rows. Their biases are
$`t_1\ge\cdots\ge t_d`$, padded by zeros to length $`n`$. At each positive
threshold $`z`$, the retained rows above that threshold span all rows above it.
If their rank is $`r(z)`$, (3) and threshold integration give

```math
\sum_q b_q\le\int_0^1\Phi_n(r(z))\,dz
=\sum_{j=1}^n(n-j+1)t_j.\tag{4}
```

Complete the retained rows to a binary basis. This invertible change of
coordinates preserves entropy; entropy subadditivity then gives

```math
\sum_{j=1}^nc(t_j)\le n-H_P(X),\qquad
c(t)=1-h_2((1-t)/2).
```

This is the independent-character entropy budget in the entropic proof of
Chang's inequality, before its quadratic relaxation. The elementary conjugacy

```math
zt-\ln2\,c(t)\le\ln\cosh z
```

follows by maximizing over $`0\le t\le1`$, with optimizer $`t=\tanh z`$.
Combining it with (4) proves

```math
s\sum_q b_q\le[n-H_P(X)]\ln2
+\sum_{k=1}^n\ln\cosh(sk).\tag{5}
```

Now take $`P`$ uniform on the nonempty good set
$`G_t=\{x:D_n(x,t)\le\varepsilon\}`$. The signed correctness sum is at
least $`N\eta`$ on every point of this set, hence $`\sum_qb_q\ge N\eta`$.
Also $`H_P(X)=\log_2|G_t|`$. Equation (5) gives (2) for every strategy;
empty good sets are harmless. This argument imposes no affine structure on
the good set.

**Evaluation of the exponent.** The function
$`2\int_0^1u\tanh(au)du`$ is continuous, strictly increasing for $`a>0`$,
and has limits zero and one. This proves existence and uniqueness of $`a`$.
Let $`I(a)=\int_0^1\ln\cosh(au)du`$. Integration by parts gives
$`I(a)=\ln\cosh a-a\eta/2`$. At $`s=a/n`$, the monotone Riemann-sum bound

```math
\sum_{k=1}^n\ln\cosh(ak/n)\le nI(a)+\ln\cosh a
```

therefore turns (2) into

```math
m_n(\varepsilon)\le e^{C_\varepsilon}2^{-n\mathcal R(\varepsilon)},
\qquad C_\varepsilon=a\eta/2+\ln\cosh a.\tag{6}
```

For $`\delta_a(u)=(1+e^{2au})^{-1}`$, the same calculation gives

```math
\mathcal R(\varepsilon)=\int_0^1[1-h_2(\delta_a(u))]du,
\qquad \int_0^12u\delta_a(u)du=\varepsilon.
```

This is the established weighted fair-binary distortion allocation.

## 4. Attainment: a weighted ball and a strict tilted margin

For $`i<j`$, the strategy answering direct pair parity with the raw bit $`x_i`$
makes an error precisely when $`x_j=1`$. Its good set has mass $`v_n`$, proving
$`m_n\ge v_n`$. It remains to determine the latter's exponent.

Choose a fixed $`a'>a`$. Under a product measure $`Q_n`$, make coordinates
$`E_{k+1}`$ independent with

```math
p_k:=Q_n(E_{k+1}=1)=(1+e^{2a'k/n})^{-1},\qquad 0\le k<n.
```

For $`W_n=\sum_{k=0}^{n-1}kE_{k+1}`$,

```math
\begin{aligned}
\frac{\mathbb E_{Q_n}W_n}{N}&\longrightarrow
2\int_0^1u\delta_{a'}(u)du<\varepsilon,\\
\mathrm{Var}_{Q_n}(W_n)&\le\tfrac14\sum_{k=0}^{n-1}k^2=O(n^3).
\end{aligned}
```

Since $`N^2`$ has order $`n^4`$, Chebyshev's inequality implies
$`Q_n(W_n\le\varepsilon N)\to1`$. The strict inequality before the
large-$`n`$ limit is essential.

Let $`L_n(E)=-\log_2Q_n(E)`$. It is a sum of independent information terms,
each bounded by $`\log_2(1+e^{2a'})`$. Thus

```math
\begin{aligned}
\mathbb E_{Q_n}L_n=H(Q_n)&=\sum_{k=0}^{n-1}h_2(p_k)\\
&=n\int_0^1h_2(\delta_{a'}(u))du+o(n),\\
\mathrm{Var}_{Q_n}(L_n)&=O_{a'}(n).
\end{aligned}
```

For any fixed $`\gamma>0`$, the intersection of the weighted ball with
$`\{L_n\ge H(Q_n)-n\gamma\}`$ has $`Q_n`$-probability tending to one.
Each word in this intersection has probability at most
$`2^{-H(Q_n)+n\gamma}`$, so the ball contains at least
$`(1-o(1))2^{H(Q_n)-n\gamma}`$ words. Consequently

```math
\liminf_n\frac1n\log_2v_n\ge
-1+\int_0^1h_2(\delta_{a'}(u))du-\gamma.
```

First let $`\gamma\downarrow0`$, then $`a'\downarrow a`$. Continuity and
(6), together with $`v_n\le m_n`$, prove (1) for all sufficiently large
lengths without a divisibility restriction. This completes the central proof.

## 5. One coding corollary, with the parity bit charged

**Corollary.** At fixed $`0<\varepsilon<1/2`$, the revision model has leading
memory rate $`\mathcal R(\varepsilon)`$ for deterministic worst-input table
distortion, average input-and-pair error, and each-fixed-pair marginal error.
Publicly chosen endpoint reads attain these rates. If $`P_n^*(B,\varepsilon)`$
optimizes the probability of table distortion at most $`\varepsilon`$, with no
additional marginal-error promise, then for integers $`B_n\ge1`$ with
$`B_n/n\to\rho\ge0`$,

```math
\lim_n-\frac1n\log_2P_n^*(B_n,\varepsilon)
=(\mathcal R(\varepsilon)-\rho)_+.\tag{7}
```

**Partial covers and the success exponent.** After fixing independent tapes,
each of at most $`2^B`$ memory labels supplies a strategy. Its successful inputs
are contained in a ball of mass at most $`m_n`$. Therefore
$`P_n^*(B,\varepsilon)\le\min\{1,2^Bm_n\}`$, also after averaging tapes.

For attainment, choose $`K=2^{B-1}`$ independent uniform reconstruction centers
$`z`$. A fixed input lies in each translated weighted ball with probability
$`v_n`$. Some deterministic codebook consequently covers a fraction at least
$`1-(1-v_n)^K`$. Retain a covering center's index, or any index outside the
union, together with exact parity. Answer $`i<j`$ by
$`p(x)\oplus x_i\oplus z_j`$. Its address is always $`i`$, and its wrong-pair
count is exactly $`\sum_j(j-1)\mathbf1\{x_j\ne z_j\}`$. All $`B`$ bits are
charged, including parity on failed inputs. Since

```math
1-(1-v_n)^K\ge1-e^{-Kv_n}
\ge(1-e^{-1})\min\{1,Kv_n\},
```

(1) proves (7). Zero exponent at the critical rate does not assert that success
tends to one; an optimal failure exponent is not claimed.

**Worst-input covers.** With
$`K=\lceil(n\ln2+1)/v_n\rceil`$ centers, the expected number of uncovered
inputs is at most $`2^ne^{-Kv_n}<1`$. Some fixed codebook covers every input.
Its storage is $`1+\lceil\log_2K\rceil=n\mathcal R+o(n)`$ bits, including
parity. Conversely, success probability one and (6) require
$`B\ge n\mathcal R-C_\varepsilon/\ln2`$.

**Expected and marginal error.** For the expected-error converse, use (5)
directly on each posterior $`P_{X\mid M=m,R=r}`$ after fixing the tapes.
If $`d_{m,r}`$ is its average pair error, its signed correctness sum has mean
$`N(1-2d_{m,r})`$. Average (5), using

```math
\mathbb E[n-H(X\mid M=m,R=r)]
=I(X;M\mid R)\le B
```

because $`X`$ is uniform and independent of $`R`$. Overall error at most
$`\varepsilon`$ gives
$`B\ln2\ge sN\eta-\sum_{k=1}^n\ln\cosh(sk)`$, and hence the same rate.
This proof does not infer a mean bound from a tail statement alone.

The deterministic cover supplies the upper bound. To obtain each-fixed-input,
each-fixed-pair error at most $`\varepsilon`$ over the seed, apply an independent
uniform coordinate permutation and XOR mask before using that cover, and
translate the queried raw read back to the original archive. For each fixed
input and pair, the transformed input and pair are uniform and independent.
Explicitly, let $`Y_a=x_{\pi(a)}\oplus Z_a`$ for public permutation $`\pi`$ and
mask $`Z`$. For transformed pair $`a<b`$ and the center $`z`$ selected for $`Y`$,
read $`x_{\pi(a)}`$ and return
$`p(x)\oplus x_{\pi(a)}\oplus z_b\oplus Z_b`$.
An error occurs exactly when $`Y_b\ne z_b`$. Thus for each seed the error table
is relabeled and its worst-input distortion remains at most $`\varepsilon`$.
Store original parity as the same charged extra bit. Addresses depend only
on query and public seed.
The per-pair input-averaged criterion is squeezed between the average-error
converse and this stronger construction.

All these guarantees concern a fraction of erroneous pairs or a marginal
error probability. They permit erroneous pairs and do not protect a query
chosen to hit an error after seeing the seed and summary. The codebooks are
existence constructions, with no efficient encoding claim.

## 6. Attribution and research decision

The mathematical contribution to assess is (1): arbitrary-address strategy
balls match ordered-endpoint weighted balls at exponential scale. The
following ingredients are established; source-specific reductions and broader
comparisons are recorded in the [literature ledger](LITERATURE_COMPARISON.md).

- The basis count uses independent pair sums or fundamental-circuit uniqueness:
  Even-Zohar, [arXiv:1108.4902v2](https://arxiv.org/pdf/1108.4902v2), Example 11;
  Tutte, [*Lectures on Matroids*](https://doi.org/10.6028/jres.069B.001), Section 2.2.
- The entropy budget is Impagliazzo–Moore–Russell,
  [arXiv:1205.0263v2](https://arxiv.org/pdf/1205.0263v2), Eq. (1) and Section 2.
- The weighted coding law is a specialization of Martinian–Wornell–Zamir,
  [*Source Coding With Distortion Side Information*](https://sia.mit.edu/wp-content/uploads/2015/04/2008-martinian-wornell-zamir-it.pdf),
  Section IV-E, Eqs. (40)–(41), and Appendix II, Eq. (121).
- General distortion-ball converses and random-code conversions are given by
  Kostina–Verdú, [arXiv:1102.3944v3](https://arxiv.org/pdf/1102.3944),
  Definition 1 and Theorems 8–10. Here a reproduction is a whole strategy;
  the scalar distortion need not be coordinatewise separable.

The [operational reduction](OPERATIONAL_REDUCTION.md) supplies exact finite
coding comparisons and an action-dependent side-information embedding. These
do not replace the evaluation of the particular strategy balls in (1).
Retaining old parity adds at most one bit, so this example establishes no new
leading cost for preserving an earlier objective.

Leading equivalence is also weaker than finite equivalence: endpoint-only
zero-error memory is $`n-1`$, while the unrestricted optimum is
$`n-\lfloor\log_2(n+1)\rfloor`$; see the
[endpoint proof](THEOREM_BRIEF.md#4-a-finite-separation-at-zero-error) and
[preserved exact baseline](../BASELINE_NOTE.md). These are context, not
dependencies of the proof above.

This is a focused sharp result for one canonical query family, assembled from
classical deductions. The [completed bounded assessment](CONTRIBUTION_ASSESSMENT.md) supports its significance as a focused theoretical contribution. The proof alone does not certify historical priority or establish a general data-structure theorem or a theory of objective preservation. Manuscript preparation is on hold.
