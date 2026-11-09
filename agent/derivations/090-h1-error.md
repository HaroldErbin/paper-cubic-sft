# 090 — Sub-task N1 of record 081: the error of H1 (centroid centre) and the scale (1.3′) against the companion's section

Brief: `agent/briefs/active-computator-090-h1-error-20261004T202400.md`. Script: `codes/verify-h1-error.py` (25/25 PASS, seed 20261004, `agent/scratch/computator/computator-090-h1-error-20261004T202400/run7.log`; numbers in `h1-error.json` there; run 7 precedes the fix pass's tolerance change in `C4-relative-tile-invariant`, written, not yet run).

**Literal task.** Execute N1 of record 081 §5.2: measure $\varepsilon_{\rm H1}(m)=|c(m)-(1+m)/3|$, $c=-2c_3$, $c_3$ from `section_jets(m, beta)[3]` of the companion package (v2.0.0), and $1/|a_3|$ against the scale (1.3′) of 081, at 081's sample points, on $\partial\mathcal V_{0,4}$ and across one of the six arcs; decide whether H1 is adequate for N2–N3 or those should call `section_jets`.

**Motivating objective.** 081's covering test (N2, N3) needs the patch's special coordinate $w=\lambda(m)/(u-c(m))$; H1 replaces $c(m)$ by the centroid. This record decides by measurement whether that is good enough, and what N2–N3 must change if not.

## Conventions and assumptions

- **A1–A5** of record 081, verbatim (book conventions; plumbing $w_Lw_R=q$; $\mathcal V_3'$ = R2's half; surfaces only; Möbius special coordinate). $\beta=\tfrac32$ throughout.
- **A6** (inherited from 081 §1, not re-decided) Frame $\{0,1,m,\infty\}$, $m\equiv Z$ of the sister's frame $(z_1,z_2,z_3,z_4)=(0,1,\infty,Z)$; the special leg is label 3; dictionary $|a_3|=1/|\lambda|$, $c_3=-c/2$ (081 (1.3), C7 chart $t=1/z$); scale (1.3′) with 081's phase convention.
- **A7** The package v2.0.0 is used as shipped (imported by path, not edited), with the declared scheme constant $\lambda_0$ of the $\Lambda_1$ weight (value from the companion SL(2,C) computation, not reproduced here).

Free constants: none. Nothing is fitted; every comparison is between two independently defined quantities (or a closed form and the package).

## Claim tree

- **A1–A7** as above.
- **Cited source** (provisional, not a hypothesis): the package v2.0.0 implements the sister's declared section (034 (2.4′); its verifier not yet reviewed by the sister's critic). Every number below is a property of that section, conditional on that source (fix pass, #1). PH34 (ledger, supported, provisional) is the section's regularity statement, resting on the same source; it is not assumed here – C5 tests it at one point.
- **C1** The dictionary $c=-2c_3$, $|\lambda|=1/|a_3|$ reproduces 081's construction where H1 is forced by symmetry: $\varepsilon_{\rm H1}=0$ at $e^{\pm i\pi/3}$ ($10^{-16}$) and, as limits, at $-1,\tfrac12,2$ (the package raises `ZeroDivisionError` exactly there, a removable singularity: $R=\infty$, $c=Z/R=0$ at $Z=-1$). [by check: C1-dictionary-symmetric, C1-dictionary-break]
- **C2** For the declared section (034 (2.4′), package v2.0.0), on the FD, $c(m)-\tfrac{1+m}3=L(m)\,D(m)$ with $L=\Lambda_1\in[0,1]$ and $D$ of (2.1); hence H1 is exact on the whole of the six arcs (not only at the symmetry points) and vanishes quadratically off them. [by C2.1, C2.2]
  - **C2.1** Closed form (2.1) from the sister's (2.4′). [cited: sister derivation 034 eq. (2.4′), via the package's `R_interior` docstring; eq. (2.1)] [check: C2-closed-form-FD]
  - **C2.2** $L=0$ on $C_3$, and the centroid property of the anchor section is $S_4$-covariant, so $\varepsilon_{\rm H1}=0$ on all six arcs. The exactness comes from the declared section's construction ($R=R_{\rm anchor}$ on $C_3$, forced within 034's affine interpolation because $R_{\rm naive}$ fails $C_3$); symmetry alone fixes only $c\in e^{i\varphi/2}\mathbb R$ there. It holds for every weight vanishing on $C_3$ (the whole $\Lambda_1$ family, every $\lambda$), not for an arbitrary admissible section. [by C2.1; block (2.2)] [check: C2-arcs-zero, C2-arcs-break]
