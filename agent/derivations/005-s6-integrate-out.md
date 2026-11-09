# Derivation record 005 — S6: integrating out $\Sigma$ returns the $\ell_3$ quartic, $q_{3,1,0}^{\rm transf}=\ell_3$

Date: 2026-06-28
Author agent: computator
Brief: `agent/briefs/done-computator-s6-integrate-out-20260628T133000.md`
Verification: `codes/verify-s6-integrate-out.py` (sympy 1.14.0, 12/12 PASS); reuses the
physical-grading toy of `codes/verify-i3-m2-invertibility.py` /
`codes/verify-omega2-physical.py`.

Reused verbatim (not re-derived): **R1** (HS action + completion of square + Σ-EOM),
**R7** (ω₂/$G_2$ graded-symmetric, non-degenerate, $m_2$ cyclic), **R8** (HS action
$S=\omega\circ\hat{\mathfrak p}(e^\Psi)$; Σ-EOM by stripping $G_2$; $\hbar_{\rm CFL}=g_s^2$),
**R9** ($\Sigma=\Psi^{\otimes2}$ unique on $\operatorname{Sym}^2\mathcal H$ ⟺
$\ker(m_2|_{\operatorname{Sym}^2})=0$; injectivity vs bounded-inverse split, C1).
Structural tool: CFL **Thm 1.3 / 6.1** (`literature/reviews/RPEPEC4L.md`), the
homotopy-transfer / minimal-model algorithm.

---

## Setup

### Assumptions and conventions

- **Sector.** Classical $g=0$, order $g_s^2$ (quartic truncation),
  $\Sigma\in\operatorname{Sym}^2\mathcal H$. Erbin (2023): metric $(-,+,+,+)$,
  $\hbar=c=1$, $\alpha'$ explicit, bra–ket. Closed pairing carries $c_0^-$ (R7).
- **Level-matching (binding).** Every field in $\ker L_0^-\cap\ker b_0^-$;
  $\mathcal H$ abbreviates the level-matched single-string space; $\Sigma$ and
  $\Psi^{\otimes2}$ live in the **off-shell** level-matched bosonic square
  $\operatorname{Sym}^2\mathcal H$ (R9, Step 2).
- **Physical $N_{\rm gh}$ (binding).** $\Psi$ at $N_{\rm gh}=2$ ($\epsilon=0$),
  $\Sigma$ at $N_{\rm gh}=4$ ($\epsilon=0$, note `eq:Sigexpand`), $N_{\rm gh}(m_2)=-2$
  (note `eq:mtwo`). All final objects physical; suspended grading only as an
  intermediate, translated back (§Suspended↔physical).
- **Data (presentation (A), R7/R8).**
  $\omega_1(A,B)=\langle A|c_0^-|B\rangle_{\rm bpz}$, $\Delta=\omega_1^{-1}$,
  $G_2:=\omega_1^{\otimes2}$ (graded-symmetric, non-degenerate, R7);
  $m_2\equiv\mathfrak p_{2,2,0}=\Delta\circ\ell_3:\mathcal H^{\otimes2}\to\mathcal H^{\otimes2}$,
  defined by
  $$
  V_4(X,Y)=G_2(X,m_2Y)=\langle x_1|\ell_3(x_2,y_1,y_2)\rangle,\qquad
  X=x_1\otimes x_2,\ Y=y_1\otimes y_2,\tag{S.1}
  $$
  with $V_4$ the fully graded-symmetric closed cyclic quartic vertex (`eq:V4ell3`).

### The HS action at $O(g_s^2)$ (R1/R8, note `eq:SHS`)

$$
S_{\rm HS}=\tfrac12 V_2(\Psi^2)+\frac{g_s}{3!}V_3(\Psi^3)
\underbrace{-\frac{g_s^2}{4!}V_4(\Sigma,\Sigma)+\frac{2g_s^2}{4!}V_4(\Sigma,\Psi^{\otimes2})}_{=:S_\Sigma[\Sigma,\Psi]}.
\tag{S.2}
$$
The $\Sigma$ sector has a **contact kinetic term** $-\tfrac{g_s^2}{4!}V_4(\Sigma,\Sigma)$
(no $1/L_0^+$ — its "kinetic operator" is the algebraic $m_2$, not $Q_B$) and a
**source/coupling** $+\tfrac{2g_s^2}{4!}V_4(\Sigma,\Psi^{\otimes2})$ to $\Psi^{\otimes2}$.
The relative coefficient is exactly $2:1$ (source : kinetic), from the symmetry
$V_4(\Sigma,\Psi^{\otimes2})=V_4(\Psi^{\otimes2},\Sigma)$ in the completion of square (R1).

