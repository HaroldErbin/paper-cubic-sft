# Record 092 – Certifying record 089's segment criterion (anchors tied to the package, step control, $\beta>2$, exact certification)

## Status

complete after fix pass on critic iteration 1 (2026-10-04 22:15; first completion 21:58): blocks (i)–(iv) done, all provisional with the external reference implementation (imported by path); `codes/verify-mu-segment-cert.py` 30/30 PASS (0.6 s, peak 86 MB); block (iv) by exact algebra instead of interval arithmetic (stated deviation); next: orchestrator's call on a narrow confirmation pass (nodes C0, C6) and promotion of the R86 text.

**Answer in one line.** In the Joukowski coordinate $x=q/(4\beta^2)$ the two anchors are rational, $B-A=(1+7x^2)/(6(1+x)^2)$, $g_1=4(1+x^2)/(1+7x^2)$, $g_0=-2(1+6x+x^2)/(1+7x^2)$, $g_{1/Z}(x)=g_0(-x)$, and the preimages of $[0,1]$ are explicit and lie off the closed FD except $g_0=0$ at $Z=-1$; so 089's segment criterion holds exactly on the whole FD, with no sampling, for every $\beta\ge\beta_{04}$ and every weight in $[0,1]$. R86's every-point clause can go from Numerical, $\beta\le2$ to Proven given the package's formulas, every $\beta\ge\beta_{04}$. Critic items #9 (anchors tied to the package's code at $2\times10^{-16}$), #8 (sampled windings certified at the polygon level) and #5 (runs at $\beta=3,4,10$) are closed as asked.

## Task and objective

- **Literal task.** Record 089 §3b (C2.6, C2.7): on $D={\rm FD}\cap\mathcal V_{0,4}$, $\mu_{1j}=S_0(1/R-t_j)$, $1/R=A+L(B-A)$, $L\in[0,1]$, so a zero needs $t_j\in[A,B]$, $t_j\in\{1,0,1/Z\}$; 089 excludes it by a numerical argument principle for $g_t=(t-A)/(B-A)$ on a sampled $\partial D$ (Numerical, $\beta\le2$). Do the critic's items in order: (i) #9 tie `A_seg`, `B_seg` to the package's `R_interior`/`weight_lambda1`, separate the weight-range assertion; (ii) #8 step control of the sampled windings; (iii) #5 $\beta>2$; (iv) #7 a rigorous certification between samples.
- **Motivating objective.** Decide whether R86's clause "every point of $Q_V$ given the sister's package (Numerical, $\beta\le2$)" can rise in tag and range, and state what remains when it cannot.

## Blocks and what failure of each would look like

1. **(i) Anchors tied to the package.** Failure: $|1/R_{\rm interior}-(A+L(B-A))|$ not at rounding level somewhere on $D$ or its walls (the re-typed anchors are not the package's), or the package's $L$ leaves $[0,1]$.
2. **(ii) Step control.** Failure: on some boundary curve a sample step $|g(Z_{k+1})-g(Z_k)|$ exceeds half the distance to the forbidden set ($[0,1]$ for $g_t$, $0$ for $B-A$), so the sampled winding is not the polygon's true winding; break leg: a deliberately coarse sampling must fail the assertion.
3. **(iii) $\beta>2$.** Failure: a run at $\beta=3$ or $4$ gives nonzero winding or a near-touch, or the tail $|Z|\to\infty$ approaches $[0,1]$.
4. **(iv) Certification between samples.** Failure: an enclosure of $g_t$ on a boundary arc meets $[0,1]$ (or one of $B-A$ meets $0$), or (exact route) a preimage of $[0,1]$ lies in $D$.

## Conventions and assumptions

- **A1** Record 089's A1–A6 (book conventions; package frame $(\zeta_1,\dots,\zeta_4)=(0,1,\infty,Z)$; the package's default section), cited, not restated.
- **A2** Input (provisional): the external reference implementation of the companion project, imported by path, not edited; `codes/verify-mu-table.py` imported, not edited.
- **A3** $D(\beta)={\rm FD}\cap\{\Re\,{\rm arccosh}(2Z-1)\le\ln4\beta^2\}$ for $\beta\ge\beta_{04}=\tfrac12+\tfrac1{\sqrt2}$ (R7, package `in_FD_cap_V04`).

## Claim tree

