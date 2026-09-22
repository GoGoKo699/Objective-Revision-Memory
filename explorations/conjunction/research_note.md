# Separate exploration: conjunction refinements

This note consolidates the conjunction checkpoint of 22 September 2026. It is **not** the parity model used in the main research line. Its source verifier and recorded outputs are unchanged; this note is an editorial restatement of its main arguments.

## Model

An original acceptance bit $`u`$ is retained separately. Conditional on an originally accepted record, there are $`n`$ additional binary facts $`x`$. A later tightening specifies a subset $`S`$ and asks whether all selected facts hold:

```math
h_S(x)=\prod_{i\in S}x_i.
```

The empty conjunction is one. An $`m`$-bit summary is formed before $`S`$ is known. Afterward the decoder can read at most $`t`$ individual raw facts, adaptively. The guarantee is exact for every record and subset. Local computation is free and the archive is not charged to $`m`$. The separately retained $`u`$ is not charged to this additional-fact summary budget.

This differs from parity in its Boolean function, revision family, memory convention, and variable probe allowance. No bounded-error theorem from the main note is transferred here.

## Dimension lower bound

If the summary has $`M`$ possible values, then

```math
M\sum_{j=0}^t\binom nj\geq2^n.
```

To see this, fix one memory cell $`C`$. A depth-$`t`$ adaptive bit decision tree computes a multilinear polynomial of degree at most $`t`$ on the full cube: sum the products of literals for its accepting paths. Therefore every requested conjunction, when restricted to $`C`$, lies in the span of at most $`\sum_{j=0}^t\binom nj`$ low-degree monomials.

All conjunctions together span every function on $`C`$: the indicator of any input is a product of coordinates and complemented coordinates and expands into conjunctions. Thus $`|C|\leq\sum_{j=0}^t\binom nj`$. Summing over the cells proves the bound. This permits adaptive reads and arbitrary encoders.

It follows that

```math
m\geq n-\log_2\sum_{j=0}^t\binom nj.
```

For any fixed positive $`\delta`$, having $`t\leq(1/2-\delta)n`$ forces a positive linear summary cost. Hence a sublinear summary cannot reduce worst-case inspection below one half by a fixed fraction.

## Matching leading-order count construction

Store only the Hamming weight $`w=\sum_i x_i`$, requiring $`\lceil\log_2(n+1)\rceil`$ bits. If $`|S|\leq n/2`$, inspect $`S`$. Otherwise inspect its complement and use

```math
\sum_{i\in S}x_i=w-\sum_{i\notin S}x_i.
```

Acceptance holds exactly when the computed sum equals $`|S|`$. At most $`\lfloor n/2\rfloor`$ raw reads are needed. Combined with the dimension lower bound, the optimal read fraction at this logarithmic summary budget tends to one half. This does not assert exact finite-length optimality at every $`n`$.

## Affine summaries and a small separation

If the summary is a rank-$`r`$ affine map over $`\mathbb F_2`$, worst-case inspection for this query family is exactly $`n-r`$. For the lower bound, ask the full conjunction at the all-ones input. Fewer than $`n-r`$ inspected coordinates leave a nonzero kernel vector vanishing on all inspected positions. Adding it preserves both the summary and transcript, but introduces a zero and changes the answer. For the upper bound, inspect a complement of pivot coordinates and reconstruct the entire input.

At four features, a two-bit arbitrary summary and one read suffice. The four cells are

```
0000 0001 0010 0111
0011 0101 0110 1011
0100 1100 1101 1110
1000 1001 1010 1111
```

The [explicit decoder](four_feature_decoder.json) gives a constant or single-coordinate literal for every cell and subset. Four summary values are necessary because a one-read cell has size at most $`1+4=5`$, and $`\lceil16/5\rceil=4`$. At the same two-bit budget, an affine summary needs at least two reads.

## Evidence and status

The unchanged [verifier](verify.py) and [recorded output](verification_results.json) test every one-read candidate cell through four features, the count construction through eight features, and all affine row spaces through four features. Run them without modifying the checkout using `python checks/run_all.py --include-conjunction` from the repository root.

These are mathematical and computational checkpoints, not historical novelty claims. The systematic-data-structure access model is established; compare the main [literature audit](../../docs/LITERATURE_COMPARISON.md). The conjunction dimension argument and count construction require their own priority and significance audit. They are retained for comparison, not merged into the current parity contribution.