### The two routes and the target identity

- **(A) Brute substitution.** Solve the Σ-EOM (R8 `eq:Sigeom`) $m_2(\Sigma)=m_2(\Psi^{\otimes2})$,
  whose unique solution on $\operatorname{Sym}^2\mathcal H$ is $\Sigma=\Psi^{\otimes2}$ (R9),
  and substitute back into $S_\Sigma$.
- **(B) CFL homotopy transfer.** Integrate out the $\Sigma$ leg of the
  $\IBL_\infty$ coderivation (Thm 1.3/6.1): the transferred product on the physical
  $\Psi$ subspace is built from the tree with one internal $\Sigma$ line carrying the
  propagator $h_\Sigma=m_2^{-1}$ (equivalently $V_4^{-1}$).

**Target.** Both routes reproduce the original quartic contact term,
$$
\boxed{\,q_{3,1,0}^{\rm transf}=\ell_3=\mathfrak p_{3,1,0}\,}
$$
i.e. the effective $\Psi$-action's quartic is $+\tfrac{g_s^2}{4!}V_4(\Psi^{\otimes2},\Psi^{\otimes2})
=\tfrac{g_s^2}{4!}\langle\Psi|\ell_3(\Psi,\Psi,\Psi)\rangle$, with the **correct sign and
coefficient** and **no extra terms**.

---

## Derivation

### Route (A) — brute substitution $\Sigma=\Psi^{\otimes2}$

Write $P:=\Psi^{\otimes2}\in\operatorname{Sym}^2\mathcal H$. The Σ sector is
$$
S_\Sigma[\Sigma]=-\frac{g_s^2}{4!}V_4(\Sigma,\Sigma)+\frac{2g_s^2}{4!}V_4(\Sigma,P).
\tag{A.1}
$$
Its stationarity in $\Sigma$ (varying the graded-symmetric bilinear $V_4$ on the even
sector, R8 step 2) gives, after stripping the **non-degenerate** $G_2$ (R7),
$$
\frac{\delta S_\Sigma}{\delta\Sigma}
=-\frac{2g_s^2}{4!}\big(m_2(\Sigma)-m_2(P)\big)=0
\;\Longrightarrow\;
m_2(\Sigma)=m_2(P).
\tag{A.2}
$$
On the off-shell level-matched $\operatorname{Sym}^2\mathcal H$, with $V_4|_{\operatorname{Sym}^2}$
non-degenerate (R9 hypothesis (5.1)), $\ker(m_2|_{\operatorname{Sym}^2})=0$, so (A.2) has
the **unique** solution
$$
\Sigma_\ast=P=\Psi^{\otimes2}.
\tag{A.3}
$$
Substituting (A.3) into (A.1), and using $V_4(P,P)$ symmetric,
$$
S_\Sigma[\Sigma_\ast]
=-\frac{g_s^2}{4!}V_4(P,P)+\frac{2g_s^2}{4!}V_4(P,P)
=\boxed{\,+\frac{g_s^2}{4!}V_4(\Psi^{\otimes2},\Psi^{\otimes2})\,}.
\tag{A.4}
$$
The $2:1$ ratio is exactly what produces $-1+2=+1$. Equivalently, by completion of
square (R1),
$$
S_\Sigma[\Sigma]=-\frac{g_s^2}{4!}V_4(\Sigma-P,\Sigma-P)+\frac{g_s^2}{4!}V_4(P,P),
\tag{A.5}
$$
whose first term vanishes at the saddle $\Sigma=P$ (the Gaussian elimination is exact),
leaving (A.4). Hence the effective $\Psi$-action is
$$
S_{\rm eff}[\Psi]=\tfrac12 V_2(\Psi^2)+\frac{g_s}{3!}V_3(\Psi^3)
+\frac{g_s^2}{4!}V_4(\Psi^{\otimes2},\Psi^{\otimes2}),
\tag{A.6}
$$
the $g_s^2$-truncated closed-string $\Loo$ action — the quartic contact term restored
with its standard, uniform-sign coefficient $+\tfrac{g_s^2}{4!}$ (consistent with the
$\Psi$-EOM R8 (2.4): varying $+\tfrac{g_s^2}{4!}V_4$ yields $+\tfrac{g_s^2}{3!}\ell_3(\Psi^{\otimes3})$).

