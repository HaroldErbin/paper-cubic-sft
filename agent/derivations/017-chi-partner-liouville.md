# 017 — The wrong-sign partner χ: Liouville-type re-localisation of the feedback

**Date:** 2026-07-07 (Fable, inline — final-session leg 2).
**Machine check:** `codes/verify-chi-partner.py` — **10/10 PASS (executed 2026-07-07)**,
2 seeds, generic (non-L∞) tensors, joint (Σ,χ) Newton saddle on the symmetric subspace,
Richardson + scaling-exponent tests.
**Status: R24 (promoted 2026-07-07).** **Blind critic pass DONE 2026-07-09 (Opus,
ST9): ACCEPT — 0 Fatal, 0 Serious.** The critic hand-re-derived the forced ratio
b²/a = 4 (coefficient chain 4!/(5!)² = 1/600), the sign-flip mechanism, the O(g⁴)
closure of S₄^χ incl. its exact match with R19's −(6/5)𝒞 bookkeeping, the λ-twist
mini-lemma, and eq:lightcone/eq:saddlesum — all confirmed; the decisive script check
judged genuine and non-circular. Concerns C1–C3 + minors applied 2026-07-09 (tex
kernel −K_Ψ⊕+V₄ precision; boost breaking at O(g³) not O(g⁴); the strong-R20
falsification conditioned on admitting indefinite-signature auxiliaries; M1/M4
notes below). Report `agent/reports/critic-r24-chi-20260709T130000.md`.
Scope: tree-level, on-shell matching at generic off-shell Ψ, through
O(g_s⁴); finite-dim algebraic layer (A2(iii)/T4 carve-out as always).

## 1. The question and the answer

The feedback $vK_\Psi^{-1}v$ recalls the induced gravitational action in 2d,
$S = R\Delta^{-1}R$, obtained by integrating the Liouville field out of
$S=\phi\Delta\phi+R\phi$. Is there a similar mechanism here? Is the new field
related to the gauge-fixed part of Σ, or is it another field?

**Answer, part 1 (dictionary — exact).** "Exact" refers to the *mechanism* (Gaussian
elimination of a linearly-sourced field producing source·kernel⁻¹·source), not to a
numerical identity between the two theories' induced actions [critic M4]. The analogy
is precise and is already realised by the deviation field. In the exact rewriting (R17)
$S_3=S^{(5)}_{\rm eff}-\tfrac{g^2}{4!}K_\Psi(\tilde X,\tilde X)+\tfrac{g^4}{600}vK_\Psi^{-1}v$:

| 2d gravity | here |
|---|---|
| Liouville field φ | deviation $\tilde X=\Sigma-\Sigma_*(\Psi)$ |
| kinetic operator Δ | dressed kernel $K_\Psi=V_4-\tfrac{g}5 V_5(\cdot,\cdot,\Psi)$ |
| curvature source R (metric-dep.) | quintic source $v=V_5(\cdot,\Psi^{\otimes2},\Psi)$ (cubic in Ψ) |
| induced nonlocal $R\Delta^{-1}R$ | feedback $\tfrac{g^4}{600}vK_\Psi^{-1}v$ |

Integrating the linearly-sourced Gaussian field out *produces* the nonlocal composite —
same mechanism, same structure.

**Answer, part 2 (the constructive converse — NEW, verified).** In 2d gravity one also
runs the dictionary backwards: the nonlocal Polyakov action is *localised* by
introducing φ. Here the object to remove is the feedback *overshoot* (it must be
SUBTRACTED at O(g⁴), which is why R19 needs the composite $-\tfrac65\mathcal C$ inside
$W_6$). Subtraction = localisation by a **wrong-sign** partner: a second auxiliary
$\chi\in\Sym^2\mathcal H_0$ ($N_{\rm gh}=4$, even — same slot as Σ) with **elementary
vertices only**:

