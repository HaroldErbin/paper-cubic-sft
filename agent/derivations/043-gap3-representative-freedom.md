# Derivation 043 — GAP-3: is the $E_\Sigma$-proportional defect removable by an admissible redefinition?

## 0. Task and objective

**Literal task.** Characterise exactly the admissible freedom in the $\Sigma_2$ gauge law
$\delta\tilde X=R_u\tilde X$ of R17/011 (B.8), compute how the closure defect
$\mathcal E=\tfrac{g_s^2}{100}[A_{u_1},A_{u_2}]\tilde X+O(g_s^3)$ of record 040 (R45)
transforms under $R_u\to R_u+\Delta R_u$, and decide whether some admissible $\Delta R_u$
removes $\mathcal E$ identically for generic $\mathcal V_4,\mathcal V_5$.

**Motivating objective.** R45 asserts that the $O(g_s^3)$ gauge algebra closes modulo **both**
equations of motion. If the $E_\Sigma$-proportional half of that statement is an artifact of
the chosen representative of the gauge law — removable by a trivial symmetry — then R45 and
an earlier statement in the quintic gauge paragraph of the notes are both wrong, and the $O(g_s^4)$ BV analysis
inherits the error.

**Scope / layer (A1).** Algebraic layer: finite-dimensional $\mathcal H_0$, generic
unconstrained totally symmetric tensors $\mathcal V_4,\mathcal V_5$, formal power series in
$g_s$ (no convergence or positivity claims), $\Sigma_2\in\operatorname{Sym}^2\mathcal H_0/
\ker\mathcal V_4$. Conventions of 040 §1 (physical ghost number, degree parity, R43
normalisation).

## 1. Notation

$p_{2,2}=:p$ (nondegenerate on the quotient, PH1/PH5), $P_u:=p_{3,2}(\cdot,\cdot,u)$,
$A_u:=p^{-1}P_u$, $K_\Psi=p-\tfrac{g_s}{5}P_\Psi=p\,M_\Psi$ with
$M_\Psi:=1-\tfrac{g_s}{5}A_\Psi$. For an operator $N$ on $\operatorname{Sym}^2$ write
$N^\star:=p^{-1}N^{\rm T}p$ (the $p$-adjoint); $A_w^\star=A_w$ for every $w$ because
$\mathcal V_5$ is totally symmetric, and $M_\Psi^\star=M_\Psi$.
$\mathfrak p:=\{N:N^\star=N\}$, $\mathfrak k:=\{N:N^\star=-N\}$;
$[\mathfrak p,\mathfrak p]\subset\mathfrak k$, $[\mathfrak k,\mathfrak p]\subset\mathfrak p$,
$[\mathfrak k,\mathfrak k]\subset\mathfrak k$ (Cartan-type grading, used below).
The R17 representative is $R_u=\tfrac{g_s}{10}K_\Psi^{-1}P_u=-\tfrac12M_\Psi^{-1}\partial_uM_\Psi$.

## 2. The constraints on $\Delta R_u$ — enumeration

Written **before** any computation, one line each with its justification. Every constraint
imposed must be forced; an over-constrained $\Delta R_u$ answers a smaller question.

1. **Invariance of the dressed quadratic form** — $S_3$ depends on $\tilde X$ *only* through
   $K_\Psi(\tilde X,\tilde X)$ (011 (B.2), exact because $S_3$ is quadratic in $\Sigma$), so
   the only condition on the law is $\delta[K_\Psi(\tilde X,\tilde X)]=0$, i.e.
   $2K_\Psi(\delta\tilde X,\tilde X)=-(\delta K_\Psi)(\tilde X,\tilde X)$. **Forced.**
2. **Hence: only the $K_\Psi$-symmetric part of $R_u$ is fixed** — the condition is a
   statement about a quadratic form in $\tilde X$; it determines
   $\operatorname{Sym}(K_\Psi R_u)=\tfrac{g_s}{10}P_u$ and nothing else. So the admissible
   freedom is $\Delta R_u=K_\Psi^{-1}S_u$ with $S_u$ an arbitrary **antisymmetric** bilinear
   form, i.e. $\Delta R_u\in\mathfrak k_{K_\Psi}$. **This is the whole freedom in the
   $\tilde X$-linear sector.**
3. **Linearity in $\Lambda$ (hence in $u=\delta\Psi$ at leading order)** — a gauge generator
   contracts exactly one parameter; a term quadratic in $\Lambda$ is not a gauge
   transformation. **Forced**, and satisfied by the R17 representative.
4. **Homogeneity in $\tilde X$ is *not* forced beyond order 0** — writing
   $\delta\tilde X=\sum_{n\ge0}T^{(n)}_u(\tilde X^{\otimes n})$, condition 1 gives: $n=0$
   $\Rightarrow T^{(0)}=0$ ($K_\Psi$ nondegenerate); $n=1$ = item 2; $n\ge2$ admissible
   whenever the induced $(n{+}1)$-form $K_\Psi(T^{(n)}(\tilde X^n),\tilde X)$ vanishes. The
   admissible family is therefore *larger* than the $\Delta R_u$ of the brief; this only
   strengthens a removability verdict and is recorded, not used.
5. **Ghost number** — $N_{\rm gh}(\tilde X)=4$, $N_{\rm gh}(u)=2$, so $\Delta R_u$ must
   preserve $N_{\rm gh}=4$ on $\operatorname{Sym}^2\mathcal H_0$. **Forced.**
6. **Grassmann parity** — $u$ is Grassmann-even (it is $\delta\Psi$), $\tilde X$ even, so
   $\Delta R_u$ is an even operator; no reordering sign arises in the antisymmetrisation.
   **Forced.**
7. **$\Delta R_u=O(g_s)$** — at $g_s^0$ the law must reduce to R11's $\delta\tilde X=0$
   (rigid slaving, C4 of 040). **Forced.**
8. **Algebraicity / locality** — each order in $g_s$ must be a polynomial in $\Psi$ built from
   $\mathcal V_5$, $p$ and $p^{-1}$ (the building blocks $R_u$ itself uses); no new inverse,
   no inverse powers of $\Psi$. **Imposed** (a redefinition of *this* theory must be built
   from its own vertices); it restricts the family, so it only strengthens a positive
   verdict.
9. **Compatibility with the quotient and reality** — $\Delta R_u$ must preserve
   $\operatorname{Sym}^2\mathcal H_0/\ker\mathcal V_4$ and the reality condition
   $\Sigma^\ddagger=\Sigma$. **Forced**; satisfied by anything built from $A_w$.
10. **Nothing else.** In particular $\Delta R_u$ is *not* required to be $\Psi$-independent,
    not required to be $p$-antisymmetric (only $K_\Psi$-antisymmetric), and not required to
    commute with $A_\Psi$.

**The hinge (checked in §5, not assumed).** Items 1–2 say the freedom is exactly
$\delta\tilde X\mathrel{+}=K_\Psi^{-1}S_u\tilde X$ with $S_u$ antisymmetric; since
$E_\Sigma=-\tfrac{g_s^2}{12}K_\Psi\tilde X$ this is $\mu\,E_\Sigma$ with
$\mu=-\tfrac{12}{g_s^2}K_\Psi^{-1}S_uK_\Psi^{-1}$ **antisymmetric** — a Henneaux–Teitelboim
*trivial symmetry* for even fields, i.e. exactly the complement of R22's symmetric,
non-trivial $\mu$. So GAP-3 = *is $\mathcal E$ removable by a trivial symmetry?*

## 3. The admissible family, exactly (C1)

### Setup

Assumptions A1, A2, A3 and the constraints of §2. Local symbols: $D_u:=\partial_u$ the
directional derivative on field space in the direction $u\in\mathcal H_0$ (field space is the
vector space $\mathcal H_0$, so $u$ is a tangent vector at $\Psi$ and $A_\Psi$ is linear in
the base point).

### Derivation

The invariance condition of 011 (B.8), written for a general $\tilde X$-linear law
$\delta\tilde X=\hat R_u\tilde X$ and arbitrary $\tilde X$, is
$$
2\,\big\langle \tilde X,\;K_\Psi\hat R_u\tilde X\big\rangle
=-\,(\partial_uK_\Psi)(\tilde X,\tilde X)
=\tfrac{g_s}{5}\,\big\langle\tilde X,P_u\tilde X\big\rangle .
\tag{3.1}
$$
A quadratic form determines only the symmetric part of its bilinear kernel, so (3.1) is
equivalent to
$$
\operatorname{Sym}\big(K_\Psi\hat R_u\big)=\tfrac{g_s}{10}P_u ,
\qquad\text{i.e.}\qquad
\hat R_u=R_u+K_\Psi^{-1}S_u,\quad S_u^{\rm T}=-S_u ,
\tag{3.2}
$$
with $R_u=\tfrac{g_s}{10}K_\Psi^{-1}P_u$ the R17 representative and $S_u$ an arbitrary
antisymmetric bilinear form on $\operatorname{Sym}^2\mathcal H_0$, linear in $u$, polynomial
in $\Psi$ at each order in $g_s$, of the ghost number and parity of §2 items 5–6, and
$O(g_s)$ by item 7. Equivalently, in terms of the $p$-adjoint of §1 and
$K_\Psi=p\,M_\Psi$:
$$
\hat R_u=R_u+\Delta R_u,
\qquad
\Delta R_u\in\mathfrak k_{K_\Psi}:=\{N:\;M_\Psi N\ \text{is }p\text{-antisymmetric}\} .
\tag{3.3}
$$
At leading order in $g_s$, $\mathfrak k_{K_\Psi}=\mathfrak k+O(g_s)$ and
$R_u=\tfrac{g_s}{10}A_u+O(g_s^2)\in\mathfrak p+O(g_s^2)$: the forced part of the law is
$K_\Psi$-**symmetric** and the freedom is $K_\Psi$-**antisymmetric**, a Cartan-type splitting
of $\mathfrak{gl}(\operatorname{Sym}^2\mathcal H_0)$.

A second reading of (3.2), used throughout §4: writing $K_\Psi=pM_\Psi$ and
$\partial_uK_\Psi=-\tfrac{g_s}{5}pA_u=p\,\partial_uM_\Psi$, the R17 representative is
$$
R_u=-\tfrac12 M_\Psi^{-1}\,\partial_u M_\Psi ,
\tag{3.4}
$$
the "logarithmic-derivative" connection, and (3.2) says
that $\hat R_u$ is admissible iff it is a **metric connection** for the $\Psi$-dependent
bilinear form $K_\Psi$ on the trivial bundle $\mathcal H_0\times\operatorname{Sym}^2
\mathcal H_0$: $\partial_u\big[K_\Psi(Y,Y)\big]=0$ along $\delta Y=\hat R_uY$.

### Commentary

- (3.1)→(3.2) is the whole content of "invariance fixes only the $K_\Psi$-symmetric part";
  it is the exact, all-orders statement, not an expansion.
- (3.4) identifies the R17 law with the *symmetric-logarithmic-derivative* choice of metric
  connection. That choice is one point of an affine space modelled on $\mathfrak k_{K_\Psi}$,
  exactly as the Levi-Civita connection sits inside the affine space of metric connections
  with torsion.

### Result

