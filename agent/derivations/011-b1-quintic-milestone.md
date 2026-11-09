# Derivation 011 — B1: the O(g_s³) quintic milestone of Route B

- **Task:** Phase B, B1 (state file resume sequence; Fable note §7 item 2): construct the
  O(g_s³) step of the cubicization tower explicitly — fix the coefficient of
  V₅(Σ,Σ,Ψ), enumerate the diagrams, verify moduli bookkeeping, extend the gauge law.
  This is "the first genuine test beyond the Gaussian identity" (R12's dynamical
  closure at the first nontrivial order).
- **Author:** Claude Fable 5, inline (no delegation), session 2026-07-03.
- **Machine check:** `codes/verify-b1-quintic.py` — **9/9 PASS (executed 2026-07-03)**.
- **Status:** candidate **R17**. No critic pass was run this session; the critic
  dispatch is listed in `agent/state/opus-side-tasks.md`.
- **Inputs reused (not re-derived):** R1 (eq:SHS), R7 (ω₂ graded-symmetric, physical
  grading), R8/R9/R10 (Gaussian identity), R11 (composite law), R12 (counting +
  triangularity), R14 (Σ-Feynman rules, telescoping conventions), R15 (V₄⁻¹ status),
  H2 closed (ledger Annotation), (5.1) defused (kernel quotient, R13).
- **Conventions:** physical N_gh grading (Ψ at 2, Σ at 4, both even; δΨ even);
  finite-dimensional model binding for the combinatorial/algebraic layer exactly as in
  R14 (CFT-level analytics stay with A2(iii)/T4); e^S path-integral weight; V₄, V₅
  totally graded-symmetric geometric vertices (H2 closed for every vertex family).

---

## 0. Executive summary

Let P ≡ Ψ⊗², X ≡ Σ − P. The unique cubic O(g_s³) completion of the HS action is

$$
S_3 \;=\; S_{\rm HS} \;+\; \frac{g_s^3}{5!}\,V_5(\Sigma,\Sigma,\Psi),
\tag{B.1}
$$

with coefficient **1/5!, forced** (§2). The central structural result is an **exact
rewriting** (identity in the fields, all orders in g_s):

$$
\boxed{\;
S_3 \;=\; S^{(5)}_{\rm eff}
\;-\;\frac{g_s^2}{4!}\,K_\Psi(\tilde X,\tilde X)
\;+\;\frac{g_s^4}{600}\,v\,K_\Psi^{-1}v,
\;}
\tag{B.2}
$$

where

- $S^{(5)}_{\rm eff}=\tfrac12V_2+\tfrac{g_s}{3!}V_3+\tfrac{g_s^2}{4!}V_4(P,P)
  +\tfrac{g_s^3}{5!}V_5(P,P,\Psi)$ is the quintic-truncated closed SFT action;
- $K_\Psi := V_4 - \tfrac{g_s}{5}\,V_5(\cdot,\cdot,\Psi)$ is the **Ψ-dressed kinetic
  kernel** on Sym²H₀ (a g_s-small perturbation of V₄; invertible on the R13 quotient
  for small g_s);
- $v := V_5(\cdot,P,\Psi)$ (a Sym²-covector, **cubic in Ψ**: quadratic through $P=\Psi^{\otimes2}$ times one explicit Ψ — consistent with $vK_\Psi^{-1}v$ being a 6-point interaction);
- $\tilde X := X - \tfrac{g_s}{5}K_\Psi^{-1}v$ is the completed-square variable, so the
  Σ-EOM is exactly $\tilde X=0$, i.e.
  $\Sigma_* = \Psi^{\otimes2} + \tfrac{g_s}{5}K_\Psi^{-1}V_5(\cdot,\Psi^{\otimes2},\Psi)$;
- the last term of (B.2) — the **feedback** — is Σ-independent, starts at O(g_s⁴)
  (a 6-point effective interaction), and is the exact, explicit form of R12's
  "feedback enters only at O(g_s⁴)".

