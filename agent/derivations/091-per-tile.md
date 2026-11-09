---
description: Per-tile step of R86 C3.4 - under PH34, mu_1 and mu_2 vanish only on a Lebesgue-null subset of the vertex region (argument from the s-arc of the fundamental tile and the S_3 x Z_2 transport; checked, 25/25); fix pass 2026-10-10 applied
---

# Record 091 – The per-tile step: $\mu_i$ vanishes on a null subset of the vertex region (argument), checked against record 089

## Status

complete after fix pass (2026-10-10, critic-091 iteration 1: #13, #3, #4, #7, #8, #10, #14 applied, results unchanged); the companion package used as input is v2.0.1; `codes/verify-per-tile.py` 25/25 PASS (re-run 2026-10-10 after a docstring edit); next: orchestrator – the proposed R86 / PH34 lines at the end.

## Task and objective

- **Literal task.** Write the per-tile step of R86 C3.4 as an argument: from PH34 (section real-analytic on each tile, continuous up to $\partial\mathcal V_{0,4}$), the parameter point of the theory's cubic vertex ($\lambda=\tfrac12$, $\gamma'=\beta$, exact), C3.2 restated (boundary matching on $\partial_s$) and the $S_3\times\mathbb Z_2$ equivariance of the section, show that the zero set of $\mu_i$ ($i=1,2$) in the vertex region has measure zero. Outline from `agent/reports/critic-fable-decisions-sec6-20261004T190300.md` Q2 / #4, declared as such and checked. Compare with record 089 (the zero at $Z=\tfrac12$).
- **Motivating objective.** R86's statement that the refutation of PH31 at $\lambda=0$ is a model artefact rests, at the a.e. strength, on this step; 089 gives a table, this record the argument, so that R86 rests on both.
- **Answer in one line.** Under PH34, for $i=1,2$, $\mu_i\ne0$ off a Lebesgue-null subset of $\mathcal V_{0,4}$ (and of $Q_V$): on the fundamental tile the six pole-at-partner conditions fail on its $s$-arc, where the glued $\lambda=\tfrac12$ halves put no pole at any puncture, hence on an open set (continuity), hence off a null set (analyticity on that one tile); the $S_3\times\mathbb Z_2$ transport carries every tile to one of these six conditions. Zeros on walls and corners are not excluded, and one exists ($Z=\tfrac12$, 089).

## Conventions and assumptions

