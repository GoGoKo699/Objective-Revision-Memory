# Delayed parity revision with limited factual access

Research working note, 22 September 2026. Editorial consolidation of the exact parity checkpoint and bounded-error checkpoint v2. Mathematical statements are retained; documentation is reorganized for this repository. The conjunction checkpoint is a different model and is documented separately.

**Status:** complete written arguments and finite regression tests, not a priority claim, peer-reviewed publication, or formal proof certificate. The [literature comparison](docs/LITERATURE_COMPARISON.md) distinguishes known ingredients from candidate contributions.

## 1. Model and accounting

An $`n`$-bit input $`X`$ is observed, with $`n\geq3`$. The original task is total parity:

```math
p(X)=\bigoplus_{a=1}^n X_a.
```

Before a query is known, an encoder forms $`M=f_R(X)`$ using at most $`B`$ bits. The public random seed $`R`$ is independent of $`X`$. A query is an unordered pair $`\{i,j\}`$ of distinct coordinates and asks for

```math
p_{ij}(X)=p(X)\oplus X_i\oplus X_j.
```

The original parity must be recoverable exactly from $`(M,R)`$ without a raw probe. To answer a revision, the decoder receives $`(M,R,i,j)`$, may read at most one original coordinate $`X_k`$, and performs arbitrary computation. The address may depend on the entire memory, seed, and query. All input-dependent retained information is charged to $`B`$. An external immutable archive still contains $`X`$; its storage is not charged to $`B`$. Probe cost is per raw bit, not per word or arbitrary function. Prior query transcripts and auxiliary input-dependent caches are not free. Time, public algorithms, and input-independent randomness are not charged.

For exact results, correctness is required for every input and query. For bounded-error results, $`X`$ is uniform and each fixed query has error at most $`\varepsilon`$, averaged over $`X`$ and randomness. The converses actually need only average error over uniform inputs and uniform pairs. Randomized constructions below can attain the stronger guarantee for every fixed input and query over the public seed. This is not simultaneous success on all queries or a guarantee for an adversarial query chosen after seeing the seed and memory.

Private randomness can be made public for lower bounds; doing so only strengthens the model. For each deterministic random-tape component, exact original parity is still recoverable. All logarithms are base two unless $`\ln`$ is written. Write

```math
N=\binom n2,\qquad
h_2(u)=-u\log_2u-(1-u)\log_2(1-u),\qquad
\Phi_n(z)=nz-\frac{z(z-1)}2.
```

Use $`h_2(0)=h_2(1)=0`$. The function $`\Phi_n`$ is increasing and concave on $`[0,n]`$. We may restrict to $`B\leq n`$, since retaining all of $`X`$ otherwise suffices.

This is a systematic-data-structure problem. Deleting two parity coefficients is not a monotone acceptance refinement and need not be a small change in the rule's behavioral consequences.

## 2. Exact optimum

**Theorem E.** For all $`n\geq3`$, the minimum memory with one raw probe and zero error is

```math
B_1^*(n)=n-\lfloor\log_2(n+1)\rfloor.
```

With two probes the exact optimum is one bit. Deleting only one coordinate also needs only the original parity bit and one probe.

### Lower bound and local-to-global property

Fix a nonempty memory cell $`C=f^{-1}(m)`$. Original parity is constant on $`C`$. To answer a pair revision, the decoder must compute $`X_i\oplus X_j`$ on $`C`$ from at most one observed bit. Every Boolean function of one bit is constant, that bit, or its complement.

In the vector space of Boolean functions on $`C`$, quotient by constant functions and denote a class by $`[g]`$. Then

```math
G=\{[0],[X_1],\ldots,[X_n]\}
```

is closed under XOR: the one-probe property puts every sum of two coordinate classes back in $`G`$. Thus $`G`$ is a binary vector space. If its dimension is $`d_C`$, then $`2^{d_C}\leq n+1`$. Select coordinate classes forming a basis. Every input coordinate restricted to $`C`$ is an affine function of those selected coordinates. Their values therefore distinguish the inputs in $`C`$, so

```math
|C|\leq2^{d_C}\leq2^{\lfloor\log_2(n+1)\rfloor}.
```

