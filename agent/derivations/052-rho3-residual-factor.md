# Derivation 052 — Is there a residual factor on $\rho_3$ in the SL(2,C) declared section? (PH26)

**Date:** 2026-09-26
**Agent:** computator
**Brief:** `agent/briefs/active-computator-rho3-residual-20260926T023000.md`
**Companion script:** `codes/verify-rho3-residual.py` (run log `agent/scratch/rho3-run1.log`)

## Task

*Literal task.* Decide PH26 (`knowledge/results.md`, Hypotheses table: "no residual factor on the mapping radius $\rho_3$ of the SL(2,C) declared section beyond what the Klein relation gives") by computing $\rho_3$ from the explicit local-coordinate map at $z_3=\infty$ and comparing it with the Klein-relation closed form.

*Motivating objective.* Every level-0 statement of line 18c (R51, R53, PH3 at level 0, the PH18 scan) is conditional on PH26; it is the last input between them and unconditional statements about the auxiliary sector at level 0.
Success means: either PH26 is discharged with a stated scope, or the factor $f(Z)$ is exhibited and handed to Task 11.

*Redirect flagged at the start (see §1.3).* The sister module's "map" route computes $\rho_3$ from `F3`, and `F3` is **defined** in that module as `Z / F1` — the Klein relation itself.
So the module-to-module comparison the brief names cannot, on its own, test the Klein relation: it tests the closed form of the $S$-dependence.
The record therefore adds the two comparisons that do test PH26: (i) $F_3$ built from the plumbing of two cubic vertices, independently of the Klein relation; (ii) the symmetry argument that makes the Klein relation a consequence of the $S_4$-invariance of the vertex rather than a choice.

## Conventions

- **A1** — Conventions of record 044 A1–A3 (Erbin 2023; punctures $(0,1,\infty,Z)$). No new convention.
- **A2** — Mapping radius at $z_3=\infty$ read in the chart $t=1/z$: $\rho_3=\lvert(1/F_3)'(0)\rvert$ (record 044 A6, sister derivation 001/003).
- **A3** — Declared section as packaged by the sister project: `local_coordinates.py` (maps of sister derivation 003 eq. (1), notes `tree_4point.tex` eq:4pt-locmaps-s), closed form of sister 046 eq. (2.3′) = record 044 A4, with the $z_3$ factors regulated away (record 044 A6, "A7 convention" of the module).
- **A4** — Cubic SL(2,C) vertex maps $f_0=2w/(2\beta+w)$, $f_1=(2\beta-w)/(2\beta+w)$, $f_\infty=(2\beta+w)/(2w)$ (sister notes `tree_3point.tex` eq:3pt:fw) and the plumbing fixture $w^{(1)}_\infty w^{(2)}_\infty=q$ (`tree_4point.tex` eq:S04-plumbing).

## Claim tree

