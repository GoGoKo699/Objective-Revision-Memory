# What the sharp pair-query theorem contributes

Internal research and contribution brief, 22 September 2026. Repository base:
`b9394cd2ea64c45943e66ba7c61ae665f3df77c3`.
This is a theorem-led working formulation, not a manuscript release or a historical-priority certificate. The [research note](../RESEARCH_NOTE.md) supplies the full sharp-rate proof; the [literature comparison](LITERATURE_COMPARISON.md) identifies established ingredients and the remaining reduction questions.

## 1. Operational question and resource ledger

An encoder sees a uniformly distributed binary archive $X\in\{0,1\}^n$ before learning an unordered pair $\{i,j\}$. It retains at most $B$ input-dependent bits. Independent public randomness is free. The immutable raw archive remains available, but answering a later query permits at most one raw-coordinate bit read. The entire summary and unlimited computation are available. Raw-read addresses may depend on the summary, query, and seed. There are no free input-dependent caches or transcripts.

The summary must determine total parity $p(X)$ exactly; the query requests $p(X)\oplus X_i\oplus X_j$. For each fixed pair, error is at most $\varepsilon$, averaged over uniform input and randomness. The converse needs only input-and-pair average error. Public permutation and masking make the optimal memory sizes for these criteria equal to the optimum requiring the same error bound for every fixed input and pair, over the seed. This does not cover simultaneous correctness or a query chosen after seeing the summary and seed.

Let $B_{\rm arb}$ denote this optimum, $B_{\rm end}$ the optimum when reads must be query endpoints, and $B_{\rm public}$ the optimum when, additionally, the read address depends only on the query and public seed. No-read answers remain allowed.

**Operational equivalence.** For every fixed $0<\varepsilon<1/2$,

$$\lim_{n\to\infty}\frac{B_{\rm arb}(n,\varepsilon)}n
=\lim_{n\to\infty}\frac{B_{\rm end}(n,\varepsilon)}n
=\lim_{n\to\infty}\frac{B_{\rm public}(n,\varepsilon)}n
=\mathcal R(\varepsilon).$$

This follows from the unrestricted converse and the existing construction: publicly assign reconstruction qualities, estimate the better represented endpoint, and reread the other. Its address does not depend on the summary. All covering indices and one parity bit are charged.

The scalar rate is already a weighted binary coding optimum:

$$\mathcal R(\varepsilon)=\inf_{0\le\delta(u)\le1/2}
\left\{\int_0^1[1-h_2(\delta(u))]du:
\int_0^1 2u\delta(u)du\le\varepsilon\right\}.$$

The quality label $u$ is public to encoder and decoder in this comparison. With $\eta=1-2\varepsilon$, the optimizer is $\delta(u)=(1+e^{2au})^{-1}$, where $\eta=2\int_0^1u\tanh(au)du$. Martinian–Wornell–Zamir supply the finite-label coding antecedent; finite partitions give this expression. The candidate contribution is equality with the unrestricted one-read optimum, not a new coding curve or a finite simulation between arbitrary implementations.

## 2. The geometric input: an almost vertex cover

Fix a seed and memory cell. A Boolean function of one observed bit is affine. After using the known total parity, each query therefore has a signed residual character with nonzero row

$$a_{ij}=e_i+e_j+\beta_{ij}e_{k_{ij}},\qquad \beta_{ij}\in\{0,1\}.$$

Take any subset $E$ of pair labels whose selected rows span a rank-$r$ space $W$. Choose $n-r$ coordinate images forming a basis of $\mathbb F_2^n/W$, and let $C$ be the other $r$ coordinate positions. Every covered pair outside $C$ has two distinct basis images. Their sum must equal an image of a coordinate in $C$: neither a zero-read residual nor an endpoint correction can cancel them. Distinct basis pairs have distinct sums, so at most $r$ such pairs exist. Thus $C$ meets all but at most $r$ edges of $E$, and

$$|E|\le f_n(r)+r,\qquad
f_n(r)=\binom n2-\binom{n-r}{2}=nr-\frac{r(r+1)}2.$$

This holds for every subset and every permitted address choice, including memory-dependent choices after conditioning. A bound on the rank of the complete query family alone would not suffice.

The sharp first-order converse actually needs only the weaker statement

$$|E|\le nr-r^2/2+o(n^2),$$

