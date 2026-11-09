# Derivation record 004 — I3: invertibility of $m_2=\mathfrak p_{2,2,0}=\Delta\circ\ell_3$ and the auxiliarity of $\Sigma$

Date: 2026-06-25 (revised 2026-06-28 after critic iter 1, report
`agent/reports/critic-i3-m2-invertibility-20260628T120000.md`).
Author agent: computator
Brief: `agent/briefs/done-computator-i3-m2-invertibility-20260625T120000.md`;
revision brief `agent/briefs/done-computator-i3-revision-20260628T123000.md`.
Verification: `codes/verify-i3-m2-invertibility.py` (sympy 1.14.0, 10/10 PASS).
Reuses the physical-grading machinery of `codes/verify-i2-ibl-action.py` /
`codes/verify-omega2-physical.py`.

Reused verbatim (not re-derived): **R1** (HS action, completion of square, Σ-EOM),
**R3** (open-stub auxiliary propagator regular as $L_0\to0$), **R7** (ω₂/$G_2$ graded
symmetric, non-degenerate, $m_2$ cyclic), **R8** (Σ-EOM derivation, sufficiency
$\Sigma=\Psi^{\otimes2}$). Precedents: **R4**/FBSP8UQ9 §8.3 (YM $\Box$-invertibility),
C9ETB6WE §2 (open-stub single-output analogue).

---

## Setup

### Assumptions and conventions

- **Sector.** Classical $g=0$, order $g_s^2$ (quartic truncation),
  $\Sigma\in\mathcal H^{\otimes2}$. Erbin (2023): metric $(-,+,+,+)$, $\hbar=c=1$,
  $\alpha'$ explicit, bra–ket. Closed-string pairing carries $c_0^-$ (R7).
- **Level-matching (binding, plan Rev-2 §3).** Every closed-string field, physical
  or auxiliary, is level-matched: $\Sigma\in\ker L_0^-\cap\ker b_0^-$ is a
  **mandatory constraint**, never the complement. The retired form
  "$\Sigma\in(\ker L_0^-)^c$" is **not** used. The pole/auxiliarity question concerns
  $L_0^+$ (the propagator denominator), not $L_0^-$. All Hilbert spaces below are the
  level-matched ones; "$\mathcal H$" abbreviates the level-matched single-string space.
- **Physical $N_{\rm gh}$ (binding, plan Rev-2 §8).** Final objects in physical
  parametrization: $\Psi$ at $N_{\rm gh}=2$, $\Sigma$ at $N_{\rm gh}=4$
  (note `eq:Sigexpand`), $N_{\rm gh}(m_2)=-2$ (note `eq:mtwo`). Physical parity
  $\epsilon=N_{\rm gh}\bmod2$. The suspended/degree-shifted field is used only as an
  intermediate; an explicit translation step (§Suspended↔physical) is carried.
- **$m_2$ is the SQUARE map.** $m_2:\mathcal H^{\otimes2}\to\mathcal H^{\otimes2}$ has
  two inputs and two outputs. The auxiliarity-relevant property is **injectivity**
  $\ker m_2=0$ — equivalently absence of a null vector of the bilinear form $V_4$ —
  **on the bosonic sector $\operatorname{Sym}^2\mathcal H$**, *not* on the full
  $\mathcal H^{\otimes2}$ (where $\wedge^2\mathcal H\subseteq\ker m_2$ always, so
  $\ker m_2=0$ is never attainable; see the Setup statement and Step 2). Injectivity
  ($\ker=0$) is weaker than invertibility (bounded inverse) in infinite dimensions; only
  injectivity is needed for auxiliarity (C1). We never use the single-output reading
  $\langle A|c_0^-|m_2(B,C)\rangle=\ell_3(A,B,C)$ as the map.

### Data (presentation (A), R7/R8)

$$
\omega_1(A,B)=\langle A|c_0^-|B\rangle_{\rm bpz},\qquad \Delta=\omega_1^{-1},\qquad
G_2:=\omega_1^{\otimes2},\tag{S.1}
$$
with $\omega_1$ odd symplectic on the $\Psi$ sector (graded antisymmetric,
non-degenerate on $\ker L_0^-\cap\ker b_0^-$) and $G_2$ the graded-**symmetric**,
non-degenerate Poisson pairing on $\mathcal H^{\otimes2}$ (R7). **Bracket shorthand
(M2).** Throughout, $\langle\,\cdot\,|\,\cdot\,\rangle$ denotes the $c_0^-$-carrying
closed-string BPZ pairing: on one string $\langle A|B\rangle:=\langle A|c_0^-|B\rangle_{\rm bpz}=\omega_1(A,B)$,
and on $\mathcal H^{\otimes2}$, $\langle X|Y\rangle:=G_2(X,Y)$ with
$G_2=(\,\cdot\,|c_0^-|\,\cdot\,)_{\rm bpz}^{\otimes2}$ (one $c_0^-$ per string); the
$c_0^-$ insertions are the entire content of the closed symplectic structure and are
never dropped. The two-output product (note `eq:mtwo`) and its defining relation:
$$
m_2\equiv\mathfrak p_{2,2,0}=\Delta\circ\ell_3:\mathcal H^{\otimes2}\to\mathcal H^{\otimes2},
\qquad
V_4(X,Y)=G_2\big(X,\,m_2 Y\big)=\langle x_1\otimes x_2\,|\,c_0^-\!\otimes c_0^-\,|\,m_2(y_1\otimes y_2)\rangle,
\tag{S.2}
$$
$X=x_1\otimes x_2$, $Y=y_1\otimes y_2$, with $V_4$ the fully graded-symmetric closed
cyclic quartic vertex, $V_4(X,Y)=\langle x_1|c_0^-|\ell_3(x_2,y_1,y_2)\rangle$ on the
single-output side.