- **C0** (root) — On the SL(2,C) declared section (A3) the mapping radius at $z_3=\infty$ carries no residual factor: $f(Z)\equiv1$ on $\mathrm{FD}\cap\mathcal V_{0,4}$ for every $\beta$, so R48's $(s,t,u)$ collapse holds with no tile-dependent weight and PH26 is discharged. [by C1–C5]
  - **C1** — $f$ is momentum independent; a nontrivial $f$ would enter tile $\sigma$ as $f^{\alpha'k^2_{\sigma^{-1}(3)}/2-2}$, visible only off equal masses; in the module `F3 := Z/F1`, so the module comparison tests the $S$-closed form, not the Klein relation. [block: §1]
  - **C2** — For any $S_4$-symmetric vertex, $\rho_3=\rho_1/\lvert Z\rvert$ in the $t=1/z$ chart (phases drop out); with $S=S_0$ this is $c(Z)$. [by A1, A2; eqs. (2.1)–(2.2); cited: sister notes `tree_4point.tex` eq:Fi-constraints-klein, sister 036 eq. (0.3)]
  - **C3** — The plumbing of two cubic vertices gives $\tilde F_3=Z/\tilde F_1$ and $\tilde F_4=Z/\tilde F_2$ identically, and $\lvert(1/\tilde F_3)'(0)\rvert=c(Z)$ exactly. [by A4; eqs. (2.3)–(2.5); by check: C3.klein13_plumbing_exact, C3.klein24_plumbing_exact, C3.rho3_plumbing_vs_closed]
  - **C4** — Numerical confirmation on the packaged section.
    - **C4.1** — Map route = closed form for all four radii, 250 + 16 points per $\beta\in\{3/2,2\}$: $\max\lvert f_3-1\rvert=$ (companion value, not reproduced here). [by check: C4.f3_region_beta1.5, C4.f3_region_beta2.0, C4.f124_region_*, C4.boundary_*]
    - **C4.2** — The residual is $h^4$ truncation; plateau at (companion value, not reproduced here). [by check: C4.step_plateau]
    - **C4.3** — The regulated way $\rho_3$ enters the tile integrand (A2, record 044 A6) agrees with an unregulated finite-frame evaluation at unequal masses to (companion value, not reproduced here), with $F_3$ from C3/§2B; the comparison is sensitive to a chart factor at the $\lvert Z\rvert$ level (leg (vi)). This tests the A6 regulation, not the Klein relation — the open-problem entry's requested test is C3/§2B. [by A2; §2D; by check: C6.moebius_unregulated_eq_regulated]
  - **C5** — The checks can fail: legs (i′), (i″), (ii), (iii), (v), (vi) fire; the brief's leg (i) is provably invisible. [§3; by check: C5.*]

Open gaps: none
Hypotheses in force: PH-044A4 (for the identification $\rho_1=\lvert S_0\rvert=c\lvert Z\rvert$ in (2.2), C3–C4; not needed for the Klein relation itself), PH-044A5 (t-, u-tiles by relabelling, §4)

## 1. Definition

**1.1 The residual factor.** Define, pointwise on the declared-section region,

$$
f(Z):=\frac{\rho_3^{\rm map}(Z)}{\rho_3^{\rm closed}(Z)},\qquad
\rho_3^{\rm map}=\bigl\lvert(1/F_3)'(0)\bigr\rvert,\qquad
\rho_3^{\rm closed}=c(Z)=\beta^{-1}\bigl(\lvert Z\rvert\lvert1-Z\rvert\bigr)^{-1/2},
\tag{1.1}
$$

and analogously $f_a:=\rho_a^{\rm map}/\rho_a^{\rm closed}$ for $a=1,2,4$ ($\rho_a^{\rm closed}=c(Z)\prod'_{b\ne a}\lvert z_{ab}\rvert$, i.e. $c\lvert Z\rvert$, $c\lvert1-Z\rvert$, $c\lvert Z\rvert\lvert1-Z\rvert$).

**1.2 How a nontrivial $f$ would enter.** In the 12-tile assembly (record 044 A5) the dressing on tile $\sigma$ is $\prod_a\rho_a^{\alpha'k^2_{\sigma^{-1}(a)}/2-2}$.
Replacing $\rho_3\to f\rho_3$ multiplies the tile-$\sigma$ integrand by $f(Z)^{\alpha'k^2_{\sigma^{-1}(3)}/2-2}$.
Since each of $k_1,k_2,k_3$ sits at $z_3$ on two tiles, the weight is tile-independent only when $k_1^2=k_2^2=k_3^2$; otherwise the individual $k_a^2$ no longer cancel (R48's iff, record 044 Block 6) and the $(s,t,u)$ collapse fails.
All three evaluations so far (sister reduced and unreduced routes, record 044) take $\rho_3$ from the same Klein relation, so the eight-point comparator is blind to $f$.

**1.3 $f$ is a property of the section.** The maps $F_a(w;Z,\beta)$ carry no momentum: $f=f(Z;\beta)$.
One scan over $Z$ at each $\beta$ decides it for every mass assignment; "unequal-mass point" in the open-problem entry designates where $f\ne1$ would become *visible*, not a different input.

**1.4 What the module comparison can and cannot test.** In `local_coordinates.py`, `F3(w) = Z / F1(w)` (docstring: "the exact-in-w Klein relation").
Hence $(1/F_3)'(0)=F_1'(0)/Z$ identically, and $f=f_1$: the module's map route for $\rho_3$ is the Klein relation followed by numerical differentiation.
The module comparison checks the closed form $\rho_a=\lvert\kappa_aS_0\rvert$ ($\kappa=(1,(1-Z)/Z,1/Z,Z-1)$) against the maps; it does not test the Klein relation.
Moreover, the sister's `verify_local_coordinates.py` compares each route against the sister's own reference code (`codes/unequal-mass-contact.py`), not the two routes against each other; the direct map-versus-closed-form comparison below is new.

**First values** (module routes, $f_a-1$ for $a=1,2,3,4$; $h=10^{-3}$):

[Table of companion-project values removed.]

$f_3-1$ tracks $f_1-1$ to rounding, as §1.4 predicts.

## 2. Computation

### 2A. The Klein relation is forced by the symmetry of the vertex (analytic)

\subsection*{Setup}
A1–A3. $V=\{1,(12)(34),(13)(24),(14)(23)\}\subset S_4$; the element $(13)(24)$ is realised by the Möbius map $M_{13}(z)=Z/z$, which exchanges $0\leftrightarrow\infty$, $1\leftrightarrow Z$ and fixes the cross-ratio (sister notes `tree_4point.tex` eq:Fi-constraints-klein).

\subsection*{Derivation}
$$
\begin{aligned}
&M_{13}\circ F_1(W,Z)=F_3(e^{i\theta}W,Z) &&\text{(invariance of the vertex under }(13)(24)\text{)}\\
&\Rightarrow\ \frac1{F_3(W')}=\frac{F_1(e^{-i\theta}W')}{Z}
\ \Rightarrow\ \Bigl\lvert\Bigl(\frac1{F_3}\Bigr)'(0)\Bigr\rvert=\frac{\lvert F_1'(0)\rvert}{\lvert Z\rvert}=\frac{\lvert S\rvert}{\lvert Z\rvert}
&&\text{(2.1)}\\
&\lvert S_0\rvert^2=\frac{\lvert Z\rvert}{\beta^2\lvert1-Z\rvert}
\ \Rightarrow\ \rho_3=\frac{1}{\beta\,\lvert Z\rvert^{1/2}\lvert1-Z\rvert^{1/2}}=c(Z) &&\text{(2.2)}
\end{aligned}
$$

\subsection*{Commentary}
(2.1): a closed-string vertex is symmetric under relabelling of punctures only up to a rotation $W\to e^{i\theta}W$ of each local coordinate (level matching); the rotation drops out of the modulus of the derivative. So, for **any** $S_4$-symmetric assignment of local coordinates, $\rho_3=\rho_1/\lvert Z\rvert$ in the $t=1/z$ chart, whatever $S$ and $R$ are. On the declared section the sister notes go further and *define* $F_2,F_3,F_4$ from $F_1$ by these relations (`tree_4point.tex` l. 2006), so there $f\equiv1$ holds by construction. (2.2) uses $S=S_0$ (sister 036 eq. (0.3), module `S0_modulus`); $R$ (and hence $\Lambda_1$) does not enter any radius.

\subsection*{Result}
$$\boxed{\ \rho_3=\rho_1/\lvert Z\rvert\ \text{for every }S_4\text{-symmetric vertex};\quad f(Z)\equiv1\ \text{on the declared section, analytically.}\ }$$
A residual factor on $\rho_3$ would therefore not be a feature of some section: it would be a violation of the $(13)(24)$ symmetry of the vertex. PH26, as worded, asks whether the declared section is symmetric under $V$, which it is by construction.

### 2B. Independent route: $F_3$ from the plumbing of two cubic vertices (exact)

\subsection*{Setup}
A4. Cubic maps $f_0,f_1,f_\infty$; $w_\infty=2\beta/(2f_\infty-1)$ (`tree_3point.tex` eq:3pt:w-from-f), so $w^{(1)}_\infty w^{(2)}_\infty=q$ gives $(2z^{(1)}-1)(2z^{(2)}-1)=4\beta^2/q$.
s-channel assignment $W_1=w^{(1)}_0$, $W_2=w^{(1)}_1$, $W_3=w^{(2)}_0$, $W_4=w^{(2)}_1$; $g_s(z)=(p_3-1)z/(p_3-z)$, $p_3=F_3^{\rm pl}(0)$, sends $p_3\to\infty$ fixing $0,1$.

\subsection*{Derivation}
$$
\begin{aligned}
F_3^{\rm pl}(W)&=\tfrac12\Bigl(1+\frac{4\beta^2}{q}\,\frac{1}{2f_0(W)-1}\Bigr),\qquad \tilde F_a=g_s\circ F_a^{\rm pl},\qquad Z=\tilde F_4(0)=\frac{(4\beta^2+q)^2}{16\beta^2q} &&\text{(2.3)}\\
\tilde F_3-\frac{Z}{\tilde F_1}&\equiv0,\qquad \tilde F_4-\frac{Z}{\tilde F_2}\equiv0\quad\text{(rational identities in }W,q,\beta) &&\text{(2.4)}\\
\Bigl(\frac1{\tilde F_3}\Bigr)'(0)&=\frac{16\beta q}{(4\beta^2-q)(4\beta^2+q)},\qquad
\Bigl\lvert\Bigl(\frac1{\tilde F_3}\Bigr)'(0)\Bigr\rvert=c(Z) &&\text{(2.5)}
\end{aligned}
$$

\subsection*{Commentary}
(2.3) is built in the script from the cubic maps alone; it does not use the module's `F3` nor the Klein relation. (2.4) is then a sympy identity. (2.5): from (2.3), $1-Z=-(4\beta^2-q)^2/(16\beta^2q)$, hence $\lvert Z\rvert\lvert1-Z\rvert=\lvert4\beta^2+q\rvert^2\lvert4\beta^2-q\rvert^2/(256\beta^4\lvert q\rvert^2)$ and $c=16\beta\lvert q\rvert/(\lvert4\beta^2+q\rvert\lvert4\beta^2-q\rvert)$, equal to the modulus of the derivative. This holds for every $q$, in particular for the module's root $q(Z)$ on $\mathrm{FD}\cap\mathcal V_{0,4}$. The plumbing $\tilde F_1$ coincides with the module's `F1` (to (companion value, not reproduced here)). Scope: the plumbing maps are the s-channel propagator family; on the vertex region the declared section keeps $S=S_0$, which is the same $F_1'(0)$ (sister 036), and replaces $R$, which does not enter $\rho$.

\subsection*{Result}
The Klein relation used by the module is exactly what the plumbing gives: $\rho_3^{\rm plumbing}=c(Z)$, identity in $(q,\beta)$, numerically $1.2\times10^{-14}$ at 80 seeded region points.

### 2C. Module scan: map route against closed form (numerical)

$f_a=\rho_a^{\rm map}/\rho_a^{\rm closed}$ at 250 seeded points of $\mathrm{FD}\cap\mathcal V_{0,4}$ per $\beta$ (rejection sampling, seed 20260926) and 16 boundary points per $\beta$ (walls C2, C3, C4 just inside, and the corner $e^{i\pi/3}$ — the brief's "$Z\to\tfrac12$" lies outside the FD, $\lvert Z\rvert\ge1$; the maximum of $c$ on the region is at the corner):

[Table of companion-project values removed.]

**Step plateau** ($\beta=3/2$, 40 points, $\max\lvert f_3-1\rvert$ vs $h$ of the fourth-order stencil):

[Table of companion-project values removed.]

The deviation falls as $h^4$ (slope (companion value, not reproduced here)) down to a plateau at (companion value, not reproduced here) for small $h$: the residual at the module's step is the stencil's truncation error, and the agreement is at machine precision once it is removed. The $f_2,f_4$ residuals (companion value, not reproduced here) are the same truncation, larger because $F_2,F_4$ have larger fifth derivatives at $W=0$; not re-plateaued, as they are not PH26's object. As §1.4 predicts, $f_3=f_1$ to (companion value, not reproduced here) at every point.

The module's `F1..F4` scanned above are the s-channel plumbing maps (sister derivation 003), not the vertex-region section maps (which differ in $R$); the mapping radii coincide because $\rho_a$ depends on $F_a'(0)=S$ only, and $S=S_0$ on both (record 044 A4, PH-044A4).

### 2D. How $\rho_3$ enters the integrand: unregulated finite frame against the regulated formula (unequal masses)

The momentum-dependent part of one tile's integrand, $\prod_a\rho_a^{\alpha'k_a^2/2}\prod_{a<b}\lvert z_{ab}\rvert^{\alpha'k_a\cdot k_b}$, is Möbius invariant for $\sum_ak_a=0$ (each $\lvert z'_{ab}\rvert^2=\lvert M'(z_a)\rvert\lvert M'(z_b)\rvert\lvert z_{ab}\rvert^2$, and $\sum_{b\ne a}k_a\cdot k_b=-k_a^2$ cancels $\rho'_a=\lvert M'(z_a)\rvert\rho_a$).
The script moves the four maps by a random Möbius $M$ (all punctures finite, no regulation, $\rho_a'$ by differentiation) and compares with the regulated formula of record 044 (A6: $\rho_3=c(Z)$ in the $t=1/z$ chart, $z_3$ factors dropped, $\mathrm{KN}=\lvert Z\rvert^{\alpha'k_1k_4}\lvert1-Z\rvert^{\alpha'k_2k_4}$).
Momenta: the Gram matrices of the eight comparator $(s,t,u)$ points (comparator file; these points carry no $Z$), with unequal $k_a^2$ summing to $s+t+u$ (different splits per point, point 2 distinct from point 1), $\alpha'=1$, 6 seeded $Z$ per point.
Result: max relative difference (companion value, not reproduced here) (limited by the finite-difference derivative at $h=2\times10^{-4}$ on the Möbius-moved maps); with $\rho_3\to\lvert Z\rvert\rho_3$ (a nontrivial $f$) the same comparison fails by (companion value, not reproduced here).
This tests the chart convention and the $z_3$ regulation (record 044 A6) — the way $\rho_3$ actually enters — at unequal masses, which the module comparison does not.

## 3. Break legs

All in `codes/verify-rho3-residual.py`, seed 20260926, $\beta=3/2$ unless stated, 60 region points.

| Leg | Perturbation | Expected | Measured | Verdict |
|---|---|---|---|---|
| (i) brief's leg | $F_3\to F_3(1+\epsilon w)$, $\epsilon=10^{-3}$ | brief: $f\ne1$ at $10^{-3}$ | $\max\lvert f-1\rvert=$ (companion value, not reproduced here) | **does not fire, correctly**: see below |
| (i′) | $F_3\to(1+\epsilon)F_3$ | $\lvert f-1\rvert=\epsilon/(1+\epsilon)$ | $\min\lvert f-1\rvert=9.99\times10^{-4}$ | fires |
| (i″) | $1/F_3\to1/F_3+\epsilon w$ | first order $\epsilon\,\mathrm{Re}(e^{-i\arg(S/Z)})/\lvert S/Z\rvert$ | fires ($>10^{-5}$) at 98 % of points, max $3.3\times10^{-3}$, min $2.3\times10^{-6}$ | fires; min is the zero curve of the first-order term |
| (ii) | closed form with $z_3=\Lambda$ finite, $\Lambda\in\{10,100\}$ (not regulated) | $O(1)$ failure | $\min\lvert f-1\rvert=0.999$ | fires |
| (iii) | $\rho_2\leftrightarrow\rho_4$ | $\lvert f-1\rvert=\lvert\lvert Z\rvert^{-1}-1\rvert$ | 59 points with $\lvert Z\rvert\ge1.01$: min $2.0\times10^{-2}$, equal to the prediction to (companion value, not reproduced here) | fires off wall C3 |
| (v) | wrong Klein pairing $\tilde F_3-Z/\tilde F_2$ (plumbing) | nonzero | nonzero | fires |
| (vi) | 2D with $\rho_3\to\lvert Z\rvert\rho_3$ | fails at unequal masses | min rel. diff (companion value, not reproduced here) | fires |

**Finding on leg (i).** The brief's perturbation cannot change $\rho_3$: in the $t=1/z$ chart
$$\Bigl(\frac{1}{F_3(1+\epsilon w)}\Bigr)'(0)=\Bigl(\frac1{F_3}\Bigr)'(0)-\epsilon\,\frac1{F_3(0)}=\Bigl(\frac1{F_3}\Bigr)'(0),\qquad \frac1{F_3(0)}=0 .$$
A factor $1+O(w)$ multiplying a map with a pole at $w=0$ changes only the subleading coefficients of $1/F_3$, not the mapping radius. The leg is kept in the script as a control that must **not** fire. The legs that do perturb $\rho_3$ are a rescaling of $F_3$ (i′) or an additive term in $1/F_3$ (i″); both fire at the $\epsilon$ level.

**Trap on leg (iii).** On wall C3 ($\lvert Z\rvert=1$) $\rho_4/\rho_2=\lvert Z\rvert=1$ and the swap is invisible (residual (companion value, not reproduced here) at $Z=e^{2i}$); the leg is run on points with $\lvert Z\rvert\ge1.01$. A random sample that happened to hug C3 would have reported a non-firing leg for the wrong reason.

**Correction during the run.** A first version of check C3.rho3_plumbing_vs_closed evaluated the uncancelled $(1/\tilde F_3)'$ at $W=0$, got `nan`, and passed because `max(0.0, nan)` returns `0.0` in Python. Fixed by cancelling the rational function first and by failing on any non-finite value; the recorded $1.2\times10^{-14}$ is from the fixed check.

## 4. Scope and consequence

**What is established.**
(a) For any $S_4$-symmetric assignment of local coordinates, $\rho_3=\rho_1/\lvert Z\rvert$ in the $t=1/z$ chart (2A); on the declared section, where $F_3:=Z/F_1$ by definition and $S=S_0$, $f\equiv1$ analytically.
(b) The Klein relation is not an extra input: the s-channel plumbing of two cubic vertices yields $\tilde F_3=Z/\tilde F_1$ as an identity in $(W,q,\beta)$, and $\lvert(1/\tilde F_3)'(0)\rvert=c(Z)$ exactly (2B).
(c) The packaged module agrees with its closed form on $\mathrm{FD}\cap\mathcal V_{0,4}$ for all four radii: $\max\lvert f-1\rvert=$ (companion value, not reproduced here) at the module's step and on the step plateau; boundary points and the corner included (2C).
(d) The regulated way $\rho_3$ enters the tile integrand (record 044 A6) agrees with an unregulated finite-frame evaluation at unequal masses to (companion value, not reproduced here), with $F_3$ from (b); the comparison is sensitive to a chart factor at the $\lvert Z\rvert$ level (leg (vi)).
Hence R48's collapse to $(s,t,u)$ holds with no tile-dependent weight, and **PH26 is discharged**.

The open-problem entry's requested test ("$\rho_3$ computed from the explicit local-coordinate map at $z_3=\infty$, not from the Klein relation") is answered by (b)/§2B, which is exact at every $Z$; (d)/§2D is a distinct, genuine test of the A6 regulation convention, not of the Klein relation.

**What it does not establish.**

- Nothing about a section that is not $S_4$-symmetric; every section this project or the sister uses is symmetric by construction (the vertex must be).
- Nothing about R48's other imports: A4's $S$ (it is the sister's $S_0$, `SL: R51`) and A5's tile assembly (`SL: R6`/`R10`) remain imported (PH-044A4, PH-044A5).
- The scanned module's `F1..F4` (2C) are the s-channel plumbing maps, not the vertex-region section maps (which differ in $R$); the mapping radii tested coincide with the section's because $\rho_a$ depends on $F_a'(0)=S$ only, and $S=S_0$ on both.
- The t- and u-channel maps are not computed separately. This is enough because record 044 applies the closed form tile by tile with the same $S_4$ relabelling (A5): on tile $\sigma$ the radii are the FD radii with momenta relabelled, $\rho_a^{\rm FD}(Z)^{\alpha'k^2_{\sigma^{-1}(a)}/2-2}$, so only the four FD radii enter, and those are what was tested. The relabelling itself is the vertex's $S_4$ covariance (`tree_4point.tex` eq:Fi-constraints-perm), part of A5.
- Nothing about the level-(1,1) states: their dressing involves $R$ and higher Taylor coefficients of the maps, not only $\rho_a$.
- The momentum-independent factor $\rho^{-2}$ and the measure: covered by (a)–(c) only as far as $\rho_3$ is concerned.

**Reading of PH26.** As worded, PH26 asked whether the declared section carries a factor on $\rho_3$ beyond the Klein relation. The answer is structural: the Klein relation is the $(13)(24)$ symmetry of the vertex, and the declared section is built from it. An earlier concern was that the module comparison tests the definition itself; §1.4 confirms it, which is why the plumbing route (2B) and the symmetry argument (2A) were added.

## 5. Self-review

1. *Objective or literal task?* The objective (remove PH26 from the level-0 line 18c) is answered; the literal module comparison alone would not have answered it, since `F3 := Z/F1` in the module (§1.4) — the record says so and adds 2A and 2B.
2. *Weakest step.* 2A's "any symmetric vertex" relies on the invariance of the vertex under $(13)(24)$ holding up to a phase only. That is the definition of a symmetric closed-string vertex (`tree_4point.tex` l. 1666 ff.); the sister notes report the Klein relations checked exactly, with trivial phases, on the propagator channels, and 2B re-derives that for the s-channel.
3. *Not checked.* t-/u-channel maps separately (argued in §4); a section other than the declared one; level (1,1).
4. *What a stronger physicist would find in five minutes.* That PH26 was never a genuine hypothesis about the section but about vertex symmetry, which makes the discharge structural rather than numerical; and that the brief's break leg (i) is invisible by construction. Both are in the record.

## Verification

`codes/verify-rho3-residual.py`, seed 20260926, run log `agent/scratch/rho3-run1.log`: **23/23 PASS, 0 FAIL, exit 0**.
Run 2 (after the critic's fix pass added `C3.F2_plumbing_eq_module`, run log `agent/scratch/rho3-run2.log`): **24/24 PASS, 0 FAIL, exit 0**.

- C3: plumbing identities (2.4) exact in sympy; $\rho_3^{\rm plumbing}$ vs $c(Z)$ $1.2\times10^{-14}$ at 80 points; plumbing $\tilde F_1$ = module `F1` to (companion value, not reproduced here); plumbing $\tilde F_2$ = module `F2` to (companion value, not reproduced here) (`C3.F2_plumbing_eq_module`, added in the fix pass); $Z(q)$ = eq:Z4-s-q.
- C2: $(12)(34)$ Klein relation exact for the plumbing maps.
- C4: region scan, boundary scan, $f_3=f_1$, step plateau with $h^4$ slope (companion value, not reproduced here).
- C6 (tree C4.3): Möbius finite frame vs regulated, 8 comparator points, unequal $k_a^2$, (companion value, not reproduced here).
- C5: legs (i) control, (i′), (i″), (ii), (iii), (v), (vi), table of §3.
The script's C-numbers predate the final claim tree; mapping: script C3 ↔ tree C3, script C2 ↔ tree C2, script C4 ↔ tree C4.1–C4.2, script C6 ↔ tree C4.3, script C5 ↔ tree C5.
Falsifiability: every comparison is between two independent routes (plumbing vs closed form; map derivative vs closed form for $\rho_1$, and for $\rho_3$ only as the $S$-closed form, §1.4; finite frame vs regulated formula); every one has a break leg that fires. One vacuous version (NaN swallowed by `max`) was found and fixed during the run (§3).
Not independent verification: the numerical-verifier has not run.

## Proposed ledger action

- **PH26** (Hypotheses table): status `open` → `discharged (derivation 052: Klein relation = (13)(24) symmetry of the vertex; plumbing F_3 = Z/F_1 exactly; module maps vs closed form (companion value, not reproduced here) at β = 3/2, 2; 24/24 PASS, seed 20260926)`.
- **R51** status: `Conditional(PH25, PH26; R48's A4, A5 imported) – Verified (…)` → `Conditional(PH25; R48's A4, A5 imported) – Verified (…)`, rest unchanged.
- **R53** status: `Conditional(PH25, PH26; R48's A4, A5 imported) – Proven (…)` → `Conditional(PH25; R48's A4, A5 imported) – Proven (…)`, rest unchanged.
- **R48**: status string carries no PH26 (`Conditional(A4, A5 — imported, see source) – Verified (…)`), unchanged. Annotate its text: the "Negative result carried by this row: it does not close the sister project's §C.2 gap on $\rho_3$" and the closing "registered as hypothesis PH26" → add "*Annotation 2026-09-26:* closed by derivation 052 — the Klein relation is the $(13)(24)$ symmetry of the vertex, re-derived from the plumbing; no residual factor; PH26 discharged."
- **PH3 at level 0** (pending row from 050 C4, not yet in the ledger): when written, its condition list is PH25, PH-044A4, PH-044A5 — no PH26.
- Records 050 (C1–C4, hypotheses line l. 53) and 051 (C6–C7, l. 43): PH26 drops from "Hypotheses in force" at their next pass; nothing else changes (their content does not depend on how PH26 is discharged).
- `knowledge/open-problems.md`, last entry: close with a pointer to 052.

## Status

Complete, critic mechanical fix pass applied (`agent/reports/critic-052-20260926T010000.md`, ACCEPT): §4(d)/C4.3 restatements corrected, `Hypotheses in force` names PH-044A4/PH-044A5, §2C/§4 note the module's `F1..F4` are plumbing maps, docstring and Verification wording fixed, `C3.F2_plumbing_eq_module` added. Script re-run: 24/24 PASS, 0 FAIL, exit 0 (seed 20260926, `agent/scratch/rho3-run2.log`). Next: orchestrator — ledger edits of the Proposed ledger action.
