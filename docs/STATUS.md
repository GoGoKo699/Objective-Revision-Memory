# Research status and next steps

22 September 2026. This is a research checkpoint, not a paper release.

## Active and separate models

The active line is **pair-parity revision**: exact original parity, then exclusion of any two coordinates, with one raw-bit reread. Exact and approximate versions of this same model are treated together in [RESEARCH_NOTE.md](../RESEARCH_NOTE.md).

The earlier **conjunction refinement** line permits arbitrary subsets of additional binary acceptance requirements. It uses exact worst-case decisions and a variable adaptive-read budget. It is preserved under [explorations/conjunction](../explorations/conjunction/research_note.md), not presented as a strengthening or replacement of the parity theorem. In particular, its half-record inspection result does not apply to the parity model.

## Claim ledger

| Claim | Current support | Not established |
| --- | --- | --- |
| Exact parity optimum | Written lower bound, construction, original verifier reproduced | Historical originality |
| Arbitrary-encoder bounded-error converse | Rank-coverage and weighted-entropy proofs; exhaustive small cells | Optimal unrestricted rate; priority |
| Sharp affine leading rate | Converse and matching random-subset construction | Exact finite-length optimum |
| Eight-versus-nine and 144-versus-171 comparisons | Exact rational arithmetic and explicit majority algorithm | Optimal nonlinear memory; first occurrence |
| Majority and RAC achievability | Credited to established coding results | No claim to invent these ingredients |
| Conjunction dimension bound and count summary | Separate proofs and unchanged verifier reproduced | Novelty, or any transfer to parity without proof |
| Real-world AI understanding or safety | Motivation only | Empirical or theoretical conclusions about deployed systems |

There is no independent expert review or formal proof-assistant verification in this record. Check success and mathematical derivation are distinct from novelty and publication significance.

## Next scientific work

**First:** complete the exact theorem comparison. The [literature note](LITERATURE_COMPARISON.md) now isolates why a literal scalar-output application of the query-with-sketch min-entropy lemma is insufficient, while leaving batched reductions open. Compare the pair-coverage count, the weighted entropy lift, and the affine rate separately. Record any subsumption explicitly.

**Second:** investigate the unrestricted rate between $1-\sqrt{h_2(\varepsilon)}$ and the smaller of $1-h_2(\varepsilon)$ and $1-\sqrt{2\varepsilon}$. A limiting optimal rate is not yet proved to exist here. Seek a matching converse, a better representation, or a concrete counterexample to a proposed stronger inequality. Avoid treating a failed proof attempt as a failed research direction.

**Third:** assess whether the surviving result supplies a clear and worthwhile theoretical contribution. The scope is classical information access; an AI-correction title is not a substitute for mathematical novelty. Do not add neural experiments merely to compensate for an unresolved contribution.

No manuscript drafting, release tagging, external correspondence, or large simulation is part of this checkpoint. The next work can remain proof-led and locally verifiable.