**Ghost-number balance fixing $N_{\rm gh}(m_2)$ (M1).** The relation
$V_4(X,Y)=G_2(X,m_2Y)$ fixes the ghost number of $m_2$ as a difference, independent of
the absolute saturation convention. $V_4$ is the physical closed quartic, saturated at
$N_{\rm gh}(X)+N_{\rm gh}(Y)$ on four physical insertions; $G_2=\omega_1^{\otimes2}$ is
saturated at $N_{\rm gh}(X)+N_{\rm gh}(m_2Y)$. Equality of the two saturations for all
$X$ forces
$$
N_{\rm gh}(m_2)\;:=\;N_{\rm gh}(m_2Y)-N_{\rm gh}(Y)\;=\;\big[N_{\rm gh}(Y)\big]_{V_4}-\big[N_{\rm gh}(m_2Y)\big]_{G_2}\ \text{matched}\ \Rightarrow\ N_{\rm gh}(m_2)=-2,
$$
the value fixed in note `eq:mtwo` (operator-grading convention of
`eq:Sigexpand`/`eq:mtwo`, in which a *lowering* product carries negative ghost number;
$\Sigma$ at $N_{\rm gh}=4$, $\Psi^{\otimes2}$ at $N_{\rm gh}=4$, $m_2\Sigma$ then at
$N_{\rm gh}=2$). We take $N_{\rm gh}(m_2)=-2$ as fixed there; its sign plays **no** role
in any equivalence below, which depend only on $m_2$ being a fixed linear map and on
$G_2$ being non-degenerate.

### The precise statement to establish (scoped to $\operatorname{Sym}^2\mathcal H$ from the outset)

**Scope (S1, C4).** The auxiliary $\Sigma$ and the source $\Psi^{\otimes2}$ are
level-matched two-string fields living in the **off-shell** graded-symmetric square
$\operatorname{Sym}^2\mathcal H$ (the bosonic sector; $\Psi^{\otimes2}$ is manifestly
symmetric). "$\ker m_2$" below always means the kernel on the **full off-shell
level-matched** $\operatorname{Sym}^2\mathcal H$ — not on $Q$-cohomology, and not on the
full $\mathcal H^{\otimes2}$. (Off-shell scope matters: R6 records that
$m_2=\mathfrak p_{2,2,0}$ is $Q$-exact, but a $Q$-exact operator need not have a large
kernel off-shell, so R6 is fully consistent with $\ker(m_2|_{\operatorname{Sym}^2})=0$.)

**Why not the full $\mathcal H^{\otimes2}$ (move the $\wedge^2$ remark up front, S1).**
$V_4$ is fully graded-symmetric, so it annihilates the graded-antisymmetric square:
$\wedge^2\mathcal H\subseteq\ker V_4=\ker m_2$ on the full $\mathcal H^{\otimes2}$
(proved in Step 2). Hence $\ker m_2=0$ is **never** satisfiable on
$\mathcal H^{\otimes2}$, and the equivalence below would be **vacuous** if stated there.
The antisymmetric square is moreover physically inert (decoupling, Step 2 / C3), so the
correct arena is $\operatorname{Sym}^2\mathcal H$ throughout.

From R8 (note `eq:Sigeom`): the $\Sigma$-EOM is
$$
m_2(\Sigma)=m_2(\Psi^{\otimes2}),\qquad \Sigma,\Psi^{\otimes2}\in\operatorname{Sym}^2\mathcal H,\tag{S.3}
$$
derived by stripping the **non-degenerate** $G_2$ — uses $G_2$ invertibility, **not**
$m_2$. $\Sigma=\Psi^{\otimes2}$ solves (S.3) (sufficiency, R8). Writing
$\Xi:=\Sigma-\Psi^{\otimes2}\in\operatorname{Sym}^2\mathcal H$, (S.3) is $m_2(\Xi)=0$.
Hence, on the level-matched symmetric square,
$$
\boxed{\ \Sigma=\Psi^{\otimes2}\ \text{is the \emph{unique} solution of (S.3) in}\ \operatorname{Sym}^2\mathcal H
\iff \ker\!\big(m_2|_{\operatorname{Sym}^2\mathcal H}\big)=0.\ }\tag{S.4}
$$
"$\Sigma$ purely auxiliary" (no independent propagating d.o.f., only the algebraic
constraint $\Sigma=\Psi^{\otimes2}$) is exactly $\ker(m_2|_{\operatorname{Sym}^2})=0$,
i.e. **injectivity** of $m_2$ on $\operatorname{Sym}^2\mathcal H$ (C1: auxiliarity needs
only injectivity, not a bounded inverse — see Step 1).

