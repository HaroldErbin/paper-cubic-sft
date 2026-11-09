# Verification scripts

Companion scripts of the cubic closed string field theory paper.
Each `verify-*.py` prints PASS/FAIL per named check and exits nonzero on failure; the records they cite are in `../agent/derivations/`.

## How to run

Requires [uv](https://docs.astral.sh/uv/).
From this directory:

```bash
uv sync
uv run python verify-b1-quintic.py
```

Outputs (figures, JSON logs) go to `output/`, which is git-ignored.
`verify-kp-complex-s.py` starts a process pool: pass `--workers N`.

## Scripts

"Standalone" = runs with the files of this repository only.
"Result" = one run on 2026-11-09 (CPU, `nice -n 19`, 3 min cap, 4 threads); TIMEOUT means the script exceeded the cap, not that a check failed.
Scripts marked "needs data not published" import data of a companion project that is not public yet, and are not included in this repository.
For the same reason the following scripts, which compare against values of that project, are listed but not included: `comparator-points-2026-09-22.py`, `verify-a2-schwinger.py`, `verify-conventions.py`, `verify-d5-five-field.py`, `verify-j-closed-form.py`, `verify-kernel-analytic-structure.py`, `verify-kp-box.py`, `verify-kp-kernel.py`, `verify-kp-real-s.py`, `verify-ph24-vs.py`, `verify-stage0-translation.py`.

| Script | Claim verified | Standalone | Result |
| --- | --- | --- | --- |
| `comparator-points-2026-09-22.py` | Evaluate F(s,t,u) at eight comparator points of the four-tachyon amplitude | yes | PASS |
| `plot-circle-gluing-covering.py` | Figure: circle-gluing covering of V_{0,4} (record 074) | yes | PASS |
| `plot-ws-q-plane.py` | Figure: the plumbing q-plane of the s-circle gluing | yes | PASS |
| `verify-002-dictionary.py` | Exchange symmetry of the BV odd symplectic form (record 002) | yes | PASS |
| `verify-220-relation.py` | CFL (2,2,0) and (1,2,0) IBL structure relations | yes | PASS |
| `verify-a1-telescoping.py` | Amplitude-level telescoping of the Sigma-exchange (record 007) | yes | PASS |
| `verify-a2-schwinger.py` | Schwinger representation of V_4^{-1} (record 008) | yes | PASS |
| `verify-a3-ibl-pedagogical.py` | Self-checks of the pedagogical IBL note | yes | PASS |
| `verify-a4pt-chain.py` | 4-point amplitude chain HS -> telescoping -> SFT (record 023) | yes | PASS |
| `verify-all-orders-eom.py` | All-orders equations of motion (record 100) | yes | PASS |
| `verify-b1-quintic.py` | O(g_s^3) quintic milestone | yes | PASS |
| `verify-b3-sextic.py` | O(g_s^4) sextic milestone | yes | PASS |
| `verify-b4-sigma3.py` | Sigma_3 milestone (record 014) | yes | PASS |
| `verify-b5-ogs4-gauge-eom-ibl.py` | O(g_s^4) gauge, EOM and IBL checks (record 015) | yes | PASS |
| `verify-b6-ogs5-septic.py` | O(g_s^5) septic order (record 018) | yes | PASS |
| `verify-b7-allorders.py` | All-orders structure (record 019) | yes | PASS |
| `verify-bare-operators.py` | Bare operators (record 115) | yes | PASS |
| `verify-brst-background.py` | Linearised BRST operator around a background (record 067) | yes | PASS |
| `verify-bv-master-equation.py` | Truncated classical BV master equation, finite cyclic L_infty model | yes | PASS |
| `verify-bv-master-k4.py` | k = 4 truncated classical BV master equation | yes | PASS |
| `verify-chain-surfaces-covers.py` | Chain surfaces as covers (record 031) | yes | PASS |
| `verify-cheung-remmen.py` | Cheung–Remmen cubic gravity vs the cubic HS step (record 099) | yes | PASS |
| `verify-chi-ogs5-count.py` | O(g_s^5) counting argument (record 038) | yes | PASS |
| `verify-chi-ogs5-matching.py` | chi-scheme O(g_s^5) matching (record 048) | yes | TIMEOUT |
| `verify-chi-partner.py` | Wrong-sign (Liouville-type) partner chi at O(g_s^4) | yes | PASS |
| `verify-circle-gluing-inverse.py` | p_{2,2}^{-1} as a circle gluing (record 074) | yes | PASS |
| `verify-circle-map.py` | Circle map Phi_n, n = 2 tachyon pair (record 071) | yes | PASS |
| `verify-conventions.py` | Ghost-sector convention reconciliation (record 041) | yes | PASS |
| `verify-covering-m06.py` | What the Sigma-composite covers in M_{0,6} (record 036) | yes | PASS |
| `verify-cubic-sft-overview.py` | Symbolic self-checks of the overview note | yes | PASS |
| `verify-d5-five-field.py` | Order-d^5 term of the five-field truncation (record 095) | yes | PASS |
| `verify-dressed-ckv.py` | Dressed CKV (record 080) | yes | PASS |
| `verify-dressed-operator-order.py` | Truncation dependence of the dressed kinetic operators (record 117) | yes | PASS |
| `verify-dressing-test.py` | Direct test of the gluing recipe, stage B (record 098) | no | needs data not published |
| `verify-exchange-real-momenta.py` | Six-point Sigma_2 exchange at real momenta (record 105) | yes | PASS |
| `verify-first-assumption.py` | Toy model of the "first assumption" passage (record 116) | yes | PASS |
| `verify-fold-arc-convergence.py` | Fold-arc convergence of the (h, m) expansion (record 079) | yes | PASS |
| `verify-fold-arc-excited.py` | Fold-arc convergence threshold, excited states (record 084) | yes | PASS |
| `verify-forced-kernel.py` | Forced-kernel search (record 107) | no | needs data not published |
| `verify-gap3c.py` | GAP-3c (record 043) | yes | PASS |
| `verify-gap3e-contractible-pair.py` | BV consequences of the flat representative (record 056) | yes | PASS |
| `verify-gauge-algebra-ogs3.py` | Gauge algebra at O(g_s^3) (records 040, 043) | yes | TIMEOUT |
| `verify-gauge-algebra-ogs4.py` | Gauge algebra at O(g_s^4) (record 053) | yes | PASS |
| `verify-gauge-unfixing-c1.py` | Gauge unfixing of Sigma_2, candidate C1 (record 108) | yes | PASS |
| `verify-gauge-unfixing-structure.py` | Gauge unfixing of Sigma_2, structure lemma (record 102) | yes | PASS |
| `verify-geometric-inverse.py` | Geometric 1/m_2 (record 030) | yes | PASS |
| `verify-gluing-recipe.py` | Gluing recipe for the explicit quartic vertex (record 096) | no | needs data not published |
| `verify-h1-error.py` | Error of H1 (record 090) | no | needs data not published |
| `verify-hessian-affine.py` | Hessian of the cubic HS action is affine in the background (record 066) | yes | PASS |
| `verify-hpt-transfer.py` | Homological-perturbation transfer of the Sigma sector | yes | PASS |
| `verify-hs-bar-cobar.py` | Route C vs the bar-cobar canonical equations (record 024) | yes | PASS |
| `verify-hs-gauge-invariance.py` | Exact off-shell gauge invariance of the HS action | yes | PASS |
| `verify-hs-level11.py` | Cubic HS action at level (1,1), Sigma block (record 064) | no | needs data not published |
| `verify-i2-ibl-action.py` | IBL action at O(g_s^2) | yes | PASS |
| `verify-i3-m2-invertibility.py` | Invertibility of the two-output product | yes | PASS |
| `verify-ibl-gauge-components.py` | Term list of the IBL gauge transformation (record 111) | yes | PASS |
| `verify-ibl-generating-sign.py` | Family encoded by the IBL generating function (record 088) | yes | PASS |
| `verify-ibl-mc-conventions.py` | Grading of the genus-zero Maurer-Cartan equation (record 103) | yes | PASS |
| `verify-ibl-remarks.py` | Finite-model checks of the IBL section remarks (record 114) | yes | PASS |
| `verify-j-closed-form.py` | Representations of J(p,q) (record 047) | yes | TIMEOUT |
| `verify-kernel-analytic-structure.py` | Analytic structure of the fixed-level kinetic operator (record 104) | yes | PASS |
| `verify-ker-v4-v5-compat.py` | Compatibility of the ker V_4 quotient with V_5 (record 034) | yes | PASS |
| `verify-kp-box.py` | Discretisation box for the pair kernel K_P (record 045) | yes | PASS |
| `verify-kp-complex-s.py` | Frozen-momentum zero scan of F(s,0,0) (record 051); optional groups need unpublished caches | yes | TIMEOUT |
| `verify-kp-kernel.py` | Level-0 s-wave pair kernel K_P (record 049) | yes | PASS |
| `verify-kp-real-s.py` | Pair kernel K_P at real s (record 050) | yes | not run (process pool) |
| `verify-linfty-ibl-repackaging.py` | L_infty => genus-zero IBL_infty repackaging (record 026) | yes | PASS |
| `verify-mc-cubic-coupling.py` | Coupling c g_s V_3(Sigma_2, Psi) (record 109) | yes | PASS |
| `verify-mean-field-decomposition.py` | Mean field, finite model (record 069) | yes | PASS |
| `verify-mean-field-fluctuations.py` | Schur identity, BRST deformation, degenerate branch (record 060); needs ~9 GB RAM | yes | PASS |
| `verify-mean-field-gap-level11.py` | Level-(1,1) gap equation (record 070) | no | needs data not published |
| `verify-mean-field-level11.py` | Joint Hessian at level (1,1) (record 063) | no | needs data not published |
| `verify-momentum-space.py` | Momentum-space auxiliary fields (record 072) | yes | PASS |
| `verify-morphism-check.py` | L_infty-morphism identities for the comparison map | yes | PASS |
| `verify-muenster-degree.py` | Degree dictionary paper / CFL / Münster–Sachs (record 120) | yes | PASS |
| `verify-multiplier-ogs4.py` | Multiplier remedy on ker V_4 at O(g_s^4) (record 068) | yes | PASS |
| `verify-mu-segment-cert.py` | Segment criterion certification (record 092) | no | needs data not published |
| `verify-mu-table.py` | Second-order coefficients mu_i(q) of the quartic vertex (record 089) | no | needs data not published |
| `verify-negative-moduli.py` | Negative moduli (record 035) | yes | PASS |
| `verify-neumann-chain.py` | Neumann-chain support | no | needs data not published |
| `verify-npatch-atlas.py` | n-puncture patch in the atlas picture (record 077) | yes | PASS |
| `verify-npatch-n3.py` | n = 3 patch and the two-patch map to M_{0,6} (record 081) | yes | PASS |
| `verify-offshell-gluing.py` | Dressed gluing off shell (record 113) | no | needs data not published |
| `verify-omega2-construction.py` | Antisymmetric two-output symplectic form omega_2 | yes | PASS |
| `verify-omega2-physical.py` | Physical grading of omega_2 | yes | PASS |
| `verify-omega-k.py` | Graded exchange symmetry of omega_k (record 055) | yes | PASS |
| `verify-p22-inverse-sewing.py` | p_{2,2}^{-1} as a sewing (record 110) | yes | PASS |
| `verify-paper-gap-7.py` | Two forms of the (2,2) relation of the raised family (record 086) | yes | PASS |
| `verify-paper-gaps-3-4.py` | Paper gaps 3 and 4 (record 085) | yes | PASS |
| `verify-partner-closure.py` | Partner count, step 2 (record 101) | yes | TIMEOUT |
| `verify-partner-count.py` | Partner count (record 101) | yes | TIMEOUT |
| `verify-partner-octic.py` | Partner count, step 3 (record 101) | yes | TIMEOUT |
| `verify-per-tile.py` | Per-tile step (record 091) | no | needs data not published |
| `verify-ph20-virtual-dim.py` | Virtual dimension (record 036 addendum) | yes | PASS |
| `verify-ph23-doublet.py` | The Sym^2 source doublet (Sigma, chi) is timelike | yes | PASS |
| `verify-ph24-vs.py` | Comparison against Virasoro–Shapiro | yes | PASS |
| `verify-ph2a.py` | Nested kernels of the dressed tower at g = 0 (record 061) | yes | PASS |
| `verify-ph31-actual.py` | PH31 for the actual p_{2,2} (record 094) | no | needs data not published |
| `verify-ph31prime.py` | Fixed-halves model: conservation law, witness, limit (record 082) | yes | PASS |
| `verify-ph31-rank-ext.py` | Extensions of the rank test (record 083) | yes | TIMEOUT |
| `verify-ph31-rank-half.py` | Rank rows at the vertex (record 093) | yes | TIMEOUT |
| `verify-ph31-rank-k3d3.py` | K = 3 cokernel of the rank test (record 087) | yes | TIMEOUT |
| `verify-ph31-rank.py` | Rank falsifier (record 078) | yes | TIMEOUT |
| `verify-ph6-conjugation-n4.py` | Conjugation invariance of the declared section at n = 4 (record 054) | no | needs data not published |
| `verify-ph7-ddagger.py` | Reality conjugation squares to +1 on Grassmann-odd states | yes | PASS |
| `verify-phase6-riemann.py` | Self-checks of the geometric-interpretation note | yes | PASS |
| `verify-q2-orientation.py` | Orientation of the off-shell measure (record 042) | yes | PASS |
| `verify-r16-scope.py` | Augmented obstruction P_{k,l} != 0 for k, l >= 2 (record 026) | yes | PASS |
| `verify-r29-onshell.py` | On-shell limit of the level-0 Sigma-exchange (record 050) | yes | PASS |
| `verify-reality-tower.py` | Reality of the auxiliary tower (record 028) | yes | PASS |
| `verify-rho3-residual.py` | No residual factor on the mapping radius rho_3 | no | needs data not published |
| `verify-riemann-m2-geometry.py` | Riemann-surface meaning of m_2 (record 020) | yes | PASS |
| `verify-rs4-sewing-fixtures.py` | Ghost-zero-mode sewing fixtures | yes | PASS |
| `verify-rs5-no-local-kernel.py` | No-local-kernel theorem for m_2^{-1} (record 022) | yes | PASS |
| `verify-s6-integrate-out.py` | Integrating out the auxiliary field Sigma | yes | PASS |
| `verify-sigma-effective.py` | Classical Sigma-only action (record 065) | yes | PASS |
| `verify-st4-bv-xtilde.py` | BV taxonomy (record 016) | yes | PASS |
| `verify-st6-ngh-formula.py` | Physical ghost-number formula for IBL structure maps | yes | PASS |
| `verify-stage0-translation.py` | Stage 0 convention check (record 046) | yes | PASS |
| `verify-stu-reduction.py` | Four-tachyon contact term depends on (s,t,u) alone (record 044) | no | needs data not published |
| `verify-tachyon-dilaton-quartic.py` | Tachyon-dilaton potential at quartic order | no | needs data not published |
| `verify-transformation-law.py` | Direct test of the off-shell gluing recipe (record 097) | no | needs data not published |
| `verify-truncation-structure.py` | Algebra of finite-field truncations (record 057) | yes | PASS |
| `verify-v3prime-route.py` | V_3' route feasibility (record 032) | yes | PASS |

`lib/circle_gluing.py` is a helper of `verify-p22-inverse-sewing.py`; `lib/gluing_recipe.py` (helper of `verify-offshell-gluing.py`) needs data not published.
