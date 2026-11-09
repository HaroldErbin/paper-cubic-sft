# 079 — Convergence of the $(h,m)$ sector expansion of the fixed-halves gluing on the fold arcs

## Status

2026-10-04 (run 1; fix pass after critic iteration 1 done). Complete: C1–C4 established; all critic-079 findings applied (`## Fix pass (critic iteration 1)`). Script `codes/verify-fold-arc-convergence.py`: 14/14 PASS, seed 20261004 (`agent/scratch/computator/computator-079-fix-20261004T105800/run-fix.log`). Next step: none (orchestrator grep of the entry against §3 Result, promotion).

## Task and objective

**Literal task** (brief `computator-079-fold-arc-convergence-20261004T100000`): for the fixed-halves form $p^{\rm circ}$ of record 074 (R80), (i) the growth of the sector coefficients $c_{h,m}$ of the tachyon four-point integrand as $h\to\infty$ on and near the fold arcs; (ii) whether $\sum_{h,m}c_{h,m}\hat f_m(h)$ converges (absolutely / conditionally / not), i.e. whether $\int_{Q_V}$ and $\sum_{h,m}$ commute; (iii) which of 074's sector-by-sector statements (C2.4 closed forms, real zeros of $\hat f_{m\ne0}$, C3 "per sector as numbers") need that exchange.

**Motivating objective.** R80's kernels are derived sector by sector; if the sector expansion fails after the region integral on the fold arcs, the sector formulas are formal there and the real zeros of $\hat f_{m\ne0}$ (and the pole reading under PH31) need another justification. Deliverable: a verdict with its regime (convergent with rate / conditionally convergent with the prescription / divergent with what survives).

## Conventions and assumptions

- **A1** Book conventions (the project conventions, Erbin 2023); $\beta=\beta'=3/2$; $q=e^{-s+i\theta}$, $Q_V=\{1<|q|<e^{\sigma_V(\theta)}\}$, $s\in(-\sigma_V(\theta),0)$, as in 074 A2, A4, (1.4).
- **A2** Fixed-halves model (074 A5): two $\mathcal V_3'$ halves, ordinary punctures at $w=\pm2\beta$ in the special-leg coordinate, glued by $w_1w_2=q$; local coordinates transported from the halves, $q$-independent in each half's own frame. A model assumption, not a hypothesis.
- **A3** External states: four tachyons $c\bar c\,e^{ik_jX}$, arbitrary (off-shell) momenta with $\sum_jk_j=0$, weights $\Delta_j=\alpha'k_j^2/4-1$; copy 1 carries $a,b$ at $w_1=+2\beta,-2\beta$, copy 2 carries $c,d$ at $w_2=+2\beta,-2\beta$. Symmetrisation over each pair ($\mathrm{Sym}^2$) where stated.

Free constants: the overall normalisation $\mathcal N$ of the integrand (Schiffer constant $\kappa$, the copy-1 and copy-2 local-coordinate factors, the vacuum normalisation) is a common multiplicative constant of every sector coefficient and of the region integral; every claim below is a statement about convergence or about ratios, so $\mathcal N$ cancels and none is fitted.

## Method (fixed before computing)

1. Closed form of the integrand of (074 (1.3)) for tachyons in the fixed-halves model, as a function of $y:=q/4\beta^2$; its holomorphic factorisation gives $c_{h,m}$ exactly as products of binomial-series coefficients $g_N$.
2. Growth: Darboux transfer from the singularities of the holomorphic factor at $|y|=1$, compared with exact coefficients to order $N\sim 400$ (mpmath/numpy recursion), fit of $\log|c|$ vs $\log h$.
3. $\sigma_V(\theta)$ by per-ray bisection (copy of 074's geometry functions), profile near the arc endpoints; $\hat f_m(h)$ by quadrature in $\theta$.
4. Integrated sums: partial sums of $\sum c_{h,m}\hat f_m(h)$ in three orders (fixed-$m$ sector sums; level order $h\le H$; square truncation), against the direct 2D integral of the closed-form integrand over $Q_V$, at several momenta (on both sides of the predicted threshold), and on the ray/window $\theta$ near $\pi$ (strictly inside) vs the fold arcs.

## Claim tree

- **A1–A3** as above.
- **C1** The tachyon integrand of the fixed-halves gluing is $I=\mathcal N|y|^{h_0}|1-y|^{2a_-}|1+y|^{2a_+}$ ($y=q/4\beta^2$), its sector coefficients are $c_{h,m}(4\beta^2)^h=\mathcal Ng_Ng_{\bar N}$ with $g_N$ the Taylor coefficients of $(1-y)^{a_-}(1+y)^{a_+}$, and their growth is $h^{-2\alpha-2}$ at fixed $m$, $h^{-\alpha-1}$ (oscillating) at fixed $\theta$ on the fold arcs, $h^{-(a_-+a_+)-1}$ at $\theta=\pi/2$, with $\alpha=\min(a_-,a_+)$ the cross-channel ($t$/$u$) collision exponent. [by C1.1–C1.3]
  - **C1.1** Closed form (1.4) of the integrand. [by A2, A3; cited: 071 C4.1, 074 (1.1)–(1.3); eq. (1.1)–(1.4)] [check: C1.1-onshell, C1.1-ghost]
  - **C1.2** The only singularities of $f$ on $|y|\le1$ are $y=\pm1$ (cross-channel collisions at $\theta=0,\pi$, outside $\bar Q_V$), and (1.6) holds exactly. [by C1.1; eq. (1.5)–(1.6)] [check: C1.2-coeffs]
  - **C1.3** Darboux asymptotics (1.7)–(1.8), fixed $m$ and fixed $\theta$, including the coalescence at $\pi/2$. [by C1.2; eq. (1.7)–(1.8)] [check: C1.3-darboux-m, C1.3-darboux-theta]
- **C2** On the fold arcs the region-integrated sector sum $\sum_{h,m}c_{h,m}\hat f_m(h)$ converges absolutely (and $\int_{Q_V}$, $\sum_{h,m}$ commute in every order) iff $\alpha>-1$; for $\alpha\le-1$ every fixed-$m$ sector sum diverges, while the level-ordered sum converges to $J$ for $\alpha>-3$, $h_0<3$ (absolutely for $\alpha>-2$, $h_0<2$), and $J$ is the Abel sum of the level series for all momenta. [by C2.1–C2.5]
  - **C2.1** Exact cancellation of $(4\beta^2)^{\pm h}$ in each term (2.1), $|\hat F_m(h)|\le8/|m|$ uniformly in $h$, and the $\sqrt3(\theta_1-\theta)^{1/2}$ profile at the arc ends. [by C1, A1; eq. (2.1)–(2.2)] [check: C2.1-profile, C3.1-table]
  - **C2.2** Absolute convergence iff $\alpha>-1$; fixed-$m$ sector sums of fixed sign diverging like $H^{-2\alpha-2}$ otherwise ($\log H$ at $\alpha=-1$). [by C1.3, C2.1; eq. (2.3)] [check: C2.2-absolute, C2.2-sector-divergence]
  - **C2.3** Level order: (2.4) and its convergence thresholds $-2$ (absolute), $-3$ (conditional) for $\alpha$ and for $a_-+a_+=-h_0$. [by C1.3, C2.1; eq. (2.4)] [check: C2.3-level-order, C2.3-h0-threshold]
  - **C2.4** The level series in its natural order converges to $J$ whenever it converges (Abel); for $\alpha>-1$ every ordering does (absolute convergence); $J$ is the Abel sum of the level series for every momentum. [by C1.1, C1.2; eq. (2.4), Abel's theorem] [by check: C2.4-abel]
  - **C2.5** Ray $\theta=\pi$: geometric, ratio $\tfrac14$; fold-arc ray: $n^{-\alpha-2}$ terms. [by C1.3, C2.1; eq. (2.5)] [check: C2.5-rays]
- **C3** R80's statements about $\hat f_m(h)$ and single eigenspaces (C2.4 closed forms and real zeros of $\hat f_{m\ne0}$, C2.2, C2.3, C2.5, the per-sector identity of C3) do not need the exchange and are unaffected; the evaluation of $p^{\rm circ}$ (and of $\mathcal V_4p^{-1}\mathcal V_4$) on given inputs as a sum of sector contributions needs it, and has it in the sense of C2 (any order for $\alpha>-1$; level order or Abel beyond); 074 (1.5)'s wording is corrected. [by C3.1–C3.3]
  - **C3.1** The transform statements involve no sum over sectors. [by C2.1; eq. (3.1)] [check: C3.1-table]
  - **C3.2** Per sector, the composite $\mathcal V_4p^{-1}\mathcal V_4$ has the same sector series as $p^{\rm circ}$ term by term, so the form-level identity holds in the summation sense of C2. [by C2, A2; cited: 074 C3, (3.1); eq. (3.3)]
  - **C3.3** The pole reading under PH31 needs the level-order or Abel remainder; for the four-point form that remainder is entire in the exponents; for the five-point composite it is not computed. [by C2.3, C2.4; eq. (3.4)]
- **C4** The regime of C2 in terms of momenta: on shell, every-order convergence iff both cross channels are below the tachyon pole ($\alpha't,\alpha'u<-4$), level-order convergence iff below the massless pole and $\alpha's>-10$; off shell every regime occurs at every channel momentum; on the ray $\theta=\pi$ and off the arcs the convergence is geometric for every momentum; excited inputs lower the threshold exponent (argued). [by C4.1–C4.4]
  - **C4.1** On-shell exponents and $a_-+a_+=-h_0$ (on and off shell). [by A3; eq. (4.1)] [by check: C4.1-onshell-map]
  - **C4.2** Independence of $h_0$ and $a_-$ off shell; every regime at every $P$. [by C4.1, C2]
  - **C4.3** Excited inputs: threshold (4.3). [eq. (4.3), argued from the OPE leading term; not machine-checked]
  - **C4.4** $\theta=\pi$ and off-arc rays: geometric convergence. [by C2.1, C2.5] [check: C2.5-rays, C2.1-profile]

Open gaps: none
Hypotheses in force: none (model assumption A2 = 074 A5, not a hypothesis; C4.3 argued, scope only)

## §1 Integrand and growth (C1)

\subsection*{Setup}
Uses A1–A3. In copy 1's special-leg coordinate $w:=w_1$ the four punctures are $w_a=2\beta$, $w_b=-2\beta$, $w_c=q/2\beta$, $w_d=-q/2\beta$ (copy 2's $w_2=\pm2\beta$ through $w_1=q/w_2$). $y:=q/4\beta^2$, so $|y|=1$ is the fold circle $|q|=4\beta^2$, on which all four punctures lie on $|w|=2\beta$. $\kappa_{ij}:=\alpha'k_i\!\cdot\!k_j$.

\subsection*{Derivation}
*(1.1) Factors.* By 074 (1.1)–(1.3) the integrand per $ds\,d\theta$ is $\langle\Phi_2^{(ab)}|\,(-i\kappa)b_0^+b_0^-\,\mathcal S(q)\,|\Phi_2^{(cd)}\rangle$, and $\mathcal S(q)|\Phi_2^{(cd)}\rangle$ is copy 2's two-puncture state with punctures at $\pm q/2\beta$ and local coordinates $w_1=q/f^{(2)}_{c,d}(\xi)$, i.e. rescaled by $q$. Matter (071 C4.1, the book's `cft:eq:scalar-ope-V-V`):
$$
\prod_{i<j}|w_{ij}|^{\kappa_{ij}}\prod_i|f_i'(0)|^{\alpha'k_i^2/2},\qquad |f'_{c,d}(0)|\propto|q| .
\tag{1.1}
$$
Ghosts: $c\bar c$ of weight $(-1,-1)$ contributes $\prod_i|f_i'(0)|^{-2}$, and, holomorphically, with $b_0=\oint\frac{dw}{2\pi i}wb(w)$ on a circle separating the two pairs and $\langle b(w)\prod_{i=1}^4c(z_i)\rangle=\prod_{i<j}z_{ij}/\prod_i(w-z_i)$,
$$
\langle c(a)c(-a)\,b_0\,c(x)c(-x)\rangle\propto x\,(a^2-x^2),\qquad a=2\beta,\ x=\frac{q}{2\beta},
\tag{1.2}
$$
so the ghost factor is $\propto|q|^2|1-y^2|^2$ ($b_0^+b_0^-=-2b_0\bar b_0$ up to order).

