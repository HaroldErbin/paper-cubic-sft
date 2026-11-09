# Derivation 019 — B7: the all-orders fixed-point theorem (the cubic action at all orders)

- **Task:** the all-orders formulation (the standing next step; 018 §6 spec):
  prove that scheme B's dressed tower closes at **every** order — i.e. determine the
  cubic action at all orders — using R25's sequential-Gaussianity observation as the
  induction seed.
- **Author:** Claude Fable 5, inline (no delegation), session 2026-07-08.
- **Machine check:** `codes/verify-b7-allorders.py` — **8/8 PASS (executed 2026-07-08,
  two seeds: default 20260708 and 41)**.
- **Status:** candidate **R26**. NO blind critic pass this session (critic queue = ST9,
  extended to cover R26).
- **Terminology:** project terms of art (*forced*, *dressed*, *feedback*, *Veronese
  diagonal*, *collapse*, *running vertex*) are defined in standard matching/EFT language
  in `knowledge/cubic-sft-ibl-pedagogical.tex` §sec:intro:glossary.
- **Inputs reused (not re-derived):** R1 (eq:SHS), R12 (tower counting), R15
  (moduli-free Σ-propagators), R17 (K_Ψ = V₄ − (g/5)W), R19 (W₆ dressing,
  master-equation-agnostic matching), R21 (Φ-map level-3 kernels M̃, ũ; collapse
  ũ(P) = M̃p₃), R25 (018: sequential exact Gaussianity, Ṽ₇ forced dressing, scheme
  merger, O(g⁵) gauge rotations).
- **Conventions:** physical N_gh (Σ_k even, N_gh = 2k); finite-dimensional binding for
  the algebraic layer exactly as R14/R17/R19/R21/R25 (CFT-level analytics of the kernel
  inverses = A2(iii)/T4 carve-out); e^S weight; V₄…V₉ generic totally symmetric tensors
  (no L∞ input — matching stays master-equation-agnostic, R19 §7); Σ₁ ≡ Ψ,
  P_k := Ψ^{⊗k}, a_k := g^{2k−2}/(2k)!.

---

## 0. Executive summary

