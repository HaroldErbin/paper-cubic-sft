# Derivation record 003 — I2: the $\IBL_\infty$ action $S=\omega\circ\hat{\mathfrak p}(e^\Psi)$ vs the HS EOM at $O(g_s^2)$

Date: 2026-06-24
Author agent: computator
Brief: `agent/briefs/done-computator-i2-action-20260624T200000.md`
Verification: `codes/verify-i2-ibl-action.py` (sympy 1.14.0, 11/11 PASS); reuses the
physical-grading toy of `codes/verify-omega2-physical.py`.

Reused verbatim (not re-derived): **R1** (HS action + completion of square + Σ-EOM),
**R5** (degree/Euler), **R6** ((2,2,0) structure equation), **R7** (ω₂ graded
symmetric / Poisson, BV antibracket partner, m₂ cyclic, non-deg).

---

## Setup

### Assumptions and conventions

- **Sector.** Classical $g=0$, order $g_s^2$ (quartic truncation), $\Sigma\in\mathcal H^{\otimes2}$.
  Erbin (2023): metric $(-,+,+,+)$, $\hbar=c=1$, $\alpha'$ explicit, bra–ket. The CFL
  formal genus variable is identified with the string coupling
  (note `eq:IBLmaster`). **$\hbar_{\rm CFL}$ identification.** The CFL
  genus-0 $n$-point vertex weighs $\hbar_{\rm CFL}^{\,n/2-1}$ (WBEIHWFU §master). To
  reproduce the standard closed genus-0 counting of (1.2) — cubic at $g_s^1$, quartic
  at $g_s^2$, i.e. $\hbar_{\rm CFL}^{\,n/2-1}=g_s^{\,n-2}$ — one needs
  $$\boxed{\hbar_{\rm CFL}=g_s^2}\qquad(\text{not }g_s):$$
  then each field carries $\hbar_{\rm CFL}^{1/2}=g_s$ (the $\hbar^{1/2}$ absorbed into
  $c$, WBEIHWFU footnote 1), a vertex $\mathcal V^{b,g}_n$ weighs
  $\hbar_{\rm CFL}^{\,2g+b+n/2-1}=g_s^{\,4g+2b+n-2}$, and the genus weight is
  $g_s^{4g-2}$. Physical Grassmann parity $\epsilon=N_{\rm gh}\bmod2$ (R7/R2.1).
  **Convention note (two distinct $\hbar$'s — reconciling the overview).** This
  $\hbar_{\rm CFL}$ is the **BV-action** weighting variable of WBEIHWFU §master
  ($S=\sum_g\hbar^{2g-1}(\omega_c\circ l^g)(e^{\hbar^{1/2}c})$, field weight
  $\hbar^{1/2}$), and equals $g_s^2$. It is **not** the same formal variable as the
  $\hbar$ of the *coderivation* master equation `eq:IBLmaster`
  ($\hat{\mathfrak p}=\sum\mathfrak p_{k,\ell,g}\hbar^{k+g-1}\tau^{\dots}$, $|\hbar|=2d$),
  where the overview says "$\hbar$ plays the role of $g_s$": there $\hbar$ is an
  *algebraic grading/genus* bookkeeping unit ($\hbar_{\rm master}=g_s$, counting
  $k+g-1$), not the physical coupling power. The two are different presentations of the
  same structure and are not in contradiction; only the BV-action $\hbar_{\rm CFL}=g_s^2$
  enters the *physical action's* $g_s$-counting used here. (Flagged for an optional
  one-line convention footnote in `cubic-sft-overview.tex` §4 near `eq:IBLmaster`.)
- **Physical $N_{\rm gh}$ parametrization (binding).** $\Psi$ at $N_{\rm gh}=2$
  ($\epsilon=0$), $\Sigma\in\mathcal H^{\otimes2}$ at $N_{\rm gh}=4$ ($\epsilon=0$),
  note `eq:Sigexpand`. **All final objects are physical**; suspended grading is used
  only as an intermediate, translated back (presentation (A)↔(B) dictionary, step F).
- **Level-matching.** Every field $\in\ker L_0^-\cap\ker b_0^-$; no "$\ker L_0^-$
  complement" restriction (plan Revision-2 §3).

### Presentation (A) data — the binding choice (R7)

This is **not** a single graded-antisymmetric $\omega=\omega_1+\omega_2$. From R7,
$\omega_2=\omega_1^{\otimes2}$ is graded **symmetric** in physical statistics, so it
cannot be a summand of one graded-antisymmetric symplectic form. The two sectors are
governed by **two distinct structures**:

- **$\Psi$ sector — odd symplectic $\omega_1$.**
  $$\omega_1(A,B)=\langle A|\,c_0^-\,|B\rangle_{\rm bpz},\qquad
  \omega_1(A,B)=-(-1)^{\epsilon(A)\epsilon(B)}\omega_1(B,A)\tag{A.1}$$
  graded antisymmetric (one $c_0^-$), non-degenerate on $\ker L_0^-\cap\ker b_0^-$,
  inverse $\Delta=\omega_1^{-1}$. This is the standard closed-string symplectic form
  carrying the $\Psi$ kinetic term $\tfrac12\langle\Psi|c_0^-Q_B|\Psi\rangle$.

- **$\Sigma$ sector — symmetric Poisson pairing $G_2$.**
  $$G_2:=\omega_1^{\otimes2}=(\cdot,c_0^-\cdot)_{\rm bpz}^{\otimes2},\qquad
  G_2(X,Y)=(-1)^{\epsilon(x_2)\epsilon(y_1)}\,\omega_1(x_1,y_1)\,\omega_1(x_2,y_2),\tag{A.2}$$
  for $X=x_1\otimes x_2,\,Y=y_1\otimes y_2$, graded **symmetric** (R7/R2.10):
  $$G_2(Y,X)=(-1)^{\epsilon(X)\epsilon(Y)}G_2(X,Y)\quad\text{on }\operatorname{supp}(G_2).\tag{A.3}$$
  $G_2$ is the bilinear form appearing in the $\Sigma$ kinetic term
  $V_4(\Sigma,\Sigma)=G_2(\Sigma,m_2\Sigma)$ (note `eq:V4ell3`/`eq:mtwo`). Its inverse
  defines the **BV antibracket** on the $\Sigma$ fields:
  $$\{F,H\}_\Sigma:=\frac{\overrightarrow\partial F}{\partial\Sigma^I}\,
  (G_2^{-1})^{IJ}\,\frac{\overleftarrow\partial H}{\partial\Sigma^J},\qquad
  G_2^{-1}=(\Delta\otimes\Delta)\ \text{up to Koszul signs},\tag{A.4}$$
  i.e. the antibracket has the Poisson-tensor $G_2^{-1}=\omega_1^{-\otimes2}$.
  The CFL/Münster–Sachs normalisation makes this antibracket
  $\propto\hbar_{\rm CFL}=g_s^2$ (WBEIHWFU footnote 1; the $g_s$ absorbed into
  each $c$, since the field weight is $\hbar_{\rm CFL}^{1/2}=g_s$); see step F.

- **Two-output product $m_2$ (note `eq:mtwo`).**
  $$m_2\equiv\mathfrak p_{2,2,0}=\Delta\circ\ell_3:\mathcal H^{\otimes2}\to\mathcal H^{\otimes2},
  \qquad N_{\rm gh}(m_2)=-2\ (\epsilon(m_2)=0),\tag{A.5}$$
  defined by $G_2(X,m_2Y)=V_4(x_1,x_2,y_1,y_2)=\langle x_1|\ell_3(x_2,y_1,y_2)\rangle$,
  with $V_4$ fully graded-symmetric (closed cyclic vertex).

### Step-0 — component master-equation relations (folded I1, reused verbatim)

From R5/R6 and note §IBL; **not** re-derived here:

- **$(1,1,0)$:** $Q^2=0$ with $Q=\mathfrak p_{1,1,0}=\hat\ell_1$ (note `eq:Loorels`).
- **$(2,2,0)$ — R6 / note `eq:IBLrels`:**
  $$\hat{\mathfrak p}_{1,1,0}\!\circ_1\!\mathfrak p_{2,2,0}
  +\mathfrak p_{2,2,0}\!\circ_1\!\hat{\mathfrak p}_{1,1,0}
  +\mathfrak p_{1,2,0}\!\circ_1\!\mathfrak p_{2,1,0}
  +\hat{\mathfrak p}_{2,1,0}\!\circ_1\!\hat{\mathfrak p}_{1,2,0}=0.\tag{0.1}$$
  This says $m_2=\mathfrak p_{2,2,0}$ is $Q$-exact ($=-[Q,\mathfrak p_{2,2,0}]$),
  **not** zero. $\ell_3=\mathfrak p_{3,1,0}$ does **not** enter (signature ordering
  $(2,2,0)\prec(3,1,0)$).
- **Degree/Euler bookkeeping — R5 / note `eq:IBLdeg`:**
  $|\mathfrak p_{k,\ell,g}|=-2d(k+g-1)-1$, $\chi=2-2g-k-\ell$; $(2,2,0)$ has $\chi=-2$
  (4-punctured sphere); the $\Loo$ truncation is $(\ell=1,g=0)$.

---

## Derivation

### Step 1 — the action $S=\omega\circ\hat{\mathfrak p}(e^\Psi)$ at $O(g_s^2)$, presentation (A)