*(1.2) Collecting powers of $|q|$.* $|q|^{\alpha'(k_c^2+k_d^2)/2-4}$ (Jacobians of copy 2) $\times|q|^{\kappa_{cd}}$ ($|w_c-w_d|=|q|/\beta$) $\times|q|^2$ (ghosts) $=|q|^{\alpha'(k_c+k_d)^2/2-2}$. The cross distances are $|w_a-w_c|=|w_b-w_d|=2\beta|1-y|$, $|w_a-w_d|=|w_b-w_c|=2\beta|1+y|$.

*(1.3) Result.* With $P:=k_c+k_d$ the momentum through the circle,
$$
I(q)=\mathcal N\,|y|^{h_0}\,|1-y|^{2a_-}\,|1+y|^{2a_+},\qquad
h_0=\tfrac{\alpha'}2P^2-2,\quad a_-=1+\tfrac12(\kappa_{ac}+\kappa_{bd}),\quad a_+=1+\tfrac12(\kappa_{ad}+\kappa_{bc}).
\tag{1.4}
$$
$h_0$ is the $L_0^+$ of the circle state's ground level, as in 074 (2.8) ($h=\tfrac{\alpha'}2P^2+N+\bar N-2$). Momentum conservation ties the three exponents, on and off shell: $a_-+a_++h_0=\tfrac{\alpha'}2(k_a+k_b+k_c+k_d)\cdot(k_c+k_d)=0$, i.e. $a_-+a_+=-h_0$ (`C4.1-onshell-map`); the integrand has two free exponents, $h_0$ (channel) and $a_-$ (cross channel). On shell ($\alpha'k_j^2=4$, $s:=-P^2$, $t:=-(k_a+k_c)^2$, $u:=-(k_a+k_d)^2$, $\alpha'(s+t+u)=-16$): $a_-=-3-\tfrac{\alpha'}2t$, $a_+=-3-\tfrac{\alpha'}2u$, $h_0=-\tfrac{\alpha'}2s-2$, and (1.4) is $Z^*$ of the Virasoro–Shapiro form ($Z'=(y^2-1)/4y^2$, $1-Z=-(1-y)^2/4y$; `C1.1-onshell` checks this against an independent Möbius frame).

*(1.5) Singularities.* $f(y):=(1-y)^{a_-}(1+y)^{a_+}=\sum_{N\ge0}g_Ny^N$ is holomorphic on $|y|<1$ with branch points at $y=\pm1$ only: the collisions $w_c\to w_a$, $w_d\to w_b$ ($y=1$) and $w_d\to w_a$, $w_c\to w_b$ ($y=-1$) of a copy-1 with a copy-2 puncture — the $t$- and $u$-channel OPEs, exponent $|1\mp y|^{2a_\mp}$ (on shell $|1-Z|^{\kappa_{ac}}$ pulled back by the 2:1 fold, $1-Z\propto(1-y)^2$). These sit on the fold circle at $\theta=0,\pi$, which are **not** on the fold arcs: the arcs $\theta\in\pm(\theta_1,\theta_2)$, $\cos\theta_1=\tfrac7{25}$ ($73.74^\circ$–$106.26^\circ$) keep $|1\pm y|\ge2\cos(\theta_2/2)=\tfrac65$. On the arcs nothing collides; the radius $|y|=1$ is set by the circle passing through all four punctures, the coefficient growth by the nearest collisions, at $\theta=0,\pi$, outside $\bar Q_V$ (there $|y|\le\tfrac14$).

*(1.6) Sector coefficients.* Since $|f(y)|^2=f(y)\overline{f(y)}$ and $g_N\in\mathbb R$ for real momenta,
$$
I=\mathcal N\sum_{N,\bar N\ge0}g_Ng_{\bar N}\,|y|^{h_0+N+\bar N}e^{i(N-\bar N)\theta}
\quad\Longrightarrow\quad
c_{h,m}\,(4\beta^2)^{h}=\mathcal N\,g_Ng_{\bar N},\quad h=h_0+N+\bar N,\ m=N-\bar N,
\tag{1.6}
$$
exactly (the $(4\beta^2)^h$ from $|y|^h=(4\beta^2)^{-h}e^{-sh}$). Recurrence: $(N+1)g_{N+1}=(a_+-a_-)g_N+(N-1-a_+-a_-)g_{N-1}$. Odd $m$ appear for the unsymmetrised integrand and are killed by $\hat f_{\rm odd}=0$ (074 C2.4); symmetrising each pair ($a_-\leftrightarrow a_+$, i.e. $y\to-y$) removes them from $c_{h,m}$ as well, as 071 C3 requires.

*(1.7) Darboux transfer.* Near $y=1$, $f\simeq2^{a_+}(1-y)^{a_-}$; near $y=-1$, $f\simeq2^{a_-}(1+y)^{a_+}$. Hence ($[y^N](1-y)^a=\Gamma(N-a)/\Gamma(-a)\Gamma(N+1)$)
$$
g_N=\frac{2^{a_+}}{\Gamma(-a_-)}N^{-a_--1}\big(1+O(N^{-1})\big)+(-1)^N\frac{2^{a_-}}{\Gamma(-a_+)}N^{-a_+-1}\big(1+O(N^{-1})\big),
\tag{1.7}
$$
a term being absent when its exponent is a non-negative integer. With $\alpha:=\min(a_-,a_+)$ (real momenta; $\Re$ otherwise):

(i) *fixed $m$, $h\to\infty$*: $c_{h,m}(4\beta^2)^h\sim\mathcal N\,C\,h^{-2\alpha-2}$, non-oscillating (the $y=1$ term squared; the cross term $\propto(-1)^Nh^{-a_--a_+-2}$ is subleading unless $a_-=a_+$);

(ii) *fixed $\theta$, level-$n$ term* $T_n(\theta):=\sum_{N+\bar N=n}g_Ng_{\bar N}e^{i(N-\bar N)\theta}$ $=[r^n]\,f(re^{i\theta})f(re^{-i\theta})$, singular in $r$ at $r=e^{\mp i\theta},\,-e^{\mp i\theta}$, each a singularity of one factor only for $\theta\notin\tfrac\pi2\mathbb Z$:
$$
T_n(\theta)\simeq2\,\mathrm{Re}\Big[\frac{2^{a_+}f(e^{-2i\theta})}{\Gamma(-a_-)}n^{-a_--1}e^{in\theta}+\frac{2^{a_-}f(-e^{-2i\theta})}{\Gamma(-a_+)}n^{-a_+-1}(-1)^ne^{in\theta}\Big],
\tag{1.8}
$$
an oscillating sum of amplitude $n^{-\alpha-1}$ on and near the fold arcs;

(iii) *at the arc midpoint $\theta=\pi/2$* the singularities $r=-i$ of $f(re^{i\theta})$ at $y=1$ and of $f(re^{-i\theta})$ at $\bar y=-1$ coalesce ($f(ir)f(-ir)=(1+r^2)^{a_-+a_+}$), and $T_n(\tfrac\pi2)\sim n^{-(a_-+a_+)-1}\cos\tfrac{n\pi}2=n^{h_0-1}\cos\tfrac{n\pi}2$ (on the ray $\theta=\pi/2$, $I=\mathcal N\,(|y|/(1+|y|^2))^{h_0}$, invariant under $|y|\to1/|y|$); (1.8) is non-uniform in a window $|\theta-\tfrac\pi2|\lesssim1/n$, its prefactor $f(e^{-2i\theta})\propto|\cos\theta|^{a_+}$;

(iv) at $\theta=0,\pi$ (not in $\bar Q_V$ near $|y|=1$): $T_n\sim n^{-2a_\mp-1}$.

\subsection*{Commentary}
(1.2): $b_0$ acts on $c(x)c(-x)|0\rangle$ as $x(c(-x)+c(x))$; the residue route of `C1.1-ghost` is the check. (1.4): the off-shell form differs from the on-shell one only through $h_0$ and $a_\pm$, because in the fixed-halves model the local coordinates of copy 2 enter only through the overall $|q|^{2(\Delta_c+\Delta_d)}$ (A2); this is the circle-state statement $\mathcal S(q)=q^{L_0}\bar q^{\bar L_0}$. (1.5): the brief's premise "the circle passes through a puncture" is right for the radius and wrong for the exponent: on the fold arcs the four punctures lie on the circle without colliding, and the momentum-dependent exponent of the growth is that of the cross-channel collisions at $\theta=0,\pi$ (the OPE exponent $\kappa_{ac}$ of 071 C4.1, of a copy-1 with a copy-2 puncture), not of anything happening on the arcs. (1.7)(ii)–(iii): "the growth at fixed $\theta$" is the level-$n$ term in a fixed direction; it is the $m$-sum of the fixed-$m$ coefficients and is smaller than them ($n^{-\alpha-1}$ against $n^{-2\alpha-2}\cdot n$ terms) through the phase cancellation of $e^{im\theta}$.

\subsection*{Result}
$$
\boxed{\ c_{h,m}(4\beta^2)^h=\mathcal N g_Ng_{\bar N}\sim h^{-2\alpha-2}\ (\text{fixed }m),\qquad
T_h(\theta)\sim h^{-\alpha-1}e^{\pm ih\theta}\ (\text{fixed }\theta\text{ on the arcs}),\qquad T_h(\tfrac\pi2)\sim h^{-(a_-+a_+)-1},\qquad \alpha=\min(a_-,a_+)\ }
$$
with $a_\mp=1+\tfrac12(\kappa_{ac}+\kappa_{bd})$, $1+\tfrac12(\kappa_{ad}+\kappa_{bc})$, $a_-+a_+=-h_0$ (so the arc-midpoint exponent is $h_0-1$, set by the channel momentum); on shell $a_-=-3-\tfrac{\alpha'}2t$, $a_+=-3-\tfrac{\alpha'}2u$. The exponent changes sign with the cross-channel momenta: $c_{h,m}(4\beta^2)^h$ grows for $\alpha<-1$ (on shell: $\alpha't>-4$ or $\alpha'u>-4$, i.e. above the cross-channel tachyon pole) and decays for $\alpha>-1$.

\subsection*{Verification}
`C1.1-onshell` (independent Möbius frame $w_a\to\infty,w_b\to0,w_c\to1$ with the on-shell Koba–Nielsen factor and $|d\zeta_d/dq|^2|q|^2$; ratio constant to $3\times10^{-10}$ over 8 seeded $q$; break: dropping $|1-y^2|^2$ gives spread $0.57$). `C1.1-ghost` (residues of $\langle bcccc\rangle$). `C1.2-coeffs` (recurrence in 40-digit mpmath vs float64 Cauchy product of the two binomial series, $7\times10^{-15}$). `C1.3-darboux-m`: at three momenta (A: $a_\mp=(-0.35,0.8)$, $h_0=-0.45$; B: $(-1.4,-0.6)$, $h_0=2$; on shell $\alpha't=-5.2$, $\alpha'u=-6.4$: $(-0.4,0.2)$) and $m=0,2,4$, the exact $g_Ng_{N-m}$ against (1.7) with relative error $\sim10^{-3}\to10^{-4}$ from $N=200$ to $1600$, and log-log slope on $N\in[800,1600]$: A $-1.300$ (pred. $-1.30$), B $+0.797$ ($+0.80$), on shell $-1.196$ ($-1.20$); break: the slope $-\alpha-1$ is rejected at every point. `C1.3-darboux-theta`: RMS envelope slopes of $T_n$ on $n\in[400,1500]$ at $\theta=80^\circ,100^\circ$: A $-0.647$ ($-0.65$), B $+0.393$ ($+0.40$), on shell $-0.606$ ($-0.60$); at $\theta=90^\circ$: A $-1.467$ ($-(a_-+a_+)-1=-1.45$), B $+0.995$ ($+1.00$), on shell $-0.806$ ($-0.80$); break: at $90^\circ$ the generic exponent $-\alpha-1$ is rejected where $|a_--a_+|>0.3$. Script run: 5/5 PASS at this stage.

## §2 Integrated sums (C2)

\subsection*{Setup}
Uses A1–A3, (1.4)–(1.8). $\rho(\theta):=\ln4\beta^2-\sigma_V(\theta)\ge0$, zero exactly on the fold arcs. $J:=\int_{Q_V}I\,ds\,d\theta$, the region integral (074 (1.3) for these inputs). $\hat F_m(h):=\int_0^{2\pi}e^{im\theta}e^{-\rho(\theta)h}d\theta$. Three summation orders of the double series over $(N,\bar N)$: *unordered* (absolute), *sector order* (fixed $m$, sum over $h$, then over $m$ — the reading "each sector is a number" of 074 §2–§3), *level order* (partial sums $h\le H$ with all $m$ at each level — the level-truncation order).

\subsection*{Derivation}
*(2.1) The term.* From (1.6) and 074 (2.8), $\hat f_m(h)=\frac1h\int_0^{2\pi}e^{im\theta}\big(e^{\sigma_V h}-\delta_{m,0}\big)d\theta$, so
$$
c_{h,m}\hat f_m(h)=\mathcal N\,g_Ng_{\bar N}\,\frac{\hat F_m(h)-2\pi\delta_{m,0}(4\beta^2)^{-h}}{h}:
\tag{2.1}
$$
the $(4\beta^2)^{\pm h}$ cancel exactly; on the fold arcs ($\rho=0$) nothing is left to damp $g_Ng_{\bar N}$ but $1/h$ and the $\theta$-integration.

*(2.2) The region near the arcs.* $\sigma_V$ is monotone on $[0,\theta_1]$ (and by evenness and $\pi$-periodicity piecewise monotone, four pieces per period, flat on the arcs), and at the arc endpoints $\rho(\theta)\simeq\sqrt3\,(\theta_1-\theta)^{1/2}$ (numerical: $\rho/\sqrt{\theta_1-\theta}=1.7286,1.7317,1.7320,1.7320$ at $10^{-2},\dots,10^{-5}$; the exit is through $|q_t|=1$). Two consequences. (a) Integrating by parts in $\theta$, $|\hat F_m(h)|\le\mathrm{TV}(e^{-\rho h})/|m|\le8/|m|$ for every $h>0$, $m\ne0$: the $\theta$-integration over the arcs' finite width supplies a factor $1/|m|$, uniformly in $h$. (b) $\hat F_m(h)\to A_m:=\int_{\rm arcs}e^{im\theta}d\theta=-4\sin(m\theta_1)/m$ (even $m\ne0$) with corrections $O(h^{-2})$ from the boundary layer of width $\sim1/3h^2$; rays just off the arcs converge geometrically with ratio $e^{-\rho(\theta)}$, the crossover at $h\sim1/\sqrt{3(\theta_1-\theta)}$.

*(2.3) Unordered / sector order.* With $|g_N|\sim N^{-\alpha-1}$ (1.7) and (2.2a), $\sum_{N,\bar N}|g_Ng_{\bar N}|\,|\hat F_{N-\bar N}|/h$ is bounded by $\sum N^{-\alpha-1}\bar N^{-\alpha-1}\big/\big((N+\bar N)(1+|N-\bar N|)\big)$: the strip $\bar N\le N/2$ gives $\sum_NN^{-\alpha-3}\sum_{\bar N\le N/2}\bar N^{-\alpha-1}$, the diagonal band $\sum_NN^{-2\alpha-3}\log N$; both converge iff $\alpha>-1$. Conversely, at fixed even $m$ with $A_m\ne0$, the terms are $\sim A_m\,C\,N^{-2\alpha-3}$, **of fixed sign** (the $y=1$ singularity squared, (1.7)(i)), so the sector sum
$$
\mathcal F_m:=\sum_hc_{h,m}\hat f_m(h)\ \text{converges iff }\alpha>-1,\ \text{and diverges like }H^{-2\alpha-2}\text{ for }\alpha<-1\ (\log H\text{ at }\alpha=-1).
\tag{2.3}
$$
Mechanism: $\mathcal F_m=\int_{Q_V}e^{im\theta}I_m(s)\,ds\,d\theta$ with $I_m$ the $m$-th Fourier mode of the integrand on the circle $|y|=e^{-s}/4\beta^2$; the Fourier mode delocalises in $\theta$ and sees the collision at $\theta=0$ on the fold circle, $I_m\sim(1-|y|)^{2\alpha+1}$ as $|y|\to1$, while the region reaches $|y|=1$ on the arcs (weight $A_m$). So for $\alpha>-1$ the double series is absolutely convergent and $\int_{Q_V}$, $\sum_{h,m}$ commute in every order (Fubini–Tonelli); for $\alpha\le-1$ no sector sum exists, although $J$ is finite for every momentum ($I$ is smooth on the compact $\bar Q_V$, which avoids $y=\pm1$).

*(2.4) Level order.* $L_n:=\sum_{N+\bar N=n}c\hat f=\frac{\mathcal N}{h}\int_0^{2\pi}T_n(\theta)\big(e^{-\rho h}-(4\beta^2)^{-h}\big)d\theta$. Insert (1.8): on the arcs $T_n$ oscillates as $e^{\pm in\theta}$ with a smooth amplitude, so the $\theta$-integral is an endpoint term $\propto n^{-\alpha-1}\cdot n^{-1}e^{\pm in\theta_{1,2}}$ (the layer (2.2b) is much narrower than the period $2\pi/n$), plus the arc-midpoint term, where the amplitude $\propto|\cos\theta|^{a_+}$ is singular and the coalescence (1.7)(iii) gives $n^{-(a_-+a_+)-2}\cos\frac{n\pi}2$; off the arcs everything is $O(e^{-\rho n})$ except the layer. Hence
$$
L_n\simeq n^{-\alpha-3}\sum_jb_je^{in\omega_j}+n^{-(a_-+a_+)-3}\,b_0\cos\tfrac{n\pi}2,\qquad \omega_j\in\{\pm\theta_1,\pm\theta_2\}+\{0,\pi\},
\tag{2.4}
$$
none of the phases trivial on the even $n$ that survive. So the level-ordered series converges absolutely iff $\alpha>-2$ and $a_-+a_+>-2$ (i.e. $h_0<2$), conditionally (Dirichlet, non-resonant phases) iff $\alpha>-3$ and $a_-+a_+>-3$ ($h_0<3$), with error $O(H^{\max(-\alpha-3,\,-(a_-+a_+)-3)})$, and diverges otherwise. Whenever it converges, it converges to $J$: $\sum_nL_nr^n=r^{-h_0}\int_{Q_V}I(ry)\,ds\,d\theta$ exactly for $r<1$, and $I(ry)\to I(y)$ boundedly on $\bar Q_V$, so the Abel limit is $J$ and Abel's theorem identifies the level series in its natural order, whenever it converges, with it (other orderings, e.g. the square truncation in the conditional regime, only under absolute convergence, $\alpha>-1$). For every momentum, $J$ is the Abel sum of the level series.

*(2.5) Single rays.* At fixed $\theta$ the radial integral of the level series is $\sum_nT_n(\theta)\big(e^{-\rho h}-(4\beta^2)^{-h}\big)/h$. At $\theta=\pi$ ($\rho=\ln4$) it converges geometrically, ratio $\tfrac14$, for every momentum. On a fold-arc ray the terms are $n^{-\alpha-2}e^{\pm in\theta}$: absolutely convergent iff $\alpha>-1$, conditionally iff $\alpha>-2$ (at $\theta=\pi/2$: $a_-+a_+$ in place of $2\alpha$, i.e. thresholds $-1$, $-2$ for $a_-+a_+$). The $\theta$-integration gains one power of $n$ in level order ((2.4) against this), and one power of $|m|$ in sector order ((2.2a)).

\subsection*{Commentary}
(2.3): the threshold $\alpha>-1$ is the local 2D integrability of $|1-y|^{2\alpha}$ at the cross-channel collision points $y=\pm1$ — the same condition under which the full-disc $s$-channel representation 074 (2.9)(iii) ($\hat f=(4\beta^2)^h/h$, $m=0$ only) converges sector by sector. The fold arcs do not make the sector expansion worse than the full disc; it is the collision at $\theta=0,\pi$, which $Q_V$ avoids but the Fourier modes do not, that sets it. (2.4): level order is better than sector order because the level-$n$ term in a fixed direction already carries the phase cancellation of all $m$ (1.7)(ii); this is the order in which a level-truncated evaluation of $p^{\rm circ}$ proceeds. (2.5): 074 (1.5)'s "the $1/h$ of the $s$-integral as the only damping" is the single-ray statement and undercounts: the integrated form has an additional $1/|m|$ (sector order) or $1/n$ (level order) from the finite angular width of the arcs.

\subsection*{Result}
$$
\boxed{\ \sum_{h,m}c_{h,m}\hat f_m(h)\ \begin{cases}
\text{absolutely convergent}\ (=J,\ \text{any order; sector tails }O(H^{-2\alpha-2}),\ \text{level error }O(H^{-\alpha-3})) & \alpha>-1\\
\text{sector sums divergent }(\sim H^{-2\alpha-2});\ \text{level order abs. convergent to }J & -2<\alpha\le-1,\ h_0<2\\
\text{level order conditionally convergent to }J & -3<\alpha\le-2\ \text{or}\ 2\le h_0<3\ (\text{and }\alpha>-3,\ h_0<3)\\
\text{divergent in every order; }J=\text{Abel sum} & \alpha\le-3\ \text{or}\ h_0\ge3
\end{cases}\ }
$$
($h_0=-(a_-+a_+)$; for $\alpha>-1$ automatically $h_0<2$; the worse of the two thresholds decides). The arc-midpoint threshold is set by the channel momentum through the circle, the endpoint one by the cross-channel exponent. Convergence is polynomial, never exponential, on the fold arcs; exponential (ratio $\tfrac14$) on the ray $\theta=\pi$ and geometric (ratio $e^{-\rho(\theta)}$) on every ray off the arcs.

\subsection*{Verification}
Script, $\beta=3/2$, six momenta satisfying $h_0=-(a_-+a_+)$ (asserted in the script): A $a_\mp=(-0.35,0.8)$, $h_0=-0.45$; on shell $(-0.4,0.2)$, $h_0=0.2$ [$\alpha't=-5.2$, $\alpha'u=-6.4$, $\alpha's=-4.4$]; B $(-1.4,-0.3)$, $1.7$; C $(-2.4,0.5)$, $1.9$; E $(-1.2,-1.2)$, $2.4$; D $(-3.5,1.0)$, $2.5$; F $(-1.75,-1.75)$, $3.5$ (fix pass); $H\le1600$; domain $h_0+n\ne0$ for even $n$ (guarded in the script); $J$ by Gauss–Legendre on $Q_V$ with $\sigma_V$ by per-ray bisection (60 steps).

| point | regime | $J$ | $S(400)$ | $S(800)$ | $S(1600)$ | sector $m=4$ at $H=400,800,1600$ |
|---|---|---|---|---|---|---|
| A | $\alpha>-1$ | 17.1479252597 | 17.1479254303 | 17.1479252817 | 17.1479252599 | 0.31417, 0.31437, 0.31445 |
| on shell | $\alpha>-1$ | 6.1497650597 | 6.1497652060 | 6.1497650902 | 6.1497650631 | 0.16901, 0.16921, 0.16929 |
| B | level abs. | 0.8536908844 | 0.8541404680 | 0.8538783599 | 0.8537645142 | 64.0, 112.8, 197.7 |
| C | level cond. (endpoints) | 0.8312204466 | 0.8488223320 | 0.8395027429 | 0.8297830812 | 1.19e6, 8.19e6, 5.67e7 |
| E | level cond. (midpoint) | 0.3699955450 | 0.3992019054 | 0.3893353559 | 0.3827766962 | 7.07, 9.77, 13.34 |
| F | divergent ($h_0\ge3$) | 0.1204213799 | 4.7944849890 | 6.7133981442 | 9.4317569647 | 364.1, 1021, 2876 |
| D | divergent | 0.5709912574 | 1.0254406766 | −0.4815201159 | −4.5395292802 | 2.19e10, 6.87e11, 2.18e13 |

Checks: `C2.1-profile` ($\sigma_V$ monotone on $[0,\theta_1]$, $\rho\simeq\sqrt3(\theta_1-\theta)^{1/2}$, $\sigma_V(0)=\ln\tfrac94$); `C3.1-table` ($\hat F_m(h)$ by graded Gauss–Legendre against a uniform $2^{16}$-point grid, and the real zero of $\hat f_4$ at $-2.356$, 074's $-2.36$: the geometry is 074's); `C2.2-absolute` (A, on shell: $|S(1600)-J|/J=1\times10^{-11}$, $6\times10^{-10}$; sector $m=4$ increment slope $-1.298$, $-1.195$ against $-2\alpha-2=-1.30,-1.20$; absolute-series increment slope $-1.17$, $-1.07$, the diagonal $\log$ of (2.3) making it shallower); `C2.2-sector-divergence` (B, C, E, D at $m=0,2,4$: $|\mathcal F_m(H)|$ slopes $0.79$–$0.81$, $2.79$, $0.41$–$0.46$, $4.98$ against $-2\alpha-2=0.8,2.8,0.4,5.0$; break leg: the same partial sums are stationary to $10^{-2}$ for A and on shell); `C2.3-level-order` (error-envelope slopes, tolerance $0.1$ where one term of (2.4) dominates, the subdominant exponent rejected: C $-0.638$ ($-0.60$ endpoint; midpoint $-1.10$ rejected), E $-0.637$ ($-0.60$ midpoint; endpoint $-1.80$ rejected), D $+0.471$ ($+0.50$, divergent: the break leg of the convergence criterion; $-0.50$ rejected); B $-1.430$ tests convergence only, its two terms $-1.30$, $-1.60$ competing at $H\le1600$, the slope required to lie in $[-1.70,-1.20]$ — B is a test of level-order convergence, not of the exponent law); `C2.3-h0-threshold` (F $(h_0,a_-,a_+)=(3.5,-1.75,-1.75)$, $\alpha>-3$, $h_0\ge3$: error-envelope slope $+0.468$ against $h_0-3=+0.50$, endpoint exponent $-1.25$ rejected; $J=0.1204213799$, $S(400,800,1600)=4.79,\,6.71,\,9.43$: the divergent side of the $h_0<3$ threshold); `C2.4-abel` ($\sum L_nr^n=r^{-h_0}\int_{Q_V}I(ry)$ at $r=0.97,0.985$ to $10^{-12}$ (A) and $4\times10^{-8}$ (D, float64 cancellation with $g_N\sim N^{2.5}$), the Abel limit approaching $J$ at $r=0.999,0.9999$; break: dropping the $-1$ of $\hat f_0$ violates the identity); `C2.5-rays` ($\theta=\pi$: relative error $<10^{-15}$ at $H=40$ for A, B, D; $\theta=80^\circ$: envelope slopes $-1.75,-0.64,+1.41$ against $-\alpha-2=-1.65,-0.60,+1.50$, error at $H=40$ from $2\times10^{-4}$ to $28$ — the break leg: the fold-arc ray is not exponentially convergent). Script run: 14/14 PASS (with C4.1; after the fix pass).

## §3 Consequences for R80's sector statements (C3)

\subsection*{Setup}
Uses C1, C2 and record 074's claims C2.1–C2.5, C3, C4, (1.5), (3.4)(v). A statement *needs the exchange* if it asserts that the region integral (1.3) of a given pair of inputs equals a sum over $(h,m)$ sectors, or that a single sector of that integral is a finite number; it does *not* need it if it is a statement about $\hat f_m(h)$ or about one $(L_0^+,L_0^-)$ eigenspace.

\subsection*{Derivation}
*(3.1) Statements about the transform alone — unaffected.* $\hat f_m(h)=\frac1h\int_0^{2\pi}e^{im\theta}(e^{\sigma_V h}-\delta_{m,0})d\theta$ is an entire function of $h$ computed from $\sigma_V$ alone (074 `C2.4-real-zeros` evaluates it from the $\sigma_V$ array; `C3.1-table` here reproduces the zero of $\hat f_4$ at $-2.356$). The constant-$\sigma$ closed forms and $1/\hat f_0=h/2\pi(e^{\sigma h}-1)$ (074 (2.6)–(2.7)), the actual-$\sigma_V$ forms (2.8), the real zeros of $\hat f_4$ ($-2.36$) and $\hat f_6$ ($-4.89,-1.91$) with their asymptotic signs, the inverse-region inequality (2.5) and the limits (2.9) involve no expansion of an integrand and no sum over sectors. The fold arcs enter them only through $\sigma_V$ itself (they produce the $h\to+\infty$ asymptotics $\hat f_m\simeq(4\beta^2)^hA_m/h$, 074 (2.8)), and that asymptotics is a property of the region, exact whatever the inputs.

*(3.2) Eigenspace statements — unaffected.* $F|h,m\rangle=\hat f_m(h)|h,m\rangle$, $G_W^{-1}=\frac i\kappa c_0^-c_0^+F^{-1}$ on each eigenspace (074 (2.1), (2.4)), the per-sector identity $\hat f\hat f^{-1}\hat f=\hat f$ of C3 (3.1), the slab telescoping (3.2)–(3.3), the zeros of $G_W$ on a sector, and C4's residue criterion (the $m_3$-integrated projection onto the finite-dimensional $W_{(N,\bar N)}(P_*)$) are statements about one eigenspace at a time. None involves $\sum_{h,m}$.

*(3.3) Form-level statements — need the exchange, and get it in the sense of C2.* The identification of the region integral with the level-sum form, $p^{\rm circ}(\Sigma,\Sigma')=\omega(\Phi\Sigma',G\Phi\Sigma)=\sum_{h,m}c_{h,m}(\Sigma,\Sigma')\hat f_m(h)$ (074 (1.3)$\to$(2.1), and (1.5)'s "level-sum form"), is exactly the series of C2. For tachyon inputs it holds: in every order iff $\alpha>-1$; in level order for $\alpha>-3$, $h_0<3$; as an Abel sum of the level series for all momenta (C2.4). The same holds for C3's form-level reading $\mathcal V_4p^{-1}\mathcal V_4=\mathcal V_4$ on given inputs: per sector the composite equals $\hat f_m(h)$ times the same $c_{h,m}$ (the projector being invisible between circle states, 074 C3), so the composite's sector series *is* the series of $p^{\rm circ}$, term by term, and the identity holds in whichever summation defines $p^{\rm circ}$'s level sum. For $\alpha\le-1$ no single sector of $p^{\rm circ}(\Sigma,\Sigma')$ is a finite number (C2.2): "the $m=4$ part of $p^{\rm circ}$ on these inputs" does not exist, although the $m=4$ eigenvalue $\hat f_4(h)$ does.

*(3.4) The pole reading under PH31.* C4's poles of $\mathcal V_5p^{-1}\mathcal V_5$ at zeros of $\hat f_m$ need, besides the residue (an eigenspace object, (3.2)), that the remaining sectors sum to something regular at $P_*$. For the four-point form, in sector order that remainder is not defined whenever the cross-channel exponent is $\le-1$ (C2.2), and in level order, or as the Abel sum, it is (C2.3, C2.4); for the five-point composite the same is expected by analogy with the four-point form, but not computed (its sector series carries $1/\hat f_m(h)$ and the transforms of 074's regions $Q_5(m_3)$, not $\hat f_m(h)$, so C2's growth analysis does not transfer). For the four-point form the Abel sum is $J$, an integral of a smooth integrand over the compact $\bar Q_V$, entire in the exponents $h_0,a_\pm$ (dominated convergence for the derivatives). The analogous regularity for the five-point composite (region $Q_5(m_3)$, $1/\hat f_m$ inserted) is not computed here.

*(3.5) Corrections to 074's wording.* (i) 074 (1.5): "on the fold arcs it sits at its radius of convergence, where the circle $|w|=\sqrt{|q|}$ passes through the ordinary punctures" — correct for the radius; "with the $1/h$ of the $s$-integral as the only damping" — incomplete: the integrated form also gains $1/|m|$ (sector order) or $1/n$ (level order) from the arcs' finite angular width (C2.1, (2.4)), and convergence is decided by the cross-channel collision exponent $\alpha$ at $\theta=0,\pi$, outside $Q_V$ (C1.2), not by anything on the arcs. (ii) 074 (1.5)'s "for finite-level inputs (A3) … no convergence hypothesis enters" is right for the region integral and for the open disc, not for the level-sum form on $\bar Q_V$, which touches $|y|=1$: there the threshold $\alpha>-1$ applies, and (§4 (4.3)) excited inputs lower $\alpha$. (iii) 074 (3.4)(v) "(3.1) as an operator identity on $\mathcal I$ does not depend on it" is correct and is (3.2)–(3.3) here. (iv) 074 §6.3 "Not checked: the $(h,m)$ expansion on the fold arcs (marginal convergence)" is now checked, with the verdict of C2.

\subsection*{Commentary}
(3.3): the reason the form-level identity survives divergence of the sectors is that both sides are the same series term by term; what fails for $\alpha\le-1$ is the decomposition of a matrix element into finite sector contributions, not any identity between operators. (3.4): this is the concrete instance of 074 H1's remark that $\Phi^\dagger$ is not continuous level by level: $\Phi^\dagger$ applied to $G\Phi\Sigma$ and summed sector by sector diverges for $\alpha\le-1$, even for finite-level $\Sigma$ at real momenta. A remark not checked here: the fixed-$m$ values $\mathcal F_m$, defined for $\alpha>-1$, continue meromorphically in $\alpha$ with poles at $\alpha=-1,-\tfrac32,-2,\dots$ (zeta-continuation of $\sum_NN^{-2\alpha-3-k}$), whose residues are $\propto A_m$ at leading order and cancel in $\sum_mA_m$ (the arcs' indicator vanishes at $\theta=0$); this would make sector values available by analytic continuation in the momenta, with spurious poles that cancel in the sum.

