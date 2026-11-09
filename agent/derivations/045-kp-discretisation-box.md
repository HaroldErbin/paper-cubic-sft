# 045 — The discretisation box for the $\Sigma$-channel pair kernel $K_P$

## Task and objective

**Literal task.** Fix, with reasons, the three values of $P^2$ and the range of the remaining two
Mandelstam invariants over which the sister SL(2,C) project must tabulate the four-tachyon
contact term, so that this project can discretise the pair kernel
$$K_P(k;k')=V_4\bigl(T(k)\,T(P-k),\;T(k')\,T(P-k')\bigr).$$

**Motivating objective.** The sister project is blocked on this number before it produces the
grid. Too small a box silently truncates the relative-momentum content of PH3's partial sums;
too large a box costs quadrature evaluations. The deliverable is a box with a stated stability
criterion.

## Conventions and assumptions

- **A1** Mostly-plus signature, $\alpha'$ explicit; numbers below are quoted in units $\alpha'=1$
  unless $\alpha'$ is written. Tachyon shell $\alpha'k_a^2=+4$. All momenta incoming, so
  $s=(k_1+k_2)^2$, $t=(k_1+k_4)^2$, $u=(k_1+k_3)^2$ and $s+t+u=\sum_ak_a^2$. The pair momentum is
  $P=k_1+k_2$, hence $P^2=s$. (The project conventions; this is the convention in which the
  $\alpha'(s+t+u)=16$ on-shell statement is written.)
- **A2** (Companion value, not reproduced here: the declared parameter set), tachyon-pair block only. The moduli region is
  $\mathrm{FD}\cap\mathcal V_{0,4}$ with $\mathrm{FD}=\{\operatorname{Im}Z\ge0,\ |Z|\ge1,\
  \operatorname{Re}Z\le1/2\}$ and $\mathcal V_{0,4}$ the closed ellipse centred at $1/2$ with
  semi-axes $a=\beta^2+1/(16\beta^2)$, $b=\beta^2-1/(16\beta^2)$ (`local_coordinates.py`,
  `in_FD_cap_V04`, `ellipse_axes`; the ellipse is the $\lvert q\rvert=1$ boundary of ledger R2).
- **A3** The $(s,t,u)$ reduction of record 044 is an **input**, not re-derived here: the momentum
  dependence of the contact integrand is
  $c(Z)^{\alpha'(s+t+u)/2}|Z|^{\alpha'u/2}|1-Z|^{\alpha't/2}$ with
  $c(Z)=\beta^{-1}(|Z||1-Z|)^{-1/2}$, times a momentum-blind factor $\prod_a\rho_a^{-2}$,
  integrated over $\mathrm{FD}\cap\mathcal V_{0,4}$ and summed over the 12-element equivariant
  group with permuted Mandelstams (R10).
- **A4** The overall constant $C$ (the sister's $C_4$) is the only free multiplicative constant in
  play; it is fixed independently of anything tested here (`SL: R8`, R37) and cancels from every
  ratio used to set the box. Nothing is fitted.
- **A5** The sister$\to$book rescaling ($V_4\times\tfrac12$, R43) is a momentum-independent
  factor, so the box, the growth law and the sampling are invariant under it. **No convention
  conversion is performed or needed here**; magnitudes quoted from the sister package are in the
  sister's convention and labelled as such.

## The three $P^2$ values (checkpoint)

| Point | Value | One-line justification |
| --- | --- | --- |
| First plumbing-lattice value | $\alpha'P^2=4$ | exact: the plumbing lattice is $P_I^2=-\tfrac2{\alpha'}(N+\bar N-2)$, and $N=\bar N=0$ is its **top** point. (This is plumbing geometry — it appears inside PH18's statement but is not PH18's content, which is that $\mathcal C^{(L)}(P)$ has a pole *off* the lattice.) The coincidence with the $n=2$ exchange pole $\alpha's_c=4(n-1)$ and with the pair-production threshold concerns the *exchange* channels; the tabulated object is the **contact** term, which R48 (`Verified`) and C1 both show is entire in the momenta, so there is nothing to stand off from. **The offset ladder of the first version is withdrawn** (fix pass 2026-09-21); evaluate on the point. |
| On-shell four-tachyon | $\alpha'P^2=16/3$ | confirmed: the crossing-symmetric representative of the shell $\alpha'(s+t+u)=16$; R29's on-shell statement is at generic on-shell kinematics and $16/3$ is a representative of it, not a distinguished requirement |
| Deep off shell | $\alpha'P^2=-10$ | **kept** (decision of the fix pass, see below). Confirmed **given level matching** ($N=\bar N$), which makes the lattice $\alpha'P^2\in\{4,0,-4,-8,\dots\}$ and puts $-10$ at the maximal distance $2$ from it. It is a generic off-lattice point; if PH18 holds, the distinguished $P^2$ is an off-lattice zero of $\det V_4^{(L)}$, and **none** of the three points is selected for that — $-10$ is merely the one furthest from the lattice. |

**Decision (fix pass, 2026-09-21): $\alpha'P^2=-10$ is kept.** The review asked whether a
timelike delivery point is legitimate at all, on the reading that A6's Euclidean prescription
forces $s=P^2\ge0$. Block 4 settles this: the prescription constrains the *integration*
variables $\ell,\ell'$, and $P$ cancels identically from both $t$ and $u$, so $P^2$ is an
unconstrained external parameter and $-10$ sits inside the prescription, not outside it. What
carries the point is the level-matched-lattice distance together with the comparator's existing
$P^2$ reach; what it is **not** is a point selected by PH18. Nothing in Blocks 5–7 changes at
$\alpha'P^2=-10$ as a result (re-run: Block 5 table, $-10$ column).

## Claim tree

**Assumptions.** A1–A5 above, plus

- **A6** *(sharpened in the fix pass of 2026-09-21; the earlier wording said "momenta taken
  Euclidean", which is ambiguous and was read by the review as a statement about the individual
  $k_a$.)* The relative-momentum content to be discretised is PH3's integral over the pair's
  **relative** momenta at fixed total momentum $P$. Write
  $$k_1=\tfrac P2+\ell,\quad k_2=\tfrac P2-\ell,\quad
   k_3=-\bigl(\tfrac P2+\ell'\bigr),\quad k_4=-\bigl(\tfrac P2-\ell'\bigr),$$
  which is record 044's assignment $k_1=k$, $k_2=P-k$, $k_3=-k'$, $k_4=-(P-k')$ with
  $\ell=k-\tfrac P2$, $\ell'=k'-\tfrac P2$. The **integration variables are $\ell,\ell'$**, and it
  is those that are Wick-rotated: $\ell=(\I\ell^0_E,\vec\ell\,)$ with $\ell_E\in\R^{26}$
  Euclidean, likewise $\ell'$, so $\ell^2=\lvert\ell_E\rvert^2\ge0$. $D=26$. The total momentum
  $P$ is **not** an integration variable and is not rotated: $P^2=s$ is an external parameter,
  free to be positive (spacelike) or negative (timelike). The kernel is a function of $(t,u)$ at
  fixed $s=P^2$ (record 044, *Interpretation*, items 1–3), so the box is two-dimensional.
- **A7** $\beta\in\{3/2,2\}$, both $>\beta_{04}=\tfrac12+\tfrac1{\sqrt2}$, so
  $\mathrm{FD}\cap\mathcal V_{0,4}=\mathrm{FD}\cap\{\text{closed ellipse}\}$ exactly (R7 caveat,
  `in_FD_cap_V04` docstring).

**Hypotheses.**

- **H1** *(statement)* The leading spectral data of $K_P$ at fixed $P$ — the largest few
  eigenvalues, and $\det V_4^{(L)}(P^2)$ through them — move by $O(\eta)$ relatively when the
  relative-momentum integration is truncated to a region that carries all but a fraction $\eta$
  of the kernel's **row mass** $\int\dd^{26}\ell'\,\lvert K_P(\ell;\ell')\rvert$ at fixed $\ell$,
  reduced by C4.2 to the one-dimensional weighted mass of eq. (5.1).
  *(motivation)* For a self-adjoint kernel $\lvert\delta\lambda\rvert\le\lVert\delta K\rVert$,
  and for a kernel of one sign the Schur test bounds the operator norm by the row mass,
  $\lVert\delta K\rVert\le\bigl(\sup_\ell\!\int\lvert\delta K\rvert\dd\ell'\bigr)^{1/2}
  \bigl(\sup_{\ell'}\!\int\lvert\delta K\rvert\dd\ell\bigr)^{1/2}$, the two factors being equal
  here by the $t\leftrightarrow u$ symmetry of 044. On the truncated region the contact term does
  not change sign (C3.3 gives a positive bound, and the tile sum is a sum of positive integrands
  there), so no cancellation can make a small discarded mass correspond to a large discarded
  operator; and the decay is exponential (C3.4), so the tail is not a slowly converging one.
  **Where the hypothesis actually bites** is the step from a *relative* row-mass fraction $\eta$
  to a *relative* eigenvalue shift: the Schur bound is on the supremum over $\ell$, and rows with
  $\lvert\ell\rvert^2$ near $T_{\max}$ are discarded wholesale by the truncation, so the
  inequality is not by itself a proof of the $O(\eta)$ statement.
  *(falsifier/discharge)* a leading eigenvalue of the discretised $K_P$ that keeps drifting as
  $T_{\max}$ is pushed past the box of C5 — the first eigenvalue computation on the delivered
  grid discharges or falsifies it.

**Claims.**

- **C1** On $\mathrm{FD}\cap\mathcal V_{0,4}$, writing $L=\ln\lvert Z\rvert$,
  $M=\ln\lvert1-Z\rvert$ and $a=\beta^2+1/(16\beta^2)$: the region is compact and bounded away
  from $Z=0,1,\infty$, and $0\le L\le\ln a$, $L\le M\le L+\ln2$. [by C1.1–C1.3]
  - **C1.1** $\operatorname{Re}Z\le\tfrac12\Rightarrow\lvert1-Z\rvert\ge\lvert Z\rvert$, and
    $\lvert Z\rvert\ge1$, so $M\ge L\ge0$. [eq. (3.1)]
  - **C1.2** $\max\lvert Z\rvert=a$ at $Z=\tfrac12+\I b$ (where also $\lvert1-Z\rvert=a$), and
    $\max\lvert1-Z\rvert=a+\tfrac12$ at $Z=\tfrac12-a$. Uses $a^2-b^2=\tfrac14$. [eq. (3.2)]
  - **C1.3** $M-L\le\ln2$, with equality only at $Z=-1$. [eq. (3.3)]
- **C2** $\operatorname{Vol}(\mathrm{FD}\cap\mathcal V_{0,4})
  =\tfrac\pi4ab-\tfrac\pi3-\tfrac{\sqrt3}8$ exactly, and $12\,\operatorname{Vol}\,\beta^8$
  reproduces the companion SL(2,C) computation's zero-momentum contact integral at $C=1$
  (value from the companion computation, not reproduced here). [eq. (3.4); by check: `C2-stage0`]
- **C3** *(growth law)* With $S=s+t+u$ and $(x,y,z)$ a permutation of $(s,t,u)$, the tile
  exponents are $p=\tfrac{\alpha'}4(x-y-z)$, $q=\tfrac{\alpha'}4(y-x-z)$, $p+q=-\tfrac{\alpha'z}2$,
  and the contact term obeys the two-sided exponential law of C3.2–C3.3. [by C3.1–C3.4]
  - **C3.1** $p+q=-\alpha'z/2$ identically; the locus $\operatorname{Re}Z=\tfrac12$
    ($M=L$) lies in the region, so $\Lambda(p,q):=\max_R(pL+qM)\ge\max(0,-\tfrac{\alpha'z}2\ln a)$.
    [by A3, C1; eq. (3.5)]
  - **C3.2** $pL+qM$ is harmonic on $R$, so $\Lambda$ is attained on $\partial R$; and
    $\max\bigl(0,\;q\ln2,\;(p+q)\ln a,\;p\ln(a-\tfrac12)+q\ln(a+\tfrac12)\bigr)\le\Lambda
    \le(p+q)_+\ln a+q_+\ln2$. [by C1; eq. (3.6); by check: `C3.2`]
  - **C3.3** Hence the closed upper bound
    $\lvert F\rvert\le2\operatorname{Vol}\beta^{\,8-\alpha'S/2}\sum_{\rm perm}
    e^{(p+q)_+\ln a+q_+\ln2}$, valid for every real $(s,t,u)$. [by C3.2; eq. (3.7);
    by check: `C3.3`]
  - **C3.4** At fixed $s$, along $t,u\to+\infty$,
    $\ln F=-\tfrac{\alpha'}2(t+u)\ln\beta+O(1)$ — pure exponential decay at rate $\ln\beta$ per
    unit $\tfrac{\alpha'}2(t+u)$, with no power-law enhancement from the moduli integral.
    [by C3.2; by check: `C3.4`]
  - **C3.5** In the opposite direction $t,u\to-\infty$ the contact term grows exponentially;
    the box is finite only because A6 puts the relative-momentum integration in the
    $t,u\ge0$ quadrant (C4.1). [by C3.2; by check: `C3.5`]
- **C4** *(accessible region and induced measure)* [by C4.1–C4.3]
  - **C4.1** *(the quadrant, at every $P^2$)* In the variables of A6,
    $t=(\ell+\ell')^2$ and $u=(\ell-\ell')^2$ **identically**: the total momentum $P$ cancels
    from both. With $\ell,\ell'$ Euclidean this gives $t,u\ge0$ for **every** value of $s=P^2$,
    timelike included, and the whole quadrant is reached. [eq. (4.1); by check: `C4-positivity`,
    `C4-quadrant-P2`]
  - **C4.2** *(exact radial reduction)* $t+u=2(\lvert\ell\rvert^2+\lvert\ell'\rvert^2)$ and
    $t-u=4\,\ell\cdot\ell'$ **identically**. Hence at fixed $\ell$, writing
    $T=\tfrac12(t+u)$ and $\lambda=\lvert\ell'\rvert$, the radial part of $\int\dd^{26}\ell'$
    reduces **without approximation** to
    $\lambda^{25}\dd\lambda=\tfrac12(T-\lvert\ell\rvert^2)^{12}\dd T$, i.e. to the weight
    $w(T)=T^{12}\bigl(1-\lvert\ell\rvert^2/T\bigr)^{12}\to T^{12}$ at large $T$. No
    narrow-band or diagonal-collapse assumption enters the weight. [eq. (4.4)–(4.5); by check:
    `C4-measure`]
  - **C4.3** *(what the band does and does not control)* At fixed $\ell$ the reached set is the
    segment $\lvert t-u\rvert\le4\lvert\ell\rvert\lambda$ at each $T$; when both arguments run
    (the kernel case) the union is the full triangle $0\le\lvert t-u\rvert\le t+u$. The band
    therefore constrains only the *angular average of $F$*, never the weight. [eq. (4.2)–(4.3);
    by check: `C4-band`]
- **C5** *(the box)* Under H1, with the proxy $\mu(T_{\max})$ of eq. (5.1) — the **row mass**
  $\int\dd^{26}\ell'\,\lvert K_P\rvert$ at fixed $\ell$, reduced by C4.2 to the
  one-dimensional $T$-integral of $w(T)\lvert F(s,T,T)\rvert$ with $w=T^{12}$ and $F$ evaluated
  on the diagonal — the tolerance $\eta\le10^{-3}$ is met by $\alpha'T_{\max}$ of the Block 5
  table; the bare-measure ($w\equiv1$) box is smaller by a measured factor $3.9$–$5.5$, and the
  difference is the $\lambda^{25}$ phase space, not the vertex. [by H1, C3.4, C4; by check:
  `C5-closedform`, `C5-measure`, `C5-transverse`]
- **C6** *(sister range)* The sister comparator's exercised range induces, at each of the three
  delivery $P^2$, a $(t,u)$ region strictly inside the C5 box; the shortfall is quantified per
  $P^2$ in the table of Block 6. [by C5; eq. (6.1)]
- **C7** *(sampling)* A **tensor Chebyshev** grid of the first kind in $(t,u)$ on
  $[0,2T_{\max}]^2$ with barycentric interpolation of $\ln F$, halved by the
  $t\leftrightarrow u$ symmetry; $n=24$, node counts of Block 7. [by C3.4, C4; by check: `C7`,
  `BREAK-C7`]

Open gaps (see also *Status*):

- **GAP-2** *(the box itself)* The box of Blocks 5–7 is derived from a diagonal proxy and
  (3.9$'$) refutes the shape it assumes. The corrected two-dimensional computation is
  preliminary (Block 5, *The two-dimensional recomputation*) and is not in the check script.
  Blocking for the hand-off.
- **GAP-1** *(angular average)* The row proxy of C5 evaluates $F$ at $t=u=T$ instead of
  averaging it over the angular spread of $\ell\cdot\ell'$ at fixed $T$. The **direction** of
  the resulting error is established (Block 5, *The transverse omission*): since $F$ is
  *minimal* on the diagonal at fixed $T$ and **grows** transversally at the rate
  $\tfrac{\alpha'}4\ln2$ (3.9$'$) over a spread that itself grows like $T$, the diagonal value
  under-states the density increasingly with $T$,
  so the true tail is **longer** and the diagonal box is too small. Measured in check
  `C5-transverse`: the ratio $\langle F\rangle_\theta/F(s,T,T)$ runs $1.10$, $1.30$, $3.37$ at
  $\alpha'T=10,20,40$ and reaches $1.05\times10^3$ at $\alpha'T=80$. Closing it means doing the
  angular integral of $F$ — the two-dimensional quadrature of GAP-2.

Hypotheses in force: H1 (C5, C6, C7). Inherited conditionality: everything built on (3.0) —
which is the collapsed form of ledger row **R48**, itself `Conditional(A4, A5 — imported)` —
carries those imported conditions; see *Scope*. PH18 and PH3 are cited for the $P^2$ values and
for the existence of the relative-momentum sum, not for any step of Blocks 3–6.

## Block 3 — The region, the exact area, and the growth law

\subsection*{Setup}

Assumptions A1–A3, A7; claims C1, C2, C3. Write $R=\mathrm{FD}\cap\mathcal V_{0,4}$,
$Z=x+\I y$, $L=\ln\lvert Z\rvert$, $M=\ln\lvert1-Z\rvert$, and
$a=\beta^2+\tfrac1{16\beta^2}$, $b=\beta^2-\tfrac1{16\beta^2}$, so that $a^2-b^2=\tfrac14$.
The object studied is the reduced tile sum of record 044 eq. (2.4) with $C$ and the factor 2
stripped where convenient:
$$F(s,t,u)=2\beta^{\,8-\alpha'S/2}\sum_{(x,y,z)}J\Bigl(\tfrac{\alpha'}4(x-y-z),\,
 \tfrac{\alpha'}4(y-x-z)\Bigr),\qquad
 J(p,q)=\int_R\lvert Z\rvert^{p}\lvert1-Z\rvert^{q}\,\dd^2Z,\tag{3.0}$$
$S=s+t+u$, the sum running over the six ordered permutations $(x,y,z)$ of $(s,t,u)$.

\subsection*{Derivation}

*Geometry of $R$.* By A7 the region is $\{\operatorname{Im}Z\ge0,\ \lvert Z\rvert\ge1,\
\operatorname{Re}Z\le\tfrac12\}$ intersected with the closed ellipse centred at $\tfrac12$ with
semi-axes $(a,b)$. Its boundary consists of four arcs: the unit circle from $\e^{\I\pi/3}$ to
$-1$; the real segment $[\tfrac12-a,-1]$; the ellipse quarter from $\tfrac12-a$ to
$\tfrac12+\I b$; and the vertical segment $\operatorname{Re}Z=\tfrac12$ from $\tfrac12+\I b$ down
to $\e^{\I\pi/3}$. (The line $\operatorname{Re}Z=\tfrac12$ passes through the ellipse centre, so
it meets the ellipse exactly at $\tfrac12\pm\I b$; and $\tfrac12-a<-1$ for $\beta\ge\tfrac32$.)

For $\operatorname{Re}Z=x\le\tfrac12$,
$$\lvert1-Z\rvert^2-\lvert Z\rvert^2=1-2x\ \ge\ 0
\qquad\Longrightarrow\qquad M\ge L\ \ge\ 0,\tag{3.1}$$
the second inequality being $\lvert Z\rvert\ge1$. On the ellipse, parametrised by
$Z=\tfrac12+a\cos\theta+\I\,b\sin\theta$ with $c=\cos\theta\in[-1,0]$ (the part with
$x\le\tfrac12$, $y\ge0$), $a^2-b^2=\tfrac14$ gives
$$\lvert Z\rvert^2=\tfrac{c^2}4+ac+\tfrac14+b^2,\qquad
 \lvert1-Z\rvert^2=\tfrac{c^2}4-ac+\tfrac14+b^2,\tag{3.2}$$
with derivatives $\tfrac c2+a>0$ and $\tfrac c2-a<0$ on $c\in[-1,0]$. So $\lvert Z\rvert$ is
maximal at $c=0$, i.e. $Z=\tfrac12+\I b$, where $\lvert Z\rvert^2=\tfrac14+b^2=a^2$ and
$\lvert1-Z\rvert=\lvert Z\rvert=a$; and $\lvert1-Z\rvert$ is maximal at $c=-1$, i.e.
$Z=\tfrac12-a$, where $\lvert1-Z\rvert=a+\tfrac12$. Since $L$ and $M$ are subharmonic, their
maxima over $R$ are on $\partial R$, and the remaining arcs give smaller values, so
$$\max_R\lvert Z\rvert=a\ \ (\text{at }Z=\tfrac12+\I b),\qquad
 \max_R\lvert1-Z\rvert=a+\tfrac12\ \ (\text{at }Z=\tfrac12-a).$$
Finally, with $r=\lvert Z\rvert$,
$$M-L=\tfrac12\ln\Bigl(1+\frac{1-2x}{r^2}\Bigr),\qquad
 \max_R\frac{1-2x}{r^2}=3\ \text{ at }Z=-1,\tag{3.3}$$
because on $r=1$ the ratio is $1-2x\le3$, and along the negative real axis $r>1$ it is
$(1+2r)/r^2$, strictly decreasing. Hence $0\le M-L\le\ln2$. This proves **C1**: $R$ is compact,
$1\le\lvert Z\rvert\le a$ and $1\le\lvert1-Z\rvert\le a+\tfrac12$, so $R$ is bounded away from
$Z=0,1,\infty$ and every $J(p,q)$ is an entire function of $(p,q)$ of exponential type.

*The area, and the Stage 0 calibration.* At $p=q=0$ the integrand is $1$, so $J(0,0)$ is the
area. The quarter-ellipse $\{x\le\tfrac12,\ y\ge0\}$ has area $\tfrac\pi4ab$, and the excised
piece $\{\lvert Z\rvert<1,\ y\ge0,\ x\le\tfrac12\}$ has area
$\tfrac\pi2-\int_{1/2}^1\sqrt{1-x^2}\,\dd x=\tfrac\pi2-\bigl(\tfrac\pi6-\tfrac{\sqrt3}8\bigr)
=\tfrac\pi3+\tfrac{\sqrt3}8$, so
$$\boxed{\ \operatorname{Vol}(R)=\frac\pi4\,ab-\frac\pi3-\frac{\sqrt3}8\ }\tag{3.4}$$
and, by the $k=0$ collapse of the tile sum (R7/R10, sister §4),
$\{T^4\}_{\rm contact}(0)/C=12\operatorname{Vol}(R)\beta^8$; the numerical values at
$\beta=\tfrac32$ and $\beta=2$ agree with the companion SL(2,C) computation (values from the
companion computation, not reproduced here) (**C2**).

*The exponents.* With $x+y+z=S$,
$$p=\frac{\alpha'}4(x-y-z)=\frac{\alpha'}2\Bigl(x-\frac S2\Bigr),\quad
 q=\frac{\alpha'}4(y-x-z)=\frac{\alpha'}2\Bigl(y-\frac S2\Bigr),\quad
 p+q=-\frac{\alpha'z}2.\tag{3.5}$$

*The rate function.* $pL+qM$ is harmonic on $R$ (neither $0$ nor $1$ belongs to $R$), so
$\Lambda(p,q):=\max_R(pL+qM)$ is attained on $\partial R$, and by C1 the image
$D=\{(L,M):Z\in R\}$ lies in the trapezoid $\{0\le L\le\ln a,\ L\le M\le L+\ln2\}$ and contains
its four corners $(0,0)$ (at $\e^{\I\pi/3}$), $(0,\ln2)$ (at $-1$), $(\ln a,\ln a)$
(at $\tfrac12+\I b$) and $(\ln(a-\tfrac12),\ln(a+\tfrac12))$ (at $\tfrac12-a$). Therefore
$$\max\Bigl(0,\ q\ln2,\ (p{+}q)\ln a,\
 p\ln\bigl(a-\tfrac12\bigr)+q\ln\bigl(a+\tfrac12\bigr)\Bigr)
 \ \le\ \Lambda(p,q)\ \le\ (p{+}q)_+\ln a+q_+\ln2,\tag{3.6}$$
$(\cdot)_+$ the positive part (**C3.2**). Two consequences used below. First, since $M=L$ on the
whole segment $\operatorname{Re}Z=\tfrac12$ (a subset of $R$ of positive length) and
$p+q=-\alpha'z/2$ is *independent of how large $p$ and $q$ separately are*,
$$\Lambda(p,q)\ \ge\ \max\Bigl(0,\ -\tfrac{\alpha'z}2\ln a\Bigr)\tag{3.5'}$$
uniformly in the transverse direction (**C3.1**). Second, $J\le\operatorname{Vol}(R)e^{\Lambda}$
gives the closed bound
$$\lvert F(s,t,u)\rvert\ \le\ 2\operatorname{Vol}(R)\,\beta^{\,8-\alpha'S/2}
 \sum_{(x,y,z)}a^{(-\alpha'z/2)_+}\,2^{\bigl(\frac{\alpha'}4(y-x-z)\bigr)_+},\tag{3.7}$$
valid for **every** real $(s,t,u)$ (**C3.3**).

*The growth law in the physical direction.* Take $s$ fixed and $t,u\to+\infty$ (A6). All six
$p+q$ equal $-\alpha'z/2$ with $z\in\{s,t,u\}$: the two tiles with $z=s$ keep $p,q$ bounded
whenever $\lvert t-u\rvert$ stays bounded, while the four tiles with $z\in\{t,u\}$ have
$p+q\to-\infty$ and are exponentially suppressed relative to them. The prefactor
$\beta^{8-\alpha'S/2}$ carries the whole $t+u$ dependence, so
$$\boxed{\ F(s,t,u)\ \sim\ 2\,\beta^{\,8-\alpha'
 s/2}\,\Bigl[J(p_s,q_s)+J(q_s,p_s)\Bigr]\,
 \beta^{-\alpha'(t+u)/2},\quad
 p_s=\tfrac{\alpha'}4(t-u-s),\ \ q_s=\tfrac{\alpha'}4(u-t-s)\ }\tag{3.8}$$
(**C3.4**): *pure exponential decay in $t+u$ at rate $\ln\beta$ per unit $\tfrac{\alpha'}2(t+u)$,
with no power-law enhancement.* Numerically, along $t=u=T$ at $\alpha'=1$, the combination
$\ln F+T\ln\beta$ settles to a constant:

| $\beta$ | $s$ | $T=8$ | $T=16$ | $T=24$ | $T=32$ | $T=40$ |
| --- | --- | --- | --- | --- | --- | --- |
| $3/2$ | $4$ | 4.33162 | 3.97791 | 3.87706 | 3.83397 | 3.81033 |
| $3/2$ | $16/3$ | 3.87224 | 3.43118 | 3.30583 | 3.25289 | 3.22400 |
| $3/2$ | $-10$ | 10.85646 | 10.83895 | 10.83295 | 10.83007 | 10.82840 |
| $2$ | $4$ | 6.57209 | 6.27818 | 6.22000 | 6.19687 | 6.18443 |
| $2$ | $16/3$ | 5.79323 | 5.36923 | 5.28331 | 5.24948 | 5.23137 |
| $2$ | $-10$ | 18.60771 | 18.60729 | 18.60718 | 18.60713 | 18.60710 |

The residual approach is $O(1/T)$, which is the $1/\lvert p\rvert$ decay of the four
subleading tiles, not a correction to the rate.

*The transverse direction.* At fixed $t+u$, moving along $t-u$ sends $p\to+\infty$,
$q\to-\infty$ at fixed $p+q$. By $(3.5')$ the rate function does not decrease, and the
integral localises on the segment $\operatorname{Re}Z=\tfrac12$ where $M-L=0$; the transverse
width is $O(1/\lvert q\rvert)$, so
$$J\ \sim\ \frac{\text{const}}{\lvert t-u\rvert}\qquad(\lvert t-u\rvert\to\infty
 \text{ at fixed }t+u):\tag{3.9}$$
**for that one tile the decay transverse to the diagonal is only a power law.**

> **Correction (fix pass, 2026-09-21) — this is the record's one substantive error, and it was
> not among the review's findings.** The first version extended (3.9) from a single $J$ to $F$
> and concluded "the box is cut by $t+u$". That extension is **false**. The tile checked in
> (3.9) and in `C3.6` is the $z=s$ tile with the *decaying* ordering, $q<0$. Its partner
> $J(q,p)$ — the one the first version lost by writing $4J(p,q)$ instead of
> $2[J(p,q)+J(q,p)]$ in (3.8) — has $q>0$, and so does the tile with $z=\min(t,u)$ once that
> invariant is small. For those, $p+q\le0\le q$, and there the sandwich (3.6) is **tight**:
> the lower bound $q\ln2$ (corner $(0,\ln2)$, at $Z=-1$) and the upper bound
> $(p+q)_+\ln a+q_+\ln2=q\ln2$ coincide, so $\Lambda=q\ln2$ exactly. With
> $q=\tfrac{\alpha'}4(\lvert t-u\rvert-s)$ this gives
> $$\frac{\partial\ln F}{\partial\lvert t-u\rvert}\Big|_{t+u}\ \longrightarrow\
> \frac{\alpha'}4\ln2\ >\ 0\qquad(\textbf{C3.7}),\tag{3.9'}$$
> i.e. at fixed $t+u$ the contact term **grows** towards the edges $u\to0$ and $t\to0$ of the
> triangle. Measured (check `C3.7`, quadrature-converged at $n=30,80,160$): at
> $\alpha'(t+u)=80$, $\beta=2$, $\alpha'P^2=4$ the slope runs $0.1645\to0.1721$ against
> $\ln2/4=0.1733$; $F$ at the edge exceeds $F$ on the diagonal by $e^{9.9}\simeq2\times10^4$
> there, and by $e^{4.4}\simeq82$ at $\alpha'(t+u)=40$.
>
> **Consequence.** The decay function of the contact term on the quadrant is
> $$\Phi(t,u)=\frac{\alpha'}2(t+u)\ln\beta-\frac{\alpha'}4\lvert t-u\rvert\ln2,\tag{3.10}$$
> positive on the whole quadrant **iff $\beta>\sqrt2$** (both declared $\beta$ qualify, but
> $\beta=\tfrac32$ only just: the edge rate is $1/6.9$ of the diagonal rate). The level sets of
> $\Phi$ are quadrilaterals, not triangles; a box cut by $t+u$ is the wrong shape, and the box
> of the first version is **too small**, most severely at $\beta=\tfrac32$. Blocks 5–7 are
> superseded accordingly; see the notice at the head of Block 5.

What bounds the region transversally is therefore not the vertex but kinematics (Block 4:
$\lvert t-u\rvert\le t+u$) together with the measure, which vanishes like $u^{12}$ on the edge.

*The other direction.* For $t,u\to-\infty$ the prefactor becomes $\beta^{+\alpha'\lvert
t+u\rvert/2}$ and, by (3.6) with $q\to+\infty$, the tile sum grows exponentially as well: the
contact term is unbounded there (**C3.5**). A finite box exists only because A6 places the
relative-momentum integration in the quadrant $t,u\ge0$ — which, by C4.1, it does at **every**
$P^2$, the timelike values included.

\subsection*{Commentary}

- (3.1) is the only place $\operatorname{Re}Z\le\tfrac12$ is used, and it is what makes
  $M\ge L$ — the inequality that keeps $\Lambda$ bounded when $p\to+\infty$ at fixed $p+q$.
  Without it one could have $\lvert Z\rvert$ large and $\lvert1-Z\rvert$ small and the growth
  law would be governed by $\max(p,q)$ rather than by $p+q$.
- (3.2): the identity $a^2-b^2=\tfrac14$ is special to these semi-axes and is what makes the
  top of the ellipse equidistant from $0$ and $1$; it is the reason the corner
  $(\ln a,\ln a)$ sits on the diagonal of the $(L,M)$ plane.
- (3.4) is exact, not a quadrature: the $\beta$ dependence of the Stage 0 number is
  $\beta^8\bigl(\tfrac\pi4ab-\tfrac\pi3-\tfrac{\sqrt3}8\bigr)$ in closed form.
- (3.7) is an inequality, not an asymptotic: it holds at every real $(s,t,u)$, including the
  directions where the contact term grows, and is what is actually checked numerically.
- (3.8): the two surviving tiles are $(t,u,s)$ and $(u,t,s)$, giving $J(p_s,q_s)$ and
  $J(q_s,p_s)$. $R$ is not symmetric under $Z\leftrightarrow1-Z$, so these are distinct off the
  diagonal and the coefficient is $2[J(p_s,q_s)+J(q_s,p_s)]$, not $4J(p_s,q_s)$; the two agree on
  $t=u$, where the numerical table below is taken, so nothing downstream changes.
- (3.8)–(3.9): the asymmetry between the two directions is the whole content of the box. Along
  the diagonal the vertex supplies the cutoff; transverse to it it does not.

\subsection*{Result}

Eq. (3.4) (exact area, Stage 0 calibration), (3.6)–(3.7) (two-sided rate bound and the closed
upper bound on the contact term), (3.8) (exponential decay $\beta^{-\alpha'(t+u)/2}$ in the
physical direction) and (3.9) (power-law decay transverse to it).

\subsection*{Verification}

Checks `C1.1`, `C1.2`, `C1.3`, `C2-stage0`, `C2-quad`, `C3.2`, `C3.3`, `C3.4`, `C3.5`, `C3.6`
of `codes/verify-kp-box.py`.

## Block 4 — What the relative-momentum integration actually reaches

\subsection*{Setup}

Assumption A6; claim C4. External datum: $P$ with $P^2=s$ fixed and of either sign. Integration
variables: the Euclidean relative momenta $\ell,\ell'\in\R^{26}$ of A6. This block was
re-derived in the fix pass of 2026-09-21; the earlier version worked with $A=k$, $B=k-P$ and an
asymptotic collapse, both of which are superseded below.

\subsection*{Derivation}

*The invariants in relative-momentum variables.* With A6's assignment,
$$u=(k_1+k_3)^2=(k-k')^2=(\ell-\ell')^2,\qquad
 t=(k_1+k_4)^2=(k+k'-P)^2=(\ell+\ell')^2.\tag{4.1}$$
The total momentum **cancels identically** from both: $k-k'=\ell-\ell'$ and
$k+k'-P=(\tfrac P2+\ell)+(\tfrac P2+\ell')-P=\ell+\ell'$. Since $\ell,\ell'$ are Euclidean,
$t$ and $u$ are squared lengths of real Euclidean vectors and hence
$$t\ \ge\ 0,\qquad u\ \ge\ 0\qquad\text{for every }s=P^2\in\R\ \ (\textbf{C4.1}).$$
Conversely every point of the quadrant is reached: taking $\lvert\ell\rvert=\lvert\ell'\rvert=\rho$
gives $t+u=4\rho^2$ and $t-u=4\rho^2\cos\theta$, so $(t,u)$ sweeps the whole segment
$\lvert t-u\rvert\le t+u$ at each $t+u$. The reached region is exactly the closed quadrant.

*Why this is the right reading of A6, and what the alternative would give.* The Wick rotation is
a convergence device applied to the **variables that are integrated**. In PH3's partial sums at
fixed $P$ those are $\ell$ and $\ell'$; $P$ is an external label carried by the $\Sigma$ line
and is not integrated at this stage, so it is not rotated and $s=P^2$ may be timelike. Had one
instead rotated the individual momenta $k,k'$ and left $P$ Minkowskian — the alternative
reading, which the review took — then in the pair rest frame $P=(\sqrt{-s},\vec0\,)$ with
$k,k'$ spatial one would get
$$t=(k+k'-P)^2=\lvert\vec k+\vec k'\rvert^2+s\ \ge\ s,\qquad u=(k-k')^2\ge0,$$
i.e. $\alpha't\ge\min(0,\alpha's)$, which at $\alpha'P^2=-10$ opens a strip $-10\le\alpha't<0$
where C3.5 says the contact term *grows*. That reading is rejected, for three reasons. (i) It
rotates a variable that is not integrated, which is not what a Wick rotation is. (ii) It is not
the pair's relative momentum: $k$ and $P-k$ are the two strands, and $\ell=\tfrac12(k_1-k_2)$ is
their relative momentum by definition; rotating $k$ rather than $\ell$ makes the prescription
frame-dependent, since $\ell$ and $k$ differ by the fixed vector $P/2$. (iii) It breaks the
strand-exchange symmetry $\ell\to-\ell$ (i.e. $k\leftrightarrow P-k$) that the kernel manifestly
has, whereas (4.1) is manifestly symmetric. The two readings agree whenever $P$ is spacelike,
which is why nothing before $\alpha'P^2=-10$ distinguished them.

*Exact radial reduction (C4.2).* Squaring and adding (4.1),
$$t+u=2\bigl(\lvert\ell\rvert^2+\lvert\ell'\rvert^2\bigr),\qquad
 t-u=4\,\ell\cdot\ell'\ ,\tag{4.2}$$
both **exact**, not asymptotic. Write $T=\tfrac12(t+u)$, $\kappa=\lvert\ell\rvert^2$,
$\lambda=\lvert\ell'\rvert$, so that $T=\kappa+\lambda^2$ and $\dd T=2\lambda\,\dd\lambda$.
Then, at fixed $\ell$,
$$\lambda^{25}\,\dd\lambda=\tfrac12\lambda^{24}\,\dd T=\tfrac12(T-\kappa)^{12}\,\dd T,\tag{4.3}$$
so that
$$\int\dd^{26}\ell'\;g\bigl(T,\ell\cdot\ell'\bigr)
 =\frac{\Omega_{24}}2\int_\kappa^\infty(T-\kappa)^{12}\,\dd T
  \int_0^\pi\sin^{24}\theta\;g\bigl(T,\ \tfrac14\delta\bigr)\,\dd\theta,
 \qquad\delta=t-u=4\sqrt{\kappa\,(T-\kappa)}\cos\theta.\tag{4.4}$$
The radial weight is therefore
$$w(T)=(T-\kappa)^{12}\ \xrightarrow[\ T\gg\kappa\ ]{}\ T^{D/2-1}\big|_{D=26}=T^{12},\tag{4.5}$$
with $12=D/2-1$ at $D=26$. **This is the single most consequential number in this record**, and
it is now obtained without any collapse: the vertex decays like $\beta^{-\alpha'T}$ (3.8) while
the $26$-dimensional phase space supplies $T^{12}$, and the product peaks at
$T_*=12/(\alpha'\ln\beta)$ — $\alpha'T_*\simeq29.6$ at $\beta=\tfrac32$, $\simeq17.3$ at
$\beta=2$. **The mass of the kernel does not sit at small relative momentum.**

*What the band still does (C4.3).* The only thing left approximate is the inner angular integral
in (4.4): $F$ is evaluated on the diagonal $\delta=0$ rather than averaged over $\theta$. At
fixed $\ell$ the reached transverse extent is $\lvert t-u\rvert\le4\lvert\ell\rvert\lambda$ —
the "band" of the earlier version — while, when both arguments run as they do for a kernel, the
union over $\ell$ is the whole triangle $\lvert t-u\rvert\le t+u$. **Both statements are true and
neither is used for the weight**, which removes the contradiction the review found: the earlier
text derived the weight from the narrow band two lines after disowning the narrow band. The
region to tabulate is the triangle $t,u\ge0$, $t+u\le2T_{\max}$; the band is where the row mass
of a *fixed* $\ell$ sits inside it.

\subsection*{Commentary}

- (4.1)–(4.2) are identities, valid off shell, for complex momenta, and at any $P^2$. They are
  the reason the quadrant statement is $P^2$-independent, which the earlier version asserted only
  for spacelike $P$ and for the wrong reason (it attributed the quadrant to "Euclidean momenta"
  rather than to the cancellation of $P$).
- (4.3) is exact because $t+u$ is an exact quadratic in $\lambda$; the earlier $O(1/\sqrt T)$
  collapse error in the *weight* is gone. The residual $\kappa/T$ in (4.5) is not an error term
  but the exact weight of the row at $\lvert\ell\rvert^2=\kappa$; using $T^{12}$ is the
  large-$T$ form, and it under-weights small $T$, which shortens rather than lengthens the tail.
- With $P$ timelike and $\ell$ rotated, the individual $k_a^2$ acquire imaginary parts
  ($k_1^2=\tfrac{P^2}4+P\cdot\ell+\ell^2$ with $P\cdot\ell$ imaginary), but they enter only
  pairwise: $k_1^2+k_2^2=\tfrac{P^2}2+2\ell^2$ is real, and $s+t+u=\sum_ak_a^2=P^2+2\ell^2+2\ell'^2$
  is real. Since the contact term depends on the momenta only through $(s,t,u)$ (R48), the
  tabulated object stays real. This matters for Block 6: what the sister must cover is a range in
  $(s,t,u)$, and the per-virtuality figure quoted there is the translation of that range into
  their (real-kinematics) variables, not a claim that the four virtualities are separately real
  in the rotated integral.

\subsection*{Result}

Eq. (4.1): $t=(\ell+\ell')^2$, $u=(\ell-\ell')^2$, so $t,u\ge0$ at **every** $P^2$ and the
reached region is the full quadrant; the region to tabulate is the triangle $t+u\le2T_{\max}$.
Eq. (4.5): the weight against which the truncation error must be measured is $T^{12}$, peaking
at $\alpha'T_*=12/\ln\beta$, derived from the exact reduction (4.3).

\subsection*{Verification}

Checks `C4-positivity` (2000 seeded configurations, **timelike $P$ included**),
`C4-quadrant-P2` (the three delivery $P^2$ separately, with the alternative $k$-Euclidean
reading computed alongside), `C4-band`, `C4-measure` (Monte-Carlo of (4.3)–(4.5) in $D=26$
against the closed form) and the break legs `BREAK-C4-reading`, `BREAK-C4-measure` of
`codes/verify-kp-box.py`.

## Block 5 — The box

> **SUPERSEDED IN PART (fix pass, 2026-09-21).** The proxy repairs below (row mass, exact
> radial reduction, agreement of C5 with (5.1)) stand. **The box numbers do not**: they were
> obtained from a one-dimensional diagonal proxy, and (3.9$'$) shows the density grows towards
> the edges, so the diagonal proxy under-states the tail. The table is kept, labelled
> *superseded*, because Block 6's arithmetic repairs are demonstrated on it and because the
> factor between it and the corrected figures is the finding. The corrected, **preliminary**
> box is in *The two-dimensional recomputation* at the end of this block. **Nothing in this
> record is to be sent to the sister project until that recomputation is reviewed**.

\subsection*{Setup}

Hypothesis H1; claims C3.4, C4, C5. The **proxy quantity is the row mass** — the mass of one
row of the kernel, $\int\dd^{26}\ell'\lvert K_P(\ell;\ell')\rvert$ at fixed $\ell$ — reduced by
the exact radial reduction (4.3) to a **one-dimensional** integral in $T=\tfrac12(t+u)$:
$$\mu(T_{\max})=\int_0^{T_{\max}}w(T)\,F(s,T,T)\,\dd T,\qquad
 \eta(T_{\max})=1-\frac{\mu(T_{\max})}{\mu(\infty)},\tag{5.1}$$
with $w(T)=T^{12}$ (the physical measure, eq. (4.5)) or $w\equiv1$ (the bare $(t,u)$ measure).
*The one-dimensionality is not a restriction of the proxy to a slice.* The full angular measure
of $\dd^{26}\ell'$ is already inside $w$ by (4.4); what is one-dimensional is the integral that
remains after the angles are done, and the sole approximation is that $F$ is evaluated at
$\delta=t-u=0$ instead of being averaged over the angles. C5 and (5.1) now state the same
object; the first version of this record stated C5 as a two-dimensional box integral
$\int_{\rm box}w\lvert F\rvert$ while (5.1) and the script computed the diagonal reduction,
and that mismatch is repaired here (fix pass 2026-09-21).

*Why this proxy, at this stage.* No eigenvalue of $K_P$ is computed in this record, so the
tolerance cannot be put on one directly. The row mass is the natural stand-in because it is the
quantity the Schur test converts into an operator-norm bound for a kernel of one sign, and the
contact term has one sign on $t,u\ge0$. The step from "the discarded row-mass fraction is
$\eta$" to "the leading spectral data move by $O(\eta)$" is **H1**, and everything in this block
is conditional on it.

*The transverse omission, and which way it moves the box* (**GAP-1**). Replacing the angular
average $\langle F\rangle_\theta$ by $F(s,T,T)$ **under-states** the density, because by (3.9$'$)
the contact term is *smallest* on the diagonal at fixed $T$ and grows towards the edges, while
the angular spread of $\delta$ at fixed $T$ grows like $T$. The under-statement therefore grows
with $T$, so the true density decays **more slowly** than the proxy and the true $T_{\max}$ is
**larger** than the one tabulated: **the box of the first version is too small.** Measured, not
asserted: check `C5-transverse` evaluates $\langle F\rangle_\theta/F(s,T,T)$ with the exact
angular weight $\sin^{24}\theta$ at $\kappa=T/2$, and the ratio runs $1.103\to1.299\to3.372$ at
$\alpha'T=10,20,40$ ($\beta=2$), converged in quadrature order ($n=30,80,160$ agree to four
digits) and reaching $1.05\times10^3$ at $\alpha'T=80$. *(This paragraph replaces a claim, made
earlier in this same fix pass, that the omission was conservative. It is not; the check that was
written to confirm that claim refuted it, and the refutation is what led to (3.9$'$).)*

\subsection*{Result}

$\alpha'T_{\max}$ with $T=\tfrac12(t+u)$, from `codes/verify-kp-box.py` check `C5`
($\alpha'=1$). **Superseded; proxy values.** The four digits are the quadrature's, not the
box's. These are the *diagonal* row-proxy values; read them as $66$ and $39$ at $\eta=10^{-3}$,
and see the recomputation below for the figures that replace them.

| weight | $\beta$ | $\alpha'P^2=4$ | $16/3$ | $-10$ | tolerance $\eta$ |
| --- | --- | --- | --- | --- | --- |
| $T^{12}$ ($D=26$) | $3/2$ | 55.96 | 55.89 | 56.26 | $10^{-2}$ |
| $T^{12}$ | $3/2$ | **66.34** | **66.27** | **66.63** | $10^{-3}$ |
| $T^{12}$ | $3/2$ | 75.72 | 75.65 | 76.01 | $10^{-4}$ |
| $T^{12}$ | $2$ | 32.69 | 32.58 | 32.92 | $10^{-2}$ |
| $T^{12}$ | $2$ | **38.77** | **38.66** | **38.99** | $10^{-3}$ |
| $T^{12}$ | $2$ | 44.26 | 44.15 | 44.48 | $10^{-4}$ |
| $1$ (bare) | $3/2$ | 8.62 | 8.20 | 11.20 | $10^{-2}$ |
| $1$ (bare) | $3/2$ | 13.85 | 13.29 | 16.87 | $10^{-3}$ |
| $1$ (bare) | $2$ | 4.60 | 4.39 | 6.64 | $10^{-2}$ |
| $1$ (bare) | $2$ | 7.43 | 7.04 | 9.96 | $10^{-3}$ |

Three features. **(i)** The box is almost independent of $P^2$: across the three values it
moves by less than $1\%$ under the physical weight. One box per $\beta$ suffices. In particular
**nothing changes at $\alpha'P^2=-10$** — re-run in the fix pass after the Part 1 re-derivation,
since that is the point the review flagged: $66.63$ and $38.99$, unchanged.
**(ii)** The physical weight pushes the box out by a measured factor between $3.9$ and $5.5$
relative to the bare measure ($3.95$–$4.99$ at $\beta=\tfrac32$, $3.91$–$5.49$ at $\beta=2$,
across the three $P^2$; the often-quoted $4.8$ and $5.2$ are the $\alpha'P^2=4$ column alone) —
the $T^{12}$ phase space, not the vertex.
**(iii)** The numbers agree with the closed-form estimate: with $F\propto\beta^{-\alpha'T}$ the
tail of $T^{12}\beta^{-\alpha'T}$ is the incomplete Gamma function $Q(13,\alpha'T\ln\beta)$, and
$Q(13,26.9)=1.08\times10^{-3}$ at both $\beta$ — so $\alpha'T_{\max}\simeq26.9/\ln\beta$ at
$\eta=10^{-3}$, an analytic formula usable at any other tolerance:
$$\boxed{\ \alpha'T_{\max}(\eta)\simeq\frac{Q^{-1}(13,\eta)}{\ln\beta},\qquad
 \alpha't,\ \alpha'u\ \ge0,\qquad \alpha'(t+u)\le2\alpha'T_{\max}.\ }\tag{5.2}$$

**The box that the first version recommended** was $\alpha'(t+u)\le133$ ($\beta=3/2$) resp.
$78$ ($\beta=2$) at $\eta=10^{-3}$, with $112$ resp. $66$ at $\eta=10^{-2}$. **These are
withdrawn** by (3.9$'$).

\subsection*{The two-dimensional recomputation (preliminary)}

*The proxy that replaces the row proxy.* Once the transverse direction carries mass, a proxy
evaluated on a slice is not usable, and the row proxy has a second defect: it depends on the
fixed $\lvert\ell\rvert^2=\kappa$ of the row. The **Hilbert–Schmidt** mass has neither problem
and is an honest operator-norm bound, $\lVert\delta K\rVert\le\lVert\delta K\rVert_{\rm HS}$.
Its measure reduces **exactly**, with no collapse and no free parameter: with $a=\ell+\ell'$,
$b=\ell-\ell'$ one has $\dd^{26}\ell\,\dd^{26}\ell'=2^{-26}\dd^{26}a\,\dd^{26}b$ and
$t=\lvert a\rvert^2$, $u=\lvert b\rvert^2$, so
$$\lVert K\rVert_{\rm HS}^2=\frac{\Omega_{25}^2}{2^{28}}
 \int_0^\infty\!\!\int_0^\infty t^{12}u^{12}\,\lvert F(s,t,u)\rvert^2\,\dd t\,\dd u.\tag{5.3}$$
The weight $t^{12}u^{12}$ vanishes on the edges, which is the physical statement that
$\ell=\pm\ell'$ is a measure-zero coincidence; it is what keeps (5.3) finite against the edge
growth (3.9$'$), and it does so only for $\beta>\sqrt2$.

*Preliminary numbers.* Tabulating $\ln F$ on a $(T,v)$ grid, $t=T(1+v)$, $u=T(1-v)$, and
integrating (5.3) numerically (scratch computation of the fix pass; **not yet a check in
`codes/verify-kp-box.py`**), the triangle $\alpha'(t+u)\le2\alpha'T_{\max}$ that captures all
but $\eta$ of the HS mass is

| $\beta$ | $\eta=10^{-2}$ | $10^{-3}$ | $10^{-4}$ | first version, $\eta=10^{-3}$ |
| --- | --- | --- | --- | --- |
| $3/2$ | $158$–$166$ | $192$–$199$ | $222$–$229$ | $66$ |
| $2$ | $29$–$32$ | $33$–$37$ | $36$–$42$ | $39$ |

(ranges over the three $P^2$). At $\beta=2$ the box is essentially unchanged; at
$\beta=\tfrac32$ it is a factor $\simeq3$ larger, because the edge decay rate
$\tfrac{\alpha'}2\ln\beta-\tfrac{\alpha'}4\ln2$ is only $1/6.9$ of the diagonal rate there.
The same computation in the level sets of $\Phi$ (3.10) gives
$\Phi_{\max}\simeq100$ ($\beta=\tfrac32$) and $\simeq60$ ($\beta=2$) at $\eta=10^{-3}$, a
quadrilateral box that is cheaper than the triangle at equal tolerance.

**Why these are preliminary and not shipped.** Three things are unverified: the extrapolation of
$\ln F$ beyond the tabulated $v=0.98$ (done with the asymptotic edge rate of (3.9$'$)); the
quadrature order of `contact` at the tile exponents $\lvert p\rvert\simeq200$ that the
$\beta=\tfrac32$ grid reaches, where `C2-quad-deep` only certifies $\lvert p\rvert\le80$; and
whether HS or the row mass is the proxy H1 should be stated against, which changes the
$\beta=\tfrac32$ answer by a factor $\simeq2$ (the $T^{12}$-weighted two-dimensional mass gives
$386$ rather than $199$). None of these is hard; none is done here.

\subsection*{Verification}

Checks `C5-monotone`, `C5-measure`, `C5-analytic` and the break leg `BREAK-C5`
(the tail of the physical weight at $\beta=\tfrac32$ is large — which is the finding of
Block 6).

## Block 6 — Relation between the box and an external evaluator's range

\subsection*{Setup}

Claim C6. An external evaluator of the contact term is exercised over a finite range of
$\lvert\alpha'k_a^2\rvert$ and $\lvert\alpha'P^2\rvert$ at $\beta\in\{3/2,2\}$ (range from the
companion SL(2,C) computation, not reproduced here). Rewritten in the fix pass: the first
version evaluated both columns at a single corner, which is not a delivery point, and inverted
(6.1) with the wrong sign.

\subsection*{Derivation}

*What an evaluator reaches, per $P^2$.* By the off-shell Mandelstam identity
$\sum_ak_a^2=s+t+u$ (record 044, C1.2), a bound $\lvert\alpha'k_a^2\rvert\le K$ on the
individual virtualities gives
$$\alpha'(t+u)=\alpha'\Bigl(\sum_ak_a^2\Bigr)-\alpha'P^2\ \le\ 4K-\alpha'P^2,\tag{6.1}$$
**and the sign of the $\alpha'P^2$ term is negative**: the reach is largest at the most negative
$P^2$.

*Inverting for the required virtuality.* Solving (6.1) for the common virtuality at
$\alpha'(t+u)=2\alpha'T_{\max}$ and four equal $k_a^2$,
$$\alpha'k_a^2=\frac{2\alpha'T_{\max}+\alpha'P^2}{4},\tag{6.2}$$
**with a $+$ sign on $\alpha'P^2$**. What the evaluator must actually be stable at is the
invariant $\alpha'(s+t+u)=2\alpha'T_{\max}+\alpha'P^2$; (6.2) is only its translation into the
(real-kinematics) per-leg variable, and is quoted as such (Block 4, *Commentary*, third item).

Applied to the **superseded** diagonal box of Block 5 ($\alpha'T_{\max}=66.34$, $66.27$, $66.63$
at $\beta=\tfrac32$; $38.77$, $38.66$, $38.99$ at $\beta=2$), (6.2) gives the required common
virtuality at each delivery point. The first version's figures were overstatements produced by
the sign error, and its shortfalls were understatements produced by pairing the most favourable
"reachable" corner with the least favourable "needed" one. **These corrections are arithmetic
and are confirmed here; they are not the final answer**, because $T_{\max}$ itself is
superseded.

Applied to the **preliminary** two-dimensional box of Block 5 ($199.1$, $199.3$, $191.8$ at
$\beta=\tfrac32$; $36.7$, $37.2$, $32.9$ at $\beta=2$), (6.2) gives the binding virtuality at
each $\beta$. **The two $\beta$ separate completely**: at $\beta=2$ the demand is what the first
version said to within rounding, while at $\beta=\tfrac32$ it is three times larger than the
first version's already-blocking figure. That is the reason nothing is sent yet.

**Under the bare measure the answer reverses at $\beta=2$ but not at $\beta=\tfrac32$.** The
one-dimensional diagonal bare boxes of the Block 5 table are $\alpha'(t+u)\le27.7$, $26.6$,
$33.7$ ($\beta=\tfrac32$) and $14.9$, $14.1$, $19.9$ ($\beta=2$); at $\beta=2$ the statement
survives the two-dimensional recomputation, which gives $\alpha'(t+u)\le18.8$. At
$\beta=\tfrac32$ it does **not** survive: the two-dimensional bare box is
$\alpha'(t+u)\le56.8$. So the measure-dependence of the conclusion — the pivot the first
version identified correctly — is real at $\beta=2$ and only partial at $\beta=\tfrac32$, where
the edge growth (3.9$'$) is slow enough to matter on its own. The question of whether an
evaluator range must be extended is therefore the question of which measure the tolerance is
taken against — i.e. of **H1** and of the $26$-dimensional phase-space weight — at $\beta=2$; at
$\beta=\tfrac32$ it is also a question about the vertex.

\subsection*{Result}

Method and arithmetic: (6.1) and (6.2) with the sign of $\alpha'P^2$ positive in (6.2).
Conclusion, **provisional on the recomputed box**: an evaluator range of the size of the
companion computation's does not cover the box under the physical measure (comparison values
from the companion computation, not reproduced here); the comparison against the box computed
with the bare $(t,u)$ measure is the $\beta$-dependent statement made above.

## Block 7 — Sampling

\subsection*{Setup}

Claim C7. What is tabulated is $\ln F$, not $F$: $F>0$ throughout the box (a positive prefactor
times a sum of positive integrals), so $\ln F$ is real-analytic there, and by (3.8) it is close
to the *linear* function $-\tfrac{\alpha'}2(t+u)\ln\beta$ plus a slowly varying remainder.

\subsection*{Derivation and result}

A tensor Chebyshev grid in $(t,u)$ on $[0,2T_{\max}]^2$, with barycentric interpolation of
$\ln F$, converges spectrally. Measured over the triangle at $\beta=2$, $\alpha'P^2=4$,
$2\alpha'T_{\max}=77.5$ (check `C7`):

| nodes per axis | max $\lvert\Delta\ln F\rvert$ on the triangle |
| --- | --- |
| 8 | $4.1\times10^{-2}$ |
| 12 | $9.0\times10^{-3}$ |
| 16 | $3.9\times10^{-4}$ |
| 20 | $1.9\times10^{-4}$ |
| 24 | $2.7\times10^{-5}$ |

**Recommendation.** $n=24$ Chebyshev nodes of the first kind per axis — **not $n=20$**: the
first version recommended $20$ with "an expected interpolation error below $10^{-4}$", and the
measurement (check `C7`, now run at $n=8,12,16,20,24$) gives $1.9\times10^{-4}$ at $n=20$ and
$2.7\times10^{-5}$ at $n=24$. Explicitly,
$t_j=\tfrac12\cdot2T_{\max}\bigl(1+\cos\tfrac{(2j+1)\pi}{2n}\bigr)$, and the
same in $u$, $j=0,\dots,n-1$. The scheme that is measured, and therefore the scheme that is shipped, is the
**full $n\times n$ tensor grid**: tensor barycentric interpolation is not defined on a
triangular subset of the nodes, so the first version's instruction to keep only the
$\simeq110$ nodes with $t+u\le T_{\rm box}$ was not the scheme whose error was measured, and
the body's $400$ and the hand-off's $110$ were two different recommendations. The only
admissible reduction is the exact $t\leftrightarrow u$ symmetry, which halves the *evaluations*
while leaving the tensor grid complete: $n(n+1)/2=210$ evaluations per $(P^2,\beta)$, i.e.
$n(n+1)/2=300$ evaluations per $(P^2,\beta)$, i.e. $1800$ in total for three $P^2$ and two
$\beta$, the remaining $276$ values being filled in by $F(s,t,u)=F(s,u,t)$. Two caveats carried
forward: the error is measured on the *superseded* box of Block 5, and the corrected box is
larger, so the node count must be re-measured on it; and it is measured for a function whose
transverse variation is now known to be exponential (3.9$'$), which is precisely the direction
in which a larger box will demand more nodes. Uniform or
geometric spacing is not recommended: the function is entire and the Chebyshev clustering is
what buys the spectral rate; geometric spacing wastes nodes near $t=0$, where nothing happens.

Two refinements, both optional and both cheap:

1. Tabulate the **reduced** quantity $\widetilde F=\ln F+\tfrac{\alpha'}2(t+u)\ln\beta$ rather
   than $\ln F$. By (3.8) this removes the exact linear trend and leaves a function that varies
   by $O(1)$ *along the diagonal* (Block 3's table: from $4.33$ to $3.81$ over
   $\alpha'T=8\to40$); transverse to it the residual still carries the
   $\exp(\tfrac{\alpha'}4\lvert t-u\rvert\ln2)$ of (3.9$'$), so the saving is in $t+u$ only and
   the "$n=12$ then suffices" of the first version does not survive. The trend is restored analytically.
2. The $t\leftrightarrow u$ halving above is not optional bookkeeping but part of the
   recommendation; the symmetry of any independently evaluated node is a free correctness check
   on the sister's routine.

## Scope

- **Class covered.** Tachyon-pair block only, (companion value, not reproduced here), matter
  sector, contact term only (no $s/t/u$ Feynman-region exchange). Real $(s,t,u)$; Euclidean
  relative momentum at fixed $P^2$ (A6). $D=26$.
- **What is unconditional *in H1*, and what it is nonetheless conditional on.** Blocks 3 and 4
  use no hypothesis of this record: the region geometry (C1), the exact area and the Stage 0
  calibration (C2), the two-sided rate bound and the closed bound (3.6)–(3.7), the exponential
  decay $\beta^{-\alpha'(t+u)/2}$ along the diagonal (3.8), the transverse **growth** law
  (3.9$'$)/(3.10), the positivity $t,u\ge0$ at every $P^2$ (C4.1) and the exact radial reduction
  (4.3). **They are not unconditional simpliciter.** Everything built on (3.0) is built on the
  collapsed form of ledger row **R48**, whose status is `Conditional(A4, A5 — imported)` (sister
  `SL: R51` for the mapping radii, `SL: R6`/`SL: R10` for the tile assembly). The correct
  statement throughout — including where the Stage 0 closed form is offered as an absolute
  calibration — is *unconditional in H1, conditional on the rows imported behind the 044
  reduction*. The first version called these blocks "unconditional"; that was an overclaim.
- **What is conditional.** The box itself (C5), the comparison with the sister range (C6) and
  the node count (C7) are conditional on **H1** — that the leading spectral data of $K_P$ follow
  the kernel's mass against the relative-momentum measure. H1 is discharged or falsified by the
  first eigenvalue computation on the delivered grid: if the leading eigenvalue keeps drifting
  as $T_{\max}$ is pushed past the box, H1 fails and the box must be re-derived against the
  eigenvalue itself.
- **What is approximate, and by how much.** The radial reduction (4.3) is now exact, so the
  earlier $O(1/\sqrt T)$ collapse error is gone. What remains approximate is (i) the
  **diagonal-only evaluation of $F$** in the superseded row proxy — not a few percent but a
  factor $10^3$ in the density at $\alpha'T=80$ (GAP-1, (3.9$'$)), which is why that proxy is
  withdrawn; (ii) in the replacement two-dimensional computation, the extrapolation of $\ln F$
  beyond $v=0.98$ and the quadrature order at $\lvert p\rvert\gtrsim200$, neither yet certified;
  (iii) the choice of HS versus $T^{12}$-weighted mass as the proxy, worth a factor $\simeq2$ at
  $\beta=\tfrac32$. The *tolerance* $\eta$ is the stated quantity; the box boundary is currently
  good to tens of percent, not to a few.
- **What is not an exclusion.** Nothing here says a smaller box cannot work, and (3.10) in
  particular says a *differently shaped* box of the same tolerance is cheaper than the triangle.
  What is established is that a box chosen against the bare $(t,u)$ measure is several times too
  small once the $D=26$ phase space is included, and that the two answers differ by the phase
  space alone — not by the vertex.
- **Not checked.** Ghost sector; level-$(1,1)$ and higher states in the pair (the box is derived
  for the tachyon-pair block, and higher levels shift the virtualities by $+4(N-1)/\alpha'$ per
  strand, which moves $t+u$ but not the decay rate); complex $(s,t,u)$; $\beta$ outside
  $\{3/2,2\}$ — though (5.2) is explicit in $\beta$ and can be evaluated anywhere above
  $\beta_{04}$.

[Correspondence with the companion project removed.]

## Verification summary

`codes/verify-kp-box.py`, run under `.venv/bin/python`, seed `20260921` printed, $\alpha'=1$.
**49 named checks, 49 PASS, 0 FAIL, exit 0.** Of these, **7 are break-on-purpose legs**
(`BREAK-C1.1`, `BREAK-C2-stage0`, `BREAK-C3.2`, `BREAK-C3.4`, `BREAK-C3.7`, `BREAK-C4-reading`,
`BREAK-C4-measure`, `BREAK-C5-closedform`, `BREAK-C7` — each perturbs a tested quantity and is
confirmed to fire) and **2 are bookkeeping controls, not break legs** (`BREAK-C3.3`, which
restates C3.3's own non-vacuity clause on the same numbers, and `CONTROL-C5-reach`, which
evaluates the Block 6 finding rather than perturbing anything). The first version's docstring
and summary called all six of its legs break legs; three of them were controls, and the count
is corrected here in the terms R40's row uses for the distinction.

Quadrature: nested Gauss–Legendre with the ellipse square root removed by $y=b\sin\theta$ and
panels broken at $\lvert Z\rvert=1$; relative error $10^{-8}$–$10^{-9}$ at $n=80$ against the
exact area (3.4), and — new in this pass — refinement at the deep exponents the box computation
actually reaches, $(p,q)=(-40,-1)$ and $(-80,-1)$, where $n=40$ agrees with $n=160$ to
$10^{-5}$ and $n=80$ to $10^{-6}$ (`C2-quad-deep`). The Stage 0 comparison agrees with the
companion computation to within the rounding of its stored doubles (figures from the companion
computation, not reproduced here), so what the check establishes is that those doubles are the
correctly rounded values of (3.4).

New or rebuilt in this pass: `C4-positivity`/`C4-quadrant-P2` now sample **timelike $P$**
explicitly at $\alpha'P^2\in\{4,16/3,-10,-25,0,9\}$ (the first version drew $P$ from a real
Gaussian, so $s\ge0$ held in every one of its 2000 configurations and the region under test was
unreachable), with `BREAK-C4-reading` confirming that the rejected $k$-Euclidean prescription
*does* produce $\alpha't<0$ at $\alpha'P^2=-10$ and only there, so the check separates the two
readings rather than passing vacuously; `C4-measure` tests the exact radial reduction (4.3) by
Monte Carlo in $D=26$ against its closed form, with the exponent-11 perturbation firing;
`C5-closedform` replaces `C5-analytic`, comparing the numerical $T_{\max}$ against
$Q^{-1}(13,\eta)/\ln\beta$ in a $\pm3\%$ window (the old check accepted a factor-$10$ window in
$\eta$, i.e. $\pm8$ in $T_{\max}$, for a number quoted to four digits), with the weight-11
perturbation firing; `C3.7` measures the transverse rate $\partial\ln F/\partial\lvert t-u\rvert
\to\ln2/4$ that refutes the first version's box shape; `C5-transverse` measures the angular
average against the diagonal value; `C7` now runs to $n=24$, tests the **full tensor grid** that
the hand-off ships, and carries a firing break leg (wrong barycentric weights).

Unchanged and still holding: the rate-function sandwich (3.6) at $800$ random $(p,q)$ to machine
precision; the closed bound (3.7) dominating $F$ at $60$ random real $(s,t,u)$ while staying
within a factor $1.6$ of it; the decay rate of (3.8) confirmed to $\alpha'T=40$ with a drift
falling like $1/T$ while a deliberately wrong rate drifts by $5.5$ per step.

**Not covered by any check in the script**: the two-dimensional recomputation of Block 5. It is
a scratch computation of this pass, and its numbers are labelled preliminary throughout.

## Status

**Partial — repaired, but the deliverable is withdrawn pending one more computation.**

Done in this pass: A6 sharpened and the reached region re-derived (Block 4, C4.1–C4.3), which
dissolves the review's critical finding and makes the quadrant statement $P^2$-independent;
$\alpha'P^2=-10$ kept, with the reason stated; the proxy made to agree with its implementation
and given a Schur-test motivation; Block 6's sign and corner errors re-derived and corrected;
the offset ladder withdrawn; the node counts reconciled and re-measured; the imported
conditionality of R48 carried into the Scope and the hand-off; nine break legs and two controls,
49/49 checks passing.

Not done, and blocking the hand-off: the two-dimensional box. Check `C5-transverse`, written in
this pass to confirm that the diagonal proxy was conservative, **refuted** that expectation, and
following it up gave (3.9$'$) — at fixed $t+u$ the contact term *grows* towards the edges of the
triangle, at the exact rate $\tfrac{\alpha'}4\ln2$. The box is therefore the wrong shape and, at
$\beta=\tfrac32$, about three times too small. Preliminary corrected figures are in Block 5;
they need (i) a certified quadrature order at $\lvert p\rvert\gtrsim200$, (ii) the $v\to1$ edge
handled without extrapolation, (iii) a decision between the Hilbert–Schmidt and $T^{12}$-weighted
proxies, and (iv) promotion of the computation into `codes/verify-kp-box.py` with its own break
leg.

Open gaps: GAP-1 (angular average — now *measured* and known to be the dominant effect, not a
refinement), GAP-2 (the two-dimensional box itself, above).
Hypotheses in force: H1 (C5, C6, C7). Inherited conditionality: R48, `Conditional(A4, A5 —
imported)`, behind everything built on (3.0).

The follow-up this record leaves is unchanged in kind but larger in stakes: record 044's note
that the six tile integrals may admit a hypergeometric/Appell representation would replace the
grid by a formula, and at $\beta=\tfrac32$ the grid is now expensive enough that the formula is
worth trying first.