Consequences, each machine-checked:

1. **On-shell matching at O(g_s³) with no unwanted terms:** $S_3(\Psi,\Sigma_*(\Psi)) =
   S^{(5)}_{\rm eff}(\Psi) + \tfrac{g_s^4}{600}vK_\Psi^{-1}v$ exactly. All tree
   amplitudes of $S_3$ agree with those of $S^{(5)}_{\rm eff}$ through O(g_s³).
2. **Diagram enumeration (§3):** at O(g_s³) (= the 5-point tree level) the HS-side
   diagrams are exactly three classes — (V₃)³ chains (shared), V₃×[Σ-exchange]
   (collapses to V₃×V₄ by R14), and the new [source–Σ-prop–V₅–Σ-prop–source] double
   telescoping, which lands on the V₅ contact kernel with coefficient exactly 1
   (15 assignments × g_s³/15). **There are no unwanted diagrams at this order** — the
   first candidates (V₅–V₃ trees with an internal Ψ line; V₅–Σ-prop–V₅ trees;
   Σ-tadpole on V₅) all enter at O(g_s⁴) or at one loop.
3. **Gauge law (§4):** the composite law receives a forced O(g_s) correction. With
   $\delta\tilde X = \tfrac{g_s}{10}\,K_\Psi^{-1}V_5(\cdot,\tilde X,\delta\Psi)$ the
   dressed quadratic form in (B.2) is **exactly invariant**, and

   $$
   \delta S_3-\delta S^{(5)}_{\rm eff}
   =\delta\Big[\tfrac{g_s^4}{600}\,vK_\Psi^{-1}v\Big]
   \tag{B.3}
   $$

   **exactly** (identity in fields, arbitrary δΨ, off-shell, no Λ-expansion) — the full
   R11 analogue at this order. Equivalently: $\hat S_3 := S_3 - {\rm feedback}(\Psi)$
   satisfies $\delta\hat S_3=\delta S^{(5)}_{\rm eff}$ exactly. Since
   $\delta S^{(5)}_{\rm eff}=O(g_s^4)$ (L∞ through ℓ₄), $S_3$ is gauge-invariant to
   the same order O(g_s⁴) as the quintic-truncated theory itself — the HS tower step
   again costs nothing. Still **no independent two-string parameter** (feeds T6,
   derivation 012).
4. **Moduli bookkeeping (§5):** inherited region by region; the Σ-propagators remain
   moduli-free kernels; V₅ enters as the single V₀,₅ block. Same carve-out language as
   R14(b).
5. **O(g_s⁴) spec (§6):** the feedback term is the precise target the V₆ step must
   absorb; written out as the next-milestone spec.

---

## 1. Setup and uniqueness of the coupling

Fields: Ψ ∈ H₀ (N_gh 2), Σ ∈ Sym²H₀ (N_gh 4), both Grassmann-even (R7/R12). The
O(g_s²) part is fixed = eq:SHS (R1). At O(g_s³) a **cubic** action can only contain a
three-field vertex; with field content {Ψ, Σ} and target V₅ the R12 counting gives the
unique partition 5 = 2+2+1, i.e. the coupling $V_5(\Sigma,\Sigma,\Psi)$. Ghost
saturation on the 5-punctured sphere: total N_gh = 6 + dim_R M₀,₅ = 6+4 = 10, and
$N_{\rm gh}(\Sigma,\Sigma,\Psi)=4+4+2=10$ ✓ (script check 8; same count as
$V_5(\Psi^5)=5\times2$). Other O(g_s³) modifications are excluded:

- $V_5(\Sigma,\Psi,\Psi,\Psi)$-type terms have ≥ 4 field slots — not cubic;
- the partition $5=3+1+1$, i.e. a cubic $V_5(\Sigma_3,\Psi,\Psi)$ with a 3-strand field
  $\Sigma_3$, is a *legitimate alternative presentation* (on-shell $\Sigma_3=\Psi^{\otimes3}$
  gives the same contact $V_5(\Psi^5)$) — it is excluded here **by the minimal field content
  {Σ₂,Ψ}**: R12 shows $\Sigma_2$ alone suffices through $V_6$, with $\Sigma_3$ first needed at
  $V_7=(3,2,2)$. So "unique" means *minimal-ansatz-unique on {Σ₂,Ψ}*, not unique across all
  multi-strand field contents;
