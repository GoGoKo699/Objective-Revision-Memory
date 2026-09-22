# Sharp unrestricted rate: proof and novelty audit

Session: 22 September 2026. Reviewed `main` commit:
`761950c4960e88269d168e68106ebea0f44d75b9`.
Its mathematical content is the checkpoint
`cbdcd0fc109c39ee5b5d53c58668695c0f785cbb`; the intervening commit adds the review brief.
Review branch: `review/sharp-rate-audit`.

**Continuation recorded below in Section 8:** reviewed merged audit commit `4e2c579795e2e780e132e3feb8072d2260ab3a7f`, on branch `research/rank-profile-foundations`. The user subsequently authorized merging; PR #3 was merged after its successful verification workflow. Sections 1-7 retain the initial audit's historical scope and handoff. Section 8 supersedes their next-action and no-merge instructions for this session.

**Latest priority decision in Section 9:** reviewed `b9394cd2ea64c45943e66ba7c61ae665f3df77c3` (merged PR #4), on `review/priority-decision`. It records a classical partial subsumption, new endpoint-access comparisons, and a compact theorem brief. Its next action supersedes the earlier research queues; historical novelty remains unresolved.

**Current continuation in Section 10:** reviewed `0e91f088cd06376458f63a20f76e2d5b507a690a` (merged PR #5), on `research/excess-distortion`. Complete classical geometric reductions supersede the earlier unresolved-geometric-priority target. A new operational deduction gives the sharp success exponent and deterministic worst-input table covers. Priority of that operational synthesis remains unresolved.

## 1. Assessment and scope

**The stated fixed-error first-order theorem survives this audit. No central mathematical defect or counterexample was found. Historical novelty is not established.** The most consequential novelty finding is that the scalar optimization, including the hyperbolic-tangent quality profile, is an explicit specialization of established weighted binary rate-distortion coding. The potentially distinctive result is equality of the full adaptive-address pair-query problem's optimal first-order rate with that coding rate, proved through the all-pairs residual-rank profile. Neither a new coding law nor the broad observation that nonlinear lossy encoders can outperform affine encoders is a defensible contribution by itself.

This report reconstructs the proof rather than relying on prior conclusions, issue closure, or passing tests. Parallel mathematical checks were reconciled with the primary review; their agreement is not independent human expert review or formal certification. No manuscript or publication-readiness claim follows.

Inspected: the current research note, status, literature comparison, reproducibility guide, baseline note and literature baseline, verification code and reports, source manifest, review brief, and issues [#1](https://github.com/GoGoKo699/Objective-Revision-Memory/issues/1) and [#2](https://github.com/GoGoKo699/Objective-Revision-Memory/issues/2), including their empty comment threads. At branch selection only `main` existed, issue #1 was open, issue #2 was closed, and no pull requests were open. The conjunction model was reproduced as required but supplies no ingredient to this parity audit.

The report adds three useful deductions: a finite-length equivalence between the stated error models; a weaker unrestricted converse obtained from the original Nisan–Rudich–Saks theorem; and a specific obstruction to direct vector batching under the cited query-with-sketch lemma. These are derived below, not attributed as statements of those papers.

## 2. Reconstructed model

For uniform $X\in\{0,1\}^n$, independent seed $R$, and fixed-length summary $M=f_R(X)$ with at most $2^B$ values, total parity must be recovered exactly from $(M,R)$. A later pair asks for $p(X)\oplus X_i\oplus X_j$. The decoder sees the entire summary, chooses an arbitrary address from $(M,R,i,j)$, and reads at most one **raw bit**. It may also use no read. Computation is unrestricted. The immutable archive is uncharged; retained input-dependent indices, caches, and transcripts are charged. Independent random tapes and code descriptions are uncharged.

The converse uses input-and-pair average error; the definition of $B_{\rm all}$ requires input-average error for each fixed pair; the construction guarantees seed-average error for each fixed input and pair. None is simultaneous success on all pairs or robustness against queries chosen after the seed/summary is observed. Fix $0<\varepsilon<1/2$ before taking $n\to\infty$, and put $\eta=1-2\varepsilon$.

### A finite-length clarification

In fact, the three optimal memory sizes coincide at every finite $n$ under the allowed public randomness. Given any input-and-pair-average scheme, choose an independent uniform permutation $\Pi$ and mask $Z$ and feed the old encoder

$$Y_a=X_{\Pi(a)}\oplus Z_a.$$

Map the requested pair to $\{a,b\}=\{\Pi^{-1}(i),\Pi^{-1}(j)\}$. Simulate a read of $Y_k$ by one read of $X_{\Pi(k)}$ and XOR with $Z_k$. Correct the revised answer by $p(Z)\oplus Z_a\oplus Z_b$ and the original-parity answer by $p(Z)$. No extra input-dependent bit is stored. For every fixed $X,i,j$, $Y$ is uniform independently of the mapped uniform pair. The resulting error equals the old input-and-pair average. The reverse inclusions are immediate. This also preserves affine encoders for each seed.

The note's first-order equality is therefore valid but weaker than this standard symmetrization deduction. This is a suggested clarification, not a repair needed by Theorem S.

## 3. Lemma-by-lemma proof assessment

| Step | Assessment | Main issue resolved |
| --- | --- | --- |
| One-read Boolean reduction | Valid | Includes constants, endpoint cancellation, and memory-dependent nonendpoint addresses. |
| Pair-rank coverage | Valid | Counts pair labels, including duplicate residual rows, and applies to every subset. |
| Greedy bias profile | Valid | Threshold-span property gives coefficients $n,n-1,\ldots,1$. |
| Conditional entropy budget | Valid | Uses subadditivity, not independence or affine memory cells. |
| Finite conjugate bound | Valid | Constants and logarithm bases agree. |
| Limiting maximizer | Valid | Unique positive parameter for each fixed interior error. |
| Covering and seeded decoder | Valid | Nonuniform coordinate errors and same-block ties are handled. |
| All-length achievability | Valid | Fixed number of quality levels precedes the large-length limit. |
| Exact/affine baseline dependencies | Valid on inspection | Needed for comparisons, not for the unrestricted rate proof. |

### 3.1 One-read reduction and rank coverage

Condition on complete independent random tapes and a nonempty memory cell. The address is now fixed for each query. A Boolean function of one observed bit is constant, that bit, or its complement. Since total parity is known, the best conditional pair error is

$$\frac{1-b_{ij}}2,\qquad
b_{ij}=\max_{\beta\in\{0,1\},k}\left|\mathbb E[(-1)^{(e_i+e_j+\beta e_k)\cdot X}\mid m,R]\right|.$$

Cellwise optimization cannot worsen average error; no claim of uniform cellwise accuracy is required. Every residual row is nonzero, even when $k$ is an endpoint.

For any selected subset of pair-labelled residuals spanning $W$ of dimension $r$, choose $n-r$ coordinate images forming a quotient basis in $\mathbb F_2^n/W$. At most $N-\binom{n-r}{2}$ pairs touch its complement. A covered pair wholly inside the basis must sum to the image of an outside coordinate; it cannot sum to zero or to a basis vector. Different basis pairs have different sums, so at most $r$ such pairs occur. Therefore

$$|E|\le N-\binom{n-r}{2}+r=nr-r(r-1)/2=\Phi_n(r).$$

This does not assume distinct residual vectors. It is an upper bound, not a finite extremal formula: for $n=7$, the maximum actual counts by rank $0,\ldots,7$ are $0,6,11,15,21,21,21,21$, whereas $\Phi_7$ gives $0,7,13,18,22,25,27,28$.

### 3.2 Profile and information accounting

Sort by bias and greedily retain independent rows with biases $t_1\ge\cdots\ge t_d$, padded by zeros. At each positive threshold $z$, the retained rows above threshold span every row above threshold. Thus, with $q(z)$ counting labels and $r(z)$ their rank,

$$\sum b_{ij}=\int_0^1q(z)\,dz
\le\int_0^1\Phi_n(r(z))\,dz
=\sum_{\ell=1}^n(n-\ell+1)t_\ell.$$

Ties affect only irrelevant threshold endpoints. Extend the retained independent rows to a basis. Entropy invariance and subadditivity give

$$\sum_\ell c(t_\ell)\le D:=n-H(X\mid m,R).$$

This holds for arbitrary conditional distributions, without independence of the transformed coordinates. On averaging, $\mathbb ED=I(X;M\mid R)\le B$. Revealing independent private tapes for the converse is legitimate; fixing a particular cell does not license replacing the conditional input law by an independent product law.

### 3.3 Conjugacy and limit

Differentiating $\ln2\,c(b)$ gives $\operatorname{atanh}b$, so

$$zb-\ln2\,c(b)\le\ln\cosh z$$

with equality at $b=\tanh z$. Apply this at $z=s(n-\ell+1)$ and average the previous bounds. Average optimal bias is at least $N\eta$, proving exactly

$$B\ln2\ge sN\eta-\sum_{k=1}^n\ln\cosh(sk).$$

Set $s=a/n$. The limiting objective has derivative $\eta/2-\int_0^1u\tanh(au)du$ and strictly negative second derivative. The derivative decreases from $\eta/2$ to $(\eta-1)/2$, giving a unique positive maximizer. Integration by parts yields the note's two equivalent rate expressions. This is a liminf argument at fixed $a$; it does not exchange an $n$-dependent optimization with the limit.

### 3.4 Covering and the seed argument

For $K\ge(m+1)2^m/V$, the expected number of uncovered words is at most $\exp(m\ln2-m-1)<1$. A covering multiset exists; removing duplicates cannot hurt. The trivial whole-cube cover handles the other branch of the minimum. Index lengths are worst-case fixed lengths. Existence says nothing about efficient encoding.

For fixed original $x,i,j$, the mask makes $Y=x\circ\Pi\oplus R$ uniform and independent of $\Pi$. Let $A(\Pi)$ be the reconstructed endpoint's position. Conditional on its quality block $\ell$, $A$ is uniform within that block: internal permutations preserve block membership and the tie rule based on original labels. Independence from $Y$ gives

$$\Pr(\text{error}\mid\ell)
=\mathbb E_Y[d_H(Y_\ell,\widehat Y_\ell)/m_\ell]
\le r_\ell/m_\ell.$$

The block-selection weights are exactly the differences of binomial coefficients stated in the note. No independent reconstruction-error hypothesis is hidden here. The decoder uses one original raw bit, public unmasking, and the stored original parity.

### 3.5 Order of limits and consequences

Given any rate tolerance $\tau>0$, first choose $a'>a$ close enough to keep the extra integral cost below $\tau/3$, while creating positive bias slack. Choose a sufficiently fine fixed $L$ preserving that slack and approximating cost within $\tau/3$. Finally choose $n_0$ such that every $n\ge n_0$ permits nearly equal blocks, preserves the slack, and has rounding/covering overhead below $\tau/3$. This proves the full limsup, rather than a divisibility subsequence.

Strict convexity makes $\tanh(au)$ the unique minimizing profile almost everywhere. Constant bias and the affine zero/one step profile meet the constraint but differ from it on positive measure, proving both strict comparisons. The expansion $a=3\gamma+O(\gamma^3)$ gives $3\gamma^2/(2\ln2)+O(\gamma^4)$ with the stated order of limits. No uniform vanishing-error or vanishing-advantage result has been proved.

The baseline exact proof's coordinate-function classes are XOR-closed modulo constants and injectively distinguish cell inputs. Its simplex construction preserves parity because its dimension is at least two. For affine summaries, conditional distributions are uniform cosets, and every pair after any particular read is either known or balanced. This verifies the dependencies behind the exact optimum and affine comparison without treating their verifiers as proofs.

## 4. Primary-source comparison ledger

Locations below belong to the versions explicitly identified, not automatically to later publications. Sources were inspected for the stated comparisons, not comprehensively re-proved.

### 4.1 Systematic structures and partial matrices

**Ramamoorthy–Rashtchian, ITCS 2020 proceedings**, [primary PDF](https://drops.dagstuhl.de/storage/00lipics/lipics-vol151-itcs2020/LIPIcs.ITCS.2020.35/LIPIcs.ITCS.2020.35.pdf), Sections 1.1–1.3 and Theorem 1, pp.35:4–35:5. Exact worst-case linear queries, linear retained bits, free index access, and charged raw probes are related to rigidity. Section 1.3 describes arbitrary preprocessing. The theorem gives the established subspace-distance characterization; it does not state a bounded-error nonlinear rate. Its model definition is unnumbered in this proceedings PDF; use version-specific locations rather than transplanting “Definition 2” from another version. A reduction still needs the all-weight-two coverage count and its conditional bias extension.

**Jukna–Schnitger, _Min-Rank Conjecture for Log-Depth Circuits_, [arXiv:1005.1009v1](https://arxiv.org/html/1005.1009v1)**, Remark 1.4 and Lemma 2.3. Exact depth-two circuits have arbitrary common bits and fixed direct input/output wiring. With at most one star per partial-matrix row, every allowed one-variable Boolean function is affine, giving $\mathrm{opt}(A)\le2^{n-\mathrm{mr}(A)}$. Conditioning on common bits and bounding cell size is already present. Applying this observation separately to memory-dependent addresses is a straightforward deduction. The nonzero-error profile and pair count are not supplied by these statements. Therefore the local one-read-to-affine observation is established machinery, not a new lemma in substance.

**Ko, _Efficient Linearization Implies the Multiphase Conjecture_, [ECCC TR22-122 PDF](https://eccc.weizmann.ac.il/report/2022/122/download)**, Lemma 3.3 and Corollary 3.4, p.8. Exact adaptive probing of linear stored functions forces a requested row into the span of the rows read. Probes to the hint are charged there. This supports established affine geometry; it neither linearizes arbitrary lossy encoders nor grants a sharp free-index one-probe bound.

**Ko, _Lower Bounds for Linear Operators_, [arXiv:2509.02730v1 HTML](https://arxiv.org/html/2509.02730v1)**, Theorem 1.3 and Protocol 1. This is an existence theorem for hard linear query sets in the cell-probe model, with charged accesses to an arbitrary stored representation and exact answers in the stated protocol. It does not identify the explicit all-pairs query set as hard. Simulating a freely visible $B$-bit summary there can require $B$ additional bit probes; setting its probe parameter to one would be invalid. Its circuit extensions also discuss advantage, so do not describe the entire paper as zero-error only.

### 4.2 Original help-bit theorems

**Nisan–Rudich–Saks, _Products and Help Bits in Decision Trees_**, [author-hosted PostScript](https://www.cs.cmu.edu/~rudich/papers/helpbits.ps), undated 12-page manuscript. Theorem 3.1, printed p.4, is a direct-product theorem for disjoint variable blocks, product input distributions, and separate depth bounds; each tree may probe other blocks. Section 4 permits arbitrary input-dependent help and help-dependent forests, including nonlocal reads. Theorem 4.1, p.7, characterizes the eventual depth with $k-1$ help bits for $k$ exact copies through sign-degree. Lemma 4.1, pp.7–8, bounds forest-cover counts by powers of single-instance success. Thus help-dependent nonlocal access and probabilistic covering are already present. The next section gives an actual weaker converse reduction; overlapping pairs require an additional argument.

The original manuscript was downloaded, converted, and read; its PostScript SHA-256 is `1680065b3d540c47bc2322a41cabe4605e15c41ef4888ca62f40ee9418945ed0`. The [SIAM endpoint](https://epubs.siam.org/doi/pdf/10.1137/S0097539795282444) did not provide full journal text. Journal identity: volume 28(3), pp.1035–1050, DOI `10.1137/S0097539795282444`. The theorem numbers above belong to the retrieved author manuscript. Journal-version equivalence remains unchecked.

**Beigi–Etesami–Gohari, [arXiv:1408.0499v1](https://arxiv.org/html/1408.0499v1)**, Theorems 6–7. Theorem 6 concerns $k=O(\log n)$ language instances known before help, polynomial-time decoding, and a fraction of correct answers; its part (ii) provides a whole-cube covering near rate $1-h_2(\alpha)$. Theorem 7 concerns i.i.d. instances, exact joint decoding, entropy-limited help with polynomial alphabet, and unassisted computational predictability. Raw input access is not limited to one bit. For two-bit parity an unassisted polynomial algorithm already exists, so those hardness implications give no memory converse here. Covering and entropy-rate help are established ingredients. These are arXiv theorem numbers; the journal version was not substituted.

### 4.3 RACs and affine encoders

**Doriguello–Montanaro, _Quantum Random Access Codes for Boolean Functions_, Quantum 5,402 (2021)**, [official PDF](https://quantum-journal.org/papers/q-2021-03-07-402/pdf/), Theorem 2, Definitions 6–7. Theorem 2 states a **private-randomness** classical RAC with $m\le[1-h_2(p)]n+7\log_2n$, crediting its reference [4], Theorem 2.2. It guarantees each fixed input/coordinate. Revealing the coins makes this usable here; add one parity bit and one endpoint read. Thus the repository's shared-randomness description is a valid consequence but should distinguish the literal statement. Function-RAC decoders receive the message and coins, with no subsequent raw read. Block coding and public symmetrization are established, and no-probe converses cannot be transferred unchanged.

**Pereira Alves–Gigena–Kaniewski, _Biased Random Access Codes_, [arXiv:2302.08494v3](https://arxiv.org/html/2302.08494v3)**, Section II, Eq.(3), Lemma 1. The objective weights input/query success; its classical optimum admits deterministic strategies, and Lemma 1 optimizes one map while fixing the other. Message alphabet size is charged; there is no raw-archive read. This validates nonuniform reconstruction priorities as prior machinery but does not derive weights from uniform external pair queries or solve the adaptive-read problem.

**Kondo et al., _Random Access Codes: Explicit Constructions, Optimality, and Classical–Quantum Gaps_, [arXiv:2604.21274v3 PDF](https://arxiv.org/pdf/2604.21274v3)**, Theorems 5 and 14, Section III-C. The setup excludes shared randomness. Theorem 5 characterizes input-and-coordinate-average RAC success by representatives minimizing average Hamming distance; Theorem 14 uses convex hulls of reconstruction points for worst-case success. Neither permits a raw read. Linear reconstruction codebooks in their constructions do not require affine encoding maps: nearest-center majority encoding is nonlinear even for the repetition codebook. Their unrestricted no-probe optimization is relevant coding background, not a theorem about this affine/nonlinear separation. The full versioned PDF was downloaded and inspected despite web-reader errors.

**Wu, _Entropy of Bernoulli Measures Conditioned on Affine Subspaces and a Problem of Ancheta–Massey_, [arXiv:2608.22837v1](https://arxiv.org/abs/2608.22837v1)**, Theorem 1 and Introduction. Theorem 1 studies linear compression of an i.i.d. Bernoulli source with unrestricted decoding and whole-vector expected Hamming error, without raw probes. The introduction credits Ancheta's fair-bit linear-encoder tradeoff $D\ge(1-R)/2$ and distinguishes linear encoders from linear codebooks. This is a direct warning against claiming generic affine inferiority as new. The older Ancheta/Massey originals were not inspected; historical attribution to them here is explicitly through Wu's primary discussion, not a completed original-source audit.

### 4.4 Weighted coding and decoder actions

**Martinian–Wornell–Zamir, _Source Coding With Distortion Side Information_, IEEE TIT 54(10),4638–4665 (2008)**, [author-hosted journal PDF](https://sia.mit.edu/wp-content/uploads/2015/04/2008-martinian-wornell-zamir-it.pdf), Theorems 2–3, Section IV-E Eqs.(40)–(41), Appendix II. A fair binary memoryless source has independent distortion weights; the index rate is paid and weighted whole-vector distortion is constrained. The optimum crossover for weight $\beta$ is $1/(1+2^{\lambda\beta})$, with rate averaging $1-h_2(\delta)$. The journal equations on p.4646 were visually checked. The [preprint cs/0412112v1](https://arxiv.org/pdf/cs/0412112v1), titled _Source Coding With Encoder Side Information_, was also read: Section IV-B1 Eqs.(14)–(16), Appendix B Eq.(56). It has different numbering. The scalar reduction below is exact; a late-query, one-read operational reduction is not supplied by this paper.

**Permuter–Weissman, _Source Coding with a Side Information “Vending Machine”_, [arXiv:0904.2311v2](https://arxiv.org/pdf/0904.2311)**, Section II-A and Theorem 1, Eqs.(4)–(7). An index selected from an i.i.d. source block determines a sequence of actions; a memoryless channel then produces side information. The rate is $\min[I(X;A)+I(X;U\mid Y,A)]$, under additive distortion and action cost constraints. This establishes message-dependent observation acquisition. It does not directly handle one late overlapping-pair request with a hard per-query one-bit read. Treating an entire archive as a source symbol changes the asymptotic block parameter and permits coding across archives; a resource-preserving single-archive reduction is still needed.

## 5. Explicit reductions and non-reductions

### 5.1 The scalar profile is established weighted rate-distortion

Specialize the weighted binary problem to public quality labels $u$ of uniform frequency on $[0,1]$, weight $\beta(u)=2u$, and no additive offset. Finite equally spaced labels suffice before taking a limit. Its optimization is

$$\min_{\delta(\cdot)}\int_0^1[1-h_2(\delta(u))]du,
\qquad \int_0^1 2u\delta(u)du\le\varepsilon.$$

With $a=\lambda\ln2$, its known allocation is

$$\delta(u)=\frac1{1+e^{2au}},\qquad 1-2\delta(u)=\tanh(au).$$

Since $\int_0^1 2u\,du=1$, its constraint becomes the note's parameter equation and its rate becomes exactly $\mathcal R(\varepsilon)$. This identifies the same scalar law, not merely similar terminology. It does **not** assume that an arbitrary one-read scheme reconstructs coordinates independently: establishing the lower bound for all such schemes is precisely the remaining substantive content of the repository argument. The triangular weights arise from pair coverage in the converse and from selecting the stronger endpoint in the construction. The finite covering construction additionally provides the required fixed-input guarantee.

### 5.2 A genuine Nisan–Rudich–Saks lower-bound corollary

Take a matching of $k=\lfloor n/2\rfloor$ pairs. For fixed seed and each possible memory value $m$, XOR the stored-parity answer into the revision decoder to obtain depth-one trees predicting those disjoint two-bit parities. Extend each tree to the whole cube, including inputs outside its memory cell. NRS Theorem 3.1 gives, for every subset $J$ of these trees,

$$\Pr(\text{all }J\text{ predictions correct})\le2^{-|J|}.$$

Other coordinates can be fixed and averaged; nonlocal reads remain allowed. If $K_m$ counts correct predictions, expansion of the exponential moment yields

$$\mathbb E e^{tK_m}\le[(1+e^t)/2]^k.$$

Sum over at most $2^B$ memory values and use Jensen, then average seeds:

$$t\mathbb E K_M\le B\ln2+k\ln[(1+e^t)/2].$$

With $\mathbb E K_M\ge k(1-\varepsilon)$, optimizing $t>0$ gives

$$B\ge\lfloor n/2\rfloor[1-h_2(\varepsilon)].$$

For pair-average correctness choose a matching with at least the average success by averaging random matchings. This charges no additional stored bits or probes and is a genuine extensive unrestricted converse from prior machinery, weaker than the sharp curve. For example its limiting coefficient at error $1/10$ is about $0.2655$, versus $0.4221$ in Theorem S.

Applying the product theorem directly to all pairs fails: pair parities share variables and satisfy triangle identities. Duplicating shared input bits destroys the required product distribution. Reparameterizing by independent edge parities changes original-coordinate reads into functions of multiple bits. None of this excludes a more elaborate reduction.

### 5.3 Direct query-with-sketch batching has a second obstruction

**Garg–He–Li–Papakonstantinou–Yang, [arXiv:2609.18024v1](https://arxiv.org/html/2609.18024v1)**, Definitions 2.1–2.4 and Lemma 2.5, permits arbitrary sketches and adaptive raw probes. The lemma requires success at least $0.99$, expected probe cost at most $0.1q$, and conditional joint output min-entropy above $2r$ for every partial assignment of length at most $q$, allowing specified good-set exclusions. This is a vector-output result, not a scalar entropy-rate theorem.

Here is a stronger obstruction than checking only one Boolean output. For any fixed batch of $k$ exclusion queries, let $U$ be the union of their endpoints, so $|U|\le2k$. If $q\ge|U|$, reveal all those endpoint bits. Conditional on this assignment the entire answer vector depends only on total parity and has at most two possible values. For any global good set $G$ of probability at least $0.99$, some positive-probability endpoint assignment $\sigma$ has $\Pr(G\mid\sigma)\ge0.99$. The permitted local exclusion leaves mass at least $0.99-2^{-2r}$. Consequently

$$H_{\min}(F(X),G\cap G_\sigma\mid\sigma)
\le\log_2\frac2{0.99-2^{-2r}}<1.11<2r,$$

contradicting the lemma's entropy hypothesis. Using only the generic $k$-probe budget, its cost condition calls for $q\ge10k$, which exposes the endpoint union. Thus direct unamplified batching at that budget cannot repair the scalar application. An independently proved much smaller actual average probe cost could allow smaller $q$; this argument does not rule that out.

There is also the separate success problem: marginal error $\varepsilon$ gives only the union-bound guarantee $1-k\varepsilon$ for the batch. Independent repetition needs a pointwise input-error guarantee before a Chernoff argument is valid. The finite symmetrization above can supply that without extra storage; $h$ independent repetitions then cost up to $hB$ retained bits and $hk$ probes, with $h=O(\log(100k)/(1-2\varepsilon)^2)$ sufficient at fixed error. Repetition does not change the true batch output's small support after endpoint exposure. More indirect reductions, altered lemmas, and sharper probe analyses remain open.

## 6. Execution evidence and its limits

At the reviewed commit, using Python 3.12.14, ran exactly:

```sh
python checks/run_all.py --include-conjunction
```

Result: **PASS**. Seven imported-file hashes, ten interface checks, and 35 local documentation links passed. Exact-parity, bounded-error, sharp-rate, and both separate conjunction JSON outputs matched their recorded reports byte-for-byte in this environment. This rerun is distinct from the earlier checkpoint's CI logs.

Before relying on it, inspected the runner and sharp verifier, including optimal-residual selection, Gray-code cell enumeration, integer rank checks, floating entropy tolerances, the counted-read decoder, and finite-cover arithmetic. The sharp suite checks only small cells, numerical conjugacy samples, a small executed code, and arithmetic implications of cover existence. It does not construct the 1024-bit covers or certify the general theorem. Tolerances and original expected outputs were not changed.

An independent subspace enumeration counted 32,494 subspaces at $n=3,\ldots,7$ and found no rank-coverage violation. This independently implemented check overlaps the baseline subspace check's scope; it is not a new larger validation claim and is not added to the repository.

The new optional [asymmetric-cover check](../../checks/reviews/verify_asymmetric_cover.py) targets a different vulnerability: uneven blocks of sizes 3 and 2 and a weak cover with every reconstruction error concentrated on one designated coordinate. It executes all 1,228,800 input/pair/permutation/mask cases. Each of 320 fixed input/pair cases has exact error $1/20$, below the radius-derived bound $1/10$, and exactly one counted raw read. Its five stored bits include parity; it is a symmetry test, not a finite memory separation. Reproduce with:

```sh
python checks/reviews/verify_asymmetric_cover.py
```

Independent arithmetic also confirms block lengths $11,21,40,59,78,95,107,117$, total 529 including parity, error $6245/65472<1/10$, and the affine necessary bound 565. Specifically $\Phi_{1024}(564)=418770<2095104/5\le419230=\Phi_{1024}(565)$. No large encoder was built.

Access limitations: several versioned arXiv URLs failed in the web reader; author-hosted copies or directly downloaded versioned PDFs supplied the full text used above. The NRS journal and BEG journal full texts remained unavailable, so manuscript/arXiv numbering is explicit. No third-party paper is redistributed in this review. Search non-detection is not evidence of novelty.

## 7. Handoff and remaining uncertainty

No central proof change is requested by this audit. Preserve the original note, license, scripts, and recorded artifacts. Suggested lead integration is to add the weighted-rate-distortion attribution and exact scalar reduction; credit the older one-variable/common-bit argument; clarify the RAC randomness statement; and optionally add finite symmetrization equivalence. These are documented proposals, not edits to the scientific claim on `main`.

The narrow defensible paper candidate is: **equality of optimal first-order memory rates for arbitrary one-probe data structures for all pair parities and a specified weighted binary coding problem, together with the resulting exact first-order affine separation**. This does not assert a finite-length bidirectional simulation of arbitrary implementations. Its value would be identifying why unrestricted memory-dependent addresses do not beat graded endpoint recovery at first order. The scalar calculus, ordinary covers, entropy subadditivity, and generic linear/nonlinear distinction are established. A specialized theorem can still be substantive, but neither historical priority nor enough breadth for a particular venue has been demonstrated.

Unresolved: whether older approximate common-bits, partial-matrix, or help-bit results already imply the full weighted pair profile; whether a resource-preserving indirect reduction subsumes the theorem; and journal-version differences in the retrieved NRS material. Finite-length optimality, efficient constructions, and adversarial post-seed queries are separate problems, not defects in the stated theorem.

**Single next research action:** complete a targeted priority comparison for the all-overlapping-pairs, memory-dependent residual-rank profile, using the Jukna–Schnitger partial-matrix formulation and NRS product theorem as explicit starting points. Ask whether they yield the full weighted profile with no changed probe/error accounting. The coding optimization itself should now be treated as known. Keep issue #1 open; the originating workspace should review and integrate this report through its pull request, without the audit workspace merging it.

## 8. Research continuation after audit integration

### 8.1 Exact base, integration, and scope

Continuation date: 22 September 2026. PR [#3](https://github.com/GoGoKo699/Objective-Revision-Memory/pull/3), report commit `08fc60ea5396b78ec091f63ea182ea25327ef88c`, was merged with the user's subsequent authorization. The exact continuation base is `4e2c579795e2e780e132e3feb8072d2260ab3a7f`. Before merging, its head and base were rechecked, its verification workflow had completed successfully, and no review comments or other open pull requests were present. Work continued on the separate `research/rank-profile-foundations` branch.

No defect in Theorem S was found in this continuation. It narrows attribution further and supplies new written deductions. It integrates the earlier report's weighted-coding attribution, finite error-model equivalence, and corrected RAC attribution into the scientific documents. The original license, baseline notes, verification programs, and recorded reports are preserved.

### 8.2 What the targeted comparison resolved

The independent-character entropy budget has a precise antecedent: Impagliazzo–Moore–Russell, *An Entropic Proof of Chang's Inequality*, [arXiv:1205.0263v2](https://arxiv.org/pdf/1205.0263v2), Eq. (1) and Section 2. The [updated comparison](../LITERATURE_COMPARISON.md) gives the substitution. Together with the weighted coding reduction already established above, this leaves the pair geometry as the main unresolved priority target.

The one-star connection can be made without assuming affine preprocessing. Fix seed and memory value $m$. After absorbing known total parity, the error vector has rows

$$Z_q=(e_i+e_j+\beta_{m,q}e_{k(m,q)})\cdot X\oplus c_{m,q}.$$

Each address is fixed only on this memory cell. Replace that address in row $e_i+e_j$ by a star; the residual is an allowed completion. For independent residual rows $J$ of size $r$, every error pattern has at most $2^{n-r}$ preimages on the cube. Therefore

$$H(X\mid m)\le n-r+H(Z_J\mid m)
\le n-r+\sum_{q\in J}h_2(\delta_{m,q}).$$

This independently recovers the entropy budget from affine fiber counting. Jukna–Schnitger's Remark 1.4 and Lemma 2.3 are the exact antecedents; this conditional approximate-entropy formulation is our deduction. It does not establish the required bound on the number of high-bias **pair labels** from the rank of every selected subset. Full-matrix rank alone cannot do so: compare $L-1$ copies of $e_1$ and one $e_2$ with $L/2$ copies of each. Both systems have rank two; under $X_1=0$ and unbiased $X_2$ their total biases are $L-1$ and $L/2$. The pair-incidence restriction provides additional information.

The continuation also inspected the primary approximate-coordinate prediction results of Meir–Wigderson and Smal–Talebanfard. Use the latter's [ECCC revision 2](https://eccc.weizmann.ac.il/report/2017/191/revision/2/download/), not its unversioned original download: the revision history acknowledges a flaw in the stronger original claim. The corrected decision-tree statement and exact theorem locations are recorded in the comparison.

Here is our explicit obstruction to the direct output-lifting reduction. If $Y$ lists all pair parities, then $Y$ has $N=\binom n2$ coordinates but entropy at most $n-1$. Applying a coordinate-prediction bound to $Y$ starts with deficit at least $N-n+1$, making it vacuous even before charging memory. Also, complementing all raw bits leaves $Y$ unchanged, so a raw bit cannot be recovered from $Y$ alone. Adding an anchor requires, in general, two lifted-coordinate reads to reconstruct a raw bit, and the coordinate theorem forbids reading its target. A basis change removes redundancy but changes the queries and raw-read locality. This excludes those direct routes, not every possible reduction.

### 8.3 Mathematical deductions completed this session

The [rank-profile continuation](../RANK_PROFILE_EXTENSIONS.md) contains complete proofs:

1. **Generic envelope lemma.** If every labelled residual subset obeys $|J|\le g(\operatorname{rank}J)$, with $g(0)=0$ nondecreasing and increments $w_j$, then for any input distribution $P$,
   $$s\sum_q|\mathbb E_P(-1)^{a_q\cdot X}|
   \le[n-H_P(X)]\ln2+\sum_j\ln\cosh(sw_j).$$
   Its equivalent exponential-moment formulation gives the same $B$-bit help-label converse. Concavity is not needed for validity; it is relevant to whether scalar optimization respects ordered biases. This isolates the generic machinery from the extremal geometry and makes no claim of a new entropy inequality.
2. **Finite cap.** Substituting $g(r)=\min\{N,\Phi_n(r)\}$ drops unnecessary terms from the finite converse. The first-order rate stays unchanged, and finite optimality is not asserted.
3. **Exact low-rank geometry.** For $n\ge2r+2$, the maximum covered-pair count of any rank-$r$ subspace is exactly $nr-r(r+1)/2$, attained by coordinate subspaces. A quotient-basis injection offsets each covered internal pair by a missing cross pair. At $n=7,r=4$ the Hamming kernel covers 21 pairs, disproving extension of this formula to all ranks. The attaining coordinate subspace need not contain total parity, so this is a geometric extremum, not a claim about optimal mandatory-parity memory.
4. **Sharp bipartite benchmark.** For any query graph, matching and vertex-cover numbers give
   $$\nu(G)[1-h_2(\varepsilon)]\le B_G
   \le\tau(G)[1-h_2(\varepsilon)]+O_\varepsilon(\log(\tau(G)+1))+1.$$
   Here every fixed allowed edge must meet the input-and-seed average-error target. Matching residuals are independent even for arbitrary third-coordinate addresses; the upper bound codes a vertex cover and charges exact parity. For bipartite graphs, $\nu=\tau$, so the rate per matching edge converges to $1-h_2(\varepsilon)$ as $\nu\to\infty$. This is an explicit deduction from established ingredients. For arbitrary bipartite graphs, uniform edge-average error is weaker: a large star disjoint from small isolated edges supplies a counterexample to silently using the same lower bound. Complete bipartite graphs do permit the weaker error quantifier by averaging maximum matchings.

These deductions improve the mathematical formulation and provide comparison families; their priority is unresolved. They do not certify the all-pairs theorem as publishable. In particular, overlapping queries alone do not distinguish it: bipartite families can have substantial overlap and still reduce to ordinary coding.

### 8.4 Verification and next action

Reran `python checks/run_all.py --include-conjunction` on the continuation working tree with Python 3.12.14: **PASS**, seven imported-file hashes, ten interface checks, and 55 local documentation links. Every original exact, bounded-error, sharp-rate, and conjunction output remained byte-identical to its committed report. No tolerance or expected result was changed. The previously executed asymmetric-cover script was inspected but did not need another rerun in this session because it and its dependent model logic were unchanged.

A separate mathematical pass checked the new envelope/Gibbs argument, cap, low-rank injection, and graph quantifiers without finding a gap. It identified one exposition ambiguity, now corrected: the weighted coding comparison explicitly makes the quality label public to encoder and decoder. Agreement between model passes remains distinct from independent human review.

The new optional `python checks/reviews/verify_low_rank_coverage.py` was executed with exact integer arithmetic. It enumerates 3,559 eligible subspaces for $n=3,\ldots,7$, verifies the new bound and coordinate-subspace attainment, checks enumeration counts against Gaussian binomials, and verifies the 21-versus-18 Hamming-kernel counterexample. It imports no baseline enumerator. It tests the specified finite range, not the general theorem or novelty.

**Remaining uncertainty and next research action:** resolve whether the pair-specific all-subsets rank envelope, or a theorem implying its approximate one-star consequence, already occurs in prior work. The general lemma now identifies exactly which geometric statement must be compared. The full finite envelope is a concrete secondary problem, with a proved low-rank regime and an explicit high-rank obstruction. Keep issue #1 open. The continuation is prepared for integration through its dedicated pull request under the user's merge authorization; no manuscript release or external researcher contact is included.

## 9. Priority decision and operational contribution

### 9.1 Reviewed version and decision

Session date: 22 September 2026. Exact reviewed main: `b9394cd2ea64c45943e66ba7c61ae665f3df77c3`, merging PR [#4](https://github.com/GoGoKo699/Objective-Revision-Memory/pull/4) and report/theory commit `e2e4735064bc6d69f50b4a302997ce635cc9c7b1`. Work is isolated on `review/priority-decision`. Main, branches, open pull requests, and the issue handoff were checked before choosing this branch. The user's merge authorization remains in effect.

**Decision: proceed with a compact theorem-led research candidate, without certifying priority or submission readiness.** The [theorem brief](../THEOREM_BRIEF.md) states its resource ledger, operational equality, geometric explanation, and a finite separation. No central proof defect was found. The main new attribution is substantive: a classical matching theorem already gives a substantial subrange of the low-rank refinement. The main new deductions compare endpoint-only and unrestricted probes and delimit what preserving the old parity contributes.

### 9.2 The right priority target and a genuine classical reduction

The first-order converse needs less than the exact finite formula. A bound

$$|E|\le nr-r^2/2+o(n^2)$$

uniform in ranks and selected labelled residual families already suffices. Threshold integration adds at most that uniform remainder to the bias sum. With dual multiplier $s=a/n$, its contribution after dividing the memory bound by $n$ is $o(1)$. Thus an earlier result with different lower-order terms could subsume the geometric input. Comparing only the precise finite polynomial would set an unjustifiably narrow priority test.

Erdős–Gallai, *On Maximal Paths and Circuits of Graphs* (1959), [original paper](https://www.renyi.hu/~p_erdos/1959-10.pdf), Theorem (4.1), printed p.354, and the extremal function on p.346, gives a concrete reduction. Any matching of selected pair labels has independent residual rows: summing $j$ disjoint pair rows has weight $2j$, which at most $j$ one-coordinate corrections cannot cancel. Hence its matching number is at most residual rank $r$. The classical extremal matching bound yields, for $n\ge2r+1$,

$$|E|\le\max\left\{\binom{2r+1}{2},nr-\frac{r(r+1)}2\right\}.$$

For $r>0$ and $n\ge(5r+3)/2$, the second term dominates and matches coordinate-subspace attainment. This portion of the range previously proved for $n\ge2r+2$ is therefore already an elementary consequence of classical extremal graph theory. The documents now give that attribution. At $r/n\to0.45$, this route allows $0.405n^2+O(n)$ edges rather than the required $0.34875n^2+O(n)$, so its loss is leading order. This establishes the limitation of this reduction, not of all possible uses of matching theory.

### 9.3 Low-weight codes: the relevant statistic and a counterexample

Briggs–Pegden, *Extremal Collections of k-Uniform Vectors*, [arXiv:1801.09609v3](https://arxiv.org/pdf/1801.09609v3), Theorem 1.2 and Lemma 2.1, count distinct vectors of specified weights at a given rank. Our statistic is instead

$$C(W)=\left|(W+B_1(0))\cap\{v:|v|=2\}\right|,$$

where $B_1(0)=\{0,e_1,\ldots,e_n\}$. Distinct pair labels can use the same residual. The direct union bound $(n-1)A_1+A_2+3A_3$, with $A_k$ the weight-$k$ count in $W$, loses the necessary information at linear rank when those separate extremal estimates are substituted.

Even the complete weight enumerator does not determine coverage. In seven coordinates, let the binary spans have integer-encoded bases $(117,13,3)$ and $(104,28,3)$, with bit position $i-1$ representing coordinate $i$. Both have dimension three and enumerator

$$1+z^2+2z^3+z^4+2z^5+z^6.$$

Their covered pairs are respectively $\{12,13,14,23,24,34\}$ and $\{12,34,35,45,46,47,67\}$: six versus seven. The optional exact check verifies the entire spans and all pair residuals. This refutes identifying coverage with the enumerator; it does not rule out sharper inequalities informed by coding theory.

There is an exact quotient formulation. Let $z$ coordinate images in $\mathbb F_2^n/W$ be zero, and let distinct nonzero images $v$ have multiplicities $m_v$. Then

$$C(W)=z(n-z)+\binom z2+\sum_v\binom{m_v}{2}
+\sum_{\{u,v,w\}:u+v+w=0}(m_um_v+m_um_w+m_vm_w).$$

Each unordered triple here consists of distinct nonzero images. The set of all nonzero coordinate images spans dimension $n-r$. The terms enumerate zero-image pairs, equal-image pairs, and pairs whose sum is another available image. A simple binary-matroid triangle count is only the special case $z=0,m_v=1$; coordinate-subspace extremizers have $z=r$. A priority reduction must preserve these zero images and multiplicities or justify eliminating them.

### 9.4 Resource-preserving comparisons

The [literature ledger](../LITERATURE_COMPARISON.md), Section 8, gives primary versions and theorem locations. This pass inspected the following statements and worked through their direct translations:

| Primary statement | Translation and outcome |
| --- | --- |
| Wang–Lim–Gastpar, arXiv:1504.00553v2, Section II and Theorem 1, Eqs. (1)-(2) | Sequential cache/update coding permits a computed update from the full source and request. Setting the cache to exact parity and the update to the requested pair parity gives one bit each and zero error. Its repeated-instance rate theorem cannot be imported as a lower bound for a one-raw-bit probe merely by equating message lengths. |
| Makhdoumi–Huang–Médard–Polyanskiy, arXiv:1308.5239v2, Definition 2, Theorem 5, Proposition 2 | Local lossy decoding uses fixed encoded-coordinate neighborhoods and average bit distortion. The literal systematic representation stores $n+B$ bits and accesses the complete $B$-bit summary plus one potentially summary-dependent raw coordinate. These are different charged resources; lifting all pair outputs also loses the iid source model. |
| Gupta–Rajan, arXiv:1510.04820v2, Sections III-IV, Propositions 1-2 | Functional index coding fixes receiver Has/Want functions. Here $H_{ij}(x)=x_{k(f(x),i,j)}$ itself depends on the encoder being optimized. The fixed-instance confusion graph does not evaluate that joint optimization; broadcast corruption is also different from task error. |
| Gál–Miltersen, BRICS RS-03-44, Theorem 2 and Section 3 | The systematic exact prefix-parity tradeoff is an explicit historical NRS application, with a different query family and error requirement. It does not give this all-pairs approximate profile by direct substitution. |
| Carlen–Cordero-Erausquin, October 2007 manuscript, Eq. (2.4) and Theorem 2.1 proof | General entropy variational duality already supplies the Gibbs step. The pair-specific geometric count remains separate. |

These comparisons retain arbitrary nonlinear preprocessing, the uncharged immutable archive, free full-summary access and public randomness, and the late fixed query. No direct translation here supplies the full leading envelope. This is a bounded statement about inspected theorems and worked reductions, not proof of historical originality. Root inspection used full primary PDFs; when a versioned web URL failed, the unversioned PDF's displayed version was checked. The repository links identify the inspected versions. No third-party full text is redistributed.

### 9.5 New deductions with complete proofs in the brief

Let $B_{\rm arb}$ be the unrestricted optimum, $B_{\rm end}$ restrict the probe to a query endpoint, and $B_{\rm public}$ further make the address independent of memory. Under the same stated error criteria, all three have leading rate $\mathcal R(\varepsilon)$ for fixed $0<\varepsilon<1/2$. The unrestricted converse and existing publicly assigned graded construction squeeze these optima. This is an operational rate equality, not a simulation of arbitrary encoders.

For endpoint residuals the exact geometric coverage envelope is

$$f_n(r)=\binom n2-\binom{n-r}{2},\qquad 0\le r\le n.$$

Two quotient-basis coordinate images cannot be covered by $e_i,e_j$, or $e_i+e_j$; coordinate subspaces attain the bound. Its increments $n-j$ give the endpoint finite converse

$$B\ln2\ge s\binom n2\eta-\sum_{k=1}^{n-1}\ln\cosh(sk).$$

The $O(1)$ difference from the displayed unrestricted lower bound at $s=a/n$ is a comparison of lower bounds, not a bound on the finite optimal-memory gap.

At zero error the distinction is real: $B_{\rm end}(n,0)=n-1$. On any memory cell, two nonconstant coordinates whose XOR is decodable from either endpoint must be equal or complementary. All nonconstant coordinates are therefore functions of one common bit, and a cell has size at most two. For the upper bound store $X_3,\ldots,X_n$ and $X_1\oplus X_2$, including exact parity implicitly. This also uses only publicly determined endpoint addresses. Compared with the baseline unrestricted optimum, the exact extra cost is $\lfloor\log_2(n+1)\rfloor-1$ bits. Finite zero error is separate from a fixed-interior-error limit.

Finally, removing the requirement to retain old parity changes memory by at most one bit: $B_{\rm pair}\le B_{\rm arb}\le B_{\rm pair}+1$. Convert answers using the retained parity in one direction and store one additional parity bit in the other. Reads and error quantifiers are unchanged. The example thus does not establish a new leading cost for objective preservation.

### 9.6 Verification, limits, and next action

Executed `python checks/run_all.py --include-conjunction` on this working tree with Python 3.12.14: **PASS**, seven imported-file hashes, ten interface checks, and 71 local documentation links. All five recorded outputs (exact, bounded-error, sharp-rate, and the two separate conjunction reports) were reproduced byte-for-byte. No baseline program, report, tolerance, source manifest, or license was changed.

Executed `python checks/reviews/verify_endpoint_scope.py`: **PASS**, exact integer arithmetic throughout. It checked 4,088 charged-memory endpoint-decoder executions through seven bits; all 1,240 same-parity three-point cells through five bits, comprising 11,896 cell/pair tests; the complete equal-enumerator six-versus-seven coverage example; and the three-bit separation with 24 unrestricted executions and six impossible endpoint cell/pair cases. The new check is optional and imports no baseline verifier. Unchanged optional asymmetric-cover and low-rank scripts were not rerun this session. No general theorem or novelty claim rests on finite enumeration.

A separate read-only mathematical pass checked the new endpoint cell proof, envelope, public-address rate equality, parity sandwich, uniform-remainder scaling, and classical matching reduction. It found no mathematical flaw and identified one wording issue, corrected before integration: the structural almost-cover statement is an additional consequence of the proof, not logically equivalent to the numerical edge-count bound alone. Agreement between model passes is not independent human validation.

**Single next research action:** have the originating research workspace assess the compact theorem brief against the explicit leading-profile priority target, and settle whether the almost-vertex-cover property (or an equivalent approximate one-star theorem) has a prior antecedent. The classical partial reduction above is a required starting point. A specialist assessment would be more informative now than another undirected search or additional lower-order refinements. No external contact has been made or is included in this session. Keep issue #1 open; the full finite envelope and efficient constructions remain secondary problems. Proceed with the narrow research candidate, not a claim of a new coding law or submission readiness.

## 10. Classical geometry and a sharp success exponent

### 10.1 Exact checkpoint and changed assessment

Session date: 22 September 2026. Reviewed main: `0e91f088cd06376458f63a20f76e2d5b507a690a`, merging PR [#5](https://github.com/GoGoKo699/Objective-Revision-Memory/pull/5), report/theory commit `973039d864d62a8931e3e846ed5f170a8031ca97`. Main, branches, open pull requests, and issue #1 comments were checked before creating `research/excess-distortion`. No intervening scientific changes or open pull requests were present. Work remains on a dedicated branch under the user's continuing research and merge authorization.

**The previous novelty target was too generous to the geometry.** The full all-subsets envelope and its almost-vertex-cover mechanism are elementary consequences of established basis facts. It is unnecessary to find an older theorem written in the repository's exact notation. The geometric lemma should remain in the proof, with attribution, but should not be presented as a separate novelty candidate. This revises the assessment; it does not invalidate the bound or identify an earlier statement of the operational memory theorem.

The positive development is a stronger operational result: the existing converse and weighted coding construction determine the best exponential rate of success below the memory threshold, and the same threshold supports deterministic worst-input table distortion. These are written deductions with complete proofs in [EXCESS_DISTORTION.md](../EXCESS_DISTORTION.md), not independently certified new theorems.

### 10.2 Complete classical geometric reductions

The [literature ledger](../LITERATURE_COMPARISON.md), Section 9, records both routes with source-specific locations.

**Affine-basis sumsets.** Even-Zohar, *On Sums of Generating Sets in $(\mathbb Z_2)^n$*, [arXiv:1108.4902v2](https://arxiv.org/pdf/1108.4902v2), Example 11, Section 3.1, printed p.7, explicitly records the independent-points construction. For an affine basis $A=\{0,b_1,\ldots,b_d\}$, $|A+A|=1+d+\binom d2$. Theorem 1, printed p.2, also gives this specialization with $t=d,k=1,w=0$ for $d\ge2$; dimensions zero and one are immediate. This uses only elementary independent-pair counting, not the paper's full compression argument.

For a selected residual space $W$ of rank $r$, set $d=n-r$ and $S=\{0,e_1+W,\ldots,e_n+W\}$. Choose basis-coordinate representatives, giving $A\subseteq S$ and $|S|\le n+1$. A covered pair requires its quotient sum to lie in $S$. Every element of $(A+A)\setminus S$ identifies a distinct missing basis pair. Therefore

$$\#\{\text{uncovered pairs}\}\ge|A+A|-|S|
\ge\binom d2-r,$$

which yields exactly $|E|\le\binom n2-\binom{n-r}{2}+r$. This works for every selected subset and preserves all coordinate labels, zero images, and multiplicities. Negative lower bounds on the missing-pair count simply give a vacuous inequality at high ranks; there is no exceptional-rank omission.

**Fundamental circuits.** Tutte, *Lectures on Matroids*, J. Res. NBS 69B (1965), [primary paper](https://doi.org/10.6028/jres.069B.001), Section 2.2, printed p.3, between (2.21) and (2.22), gives uniqueness of the circuit meeting a minimal circuit-hitting set in a specified singleton. Its modern interpretation is fundamental-circuit uniqueness relative to the complementary basis; Tutte's rank convention must be translated.

In the labelled coordinate-image matroid, any covered pair of basis elements is completed by a nonbasis coordinate into a three-element circuit. That circuit is the completing element's unique fundamental circuit, so each of the $r$ nonbasis coordinates completes at most one basis pair. All other covered pairs touch those $r$ coordinates. This recovers both the envelope and the almost-cover statement. Loops and parallel elements remain in the matroid and do not invalidate the argument.

**Attribution boundary.** These are complete reductions to classical ingredients, not an assertion that Even-Zohar or Tutte studied delayed pair queries, nonlinear summaries, or the sharp error-rate curve. Conversely, failure to locate the repository's exact wording no longer supports a standalone geometric-novelty candidate. The earlier Erdős–Gallai partial reduction remains correct and relevant to the stronger low-rank refinement, but is not needed to attribute the main envelope.

Source access: the primary additive paper was inspected in parallel and by the main pass, including Theorem 1, Example 11, and the arXiv version history. Its PDF footer identifies v2, 30 July 2012; the current PDF's internal title date is 10 October 2018, so citations use the explicit arXiv version. Tutte's primary full-text OCR was inspected in the matroid pass and its relevant passage checked during synthesis. The main pass's direct PDF request exceeded the reader's size limit; alternate archive/OCLC requests failed. The report does not claim a second complete retrieval of that paper. No third-party full text is redistributed.

### 10.3 The stronger operational theorem

Fix all input-independent tapes. For each input, define $\Delta_R(x)$ as the fraction of the $N=\binom n2$ pair queries the decoder would answer incorrectly, considering each separately from the same summary with its own one-read budget. This is a counterfactual error table, not a free multiquery execution. It permits erroneous pairs and supplies no guarantee against choosing one adversarially after the seed is visible.

Keep all resource and exact-parity constraints. For the new optimization, the table-distortion criterion **replaces** the original per-fixed-query error promise. It must not be imposed together with that promise when studying subthreshold success: the partial-cover constructions intentionally fail on most inputs there.

**Finite tail converse.** The existing exponential-moment lemma and positivity over at most $2^B$ memory labels give

$$\Pr\{\Delta_R(X)\le\varepsilon\}
\le\min\left\{1,\exp\left[B\ln2-sN(1-2\varepsilon)
+\sum_{k=1}^n\ln\cosh(sk)\right]\right\}.$$

At $s=a/n$, this is at most
$\min\{1,e^{C_\varepsilon}2^{B-n\mathcal R(\varepsilon)}\}$,
where $C_\varepsilon=a(1-2\varepsilon)/2+\ln\cosh a$. The proof extends each memory label's decoder characters to the whole cube, applies the uniform moment bound, then averages tapes. No affine-cell assumption or restriction on summary-dependent addresses is introduced.

**Worst-input covering.** In a fixed order, estimate endpoint $j$ and reread $i$ for $i<j$. For reconstructed word $z$ the exact table-error count is

$$N\Delta(x)=\sum_{j=1}^n(j-1)\mathbf1\{x_j\ne z_j\}.$$

For consecutive blocks of lengths $m_\ell$, cumulative endpoints $s_\ell$, and covering radii $r_\ell$, every input has at most $\sum_\ell(s_\ell-1)r_\ell$ wrong pairs. Ordinary covers charge all their index bits and one exact parity bit. Choosing a strict distortion margin, then a fine fixed number of blocks, then sufficiently large $n$, attains rate $\mathcal R(\varepsilon)$ for every input. The resulting address is deterministic and depends only on the query. Public symmetrization can additionally supply the old marginal guarantee while preserving each table's distortion bound for every input and seed.

**Sharp success exponent.** Let $P_n^*(B,\varepsilon)$ be the best success probability for this table criterion under the resource constraints. For fixed $0<\varepsilon<1/2$, integer $B_n\ge1$, and $B_n/n\to\rho\ge0$,

$$\lim_{n\to\infty}-\frac1n\log_2 P_n^*(B_n,\varepsilon)
=\bigl(\mathcal R(\varepsilon)-\rho\bigr)_+.$$

The converse is the preceding tail bound. For attainment, an ordered-endpoint weighted ball has relative volume $v_n=2^{-n\mathcal R(\varepsilon)+o(n)}$, proved by Chernoff above and finite-block type counts below. With $K=2^{B-1}$ reconstruction centers, a fixed codebook exists covering fraction at least $1-(1-v_n)^K\ge(1-e^{-1})\min\{1,Kv_n\}$. Store the selected center's $B-1$-bit index and exact parity. Thus deterministic endpoint schemes attain the unrestricted success exponent. The codebook is fixed independently of input; no input-dependent storage is omitted.

The result does not identify the optimal failure exponent above the threshold. At the critical rate, zero success exponent alone does not imply success tends to one. Fixed tolerated excess-distortion probability below one has the same rate threshold, and success probability as small as $e^{-o(n)}$ still requires that leading rate. These claims keep the error parameter fixed in the interior.

### 10.4 Verification and assessment

Executed `python checks/run_all.py --include-conjunction` with Python 3.12.14 on this working tree: **PASS**, seven imported-file hashes, ten interface checks, and 86 local documentation links. All five recorded outputs were reproduced byte-for-byte. `git diff --check` passed, and a comparison against the reviewed base confirmed that the license, baseline notes, source manifest, original verifiers, recorded reports, and separate conjunction exploration were unchanged.

Executed `python checks/reviews/verify_excess_distortion.py`: **PASS**, with exact integer and rational arithmetic. The explicit unequal-block cover used four charged summary bits and one counted endpoint read in all 2,688 input/pair executions; its maximum wrong-pair count was seven, below the coarse bound eight. Three explicit decoders through eight bits, including a nonlinear retained AND bit and summary-dependent nonendpoint addresses, supplied 33,768 input/pair executions, 22,512 counted reads, and 534 exact rational tail inequalities. Of those upper bounds, 44 were below one. The script verifies oracle guards and actual address dependence. These checks do not extrapolate a limiting exponent. Earlier optional review scripts were unchanged and were not rerun in this session. No baseline verifier or recorded output was modified.

A separate read-only proof pass checked the tail prefactor, extension outside memory cells, arbitrary tape couplings, weighted-ball volume limit, finite index/parity accounting, partial-cover probability, critical-rate interpretation, and symmetrization. It found no mathematical defect. It identified the ambiguity about admissible schemes noted above; the new note and brief now explicitly remove the old per-query error promise from the success optimization. Agreement between model passes is not independent human validation or a proof-assistant certificate.

**Revised development decision:** retain a narrow operational coding candidate, now with a sharp success exponent and a deterministic covering interpretation. Its elementary geometry and standard information-theoretic ingredients should be credited plainly. This is more precise than defending an unlocated standalone geometric theorem, but does not itself establish historical novelty or enough significance for publication.

**Single next action:** assess the rate/success-exponent characterization as an application in approximate systematic data structures and source coding. Issue #1 remains open for that operational priority and significance assessment; the geometric attribution subquestion is resolved at the level needed for honest presentation. No external researcher contact, submission, or manuscript release occurred. Preserve the main proof, license, and original verification artifacts when integrating this continuation.