$$
\boxed{\;\hat R_u=R_u+K_\Psi^{-1}S_u,\quad S_u^{\rm T}=-S_u\;}
$$
— the admissible family, exact in $g_s$, with $S_u$ linear in $u$, $O(g_s)$, algebraic in
$\Psi$, $N_{\rm gh}$-preserving and even. [check: `D1`, `D1-break` — tests (3.2), the
linear-algebraic admissibility condition, only; `D1`'s generic $S_u$ is built from a random
matrix and so does not itself satisfy §2 item 8 (algebraicity), which is checked by
inspection]

## 4. How $\mathcal E$ transforms (C2)

### Setup

A1–A3 and C1. Both $u_1,u_2$ Grassmann-even, so the antisymmetrisation in
$1\leftrightarrow2$ carries no extra sign (040 §1).

### Derivation

From 040 (5.11), exact in $g_s$ and for any $\tilde X$-linear law,
$$
[\delta_1,\delta_2]\tilde X=\hat R_{[\delta_1,\delta_2]\Psi}\tilde X+\mathcal E[\hat R],
\qquad
\mathcal E[\hat R]=\Big\{\partial_{u_1}\hat R_{u_2}-\partial_{u_2}\hat R_{u_1}
+[\hat R_{u_2},\hat R_{u_1}]\Big\}\tilde X .
\tag{4.1}
$$
Read $\hat R$ as a $\mathfrak{gl}(\operatorname{Sym}^2\mathcal H_0)$-valued one-form on field
space, $\hat R=\hat R_{\mathrm d\Psi}$. Then the brace in (4.1) is
$$
\mathcal E[\hat R]=\big(\mathrm d\hat R-\hat R\wedge\hat R\big)(u_1,u_2)
=-\,F[\,\partial-\hat R\,](u_1,u_2) ,
\tag{4.2}
$$
i.e. **$\mathcal E$ is (minus) the curvature of the connection $\nabla_u=\partial_u-\hat R_u$**
on the trivial $\operatorname{Sym}^2\mathcal H_0$-bundle over field space. Substituting
$\hat R=R+\Delta R$ and using $[\hat R_2,\hat R_1]=[R_2,R_1]+[R_2,\Delta_1]+[\Delta_2,R_1]
+[\Delta_2,\Delta_1]$:
$$
\boxed{\;
\mathcal E[\hat R]=\mathcal E[R]
+\Big(\partial_{u_1}\Delta R_{u_2}-\partial_{u_2}\Delta R_{u_1}\Big)
+\Big([R_{u_2},\Delta R_{u_1}]+[\Delta R_{u_2},R_{u_1}]\Big)
+[\Delta R_{u_2},\Delta R_{u_1}] \;}
\tag{4.3}
$$
— exact in $g_s$; in one line, $\mathcal E[R+\Delta R]=\mathcal E[R]+\nabla^R\!\Delta R
+[\Delta R\wedge\Delta R]$, the covariant differential of the shift plus its square. **Both**
terms of $\mathcal E$ move, as the brief warns: the $\partial_\Psi R$ term picks up
$\mathrm d\Delta R$ and the $[R,R]$ term picks up the cross and quadratic brackets.

**Order counting.** With $\Delta R_u=\sum_{n\ge1}g_s^n\Delta^{(n)}_u$:
$$
\mathcal E[\hat R]\big|_{g_s^1}=g_s\big(\partial_{u_1}\Delta^{(1)}_{u_2}
-\partial_{u_2}\Delta^{(1)}_{u_1}\big),
\tag{4.4}
$$
$$
\mathcal E[\hat R]\big|_{g_s^2}=g_s^2\Big\{\tfrac1{100}[A_{u_1},A_{u_2}]
+\big(\partial_{u_1}\Delta^{(2)}_{u_2}-\partial_{u_2}\Delta^{(2)}_{u_1}\big)
+\tfrac1{10}\big([A_{u_2},\Delta^{(1)}_{u_1}]+[\Delta^{(1)}_{u_2},A_{u_1}]\big)
+[\Delta^{(1)}_{u_2},\Delta^{(1)}_{u_1}]\Big\} .
\tag{4.5}
$$
The $\mathfrak k/\mathfrak p$ grading of §1 splits (4.5): $[A,A]$, $\mathrm d\Delta^{(2)}$ and
$[\Delta^{(1)},\Delta^{(1)}]$ are in $\mathfrak k$, the cross bracket $[A,\Delta^{(1)}]$ is in
$\mathfrak p$ and must cancel on its own. The defect to be killed,
$\tfrac1{100}[A_{u_1},A_{u_2}]$, is $\mathfrak k$-valued — as it must be, since a defect of an
admissible law is again admissible-type.

### Commentary

- (4.2) is the structural statement the rest of the record rests on: closure of the auxiliary
  sector = flatness of the compensator connection. It reproduces the two mechanisms of 040
  §5.9 as the two halves of a curvature, and explains at once why the defect is second order
  in the compensator (a curvature has no first-order piece in a connection that starts at
  $O(g_s)$) and why it is exactly $\tilde X$-proportional.
- Check of (4.2) on a pure-gauge connection: if $\hat R_u=(\partial_uG)G^{-1}$ then
  $\partial_{u_1}\hat R_{u_2}=(\partial_1\partial_2G)G^{-1}-\hat R_{u_2}\hat R_{u_1}$, whose
  antisymmetrisation is $[\hat R_{u_1},\hat R_{u_2}]=-[\hat R_{u_2},\hat R_{u_1}]$, so
  $\mathcal E=0$ identically. This is used in §5.
- (4.4): a generic $O(g_s)$ shift introduces a defect at $g_s^1$, one order *below* the one of
  R45. Any removal must therefore have $\mathrm d\Delta^{(1)}=0$ — automatically satisfied by
  $\Delta R=O(g_s^2)$, which is what §5 uses.

### Result

$\mathcal E[R+\Delta R]=\mathcal E[R]+\nabla^R\!\Delta R+[\Delta R\wedge\Delta R]$, eq. (4.3),
exact; order by order (4.4)–(4.5). [check: `D2`, `D2-break`]

## 5. The verdict: $\mathcal E$ is removable (C3)

### Setup

A1–A3, C1, C2. One further structural input, declared: $M_\Psi=1-\tfrac{g_s}{5}A_\Psi$ has a
square root $M_\Psi^{1/2}$ as a **formal power series in $g_s$** with coefficients polynomial
in $A_\Psi$, namely $M^{\pm1/2}=\sum_{n\ge0}\binom{\pm1/2}{n}(-\tfrac{g_s}{5}A_\Psi)^n$; this
needs no positivity or convergence, only the formal-series layer A1. $M^{1/2}$, $M^{-1/2}$ are
$p$-self-adjoint, being polynomials in the single $p$-self-adjoint operator $A_\Psi$.

### Derivation

**(5.1) The candidate.** Put
$$
G(\Psi):=M_\Psi^{-1/2},
\qquad
\hat R_u:=\big(\partial_uG\big)G^{-1}=\big(\partial_uM_\Psi^{-1/2}\big)M_\Psi^{1/2} .
\tag{5.1}
$$

**(5.2) $\hat R$ is flat.** By the pure-gauge computation of §4 (Commentary),
$\mathcal E[\hat R]=0$ **identically, to all orders in $g_s$**, for every $u_1,u_2$ and every
$\tilde X$. Equivalently: the law $\delta\tilde X=\hat R_u\tilde X$ integrates to
$\tilde X=G(\Psi)\hat Y$ with
$$
\boxed{\;\hat Y:=M_\Psi^{1/2}\,\tilde X,\qquad \delta\hat Y=0\;}
\tag{5.2}
$$
— the deviation is *inert* in the variable $\hat Y$, and a law with a $\Psi$-independent
transformation rule has vanishing closure defect trivially.

**(5.3) $\hat R$ is admissible.** Write $N:=M_\Psi^{1/2}$, so $M=N^2$, $N^\star=N$ and
$\partial_uN^{-1}=-N^{-1}(\partial_uN)N^{-1}$. Admissibility (3.2) requires
$\operatorname{Sym}(K_\Psi\hat R_u)=-\tfrac12\partial_uK_\Psi$, i.e., after stripping the
common left factor $p$ and using $(pZ)^{\rm T}=pZ^\star$ with
$\big(M(\partial_uN^{-1})N\big)^\star=N(\partial_uN^{-1})M$:
$$
\tfrac12\Big[M(\partial_uN^{-1})N+N(\partial_uN^{-1})M\Big]
=\tfrac12\Big[-N(\partial_uN)-(\partial_uN)N\Big]
=-\tfrac12\,\partial_u\big(N^2\big)=-\tfrac12\,\partial_uM .
\tag{5.3}
$$
✓, **exactly and to all orders in $g_s$**. Equivalently: $G^{\rm T}K_\Psi G=
p\,M^{-1/2}MM^{-1/2}=p$, so $\hat R$ is the connection that trivialises the dressed form,
$K_\Psi(\tilde X,\tilde X)=p_{2,2}(\hat Y,\hat Y)$ with $\hat Y$ inert — invariance is
manifest.

**(5.4) The shift, in closed form.** Expanding (5.1) with
$M^{-1/2}=1+\tfrac{g_s}{10}A_\Psi+\tfrac{3g_s^2}{200}A_\Psi^2+O(g_s^3)$ and
$M^{1/2}=1-\tfrac{g_s}{10}A_\Psi-\tfrac{g_s^2}{200}A_\Psi^2+O(g_s^3)$,
$$
\hat R_u=\tfrac{g_s}{10}A_u+g_s^2\Big(\tfrac{3}{200}A_\Psi A_u+\tfrac{1}{200}A_uA_\Psi\Big)
+O(g_s^3),
\qquad
R_u=\tfrac{g_s}{10}A_u+\tfrac{g_s^2}{50}A_\Psi A_u+O(g_s^3),
$$
$$
\boxed{\;\Delta R_u=\hat R_u-R_u=-\frac{g_s^2}{200}\,\big[A_\Psi,A_u\big]+O(g_s^3)\;}
\tag{5.4}
$$
— $\mathfrak k$-valued ($[\mathfrak p,\mathfrak p]\subset\mathfrak k$) ✓, linear in $u$ ✓,
$O(g_s^2)$ so no $g_s^1$ defect is created (4.4) ✓, $N_{\rm gh}$-preserving and even ✓,
polynomial in $\Psi$ from the vertices alone ✓.

**(5.5) Second route — the Poincaré lemma, independent of the square root.** $A_u$ is linear
in $u$ and **independent of $\Psi$**, so $\omega(u_1,u_2):=[A_{u_1},A_{u_2}]$ is a
constant-coefficient $\mathfrak k$-valued 2-form on the vector space $\mathcal H_0$. Every
such form is exact, with the explicit Euler-vector primitive
$\eta_u(\Psi)=\tfrac12\,\iota_\Psi\omega=\tfrac12[A_\Psi,A_u]$:
$\mathrm d\eta(u_1,u_2)=\tfrac12[A_{u_1},A_{u_2}]-\tfrac12[A_{u_2},A_{u_1}]=\omega(u_1,u_2)$.
Hence $\Delta^{(2)}_u=-\tfrac{1}{200}[A_\Psi,A_u]$ solves $\mathrm d\Delta^{(2)}
=-\tfrac1{100}\omega$, killing the $g_s^2$ defect in (4.5) with
$\Delta^{(1)}=0$. This reproduces (5.4) **without** using $M^{1/2}$, and shows that the
removal at order $g_s^2$ needs nothing beyond the contractibility of field space.