- an O(g_s³) linear-in-Σ tadpole $g_s^3L(\Sigma)$ would shift the saddle at O(g_s) and
  contaminate the effective action / higher-point amplitudes at O(g_s³) — forbidden by
  matching to $S^{(5)}_{\rm eff}$;
- O(g_s³) corrections to the O(g_s²) kernels are forbidden by the same matching
  (given the O(g_s²) structure already fixed).

So (B.1) is the **minimal-ansatz-unique** completion (on the field content {Σ₂,Ψ}), up to
O(g_s) field redefinitions of Σ (which move terms between the presentations but not the
physics).

## 2. The exact rewriting and the coefficient

Expand $V_5(\Sigma,\Sigma,\Psi)$ around the O(g_s²) saddle, $\Sigma = P + X$:

$$
V_5(\Sigma,\Sigma,\Psi)=V_5(X,X,\Psi)+2V_5(X,P,\Psi)+V_5(P,P,\Psi).
\tag{B.4}
$$

With a general coefficient $c\,g_s^3/5!$ on the coupling,

$$
S_3-S^{(5)}_{\rm eff}
=-\frac{g_s^2}{4!}V_4(X,X)
+\frac{c\,g_s^3}{5!}\Big[V_5(X,X,\Psi)+2V_5(X,P,\Psi)\Big]
+\frac{(c-1)g_s^3}{5!}V_5(P,P,\Psi).
\tag{B.5}
$$

The last term is X-independent and survives on-shell at O(g_s³) unless **c = 1**:
matching forces the coefficient (script check 3: the residual mismatch is
$(c-1)\tfrac{g_s^3}{5!}V_5(\Psi^5)+O(g_s^4)$, verified by Richardson extrapolation in
g_s). This is the naive "replace P by Σ with the same 1/5!" — but now *derived*, and
the X-dependence in (B.5) is what carries all the dynamics.

Set c = 1. Absorb the X-quadratic V₅ term into the dressed kernel
$K_\Psi(A,B) := V_4(A,B) - \tfrac{4!}{5!}g_s V_5(A,B,\Psi)
= V_4(A,B)-\tfrac{g_s}{5}V_5(A,B,\Psi)$:

$$
S_3-S^{(5)}_{\rm eff}
=-\frac{g_s^2}{4!}\Big[K_\Psi(X,X)-\frac{2g_s}{5}\,v(X)\Big],
\qquad v:=V_5(\cdot,P,\Psi).
\tag{B.6}
$$

Completing the square with $\tilde X = X-\tfrac{g_s}{5}K_\Psi^{-1}v$ gives (B.2) with
the feedback $+\tfrac{g_s^2}{4!}\cdot\tfrac{g_s^2}{25}\,vK_\Psi^{-1}v
=+\tfrac{g_s^4}{600}\,vK_\Psi^{-1}v$. Machine check 1 verifies (B.2) as an identity in
(Σ, Ψ, g_s) to machine precision (20 random draws); check 2 verifies $\tilde X$
vanishes on the Newton-solved saddle and that the on-shell difference equals the
feedback exactly, with the correct analytic small-g_s series
$\tfrac1{600}[vV_4^{-1}v + \tfrac{g_s}{5}vV_4^{-1}WV_4^{-1}v+O(g_s^2)]$,
$W=V_5(\cdot,\cdot,\Psi)$.