### Route (B) — CFL homotopy transfer / propagator form

The HS-extended theory is an $\IBL_\infty$/$\Loo$ structure on
$\mathcal H_{\rm tot}=\mathcal H_\Psi\oplus\mathcal H_\Sigma$ in which the physical
quartic $\mathfrak p_{3,1,0}=\ell_3$ has been **strictified to zero** and replaced by
(i) a two-input/one-output coupling vertex $V:\mathcal H_\Psi^{\otimes2}\to\mathcal H_\Sigma$
(the source term $V_4(\Sigma,\Psi^{\otimes2})$) and (ii) the $\Sigma$ contact kinetic
term $V_4(\Sigma,\Sigma)$ whose operator is $m_2$. Integrating out $\Sigma$ is the
minimal-model / homotopy transfer of CFL Thm 1.3/6.1 from $\mathcal H_{\rm tot}$ to
$\mathcal H_\Psi$, with the **homotopy** $h$ chosen as the $\Sigma$ propagator: $h=0$ on
$\mathcal H_\Psi$, $h=m_2^{-1}$ (equivalently $V_4^{-1}$) on $\mathcal H_\Sigma$.

The transferred operation $\mathfrak q_{3,1,0}$ ($K=3$ inputs, $L=1$ output, $G=0$) has
**no direct term** ($\mathfrak p_{3,1,0}^{\rm tot}=0$ in the strictified theory), so it is
built entirely from the transfer recursion's $\widetilde R$ tree (CFL eq. 1005): the
unique genus-0 tree with four external $\Psi$ legs and one internal $\Sigma$ line, two
coupling vertices $V$ joined by $h$:
$$
\mathfrak q_{3,1,0}^{\rm transf}(\Psi^{\otimes3})
\ \longleftrightarrow\
V_4^{\rm transf}(P,P)=G_2\big(V\,P\,,\,h\,V\,P\big).
\tag{B.1}
$$
Concretely, with $V\,P=m_2 P$ (the coupling is $m_2$) and $h=m_2^{-1}$,
$$
G_2(m_2P\,,\,m_2^{-1}m_2P)=G_2(m_2P\,,\,P)=G_2(P,m_2P)=V_4(P,P),
\tag{B.2}
$$
the propagator **cancels exactly one vertex factor**, rebuilding the quartic vertex.
Tracking the coefficients via the Gaussian extremum
$S_\Sigma=G_2(\Sigma,A\Sigma)+G_2(\Sigma,b)$ with $A=-\tfrac{g_s^2}{4!}m_2$,
$b=\tfrac{2g_s^2}{4!}m_2P$, the extremal value is
$$
S_\Sigma^\ast=-\tfrac14\,G_2(b,A^{-1}b)
=-\tfrac14\Big(\tfrac{2g_s^2}{4!}\Big)^2(-4!\,g_s^{-2})\,G_2(m_2P,m_2^{-1}m_2P)
=+\frac{g_s^2}{4!}V_4(P,P),
\tag{B.3}
$$
the propagator $A^{-1}=-4!\,g_s^{-2}m_2^{-1}$ being the internal $\Sigma$ line. Routes
(A) and (B) **agree**: (B.3) = (A.4).

### Identification $q_{3,1,0}^{\rm transf}=\ell_3$