> **Revision note (2026-07-08, post blind critic).** Blind critic pass
> (`agent/reports/critic-b7-allorders-20260708T202600.md`, Opus): REVISE, no Fatal —
> every load-bearing chain hand-re-derived correct. Fixes applied in this revision:
> **S1** truncation remainder corrected O(g^{2K+2}) → O(g^{2K}) (match through
> O(g^{2K−1}), consistent with the script's slope-8 check at K=4) here, in the ledger
> and in the note; **C1** the §0 recursion box repaired (spurious +d_n/n! term
> removed; §4 was already correct); **C3** presentation-independence scoped to its
> independent evidence (level 3); **C4** shared-parent hypothesis lifted into the
> theorem statement; **C5/M3** headline softened to "a cubic action … unique up to
> Veronese-diagonal-preserving presentation freedom (formal power series, algebraic
> layer)"; **M1** hollow homogeneity sub-check in check 6 replaced by a genuine
> linearity test (script re-run, 8/8 PASS); **M2** the §4 mismatch definition now
> states the odd-coupling exclusion explicitly.

**A cubic action exists at all orders — unique up to Veronese-diagonal-preserving
presentation freedom — and its construction is a mechanical recursion** (a formal
power-series statement at the finite-dimensional algebraic layer, as R17–R25). Three
structural facts, then the theorem:

1. **Jacobi form (§1).** The scheme-B action eq:Sdrallorders is **jointly quadratic in
   the entire auxiliary tower** (Σ₂,…,Σ_K) — stronger than 018's "sequentially
   Gaussian". Its Hessian is **block-tridiagonal** (a Jacobi operator): diagonal blocks
   = the Ψ-dressed kinetics M̂_k = M̃_k − (g/(2k+1))T_{2k+1}(·,·,Ψ), off-diagonal
   blocks = the source maps L_k(Ψ), and the only inhomogeneity is the k = 2 source
   ũ₂ = V₄(·,Ψ^{⊗2}).

2. **The effective action is one Gaussian with a continued-fraction kernel (§2).**
   $$ S(\text{saddles}) = \tfrac12 V_2 + \tfrac{g}{3!}V_3
      + \frac{g^2}{4!}\,\tilde u_2^{\top}\hat H_2(g,\Psi)^{-1}\tilde u_2,\qquad
      \hat H_k = \hat M_k - g^2\,\tfrac{(2k)!}{(2k+2)!}\,
      L_{k+1}^{\top}\hat H_{k+1}^{-1}L_{k+1} $$
   (nested Schur complements = an operator continued fraction). Closure
   eq:closuredef becomes the **fixed-point equation**: the full classical
   closed-string effective action equals the value of a single exact Gaussian in Σ₂.

3. **Telescoping contact lemma (§3).** Level-k data first enter the g-expansion at
   order g^{2k−2}; at orders g^{2k−2}, g^{2k−1} they enter **only through the Veronese
   diagonals** T_{2k}(Ψ^{2k}), T_{2k+1}(Ψ^{2k+1}), linearly, with coefficients exactly
   1/(2k)! and 1/(2k+1)! — because the rung factors telescope,
   (1/4!)·(4!/6!)(6!/8!)⋯((2k−2)!/(2k)!) = 1/(2k)!, and the collapse identity
   ũ_j(P_{j−1}) = M̃_jP_j pins every flank to the Veronese at leading order.

4. **Theorem (§4): the diagonal recursion**
   $$ \boxed{\; T_n = -\,n!\,\mathrm{Pol}\big(A_{n-2}\big),\qquad
      A_{n-2}(\Psi) = [g^{n-2}]\big(S_{<n}(\text{saddles}) - S_{\rm eff}\big)
      \;} $$
   (the previous tower's order-n mismatch against the FULL target — the geometric
   V_n re-enters through the polarization, so equivalently d_n := T_n(Ψ^n) =
   V_n(Ψ^n) − n!·Pol(feedback); the new diagonal cancels the mismatch) is
   **always solvable** (A_{n−2} is a homogeneous degree-n polynomial in Ψ, so a
   symmetric tensor with that diagonal exists by polarization), **unique in the
   diagonal** (linear response with coefficient 1/n!, check 4), and **triangular**
   (order n never disturbs orders < n, check 3). Hence eq:Sdrallorders closes at every
   order: as a formal power series in g the identity eq:closuredef holds exactly, and
   at every finite truncation K the on-shell value is a closed-form rational function
   of g matching S_eff through O(g^{2K−1}) with O(g^{2K}) remainder — the first
   unmatched order needs the absent level K+1 (check 2: log-slope 8.015 at K = 4,
   i.e. remainder g⁸). All geometric vertices V_n enter the action **only
   through the forced diagonals**; everything off-diagonal is presentation freedom
   that feeds forward and is re-absorbed by the recursion (check 5; independent
   cross-check at level 3, see §4 point 3).

5. **Gauge at all orders (§5):** the exact completed square
   S = S(saddles) + Σ_k(−a_k)Ĥ_k(Y_k,Y_k) holds off-shell at every K, so the gauge
   laws are the kernel rotations δY_k = −½Ĥ_k⁻¹(δĤ_k)Y_k for every k, giving
   δS = δ[S(saddles)] **exactly** (check 6, 8.9e-16; falsification legs match).
   Homogeneous, no independent parameters — R18's pattern now at all orders.

6. **The O(g⁶) instance (018 §6 spec) is settled en passant (§6):** the k = 4 pair
   {(4,4),(4,3,1)} with source ũ₄(Σ₃) closes orders g⁶ and g⁷ with forced diagonals
   (check 2); the source is forced (zeroing it leaves exactly the A₆ deficit, check 7)
   and **uses Σ₃** (∂Σ₄*/∂Σ₃ = Ĥ₄⁻¹L₄ ≠ 0) — the tower expectation
   Σ_k ↔ (Ṽ_{2k}, Ṽ_{2k+1}) holds at k = 4, and by the theorem at every k.

## 1. The Jacobi form

The scheme-B ansatz (eq:Sdrallorders, truncated at K; shared ½V₂ + gV₃/3!
suppressed):

$$ S_K = \sum_{k=2}^{K}\Big[ a_k\big(-\tilde M_k(\Sigma_k,\Sigma_k)
   + 2\langle\tilde u_k(\Sigma_{k-1}),\Sigma_k\rangle\big)
   + \frac{g^{2k-1}}{(2k+1)!}\,T_{2k+1}(\Sigma_k,\Sigma_k,\Psi)\Big], $$

with ũ_k(Σ_{k−1}) = L_k(Ψ)Σ_{k−1} linear (one Ψ strand, partition 2k = k+(k−1)+1) and
ũ₂ = V₄(·,Ψ^{⊗2}). Every term is at most quadratic in the tower **jointly**: kinetics
and odd couplings are (Σ_k,Σ_k) bilinears (the odd (k,k,1) coupling has Ψ in the third
slot — this is what "canonical scheme B" buys), sources are (Σ_k,Σ_{k−1}) bilinears.
So S_K = −𝒜(Σ,Σ) + 2⟨𝔟,Σ⟩ with 𝒜 block-tridiagonal,

$$ \mathcal A_{kk} = a_k\hat M_k,\quad
   \hat M_k = \tilde M_k - \tfrac{g}{2k+1}T_{2k+1}(\cdot,\cdot,\Psi),\quad
   \mathcal A_{k,k-1} = -a_kL_k,\qquad
   \mathfrak b = (a_2\tilde u_2, 0, \dots, 0). $$

018's "sequential exact Gaussianity" is the block-Cholesky elimination of this Jacobi
operator; the joint-quadratic statement is the cleaner (and slightly stronger)
formulation. Verified: block solve == nested Schur == direct action evaluation at real
and complex g, machine precision (checks 0, 3).

## 2. The on-shell value: one Gaussian, an operator continued fraction

Eliminating top-down (Schur complements on the Jacobi form):

$$ \hat H_K = \hat M_K,\qquad
   \hat H_k = \hat M_k - g^2\,\frac{(2k)!}{(2k+2)!}\,
   L_{k+1}^{\top}\hat H_{k+1}^{-1}L_{k+1}
   \quad (k = K{-}1,\dots,2), $$

$$ \boxed{\; S_K(\text{saddles}) = \tfrac12V_2 + \tfrac{g}{3!}V_3
   + \frac{g^2}{4!}\,\tilde u_2^{\top}\hat H_2^{-1}\tilde u_2 \;} $$

— since 𝔟 is supported in the k = 2 block, the whole tower's on-shell value is the
(2,2) resolvent block of the Jacobi operator evaluated on the quartic source. The
factor (2k)!/(2k+2)! = a_{k+1}/a_k (k = 2: 1/30 = 018's K̂ coefficient; k = 3: 1/56).
Saddles chain down as Σ_k* = Ĥ_k⁻¹L_kΣ_{k−1}*, Σ₂* = Ĥ₂⁻¹ũ₂, each = P_k + O(g)
(check 2, deviation slope 1.000). K = 2 sanity: Ĥ₂ = V₄ − (g/5)W reproduces R17's
c₂ = V₄(Ψ⁴)/4!, c₃ = V₅(Ψ⁵)/5!, c₄ = vᵀV₄⁻¹v/600 analytically (check 0).

**Convention note (bug class worth recording):** define the order-n mismatch
A_{n−2}(Ψ) := [g^{n−2}](value − S_eff) against the FULL target (V_n included). Then
the new kernel is T_n = −n!·Pol(A_{n−2}); the geometric V_n reappears through the
polarization (Pol(A) contains −V_n/n!), i.e. T_n = V_n − n!·Pol(feedback). Writing
"V_n − n!Pol(A_{n−2})" with the full-target A double-counts V_n (caught by check 2's
first run).

## 3. The telescoping contact lemma

**(a) Collapse (parent lemma).** If M̃_k and ũ_k are the (k|k) and (k|k−1,1)
restrictions of ONE 2k-linear parent T_{2k}, then ũ_k(P_{k−1}) = M̃_kP_k identically
in Ψ — trivially, both sides are T_{2k}(·, Ψ^{2k−k}) with all non-Σ_k slots at Ψ. No
symmetry of the parent is needed beyond the shared parent itself; in particular
**block composites (R21's ΦᵀV₄⁻¹Φ) and fully symmetric polarizations qualify
equally** (checks 0, 2: both collapse identities at 1e-14).

**(b) First-entry order.** Each rung k → k+1 of the continued fraction costs g²
(the Schur correction), so level-k data first touch the value at
g²·(g²)^{k−2} = g^{2k−2}; the odd T_{2k+1} first enters at one more power (its (g/(2k+1))
dressing of M̂_k).

**(c) Diagonal-only, coefficient 1/n!.** At the first-entry order every flank of the
level-k insertion is pinned to the Veronese: ũ₂ᵀV₄⁻¹ = P₂ᵀ, and inductively
Ĥ_j⁻¹ũ_j(P_{j−1}) = P_j + O(g) by (a). The level-k leading contribution is therefore

$$ a_k\,\tilde u_k(P_{k-1})^{\top}\tilde M_k^{-1}\tilde u_k(P_{k-1})
   = a_k\,(\tilde M_kP_k)^{\top}\tilde M_k^{-1}(\tilde M_kP_k)
   = a_k\,T_{2k}(\Psi^{2k}), $$

and the prefactor chain telescopes: (1/4!)·(4!/6!)(6!/8!)⋯((2k−2)!/(2k)!) = 1/(2k)!.
For the odd insertion, M̂_k⁻¹ = M̃_k⁻¹ + (g/(2k+1))M̃_k⁻¹T_{2k+1}M̃_k⁻¹ + O(g²)
sandwiched between Veronese flanks gives +g^{2k−1}T_{2k+1}(Ψ^{2k+1})/(2k+1)!.
Machine form (check 4): perturbing T₈ by ε a^{⊗8} shifts c₆ by exactly
ε(a·Ψ)⁸/8! and leaves c₂…c₅ bit-identical; same for T₉ at c₇.

## 4. The theorem

**Theorem (all-orders closure of the dressed tower).** Let {V_n}_{n≥2} be arbitrary
symmetric tensors on a finite-dimensional H, generic in the sense that the nested
kernels Ĥ_k(g,Ψ) are invertible in a neighbourhood of g = 0 (the all-orders
auxiliarity hypothesis; CFT status = the standing carve-out). **Hypothesis
(shared-parent presentation class):** at every level k the kinetic M̃_k and the
source ũ_k are the (k|k) and (k|k−1,1) restrictions of ONE 2k-linear parent T_{2k}
(§3(a)); block composites and full polarizations both qualify, but presentations
with independent kinetic/source parents are outside the theorem (they break the
collapse and the diagonal-only first entry). Then there exist parents
{T_n}_{n≥4} — T₄ = V₄, T₅ = V₅, and for n ≥ 6 recursively

$$ T_n := -\,n!\,\mathrm{Pol}\big(A_{n-2}\big),\qquad
   A_{n-2}(\Psi) = [g^{n-2}]\Big(S_{\text{prev}}(\text{saddles})
   - S_{\rm eff}\Big), $$

where S_prev is the previous tower built from **T₄,…,T_{n−1} only** (for odd
n = 2k+1 the top level k carries its kinetic T_{2k} but NOT the odd coupling being
solved for; for even n = 2k the level-k pair is absent entirely) — such that the
scheme-B action eq:Sdrallorders satisfies the closure condition eq:closuredef as a
formal power series in g; at each truncation K the identity is an exact
rational-in-g statement with O(g^{2K}) remainder (matched through O(g^{2K−1}); the
first unmatched order is the absent level K+1's first entry g^{2(K+1)−2} = g^{2K}).
Moreover:

1. **Existence** is automatic: A_{n−2} is a homogeneous degree-n polynomial in Ψ
   (scaling argument: under Ψ → tΨ, Σ_k → t^kΣ_k, g → g/t every term of S_K scales as
   t², so [g^m](value) is homogeneous of degree m+2), hence Pol(A) exists in char 0.
2. **The diagonal is forced**: by §3(c) the order-n coefficient responds to T_n
   linearly through its diagonal with coefficient 1/n!, so d_n is pinned; and the
   recursion is well-founded because order n depends only on {T_m, m < n} plus d_n
   (triangularity, §3(b) + check 3).
3. **Everything else is presentation freedom** (within the shared-parent class): any
   parents with the forced diagonals close; different choices (fully-polarized vs
   block-composite kernels) change the higher feedbacks A_m (m > n−2) and hence the
   higher forced diagonals — the freedom feeds forward and is re-absorbed (check 5:
   tower A with canonical R21/R25 level-3 kernels and tower B with fully-polarized
   kernels both close to 1e-15; their T₆'s share the diagonal, differ as tensors by
   O(1), and their forced d₇'s differ). **Evidence scope (critic C3):** the genuinely
   independent cross-check is at level 3 — tower A's kernel is R21's block composite
   ΦᵀV₄⁻¹Φ (built from V₅, V₆, no fitting) vs tower B's polarized kernel, agreeing on
   the Veronese diagonal while differing as tensors; at level 4 both towers use the
   same polarization-fit machinery, so those legs are self-consistency of the fit,
   not an independent second construction.
4. **Fixed-point form**: in the K → ∞ formal limit,
   $$ S_{\rm eff}[\Psi] - \tfrac12V_2 - \tfrac{g}{3!}V_3
      = \frac{g^2}{4!}\,\tilde u_2^{\top}\hat H_2(g,\Psi)^{-1}\tilde u_2, $$
   with Ĥ₂ the infinite continued fraction — every [gᵐ] of which stabilizes at finite
   K. The entire interaction content of closed-string perturbation theory (tree-level,
   classical) is carried by the forced Veronese diagonals of the tower kernels.

*Proof.* §1 (Jacobi form) + §2 (Schur value) + §3 (contact lemma) + induction on n:
assume T₄,…,T_{n−1} chosen so the mismatch is O(g^{n−2}). The order-(n−2) coefficient
of the new tower (with T_n added at its level) is A_{n−2} + d_n/n! by §3(c) and
linearity; setting d_n = −n!A_{n−2}··· i.e. T_n = −n!Pol(A_{n−2}) cancels it; lower
orders are untouched by §3(b). Homogeneity (point 1) guarantees Pol exists. ∎

The theorem elevates 018 §6's conjecture to a proof at the algebraic layer, and
replaces "check order n" by "evaluate one polynomial and polarize" — the recursion is
mechanical (the verify script executes it end-to-end for n = 6…9 in under a second).

## 5. Gauge laws at all orders

Block-Cholesky off-shell: with Y_k := Σ_k − Ĥ_k⁻¹L_kΣ_{k−1} (conditional saddles;
Y₂ = Σ₂ − Ĥ₂⁻¹ũ₂),

$$ S_K = S_K(\text{saddles}) + \sum_{k=2}^{K}(-a_k)\,\hat H_k(Y_k,Y_k)
   \qquad\text{exactly, off-shell} $$

(check 6, 4e-18). Demanding δ[deviation part] = 0 under arbitrary δΨ gives the
kernel rotations **at every level**,

$$ \delta Y_k = -\tfrac12\,\hat H_k^{-1}(\delta\hat H_k)\,Y_k,\qquad k = 2,\dots,K, $$

with δĤ_k assembled from δM̂_k = −(g/(2k+1))T_{2k+1}(·,·,δΨ), δL_k = L_k(δΨ) and the
recursion. Then δS_K = δ[S_K(saddles)] exactly (check 6: 8.9e-16 relative, analytic
directional derivatives; dropping δY₄ or δY₂ leaves exactly −a_kY_kᵀ(δĤ_k)Y_k, both
matched at 1e-9). Homogeneous (δY ∝ Y), no independent parameter at any level — the
R18/R21/R22/R25 pattern is now a theorem for the whole tower: the auxiliary sector is
pure saddle-tracking + contractible rotations (R22's BV class, field-dependent-kinetic
corner at every level from the odd couplings).

## 6. What this settles

- **O(g⁶) + O(g⁷) closure (the 018 §6 spec):** the k = 4 pair with kinetic from T₈,
  source ũ₄(Σ₃) (which **uses Σ₃**: ∂Σ₄*/∂Σ₃ = Ĥ₄⁻¹L₄ ≠ 0, check 7) and odd (4,4,1)
  coupling from T₉ closes both orders with forced diagonals (check 2). The tower
  assignment Σ_k ↔ (Ṽ_{2k}, Ṽ_{2k+1}) holds at k = 4 and, by the theorem, at every k.
- **The scheme question is closed at all orders:** scheme A/B/C and the partition
  menus are all members of the one closure family classified by point 3 of the
  theorem — the diagonal is physics, the rest is bookkeeping. Canonical member =
  the jointly-Gaussian (k,k,1) tower (this derivation); it is the unique shape for
  which the value is a closed-form continued fraction and the gauge laws are explicit
  rotations at every order.
- **"More composite, not more ad hoc" is now a theorem:** eq:runningV's rule (deficit
  vertex = n-th Veronese derivative of the eliminated lower action) IS the forced
  diagonal recursion.

## 7. Established vs open

**Established (machine-checked, finite-dim algebraic layer, generic non-L∞ tensors,
two seeds, 8/8):**
(i) Jacobi form; block solve == continued fraction == direct action, real and complex
g (checks 0, 3); (ii) collapse for block and polarized parents (checks 0, 2);
(iii) the diagonal recursion executes n = 6…9 and closes c₂…c₇ at 1e-15 with O(g⁸)
remainder, slope 8.015 (check 2) — NOTE (critic C2): the c₂…c₇ = target numbers are
a self-consistency check of the fit (T_n is constructed to cancel the mismatch); the
independent weight is carried by the fit validation at fresh points (homogeneity/
existence), the diag/n! response (check 4), triangularity (check 3), and the
finite-g slope; (iv) diagonal response exactly diag/n!, lower
orders bit-identical (checks 3, 4); (v) presentation freedom feeds forward and is
re-absorbed (check 5); (vi) all-orders gauge rotations, exact equality, falsification
legs (check 6); (vii) level-4 source forced and Σ₃-dependent (check 7).

**Open / carve-outs:**
(a) CFT-level analytics: invertibility/boundedness of the nested Ĥ_k(g,Ψ) chain — the
all-orders auxiliarity condition (one condition per level; strictly extends
A2(iii)/T4); region identification inherited (R14(b) language);
(b) **convergence in g of the infinite continued fraction is NOT addressed** — the
theorem is order-by-order (formal series); at fixed truncation everything is exact
rational. The perturbative-branch caveats (R19 (g)) apply;
(c) non-Gaussian partition realizations at n ≥ 8 ((3,3,2)-type couplings): conjectured
to close as free partition splits by the R25 pattern (Veronese diagonal is all that
matters), but they break the Jacobi form and are NOT covered by the theorem or the
script;
(d) kernel uniqueness at fixed diagonal is a freedom class, not a defect — but the
*canonical strand-local* representative at levels ≥ 4 (the running-composite form of
the T₈, T₉ parents, extending R25 §4) was not constructed explicitly here (the script
uses polarized parents at level 4);
(e) blind critic pass — queued (ST9, now R16/R21–R26);
(f) quantum/genus tower excluded (excluded by scope).

**Result → candidate R26.** The cubic action exists at all orders: scheme B's tower
with kernels fixed by the forced-diagonal recursion satisfies eq:closuredef as a
formal power series (exact rational at every truncation), the full effective action
is one Gaussian with an operator-continued-fraction kernel, and the gauge structure
is explicit kernel rotations at every level. The O(g⁶) instance (018 §6) is
confirmed en passant.