**Invertibility scope.** $K_\Psi = V_4(1 - \tfrac{g_s}{5}V_4^{-1}W)$: on the R13
quotient (Σ ∈ Sym²H₀/ker V₄) and for g_s small, $K_\Psi$ is invertible whenever V₄ is,
by Neumann series — no *new* invertibility condition arises at this order beyond the
R9/R13/(5.1)-quotient package, only the same functional-analytic regularity carried
there (bounded $V_4^{-1}$ for the series; finite-dim: automatic). Note $K_\Psi$ is
field-dependent: the Σ-propagator of the O(g_s³) theory is $K_\Psi^{-1}$, whose
expansion in g_s generates precisely the [Σ-prop–V₅(·,·,Ψ)–Σ-prop] insertions of §3.

## 3. Diagram enumeration at O(g_s³) (5 points, tree)

Power counting: n-point tree amplitudes scale as $g_s^{n-2}$; O(g_s³) = the 5-point
tree level. Σ-lines can terminate only on the source vertex
$\tfrac{2g_s^2}{4!}V_4(\Sigma,P)$ (linear in Σ) or the new vertex
$\tfrac{g_s^3}{5!}V_5(\Sigma,\Sigma,\Psi)$ (quadratic in Σ). R14 Feynman rules,
extended: propagator $\tfrac{12}{g_s^2}(V_4|_{\rm Sym^2})^{-1}$; source vertex
$\tfrac{g_s^2}{6}V_4(\cdot,\Psi_i\otimes\Psi_j)$; new vertex
$\tfrac{g_s^3}{5!}V_5(\cdot,\cdot,\Psi_i)$ with two Σ-legs.

**Complete enumeration** (5 distinct externals):

| class | diagram | value | matches |
|---|---|---|---|
| (a) | (V₃)³, two Ψ-props, 15 channels | shared verbatim | (V₃)³ plumbing regions |
| (b) | V₃ —Ψ-prop— [source–Σ-prop–source] | R14 collapse with one internal leg ⇒ V₃×(g_s²V₄) | V₃×V₄ plumbing regions |
| (c) | [source–Σ-prop]–V₅(·,·,Ψ)–[Σ-prop–source] | $\tfrac{g_s^3}{15}V_5(\Psi_j,\Psi_k,\Psi_l,\Psi_m,\Psi_i)$ per assignment; **15 assignments** | V₅ contact, coefficient **1** |

