# Derivation 053 — GAP-3d, part A: the $\Sigma_2$ gauge algebra at $O(g_s^4)$ (sextic action): constraints, admissible family, defect formula, removability criterion

## 0. Task and objective

**Literal task** (brief `computator-gauge-ogs4-a-20260926T023500`). Redo the analysis of 043
§2–§4 (constraint enumeration, admissible family of the $\Sigma_2$ gauge law, curvature
reading of the closure defect) for the sextic-truncated action $S_4$ of R19/013, whose exact
rewriting around the saddle is (013 §4, §6)
$$
S_4=S^{(6)}_{\rm eff}(\Psi)+\Phi^*(Y;\Psi)+\mathbb F_5(\Psi),\qquad
\Phi^*(Y;\Psi)=-\tfrac{g_s^2}{4!}\mathcal K(Y,Y)+\tfrac{g_s^4}{6!}T(Y,Y,Y),\qquad
Y=\Sigma_2-\Sigma_*(\Psi),
\tag{0.1}
$$
and state, for part B, a removability criterion with the invariants and the finite-model
design that test it.

**Motivating objective.** The paper presents the theory through the sextic order, but the
closure of the $\Sigma_2$ gauge algebra "modulo the $\Psi$ equation of motion alone" (043,
R45 carve-out) is established only within the quintic-truncated action $S_3$, whose
auxiliary sector is a pure quadratic form. Either verdict at $O(g_s^4)$ — closure modulo the
$\Psi$ EOM alone (a flat representative exists) or closure only modulo both EOMs (a proven
obstruction) — is a consistent statement; the silence is not.

**Scope (A1 of 043, cited).** Algebraic layer: finite-dimensional $\mathcal H_0$, generic
totally symmetric tensors $\mathcal V_4,\mathcal V_5,\mathcal V_6$ (PH14 for the transfer to
string vertices; PH1/PH5 for the nondegeneracy of $p_{2,2}$ on the quotient), formal power
series in $g_s$, $Y\in V:=\operatorname{Sym}^2\mathcal H_0/\ker\mathcal V_4$, $D:=\dim V$.
Conventions of 040 §1 and 043 §1 (physical ghost number, degree parity, R43 normalisation),
cited and not re-declared; there is no `knowledge/conventions.md` in this project.