**(5.6) Order-$g_s^2$ verification by hand.** With $\hat R$ of (5.4):
$\partial_{u_1}\hat R_{u_2}-\partial_{u_2}\hat R_{u_1}
=g_s^2\,\tfrac{2}{200}\,[A_{u_1},A_{u_2}]
=\tfrac{g_s^2}{100}[A_{u_1},A_{u_2}]$ and
$[\hat R_{u_2},\hat R_{u_1}]=\tfrac{g_s^2}{100}[A_{u_2},A_{u_1}]
=-\tfrac{g_s^2}{100}[A_{u_1},A_{u_2}]$: the sum vanishes. Compare 040's split for $R$,
$\tfrac1{50}-\tfrac1{100}=\tfrac1{100}$: the shift moves the *first* term from $\tfrac1{50}$
to $\tfrac1{100}$ and leaves the second, exactly the $-\tfrac1{100}$ of $\mathrm d\Delta^{(2)}$.

**(5.7) The hinge: the shift is a trivial symmetry.** $\Delta R_u\tilde X$ is a shift of the
gauge law of $\tilde X$; with $E_\Sigma=-\tfrac{g_s^2}{12}K_\Psi\tilde X$ (R22),
$$
\Delta R_u\tilde X=K_\Psi^{-1}S_u\tilde X=\mu\,E_\Sigma,
\qquad
\mu=-\tfrac{12}{g_s^2}K_\Psi^{-1}S_uK_\Psi^{-1},
\qquad \mu^{\rm T}=-\mu ,
\tag{5.5}
$$
because $S_u$ is antisymmetric and $K_\Psi$ symmetric. For **even** fields HT-triviality
requires exactly an antisymmetric $\mu$ (R22 (1), derived there from first principles with the
parameter-parity factor dropping out). So every admissible $\Delta R_u$ **is** a trivial
symmetry, and conversely every trivial symmetry of the $\tilde X$-linear form is admissible:
the identification the brief asks to check holds, and it is *complementary* to R22, which
found the **forced** part of $R_u$ to have a **symmetric** $\mu$ and therefore not to be
trivial. For (5.4), $S_u=-\tfrac{g_s^2}{200}K_\Psi[A_\Psi,A_u]$, antisymmetric at leading
order because $p[A_\Psi,A_u]$ is. [check: `D4`, `D4-break`]

### Commentary

- The geometric content in one sentence: $R$ is a metric connection for the $\Psi$-dependent
  form $K_\Psi$, its curvature is the defect, and a metric on a **contractible** base is
  trivialisable — so a *flat* metric connection exists, and the curvature of the particular
  representative R17 chose is not an invariant of the problem.
- Why R17's representative is curved at all: (3.4) is the symmetric logarithmic derivative
  $-\tfrac12M^{-1}\partial_uM$, while the flat one is $(\partial_uM^{-1/2})M^{1/2}$. The two
  agree iff $A_\Psi$ and $A_u$ commute; their difference is precisely $-\tfrac{g_s^2}{200}
  [A_\Psi,A_u]$, the same commutator whose antisymmetrised derivative is the defect. The
  "generically nonzero" of R45 (GAP-2) is therefore the statement that R17's choice is
  generically *not* the flat one — not that no flat one exists.
- **Limiting case $g_s\to0$**: $\Delta R_u=O(g_s^2)\to0$, $\hat Y\to\tilde X$, $\delta\tilde X
  \to0$: R11 is recovered, and the flat representative is *the* one in which the **form** of
  R11's statement "$\delta X=0$" survives at $O(g_s^3)$: the deviation variable is inert, now
  $\hat Y=M_\Psi^{1/2}\tilde X$, which reduces to R11's $X$ only as $g_s\to0$ ($\hat Y=X$ only
  at $g_s^0$, and R11's statement is finite while this one is infinitesimal).
- **Regime**: the argument uses no property of $\mathcal V_4,\mathcal V_5$ beyond total
  symmetry (giving $A_w^\star=A_w$) and invertibility of $p_{2,2}$ on the quotient (PH1/PH5).
  It is therefore *independent of $N$* and does **not** inherit GAP-2's $N=2$ genericity
  limit: GAP-2 concerns whether $[A_{u_1},A_{u_2}]\neq0$, which is what makes the *R17*
  representative curved; the removal works whether or not that commutator vanishes.
- Uniqueness of the preferred representative: $\hat R$ is unique up to a $\Psi$-independent
  $K$-orthogonal rotation of $\hat Y$ (the residual freedom $\Delta R'\in\mathfrak k_{K_\Psi}$
  with $\mathrm d\Delta R'+[\Delta R',\Delta R']=0$, i.e. flat $\mathfrak k$-connections on a
  contractible base, all pure gauge). The canonical choice is (5.1).

### Result

$$
\boxed{\;\text{\bf Removable.}\quad
\hat R_u=\big(\partial_uM_\Psi^{-1/2}\big)M_\Psi^{1/2}
=R_u-\tfrac{g_s^2}{200}[A_\Psi,A_u]+O(g_s^3)
\quad\Longrightarrow\quad \mathcal E[\hat R]=0\ \text{exactly}\;}
$$
$\mathcal E[\hat R]=0$ identically — as an exact identity in $g_s$ for the quintic-truncated
action $S_3$, whose entire $\tilde X$-dependence is the quadratic form
$K_\Psi(\tilde X,\tilde X)$ (A3, 011 (B.2)); at $O(g_s^4)$ that premise must be re-established
before the statement is extended. $\hat R$ satisfies the invariance condition (3.1) exactly,
differing from R17's representative by a Henneaux–Teitelboim **trivial symmetry**. In the
variable
$\hat Y=M_\Psi^{1/2}\tilde X$ the law is $\delta\hat Y=0$ and
$S_3=S^{(5)}_{\rm eff}(\Psi)-\tfrac{g_s^2}{4!}p_{2,2}(\hat Y,\hat Y)
+\tfrac{g_s^4}{600}vK_\Psi^{-1}v$ with a $\Psi$-**independent** auxiliary kinetic form.
Consequently
$$
[\delta_{\Lambda_1},\delta_{\Lambda_2}]\Sigma_2
=\delta_{\Lambda_{12}}\Sigma_2+\hat\Phi_{\rm exact}(\mathcal D_\Psi)
\qquad\text{(no }\mathcal E\text{), to all orders in }g_s\text{ within }S_3 :
$$
the algebra closes **modulo the $\Psi$ equation of motion alone**. The
$E_\Sigma$-proportional defect of R45 is a property of the R17/011 (B.8) representative, not
of the theory.

### Verification

Script Part D: `D1` (admissibility of the family, and that $R$ is the symmetric part),
`D2` ($\mathcal E$ transforms by (4.3)), `D3` ($\mathcal E[\hat R]=0$ to $O(g_s^4)$ on random
data, and (5.4) as its $g_s^2$ truncation), `D4` (the shift is a trivial symmetry: $\mu$
antisymmetric), `D5` ($G^{\rm T}K_\Psi G=p$ and $\delta\hat Y=0$), each with a break leg;
plus the re-check that $\mathcal E[R]\neq0$ on the same data (so the checks are not vacuous).

## Claim tree

- **A1** Algebraic layer: finite-dimensional $\mathcal H_0$, generic totally symmetric
  $\mathcal V_4,\mathcal V_5$, formal power series in $g_s$,
  $\Sigma_2\in\operatorname{Sym}^2\mathcal H_0/\ker\mathcal V_4$.
- **A2** Conventions of 040 §1 (physical $N_{\rm gh}$, degree parity, R43 normalisation);
  $\mathcal E$ of 040 (5.11) and its $g_s^2$ value (R45) are taken as given, not re-derived.
- **A3** $S_3$ depends on $\tilde X$ only through $K_\Psi(\tilde X,\tilde X)$ — 011 (B.2),
  exact because $S_3$ is quadratic in $\Sigma_2$. This is what makes the invariance condition
  (3.1) the *only* condition on the law. This is exact for $S_3$ and is the step that fails
  first beyond the quintic truncation.
- **A4** $M_\Psi^{\pm1/2}$ exist as formal power series in $g_s$ with coefficients polynomial
  in $A_\Psi$ (A1; no positivity, no convergence).