---

## Derivation

### Step 1 — structural reduction $\ker m_2=\ker V_4$

$G_2$ is non-degenerate (R7). From (S.2), as linear maps on $\mathcal H^{\otimes2}$,
$$
m_2=G_2^{-1}\circ V_4,\tag{1.1}
$$
where $V_4$ now denotes the **bilinear-form-as-operator**
$X\mapsto V_4(\,\cdot\,,X)$ (one index raised, the other free). Since $G_2^{-1}$ is a
bijection,
$$
\boxed{\ \ker m_2=\ker V_4,\qquad \ker m_2=0 \iff V_4\ \text{has no null vector (injective).}\ }
\tag{1.2}
$$
This is the precise equivalence the brief asks for: **injectivity of the square map
$m_2$ ($\ker m_2=0$) on the level-matched space $=$ absence of a null vector of the
quartic contact vertex $V_4$.**

**Injective vs. invertible in infinite dimensions (C1).** Auxiliarity — uniqueness of
the EOM solution (S.4) — needs only **injectivity** $\ker m_2=0$, i.e. that $0$ is not
an eigenvalue. It does *not* require $m_2$ to be invertible. On the genuine
infinite-dimensional $\mathcal H$ (the regime of (5.1)) the two are inequivalent: $0$ may
lie in the **continuous / approximate** spectrum (an approximate null sequence
$\|m_2 X_n\|\to0$, $\|X_n\|=1$, with no normalizable null vector), and the range need not
be closed. Conversely, *actually integrating $\Sigma$ out* — the S6 / homotopy-transfer
step, which inserts a propagator $V_4^{-1}$ — needs a genuine **bounded inverse** (closed
range and surjectivity), an extra infinite-dimensional requirement strictly stronger than
the injectivity (5.1) settles. The boxes below therefore say "no null vector / injective",
never "invertible", except where the propagator (integrate-out) version is explicitly
meant.

**Spectral content (M3).** No spectral input about $\ell_3$ is needed *for the
equivalence* (1.2) — $G_2$ non-degeneracy does all the work there. The spectral content
is exactly the open residual (5.1): whether $\ell_3$ admits a symmetric level-matched
null vector. (Toy: T1a $\det G_2\neq0$; T1b $G_2 m_2=V_4$; T1c
$\operatorname{rank}m_2=\operatorname{rank}V_4$.)

### Step 2 — the symmetric/antisymmetric split: $\wedge^2\mathcal H$ is an unphysical kernel

$V_4$ is **fully graded-symmetric** (closed cyclic vertex, R7). On the physical even
sector ($\epsilon=0$, where $N_{\rm gh}=4$ states live) the two slots of a two-particle
state $X=x_1\otimes x_2$ are exchanged with **no** Koszul sign, so $V_4(\,\cdot\,,X)$
depends only on the symmetric part of $X$:
$$
V_4\big(\,\cdot\,,\,x_1\otimes x_2-x_2\otimes x_1\big)=0.\tag{2.1}
$$
Therefore on the **full** $\mathcal H^{\otimes2}$,
$$
\wedge^2\mathcal H\ \subseteq\ \ker V_4=\ker m_2.\tag{2.2}
$$

**Why the $\wedge^2$ kernel is harmless: decoupling, not "bosonic" (C3).** The
antisymmetric part of $\Sigma$ does not appear **anywhere** in the action. $V_4$
annihilates $\wedge^2\mathcal H$ in *both* terms that contain $\Sigma$ (R1/R8): the
kinetic term $-\tfrac{g_s^2}{4!}V_4(\Sigma,\Sigma)$ and the source term
$+\tfrac{2g_s^2}{4!}V_4(\Sigma,\Psi^{\otimes2})$. Decomposing
$\Sigma=\Sigma_{\rm sym}\oplus\Sigma_{\rm anti}$, every occurrence
$V_4(\Sigma,-)=V_4(\Sigma_{\rm sym},-)$ by (2.1), so $\Sigma_{\rm anti}$ is **neither
sourced nor propagating** — it is absent from the action and can be consistently
truncated. This is airtight regardless of any "bosonic" declaration: even if one
allowed an antisymmetric component of the auxiliary field, decoupling removes it. The
relevant arena is therefore $\operatorname{Sym}^2\mathcal H$, where $\Psi^{\otimes2}$
also lives.