The schematic $\IBL_\infty$ action pairs the codifferential $\hat{\mathfrak p}$ applied
to the group-like element $e^\Psi$ with the symplectic data. In presentation (A) the
pairing is sector-split: the $\ell=1$ outputs are paired with $\omega_1$, the $\ell=2$
output ($\Sigma\in\mathcal H^{\otimes2}$) with $G_2$. Expanding $\hat{\mathfrak p}(e^\Psi)$
to the order producing the quartic/$\Sigma$ terms and reading off the pieces:

$$\hat{\mathfrak p}(e^\Psi)\big|_{O(g_s^2)}
=\underbrace{Q\Psi}_{\ell=1}
+\underbrace{\tfrac12 g_s\,\ell_2(\Psi,\Psi)}_{\ell=1}
+\underbrace{\tfrac{1}{3!}g_s^2\,\ell_3(\Psi,\Psi,\Psi)}_{\ell=1\ (\text{traded})}
+\underbrace{g_s^2\,\mathfrak p_{2,2,0}\Sigma}_{\ell=2}
+\cdots\tag{1.1}$$

Pairing with $\omega_1$ on the $\ell=1$ outputs and with $G_2$ on the $\ell=2$ output,
and performing the HS trade of the $\ell_3$ quartic (R1, note `eq:SHSderive`):

$$\boxed{\;
S_{\rm HS}=\tfrac12\,V_2(\Psi^2)+\frac{g_s}{3!}\,V_3(\Psi^3)
-\frac{g_s^2}{4!}\,G_2(\Sigma,m_2\Sigma)
+\frac{2g_s^2}{4!}\,G_2(\Sigma,m_2\Psi^{\otimes2})
\;}\tag{1.2}$$

where I used $V_4(\Sigma,\Sigma)=G_2(\Sigma,m_2\Sigma)$ and
$V_4(\Sigma,\Psi^{\otimes2})=G_2(\Sigma,m_2\Psi^{\otimes2})$ (note `eq:mtwo`). This is
note `eq:SHS` with the pairing displayed as the **symmetric** $G_2$:

- $V_2(\Psi^2)=\omega_1(\Psi,Q_B\Psi)$ — the $\Psi$ kinetic term, **$\omega_1$ sector**.
- $V_3(\Psi^3)=\omega_1(\Psi,\ell_2(\Psi,\Psi))$ — cubic, $\omega_1$ sector.
- $-\tfrac{g_s^2}{4!}G_2(\Sigma,m_2\Sigma)$ — the $\Sigma$ **kinetic** term, **$G_2$
  sector**, a *symmetric* bilinear in $\Sigma$ (this is exactly why the completion of
  square goes through; see step 1a).
- $+\tfrac{2g_s^2}{4!}G_2(\Sigma,m_2\Psi^{\otimes2})$ — the $\Sigma$–$\Psi$ coupling.

The CFL $\hbar_{\rm CFL}=g_s^2$ counting checks: each $\Psi$ carries
$\hbar_{\rm CFL}^{1/2}=g_s$, so the genus-0 $n$-point vertex
$\langle\Psi|\ell_{n-1}(\Psi^{n-1})\rangle=\omega_1(\Psi,\cdot)$ weighs
$\hbar_{\rm CFL}^{\,n/2-1}=g_s^{\,n-2}$:
$$V_3(\Psi^3)\sim g_s^{3-2}=g_s^1,\qquad
V_4(\Psi^4)\sim g_s^{4-2}=g_s^2\tag{1.4}$$
— matching the cubic $g_s/3!$ and quartic $g_s^2/4!$ coefficients in (1.2). The earlier
"$\hbar=g_s$, field $g_s^{1/2}$" gave $V_3\sim g_s^{1/2}$, which is wrong; the correct
identification is $\hbar_{\rm CFL}=g_s^2$. The final action (1.2) itself is inherited
verbatim from R1 (`eq:SHS`) — only the $\hbar_{\rm CFL}$ entry is corrected here. No
other deviation from Erbin (2023) / Münster–Sachs.

#### Step 1a — graded structure of the $\Sigma$ kinetic bilinear