- **A1** Package frame (089 A2): punctures $(z_1,z_2,z_3,z_4)=(0,1,\infty,Z)$, label 3 in the chart $t=1/z$; 2-jet $(a,c)$ of a Möbius map $F$ at its puncture $z_0$, $c=-1/(2(F(\infty)-z_0))$; $R_a:=F_a(\infty)$, the pole of the coordinate at puncture $a$.
- **A2** Tiling (ledger R7, package `in_closed_FD`, `tile_of`): $\mathrm{FD}=\{\Im Z\ge0,\ |Z|\ge1,\ \Re Z\le\tfrac12\}$, walls $C_1$ (real axis, $Z\le-1$), $C_2$ ($\Re Z=\tfrac12$), $C_3$ ($|Z|=1$), $C_4$ (the $s$-ellipse, $|q|=1$). $T_0:=$ interior of $\mathrm{FD}\cap\mathcal V_{0,4}$. The twelve tiles are $g\cdot T_0$, $g=(\pi,\epsilon)\in S_3\times\mathbb Z_2$ ($\pi$ fixes label 4), acting by relabelling (old label $i$ becomes $\pi(i)$) and conjugation.
- **A3** $\beta>\beta_{04}=\tfrac12+\tfrac1{\sqrt2}$ (R7); the theory's $\beta\ge\tfrac32$; checks at $\beta=\tfrac32$ and $2$.
- **A4** The actual $\mathcal V_4$ is the section fixed by the construction in record 080 (080 A7, R86 Scope), $S_4$-symmetric (080 A5) and equivariant under complex conjugation (used for the $\epsilon=1$ tiles in (1.3)); the theory's cubic vertex is $\mathcal V_3'(\lambda=\tfrac12,\gamma'=\beta)$ (cubic vertex maps in one frame, not yet public).
- **Input (reviewed).** The companion project's package v2.0.1 (ledger PH34), imported by path, not edited.

## Step list

- S1 Tiling (§1): $T_0$ open and connected, touching $\partial_s$ along an arc with interior and no other channel boundary; the channel touched by each $g\cdot T_0$.
- S2 Transport (§1): $\{\mu_1=0\}\cap g\cdot T_0=g\cdot\{P_{ab}\}$ on $T_0$, $(a,b)=(\pi^{-1}(1),\pi^{-1}(2))$; likewise $\mu_2$; the six ordered pairs of $\{1,2,3\}$ as affine conditions on the $c_j$.
- S3 Boundary values on $\partial_s$ (§2): glued $\lambda=\tfrac12$ halves; no pole sits at a puncture; limiting case $\mu_i=\tfrac1{2\beta}$.
- S4 Continuity up to $\partial_s$ (§3, PH34): non-vanishing on an open subset of $T_0$ for every pair.
- S5 Analyticity on $T_0$ (§3, PH34): null zero set; transport; walls; $Q_V$.
- S6 Comparison with 089; what is not covered (§4).

## Claim tree

- **A1–A4** as above.
- **PH34** (ledger; supported, the companion package v2.0.1): the section is real-analytic on each of the twelve tiles; at $\partial\mathcal V_{0,4}$ the $c_j$ join the channel maps $C^1$. Used here only on $T_0$: continuity of $c_1,c_2,c_3$ up to the $s$-arc (C3, C4) and real-analyticity on the open $T_0$ (C5).
- **C0 (root)** Under PH34: for $i=1,2$ the zero set of $\mu_i$ in $\mathcal V_{0,4}$ is Lebesgue-null in $Z$, and in $Q_V$ in $q$ (R86 C3.4 at the a.e. strength, per-tile step included). Inputs: the $S_4$-symmetry and the complex-conjugation equivariance of the section (A4) and the parameter point $\lambda=\tfrac12$, $\gamma'=\beta$ (exact). Zeros are not excluded: the symmetry-forced zero at $Z=\tfrac12$ (089) on the closure is consistent with C0, and "nowhere zero" is not claimed. [by C1–C5; C6 for the consistency]
  - **C1** $T_0$ is open and connected and, for $\beta>\beta_{04}$, touches $\partial_s$ along an arc with non-empty interior and no other channel boundary; $g\cdot T_0$ touches the boundary of the channel containing $\{\pi(3),4\}$. [by A2, A3; eq. (1.1)–(1.2)] [check: C1-arc, C1-T0-only-s, C1-tile-channel]
  - **C2** $\{\mu_1=0\}\cap g\cdot T_0=g\cdot(\{P_{\pi^{-1}(1)\pi^{-1}(2)}\}\cap T_0)$, likewise $\mu_2$ with the pair reversed; the twelve tiles need exactly the six conditions (1.4) on $T_0$, affine in $c_1,c_2,c_3$. [by A1, A4 ($S_4$-symmetry and conjugation equivariance), 080 (1.6); eq. (1.3)–(1.4); step from the critic's outline, checked] [check: C2-transport]
  - **C3** Under PH34, on $\partial_s\cap\overline{T_0}$ the coordinates are the glued $\lambda=\tfrac12$, $\gamma'=\beta$ halves' and no pole sits at any puncture: $E_{ab}\ne0$ there for all six pairs; limiting value $\mu_{1,2}=\tfrac1{2\beta}$. [by A3, A4 (parameter point), PH34 (last clause), 032 (1.2) (the special-leg coordinate $w=2\beta(1-z)/(1+z)$), 089 C3.1 (the package's $s$-channel maps are the glued halves); eq. (2.1)–(2.2); by check: C3-boundary-package (the package's channel maps are the glued halves, six pairs)] [check: C3-boundary-exact, C3-boundary-exact-mu] — independently of the package, the boundary values for the actual vertex are R86 C3.2 (Argued).
  - **C4** Under PH34, each $E_{ab}$ is non-zero on a non-empty open subset of $T_0$ adjacent to the $s$-arc. [by PH34 (continuity at $\partial\mathcal V_{0,4}$), C1, C3; eq. (3.1)] [check: C4-continuity]
  - **C5** Under PH34, $\{\mu_i=0\}\cap\mathcal V_{0,4}$ is null in $Z$ and $\{\mu_i=0\}\cap Q_V$ null in $q$, $i=1,2$. [by PH34 (analyticity on $T_0$), C1, C2, C4; eq. (3.2)–(3.4)]
  - **C6** Consistency with 089: $E_{13}$, $E_{31}$ vanish (linearly) at the corner $Z_0=-1$ of $\overline{T_0}$, the pull-back of 089's zero at $Z=\tfrac12$ by the tiles 132, 231, forced by the $(24)$-automorphism; it lies on the boundary of $T_0$, at distance $a-\tfrac32>0$ from the $s$-arc, and touches neither input of C4–C5; C5 is weaker than 089's numerical no-zero statement on the open $Q_V$ and consistent with it. [by A4, C1, C2; eq. (4.1); 089 C2.4] [check: C6-corner-zero]

Open gaps: none
Hypotheses in force: PH34 (C3, C4, C5, hence C0); R86 C3.2 (Argued) is a package-independent second support of C3's boundary values, not needed under A4 + PH34.

## §1 (C1, C2) – The tiles and the transport of the condition

\subsection*{Setup}
A1, A2, A3. For a four-punctured sphere $\Sigma$ with Möbius local coordinates $F_j$, write $P_{ab}(\Sigma)$ for "the pole of the coordinate at puncture $a$ sits at puncture $b$", $R_a=z_b$. By 080 (1.6), $\mu_1=0\iff P_{12}$ and $\mu_2=0\iff P_{21}$ (the CKV of the $s$-pair $(1,2)$, any chart).

\subsection*{Derivation}
*The fundamental tile.* $T_0=\{\Im Z>0,\ \Re Z<\tfrac12,\ |Z|>1\}\cap\{\text{inside the }s\text{-ellipse}\}$, ellipse $Z=\tfrac12+a\cos\varphi+\mathrm ib\sin\varphi$, $a=\beta^2+\tfrac1{16\beta^2}$, $b=\beta^2-\tfrac1{16\beta^2}$ (package `ellipse_axes`, R7). On the arc $\varphi\in[\tfrac\pi2,\pi]$, with $c=\cos\varphi$ and $a^2-b^2=\tfrac14$,
$$
|Z|^2=\tfrac14+b^2+ac+\tfrac{c^2}4,\qquad \partial_c|Z|^2=a+\tfrac c2>0\ \Rightarrow\ \min|Z|^2=(a-\tfrac12)^2>1\iff a>\tfrac32\iff\beta>\beta_{04}. \tag{1.1}
$$
So for $\beta>\beta_{04}$ the $s$-arc $C_4\cap\overline{T_0}$ runs from $C_1$ (at $\tfrac12-a<-1$) to $C_2$ (at $\tfrac12+\mathrm ib$, $b>\tfrac{\sqrt3}2$) inside $|Z|>1$: an arc with non-empty relative interior. ($\beta_{04}$ is exactly the value at which the ellipse passes through the corner $Z=-1$: $a=\tfrac32\iff\beta^2=\tfrac{(1+\sqrt2)^2}4$.) $T_0$ is connected: each vertical slice $\{y:\ x+\mathrm iy\in T_0\}$ is the interval $(\ell(x),u(x))$ with $\ell(x)=\sqrt{1-x^2}$ for $|x|<1$, $0$ for $x\le-1$, $u(x)$ the upper half of the ellipse, both continuous on $(\tfrac12-a,\tfrac12)$ and $\ell<u$ by (1.1); a region between two continuous graphs is connected. $\overline{T_0}$ meets neither the $t$- nor the $u$-channel region: $|Z-1|\ge|Z|\ge1$ on $\overline{\rm FD}$, while the $u$-region is the image of the exterior of the $s$-ellipse under $Z\mapsto1/Z$, hence inside $|Z|<1/(a-\tfrac12)<1$, and the $t$-region its image under $Z\mapsto1-Z$, inside $|Z-1|<1$ (machine check below: $\min|q_t|$, $\min|q_u|>1$ on $\overline{T_0}$). $\tag{1.2}$

*The twelve tiles.* $g=(\pi,\epsilon)$ relabels old label $i$ as $\pi(i)$ ($\pi(4)=4$) after conjugation if $\epsilon=1$. $\partial_s$ is the boundary of the Feynman region of the pairing $\{12|34\}$; $g$ maps it to the boundary of the Feynman region of $\{\pi(1)\pi(2)|\pi(3)4\}$, so $g\cdot T_0$ touches exactly one channel boundary, that of the pairing containing $\{\pi(3),4\}$ ($s$: $\pi(3)=3$; $t=\{13|24\}$: $\pi(3)=2$; $u=\{14|23\}$: $\pi(3)=1$).

*Transport of the condition.* By $S_4$-symmetry of the section (080 A5; for the package, the section on every tile is by construction the relabelling of the section on the fundamental domain), the coordinate at puncture $\pi(i)$ of $g\cdot\Sigma_0$ is $N\circ F_i$ (after conjugation if $\epsilon=1$), $F_i$ the coordinate at puncture $i$ of $\Sigma_0$, $N$ the Möbius normalisation (up to a rotation of $W$, which moves no pole). $N$ and conjugation carry poles to poles and punctures to punctures, so
$$
P_{12}(g\cdot\Sigma_0)\iff P_{\pi^{-1}(1)\pi^{-1}(2)}(\Sigma_0),\qquad P_{21}(g\cdot\Sigma_0)\iff P_{\pi^{-1}(2)\pi^{-1}(1)}(\Sigma_0), \tag{1.3}
$$
i.e. $\{\mu_1=0\}\cap g\cdot T_0=g\cdot\big(\{P_{ab}\}\cap T_0\big)$, $(a,b)=(\pi^{-1}(1),\pi^{-1}(2))$.

*Enumeration* (each row for $\epsilon=0,1$; tile name as in 089: the first three entries of $\pi$):

| tile $g\cdot T_0$ | $\pi(3)$ | channel boundary touched | $\mu_1=0$ on it $\iff$ on $T_0$ | $\mu_2=0$ $\iff$ | Klein class on $T_0$ |
| --- | --- | --- | --- | --- | --- |
| 123 | 3 | $\partial_s$ | $P_{12}$ | $P_{21}$ | $s$ ($\{12\vert34\}$) |
| 213 | 3 | $\partial_s$ | $P_{21}$ | $P_{12}$ | $s$ |
| 132 | 2 | $\partial_t$ | $P_{13}$ | $P_{31}$ | $t$ ($\{13\vert24\}$) |
| 312 | 2 | $\partial_t$ | $P_{23}$ | $P_{32}$ | $u$ ($\{14\vert23\}$) |
| 321 | 1 | $\partial_u$ | $P_{32}$ | $P_{23}$ | $u$ |
| 231 | 1 | $\partial_u$ | $P_{31}$ | $P_{13}$ | $t$ |

Four tiles touch each channel boundary. On $T_0$ all six ordered pairs of $\{1,2,3\}$ occur, never label 4. In the package frame the punctures $1,2,3$ sit at the fixed points $0,1,\infty$, so the six conditions are affine in the second-order coefficients (A1: $R_a-z_a=-1/2c_a$; label 3 in $t=1/z$):
$$
P_{12}:1+2c_1=0,\quad P_{13}:c_1=0,\quad P_{21}:1-2c_2=0,\quad P_{23}:c_2=0,\quad P_{31}:c_3=0,\quad P_{32}:1+2c_3=0. \tag{1.4}
$$
The last column: the Klein relabellings act on each surface by automorphisms, so $P_{12}\iff P_{21}\iff P_{34}\iff P_{43}$ etc.; the six conditions reduce to three functions on $T_0$, one per pairing – 089 C2.3's "three functions on the FD". The argument below does not need this reduction.

\subsection*{Commentary}
The critic's outline (critic-fable-decisions-sec6 Q2) states (1.3) with the pair $\pi_g^{-1}(1,2)$ and "every tile touches exactly one channel boundary"; both are taken from it and checked here (`C2-transport`, `C1-tile-channel`). The direction $\pi^{-1}$ matters for the 3-cycles; the break legs use $\pi$ and fire. Only the contact of $T_0$ with $\partial_s$ is used below; the column "channel touched" is not used by the argument (the alternative route – each tile's own channel boundary, with the channel maps there – gives the same result, since the $t$, $u$ channel maps are relabellings of the $s$ ones).

\subsection*{Result}
[C1] $T_0$ is open, connected, and touches $\partial_s$ along an arc with interior, and no other channel boundary; tile $g\cdot T_0$ touches the boundary of the channel of $\{\pi(3),4\}$. [C2] $\{\mu_1=0\}\cap g\cdot T_0=g\cdot(\{P_{\pi^{-1}(1)\pi^{-1}(2)}\}\cap T_0)$ and likewise for $\mu_2$; the twelve tiles need the six conditions (1.4) on $T_0$.

\subsection*{Verification}
`C1-arc` ((1.1) numerically on the arc: $\tfrac12-a=-1.778$, $b=2.222$, $\min|Z|=1.778$ at $\beta=\tfrac32$; $-3.516$, $3.984$, $3.516$ at $\beta=2$). `C1-T0-only-s` (85905 and 113298 points of $\overline{T_0}$: $\min|q_t|$, $\min|q_u|$ at each $\beta$: (companion value, not reproduced here)). `C1-tile-channel` (for each of the 12 $g$, a point of $T_0$ at $|q|=1\pm10^{-3}$ moved by $g$: inside lands in tile $g$ and in $\mathcal V_{0,4}$, outside in the Feynman region of the predicted channel; table above reproduced), `BREAK-C1-tile-channel` ($\pi^{-1}(3)$ in place of $\pi(3)$: fires). `C2-transport` (the Möbius-invariant $X_{abc}=[R_a,z_b;z_a,z_c]$, zero iff $P_{ab}$: $X_{123}(g\cdot Z_0)$ and $X_{213}(g\cdot Z_0)$ from the package's section on the tile against the pulled-back pair from its section on the fundamental domain at $Z_0$, conjugated for $\epsilon=1$; 40 random $Z_0\in T_0$ × 12 tiles, agreement to round-off), `BREAK-C2-transport` ($\pi$ for $\pi^{-1}$: deviation (companion value, not reproduced here); fires).

## §2 (C3) – Boundary values on the $s$-arc: no pole at a puncture

\subsection*{Setup}
A3, A4, §1. The surface on $\partial_s$ ($|q|=1$) is two copies of $\mathcal V_3'(\lambda,\gamma'=\beta)$ glued by $w_Aw_B=q$ at their special legs, $w=2\beta(1-z)/(1+z)$ (032 (1.2); 089 §1–2). Half: $f_0(W)=W/(\lambda W+\beta)$ at $z=0$, pole $f_0(\infty)=1/\lambda$; $f_\infty=1/f_0$ at $z=\infty$, pole $\lambda$. Labels (089 C1): $1,2$ = half A ($z=0,\infty$), $3,4$ = half B ($z=0,\infty$). That the vertex's coordinates on $\partial_s\cap\overline{T_0}$ are these glued maps with $\lambda=\tfrac12$: for the package's section, PH34's last clause ("the $c_j$ join the channel maps at $\partial\mathcal V_{0,4}$") together with 089 C3.1 (the package's $s$-channel maps are the glued $\lambda=\tfrac12$, $\gamma'=\beta$ halves); for the actual vertex independently of the package, R86 C3.2 restated (boundary matching through the geometric master equation, Argued). The value $\lambda=\tfrac12$ is exact for the cubic vertex.

\subsection*{Derivation}
In the global coordinate $w_A$ of the glued sphere:
$$
\begin{aligned}
z_1&=2\beta, & z_2&=-2\beta, & z_3&=\tfrac{q}{2\beta}, & z_4&=-\tfrac{q}{2\beta},\\
R_1&=2\beta\,\tfrac{\lambda-1}{\lambda+1}, & R_2&=-R_1, & R_3&=\tfrac{q}{R_1}, & R_4&=-\tfrac{q}{R_1};
\end{aligned}
\qquad \lambda=\tfrac12:\ R_1=-\tfrac{2\beta}3,\ R_3=-\tfrac{3q}{2\beta}. \tag{2.1}
$$
At $\lambda=\tfrac12$ the twelve differences $R_a-z_b$ ($a\ne b$) vanish only at
$$
R_1=z_2,\ R_2=z_1:\ \text{never};\qquad R_3=z_4,\ R_4=z_3:\ q=0;\qquad \text{the other eight}:\ q=\pm\tfrac{4\beta^2}3 . \tag{2.2}
$$
On $|q|=1$ none of them vanishes unless $\beta^2=\tfrac34$, excluded by A3 ($\beta_{04}^2\approx1.457$). Hence on $\partial_s\cap\overline{T_0}$ the six conditions (1.4) all fail: no coordinate has its pole at any puncture. The pole of $F_1$ sits at $z=2$ of half A, $w_A=-\tfrac{2\beta}3$ ($=-1$ at $\beta=\tfrac32$, on the special circle), at modulus $\tfrac{2\beta}3$ against $2\beta$ and $\tfrac1{2\beta}$ for the punctures.

*Limiting case.* In the circle frame $u=1/w_A$ ($u_{1,2}=\pm\tfrac1{2\beta}$), 080 (3.1) gives $\mu_1=\mu_2=\lambda/\beta$, i.e. $\tfrac1{2\beta}$ ($=\tfrac13$ at $\beta=\tfrac32$) on $\partial_s$: 089 (2.2), here re-derived from (2.1). At $\lambda=0$, $R_1=-2\beta=z_2$ for every $q$: the rigid $\alpha'_{\rm v}=0$ halves have the pole at the partner on all of $\partial_s$, and the boundary gives the continuity step nothing – the reason this argument was unavailable while PH33 stood.

\subsection*{Commentary}
(2.1): plumbing keeps each half's own coordinates; the glued surface is one sphere with coordinate $w_A$, half B's points enter through $w_A=q/w_B$. The pole of a Möbius coordinate is a point of that sphere, so (2.1) is global. (2.2): $R_1-z_3=0\iff q=-\tfrac{4\beta^2}3$, etc.; $|q|=\tfrac{4\beta^2}3>1$ for $\beta>\tfrac{\sqrt3}2$. The critic's outline gives "$w=-1$" and "$|w|=\tfrac13$": these are the $\beta=\tfrac32$ values of $-\tfrac{2\beta}3$ and $\tfrac1{2\beta}$. In the package frame the boundary values are $X_{abc}$ of the glued maps, with $|X_{abc}|$ bounded away from zero on the $T_0$ arc.

\subsection*{Result}
[C3] On $\partial_s\cap\overline{T_0}$ (and on all of $|q|=1$), for $\beta>\beta_{04}$, $R_a\ne z_b$ for all $a\ne b\in\{1,2,3,4\}$: each of the six conditions (1.4) fails there. Limiting value $\mu_{1,2}=\tfrac1{2\beta}$.

\subsection*{Verification}
`C3-boundary-exact` (sympy, $\lambda=\tfrac12$: the zero loci (2.2) for all 12 ordered pairs; $\min|R_a-z_b|=0.250$ on $|q|=1$ over 200 random $(\beta,\theta)$, $\beta\in(\beta_{04},4)$), `C3-boundary-exact-mu` ($\mu_1=\lambda/\beta$ exactly), `BREAK-C3-lambda0` ($R_1-z_2\equiv0$ at $\lambda=0$: the boundary step fails for the rigid model), `C3-boundary-package` (the package's $s$-channel maps on the $T_0$ arc, 25 angles × 6 pairs: $X_{abc}$ equals the sympy gluing to round-off; independent of 089 C3.1, which compared $c_{1,2}$, $|a_{1,2}|$ only).

## §3 (C4, C5) – From the arc into the tile, and from $T_0$ to $\mathcal V_{0,4}$

\subsection*{Setup}
§1, §2, PH34. $E_{ab}$ the affine functions of (1.4) on $T_0$ ($E_{12}=1+2c_1$, $E_{13}=c_1$, …): $E_{ab}(Z)=0\iff P_{ab}$.

\subsection*{Derivation}
*Open set (C4).* By PH34's last clause the $c_a$ of the section on $T_0$ extend continuously to $\partial_s\cap\overline{T_0}$ with the glued maps' values (only continuity is used, not the $C^1$ joining). Take $p$ in the relative interior of the $s$-arc (§1). By §2, $E_{ab}(p)\ne0$, so there is a disc $D\ni p$ with $E_{ab}\ne0$ on $D\cap(T_0\cup\text{arc})$; $D\cap T_0$ is non-empty and open ($p\in\overline{T_0}$). So each $E_{ab}$ is non-zero on a non-empty open $U_{ab}\subset T_0$; one $D$ serves all six pairs. $\tag{3.1}$

*Null set on $T_0$ (C5).* By PH34 the $c_a$, hence the $E_{ab}$, are real-analytic on the open, connected $T_0$ (§1). A real-analytic $f\not\equiv0$ on a connected open $U\subset\mathbb R^2$ has a Lebesgue-null zero set (standard; Mityagin, arXiv:1512.07276, gives the general case; for complex $E$ apply it to $|E|^2$). Proof in two variables: if $\{f=0\}$ had positive measure, some closed rectangle $Q=I_x\times I_y\subset U$ would meet it in positive measure; by Fubini a set $A\subset I_x$ of positive measure has slices $\{y:f(x,y)=0\}\cap I_y$ of positive measure; for $x\in A$ the one-variable analytic $y\mapsto f(x,y)$ (analytic on a neighbourhood of $I_y$) then has accumulating zeros and vanishes on $I_y$; for each $y\in I_y$, $x\mapsto f(x,y)$ vanishes on $A$, which accumulates, so $f\equiv0$ on $Q$, and on $U$ by the identity theorem ($U$ connected). By (3.1) and $T_0$ connected (§1), $\{E_{ab}=0\}\cap T_0$ is null for each of the six pairs. $\tag{3.2}$

*Transport.* $Z\mapsto g\cdot Z$ (`act_on_modulus`) is a Möbius or anti-Möbius map of the $Z$-sphere, a real-analytic diffeomorphism $T_0\to g\cdot T_0$; it maps null sets to null sets. By (1.3), $\{\mu_1=0\}\cap g\cdot T_0=g\cdot(\{E_{\pi^{-1}(1)\pi^{-1}(2)}=0\}\cap T_0)$: null, for each of the twelve $g$; likewise $\mu_2$. $\tag{3.3}$

*Walls and $Q_V$.* $\mathcal V_{0,4}\setminus\bigcup_g g\cdot T_0$ is the union of the tile walls (finitely many analytic arcs: images of $C_1$, $C_2$, $C_3$) and $\partial\mathcal V_{0,4}$: null. So $\{\mu_i=0\}\cap\mathcal V_{0,4}$ is null in $Z$, $i=1,2$. On $Q_V$, $\mu_i(q)$ is the same condition at $Z(q)=(q+4\beta^2)^2/16\beta^2q$ (089 (1.1); $P_{12}$ is intrinsic to the surface), $Z$ is holomorphic on $Q_V$ with $Z'(q)=0$ only at $q=\pm4\beta^2$, outside the open $Q_V$ (since $Z(4\beta^2)=1$ and $Z(-4\beta^2)=0$ are the centres of the $t$- and $u$-channel Feynman regions, so both points lie in those regions, not in $\overline{Q_V}$); a local diffeomorphism pulls null sets back to null sets, so $\{q\in Q_V:\mu_i(q)=0\}$ is null. $\tag{3.4}$

\subsection*{Commentary}
(3.1) is where the parameter point enters: at $\lambda=0$, $E_{12}$ and $E_{21}$ vanish on the whole arc and (3.1) gives nothing for the tiles 123, 213 (nor, by (1.3), for any $\mu_1$ condition pulled back to $P_{12}$, $P_{21}$). (3.2) is where analyticity enters, used only on $T_0$: analyticity on the other eleven tiles is not needed (transport (3.3) replaces it), nor across any wall or arc. Before the critic's outline, PH34's Scope listed "$\mu_i\not\equiv0$ on each tile" as missing; (3.1)–(3.3) supply it from the $s$-arc of one tile. A second route, not used: each tile's own channel boundary, where the $t$- or $u$-channel maps (relabellings of the $s$ ones) put no pole at a puncture by the same (2.2).

\subsection*{Result}
[C4] Each $E_{ab}$, $(a,b)$ an ordered pair of $\{1,2,3\}$, is non-zero on a non-empty open subset of $T_0$ adjacent to the $s$-arc. [C5] Under PH34, $\{\mu_i=0\}\cap\mathcal V_{0,4}$ ($i=1,2$) is Lebesgue-null in $Z$, and $\{\mu_i=0\}\cap Q_V$ is null in $q$.
$$
\boxed{\ \text{Under PH34 (with the parameter point }\lambda=\tfrac12,\gamma'=\beta\text{ and the }S_4\text{-symmetry of the section): }\mu_i\ne0\text{ at almost every point of }\mathcal V_{0,4}\ \text{and of }Q_V\ }
$$

\subsection*{Verification}
`C4-continuity` (the package's section at $q=(1+\varepsilon)e^{\mathrm i\theta}$, 13 angles of the $T_0$ arc, six pairs: $\max|X-X_{\rm boundary}|$ decreases linearly with $\varepsilon=10^{-2},\dots,10^{-5}$ at both $\beta$, because the boundary value is taken at $|q|=1$ while the point sits at $|q|=1+\varepsilon$; $|X|$ stays bounded away from zero), `BREAK-C4-wrong-pair` (the boundary value of $(a,c)$ for $(a,b)$: deviation (companion value, not reproduced here); fires), `C4-C1-join` (supporting: against the $s$-channel maps continued to the same $Z$ the deviation is $O(\varepsilon^2)$: PH34's $C^1$ joining holds for all six pairs on this arc, not only for $\mu_{1,2}$ as in 089 C3.4). The measure-theoretic steps (3.2)–(3.4) are proved by hand above and not machine-checked.

## §4 (C6) – Comparison with record 089, and what is not covered

*The zero at $Z=\tfrac12$.* 089 (3.2): $\mu_1=\mu_2=0$ at $Z=\tfrac12$ (on the fold circle, a corner of the tiles 132, 231 and conjugates), forced by the automorphism realising $(34)$. Read through (1.3): on tile 132 ($\pi=(23)$, $Z_0=Z/(Z-1)$) the point is $Z_0=-1$ and the condition is $P_{13}$; on tile 231 it is $P_{31}$ at the same $Z_0$. At $Z_0=-1$ the surface $(0,1,\infty,-1)$ has the automorphism $\zeta\mapsto-\zeta$ (relabelling $(24)$), which fixes punctures 1 and 3; $S_4$-symmetry makes $F_1$ odd up to a rotation of $W$, so $c_1=0$: the pole of $F_1$ is at $\infty=z_3$ ($P_{13}$), and likewise $c_3=0$ ($P_{31}$) – 089 (3.2) transported. So two of the six functions (1.4), $E_{13}$ and $E_{31}$ (one Klein class, $t$), vanish at the corner $Z_0=-1$ of $\overline{T_0}$ (walls $C_1\cap C_3$), linearly. $\tag{4.1}$

*Consistency.* (4.1) is a zero on the boundary of $T_0$, not in it, and at distance $a-\tfrac32>0$ from the $s$-arc (§1; at $\beta=\beta_{04}$ the arc would reach the corner, which is one reason for A3). Neither input of the argument is touched: the non-vanishing (3.1) is near the arc, the analyticity (3.2) is on the open tile, and a null zero set allows zeros on walls and corners. The argument claims no more than measure zero: a statement "$\mu_i$ nowhere zero on $\overline{\mathcal V_{0,4}}$" would be false at $Z=\tfrac12$ (and, for the other pairs, at $Z=-1$, $Z=2$, 089 C2.4). 089's numerical statement – no zero in the open $Q_V$, $|\mu_1|$ bounded away from zero outside $|Z-\tfrac12|<$ (companion value, not reproduced here) – is stronger than C5 and consistent with it; C5 does not reproduce it.

*Not covered.* (i) The corners $e^{\pm\mathrm i\pi/3}$ (fixed points of the 3-cycles, corners of six tiles each) and the other tile corners: points, not covered by the tile argument, irrelevant for measure (089: $|\mu_{ij}|=1/(\sqrt3\beta)$ at $e^{\mathrm i\pi/3}$). (ii) Analyticity across the six arcs, the real-axis walls and $\Re Z=\tfrac12$ is not used; PH34's piecewise form is all that enters, and only on $T_0$. (iii) No pointwise non-vanishing in the interior beyond a neighbourhood of the $s$-arc of each tile (and its images): that is 089's table, not this argument. (iv) PH34 is supported by the companion package v2.0.1, not proved; the boundary values for the actual vertex beyond the package rest on R86 C3.2 (Argued). (v) $\beta\le\beta_{04}$.

\subsection*{Verification}
`C6-corner-zero` ($Z_0=-1+r\,e^{3\pi\mathrm i/4}$, $r=10^{-2},10^{-3},10^{-4}$: $|X_{132}|$, $|X_{312}|$ vanish linearly in $r$; the four other pairs stay at (companion value, not reproduced here); both $\beta$).

## Verification – run

`OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 /usr/bin/time -v uv run --no-sync python codes/verify-per-tile.py`: `SUMMARY: 25/25 PASS (2.5 s)`, peak RSS 99800 kB, single process, seed 20261004, $\beta=\tfrac32$ and $2$. Break legs `BREAK-C1-tile-channel`, `BREAK-C2-transport`, `BREAK-C3-lambda0`, `BREAK-C4-wrong-pair` all fire. Output in `agent/scratch/computator/computator-091-per-tile-20261004T204400/run4.txt`. Earlier run: `C4-continuity` failed at both $\beta$ with a threshold $10^{-6}$ at $\varepsilon=10^{-5}$ that assumed $O(\varepsilon^2)$ convergence; the observed rate is exactly one decade per decade because the boundary value is evaluated at $|q|=1$ and the point at $|q|=1+\varepsilon$ (the $X_{abc}$ of the glued maps vary with $q$ in the package frame, unlike $\mu_{1,2}$ in 089's circle frame). Threshold set to continuity ($<10^{-4}$, rate $>0.9$); the $O(\varepsilon^2)$ statement moved to `C4-C1-join`, which compares at the same $Z$. Diagnosis: the check's expectation, not the result. Re-run 2026-10-10 after the docstring edit (staleness of "provisional"/v2.0.0, critic-091 #10): `SUMMARY: 25/25 PASS (11.4 s)`, peak RSS 97880 kB, single process; `ruff` was not available in the environment, so the file was not re-formatted (docstring text only).

## Self-review

1. *Objective.* Answered: R86 C3.4's a.e. clause now follows from PH34 by an argument (C0), with 089's table as independent numerical evidence for the stronger "no zero in open $Q_V$". The open per-tile step of R86 and PH34's Scope is closed, conditional on PH34 only.
2. *Weakest step.* C3's identification of the vertex's coordinates on the $s$-arc with the glued $\lambda=\tfrac12$ halves: for the package it is PH34's last clause (package v2.0.1), for the actual vertex R86 C3.2 (Argued). Shored up by `C4-continuity` and `C4-C1-join` (the package's section joins the channel maps, $O(\varepsilon^2)$, for all six pairs on this arc) and `C3-boundary-package` (the channel maps are the independent gluing, $10^{-15}$).
3. *Not checked.* PH34 itself (an input); the measure-theoretic steps (proved by hand, standard); $\beta\le\beta_{04}$ (excluded by A3; at $\beta_{04}$ the $s$-arc reaches the corner $Z_0=-1$, where $E_{13}=0$ is forced); other members of the companion's weight family: the argument applies to any $S_4$-symmetric section analytic on one fundamental tile and continuous up to $\partial_s$ with these boundary values, but no other member was run.
4. *What a stronger reader would add.* That the interpolating weight plays no role: the per-tile step uses one tile's analyticity and the boundary values, so it holds for the whole family of sections of the companion construction. And that C5 cannot be pushed to "no zero in the open $\mathcal V_{0,4}$" by the same means: the $c_j$ are real-analytic, not holomorphic, in $Z$, so no argument principle counts their zeros; 089's table is the evidence for that stronger form.

## Proposed ledger lines (for the orchestrator)

Rewritten in the fix pass of 2026-10-10 (critic-091 #13, #14, #8, #3, #9, #11) against the current entries of `knowledge/results.md`: R86 l. 1790–1810, PH34 l. 465–479. Every left-hand side below is a verbatim substring of the current entry, occurring exactly once in it (checked by `grep -o -F … | wc -l` on the line range; the counts are in the fix-pass report). The PH34 condition is carried wherever the a.e. clause is stated.

*R86* (`knowledge/results.md` l. 1790–1810). Replace, in this order:

1. [heading] `(records 089, 092, provisional; exact, every $\beta\ge\beta_{04}$)` → `(records 089, 092; exact, every $\beta\ge\beta_{04}$)`

2. [heading] `with $\mu_i=\tfrac13$ (C3.2 restated after PH33's refutation)` → `with $\mu_i=\tfrac1{2\beta}$ ($\tfrac13$ at $\beta=\tfrac32$) (C3.2 restated after PH33's refutation)`

3. [Scope] `read with $\mu_i=\tfrac13$ there` → `read with $\mu_i=\tfrac1{2\beta}$ ($\tfrac13$ at $\beta=\tfrac32$) there`

4. [Scope] `argued in record 091 from PH34, the parameter point and C3.2 — 091's critic pending` → `shown in record 091 from PH34 (continuity up to $\partial_s$ and analyticity on the fundamental tile only), the parameter point, and the $S_4$-symmetry and complex-conjugation equivariance of the section; zeros on tile walls and corners are not excluded ($Z=\tfrac12$ is one, record 089)`

5. [Verification (2026-10-06 line)] `the a.e. clause stays Conditional(PH34) with its open per-tile step` → `the a.e. clause stays Conditional(PH34); its per-tile step is shown in record 091 (line below)`

6. [Status] `($\mu_i=\tfrac13$ on $|q|=1$ and over $\mathcal F_s$)` → `($\mu_i=\tfrac1{2\beta}$, $\tfrac13$ at $\beta=\tfrac32$, on $|q|=1$ and over $\mathcal F_s$)`

7. [Status] `the a.e. strength of C3.4 – Conditional(PH34), the per-tile step closed Numerical (record 089: $\mu_i\ne0$ at grid points of every tile, provisional with the package; record 091 gives the argument, critic pending)` → `the a.e. strength of C3.4 – Conditional(PH34) – Proven (record 091; finite steps machine-checked; independent of the anchors' formulas and of the interpolation weight), the per-tile step also Numerical in record 089 ($\mu_i\ne0$ at grid points of every tile)`

8. [paper edit] `and, if the vertex's coordinates depend analytically on the modulus, at almost every point` → `and, if the vertex's coordinates depend analytically on the modulus inside each of the twelve tiles of the vertex region – as the explicit section indicates –, at almost every point`

9. [paper edit] `(at almost every modulus if the coordinates are analytic)` → `(at almost every modulus under the same hypothesis)`

10. [paper edit] `(constant $\mu=\tfrac13$ at the theory's point` → `(constant $\mu=\tfrac1{2\beta}$, $\tfrac13$ at $\beta=\tfrac32$, at the theory's point`

11. [Verification, new line after the 2026-10-06 line] "2026-10-04 (re-run 2026-10-10 after a docstring edit: 25/25 PASS) – derivation, exact/numerical – `agent/derivations/091-per-tile.md` C0–C6 – the per-tile step under PH34: the twelve tiles are carried by the $S_3\times\mathbb Z_2$ transport (with the section's $S_4$-symmetry and complex-conjugation equivariance, A4) to the six pole-at-partner conditions on the fundamental tile; these fail on its $s$-arc (the glued $\lambda=\tfrac12$ halves put no pole at a puncture; the zeros of the twelve differences are at $q=0$ and $|q|=\tfrac{4\beta^2}3$ only, never on $|q|=1$ for $\beta>\beta_{04}$), hence on an open set (PH34 continuity up to $\partial_s$) and off a null set (PH34 real-analyticity on that tile); `codes/verify-per-tile.py` 25/25 PASS (seed 20261004; `C2-transport` checks (1.3) against the package's relabelling, not the equivariance itself; break legs `BREAK-C1-tile-channel`, `BREAK-C2-transport`, `BREAK-C3-lambda0`, `BREAK-C4-wrong-pair` fire); consistent with record 089's zero at $Z=\tfrac12$ (a tile corner, $(24)$-automorphism)".

*PH34* (`knowledge/results.md` l. 465–479). Replace, in this order:

1. [Scope] `$\mu_i\not\equiv0$ on each tile (or the $S_3\times\mathbb Z_2$ equivariance of the section, which transports the condition $R_i=u_j$ – pole at the partner – between tiles) — not shown here; judged closable in a short record (critic-fable-decisions-sec6, #4)` → `$\mu_i\not\equiv0$ on each tile, which is shown in record 091 (C4) from this hypothesis (continuity of the $c_j$ up to $\partial_s$ and real-analyticity on the fundamental tile only) and the boundary values of the glued $\lambda=\tfrac12$ halves, transported between tiles by the $S_3\times\mathbb Z_2$ equivariance of the section (which transports the condition $R_i=u_j$ – pole at the partner – between tiles); zeros on tile walls and corners are not excluded`

2. [Verification (2026-10-06 line, last sentence)] `The per-tile step of R86's a.e. clause is still open` → `The per-tile step of R86's a.e. clause is shown in record 091 (Scope)`

3. [Used by] `R86 (C3.4, the a.e. clause, together with the open per-tile step)` → `R86 (C3.4, the a.e. clause, through record 091)`

4. [Verification, new line after the 2026-10-06 line] "2026-10-04 – numerical check – `codes/verify-per-tile.py` `C4-C1-join`: on the $s$-arc of the fundamental tile (13 angles, $\beta=\tfrac32$ and $2$) the package's $c_1,c_2,c_3$ join the $s$-channel maps to $O(\varepsilon^2)$ (six pole-at-partner functions; decades per decade (companion value, not reproduced here) over $\varepsilon=10^{-2},\dots,10^{-5}$; record 089 C3.4 had $\mu_{1,2}$ only)".

*Paper* (critic #4, optional; paper text, to be proposed to the author). Current `paper/sections/06-worldsheet.tex` l. 463, a verbatim unique line: `By analyticity on each tile, the failure then reaches almost every point if, and only if, it occurs somewhere in each tile, which we have not shown.` → `If the local coordinates depend analytically on the modulus within each tile of the vertex region, as the explicit construction indicates, their continuity up to the boundary of the propagator region, where the pole of each coordinate sits at none of the punctures, carries the failure to almost every point.` The hypothesis is carried in the sentence; the PH34 clause is not to be dropped.