**Reading of the brief adopted (stated up front, justified in §2–§3).** The brief expects
the freedom to collapse to the stabiliser of $T$ inside $\mathfrak k_{\mathcal K}$ and
proposes, as part-B falsifier, $\Psi$-dependence of the $\mathrm{GL}$-invariants of the
cubic tensor in the $\mathcal K$-orthonormal frame. Both presuppose that the law and the
field redefinition are **linear in $Y$**. 043 §2 item 4 already records that linearity in
$\tilde X$ is *not* forced, and at $O(g_s^4)$ the forced part of the law is itself
nonlinear in $Y$ (R19's law is a Neumann series in $Y$). The enumeration of §2 therefore
does not impose linearity, and §3 and §5 derive the consequences: the freedom does not
collapse, and the removability question is one of *right-equivalence of the function
$\Phi^*(\cdot;\Psi)$ under $\Psi$-dependent formal diffeomorphisms of $V$ fixing $0$*, for
which the invariants of the brief are not invariants. This is a redirect of items 3 and 5,
not a change of the objective; the brief's linear-sector expectation is recorded as a
sub-case in §3.

## Claim tree

- **A1** Scope of 043 A1 extended to $\mathcal V_6$: finite model, generic tensors, formal
  series in $g_s$; $p:=p_{2,2}$ nondegenerate on $V$ (PH1/PH5).
- **A2** Conventions of 040 §1 / 043 §1 (cited).
- **A3** The exact rewriting (0.1) of 013 §4/§6 (R19, kind (c)): $\mathcal K(\Psi)$ is the
  saddle Hessian, $T=\mathcal V_6-\tfrac65\mathcal C$ is $\Psi$-**independent**, $\Phi^*$ is
  exactly cubic in $Y$, and $\mathbb F_5$ is $Y$-independent.
- **A4** $\mathcal K(\Psi)^{-1}$ and $M_{\mathcal K}^{\pm1/2}$ (with $\mathcal K=pM_{\mathcal
  K}$) exist as formal power series in $g_s$ with polynomial coefficients (Neumann; 013
  check 0, 043 A4).
- **C1** Under PH14, PH1, PH5 (finite model), the admissible $\Sigma_2$ gauge laws at
  $O(g_s^4)$ form the affine space $F_u=F^{(19)}_u+\mathcal K^{-1}S_u(Y)\nu(Y)$,
  $S_u^{\rm T}=-S_u$ (boxed, §3), and the freedom does **not** collapse. [by C1.1–C1.4]
  - **C1.1** The invariance condition is the single identity (3.2), affine-linear in $F_u$,
    whose degree-$k$ part (3.5) couples $F^{(k-1)}$ to $F^{(k-2)}$; R19's law is a
    particular solution. [by A3, A4; eqs. (3.2)–(3.3), (3.5)] [check: C1.1 — PASS (part B, §7); sanity (a)]
  - **C1.2** No $Y$-linear law is admissible for generic $T$: (3.7) is overdetermined
    ($\binom{D+2}3>\tfrac{D(D-1)}2$) and its source is generically outside the image. [by
    A1, C1.1; eq. (3.7)] [check: C1.2 — PASS at $D=3,6$ (part B, §7); sanity (c) at $D=3$]
  - **C1.3** The kernel is $\mathfrak{stab}(\Phi^*)=\{\mathcal K^{-1}S(Y)\nu(Y)\}$, $S$
    antisymmetric (Koszul exactness), equal to the trivial symmetries $\mu E_\Sigma$ with
    $\mu$ antisymmetric; at $T\to0$ it reduces to 043 (3.2)–(3.3). [by A4, C1.1; eqs. (3.1),
    (3.4)] [check: C1.3 — PASS (part B, §7); sanity (b)]
  - **C1.4** The freedom at degree $k-1$ in $Y$ is $\ker\sigma_k$, dimension (3.6), the same
    as at $T=0$; the chain (3.5) is solvable at every degree because $\sigma_k$ is onto.
    [by C1.1; eq. (3.6)] [by counting; solvability corroborated by C3.1 — PASS (the recursion
    (5.3) solvable to $n=10$, part B, §7)]
- **C2** Under PH14, PH1, PH5, the closure defect of any admissible law is the curvature
  (4.1) of the Ehresmann connection $H_u=\partial_u+F_u$ with structure group the formal
  diffeomorphisms of $V$ fixing $0$; it is exactly a trivial symmetry (4.3); for R19's law
  $\mathcal E_4=\mathcal E_3+\Delta\mathcal E$ with $\Delta\mathcal E=O(g_s^3)$ (4.6). [by
  C2.1–C2.3]
  - **C2.1** Formula (4.1) and its curvature reading (4.2); $\mathcal E_4\in
    \mathfrak{stab}(\Phi^*)$ (4.3). [by A2, C1.3; eqs. (4.1)–(4.3)] [check: C2.1 — PASS (part B, §7)]
  - **C2.2** For R19's law $\mathcal E^{(1)}_4=[R^{(19)}_{u_1},R^{(19)}_{u_2}]Y$ exactly,
    and the linear-sector shift from 043 is (4.7), $O(g_s^3)$, $\mathfrak k$-valued. [by
    C2.1; eqs. (1.3), (4.5)–(4.7)] [check: C2.2 — PASS, exact Taylor coefficients (part B, §7)]
  - **C2.3** The $Y$-quadratic sector of $\mathcal E_4$ starts at $O(g_s^4)$ with leading
    term (4.8), consistent with (3.5) at $k=3$. [by C2.1; eqs. (4.4b), (4.8)] [check: C2.3
    — PASS (part B, run 7, §7); second coefficient of (4.8) corrected on the fix pass
    (hand re-derivations in §7 and by the critic agree with the machine)]
- **C3** Under PH14, PH1, PH5, a flat admissible representative exists at $O(g_s^4)$ within
  $S_4$: the Morse map $\hat Y=G_\Psi(Y)$ of (5.4)–(5.5) makes $\Phi^*$ $\Psi$-independent,
  and $F^{\rm flat}$ of (5.6) is admissible, flat, and differs from R19's law by a trivial
  symmetry; hence (5.7): the algebra closes modulo the $\Psi$ equation of motion alone. The
  brief's invariants of $\hat T_\Psi$ are invariants of linear equivalence only and do not
  obstruct. [by C3.1–C3.3]
  - **C3.1** Existence and explicit recursion (5.3)–(5.4) of $G_\Psi$, algebraic at each
    order in $g_s$; (5.5). [by A4, C1.4; eqs. (5.2)–(5.5)] [check: C3.1 — PASS (part B, §7); sanity
    (d) for $q_2$]
  - **C3.2** Criterion: flat admissible representative $\Leftrightarrow$ $\Psi$-dependent
    admissible $G_\Psi$ with $\Phi^*\circ G_\Psi^{-1}$ $\Psi$-independent $\Leftrightarrow$
    the germs $\Phi^*(\cdot;\Psi)$ are right-equivalent $\Leftrightarrow$ (5.1) (Morse
    lemma with parameters, context; the $\Leftarrow$ direction used by C3.3 is supplied by
    the explicit construction (5.3)–(5.6)). [by C1.1, C2.1; §5 *Criterion*, *Invariant
    form*] [check: C3.2-expansion — PASS (the $Y$-quadratic sector of $F^{\rm flat}$ against
    the corrected (5.6), part B run 7, §7)]
  - **C3.3** $F^{\rm flat}=-(DG)^{-1}\partial_uG$ is flat by (4.2) and admissible by (5.5);
    the closure statement (5.7). [by C2.1, C3.1, C3.2; eqs. (5.6)–(5.7)] [check: C3 — PASS (part B, §7)]
    (fix pass: the displayed expansion in (5.6) corrected — justification changed, statement
    of C3.3 unchanged, since $F^{\rm flat}$ is defined and checked as $-(DG)^{-1}\partial_uG$)

Open gaps: none
Hypotheses in force: PH14, PH1, PH5

## 1. Notation, objects, orders

All objects live on $V=\operatorname{Sym}^2\mathcal H_0/\ker\mathcal V_4$; bilinear forms
are identified with maps $V\to V^*$; for an operator $N$ on $V$, $N^\star:=p^{-1}N^{\rm T}p$
is the $p$-adjoint and $\mathfrak p,\mathfrak k$ the $p$-symmetric and $p$-antisymmetric
operators (043 §1).

| Symbol | Definition | Order in $g_s$ (relative to $p=\mathcal V_4$) | Source |
|---|---|---|---|
| $P$ | $\Psi\otimes\Psi$ | $0$ | 013 |
| $P_u$, $A_u$ | $p_{3,2}(\cdot,\cdot,u)$, $p^{-1}P_u$ | $0$ | 043 §1 |
| $K_\Psi=pM_\Psi$ | $p-\tfrac{g_s}{5}P_\Psi$ | $1+O(g_s)$ | 043 §1 |
| $v$ | $p_{3,2}(\cdot,P,\Psi)$ | $0$ | R17 |
| $T$ | $\mathcal V_6-\tfrac65\mathcal C$, symmetric trilinear on $V$, **$\Psi$-independent** | $0$ | 013 §3 |
| $B_w$ | $p^{-1}T(\cdot,\cdot,w)$, $w\in V$; $B_w\in\mathfrak p$ | $0$ | new (local) |
| $K_6$ | $K_\Psi-\tfrac{g_s^2}{10}T(\cdot,\cdot,P)$ | $1+O(g_s)+O(g_s^2)$ | 013 §4 |
| $X_*$ | $\Sigma_*-P=\tfrac{g_s}{5}K_\Psi^{-1}v+O(g_s^2)$ | $O(g_s)$ | R17, 013 §4 |
| $\mathcal K$ | $K_6-\tfrac{g_s^2}{10}T(\cdot,\cdot,X_*)$, saddle Hessian | $1+O(g_s)+O(g_s^2)+O(g_s^3)$ | 013 §6 |
| $M_{\mathcal K}$ | $p^{-1}\mathcal K=M_\Psi-\tfrac{g_s^2}{10}B_P-\tfrac{g_s^3}{50}B_{K_\Psi^{-1}v}+O(g_s^4)$; $M_{\mathcal K}^\star=M_{\mathcal K}$ | as above | (1.1) |
| $Y$ | $\Sigma_2-\Sigma_*(\Psi)$; the exact-variable counterpart of 043's $\tilde X$ | field | 013 §6 |
| $\Phi^*(Y;\Psi)$ | $-\tfrac{g_s^2}{24}\mathcal K(Y,Y)+\tfrac{g_s^4}{720}T(Y,Y,Y)$ | cubic term $O(g_s^2)$ relative to the quadratic | (0.1) |
| $F_u(Y)$ | a gauge law $\delta Y=F_u(Y)$, $\delta\Psi=u$; $F$ linear in $u$ | — | §2 |
| $R^{(19)}_u$ | $-\tfrac12\mathcal K^{-1}\partial_u\mathcal K$, the $Y$-linear part of R19's law | $O(g_s)$ | (1.3) |
| $T_Y$ | the operator $\mathcal K^{-1}T(\cdot,Y,\cdot)$ on $V$, linear in $Y$ | $0$ | (1.2) |
| $F^{(19)}_u(Y)$ | $\big(1-\tfrac{g_s^2}{20}T_Y\big)^{-1}R^{(19)}_uY$, R19's law solved | $O(g_s)$; degree $n{+}1$ in $Y$ at relative $O(g_s^{2n})$ | (1.2) |

**Explicit expansions.** Writing $\partial_uP=2\,u\odot\Psi$,
$$
\mathcal K=p-\tfrac{g_s}{5}P_\Psi-\tfrac{g_s^2}{10}T(\cdot,\cdot,P)
-\tfrac{g_s^3}{50}T(\cdot,\cdot,K_\Psi^{-1}v)+O(g_s^4),
\tag{1.1}
$$
$$
F^{(19)}_u(Y)=R^{(19)}_uY+\tfrac{g_s^2}{20}\,\mathcal K^{-1}T\big(\cdot,Y,R^{(19)}_uY\big)
+\tfrac{g_s^4}{400}\,\mathcal K^{-1}T\big(\cdot,Y,\mathcal K^{-1}T(\cdot,Y,R^{(19)}_uY)\big)+\dots ,
\tag{1.2}
$$
$$
R^{(19)}_u=-\tfrac12\mathcal K^{-1}\partial_u\mathcal K
=\tfrac{g_s}{10}A_u+\tfrac{g_s^2}{50}A_\Psi A_u+\tfrac{g_s^2}{10}B_{u\odot\Psi}+O(g_s^3)
=R^{(17)}_u+\delta R_u,\qquad
\delta R_u=\tfrac{g_s^2}{10}B_{u\odot\Psi}+\delta R^{(3)}_u+O(g_s^4),
\tag{1.3}
$$
$$
\delta R^{(3)}_u=\tfrac{g_s^3}{100}B_{p^{-1}\partial_uv}+\tfrac{g_s^3}{50}A_\Psi B_{u\odot\Psi}
+\tfrac{g_s^3}{100}B_PA_u,\qquad
\partial_uv=2p_{3,2}(\cdot,u\odot\Psi,\Psi)+p_{3,2}(\cdot,P,u).
\tag{1.3'}
$$
(1.2) is the Neumann solution of the boxed implicit law of 013 §0,
$\delta Y=\mathcal K^{-1}[-\tfrac12(\delta\mathcal K)(\cdot,Y)+\tfrac{g_s^2}{20}T(\cdot,Y,\delta Y)]$:
the law is a **power series in $Y$**, the degree-$(n{+}1)$ term carrying $g_s^{1+2n}$. (1.3)
follows from $\partial_u\mathcal K=-\tfrac{g_s}{5}P_u-\tfrac{g_s^2}{5}T(\cdot,\cdot,u\odot\Psi)
+O(g_s^3)$ and $\mathcal K^{-1}=p^{-1}(1+\tfrac{g_s}{5}A_\Psi+O(g_s^2))$; the $O(g_s^2)$
term $\tfrac{g_s^2}{50}A_\Psi A_u$ is the one already present in R17's
$-\tfrac12M_\Psi^{-1}\partial_uM_\Psi$ (043 (3.4)), so the **new** $O(g_s^2)$ piece is
$\tfrac{g_s^2}{10}B_{u\odot\Psi}\in\mathfrak p$. (1.3') is the $g_s^3$ part of
$\tfrac12(1+\epsilon+\epsilon^2)\partial_u\epsilon$ with $\mathcal K=p(1-\epsilon)$,
$\epsilon=\tfrac{g_s}{5}A_\Psi+\tfrac{g_s^2}{10}B_P+\tfrac{g_s^3}{50}B_{p^{-1}v}+O(g_s^4)$,
minus R17's $\tfrac{g_s^3}{250}A_\Psi^2A_u$.

**Orders, summarised.** Relative to the leading quadratic form $p(Y,Y)$: the $\Psi$-dressing
of the Hessian enters at $g_s^1$ ($\mathcal V_5$), $g_s^2$ ($T$ through $P$) and $g_s^3$ ($T$
through $X_*$); the cubic self-interaction at $g_s^2$. In the law: the linear part is
$O(g_s)$ with $T$-corrections from $O(g_s^2)$; the quadratic part is $O(g_s^3)$; the cubic
part $O(g_s^5)$. 043's variables map as $\tilde X\to Y$, $K_\Psi\to\mathcal K$,
$M_\Psi\to M_{\mathcal K}$, $R^{(17)}_u\to R^{(19)}_u$ plus the nonlinear tail of (1.2).

## 2. The constraints on the law $F_u$ — enumeration

Written before any computation, one line each with the justification and whether it is
forced. The unknown is a gauge law $\delta Y=F_u(Y)$, $\delta\Psi=u$, on $S_4$ around the
exact saddle; 043's $\Delta R_u$ is the special case $F_u(Y)=(R_u+\Delta R_u)Y$.

1. **Invariance of $\Phi^*$** — by A3, $S_4$ depends on $Y$ only through $\Phi^*(Y;\Psi)$,
   so gauge invariance of $S_4$ through $O(g_s^4)$ ($\delta S^{(6)}_{\rm eff}=0$ by the
   $L_\infty$ law for $\Psi$, $\delta\mathbb F_5=O(g_s^5)$, R19 (6), 013 §6) reduces to
   $\delta\Phi^*=0$ for the $Y$-law, for arbitrary $u$; (2.1) is imposed exactly, because
   R19's law satisfies it exactly. The condition is
   $(\partial_u\Phi^*)(Y)+D_Y\Phi^*\cdot F_u(Y)=0$. **Forced.** Explicitly, with the
   $\Psi$-independence of $T$ (A3),
   $$
   -\tfrac{g_s^2}{24}(\partial_u\mathcal K)(Y,Y)-\tfrac{g_s^2}{12}\mathcal K\big(F_u(Y),Y\big)
   +\tfrac{g_s^4}{240}T\big(F_u(Y),Y,Y\big)=0 .
   \tag{2.1}
   $$
2. **(2.1) is one identity in $Y$; graded by degree it is a chain of conditions, not two.**
   Expanding $F_u(Y)=\sum_{n\ge0}F^{(n)}_u(Y^{\otimes n})$ ($F^{(n)}$ symmetric
   $n$-linear), the degree-$k$ part of (2.1) is: $k=1$: $\mathcal K(F^{(0)},Y)=0$;
   $k=2$: $\tfrac12(\partial_u\mathcal K)(Y,Y)+\mathcal K(F^{(1)}Y,Y)=0$; $k\ge3$:
   $\mathcal K(F^{(k-1)}(Y^{k-1}),Y)=\tfrac{g_s^2}{20}T(F^{(k-2)}(Y^{k-2}),Y,Y)$. The brief's
   "quadratic and cubic conditions" are $k=2,3$; the cubic one is *not* the last, because
   the cubic term of $\Phi^*$ feeds every $F^{(n)}$ into the next degree. **Forced** (a
   consequence of item 1, recorded because it decides item 4). Which part of $F$ each fixes:
   the degree-$k$ condition fixes the **totally symmetrised** $(k)$-form
   $\mathcal K(F^{(k-1)}(Y^{k-1}),Y)$ and nothing else (§3).
3. **Linearity in $\Lambda$, hence in $u$** — as 043 item 3. **Forced.** Invariance is
   demanded for arbitrary $u\in\mathcal H_0$, not only for $u$ in the image of the $\Psi$
   gauge law (same choice as 043); this can only shrink the admissible class, so C3 is
   unaffected.
4. **Homogeneity / polynomial degree in $Y$ is not forced** — 043 item 4 recorded this for
   $S_3$, where it was optional; here the chain of item 2 makes a $Y$-**nonlinear** law
   *mandatory* for generic $T$ (C1.2). So the family is sought among formal power series
   in $Y$ (with a Neumann-type radius, as R19's law itself). **Not imposed**; imposing
   "linear in $Y$" would give an empty family, and "linear plus quadratic" an
   over-constrained one that answers a smaller question (043's rule).
5. **Ghost number** — $N_{\rm gh}(Y)=4$, $N_{\rm gh}(u)=2$; $F^{(n)}_u$ must carry
   $N_{\rm gh}=4$ out of $n$ copies of $Y$ and one $u$. **Forced**; satisfied by anything
   built from $A_w$, $B_w$, $T_Y$, $\mathcal K^{-1}$ (each $T$-slot saturates as in 013 §0
   item 3).
6. **Grassmann parity** — $u$, $Y$ even; $F_u$ even; no reordering signs. **Forced.**
7. **$F_u=O(g_s)$** — at $g_s^0$ the law reduces to $\delta Y=0$ (R11 rigid slaving).
   **Forced.**
8. **Reduction to 043 at $T\to0$** — at $T=0$, $\Phi^*$ is the quadratic form
   $K_\Psi(Y,Y)$, so the family must reduce to 043's $\{R^{(17)}_u+K_\Psi^{-1}S_u\}$
   (plus its unused nonlinear tail, 043 item 4). **Forced** (it is item 1 at $T=0$); used
   as a check of §3, not as a constraint.
9. **Algebraicity** — each order in $g_s$ polynomial in $\Psi$ and $Y$, built from
   $\mathcal V_{4,5,6}$, $\mathcal C$, $p^{-1}$ ($\mathcal K^{-1}$ as a Neumann series).
   **Imposed** (043 item 8, same reason); it restricts and can only strengthen a positive
   verdict.
10. **Quotient and reality** — as 043 item 9. **Forced**; satisfied by anything built from
    the listed blocks.
11. **Nothing else.** In particular the law is not required to be linear in $Y$ (item 4),
    not required to have $\Psi$-independent coefficients, and the *redefinition* of §5 is
    not required to be linear either: a field redefinition $\hat Y=G_\Psi(Y)$ is admissible
    iff it is an invertible formal series in $Y$ with $G_\Psi(0)=0$ obeying items 5, 6, 9,
    10 — the same class as the laws.

**What changes relative to 043.** Items 1, 3, 5–7, 9, 10 are unchanged in content. The
substantive change is item 2/4: the invariance identity is no longer a statement about a
quadratic form, so it no longer terminates at the $\mathcal K$-antisymmetric part of a single
operator; and the class of admissible objects (laws and redefinitions) is the group of
formal diffeomorphisms of $V$ fixing $0$ rather than $\mathrm{GL}(V)$. The brief's expected
collapse to $\mathfrak k_{\mathcal K}\cap\mathfrak{stab}(T)$ is what item 2 gives if item 4
is *imposed* as "linear in $Y$" — recorded in §3 as the linear sub-case, together with the
reason it is empty.

## 3. The admissible family, exactly (C1)

### Setup

A1–A4 and the constraints of §2. Local symbols: $\partial_u$ the directional derivative on
$\Psi$-space at fixed $Y$; $T_Y:=\mathcal K^{-1}T(\cdot,Y,\cdot)$, an operator on $V$
linear in $Y$ and $\mathcal K$-self-adjoint ($\mathcal K(w,T_Yw')=T(w,Y,w')$); and the
**gradient vector field**
$$
\nu(Y):=Y-\tfrac{g_s^2}{20}\,\mathcal K^{-1}T(\cdot,Y,Y)
=-\tfrac{12}{g_s^2}\,\mathcal K^{-1}\,\frac{\partial\Phi^*}{\partial Y},
\tag{3.1}
$$
so that $D_Y\Phi^*\cdot w=-\tfrac{g_s^2}{12}\,\mathcal K(\nu(Y),w)$ for every $w\in V$, and
$E_\Sigma=\partial\Phi^*/\partial Y=-\tfrac{g_s^2}{12}\mathcal K\nu(Y)$ is the $\Sigma_2$
equation of motion.

### Derivation

The invariance condition (2.1), divided by $-\tfrac{g_s^2}{12}$, is
$$
\mathcal K\big(\nu(Y),F_u(Y)\big)=-\tfrac12\,(\partial_u\mathcal K)(Y,Y)
\qquad\text{for all }Y .
\tag{3.2}
$$
It is affine-linear in the unknown $F_u$; the family is a particular solution plus the
kernel.

*Particular solution.* R19's law (1.2), $F^{(19)}_u=(1-\tfrac{g_s^2}{20}T_Y)^{-1}R^{(19)}_uY$,
satisfies (3.2): since $\mathcal K(\nu(Y),w)=\mathcal K(Y,w)-\tfrac{g_s^2}{20}T(Y,Y,w)
=\mathcal K\big(Y,(1-\tfrac{g_s^2}{20}T_Y)w\big)$,
$$
\mathcal K\big(\nu(Y),F^{(19)}_u(Y)\big)=\mathcal K\big(Y,R^{(19)}_uY\big)
=-\tfrac12(\partial_u\mathcal K)(Y,Y),
\tag{3.3}
$$
the last step by $R^{(19)}_u=-\tfrac12\mathcal K^{-1}\partial_u\mathcal K$. This is 013 §6's
verification, rewritten through $\nu$.

*Kernel.* The homogeneous equation $\mathcal K(\nu(Y),F(Y))=0$ says that $F$ is a formal
vector field on $V$ tangent to the level sets of $\Phi^*(\cdot;\Psi)$, i.e. $F\in
\mathfrak{stab}(\Phi^*)$. Since $\nu(Y)=Y+O(Y^2)$, the components $z_i:=(\mathcal K\nu(Y))_i$
are formal coordinates on $V$ (invertible Jacobian at $0$), and the equation reads
$\sum_iz_iF^i(z)=0$ in $k[[z_1,\dots,z_D]]$, $k=\mathbb Q[\Psi][[g_s]]$ (the change of
coordinates $Y\mapsto z=\mathcal K\nu(Y)$ is invertible over $k$ by A4). In
$k[[z_1,\dots,z_D]]$, for any commutative ring $k$, each $z_i$ is a non-zero-divisor modulo
$(z_1,\dots,z_{i-1})$, since the quotient is $k[[z_i,\dots,z_D]]$; so $(z_1,\dots,z_D)$ is a
regular sequence and the first homology of its Koszul complex vanishes (Eisenbud,
*Commutative Algebra*, Cor. 17.5), i.e. the kernel of $F\mapsto\sum_iz_iF^i$ consists of the
antisymmetric combinations. So the general solution is $F^i=\sum_ja^{ij}(z)z_j$ with
$a^{ij}=-a^{ji}$ formal series. Writing $S:=\mathcal Ka\mathcal K$ (an antisymmetric bilinear
form on $V$, $Y$-dependent),
$$
\mathfrak{stab}(\Phi^*)=\big\{\,F(Y)=\mathcal K^{-1}S(Y)\,\nu(Y)\ :\ S(Y)^{\rm T}=-S(Y)\,\big\} .
\tag{3.4}
$$
Conversely every such $F$ is in the kernel: $\mathcal K(\nu,\mathcal K^{-1}S\nu)=S(\nu,\nu)=0$.

*Graded structure and dimension count.* Expanding $F_u=\sum_nF^{(n)}_u$, the degree-$k$ part
of (3.2) is (§2 item 2)
$$
\operatorname{Sym}_{k}\!\Big[\mathcal K\big(F^{(k-1)}_u(Y^{k-1}),Y\big)\Big]
=\delta_{k,2}\big(-\tfrac12\partial_u\mathcal K(Y,Y)\big)
+\tfrac{g_s^2}{20}\operatorname{Sym}_k\!\Big[T\big(F^{(k-2)}_u(Y^{k-2}),Y,Y\big)\Big],
\qquad k\ge1 ,
\tag{3.5}
$$
where $\operatorname{Sym}_k$ is total symmetrisation of a $k$-form and $F^{(-1)}:=0$. At
every $k$ the left side is the image of $F^{(k-1)}$ under the surjection
$\sigma_k:\operatorname{Sym}^{k-1}V\otimes V\to\operatorname{Sym}^kV$ (composition with
$\mathcal K$ and symmetrisation), so (3.5) is *always solvable* for $F^{(k-1)}$ whatever
$F^{(k-2)}$ is, and the freedom at degree $k-1$ is $\ker\sigma_k$:
$$
\dim\ker\sigma_k=D\binom{D+k-2}{k-1}-\binom{D+k-1}{k},\qquad
\dim\ker\sigma_2=\tfrac{D(D-1)}{2},\quad\dim\ker\sigma_3=\tfrac{D(D-1)(D+1)}{3}.
\tag{3.6}
$$
The counts are those of the $T=0$ problem: $T$ enters (3.5) only through the source, which
shifts the particular solution degree by degree and never restricts the kernel. (3.6)
agrees with the Koszul count from (3.4) ($S$ of degree $k-2$ in $Y$, modulo the second
Koszul syzygies), e.g. at $k=3$: $\tfrac{D(D-1)}2D-\binom D3=\tfrac{D(D-1)(D+1)}3$.

*The linear sub-case (the brief's expected shape), for the record.* If $F_u=\hat R_uY$ is
imposed, (3.5) at $k=2$ gives $\hat R_u=R^{(19)}_u+\mathcal K^{-1}S_u$, $S_u^{\rm T}=-S_u$,
and at $k=3$ (with $F^{(2)}=0$) the extra condition
$$
\operatorname{Sym}_3\big[T(\mathcal K^{-1}S_uY,Y,Y)\big]
=-\operatorname{Sym}_3\big[T(R^{(19)}_uY,Y,Y)\big]
=-\tfrac{g_s}{10}\operatorname{Sym}_3\big[T(A_uY,Y,Y)\big]+O(g_s^2):
\tag{3.7}
$$
$\tfrac{D(D-1)}2$ unknowns against $\binom{D+2}{3}$ equations, and
$\binom{D+2}3>\tfrac{D(D-1)}2$ for every $D\ge1$. For generic $T$ and $A_u$ the right side is
not in the image of the left (checked numerically at $D=3$, §3 sanity evaluation:
least-squares residual of order one), so **no $Y$-linear law exists at all** (C1.2); the
homogeneous part of (3.7), $\mathfrak k_{\mathcal K}\cap\mathfrak{stab}(T)$, is $\{0\}$ by
the same count — this is the "collapse" the brief anticipated, and it is the collapse of an
empty family. The brief's expectation was right about the linear sector and wrong about the
premise: the forced part of the law is not linear.

*Reduction at $T\to0$ (§2 item 8).* $\nu\to Y$, $F^{(19)}\to R^{(17)}_uY$, and (3.4) becomes
$K_\Psi^{-1}S(Y)Y$: at degree one this is 043 (3.2)–(3.3), and the higher degrees are 043
§2 item 4's unused tail. ✓

*The hinge, again.* By (3.1), the freedom (3.4) is
$\mathcal K^{-1}S\nu=-\tfrac{12}{g_s^2}\,\mathcal K^{-1}S\mathcal K^{-1}E_\Sigma=\mu\,E_\Sigma$
with $\mu=-\tfrac{12}{g_s^2}\mathcal K^{-1}S(Y)\mathcal K^{-1}$ **antisymmetric** and now
field-dependent: exactly the Henneaux–Teitelboim trivial symmetries of $S_4$, as in 043 §2.
GAP-3d is again "is $\mathcal E_4$ removable by a trivial symmetry?".

### Commentary

- (3.1)–(3.2): the whole simplification is that a cubic $\Phi^*$ with nondegenerate Hessian
  has a gradient field $\nu$ that is a formal coordinate change; the invariance condition is
  then a *linear* statement about $F$ with respect to this one vector field.
- (3.4): Koszul exactness is the formal-power-series version of "a vector orthogonal to $\nu$
  is $S\nu$ with $S$ antisymmetric", valid across the locus $\mathcal K(\nu,\nu)=0$ (which
  exists for indefinite $\mathcal K$) because it is an algebraic, not a pointwise, statement.
- (3.5)–(3.6): the chain never obstructs because $\sigma_k$ is onto; this is the exact
  reason R19's implicit law has a solution to all orders, and the reason the freedom is
  unchanged by $T$.
- (3.7): the only place $T$ could restrict the freedom is if the law is forced to stop at a
  finite degree in $Y$; nothing forces that (§2 item 4).

### Result

$$
\boxed{\;
F_u(Y)=\underbrace{\big(1-\tfrac{g_s^2}{20}T_Y\big)^{-1}R^{(19)}_uY}_{F^{(19)}_u\ (\text{R19})}
\;+\;\mathcal K^{-1}S_u(Y)\,\nu(Y),
\qquad S_u(Y)^{\rm T}=-S_u(Y),\qquad
\nu(Y)=Y-\tfrac{g_s^2}{20}\mathcal K^{-1}T(\cdot,Y,Y)\;}
$$
— the admissible family at $O(g_s^4)$, exact in $g_s$ for the condition (2.1) (which is the
whole of gauge invariance of $S_4$ through $O(g_s^4)$, §2 item 1), with $S_u(Y)$ an
antisymmetric-form-valued formal series in $Y$, linear in $u$, $O(g_s)$, algebraic,
$N_{\rm gh}$-preserving and even. Dimension of the freedom at degree $k-1$ in $Y$:
$\dim\ker\sigma_k$ of (3.6), the same as at $T=0$; **no collapse**. The freedom is exactly the
set of trivial symmetries of $S_4$. No $Y$-linear law is admissible for generic $T$; the
brief's $\mathfrak k_{\mathcal K}\cap\mathfrak{stab}(T)$ is the (trivial) homogeneous part of
a family with no particular solution. [sanity evaluation: `agent/scratch/sanity-053.py`,
§3 items (a)–(c); part B owns the named checks]

## 4. The commutator defect $\mathcal E_4$ (C2)

### Setup

A1–A4, C1. Both $u_1,u_2$ Grassmann-even. A law is now a $\Psi$-dependent formal vector
field $F_u$ on $V$ (linear in $u$); $D_YF$ is its Jacobian; $[X,Z]_{\rm Lie}:=D_YZ\cdot X-
D_YX\cdot Z$ is the Lie bracket of vector fields on $V$. $\partial_u$ acts on the explicit
$\Psi$-dependence of $F$ at fixed $Y$ and fixed $u_{1,2}$; the $\Psi$-dependence of the
$u_i$ themselves is carried, as in 040 (5.11), by the $F_{[\delta_1,\delta_2]\Psi}$ term.

### Derivation

Applying $\delta_1$ to $\delta_2Y=F_{u_2}(Y;\Psi)$ and antisymmetrising,
$$
[\delta_1,\delta_2]Y=F_{[\delta_1,\delta_2]\Psi}(Y)+\mathcal E_4,\qquad
\mathcal E_4:=\partial_{u_1}F_{u_2}-\partial_{u_2}F_{u_1}+[F_{u_1},F_{u_2}]_{\rm Lie} ,
\tag{4.1}
$$
which for $F_u=\hat R_uY$ is 043 (4.1) (the map $\hat R\mapsto\hat RY$ from matrices to
linear vector fields is an anti-homomorphism, $[\hat R_1Y,\hat R_2Y]_{\rm Lie}=[\hat R_2,
\hat R_1]Y$). Geometrically: with the horizontal lifts $H_u:=\partial_u+F_u^i\partial_{Y^i}$
of the Ehresmann connection on $V\times\mathcal H_0\to\mathcal H_0$ whose horizontal curves
are the gauge orbits, $\mathcal E_4=[H_{u_1},H_{u_2}]$ for constant $u_1,u_2$ — the
**curvature** of a connection whose structure group is the group of formal diffeomorphisms
of $V$ fixing $0$, no longer $\mathrm{GL}(V)$. Flatness $\Leftrightarrow$ (Frobenius,
contractible base) there is a $\Psi$-dependent formal diffeomorphism $G_\Psi$ of $V$ with
$$
F_u=-\,(D_YG_\Psi)^{-1}\,\partial_uG_\Psi\qquad(\text{pure gauge}),\qquad
\text{equivalently }\ \delta\hat Y=0\ \text{ for }\ \hat Y:=G_\Psi(Y).
\tag{4.2}
$$
[Same argument as 043 §4's pure-gauge check: if (4.2) holds then $H_u(G_\Psi(Y))=0$ for all
$u$, so $[H_1,H_2]$ annihilates the coordinates $\hat Y$ and, being vertical, vanishes.]

**$\mathcal E_4$ is a trivial symmetry, exactly.** Each $\delta_i$ preserves $\Phi^*$
identically, hence so does $[\delta_1,\delta_2]$; and $F_w$ with $w=[\delta_1,\delta_2]\Psi$
satisfies (3.2) with $u\to w$. Subtracting, $D_Y\Phi^*\cdot\mathcal E_4=0$: by (3.4),
$$
\mathcal E_4=\mathcal K^{-1}\,\Xi_{12}(Y)\,\nu(Y)=\mu_{12}\,E_\Sigma ,\qquad
\Xi_{12}^{\rm T}=-\Xi_{12},\quad\mu_{12}=-\tfrac{12}{g_s^2}\mathcal K^{-1}\Xi_{12}\mathcal K^{-1},
\tag{4.3}
$$
the $O(g_s^4)$ form of R45's "exactly $\tilde X$-proportional": the defect is exactly
proportional to the $\Sigma_2$ equation of motion with an antisymmetric, field-dependent
coefficient. Part B checks (4.3) as a structural identity on the computed $\mathcal E_4$.

**Graded formula.** With $F_u(Y)=\hat R_uY+Q_u(Y,Y)+O(Y^3)$ ($Q_u$ symmetric bilinear),
$$
\mathcal E_4^{(1)}=\big(\partial_{u_1}\hat R_{u_2}-\partial_{u_2}\hat R_{u_1}
+[\hat R_{u_2},\hat R_{u_1}]\big)Y ,
\tag{4.4a}
$$
$$
\mathcal E_4^{(2)}=\partial_{u_1}Q_{u_2}(Y,Y)-\partial_{u_2}Q_{u_1}(Y,Y)
+2Q_{u_2}(Y,\hat R_{u_1}Y)-2Q_{u_1}(Y,\hat R_{u_2}Y)
+\hat R_{u_2}Q_{u_1}(Y,Y)-\hat R_{u_1}Q_{u_2}(Y,Y),
\tag{4.4b}
$$
and $\mathcal E_4^{(n)}$ for $n\ge3$ from (4.1) in the same way; (4.4b) is new at this order
(043's law had $Q=0$).

**R19's law.** Its linear part is the symmetric-logarithmic-derivative connection
$\hat R_u=R^{(19)}_u=-\tfrac12\mathcal K^{-1}\partial_u\mathcal K$ of the *saddle Hessian*.
For any such connection $\partial_{u_1}\hat R_{u_2}-\partial_{u_2}\hat R_{u_1}
=\tfrac12[\mathcal K^{-1}\partial_1\mathcal K,\mathcal K^{-1}\partial_2\mathcal K]
=2[\hat R_{u_1},\hat R_{u_2}]$ (the $\partial_1\partial_2\mathcal K$ term is symmetric and
drops), so
$$
\mathcal E_4^{(1)}\big|_{\rm R19}=\big[R^{(19)}_{u_1},R^{(19)}_{u_2}\big]Y
\quad\text{exactly},\qquad
\mathcal E_3=\big[R^{(17)}_{u_1},R^{(17)}_{u_2}\big]\tilde X=\tfrac{g_s^2}{100}[A_{u_1},A_{u_2}]\tilde X+O(g_s^3)
\ \ (\text{043 §4, R45}).
\tag{4.5}
$$
With $R^{(19)}=R^{(17)}+\delta R$ of (1.3),
$$
\boxed{\;
\mathcal E_4=\mathcal E_3+\Delta\mathcal E,\qquad
\Delta\mathcal E=\underbrace{\Big([R^{(17)}_{u_1},\delta R_{u_2}]+[\delta R_{u_1},R^{(17)}_{u_2}]
+[\delta R_{u_1},\delta R_{u_2}]\Big)Y}_{\text{linear sector, }O(g_s^3)}
+\underbrace{\mathcal E_4^{(2)}+O(Y^3)}_{O(g_s^4)}\;}
\tag{4.6}
$$
$$
\Delta\mathcal E\big|_{g_s^3}=\tfrac{g_s^3}{100}\Big([A_{u_1},B_{u_2\odot\Psi}]-[A_{u_2},B_{u_1\odot\Psi}]\Big)Y
\ \in\mathfrak k ,
\tag{4.7}
$$
using $[\mathfrak p,\mathfrak p]\subset\mathfrak k$ ($A_w,B_w\in\mathfrak p$). The quadratic
sector: $Q_u(Y,Y)=\tfrac{g_s^2}{20}\mathcal K^{-1}T(\cdot,Y,R^{(19)}_uY)
=\tfrac{g_s^3}{200}p^{-1}T(\cdot,Y,A_uY)+O(g_s^4)$ has no explicit $\Psi$ at leading order,
so every term of (4.4b) is $O(g_s^4)$: expanding (4.4b) with (1.3),
$$
\mathcal E_4^{(2)}\big|_{g_s^4}=\tfrac{g_s^4}{2000}\,p^{-1}T\big(\cdot,Y,[A_{u_1},A_{u_2}]Y\big)
-\tfrac{g_s^4}{2000}\Big(A_{u_2}p^{-1}T(\cdot,Y,A_{u_1}Y)-A_{u_1}p^{-1}T(\cdot,Y,A_{u_2}Y)\Big),
\tag{4.8}
$$
[coefficients confirmed exactly by part B's check `C2.3` (§7; the second coefficient was
first written $-\tfrac{19}{2000}$, corrected on the fix pass); the consistency test
$\operatorname{Sym}_3[\mathcal K(\mathcal E^{(2)}_4,Y)]=\tfrac{g_s^2}{20}\operatorname{Sym}_3
T(\mathcal E^{(1)}_4,Y,Y)$ — (3.5) at $k=3$ applied to $\mathcal E_4\in\mathfrak{stab}$ — is
satisfied by (4.8) at $g_s^4$: the second bracket is $p$-orthogonal to $Y$ because
$p(Y,A_2p^{-1}T(\cdot,Y,A_1Y))=T(A_2Y,Y,A_1Y)$ is $1\leftrightarrow2$ symmetric, and the
first gives $\tfrac{g_s^4}{2000}T(Y,Y,[A_1,A_2]Y)$ on both sides. This test is blind to
the second coefficient (the second bracket is $p$-orthogonal to $Y$ for any coefficient), so
it does not corroborate it; the exact Taylor check does.]

**Order summary.** $\mathcal E_4=\tfrac{g_s^2}{100}[A_{u_1},A_{u_2}]Y+O(g_s^3)$: the leading
defect is unchanged; the $T$-terms enter at $g_s^3$ in the linear sector (4.7) and at $g_s^4$
in the quadratic sector (4.8). Since $\delta R_u\in\mathfrak p+O(g_s^3)$, the
$\mathfrak k/\mathfrak p$ bookkeeping of 043 (4.5) survives: $\Delta\mathcal E|_{g_s^3}$ is
$\mathfrak k$-valued.

### Commentary

- (4.1)–(4.2): the structure of 043 §4 survives verbatim with $\mathrm{GL}(V)$ replaced by
  the formal diffeomorphism group; this is what makes §5's criterion a statement about
  right-equivalence of functions rather than congruence of matrices.
- (4.3) is the strongest structural constraint on $\mathcal E_4$ and costs nothing: it is
  the statement that the commutator of two symmetries of $\Phi^*$ is a symmetry. It fixes the
  form of every order of the defect up to an antisymmetric $\Xi_{12}(Y)$.
- (4.5): the simplification $\mathrm d\hat R=2\hat R\wedge\hat R$ holds for every
  symmetric-logarithmic-derivative connection, whatever the metric; 043's
  $\tfrac{g_s^2}{100}[A_1,A_2]$ is its leading term.
- (4.7)–(4.8) are sanity evaluations of the leading new terms, not the deliverable; part B
  computes $\mathcal E_4$ in the finite model with no expansion.

### Result

(4.1)–(4.3) exact; (4.6) the split $\mathcal E_4=\mathcal E_3+\Delta\mathcal E$ with
$\Delta\mathcal E=O(g_s^3)$, leading terms (4.7)–(4.8).

## 5. Removability criterion (C3) and the part-B design

### Setup

A1–A4, C1, C2. "Admissible redefinition": a $\Psi$-dependent formal diffeomorphism
$G_\Psi$ of $V$ with $G_\Psi(0)=0$ obeying §2 items 5, 6, 9, 10 (§2 item 11).

### Derivation

**Criterion.** *A flat admissible representative exists iff there is an admissible
$G_\Psi$ such that $\Phi_0(\hat Y):=\Phi^*(G_\Psi^{-1}(\hat Y);\Psi)$ is $\Psi$-independent.*
($\Leftarrow$) $F_u:=-(D_YG_\Psi)^{-1}\partial_uG_\Psi$ is flat by (4.2), and admissible
because $\Phi^*=\Phi_0\circ G_\Psi$ gives $\delta\Phi^*=D\Phi_0\cdot\delta\hat Y=0$.
($\Rightarrow$; standard, not used by C3.3, which needs only $\Leftarrow$) A flat law is
of the form (4.2) for some $G_\Psi$: order by order in $g_s$, flatness makes
$\partial_uG=-D_YG\cdot F_u$ a closed polynomial 1-form in $\Psi$ on a vector space, which
integrates to a polynomial $G$ (Frobenius on the contractible base; $G$ is built from the
law, hence admissible), and then
$\partial_u\big[\Phi^*(G_\Psi^{-1}(\hat Y);\Psi)\big]_{\hat Y}=\partial_u\Phi^*+D_Y\Phi^*\cdot F_u=0$
by (3.2). $\square$

**Invariant form.** The criterion says that the germs $\Phi^*(\cdot;\Psi)$, $\Psi\in
\mathcal H_0$, are all **right-equivalent** (under formal diffeomorphisms fixing $0$) to one
fixed germ, with the equivalence depending algebraically on $\Psi$. The complete invariant of
right-equivalence of a germ with **nondegenerate Hessian** is the linear-equivalence class of
its Hessian (Morse lemma; with parameters, the diffeomorphism depends polynomially on them at
each order in $g_s$; Arnold, Gusein-Zade and Varchenko, *Singularities of Differentiable
Maps* vol. 1, §11): over $\mathbb C$ nothing, over $\mathbb R$ the signature. This is
context: in the formal setting $M_{\mathcal K}=1+O(g_s)$ makes the signature clause
automatic, and the proof of C3 is the explicit construction (5.3)–(5.6) below, valid over
$\mathbb C$. So the
necessary and sufficient condition is
$$
\boxed{\;\mathcal K(\Psi)\ \text{nondegenerate on }V\ \text{for all }\Psi,\ \text{with
constant signature}\;}
\tag{5.1}
$$
— which holds: $\mathcal K=p\,M_{\mathcal K}$ with $M_{\mathcal K}=1+O(g_s)$ invertible as a
formal series (A4), and the signature of a continuous family of nondegenerate forms is
constant. **The cubic tensor $T$ carries no invariant of the problem.** In particular the
brief's $\hat T_\Psi=T(\mathcal K^{-1/2}\cdot,\mathcal K^{-1/2}\cdot,\mathcal K^{-1/2}\cdot)$
modulo $\mathrm O(\mathcal K)$ is the invariant of *linear* right-equivalence
($\mathrm{GL}(V)$), the wrong group: under $\hat Y=Y+q(Y,Y)$ the cubic part of $\Phi^*$ shifts
by $-\tfrac{g_s^2}{12}\mathcal K(q(Y,Y),Y)$, and $q\mapsto\operatorname{Sym}_3\mathcal K(q(Y,Y),Y)$
is onto $\operatorname{Sym}^3V^*$ ($\sigma_3$ of §3), so $\hat T_\Psi$ can be set to zero
identically. Its $\Psi$-dependence, generically present, would not have proven an
obstruction.

**Explicit construction of $G_\Psi$ (C3.1).** Write $\hat Y=G_\Psi(Y)=M_{\mathcal K}^{1/2}
\tilde G_\Psi(Y)$, $\tilde G_\Psi(Y)=Y+\sum_{n\ge2}q_n(Y^{\otimes n})$, and demand
$$
\mathcal K\big(\tilde G_\Psi(Y),\tilde G_\Psi(Y)\big)=\mathcal K(Y,Y)-\tfrac{g_s^2}{30}T(Y,Y,Y)
=-\tfrac{24}{g_s^2}\Phi^*(Y;\Psi).
\tag{5.2}
$$
The degree-$(n{+}1)$ part of (5.2) is
$$
2\,\mathcal K\big(q_n(Y^n),Y\big)=-\tfrac{g_s^2}{30}\,\delta_{n,2}\,T(Y,Y,Y)
-\sum_{\substack{a+b=n+1\\ a,b\ge2}}\mathcal K\big(q_a(Y^a),q_b(Y^b)\big),
\qquad n\ge2,
\tag{5.3}
$$
solvable for $q_n$ at every $n$ because $\sigma_{n+1}$ is onto (C1.4); the canonical
solution takes the right side as a symmetric $(n{+}1)$-form $\omega_{n+1}$ and sets
$q_n(Y^n)=\tfrac12\mathcal K^{-1}\omega_{n+1}(\cdot,Y^n)$, so
$$
q_2(Y,Y)=-\tfrac{g_s^2}{60}\,\mathcal K^{-1}T(\cdot,Y,Y),\qquad
q_3(Y^3)=-\tfrac12\,\mathcal K^{-1}\mathcal K\big(q_2(\cdot\,,Y),q_2(Y,Y)\big)\big|_{\rm sym}
=O(g_s^4),\qquad q_n=O(g_s^{2(n-1)}) .
\tag{5.4}
$$
Every $q_n$ is built from $\mathcal K^{-1}$ (Neumann) and $T$: algebraic, $N_{\rm gh}$- and
parity-preserving, quotient- and reality-compatible. Then, with $M_{\mathcal K}^{1/2}$ of A4
and $(M_{\mathcal K}^{1/2})^\star=M_{\mathcal K}^{1/2}$ (043 §5 with $M_\Psi\to M_{\mathcal K}$),
$$
\Phi^*(Y;\Psi)=-\tfrac{g_s^2}{24}\,\mathcal K\big(\tilde G_\Psi(Y),\tilde G_\Psi(Y)\big)
=-\tfrac{g_s^2}{24}\,p\big(\hat Y,\hat Y\big),\qquad \hat Y=M_{\mathcal K}^{1/2}\tilde G_\Psi(Y) ,
\tag{5.5}
$$
$\Psi$-**independent**. The sanity evaluation (d) of `agent/scratch/sanity-053.py` confirms
the first step: with $q_2$ alone the residual of (5.5) scales as $g_s^6$ (ratio $62.6$ for a
halving, expected $64$).

**The flat admissible law and the closure statement.**
$$
\boxed{\;F^{\rm flat}_u=-(D_YG_\Psi)^{-1}\partial_uG_\Psi
=\big(\partial_uM_{\mathcal K}^{-1/2}\big)M_{\mathcal K}^{1/2}Y
+\tfrac{g_s^2}{60}\,R^{(19)}_u\,\mathcal K^{-1}T(\cdot,Y,Y)
+\tfrac{g_s^2}{30}\,\mathcal K^{-1}T(\cdot,Y,R^{(19)}_uY)
+O(g_s^4Y^2)+O(Y^3)\;}
\tag{5.6}
$$
The linear sector is exact in $g_s$ (the degree-1 part of $-(D_YG)^{-1}\partial_uG$ involves
only $M_{\mathcal K}^{1/2}$). The quadratic sector follows from $\delta\hat Y=0$ at degree 2:
with $\rho:=M_{\mathcal K}^{-1/2}\partial_uM_{\mathcal K}^{1/2}=-R^{(19)}_u+O(g_s^2)$ and
$\partial_uq_2=2R^{(19)}_uq_2$ ($T$ $\Psi$-independent),
$F^{{\rm flat},(2)}=-\rho q_2-\partial_uq_2-2q_2(Y,F^{(1)})=-R^{(19)}_uq_2-2q_2(Y,R^{(19)}_uY)
+O(g_s^4Y^2)$, which is the displayed pair; check against (3.5) at $k=3$:
$\mathcal K(F^{(2)},Y)=(\tfrac1{60}+\tfrac1{30})g_s^2T(R_uY,Y,Y)=\tfrac{g_s^2}{20}T(R_uY,Y,Y)$
($\mathcal KR^{(19)}$ symmetric). [The first version of this box displayed
$\tfrac{g_s^2}{30}R^{(19)}_u\mathcal K^{-1}T(\cdot,Y,Y)$ with remainder $O(g_s^3Y^2)$: not
admissible at leading order, and of the order of its own remainder; corrected on the fix
pass after the critic's review, machine-checked by `C3.2-expansion` (§7).]
is admissible and flat: $\delta\hat Y=0$, $\mathcal E_4[F^{\rm flat}]=0$ identically, and
$F^{\rm flat}-F^{(19)}\in\mathfrak{stab}(\Phi^*)$ is a trivial symmetry (C1). Consequently,
within $S_4$,
$$
[\delta_{\Lambda_1},\delta_{\Lambda_2}]\Sigma_2=\delta_{\Lambda_{12}}\Sigma_2
+\hat\Phi_{\rm exact}(\mathcal D_\Psi),\qquad
\hat\Phi_{\rm exact}(w):=\partial_w\Sigma_*(\Psi)+F^{\rm flat}_w(Y),
\tag{5.7}
$$
no $\mathcal E$: **the algebra closes modulo the $\Psi$ equation of motion alone at
$O(g_s^4)$**, in the representative (5.6), by the same mechanism as 043 with one more
ingredient (the Morse map removes the cubic term before the square root removes the
$\Psi$-dependence of the Hessian). The R19 representative is curved,
$\mathcal E_4=\tfrac{g_s^2}{100}[A_1,A_2]Y+O(g_s^3)\neq0$, exactly as R17's was.

**Scope.** Within the finite model with generic tensors (PH14) and $p$ nondegenerate on $V$
(PH1/PH5); exact in $g_s$ as a formal series; the series in $Y$ has the Neumann radius of
R19's own law. Not established: convergence, the string-vertex realisation, and the
canonical transformation induced on $\Psi^+$ (GAP-3e, unchanged).

### Part-B design (what `codes/verify-gauge-algebra-ogs4.py` computes)

Model: the tensors of `codes/verify-b3-sextic.py` lines 79–190 ($\mathcal V_{4,5,6}$,
$\Lambda_I$ basis, `Kmat`, `vvec`, `T_action()` $=T$, `solve_saddle`), at $N=2$ ($D=3$) and
$N=3$ ($D=6$), two seeds, $g_s\in\{0.05,0.1,0.2\}$, complex arithmetic so that
$\partial_u$ of any quantity (including through the Newton saddle) is a complex-step
derivative at machine precision. $\mathcal K=-\tfrac{12}{g_s^2}\times$`hess` at
$\Sigma_*$, $\Phi^*$ from `S4_minus_shared` minus its saddle value. Checks, named after the
nodes:

- `C1.1`, `C1.3`: invariance residual (2.1) for $F^{(19)}$ (linear solve of the implicit
  law) and for $F^{(19)}+\mathcal K^{-1}S(Y)\nu(Y)$ with random $Y$-dependent antisymmetric
  $S$; break: symmetric $S$.
- `C1.2`: least-squares residual of (3.7) at $D=3,6$, relative residual $O(1)$; break: the
  same system with $T\to0$ (then the linear family exists, residual $0$).
- `C2.1`, `C2.2`, `C2.3`: $\mathcal E_4[F^{(19)}]$ by (4.1) with complex-step $\partial_u$
  and $D_Y$; (4.3) as a structural test ($\mathcal K(\nu,\mathcal E_4)=0$); Richardson in
  $g_s$ for $\mathcal E_4-\tfrac{g_s^2}{100}[A_1,A_2]Y=O(g_s^3)$ and the coefficients
  (4.7), (4.8); break: a wrong coefficient in (4.7).
- `C3.1`: iterate (5.3) to $n=4$ and check the residual of (5.5) scales as
  $g_s^{2n+2}$; and at fixed $g_s$ iterate to machine precision.
- `C3` (main): $\mathcal E_4[F^{\rm flat}]=0$ at machine precision **and** invariance
  residual $0$ for $F^{\rm flat}$; two breaks that separate the two properties: $G$
  truncated to $M_{\mathcal K}^{1/2}$ alone (flat, **not** admissible: residual $O(g_s^4)$)
  and $F^{(19)}$ (admissible, **not** flat: $\mathcal E_4=O(g_s^2)$).
- `C3-invariants` (documentary): the brief's invariants of $\hat T_\Psi$
  ($\hat T_{ijk}\hat T_{ijk}$, eigenvalues of $\hat T_{ijk}\hat T_{ijl}$) at two values of
  $\Psi$ — expected to differ, recorded to show that their variation coexists with the
  flat representative.
- Orders to separate: $g_s^2$ (043's defect), $g_s^3$ (4.7), $g_s^4$ (4.8); Richardson with
  $g_s$ halving, slopes reported.

## 6. Result

**GAP-3d, part A: the premise of 043 fails at $O(g_s^4)$ and its conclusion survives.**

1. The invariance condition of the sextic action is one polynomial identity (3.2) in $Y$;
   it forces a $Y$-**nonlinear** law (no linear law exists for generic $T$, C1.2) and fixes,
   degree by degree, only the symmetrised part of $\mathcal K(F^{(k-1)},Y)$. The admissible
   family is
   $F_u=F^{(19)}_u+\mathcal K^{-1}S_u(Y)\nu(Y)$, $S_u$ antisymmetric, $\nu=Y-\tfrac{g_s^2}{20}
   \mathcal K^{-1}T(\cdot,Y,Y)$ (C1): the trivial symmetries of $S_4$, with the same graded
   dimension as at $T=0$. The brief's expected collapse to $\mathfrak k_{\mathcal K}\cap
   \mathfrak{stab}(T)$ is the collapse of the (empty) linear sub-family.
2. The defect of any admissible law is the curvature of a connection with structure group
   the formal diffeomorphisms of $V$ fixing $0$ (C2), and is exactly a trivial symmetry,
   $\mathcal E_4=\mu_{12}E_\Sigma$ with $\mu_{12}$ antisymmetric (4.3). For R19's law
   $\mathcal E_4=\tfrac{g_s^2}{100}[A_{u_1},A_{u_2}]Y+O(g_s^3)$, the $T$-terms entering at
   $g_s^3$ (4.7) and $g_s^4$ (4.8).
3. The removability criterion is right-equivalence of the germs $\Phi^*(\cdot;\Psi)$; for a
   nondegenerate Hessian its only invariant is the signature of $\mathcal K(\Psi)$, constant
   (5.1). Hence a flat admissible representative exists (C3): the Morse map (5.4)–(5.5)
   followed by $M_{\mathcal K}^{1/2}$ gives $\hat Y$ with $\Phi^*=-\tfrac{g_s^2}{24}p(\hat Y,
   \hat Y)$ and $\delta\hat Y=0$; the algebra closes **modulo the $\Psi$ equation of motion
   alone at $O(g_s^4)$**, (5.7). The $\hat T_\Psi$-invariant test proposed for part B is not
   a falsifier (wrong equivalence group) and is kept only as documentation.
4. Expected verdict of part B: **positive**, with the proof already in C3; part B's role is
   the machine confirmation of C1–C3 in the finite model and the explicit coefficients
   (4.7)–(4.8).

Proposed ledger row (after part B and the critic): *Gauge algebra at $O(g_s^4)$, $\Sigma_2$
row — Conditional(PH14, PH1, PH5) – Proven within the finite model:* the admissible freedom
is the set of trivial symmetries $\mathcal K^{-1}S(Y)\nu(Y)$; the R19 representative is
curved, $\mathcal E_4=\tfrac{g_s^2}{100}[A_1,A_2]Y+O(g_s^3)$; the Morse-plus-square-root
representative $F^{\rm flat}=-(D_YG_\Psi)^{-1}\partial_uG_\Psi$, built by the explicit
construction (5.3)–(5.6) (Morse map plus $M_{\mathcal K}^{1/2}$), is flat and admissible, so
the $\Sigma_2$ algebra closes modulo the $\Psi$ EOM alone within $S_4$ at $O(g_s^4)$; R45's
carve-out (v) stands: the $\mathcal F$-proportional $\mathcal D_\Psi$ and the openness of the
closed-SFT gauge algebra (Zwiebach 1993) are untouched.

**Self-review (research skill §5).** (1) The objective — a verdict with a proof — is
answered, in the positive direction, not the direction the brief anticipated; the
literal items 3 and 5 were redirected because their premise (linearity) is not among the
forced constraints. (2) Weakest step: Koszul exactness for the kernel (3.4) (now with its two-line
justification), and the explicit coefficients (4.8), hand-expanded; part B checks both
(the second coefficient of (4.8) was corrected on the fix pass). (3) Not checked: convergence of the $Y$-series (same status as R19's law) and
the string-vertex realisation (PH14). (4) A stronger physicist would say at once "Morse
lemma" on seeing a cubic with nondegenerate Hessian — which is the content of §5; what
remains for such a reader is the canonical transformation on $\Psi^+$ (GAP-3e).

## 7. Part B — machine confirmation (`codes/verify-gauge-algebra-ogs4.py`)

### Setup

A1–A4, C1–C3 as stated in §1–§5; the design of §5 *Part-B design*, executed as written.
Script: `codes/verify-gauge-algebra-ogs4.py`; log: `agent/scratch/gauge-ogs4-run1.log`.

**Model.** The tensors of `codes/verify-b3-sextic.py` lines 79–190, reconstructed verbatim
(`Model`): $\mathcal H_0=\mathbb R^N$, generic totally symmetric $\mathcal V_{4,5,6}$,
orthonormal $\operatorname{Sym}^2$ basis $\Lambda_I$, $p=$`V4S`, $P_w=$`V5S`$\cdot w$,
$T=$`T_action(1, 6/5)`$=\mathcal V_6-\tfrac65\mathcal C$; $N=2$ ($D=3$) and $N=3$ ($D=6$),
seeds $20260926$ and $53$ for the tensors (the test vectors $\Psi,u_1,u_2,Y$ from seed$+7$);
$g_s\in\{0.05,0.1,0.2\}$, Richardson sequence $0.2,0.1,0.05,0.025,0.0125$. The
$\Sigma$-sector action is used divided by $g_s^2$ (a polynomial in $g_s$), so
$\mathcal K=-\tfrac{12}{g_s^2}$`hess`$|_{\Sigma_*}=p-\tfrac{g_s}5P_\Psi-\tfrac{g_s^2}{10}
T(\cdot,\cdot,\Sigma_*)$ and $\Phi^*=(S_4-\text{shared})(\Sigma_*+Y)-(\ldots)(\Sigma_*)$, both
regular at $g_s=0$.

**Differentiation (a change of *method* relative to the design's "complex step", not of
object).** Every derivative is taken by forward-mode automatic differentiation with
*multi-dual numbers* (class `MD`: $m$ nilpotents $\epsilon_a$, $\epsilon_a^2=0$,
$\epsilon_a\epsilon_b\neq0$, components indexed by subsets), exact to rounding and with no
step size: seeding $\Psi\to\Psi+\epsilon_1u_1+\epsilon_2u_2$ and $Y\to Y+\epsilon_3w$
gives $\partial_{u_i}$, $\partial_{u_1}\partial_{u_2}$ and $D_Y(\cdot)w$ through the Newton
saddle, the Denman–Beavers square root and the Morse recursion (a Newton-type iteration
converges one more nilpotent order per step after the primal has converged; the script
runs `#directions + 3` extra steps and asserts the residual). Complex-step would have
given only *one* nested derivative; (4.1) needs $\partial_{u_1}$ of a law that itself
contains $\partial_{u_2}\mathcal K$ (and, for $F^{\rm flat}$, $\partial_{u_2}G$). The same
device with $g_s\to\epsilon_4+\dots+\epsilon_7$ at $g_s=0$ yields the **exact Taylor
coefficients** $c_k=\text{comp}[k\text{-subset}]/k!$ of any quantity through $g_s^4$ (all
$\binom4k$ subsets must agree — asserted), which is how (4.7)–(4.8) are compared to
$\mathcal E_4$ with no expansion by hand and no fit; the Richardson slopes asked for by the
brief are computed as well, at finite $g_s$, with the $Y$-linear and $Y$-quadratic sectors
separated by polarisation ($\mathcal E_4(tY)$ at $t=\pm1,\pm\tfrac12,\pm\tfrac14$, degrees
$1$–$6$ solved exactly).

**Objects.** $F^{(19)}$: the implicit law of 013 solved as the linear system
$(\mathcal K-\tfrac{g_s^2}{20}T(\cdot,Y,\cdot))\,\delta Y=-\tfrac12(\partial_u\mathcal K)Y$
(all orders in $Y$). $\mathcal E_4$: (4.1) literally, with $D_YF\cdot w$ by seeding $Y$.
$G_\Psi$: $M_{\mathcal K}^{1/2}$ by Denman–Beavers on $p^{-1}\mathcal K$ (inverses and sums
only), $\tilde G_\Psi$ by the recursion (5.3) on symmetric tensors $q_n[I,J_1..J_n]$,
$q_n=\tfrac12\mathcal K^{-1}\omega_{n+1}(\cdot,Y^n)$ with $\omega_{n+1}$ the total
symmetrisation (sum over shuffles) of $-\sum_{a+b=n+1}\mathcal K(q_a,q_b)$; truncation
$n_{\max}=10$ at $D=3$ (rank-11 tensors) and $n_{\max}=7$ at $D=6$ (rank-8, $1.7\times10^6$
entries). $F^{\rm flat}_u=-(D_YG)^{-1}\partial_uG$ with the Jacobian
$D_Y\tilde G=1+\sum_nn\,q_n(Y^{n-1},\cdot)$ exact. The invariance residual is (3.2),
$\mathcal K(\nu(Y),F)+\tfrac12\partial_u\mathcal K(Y,Y)$, normalised by the second term;
$\|\mathcal E_4\|$ is normalised by the largest of its four terms.

**Checks and what fails each** (names = claim-tree nodes):

| Check | Fails if | Break leg (must FAIL the same test) |
|---|---|---|
| S0 | $\Phi^*$ from the action $\neq$ its cubic form, or forward-mode $\partial_u\mathcal K\neq$ IFT value | — (setup) |
| C1.1 | $F^{(19)}$ not admissible (residual $\gg10^{-9}$) | R19's linear part without the $T$-correction |
| C1.3 | $F^{(19)}+\mathcal K^{-1}S(Y)\nu(Y)$, $S=S_0+S_1Y$ antisymmetric, not admissible | symmetric $S$ |
| C1.2 | a $Y$-linear law exists (LS residual of (3.7) $\to0$) at $D=3$ or $6$ | $T\to0$; a source placed in the image |
| C2.1 | $\mathcal K(\nu,\mathcal E_4[F^{(19)}])\neq0$ | the non-admissible law of C1.1's break |
| C2.2 | $\mathcal E^{(1)}_4\neq[R^{(19)}_1,R^{(19)}_2]Y$, or $c_0,c_1\neq0$, or $c_2\neq\tfrac1{100}[A_1,A_2]Y$, or $c_3-c_3[\mathcal E_3]\neq$ (4.7) | $\tfrac1{100}\to\tfrac1{50}$ in (4.7) |
| C2.3 | the $Y$-quadratic sector nonzero below $g_s^4$, or its exact $g_s^4$ coefficient $\neq$ (4.8) | $\tfrac1{2000}\to\tfrac1{1000}$ in (4.8) |
| C2-R | last Richardson slope off by $>0.35$ from $2,3,4$ (linear sector), or below $5-0.35$ (quadratic; one-sided since the fix pass) | $2\times$(4.7): slope stays $3$; (4.8) as first written ($-\tfrac{19}{2000}$): slope stays $4$ |
| C3.1 | residual of (5.5) at truncation $n\le4$ does not scale as $g_s^{2n+2}$ | — (the slopes themselves) |
| C3 | $\mathcal E_4[F^{\rm flat}]\neq0$ or $F^{\rm flat}$ not admissible | $G=M_{\mathcal K}^{1/2}$ alone (flat, not admissible); $F^{(19)}$ (admissible, not flat) |
| C3.2-expansion (fix pass) | the $Y$-quadratic part of $F^{\rm flat}=-(D_YG)^{-1}\partial_uG$ nonzero below $g_s^3$, or its exact $g_s^3$ coefficient $\neq$ the corrected (5.6) (built from $R^{(19)}_u$, $\mathcal K^{-1}$) or its hand form $\tfrac1{600}A_up^{-1}T(\cdot,Y,Y)+\tfrac1{300}p^{-1}T(\cdot,Y,A_uY)$, or not degree-2 homogeneous | (5.6) as first written, $\tfrac{g_s^2}{30}R^{(19)}_u\mathcal K^{-1}T(\cdot,Y,Y)$ |

### Derivation

Final run: `agent/scratch/gauge-ogs4-run7.log` (fix pass, 120 s, 25 PASS, 0 FAIL, exit 0;
run 6, 113 s, is the pre-fix run and runs 1–5 the development runs, see *Verification*).
All numbers below are from run 7; they coincide with run 6 except where marked. "Residual" means the normalised quantity defined in the Setup; the
worst value over the twelve $(D,\text{seed},g_s)$ configurations is quoted unless a
configuration is named.

**Setup and C1.** S0: $\Phi^*$ from the action around the saddle equals its cubic form to
$3\times10^{-14}$; forward-mode $\partial_u\mathcal K$ equals the implicit-function-theorem
value to $3\times10^{-14}$ (A3, and the differentiation method, validated). C1.1: residual
of $F^{(19)}$ $1.2\times10^{-15}$; break (no $T$-correction) $\ge1.7\times10^{-4}$. C1.3:
with $\mathcal K^{-1}S(Y)\nu(Y)$, $S=S_0+S_1Y$ antisymmetric, $2.6\times10^{-13}$; break
(symmetric $S$) $\ge47$. C1.2: relative least-squares residual of (3.7): $0.751$, $0.347$
($D=3$: 3 unknowns, 10 equations, rank 3), $0.533$, $0.118$ ($D=6$: 15 unknowns, 56
equations, rank 15); breaks: $T\to0$ gives $0$, a source placed in the image gives
$2\times10^{-15}$. The C1.2 threshold $0.1$ against the observed minimum $0.118$ ($D=6$, seed
53) is a thin margin; the falsifier is exercised by both break legs.

**C2 — exact Taylor coefficients (nilpotent $g_s$, all four configurations).**

| Quantity | Statement tested | Relative error |
|---|---|---|
| $\mathcal E^{(1)}_4$ vs $[R^{(19)}_1,R^{(19)}_2]Y$, all orders $g_s^0..g_s^4$ | (4.5) | $\le1.9\times10^{-14}$ |
| $c_0,c_1$ of $\mathcal E_4$ | $=0$ | $0$ |
| $c_2$ | $\tfrac1{100}[A_1,A_2]Y$ | $3.1\times10^{-14}$ |
| $c_3[\mathcal E_3]$, $\mathcal E_3=[R^{(17)}_1,R^{(17)}_2]Y$ | $\tfrac1{500}([A_1,A_\Psi A_2]+[A_\Psi A_1,A_2])Y$ | $6.6\times10^{-15}$ |
| $c_3[\mathcal E_4]-c_3[\mathcal E_3]$ | (4.7) | $2.7\times10^{-14}$ |
| $Y$-quadratic sector through $g_s^3$ | $=0$ | $0$ |
| $c_4$ of the $Y$-quadratic sector | (4.8) (corrected) | $\le1.0\times10^{-13}$ (run 6, against the first version: $0.88$–$0.93$, FAIL) |

C2.1 at fixed $g_s$: $\mathcal K(\nu,\mathcal E_4[F^{(19)}])/(\|\mathcal K\nu\|\|\mathcal
E_4\|)\le1.0\times10^{-14}$ with $\|\mathcal E_4\|\ge9.5\times10^{-3}$ of the term scale
(nonvacuous); break (non-admissible law) $\ge1.1\times10^{-5}$. Breaks of the coefficient
checks: $\tfrac1{100}\to\tfrac1{50}$ in (4.7) gives error $\ge0.50$;
$\tfrac1{2000}\to\tfrac1{1000}$ in (4.8) gives $\ge0.28$ (run 7; $\ge0.88$ in run 6, where
the second coefficient of the tested formula was still $-\tfrac{19}{2000}$).

**The run-6 failure of (4.8), diagnosed in the brief's order** (historical; corrected in §4
on the fix pass, confirmed by the critic's independent hand re-derivation and by run 7). (i) Check typo: the script encodes
$s_1=p^{-1}T(\cdot,Y,[A_1,A_2]Y)$ and $s_2=A_2p^{-1}T(\cdot,Y,A_1Y)-A_1p^{-1}T(\cdot,Y,A_2Y)$
exactly as (4.8) writes them, and the break leg confirms the check responds to the first
coefficient. (ii) Transcription: none — the coefficient is compared, not copied through a
formula. (iii) The claim: the least-squares fit of the exact $c_4$ on $(s_1,s_2)$ gives
$(a,b)=(\tfrac1{2000},-\tfrac1{2000})$ to six digits with fit residual $10^{-15}$ in all
four configurations (a diagnostic; not used to pass anything). The hand expansion of (4.4b)
with (1.3) reproduces this: with $Q_u=\tfrac{g_s^3}{200}p^{-1}T(\cdot,Y,A_uY)
+\tfrac{g_s^4}{1000}\big[A_\Psi p^{-1}T(\cdot,Y,A_uY)+p^{-1}T(\cdot,Y,A_\Psi A_uY)\big]
+\tfrac{g_s^4}{200}p^{-1}T(\cdot,Y,B_{u\odot\Psi}Y)+O(g_s^5)$, the three groups of (4.4b)
contribute at $g_s^4$: $\partial_1Q_2-\partial_2Q_1=\tfrac1{1000}s_1-\tfrac1{1000}s_2$ (the
$B$ term is $1\leftrightarrow2$ symmetric and drops); $2Q_2(Y,R_1Y)-2Q_1(Y,R_2Y)=
-\tfrac1{2000}s_1$ (the $T(\cdot,A_1Y,A_2Y)$ terms cancel); $R_2Q_1-R_1Q_2=+\tfrac1{2000}s_2$.
Sum: $\tfrac1{2000}s_1-\tfrac1{2000}s_2$. So (4.8) is wrong in its second coefficient,
$-\tfrac{19}{2000}\to-\tfrac1{2000}$; the first coefficient, the structure, and the
consistency test of §4 (which is blind to the second coefficient) are unaffected, and
nothing downstream (C3) uses (4.8). Part B did not correct §4 (its brief: report, do not
adjust); the fix pass did.

**C2-R — Richardson slopes** ($g_s$ halving from $0.2$ to $0.003125$; the last slope per
configuration, expected value in brackets). Linear sector: $\|\mathcal E^{(1)}\|$:
$1.99,2.01,2.01,1.92$ [2]; after removing $\tfrac{g_s^2}{100}[A_1,A_2]Y$: $2.92,2.97,2.98,
3.30$ [3]; after removing also $g_s^3\big(c_3[\mathcal E_3]+(4.7)\big)$: $4.00,4.00,4.00,
4.05$ [4]; break ($2\times$(4.7)): $3.07,3.02,3.01,2.79$ (stays at 3). Quadratic sector
after removing $g_s^4\times$(4.8): $4.93,4.96,4.98,5.75$ [$\ge5$]; break ((4.8) as first
written, $-\tfrac{19}{2000}$): $4.00,4.00,4.00,4.00$ (stays at 4; this was run 6's failing
leg). The $5.75$ at $D=6$, seed 53 is pre-asymptotic: the $g_s^6$ term dominates the
$g_s^5$ one down to $g_s\approx0.002$; extending the sequence to $g_s=0.00078125$ (scratch
run, same script, that configuration only) gives the last slopes $5.88,6.17,6.07,5.75,
5.31,5.06\to5$. The run-6 expectation that this leg would pass unchanged at $5\pm0.35$ was
wrong for that reason; the fix pass made the test one-sided (slope $\ge4.65$, which is the
content of "residual $O(g_s^5)$") and added the break leg, rather than extending the
sequence globally (the other configurations reach the rounding floor,
$5\times10^{-14}$ at $g_s=0.003125$). The configuration $D=6$, seed 53 has $T$ entries $\sim300$ (composite
$\mathcal C$ through $\mathcal V_4^{-1}$), coefficient ratios $c_3/c_2\sim28$,
$c_4/c_2\sim700$, and reaches the asymptotic regime only below $g_s\approx0.01$ — the
reason for the extended sequence. The exact-coefficient method above is the sharp
instrument; the slopes are the brief's deliverable and agree with it.

**C3.1 — Morse map.** Relative residual of (5.5) by truncation order $n$ (normalised by
$|\Phi^*|=O(g_s^2)$, so the relative order is $2n$ and the absolute $2n+2$), slopes from the
smallest halving pair above the rounding floor: $n=2$: $3.96,3.90,3.99,3.98$ [4]; $n=3$:
$5.94,5.86,6.00,5.96$ [6]; $n=4$: $7.65,7.83,7.96,7.94$ [8]. At the largest truncation
($n=10$ at $D=3$, $n=7$ at $D=6$) the residual reaches $10^{-16}$–$10^{-15}$ in ten of the
twelve configurations and $9\times10^{-12}$ ($D=3$, seed 53, $g_s=0.2$); at $D=6$, seed 53,
$\|\tfrac{g_s^2}{20}\mathcal K^{-1}T_Y\|_2=0.44,0.23,0.08$ at $g_s=0.2,0.1,0.05$ and the
$Y$-series converges by a factor $\sim5$–$30$ per order: residual $3\times10^{-7}$,
$1.6\times10^{-9}$, $6\times10^{-13}$ at $n=7$ (truncation level, decreasing with $n$ at
every $g_s$).

**C3 — main.** $\|\mathcal E_4[F^{\rm flat}]\|/\text{scale}\le4.8\times10^{-16}$ in all
twelve configurations (flatness is exact for every truncation of $G$, as (4.2) says).
Invariance residual of $F^{\rm flat}$ at $n_{\max}$: $\le1.8\times10^{-15}$ in nine
configurations, $1.3\times10^{-10}$ ($D=3$, seed 53, $g_s=0.2$; (5.5) residual
$9\times10^{-12}$), and at the truncation level for $D=6$, seed 53: $8.0\times10^{-7}$
($g_s=0.2$), $4.2\times10^{-9}$ ($0.1$), $6.2\times10^{-12}$ ($0.05$), each within a factor
$3$ of the (5.5) residual and decreasing with $n$ at every $g_s$ (asserted). The two
separating breaks: $G=M_{\mathcal K}^{1/2}$ alone is flat ($\mathcal E_4\le3.9\times
10^{-16}$) and **not** admissible (residual $2\times10^{-4}$–$0.26$, scaling as $g_s^2$ in
the normalised (3.2) form, i.e. $g_s^5$ in (2.1): the design's "$O(g_s^4)$" was a rough
estimate); $F^{(19)}$ is admissible ($1.2\times10^{-15}$) and **not** flat
($\|\mathcal E_4\|\ge9.5\times10^{-3}$ of the term scale).

**C3-invariants (documentary).** $\hat T_{ijk}\hat T_{ijk}$ and the eigenvalues of
$\hat T_{ijk}\hat T_{ijl}$ (complex $\mathcal K^{-1/2}$ for the indefinite $\mathcal K$) at
$\Psi$ and $\Psi+0.7u_1$, $g_s=0.1$: e.g. $-1488$ vs $-1315$ ($D=3$, seed 20260926),
$17989$ vs $25415$ (seed 53): they differ, and the flat representative exists regardless
(§5: invariants of the wrong equivalence group).

**C3.2-expansion (fix pass) — the displayed expansion (5.6).** With nilpotent $g_s$ and
$F^{\rm flat}=-(D_YG)^{-1}\partial_uG$ computed from $G$ (`FlatLaw.law`, Morse map to
$q_3$), the even part $\tfrac12(F(Y)+F(-Y))$ (degree-4 and higher parts start at $g_s^7$)
vanishes through $g_s^2$ ($0$); its $g_s^3$ coefficient equals the corrected (5.6) to
$5.4\times10^{-15}$ and the hand form $\tfrac1{600}A_up^{-1}T(\cdot,Y,Y)+\tfrac1{300}
p^{-1}T(\cdot,Y,A_uY)$ to $5.9\times10^{-15}$; $Y\to2Y$ multiplies it by $4$
($8.3\times10^{-15}$). Break: the first version of the box fails with relative error
$\ge0.60$ (up to $2.2$).

### Result

Part B confirms C1, C2.1, C2.2, C3.1 and C3 in the finite model at $N=2,3$, two seeds,
$g_s\in\{0.05,0.1,0.2\}$, to rounding where the $Y$-series converges and to the truncation
level (tracked) where it does not; every check has a break leg that fails. After the fix
pass C2.3 passes with (4.8)'s second coefficient $-\tfrac1{2000}$ (first written
$-\tfrac{19}{2000}$; machine, part-B hand re-derivation and the critic agree), and the
corrected expansion (5.6) is machine-checked (C3.2-expansion). The closure statement (5.7) —
the algebra closes modulo the $\Psi$ equation of motion alone at $O(g_s^4)$ in the
representative $F^{\rm flat}$ — is machine-confirmed; neither (4.8) nor the displayed
expansion of (5.6) is used by it.

Proposed ledger row: §6 (as updated on the fix pass).

### Verification

Script `codes/verify-gauge-algebra-ogs4.py` (seeds printed; PASS/FAIL per check with the
tested quantity; break legs; summary line; exit code = number of failures). Logs:
`agent/scratch/gauge-ogs4-run7.log` (final, fix pass: 25 PASS, 0 FAIL, exit 0; a first run-7
attempt, before the one-sided quadratic Richardson test, failed only `C2-R-quad-c4` at
$5.75$ and was overwritten), `agent/scratch/gauge-ogs4-run6.log` (pre-fix: exit 2, the two
legs testing (4.8) as first written). Runs
1–5 were development: run 1 exposed an incomplete subset closure in the multi-dual linear
solve (visible only when the matrix is linear in the nilpotents: $\mathcal E_3$'s $g_s^3$
coefficient came out with the wrong sign; fixed in run 2); runs 3–5 scaled $|Y|$ to
$\sim1$ at $D=6$, extended the Richardson sequence, and set the slope expectations to the
normalisation actually used ($2n$ relative). No claim was adjusted. Not lint-checked: no
`ruff` in the project venv and no `justfile`.

## Status

Complete (parts A and B, critic iteration 1, fix pass). Last completed: fix pass after
`agent/reports/critic-053-20260926T030500.md` — (4.8)'s second coefficient corrected to
$-\tfrac1{2000}$, boxed (5.6) expansion corrected, §2/§3/§5 wording and citations, row
updated; run 7 of `codes/verify-gauge-algebra-ogs4.py` (log
`agent/scratch/gauge-ogs4-run7.log`): 25 PASS, 0 FAIL, exit 0. Outcome: C1, C2, C3
machine-confirmed, including C2.3 and the new C3.2-expansion.

## Next

Orchestrator: promotion of the §6 row. Open beyond this record: GAP-3e (canonical
transformation on $\Psi^+$), convergence of the $Y$-series, the string-vertex realisation
(PH14).