**Symmetric outputs: $m_2(\operatorname{Sym}^2)\subseteq\operatorname{Sym}^2$ (C2).**
The equivalence (2.3) below uses $V_4|_{\operatorname{Sym}^2}(X,Y)=G_2(X,m_2Y)$ with
$X,Y\in\operatorname{Sym}^2$. Because $G_2=\omega_1^{\otimes2}$ is **block-diagonal**
w.r.t. the symmetric/antisymmetric split, $G_2(X,m_2Y)=0$ for all symmetric $X$ forces
only the **symmetric component** of $m_2Y$ to vanish. The equivalence to $m_2Y=0$
therefore requires that $m_2$ have **symmetric outputs**,
$m_2(\operatorname{Sym}^2)\subseteq\operatorname{Sym}^2$. This holds as a consequence of
the *full* graded symmetry of $V_4$ (symmetry in the two output slots $x_1,x_2$, not
only the input slots): for symmetric $Y$, $G_2\big((x_1\otimes x_2-x_2\otimes x_1),m_2Y\big)
=V_4(x_1\otimes x_2-x_2\otimes x_1,Y)=0$ by (2.1) applied to the output slots, so the
antisymmetric component of $m_2Y$ pairs to zero against the (non-degenerate) $G_2$ and
hence vanishes. Without symmetric outputs a symmetric $Y\neq0$ with $m_2Y$ purely
antisymmetric would satisfy $V_4|_{\operatorname{Sym}^2}(\,\cdot\,,Y)=0$ yet $m_2Y\neq0$,
breaking (2.3); symmetric outputs is exactly what excludes this. (Toy: new check T1e,
$m_2(\operatorname{Sym}^2)\subseteq\operatorname{Sym}^2$.)

Restricting to $\operatorname{Sym}^2\mathcal H$, with symmetric outputs in force:
$$
\boxed{\ \ker\big(m_2|_{\operatorname{Sym}^2\mathcal H}\big)=0
\iff V_4\ \text{non-degenerate (no null vector) on}\ \operatorname{Sym}^2\mathcal H.\ }\tag{2.3}
$$
(Toy: T1d $m_2|_{\wedge^2}=0$ explicitly, $\dim\wedge^2=3$ in the toy; T1e symmetric
outputs; T2a generic $V_4|_{\operatorname{Sym}^2}$ has nonzero determinant, $m_2$
injective there; T2b $\ker(m_2|_{\operatorname{Sym}^2})=0\Rightarrow\Xi=0$.)

This refinement is a genuine output of the computation, not present in the note's DC1
heuristic, and must be carried into any R9 statement: **auxiliarity is a statement on
$\operatorname{Sym}^2\mathcal H$.**

### Step 3 (HEURISTIC / MOTIVATION ONLY — not part of the verified core)

> **Warning.** Nothing in this step is used to establish the equivalence (1.2), (2.3),
> (4.1), or the counterexample structure (4.2). It collects *motivation* for expecting
> (5.1) to hold, and is honest about why that motivation is **not** evidence and does
> **not** transfer to the infinite-dimensional vertex. The earlier draft promoted this
> material to "Verified"; that was an over-claim (critic S2) and is retracted here.

**(i) Pole-freeness is automatic and logically unrelated to non-degeneracy.** $V_4$ is a
**contact term**: by definition it carries no internal $1/L_0^+$ propagator (the
propagator channels are the *separate* Feynman region traded away by the HS step,
R1/R2). So "pole-free $V_4$" is not a theorem — it is built in — and it is therefore
**not** an analogue of R3, where a genuine kinetic operator
$Q_B/(1-e^{-2\lambda L_0})$ with a *potential* pole at $L_0=0$ is *shown* to be regular.
More importantly, pole-freeness and non-degeneracy are **unrelated** properties:
pole-freeness is absence of poles, non-degeneracy is absence of a zero eigenvalue. A
pole-free (entire) operator-valued function can vanish identically or on an arbitrarily
large set. The inference "contact term $\Rightarrow$ pole-free $\Rightarrow\det V_4$ not
identically zero" is a **non-sequitur** and is withdrawn.

**(ii) "Generic / measure-zero / removable" has no meaning for the fixed CFT vertex.**
The physical $V_4$ is a **single fixed operator** with fixed CFT amplitudes on
$\operatorname{Sym}^2(\ker L_0^-\cap\ker b_0^-)$. It either possesses a symmetric
level-matched null vector or it does not — there is no parameter ensemble over which
"generic" or "measure-zero" could be asserted. The toy's $\det V_4\neq0$ holds only
because the toy amplitudes are *free generic parameters*; the Verification note itself
records that small/structured toys are *structurally rank-deficient*, so even in toys
non-degeneracy is not automatic. Reading a generic-finite-dimensional fact as the
infinite-dimensional result is exactly the over-reach being retracted.

