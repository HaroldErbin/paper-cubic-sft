# 047 — Does $J(p,q)$ over $\mathrm{FD}\cap\mathcal V_{0,4}$ have a closed form?

## Status

**Consolidated 2026-09-23** (brief `computator-047-improve-20260923T153000`) after six runs (derivation and two fix passes 2026-09-22; external-review corrections, $p=0$/$q=0$ closed forms, fix pass on their node check 2026-09-23): every claim is stated once, in final form, in the claim tree, Block A, `## Result`, `### Scope of the exclusion` and `## Proposed ledger row`; the correction and fix-pass sections are the audit trail. Harness `codes/verify-j-closed-form.py`: **25/25 PASS**, exit 0, seed 20260922. Last completed step: consolidation, then the fix pass on its node check (2026-09-23, table at the end of the record; no verdict changed, no script run). Next: `## Next` items 1–4, and item 6 (weakest step, ellipse obstruction). `Open gaps:` C4.1 only.

## Task and objective

**Literal task.** Decide whether
$$J(p,q)=\int_{R}\lvert Z\rvert^{p}\lvert1-Z\rvert^{q}\,\dd^2Z,\qquad R=\mathrm{FD}\cap\mathcal V_{0,4},$$
admits a closed form (Appell $F_1/F_2$, finite combination of Gauss ${}_2F_1$, or a one-dimensional
integral of such functions), or a representation replacing two-dimensional quadrature by something
exact or rapidly convergent with a rigorous error bound. Sub-task 1: route list, falsifier harness,
route (a) (boundary reduction) to a verdict.