Partitioning all $`2^n`$ inputs requires at least $`2^{n-\lfloor\log_2(n+1)\rfloor}`$ memory values. No linearity assumption was made about the encoder.

The same closure proves a local-to-global statement: any exact one-probe representation for all pair revisions also supports every parity objective with one probe. A sum of any number of coordinate classes is in $`G`$. This statement is about parity objectives, not arbitrary Boolean functions.

### Matching affine construction

Set $`d=\lfloor\log_2(n+1)\rfloor`$ and $`a=2^d-1`$. Number coordinates from 1. Interpret each $`i\leq a`$ as a nonzero $`d`$-bit vector. Let $`u_b=X_{2^b}`$ for $`b=0,\ldots,d-1`$. Define

```math
z_i=\begin{cases}
X_i\oplus\langle i,u\rangle,&1\leq i\leq a,\\
X_i,&i\gt a.
\end{cases}
```

For each pivot $`i=2^b`$, $`z_i=0`$, so store only the other $`n-d`$ values. Since $`d\geq2`$, the XOR of all nonzero $`d`$-bit labels is zero. Hence original parity is the XOR of the stored values.

To obtain $`X_i\oplus X_j`$, set $`\lambda=(i\text{ if }i\leq a\text{ else }0)\oplus(j\text{ if }j\leq a\text{ else }0)`$. If $`\lambda=0`$, return $`z_i\oplus z_j`$. Otherwise read $`X_\lambda`$ and return

```math
z_i\oplus z_j\oplus X_\lambda\oplus z_\lambda.
```

XOR with the known original parity to answer the revision. This is established simplex-code machinery used as a matching construction, not a new code family. Two probes need only stored $`p(X)`$ and direct reads of $`X_i,X_j`$; one bit is necessary because the original task is nonconstant.

## 3. Rank-coverage lemma

For a collection $`E`$ of distinct unordered pairs, choose for each pair a row

```math
a_{ij}=e_i+e_j+\beta_{ij}e_{k_{ij}},\qquad \beta_{ij}\in\{0,1\},
```

where $`e_k`$ is a coordinate basis vector. These rows are nonzero even if $`k`$ is an endpoint. Let $`W`$ be their span and $`r=\dim W`$.

**Lemma R.**

```math
|E|\leq\Phi_n(r).
```

**Proof.** In the quotient $`\mathbb F_2^n/W`$, choose $`n-r`$ coordinate images forming a basis, indexed by $`I`$. A selected pair with both endpoints in $`I`$ must satisfy $`v_i+v_j=v_k`$, with $`k`$ outside $`I`$: independence rules out a zero sum or a single basis vector. Distinct pairs of basis vectors have distinct sums. Only $`r`$ coordinates lie outside $`I`$, so there are at most $`r`$ such selected pairs. There are at most $`N-\binom{n-r}{2}`$ pairs not wholly in $`I`$. Thus

```math
|E|\leq N-\binom{n-r}{2}+r=\Phi_n(r).
```

The argument holds for every subset of selected rows. The bound may exceed $`N`$ at large rank; it is not a claim of finite-length attainability at every rank.

## 4. Arbitrary preprocessing with bounded error

**Theorem A.** If the average revised-query error is at most $`\varepsilon\lt 1/2`$, then

```math
N[1-h_2(\varepsilon)]\leq\Phi_n(B).
```

Equivalently,

```math
B\geq n+\tfrac12-\sqrt{n(n-1)h_2(\varepsilon)+2n+\tfrac14}.
```

Round upward for integral $`B`$ and also require $`B\geq1`$. At zero error this bound is weaker than Theorem E.

### Conditional information cost

Fix a seed and a nonempty memory cell. Since original parity is known, an optimal one-probe decoder predicts $`X_i+X_j`$ as a constant, $`X_k`$, or its complement. Its conditional error therefore has the form

```math
\eta_{ij}=\Pr[a_{ij}\cdot X\ne c_{ij}\mid M=m,R],\qquad0\leq\eta_{ij}\leq\tfrac12,
```

