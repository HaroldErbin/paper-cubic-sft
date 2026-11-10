# 054 – PH6 (b): conjugation invariance of the SL(2,C) family at n = 4

Brief: `agent/briefs/active-computator-ph6-family-20260926T021000.md`.
Companion script: `codes/verify-ph6-conjugation-n4.py`.

## Status

All steps done (1–6); script run 1: 45/45 PASS incl. 14 break legs, seed 20260926. Critic ACCEPT (`agent/reports/critic-054-20260926T022000.md`); mechanical fix pass applied (I1 relabelled analytic with the closed-form distance argument, triangle-group angles corrected, probe clause reworded as a C1.2/C1.3 corollary throughout, PH6 wording extended to name all residues, $\beta>\tfrac12$ qualifier and A2 wording added). No script change, no re-run. Next: orchestrator promotion.

## Task and objective

**Literal task.** For the sister project's declared SL(2,C) section at $n=4$, establish the geometric inputs of record 028 §1 (C4) that give $\ddagger$-equivariance of $V_4$: (i) conjugation invariance of the region (tiling by $G=S_3\times\{1,\mathrm{conj}\}$); (ii) conjugation equivariance of the section data (radii, $S_0$, $R$, $\Lambda_1$, $F_a$); (iii) behaviour of $\mathrm d^2Z$ and of the level-0 Koba–Nielsen integrand of 044 so that the tile sum is $\ddagger$-equivariant on the tachyon block.

**Objective.** R35 and R46 are conditional on PH6; this record turns clause (b) of PH6 from "unconfirmed, likely" into a checked statement at $n=4$ for the family actually used.

## Conventions

Book conventions (the project conventions; `knowledge/conventions.md`). Punctures $0,1,\infty,Z$ on the sphere; $\mathrm d^2Z=2\,\mathrm d\,\mathrm{Re}Z\,\mathrm d\,\mathrm{Im}Z$ (044 A1–A7, cited not restated).

## Step 1 – The 028 §1 argument and its geometric inputs

028 §1 (C4): "$V_4(A_1,\dots,A_4)^*=V_4(A_1^\ddagger,\dots,A_4^\ddagger)$ follows from Sonoda–Zwiebach H5 ($\mathcal O(t^*)=\mathcal O(t)^*$) together with the invariance of the moduli region $\mathcal V_{0,4}$ and of its measure under complex conjugation of the moduli." The origin paragraph: $V_n$ is a correlator over a real region with a real measure; H5 says insertions and plumbing data transform under hermitian conjugation into insertions of the $\ddagger$-conjugate states at the conjugate moduli.

Checklist of the inputs, as they must hold for an explicit section:

| # | Input | Form for the family | Step | Outcome |
|---|---|---|---|---|
| I1 | region invariant under $Z\to\bar Z$ | $\overline{\mathcal V_{0,4}}=\mathcal V_{0,4}$; conj maps $\mathrm{FD}\cap\mathcal V_{0,4}$ onto a tile of the $G$-tiling; boundary arcs to boundary arcs | 2 | holds (C1.1) |
| I2 | local coordinates conjugation-equivariant (H5 for the section) | $F_a(\bar w;\bar Z)=\overline{F_a(w;Z)}$; hence radii $\rho_a(\bar Z)=\rho_a(Z)$ | 3 | holds for $F_a'(0)$ and the plumbing maps; vertex-section maps beyond first order not packaged (C1.2) |
| I3 | point maps / weight equivariant (section data entering the tile assembly) | $S_0(\bar Z)=\overline{S_0(Z)}$, $R(\bar Z,Z)=\overline{R(Z,\bar Z)}$, $\Lambda_1(\bar Z)=\Lambda_1(Z)$ | 3 | holds (C1.3) |
| I4 | measure real and conj-invariant up to orientation | $\mathrm d^2Z$ positive, orientation reversal compensated by the region map | 4 | holds; level-0 block equivariant but blind to I1–I3 (C1.4) |
| I5 | CFT reality of the correlator (H5 proper) | $\langle\prod f_a\circ A_a\rangle^*=\langle\prod \bar f_a\circ A_a^\ddagger\rangle$ | 4 (level 0 only: explicit KN integrand) | cited (A4); probe for primaries (C1.5) |

## Claim tree