$$S_\chi = +\frac{g^2}{4!}\,a_\chi V_4(\chi,\chi) + \frac{g^3}{5!}\,b_\chi V_5(\chi,\Sigma,\Psi),
\qquad \boxed{b_\chi^2/a_\chi = 4}\ \ \text{(forced)},\ (a_\chi,b_\chi)=(1,2).$$

Only the invariant *ratio* $b_\chi^2/a_\chi$ is forced [critic M1]: the rescaling
$\chi\to\lambda\chi$ sends $(a_\chi,b_\chi)\to(\lambda^2 a_\chi,\lambda b_\chi)$ and
leaves $b_\chi^2/a_\chi$ fixed, so $(1,2)$ is the field-normalisation choice that
realises the universal HS 1:2 ratio, not an independently forced pair.

Note the PLUS sign of the kinetic term (opposite to Σ's $-\tfrac{g^2}{4!}V_4(\Sigma,\Sigma)$)
and that every term is cubic in fields (the coupling is $\chi\Sigma\Psi$ trilinear —
using $v(\chi)=V_5(\chi,\Psi^{\otimes2},\Psi)$ directly would be quartic and is NOT used).
χ has no $V_4(\chi,\Psi^{\otimes2})$ source: it couples to the theory only through the
$O(g^3)$ trilinear vertex, so its on-shell value starts at $\chi_*=-\tfrac{g}{10}b_\chi
V_4^{-1}v+O(g^2)$ and its sector contributes $-\tfrac{b_\chi^2}{4a_\chi}\cdot
\tfrac{g^4}{600}\,vV_4^{-1}v+O(g^5)$ on-shell — cancelling the R17 feedback exactly when
$b_\chi^2/a_\chi=4$.

**Consequence (the headline):** the action with content $(\Psi,\Sigma_2,\chi)$ and PURE
GEOMETRIC vertices
$$S^{\chi}_4 = S_{\rm HS} + \frac{g^3}{5!}V_5(\Sigma,\Sigma,\Psi)
+ \frac{g^2}{4!}V_4(\chi,\chi) + \frac{2g^3}{5!}V_5(\chi,\Sigma,\Psi)
+ \frac{g^4}{6!}V_6(\Sigma,\Sigma,\Sigma)$$
matches $S^{(6)}_{\rm eff}$ on-shell through O(g⁴) — **no composite $W_6$, no dressed
$\tilde V_6$, no $\Sigma_3$**. All six checks of the script confirm this on generic
tensors (master-equation-agnostic, like R19/R20).

## 2. Relation to R20 (consistency, not contradiction)

R20 proved: no elementary presentation with content $\Sigma_2\oplus\Sigma_3$ closes; the
strong form ("no elementary presentation whatsoever") was explicitly a conjecture
(critic finding F5 narrowed the scope). The χ-scheme **settles the strong form in the
NEGATIVE — provided indefinite-signature (negative-kinetic) auxiliaries are admitted
as an "elementary presentation"** [critic C3; the falsification inherits the
tree-level-only unitarity caveat of §3 as part of its scope]: an elementary
presentation exists, with the third field being not the next
symmetric power $\Sigma_3\in\Sym^3$ but a *wrong-sign partner in the same* $\Sym^2$
*slot*. R20's mechanism is untouched — a $\Sigma_3$-exchange is quadratic in Σ₂ and
$V_6$-built, so it can never reach the feedback; the χ-exchange is *also* quadratic in
Σ₂ but $V_5V_4^{-1}V_5$-built with a sign-flipped propagator, which is exactly what the
feedback subtraction needs. The trade is not $V_4^{-1}\to V_6^{-1}$ (impossible, R20)
but $+V_4^{-1}\to$ paired $\pm V_4^{-1}$ (possible).

## 3. What χ is and is not (relation to the gauge-fixed part of Σ)

- **Parity bookkeeping:** χ pairs through $V_4$ (4-punctured-sphere saturation
  $4+4=8$), so $N_{\rm gh}(\chi)=4$, Grassmann-even — the SAME quantum numbers as Σ.
  It is therefore NOT the $c_0$-type up-component $\Sigma_\uparrow$ of an unconstrained
  two-string field (that component would sit at odd $N_{\rm gh}=3$), and NOT R18's
  ghost-5 partner Π (which pairs via ω₂ at saturation 10). At the parity level the
  answer to the gauge-fixed-part question is: **yet another field**.
- **Signature structure:** the joint quadratic form of the $(\tilde X,\tilde\chi)$
  sector is split-signature, $-K_\Psi\oplus+K_\Psi$ at leading dressing; in light-cone
  combinations $\Pi_\pm=\tilde X\mp\tilde\chi$ it is purely off-diagonal
  $\sim K_\Psi(\Pi_+,\Pi_-)$ — formally the shape of a BV/quartet (contractible-pair)
  sector and *suggestive* of an already-gauge-fixed enlarged theory (the T6-bis lead),
  now with a $V_4$-type (not $\hat Q$-type) off-diagonal kernel. Whether an enlarged
  gauge symmetry rotates $\Pi_\pm$ (making the negative-norm direction harmless as a
  gauge artifact) is OPEN and is precisely a T6-bis-type question.
- **Unitarity caveat (honest):** χ has negative kinetic energy. As a *contact*
  auxiliary (kinetic $V_4$, no $1/L_0^+$ pole, no propagating states — R14/R15
  telescoping applies verbatim with a sign) it produces no negative-norm asymptotic
  states at tree level; the formal Gaussian is signature-indifferent (R14's det
  clause). But its status in the quantum theory (loops, BV quantisation) is open, and
  the gauge/BV analysis of the χ-sector has NOT been done (ST7).

## 4. Machine verification (script summary)

`codes/verify-chi-partner.py`, N=4, generic symmetric $T_2..T_6$, generic Ψ, 2 seeds.
On-shell-in-auxiliaries action at off-shell Ψ = generating function of all trees, so the
Richardson test in g covers contact reproduction AND exchange-class cancellation:
1. no-χ baseline: mismatch/g⁴ → $+vV_4^{-1}v/600$ (rel. err. 3e-5) — R19/R20 residual;
2. χ(1,2): mismatch/g⁴ → 0 (4e-5 of target, seed 7; 8e-4 seed 23);
3. b=1: residual → $(1-b^2/4)\cdot$target (rel. err. 3e-5) — coefficient forced;
4. O(g³) safety: 5-pt matching uncontaminated (χ-exchange starts at O(g⁴));
5. scaling exponent of the χ(1,2) residual ≈ 0.93 ⇒ mismatch = O(g⁵).

Numerics notes (critic M2/M3, 2026-07-09): the ×20 seed spread in check 2 (4e-5 vs
8e-4, pass gate 1e-2) is joint-saddle conditioning noise rather than clean Richardson
O(g₀²) scaling — the scaling leg (check 5) is the safeguard against a hidden constant
residual; the quoted "1e-3 level" is a performance number, not the pass threshold. The
slope 0.93 vs the ideal 1.0 reflects finite-window O(g⁶) contamination/saddle noise
over the fit range [6e-3, 3e-2]; its role is to exclude the slope-0 signature of
non-closure, which it does comfortably.

## 5. Open (→ ST7 side task + all-orders section)

(a) Off-shell exact rewriting of $S^\chi_4$ (split-signature completion of squares) and
the gauge law of the χ-sector (expected: contractible-pair law, R22 class; is δχ also
saddle-tracking + homogeneous rotation?). (b) O(g⁵)+ extension: the O(g⁵) feedback
$A_5$ has two composite structures; which χ-couplings (e.g. $V_6(\chi,\Sigma,\Sigma)$,
$V_6(\chi,\chi,\Sigma)$) cancel them, and does ONE χ suffice to all orders, or does the
wrong-sign tower mirror the Σ-tower? (c) BV/quartet interpretation and the T6-bis
connection (is there an enlarged gauge symmetry rotating $\Pi_\pm$?). (d) Reality of the
χ-sector (expected $\chi^\ddagger=\chi$, same argument as Σ). (e) Quantum status of the
negative-norm direction.
