---
id: 044-stu-reduction-contact-term
brief: agent/briefs/active-computator-stu-reduction-20260921T214000.md
created: 2026-09-21
script: codes/verify-stu-reduction.py
---

# 044 — The four-tachyon contact term depends on $(s,t,u)$ alone

## Task and objective

**Literal task.** Establish, inside this project, that the off-shell four-tachyon contact
term $\{T^4\}_{\rm contact}(k_1,\dots,k_4)$ in the SL(2,C) project's declared section depends
on the external momenta only through the Mandelstam invariants $(s,t,u)$ — the individual
$k_a^2$ cancelling *pointwise* in the moduli parameter $Z$ — and determine exactly which
properties of the section that cancellation uses. Also: determine whether a residual
momentum-independent weight on $\rho_3$ is visible to a test run on this side.

**Motivating objective.** A numerical grid of this
object is what the pair-kernel discretisation requires. That grid feeds PH1 (ii), PH3, PH18 and R29's H1/H2. A three-parameter object instead
of a six-parameter one changes what must be requested and what can be built from it (the pair
kernel $K_P(k;k')$ and its discretisation box, record 045). The reduction must therefore be
owned here, with its regime of validity, rather than inherited from a sentence in a hand-off.

## Status

Last completed: all sections written, all checks run and passing (32/32, 5 break legs
firing), report written, and a mechanical fix pass applied following
`agent/reports/critic-044-20260921T220500.md`. **One caveat travels with the record: it
does not close the sister project's §C.2 gap on $\rho_3$ (C5.4) — the shipped module
defines $\rho_3$ through the Klein relation $F_3=Z/F_1$, so no check here determines
$\rho_3$ independently of that definition.**
Next: none inside this record; the record is complete and ready for promotion.

## Claim tree

### Assumptions (record level)

- **A1** — Erbin (2023) conventions: metric $(-,+,+,+)$, $\hbar=c=1$, $\alpha'$ explicit.
  Project conventions (physical ghost number, $\nu=-\tfrac12$).
- **A2** — All four momenta incoming, $\sum_a k_a=0$. Off-shell Mandelstam convention
  $s_{ab}:=(k_a+k_b)^2$, so $k_a\!\cdot\!k_b=\tfrac12\bigl(s_{ab}-k_a^2-k_b^2\bigr)$, and
  $s:=s_{12}$, $t:=s_{13}$, $u:=s_{14}$. No mass-shell condition is imposed anywhere.
- **A3** — Punctures fixed at $(z_1,z_2,z_3,z_4)=(0,1,\infty,Z)$, $Z$ the cross-ratio modulus.
- **A4** *(imported, not re-derived)* — Declared-section mapping radii in closed form,
  $\rho_a=c(Z)\prod'_{b\ne a}\lvert z_{ab}\rvert$ with
  $c(Z)=\beta^{-1}\bigl(\lvert Z\rvert\lvert1-Z\rvert\bigr)^{-1/2}$ **independent of $a$**;
  source: sister derivation 046 eq. (2.3′), `SL: R51`.
- **A5** *(imported, not re-derived)* — The equivariant 12-tile assembly of the contact term
  (`SL: R6`, `SL: R10`, package §4): $\{T^4\}_{\rm contact}
  =C\sum_{g\in G}\int_{\mathrm{FD}\cap\mathcal V_{0,4}}
  \bigl[\prod_a\rho_a^{\rm FD}(Z)^{\alpha'k_{\sigma_g^{-1}(a)}^2/2-2}\bigr]
  \mathrm{KN}(\sigma_g^{-1}k;Z)\,d^2Z$, with
  $\mathrm{KN}(k;Z)=\lvert Z\rvert^{\alpha'k_1k_4}\lvert1-Z\rvert^{\alpha'k_2k_4}$ and
  $G=S_3\times\mathrm{conj}$ of order 12.
- Registered in the ledger (2026-09-26): A4 = PH29, A5 = PH30 (records 049–052 write them `PH-044A4`, `PH-044A5`).
- **A6** — $z_3=\infty$ regularisation (the "A7 convention" of the sister module): every
  factor carrying the index 3 as a *puncture position* is dropped consistently from both
  $\rho_a$ (the primed product in A4, with $\rho_3$ read in the $t=1/z$ chart) and from the
  Koba–Nielsen product (whence the two-factor $\mathrm{KN}$ of A5, $\lvert z_{12}\rvert=1$
  being trivial).
- **A7** — Tachyonic dressing weight: the local-frame dressing exponent is
  $\alpha'k_a^2/2-2$ per puncture (tachyon vertex operator of conformal weight
  $(\alpha'k^2/4-1,\ \alpha'k^2/4-1)$).
- **A8** — Declared section: $S=S_0$ (sister 036), $\Lambda_1$ at
  its declared-section value $\lambda_0$; numerics at $\beta\in\{3/2,2\}$, analytic
  statements for $\beta>\beta_{04}$ ($\beta_{04}=$ (companion value, not reproduced here)).
- **A9** — The reduction is a statement about *momentum dependence* of the integrand. It is
  invariant under the overall normalisation rescaling $\nu=-1\to-\tfrac12$ (`R43`,
  $V_4\times\tfrac12$), which is a momentum-independent constant. No conversion is performed.

### Hypotheses

None. The result is unconditional given A1–A9.

### Claims

- **C1** — In the declared section the full four-tachyon contact integrand of A5 depends on
  the external momenta only through $(s,t,u)$, pointwise in $Z$ and per tile.
  [by C1.1–C1.4]
  - **C1.1** — With A4 and A6, $\prod_a\rho_a^{\alpha'k_a^2/2}\cdot\mathrm{KN}(k;Z)
    = c(Z)^{\alpha'\sum_ak_a^2/2}\,\lvert Z\rvert^{\alpha'u/2}\,\lvert1-Z\rvert^{\alpha't/2}$,
    identically in $Z$. [by A2, A4, A6; block *Pointwise cancellation*, eq. (1.6)]
  - **C1.2** — $\sum_ak_a^2=s+t+u$ identically, using $\sum_ak_a=0$ and nothing else (no
    mass-shell condition). [by A2; eq. (1.7)]
  - **C1.3** — $\prod_a\rho_a=\beta^{-4}$ exactly, for every $Z$; hence the momentum-blind
    factor $\prod_a\rho_a^{-2}=\beta^{8}$ is $Z$-independent. This reproduces the `SL: R5`
    modulus identity from A4. [by A4; eq. (1.8); check `C1.3`]
  - **C1.4** — Consequently the per-tile integrand is
    $\beta^{8}\,c(Z)^{\alpha'(s+t+u)/2}\lvert Z\rvert^{\alpha'x/2}\lvert1-Z\rvert^{\alpha'y/2}$
    with $(x,y)$ a pair of distinct Mandelstams fixed by the tile. [by C1.1–C1.3; eq. (1.9)]
- **C2** — The 12 tiles of $G$ realise each of the six *ordered* pairs $(x,y)$ of distinct
  elements of $\{s,t,u\}$ exactly twice, so
  $$\{T^4\}_{\rm contact}=2C\,\beta^{\,8-\alpha'(s+t+u)/2}\!\!\sum_{(x,y,z)\in S_3\cdot(s,t,u)}
    \int_{\mathrm{FD}\cap\mathcal V_{0,4}}\!\!
    \lvert Z\rvert^{\alpha'(x-y-z)/4}\lvert1-Z\rvert^{\alpha'(y-x-z)/4}\,d^2Z,$$
  which is manifestly totally symmetric in $(s,t,u)$ — i.e. totally crossing symmetric.
  [by C1, A5; block *Tile sum and crossing*, eq. (2.4); checks `C2`, `C2-crossing`]
- **C3** — Limiting cases. [by C3.1, C3.2]
  - **C3.1** — At equal masses $k_a^2\equiv k^2$ the dressing collapses to the
    $Z$-independent prefactor $\beta^{8-2\alpha'k^2}$, matching `SL: R6`/`SL: R10`; the
    residual $k^2$ dependence of an $(s,t,u)$-only object is not a contradiction because
    $s+t+u=4k^2$ on that locus. [by C1.3, C1.4; block *Limits*; check `C3.1`]
  - **C3.2** — At $k=0$ the tile sum reduces to
    $12\,C\,\mathrm{Vol}(\mathrm{FD}\cap\mathcal V_{0,4})\,\beta^{8}$, the Stage 0 value.
    [by C2; check `C3.2`]
- **C4** — Regime of validity. The single load-bearing section property is the
  $a$-independence of the prefactor in A4; equivalently $\rho_a=\lvert\kappa_a\rvert\,\lvert
  S(Z)\rvert$ with $\kappa=(1,(1-Z)/Z,1/Z,Z-1)$ carrying all the puncture dependence.
  [by C4.1–C4.3]
  - **C4.1** — A puncture-dependent prefactor $c\to c_a$ reintroduces
    $\prod_ac_a(Z)^{\alpha'k_a^2/2}$, which is not a function of $(s,t,u)$ unless all $c_a$
    coincide. [by C1.1; block *Regime*; check `C1.4-aindep`]
  - **C4.2** — The reduction survives an arbitrary variation of the second-point map $S$
    (which enters only as the $a$-independent factor $\lvert S\rvert=c$), and is
    *independent of $\Lambda_1$*, which does not enter the radii at all. [by A4, C4.1;
    check `C4.2-lambda`]
  - **C4.3** — The $z_3=\infty$ regularisation A6 enters twice and must be the *same* both
    times: the primed product in $\rho_a$ and the dropped $z_{3b}$ factors in $\mathrm{KN}$.
    Dropping it on one side only leaves an uncancelled $\lvert z_{3b}\rvert$ divergence.
    [by C1.1; block *Regime*]
- **C5** — The residual-weight falsifier. [by C5.1–C5.4]
  - **C5.1** — $\rho_3\to\mu\rho_3$ ($\mu$ momentum-independent) multiplies the tile-$g$
    integrand by $\mu^{\alpha'k^2_{\sigma_g^{-1}(3)}/2-2}$; the $\mu^{-2}$ is an overall
    constant, but the momentum-dependent part destroys the $(s,t,u)$ reduction. It is
    therefore *visible* to the two-configuration test of C1. [by C1.1; block *Residual
    weight*; break leg `BREAK-rho3`]
  - **C5.2** — $c\to\mu c$ (all four punctures) multiplies the whole object by
    $\mu^{\alpha'(s+t+u)/2-8}$. The reduction and the crossing symmetry both survive; the
    weight is *invisible* to every momentum-structure test in this record. [by C1.1, C1.3;
    break leg `BREAK-c`]
  - **C5.3** — Whether C5.1's breaking is a *crossing* violation is not determined by A5:
    the group $G$ fixes only the coset of $\sigma_g$ in $S_4/V$ ($V$ the Klein four-group),
    and $\sigma_g^{-1}(3)$ takes all four label values across a coset. Under the explicit
    representative choice stated in the block, the deformed sum is not symmetric under
    relabellings moving puncture 3, and the violation shows as a failure of total
    $(s,t,u)$ symmetry. [by C5.1, A5; block *Residual weight*; check `C5.3`]
  - **C5.4** — This record does **not** close the sister project's §C.2 gap: the only
    $\rho_3$ available on this side is defined through the Klein relation $F_3=Z/F_1$, so
    `radii_from_maps` and `radii_closed_form` share it and neither determines it
    independently. [by inspection of the shipped module; block *Residual weight*]

Open gaps: none
Hypotheses in force: none

## Derivation

### Block 1 — Pointwise cancellation

\subsection*{Setup}

Assumptions A1–A4, A6, A7. Block-local notation: write the *regulated* puncture product

$$P_a:=\prod_{b\ne a}{}^{'}\lvert z_{ab}\rvert,\tag{1.1}$$

the prime meaning that every factor carrying the puncture index 3 is omitted (A6). With
$(z_1,z_2,z_3,z_4)=(0,1,\infty,Z)$,

$$P_1=\lvert z_{12}\rvert\lvert z_{14}\rvert=\lvert Z\rvert,\quad
P_2=\lvert z_{21}\rvert\lvert z_{24}\rvert=\lvert1-Z\rvert,\quad
P_3=1,\quad
P_4=\lvert z_{41}\rvert\lvert z_{42}\rvert=\lvert Z\rvert\lvert1-Z\rvert.\tag{1.2}$$

A4 then reads $\rho_a=c(Z)P_a$ with $c$ independent of $a$.

\subsection*{Derivation}

The momentum-dependent part of the local-frame dressing (A7) is

$$D(k;Z):=\prod_a\rho_a^{\alpha'k_a^2/2}
=c(Z)^{\alpha'\sum_ak_a^2/2}\prod_aP_a^{\alpha'k_a^2/2}.\tag{1.3}$$

Substituting (1.2),

$$\prod_aP_a^{\alpha'k_a^2/2}
=\lvert Z\rvert^{\alpha'(k_1^2+k_4^2)/2}\,\lvert1-Z\rvert^{\alpha'(k_2^2+k_4^2)/2}.\tag{1.4}$$

The regulated Koba–Nielsen factor (A5, A6) is, using A2,

$$\mathrm{KN}(k;Z)
=\lvert Z\rvert^{\alpha'k_1\cdot k_4}\lvert1-Z\rvert^{\alpha'k_2\cdot k_4}
=\lvert Z\rvert^{\alpha'(s_{14}-k_1^2-k_4^2)/2}\,
 \lvert1-Z\rvert^{\alpha'(s_{24}-k_2^2-k_4^2)/2}.\tag{1.5}$$

Multiplying (1.3)–(1.5), the exponent of $\lvert Z\rvert$ is
$\tfrac{\alpha'}2(k_1^2+k_4^2)+\tfrac{\alpha'}2(s_{14}-k_1^2-k_4^2)=\tfrac{\alpha'}2s_{14}$,
and likewise for $\lvert1-Z\rvert$. Momentum conservation gives $s_{14}=s_{23}=u$ and
$s_{24}=s_{13}=t$. Hence, identically in $Z$,

$$\boxed{\;D(k;Z)\,\mathrm{KN}(k;Z)
=c(Z)^{\alpha'\sum_ak_a^2/2}\;\lvert Z\rvert^{\alpha'u/2}\;\lvert1-Z\rvert^{\alpha't/2}.\;}
\tag{1.6}$$

The remaining momentum dependence sits in $\sum_ak_a^2$. With $\sum_ak_a=0$,

$$s+t+u=(k_1+k_2)^2+(k_1+k_3)^2+(k_1+k_4)^2
=3k_1^2+k_2^2+k_3^2+k_4^2+2k_1\!\cdot\!(k_2+k_3+k_4)
=\sum_ak_a^2,\tag{1.7}$$

since $k_2+k_3+k_4=-k_1$. No mass-shell condition was used.

The momentum-blind remainder of the dressing is $\prod_a\rho_a^{-2}$, and by A4 with (1.2)

$$\prod_a\rho_a=c(Z)^4\prod_aP_a
=\beta^{-4}\bigl(\lvert Z\rvert\lvert1-Z\rvert\bigr)^{-2}\cdot
 \lvert Z\rvert^{2}\lvert1-Z\rvert^{2}
=\beta^{-4},\tag{1.8}$$

so $\prod_a\rho_a^{-2}=\beta^{8}$, independent of $Z$. Collecting, the full integrand on the
tile carrying the ordered Mandelstam pair $(x,y)$ is

$$\mathcal I_{(x,y)}(s,t,u;Z)
=\beta^{8}\,c(Z)^{\alpha'(s+t+u)/2}\,
 \lvert Z\rvert^{\alpha'x/2}\,\lvert1-Z\rvert^{\alpha'y/2}.\tag{1.9}$$

\subsection*{Commentary}

- (1.2): the primed product is the content of the $z_3=\infty$ regularisation. The three
  factors $\lvert z_{3b}\rvert$ are individually divergent; A6 removes them from $\rho_3$ and
  from $\mathrm{KN}$ in the same stroke, which is why $P_3=1$ and why $\mathrm{KN}$ has two
  factors rather than five. $\lvert z_{12}\rvert=1$ makes the $s_{12}$ factor trivial, so $s$
  itself never appears explicitly in $\mathrm{KN}$ — it enters only through (1.7).
- (1.4)–(1.5): this is the whole mechanism. $\mathrm{KN}$ carries $-\tfrac{\alpha'}2k_a^2$ for
  each puncture pair the dressing carries $+\tfrac{\alpha'}2k_a^2$ for, because
  $k_a\!\cdot\!k_b$ contains $-\tfrac12(k_a^2+k_b^2)$ and each $P_a$ is built from exactly the
  same $\lvert z_{ab}\rvert$ factors that appear in $\mathrm{KN}$. The cancellation is
  therefore *structural*, not numerical: the dressing's puncture product is the Koba–Nielsen
  product raised to the opposite power. It survives only because $c$ is $a$-independent, so
  that $c$ collects the leftover $\sum_ak_a^2$ into a single power.
- (1.7): this is the off-shell Mandelstam identity. It is an identity of momentum
  conservation, valid for arbitrary virtualities; the familiar on-shell statement
  $s+t+u=\sum m_a^2$ is its restriction. For four tachyons on shell $\alpha'k_a^2=4$ and
  $\alpha'(s+t+u)=16$; the grid this project needs must be free to leave that plane.
- (1.8): this is the `SL: R5` modulus identity $\prod_a\lvert F_a'(0)\rvert=\beta^{-4}$,
  recovered here from A4 rather than assumed. It is also a non-trivial consistency check of
  A4 against an independently ledgered sister result.

\subsection*{Result}

Eq. (1.6) with (1.7): every individual $k_a^2$ cancels pointwise in $Z$, and the integrand's
entire momentum dependence is $c(Z)^{\alpha'(s+t+u)/2}\lvert Z\rvert^{\alpha'u/2}
\lvert1-Z\rvert^{\alpha't/2}$, times the momentum-blind $\beta^{8}$ of (1.8).

\subsection*{Verification}

Checks `C1.1`, `C1.2`, `C1.3` of `codes/verify-stu-reduction.py`: symbolic (sympy, exact
rationals) cancellation of (1.6); the identity (1.7) as a polynomial identity in the four
four-vectors; and (1.8) numerically against `radii_from_maps` (which differentiates the maps)
at sampled $Z\in\mathrm{FD}\cap\mathcal V_{0,4}$ and both $\beta$. Check `C1-twoconfig`
compares the full integrand at two momentum configurations with identical $(s,t,u)$ and
different individual $k_a^2$ — see *Two configurations* below.

### Block 2 — Tile sum and crossing

\subsection*{Setup}

Assumptions A2, A3, A5; claims C1.1–C1.4.

\subsection*{Derivation}

Let $\sigma\in S_4$ act on momentum labels, and write $a=\sigma^{-1}(1)$, $b=\sigma^{-1}(2)$,
$c=\sigma^{-1}(3)$, $d=\sigma^{-1}(4)$. Repeating (1.3)–(1.6) with $k\to\sigma^{-1}k$, the
tile integrand is (1.9) with

$$x=s_{ad},\qquad y=s_{bd}.\tag{2.1}$$

Since $a,b,c$ are the three labels distinct from $d$, the three quantities
$s_{ad},s_{bd},s_{cd}$ are exactly $\{s,t,u\}$ in some order, so $(x,y)$ is an ordered pair
of *distinct* Mandelstams and $z:=s_{cd}$ is the third.

The action of $S_4$ on the cross-ratio $Z$ has kernel the Klein four-group
$V=\{e,(12)(34),(13)(24),(14)(23)\}$, and $S_4/V\cong S_3$ acts faithfully on
$\{s,t,u\}$ — indeed $V$ fixes $s=s_{12}=s_{34}$, $t=s_{13}=s_{24}$, $u=s_{14}=s_{23}$ each.
The $S_3$ factor of $G$ (A5) is a set of coset representatives, so as $g$ runs over it,
$(x,y)$ runs over the six ordered pairs of distinct Mandelstams exactly once. The
$\mathrm{conj}$ factor acts as $Z\mapsto\bar Z$, under which (1.9) is invariant (it depends on
$Z$ through $\lvert Z\rvert$ and $\lvert1-Z\rvert$ only) and which leaves the momenta
untouched; it contributes an overall factor 2. Hence

$$\{T^4\}_{\rm contact}(s,t,u)
=2C\sum_{(x,y)}\int_{\mathrm{FD}\cap\mathcal V_{0,4}}
 \mathcal I_{(x,y)}(s,t,u;Z)\,d^2Z,\tag{2.2}$$

the sum running over the six ordered pairs. Inserting
$c(Z)^{\alpha'(s+t+u)/2}=\beta^{-\alpha'(s+t+u)/2}
\bigl(\lvert Z\rvert\lvert1-Z\rvert\bigr)^{-\alpha'(s+t+u)/4}$ and using $s+t+u=x+y+z$,

$$\frac{\alpha'x}2-\frac{\alpha'(x+y+z)}4=\frac{\alpha'(x-y-z)}4,\qquad
\frac{\alpha'y}2-\frac{\alpha'(x+y+z)}4=\frac{\alpha'(y-x-z)}4,\tag{2.3}$$

so that

$$\boxed{\;\{T^4\}_{\rm contact}(s,t,u)
=2C\,\beta^{\,8-\alpha'(s+t+u)/2}\!\!\!\sum_{(x,y,z)\in S_3\cdot(s,t,u)}\;
 \int_{\mathrm{FD}\cap\mathcal V_{0,4}}
 \lvert Z\rvert^{\frac{\alpha'}4(x-y-z)}\,
 \lvert1-Z\rvert^{\frac{\alpha'}4(y-x-z)}\,d^2Z.\;}\tag{2.4}$$

\subsection*{Commentary}

- (2.1): the tile does not move the integration region; it permutes the momentum labels, which
  is the equivariant form of A5. The region and the radii $\rho_a^{\rm FD}(Z)$ are the same on
  every tile, which is why the $(x,y)$ label is the *only* thing that distinguishes tiles.
- The $S_4/V$ statement is what makes the answer crossing symmetric rather than merely
  symmetric under a subgroup: the six cosets exhaust the permutations of $\{s,t,u\}$, and
  the sum over them of a fixed function of $(x,y)$ is a totally symmetric function of
  $(s,t,u)$. Total crossing symmetry is thus *derived from the equivariant assembly A5*
  rather than assumed separately: given that A5 sums over a transversal of $V$, the six
  reduced tiles exhaust the permutations of $(s,t,u)$ and their sum is symmetric. Crossing
  of the vertex itself is an input of A5, not a result of this record.
- (2.4): the $\beta$-prefactor is exact and carries all of the $\beta$ dependence outside the
  integral only because of (1.8); the integrals themselves still depend on $\beta$ through the
  region $\mathcal V_{0,4}(\beta)$.
- Convergence: the exponents in (2.4) are real, and the integrand is a positive power-law in
  $\lvert Z\rvert$ and $\lvert1-Z\rvert$. The region $\mathrm{FD}\cap\mathcal V_{0,4}$ is
  compact and bounded away from $Z=0$ and $Z=1$ for $\beta>\beta_{04}$ (the fundamental domain
  has $\lvert Z\rvert\ge1$, $\mathrm{Re}\,Z\le\tfrac12$), so each integral is finite for
  *every* complex $(s,t,u)$: the contact term is entire in the momenta, as `SL: R10` states.

\subsection*{Result}

Eq. (2.4). $\{T^4\}_{\rm contact}$ is a totally symmetric function of $(s,t,u)$ and of
nothing else.

\subsection*{Verification}

Check `C2`: the unreduced 12-tile sum, built from `radii_from_maps` and the unreduced
$\mathrm{KN}$, agrees with (2.4) pointwise in $Z$ and after quadrature. Check `C2-crossing`:
the value of (2.4) is invariant under all six permutations of $(s,t,u)$ at fixed $\beta$,
including at points with $\alpha'(s+t+u)\ne16$.

### Block 3 — Two configurations

\subsection*{Setup}

The substance of the numerical falsification test. Two momentum configurations with the same
$(s,t,u)$ but different individual $k_a^2$; A2 throughout.

\subsection*{Derivation}

The map $(k_1,\dots,k_4)\mapsto(k_a^2;s,t,u)$ has, at fixed $(s,t,u)$, a three-parameter
family of preimages modulo the single constraint (1.7). A convenient explicit pair, in
$D=26$ with $\alpha'=1$ and $\sum_ak_a=0$, is built from a common $(s,t,u)$ and
$\sum_ak_a^2=s+t+u$ with the $k_a^2$ redistributed:

| | $\alpha'k_1^2$ | $\alpha'k_2^2$ | $\alpha'k_3^2$ | $\alpha'k_4^2$ | $\alpha's$ | $\alpha't$ | $\alpha'u$ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| config **X** | $4$ | $4$ | $4$ | $4$ | $2.0$ | $5.0$ | $9.0$ |
| config **Y** | $-1$ | $7$ | $3$ | $7$ | $2.0$ | $5.0$ | $9.0$ |

Both satisfy $\sum_a\alpha'k_a^2=16=\alpha'(s+t+u)$, so both are legitimate configurations of
four momenta with $\sum_ak_a=0$ (check `C1-configs-realisable` calls the script's `realise`
routine to construct explicit 26-vectors for each row and verifies conservation and every
invariant, rather than assuming realisability from the Gram-matrix eigenvalue count alone).
The
individual $k_a\!\cdot\!k_b$ differ between X and Y — e.g.
$\alpha'k_1\!\cdot\!k_4=\tfrac12(\alpha'u-\alpha'k_1^2-\alpha'k_4^2)$ is
$\tfrac12(9-8)=0.5$ for X and $\tfrac12(9+1-7)=1.5$ for Y — so the dressing and $\mathrm{KN}$
each differ pointwise in $Z$; only their product agrees. That is why the check is not vacuous.

A second pair is used **off** the on-shell sum plane, with $\alpha'(s+t+u)=6\ne16$:

| | $\alpha'k_1^2$ | $\alpha'k_2^2$ | $\alpha'k_3^2$ | $\alpha'k_4^2$ | $\alpha's$ | $\alpha't$ | $\alpha'u$ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| config **X′** | $1$ | $1$ | $2$ | $2$ | $-4.0$ | $5.0$ | $5.0$ |
| config **Y′** | $-1$ | $3$ | $0$ | $4$ | $-4.0$ | $5.0$ | $5.0$ |

All four are realisable in $\mathbb R^{1,25}$: the Gram matrix of $(k_1,k_2,k_3)$ built from
the invariants has at most one negative eigenvalue in each case (0 for X, 1 for Y, X′, Y′),
and check `C1-configs-realisable` runs the script's `realise` routine on all four,
confirming it produces explicit 26-vectors with $\sum_ak_a=0$ reproducing every declared
invariant to $10^{-9}$. Configuration X is the equal-mass on-shell tachyon point
$\alpha'k_a^2=4$; Y shares its $(s,t,u)$ while being off shell on every leg.

\subsection*{Result}

Under C1, the full integrand — and hence the tile sum — takes the same value on X and Y, and
on X′ and Y′, at every $Z$.

\subsection*{Verification}

Check `C1-configs-realisable` (realisability of X, Y, X′, Y′ as explicit 26-vectors, machine
checked). Check `C1-twoconfig` (pointwise, sampled $Z$, both $\beta$), and
`C1-twoconfig-integrated` (after quadrature). Break leg `BREAK-mandelstam` swaps the $t$ and
$u$ assignments in $\mathrm{KN}$ and is confirmed to fire.

### Block 4 — Limits

\subsection*{Setup}

Claims C1.3, C1.4; A7, A8.

\subsection*{Derivation}

**Equal masses.** Put $k_a^2\equiv k^2$. Then the dressing factorises before any use of
(1.6):

$$\prod_a\rho_a^{\alpha'k^2/2-2}=\Bigl(\prod_a\rho_a\Bigr)^{\alpha'k^2/2-2}
=\bigl(\beta^{-4}\bigr)^{\alpha'k^2/2-2}=\beta^{\,8-2\alpha'k^2},\tag{4.1}$$

a single $Z$-independent prefactor on every tile — `SL: R6` in the `SL: R10` assembly.
Consistency with (2.4): on this locus $s+t+u=4k^2$ by (1.7), so
$\beta^{8-\alpha'(s+t+u)/2}=\beta^{8-2\alpha'k^2}$, the same prefactor. The residual
$\lvert Z\rvert,\lvert1-Z\rvert$ exponents of (2.4) then match the equal-mass
$\mathrm{KN}$ exponents term by term: e.g.
$\tfrac{\alpha'}4(u-t-s)=\tfrac{\alpha'}2u-\alpha'k^2=\alpha'k_1\!\cdot\!k_4$.

**$k=0$.** All invariants vanish, (2.4) collapses to

$$\{T^4\}_{\rm contact}(0,0,0)=2C\beta^{8}\cdot6\cdot\mathrm{Vol}(\mathrm{FD}\cap\mathcal
V_{0,4})=12\,C\,\mathrm{Vol}(\mathrm{FD}\cap\mathcal V_{0,4})\,\beta^{8},\tag{4.2}$$

the Stage 0 value of `SL: R7`/`SL: R10`.

\subsection*{Commentary}

*Why the equal-mass $k^2$ dependence is not a contradiction.* An $(s,t,u)$-only function
restricted to a locus on which $(s,t,u)$ themselves depend on $k^2$ will of course depend on
$k^2$. The equal-mass line is such a locus: $s+t+u=4k^2$ fixes $k^2$ as a function of the
invariants. The content of C1 is that $k^2$ enters *only* through this combination — two
equal-mass configurations with the same $(s,t,u)$ necessarily have the same $k^2$, so the
equal-mass line cannot by itself distinguish a six-parameter object from a three-parameter
one. That is exactly why an equal-mass-only test cannot distinguish the two objects, so the reduction was left
untested, and why the two-configuration test of Block 3 is the load-bearing check.

\subsection*{Verification}

Checks `C3.1` (the prefactor (4.1) against $\beta^{8-2\alpha'k^2}$ at sampled $k^2$ and both
$\beta$, with radii from `radii_from_maps`) and `C3.2` ((4.2) against a direct quadrature of
the $k=0$ tile sum, and against $12\beta^{8}\mathrm{Vol}$).

### Block 5 — Regime of validity

\subsection*{Setup}

Claim C4. What the reduction uses, and what would break it.

\subsection*{Derivation and discussion}

**The load-bearing property.** Exactly one: in A4 the prefactor $c(Z)$ does not depend on the
puncture label $a$. Equivalently, $\rho_a=\lvert\kappa_a\rvert\,\lvert S_0(Z)\rvert$ with
$\kappa=\bigl(1,\ (1-Z)/Z,\ 1/Z,\ Z-1\bigr)$ and $\lvert S_0\rvert=\lvert
Z\rvert^{1/2}/(\beta\lvert Z-1\rvert^{1/2})$: all the puncture dependence sits in $\kappa_a$,
which is precisely the Koba–Nielsen product $P_a$ up to an $a$-independent factor. This is
the sister project's "$\gamma_a=1$ for every puncture", i.e. the Möbius character of the
vertex maps.

**What a puncture-dependent prefactor would do.** With $\rho_a=c_a(Z)P_a$, eq. (1.6) becomes

$$D\,\mathrm{KN}=\prod_ac_a(Z)^{\alpha'k_a^2/2}\;
\lvert Z\rvert^{\alpha'u/2}\lvert1-Z\rvert^{\alpha't/2},\tag{5.1}$$

and $\prod_ac_a^{\alpha'k_a^2/2}$ is a function of the four $k_a^2$ separately whenever the
$c_a$ are not all equal. Writing $c_a=c\,e^{\gamma_a}$, the obstruction is
$\exp\bigl[\tfrac{\alpha'}2\sum_a\gamma_a(Z)k_a^2\bigr]$: it reduces to $(s,t,u)$ iff all
$\gamma_a$ coincide (then $\sum_a\gamma k_a^2=\gamma(s+t+u)$). So the reduction is an
*if and only if* statement about the section, not a generic feature.

**Variation of $S$.** The second-point map $S$ enters only as the $a$-independent factor:
$\rho_a=\lvert\kappa_aS\rvert$. Any other choice $S\to\tilde S(Z)$ therefore keeps A4's form
with $c=\lvert\tilde S\rvert$ and the reduction is untouched — only the explicit
$c(Z)^{\alpha'(s+t+u)/2}$ in (1.9) changes, and with it (1.8): using $\lvert\kappa_a\rvert
=P_a/\lvert Z\rvert$,
$$\prod_a\rho_a=\lvert\tilde S\rvert^4\prod_a\lvert\kappa_a\rvert
=\lvert\tilde S\rvert^4\,\frac{\lvert1-Z\rvert^2}{\lvert Z\rvert^2},$$
which is constant in $Z$ only for $\lvert\tilde S\rvert\propto\lvert Z\rvert^{1/2}
/\lvert1-Z\rvert^{1/2}$, i.e. for $S_0$ itself up to a constant. So the clean $\beta^8$ of
(2.4) is special to $S=S_0$ while the $(s,t,u)$ reduction is not. The sister project has
**not** varied $S$; the reduction does not need them to.

**Variation of $\Lambda_1$.** $\Lambda_1$ (the $C^1$ weight, with the values of $\lambda$ used by the companion project: (companion value, not reproduced here)) enters the *interior* point map $R(Z,\bar Z;\beta)$, which is
level-$(1,1)$ machinery. It does not enter the mapping radii: by A4, $c(Z)=\beta^{-1}
(\lvert Z\rvert\lvert1-Z\rvert)^{-1/2}$ and the $P_a$ of (1.2) contain only $Z$ and $\beta$,
so $\Lambda_1$ cannot enter $\rho_a$ given A4's closed form. The reduction is therefore
exactly $\lambda$-independent. The script's `C4.2-lambda` corroborates this by an
`inspect.signature` guard on the sister module (`radii_closed_form`, `radii_from_maps` and
the maps $F_1$–$F_4$, `q_of_Z` take no `lam` parameter) — an API fact, not itself a
mathematical statement about $\rho_a$ as a function value; the mathematical argument is A4's
closed form above.

**The $z_3=\infty$ regularisation.** A6 enters twice: it defines $P_3=1$ (equivalently
$\rho_3$ in the $t=1/z$ chart) and it removes the three $\lvert z_{3b}\rvert^{\alpha'k_3k_b}$
factors from $\mathrm{KN}$. The two removals must be the *same* prescription, since the
cancellation of (1.4) against (1.5) is factor by factor. Regulating one side and not the other
leaves an uncancelled $\lvert z_{3b}\rvert$-dependence, which is divergent, not merely a
$k_a^2$ residue. The prescription is imported (A6); this record does not re-derive it, and a
different consistent prescription (e.g. keeping a finite cutoff $\lvert z_3\rvert=\Lambda$ on
both sides) would change $c$ by an $a$-independent factor and hence, by the paragraph above,
leave the reduction intact.

**Scope — what this result does not cover.**

1. Tachyons only. The reduction uses the dressing exponent $\alpha'k_a^2/2-2$ of A7. For a
   level-$(1,1)$ external state the dressing exponent shifts by the oscillator level and the
   local-frame rotation $\arg F_a'(0)$ enters, which the modulus $\rho_a$ does not see. The
   statement made here is about $\{T^4\}$ and about no other coupling.
2. Contact term only. The s/t/u Feynman-region exchange contributions carry region-specific
   radii $\rho_a^{(c)}$ and are outside A5; nothing here bears on them.
3. The declared section, $\beta>\beta_{04}$; numerically exercised at $\beta\in\{3/2,2\}$.
4. The reduction is a statement about the *integrand*. It does not by itself say that the
   resulting three-parameter function is smooth, bounded, or numerically tractable on the box
   needed for $K_P$ — that is record 045's question.
5. It does not establish A4 or A5. Both are imported from the sister project and inherit that
   project's scope, including the §C.2 caveat addressed in Block 6.

### Block 6 — The residual weight on $\rho_3$

\subsection*{Setup}

Claim C5. Let $\mu>0$ be a momentum-independent constant.

\subsection*{(i) What survives analytically**

**Case A: $\rho_3\to\mu\rho_3$.** The Koba–Nielsen factor is built from the $z_{ab}$ and is
untouched; only the dressing changes. On tile $g$, the puncture at position 3 carries momentum
$k_{c_g}$ with $c_g:=\sigma_g^{-1}(3)$, so the tile integrand acquires

$$\mu^{\alpha'k_{c_g}^2/2-2}.\tag{6.1}$$

The $\mu^{-2}$ is the same on every tile and is an overall constant $\mu^{-2}$ on
$\{T^4\}_{\rm contact}$ — invisible to any momentum-structure test. The factor
$\mu^{\alpha'k_{c_g}^2/2}$ is not: the deformed sum is

$$\{T^4\}^{\mu}_{\rm contact}=\mu^{-2}\,2C\sum_{(x,y)}\mu^{\alpha'k_{c(x,y)}^2/2}
\int_{\mathrm{FD}\cap\mathcal V_{0,4}}\mathcal I_{(x,y)}(s,t,u;Z)\,d^2Z,\tag{6.2}$$

a linear combination of the six reduced tile integrals with coefficients depending on
*individual* virtualities. Two configurations with the same $(s,t,u)$ and different $k_a^2$
give different values for generic $\mu\ne1$, so the $(s,t,u)$ reduction is a genuine falsifier
for this weight. This is C5.1.

**Case B: $c\to\mu c$, i.e. $\rho_a\to\mu\rho_a$ for all four.** Then
$\prod_a\rho_a^{\alpha'k_a^2/2-2}$ acquires $\mu^{\alpha'\sum_ak_a^2/2-8}
=\mu^{\alpha'(s+t+u)/2-8}$ by (1.7), the same on every tile. Hence

$$\{T^4\}^{\mu\,c}_{\rm contact}(s,t,u)=\mu^{\alpha'(s+t+u)/2-8}\,
\{T^4\}_{\rm contact}(s,t,u).\tag{6.3}$$

The object stays a function of $(s,t,u)$ alone and stays totally crossing symmetric.

A sharper accident is worth recording, because it is a trap for anyone who tests Case B on the
natural kinematics: on the four-tachyon shell sum $\alpha'(s+t+u)=16$ the exponent in (6.3)
is $8-8=0$ and the common weight drops out **exactly**, for every $\mu$. A Case-B test run at
the on-shell sum plane therefore reports "no effect" for a reason that has nothing to do with
the structure under test. The script's `BREAK-c` leg is run at $\alpha'(s+t+u)=6$ for that
reason, and the check `C5.2-onshellsum` records both behaviours side by side.

No test in
this record — reduction, crossing, equal-mass collapse (which would read
$\beta^{8-2\alpha'k^2}\mu^{2\alpha'k^2-8}$ and simply redefines the prefactor), $k=0$ (which
reads $12C\mathrm{Vol}\,\beta^8\mu^{-8}$ and is indistinguishable from a rescaling of $C$ or
of the Stage 0 anchor) — can see it. This is C5.2.

\subsection*{(iii) Is Case A a crossing violation?}

Only under a choice that A5 does not make. The group in A5 is $G=S_3\times\mathrm{conj}$ of
order 12, and its $S_3$ is a set of coset representatives of $V$ in $S_4$. As shown in Block 2,
the tile's reduced content — the ordered pair $(x,y)$ — depends only on the coset, whereas
$c_g=\sigma_g^{-1}(3)$ does not: $V$ acts simply transitively on $\{1,2,3,4\}$, so across one
coset $\sigma^{-1}(3)$ takes all four label values. **The undeformed object is blind to this
ambiguity precisely because of the cancellation of Block 1; the deformed object is not.** So
"which momentum sits at the regulated puncture" is a piece of data the package leaves
unfixed, and it becomes the whole content of the question.

Under the natural representative choice used in the script — fix $\sigma^{-1}(4)=4$ and let
$\sigma^{-1}$ permute $\{1,2,3\}$ over the three remaining positions — the six tiles are

| $(a,b,c)=(\sigma^{-1}1,\sigma^{-1}2,\sigma^{-1}3)$ | $x=s_{a4}$ | $y=s_{b4}$ | $c$ |
| --- | --- | --- | --- |
| $(1,2,3)$ | $u$ | $t$ | 3 |
| $(1,3,2)$ | $u$ | $s$ | 2 |
| $(2,1,3)$ | $t$ | $u$ | 3 |
| $(2,3,1)$ | $t$ | $s$ | 1 |
| $(3,1,2)$ | $s$ | $u$ | 2 |
| $(3,2,1)$ | $s$ | $t$ | 1 |

(using $s_{14}=u$, $s_{24}=t$, $s_{34}=s$). The six ordered pairs are covered exactly once, as
required; the multiset of regulated-puncture labels is $\{1,1,2,2,3,3\}$ — label 4 never
appears. So (6.2) weights the tile carrying $(x,y)=(u,t)$ by $\mu^{\alpha'k_3^2/2}$ and the
tile carrying $(t,u)$ by the same, but the pair $(u,s)$ and $(s,u)$ by $\mu^{\alpha'k_2^2/2}$.
Relabelling $2\leftrightarrow3$ exchanges $t\leftrightarrow s$ and $k_2^2\leftrightarrow
k_3^2$; the deformed sum is then *not* invariant, because the coefficient attached to a given
Mandelstam pair does not follow the relabelling. Concretely, the deformed object fails total
$(s,t,u)$ symmetry as soon as two of the $k_a^2$ differ; the script measures this.

Answer to (iii): **yes for a puncture-selective weight** — the violation shows as a failure of crossing symmetry under
permutations moving puncture 3 — but the statement is representative-dependent, and what is
representative-*in*dependent is the weaker and sharper statement C5.1: the weight destroys the
$(s,t,u)$ reduction. The reduction test is therefore the falsifier to quote, not the crossing
test.

\subsection*{(iv) Case A versus Case B, and what this project cannot see}

- Case A (selective) is visible: it breaks the reduction, which is a property this project
  tests directly (`BREAK-rho3`).
- Case B (common) is invisible to every momentum-structure test: it is absorbed as
  $\mu^{\alpha'(s+t+u)/2-8}$, a reparametrisation of the answer (`BREAK-c`, which is
  confirmed to leave the reduction and crossing checks passing while changing the value).
- **The sister project's §C.2 gap is not closed here** (C5.4). Their statement is that a
  $\sigma$-independent residual weight on $\rho_3$ cancels between their comparator and their
  claim. On this side the same obstruction holds, for the same reason: the shipped module
  obtains $\rho_3$ as $\lvert(1/F_3)'(0)\rvert$ with $F_3:=Z/F_1$ (derivation 003 eq. (1)), so
  `radii_from_maps` and `radii_closed_form` are two routes to the *same* definition and agree
  on $\rho_3=\rho_1/\lvert Z\rvert$ by construction. There is no independent determination of
  $\rho_3$ available here. What this record establishes is narrower and still useful: *if* a
  puncture-selective weight were present, the $(s,t,u)$ reduction would fail, and the
  reduction is testable against the delivered module at no extra cost. Since the reduction
  passes at $10^{-13}$, a selective weight is excluded *relative to the module's own
  definitions* — which is a consistency statement about the module, not an independent
  determination of $\rho_3$.
- Actually closing the gap requires a determination of $\rho_3$ that does not route through
  the Klein relation: e.g. the $t=1/z$ chart map at $z_3=\infty$ constructed directly from the
  plumbing data, or the $S_4$ relabelling to the $t$-channel maps (which the package
  explicitly does not ship). Closing the gap needs such a determination, outside this record.

## Interpretation — what this means for the pair kernel

The object this project needs is
$K_P(k;k')=V_4\bigl(T(k)T(P-k),\,T(k')T(P-k')\bigr)$: the tachyon-pair block of the $\Sigma$
line at total momentum $P$, an integral kernel in the relative momenta of the two pairs. Its
four external momenta are $k_1=k$, $k_2=P-k$, $k_3=-k'$, $k_4=-(P-k')$, and the intermediate
pairs are off shell with $k^2\ne(P-k)^2$: that asymmetry is exactly what made a six-parameter
grid look necessary.

Under C1, $K_P$ depends on $(k,k')$ only through $(s,t,u)$, and on that locus
$s=(k_1+k_2)^2=P^2$ is *fixed*. So at fixed $P^2$ the kernel is a function of two invariants,
$t$ and $u$, with $t+u=\sum_ak_a^2-P^2$ determined by the four virtualities. Three consequences:

1. The individual virtualities $k^2$, $(P-k)^2$, $k'^2$, $(P-k')^2$ enter **only** through
   their sum, and that sum is $s+t+u$. The kernel is not a function of the relative momenta in
   any finer sense.
2. Total crossing symmetry in $(s,t,u)$ is a symmetry of the kernel, hence in particular
   $K_P(k;k')$ is symmetric under $t\leftrightarrow u$, which is the exchange of the two
   strands of one pair. That symmetry is a free, exact check on any discretisation.
3. The discretisation box is a box in $(t,u)$ at each $P^2$, two-dimensional and bounded by a
   crossing-symmetric region, not a four-dimensional box in the virtualities. This is the
   premise record 045 takes as given, and it holds.

One caveat travels with this result. The reduction is verified against the sister module's
own definitions, and that module fixes $\rho_3$ through the Klein relation $F_3:=Z/F_1$; a
residual momentum-independent weight inserted in the *definition* of $\rho_3$ is therefore
invisible here (C5.4). What is excluded is a weight inserted downstream, which would break
the $(s,t,u)$ reduction.

## Verification summary

`codes/verify-stu-reduction.py`, run under `.venv/bin/python`, seed `20260921` printed.
**32 named checks, 32 PASS, 0 FAIL**, of which **5** are break-on-purpose legs
(`BREAK-cancel`, `BREAK-conservation`, `BREAK-r5`, `BREAK-mandelstam`, `BREAK-rho3`), all
confirmed to fire (written as assertions that the corrupted quantity *does* deviate, so a
non-firing leg reports FAIL rather than being silently ignored). `BREAK-c` is not such a
leg: it is a positive demonstration that a common weight on all four $\rho_a$ leaves the
reduction and crossing checks passing while moving the value (C5.2). `C5.2-pointwise` is a
consistency check, not an independent determination — it cannot fail, because the
deformation factor is shared by construction between the two configurations it compares;
`C5.2-onshellsum` is the check that establishes C5.2's behaviour. `C1-configs-realisable`
machine-checks the realisability of configurations X, Y, X′, Y′ via the script's `realise`
routine (previously described in prose only). One caveat carries over from the
Interpretation section: `radii_from_maps`/`radii_closed_form` obtain $\rho_3$ through the
same Klein relation $F_3=Z/F_1$, so a momentum-independent weight inserted in $\rho_3$'s
*definition* is not visible to any check here (C5.4); what is excluded is a weight inserted
downstream. $\alpha'=1$ in the numerics; momenta quoted as $\alpha'k_a^2$. Quadrature:
midpoint grid $220\times220$ over the bounding box of $\mathrm{FD}\cap\mathcal V_{0,4}$ with
the `in_FD_cap_V04` mask, cross-checked against a $4\times10^5$-point Monte-Carlo area at
$3\times10^{-3}$. Representative numbers: $\rho$-route agreement $4.4\times10^{-13}$;
two-configuration pointwise agreement $1.0\times10^{-12}$; after quadrature
$4.4\times10^{-14}$; $\prod_a\rho_a\beta^4-1\le6.7\times10^{-13}$; crossing spread
$2\times10^{-16}$ — all unchanged from the previous run.

| Check | Node | What it tests | Falsifiable because |
| --- | --- | --- | --- |
| `C1.1-symbolic` | C1.1 | sympy: (1.6) as an exact identity in symbolic $k_a^2,s,t,u$ | perturbing one exponent leaves a non-zero residue |
| `C1.2` | C1.2 | $\sum_ak_a^2=s+t+u$ on explicit random 26-vectors with $\sum k_a=0$ | fails on vectors violating conservation |
| `C1.3` | C1.3 | $\prod_a\rho_a=\beta^{-4}$ from `radii_from_maps` (differentiates the maps) | independent route; compares to a literature constant |
| `C1.3-cform` | C1.3 | `radii_closed_form` vs `radii_from_maps`, all four $a$ | two independent routes to $\rho_a$ (except $\rho_3$, see C5.4) |
| `C1.4-aindep` | C4.1 | $\rho_a/P_a$ is the same for all four $a$, from `radii_from_maps` | a puncture-dependent prefactor would show as a spread (for $a\in\{1,2,4\}$; the $a=3$ entry equals the $a=1$ entry by the Klein relation, same caveat as C5.4) |
| `C1-configs-realisable` | (Block 3) | `realise` produces explicit 26-vectors for X, Y, X′, Y′ reproducing $\sum_ak_a=0$ and every declared invariant | fails on a Gram matrix/eigenbasis that does not reproduce the declared $k_a^2,s,t,u$ |
| `C1-twoconfig` | C1 | integrand at X vs Y, and X′ vs Y′, pointwise in $Z$, both $\beta$ | the two configs have different $k_a\!\cdot\!k_b$ |
| `C1-twoconfig-integrated` | C1 | same, after quadrature over $\mathrm{FD}\cap\mathcal V_{0,4}$ | ditto |
| `C2` | C2 | unreduced 12-tile sum vs closed form (2.4) | two independent assemblies |
| `C2-crossing` | C2 | (2.4) invariant under all 6 permutations of $(s,t,u)$, on and off $\alpha'(s+t+u)=16$ | tests that the six representatives cover the six ordered Mandelstam pairs exactly once (a defective `REPS` table would show as a spread); run with `reduced=True`, so `ksq`/`kdot` are unused and the sum is symmetric by construction — crossing of the assembly itself is tested by `C2-crossing-unreduced`, not by this check |
| `C3.1` | C3.1 | equal-mass prefactor $=\beta^{8-2\alpha'k^2}$ | consistency with C1.3 (the prefactor is $(\prod_a\rho_a)^{\alpha'k^2/2-2}$, so this holds as soon as C1.3 does); not an independent determination |
| `C3.2` | C3.2 | $k=0$ tile sum $=12C\mathrm{Vol}\,\beta^8$ | consistency with C1.3 in the same grid, modulo the region volume; the volume itself is cross-checked by an independent quadrature (`vol` vs `vol_mc`), which is the one independent clause |
| `C4.2-lambda` | C4.2 | `radii_from_maps`/`radii_closed_form`/`F1`–`F4`/`q_of_Z` take no `lam` parameter, while `weight_lambda1` does depend on it | an API guard on the sister module's signatures, not a numerical statement about $\rho_a$ as a function value; the mathematical argument is A4's closed form, which contains only $Z$ and $\beta$ (Block 5) |
| `C5.1` | C5.1 | (6.2): deformed sum differs between X and Y | — |
| `C5.2` | C5.2 | (6.3): deformed sum $=\mu^{\alpha'(s+t+u)/2-8}\times$ undeformed | — |
| `C5.3` | C5.3 | deformed ($\rho_3$) sum fails $(s,t,u)$ permutation symmetry | — |
| `BREAK-rho3` | C5.1 | reduction check re-run with $\mu=1.3$ on $\rho_3$ → must FAIL | fires |
| `C5.2-onshellsum` | C5.2 | the common weight drops out exactly at $\alpha'(s+t+u)=16$ but not off it | contrasts two kinematic planes |
| `BREAK-c` | C5.2 | reduction and crossing re-run with $\mu=1.3$ on $c$, **off** the shell-sum plane → must still PASS, value must move | fires (value moves by $0.73$) |
| `BREAK-conservation` | C1.2 | (1.7) re-run on four unconstrained momenta → must FAIL | fires |
| `C1-twoconfig-nontrivial` | C1 | the two configurations do have different $k_a\!\cdot\!k_b$ | guards against a vacuous comparison |
| `BREAK-mandelstam` | C1 | $t\leftrightarrow u$ swapped in $\mathrm{KN}$ → reduction must FAIL | fires |
| `BREAK-cancel` | C1.1 | dressing exponent $\alpha'k_a^2/2\to\alpha'k_a^2/3$ → (1.6) must FAIL | fires |
| `BREAK-r5` | C1.3 | $\prod\rho_a$ compared to $\beta^{-3}$ → must FAIL | fires |

## Proposed ledger row

**Result.** In the SL(2,C) project's declared section ($S=S_0$, $\beta>\beta_{04}$), the
off-shell four-tachyon contact integrand of the equivariant 12-tile assembly A5 depends on
the external momenta only through $(s,t,u)$, pointwise in the moduli parameter $Z$ and per
tile (C1–C2); the individual $k_a^2$ cancel identically using only $\sum_ak_a=0$, with no
mass-shell input. The reduction is an *iff* statement: it holds exactly when the mapping
radii's prefactor $c(Z)$ is $a$-independent (C4), which is the section's actual property
(A4). At fixed $P^2=s$, the pair kernel $K_P(k;k')$ needed by record 045 is therefore a
function of two invariants $(t,u)$, not four virtualities, with an exact
$t\leftrightarrow u$ crossing check on any discretisation.

**Status.** `Conditional(A4, A5) – Verified`. A4 (mapping radii closed form, sister
`SL: R51`) and A5 (equivariant tile assembly, sister `SL: R6`/`SL: R10`) are imported, not
re-derived here, and carry the sister project's own ledger status for those rows; the
result stated above is unconditional given A1–A9 of this record but inherits whatever
conditionality A4/A5 carry on the sister side. No hypothesis of this record's own is left
open (Hypotheses in force: none).

**Scope** (record 044, Block 5): tachyons only, via the dressing exponent A7; the contact
term only, not the s/t/u exchange contributions (A5); the declared section and
$\beta>\beta_{04}$, exercised numerically at $\beta\in\{3/2,2\}$; a statement about the
integrand, not about smoothness/tractability of the resulting kernel on the discretisation
box (record 045's question); it does not establish A4 or A5 themselves.

**Negative result carried by this row (C5.4).** This record does **not** close the sister
project's §C.2 gap on $\rho_3$: the shipped module obtains $\rho_3$ through the Klein
relation $F_3:=Z/F_1$, so every check here is run against that definition and cannot detect
a momentum-independent weight folded into it. What is established is narrower: *if* such a
weight were inserted downstream of that definition (on one puncture selectively), the
$(s,t,u)$ reduction would fail and is a working falsifier against the delivered module
(`BREAK-rho3`); a weight common to all four punctures is invisible to every
momentum-structure test run here (C5.2), including crossing. Closing the sister gap
requires a determination of $\rho_3$ that does not route through the Klein relation, which is outside this record.

**Feeds**: PH1 (ii), PH3, PH18, R29-H1/H2 (via record 045's pair-kernel discretisation).
