# 064 — The cubic HS action at level (1,1), zero momentum: the $\Sigma$ block

Brief: `agent/briefs/active-computator-hs-level11-20261001T003500.md` (Task 17).
Script: `codes/verify-hs-level11.py` (logs `agent/scratch/hs-level11-run1.log`, `-run2.log`).

## Status

Fix pass 1 applied (2026-10-01, critic-064-20261001T014000, REVISE light: #1–#14; #10 is the orchestrator's, C5 drafted in the report). Script run 2: 67/67 PASS (seed 20261001), log `agent/scratch/hs-level11-run2.log` (run 1: 65/65). Next: narrow confirmation critic (orchestrator).

## Task and objective

**Literal task.** Write R1's cubic HS action on $\Psi=tT+dD$, $\Sigma=\sigma_1e_1+\sigma_2e_2+\sigma_3e_3$ at level (1,1), zero momentum, with numerical coefficients at $\beta\in\{\tfrac32,2\}$ (book normalisation); analyse the $\Sigma$ block $-\tfrac{g_s^2}{4!}V_4$ on $\mathrm{Sym}^2\{T,D\}$ (eigen-decomposition, signature, contour, fluctuation meaning); list the $V_5$ data an $S_3$ instance needs.

**Objective.** Objective 2 of the close-out and the paper's consistency-check section: the smallest concrete instance of the cubic theory, with numbers, in which the auxiliary field's quadratic form is indefinite; consumed by Task 14b (fluctuations around 059's critical points) and Task 15 (mean field).

## Conventions and assumptions

- **A1** Book normalisation (the project conventions, R43): sister → book $V_n\times\tfrac12$ (every $n$), $G_2\times\tfrac14$, $\operatorname{spec}(m_2)\times2$, signs unchanged. Identical to 059 A1.
- **A2** Action side: $V_n=-\{\cdot\}_{\rm pot}$ (companion package, potential side); zero-momentum potential $\mathcal V:=-S$ (059 A2). Path-integral weight $e^{S}$ (007 §4–§5, "real $e^S$ weight"): at momentum $k$, $\tfrac12V_2(T,T)t^2=-\tfrac{\alpha'}8(k^2+m_T^2)t^2$, damped for Euclidean $k^2\to\infty$, so $S=-S_E$. The relative sign of $V_4$ against $V_{2,3}$ (branch A) is R47's, whose caveat is that $\chi=-1$ is imported from the companion computation; it is the one sister input whose flip turns $\operatorname{In}(A)$ into $(1,2)$ (two rotated directions, the $TD$ direction convergent, a different 059 point), while the indefiniteness itself would survive.
- **A3** Five-field model of 057 §3 (C3.1): $\mathcal U=\mathrm{span}(T,D)$, $\mathcal S=\mathrm{Sym}^2\mathcal U$, **coordinate basis** $e_1=T\otimes T$, $e_2=\tfrac12(T\otimes D+D\otimes T)$, $e_3=D\otimes D$ (the sister's basis); $\sigma_i$ are coordinates in it; $A:=V_4\vert_{\mathcal S}$, $A_{ij}=h_{i+j-2}$, $h_k:=V_4(T^{4-k}D^k)$; $p:=(t^2,2td,d^2)$ the coordinates of $\Psi^{\otimes2}$.
- **A4** Data: the sister's declared section ($S=S_0$, $\Lambda_1$ at its declared value $\lambda_0$, mixed block on), whose region is the sister's $\mathcal V_{0,4}$ (`SL: R7`); zero momentum, tree level, R1's $O(g_s^2)$ action (no $V_5$). **Data caveat (as 059 A4):** sister R36 lists the $T^2D^2$ and odd-dilaton rows ($h_1,h_2,h_3$) as weight-scheme values; whether a later sister row fixes them (in particular $h_2=\{T^2D^2\}$, the entry $A_{22}$ that carries the $TD$ identification) in the declared section is not checked. $h_4$ is R36's closed form (contact part); the section dependence of $h_0,h_4$ is not reported.
- Hypotheses: none. R14 is Conditional(PH1), and PH1 is not inherited: at level (1,1) $A$ is explicitly invertible ((companion value, not reproduced here)) and only R14's finite-dimensional Feynman rules are used (quotient and level limit of PH1 are not entered).

## Claim tree

- **A1–A4** as above.
- Hypotheses: none.
- **C0** At level (1,1), zero momentum, $O(g_s^2)$, book normalisation, declared section: R1's action on $(t,d,\sigma)$ has the coefficients of Tables 1.1 and 2.1. Its $\sigma$-EOM gives $\sigma_*=(t^2,2td,d^2)$ in the basis $e_2=\tfrac12(TD+DT)$, and its joint critical point reproduces 059's $\tau,\delta>0$ points. $V_4\vert_{\mathcal S}$ has inertia $(2,1)$ at both $\beta$ (the action's block $-\tfrac{g^2}{24}V_4$ has $(1,2)$), with the single opposite-sign direction along the $TD$ pair. The $\Sigma$ Gaussian is defined by rotating that one combination to the imaginary axis, which changes only a field-independent phase. At zero momentum the block is a constant, algebraic (non-dynamical) direction of the quadratic form; whether $\Sigma$ has propagating modes (real zeros of $\det A(k)$) is not examined at level (1,1), while in $\Psi$ amplitudes at $O(g_s^2)$ the $\Sigma$ exchange telescopes to the contact $V_4$ (R14), so no $\Sigma$ pole appears there. The inertia holds for all real $(h_1,h_3)$ when $-\sqrt{h_0h_4}<h_2<0$ and is data-conditional on the weight-scheme $h_2$ (A4). [by C1–C5]
  - **C1** Table 1.1: $h_k=M_k/\pi$ (Hankel), $V_2(T,T)=1$, $V_2(T,D)=V_2(D,D)=0$, $V_3(T^3)=-\beta^6$, $V_3(TD^2)=\beta^2/2$, $V_3(T^2D)=V_3(D^3)=0$. [by C1.1, C1.2]
    - **C1.1** $A=V_4\vert_{\mathcal S}=M/\pi$ in the basis $(e_1,e_2,e_3)$, Hankel. [by A1, A2, R43; eq. (1.1); cited: the companion project's level-(1,1) data files] [check: C1.1-hankel-*, C1.1-anchor-T4-*, C1.1-anchor-T4-break-*, C1.1-anchor-T3D-*, C1.1-anchor-R36-*]
    - **C1.2** Quadratic and cubic entries. [by A1, A2, R43, R46; eq. (1.2)–(1.3); cited: the companion project's package notes] [check: C1.2-YZ-cubic, C1.2-YZ-cubic-break; C1.2-V2-* is a transcription print]
  - **C2** The action (2.1) with R1's normalisations, $\sigma_*=p$, and the joint critical point equal to 059's. [by C2.1, C2.2]
    - **C2.1** With R1's $\tfrac{2g^2}{4!}$ the saddle is $\sigma_*=p$ and (2.5) holds exactly. The brief's $\tfrac{g^2}{3!}$ would give $2p$ and $4\times$ the quartic. [by R1, A3; eq. (2.1)–(2.5)] [check: C2.1-sigma-star, C2.1-exact, C2.1-coefficient-break]
    - **C2.2** The five-variable critical point equals 059 Table 3.1 and 059 §4's $\sigma_*$ (to $4\times10^{-8}$, limited by 059's 7 digits). [by C1, C2.1; by check: C2.2-joint-*] [check: C2.2-joint-break-norm-*, C2.2-joint-break-coef-*]
  - **C3** The $\Sigma$ block. [by C3.1–C3.5]
    - **C3.1** $\mathrm{In}(A)=(2,1)$ at both $\beta$ (two routes), $\mathrm{In}(-\tfrac{g^2}{24}A)=(1,2)$; eigen-decomposition as in the §3 table (coordinate basis, not invariant). [eq. (3.1); by check: C3.1-signature-*] [check: C3.1-signature-break-potential-*, C3.1-signature-break-margin-*]
    - **C3.2** $\operatorname{spec}(G_2^{-1}A)=\tfrac4\pi\hat\lambda_{\rm sister}>0$. [by A1, C1.1; by check: C3.2-pencil-*] [check: C3.2-pencil-break-*]
    - **C3.3** For a positive $\operatorname{spec}(m_2)$, $\mathrm{In}(A)=\mathrm{In}(G_2)$, with the negative direction along $G_2$'s ($x_-\approx e_2$, equal to the sister's $x_2$). [eq. (3.2)–(3.3); by C3.2] [check: C3.3-congruence-*, C3.3-negative-pencil-vector-*, C3.3-congruence-break-*]
    - **C3.4** The opposite-sign combination is the $TD$ pair: eigenvector close to $e_2$; $A_{22}=h_2<0$; $A\vert_{\mathrm{span}(e_1,e_3)}>0$. [by C1.1; block: §3; by check: C3.4-negative-direction-*]
    - **C3.5** (2,1) holds for every real pair $(h_1,h_3)$ jointly whenever $-\sqrt{h_0h_4}<h_2<0$ ($A_{22}=h_2<0$ gives $n_-\ge1$, $A\vert_{\mathrm{span}(e_1,e_3)}>0$ gives $n_+\ge2$, neither involving $h_1,h_3$); the delivered $h_2$ lies at (companion value, not reproduced here) of the window edges. With $h_1,h_3$ fixed the inertia flips at $h_2=$ (companion value, not reproduced here) ($\beta=\tfrac32$) and $h_2=$ (companion value, not reproduced here) ($\beta=2$, where it becomes $(3,0)$); at $\beta=\tfrac32$ it survives any $h_2>$ (companion value, not reproduced here). The data caveat of A4 applies to $h_2$. One-at-a-time second route: $\det A$ has no real zero in $h_1$ (resp. $h_3$). [by C1.1, A4; block: §3 *Robustness*; by check: C3.5-robust-joint-h1-h3-*, C3.5-robust-h1-h3-*, C3.1-signature-break-margin-*] [check: C3.5-robust-break-h2-sign-* (can fail: with $h_2\to+\lvert h_2\rvert$ the discriminant of $\det A(h_1)$ is positive, real zeros appear, and a pair $(h_1,h_3)$ leaves $(2,1)$)]
  - **C4** Meaning of the indefinite block. [by C4.1, C4.2]
    - **C4.1** (a) Under 007's analytic-continuation prescription, the $\Sigma$ Gaussian is the integral over a contour with exactly one real combination imaginary: $\sigma_{TD}$, or the $A$-negative eigencombination. Rotating $\sigma_{TT}$ does not converge. The value is (4.4): a field-independent $\pm i$ phase times the tree-level HS exponent, and the moments give the propagator $\tfrac{12}{g^2}A^{-1}$ (R14 used through its finite-dimensional rules only: PH1 is not inherited, A4). [by R14, A2, C3.1, C3.4; eq. (4.1)–(4.5)] [check: C4.1-real-contour-divergent-*, C4.1-contour-TD-*, C4.1-contour-eig-*, C4.1-exponent-break-*, C4.1-contour-break-TT-*, C4.1-propagator-*]
    - **C4.2** (b) The $\sigma\sigma$ block of $\mathrm{Hess}\,\mathcal V_{\rm joint}$ is the constant $\tfrac{g^2}{12}A$, and $\mathrm{In}(\mathrm{Hess}\,\mathcal V_{\rm joint})=(2,1)+\mathrm{In}(\mathrm{Hess}\,\mathcal V_{\rm eff})$ on the $\sigma$-shell. At zero momentum it is an algebraic (non-dynamical) direction (algebraic $\sigma$ equation, contact $V_4$); propagation at $k\neq0$ is not examined, and in $\Psi$ amplitudes the $\Sigma$ exchange reduces to the contact $V_4$ at all $k$ (R14's telescoping). In $\mathrm{Hess}\,S$ (060 C1.7) the block contributes $\mathrm{In}(-A)=(1,2)$. [by R1, R14, C2.1, C3.1; eq. (4.6)–(4.7)] [check: C4.2-block-constant-*, C4.2-block-constant-break-*, C4.2-schur-*, C4.2-haynsworth-*]
  - **C5** The $S_3$ instance needs $w_k=V_5(T^{5-k}D^k)$, $k=0..5$, none available. With them, $W(\Psi)=t\,\mathrm{Hank}(w_{0..4})+d\,\mathrm{Hank}(w_{1..5})$, and the $\sigma$ equation is $(A-\tfrac g5W)\sigma=Ap$. [by R17, R61, A3; block: §5] (statement, no check)

Open gaps: none
Hypotheses in force: none

## 1. Coefficient table (C1)

\subsection*{Setup}
A1, A2, A4. Raw data files of the companion SL(2,C) project (level-(1,1) block $M:=V_4/C_4$ with its error bars, $G_2$, and the potential-side normalisation) and its package notes (BPZ pairing $g$, the potential-side cubic brackets $\{T^3\}_{\rm pot}$, $\{TD^2\}_{\rm pot}$, the book column); values from the companion SL(2,C) computation, not reproduced here.

\subsection*{Derivation}
$$
\begin{aligned}
V_4^{\rm book}&=\tfrac12\,V_4^{\rm sis,act}=\tfrac12\,(-C_4)\,M=\frac{M}{\pi},\qquad A=\frac M\pi,\quad h_k=A_{1,k+1}\ (k\le2),\ h_3=A_{23},\ h_4=A_{33}, &&(1.1)\\
V_2(T,T)&=L_0^+(T)\,g^{\rm book}(T,T)=(-2)(-\tfrac12)=1,\qquad V_2(T,D)=0\ (g(T,D)=0),\qquad V_2(D,D)=0\ (L_0^+D=0\text{ at }k=0), &&(1.2)\\
V_3(T^3)&=-\tfrac12\{T^3\}_{\rm pot}=-\beta^6,\qquad V_3(TD^2)=-\tfrac12\{TD^2\}_{\rm pot}=+\tfrac{\beta^2}2,\qquad V_3(T^2D)=V_3(D^3)=0. &&(1.3)
\end{aligned}
$$

**Table 1.1** (book, action side, declared section; $V_3(T^2D)=V_3(D^3)=V_2(T,D)=V_2(D,D)=0$ at both $\beta$):

| $\beta$ | $V_2(T,T)$ | $V_3(T^3)$ | $V_3(TD^2)$ | $h_0=V_4(T^4)$ | $h_1=V_4(T^3D)$ | $h_2=V_4(T^2D^2)$ | $h_3=V_4(TD^3)$ | $h_4=V_4(D^4)$ |
|---|---|---|---|---|---|---|---|---|
| 3/2 | 1 | −11.390625 | 1.125 | not reproduced | not reproduced | not reproduced | not reproduced | not reproduced |
| 2 | 1 | −64 | 2 | not reproduced | not reproduced | not reproduced | not reproduced | not reproduced |

The $h_k$ are values from the companion SL(2,C) computation, not reproduced here.

The $3\times3$ block on $\mathrm{Sym}^2\{T,D\}$ in the basis $(e_1,e_2,e_3)=(TT,\tfrac12(TD+DT),DD)$ is the Hankel matrix
$$
A=V_4\big\vert_{\mathcal S}=\begin{pmatrix}h_0&h_1&h_2\\h_1&h_2&h_3\\h_2&h_3&h_4\end{pmatrix}. \tag{1.4}
$$
Book pairing on the block: $G_2^{\rm book}=\tfrac14\operatorname{diag}(1,-1,4)$ (= $g\otimes g$ on $e_i$ with $g^{\rm book}=\operatorname{diag}(-\tfrac12,1)$). It does not enter the action (R1 uses $V_4$ as a bilinear form); it enters §3 only through $m_2=G_2^{-1}A$.

\subsection*{Commentary}
- (1.1): the file's block is potential side divided by $C_4=-2/\pi$; action side is $-\{\cdot\}_{\rm pot}$ (companion normalisation), book halves it. Entries $(1,3)$ and $(2,2)$ are the same coupling $\{T^2D^2\}$ (Hankel: $e_1\cdot e_3$ and $e_2\cdot e_2$ both carry $T^2D^2$; the $\tfrac12$ in $e_2$ is compensated by the two orderings).
- Anchors (independent of this record's arithmetic): $h_0=-\tfrac12\{T^4\}_{\rm pot}$ with the companion's calibration of $\{T^4\}_{\rm pot}$; $h_1=-\tfrac12\{T^3D\}_{\rm pot}$ with the companion's value of $\{T^3D\}_{\rm pot}$; and the closed form of $h_4$, the contact part of $\{D^4\}$ (companion R36; used in 059 C3.5); values from the companion SL(2,C) computation, not reproduced here.
- Numerical errors of the entries (divided by $\pi$) are far below every digit used here. Section dependence: only $\{T^3D\}$ has a sampled band (companion R44; not a bound).
- (1.3): as 059 (1.3); $\{T^2D\}=\{D^3\}=0$ by chiral ghost-number selection (R46, sister R17).

\subsection*{Verification}
`C1.1-hankel-*` (file block symmetric and Hankel), `C1.1-anchor-T4-*`, `C1.1-anchor-T3D-*`, `C1.1-anchor-R36-*` (these test the file against the package's calibration and $C_4$, not R43's factors; the break leg, $\times1$ instead of $\times\tfrac12$, only shows the code's two factors are consistent), `C1.2-V2`, `C1.2-YZ-cubic` ($\times2$ to YZ's normalisation at $\beta=3^{3/2}/4$ gives $-t^2+\tfrac{6561}{4096}t^3-\tfrac{27}{32}td^2$; break: $V_3(TD^2)$ sign flipped).

## 2. The action and the $\sigma$ equation (C2)

\subsection*{Setup}
A1–A4; Table 1.1. R1 verbatim (ledger row R1): $S_{\rm HS}=\tfrac12V_2(\Psi^2)+\tfrac{g}{3!}V_3(\Psi^3)-\tfrac{g^2}{4!}V_4(\Sigma,\Sigma)+\tfrac{2g^2}{4!}V_4(\Sigma,\Psi^{\otimes2})$, $g\equiv g_s$. $a:=V_3(T^3)$, $b:=V_3(TD^2)$.

**Coefficient of the mixed term.** The brief writes $\tfrac{g^2}{3!}V_4(\Sigma,\Psi,\Psi)$; R1 has $\tfrac{2g^2}{4!}=\tfrac{g^2}{12}$, half of it. R1 is used. With $\tfrac{g^2}{6}$ the saddle would be $\Sigma_*=2\Psi^{\otimes2}$ and the induced quartic $\tfrac{g^2}{6}V_4(\Psi^4)=4\times$ the target $\tfrac{g^2}{4!}V_4(\Psi^4)$ (check `C2.1-coefficient-break`). R1's value is the one fixed by the target, not a free constant.

\subsection*{Derivation}
With $\Psi^{\otimes2}=t^2e_1+2td\,e_2+d^2e_3$ (A3: $T\otimes D+D\otimes T=2e_2$), $V_4(\Sigma,\Sigma)=\sigma^\top A\sigma$, $V_4(\Sigma,\Psi^{\otimes2})=\sigma^\top Ap$, $V_3(\Psi^3)=at^3+3b\,td^2$:
$$
\begin{aligned}
S(t,d,\sigma)&=\tfrac12t^2+\tfrac g6\big(a\,t^3+3b\,td^2\big)-\tfrac{g^2}{24}\,\sigma^\top A\sigma+\tfrac{g^2}{12}\,\sigma^\top Ap, &&(2.1)\\
\sigma^\top A\sigma&=h_0\sigma_1^2+2h_1\sigma_1\sigma_2+h_2(2\sigma_1\sigma_3+\sigma_2^2)+2h_3\sigma_2\sigma_3+h_4\sigma_3^2, &&(2.2)\\
\sigma^\top Ap&=\sigma_1(h_0t^2+2h_1td+h_2d^2)+\sigma_2(h_1t^2+2h_2td+h_3d^2)+\sigma_3(h_2t^2+2h_3td+h_4d^2), &&(2.3)\\
\partial_\sigma S&=-\tfrac{g^2}{12}\,A(\sigma-p)=0\ \Longrightarrow\ \sigma_*=p=(t^2,\,2td,\,d^2)\quad(\det A\neq0), &&(2.4)\\
S(t,d,\sigma)&=S_{\rm eff}(t,d)-\tfrac{g^2}{24}(\sigma-p)^\top A(\sigma-p),\qquad S_{\rm eff}=\tfrac12t^2+\tfrac g6(at^3+3btd^2)+\tfrac{g^2}{24}\textstyle\sum_{k=0}^4\binom4kh_kt^{4-k}d^k. &&(2.5)
\end{aligned}
$$

**Table 2.1** Numerical action, $S=\tfrac12t^2+g\,[c_{t^3}t^3+c_{td^2}td^2]+g^2\,[\text{quadratic in }\sigma+\text{linear in }\sigma]$ (book; coefficients of the monomials, 10 digits in the script log):

| monomial | $\beta=\tfrac32$ | $\beta=2$ |
|---|---|---|
| $t^3$ | $-1.8984375\,g$ | $-10.66666667\,g$ |
| $td^2$ | $0.5625\,g$ | $1\,g$ |
| $\sigma_i\sigma_j$ and $\sigma_i\,(t^2,td,d^2)$ monomials | not reproduced | not reproduced |

The $\sigma$-dependent coefficients follow from (2.2)–(2.3) and the $h_k$ of Table 1.1; values from the companion SL(2,C) computation, not reproduced here.

In $(\tau,\delta,s)=(gt,gd,g^2\sigma)$, $g^2S$ is $g$-free (059 C2): all critical data scale exactly.

**Joint critical point.** $\nabla_{(t,d,\sigma)}S=0$ at $g=1$, solved by Newton on all five variables from 059's Table 3.1 point, returns (script `C2.2-joint-*`), at both $\beta$, the point $(\tau,\delta)$ with $\sigma_*=p(\tau_*,\delta_*)$ and the value $\mathcal V_*=-S_*$ of 059 Table 3.1 (numerical values not reproduced here: they follow from the companion SL(2,C) data).

\subsection*{Commentary}
- (2.4): $S$ is quadratic in $\sigma$ with constant coefficient $-\tfrac{g^2}{24}A$; the saddle needs only $\det A\neq0$ ((companion value, not reproduced here)). No positivity is used: $\sigma_*$ is a stationary point, not an extremum (§3–§4).
- (2.5): completion of the square inside $\mathcal S$ ($P=\Psi^{\otimes2}\in\mathcal S$, Veronese closure, 057 (3.1)); exact, no higher terms.
- The joint point is found with $\sigma$ free (not eliminated first), so the agreement with 059 tests (2.1) as written, including the factor $\tfrac2{4!}$ and the $\tfrac12$ in $e_2$. Break legs: the brief's $\tfrac{g^2}{3!}$, and $V_4$ in the sister normalisation ($\times1$ instead of $\times\tfrac12$) with book $V_2,V_3$, both move the point away from 059's (a wrong relative factor between $V_4$ and $V_{2,3}$ changes the physics, a common one only rescales $S$).

\subsection*{Verification}
`C2.1-sigma-star` (sympy `solve` of (2.4)), `C2.1-exact` ((2.5) as a polynomial identity; break `C2.1-coefficient-break`: the brief's coefficient fails it), `C2.2-joint-*` (5-variable Newton vs 059 Table 3.1 and 059 §4 $\sigma_*$ table to $10^{-6}$), `C2.2-joint-break-norm-*`, `C2.2-joint-break-coef-*`.

## 3. The $\Sigma$ block (C3)

\subsection*{Setup}
A1, A3; Table 1.1; $G_2^{\rm book}=\tfrac14\operatorname{diag}(1,-1,4)$ (§1). The $\Sigma$ block of the action is $-\tfrac{g^2}{24}A$ (in $S$); in $\mathcal V=-S$ it is $+\tfrac{g^2}{24}A$. Everything below is stated for $A$; the block of $S$ has the opposite inertia.

**What is basis-independent.** $A$ is a bilinear form, not an operator: its eigenvalues and orthonormal eigenvectors refer to the Euclidean metric of the coordinates $(\sigma_1,\sigma_2,\sigma_3)$ in the basis $(e_1,e_2,e_3)$ and change under a change of basis (e.g. $e_2\to(TD+DT)/\sqrt2$). Invariant are: the inertia (Sylvester), the cone $\{\sigma:\sigma^\top A\sigma<0\}$, and the spectrum of the pencil $(A,G_2)$, i.e. of $m_2=G_2^{-1}A$. All three are given.

\subsection*{Derivation}
*Coordinate-basis eigen-decomposition* (script log, `C3.1-signature-*`):

The eigenvalues of $A$ at both $\beta$ (one negative, two positive, the negative one with eigenvector close to $e_2$, the smaller positive one close to $e_3$, the larger one close to $e_1$) and the corresponding eigenvalues of the block of $S$ follow from the companion SL(2,C) data and are not reproduced here.

$$
\mathrm{In}(A)=(2,1,0),\qquad \mathrm{In}\big(-\tfrac{g^2}{24}A\big)=(1,2,0)\quad\text{at }\beta=\tfrac32,2. \tag{3.1}
$$
Second route (Jacobi): leading minors $(h_0,\ h_0h_2-h_1^2,\ \det A)$ with signs $(+,-,-)$ at both $\beta$ ((companion value, not reproduced here)): one sign change, one negative eigenvalue.

*Pencil and congruence.* Let $m_2x_i=\mu_ix_i$ with $x_i^\top G_2x_i=\epsilon_i=\pm1$. Since $G_2m_2=A$ is symmetric, $m_2$ is $G_2$-self-adjoint; for distinct real $\mu_i$ the $x_i$ are $G_2$-orthogonal, and
$$
X^\top AX=X^\top G_2X\,\operatorname{diag}(\mu)=\operatorname{diag}(\epsilon_i\mu_i). \tag{3.2}
$$
The data give $\mu_i$ at both $\beta$ all positive (values from the companion SL(2,C) computation, not reproduced here), equal to $\tfrac4\pi\times$ the companion's printed $\hat\lambda$ ($\operatorname{spec}(m_2)^{\rm book}=2\times$ companion action side $=2\cdot\tfrac2\pi\hat\lambda$). With all $\mu_i>0$, (3.2) gives $\mathrm{In}(A)=\mathrm{In}(\operatorname{diag}\epsilon)=\mathrm{In}(G_2)=(2,1)$:
$$
\operatorname{spec}(m_2)>0\ \ (\text{action side})\quad\Longrightarrow\quad \mathrm{In}(V_4\vert_{\mathcal S})=\mathrm{In}(G_2\vert_{\mathcal S}). \tag{3.3}
$$
The $G_2$-negative pencil vector $x_-$ is close to $e_2$ at both $\beta$, parallel to the companion's printed $x_2$, and $x_-^\top Ax_-=-\mu_-\cdot|x_-^\top G_2 x_-|<0$.

*The opposite-sign combination.* In every description it is the $TD$ pair: the coordinate eigenvector has overlap with $e_2$ close to 1; pencil vector $x_-\approx e_2$; and directly $A_{22}=V_4(e_2,e_2)=h_2=V_4(T^2D^2)<0$ while $A\vert_{\mathrm{span}(e_1,e_3)}=\begin{pmatrix}h_0&h_2\\h_2&h_4\end{pmatrix}$ is positive definite. The $TT$ and $DD$ pairs span a positive plane; the negative eigenvector is $e_2$ tilted by a few degrees, with comparable small admixtures of $e_1$ and $e_3$.

*Robustness* (`C3.5-*`, `C3.1-signature-break-margin-*`). A section change moves $h_1$ and $h_3$ together (both odd-dilaton rows, A4), so the statement needed is joint: $A_{22}=h_2<0$ gives $n_-\ge1$, and $A\vert_{\mathrm{span}(e_1,e_3)}=\begin{pmatrix}h_0&h_2\\h_2&h_4\end{pmatrix}>0$, which involves neither $h_1$ nor $h_3$, gives $n_+\ge2$. Hence $\mathrm{In}(A)=(2,1)$ for every real pair $(h_1,h_3)$ whenever $-\sqrt{h_0h_4}<h_2<0$ (the delivered $h_2$ at (companion value, not reproduced here) of the window edges), in particular across the sampled section band of $\{T^3D\}$ (companion R44), the only entry with a reported band. Second route, one entry at a time: $\det A$ is quadratic in $h_1$ (resp. $h_3$), with leading coefficient $-h_4<0$ and discriminant $4(h_2h_4-h_3^2)(h_0h_4-h_2^2)<0$, so it has no real zero and is negative. The $h_2$ margins, other entries fixed: $\det A$ is a cubic in $h_2$; at $\beta=\tfrac32$ its only real zero is $h_2\approx$ (companion value, not reproduced here), so $(2,1)$ holds for every $h_2$ above it; at $\beta=2$ the real zeros include (companion value, not reproduced here), and above it $A$ is positive definite, $(3,0)$. The $TD$ reading ($A_{22}<0$) needs $h_2<0$ at either $\beta$; $h_2$ is a weight-scheme value (A4).

\subsection*{Commentary}
- (3.1) corrects a reading of the brief: the $(2,1)$ in the context document (§3, "signature $(2,1)$") is the signature of $G_2$, not of $V_4$. $V_4\vert_{\mathcal S}$ also has $(2,1)$ — from the data (059 §1 already, here by two routes) — and the block as it stands in $S$, $-\tfrac{g^2}{24}A$, has $(1,2)$.
- (3.3) explains the coincidence and turns it into a consistency relation between two companion outputs: the companion's verdict that $\hat\lambda$ is positive is equivalent, given diagonalisability with real spectrum, to $V_4$ inheriting $G_2$'s inertia with its negative direction along $G_2$'s ($e_2$, where $g(T,T)g(D,D)<0$). The indefiniteness of the $\Sigma$ form is therefore the indefiniteness of the BPZ pairing on $\mathrm{Sym}^2$, carried through a positive $m_2$; given the positive spectrum of $m_2$ (a property of the level-(1,1) data, recomputed here and not derived structurally: it flips with the relative sign of $C_4$, R47, and R53's structural positivity is level-0 and conditional, PH1 scope) the negative direction is $G_2$'s, along $e_2$ where $g(T,T)g(D,D)<0$.
- *Beyond level (1,1).* This extension is expected and has not been checked, and it assumes $\Sigma$ ranges over the full $\mathrm{Sym}^2$, not the quotient by $\ker V_4$ (R9). If $\operatorname{spec}(m_2)>0$ persisted at higher level, (3.3) would give $n_-(V_4\vert_{\mathcal S})=n_-(G_2\vert_{\mathcal S})$. For a $g$-orthogonal basis with $n_\pm$ states of either norm sign, $G_2=g\otimes g$ on $\mathrm{Sym}^2$ is negative exactly on the $n_+n_-$ products of one positive-norm and one negative-norm state. Here $n_+=n_-=1$, which gives $1$. The number of rotated directions in §4 would then grow with the level, as for the conformal factor of the metric (Gibbons, Hawking, Perry 1978, Nucl. Phys. B138, 141).
- *Limit $d=0$.* In the one-field model $(t,\sigma_1)$ the $\Sigma$ block is $h_0>0$, definite, and needs no rotation, consistent at $k=0$ with R53's level-0 definiteness (conditional on PH25, PH29, PH30). The indefinite direction enters with the dilaton. The $\beta$ dependence is tested at two points only; $\beta\to\beta_{04}$, where $\lvert\det A\rvert^{-1/2}$ in (4.4) would be the quantity to watch, is not examined.
- The $(2,1)$ is not fragile: it survives arbitrary changes of $\{T^3D\}$ and $\{TD^3\}$ and needs order-one changes of $h_0,h_2,h_4$ to flip. Only $\{T^3D\}$ has a sampled section band; the section dependence of $h_0,h_4$ is not reported, and $h_2$ (and $h_1,h_3$) are weight-scheme values (A4, data caveat); the margins above are what a band on them would have to exceed.

\subsection*{Verification}
`C3.1-signature-*` (eigenvalues and Jacobi minors; breaks: $A\to-A$ gives $(1,2)$ by both routes; past the nearest margin the inertia changes by both routes), `C3.2-pencil-*` ($\tfrac4\pi\hat\lambda$ to $10^{-9}$; break: $G_2$ without $\tfrac14$), `C3.3-congruence-*` ((3.2) to $10^{-16}$ off-diagonal; break: $-A$ has all-negative pencil spectrum and $\mathrm{In}\ne\mathrm{In}(G_2)$), `C3.3-negative-pencil-vector-*` (cosine with the sister's $x_2$ equal to 1 to $10^{-12}$), `C3.4-negative-direction-*`, `C3.5-robust-joint-h1-h3-*` (403 seeded real pairs, window on $h_2$), `C3.5-robust-h1-h3-*` (one entry at a time), `C3.5-robust-break-h2-sign-*` (break that can fail: $h_2\to+\lvert h_2\rvert$ gives real zeros of $\det A(h_1)$ and a pair $(h_1,h_3)$ leaving $(2,1)$; the previous break on the $h_2$ cubic could not fail, since a real cubic always has a real root). The pencil comparison tests the file against the sister's separate QZ result; the factors $\tfrac14$, $\tfrac12$ are R43's (cited), and the $\tfrac4\pi$ is derived from them, so the break without $\tfrac14$ only checks the code's factors.

## 4. Meaning of the indefinite block (C4)

\subsection*{Setup}
A2 (weight $e^{S}$), A3; §2–§3. R1 states no contour. The project's prescription is record 007 §4 (R14's determinant clause, written after critic-a1 Issue 5): the $\Sigma$ integral is a *formal Gaussian defined by analytic continuation*, $M$ being indefinite, with a field-independent determinant factor. At fixed $\Psi$ the $\Sigma$ part of the weight is
$$
e^{S_\Sigma},\qquad S_\Sigma=-\tfrac12\sigma^\top Q\sigma+b^\top\sigma,\qquad Q:=\tfrac{g^2}{12}A,\quad b:=\tfrac{g^2}{12}Ap. \tag{4.1}
$$
Let $A=\sum_i\lambda_iu_iu_i^\top$ (§3 table), $\lambda_-<0<\lambda_2<\lambda_3$, $\sigma=\sum_i\eta_iu_i$.

\subsection*{Derivation}
*(a) Contour.* On the real contour, along $\eta_-$: $S_\Sigma\supset+\tfrac{g^2}{24}\lvert\lambda_-\rvert\eta_-^2$, so $\int_{\mathbb R^3}e^{S_\Sigma}$ diverges. The prescription continues from a positive form: take $Q_\theta:=\tfrac{g^2}{12}\big(\sum_{i\neq-}\lambda_iu_iu_i^\top+e^{i\theta}\lvert\lambda_-\rvert u_-u_-^\top\big)$, positive at $\theta=0$, equal to $Q$ at $\theta=\pm\pi$, and let the $\eta_-$ contour follow, $\eta_-=e^{-i\theta/2}y$, $y\in\mathbb R$. Then $e^{i\theta}\lvert\lambda_-\rvert\eta_-^2=\lvert\lambda_-\rvert y^2$ for every $\theta$, the integral converges along the whole path, is analytic in $\theta$, and equals the $\theta=0$ formula continued:
$$
\begin{aligned}
\int d\eta_-\,e^{-\frac12\frac{g^2}{12}e^{i\theta}\lvert\lambda_-\rvert\eta_-^2+\beta_-\eta_-}
&=e^{-i\theta/2}\sqrt{\tfrac{24\pi}{g^2\lvert\lambda_-\rvert}}\;\exp\Big(\tfrac{6\,\beta_-^2}{g^2e^{i\theta}\lvert\lambda_-\rvert}\Big), &&(4.2)\\
\theta\to\pm\pi:\quad \eta_-&\in\mp i\,\mathbb R,\qquad \text{value}=\mp i\sqrt{\tfrac{24\pi}{g^2\lvert\lambda_-\rvert}}\;\exp\Big(\tfrac{6\,\beta_-^2}{g^2\lambda_-}\Big). &&(4.3)
\end{aligned}
$$
The continuation lands on the contour with the $A$-negative combination imaginary and the other two real; the two directions of continuation differ by the orientation of that axis, i.e. by the sign of the prefactor. Assembling the three directions,
$$
\int_\Gamma d^3\sigma\,e^{S_\Sigma}=\pm i\Big(\frac{24\pi}{g^2}\Big)^{3/2}\lvert\det A\rvert^{-1/2}\,\exp\Big(\frac{g^2}{24}\,p^\top Ap\Big)=\pm i\Big(\frac{24\pi}{g^2}\Big)^{3/2}\lvert\det A\rvert^{-1/2}\,e^{\frac{g^2}{4!}V_4(\Psi^4)}, \tag{4.4}
$$
since $\tfrac12b^\top Q^{-1}b=\tfrac{g^2}{24}p^\top Ap$ is rational in $Q$ and single-valued.

*Which contours are admissible.* For $\Gamma=\{x+iy:\ x\in V_+,\ y\in V_-\}$ with $\mathbb R^3=V_+\oplus V_-$: $\operatorname{Re}\,\sigma^\top Q\sigma=x^\top Qx-y^\top Qy$ (the cross term is imaginary), so $\Gamma$ converges iff $A\vert_{V_+}>0$ and $A\vert_{V_-}<0$; hence $\dim V_-=n_-(A)=1$. For any admissible $\Gamma=C\mathbb R^3$, $\det C\cdot\det(C^\top QC)^{-1/2}=\pm\det Q^{-1/2}$ and $(C^\top QC)^{-1}C^\top b=C^{-1}p$, so (4.4) holds for every admissible $\Gamma$, up to the orientation sign. Two choices:
$$
\Gamma_{TD}:\ \sigma_1,\sigma_3\in\mathbb R,\ \ \sigma_2\in i\mathbb R;\qquad \Gamma_{\rm eig}:\ \eta_-\in i\mathbb R,\ \eta_{2,3}\in\mathbb R. \tag{4.5}
$$
$\Gamma_{TD}$ is admissible because $A_{22}=h_2<0$ and $A\vert_{\mathrm{span}(e_1,e_3)}>0$ (§3). Rotating $\sigma_{TT}$ instead is not ($\operatorname{Re}Q$ indefinite). Since $b$ is real and the integrand entire, the imaginary axis can be translated through the real saddle: $\sigma_2=2td+iy$. The fluctuation of the $TD$ coordinate about its saddle is imaginary, those of $TT$ and $DD$ real.

Moments on an admissible contour are the continued Gaussian moments, $\langle\delta\sigma\,\delta\sigma^\top\rangle_\Gamma=Q^{-1}=\tfrac{12}{g^2}A^{-1}$ (numerically on $\Gamma_{TD}$): the $\Sigma$ propagator of R14's Feynman rules, $(12/g_s^2)(V_4\vert_{\rm Sym^2})^{-1}$, is unchanged by the rotation.

*(b) Fluctuation problem.* With $\mathcal V_{\rm joint}:=-S$ and $x=(t,d)$:
$$
\mathrm{Hess}\,\mathcal V_{\rm joint}=\begin{pmatrix}H_{xx}(x,\sigma)&-\tfrac{g^2}{12}J^\top A\\-\tfrac{g^2}{12}AJ&\tfrac{g^2}{12}A\end{pmatrix},\qquad J:=\partial p/\partial x, \tag{4.6}
$$
the $\sigma\sigma$ block constant. On the $\sigma$-shell $\sigma=p(x)$ its Schur complement is the Hessian of $\mathcal V_{\rm eff}=-S_{\rm eff}$ (envelope identity), and Haynsworth's inertia additivity (Haynsworth 1968, Linear Algebra Appl. 1, 73) gives
$$
\mathrm{In}(\mathrm{Hess}\,\mathcal V_{\rm joint})=\mathrm{In}(A)+\mathrm{In}(\mathrm{Hess}\,\mathcal V_{\rm eff})=(2,1,0)+\mathrm{In}(\mathrm{Hess}\,\mathcal V_{\rm eff}) \tag{4.7}
$$
at every $x$. *Sign convention.* (4.7) is for $\mathrm{Hess}(-S)$, with $\mathcal V_{\rm eff}=-S_{\rm eff}$, and the count "subtract $n_-(A)=1$" holds for $\mathrm{Hess}(-S)$ only. Record 060 C1.7 writes the same identity for $\mathrm{Hess}\,S$ and calls the effective action $V_{\rm eff}$; there the block contributes $\mathrm{In}(-A)=(1,2)$, i.e. two negative directions. Task 14b must fix one side (proposed C5 in the report). At 059's $\tau,\delta>0$ points: $(3,2)=(2,1)+(1,1)$.

\subsection*{Commentary}
- (4.2)–(4.3): the continuation acts on one real direction only because $n_-(A)=1$. Its sign ($\theta\to+\pi$ or $-\pi$) is not fixed by 007's prescription and is irrelevant: it multiplies $Z$ by a field-independent $\pm i$, which cancels in every normalised correlator $Z[J]/Z[0]$ (007 §4 item 1).
- (4.4) is the HS identity with an indefinite kernel: the exponent is exactly the quartic term of the original action, contour-independent. The classical content of R1 and the tree-level telescoping R14 do not see the indefiniteness. The Gaussian over $\Psi$ at zero momentum is itself not convergent (tachyon, and the dilaton's wrong-sign kinetic term); that is a separate issue, not addressed here. The $\Sigma$ integral is done first, at fixed $\Psi$.
- (4.7): the $\Sigma$ block adds exactly one negative direction to the joint Hessian of $\mathcal V$, at every background, the perturbative vacuum included. It carries no information about the $\Psi$ critical point. It is the same direction whose Gaussian (a) rotates, so it is the auxiliary analogue of the conformal-factor rotation, not an instability. For Task 14b: count negative modes on the Schur complement $\mathrm{Hess}\,\mathcal V_{\rm eff}$, and subtract $n_-(A)=1$ from any joint count.
- *Ghost-like, algebraic at zero momentum.* At zero momentum the block is a constant, algebraic (non-dynamical) direction of the quadratic form: the $\sigma$ equation (2.4) has no derivative and no $L_0$, $V_4$ is a contact vertex, and the "propagator" is the constant $\tfrac{12}{g^2}A^{-1}$. "Propagating" discriminates nothing at $k=0$. The all-$k$ argument is R14's telescoping: in $\Psi$ amplitudes at $O(g_s^2)$ the $\Sigma$ exchange reduces to the contact $V_4$, so no $\Sigma$ pole appears there. Whether $\Sigma$ has propagating modes is not examined. At $k\neq0$ the block is $A(k)$, with entries entire in $k^2$. A pole of the $\Sigma$ propagator would need $\det A(k)=0$. That is not examined at level (1,1): R53 excludes real zeros at level 0 only, and the $k$-dependence of the $D$ legs mixes with the graviton trace (059 C3.6).

\subsection*{Verification}
`C4.1-real-contour-divergent-*` ($\operatorname{Re}Q$ has one negative eigenvalue), `C4.1-contour-TD-*`, `C4.1-contour-eig-*`: tensor Gauss–Hermite quadrature on $\Gamma$ (48 nodes per axis, agreement with 40 nodes to $10^{-9}$, an exact real translation, no closed form used), divided by $e^{\frac{g^2}{24}p^\top Ap}$, at three seeded $\Psi$. The ratio is $\Psi$-independent to $4\times10^{-15}$, purely imaginary, and has modulus $(24\pi/g^2)^{3/2}\lvert\det A\rvert^{-1/2}$ at both $\beta$ ($g=1$). Breaks: the exponent $\tfrac{g^2}{12}$ makes the ratio $\Psi$-dependent (`C4.1-exponent-break-*`), and rotating $\sigma_{TT}$ gives an indefinite $\operatorname{Re}Q$ (`C4.1-contour-break-TT-*`). `C4.1-propagator-*`: second moment on $\Gamma_{TD}$ $=\tfrac{12}{g^2}A^{-1}$ to $10^{-14}$ (weak break: the entrywise absolute value fails). `C4.2-block-constant-*`: break with a $V_5(\Sigma,\Sigma,\Psi)$-type term through the same Hessian code. `C4.2-schur-*`: break with an off-shell $\sigma$. `C4.2-haynsworth-*`.

## 5. Quintic order (C5)

No computation here, only statements.

**Data the $S_3$ instance needs.** R17's $\tfrac{g^3}{5!}V_5(\Sigma,\Sigma,\Psi)$ restricted to $\Sigma\in\mathcal S$ and $\Psi=tT+dD$ needs the six zero-momentum couplings
$$
w_k:=V_5(T^{5-k}D^k),\qquad k=0,\dots,5,
$$
in the sister's declared section, extended consistently to $\mathcal V_{0,5}$, in the book normalisation. By total symmetry, $V_5(e_i,e_j,\Psi)=t\,w_{i+j-2}+d\,w_{i+j-1}$, i.e. $W(\Psi)=t\,\mathrm{Hank}(w_0,\dots,w_4)+d\,\mathrm{Hank}(w_1,\dots,w_5)$. None of the six is available in the literature or in the companion project (no $V_5$ coupling is available). No selection rule is known to set any of them to zero. The chiral rule that kills $\{T^2D\},\{D^3\}$ is a cubic-vertex statement, and it already fails at quartic order ($\{T^3D\},\{TD^3\}\neq0$, companion R44).

**What can be said without them.** The $\sigma$ equation becomes $\big(A-\tfrac g5W(\Psi)\big)\sigma=Ap$ (057 (3.2), R61). The $\Sigma$ block of the Hessian becomes the field-dependent $-\tfrac{g^2}{12}K_{\mathcal S}(\Psi)$, $K_{\mathcal S}=A-\tfrac g5W(\Psi)$. The inertia of $-\tfrac{g^2}{12}K_{\mathcal S}$ stays $(1,2)$, i.e. that of $K_{\mathcal S}$ stays $(2,1)$, on the connected component of $\{\det K_{\mathcal S}\neq0\}$ containing $\Psi=0$; the boundary is $\det K_{\mathcal S}(\Psi)=0$, a cubic curve in the $(\tau,\delta)$ plane on which $\sigma_*$ has its pole (R61). Only there can the auxiliary form register a background, and only through the unknown $w_k$.

**For Task 15 (mean field).** At $O(g_s^2)$ the $\Sigma$ saddle is real ($\sigma_*=p$), the admissible contour of §4 passes through it, and the $\Sigma$ fluctuation determinant is field-independent: there is no $\Sigma$-loop correction to $\mathcal V_{\rm eff}$ at this order. From $S_3$ on, $K_{\mathcal S}(\Psi)$ is field-dependent, so is $\det K_{\mathcal S}^{-1/2}$, and its phase can jump across $\det K_{\mathcal S}=0$.

## Result

**Action** (book, zero momentum, level (1,1), declared section, $O(g_s^2)$; A1–A4):
$$
\boxed{S=\tfrac12t^2+\tfrac{g}{6}\big(V_3(T^3)\,t^3+3V_3(TD^2)\,td^2\big)-\tfrac{g^2}{24}\,\sigma^\top A\sigma+\tfrac{g^2}{12}\,\sigma^\top A\,(t^2,2td,d^2)^\top}
$$
with $V_3(T^3)=-\beta^6$, $V_3(TD^2)=\beta^2/2$, and $A$ the Hankel block of Table 1.1; numerical monomials in Table 2.1. Basis: $e_2=\tfrac12(TD+DT)$ (coordinates), so $\sigma_*=(t^2,2td,d^2)$. The joint critical point reproduces 059's $\tau,\delta>0$ points.

**$\Sigma$ block.** $A=V_4\vert_{\mathcal S}$ has inertia $(2,1)$ at $\beta=\tfrac32,2$. The block in the action, $-\tfrac{g^2}{24}A$, has $(1,2)$. The opposite-sign combination is the $TD$ pair: eigenvector $\approx e_2$, $A_{22}=h_2<0$, and $A$ is positive on $\mathrm{span}(TT,DD)$. Given the positive spectrum of $m_2$ (a property of the level-(1,1) data, not derived here), (3.3) gives $G_2$'s inertia. It holds for every real pair $(\{T^3D\},\{TD^3\})$ jointly whenever $-\sqrt{h_0h_4}<V_4(T^2D^2)<0$; $V_4(T^2D^2)$ is a weight-scheme value (A4), at (companion value, not reproduced here) of the bound. With $h_1,h_3$ fixed the inertia flips at $h_2=$ (companion value, not reproduced here) ($\beta=\tfrac32$) and $h_2=$ (companion value, not reproduced here) ($\beta=2$, to $(3,0)$).

**Meaning.** (a) The $\Sigma$ Gaussian is defined by rotating exactly one real combination to the imaginary axis: $\sigma_{TD}$ itself, with $\sigma_{TT},\sigma_{DD}$ real, or the $A$-negative eigen-combination. The result is $\pm i(24\pi/g^2)^{3/2}\lvert\det A\rvert^{-1/2}e^{\frac{g^2}{4!}V_4(\Psi^4)}$. Only the field-independent phase depends on the choice, and the propagator stays $\tfrac{12}{g^2}A^{-1}$. (b) In the fluctuation problem the block is constant and adds exactly one negative direction to the joint Hessian of $\mathcal V$ at every background. At zero momentum this is a constant, algebraic (non-dynamical) direction of the quadratic form. Whether $\Sigma$ has propagating modes (real zeros of $\det A(k)$) is not examined at level (1,1); in $\Psi$ amplitudes at $O(g_s^2)$ the $\Sigma$ exchange telescopes to the contact $V_4$ (R14), so no $\Sigma$ pole appears there. Negative-mode counts for Task 14b belong to the Schur complement $\mathrm{Hess}\,\mathcal V_{\rm eff}$; in $\mathrm{Hess}\,S$ (060 C1.7) the block contributes $\mathrm{In}(-A)=(1,2)$.

**Quintic.** Needs $w_k=V_5(T^{5-k}D^k)$, $k=0..5$ (none available).

**Proposed ledger row.** "Cubic HS action at level (1,1), zero momentum (record 064; book normalisation R43, relative sign of $V_4$ per R47; SL(2,C) declared section `SL: R7` with the sister's delivered $V_4$ block; $O(g_s^2)$; five-field truncation). R1's action on $\Psi=tT+dD$, $\Sigma\in\mathrm{Sym}^2\{T,D\}$ (coordinate basis $e_2=\tfrac12(TD+DT)$) has the coefficients of 064 Tables 1.1 and 2.1. Its joint critical point reproduces record 059's $\tau,\delta>0$ points, with $\sigma_*=(t^2,2td,d^2)$. $A=V_4\vert_{\mathrm{Sym}^2}$ has inertia $(2,1)$ at $\beta=\tfrac32,2$; the block of the action, $-\tfrac{g_s^2}{4!}A$, has $(1,2)$. The opposite-sign direction is the $TD$ pair (eigenvector close to $e_2$; $A_{22}=V_4(T^2D^2)<0$; $A>0$ on $\mathrm{span}(TT,DD)$). Given the positive spectrum of $m_2=G_2^{-1}A$ (a property of the level-(1,1) data), the inertia is that of $G_2$ (congruence). It holds for all real values of $\{T^3D\}$, $\{TD^3\}$ jointly whenever $-\sqrt{h_0h_4}<V_4(T^2D^2)<0$; with $h_1,h_3$ fixed it flips at $h_2=$ (companion value, not reproduced here) ($\beta=\tfrac32$) and $h_2=$ (companion value, not reproduced here) ($\beta=2$, to $(3,0)$). The delivered $V_4(T^2D^2)$, a weight-scheme value per sister R36 (as are the odd-dilaton rows), lies at (companion value, not reproduced here) of that bound. With the weight $e^{S}$ ($S=-S_E$), the $\Sigma$ Gaussian (007's analytic continuation) is the integral over a contour with exactly one real direction imaginary: the $TD$ coordinate, or the $A$-negative eigencombination. It equals $\pm i(24\pi/g_s^2)^{3/2}\lvert\det A\rvert^{-1/2}e^{\frac{g_s^2}{4!}V_4(\Psi^4)}$; only the field-independent phase depends on the contour, and the propagator stays $\tfrac{12}{g_s^2}A^{-1}$. At zero momentum the block adds one constant negative direction to $\mathrm{Hess}(-S)$ (Haynsworth 1968; two to $\mathrm{Hess}\,S$, the convention of 060 C1.7, where the block contributes $\mathrm{In}(-A)=(1,2)$), a constant, algebraic (non-dynamical) direction of the quadratic form; negative-mode counts belong to the Schur complement $\mathrm{Hess}\,\mathcal V_{\rm eff}$ ($\mathcal V_{\rm eff}=-S_{\rm eff}$). Whether $\Sigma$ has propagating modes (zeros of $\det A(k)$) is not examined at level (1,1); in $\Psi$ amplitudes at $O(g_s^2)$ the $\Sigma$ exchange telescopes to the contact $V_4$ (R14), so no $\Sigma$ pole appears there." Status: **Verified** (67/67 PASS, seed 20261001), no PH (R14's PH1 is not inherited: $A$ is invertible at this truncation and only R14's finite-dimensional rules are used). Scope: zero momentum, level (1,1), $\beta\in\{\tfrac32,2\}$, declared section, quartic vertex order. Sister numbers not verified; $h_2$ weight-scheme caveat as stated; relative sign of $V_4$ per R47 (its $\chi=-1$ import from `SL: R37`; a flip gives $(1,2)$ for $A$).

## Verification

`codes/verify-hs-level11.py`, run 2 (`OMP_NUM_THREADS=1`), log `agent/scratch/hs-level11-run2.log`: **67 PASS / 0 FAIL**, seed 20261001, exit 0 (run 1, before the fix pass: 65/65; the two vacuous `C3.5-robust-break-h2-*` legs replaced by `C3.5-robust-break-h2-sign-*`, two `C3.5-robust-joint-h1-h3-*` added). ruff is not installed in the project venv, so no ruff run in this pass (run 1: clean). Of the 67, 24 are named break legs, all failing as they must. Two more break legs sit inside `C4.2-schur-*` (off-shell $\sigma$) and `C4.1-propagator-*` (weak: entrywise absolute value). `C1.2-V2-*` is a transcription print that cannot fail meaningfully. `C1.1-hankel-*` checks the file's structure, not physics.

Independent anchors, as opposed to re-evaluations of the same data:
- the companion's calibration of $\{T^4\}$ (three-route value);
- the companion's $\{T^3D\}$;
- the closed form of $h_4$ (companion R36);
- YZ's cubic couplings at $\beta=3^{3/2}/4$;
- the companion's printed pencil spectrum and eigenvector (a separate QZ computation);
- record 059's critical points, obtained there by eliminating $\sigma$ first, whereas here all five variables are solved jointly;
- quadrature of the $\Sigma$ Gaussian with no closed form used.

The conversion factors are R43's (cited, not tested here): the anchors test the file against the package and $C_4$, and the pencil comparison tests the file against the sister's separate QZ result, with the $\tfrac4\pi$ derived from the same factors. The breaks ($V_4\times1$, $G_2$ without $\tfrac14$) only show that the code's factors are consistent; the joint-point breaks test consistency with 059, which used the same R43. For the physics claims the factor $\tfrac12$ is inert: it is common to all $V_n$, rescales $S$, and moves only the tabulated coefficients and the Gaussian normalisation; the inertia is invariant under a positive rescaling of $A$. R1's coefficient is tested by breaks: $\tfrac{g^2}{3!}$ fails the square completion and moves the point.

Not verified: the sister numbers themselves, and R47's relative sign of $V_4$ (imported with its `SL: R37` caveat; a flip turns $\mathrm{In}(A)$ into $(1,2)$); the momentum dependence of the block ($A(k)$, possible zeros of $\det A(k)$); the section dependence of $h_0,h_2,h_3,h_4$ (not reported by the sister; $h_1,h_2,h_3$ are weight-scheme values, A4); the claim that every admissible contour is homotopic to the two tested (argued algebraically in §4, tested on $\Gamma_{TD}$ and $\Gamma_{\rm eig}$); anything involving $V_5$ (§5 is a statement only).
