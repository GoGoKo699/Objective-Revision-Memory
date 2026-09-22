# Rank-profile continuation: general machinery and graph benchmarks

Research continuation, 22 September 2026. Base inspected:
`4e2c579795e2e780e132e3feb8072d2260ab3a7f`.

These are written deductions extending the [sharp-rate audit](reviews/SHARP_RATE_AUDIT.md), not a historical-priority claim. They separate generic entropy machinery from the pair-specific extremal problem, strengthen one finite converse, and identify graph families whose first-order answer follows from established ingredients. The [main theorem](../RESEARCH_NOTE.md) and its original verification artifacts are unchanged.

## 1. A general rank-envelope lemma

Let nonzero rows $`a_q\in\mathbb F_2^n`$ be indexed by a finite query set $`Q`$; repeated rows are allowed. Suppose a nondecreasing function $`g:\{0,\ldots,n\}\to\mathbb R_{\ge0}`$ satisfies $`g(0)=0`$ and, for every $`J\subseteq Q`$,

```math
|J|\le g\bigl(\mathrm{rank}\{a_q:q\in J\}\bigr).
```

Put $`w_j=g(j)-g(j-1)\ge0`$ and $`c(b)=1-h_2((1-b)/2)`$. For **every** distribution $`P`$ on the cube, writing $`D_P=n-H_P(X)`$ in bits,

```math
s\sum_{q\in Q}|\mathbb E_P(-1)^{a_q\cdot X}|
\le D_P\ln2+\sum_{j=1}^n\ln\cosh(sw_j),\qquad s\ge0.\qquad\text{(1)}
```

**Proof.** Sort rows by decreasing absolute bias and retain an independent row whenever possible. Let their biases be $`t_1\ge\cdots\ge t_d`$, padded with zeros. At any positive threshold $`z`$, the greedy rows above threshold span all rows above threshold. If their rank is $`r(z)`$, threshold integration gives

```math
\sum_q|\mathbb E_P(-1)^{a_q\cdot X}|
\le\int_0^1g(r(z))\,dz
=\sum_{j=1}^nw_jt_j.
```

Extend the retained rows to a binary basis. The invertible change of variables preserves entropy; subadditivity gives $`\sum_jc(t_j)\le D_P`$. Apply

```math
zb-\ln2\,c(b)\le\ln\cosh z
```

with $`z=sw_j`$ and sum. This proves (1), including distributions that are not uniform on a memory cell.

Monotonicity of $`g`$ suffices. Discrete concavity additionally makes $`w_1\ge\cdots\ge w_n`$, so the unconstrained maximizing biases $`t_j=\tanh(sw_j)`$ obey the greedy ordering. Without concavity, (1) remains valid, but independent scalar optimization can lose information about that ordering. Neither concavity nor the displayed optimizer guarantees that any encoder attains the bound.

