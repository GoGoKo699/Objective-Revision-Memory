# Decoder strategies, distortion balls, and the remaining theorem

Internal proof and priority note, 22 September 2026. Reviewed main:
`f1ecb10769f2b6ce0abe215d16f30767a02957d0`.
The reductions below identify which parts of the
[excess-distortion theorem](EXCESS_DISTORTION.md) are ordinary lossy coding,
and isolate its task-specific extremal statement. They introduce no separate
historical-novelty claim.

The subsequent [self-contained pair-query note](PAIR_QUERY_NOTE.md) supplies
the complete central proof without following links among earlier deductions.
This document retains the detailed source-coding reductions and finite
accounting comparisons.

## 1. Resources and the criterion

An encoder sees a uniform archive $`X\in\{0,1\}^n`$, $`n\ge3`$, before a pair
query. Its fixed worst-case summary contains at most $`B`$ input-dependent bits.
The original archive is uncharged and immutable; the whole summary and
unlimited computation are available. A query permits at most one raw-coordinate
bit read, whose address may depend on the summary, query, and independent
random tapes. A computed Boolean update, a word read, or a free input-dependent
cache is not allowed. Fixed codebooks and independent randomness are uncharged.

In the revision model, total parity $`p(X)`$ must be recoverable exactly from
the summary and seed alone, on every input, including unsuccessful inputs.
Pair $`q=\{i,j\}`$ requests $`p(X)\oplus X_i\oplus X_j`$.
Fixing all random tapes gives a counterfactual answer table: each pair is
considered separately with its own one-read budget, from the same summary.
Its distortion $`\Delta`$ is the fraction of incorrect pair answers. Write
$`P_n^*(B,\varepsilon)`$ for the greatest probability that
$`\Delta\le\varepsilon`$, over uniform input and independent tapes.
This criterion replaces, rather than additionally imposes, a per-query error
promise. It does not mean answering all pairs with one total read or protecting
against a pair chosen to hit an error after seeing the summary and seed.

## 2. Exact coding reduction without mandatory parity

First ask directly for $`X_i\oplus X_j`$, without requiring retained parity.
Let $`\mathcal T_n`$ contain every decoder strategy
$`t=((k_q,g_q))_q`$, where $`k_q\in[n]`$ and $`g_q:\{0,1\}\to\{0,1\}`$.
Constant functions include no-read answers. Set $`N=\binom n2`$ and

```math
D_n(x,t)=\frac1N\sum_{q=\{i,j\}}
\mathbf1\{g_q(x_{k_q})\ne x_i\oplus x_j\}.
```

This is a finite, generally nonseparable distortion measure with source
alphabet $`\{0,1\}^n`$ and reproduction alphabet $`\mathcal T_n`$.
A fixed $`B`$-bit scheme selects at most $`2^B`$ strategies, one for each memory
label. Conversely, any such codebook is implemented by retaining its selected
index and executing the indexed strategy. Thus this is exactly fixed-length
lossy coding; summary-dependent addresses are included in the reproduction
symbol. No strategy description is charged separately because the codebook
is fixed independently of the input. Random tapes cannot improve the optimal
average success probability: some deterministic realization performs at least
as well as their average. The same equivalence holds for expected distortion.