- **A1–A3** as above.
- **C0 (root)** Given the external reference implementation (provisional): for every $\beta\ge\beta_{04}$ and every interpolation weight with values in $[0,1]$, $t_j\notin[A,B]$ on $D(\beta)$ except $t_3=0$ at $Z_0=-1$; so $\mu_{1j}\ne0$ on $D(\beta)$ except possibly $\mu_{13}$ at $Z_0=-1$ (zero iff $L(-1)=0$, true for the package's weight when $\beta>\beta_{04}$; at $\beta=\beta_{04}$ exactly, $d_3(-1)=d_4(-1)=0$, the corner is C3$\cap$C4 (a cusp of $D$), the package's weight is discontinuous there and returns $L=1$ through its `a + b <= 0` branch, so $\mu_{13}(-1)=S_0(-1)(1-1/\sqrt2)\ne0$; the non-vanishing claim is unaffected, it needs only $L\in[0,1]$), and $\mu_1=\mu_2\ne0$ at every point of $Q_V$. Exact: closed-form algebra in $x=q/(4\beta^2)$ (no sampling, no argument principle), identities sympy-exact, inequalities by hand; the code's anchors and weight tied to the formulas at rounding level. [by C1, C4, C5, C6; 089 C2.6 ((3.4))]
  - **C1** (block i) The package's code computes $1/R=A+L(B-A)$ with 089's $A$, $B$ (at rounding level, interior and walls), and its $L$ lies in $[0,1]$ on $D(\beta)$. [eq. (i.1) (range by hand); cited: package `R_interior`, `weight_lambda1`; by check: C1-tie, C1-anchors] [check: C1-weight-range, BREAK-C1-tie]
  - **C2** (block ii) 089's sampled windings ($\beta=\tfrac32,2$) are the windings of polygons that miss the forbidden sets: every step is below a fraction of the local distance given by (companion value, not reproduced here) (for $g_0$ off $|Z+1|<10^{-2}$). Not used by C0 (superseded by C4); it closes critic #8 for the sampled route. [eq. (ii.1); by check: C2-step] [check: BREAK-C2-coarse]
  - **C3** (block iii) The sampled route passes at $\beta=3,4,10$ (Numerical); the limiting region of $D(\beta)$ as $\beta\to\infty$ is the closed FD, compact in $x$ as the triangle $T$ with $Z=\infty$ at $x=0$; the range "every $\beta\ge\beta_{04}$" is C4's. [by check: C3-windings; by C4]
  - **C4** (block iv) On the whole closed FD: $B\ne A$, $g_1,g_{1/Z}\notin[0,1]$, $g_0\notin(0,1]$, $g_0=0$ only at $Z=-1$ ((iv.9)). [by C4.1–C4.3]
    - **C4.1** $x=e^{-{\rm arccosh}(2Z-1)}=q/(4\beta^2)$, $Z=(1+x)^2/(4x)$, $|x|<1$, $\Im Z\ge0\iff\Im x\le0$, real points as in (iv.2), no jump across C1. [eq. (iv.1)–(iv.2)] [check: C4.1-uniformization]
    - **C4.2** The rational forms (iv.3). [eq. (iv.3); by check: C4.2-rational-forms] [check: C4.2-package-tie, BREAK-C4.2-package-tie]
    - **C4.3** The preimages of $[0,1]$ under $g_1$, $g_0$, $g_{1/Z}$ and the zeros of $B-A$ lie outside the closed FD, except $g_0=0$ at $Z=-1$ ((iv.4)–(iv.8)). [by C4.1, C4.2; eq. (iv.4)–(iv.8); by check: C4.3-preimages] [check: C4.3-scan, BREAK-C4.3-planted]
  - **C5** $\mu_{1j}=S_0(B-A)(L-g_{t_j})$ on $D(\beta)$, hence $|\mu_{1j}|\ge|S_0||B-A|\,{\rm dist}(g_{t_j},[0,1])$ ((iv.10)). [by C1, C4.2; 089 C2.6 (3.4)] [check: C5-product-form]
  - **C6** (added in fix pass, critic iteration 1 #3) Transport to the twelve tiles, read from the package's code: $F_j=K_j\circ F_1$ with the $K_j$ the double transpositions, $F'_j=N\circ F_{\pi^{-1}(j)}$, $|\mu|$ chart-independent, so $|\mu_{12}(g\cdot Z_0)|=|\mu_{\pi^{-1}(1)\pi^{-1}(2)}(Z_0)|$ with $Z_0\in D$; on the orbit $\{-1,2,\tfrac12\}$ of $Z_0=-1$ only $Z=\tfrac12$ carries the class of $(13)$. [cited: the package's section, relabelling, tile and membership routines; 080 (1.3); eq. (iv.11)] (089 C2.3's numerics confirm it; not its support)

Open gaps: none
Hypotheses in force: none (the package's formulas are a provisional cited input, not a hypothesis; PH34 is not used)

## Block (i) – anchors tied to the package (critic #9)

\subsection*{Setup}
A1, A2. $A_{\rm seg}(Z)=(1+Z)/(3Z)$, $B_{\rm seg}(Z)=(1+3x)/(2(1+x))$, $x=e^{-{\rm arccosh}(2Z-1)}$ (`codes/verify-mu-table.py` l. 661–669, re-typed there). Package: `R_interior`, `R_anchor`, `R_naive`, `weight_lambda1`, `_d3`, `_d4`.

\subsection*{Derivation}
The claim (3.6) of 089 rests on two facts about the package's code:
$$
\frac1{R_{\rm interior}(Z)}=A(Z)+L(Z)\,\big(B(Z)-A(Z)\big),\qquad L(Z)={\tt weight\_lambda1}(Z,\beta)\in[0,1]\quad(Z\in D). \tag{i.1}
$$
The first is the body of `R_interior` (critic iteration 2, hand check (a)); here it is asserted against the package's own functions, not the re-typed formula. The second holds by hand: $d_3=(|Z|^2-1)(|Z-1|^2-1)\ge0$ on the FD ($|Z|\ge1$, and $\Re Z\le\tfrac12$ gives $|Z-1|^2\ge|Z|^2$), $d_4=\ln4\beta^2-\Re w\ge0$ inside the ellipse, so $s=d_3/(d_3+\lambda_0d_4)\in[0,1]$, $\phi(s)=s^2(3-2s)\in[0,1]$; the branch $d_3+\lambda_0d_4\le0$ returns $1$. Under rounding ($d_3$ or $d_4$ of order $-10^{-16}$ on a wall) $s$ leaves $[0,1]$ by $O(10^{-16})$, and $\phi$ stays in $[0,1]$ on $[-\tfrac12,\tfrac32]$.

*Computation* (`C1-tie`, `C1-anchors`, `C1-weight-range`, `BREAK-C1-tie`; $\beta=\tfrac32$, $2$; 200 random points of $D$ and 240 wall points, corners $Z=-1+10^{-16}i$ and $e^{i\pi/3}$ included):

| | $\beta=\tfrac32$ | $\beta=2$ |
| --- | --- | --- |
| $\max\lvert1/R_{\rm interior}-(A_{\rm seg}+L(B_{\rm seg}-A_{\rm seg}))\rvert$ | rounding level | rounding level |
| $\max\lvert A_{\rm seg}-1/R_{\rm anchor}\rvert$, $\max\lvert B_{\rm seg}-1/R_{\rm naive}\rvert$ | rounding level | same |
| range of the package's $L$ on 4000 points (2000 random, 2000 on walls); $\min d_3$, $\min d_4$ | (companion value, not reproduced here) | (companion value, not reproduced here) |
| $L$ on C3 / on C4 (three points each) | (companion value, not reproduced here) | same |
| break: a 1 % typo ($3\to3.03$) in $A$, in $B$: tie error | $4.8\times10^{-3}$, $1.9\times10^{-3}$ | $4.3\times10^{-3}$, $1.4\times10^{-3}$ |

The weight-range assertion is now its own check (`C1-weight-range`); 089's `BREAK-C2-segment` bundled it.

\subsection*{Commentary}
The package's anchor is singular at the exact corner $Z=-1$; 089's boundary sample $e^{i\pi}=-1+1.2\times10^{-16}i$ avoids it, and the section there is defined by continuity (089 (3.3)). The tie is at rounding level everywhere, walls included, so 089's (3.6) holds for the package's code and not only for the record's reading of it.

\subsection*{Result}
C1 holds: the package's $1/R$ is $A+L(B-A)$ with 089's $A$, $B$, and the package's $L$ lies in $[0,1]$ on $D$ (by hand; sampled check at rounding level). Critic #9 closed.

## Block (ii) – step control (critic #8)

\subsection*{Setup}
089's sampled boundary `fd_boundary` ($4\times20000$ points, counter-clockwise; C1, C3, C2, C4), the curves $v\in\{B-A,\ g_1,\ g_0,\ g_{1/Z}\}$ on it, forbidden sets $K_{B-A}=\{0\}$, $K_{g_t}=[0,1]$. ${\rm dist}_k={\rm dist}(v_k,K)$.

\subsection*{Derivation}
*Lemma.* If $|v_{k+1}-v_k|<\min({\rm dist}_k,{\rm dist}_{k+1})$ for every $k$, the polygon $P$ through the samples misses $K$ (the chord $[v_k,v_{k+1}]$ lies in the disc of radius $|v_{k+1}-v_k|$ about $v_k$, which misses $K$), and for every $p\in K$ the sum of principal arguments $\sum_k{\rm Arg}\,\frac{v_{k+1}-p}{v_k-p}$ is $2\pi$ times the winding number of $P$ about $p$ (a chord missing $p$ subtends an angle in $(-\pi,\pi)$, which is its principal value). With $K$ connected, that winding number is the same for every $p\in K$. The script asserts the stronger $|v_{k+1}-v_k|<\tfrac12\min({\rm dist}_k,{\rm dist}_{k+1})$. $\tag{ii.1}$

For $g_0$, ${\rm dist}_k\to0$ at the corner $Z=-1$, where $g_0$ touches $0$; there (ii.1) is asserted with $K=[0,1]$ on $|Z+1|\ge10^{-2}$ and with $K=\{\tfrac12\}$ everywhere (so the winding about $\tfrac12$ is the polygon's); that $g_0$ misses $(0,1]$ inside $|Z+1|<10^{-2}$ is 089's corner argument (3.7), now superseded by the exact C4.3.

*Computation* (`C2-step`, `BREAK-C2-coarse`): largest value of $|v_{k+1}-v_k|/\min({\rm dist}_k,{\rm dist}_{k+1})$ (asserted $<\tfrac12$), largest step, smallest distance, winding.

[Table of companion-project values removed.]

The windings of all four curves are zero to rounding ($\le10^{-15}$) at both $\beta$; the break leg (12 samples per wall) fails the step assertion at both $\beta$.

\subsection*{Commentary}
The steps in the $g$-plane are (companion value, not reproduced here), against distances (companion value, not reproduced here) ($g_1$, $g_{1/Z}$), (companion value, not reproduced here) ($g_0$ off the corner disc) and nonzero ($B-A$): the worst ratio is (companion value, not reproduced here). The critic's hand estimate ($|g'|$ up to a few hundred near $e^{i\pi/3}$, steps up to $0.1$) was pessimistic: the exact forms of block (iv) give a much smaller $|{\rm d}g_1/{\rm d}Z|$ there. 089's Commentary sentence, which compared a distance in the $g$-plane with a step in the $Z$-plane, now reads: the largest step in the $g$-plane is below a small fraction of the local distance to the forbidden set on every curve. What (ii) does not give: the true curve between two samples (block (iv)).

\subsection*{Result}
C2 holds at $\beta=\tfrac32$, $2$: the windings read by 089 (all $0$) are the windings of the sampled polygons, which miss the forbidden sets (for $g_0$, off $|Z+1|<10^{-2}$). Critic #8 closed for the sampled route; the break leg fires.

## Block (iii) – $\beta>2$ (critic #5)

\subsection*{Setup}
A3. $A$, $B$, $t_j$ do not depend on $\beta$; only $D(\beta)$ does, and $D(\beta)\subset D(\beta')$ for $\beta\le\beta'$ (confocal ellipses, foci $0,1$; package `ellipse_axes`: $a,b=\beta^2\pm1/(16\beta^2)$, $a^2-b^2=\tfrac14$).

\subsection*{Derivation}
*Sampled route at larger $\beta$* (`C3-windings`, same checks as block (ii), 20000 points per wall):

[Table of companion-project values removed.]

At $\beta=3,4,10$ all four windings are below $2\times10^{-15}$ in modulus. The minimum distance of $g_{1/Z}$ decreases with $\beta$ towards the tail value ${\rm dist}(-2,[0,1])=2$ along the growing C4 (location not printed).

*Tail and limiting region.* As $\beta\to\infty$, $D(\beta)\uparrow{\rm FD}$ (the closed fundamental domain, unbounded). Sampling cannot reach it; the exact route of block (iv) does: in the coordinate $x=q/(4\beta^2)$, $Z=\infty$ is $x=0$, the closed FD together with $Z=\infty$ is the compact curvilinear triangle $T=\{\Im x\le0,\ |x|\le1\}\cap\{Z(x)\in{\rm FD}\}\cup\{0\}$ with vertices $x=0$ ($Z=\infty$), $x=-(3-2\sqrt2)$ ($Z=-1$), $x=-i(2-\sqrt3)$ ($Z=e^{i\pi/3}$), and $D(\beta)=T\cap\{|x|\ge1/(4\beta^2)\}$. The anchors extend holomorphically to $x=0$: $A=\tfrac13$, $B=\tfrac12$, $g_1=4$, $g_0=g_{1/Z}=-2$ there (the critic's limits). Block (iv) proves the criterion on all of $T$ at once.

\subsection*{Result}
C3: the sampled route passes at $\beta=3,4,10$ (Numerical, as 089); the statement for every $\beta\ge\beta_{04}$ is C4 (exact, on the limiting region $T\supset D(\beta)$ for every $\beta$). Critic #5 closed: range every $\beta\ge\beta_{04}=\tfrac12+\tfrac1{\sqrt2}$ (the package's range; the physical range $\beta\ge\tfrac32$ included).

## Block (iv) – certification (critic #7)

Deviation from the brief, one line: the interval-arithmetic enclosure was not built, because the coordinate $x$ below makes $A$, $B$, $t_j$ rational and the criterion decidable in closed form; that proves more than an enclosure on $\partial D(\beta)$ would (no sampling, no argument principle, every $\beta$ at once).

\subsection*{Setup}
A1–A3, C1. $w={\rm arccosh}(2Z-1)$ (package `_w_of_Z`, principal branch), $x:=e^{-w}$.

\subsection*{Derivation}
*Uniformization (C4.1).* From $\cosh w=2Z-1$, $x+1/x=2(2Z-1)$:
$$
Z=\frac{(1+x)^2}{4x},\qquad x=\frac{q}{4\beta^2}, \tag{iv.1}
$$
the second since the package's `q_of_Z` is $4\beta^2u$ with $u$ the $|u|<1$ root of $u^2-2(2Z-1)u+1=0$, the same equation. For $Z\notin[0,1]$, $\Re w>0$, so $|x|<1$; $x\mapsto Z$ is the Joukowski bijection from the punctured open unit disc onto $\mathbb C\setminus[0,1]$. With $x=\rho e^{i\varphi}$, $\Im Z=\tfrac14(\rho-\rho^{-1})\sin\varphi$, so $\Im Z\ge0\iff\Im x\le0$. On the real axis, ${\rm d}Z/{\rm d}x=(x^2-1)/(4x^2)<0$ on $(-1,0)$ with $Z(-1)=0$, $Z(0^-)=-\infty$, $Z(-3+2\sqrt2)=-1$; and $Z(x)\ge1$ for $x\in(0,1)$ ($(1+x)^2\ge4x$). Hence
$$
{\rm FD}\cap\mathbb R=(-\infty,-1]\ \longleftrightarrow\ x\in[-(3-2\sqrt2),0),\qquad Z\in(-1,0)\ \longleftrightarrow\ x\in(-1,-(3-2\sqrt2)). \tag{iv.2}
$$
$x$ has no jump across the cut $2Z-1<-1$ (089 §3b, critic #1), so the package's $B$ is $B(x(Z))$ on C1 from either side.

*Rational forms (C4.2).* Substituting (iv.1) into $A=(1+Z)/(3Z)$ and $B=(1+3x)/(2(1+x))$:
$$
\begin{aligned}
A&=\frac{1+6x+x^2}{3(1+x)^2},\qquad B-A=\frac{1+7x^2}{6(1+x)^2},\\
g_1&=\frac{1-A}{B-A}=\frac{4(1+x^2)}{1+7x^2},\qquad
g_0=\frac{-A}{B-A}=-\frac{2(1+6x+x^2)}{1+7x^2},\qquad
g_{1/Z}=\frac{1/Z-A}{B-A}=-\frac{2(1-6x+x^2)}{1+7x^2}=g_0(-x).
\end{aligned} \tag{iv.3}
$$

*Preimages of $[0,1]$ (C4.3).* For $s\in[0,1]$:

- $g_1=s\iff(4-7s)x^2+(4-s)=0$, so $x^2=(s-4)/(4-7s)$ ($s\ne\tfrac47$; at $s=\tfrac47$ no finite root) and
  $$|x|^4-1=\frac{(4-s)^2-(4-7s)^2}{(4-7s)^2}=\frac{48\,s(1-s)}{(4-7s)^2}\ge0 .$$
  Every preimage has $|x|\ge1$: no $Z\in\mathbb C\setminus[0,1]$ has $g_1(Z)\in[0,1]$. $\tag{iv.4}$
- $g_0=s\iff(7s+2)x^2+12x+(s+2)=0$, discriminant$/4$ $=32-16s-7s^2\ge9$ on $[0,1]$ (concave, endpoint values $32$, $9$): two real roots, sum $-12/(7s+2)<0$, product $(s+2)/(7s+2)>0$, both negative. For $s>0$, $g_0=s$ with $1+7x^2>0$ forces $1+6x+x^2<0$, i.e. $x\in(-3-2\sqrt2,-3+2\sqrt2)$; inside the unit disc that is $x\in(-1,-(3-2\sqrt2))$, i.e. $Z\in(-1,0)$ by (iv.2): $|Z|<1$, not in the FD. For $s=0$: $x=-3\pm2\sqrt2$, in the disc only $x=-(3-2\sqrt2)$, $Z=-1$. $\tag{iv.5}$
- $g_{1/Z}(x)=g_0(-x)$: the preimages are the negatives of (iv.5), real positive, i.e. $Z\in(1,\infty)$ ($\Re Z>\tfrac12$), not in the FD; for $s=0$, $x=3-2\sqrt2$, $Z=2$. $\tag{iv.6}$
- $B-A=0\iff x=\pm i/\sqrt7$, $Z=\tfrac12\mp\tfrac{3\sqrt7}{14}i$, $|Z|^2=\tfrac47<1$: not in the FD; the poles of (iv.3) are at $x=-1$ ($|x|=1$, $Z=0$) and at $x=\pm i/\sqrt7$ ($g_t$). $\tag{iv.7}$
- Zeros ($s=0$) of $g_1$: $x=\pm i$, $Z=\tfrac12$ (on $[0,1]$). $\tag{iv.8}$

Hence, on the whole closed FD (every $\beta$: $D(\beta)\subset{\rm FD}$):
$$
\boxed{\ B\ne A,\qquad g_1,\ g_{1/Z}\notin[0,1],\qquad g_0\notin(0,1],\quad g_0=0\iff Z=-1\ } \tag{iv.9}
$$
and with C1 and 089 (3.4), $\mu_{1j}=S_0(1/R-t_j)$, $S_0\ne0$:
$$
\mu_{1j}=S_0\,(B-A)\,\big(L-g_{t_j}\big)=S_0\,\frac{1+7x^2}{6(1+x)^2}\,\big(L-g_{t_j}(x)\big),\qquad |\mu_{1j}|\ge|S_0|\,|B-A|\,{\rm dist}\big(g_{t_j},[0,1]\big). \tag{iv.10}
$$
So for every weight $L\in[0,1]$, $\mu_{1j}\ne0$ on $D(\beta)$ except possibly $\mu_{13}$ at $Z_0=-1$, where (iv.10) gives $\mu_{13}(-1)=S_0(-1)\,(1-1/\sqrt2)\,L(-1)$ (089's value): zero for the package's weight when $\beta>\beta_{04}$ (at $\beta=\beta_{04}$ exactly the corner $Z_0=-1$ is C3$\cap$C4, where the package's weight returns $L=1$ and $\mu_{13}(-1)\ne0$; the non-vanishing is unaffected, it needs only $L\in[0,1]$). Transported ((iv.11), C6), $\mu_1=\mu_2\ne0$ on the closed $\mathcal V_{0,4}$ except possibly at $Z=\tfrac12$, in particular at every point of $Q_V$, for every $\beta\ge\beta_{04}$.

*Transport to the twelve tiles (C6; read from the package's code, no numerics).* Three facts, each a line of the code:
$$
\begin{aligned}
&\text{(a) section on the fundamental domain}:\ F_j=K_j\circ F_1\ (j=2,3,4),\\
&\phantom{\text{(a) }}K_2,K_3,K_4\ \text{Möbius maps realising }(12)(34),\ (13)(24),\ (14)(23)\ \text{on }(0,1,\infty,Z);\\
&\text{(b) relabelling}:\ F'_j=N\circ F_{\pi^{-1}(j)}\ (\text{conjugation first}),\ N\ \text{Möbius};\ \ |\mu|\ \text{is chart-independent (080 (1.3))},\ \text{so}\\
&\phantom{\text{(b) }}|\mu_{12}(g\cdot Z_0)|=|\mu_{\pi^{-1}(1)\pi^{-1}(2)}(Z_0)|,\qquad g=(\pi,{\rm conj})=\texttt{tile\_of}(Z),\ Z_0\in D;\\
&\text{(c) }\texttt{in\_V04}(Z):\ \text{is defined as }Z_0=\texttt{tile\_of}(Z)\in D,\ \text{so every point of }\mathcal V_{0,4}\text{ is }g\cdot Z_0\text{ with }Z_0\in D.
\end{aligned} \tag{iv.11}
$$
By (a), every ordered pair of $F_i$ at $Z_0$ is, in modulus, one of $\mu_{12},\mu_{13},\mu_{14}$ at $Z_0$, so (iv.9)–(iv.10) cover all pairs on $D\setminus\{-1\}$ and nothing more is needed there. At $Z_0=-1$ ($1/R=0$ for $\beta>\beta_{04}$): $|\mu_{12}|=|\mu_{14}|=|S_0(-1)|\ne0$ and $\mu_{13}$ is the only possible zero. The $s$-pair of a point of the orbit $\{-1,2,\tfrac12\}$ of $Z_0=-1$ is, by (b), $(\pi^{-1}(1)\pi^{-1}(2))$ at $Z_0=-1$: $Z=-1$ is reached with $g=e$, pair $(12)$; $Z=2$ with $g=(12)$ ($Z\mapsto1-Z$, the second element of `TILE_GROUP`), pair $(21)\simeq(12)$ by $K_2$; $Z=\tfrac12$ with $g=(23)$ ($Z\mapsto Z/(Z-1)$), pair $(13)$, the only one in the class $\{13,24\}$. Hence $\mu_1=\mu_2$ vanishes on the closed $\mathcal V_{0,4}$ at most at $Z=\tfrac12$. (A one-off run of `tile_of` at exact real $Z=-1,2,\tfrac12$ returns (companion value, not reproduced here); at neighbouring complex $Z$ other elements of the same orbit appear, with the same class at $Z_0$. Scratch, not a check of the script.) The phase reading (089 C2.2, A4) affects only the phase of $\mu_1=\mu_2$, not the zero set.

*Computation* (`C4.1-uniformization`, `C4.2-rational-forms`, `C4.2-package-tie`, `BREAK-C4.2-package-tie`, `C4.3-preimages`, `C4.3-scan`, `BREAK-C4.3-planted`, `C5-product-form`):

| check | outcome |
| --- | --- |
| C4.1 at $\beta=\tfrac32,2,4$ (440 points of $D$ and walls, 30 points on C1 from below the cut) | $\max\lvert(1+x)^2/(4x)-Z\rvert/\max(1,\lvert Z\rvert)=8\times10^{-16}$; $\max\lvert q/(4\beta^2)-x\rvert\le3.7\times10^{-15}$; $\max\lvert x\rvert=0.2679=2-\sqrt3$ (at $e^{i\pi/3}$); $\max\Im x=2\times10^{-17}$; jump of $x$ across C1 $3\times10^{-17}$ |
| C4.2, sympy | (iv.3) exact (`simplify` of the differences $=0$) and at 5 random complex $x$ to $4\times10^{-15}$ |
| C4.2 against the package ($1/R_{\rm anchor}$, $1/R_{\rm naive}$ at the package's $x$) | agreement at rounding level; break $7\to6.9$: $1.1\times10^{-3}$ |
| C4.3, sympy (identities; the inequalities of (iv.4)–(iv.8) are by hand) | the quadratics, $|x|^4-1=48s(1-s)/(4-7s)^2$, the discriminant, $Z(-3+2\sqrt2)=-1$, ${\rm d}Z/{\rm d}x$, $g_{1/Z}(x)=g_0(-x)$, $\lvert Z\rvert^2=\tfrac47$ at the zeros of $B-A$, $Z(\pm i)=\tfrac12$, $Z(3-2\sqrt2)=2$: all exact |
| C4.3-scan (roots of $6(1+x)^2(t-A)-s(1+7x^2)$ for 2001 values of $s$, mapped to $Z$, tested with `in_closed_FD`) | $t=1$: 0 roots in the closed FD; $t=1/Z$: 0; $t=0$: 1, and every hit is at the corner (asserted: hits $\ge1$ and $\max\lvert Z+1\rvert<10^{-6}$; observed $2\times10^{-15}$, $s=0$) |
| break: planted constant $t^*=A+\tfrac12(B-A)$ at $Z^*=-0.3+1.5i$ | 1974 roots in the closed FD, $\max\lvert Z+1\rvert=2.24$: fires, and the $t=0$ corner-only assertion rejects them |
| C5 ((iv.10) against 089's jet route `mu_pair`, 100 points $\times$ 3 pairs) | $1.6\times10^{-15}$ ($\beta=\tfrac32$), $7\times10^{-16}$ ($\beta=4$) |

\subsection*{Commentary}
(iv.1): $x$ is the plumbing parameter in units of its fold value $4\beta^2$ ($|x|=1$ is $Z\in[0,1]$); the propagator region is $|x|<1/(4\beta^2)$, and the $\beta$-dependence of $D(\beta)$ is only the inner circle $|x|\ge1/(4\beta^2)$ (C4 is $|q|=1$). (iv.3) explains 089's numbers: $|B-A|$ is smallest at $e^{i\pi/3}$ because $B-A$ vanishes at $Z=\tfrac12+0.567i$, just below that corner on the line $\Re Z=\tfrac12$; $g_1(-1)=2+\sqrt2$ (089's $2.414$ is ${\rm dist}=1+\sqrt2$); the tail values $4$, $-2$, $-2$ are $x=0$. (iv.4) is the strongest statement: $1\in[A,B]$ never happens off $[0,1]$, so the $(12)$ factor of $\mu$ on the FD never vanishes, for any weight in $[0,1]$. (iv.5)–(iv.6) say that $0$ and $1/Z$ enter the segment only along the real $Z$-axis, outside the FD, and $0$ reaches its endpoint $A$ exactly at the corner $Z=-1$. Nothing in (iv.4)–(iv.8) is numerical: the scan is a second route, not the support. Why the anchors are rational in $x$: $A$ is rational in $Z$, which is rational in $x$; $B$ is the $C4$ datum, rational in $q$ by construction (`R_naive`: "beta-independent as a function of Z (via x only)").

\subsection*{Result}
C4 (and C5) hold exactly, given the package's formulas: (iv.9) on the whole closed FD, hence on $D(\beta)$ for every $\beta\ge\beta_{04}$; the weight enters only through $L\in[0,1]$ (C1). Critic #7 closed by a stronger route than the one it proposed.

## Verification – run

`OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 /usr/bin/time -v .venv/bin/python codes/verify-mu-segment-cert.py` (run 3, 2026-10-04 22:13, after the fix pass; runs 1 and 2 were 30/30 as well, run 1 with the looser C4.1 bound; the fix pass changed only `C4.3-scan`'s $t=0$ assertion and `BREAK-C4.3-planted`, plus the docstring, critic-092 #6, #7), exit 0, **30/30 PASS**, 0.6 s, peak RSS 86 MB (limit 0.5 GB). The script imports `codes/verify-mu-table.py` (unchanged; its module code only re-creates an existing scratch folder) and the package by path. Every check that can be broken has a break leg that fires: `BREAK-C1-tie`, `BREAK-C2-coarse`, `BREAK-C4.2-package-tie`, `BREAK-C4.3-planted` (now also shows that the $t=0$ corner-only assertion rejects hits away from the corner); `C4.2-rational-forms` and `C4.3-preimages` are exact sympy identities that any change of a coefficient breaks, the inequalities of (iv.4)–(iv.8) are by hand (not machine-checked). Not machine-checked here: the package's construction (089 C2.2) and 080 (1.7) (Proven in R86 C1); the transport (iv.11) is a reading of the code, backed by 089's numerics.

```text
seed 20261004 (+92)
[PASS] C1-tie[b=1.5]: tie of the package's 1/R to A_seg + L (B_seg - A_seg) at rounding level (440 pts: 200 random in D, 240 on the four walls incl. corners)
[PASS] C1-anchors[b=1.5]: anchors A_seg, B_seg tie to the package at rounding level
[PASS] C1-weight-range[b=1.5]: (companion value, not reproduced here)
[PASS] BREAK-C1-tie[b=1.5]: typo 3 -> 3.03 in A: tie error 4.8e-03; in B: 1.9e-03 (both fail 1e-13)
[PASS] C1-tie[b=2.0]: tie of the package's 1/R to A_seg + L (B_seg - A_seg) at rounding level (440 pts: 200 random in D, 240 on the four walls incl. corners)
[PASS] C1-anchors[b=2.0]: anchors A_seg, B_seg tie to the package at rounding level
[PASS] C1-weight-range[b=2.0]: (companion value, not reproduced here)
[PASS] BREAK-C1-tie[b=2.0]: typo 3 -> 3.03 in A: tie error 4.3e-03; in B: 1.4e-03 (both fail 1e-13)
[PASS] C2-step[b=1.5]: steps and distances (companion value, not reproduced here); windings: B-A 2.1e-16; g_1 4.8e-18; g_1/Z -1.6e-16; g_0 1.2e-16
[PASS] BREAK-C2-coarse[b=1.5]: 12 samples per wall: step condition fails on ['g_0'] (ratios: companion value, not reproduced here)
[PASS] C2-step[b=2.0]: steps and distances (companion value, not reproduced here); windings: B-A 8.8e-17; g_1 4.2e-17; g_1/Z 6.5e-16; g_0 5.1e-16
[PASS] BREAK-C2-coarse[b=2.0]: 12 samples per wall: step condition fails on ['g_1/Z', 'g_0'] (ratios: companion value, not reproduced here)
[PASS] C3-windings[b=3.0]: steps and distances (companion value, not reproduced here); windings: B-A 4.4e-16; g_1 4.5e-18; g_1/Z 1.2e-15; g_0 -2.3e-16
[PASS] C3-windings[b=4.0]: steps and distances (companion value, not reproduced here); windings: B-A 3.4e-16; g_1 1.6e-17; g_1/Z 3.5e-16; g_0 2.5e-16
[PASS] C3-windings[b=10.0]: steps and distances (companion value, not reproduced here); windings: B-A 1.9e-16; g_1 1.3e-17; g_1/Z 1.9e-16; g_0 -3.5e-16
[PASS] C4.2-rational-forms: B - A = (1+7x^2)/(6(1+x)^2), g_1 = 4(1+x^2)/(1+7x^2), g_0 = -2(1+6x+x^2)/(1+7x^2), g_1/Z = -2(1-6x+x^2)/(1+7x^2): sympy True, 5 random x: 4.2e-15
[PASS] C4.3-preimages: t=1: (4-7s)x^2 + (4-s) = 0, |x|^4 - 1 = 48s(1-s)/(4-7s)^2 >= 0: True | t=0: (7s+2)x^2 + 12x + (s+2) = 0, disc/4 = 32 - 16s - 7s^2 >= 9, roots < 0; x in (-1, -3+2sqrt2) maps onto Z in (-1, 0); Z(-3+2sqrt2) = -1: True | t=1/Z: g_1/Z(x) = g_0(-x), preimages x > 0 <=> Z > 1: True | B - A = 0 at Z = 1/2 - 3*sqrt(7)*I/14, 1/2 + 3*sqrt(7)*I/14, |Z|^2 = 4/7: True | zeros of g_1, g_1/Z at Z = 1/2, 2 (not in FD): True
[PASS] C4.1-uniformization[b=1.5]: max |(1+x)^2/(4x) - Z|/max(1,|Z|) = 7.8e-16; max |q/(4b^2) - x| = 9.4e-16; max |x| = 0.2679 (<= 2 - sqrt3 = 0.2679 asserted); max Im x = 2.1e-17; x jump across C1 = 3.1e-17
[PASS] C4.2-package-tie[b=1.5]: package anchors agree with the rational forms at 440 pts of D and walls, at rounding level
[PASS] BREAK-C4.2-package-tie[b=1.5]: 7 -> 6.9 in B - A: error 1.1e-03 (fails 1e-13)
[PASS] C4.1-uniformization[b=2.0]: max |(1+x)^2/(4x) - Z|/max(1,|Z|) = 7.8e-16; max |q/(4b^2) - x| = 1.3e-15; max |x| = 0.2679 (<= 2 - sqrt3 = 0.2679 asserted); max Im x = 2.1e-17; x jump across C1 = 3.1e-17
[PASS] C4.2-package-tie[b=2.0]: package anchors agree with the rational forms at 440 pts of D and walls, at rounding level
[PASS] BREAK-C4.2-package-tie[b=2.0]: 7 -> 6.9 in B - A: error 1.1e-03 (fails 1e-13)
[PASS] C4.1-uniformization[b=4.0]: max |(1+x)^2/(4x) - Z|/max(1,|Z|) = 8.1e-16; max |q/(4b^2) - x| = 3.7e-15; max |x| = 0.2679 (<= 2 - sqrt3 = 0.2679 asserted); max Im x = 2.1e-17; x jump across C1 = 3.1e-17
[PASS] C4.2-package-tie[b=4.0]: package anchors agree with the rational forms at 440 pts of D and walls, at rounding level
[PASS] BREAK-C4.2-package-tie[b=4.0]: 7 -> 6.9 in B - A: error 1.1e-03 (fails 1e-13)
[PASS] C4.3-scan: roots in the closed FD over 2001 values of s: t=1: 0, t=1/Z: 0, t=0: 1 (every one of them at |Z + 1| <= 2.1e-15, the corner Z = -1; asserted: hits >= 1 and max |Z + 1| < 1e-6)
[PASS] BREAK-C4.3-planted: planted t* = A + (B - A)/2 at Z* = -0.3 + 1.5i: 1974 roots in the closed FD, max |Z + 1| = 2.24; the t=0 leg's corner-only assertion rejects them (only_at_corner = False)
[PASS] C5-product-form[b=1.5]: max ||mu_1j| - |S_0 (B-A)(L - g_j)|| = 1.6e-15 (100 pts x 3 pairs)
[PASS] C5-product-form[b=4.0]: max ||mu_1j| - |S_0 (B-A)(L - g_j)|| = 7.2e-16 (100 pts x 3 pairs)
SUMMARY: 30/30 PASS (0.6 s)
Maximum resident set size (kbytes): 86412
```

## What R86's tag and range can become

- **The criterion itself** ((iv.9): on the closed FD, $1,1/Z\notin[A,B]$, and $0\in[A,B]$ only at $Z=-1$, where $0=A$) is a statement about explicit elementary functions, proved in closed form: **Proven** (exact algebra: identities sympy-exact, inequalities by hand), independent of the package's status and of $\beta$.
- **R86's every-point clause** ("$\mu_i(q)\ne0$ at every point of $Q_V$ given the sister's package") goes from *Numerical, $\beta\le2$* to **Proven given the package's formulas, every $\beta\ge\beta_{04}$, any interpolation weight with values in $[0,1]$**, provisional with the package. Its chain: C1 (the code computes $A+L(B-A)$ and $L\in[0,1]$; by hand, checked at rounding level), (iv.9), 089 (3.4) (from 080 (1.7), R86 C1), and the Klein reduction and transport, read from the code in (iv.11) (C6; 089's numerics confirm). The tag is Proven, not Verified: the argument is a complete hand derivation from the package's formulas; the sympy identities and the numeric ties are its verification lines, as the tag table prescribes. *Numerical* no longer describes the evidence; no "Verified" alternative is proposed.
- **R86's second clause, "nowhere else in $\mathcal V_{0,4}$ for the $s$-pair"** (R86's Status line, now *Numerical given the package*): C0's "$\mu_1=\mu_2\ne0$ on the closed $\mathcal V_{0,4}$ except possibly at $Z=\tfrac12$" makes it **Proven given the package's formulas** as well, for every $\beta\ge\beta_{04}$ ((iv.9)–(iv.11)); the orchestrator updates both clauses (critic-092 #4). Also affected: the **Scope** bullet's "(closed numerically by record 089 …)".
- **The zero at $Z=\tfrac12$**: unchanged (Proven for every $S_4$-symmetric section, 089 (3.2)/(3.2')); (iv.10) gives the package's value $\mu_{13}(-1)=S_0(-1)(1-1/\sqrt2)L(-1)=0$ in one line, for $\beta>\beta_{04}$ (at $\beta=\beta_{04}$ exactly the corner is C3$\cap$C4, a cusp of $D$: $d_3(-1)=d_4(-1)=0$, the package's weight returns $L=1$ through its `a + b <= 0` branch and is discontinuous there, so $\mu_{13}(-1)=S_0(-1)(1-1/\sqrt2)\ne0$; at that one value of $\beta$ the package's formula does not deliver the zero at $Z=\tfrac12$ (089 C2.4), whose premise, a section continuous at the corner, fails; the non-vanishing claim is unaffected).- **089's sampled route** keeps its role as a second route: its windings are now certified at the polygon level (C2) and it passes at $\beta=3,4,10$ (C3).
- **Range.** "$\beta\le2$" is replaced by "every $\beta\ge\beta_{04}=\tfrac12+\tfrac1{\sqrt2}$" (the package's range; $D(\beta)\subset{\rm FD}$ and (iv.9) holds on the whole FD). Below $\beta_{04}$ the package does not define the section ($\mathcal V_{0,4}\ne{\rm FD}\cap$ ellipse, R7): not covered, and not needed for the physical range $\beta\ge\tfrac32$.

## What remains

- The package is provisional. Every statement about $\mu$ is "given the package's formulas": $A$, $B$ (exactly the two anchors), the weight's range, $S_0$, the Klein maps and the transport. A revision of the weight that keeps it in $[0,1]$ and keeps the anchors leaves the result intact; a change of anchor does not.
- 089 C2.2 (the reading of the package's labels and phase) affects only the phase of $\mu_1=\mu_2$, not the zero set; 089 C2.3 (the transport) is read from the package's code in (iv.11), two lines, and 089's numerics confirm it. The package's section construction itself is not examined here.
- Not built: interval arithmetic on $\partial D$ (critic #7's route) – superseded, since (iv.9) needs no enclosure.
- Optional, not done: an exact lower bound on $|\mu_1|$ over $Q_V$ from (iv.10) (it would replace 089's sampled minima of $|\mu_1|$ by bounds); (iv.10) gives it as $|S_0||B-A|\,{\rm dist}(g_t,[0,1])$, with every factor explicit in $x$.
- Critic #6 (orchestrator's call): with the every-point clause Proven given the package, R86's a.e. clause Conditional(PH34) adds nothing to the non-vanishing.

## Self-review

1. **Objective.** Answered: R86's every-point clause can rise from Numerical to Proven given the package's formulas, and its range from $\beta\le2$ to every $\beta\ge\beta_{04}$; what it still rests on is listed above.
2. **Weakest step.** The application of (iv.9) to $\mu$ goes through the package's code as read: C1 ties the anchors and the weight at rounding level, and the Klein maps and the transport are read from the package's code in (iv.11) (C6), 089's numerics confirming; what remains unreviewed is the package itself. The algebra (iv.3)–(iv.8) is exact and short; its sympy check is falsifiable (any coefficient change breaks the identities; the numeric tie to the package fails at $10^{-3}$ under a $7\to6.9$ change; the root scan finds 1974 roots in the FD for a planted value).
3. **Not checked.** The package's construction itself (out of scope, the sister's); $\beta<\beta_{04}$ (outside the package's range). The C2 step condition near the corner for $g_0$ uses the point $\tfrac12$, not $[0,1]$ – acceptable because C0 no longer rests on C2.
4. **What a stronger reader would find in five minutes.** That the anchors are rational in $q$ – found, and it is the result. Possibly that $g_1(x)=4(1+x^2)/(1+7x^2)$ makes "the $(12)$ factor never vanishes" true off $[0,1]$ for any weight, not only on the FD: noted in the Commentary of block (iv).

## Proposed R86 verification line

- 2026-10-04 – exact/numerical check (provisional: the external reference implementation) – `codes/verify-mu-segment-cert.py`, 30/30 PASS (re-run after fix pass 1, 0.6 s, peak 86 MB), seed 20261004 (+92), β = 3/2, 2 (blocks i, ii), 3, 4, 10 (sampled route), 3/2, 2, 4 (package ties) – record 092: in $x=q/(4\beta^2)$ the anchors are rational, $B-A=(1+7x^2)/(6(1+x)^2)$, $g_1=4(1+x^2)/(1+7x^2)$, $g_0=-2(1+6x+x^2)/(1+7x^2)$, $g_{1/Z}(x)=g_0(-x)$, and the preimages of $[0,1]$ are explicit and miss the closed FD except $g_0=0$ at $Z=-1$ (identities sympy-exact, inequalities by hand; numeric root scan as second route, its $t=0$ leg asserts that every hit is at the corner; break legs fire); so $\mu_{1j}=S_0(B-A)(L-g_{t_j})\ne0$ on $D(\beta)$ except possibly $\mu_{13}(-1)$, for every weight in $[0,1]$ and every $\beta\ge\beta_{04}$ (the corner value $\mu_{13}(-1)=0$ for the package's weight holds for $\beta>\beta_{04}$ only: at $\beta_{04}$ the corner is C3$\cap$C4 and the weight returns $L=1$) – the every-point clause is exact given the package's formulas, no longer sampled; the package's `R_interior` equals $A+L(B-A)$ at rounding level on $D$ and its walls, $L\in[0,1]$ (`C1-tie`, `C1-weight-range`); 089's sampled windings certified at the polygon level (steps small against the distance, `C2-step`; ratio: companion value, not reproduced here) and passing at $\beta=3,4,10$; transport to the twelve tiles read from the package's `relabel`/`section_FD` (critic-092 (d); record 092 (iv.11)).
- 2026-10-04 – critic review – `agent/reports/critic-092-20261004T215700.md` – (iv.1)–(iv.10), the image of the closed FD, the $\beta$-range and the transport at the orbit of $Z_0=-1$ re-derived by hand; ACCEPT, minor (endpoint $\beta_{04}$ at the corner, scan leg, wording)

Where R86 changes (critic-092): the heading sentence, the bracketed tag, the **Status** line (every-point clause **and** the clause "nowhere else in $\mathcal V_{0,4}$ for the $s$-pair", both to Proven given the package's formulas, every $\beta\ge\beta_{04}$) and the **Scope** bullet's "(closed numerically by record 089 …)"; the critic's replacement text is in its report, section *R86 line*.

## Fix pass (critic iteration 1)

Source: `agent/reports/critic-092-20261004T215700.md` (ACCEPT; 0 critical, 0 major, 5 minor, notes). One line per finding, in the critic's words where it gives them.

- **#1, applied.** At $\beta=\beta_{04}$ exactly, $d_3(-1)=0$ and $d_4(-1)=\ln(3+2\sqrt2)-{\rm arccosh}\,3=0$: the corner $Z_0=-1$ is C3$\cap$C4 (a cusp of $D$), the package's weight is discontinuous there and returns $L=1$ through its `a + b <= 0` branch (read in `weight_lambda1`), so "$\mu_{13}(-1)=0$ for the package's weight" holds for $\beta>\beta_{04}$ only; the non-vanishing claim (every $\beta\ge\beta_{04}$) is unaffected. Parenthetical added at C0, after (iv.10) and in *What R86's tag…* (third bullet); one erratum line after (3.3) in `agent/derivations/089-mu-table.md` (bookkeeping, no other change to 089). Statement of C0 changed (the corner value), not its support.
- **#2** (note, "$(1,\infty)$" in (iv.6) vs the exact image $(1,2]$): no change, true as written.
- **#3, applied.** The transport is read from the code, not "confirmed numerically": new node C6 and (iv.11) (`section_FD`: $F_j=K_j\circ F_1$, $K_j$ the double transpositions; `relabel`: $F'_j=N\circ F_{\pi^{-1}(j)}$, $|\mu|$ chart-independent; the orbit of $Z_0=-1$: $g=e$, $(12)$, $(23)$ at $Z=-1,2,\tfrac12$, only the last in the class of $(13)$); the "Verified" alternative for R86 is dropped (the tag is Proven given the package). C0's citation of 089 C2.3 is replaced by C6; *What remains* (second bullet), *Self-review* (items 1, 2) and *What R86's tag…* (second bullet) updated. I re-read `tile_of`/`relabel`/`section_FD` in the package and ran `tile_of` once at exact real $Z=-1,2,\tfrac12$ (scratch, not a check): (companion value, not reproduced here), as the critic states. Justification of C0 changed, its statement unchanged by #3.
- **#4, applied.** *What R86's tag…* now lists R86's second clause, "nowhere else in $\mathcal V_{0,4}$ for the $s$-pair" (Status line; Numerical given the package), as upgraded to Proven given the package's formulas, with the Scope bullet "(closed numerically by record 089 …)" and the proposed-line section's "Where R86 changes".
- **#5, applied.** Block (iv) Commentary: "$x$ is the plumbing parameter in units of its fold value $4\beta^2$ ($|x|=1$ is $Z\in[0,1]$); the propagator region is $|x|<1/(4\beta^2)$". Wording only.
- **#6, applied.** `codes/verify-mu-segment-cert.py`: `preimages_in_FD` returns the largest $|Z+1|$ among the FD hits (was the smallest); `C4.3-scan`'s $t=0$ leg asserts `only_at_corner` (at least one hit and max $|Z+1|<10^{-6}$), the printed text corrected; `BREAK-C4.3-planted` additionally asserts that `only_at_corner` rejects the planted hits (max $|Z+1|=2.24$), so the leg can fail. Re-run (docstring also updated for #7): **30/30 PASS, 0.6 s, peak 86 MB**; `t=0: 1` hit, max $|Z+1|=2.1\times10^{-15}$.
- **#7, applied.** C0, *What R86's tag…* (first bullet), the table row of C4.3 sympy, the *Verification – run* text, the script docstring and the proposed R86 line: "identities sympy-exact, inequalities by hand".
- **R86 line, applied.** The two edits of the critic (identities/inequalities wording; the transport read from `relabel`/`section_FD`) and the new counts (30/30) are in the *Proposed R86 verification line*, plus the critic's review line; the corner clause for $\beta>\beta_{04}$ is carried there.

*Changed nodes.* C0: statement (corner value for $\beta>\beta_{04}$ only; "identities sympy-exact, inequalities by hand") and justification (C6 replaces 089 C2.3); C6: new; C4.3: wording of the check description only (its statement and justification unchanged); C1, C2, C3, C4.1, C4.2, C5: unchanged. *Dependents of C0:* it is the root; R86's every-point clause and the zero at $Z=\tfrac12$ restate it – both hold as written for $\beta>\beta_{04}$ and the first for $\beta=\beta_{04}$ in its non-vanishing form. No dependents of C4.3 beyond C0 and C5, both unchanged.

