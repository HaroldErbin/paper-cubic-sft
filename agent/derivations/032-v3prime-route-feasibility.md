---
id: 032-v3prime-route-feasibility
brief: agent/briefs/active-computator-14a-v3prime-regions-20260914T052500.md; agent/briefs/active-computator-14b-operator-identity-20260914T073000.md (§4); agent/briefs/active-computator-14c-verdict-20260914T080000.md (§5–§8)
plan: plans/next-steps-2026-09-07.md Task 14 (14a → 14b → 14c)
script: codes/verify-v3prime-route.py
created: 2026-09-14
depends: 030 §5.4, §6.2; R2; notes-harold/notes-old/sections/hb_4pt.tex; notes-harold/notes_4_point_summary.tex
---

# 032 — The $\mathcal V_3'$ route (α-rev): feasibility study (14a: covering; 14b: operator identity §4; 14c: seams, verdict §5–§8)

## Restated task and objective

**Literal task (14a).** For the single-strand option (α-rev) of 030 §5.4 — auxiliary
$\Phi\in\mathcal H_0$, reversed-range propagator $\hat{\mathsf P}=b_0^+(e^{\sigma L_0^+}-1)/L_0^+$,
coupled through Harold's asymmetric vertex $\mathcal V_3'$ on its special leg — (1) fix the
conventions ($\mathcal V_3'$ maps, $Z_4^{(\alpha)}(q)$, Feynman regions $\mathcal F'_\alpha$,
$\mathcal M'_\times$), (2) compute the **coordinate-extension precondition**: the maximal
$\sigma_{\max}$ for which the special-leg coordinate disc extends to radius $e^{\sigma}$ and
stays embedded, (3) compute the **covering map** (6.1): per channel the region
$R_\alpha(\sigma)=\{Z_4^{(\alpha)}(e^{\sigma'+i\theta}):0\le\sigma'\le\sigma\}$, the gap
$\mathcal M'_\times\setminus\bigcup_\alpha R_\alpha$ and the overlap, and whether a
$\sigma(\theta)$ covers $\mathcal M'_\times$ once without overlap. 14b: the operator identity
(6.2). 14c: verdict.

**Motivating objective.** The second question of the 4-point summary note (`notes_4_point_summary.tex` §Questions):
can the interior $\mathcal M'_\times$ be covered by the same $\mathcal V_3'$ family continued to
$|q|>1$? A "no" for every $\sigma(\theta)$ is a covering obstruction of Sonoda–Zwiebach's kind
and leaves the $V_4$-kinetic theory (γ) as the only cubic theory reproducing $V_4$.
**No covering prescription is claimed**; the deliverable is the map of what is covered.

## §0 Verdict table

| row | question | answer | status |
|---|---|---|---|
| (P) | precondition: $\sigma_{\max}$ for the special-leg disc | $r_{\max}=\frac{2\beta'(\gamma'-1)}{\gamma'+1}$ ($\alpha'=0$); $\sigma_{\max}=\ln r_{\max}$ (one-sided cut) or $2\ln r_{\max}$ (symmetric cut, H1); $=0$ for the tangent (SZ-type) vertex, $>0$ with slack (§2) | computed, self-checked (P1a–f); cut convention stated, not chosen |
| (i-s) | $s$-channel region, density, gap, overlap | $R_s$ = image of $1<|q|\le e^{\sigma(\theta)}$, injective; grid $h=0.004$; with the $S_3$ seam $|R_s|=10.845$; with constant $\sigma$: gap-free only for $\sigma\ge0.879$, overlap-free only for $\sigma\le0.434$ (§3) | computed (C2a–h) |
| (i-t) | $t$-channel | $R_t=$ image of $R_s$ under $z\mapsto z/(z-1)$; $|R_t|=1.838$ (seam) | computed |
| (i-u) | $u$-channel | $R_u=$ image of $R_s$ under $z\mapsto1/(1-z)$; $|R_u|=1.838$ (seam) | computed |
| (i) | covering $\sigma(\theta)$ exists? | **constant $\sigma$: no** ($\sigma_{\rm ov}=0.434<\sigma^*=0.879$, over-determined). **$\theta$-dependent: yes**, e.g. the $S_3$ seam $\sigma(\theta)\in[0.434,0.880]$, gap 0.09 %, overlap $\sim0$; under-determined (works for the sampled star-shaped partitions). Needs $\Phi\in\mathcal H$ (030 count (i)) and a slack vertex $\gamma'\ge9.19$ (one-sided cut) / $\ge3.15$ (symmetric cut) at $\alpha'=0$ for (P-strict). Gap 0.09 % measured at one grid ($h=0.004$), attributed to discretisation, $h$-scaling not tested | computed; sewability beyond four points not checked |
| (ii) | operator identity (6.2) on shell | **holds on shell to the covering accuracy** (rel. diff $-7\times10^{-4}$, $-9\times10^{-4}$ at two generic momenta; deficit = the 0.09 % seam gap); reduces to (6.1) + the pull-back identity (4.5) *under the sewing-convergence hypothesis (P)*, no Jacobian/sign/boundary anomaly on $|q|>1$ by argument; the on-shell check tests (6.1) with the tachyon weight, not (m) itself; (c),(s) invisible on shell, (l) harmless (§4) | argued (measure) + computed (C3a–f, 2 break legs); (4.5) not machine-checked |
| (iii) | verdict | **conditional go** — see §6: seam coordinates continuous at first order on the $S_3$ seam (reflection symmetry), discontinuous at second order ($\sim15\,\%$ of the disc radius) on every admissible seam; strictly cubic version expected to fail off shell on non-primary external states (not evaluated); collar term (5.2) a sufficient cure under one checkable condition | geometry: proven + computed (part 4, 14d); gauge statement: argued |

## §1 Conventions

**The vertex $\mathcal V_3'$** (Harold, `hb_4pt.tex`; overview §explicit; R2). Three punctures at
$z=0,\infty,1$ on the sphere; real parameters $\alpha',\gamma',\beta'$; local coordinate $w$,
$|w|\le1$, at each puncture:

| puncture | leg | map $z=f(w)$ | image disc $f(\{|w|\le1\})$ (centre, radius on the real axis) |
|---|---|---|---|
| $z=0$ | $A_1$ (symmetric) | $f_0'(w)=\dfrac{w}{\alpha'w+\gamma'}$ | endpoints $-\tfrac{1}{\gamma'-\alpha'},\ \tfrac{1}{\gamma'+\alpha'}$: $c_0=-\tfrac{\alpha'}{\gamma'^2-\alpha'^2}$, $\rho_0=\tfrac{\gamma'}{\gamma'^2-\alpha'^2}$ |
| $z=\infty$ | $A_2$ (symmetric) | $f_\infty'(w)=\dfrac{\alpha'w+\gamma'}{w}=1/f_0'(w)$ | exterior $\{|z-\alpha'|\ge\gamma'\}$ |
| $z=1$ | $A'$ (special) | $f_1'(w)=\dfrac{2\beta'-w}{2\beta'+w}$ | for radius $r<2\beta'$: endpoints $\tfrac{2\beta'-r}{2\beta'+r},\tfrac{2\beta'+r}{2\beta'-r}$: $c_1(r)=\tfrac{4\beta'^2+r^2}{4\beta'^2-r^2}$, $\rho_1(r)=\tfrac{4\beta'r}{4\beta'^2-r^2}$ |

(1.1) The image discs are computed from the fact that a real Möbius map sends a circle
centred on the real axis to a circle centred on the real axis, so the image disc is fixed by
the images of $w=\pm r$. Harold's non-overlap conditions $\alpha'\le\gamma'-1$ (this is
$f_0'(D)\cap f_\infty'(D)=\emptyset$) and $\gamma'\ge\frac{1}{A-2}\big(A+\frac{4\beta'}{1-2\beta'}\big)$
(this is $f_0'(D)\cap f_1'(D)=\emptyset$; at $\alpha'=0$ it reads
$\gamma'\ge\frac{2\beta'+1}{2\beta'-1}$) are reproduced by these disc data — checked in §2. The
$z\to1/z$ symmetry ($f_1'(-w)=1/f_1'(w)$, $f_0'\leftrightarrow f_\infty'$) makes the
$f_1'$–$f_\infty'$ condition identical to the $f_1'$–$f_0'$ one. Slack parameters $A,B$ of
Harold's notes: with his inequality $\gamma'\ge\frac1{A-2}(A+\frac{4\beta'}{1-2\beta'})$, $A=1$ corresponds
to $\alpha'=0$ and saturation ($\gamma'=2$ at $\beta'=3/2$) is $B=0$; the earlier "$A=B=0$ is the
tangent vertex" was a parametrisation slip (critic 032 H1, not checked against `hb_4pt.tex`).

**Puncture location after twist gluing on the special legs** (R2, Verified): independent of
$\alpha',\gamma'$; with $\beta'=\beta$,
$$
Z_4^{(s)}(q)=\frac{(q+4\beta^2)^2}{16\beta^2\,q}=\cosh^2 H(q),\qquad H(q)=\ln\frac{2\beta}{\sqrt q},
\qquad Z_4^{(t)}=\frac{Z_4^{(s)}}{Z_4^{(s)}-1},\qquad Z_4^{(u)}=\frac{1}{1-Z_4^{(s)}} .
\tag{1.2}
$$
Punctures at $0,1,\infty,Z_4$; $\mathcal M_{0,4}=\mathbb C\setminus\{0,1\}$. Parametrisation
$q=e^{-s+i\theta}$; the propagator side is $s\ge0$, the continuation asked about is
$s\in[-\sigma(\theta),0]$, i.e. $|q|=e^{\sigma}\in[1,e^{\sigma(\theta)}]$.

(1.3) *Two facts about (1.2) used throughout.* (a) $Z_4^{(s)}$ is invariant under the involution
$q\mapsto16\beta^4/q$, whose fixed circle $|q|=4\beta^2$ maps to the real segment $[0,1]$
($q=4\beta^2e^{i\varphi}\Rightarrow Z_4^{(s)}=\cos^2(\varphi/2)$). Hence $q\mapsto Z_4^{(s)}(q)$ is
**injective on the disc $|q|<4\beta^2$**, with image $\mathbb C\setminus[0,1]$. (b) The
$t,u$ closures are the transpositions of $S_3\subset PSL(2,\mathbb Z)$ acting on the cross-ratio
plane: $z\mapsto z/(z-1)$ (fixes $0,2$, swaps $1\leftrightarrow\infty$) and $z\mapsto1/(1-z)$
(order 3 element, $\infty\to0\to1\to\infty$). So the three channel families are one family
moved around by the anharmonic group.

**Feynman regions and the interior, defined internally.**
$$
\mathcal F'_\alpha:=\{Z_4^{(\alpha)}(q):|q|\le1\},\qquad
\mathcal M'_\times:=\mathcal M_{0,4}\setminus\bigcup_{\alpha=s,t,u}\mathcal F'_\alpha,
\qquad
R_\alpha(\sigma):=\{Z_4^{(\alpha)}(e^{\sigma'+i\theta}):0<\sigma'\le\sigma(\theta)\}.
\tag{1.4}
$$
No external quartic vertex enters: $\mathcal M'_\times$ is whatever the twist-only gluing leaves.
Real-axis data at $\beta=3/2$ (from (1.2); note $Z_4^{(s)}(\pm1)=\pm\frac{(4\beta^2\pm1)^2}{16\beta^2}$,
i.e. $25/9$ and $-16/9$):
$\mathcal F'_s\cap\mathbb R=(-\infty,-16/9]\cup[25/9,\infty)$,
$\mathcal F'_t\cap\mathbb R=[16/25,\,25/16]$, $\mathcal F'_u\cap\mathbb R=[-9/16,\,9/25]$. The three
are disjoint (checked numerically on a grid, §3), so $\mathcal M'_\times$ is non-empty and
bounded; it is the region between them containing the points $e^{\pm i\pi/3}$.

**Physical-grading counts inherited from 030 §6.2** (not re-derived): $N_{\rm gh}(\Phi)=2$;
$\gamma(\mathcal V_3')=-1$ as $\mathcal H_0^{\otimes2}\to\mathcal H_0$, $+4$ the other way;
$\gamma(\hat{\mathsf P})=-1$; exchange $\mathcal V_3'\circ\hat{\mathsf P}\circ\mathcal V_3'$ has
$\gamma=+2=\gamma(m_2)$, moduli $2=\dim_\mathbb R\mathcal M_{0,4}$, sphere topology.
Count (i) of 030: a $\theta$-dependent $\sigma(\theta)$ forces $\Phi\in\mathcal H$ (level-mismatched
components); $\sigma$ constant $\Leftrightarrow\Phi\in\mathcal H_0$. Both cases are mapped in §3.

**Parameter values used numerically.** $\beta=\beta'=3/2$ (Harold's figure), with the
$\mathcal V_3'$ slack parameters scanned: $\alpha'=0$ and $\gamma'\in\{\gamma'_{\rm sat},\,1.1\gamma'_{\rm sat},\,2\gamma'_{\rm sat}\}$
where $\gamma'_{\rm sat}=\frac{2\beta'+1}{2\beta'-1}=2$ is the saturated value; plus a seeded
sample of general $(\alpha',\gamma')$ in the allowed cone.

## §2 Precondition (first falsifier)

**Setup.** (α-rev) glues two $\mathcal V_3'$ on their special legs by $w_1w_2=q$. For $|q|<1$
the annuli $|q|<|w_i|<1$ inside the two coordinate discs are identified (standard plumbing);
at $|q|=1$ the discs are glued along their boundary circles; for $|q|=e^{\sigma}>1$ the
identified annuli are $1<|w_i|<e^{\sigma}$, which lie *outside* the unit coordinate discs. The
composite is a legitimate sewn surface only if the coordinate $w$ of the special leg extends
to $|w|\le e^{\sigma}$ as an embedded disc — **cut convention (H1):** this is the *one-sided* cut
(sphere 1 cut at $|w_1|=1$, sphere 2 at $|w_2|=e^\sigma$); the plumbed surface is the same for any
cut $|w_1|=\rho$, $|w_2|=e^\sigma/\rho$, and the *symmetric* cut $\rho=e^{\sigma/2}$ needs each disc
extended only to $e^{\sigma/2}$, so the necessary-and-sufficient sewability bound is $\sigma\le2\sigma_{\max}$
with $\sigma_{\max}$ as in (2.4). Both are quoted below ($\gamma'\ge9.19$ one-sided, $\ge3.15$
symmetric for the $S_3$ seam); the record does not choose, since $\hat{\mathsf P}$ acts on one leg
but the surface state is cut-independent — the choice belongs to the paper — disjoint from the other two coordinate discs of the
same $\mathcal V_3'$ — otherwise the identified region overlaps the punctures' discs. Two
versions of the test, both computed (script part 1):

- **(P-strict)** on the vertex sphere: $f_1'(\{|w|\le r\})\cap f_0'(D)=\emptyset$ and
  $\cap f_\infty'(D)=\emptyset$; $\sigma_{\max}:=\ln r_{\max}$.
- **(P-comp)** on the $s$-channel composite at $q=e^{\sigma+i\theta}$: the four coordinate
  discs $F_1(D)=f_0'(D)$, $F_2(D)=f_\infty'(D)$, $F_{3,4}(D)=T_q(f_{0,\infty}'(D))$ with
  $T_q(z')=f_1'\big(q/f_1'^{-1}(z')\big)$ pairwise disjoint; $\sigma_{\rm comp}(\theta)$ the
  largest such $\sigma$. (P-comp) is weaker than (P-strict): it only asks that the
  *transported* discs of sphere 2 avoid those of sphere 1, not that the identified annulus be
  embedded. It is the four-point cross-ratio sweep's own consistency condition; (P-strict) is
  what five-point sewability needs (030 §5.4).

**Derivation.**
$$
\begin{aligned}
&\text{(2.1)}\quad f_1'(\{|w|\le r\})=\Big\{\,|z-c_1(r)|\le\rho_1(r)\Big\},\quad
c_1(r)=\frac{4\beta'^2+r^2}{4\beta'^2-r^2},\ \ \rho_1(r)=\frac{4\beta' r}{4\beta'^2-r^2}\quad(r<2\beta');\\
&\text{(2.2)}\quad f_0'(D)=\{|z-c_0|\le\rho_0\},\ \ c_0=-\tfrac{\alpha'}{\gamma'^2-\alpha'^2},\ \rho_0=\tfrac{\gamma'}{\gamma'^2-\alpha'^2};
\qquad f_\infty'(D)=\{|z-\alpha'|\ge\gamma'\};\\
&\text{(2.3)}\quad \text{(P-strict)}\iff |c_1(r)-c_0|\ge\rho_1(r)+\rho_0\ \ \text{and}\ \ |c_1(r)-\alpha'|+\rho_1(r)\le\gamma';\\
&\text{(2.4)}\quad \alpha'=0:\ \ \frac{2\beta'-r}{2\beta'+r}\ge\frac1{\gamma'}\iff r\le r_{\max}=\frac{2\beta'(\gamma'-1)}{\gamma'+1},
\qquad \boxed{\ \sigma_{\max}=\ln\frac{2\beta'(\gamma'-1)}{\gamma'+1}\ }\ ;\\
&\text{(2.5)}\quad \sigma_{\max}>0\iff\gamma'>\gamma'_{\rm sat}:=\frac{2\beta'+1}{2\beta'-1};\qquad
\sigma_{\max}=0\ \text{at the saturated (tangent) vertex}.
\end{aligned}
$$

**Commentary.** (2.1)–(2.2): images of $|w|=r$ under real Möbius maps are circles symmetric
about the real axis, fixed by the images of $w=\pm r$; the side is fixed by the image of the
puncture ($f_\infty'(0)=\infty$ gives the exterior). (2.3): the two conditions coincide under
$z\to1/z$ (P1d); the leftmost point of $f_1'(D_r)$ is $(2\beta'-r)/(2\beta'+r)$ and the rightmost
point of $f_0'(D)$ at $\alpha'=0$ is $1/\gamma'$, giving (2.4). (2.5) is the second
non-overlap condition at $A=1$ ($\alpha'=0$) with equality, so $\sigma_{\max}=0$ exactly when
his inequality is saturated ($B=0$), and the slack parameter $B>0$ buys room:
$\sigma_{\max}=\ln\frac{2\beta'(\gamma'-1)}{\gamma'+1}$ grows to $\ln 2\beta'$ as $\gamma'\to\infty$
(the pole of $f_1'$ at $w=-2\beta'$ is the absolute ceiling, $r<2\beta'$). For $\beta'=3/2$:
$\gamma'_{\rm sat}=2$, $\sigma_{\max}(\gamma'=2.2)=0.1178$, $\sigma_{\max}(\gamma'=4)=0.5878$,
ceiling $\ln3=1.0986$.

**Results (script part 1, $\beta'=3/2$, all PASS, 13 checks incl. one break leg).**

| vertex ($\alpha'=0$) | $\sigma_{\max}$ (P-strict) | $\sigma_{\rm comp}(\theta)$ range over $36$ twists | remark |
|---|---|---|---|
| $\gamma'=\gamma'_{\rm sat}=2$ (tangent, SZ-type) | **0** | $[0,\,1.017]$; $=0$ at $\theta=0$, max at $\theta=\pi/2$ | no room for a sewable extension |
| $\gamma'=2.2$ | $0.1178$ | $[0.235,\,1.422]$ | (P-comp) $\ge$ (P-strict) everywhere |
| $\gamma'=4$ | $0.5878$ | $[1.172,\,\ge3]$ (capped at the scan range) | idem |
| 174 seeded $(\alpha',\gamma')$ in the allowed cone | $[0.099,\,0.905]$ | — | analytic (2.3) $\equiv$ numeric bisection (P1c) |

**Reading.** (a) For the SZ-type (tangent) vertex the precondition fails at once:
$\sigma_{\max}=0$, so any $|q|>1$ continuation has no sewable meaning, exactly as 030 §5.4
anticipated. (b) Harold's $\mathcal V_3'$ has two free parameters that do not affect the
puncture positions (R2), and the precondition is a condition on *them*: with slack ($B>0$)
$\sigma_{\max}>0$, bounded above by $\ln 2\beta'$ — a constant, $\theta$-independent bound, as
$\Phi\in\mathcal H_0$ requires. (c) Whether $\sigma_{\max}$ is *large enough* is the question
of §3: the interior $\mathcal M'_\times$ is reached only up to a $\sigma$ that §3 computes,
and (2.4) must exceed it. (d) The weaker (P-comp) bound is $\theta$-dependent even at the
tangent vertex; it is the bound that a naive four-point sweep would report and it is not the
right one for sewability — recorded to prevent that misreading in 14b/14c.

**Aside (not acted on).** The composite was rebuilt directly from the gluing: $z_3=\frac{4\beta'^2-q}{4\beta'^2+q}$,
$z_4=1/z_3$, and the cross-ratio $Z_4=1/(1-z_3^2)=\frac{(q+4\beta'^2)^2}{16\beta'^2q}$ reproduces R2
($\cosh^2\ln2\beta=\frac{(4\beta^2+1)^2}{16\beta^2}$).

## §3 The covering map (6.1)

**Method (script part 2).** Euclidean area on the cross-ratio plane, grid step $h=0.004$ on
$[-3,4]\times[-3,3]$ ($1750\times1500$ points; $\mathcal M'_\times$ is bounded and does not touch
the box, C2b2). Each grid point $z$ is pulled back to the three channel parameters
$q_\alpha(z)$: $z_s=z$, $z_s=z/(z-1)$ ($t$), $z_s=1-1/z$ ($u$), then
$$
q(z_s)=\text{root of } q^2+(8\beta^2-16\beta^2z_s)\,q+16\beta^4=0\ \text{ with }|q|<4\beta^2
\tag{3.1}
$$
(the other root is $16\beta^4/q$; (1.3a) makes this branch the unique preimage in the
injectivity disc; C2a). Then $z\in\mathcal F'_\alpha\iff|q_\alpha|\le1$,
$z\in R_\alpha(\sigma)\iff1<|q_\alpha|\le e^{\sigma(\arg q_\alpha)}$, and
$\mathcal M'_\times=\{\min_\alpha|q_\alpha|>1\}$. Gap $=|\mathcal M'_\times\setminus\bigcup R_\alpha|$,
overlap $=\sum_\alpha|R_\alpha|-|\bigcup_\alpha R_\alpha|$, spill $=\sum_\alpha|R_\alpha\cap\bigcup_\beta\mathcal F'_\beta|$.
$\beta=3/2$ throughout; $|\mathcal M'_\times|=14.534$.

**(3.2) Constant $\sigma$ (the $\Phi\in\mathcal H_0$ case).** Two thresholds, read off the grid:
$$
\sigma^*=\ln\max_{z\in\mathcal M'_\times}\min_\alpha|q_\alpha(z)|=0.8793\ (|q|=2.409),\qquad
\sigma_{\rm ov}=\ln\min_{z\in\mathcal M'_\times}\big(\text{2nd smallest }|q_\alpha(z)|\big)=0.4345\ (|q|=1.544).
$$
The gap closes at $\sigma^*$ (last point covered: $z=\tfrac12+0.864i\approx e^{i\pi/3}$, the
$S_3$-fixed point, as symmetry dictates); overlap begins at $\sigma_{\rm ov}<\sigma^*$. Hence
**no constant $\sigma$ covers $\mathcal M'_\times$ once without overlap** (C2c) — the
over-determination anticipated in S5, now quantified:

| constant $\sigma$ | $|R_s|$ | $|R_t|$ | $|R_u|$ | gap | overlap | spill into $\mathcal F'$ |
|---|---|---|---|---|---|---|
| $\sigma_{\rm ov}=0.4345$ | 9.239 | 1.181 | 1.181 | 2.934 (20 %) | 0.000 | 0 |
| $\sigma^*=0.8793$ | 13.176 | 5.580 | 5.580 | 0.000 | 8.996 (62 %) | 0.806 |
| $\sigma_{\max}(\gamma'=2.2)=0.1178$ | 3.339 | 0.204 | 0.204 | 10.786 (74 %) | 0 | 0 |
| $\sigma_{\max}(\gamma'=4)=0.5878$ | 11.002 | 2.066 | 2.066 | 1.014 (7 %) | 1.614 | 0 |
| ceiling $\ln2\beta'=1.0986$ | 14.158 | 12.348 | 12.348 | 0.000 | 13.632 | 10.689 |

(the $s$ region is larger because $\mathcal F'_s$ is the neighbourhood of $\infty$ and the
Euclidean measure is not $S_3$-invariant; $|R_t|=|R_u|$ by the $z\to1-z$ symmetry).

**(3.3) $\theta$-dependent $\sigma(\theta)$ (the $\Phi\in\mathcal H$ case) — a covering exists.**
Within one channel the map $q\mapsto Z_4^{(s)}$ is injective on $|q|<4\beta^2$ (1.3a), so for
*any* single-valued $\sigma(\theta)$ the region $R_s$ is covered once; the only content of
"once, without overlap" is the choice of a partition of $\mathcal M'_\times$ into three pieces
adjacent to $\mathcal F'_s,\mathcal F'_t,\mathcal F'_u$ whose seams are graphs $\sigma=\sigma(\theta)$
in the log-polar $q$-plane of each channel (a "star-shapedness" condition). The natural candidate
is the $S_3$-symmetric partition by the fixed lines of the three transpositions of the anharmonic
group: $D_s=\{|z|>1,|z-1|>1\}$, $D_t=\{|z-1|<1,\ \Re z>\tfrac12\}$, $D_u=\{|z|<1,\ \Re z<\tfrac12\}$
(seams $|z|=1$, $|z-1|=1$, $\Re z=\tfrac12$, meeting at $e^{\pm i\pi/3}$). Because the closures
(1.2) *are* the $S_3$ maps and commute with $q$, one function $\sigma(\theta)$ serves all three
channels. Computed by ray-marching $Z_4^{(s)}(e^{\sigma+i\theta})$ to its first exit from $D_s$
(721 twists, 4000 radial steps):

- $\mathcal F'_s\subset D_s$ (C2e) and the preimage of $D_s$ is star-shaped in $q$: no ray
  re-enters $D_s$ after leaving it (C2e2). So $\sigma(\theta)$ is single-valued.
- $\sigma(\theta)\in[0.4341,\ 0.8802]$, minimum at $\theta=\pi$ (real axis, $z<0$ side, where the seam
  $|z|=1$ is closest to $\partial\mathcal F'_s$), maximum at $\theta=\pm\pi/2$ (toward the
  corners $e^{\pm i\pi/3}$); $\pi$-periodic in $\theta$ (C2g3, from $1-Z_4^{(s)}(q)=Z_4^{(s)}(-q)$, C2g2).
  The two constant thresholds of (3.2) are exactly $\min\sigma(\theta)$ and $\max\sigma(\theta)$.
- Coverage with this $\sigma(\theta)$: $|R_s|=10.845$, $|R_t|=|R_u|=1.838$, **gap $0.0133$ (0.09 % of
  $|\mathcal M'_\times|$, seam-discretisation noise), overlap $3\times10^{-5}$, spill 0** (C2f).
  Break leg: replacing the $u$-closure by its inverse $1/(1-z)$ moves $R_u$ on top of $R_t$:
  gap $1.851$, overlap $1.838$ (C2h fails as required).

Equation count (S5's question): for each channel, the seam is one real curve in a 2-real-dimensional
$q$-annulus, i.e. one real function $\sigma_\alpha(\theta)$ — three unknown functions; the
constraints are that the three image curves $Z_4^{(\alpha)}(e^{\sigma_\alpha(\theta)+i\theta})$
pairwise coincide along common arcs and meet at two triple points. Any partition of
$\mathcal M'_\times$ with star-shaped preimages solves it, so the problem is
**under-determined** for $\sigma(\theta)$ (a continuum of partitions; the $S_3$-symmetric one is the
canonical choice) and **over-determined** for constant $\sigma$ (one number, two thresholds that
disagree).

**(3.4) Against the precondition of §2.** $\max_\theta\sigma(\theta)=0.8802<\ln2\beta'=1.0986$: the
$S_3$ seam lies *below* the absolute ceiling of the special-leg coordinate. With $\alpha'=0$,
(2.4) gives $\sigma_{\max}\ge0.8802\iff\gamma'\ge9.19$ for the one-sided cut ($\gamma'\ge9.15$ for $\sigma^*$); for the symmetric cut ($2\sigma_{\max}\ge0.8802$, H1) $\gamma'\ge3.15$. A
$\mathcal V_3'$ with that much slack ($B\approx3.6$ in Harold's notation, $\gamma'\approx4.6\,\gamma'_{\rm sat}$)
satisfies (P-strict) for every twist while the puncture positions, hence $\mathcal F'_\alpha$ and
$\mathcal M'_\times$, are unchanged (R2: independent of $\alpha',\gamma'$). The tangent vertex
($\gamma'=\gamma'_{\rm sat}$) covers nothing; a mildly slack one ($\gamma'=4$) covers 93 %.

## Working notes (hand-off to 14b)

1. **What 14a settles.** The geometric side of (α-rev) is not obstructed at the covering level:
   the $\mathcal V_3'$ family continued to $|q|=e^{\sigma(\theta)}$ with the $S_3$-symmetric seam
   covers $\mathcal M'_\times$ once without overlap, and the required $\sigma(\theta)\le0.880<\ln2\beta'$
   is compatible with an embedded extension of the special-leg coordinate for a slack vertex
   ($\gamma'\ge9.19$ one-sided / $3.15$ symmetric cut, $\alpha'=0$, $\beta'=3/2$). A constant $\sigma$ (auxiliary in $\mathcal H_0$)
   does not work: this is the one clean "no" of 14a.
2. **Price already visible.** (a) $\sigma(\theta)$ non-constant $\Rightarrow$ $\Phi\in\mathcal H$
   with level-mismatched components and the twist projector replaced by
   $\int d\theta\,e^{i\theta L_0^-}(e^{\sigma(\theta)L_0^+}-1)/L_0^+$ (030 count (i)); 14b must use
   this operator, not $\delta_{L_0^-,0}$. Since $\sigma(\theta)$ is $\pi$-periodic, only even
   $L_0^-$ components are sourced. (b) The seam is a choice; nothing in the vertex data selects
   it (under-determination) — a legitimate gauge-like freedom or an ambiguity, to be judged in 14c.
3. **Local coordinates for (6.2).** On $R_\alpha$ the composite coordinates are the transported
   maps of §2: $F_1=f_0'$, $F_2=f_\infty'$, $F_{3,4}=T_q\circ f'_{0,\infty}$ with
   $T_q(z')=f_1'(q/f_1'^{-1}(z'))$ at $|q|>1$ (rebuilt from the gluing, see §2 aside). These
   are *not* continuous across the seams (the $s$- and $t$-side coordinates at a seam point come
   from different gluings), exactly the first question of the 4-point summary note; (6.2) on shell is insensitive to
   this, off shell it is the obstruction to watch.
4. **Tautology guard (030 §4.1).** $\hat{\mathsf P}_{[-\sigma(\theta),0]}$ is now fixed by
   14a's seam before $V_4$ is looked at; 14b compares $\sum_\alpha\omega_1(\mathcal V_3'(\Psi,\Psi),\hat{\mathsf P}\mathcal V_3'(\Psi,\Psi))$
   with $\int_{\mathcal M'_\times}\Omega_{V_4}$ using the SZ measure with the coordinates of item 3;
   the comparison can fail (wrong measure normalisation, $S_4$ condition on the special leg).
5. **Not done here.** Sewability of the extended composite in five-point Feynman regions
   ((P-strict) is necessary, not shown sufficient); the $\beta$-dependence (only $\beta=3/2$
   scanned; $\sigma^*,\sigma(\theta)$ scale with $\beta$ and so does the ceiling $\ln2\beta'$);
   Fubini–Study areas (Euclidean used, stated); whether a $\theta$-independent seam exists for a
   *different* partition — ruled out by the two constant thresholds, which are partition-independent.

6. **Hand-off to 14c (from 14b).** *Verdict inputs:* (6.1) holds with a $\theta$-dependent seam
   (14a); (6.2) holds on shell to the covering accuracy and reduces to (6.1) + the pull-back
   identity (4.5) under the convergence hypothesis (P) — (m) argued (not tested by the on-shell
   check, which pulls back the same integrand), moot-on-shell (c),(s), and (l) harmless for the identity.
   *What the vertex buys regardless:* the $\mathcal V_3'$ family with a slack special leg
   ($\gamma'\ge9.19$ / $3.15$ by cut) gives a sewable, $S_4$-covariant piecewise coordinate system on
   $\mathcal M'_\times$ with the correct measure — i.e. a candidate $V_4$ *region* with
   coordinates, à la Erbin–Fırat, at no extra vertex data. *What remains open (14c):* (α) the
   seams: the transported coordinates jump across $\partial R_\alpha\cap\partial R_\beta$, so the
   BRST boundary terms (4.8) of adjacent channels are not equal off shell — gauge invariance of
   the single-strand action is the question, and the answer decides between "cubic theory with
   geometric auxiliary" and "an on-shell-only coincidence"; possible cures to assess: a
   $\theta$-dependent interpolation of the coordinates near the seams (costs a genuine $V_4$
   correction on a collar), or choosing the seam where the $s$- and $t$-composites' coordinates
   coincide (over-determined — likely impossible, to be checked as an equation count, cf. §3.3).
   (β) The seam is under-determined (any star-shaped partition) — either a gauge-like freedom
   (if the off-shell theories for different seams are related by a field redefinition of $\Phi$)
   or an ambiguity. (γ) The kinetic operator on $\mathcal H^{\rm even}$: $\hat{\mathsf P}$ has a
   kernel on odd $L_0^-$, so $\Phi$ must be restricted to the even sector; state this as a
   constraint replacing $b_0^-\Phi=L_0^-\Phi=0$. (δ) Not checked here: five-point sewability
   of the composite (item 5), $\beta\neq3/2$. *Ledger proposal:* one row — "the reversed-range
   single-strand exchange reproduces $\int_{\mathcal M'_\times}\Omega_{V_4}$ on shell iff the
   seam covers $\mathcal M'_\times$ (6.1); off shell the seam coordinate discontinuity is the
   open obstruction" — status *computed/self-checked*, conditional on the standard sewing
   identity (4.5) not machine-checked at CFT level.

## §4 The operator identity (6.2) — 14b

**Literal task (14b).** With the propagator $\hat{\mathsf P}_{[-\sigma(\theta),0]}$ fixed by the
$S_3$ seam of §3.3 (tautology guard: fixed *before* $V_4$ is looked at), decide whether the
exchange sum $\sum_\alpha\omega_1(\mathcal V_3'(\Psi,\Psi),\hat{\mathsf P}\,\mathcal V_3'(\Psi,\Psi))$
equals $\int_{\mathcal M'_\times}\Omega_{V_4}$ on shell (four tachyons, generic momenta), 030 (6.2).
**Objective.** (6.1) is necessary, not sufficient: (6.2) can fail through (m) the measure
normalisation / $\sigma(\theta)$ Jacobian, (c) the coordinate discontinuity across the seams,
(s) the $S_4$ condition on the special leg, (l) the level-mismatched components of $\Phi$.
Both outcomes are reported.

### 4.1 The two sides written out

**Propagator (14a's seam, twist projector replaced; 030 count (i)).** With $q=e^{-s+i\theta}$ and
the reversed range $s\in[-\sigma(\theta),0]$,
$$
\hat{\mathsf P}_{[-\sigma(\theta),0]}
=\int_0^{2\pi}\frac{d\theta}{2\pi}\int_{-\sigma(\theta)}^{0}ds\;
b_0^+b_0^-\,e^{-sL_0^+}e^{i\theta L_0^-}
=b_0^+b_0^-\int_0^{2\pi}\frac{d\theta}{2\pi}\,e^{i\theta L_0^-}\,\frac{e^{\sigma(\theta)L_0^+}-1}{L_0^+},
\tag{4.1}
$$
an operator on $\mathcal H$ (not $\mathcal H_0$: for non-constant $\sigma$ the $\theta$-integral is
not $\delta_{L_0^-,0}$). Since $\sigma(\theta+\pi)=\sigma(\theta)$ (C2g3), (4.1) annihilates the
odd-$L_0^-$ components: $\hat{\mathsf P}$ acts on $\mathcal H^{\rm even}=\{L_0^-\in2\mathbb Z\}$
only — item (l), see 4.4.

**LHS, one channel.** Both $\mathcal V_3'$ are the surface states of §1 with the special leg
$f_1'$ sewn by $f_1'^{-1}(z)\,f_1'^{-1}(z')=q$ (plumbing in the special-leg coordinates). By
the sewing theorem (sum over a complete set of intermediate states of $\mathcal H$ equals the
plumbing of the two surfaces; Erbin 2021 §"plumbing fixture", Zwiebach 1993 §3–4), the
state-space expression is a worldsheet integral:
$$
\omega_1\!\big(\mathcal V_3'(\Psi,\Psi),\hat{\mathsf P}\,\mathcal V_3'(\Psi,\Psi)\big)
=\int_0^{2\pi}\frac{d\theta}{2\pi}\int_{-\sigma(\theta)}^{0}ds\;
\Big\langle b(\partial_s)\,b(\partial_\theta)\ \prod_{i=1}^4 F_i\circ\Psi\Big\rangle_{\Sigma_q},
\tag{4.2}
$$
where $\Sigma_q$ is the sphere with punctures at $0,\infty,1,Z_4^{(s)}(q)$ (1.2), the local
coordinates are the transported ones of Working notes item 3 ($F_1=f_0'$, $F_2=f_\infty'$,
$F_{3,4}=T_q\circ f'_{0,\infty}$), and $b(\partial_s)=b_0^++\bar b_0^+$-type, $b(\partial_\theta)$ the
antighost insertions for the Schiffer vectors of the plumbing family — on the sewing circle they
are exactly $b_0^+$ and $b_0^-$ of (4.1), independent of whether $|q|<1$ or $|q|>1$. In (4.2)
the operator $b_0^+b_0^-$ of (4.1) has been moved onto the surface; the $1/2\pi$ is the standard
propagator normalisation, the same one that makes the $|q|\le1$ Feynman regions
$\mathcal F'_\alpha$ reproduce the amplitude there.

**RHS.** $\Omega_{V_4}$ is the Sonoda–Zwiebach canonical 2-form on $\mathcal M_{0,4}$ for the
local-coordinate data $\{F_i\}$: at the point $Z$, with $\Sigma_Z$ the sphere punctured at
$0,\infty,1,Z$,
$$
\int_{\mathcal M'_\times}\Omega_{V_4}
=\int_{\mathcal M'_\times} d^2Z\;
\Big\langle b(\partial_Z)\,b(\partial_{\bar Z})\ \prod_{i=1}^4 F_i\circ\Psi\Big\rangle_{\Sigma_Z},
\qquad
b(\partial_Z)=\oint_{C_4}\frac{dw}{2\pi i}\,\frac{\partial F_4}{\partial Z}\!\Big/\!\frac{\partial F_4}{\partial w}\ b(w)+\dots,
\tag{4.3}
$$
where the coordinates $F_i(Z)$ on $\mathcal M'_\times$ are *defined* channel-wise:
on $R_\alpha$ (the $S_3$ partition of §3.3) they are the transported coordinates of the
$\alpha$-channel composite at the unique $q$ with $Z_4^{(\alpha)}(q)=Z$ (injectivity, 1.3a).
The brief's RHS is therefore not an independent vertex: it is the covering of §3 read as a
piecewise coordinate assignment. This is what the tautology guard (item 4) warns about, and
it fixes what (6.2) can and cannot test — stated in the table.

**Where the two sides can differ.**

| item | what it is | can it bite on shell? | where settled |
|---|---|---|---|
| (m) measure | (4.2) is $\int ds\,d\theta$ of the $(s,\theta)$-Beltrami integrand; (4.3) is $\int d^2Z$ of the $Z$-Beltrami integrand. Equal iff the sewing measure is the pull-back of the canonical measure along $q\mapsto Z_4^{(\alpha)}(q)$ *also for $|q|>1$*, with the right orientation and no boundary term from the $\theta$-dependent limit $\sigma(\theta)$. | yes (a Jacobian power or a sign would show up in the tachyon integral) | 4.2, script part 3 |
| (c) coordinates | $F_i$ jump across the seams $\partial R_\alpha\cap\partial R_\beta$ (item 3): the $s$-side and $t$-side composites give different discs at the same $Z$. | no: on shell the integrand of (4.3) is independent of the $F_i$ (weight-$(0,0)$ primaries, 4.3). Off shell: the RHS is only piecewise smooth; a vertex $V_4$ with these coordinates is not a smooth section — obstruction candidate for 14c | 4.3 (on shell); 14c |
| (s) $S_4$ | the three channels give $S_3$ on the $\Psi$ legs automatically; full $S_4$ needs the composite coordinates on $R_s$ to be symmetric under $(12)$, $(34)$, $(13)(24)$ | no on shell (integrand coordinate-free; $\mathcal M'_\times$ is $S_3$-invariant by (1.3b), (1.4)). Off shell: $(12)$ is $z\to1/z$ ($f_0'\leftrightarrow f_\infty'$, §1); $(13)(24)$ is the swap of the two vertices, a symmetry because both special legs carry the same $f_1'$ and the plumbing $w_1w_2=q$ is symmetric; so the piecewise $F_i$ *are* $S_4$-covariant, up to (c) at the seams | 4.4 |
| (l) levels | $\hat{\mathsf P}$ acts on $\mathcal H^{\rm even}\subset\mathcal H$, kills odd $L_0^-$; the intermediate-state sum in (4.2) runs over all of $\mathcal H$ | no for (6.2): (4.2) is an identity of the worldsheet integrand whatever the range in $\theta$. It bites for the *kinetic* term ($\hat{\mathsf P}^{-1}$ on $\mathcal H$ needs a complement of the odd sector) | 4.4, 14c |

So on shell, (6.2) reduces to two separable statements: **(A)** the local identity (m),
pointwise in $q$ on $|q|>1$, and **(B)** the covering (6.1) — because on shell both integrands
are the same coordinate-free function $f(Z)$ and (6.2) becomes
$\sum_\alpha\int_{R_\alpha}f\,d^2Z=\int_{\mathcal M'_\times}f\,d^2Z$, true iff the $R_\alpha$
tile $\mathcal M'_\times$ once. (B) is 14a's result (gap 0.09 %, overlap $3\times10^{-5}$); 4.2
does (A), 4.3 checks (A)+(B) together numerically on the tachyon integrand.

### 4.2 Measure: $b$-insertions and the Jacobian of $\sigma(\theta)$

**(4.4) Schiffer vectors of the plumbing family.** The sewing $w_1w_2=q$ in the special-leg
coordinates deforms under $q\to q+\delta q$ by the vector field $v=(\delta q/q)\,w\,\partial_w$ on
the sewing circle, whose antighost insertion is $\oint\frac{dw}{2\pi i}\,v(w)\,b(w)=(\delta q/q)\,b_0$
(and $(\delta\bar q/\bar q)\,\bar b_0$). With $q=e^{-s+i\theta}$,
$\partial_s=-(q\partial_q+\bar q\partial_{\bar q})$, $\partial_\theta=i(q\partial_q-\bar q\partial_{\bar q})$:
$$
b(\partial_s)=-(b_0+\bar b_0)=-b_0^+,\qquad b(\partial_\theta)=i(b_0-\bar b_0)=i\,b_0^-,\qquad
ds\,d\theta=\frac{d^2q}{|q|^2}\quad(d^2q:=d\,\Re q\,d\,\Im q).
\tag{4.4}
$$
These are algebraic identities in $q$; nothing in them refers to $|q|<1$. The insertion
$b(\partial_s)b(\partial_\theta)\,ds\,d\theta=-i\,b_0^+b_0^-\,ds\,d\theta$ is exactly the operator content of
(4.1) (the overall constant is the one fixed once and for all by the $|q|\le1$ Feynman regions,
so it drops out of a *ratio* statement; §4.3 compares ratios). Reversing the range $s\in[0,\infty)\to[-\sigma(\theta),0]$
changes neither the integrand nor the orientation: the domain
$\{(s,\theta):-\sigma(\theta)\le s\le0,\ 0\le\theta<2\pi\}$ carries the positive measure $ds\,d\theta$,
and its image $R_s$ under $q\mapsto Z_4^{(s)}(q)$ is positively oriented because the map is
holomorphic (orientation preserving) and injective there (1.3a). A sign flip $s\to-s$ would flip
$b(\partial_s)$ and $ds$ together — no net effect.

**(4.5) Pull-back to the cross-ratio plane.** $Z=Z_4^{(\alpha)}(q)$ is holomorphic; the Beltrami
insertion is linear in the deformation, so $b(\partial_q)=Z'(q)\,b(\partial_Z)$, $b(\partial_{\bar q})=\overline{Z'(q)}\,b(\partial_{\bar Z})$, and
$$
\big\langle b(\partial_s)b(\partial_\theta)\textstyle\prod F_i\circ\Psi\big\rangle_{\Sigma_q}\,ds\,d\theta
=\big\langle b(\partial_Z)b(\partial_{\bar Z})\textstyle\prod F_i\circ\Psi\big\rangle_{\Sigma_Z}\,|Z'(q)|^2\,\frac{d^2q}{|q|^2}
=\Omega_{V_4}\big|_{Z=Z_4^{(\alpha)}(q)},
\tag{4.5}
$$
i.e. the sewing measure is the pull-back of the canonical measure, *pointwise in $q$*, with the
local coordinates on $\Sigma_Z$ being those induced by the sewing — which is the definition of
the transported $F_i$ (item 3). The Jacobian between the $(s,\theta)$ and $Z$ parametrisations is
$$
J_\alpha(q)=\frac{d^2Z}{ds\,d\theta}=|q|^2\,\big|Z_4^{(\alpha)\prime}(q)\big|^2,\qquad
Z_4^{(s)\prime}(q)=\frac{(q+4\beta^2)(q-4\beta^2)}{16\beta^2q^2},\qquad
Z_4^{(t,u)\prime}=g_{t,u}'(Z_4^{(s)})\,Z_4^{(s)\prime},
\tag{4.6}
$$
with $g_t(z)=z/(z-1)$, $g_u(z)=1/(1-z)$ from (1.3b); $J_s$ vanishes only on $|q|=4\beta^2$
(the fold circle of (1.3a)), outside every $R_\alpha$ since $\sigma(\theta)\le0.880<\ln4\beta^2=2.197$.
Hence, summing channels,
$$
\text{LHS of (6.2)}=\sum_\alpha\int_{R_\alpha}\Omega_{V_4}^{(F^{(\alpha)})}
\tag{4.7}
$$
exactly (no approximation, on or off shell), where $\Omega^{(F^{(\alpha)})}$ carries the
$\alpha$-channel transported coordinates. Statement (A) of 4.1 is therefore **proven** by the
standard argument; the reversal $|q|>1$ enters only through the precondition that the
transported discs exist and are embedded (§2, (P-strict)), which the correlator in (4.5) needs
for the $F_i$ to be defined at all on $|w|\le1$.

**(4.8) What the $\theta$-dependent boundary does and does not do.** In (4.7) the bound
$\sigma(\theta)$ only shapes the domain; a 2-form integrated over a region with piecewise-smooth
boundary produces no boundary term, so no "$b(\partial_\theta)$ at the seam" appears in (6.2).
The seam becomes visible in the BRST variation of the propagator — the object that governs
gauge invariance (14c), not (6.2). With $\{Q_B,b_0^\pm\}=L_0^\pm$ and an integration by parts in
$\theta$ ($L_0^-e^{i\theta L_0^-}=-i\partial_\theta e^{i\theta L_0^-}$):
$$
\{Q_B,\hat{\mathsf P}\}
=\int_0^{2\pi}\frac{d\theta}{2\pi}\,e^{i\theta L_0^-}\Big[\,b_0^-\big(e^{\sigma(\theta)L_0^+}-1\big)
-i\,\sigma'(\theta)\,b_0^+\,e^{\sigma(\theta)L_0^+}\Big]
=\underbrace{-\!\int\!\tfrac{d\theta}{2\pi}e^{i\theta L_0^-}b_0^-}_{|q|=1:\ \partial\mathcal F'_\alpha}
+\underbrace{\int\!\tfrac{d\theta}{2\pi}\,e^{i\theta L_0^-}e^{\sigma(\theta)L_0^+}\big(b_0^--i\sigma'(\theta)b_0^+\big)}_{|q|=e^{\sigma(\theta)}:\ \text{seam}} .
\tag{4.8}
$$
The seam term is the antighost of the *tangent* to the boundary curve
$(s,\theta)=(-\sigma(\theta),\theta)$, direction $(-\sigma'(\theta),1)$, as it must be: the
boundary of a Feynman region contributes $\oint b(\text{tangent})$. For constant $\sigma$ the
$b_0^+$ piece drops and one recovers the familiar $b_0^-\,e^{\sigma L_0^+}$ at a round boundary.
Gauge invariance of the single-strand theory requires the seam terms of adjacent channels to
cancel along $\partial R_\alpha\cap\partial R_\beta$; there the two channels carry *different*
transported coordinates (item (c)), so the cancellation is not automatic off shell — recorded
for 14c in Working notes, not decided here.

**Dimensional check.** All quantities are dimensionless cross-ratios and Schwinger parameters
($\alpha'$ enters only through the on-shell exponents of 4.3); void, as in §3.

### 4.3 On-shell evaluation: four tachyons at generic momenta

**(4.9) Reduction.** For weight-$(0,0)$ primaries (on-shell tachyons, $\alpha'k_i^2=4$) the
correlator in (4.3) is independent of the local coordinates $F_i$ — the conformal factors
$|F_i'(0)|^{2h_i}$ are $1$ — so the integrand is the coordinate-free Koba–Nielsen function on
$\mathcal M_{0,4}$ with punctures at $0,\infty,1,Z$:
$$
\Omega_{V_4}\big|_{\rm on\ shell}=\mathcal N\,f(Z)\,d^2Z,\qquad
f(Z)=|Z|^{2a}|1-Z|^{2b},\qquad a=\tfrac{\alpha'}{2}k_1\!\cdot\!k_4,\ b=\tfrac{\alpha'}{2}k_3\!\cdot\!k_4
\tag{4.9}
$$
(the $b$-ghost and $c$-ghost factors combine into the constant $\mathcal N$, the same on both
sides since (4.5) is exact; the labels of the punctures fixed at $0,1,\infty$ follow 023 §1 /
R29's convention, immaterial here because $\mathcal M'_\times$ is $S_3$-invariant and the same
$f$ is used on both sides). The item-(c) discontinuity of the $F_i$ at the seams is invisible in
(4.9): this is the precise sense in which (6.2) *on shell* cannot see the coordinates. Because
$\mathcal M'_\times$ is compact and bounded away from $0,1,\infty$ (C2b, C2b2), $f$ is smooth and
bounded on it for every $(a,b)$, and "generic momenta" means generic exponents $(a,b)$; two seeded
points are used, $(0.460,-1.431)$ and $(-1.332,-0.910)$.

**(4.10) The two sides, computed independently (script part 3).**
$$
\text{LHS}=\sum_{\alpha}\int_{-\pi}^{\pi}d\theta\int_0^{\sigma(\theta)}ds'\;
f\big(Z_4^{(\alpha)}(e^{s'+i\theta})\big)\,J_\alpha(e^{s'+i\theta}),\qquad
\text{RHS}=\int_{\mathcal M'_\times}f\,d^2Z,
\tag{4.10}
$$
LHS by midpoint quadrature in $(s',\theta)$ ($1440\times400$ per channel, seam $\sigma(\theta)$ of
§3.3 interpolated) with the Jacobian (4.6); RHS by the Part-2 grid ($h=0.004$) over the mask
$\mathcal M'_\times$; the closed-form $Z_4^{(s)\prime}$ and the closure Jacobians $g'_{t,u}$ are
checked against finite differences first (C3a, C3a2, C3a3).

| | point 1 $(a,b)=(0.460,-1.431)$ | point 2 $(a,b)=(-1.332,-0.910)$ |
|---|---|---|
| LHS $s/t/u$ | $4.8048\ /\ 6.6989\ /\ 0.9630$ | $1.1568\ /\ 3.9574\ /\ 5.6711$ |
| grid $\int_{R_\alpha}f$, $s/t/u$ | $4.8047\ /\ 6.6931\ /\ 0.9555$ | $1.1567\ /\ 3.9301\ /\ 5.6453$ |
| LHS total | $12.4667$ | $10.7853$ |
| RHS $\int_{\mathcal M'_\times}f$ | $12.4754$ | $10.7953$ |
| $({\rm LHS}-{\rm RHS})/{\rm RHS}$ | $-7.0\times10^{-4}$ | $-9.2\times10^{-4}$ |
| grid error of RHS ($h$ vs $2h$) | $3.2\times10^{-4}$ | $6.7\times10^{-4}$ |

**Reading.** (i) Per channel, the $(s',\theta)$ quadrature with the Jacobian (4.6) reproduces the
grid integral over the *same* region $R_\alpha$ to $\lesssim0.8\,\%$ (C3b; the $t,u$ pieces are
small regions, $|R_{t,u}|=1.84$, so the grid's boundary error is relatively larger there) —
this is the measure identity (A) tested on the tachyon integrand: the Jacobian
$|q|^2|Z'|^2$ is right, no extra factor. (ii) The channel sum equals the $\mathcal M'_\times$
integral to $-0.07\,\%$ and $-0.09\,\%$, LHS *below* RHS by exactly the covering-gap fraction
of §3.3 ($0.09\,\%$, C3c, C3c-b): the residual is the seam-discretisation gap of (6.1), not a
property of (6.2). (iii) Break legs: Jacobian power $|Z'|^1$ instead of $|Z'|^2$ gives
$+59\,\%$ (C3d-break); replacing the seam by the constant $\sigma_{\rm ov}$ (20 % gap) gives
$-23\,\%$ (C3e-break); both fail as required, so the comparison has teeth against the two
things it claims to test — the Jacobian and the covering. (iv) The seam has no odd Fourier
modes (C3f), confirming item (l): only even $L_0^-$ components are sourced by $\hat{\mathsf P}$.

**(4.11) Result.**
$$
\boxed{\ \sum_{\alpha=s,t,u}\omega_1\!\big(\mathcal V_3'(\Psi,\Psi),\hat{\mathsf P}_{[-\sigma(\theta),0]}\mathcal V_3'(\Psi,\Psi)\big)
=\int_{\mathcal M'_\times}\Omega_{V_4}\quad\text{on shell, to the accuracy of the covering (6.1)}\ }
$$
i.e. (6.2) holds on shell exactly when (6.1) holds; the reversed range $|q|>1$ introduces no
Jacobian, sign or boundary anomaly (4.2), and the on-shell integrand is blind to (c) and (s).

### 4.4 Verdict (ii)

**Verdict (ii), four-way vocabulary: holds on shell — conditionally on (6.1), which it inherits;
not a tautology, but not an independent test of the vertex either.** Precisely:

- *Proven (argument, standard):* the sewing measure of the $\mathcal V_3'\circ\hat{\mathsf P}\circ\mathcal V_3'$
  composite on the reversed range $|q|\in(1,e^{\sigma(\theta)}]$ is the pull-back of the canonical
  measure with the transported coordinates, pointwise in $q$ (4.5)–(4.7); the $\theta$-dependent
  bound shapes the domain only and produces no boundary term in (6.2) (4.8).
- *Computed, self-checked (script part 3, 13 checks, 2 break legs):* on shell, LHS $=$ RHS to
  $-7\times10^{-4}$ and $-9\times10^{-4}$ at two generic momentum points, the deficit being the
  $0.09\,\%$ covering gap of the discretised seam; wrong Jacobian power $\to+59\,\%$, constant
  $\sigma\to-23\,\%$.
- *Status of the four items:* **(m) argued, not tested** — no normalisation, Jacobian or orientation
  mismatch on $|q|>1$ *by the argument of 4.2, under the sewing-convergence hypothesis (P)*; the
  on-shell check C3a–c pulls back the same integrand on both sides and so tests (6.1) with the
  tachyon weight, not the measure identity (4.5) itself (critic 032 H3). **(c) not tested by (6.2) on shell** — on-shell integrands are
  coordinate-free; off shell the RHS is only piecewise defined, and the seam terms of (4.8) do
  not cancel between channels unless the transported coordinates agree at the seams, which
  they do not (item 3). This is the live obstruction, for 14c. **(s) settled off shell up to (c):**
  the piecewise $F_i$ are $S_4$-covariant ((12) is $z\to1/z$, (13)(24) is the vertex swap,
  (1.3b) permutes channels); on shell moot. **(l) settled for (6.2), open for the action:**
  $\hat{\mathsf P}$ acts on the even-$L_0^-$ sector of $\mathcal H$ only (C3f); harmless for the
  identity, but the kinetic operator $\hat{\mathsf P}^{-1}$ must be defined on a complement of the
  odd sector — a statement about the single-strand action, not about $V_4$.
- *Tautology guard:* respected ($\hat{\mathsf P}$ fixed by the seam before $f$ was integrated;
  the break legs show the comparison can fail). But the on-shell content of (6.2) is exactly (6.1)
  plus a standard measure identity: (6.2) on shell adds **no** constraint on $\mathcal V_3'$
  beyond the covering. The non-trivial content of the route lies off shell, in (c).

## Verification

Script `codes/verify-v3prime-route.py` (`.venv/bin/python`, numpy only, seed 20260914): **62/62
PASS**, seven break legs fail as required. **Part 1 (13):** closed-form $\sigma_{\max}$ (2.4) vs
bisection on the disc data at three $\gamma'$ (P1b); wrong closed form fails (P1b-break); tangency
inequality (2.3) vs numeric non-overlap on seeded $(\alpha',\gamma')$ (P1c); $z\to1/z$ symmetry
(P1d); composite discs disjoint at $|q|=1$ (P1e); composite bound $\ge$ strict bound (P1f). The
cut convention (H1) is not testable by these checks. **Part 2 (20):** inverse (3.1) (C2a);
$|q|=4\beta^2\mapsto[0,1]$ (C2a2); Feynman regions disjoint etc. (C2b); thresholds (C2c);
gap/overlap (C2d); star-shapedness (C2e); seam coverage (C2f); $\pi$-periodicity (C2g); wrong
closure fails (C2h-break). One grid only; $h$-scaling of the gap not tested. **Part 3 (13):**
Jacobians vs finite differences (C3a–a3); quadrature vs grid per channel (C3b — a change of
variables in the code, not the CFT measure identity); channel sum vs $\int_{\mathcal M'_\times}f$
(C3c, C3c-b); wrong Jacobian power and constant $\sigma$ fail (C3d, C3e-break); no odd Fourier
modes (C3f). **Part 4 (16, rewritten 14d):** positions (C4a); coordinates exactly Möbius (C4b);
first-order moduli agree on the $S_3$ seam, $|\Re m|<10^{-6}$ (C4c; observed $3\times10^{-14}$);
phase mismatch a common rotation (C4c2); perturbed $A_1$ disc breaks C4c (C4c-break); reflection
formula for the $t$-germs at first (C4g) and second order (C4g2, (5.4)); plain conjugation fails
(C4g-break); sphere-exchange symmetry of the $s$-germ moduli (C4h); second-order and disc-image
mismatch $>0.05$ on the seam (C4k, C4k2) and at $Z=2$ (C4f); self-comparison fails (C4k-break);
ray scan: first-order zero on the seam (C4d), non-vacuous (C4d2), full 12-component mismatch
bounded below by $2.18$ (C4d3). Not machine-checked: (4.5), (4.8), the value of (5.1′), the collar
condition; dimensional checks void (cross-ratios).

## §5 The seam question (α): equation count and cures — 14c

**Setting.** A seam point is $Z\in\partial R_s\cap\partial R_t$ (the arc $|Z-1|=1$, $\Re Z>\tfrac12$
of the $S_3$ partition, §3.3; the other two seams are its images under (1.3b)). At $Z$ the
$s$-composite ($q_s$, pairs $(12)|(34)$) and the $t$-composite ($q_t$, pairs $(13)|(24)$) are the
*same* four-punctured sphere — same $Z$, C4a — carrying two different systems of local
coordinates $F_i^{(s)}(w;Z)$, $F_i^{(t)}(w;Z)$, $i=1..4$ (Working notes item 3). Both are written in
the fixed frame $(0,1,\infty,Z)$, so no Möbius freedom is left to absorb a difference.

**(5a) Equation count for a sharp seam — first order, phases quotiented (14d, after critic 032 H4).**
*Unknowns:* the seam is a graph $\sigma=\sigma(\theta)$ in the log-polar $q_s$-plane — **one real
unknown per $\theta$**. *Equations:* for a sharp seam the first question of the 4-point summary note asks
$F_i^{(s)}(\,\cdot\,;Z)=F_i^{(t)}(\,\cdot\,;Z)$ as germs at $w=0$, $i=1..4$. Positions agree
(C4a, 0 conditions). A closed-string local coordinate is defined only up to a rotation
$w\mapsto e^{i\varphi_i}w$: the rotation acts on the state inserted at puncture $i$ by
$e^{i\varphi_iL_0^-}$, which is $1$ on $\mathcal H_0$ (the $L_0^-\Psi=0$ constraint exists
precisely so that the phase of the coordinate is immaterial; Zwiebach 1993 §2, Erbin 2021 ch. on
the $b_0^-,L_0^-$ constraints). The four external legs of the exchange diagram carry physical
$\Psi\in\mathcal H_0$, so the four phases $\arg F_i'(0)$ are **not conditions**. At first order
the conditions are the four moduli $|F_i^{(s)\prime}(0)|=|F_i^{(t)\prime}(0)|$: **4 real
conditions per $\theta$, count $4:1$** (the record's earlier $8:1$ counted the phases; withdrawn).

*Computed (script part 4, rewritten; $\gamma'=9.5$, $\alpha'=0$, $\beta'=3/2$).* Split the
log-ratio $m_i=\log\big(F_i^{(s)\prime}(0)/F_i^{(t)\prime}(0)\big)$ into $\Re m_i$ (moduli,
physical) and $\Im m_i$ (phases, gauge):
- on the $S_3$ seam ($|Z-1|=1$, $\Re Z>\tfrac12$, 25 points): $|\Re m_i|\le3\times10^{-14}$ for
  all $i$ and all points (C4c, threshold $10^{-6}$; germs exact — every $F_i$ is a composition of Möbius maps, C4b), while $\Im m_i\in[-2.67,2.67]$, **identical at
  the four punctures** at every sampled point (C4c2; e.g. $(-2.6704)^{\times4}$ at
  $Z=1+e^{-0.94i}$, $(\pm\pi)^{\times4}$ at $Z=2$ up to the branch cut of $\log$). The entire
  $|m|\in[5.34,6.28]$ of the previous version was a common rotation of the four coordinates.
- **All four first-order conditions are met on the $S_3$ seam.** Reason (critic's argument,
  verified here as C4g): on $|Z-1|=1$ one has $g_t(Z)=Z/(Z-1)=\bar Z$, so
  $\mathsf R:=g_t\circ{\rm conj}$ is the anti-holomorphic reflection across the seam circle,
  fixing it pointwise and swapping $1\leftrightarrow\infty$ (labels $2\leftrightarrow3$). The
  vertex maps have real coefficients, so the $s$-composite at $\bar q$ is the complex conjugate
  of the one at $q$; on the seam $q_t=\bar q_s$ and the $t$-composite is by construction
  $F_i^{(t)}=\mathsf R\circ F_{\pi(i)}^{(s)}\circ{\rm conj}$ with $\pi=(23)$ (the critic wrote
  $\pi={\rm id}$; since $\mathsf R$ swaps $1\leftrightarrow\infty$ the labels must be permuted). Hence
  $F_i^{(t)\prime}(0)=g'_i\,\overline{F_{\pi(i)}^{(s)\prime}(0)}$ where $g'_i$ is the derivative
  of $g_t$ in the charts at $\bar z_{\pi(i)}$: $g'=-1$ at $0$; $+1$ at $1$ (from the $1/z$ chart at
  $\infty$); $+1$ at $\infty$ (chart $1/z$, from $1$); $-1/(\bar Z-1)^2$ at $Z$ — all of unit
  modulus because $|\bar Z-1|=1$ on the seam. So $|F_i^{(t)\prime}(0)|=|F_{\pi(i)}^{(s)\prime}(0)|$,
  and the first-order conditions at punctures $2,3$ reduce to the $s$-composite's own symmetry
  $|F_2^{(s)\prime}(0)|=|F_3^{(s)\prime}(0)|$ (sphere exchange $w_1\leftrightarrow w_2$ combined
  with $f_1(-w)=1/f_1(w)$), which holds to $10^{-9}$ on the seam together with
  $|F_1^{(s)\prime}|=|F_4^{(s)\prime}|$ (C4h). C4g checks the closed-form reflection formula
  against the independently built $t$-germs at all 25 points; plain conjugation without $g_t$
  fails it (C4g-break).
- along the nine $s$-channel rays $\theta=$ const of §3 ($\sigma\in[0.2,1.2]$), $\min_\sigma|\Re m|$
  is $\le2.9\times10^{-3}$ on every ray (C4d; table in (5a′)), attained within $0.003$ of the
  $S_3$ seam circle (grid resolution $\Delta\sigma=0.005$); away from the seam $|\Re m|$ reaches
  $0.47$–$0.51$ on every ray (C4d2). The first-order conditions are therefore not vacuous: they
  *select* the $S_3$ seam, on which all four are met — a $4:1$ system with a solution, not an
  over-determined one (the four are dependent by the reflection symmetry).

The genuine question is therefore at **second order**: (5a′) below.

**(5a′) Second order and the disc image (the re-derivation).** Every transported coordinate is a
Möbius map (composition of $f_0,f_\infty,f_1,T,M,g_t$; C4b verifies the three-point fit to
$10^{-10}$ at a fourth point). A Möbius germ is fixed by $F(0)$, $c_1=F'(0)$, $c_2=F''(0)/2$;
under $w\mapsto e^{i\varphi}w$, $c_1\mapsto e^{i\varphi}c_1$, $c_2\mapsto e^{2i\varphi}c_2$, so
the phase-invariant data are $|c_1|$ (first order, 1 real) and
$$\kappa:=\frac{c_2}{c_1^2}=-\frac{cd}{ad-bc}\quad\text{for }F(w)=\frac{aw+b}{cw+d}\tag{5.3}$$
(second order, 2 real). Equivalently — and this is the cleaner object, because it is what the
sewing sees — the *image of the unit disc* $F(D)$, a disc with centre and radius (3 real):
$F(D)$ together with $F(0)=z_i$ fixes $F$ up to $w\mapsto e^{i\varphi}w$ (uniqueness of the
Riemann map), so **germ coincidence modulo phase $\iff$ disc-image coincidence**, and for Möbius
maps second order is the *full* germ. Both were computed (script part 4): $\Delta\kappa_i=\kappa_i^{(s)}-\kappa_i^{(t)}$
and the relative Hausdorff distance $d_H(F^{(s)}_i(D),F^{(t)}_i(D))/r^{(s)}_i=(|c^{(s)}-c^{(t)}|+|r^{(s)}-r^{(t)}|)/r^{(s)}$
(punctures $3$ in the chart $1/z$).

*Reflection formula, second order (C4g2).* From $F_i^{(t)}=g_t\circ\overline{F_{\pi(i)}^{(s)}}$
(the bar denotes conjugated Taylor coefficients) and $g_t(z_i+u)=g_t(z_i)+g'u+\tfrac12g''u^2+\dots$:
$$\kappa_i^{(t)}=\frac{\overline{\kappa_{\pi(i)}^{(s)}}}{g'_i}+\frac{g''_i}{2g_i'^2},\qquad
(g',g'')=(-1,-2)_{z=0},\ (1,2)_{z=1},\ (1,-2)_{z=\infty},\ \Big(-\tfrac1{(\bar Z-1)^2},\tfrac2{(\bar Z-1)^3}\Big)_{z=Z},
\tag{5.4}$$
verified against the independently constructed $t$-germs at all 25 seam points to $10^{-8}$
(C4g2). So $\Delta\kappa_1=\kappa_1^{(s)}+\overline{\kappa_1^{(s)}}+1=1+2\Re\kappa_1^{(s)}$: the
second-order mismatch is *generically non-zero* — the disc $F_1^{(s)}(D)$ would have to be
$\mathsf R$-symmetric for it to vanish, and the $A_1$ disc is not.

*Numbers ($\gamma'=9.5$, $\alpha'=0$, $\beta'=3/2$).*

| where | $|\Delta\kappa_i|$, $i=1..4$ | $d_H/r^{(s)}$, $i=1..4$ |
|---|---|---|
| $S_3$ seam, 25 pts, min over pts | $1.000,\ 1.782,\ 1.782,\ 1.000$ | $0.160,\ 0.141,\ 0.160,\ 0.163$ |
| $S_3$ seam, max over pts | $1.000,\ 2.000,\ 2.000,\ 1.000$ | $0.171,\ 0.149,\ 0.171,\ 0.175$ |
| $Z=2$ ($g_t$-fixed point) | $1,\ 2,\ 2,\ 1$ | $0.171,\ 0.149,\ 0.171,\ 0.175$ |
| 9 rays, $\min_\sigma\|(\Re m,\Delta\kappa)\|$ | $[2.18,\ 3.14]$ (norm over the 12 components) | — |

($|\Delta\kappa_{1,4}|=1$ exactly on the seam: at $\alpha'=0$, $\kappa_1^{(s)}=-1$ exactly
($F_1^{(s)}=w/(w-\gamma'z_3)$), so $\kappa_1^{(t)}=0$ — the $t$-coordinate at puncture 1 is affine,
its disc centred on the puncture, while the $s$-disc is off-centre with the same conformal radius
(critic 032 iteration 2); the disc-image numbers are the
physical statement: the two coordinate discs at each puncture differ by $14$–$17\,\%$ of their
radius.) Checks: C4k ($|\Delta\kappa|>0.05$), C4k2 ($d_H/r>0.05$), C4f (at $Z=2$), break leg C4k
(the $s$-composite against itself gives $0$ and fails), C4d3 (no zero of the 12-component
phase-invariant mismatch on any ray, $\min\ge2.18$).

**Corrected count.** Per seam point, phases quotiented: **4 real conditions at first order — met
on the $S_3$ seam, by $\mathsf R$; 8 real conditions at second order (= the full Möbius germ) —
none met, mismatch $O(1)$ ($d_H/r\approx0.15$)**; total $12:1$, over-determined, with the first
genuine (unsolved) condition appearing at second order. Ray scan: the first-order minimum sits
on the $S_3$ seam, the full mismatch has no zero anywhere in the admissible range (C4d3), so
no sharp seam curve, star-shaped or not, makes the coordinate discs continuous; the $S_3$ seam
is the unique first-order solution and the best one can do.

**Consequence for gauge invariance — (5.1) re-argued.** The seam terms of (4.8) for adjacent
channels are the same antighost insertion $b(\text{tangent})$ on the same surface in the two
coordinate systems:
$$
\delta_{Q}S_{\rm exch}\big|_{\rm seams}
=\sum_{\text{seams }(\alpha\beta)}\ \oint_{\partial R_\alpha\cap\partial R_\beta}
\Big[\Omega^{(3)}_{b}\big(F^{(\alpha)}\big)-\Omega^{(3)}_{b}\big(F^{(\beta)}\big)\Big](\Psi^{\otimes4}).
\tag{5.1}
$$
The frame change at puncture $i$ is the operator $U_i=e^{i\varphi_iL_0^-}\exp\big(v_1^{(i)}L_1+\bar v_1^{(i)}\bar L_1+\dots\big)$
acting on $\Psi_i$, with $v_1^{(i)}=c_2/c_1$ (after aligning $|c_1|$, which agrees on the seam):
aligning the phases, $\Delta v_1^{(i)}=c_1^{(i)}\Delta\kappa_i$, $|\Delta v_1|=|c_1||\Delta\kappa|\approx0.14$
($|c_1|\approx0.14$, $|\Delta\kappa|=1$ at punctures $1,4$; $\approx0.15$ at $2,3$). Hence, on the
$S_3$ seam: (a) the $L_{n\ge1}$ part of $U_i$ is trivial on primaries and the $L_0^\pm$ part agrees
($|c_1|$ equal, $L_0^-=0$); but the antighost insertion of $\Omega_b$ carries $b_{n\ge1}$ modes
weighted by $\partial_\theta\Delta v_n$; on externals $c_1\bar c_1V|0\rangle$ ($V$ a matter primary of
any weight) both $L_{n\ge1}$ and $b_{n\ge1}$ annihilate the state ($\{b_1,c_1\}=0$, $b_n|0\rangle=0$
for $n\ge-1$), so (5.1) vanishes identically for total-primary externals in $\mathcal H_0$, on or off
shell; the seam term first acts on level-one non-primaries ($L_{-1}$ descendants, ghost-excited
states), which the string field contains — (5.1′) below is to be read with $\Psi_i$ non-primary
(critic 032 iteration 2, H4); (b) for generic externals the leading
term of (5.1) is
$$\oint\ \Delta v_1^{(i)}\,\Omega_b\big(\Psi_1,\dots,L_1\Psi_i,\dots\big)+\partial_\theta\Delta v_1^{(i)}\,\big(\dots b_1\Psi_i\dots\big)+{\rm c.c.}+O(\Delta v_1^2),\tag{5.1′}$$
non-zero unless the $\theta$-integral over the seam and the sum over the three seams cancel it.
*Evaluated here:* the coefficient $\Delta v_1^{(i)}(\theta)$ (table above), not the matrix element;
the phase of $\Delta v_1$ rotates along the seam (common rotation $\Im m(\theta)\in[-2.67,2.67]$
plus the phase of $\Delta\kappa$), so an $S_3$-covariant cancellation after integration is not
excluded by the numbers — an evaluation of (5.1′) on a level-one non-primary at generic momentum
is the outstanding machine check. Status of the off-shell claim: **argued; generically non-zero at
$O(\Delta v_1)$, not evaluated.**

**(5b) Cures: the collar term is sufficient, not shown necessary.** Harold's proposal —
interpolate, $F^{(\times)}_i(w;Z)=$ a $Z$-dependent combination of the $F_i^{(\alpha)}$ on a
collar $C_\epsilon$ around the seams, equal to $F_i^{(\alpha)}$ outside — gives a continuous
$S_4$-covariant coordinate system on $\mathcal M'_\times$ with the Feynman-boundary values fixed
at $|q|=1$ (R2); $\int_{\mathcal M'_\times}\Omega(F^{(\times)})$ is then a legitimate SZ quartic
vertex and the geometric master equation closes. The cubic exchange does not produce it (on
$C_\epsilon\cap R_\alpha$ it yields $\Omega(F^{(\alpha)})$, §4.2 being pointwise in $q$), so
$$
S=S_{\rm kin}+\omega_1\big(\Phi,\mathcal V_3'(\Psi,\Psi)\big)+\Delta S_4,\qquad
\Delta S_4=\sum_\alpha\int_{C_\epsilon\cap R_\alpha}\Big[\Omega\big(F^{(\times)}\big)-\Omega\big(F^{(\alpha)}\big)\Big](\Psi^{\otimes4}),
\tag{5.2}
$$
is gauge invariant *if* the interpolated discs stay embedded (§6). $\Delta S_4$ vanishes on shell,
is $O(\Delta v_1)\approx0.14$ relative off shell, and tends as
$\epsilon\to0$ to a seam distribution. **Whether (5.2) is the *only* cure is open** (the earlier
"$\iff$" and "a propagator-only cure does not exist" are withdrawn). Two points, following the
critic: (i) the *common rotation* $e^{i\varphi(\theta)L_0^-}$ of the four coordinates needs no
cure at all on $\mathcal H_0$ externals, and a $\theta$-dependent phase on the internal line
$e^{i\varphi(\theta)L_0^-}$ merely reparametrises $\theta$ (it is the twist itself) — it neither
produces nor removes anything physical; (ii) the second-order mismatch is a *relative* frame
change between the pair $(12)$ on sphere 1 and $(34)$ on sphere 2, and a modified sewing map at
the neck ($w_1w_2=q\,(1+\epsilon_1w_2+\dots)$, i.e. an operator $e^{\sum\epsilon_nL_n}$-type
insertion on the internal line) *does* change the transported coordinates of one sphere relative
to the other in the fixed frame. The earlier argument ("a single conformal map acts identically on
all four coordinates") was wrong for exactly this reason. Counting does not exclude a neck-map
cure — a general sewing map has infinitely many parameters for the 8 second-order conditions per
$\theta$ — but it must reduce to the standard plumbing at $|q|=1$ (to cancel against the physical
propagators) and be $S_3$-covariant; whether such a $\theta$-dependent kinetic operator exists is
**open, not analysed**. A $\mathcal V_3'$ depending on the adjoining propagator's $(\sigma,\theta)$
remains excluded as non-local. Hence: *the collar term (5.2) is one sufficient cure; a modified
internal-line operator is a candidate cure not excluded; a strictly cubic theory with the
standard $\hat{\mathsf P}$ and a sharp seam is expected to fail at second order off shell on non-primary external states
(argued, (5.1′) not evaluated).*

**(5c) Comparison with Erbin–Fırat (open string, `C9ETB6WE` §4–5).** Their cubic stubbed
theory is gauge invariant because $(\mathcal H\times\mathcal H,V_1,V_2)$ is a *strictly
associative* DG algebra: the $e^{-\lambda L_0}$ placements of their eq. (4.6) make
$V_2(V_2(\cdot,\cdot),\cdot)=V_2(\cdot,V_2(\cdot,\cdot))$ exactly, so the four-input relation
holds with $V_4=0$ and the non-polynomial theory is recovered by homotopy transfer (SDR, side
conditions (4.19)). Geometrically, associativity of Witten's product is the statement that the
$s$- and $t$-channel strips meet at $t=0$ with the *same* strip coordinates on the common
surface — the open-string seam is a point and the coordinates are continuous across it. The
closed analogue of their construction would be an $L_\infty$ structure on
$\mathcal H\times\mathcal H^{\rm even}$ with brackets $\{Q_B,\ \mathcal K=\hat{\mathsf P}^{-1},\ \mathcal V_3'\}$
and no 4-bracket; its four-input relation is, in geometric form, $\sum_\alpha\{Q_B,\hat{\mathsf P}\}$
inserted in $\mathcal V_3'\circ\hat{\mathsf P}\circ\mathcal V_3'$ $=0$. By (4.8) this splits into the
$|q|=1$ terms — which cancel against the $s=0$ boundaries of the physical propagators, provided
the physical cubic vertex is the same $\mathcal V_3'$ (or one whose Feynman boundary is R2's
curve with the same coordinates; assumption A5, §7) — and the seam terms (5.1). **The seam term
of (4.8) is exactly the failure of the $L_\infty$ relation at four inputs**; §5a–a′ show it is
$O(\Delta v_1)$ off shell on every sharp seam (argued, not evaluated). What Erbin–Fırat get for free from associativity (coordinate
continuity at the seam) is, for the closed string, the second-order system of §5a′ (first order is solved by the $S_3$ seam) — the
same obstruction that forces $V_4\neq0$ in the standard cubic closed theory (SZ), displaced from
$|q|=1$ to the seam curve. Their generalised stubs (§7 of the review: any BPZ-even $S$ commuting
with $Q_B$) do not help: the obstruction is in the vertex coordinates, not in the kinetic operator.

## §6 Verdict (iii) — rewritten 14d

**Verdict: conditional go; the strictly cubic single-strand theory is *conjectured* not gauge
invariant off shell (second-order seam mismatch computed, its effect on (5.1) not evaluated); with
the collar term (5.2) the theory is gauge invariant under one stated, checkable condition.**
Evidence levels: first-order seam continuity on the $S_3$ seam — *proven* (reflection $\mathsf R$,
(5.4)) and *computed* (C4c, C4g, exact); second-order/disc mismatch $O(1)$ on every admissible
sharp seam — *computed* (C4k, C4d3, $\gamma'=9.5$, $\beta'=3/2$ only); (5.1) $\ne0$ off shell —
*argued*, not evaluated; collar cure sufficient — *argued* (SZ master equation); collar cure
necessary — *not shown* (a neck-map cure is open, §5b).

*What is shown.* (1) The $S_3$ seam makes the transported coordinates of adjacent channels agree
at first order, up to a common rotation that is trivial on $\mathcal H_0$: the four physical
first-order conditions are solved, exactly, by the reflection symmetry across the seam. (2) The
coordinate *discs* still differ at each puncture by $d_H/r\approx0.14$–$0.17$ (second order = the
full Möbius germ), for the $S_3$ seam and for every seam curve in the admissible range; a sharp
seam with continuous coordinate discs does not exist ($12:1$ count, first 4 met, next 8 not).
(3) The seam term (5.1) is the failure of the four-input $L_\infty$ relation (§5c); on shell it
vanishes (§4); off shell its leading term is (5.1′), coefficient $|\Delta v_1|\approx0.14$, matrix
element not evaluated. Insensitivity to $\beta',\gamma'$ is *not* claimed any more: only the
$12:1$ count is parameter-free; the size and the possible integrated cancellation were checked at
one parameter point.

*Conditional go (construction named).* Vertex data: Harold's $\mathcal V_3'$ with a slack special
leg, $\gamma'\ge3.15$ (symmetric plumbing cut) or $\ge9.19$ (one-sided cut) at $\alpha'=0$,
$\beta'=3/2$ (§2, (P-strict)); auxiliary $\Phi\in\mathcal H^{\rm even}$ (even $L_0^-$,
level-mismatched components allowed; $\mathcal K=\hat{\mathsf P}^{-1}$ on the complement of the
odd sector — (γ)); propagator $\hat{\mathsf P}=\int\frac{d\theta}{2\pi}e^{i\theta L_0^-}b_0^+(e^{\sigma(\theta)L_0^+}-1)/L_0^+$
with the $S_3$ seam $\sigma(\theta)\in[0.434,0.880]$ of §3.3 — now singled out also as the unique
first-order-continuous seam in the scanned range (C4d), not merely one covering choice; plus
$\Delta S_4$ of (5.2) on a collar $C_\epsilon$ with interpolated coordinates $F^{(\times)}$.
**The single condition that decides**, checkable: *there exist interpolated coordinates
$F^{(\times)}_i$ on $C_\epsilon$, equal to $F^{(\alpha)}_i$ at its two edges, whose four discs stay
disjoint and embedded throughout the collar* ((P-strict) extended from $R_\alpha$ to
$C_\epsilon$; testable by the disc-overlap routine of script part 1 on an explicit interpolation
— since the two discs at each puncture differ by only $\sim15\,\%$ of their radius and the first
order already agrees, a linear interpolation of the disc data is the natural candidate). If it
holds, (5.2) is a consistent theory by the SZ geometric master equation. If it fails, *this*
interpolation fails; other interpolations, or a modified neck map (§5b (ii)), are not excluded.
Still to be proven even then: five-point sewability of the composite (δ), the $S_4$ condition on
the special leg beyond the piecewise covariance of §4.4 (s), and that the collar's $\epsilon\to0$
limit is a well-defined seam vertex (not needed: finite $\epsilon$ is a legitimate choice).

*What the paper may say.* *The single-strand reversed-range exchange with $\mathcal V_3'$
reproduces $\int_{\mathcal M'_\times}\Omega_{V_4}$ on shell (§4); the $S_3$ seam makes the local
coordinates of adjacent channels continuous at first order but not beyond, the coordinate discs
differing by $\sim15\,\%$ of their radius across the seam; off shell the strictly cubic theory is
therefore expected to fail gauge invariance at second order in the seam data on non-primary external states, and a
collar-supported quartic term (5.2) restores it under a stated condition.* Not: "a cubic theory
with a geometric auxiliary channel exists à la Erbin–Fırat" (price $X=\Delta S_4$, or an as yet
unconstructed modified kinetic operator), and not "the strictly cubic version is an on-shell
coincidence" as a proven statement — it is the expected outcome, with (5.1′) unevaluated.

**The two questions of the 4-point summary note (`notes_4_point_summary.tex` §Questions).**

*Q1 — functions $f_i^{(\times)}$ agreeing with $f_i^{(\alpha)}$ on $\partial\mathcal M_\alpha\cap\mathcal M_\times$.*
Such functions exist. Corrected after critic 032: a seam achieving *first-order* agreement of the
$f_i^{(\alpha)}$ across it *does* exist — the $S_3$ seam (fixed circles of the transpositions),
where the $s$- and $t$-coordinates are related by the anti-holomorphic reflection across the
seam, so their derivative moduli coincide and the phases differ by a common rotation invisible on
$\mathcal H_0$ (§5a). Agreement of the full germs (for these Möbius coordinates: of the coordinate
*discs*) fails at second order by $\sim15\,\%$ of the disc radius, for the $S_3$ seam and for every
other seam in the admissible range (§5a′). Harold's interpolation is therefore needed only for the
second-order data, and the discs to be interpolated are already close; its cost is the quartic
collar term (5.2), one sufficient cure (necessity not shown, §5b).

*Q2 — $\sigma(\theta)$ such that $Z_4^{(s,t,u)}(e^{\sigma+i\theta})$, $s\in[-\sigma(\theta),0]$,
covers $\mathcal M_\times$.* Yes: with the $S_3$-symmetric seam (fixed lines of the transpositions)
$\sigma(\theta)\in[0.434,0.880]$ covers $\mathcal M'_\times$ once, gap $0.09\,\%$ of the
discretisation, no overlap (§3.3, C2); a constant $\sigma$ cannot ($0.434<0.879$, §3.2). The
price is $\Phi\in\mathcal H^{\rm even}$ with level-mismatched components (030 count (i)) and a
slack special leg $\gamma'\ge9.19$ (one-sided cut; $3.15$ symmetric, §2) ($\alpha'=0$) so that the extended coordinate disc stays
embedded (§2); the curves $Z_4^{(\alpha)}(e^{\sigma(\theta)+i\theta})$ of the three channels
merge along the seams, as the seam analysis anticipates.

**What the vertex buys regardless of the verdict.** The $\mathcal V_3'$ family with a slack
special leg gives, at no extra vertex data, a sewable (four-point; five-point unchecked)
$S_4$-covariant piecewise coordinate system on all of $\mathcal M'_\times$ — continuous at first
order across the $S_3$ seams, discontinuous at second order — whose measure is the
canonical SZ measure (4.5)–(4.7) and whose outer boundary is R2's curve with the Feynman-region
coordinates. That is a candidate $V_4$ *region with coordinates* — exactly the input the
interpolation (5.2) or a standard $V_4$ construction needs, and a direct closed-string analogue
of the stub-region interpretation in Erbin–Fırat (`C9ETB6WE` §E). The under-determination (β) is
then a gauge-like freedom: different seams give different $F^{(\times)}$, hence different
$V_4^{(\times)}$ related by the standard vertex-coordinate homotopy (a field redefinition), *if*
the collar term is included; for the sharp cubic theory it is a genuine ambiguity between
non-gauge-invariant actions.

## §7 Self-review (14a–d)

**Weakest step.** The passage from "the coordinate discs differ at second order on every sharp
seam" (computed, exact Möbius data) to "(5.1) is non-zero off shell" (argued via (5.1′)). The
coefficient $\Delta v_1(\theta)$ rotates along the seam; an $S_3$-covariant cancellation after the
$\theta$-integral and the sum over seams is not excluded. Machine check not done: evaluate
(5.1′) on a level-one *non-primary* state (primaries give zero exactly) at generic momentum with the explicit Möbius $F^{(s)},F^{(t)}$ of
part 4 (an extension of part 3's quadrature). 14c's version of this section rested on a
mismatch that was pure coordinate phase (critic 032 H4); that is corrected in §5a–a′.

**Assumptions carried, all stated.** A1 $\alpha'=0$, $\beta'=3/2$, $\gamma'=9.5$ (numbers);
the $12:1$ count and the reflection argument are parameter-free, the sizes are not. A2 The $S_3$
partition as the seam; the ray scan C4d–d3 covers the admissible range for any star-shaped seam.
A3 The sewing measure identity (4.5) at CFT level, under the convergence hypothesis (P). A4
Frame-dependence of $\Omega_b$ off shell (standard). A5 The physical cubic vertex whose $s=0$
boundaries cancel the $|q|=1$ terms of (4.8) is $\mathcal V_3'$ or shares R2's boundary
coordinates. A6 External states in $\mathcal H_0$ (phase quotient); internal states in
$\mathcal H^{\rm even}$ are integrated out in (5.1). A7 Plumbing cut convention (§2, H1): both
$\sigma_{\max}$ values are quoted.

**Not checked across 14a–d:** five-point sewability; $\beta'\ne3/2$; (4.5), (4.8) by hand only;
Fubini–Study areas; the off-shell value of (5.1′); the collar existence condition of §6; a
neck-map cure (§5b (ii)); the $S_4$ condition beyond piecewise covariance; $\mathcal K$ on
$\mathcal H^{\rm even}$ beyond C3f; $h$-scaling of the 0.09 % covering gap (H2, one grid only).

**Falsifiability of the machine checks.** 62/62; break legs P1b-break, C2h, C3d, C3e, C4c-break (perturbed
$A_1$ disc, $|\Re m|\to0.05$), C4g-break (wrong reflection), C4k-break (self-comparison) all FAIL
as required. Part 4 germs are exact (Möbius fit, C4b), so no step-size question remains. C4g/C4g2
compare the independently constructed $t$-composite against a closed-form prediction from the
$s$-composite — the independent check §7 (14c) asked for; it passes, so `t_composite_maps` is
correct and 14c's error was in what was compared, as the critic said.

**Scope of the verdict.** (α-rev) only; nothing on (α-neck) or (γ). Within (α-rev): conditional
go with the collar term; strictly cubic expected to fail off shell at second order on non-primary external states, not proven.

## §8 Proposed ledger text (not applied; no stronger than §6)

**New row (Task 14, record 032, script `codes/verify-v3prime-route.py` 62/62).**
*Single-strand $\mathcal V_3'$ route (α-rev).* (P) The special-leg disc of $\mathcal V_3'$ extends
to radius $r$ and stays embedded iff $r\le r_{\max}=\frac{2\beta'(\gamma'-1)}{\gamma'+1}$ ($\alpha'=0$);
$\sigma_{\max}=\ln r_{\max}$ for a one-sided plumbing cut, $2\ln r_{\max}$ for the symmetric cut;
$=0$ for the tangent (SZ-type) vertex — *computed, self-checked*. (i) The reversed-range family
covers $\mathcal M'_\times$ once for the $S_3$ seam $\sigma\in[0.434,0.880]$ (needs
$\gamma'\ge3.15$ symmetric / $9.19$ one-sided, $\Phi\in\mathcal H^{\rm even}$), never for constant
$\sigma$ — *computed*. (ii) The operator identity holds on shell to the covering accuracy, under the
sewing-convergence hypothesis — *argued (measure) + computed*. (iii) Across the $S_3$ seam the
transported coordinates agree at first order up to a common phase (reflection symmetry; 4 real
conditions met) and differ at second order by $\sim15\,\%$ of the disc radius on every admissible
seam ($12:1$ count) — *proven + computed*; hence the four-input $L_\infty$ relation is expected to
fail off shell on non-primary external states by the seam term (5.1′) (primaries give zero exactly), *argued, not evaluated*; the collar quartic term (5.2) is a
sufficient cure under a stated, unchecked embedding condition; necessity not shown. Status:
computed/self-checked for (P),(i),(ii),(iii-geometry); argued for (iii-gauge); critic iteration 2 (2026-09-14): REVISE light 0F/1S/8m, one-liners applied by the orchestrator; promoted.

**Annotation proposed for R30:** "(α-rev): covering exists with a $\theta$-dependent seam (032 §3);
on-shell identity holds (032 §4); seam coordinates continuous at first order, not at second (032
§5a–a′); off-shell gauge invariance of the strictly cubic version expected to fail on non-primary external states, not evaluated;
collar quartic term (5.2) is a sufficient cure. Does *not* by itself retire (α-rev) in favour of (γ)."

**Annotation proposed for R2:** "The same $\mathcal V_3'$ family continued to $|q|>1$ is injective on
$|q|<4\beta'^2$ and, with the $S_3$ seam, covers $\mathcal M'_\times$ once; the transported
coordinates are $S_4$-covariant piecewise, continuous at first order and discontinuous at second
order across the seams (032 §3.3, §5a–a′)."

**One line for the Riemann-surface note, item (D):** "The single-strand exchange with $\mathcal V_3'$
covers the vertex region and reproduces $V_4$ on shell; across the seams the two channels' local
coordinate discs differ at second order, so off shell (on non-primary external states) a quartic term on a collar around the seams is
expected to be needed — the closed-string cost of what associativity gives Erbin–Fırat for free."

## Status
record closed 2026-09-14: critic iteration 2 REVISE light (one-liners 1–4 applied by the orchestrator; H4 correction: seam term vanishes on total-primary externals, acts on non-primaries); promoted to ledger R37 + annotations R30/R2; open decisions: (a) evaluating (5.1′) on a level-one non-primary, (b) cut convention, (c) neck-map cure; next: none
`14d complete (seam question re-derived with phases quotiented); next: critic iteration 2 (§5–§8 + H1/H3 propagation)`