The integrate-out delivers the effective quartic as a bilinear **form**
$V_4^{\rm transf}$ on $\operatorname{Sym}^2\mathcal H$ via
$S_\Sigma^\ast=\tfrac{g_s^2}{4!}V_4^{\rm transf}(P,P)$; by (A.4)/(B.3),
$$
V_4^{\rm transf}=V_4\quad\text{(on }\operatorname{Sym}^2\mathcal H\text{, identical entries, no extra terms).}
\tag{C.1}
$$
The single-output products are obtained from their quartic forms by the **same**
index-raising $\Delta=\omega_1^{-1}$ (`eq:V4ell3`/`eq:mtwo`):
$\ell_3=\Delta\circ V_4$ and $q_{3,1,0}^{\rm transf}=\Delta\circ V_4^{\rm transf}$. Since
$\Delta$ is a bijection, (C.1) gives
$$
\boxed{\,q_{3,1,0}^{\rm transf}=\Delta\circ V_4^{\rm transf}=\Delta\circ V_4=\ell_3=\mathfrak p_{3,1,0}\,}.
\tag{C.2}
$$
This is the dynamical counterpart of R9: there the Σ-EOM had the unique solution
$\Sigma=\Psi^{\otimes2}$ (kernel/uniqueness); here substituting it back (or running the
transfer) reproduces exactly the $\ell_3$ quartic of the original $\Loo$ theory.

---

## Commentary

- **(A.1)–(A.4): the $G_2$ bookkeeping and why the cross-term doubles.** The Σ kinetic
  term $V_4(\Sigma,\Sigma)=G_2(\Sigma,m_2\Sigma)$ is a symmetric bilinear (R7/R8 step 1a),
  and the source $V_4(\Sigma,\Psi^{\otimes2})=G_2(\Sigma,m_2\Psi^{\otimes2})$ enters with
  coefficient $2$ because in $V_4(\Sigma-P,\Sigma-P)$ the cross-term
  $-2V_4(\Sigma,P)$ has the factor $2$ from $V_4(\Sigma,P)=V_4(P,\Sigma)$. That $2$ is
  precisely what makes the saddle value $-1+2=+1$, restoring the quartic with the
  **same** coefficient it had before the HS trade.
- **The sign (subtlety, flagged).** Integrating $\Sigma$ out of `eq:SHS` yields
  $+\tfrac{g_s^2}{4!}V_4(\Psi^4)$ — the **uniform-sign** quartic of the standard
  closed-string action (same sign as the kinetic $\tfrac12 V_2$ and cubic $\tfrac{g_s}{3!}V_3$
  terms), consistent with the $\Psi$-EOM R8 (2.4). The overview's intermediate
  `eq:SHSderive` writes the *discarded* pure-$\Psi$ term as $-\tfrac{g_s^2}{4!}V_4(\Psi^4)$
  and calls it "the original quartic"; this opposite sign is a bookkeeping artefact of
  that intermediate presentation (the term that is dropped to pass from `eq:SHSderive` to
  `eq:SHS` is **minus** the physical quartic), and does **not** affect `eq:SHS` itself.
  The physically meaningful and correct statement is route (A): `eq:SHS` integrated out
  $=+\tfrac{g_s^2}{4!}V_4(\Psi^4)$. (Minor documentation inconsistency in the
  `eq:SHSderive` prose — flagged for the critic; the boxed `eq:SHS` and `eq:Sigeom`
  are correct.)
- **(B.1)–(B.3): the homotopy/propagator choice.** Route (B) needs a genuine propagator
  $h=m_2^{-1}=V_4^{-1}\circ G_2$ on $\operatorname{Sym}^2\mathcal H$, i.e. a **bounded
  inverse** of the contact kinetic operator — this is the C1 residual of R9: strictly
  stronger than the injectivity ($\ker=0$) that route (A)'s uniqueness uses. CFL Thm
  1.3/6.1 guarantees the transferred $\IBL_\infty$ structure exists over a field of
  characteristic $0$ given the deformation retract data $(\mathcal H_{\rm tot}=H\oplus B\oplus A,h)$;
  the natural retract here sends $H=\mathcal H_\Psi$ and $h$ = the $\Sigma$ propagator. The
  $\widetilde R$ recursion produces exactly one tree at $(3,1,0)$ (two cubic-type couplings,
  one internal line), and its value (B.2) is $V_4$ — the propagator cancels one vertex
  factor. The $L!,K!$ symmetry factors of CFL eq. 1005 reproduce the $\tfrac{1}{4!}$ and the
  doubling already visible in route (A); the toy checks the net coefficient is $+\tfrac{1}{4!}$.