uniformly over ranks and residual families. Indeed, greedy threshold integration turns this into a bias-sum bound with an $o(n^2)$ additive remainder. The entropy-dual multiplier is $s=a/n$; after dividing memory by $n$, that remainder vanishes. Consequently, any prior theorem implying this leading all-subsets profile would already supply the substantive geometric input. Priority comparisons must not require the precise lower-order term to match.

The [general envelope lemma](RANK_PROFILE_EXTENSIONS.md) organizes the next steps: greedy integration, the independent-character entropy budget from the entropic Chang argument, and scalar conjugacy. It is a reusable deduction, not a separate claim of a new entropy inequality or automatic achievability for every query family.

## 3. Endpoint geometry and its finite converse

For endpoint reads, residual rows belong to $\{e_i,e_j,e_i+e_j\}$. A pair wholly inside the quotient coordinate basis cannot be covered. Therefore the exact maximum geometric coverage is $f_n(r)$ for every $0\le r\le n$: the upper bound follows immediately, and the span of any $r$ coordinate rows attains it. This geometric attainment does not impose the mandatory-parity constraint on the subspace.

For completeness, let $t_1\ge\cdots\ge t_n\ge0$ be the biases of a greedy independent residual basis, padded with zeros, on a memory cell. Threshold integration and the increments $f_n(j)-f_n(j-1)=n-j$ give

$$\sum_{i<j}b_{ij}\le\sum_{j=1}^n(n-j)t_j.$$

Writing $c(t)=1-h_2((1-t)/2)$ and $D=n-H(X\mid m,R)$, entropy subadditivity in a completed linear basis gives $\sum_jc(t_j)\le D$. Apply $zt-\ln2\,c(t)\le\ln\cosh z$, then average cells and seeds using $\mathbb ED\le B$. The endpoint finite converse is

$$B\ln2\ge s\binom n2\eta-\sum_{k=1}^{n-1}\ln\cosh(sk),\qquad s\ge0.$$

The unrestricted displayed converse adds one subtractive term, $\ln\cosh(sn)$. At $s=a/n$ this is only $O(1)$, explaining why nonendpoint geometry cannot change the first-order rate. Comparing these lower bounds does **not** bound the difference between finite optimal memory sizes.

## 4. A finite separation at zero error

Endpoint-only zero-error memory is exactly

$$B_{\rm end}(n,0)=n-1.$$

To prove the lower bound, fix a seed that is correct on every input and pair. Such seeds have probability one under marginal zero-error guarantees, since inputs and pairs form finite sets. On a memory cell, consider two nonconstant coordinate functions $X_i,X_j$. If their XOR is determined without reading, they are equal or complementary. If it is decoded from $X_i$, then $X_j$ is a Boolean function of $X_i$; nonconstancy again forces equality or complementation. Reading $X_j$ gives the same conclusion. Hence every nonconstant coordinate is a fixed choice of one common bit or its complement. A cell has at most two inputs, so at least $2^{n-1}$ memory labels are needed.

For attainment, retain $X_3,\ldots,X_n$ and $X_1\oplus X_2$. These $n-1$ bits determine total parity. Pair $\{1,2\}$ and pairs among retained coordinates need no read; other pairs require reading their unretained endpoint.

The [baseline exact theorem](../BASELINE_NOTE.md) gives unrestricted optimum $n-\lfloor\log_2(n+1)\rfloor$. Nonendpoint reads therefore save exactly $\lfloor\log_2(n+1)\rfloor-1$ bits at zero error. Already $n=3$ gives one versus two bits. First-order equivalence is not finite equivalence, and the fixed-interior-error theorem supplies no uniform vanishing-error claim.

## 5. Scope and drafting decision

Let $B_{\rm pair}$ be the same access model asking directly for $X_i\oplus X_j$, without mandatory original parity. Then, at every finite $n$ and error allowance,

$$B_{\rm pair}\le B_{\rm arb}\le B_{\rm pair}+1.$$

The first inequality uses the retained exact parity to convert a revision answer to a pair-parity answer. The second stores one additional exact parity bit and converts in reverse. Error and read budgets are unchanged; the argument also applies to endpoint restrictions. Preserving the old objective therefore has no additional leading memory cost in this example.

Proceed with a lean research candidate centered on unrestricted versus publicly chosen endpoint access, its geometric explanation, and the finite zero-error counterpoint. Retain explicit attribution for the coding law and entropy machinery. The affine separation and bipartite benchmark are consequences and context, not independent evidence of originality. Historical priority remains unresolved; submission, a new-coding-law claim, and a general claim about objective preservation are not justified by the present audit.