\subsection*{Result}
R80's explicit kernels (C2.4: closed forms, $1/\hat f_m$, the real zeros of $\hat f_{m\ne0}$ and their asymptotic signs), C2.2, C2.3, C2.5 and C3's per-sector identity are statements about the region transform or about single eigenspaces and are **not affected** by the fold arcs. What needs the exchange of $\int_{Q_V}$ and $\sum_{h,m}$ is the evaluation of $p^{\rm circ}$ (and of $\mathcal V_4p^{-1}\mathcal V_4$) on given inputs as a sum of sector contributions: valid in every order iff $\alpha>-1$, in level order or as an Abel sum beyond. The pole reading under PH31 needs the level-order (or Abel) remainder, not sector-by-sector sums.

\subsection*{Verification}
(3.1) rests on `C3.1-table` (the zero of $\hat f_4$ recomputed with this record's independent $\sigma_V$ bisection and graded quadrature) and on 074's own `C2.4-real-zeros`; (3.3) on `C2.2-absolute`, `C2.2-sector-divergence`, `C2.3-level-order`, `C2.4-abel`. (3.2), (3.4) and (3.5) are readings of 074's statements against C2, not machine-checked; the meromorphic continuation in the commentary is not checked.

## §4 Regime and momentum dependence (C4)

\subsection*{Setup}
Uses (1.4), C2. Mandelstam variables of §1 (1.3): $s=-(k_c+k_d)^2$ (the channel through the circle), $t=-(k_a+k_c)^2$, $u=-(k_a+k_d)^2$; on shell $\alpha'(s+t+u)=-16$.

\subsection*{Derivation}
*(4.1) On shell.* $a_-=-3-\tfrac{\alpha'}2t$, $a_+=-3-\tfrac{\alpha'}2u$, $h_0=-\tfrac{\alpha'}2s-2=-(a_-+a_+)$ (`C4.1-onshell-map`, exact). The thresholds of C2 become thresholds on the cross-channel momenta, at the cross-channel poles of the Virasoro–Shapiro amplitude ($\tfrac{\alpha'}4t=-1,0,1,\dots$ is $a_-=-1,-3,-5,\dots$):
$$
\begin{array}{ll}
\text{every order (absolute), }\int_{Q_V}\leftrightarrow\sum_{h,m}: & \alpha't<-4\ \text{and}\ \alpha'u<-4\quad(\text{both below the tachyon pole; then }\alpha's>-8)\\
\text{level order, absolute:} & \alpha't,\alpha'u<-2\ \text{and}\ \alpha's>-8\\
\text{level order, conditional:} & \alpha't,\alpha'u<0\ (\text{below the massless pole})\ \text{and}\ \alpha's>-10\\
\text{no ordering converges; }J=\text{Abel sum}: & \text{otherwise.}
\end{array}
\tag{4.1}
$$
The growth exponents of C1 change sign with the cross-channel momentum: fixed $m$, $h^{-2\alpha-2}=h^{4+\alpha't}$ (for $\alpha=a_-$), growing iff $t$ is above the tachyon pole; fixed $\theta$ on the arcs, $h^{-\alpha-1}=h^{2+\alpha't/2}$, growing iff $\alpha't>-4$ as well; at the arc midpoint $h^{h_0-1}=h^{-\alpha's/2-3}$, set by the channel momentum, growing iff $\alpha's<-6$. The $s$-channel OPE representation of the full on-shell amplitude over the injectivity disc (074 (2.9)(iii)) converges sector by sector under exactly the first line: the fold arcs add nothing beyond the cross-channel tachyon poles in sector order, and remove the $\theta=0,\pi$ collisions in level order.

