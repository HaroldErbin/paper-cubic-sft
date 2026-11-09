# Record 089 – The second-order coefficients $\mu_i(q)$ of the actual quartic vertex over $Q_V$, from the sister's section

## Status

complete after fix pass 2 (2026-10-04, critic-089 iterations 1 and 2 applied, see *Fix pass* and *Fix pass 2* at the end): steps (i)–(iv) and the segment criterion (C2.7) done, all results provisional with the sister's package v2.0.0 (unreviewed); the every-point claim is Numerical (analytic reduction; winding numbers from a sampled boundary, not interval arithmetic; $\beta=\tfrac32$ and $2$, hence every $\beta\le2$); `codes/verify-mu-table.py` 56/56 PASS (seed 20261004, $\beta=\tfrac32$ and $2$; not re-run in fix pass 2); R86 and PH34 text promoted 2026-10-04 (see the last section); open: script items #8, #9 of critic iteration 2 (Fix pass 2).

## Task and objective

- **Literal task.** Evaluate record 080's criterion (3.1), $\mu_1(q)=\beta a_1(q)\,(R_1(q)-u_2)/(R_1(q)-u_1)$, $\mu_2(q)=-\beta a_2(q)\,(R_2(q)-u_1)/(R_2(q)-u_2)$, pointwise on $Q_V$ from the sister's package v2.0.0: (i) the dictionary package frame → 080's circle frame, checked by two routes; (ii) a table of $\mu_{1,2}$ on a grid of $Q_V$ sampling all twelve tiles, per-tile minimum $|\mu_i|$ and zeros, refinement check; (iii) the check $\mu_1=\mu_2=\tfrac13$ ($\beta=\tfrac32$) on $|q|=1$ and over $\mathcal F_s$, with break legs; (iv) the behaviour of $\mu_i$ across one of the six arcs of PH34.
- **Motivating objective.** R86's "almost every point" clause rests on PH34 plus the non-vanishing of $\mu_i$ somewhere in each tile, not shown. The table is the numerical evidence for or against that step; the $\tfrac13$ check tests R86's restated boundary clause (C3.2) and the package together.
- **Answer in one line.** $\mu_1=\mu_2$ on all of $Q_V$; given the package's formulas (provisional) it is non-zero at every point of the open $Q_V$, in all twelve tiles (Numerical: segment criterion C2.7, for any interpolation weight with values in $[0,1]$, by a numerical argument principle on a sampled boundary, not interval arithmetic, at $\beta=\tfrac32$ and $2$, hence every $\beta\le2$; the grid gives sampled minima, not bounds); its only zero on the closure, for the package's weight, is a simple zero at $Z=\tfrac12$ ($q=\pm4i\beta^2$, on the fold circle, a corner of four tiles), forced by an automorphism of that surface; $\mu_i=\tfrac1{2\beta}$ ($=\tfrac13$ at $\beta=\tfrac32$) exactly on $\mathcal F_s$ and approached as $O(\varepsilon^2)$ at $|q|=1+\varepsilon$. The per-tile step of R86 holds (Numerical, provisional with the package), and in a stronger form: no zero in the open $Q_V$. At the tested arc point $Z=e^{2\pi i/3}$, for the pair $(1,2)$, $\mu_1$ is $C^0$ with a kink, not $C^1$ as the brief expected; the factor that decides its zeros is $C^1$ with a jump in the second derivative, as PH34 states for $c_j$ (other arc points and pairs not run).

## Step list and what failure would have looked like

1. **(i) Dictionary.** Failure: the package's $q$ is not 074's $q$, or the labels $\{1,2\}$ are not half A (tested by `C1-q-dictionary`, `C1-positions`, `C3-glued-maps`). The agreement of the three routes for $\mu_i$ is an implementation check, not a test of the dictionary: $\mu$ does not depend on the chart, so a wrong $u_{3,4}$ would pass it. Outcome: none of these failures.
2. **(iii) The $\tfrac1{2\beta}$ check.** Failure: the package's $s$-channel maps are not the glued $\lambda=\tfrac12$, $\gamma'=\beta$ halves, or `section_maps` does not tend to $\tfrac1{2\beta}$ at $|q|\to1^+$; the break legs $\lambda=0$, $\lambda=\tfrac14$, the wrong pair and the $\alpha'_{\rm v}=0$ prediction must fail. Outcome: passed, break legs fire.
3. **(ii) Table.** Failure for the objective: a tile with $\mu_i\equiv0$, or zeros on an open set. Outcome: an isolated zero at a tile corner on the boundary of $Q_V$ (the a priori check "no zero on any tile" failed and was restated, §3).
4. **(iv) Arcs.** Failure of the brief's expectation: a jump in $\mu_i$ or in its first derivative. Outcome: $\mu_i$ has a first-derivative jump (from $|a_i|$, as PH34 states); its zero-deciding factor is $C^1$.

## Conventions and assumptions