The completion-of-square (R1) needs the $\Sigma$ **kinetic bilinear**
$B(X,Y):=V_4(X,Y)=G_2(X,m_2Y)$ to be **symmetric** in $X\leftrightarrow Y$:
$$V_4(\Sigma,\Sigma)-2V_4(\Sigma,\Psi^{\otimes2})+V_4(\Psi^{\otimes2},\Psi^{\otimes2})
=V_4(\Sigma-\Psi^{\otimes2},\,\Sigma-\Psi^{\otimes2}).\tag{1.3}$$
The symmetry that (1.3) needs is a property of the **kinetic bilinear $B=V_4$**, i.e.
a property of the **closed cyclic vertex $V_4$** (a CFT fact: $V_4$ fully
graded-symmetric), **not** of whether the outer two-output pairing is presented as the
symmetric Poisson $G_2$ (presentation A) or as the antisymmetric BV partner
$\omega_2^{\rm symp}=G_2\circ(s\otimes s)$ (presentation B). $B=V_4$ is graded-symmetric
(cyclicity of $m_2$, R7): as a matrix it is **plainly symmetric on the even sector**
$\epsilon=0$ and antisymmetric on the odd sector $\epsilon=1$. Since $\Sigma$ and
$\Psi^{\otimes2}$ both have $N_{\rm gh}=4$ ($\epsilon=0$), they live in the **even
sector**, where $B$ is symmetric and (1.3) holds. This is the precise content of note
`eq:SHSderive`'s "$V_4$ a graded-symmetric bilinear form".

**Presentation-independence (no "forcing").** The completion of square is therefore
**presentation-independent**: presentations (A) and (B) share the identical kinetic
bilinear $B=V_4$ (same matrix entries, R7), identical $m_2$, and identical $\Sigma$-EOM.
(Toy F1's genuinely failable content is that the (B) form $\omega_2^{\rm symp}$ it builds
is truly graded-antisymmetric in the suspended parity; that (B)'s EOM operator equals
(A)'s is then a relabel — (B) and (A) share the same matrix entries by construction, R7,
so this half is a consistency check, not an independent test.) Presentation (A) — the
symmetric Poisson $G_2$ — is the
**natural/convenient** presentation in which the required symmetry of $B$ is *manifest*
(the outer pairing and the kinetic bilinear have the same symmetry type), and it is the
binding choice for the *final objects* per R7 and the brief; but it is **not** that an
antisymmetric outer pairing would break the completion of square. (Toy: checks
C0a/C0b/C1 for $B$ symmetric on the even sector; F1 for presentation-independence.)

### Step 2 — equations of motion

**$\Sigma$-EOM.** Vary (1.2) in $\Sigma$. On the even sector $B$ is symmetric, so
$$\frac{\delta S_{\rm HS}}{\delta\Sigma}
=-\frac{2g_s^2}{4!}\Big(B\,\Sigma-B\,\Psi^{\otimes2}\Big)
=-\frac{2g_s^2}{4!}\,G_2\big(m_2(\Sigma)-m_2(\Psi^{\otimes2})\big)=0.\tag{2.1}$$
$G_2$ is non-degenerate (R7), so the outer pairing strips:
$$\boxed{\;m_2(\Sigma)=m_2(\Psi^{\otimes2})\;}\tag{2.2}$$
which is note `eq:Sigeom`. **Invertibility of $m_2$ is NOT used:** $\Sigma=\Psi^{\otimes2}$
*solves* (2.2) (sufficiency, no inversion), but is the *unique* solution only if
$\ker m_2=0$ — that is open, task I3. (Toy: D1/D2/D3.)

**$\Psi$-EOM (schematic; coefficient inherited from R1).** Varying (1.2) in $\Psi$
gives, schematically,
$$\frac{\delta S_{\rm HS}}{\delta\Psi}
=Q_B\Psi+\tfrac{g_s}{2}\ell_2(\Psi,\Psi)
+\frac{2g_s^2}{4!}\,\frac{\delta}{\delta\Psi}V_4(\Sigma,\Psi^{\otimes2})=0.\tag{2.3}$$
**This is marked schematic:** the explicit graded variation of
$V_4(\Sigma,\Psi^{\otimes2})=G_2(\Sigma,m_2(\Psi\otimes\Psi))$ in $\Psi$ — defining the
adjoint of $m_2$ w.r.t. $G_2$, tracking the **two** $\Psi$-insertions (each gives a
factor, Leibniz on $\Psi\otimes\Psi$), the graded signs, and the
$\tfrac{2}{4!}\cdot2=\tfrac{1}{3!}$ combinatorial bookkeeping that converts the quartic
$\tfrac{1}{4!}$ into the cubic $\tfrac{1}{3!}$ — is **not** carried out here; the
coefficient is inherited from R1 (`eq:SHS`), where the completion of square fixes it.
On-shell, substituting (2.2)/$\Sigma=\Psi^{\otimes2}$ and using cyclicity of $m_2$ (R7),
the $\Sigma$-$\Psi$ term reconstructs the $\ell_3$ quartic and (2.3) reduces to
$$Q_B\Psi+\tfrac{g_s}{2}\ell_2(\Psi,\Psi)+\tfrac{g_s^2}{3!}\ell_3(\Psi,\Psi,\Psi)+\cdots=0,
\tag{2.4}$$
the $g_s^2$-truncated closed-string $\Loo$ EOM — $\Sigma$ playing the contact channel.
(R1; the on-shell reduction is the standard completion-of-square back-substitution. The
$\tfrac{1}{3!}$ in (2.4) is the R1 coefficient, **not** independently re-derived here —
so this step makes no "no factor mismatch" claim about the $\Psi$-EOM.)

