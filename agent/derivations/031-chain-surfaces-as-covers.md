# 031 — Chain surfaces of the auxiliary channel as branched covers (Task 13)

- Date: 2026-09-14. Sub-tasks: **13a** (§1–§3, conventions, involution on a slice, frozen
  $k=2$ chain) → **13b** (§4–§5, quotient family vs $\mathcal V_{0,4}$, sewing lift) →
  **13c** (§6–§9, twist-field ghost count, the 2→2 question, self-review, ledger text).
- Briefs: 13a `agent/briefs/active-computator-13a-covers-setup-20260914T003500.md`;
  13b `agent/briefs/active-computator-13b-quotient-family-20260914T011500.md`;
  13c `agent/briefs/active-computator-13c-twist-count-20260914T020000.md`.
- Script: `codes/verify-chain-surfaces-covers.py` (part 1 = §2, part 2 = §3, parts 3–4 = §4,
  part 5 = §5, part 6 = §6).
- 13b inputs: R2 (`knowledge/cubic-sft-overview.tex` §explicit, eqs (V3primemaps), (Z4),
  (Zstu)); 020 §1 (frozen-neck sewing, (1.a)) and §5 (coloured gluing).
- Inputs taken as given: 030 §6.1 (hand-off, Q13), 030 §1.1 (conventions), 030 §3.7.3
  (eight antighosts), 030 §5.3 (case (β)), 008 (B.2), ledger R27/R30.
- Literature: Lunin–Mathur, hep-th/0006196 (covering-space dictionary), cited from memory.

**Literal task (13a).** For fixture (β2): decide whether each slice
$\Sigma_{1,4}(s,\theta)$ carries the holomorphic involution $\iota$ of Q13, and locate the
frozen ($s=0$) quotient in $\mathcal M_{0,4}$.
**Objective served.** Q13 (030 §6.1): is the (β2) torus family a double cover of the
$\mathcal V_{0,4}$ family? A "no" excludes (β); a "yes" makes R27's resolved genus literal.


## 0. Verdict table

| # | question | verdict (13a) | where |
|---|---|---|---|
| (i) | involution $\iota$ exists on a slice $\Sigma_{1,4}(s,\theta)$ | **conditionally yes** — *if*: proven; *only if*: argued (decomposition-preservation sentence of §2.2, not proven) + numerically supported (script 2b, one non-harmonic slice): $\mu_0$ harmonic, $(1,2;a,b)=(3,4;a',b')=-1$, with $\iota_1$-symmetric discs, *and* the tube is diagonal (β2); (β1) product tube excluded for $|s_a-s_b|>C(\mu_0)$ (proven) and numerically at a generic point; every $q_a\ne q_b$ not proven | §2, (2.4) |
| (ii) | position of the frozen ($s=0$) quotient in $\mathcal M_{0,4}$ | **computed, side undecided**: $x(0,\theta)=\lambda(\tau(0,\theta))$ via Schottky uniformisation (exact for Möbius discs); it is the $|q|=1$ curve of the *induced* cubic vertex (3.6); inside/outside $\partial\mathcal V_{0,4}$ depends on the disc size $r\subset\mu_0$ vs SZ (13b) | §3, (3.7) |
| (iii) | quotient family $=\mathcal V_{0,4}$ (region and boundary) | **no, numerically supported (Möbius-disc model, sampled $(\beta,r)$)**: geometrically, the induced disc is a limaçon, never SZ's round disc (proven for all admissible $(z_a,r)$; this alone does *not* imply that the $|q|=1$ curves differ); the necessary tiling condition (A) — one $\lambda$ matching both real crossings of R2's $\partial\mathcal V_{0,4}$ — fails at the sampled $(\beta,r)$: for $r<r_c(\beta)$ the collar never reaches $\partial F_s$, for $r>r_c(\beta)$ the two crossing-$\lambda$'s have ratio $<1$ over the whole $r$ scan (script 7a; relative mismatch $0.20$ at $\beta=1$, decreasing with $\beta$, $5\times10^{-3}$ at $\beta=5$, script 7b — $O(1)$ for $\beta=O(1)$, not uniform in $\beta$); frozen curves do not seam (B). R2's $\beta$ is a free parameter of the $\mathcal V_3'$ family ($\beta>\tfrac12$), not a fixed number, so the scan is over a stated range $\beta\in[0.75,3]$. A general proof of $\partial_{s=\lambda}C_s\neq\partial F_s$ for all $r$ is open; the *objective* (β2 is not the $V_4$ integrand) is closed independently by the loop-momentum argument inherited from 030 §3.7.3 (§4.3) | §4, (4.3)–(4.7) |
| (iv) | sewing lift (does the plumbing fixture descend to the quotient?) | **partially**: soaked part lifts exactly to the orbifold untwisted-sector one-neck propagator ($L_{\rm tot}=L_0^{\rm orb}$) — "exactly" relative to the orbifold covering dictionary (Lunin–Mathur), cited from memory and not verified here; the Grassmann factorisation itself is proven; non-standard by the factor $-\tfrac14 b^+_{\rm rel}b^-_{\rm rel}$ (zero modes of the $S_2$-odd ghost = the two unsoaked tube antighosts, $\iota$-odd frozen moduli) and by the projection onto $\mathcal H_0\otimes\mathcal H_0$ | §5, (5.3)–(5.5) |
| (v) | twist-field ghost count (6 vs 12) | **match at 12** ($3$ per twist field $=\tfrac32+\tfrac32$ of the bosonised antiperiodic $\lambda=2$ twist field): the fixture realises reading (B) (all eight antighosts stay insertions: $4$ Beltrami at branch points, $b^\pm_{\rm tot}b^\pm_{\rm rel}$ on the neck); 030 posed readings (A)/(B) and left the choice open; the fixture realises (B), and all-six (A) is not realisable ($3/2\notin\mathbb Z$); **no independent anomaly "no"** — Q13's no is geometric + loop momentum | §6, (6.2)–(6.5) |
| (vi) | The 2→2 question: why a 2→2 gluing still describes a sphere | **answered**: on the quotient it is a 1→1 gluing of two three-punctured spheres of the *doubled* (orbifold) theory, the pair puncture being one puncture; the sphere is the orbifold's, the torus its double cover, the coloured genus $0$ is the quotient's genus; the loop momentum is the doubled theory's tree-level neck sum | §7, (7.1)–(7.3) |


## 1. Conventions

Everything from 030 §1.1 is inherited (physical ghost number, (1.1), fixtures (C5)); only
what 13a–c need is restated.

**(D1) The rigid slice.** $\Omega_{V_4}(\mu_0)$ is the $V_4$ integrand at one point
$\mu_0\in\mathcal P_{0,4}$: a four-punctured sphere with punctures $\{1,2,a,b\}$ and a
local coordinate (disc) at each puncture, carrying two unsoaked Beltrami antighosts
$b(\partial_{\mu_1})b(\partial_{\mu_2})$ (030 §3.7.3, row 12). Second copy: punctures
$\{3,4,a',b'\}$, same $\mu_0$.

**(D2) The diagonal plumbing.** Necks $a\sim a'$, $b\sim b'$ glued by
$$
w_a\,w_{a'}=q,\qquad w_b\,w_{b'}=q,\qquad q=e^{-s+i\theta},\quad s\in[0,\lambda],\ \theta\in S^1,
\tag{1.1}
$$
the *same* $q$ on both necks ((β2), 030 §5.3). The product tube (β1) has independent
$q_a\neq q_b$. The glued surface is $\Sigma_{1,4}(s,\theta)$, genus 1 by 008 (B.2)
($\chi=2\cdot(2-4)+0=-4$ for two spheres with two necks, so $2-2g-4=-4$, $g=1$).
Frozen chain: $s=0$, $|q|=1$ (R27's $k=2$ node, unintegrated).

**(D3) Antighosts.** Eight on $\Sigma_{1,4}$: four Beltrami on the two rigid slices, two
$b^+$ and two $b^-$ on the two necks; only $b(\partial_s)=b^+_{\rm tot}$ and
$b(\partial_\theta)=b^-_{\rm tot}$ are soaked by the $(s,\theta)$ integral (030 §3.7.3;
$n_b^{\rm tot}=8=\dim_\R\mathcal M_{1,4}$). The six unsoaked ones are what a "yes" to Q13
must reinterpret as twist-field ghost number (13c).

**(D4) Explicit model of the rigid slice (fixed for Task 13).** Sphere 1 is $\mathbb{CP}^1$
with coordinate $z$,
$$
1\mapsto z=0,\qquad 2\mapsto z=\infty,\qquad a\mapsto z_a,\qquad b\mapsto z_b ,
\tag{1.2}
$$
local coordinates (Möbius in $z$, disc radius $r$)
$$
w_a(z)=\frac{z-z_a}{r_a},\qquad w_b(z)=\frac{z-z_b}{r_b},\qquad
|z-z_a|<r_a,\ |z-z_b|<r_b \text{ disjoint and not containing } 0,\infty .
\tag{1.3}
$$
Residual freedom: the Möbius maps fixing $0,\infty$ are $z\mapsto cz$, $c\in\mathbb C^*$;
they rescale $(z_a,z_b,r_a,r_b)\mapsto(cz_a,cz_b,|c|r_a,|c|r_b)$ up to the phase of $c$ in
$w$ (a rotation of each local coordinate). Invariants: the cross-ratio
$$
(1,2;a,b):=\frac{(z_1-z_a)(z_2-z_b)}{(z_1-z_b)(z_2-z_a)}\;\xrightarrow{\;z_1=0,\ z_2\to\infty\;}\;\frac{z_a}{z_b},
\tag{1.4}
$$
and the ratios $r_a/|z_a|$, $r_b/|z_b|$. Sphere 2 is the same model in a coordinate
$z'$ with $3\mapsto0$, $4\mapsto\infty$, $a'\mapsto z_a$, $b'\mapsto z_b$ (same $\mu_0$,
D1). Whether the *actual* $\mathcal V_{0,4}$ slice $\mu_0$ (SZ-type discs, R2) is of the
form (1.3) with Möbius discs is not assumed; the Möbius form is what makes §3's
uniformisation exact, and the criterion of §2 does not depend on it.

**(D5) Riemann-surface facts used (standard, no citation).** A non-trivial Möbius
involution has exactly two fixed points; an involution of a genus-1 curve with a fixed
point is $u\mapsto c-u$ and has exactly four fixed points, the translates of one by
$E[2]$; $E/\iota\cong\mathbb{CP}^1$ branched at those four points (Riemann–Hurwitz,
030 §6.1); the branch cross-ratio is the modular $\lambda$-function of $\tau$ (any of its
six $S_3$ images, depending on the labelling). Covering dictionary: Lunin–Mathur,
hep-th/0006196.



## 2. The involution on a slice

### 2.1 Möbius involution on sphere 1 (first falsifier)

*Claim.* A Möbius involution $\iota_1$ of sphere 1 with $\iota_1(1)=1$, $\iota_1(2)=2$,
$\iota_1(a)=b$ exists iff $(1,2;a,b)=-1$; it is then unique.

*Derivation.* In the model (1.2) the Möbius maps fixing $0$ and $\infty$ are
$z\mapsto cz$; an involution needs $c^2=1$, $c\ne1$, so
$$
\iota_1(z)=-z
\tag{2.1}
$$
is the *only* non-trivial Möbius involution fixing $1,2$. It swaps $a\leftrightarrow b$ iff
$z_b=-z_a$, i.e. by (1.4) iff $(1,2;a,b)=z_a/z_b=-1$. Conversely if $z_a/z_b=-1$, (2.1)
does the job. $\square$ (Coordinate-free: the fixed points $1,2$ and any two swapped points
$a,b$ satisfy $(1,2;a,b)=(1,2;b,a)=(1,2;a,b)^{-1}$, so the cross-ratio is $\pm1$, and
$+1$ would force $a=b$.) Same statement for sphere 2 with $(3,4;a',b')=-1$; since both
slices are the same $\mu_0$ (D1), one condition on $\mu_0$ covers both. Call a slice with
$(1,2;a,b)=-1$ **harmonic**.

### 2.2 Lift to the plumbed surface