- **C3** (1.3′) is the package's transport: $1/|a_3|=|\lambda_{(1.3')}|$ on all twelve tiles and on $\partial\mathcal V_{0,4}$; $c$ obeys 081's affine equivariance $c(gm)=a_gc(m)+b_g$ (S₃ fixing label 3) although the package transports by the S₃ fixing label 4. First machine test of (1.3′) off the FD (081 §5.3's open item). [by check: C3-scale-all-tiles, C3-scale-boundary, C3-equivariance-c, with break legs]
- **C4** Size of the error (measurement): $\varepsilon_{\rm H1}$ at $m=-\tfrac{16}9,\tfrac{25}9$ on $\partial\mathcal V_{0,4}$ (exact value, (4.1): companion value, not reproduced here); that it is the global maximum is a grid and boundary-sampling measurement (fix pass, #4); per-tile maxima as in §4 (companion values, not reproduced here); the relative error $\varepsilon_{\rm H1}/|\lambda|$ is tile-invariant, with its maximum just inside $\partial\mathcal V_{0,4}$ on the real wall (numerical: bounded search on the real wall and Nelder–Mead; boundary value (companion value, not reproduced here)). On $\partial\mathcal V_{0,4}$ $c$ equals the glued channel maps' centre ($C^0$ join). [by check: C4-boundary-channel, C4-boundary-exact-value, C4-abs-max-on-boundary, C4-rel-max-interior, C4-relative-tile-invariant; table §4]
- **C5** Across the arc $|m|=1$ at $\arg m=\tfrac{2\pi}3$: $f=c-\tfrac{1+m}3=A_\pm\delta^2+O(\delta^3)$ on both sides ($C^1$), $A_+$ equal to the closed form (5.1), $A_-=e^{i\varphi}\bar A_+$ (predicted from 081's $g=1/m$ equivariance and conjugation), so $c$ is not $C^2$ while $|A_+|=|A_-|$: $\varepsilon_{\rm H1}$ is $C^2$ at leading order there, only the phase of $c$'s second-order term jumps; $|\lambda|$ has the kink (1.3′) predicts. Consistent with PH34 at that point. [by check: C5-arc-C1, C5-arc-not-C2, C5-arc-prediction, C5-arc-closed-form, C5-arc-break, C5-arc-scale-kink]
- **C6** Verdict: H1 is not adequate for N2–N3; they should take $c=-2c_3$ from the package (with the three operational changes of C6.3–C6.4). [by C4, C6.1–C6.4]
  - **C6.1** The limit moduli of 081 (3.1) move: `near-boundary`'s $\mu_L$ goes from outside $\mathcal V_{0,4}$ (under H1) to inside (under the section), so C4.1's prediction for that ray changes from a (d) chain region to an own-channel $\mathcal V_4\mathcal V_4$ re-entry; the other three predictions stand; over the grid, membership of $\mu(m)$ disagrees on a fraction of $\mathcal V_{0,4}$ (companion value, not reproduced here). [by C3.1 of 081, check: C6-moduli-transcription; measurement §6]
  - **C6.2** The six-point moduli (081 (2.2)) shift by (companion values, not reproduced here) at $|q|=1,3,12$ (zero at `sym-sym`). [measurement §6]
  - **C6.3** $c(m)$ from the section is not holomorphic ($|\partial_{\bar m}c|/|\partial_mc|$ at $-1.3$, the largest of four sample points: companion value, not reproduced here – a measurement): 081's complex $3\times3$ Jacobian is invalid with it; N2 and N5 need the real $6\times6$ Jacobian, and 081 §5.1 item 2's "holomorphic on each product tile" holds under H1 only. Consequence for the fold analysis (fix pass, #6): for the holomorphic H1 map $\det J_{\mathbb R}=|\det J_{\mathbb C}|^2\ge0$, the critical set has real codimension 2 in the 6-real-dimensional $(m_L,m_R,q)$ and generic rays miss it, so folds of the $x\mapsto|x|$ type occur only at product walls (081 N5's set-up); with the section's $c$, $\det J_{\mathbb R}$ can change sign inside a tile – the critical locus is generically a real hypersurface met by generic rays – so folds are possible inside tiles, and N5 must look for sign changes of $\det J_{\mathbb R}$ in tile interiors. [by check: C6-nonholomorphic]
  - **C6.4** Operational: the package fails at exactly $m=-1,\tfrac12,2$ (use H1's value there, exact by C1); `section_maps(strict=True)` raises off $\mathcal V_{0,4}$, so the root find needs an extension there – the package's channel maps, $C^0$ join verified (C4), $C^1$ per PH34 not tested here. [by C1, C4]

Open gaps: none
Hypotheses in force: none. The numbers are conditional on the cited source – the package v2.0.0 implementing the sister's declared section (provisional, unreviewed by the sister's critic) – not on PH34, which C5 tests at one point; H1 of 081 is the object measured here, not in force.

## §1 Dictionary at the symmetry points (C1)

\subsection*{Setup}
A6, A7. `jet3(m)` = `jets(section_maps(m, beta))[3]` $=(a_3,c_3)$; $c_{\rm sec}=-2c_3$.

\subsection*{Derivation / numbers}
On the FD the section is $F_1=RSW/(SW+R)$, $F_3=Z/F_1=(ZSW+ZR)/(RSW)$, i.e. the Möbius tuple $(ZS,ZR,RS,0)$; the package's `mobius_jet` at infinity gives $a_3=-\det/B^2=S/Z$, $c_3=AB/(2\det)=-Z/(2R)$, so $1/|a_3|=|Z/S|=|\lambda|$ and $c=-2c_3=Z/R$ – 081's (1.3) dictionary, re-derived from the package's closed forms.
$$
\varepsilon_{\rm H1}(e^{\pm i\pi/3})=1.1\times10^{-16},\qquad \varepsilon_{\rm H1}(-1+10^{-9}i)=5\times10^{-26},\quad \varepsilon_{\rm H1}(\tfrac12+10^{-9}i)=7\times10^{-25},\quad \varepsilon_{\rm H1}(2+10^{-9}i)=2\times10^{-25}.
\tag{1.1}
$$
Break leg: $c=+2c_3$ gives $1.155,1.155,1.000,2.000$ at $e^{\pm i\pi/3},\tfrac12,2$ (at $-1$ both signs give $0$; that point cannot discriminate the sign).

\subsection*{Commentary}
The package evaluates `R_anchor` $=3Z/(1+Z)$ before inverting, so `section_jets` raises `ZeroDivisionError` at $Z=-1$ and at its images $\tfrac12,2$ (the transport lands on $Z_0=-1$). The singularity is removable ($1/R=0$ there; $F_1\to SW$), so the limits are evaluated $10^{-9}$ away. The offset points lie on or tangent to the arcs where $\varepsilon_{\rm H1}\equiv0$ ($\tfrac12+10^{-9}i$ on $\Re m=\tfrac12$; $-1+10^{-9}i$, $2+10^{-9}i$ along the tangents of $|m|=1$, $|m-1|=1$, at distance $\approx5\times10^{-19}$ from them); the values are round-off (fix pass, #2).

\subsection*{Result}
The dictionary holds; $\varepsilon_{\rm H1}=0$ at the five symmetry points. [C1]

## §2 Closed form on the FD; exactness on the arcs (C2)

\subsection*{Setup}
A7. The companion's declared section: an affine interpolation between the anchor and the $C_4$ datum with a weight $L$ built from $d_3=(|Z|^2-1)(|Z-1|^2-1)$ and $d_4=\log4\beta^2-\Re w$, $w=\operatorname{arccosh}(2Z-1)$ (explicit formula from the companion SL(2,C) computation, not reproduced here).

\subsection*{Derivation}
$$
\begin{aligned}
c(Z)&=\frac Z{R}=(1-L)\,\frac{1+Z}3+L\,\frac{Z(1+3x)}{2(1+x)},\\
c(Z)-\frac{1+Z}3&=L(Z)\,D(Z),\qquad D(Z):=\frac{Z(1+3x)}{2(1+x)}-\frac{1+Z}3,\qquad \varepsilon_{\rm H1}=L\,|D|.
\end{aligned}
\tag{2.1}
$$
(2.2) *The arcs.* $d_3=0$ on $C_3$ ($|Z|=1$), so $L=0$ there and $c=(1+Z)/3$ on the whole wall, not only at its ends. This is the declared section's construction, not a symmetry consequence (fix pass, #3): on $|Z|=1$ the surface has the antiholomorphic automorphism $u\mapsto Z\bar u$ (legs 1, 3 fixed, $2\leftrightarrow4$), and equivariance of $w_3=\lambda/(u-c)$ under it forces only $c=Z\bar c$, i.e. $c\in e^{i\varphi/2}\mathbb R$ ($Z=e^{i\varphi}$), one real condition, of which the centroid $e^{i\varphi/2}\,2\cos(\varphi/2)/3$ is one point; $R_{\rm naive}$'s centre is off that line (at $Z=e^{2\pi i/3}$ it is not real; value: companion value, not reproduced here), so within the affine interpolation (2.1) the $C_3$ condition forces $L=0$, hence the centroid. The arc exactness therefore holds for every weight vanishing on $C_3$ – the whole $\Lambda_1$ family, every $\lambda$ (it survives verdict item (v)) – but not for an arbitrary admissible section. Off the FD: at $L=0$ the section is the anchor section $R=R_{\rm anchor}$, whose pole at every leg is the centroid of the other three punctures in an affine chart where that leg is at $\infty$ (leg 3: $Z/R_{\rm anchor}=(1+Z)/3$; leg 1: $R_{\rm anchor}=3Z/(1+Z)$, the centroid $(1+1/Z)/3$ in the chart $1/z$). That notion is Möbius-invariant (charts with a given point at $\infty$ differ by affine maps, which preserve centroids), so the anchor section is $S_4\times\mathbb Z_2$-equivariant with centroid poles, and its transport to the six images of $C_3$ – the arcs joining $e^{\pm i\pi/3}$ to $-1,\tfrac12,2$ – has $c=(1+m)/3$. Near $C_3$, $L\simeq3\,(d_3/\lambda_0d_4)^2$ with $d_3$ linear in the distance: $\varepsilon_{\rm H1}$ vanishes quadratically off the arcs.

\subsection*{Commentary}
(2.1) is a transcription of the sister's formula; the check compares it with the package's Möbius-layer route (tuples, relabelling, `mobius_jet`), so it tests the jet machinery and the dictionary, not the formula itself. (2.2) is what makes 081's H1 statement too weak: H1 is exact on curves, not only at points – still never on an open set (081's H1 text stands on that point).

\subsection*{Result}
$\varepsilon_{\rm H1}=L|D|$ on the FD; zero on all six arcs, quadratic off them; largest where $L=1$, i.e. on $\partial\mathcal V_{0,4}$ ($C_4$), where $c$ is the glued $s$-channel centre $Z/R_{\rm naive}$. [C2]

\subsection*{Verification}
`C2-closed-form-FD`: (2.1) vs the package at 300 random FD points, $7.0\times10^{-16}$; break ($L\to1$): (companion value, not reproduced here). `C2-arcs-zero`: 120 random points on the six arcs (20 per arc), $\max\varepsilon_{\rm H1}=4.6\times10^{-16}$; break: off the arcs along the normal, (companion values, not reproduced here; quadratic vanishing near the corners).

## §3 The scale (1.3′) and the equivariance of $c$ (C3)

\subsection*{Derivation / numbers}
081's affine relabellings $u'=a_gu+b_g$ of $\{0,1,m\}$ with $\infty$ fixed: $(g,a_g,b_g)=(m,1,0),\ (1-m,-1,1),\ (1/m,1/m,0),\ ((m-1)/m,-1/m,1),\ (1/(1-m),-1/(1-m),1/(1-m)),\ (m/(m-1),1/(1-m),m/(m-1))$; the centre must obey $c(gm)=a_gc(m)+b_g$ and the scale $|\lambda(gm)|=|a_g||\lambda(m)|$. The package transports by $S_3$ on labels $1,2,3$ with label 4 fixed (and conjugation); the two agree only if the section is $S_4$-symmetric (the Klein relations on the FD). Measured: $\max\big|1/|a_3|-|\lambda_{(1.3')}|\big|/|\lambda|=6.8\times10^{-16}$ (600 random points, all twelve tiles), $1.3\times10^{-15}$ on $\partial\mathcal V_{0,4}$ (24000 points); $\max|c(gm)-a_gc(m)-b_g|=7.8\times10^{-16}$ (100 FD points and their conjugates × 6). At the samples $1/|a_3|-|\lambda|\le9\times10^{-16}$.

\subsection*{Result}
(1.3′) is the sister's transport, wall for wall and tile for tile (081 §5.3's "not yet machine-checked" is closed); $c$ is affine-equivariant in 081's sense. [C3]

\subsection*{Verification}
Breaks: the naive $\beta|m(m-1)|^{1/2}$ off the FD differs from the package's scale (`C3-scale-break`; companion value, not reproduced here); dropping $b_g$ (`C3-equivariance-break`; companion value, not reproduced here).

## §4 Size of the error: samples, boundary, per tile (C4)

\subsection*{Setup}
Grid of step $0.02$ over $[-1.79,2.79]\times[-2.25,2.25]$ (offset to avoid $0,1$ and the real axis), points kept if in $\mathcal V_{0,4}$ by both 081's criterion and the package's (36339 points); tiles named as in 081's table (`*` = conjugate). Boundary: the $C_4$ arc of the FD ($4001$ samples of the ellipse) transported by the twelve tile elements.

\subsection*{Derivation / numbers}
*Exact boundary value* (by hand): at $Z=-\tfrac{16}9$ (real end of the FD, $q=-1$, $x=-\tfrac19$), the section's centre is $c=Z\,\tfrac{1+3x}{2(1+x)}$ and $\varepsilon_{\rm H1}=|c-\tfrac{1+Z}3|$ (values of $c$, $\varepsilon_{\rm H1}$, $\varepsilon_{\rm H1}/|\lambda|$ and $\varepsilon_{\rm H1}/|c_{\rm H1}|$ at this point: companion values, not reproduced here):
$$
\varepsilon_{\rm H1}(-\tfrac{16}9)=\text{(companion value, not reproduced here)}.
\tag{4.1}
$$
The last ratio recovers, in terms of the centre, the mismatch of the anchor section against the $C_4$ datum quoted in 081 H1.

*Samples of 081* (the four sample pairs use three values of $m$):

The values of $c_{\rm sec}$, $\varepsilon_{\rm H1}$ and $\varepsilon_{\rm H1}/|\lambda|$ at $m=e^{i\pi/3},-1.3,-0.62$ come from the companion SL(2,C) package and are not reproduced here; at $m=e^{i\pi/3}$ the section's centre equals the centroid ($\varepsilon_{\rm H1}=0$, $|\lambda|=1.5$).

*Per tile* (grid; absolute maxima are grid values, resolution $0.02$):

The per-tile maxima of $\varepsilon_{\rm H1}$ (on $T_0,T_1$ and the lenses the maximum sits on the tile's boundary arc, with the boundary value (4.1) on $T_0,T_1$; on $T_2,T_3$ it sits in the interior), of $\varepsilon_{\rm H1}/|\lambda|$ and the area-means are grid values from the companion SL(2,C) package, not reproduced here.

The maximum of the relative error, found by a bounded search on the real wall and then a 2D Nelder–Mead, lies just inside $\partial\mathcal V_{0,4}$ on the FD, on $C_1$, slightly above the boundary value (companion value, not reproduced here); by the $S_3\times\mathbb Z_2$ invariance of $\varepsilon_{\rm H1}/|\lambda|$ the same value holds on every tile.

\subsection*{Commentary}
$\varepsilon_{\rm H1}$ and $|\lambda|$ both scale by $|a_g|$ under 081's relabellings (C3), so $\varepsilon_{\rm H1}/|\lambda|$ is a function on $\mathcal V_{0,4}/S_3\times\mathbb Z_2$ – the frame-independent measure (a shift $\delta c$ changes the special coordinate by $w\mapsto w+(\delta c/\lambda)w^2+\dots$). The absolute error per tile follows from it times $|\lambda|$: on $T_2,T_3$ ($|a_g|=1/|m|$ or $1/|1-m|$) the maximum moves inside the tile, which is why the per-tile absolute maximum is on the boundary for $T_0,T_1$ and the lenses only. The relative error is largest exactly where the patch must match its neighbours: at $\partial\mathcal V_{0,4}$, H1's coordinate is not the glued Feynman coordinate (the requirement of 081 (1.5) at the propagator wall is met by $|\lambda|$ but not by H1's centre).

\subsection*{Result}
$\varepsilon_{\rm H1}$ at $-\tfrac{16}9$ (and $\tfrac{25}9$) on $\partial\mathcal V_{0,4}$ takes an exact value (4.1) (companion value, not reproduced here); that it is the global maximum of $\varepsilon_{\rm H1}$ is a grid and boundary-sampling measurement (grid $0.02$, $4001\times12$ boundary samples); $\max\varepsilon_{\rm H1}/|\lambda|$ lies just inside $\partial\mathcal V_{0,4}$ (numerical, Nelder–Mead; value not reproduced here); $0$ on the six arcs (exact, C2.2). Supporting the sampled maximum: along the real wall $\varepsilon_{\rm H1}$ decreases inward (the product of the maximal relative error and $|\lambda|$ at the interior maximum stays below the boundary value; the critic's hand value), since $|\lambda|$ drops over the last $0.042$ by more than the relative error rises (companion values, not reproduced here). [C4]

\subsection*{Verification}
`C4-boundary-channel`: $c_{\rm sec}$ vs the centre of `channel_maps` of the channel with $|q_c|=1$, $2.7\times10^{-15}$ on 24000 boundary points; break (another channel's maps): (companion value, not reproduced here). `C4-boundary-exact-value`: (4.1) to $10^{-12}$. `C4-abs-max-on-boundary` (global form; the per-tile form is false for $T_2,T_3$, found by the first run and recorded in the table), `C4-rel-max-interior`, `C4-relative-tile-invariant` (per-tile maxima within a spread at grid resolution (companion value, not reproduced here); tolerance tightened from 5 % to 0.5 % in fix pass #10 – **written, not yet run**; on run 7's recorded maxima the tightened check passes; the property is exact given C3, so this check is a grid-resolution measurement more than an independent test).

## §5 Across the arc $|m|=1$ (C5)

\subsection*{Setup}
$Z_1=e^{i\varphi}$, $\varphi=\tfrac{2\pi}3$ (generic point of the arc from $e^{i\pi/3}$ to $-1$, $T_0|T_2$); $m=(1+\delta)Z_1$; one-sided least-squares fits $f=c_1\delta+c_2\delta^2+c_3\delta^3+c_4\delta^4$ on $\delta=\pm0.0002\,k$, $k=1..10$ ($f(1)=0$ checked separately).

\subsection*{Derivation}
FD side ($\delta>0$): $d_3=(r^2-1)(|Z-1|^2-1)\simeq2\delta\,(|Z_1-1|^2-1)$, $L\simeq3\,(d_3/\lambda_0d_4)^2$, so
$$
A_+=3\Big(\frac{2(|Z_1-1|^2-1)}{\lambda_0\,d_4(Z_1)}\Big)^2D(Z_1).
\tag{5.1}
$$
$T_2$ side ($\delta<0$): 081's $g=1/m$ ($a_g=1/m$, $b_g=0$) gives $c(m)=m\,c(1/m)$, the centroid likewise, so $f(m)=m\,f(1/m)$; $1/m=\overline{Z'}$ with $Z'=r^{-1}Z_1$ in the FD, and conjugation gives $f(\bar Z)=\overline{f(Z)}$; with $r^{-1}-1=-\delta+O(\delta^2)$:
$$
A_-=e^{i\varphi}\,\overline{A_+}.
\tag{5.2}
$$
Scale: (1.3′) gives $|\lambda|=\beta|m(m-1)|^{1/2}$ on $T_0$, $\beta|m-1|^{1/2}$ on $T_2$, so $\partial_r|\lambda|$ jumps by $\tfrac\beta2|Z_1-1|^{1/2}=0.98706$.

\subsection*{Numbers}
$f(1)=8\times10^{-17}$; fitted $|f'(1^\pm)|=1.1\times10^{-12},1.3\times10^{-11}$ (were $9.9\times10^{-10},8.3\times10^{-9}$ at $5h$: fit error, $\to0$). The fitted $A_+$ agrees with (5.1) to $10^{-5}$ and $A_-$ with (5.2) to $3.8\times10^{-7}$ (values from the companion SL(2,C) computation, not reproduced here), $|A_+|=|A_-|$, $|A_+-A_-|$ (companion value, not reproduced here). Jump of $\partial_r(1/|a_3|)$: $0.98706$.

\subsection*{Commentary}
$c$ is $C^1$ and not $C^2$ across the arc, as PH34 states; the jump of the second derivative is a pure phase, (5.2), forced by the transport ($g=1/m$ composed with conjugation) – so $\varepsilon_{\rm H1}=|f|$ has equal curvature on both sides at leading order: the error is $C^2$ across the arc there even though $c$ is not. The first fit (step $0.004$, cubic, free constant) failed (5.2) at $5\times10^{-2}$; the converged fits above show that was truncation error of the fit, not of the result.

\subsection*{Result}
Across the arc: $\varepsilon_{\rm H1}\simeq|A|\,\delta^2$ on both sides ($|A|$: companion value, not reproduced here), $c$ $C^1$-not-$C^2$ with (5.2), $|\lambda|$ kinked as (1.3′) predicts. [C5]

\subsection*{Verification}
`C5-arc-C1`, `C5-arc-not-C2`, `C5-arc-prediction`, `C5-arc-closed-form`, `C5-arc-scale-kink`; break `C5-arc-break`: the alternatives $A_+$, $\bar A_+$, $-e^{i\varphi}\bar A_+$ miss $A_-$ by (companion values, not reproduced here, relative).

## §6 Consequences for N2–N3; verdict (C6)

\subsection*{Numbers}
*Limit moduli* $\mu=\chi(0,1,m;c)$ of 081 (3.1) (transcription check: 081's hand values $6.2174$, $-2.6387$, $e^{i\pi/3}$ under H1 reproduced):

| $m$ | $\mu$ (H1) | in $\mathcal V_{0,4}$ |
| --- | --- | --- |
| $e^{i\pi/3}$ | $e^{i\pi/3}$ | yes |
| $-1.3$ | $6.2174$ | no |
| $-0.62$ | $-2.6387$ | no |

The values of $\mu$ under the section, and their membership in $\mathcal V_{0,4}$, come from the companion SL(2,C) package and are not reproduced here.

So by 081's criterion (3.1): `sym-sym` → own $\mathcal V_4\mathcal V_4$ (unchanged), `sym-nearZ2` → (d) (unchanged), `nearZ2-nearZ2` → (c) $\mathcal V_3^4$ (unchanged, $\mu$ now near the wall), **`near-boundary` → own $\mathcal V_4\mathcal V_4$ re-entry**, not a (d) chain region. On the 36339 grid points, $\mu(m)\in\mathcal V_{0,4}$ under H1 and under the section: (companion values, not reproduced here) – the two memberships disagree on a fraction of $\mathcal V_{0,4}$ (grid area), hence on a larger fraction of the product base for a pair.

*Six-point moduli* (2.2), relative shift $\max_k|\Delta\chi_k|/\max(|\chi_k|,1)$, $\theta=0$:

[Table of companion-project values removed.]

(The table listed the shift for the pairs `sym-sym` (zero), `nearZ2-nearZ2`, `sym-nearZ2` and `near-boundary` at $\vert q\vert=1,3,12$.)

*Holomorphy* of $c_{\rm sec}$ (central differences, $h=10^{-6}$): $\partial_{\bar m}c\ne0$ at $-1.3$, $-0.62$, $-0.3+1.5i$ and $0.2+1.2i$ (values from the companion package, not reproduced here); centroid control $|\partial_{\bar m}|<10^{-11}$.

\subsection*{Commentary}
The error is not a small perturbation for the covering test: it changes a predicted ray end at one of four samples, shifts the image of the march by order one at $|q|=12$, and is largest at $\partial\mathcal V_{0,4}$, where the patch must glue to the Feynman regions. The section is non-holomorphic (the sister's 034 §1 obstruction: no holomorphic equivariant $R$ meets the $C_4$ datum), so with it the two-patch map is real-analytic on each product tile, not holomorphic; rank must be tested on the real $6\times6$ Jacobian of $(\Re\chi,\Im\chi)$ in $(\Re,\Im)$ of $(m_L,m_R,q)$. 081 C1–C3 hold for any $c(m)$ except the holomorphy statement of 081 (2.4) (with its complex Jacobian) and C3 (i)'s complex determinant, which become the real $6\times6$ Jacobian (fix pass, critic #9; the same holomorphy statement sits at 081 l. 85 and §5.1 item 2); C4's numbers and C4.1 depend on $c(m)$.

\subsection*{Result – the verdict for N2–N3}
H1 is **not adequate**. N2–N3 (and N4, N5) should take $c(m)=-2c_3(m)$ from `section_jets` (provisional: the package v2.0.0 as the sister's declared section) and $|\lambda|$ from (1.3′) (equal to $1/|a_3|$, C3) with 081's phase convention, and: (i) replace 081's complex Jacobian (`jacobian`, `C2.4-jacobian`, `C4-march-rank`) by the real $6\times6$ one, and in N5 look for sign changes of its determinant inside tiles (C6.3); (ii) in the membership root find, evaluate $c(m')$ off $\mathcal V_{0,4}$ with the package's channel maps ($C^0$ join verified here) and with `section_maps(..., strict=False)` never; (iii) at $m=-1,\tfrac12,2$ exactly, use the centroid (exact there, C1); (iv) re-derive C4.1's predictions with the section's $\mu$ (`near-boundary` now → own re-entry); (v) the section is the declared one at $\lambda_0$ – another member of the sister's $\Lambda_1$ family (R49's $\lambda_0/4$, $4\lambda_0$) has another $c(m)$, so the covering test concerns this vertex only. Runtime is not an obstacle: `section_jets` costs $\sim10^{-4}$ s (36k grid points with everything else in 5 s). [C6]

## Self-review (research skill §5)

1. *Objective.* Answered: the error is measured everywhere it was asked (samples, boundary, across an arc, per tile) and the verdict is backed by its consequence for the covering test (the limit-moduli flip), not only by its size; the measurement also closes 081's open item on (1.3′).
2. *Weakest step.* Everything is the package's section (a provisional cited source: the package v2.0.0 as the sister's declared section, the sister's verifier not yet reviewed by its critic; PH34 rests on the same source and is tested, not assumed, by C5). The independent checks are the symmetry-forced zeros (C1), the cross-transport equivariance (C3), the prediction (5.2), the channel-map join and the hand value (4.1); (2.1) is a transcription of the same formula the package uses.
3. *Not checked.* The $C^1$ join at $\partial\mathcal V_{0,4}$ (only $C^0$); the corners $e^{\pm i\pi/3}$ (`sym-sym` sits on one: values exact, derivatives one-sided); the second-order behaviour on the other five arcs and at other points of this one; other $\beta$; the covering test itself.
4. *What a stronger physicist would add.* That H1's centroid is the anchor section ($R_{\rm anchor}$): a different $S_4$-symmetric section, not a consistent vertex – it misses the $C_4$ datum (by an amount in the centre given in (4.1): companion value, not reproduced here), so it does not glue at $\partial\mathcal V_{0,4}$ (fix pass, #5). A covering test run with it tests the wrong object at exactly the seams; this is stated in §4 and §6.

## Corrections to record 081 (extended in fix pass, critic-090 table; applied to 081 as its section "Corrections from record 090 (2026-10-04)")

Line numbers are those of 081 before the edit.

1. **H1: exact on the six arcs, quadratic off them.** H1 (§ Hypotheses, l. 44; claim-tree line, l. 24): "exact only at the symmetry points (and at $n=2$)" → exact at the symmetry points and on the whole of the six arcs (and at $n=2$), vanishing quadratically off them, by the declared section's construction ($R=R_{\rm anchor}$ on $C_3$, forced within the sister's affine interpolation because $R_{\rm naive}$ fails $C_3$; symmetry alone fixes only $c\in e^{i\varphi/2}\mathbb R$ there; C2.2 here); "never on an open set" stands. l. 44's "Falsified … or discharged by" clause → falsified as a usable approximation for N2–N5 by this record; C4's numbers stand as H1-conditional. l. 198 (§5.1 item 1, "exact at the symmetry points, not elsewhere if PH34 holds") likewise. l. 205 (§5.2 inherit line, "until N1 decides (then possibly $c=-2c_3$)") → decided: $c=-2c_3$ from `section_jets`. The (1.3) block (l. 66) carries no "exact only" text: nothing to change there.
2. **C4.1: `near-boundary` → own $\mathcal V_4\mathcal V_4$ re-entry with the section's centre** ($\mu_L\in\mathcal V_{0,4}$; value: companion value, not reproduced here); the prediction under H1 stays as written for H1. l. 209 (§5.2 N3, "start where C4.1 predicts the ends: the chain regions at `sym-nearZ2` and `near-boundary`") → chain regions at `sym-nearZ2` only; `near-boundary` goes to N2's own-channel test. l. 161 and l. 185 are stated under H1 and can stay.
3. **Holomorphy: under H1 only.** §5.1 item 2 (l. 199, "holomorphic on each of the $12\times12$ product tiles"); also l. 85 (§1, after the tile table), l. 133 ((2.4), complex Jacobian), l. 151 (C3 (i): complex determinant → real $6\times6$ Jacobian), l. 211 (N5: $\det J_{\mathbb R}$, sign changes in tile interiors, C6.3 here), l. 40 and l. 44 ("C1–C3 hold for any $c(m)$" → except (2.4) and C3 (i)). With the section's centre the map is real-analytic on each product tile, not holomorphic.
4. **§5.3: (1.3′) is now machine-checked against `section_jets`** (C3 here); also l. 221 (§5.4 item 2, "not yet by machine (N1)").

081's l. 233 and l. 241 are its fix-pass log; left as history.

## Proposed ledger entry

**H1's error and the scale of the $n=3$ patch, against the sister's section** — against a provisional cited source, the package v2.0.0 as the sister's declared section (its verifier not yet reviewed by the sister's critic; not a hypothesis, and not PH34, which C5 tests at one point). On the FD $c-\tfrac{1+m}3=\Lambda_1D$ (2.1) – Verified; the centroid is exact on the six arcs, by the section's construction ($L=0$ on $C_3$, for the whole $\Lambda_1$ family) – Verified; the value $\varepsilon_{\rm H1}(-\tfrac{16}9)$ on $\partial\mathcal V_{0,4}$ (4.1; companion value, not reproduced here) – Verified (exact, by hand and to $10^{-12}$); that it is the global maximum of $\varepsilon_{\rm H1}$, and $\max\varepsilon_{\rm H1}/|\lambda|$ just inside $\partial\mathcal V_{0,4}$ – Numerical (grid $0.02$ plus $4001\times12$ boundary samples; Nelder–Mead); $c$ is $C^1$-not-$C^2$ across the arc $|m|=1$ with $A_-=e^{i\varphi}\bar A_+$ – Verified at $\arg m=\tfrac{2\pi}3$ (one-sided fits against (5.1)–(5.2)); 081's scale (1.3′) equals $1/|a_3|$ on all tiles – Verified; the centroid is inadequate for the covering test (limit-moduli membership changes on a fraction of $\mathcal V_{0,4}$, grid area (companion value, not reproduced here); the `near-boundary` ray end flips) – Numerical. Verification: `codes/verify-h1-error.py` 25/25 PASS (seed 20261004, run 7), break legs for C1–C5. Source: `agent/derivations/090-h1-error.md#C6`.

## Fix pass (critic iteration 1)

Brief `agent/briefs/active-computator-090-fix-20261004T205500.md`; critique `agent/reports/critic-090-20261004T203900.md` (REVISE, mechanical: 0 critical, 1 major, 7 minor, 4 notes). Text-only pass with the critic's text; no number changes, no script executed. One line per finding; "pending" until applied.

- #9 [major] §6 "Nothing in 081 C1–C3 depends on the form of $c(m)$" is false. **Applied** with the critic's text: §6 Commentary now reads "081 C1–C3 hold for any $c(m)$ except the holomorphy statement of 081 (2.4) and C3 (i)'s complex determinant, which become the real $6\times6$ Jacobian"; the extended correction 3 below; consistent with C6.3. Changed: C6 (justification text only; the verdict and C6.3's statement already said this).
- #1 [minor] dependency misnamed: the package being the declared section, not PH34. **Applied**: the claim-tree PH34 line replaced by a "Cited source" line (the package v2.0.0 as the sister's declared section, provisional; PH34 rests on the same source and is tested by C5, not assumed); C2 "Under PH34" → "For the declared section (034 (2.4′), package v2.0.0)"; `Hypotheses in force:` → none, with the cited source named; §6 Result "(provisional with PH34)" and self-review item 2 reworded; proposed ledger entry: `Conditional(PH34)` dropped, the provisional source named. C5's "Consistent with PH34" kept. Changed: C2 (justification: the cited input renamed; statement unchanged), the `Hypotheses in force:` line (reworded; no node's truth changes).
- #2 [minor] §1 Commentary: the $10^{-9}$-offset values are round-off, not quadratic vanishing. **Applied** with the critic's text ("the offset points lie on or tangent to the arcs where $\varepsilon_{\rm H1}\equiv0$; the values are round-off"), plus the critic's distances. Changed: none (C1's statement and evidence unchanged; Commentary text only).
- #3 [minor] C2.2, (2.2): arc exactness from the section's construction, not symmetry. **Applied** with the critic's text in C2.2 and in block (2.2) (the antiholomorphic automorphism $u\mapsto Z\bar u$ forces only $c\in e^{i\varphi/2}\mathbb R$; $R_{\rm naive}$ fails $C_3$, so the interpolation forces $L=0$; exactness for the whole $\Lambda_1$ family, not for an arbitrary admissible section); also in correction 1 to 081 below. Changed: C2.2 (justification; statement unchanged, its scope made explicit).
- #4 [minor] C4, §4 Result, ledger entry: the boundary value exact as a value, maximum by sampling. **Applied**: claim-tree C4 ("exact value, (4.1); that it is the global maximum is a grid and boundary-sampling measurement"; the relative maximum marked numerical), §4 Result rewritten the same way with the critic's inward-decrease argument, C6.3's ratio marked as the largest of four samples; proposed ledger entry: the closed form, the arcs and the value (4.1) Verified, the two maxima and the membership disagreement Numerical. Changed: C4 (statement: "max … exact" → exact value + measured maximum; no number changes), C6.3 (statement: wording of one number only).
- #5 [minor] Self-review item 4: "legitimate vertex" → not a consistent vertex. **Applied** with the critic's text ("a different $S_4$-symmetric section, not a consistent vertex: it does not glue at $\partial\mathcal V_{0,4}$"), with the reason from (4.1). Changed: none (self-review text; §4's argument already stated it correctly).
- #6 [minor] C6.3: sign changes of $\det J_{\mathbb R}$ inside tiles; N5. **Applied**: one passage in C6.3 (under H1 $\det J_{\mathbb R}=|\det J_{\mathbb C}|^2\ge0$, codimension-2 critical set, folds only at product walls; with the section's $c$ sign changes inside tiles, a real hypersurface met by generic rays; N5 looks for them), one clause in §6 Result item (i), and the N5 item of correction 3 to 081. Changed: C6.3 (statement: a consequence added), C6 (verdict item (i) extended; the verdict unchanged).
- #10 [minor] `C4-relative-tile-invariant` tolerance. **Applied in the script text**: `codes/verify-h1-error.py`, threshold `0.05` → `0.005` (0.5 %, the critic's "about 0.5 % (grid resolution)") with a two-line comment; **written, not yet run** (no script executed in this pass). It needs no run to know the outcome on run 7's data: the grid is deterministic (fixed offset `0.0013`, no seed), and run 7's per-tile maxima (`h1-error.json`, read) span a range (companion values, not reproduced here) whose spread is below 0.5 %. The next run of the script confirms it. §4 Verification updated. Changed: none (C4's statement unchanged; the check's tolerance only).
- Notes #7, #8, #11, #12. **Not applied** (not in the brief's list; the critic marks #7 optional and #11 harmless). For a later pass: #7 – (5.1)–(5.2) hold at any non-corner $Z_1$ on $C_3$ and C3's equivariance carries them to the other five arcs, so self-review item 3 undersells; #8 – the disagreement fractions (companion values, not reproduced here) are Euclidean area in the $m$ plane, not a tile-invariant measure (the verdict does not rest on it); #11 – on the FD part of $\partial\mathcal V_{0,4}$ `C4-boundary-channel` meets the same formula ($R=R_{\rm naive}=F_1(\infty)$ of `maps_s_channel`), so self-review item 2's "channel-map join" as an independent check is overstated; #12 – the Nelder–Mead start is hard-coded (`gm` computed, unused), `C2-arcs-break`'s margin is small (companion value, not reproduced here), the $-1$ leg of `C1-dictionary-symmetric` is vacuous (the script says so). The brief scopes the script to #10 only, so #12's script edits are not made.
- Corrections to record 081: the critic's extended table. **Applied** here (section "Corrections to record 081", four numbered corrections with all the critic's locations and #3's reason) and in 081 (its section "Corrections from record 090 (2026-10-04)", each location edited in place).

**Changed nodes and dependents** (claim-tree *Fix pass*, step 2).

| node | statement or justification | change |
| --- | --- | --- |
| PH34 line → Cited source line | – | the dependency renamed: the package v2.0.0 as the sister's declared section (provisional); PH34 tested by C5, not assumed (#1) |
| C2 | justification | "Under PH34" → "for the declared section (034 (2.4′), package v2.0.0)" (#1) |
| C2.2 | justification | the reason for arc exactness: the section's construction, not symmetry; scope: the whole $\Lambda_1$ family (#3) |
| C4 | statement | boundary value (companion value, not reproduced here): exact value, maximum by sampling; relative maximum numerical (#4); no number changes |
| C6.3 | statement | fold consequence added (sign changes of $\det J_{\mathbb R}$ inside tiles, N5) (#6); the ratio worded as the largest of four samples (#4) |
| C6 | statement (item (i) only) | verdict item (i) extended by the N5 sign-change search; §6 Commentary's false sentence corrected (#9); the verdict unchanged |

Dependents: C2 → C4, C6 (hold: no number depends on the renaming). C2.2 → C2 (holds: statement unchanged), C4 (holds). C4 → C6 (holds: the verdict rests on the `near-boundary` flip, the size at the seams and the exact value (4.1), not on the maximum being proven global). C6.3 → C6 (holds, extended). C1, C3, C5, C6.1, C6.2, C6.4 unchanged. The `Hypotheses in force:` line changed (PH34 → none, the provisional source named): by the schema a further critic pass would be a **full re-review**; no number and no verdict changed.

## Status

Fix pass (critic iteration 1) complete (21:04): #9, #1–#6 applied with the critic's text, #10 applied in the script text (**written, not yet run**; passes on run 7's recorded data), notes #7, #8, #11, #12 recorded, not applied (outside the brief's list); the extended corrections applied to 081 (its section "Corrections from record 090 (2026-10-04)"). The quoted 25/25 PASS is run 7, before the tolerance change. Next: the next run of `codes/verify-h1-error.py` confirms #10; N2 with the section's centre and the real Jacobian. Pre-fix state: complete (20:37), C1–C6 established, script 25/25 PASS (run 7).