**(iii) The YM $\Box$-at-$p^2=0$ analogy is motivational only and does not transfer.**
In YM (FBSP8UQ9 §8.3, R4) the auxiliary kinetic operator $\Box$ *does* have a kernel
(the massless shell) yet integrates out benignly via a Green's function, because the
degeneration is a measure-zero shell in a **continuous momentum spectrum** diagonalizing
$\Box$. The SFT condition (5.1) is structurally different: it is an
**operator-kernel** question on $\operatorname{Sym}^2\mathcal H$, not a "$\det$ vanishes
at special momenta $p^2=0$" question, and there is no single invariant $q$ that
diagonalizes the contact vertex on the two-string space. A **normalizable** symmetric
null vector of $V_4$ would be an honest **flat direction** of the action — not a
removable shell. The analogy therefore motivates the *expectation* of non-degeneracy but
provides **no** argument for it.

**Net.** Step 3 is plausibility narrative, not proof. The genuine open question is
exactly (5.1), settled by neither pole-freeness nor genericity nor the YM analogy.

### Step 4 — the spectral condition and what a counterexample would look like

By (2.3) (with symmetric outputs, C2), the **spectral condition that decides
auxiliarity** is:
$$
\boxed{\
m_2\ \text{injective on}\ \operatorname{Sym}^2\mathcal H\ (\ker=0)
\iff
V_4|_{\operatorname{Sym}^2\mathcal H}\ \text{has no null vector}
\iff
\ell_3\ \text{has no symmetric null vector}\ \Xi:\ \ell_3(\,\cdot\,,\Xi)=0.
\ }\tag{4.1}
$$
The last equivalence: $V_4(Y,\Xi)=\langle y_1|c_0^-|\ell_3(y_2,\xi_1,\xi_2)\rangle$ for
all $Y$, and $\omega_1=(\,\cdot\,|c_0^-|\,\cdot\,)_{\rm bpz}$ non-degenerate, so
$V_4(\,\cdot\,,\Xi)=0\iff\ell_3(z,\xi_1,\xi_2)=0$ for all $z\in\mathcal H$, i.e. $\Xi$
is a symmetric null vector of the bracket $\ell_3$. (As in C1, this is the **injectivity**
question; the integrate-out step additionally needs a bounded $V_4^{-1}$.)

**A genuine counterexample to auxiliarity** would be a level-matched, symmetric
$\Xi=\sum\xi_{rs}\,\phi_r\odot\phi_s\in\operatorname{Sym}^2(\ker L_0^-\cap\ker b_0^-)$,
$\Xi\neq0$, with
$$
\ell_3(z,\xi_1,\xi_2)=0\quad\text{for all }z\in\mathcal H
\quad(\text{equivalently}\ V_4(\,\cdot\,,\Xi)=0).\tag{4.2}
$$
For such a $\Xi$, $\Sigma=\Psi^{\otimes2}+\Xi$ would **also** solve the $\Sigma$-EOM
(S.3): $\Sigma$ would carry a flat direction $\Xi$ and fail to be purely auxiliary.
(Toy T3 builds exactly this: tuning one vertex amplitude to make
$\det V_4|_{\operatorname{Sym}^2}=0$ produces a symmetric null vector $\Xi$ for which
$\Sigma=\Psi^{\otimes2}+\Xi$ solves the EOM — the equivalence (2.3) is **sharp**.)

So a counterexample to auxiliarity is **exactly** a symmetric, level-matched null vector
of $\ell_3$. Whether one exists for the genuine CFT vertex is the open condition (5.1);
the Step 3 heuristic (pole-freeness, the YM/R3 analogies) only motivates expecting none
and is **not** evidence — in particular a normalizable such $\Xi$ would be an honest flat
direction, not a removable / measure-zero artefact.

### Step 5 — what remains CFT-level open

The toy establishes the algebraic facts (1.2), (2.3), (4.1) and the sharpness of the
equivalence. It does **not** compute the worldsheet $c_0^-$, $\ell_3$, $V_4$ on the
genuine infinite-dimensional level-matched $\mathcal H$. The **genuinely open** part is
the CFT-level non-degeneracy:
$$
\text{(OPEN)}\quad
V_4|_{\operatorname{Sym}^2(\ker L_0^-\cap\ker b_0^-)}\ \text{has no null vector},
\tag{5.1}
$$
i.e. $\ell_3$ has no symmetric level-matched null vector. The YM ($\Box$ away from
$p^2=0$) and open-stub ($L_0\to0$ regularity, R3) statements are *proven in their own
settings*, but as stressed in Step 3 they are **only motivational** here: neither
transfers to (5.1), which is a genuine operator-kernel question on
$\operatorname{Sym}^2\mathcal H$, not a removable-shell or no-pole question. (5.1) must
be checked directly for the closed quartic contact vertex and is flagged **open**
(numerical-verifier / CFT computation, mirroring how R7/R8 scoped their CFT-level gaps).

---

## Suspended ↔ physical translation

