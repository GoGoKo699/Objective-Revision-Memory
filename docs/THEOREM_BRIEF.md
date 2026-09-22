# What the sharp pair-query theorem contributes

Internal research and contribution brief, 22 September 2026. Repository base:
`f1ecb10769f2b6ce0abe215d16f30767a02957d0`.
This is a theorem-led working formulation, not a manuscript release or a historical-priority certificate. The [research note](../RESEARCH_NOTE.md) supplies the full sharp-rate proof; the [literature comparison](LITERATURE_COMPARISON.md) identifies established ingredients and the remaining reduction questions.

**Precise priority question.** For a fixed one-read decoder strategy $t$,
let $D_n(x,t)$ be its fraction of wrong direct pair-parity answers. Addresses
may be arbitrary coordinates, but are fixed once the strategy and query are
specified. Set

$$m_n(\varepsilon)=\max_t2^{-n}|\{x:D_n(x,t)\le\varepsilon\}|.$$

The task-specific theorem is $m_n(\varepsilon)=2^{-n\mathcal R(\varepsilon)+o(n)}$
for fixed interior error; an ordered-endpoint strategy attains this exponent.
The [operational reduction](OPERATIONAL_REDUCTION.md) proves the statement from
the existing moment bound and weighted-ball volume. A memory label selects a
strategy, so arbitrary preprocessing and summary-dependent addresses are
included. Kostina–Verdú's general distortion theorems then supply the covering
and success-exponent conversion. Those consequences should be grouped under
one result, not counted as independent novelty claims.

The review question is whether a prior theorem evaluates this extremal ball,
or implies it through an explicit reduction preserving raw-coordinate probes,
charged summary bits, and error quantifiers. A separate significance question
is whether this canonical equality merits a focused short note. No efficient
encoder, new scalar coding law, or general objective-preservation principle is
being proposed.

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

This holds for every subset and every permitted address choice, including memory-dependent choices after conditioning. A bound on the rank of the complete query family alone would not suffice. The mechanism is established: fundamental-circuit uniqueness gives at most one completed basis pair per nonbasis coordinate. Equivalently, affine-basis pair sums are distinct. The [literature comparison](LITERATURE_COMPARISON.md) now supplies complete classical reductions, including the exact finite envelope. This is a task-specific elementary lemma, not a standalone geometric novelty claim.

For comparison, the sharp first-order converse would need only the weaker statement

$$|E|\le nr-r^2/2+o(n^2),$$

uniformly over ranks and residual families. Indeed, greedy threshold integration turns this into a bias-sum bound with an $o(n^2)$ additive remainder. The entropy-dual multiplier is $s=a/n$; after dividing memory by $n$, that remainder vanishes. The classical reductions now meet even the exact finite criterion. Priority assessment should therefore concern the operational characterization, rather than continue searching for novelty of this basis count.

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

Proceed with a lean internal candidate centered on the extremal decoder-ball evaluation and ordered-endpoint attainment. Present unrestricted versus publicly chosen endpoint access, covering, and the success exponent below as its operational consequences, with explicit attribution for general lossy coding as well as geometry and entropy. The affine separation and bipartite benchmark are context, not independent evidence of originality. The action-dependent coding comparison now has a worked indirect-source reduction, rather than just a list of model differences. Historical priority and significance remain unresolved; the audit does not establish submission readiness.

## 6. Stronger operational form: covers and the success exponent

Fix an input and all random tapes, and let $\Delta$ be the fraction of the $\binom n2$ pair queries the decoder would answer incorrectly, each considered separately from the same summary with its own one-read budget. Define $P_n^*(B,\varepsilon)$ as the largest probability, over uniform input and independent tapes, that $\Delta\le\varepsilon$. This optimization preserves the resource and exact-parity rules; the table criterion replaces the per-query error promise, rather than imposing it as an additional feasibility condition.

For fixed $0<\varepsilon<1/2$ and any integer sequence $B_n\ge1$ with $B_n/n\to\rho\ge0$, the [excess-distortion theorem](EXCESS_DISTORTION.md) proves

$$\lim_{n\to\infty}-\frac1n\log_2 P_n^*(B_n,\varepsilon)
=\bigl(\mathcal R(\varepsilon)-\rho\bigr)_+.$$

Deterministic ordered-endpoint schemes attain this exponent. Their reconstruction error has an exact weighted Hamming interpretation: estimate endpoint $j$ and read endpoint $i$ for $i<j$, so $N\Delta(x)=\sum_j(j-1)\mathbf1\{x_j\ne z_j\}$. Weighted balls have uniform-input probability $2^{-n\mathcal R(\varepsilon)+o(n)}$. Partial covers using $2^{B-1}$ centers charge $B-1$ index bits and one parity bit and attain the success exponent. The arbitrary-address converse follows from the existing exponential-moment inequality and a union bound over memory labels.

The rate $\mathcal R(\varepsilon)$ also suffices for a deterministic guarantee $\Delta(x)\le\varepsilon$ on **every** input. Block covers with a strict distortion margin prove this for all sufficiently large lengths. Public permutation and masking can then add the original fixed-input/fixed-pair marginal error guarantee while preserving the table-distortion bound for every input and seed.

These statements concern the fraction of incorrect pairs. They do not answer every pair with one total read, ensure every answer is correct, or protect against selecting an erroneous pair after seeing the seed. At the critical rate the success exponent is zero, which need not mean success probability tends to one. The optimal failure exponent above the rate is not claimed.