- **A1** Book conventions (the project conventions); geometric data only, no correlator normalisation enters.
- **A2** Package frame: punctures $(\zeta_1,\zeta_2,\zeta_3,\zeta_4)=(0,1,\infty,Z)$, label 3 in the chart $t=1/\zeta$; $s$-channel $=\{12|34\}$; 2-jet $(a,c)$, $F(W)=\zeta_0+aW+bW^2+\dots$, $c=b/2a^2=-1/(2(F(\infty)-\zeta_0))$ (package README, *Conventions*).
- **A3** Circle frame of half A (078 A2, 080 §2): $u=1/w_A$, $w_A$ the special-leg coordinate of half A; $u_{1,2}=\pm z$, $z=\tfrac1{2\beta}$; output at $u=\infty$; CKV of the pair $v=\beta(u^2-z^2)\partial_u$.
- **A4** Phase convention for $\mu_i$: $W$ is rotated so that $a_1^{(u)}>0$ and $a_2^{(u)}<0$ in the circle frame (the rigid halves' convention $f_2=-f_1$, 078 (4.1)). $|\mu_i|$ and the zero set do not depend on it (080 (1.3)); with it $\mu_i$ is a function of the surface, continuous across the tile walls where the package's own phase of $a_j$ jumps.
- **A5** $\beta=\tfrac32$ (main) and $\beta=2$; the package's default section ($\Lambda_1$ weight at $\lambda_0$).
- **A6** The actual $\mathcal V_4$ is the section fixed by the construction of the companion project (R86 Scope, 080 A7, positions clause and identification; the parameter point $\lambda=\tfrac12$, $\gamma'=\beta$ of the cubic vertex).
- **Input (provisional).** The sister's package v2.0.0, imported by path, not edited. Its section data are unreviewed on the sister's side: every number below built on `section_maps` is provisional with it. The $s$-channel maps (`maps_s_channel`, `channel_maps`) are checked here independently (C3.1).

## Claim tree

- **A1–A6** as above.
- **PH34** (ledger; provisional): the section is real-analytic on each of the twelve tiles; across the six arcs $c_j$ is $C^1$ not $C^2$ and $|a_j|$ $C^0$ with a kink; at $\partial\mathcal V_{0,4}$ the $c_j$ join the channel maps $C^1$, and so do the $|a_j|$ (no kink there: on the FD every $|a_j|$ is $|S_0|$ times a rational function of $Z$, and $S_0$ is the $s$-channel's $a_1$; C3.4 measures $O(\varepsilon^2)$). Restatement corrected in fix pass 1 (critic #3); it was "$|a_j|$ $C^0$ with a kink across the six arcs and at $\partial\mathcal V_{0,4}$".
- **C0 (root)** With the sister's package v2.0.0 as input (provisional, unreviewed): on the open $Q_V$, $\mu_1=\mu_2\ne0$ at every point, for the package's weight and for any interpolation weight with values in $[0,1]$ (C2.7; Numerical: analytic reduction, winding numbers from a sampled boundary, not interval arithmetic; $\beta=\tfrac32$ and $2$, hence every $\beta\le2$ by the nesting of $D(\beta)$); sampled minima on a $200\times800$ grid: $|\mu_1|$ stays bounded away from zero outside $|Z-\tfrac12|<0.1$, and $|\mu_1|/|Z-\tfrac12|$ stays bounded away from zero inside (sampled, not bounds; values from the companion SL(2,C) package, not reproduced here); for the package's weight (for which $L=O(|Z+1|^2)$ at the corner, (3.3)) the only zero on the closure of $Q_V$ is the simple zero at $Z=\tfrac12$ ($q=\pm4i\beta^2$, fold circle), forced by the $(34)$-automorphism of that surface (and, by the 2-jet form of (3.2), for every $S_4$-symmetric section continuous there), of slope $2\sqrt2/(3\beta)$; $\mu_i=\tfrac1{2\beta}$ on $\overline{\mathcal F_s}$ and $\mu_i-\tfrac1{2\beta}=O(\varepsilon^2)$ at $|q|=1+\varepsilon$; at the tested arc point $Z=e^{2\pi i/3}$, pair $(1,2)$, $\mu_1$ is $C^0$ with a kink and its zero-deciding factor $C^1$. Hence each of the twelve tiles carries an open set (in fact all of its interior in $Q_V$) where $\mu_i\ne0$: R86's per-tile step holds (Numerical, provisional with the package). [by C1–C4]
  - **C1** Dictionary: the package's $q$ is 032/074's plumbing parameter; labels $\{1,2\}$ are half A; the circle-frame positions are $u=(z,-z,2\beta/q,-2\beta/q)$ and $\zeta=N(u)$ of (1.2); $\mu_i$ agrees by three routes. [by C1.1–C1.3]
    - **C1.1** `q_of_Z` inverts $Z_4^{(s)}(q)=(q+4\beta^2)^2/16\beta^2q$ on $|q|<4\beta^2$, and the package's $\mathcal V_{0,4}$ test reproduces 074's $\sigma_V(\pi)$. [eq. (1.1); by check: C1-q-dictionary, C1-sigmaV-pi]
    - **C1.2** In the circle frame of half A the half-B punctures sit at $u_{3,4}=\pm2\beta/q$; 080 §3's $\pm q/z$ is a $q\leftrightarrow1/q$ slip without effect on $\mu_{1,2}$ or on 080 C3.3. [eq. (1.2)–(1.3); by check: C1-positions, BREAK-C1-q-inverse]
    - **C1.3** $\mu_i$ from 080 (3.1) in the circle frame, from 080 (1.7) in the package frame, and from a Cauchy-integral push-forward of the CKV agree. [eq. (1.4)–(1.6); by check: C1-three-routes]
  - **C3** The boundary clause: $\mu_1=\mu_2=\tfrac1{2\beta}$ on $\overline{\mathcal F_s}$, $=\tfrac13$ at $\beta=\tfrac32$. [by C3.1–C3.4]
    - **C3.1** The package's $s$-channel maps are the gluing of two $\mathcal V_3'(\lambda=\tfrac12,\gamma'=\beta,\beta')$ halves (and not of $\lambda=0$ or $\tfrac14$). [eq. (2.1); by check: C3-glued-maps, BREAK-C3-lambda]
    - **C3.2** Glued $\mathcal V_3'(\lambda,\beta)$ halves have $\mu_1=\mu_2=\lambda/\beta$ exactly in the A4 phase. [eq. (2.2); by check: C3-sympy-mu; cf. 080 C3.1]
    - **C3.3** The package's maps on $\mathcal F_s$ give $\mu_i=\tfrac1{2\beta}$ to $10^{-15}$. [by C3.1, C3.2; by check: C3-Fs-mu]
    - **C3.4** `section_maps` at $|q|=1+\varepsilon$ gives $\mu_i-\tfrac1{2\beta}=O(\varepsilon^2)$ uniformly in $\theta$ (24 angles): the section joins the Feynman value $C^1$ in the radial direction. [by check: C3-boundary-limit (rate asserted), BREAK-C3-boundary-lambda0; provisional with the package]
  - **C2** The table over $Q_V$ and the zero set. [by C2.1–C2.7]
    - **C2.1** The grids (coarse $100\times400$, fine $200\times800$ in $(\ln|q|,\arg q)$) meet all twelve tiles. [by check: C2-tiles-covered]
    - **C2.2** $\mu_1=\mu_2$ (A4 phase) on $Q_V$: Klein covariance; true by construction of the package (`section_FD` imposes $F_2=K_2\circ F_1$), the check confirms the record's reading of the package's labels and phase. [eq. (3.1); by check: C2-klein]
    - **C2.3** On tile $g=(\pi,\epsilon)$, $|\mu_{12}(g\cdot Z_0)|=|\mu_{\pi^{-1}(1)\pi^{-1}(2)}(Z_0)|$ with $Z_0$ in the fundamental domain: the twelve tiles carry three functions, $|\mu_{12}|$, $|\mu_{13}|$, $|\mu_{23}|=|\mu_{14}|$ on the FD. True by construction of the package (`section_maps` is `relabel(section_FD(Z0))`); the check confirms the record's reading of the package's labels and permutation. [by A6; by check: C2-equivariance]
    - **C2.4** $\mu_{12}\to0$ linearly at $Z=\tfrac12$ (slope (companion value, not reproduced here) at $\beta=\tfrac32$, isotropic); the zero is forced: at $Z=\tfrac12$ the involution $\psi(\zeta)=\zeta/(2\zeta-1)$ fixes punctures 1, 2 and swaps 3, 4, and $S_4$-symmetry puts the pole of $F_1$ at $\zeta=1=\zeta_2$ (Möbius form, (3.2)); for every $S_4$-symmetric section, Möbius or not, the 2-jet form gives $c_1=-\tfrac12$ and $\mu_{12}=0$ (critic iteration 2, #3; right after (3.2)). Its $S_3$ images: $\mu_{13}\to0$ at $Z=-1$, $\mu_{14}\to0$ at $Z=2$. (3.2) presupposes the section defined and $S_4$-symmetric at the corner; the package's section extends continuously there (3.3), and its formula gives the zero directly ($\mu_{13}=S_0/R=0$ at $Z_0=-1$), a second route; the slope is derived, (3.5). [eq. (3.2), (3.3), (3.5); by C2.6; by check: C2-zero-at-half, BREAK-C2-zero-at-half, C2-symmetric-zeros]
    - **C2.5** Sampled minima (not bounds): at every grid point $|\mu_1|$ is bounded away from zero outside the disc $|Z-\tfrac12|<0.1$ and $|\mu_1|/|Z-\tfrac12|$ is bounded away from zero inside ($\beta=\tfrac32$; numerical values not reproduced here), and the per-tile minima of $|\mu_1|/|Z-\tfrac12|$ are stable to $0.7\,\%$ under halving the step. The grid alone proves nothing between grid points (a zero pair with a basin narrower than the step would pass); the statement for every point is C2.7. [by check: C2-no-other-zero, C2-refinement]
    - **C2.6** On the closed FD, $|\mu_{1j}|=|S_0|\,|1/R-1/\zeta_j|$, $1/\zeta_j\in\{1,0,1/Z\}$, and every pair's $\mu$ on the FD is one of these three by the Klein maps; closed forms $|\mu_{12}(-1)|=1/(\sqrt2\beta)$, slope $2\sqrt2/(3\beta)$ at $Z=\tfrac12$, $|\mu_{1j}(e^{i\pi/3})|=1/(\sqrt3\beta)$ (provisional with the package's formulas). [eq. (3.3)–(3.5); by A2, A6, 080 (1.7); by check: C2-closed-forms, C2-zero-at-half, C2-symmetric-zeros]
    - **C2.7** Segment criterion, Numerical (analytic reduction (3.4)–(3.6), holomorphy and the algebraic zeros of $g_t$; the decision "$g_t(\partial D)$ misses $(0,1]$, windings $0$" is read from a sampled boundary, not interval arithmetic; $\beta=\tfrac32$ and $2$, hence every $\beta\le2$: $A$, $B$, $t_j$ do not depend on $\beta$, the weight drops out, and $D(\beta)={\rm FD}\cap\{\Re\,{\rm arccosh}(2Z-1)\le\ln4\beta^2\}$ grows with $\beta$, the ellipses being confocal): for every interpolation weight $L$ with values in $[0,1]$, no zero of any $\mu_{1j}$ on the closed FD $\cap\,\mathcal V_{0,4}$ except possibly $\mu_{13}$ at the corner $Z_0=-1$, where $\mu_{13}(-1)=S_0(-1)\,L(-1)\,(1-1/\sqrt2)$ vanishes iff $L(-1)=0$ – true for the package's weight (3.3), and for any weight meeting the corner condition $R(-1)=\infty$; transported, $\mu_1=\mu_2\ne0$ on the closed $\mathcal V_{0,4}$ except possibly at $Z=\tfrac12$ (where it vanishes for the package's weight), in particular at every point of the open $Q_V$ (given the package's formulas). [eq. (3.6)–(3.8); by C2.6, C2.3; by check: C2-segment-no-pole, C2-segment, C2-segment-corner, BREAK-C2-segment]
  - **C4** Across the arc $|Z|=1$ at the one tested point $Z=e^{2\pi i/3}$, pair $(1,2)$: $\mu_1$ is continuous with a jump of its first derivative, carried by $|a_1|$; the factor $g_1=\mu_1/|a_1^{(u)}|=\beta(R_1-u_2)/(R_1-u_1)$ is $C^1$ with a jump of its second derivative; across the analytic wall $\Re Z=\tfrac12$ above $e^{i\pi/3}$ and at an interior point nothing jumps. Other arc points and the pairs $(1,3)$, $(2,3)$ not run (covering $\mu_{12}$ on all six arcs needs $\mu_{12},\mu_{13},\mu_{23}$ across C3, C2.3). Provisional with the package. [eq. (4.1); by check: C4-arc-C0, C4-arc-kink, C4-control]

Open gaps: none
Hypotheses in force: none used by C0 after fix pass 1 (the "every point" strength now comes from C2.7, a property of the package's formulas, not from PH34's continuity); PH34 is tested at one arc point (C4) and is what R86's a.e. clause adds; the package is a provisional cited input throughout, not a hypothesis.

## §1 (C1) – Dictionary

\subsection*{Setup}
A2, A3. $W$ the local coordinate (unit disc) shared by both frames. A Möbius map is $(A,B,C,D)$, $W\mapsto(AW+B)/(CW+D)$.

\subsection*{Derivation}
*The plumbing parameter.* 032 (1.2): two $\mathcal V_3'$ halves glued at their special legs by $w_Aw_B=q$; the ordinary punctures of half A sit at $w_A=\pm2\beta$ ($z=0$, $z=\infty$ of half A), those of half B at $w_A=q/w_B=\pm q/2\beta$. The cross-ratio sending $(2\beta,-2\beta,q/2\beta)\to(0,1,\infty)$ sends $-q/2\beta$ to
$$
Z=\frac{(q+4\beta^2)^2}{16\beta^2q}\iff q^2+8\beta^2(1-2Z)\,q+16\beta^4=0 , \tag{1.1}
$$
the equation `q_of_Z` solves, root $|q|<4\beta^2$. So the package's labels are $1,2=$ half A ($z=0,\infty$), $3,4=$ half B, its $q$ is 032's and 074's, and $Q_V=\{1<|q|<e^{\sigma_V(\theta)}\}$ is the same set.

*Circle frame.* $u=1/w_A$ (078 A2: $u=1/f_1'^{-1}(z)$): $u_1=z$, $u_2=-z$, $u_{3,4}=1/(\pm q/2\beta)=\pm2\beta/q$; the gluing reads $u_Au_B=1/q$ in circle-frame coordinates (A2 of 074 writes $u_Au_B=q$ for the special-leg coordinates $w$). The Möbius map to the package frame:
$$
\zeta=N(u)=\frac{(u-u_1)(u_2-u_3)}{(u-u_3)(u_2-u_1)},\qquad N(u_1,u_2,u_3,u_4)=(0,1,\infty,Z). \tag{1.2}
$$
080 §3 writes $u_{3,4}=\pm q/z$; with it $N(u_4)\ne Z$ (`BREAK-C1-q-inverse`). The slip does not reach $\mu_{1,2}$, which use only $u_1,u_2$ and $F_1,F_2$, nor 080 C3.3 ($u_2\ne u_4$ holds in both forms on $1<|q|<4\beta^2$). $\tag{1.3}$

*Three routes to $\mu_i$.* (a) Circle frame, 080 (3.1): $F_i^{(u)}=N^{-1}\circ F_i$, $a_i^{(u)}=(F_i^{(u)})'(0)$, $R_i=F_i^{(u)}(\infty)$,
$$
\mu_1=\beta a_1^{(u)}\frac{R_1-u_2}{R_1-u_1},\qquad \mu_2=-\beta a_2^{(u)}\frac{R_2-u_1}{R_2-u_2};\qquad
\mu_1^{\rm A4}=\beta|a_1^{(u)}|\frac{R_1-u_2}{R_1-u_1},\quad \mu_2^{\rm A4}=\beta|a_2^{(u)}|\frac{R_2-u_1}{R_2-u_2}. \tag{1.4}
$$
(b) Any frame $x$ with both punctures finite, 080 (1.7): $\mu_i=a_i/(x_i-x_j)-2a_ic_i$ (computed in $x=1/(\zeta-p)$, $p$ generic, with the package's `mobius_jet`). $\tag{1.5}$
(c) The definition 080 (1.3) itself: $\tilde v(W)=v(F_i(W))/F_i'(W)$ with $v=(x-x_i)(x-x_j)$, Taylor coefficients by FFT on $|W|=0.05$, $\mu_i=v_2/v_1$ (no jet formula, no pole). $\tag{1.6}$

\subsection*{Commentary}
(1.1): the branch $|q|<4\beta^2$ is 032 (1.3a)'s injectivity disc. (1.2): $N$ is fixed by three points; the fourth is a check. (1.4)–(1.6) compute the same intrinsic number (080 (1.3) is chart-independent), with the same $W$, so they must agree as complex numbers, not only in modulus. A4's $\mu^{\rm A4}$ removes the phase of $a_i^{(u)}$; on the rigid halves $a_1^{(u)}=1/\beta\gamma'>0$, $a_2^{(u)}=-a_1^{(u)}$, and $\mu^{\rm A4}=\mu$.

\subsection*{Result}
The dictionary (1.1)–(1.2), the formula (1.4). At a point of $\mathcal F_s$ ($\beta=\tfrac32$) the package's $F_1,F_2$ in the circle frame have $a_1^{(u)}$, $R_1$, $a_2^{(u)}$, $R_2$ (companion value, not reproduced here): the rigid $\lambda=\tfrac12$, $\gamma'=\beta$ halves of 078 (4.1) composed with $W\to-W$. [C1]

\subsection*{Verification}
`C1-q-dictionary` (200 random $q$ in $|q|<4\beta^2$, both sides of $|q|=1$: relative error $\le6.6\times10^{-15}$); `C1-sigmaV-pi` (bisection of the package's $\mathcal V_{0,4}$ test along $\theta=\pi$ against 074's closed form $\ln4\beta^2-2\,{\rm arcsinh}\frac{4\beta}{4\beta^2-1}$: $0.8109302162$ at $\beta=\tfrac32$, $1.7509374747$ at $\beta=2$, both agree to $10^{-10}$; independent of the package's region code); `C1-positions`; `BREAK-C1-q-inverse` (fires); `C1-three-routes` (60 random points of $\mathcal V_{0,4}$ per $\beta$, max $|\Delta\mu|\le5.1\times10^{-13}$): an implementation check of the three evaluations; it cannot detect a wrong $u_{3,4}$ ($\mu$ is chart-independent, and any $N$ with $N(u_{1,2})=(0,1)$ gives the same value). The dictionary is tested by `C1-positions` (self-consistency of (1.1)–(1.2)), `C1-q-dictionary` and `C3-glued-maps`.

## §2 (C3) – The boundary clause: $\mu_i=\tfrac1{2\beta}$ on $\overline{\mathcal F_s}$

\subsection*{Setup}
A3–A6, §1. $\mathcal V_3'(\lambda,\gamma',\beta')$ of 032 §1 with $\gamma'=\beta'=\beta$: $f_0(W)=W/(\lambda W+\beta)$ at $z=0$, $f_\infty=1/f_0$, special leg $w=2\beta(1-z)/(1+z)$. The theory's cubic vertex is $\lambda=\tfrac12$.

\subsection*{Derivation}
*Gluing, independently of the package.* In sympy, exact rational $\beta$, $\lambda$ and $q\in\{\tfrac12+\tfrac i3,\ -\tfrac3{10}-\tfrac i2,\ 2+i\}$: the four maps $\zeta_j(W)$ of the glued surface in the frame (1.1), and their 2-jets. Compared with `maps_s_channel` at $Z(q)$: $c_1,c_2,|a_1|,|a_2|$ agree to $4.4\times10^{-16}$ at $\lambda=\tfrac12$ and differ by (companion value, not reproduced here) ($\lambda=0$), (companion value, not reproduced here) ($\lambda=\tfrac14$) at $\beta=\tfrac32$. $\tag{2.1}$

*Circle frame of the glued halves.* $u=1/w_A$, $F_1^{(u)}(W)=1/w_A(f_0(W))$, $F_2^{(u)}=1/w_A(1/f_0(W))=-F_1^{(u)}$; by (1.4)
$$
\mu_1=\mu_2=\frac{\lambda}{\beta}\quad(\gamma'=\beta),\qquad \lambda=\tfrac12:\ \mu_i=\tfrac1{2\beta}=\tfrac13\ (\beta=\tfrac32),\ \tfrac14\ (\beta=2), \tag{2.2}
$$
exactly (sympy, $\lambda\in\{0,\tfrac14,\tfrac12\}$; 080 C3.1 with $\gamma'=\beta$). The glued maps in the circle frame do not depend on $q$, so (2.2) holds on all of $\mathcal F_s$ and on its boundary $|q|=1$.

*Approach from $Q_V$.* `section_maps` at $q=(1+\varepsilon)e^{i\theta}$, 24 angles:

[Table of companion-project values removed.]

Measured rate (companion value, not reproduced here), consistent with $\varepsilon^{2}$ at both $\beta$: $\mu_i$ is continuous at $|q|=1$ with zero radial derivative on the $Q_V$ side, i.e. it joins the constant Feynman value $C^1$. $\tag{2.3}$

\subsection*{Commentary}
(2.1) is the check that the package's $s$-channel family is the gluing of two copies of the theory's cubic vertex: it tests the package's derivation 003 maps against 032's $\mathcal V_3'$ with nothing shared but the parametrisation (1.1). (2.2) holds for every $q$ because the circle frame of half A is half A's own frame. (2.3): PH34 says only that the $c_j$ join the channel maps $C^1$; the $O(\varepsilon^2)$ of $\mu_i=|a_i|\cdot g_i$ shows that, radially, $|a_i|$ joins $C^1$ as well. The break leg of the boundary check (fix pass 1, critic #12): the same pipeline (`mu_circle` at $|q|=1+10^{-6}$, 24 angles, same target and tolerance) fed with glued $\lambda=0$ halves deviates by $\tfrac1{2\beta}$ and fails, while glued $\lambda=\tfrac12$ halves through the same code deviate by $2\times10^{-16}$ (`BREAK-C3-boundary-lambda0`). The former legs are relabelled: the $(1,3)$ pair at $|q|\to1^+$ ($|\mu_{13}|$: companion value, not reproduced here, $\ne\tfrac13$) is a sanity check (`SANITY-C3-wrong-pair`), it runs a different function; the comparison of the measured $\tfrac13$ with 080's former $\alpha'_{\rm v}=0$ prediction $0$ is dropped (it compared a value already found to be $\tfrac13$ with $0$).

\subsection*{Result}
$$
\boxed{\ \mu_1=\mu_2=\tfrac1{2\beta}\ \text{on }\overline{\mathcal F_s}\ \text{(exact)};\qquad \mu_i\big((1+\varepsilon)e^{i\theta}\big)=\tfrac1{2\beta}+O(\varepsilon^2)\ \text{from }Q_V\ }
$$
R86's restated boundary clause ($\mu_i=\tfrac13$ on $|q|=1$ and over $\mathcal F_s$, $\beta=\tfrac32$) is confirmed by the package's $s$-channel maps and by the independent gluing; the approach from $Q_V$ (C3.4) rests on `section_maps` alone and is provisional with the package. [C3]

\subsection*{Verification}
`C3-glued-maps`, `BREAK-C3-lambda` (fires at $\lambda=0,\tfrac14$), `C3-sympy-mu` (exact), `C3-Fs-mu` ($\le2\times10^{-15}$ on $\approx100$ random points of $\mathcal F_s$), `C3-boundary-limit` (table above; since fix pass 1 it asserts the rate, $|{\rm rate}-2|<0.1$, measured rate: companion value, not reproduced here), `BREAK-C3-boundary-lambda0` (fires), `SANITY-C3-wrong-pair`. Both $\beta$.

## §3 (C2) – The table over $Q_V$

\subsection*{Setup}
§1, A4, A5. Grid: cell-centred in $(\ln|q|,\arg q)\in(0,\ln4\beta^2)\times(-\pi,\pi]$, coarse $100\times400$, fine $200\times800$, points kept where the package's closed-$\mathcal V_{0,4}$ test holds (fine: number of kept points, companion value, not reproduced here). Tile of a point: `tile_of` (permutation of labels 1, 2, 3, conjugation flag `*`).

\subsection*{Derivation}
*Klein covariance.* At every $Z$ the relabelling $(12)(34)$ maps the surface to itself through $u\mapsto-u$ in the circle frame (swaps $u_1\leftrightarrow u_2$, $u_3\leftrightarrow u_4$); $S_4$-symmetry then gives $F_2^{(u)}=-F_1^{(u)}\circ(e^{i\alpha}\cdot)$ and, $\mu$ being intrinsic and A4 fixing the phase,
$$
\mu_1^{\rm A4}(q)=\mu_2^{\rm A4}(q)\quad\text{on }Q_V . \tag{3.1}
$$
*Per-tile table* ($\beta=\tfrac32$; $\mu_2$ identical by (3.1); conjugate tiles identical in modulus):

| tile | where the minimum of $\lvert\mu_1\rvert$ sits |
| --- | --- |
| 123, 213 (and `*`) | $\lvert q\rvert\to1$ ($\partial_s$), value $\tfrac1{2\beta}$ |
| 132, 231 (and `*`) | $Z\to\tfrac12$ (fold point $q=\pm4i\beta^2$) |
| 312, 321 (and `*`) | on the arc $\lvert Z\rvert=1$ |

The numerical values of the minima and maxima come from the companion SL(2,C) package and are not reproduced here; at $\beta=2$ the pattern is the same, and the ratio minima are stable to $0.7\,\%$ under halving the step.

*The zero at $Z=\tfrac12$.* The surface $(0,1,\infty,\tfrac12)$ has the automorphism $\psi(\zeta)=\zeta/(2\zeta-1)$: $\psi(0)=0$, $\psi(1)=1$, $\psi(\infty)=\tfrac12$, $\psi(\tfrac12)=\infty$, $\psi'(0)=-1$, $\psi^2={\rm id}$. It realises the relabelling $(34)$, so by $S_4$-symmetry $F_1(e^{i\alpha}W)=\psi(F_1(W))$; comparing first-order terms, $e^{i\alpha}=-1$. With $F_1(W)=aW/(1+\nu W)$:
$$
F_1(-W)=\frac{-aW}{1-\nu W},\qquad \psi(F_1(W))=\frac{aW}{2aW-1-\nu W}=\frac{-aW}{1+(\nu-2a)W}
\ \Longrightarrow\ \nu=a,\quad F_1(\infty)=\frac a\nu=1=\zeta_2 , \tag{3.2}
$$
the pole at the partner, i.e. $\mu_1=0$ (080 (1.6)); likewise $\mu_2=0$.

*2-jet form of (3.2), for every $S_4$-symmetric section (critic iteration 2, #3).* Not only Möbius ones: only the 2-jet of $F_1$ enters. With $\psi(\zeta)=\zeta/(2\zeta-1)=-\zeta-2\zeta^2+O(\zeta^3)$ and $F_1(W)=aW+bW^2+O(W^3)$, the condition $F_1(-W)=\psi(F_1(W))$ (the symmetry above, $e^{i\alpha}=-1$) reads at order $W^2$
$$
b=-b-2a^2\ \Longrightarrow\ b=-a^2,\qquad c_1=\frac b{2a^2}=-\frac12, \tag{3.2'}
$$
and 080 (1.7) with $x_1=0$, $x_2=1$ gives $\mu_{12}=\dfrac a{0-1}-2a\Big(-\dfrac12\Big)=0$. The Möbius form (3.2) is the special case $b=-a\nu$, $\nu=a$. So the zero at $Z=\tfrac12$ is forced for any section that is defined and $S_4$-symmetric at that surface, independently of the package and of the weight; what the package adds is that its section is defined there, (3.3).

*Location and slope.* $Z=\tfrac12$ is $q=4\beta^2e^{\pm i\pi/2}$, on the fold circle: inside the fold arcs of 074 C1.3 ($\cos^2\tfrac\theta2=\tfrac12\in(\tfrac9{25},\tfrac{16}{25})$ at $\beta=\tfrac32$), on the boundary of $Q_V$, and an interior point of $\mathcal V_{0,4}$ as a set of surfaces (on the real segment reached only as the fold, a corner of the tiles 132, 231 and conjugates). (3.2) presupposes that the section is defined, single-valued and $S_4$-symmetric at $Z=\tfrac12$, a corner of four tiles; this holds for the package: its section extends continuously to the FD image $Z_0=-1$ of the corner ((3.3) below; the division by $1+Z_0$ is in $R_{\rm anchor}$, not in the section), and its formula gives the zero directly, $\mu_{13}=S_0/R=0$ at $Z_0=-1$ ((3.4) below), a second route next to (3.2). Numerically $|\mu_1|/|Z-\tfrac12|$ tends to a limit that is isotropic to $5\times10^{-4}$ at $r=10^{-4}$: a simple zero, of slope $2\sqrt2/(3\beta)$, derived in (3.5). Its images under $S_3$ (C2.3): $\mu_{13}=0$ at $Z=-1$, $\mu_{14}=0$ at $Z=2$, with slope $|S_0(-1)|/3=1/(3\sqrt2\beta)$ (the slope at $Z=\tfrac12$ divided by $4=|{\rm d}(Z/(Z-1))/{\rm d}Z|$ at $Z=\tfrac12$); there $|\mu_{12}|=1/(\sqrt2\beta)$, the per-tile maximum of tiles 123/213. At the $S_3$-fixed point $e^{i\pi/3}$, $|\mu_{ij}|=1/(\sqrt3\beta)$ for all pairs (no zero). All three values are derived in (3.5).

\subsection*{Commentary}
The table first ran with the a priori check "min $|\mu_i|>\tfrac1{20\beta}$ on every tile, stable under refinement"; it failed on tiles 132/231, whose minimum halved with the grid step: the signature of an isolated simple zero at distance $\sim$ one step from the grid, located at $Z=\tfrac12$ and then explained by (3.2). The check was restated as C2.4 (the zero) plus C2.5 (no other zero); a first restated refinement check on $\min|\mu_1|$ over $|Z-\tfrac12|\ge0.1$ failed at $3.7\,\%$ because that minimum sits on the excision circle (there $|\mu_1|$ is proportional to the radius $0.1$) and measures the grid's distance to it; the refinement quantity is now the per-tile minimum of $|\mu_1|/|Z-\tfrac12|$, finite at the zero. The equivariance C2.3 explains the pattern of the table: tiles 123/213 carry $|\mu_{12}|$ on the FD (adjacent to $\partial_s$, where it is $\tfrac1{2\beta}$), tiles 132/231 carry $|\mu_{13}|$ (vanishing at the FD corner $Z_0=-1$, image of $Z=\tfrac12$), tiles 312/321 carry $|\mu_{23}|$ (no zero on the closed FD: its zero, at $Z_0=2$ via Klein, is outside). The grid numbers are sampled minima, not bounds: PH34 gives qualitative regularity, not a derivative constant, and cannot interpolate them; the minimum outside the disc sits on the excision circle, where the continuous infimum is probably slightly below the grid value. The statement for every point is the segment criterion of §3b, which does not use the grid (fix pass 1, critic #2).

\subsection*{Result}
$$
\boxed{\ \mu_1=\mu_2\ne0\ \text{at every point of the open }Q_V;\quad \{\mu_i=0\}\cap\overline{\mathcal V_{0,4}}=\{Z=\tfrac12\}\ \text{(for the }s\text{-pair; simple, symmetry-forced)}\ }
$$
(the boxed statement by C2.7, §3b: given the package's formulas, provisional, for any interpolation weight with values in $[0,1]$; Numerical, by an argument principle on a sampled boundary, not interval arithmetic; the zero at $Z=\tfrac12$ holds for the package's weight and, by (3.2'), for every $S_4$-symmetric section), with the per-tile sampled minima of the table (sampled, not bounds). For R86: each tile has $|\mu_i|$ above a bound (companion value, not reproduced here) at its grid points of $Q_V$ outside a disc of radius $0.1$ about one corner, so the per-tile step holds (Numerical) without any interpolation; the "almost every point" clause can be read "every point of $Q_V$" (provisional with the package, by the segment criterion, numerical argument principle on a sampled boundary, not interval arithmetic). At the single surface $Z=\tfrac12$ of $\mathcal V_{0,4}$, R84's criterion holds exactly ($\mu_1=\mu_2=0$): measure zero, outside the open $Q_V$. [C2]

\subsection*{Verification}
`C2-tiles-covered` (12/12 at both resolutions), `C2-klein` ($\max|\mu_1-\mu_2|\le6.7\times10^{-16}$), `C2-equivariance` (8637 and 11920 points, $\le3.4\times10^{-15}$, against `section_FD` directly), `C2-zero-at-half` and `BREAK-C2-zero-at-half` (the same test at $Z=\tfrac12+0.3i$ gives a ratio growing as $1/r$: values not reproduced here, fires), `C2-symmetric-zeros`, `C2-no-other-zero` (sampled minima at grid points; thresholds: $\tfrac1{20\beta}$ outside the disc, half the slope inside; both thresholds passed at $\beta=\tfrac32$), `C2-refinement` ($5.5\times10^{-3}$, $6.9\times10^{-3}$; detects only features resolved by one of the two grids). `C2-klein` and `C2-equivariance` hold by construction of the package for any $R$, $S$; they test the record's reading of the package's labels, permutation and phase, not the section. Since fix pass 1 `C2-zero-at-half` and `C2-symmetric-zeros` compare with the derived values (3.5).

## §3b (C2.6, C2.7) – Closed forms on the FD and the segment criterion (fix pass 1)

\subsection*{Setup}
A2, A6; the package's section on $D:={\rm FD}\cap\mathcal V_{0,4}=D(\beta)={\rm FD}\cap\{\Re\,{\rm arccosh}(2Z-1)\le\ln4\beta^2\}$ (closed; walls C1: $Z\le-1$ real, C3: $|Z|=1$, C2: $\Re Z=\tfrac12$, C4: the ellipse, $|q|=1$; $D(\beta)$ grows with $\beta$, the ellipses being confocal with foci $0,1$; the corner $-1$ lies in $D(\beta)$ iff $\beta\ge(1+\sqrt2)/2$, by hand: $\Re\,{\rm arccosh}(-3)=2\ln(1+\sqrt2)$, and below that the surface $Z=\tfrac12\notin\mathcal V_{0,4}$ and no zero occurs; critic iteration 2, #5): $F_1=RSW/(SW+R)$, so $F_1(0)=0$, $F_1'(0)=S=S_0(Z)=\beta^{-1}\sqrt{Z/(Z-1)}\ne0$, $F_1(\infty)=R$; $1/R=(1-L)A+LB$ with
$$
A(Z)=\frac{1+Z}{3Z},\qquad B(Z)=\frac{1+3x}{2(1+x)},\quad x=e^{-{\rm arccosh}(2Z-1)},\qquad L=\Lambda_1(Z,\beta);
$$
$F_j=K_j\circ F_1$ with the Klein maps $K_j$; off the FD the section is the transport (`section_maps` $=$ `relabel(section_FD(Z0))`). $\delta:=Z+1$.

\subsection*{Derivation}
*Corner (critic #1).* At $Z_0=-1$: $|Z|^2-1=-2\Re\delta+|\delta|^2$, $|Z-1|^2-1=3+O(|\delta|)$, so $d_3=-6\Re\delta+O(|\delta|^2)$, while $d_4(-1)>0$; hence $s=O(|\delta|)$ and $L=\phi(s)=3s^2-2s^3=O(|\delta|^2)$. With $A=\delta/(3(\delta-1))=-\delta/3+O(\delta^2)$:
$$
\frac1R=-\frac\delta3+O(|\delta|^2)\to0,\qquad F_1=\frac{SW}{1+SW/R}\to S_0(-1)\,W , \tag{3.3}
$$
continuously: the section extends to the corner on each tile; the division by $1+Z_0$ is in $R_{\rm anchor}=3Z/(1+Z)$, not in $F_1$.

*Erratum (record 092, critic-092 iteration 1, #1; bookkeeping, no other change to this record).* The statement $d_4(-1)>0$ above holds for $\beta>\beta_{04}=\tfrac12+\tfrac1{\sqrt2}$; at $\beta=\beta_{04}$ exactly, $d_3(-1)=d_4(-1)=0$ ($\ln(3+2\sqrt2)={\rm arccosh}\,3$), the corner $Z_0=-1$ is C3$\cap$C4 (a cusp of $D$), and the package's weight is discontinuous there (its `a + b <= 0` branch returns $L=1$), so (3.3) and the sentences "$\mu_{13}(-1)=0$ for the package's weight" (C0, C2.4, C2.7, (3.8) and after) hold for $\beta>\beta_{04}$ only; at $\beta_{04}$ $\mu_{13}(-1)=S_0(-1)(1-1/\sqrt2)\ne0$ for the package's code. The non-vanishing claims are unaffected (they need only $L\in[0,1]$).

*Closed form (critic #5).* In the chart $\zeta$ with puncture 1 at $0$ and puncture $j$ at $\zeta_j$ finite, 080 (1.7) with $a_1=S$, $c_1=-1/(2(R-0))$ gives $\mu_{1j}=S/(0-\zeta_j)+S/R$; for $j=3$ ($\zeta_3=\infty$) the chart-independent limit:
$$
\mu_{1j}=S_0\Big(\frac1R-\frac1{\zeta_j}\Big),\qquad \frac1{\zeta_j}\in\{1,0,\tfrac1Z\}\quad(j=2,3,4). \tag{3.4}
$$
Since $F_j=K_j\circ F_1$ exactly, every $\mu_i^{(ik)}$ on $D$ equals some $\mu_1^{(1k')}$ (e.g. $K_2$ realises $(12)(34)$: $\mu_2^{(21)}=\mu_1^{(12)}$, $\mu_2^{(23)}=\mu_1^{(14)}$). Values, from (3.3)–(3.4):
$$
\begin{aligned}
|\mu_{12}(-1)|&=|S_0(-1)|=\tfrac1\beta\big|\sqrt{\tfrac{-1}{-2}}\big|=\tfrac1{\sqrt2\beta},\\
|\mu_{13}(Z_0)|&=|S_0|\,|1/R|=\tfrac{|S_0(-1)|}3\,|\delta|+O(|\delta|^2)\quad\text{(isotropic: the leading term is holomorphic in }\delta),\\
\text{slope at }Z=\tfrac12:&\quad Z_0=\tfrac Z{Z-1},\ \big|\tfrac{{\rm d}Z_0}{{\rm d}Z}\big|_{1/2}=4\ \Rightarrow\ \tfrac43|S_0(-1)|=\tfrac{2\sqrt2}{3\beta},\\
|\mu_{1j}(e^{i\pi/3})|&=\tfrac1\beta\cdot\tfrac1{\sqrt3}\quad(L=0\text{ on C3, }1/R=A=\tfrac1{\sqrt3}e^{-i\pi/6},\ |A|=|1-A|=|A-e^{-i\pi/3}|=\tfrac1{\sqrt3},\ |S_0|=\tfrac1\beta).
\end{aligned} \tag{3.5}
$$

*Segment criterion (critic #2(b)).* On $D$, $L\in[0,1]$: $d_3\ge0$ ($|Z|\ge1$ and $|Z-1|^2=|Z|^2-2\Re Z+1\ge|Z|^2\ge1$), $d_4\ge0$ inside the ellipse, $\phi([0,1])=[0,1]$ (and the package returns $1$ when $d_3+\lambda_0d_4\le0$). So $1/R(Z)$ lies on the segment $[A(Z),B(Z)]$ whatever the weight, and by (3.4), $S_0\ne0$:
$$
\mu_{1j}(Z)=0\ \Longrightarrow\ t_j(Z)\in[A(Z),B(Z)],\qquad t_j\in\{1,\,0,\,1/Z\}, \tag{3.6}
$$
a sufficient condition for non-vanishing that does not depend on $L$. With $g_t:=(t-A)/(B-A)$, $t\in[A,B]\iff g_t\in[0,1]$. $g_t$ is meromorphic on a neighbourhood of $D$, with poles only at the zeros of $B-A$ (critic iteration 2, #1): $A$ is meromorphic with its only pole at $0\notin D$; $B$ is holomorphic on a neighbourhood of $D$, since the branch points $Z=0,1$ of ${\rm arccosh}(2Z-1)$ are outside $D$ and $x=e^{-{\rm arccosh}(2Z-1)}$ has no jump across the cut $2Z-1<-1$ (on its two sides $w={\rm arccosh}(2Z-1)=r\pm i\pi$, and $e^{-w}=-e^{-r}$ on both), so the choice of boundary value on C1 is immaterial; and $1+x=0$ only at $Z=0$. Hence the textbook argument principle applies on the Jordan curve $\partial D$ (no boundary-continuity version is needed). At the corner, $B(-1)=1-1/\sqrt2$ ($x(-1)=-(3-2\sqrt2)$), so
$$
g_0=\frac{-A}{B-A}=\frac{Z+1}{3(1-1/\sqrt2)}+O(|Z+1|^2); \tag{3.7}
$$
near $-1$, $D$ lies in $\Im(Z+1)\ge0$, with $\Im(Z+1)=0$ only on C1, where $A,B$ are real and $g_0\le0$: $g_0(\partial D)$ meets $[0,1]$ only at $0$, at $Z=-1$. Argument principle: if $B-A$ has no zero on $D$ (no zero on $\partial D$, winding number $0$ of $(B-A)(\partial D)$ about $0$), $g_t(\partial D)$ misses $(0,1]$, and its winding number about $\tfrac12$ is $0$, then $g_t-p$ has no zero in $D$ for every $p\in(0,1]$ (the count is the winding number about $p$, constant on the connected $(0,1]$ which the curve misses). $g_t=0$ iff $A=t$: $A=1\iff Z=\tfrac12\notin D$; $A=1/Z\iff Z=2\notin D$; $A=0\iff Z=-1$. Hence
$$
\{Z\in D:\ \exists j,\ t_j(Z)\in[A(Z),B(Z)]\}=\{-1\}\ (j=3\text{ only}). \tag{3.8}
$$
(3.8) says where (3.6) cannot decide, not that $\mu_{13}$ vanishes there (critic iteration 2, #2). At $Z_0=-1$, $A=0$ and $B=1-1/\sqrt2$, so for a general weight $\mu_{13}(-1)=S_0(-1)\,L(-1)\,(1-1/\sqrt2)$, which vanishes iff $L(-1)=0$. The segment argument is silent there; the zero comes from the package's $L=O(|\delta|^2)$, (3.3), or from any weight meeting the corner condition $R(-1)=\infty$ (the condition that (3.2') imposes on an $S_4$-symmetric section, transported to the FD corner).

*Computation* (`C2-segment-no-pole`, `C2-segment`, `C2-segment-corner`, `BREAK-C2-segment`; $\partial D$ sampled counter-clockwise by $4\times20000$ points, largest argument step $<0.2$ rad asserted):

[Table of companion-project values removed.]

All windings about $\tfrac12$ (and of $B-A$ about $0$) are $0$ at both $\beta$; the break leg (planted $t^*=A+\tfrac12(B-A)$ at $Z^*=-0.3+1.5i\in D$) has winding $1$ at both $\beta$.

`C2-closed-forms`: $\max\big||\mu_{1j}|-|S_0||1/R-1/\zeta_j|\big|\le2.6\times10^{-15}$ (200 random points of $D$, three pairs, jet route of (1.5) against (3.4)); $|\mu_{1j}(e^{i\pi/3})|=1/(\sqrt3\beta)$ to $10^{-12}$ for $j=2,3,4$ at $\beta=\tfrac32$ and $2$. `C2-zero-at-half` now asserts the slope against $2\sqrt2/(3\beta)$ (agreement $2\times10^{-5}$ at $r=10^{-4}$), `C2-symmetric-zeros` the $Z_0=-1$ slope against $|S_0(-1)|/3$.

\subsection*{Commentary}
(3.3) answers critic #1: (3.2)'s premise (the section defined and symmetric at the corner) holds for the package; (3.4) at $Z_0=-1$ then gives $\mu_{13}=0$ from the formula alone. (3.6) is weaker than an equivalence: it discards the weight, so it can only fail to decide, never give a false "no zero"; it decides here because the three points stay far from the segments except at the one corner where $A=0$. The argument principle turns the two-dimensional question into a one-dimensional one on $\partial D$; the boundary data are sampled (boundary sampled, not interval arithmetic), but on a curve, with the argument steps bounded and distances bounded below (companion value, not reproduced here) against steps of order $10^{-4}$ in $Z$ [open, Fix pass 2 #8: this compares a distance in the $g$-plane with a step in the $Z$-plane; the relevant inequality, $\max_k|g(Z_{k+1})-g(Z_k)|$ below half the local distance to $[0,1]$, is not yet asserted by the script – the critic's hand estimate gives steps $\lesssim0.1$ in $g$ where the distance is (companion value, not reproduced here), and $\sim2\times10^{-4}$ where it is (companion value, not reproduced here)]. The transport (C2.3) carries (3.8) to all twelve tiles: the $s$-pair at $Z$ is the pair $(\pi^{-1}(1)\pi^{-1}(2))$ at $Z_0$, and it vanishes only where that pair is in the class of $(13)$ at $Z_0=-1$, i.e. at $Z=\tfrac12$ (at $Z=-1$ and $Z=2$, the other points of the orbit, the $s$-pair is $1/(\sqrt2\beta)\ne0$, checked at $\beta=\tfrac32$). The criterion is weight-independent, so it also tests a later revision of the weight by the sister project, as long as the weight stays in $[0,1]$ and the anchors $A$, $B$ are kept (critic #8).

\subsection*{Result}
$$
\boxed{\ \text{for every weight }L\in[0,1]:\ \mu_{1j}\ne0\ \text{on }D\ \text{except possibly }\mu_{13}\text{ at }Z_0=-1;\qquad \mu_1=\mu_2\ne0\ \text{on }\overline{\mathcal V_{0,4}}\setminus\{Z=\tfrac12\}\supset Q_V\ }
$$
where $\mu_{13}(-1)=S_0(-1)\,L(-1)\,(1-1/\sqrt2)$ vanishes iff $L(-1)=0$: true for the package's weight (3.3), and for any weight meeting the corner condition $R(-1)=\infty$. Given the package's formulas ($S_0$, the anchors, the weight's range, the Klein maps and the transport; provisional with the package). Tag: Numerical (analytic reduction; winding numbers from a sampled boundary, not interval arithmetic; $\beta=\tfrac32$ and $2$, hence every $\beta\le2$ by nesting: $A$, $B$, $t_j$ are $\beta$-independent and $D(\beta)$ grows with $\beta$). For $\beta>2$ the claim is not covered (see Fix pass 2, #5). [C2.6, C2.7]

## §4 (C4) – Across an arc

\subsection*{Setup}
PH34, A4. Path $Z(t)=Z_*+tn$ with $Z_*=e^{2\pi i/3}$ on the arc $|Z|=1$ (wall C3 of the FD, between $e^{i\pi/3}$ and $-1$), $n=e^{2\pi i/3}$ (radial; $t>0$ in the FD). Quantities: $\mu_1^{\rm A4}$, $g_1:=\mu_1^{\rm A4}/|a_1^{(u)}|=\beta(R_1-u_2)/(R_1-u_1)$ (a function of $c_1$ alone, by $R_1=N^{-1}(-1/2c_1)$), and $|a_1^{(u)}|$. One-sided degree-5 fits on 16 points $t=\pm kh$, $h=2\times10^{-3}$ and $10^{-3}$; a jump is real when stable under $h\to h/2$ (ratio within $5\,\%$).

\subsection*{Derivation}
Jumps (side $t>0$ minus side $t<0$), $\beta=\tfrac32$, $h=10^{-3}$:

[Table of companion-project values removed.]

The value jumps are below $2\times10^{-12}$ for all five quantities and the first-derivative jumps of $g_1$ are at the level of $10^{-9}$; $\beta=2$: the same pattern. Controls (wall $\Re Z=\tfrac12$ at $\tfrac12+1.3i$, horizontal; interior point $-0.3+1.5i$): all value and first-derivative jumps $\le7\times10^{-12}$, second-derivative jumps $\le7\times10^{-9}$. $\tag{4.1}$

\subsection*{Commentary}
The pattern is PH34's, read through (1.4): $\mu_1^{\rm A4}=|a_1^{(u)}|\,g_1$ with $|a_1^{(u)}|$ continuous with a kink and $g_1$ (through $c_1$) $C^1$ with a second-derivative jump. So at the tested point $\mu_1$ itself is $C^0$, not $C^1$, across the arc — the brief's expectation ("$\mu_i$ and its first derivative continuous, a jump in the second") holds for $g_i$, not for $\mu_i$. Nothing in the a.e. argument needs more than continuity: the zero set of $\mu_i$ is that of $g_i$ ($|a_i|>0$). The first-derivative jump of $|a_1^{(u)}|$ across the arc is (companion value, not reproduced here) at $\beta=\tfrac32$ and $\beta=2$ (observed, not derived). One arc point is tested, for the pair $(1,2)$ only. The transport argument is incomplete: by C2.3, $\mu_{12}$ across the arc $g\cdot{\rm C3}$ is $\mu_{\pi^{-1}(1)\pi^{-1}(2)}$ across C3, so covering $\mu_{12}$ on all six arcs needs $\mu_{12},\mu_{13},\mu_{23}$ across C3, and only $\mu_{12}$ was run (fix pass 1, critic #6). Low stakes: downstream only $C^0$ is used, and $C^0$ follows from the section's continuity.

\subsection*{Result}
At the tested arc point $Z=e^{2\pi i/3}$, pair $(1,2)$, $\beta=\tfrac32$ and $2$: $\mu_1\in C^0\setminus C^1$; $g_1\propto(R_1-u_2)/(R_1-u_1)$ in $C^1\setminus C^2$ (provisional with the package; other arc points and pairs not run). [C4]

\subsection*{Verification}
`C4-arc-C0`, `C4-arc-kink` (all four sub-statements true at both $\beta$), `C4-control` (the method shows no jump where none is expected: the falsifiability leg).

## Verification – run

Fix pass 1: `OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 /usr/bin/time -v .venv/bin/python codes/verify-mu-table.py`: `SUMMARY: 56/56 PASS`, single process, seed 20261004; final run quoted in the Fix pass section. Partial results now in `agent/scratch/computator/computator-089-fix-20261004T210100/partial.json` (the script's scratch path moved to the fix pass's folder); outputs `run*.txt` there. Changes: 10 new checks (per $\beta$: `C2-segment-no-pole`, `C2-segment`, `C2-segment-corner`, `BREAK-C2-segment`, `C2-closed-forms`), `BREAK-C3-alpha0` replaced by `BREAK-C3-boundary-lambda0`, `BREAK-C3-wrong-pair` relabelled `SANITY-C3-wrong-pair`, `C3-boundary-limit` asserts the rate, `C2-zero-at-half` and `C2-symmetric-zeros` assert the derived values (3.5). One FAIL during the fix pass: `C2-segment[b=2.0]` on its first run, the threshold $0.5$ on $\min{\rm dist}/|Z+1|$ was applied over all of $\partial D$, where far from the corner the ratio is small only because $|Z+1|$ is large ($0.487$); a typo in the check, fixed by applying the scale-invariant bound on $|Z+1|<0.1$ only and the plain distance elsewhere (the result was unchanged).

Original run (before the fix pass): `SUMMARY: 46/46 PASS (14.5 s)`, peak RSS 88896 kB; outputs in `agent/scratch/computator/computator-089-mu-table-20261004T202400/` (`run5.txt`). Earlier runs there: the first full run had 4 FAIL (`C2-no-zero` and `C2-refinement` at both $\beta$) – the zero of §3; a second run had 1 FAIL (`C2-refinement` at $\beta=\tfrac32$, excision-circle artefact, §3 Commentary); one transcription fix before that (`C3-sympy-mu`: sympy returned `nan` for $F_2$ before `cancel`; the result was unchanged, the check's simplification was wrong).

## Self-review

1. *Objective.* Answered: the per-tile non-vanishing holds on every tile (numerically, provisional with the package), and the zero set is located: one symmetric point on the fold boundary of $Q_V$. The critic's planned hand argument (critic-fable-decisions-sec6, Q2/#4) can now cite C2.3 (equivariance: three functions on the FD) and C3 (non-zero boundary value $\tfrac1{2\beta}$ on $\partial_s$, where the FD meets the $s$-ellipse); it needs only those boundary values and is unaffected by C2.4. A stronger "nowhere zero on $\mathcal V_{0,4}$" would be false: $\mu_{13}$ vanishes at the FD corner $Z_0=-1$ (the image of $Z=\tfrac12$).
2. *Weakest step.* Before the fix pass: C2.5, from a grid to every point (sampled minima, a narrow zero pair could escape). Now replaced by C2.7, which reduces the zero question to one explicit holomorphic function per pair on the FD and decides it by the argument principle on the boundary; its remaining weakness is that the boundary data are sampled (boundary sampled, not interval arithmetic; hence the tag Numerical), with large margins, and that it is a statement about the package's formulas, themselves unreviewed. It is weight-independent, so it is also a criterion against which the sister's eventual revision of the weight can be tested (critic #8).
3. *Not checked.* The package's section construction itself (only its $s$-channel maps are checked independently, C3.1); arcs other than one point, and the pairs $(1,3)$, $(2,3)$ across the arc; $\beta>2$ (C2.7 is run at $\beta=\tfrac32$ and $2$; $A$, $B$, $t_j$ and the weight's range do not depend on $\beta$ and only the domain $D(\beta)$ does, growing with $\beta$, so the $\beta=2$ run covers every $\beta\le2$ by nesting; for $\beta>2$ the critic suggests a tail bound on $|Z|\ge R_0$ ($A=\tfrac13+\tfrac1{3Z}$, $B=\tfrac12+\tfrac1{4Z}+O(Z^{-2})$, so $g_1\to4$, $g_0,g_{1/Z}\to-2$) plus one run at a $\beta$ whose ellipse contains $|Z|\le R_0$, e.g. $R_0=10$, $\beta\approx3.3$: an optional light task, not done); the derivative-jump value of $|a_1|$ across the arc (companion value, not reproduced here; observed, not derived).
4. *What a stronger reader would add.* That the zero at $Z=\tfrac12$ is a theorem for any $S_4$-symmetric section defined there, Möbius by (3.2) and general by its 2-jet form (3.2'), independent of the package; and that the R84 criterion therefore holds on one surface of $\mathcal V_{0,4}$ — a measure-zero exception to be stated wherever R86 says "every point".

## Proposed ledger lines

Promoted on 2026-10-04 with the text of `agent/reports/critic-089-iter2-20261004T211500.md` (*R86 / PH34 text acceptable to this review*); see `knowledge/results.md` R86, PH34.

## Fix pass (critic iteration 1)

Brief `computator-089-fix-20261004T210100`, critic report `critic-089-20261004T204300` (REVISE, light: 0 critical, 1 major, 9 minor, 2 notes). One line per finding.

- **#2 (major), applied.** (a) C0, C2.5, the §3 Commentary and Result and the proposed R86 lines now call the minimum of $|\mu_1|$ outside the disc and the slope bound inside it sampled minima at grid points, not bounds; "PH34 for the interpolation" is dropped everywhere. (b) The critic's segment check is added as §3b, (3.6)–(3.8), node C2.7: on $D={\rm FD}\cap\mathcal V_{0,4}$ a zero of any pair's $\mu$ needs $t\in\{1,0,1/Z\}$ on the segment $[A,B]$; with $g_t=(t-A)/(B-A)$ holomorphic on $D$, the argument principle on $\partial D$ decides it for every weight with values in $[0,1]$. Result at $\beta=\tfrac32$ and $2$: no zero on $D$ except possibly $\mu_{13}$ at the corner $Z_0=-1$ (the known zero, image of $Z=\tfrac12$, for the package's weight; "possibly" since Fix pass 2 #2); the corner is not excised but handled by the expansion (3.7), so the check applies on all of $D$. What it proves: given the package's formulas ($S_0$, the anchors, the weight's range, the Klein maps, the transport), $\mu_1=\mu_2\ne0$ at every point of $\overline{\mathcal V_{0,4}}\setminus\{Z=\tfrac12\}$, hence of the open $Q_V$, without PH34. What it does not prove: anything about the section's construction (unreviewed), and its boundary data are sampled (no interval arithmetic). Break leg: a planted point on the segment gives winding $1$. Wording upgraded to "every point of $Q_V$, given the package's formulas" and no further.
- **#1, applied.** The sentence "the package cannot evaluate at this corner" is replaced (§3) by the continuity of the section at the corner, (3.3), and the formula route $\mu_{13}=S_0/R=0$ at $Z_0=-1$, (3.4), cited from C2.4.
- **#3, applied.** The claim tree's PH34 restatement corrected: $|a_j|$ has a kink across the six arcs, not at $\partial\mathcal V_{0,4}$, where it joins $C^1$ (the old wording is quoted in the node). The PH34 heading clarification is proposed to the orchestrator in the ledger lines.
- **#4, applied.** "Provisional with the package" added to the Status line, the §2 Result (the approach from $Q_V$ rests on `section_maps` alone), the §4 Result, the proposed PH34 line, and C0, C3.4, C4.
- **#5, applied.** (3.4)–(3.5) derive $|\mu_{1j}|=|S_0||1/R-1/\zeta_j|$, $|\mu_{12}(-1)|=1/(\sqrt2\beta)$, the slope $2\sqrt2/(3\beta)$ at $Z=\tfrac12$ (and $|S_0(-1)|/3$ at $Z_0=-1$), $|\mu(e^{i\pi/3})|=1/(\sqrt3\beta)$; node C2.6; `C2-closed-forms` checks (3.4) against the jet route at 200 points ($2.6\times10^{-15}$) and the $e^{i\pi/3}$ value; `C2-zero-at-half` and `C2-symmetric-zeros` now assert the derived slopes. Self-review 3 no longer lists the slope.
- **#6, applied (scoping).** C0, C4, the §4 Commentary and Result and the PH34 line are scoped to the tested point $Z=e^{2\pi i/3}$ and the pair $(1,2)$; the §4 Commentary states why the transport argument is incomplete. $\mu_{13}$, $\mu_{23}$ across the arc were not run.
- **#7 (note), not applied.** The A4 phase stays local; registering it in `knowledge/conventions.md` is the orchestrator's call if R86 quotes signed $\mu$ values.
- **#8 (note), applied.** One sentence in the §3b Commentary and Self-review 2: the criterion is weight-independent and can test the sister's eventual revision of the weight.
- **#9, applied.** Erratum paragraph inserted after the Status section of record 080 (A7 l. 27, §3 Setup l. 151, C3.3 l. 169 with "$|q|>1$" → "$|q|<4\beta^2$", `setup-u2-ne-u4` l. 185), no claim changes, sections not rewritten. Record 074 checked (A2, (1.6), §1 Setup l. 51): no slip there – A2's $u_Au_B=q$ is written for the disc coordinates ($w$ in 074 §1), and (1.6) keeps the positions at $\pm2\beta$ in the $w$-frame; 080's slip came from reading 074's $u$ as the circle-frame $u=1/w_A$. No erratum line in 074. The proposed "Correction to record 080 §3 / R86 Scope" ledger line is replaced accordingly.
- **#10, applied.** `C3-boundary-limit` asserts $|{\rm rate}-2|<0.1$ (measured rate: companion value, not reproduced here).
- **#11, applied.** C2.2, C2.3 and the §3 Verification state that `C2-klein` and `C2-equivariance` hold by construction of the package and test the reading of its labels, permutation and phase; the step list, the §1 Verification and the script docstring state that `C1-three-routes` cannot detect a wrong $u_{3,4}$, and name the checks that test the dictionary.
- **#12, applied.** `BREAK-C3-alpha0` replaced by `BREAK-C3-boundary-lambda0` (the pipeline of `C3-boundary-limit` fed with glued $\lambda=0$ halves fails by $\tfrac1{2\beta}$; $\lambda=\tfrac12$ halves through the same code pass at $2\times10^{-16}$); `BREAK-C3-wrong-pair` relabelled `SANITY-C3-wrong-pair`.

**Changed nodes.**
- C0: statement changed (sampled minima instead of bounds; "every point" now by C2.7, not PH34; slope stated; arc clause scoped to one point and pair; provisional explicit).
- C2.5: statement changed (sampled minima, no PH34, no "every point").
- C2.6, C2.7: new nodes.
- C4: statement changed (scoped to $Z=e^{2\pi i/3}$, pair $(1,2)$).
- C2: justification changed ([by C2.1–C2.7]); title widened to "and the zero set".
- C2.4: justification changed (corner premise (3.3), second route (3.4), derived slope (3.5)); statement unchanged.
- C2.3: statement adds $|\mu_{23}|=|\mu_{14}|$ and the by-construction remark; content unchanged.
- C2.2, C3.4: justification changed (check scope; rate asserted, break leg replaced); statements unchanged.
- PH34 restatement: corrected to the ledger body (no status change).
- `Hypotheses in force:` changed: PH34 is no longer used by C0.

**Dependents.** C2.4, C2.5, C2.6, C2.7 → C2 → C0; C3.4 → C3 → C0; C4 → C0. Each holds as revised: C2 holds with C2.7 carrying the every-point claim and C2.5 reduced to sampled evidence; C3 is unchanged in statement; C0 holds in its revised form. All restatements updated: Status, Answer in one line, §2/§3/§3b/§4 Results, Verification blocks, Verification – run, Self-review, proposed ledger lines. By the schema the root statement and the `Hypotheses in force:` line changed, so the next pass is a full re-review; the substantive new material is §3b.

**Script.** `OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 /usr/bin/time -v .venv/bin/python codes/verify-mu-table.py` (final run, after `ruff format`): `SUMMARY: 56/56 PASS (15.7 s)`, exit 0, peak RSS 106028 kB, single process, seed 20261004; output `agent/scratch/computator/computator-089-fix-20261004T210100/run-final.txt`.


## Fix pass 2 (critic iteration 2)

Brief `computator-089-fix2-20261004T213300`, critic report `critic-089-iter2-20261004T211500` (REVISE, mechanical: 0 critical, 1 major, 5 minor, 3 notes; §3b holds, all twelve iteration-1 findings landed).
Wording only: no script run (`codes/verify-mu-table.py` stays at 56/56 PASS from fix pass 1), no number changed, no new check.
One line per finding.

- **#4 (major, tagging), applied.**
  - The every-point claim is Numerical (analytic reduction; winding numbers from a sampled boundary, not interval arithmetic; $\beta=\tfrac32$ and $2$, hence every $\beta\le2$), no longer Verified: §3b Result (the word "Verified" is gone from the record; grep), C2.7, Status.
  - The proposed R86 Status consequence (old l. ≈275) is dropped with the whole *Proposed ledger lines* section (below); the critic's accepted text carries the Numerical tag.
  - The per-tile step is tagged "Numerical, provisional with the package" again: C0, Answer in one line, §3 Result.
  - "Boundary sampled, not interval arithmetic" added at Status, Answer in one line, C0, C2.7, §3 Result, §3b Commentary, §3b Result, Self-review 2. The Statement clause was in the dropped ledger section.
- **#2, applied.**
  - "except $\mu_{13}(-1)=0$" → "except possibly $\mu_{13}$ at $Z_0=-1$, where $\mu_{13}(-1)=S_0(-1)L(-1)(1-1/\sqrt2)$ vanishes iff $L(-1)=0$ – true for the package's weight (3.3), and for any weight meeting the corner condition $R(-1)=\infty$": C2.7, the §3b Result box, a paragraph after (3.8), and the quoted Fix pass 1 #2 line.
  - In C0 the "only zero … at $Z=\tfrac12$" is now attached to the package's weight. The Answer line likewise.
- **#3, applied.** The 2-jet argument is added right after (3.2) as (3.2'): $\psi(\zeta)=-\zeta-2\zeta^2+O(\zeta^3)$, $F_1(-W)=\psi(F_1(W))$ at order $W^2$ gives $b=-a^2$, $c_1=-\tfrac12$, so $\mu_{12}=a/(0-1)-2a(-\tfrac12)=0$ by 080 (1.7); the Möbius form (3.2) is the case $b=-a\nu$, $\nu=a$. Cited in C0, C2.4, the §3 Result and Self-review 4. Hand-checked, not machine-checked (no run in this pass).
- **#5, applied.**
  - Stated in C0, C2.7, the §3b Setup and Result, Self-review 3, the Status line and the Answer line: $\beta=\tfrac32$ and $2$, hence every $\beta\le2$ by nesting ($A$, $B$, $t_j$ and the weight's range do not depend on $\beta$, $D(\beta)={\rm FD}\cap\{\Re\,{\rm arccosh}(2Z-1)\le\ln4\beta^2\}$ grows with $\beta$).
  - The corner $-1\in D(\beta)$ iff $\beta\ge(1+\sqrt2)/2$ (hand check of the critic's remark: $\Re\,{\rm arccosh}(-3)=2\ln(1+\sqrt2)$), below which $\mu\ne0$ everywhere.
  - Not covered: $\beta>2$. The critic's tail-bound plus one run at $\beta\approx3.3$ is an optional light task, not done.
- **#1 (note), applied.** (3.6)'s holomorphy sentence replaced by the critic's wording: $B$ is holomorphic on a neighbourhood of $D$ ($x=e^{-w}$ has no jump across $2Z-1<-1$: $w=r\pm i\pi$ on its two sides, $e^{-w}=-e^{-r}$ on both), so $g_t$ is meromorphic on a neighbourhood of $D$ and the textbook argument principle applies.
- **Proposed ledger lines, replaced** by the line "Promoted on 2026-10-04 with the text of `agent/reports/critic-089-iter2-20261004T211500.md` (*R86 / PH34 text acceptable to this review*); see `knowledge/results.md` R86, PH34." The R86 Verification line, the Status consequence, the PH34 line and the record 080 / R86 Scope bullet are no longer in the record.
- **#8 (minor), open, not applied.** The §3b Commentary sentence compares a distance in the $g$-plane with a step in the $Z$-plane. The fix is a light script task (print $\max_k|g(Z_{k+1})-g(Z_k)|$ per $t$ and for $B-A$ about $0$; away from the corner assert it is below half the local distance; rely on (3.7) inside $|Z+1|<10^{-2}$; restate the Commentary in $g$-steps). It needs a run. The Commentary now carries an `[open, Fix pass 2 #8]` mark and the critic's hand estimate, which changes no conclusion.
- **#9 (minor), open, not applied.** (a) `A_seg`, `B_seg` re-type the package's anchors: assert $|1/{\rm R\_interior}(Z)-(A+L(B-A))|<10^{-13}$ at the 200 random points of `C2-closed-forms`; (b) move the weight-range assertion ($0\le L\le1$, 2000 samples) out of `BREAK-C2-segment` into that check, so a failure is not ambiguous. Needs a run.
- **#6, #7 (notes), no record change** (the critic's own routing): #6 is the orchestrator's call on the Statement clause (every-point primary, a.e. clause a remark); #7 is the interval-arithmetic route to `Proven`/`Verified` if R86 ever needs it.

**Changed nodes.**
- C0: statement changed (Numerical tag, "boundary sampled, not interval arithmetic", $\beta\le2$ by nesting, the $Z=\tfrac12$ zero attached to the package's weight and to the 2-jet form).
- C2.7: statement changed ("possibly except $\mu_{13}$ at $Z_0=-1$", Numerical, $\beta\le2$); justification unchanged.
- C2.4: justification extended (2-jet form (3.2')); statement unchanged.
- Not changed: C2.6, C2, C2.1–C2.3, C2.5, C1, C3, C4 (statement and justification), the PH34 restatement, `Open gaps:` and `Hypotheses in force:`.

**Dependents.** C2.7 → C2 → C0: C2 holds as before (its justification [by C2.1–C2.7] is unchanged and the C2.7 change only weakens "the only zero" to "possibly"); C0 holds in its revised form, and its every-point clause (statement) is unchanged apart from the tag.
The root statement is weaker only in tagging: no claim is dropped.
All restatements updated: Status, Answer in one line, C0, C2.4, C2.7, §3 (after (3.2), Result), §3b (Setup, after (3.6), after (3.8), Commentary, Result), Self-review 2–4, the ledger section.

**Open gaps:** none (claim tree unchanged). Open script items (not gaps): #8, #9; optional $\beta>2$ extension.