*(4.2) Off shell.* $h_0$ and $a_-$ are independent ($a_+=-h_0-a_-$): at any channel momentum $P$ (any $h_0$, in particular at 074's real zeros $h_*$) the relative momenta $\kappa_{ac}+\kappa_{bd}$ move $\alpha$ through all four regimes. No region of the channel momentum is protected: whether the sector-by-sector evaluation of $p^{\rm circ}$ on tachyon pairs converges is decided by the cross-channel exponent, which the sector label $(h,m)$ does not see.

*(4.3) Excited inputs (argued, not machine-checked).* For inputs with oscillator excitations the leading singularity of the holomorphic factor at $y=1$ comes from the OPE of the colliding pairs $(a,c)$, $(b,d)$; contracting an oscillator $\partial X$ of one operator with the exponential of the other lowers the exponent by one per oscillator, with a coefficient $\propto k$ that is non-zero for generic momenta (example: $(\epsilon\cdot\partial X)^\nu e^{ik_aX}(z)\,e^{ik_cX}(w)\supset(\tfrac{\alpha'}{2}\epsilon\cdot k_c)^\nu(z-w)^{-\nu}\,\cdots$, non-zero for $\epsilon\cdot k_c\ne0$). So $a_\mp\to a_\mp-\nu_\mp$ holomorphically and $a_\mp-\bar\nu_\mp$ antiholomorphically, $\nu_-\le N_a+N_c+N_b+N_d$ (equality generically), and (1.7)–(2.3) give the sector-order threshold
$$
\min_\mp\Big(a_\mp-\tfrac12(\nu_\mp+\bar\nu_\mp)\Big)>-1 .
\tag{4.3}
$$
At fixed momenta, inputs of high enough level violate it. Hence the every-order exchange holds, at any momentum, only on level-bounded subspaces. On all of $\mathrm{Sym}^2\mathcal H_0$ the level-sum form of $p^{\rm circ}$ is available only in level order or as an Abel sum. This sharpens 074 A3's "finite correlators" to "finite correlators, whose sector expansions on $\bar Q_V$ converge in the order and range of (4.1)–(4.3)".

*(4.4) Limiting ray.* At $\theta=\pi$ ($\sigma_V=\ln\tfrac94$, $\rho=\ln4$) the ray sum converges geometrically with ratio $\tfrac14$, times the polynomial $T_n(\pi)\sim n^{-2a_+-1}$, for every momentum (`C2.5-rays`: $<10^{-15}$ at $H=40$ for A, B, D, including D where the fold-arc ray diverges). Rays off the arcs converge with ratio $e^{-\rho(\theta)}$, $\rho\simeq\sqrt{3(\theta_1-\theta)}$ at the arc ends. The marginal behaviour is confined to the closed fold arcs.

\subsection*{Commentary}
(4.1): the coincidence of the every-order threshold with the cross-channel tachyon pole is structural. Near $y=\pm1$ the fixed-halves integrand is the pull-back of the $t$/$u$-channel collision region, whose local integrability is what the pole at $\alpha't=-4$ measures; in sector order the region's shape does not help, because each Fourier mode feels the collision. (4.3) is the only argued step of the record: the integer shifts are standard OPE counting, and the coefficients' non-vanishing for generic momenta is not shown in general. It is a scope statement for the regime, not an input of C1–C3.

\subsection*{Result}
$$
\boxed{\ \text{On shell: every order}\iff\alpha't,\alpha'u<-4;\ \ \text{level order}\iff\alpha't,\alpha'u<0,\ \alpha's>-10\ (\text{absolutely for }<-2,\ >-8);\ \ \text{else Abel/continuation only}\ }
$$
Off shell, $a_-$ and $h_0$ are free, and every regime occurs at every channel momentum. Excited inputs lower the effective exponent by half the total level of the colliding pairs (argued).

*Scope for the actual $p_{2,2}$.* (i) On shell at four points the integrand of $p_{2,2}$ equals that of $p^{\rm circ}$ pointwise in $q$ (074 C1.4, modulo 032 (4.5)), so the on-shell regimes of (4.1) and the Abel statement are statements about $p_{2,2}$ itself on four on-shell tachyons. (ii) Off shell the dressed gluing $\tilde G$ is not a function of $L_0^\pm$ (074 (1.6)) and on the fold arcs the puncture positions move as well, so neither the coefficients $c_{h,m}$ nor the reading of $(h,m)$ as eigenvalues transfers; the off-shell part of C2–C4 is a statement about the model A2 only.

\subsection*{Verification}
`C4.1-onshell-map` (sympy, exact: the on-shell exponents in terms of $s,t,u$ and $s+t+u=-16/\alpha'$ from conservation; the identity $a_-+a_++h_0=0$ off shell with conservation; break leg: without conservation the identity fails). (4.1)'s regimes follow from C2 and (4.1) by substitution. (4.3) is not machine-checked.

## Self-review

1. *Objective vs task.* The objective was whether R80's sector formulas are formal on the fold arcs. Answer: the kernels themselves ($\hat f_m$, $1/\hat f_m$, the real zeros, the per-sector identity) are not affected, because they are statements about the region's transform and single eigenspaces (C3). What the fold arcs (more precisely, the cross-channel collisions at $\theta=0,\pi$ on the fold circle) affect is the decomposition of a given matrix element of $p^{\rm circ}$ into sector contributions. That decomposition is absolutely convergent iff $\alpha>-1$, level-order convergent in a wider range, and Abel-summable always (C2, C4). The verdict has its regime.
2. *Weakest step.* (4.3), the extension to excited inputs, is argued, not checked. It is a scope statement and enters no other node. Among the computed results the weakest is the level-order rate for B (slope $-1.43$ against the predicted $-1.30$): two power laws compete at accessible $H$, so B tests convergence only; the two exponents of (2.4) are tested separately at C and E, where each dominates (tolerance $0.1$, the other rejected). The convergence verdict does not depend on the rate.
3. *Not checked.* The five-point composite (C4 of 074): whether the level-order remainder is regular at $P_*$ there. The meromorphic continuation of the sector values (commentary of §3). Non-tachyon inputs, beyond the argument of (4.3). $\beta\ne3/2$; the analysis only uses that the arcs avoid $\theta=0,\pi$ and that $\rho$ is piecewise monotone. Complex momenta: the thresholds read with $\Re a_\pm$, not run. The actual $p_{2,2}$ off shell (§4 Result, *Scope*: on shell at four points the verdict is about $p_{2,2}$ itself; off shell nothing transfers). None of these changes the verdict for tachyon inputs at $\beta=3/2$.
4. *What a stronger physicist would find in five minutes.* That the brief's premise (marginality from "the circle passing through a puncture") misidentifies the source of the growth exponent. §1 (1.5) corrects it: the exponent comes from the cross-channel collision, outside $Q_V$. The same physicist would also note that the every-order threshold is the cross-channel tachyon pole, so the sector-by-sector representation of $p^{\rm circ}$ has the same domain as the $s$-channel OPE representation of the full amplitude (§4 (4.1)). Both are stated. A further point is only partly addressed: R80's operator statements ($G\Pi G=G$) are defined level by level, so the natural summation for them is the level order. The record says this (§2 commentary, §3), but does not rewrite 074's text, which is not this record's to edit.

## Proposed ledger entry

**R? — Fold-arc convergence of the sector expansion of the fixed-halves gluing (tachyon inputs, $\beta=3/2$): the region transforms and per-sector statements of R80 are unaffected; the sector decomposition of $p^{\rm circ}$'s matrix elements converges in every order iff the cross-channel exponent $\alpha>-1$, in level order for $\alpha>-3$, $h_0<3$, and is Abel-summable always [Numerical / Verified]**

- **Source**: `agent/derivations/079-fold-arc-convergence.md` C1–C4; `codes/verify-fold-arc-convergence.py` 14/14 PASS, seed 20261004 (`agent/scratch/computator/computator-079-fix-20261004T105800/run-fix.log`; run 1: 13/13, before the fix pass).
- **Scope**: fixed-halves model (074 A5, a model assumption); four tachyon inputs with arbitrary momenta subject to conservation; $\beta=3/2$; real momenta (complex: $\Re a_\pm$, not run); excited inputs by the argued shift (4.3) only. For the actual $p_{2,2}$: on shell at four points its integrand is the same function of $q$ (074 C1.4, modulo 032 (4.5)), so the on-shell regimes (4.1) and the Abel statement hold for $p_{2,2}$ itself on four on-shell tachyons; off shell nothing transfers (the dressed gluing is not a function of $L_0^\pm$, 074 (1.6)).
- **Statement**: the integrand is $\mathcal N|y|^{h_0}|1-y|^{2a_-}|1+y|^{2a_+}$, $y=q/4\beta^2$, $a_-+a_+=-h_0$. The sector coefficients satisfy $c_{h,m}(4\beta^2)^h=\mathcal Ng_Ng_{\bar N}\sim h^{-2\alpha-2}$ at fixed $m$, and the level-$h$ term is $\sim h^{-\alpha-1}$ (oscillating) at fixed $\theta$ on the arcs and $h^{h_0-1}$ at the arc midpoint. Here $\alpha=\min a_\pm$ is the exponent of the cross-channel collisions at $\theta=0,\pi$ on the fold circle, outside $\bar Q_V$, not of anything on the arcs. $\sum_{h,m}c_{h,m}\hat f_m(h)$ is absolutely convergent iff $\alpha>-1$ (on shell: $\alpha't,\alpha'u<-4$, the cross-channel tachyon poles). For $\alpha\le-1$ every fixed-$m$ sector sum with $A_m\ne0$ diverges like $H^{-2\alpha-2}$ ($\log H$ at $\alpha=-1$). The level-ordered sum converges to the region integral for $\alpha>-3$ and $h_0<3$ (absolutely for $\alpha>-2$, $h_0<2$). For every momentum the region integral is the Abel sum of the level series. The convergence is polynomial on the fold arcs and geometric off them (ratio $\tfrac14$ at $\theta=\pi$). R80's closed forms, $1/\hat f_m$, the real zeros of $\hat f_{m\ne0}$ and C3's per-sector identity are statements about the region transform and single eigenspaces, and are unaffected. The pole reading of R80 (C2.4's pole clause and C4, under PH31) is a statement about the level-order or Abel remainder, not about sector-by-sector sums: in fixed-$m$ sector order the remainder is not defined for $\alpha\le-1$ (four-point form; the five-point composite is not computed).
- **Status**: C1 (closed form, Darboux growth) — Verified (exact on-shell match with an independent Möbius frame; Darboux against exact coefficients to $N=1600$). C2.1–C2.2 (bound, absolute threshold $\alpha>-1$ in both directions) — Proven modulo the sampled piecewise monotonicity of $\sigma_V$ and the Numerical arc geometry of R80 C1.3 ($\cos\theta_1=\tfrac7{25}$, $\sigma_V(0)=\ln\tfrac94$, $\beta=3/2$); C2.3–C2.4 (level-order thresholds, Abel sum) — Argued (leading-order endpoint/coalescence analysis (2.4)), Numerical at six momenta; C2.5 — Numerical. C3 — Proven (a reading of 074's statements against C2). C4.1 — Verified (sympy). C4.3 (excited inputs) — Argued.
- **Verification** (proposed lines): 2026-10-04 – exact/numerical check – `codes/verify-fold-arc-convergence.py`, 14/14 PASS: `C1.1-onshell` (break: no ghost factor), `C1.1-ghost`, `C1.2-coeffs`, `C1.3-darboux-m` (break: exponent $-\alpha-1$), `C1.3-darboux-theta` (break: generic exponent at $\pi/2$), `C2.1-profile`, `C3.1-table` (reproduces 074's zero of $\hat f_4$), `C2.2-absolute`, `C2.2-sector-divergence` (break: stationary for $\alpha>-1$), `C2.3-level-order` (exponents at C and E to $0.1$, subdominant rejected; break: D diverges), `C2.3-h0-threshold` (F diverges through the midpoint), `C2.4-abel` (break: wrong $\hat f_0$), `C2.5-rays` (break: fold-arc ray not exponential), `C4.1-onshell-map` (break: no conservation).
- **Consequence for R80**: 074 (1.5)'s "with the $1/h$ of the $s$-integral as the only damping" should read: the integrated form gains a further $1/|m|$ (sector order) or $1/n$ (level order) from the arcs' angular width, and convergence is set by the cross-channel exponent $\alpha$. 074 (1.5)'s "for finite-level inputs … no convergence hypothesis enters" holds for the region integral (and the open disc), not for the level-sum form on $\bar Q_V$, which touches $|y|=1$: there the threshold $\alpha>-1$ applies to every-order summation, and excited inputs lower $\alpha$ ((3.5)(ii), (4.3)). The pole reading under PH31 (R80 C2.4's pole clause, C4) needs the level-order or Abel remainder (C3.3). The §6.3 item "not checked: fold arcs" is closed by this entry.

## Fix pass (critic iteration 1)

Critic report `agent/reports/critic-079-20261004T102600.md` (REVISE, light). One line per finding, in the order applied.

- **#13 [major]** Proposed ledger entry: **Statement** now ends with the C3.3 qualifier (pole reading of R80 C2.4/C4 under PH31 = level-order or Abel remainder; sector-order remainder undefined for $\alpha\le-1$; five-point composite not computed); **Consequence for R80** now carries (3.5)(ii) (074 (1.5)'s "no convergence hypothesis enters" holds for the region integral, not for the level-sum form on $\bar Q_V$) and the C3.3 line. Body (§3 Result, (3.5), self-review) already said so; no change there.
- **#14 [minor]** (with note #2) Entry **Status**: C2 split into C2.1–C2.2 Proven modulo the sampled profile and the Numerical arc geometry (R80 C1.3), C2.3–C2.4 Argued + Numerical at six momenta, C2.5 Numerical. The claim tree's justification kinds are unchanged (C2.3 cites (2.4) and its check, as before); only the entry's calibration changed.
- **#11 [minor]** Scope for the actual $p_{2,2}$ added: §4 Result (*Scope for the actual $p_{2,2}$*, (i) on shell = $p_{2,2}$ itself by 074 C1.4 mod 032 (4.5), (ii) off shell nothing transfers, 074 (1.6)), self-review item 3, entry **Scope**. No new computation; C4's statement unchanged (it is already a statement in the model's momenta).
- **#3 [minor]** C2.4 (node) and (2.4) text: "any convergent ordering" → the level series in its natural order converges to $J$ whenever it converges (Abel); every ordering only under absolute convergence ($\alpha>-1$); square truncation in the conditional regime not covered. The §2 Result table was already in level order; unchanged. Statement of C2.4 changed (narrowed), justification unchanged. Dependents: C2 (statement says "the level-ordered sum converges to $J$" — still holds), C3.3, C3 (use level order/Abel only — still hold).
- **#4 [minor]** C2.4 now cites `by C1.1, C1.2` (closed form and sector decomposition (1.6); uniform convergence on $\bar Q_V$ for $r<1$). Justification only.
- **#8 [minor]** (3.4) reworded: the sector-order/level-order statement is made for the four-point form (C2.2–C2.4); for the five-point composite "expected by analogy with the four-point form, but not computed", with the reason C2 does not transfer. Node C3.3 unchanged (already hedged).
- **#6 [note, wording]** "($\log H$ at $\alpha=-1$)" added to the entry's Statement and to node C2.2, as in (2.3); the entry's "every fixed-$m$ sector sum" restricted to $A_m\ne0$, as (2.3) states.
- **#19 [minor]** Checks renamed after the node they support, in the script and every occurrence in the record (tree tags, §1–§3 Verification, (3.1), entry Verification): `C2.0-profile` → `C2.1-profile` (C2.1, C4.4), `C2.0-table` → `C3.1-table` (C3.1; also listed on C2.1 for the $\hat F_m$ quadrature), `C1.2-darboux-m` → `C1.3-darboux-m` (C1.3). Also `C2.1-absolute` → `C2.2-absolute`: it is tagged on C2.2 (absolute convergence for $\alpha>-1$) and would otherwise sit on the wrong node once C2.1 carries `C2.1-profile` (same rule, not named by the critic).
- **#17 [minor]** `C2.3-level-order` made discriminating: the exponent law is asserted to $0.1$ at C (endpoint, $-0.638$ vs $-0.60$) and E (midpoint, $-0.637$ vs $-0.60$), where one term dominates by $\ge0.5$, and at D (divergent, $+0.471$ vs $+0.50$), with the subdominant exponent rejected ($>0.3$ away) at each; B now tests only level-order convergence (slope $-1.430$ in the bracket $[-1.70,-1.20]$ of its two competing exponents), not the exponent law. Record: §2 Verification, self-review item 2, entry Verification line.
- **#18 [minor]** New check `C2.3-h0-threshold` at F $=(h_0,a_-,a_+)=(3.5,-1.75,-1.75)$ ($\alpha>-3$, $h_0\ge3$): level-order error envelope grows, slope $+0.468$ against $h_0-3=+0.50$ (endpoint $-1.25$ rejected); $|S(1600)-J|=9.3$. PASS by showing divergence. Added to C2.3's tag, the §2 table (row F) and Verification, and the entry.
- **#20 [note]** Script domain: a guard raises `ValueError` if $h_0+n=0$ for an even $n$ (the $m\ne0$ terms are $0/0$ there); the domain is stated in the docstring and in §2 Verification. No test point is affected.
- **Not changed**: notes #1, #5, #7, #9, #10, #12, #15, #16 (no action asked); #2 folded into #14.
- **Re-run**: `.venv/bin/python codes/verify-fold-arc-convergence.py` (formatted with `ruff format`), run from `agent/scratch/computator/computator-079-fix-20261004T105800/` so that the relative scratch path of the script writes there and run 1's log is untouched: **14/14 PASS**, seed 20261004, 17 s (`run-fix.log`). Every previous check still passes under its new name.
- **Changed nodes**: C2.4 (statement narrowed to the natural level order; justification gains C1.1, C1.2), C2.2 (statement: "$\log H$ at $\alpha=-1$", already in (2.3)), C2.3 (justification: one more check). Dependents: C2 (its statement already reads "level-ordered sum converges to $J$" — holds), C3 and C3.3 (use level order / Abel only — hold), C4 (thresholds unchanged — holds). No node's truth value changed; the entry's Statement, Scope, Status and Consequence were updated (#13, #14, #11, #6).