**Motivating objective.** Record 044 (R48) reduced the off-shell four-tachyon contact term to six
integrals $J(p,q)$, $(p,q)=\tfrac{\alpha'}4(x-y-z,\,y-x-z)$ over the ordered permutations of
$(s,t,u)$. Record 045 concluded that without a formula the comparator grid must be produced
before the pair kernel $K_P$ (PH1 (ii), PH3, PH18) can be studied.
A closed form, or a convergent series with closed-form terms, removes the grid; a stated obstruction
fixes the grid as the route and names the responsible feature of $R$.

## Conventions and assumptions

- **A1** $\dd^2Z=\dd x\,\dd y$, $Z=x+\I y$ (as in `j_integral` of `codes/verify-kp-box.py`).
- **A2** $\beta\ge\beta_{04}$ ($\beta_{04}=$ (companion value, not reproduced here)), the range on which the four-arc description below holds ($a\ge\tfrac32$, the ellipse meeting the real axis left of $-1$; `## Corrections 2026-09-23`, item 8); the tests use $\beta\in\{\tfrac32,2\}$; $a=\beta^2+\tfrac1{16\beta^2}$, $b=\beta^2-\tfrac1{16\beta^2}$,
  $a^2-b^2=\tfrac14$ (record 045 ll. 196–245; the ellipse is the $\lvert q\rvert=1$ boundary of ledger row **R2**, $\partial\mathcal V_{0,4}=\{Z_4^{(s)}(\e^{\I\theta})\}$ with $Z_4^{(s)}(q)=\cosh^2\!\bigl(\ln\tfrac{2\beta}{\sqrt q}\bigr)$, whose semi-axes are $\tfrac12\cosh(2\ln2\beta)=a$ and $\tfrac12\sinh(2\ln2\beta)=b$ — 045 A2 cites this as R7, which is a different row). $R$ is the closed region
  $\{\operatorname{Im}Z\ge0,\ \lvert Z\rvert\ge1,\ \operatorname{Re}Z\le\tfrac12\}\cap
  \{(x-\tfrac12)^2/a^2+y^2/b^2\le1\}$, with the four boundary arcs of 045: unit circle from
  $\e^{\I\pi/3}$ to $-1$, real segment $[\tfrac12-a,-1]$, ellipse quarter from $\tfrac12-a$ to
  $\tfrac12+\I b$, vertical segment $\operatorname{Re}Z=\tfrac12$ from $\tfrac12+\I b$ to $\e^{\I\pi/3}$.
- **A3** Branches. On the closed upper half-plane minus $\{0,1\}$,
  $Z^{p/2}:=\lvert Z\rvert^{p/2}\e^{\I p\theta_0/2}$ with $\theta_0=\arg Z\in[0,\pi]$, and
  $(1-Z)^{q/2}:=\lvert1-Z\rvert^{q/2}\e^{\I q\theta_1/2}$ with $\theta_1=\arg(1-Z)\in[-\pi,0]$.
  Both are the principal branches (cuts $(-\infty,0]$ and $[1,\infty)$), the first taken as its
  boundary value from above on the negative axis; both are continuous on the closed half-plane and
  holomorphic in its interior. $R$ lies in the closed upper half-plane and avoids $0,1$.
- **A4** $p,q\in\mathbb R$ with $p\notin\{-2,-4,\dots\}$ (poles of the antiderivative normalisation
  used in Block A; the identity extends by continuity, see Commentary).
- Reused: R48 (reduction to $J$), record 045 C1 (compactness, $1\le\lvert Z\rvert\le a$,
  $1\le\lvert1-Z\rvert\le a+\tfrac12$, so $J$ is entire in $(p,q)$) and (3.4) (area).
- No `knowledge/conventions.md` exists in this project; A1–A3 are local conventions.

## Candidate routes (ranked by cost-to-information)

| # | Route | What success gives | What failure looks like |
|---|---|---|---|
| (a) | **Boundary reduction** (Green/Stokes): $\int_R f\bar f\,\dd^2Z=\tfrac1{2\I}\oint_{\partial R}f\,\overline G\,\dd Z$, $G'=f=Z^{p/2}(1-Z)^{q/2}$, $G$ an incomplete Beta (${}_2F_1$). Cheapest; localises which arc obstructs. | Per-arc closed forms; at worst a 1D integral of ${}_2F_1$ over four arcs (category 3 of the brief). | Arcs on which $\int f\overline G\,\dd Z$ has no closed form – expected for the circle and the ellipse quarter, because $G$ has no constant phase or reflection symmetry there; then the verdict is "1D integral of ${}_2F_1$, no further closure by this route". |
| (c′) | **Bipolar / elliptic coordinates** $(r,\rho)=(\lvert Z\rvert,\lvert1-Z\rvert)$. Observation made at the skeleton stage: $a^2-b^2=\tfrac14$ means the ellipse is *confocal with foci at $0$ and $1$*: $\partial\mathcal V_{0,4}=\{r+\rho=2a\}$. In $u=r+\rho$, $v=\rho-r$ the region is the trapezoid $\{0\le v\le1,\ 2+v\le u\le2a\}$ and $J=2^{-p-q-2}\!\int\!\frac{(u-v)^{p+1}(u+v)^{q+1}\,\dd u\,\dd v}{\sqrt{(u^2-1)(1-v^2)}}$. Three of the four arcs are coordinate lines; only the unit circle ($u=2+v$) is not. | Expanding in $v/u\le\tfrac13$ (geometric, not marginal) gives a series whose terms are Beta × incomplete-Beta on the $u\ge3$ part and Appell $F_1$ at fixed arguments $(-1,-\tfrac12)$ on the $u\in[2,3]$ part. | A closed form would need the $u$-integral with $v$-dependent lower limit $2+v$; that piece is Lauricella-type. Failure = the $u\in[2,3]$ strip does not reduce below Appell $F_1$, or the series' Appell terms cost more than quadrature. |
| (b) | **Double series in $1/Z$** (brief). $\lvert1-Z\rvert^q=\lvert Z\rvert^q\lvert1-Z^{-1}\rvert^q$, expanded binomially. | Terms $\int_R\lvert Z\rvert^{p+q}Z^{-m}\bar Z^{-n}$, elementary or ${}_2F_1$ per piece. | Marginal convergence on the unit-circle arc ($\lvert Z^{-1}\rvert=1$): algebraic tail, no useful error bound at large $\lvert q\rvert$. Superseded by (c′), whose expansion parameter is $\le\tfrac13$ on $R$. |
| (c) | **Region decomposition** quarter-ellipse minus half-disc piece, polar/elliptic coordinates. | Disc piece by polar coordinates around $0$ (partial angular integrals of $(1-2r\cos\theta+r^2)^{q/2}$ = Appell $F_1$); ellipse piece by (c′). | The line $\operatorname{Re}Z=\tfrac12$ is not a polar coordinate line about $0$: the disc piece splits again; result is a sum of Appell/Lauricella pieces, not a closed form. |
| (d) | **Literature**: restricted Virasoro–Shapiro integrals over fundamental-domain-type regions (off-shell / stubbed closed-string amplitudes). | A known reduction. | No reference found (none searched in sub-task 1; the region's confocal-ellipse structure is specific to the SL(2,C) vertex and unlikely to be tabulated). |

Applicable checks for any representation: $J(0,0)=\operatorname{Vol}(R)$ of 045 (3.4); agreement with
`j_integral` at seeded random $(p,q)$ including $\lvert p\rvert+\lvert q\rvert>100$, at
$\beta=\tfrac32,2$; break leg ($\times(1+10^{-3})$ must FAIL).

## Claim tree

- **A1–A4** as above.
- **C1** $J(p,q)=\tfrac1{2\I}\oint_{\partial R}f\,\overline{G}\,\dd Z=\tfrac12\operatorname{Im}\oint_{\partial R}\overline{G}\,\dd G$ – $J$ is the area of $G(R)$ counted with multiplicity – for $G$ any antiderivative of $f=Z^{p/2}(1-Z)^{q/2}$ on the upper half-plane. [by C1.1–C1.3; eq. (A.2)] [check: C3-hyp, C3-cheb, C3-area]
  - **C1.1** With A3, $f$ is holomorphic on the open upper half-plane, continuous on $R$, and $\lvert f\rvert^2=\lvert Z\rvert^p\lvert1-Z\rvert^q$. [by A3; block A]
  - **C1.2** Stokes on the compact simply connected $R$ with piecewise-smooth boundary gives (A.2); the exact part $\tfrac12\dd\lvert G\rvert^2$ integrates to zero, so the per-arc swept areas $J_k$ sum to $J$. [by A2, C1.1, C1.3 (existence of $G$), and the positive orientation of $\partial R$ fixed in the Setup of Block A; eq. (A.1)–(A.2)] [check: C1-closure]
  - **C1.3** $G(Z)=B_Z(\tfrac p2+1,\tfrac q2+1)-B_{-1}(\tfrac p2+1,\tfrac q2+1)$ with the principal-branch ${}_2F_1$ form (A.3) is an antiderivative of $f$ with the branches A3, equal to $\int_{-1}^Zf$ along any path in the closed half-plane. [by A3, A4; eq. (A.3)–(A.4)] [check: C1.3-derivative, C1.3-path]
- **C2** Per-arc reduction of (A.2). [by C2.1–C2.4; block A]
  - **C2.1** The real segment contributes $J_{\text{real}}=0$: $\arg(f\,\dd Z)=\tfrac{\pi p}2$ is constant there ($\dd Z=\dd x$), so its image under $G$ is the radial line $-\e^{\I\pi p/2}\Phi$ through $G(-1)=0$. [by A3, C1.3; eq. (A.5)] [check: C2-real]
  - **C2.2** The vertical segment contributes $\tfrac12\operatorname{Re}G(\e^{\I\pi/3})\,\Psi(b)$, $\Psi$ a real ${}_2F_1$, iff $p=q$ ($\arg(f\,\dd Z)=\tfrac{(p-q)\theta_0}2+\tfrac\pi2$ constant iff $p=q$); for $p\ne q$ the image is curved and the same formula fails. [by A3, C1.3; eq. (A.6)] [check: C2-vert, C2-vert-neq]
  - **C2.3** *(Verdict of route (a) at generic $(p,q)$.)* (i) *Constant phase.* The image of an arc under $G$ is straight iff $\arg(f\,\dd Z)$ is constant on it, (C.1)–(C.2): on the unit circle iff $2p+q=-4$, where the line passes through $G(-1)=0$ and $J_{\text{circle}}=0$ exactly; on the ellipse quarter iff $p=q=-1$, where $J_{\text{ellipse}}$ is the triangle (C.3); off these loci (including $(0,0)$) the mechanism closes neither curved arc. (ii) *Reflection.* Schwarz reflection applies on the three curved arcs (and on the real segment with $G(S(Z))$ read as the boundary value from *below* the cut): each carries an algebraic Schwarz function $S$, $\bar Z=S(Z)$ on the arc — $1/Z$ (circle), $1-Z$ (vertical), $\tfrac12+4(a^2+b^2)(Z-\tfrac12)\pm8ab\sqrt{Z(Z-1)}$ (confocal ellipse, sheet fixed by the arc), (A.7) — so $\overline{G(Z)}=G(S(Z))+\text{const}$, (A.8), and every arc contribution is a contour integral of a holomorphic integrand. (iii) *The obstruction.* At generic $(p,q)$ that integrand is (two powers)$\times{}_2F_1$ with exponents unmatched to the hypergeometric parameters, (A.9); its antiderivative (A.11) is a Kampé de Fériet double series in one variable, single-series when Euler's transformation absorbs one power ($\mu=a+b-c$, (C.4) — sufficient, not necessary; met on $p=0$ and $q=-2$, one per Pfaff representative (C.5)(B), (A), and on $q=-1$ directly) or when the ${}_2F_1$ degenerates ($p+q=-4$, $G$ elementary). These lines close the circle arc only. Hence $J_{\text{circle}}$, $J_{\text{ellipse}}$ remain one-dimensional integrals $\tfrac12\int\operatorname{Im}\bigl(\overline G\,G'(Z)\,Z'(t)\bigr)\dd t$ of a ${}_2F_1$: **category 3 of the brief, not a closed form, for generic $(p,q)$** — "generic" meaning off the lines $p=0$, $q=0$ (C2.4) and the point $(-1,-1)$ (${}_2F_1$ endpoint values and one ${}_3F_2$, (C.6)). Scope: no closed form *found* by the boundary route, not a proof of non-existence. [by A3; block A, C2 paragraphs; the corrected constant-phase and Euler clauses are derived in `## Corrections 2026-09-23` items 1–3, 5] [check: C2.3-reflect, C7-item1-circle-line, C7-item2-ellipse-point, C7-item3-euler, C7-item5-first-form]
  - **C2.4** On $p=0$ and on $q=0$ route (a) closes, with all coefficients and branches: $J(0,q)$ is (L.6) — incomplete Beta on the circle and on the vertical segment, two Appell $F_1(a;\cdot,\cdot;a+1;cw,w/c)$ on the ellipse through the uniformiser $Z=(cw+1)^2/4cw$, $c=4\beta^2$, i.e. $Z_4^{(s)}(1/w)$ of R2 — and $J(p,0)$ is (L.12) — the circle arc *elementary* ($-\tfrac{2\pi}3$, (L.8)), incomplete Beta on the vertical segment, two Appell $F_1$ on the ellipse with first argument $c-\I0$ at $w=-1$ (the cut of $Z^{p/2}$, which $\partial R$ touches). The two lines are not related by a symmetry of $R$. They are the codimension-one lines $x=y+z$, $y=x+z$ of R48's ordered Mandelstam triple, so they do not answer the objective, but they are inside the class the exclusion covers and are exact anchors for the series route (c′). [by A2–A4, C1.3, C2.3 (Schwarz functions); eqs. (L.1)–(L.12); first derived by the critic of iteration 2 (`agent/reports/critic-047-iter2-20260922T184000.md`, node 3)] [check: C6-closed-lines, C6-appell-series, C6-area-limit, C6-no-symmetry]
- **C3** The representation (A.2) reproduces the area (045 (3.4)) at $p=q=0$ and agrees with the 2D quadrature `j_integral` at 12 seeded random $(p,q)$ (4 with $\lvert p\rvert+\lvert q\rvert>100$), $\beta\in\{\tfrac32,2\}$, to $2\times10^{-9}$ (the accuracy of the reference at $n=640$); its two evaluations (${}_2F_1$ and Chebyshev, hypergeometric-free) agree to $\lesssim10^{-10}$ (worst of the 12 points; $10^{-15}$ at moderate exponents); the $\times(1+10^{-3})$ break leg fails. [by check: C3-area, C3-hyp, C3-cheb, C3-mutual, C3-break]
  - **C3.1** `j_integral` converges algebraically, error $\propto n^{-3}$ towards the boundary value, because its inner limits $\mp\sqrt{1-y^2}$ give the outer integrand a **square-root branch point at the panel endpoint** $y=1$ (both inner segments lose length $\sqrt{2(1-y)}$ there, and $y=b\sin t$ has nonzero slope, so the branch point survives in $t$); Gauss–Legendre on an endpoint singularity $x^{s}$ converges as $n^{-2(s+1)}$, i.e. $n^{-3}$ at $s=\tfrac12$. At its default $n=40$ it carries $\sim10^{-6}$ relative error for moderate negative exponents. [by check: C3-ref-conv]
- **C4** Bipolar representation (B.4): $R$ is the trapezoid $\{0\le v\le1,\ 2+v\le u\le2a\}$ in $u=\lvert Z\rvert+\lvert1-Z\rvert$, $v=\lvert1-Z\rvert-\lvert Z\rvert$, because $\partial\mathcal V_{0,4}$ is the confocal ellipse with foci $0,1$ ($a^2-b^2=\tfrac14$); the Jacobian is (B.2). [by A2; eq. (B.1)–(B.4)] [check: C4-uv, C4-uv-VS]
  - **C4.1** The expansion (B.5) in $w=v/u$ converges geometrically at ratio $\le\tfrac13$ on $R$; the only obstruction to term-wise closed forms is the slanted side $u=2+v$ (unit circle). Its tail bound and the term integrals over the triangle $\{2\le u\le3,\ 0\le v\le u-2\}$ are left to the continuation. [GAP]

Open gaps: C4.1 (continuation: series route (c′); does not affect C1–C3).
Hypotheses in force: none

## Block A — Route (a): boundary reduction

\subsection*{Setup}

Assumptions A1–A4. Write $f(Z)=Z^{p/2}(1-Z)^{q/2}$ with the branches A3, $\alpha=\tfrac p2+1$,
$\gamma=\tfrac q2+1$, and $G$ for an antiderivative of $f$ on the open upper half-plane $\mathbb H$.
$\partial R$ is positively oriented (interior on the left): circle from $-1$ to $\e^{\I\pi/3}$
(clockwise on the circle, $\theta:\pi\to\pi/3$), vertical segment up to $\tfrac12+\I b$, ellipse
quarter $\theta:\tfrac\pi2\to\pi$ to $\tfrac12-a$, real segment rightwards to $-1$.

\subsection*{Derivation}

*C1.1.* By A3, $f$ is holomorphic on $\mathbb H$ and continuous on $\overline{\mathbb H}\setminus\{0,1\}\supset R$,
and $f\bar f=\lvert Z\rvert^p\lvert1-Z\rvert^q$ since the phases cancel.

*C1.2.* For $G$ holomorphic with $G'=f$, the 1-form $\omega=f\,\overline G\,\dd Z$ satisfies
$$\dd\omega=\partial_{\bar Z}\bigl(f\overline G\bigr)\,\dd\bar Z\wedge\dd Z
 =f\,\overline{G'}\,\dd\bar Z\wedge\dd Z=2\I\,\lvert f\rvert^2\,\dd x\wedge\dd y,\tag{A.1}$$
using $\dd\bar Z\wedge\dd Z=2\I\,\dd x\wedge\dd y$ and $\partial_{\bar Z}f=0$. Stokes on the compact
$R$ (piecewise smooth boundary, $\omega$ continuous up to the boundary) gives
$$\boxed{\ J(p,q)=\frac1{2\I}\oint_{\partial R}f\,\overline G\,\dd Z
 =\frac12\operatorname{Im}\oint_{\partial R}\overline G\,\dd G\ }\tag{A.2}$$
The second form: along $\partial R$, $\dd\lvert G\rvert^2=\overline G\,\dd G+G\,\overline{\dd G}$, so
$\overline G\,\dd G=\tfrac12\dd\lvert G\rvert^2+\I\operatorname{Im}(\overline G\,\dd G)$ and the exact
part integrates to zero around the closed curve. Hence $J$ is the (multiplicity-counted) area of
$G(R)$, and the per-arc contributions are the areas swept from the origin of the $G$-plane by the
image arcs: $J=\sum_kJ_k$, $J_k=\tfrac12\int_{t_0^{(k)}}^{t_1^{(k)}}\operatorname{Im}\bigl(\overline G\,G'(Z)\,Z'(t)\bigr)\dd t$
for any parametrisation $t\mapsto Z(t)$ of arc $k$ (the differential $\dd Z$ is complex on three of the
four arcs, so it is kept inside the imaginary part).
The additive constant of $G$ drops out by Cauchy ($\oint f\,\dd Z=0$); fix it by $G(-1)=0$.

*C1.3.* An antiderivative of $Z^{\alpha-1}(1-Z)^{\gamma-1}$ on $\mathbb C\setminus\bigl((-\infty,0]\cup[1,\infty)\bigr)$
with principal branches is the incomplete Beta function
$$B_Z(\alpha,\gamma)=\frac{Z^{\alpha}}{\alpha}\,{}_2F_1(\alpha,1-\gamma;\alpha+1;Z),\qquad
 \frac{\dd}{\dd Z}B_Z(\alpha,\gamma)=Z^{\alpha-1}(1-Z)^{\gamma-1},\tag{A.3}$$
valid for $\alpha\notin\{0,-1,-2,\dots\}$ (A4) as an identity of analytic functions (the ${}_2F_1$
continued to $\lvert Z\rvert\ge1$ has its cut on $[1,\infty)$, the same as $(1-Z)^{\gamma-1}$). On
$\overline{\mathbb H}$ the boundary values from above are taken on $(-\infty,0]$, matching A3. So
$$G(Z)=B_Z(\alpha,\gamma)-B_{-1}(\alpha,\gamma),\qquad G(-1)=0,\tag{A.4}$$
and $G(Z)=\int_{-1}^Zf$ along any path in $\overline{\mathbb H}$ avoiding $0,1$.

*C2, real segment.* For $Z=x\in[\tfrac12-a,-1]$: $\theta_0=\pi$, $\theta_1=0$, so
$f(x)=\e^{\I\pi p/2}\phi(x)$ with $\phi(x)=\lvert x\rvert^{p/2}(1-x)^{q/2}>0$, and
$G(x)=-\e^{\I\pi p/2}\Phi(x)$, $\Phi(x)=\int_x^{-1}\phi$. The image of the segment is the radial
line $\{-\e^{\I\pi p/2}\Phi\}$ through $G(-1)=0$: $\operatorname{Im}(\overline G\,G')=0$ pointwise and
$$J_{\text{real}}=0.\tag{A.5}$$
(With another base point $Z_0$ the segment contributes $\tfrac12\operatorname{Im}\bigl(\overline{G(-1)}\e^{\I\pi p/2}\bigr)\Phi(\tfrac12-a)$,
where $\Phi(\tfrac12-a)=\int_1^{a-1/2}t^{p/2}(1+t)^{q/2}\dd t$ is a real incomplete Beta – closed either way.)

*C2, vertical segment.* $Z=\tfrac12+\I y$, $y\in[\tfrac{\sqrt3}2,b]$, $1-Z=\bar Z$, so
$f=\lvert Z\rvert^{(p+q)/2}\e^{\I(p-q)\theta_0/2}$, $\theta_0=\arctan2y\in[\tfrac\pi3,\tfrac\pi2)$.
For $p=q$: $f=\lvert Z\rvert^p$ is real, $G(Z)=G_1+\I\Psi(y)$ with $G_1=G(\e^{\I\pi/3})$ and
$\Psi(y)=\int_{\sqrt3/2}^y(\tfrac14+y'^2)^{p/2}\dd y'$ real, and $\overline G\,\dd G=(\overline{G_1}-\I\Psi)\,\I\lvert Z\rvert^p\dd y$ gives
$$J_{\text{vert}}\big|_{p=q}=\tfrac12\operatorname{Re}(G_1)\,\Psi(b),\qquad
 \Psi(b)=\int_{\sqrt3/2}^{b}\bigl(\tfrac14+y^2\bigr)^{p/2}\dd y\ \ (\text{a }{}_2F_1).\tag{A.6}$$
For $p\ne q$ the phase $\e^{\I(p-q)\theta_0/2}$ varies along the segment, the image is curved, and
no reduction of $\int\operatorname{Im}(\overline G\,G'(Z)\,Z'(t))\dd t$ below a one-dimensional integral of
${}_2F_1$ was found.

*C2, unit circle.* $Z=\e^{\I\theta}$: $1-\e^{\I\theta}=2\sin\tfrac\theta2\,\e^{\I(\theta-\pi)/2}$,
$\theta_1=\tfrac{\theta-\pi}2\in[-\tfrac\pi3,0]$ (principal, consistent with A3), so
$f=(2\sin\tfrac\theta2)^{q/2}\e^{\I[p\theta/2+q(\theta-\pi)/4]}$, $\dd Z=\I\e^{\I\theta}\dd\theta$.
The phase of $f\,\dd Z$ is $\theta(\tfrac p2+\tfrac q4+1)+\text{const}$, (C.1): constant iff $2p+q=-4$, where the
image line passes through $G(-1)=0$ and $J_{\text{circle}}=0$ exactly; otherwise (including $(0,0)$) the
constant-phase mechanism fails. (An earlier version dropped the $\tfrac12$ of $(1-Z)^{q/2}$ in the phase
and tested $\arg f$ instead of $\arg(f\,\dd Z)$; corrected in `## Corrections 2026-09-23`, item 1.)

*C2.3, the reflection mechanism, and what actually obstructs closure.* Schwarz reflection is **not**
obstructed on the three curved arcs of $\partial R$; the obstruction lies one step further on. Each of
the four arcs carries an algebraic Schwarz function $S$, i.e. $\bar Z=S(Z)$ pointwise on the arc:
$$S(Z)=\frac1Z\ \text{(circle)},\quad S(Z)=1-Z\ \text{(vertical)},\quad S(Z)=Z\ \text{(real)},\quad
 S(Z)=\tfrac12+4(a^2+b^2)\bigl(Z-\tfrac12\bigr)+8ab\sqrt{Z(Z-1)}\ \text{(ellipse)},\tag{A.7}$$
the last two-valued, the sheet fixed by the arc (the sign written is the one selected by the
principal square root on the *open* quarter $\tfrac12-a\to\tfrac12+\I b$; at the endpoint
$\tfrac12+\I b$ the argument $Z(Z-1)=-a^2$ sits on the cut of the principal root and the value is to
be taken as the limit along the arc — a measure-zero point, never sampled by `C2.3-reflect`);
$a^2-b^2=\tfrac14$ is what puts the branch points of $S$ exactly at the foci $0,1$. For real
$p,q$ the incomplete Beta satisfies $\overline{B_{\bar w}(\alpha,\gamma)}=B_w(\alpha,\gamma)$ on the cut
plane, so on each of the three curved arcs
$$\overline{G(Z)}=G\bigl(S(Z)\bigr)+\text{const},\tag{A.8}$$
the right-hand side being *holomorphic* in $Z$ in a neighbourhood of the arc (on the two-sheeted
algebraic curve of $S$, in the ellipse case). Every arc contribution to (A.2) is therefore a contour
integral of a holomorphic integrand; (A.8) is checked on all three curved arcs by `C2.3-reflect`
(spread $6\times10^{-29}$). On the **real segment** $S(Z)=Z$ and (A.8) holds only with $G(S(Z))$ read
as the boundary value from *below* the cut, $B_x^{\text{below}}=\overline{B_x^{\text{above}}}$ — A3
fixes $G$ by its value from above, and the two differ there by the phase $\e^{-\I\pi p}$, not by a
constant. Nothing rests on that arc: it is closed exactly by (A.5). On the circle, substituting $w=S(Z)=1/Z$ in $f\,\overline G\,\dd Z$ and using
$Z^{p/2}Z^{-\alpha}=Z^{-1}$ turns the first term into
$$\frac1{2\I}\int_{\text{circle}}f\,\overline G\,\dd Z=-\frac1{2\I\alpha}\int_{-1}^{\e^{-\I\pi/3}}w^{-q/2-1}(w-1)^{q/2}
 \,{}_2F_1(\alpha,1-\gamma;\alpha+1;w)\,\dd w
 \ -\ \frac{\overline{B_{-1}}}{2\I}\bigl[G\bigr]_{-1}^{\e^{\I\pi/3}},\tag{A.9}$$
all branches principal, the second term a pure endpoint value. The left-hand side is the first-form
piece, equal to $J_{\text{circle}}-\tfrac\I4\lvert G(\e^{\I\pi/3})\rvert^2$ by (C.8); the swept area
$J_{\text{circle}}$ is its real part (`C7-item5-first-form`). (The sign of the first term is the
minus sign of the Jacobian $\dd Z=-\dd w/w^2$; it is opposite to the one quoted in the critic report
of iteration 1, whose displayed formula dropped that Jacobian. There is **no** branch discrepancy:
with $Z=\e^{\I\theta}$, $\theta\in(\tfrac\pi3,\pi)$, one has $\arg w=-\theta\in(-\pi,-\tfrac\pi3)$,
principal, and both $Z^{p/2}Z^{-\alpha}=Z^{-1}$ and $w^{-q/2}(w-1)^{q/2}=(1-Z)^{q/2}$ hold with all
branches principal — re-derived by the critic of iteration 2 and consistent with the numerical
agreement to $10^{-16}$ at $(p,q)=(-3.4,2.1)$, $(1.7,-5.3)$.) The
same mechanism on the vertical segment gives, by parts,
$J_{\text{vert}}=\tfrac1{2\I}\bigl([G\tilde G]-\int G\,\tilde f\,\dd Z+c\,[G]\bigr)$ with
$\tilde G(Z)=B_{1-Z}(\alpha,\gamma)$, $\tilde f=\tilde G'=-Z^{q/2}(1-Z)^{p/2}$ (the antiderivative with
$p\leftrightarrow q$ up to sign) and $c=\overline{G}-\tilde G$ the constant of (A.8).

**The obstruction is (A.9), not the reflection, and it is the pair of powers, not the endpoints.**
A single power against a ${}_2F_1$ integrates at *any* endpoint,
$$\int_0^zw^{\lambda}\,{}_2F_1(a,b;c;w)\,\dd w
 =\frac{z^{\lambda+1}}{\lambda+1}\,{}_3F_2(a,b,\lambda+1;c,\lambda+2;z),\tag{A.10}$$
term by term. What obstructs in (A.9) is the *second* power: with $(1-w)^{\mu}$ present,
$$\int_0^zw^{\lambda}(1-w)^{\mu}{}_2F_1(a,b;c;w)\,\dd w
 =\frac{z^{\lambda+1}}{\lambda+1}\sum_{m,n\ge0}\frac{(\lambda+1)_{m+n}}{(\lambda+2)_{m+n}}
 \frac{(-\mu)_m(a)_n(b)_n}{(c)_n\,m!\,n!}\,z^{m+n},\tag{A.11}$$
a Kampé de Fériet double series in the single variable $z$ (not Appell: the factor
$(a)_n(b)_n/(c)_n$ carries one index only); the prefactor is (C.9), and at $\mu=0$ (A.11) is (A.10)
(checked by the (A.11) leg of `C7-item8-beta04`; item 8 of `## Corrections 2026-09-23`). It collapses to a single hypergeometric series
when Euler's transformation absorbs the extra power, $\mu=a+b-c$ (C.4) — a sufficient condition, not a
necessary one (item 3; the two Pfaff representatives of the integrand are (C.5)). For (A.9), after Pfaff
($x=w/(w-1)$) the integrand is $x^{-\gamma}(1-x)^{-\gamma}{}_2F_1(1,1-\gamma;\alpha+1;x)$ (C.5)(B)
and the condition reads $-\gamma=1+(1-\gamma)-(\alpha+1)$, i.e. $\alpha=1$, i.e. $\boldsymbol{p=0}$; the other
representative (C.5)(A) absorbs at $\gamma=0$ ($q=-2$);
directly on (A.9), $\gamma=\tfrac12$ (i.e. $q=-1$) also absorbs $(w-1)^{\gamma-1}$ and leaves a
${}_3F_2$ at the generic endpoint, (C.6); and on $p+q=-4$ the ${}_2F_1$ itself is elementary. So the statement is about the **exponents**, not the endpoints:
for generic $(p,q)$ the arc integral is (two powers)$\times{}_2F_1$ with exponents unmatched to the
hypergeometric parameters, and has no antiderivative in the brief's classes. The same statement holds
on the ellipse quarter, with the extra feature that $S$ is two-valued there.

*The lines $p=0$ and $q=0$, where route (a) closes.* At $p=0$, $f=(1-Z)^{q/2}$ and
$G=-\gamma^{-1}(1-Z)^{\gamma}+\text{const}$ is elementary; at $q=0$, $f=Z^{p/2}$ and
$G=\alpha^{-1}Z^{\alpha}+\text{const}$. On each line the Schwarz functions (A.7) turn every arc
integrand into powers of linear factors: incomplete Betas on the circle ($p=0$; on $q=0$ the circle
integrand is $Z^{-1}\dd Z$, elementary) and on the vertical segment, and, in the uniformiser
$Z=(cw+1)^2/4cw$ of R2 ($c=4\beta^2$, $w=\e^{\I t}$), two Appell $F_1(a;\cdot,\cdot;a+1;\pm cw,\pm w/c)$
on the ellipse quarter. The closed forms with every coefficient, phase and branch are (L.6) for
$J(0,q)$ and (L.12) for $J(p,0)$ (`## The lines $p=0$ and $q=0$ with coefficients (2026-09-23)`;
verified against (A.2) at 16 points to $1.4\times10^{-15}$, `C6-closed-lines`). The $q=0$ ellipse
term needs the $c-\I0$ prescription on its first Appell argument because $\partial R$ touches the cut
of $Z^{p/2}$; the two lines are not related by any symmetry of $R$. These are the codimension-one
lines $x=y+z$, $y=x+z$ of R48's ordered Mandelstam triple, so they do not answer the objective, but
they lie *inside* the class the exclusion claims to cover and are exact anchors for the series route
(c′). (Node C2.4; first derived by the critic of iteration 2.)

*Positive by-product, as a lead only.* Because the circle integrand is holomorphic after (A.8), the
circle contour may be deformed off $\lvert Z\rvert=1$ into $\lvert Z\rvert>1$ (staying clear of
$Z=1$) — **except at its endpoints** $-1$ and $\e^{\I\pi/3}$, which are fixed and lie on
$\lvert Z\rvert=1$ ($-1$ additionally on the cut of $B_{1/Z}$). A $1/Z$ expansion on the deformed
contour is therefore still marginal at both ends; the deformation helps the interior only. Whether
this rescues route (b) for this piece is **not examined here**.

*C2, ellipse quarter.* Same conclusion as the circle, through (A.7)–(A.8): $\arg(f\,\dd Z)$ is
constant only at $p=q=-1$ (C.2), the Schwarz function exists and is algebraic, and the resulting
one-dimensional integral is again powers against a ${}_2F_1$. The precise form differs from (A.9),
and the difference is worth stating (added in the consolidation pass of 2026-09-23; an argument, not
machine-checked — `## Next`, item 6). In the uniformiser $Z=(cw+1)^2/4cw$, $\bar Z=(w+c)^2/4cw$ of (L.0),
$f\,\dd Z$ is a product of powers of the linear factors $cw\pm1$, $w$, while
$\overline{G}=G(\bar Z)+\text{const}$ is the ${}_2F_1(\alpha,1-\gamma;\alpha+1;\cdot)$ of (A.3) at the
argument $(w+c)^2/4cw=\bigl(1+x\bigr)^2/4x$, $x=w/c$ — the argument of Gauss's quadratic transformations
(up to $z\mapsto1/z$, which needs no parameter condition). By Goursat's criterion (DLMF 15.8(iii)) a
quadratic transformation of ${}_2F_1(a,b;c;z)$ exists iff two of $\pm(1-c)$, $\pm(a-b)$, $\pm(a+b-c)$
coincide or one equals $\pm\tfrac12$; here $(1-c,a-b,a+b-c)=(-\alpha,\ \alpha+\gamma-1,\ -\gamma)$,
and the criterion holds exactly on the lines $p=q$, $p+q=-4$, $q=0$, $2p+q=-4$, $p=0$, $p+2q=-4$,
$p\in\{-1,-3\}$, $q\in\{-1,-3\}$, $p+q\in\{-1,-3\}$ — the parameter lines on which the ${}_2F_1$
admits *a* quadratic transformation (of some argument); the list contains every special locus found
above except $q=-2$ ($p=0$, $q=0$, $p=q$, $2p+q=-4$, $p+q=-4$, $q=-1$ are on it; $q=-2$ is
$a+b-c=0$, the logarithmic case, not on it) and no two-dimensional region. Only a sub-family acts on
the ellipse argument itself (fix pass 2026-09-23, after the node check; an argument, not
machine-checked): the map $z=(1+x)^2/4x$ has $\dd z/\dd x=(x^2-1)/4x^2$, so it is ramified at
$x=-1$ over $z=0$ and at $x=1$ over $z=1$, while $z=\infty$ has the two unramified preimages
$x=0,\infty$. The pull-back of the hypergeometric equation is Fuchsian in $x$ with the four singular
points $x=-1,1,0,\infty$ and exponent differences $2(1-c)$, $2(c-a-b)$, $a-b$, $a-b$; it is again a
three-point (${}_2F_1$-in-$x$) equation iff one ramified point becomes ordinary, i.e. $1-c=\pm\tfrac12$
or $a+b-c=\pm\tfrac12$ — the lines $p\in\{-1,-3\}$ or $q\in\{-1,-3\}$ (the unramified points keep the
non-integer difference $a-b$ and stay singular). On the seven "two equal differences" lines the
available quadratic transformation is ramified over other pairs of points (on $1-c=\pm(a-b)$, for
instance, its argument $4z/(1+z)^2$ composed with $z(x)$ is of degree four in $x$), so it does not
linearise the ellipse argument. Off the lines $p\in\{-1,-3\}$, $q\in\{-1,-3\}$ the ellipse integrand is
therefore (powers of four linear factors in $w$)$\times{}_2F_1$ at a degree-two rational argument
that cannot be reduced to a linear one by a quadratic transformation, so the ellipse arc is *more*
obstructed than the circle, not equally: (A.11) does not even apply to it as written. The verdict
(one-dimensional integral of a ${}_2F_1$ at generic $(p,q)$) is unchanged; what this adds is that
the two curved arcs obstruct for structurally different reasons, and that the lines $p\in\{-1,-3\}$,
$q\in\{-1,-3\}$ — not the full Goursat list — are the natural next family to test for closure of
the ellipse piece; $p=q=-1$, where the ellipse does close, lies in it, and $p=0$, $q=0$ close
because $G$ is elementary there, with no transformation needed. (Its confocal structure – foci at $0$ and $1$ – is what route (c′) exploits; see Block B.
The anti-Möbius map $Z\mapsto1-\bar Z$ fixes the *full* ellipse setwise; it does not fix the quarter
arc, but for $p=q$ it does relate $\overline G$ on the quarter to $G$ on the mirror quarter.)

\subsection*{Commentary}

- (A.1)–(A.2): standard; the content is the branch choice A3, which makes $f$ single-valued on
  $R$ – $R$ touches the negative axis, so the principal cut of $Z^{p/2}$ is on $\partial R$ and the
  boundary value from above must be used consistently in $f$ and in $G$. This is the step the
  harness falsifies (`C1.3-derivative`, `C1.3-path`, `C1-closure`).
- (A.2), second form: $J$ real forces $\operatorname{Re}\oint f\overline G\dd Z=0$; the per-arc
  split of $\tfrac1{2\I}\int f\overline G\dd Z$ carries a spurious *imaginary* part
  $\tfrac1{4\I}[\lvert G\rvert^2]$ (the bracket is real, the prefactor $\tfrac1{4\I}$ imaginary)
  that telescopes around the loop. The swept-area form $J_k$ is the meaningful per-arc quantity.
- (A.3): the ${}_2F_1$ representation is the analytic continuation in $\alpha$ of
  $\int_0^Zw^{\alpha-1}(1-w)^{\gamma-1}\dd w$; for $p\le-2$ it is no longer that integral but is
  still an antiderivative. At $\alpha\in\{0,-1,\dots\}$ (A4) the normalisation has a pole; the
  difference (A.4) has a finite limit, and $J$ is entire (045 C1), so nothing is lost.
- (A.5)–(A.6): the "constant phase" mechanism – the image of an arc is a straight line iff
  $\arg(f\,\dd Z)$ is constant on it, and sweeps no area iff that line passes through the base point
  (`## Corrections 2026-09-23`, item 1). This holds on the real segment for all $(p,q)$, on the
  vertical segment iff $p=q$, on the circle iff $2p+q=-4$ (contribution $0$), on the ellipse iff
  $p=q=-1$ (triangle (C.3)); it fails on the two curved arcs at generic $(p,q)$ and at $(0,0)$.
- (A.7)–(A.8): the Schwarz function of an arc is the algebraic function agreeing with $Z\mapsto\bar Z$
  *on that arc only*; its existence is generic for circles, lines and conics and is not a symmetry of
  $\mathbb C\setminus\{0,1\}$. What (A.8) buys is that $\overline G$, an anti-holomorphic object, is the
  boundary value of a holomorphic one, so the arc contributions of (A.2) are ordinary contour
  integrals. It holds as written on the three curved arcs; on the real segment the right-hand side
  must be read with the boundary value of $B_w$ from below the cut, which is not A3's choice — the
  segment is closed by (A.5) instead, so nothing depends on it. An earlier version of this record asserted the opposite ("Schwarz reflection does not
  apply"), located the obstruction in a missing Möbius symmetry, and called constant phase and
  reflection "the only two mechanisms"; the critic of iteration 1 refuted that, and `C2.3-reflect`
  now checks (A.8) on all three curved arcs. The verdict of route (a) is unchanged — only the reason.
- (A.9)–(A.11): the obstruction proper, and what it is not. It is **not** the endpoints: (A.10) shows
  that a single power against a ${}_2F_1$ integrates to a ${}_3F_2$ at an arbitrary endpoint, so the
  earlier statement of this record ("no antiderivative between endpoints outside $\{0,1,\infty\}$")
  was false and is withdrawn. It is the second power: (A.11) is a Kampé de Fériet double series in
  one variable, single-series under Euler's condition $\mu=a+b-c$ (C.4), which on (A.9) selects
  $p=0$ (Pfaff (B)), $q=-2$ (Pfaff (A)) and $q=-1$ (directly) — circle only, and sufficient only
  (`## Corrections 2026-09-23`, item 3). For generic $(p,q)$ the exponents are
  unmatched and route (a) stops there; on $p=0$ and $q=0$ it does not stop, and $J$ closes (C2.4).

\subsection*{Result}

Route (a) yields the exact one-dimensional representation (A.2) with $G$ the incomplete Beta (A.4):
$J(p,q)$ is the area of $G(R)$. Per arc: real segment $0$ (A.5); vertical segment closes by the
constant-phase mechanism iff $p=q$ (A.6); the circle closes by it iff $2p+q=-4$ (contribution $0$)
and the ellipse iff $p=q=-1$ (C.3); at generic $(p,q)$ circle and ellipse remain one-dimensional integrals of a
${}_2F_1$ times its derivative, $\tfrac12\int\operatorname{Im}\bigl(\overline G\,G'(Z)\,Z'(t)\bigr)\dd t$.
**Verdict of route (a) for generic $(p,q)$: category 3 of the brief (1D integral of Gauss ${}_2F_1$),
not a closed form.** The obstruction is *not* a missing symmetry: Schwarz reflection holomorphises
$\overline G$ on the three curved arcs (A.7)–(A.8) (and on the real segment with the lower boundary
value). It is that the resulting holomorphic contour integral (A.9) is
(two powers)$\times{}_2F_1$ with exponents unmatched to the hypergeometric parameters, whose
antiderivative (A.11) is a Kampé de Fériet double series, single-series under Euler's condition
$\mu=a+b-c$ (sufficient, not necessary); on the ellipse the ${}_2F_1$ sits at a quadratic-rational
argument with no quadratic transformation available at generic $(p,q)$.
On the lines $p=0$ and $q=0$ route (a) closes: $J(0,q)$ and $J(p,0)$ are
finite combinations of ${}_2F_1$ and Appell $F_1$, (L.6) and (L.12) (C2.4); at $(-1,-1)$ it closes in
${}_2F_1$ endpoint values and one ${}_3F_2$ (C.3), (C.6).

\subsection*{Verification}

See `## Verification` below (checks `C1.3-*`, `C1-closure`, `C3-*`, `C2-*` of
`codes/verify-j-closed-form.py`).

## Block B — Route (c′): the confocal structure of $R$ (skeleton-stage observation, verified)

\subsection*{Setup}

Assumptions A1, A2. Bipolar variables $r=\lvert Z\rvert$, $\rho=\lvert1-Z\rvert$, and
$u=r+\rho$, $v=\rho-r$. This block is not part of route (a); it is recorded because it changes the
ranking of routes (b)–(c) for the continuation and because its verification was cheap.

\subsection*{Derivation}

From $\rho^2=1-2x+r^2$: $x=\tfrac12(r^2-\rho^2+1)$, $y=\sqrt{r^2-x^2}$ on the sheet $y\ge0$, and
$$\frac{\partial(x,y)}{\partial(r,\rho)}=\frac{r\rho}{y},\qquad
 4y^2=\bigl((r+\rho)^2-1\bigr)\bigl(1-(\rho-r)^2\bigr)=(u^2-1)(1-v^2).\tag{B.1}$$
With $\dd r\,\dd\rho=\tfrac12\dd u\,\dd v$ and $r\rho=\tfrac14(u^2-v^2)$,
$$\dd x\,\dd y=\frac{(u^2-v^2)\,\dd u\,\dd v}{4\sqrt{(u^2-1)(1-v^2)}}\qquad(y\ge0).\tag{B.2}$$
Since $a^2-b^2=\tfrac14$, the ellipse $\partial\mathcal V_{0,4}$ has foci at $\tfrac12\pm\tfrac12=0,1$, i.e.
$$\partial\mathcal V_{0,4}=\{\lvert Z\rvert+\lvert1-Z\rvert=2a\}=\{u=2a\}.\tag{B.3}$$
The other constraints: $\operatorname{Re}Z\le\tfrac12\iff\rho\ge r\iff v\ge0$; $\lvert Z\rvert\ge1\iff u-v\ge2$;
the triangle inequality gives $v\le1$ with equality on the negative real axis. Hence
$$R\ \longleftrightarrow\ D=\{0\le v\le1,\ 2+v\le u\le2a\},\qquad
\boxed{\ J(p,q)=2^{-p-q-2}\int_0^1\!\frac{\dd v}{\sqrt{1-v^2}}\int_{2+v}^{2a}\!\frac{\dd u}{\sqrt{u^2-1}}\,(u-v)^{p+1}(u+v)^{q+1}\ }\tag{B.4}$$
The four corners of the trapezoid $D$ are $(2,0)\leftrightarrow\e^{\I\pi/3}$, $(3,1)\leftrightarrow-1$,
$(2a,1)\leftrightarrow\tfrac12-a$, $(2a,0)\leftrightarrow\tfrac12+\I b$; the sides $v=0$, $v=1$, $u=2a$
are the vertical segment, the real segment and the ellipse, and the slanted side $u=2+v$ is the unit
circle. On the whole plane (two sheets, $v\in[-1,1]$, $u\ge1$) the same Jacobian gives
$2\cdot2^{-p-q-2}\int_{-1}^1\int_1^\infty$, which must reproduce the Virasoro–Shapiro form
$\pi\,\Gamma(1+\tfrac p2)\Gamma(1+\tfrac q2)\Gamma(-1-\tfrac{p+q}2)/[\Gamma(-\tfrac p2)\Gamma(-\tfrac q2)\Gamma(2+\tfrac{p+q}2)]$
for $p,q>-2$, $p+q<-2$ (check `C4-uv-VS`).

*Consequence for routes (b)/(c).* In (B.4) the expansion parameter $w=v/u=(\rho-r)/(\rho+r)$ obeys
$0\le w\le\tfrac13$ on $R$ (maximum at $Z=-1$), so
$$(u-v)^{p+1}(u+v)^{q+1}=u^{p+q+2}\sum_{n\ge0}c_n(p,q)\,w^n,\qquad
 c_n=\sum_{j=0}^n(-1)^j\binom{p+1}{j}\binom{q+1}{n-j},\tag{B.5}$$
converges geometrically at ratio $\le\tfrac13$ uniformly in $Z$ on $R$ — but **not** uniformly in
$(p,q)$: the $c_n$ grow like $\binom{\lvert p\rvert+n}{n}$, so the geometric decay only sets in after
$n\gtrsim\lvert p\rvert/2$ (see the Commentary) — unlike
the $1/Z$ expansion of route (b), which is marginal on the unit circle. Each term splits into the
rectangle $[3,2a]\times[0,1]$, where it factorises into $\tfrac12B(\tfrac{n+1}2,\tfrac12)$ times the
incomplete integral $\int_3^{2a}u^{p+q+2-n}(u^2-1)^{-1/2}\dd u$ (a ${}_2F_1$ in $1/u^2$), and the
triangle $\{2\le u\le3,\ 0\le v\le u-2\}$ where the $v$-dependent limit couples the variables. The
triangle piece is where a closed form would have to come from; it is the image of the unit-circle
arc's neighbourhood, the one boundary arc that is not a coordinate line of the confocal system.

\subsection*{Commentary}

- (B.1)–(B.2): the bipolar Jacobian; $4y^2$ is Heron's formula for the triangle with sides
  $1,r,\rho$, which is why the square root factorises.
- (B.3): the observation that makes $R$ a trapezoid. It relies only on $a^2-b^2=\tfrac14$ (record 045,
  from the ledger's ellipse), and is the geometric reason the ellipse arc is *not* the obstruction
  for a series approach: the unit-circle arc is.
- (B.5): the coefficients $c_n$ grow like $n^{\max(p,q)+1}$-type polynomials times binomial
  factors for large $\lvert p\rvert,\lvert q\rvert$; the number of terms for a given accuracy grows
  with $\lvert p\rvert+\lvert q\rvert$. The rigorous tail bound is left to the continuation.

\subsection*{Result}

(B.4) is an exact two-dimensional representation over a trapezoid with an algebraic weight; not a
closed form. Its value is (i) it identifies the unit-circle arc as the single feature of $R$
obstructing separation, and (ii) it provides the geometric ($\le\tfrac13$) expansion (B.5) for the
continuation's series route.

\subsection*{Verification}

Checks `C4-uv` (against `j_integral`, random $(p,q)$, both $\beta$) and `C4-uv-VS` (whole plane
against the Virasoro–Shapiro Beta form) of `codes/verify-j-closed-form.py`.

## Verification

Script `codes/verify-j-closed-form.py` (mpmath at 30 digits for the ${}_2F_1$ route, numpy double
precision for the Chebyshev route; seed printed; nonzero exit on failure). Current state: **25/25
PASS**, exit 0, seed 20260922 (full run of 2026-09-23, `agent/scratch/j-closed-form-full-fixpass-2026-09-23.log`);
seed 7 was also run at the 14-check stage. Growth of the harness: 14 checks (derivation, 2026-09-22),
`C2.3-reflect` added and `C3-ref-conv` tightened (fix pass, critic iteration 1), `C5-045-shift`
added (fix pass, critic iteration 2; the run log pasted at the end of this section is that 16-check
run, and the numbers of the table below are from it), `C7-item1-circle-line`, `C7-item2-ellipse-point`,
`C7-item3-euler`, `C7-item5-first-form`, `C7-item8-beta04` added, each with a break leg (corrections
2026-09-23; (A.11) leg of `C7-item8-beta04` added in the fix pass of the node check), `C6-closed-lines`,
`C6-appell-series`, `C6-area-limit`, `C6-no-symmetry` added (C2.4 pass 2026-09-23; their rows are in
the Verification block of `## The lines $p=0$ and $q=0$ with coefficients (2026-09-23)`). Checks,
named after the nodes they test:

| Check | What it compares | Outcome |
|---|---|---|
| `C1.3-derivative` | `mp.diff` of $G$ from (A.4) vs $f$ with branches A3, 8 random interior points, $\lvert p\rvert,\lvert q\rvert<30$ (a fixed-step central difference at 30 digits lost up to $10^{-9}$ at one seed-7 point where mpmath's ${}_2F_1$ is least accurate; replaced) | max rel $\lesssim10^{-26}$ |
| `C1.3-path` | $G$ from (A.4) vs `mp.quad` of $f$ along the straight path $-1\to Z$ | max rel $4.6\times10^{-30}$ |
| `C1-closure` | $\operatorname{Re}\oint f\overline G\dd Z=0$ and $\oint f\dd Z=0$ (accumulated $G$ returns to $0$) on the four parametrised arcs | $7\times10^{-15}$ |
| `C3-area` | (A.2) at $p=q=0$ vs (3.4) of 045, both $\beta$ | rel $3\times10^{-18}$ (${}_2F_1$), $10^{-15}$ (Chebyshev) |
| `C3-hyp` | (A.2) with $G$ from ${}_2F_1$ vs `j_integral` ($n=640$), 6 random $(p,q)$ per $\beta$, 2 per $\beta$ with $\lvert p\rvert+\lvert q\rvert>100$ (up to $(-91,-82)$, $(-86,+82)$; $J$ ranging over $10^{-5}$–$10^{22}$) | max rel $4.9\times10^{-10}$ |
| `C3-cheb` | same identity, $G$ by Chebyshev cumulative integration of $f$ along $\partial R$ (no hypergeometric function, degree 600) vs `j_integral` | max rel $4.9\times10^{-10}$ |
| `C3-mutual` | the two evaluations of (A.2) against each other | max rel $5.7\times10^{-11}$ (worst of 12 points; $10^{-15}$ at moderate exponents) |
| `C3-ref-conv` | at the points where the $n=160$ quadrature error is resolvable ($\ge1$ required, else FAIL), the errors of `j_integral` at $n=160,320,640$ relative to the boundary value fall monotonically with ratios in $[6,11]$ (window narrowed in the fix pass so that $n^{-2}$ and $n^{-4}$ are excluded) | PASS: ratios $\approx8$ ($n^{-3}$) |
| `C3-break` | (A.2) $\times(1+10^{-3})$ against the $2\times10^{-9}$ comparison | FAILS as required |
| `C2-real` | swept area of the real segment / $J$ | $1.8\times10^{-34}$ |
| `C2-vert`, `C2-vert-neq` | vertical arc at $p=q$ vs (A.6): rel $2\times10^{-17}$; the same formula at $p\ne q$ deviates by $\ge0.47$ | PASS / PASS |
| `C2.3-reflect` | (A.8) on the three curved arcs: $\overline{G(Z)}-G(S(Z))$ constant along each arc, $S$ from (A.7), 4 random/fixed $(p,q)$ per $\beta$, arc points and $S$ built at mpmath precision; break leg feeds each arc the Schwarz function of a *different* arc | max relative spread $6.3\times10^{-29}$; break leg min spread $5.9\times10^{-3}$, fires as required |
| `C5-045-shift` | $F(s,T,T)$ of R48 at record 045's 18 headline points, each tile $J$ by `j_integral`($n=40$) vs by `J_boundary_cheb`(deg 600); asserts $\max\lvert\text{shift}\rvert<10^{-6}$ and Chebyshev 600 vs 900 $<10^{-13}$. The reproducible source of the table in `## Consequence for 045` | max shift $4.0\times10^{-7}$, max 600/900 $8.8\times10^{-15}$ |
| `C7-item1-circle-line` | (C.1): unit phase of $f\,\dd Z$ constant on the circle at 3 seeded $(p,q)$ on $2p+q=-4$ (mpmath arc points) and $\lvert J_{\text{circle}}/J\rvert<10^{-12}$; control $p+q=-2$; break leg: the old criterion $\arg f$ | spread $5\times10^{-31}$, ratio $2\times10^{-18}$; control $\ge0.04$; break $1.0$ |
| `C7-item2-ellipse-point` | (C.2)–(C.3) at $(-1,-1)$; 3 random off-point $(p,q)$; break leg: (C.3) with endpoints exchanged | spread $2\times10^{-31}$, rel $4\times10^{-17}$; off-point $\ge0.1$; break $2.0$ |
| `C7-item3-euler` | (C.4) with $\mu=A+B-C$ vs $C-A-B$; (C.5)(A),(B) pointwise vs the mixed form; (C.6) vs quadrature at $p\in\{-3.4,1.7\}$; $J(-1,-1)$ assembled from (A.6), (C.3), (C.6) vs `J_boundary_hyp` and `j_integral`(640); break leg: wrong branch of $w^{1/2}$ at $-1$ in (C.6) | $4\times10^{-31}$ vs $1.0$; $3\times10^{-31}$, mixed spread $0.18$; (C.6) $4\times10^{-31}$ (break $1.0$); $J(-1,-1)$: $4\times10^{-18}$, $4\times10^{-11}$ |
| `C7-item5-first-form` | (C.8) at $(-3.4,2.1)$, $(1.7,-5.3)$; break leg: imaginary term dropped | $9\times10^{-17}$; break $0.1$ |
| `C7-item8-beta04` | $a(\beta_{04})=\tfrac32$ exactly, $a<\tfrac32$ below; (A.10) by quadrature; break leg: (A.10) without $1/(\lambda+1)$; (A.11) leg: the double series with the $\tfrac1{\lambda+1}$ prefactor (truncated at $m+n<90$) vs quadrature of $w^{\lambda}(1-w)^{\mu}{}_2F_1$ at $(\lambda,\mu,z)=(0.3,0.6,0.4+0.2\I)$, $(0.85,1.7,-0.3+0.35\I)$, and its $\mu=0$ specialisation vs (A.10); break leg: prefactor dropped | $a(\beta_{04})-\tfrac32=0$, $a(\beta_{04}-0.05)=$ (companion value, not reproduced here); (A.10) $2.5\times10^{-32}$ (break $7.3\times10^{-2}$); (A.11) $1.5\times10^{-30}$, $\mu=0$ leg $2.5\times10^{-32}$ (break $6.3\times10^{-2}$) |
| `C4-uv` | (B.4) by nested `mp.quad` vs (A.2) and vs `j_integral`(640), 4 random points | $1.5\times10^{-15}$, $5.1\times10^{-11}$ |
| `C4-uv-VS` | bipolar Jacobian on $\mathbb C$ vs the Virasoro–Shapiro Beta form at $(p,q)=(-1.5,-1.5),(-1.2,-1.7),(-1.0,-1.6)$ | max rel $3.8\times10^{-11}$ |

Findings of the verification beyond PASS/FAIL:

- **The 2D reference is the less accurate side.** `j_integral` converges as $n^{-3}$ (square-root
  branch point of its inner limits $\mp\sqrt{1-y^2}$ at the panel endpoint $y=1$); at its default
  $n=40$ its relative error is $\approx2\times10^{-6}$ at $(p,q)=(-14.7,-4.4)$, $\beta=\tfrac32$, and
  $\approx10^{-8}$ at $n=160$. The two evaluations of (A.2) agree to $\lesssim10^{-10}$ (worst of the
  12 points; $10^{-15}$ at moderate exponents). The tolerance of the C3 checks ($2\times10^{-9}$) is
  the reference's accuracy at $n=640$, not the representation's. Any future comparison at the
  $10^{-6}$ level that uses `j_integral` at $n=40$ (record 045's checks did) is limited by the
  reference. **Measured, not asserted, in the fix pass:** see `## Consequence for 045` — the
  induced shift in $F(s,t,u)$ at 045's own headline points is $\le4\times10^{-7}$ relative, three to
  four orders below 045's $10^{-3}$-level conclusions.
- **Cost.** Chebyshev route: $4\times600$ elementary evaluations of $f$ per $J$, double precision,
  $\lesssim10^{-10}$ relative (worst of 12 points; $10^{-15}$ at moderate exponents); `j_integral` at $n=640$: $\sim1.2\times10^6$ evaluations for $10^{-9}$.
  The ${}_2F_1$ route is exact but slow in mpmath (up to 20 s per $J$ at $\lvert p\rvert+\lvert q\rvert\sim170$).
- Excluded from `C4-uv-VS`: $(p,q)=(-0.5,-1.9)$, where the corner singularity $r^{-0.8}$ at $Z=1$
  leaves nested tanh–sinh at $4\times10^{-3}$; a quadrature limitation, stated in the docstring.
- The Chebyshev degrees ($601$ interpolation points, $600$-point Gauss–Legendre) are not matched: the
  cumulative integration of the interpolant is exact, the subsequent quadrature of the *product*
  $\overline G\,h$ (degree $\approx1200$) is not, being exact only to polynomial degree $2\,\mathrm{deg}-1$.
  Harmless — the tail coefficients are below the working precision — but the docstring's
  "integrated exactly" refers to the cumulative step only, and now says so.
- Not machine-checked: the negative statement C2.3 itself (no closed form on the curved arcs by the
  boundary route at generic $(p,q)$ — its two ingredients are checked: constant phase by
  `C2-vert`/`C2-vert-neq`, reflection by `C2.3-reflect`; what is not machine-checkable is the
  non-existence of an antiderivative for (A.9)); the quadratic-transformation argument on the ellipse
  arc (Block A, *C2, ellipse quarter*; `## Next` item 6); the series claims of C4.1. Node C2.4 is
  machine-checked (`C6-*`).

Run log of the fix pass of critic iteration 2 (`.venv/bin/python codes/verify-j-closed-form.py 20260922`, exit 0); the per-point lines of
`C3-hyp`/`C3-area` and the eighteen of `C5-045-shift` are elided, everything else is verbatim:

```text
seed = 20260922
[PASS] C1.3-derivative — max rel |G' - f| = 2.9e-30 (8 points, |p|,|q|<30)
[PASS] C1.3-path — max rel |G - int_{-1}^Z f| = 4.6e-30 (mpmath quad)
[PASS] C1-closure — max(|Re oint|/|Im oint|, |G(-1) after loop|/sqrt J) = 7.0e-15
[PASS] C3-area — boundary representation at p=q=0 vs 045 eq. (3.4)
[PASS] C3-ref-conv — j_integral errors vs boundary value fall as n^-3 (ratios in [6,11]) at the 5 resolvable points (>= 1 required)
[PASS] C3-hyp — boundary (2F1) vs j_integral(n=640), 6 points per beta incl. |p|+|q|>100, max rel 4.9e-10
[PASS] C3-cheb — boundary (Chebyshev, no 2F1) vs j_integral(n=640), max rel 4.9e-10
[PASS] C3-mutual — 2F1 vs Chebyshev evaluations of the boundary representation, max rel 5.7e-11
[PASS] C3-break — representation x (1+1e-3) fails the 2e-9 comparison at (p,q,beta)=(-12.574,18.560,1.5)
[PASS] C2-real — real-segment swept area / J, max 1.8e-34
[PASS] C2-vert — vertical arc at p=q vs (1/2) Re G(e^(i pi/3)) Psi, max rel 2.0e-17
[PASS] C2-vert-neq — the p=q formula does not extend to p!=q (min rel deviation 4.7e-01)
[PASS] C2.3-reflect — conj(G) - G(S) constant along circle/vertical/ellipse arcs (4 (p,q) per beta): max relative spread 6.3e-29; break leg (Schwarz function of the wrong arc): min spread 5.9e-03, must exceed 1e-4
        (the eighteen per-point lines printed here are the table of `## Consequence for 045`; elided)
[PASS] C5-045-shift — F(s,T,T) of R48 at 045's 18 headline points: max |relative shift of the n=40 quadrature| 4.0e-07 (< 1e-6) at beta=1.5, box (HS, preliminary), a'P^2=5.333; max Chebyshev 600/900 discrepancy 8.8e-15 (< 1e-13)
[PASS] C4-uv — bipolar representation, 4 points: max rel vs boundary 1.5e-15, vs j_integral(640) 5.1e-11
[PASS] C4-uv-VS — bipolar Jacobian on C vs Virasoro-Shapiro Beta form, 3 points, max rel 3.8e-11
16/16 checks passed (seed 20260922)
```

## Result

1. **Route (a) verdict.** $J(p,q)$ has the exact one-dimensional representation
   $$J(p,q)=\tfrac12\operatorname{Im}\oint_{\partial R}\overline{G}\,\dd G,\qquad
     G(Z)=B_Z\bigl(\tfrac p2+1,\tfrac q2+1\bigr)-B_{-1}\bigl(\tfrac p2+1,\tfrac q2+1\bigr),$$
   the area of the image of $R$ under the incomplete-Beta map, valid for all real $(p,q)$ and
   $\beta\ge\beta_{04}$. Per arc, the image is straight iff $\arg(f\,\dd Z)$ is constant, and then
   the arc closes in endpoint values of $G$:

   | Arc | constant phase iff | contribution there | closes otherwise? |
   |---|---|---|---|
   | real segment | all $(p,q)$ | $0$ (A.5) | — |
   | vertical segment | $p=q$ | $\tfrac12\operatorname{Re}G(\e^{\I\pi/3})\,\Psi(b)$ (A.6) | as an incomplete Beta on $p=0$ (L.3), $q=0$ (L.9), $p+q=-4$ ($G$ elementary, `## Corrections` item 3(b)) |
   | unit circle | $2p+q=-4$ | $0$ exactly (image line through $G(-1)=0$) | as a single ${}_3F_2$ on $q=-1$ (C.6), $q=-2$ (Euler absorption, circle arc only); as an incomplete Beta on $p+q=-4$ ($G$ elementary, item 3(b)) and on $p=0$ (L.2); elementary on $q=0$ (L.8) |
   | ellipse quarter | $p=q=-1$ | triangle $\tfrac12\operatorname{Im}\bigl(\overline{G(\tfrac12+\I b)}\,G(\tfrac12-a)\bigr)$ (C.3) | two Appell $F_1$ on $p=0$, $q=0$ (L.5), (L.11) |

   **$J$ itself closes** on the lines $p=0$ and $q=0$ — (L.6) and (L.12), ${}_2F_1$ and Appell $F_1$ —
   and at the point $(-1,-1)$ (${}_2F_1$ endpoint values and one ${}_3F_2$); nowhere else was a
   closure found. **For generic $(p,q)$ the circle and ellipse arcs stay one-dimensional integrals
   of $\operatorname{Im}\bigl(\overline G\,G'(Z)\,Z'(t)\bigr)$, a ${}_2F_1$ times its derivative:
   category 3 of the brief, not a closed form.** The obstruction is the pair of powers at generic
   exponents against the ${}_2F_1$ ((A.9), (A.11), single-series only under Euler's $\mu=a+b-c$, a
   sufficient condition), and on the ellipse additionally the quadratic-rational argument of the
   ${}_2F_1$ (Block A, *ellipse quarter*). Verified against the 2D quadrature at 12 random $(p,q)$
   up to $\lvert p\rvert+\lvert q\rvert\approx170$, both $\beta$; the closed forms on the two lines
   at 16 points to $1.4\times10^{-15}$.
2. **Practical consequence.** The hypergeometric-free evaluation of the same identity (Chebyshev
   cumulative integration along $\partial R$) computes $J$ to $\lesssim10^{-10}$ (worst of the 12 test
   points; $10^{-15}$ at moderate exponents) with $\sim2400$
   elementary evaluations in double precision – three orders of magnitude cheaper than the 2D
   reference at $10^{-9}$, and with a spectral (geometric) error bound from the analyticity of
   $f(Z(t))Z'(t)$ on each arc (the integrand is analytic on a neighbourhood of every closed arc
   parameter interval, since $R$ avoids $0,1$; Bernstein-ellipse bound, not quantified here).
3. **Structural finding (Block B).** $\partial\mathcal V_{0,4}$ is the confocal ellipse with foci
   at the branch points $0,1$; in $(u,v)=(\lvert Z\rvert+\lvert1-Z\rvert,\lvert1-Z\rvert-\lvert Z\rvert)$
   the region is the trapezoid $\{0\le v\le1,\ 2+v\le u\le2a\}$ with the elementary weight (B.4).
   The single feature of $R$ obstructing separation and term-wise closed forms is the unit-circle
   arc $u=2+v$ (the $\lvert Z\rvert\ge1$ side of the fundamental domain) – not the ellipse.
4. **Interpretation for the objective.** No closed form was obtained. The brief's condition
   "a representation replacing 2D quadrature by something exact or rapidly convergent with a
   rigorous error bound" is met by (1)–(2) **as to exactness** — (A.2) is an identity, not an
   approximation, and its Chebyshev evaluation is spectrally convergent — but **not yet as to the
   rigorous bound**: the Bernstein-ellipse parameter of each arc is computable and is not computed
   here (`## Next`, item 2). What is available instead is the empirical figure $\lesssim10^{-10}$
   over 12 points. Whether this lifts the need for the sister grid depends on what the grid is for:
   if it is only to *evaluate* $F(s,t,u)$ of R48 at the box of 045, this project can do it now (six
   $J$'s per point, milliseconds each) — with the caveat that R48 is `Conditional` on its imported
   inputs (`SL: R51`, `SL: R6`/`SL: R10`), so what is evaluated is the declared-section contact term
   *under those conditions*, whereas the mathematics of $J$ established here is unconditional; if it
   is to *compare* the declared-section contact term against the sister's independent machinery, the
   grid is still the comparator and nothing here replaces it. The orchestrator decides; the record
   does not.

### Scope of the exclusion

**Class covered.** Closed forms for $J(p,q)$ reachable by the boundary route (A.2), i.e. by reducing
each arc contribution to endpoint values of functions in the brief's classes (finite combinations of
Gauss ${}_2F_1$, Appell $F_1/F_2$). *Reason for the class:* (A.2) is an exact identity valid for all
real $(p,q)$ and all $\beta\ge\beta_{04}$, and it is the cheapest reduction of the two-dimensional
integral; it is the route a closed form would most naturally come through, not an artificially small
class.

**The exclusion is for generic $(p,q)$**, and "generic" is spelled out. $J$ itself closes by route (a)
on the lines $p=0$ and $q=0$: $J(0,q)$ is (L.6), $J(p,0)$ is (L.12) — incomplete Betas on the circle
(elementary on $q=0$) and vertical arcs, two Appell $F_1$ on the ellipse arc through R2's uniformiser
$Z=Z_4^{(s)}(1/w)=(4\beta^2w+1)^2/16\beta^2w$ (node C2.4, `C6-closed-lines`, 16 points to $1.4\times10^{-15}$) —
and at the point $(-1,-1)$, where all four arcs close (${}_2F_1$ endpoint values and one ${}_3F_2$,
(C.3), (C.6)). In R48's ordered Mandelstam triple the two lines are the codimension-one loci
$x=y+z$ and $y=x+z$, so the objective (a formula on the grid) is untouched; but they are inside the
class this exclusion covers, so the exclusion is stated off them. Single arcs close on further
lower-dimensional loci without closing $J$: the vertical segment on $p=q$, the circle on $2p+q=-4$
(contribution exactly $0$; $\alpha'(x-y-3z)=-16$ in R48's variables), as a single ${}_3F_2$ on
$q=-1$, $q=-2$, and as an incomplete Beta on $p+q=-4$ ($G$ elementary; the vertical segment closes
there too); the ellipse at $p=q=-1$. No two-dimensional region of the $(p,q)$ plane
closes. (The lines $p=0$, $q=0$, $p=q$, $2p+q=-4$, $p+q=-4$, $q=-1$ are all among the lines on
which the incomplete Beta's ${}_2F_1$ admits a quadratic transformation, Block A *ellipse quarter* —
an observation of the consolidation pass, not a checked claim.)

**What the obstruction is, and is not.** It is *not* a missing symmetry. Both mechanisms available on
an arc do apply in the expected places: constant phase (criterion $\arg(f\,\dd Z)$) closes the real segment for every $(p,q)$,
the vertical segment for $p=q$, the circle for $2p+q=-4$ and the ellipse at $p=q=-1$; Schwarz reflection (A.7)–(A.8) applies on the three curved arcs
(circle and ellipse included, and on the real segment with the boundary value of $B_w$ from below the
cut), making each arc contribution a contour integral of a holomorphic integrand. Nor is it the
endpoints: by (A.10), a single power against a ${}_2F_1$ integrates to a ${}_3F_2$ at an arbitrary
endpoint. The obstruction is the **pair of powers at generic exponents**: by (A.9) the arc integrals
are $\int(\text{two powers})\times{}_2F_1$ with exponents unmatched to the hypergeometric
parameters, and the antiderivative (A.11) is a Kampé de Fériet double series in one variable, which
collapses to a single hypergeometric series when Euler's transformation absorbs a power
($\mu=a+b-c$; i.e. $p=0$, where $J$ itself closes, or $q=-1$, $q=-2$ on the circle alone) or
when the ${}_2F_1$ degenerates ($p+q=-4$) — sufficient conditions; no necessary one is established.
On the ellipse arc the ${}_2F_1$ sits at a quadratic-rational argument of the uniformiser, and a
quadratic transformation exists only on the lines listed in Block A (*ellipse quarter*): that arc is
more obstructed than the circle, not equally.

**Cases outside the class.** The series route (c′) of Block B (open, C4.1); any identity special to
incomplete Beta functions along confocal conics (none known to this record); and, as a *lead only*, a
**contour deformation** of the circle piece off $\lvert Z\rvert=1$, possible because the integrand is
holomorphic after (A.8) — but the endpoints $-1$ and $\e^{\I\pi/3}$ stay on $\lvert Z\rvert=1$, so a
$1/Z$ expansion on the deformed contour is still marginal at both ends and only the interior of the
contour is improved. Whether this rescues route (b) is not examined here.

**Weakest relaxation that would evade the exclusion.** Either (i) a reduction of (A.9) at the
endpoints $\e^{\pm\I\pi/3}$, $\tfrac12\pm\I b$, $\tfrac12-a$ — e.g. a contiguous-relation or
quadratic-transformation accident special to the contiguity $c=a+1$ that the incomplete Beta always
has (its ${}_2F_1(\alpha,1-\gamma;\alpha+1;Z)$ in (A.3) has third parameter one above the first, for
every $(p,q)$ — an earlier version of this paragraph wrote this condition as "$\gamma=\alpha+1$",
which in this record's notation would be the unrelated line $q=p+2$); it would close the circle arc
and leave only the ellipse; or (ii) a closed form for
$\int_{2}^{3}\frac{\dd u}{\sqrt{u^2-1}}\int_0^{u-2}\frac{v^n\,\dd v}{\sqrt{1-v^2}}u^{m}$ (the triangle
piece of (B.5)), which would make every term of the geometric series closed.

## Proposed ledger row

Final text of R50 after the consolidation of 2026-09-23, incorporating the five edits (i)–(v) of the
corrections and fix passes (constant-phase criterion and loci; Euler absorption sufficient only, with
its lines; the $J(-1,-1)$ corollary; C2.4 verified with its two sharpenings; the $\tfrac1{\lambda+1}$
prefactor) and the SL(2,C) review status. One line, in the ledger's format; the orchestrator promotes it:

| R50 | **The tile integral $J(p,q)=\int_{\mathrm{FD}\cap\mathcal V_{0,4}}\lvert Z\rvert^p\lvert1-Z\rvert^q\,\mathrm d^2Z$ of R48 has an exact one-dimensional boundary representation; it closes on the lines $p=0$, $q=0$ and at $(-1,-1)$, and for generic $(p,q)$ has no closed form by the boundary route (derivation 047; critics 2026-09-22: iteration 1 REVISE mechanical → fix, iteration 2 node-check → fix; SL(2,C) external review 2026-09-23, five items confirmed and applied, node check → fix; consolidated 2026-09-23).** $J=\tfrac12\operatorname{Im}\oint_{\partial R}\overline G\,\mathrm dG$ with $G=B_Z(\tfrac p2+1,\tfrac q2+1)-B_{-1}(\cdot)$ the incomplete Beta (principal branches, boundary values from above on the negative axis): the area of $G(R)$, valid for $\beta\ge\beta_{04}$ ($\beta_{04}=$ (companion value, not reproduced here); the four-arc region). An arc closes by constant phase iff $\arg(f\,\mathrm dZ)$ is constant on it: real segment always ($0$), vertical segment iff $p=q$, unit circle iff $2p+q=-4$ (contribution exactly $0$), ellipse iff $p=q=-1$ (a triangle in two endpoint values of $G$). On $p=0$ and $q=0$ the route closes with all coefficients: $J(0,q)$ and $J(p,0)$ are finite combinations of ${}_2F_1$ (incomplete Betas on the circle and vertical arcs; the circle elementary on $q=0$) and two Appell $F_1$ on the ellipse arc through R2's uniformiser $Z=Z_4^{(s)}(1/w)=(4\beta^2w+1)^2/16\beta^2w$ (first argument $c-\mathrm i0$ at $w=-1$ on $q=0$), verified at 16 points to $1.4\times10^{-15}$ (`C6-closed-lines`); the two lines are not related by a symmetry of $R$. $J(-1,-1)$ closes in ${}_2F_1$ endpoint values and one ${}_3F_2$. For generic $(p,q)$ — off these lines and this point — circle and ellipse arcs stay one-dimensional integrals of (two powers)$\times{}_2F_1$ with unmatched exponents: a Kampé de Fériet double series in one variable (antiderivative $\tfrac{z^{\lambda+1}}{\lambda+1}\sum_{m,n}\dots$, prefactor included), single-series when Euler's transformation absorbs a power ($\mu=a+b-c$; sufficient, not necessary: $p=0$ and $q=-2$, one per Pfaff representative, $q=-1$ directly, and the degenerate $p+q=-4$ where $G$ is elementary; circle arc only). The obstruction is not a missing symmetry — every arc carries an algebraic Schwarz function ($1/Z$, $1-Z$, $\tfrac12+4(a^2+b^2)(Z-\tfrac12)\pm8ab\sqrt{Z(Z-1)}$ on the confocal ellipse, branch points at the foci $0,1$ since $a^2-b^2=\tfrac14$), so reflection holomorphises $\overline G$ on the three curved arcs (checked to $10^{-29}$) — nor the endpoints (one power against a ${}_2F_1$ integrates to a ${}_3F_2$ at any endpoint); on the ellipse the ${}_2F_1$ sits moreover at a quadratic-rational argument (argument, not machine-checked). Not a proof of non-existence. In confocal coordinates $u=\lvert Z\rvert+\lvert1-Z\rvert$, $v=\lvert1-Z\rvert-\lvert Z\rvert$ the region is the trapezoid $\{0\le v\le1,\ 2+v\le u\le2a\}$ with elementary weight; the unit-circle side is the only non-coordinate boundary. Hypergeometric-free evaluation by Chebyshev cumulative integration along $\partial R$: $\sim2400$ evaluations, agreement with the ${}_2F_1$ evaluation $\lesssim10^{-10}$ (worst of 12 points, $10^{-15}$ at moderate exponents) and with 2D quadrature to its $2\times10^{-9}$ at $\lvert p\rvert+\lvert q\rvert\le170$, $\beta\in\{\tfrac32,2\}$; rigorous error bound not yet quantified. Side findings: `j_integral` of `verify-kp-box.py` converges as $n^{-3}$ (square-root branch point at the panel endpoint $y=1$), $\sim10^{-6}$ at $n=40$; the induced shift of the six-$J$ contact term at 045's eighteen headline points is $\le4\times10^{-7}$ (check `C5-045-shift`), so no 045 conclusion moves. **Consequence for the SL(2,C) exchange: this project evaluates $K_P$ itself.** The derivation belongs to the companion paper (decision of 2026-09-22); this project cites it. | Verified (25/25 PASS, seed 20260922, exit 0, 11 break legs firing in 9 checks (`C3-break`, `C2.3-reflect`, `C7-item1/2/3/5`, `C7-item8` two legs, `C6-closed-lines` two legs, `C6-appell-series`); unconditional as mathematics of $J$; relevance to $K_P$ inherits R48's conditions `SL: R51`, `SL: R6`/`SL: R10`); representation independently re-implemented and checked by a sibling project; its review of the obstruction section applied | `agent/derivations/047-j-integral-closed-form.md`; `codes/verify-j-closed-form.py` |

## Fix pass 2026-09-22 (critic iteration 1)

Critic report: `agent/reports/critic-047-20260922T164500.md` (verdict REVISE, mechanical; 0 Fatal,
2 Serious, 4 Concern, 6 Minor). Every finding, its resolution and its location:

| # | Finding (severity) | Change made | Location in this record / script |
|---|---|---|---|
| 1 | Stated obstruction is wrong: Schwarz reflection *does* holomorphise $\overline G$ on every arc (Serious) | Re-derived the mechanism, added the Schwarz functions (A.7), the identity (A.8), the circle reduction (A.9) and the by-parts form on the vertical segment; the obstruction is now stated as the absence of an antiderivative for (power)$\times{}_2F_1$ between endpoints outside $\{0,1,\infty\}$; "the only two mechanisms" dropped; contour-deformability of the circle piece recorded as a positive by-product | Block A (*C2.3, the reflection mechanism…*), Commentary bullets 5–6, node C2.3, `### Scope of the exclusion` (rewritten: class, obstruction, cases outside, weakest relaxation), Block A Result |
| 2 | Result 4 overclaims the brief's "rigorous error bound" condition as met (Serious) | "met" → "met **as to exactness**, not yet as to the rigorous bound"; pointer to `## Next` item 2; empirical figure quoted instead | Result 4 |
| 3 | Chebyshev precision quoted as four different numbers (Concern) | Single statement "$\lesssim10^{-10}$ (worst of 12 points; $10^{-15}$ at moderate exponents)" everywhere | node C3, Result 2, Verification table (`C3-mutual`), Verification findings bullets 1–2, script docstring |
| 4 | "the vertical segment closes iff $p=q$" — what is shown is that the *constant-phase formula* closes iff $p=q$ (Concern) | "closes by the constant-phase mechanism iff $p=q$" | Block A Result, Result 1 |
| 5 | Per-arc quantity written with complex $\dd Z$; the script integrates $\operatorname{Im}(\overline G\,G'\,\dd Z)$ (Concern) | Rewritten as $\tfrac12\int\operatorname{Im}\bigl(\overline G\,G'(Z)\,Z'(t)\bigr)\dd t$, with a parenthesis saying why | 5 sites: node C2.3, Block A C1.2 ($J_k$), Block A vertical $p\ne q$ paragraph, Block A Result, Result 1. The sixth site the critic listed, in `### Scope of the exclusion`, no longer contains the expression after the rewrite of finding 1. The pointwise $\operatorname{Im}(\overline G\,G')=0$ of (A.5) is left as is — it carries no differential |
| 6 | `C3-ref-conv` passes vacuously if no point is resolvable; window $[4,16]$ admits $n^{-2}$–$n^{-4}$ (Concern/Minor) | `n_conv >= 1` required; window narrowed to $[6,11]$ | `codes/verify-j-closed-form.py`, `C3-ref-conv`; Verification table row; docstring |
| 7 | 045's box numbers: the "$n=40$ is good enough" claim was asserted, not shown (Concern) | New section, 18 points recomputed with (A.2), shift table, mechanism, explicit answer "no 045 conclusion moves" | `## Consequence for 045` |
| 8 | Ellipse row cited as "the ledger" (045 cites R7, a different row) (Minor) | Named **R2** and checked: $Z_4^{(s)}(\e^{\I\theta})=\cosh^2(\ln2\beta-\tfrac{\I\theta}2)$ has semi-axes $\tfrac12\cosh(2\ln2\beta)=\beta^2+\tfrac1{16\beta^2}=a$, $\tfrac12\sinh(2\ln2\beta)=b$; 045's "R7" flagged as a mis-citation | A2 |
| 9 | C1.2 cites only A2, C1.1 (Minor) | Added C1.3 (existence of $G$) and the orientation convention | node C1.2 |
| 10 | (B.5) "uniformly on $R$" — uniform in $Z$, not in $(p,q)$ (Minor) | Sentence aligned with the Commentary: uniform in $Z$, not in $(p,q)$, decay from $n\gtrsim\lvert p\rvert/2$ | Block B, after (B.5) |
| 11 | Result 4 inherits R48's conditionality (Minor); `J_boundary_cheb` docstring "integrated exactly" (Minor); undocumented closure tolerance (Minor); "non-analytic at the panel endpoint" should say square-root branch point (item 4 of the report) | One clause added on `Conditional(SL: R51, SL: R6/R10)`; docstring split between the exact cumulative step and the Gauss–Legendre product step; comment added on the $\sqrt J$ normalisation; branch-point mechanism and the $n^{-2(s+1)}$ rate written out | Result 4; script `J_boundary_cheb`, `C1-closure`; node C3.1, Verification findings bullet 1 |

**Not accepted as stated, and why.** The critic's displayed circle formula carries $+\tfrac1{2\I\alpha}\int\dots$;
with principal branches the sign is $-$ (verified to $10^{-16}$ at two $(p,q)$, see (A.9)), the
discrepancy being the Jacobian $\dd Z=-\dd w/w^2$, which the critique's formula dropped. *(This
sentence originally attributed the discrepancy to the branch of $w^{-p/2}$ under $w=1/Z$; the critic
of iteration 2 re-derived all branches and found no discrepancy — a branch mismatch would give a
phase $\e^{\pm\I\pi p/2}$, not a universal $-1$. Conclusion unchanged, reason corrected.)* The
formula's role — exhibiting the arc
contribution as a holomorphic integral of powers $\times{}_2F_1$ — is unaffected. (The characterisation
of that integral as "between generic endpoints" was itself corrected in the fix pass of iteration 2:
what is generic is the pair of exponents, not the endpoints.)

**New check.** `C2.3-reflect` (making 15), testing (A.8) on the circle, vertical and ellipse arcs;
break leg: the Schwarz function of a *different* arc, which must destroy the constancy. Two things
were learned writing it. (i) The double-precision arc points of `arcs()` are $\sim10^{-16}$ off the
exact curve, and the ellipse Schwarz function amplifies that to $\sim10^{-13}$ in $\overline G-G(S)$;
building the arc points and $a,b$ at mpmath precision sharpens the check from $5\times10^{-13}$ to
$6.3\times10^{-29}$. (ii) A first break leg that merely rescaled $S$ by $1+10^{-3}$ was too weak — at
some $(p,q)$ it left a spread of $10^{-7}$ — so it was replaced by the wrong-arc substitution
(min spread $5.9\times10^{-3}$ over the eight cases). Both were found by the check failing, not by
inspection. The re-framed scope statement is therefore
evidence-backed on its positive half; its negative half (no antiderivative for (A.9)) remains a
literature-grade statement, declared as such.

**Deferred, with the critic's agreement.** The large-exponent Laplace asymptotics of $J$ (report item
9) — recommended for the continuation, not required by this record's claims; added as `## Next`
item 4.

## Fix pass 2026-09-22 (critic iteration 2)

Critic report: `agent/reports/critic-047-iter2-20260922T184000.md` (node check; nodes 1, 2, 4, 5
hold, node 3 fails as worded, node 6 inherits it; 0 critical). Every finding and its resolution:

| # | Finding (severity) | Change made | Location |
|---|---|---|---|
| 1 | The stated obstruction is refutable: $\int_0^zw^{\lambda}{}_2F_1=\tfrac{z^{\lambda+1}}{\lambda+1}{}_3F_2$ at *any* endpoint, so "no antiderivative between endpoints outside $\{0,1,\infty\}$" is false. The real obstruction is the *second* power at generic exponents (Kampé de Fériet, single-series only under Euler's $\mu=c-a-b$) (major) | Obstruction re-stated at all six locations, with (A.10) (the counter-example) and (A.11) (the double series) added; the Euler condition traced to $p=0$ (after Pfaff) and $q=-1$ (circle, directly) | node C2.3, Block A (*The obstruction is (A.9)…*), Commentary bullet (A.9)–(A.11), Block A Result, `### Scope of the exclusion`, `## Proposed ledger row`, Result 1, script docstring (`C2.3-reflect`, *What is NOT verified*) |
| 2 | The exclusion is wider than its class: on $p=0$ and $q=0$ route (a) closes in ${}_2F_1$ + Appell $F_1$ (major, same node) | Exclusion restricted to **generic $(p,q)$** everywhere; the critic's derivation of the two lines recorded in Block A and as **node C2.4**, flagged *derived by the critic, not re-derived and not machine-checked here*, entered in `Open gaps:`; the machine check deferred as `## Next` item 5 (`C6-closed-lines`) — not written, outside the 30-minute box | new node C2.4, Block A (*The lines $p=0$ and $q=0$…*), `### Scope of the exclusion` (new first paragraph), Block A Result, Result 1, ledger row, `## Next` item 5, `Open gaps:` |
| 3 | (A.8) "on each arc" is false on the real segment with A3's boundary value from above (minor) | Qualifier "on the three curved arcs (on the real segment with $G(S(Z))$ the boundary value from below)" at all four locations, with the phase $\e^{-\I\pi p}$ named and the remark that (A.5) closes that arc anyway; the ellipse endpoint $\tfrac12+\I b$ on the root's cut flagged in (A.7) | node C2.3, Block A around (A.7)–(A.8), Commentary bullet (A.7)–(A.8), Block A Result, ledger row |
| 4 | The (A.9) sign is right but its stated *reason* is wrong: the critique dropped the Jacobian $\dd Z=-\dd w/w^2$; there is no branch discrepancy (minor) | Reason replaced in both places, with the branch re-derivation (all principal) summarised; the superseded attribution flagged rather than deleted | Block A after (A.9); `## Fix pass … (critic iteration 1)`, *Not accepted as stated* |
| 5 | The 18-point 045 shift table has no script: a numerical claim headed for the ledger with no reproducible source (major in consequence, mechanical) | New harness check **`C5-045-shift`** (making 16): the eighteen $(\beta,\alpha'P^2,\alpha'T)$ listed in the script, $F$ recomputed tile by tile with `j_integral(n=40)` and with `J_boundary_cheb(deg=600)`, one printed line per point, assertions $\max\lvert\text{shift}\rvert<10^{-6}$ and `cheb 600/900` $<10^{-13}$. The record's table is now that check's output | `codes/verify-j-closed-form.py` (`POINTS_045`, `contact_F`, check `C5-045-shift`), docstring, `## Consequence for 045`, `## Verification` |
| 6 | "exponentially suppressed" is wrong: the suppression is algebraic, $J\sim1/\lvert p\rvert$, because $R$ touches $\lvert Z\rvert=1$ (minor) | Corrected, with the mechanism ($\lvert Z\rvert^p=1$ on the circle arc) and the remark that the $10^{-30}$-scale $F$ values come from R48's prefactor; this strengthens the argument, since it explains why the suppressed tiles still supply half the shift | `## Consequence for 045`, first bullet of *Reading* |
| 7 | The contour-deformation "consequence" is over-stated: the endpoints $-1$, $\e^{\I\pi/3}$ stay on $\lvert Z\rvert=1$ (minor) | Downgraded to a lead at all three locations: the deformation improves the interior only, the $1/Z$ expansion is still marginal at both ends, "not examined here" | Block A (*Positive by-product, as a lead only*), `### Scope of the exclusion` (*Cases outside the class*), ledger row |
| 8 | Relaxation (i) "special to $\gamma=\alpha+1$" presumably means the contiguity $c=a+1$; in the record's notation $\gamma=\alpha+1$ reads $q=p+2$ (minor) | Written out: the incomplete Beta's ${}_2F_1(\alpha,1-\gamma;\alpha+1;Z)$ has $c=a+1$ for *every* $(p,q)$; the earlier phrasing named an unrelated line | `### Scope of the exclusion`, *Weakest relaxation* |
| 9 | Outside the critic's list: the Commentary calls $\tfrac1{4\I}[\lvert G\rvert^2]$ "a spurious real part"; it is imaginary (minor) | Corrected | Commentary bullet on (A.2) |
| 10 | The ledger row is not mirrored in the record (brief's premise; no such section existed) | New section `## Proposed ledger row` with the final wording after edits 1–7 above | `## Proposed ledger row` |

**Not done, and why.** The optional `C6-closed-lines` check of node C2.4 (the $p=0$/$q=0$ closed
forms against (A.2)) was not written: constructing the two Appell $F_1$ terms in the uniformiser
correctly is more than the remaining time box allows, and writing it quickly would produce a check
that tests the substitution rather than the closure. It is `## Next` item 5, and C2.4 carries the
"derived, not machine-checked" label in the tree, the Result, the Scope and the ledger row until it
is run. Nothing else in the record depends on C2.4.

**What did not change.** No number, no check outcome, no verdict: route (a) still does not close for
generic $(p,q)$, which is the case the objective needs. What changed is the *reason* for that
verdict and the *scope* it is stated on.

## Consequence for 045

*Added in the fix pass of 2026-09-22 (critic finding 4, "needs a small computation, not a
re-derivation"). Record 045 is **not edited**; this section states what the finding does to it.*

**Question.** Record 045's numbers come from `contact(s,t,u,beta,n)` of `codes/verify-kp-box.py`,
which evaluates the six $J$'s of R48 (3.0) with `j_integral` at its default $n=40$. Section
`## Verification` above shows that rule is only $O(n^{-3})$ accurate, $\sim2\times10^{-6}$ relative at
one moderate point. The assertion made there — "not a defect of 045's conclusions" — was not shown.
It is shown here.

**Method.** $F(s,t,u)$ of R48 recomputed at 045's own headline points with each $J$ evaluated (i) by
`j_integral` at $n=40$ (what 045 used) and (ii) by `J_boundary_cheb` at degree $600$ (this record's
representation (A.2)). The points are 045's, on the diagonal $t=u=T$ at $s=\alpha'P^2$ (its 045 A1
convention $P^2=s$): three **scan points** per $\beta$ at $\alpha'P^2=4$, $\tfrac{16}3$, $-10$,
the **superseded diagonal box** (Block 5,
$\alpha'T_{\max}$), and the **preliminary HS box** (Block 5, two-dimensional recomputation), the last
two at their per-$P^2$ values for each $\beta$. The Chebyshev value is itself checked for
self-consistency by re-running at degree $900$ (column `cheb 600/900`).

*In the harness since the fix pass of the critic's iteration 2:* the whole table is regenerated by
the check **`C5-045-shift`** of `codes/verify-j-closed-form.py`, which lists the eighteen
$(\beta,\alpha'P^2,\alpha'T)$ explicitly, prints one line per point, and asserts
$\max\lvert\text{shift}\rvert<10^{-6}$ and `cheb 600/900` $<10^{-13}$. The numbers below are that
check's output.

[Table of companion-project values removed.]

**Reading.** The worst shift over all eighteen points is $4.0\times10^{-7}$ relative, and it is
*negative everywhere*: the $n=40$ rule under-estimates $F$, uniformly.

Two features worth recording.

- **The shift depends on $\alpha'P^2$ and essentially not on $T$** — it moves by under $20\%$ while
  $\alpha'T$ runs from (companion value, not reproduced here) to (companion value, not reproduced here). The reason is visible in (3.0) of 045: for $t=u=T$ the six
  ordered permutations give three distinct exponent pairs, each twice, and only one of them,
  $(p,q)=(-\tfrac{\alpha'P^2}4,-\tfrac{\alpha'P^2}4)$, is $T$-independent; the other two carry
  $p$ or $q\simeq-\tfrac{\alpha'T}2$ and are strongly suppressed on $\lvert Z\rvert\ge1$. That one
  tile dominates the sum, and its own $n=40$ relative error ($-1.6\times10^{-7}$, $-2.0\times10^{-7}$,
  $-7.8\times10^{-9}$ at $\beta=\tfrac32$; $-8.3\times10^{-8}$, $-1.2\times10^{-7}$,
  $-1.4\times10^{-10}$ at $\beta=2$) accounts for about half the shift, the remainder coming from the
  suppressed large-$\lvert p\rvert$ tiles, whose relative error is larger but whose weight is small.
  Hence the anxiety behind the critic's concern — that the $n=40$ error grows with the exponents the
  box reaches — does **not** materialise: the exponents that grow with $T$ sit on the suppressed
  tiles. The suppression is **algebraic**, not exponential: $R$ touches $\lvert Z\rvert=1$ along the
  whole circle arc, where $\lvert Z\rvert^{p}=1$, so $J(p,q)\sim1/\lvert p\rvert$ at large
  $\lvert p\rvert$ (the (companion value, not reproduced here)-scale $F$ values in the table come from R48's prefactor
  $\beta^{8-\alpha'(s+2T)/2}$, not from the tiles). That is why those tiles can still supply about
  half the shift at every $T$ — which is what the per-tile numbers above show, and it strengthens
  rather than weakens the conclusion.
- **The large-exponent quadrature question of 045 is a separate one.** 045's *own* open item ("the
  quadrature order of `contact` at the tile exponents $\lvert p\rvert\simeq$ (companion value, not reproduced here) that the
  $\beta=\tfrac32$ grid reaches, where `C2-quad-deep` only certifies $\lvert p\rvert\le80$") is
  answered in the affirmative by this table at $\lvert p\rvert+\lvert q\rvert\approx$ (companion value, not reproduced here) — the
  Chebyshev route agrees with $n=40$ there to $4\times10^{-7}$ — and (A.2) removes the question
  altogether for any future evaluation, since it is accurate to $\lesssim10^{-10}$ at these exponents
  and $10^3$ times cheaper.

**Does any 045 conclusion move? No.** Every conclusion of 045 that uses `contact` is stated at the
$10^{-3}$ level (the tolerances $\eta\in\{10^{-2},10^{-3},10^{-4}\}$ defining the box), as a ratio of
two `contact` evaluations (the transverse ratio $\langle F\rangle_\theta/F(s,T,T)$, the factors
(companion value, not reproduced here), the shortfalls (companion value, not reproduced here)), or as a $T_{\max}$ read off a tail integral
whose integrand is smooth. A uniform $4\times10^{-7}$ relative bias changes $T_{\max}$ by
$O(10^{-7}/\ln\beta)$ in $\alpha'T$ — six orders below the quoted four digits — and cancels almost
exactly in every ratio. **What is *not* covered by this statement**, and was not covered before
either, is any comparison of an *absolute* value of $F$ with the sister project's machinery at the
$10^{-4}$ level or better; for those, `j_integral` at $n=40$ is not adequate and (A.2) should be used.

## Next

Continuation (sub-task 2), inheriting A1–A4, the harness, and the base point $G(-1)=0$:

1. Route (c′)/(b) merged: the series (B.5) in $w=v/u\le\tfrac13$. Compute the rectangle terms in
   closed form; reduce the triangle terms (expand $(u^2-1)^{-1/2}$ in $u^{-2}\le\tfrac14$, then
   $\int_0^1v^n(1-v^2)^{-1/2}(2+v)^M\dd v$ is an Appell $F_1$ at arguments $(-1,-\tfrac12)$, or an
   elementary function for integer $M$); bound the tail rigorously; test convergence at
   $\lvert p\rvert+\lvert q\rvert\sim200$ with the harness (`C4.1` checks). Failure mode: term count
   growing with $\lvert p\rvert+\lvert q\rvert$ faster than the quadrature cost it replaces.
2. Quantify the Chebyshev error bound of Result 2 (Bernstein ellipse of each arc's integrand) so
   the representation carries the "rigorous error bound" the brief asks for.
3. Route (d): one literature search on fundamental-domain-restricted Virasoro–Shapiro integrals;
   report "none found" if so.
4. Large-exponent asymptotics of $J$ by Laplace at the maximising boundary point of
   $\lvert Z\rvert^p\lvert1-Z\rvert^q$ on $R$ (a corner $-1$, $\tfrac12-a$, $\tfrac12+\I b$,
   $\e^{\I\pi/3}$, or an interior point of an arc). Two uses: it certifies the Chebyshev route at
   $\lvert p\rvert+\lvert q\rvert\gg100$, where no independent reference exists, and it says whether
   the six-term sum of R48 (3.0) suffers cancellation at the box's large virtualities. (Critic
   iteration 1, report item 9.)
5. *Done 2026-09-23* (brief `computator-047-c24-20260923T124500`): node C2.4 machine-checked,
   `C6-closed-lines` and three companion checks, (L.6), (L.12), 16 points to $1.4\times10^{-15}$.
   Its second use stands: exact anchors for the series route of item 1.
6. **Weakest remaining step (consolidation pass 2026-09-23).** The ellipse-arc obstruction rests on
   an argument, not a check: in the uniformiser the ellipse integrand is (powers of four linear
   factors)$\times{}_2F_1$ at the quadratic-rational argument $(1+x)^2/4x$, and Goursat's criterion
   (DLMF 15.8(iii)) gives a quadratic transformation only on the lines listed in Block A (*ellipse
   quarter*) — which contain every special locus found in this record except $q=-2$ — and, by the
   ramification argument added there (fix pass 2026-09-23), only the sub-family $p\in\{-1,-3\}$,
   $q\in\{-1,-3\}$ acts on the ellipse argument $(1+x)^2/4x$. Two things to do: (a) a
   sympy/mpmath check that the ellipse integrand at a generic $(p,q)$ is *not* reducible by any of
   DLMF's quadratic transformations, and that on $q=-1$ or $p=-1$ off the point $(-1,-1)$ it *is*,
   i.e. whether the ellipse arc closes there (it would be a new single-arc locus; whether
   $J$ closes on it is a separate question; $p+2q=-4$, proposed here before the node check, is
   expected to fail for the structural reason above and is no longer the test line); (b) rewrite the "same statement holds on the ellipse
   quarter" clause of C2.3 (iii) once (a) is run, since the two curved arcs obstruct for different
   reasons. Until then the ellipse claim in C2.3 stands on the weaker ground "one-dimensional
   integral of a ${}_2F_1$, no reduction found", which is all the verdict needs.

## Corrections 2026-09-23 (external review)

*Audit trail. Source: external review of the note (2026-09-23), items 1, 2, 3, 5, 8
(item 6 = node C2.4, next section; items 4, 7 handled elsewhere). Brief
`computator-047-corr-20260923T130000`; item 8 completed by the fix pass of the node check
(`computator-047-fix-20260923T142500`). The reviewer's equation numbers run ahead of the note's
`.aux`; items are mapped by content. Every item was **confirmed**. The corrected statements now live
in the claim tree (C2.1–C2.3), Block A, `## Result`, `### Scope of the exclusion` and `## Proposed
ledger row`; this section keeps the re-derivations (C.1)–(C.9), the counter-computations and the
numbers.*

| Item | Claim as received | Outcome | Now lives in |
|---|---|---|---|
| 1 | Criterion is $\arg(f\,\dd Z)$; circle closes on $2p+q=-4$; (f-circle) drops a $\tfrac12$; "exactly two arcs" false; phase not constant at $(0,0)$ | confirmed, (C.1); `C7-item1-circle-line` | C2.1–C2.3, Block A circle paragraph, Result table |
| 2 | Ellipse image straight only at $p=q=-1$ | confirmed, (C.2)–(C.3); `C7-item2-ellipse-point` | C2.3, Result table |
| 3 | Euler sign $\mu=a+b-c$; mixed Pfaff integrand; "exactly when" not established | confirmed and sharpened, (C.4)–(C.6); corollary $J(-1,-1)$ closed; `C7-item3-euler` | C2.3, Block A after (A.11), Scope |
| 5 | (A.9) is the first-form piece, not the swept area | confirmed, (C.7)–(C.8); `C7-item5-first-form` | (A.9) left-hand side |
| 8 | Range $\beta\ge\beta_{04}$; $1/(\lambda+1)$ missing in "(5.7)" | confirmed (range); confirmed (factor, in (A.11) — first disputed by reading "(5.7)" as (A.10), reversed in the fix pass), (C.9); `C7-item8-beta04` | A2, (A.11) |

### Item 1 — the criterion is $\arg(f\,\dd Z)$, and the circle closes on $2p+q=-4$

**Claim as received.** The constant-phase criterion must be on $\arg(f\,\dd Z)$, not $\arg f$; with it
the unit-circle arc also closes, on the line $2p+q=-4$; (f-circle) drops the $\tfrac12$ of
$\arg(1-Z)$; "exactly two arcs, and no more" is false; the phase is not constant at $(0,0)$.

**Re-derivation.** The swept area of an arc is $J_k=\tfrac12\int\operatorname{Im}(\overline G\,\dd G)$
with $\dd G=f\,\dd Z$. The image $G(\text{arc})$ is a straight segment iff the *direction* of
$\dd G$, i.e. $\arg(f\,\dd Z)$, is constant along the arc — $\arg f$ alone is the right criterion only
where $\dd Z$ itself has constant phase (the two straight arcs). If the segment's line passes through
$G(-1)=0$ the swept area is exactly $0$; otherwise it is $\tfrac12\operatorname{Im}\bigl(\overline{G(Z_0)}\,G(Z_1)\bigr)$
(triangle with the origin), elementary in the endpoint values. With A3:

- *Real segment*, $\dd Z=\dd x$: $\arg(f\,\dd Z)=\tfrac{\pi p}2$, constant for all $(p,q)$; the line
  passes through $G(-1)=0$: $J_{\text{real}}=0$ (A.5). Unchanged.
- *Vertical segment*, $\dd Z=\I\,\dd y$: $\arg(f\,\dd Z)=\tfrac{(p-q)\theta_0}2+\tfrac\pi2$, constant
  iff $p=q$. Unchanged (A.6).
- *Unit circle*, $Z=\e^{\I\theta}$, $\theta_0=\theta$, $\theta_1=\tfrac{\theta-\pi}2$:
  $$f=\bigl(2\sin\tfrac\theta2\bigr)^{q/2}\e^{\I[p\theta/2+q(\theta-\pi)/4]},\qquad
    \dd Z=\I\e^{\I\theta}\dd\theta,\qquad
    \arg(f\,\dd Z)=\theta\Bigl(\frac p2+\frac q4+1\Bigr)+\frac\pi2-\frac{\pi q}4 .\tag{C.1}$$
  Constant iff $\tfrac p2+\tfrac q4+1=0$, i.e. $\boxed{2p+q=-4}$. The record's Block A ("$C2$, unit
  circle") and the note's (f-circle) wrote the phase of $f$ as $[p\theta+q(\theta-\pi)]/2$, i.e.
  $q\theta_1$ instead of $q\theta_1/2$ — the $\tfrac12$ of $(1-Z)^{q/2}=\lvert1-Z\rvert^{q/2}\e^{\I q\theta_1/2}$
  was dropped, exactly as the reviewer says. On the line the arc starts at $-1$ where $G=0$, so the
  straight image passes through the origin and $J_{\text{circle}}=0$ **exactly**, for every $\beta$.
  At $(0,0)$ the slope is $1$: the phase is *not* constant (the earlier "for all $(p,q)\ne(0,0)$"
  was a statement about $\arg f$ and is withdrawn).
- *Ellipse quarter*: see item 2 — constant iff $p=q=-1$.

Control line $p+q=-2$ (the reviewer's first, rejected proposal): the slope $(2p+q+4)/4=(p+2)/4$
does not vanish on it except at $(-2,0)$, which is excluded by A4 (and lies on $2p+q=-4$ anyway).

**Numerical check** (scratch run, $\beta=\tfrac32$, `J_boundary_hyp` per arc; harness check
`C7-item1-circle-line`). Phase spread $\max_\theta\lvert u(\theta)-u(\theta_0)\rvert$ of the unit
phase $u=f\,\dd Z/\lvert f\,\dd Z\rvert$ and circle swept area relative to $J$:

| $(p,q)$ | on line | spread | $J_{\text{circle}}/J$ |
|---|---|---|---|
| $(-1,-2)$ | $2p+q=-4$ | $3\times10^{-17}$ | $4\times10^{-20}$ |
| $(-2.2,0.4)$ | $2p+q=-4$ | $2\times10^{-16}$ | $5\times10^{-17}$ |
| $(0,-4)$ | $2p+q=-4$ | $7\times10^{-17}$ | $2\times10^{-18}$ |
| $(-3.1,2.2)$, $(0.9,-5.8)$, $(-\tfrac43,-\tfrac43)$, $(-0.5,-3)$ | $2p+q=-4$ | $\le2\times10^{-16}$ | $\le4\times10^{-17}$ |
| $(-1,-1)$ | $p+q=-2$ | $0.47$ | $-0.13$ |
| $(-3.1,1.1)$, $(0.9,-2.9)$ | $p+q=-2$ | $0.51$, $1.26$ | $0.18$, $-0.26$ |
| $(0,0)$ | — | $1.62$ | $-0.23$ |

(Spreads at $10^{-16}$ are the double-precision arc points of `arcs()`; the harness check builds
the points in mpmath and reaches $10^{-28}$.) The reviewer's figures ($5\times10^{-26}$,
$10^{-33}$ on the line; $0.07$–$0.30$ off it) are reproduced in kind.

**Verdict: confirmed.** Corrected statement: *the image of an arc under $G$ is straight iff
$\arg(f\,\dd Z)$ is constant on it. This holds on the real segment for all $(p,q)$ (contribution
$0$), on the vertical segment iff $p=q$ (A.6), on the unit circle iff $2p+q=-4$ (contribution
exactly $0$, the image line passing through $G(-1)=0$), and on the ellipse quarter iff $p=q=-1$
(item 2; contribution $\tfrac12\operatorname{Im}(\overline{G(\tfrac12+\I b)}\,G(\tfrac12-a))$).*
"Closes exactly two arcs, and no more" is false as a statement about all $(p,q)$: at generic
$(p,q)$ the mechanism closes one arc (the real segment); on the three loci above it closes a second;
at $(-\tfrac43,-\tfrac43)$ (on $p=q$ and $2p+q=-4$) and at $(-1,-1)$ (on $p=q$) it closes three;
never all four ($p=q=-1$ and $2p+q=-4$ are incompatible). None of these loci closes $J$ by itself.

**For the objective.** In R48's tile exponents $(p,q)=\tfrac{\alpha'}4(x-y-z,\,y-x-z)$ the circle line
reads $\alpha'(x-y-3z)=-16$, a codimension-one hyperplane in the ordered Mandelstam triple; it does
not answer the objective. On $p=0$ and $q=0$ the circle arc is not on $2p+q=-4$ (except at $(0,-4)$
and, excluded, $(-2,0)$), so C2.4 needs its own circle reduction there — it has one, (L.2), (L.8).

### Item 2 — the ellipse image is straight only at $p=q=-1$

**Claim as received.** The ellipse image is straight only at $p=q=-1$.

**Re-derivation.** Use the confocal parametrisation of the ellipse of A2 (foci $0,1$):
$Z=\cosh^2\tfrac\zeta2$, $\zeta=\xi_0+\I\eta$, $\xi_0=2\ln2\beta$ fixed, so that $1-Z=-\sinh^2\tfrac\zeta2$
and $\dd Z=\sinh\tfrac\zeta2\cosh\tfrac\zeta2\,\I\,\dd\eta$ (this is R2's $Z_4^{(s)}(\e^{\I\theta})=\cosh^2(\ln2\beta-\tfrac{\I\theta}2)$
up to the orientation of $\eta$). On the quarter $\tfrac12-a\to\tfrac12+\I b$ the half-argument
$\tfrac\zeta2=\tfrac{\xi_0}2+\I\tfrac\eta2$ has $\tfrac\eta2\in[\tfrac\pi4,\tfrac\pi2]$, where
$\cosh\tfrac\zeta2$ and $\sinh\tfrac\zeta2$ lie in the closed first quadrant, so A3's principal
branches give $Z^{p/2}=\cosh^p\tfrac\zeta2$ and $(1-Z)^{q/2}=\e^{-\I\pi q/2}\sinh^q\tfrac\zeta2$
(with $\arg(1-Z)=2\arg\sinh\tfrac\zeta2-\pi\in[-\pi,0]$). Hence
$$f\,\dd Z=\I\e^{-\I\pi q/2}\cosh^{p+1}\tfrac\zeta2\,\sinh^{q+1}\tfrac\zeta2\,\dd\eta,\qquad
  \arg(f\,\dd Z)=(p+1)\arctan\bigl(\tanh\tfrac{\xi_0}2\tan\tfrac\eta2\bigr)
  +(q+1)\arctan\bigl(\coth\tfrac{\xi_0}2\tan\tfrac\eta2\bigr)+\text{const}.\tag{C.2}$$
Set $x=\tfrac{\xi_0}2>0$, $T=\tan\tfrac\eta2\in[1,\infty)$. The $\eta$-derivative of (C.2) is
$\tfrac12\sec^2\tfrac\eta2\bigl[(p+1)\tfrac{\tanh x}{1+\tanh^2x\,T^2}+(q+1)\tfrac{\coth x}{1+\coth^2x\,T^2}\bigr]$,
a rational function of $T$ that vanishes on $[1,\infty)$ iff it vanishes identically; $T=0$ and
$T\to\infty$ give $(p+1)\tanh x+(q+1)\coth x=0$ and $(p+1)\coth x+(q+1)\tanh x=0$, a homogeneous
system with determinant $\tanh^2x-\coth^2x<0$ for $x>0$. So $p+1=q+1=0$:
$\boxed{p=q=-1}$, and at that point $f\,\dd Z=\I\e^{\I\pi/2}\dd\eta=-\dd\eta$ is real. The image is
then the straight segment from $G(\tfrac12+\I b)$ to $G(\tfrac12-a)$, which does not pass through
$G(-1)=0$, so the arc contributes the triangle area
$$J_{\text{ellipse}}\big|_{p=q=-1}=\tfrac12\operatorname{Im}\bigl(\overline{G(\tfrac12+\I b)}\,G(\tfrac12-a)\bigr),\tag{C.3}$$
elementary in two endpoint values of $G$ (each a ${}_2F_1$). At $(-1,-1)$ the vertical segment
closes too ($p=q$) and the circle is on $q=-1$, where item 3 shows the circle piece is a single
${}_3F_2$ — so $J(-1,-1)$ is a closed form (see item 3).

**Numerical check** ($\beta=\tfrac32$; harness `C7-item2-ellipse-point`): unit-phase spread of
$f\,\dd Z$ on the ellipse quarter, and the swept area against (C.3):

| $(p,q)$ | spread | $J_{\text{ellipse}}$ | (C.3) | rel. diff. |
|---|---|---|---|---|
| $(-1,-1)$ | $1.5\times10^{-16}$ | $0.3412378$ | $0.3412378$ | $<10^{-15}$ |
| $(-1,-1.3)$ | $0.18$ | $0.2275$ | $0.2586$ | $0.14$ |
| $(-0.7,-1)$ | $0.24$ | $0.4570$ | $0.3893$ | $0.15$ |
| $(-2.4,-2.4)$ | $1.67$ | $-0.0184$ | $0.0182$ | $2.0$ |
| $(0,0)$ | $1.30$ | $2.3088$ | $0.8642$ | $0.63$ |

**Verdict: confirmed.** In R48's variables $p=q=-1$ is the line $x-y-z=y-x-z=-4/\alpha'$, i.e. $x=y$,
$z=4/\alpha'$ (orchestrator fix 2026-09-23: $z=x+4/\alpha'$ before) — codimension two, no bearing on the objective.

### Item 3 — Euler absorption: sign, the mixed Pfaff integrand, and "exactly when"

**Claim as received.** (5.9) [= `eq:euler-condition`, (A.11)'s condition] has the wrong sign:
absorption iff $\mu=A+B-C$; the Pfaff integrand at note l. 803–804 mixes two Euler representatives;
the two errors compensate at $p=0$, so "exactly when" (l. 794) is not established.

**Re-derivation.** *(i) Absorption.* Euler's transformation
${}_2F_1(A,B;C;w)=(1-w)^{C-A-B}{}_2F_1(C-A,C-B;C;w)$ rearranges to
$$(1-w)^{A+B-C}\,{}_2F_1(A,B;C;w)={}_2F_1(C-A,C-B;C;w),\tag{C.4}$$
so $(1-w)^{\mu}{}_2F_1(A,B;C;w)$ is a single ${}_2F_1$ (with no power left) iff $\mu=A+B-C$, or
trivially $\mu=0$. With $\mu=C-A-B$ the product is $(1-w)^{2(C-A-B)}{}_2F_1(C-A,C-B;C;w)$, nothing
absorbed. The record's (A.11) sentence and the note's `eq:euler-condition` state $\mu=C-A-B$:
**wrong sign, confirmed.**

*(ii) The Pfaff forms of the (A.9) integrand* $I(w)\,\dd w=w^{-\gamma}(w-1)^{\gamma-1}{}_2F_1(\alpha,1-\gamma;\alpha+1;w)\,\dd w$
under $x=w/(w-1)$ ($w=-x/(1-x)$, $1-w=(1-x)^{-1}$, $\dd w=-\dd x/(1-x)^2$). For $w=\e^{-\I\theta}$,
$\theta\in(\tfrac\pi3,\pi)$, one finds $x=\e^{\I(\pi-\theta)/2}/(2\sin\tfrac\theta2)$: $x$ in the
upper half-plane with $\tfrac12\le\lvert x\rvert\le1$, $1-x$ in the lower half-plane, and with all
branches principal $w^{-\gamma}=\e^{\I\pi\gamma}x^{-\gamma}(1-x)^{\gamma}$,
$(w-1)^{\gamma-1}=\e^{-\I\pi(\gamma-1)}(1-x)^{1-\gamma}$ (the constant phases combine with the
Jacobian's $-1$ to $+1$). The two Pfaff transformations of the ${}_2F_1$ give two representatives:
$$\begin{aligned}
 \text{(A)}\quad {}_2F_1(\alpha,1-\gamma;\alpha+1;w)&=(1-w)^{-\alpha}{}_2F_1(\alpha,\alpha+\gamma;\alpha+1;x)
 &&\Rightarrow\ I\,\dd w=x^{-\gamma}(1-x)^{\alpha-1}{}_2F_1(\alpha,\alpha+\gamma;\alpha+1;x)\,\dd x,\\
 \text{(B)}\quad {}_2F_1(\alpha,1-\gamma;\alpha+1;w)&=(1-w)^{\gamma-1}{}_2F_1(1,1-\gamma;\alpha+1;x)
 &&\Rightarrow\ I\,\dd w=x^{-\gamma}(1-x)^{-\gamma}{}_2F_1(1,1-\gamma;\alpha+1;x)\,\dd x.
\end{aligned}\tag{C.5}$$
The note (and the record after (A.11)) wrote $x^{-\gamma}(1-x)^{-\gamma}{}_2F_1(\alpha,\alpha+\gamma;\alpha+1;x)$:
the powers of (B) with the ${}_2F_1$ of (A). **Mixed representatives, confirmed** (the two are
related by Euler on the $x$ side, so the mixed form is neither). *(iii) The compensation.* With the
correct sign (C.4) on (B): $-\gamma=1+(1-\gamma)-(\alpha+1)\iff\alpha=1\iff p=0$. On (A):
$\alpha-1=\alpha+(\alpha+\gamma)-(\alpha+1)\iff\gamma=0\iff q=-2$. Directly on $I$ (no Pfaff, power
$(1-w)^{\gamma-1}$ up to a constant phase): $\gamma-1=\alpha+(1-\gamma)-(\alpha+1)\iff\gamma=\tfrac12\iff q=-1$.
With the *wrong* sign on the *mixed* form: $-\gamma=(\alpha+1)-\alpha-(\alpha+\gamma)\iff\alpha=1\iff p=0$
— the same line, by two compensating errors, exactly as the reviewer says. (The record's $q=-1$
statement used the correct sign tacitly; it stands.)

*(iv) "Exactly when".* The note's l. 794 says the double series (A.11) collapses to a single
hypergeometric series *exactly when* Euler absorbs the power. Absorption is sufficient; it is not
necessary, and three counter-examples are at hand: (a) each Pfaff representative absorbs on its own
line — $p=0$ (B), $q=-2$ (A), $q=-1$ (direct) — so the single-series set is at least the union, not
one line; (b) on $p+q=-4$, i.e. $\gamma=-\alpha$, the ${}_2F_1$ is elementary,
${}_2F_1(\alpha,1+\alpha;\alpha+1;w)=(1-w)^{-\alpha}$, $G=\alpha^{-1}(Z/(1-Z))^{\alpha}+\text{const}$,
and every arc integrand is algebraic (circle and vertical: incomplete Beta, a single ${}_2F_1$; the
ellipse: four linear factors in the uniformiser, a Lauricella $F_D^{(3)}$, *outside* the brief's
Appell class), with $\mu$ absorbing nothing; (c) at $q=-1$ the circle piece is explicitly a
${}_3F_2$ at the endpoint: with $\gamma=\tfrac12$, Euler on $I$ gives
$I\,\dd w=\I\,w^{-1/2}{}_2F_1(1,\alpha+\tfrac12;\alpha+1;w)\,\dd w$ (the phase $\I$ from
$(w-1)^{-1/2}(1-w)^{1/2}$ on the lower arc), and by (A.10)
$$\int I\,\dd w=2\I\,w^{1/2}\,{}_3F_2\bigl(1,\alpha+\tfrac12,\tfrac12;\alpha+1,\tfrac32;w\bigr)\Big|_{-1}^{\e^{-\I\pi/3}},\tag{C.6}$$
the value at $-1$ taken from below ($w^{1/2}=-\I$); both endpoints lie on $\lvert w\rvert=1$, where the
${}_3F_2$ series converges because its parameter excess is
$(\alpha+1+\tfrac32)-(1+\alpha+\tfrac12+\tfrac12)=\tfrac12>0$ (absolutely, for every $\alpha$), so the
endpoint values are values of the series itself, not continuations. **Corollary (new): $J(-1,-1)$ is a closed
form** — real segment $0$, vertical segment (A.6) ($p=q$), ellipse (C.3), circle
$=\operatorname{Re}$ of (A.9) with (C.6) — in ${}_2F_1$ endpoint values and one ${}_3F_2$.

**Numerical checks** (scratch; harness `C7-item3-euler`): (C.4) at three random complex
$(A,B,C,w)$: residual $\le2\times10^{-31}$ with $\mu=A+B-C$, $\ge1.6$ with $\mu=C-A-B$. (C.5): the
ratio $I\,\dd w/(\text{form}\,\dd x)$ is $1$ for (A) and (B) and varies along the arc for the mixed
form. $G$ elementary on $p+q=-4$ at $p\in\{-1.3,0.7,-2.6\}$: $G-\alpha^{-1}(Z/(1-Z))^{\alpha}$
constant over three points to $\le4\times10^{-17}$. (C.6) against mpmath quadrature of $I$ along the
arc at $p\in\{-3.4,1.7,0.4\}$, $q=-1$: $\lvert\Delta\rvert\le3.2\times10^{-17}$ on values of size
$1.4$–$2.6$.

**Verdict: confirmed, and sharpened.** Corrected statements: absorption iff $\mu=A+B-C$ (C.4);
the Pfaff integrand is (C.5)(A) or (B), not their mixture; "exactly when" is **false**, replaced by:
*Euler absorption is a sufficient condition for the circle integrand to reduce to a single
hypergeometric series; it holds on $p=0$, $q=-1$, $q=-2$ (one per representative), and the
degenerate line $p+q=-4$ (elementary $G$) closes it too. No necessary condition is established.*
The lines $q=-1$, $q=-2$, $p+q=-4$ close the **circle arc only**; the closure of $J$ on them is not
claimed (the ellipse piece is Lauricella at best on $p+q=-4$, and untouched on $q=-1$, $q=-2$
except at $(-1,-1)$).

### Item 5 — (A.9) is the first-form piece, not the swept area

**Claim as received.** Eq. (5.5) [= `eq:circle-reduced`, (A.9)], labelled $J_{\text{circle}}$, is
the first-form piece; it differs from the circle-arc contribution by an imaginary term.

**Re-derivation.** (A.9) was obtained by substituting $w=1/Z$ in $\tfrac1{2\I}\int_{\text{circle}}f\,\overline G\,\dd Z$,
the per-arc piece of the *first* form of (A.2). By the Commentary on (A.2),
$\overline G\,\dd G=\tfrac12\dd\lvert G\rvert^2+\I\operatorname{Im}(\overline G\,\dd G)$, so on any arc
$$\frac1{2\I}\int f\,\overline G\,\dd Z=\underbrace{\frac12\int\operatorname{Im}(\overline G\,\dd G)}_{J_k\ \text{(swept area, real)}}
 +\frac1{4\I}\bigl[\lvert G\rvert^2\bigr]_{\text{start}}^{\text{end}} .\tag{C.7}$$
On the circle the start is $-1$ with $G(-1)=0$, so
$$\text{(A.9)}=J_{\text{circle}}-\frac\I4\,\lvert G(\e^{\I\pi/3})\rvert^2,\tag{C.8}$$
and the swept area is $J_{\text{circle}}=\operatorname{Re}\,\text{(A.9)}$. The label
"$J_{\text{circle}}$" on (A.9) is therefore wrong by the purely imaginary term (C.8); the bracket
$[\lvert G\rvert^2]$ telescopes around the loop, so nothing in $J$ is affected.

**Numerical check** ($\beta=\tfrac32$; harness `C7-item5-first-form`): (A.9)'s right-hand side by
mpmath quadrature along $w=\e^{-\I\theta}$ versus the swept area of `J_boundary_hyp` and
$-\tfrac\I4\lvert G(\e^{\I\pi/3})\rvert^2$:

| $(p,q)$ | (A.9) | $J_{\text{circle}}$ | (A.9) $-J_{\text{circle}}$ | $-\tfrac\I4\lvert G_1\rvert^2$ |
|---|---|---|---|---|
| $(-3.4,2.1)$ | $0.368200282745-3.12795385186\,\I$ | $0.3682002827$ | $2\times10^{-16}-3.12795\,\I$ | $-3.12795\,\I$ |
| $(1.7,-5.3)$ | $-0.0372756098281-0.103871575499\,\I$ | $-0.0372756098$ | $3\times10^{-18}-0.103872\,\I$ | $-0.103872\,\I$ |

(This also re-verifies (A.9) itself, sign included, at the two points quoted in the fix pass of
iteration 1 — previously asserted in prose, now a harness check.)

**Verdict: confirmed.** (A.9) equals $J_{\text{circle}}-\tfrac\I4\lvert G(\e^{\I\pi/3})\rvert^2$;
the circle's swept area is its real part. The left-hand side of (A.9) is now written as the first-form piece.

### Item 8 — region condition $\beta\ge\beta_{04}$; the $1/(\lambda+1)$ of (A.11)

**Claim as received.** The region condition is $\beta\ge\beta_{04}$ ($\beta_{04}=$ (companion value, not reproduced here)), not
$\beta\ge\tfrac32$; a $1/(\lambda+1)$ is missing in "(5.7)". The equation numbers of the review
differ from the note's; "(5.7)" is `eq:one-power` (A.10) or `eq:two-powers` (A.11), and
the content decides: it is (A.11).

**Re-derivation.** The four-arc description of $R$ (A2) needs the ellipse to meet the real axis
left of $-1$, $\tfrac12-a\le-1\iff a\ge\tfrac32$, and the vertical line above $\e^{\I\pi/3}$,
$b\ge\tfrac{\sqrt3}2$. With $a=\beta^2+\tfrac1{16\beta^2}$: $a\ge\tfrac32\iff16\beta^4-24\beta^2+1\ge0
\iff\beta^2\ge$ (companion value, not reproduced here), i.e.
$\boxed{\beta\ge\beta_{04}}$ with $\beta_{04}=$ (companion value, not reproduced here) (sympy: the positive root of
$a=\tfrac32$ agrees with $\beta_{04}$, difference simplifies to $0$). At
$\beta_{04}$, $b=$ (companion value, not reproduced here)$>\tfrac{\sqrt3}2$, so the second condition is implied. So $\beta\ge\tfrac32$
(A2, and note l. 332) is sufficient, not necessary: the correct range is $\beta\ge\beta_{04}$, the
same threshold as R48's "declared section with $\beta>\beta_{04}$" — this is the threshold stated in R48, at which the ellipse passes through $-1$ and the $\mathcal V_{0,4}$ region first covers
the fundamental-domain corner. Nothing in Block A or B used $\tfrac32$ beyond the test values
$\beta\in\{\tfrac32,2\}$. **Confirmed**; A2 is annotated (statement of the range only; no result
changes).

The $1/(\lambda+1)$. Term by term, with $(1-w)^{\mu}=\sum_m\tfrac{(-\mu)_m}{m!}w^m$ and
${}_2F_1=\sum_n\tfrac{(a)_n(b)_n}{(c)_n n!}w^n$,
$$\int_0^zw^{\lambda+m+n}\dd w=\frac{z^{\lambda+1+m+n}}{\lambda+1+m+n},\qquad
 \frac1{\lambda+1+k}=\frac1{\lambda+1}\,\frac{(\lambda+1)_k}{(\lambda+2)_k}\quad(k=m+n),\tag{C.9}$$
so the double series of (A.11) carries the prefactor $\tfrac{z^{\lambda+1}}{\lambda+1}$, exactly as
(A.10) does; at $\mu=0$ only $m=0$ survives and (A.11) *is* (A.10). The record's (A.11) and the
note's `eq:two-powers` were written with $z^{\lambda+1}$ alone: the two adjacent equations disagreed
by the factor $\lambda+1$ at $\mu=0$. The corrections pass of 2026-09-23 read "(5.7)" as (A.10),
found the factor present there, and declared the item **not reproducible** — that checked the wrong
equation; the remark is correct as stated. (A.11) is corrected in Block A; the (A.11) leg
of `C7-item8-beta04` evaluates the double series (with and without the prefactor) against quadrature
of $w^{\lambda}(1-w)^{\mu}{}_2F_1(a,b;c;w)$ at $(\lambda,\mu,z)=(0.3,0.6,0.4+0.2\I)$ and
$(0.85,1.7,-0.3+0.35\I)$ (both with $\lambda>0$, so that the quadrature reference has no endpoint singularity), and its $\mu=0$ specialisation against (A.10) — numbers in the fix-pass
table. No consequence for the obstruction (an overall constant leaves the double-series structure
untouched), for any number of Blocks A–B (nothing was ever evaluated through (A.11)), or for the
Euler condition.

**Verdict: confirmed (range), confirmed (factor; in (A.11), not (A.10)).** A2 now states the range
$\beta\ge\beta_{04}$; (A.11) carries the prefactor (an identity cited by C2.3 for its *structure*; C2.3 unchanged).

### What changed in R50 and in the scope of the exclusion

Five edits to R50, all incorporated in `## Proposed ledger row`: (i) the constant-phase criterion
$\arg(f\,\mathrm dZ)$ with the loci circle $2p+q=-4$ (contribution $0$) and ellipse $p=q=-1$;
(ii) Euler absorption "single-series when" (sufficient) with $\mu=a+b-c$ on $p=0$, $q=-1$, $q=-2$
and the degenerate $p+q=-4$, circle arc only; (iii) $J(-1,-1)$ closes in ${}_2F_1$ and one ${}_3F_2$;
(iv) C2.4 "not machine-checked" → verified by `C6-closed-lines` (16 points, $1.4\times10^{-15}$), with
its two sharpenings (circle elementary on $q=0$; $c-\I0$ on the $q=0$ ellipse term); (v) the Kampé de
Fériet antiderivative quoted with its prefactor $z^{\lambda+1}/(\lambda+1)$. The range is
$\beta\ge\beta_{04}$ (A2), as R48 already states. Scope: "generic" spelled out in
`### Scope of the exclusion`. Not changed: (A.2), (A.5)–(A.10) as identities, (A.11) up to the
prefactor, every number of Blocks A–B, the Chebyshev evaluation, the 045 shift table; R50 never
relied on "exactly two arcs".

### Note-side edits implied by the corrections (for the next revision of `j-boundary-representation.tex`; the note is not edited here)

- `eq:two-powers` (note l. 782–788): insert the prefactor $\tfrac1{\lambda+1}$ in front of the double
  series, as in (A.11) corrected; the sentence after it may add "at $\mu=0$ this reduces to
  `eq:one-power`". (Item 8, second half.)
- `eq:euler-condition`: sign $\mu=a+b-c$, not $c-a-b$; the mixed integrand after Pfaff replaced by
  the two representatives (C.5)(A), (B); "exactly when" → "when" (sufficient), with the lines
  $p=0$, $q=-1$, $q=-2$ and the degenerate $p+q=-4$. (Item 3 — already listed there.)
- Note l. 332: the range $\beta\ge\tfrac32$ → $\beta\ge\beta_{04}$ ($\beta_{04}=$ (companion value, not reproduced here);
  $\tfrac32$ stays as the test value). (Item 8, first half.)
- The constant-phase criterion is $\arg(f\,\dd Z)$; the circle arc vanishes on $2p+q=-4$, the
  ellipse is straight only at $p=q=-1$; the first-form circle piece is (C.8). (Items 1, 2, 5.)
- Corollary $J(-1,-1)$ in ${}_2F_1$ and one ${}_3F_2$; the ${}_3F_2$ of (C.6) converges on
  $\lvert w\rvert=1$ (parameter excess $\tfrac12$). (Item 3, corollary.)

## The lines $p=0$ and $q=0$ with coefficients (2026-09-23)

Brief `computator-047-c24-20260923T124500` (external review, item 6, node C2.4). Conventions
A1–A4 and the `## Corrections 2026-09-23` inherited verbatim; $c:=4\beta^2$ ($\ge9$), so $16\beta^2=4c$,
$a=\tfrac{c^2+1}{4c}$, $b=\tfrac{c^2-1}{4c}$. Companion check: `C6-closed-lines` in
`codes/verify-j-closed-form.py`.

Skeleton (first checkpoint) — which piece closes on each arc, and in what:

| Arc | $p=0$ ($f=(1-Z)^{q/2}$, $G$ elementary) | $q=0$ ($f=Z^{p/2}$, $G$ elementary) |
|---|---|---|
| real segment | $0$ (A.5) | $0$ (A.5) |
| unit circle ($\bar Z=1/Z$) | incomplete Beta $B_Z(-\tfrac q2,\,q+2)$ between $-1$ and $\e^{\I\pi/3}$, plus endpoint values of $G$ | **elementary**: $\int Z^{-1}\dd Z=-\tfrac{2\pi\I}3$, plus endpoint values of $G$ (degenerate case of the incomplete Beta) |
| vertical segment ($\bar Z=1-Z$) | $B_Z(\tfrac q2+2,\,\tfrac q2+1)$ between $\e^{\I\pi/3}$ and $\tfrac12+\I b$ | $B_Z(\tfrac p2+1,\,\tfrac p2+2)$, same endpoints |
| ellipse quarter (uniformiser $w=\e^{\I t}$, $Z=\tfrac{(cw+1)^2}{4cw}$) | two Appell $F_1(a;-q-1,-q-2;a+1;\,cw,\,w/c)$, $a\in\{-q-2,-q-1\}$, endpoints $w=\I,-1$ | two Appell $F_1(a;-p-1,-p-2;a+1;\,-cw,\,-w/c)$, $a\in\{-p-2,-p-1\}$; at $w=-1$ the first argument sits on the cut $[1,\infty)$ and is taken as $c-\I0$ |

Per line the endpoint values of $G$ cancel around the loop, so the summed formula has only the
three arc integrals. The two lines are **not** related by a symmetry of $R$ (see *Asymmetry*
below). Steps: (1) the $p=0$ reduction and the three arc integrals; (2) the $q=0$ reduction;
(3) the branch bookkeeping in the uniformiser; (4) the $q\to0$ limit and the area; (5) the
check table; (6) verdict on C2.4.

\subsection*{Setup}

A1–A4. $f=Z^{p/2}(1-Z)^{q/2}$, $\alpha=\tfrac p2+1$, $\gamma=\tfrac q2+1$, $G(Z)=\int_{-1}^Zf$ (C1.3),
$J=\sum_kJ_k$, $J_k=\tfrac12\operatorname{Im}\int_k\overline G\,\dd G$ (A.2), arcs in the order and
orientation of Block A: circle $Z_1=-1\to Z_2=\e^{\I\pi/3}$, vertical $Z_2\to Z_3=\tfrac12+\I b$,
ellipse $Z_3\to Z_4=\tfrac12-a$, real $Z_4\to Z_1$. Incomplete Beta as in (A.3),
$B_Z(\alpha',\gamma'):=\tfrac{Z^{\alpha'}}{\alpha'}\,{}_2F_1(\alpha',1-\gamma';\alpha'+1;Z)$, principal
${}_2F_1$, $Z^{\alpha'}$ with $\arg Z\in[0,\pi]$ (boundary value from above on the negative axis), so that
$\dd B_Z/\dd Z=Z^{\alpha'-1}(1-Z)^{\gamma'-1}$ on the closed upper half-plane minus $\{0,1\}$ with
principal $(1-Z)^{\gamma'-1}$. All other powers are principal. Uniformiser of the ellipse (R2, A2):
$$Z=\frac{(cw+1)^2}{4cw}=\tfrac12+\beta^2w+\frac1{16\beta^2w},\qquad w=\e^{\I t},\ t:\tfrac\pi2\to\pi,\ \text{i.e. }w:\I\to-1,\tag{L.0}$$
on which $1-Z=-\tfrac{(cw-1)^2}{4cw}$, $\bar Z=\tfrac{(w+c)^2}{4cw}$, $1-\bar Z=-\tfrac{(c-w)^2}{4cw}$,
$\dd Z=\tfrac{(cw-1)(cw+1)}{4cw^2}\dd w$; $\arg w=t\in[\tfrac\pi2,\pi]$, $w^{s}$ taken with that argument
($w=-1$: $\e^{\I\pi s}$). Appell $F_1$ with third parameter $a+1$, through its Euler integral
(DLMF 16.15.1, $c'=a+1$):
$$\Phi_a(w;b_1,b_2;x,y):=\frac{w^a}{a}F_1\bigl(a;b_1,b_2;a+1;x,y\bigr)
 =\int_0^w s^{a-1}\Bigl(1-\frac xw s\Bigr)^{-b_1}\Bigl(1-\frac yw s\Bigr)^{-b_2}\dd s\quad(\operatorname{Re}a>0),\tag{L.F}$$
continued analytically in $a$ (simple poles at $a\in\mathbb Z_{\le0}$, which cancel in every
endpoint difference $[\Phi_a]_{w_0}^{w_1}$ below) and in $x$ off $[1,\infty)$. The single-sum form
used as the second evaluator,
$F_1(a;b_1,b_2;a+1;x,y)=\sum_{m\ge0}\frac{(a)_m(b_2)_m}{(a+1)_m\,m!}y^m\,{}_2F_1(a+m,b_1;a+m+1;x)$,
follows from (L.F) by expanding $(1-\tfrac yws)^{-b_2}$ (convergent for $\lvert y\rvert<1$; here
$\lvert y\rvert=1/c\le\tfrac19$).

\subsection*{Derivation}

*Step 1, the line $p=0$.* $f=(1-Z)^{q/2}$ and, for $\gamma\ne0$,
$$G(Z)=\frac{2^{\gamma}-(1-Z)^{\gamma}}{\gamma},\qquad
 \overline G\,\dd G=\frac{2^{\gamma}}{\gamma}\,\dd G-\frac1\gamma\,\overline{(1-Z)^{\gamma}}\,(1-Z)^{q/2}\dd Z
 =\frac{2^{\gamma}}{\gamma}\,\dd G-\frac1\gamma\,\lvert1-Z\rvert^{q}\,(1-\bar Z)\,\dd Z,\tag{L.1}$$
since $\overline{(1-Z)^{\gamma}}(1-Z)^{q/2}=\lvert1-Z\rvert^{q+1}\e^{-\I\theta_1}=\lvert1-Z\rvert^{q}(1-\bar Z)$.
The first term is exact, so per arc
$$J_k=\frac{2^{\gamma}}{2\gamma}\operatorname{Im}\bigl[G\bigr]_k-\frac1{2\gamma}\operatorname{Im}I_k,\qquad
 I_k:=\int_k\lvert1-Z\rvert^{q}(1-\bar Z)\,\dd Z,\qquad
 J(0,q)=-\frac1{2\gamma}\operatorname{Im}\sum_kI_k\tag{L.1$'$}$$
(the $[G]_k$ telescope around $\partial R$). On each arc $\lvert1-Z\rvert^{q}(1-\bar Z)$ is written
holomorphically through the Schwarz function (C2.3):

- *Circle*, $\bar Z=1/Z$: $\lvert1-Z\rvert^2=(1-Z)(1-1/Z)$ and, with $\theta_1=\tfrac{\theta-\pi}2$,
  $\arg(Z-1)-\arg Z=\theta_1+\pi-\theta=\tfrac{\pi-\theta}2\in[0,\tfrac\pi3]$, so the principal powers
  compose without a $2\pi$ defect: $(1-1/Z)^{q/2}=\e^{\I\pi q/2}Z^{-q/2}(1-Z)^{q/2}$, hence
  $$\lvert1-Z\rvert^{q}(1-\bar Z)\,\dd Z=-\e^{\I\pi q/2}Z^{-q/2-1}(1-Z)^{q+1}\dd Z,\qquad
   I_{\rm circle}=-\e^{\I\pi q/2}\Bigl[B_Z\bigl(-\tfrac q2,\ q+2\bigr)\Bigr]_{-1}^{\e^{\I\pi/3}}.\tag{L.2}$$
- *Vertical*, $\bar Z=1-Z$, $\theta_1=-\theta_0$: $\lvert1-Z\rvert^{q}=Z^{q/2}(1-Z)^{q/2}$ exactly, so
  $$\lvert1-Z\rvert^{q}(1-\bar Z)\,\dd Z=Z^{q/2+1}(1-Z)^{q/2}\dd Z,\qquad
   I_{\rm vert}=\Bigl[B_Z\bigl(\tfrac q2+2,\ \tfrac q2+1\bigr)\Bigr]_{\e^{\I\pi/3}}^{\frac12+\I b}.\tag{L.3}$$
- *Ellipse*, (L.0). Put $A=cw-1$, $B=c-w$; on $\lvert w\rvert=1$, $\bar A=B/w$, so
  $\lvert1-Z\rvert=\tfrac{\lvert A\rvert^2}{4c}=\tfrac{AB}{4cw}$ (a positive real written as a
  rational function of $w$), and the principal arguments satisfy $\arg A+\arg B-\arg w=0$ exactly on
  the arc ($\arg A\in(\tfrac\pi2,\pi]$, $\arg B=t-\arg A$, checked at both ends). Hence
  $$\lvert1-Z\rvert^{q}(1-\bar Z)\,\dd Z=-(4c)^{-q-2}A^{q+1}B^{q+2}(cw+1)\,w^{-q-3}\dd w.\tag{L.4}$$
  Branches into Appell form: $1-cw=-A$ has $\arg\in(-\tfrac\pi2,0]$, so $A^{q+1}=\e^{\I\pi(q+1)}(1-cw)^{q+1}$
  (principal both); $B^{q+2}=c^{q+2}(1-w/c)^{q+2}$ with $\lvert w/c\rvert\le\tfrac19$. Then
  $-(4c)^{-q-2}c^{q+2}\e^{\I\pi(q+1)}=4^{-q-2}\e^{\I\pi q}$ and $(cw+1)w^{-q-3}=w^{-q-3}+c\,w^{-q-2}$:
  $$I_{\rm ell}=4^{-q-2}\e^{\I\pi q}\Bigl[\Phi_{-q-2}(w)+c\,\Phi_{-q-1}(w)\Bigr]_{w=\I}^{w=-1},\qquad
   \Phi_a(w)=\frac{w^a}{a}F_1\bigl(a;\,-q-1,\,-q-2;\,a+1;\ cw,\ \tfrac wc\bigr).\tag{L.5}$$
  The endpoint difference of the straight-path integrals (L.F) equals the arc integral: for
  $\operatorname{Re}a>0$ by Cauchy on the quarter disc $\{\operatorname{Re}w\le0,\operatorname{Im}w\ge0,\lvert w\rvert\le1\}$
  (the integrand is holomorphic inside; $(1-cw)^{q+1}$ and $(1-w/c)^{q+2}$ have their cuts on
  $[1/c,\infty)$ and $[c,\infty)$, outside; $w^{a-1}$ carries the boundary value from above on the
  negative axis, where the path $0\to-1$ lies), and for all $a$ by analytic continuation, both sides
  being meromorphic in $a$ with the same poles. The first argument $x=cw\in\{c\I,-c\}$ is off the cut of
  $F_1$; $\lvert x\rvert=c$ ($c\ge9$ at $\beta\ge\tfrac32$; lower bound on $c$ over the whole range: (companion value, not reproduced here)) requires the continuation of $F_1$ outside the unit polydisc.
- *Real*: $x\in[\tfrac12-a,-1]$, $(1-x)^{q+1}\dd x$ and $G(x)$ real: $J_{\rm real}=0$ (A.5).

Summed, with the $[G]_k$ terms telescoping:
$$\boxed{\ J(0,q)=-\frac{1}{q+2}\operatorname{Im}\Bigl\{-\e^{\I\pi q/2}\Bigl[B_Z\bigl(-\tfrac q2,q+2\bigr)\Bigr]_{-1}^{\e^{\I\pi/3}}
 +\Bigl[B_Z\bigl(\tfrac q2+2,\tfrac q2+1\bigr)\Bigr]_{\e^{\I\pi/3}}^{\frac12+\I b}
 +4^{-q-2}\e^{\I\pi q}\Bigl[\Phi_{-q-2}+c\,\Phi_{-q-1}\Bigr]_{\I}^{-1}\Bigr\}\ }\tag{L.6}$$
valid for $q\notin\{0,-2\}\cup\{-4,-6,-8,\dots\}\cup\mathbb Z_{\ge-1}$ as written (normalisation
poles of $B_Z$: the circle term $B_Z(-\tfrac q2,\cdot)$ at $q\in\{0,2,4,\dots\}\subset\mathbb Z_{\ge-1}$,
the vertical term $B_Z(\tfrac q2+2,\cdot)$ at $\tfrac q2+2\in\mathbb Z_{\le0}$, i.e. $q\in\{-4,-6,-8,\dots\}$;
the pole of $1/\gamma$ at $-2$; $F_1$ with $a+1\in\mathbb Z_{\le0}$ for integer $q\ge-1$), all
removable — $J$ is entire in $q$ (045 C1) — and extended by continuity.

*Step 2, the line $q=0$.* $f=Z^{p/2}$ and, for $\alpha\ne0$, $G(Z)=\tfrac{Z^{\alpha}-\e^{\I\pi\alpha}}{\alpha}$
($(-1)^{\alpha}=\e^{\I\pi\alpha}$ from above). With $\overline{Z^{\alpha}}Z^{p/2}=\lvert Z\rvert^{p+1}\e^{-\I\theta_0}=\lvert Z\rvert^{p}\bar Z$,
$$\overline G\,\dd G=\frac1\alpha\lvert Z\rvert^{p}\bar Z\,\dd Z-\frac{\e^{-\I\pi\alpha}}{\alpha}\dd G,\qquad
 J_k=\frac1{2\alpha}\operatorname{Im}K_k-\frac{1}{2\alpha^2}\operatorname{Im}\Bigl(\e^{-\I\pi\alpha}\bigl[Z^{\alpha}\bigr]_k\Bigr),\qquad
 K_k:=\int_k\lvert Z\rvert^{p}\bar Z\,\dd Z,\tag{L.7}$$
$J(p,0)=\tfrac1{2\alpha}\operatorname{Im}\sum_kK_k$ (the $[Z^\alpha]_k$ telescope: $Z^\alpha$ is
single-valued on $\partial R$ with the boundary value from above, C1.3). Note the $\alpha^{-2}$ in the
endpoint term, from $\dd G=\dd Z^\alpha/\alpha$ — an $\alpha^{-1}$ there breaks the per-arc comparison
while leaving the total intact (found by the harness during this pass).

- *Circle*: $\lvert Z\rvert=1$, $\bar Z\,\dd Z=Z^{-1}\dd Z$, so the arc is **elementary**, no ${}_2F_1$:
  $$K_{\rm circle}=\bigl[\ln Z\bigr]_{-1}^{\e^{\I\pi/3}}=-\frac{2\pi\I}3 .\tag{L.8}$$
  (The incomplete Beta the earlier statement announced degenerates: the exponents are $(-1,0)$.)
- *Vertical*: $\lvert Z\rvert^{p}=Z^{p/2}(1-Z)^{p/2}$ exactly, $\bar Z=1-Z$:
  $$\lvert Z\rvert^{p}\bar Z\,\dd Z=Z^{p/2}(1-Z)^{p/2+1}\dd Z,\qquad
   K_{\rm vert}=\Bigl[B_Z(\alpha,\ \alpha+1)\Bigr]_{\e^{\I\pi/3}}^{\frac12+\I b}.\tag{L.9}$$
- *Ellipse*, (L.0). $\overline{cw+1}=(c+w)/w$ gives $\lvert Z\rvert=\tfrac{(cw+1)(w+c)}{4cw}$ with the
  principal arguments composing exactly ($\arg(cw+1)+\arg(w+c)-\arg w=0$ on the arc, both ends
  checked: $\pi+0-\pi$ at $w=-1$, $\arctan c+\arctan\tfrac1c-\tfrac\pi2$ at $w=\I$). With
  $(w+c)^{p+2}=c^{p+2}(1+w/c)^{p+2}$, $cw-1=-(1-cw)$ and $(4c)^{-p-2}c^{p+2}=4^{-p-2}$:
  $$\lvert Z\rvert^{p}\bar Z\,\dd Z=-4^{-p-2}\,(1+cw)^{p+1}(1+w/c)^{p+2}(1-cw)\,w^{-p-3}\dd w
   =-4^{-p-2}\bigl[w^{-p-3}-c\,w^{-p-2}\bigr](1+cw)^{p+1}(1+w/c)^{p+2}\dd w,\tag{L.10}$$
  $$K_{\rm ell}=-4^{-p-2}\Bigl[\Psi_{-p-2}(w)-c\,\Psi_{-p-1}(w)\Bigr]_{w=\I}^{w=-1},\qquad
   \Psi_a(w)=\frac{w^a}{a}F_1\bigl(a;\,-p-1,\,-p-2;\,a+1;\ -cw,\ -\tfrac wc\bigr).\tag{L.11}$$
  Here $(1+cw)^{p+1}$ is principal with $\operatorname{Im}(1+cw)=c\sin t\ge0$: at $w=-1$ it is the
  boundary value from above of the cut of $(1+cw)^{p+1}$ at $w=-1/c$ (this is the cut of $Z^{p/2}$
  at $Z=0$, which $\partial R$ touches along the real segment; the $p=0$ line has no such cut, which
  is why (L.5) needed no prescription). Correspondingly the first Appell argument $x=-cw$ is
  $c-\I0$ at $w=-1$ — on the cut $[1,\infty)$ of $F_1$, approached from $\operatorname{Im}x<0$ — and
  $x=-c\I$ at $w=\I$. The Cauchy argument of (L.5) applies with the branch point $w=-1/c$ on the
  boundary of the quarter disc; the identity holds for $\operatorname{Re}a>0$, $\operatorname{Re}(p+1)>-1$
  and extends analytically in $(a,b_1)$ to all $p$. Equivalent, prescription-free form (used by the
  second evaluator): substituting $u=1+cw$ in each term of the single-sum expansion,
  $\int_{\I}^{-1}w^{a+m-1}(1+cw)^{p+1}\dd w=c^{-a-m}\e^{\I\pi(a+m-1)}\bigl[B_u(p+2,\ a+m)\bigr]_{u=1+c\I}^{u=1-c}$,
  where $u^{p+2}$ at $u=1-c<0$ carries the boundary value from above and the ${}_2F_1$ argument
  $1-c$ is off its cut.
- *Real*: $\lvert x\rvert^{p}x\,\dd x$ and $\e^{-\I\pi\alpha}Z^{\alpha}=\lvert x\rvert^\alpha$ real: $J_{\rm real}=0$.

Summed:
$$\boxed{\ J(p,0)=\frac{1}{p+2}\Bigl\{-\frac{2\pi}3+\operatorname{Im}\Bigl[B_Z(\alpha,\alpha+1)\Bigr]_{\e^{\I\pi/3}}^{\frac12+\I b}
 -4^{-p-2}\operatorname{Im}\Bigl[\Psi_{-p-2}-c\,\Psi_{-p-1}\Bigr]_{\I}^{-1}\Bigr\},\qquad\alpha=\tfrac p2+1\ }\tag{L.12}$$
valid as written for $p\notin\{-2,-4,-6,\dots\}\cup\mathbb Z_{\ge-1}$ (A4's $p=-2$ and the normalisation poles of
the vertical term $B_Z(\alpha,\alpha+1)$ at $\alpha\in\mathbb Z_{\le0}$, as for (L.6) — orchestrator fix 2026-09-23, the set
listed only $p=-2$ before; $F_1$ with $a+1\in\mathbb Z_{\le0}$), removable poles, extended by continuity.

*Step 3, the limits $q\to0$ and $p\to0$.* At $q=0$, (L.2)–(L.5) are elementary
($-[\ln Z-Z]$, $[Z^2/2]$, $\tfrac1{16}[\,w^{-3}(1-cw)(1-w/c)(1+cw)\,]$-integrals), and (L.1$'$) reads
$J(0,0)=\tfrac12\operatorname{Im}\oint\bar Z\,\dd Z$, the area: (L.6) reproduces 045 (3.4) in the limit.
Same for (L.12) at $p=0$ ($\tfrac12\operatorname{Im}\oint\bar Z\dd Z$ again; (L.8) is the circle's
$-\tfrac{2\pi}3\cdot\tfrac12$ share of the area). Numerically the poles of $B_Z$ and $F_1$ at these
points are removable but cancel between endpoints, so the limit is taken symmetrically,
$\tfrac12[J(0,\epsilon)+J(0,-\epsilon)]=J(0,0)+O(\epsilon^2)$ — `C6-area-limit`.

*Asymmetry.* $Z\mapsto1-\bar Z$ exchanges $\lvert Z\rvert$ and $\lvert1-Z\rvert$ and fixes the full
confocal ellipse, but maps $R$ (which has $\lvert Z\rvert\ge1$, $\operatorname{Re}Z\le\tfrac12$) to
$\{\lvert1-Z\rvert\ge1,\operatorname{Re}Z\ge\tfrac12\}\cap\mathcal V_{0,4}\ne R$; no element of the
symmetry group of $R$ (trivial) relates the two lines, and $J(0,e)\ne J(e,0)$ (e.g. $J(0,1.3)=7.2777$,
$J(1.3,0)=4.7719$ at $\beta=\tfrac32$; `C6-no-symmetry`). The structural asymmetry is the cut: $\partial R$
touches the cut of $Z^{p/2}$ (real segment) and not that of $(1-Z)^{q/2}$, whence the $c-\I0$
prescription in (L.11) and its absence in (L.5), and the elementary circle (L.8) on $q=0$ versus the
incomplete Beta (L.2) on $p=0$.

\subsection*{Commentary}

- (L.1), (L.7): the reduction is Stokes' theorem applied to $\lvert1-Z\rvert^{q}(1-\bar Z)$, resp.
  $\lvert Z\rvert^{p}\bar Z$, whose $\bar Z$-derivative is $-\gamma\lvert1-Z\rvert^{q}$, resp.
  $\alpha\lvert Z\rvert^{p}$ — the general (A.2) specialised to an elementary $G$. The endpoint
  terms are kept so that the *per-arc* swept areas $J_k$ of (A.2) (what `J_boundary_hyp(per_arc=True)`
  returns, base point $G(-1)=0$) can be compared one by one; they drop from the totals.
- (L.2), (L.4), (L.10): every "$\lvert\cdot\rvert^{s}$ = product of principal powers" step is a
  statement that the principal arguments of the factors add up to the argument of the product
  without a $2\pi$ defect; each is checked at both endpoints of the arc in the text and, at
  interior points, by the harness (the per-arc agreement to $10^{-15}$ would fail by a phase
  $\e^{2\pi\I s}$ otherwise).
- (L.5), (L.11): the Appell $F_1$ enters only through (L.F) with third parameter $a+1$, the
  one-parameter family for which $F_1$ is an antiderivative in its own base point; the pair
  $(x,y)=(\pm cw,\pm w/c)$ has $\lvert x\rvert=c\ge$ (companion value, not reproduced here) and $\lvert y\rvert\le$ (companion value, not reproduced here) ($9$, $\tfrac19$ at $\beta=\tfrac32$) — outside and
  well inside the unit disc respectively. mpmath's `appellf1` continues in $x$; the single-sum form
  (Setup) converges geometrically in $y$ and needs only ${}_2F_1$ at $\lvert x\rvert=c$ (or, on $q=0$,
  the $u$-substituted incomplete Betas), so the two evaluators share no code path beyond `hyp2f1`.
  Their agreement to $10^{-26}$ (`C6-appell-series`) fixes the continuation and the $c-\I0$ side;
  the wrong side differs at $O(1)$.
- (L.8): on $q=0$ the circle arc is not on the constant-phase line $2p+q=-4$ (item 1 of the
  corrections; only at $(-2,0)$, excluded) — it closes for another reason, $\lvert Z\rvert^{p}\equiv1$
  there, which is also why $J(p,0)$ is only algebraically suppressed at large $\lvert p\rvert$
  (`## Consequence for 045`).
- Validity of the formulas at the excluded exponents (integer $q\ge-1$ etc.) is by continuity: $J$
  is entire (045 C1) and each excluded value is a removable singularity of an endpoint
  difference. The harness uses non-integer exponents.

\subsection*{Result}

$J(0,q)$ is (L.6) and $J(p,0)$ is (L.12): on each line, one incomplete Beta on the vertical
segment, one incomplete Beta (on $p=0$) or an elementary term $-\tfrac{2\pi}3$ (on $q=0$) on the
unit circle, two Appell $F_1(a;\cdot,\cdot;a+1;x,y)$ with $\lvert x\rvert=4\beta^2$, $\lvert y\rvert=1/4\beta^2$
on the ellipse quarter, nothing on the real segment. Every coefficient, phase and branch is
stated above; both lines verified against (A.2) to the reference's own precision ($1.4\times10^{-15}$
worst, 16 points, $\lvert q\rvert$ or $\lvert p\rvert$ up to $21.7$, $\beta\in\{\tfrac32,2\}$), the
$q\to0$/$p\to0$ limits reproduce the area to $6.8\times10^{-13}$ (symmetric difference,
$\epsilon=10^{-6}$), the two lines are not related by a symmetry. **Node C2.4 is verified as
stated**, with two sharpenings: on $q=0$ the circle arc is elementary rather than an incomplete
Beta, and the $q=0$ ellipse term needs the $c-\I0$ prescription (or the $u$-substituted form) because
$\partial R$ touches the cut of $Z^{p/2}$. No claimed closure fails on any arc. The endpoint term of
(L.7) carries $\alpha^{-2}$, not $\alpha^{-1}$ (per-arc bookkeeping only).

\subsection*{Verification}

`codes/verify-j-closed-form.py --only C6` (4 checks, 4 PASS; the full harness, 25 checks, is
run once at the end of this pass: 25/25 PASS, exit 0, seed 20260922 (report `agent/reports/computator-047-c24-20260923T124500.md`);
the record's main `## Verification` table above is not extended — the C6 rows live here). Reference: `J_boundary_hyp(per_arc=True)` — (A.2) with $G$
from (A.3), mpmath quadrature per arc; its arc parametrisations are double precision, so
$\sim10^{-15}$ relative is its floor.

| line | exponent | $\beta$ | closed form (L.6)/(L.12) | (A.2) | rel. diff | max per-arc rel. diff |
|---|---|---|---|---|---|---|
| $p=0$ | $q=-21.7$ | $\tfrac32$ | $0.0029968161665203085$ | $0.0029968161665203128$ | $1.4\times10^{-15}$ | $9.8\times10^{-16}$ |
| $p=0$ | $q=-3.3$ | $\tfrac32$ | $0.29562087558224580$ | $0.29562087558224582$ | $4.5\times10^{-17}$ | $9.2\times10^{-17}$ |
| $p=0$ | $q=1.3$ | $\tfrac32$ | $7.2777400489870714$ | $7.2777400489870713$ | $2.6\times10^{-18}$ | $2.1\times10^{-17}$ |
| $p=0$ | $q=20.3$ | $\tfrac32$ | $182375762.18390841$ | $182375762.18390829$ | $6.7\times10^{-16}$ | $6.7\times10^{-16}$ |
| $q=0$ | $p=-21.7$ | $\tfrac32$ | $0.10491825555419988$ | $0.10491825555419988$ | $5.5\times10^{-17}$ | $4.9\times10^{-17}$ |
| $q=0$ | $p=-3.3$ | $\tfrac32$ | $0.87202892698129237$ | $0.87202892698129245$ | $9.1\times10^{-17}$ | $7.8\times10^{-17}$ |
| $q=0$ | $p=1.3$ | $\tfrac32$ | $4.7719380011395506$ | $4.7719380011395509$ | $7.6\times10^{-17}$ | $9.2\times10^{-17}$ |
| $q=0$ | $p=20.3$ | $\tfrac32$ | $925421.44995447400$ | $925421.44995447497$ | $1.1\times10^{-15}$ | $1.1\times10^{-15}$ |
| $p=0$ | $q=-21.7$ | $2$ | $0.0029968173230483335$ | $0.0029968173230483377$ | $1.4\times10^{-15}$ | $9.8\times10^{-16}$ |
| $p=0$ | $q=-3.3$ | $2$ | $0.45183242351796004$ | $0.45183242351796006$ | $3.4\times10^{-17}$ | $6.6\times10^{-17}$ |
| $p=0$ | $q=1.3$ | $2$ | $51.959949759007103$ | $51.959949759007102$ | $3.2\times10^{-17}$ | $2.9\times10^{-17}$ |
| $p=0$ | $q=20.3$ | $2$ | $12988368182111.780$ | $12988368182111.777$ | $2.0\times10^{-16}$ | $2.0\times10^{-16}$ |
| $q=0$ | $p=-21.7$ | $2$ | $0.10491866629026311$ | $0.10491866629026312$ | $5.3\times10^{-17}$ | $4.9\times10^{-17}$ |
| $q=0$ | $p=-3.3$ | $2$ | $1.1983956584295495$ | $1.1983956584295496$ | $5.9\times10^{-17}$ | $5.7\times10^{-17}$ |
| $q=0$ | $p=1.3$ | $2$ | $39.425828604915263$ | $39.425828604915262$ | $1.8\times10^{-17}$ | $1.6\times10^{-17}$ |
| $q=0$ | $p=20.3$ | $2$ | $521894219426.87644$ | $521894219426.87650$ | $1.3\times10^{-16}$ | $1.3\times10^{-16}$ |

| check | what | outcome |
|---|---|---|
| `C6-closed-lines` | the 16 rows above, total and per arc, tolerance $10^{-12}$; break legs: ellipse $F_1$ term $\times(1+10^{-3})$ at the 12 points where $\lvert J_{\rm ell}\rvert>10^{-4}\lvert J\rvert$ (min rel $6.0\times10^{-5}$; at $q=-21.7$ the ellipse carries $\sim10^{-9}$ of $J$, the weight sits at $\e^{\I\pi/3}$), largest arc term $\times(1+10^{-3})$ at all 16 (min rel $4.6\times10^{-4}$) | PASS, max $1.4\times10^{-15}$ / $1.1\times10^{-15}$ |
| `C6-appell-series` | mpmath `appellf1` (continuation in $x$, $c-\I0$ by $x=c(1-10^{-40}\I)$) vs the single-sum incomplete-Beta form, both lines, 16 points; break: $c+\I0$ | PASS, max rel $1.2\times10^{-26}$; break rel $0.94$ |
| `C6-area-limit` | $\tfrac12[J(0,\pm\epsilon)]$ and $\tfrac12[J(\pm\epsilon,0)]$ vs 045 (3.4), $\epsilon=10^{-6}$, 50 digits, tolerance $10^{-11}$; one-sided offset must be $O(\epsilon)$ | PASS, max rel $6.8\times10^{-13}$; one-sided $1.1\times10^{-6}$ |
| `C6-no-symmetry` | $\min\operatorname{rel}\lvert J(0,e)-J(e,0)\rvert$, $e\in\{1.3,-3.3\}$, both $\beta$, must exceed $10^{-2}$ | PASS, $0.32$ |

Not verified here: the formulas at the excluded (integer) exponents, taken by continuity; the
$F_1$ continuation beyond the two evaluators' mutual agreement (no third, e.g. direct
Euler-integral, evaluation at $\operatorname{Re}a\le0$ — the Euler integral itself was checked against
`appellf1` at $\operatorname{Re}a>0$ during development, $q=-3.7$, both endpoints, to $10^{-30}$, but that
check is not in the harness).

## Fix pass 2026-09-23 (node check of the corrections)

Brief `computator-047-fix-20260923T142500`, applying `agent/reports/critic-047-corr-20260923T141000.md` (verdict: accept with one Serious).

| # | Finding (severity) | Action | Locations |
|---|---|---|---|
| 1 | The item-8 dispute is wrong: the $1/(\lambda+1)$ is missing from (A.11), not from (A.10) (Serious) | Re-derived term by term, (C.9): the prefactor is $\tfrac{z^{\lambda+1}}{\lambda+1}$, and at $\mu=0$ (A.11) must reduce to (A.10). Prefactor restored in (A.11) with a dated note; item 8 heading and second half rewritten as **confirmed** (the reviewer's "(5.7)" is (A.11)/`eq:two-powers`; the corrections pass checked (A.10) and answered the wrong equation); plan line of item 8 corrected; (A.11) leg added to `C7-item8-beta04` (double series truncated at $m+n<90$ vs quadrature at two $(\lambda,\mu,z)$, $\mu=0$ specialisation vs (A.10), break leg = prefactor dropped); R50 edit (v) added; note-side list written | Block A (A.11); `### Item 8`; corrections plan (item 8 bullet); `### What changes in R50`; `## Verification` table row; `codes/verify-j-closed-form.py` docstring and check |
| 2 | R50 edit list stale on C2.4 (Concern) | Edit (iv) added: the two "not machine-checked, node C2.4" flags → verified by `C6-closed-lines` (16 points, $1.4\times10^{-15}$), with the two C2.4 sharpenings named | `### What changes in R50` |
| 3 | Exclusion set of (L.6) incomplete; (C.6) convergence on $\lvert w\rvert=1$ unstated (Minor) | (L.6): exclusion set now $q\notin\{0,-2\}\cup\{-4,-6,-8,\dots\}\cup\mathbb Z_{\ge-1}$, each pole attributed to its term; (C.6): the ${}_3F_2$ converges absolutely on $\lvert w\rvert=1$, parameter excess $\tfrac12>0$, so the endpoint values are values of the series | (L.6) validity clause; item 3 (c), after (C.6) |
| – | Drive-by: the script docstring of `C2.3-reflect` still gave Euler's condition as $\mu=c-a-b$ (item 3 corrected the sign in the record only) | Docstring line corrected to $\mu=a+b-c$, sufficient, $p=0$, $q=-1$, $q=-2$ | script docstring |

**Dependents of the changed nodes.** (A.11) is cited by C2.3 for its *structure* (double series in one variable, collapsing under Euler's condition), by the Commentary bullet (A.9)–(A.11), the `### Scope of the exclusion` and the proposed ledger row — none of them quotes the prefactor, and an overall constant changes neither the structure nor the collapse condition: all hold, statements unchanged, justification unchanged. Nothing numerical in Blocks A–B, in `## Consequence for 045` or in C2.4 was ever evaluated through (A.11). (L.6): validity clause only, the formula and `C6-closed-lines` (non-integer points) unchanged. (C.6): justification strengthened, statement unchanged; the $J(-1,-1)$ corollary and `C7-item3-euler` unchanged. For each changed node: (A.11) — statement changed (prefactor); item 8 — verdict changed (disputed → confirmed); (L.6), (C.6) — justification only.

**Harness.** `--only legacy` after the edits (`agent/scratch/j-closed-form-legacy-fixpass-2026-09-23.log`): **21/21 PASS**, seed 20260922; `C7-item8-beta04`: $a(\beta_{04})-\tfrac32=0$, $a(\beta_{04}-0.05)=$ (companion value, not reproduced here); (A.10) $2.5\times10^{-32}$ (break $7.3\times10^{-2}$); **(A.11) leg**: double series vs quadrature max $1.5\times10^{-30}$ over the two points, $\mu=0$ specialisation vs (A.10) $2.5\times10^{-32}$, break leg (prefactor dropped) min $6.3\times10^{-2}$. Full run (`agent/scratch/j-closed-form-full-fixpass-2026-09-23.log`, started 15:08, ≈43 min): **25/25 PASS**, exit code 0, seed 20260922 (25/25 before the pass).

## Fix pass 2026-09-23 (node check of the consolidation)

Findings of `agent/reports/critic-047-improve-20260923T155000.md`; one row per finding.

| Finding | Severity | Applied / disputed | Where |
| ------- | -------- | ------------------ | ----- |
| `## Result` per-arc table: vertical row "closes otherwise? no" contradicts C2.4 (L.3), (L.9) and item 3(b); circle row files $p+q=-4$ under ${}_3F_2$ where the source says incomplete Beta | Concern, mechanical | Applied: vertical cell → incomplete Beta on $p=0$ (L.3), $q=0$ (L.9), $p+q=-4$; circle cell → ${}_3F_2$ on $q=-1$, $q=-2$; incomplete Beta on $p+q=-4$ and $p=0$ (L.2); elementary on $q=0$ (L.8). Other rows checked against (A.5), (C.3), (L.5), (L.11): unchanged. The same fold in `### Scope` ("as a single ${}_3F_2$ on $q=-1$, $q=-2$, $p+q=-4$") corrected identically | `## Result` item 1 table; `### Scope of the exclusion` second paragraph |
| Block A *ellipse quarter*: Goursat list read as if every line linearised the ellipse argument; item 6(a) aimed at $p+2q=-4$ | Concern, one paragraph | Applied, after re-checking the ramification argument (agree: $z=(1+x)^2/4x$ ramified at $x=\pm1$ over $z=0,1$; pulled-back exponent differences $2(1-c)$, $2(c-a-b)$, $a-b$, $a-b$; three-point iff $1-c=\pm\tfrac12$ or $a+b-c=\pm\tfrac12$, i.e. $p\in\{-1,-3\}$ or $q\in\{-1,-3\}$). Paragraph now states the list as "admits *a* quadratic transformation", names the sub-family, keeps the not-machine-checked flag, and "cannot be reduced to a linear one" reads "by a quadratic transformation"; item 6(a) redirected to $q=-1$ or $p=-1$ off $(-1,-1)$ | Block A, *C2, ellipse quarter*; `## Next` item 6 |
| Ledger row: "7 break legs firing" stale | Minor, mechanical | Applied: log lists 9 checks with break legs, 11 legs (C7-item8 and C6-closed-lines carry two each) | `## Proposed ledger row`, status cell |
| "every special locus found above" omits $q=-2$ | Minor | Applied: "except $q=-2$" with the reason ($a+b-c=0$, logarithmic) | Block A, *ellipse quarter*; `## Next` item 6 |
| C2 cites C2.1–C2.3 only | Minor, mechanical | Applied: C2.1–C2.4 | Claim tree, C2 |
| "R2's uniformiser" is $Z_4^{(s)}(1/w)$ | Minor | Applied: qualifier added at the three places (C2.4, `### Scope`, ledger row) | Claim tree C2.4; `### Scope`; ledger row |
| "one per Pfaff representative" covers the direct case $q=-1$ | Minor | Applied: "$p=0$ and $q=-2$, one per Pfaff representative (C.5)(B), (A), and $q=-1$ directly" | Claim tree C2.3 (iii); ledger row |