with rows of the form in Lemma R. Replacing a decoder by its cellwise optimum cannot worsen overall error; it does not mean every cell meets the target $`\varepsilon`$.

Let $`w_{ij}=1-h_2(\eta_{ij})`$ and $`D=n-H(X\mid M=m,R)`$. For any independent subset $`J`$ of rows, extend $`J`$ to a basis of $`\mathbb F_2^n`$. An invertible linear change of variables preserves entropy. Subadditivity gives

```math
H(X\mid m,R)\leq\sum_{e\in J}h_2(\eta_e)+(n-|J|),
\qquad D\geq\sum_{e\in J}w_e.
```

This uses no assumption that the conditional distribution is affine.

### Weighted rank and averaging

Sort rows by decreasing weight and greedily retain independent rows. At threshold $`s\in[0,1]`$, let $`q(s)`$ be the number of rows of weight at least $`s`$ and $`r(s)`$ their rank. The greedy independent set has total weight $`L=\int_0^1r(s)\,ds\leq D`$. Applying Lemma R at every threshold and then concavity,

```math
\sum_e w_e=\int_0^1q(s)\,ds
\leq\int_0^1\Phi_n(r(s))\,ds
\leq\Phi_n(L)\leq\Phi_n(D).
```

For uniform $`X`$ independent of the seed,

```math
\mathbb E D=I(X;M\mid R)\leq H(M\mid R)\leq B.
```

Average over cells and seeds and use concavity of $`\Phi_n`$. Finally, concavity of binary entropy yields

```math
N[1-h_2(\varepsilon)]\leq
\mathbb E\sum_e[1-h_2(\eta_e)]\leq\Phi_n(B).
```

This proves Theorem A with memory-dependent addresses, arbitrary preprocessing, and errors concentrated in particular cells.

For fixed $`\varepsilon\lt 1/2`$, the asymptotic lower rate is $`1-\sqrt{h_2(\varepsilon)}\gt 0`$. Two probes still succeed exactly with one bit. The extensive one-probe memory requirement is therefore not solely a zero-error effect.

## 5. Affine preprocessing

An affine encoder has $`M=A_RX+b_R`$ over $`\mathbb F_2`$; the matrix and offset depend on the independent seed but not otherwise on $`X`$. Decoders are unrestricted.

**Theorem L.**

```math
N(1-2\varepsilon)\leq\Phi_n(B),
```

and, for every fixed $`0\lt \varepsilon\lt 1/2`$,

```math
B_{\mathrm{aff}}(n,\varepsilon)=[1-\sqrt{2\varepsilon}]n+O(1).
```

**Converse.** Fix a seed. Write $`W`$ for the row space of $`A_R`$, with dimension $`r\leq B`$. Original parity being exact requires the all-ones row to belong to $`W`$. A memory cell is a uniform affine coset. Pair parity $`q=e_i+e_j`$ is determined by the memory and a raw read at $`k`$ precisely when $`q\in W+\mathrm{span}\{e_k\}`$. Otherwise it remains balanced after conditioning on both. This holds for every address, including a memory-dependent one. Each query is either recoverable exactly or has minimum error one half. Lemma R limits exactly recoverable pairs to $`\Phi_n(r)\leq\Phi_n(B)`$. Averaging over seeds proves the bound.

**Achievability.** Select an input-independent uniformly random subset of $`b`$ coordinates. Store their raw values and exact original parity, using $`b+1`$ bits. If either excluded coordinate is stored, read the other; if both are stored, no read is needed. If neither is stored, guess. For every fixed input and pair,

```math
\varepsilon_{n,b}=\frac{(n-b)(n-b-1)}{2n(n-1)}.
```

The least $`b`$ meeting the target gives the leading rate above. This need not be finite-length optimal; the $`O(1)`$ assertion fixes positive $`\varepsilon`$ first.

## 6. Explicit nonlinear separation

Use an odd block length $`k`$ dividing $`n`$. Store total parity and the majority bit of each block, using $`B=n/k+1`$ bits. Read $`X_i`$, estimate $`X_j`$ from its block majority, and output the revised parity. For uniform input the error for every fixed query is

