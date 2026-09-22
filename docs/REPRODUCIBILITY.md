# Reproduction and evidence boundaries

Python 3.10 or newer, standard library only. Run without `-O`; assertions and explicit guards must remain active.

```sh
python checks/run_all.py
python checks/run_all.py --include-conjunction
```

The runner writes temporary reports outside the checkout, compares them with the recorded JSON, checks the source manifest, resolves local documentation links, and tests original raw-read interfaces. It now includes `verify_sharp_rate.py` in addition to the original exact and bounded-error suites. The optional conjunction suite remains a separate model.

## New sharp-rate suite

Run it alone with:

```sh
python checks/verify_sharp_rate.py --output /tmp/a1-sharp-rate.json
```

The [recorded report](../results/sharp_rate.json) contains the following scopes.

| Check | Scope | Arithmetic |
| --- | --- | --- |
| Memory-cell enumeration | All 131,610 nonempty fixed-parity cells at n=3,4,5 | Integer correlations and binary ranks |
| Rank-profile and threshold coverage | 384,828 checks on those cells | Exact integer comparisons |
| Independent-bias entropy budget | Every enumerated cell | Floating logarithms, tolerance 2e-10 |
| Conditional finite dual inequality | 526,440 cell/parameter checks | Floating logarithms, tolerance 2e-10 |
| Seeded graded decoder | 36,864 executions; all 96 fixed input/query cases at n=4, every mask and permutation | Exact error 1/8 and counted one-read access |
| Finite covering-existence certificate | Eight 128-bit blocks; 529 summary bits vs affine lower bound 565 at error 1/10 | Exact integer and rational arithmetic |
| Rate curve and convex identities | Listed error values, 2,048 versus 4,096 Simpson panels, discrete quality profiles | Numerical illustration only |

Curve checks compare rates to 1e-9 and parameters to 1e-8; displayed reports round illustration values to nine decimal places. Internal analytic identity checks use 2e-10. The runner's report comparison uses 1e-10 absolute/relative tolerance for floating fields, requiring exact equality for discrete fields. These are numerical tolerances, not interval-arithmetic certificates.

The large Hamming covers are not enumerated or built. Their finite size and error bounds are consequences of the written covering-existence argument; the script verifies the arithmetic. The small four-bit scheme is executed through an oracle that rejects a second raw read. Neither kind of check proves general optimality by extrapolation.

## Preserved baseline

The original exact and bounded-error scripts and reports, along with the separate conjunction artifacts listed in [SOURCE_MANIFEST.json](SOURCE_MANIFEST.json), remain unchanged. Their original scopes and detailed counts are in the committed result files. Exact parity has one-based raw-coordinate conventions; bounded-error code has zero-based conventions. The runner explicitly checks both and rejects disabled assertions.

[BASELINE_NOTE.md](../BASELINE_NOTE.md) preserves the prior repository note. Its old open-rate language is historical; [RESEARCH_NOTE.md](../RESEARCH_NOTE.md) supplies the new matching proof. Existing imported-file hashes do not purport to authenticate new files; Git records those revisions normally.

No network access, GPU, simulation cluster, third-party optimizer, or training dataset is used by these checks. Passing them supports implementation and finite-counterexample testing, not historical novelty, independent human validation, or a formal proof certificate. CI conclusions must be read from the completed workflow run, not inferred from the presence of a workflow file.

## Optional audit and continuation checks

These targeted checks supplement the unchanged runner and recorded reports:

```sh
python checks/reviews/verify_asymmetric_cover.py
python checks/reviews/verify_low_rank_coverage.py
python checks/reviews/verify_endpoint_scope.py
python checks/reviews/verify_excess_distortion.py
```

The first executes 1,228,800 input/pair/permutation/mask cases with uneven blocks and reconstruction errors concentrated on one coordinate. Every fixed input/pair has exact error $1/20$ and one counted raw read; all five summary bits, including parity, are charged. This tests symmetrization, not a memory separation.

The second independently enumerates binary subspaces by reduced row echelon bases, without importing baseline routines. For $n=3,\ldots,7$ and $0\le r\le\lfloor(n-2)/2\rfloor$, it checks all 3,559 subspaces, direct residual-row membership, enumeration counts against Gaussian binomials, and attainment of $nr-r(r+1)/2$ by coordinate subspaces. It also enumerates the 16-vector rank-four Hamming kernel at $n=7$, which covers all 21 pairs and disproves a global extension of that formula. All arithmetic is exact. The [continuation note](RANK_PROFILE_EXTENSIONS.md) supplies the proof and range restriction.

The third uses an endpoint-only raw-read oracle and the complete charged $n-1$-bit summary for every input/pair at $n=3,\ldots,7$ (4,088 executions). It checks all 1,240 same-parity three-point cells through five bits against both endpoint addresses and all Boolean truth tables, finding an impossible pair in every cell. It also verifies the one-bit unrestricted versus two-bit endpoint construction at $n=3$, and two dimension-three subspaces of seven bits with the same full weight enumerator but pair coverage six versus seven. It imports no baseline verifier and uses exact integer arithmetic. The [theorem brief](THEOREM_BRIEF.md) and [audit](reviews/SHARP_RATE_AUDIT.md) give the general proofs and scope limitations.

The fourth checks the [excess-distortion deduction](EXCESS_DISTORTION.md). An explicit cover on unequal three- and four-bit blocks charges four summary bits including parity; all 2,688 input/pair executions use one counted endpoint read. It verifies the exact weighted-error identity and the worst-input bound. Separate tail checks enumerate 33,768 input/pair executions for three decoders through eight bits, including a nonlinear retained bit and summary-dependent nonendpoint addresses. All 534 tail inequalities use exact rational arithmetic by setting $e^s$ to a rational number; 44 upper bounds are below one. No asymptotic exponent is inferred from these finite checks.

These scripts print their results; no original report or tolerance is changed. The optional checks are not silently treated as CI gates in the existing workflow.