$\iota$ on $\Sigma_{1,4}$ must restrict to $\iota_1$ on sphere 1 and $\iota_2$ on
sphere 2 (a holomorphic involution of the glued surface fixing the punctures restricts, away
from the necks, to automorphisms of the punctured slices, which are Möbius — this sentence
is *asserted, not proven*: the neck annuli are not canonical subsets of the glued torus, so an
involution of the torus fixing the four punctures, $u\mapsto c-u$ by (D5), need not preserve
the plumbing decomposition; the "only if" below therefore rests on this assertion plus the
numerical break leg of script 2b, while the "if" direction is proven). It exchanges
the necks, so it must map the $a$-annulus to the $b$-annulus compatibly with (1.1):
$$
w_b(\iota_1 z)=e^{i\varphi}w_a(z),\qquad w_{b'}(\iota_2 z')=e^{i\varphi'}w_{a'}(z'),
\tag{2.2}
$$
for constant phases (the local coordinate at $b$ must be the $\iota_1$-transport of that at
$a$ up to a rotation; any non-rotational mismatch, e.g. $r_b\neq r_a$ in (1.3), obstructs
the lift because $\iota_1$ is an isometry of the round discs only for $r_a=r_b$ — under D1,
the same $\mu_0$ on both spheres; in general (1.1) constrains the products $r_br_{b'}$ vs
$r_ar_{a'}$, and the coordinate-free criterion is $w_b\circ\iota_1=e^{i\varphi}w_a$ on the
annulus, as stated). Then a
point of the $a$-neck with $w_aw_{a'}=q_a$ is sent to a point with
$w_bw_{b'}=e^{i(\varphi+\varphi')}q_a$, which lies on the $b$-neck iff
$$
q_b=e^{i(\varphi+\varphi')}\,q_a .
\tag{2.3}
$$
So the lift exists iff $|q_a|=|q_b|$ (equal neck lengths) and the twists differ by the fixed
phase $\varphi+\varphi'$, which is absorbed by redefining $w_b\to e^{-i\varphi}w_b$ (a
choice of the rigid slice's coordinates, i.e. of $\mu_0$): the *diagonal* tube (1.1). In
the model (1.3) with $z_b=-z_a$, $r_b=r_a$: $w_b(-z)=(-z+z_a)/r_a=-w_a(z)$,
$\varphi=\varphi'=\pi$, $\varphi+\varphi'=0$, so (2.3) is $q_b=q_a$ exactly.

*Fixed points of the lift.* $\iota$ fixes $1,2$ (sphere 1) and $3,4$ (sphere 2); on the
necks $\iota$ maps neck $a$ to neck $b$, so there are no fixed points there; on the slices
the only fixed points of $z\mapsto-z$ are $0,\infty$. Hence exactly four fixed points,
the external punctures — consistent with Riemann–Hurwitz $b=4$ and with (D5): $\iota$ is
*the* elliptic involution centred at puncture 1, and the four punctures are mutually
2-torsion translates on the torus. (Script part 2 tests this numerically.)

$$
\boxed{\text{(i): }\iota\text{ exists on }\Sigma_{1,4}(s,\theta)\text{ for all }(s,\theta)\iff
\mu_0\text{ harmonic }((1,2;a,b)=(3,4;a',b')=-1),\ w_b=\iota_1^*w_a\text{ up to phase, and the tube is diagonal.}}
\tag{2.4}
$$
Label of (2.4): "$\Leftarrow$" (harmonic $\Rightarrow\iota$) **proven**; "$\Rightarrow$" (only if)
**argued + numerically supported** — it uses the unproven decomposition-preservation sentence
above and script 2b's break leg on one non-harmonic slice (and, for the product tube, §2.3).
Only the "if" direction is used by the "no" of row (iii).

### 2.3 "Only if" for the product tube (β1)

Take a harmonic $\mu_0$ and $q_a\neq q_b$ with $|q_a|\neq|q_b|$ (generic point of (β1)).
Suppose $\iota$ exists. It is a conformal automorphism of $\Sigma_{1,4}(q_a,q_b)$ mapping the
isotopy class $\gamma_a$ of the $a$-neck core curve to $\gamma_b$ (it swaps the necks); on
the four-punctured torus $\gamma_a\neq\gamma_b$ as isotopy classes (both separate
$\{1,2\}$ from $\{3,4\}$ but are distinguished by the punctures). Extremal length is a
conformal invariant, so $\mathrm{EL}(\gamma_a)=\mathrm{EL}(\gamma_b)$. Bounds: the neck
annulus $\{|q_a|<|w_a|<1\}$ is embedded in class $\gamma_a$ with modulus
$s_a/2\pi$ ($s_a=-\log|q_a|$), so $\mathrm{EL}(\gamma_a)\le2\pi/s_a$; conversely any
annulus in class $\gamma_a$ is contained in the neck annulus extended by the two
punctured slices, whose contribution is bounded by a constant $C(\mu_0)$ (the maximal
modulus of an annulus around $a$ in the slice avoiding $1,2,b$ is finite), so
$\mathrm{EL}(\gamma_a)\ge2\pi/(s_a+C)$, with $C$ the same for $b$ by harmonicity. Hence
$s_a\le s_b+C$ and $s_b\le s_a+C$: for $|s_a-s_b|>C(\mu_0)$ **no** involution exists.
This proves the "only if" on an open set of (β1) (large length mismatch); for
$0<|s_a-s_b|\le C$ the argument is silent. Complement by dimension count (D5): the locus
in $\mathcal M_{1,4}$ where the four punctures are 2-torsion translates has
$\dim_\mathbb C=1$, while (β1) sweeps a 2-complex-parameter family $(q_a,q_b)$ containing
the diagonal $q_a=q_b$; the locus meets the family in a 1-dimensional set that contains
the diagonal, so away from the diagonal it can only be another curve, and the extremal
length bound excludes any such curve with $|s_a-s_b|$ large. Status: **proven for
$|s_a-s_b|>C$, dimensionally generic otherwise, not proven for every $q_a\ne q_b$.**
(A fixed-point count does not help: any $u\mapsto c-u$ has four fixed points.)

### 2.4 Is the actual $\mathcal V_{0,4}$ slice harmonic?

Not decidable from the inputs. (2.4) is a condition on $\mu_0\in\mathcal P_{0,4}$: the
puncture positions must satisfy $(1,2;a,b)=-1$ *and* the two local discs must be
exchanged by $z\mapsto-z$. The $V_4$ integrand at a generic point of $\mathcal V_{0,4}$
does not satisfy the first; a symmetric point does (the cross-ratio $-1$ is the
$\mathbb Z_2$-symmetric point of the $\{1,2\}|\{a,b\}$ channel; note that in
$\mathcal M_{0,4}$ the point $x=-1$ and its $S_3$ images $x=2,\tfrac12$ are exactly the
points with an extra $\mathbb Z_2$ automorphism). Whether the SZ-type local coordinates of
$\mathcal V_{0,4}$ at that point are $\iota_1$-symmetric is automatic if the coordinates
are defined canonically from the punctured sphere (any canonical construction commutes
with automorphisms — SZ minimal-area or the quadratic-differential prescription both do);
so the second condition holds for canonical coordinates at a harmonic point. **What
decides it:** the value of $\mu_0$ that (β2) uses. 030 leaves $\mu_0$ free ("a single
point of $\mathcal P_{0,4}$"). So (i) is *conditionally yes*: (β2) must fix
$\mu_0$ at the harmonic point $(1,2;a,b)=-1$ with canonical coordinates. Since
$\mathcal V_{0,4}$ is the *whole* vertex region and $\Omega_{V_4}(\mu_0)$ is its integrand
at one point, choosing $\mu_0$ harmonic is a restriction of (β2), not a property of
$V_4$; whether the restricted fixture reproduces $V_4$ is (iii) (13b).



## 3. The $k=2$ frozen chain in $\mathcal M_{0,4}$

### 3.1 Schottky uniformisation of the chain (exact for Möbius discs)

With the model (1.3), $z_b=-z_a$, $r_a=r_b=r$, the gluing (1.1) is a pair of Möbius maps
sphere 1 → sphere 2,
$$
T_a:\ z'=z_a+\frac{r^2q_a}{z-z_a},\qquad T_b:\ z'=-z_a+\frac{r^2q_b}{z+z_a}
\tag{3.1}
$$
(from $w_{a'}(z')=q_a/w_a(z)$). Identify sphere 2 with sphere 1 through $T_a$; the
$b$-gluing becomes a self-identification of sphere 1 by
$$
g:=T_b^{-1}\circ T_a\in PSL(2,\mathbb C),
\tag{3.2}
$$
and $\Sigma_{1,4}=\Omega/\langle g\rangle$, a Schottky torus: $g$ maps the exterior of the
disc $D_a$ into $D_b$ (disjoint discs), hence is loxodromic with multiplier $\kappa$,
$0<|\kappa|<1$, **also at $|q|=1$**: the frozen chain is a non-degenerate torus as long as
the coordinate discs are disjoint. Conjugating $g$ to $\zeta\mapsto\kappa\zeta$ by
$\zeta=(z-\xi_+)/(z-\xi_-)$ ($\xi_\pm$ the fixed points of $g$),
$$
\Sigma_{1,4}\cong\mathbb C^*/\langle\kappa\rangle\cong\mathbb C/(\mathbb Z+\tau\mathbb Z),
\qquad \tau=\frac{\log\kappa}{2\pi i},\qquad u=\frac{\log\zeta}{2\pi i},
\tag{3.3}
$$
and the four punctures sit at $u_1=u(0)$, $u_2=u(\infty)$, $u_3=u(T_a^{-1}(0))$,
$u_4=u(T_a^{-1}(\infty))$. Numerically (script 2b) $u_i-u_1$, $i=2,3,4$, are the three
non-zero half-periods — the involution of §2 is the elliptic involution centred at $1$
and its fixed points are exactly the four punctures, as claimed in §2.2; the check fails
for a non-harmonic slice and for a product tube $q_a\ne q_b$ (script 2b break legs), the
latter giving *numerical* support for §2.3 beyond the extremal-length regime.

### 3.2 The modulus $\tau(s,\theta)$ and the branch cross-ratio

Degeneration $s\to\infty$: $\kappa\to0$, $\mathrm{Im}\,\tau\to\infty$, with
$$
\frac{d\,\mathrm{Im}\,\tau}{ds}\;\xrightarrow{s\to\infty}\;\frac1\pi ,
\tag{3.4}
$$
i.e. $2\pi\,\mathrm{Im}\,\tau\simeq2s$: the $B$-cycle of the torus runs through *both* necks,
so the shared length $s$ counts twice (script 2e; the naive $1/2\pi$ fails the check). The
$A$-cycle is the neck circle. So $\tau\simeq(2s-2i\theta)/(2\pi i)+O(1)$, up to the
sign convention of $\theta$, plus an $O(1)$ correction from the rigid slices; on the
frozen slice $s=0$ the correction is everything: for $z_a=1$, $r=0.45$,
$\mathrm{Im}\,\tau(0,\theta)\in[0.915,0.980]$, $\mathrm{Re}\,\tau(0,\theta)$ sweeps
$[-0.36,0.36]$ (script output, $\theta\in[0,2\pi)$; $\theta$ and $2\pi-\theta$ give
conjugate $\tau$, a reflection symmetry of the model).

Branch cross-ratio: with puncture $1$ at $\infty$ of the quotient $\mathbb{CP}^1$
($\wp(u-u_1)$), $e_i=\wp(u_{i+1}-u_1)$ and
$$
x=\frac{e_1-e_3}{e_2-e_3}\in S_3\cdot\lambda(\tau),\qquad
\lambda(\tau)=\frac{\theta_2(0|\tau)^4}{\theta_3(0|\tau)^4},
\tag{3.5}
$$
checked to $8\times10^{-7}$ against a direct lattice-sum $\wp$ (script 2c, Richardson
extrapolated; the perturbed-$\tau$ break leg fails). Frozen curve on the numerical slice:
$|\lambda(\tau(0,\theta))|\in[0.52,0.70]$, $\lambda=0.597$ at $\theta=0$, $0.522$ at
$\theta=\pi$, complex in between (arg up to $\pm0.78$). As $s\to\infty$, $\lambda\to0$
(script 2d): the $s$-channel degeneration $x\to0$ in this labelling.

### 3.3 Position relative to $\mathcal V_{0,4}$ — what can and cannot be said

*Structural observation (the key output of 13a for 13b).* Because $\iota$ acts on each slice
as $z\mapsto-z$, the quotient of sphere 1 is $\mathbb{CP}^1$ with $u=z^2$, punctures $1,2$
at $u=0,\infty$ (the branch points) and *one* regular puncture at $u_a=z_a^2$ (the common
image of $a$ and $b$), with local coordinate $W_a:=w_a\circ\sqrt{\cdot}$ on the image of
the $a$-disc. Same for sphere 2. The quotient family is therefore
$$
\Sigma_{1,4}(s,\theta)/\iota\;=\;\text{two 3-punctured spheres }(0,\infty,u_a),\ (0,\infty,u_{a'})
\text{ plumbed by one neck } W_aW_{a'}=q=e^{-s+i\theta},
\tag{3.6}
$$
i.e. **a one-neck $s$-channel Feynman family of a rigid cubic vertex** whose local
coordinate at the third puncture is the induced $W_a$ (not Möbius in $u$, not SZ) — with
the two branch punctures carrying the pulled-back external states (twist fields, 13c). The
region swept by $x(s,\theta)$ for $s\in[0,\lambda]$ is a collar of the $s$-channel
degeneration bounded by the curve $|q|=1$ **of the induced coordinates**. Consequently:

- (ii) the frozen quotient $x(0,\theta)$ is the $|q_W|=1$ curve of the $W$-cubic vertex.
  Its position relative to R2's boundary of $\mathcal V_{0,4}$ (the $|q|=1$ curve of the
  *SZ* cubic vertex) is decided by comparing the induced disc $|W_a|<1$ with the SZ disc at
  the third puncture of $(0,\infty,u_a)$: if the induced disc is smaller (larger), the
  frozen curve lies inside the $s$-channel Feynman region (inside $\mathcal V_{0,4}$),
  respectively. The induced disc is the image under $u=z^2$ of $|z-z_a|<r$, $r<|z_a|$; its
  size is not fixed by anything in 13a's inputs ($r$ is part of $\mu_0$). **Not decided
  here; R2's SZ data were not among the inputs.** On the numerical slice ($z_a=1$,
  $r=0.45$) the frozen curve sits at $|\lambda|\approx0.52$–$0.70$ around the real axis
  between the $x=0$ degeneration and the symmetric point $x=\tfrac12$ (image of the
  $\mathbb Z_3$-symmetric point $e^{i\pi/3}$ under $S_3$ is not this; $x=\frac12$ is the
  $\mathbb Z_2$ point), which is *where a $|q|=1$ boundary of an $s$-channel collar is
  expected*; consistent with, not evidence for, either sign.
- The quotient family is *one channel's collar*, never the full vertex region; (3.13)'s
  $\mathrm{Sym}_{S_4}$ supplies three collars ($s,t,u$). So (iii) becomes: do the three
  bounded ($s\le\lambda$) collars of the $W$-cubic vertex tile $\mathcal V_{0,4}$ exactly?
  A necessary condition is that at $\lambda$ the three collars meet along the SZ boundary
  of $\mathcal V_{0,4}$ — i.e. the $W$-vertex with a tube of length $\lambda$ has the SZ
  vertex's Feynman regions as its complement. This is the closed-string Erbin–Fırat stub
  relation between two cubic vertices (030 §3.5) read backwards, and is 13b's computation.
  It also reframes the question (vi): a 2→2 gluing of two four-punctured spheres
  describes a sphere because, on the quotient, it *is* a 1→1 gluing of two three-punctured
  spheres — the pair puncture is one puncture of the quotient.

$$
\boxed{\text{(ii): }x(0,\theta)=\lambda(\tau(0,\theta))\text{ is the }|q|=1\text{ curve of the induced }W\text{-cubic vertex (3.6); its side of }\partial\mathcal V_{0,4}\text{ is fixed by the disc size }r\text{ in }\mu_0\text{ — undecided in 13a.}}
\tag{3.7}
$$



## Working notes

**Hand-off to 13b.** Inherit verbatim: the model (D4) with $z_b=-z_a$, $r_a=r_b=r$; the
Schottky uniformisation (3.1)–(3.3) and `torus_data` in the script; the quotient
description (3.6). 13b must: (1) obtain R2's SZ cubic-vertex disc at the third puncture of
$(0,\infty,u_a)$ and compare it with the induced disc $\{|W_a|<1\}=\{u=z^2:|z-z_a|<r\}$
(this decides the side in (3.7); if SZ's canonical coordinates at the harmonic point of
$\mathcal V_{0,4}$ are used for $\mu_0$, $r$ is *not* free and the comparison is a
computation); (2) compute the region swept by the three $S_4$-images of the collar
$\{x(s,\theta):s\in[0,\lambda]\}$ and test whether some $\lambda$ makes their union equal
$\mathcal V_{0,4}$ with R2's boundary (tiling test; a necessary check is that the
collar's outer curve at $s=\lambda$ coincides with R2's $|q_{SZ}|=1$ curve); (3) sewing
lift: does the (β2) fixture $b_1b_2b_1^-b_2^-\,e^{-sL_{\rm tot}+i\theta L^-_{\rm tot}}$
descend to the quotient's single neck as $b^+b^-e^{-sL_0^++i\theta L_0^-}$ of the covering
theory ($L_{\rm tot}$ on the pair = $L_0$ of the $\mathbb Z_2$-orbifold untwisted sector,
Lunin–Mathur), and where do the two unsoaked tube antighosts go? 13b should not redo §2.
Caveat for 13b: the Möbius-disc assumption in (D4) makes §3 exact; for SZ discs the
uniformisation is numerical (the criterion (2.4) is unaffected).

**Hand-off to 13c (from 13b).** Rows (v), (vi). Inherit: the quotient is a one-neck collar
of the induced $W$-cubic vertex (3.6), with R2's $X$-labelling (4.4) ($X\to1$ = $s$-channel);
verdict (iii) = no, (iv) = partial with the split of the six unsoaked antighosts as
$4$ ($\iota$-even Beltrami, two per rigid slice, sitting at the branch-point twist fields) $+\,2$
($b^\pm_{\rm rel}$, $\iota$-odd, on the neck; §5.2). For row (v): the ghost number the four
twist fields must carry follows from conservation on the quotient sphere with the neck
insertion (5.5) — the neck carries $N_{\rm gh}$ lower by $2$ than a standard propagator, and
the rigid slices contribute the four unsoaked Beltrami $b$'s; 13c should count $12$ (two
$N_{\rm gh}=2$ states per branch point pulled back) against $6$ and locate the difference in
the untwisted-sector projection of §5.1 item 1 as well. For row (vi): §3.3's reframing —
the 2→2 gluing is a 1→1 gluing of two three-punctured spheres on the quotient, the pair
puncture being one puncture of the quotient — stands; 13c should phrase it with (3.6) and
(5.4) and note that the sphere so obtained is a sphere of the *doubled* (orbifold) theory,
which is why the loop momentum $\int d^Dk_a$ of 030 §3.7.3 survives (§4.3). Loophole left
by 13b (§4.2 end): non-Möbius $\mu_0$ discs whose $z^2$-image is exactly $D_{SZ}$ — a
Cassini-type region — not excluded geometrically (row (iii) stays open there); the
loop-momentum argument (inherited from 030) closes the *objective* for any $\mu_0$, not this
geometric question.

**Failed/corrected angle (kept for the record).** The first guess
$d\,\mathrm{Im}\,\tau/ds=1/2\pi$ failed check 2e; the correct value $1/\pi$ (3.4) follows
from the $B$-cycle crossing both necks. No other check failed once the multiplier
orientation bug in the script was fixed.


## Verification

`codes/verify-chain-surfaces-covers.py` (run with `.venv/bin/python`: part 4 and part 7 import
`scipy`, absent from the system interpreter), seed 20260914, **15/15 PASS** (13a part), every
claim with a break-on-purpose leg. Evidence hierarchy for row (iii): checks 4a and 7a–7b (and
the loop-momentum argument for the objective) are decisive; 3b (limaçon not a circle) is
true but not by itself decisive, see (4.3):
- 1a: criterion (2.1)/(1.4) on 20 random slices (random fixed points $p,q$, random $z_a$;
  cross-ratio $-1$ to $10^{-10}$); break: generic slice has no swapping involution;
  uniqueness $c^2=1$.
- 1b: lift (2.3) in the model, $w_bw_{b'}=q_a$ exactly; break: $q_b\ne q_a$ violates it.
- 2a: frozen slice $|q|=1$ is a non-degenerate Schottky torus ($|\kappa|=2.7\times10^{-3}$
  at $z_a=1$, $r=0.45$).
- 2b: punctures $2,3,4$ are the three distinct non-zero half-periods relative to $1$;
  breaks: non-harmonic slice, product tube — both fail the 2-torsion test.
- 2c: direct $\wp$-lattice cross-ratio vs $\lambda(\tau)$ from `mpmath.jtheta`: in the $S_3$
  orbit to $8\times10^{-7}$; break: $\tau+0.05i$ leaves the orbit.
- 2d–2e: $\mathrm{Im}\,\tau$ increasing in $s$, $\lambda\to0$ at $s=8$, slope $1/\pi$
  (break: $1/2\pi$ fails).
**13b addendum — parts 3–5, total 43/43 PASS**, every claim with a break leg:
- 3a: $1-X_{SZ}=1/Z_4$ (R2) at 10 random $(\beta,q)$; break: wrong $\beta$.
- 3b: $\partial D_W$ not a circle (circumcircle test); break: a circle passes.
- 3c: region test $X_{SZ}(\{|q|<1\})$ validated on $|q|=0.7$ (in), $1.3$ (out).
- 3d: harmonic point $X=2$ ($Z_4=-1$) on the $s$-boundary iff $\beta=(1+\sqrt2)/2$; $X=-1$ never.
- 3e: $X_W$ from theta-function $\wp$ vs lattice $\wp$ ($<3\times10^{-3}$); break: $\tau+0.05i$.
- 3f: $X_W\to1$ at $s=5$ (labelling). 3g: nesting thresholds (4.5), definite side in both
  nested regimes, transition $r_c\in[0.472,0.550]$ at $\beta=1$ strictly inside $(r_{\rm in},r_{\rm out})$.
- 4a: no common $\lambda$ for the two real crossings at three $(\beta,r)$; set-distance $0.52$
  at the matched $\lambda$; break: $\partial F_s$ against itself $<10^{-2}$.
- 4b: no seam on the real axis ($0.074$, $0.126$); break: $(x,1-x)$ passes.
- 5a–5c: Grassmann representation (Jordan–Wigner, 16-dim); (5.2), (5.3) with sign; breaks:
  wrong sign fails; non-vacuity ($\mathcal F\ne0$).
**13c addendum — part 6, total 59/59 PASS** (exact rational arithmetic, `fractions`):
- 6a: torus balance (6.1); break: seven antighosts.
- 6b: quotient balance (6.2) solved for $N_{\rm gh}(\sigma)$: $3$ under (B), $3/2$ under (A);
  difference $6$ split $2+4$.
- 6c: $h(q)$ from $h(c)=-1$, $h(b)=2$ alone reproduces the independent datum
  $h(e^{3\sigma})=0$ and $Q=-3$; break: a $\lambda=1$ system fails.
- 6d: half-integer minimiser $q=3/2$, $h=-9/8$, strict (neighbours at $-5/8$).
- 6e: match $2q_\sigma=N_{\rm gh}(\sigma)$ under (B); $3/2\notin\mathbb Z$; per-chirality
  $6=2\times3$; breaks: $\lambda=1$ ghosts ($q=1/2$) and a wrong saturation $6$ both fail.
**13d addendum — part 7, total 69/69 PASS** (critic 031, Routing item 1):
- 7a: scan $r\in[0.30,0.95]$ (27 points) at $\beta\in\{0.75,1,(1+\sqrt2)/2,1.5,2,3\}$ ($\beta$ is
  a free parameter of $\mathcal V_3'$, so a range, not a value): where both real crossings
  exist, the ratio $\lambda_\pi/\lambda_0$ of the two crossing-$\lambda$'s is $<1$ at every
  point (max $0.46$–$0.99$, rising with $\beta$); it never reaches $1$; break: a stubbed SZ
  coordinate gives ratio $1$ to $10^{-10}$.
- 7b: relative set-distance of 4a (divided by the diameter of R2's curve) is $r$-independent
  ($r=0.6$ vs $0.95$ to $10^{-6}$) and equals $0.20,\,0.037,\,0.015,\,0.005$ at
  $\beta=1,2,3,5$: $O(1)$ at $\beta=O(1)$, decreasing monotonically, below $10^{-2}$ at
  $\beta=5$ (degenerate limit, R2's curve collapses to $X=1$). The mismatch is not uniform in
  $\beta$; no sampled point reaches a match.
Not machine-checked (13c): the covering dictionary; the identification of the ghost twist
field with the antiperiodic ground state (6.4) (standard CFT, from memory); the descendant
relabelling of §6.1. Dimensional check: ghost numbers and charges are dimensionless integers
or half-integers. Limiting case: setting the twist fields aside recovers the torus count (6.1).

Not machine-checked (13b): the exact tiling (only necessary conditions (A),(B)); overlap of
the three collars; the covering dictionary of §5.1 (Lunin–Mathur, operator argument); the
Cassini loophole (§4.2 end). Limiting cases: $s\to\infty$ gives $X\to1$ in both
constructions (3f, and (4.4) at $q\to0$).

Not machine-checked (13a): the extremal-length constant $C(\mu_0)$ of §2.3 (argument only); the
dimension count of §2.3. Dimensional
check: all quantities are dimensionless moduli. Limiting case: $s\to\infty$ reproduces the
$s$-channel degeneration $x\to0$ and the two-necks-in-series length $2s$.


## 4. The quotient family against $\mathcal V_{0,4}$ (13b)

**Literal task (13b).** Fill rows (iii), (iv): compare the induced disc of (3.6) with R2's
SZ disc at the third puncture (side of the frozen curve, §4.1); test whether the three
$S_4$-images of the collar $\{x(s,\theta):s\in[0,\lambda]\}$ tile $\mathcal V_{0,4}$ with
R2's boundary (§4.2); decide whether the (β2) fixture descends to a one-neck propagator on
the quotient (§5). **Objective served.** Second half of Q13: is the quotient family the
$\mathcal V_{0,4}$ region with R2's boundary? "No" excludes fixture (β) as a
representation of the $V_4$ theory; "yes" makes it a construction.

### 4.1 R2's SZ disc vs the induced disc

**R2's data in the $u$-coordinate.** The quotient sphere $(0,\infty,u_a)$ of (3.6) is
Möbius-equivalent to SZ's $\mathcal V_3'$ sphere $(0,\infty,1)$ by $\zeta=u/u_a$ (the only
Möbius maps fixing $0,\infty$ are dilations, so this is forced up to the phase of the
local coordinate). The special-puncture coordinate of $\mathcal V_3'$ is
$f_1'(w)=(2\beta-w)/(2\beta+w)$ (overview eq. (V3primemaps), $\beta'=\beta$), i.e.
$$
w_{SZ}(u)=2\beta\,\frac{u_a-u}{u_a+u},\qquad
D_{SZ}:=\{|w_{SZ}|<1\}=\Big\{\frac{|u-u_a|}{|u+u_a|}<\frac1{2\beta}\Big\},\quad \beta>\tfrac12 ,
\tag{4.1}
$$
an Apollonian disc about $u_a$ — a **round** disc in $u$ (its boundary is a circle, since
$w_{SZ}$ is Möbius). The one-neck plumbing $w_{SZ}w'_{SZ}=q$ of two such spheres is R2's
$s$-channel family, $|q|=1$ being $\partial\mathcal V_{0,4}$ in that channel (R2, eq. (Z4)).

**The induced disc.** From (3.6), $W_a=w_a\circ\sqrt{\cdot}$ on the image of the $a$-disc:
$$
D_W:=\{|W_a|<1\}=\{u=z^2:\ |z-z_a|<r\},\qquad \partial D_W=\{(z_a+re^{i\phi})^2\},
\tag{4.2}
$$
whose boundary is the image of a circle not centred at $0$ under $z\mapsto z^2$: a limaçon
of Pascal, **never a circle** for $r>0$ (a circle $|z-z_a|=r$ maps to a circle under $z^2$
only if $z_a=0$; here $0<r<|z_a|$). Hence, for every $r$ and every $\beta$,
$$
D_W\neq D_{SZ}\quad\text{(proven; limaçon vs circle).}
\tag{4.3}
$$
**What (4.3) does and does not imply.** Different discs do *not* by themselves imply that
the $|q|=1$ curves differ: the plumbed cross-ratio $X(q)=W^{-1}(q/W(0))/W^{-1}(q/W(\infty))$
depends on the univalent $W^{-1}$ only through its values on two circles, and two different
univalent maps can agree there (equal discs $\Rightarrow$ equal curves holds, by the Riemann
mapping theorem up to rotation; the converse used in an earlier version of this record does
not follow). Whether $x(0,\theta)$ lies on $\partial\mathcal V_{0,4}$ as a curve is therefore
decided by the direct test of §4.2 (condition (A), script 4a and 7a): numerically no at the
sampled $(\beta,r)$, with the caveats stated there. Note also that R2's $\beta$ is a free
parameter of the $\mathcal V_3'$ family ($\beta'>\tfrac12$, overview eq. (V3primemaps)); R2's
boundary match holds for every $\beta'=\beta$, so there is no single "physical" $\beta$ to
sample and the statements below are made over a stated range.

**Is $r$ fixed?** The brief's conditional — "if $\mu_0$ uses SZ's canonical coordinates at
the harmonic point of $\mathcal V_{0,4}$" — does not fix $r$ on its own: SZ's canonical
coordinates are defined on $\partial\mathcal V_{0,4}$ (induced by the plumbing of two
$\mathcal V_3'$), and the harmonic locus $(1,2;a,b)=-1$ meets R2's $s$-channel boundary curve
only for the special value $\beta=(1+\sqrt2)/2$ (the harmonic point is $Z_4=-1$, i.e.
$X=2$ in (4.4); $X_{SZ}(\beta,q=-1)=\big((4\beta^2+1)/(4\beta^2-1)\big)^2=2$ iff
$4\beta^2=(1+\sqrt2)^2$; script 3d); the discs induced there at $a,b$ are moreover not Möbius in $z$, so the
model (D4) does not literally apply. In the interior of $\mathcal V_{0,4}$ the minimal-area
coordinates are not available in closed form. **Conclusion: $r$ remains a parameter of
$\mu_0$**; §4.1 therefore decides the side of $x(0,\theta)$ *as a function of $r$* (at fixed
$\beta$), which is enough for row (iii) because the direct test of §4.2 is itself run over $r$ (script 7a).

**Nesting.** $D_W\subset D_{SZ}$ iff $\max_{|z-z_a|=r}2\beta\,|z^2-z_a^2|/|z^2+z_a^2|\le1$;
$D_{SZ}\subset D_W$ iff the reverse inequality with min. Between the two thresholds
$r_{\rm in}(\beta)<r<r_{\rm out}(\beta)$ the boundaries cross and the frozen curve
$x(0,\theta)$ crosses $\partial\mathcal V_{0,4}$: partly in the $s$-channel Feynman region,
partly inside $\mathcal V_{0,4}$. Nesting is a *sufficient* condition for a definite side
(a smaller disc at fixed $|q|$ is a longer effective tube). The exact side test is done in
the moduli plane (script part 3): $X_W(0,\theta)$ against the region $X_{SZ}(\{|q|<1\})$,
with the common labelling $1=0,\ 2=\infty$ on sphere 1, $3,4$ = images of $0',\infty'$ of
sphere 2, and $X:=(1,2;3,4)$, so that $X\to0$ is the $s$-channel degeneration in both
constructions. 

**The two cross-ratios (script part 3).** SZ plumbing: sphere-2 punctures $0',\infty'$ land
at $u=u_a(4\beta^2\mp q)/(4\beta^2\pm q)$, so
$$
X_{SZ}(q)=\Big(\frac{4\beta^2-q}{4\beta^2+q}\Big)^2,\qquad 1-X_{SZ}(q)=\frac{16\beta^2q}{(4\beta^2+q)^2}=\frac1{Z_4(q)}
\tag{4.4}
$$
with R2's $Z_4$ (check 3a): the $s$-channel degeneration is $X\to1$ ($3,4$ collide), and the
$s$-channel Feynman region is $X_{SZ}(\{|q|<1\})$, whose membership is decided exactly by
inverting (4.4) ($q=4\beta^2(1\mp\sqrt X)/(1\pm\sqrt X)$; $q\mapsto X$ is injective on the
unit disc since its second preimage is $16\beta^4/q$; validated on known-$|q|$ points, 3c).
Cover side: $X_W(s,\theta)=(P_2-P_4)/(P_2-P_3)$, $P_i=\wp(u_i-u_1)$ from theta functions
(agrees with the lattice $\wp$ of §3 to $<3\times10^{-3}$, 3e; $X_W\to1$ as $s\to\infty$, 3f).
(4.4) also shows the harmonic point $Z_4=-1$ ($X=2$) is on R2's $s$-boundary iff
$\beta=(1+\sqrt2)/2$, and its $S_3$ companion $X=-1$ never is (3d).

**Nesting thresholds and side (3g), $z_a=1$.**
$$
\begin{array}{c|cc|c}
\beta & r_{\rm in} & r_{\rm out} & \text{side of }x(0,\theta)\\ \hline
0.75 & 0.532 & \text{none }(<1) & \text{Feynman for } r\le0.6;\ \mathcal V_{0,4}\text{ at } r=0.8\\
1 & 0.420 & 0.732 & \text{Feynman for } r\le0.472;\ \text{mixed at } r\in[0.498,0.524];\ \mathcal V_{0,4}\text{ for } r\ge0.55\\
1.207 & 0.356 & 0.554 & \text{Feynman for } r\le0.3;\ \mathcal V_{0,4}\text{ for } r\ge0.45\\
1.5 & 0.293 & 0.414 & \text{Feynman for } r\le0.3;\ \mathcal V_{0,4}\text{ for } r\ge0.45
\end{array}
\tag{4.5}
$$
Nesting is sufficient (both nested regimes give a definite side, 3g), and the transition
$r_c(\beta)$ lies strictly between the thresholds, with a narrow window of $r$ (width
$\lesssim0.05$ at $\beta=1$) where the frozen curve **crosses** $\partial\mathcal V_{0,4}$
(fraction of sampled $\theta$ inside the Feynman region $0.56\to0.33$). So the answer to
(3.7) is: **inside the $s$-channel Feynman region for $r<r_c(\beta)$, inside
$\mathcal V_{0,4}$ for $r>r_c(\beta)$, crossing in a thin window; on the boundary as a curve at
no sampled $(\beta,r)$ (numerical, §4.2 / script 4a, 7a).**
In the $V_4$ theory $r$ is not a free knob — it is whatever $\mu_0$'s local coordinates at
$a,b$ are — but at no sampled $r$ does the frozen curve coincide with R2's boundary (§4.2, script 7a).

### 4.2 The collar and the tiling test

**Geometry of the collar.** In the $X=(1,2;3,4)$ labelling of (4.4) the $s$-channel
degeneration is $X=1$ and R2's $s$-channel Feynman region $F_s=X_{SZ}(\{|q|<1\})$ is a
neighbourhood of $X=1$ bounded by the closed, reflection-symmetric curve
$X_{SZ}(e^{i\theta})$, crossing the real axis at $X_{SZ}(1)=\big(\frac{4\beta^2-1}{4\beta^2+1}\big)^2<1$
and $X_{SZ}(-1)>1$. The quotient collar $C_s(\lambda)=\{X_W(s,\theta):0\le s\le\lambda\}$ runs
from the frozen curve ($s=0$) *towards* $X=1$ ($s\to\infty$, check 3f); its two boundary
curves are the frozen curve and the $s=\lambda$ curve. Its $S_4$-images $C_t,C_u$ are the
$S_3$-images of $C_s$ in the $X$-plane (about $X=0$ and $X=\infty$). Since
$\mathcal V_{0,4}=\mathbb{CP}^1\setminus(F_s\cup F_t\cup F_u)$ (R2), the union of the three
collars can equal $\mathcal V_{0,4}$ only if

- **(A)** the $s=\lambda$ curve of $C_s$ is exactly $\partial F_s$, i.e. $X_W(\lambda,\theta)$
  and $X_{SZ}(e^{i\theta'})$ coincide as sets, and
- **(B)** the three frozen curves are the internal seams of the tiling — every point of the
  $s$-frozen curve lies on the $t$- or $u$-frozen curve (no gap, no overlap).

**(A) fails (script 4a).** Both curves are symmetric under $\theta\to-\theta$ (complex
conjugation), so each crosses the real axis exactly at $\theta=0$ and $\theta=\pi$; equality
as sets requires $X_W(\lambda,0)=X_{SZ}(1)$ *and* $X_W(\lambda,\pi)=X_{SZ}(-1)$ for the same
$\lambda$. At $z_a=1$:
$$
\begin{array}{c|c|cc|cc|c}
\beta & r & X_W(0,0) & X_W(0,\pi) & X_{SZ}(1) & X_{SZ}(-1) & \lambda \text{ solving }\theta=0\ /\ \theta=\pi\\ \hline
1 & 0.45 & 0.403 & 2.094 & 0.360 & 2.778 & \text{none / none}\\
1 & 0.6 & 0.164 & 3.446 & 0.360 & 2.778 & 0.472\ /\ 0.217\\
1.5 & 0.3 & 0.686 & 1.412 & 0.640 & 1.5625 & \text{none / none}
\end{array}
\tag{4.6}
$$
For $r<r_c(\beta)$ (frozen curve already inside $F_s$, §4.1) no $\lambda\ge0$ reaches
$\partial F_s$ at all — the collar moves deeper into $F_s$ as $\lambda$ grows. For
$r>r_c(\beta)$ the two crossings are matched by *different* $\lambda$ (ratio $\approx2.2$ at
$\beta=1$, $r=0.6$), and at the $\theta=0$-matched $\lambda=0.472$ the set-distance between
$X_W(\lambda,\theta)$ and $\partial F_s$ reaches $0.52$ (break leg: $\partial F_s$ against
itself, $<10^{-2}$). Hence there is no $\lambda$ with $\partial_{s=\lambda}C_s=\partial F_s$
for any of the sampled $(\beta,r)$; at $\beta=O(1)$ the mismatch is $O(1)$, not a tuning
issue. **Scan over $r$ (script part 7, 13d).** Over $r\in[0.30,0.95]$ (27 points) at
$\beta\in\{0.75,1,(1+\sqrt2)/2,1.5,2,3\}$: where both real crossings exist ($r>r_c(\beta)$),
the ratio $\lambda_\pi/\lambda_0$ of the two crossing-$\lambda$'s stays strictly below $1$ at
every sampled point (max $0.46,0.82,0.90,0.95,0.98,0.99$ respectively, at $r=0.95$); it
never reaches $1$ (break leg: a stubbed SZ coordinate $e^{\lambda/2}w_{SZ}$ gives ratio $1$
to $10^{-10}$). The ratio does, however, tend to $1$ as $\beta$ grows: the relative set
distance of 4a (distance divided by the diameter of R2's curve, $r$-independent because $r$
only shifts the matched $\lambda$) is $0.20,\ 0.037,\ 0.015,\ 0.005$ at $\beta=1,2,3,5$
(7b). Large $\beta$ is the degenerate limit in which R2's curve collapses to the point
$X=1$ and both constructions approach the $s$-channel degeneration, so the mismatch is
$O(1)$ for $\beta=O(1)$ but **not uniform in $\beta$**; a general proof that
$\partial_{s=\lambda}C_s\neq\partial F_s$ for all $(\beta,r)$ is not supplied here. What the
numbers show is that the $s=\lambda$ curve, the $|q|=e^{-\lambda}$ curve of the *$W$-vertex*,
is not the curve of a stubbed SZ coordinate $e^{\lambda/2}w_{SZ}$ at any sampled $(\beta,r)$
— the Erbin–Fırat stub relation of §3.3 has no solution there; that $W$ is non-Möbius
(limaçon disc (4.2)) is consistent with this but does not prove it, see (4.3).

**(B) fails on the real axis (script 4b).** The $s$-frozen curve meets $\mathbb R$ at
$a=X_W(0,0)$, $c=X_W(0,\pi)$; the $t$/$u$-frozen curves meet $\mathbb R$ at the $S_3$-images
of $a,c$. A seam through the real crossings requires $c\in S_3\cdot a$ (or $a\in S_3\cdot c$):
the minimal distance is $0.074$ ($r=0.45$) and $0.126$ ($r=0.6$) — no seam (break leg: a
genuine pair $(x,1-x)$ passes). Overlap/gap of the three collars away from the real axis was
not tested (not needed: (A) alone is decisive).

**What remains untested.** The exact tiling (area or winding test) was not run; (A) is a
necessary condition; for $r<r_c(\beta)$ it is vacuous (the collar never reaches $\partial F_s$),
and for $r>r_c$ it fails at every sampled $(\beta,r)$ of the part-7 scan ($\beta\in[0.75,3]$,
$r\in[0.3,0.95]$; relative mismatch $O(1)$ at $\beta=O(1)$, not uniform in $\beta$). Not sampled: $z_a\ne1$ (a dilation, no loss), non-Möbius discs in $\mu_0$
(D4 caveat) — for those the induced disc is still the $z^2$-image of an $\iota_1$-symmetric
disc, hence still not the round $D_{SZ}$ unless the disc in $z$ is itself the preimage of a
round disc, i.e. $\{|z^2-u_a|/|z^2+u_a|<1/2\beta\}$, a *Cassini-type* region which is not a
local-coordinate disc of the form (1.3); whether a minimal-area $\mu_0$ could produce exactly
that region is the only loophole, and it would need the $V_4$ vertex's coordinates at $a,b$
to know about SZ's $\beta$.

### 4.3 Verdict on row (iii)

**No — numerically supported (Möbius-disc model, sampled $(\beta,r)$).** The quotient family
$\{\Sigma_{1,4}(s,\theta)/\iota\}$ is a one-neck collar of the induced $W$-cubic vertex whose
disc (4.2) is a limaçon, never SZ's round disc (4.1) (proven, (4.3)); this by itself does not
decide whether the $|q|=1$ curves coincide. The direct test does: for $r<r_c(\beta)$ the
collar never reaches $\partial F_s$ (solid); for $r>r_c(\beta)$ the necessary condition (A)
fails at every sampled $(\beta,r)$ — the two crossing-$\lambda$'s never coincide (ratio $<1$
over the $r$ scan, script 7a), with an $O(1)$ relative mismatch at $\beta=O(1)$ that shrinks in
the degenerate large-$\beta$ limit (7b) — and the frozen curves do not seam (B). The union of
the three $S_4$-images is therefore not $\mathcal V_{0,4}$ with R2's boundary at the sampled
points — for $r<r_c(\beta)$ it lies entirely inside the Feynman regions, for $r>r_c(\beta)$ it
is a proper sub-collar of $\mathcal V_{0,4}$ with the wrong inner boundary. A proof for all
$(\beta,r)$ and for non-Möbius $\mu_0$ discs (the Cassini loophole, §4.2 end) is open; the
conclusion that the (β) double-strand fixture is not a representation of the $V_4$ theory
does not rest on it (loop momentum, below).
$$
\boxed{\text{(iii): no, numerically. }\ \partial_{s=\lambda}C_s\neq\partial\mathcal V_{0,4}\ \forall\lambda\ \text{at all sampled }(\beta,r)\ (\beta\in[0.75,3],\ r\in[0.3,0.95]);\ D_W\neq D_{SZ}\ \text{proven but not sufficient.}}
\tag{4.7}
$$

**The loop-momentum route (inherited from 030 §3.7.3, §6.1; only sketched here).** Two
statements must be kept apart. (1) *The objective* — is the (β2) composite the $V_4$
integrand? — is closed by the loop momentum, independently of any local-coordinate data: the
composite contains $\int d^Dk_a$ over the pair's relative momentum ($k_b=-k_1-k_2-k_a$), a
genuine torus loop momentum producing pair-channel thresholds in the external momenta, while
the tree-level $\mathcal V_{0,4}$ integrand at fixed $\mu$ is a finite sum with no such
analytic structure; in the words of §7, the doubled theory's tree amplitude is not the single
theory's $V_4$. That argument needs neither $\beta$ nor $r$ nor the uniformisation of §3, and
it holds for any $\mu_0$, Möbius discs or not. (2) *The geometric question of row (iii)* —
does the quotient *family* coincide with $\mathcal V_{0,4}$? — is **not** closed by it: for
Möbius discs the answer is no, numerically (§4.2); for a non-Möbius (Cassini-type) $\mu_0$
the geometric question stays open. The loop momentum makes that loophole irrelevant to the
objective, not closed. What the present
computation adds is the *geometric* reason and its precise location: the quotient is a
legitimate one-neck cubic-vertex collar (so "genus" is not the obstruction — the cover is
genuinely a sphere), but of the wrong vertex ($W\neq w_{SZ}$) and covering only collars, not
the vertex region; and the correlator-level loop momentum reappears on the quotient as the
neck sum over the *untwisted sector of the doubled theory* rather than over a single copy
(§5.1), which is where the extra $\int d^Dk$ lives.


## 5. The sewing lift (13b)

### 5.1 Descent of the (β2) fixture

**Setup.** On the pair space $\mathcal S_{\rm pair}$ write $b_i^\pm:=b_0^{\pm(i)}$,
$L_i^\pm:=L_0^{\pm(i)}$, $i=1,2$ for the two strands ($a$ and $b$ necks), and
$$
L_{\rm tot}^\pm=L_1^\pm+L_2^\pm,\qquad b_{\rm tot}^\pm=b_1^\pm+b_2^\pm,\qquad b_{\rm rel}^\pm=b_1^\pm-b_2^\pm .
\tag{5.1}
$$
The (β2) fixture (030 §5.3, D3) is $\mathcal F_{\beta2}=b_1^+b_2^+b_1^-b_2^-\,e^{-sL^+_{\rm tot}+i\theta L^-_{\rm tot}}$,
integrated over $s\in[0,\lambda]$, $\theta\in S^1$, with $b(\partial_s)=b^+_{\rm tot}$,
$b(\partial_\theta)=b^-_{\rm tot}$ the soaked pair. Ghost algebra: $\{b_i^\pm,b_j^\pm\}=0$,
so $(b^\pm_{\rm tot})^2=(b^\pm_{\rm rel})^2=0$ and
$$
b_1^\pm b_2^\pm=\tfrac14(b^\pm_{\rm tot}+b^\pm_{\rm rel})(b^\pm_{\rm tot}-b^\pm_{\rm rel})
=-\tfrac12\,b^\pm_{\rm tot}\,b^\pm_{\rm rel},
\tag{5.2}
$$
hence, with one transposition ($b^+_{\rm rel}$ past $b^-_{\rm tot}$),
$$
\mathcal F_{\beta2}=\tfrac14\;b^+_{\rm tot}b^+_{\rm rel}\;b^-_{\rm tot}b^-_{\rm rel}\;e^{-sL^+_{\rm tot}+i\theta L^-_{\rm tot}}
=-\tfrac14\;b^+_{\rm tot}b^-_{\rm tot}\;b^+_{\rm rel}b^-_{\rm rel}\;e^{-sL^+_{\rm tot}+i\theta L^-_{\rm tot}}
\tag{5.3}
$$
(script 5c; the first attempt had $+\tfrac14$ in the second ordering, caught by the check).

**Covering dictionary.** The quotient neck of (3.6) is a single tube of the $\mathbb Z_2$
orbifold of two copies of the worldsheet CFT (Lunin–Mathur, hep-th/0006196): the involution
swaps the two necks without fixed points on them, so the quotient neck carries the
*untwisted* sector, states of $(\mathcal H\otimes\mathcal H)^{S_2}$, with
$L_0^{\rm orb,\pm}=L^\pm_{\rm tot}$ and ghost zero modes $b_0^{{\rm orb},\pm}=b^\pm_{\rm tot}$
(the $S_2$-even combinations of the parent fields' zero modes; the twisted sectors live at
the branch points $1,2,3,4$ and are 13c's twist fields). Therefore the exponential and the
soaked pair in (5.3) descend **exactly** to the standard one-neck integrand of the covering
theory,
$$
b^+_{\rm tot}b^-_{\rm tot}\,e^{-sL^+_{\rm tot}+i\theta L^-_{\rm tot}}
=b_0^{{\rm orb},+}b_0^{{\rm orb},-}\,e^{-sL_0^{{\rm orb},+}+i\theta L_0^{{\rm orb},-}} ,
\tag{5.4}
$$
which is the numerator of $b_0^+b_0^-\,(1-e^{-\lambda L_0^+})/L_0^+\,\delta_{L_0^-,0}$ after
the $(s,\theta)$ integral — a stubbed propagator of length $\lambda$ on the quotient's single
neck (consistent with §3.3: the quotient family is a one-neck Feynman collar).

Two discrepancies with a *standard* one-neck propagator of the orbifold survive:

1. **The state space of the neck sum.** The pair space is $\mathrm{Sym}^2\mathcal H_0$
   (per-strand level matching $L_1^-=L_2^-=0$, the project conventions; 020 (1.a): each
   $\omega_1^{-1}$ carries its own $b_0^-\delta_{L_0^-,0}$), whereas the orbifold's untwisted
   neck sum runs over $(\mathcal H\otimes\mathcal H)^{S_2}\cap\ker L^-_{\rm tot}$, which
   contains states with $L_1^-=-L_2^-\neq0$. The descended propagator is the orbifold
   propagator *projected* onto $\mathcal H_0\otimes\mathcal H_0$: a proper sub-sum. (Its
   $\int d^Dk_a$ over the relative momentum — 030 §3.7.3 — is the orbifold's untwisted
   two-copy momentum sum; on a single-copy sphere it has no counterpart.)
2. **The factor $b^+_{\rm rel}b^-_{\rm rel}$** — §5.2.

### 5.2 The two unsoaked tube antighosts

By (5.3) the two unsoaked tube antighosts of D3 are exactly $b^\pm_{\rm rel}=b_1^\pm-b_2^\pm$,
the zero modes of the $S_2$-**odd** combination $b^{(1)}(w)-b^{(2)}(w)$ of the two ghost
fields. On the covering torus they are the Beltrami antighosts of the *relative* neck
deformations $\delta(s_a-s_b)$, $\delta(\theta_a-\theta_b)$ — the two moduli of
$\mathcal M_{1,4}$ that the diagonal tube freezes and that break $\iota$ (§2.3): they are
$\iota$-odd deformations, so on the quotient they are **not moduli at all** (the
$\iota$-invariant deformations of $\Sigma_{1,4}$ are the deformations of the quotient
sphere with its four branch points, $\dim_{\mathbb C}=1$, swept by $(s,\theta)$). On the
quotient, $b^+_{\rm rel}b^-_{\rm rel}$ is therefore an $S_2$-even bilinear in the odd ghost
field's zero modes, inserted in the neck: a legitimate operator of the orbifold CFT (even
under the orbifold projection, so it acts within the untwisted sector), but **not part of
any propagator** — it multiplies the standard numerator (5.4), lowering the ghost number
carried by the neck by $2$ relative to a one-neck propagator (physical grading: $N_{\rm gh}(b)=-1$).
By ghost-number conservation on the quotient sphere, the four twist-field insertions at the
branch points must carry $+2$ more than four ordinary $N_{\rm gh}=2$ external states would,
which is the tube contribution to the $6$-vs-$12$ count of row (v): the six unsoaked
antighosts of D3 split as $4$ (Beltrami, two per rigid slice, $\iota$-even, attached to the
branch-point twist fields) $+\,2$ ($b^\pm_{\rm rel}$, $\iota$-odd, attached to the neck).
The only way to absorb $b^\pm_{\rm rel}$ into a propagator would be to *integrate* the
relative moduli — i.e. the product tube (β1) — which destroys $\iota$ (row (i)).

### 5.3 Verdict on row (iv)

**Partially: the (β2) fixture descends to the quotient neck as
$-\tfrac14\,b^+_{\rm rel}b^-_{\rm rel}\times[\text{standard stubbed one-neck propagator of the
$\mathbb Z_2$-orbifold untwisted sector, projected onto $\mathcal H_0\otimes\mathcal H_0$}]$,
(5.3)–(5.4) — the exponential and the soaked pair lift exactly, $L_{\rm tot}=L_0^{\rm orb}$.**
It is **not** a standard one-neck propagator of the covering theory: the extra even bilinear
$b^+_{\rm rel}b^-_{\rm rel}$ (zero modes of the $S_2$-odd ghost, antighosts of the frozen
$\iota$-odd relative-neck moduli) has no propagator interpretation on the quotient, and the
neck sum is a proper sub-sum of the orbifold's untwisted sector.
$$
\boxed{\text{(iv): }\mathcal F_{\beta2}\ \downarrow\ -\tfrac14\,b^+_{\rm rel}b^-_{\rm rel}\;b_0^{{\rm orb},+}b_0^{{\rm orb},-}e^{-sL_0^{{\rm orb},+}+i\theta L_0^{{\rm orb},-}}\big|_{\mathcal H_0\otimes\mathcal H_0}\ \ (\text{exact lift of the soaked part; non-standard by } b^\pm_{\rm rel}\text{ and the projection}).}
\tag{5.5}
$$
Machine check: (5.2)–(5.3) are Grassmann algebra (four anticommuting generators); checked
in script part 5 (exterior-algebra matrices) — see Verification.


## 6. The twist-field ghost count (13c)

**Literal task (13c).** Fill rows (v) and (vi) of §0: decide which of 030 §6.1's two
readings of the six unsoaked antighosts the (β2) fixture realises, run the ghost-number
balance on the quotient sphere of the doubled theory, compare with the bosonised $\mathbb Z_2$
twist field of the antiperiodic $\lambda=2$ $bc$ system, and answer the question of §7.
**Objective served.** Say *why* Q13 is "no" in the covering language (is the anomaly
mismatch $6$ vs $12$ an independent "no", or is the covering bookkeeping consistent and the
obstruction purely geometric, as §4.3 anticipated?).

Conventions: physical ghost grading of 030 §1.1 ($N_{\rm gh}(b)=-1$, $N_{\rm gh}(c)=+1$,
holomorphic and antiholomorphic added), sphere saturation $6$ per copy of the worldsheet
CFT, torus saturation $0$; the doubled theory has two copies, so its sphere saturation is
$12$. Inherited verbatim: (3.6), (4.4), (5.3), (5.5), the split $4+2$ of §5.2.

### 6.1 The two readings

030 §6.1 left open which of two readings applies to the six unsoaked antighosts of the
(β2) fixture (four Beltrami $b$'s of the two rigid slices $\Omega_{V_4}(\mu_0)$, two tube
antighosts beyond the soaked pair):

- **(A)** they are absorbed into the four twist-field vertex operators at the branch points
  $1,2,3,4$, which then carry total $N_{\rm gh}=6$ ($3/2$ each);
- **(B)** they remain separate insertions on the cover (equivalently on the quotient), and
  the twist fields carry total $N_{\rm gh}=12$ ($3$ each).

**What 13b's split says.** By (5.3) the two unsoaked tube antighosts are $b^\pm_{\rm rel}=
b_0^{\pm(1)}-b_0^{\pm(2)}$, zero modes of the $S_2$-odd ghost field on the quotient *neck*
(§5.2). The neck of (3.6) is a tube on which $\iota$ acts freely, so it carries the
untwisted sector; $b^+_{\rm rel}b^-_{\rm rel}$ is an $S_2$-even bilinear acting within that
sector, inserted in the neck, at finite distance (in the plumbing coordinate) from all four
branch points. It is not a mode of any operator at a branch point and cannot be moved there
without crossing the neck sum, which is over states, not over a vacuum. **These two are
therefore reading (B): separate insertions.** They lower the ghost number carried by the
neck by $2$ relative to the standard one-neck propagator (5.4).

The four Beltrami antighosts $b(\partial_{\mu_1})b(\partial_{\mu_2})$ per rigid slice are
$\iota$-even (§5.2: they are the antighosts of the deformations of the pair position $u_a$
in the quotient sphere $(0,\infty,u_a)$, which is $\iota$-invariant). On the quotient
three-punctured sphere the position of the third puncture is not a modulus (Möbius); a
Beltrami differential $\mu=\bar\partial v$ of a Möbius deformation gives, by the usual
contour argument, $\int\mu\,b=\oint v\,b$ acting on the insertions it encloses — here the
two twist fields at $u=0,\infty$ and the pulled-back external states. So each Beltrami
$b$ can be *written* as a $b$-mode descendant of a branch-point twist field (a dressed
field $b_{-n}\sigma$, $N_{\rm gh}$ lower by $1$) or left as an insertion; the two
descriptions are the same operator and the same total ghost number. Reading (A) is thus
available for these four as a *relabelling*, but it changes nothing in the balance: the
dressed field has $N_{\rm gh}(\sigma)-1$, and the bare twist field's ghost number is what
the CFT fixes (§6.2), not what one chooses to attach to it.

**Consequently the (β2) fixture realises reading (B)**: all eight antighosts of the torus
measure (two soaked, six unsoaked) are insertions of the covering theory on the quotient,
$4$ at (or attributable to) the branch points and $4$ on the neck ($b^\pm_{\rm tot}$ soaked,
$b^\pm_{\rm rel}$ unsoaked); the twist fields are the bare $\mathbb Z_2$ twist fields of the
doubled ghost system. Reading (A) as stated in 030 — six units *inside* four local
operators, $3/2$ each — is not realisable by any operator of the doubled theory: a twist
field is antiperiodic for $b^-c^-$ in *both* chiralities ($\iota$ is holomorphic and acts on
$z$ and $\bar z$ alike), so its holomorphic and antiholomorphic ghost charges are both in
$\tfrac12+\mathbb Z$ and their sum is an integer; $3/2$ is excluded. 030 §6.1 did not assert
$6$: it posed readings (A) (six antighosts absorbed into the twist-field operators, total $6$,
$3/2$ each) and (B) (they remain insertions, total $12$, $3$ each) and asked which applies.
The answer: reading (A), left open by 030, is inadmissible as stated ($3/2\notin\mathbb Z$);
(B) applies. Its all-six form is what is excluded: a *partial* (A) — the four Beltrami $b$'s
absorbed into the branch-point operators (the relabelling above, dressed fields with
$N_{\rm gh}=2$) and the two neck antighosts left on the neck — is realisable with total $8$
($2$ each, integer) and is the same count in different bookkeeping.

### 6.2 Conservation on the quotient sphere

**Torus side (input, 030 §3.7.3).** $\Sigma_{1,4}(s,\theta)$ carries four external states,
$N_{\rm gh}=2$ each, and eight antighosts; torus saturation is $0$:
$$
4\cdot2-8=0 .
\tag{6.1}
$$

**Quotient side.** By (3.6) and (5.5) the same correlator is a sphere correlator of the
$\mathbb Z_2$ orbifold of two copies of the worldsheet CFT (Lunin–Mathur), with: the four
pulled-back external states ($+8$: pull-back does not change the ghost number of a
state), the neck insertion (5.5) — standard soaked pair $b^\pm_{\rm tot}$ ($-2$) and the
extra $b^\pm_{\rm rel}$ ($-2$) —, the four Beltrami antighosts of the rigid slices
($-4$, kept as insertions per §6.1), and four twist fields $\sigma_i$ at the branch points.
Sphere saturation of the doubled theory is $12$, so conservation forces
$$
8-2-2-4+\sum_{i=1}^4N_{\rm gh}(\sigma_i)=12
\quad\Longrightarrow\quad
\sum_iN_{\rm gh}(\sigma_i)=12,\qquad N_{\rm gh}(\sigma)=3\ \text{each}.
\tag{6.2}
$$
Under reading (A) the six unsoaked $b$'s are inside the $\sigma_i$ and the same equation
reads $8-2+\sum_iN_{\rm gh}(\sigma_i^{\rm (A)})=12$, i.e. $6$ total, $3/2$ each — 030's
number. The difference $12-6=6$ is exactly the six unsoaked antighosts; on the (β2)
quotient it sits in two places: $4$ at the branch points (Beltrami $b$'s) and $2$ on the
neck ($b^\pm_{\rm rel}$). The neck part is the same object as the projection of §5.1
item 1: $b_1^-b_2^-=-\tfrac12b^-_{\rm tot}b^-_{\rm rel}$ by (5.2), and the two per-strand
factors $b_0^{-(i)}$ are what project the neck sum onto $\mathcal H_0\otimes\mathcal H_0$
(each strand's $\omega_1^{-1}=b_0^-\delta_{L_0^-,0}$, R27 RS4); the orbifold's own
propagator supplies only $b^-_{\rm tot}$, so $b^-_{\rm rel}$ *is* the projection beyond the
untwisted-sector sum, and item 1 and item 2 of §5.1 are one discrepancy, not two.

**The bosonised twist field.** Bosonise one $bc$ system of weight $\lambda=2$: $c=e^{\sigma}$,
$b=e^{-\sigma}$, $N_{\rm gh}(e^{q\sigma})=q$ (holomorphic charge), with
$$
h(e^{q\sigma})=\tfrac12q^2-\tfrac32q=\tfrac12q(q-3),
\tag{6.3}
$$
fixed by $h(c)=-1$ ($q=1$) and $h(b)=2$ ($q=-1$); independent datum: $h(e^{3\sigma})=0$
($c\partial c\partial^2c$, the conjugate vacuum), and the background charge $Q=-3$
(sphere saturation $\sum q=3$ per chirality). On the quotient the combinations
$b^\pm c^\pm$ of the two copies are periodic ($+$) and antiperiodic ($-$) around a branch
point; the $\mathbb Z_2$ twist field is the ground state of the antiperiodic $b^-c^-$ system
tensored with the $b^+c^+$ vacuum. Half-integer moding of $b^-,c^-$ means half-integer
charge $q\in\tfrac12+\mathbb Z$ for the twist field; the ground state minimises (6.3) over
half-integers: $h(\tfrac12)=h(\tfrac52)=-\tfrac58$, $h(\tfrac32)=-\tfrac98$ (the minimum,
at the midpoint $q=-Q/2$), so
$$
\sigma=e^{\tfrac32\sigma^-}\otimes\bar e^{\tfrac32\bar\sigma^-},\qquad
q_\sigma=\bar q_\sigma=\tfrac32,\qquad N_{\rm gh}(\sigma)=\tfrac32+\tfrac32=3 .
\tag{6.4}
$$
(The choice $q=\tfrac32$ is self-conjugate under $q\mapsto3-q$. The weight $h=-\tfrac98$ is the
bosonised antiperiodic ground-state value; it was **not reconciled** with the covering-space
Schwarzian formula $h_\sigma=\tfrac{c}{24}(N-\tfrac1N)=\tfrac c{16}=-\tfrac{13}{8}$ for $c=-26$,
$N=2$ — the value Lunin–Mathur use and the one that makes matter and ghosts cancel in
$D=26$ — and the antiperiodic spectrum $\{-\tfrac98+\tfrac12\mathbb Z_{\ge0}\}$ contains no state
at $-\tfrac{13}8$, so the two are in genuine tension (for a complex fermion the analogous
tension, Schwarzian $\tfrac1{16}$ vs Ramond $\tfrac18$, is resolved by a spin-structure
correction; the $bc$ background charge may play the same role here). This is unchecked CFT
input. The ghost-number match below does **not** depend on $h$: it uses only that
$q=-Q/2=\tfrac32$ is the self-conjugate charge.)

**Comparison.** (6.2) requires $3$; (6.4) gives $3$: **match, with no residue**, under reading
(B) — the one the fixture realises (§6.1). Reading (A)'s $3/2$ mismatches (6.4) by the full
$3/2$ per field, $6$ in total, but it is not the fixture's reading, and $3/2$ is not an
admissible total charge of any twist field (both chiral charges half-integer, §6.1). Per
chirality the balance reads $4-4+4\cdot\tfrac32=6=2\times3$: the four twist fields supply
$6$, the two copies' sphere saturations take $3+3$; only the *total* current $j^{(1)}+j^{(2)}$
is conserved in the presence of twist fields ($j^-$ is $S_2$-odd and branched), so no
separate $\pm$ balance is required or imposed.

*Script part 6.* (6a) torus balance (6.1); (6b) quotient balance (6.2) solved for
$N_{\rm gh}(\sigma)$, reading (B) $=3$, reading (A) $=3/2$; (6c) $h(q)$ reconstructed from
$h(c),h(b)$ alone and tested against the independent datum $h(e^{3\sigma})=0$ and the
saturation $-Q=3$; (6d) minimiser of $h$ over half-integers is $q=3/2$; (6e) match
$2q_\sigma=N_{\rm gh}(\sigma)$ under (B), and (A)'s $3/2\notin\mathbb Z$; break legs: a
$\lambda=1$ system ($Q=-1$, minimiser $q=1/2$, total $1$) fails the match, and a torus
count with seven antighosts fails (6.1).

### 6.3 Verdict on row (v)

**Match, at $12$ ($3$ per twist field): the (β2) fixture realises reading (B), all eight
antighosts of the torus measure survive as insertions on the quotient ($4$ Beltrami at the
branch points, $b^\pm_{\rm tot}b^\pm_{\rm rel}$ on the neck), and conservation on the sphere
of the doubled theory (6.2) then demands exactly the ghost number $\tfrac32+\tfrac32=3$ that
the bosonised antiperiodic $\lambda=2$ twist field carries (6.4).** Of the two readings
030 §6.1 posed, (A) is inadmissible in its all-six form ($3/2\notin\mathbb Z$) and not the
fixture's; (B) applies. The "$6$ vs $12$" question is therefore **not** an
independent "no" to Q13's second half — the ghost anomaly is consistent with the covering
picture, and the "no" of Q13 rests entirely on the geometry (row (iii), (4.7)) and the loop
momentum (§4.3), exactly as §4.3 anticipated ("genus is not the obstruction").
$$
\boxed{\text{(v): }N_{\rm gh}(\sigma)=3=\tfrac32+\tfrac32\ \text{(match under reading (B), the fixture's); no anomaly obstruction; reading (A), left open by 030, is inadmissible }(3/2\notin\mathbb Z).}
\tag{6.5}
$$
Status: the balance (6.1)–(6.2) is arithmetic, script part 6 (16 checks, break legs);
(6.3)–(6.4) are standard bosonisation, checked against $h(c\partial c\partial^2c)=0$; the
identification of the ghost twist field with the antiperiodic ground state is CFT input
(not machine-checked). One caveat: (6.4) is the *lowest* twist field; excited twist fields
$e^{q\sigma^-}$, $q\in\tfrac32+\mathbb Z$, carry other integer totals, so the match is
"the ground-state twist field is exactly what conservation asks for", not a uniqueness
theorem. In particular the descendant relabelling of §6.1 (four Beltrami $b$'s as
$b$-modes on the $\sigma_i$) gives $N_{\rm gh}=2$ dressed fields, consistent with the same
total.


## 7. Why a 2→2 gluing still describes a sphere (13c)

**The question.** Gluing two four-punctured spheres along *two* punctures each ($a\sim a'$,
$b\sim b'$) opens a handle: $\chi=2+2-2\cdot2=0$, a torus (008 (B.2), R27's resolved
genus). Yet the auxiliary channel is meant to reproduce the tree-level $\mathcal V_{0,4}$, a
sphere. Why does the 2→2 gluing "still describe a sphere" — where did the hole go?

**Answer (plain language, at the level of §3.3).** It does not describe a sphere *of the
single worldsheet CFT*; it describes a sphere *of the doubled theory*. The pair puncture is
one puncture of $\mathcal S=\mathrm{Sym}^2\mathcal H$ but two of the CFT surface (030
§3.7.3). Take the two copies of the CFT as one theory (the $\mathbb Z_2$ orbifold
$(\mathrm{CFT}\otimes\mathrm{CFT})/S_2$, Lunin–Mathur); then a state of the pair space is
one state of the doubled theory on one tube, and gluing $a\sim a'$ *and* $b\sim b'$ with
the same plumbing parameter is gluing *one* tube of the doubled theory. On the quotient of
(3.6), each rigid slice $\Omega_{V_4}(\mu_0)$ with punctures $\{1,2,a,b\}$ becomes a
three-punctured sphere $(0,\infty,u_a)$ of the doubled theory: $1,2$ at the branch points
$u=0,\infty$, and the pair $\{a,b\}$ as the *single* puncture $u_a=z_a^2$. The 2→2 gluing
of two four-punctured spheres is then a 1→1 gluing of two three-punctured spheres,
$$
(0,\infty,u_a)\ \#_{W_aW_{a'}=q}\ (0,\infty,u_{a'})\;=\;\text{a sphere with four branch
points},\qquad\chi=2+2-2\cdot1=2 ,
\tag{7.1}
$$
which is a sphere. The handle is not lost: it is what "doubled" means. A two-sheeted cover
of a sphere branched at four points is a torus, and the two sheets are the two strands of
the pair. The ghost bookkeeping of §6 confirms this is a consistent reading: the torus
saturation $0$ of one copy equals the sphere saturation $12$ of two copies minus the four
twist fields' $4\times3$.

**Worked line.** The (β2) integrand, by (3.6) and (5.4)–(5.5), is
$$
\Big\langle\,\sigma_1\sigma_2\,\Psi_1\Psi_2\,b(\partial_{\mu_1})b(\partial_{\mu_2})\Big\rangle_{(0,\infty,u_a)}
\;\Big[-\tfrac14\,b^+_{\rm rel}b^-_{\rm rel}\;b_0^{{\rm orb},+}b_0^{{\rm orb},-}\,
e^{-sL_0^{{\rm orb},+}+i\theta L_0^{{\rm orb},-}}\Big]_{\mathcal H_0\otimes\mathcal H_0}
\Big\langle\,\sigma_3\sigma_4\,\Psi_3\Psi_4\,b(\partial_{\mu_1'})b(\partial_{\mu_2'})\Big\rangle_{(0,\infty,u_{a'})},
\tag{7.2}
$$
read in the doubled theory: two three-point functions with one twist field per external
puncture, joined by one neck carrying the untwisted-sector sum with $L_0^{\rm orb}=L_{\rm tot}$.
The $s$-integral of the neck is the one-parameter family of a sphere with four points
(complex dimension $1=\dim\mathcal M_{0,4}$), which is exactly $\dim\mathcal M_{1,4}$
*restricted to $\iota$-invariant deformations*; the other three complex moduli of the torus
($\iota$-odd) are frozen, and their antighosts are the six unsoaked $b$'s of §6.

**What is and is not a sphere.**

| object | topology | status |
|---|---|---|
| resolved surface $\Sigma_{1,4}(s,\theta)$ of the single CFT | torus, $g=1$ (008 (B.2)) | geometry; carries the torus measure, but with $6$ of $8$ directions frozen |
| quotient $\Sigma_{1,4}/\iota$ | sphere, $g=0$ — of the **doubled** theory, with $4$ twist fields | geometry, exact for the (β2) fixture on a harmonic slice (rows (i), (iv)) |
| coloured graph (R27 (6)): two colour-1 vertices, one colour-2 edge | genus $0$ | bookkeeping: $g_{\rm res}=L_c+\sum_e(k_e-1)=0+1$ is the resolved genus, the coloured genus is $0$ |
| what $\mathcal V_{0,4}$ needs | sphere of the **single** CFT, four ordinary punctures, no twist fields | not obtained: the doubled sphere is a different surface (rows (iii), (v)) |

So R27's "resolved genus is bookkeeping, not geometry" is precise in the following sense:
the resolved genus $1$ is the genus of the cover; the physical object is the quotient, a
genus-$0$ surface of the doubled theory, and this is a sphere in the same sense that the
coloured graph is genus $0$ — the coloured graph *is* the quotient's graph (one colour-2
edge = one neck of the doubled theory). Why the loop momentum $\int d^Dk_a$ survives is
now visible: the neck sum of a sphere of the doubled theory runs over the untwisted sector
$(\mathcal H\otimes\mathcal H)^{S_2}$, whose momentum is a *pair* $(k_a,k_b)$ with only the
sum fixed by the external states; a single-copy sphere neck carries one momentum, fixed.
The "extra" integral is the doubled theory's ordinary tree-level state sum, and it is the
torus loop momentum of the cover (030 §3.7.3, §4.3): tree level in the doubled theory,
one loop in the single one — the two are the same statement, and neither is $\mathcal V_{0,4}$.

$$
\boxed{\text{(vi): the 2→2 gluing is a 1→1 gluing of two three-punctured spheres of the doubled theory (7.1)–(7.2); the sphere is a sphere of the orbifold, the torus is its double cover, and the coloured genus }0\text{ is the quotient's genus.}}
\tag{7.3}
$$


## 8. Self-review (13c)

**The four questions.**

1. *Does the result answer the objective, not just the task?* Yes for Q13: rows (i)–(vi)
   together give "no" with its reason — the (β2) family is a legitimate one-neck collar of
   a cubic vertex of the *doubled* theory (rows (i), (iv), (v), (vi) all consistent), but
   of the wrong vertex ($W\neq w_{SZ}$, row (iii): numerically, Möbius-disc model, sampled
   $(\beta,r)$) and with a neck sum ($\int d^Dk_a$) that $\mathcal V_{0,4}$ does not have
   (loop momentum, inherited from 030; any $\mu_0$). Row (v) answers the (A)/(B) question 030
   §6.1 posed and removes the anomaly route to "no"; the "no" is correlator-level and,
   numerically, geometric — not anomalous.
2. *What is the weakest step?* The identification of the ghost twist field with the
   antiperiodic ground state $e^{\frac32\sigma^-}$ (6.4): standard, but taken from memory
   (not fetched), and the match (6.5) is with the *lowest* twist field only; excited twist
   fields carry other integer totals, so (6.5) is consistency, not uniqueness. Second: §6.1's
   claim that $b^\pm_{\rm rel}$ cannot be attributed to a branch point rests on the operator
   picture of §5 (Lunin–Mathur dictionary), which is not machine-checkable. Third: §7's
   table entry "coloured genus $0$ = quotient's genus" is an identification of two
   bookkeepings, argued (one colour-2 edge = one neck of the doubled theory), not proven for
   general coloured graphs.
3. *What was checked by ground truth?* Parts 1–7 of the script, 69/69: cross-ratio criterion
   and lift (§2), Schottky/$\lambda(\tau)$ (§3), limaçon vs circle and the tiling necessary
   conditions, incl. the $r$-scan of the crossing-$\lambda$ ratio at six $\beta$ (§4), the Grassmann factorisation (§5), the ghost balance and bosonised weight
   function (§6). Not checked by machine: the covering dictionary itself; the twist-field
   identification; the descendant relabelling of §6.1.
4. *What would a critic attack first?* (a) Whether $\iota$-even Beltrami $b$'s "at the
   branch points" is well defined — §6.1 makes it a relabelling, so the count does not depend
   on it; (b) whether the per-chirality half-integrality argument against $3/2$ holds if the
   twist fields carried different charges in the two chiralities ($q\ne\bar q$): it does,
   the sum of two half-integers is an integer regardless; (c) the reliance on Möbius discs
   in §3–§4 (exactness) — the criterion (2.4) is coordinate-free and survives; the limaçon
   argument does **not** (it is a statement about round discs; for a non-Möbius $\mu_0$ the
   induced disc is the $z^2$-image of a non-round disc, §4.2 end), and the numerical
   positions in (4.5)–(4.7) are for the Möbius model only.

**What 13a–c did not check.**

- *Exact tiling* of $\mathcal V_{0,4}$ by the three $S_4$-images of the collar: only the
  necessary condition (A) at $s=\lambda$ and the seam condition (B) were tested (§4.2); the
  overlap of the three images was not computed. Since (A) fails at $O(1)$, the tiling fails
  a fortiori; the overlap is moot for the verdict.
- *Collar overlap* between the $s\to\lambda$ end of the collar and $\mathcal V_{0,4}$'s
  interior for $r>r_c(\beta)$: stated (§4.3), not quantified.
- *The Cassini loophole* (§4.2 end): a non-Möbius $\mu_0$ disc whose $z^2$-image is exactly
  $D_{SZ}$ — a Cassini-type region $\{|z^2-z_a^2|<\rho\}$ — is not excluded by the limaçon
  argument, which assumes Möbius (round) discs on the cover. Geometrically, row (iii) is
  *open* for such discs. The loop-momentum argument (inherited from 030 §3.7.3, sketched in
  §4.3) does not close this geometric question; it closes the *objective* for any $\mu_0$: it
  uses no local-coordinate data — the (β2) neck sum over $\mathcal H_0\otimes\mathcal H_0$
  carries $\int d^Dk_a$ and produces pair-channel thresholds in the external momenta that the
  tree-level $\mathcal V_{0,4}$ integrand at fixed $\mu$ (a finite sum of matrix elements)
  cannot. So even a $\mu_0$ that made row (iii) "yes" would leave (3.13) false as a
  correlator identity. §7 makes the same point structurally: the neck is a neck of the
  doubled theory.
- *The non-Möbius disc case* in general: §2's criterion (2.4) is coordinate-free (it is a
  cross-ratio condition plus disc symmetry), so row (i) stands; §3's uniformisation and
  §4's numbers assume Möbius discs and would need numerical uniformisation otherwise.
- *(β1) for every $(q_a,q_b)$*: row (i)'s exclusion of the product tube is proven for
  $|s_a-s_b|>C(\mu_0)$ and numerically at a generic point; the full range was not covered.
  Irrelevant to the (β2) verdicts.

**Regime of validity.** Fixture (β2) of 030 §5.3 on a harmonic rigid slice $\mu_0$ with
$\iota_1$-symmetric discs, diagonal tube, pair space $\mathrm{Sym}^2\mathcal H_0$ with
per-strand level matching (R27 RS4), physical ghost grading, bosonic closed string. The
ghost count of §6 assumes the standard $\mathbb Z_2$-orbifold structure of the doubled
$bc$ system (untwisted $b^+c^+$, antiperiodic $b^-c^-$ at branch points), i.e. that $\iota$
acts on the ghosts as on any weight-$(2,0)$ field. Nothing here addresses (α-rev)/(α-neck)
(030 §6.2, Task 14), which are single-strand and outside the covering picture.


## 9. Proposed ledger text (13c; not applied)

**New row (proposed ID R33) — "Q13 answered: (β) excluded".**

> **Q13 (030 §6.1) answered "no"; the (β) double-strand fixture is excluded as a
> representation of the $V_4$ theory (Task 13, derivation 031).** (i) The (β2) torus family
> $\Sigma_{1,4}(s,\theta)$ carries the neck-swapping involution $\iota$ with the four external
> punctures as fixed points if the rigid slice $\mu_0$ is harmonic ($(1,2;a,b)=(3,4;a',b')=-1$)
> with $\iota_1$-symmetric discs and the tube is diagonal (Proven); the converse "only if" is
> argued + numerically supported (one slice); the product tube (β1) is excluded
> for $|s_a-s_b|>C(\mu_0)$ (Proven) and numerically at a generic point. (ii)–(iii) The quotient
> family is a one-neck $s$-channel collar of an *induced* cubic vertex whose disc at the pair
> puncture is a limaçon, never SZ's round disc (proven, not by itself decisive); it is not
> $\mathcal V_{0,4}$ with R2's boundary at any sampled $(\beta,r)$, $\beta\in[0.75,3]$
> ($\beta$ is a free parameter of the $\mathcal V_3'$ family), $r\in[0.3,0.95]$: for
> $r<r_c(\beta)$ the collar never reaches $\partial F_s$, for $r>r_c$ the necessary tiling
> condition fails (crossing-$\lambda$ ratio $<1$ throughout; relative mismatch $O(1)$ at
> $\beta=O(1)$, shrinking in the degenerate large-$\beta$ limit) — numerically supported
> (Möbius-disc model, sampled $(\beta,r)$; checks 3a–4b, 7a–7b); general proof open. (iv) The
> fixture descends exactly in its
> soaked part to the $\mathbb Z_2$-orbifold's stubbed untwisted one-neck propagator, times
> $-\tfrac14b^+_{\rm rel}b^-_{\rm rel}$ (the two unsoaked tube antighosts = zero modes of the
> $S_2$-odd ghost, antighosts of the frozen $\iota$-odd relative-neck moduli; also the
> per-strand projection onto $\mathcal H_0\otimes\mathcal H_0$) — Grassmann factorisation
> Proven (checks 5a–5c); the descent statement ($L_{\rm tot}=L_0^{\rm orb}$,
> $b_{\rm tot}=b_0^{\rm orb}$) uses the orbifold covering dictionary (Lunin–Mathur) from
> memory, unverified. (v) Ghost anomaly: **no obstruction** — the fixture realises the reading in
> which all eight torus antighosts stay insertions, conservation on the doubled-theory sphere
> forces $N_{\rm gh}=3$ per twist field, matching the bosonised antiperiodic $\lambda=2$
> twist field ($\tfrac32+\tfrac32$); of the two readings 030 §6.1 posed, (A) (total $6$) is
> inadmissible as stated ($3/2\notin\mathbb Z$) and (B) (total $12$) applies (checks 6a–6e;
> twist-field identification is CFT input, its weight $h=-9/8$ not reconciled with the
> Schwarzian $-13/8$). (vi) the 2→2
> question: on the quotient the gluing is a 1→1 gluing of two three-punctured spheres of the
> *doubled* theory; the sphere is the orbifold's, the torus its double cover, the coloured
> genus $0$ the quotient's genus; the loop momentum $\int d^Dk_a$ is the doubled theory's
> tree-level neck sum. The "no" is correlator-level (loop momentum, inherited from 030
> §3.7.3: valid for any $\mu_0$, closes the objective) and geometric (iii: Möbius-disc model,
> numerical, sampled $(\beta,r)$), not anomalous; the geometric question stays open for
> non-Möbius (Cassini-type) $\mu_0$ discs, which the loop momentum makes irrelevant to the
> objective without closing. Not checked: exact tiling and collar overlap (moot given (iii));
> (β1) for every $(q_a,q_b)$; a general proof of (iii) for all $(\beta,r)$.
>
> Status: (i) if: Proven; only if: argued + numerically supported / (iii) numerically
> supported (Möbius-disc model, sampled $(\beta,r)$) / (iv) Grassmann part Proven; descent
> from-memory dictionary / (v) Verified (arithmetic) + CFT input ($h$ unreconciled) / (vi)
> argued. Script `codes/verify-chain-surfaces-covers.py` (run with `.venv/bin/python`; needs
> scipy), seed 20260914, 69/69 PASS, every check with a break-on-purpose leg. Pending: critic
> iteration 2 (narrow) on 031. Sources: `agent/derivations/031-chain-surfaces-as-covers.md`; reports
> `agent/reports/computator-13{a,b,c}-*.md`.

**Annotations to existing rows.**

- **R27** (item (2), resolved genus): append "*Annotation 2026-09-14 (031 §7):* the resolved
  genus $g_{\rm res}=1$ of a colour-2 edge is the genus of the double cover; the physical
  surface is the quotient, a sphere of the *doubled* ($\mathbb Z_2$-orbifold) worldsheet
  theory with twist fields at the external punctures, and the coloured genus $0$ is the
  quotient's genus — 'bookkeeping, not geometry' made precise. The pair-state sum on a
  colour-2 edge is the doubled theory's untwisted-sector neck sum, which carries the cover's
  loop momentum."
- **R28**: unchanged (031 adds nothing to the no-local-kernel theorem; the (β) exclusion is a
  change-of-kinetic-term statement, R30's territory).
- **R30**: in "Not settled", replace "Q13" by "Q13 **closed 2026-09-14 (no; 031, proposed
  R33)**: (β) excluded as a representation of the $V_4$ theory by the loop momentum
  (any $\mu_0$) and, in the Möbius-disc model, numerically by the geometry of the quotient
  collar at sampled $(\beta,r)$; the ghost anomaly is consistent with the
  covering picture and is not the obstruction. (α-rev)/Task 14 is the only live geometric
  option."
- **Riemann-surface note, open item (D)** (`knowledge/cubic-sft-riemann-surfaces.tex`
  §open): one line — "(D) resolved: the branched-cover reading of a colour-2 edge is
  consistent (the resolved torus is the double cover of a sphere of the doubled theory,
  031 §7) but does not make the auxiliary channel a representation of $\mathcal V_{0,4}$
  (031 §4.3, §6.3)."


## Status — record closed 2026-09-14: critic iteration 2 ACCEPT (3 one-line residues applied by the orchestrator); promoted to ledger R33 + annotations R27/R30; next: none