- **Identification with $\ell_3$.** $V_4$ and $V_4^{\rm transf}$ being equal as forms,
  and $\ell_3,\,q_3^{\rm transf}$ being their $\Delta$-raisings, the products coincide.
  The toy builds $\ell_3=\Delta\circ V_4$ explicitly and verifies the round-trip
  $\omega_1(x_1,\ell_3(x_2,y_1,y_2))=V_4(x_1,x_2,y_1,y_2)$ for all insertions.

---

## Suspended ↔ physical translation

The CFL transfer (Thm 6.1) and the $\IBL$ products are naturally defined on the
suspended module $C[1]$, where $m_2=\mathfrak p_{2,2,0}$ is a genuine degree
$-2d(k+g-1)-1$ operation and the homotopy $h$ has CFL morphism degree $-2d(k+g-1)$
(degree $+1$ relative to $m_2$). As in R7/R8/R9, the **entries** of $G_2$, $V_4$, $m_2$,
and the transferred form $V_4^{\rm transf}$ are identical in the suspended (B) and
physical (A) presentations; only Koszul-sign labels differ. The invariant object is the
subspace, not the word: the inert kernel $\wedge^2\mathcal H$ in physical parity becomes
the graded-symmetric square in the one-unit-shifted parity (R9 M4). We state all final
objects in **physical** $N_{\rm gh}$: $\Psi$ at $N_{\rm gh}=2$, $\Sigma$ at $N_{\rm gh}=4$,
$N_{\rm gh}(m_2)=-2$; $\operatorname{Sym}^2\mathcal H$ is the physical bosonic ($\epsilon=0$)
sector where $\Psi^{\otimes2}$ lives; $q_{3,1,0}^{\rm transf}$ and $\ell_3=\mathfrak p_{3,1,0}$
carry the same physical ghost number. The toy runs entirely in physical parity, so no
suspended grading enters the final checks.

---

## Result

### Lemma (candidate R10) — integrating out $\Sigma$ reproduces the $\ell_3$ quartic