The entropy budget is established: see Impagliazzo–Moore–Russell, [*An Entropic Proof of Chang's Inequality*, arXiv:1205.0263v2](https://arxiv.org/pdf/1205.0263v2), Eq. (1) and Section 2's basis transfer. The query-specific rank envelope supplies the separate geometric input.

### Equivalent exponential-moment formulation

For arbitrary signs $`\sigma_q\in\{-1,1\}`$, define $`S(x)=\sum_q\sigma_q(-1)^{a_q\cdot x}`$. Under uniform $`U`$ on the cube, (1) implies

```math
\ln\mathbb E_Ue^{sS(X)}\le\sum_j\ln\cosh(sw_j).\qquad\text{(2)}
```

Indeed, substitute the tilted distribution $`P_s(x)=U(x)e^{sS(x)}/Z`$ into (1). Its relative entropy is $`D(P_s\Vert U)=s\mathbb E_{P_s}S-\ln Z=D_{P_s}\ln2`$, and the signed expectation is at most the sum of absolute biases. Conversely, the usual entropy variational inequality applied to (2), with each sign chosen to match its bias under $`P`$, recovers (1).

This duality is standard; for a primary general-measure-space formulation see Carlen–Cordero-Erausquin, [*Subadditivity of the Entropy and its Relation to Brascamp–Lieb Type Inequalities*](https://webusers.imj-prg.fr/~dario.cordero/Docs/articles/subaddOCT1.pdf), October 2007 manuscript, Eq. (2.4) and the proof of Theorem 2.1. No separate novelty claim is made for the Gibbs conversion.

For a fixed public seed and memory label $`m`$, each one-read Boolean decoder, after removing the exactly known original parity, has a signed residual character. If every such decoder family has the same envelope, let $`S_m`$ be its signed correctness score. There are at most $`2^B`$ memory labels, so

```math
\mathbb E_U e^{sS_{M(X)}(X)}
\le\sum_m\mathbb E_Ue^{sS_m(X)}
\le2^B\exp\!\left(\sum_j\ln\cosh(sw_j)\right).
```

Averaging independent seeds and applying Jensen yields the memory converse. This permits memory-dependent addresses and arbitrary preprocessing. It expresses the argument as a bound on fixed decoder families followed by a union bound over help labels; it is not an additional stronger theorem.

## 2. A capped finite converse for all pairs

For $`N=\binom n2`$, the existing coverage lemma and the trivial pair count together permit the concave envelope

```math
g(r)=\min\{N,\Phi_n(r)\},\qquad
\Phi_n(r)=nr-r(r-1)/2.
```

Let $`\rho`$ be the least integer with $`\Phi_n(\rho)\ge N`$, equivalently

```math
\rho=\left\lceil\frac{2n+1-\sqrt{8n+1}}2\right\rceil.
```

Its positive increments are

```math
w_j=n-j+1\quad(1\le j\lt \rho),\qquad
w_\rho=N-\Phi_n(\rho-1),
```

and all later increments vanish. Therefore any scheme in the original model with average pair bias at least $`\eta=1-2\varepsilon`$ satisfies

```math
B\ln2\ge sN\eta-\sum_{j=1}^{\rho}\ln\cosh(sw_j),\qquad s\ge0.\qquad\text{(3)}
```

This strengthens the displayed finite inequality in the main note: it only reduces or deletes its nonnegative $`\ln\cosh`$ terms. It changes neither resource accounting nor error quantifiers. In particular, the converse still needs only average error over uniform inputs and uniform pairs; exact total parity remains part of the charged summary. It is not asserted to be finite-length optimal. At zero error, taking $`s\to\infty`$ gives $`B\ge\rho`$, still weaker in general than the separate exact theorem. At fixed interior error it leaves the existing sharp first-order rate unchanged.

## 3. Exact pair coverage at low rank

There is a sharper geometric statement in a restricted rank range. If $`W\subseteq\mathbb F_2^n`$ has dimension $`r`$ and $`n\ge2r+2`$, the maximum number of pairs admitting

```math
e_i+e_j+\beta e_k\in W,\qquad\beta\in\{0,1\},
```

is exactly

```math
nr-\frac{r(r+1)}2=N-\binom{n-r}{2}.\qquad\text{(4)}
```

**Upper bound.** Set $`d=n-r`$ and choose coordinate images indexed by $`I`$ that form a basis of $`\mathbb F_2^n/W`$. There are $`r`$ remaining coordinate positions. Each recoverable pair wholly in $`I`$ has a distinct sum of two basis vectors, which must equal the image of an outside coordinate. Choose one such witness coordinate for each pair; the witnesses are distinct.

For a witness with image $`v=e_i+e_j`$ in this quotient basis, consider its pairs with the $`d-2`$ basis coordinates other than $`i,j`$. Their quotient sums are the distinct weight-three vectors $`v+e_k`$. None is zero or a basis image. Nor can one equal the witness's own image. At most $`r-1`$ other outside coordinate images are available. Since $`d\ge r+2`$, at least one of these cross pairs is unrecoverable. Different witnesses produce different missing cross pairs.

Thus every recoverable pair inside $`I`$ is offset by a missing pair having an endpoint outside $`I`$. There are $`N-\binom d2`$ pairs of the latter kind in total, proving the upper bound.

**Attainment.** Take $`W`$ to be the span of $`r`$ coordinate rows. Every pair touching those coordinates is recoverable by using its stored endpoint as the residual and rereading the other endpoint. There are exactly the number in (4). For $`r\gt 0`$ these selected residuals can span all of $`W`$; $`r=0`$ is immediate.

This is an exact extremal statement about the residual-row geometry, not the optimal memory in the mandatory-parity model: the attaining subspace need not contain total parity. A global extension is false: at $`n=7,r=4`$, the kernel of the matrix with all seven nonzero three-bit columns covers all 21 pairs, whereas (4) would allow only 18. Combining improved low-rank values with other bounds can create nonconcave increments, so unconstrained scalar optimization need not give a stronger final bound. Retaining the bias ordering or choosing a concave majorant avoids that issue. No unrestricted full-rank formula follows from (4).

The optional [exact check](../checks/reviews/verify_low_rank_coverage.py) independently enumerates all 3,559 subspaces in the stated rank range for $`n=3,\ldots,7`$, checks attainment, and verifies that counterexample. It supports the proof without establishing the general statement by enumeration.

**Prior-theorem reduction, added in the priority audit.** Matching residuals are independent, so any such covered-pair graph has matching number at most $`r`$. Erdős–Gallai's [1959 Theorem (4.1)](https://www.renyi.hu/~p_erdos/1959-10.pdf), printed p.354, therefore gives, when $`n\ge2r+1`$,

```math
|E|\le\max\left\{\binom{2r+1}{2},\ nr-\frac{r(r+1)}2\right\}.
```

For $`r\gt 0`$ and $`n\ge(5r+3)/2`$, its second term dominates, recovering the exact formula (4) by an elementary classical reduction. The proof above extends to the larger range $`n\ge2r+2`$. This difference does not certify its historical priority. The matching bound alone is too weak at other linear ranks to supply the full leading profile; see the [audit](reviews/SHARP_RATE_AUDIT.md).

## 4. Matching converse and bipartite sharp rate

Let a graph $`G`$ specify the allowed pair queries, and let $`\nu(G)`$ and $`\tau(G)`$ denote its maximum matching and minimum vertex-cover sizes. Write $`B_G`$ for minimum memory with error at most $`\varepsilon`$ for each fixed allowed edge, averaged over uniform input and independent randomness. The archive, parity requirement, one-bit read, and charged memory are unchanged.

For any matching of size $`k`$, **every** choice of one-read residual rows is independent. A sum over $`j`$ matching edges starts with Hamming weight $`2j`$; adding at most $`j`$ coordinate rows cannot make it zero. Consequently, for a fixed memory label and seed, the signed residual characters for the matching are independent unbiased signs under uniform $`X`$. Their exponential moment is exactly $`(\cosh s)^k`$.

The memory-label argument above gives

```math
B\ln2\ge sk\eta-k\ln\cosh s.
```

Optimizing $`s\ge0`$ yields

```math
B\ge k[1-h_2(\varepsilon)]\qquad\text{(5)}
```

whenever that matching's average error is at most $`\varepsilon`$. Error need not be uniform within its memory cells or across its edges. This supplies a complete elementary proof of the matching corollary attributed to Nisan–Rudich–Saks in the [audit](reviews/SHARP_RATE_AUDIT.md#52-a-genuine-nisanrudichsaks-lower-bound-corollary); no new direct-product principle is claimed.

If **each fixed allowed edge** has input-and-seed-average error at most $`\varepsilon`$, apply (5) to a maximum matching. Conversely, cover all edges by a minimum vertex cover $`C`$. Encode its $`\tau(G)`$ raw bits with an ordinary covering-based random access code, and retain exact original parity. For each query, estimate a deterministically chosen endpoint in $`C`$ and reread the other endpoint. The masking/permutation construction in the [main note](../RESEARCH_NOTE.md#41-an-ordinary-covering-ingredient-credited-to-prior-coding-theory), now applied only within $`C`$, gives the stronger guarantee for every fixed input and fixed allowed edge over the independent seed. For fixed $`0\lt \varepsilon\lt 1/2`$,

```math
\nu(G)[1-h_2(\varepsilon)]\le B_G
\le\tau(G)[1-h_2(\varepsilon)]+O_\varepsilon(\log(\tau(G)+1))+1.\qquad\text{(6)}
```

All index bits and the parity bit are charged; time and public randomness are uncharged. The upper bound is existence-based. For bipartite graphs, the established matching–cover equality gives $`\nu=\tau`$. Hence along any bipartite graph sequence with $`\nu(G)\to\infty`$,

```math
\frac{B_G}{\nu(G)}\longrightarrow1-h_2(\varepsilon).\qquad\text{(7)}
```

### Edge-average error requires a separate condition

For complete bipartite graphs, averaging uniformly chosen maximum matchings makes every edge equally represented. Therefore some matching has error no larger than the graph's uniform edge-average error, and (5) proves the same rate under that weaker criterion. This reasoning also applies whenever a distribution on maximum matchings has equal edge marginals, including regular bipartite graphs.

It fails for arbitrary bipartite graphs. Take a star with $`k^2`$ edges disjoint from $`k`$ isolated edges. Retaining the star center and total parity uses two bits, answers all star queries exactly, and allows random guesses on the isolated edges. Uniform edge-average error is only $`k/[2(k^2+k)]`$, while $`\nu=k+1`$. Thus no growing lower bound proportional to $`\nu`$ holds at fixed positive edge-average error for all such graphs. Arbitrary vertex permutations need not preserve the allowed query set.

## 5. Research interpretation

The general entropy budget, binary conjugacy, coding ingredient, and matching–cover theorem are established. The generic envelope deduction, cap refinement, low-rank geometry, and graph corollary are proved above; their historical priority is unresolved. In particular, many overlapping-query families already reduce sharply to ordinary coding. The remaining candidate contribution of the all-pairs theorem is its specific residual-rank profile and its sharp operational match for unrestricted summaries and memory-dependent probes, not overlap or the hyperbolic-tangent formula alone.