```math
\delta_k=\frac12\left[1-\frac{\binom{k-1}{(k-1)/2}}{2^{k-1}}\right].
```

The other $`k-1`$ bits tie with the displayed binomial probability, in which case majority agrees with $`X_j`$. Otherwise their majority is independent of $`X_j`$ and is wrong half the time. This remains valid when both queried coordinates are in the same block; the decoder ignores the extra statistical use of its exact read.

For a worst-case fixed-input guarantee over public randomness, form majorities of $`Y=X\oplus R`$ with a uniform public mask and unmask the estimated bit. Retain $`p(X)`$ itself. For fixed $`X`$, $`Y`$ is uniform, so the same error holds. Physical storage of the mask is not charged, consistently with the shared-randomness model.

At $`k=7`$, error is $`11/32`$. At $`n=49`$, eight bits suffice. But

```math
\Phi_{49}(8)=364\lt \binom{49}{2}\frac5{16}=\frac{735}{2},
```

so every affine scheme needs at least nine bits. At $`n=1001`$, 144 nonlinear bits suffice while the affine converse requires at least 171. These are comparisons, not proofs of nonlinear optimality.

Majority coding and symmetrization are established random access coding ingredients. The distinction here concerns the encoding map: a majority map is nonlinear although its reconstruction codebook $`\{0^k,1^k\}`$ is linear. This does not refute exact-computation linearization conjectures. At zero error, Theorem E already has an affine optimum.

## 7. Known coding upper bound and open rate

A classical random access code permits estimation of any selected raw bit with error $`\varepsilon`$, using $`[1-h_2(\varepsilon)]n+O(\log n)`$ bits. This is credited to prior work, specifically Theorem 2 and antecedents in Doriguello and Montanaro; see the literature comparison. Add one exact parity bit, read $`X_i`$, and estimate $`X_j`$ using the code.

A direct covering argument also fits our model. Let $`V=\sum_{j=0}^{\lfloor\varepsilon n\rfloor}\binom nj`$. Sampling

```math
K=\left\lceil\frac{2^n}{V}(n\ln2+1)\right\rceil
```

uniform centers leaves expected uncovered points at most $`2^n\exp(-KV/2^n)\lt 1`$, so a covering exists. Encode by a nearest center. A public uniform mask and coordinate permutation distribute its at most $`\lfloor\varepsilon n\rfloor`$ reconstruction errors equally among fixed coordinates, for every fixed input. The center index plus parity has the claimed cost. This proves existence, not efficient encoding; no large cover has been implemented.

Consequently,

```math
1-\sqrt{h_2(\varepsilon)}
\leq\liminf_{n\to\infty}\frac{B_{\mathrm{all}}(n,\varepsilon)}n
\leq\limsup_{n\to\infty}\frac{B_{\mathrm{all}}(n,\varepsilon)}n
\leq\min\{1-h_2(\varepsilon),1-\sqrt{2\varepsilon}\}.
```

Existence of a limiting optimal rate is not asserted. The ratio of the entropy-rate upper coefficient to the converse coefficient is $`1+\sqrt{h_2(\varepsilon)}\leq2`$.

For success $`1/2+\gamma`$, first take large $`n`$ at fixed $`\gamma\gt 0`$, then small $`\gamma`$. The unrestricted memory rate is $`\Theta(\gamma^2)`$, up to the unresolved constant, whereas the optimal affine rate is $`\gamma+O(\gamma^2)`$. This is not a uniform finite-$`n`$ statement for arbitrarily vanishing advantage.

## 8. Evidence and remaining obligations

The unchanged source verifiers and recorded reports are traced in [SOURCE_MANIFEST.json](docs/SOURCE_MANIFEST.json). The [reproduction guide](docs/REPRODUCIBILITY.md) lists exact scopes and numerical tolerances. Finite checks support implementation correctness and help find counterexamples; they do not establish the general theorems or their novelty.

The next scientific obligations are theorem-level comparison with systematic/common-bits and random access coding literature, investigation of the unrestricted-rate gap, and assessment of whether the result is significant enough for a paper. Neither a novelty claim nor an AI-safety conclusion follows from successful repository validation.