> **Hypotheses.** (H1) $\omega_1=(\cdot,c_0^-\cdot)_{\rm bpz}$ non-degenerate on
> $\ker L_0^-\cap\ker b_0^-$ (R7), so $\Delta=\omega_1^{-1}$, $G_2=\omega_1^{\otimes2}$
> non-degenerate. (H2) $V_4$ fully graded-symmetric closed cyclic quartic vertex,
> $V_4(X,Y)=G_2(X,m_2Y)$, $m_2=\Delta\circ\ell_3$ (`eq:mtwo`). (H3) $\Sigma,\Psi^{\otimes2}$
> level-matched in $\operatorname{Sym}^2\mathcal H$, $N_{\rm gh}=4$. (H4) $V_4|_{\operatorname{Sym}^2}$
> non-degenerate (R9 hypothesis (5.1)); for the propagator route (B) also a **bounded**
> inverse $V_4^{-1}$ (closed range, R9 C1).
>
> **Claim.** Under (H1)–(H4), integrating out $\Sigma$ from the HS action `eq:SHS` — via
> the Σ-EOM saddle $\Sigma=\Psi^{\otimes2}$ (route A, R9), equivalently via CFL
> homotopy transfer of the $\Sigma$ leg with propagator $h=m_2^{-1}$ (route B,
> Thm 1.3/6.1) — yields the effective $\Psi$-action
> $$
> S_{\rm eff}[\Psi]=\tfrac12 V_2(\Psi^2)+\frac{g_s}{3!}V_3(\Psi^3)
> +\frac{g_s^2}{4!}V_4(\Psi^{\otimes2},\Psi^{\otimes2}),
> $$
> with the quartic restored at its standard uniform-sign coefficient $+\tfrac{g_s^2}{4!}$
> and **no extra terms**. The transferred bilinear form equals the original
> ($V_4^{\rm transf}=V_4$), hence the transferred product equals the closed-string cubic
> product:
> $$
> q_{3,1,0}^{\rm transf}=\ell_3=\mathfrak p_{3,1,0}.
> $$
> Routes (A) and (B) **agree**; the internal $\Sigma$ line $V_4^{-1}$ cancels exactly one
> vertex factor, the tree rebuilding $V_4=\ell_3$.
>
> **Status of the hypotheses — OPEN (CFT-level, same as R9).** (H2) full graded symmetry
> of $V_4$ and (H4) non-degeneracy of $V_4$ on $\operatorname{Sym}^2(\ker L_0^-\cap\ker b_0^-)$
> are the **same two residuals** R9 carries; S6 inherits them because the substitution uses
> $\Sigma=\Psi^{\otimes2}$ (R9). Route (B) inherits in addition the **bounded-inverse**
> condition (C1): when $V_4|_{\operatorname{Sym}^2}$ degenerates, the propagator fails to
> exist and route (B) breaks (route A's saddle becomes non-unique, R9 T3).

### Promotability

**Candidate R10, to be entered after the critic loop (deferred to next session).**
Status should be **Verified (toy-level algebraic identity; conditional reduction)**, in
the **same scoping style as R7/R8/R9**. The **Verified algebraic core** (toy, 12/12 PASS):
- (i) Route (A): the Σ-EOM saddle $\Sigma=\Psi^{\otimes2}$ substituted into `eq:SHS` gives
  the effective quartic $+\tfrac{g_s^2}{4!}V_4(\Psi^{\otimes2},\Psi^{\otimes2})$ — exact
  coefficient $+\tfrac{1}{4!}$, correct sign (A1–A4).
- (ii) Route (B): the propagator/homotopy-transfer integrate-out **agrees** with (A); the
  internal $\Sigma$ line is $V_4^{-1}$ and cancels one vertex factor, rebuilding $V_4$ (B1–B3).
- (iii) Identification: $V_4^{\rm transf}=V_4$ (no extra terms) ⇒ $q_{3,1,0}^{\rm transf}=\ell_3$
  via the shared $\Delta$-raising (C1, C2).

**Explicitly excluded from the Verified core (OPEN, CFT-level):** (H2) $V_4$ graded
symmetry and (H4) $V_4$ non-degeneracy on $\operatorname{Sym}^2(\ker L_0^-\cap\ker b_0^-)$
— **the same residuals as R9** — plus the **bounded $V_4^{-1}$** (C1) needed for the
propagator route (B). The toy does **not** compute the worldsheet $c_0^-$, $\ell_3$, $V_4$
on the genuine infinite-dimensional $\mathcal H$. No over-claim: S6 is the *dynamical*
statement conditional on exactly R9's inputs.

### Established vs. open

**Established (toy-verified algebraic identity, physical $N_{\rm gh}$).**
- Route (A) substitution reproduces $+\tfrac{g_s^2}{4!}V_4(\Psi^4)$, exact coefficient and
  sign; completion of square exact (A1–A4).
- Route (B) propagator/transfer agrees with (A); propagator $=V_4^{-1}$; internal line
  cancels one vertex factor (B1–B3).
- $V_4^{\rm transf}=V_4$ ⇒ $q_{3,1,0}^{\rm transf}=\ell_3$ (C1, C2).
- Scope/sharpness: degenerate $V_4|_{\operatorname{Sym}^2}$ ⇒ route (B) propagator fails,
  route (A) saddle non-unique (D1); sign guard (D2).

**Open (not settled here; CFT-level, inherited from R9).**
- (H4)/(5.1) non-degeneracy of $V_4$ on $\operatorname{Sym}^2(\ker L_0^-\cap\ker b_0^-)$.
- (H2) full graded symmetry of the closed cyclic quartic vertex $V_4$.
- (C1) bounded inverse $V_4^{-1}$ (closed range) for the integrate-out / propagator —
  strictly stronger than R9 injectivity. → numerical-verifier / CFT.

### Proposed next step

After the deferred critic loop promotes R10: **I4** (cheap citation, arXiv:1905.06785
eq. (5.55)) and **Phase 6** (Riemann-surface interpretation of the contact-term /
no-pole property — the geometric meaning of the $\Sigma$ propagator $V_4^{-1}$).

---

## Verification

Script: `codes/verify-s6-integrate-out.py` (sympy 1.14.0, **12 checks, all PASS**).
Toy: the physical-grading proxy of `verify-i3-m2-invertibility.py` — three $N_{\rm gh}=2$
and three $N_{\rm gh}=3$ single-string states, $\omega_1$ pairing $2\leftrightarrow3$,
$G_2=\omega_1^{\otimes2}$, fully graded-symmetric $V_4$ on the $N_{\rm gh}=4$ block,
$\operatorname{Sym}^2$/$\wedge^2$ split explicit. $\Psi^{\otimes2}$ built from a generic
$N_{\rm gh}=2$ vector. The overall $g_s^2$ is an inert prefactor, dropped in the toy.
Each check is an internal algebraic self-check, **not** an independent CFT re-derivation.

| ID | Check | Method | Outcome | Scope |
| --- | --- | --- | --- | --- |
| S0a | $G_2$ non-deg (R7); $V_4|_{\operatorname{Sym}^2}$ invertible (R9 generic regime) | $\det G_2$, $\det V_4|_{\operatorname{Sym}^2}$ | PASS | well-posedness; bounded $V_4^{-1}$ assumed (C1 flagged) |
| A1 | Σ-EOM $m_2(\Sigma)=m_2(\Psi^{\otimes2})$ unique soln $\Sigma=\Psi^{\otimes2}$ on $\operatorname{Sym}^2$ | strip non-deg $V_S$, solve | PASS | R9 injectivity |
| A2 | effective quartic coeff exactly $+\tfrac1{4!}$ (the $2{:}1$ ratio gives $-1+2=+1$) | substitute saddle | PASS | coefficient bookkeeping |
| A3 | effective quartic $=+\tfrac1{4!}V_4(\Psi^{\otimes2},\Psi^{\otimes2})$, correct sign | value match | PASS | matches R8 (2.4) uniform sign |
| A4 | completion of square; saddle piece vanishes | symbolic diff | PASS | `eq:SHSderive` (R1), Gaussian exact |
| B1 | routes agree: $S^\ast=-\tfrac14 b^TA^{-1}b=$ route-A value | propagator extremum | PASS | (A)=(B) |
| B2 | propagator (internal Σ line) $A^{-1}=-4!\,V_S^{-1}\sim V_4^{-1}$ | matrix identity | PASS | needs bounded inverse (C1) |
| B3 | internal-line cancellation $(V_Sp)^TV_S^{-1}(V_Sp)=p^TV_Sp$ | symbolic | PASS | tree rebuilds $V_4=\ell_3$ |
| C1 | $V_4^{\rm transf}=V_4$ on $\operatorname{Sym}^2$ ⇒ $q_{3,1,0}^{\rm transf}=\ell_3$ | matrix equality | PASS | no extra terms; shared $\Delta$-raising |
| C2 | explicit $\ell_3=\Delta\circ V_4$ well-defined, round-trip reconstructs $V_4$ | solve $\omega_1$ raising, check all insertions | PASS | $q_3^{\rm transf}=\ell_3$ componentwise |
| D1 | scope: degenerate $V_4|_{\operatorname{Sym}^2}$ ⇒ propagator $A^{-1}$ fails (route B breaks); saddle non-unique (R9 T3) | tune $\det=0$, rank | PASS | ties S6 to H2+(5.1)+C1 residual |
| D2 | sign guard: effective quartic $+$ sign (the $2{:}1$ ratio gives $+1$) | sign of coeff | PASS | guards `eq:SHSderive` sign subtlety |

**Scope note (no over-claim).** The toy certifies the **algebraic identity**
$q_{3,1,0}^{\rm transf}=\ell_3$ (coefficient $+\tfrac1{4!}$, sign, no extra terms) and the
**agreement of routes (A) and (B)**, in physical parity. It does **not** compute the
worldsheet vertex content, nor certify (H2), (H4)/(5.1), or the bounded $V_4^{-1}$ (C1) —
the same CFT-level residuals R9 carries, with C1 the additional infinite-dimensional input
specific to the integrate-out. S6 is the dynamical complement of R9, conditional on exactly
R9's hypotheses.