Intermediate algebra (e.g. the BV/odd-symplectic presentation (B) of R7) may use the
one-unit degree shift $s:\mathcal H\to\mathcal H[1]$, under which
$\omega_2^{\rm symp}=G_2\circ(s\otimes s)$ is graded-**antisymmetric** and $m_2$ is a
genuine $\IBL$ product. The shift is parity-relevant only by one unit per slot; the
**entries** of $G_2$, $V_4$, $m_2$ are identical in (A) and (B) (R7), and the kernel of
$m_2$ is presentation-independent (it is $\ker V_4$, a property of the matrix entries).
**What is presentation-invariant is the *subspace* (M4).** The invariant object is the
flat-direction subspace $\wedge^2\mathcal H=\ker V_4$ (equivalently $\ker m_2$), *not*
the words "symmetric"/"antisymmetric": under the one-unit shift $s$ the Koszul sign flips
and the **label** "$\operatorname{Sym}^2$" in (A) becomes the graded-**antisymmetric**
square in (B). The *same* subspace is the inert one in both; a reader using presentation
(B) must select the subspace, not the label, to avoid truncating the wrong square. We work
throughout in **physical** parity, where the inert square is the plain-antisymmetric one
and $\operatorname{Sym}^2$ is the physical bosonic sector. Hence all final objects are
stated in the **physical** parametrization:

- $\Psi$ at $N_{\rm gh}=2$, $\Sigma$ at $N_{\rm gh}=4$, $N_{\rm gh}(m_2)=-2$;
- $\operatorname{Sym}^2\mathcal H$ is the **graded-symmetric** square in physical parity
  $\epsilon=N_{\rm gh}\bmod2$ (the $N_{\rm gh}=4$ states are $\epsilon=0$, so graded-sym
  $=$ plain-sym on this sector — no shift ambiguity);
- the kernel condition (4.1)–(4.2) and the Lemma below are physical.

(Toy T1d/T2/T3 verify the symmetric-square statements directly in physical parity, so
no suspended grading enters the final checks.)

---

## Result

### Lemma (candidate R9) — auxiliarity of $\Sigma$ reduces to non-degeneracy of $V_4$ on $\operatorname{Sym}^2\mathcal H$

> **Hypotheses.** (H1) $\omega_1=(\cdot,c_0^-\cdot)_{\rm bpz}$ is non-degenerate on the
> level-matched space $\ker L_0^-\cap\ker b_0^-$ (standard; R7), so $\Delta=\omega_1^{-1}$
> and $G_2=\omega_1^{\otimes2}$ are non-degenerate. (H2) $V_4$ is the fully
> graded-symmetric closed cyclic quartic vertex with
> $V_4(X,Y)=G_2(X,m_2Y)$, $m_2=\Delta\circ\ell_3$ (note `eq:mtwo`). (H3) $\Sigma$ and
> $\Psi^{\otimes2}$ are level-matched and lie in the bosonic sector
> $\operatorname{Sym}^2\mathcal H$, $N_{\rm gh}=4$.
>
> **Claim (conditional reduction).** On the **off-shell** level-matched
> $\operatorname{Sym}^2\mathcal H$, with $m_2$ having symmetric outputs
> $m_2(\operatorname{Sym}^2)\subseteq\operatorname{Sym}^2$ (a consequence of full graded
> symmetry of $V_4$):
> $$
> \ker m_2=\ker V_4,\qquad
> \ker\big(m_2|_{\operatorname{Sym}^2}\big)=0
> \iff V_4|_{\operatorname{Sym}^2}\ \text{has no null vector}
> \iff \ell_3\ \text{has no symmetric null vector}.
> $$
> When this **injectivity** holds, the $\Sigma$-EOM $m_2(\Sigma)=m_2(\Psi^{\otimes2})$
> (note `eq:Sigeom`) has the **unique** solution $\Sigma=\Psi^{\otimes2}$, so $\Sigma$
> is **purely auxiliary** (no independent propagating degree of freedom). On the full
> $\mathcal H^{\otimes2}$, $\ker m_2\supseteq\wedge^2\mathcal H$ always, so the
> equivalence is meaningful **only** on $\operatorname{Sym}^2$; the $\wedge^2$ flat
> direction is physically inert by **decoupling** (it appears in neither the $\Sigma$
> kinetic nor the source term — Step 2/C3), not by a parity declaration. *Injectivity vs.
> invertibility (C1):* auxiliarity needs only $\ker=0$; actually integrating $\Sigma$ out
> (S6) needs in addition a bounded inverse $V_4^{-1}$ (closed range), a strictly stronger
> infinite-dimensional condition.
>
> **Status of the hypothesis (5.1) — OPEN (heuristic only below).** Pole-freeness of
> $V_4$ is **automatic** (it is a contact term) and bears **no** logical relation to
> non-degeneracy; "generic / measure-zero / removable" has **no** meaning for the single
> fixed CFT vertex, which either has a symmetric level-matched null vector or does not;
> and the YM $\Box$-at-$p^2=0$ and open-stub $L_0\to0$ analogies are **motivational
> only** and do not transfer (a normalizable null vector of $V_4$ would be an honest flat
> direction, not a removable shell). See Step 3. The **CFT-level** non-degeneracy (5.1) —
> that the closed quartic vertex has no symmetric level-matched null vector — is **not
> proven here** and is flagged **OPEN**.

