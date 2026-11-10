# 028 — Reality of the whole auxiliary tower ($\Sigma_k$, $\chi$, Route C multipliers $\lambda_k$)

**Date:** 2026-09-14 (Fable, computator; brief
`agent/briefs/active-computator-9a-reality-tower-20260914T045500.md`, Task 9a).
**Machine check:** `codes/verify-reality-tower.py` (finite-dim toy; see §Verification).
**Inputs (read by line range only):** note §reality (pedagogical, ll. 1157–1216); 017 (all);
019 §1, §4; 024 §2.3; ledger rows R12, R13, R24, R26.
**Scope:** algebraic layer (finite-dimensional $\mathcal H_0$, generic symmetric tensors
$V_n$, formal power series in $g$); the CFT reality of $V_n$ is a *hypothesis* inherited from
the note (Sonoda–Zwiebach H5), stated once in §1 and not re-derived.

## Task and objective

**Literal task.** The note proves the $\Sigma$ kinetic term $V_4(\Sigma,\Sigma)$ real at
$O(g_s^2)$ with $\Sigma^\ddagger=\Sigma$. Extend to (a) all kinetic terms
$V_{2k}(\Sigma_k,\Sigma_k)$ and (a′) all sources $V_{a+b+c}(\Sigma_a,\Sigma_b,\Sigma_c)$ of the
tower, including the reality of the on-shell values $\Sigma_k^*(\Psi)$ (019's fixed point);
(b) the $\chi$ partner of R24; (c) the Route C multipliers $\lambda_k$ of R13.

**Objective.** The paper states a real action at all orders. Each auxiliary field needs its
reality condition and each term a reality proof (or the named obstruction). Close R13's
"reality unassigned" and R24's "$\chi^\ddagger=\chi$ expected, unproven".

## 0. Verdict table

| Item | Condition | Verdict | Where |
|---|---|---|---|
| (a) tower kinetic terms $V_{2k}(\Sigma_k,\Sigma_k)$, $\tilde M_k$, $\hat M_k$ | $\Sigma_k^\ddagger=\Sigma_k$ | **real** to all orders, given (H$_R$) and real coefficients | §2, Steps 2.1–2.2 |
| (a′) tower sources $V_{a+b+c}(\Sigma_a,\Sigma_b,\Sigma_c)$, $L_k$; on-shell $\Sigma_k^*(\Psi)$ | $\Sigma_k^\ddagger=\Sigma_k$ (forced by the sources up to the source-kernel directions $\bigcap_k(\operatorname{im}L_k)^\perp$, Step 2.4; generic parents span the dual, the CFT $V_n$ need not) | **real**; fixed point preserves reality (Lemma 2, incl. $\ker V_{2k}$ quotient) | §2, Steps 2.3–2.4 |
| (b) $\chi$ | $\chi^\ddagger=\chi$ — **forced** by the linear coupling with real $b_\chi$; R24 flag closed | **real**; wrong kinetic sign is a *consequence* of reality + $b^2/a=4$ | §3 |
| (c) $\lambda_k$ | $\lambda_k^\ddagger=\lambda_k$ (componentwise $\ddagger$; $(-1)^{k(k-1)/2}$ in the reversed-order convention); R13 flag closed | **real** $S_C$ to all orders, given the two §4.3 inputs (Grassmann-odd conjugation rule, $\ddagger^2=1$ on odd states), stated and not checked | §4 |

All verdicts are conditional on (H$_R$), eq. (1.1): the $\ddagger$-equivariance of every $V_n$,
which follows from Sonoda–Zwiebach H5 plus conjugation invariance of the moduli regions and
measures — the two inputs under which the nonpolynomial action itself is real.

## 1. Convention

Inherited verbatim from the note (§reality, ll. 1157–1216) and used once here.

**(C1) The conjugation.** $\ddagger=\mathrm{BPZ}\circ(\text{hermitian conjugation})$ is an
antilinear involution of $\mathcal H_0$ preserving the ghost grading:
$(aA+bB)^\ddagger=a^*A^\ddagger+b^*B^\ddagger$, $(A^\ddagger)^\ddagger=A$. A state is
*$\ddagger$-real* if $A^\ddagger=A$; every $A$ splits uniquely as $A=A_r+iA_i$ with
$A_r=\tfrac12(A+A^\ddagger)$, $A_i=\tfrac1{2i}(A-A^\ddagger)$ both $\ddagger$-real. The closed
string field satisfies $\Psi^\ddagger=\Psi$ ($N_{\rm gh}=2$, Grassmann-even).

**(C2) Extension to $\mathcal H_0^{\otimes k}$.** Componentwise and antilinearly,
$(A_1\otimes\cdots\otimes A_k)^\ddagger:=A_1^\ddagger\otimes\cdots\otimes A_k^\ddagger$, *without*
a reordering sign. For the tower this is unambiguous: every strand of $\Sigma_k$ has
$N_{\rm gh}=2$ (even), so the alternative "reversed-order" hermitian conjugation gives the same
map. The two conventions differ by $(-1)^{k(k-1)/2}$ on tensors all of whose strands are
Grassmann-odd — this is exactly the case of $\lambda_k$ (three units of ghost number per
strand, 024 §2.3) and is tracked in §4. $\mathrm{Sym}^k\mathcal H_0$ is $\ddagger$-stable, and so
is the quotient by $\ker V_{2k}$ once $V_{2k}$ is real (Lemma 2 below). $\ddagger$-reality of
$\Psi^{\otimes k}$ follows from that of $\Psi$.

**(C3) Reality of the pairing.** In the adopted normalisation
$\langle c_{-1}\bar c_{-1}c_0^-c_0^+c_1\bar c_1\rangle=-\tfrac12$ (real, no $i$), the note
states: $\omega_1(A,B)=\langle A|c_0^-|B\rangle$ is real for $\ddagger$-real $A,B$. We use it at
all ghost numbers (the reality of the $\Psi$ kinetic term $\langle\Psi|c_0^-Q_B|\Psi\rangle$
already pairs $N_{\rm gh}=2$ with $N_{\rm gh}=3$; the only structural input is that
hermitian conjugation of $c_0^-$ and of the BPZ inner product introduces no phase, which is
what the normalisation fixes). Caveat: hermitian conjugation reverses the order of $A$ and $B$,
so for two Grassmann-odd arguments the equivariance $\omega_1(A,B)^*=\omega_1(A^\ddagger,B^\ddagger)$
may carry a relative sign $(-1)^{|A||B|}$ that the note's even–odd case does not probe. Every
pairing used below is even–even (tower strands) or odd–even ($\lambda_k$ against $C_k$), so (C3)
is used only in the gradings where it is established; the odd–odd case is not needed.

**(C4) Reality of the vertices — hypothesis (H$_R$).** For the note's $n=4$,
$V_4(A_1,\dots,A_4)^*=V_4(A_1^\ddagger,\dots,A_4^\ddagger)$ follows from Sonoda–Zwiebach H5
($\mathcal O(t^*)=\mathcal O(t)^*$) *together with* the invariance of the moduli region
$\mathcal V_{0,4}$ and of its measure under complex conjugation of the moduli; (1.1) is the
conclusion of these two inputs, not H5 itself. We assume the same conclusion for every $n$:
$$V_n(A_1,\dots,A_n)^*=V_n(A_1^\ddagger,\dots,A_n^\ddagger)\qquad(n\ge2).\tag{1.1}$$
Origin: $V_n$ is a correlator of the $n$ vertex operators over a real region of moduli space
with a real measure; H5 says the vertex-operator insertions and the plumbing data transform
under hermitian conjugation into the insertions of the $\ddagger$-conjugate states at the
complex-conjugate moduli, and the moduli region and measure are invariant under that
conjugation. This is the standard CFT reality that makes the full nonpolynomial action real
[Erbin 2023]; the record does not re-derive it. Everything below is *conditional on* (1.1).

**Lemma 1 (real $\Leftrightarrow$ $\ddagger$-equivariant).** Let $F$ be a multilinear form on
$\mathcal H_0^{\otimes n}$ (or on any $\ddagger$-stable subspace). Then
$F(A_1,\dots,A_n)^*=F(A_1^\ddagger,\dots,A_n^\ddagger)$ for all arguments iff
$F$ takes real values on $\ddagger$-real arguments.

*Proof.* ($\Rightarrow$) immediate. ($\Leftarrow$) both $A\mapsto F(\dots,A,\dots)^*$ and
$A\mapsto F(\dots,A^\ddagger,\dots)$ are antilinear in each slot; two antilinear maps agreeing
on the real subspace (which spans over $\mathbb C$: $A=A_r+iA_i$) agree everywhere. $\square$

So (C3) says $\omega_1$ is equivariant, and (H$_R$) is the statement that each $V_n$ is
equivariant. Consequences used throughout:

- **(1.2)** $\omega_k:=\omega_1^{\otimes k}$ is equivariant on $\mathcal H_0^{\otimes k}$ (with (C2)):
  on product states $\omega_k(\otimes A_i,\otimes B_i)=\prod_i\omega_1(A_i,B_i)$, a product of
  equivariant forms; both sides of the equivariance identity are antilinear in each argument
  and agree on product states, which span. Hence $\omega_k$ is real on componentwise-real
  states, in particular on $\mathrm{Sym}^k\mathcal H_0$.
- **(1.3)** Multi-strand slots: $V_{a+b+c}(\Sigma_a,\Sigma_b,\Sigma_c)$ is the multilinear form
  $V_n$ on $\mathcal H_0^{\otimes n}$ evaluated on the tensor $\Sigma_a\otimes\Sigma_b\otimes\Sigma_c$;
  by (C2) and (1.1) it is equivariant in $(\Sigma_a,\Sigma_b,\Sigma_c)$, hence real when the three
  arguments are real.
- **(1.4)** Real linear combinations, products, and compositions of equivariant forms are
  equivariant; the polarization of a polynomial that is real on real arguments is an
  equivariant symmetric form (polarization has rational coefficients).
- **(1.5)** Operators. If $\omega$ is a non-degenerate equivariant pairing and $F(X,Y)=\omega(X,\hat FY)$,
  then $F$ equivariant $\Leftrightarrow$ $\hat F$ is *real*: $\hat F(Y^\ddagger)=(\hat FY)^\ddagger$.
  Real operators form a real algebra; the transpose w.r.t. $\omega$ of a real operator is real.

## 2. The tower

Setting: 019 §1/§4, truncation $K$, $g$ real, coefficients $a_k$ real, tower
$(\Sigma_2,\dots,\Sigma_K)$, $\Sigma_k\in\mathrm{Sym}^k\mathcal H_0$, all strands even.
Reality condition adopted for every level (the note's (eq:Sigreal) at $k=2$):
$$\Sigma_k^\ddagger=\Sigma_k\qquad(k\ge2).\tag{2.1}$$

**Lemma 2 (inverse of a real operator).** Let $\hat A$ be a real operator on a
$\ddagger$-stable space $W$ (in the sense (1.5)). Then (i) $\ker\hat A$ and
$\operatorname{im}\hat A$ are $\ddagger$-stable; (ii) if $\hat A$ is invertible, $\hat A^{-1}$ is
real; (iii) in general, for a real source $b\in\operatorname{im}\hat A$, the solution set
$\{X:\hat AX=b\}$ is $\ddagger$-stable and contains a real element, and its class in
$W/\ker\hat A$ is real.

*Proof.* (i) $\hat AX=0\Rightarrow\hat A(X^\ddagger)=(\hat AX)^\ddagger=0$; $Y=\hat AX\Rightarrow
Y^\ddagger=\hat A(X^\ddagger)$. (ii) With $X=\hat A^{-1}Y$: $\hat A(X^\ddagger)=Y^\ddagger$, so
$\hat A^{-1}(Y^\ddagger)=X^\ddagger=(\hat A^{-1}Y)^\ddagger$. (iii) If $\hat AX=b$ then
$\hat A(X^\ddagger)=b^\ddagger=b$, so $X^\ddagger$ is a solution and $X_r=\tfrac12(X+X^\ddagger)$
is a real solution; two solutions differ by a kernel element, and the quotient map is
$\ddagger$-equivariant by (i). $\square$

**Step 2.1 — the geometric parents are real.** $T_4=V_4$, $T_5=V_5$ are equivariant by (H$_R$).
For $n\ge6$, $T_n=-n!\,\mathrm{Pol}(A_{n-2})$ with $A_{n-2}(\Psi)=[g^{n-2}](S_{\rm prev}(\text{saddles})-S_{\rm eff})$.
Induction on $n$: if $T_4,\dots,T_{n-1}$ are equivariant, then (Step 2.2 applied to the
previous tower) $S_{\rm prev}(\text{saddles})$ is real for real $\Psi$; $S_{\rm eff}$ is real for
real $\Psi$ by (H$_R$); hence $A_{n-2}$ is a polynomial real on real $\Psi$ (coefficient of a real
power series in real $g$) and its polarization is equivariant by (1.4). So all parents, all
restrictions $\tilde M_k$ (the $(k|k)$ block), $L_k$ (the $(k|k-1,1)$ block with real $\Psi$
inserted), $\hat M_k=\tilde M_k-\tfrac{g}{2k+1}T_{2k+1}(\cdot,\cdot,\Psi)$ and
$\tilde u_2=V_4(\cdot,\Psi^{\otimes2})$ are equivariant forms / real operators (1.5).

**Step 2.2 — the action is real off-shell.** $S_K=-\mathcal A(\Sigma,\Sigma)+2\langle\mathfrak b,\Sigma\rangle$
(019 §1) is a real linear combination of equivariant forms evaluated on real arguments
$(\Sigma_k,\Psi)$: every kinetic term $a_k\tilde M_k(\Sigma_k,\Sigma_k)$, every odd coupling
$T_{2k+1}(\Sigma_k,\Sigma_k,\Psi)$, every source $2a_k\langle L_k(\Psi)\Sigma_{k-1},\Sigma_k\rangle$
is real. In particular this covers items (a) and (a′) of the brief in the canonical
presentation, and — by (1.3) — any presentation whose terms are geometric
$V_{a+b+c}(\Sigma_a,\Sigma_b,\Sigma_c)$ with real coefficients (R12's counting form, 017's
$S_4^\chi$ for its $\Sigma$-sector). *Verdict (a), (a′): real, given (2.1), (H$_R$) and real
coefficients; no further condition.*

**Step 2.3 — the fixed point preserves reality (the non-trivial step).** The saddle is
$\Sigma^*=\mathcal A^{-1}\mathfrak b$ with $\mathcal A$ block-tridiagonal in real operators
(Step 2.1) and $\mathfrak b=(a_2\tilde u_2,0,\dots,0)$ real for real $\Psi$. Under 019's
all-orders auxiliarity hypothesis ($\hat H_k$ invertible near $g=0$) $\mathcal A$ is invertible
and Lemma 2(ii) gives $\Sigma^{*\ddagger}=\Sigma^*$ level by level. Equivalently, through the
nested Schur form: $\hat H_K=\hat M_K$ is real; $\hat H_k=\hat M_k-g^2\tfrac{(2k)!}{(2k+2)!}L_{k+1}^\top\hat H_{k+1}^{-1}L_{k+1}$
is real by (1.5) and Lemma 2(ii) (real coefficient, transpose, inverse, composition), so the
continued fraction $\hat H_2$ is real, its inverse is real, and
$\Sigma_2^*=\tfrac12\hat H_2^{-1}\tilde u_2$ (up to 019's normalisation), then
$\Sigma_k^*=c_k\hat H_k^{-1}L_k\Sigma_{k-1}^*$ downward, are all real. The on-shell value
$S(\text{saddles})=\tfrac12V_2+\tfrac g{3!}V_3+\tfrac{g^2}{4!}\tilde u_2^\top\hat H_2^{-1}\tilde u_2$
is therefore real — as it must be, since it equals $S_{\rm eff}$ order by order.
*Kernel.* The CFT $V_{2k}$ is degenerate (R-ledger: $\Sigma\in\mathrm{Sym}^2\mathcal H_0/\ker V_4$).
Lemma 2(iii) covers this *given solvability* $b\in\operatorname{im}\hat A$, which is 019's
auxiliarity hypothesis and not a reality statement: under it $\ker\hat M_k$ is $\ddagger$-stable,
the quotient inherits $\ddagger$, and the on-shell class is real; a real representative always
exists (the real part of any solution). Reality of the on-shell class is thus proved conditional
on 019's solvability, not unconditionally. The perturbative $O(g_s^2)$ statement $\Sigma_2^*=\Psi^{\otimes2}+O(g)$ is the $g\to0$
limit of this. Reality of the leading term $\Psi^{\otimes 2}$ is (C2).

**Step 2.4 — sharpness of (2.1).** Is $\Sigma_k^\ddagger=\Sigma_k$ *forced*? For a single level
with kinetic term only, $V_{2k}(\Sigma_k,\Sigma_k)$ is real also for $\Sigma_k^\ddagger=-\Sigma_k$
($\Sigma_k=i\Sigma_r$, value $-V_{2k}(\Sigma_r,\Sigma_r)$), and more generally for any
$\Sigma_k^\ddagger=e^{i\theta}\Sigma_k$ with $e^{i\theta}=\pm1$. The *source*
$\langle L_k(\Psi)\Sigma_{k-1},\Sigma_k\rangle$ removes this freedom: it is linear in $\Sigma_k$
with a real coefficient operator acting on a real $\Sigma_{k-1}$, hence real iff
$\Sigma_k$'s imaginary part is $\omega_k$-orthogonal to $L_k(\Psi)\Sigma_{k-1}$ for all real
$\Psi,\Sigma_{k-1}$, i.e. iff $\mathrm{Im}\,\Sigma_k\in\bigcap_{\Psi,\Sigma_{k-1}}(\operatorname{im}L_k)^\perp$
— zero for generic parents (the sources span the dual). Propagating from $\Sigma_1=\Psi$ (real
by assumption) up the tower, the chain of sources forces (2.1) at every level, up to the
kernel directions of the sources, which are also the directions absent from the dynamics.
So (2.1) is not a choice but the unique condition compatible with a real $\Psi$; a relative
phase between levels is excluded by the sources, and $\Sigma_k\to-\Sigma_k$ is a field
redefinition that flips the sign of the source coefficient, not a different reality condition.

**Script part 1** (`codes/verify-reality-tower.py`, checks 1.x): $\mathcal H_0=\mathbb C^N$ with
the antilinear involution $\ddagger=$ entrywise complex conjugation followed by a fixed real
orthogonal involution $J$ (so $\ddagger\ne$ plain conjugation and the real subspace is not the
coordinate one); real $V_n$ = symmetric tensors with $V_n(J\cdot,\dots,J\cdot)=V_n$ real-valued
on real vectors, generated as $J$-symmetrised real random tensors; tower through $k=3$ with
parents $T_4,T_5,T_6,T_7$ (generic real, not fitted — reality does not depend on the
closure recursion); checks: reality of $S_K$ at random real $(\Psi,\Sigma_2,\Sigma_3)$ and
complex $g$ real; reality of on-shell $\Sigma_2^*,\Sigma_3^*$ ($\|\Sigma^{*\ddagger}-\Sigma^*\|$
at machine precision) including a degenerate $V_4$ with a $\ddagger$-stable kernel (class
reality); break legs: one non-equivariant component in $V_5$ makes both the action value and
$\Sigma^*$ non-real; a relative phase $\Sigma_2\to i\Sigma_2$ makes the source term imaginary.

## 3. The partner $\chi$

From 017 §1: $\chi\in\mathrm{Sym}^2\mathcal H_0$, $N_{\rm gh}=4$ (even strands, so (C2) is
unambiguous), with
$$S_\chi=\frac{g^2}{4!}\,a_\chi V_4(\chi,\chi)+\frac{g^3}{5!}\,b_\chi V_5(\chi,\Sigma,\Psi),
\qquad b_\chi^2/a_\chi=4\ \text{(forced by on-shell matching, R24)},\tag{3.1}$$
$(a_\chi,b_\chi)=(1,2)$ being the normalisation choice; only the ratio is invariant under the
complex rescaling $\chi\to\lambda\chi$, $(a,b)\to(\lambda^2a,\lambda b)$.

**Step 3.1 — general reality condition.** Suppose $\chi^\ddagger=e^{i\theta}\chi$ for some
phase. Then $\chi'=e^{-i\theta/2}\chi$ is $\ddagger$-real, and in terms of $\chi'$ the couplings
are $(a',b')=(e^{i\theta}a_\chi,e^{i\theta/2}b_\chi)$. With $\Sigma,\Psi$ real and (H$_R$), $S_\chi$
is real for all real $\chi'$ iff $a'$ and $b'$ are real (Lemma 1 applied slot by slot: the
kinetic and the coupling term are independent functions of $\chi'$ and must be real
separately — the kinetic is quadratic, the coupling linear in $\chi'$, so no cancellation
between them is possible for all $\chi'$). Hence:
$$S_\chi\ \text{real}\iff e^{i\theta}a_\chi\in\mathbb R\ \text{and}\ e^{i\theta/2}b_\chi\in\mathbb R .\tag{3.2}$$

**Step 3.2 — with R24's real couplings the condition is $\chi^\ddagger=\chi$.** If
$(a_\chi,b_\chi)$ are real and nonzero (as in R24, $(1,2)$), (3.2) forces $e^{i\theta/2}=\pm1$,
i.e. $e^{i\theta}=1$: $\boxed{\chi^\ddagger=\chi}$. The sign ambiguity $e^{i\theta/2}=-1$ is
the field redefinition $\chi\to-\chi$ (which flips $b_\chi$), not a different condition. So the
"expected" of R24 is proven, on the same footing as (2.1) for $\Sigma$: the *linear* coupling
excludes a phase, exactly as the source excludes it for $\Sigma_k$ (Step 2.4). (No circularity
with R24's real $(a,b)=(1,2)$: R24's on-shell matching is algebraic in the ratio $b^2/a$ and holds
verbatim for complex $(a,b)$, and the ratio is invariant under the rescaling (3.1).) The
alternative $\chi^\ddagger=-\chi$ with real $(a,b)$ leaves the kinetic term real (it becomes
$-a_\chi V_4(\chi_r,\chi_r)$) but makes the coupling imaginary — script check 2.2.

**Step 3.3 — the wrong sign is a consequence of reality.** Conversely, take any phase
convention and pass to the real field $\chi'$ with real $(a',b')$. On-shell matching (R24,
invariant under rescaling) gives $a'=b'^2/4$; with $b'$ real and nonzero, $a'>0$. Since
$\Sigma$'s kinetic term is $-\tfrac{g^2}{4!}V_4(\Sigma,\Sigma)$, the $\chi$ kinetic term
$+\tfrac{g^2}{4!}a'V_4(\chi',\chi')$ has the opposite sign *for the real field*:
$$\text{reality of }S_\chi\ +\ b'^2/a'=4\ \Longrightarrow\ a'>0:\ \text{the indefinite signature of R24 is forced, not chosen.}\tag{3.3}$$
A right-sign partner ($a'<0$) would need $b'$ imaginary, i.e. a non-real action. Script
check 2.3 exhibits the equivalence $(\chi^\ddagger=-\chi,\,b\in i\mathbb R)\simeq(\chi'\text{ real},\,a'=-a)$
with $b'^2/a'=b^2/a$ invariant. This sharpens 017 §3's "unitarity caveat": at tree level
the negative kinetic sign cannot be rotated away by a reality convention.

**Step 3.4 — on-shell value and the $O(g^4)$ theory.** $\chi_*=-\tfrac{g}{10}\tfrac{b_\chi}{a_\chi}V_4^{-1}v$
with $v=V_5(\cdot,\Sigma,\Psi)$ real for real $(\Sigma,\Psi)$ and $V_4^{-1}$ real on
$\mathrm{Sym}^2\mathcal H_0/\ker V_4$ (Lemma 2): $\chi_*^\ddagger=\chi_*$ (check 2.4). The full
$S_4^\chi$ of 017 is a real combination of geometric $V_n$ on real arguments $(\Psi,\Sigma,\chi)$,
hence real (Step 2.2 with (1.3)). If the $O(g^5)+$ extension needs a wrong-sign tower
(017 §5(b), open), the same argument applies field by field: each partner couples linearly
to real fields through a real $V_n$, so its reality condition is $\ddagger$-real, and each
forced kinetic sign is fixed by the corresponding matching ratio.

*Verdict (b): $\chi^\ddagger=\chi$, forced (not merely expected) by the linear coupling with
real $b_\chi$; the wrong sign of $a_\chi$ is a consequence of reality plus the forced ratio.*

## 4. Route C multipliers

R13: $S_C=\tfrac12\langle\Psi,Q\Psi\rangle+\sum_n\tfrac{g^{n-2}}{n!}\langle V_n|\sigma_n\rangle
+\sum_k\langle\lambda_k,\sigma_k-\sigma_{k-1}\otimes\Psi\rangle$, pairing $\omega_k=\omega_1^{\otimes k}$
(024 §2.3), $N_{\rm gh}(\lambda_k)=3k$, Grassmann parity $k\bmod2$; $\sigma_k$ even,
$N_{\rm gh}=2k$.

**Step 4.1 — the $\sigma$-sector.** $\sigma_k^\ddagger=\sigma_k$ (componentwise, all
strands even; on-shell $\sigma_k=\Psi^{\otimes k}$ is real by (C2)) is forced, not chosen: the
vertex term $\langle V_n|\sigma_n\rangle=V_n(\sigma_n)$ is *linear* in $\sigma_n$ with $V_n$
equivariant by (H$_R$), so a phase $\sigma_n^\ddagger=e^{i\theta}\sigma_n$ makes it non-real
(the argument of (3.2)'s linear term). With it the vertex terms are real by (H$_R$), and the constraints
$C_k:=\sigma_k-\sigma_{k-1}\otimes\Psi$ are $\ddagger$-real. The $\lambda$-EOMs
$\sigma_k=\sigma_{k-1}\otimes\Psi$ are real equations, so back-substitution preserves reality
and reproduces the (real) nonpolynomial action. The $\sigma$-EOMs
$\lambda_k=\lambda_{k+1}\cdot\Psi\ (\text{contracted})-\tfrac{g^{2k-2}}{(2k)!}V_{2k}|_{\sigma}$-type
relations have real coefficients, so the on-shell $\lambda_k$ are real if the top one is.

**Step 4.2 — the multiplier term.** Since $\omega_k$ is equivariant (1.2), for any $\lambda_k$
and real $C_k$: $\omega_k(\lambda_k,C_k)^*=\omega_k(\lambda_k^\ddagger,C_k)$. Hence the term is
real for all real $C_k$ iff $\omega_k(\lambda_k^\ddagger-\lambda_k,C_k)=0$ for all real $C_k$;
the real $C_k$ span over $\mathbb C$ the space in which $\sigma_k$ lives — $\mathrm{Sym}^k\mathcal H_0$
if $\sigma_k$ is symmetric (R13's on-shell $\Psi^{\otimes k}$ suggests so; 024 §2.3), in which case
$\sigma_{k-1}\otimes\Psi$ is symmetrised and (4.1) fixes only the $\mathrm{Sym}^k$-dual part of
$\lambda_k$, the rest being non-dynamical — and $\omega_k$ is non-degenerate there (R13: iff
$\omega_1$ is), so
$$\boxed{\lambda_k^\ddagger=\lambda_k}\qquad\text{(componentwise convention (C2), all }k).\tag{4.1}$$

*Annotation 2026-09-26 (record 055, critic-055-20260926T032500):* the $\mathrm{Sym}^k$-dual
part of $\lambda_k$ singled out above is the Koszul-antisymmetric part of
$\mathcal H_3^{\otimes k}$ (component arrays symmetric); see 055 §B2 (B2.2).
Script checks 3.1–3.3 ($k=1,2,3$): real $\lambda$ gives real values; a $\ddagger$-imaginary
part gives imaginary values; the solution space is exactly the real subspace (real dimension
$N^k$ — the toy takes $\lambda_k$ and $C_k$ in the full $\mathcal H_0^{\otimes k}$; for a
$\mathrm{Sym}^k$ multiplier the same argument restricts to $\mathrm{Sym}^k$ with dimension
$\binom{N+k-1}{k}$ and the toy's statement is the unsymmetrised version). No sign appears in this convention: the pairing is bilinear and equivariant
regardless of the ghost numbers of its arguments (C3), and the reality condition is the
same "+" for even and odd $k$.

**Step 4.3 — where a sign can enter (the brief's "$\pm$").** Two convention-dependent places,
both outside the toy:

1. *Reversed-order conjugation.* If $\ddagger$ on $\mathcal H_0^{\otimes k}$ is defined through
   hermitian conjugation with order reversal, it differs from (C2) by $(-1)^{k(k-1)/2}$ on
   tensors all of whose strands are Grassmann-odd. $\lambda_k$ is dual to $\mathrm{Sym}^k$ of
   $N_{\rm gh}=2$ strands via per-strand $c_0^-$ (saturation 5 per strand), so each of its
   strands sits at $N_{\rm gh}=3$, odd. In that convention (4.1) reads
   $\lambda_k^{\ddagger_{\rm rev}}=(-1)^{k(k-1)/2}\lambda_k$: $+$ for $k\equiv0,1$, $-$ for
   $k\equiv2,3\pmod 4$. This is the same condition written in another basis convention, not
   a physical alternative; the record adopts (C2), and any statement in the paper must name
   the convention.
2. *Grassmann layer.* For odd $k$ the components of $\lambda_k$ are Grassmann-odd; "real"
   then depends on the conjugation rule for products of odd generators
   ($(\theta_1\theta_2)^*=\theta_2^*\theta_1^*$ vs. $\theta_1^*\theta_2^*$), which the
   finite-dimensional toy (commuting components) does not model. With the standard rule
   (reversal on odd generators) and the componentwise $\ddagger$ on states, the term
   $\omega_k(\lambda_k,C_k)$ is Grassmann-even (024) and its reality is (4.1); a
   different Grassmann convention shifts (4.1) by the same kind of sign as item 1. Also
   assumed: $\ddagger^2=1$ on odd states (C1); if BPZ∘h.c. squared to $-1$ on the odd sector
   there would be no $\ddagger$-real odd states and the condition would have to be
   $\lambda_k^\ddagger=\pm i\lambda_k$ — not the case for the standard closed-string
   conjugation [Erbin 2023, where $\Psi^\ddagger=\Psi$ is imposed at every ghost number of
   the unconstrained field], but stated here as the one input not checked in this record.

*Verdict (c): $\lambda_k^\ddagger=\lambda_k$ for all $k$ in the componentwise convention;
$S_C$ is then real to all orders with $(\Psi,\sigma_k,\lambda_k)$ all $\ddagger$-real. The
$(-1)^{k(k-1)/2}$ of the reversed-order convention is a notation, not an obstruction.*

## Working notes

**Hand-off to 9b (T5 morphism check, record 029).** Nothing from this record is needed except
the convention of §1: $\ddagger$ componentwise (C2), Lemma 1 (real $\Leftrightarrow$
equivariant), and (H$_R$). If 9b's morphism $F$ is built from $V_n$, inverses and real
coefficients, it is automatically real (Step 2.1's argument); a non-real $F$ would signal a
non-real ingredient.

**What was not done.** (i) (H$_R$) for $n\ge5$ is inherited, not derived: the note proves it
at $n=4$ from Sonoda–Zwiebach H5; the general-$n$ statement is the standard one but is not
in the inputs. (ii) The Grassmann-odd sector ($\lambda_k$, odd $k$): the toy has commuting
components; the sign of the reality condition is convention-dependent as described in §4.3
and the $\ddagger^2=1$ assumption on odd states is not checked here. (iii) Convergence in
$g$ is not addressed (as in R26); reality is proven order by order / at fixed truncation.
(iv) The non-canonical presentations of R26 (fully polarized parents) are covered by
Step 2.1's induction only if the polarization-fit is done with real coefficients — true for
019's construction, but not re-checked numerically. (v) $\chi$ at $O(g^5)+$: argument given
field by field, no explicit tower.

**Proposed ledger text (for the orchestrator; not written to the ledger).**

*New row.* "**Reality of the whole auxiliary tower.** With $\ddagger=$ BPZ∘h.c. extended
componentwise to $\mathcal H_0^{\otimes k}$ and the hypothesis that every geometric $V_n$ is
$\ddagger$-equivariant ($V_n(A_i)^*=V_n(A_i^\ddagger)$ — the conclusion of Sonoda–Zwiebach H5 plus
conjugation invariance of the moduli regions and measures, the same inputs that make the
nonpolynomial action real), the scheme-B tower action of R26 is real at every
truncation for $\Sigma_k^\ddagger=\Sigma_k$, $\Psi^\ddagger=\Psi$: all kinetic terms, odd
couplings and sources are real, all parents $T_n=-n!\,\mathrm{Pol}(A_{n-2})$ are real by
induction, and the fixed point preserves reality ($\hat H_k$ real ⇒ $\hat H_k^{-1}$ real,
$\ker\hat M_k$ $\ddagger$-stable, on-shell class real). The condition $\Sigma_k^\ddagger=\Sigma_k$
is forced level by level by the sources, up to source-kernel directions, not chosen. Same for any presentation by geometric
$V_{a+b+c}(\Sigma_a,\Sigma_b,\Sigma_c)$ with real coefficients (R12). | Verified, conditional on (H$_R$) (proof at the
algebraic layer; numpy toy with a non-trivial antilinear involution, 18/18 PASS incl.
degenerate kernel and break legs) | `agent/derivations/028-reality-tower.md`;
`codes/verify-reality-tower.py`."

*R24 flag.* Replace "reality expected $\chi^\ddagger=\chi$, unproven" by "reality:
$\chi^\ddagger=\chi$ **proven** given (H$_R$) (and R24's ratio $b^2/a$, algebraic in complex $(a,b)$) and *forced* by the linear coupling $b_\chi V_5(\chi,\Sigma,\Psi)$
with real $b_\chi$ (a phase $\chi^\ddagger=e^{i\theta}\chi$ is a field redefinition
$(a,b)\to(e^{i\theta}a,e^{i\theta/2}b)$ and reality of both coefficients pins $e^{i\theta}=1$);
moreover reality + $b_\chi^2/a_\chi=4$ ⇒ $a_\chi>0$: the wrong sign is forced (028 §3)."

*R13 flag.* Replace "reality" in OPEN by "reality: $\sigma_k^\ddagger=\sigma_k$,
$\lambda_k^\ddagger=\lambda_k$ in the componentwise $\ddagger$ convention (equal to
$(-1)^{k(k-1)/2}\lambda_k$ under reversed-order h.c., since each strand of $\lambda_k$ is at
$N_{\rm gh}=3$); $S_C$ real to all orders; Grassmann-odd conjugation rule and $\ddagger^2=1$ on
odd states assumed (028 §4)."

## Verification

`codes/verify-reality-tower.py`, seed 20260914, $N=3$ ($\dim\mathrm{Sym}^2=6$,
$\dim\mathrm{Sym}^3=10$), executed 2026-09-14: **18/18 PASS**, exit 0.

Representation: $\mathcal H_0=\mathbb C^3$, $x^\ddagger=J\bar x$ with $J$ a random real
reflection (so the $\ddagger$-real subspace is $\{x_r+ix_i: Jx_r=x_r, Jx_i=-x_i\}$, not the
coordinate real subspace — a plain-conjugation toy would make several checks vacuous);
$\omega_1(x,y)=x^Ty$; real symmetric $V_n$ generated as $J^{\otimes n}$-conjugation-symmetrised
complex random tensors (check 1.1 confirms equivariance, 1.1b that a generic tensor fails it).
Tower: 019 §1 Jacobi form with generic real $T_4..T_7$ (not fitted for closure — reality is
independent of the recursion), $g=0.37$, $a_k=g^{2k-2}/(2k)!$.

| Check | Claim | Method | Falsifier |
|---|---|---|---|
| 1.2 | $S_K$ real off-shell (Step 2.2) | value at random real fields, $|\mathrm{Im}|<10^{-10}$ | 1.5, 1.6 |
| 1.3, 1.3b | saddle real, on-shell value real (Step 2.3) | `solve`, $\|\Sigma^{*\ddagger}-\Sigma^*\|<10^{-10}$ | 1.5 |
| 1.4, 1.4b | degenerate kernel: solution class real (Lemma 2(iii)) | $\omega$-orthogonal real projector kills one real direction, rank drops by 1, kernel vector real, `lstsq` min-norm solution real and exact | — (structural) |
| 1.5 | break: non-equivariant $V_5$ component ⇒ $S$ and $\Sigma^*$ non-real | as 1.2/1.3 with $T_5+i\,\mathrm{Re}(T_5')$ | — |
| 1.6 | break: $\Sigma_2\to i\Sigma_2$ ⇒ non-real (Step 2.4) | as 1.2 | — |
| 2.1 | $S_\chi$ real, $\chi$ real, $(a,b)=(1,2)$ | value | 2.2 |
| 2.2 | $\chi^\ddagger=-\chi$, real $(a,b)$: kinetic real, coupling imaginary (Step 3.2) | both terms separately | — |
| 2.3 | $(\chi^\ddagger=-\chi,\ b\in i\mathbb R)\simeq(\chi'\text{ real},\ a'=-a)$, $b^2/a$ invariant (Step 3.3) | equality of values, ratio | — |
| 2.4, 2.4b | $\chi_*$ real for real $b$; $\ddagger$-imaginary for imaginary $b$ (Step 3.4) | `solve` on $\mathrm{Sym}^2$ | 2.4b |
| 2.5 | $\chi_*$ is stationary | gradient $<10^{-10}$ | — |
| 3.1–3.3 | $\omega_k(\lambda,C)$ real ∀ real $C$ iff $\lambda$ real, $k=1,2,3$ (4.1) | values + rank of the real-linear map $\lambda\mapsto\mathrm{Im}\,\omega_k(\lambda,C_j)$ over a spanning set of real $C_j$: solution space has real dimension exactly $N^k$ | $\ddagger$-imaginary part added |

Development note (consolidated): two check bugs were found and fixed during the run, both in
the check code, not in the derivation — (i) 2.4 first inverted $V_4$ on the full
$\mathcal H^{\otimes2}$, where the symmetric tensor is degenerate on antisymmetric tensors
(fixed by restricting to $\mathrm{Sym}^2$); (ii) 3.x first spanned the real subspace with
$\tfrac12(e_j+e_j^\ddagger)$ only, which misses the $J$-odd imaginary directions; (iii) 1.4
first used a Hermitian projector $I-ww^\dagger$, which is not $\ddagger$-real and does not
lower the rank of the bilinear form — replaced by the $\omega$-orthogonal $I-ww^T/\omega(w,w)$.

Not machine-checked: (H$_R$) itself; the Grassmann-odd sector and the $\ddagger^2$ on odd
states (§4.3); convergence in $g$.

**Part 5 (Step 2.1's polarisation step, added 2026-09-26).** The one carve-out named above —
"parents $T_{n\ge6}$ real because the polarisation of a real polynomial has real coefficients"
— is now exercised directly, closing it. Construction: a ground-truth $\ddagger$-real,
permutation-symmetric tensor $C$ (order $n=6$, generated exactly as `real_sym_tensor` in part 1)
defines the scalar polynomial $A(\Psi)=C(\Psi^{\otimes6})$; the standard finite-difference
polarisation formula
$$\mathrm{Pol}(A)(v_1,\dots,v_6)=\frac1{6!}\sum_{S\subseteq[6]}(-1)^{6-|S|}A\Big(\sum_{i\in S}v_i\Big)$$
is implemented as a black box that only ever calls $A$ as a scalar function — it never touches
$C$ — and reconstructs $T_6=-6!\,\mathrm{Pol}(A)$. Checks: 5.1 $T_6$ is $\ddagger$-real; 5.2 $T_6$
is a symmetric tensor; 5.3 $T_6$ reconstructs $-6!\,C$ exactly (componentwise, $\|\cdot\|\sim
10^{-11}$), i.e. the routine correctly inverts the polarisation map; 5.4 the diagonal identity
$T_6(\Psi^{\otimes6})=-6!\,A(\Psi)$ holds at a random real $\Psi$ off the $0/1$ construction grid
(an independent evaluation point, not one of the basis sums used to build $T_6$); 5.5
$\ddagger$-equivariance of $T_6$ at generic complex arguments, the form Step 2.1 actually uses
downstream ((1.4), (1.5)). Break legs: a complex perturbation of a single coefficient of $A$
(one permutation-symmetric orbit of $C$, kept permutation-symmetric so 5.2's structural property
survives) breaks both 5.1 (reality, $\|T^\ddagger-T\|\sim5\times10^3$) and 5.5 (equivariance,
residual $\sim6\times10^3$) while leaving symmetry intact — confirming the checks probe reality
specifically, not symmetry; a wrong normalisation $(n-1)!$ in place of $n!$ breaks the diagonal
identity 5.4 by exactly the expected factor $n=6$. Together with parts 1–4 (which already prove
that a real $A_{n-2}$ propagates to a real tower, granting the parents' reality), part 5 confirms
the remaining link: the polarisation map itself, applied mechanically to a real polynomial,
outputs a $\ddagger$-real, correctly-normalised symmetric tensor. Script:
`codes/verify-reality-tower.py`, part 5 (function `part5`); log
`agent/scratch/reality-tower-run-part5.log`; full run **55/55 PASS** (48 pre-existing + 7 new),
exit 0, seed 20260914, re-run confirms parts 1–4 unchanged.

## Status

record closed 2026-09-14: critic ACCEPT (9 minor edits applied in 9c); promoted to ledger R35 (+ R13/R24 flag closures); next: none
9c fixes applied (H5 → H5 + region/measure invariance; source-kernel caveat in §0 and ledger text; (C3) odd–odd sign caveat; solvability caveat in the kernel paragraph; R24 complex-$(a,b)$ sentence; $\sigma_k$ reality forced; $\mathrm{Sym}^k$ vs $\mathcal H_0^{\otimes k}$ in Step 4.2; §0 row (c) hedge; Step 2.1 induction listed as untested; script 18/18 PASS); closed pending promotion. Reports: `agent/reports/computator-9a-reality-tower-20260914T045500.md`, `agent/reports/computator-9c-fixes-20260914T071000.md`.
2026-09-26: added script part 5 exercising Step 2.1's polarisation step directly (task 9e,
rigor-audit carve-out). 55/55 PASS (48 pre-existing unchanged + 7 new checks 5.1–5.5,
break-5.1/5.5, break-5.4). Verification section updated above. Report:
`agent/reports/computator-r35-polarisation-20260926T015000.md`. Next: none pending on this
record; ledger annotation (removing the "polarisation step untested" caveat from R35, if any)
is the orchestrator's.
2026-09-26 (Task 8a): the general-$n$ source for H5 + region/measure invariance is located —
Zwiebach 1993 (hep-th/9206084) §5.1 condition (c) and §7.4 eq. (7.98) prove the reality of
$\{\Psi^n\}_g$ for every $(g,n)$ given the mirror condition on the vertices; extraction in
`agent/context/zwiebach1993-vertex-reality-2026-09-26.md`. PH6 (a) supported by citation; (b)
for the SL(2,C) family: record 054 at $n=4$ (R56).

## Addendum 2026-09-26 — PH7: is $\ddagger^2=1$ on Grassmann-odd states? (Task 9c)

**Brief:** `agent/briefs/active-computator-ph7-20260926T102000.md` (computator, Opus).
**Script:** `codes/verify-ph7-ddagger.py`; log `agent/scratch/ph7-run1.log`.
**Sources:** [Erbin 2023] (book conventions) and Zwiebach 1993 (hep-th/9206084).
This addendum is appended; nothing above it is edited. No claim tree (legacy record).

### P.0 Task and objective

*Literal task.* Compute $\ddagger$ and $\ddagger^2$ explicitly, in the book's conventions, on one
Grassmann-odd and one Grassmann-even level-matched state annihilated by $b_0^-$, with complex
coefficients, tracking every Grassmann sign; machine-check it on a Jordan–Wigner representation of
the ghost modes $c_{-1},c_0,c_1,b_{-1},b_0,b_1$ and their barred partners.
*Objective.* PH7 ($\ddagger^2=1$ on Grassmann-odd states) is the one fact bundled with the reality
of the Route C multipliers at odd $k$ (R13, R35); if it failed there would be no $\ddagger$-real odd
states. A definite sign, with the convention that decides it, closes PH7 either way.

### P.1 The definitions, as quoted

*Book ([Erbin 2023]).* Notation collision first: the book's macro `\eadj`
renders $^\ddagger$ and denotes the **Hermitian-conjugate state** (`includes/commands.tex` l. 93;
`chapters/formulas.tex` l. 150, 193; `chapters/bsft_free_brst.tex` l. 240). The book's reality
conjugation is the **star conjugation** $\mathcal O^\star$ (`\sco`, commands l. 95), and the book
notes that it is Erler's $\mathcal O^\ddagger$ (`cft_operator_formalism.tex` l. 1300–1302). The
project's $\ddagger$ (028 §1, C1) is the book's $\star$.

- Star conjugation, `cft_operator_formalism.tex` l. 1240–1246 (`cft:eq:conj-star`):
  "we define star conjugation as the combination of Hermitian and BPZ conjugations:
  $\mathcal O(z,\bar z)^\star:=\big(\mathcal O(z,\bar z)^t\big)^\dagger=\big(\mathcal O(z,\bar z)^\dagger\big)^t$."
- Its algebra, l. 1275–1289: "star conjugation acts by complex conjugation of any $c$-number and
  reverses the order of the operators without any sign: $((\lambda A)^\star)^\star=A$,
  $(\lambda A)^\star=\lambda^*A^\star$, $(AB)^\star=B^\star A^\star$"; for a string,
  $(\lambda A_1\cdots A_n)^\star=\lambda^*A_n^\star\cdots A_1^\star$. (The involution statement
  l. 1277 drops the $\lambda$ on the right-hand side; it evidently means $\lambda A$.)
- Hermitian adjoint of operators, l. 940–955: "reverses the order of the operators without any
  sign", $(\lambda A_1\cdots A_n)^\dagger=\lambda^*A_n^\dagger\cdots A_1^\dagger$.
- BPZ of operators, l. 1134–1146: "does not complex conjugate $c$-number nor changes the order of
  the operators", $(AB)^t=A^tB^t$, $(A^t)^t=A$; l. 1147–1154: restoring radial order gives
  $(AB)^t=(-1)^{|A||B|}B^tA^t$ — "This problem does not arise when working in terms of the modes."
- Modes, l. 1673–1698: $\phi_n^t=(-1)^h(\pm1)^n\phi_{-n}$ (`cft:eq:chiral-modes-bpz`),
  $\phi_n^\dagger=\phi^+_{-n}$ (`cft:eq:chiral-modes-adj`), $\phi_n^\star=(-1)^h(\pm1)^n\phi^+_n$
  (`cft:eq:chiral-modes-star`).
- Closed string, `bos_worldsheet_cft.tex` l. 1098: "For the closed string, BPZ conjugation uses the
  inversion $I^+(z)=1/z$"; table l. 1130–1213: $b_n^\dagger=b_{-n}$, $c_n^\dagger=c_{-n}$ (same for
  barred), $b_n^t=b_{-n}$, $c_n^t=-c_{-n}$, $b_n^\star=b_n$, $c_n^\star=-c_n$; l. 1217–1229
  (`bos:eq:conjugation-c0pm-b0pm`): $(c_0^\pm)^t=-c_0^\pm$, $(b_0^\pm)^t=b_0^\pm$. Open string
  (l. 1554–1575, $I^-$): $c_n^t=(-1)^{n+1}c_{-n}$, $b_n^t=(-1)^nb_{-n}$.
- States, `formulas.tex` l. 193: $(\lambda A_1\cdots A_n|0\rangle)^{\rm hc}=\lambda^*\langle0|A_n^\dagger\cdots A_1^\dagger$;
  l. 231–234: $(\lambda A_1\cdots A_n|0\rangle)^t=\lambda\langle0|A_1^t\cdots A_n^t$ (order kept, no
  conjugation); l. 200–202: $(A,B):=\langle A_{\rm hc}|B\rangle$ obeys $(A,B)^\dagger=-(B,A)$.
- Normalisation, `bos_worldsheet_cft.tex` l. 1310–1321: $\langle c_{-1}\bar c_{-1}c_0\bar c_0c_1\bar c_1\rangle=-1$,
  $\langle c_{-1}\bar c_{-1}c_0^-c_0^+c_1\bar c_1\rangle=-\tfrac12$.
- Reality condition. Open string, `bsft_free_brst.tex` l. 237–241: "The appropriate reality
  condition identifies the Euclidean and BPZ conjugates: $|\Phi\rangle^{\rm hc}=|\Phi\rangle^t$."
  Closed string: **no condition in the text** — only the comment l. 1637
  "% reality condition, Zwiebach : $\langle\Psi_{\rm hc}|=-\langle\Psi|$". The PH7 motivation
  "[Erbin 2023] imposes $\Psi^\ddagger=\Psi$ at every ghost number of the unconstrained field" is
  therefore not a statement of the book's text; the closed-string condition in use is Zwiebach's.

*Zwiebach 1993 (hep-th/9206084).*

- l. 246–248, (2.31): $\langle\mathbf 1,p|c_{-1}\bar c_{-1}c_0^+c_0^-c_1\bar c_1|\mathbf 1,p'\rangle=(2\pi)^d\delta^d(p-p')$ (real, no $i$).
- l. 258–266, (2.33)–(2.34): $c_n^\dagger=c_{-n}$, $b_n^\dagger=b_{-n}$;
  $(A_1\cdots A_n|\mathbf 1,p\rangle c)^\dagger=\bar c\,\langle\mathbf 1,p|A_n^\dagger\cdots A_1^\dagger$.
- l. 284–288, (2.37): $(A,B)^\dagger=-(B,A)$; "The unusual minus sign arises due to the absence of
  an $i$ factor in the right hand side of (2.31) … We have used the dagger … instead of complex
  conjugation in order to take into account the fact that the c-numbers that multiply the states
  may have nontrivial statistics."
- l. 306–326, (2.40)–(2.42): BPZ with $I(z)=1/z$, $\phi_n^T=(-1)^d\phi_{-n}$;
  $(c\,a_nb_mc_p\cdots|\mathbf 1\rangle)^T=\langle\mathbf 1|\,c\,(a_n)^T(b_m)^T(c_p)^T\cdots$ — "the
  order of the operators does not change and … the c-number is not complex conjugated."
- l. 654–657, (3.6): "we demand that hermitian conjugation and BPZ conjugation give the same state
  up to a sign: $(|\Psi\rangle)^\dagger\equiv\langle\Psi_{hc}|=-\langle\Psi|$"; (3.7)–(3.8), l. 660–672:
  for $|T\rangle=\int\phi(p)c_1\bar c_1|\mathbf 1,p\rangle$ this is $\phi^*(p)=\phi(-p)$; (3.9), l. 676–684.

### P.2 Setup

Assumptions local to this addendum (conventions, all quoted in P.1):

- (P-A1) Hermitian conjugation: $c_n^\dagger=c_{-n}$, $b_n^\dagger=b_{-n}$ (barred alike); on states,
  order reversal without sign and complex conjugation of the coefficient.
- (P-A2) BPZ: $\phi_n^t=(-1)^h(\pm1)^n\phi_{-n}$, closed string $I^+$ (book) or $I^-$ (ledger
  C1(ii)); on states, order kept and no conjugation (ledger C1(iii)).
- (P-A3) $\ddagger:=\eta\,\mathrm{bpz}^{-1}\circ\mathrm{hc}$ on kets, $\eta=\pm1$ a constant
  ($\eta=-1$ is Zwiebach (3.6)); the ghost-number-dependent variant
  $\ddagger':=(-1)^{N_{\rm gh}+1}\,\mathrm{bpz}^{-1}\circ\mathrm{hc}$ appears in P.6.
- (P-A4) Coefficients: complex numbers, or Grassmann-odd c-numbers placed to the right of the ket
  (Zwiebach l. 742: $|\Lambda\rangle=\sum|\Phi_r\rangle\lambda_r$), with a conjugation $\dagger$
  that reverses products (Zwiebach l. 288). Its square is the one input left open by (P-A1)–(P-A3):
  standard $\theta^{\dagger\dagger}=\theta$, or graded $\theta^{\dagger\dagger}=(-1)^{|\theta|}\theta$.

*Constants.* The out-vacuum normalisation $\kappa$ is fixed from the book's
$\langle c_{-1}\bar c_{-1}c_0\bar c_0c_1\bar c_1\rangle=-1$; the $c_0^\pm$ form $-\tfrac12$ is then a check.
$\ddagger$ does not depend on $\kappa$ (P7.6). $\eta$ is a sign convention. Nothing is fitted.

*States.* $A_\alpha=\alpha\,c_1\bar c_1|0\rangle$ (even, $N_{\rm gh}=2$) and
$B_\beta=\beta\,c_0^+c_1\bar c_1|0\rangle$ (odd, $N_{\rm gh}=3$, the per-strand ghost number of
$\lambda_k$, 024 §2.3); both have $L_0=\bar L_0=-1$ and are annihilated by $b_0^-$
($\{b_0^-,c_0^+\}=\tfrac12-\tfrac12=0$). $\alpha,\beta\in\mathbb C$ generic; $A_1,B_1$ at unit coefficient.

### P.3 Derivation

$$\phi_n^\star:=(\phi_n^\dagger)^t=(\phi_{-n})^t=(-1)^h(\pm1)^n\phi_n=:s_\phi\,\phi_n,\qquad s_\phi\in\{\pm1\}.\tag{P.1}$$
Closed string, $I^+$: $c_n^\star=-c_n$, $b_n^\star=b_n$, $(c_0^\pm)^\star=-c_0^\pm$; $I^-$: $c_n^\star=(-1)^{n+1}c_n$.

For $v=\lambda\,O_1\cdots O_k|0\rangle$, $O_i$ creation modes, $k_o$ of them Grassmann-odd:
$$\begin{aligned}
\mathrm{hc}(v)&=\lambda^*\langle0|O_k^\dagger\cdots O_1^\dagger,\\
v^\ddagger=\eta\,\mathrm{bpz}^{-1}\big(\mathrm{hc}(v)\big)&=\eta\lambda^*\,O_k^\star\cdots O_1^\star|0\rangle
=\eta\lambda^*\Big(\prod_{i}s_{O_i}\Big)(-1)^{k_o(k_o-1)/2}\,O_1\cdots O_k|0\rangle,
\end{aligned}\tag{P.2}$$
$$v^{\ddagger\ddagger}=\eta^2\,(\lambda^*)^*\Big(\prod_{i}s_{O_i}\Big)^2\big((-1)^{k_o(k_o-1)/2}\big)^2\,O_1\cdots O_k|0\rangle=v.\tag{P.3}$$

Even control:
$$\begin{aligned}
\mathrm{hc}(A_\alpha)&=\alpha^*\langle0|\bar c_{-1}c_{-1},\\
A_\alpha^\ddagger&=\eta\alpha^*\,\bar c_{-1}^{\,t}c_{-1}^{\,t}|0\rangle=\eta\alpha^*(-\bar c_1)(-c_1)|0\rangle
=\eta\alpha^*\,\bar c_1c_1|0\rangle=-\eta\alpha^*A_1,\\
A_\alpha^{\ddagger\ddagger}&=-\eta\,(-\eta\alpha^*)^*A_1=\alpha A_1.
\end{aligned}\tag{P.4}$$
Odd state:
$$\begin{aligned}
\mathrm{hc}(B_\beta)&=\beta^*\langle0|\bar c_{-1}c_{-1}c_0^+,\\
B_\beta^\ddagger&=\eta\beta^*\,\bar c_{-1}^{\,t}c_{-1}^{\,t}(c_0^+)^t|0\rangle=\eta\beta^*\,\bar c_1c_1(-c_0^+)|0\rangle
=\eta\beta^*\,c_0^+c_1\bar c_1|0\rangle=\eta\beta^*B_1,\\
B_\beta^{\ddagger\ddagger}&=\eta\,(\eta\beta^*)^*B_1=\beta B_1.
\end{aligned}\tag{P.5}$$

Grassmann layer, $v=|\phi\rangle\theta$ with $|\phi\rangle$ a monomial with $k_o$ odd modes and $\theta$ of parity $p$:
$$\begin{aligned}
\mathrm{hc}(|\phi\rangle\theta)&=\theta^\dagger\langle\phi_{\rm hc}|=(-1)^{pk_o}\langle\phi_{\rm hc}|\,\theta^\dagger,\\
(|\phi\rangle\theta)^\ddagger&=(-1)^{pk_o}\,|\phi^\ddagger\rangle\,\theta^\dagger,\qquad
(|\phi\rangle\theta)^{\ddagger\ddagger}=|\phi\rangle\,\theta^{\dagger\dagger}.
\end{aligned}\tag{P.6}$$

### P.4 Commentary

- (P.1): hc and BPZ each send $n\to-n$, so their composite sends a mode to a multiple of itself; the
  multiple is real because $h$ is an integer ($h_c=-1$, $h_b=2$). In the matter sector the same holds
  up to $p\to-p$ ($\alpha_n^\star=-\alpha_n$, $|k\rangle^\star=|-k\rangle$, book l. 1188–1213, 1258–1264),
  also an involution.
- (P.2): the order reversal comes from hc alone; $\mathrm{bpz}^{-1}$ keeps the order (it is its own
  inverse on modes, $(\phi_n^t)^t=\phi_n$). The sign $(-1)^{k_o(k_o-1)/2}$ restores the original order;
  creation modes mutually anticommute (no contractions among them).
- (P.3): the reversal sign and each $s_O$ enter squared, and $\lambda$ is conjugated twice. So $\ddagger$
  is diagonal in the monomial basis with real $\pm1$ entries; an antilinear map of this form squares to
  $1$. The mismatch the brief points to (hc reverses, BPZ keeps) is exactly what makes $\ddagger$
  order-reversing, and a second application undoes it: it cannot produce $(-1)^\epsilon$ in $\ddagger^2$.
- (P.4): $\bar c_1c_1=-c_1\bar c_1$. The same product $\bar c_{-1}^{\,t}c_{-1}^{\,t}=\bar c_1c_1$ holds with
  $I^-$ ($c_{-1}^t=(-1)^{-2}c_1$).
- (P.5): $\bar c_1c_1c_0^+\to c_0^+c_1\bar c_1$ is the reversal of three odd modes, sign $(-1)^3=-1$,
  which cancels the $-1$ of $(c_0^+)^t=-c_0^+$.
- (P.6): moving $\theta^\dagger$ from the left of the bra (Zwiebach (2.34)) to the right, where BPZ keeps
  the coefficient, costs $(-1)^{pk_o}$; that sign is squared on the second application. What survives is
  $\theta^{\dagger\dagger}$.
- *Well-definedness of the order-kept BPZ rule.* It is consistent only on normal-ordered (creation)
  words. As an operator map BPZ is the graded anti-automorphism $(XY)^t=(-1)^{|X||Y|}Y^tX^t$ (book
  l. 1151), which coincides with the order-kept rule on mutually anticommuting creation modes (check
  B1, all twelve modes). Applied literally to a non-normal-ordered word it contradicts the algebra:
  $b_{-1}c_1|0\rangle=|0\rangle$, whereas $\langle0|b_{-1}^tc_1^t=-\langle0|b_1c_{-1}=0$ ($I^+$). The book's
  "This problem does not arise when working in terms of the modes" (l. 1154) holds for creation words;
  C1(iii) should carry that qualifier. Symmetrically, hc must be the *ungraded* reversal (check H1).
- *$I^+$ versus $I^-$.* On a monomial the two BPZ rules differ by $(-1)^{\sum n_i+\sum\bar n_j}=(-1)^{L_0-\bar L_0}$,
  so C1(ii) (the $I^-$ rule) and the book's closed-string table ($I^+$) agree on level-matched states
  (P7.5: 24 level-matched monomials agree, others differ, e.g. $c_1|0\rangle$).
- *Normalisation.* $\kappa$ drops out of $\ddagger$ (hc and BPZ land on the same out-vacuum). The real
  normalisation ("no $i$") behind Zwiebach's minus sign in (2.37) therefore does not reach $\ddagger$ or
  $\ddagger^2$. It reaches the equivariance sign of the pairing (P.6 below).

### P.5 Result and verdict

$$\boxed{\ \ddagger^2=+1\ \text{on every state of the closed-string Fock space, Grassmann-even and odd,}\
A_\alpha^\ddagger=-\eta\alpha^*A_1,\quad B_\beta^\ddagger=\eta\beta^*B_1\ }$$
for either constant sign $\eta$, either inversion $I^\pm$, any normalisation, and either ordering
convention for products (the order-reversing flip changes $\ddagger$ by $(-1)^{k(k-1)/2}$ per $k$-mode
word, not $\ddagger^2$: checks R1a–R1c). With Grassmann-odd coefficients
$(|\phi\rangle\theta)^{\ddagger\ddagger}=|\phi\rangle\theta^{\dagger\dagger}$: $+1$ for the standard,
involutive conjugation of c-numbers; $(-1)^{|\theta|}$ only in the graded convention
$\theta^{\dagger\dagger}=-\theta$ (break leg Gr2).

**Verdict: PH7 holds.** It is a consequence of the definitions, not a hypothesis. The one convention that
could flip it is the square of complex conjugation on Grassmann-odd c-numbers. Zwiebach writes the
conjugate of a coefficient as a dagger (l. 288, "c-numbers $\ldots$ may have nontrivial statistics") and
states no rule for its square; the involutive rule is the standard reading of a Hermitian conjugation
(a convention, named here), and the graded rule appears in none of the inputs read here. For commuting
(ordinary) coefficients PH7 is unconditional. The ordering mismatch between hc and BPZ does not decide it.

*Consequence (closure map).* There is no obstruction to $\ddagger$-real odd states: every odd state splits
into $\ddagger$-real and $\ddagger$-imaginary parts. The Route C multipliers at odd $k$ admit a reality
condition. Its sign is a convention, fixed in P.6. R35's "Route C multipliers at odd $k$:
Conditional(PH6, PH7)" reduces to Conditional(PH6) plus the named sign convention. The HS tower is
unaffected (R46 does not use PH7).

*Proposed PH7 row (for the orchestrator; not written to the ledger).* Status column: "**discharged
2026-09-26** – Proven (028 addendum P.3–P.5; node check `agent/reports/critic-028-ph7-node-20260930T233800.md`:
P.3, P.5 hold) – Verified on the ghost truncation $n\in\{-1,0,1\}$ (`codes/verify-ph7-ddagger.py`, 35/35, seed
20260926); matter sector argued, not machine-checked". Appended text: "$\ddagger=\eta\,\mathrm{bpz}^{-1}\circ\mathrm{hc}$ maps each mode monomial
to a real multiple of itself ($\phi_n^\star=(-1)^h(\pm1)^n\phi_n$), so $\ddagger^2=+1$ on every state,
even or odd, for either sign $\eta$, either inversion, any normalisation and either ordering convention
for products. With Grassmann-odd coefficients $\ddagger^2$ is the square of c-number conjugation: $+1$
in the standard involutive convention for conjugating odd coefficients (Zwiebach writes it as a dagger;
no input states a rule for its square), $-1$ on odd coefficients only under the graded
convention $\theta^{**}=-\theta$." Motivation column, correction (the addendum's reading of the book's current text, not verified by the node check): the book
states the reality condition only for the open string (`bsft_free_brst.tex` l. 237–241); for the
closed string it has a TODO citing Zwiebach (3.6) (l. 1637). The source for the closed string is
Zwiebach (3.6)/(3.9).

### P.6 Side finding: the sign of the reality condition, and 028 (C3)

This is outside the literal task but bears on the objective (reality of $S_C$ at odd $k$).

1. With a constant $\eta$ and $s=+1$ (R58), the pairing is **anti-equivariant**:
   $\omega_1(A^\ddagger,B^\ddagger)=-\,\omega_1(A,B)^*$ on every nonvanishing pair of the truncated
   space, $(g_A,g_B)\in\{(0,5),\dots,(5,0)\}$ (check S2a). This is Zwiebach's (2.37) minus sign, a
   consequence of the real normalisation. So 028 (C3), "$\omega_1(A,B)$ is real for $\ddagger$-real
   $A,B$", **fails for constant $\eta$** (either sign). Example with $\eta=+1$: $iA_1$ and $B_1$ are $\ddagger$-real,
   and $\omega_1(iA_1,B_1)=-\tfrac i2$.
2. With $\ddagger'=(-1)^{N_{\rm gh}+1}\,\mathrm{bpz}^{-1}\circ\mathrm{hc}$, the pairing is equivariant on
   every pair (S2b; any sign $\eta(g)$ with $\eta(g)\eta(5-g)=-1$ does this), $\ddagger'^2=1$ (S2c), and
   $A_1$, $B_1$ with real coefficients are both $\ddagger'$-real.
3. **$\ddagger'$ is what Zwiebach's condition becomes on components, single strand.** Impose (3.6) with its constant
   $\eta=-1$ on the Grassmann-even total field $\sum_s|\Phi_s\rangle\psi_s$, where odd states carry odd
   coefficients. Then (P.6) with $p=k_o$ gives $(|\Phi_s\rangle\psi_s)^\ddagger=(\ddagger'|\Phi_s\rangle)\,\psi_s^\dagger$
   on every component (check S3, all 64 ghost words; single strands only, extended componentwise to $k$ strands, since a
total sign $(-1)^{N^{\rm tot}_{\rm gh}+1}$ differs from the componentwise one by $(-1)^{k+1}$). The break leg, which drops the $(-1)^{k_o}$ from
   moving the coefficient, fails.

*Consequence for 028.* The componentwise conditions of 028 ($\Psi^\ddagger=\Psi$, $\lambda_k^\ddagger=\lambda_k$,
with $\omega_1$ equivariant, (C3)) are correct when $\ddagger$ is read as $\ddagger'$. On the even-strand objects
($\Psi$, every strand of $\Sigma_k$, $\chi$), $\ddagger'$ is Zwiebach's constant-sign conjugation (3.6) with $\eta=-1$
at $N_{\rm gh}=2$; the difference is on the $N_{\rm gh}=3$ strands (targets of the operators in (1.5), $\lambda_k$).
Read literally, 028 (C1) "$\ddagger=$ BPZ∘h.c." is $\eta=+1$, the opposite of Zwiebach (3.6) at $N_{\rm gh}=2$.
With Zwiebach's constant $\eta=-1$, (C3) fails by a sign and the multiplier condition becomes
$\lambda_k^\ddagger=(-1)^k\lambda_k$; for $\eta=+1$ the sign flip moves to the even side instead
($\Psi^{\ddagger'}=-\Psi$, $\Sigma_k^{\ddagger'}=(-1)^k\Sigma_k$), so "with a constant $\eta$" is not a statement
about $\lambda_k$ alone. If the $\lambda_k$ carry commuting coefficients they are in the situation of the classical
gauge parameter $\Lambda$ of Zwiebach (3.18) ($|\Lambda\rangle=\sum|\Phi_r\rangle\lambda_r$, odd state, commuting
coefficient, $\Lambda^{\ddagger'}=-\Lambda$), which his condition (3.6) does not cover: $\lambda_k^{\ddagger'}=\lambda_k$ then
rests on the equivariance of $\omega_k$, i.e. on the reality of $S_C$. This addendum did not read the
pedagogical note's §reality (outside the scope), so which reading it uses is not checked here.

*Proposed conventions-ledger entry (node-checked 2026-09-30; text as amended by the critic).*
"C3 — Reality conjugation. $\ddagger:=(-1)^{N_{\rm gh}+1}\,\mathrm{bpz}^{-1}\circ\mathrm{hc}$ on single-strand
states, extended componentwise to $\mathcal H_0^{\otimes k}$ (028 (C2)); $\ddagger^2=1$ (028 addendum P.3).
With it $\omega_1$ is equivariant, $\omega_1(A^\ddagger,B^\ddagger)=\omega_1(A,B)^*$, given Zwiebach (2.37) and
$s=+1$ (C1, R58); a constant sign makes it anti-equivariant. On a Grassmann-even total field whose coefficients
carry physical statistics, $X^\ddagger=X$ componentwise is Zwiebach (3.6); at $N_{\rm gh}=2$ it is Zwiebach's
condition itself (tachyon: $\phi^*(p)=\phi(-p)$). For an odd-$N_{\rm gh}$ object with commuting coefficients,
Zwiebach (3.18) (classical gauge parameter) reads $\Lambda^\ddagger=-\Lambda$ ($\Lambda^{\ddagger'}=-\Lambda$ in the
$\ddagger'$ notation); the Route C multipliers are declared $\lambda_k^\ddagger=\lambda_k$ because that makes $\omega_k$
equivariant and $S_C$ real. Checked on $A_1=c_1\bar c_1|0\rangle$, $B_1=c_0^+c_1\bar c_1|0\rangle$, both real."
Two further candidate qualifiers, unchanged: C1(iii) holds on normal-ordered words, and C1(ii) is the $I^-$ rule,
equal to the book's closed-string $I^+$ on level-matched states.

### P.7 Verification

Script `codes/verify-ph7-ddagger.py` (numpy; Jordan–Wigner on the 64-dim ghost space $n\in\{-1,0,1\}$,
and 256-dim with two Grassmann generators $\theta,\bar\theta$ for the coefficient layer). Run:
`.venv/bin/python codes/verify-ph7-ddagger.py`, seed 20260926, **35/35 PASS**, exit 0, log
`agent/scratch/ph7-run1.log`. The hc and BPZ matrices are built from the word rules (P-A1, P-A2), and
$K=(P^T)^{-1}G^T$ gives $\ddagger v=\eta K\bar v$.

- *Conventions reproduced:* N1, the $-\tfrac12$ in the $c_0^-c_0^+$ form from the $-1$ in the
  $c_0\bar c_0$ form (break: the $c_0^+c_0^-$ order gives $+\tfrac12$); N0, the vacua; C1, the mode
  tables equal the general formula; N2, $G^H=-G$, i.e. Zwiebach (2.37) (break: an $i$ in the
  normalisation gives $G^H=+G$); S1, $\omega_1(A_1,B_1)=\omega_1(B_1,A_1)=-\tfrac12$ (ledger C1).
- *Word rules versus the Clifford algebra:* H1 (hc, all twelve modes including $b_n$; break: graded
  hc fails); B1 (BPZ graded anti-automorphism, $I^\pm$; break: order-reversing BPZ is neither graded
  nor ungraded).
- *PH7:* P7.0 ($b_0^-$ kernel); P7.1 and P7.2 test the values (P.4) and (P.5) at complex $\alpha,\beta$
  (breaks: the opposite signs are rejected); P7.2b, $\eta=\pm1$; P7.3, $K\bar K=1$ on all 64 states for
  $I^+$ and $I^-$, plus random complex even and odd vectors; P7.4, $K$ diagonal with the signs of
  (P.2); P7.5, $I^\pm$ agree on level-matched states; P7.6, $\kappa\to3.7i\,\kappa$ leaves $K$ unchanged.
- *Order-reversing BPZ (positive checks):* R1a–R1c are positive checks of "the ordering changes $\ddagger$, not
  $\ddagger^2$"; the break leg for that ordering is `break-B1-order-reversing-bpz` (order-reversing BPZ is not an
  anti-automorphism). The order-reversing BPZ multiplies $\ddagger$ by $(-1)^{k(k-1)/2}$, so
  $B_1$ turns imaginary and $A_1$ real, while $\ddagger^2=1$ is unchanged. The brief expected the
  $\ddagger^2$ sign to flip; it does not, see (P.3).
- *Which checks can fail.* P7.3 ($K\bar K=1$) cannot fail under any real mode rule (with real mode coefficients
  $K$ is diagonal with entries $\pm1$ by construction): it is a plumbing check, and would detect only a complex phase
  in a mode rule, which is P.3's claim. Gr2 is the only leg that makes the $\ddagger^2$ test fail. The mode-sector
  falsifiers are P7.4 (sign formula of (P.2)), P7.1/P7.2 with their break legs, and H1/B1 with theirs.
- *The $\ddagger^2$ check can fail:* Gr2. With the graded c-number conjugation, $K\bar K=\mathrm{diag}\big((-1)^{|{\rm coef}|}\big)\ne1$
  is detected. Gr1 (standard conjugation, $K\bar K=1$ on 256 states) and Gr1b (formula (P.6) on all
  64 ghost words) are the positive legs.
- *Side finding:* S2a (anti-equivariance, constant $\eta$), S2b and S2c ($\ddagger'$), S3 (Zwiebach on
  the total field is $\ddagger'$, single strands; its break leg drops the odd-coefficient sign, which is Zwiebach's
  (3.18) sign for commuting coefficients, so it fails only for odd coefficients).

*Not verified by machine.* The matter sector, momentum and higher oscillators are argued in (P.1),
not checked: star maps each mode to a real multiple of itself, up to $p\to-p$. The pedagogical note's
convention was not read.

### Addendum status

Node check 2026-09-30 passed (`agent/reports/critic-028-ph7-node-20260930T233800.md`: P.3, P.5, P.6 hold); PH7 discharged;
fix pass 2026-10-01 applied the critic's wording edits (C3 text replaced, P.5/P.6/P.7 wording).
Addendum complete 2026-09-26 (P.0–P.7). PH7 holds: $\ddagger^2=+1$, and the deciding convention is
involutive c-number conjugation. Side finding P.6: 028 (C3) needs $\ddagger$ read as
$\ddagger'=(-1)^{N_{\rm gh}+1}\mathrm{bpz}^{-1}\circ\mathrm{hc}$, which is Zwiebach (3.6) on the total
field. Next: orchestrator. Ledger PH7, R35 and R13 wording, and conventions candidates C3 and C1
qualifiers. Report: `agent/reports/computator-ph7-20260926T102000.md`.

## Addendum 2026-11-10 — external review (SL(2,C) project)

Source: external review, SL(2,C) vertices and ghost-dilaton project, 2026-11-10 (`SL:` reports `critic-import-073a-20261110T171501`, `critic-import-073b-20261110T171502`), passed on in the message `inbox/done/2026-11-10-sl2c-vertices-ghost-dilaton-import-review-findings.md`.
Brief: `agent/briefs/active-computator-import-review-addenda-20261110T183258.md`.
Two wording and scope corrections; no result, number or check of this record changes.
The text above this heading is not edited; the corrected readings below supersede the wording at the places listed.
Notation: $\star:=\mathrm{bpz}^{-1}\circ\mathrm{hc}$ without sign, $\ddagger':=(-1)^{N_{\rm gh}+1}\star$ (conventions C3; 075, R81).

### A.1 (C1): which conjugation

*Statement corrected.* (C1) l. 41 writes $\ddagger=\mathrm{BPZ}\circ(\text{hermitian conjugation})$.
Every statement of this record that uses $\ddagger$ ($\Psi^\ddagger=\Psi$, $\omega_1$ equivariant (C3), $\lambda_k^\ddagger=\lambda_k$ (4.1), Step 4.2) holds for $\ddagger'$ and only for it: the bare $\star$ gives $\Psi^\star=-\Psi$ and an anti-equivariant $\omega_1$ (P.6, items 1–3).
With a constant sign the multiplier condition would read $\lambda_k^\ddagger=(-1)^k\lambda_k$ (P.6, l. 681–682), which contradicts (4.1) and R35's Scope.
So **read $\ddagger$ throughout as $\ddagger'$**.

*Status.* Already settled in this record: addendum P.6 (l. 656–700; the consequence paragraph l. 676–689, in particular l. 680 "Read literally, 028 (C1) … is $\eta=+1$"), the C3 text of l. 690–699, and the Status line of l. 742–750; in the ledger by conventions C3 and R35's Scope ("convention: $\ddagger$ is Zwiebach's (3.6) …, i.e. $(-1)^{N_{\rm gh}+1}\mathrm{bpz}^{-1}\circ\mathrm{hc}$").
The external review's point (premise 1 of the brief) is therefore not a new finding; this addendum only adds the pointer from (C1) to P.6.

*Places to read as $\ddagger'$* (grep `BPZ\|bpz`): l. 41 (C1); l. 309 ("if BPZ∘h.c. squared to $-1$ …", about $\ddagger^2$, unchanged by the sign, PH7 / P.3); l. 340 (the proposed ledger row "With $\ddagger=$ BPZ∘h.c.", superseded by R35's body, which already states $(-1)^{N_{\rm gh}+1}\mathrm{bpz}^{-1}\circ\mathrm{hc}$); l. 63 mentions "the BPZ inner product" only as the pairing and is not a statement about $\ddagger$.
Statement or justification: the statement of (C1) is corrected (the sign), the justifications of every node are unchanged.

### A.2 (H$_R$), eq. (1.1): all arguments versus Grassmann-even arguments

*Statement corrected.* Eq. (1.1), l. 75, is written for all arguments, $n\ge2$:
$V_n(A_1,\dots,A_n)^*=V_n(A_1^\ddagger,\dots,A_n^\ddagger)$.
On general arguments the correct form is the one with the Koszul sign,
$$V_n(A_1^{\ddagger'},\dots,A_n^{\ddagger'})=(-1)^{k_o(k_o-1)/2}\,V_n(A_1,\dots,A_n)^*,\tag{A.1}$$
$k_o$ the number of Grassmann-odd arguments; this is H1 of record 075 (= PH6 in its component form, with the sign already carried by PH6's annotation of 2026-10-01).
It reduces to (1.1) exactly when $k_o\in\{0,1\}$, in particular for Grassmann-even arguments, and (1.1) as written is false in general.

*Derivation of (A.1) from R81 (one line).* 075 (4.4) gives $V_n(A^\star)=(-1)^{n+\sum_{i<j}|A_i||A_j|}V_n(A)^*$ on the support, and $\sum_{i<j}|A_i||A_j|=k_o(k_o-1)/2$.
By $\ddagger'=(-1)^{N_{\rm gh}+1}\star$ on each strand and the support condition $\sum_iN_i=2n$ (the sphere correlator of $n$ closed vertex operators with $2(n-3)$ $b$-insertions has total ghost number 6), $V_n(A^{\ddagger'})=(-1)^{\sum_i(N_i+1)}V_n(A^\star)=(-1)^nV_n(A^\star)$, which gives (A.1); this is the cross-check at the end of 075 (4.4).

*Counter-example to the unsigned form (no hypothesis needed).* $V_2(A,B)=\langle A|c_0^-Q_B|B\rangle$ on ghost numbers $(N_A,N_B)=(1,3)$.
Ghost count: $1+3+1+1=6$ ($c_0^-$ and $Q_B$ add one each), so the sphere vacuum functional does not vanish; both arguments are Grassmann-odd, $k_o=2$.
075 (4.4) at $n=2$ (from C4.1 and C4.3, without H1) gives $V_2(A^\star,B^\star)=(-1)^{|B|}V_2(A,B)^*=-V_2(A,B)^*$, and $\ddagger'$ is $+\star$ on $N=1,3$ ($(-1)^{N+1}=+1$), hence $V_2(A^{\ddagger'},B^{\ddagger'})=-V_2(A,B)^*$, the factor $(-1)^{k_o(k_o-1)/2}=-1$ of (A.1).
The unsigned (1.1) would give $+$.

*Where this record's results stand.* (i) The tower uses only Grassmann-even arguments of $V_n$, $k_o=0$: every strand of $\Sigma_k$ ($N_{\rm gh}=2$, (C2)), $\Psi$ ($N_{\rm gh}=2$), $\chi$ ($\chi\in\mathrm{Sym}^2\mathcal H_0$, $N_{\rm gh}=4$, two strands of $N_{\rm gh}=2$, l. 201) and the sources $\sigma_n$ of Step 4.1.
So Lemma 1, (1.3), Steps 2.1–2.4, §3 and Step 4.1 use (H$_R$) only on the sector where (1.1) and (A.1) agree, and no verdict of §0 changes.
(ii) §4, the odd-$k$ multipliers $\lambda_k$ (odd strands, $N_{\rm gh}=3$ each): the multiplier term $\omega_k(\lambda_k,C_k)$ involves the pairing $\omega_k=\omega_1^{\otimes k}$, not a vertex $V_n$ on odd arguments, so (H$_R$) is not what it rests on; its input is the equivariance of $\omega_1$ read with $\ddagger'$ (C3, P.6; on every nonvanishing pair, the strands being (odd, even) since $N_A+N_B=5$) and the componentwise convention (C2).
The Koszul-type sign of odd-strand tensors is already carried at the places that this record's Step 4.3 and addendum P.3 name: the reversed-order shift $(-1)^{k(k-1)/2}$ of Step 4.3 item 1 (the same sign as (A.1) with $k_o=k$), the Grassmann-layer rule of item 2, and $\ddagger^2=1$ (PH7, P.3 with the factor $(-1)^{k_o(k_o-1)/2}$ in l. 554–560).
So §4 is not affected and its verdict (c) stays as stated: $\lambda_k^\ddagger=\lambda_k$ in the componentwise convention, Conditional(PH6) – Proven at odd $k$ "with $\ddagger$ as in conventions C3".
The PH6 annotation of 2026-10-01 says R35 "was not rechecked against the signed form": this addendum is that recheck, and R35 is unaffected.
(iii) The paper already restricts the vertex reality to even arguments (`paper/sections/02-2-quartic.tex` l. 54–60, eq. `eq:hs4:vertex-real`, "for even arguments", with the star form $(-1)^n$), consistent with (A.1) at $k_o=0$; nothing to change there.

*Restatements of (H$_R$) in this record* (grep `H\$_R\$\|(1.1)`), each to be read as "(1.1) on Grassmann-even arguments, (A.1) in general": l. 28 and l. 33 (§0 verdict table and its closing sentence); l. 70–81 ((C4), eq. (1.1) at l. 75 is the one unsigned display; l. 81 "Everything below is conditional on (1.1)"); l. 92–93 ("(H$_R$) is the statement that each $V_n$ is equivariant"); l. 102 ((1.3), arguments are tensors of even strands); l. 132, 136, 149 (Steps 2.1, 2.2); l. 196, 210 (check 2.5 text and Step 3.1); l. 261–262 (Step 4.1, $\sigma_n$ even); l. 323, 327 (hand-off and "What was not done" (i)); l. 342, 350, 356 (the proposed ledger text, the row's verification column and the R24 flag); l. 402 ("Not machine-checked: (H$_R$) itself; the Grassmann-odd sector").
Statement or justification: the *statement* of (H$_R$) is corrected (all arguments → even arguments, general form (A.1)); the justification and every dependent node are unchanged, because they use $k_o=0$ only.
The script `codes/verify-reality-tower.py` (finite-dimensional toy, commuting components, even sector) is not touched and tests no odd argument; it is not re-run.

### Proposed ledger annotation for R35

An external review (SL(2,C) vertices and ghost-dilaton project, 2026-11-10; `SL:` reports `critic-import-073a-20261110T171501`, `critic-import-073b-20261110T171502`) found two wordings of this entry's source (028) too strong. (i) (H$_R$), $V_n(A_i)^*=V_n(A_i^\ddagger)$, is stated for all arguments; as written it holds for Grassmann-even arguments only: on general arguments the correct form is $V_n(A_i^{\ddagger'})=(-1)^{k_o(k_o-1)/2}V_n(A_i)^*$, $k_o$ the number of Grassmann-odd arguments, i.e. H1 of record 075 (R81) with the Koszul sign (counter-example to the unsigned form: $V_2(A,B)=\langle A|c_0^-Q_B|B\rangle$ on ghost numbers $(1,3)$, sign $-1$); the tower (every strand of $\Sigma_k$, $\Psi$, $\chi$, $\sigma_n$) uses even arguments only, and the odd-$k$ multipliers rest on the equivariance of the pairing, not of a vertex on odd arguments, so (H$_R$) is meant in this entry on the even sector, where nothing changes. (ii) Record 028 (C1) writes $\ddagger=\mathrm{BPZ}\circ\mathrm{hc}$; every statement of the entry holds for $\ddagger'=(-1)^{N_{\rm gh}+1}\mathrm{bpz}^{-1}\circ\mathrm{hc}$ (the entry's body and Scope already say so, conventions C3), the bare $\mathrm{bpz}^{-1}\circ\mathrm{hc}$ giving $\Psi^\star=-\Psi$ and an anti-equivariant pairing. No result, status tag or number of the entry changes; the PH6 annotation of 2026-10-01 (signed form) is the same correction, and R35 is thereby rechecked against it.

### Status of the 2026-11-10 addendum

Status line of this addendum: complete 2026-11-10; next: orchestrator (ledger clerk copies the annotation for R35).