Kostina and Verdú, *Fixed-length lossy compression in the finite blocklength
regime*, [arXiv:1102.3944v3](https://arxiv.org/pdf/1102.3944), 4 February
2014, Definition 1, treats arbitrary alphabets and distortion. Section IV,
Theorem 8, Eq. (60), gives a converse through distortion-ball probabilities;
Theorems 9–10, Eqs. (65) and (70), give exact average random-code performance
and the resulting existence bound. These theorems are on printed p.6.
Their Theorem 12's Gaussian approximation additionally assumes stationary
memoryless sources and separable distortion. It does not automatically apply
to this growing strategy alphabet and its distortion.

## 3. The extremal statement that still needs evaluation

Define the largest one-strategy ball mass

```math
m_n(\varepsilon)=\max_{t\in\mathcal T_n}
2^{-n}|\{x:D_n(x,t)\le\varepsilon\}|.
```

For every fixed $`0<\varepsilon<1/2`$, the existing proof implies

```math
v_n(\varepsilon)\le m_n(\varepsilon)
=2^{o(n)}v_n(\varepsilon)
=2^{-n\mathcal R(\varepsilon)+o(n)},\tag{1}
```

where

```math
v_n(\varepsilon)=2^{-n}
\left|\left\{e:\sum_{j=1}^n(j-1)e_j\le\varepsilon N\right\}\right|.
```

Here $`\mathcal R`$ is the [research note's](../RESEARCH_NOTE.md) sharp rate:
with $`\eta=1-2\varepsilon`$ and
$`\eta=2\int_0^1u\tanh(au)\,du`$,
$`\mathcal R=(a\eta-\ln\cosh a)/\ln2`$.

**Proof.** The strategy answering $`i<j`$ with the raw bit $`x_i`$ has distortion
$`N^{-1}\sum_j(j-1)x_j`$, so its ball has mass $`v_n`$. For an arbitrary strategy,
write $`g_q(b)=\alpha_q\oplus\beta_qb`$. Its correctness signs are nonzero
residual characters with rows $`e_i+e_j+\beta_qe_{k_q}`$. Let $`S_t`$ be their
sum. The [rank-envelope moment bound](RANK_PROFILE_EXTENSIONS.md#equivalent-exponential-moment-formulation)
and Chernoff give, for every $`s\ge0`$,

```math
m_n(\varepsilon)\le
\exp\left[-sN\eta+\sum_{k=1}^n\ln\cosh(sk)\right].\tag{2}
```

At $`s=a/n`$, the integral estimate in
[excess distortion, Section 2](EXCESS_DISTORTION.md#2-finite-tail-bound-and-a-strong-converse)
is at most $`e^{C_\varepsilon}2^{-n\mathcal R}`$, where
$`C_\varepsilon=a\eta/2+\ln\cosh a`$.
The weighted-ball type-counting argument in
[Section 4](EXCESS_DISTORTION.md#4-the-optimal-success-exponent-below-the-rate)
proves $`v_n=2^{-n\mathcal R+o(n)}`$, with a fixed finite partition and strict
distortion margin before each large-$`n`$ limit. Squeezing proves (1).
The ratio assertion is subexponential; it is not a constant or polynomial
bound, nor finite equality of the two ball volumes.

## 4. Translation symmetry and finite success bounds

For a mask $`z\in\{0,1\}^n`$, keep the addresses of $`t`$ and define

```math
g_q^z(b)=g_q(b\oplus z_{k_q})\oplus z_i\oplus z_j.
```

Then $`D_n(x,t^z)=D_n(x\oplus z,t)`$. Consequently, uniform independent
translates of a maximizing strategy each cover any fixed input with probability
$`m_n`$. A codebook of $`K`$ such translates has expected covered fraction
$`1-(1-m_n)^K`$, so a deterministic codebook attains at least that fraction.
This is precisely the random-coding conversion above. Its address pattern is
the same for every codeword, and hence independent of the summary; the pattern
may use **nonendpoint** coordinates.

Let $`Q_n(B,\varepsilon)`$ be optimal success without mandatory parity.
Every $`B`$-bit revision scheme becomes a pair scheme by XORing its answer with
the parity recovered from its label. Every pair scheme becomes a revision
scheme after adding one exact-parity bit, including on inputs outside its good
set. Thus, for $`B\ge1`$,

```math
Q_n(B-1,\varepsilon)\le P_n^*(B,\varepsilon)
\le Q_n(B,\varepsilon).
```

Combining the translated codebook with the union bound over at most $`2^B`$
strategy balls gives the fully finite sandwich

```math
1-(1-m_n)^{2^{B-1}}
\le P_n^*(B,\varepsilon)
\le\min\{1,2^Bm_n\}.\tag{3}
```

The lower construction charges $`B-1`$ index bits and one parity bit.
Moreover, with $`u=2^Bm_n`$,
$`1-(1-m_n)^{2^{B-1}}\ge1-e^{-u/2} \ge(1-e^{-1/2})\min\{1,u\}`$.
Thus the two sides differ by at most a universal multiplicative constant.
The lower bound already uses deterministic summary-independent addresses.
Together with (1), (3) gives the existing success exponent
$`(\mathcal R-\rho)_+`$ when $`B_n\ge1`$ and $`B_n/n\to\rho`$.
The coding conversion supplies no independent novelty and does not identify
a finite optimal memory gap for endpoint-only access.

## 5. Covers with a fixed address pattern

The symmetry also gives a finite worst-input comparison, without asymptotics.
For $`0\le\varepsilon<1/2`$, put $`c_n=n\ln2+1`$ and
$`K=\lceil c_n/m_n(\varepsilon)\rceil`$. The expected number of uncovered
inputs after $`K`$ random translates is at most
$`2^ne^{-Km_n}\le e^{-1}<1`$. Since that number is an integer, some fixed
codebook covers the whole cube. Its charged memory, including parity, is at most

```math
1+\lceil\log_2K\rceil.
```

Let $`B_{\rm cov}^{\rm arb}`$ and $`B_{\rm cov}^{\rm fixed}`$ be deterministic
worst-input cover optima with, respectively, summary-dependent addresses and
one address pattern fixed by the query. If an unrestricted $`B`$-bit revision
cover exists, the union bound gives $`m_n\ge2^{-B}`$. With
$`\ell=\lceil\log_2c_n\rceil`$, we have $`K\le2^{B+\ell}`$, so

```math
B_{\rm cov}^{\rm arb}\le B_{\rm cov}^{\rm fixed}
\le B_{\rm cov}^{\rm arb}+1+\lceil\log_2(n\ln2+1)\rceil.\tag{4}
```

All translations preserve the maximizing strategy's addresses. This proves
(4) for fixed addresses that may be nonendpoints; replacing that class by
endpoint addresses would be an unjustified extra conclusion. The argument is
an existence proof and supplies no efficient algorithm for finding a maximizing
strategy or the cover.

## 6. Why infinite parity penalties are insufficient

Augmenting a reproduction by a parity flag and assigning infinite distortion
when that flag is wrong only enforces parity on successful inputs. It does not
enforce exact parity on the entire archive distribution in partial-cover coding.

For example, take $`n=3`$, one reproduction symbol, parity flag zero, and the
pair strategy that reads the complementary coordinate. On every even-parity
input this correctly returns the pair parity. Under the infinite-penalty
formulation, the zero-bit code therefore succeeds on half the inputs at
distortion zero. Yet no zero-bit summary can determine total parity exactly.
The additional parity bit in (3) avoids this mismatch even on failed inputs.

## 7. An exact action-dependent side-information comparison

Permuter and Weissman, *Source Coding with a Side Information “Vending
Machine”*, [arXiv:0904.2311v2](https://arxiv.org/pdf/0904.2311), 30 April
2009, Section II-F, Theorem 4, Eqs. (49)–(51), printed pp.15–16, treat
indirect source coding with decoder actions. This gives a closer comparison
than merely pointing out differences from their direct-source Theorem 1.

Fix the archive width $`n`$, and repeat independent archives $`L`$ times before
taking $`L\to\infty`$. In their notation the hidden source is our
$`S=(X,Q)`$, with $`X`$ uniform and $`Q`$ an independent uniform pair. The encoder
observes only $`Z=X`$. An action $`A`$ is a complete address map $`q\mapsto k_q`$,
chosen from the received message; the side-information channel returns
$`Y=(Q,X_{A(Q)})`$. Reconstruction is a binary pair-parity answer, with
distortion $`\mathbf1\{\widehat b\ne X_i\oplus X_j\}`$ when $`Q=\{i,j\}`$.
Every action costs one raw read; a decoder can ignore that bit. The finite
action alphabet may be large. Its selection is paid through the message,
not provided as free input-dependent information. The encoder never sees $`Q`$.

Let $`F_n(D)`$ be their asymptotic rate in bits per archive for this instance,
and define the ordinary information rate-distortion function on strategies by

```math
G_n(D)=\min_{P_{T|X}:\,\mathbb E D_n(X,T)\le D} I(X;T).
```

All information quantities in this section use bits. Theorem 4 evaluates
$`F_n(D)`$ as the minimum of $`I(X;A)+I(X;U\mid Y,A)`$ over admissible auxiliaries
and reconstructions. Absorb $`A`$ into $`U`$, so $`A`$ is a function of $`U`$.
Their channel factorization gives $`U-(X,A)-Y`$ and hence

```math
I(X;A)+I(X;U\mid Y,A)=I(X;U)-I(U;Y\mid A).
```

Because $`Q`$ is independent of $`(X,U,A)`$,

```math
0\le I(U;Y\mid A)=I(U;X_{A(Q)}\mid Q,A)\le1.
```

Each auxiliary value fixes an address map and an answer function for every
pair and read bit, hence a strategy $`T`$. Collapsing auxiliary values that
induce the same strategy preserves distortion and cannot increase
$`I(X;T)`$. Conversely, any stochastic strategy label is an admissible
auxiliary. Therefore

```math
G_n(D)-1\le F_n(D)\le G_n(D).\tag{5}
```

This is a reduction to their theorem, with a one-bit bound on the possible
benefit of jointly decoding repeated side information. It is not a claim that
their paper evaluates the strategy optimization for pair parity.

For completeness, the existing moment converse also evaluates its leading
rate. Apply the Gibbs variational inequality separately to each conditional
law $`P_{X|T=t}`$ and its signed correctness sum $`S_t`$. Averaging gives

```math
G_n(D)\ln2\ge sN(1-2D)-\sum_{k=1}^n\ln\cosh(sk),\qquad s\ge0.
```

This argument permits arbitrary posterior laws and stochastic encoders.
At fixed $`0<D<1/2`$, the deterministic endpoint covers bound $`G_n(D)`$ above
by $`n\mathcal R(D)+o(n)`$; the displayed bound and (5) give

```math
\lim_{n\to\infty}\frac{F_n(D)}n
=\lim_{n\to\infty}\frac{G_n(D)}n=\mathcal R(D).
```

The prior theorem takes $`L\to\infty`$ at fixed $`n`$ and controls expected
distortion. It does not itself establish the single-archive worst-input
table guarantee or the success exponent as $`n\to\infty`$. Both $`F_n`$ and
$`G_n`$ here concern direct pair parity; retaining old parity exactly on all
inputs requires at most one additional bit per archive. Repeated coding
and an expected-distortion constraint must not silently replace that rule.

## 8. Contribution decision

The general distortion formulation, sphere-volume converse, random coding,
translation covering, and the resulting success-exponent conversion are
established ingredients or direct deductions. Equation (1) isolates the
task-specific content: arbitrary one-read strategy balls have the same
exponential volume as ordered-endpoint weighted Hamming balls. The existing
proof evaluates that quantity using the elementary rank envelope and entropy
machinery. Whether this precise operational evaluation was already known
remains unresolved. It is the candidate claim to compare, rather than promoting
the generic coding conversion as another independent research contribution.

The next useful review question is concrete: **does an existing theorem
already evaluate $`m_n(\varepsilon)`$, or imply (1) through a verified reduction
preserving the raw-read rule and error quantifiers?** The ordinary coding
conversion and the action-dependent information characterization are now
attributed. A focused internal short note can lead with (1), group the coding
consequences together, and retain the finite endpoint separation as context.
Priority and publication significance remain separate unresolved judgments.