### Promotability

**Promotable as R9 with the explicit hypotheses above**, in the same scoping style as
R7/R8. The **Verified algebraic core** (conditional reduction, toy-level, 10/10 PASS) is
exactly:
- (i) $\ker m_2=\ker V_4$ via non-degenerate $G_2$ (1.2);
- (ii) the $\operatorname{Sym}^2$ refinement: $\wedge^2\subseteq\ker m_2$, the equivalence
  $\ker(m_2|_{\operatorname{Sym}^2})=0\iff V_4|_{\operatorname{Sym}^2}$ non-degenerate
  (2.3), with **symmetric outputs** $m_2(\operatorname{Sym}^2)\subseteq\operatorname{Sym}^2$
  (C2) and **decoupling** of $\wedge^2$ (C3);
- (iii) the $\ell_3$-null-vector equivalence (4.1) and the sharp counterexample
  characterisation (4.2).

The contact-term/no-pole/measure-zero/generic material is **explicitly excluded** from the
Verified core (it is heuristic only, Step 3; see critic S2). **Two CFT-level inputs remain
OPEN:** (5.1) non-degeneracy / absence of a symmetric level-matched null vector of $V_4$ on
the infinite-dimensional $\operatorname{Sym}^2(\ker L_0^-\cap\ker b_0^-)$, **and** the
hypothesis **H2** that the closed cyclic quartic vertex $V_4$ is fully graded-symmetric at
the CFT level (itself flagged open in R7/R8, and the input behind both the $\wedge^2$
decoupling and the symmetric outputs). R9 should be entered as status **Verified (algebraic
core; conditional reduction; toy)** with **both** open residuals — H2 ($V_4$ symmetry) and
(5.1) ($V_4$ non-degeneracy on $\operatorname{Sym}^2$) — explicitly listed, exactly parallel
to R7/R8.

### Established vs. open

**Established (toy-verified algebraic core).**
- $m_2=G_2^{-1}V_4$, $G_2$ non-degenerate $\Rightarrow\ker m_2=\ker V_4$ (T1a–c).
- Full-space kernel contains the unphysical $\wedge^2\mathcal H$ (T1d); $m_2$ has
  symmetric outputs $m_2(\operatorname{Sym}^2)\subseteq\operatorname{Sym}^2$ (T1e), so on
  $\operatorname{Sym}^2\mathcal H$ the **implication** holds: *whenever*
  $V_4|_{\operatorname{Sym}^2}$ is non-degenerate, $m_2$ is **injective** and
  $\Sigma=\Psi^{\otimes2}$ is the unique solution (T2a, T2b). The toy verifies this
  implication, **not** the premise — whether the genuine CFT vertex satisfies
  non-degeneracy is exactly (5.1), open (no "generic"/measure-zero reading is claimed here;
  cf. critic S2/F5).
- Sharpness: a symmetric null vector of $V_4$ (=null vector of $\ell_3$) is a genuine
  flat direction $\Sigma=\Psi^{\otimes2}+\Xi$ of the EOM (T3).

**Heuristic only (NOT certified, NOT part of the Verified core; Step 3 / critic S2).**
- The toy "no-pole" model $\det V_4(q)$ being a nonzero polynomial with a finite zero set
  (T4a, T4b) **illustrates** the contact-term picture but does **not** certify the vertex:
  pole-freeness is automatic and unrelated to non-degeneracy, and "generic / measure-zero"
  has no meaning for the single fixed CFT vertex (5.1). T4a/T4b are retained only as
  illustrations of the heuristic, never as evidence for (5.1).

**Open (not settled here).**
- CFT-level non-degeneracy (5.1): $V_4$ (equivalently $\ell_3$) has no symmetric
  level-matched null vector on $\operatorname{Sym}^2(\ker L_0^-\cap\ker b_0^-)$. The
  toy reduces the auxiliarity question to this spectral condition; it does not certify
  the infinite-dimensional statement. → numerical-verifier / CFT.
- The conditional reduction is also predicated on **H2** — full graded symmetry of the
  closed cyclic quartic vertex $V_4$ at the CFT level (the input that gives both the
  $\wedge^2$ decoupling and the symmetric outputs $m_2(\operatorname{Sym}^2)\subseteq
  \operatorname{Sym}^2$). This same CFT-level $V_4$ symmetry is itself **flagged open**
  in R7/R8; the present Lemma assumes it and does not establish it. So the auxiliarity
  reduction rests on **two** CFT-level inputs — H2 ($V_4$ symmetry) and (5.1) ($V_4$
  non-degeneracy on $\operatorname{Sym}^2$) — both open. → numerical-verifier / CFT.

### Proposed next step