### Step 3 — comparison with the $(1,1,0)$ and $(2,2,0)$ component relations

**$(1,1,0)$.** The kinetic sector $Q_B\Psi$ in (2.3)/(2.4) is governed by $Q^2=0$
(step 0). The toy confirms a nilpotent $Q=\mathfrak p_{1,1,0}$ (check G1).

**$(2,2,0)$ — what the comparison actually shows (DC5/DC7).** The $\Sigma$-EOM (2.2) is
built **entirely from $m_2=\mathfrak p_{2,2,0}$** (toy E1: the EOM operator,
independently reconstructed from the action gradient, equals $m_2=G_2^{-1}V_4$ — no
$\mathfrak p_{3,1,0}$ insertion, consistent with R6's signature ordering).

**Category distinction (the precise relationship).** The $\Sigma$-EOM and the $(2,2,0)$
relation R6 are objects of **different type**, and the comparison must respect that:

- The **$\Sigma$-EOM** $m_2(\Sigma)=m_2(\Psi^{\otimes2})$ is a **field equation** in
  $\mathcal H^{\otimes2}$ — a condition on the *configuration* $(\Psi,\Sigma)$.
- The **$(2,2,0)$ relation R6** (0.1) is an **off-shell operator identity** among the
  $\IBL_\infty$ operations $\{Q=\mathfrak p_{1,1,0},\,\ell_2=\mathfrak p_{2,1,0},\,
  \mathfrak p_{1,2,0},\,\mathfrak p_{2,2,0}\}$, asserting $Q$-exactness of
  $\mathfrak p_{2,2,0}$. **None** of $Q$, $\ell_2$, $\mathfrak p_{1,2,0}$ appears in the
  $\Sigma$-EOM.

So the EOM is **not identical to** R6. What is actually shown is the weaker, correct
statement:

> The HS $\Sigma$-EOM is the on-shell relation $m_2(\Sigma)=m_2(\Psi^{\otimes2})$, built
> from $\mathfrak p_{2,2,0}$ **alone** (no $\mathfrak p_{3,1,0}$, toy E1), and is
> **consistent with** the off-shell operator relation R6 — they invoke the same operation
> $\mathfrak p_{2,2,0}$ at the same signature $(2,2,0)$, with the same signature ordering
> excluding $\mathfrak p_{3,1,0}$. R6 is the **separate, off-shell mechanism** ($Q$-exactness
> of $\mathfrak p_{2,2,0}$) that makes the HS-traded $\ell_3$ quartic a $Q$-homotopy of the
> cobracket–bracket composition, i.e. makes $\Sigma$ a genuine contact (non-propagating)
> field. The EOM realises the *field-content* side of $\mathfrak p_{2,2,0}$; R6 is the
> *operator-consistency* side. The two are compatible, not equal.

So the **confirmed statement** (demoted from "= master equation"):

> **The HS action (1.2) and its equations of motion are mutually consistent in
> presentation (A): the $\Sigma$-EOM is $m_2(\Sigma)=m_2(\Psi^{\otimes2})$ (`eq:Sigeom`),
> built from $m_2=\mathfrak p_{2,2,0}$ alone (no $\mathfrak p_{3,1,0}$), derived without
> assuming $m_2$ invertible, and consistent with the $(2,2,0)$ operator relation R6 by
> signature ordering — though not identical to it. Identifications: $G_2=\omega_1^{\otimes2}$,
> $\{\cdot,\cdot\}=G_2^{-1}$, $\hbar_{\rm CFL}=g_s^2$.** Uniqueness of
> $\Sigma=\Psi^{\otimes2}$ (vs. merely $m_2(\Sigma)=m_2(\Psi^{\otimes2})$) requires
> $\ker m_2=0$, open (I3).

There is **no mismatch** in sign, factor, or structure at the level shown: the EOM (2.2)
involves $\mathfrak p_{2,2,0}$, the same operation R6 constrains; $\ell_3=\mathfrak p_{3,1,0}$
appears in neither (traded for the $\Sigma$-coupling); the signature ordering is respected.
This is **action/EOM consistency**, not a proof that "HS EOM = master equation at (2,2,0)".

**Scope of the DC5/DC7 claim.** This settles the *action/EOM consistency* of `eq:SHS`
in presentation (A) (DC5's "form of the action" and DC7). It does **not** close DC5/DC6
in full: the overview still flags the schematic $S=\omega\circ\hat{\mathfrak p}(e^\Psi)$
and the very definition of $\omega_2$ as open. The CFT-level $V_4$ graded symmetry and
$m_2$ invertibility (I3) remain open; the claim here is scoped to the algebraic/toy-level
consistency actually demonstrated.

### Step 4 — self-consistency

- **Cyclicity of $m_2$ w.r.t. $G_2$ (R7).** $G_2(X,m_2Y)=G_2(m_2X,Y)$ from full graded
  symmetry of $V_4$; this is what makes the kinetic bilinear $B=V_4$ symmetric and the
  completion of square exact (step 1a). Toy B1. Presentation-independent: toy F1 builds
  the antisymmetric presentation-(B) form $\omega_2^{\rm symp}=G_2\circ(s\otimes s)$
  explicitly, confirms it is genuinely graded-antisymmetric in the suspended parity, and
  checks the EOM operator agrees with presentation (A)'s $m_2$.
- **$m_2=\mathfrak p_{2,2,0}$ is $Q$-exact, not zero (R6).** The EOM uses $m_2$ as a
  nonzero operator; consistent with (0.1). No $\ell_3=\mathfrak p_{3,1,0}$ inserted into
  (0.1) (toy E1).

---

## Commentary

- **(1.2)/(1.3) — what is and is not "forced".** The completion of square needs the
  **kinetic bilinear** $B=V_4$ to be graded-symmetric — a property of the **closed cyclic
  vertex $V_4$** (a CFT fact, R7), **not** of the outer two-output pairing's presentation.
  The symmetry of $B$ is presentation-independent: presentations (A) (symmetric Poisson
  $G_2$) and (B) (antisymmetric BV partner $\omega_2^{\rm symp}=G_2\circ(s\otimes s)$)
  share the *same* matrix entries, the *same* $B=V_4$, and the *same* $\Sigma$-EOM (toy
  F1). So an antisymmetric outer pairing does **not** break the trade — that earlier
  "antisymmetric $\omega_2$ collapses the completion of square" was a strawman and is
  withdrawn. Presentation (A) is the **natural/convenient** presentation that makes the
  required symmetry of $B$ manifest, and is the binding choice for the final objects (R7,
  brief) — but it is a *convenient* choice, not *forced* by consistency. This is fully
  consistent with R7's "DC6 stands physically" (the *physical* $\omega_1^{\otimes2}$ is
  symmetric); it settles the action/EOM consistency of `eq:SHS` (DC5/DC7), not the full
  DC5/DC6 (which the overview still flags open).
- **(A.4) antibracket.** $G_2^{-1}=\omega_1^{-\otimes2}$ is the Poisson tensor of the
  $\Sigma$ BV antibracket; its $\propto\hbar_{\rm CFL}$ normalisation matches Münster–Sachs
  (WBEIHWFU footnote 1, $\mathfrak L_c=\sum_g\hbar^gL^g+\hbar D(\omega_c^{-1})$: the
  bivector $D(\omega_c^{-1})$ enters at one power of $\hbar_{\rm CFL}=g_s^2$). The
  $\Sigma$-sector bracket is the closed-string two-output analogue of the open-string
  $\delta=D(\omega_o^{-1})$.
- **(2.2)/(2.4).** The $\Sigma$-EOM strips $G_2$ (non-degenerate) to a *pure $m_2$*
  relation — this is why the comparison with R6 is clean: both invoke
  $\mathfrak p_{2,2,0}$ at signature $(2,2,0)$. But the EOM is a *field equation* and R6
  an *off-shell operator identity*: they are **consistent, not equal** (step 3). The
  $\Psi$-EOM (2.3) is left schematic; its $\tfrac{1}{3!}$ coefficient is inherited from
  R1, not re-derived.
- **Open / non-claimed.** The toy tests the **sign/factor/structure bookkeeping** only,
  in the physical grading. It does **not** compute the worldsheet $c_0^-$, $\ell_3$,
  $V_4$ on level-matched $\mathcal H$ (CFT-level content), nor prove $\ker m_2=0$
  (I3), nor the gauge sector (S2).

---

## Result

$$\boxed{\;
S_{\rm HS}=\tfrac12\,\omega_1(\Psi,Q_B\Psi)
+\frac{g_s}{3!}\,\omega_1(\Psi,\ell_2(\Psi,\Psi))
-\frac{g_s^2}{4!}\,G_2(\Sigma,m_2\Sigma)
+\frac{2g_s^2}{4!}\,G_2(\Sigma,m_2\Psi^{\otimes2}),
\;}$$

presentation (A), physical $N_{\rm gh}$: $\Psi$ at $N_{\rm gh}=2$, $\Sigma$ at
$N_{\rm gh}=4$; $\omega_1=(\cdot,c_0^-\cdot)_{\rm bpz}$ odd symplectic on the $\Psi$
sector; $G_2=\omega_1^{\otimes2}$ symmetric Poisson on the $\Sigma$ sector with BV
antibracket $\{\cdot,\cdot\}_\Sigma=G_2^{-1}=\omega_1^{-\otimes2}$;
$m_2=\mathfrak p_{2,2,0}=\Delta\circ\ell_3$; $\hbar_{\rm CFL}=g_s^2$.

EOM:
$$\boxed{\;
m_2(\Sigma)=m_2(\Psi^{\otimes2})\quad(\Sigma,\ \text{field eq.}),\qquad
Q_B\Psi+\tfrac{g_s}{2}\ell_2(\Psi,\Psi)+\tfrac{g_s^2}{3!}\ell_3(\Psi^{\otimes3})+\cdots=0
\quad(\Psi,\ \text{schematic; on-shell }\Sigma=\Psi^{\otimes2}).
\;}$$

**Verdict (action/EOM consistency; DC5/DC7 scoped):**
**The HS action (1.2) and its EOM are mutually consistent in presentation (A). The
$\Sigma$-EOM is the field equation $m_2(\Sigma)=m_2(\Psi^{\otimes2})$ (`eq:Sigeom`), built
from $m_2=\mathfrak p_{2,2,0}$ alone (no $\mathfrak p_{3,1,0}$), derived without assuming
$m_2$ invertible, and CONSISTENT WITH — but NOT identical to — the off-shell $(2,2,0)$
operator relation R6 (a $Q$-exactness statement; R6 is the separate mechanism making
$\Sigma$ auxiliary). Identifications: $G_2=\omega_1^{\otimes2}$, $\{\cdot,\cdot\}=G_2^{-1}$,
$\hbar_{\rm CFL}=g_s^2$.** No sign/factor/structural mismatch at the level shown.
Uniqueness of $\Sigma=\Psi^{\otimes2}$ requires $\ker m_2=0$ (open, I3). This is a
*field equation = operator-consistency* relationship, **not** "HS EOM = master equation
at $(2,2,0)$". DC5 (action form) / DC7 settled at the action/EOM-consistency level; the
schematic $S=\omega\circ\hat{\mathfrak p}(e^\Psi)$ and $\omega_2$ definition (DC5/DC6)
remain flagged open in the overview.

### Established vs. open

**Established (toy-verified sign/structure algebra).**
- The HS action (1.2) in presentation (A) with symmetric Poisson $G_2$ on $\Sigma$, odd
  $\omega_1$ on $\Psi$; completion of square exact on the physical even sector
  (C0a/C0b/C1) — *presentation-independent* (the symmetry needed is that of the cyclic
  vertex $V_4$, not of the outer pairing).
- $\Sigma$-EOM $m_2(\Sigma)=m_2(\Psi^{\otimes2})$, derived without assuming $m_2$
  invertible (D1/D2/D3).
- EOM operator independently reconstructed from the action gradient = $\mathfrak p_{2,2,0}$;
  no $\mathfrak p_{3,1,0}$ insertion (E1), consistent with R6 ordering; $m_2$ cyclic
  w.r.t. $G_2$ (B1); presentations (A)/(B) give the identical EOM (F1).
- $(1,1,0)$ kinetic sanity: $Q^2=0$ a *nontrivial, solvable* nilpotency condition (G1).
- **Consistency (not identity)** between the HS $\Sigma$-EOM (field eq.) and the
  $(2,2,0)$ operator relation R6, under the stated identifications.
- $\hbar_{\rm CFL}=g_s^2$ reproduces the genus-0 coupling powers of (1.2).

**Open (not settled here).**
- $\ker m_2=0$ / $m_2$ invertibility ⇒ $\Sigma=\Psi^{\otimes2}$ unique / $\Sigma$ purely
  auxiliary — **task I3**.
- CFT-level vertex content ($c_0^-$, $\ell_3$, $V_4$ on level-matched $\mathcal H$) —
  numerical-verifier / CFT computation.
- Gauge transformations of the $\Sigma$ sector — **task S2** (cf. I4 = arXiv:1905.06785
  eq. (5.55)).
- Homotopy-transfer integrate-out toy — **task S6**.

### Proposed next step

**I3** (auxiliarity / $m_2$ invertibility): the only gap between the confirmed
$m_2(\Sigma)=m_2(\Psi^{\otimes2})$ and the desired $\Sigma=\Psi^{\otimes2}$. Heuristic:
$V_4$ is a genuine contact term (no $V_4$ poles, R3 analogue), suggesting non-degeneracy
of $V_4$ ⇒ $m_2$ invertible on physical states — to be made precise. Alternatively **S6**
(homotopy-transfer toy) to check integrating out $\Sigma$ returns the $\ell_3$ quartic.

---

## Verification

Script: `codes/verify-i2-ibl-action.py` (sympy 1.14.0, **11 checks, all PASS — all 11
are substantive/failable after the iter-1 revision**; the previously-hollow E1/F1/G1
were rewritten, see below). Reuses the physical-grading toy of
`codes/verify-omega2-physical.py` ($\dim\mathcal H=4$, $N_{\rm gh}=[2,3,2,3]$,
$\epsilon=[0,1,0,1]$, $\omega_1$ pairing $N_{\rm gh}=2\leftrightarrow3$,
$G_2=\omega_1^{\otimes2}$). Each check is an internal algebraic self-check, **not** an
independent re-derivation of the closed-string CFT result.

| ID | Check | Method | Outcome | Scope |
| --- | --- | --- | --- | --- |
| A | $G_2=\omega_1^{\otimes2}$ graded-**symmetric** (R7) | grade-violation count | PASS | presentation (A) natural; symmetric Poisson |
| B1 | $m_2=\mathfrak p_{2,2,0}$ cyclic w.r.t. $G_2$; uses only $V_4$, no $\ell_3$ | $m_2=G_2^{-1}V_4$, compare | PASS | R7 reused; R6 untouched |
| C0a | $B=V_4$ **symmetric on even sector** ($\epsilon=0$): $\Sigma,\Psi^{\otimes2}$ live here | matrix sym on $\epsilon=0$ block | PASS | physical $N_{\rm gh}=4$ ⇒ even |
| C0b | $B$ **antisymmetric on odd sector** ($\epsilon=1$): confirms graded structure | matrix antisym on $\epsilon=1$ block | PASS | not populated by $N_{\rm gh}=4$ |
| C1 | completion of square $V_4(S,S)-2V_4(S,P)+V_4(P,P)=V_4(S-P,S-P)$ on even sector | symbolic diff | PASS | `eq:SHSderive`→`eq:SHS` (R1) |
| D1 | $\Sigma$-gradient $=-(2g_s^2/4!)B(\Sigma-\Psi^{\otimes2})$ | $\partial_\Sigma S_{\rm HS}$ | PASS | even-sector variation |
| D2 | $\Sigma$-EOM $B(\Sigma-P)=0\Leftrightarrow m_2(\Sigma)=m_2(\Psi^{\otimes2})$ | strip $G_2$ ($\det\neq0$) | PASS | `eq:Sigeom`; $m_2$ inversion **not** used |
| D3 | $\Sigma=\Psi^{\otimes2}$ solves the EOM (sufficiency) | substitute | PASS | necessity needs $\ker m_2=0$ → I3 |
| **E1** (reworked) | EOM operator **independently reconstructed from the action gradient** = $m_2=\mathfrak p_{2,2,0}$ | Hessian of $S$, strip $G_2$, compare to $G_2^{-1}V_4$ | PASS | failable (distinguishes $V_4$ from $V_4^T$); no $\mathfrak p_{3,1,0}$ |
| **F1** (reworked) | presentations (A) & (B) give **identical** $\Sigma$-EOM; (B)'s $\omega_2^{\rm symp}$ **genuinely graded-antisym** | build shifted form, count anti-viol, compare EOM | PASS | failable; presentation-independence |
| **G1** (reworked) | $(1,1,0)$: $Q^2=0$ a **nontrivial, solvable** constraint | 3 adjacent $N_{\rm gh}$ $[3,4,5]$ chain; $Q^2$ a priori $\neq0$; solve | PASS | failable (length-2 raising chain) |

**Scope note (no over-claim).** The toy verifies the **sign/factor/structure
bookkeeping** of the completion of square, the two EOM, and the $(2,2,0)$ comparison,
in the physical grading. It does **not** compute the worldsheet vertex content, prove
$\ker m_2=0$, or settle infinite-dimensional non-degeneracy — those are I3 / CFT-level /
numerical-verifier tasks. The structural facts demonstrated — (i) the completion of
square needs $B=V_4$ graded-symmetric, a *vertex* property, *presentation-independent*;
(ii) the $\Sigma$-EOM is a field equation built from $\mathfrak p_{2,2,0}$ alone,
*consistent with* (not equal to) the operator relation R6 — are robust to the toy size.
**Iter-1 revision note:** E1/F1/G1 were rewritten from tautological/vacuous to failable;
the headline was demoted from "HS EOM = master equation at $(2,2,0)$" (a category error,
field eq. vs operator identity) to "action/EOM consistency"; $\hbar_{\rm CFL}$ corrected
$g_s\to g_s^2$; the "presentation (A) forced" strawman was withdrawn.