- **A1** Conventions and setup of 044 A1–A3, A6, A7 (book conventions, momenta, punctures $0,1,\infty,Z$, $z_3=\infty$ regularisation, tachyonic dressing), cited.
- **A2** *(imported)* 044 A4 (radii closed form, `SL: R51`) and A5 (equivariant 12-tile assembly, `SL: R6/R10/R14`), the inputs of R48; `SL: R7` ($\mathrm{FD}\cap\mathcal V_{0,4}=\mathrm{FD}\cap E_\beta$ for $\beta\ge\beta_{04}$) is re-derived for the region (2.1) in C1.1.3; that (2.1) is the sister's $\mathcal V_{0,4}$ is still `SL: R7`'s content.
- **A3** *(imported)* The declared section as packaged by the sister module: $S=S_0$, $R$ of `SL: R34` at $\lambda_0$, frames $F_a'(0)=\kappa_aS_0$; $\beta\ge\beta_{04}$, numerics at the standard parameter values of the companion construction.
- **A4** CFT reality of plane correlators with real exponents (Sonoda–Zwiebach H5 restricted to primaries; 028 (C4)), used only in C1.5.
- No new hypothesis. PH26 ($\rho_3$ residual factor) is not needed: a real positive factor on any $\rho_a$ leaves every claim below unchanged.
- **C1** At $n=4$, the SL(2,C) declared section satisfies the geometric inputs I1–I4 of 028 §1 (region, local coordinates to first order, point maps and weight, measure), and $V_4$ is $\ddagger$-equivariant on the level-0 tachyon block; for integer-spin primaries under the CFT reality input, the conj tile pairs are real as a corollary of C1.2/C1.3 (frame equivariance) and the Schwarz-symmetric correlator form — a diagnostic, not an independent test of I1. [by C1.1–C1.5]
  - **C1.1** I1: $\mathcal V_{0,4}$ is conj-invariant; conj maps $T=\mathrm{FD}\cap\mathcal V_{0,4}$ onto the tile $\bar T$ of the $G$-decomposition; walls go to walls, $C_4$ into $\partial\mathcal V_{0,4}$. [by C1.1.1–C1.1.3; step 2]
    - **C1.1.1** $S_3$ commutes with conj; $G=S_3\times\{1,\mathrm{conj}\}$, order 12. [eq. (2.2)] [check: C1.1-commute, C1.1-group]
    - **C1.1.2** $E_\beta$ and the region (2.1) are conj-invariant. [by C1.1.1; eq. (2.3)] [check: C1.1-conj]
    - **C1.1.3** The 12 tiles reproduce (2.1) exactly for $\beta\ge\beta_{04}$ (unit disc inside $E_\beta$, analytic). [step 2 (d); by check: C1.1-tiling] [check: C1.1-disc (numerical confirmation), C1.1-arcs]
  - **C1.2** I2 (first order and plumbing maps): $F_a(\bar w;\bar Z)=\overline{F_a(w;Z)}$, $\rho_a(\bar Z)=\rho_a(Z)$, $F_a'(0)=\kappa_aS_0$ for $a=1,4$. [by A3; eq. (3.1)] [check: C1.2-maps, C1.2-radii, C1.2-derivs]
  - **C1.3** I3: $S_0$, $R$ conj-equivariant, $\Lambda_1$ conj-invariant; the conj-transported section equals the closed forms at $\bar Z$ and glues across $C_1$; the wall conditions on $C_2$, $C_3$ hold. [by A3; eqs. (3.1), (3.2)] [check: C1.3-equiv, C1.3-mirrorC1, C1.3-mirrorsC2C3]
  - **C1.4** I4 and level 0: the tile sum (4.3) is real for real off-shell momenta, and $\{T(k_i)\}^*=\{T(k_i)^\ddagger\}$; this holds tile by tile and does not test C1.1–C1.3. [by A1, A2, C1.1, C1.2; eqs. (4.1)–(4.4)] [check: C1.4-integrand, C1.4-tilesum, C1.4-blind]
  - **C1.5** For integer-spin primaries of real weights, the conj tile pair is real with the declared section; removing the conj tile or deforming $S$ by an odd imaginary term breaks it. [by A4, C1.1, C1.2, C1.3; step 4 commentary] [check: C1.5-probe]

Open gaps: none within the scope stated (the out-of-scope items are listed in step 5, not as nodes).
Hypotheses in force: none (A2, A3 imported inputs; A4 used only by C1.5)

Ledger note: the brief's "R14", "R34", "R44" are the sister project's rows (`SL: R14` equivariant transport and $G=S_3\times\{1,\mathrm{conj}\}$, `SL: R34` interior map, `SL: R44` odd-dilaton densities); this project's R14/R34/R44 are different results. Cited below with the `SL:` prefix.

## Step 2 – (i) The region and its tiling under conjugation

### Setup

A3 of 044 (punctures $0,1,\infty,Z$). Block-local definitions, all from the sister module (`in_closed_FD`, `ellipse_axes`, `in_V04_ellipse`):