**S6** (homotopy-transfer integrate-out toy): check that integrating out $\Sigma$ by
its EOM on $\operatorname{Sym}^2\mathcal H$ returns the $\ell_3$ quartic — a direct
dynamical check that complements the kernel statement here. Then **I4** (cite
arXiv:1905.06785 eq. (5.55)) and Phase 6 (Riemann-surface interpretation of the
no-pole/contact-term property).

---

## Verification

Script: `codes/verify-i3-m2-invertibility.py` (sympy 1.14.0, **10 checks, all PASS**).
Toy: level-matched proxy with three $N_{\rm gh}=2$ and three $N_{\rm gh}=3$ single-string
states (the enlarged single-particle space is needed so the fully graded-symmetric
quartic is generically non-degenerate on the symmetric square — a 2-state space is
structurally rank-deficient, an artefact of too few states). $\omega_1$ pairs
$N_{\rm gh}=2\leftrightarrow3$; $G_2=\omega_1^{\otimes2}$; saturation tuned so the
$\Sigma$-kinetic pairing $V_4(\Sigma,\Sigma)$ ($N_{\rm gh}=4\otimes4$) is the nonzero
block; $\Sigma$ sector $=$ $N_{\rm gh}=4$ even sub-block, $\operatorname{Sym}^2$ and
$\wedge^2$ split explicitly. Each check is an internal algebraic self-check, **not** an
independent re-derivation of the CFT result.

| ID | Check | Method | Outcome | Scope |
| --- | --- | --- | --- | --- |
| T1a | $G_2=\omega_1^{\otimes2}$ non-degenerate; $(S_{\rm out},S_{\rm in})$ block invertible | $\det G_2$, $\det G_2|_{\rm block}$ | PASS | R7; defines $m_2$ without inverting $m_2$ |
| T1b | $m_2=G_2^{-1}V_4$ (eq:mtwo): $G_2 m_2=V_4$ | matrix identity | PASS | one index raised by $\Delta$ |
| T1c | $\ker m_2=\ker V_4$: $\operatorname{rank}m_2=\operatorname{rank}V_4$ | rank on generic amplitudes | PASS | **the equivalence**; $\ker m_2=0\iff V_4$ non-deg |
| T1d | full-space $\ker m_2\supseteq\wedge^2\mathcal H$: $m_2|_{\wedge^2}=0$ | apply $m_2$ to antisym basis | PASS | unphysical kernel; removed by $\operatorname{Sym}^2$ |
| T1e | **symmetric outputs** $m_2(\operatorname{Sym}^2)\subseteq\operatorname{Sym}^2$ (C2): antisym part of $m_2(\operatorname{Sym}^2)$ is $0$ | project $m_2P_{\rm sym}$ onto $\wedge^2$ | PASS | makes (2.3) hold; from full $V_4$ symmetry |
| T2a | generic $V_4$ non-degenerate on $\operatorname{Sym}^2$ $\Rightarrow m_2$ injective | $\det V_4|_{\operatorname{Sym}^2}\neq0$ | PASS | physical bosonic sector |
| T2b | $m_2$ injective on $\operatorname{Sym}^2\Rightarrow\Sigma=\Psi^{\otimes2}$ unique | $\ker=\{0\}$ | PASS | $\Xi=0$; purely auxiliary |
| T3 | sharpness: degenerate $V_4|_{\operatorname{Sym}^2}\Rightarrow$ flat direction $\Xi$, $\Sigma=\Psi^{\otimes2}+\Xi$ solves EOM | tune $\det=0$, exhibit null vector, check residual | PASS | failable; counterexample structure |
| T4a | **(heuristic illustration only)** toy contact-term model $\det V_4(q)$ nonzero polynomial in $q$, no poles | symbolic det, `is_polynomial` | PASS | illustrates Step 3 narrative; **does NOT certify** (5.1) |
| T4b | **(heuristic illustration only)** toy zero set finite (#zeros $\le\deg$) | `solve` det$=0$ | PASS | illustrates Step 3; not evidence for the fixed CFT vertex |

**Scope note (no over-claim).** The **Verified algebraic core** the toy certifies is: the
equivalence $\ker m_2=\ker V_4$ (T1a–c), the $\operatorname{Sym}^2$ refinement with
$\wedge^2\subseteq\ker m_2$ and symmetric outputs (T1d, T1e), generic non-degeneracy and
uniqueness on $\operatorname{Sym}^2$ (T2a, T2b), and the sharp counterexample
characterisation (T3) — all in physical parity. T4a/T4b are **heuristic illustrations of
Step 3 only**, not part of the certified core: pole-freeness is automatic and unrelated to
non-degeneracy, and genericity/measure-zero has no meaning for the single fixed CFT vertex.
The toy does **not** compute the worldsheet $c_0^-$, $\ell_3$, $V_4$ on the genuine
level-matched infinite-dimensional $\mathcal H$, nor certify (5.1). The
infinite-dimensional non-degeneracy of $V_4$ on
$\operatorname{Sym}^2(\ker L_0^-\cap\ker b_0^-)$ is the open residual, scoped exactly as
R7/R8 scoped their CFT-level gaps.