- **C1** The admissible family is exactly $\hat R_u=R_u+K_\Psi^{-1}S_u$ with $S_u$
  antisymmetric, linear in $u$, $O(g_s)$, $N_{\rm gh}$-preserving, even, algebraic in $\Psi$;
  equivalently $\operatorname{Sym}(K_\Psi\hat R_u)=\tfrac{g_s}{10}P_u$. Nothing else is
  constrained (§2 items 1–10). [by A2, A3; eqs. (3.1)–(3.3)] [check: `D1`, break-`D1` — tests
  (3.2) only; ghost number, parity, reality, quotient and algebraicity (§2 items 5, 6, 8, 9)
  are checked by inspection, not by `D1`'s random $S_u$]
  - **C1.1** The same condition also admits terms of higher degree in $\tilde X$
    ($T^{(n\ge2)}$ with $K_\Psi(T^{(n)}(\tilde X^n),\tilde X)=0$) and forbids a
    $\tilde X$-independent term. Recorded, not used; it only enlarges the family.
    [by A3; §2 item 4]
- **C2** $\mathcal E$ is (minus) the curvature of $\hat R$ read as a connection on field
  space, and under $R\to R+\Delta R$ it transforms as
  $\mathcal E[R+\Delta R]=\mathcal E[R]+\nabla^R\!\Delta R+[\Delta R\wedge\Delta R]$ — both
  the $(\partial_\Psi R)$ term and the $[R,R]$ term move. [by A2, C1; eqs. (4.1)–(4.5)]
  [check: `D2`, break-`D2`]
  - **C2.1** A shift with a nonzero $O(g_s)$ part generically creates a defect at $g_s^1$,
    one order below R45's; removal therefore requires $\Delta R=O(g_s^2)$ or a closed
    $\Delta^{(1)}$. [by C2; eq. (4.4)]
- **C3** **Removable.** $\hat R_u=(\partial_uM_\Psi^{-1/2})M_\Psi^{1/2}$ is admissible
  exactly (5.3) and flat exactly (5.2): $\mathcal E[\hat R]=0$ identically — as an exact
  identity in $g_s$ for the quintic-truncated action $S_3$, whose entire $\tilde
  X$-dependence is the quadratic form $K_\Psi(\tilde X,\tilde X)$ (A3, 011 (B.2)); at
  $O(g_s^4)$ that premise must be re-established before the statement is extended. Its
  shift from the R17 representative is
  $\Delta R_u=-\tfrac{g_s^2}{200}[A_\Psi,A_u]+O(g_s^3)$. Hence the $E_\Sigma$-proportional
  defect of R45 is a property of the R17/011 (B.8) representative, not of the theory, and
  the algebra closes modulo the $\Psi$ equation of motion **alone**.
  [by A3, A4, C1, C2; §5.1–§5.6] [check: `D0`, `D3`, `D3-closed`, break-`D3`, `D5`,
  break-`D5`]
  - **C3.1** Second, independent route at order $g_s^2$: $[A_{u_1},A_{u_2}]$ is a
    constant-coefficient 2-form on the vector space $\mathcal H_0$, hence exact, with
    primitive $\tfrac12[A_\Psi,A_u]$ — reproducing (5.4) without the square root.
    [by C2; §5.5] [analytic only — `D3-closed` compares the resulting shift with route 1's
    closed form, not $\mathrm d\eta=\omega$ itself, so it does not separately test this route]
  - **C3.2** The hinge holds: an admissible $\Delta R_u$ is exactly a Henneaux–Teitelboim
    **trivial symmetry** ($\mu=-\tfrac{12}{g_s^2}K_\Psi^{-1}S_uK_\Psi^{-1}$ antisymmetric,
    the condition R22 derived for even fields), complementary to R22's finding that the
    *forced* part has symmetric $\mu$ and is not trivial. So $\mathcal E$ is killed by a
    trivial symmetry and was never physical. [by C1, R22; eq. (5.5)] [check: `D4`,
    break-`D4`]
  - **C3.3** Preferred representative: $\hat Y:=M_\Psi^{1/2}\tilde X$ is **inert**
    ($\delta\hat Y=0$) and $K_\Psi(\tilde X,\tilde X)=p_{2,2}(\hat Y,\hat Y)$ with a
    $\Psi$-independent kinetic form — the **form** of R11's "$\delta X=0$" survives at
    $O(g_s^3)$: the deviation variable is inert, now $\hat Y=M_\Psi^{1/2}\tilde X$, which
    reduces to R11's $X$ only as $g_s\to0$. That $(\hat Y,\hat Y^+)$ is a
    constant-coefficient contractible pair is **expected, not derived** (GAP-3e). [by C3;
    (5.2)] [check: `D5`, `D5-inert`]
  - **C3.4** The verdict does **not** inherit GAP-2's $N=2$ genericity limit: it uses only
    total symmetry of the vertices ($A_w^\star=A_w$) and invertibility of $p_{2,2}$ on the
    quotient (PH1/PH5), for any $N$ and any vertices. GAP-2 concerns whether
    $[A_{u_1},A_{u_2}]\neq0$, i.e. whether R17's representative is curved at all; the removal
    holds either way. [by §5, Commentary]
- **C4** Limiting case $g_s\to0$: $\Delta R_u=O(g_s^2)\to0$, $\hat R\to0$,
  $\hat Y\to\tilde X$, and R11's rigid slaving is recovered; the two representatives agree
  at $O(g_s)$ and first differ at $g_s^2$. [by C3; §5 Commentary] [check: `D3-closed`]

Open gaps: [GAP-3a] closed 2026-09-26 (analytic all-orders proof; machine check at $N=2$ and $N=3$ through $g_s^5$, 54/54 PASS); [GAP-3b] open — the $\mathcal F$-proportional defect $\mathcal D_\Psi$ is not addressed, and the openness of the closed-SFT gauge algebra (Zwiebach 1993) stands; [GAP-3c] closed 2026-09-26 by the addendum (C5; node check 2026-09-30) — unique up to $\Psi$-dependent $p$-preserving relabellings $h_\Psi$, $h_0=\mathrm{id}$, each a pure-gauge trivial symmetry with $\mathcal E=0$; $\Psi$-independent relabellings of $\hat Y$ leave the law unchanged; [GAP-3d] closed by 053 (R57); [GAP-3e] closed by 056 (R60), properness of the BV extension by R62 ($k\le3$, PH27), open at $O(g_s^4)$ (Task 7b).
Hypotheses in force: PH1, PH5; PH14 for the $O(g_s^4)$ clauses of C5.1, C5.5, C5.7; PH27 for the properness clause of C5.7 only.

## 6. Verification

`codes/verify-gauge-algebra-ogs3.py`, **Part D** (new; Parts A–C untouched and still
passing), seed `20260922`, $N=2$, exact rational arithmetic, truncation $g_s^4$ (one order
above Part C). Part D adds 8 checks + 5 break legs; totals after the addition: 29 checks,
12 break legs, exit 0.

| check | content | break leg |
|---|---|---|
| `D0` | $\mathcal E[R]\neq0$ on this data (R45) — makes `D3` non-vacuous | — |
| `D1` | admissibility ⟺ $\operatorname{Sym}(K_\Psi\hat R_u)=\tfrac{g_s}{10}P_u$; preserved by antisymmetric $S_u$ | a **symmetric** $S_u$ breaks admissibility |
| `D2` | the transformation law (4.3), with a generic admissible $O(g_s^2)$ shift | dropping the cross brackets $[R,\Delta R]$ breaks it |
| `D3` | $\mathcal E[\hat R]=0$ through $g_s^4$ | coefficient $-\tfrac1{200}\to-\tfrac1{100}$ leaves $\mathcal E\neq0$ (sharpness) |
| `D3-closed` | $\Delta R_u=-\tfrac{g_s^2}{200}[A_\Psi,A_u]+O(g_s^3)$, no $g_s^0$ or $g_s^1$ part | (shares `D3`'s leg) |
| `D4` | $K_\Psi\Delta R_u$ antisymmetric ⟹ HT-trivial symmetry | the **forced** $K_\Psi R_u$ is symmetric, not antisymmetric (R22) — the test discriminates |
| `D5` | $G^{\rm T}K_\Psi G=p_{2,2}$ for $G=M_\Psi^{-1/2}$ | $G=M_\Psi^{+1/2}$ does *not* trivialise: the branch matters |
| `D5-inert` | **structural**: $\delta\hat Y=0$ (integrates (5.2); cannot fail by construction, labelled as such) | — |

**Depth checklist.** (i) *limiting case*: $g_s\to0$, C4, checked by `D3-closed`; (ii)
*dimensional/grading*: $N_{\rm gh}$ and Grassmann parity of $\Delta R_u$ checked by
inspection (§2 items 5–6, §5.4) — $A_w$ preserves $N_{\rm gh}=4$ on $\operatorname{Sym}^2$
for $N_{\rm gh}(w)=2$, and every operator here is even; (iii) *second method*: §5.5 (Poincaré lemma) reproduces the removal at order $g_s^2$ by an
independent mechanism; the all-orders statement has a single route, corroborated to $g_s^4$
by `D3`; (iv) *special case*:
if $A_\Psi$ and $A_u$ commute, $\hat R=R$ and both are flat — consistent with $\mathcal E
\propto[A_{u_1},A_{u_2}]$; (v) *regime*: any $N$, any totally symmetric vertices, formal
series in $g_s$, action $S_3$ (quintic truncation).

**Reality and the quotient** (checked by inspection, not by machine): $M_\Psi^{\pm1/2}$ is a
real power series in $A_\Psi$, so $\hat R$ preserves the reality condition
$\Sigma^\ddagger=\Sigma$ and the quotient $\operatorname{Sym}^2\mathcal H_0/\ker\mathcal V_4$
whenever $A_\Psi$ does — the same requirement $R_u$ already carries (PH1/PH5).

**GAP-3a extension (2026-09-26).** A second, independent invocation
`part_D(N=3, gord=5)` (same script, same seed `20260922`) repeats every check of the table
above at $N=3$ (pair-basis dimension $n=6$, vs. $n=3$ at $N=2$) and truncation $g_s^5$ (one
order beyond the table's $g_s^4$): `D0-N3g5` through `break-D5-N3g5`, 8 checks + 5 break
legs, all PASS (54 PASS / 0 FAIL for the whole script, exit 0; log
`agent/scratch/gauge-ogs3-run-N3.log`). In particular `D0-N3g5` again shows
$\mathcal E[R]\neq0$ on this data (so `D3-N3g5` is not vacuous), and `D3-N3g5` shows
$\mathcal E[\hat R]=0$ identically through $g_s^5$: the all-orders flatness of $\hat R$ is
now corroborated one $g_s$-order and one $H_0$-dimension beyond the original run, with the
same exact rational arithmetic throughout (no floats introduced). The run was expensive —
wall time $\approx3.6\times10^4$ s ($\approx10$ h), dominated by entrywise `sp.simplify` on
the $6\times6$ matrices at $g_s^5$ rather than by the linear algebra — but that cost is
purely computational and introduces no new approximation into the check.

## 7. Result

**GAP-3 is settled: the $E_\Sigma$-proportional defect is removable.**

1. The admissible freedom in the $\Sigma_2$ gauge law is exactly
   $\hat R_u=R_u+K_\Psi^{-1}S_u$ with $S_u$ antisymmetric (C1), and it is exactly the set of
   Henneaux–Teitelboim trivial symmetries (C3.2) — the hinge of the brief, checked, not
   assumed.
2. $\mathcal E$ is the curvature of $R$ read as a connection on field space (C2); the R17
   representative is the symmetric-logarithmic-derivative metric connection
   $-\tfrac12M_\Psi^{-1}\partial_uM_\Psi$, and its curvature is
   $\tfrac{g_s^2}{100}[A_{u_1},A_{u_2}]$.
3. The metric $K_\Psi$ lives over a **contractible** base, so a flat metric connection exists:
   $\hat R_u=(\partial_uM_\Psi^{-1/2})M_\Psi^{1/2}$, admissible and flat — $\mathcal E[\hat
   R]=0$ identically, as an exact identity in $g_s$ for the quintic-truncated action $S_3$
   (A3, 011 (B.2)); at $O(g_s^4)$ that premise must be re-established before the statement is
   extended (C3) — differing from R17's choice by the trivial symmetry
   $-\tfrac{g_s^2}{200}[A_\Psi,A_u]+O(g_s^3)$.
4. In the preferred representative, $\hat Y=M_\Psi^{1/2}\tilde X$ is inert, the auxiliary
   kinetic form is $\Psi$-independent, and
   $[\delta_{\Lambda_1},\delta_{\Lambda_2}]\Sigma_2=\delta_{\Lambda_{12}}\Sigma_2
   +\hat\Phi_{\rm exact}(\mathcal D_\Psi)$: **the algebra closes modulo the $\Psi$ equation of
   motion alone, within the quintic-truncated action $S_3$; at $O(g_s^4)$ this must be
   re-established.**
5. What survives of R45: the identity 040 (5.11), the exact $\tilde X$-proportionality of
   $\mathcal E$, the absence of a new gauge parameter, and the value
   $\tfrac{g_s^2}{100}[A_{u_1},A_{u_2}]$ **in the R17/011 (B.8) representative**. What does
   not survive: "the algebra closes modulo **both** equations of motion" as a statement about
   the theory, and the classification of $\lambda^\Sigma$ as a genuine $E$-structure function
   — it is a trivial-symmetry coboundary and can be set to zero (**expected, not derived**:
   the canonical transformation induced on $\Psi^+$ by $\hat Y=M_\Psi^{1/2}\tilde X$ is not
   written here; see GAP-3e).
6. The verdict does not inherit GAP-2's $N=2$ limit (C3.4). GAP-2 remains relevant only to
   the (now secondary) statement that R17's representative is curved for generic vertices.

## Self-review

- **Objective vs. literal task.** The literal task — characterise $\Delta R_u$, transform
  $\mathcal E$ under it, and decide removability — is answered positively (C1–C3). The
  motivating objective, deciding whether R45's "closes modulo **both** equations of motion"
  and the quintic gauge paragraph of the notes are wrong, is met **within $S_3$**: there the
  removal is exact, so that reading of R45 does not survive as a statement about the theory.
  It is not met beyond $S_3$: at $O(g_s^4)$, once $\mathcal V_6$ and $\Sigma_3$ enter, A3
  fails and the question re-opens (GAP-3d).
- **Weakest step, and what was done about it.** A3 — that $S_3$'s entire $\tilde
  X$-dependence is the quadratic form $K_\Psi(\tilde X,\tilde X)$, exact only because $S_3$
  is the quintic truncation. Everything downstream (the family C1, the flatness C3) is
  conditioned on it. The restriction is now stated everywhere the verdict itself is stated —
  the boxed Result, §7.3–7.4, the claim-tree C3 node, the Status line and the script
  docstring — not only at A1/A3, so a reader cannot take the boxed Result without the scope.
- **What was not checked, and why that is acceptable.** (i) The $O(g_s^4)$ survival of A3
  itself: out of scope for closing GAP-3 as posed within $S_3$; flagged as GAP-3d. (ii) The
  BV/antifield consequences claimed in §7.5 and C3.3 — the $(\hat Y,\hat Y^+)$
  constant-coefficient contractible pair, the canonical transformation on $\Psi^+$, benign
  inheritance by 015 §4 — are asserted, not derived; labelled as expectations and recorded as
  GAP-3e, since establishing them is a separate BV computation outside the algebraic-layer
  scope (A1). (iii) `D3-closed`'s tag on C3.1 does not test the Poincaré-lemma route's own
  step ($\mathrm d\eta=\omega$); the tag is dropped there and C3.1 is marked analytic only.
- **What a stronger reader would find in five minutes.** Before this pass: the boxed Result,
  §7, the claim-tree C3 node and the Status line all read "exactly, to all orders in $g_s$"
  with no mention that this is a statement about $S_3$, not about the full theory — a reader
  who stopped at the boxed Result or §7.3 would not know the premise fails at $O(g_s^4)$. The
  check counts (9 checks + 4 break legs, 30 checks + 11 break legs) also did not match Part D
  of the script (8 checks + 5 break legs; 29 + 12 for the whole script) and would fail on
  inspection.

## Status

*2026-09-26 (orchestrator, bookkeeping):* GAP-3d closed by record 053 (R57) — at $O(g_s^4)$ the premise (quadratic auxiliary dependence) fails but the conclusion survives via the Morse map; GAP-3a's $N=3$, $g_s^5$ machine run (`agent/scratch/gauge-ogs3-run-N3.log`) has since
finished, all PASS (54/54, exit 0; wall time $\approx10$ h) — GAP-3a is closed (§6, Open
gaps).

**Complete.** Skeleton and constraint enumeration (§2) → admissible family (§3, C1) →
transformation of $\mathcal E$ (§4, C2) → verdict (§5, C3; exact within the quintic-truncated
$S_3$, open at $O(g_s^4)$ — GAP-3d) → Part D of `codes/verify-gauge-algebra-ogs3.py` (8
checks + 5 break legs, all PASS, Parts A–C untouched) → record consolidated. Next
(orchestrator): rewrite R45 per the replacement row in
`agent/reports/computator-gap3-20260922T210000.md`; the quintic gauge paragraph of the notes
and the $O(g_s^4)$ BV analysis (015 §4) both inherit the change.
2026-09-26: GAP-3e (§7 item 5) settled by record 056 → ledger R60 (contractible pair in the hatted chart; conditional on the $\Psi$-sector master equation, Task 7).

## Addendum 2026-09-26 — GAP-3c

*Brief `computator-gap3c-20260926T101500`. Append-only: nothing above this heading is edited.
The addendum's nodes C5.* continue the record's tree, and its `Open gaps:` line (A.6)
supersedes the GAP-3c clause of the record's `Open gaps:` line.*

### A.0 Task, objective, reading adopted

**Literal task.** Show that the residual freedom named by GAP-3c — "$\hat R$ is unique only
up to a $\Psi$-independent $K$-orthogonal rotation of $\hat Y$ and up to the higher-degree
freedom C1.1" — carries no physical content: (i) the rotation changes $\hat R$ by a
trivial-symmetry term and leaves $\mathcal E$ unchanged at every order; (ii) likewise for
C1.1; (iii) the BV chart of 056 is unaffected; (iv) the falsifier "a rotation that changes
$\mathcal E$ at fixed order" cannot exist, or is exhibited.

**Objective.** Close the last open gap of R45 other than GAP-3a's machine run, so that the
ledger can state the flat representative as unique up to trivial symmetries.

**Reading adopted (justified in A.1–A.2).** The GAP-3c sentence conflates two different
freedoms, and the literal item (i) concerns the one without content:

- (α) *For a fixed law*, the inert variable is defined up to a $\Psi$-**independent**
  invertible map $L$ of $\hat Y$; requiring its kinetic form to stay $p$ restricts $L$ to
  $\mathrm{Diff}_p(V)$ ($\mathrm O(p)$ for linear $L$). Such an $L$ does **not change the law at all** (C5.2): $\Delta\hat R=0$, the
  trivial-symmetry form with $S=0$.
- (β) *The law itself* is not unique: the flat admissible laws are those of
  $h_\Psi\circ\mathcal G_\Psi$ with $h_\Psi$ a $\Psi$-**dependent** map preserving
  $p(\hat Y,\hat Y)$ (C5.1). This is the freedom with content; (i)–(iv) are answered for it.

The record's parenthetical tangent condition "$\mathrm d\Delta R'+[\Delta R',\Delta R']=0$"
should read $\nabla^{\hat R}\Delta R'+[\Delta R'\wedge\Delta R']=0$ (043 (4.3) with $\mathcal
E[\hat R]=0$); in the $\hat Y$ frame it becomes a flat $\mathfrak k$-connection, which is the
statement of (β). The brief's proposed break leg — "a non-orthogonal $O$ changes $\mathcal E$
or breaks admissibility" — fails for a $\Psi$-independent $O$ (any constant $L$ leaves the law
unchanged, C5.2); the break that separates the properties is a $\Psi$-**dependent**
non-orthogonal map, which keeps flatness and breaks admissibility (C5.3). The script is built
on that break.

**Convention.** 053/056: $\hat Y=\mathcal G_\Psi(\tilde X)$, law $F_u=-(D\mathcal G)^{-1}
\partial_u\mathcal G$. At $O(g_s^3)$, $\mathcal G=M_\Psi^{1/2}$ (043's $G=\mathcal G^{-1}$)
and $\hat R_u=-\mathcal G^{-1}\partial_u\mathcal G=(\partial_uM^{-1/2})M^{1/2}$, 043 (5.1).
Write $Q(\tilde X):=K_\Psi(\tilde X,\tilde X)$ at $O(g_s^3)$ and
$Q(Y):=-\tfrac{24}{g_s^2}\Phi^*(Y;\Psi)$ at $O(g_s^4)$ (053 (5.2)); in both cases
$$
p\big(\mathcal G_\Psi(\cdot),\mathcal G_\Psi(\cdot)\big)=Q
\qquad\text{(043 (5.3) } G^{\rm T}K_\Psi G=p\text{; 053 (5.5))},
\tag{A.0}
$$
admissibility is $DQ\cdot F_u+\partial_uQ=0$ (043 (3.1), 053 (3.2)), and flatness is
$\mathcal E[F]=0$ with $\mathcal E$ of 053 (4.1) (043 (4.1) for linear laws).

### A.1 The residual family, exactly (C5.1)

**Setup.** A1–A4 of the record; 053 A1–A4 for the $O(g_s^4)$ clause. Laws are formal in
$\tilde X$ (C1.1 included) and in $g_s$. $\mathrm{Diff}_p(V)$: formal diffeomorphisms $h$ of
$V$ fixing $0$ with $p(h(\hat Y),h(\hat Y))=p(\hat Y,\hat Y)$; $\mathrm O(p)$ its linear part. ($h(0)=0$ is forced: $F'_u(0)=0$ by §2 item 4, so $\mathcal G'_\Psi(0)$ is $\Psi$-independent.)

**Derivation.** *Composition formula.* For any $\Psi$-dependent formal diffeomorphism
$h_\Psi$ of $V$ and $\mathcal G'=h_\Psi\circ\mathcal G_\Psi$: $D\mathcal G'=(Dh\circ\mathcal G)
\,D\mathcal G$ and $\partial_u\mathcal G'=(\partial_uh)\circ\mathcal G+(Dh\circ\mathcal G)\,
\partial_u\mathcal G$, so
$$
F^{h}_u:=-(D\mathcal G')^{-1}\partial_u\mathcal G'
=F_u+(D\mathcal G)^{-1}\,\big(w_u\circ\mathcal G\big),
\qquad
w_u:=-(Dh)^{-1}\partial_uh .
\tag{A.1}
$$
In particular $F^h=F$ iff $\partial_uh=0$ for all $u$: two maps give the same law iff they
differ by a $\Psi$-independent left factor.

*Every flat admissible law is of this form.* Let $F'$ be flat and admissible. Flat $\Rightarrow$
pure gauge, $F'=-(D\mathcal G')^{-1}\partial_u\mathcal G'$ for some $\mathcal G'_\Psi$ (053 §5
*Criterion*, ($\Rightarrow$): Frobenius on the contractible base, order by order in $g_s$),
fixed by $F'$ up to a $\Psi$-independent left factor (A.1). Admissible $\Rightarrow$
$Q\circ\mathcal G'^{-1}_\Psi$ is $\Psi$-independent (same place: $\partial_u[Q(\mathcal
G'^{-1}(\hat Y))]=\partial_uQ+DQ\cdot F'=0$). Use the left factor to impose $\mathcal
G'_0=\mathcal G_0$ at the base point $\Psi=0$. Then, for every $\Psi$,
$$
Q\circ\mathcal G'^{-1}_\Psi=Q_0\circ\mathcal G'^{-1}_0=Q_0\circ\mathcal G_0^{-1}
\overset{\rm (A.0)}{=}p ,
\tag{A.2}
$$
so $h_\Psi:=\mathcal G'_\Psi\circ\mathcal G_\Psi^{-1}$ satisfies $p\circ h_\Psi=p$ and $h_0=
\mathrm{id}$, and $F'=F^h$.

*Conversely*, for every $h:\Psi\mapsto h_\Psi\in\mathrm{Diff}_p(V)$ with $h_0=\mathrm{id}$,
$F^h$ is flat (pure gauge, 053 (4.2)) and admissible ($Q\circ(h\circ\mathcal G)^{-1}=p\circ
h^{-1}=p$ is $\Psi$-independent). The correspondence $h\mapsto F^h$ is injective: $F^{h_1}=
F^{h_2}$ forces $h_2\circ h_1^{-1}$ to be $\Psi$-independent (A.1), hence equal to its value
$\mathrm{id}$ at $\Psi=0$.

*Linear sector.* At $O(g_s^3)$, $\mathcal G$ is linear, and $F^h$ is linear in $\tilde X$ iff
$h_\Psi=H_\Psi\in\mathrm O(p)$. Conversely, if $F^h$ is linear then $k_\Psi=h_\Psi^{-1}$ solves $\partial_uk=w_u\circ k$, a linear ODE with $k_0=\mathrm{id}$, so $h_\Psi$ is linear. §2 item 7 ($\Delta R=O(g_s)$) forces $\partial_uH=O(g_s)$, so
$H=1+O(g_s)$ given $H_0=1$.

**Result.**
$$
\boxed{\;\{\text{flat admissible laws}\}=\big\{F^h:\ h_\Psi\in\mathrm{Diff}_p(V),\
h_0=\mathrm{id},\ h_\Psi\text{ ghost-number preserving, compatible with the quotient and the reality condition, polynomial in }\Psi\text{ at each order in }g_s,\ \partial_uh=O(g_s)\ \text{(043 §2 items 5, 7, 8, 9)}\big\},\ \text{bijectively};\quad
\text{linear sector: } h_\Psi=H_\Psi\in\mathrm O(p),\ H=1+O(g_s)\;}
$$
— at $O(g_s^3)$ within $S_3$ and, with $Q=-\tfrac{24}{g_s^2}\Phi^*$, at $O(g_s^4)$ within
$S_4$. The family is not reduced to a point: for instance $\Omega_\Psi=g_s^2\,(P\,v^{\rm T}-
p^{-1}v\,P^{\rm T}p)$, built from $P=\Psi\otimes\Psi$ and $v=p_{3,2}(\cdot,P,\Psi)$ (R17), is
$p$-antisymmetric, algebraic in $\Psi$ and vanishes at $\Psi=0$, and $H=e^{\Omega}$ is a
member. [check: `C5.1-base` — the base point $\hat R$ admissible and flat, $\mathcal E[R^{(17)}]
\neq0$ on the same data; the Frobenius and normalisation steps are analytic]

### A.2 Ψ-independent relabellings (C5.2) and Ψ-dependent rotations (C5.3)

**C5.2 — $\Psi$-independent $L$.** By (A.1) with $\partial_uL=0$, $F^L=F$ for **every**
$\Psi$-independent invertible $L$, orthogonal or not: $\Delta\hat R=0$, $S=0$, $\mathcal E$ and
everything built from the law are unchanged. What $L$ changes is the kinetic form of the
inert variable, $p\mapsto L^{-\rm T}pL^{-1}$, which stays $p$ iff $L\in\mathrm{Diff}_p(V)$ ($\mathrm O(p)$ for linear $L$). So the
"$\Psi$-independent $K$-orthogonal rotation of $\hat Y$" of GAP-3c is a relabelling of $\hat Y$
at fixed law, not a freedom of $\hat R$. [check: `C5.2`, `C5.2-nonorth`]

**C5.3 — $\Psi$-dependent $H\in\mathrm O(p)$.** (A.1) in the linear sector:
$$
\hat R^H_u=\hat R_u+\Delta R_u,\qquad
\Delta R_u=-\,\mathcal G^{-1}\big(H^{-1}\partial_uH\big)\,\mathcal G .
\tag{A.3}
$$
With $K_\Psi=\mathcal G^{\rm T}p\,\mathcal G$ (A.0), $K_\Psi\mathcal G^{-1}=\mathcal G^{\rm T}p$,
and $pH^{-1}=H^{\rm T}p$ ($H\in\mathrm O(p)$):
$$
S_u:=K_\Psi\Delta R_u=-\,\mathcal G^{\rm T}\big(H^{\rm T}p\,\partial_uH\big)\,\mathcal G,
\qquad
\big(H^{\rm T}p\,\partial_uH\big)^{\rm T}=(\partial_uH)^{\rm T}pH=-H^{\rm T}p\,\partial_uH ,
\tag{A.4}
$$
the last equality by differentiating $H^{\rm T}pH=p$. So $S_u^{\rm T}=-S_u$: $\Delta R\in
\mathfrak k_{K_\Psi}$ and $\Delta R_u\tilde X=\mu_uE_\Sigma$ with $\mu_u=-\tfrac{12}{g_s^2}
K_\Psi^{-1}S_uK_\Psi^{-1}$ antisymmetric — a Henneaux–Teitelboim trivial symmetry, by 043
(5.5)/C3.2. Its $O(g_s)$ part $-\partial_uH^{(1)}$ is exact, so no $g_s^1$ defect arises
(C2.1).

Equivalently, with the $\Psi$-dependent map
$$
g_\Psi:=\mathcal G^{-1}H^{-1}\mathcal G,\qquad g^{\rm T}K_\Psi g=\mathcal G^{\rm T}H^{-\rm T}p
H^{-1}\mathcal G=K_\Psi ,
\qquad
\hat R^H_u=g\hat R_ug^{-1}+(\partial_ug)g^{-1} .
\tag{A.5}
$$
Proof of the last form: under $\delta\tilde X=\hat R\tilde X$ the field $\tilde X':=g\tilde X$
has law $(\partial_ug+g\hat R_u)g^{-1}$, and $H\mathcal G\tilde X'=\mathcal G\tilde X=\hat Y$ is
inert, so that law is the one whose inert variable is $H\mathcal G(\cdot)$, i.e. $\hat R^H$.
Here $K_\Psi$ and $p$ are symmetric (indefinite) bilinear forms, so the group preserving them is the pseudo-orthogonal group $\mathrm O(r,s)$ of their signature: non-compact, not symplectic (a symplectic group would need an antisymmetric form; a Grassmann-odd sector, excluded by §2 item 6, would give $\mathrm{OSp}$). For nonlinear $L$ the relevant group is $\mathrm{Diff}_p(V)$. The map $\tilde X\mapsto g_\Psi\tilde X$ preserves $K_\Psi(\tilde X,\tilde X)$: it is a
field-dependent invariance of the auxiliary sector of $S_3$, and the residual family is the
orbit of $\hat R$ under these $K$-orthogonal relabellings — the "$\hat R\to O\hat RO^{-1}$-type"
transformation of the brief, with its inhomogeneous term. [check: `C5.3`, `C5.3-gauge`;
break: `C5.3-break` — a $\Psi$-dependent $p$-**symmetric** generator keeps the law flat and
breaks admissibility]

### A.3 The defect under the residual freedom (C5.4) and the falsifier (C5.6)

**Covariance.** For constant $u_1,u_2$ and $\nabla_u:=\partial_u-R_u$ acting on
$\operatorname{Sym}^2$-valued functions of $\Psi$,
$[\nabla_{u_1},\nabla_{u_2}]=-(\partial_1R_2-\partial_2R_1+[R_2,R_1])=-\mathcal E[R]$
(043 (4.2)). For any invertible $\Psi$-dependent $g$ put $g\cdot R:=gRg^{-1}+(\partial g)
g^{-1}$; since $g\,\partial_u(g^{-1}\,\cdot)=\partial_u-(\partial_ug)g^{-1}$,
$g\nabla_ug^{-1}=\partial_u-g\cdot R_u$, and
$$
\boxed{\;\mathcal E[g\cdot R]=g\,\mathcal E[R]\,g^{-1}\;}
\tag{A.6}
$$
exactly, for every law $R$ (admissible or not), every $g$, to all orders in $g_s$. The
nonlinear analogue is the covariance of the curvature (053 (4.1)) of an Ehresmann connection
under a vertical automorphism: with $\varphi_\Psi:=\mathcal G^{-1}\circ h_\Psi^{-1}\circ
\mathcal G$ (the nonlinear $g$ of (A.5)), $F^h=\varphi_*F$ and $\mathcal E_{\rm Lie}[F^h]=
\varphi_*\,\mathcal E_{\rm Lie}[F]$, which vanishes iff $\mathcal E_{\rm Lie}[F]$ does.

**Consequences.**

1. On the residual family, $\mathcal E[\hat R^H]=g\,\mathcal E[\hat R]\,g^{-1}=0$: identically,
   at every order of the formal $g_s$ expansion — exactly within the quintic-truncated $S_3$, and within $S_4$ under PH14 (R57); nothing is claimed beyond $S_4$ — for every $H$ (and every $h$ in the nonlinear sector). This is
   the brief's "$\mathcal E=0$ is preserved", now as an identity rather than an order-by-order
   observation. [check: `C5.4-flat` at two couplings and two models]
2. On a curved representative the same relabelling acts by conjugation. With $g=1+O(g_s)$
   (A.1, linear sector) and $\mathcal E[R^{(17)}]=\tfrac{g_s^2}{100}[A_{u_1},A_{u_2}]+O(g_s^3)$
   (R45),
   $$
   \mathcal E[g\cdot R^{(17)}]=\mathcal E[R^{(17)}]+O(g_s^3):
   \tag{A.7}
   $$
   the R45 leading coefficient and the (non)vanishing of $\mathcal E$ are invariants of the
   orbit; only subleading orders are conjugated. [check: `C5.4-cov` (the full identity (A.6)
   on $R^{(17)}$, an explicit law with no pure-gauge structure) and `C5.4-order` (halving
   ratios $7.91$ and $7.99$, against $8$ for $O(g_s^3)$)]

**The falsifier (C5.6).** *A rotation that changes $\mathcal E$ at fixed order* would be a
member of the residual family — a $K$-orthogonal $g_\Psi$ (A.5), or a $p$-preserving $h_\Psi$
— with $\mathcal E[g\cdot\hat R]\neq0$ at some order. By (A.6) and $\mathcal E[\hat R]=0$ this
is impossible: the statement is proved, not the outcome of a search. What does move
$\mathcal E$ is a trivial symmetry that is **not** of the pure-gauge form (A.3), for example
$\Delta R_u=K_\Psi^{-1}S_u$ with $S_u=g_s^2\,\mathsf Y(\Psi,u)$ antisymmetric but with
non-vanishing curl in $(\Psi,u)$: it is admissible, and $\mathcal E[\hat R+\Delta R]=
\nabla^{\hat R}\Delta R+[\Delta R\wedge\Delta R]\neq0$ (043 (4.3)). Such a shift is outside
the residual family, since it is not flat, and its defect is itself $\mathfrak
k_{K_\Psi}$-valued, i.e. again a trivial symmetry (043 (4.5), 053 (4.3)). [check:
`C5.4-break` — admissible to $10^{-15}$, $|\mathcal E|$ larger than $|\mathcal
E[R^{(17)}]|$ by $10^2$–$10^3$, $K_\Psi\mathcal E$ antisymmetric to $10^{-15}$]

### A.4 The higher-degree freedom C1.1 and the $O(g_s^4)$ family (C5.5)

**Every C1.1 term is a trivial symmetry.** An admissible law $F_u$ differs from $\hat R_u
\tilde X$ by a solution of the homogeneous condition $DQ\cdot(F_u-\hat R_u\tilde X)=0$, i.e.
an element of $\mathfrak{stab}(Q)$. By Koszul exactness (053 (3.4) at $T=0$, $\nu=\tilde X$),
$$
\mathfrak{stab}(Q)=\big\{K_\Psi^{-1}S(\tilde X)\,\tilde X:\ S(\tilde X)^{\rm T}=-S(\tilde X)
\big\}=\big\{\mu(\tilde X)E_\Sigma:\ \mu^{\rm T}=-\mu\big\},
\tag{A.8}
$$
the field-dependent trivial symmetries. So the higher-degree terms $T^{(n\ge2)}$ of C1.1 are
of trivial-symmetry form by the invariance condition itself, whether or not the law is flat.
At $O(g_s^4)$ the same statement is 053 C1.3, with $\mathcal K^{-1}S(Y)\nu(Y)$.

*Proof of (A.8).* Let $V$ be the difference of two admissible laws, so $DQ\cdot V=0$. Then $DQ\cdot V=2\xi^{\rm T}V$ with $\xi=K_\Psi\tilde X$, a system of linear coordinates over $\mathbb C[\Psi][[g_s]]$, hence a regular sequence; Koszul $H_1=0$ gives $V=A(\tilde X)\xi$ with $A^{\rm T}=-A$, i.e. $S=K_\Psi AK_\Psi$. Conversely $\tilde X^{\rm T}S\tilde X=0$. At $O(g_s^4)$ the same holds with $\xi=\mathcal K\nu=\tfrac12\nabla Q$, $\nu=Y+O(Y^2)$ a formal coordinate (R57's $\Phi^*$: $Q=\mathcal K(Y,Y)-\tfrac{g_s^2}{30}T(Y,Y,Y)$, $\nabla Q=2\mathcal K\nu$).

**The flat ones.** By C5.1 the flat admissible laws with higher-degree terms are the $F^h$
with $h_\Psi$ nonlinear. Differentiating $p(h(\hat Y),h(\hat Y))=p(\hat Y,\hat Y)$ in $\Psi$
and in $\hat Y$ gives $p(h,\partial_uh)=0$ and $(Dh)^{\rm T}p\,h=p\hat Y$, hence
$$
p\big(\hat Y,w_u(\hat Y)\big)=-\,h^{\rm T}p\,Dh\,(Dh)^{-1}\partial_uh=-\,p(h,\partial_uh)=0 ,
\tag{A.9}
$$
so $w_u\in\mathfrak{stab}(p)$ and, by (A.0), $DQ\cdot(D\mathcal G)^{-1}(w_u\circ\mathcal G)=
2\,p(\mathcal G,w_u\circ\mathcal G)=0$: the shift in (A.1) lies in $\mathfrak{stab}(Q)$, which
is (A.8) at $O(g_s^3)$ and 053 C1.3's $\mathcal K^{-1}S(Y)\nu(Y)$ at $O(g_s^4)$. Its defect
vanishes by (A.6) in the nonlinear form. [check: `C5.5` — nonlinear $h(\hat Y)=
e^{\Omega(\Psi,\hat Y)}\hat Y$ with $\Omega$ $p$-antisymmetric and linear in $\hat Y$, on a
$\Psi$-quadratic $K$: admissible, shift in $\mathfrak{stab}(Q)$, $\mathcal E_{\rm Lie}=0$, all
to $10^{-13}$; break: `C5.5-break` — a $\Psi$-dependent quadratic map not preserving $p$
stays flat and breaks admissibility. The $O(g_s^4)$ clause with the cubic $T$ is analytic
here: it uses only (A.0), which is 053 (5.5), machine-checked under R57.]

### A.5 BV: the flat law and the cotangent-lift chart (C5.7)

**056 §5a, derived.** Let $L$ be any $\Psi$-independent formal diffeomorphism of $V$. By
the chain rule, with no $\partial_uL$ term,
$$
D_{\tilde X}(L\circ\mathcal G)=(DL\circ\mathcal G)\,D\mathcal G,\qquad
\partial_u(L\circ\mathcal G)=(DL\circ\mathcal G)\,\partial_u\mathcal G
\quad\Longrightarrow\quad
F^{\rm flat}[L\circ\mathcal G]=F^{\rm flat}[\mathcal G],
\tag{A.10}
$$
the special case $\partial_uL=0$ of (A.1). In 056 (2.4),
$$
\hat Y'^+=\big(D(L\circ\mathcal G)\big)^{-\rm T}\tilde X^+=(DL)^{-\rm T}\hat Y^+,\qquad
\hat\Psi'^+=\Psi^+-(\partial_\Psi\mathcal G)^{\rm T}(DL)^{\rm T}(DL)^{-\rm T}
(D\mathcal G)^{-\rm T}\tilde X^+=\hat\Psi^+ ,
\tag{A.11}
$$
so the new chart is the old one followed by the cotangent lift of $\hat Y\mapsto L(\hat Y)$,
acting on the pair $(\hat Y,\hat Y^+)$ alone; $\hat\Psi^+$, the ghosts and (2.7) are
unchanged. The hatted-chart action becomes $S^\Psi_{\rm BV}-\tfrac{g_s^2}{4!}p\big(L^{-1}(\hat
Y'),L^{-1}(\hat Y')\big)$: still decoupled; a constant-coefficient pair with the same $p$ iff
$L\in\mathrm{Diff}_p(V)$ ($\mathrm O(p)$ for linear $L$), and otherwise still contractible (the $s$-image of $\hat Y'^+$ is the
gradient of a $\Psi$-independent function with nondegenerate Hessian, a formal coordinate).
[check: `C5.7` — $F^{\rm flat}$, the $\hat\Psi^+$ shift of 056 (2.4) evaluated directly, and
056 (2.7), each unchanged under a nonlinear non-orthogonal $\Psi$-independent $L$; break:
`C5.7-break` — a $\Psi$-dependent $L$ changes $F^{\rm flat}$ at order one]

**The $\Psi$-dependent freedom (β) in BV.** 056 §2–§3 use only two properties of the flat
representative: $\hat Y=\mathcal G(\tilde X)$ is inert, and $p(\mathcal G,\mathcal G)=Q$. Both
hold for $\mathcal G^h=h\circ\mathcal G$ (C5.1), so each member $F^h$ has its own hatted chart
$\tau^h$ (056 C1 with $\mathcal G\to\mathcal G^h$), in which its BV extension takes the same
decoupled form $S_{\rm dec}:=S^\Psi_{\rm BV}-\tfrac{g_s^2}{4!}p(\hat Y,\hat Y)$ (056 C2.3,
identity) (plus the $\Sigma_3$ pair $-a\tfrac{g_s^4}{6!}K_3(Y_3,Y_3)$ at $O(g_s^4)$, R60, untouched by $h$). Hence
$$
S_{\rm BV}[F^h]=S_{\rm dec}\circ\tau^h=S_{\rm BV}[\hat R]\circ\big(\tau^{-1}\circ\tau^h\big),
\tag{A.12}
$$
and $\tau^{-1}\circ\tau^h$ is the cotangent lift of the $Q$-preserving field redefinition
$\tilde X\mapsto\mathcal G_\Psi^{-1}\big(h_\Psi(\mathcal G_\Psi(\tilde X))\big)=\varphi_\Psi^{-1}
(\tilde X)$ — in the linear sector $\tilde X\mapsto g_\Psi^{-1}\tilde X$, with $g$ of (A.5) —
canonical by 056 (2.8). The BV actions of
any two members of the residual family are thus related by an **explicit** canonical
transformation, with no appeal to the uniqueness theorem that 056 C3.2 cites. As in R60, the
identities are unconditional; that these actions are *proper* solutions follows by R62 ($k\le3$, conditional on PH27) through (A.12) for the $S_3$ clause, a canonical transformation preserving properness; open at $O(g_s^4)$ ($k=4$, Task 7b).

### A.6 Claim tree — addendum nodes

- Assumptions: A1–A4 of the record; 053 A1–A4 for the $O(g_s^4)$ clauses; 056 A1, A4
  (antibracket, convention C2) for C5.7.
- **C5** GAP-3c closed. Under PH1, PH5 (and PH14 for the $O(g_s^4)$ clauses and the BV
  clause (A.12)): the flat
  admissible representative is unique up to trivial symmetries. $\Psi$-independent
  relabellings of $\hat Y$ leave the law unchanged. The flat admissible laws are exactly the
  $F^h$, $h_\Psi$ $p$-preserving with $h_0=\mathrm{id}$ (linear sector: $H_\Psi\in\mathrm O(p)$,
  i.e. $K_\Psi$-orthogonal relabellings $g_\Psi$ of $\tilde X$). Each differs from $\hat R$ by
  a pure-gauge Henneaux–Teitelboim trivial symmetry and has $\mathcal E=0$ identically. Their
  BV extensions are related by explicit cotangent-lift canonical transformations. [by
  C5.1–C5.7]
  - **C5.1** The flat admissible laws are in bijection with
    $\{h_\Psi\in\mathrm{Diff}_p(V),\ h_0=\mathrm{id},\ h_\Psi$ ghost-number preserving, compatible with the quotient and the reality condition, polynomial in $\Psi$ at each order in $g_s$, $\partial_uh=O(g_s)$ (043 §2 items 5, 7, 8, 9)$\}$ through $F^h=-(D(h\circ\mathcal G))^{-1}
    \partial_u(h\circ\mathcal G)$; linear sector $H\in\mathrm O(p)$, $H=1+O(g_s)$; the family is
    not reduced to a point. [by A1–A4, C1, C1.1, C3; cited: 053 §5 *Criterion* (Frobenius,
    $\Rightarrow$); eqs. (A.0)–(A.2)] [check: `C5.1-base`]
  - **C5.2** A $\Psi$-independent invertible $L$ (orthogonal or not) leaves the law
    unchanged ($\Delta\hat R=0$); it changes only the kinetic form of $\hat Y$, which stays $p$
    iff $L\in\mathrm{Diff}_p(V)$ ($\mathrm O(p)$ for linear $L$). [by C5.1; eq. (A.1) with $\partial_uL=0$] [check: `C5.2`,
    `C5.2-nonorth`]
  - **C5.3** For $\Psi$-dependent $H\in\mathrm O(p)$, $\Delta R_u=-\mathcal G^{-1}(H^{-1}
    \partial_uH)\mathcal G=K_\Psi^{-1}S_u$ with $S_u$ antisymmetric: a trivial symmetry; the
    $O(g_s)$ part is exact; equivalently $\hat R^H=g\cdot\hat R$ with $g=\mathcal G^{-1}H^{-1}
    \mathcal G$ $K_\Psi$-orthogonal. [by C5.1, C3.2, C2.1; eqs. (A.3)–(A.5)] [check: `C5.3`,
    `C5.3-gauge`, break `C5.3-break`]
  - **C5.4** $\mathcal E[g\cdot R]=g\,\mathcal E[R]\,g^{-1}$ exactly, for every law and every
    $g$ (nonlinear: $\varphi_*$); hence $\mathcal E=0$ on the whole residual family at every
    order of the formal $g_s$ expansion — exactly within the quintic-truncated $S_3$, and within $S_4$ under PH14 (R57); nothing is claimed beyond $S_4$ — and on a curved representative the R45 leading term is invariant (A.7). [by C2,
    C5.3; eqs. (A.6)–(A.7)] [check: `C5.4-flat`, `C5.4-cov`, `C5.4-order`]
  - **C5.5** Every higher-degree term of C1.1 is a field-dependent trivial symmetry (A.8);
    the flat ones are the nonlinear $F^h$, whose shift lies in $\mathfrak{stab}(Q)$ (A.9) —
    at $O(g_s^4)$, the 053 C1.3 family — with $\mathcal E_{\rm Lie}=0$. [by C1.1, C5.1, C5.4;
    053 (3.4) (Koszul), R57 for (A.0) at $O(g_s^4)$; the $O(g_s^4)$ clause under PH14; eqs.
    (A.8)–(A.9)] [check: `C5.5`, break `C5.5-break` — $O(g_s^3)$-type quadratic $Q$ only]
  - **C5.6** Falsifier: no member of the residual family changes $\mathcal E$ at any order (of the formal $g_s$ expansion, within the truncations of C5.4);
    $\mathcal E$ moves only under trivial symmetries that are not pure gauge, which lie
    outside the family and have $\mathfrak k_{K_\Psi}$-valued defect. [by C5.1, C5.4; 043
    (4.3)] [check: `C5.4-break`]
  - **C5.7** Under a $\Psi$-independent $L$, $F^{\rm flat}$, $\hat\Psi^+$ and 056 (2.7) are
    unchanged and the chart changes by the cotangent lift of $L$ on $(\hat Y,\hat Y^+)$ alone
    (constant coefficient $p$ iff $L\in\mathrm{Diff}_p(V)$, i.e. $\mathrm O(p)$ for linear $L$); for the $\Psi$-dependent freedom,
    $S_{\rm BV}[F^h]=S_{\rm BV}[\hat R]\circ(\tau^{-1}\circ\tau^h)$, an explicit canonical
    transformation. The identities are unconditional; properness by R62 ($k\le3$, conditional on PH27) through (A.12) for the $S_3$ clause; open at $O(g_s^4)$ ($k=4$, Task 7b). [by C5.1, R60 (056 C1, C2.3, (2.4), (2.7), (2.8)); eqs.
    (A.10)–(A.12)] [check: `C5.7`, break `C5.7-break`]

Open gaps: none new. The record's [GAP-3c] is closed by C5; the rest of the record's
`Open gaps:` line: GAP-3a closed (54/54 PASS at $N=3$, $g_s^5$), GAP-3b open, GAP-3d closed by
R57, GAP-3e closed by R60, properness of the BV extension by R62 ($k\le3$, PH27), open at
$O(g_s^4)$ ($k=4$, Task 7b).
Hypotheses in force: PH1, PH5 (inherited); PH14 for the $O(g_s^4)$ clauses of C5.1, C5.5,
C5.7, and for C5.7's (A.12), which cites R60 (`Conditional(PH1, PH5, PH14)`); PH27 for
C5.7's properness clause. No new hypothesis.

### A.7 Verification

`codes/verify-gap3c.py` (new; `codes/verify-gauge-algebra-ogs3.py` untouched, its part D run at $N=3$, $g_s^5$: 54/54 PASS), seed `20260926`, JAX float64 forward-mode derivatives (no finite differences),
$\dim V=5$, 3 field directions, indefinite well-conditioned $p$, models "lin"
($K_\Psi=p-\tfrac{g}{5}P_\Psi$, the $S_3$ form) and "quad" (plus $g^2Q(\Psi,\Psi)$, a generic
$\Psi$-dependent symmetric form standing in for 053's $\mathcal K(\Psi)$), $g\in\{0.2,0.1\}$;
$\mathcal G=M^{1/2}$ by Denman–Beavers, cross-checked against `scipy.linalg.sqrtm` to
$10^{-15}$. Log: `agent/scratch/gap3c-run1.log`. **46 checks, 46 PASS, exit 0** (36 checks +
10 break legs).

| check | content | break leg |
|---|---|---|
| `model`, `sqrt-sanity` | $\mathcal G^2=M$, spectrum of $M-1$ in the disc of radius $0.5$ | — |
| `C5.1-base` | $\hat R$ admissible and flat; $\mathcal E[R^{(17)}]\neq0$ on the same data | — |
| `C5.2` | constant $O\in\mathrm O(p)$: law unchanged | — |
| `C5.2-nonorth` | constant non-orthogonal $L$: law **also** unchanged (the brief's break leg does not break) | — |
| `C5.3` | (A.3) against the direct law of $H\mathcal G$; $S_u$ antisymmetric; $\hat R^H$ admissible | `C5.3-break`: $\Psi$-dependent $p$-symmetric generator — flat, not admissible |
| `C5.3-gauge` | (A.5): $g\cdot\hat R=\hat R^H$, $g^{\rm T}Kg=K$ | — |
| `C5.4-flat` | $\mathcal E[\hat R^H]=0$ | — |
| `C5.4-cov` | (A.6) on $R^{(17)}$; $\mathcal E$ itself moves (conjugation is not the identity) | — |
| `C5.4-order` | (A.7): halving ratio $7.91$; R45 leading term: ratio $7.99$ | — |
| — | — | `C5.4-break`: non-pure-gauge antisymmetric $S_u$ — admissible, $\mathcal E\neq0$, $K\mathcal E$ antisymmetric |
| `C5.5` | nonlinear $h$: admissible, shift in $\mathfrak{stab}(Q)$, $\mathcal E_{\rm Lie}=0$ | `C5.5-break`: $\Psi$-dependent non-$p$-preserving $h$ — flat, not admissible |
| `C5.7` | $F^{\rm flat}$, 056 (2.4) $\hat\Psi^+$ shift and (2.7) unchanged under nonlinear $L$ | `C5.7-break`: $\Psi$-dependent $L$ changes $F^{\rm flat}$ |

**The checks can fail.** The first run, on a random $p$ with a near-zero eigenvalue, failed
`C5.4-order` (ratios $4.5$, $4.7$: expansion parameter not small) and the whole "quad" block
at $g=0.2$ (spectrum of $M$ outside the Denman–Beavers domain). Conditioning $p$ fixed both.
The `model` check now guards the domain. Each identity is compared with an independent path:
(A.3) with the directly differentiated law of $H\mathcal G$, (A.6) on $R^{(17)}$, which has
no pure-gauge structure, and (A.11) through 056 (2.4) evaluated from the Jacobians. A sign
flip in (A.3), or dropping the conjugation in (A.6), gives relative errors of order one (the
`C5.4-cov` line reports $\mathcal E$ moving by $0.07$–$0.30$).

**Not tested (script gaps, 2026-09-30 node check; script unchanged).** `curv_nl` is evaluated only on pure-gauge laws, never on a curved law, so a routine returning $\approx0$ identically would pass `C5.5` and `C5.5-break`; and $\hat Y'^+=(DL)^{-\rm T}\hat Y^+$ of (A.11) is not tested (only $\hat\Psi^+$ and (2.7) are).

**Not machine-checked.** The Frobenius and normalisation steps of C5.1 (analytic, cited from
053 §5); the $O(g_s^4)$ clause with the cubic $T$ (it rests on (A.0) = 053 (5.5), checked
under R57); the BV identity (A.12) beyond the invariance of (2.4)/(2.7) (it composes 056's
unconditional identities). The model uses generic symmetric $P_a$, not totally symmetric
string vertices. It is a superset, since only the symmetry of $K$ enters.

**Depth.** Limiting case $g_s\to0$: $H=1+O(g_s)$, $g\to1$, the family collapses to $\hat
R\to0$ (R11). Special case $H$ constant: C5.2. Second route for the flatness of the family:
pure gauge (A.1) and covariance (A.6), which agree. Regime: formal series in $g_s$ in the
record; in the script, finite $g$ inside the square-root domain.

### A.8 Result, self-review, status (addendum)

**Result.** GAP-3c is closed. The flat admissible representative is unique up to trivial
symmetries in the following exact sense:

1. The inert variable of a given law is unique up to $\Psi$-independent relabellings, which
   leave the law, $\mathcal E$, $\hat\Psi^+$ and the BV chart's coupling to the $\Psi$ sector
   unchanged. The GAP-3c sentence ("$\Psi$-independent $K$-orthogonal rotation of $\hat Y$")
   described this relabelling, not a freedom of $\hat R$.
2. The law itself is unique up to $\Psi$-dependent $p$-preserving relabellings $h_\Psi$ of
   $\hat Y$, $h_0=\mathrm{id}$ (linear: $H_\Psi\in\mathrm O(p)$, equivalently $K_\Psi$-orthogonal
   $g_\Psi$ acting on $\tilde X$, $\hat R\to g\hat Rg^{-1}+(\partial g)g^{-1}$). Each changes
   $\hat R$ by a pure-gauge Henneaux–Teitelboim trivial symmetry: $K_\Psi^{-1}S_u$, $S_u$
   antisymmetric, and $K^{-1}S(\tilde X)\tilde X$ or $\mathcal K^{-1}S(Y)\nu(Y)$ in the
   nonlinear sector.
3. $\mathcal E$ is covariant, $\mathcal E\to g\mathcal Eg^{-1}$, so it vanishes on the whole
   family, at every order of the formal $g_s$ expansion — exactly within the quintic-truncated $S_3$, and within $S_4$ under PH14 (R57); nothing is claimed beyond $S_4$. No member of the flat family acquires a non-zero $\mathcal E$ at any order; this is proved, not found by search. On a curved representative a rotation conjugates $\mathcal E$: its vanishing and its leading coefficient are invariant, the orders $g_s^3$ and higher change. On R17's curved representative the leading coefficient
   $\tfrac{g_s^2}{100}[A_{u_1},A_{u_2}]$ is invariant.
4. BV: the BV extensions of two members are related by the explicit cotangent lift of
   $\varphi_\Psi^{-1}$. Properness by R62 ($k\le3$, conditional on PH27) through (A.12) for the $S_3$ clause; open at $O(g_s^4)$ ($k=4$, Task 7b).

**Self-review.**

- *Objective.* Met: the ledger can state "unique up to trivial symmetries". The literal (i)
  turned out to be the empty case. The addendum says so and answers (i)–(iv) for the freedom
  with content.
- *Weakest step.* The ($\Rightarrow$) half of C5.1, "flat implies pure gauge", is Frobenius
  for formal series on a contractible base. It is cited from 053 §5, where it is called
  standard, and is not re-proved here. Only the characterisation depends on it. C5.3–C5.7
  hold for every $F^h$ without it.
- *Not checked.* The $O(g_s^4)$ cubic case is not machine-checked here. It needs nothing
  beyond (A.0), which R57 verifies. The algebraicity of $h$ (§2 item 8) is not classified; one
  algebraic example is exhibited.
- *What a stronger reader would add.* (A.12) also makes 056 C3.2's uniqueness-theorem citation
  unnecessary within the flat family. It does not do so between R17 and the flat law, because
  R17 is not flat.

**Status (addendum).** Complete: A.0–A.8, `codes/verify-gap3c.py` (46/46 PASS, exit 0). Next
(orchestrator): annotate R45 (GAP-3c closed), cross-reference R57/R60, and update the
record's `Open gaps:` line by bookkeeping.
2026-09-26 [GAP-3a]: the machine check of part D is extended to $N=3$ through $g_s^5$ (`codes/verify-gauge-algebra-ogs3.py`, `part_D(3, 5)`, log `agent/scratch/gauge-ogs3-run-N3.log`): 54 PASS, 0 FAIL, exit 0, wall 35 868 s — D0–D5 and their break legs at N=3, g⁵, including $\mathcal E[\hat R]=0$ identically through $g_s^5$, the shift $-\tfrac{g^2}{200}[A_\Psi,A_u]$ with the sharp coefficient, the antisymmetry of $K_\Psi\,\delta R_u$, and $G^\top K_\Psi G=p_{2,2}$ for $G=M^{-1/2}$. GAP-3a is closed at the level 'analytic proof to all orders, machine check at N=2 and N=3 through $g_s^5$'.