- $\mathrm{FD}=\{\operatorname{Im}Z\ge0,\ |Z|\ge1,\ \operatorname{Re}Z\le\tfrac12\}$, walls $C_1$ (real, $Z\le-1$), $C_2$ ($\operatorname{Re}Z=\tfrac12$), $C_3$ ($|Z|=1$).
- $E_\beta$: the closed ellipse centred at $\tfrac12$ with semi-axes $a=\beta^2+1/16\beta^2$, $b=\beta^2-1/16\beta^2$ on the real and imaginary axes; its boundary is the image of $|q|=1$ under $Z^{(s)}(q)=\tfrac12+\beta^2/q+q/16\beta^2$ (`SL: R7`, this project's R2), wall $C_4$.
- $T:=\mathrm{FD}\cap E_\beta$, which equals $\mathrm{FD}\cap\mathcal V_{0,4}$ for $\beta\ge\beta_{04}$ (`SL: R7`, imported).
- $S_3$: the anharmonic group $\{Z,\,1-Z,\,1/Z,\,Z/(Z-1),\,1/(1-Z),\,(Z-1)/Z\}$; $G=S_3\times\{1,\mathrm{conj}\}$, $\mathrm{conj}(Z)=\bar Z$.
- Independent definition of the contact region, not using the tiling: the $s$-channel Feynman region is the exterior of $E_\beta$ (the $|q|<1$ image, $Z\to\infty$ as $q\to0$); the $t$- and $u$-channel regions are its images under the maps sending $\infty$ to $0$ and to $1$ (R2's cross-ratio closure). Hence
$$\mathcal V_{0,4}^{\rm ind}=\{Z:\ Z\in E_\beta,\ 1/Z\in E_\beta,\ 1/(1-Z)\in E_\beta\}.\tag{2.1}$$

### Derivation

(a) Every element of $S_3$ is a Möbius map with real (integer) coefficients, so $\overline{h(Z)}=h(\bar Z)$ for $h\in S_3$:
$$\mathrm{conj}\circ h=h\circ\mathrm{conj}.\tag{2.2}$$
Hence $G$ is a direct product of order 12 and $\mathrm{conj}$ permutes the tiles: $\mathrm{conj}(h(T))=h(\mathrm{conj}\,T)=(h\cdot\mathrm{conj})(T)$.

(b) $E_\beta$ is invariant under $Z\to\bar Z$ (centre on the real axis, axes along the real and imaginary directions; equivalently $Z^{(s)}(\bar q)=\overline{Z^{(s)}(q)}$ and $|\bar q|=|q|$). With (2.2), each of the three conditions of (2.1) is conj-invariant:
$$\overline{\mathcal V_{0,4}^{\rm ind}}=\mathcal V_{0,4}^{\rm ind}.\tag{2.3}$$

(c) $\mathrm{conj}(\mathrm{FD})=\{\operatorname{Im}Z\le0,|Z|\ge1,\operatorname{Re}Z\le\tfrac12\}$ is the $G$-image of FD by $g=\mathrm{conj}$. $\mathrm{FD}$ is one of the 12 triangles cut out of the sphere by the real axis, the circles $|Z|=1$, $|Z-1|=1$ and the line $\operatorname{Re}Z=\tfrac12$ (vertices $-1$, $e^{i\pi/3}$, $\infty$); these triangles are the $G$-orbit of FD, and $G$ acts simply transitively on them (standard: the extended anharmonic group, fixed points $e^{\pm i\pi/3}$, $-1,\tfrac12,2$). Hence $\mathrm{conj}(T)=\mathrm{conj}(\mathrm{FD})\cap E_\beta$ is the tile $g=\mathrm{conj}$ of the decomposition, and $T\cap\mathrm{conj}(T)=C_1\cap E_\beta$ (measure zero).

(d) Tiling consistency, the one input specific to the family. $\mathcal V_{0,4}^{\rm ind}=\bigcup_{g\in G}g(T)$ up to walls. Each condition of (2.1) is permuted by $S_3$ (using the $Z\to1-Z$ symmetry of $E_\beta$; the set $\{Z,1/Z,1/(1-Z)\}$ is R2's $s,t,u$ closure $Z^{(t)}=Z/(Z-1)$, $Z^{(u)}=1/(1-Z)$ read through that symmetry) and is conj-invariant by (b), so $\mathcal V^{\rm ind}_{0,4}$ is $G$-invariant; with (c) the statement reduces to $\mathrm{FD}\cap\mathcal V^{\rm ind}_{0,4}=\mathrm{FD}\cap E_\beta$. On FD, $|Z|\ge1$ and $|1-Z|\ge1$, so $1/Z$ and $1/(1-Z)$ lie in the closed unit disc, and the reduction holds iff the unit disc lies in $E_\beta$, i.e. $\operatorname{dist}(0,\partial E_\beta)\ge1$. This distance has an exact closed form. With $E_\beta$ centred at $\tfrac12$ (offset $c=\tfrac12$ from $0$) and semi-axes $a,b$, the squared distance from $0$ to the boundary point $(\tfrac12+a\cos\theta,\,b\sin\theta)$ is
$$d^2(\theta)=(a^2-b^2)u^2+2ac\,u+c^2+b^2,\qquad u=\cos\theta\in[-1,1],$$
a convex quadratic in $u$ (leading coefficient $a^2-b^2=\tfrac14$) with vertex at $u^*=-ac/(a^2-b^2)=-2a\le-3<-1$. The minimum on $[-1,1]$ is therefore at $u=-1$, i.e. at the left vertex, with $d^2=(a-c)^2$:
$$\operatorname{dist}(0,\partial E_\beta)=a-\tfrac12\quad\text{exactly, for every }\beta>\tfrac12.$$
Hence the unit disc lies in $E_\beta$ iff $a\ge\tfrac32$ iff $16\beta^4-24\beta^2+1\ge0$, i.e. $\beta\ge\beta_{04}=\tfrac12+\tfrac1{\sqrt2}$, in the range $\beta>\tfrac12$ (where $b>0$; $a=\tfrac32$ solves $16\beta^4-24\beta^2+1=0$, the definition of $\beta_{04}$). The closed form reproduces the scanned values of $a-\tfrac12$ (including a break leg below the threshold), kept as a numerical confirmation (`C1.1-disc`). This is `SL: R7`'s "limaçon exclusion measure zero for $\beta\ge\beta_{04}$", re-derived here from the conjugation side.

(e) Boundary arcs. $\partial T$ consists of four arcs: $C_1\cap E_\beta$ (real segment $[\tfrac12-a,-1]$), $C_3$ from $-1$ to $e^{i\pi/3}$, $C_2$ from $e^{i\pi/3}$ to $\tfrac12+ib$, and the ellipse arc $C_4$ from $\tfrac12+ib$ to $\tfrac12-a$. Conjugation fixes $C_1$ pointwise and maps $C_2,C_3,C_4$ onto the corresponding arcs of $\partial(\mathrm{conj}\,T)$. The arcs' Schwarz functions (047 (A.7)): $S(Z)=Z$, $1-Z$, $1/Z$, and the confocal-ellipse one; on the arc $\bar Z=S(Z)$, so each interior wall is the fixed set of an orientation-reversing element $\mathrm{conj}\circ h$ with $h=\mathrm{id},\ 1-Z,\ 1/Z\in S_3$, i.e. the mirrors of $\mathrm{conj},\ \mathrm{conj}\circ(1-Z),\ \mathrm{conj}\circ(1/Z)$ of $G$ — the reflections that generate $G$ as a reflection group — and $C_4\subset\partial\mathcal V_{0,4}$ is mapped by conj into $\partial\mathcal V_{0,4}$ by (2.3).

### Commentary

- (2.2) is the whole reason conjugation is compatible with the tiling: the permutation part of $G$ has real coefficients. A vertex family whose $S_3$ acted by non-real Möbius maps would not have this.
- (d) is the only place the specific family enters (the ellipse size). It is `SL: R7`'s statement that the limaçon exclusion is measure zero for $\beta\ge\beta_{04}$, seen from the conjugation side.
- (e): $G$ is generated by the three reflections in the walls of FD (the spherical triangle group $(2,2,3)$: angles $\pi/2,\pi/3,\pi/2$ at $-1$, $e^{i\pi/3}$, $\infty$, order 12); the tiling is therefore the reflection tiling, conj is one of the generating reflections, and conjugation invariance of the *decomposition* is automatic once the region test is $G$-invariant. What is not automatic, and is checked in step 3, is that the *section* glues across the mirror $C_1$ of conj.

### Result

$$\boxed{\ \overline{\mathcal V_{0,4}}=\mathcal V_{0,4}=\bigcup_{g\in S_3\times\{1,\mathrm{conj}\}}g(T),\qquad \mathrm{conj}(h(T))=(h\cdot\mathrm{conj})(T)\ \ (\beta\ge\beta_{04}).\ }$$

The contact region is conjugation invariant as a set; conjugation is one of the three generating reflections of the tiling (mirror $C_1$), and permutes the 12 tiles in six pairs $\{h(T),h(\bar T)\}$; the walls go to walls, the outer arc $C_4$ to $\partial\mathcal V_{0,4}$. Analytic, including the unit-disc inclusion ($\operatorname{dist}(0,\partial E_\beta)=a-\tfrac12$ exactly), numerically confirmed.

### Verification

Script part 1 (seed 20260926, log `agent/scratch/ph6-n4-run1.log`): `C1.1-commute` (exact, 0), `C1.1-group` ($|G|=12$, closed), `C1.1-disc` (three parameter values), `C1.1-tiling` (a sampled region test: 0 mismatches between (2.1) and the union of the 12 tiles, 0 multiply covered), `C1.1-conj` (0 failures of conj-invariance and of the tile map $(h,c)\to(h,1-c)$), `C1.1-arcs` (mirror residuals $\le2\times10^{-16}$, conjugated $C_4$ on $\partial E_\beta$ to $4\times10^{-16}$). Break legs fire: a non-real Möbius map fails to commute, a parameter value below the threshold breaks the disc inclusion, the union with the conj tile removed is not conj-invariant, the $C_2$ arc fed the $C_3$ mirror fails.

## Step 3 – (ii) The section data under conjugation

### Setup

A2, A3 (below). Block-local: $q(Z;\beta)$ the $|q|\le1$ root of $q^2+8\beta^2(1-2Z)q+16\beta^4=0$ (module `q_of_Z`); $F_a(w;Z)$ the module's maps (the $s$-channel plumbing maps, 052 §2C, whose $F_a'(0)$ equal the section's: $F_1'(0)=S_0$, $F_4'(0)=(Z-1)S_0$, checked, and generally $F_a'(0)=\kappa_aS_0$, $\kappa=(1,(1-Z)/Z,1/Z,Z-1)$, $a=3$ in the $t=1/z$ chart); $S_0=\beta^{-1}\sqrt{Z/(Z-1)}$ (principal branch); $1/R=(1-\Lambda_1)(1+Z)/3Z+\Lambda_1(1+3x)/2(1+x)$, $x=e^{-w(Z)}$, $w=\operatorname{arccosh}(2Z-1)$; $\Lambda_1=\phi(d_3/(d_3+\lambda_0d_4))$, $d_3=(|Z|^2-1)(|Z-1|^2-1)$, $d_4=\log4\beta^2-\operatorname{Re}w$.

### Derivation

The rule: an analytic function with real Taylor coefficients, or a principal branch ($\sqrt{\ }$, $\log$, $\operatorname{arccosh}$) whose cut lies on the real axis, satisfies $f(\bar u)=\overline{f(u)}$ off its cut.

$$\begin{aligned}
q(\bar Z)&=\overline{q(Z)} &&\text{(real-coefficient quadratic; root selection by }|q|\text{)}\\
F_a(\bar w;\bar Z)&=\overline{F_a(w;Z)} &&\text{(rational in }w,q,\beta\text{ with real coefficients; }F_{3,4}=Z/F_{1,2})\\
\rho_a(\bar Z)&=\rho_a(Z) &&\text{(closed form depends on }|Z|,|1-Z|\text{ only)}\\
S_0(\bar Z)&=\overline{S_0(Z)} &&\text{(}Z/(Z-1)\text{ real-rational, cut }Z\in[0,1)\text{ outside }\mathrm{FD}\cup\overline{\mathrm{FD}}\text{)}\\
\Lambda_1(\bar Z)&=\Lambda_1(Z) &&(d_3,\ \operatorname{Re}w\text{ conj-invariant})\\
R(\bar Z,Z)&=\overline{R(Z,\bar Z)} &&\text{(anchors real-rational in }Z,x;\ x(\bar Z)=\overline{x(Z)};\ \Lambda_1\text{ real)}
\end{aligned}\tag{3.1}$$

Gluing across the mirror of conj. The section on the tile $\bar T$ is the conj-transport of the section on $T$ (`SL: R14`): $F^{\bar T}_a(w;\bar Z):=\overline{F_a(\bar w;Z)}$, $S^{\bar T}(\bar Z):=\overline{S_0(Z)}$, $R^{\bar T}(\bar Z):=\overline{R(Z)}$. By (3.1) the transported data are the same closed forms evaluated at $\bar Z$. The transported section is continuous across $C_1$ iff the FD data are real on $C_1$:
$$Z\in C_1\ (Z\le-1):\quad q,\ S_0=\beta^{-1}\sqrt{Z/(Z-1)}\ (Z/(Z-1)\in(\tfrac12,1)),\ R\ (x=e^{-w}<0\text{ real}),\ F_a(w\in\mathbb R)\ \in\mathbb R.\tag{3.2}$$
On the other two mirrors the transport uses $\mathrm{conj}\circ(1-Z)$ and $\mathrm{conj}\circ(1/Z)$; the corresponding conditions are the sister wall conditions $\operatorname{Re}(Z/R)=\tfrac12$ on $C_2$ and $\operatorname{Im}(e^{i\theta/2}/R)=0$ on $C_3$ (`SL: R34`), re-checked here.

### Commentary

- (3.1), $R$: $R$ is non-holomorphic in $Z$ (`SL: R34`), so equivariance is the statement $R(\bar Z,Z)=\overline{R(Z,\bar Z)}$ for a real-analytic function of $(Z,\bar Z)$; it holds because the non-holomorphic dependence enters only through the real weight $\Lambda_1$.
- (3.2): on $C_1$, $2Z-1\le-3$ is on the cut of $\operatorname{arccosh}$; $w=\operatorname{arccosh}|2Z-1|\pm i\pi$ on either side, and $x=e^{-w}=-e^{-\operatorname{Re}w}$ is the same real number from both sides, so $R$ is continuous and real on $C_1$ whatever the side convention.
- The second-order data of the vertex-section maps (which differ from the plumbing maps by $R$, 052 §2C) are not packaged by the sister module; their equivariance follows from (3.1) only if the construction $(S,R)\mapsto F_a$ has real coefficients, which is expected (it is built from real-affine wall conditions) but not checked here.

### Result

$$\boxed{\ F_a(\bar w;\bar Z)=\overline{F_a(w;Z)},\ \ \rho_a(\bar Z)=\rho_a(Z),\ \ S_0(\bar Z)=\overline{S_0(Z)},\ \ R(\bar Z,Z)=\overline{R(Z,\bar Z)},\ \ \Lambda_1(\bar Z)=\Lambda_1(Z)\ }$$

identically on $T\cup\bar T$, both $\beta$; the conj-transported section is given by the same closed forms and glues across $C_1$.

### Verification

Script part 2: `C1.2-maps` ($q$ and $F_{1..4}$ at 400 random complex $w$, $|w|\sim0.15$: residual $0$, i.e. exact in floating point), `C1.2-radii` (closed form and from the maps: $0$), `C1.2-derivs` ($|F_1'(0)-S_0|\le5\times10^{-14}$, $|F_4'(0)-(Z-1)S_0|\le10^{-12}$), `C1.3-equiv` ($S_0,R,\Lambda_1$: $0$), `C1.3-mirrorC1` ($\max|\operatorname{Im}|\le6\times10^{-16}$), `C1.3-mirrorsC2C3` ($\le2\times10^{-16}$). Break leg: $S_\varepsilon=S_0+i\varepsilon|Z|/\beta$, $\varepsilon=0.05$ (an imaginary term even in $Z\to\bar Z$, hence odd under the rule) fails equivariance and reality on $C_1$. The exact zeros reflect that IEEE complex arithmetic and the C99 branch conventions are themselves conj-symmetric; the break legs show the checks can fail.

## Step 4 – (iii) Measure, level-0 integrand and tile sum

### Setup

A1–A3. Block-local: the level-0 tachyon state $T(k)=c_1\bar c_1|k\rangle$; its conjugate $T(k)^\ddagger=\epsilon\,T(-k)$ for real $k$, $\epsilon=\pm1$ fixed by (C1)/(C3) of 028 (hermitian conjugation reverses the momentum; BPZ does not). The tile contribution (044 A5): $\mathcal I_g(k;Z)=\prod_a\rho_a(Z)^{\alpha'k_{\sigma_g^{-1}(a)}^2/2-2}\,\mathrm{KN}(\sigma_g^{-1}k;Z)$, $\mathrm{KN}(k;Z)=|Z|^{\alpha'k_1\cdot k_4}|1-Z|^{\alpha'k_2\cdot k_4}$, powers of positive reals defined by $x^p=e^{p\log x}$.

### Derivation

Measure. $\mathrm d^2Z=2\,\mathrm d\operatorname{Re}Z\,\mathrm d\operatorname{Im}Z$ is a positive density; $Z\to\bar Z$ is an isometry of $\mathbb C$ with Jacobian $-1$, so as densities
$$\int_{\bar T}f(Z)\,\mathrm d^2Z=\int_Tf(\bar Z)\,\mathrm d^2Z.\tag{4.1}$$
(The orientation reversal is absorbed by the $b\bar b$ insertion of the measure 2-form; at level 0 that factor is folded into the $-2$ of the dressing exponent, 044 A7, and is a positive density.)

Integrand. By (3.1) the radii are conj-invariant and $|Z|,|1-Z|$ are, so
$$\mathcal I_g(k;\bar Z)=\mathcal I_g(k;Z),\qquad \mathcal I_g(\bar k;Z)=\overline{\mathcal I_g(k;Z)},\qquad \mathcal I_g(k;Z)>0\ \ (k\text{ real}).\tag{4.2}$$
Tile sum. With (4.1), (4.2) and the six conj pairs of step 2,
$$\{T(k_1)\cdots T(k_4)\}=C\sum_{h\in S_3}\Bigl[\int_T\mathcal I_h+\int_{\bar T}\mathcal I_{h\,\mathrm{conj}}\Bigr]=2C\sum_{h\in S_3}\int_T\mathcal I_h(k;Z)\,\mathrm d^2Z,\tag{4.3}$$
conjugate tiles add (`SL: R44`, here at level 0). For real momenta each term is positive, $C$ is a real normalisation, so the block is real; and since $\mathcal I_h$ is even in $k$,
$$\{T(k_1)\cdots T(k_4)\}^*=\{T(k_1)\cdots T(k_4)\}=\epsilon^4\{T(-k_1)\cdots T(-k_4)\}=\{T(k_1)^\ddagger\cdots T(k_4)^\ddagger\}.\tag{4.4}$$
For complex momenta, $\{\cdots\}(\bar k)=\overline{\{\cdots\}(k)}$ by (4.2).

### Commentary

- (4.3)–(4.4): the level-0 block is real *tile by tile*. It would stay real with a tile removed or with the deformed $S_\varepsilon$ (only $|S|$ enters the radii). So the level-0 tachyon block, the order at which every level-0 number of this project is computed, satisfies $\ddagger$-equivariance for a reason that does not use inputs I1–I3: it cannot test PH6 (b). This is recorded as check `C1.4-blind`.
- To make I1–I3 load-bearing, part 4 of the script adds a phase-sensitive probe: primaries of weights $(\bar h_a+s_a,\bar h_a)$, integer spins $s_a$, real $\bar h_a$, inserted in the section's frames $F_a'(0)=\kappa_aS_0$, times a plane correlator $\prod_{ab}|z_{ab}|^{2\gamma_{ab}}(z_{ab}/|z_{ab}|)^{m_{ab}}$ with integer $m_{ab}$ (the compact-boson form; $m_{ab}=n_aw_b+n_bw_a$), over the regulated pairs $(12),(14),(24)$. For such states the CFT reality input I5 is the statement that the correlator with real exponents satisfies $\overline{\langle\cdots\rangle(z)}=\langle\cdots\rangle(\bar z)$, momentum reversal leaving the bilinear exponents unchanged; the geometric inputs then make the pair $\int_T+\int_{\bar T}$ real. This is a representation of 028 §1's argument for all states whose frame transformation involves $F_a'(0)$ only (primaries), not for descendants or ghost insertions beyond level 0.

### Result

$$\boxed{\ \{T(k_1)\cdots T(k_4)\}^*=\{T(k_1)^\ddagger\cdots T(k_4)^\ddagger\}\quad\text{on the SL}(2,\mathbb C)\text{ declared section, all }\beta\ge\beta_{04},\ \text{real off-shell momenta}\ }$$

and, for integer-spin primaries of real weights, the conj pair of tiles gives a real contribution with the declared section — a corollary of C1.2/C1.3 and the Schwarz-symmetric correlator form, not an independent test of I1 — and fails to with either break leg.

### Verification

Script part 3: `C1.4-integrand` ($\mathcal I(\bar Z)-\mathcal I(Z)=0$, $\operatorname{Im}\mathcal I=0$ at real $k$, $\mathcal I(\bar k)-\overline{\mathcal I(k)}=0$; transcription against 044 (1.6) to $5\times10^{-15}$, at random complex off-shell $k\in\mathbb C^{4\times3}$), `C1.4-tilesum` (Monte Carlo pair sum on 400 points of $T$: imaginary part $0$), `C1.4-blind` (real with a tile removed and with $S_\varepsilon$). Part 4: `C1.5-probe` ($|\operatorname{Im}|/\text{scale}=0$ over 6 seeded spin/charge sets per $\beta$); break legs `C1.5-tile-removed` ($T$ alone) and `C1.5-S-odd` (pair with $S_\varepsilon$) fire.

## Step 5 – Statement, scope, break legs

**Statement.** For the SL(2,C) declared section at $n=4$, $\beta\ge\beta_{04}$:

1. (I1, analytic; numerically confirmed) The contact region $\mathcal V_{0,4}$ is invariant under $Z\to\bar Z$; the tiling by $G=S_3\times\{1,\mathrm{conj}\}$ is consistent: conj is the reflection in the wall $C_1$, maps $T$ onto the tile $\bar T$ and permutes the 12 tiles in six pairs.
2. (I2, I3, analytic + numerical) The section data as packaged are conj-equivariant, the conj-transported section is the same closed forms at $\bar Z$, and it glues across the mirror $C_1$ (data real there).
3. (I4 + level 0) The level-0 tachyon block of $V_4$ is $\ddagger$-equivariant, equivalently real, at real off-shell momenta; conjugate tiles add.
4. (probe, a corollary of C1.2/C1.3 and the Schwarz-symmetric correlator form, not an independent test of I1) For integer-spin primaries the conj-paired tiles give real contributions; both break legs destroy this.

**Which clause of (H$_R$) is thereby established for this family.** The geometric half of 028 (C4) at $n=4$ — "invariance of the moduli region $\mathcal V_{0,4}$ and of its measure under complex conjugation of the moduli" — together with conj-equivariance of the section's local-coordinate data to first order ($F_a'(0)$) and of the plumbing maps to all orders. The full equivariance $V_4(A_i)^*=V_4(A_i^\ddagger)$ is established for the level-0 tachyon block (unconditionally, and trivially in the sense of C1.4) and, granted the CFT reality A4, for integer-spin primaries.

**Scope – what stays a hypothesis (PH6 unchanged there).**

- Higher levels: descendants need the vertex-section maps beyond first order, $F_a''(0),\dots$, which on $T$ differ from the plumbing maps through $R$ (052 §2C). $R$'s equivariance is established (C1.3); the construction $(S_0,R)\mapsto F_a$ is not packaged, and its conj-equivariance is expected (real-affine wall conditions, real weight) but not checked.
- Ghost insertions: the $b\bar b$ measure 2-form and its orientation behaviour under conj are argued (4.1) and are absorbed into the positive dressing at level 0 only; the general statement, including the odd-state sign conventions of PH7, is not re-derived.
- The CFT reality input (Sonoda–Zwiebach H5) itself is cited, not derived (A4).
- $n\ge5$: nothing here. R46 uses PH6 at $n=4,5$; only its $n=4$ leg gains support.

**Break legs** (all fire): a non-real Möbius map does not commute with conj; a parameter value below $\beta_{04}$ breaks the unit-disc inclusion; one tile (the conj tile) removed makes the union non-invariant and the probe non-real; $S_\varepsilon=S_0+i\varepsilon|Z|/\beta$ fails (ii) and the probe; a wrong mirror assignment on the arcs fails. The level-0 block does **not** respond to the last two — that is the content of `C1.4-blind`, not a defect of the checks.

## Step 6 – Proposed ledger changes

**New row (proposed).** *PH6 (b) at $n=4$ for the SL(2,C) family (record 054).* For $\beta\ge\beta_{04}$ (exactly, for $\beta>\tfrac12$) the declared-section contact region $\mathcal V_{0,4}$ is conjugation invariant and tiled consistently by $G=S_3\times\{1,\mathrm{conj}\}$ (conj = reflection in the wall $C_1$; 12 tiles in six conj pairs; the unit-disc inclusion $\operatorname{dist}(0,\partial E_\beta)\ge1$ is exactly $\beta\ge\beta_{04}$); the section data ($q$, plumbing $F_a$, $\rho_a$, $S_0$, $R$, $\Lambda_1$) are conj-equivariant identically, the conj-transported section equals the closed forms at $\bar Z$ and glues across $C_1$; the level-0 four-tachyon contact term is real (equivalently $\ddagger$-equivariant) at real off-shell momenta, conjugate tiles adding — tile by tile, so level 0 does not test the geometric input; for integer-spin primaries under the CFT reality input, the conj tile pairs are real – a corollary of the frame equivariance, checked numerically as a phase-sensitive probe that, unlike the level-0 block, fails when the conj tile is dropped or $S_0$ is deformed by $i\varepsilon|Z|/\beta$. Scope: $n=4$; first-order section data (descendants need the unpackaged $(S_0,R)\mapsto F_a$); ghost measure argued, not derived; CFT reality (H5) cited. Status: `Proven – Verified` for the geometric statements and the level-0 block (analytic, `codes/verify-ph6-conjugation-n4.py` 45/45, 14 break legs, seed 20260926); the probe clause conditional on the CFT reality input already inside PH6's statement.

**PH6 status change (proposed wording):** `supported at n=4 for the SL(2,C) family (R…: region, tiling, first-order section data and plumbing maps proven; level-0 block real tile by tile, hence blind); open: descendant-level frame data, b-ghost measure, H5 itself as a CFT input, n≥5`.

## Addendum 2026-11-10 — external review (SL(2,C) project)

Source: external review, SL(2,C) vertices and ghost-dilaton project, 2026-11-10 (`SL:` report `critic-import-076-20261110T171506`, findings F1 and F5), passed on in `inbox/done/2026-11-10-sl2c-vertices-ghost-dilaton-import-review-findings.md`, and the orchestrator's hand check of the converse (brief `agent/briefs/active-computator-import-review-addenda-20261110T183258.md`, premise 3), re-read here step by step.
Scope and wording corrections; no result, number or check output of this record changes.
The text above this heading is not edited; the readings below supersede the wording at the places listed.

### B.1 Step 2 (d): the unit-disc inclusion is sufficient, not necessary

*Statement corrected.* Step 2 (d) (l. 80, l. 84) says that the reduction $\mathrm{FD}\cap\mathcal V^{\rm ind}_{0,4}=\mathrm{FD}\cap E_\beta$ "holds iff the unit disc lies in $E_\beta$".
The "only if" is false.
**For every $\beta>\tfrac12$**: $\mathrm{FD}\cap\mathcal V^{\rm ind}_{0,4}=\mathrm{FD}\cap E_\beta$.

*Proof (hand check, premise 3 of the brief; re-checked).* $\mathcal V^{\rm ind}_{0,4}\subset E_\beta$ by (2.1).
Conversely let $Z\in\mathrm{FD}\cap E_\beta$, so $|Z|\ge1$.
(i) $1/Z=\bar Z/|Z|^2$ lies on the segment from $0$ to $\bar Z$. $\bar Z\in E_\beta$ by the conjugation symmetry (step 2 (b)). $0\in E_\beta$ for $\beta>\tfrac12$: $E_\beta$ is centred at $\tfrac12$ with real semi-axis $a=\beta^2+1/(16\beta^2)>\tfrac12$ (AM–GM, equality only at $\beta=\tfrac12$, where $b=0$). $E_\beta$ is convex, so $1/Z\in E_\beta$.
(ii) $E_\beta$ is symmetric under $Z\to1-Z$ (centre $\tfrac12$ on the real axis), so $1-Z\in E_\beta$, $|1-Z|\ge1$ on FD, and (i) applied to $1-Z$ gives $1/(1-Z)=\overline{(1-Z)}/|1-Z|^2\in E_\beta$.
Hence $Z\in\mathcal V^{\rm ind}_{0,4}$. The $G$-invariance of $\mathcal V^{\rm ind}_{0,4}$ in (d) used only (b) and the $S_3$ symmetry and holds for all $\beta$, so the tiling $\mathcal V^{\rm ind}_{0,4}=\bigcup_gg(T)$, the conjugation invariance (2.3), the six-pair structure and the arcs of (e) hold for every $\beta>\tfrac12$ ($b>0$ requires $\beta>\tfrac12$ anyway).
The closed form $\operatorname{dist}(0,\partial E_\beta)=a-\tfrac12$ and the equivalence "unit disc $\subset E_\beta$ $\Leftrightarrow$ $\beta\ge\beta_{04}$" stay correct; they describe a sufficient condition for the reduction, with a different role below.

*Role of $\beta_{04}$.* Per the sender, $\beta_{04}=\tfrac12+1/\sqrt2$ is the threshold for pairwise disjoint Feynman regions (the $s$-, $t$-, $u$-channel regions, the images of the exterior of $E_\beta$), not a condition of the tiling. One direction checked here in one line: if the unit disc lies in $E_\beta$ then $Z\notin E_\beta$ forces $|Z|>1$, so $1/Z\in$ unit disc $\subset E_\beta$, i.e. the $s$- and $t$-regions do not meet; the necessity of $\beta\ge\beta_{04}$ for disjointness is the sender's statement and is not examined here.
Consequently `SL: R7` as quoted in A2 (l. 37) and T (l. 64), "$\mathrm{FD}\cap\mathcal V_{0,4}=\mathrm{FD}\cap E_\beta$ for $\beta\ge\beta_{04}$", is true but not sharp.

*Check.* `C1.1-tiling` was run at the standard parameter values of the companion construction only, both above $\beta_{04}$ and also above $\tfrac12$, so it cannot fail for a wrong $\beta_{04}$ and does not test the threshold; the break leg "$\beta=0.9<\beta_{04}$ breaks the unit-disc inclusion" (l. 102, l. 196) is a break of the disc check `C1.1-disc` only, not of the tiling (at $\beta=0.9>\tfrac12$ the tiling holds by the proof above). The script is not edited or re-run.

### B.2 Section data: strict inequality (sender's statement, not re-derived)

The sender reports that the section data of the declared section exist for $\beta>\beta_{04}$ strictly: at $\beta=\beta_{04}$ the corner $Z=-1$ gives $1/R=0$ from the wall conditions and a nonzero value from the sewing datum.
Recorded as the sender's statement; not re-derived here and not checked against the sister's module.
Where it bears: the clauses of this record that use the section data (C1.2, C1.3, C1.4, C1.5 and their parents, A3 "$\beta\ge\beta_{04}$" at l. 38, the statement at l. 180) carry $\beta\ge\beta_{04}$ as the scope; they are to be read with $\beta>\beta_{04}$ strictly.
The numerics at the standard parameter values are unaffected, and so is C1.1 (region and tiling), which needs only $\beta>\tfrac12$.

### B.3 Places to read as corrected

Grep `beta_{04}\|unit.disc\|unit disc` over the record; for each, the reading after this addendum.
- l. 37 (A2) and l. 64: "for $\beta\ge\beta_{04}$" → true, not sharp; region and tiling for every $\beta>\tfrac12$ (B.1).
- l. 38 (A3), l. 180 (Statement): scope $\beta\ge\beta_{04}$ of the section data → strictly $\beta>\beta_{04}$ (B.2); the region claims (item 1 of l. 180's list) → $\beta>\tfrac12$.
- l. 45 (**C1.1.3**) "reproduce (2.1) exactly for $\beta\ge\beta_{04}$ (unit disc inside $E_\beta$, analytic)": statement corrected to every $\beta>\tfrac12$; the justification changes from "unit disc inside $E_\beta$" (sufficient) to the convexity argument of B.1; dependents C1.1 (l. 42), C1 (l. 41) and C1.2–C1.5 (l. 46–49) keep their statements within the scope of B.2, and C1.4/C1.5, which sit on the section data, carry $\beta>\beta_{04}$.
- l. 80 and l. 84 (step 2 (d)): "iff the unit disc lies in $E_\beta$" → "if"; the distance formula and "iff $\beta\ge\beta_{04}$" for the disc inclusion stand.
- l. 91 (commentary): "(d) is the only place the specific family enters (the ellipse size)" → the ellipse size enters the Feynman-region disjointness, not the tiling.
- l. 96 (boxed result of step 2, "$(\beta\ge\beta_{04})$") and l. 98 ("including the unit-disc inclusion"): the boxed statement holds for $\beta>\tfrac12$; the disc inclusion is an additional true fact.
- l. 102 and l. 196: break leg $\beta=0.9$ breaks the disc inclusion only (B.1, Check).
- l. 170 (boxed result of step 4, "all $\beta\ge\beta_{04}$"): read $\beta>\beta_{04}$ (B.2); the level-0 block is real tile by tile and the statement itself does not use the section.
- l. 200 (step 6, proposed row; R56 was promoted from it): "For $\beta\ge\beta_{04}$ (exactly, for $\beta>\tfrac12$) … the unit-disc inclusion … is exactly $\beta\ge\beta_{04}$" → region and tiling for all $\beta>\tfrac12$; section-data clauses for $\beta>\beta_{04}$; the disc inclusion is not a condition of either (annotation below).
- l. 8 (Status) mentions the "$\beta>\tfrac12$ qualifier" of the fix pass; it is the qualifier now made exact by B.1.
- Script `codes/verify-ph6-conjugation-n4.py` l. 6 (docstring): "the unit disc lies in the ellipse (beta >= beta_04)" is a check statement for `C1.1-disc`, correct as such.

Statement or justification: the statement of C1.1.3 is corrected (wider range), its justification replaced (convexity instead of the disc inclusion); step 2 (d) changes its justification and its "iff"; the scope $\beta>\beta_{04}$ of B.2 changes statements of C1.2–C1.5 by the sender's report.

### Proposed ledger annotation for R56

An external review (SL(2,C) vertices and ghost-dilaton project, 2026-11-10; `SL:` report `critic-import-076-20261110T171506`, F1 and F5) and the orchestrator's hand check found the scope's $\beta\ge\beta_{04}$ misattributed. The reduction $\mathrm{FD}\cap\mathcal V^{\rm ind}_{0,4}=\mathrm{FD}\cap E_\beta$, hence the conjugation invariance of the region and its tiling by $G=S_3\times\{1,\mathrm{conj}\}$ (R56's first Status line), holds for every $\beta>\tfrac12$: for $Z\in\mathrm{FD}\cap E_\beta$, $|Z|\ge1$, and $1/Z=\bar Z/|Z|^2$ lies on the segment from $0$ to $\bar Z$, with $\bar Z\in E_\beta$ by conjugation symmetry and $0\in E_\beta$ for $\beta>\tfrac12$, so $1/Z\in E_\beta$ by convexity, likewise $1/(1-Z)$ through $Z\to1-Z$. The unit-disc inclusion ($\beta\ge\beta_{04}$) is sufficient for the reduction, not necessary; $\beta_{04}$ is the threshold for pairwise disjoint Feynman regions, not a condition of the tiling, and the check `C1.1-tiling` (run at the standard parameter values) does not test it. Per the review, the section data of the declared section exist for $\beta>\beta_{04}$ strictly (at $\beta_{04}$ the corner $Z=-1$ gives $1/R=0$ from the wall conditions and a nonzero value from the sewing datum; the sender's statement, not re-derived here), so the clauses of the Scope that use the section data read $\beta>\beta_{04}$. No result or number changes; the numerics at the standard parameter values are unaffected.

### Status of the 2026-11-10 addendum

Status line of this addendum: complete 2026-11-10; next: orchestrator (ledger clerk copies the annotation for R56).