Class (b): the R14 kernel identity $V_4V_4^{-1}V_4=V_4$ is slot-agnostic, so it holds
with one leg internal; nothing new to compute. Class (c), the new computation: the
Wick factor is $[\text{cross-term of }e^B\text{: }B_{jk}B_{lm}\text{ coefficient }1]
\times[2\text{ pairings of the two }B\text{'s onto the two }\Sigma\text{-slots}]$, each
source–propagator chain telescopes to $2q_{jk}$ ($q$ = symmetrized pair), giving per
unordered assignment $\{i;\{jk\},\{lm\}\}$:

$$
2\cdot\frac{g_s^3}{5!}\,V_5(2q_{jk},\,2q_{lm},\,\Psi_i)
=\frac{g_s^3}{15}\,V_5(\Psi_j,\Psi_k,\Psi_l,\Psi_m,\Psi_i),
\tag{B.7}
$$

and there are $5\times3=15$ assignments (choice of the single external × unordered
pair-of-pairs), summing to $g_s^3\,V_5(\Psi_1,\dots,\Psi_5)$ — **exactly** the contact
kernel of $\tfrac{g_s^3}{5!}V_5(\Psi^5)$ on distinct externals. The **Wick multiplicity 2**
is established by the check-0 collapse / the generating-functional argument (the $1/2!$ of
the two identical sources is cancelled by the 2 ways to contract them onto the two Σ-slots;
each slot fills with the propagated source $=P$ exactly). Script check 4 then certifies the
per-assignment value, the count 15, and the sum *given* that multiplicity — it does not
independently re-derive the factor 2 (it is hardcoded there), so it is a consistency check,
not an independent corroboration of the 2 (same "consistency vs independent corroboration"
caveat as R11/R14). (Equivalently, at one stroke: both telescopings collapse
$V_5(PB,PB,\Psi)=V_5(P,P,\Psi)$ since the propagated source is exactly $P$ — check 0.)

**No unwanted diagrams at O(g_s³).** Candidates and why they are absent:

- V₅ with one internal Ψ-leg to a V₃, both Σ-legs sourced: order
  $g_s^{3+1+2+2-2-2}=g_s^4$, 6 externals — next order.
- Two V₅'s joined by a Σ-prop, other legs sourced: $g_s^{3+3+2+2-2-2-2}=g_s^4$ —
  next order (this is the diagrammatic avatar of the feedback term in (B.2)).
- Σ-chains through a source vertex: impossible — the source is linear in Σ (a vertex
  can carry two Σ-lines only if it is V₅, which costs g_s³).
- Σ-tadpole on V₅ (the two Σ-legs of one V₅ contracted together): one loop, O(ℏ) —
  outside tree level. *Flag for the quantum tower:* this is the first place a
  Σ-loop exists at all; its IBL bookkeeping (p₁,₁,₁-type genus grading in the
  coloured operad, R15's two-gradings statement) belongs to the quantum phase.

Combined with the exact Gaussian argument of R14 (which covered all Ψ-Green's
functions at O(g_s²)), the action-level identity (B.2) guarantees that **every** tree
amplitude matches through O(g_s³) — the diagram table above is the mechanism, (B.2)
the proof.

## 4. The gauge law at O(g_s³)

Under the truncated L∞ transformation (now including ℓ₄)
$\delta\Psi=Q_B\Lambda+g_s\ell_2(\Psi,\Lambda)+\tfrac{g_s^2}{2}\ell_3(\Psi,\Psi,\Lambda)
+\tfrac{g_s^3}{3!}\ell_4(\Psi^3,\Lambda)$, one has
$\delta S^{(5)}_{\rm eff}=O(g_s^4)$ (geometric master equation through V₀,₅). The
naive composite law $\delta\Sigma=\delta(\Psi^{\otimes2})$ **fails** at O(g_s³)
(script check 5, falsifiability leg): the obstruction is the Ψ-dependence of the
dressed kernel $K_\Psi$ and of the shift $\tilde X$. The repair is forced and unique
up to trivial symmetries. Demanding invariance of each structure in (B.2):

- the dressed quadratic form is exactly invariant iff
  $2K_\Psi(\delta\tilde X,\tilde X)=-\,(\delta K_\Psi)(\tilde X,\tilde X)
  =\tfrac{g_s}{5}V_5(\tilde X,\tilde X,\delta\Psi)$, solved by

  $$
  \boxed{\;\delta\tilde X=\frac{g_s}{10}\,K_\Psi^{-1}V_5(\cdot,\tilde X,\delta\Psi)\;}
  \tag{B.8}
  $$

  — the deviation $\tilde X$ transforms **homogeneously** (a Ψ-dependent linear
  rotation; N_gh check: $V_5$ eats (4,2) and returns a saturation-10 covector ⇒
  ghost-4 vector after $K^{-1}$ ✓). Script check 5 confirms the variation of the
  quadratic form vanishes to machine precision (2×10⁻¹⁷), off-shell, arbitrary δΨ.
- translating back to Σ ($\Sigma = P + \tfrac{g_s}{5}K_\Psi^{-1}v + \tilde X$):

  $$
  \delta\Sigma
  =\underbrace{\delta(\Psi^{\otimes2})}_{\text{R11 composite}}
  +\underbrace{\delta\Big[\tfrac{g_s}{5}K_\Psi^{-1}v\Big]}_{=\;\delta\Sigma_*(\Psi)\text{ correction}}
  +\underbrace{\tfrac{g_s}{10}K_\Psi^{-1}V_5(\cdot,\tilde X,\delta\Psi)}_{\text{homogeneous in }\tilde X}.
  \tag{B.9}
  $$

  Reading: **Σ transforms as its own perturbative saddle $\Sigma_*(\Psi)$, plus a
  homogeneous rotation of the deviation** — the composite law is the O(g_s⁰)
  truncation of $\delta\Sigma=\delta(\Sigma_*(\Psi))$. The $\tilde X$-term vanishes
  on-shell; it is EOM-supported but *not* discardable off-shell (it is what cancels
  the $\delta K_\Psi$ anomaly). **BV classification (SETTLED, derivation 016 / R22,
  ST4):** this piece is *neither* a Henneaux–Teitelboim trivial gauge symmetry — its
  effective generator $\mu=-\tfrac{6}{5g_s}K_\Psi^{-1}V_5(\cdot,\cdot,\delta\Psi)
  K_\Psi^{-1}$ is graded-**symmetric**, while even fields require an
  **anti**symmetric $\mu$, and the parity of $\delta\Psi$ cannot antisymmetrise it
  ($\delta\Psi$ is a spectator in the swap of the two $\Sym^2$ slots of $V_5$) — *nor*
  a nontrivial gauge symmetry (no independent parameter; $R^{\tilde X}_\Lambda\propto
  \tilde X$ vanishes on-shell). It is the forced transformation law of the **auxiliary
  field** $\tilde X$ under the single $\Lambda$-symmetry: the $O(g_s^3)$ descendant of
  R11's $(\tilde X,\tilde X^+)$ **contractible pair**, the only new feature being that
  the dressed kinetic $K_\Psi$ is $\Psi$-dependent, forcing a nonzero but
  EOM-proportional rotation. Same BV class as the $O(g_s^4)$ $\delta Y_2$ (015 §4.2);
  reduces to $\delta Y_3=0$ / R11 when the auxiliary kinetic is field-independent. See
  `agent/derivations/016-st4-bv-homogeneous-law.md`.

With (B.9), the **exact** statement (B.3) holds: script check 5 verifies
$\delta S_3-\delta S^{(5)}_{\rm eff}-\delta[{\rm feedback}]=0$ (finite-difference
limited at 10⁻¹⁰) for arbitrary off-shell (Σ, Ψ, δΨ) and finite g_s. Since the
feedback is O(g_s⁴) and Σ-independent, $S_3$ is gauge-invariant to O(g_s⁴) — the same
order as the truncation itself. R11's slogan persists at the next order: *the HS tower
step costs nothing in gauge invariance, and introduces no independent two-string
parameter* (the deviation transforms homogeneously — no inhomogeneous
$\hat Q\Lambda_1$ piece can be generated; see derivation 012 for the systematic
statement).

## 5. Moduli bookkeeping

Inherited, region by region, in the R14(b) sense: what is *computed* here are the
coefficients (all = 1 after telescoping); the region identification is taken over from
the standard vertex construction. Explicitly, the O(g_s³) 5-point integrand
decomposition of $S_3$ is

$$
\mathcal M_{0,5}
=\underbrace{[\,(V_3)^3\ \text{plumbing}\,]}_{\text{class (a), shared}}
\cup\underbrace{[\,V_3\times\mathcal V_{0,4}\ \text{plumbing}\,]}_{\text{class (b), R14 collapse}}
\cup\underbrace{\mathcal V_{0,5}}_{\text{class (c), coefficient 1}},
$$

with **no new moduli integrals introduced**: both Σ-propagators in class (c) are
moduli-free algebraic kernels (R15: the Schwinger parameter of $V_4^{-1}$ is spectral,
not a modulus; the double-line/coloured-tree grading applies verbatim — a class-(c)
diagram is a coloured tree with two colour-2 edges, underlying uncoloured genus 2,
physically graded by the coloured tree structure). The dressed propagator
$K_\Psi^{-1}$ expands into chains [V₄⁻¹–V₅(·,·,Ψ)–V₄⁻¹–…] — coloured trees with
Ψ-leaves, again moduli-free.

## 6. The O(g_s⁴) spec (next milestone, NOT executed here)

> **SUPERSEDED by R19 / derivation 013 (B3).** The expectation floated below — that the
> O(g_s⁴) identity "should close with $c_6=1$ if the vertices satisfy the geometric master
> equation" — was subsequently **falsified**: the pure geometric $V_6$ fails, the forced
> vertex is the *dressed* $W_6=V_6-\tfrac65\mathcal C$ (Σ-channel exchange composite), and the
> master equation is **not** the closure mechanism (Route-B matching is master-equation-agnostic;
> its content sits in the target $S^{(6)}_{\rm eff}$). The *feedback-absorption* part of the spec
> below is correct and confirmed by R19; the "$c_6=1$ / master-equation-as-closure" reading is not.
> Read §6 as the (partly wrong) forward guess it was labelled to be.

At O(g_s⁴) the target is $S^{(6)}_{\rm eff}\supset\tfrac{g_s^4}{6!}V_6(\Psi^6)$ and the
tower adds $\tfrac{g_s^4}{6!}\,c_6\,V_6(\Sigma,\Sigma,\Sigma)$ (R12: 6 = 2+2+2, Σ₂
alone still suffices). The matching condition now has genuine content beyond the
Gaussian identity: on-shell,

$$
S_4(\Sigma_*) - S^{(6)}_{\rm eff}
=\Big[\underbrace{\tfrac{g_s^4}{600}\,vV_4^{-1}v}_{\text{feedback (B.2)}}
+\underbrace{(c_6-1)\tfrac{g_s^4}{6!}V_6(P,P,P)}_{\text{contact mismatch}}
+\underbrace{\tfrac{g_s^4}{6!}\,c_6\cdot3\,V_6(X_*,P,P)\cdot 0 + \dots}_{O(g_s^5)}\Big]
+O(g_s^5),
$$

so the V₆ step must **absorb the explicit feedback term**: the correct statement is
NOT $c_6=1$ alone — the O(g_s⁴) 6-point amplitude receives [V₆-collapse] +
[feedback/two-V₅ trees] + [V₅×V₃ internal-Ψ trees] and must reproduce the
$V_6$ contact + [V₅×V₃] + [V₄×V₄] + [V₄×V₃×V₃] + [(V₃)⁴] regions. The clean way to
run it: extend (B.2) — complete the square in the presence of the V₆ coupling and
read off the condition on $c_6$ (expected: $c_6=1$ with the feedback matching the
*difference* between the geometric $V_6$ region and the naive one; if the vertices
satisfy the geometric master equation the identity should close with $c_6=1$ —
this is the real test of "dynamical closure" and needs the L∞ relations as input,
unlike everything through O(g_s³)). Deliverable spec: mirror this derivation;
the new technical ingredient is that matching starts to *use* the master equation
rather than mere completion of squares.

## 7. What is established vs open

**Established (machine-checked, finite-dim algebraic layer):**
(i) coefficient 1/5! forced (checks 1–3); (ii) exact rewriting (B.2) (check 1);
(iii) saddle/on-shell matching with explicit O(g_s⁴) feedback (check 2);
(iv) 5-point diagram enumeration: three classes, no unwanted diagrams, contact
coefficient 1 (check 4); (v) exact gauge equality (B.3) with the corrected law
(B.8)/(B.9), naive law falsified (check 5).

**Open / carve-outs (mirror R14/R15):**
(a) CFT-level analytics of $V_4^{-1}$, $K_\Psi^{-1}$ (spectrum, boundedness) = A2(iii)/T4;
(b) region identification inherited, not re-derived;
(c) BV classification of the homogeneous $\tilde X$-term in (B.9) — **SETTLED**
(derivation 016 / R22, ST4): auxiliary-field/contractible-pair transformation law,
neither HT-trivial ($\mu$ symmetric) nor nontrivial (no independent parameter);
(d) O(g_s⁴) dynamical closure = §6 spec (first place the master equation is load-bearing);
(e) one-loop Σ-tadpole bookkeeping = quantum tower (IBL/coloured-genus grading).
