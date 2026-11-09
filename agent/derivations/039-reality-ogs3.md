# 039 — Reality of $\Sigma_2$ at $O(g_s^3)$

**Date:** 2026-09-22 (Opus, computator; brief
`agent/briefs/active-computator-reality-ogs3-20260922T150100.md`).
**Machine check:** `codes/verify-reality-tower.py`, part 4 (16 positive checks `C2.1`…`C4.3`
plus 14 break legs; run 2026-09-22, seeds 20260914 and 20260922, N = 3). Counts and the full run
are in §4.
**Inputs (read by line range):** 028 §0 verdict table, §1 (ll. 37–111), §2 (ll. 112–200);
`knowledge/discussions/2026-09-19-hs-order-by-order.md` §1 l. 40, §2 (ll. 59–133);
011 §1–§2 (eqs. B.4–B.6) and §4 (eqs. B.8–B.9); ledger rows R11, R12, R17 (with its 2026-09-19
annotation), R22, R23, R38 (with its 2026-09-19 annotation), R40 and the `## Hypotheses` table
(PH1, PH2, PH5, PH6, PH7).
**Scope:** algebraic layer — finite-dimensional $\mathcal H_0$, generic $\ddagger$-equivariant
symmetric tensors $\mathcal V_n$, formal power series in real $g_s$. Same layer as 028. The CFT
reality of the $\mathcal V_n$ is PH6 and is not re-derived here.

## Task and objective

**Literal task.** Decide whether the reality condition $\Sigma_2^\ddagger=\Sigma_2$ survives at
$O(g_s^3)$ in the truncated form in which the quintic order is actually written, i.e. with the
corrected saddle and the corrected gauge law, both of which carry an inverse $p_{2,2}^{-1}$.
Three clauses: (1) does $\ddagger$ commute with $p_{2,2}^{-1}$; (2) is the corrected saddle real;
(3) does the corrected gauge law map the real locus to itself.

**Objective.** The paper claims a real action at all orders. The quintic order is the first where
the auxiliary field is not $\Psi^{\otimes2}$ and where an inverse enters the field's own
definition and transformation — the first place where reality could fail structurally rather than
by bookkeeping. The quintic
subsection of the notes needs either the statement or the named obstruction before it
can be written.

**Verdict (summary).** All three clauses close. Reality survives, and survives in a stronger form
than asked: to all orders of the formal $g_s$ expansion inside the quintic truncation, which needs
only PH1 order by order, and non-perturbatively in $g_s$ wherever the dressed kernel $K_\Psi$ is
invertible on the quotient, which is PH2. The $\ddagger$-stability of $\ker\mathcal V_4$ is a
**consequence** of PH6 at $n=4$ alone, not an additional hypothesis — see C2.2 and (1.5), which is
one line and uses neither $p_{2,2}$ nor the non-degeneracy of $\omega_2$.

The result is `Conditional(PH6 [n=4,5], PH1, PH2, PH5/R38)`. **No hypothesis new to the project is
declared**, but four inherited ones are in force, two more than the record's first run listed:
PH2 for $K_\Psi^{-1}$ beyond formal order-by-order inversion, and PH5/R38
($\mathcal V_5(\ker\mathcal V_4,\cdot,\cdot)=0$), without which the $O(g_s^3)$ objects do not
descend to $W_q$ at all. The second of these is the condition the ledger's 2026-09-19 R38
annotation attaches to every $O(g_s^3)$ row, and 039 joins that list.

## Conventions

Inherited verbatim from 028 §1; restated only where this record uses them.

**(C1) The conjugation.** $\ddagger=\mathrm{BPZ}\circ(\text{hermitian conjugation})$ is an
antilinear involution of $\mathcal H_0$ preserving the ghost grading:
$(aA+bB)^\ddagger=a^*A^\ddagger+b^*B^\ddagger$, $(A^\ddagger)^\ddagger=A$. $A$ is *$\ddagger$-real*
if $A^\ddagger=A$; every $A$ splits as $A=A_r+iA_i$ with $A_r,A_i$ real, so the real subspace spans
$\mathcal H_0$ over $\mathbb C$.

**(C2) Tensor powers.** $(A_1\otimes\cdots\otimes A_k)^\ddagger=A_1^\ddagger\otimes\cdots\otimes
A_k^\ddagger$, componentwise, **without reordering sign**. This is unambiguous exactly on the
spaces whose strands all have $N_{\rm gh}=2$ (Grassmann-even), i.e. on
$\mathrm{Sym}^2\mathcal H_0$ at $N_{\rm gh}=4$ and $\mathrm{Sym}^3\mathcal H_0$ at
$N_{\rm gh}=6$; both are $\ddagger$-stable. We call these the **even-strand spaces**.

It is *not* unambiguous on $\mathrm{Sym}^2\mathcal H_0$ at $N_{\rm gh}=6$ — two strands of
$N_{\rm gh}=3$, Grassmann-odd — which is, by the grading of §5, the *target* of both $p_{2,2}$ and
$p_{3,2}$. There the two conventions of 028 (C2) differ by $(-1)^{k(k-1)/2}=-1$ at $k=2$, and
$\ddagger^2=1$ is PH7. **This record never applies $\ddagger$ to an odd-strand tensor**: §1 is
stated for the composites $P=p_{2,2}^{-1}p_{3,2}$ and $R=K_\Psi^{-1}p_{2,2}$, which map an
even-strand space to an even-strand space, and every conjugation below is taken on such a space.
PH7 is therefore not inherited (see the remark after (1.7) for the price of the alternative
route).

**(C3) The pairing.** $\omega_1(A,B)=\langle A|c_0^-|B\rangle$ is $\ddagger$-equivariant,
$\omega_1(A,B)^*=\omega_1(A^\ddagger,B^\ddagger)$, in the normalisation
$\langle c_{-1}\bar c_{-1}c_0^-c_0^+c_1\bar c_1\rangle=-\tfrac12$ (real, no $i$). We write
$\braket{\cdot,\cdot}:=\omega_2=\omega_1^{\otimes2}$ on $\mathcal H_0^{\otimes2}$, equivariant by
028 (1.2).

**Grading of the pairing.** $\omega_1$ is non-zero only for $N_{\rm gh}(A)+N_{\rm gh}(B)=5$, so
$\omega_2$ pairs $N_{\rm gh}=4$ with $N_{\rm gh}=6$ — it is a pairing **between two different
graded sectors**, not a form on one space. It is non-degenerate as such a pairing between
$\mathrm{Sym}^2\mathcal H_0$ at $N_{\rm gh}=4$ and $\mathrm{Sym}^2\mathcal H_0$ at
$N_{\rm gh}=6$: the splitting $\mathcal H_0^{\otimes2}=\mathrm{Sym}^2\oplus\Lambda^2$ is
$\omega_2$-orthogonal in each sector, the Koszul sign in $\omega_1(x_2,y_1)$ being $+1$ because
the $N_{\rm gh}=4$ slot is Grassmann-even. **The record's first run wrote (C3) as a one-space
statement on $\mathrm{Sym}^2$**; that reading is corrected here and nothing below depends on it,
because the load-bearing chain of §1 goes through the composites, whose characterisation
(1.7)–(1.8) uses only the equivariance of $\mathcal V_4$ and $\mathcal V_5$ and never $\omega_2$'s
non-degeneracy.

**(C4) Lemma 1 of 028** (reused, not re-derived): a multilinear form on a $\ddagger$-stable space
is $\ddagger$-equivariant iff it is real-valued on $\ddagger$-real arguments.

**(C5) Lemma 2 of 028** (reused, not re-derived). For a *real* operator $\hat A$ on a
$\ddagger$-stable $W$ — meaning $\hat A(X^\ddagger)=(\hat AX)^\ddagger$ — : (i) $\ker\hat A$ and
$\operatorname{im}\hat A$ are $\ddagger$-stable; (ii) if $\hat A$ is invertible, $\hat A^{-1}$ is
real; (iii) for a real $b\in\operatorname{im}\hat A$ the solution set of $\hat AX=b$ is
$\ddagger$-stable, contains a real element, and its class in $W/\ker\hat A$ is real.

**(C6) 028 (1.5)** (reused): with $\omega$ non-degenerate and equivariant and
$F(X,Y)=\omega(X,\hat FY)$, $F$ is equivariant $\iff$ $\hat F$ is real.

**(C7) Notation of this project.** $\mathcal V_4(A,B)=\braket{A,p_{2,2}B}$ for
$A,B\in\mathrm{Sym}^2\mathcal H_0$, and $\mathcal V_5(A,B)=\braket{A,p_{3,2}B}$ for
$A\in\mathrm{Sym}^2\mathcal H_0$, $B\in\mathrm{Sym}^3\mathcal H_0$. So
$p_{2,2}$ and $p_{3,2}$ are **linear** maps, and by the grading of (C3) and §5 they are maps
between *different* graded sectors:
$$
p_{2,2}:\ \mathrm{Sym}^2\mathcal H_0\big|_{N_{\rm gh}=4}\longrightarrow
\mathrm{Sym}^2\mathcal H_0\big|_{N_{\rm gh}=6},\qquad
p_{3,2}:\ \mathrm{Sym}^3\mathcal H_0\big|_{N_{\rm gh}=6}\longrightarrow
\mathrm{Sym}^2\mathcal H_0\big|_{N_{\rm gh}=6},
$$
i.e. $N_{\rm gh}(p_{2,2})=+2$ and $N_{\rm gh}(p_{3,2})=0$, in agreement with R23's
$N_{\rm gh}(p_{k,\ell,g})=3\ell-2k+g$ and with the project convention $N_{\rm gh}(m_2)=+2$
(`knowledge/reading-map.md` l. 39: input 4, output 6). Their common target is odd-strand; the
composites
$$
P:=p_{2,2}^{-1}p_{3,2}:\ \mathrm{Sym}^3\mathcal H_0\big|_{6}\to W_q,\qquad
R:=K_\Psi^{-1}p_{2,2}:\ \mathrm{Sym}^2\mathcal H_0\big|_{4}\to W_q
$$
are not: both are maps between even-strand spaces, and they are the objects §1 works with.
The multi-argument writings are contractions of the same map:
$p_{3,2}(\Psi,B):=p_{3,2}(\Psi\odot B)$ for $B\in\mathrm{Sym}^2$, $p_{3,2}(\Psi^{\otimes3})
:=p_{3,2}(\Psi\odot\Psi\odot\Psi)$, $W\leftrightarrow p_{3,2}(\Psi,\cdot)$. Dressed kernel
$K_\Psi:=p_{2,2}-\tfrac{g_s}5p_{3,2}(\Psi,\cdot)$ (011 §2, discussion §1); it carries the same
$+2$ grading as $p_{2,2}$, since $p_{3,2}(\Psi,\cdot)$ does.
$W_q:=\mathrm{Sym}^2\mathcal H_0|_{N_{\rm gh}=4}/\ker\mathcal V_4$ is the space $\Sigma_2$ lives
in — an even-strand space.

## Equivariance facts each clause needs

| Fact | Statement | Source |
|---|---|---|
| (E1) | $\omega_1$, hence $\omega_2$, is equivariant; $\omega_2$ non-degenerate on $\mathrm{Sym}^2$ | (C3), 028 (1.2) |
| (E2) | $\mathcal V_4$ equivariant | PH6 at $n=4$ (028 (1.1)) |
| (E3) | $\mathcal V_5$ equivariant | PH6 at $n=5$ |
| (E4) | $P=p_{2,2}^{-1}p_{3,2}$ real, as a map between even-strand spaces | C2.1 below, from (E2)+(E3)+PH1+PH5/R38; eq. (1.7) |
| (E5) | $R=K_\Psi^{-1}p_{2,2}$ real, likewise | C2.1 below, from (E2)+(E3)+PH2+PH5/R38; eq. (1.8) |
| (E6) | $\ker\mathcal V_4$ is $\ddagger$-stable; $\ddagger$ descends to $W_q$ | C2.2, from (E2) alone; eq. (1.5) |
| (E7) | $\mathcal V_5(\ker\mathcal V_4,\cdot,\cdot)=0$, so $p_{3,2}$, $K_\Psi$ and the composites descend to $W_q$ | PH5/R38 (ledger annotation 2026-09-19) |
| (E8) | the coefficients $1$, $2$, $\tfrac15$, $\tfrac35$, $\tfrac1{10}$ and $g_s$ are real | A4 |
| (E9) | (remark only) $p_{2,2}$, $p_{3,2}$ real individually — needs the odd-strand $\ddagger$ convention and PH7 | remark after (1.7) |

## Claim tree

- **A1** Algebraic layer: $\mathcal H_0$ finite-dimensional, $\mathcal V_n$ generic symmetric
  multilinear forms, all statements formal power series in $g_s$.
- **A2** Conventions (C1)–(C7): $\ddagger$ antilinear involution, componentwise on tensors without
  reordering sign, $\omega_1$ equivariant in the stated normalisation, physical ghost number
  ($N_{\rm gh}(\Psi)=2$, $N_{\rm gh}(\Sigma_2)=4$, $N_{\rm gh}(p_{2,2})=+2$,
  $N_{\rm gh}(p_{3,2})=0$). $\ddagger$ is applied **only** on even-strand spaces
  ($\mathrm{Sym}^2|_{4}$, $\mathrm{Sym}^3|_{6}$, $\mathcal H_0|_{2}$), never on the odd-strand
  target $\mathrm{Sym}^2|_{6}$ of $p_{2,2}$ and $p_{3,2}$.
- **A3** $\Sigma_2\in\mathrm{Sym}^2\mathcal H_0|_{N_{\rm gh}=4}/\ker\mathcal V_4=W_q$,
  level-matched and kernel-quotiented; equalities involving $\Sigma_2$ and $\delta\Sigma_2$ are
  equalities of classes in $W_q$. That the $O(g_s^3)$ expressions *descend* to $W_q$ at all is
  **H3 = PH5/R38**, not part of A3.
- **A4** $g_s\in\mathbb R$; $\Psi^\ddagger=\Psi$; $\delta\Psi^\ddagger=\delta\Psi$ — an
  assumption restricting the variations considered, not a theorem: the tangency argument of §3
  shows only that *if* the $\Psi$ gauge law maps the real locus into itself, then $\delta\Psi$
  is real, and that antecedent is the odd-sector question (PH7). The statement proved here is
  about variations already tangent to the real locus.
- **H1 = PH6** Every geometric $\mathcal V_n$ is $\ddagger$-equivariant (028's (H$_R$)); used here
  at $n=4,5$ only. Motivation and falsifier: ledger `## Hypotheses`, PH6.
- **H2 = PH1** $p_{2,2}$ descends to an invertible map on $W_q$, level by level. Motivation and
  falsifier: ledger `## Hypotheses`, PH1. This suffices for every statement that is *formal* in
  $g_s$, order by order.
- **H2′ = PH2** The dressed kernel $K_\Psi=p_{2,2}+O(g_s)$ is invertible on $W_q$ level by level
  in a neighbourhood of $g_s=0$. The record's first run reduced this to PH1 "by Neumann series,
  no new invertibility condition at this order"; the ledger's PH2 row records that reduction as
  *an argument, not a source statement*, and PH2 strictly extends PH1 (019 ll. 299–301). The
  non-perturbative-in-$g_s$ form of clause 2 (2.6) and of clause 3 (3.6) rests on PH2; the
  order-by-order form rests on PH1 only. Motivation and falsifier: ledger `## Hypotheses`, PH2.
- **H3 = PH5/R38** $\mathcal V_5(\ker\mathcal V_4,\mathrm{Sym}^2\mathcal H_0,\mathcal H_0)=0$
  (or $\ker\mathcal V_4=0$). Needed for $p_{3,2}$, $K_\Psi$, $P$, $R$ and term (c) of the gauge
  law to be defined on classes in $W_q$ at all. This is verbatim the ledger's 2026-09-19 R38
  annotation, which attaches the condition to every $O(g_s^{\ge3})$ row; 039 is a new $O(g_s^3)$
  row and joins that list. Motivation and falsifier: ledger `## Hypotheses`, PH5, and the R38
  annotation. Cf. the R17 annotation and 036/R40: *every $O(g_s^{\ge3})$ toy with a generic
  invertible $\mathcal V_4$ never saw this condition* — the trap the script's part 4 fell into on
  its first run and which the degenerate re-runs of §4 now exercise.
- **C1** Under PH6 ($n=4,5$), PH1, PH2 and PH5/R38, the reality condition
  $\Sigma_2^\ddagger=\Sigma_2$ is preserved at $O(g_s^3)$: the corrected saddle is
  $\ddagger$-real and the corrected gauge law maps the real locus of $(\Psi,\Sigma_2)$ to the
  real locus. [by C2, C3, C4]
  - **C2** (clause 1) Under PH6, PH1, PH2 and PH5/R38, the composites $P=p_{2,2}^{-1}p_{3,2}$ and
    $R=K_\Psi^{-1}p_{2,2}$ are real maps between even-strand spaces, and in particular $\ddagger$
    commutes with $p_{2,2}^{-1}$ on $W_q$. [by C2.1–C2.5]
    - **C2.1** $P$ and $R$ are real maps; equivalently $\ddagger$ commutes with $p_{2,2}^{-1}$ on
      $W_q$. Proved from the characterisations $\mathcal V_4(A,PC)=\mathcal V_5(A,C)$ and
      $\mathcal V_4^\Psi(A,RB)=\mathcal V_4(A,B)$, with $\ddagger$ applied only on even-strand
      spaces. [by H1 ($n=4,5$), H2, H2′, H3, A2; eqs. (1.7), (1.8)] [check: C2.1, C2.1-P,
      C2.1-R]
    - **C2.2** $\ker\mathcal V_4$ is $\ddagger$-stable and $\ddagger$ descends to an antilinear
      involution of $W_q$; this is a consequence of PH6 at $n=4$ alone — not of PH1, not of
      $\omega_2$-non-degeneracy, not a new hypothesis. [by H1; eq. (1.5)] [check: C2.2]
    - **C2.3** Under PH1 and PH5/R38, $(p_{2,2}^{-1}A)^\ddagger=p_{2,2}^{-1}(A^\ddagger)$ as
      classes in $W_q$, for every $A$ in the image, not only real $A$; and the statement is a
      statement about *classes*: two representatives differing by a kernel element have
      $\ddagger$-images in the same class. [by H2, H3, C2.1, C2.2; eq. (1.6)]
      [check: C2.3, C2.3-quotient]
    - **C2.4** Without PH1 the weaker statement of C5(iii) still holds: for real
      $A\in\operatorname{im}p_{2,2}$ the solution class is real and a real representative exists.
      [by C2.1, C2.2, C5(iii)]
    - **C2.5** (remark, not load-bearing) The individual maps $p_{2,2}$ and $p_{3,2}$ are real
      *if* the odd-strand $\ddagger$ convention of 028 (C2) is fixed on their common target
      $\mathrm{Sym}^2|_{N_{\rm gh}=6}$, which brings PH7. The composite route of C2.1 avoids
      this; the two routes agree because the odd-strand sign convention cancels between
      $p_{3,2}$ and $p_{2,2}^{-1}$. [by H1, PH7; remark after (1.7)]
  - **C3** (clause 2) Under PH6, PH1, PH2 and PH5/R38, $\Psi^\ddagger=\Psi$ implies
    $(\Sigma_2^*)^\ddagger=\Sigma_2^*$. [by C3.1–C3.3]
    - **C3.1** The truncated saddle $\Psi^{\otimes2}+\tfrac{g_s}5P(\Psi^{\otimes3})$ is
      $\ddagger$-real through $O(g_s)$ inclusive; this needs PH1 only (order by order).
      [by C2.1, A4, H3; eq. (2.2)] [check: C3.1, C3.1-deg]
    - **C3.2** The exact quintic saddle $\Sigma_2^*=R(\Psi^{\otimes2})=K_\Psi^{-1}
      p_{2,2}(\Psi^{\otimes2})$ is $\ddagger$-real to all orders of the formal $g_s$ expansion
      (PH1) and non-perturbatively wherever $K_\Psi$ is invertible on $W_q$ (**PH2**).
      [by C2.1, H2′, H3, C5(ii); eq. (2.4)] [check: C3.2, C3.2-deg]
    - **C3.3** $g_s\to0$ reduces C3.1 to $(\Psi^{\otimes2})^\ddagger=\Psi^{\otimes2}$, i.e. to the
      known $O(g_s^2)$ statement and to 028 Step 2.3's leading term. [by A2, C3.1]
  - **C4** (clause 3) Under PH6, PH1, PH2 and PH5/R38, the $O(g_s^3)$ gauge law maps the real
    locus to itself:
    $\Psi,\delta\Psi,\Sigma_2$ all $\ddagger$-real $\Rightarrow$ $\delta\Sigma_2$ $\ddagger$-real.
    [by C4.1–C4.4]
    - **C4.1** Each of the three terms of the law is separately $\ddagger$-real. Term (c),
      $\tfrac{g_s}{10}P(\Sigma_2-\Psi^{\otimes2},\delta\Psi)$, is defined on classes only under
      PH5/R38. [by C2.1, A4, E8, H3; eqs. (3.2)–(3.4)] [check: C4.1, C4.1-deg]
    - **C4.2** Reality is insensitive to the symmetrisation reading of $2\,\delta\Psi\otimes\Psi$:
      both the unsymmetrised tensor and its symmetrisation are $\ddagger$-real. [by A2 (C2);
      eq. (3.5)] [check: C4.2]
    - **C4.3** The exact law (011 B.9) is real by the same route, so the conclusion is not an
      artefact of the $O(g_s)$ truncation; it carries PH2 with $K_\Psi^{-1}$. [by C3.2, C2.1,
      H2′; eq. (3.6)] [check: C4.3]
    - **C4.4** PH7 is not needed for the statement proved here, which is about variations already
      tangent to the real locus (A4) and whose whole chain stays on even-strand spaces (A2, C2).
      Whether **every** gauge parameter $\Lambda$ ($N_{\rm gh}=1$, Grassmann-odd) produces such a
      variation is the odd-sector question (PH7) and **is not settled here**. [by A2, A4, C2.1;
      §3.4]

Open gaps: none
Hypotheses in force: PH6 (= H1, at $n=4,5$), PH1 (= H2), PH2 (= H2′), PH5/R38 (= H3)

## Status

Last completed: mechanical fix pass after critic iteration 2 (brief
`agent/briefs/active-fix-039-mechanical-20260922T171500.md`, 2026-09-22). Restated (1.6) on
$\operatorname{im}p_{2,2}$ with the transported conjugation (no PH7) and dropped the now-unused
C2.3 citations from C3.1, C3.2, C4.1 and the §2/§3 "Uses" lines; added two §4 scope-honesty notes
(R38 imposed in the $\mathrm{Sym}^3$ slot only; `C4.3`/`C4.2` run in the invertible sector only);
corrected the stale header count; added break leg `break-C3.2b` for `C3.2`'s Richardson-ratio
coefficient. Script part 4: 30 checks (16 positive, 14 break legs), 48/48 overall with parts 1–3
unchanged, at seeds 20260914 and 20260922. No clause verdict changed; the result is still stated
as `Conditional(PH6 [n=4,5], PH1, PH2, PH5/R38)`.
Next: none — record complete and consolidated (one Status line, no duplicated sections); the
§6 row is not promoted here (the record is on hold pending a separate conventions
question).

## 1. Clause 1 — the conjugation and the inverse

### Setup

Assumptions A1–A4; hypotheses H1 (PH6) at $n=4,5$, H2 (PH1), H2′ (PH2), H3 (PH5/R38). Symbols:
$p_{2,2}$, $p_{3,2}$, $P=p_{2,2}^{-1}p_{3,2}$, $R=K_\Psi^{-1}p_{2,2}$,
$\braket{\cdot,\cdot}=\omega_2$, $W_q=\mathrm{Sym}^2\mathcal H_0|_{N_{\rm gh}=4}/
\ker\mathcal V_4$ as in (C7).

*Equation labels are stable across the fix pass and therefore no longer monotonic:* (1.5) now
precedes (1.7), and (1.6) follows it. (1.3) and (1.4) of the first run — the individual-operator
statements — are withdrawn from the load-bearing chain and survive as the remark after (1.7);
nothing cites them.

### What 028 already gives, and what it does not

028 §1 (C2) states "$\mathrm{Sym}^k\mathcal H_0$ is $\ddagger$-stable, and so is the quotient by
$\ker V_{2k}$ once $V_{2k}$ is real (Lemma 2 below)", and Lemma 2 gives (i) $\ddagger$-stability of
$\ker\hat A$ and $\operatorname{im}\hat A$ for a real operator $\hat A$, (ii) reality of $\hat
A^{-1}$ when invertible, (iii) reality of the solution class when not. Step 2.3 uses (ii) on the
block operator $\mathcal A$ and on the nested kernels $\hat H_k$, and records that the $\ker
V_{2k}$ quotient is covered by (iii) *given solvability*.

Two of the three "novelties" the first run of this record claimed are genuine; the third was a
misreading of 028, corrected here.

1. **Genuine.** 028 Step 2.1 establishes reality for the *tower* forms $\tilde M_k$, $\hat M_k$,
   $L_k$ built from the parents $T_n$ of 019's closure recursion, not for the geometric
   $\mathcal V_4$ read as an operator in this project's $p_{2,2}$ notation, and it does not make
   the identification $\ker\mathcal V_4=\ker p_{2,2}$. The argument is the same one line, but the
   object is different.
2. **Genuine.** The same for $p_{3,2}$, which is not an operator on a single space but a map
   $\mathrm{Sym}^3\to\mathrm{Sym}^2$ between two different spaces — and, by the grading of (C3),
   $p_{2,2}$ is *also* such a map ($N_{\rm gh}=4\to6$). 028 never needs a map of unequal strand
   number, nor of unequal ghost grading, in isolation (its $L_k$ has $\Psi$ already inserted). The
   two-space version has to be written out; it is (1.7)–(1.8) below.
3. **Not a novelty — the first run misread 028.** That run said "028 only ever evaluates the
   inverse on a real source, so it needs, and proves, only the weaker 'real in, real out'". That
   is false of Lemma 2(ii), whose proof (028 ll. 121–128) sets $X=\hat A^{-1}Y$ and concludes
   $\hat A^{-1}(Y^\ddagger)=(\hat A^{-1}Y)^\ddagger$ **for arbitrary $Y$**, with no reality
   assumption. The real-source restriction belongs to Lemma 2(iii) alone. So: *for an invertible
   $p_{2,2}$, 028 Lemma 2(ii) already gives the commutation at arbitrary argument and this record
   adds nothing.* What it does add is the **quotient case**: on $W_q$ the relevant statement is
   about classes, and 028's (iii) covers only real sources. (1.6) and script check
   `C2.3-quotient` supply that case.

### Derivation

**(1.1) $\mathcal V_4$ and $\mathcal V_5$ as pairings.** By (C7), for $A,B\in\mathrm{Sym}^2$ and
$C\in\mathrm{Sym}^3$,
$$
\mathcal V_4(A,B)=\braket{A,p_{2,2}B},\qquad \mathcal V_5(A,C)=\braket{A,p_{3,2}C}.
\tag{1.1}
$$
Both slots on the left are even-strand; the intermediate objects $p_{2,2}B$ and $p_{3,2}C$ on the
right live in the odd-strand $\mathrm{Sym}^2|_{N_{\rm gh}=6}$, which is why the derivation below is
organised so that $\ddagger$ is never applied to them.

**(1.2) Equivariance of the forms.** By H1 (PH6) and (C2),
$$
\mathcal V_4(A^\ddagger,B^\ddagger)=\mathcal V_4(A,B)^*,\qquad
\mathcal V_5(A^\ddagger,C^\ddagger)=\mathcal V_5(A,C)^*,
\tag{1.2}
$$
where $\ddagger$ acts componentwise (C2) on the even-strand spaces $\mathrm{Sym}^2|_4$ and
$\mathrm{Sym}^3|_6$, under which both are $\ddagger$-stable.

**(1.5) The kernel is $\ddagger$-stable and $\ddagger$ descends** (one line, from (1.2) alone).
Let $B\in\ker\mathcal V_4:=\{B:\mathcal V_4(A,B)=0\ \forall A\in\mathrm{Sym}^2\mathcal H_0\}$. By
(1.2),
$$
\mathcal V_4(A,B^\ddagger)=\mathcal V_4(A^\ddagger,B)^*=0\quad\text{for all }A,
\qquad\text{hence}\qquad(\ker\mathcal V_4)^\ddagger=\ker\mathcal V_4 ,
\tag{1.5}
$$
since $A\mapsto A^\ddagger$ is a bijection of $\mathrm{Sym}^2\mathcal H_0|_4$. Hence $\ddagger$
descends to $W_q$, $[B]^\ddagger:=[B^\ddagger]$, still antilinear and still an involution.

**(1.7) The composite $P=p_{2,2}^{-1}p_{3,2}$ is real.** Under H3 (PH5/R38),
$\mathcal V_5(\kappa,\cdot,\cdot)=0$ for $\kappa\in\ker\mathcal V_4$, so $p_{3,2}$ and $p_{2,2}$
both descend and $P:\mathrm{Sym}^3\mathcal H_0|_6\to W_q$ is well defined under H2 (PH1). It is
characterised, without reference to the odd-strand intermediate space, by
$$
\mathcal V_4(A,PC)=\braket{A,p_{2,2}p_{2,2}^{-1}p_{3,2}C}=\braket{A,p_{3,2}C}=\mathcal V_5(A,C)
\qquad\text{for all }A\in\mathrm{Sym}^2\mathcal H_0|_4 .
$$
Then, for every $C\in\mathrm{Sym}^3\mathcal H_0|_6$ and every $A$,
$$
\begin{aligned}
\mathcal V_4\big(A,\,P(C^\ddagger)\big)
  &=\mathcal V_5(A,C^\ddagger)\\
  &=\mathcal V_5(A^\ddagger,C)^*\\
  &=\mathcal V_4(A^\ddagger,PC)^*\\
  &=\mathcal V_4\big(A,(PC)^\ddagger\big),
\end{aligned}
\tag{1.7}
$$
and since $\mathcal V_4$ is non-degenerate on $W_q$ (H2 = PH1),
$$
\boxed{\;P(C^\ddagger)=(PC)^\ddagger\quad\text{in }W_q .\;}
$$
Every conjugation in (1.7) is taken on $\mathrm{Sym}^2\mathcal H_0|_4$ or on
$\mathrm{Sym}^3\mathcal H_0|_6$ — both even-strand. **This is the step by which PH7 is avoided**:
the odd-strand space $\mathrm{Sym}^2|_6$ appears only inside the *unconjugated* combination
$\braket{A,p_{3,2}C}$, which is a number.

*Remark (C2.5), not load-bearing.* One may instead fix the $\ddagger$ convention on
$\mathrm{Sym}^2|_6$ and prove $p_{2,2}(B^\ddagger)=(p_{2,2}B)^\ddagger$ and
$p_{3,2}(C^\ddagger)=(p_{3,2}C)^\ddagger$ separately, by (C6) in its two-space form. That route
needs $\ddagger^2=1$ on Grassmann-odd states, i.e. **PH7**, and inherits 028 (C2)'s
$(-1)^{k(k-1)/2}=-1$ sign ambiguity at $k=2$. It reaches the same conclusion because that sign is
an overall convention on the odd-strand space and cancels between $p_{3,2}$ and $p_{2,2}^{-1}$ in
every composite used below. The record does not take this route, and therefore does not inherit
PH7.

**(1.6) The inverse commutes with $\ddagger$ on classes.** State this for
$A\in\operatorname{im}p_{2,2}\subset\mathrm{Sym}^2\mathcal H_0|_6$, writing $A=p_{2,2}B$ for some
$B\in\mathrm{Sym}^2\mathcal H_0|_4$, with the conjugation on $A$ *transported* from the
even-strand space through $p_{2,2}$, $A^\ddagger:=p_{2,2}(B^\ddagger)$ — not the ambiguous
odd-strand convention of (C2). Then
$$
\boxed{\;(p_{2,2}^{-1}A)^\ddagger=p_{2,2}^{-1}(A^\ddagger)\quad\text{in }W_q ,\;}
\tag{1.6}
$$
holds for every such $A$, including non-real $B$ — a statement about **classes**: the left side is
$p_{2,2}^{-1}A=[B]$, so $(p_{2,2}^{-1}A)^\ddagger=[B]^\ddagger=[B^\ddagger]$ by (1.5)'s descended
involution on $W_q$; the right side is $p_{2,2}^{-1}(A^\ddagger)=p_{2,2}^{-1}(p_{2,2}(B^\ddagger))
=[B^\ddagger]$ by definition of the inverse on classes. The two sides coincide termwise, so (1.6)
is a restatement of (1.5) together with the definition of the transported $A^\ddagger$, and
carries no PH7. Well-posedness on classes is as before: if $X$ and $X+\kappa$,
$\kappa\in\ker\mathcal V_4$, are two representatives of $B$, then by (1.5)
$X^\ddagger-(X+\kappa)^\ddagger=-\kappa^\ddagger\in\ker\mathcal V_4$, so the two $\ddagger$-images
lie in the same class. For invertible $p_{2,2}$ (no kernel, $B$ a single vector) this is 028
Lemma 2(ii) verbatim under the transported convention; the class form is not new either, only
made explicit.

**(1.8) The composite $R=K_\Psi^{-1}p_{2,2}$ is real.** Write the dressed quartic form
$$
\mathcal V_4^\Psi(A,B):=\braket{A,K_\Psi B}=\mathcal V_4(A,B)-\tfrac{g_s}5\,\mathcal V_5(A,\Psi\odot B),
$$
a form on $\mathrm{Sym}^2|_4\times\mathrm{Sym}^2|_4$, equivariant by (1.2), $g_s\in\mathbb R$ and
$\Psi^\ddagger=\Psi$ (A4). Under H3 it descends to $W_q$; under H2′ (PH2) it is non-degenerate
there, so $R$ is well defined by $\mathcal V_4^\Psi(A,RB)=\mathcal V_4(A,B)$. Exactly as in (1.7),
$$
\mathcal V_4^\Psi\big(A,R(B^\ddagger)\big)=\mathcal V_4(A,B^\ddagger)=\mathcal V_4(A^\ddagger,B)^*
=\mathcal V_4^\Psi(A^\ddagger,RB)^*=\mathcal V_4^\Psi\big(A,(RB)^\ddagger\big),
\tag{1.8}
$$
hence $R(B^\ddagger)=(RB)^\ddagger$ in $W_q$. Again both slots are even-strand throughout.

### Commentary

- (1.5): the answer to the brief's explicit question, and it is one line. $\ddagger$-stability of
  $\ker\mathcal V_4$ is **not** an additional hypothesis: it follows from PH6 at $n=4$ and nothing
  else — not from $p_{2,2}$, not from non-degeneracy of $\omega_2$, not from anything in the odd
  sector. Stated as a standalone: *a $\ddagger$-equivariant form has a $\ddagger$-stable kernel,
  and the quotient by it inherits the involution.* (The first run of this record proved the same
  thing through the operator reality of $p_{2,2}$ and (C5)(i); that route is correct but longer,
  drags in $\omega_2$-non-degeneracy, and touches the odd-strand sector.)
- (1.7), line by line: the first equality is the characterisation of $P$; the second is (1.2) at
  $n=5$ with $A\mapsto A^\ddagger$ (H1); the third is the characterisation again; the fourth is
  (1.2) at $n=4$ (H1). Antilinearity is respected at every step — the complex conjugation on the
  right-hand side of line 2 is what turns the antilinear $\ddagger$ on both slots into a linear
  statement about $P$.
- (1.7) and (1.8) use PH5/R38 twice over: once so that $p_{3,2}$ and $K_\Psi$ are defined on
  classes, and once so that the characterising identities are identities *on $W_q$*. Without it
  the objects of §§2–3 are expressions in $\mathrm{Sym}^2\mathcal H_0$ that need not descend, and
  the whole statement "$\Sigma_2^\ddagger=\Sigma_2$ in $W_q$" has no subject. This is the
  condition that a toy with a generic invertible $\mathcal V_4$ cannot see (R17 annotation; 036 /
  R40), and it is why §4 now re-runs clauses 2 and 3 with a degenerate $\mathcal V_4$.
- (1.6): the trap the brief flags is that $\ddagger$ is antilinear while $p_{2,2}^{-1}$ is linear.
  (1.6) is a genuine commutation, not a conjugate-twisted one, precisely because no coefficient is
  moved past $\ddagger$ anywhere in the argument. A check that only tests (1.6) on
  $\ddagger$-real $A$ would be vacuous for the antilinearity question, since then both sides reduce
  to the same real vector; script check `C2.3` therefore tests generic complex $A$, and
  `C2.3-quotient` tests two representatives differing by a kernel element.
- Without H2 (PH1), C2.4: (C5)(iii) still gives reality of the solution class for a real source in
  $\operatorname{im}p_{2,2}$, which is all clause 2 needs at leading order; clause 3 needs the map
  statement (1.6)–(1.7) and hence H2. This is the same dependence 028 Step 2.3 carries.

### Result

Clause 1 holds: $\ddagger$ preserves $\ker\mathcal V_4$ (from PH6 at $n=4$ alone), descends to
$W_q$, and commutes with $p_{2,2}^{-1}$, with $P=p_{2,2}^{-1}p_{3,2}$ and with $R=K_\Psi^{-1}
p_{2,2}$ there — under PH6 ($n=4,5$), PH1, PH2 (for $R$) and PH5/R38 (for the descent). No
hypothesis new to the project; PH7 is not inherited, by (1.7).

### Verification

Script part 4, checks `C2.1` (operator reality of $p_{2,2}$, $p_{3,2}$ in the ungraded toy),
`C2.1-P` and `C2.1-R` (reality of the composites through their characterising identities, the
form (1.7)/(1.8) actually relied on), `C2.2` (kernel stability for a deliberately degenerate
$\mathcal V_4$), `C2.3` (commutation at generic complex $A$), `C2.3-quotient` (the genuine class
statement: two representatives differing by a kernel element have $\ddagger$-images in the same
class, and $\mathrm{pinv}(p_{2,2})A^\ddagger-(\mathrm{pinv}(p_{2,2})A)^\ddagger\in\ker$ without
being zero). Break legs `break-C2.1`, `break-C2.2`, `break-C2.3`, `break-C2.3-quotient`. See §4.

## 2. Clause 2 — the corrected saddle

### Setup

Assumptions A1–A4; H1 at $n=4,5$; H2 (PH1); H2′ (PH2) for the non-perturbative statement (2.6);
H3 (PH5/R38) throughout, without which none of the expressions below descends to $W_q$. Uses
(1.5), (1.7), (1.8) of §1.

### Derivation

**(2.1) The statement.** The corrected saddle of the quintic truncation (discussion §1, §2) is
$$
\Sigma_2^*(\Psi)=\Psi^{\otimes2}+\frac{g_s}5\,P(\Psi^{\otimes3})+O(g_s^2),
\qquad P=p_{2,2}^{-1}p_{3,2}.
\tag{2.1}
$$

**(2.2) Term by term**, written with the composite $P=p_{2,2}^{-1}p_{3,2}$ of (1.7) so that no
conjugation is taken on an odd-strand space. With $\Psi^\ddagger=\Psi$ (A4):
$$
\begin{aligned}
(\Psi^{\otimes2})^\ddagger
  &=\Psi^\ddagger\otimes\Psi^\ddagger=\Psi^{\otimes2},\\
\Big(\tfrac{g_s}5\,P(\Psi^{\otimes3})\Big)^\ddagger
  &=\tfrac{g_s^*}5\big(P(\Psi^{\otimes3})\big)^\ddagger\\
  &=\tfrac{g_s}5\,P\big((\Psi^{\otimes3})^\ddagger\big)\\
  &=\tfrac{g_s}5\,P(\Psi^{\otimes3}).
\end{aligned}
\tag{2.2}
$$
Hence, as classes in $W_q$,
$$
\big(\Sigma_2^*(\Psi)\big)^\ddagger=\Sigma_2^*(\Psi)+O(g_s^2).
\tag{2.3}
$$

**(2.4) The exact statement inside the quintic truncation.** The saddle is not only known to
$O(g_s)$: the $\Sigma_2$-equation of motion is linear, so (discussion §1)
$$
\Sigma_2^*=K_\Psi^{-1}p_{2,2}(\Psi^{\otimes2}),\qquad
K_\Psi=p_{2,2}-\tfrac{g_s}5\,p_{3,2}(\Psi,\cdot).
\tag{2.4}
$$
Rather than asserting the reality of $K_\Psi$ and of the source separately — which would require
$\ddagger$ on the odd-strand target — read the whole of (2.4) as the composite $R=K_\Psi^{-1}
p_{2,2}$ of (1.8):
$$
\Sigma_2^*=R(\Psi^{\otimes2}),\qquad
\mathcal V_4^\Psi(A,RB)=\mathcal V_4(A,B),\qquad
\mathcal V_4^\Psi(A,B)=\mathcal V_4(A,B)-\tfrac{g_s}5\mathcal V_5(A,\Psi\odot B).
\tag{2.5}
$$
$\mathcal V_4^\Psi$ is equivariant because $\mathcal V_4$ and $\mathcal V_5$ are (H1), $g_s$ is
real (A4) and $\Psi^\ddagger=\Psi$; it descends to $W_q$ by H3 (PH5/R38). $R$ is then real by
(1.8), and $\Psi^{\otimes2}$ is real by (C2), so
$$
\boxed{\;(\Sigma_2^*)^\ddagger=\Sigma_2^*\ \text{ in }W_q\;}
\tag{2.6}
$$
— to all orders of the formal $g_s$ expansion (PH1), and non-perturbatively in $g_s$ wherever
$K_\Psi$ is invertible on $W_q$ (PH2).
**The invertibility of $K_\Psi$ is PH2, not PH1.** The first run of this record wrote "invertible
on $W_q$ for small $g_s$ by Neumann series (011 §2) — no new condition at this order". The ledger's
PH2 row records exactly that reduction as *an argument, not a source statement*, and PH2 strictly
extends PH1 (019 ll. 299–301): $K_\Psi$ is the dressed kernel $\hat H_2(g_s,\Psi)$. Order by
order in $g_s$ the Neumann series does reduce to PH1, and the formal statement of (2.6) needs no
more; the non-perturbative half of (2.6) — which is the part that is *stronger than the brief
asked* — needs PH2.

**(2.7) Consistency of (2.1) with (2.4).** Expanding in the composite form (the only form
consistent with the grading),
$$
\Sigma_2^*=\Big(1-\tfrac{g_s}5\,P(\Psi,\cdot)\Big)^{-1}\Psi^{\otimes2}
=\Psi^{\otimes2}+\tfrac{g_s}5\,P(\Psi,\Psi^{\otimes2})+O(g_s^2),
\tag{2.7}
$$
and $P(\Psi,\Psi^{\otimes2})=P(\Psi^{\otimes3})$, reproducing (2.1). Every coefficient
of the Neumann series is a real rational multiple of a power of $g_s$, which is the order-by-order
form of (2.6).

### Commentary

- (2.2), line 1 $\to$ 2: $g_s^*=g_s$ by A4 and $\tfrac15\in\mathbb Q$ — this is the step the brief
  calls the antilinearity trap, and it is the only coefficient moved past $\ddagger$ in clause 2.
- (2.2), line 2 $\to$ 3: (1.7), which needs PH6 at $n=4,5$, PH1 and PH5/R38 together; line
  3 $\to$ 4: (C2) with $\Psi^\ddagger=\Psi$, on the even-strand $\mathrm{Sym}^3|_6$.
- (2.3) is an equality of classes in $W_q$. On representatives it holds modulo $\ker\mathcal V_4$,
  which is exactly the ambiguity $\Sigma_2$ has anyway (A3, R11's "residual freedom = kernel
  shifts"); by (1.5) that ambiguity is itself a $\ddagger$-stable subspace, so choosing a real
  representative is always possible ((C5)(iii)).
- (2.6) is stronger than the brief asks, and the strengthening is exactly where PH2 enters: the
  $O(g_s)$ truncation of the saddle is not where reality could have failed, because the exact
  quintic saddle is a real map applied to a real vector — but "exact" here means
  "non-perturbative in $g_s$", which presupposes that $K_\Psi$ is invertible on $W_q$ and not
  merely invertible as a formal series. Formal-series invertibility is PH1; the rest is PH2.
- There is no obstruction to exhibit. The only way clause 2 could have failed is a complex
  coefficient in (2.1) or a non-real $p_{3,2}$ — the first is excluded by inspection, the second
  is PH6.

### Result

Clause 2 holds, through $O(g_s)$ inclusive (2.3), to all orders of the formal $g_s$ expansion
under PH1, and non-perturbatively in $g_s$ within the quintic truncation under PH2 (2.6). All of
it presupposes PH5/R38 for the descent to $W_q$.

### Verification

Script part 4, checks `C3.1` (truncated saddle real), `C3.2` (exact $K_\Psi^{-1}$ saddle real, and
its $g_s$-expansion agrees with the truncated formula to $O(g_s^2)$, Richardson ratio $\simeq4$ —
the only check in part 4 that tests a *coefficient*), and their degenerate counterparts
`C3.1-deg`, `C3.2-deg`, run with the rank-deficient $\mathcal V_4$ under a $\mathcal V_5$ built to
annihilate $\ker\mathcal V_4$ (the PH5/R38 condition), which is what exercises H3. Break legs
`break-C3.1` (replacing $\tfrac15$ by $\tfrac i5$ makes the saddle non-real — a weak leg: it
tests only that `real2()` detects an imaginary coefficient) and `break-C3.2` (a non-equivariant
$\mathcal V_5$ does too — substantive).

## 3. Clause 3 — the gauge law

### Setup

Assumptions A1–A4; H1 at $n=4,5$; H2 (PH1); H2′ (PH2) for the exact law (3.6); H3 (PH5/R38)
throughout — term (c) below is the place where it is indispensable. Uses (1.5), (1.7),
(1.8), (2.5).

### Derivation

**(3.1) The law.** From the discussion §2,
$$
\delta\Sigma_2
=\underbrace{2\,\delta\Psi\otimes\Psi}_{(\mathrm a)}
+\underbrace{\tfrac{3g_s}5\,P(\delta\Psi,\Psi,\Psi)}_{(\mathrm b)}
+\underbrace{\tfrac{g_s}{10}\,P(\Sigma_2-\Psi^{\otimes2},\delta\Psi)}_{(\mathrm c)}
+O(g_s^2),\qquad P=p_{2,2}^{-1}p_{3,2}.
\tag{3.1}
$$
Take $\Psi^\ddagger=\Psi$, $\delta\Psi^\ddagger=\delta\Psi$ (A4), $\Sigma_2^\ddagger=\Sigma_2$.

**Descent to $W_q$ (H3 = PH5/R38).** $\Sigma_2$ is a class, so term (c) is an expression in a
class; it is defined only if $P(\kappa,\delta\Psi)=0$ for $\kappa\in\ker\mathcal V_4$, i.e. only
if $\mathcal V_5(\ker\mathcal V_4,\mathrm{Sym}^2\mathcal H_0,\mathcal H_0)=0$. The same condition
makes $K_\Psi$ of (2.4) act on $W_q$. This is H3, verbatim the ledger's 2026-09-19 R38 annotation;
without it (3.1) is not a law on $W_q$ and the clause has no subject. Every $O(g_s^{\ge3})$ row of
the ledger carries this condition (R17–R22, R24–R26, R30, R33, R34(2)) and 039 joins them.

**(3.2) Term (a).** With $2\in\mathbb R$ and (C2),
$$
(2\,\delta\Psi\otimes\Psi)^\ddagger=2\,\delta\Psi^\ddagger\otimes\Psi^\ddagger
=2\,\delta\Psi\otimes\Psi .
\tag{3.2}
$$

**(3.3) Term (b).** $\delta\Psi\odot\Psi\odot\Psi\in\mathrm{Sym}^3|_{N_{\rm gh}=6}$ is
$\ddagger$-real by (C2) — an even-strand space — so
$$
\Big(\tfrac{3g_s}5P(\delta\Psi,\Psi,\Psi)\Big)^\ddagger
=\tfrac{3g_s}5\,P\big((\delta\Psi\odot\Psi\odot\Psi)^\ddagger\big)
=\tfrac{3g_s}5\,P(\delta\Psi,\Psi,\Psi),
\tag{3.3}
$$
using $g_s^*=g_s$, $\tfrac35\in\mathbb Q$, then (1.7).

**(3.4) Term (c).** $X:=\Sigma_2-\Psi^{\otimes2}$ satisfies $X^\ddagger=\Sigma_2^\ddagger-
(\Psi^{\otimes2})^\ddagger=X$ ($\ddagger$ is additive, and real for real coefficients — here the
coefficients are $+1,-1$). Hence $X\odot\delta\Psi\in\mathrm{Sym}^3$ is $\ddagger$-real and
$$
\Big(\tfrac{g_s}{10}P(X,\delta\Psi)\Big)^\ddagger
=\tfrac{g_s}{10}\,P(X,\delta\Psi)
\tag{3.4}
$$
by (1.7), the equality holding in $W_q$ and the expression being defined there by H3.

**(3.5) The symmetrisation reading.** The source writes term (a) unsymmetrised. Two readings:
$$
(\mathrm a)_{\rm unsym}=2\,\delta\Psi\otimes\Psi\in\mathcal H_0^{\otimes2},\qquad
(\mathrm a)_{\rm sym}=\delta\Psi\otimes\Psi+\Psi\otimes\delta\Psi\in\mathrm{Sym}^2\mathcal H_0 .
\tag{3.5}
$$
By (C2), $\ddagger$ acts componentwise **without reordering sign** (legitimate because both
strands are Grassmann-even), so $\ddagger$ commutes with the flip $A\otimes B\mapsto B\otimes A$
and hence with the symmetriser. Both readings are therefore $\ddagger$-real, and
$((\mathrm a)_{\rm sym})^\ddagger=(\mathrm a)_{\rm sym}$,
$((\mathrm a)_{\rm unsym})^\ddagger=(\mathrm a)_{\rm unsym}$. **Reality does not depend on the
choice.** What the choice does affect is whether $\delta\Sigma_2$ lands in $\mathrm{Sym}^2$ at all:
$(\mathrm a)_{\rm unsym}$ does not, and only its symmetrisation is a legitimate variation of a
$\mathrm{Sym}^2$-valued field. The two agree when contracted into the symmetric vertices
$\mathcal V_4,\mathcal V_5$, which is the "declared to act inside symmetric vertices only" reading.
We adopt $(\mathrm a)_{\rm sym}$ throughout; the reality verdict is the same either way.

**(3.6) The exact law.** The same argument applies verbatim to the exact law (011 B.9),
$$
\delta\Sigma
=\delta(\Psi^{\otimes2})+\delta\Big[\tfrac{g_s}5K_\Psi^{-1}v\Big]
+\tfrac{g_s}{10}K_\Psi^{-1}p_{3,2}(\tilde X,\delta\Psi),
\qquad v=p_{3,2}(\Psi^{\otimes3}),\ \tilde X=\Sigma-\Sigma_2^* ,
\tag{3.6}
$$
because $K_\Psi^{-1}p_{2,2}=R$ is real (1.8) and $K_\Psi^{-1}p_{3,2}=RP$ is a composite of two
real maps between even-strand spaces, $\tilde X$ is real by (2.6), and all coefficients are real
rationals times $g_s$. The non-perturbative reading of (3.6) carries PH2 with $K_\Psi^{-1}$; the
order-by-order reading needs PH1 only. The middle term is the
variation of a real expression along a real direction and is real by real-linearity of $\delta$.
So reality is not an accident of the $O(g_s)$ truncation.

**(3.7) Conclusion.** The real locus $\{(\Psi,\Sigma_2):\Psi^\ddagger=\Psi,\ \Sigma_2^\ddagger=
\Sigma_2\}$ is mapped to itself by (3.1): $\delta\Sigma_2^\ddagger=\delta\Sigma_2$, so
$(\Sigma_2+\delta\Sigma_2)^\ddagger=\Sigma_2+\delta\Sigma_2$.

### Commentary

- Every step that moves $\ddagger$ past a coefficient is (A4) plus rationality of $2,\tfrac35,
  \tfrac1{10}$; every step that moves it past a map cites (1.7) or (1.8) (PH6 at $n=4,5$, PH1,
  PH5/R38; PH2 for $R$). There is no other kind of step in clause 3, and none of them applies
  $\ddagger$ to an odd-strand tensor.
- **What A4 is and is not.** $\delta\Psi^\ddagger=\delta\Psi$ is an assumption restricting the
  variations considered, not a theorem. The tangency argument — the $\Psi$ gauge law preserves
  $\Psi^\ddagger=\Psi$, so $\delta\Psi$ is tangent to the real locus, which is a real-linear
  subspace and therefore its own tangent space — establishes only the implication *if the $\Psi$
  gauge law maps the real locus into itself, then $\delta\Psi$ is real*. Its antecedent is the
  odd-sector statement: for $\delta\Psi=Q_B\Lambda+g_s\ell_2(\Psi,\Lambda)+\dots$ it holds iff
  $\Lambda^\ddagger=\Lambda$ is available, i.e. under PH7 ($\ddagger^2=1$ on Grassmann-odd states)
  together with the odd–even case of (C3) that 028 explicitly declines to use. **What this record
  proves is the restricted statement**: reality is preserved along those variations that are
  themselves real. Whether every gauge parameter $\Lambda$ produces such a variation is the
  odd-sector question and is *not settled here*. What *is* cleanly avoided is PH7 inside §§1–3,
  by (1.7)–(1.8): no conjugation is ever taken on an odd-strand space.
- Term (c) is the "rotation" of the deviation (discussion §2, R22): reality of the compensator is
  what guarantees that the contractible-pair mechanism does not push the auxiliary field off the
  real locus. This is the one place where a structural failure was conceivable — the compensator
  is forced, so its coefficient is not free to be adjusted — and it does not occur, because the
  forcing condition $2K_\Psi(\delta\tilde X,\tilde X)=-(\delta K_\Psi)(\tilde X,\tilde X)$ is an
  equation between $\ddagger$-equivariant forms with real data, whose solution is therefore real.
- What would break clause 3: a genuinely complex coefficient in the forced compensator (there is
  none: $-\tfrac12K_\Psi^{-1}\delta K_\Psi$ has rational coefficients), or a $\mathcal V_5$ that is
  not $\ddagger$-equivariant (PH6 at $n=5$), or a $\ker\mathcal V_4$ that is not $\ddagger$-stable
  (excluded by (1.5), itself a consequence of PH6 at $n=4$). What would make it *meaningless*
  rather than false is the failure of H3: a $\ker\mathcal V_4\neq0$ on which $\mathcal V_5$ does
  not vanish, so that (3.1) is not a law on $W_q$ at all.

### Result

Clause 3 holds for the variations of A4 — those tangent to the real locus — in both
symmetrisation readings, and for the exact law (3.6) as well as its $O(g_s)$ truncation, under
PH6 ($n=4,5$), PH1, PH5/R38, and PH2 for the non-perturbative form of (3.6). It does not settle
whether every gauge parameter produces a real $\delta\Psi$ (PH7).

### Verification

Script part 4, checks `C4.1` (each term real), `C4.1-deg` (the same with a degenerate
$\mathcal V_4$ and an $\mathcal V_5$ satisfying the PH5/R38 condition — this is the run that
exercises H3 on term (c)), `C4.2` (both readings real; and they agree inside
$\mathcal V_4,\mathcal V_5$), `C4.3` (exact law real). Break leg `break-C4.1`: $\tfrac{3}{5}\to
\tfrac{3i}{5}$ makes $\delta\Sigma_2$ non-real — a weak leg, see §4.

## 4. Verification (summary)

`codes/verify-reality-tower.py` part 4, added to the existing script (parts 1–3 unchanged and
still passing). Same finite-dimensional toy as 028: $\mathcal H_0=\mathbb C^N$ ($N=3$),
$\ddagger x=J\bar x$ with $J$ a real orthogonal reflection (so the $\ddagger$-real subspace is not
the coordinate one), $\omega_1(x,y)=x^{\rm T}y$, $\mathcal V_4,\mathcal V_5$ random symmetric
tensors made $\ddagger$-equivariant. $p_{2,2}$ and $p_{3,2}$ are the matrices of $\mathcal V_4$
and $\mathcal V_5$ in an orthonormal real basis of $\mathrm{Sym}^2$ and $\mathrm{Sym}^3$.

Part 4 now runs **two sectors**:

- the **invertible sector** ($\ker\mathcal V_4=0$), the toy's default and all the first run had;
- the **degenerate sector** ($\ker\mathcal V_4\neq0$), with $\mathcal V_5$ built to annihilate
  $\ker\mathcal V_4\odot\mathcal H_0$ — the PH5/R38 condition imposed by construction, check
  `C2.R38` — and every comparison made **as classes** in $W_q$ (projector onto the
  $\ker$-complement, plus the requirement that the raw vector difference be *non*-zero, so that
  a class statement is not mistaken for a vector identity).

This covers all three clauses in both sectors, except the exact-law check `C4.3` and the
symmetrisation check `C4.2`, which run in the invertible sector only.

Counts: **30 checks in part 4** — 16 positive and **14 break legs** — and **48/48 PASS overall**
with parts 1–3 (18 checks). Run 2026-09-22 at seed `20260914` (the original seed, kept) and
re-run at seed `20260922` via `VERIFY_SEED=20260922`: 48/48 at both.
(The record's first run said "5 break legs"; there were 6, then 13, and there are now 14.)

| Check | Node | What it tests | Falsified by |
|---|---|---|---|
| `C2.1` | C2.5 | $p_{2,2}\tilde J=\tilde J\bar p_{2,2}$ and the same for $p_{3,2}$ — the *individual*-operator route, which in the graded theory needs the odd-strand convention and PH7 | a non-equivariant component in $\mathcal V_4$ or $\mathcal V_5$ |
| `C2.1-P` | C2.1 | the composite $P=p_{2,2}^{-1}p_{3,2}$ of (1.7) is real, at generic complex $C$ | a non-equivariant $\mathcal V_5$ |
| `C2.1-R` | C2.1 | the composite $R=K_\Psi^{-1}p_{2,2}$ of (1.8) is real, at generic complex $B$ | a $\ddagger$-non-real $\Psi$ in the dressing |
| `C2.2` | C2.2 | for a rank-deficient $\mathcal V_4$ (a real null direction built in), $\ddagger(\ker)=\ker$ | a non-equivariant $\mathcal V_4$ |
| `C2.3` | C2.3 | $(p_{2,2}^{-1}A)^\ddagger=p_{2,2}^{-1}(A^\ddagger)$ at **generic complex** $A$ | a complex rescaling of $p_{2,2}$ |
| `C2.3-quotient` | C2.3 | the genuine class statement: (i) $\ddagger(X+\kappa)$ and $\ddagger X$ are in the same class while differing as vectors by $O(1)$; (ii) the commutation residual lies **in** $\ker$ and is not zero | a non-$\ddagger$-stable kernel (then $\ddagger$ is ill defined on classes) |
| `C2.R38` | H3 | the constructed degenerate $\mathcal V_5$ annihilates $\ker\mathcal V_4\odot\mathcal H_0$ and stays equivariant | — (construction check for the sector) |
| `C2.1-P-deg` | C2.1 | $P$ real **as a class** on $W_q$ with $\ker\mathcal V_4\neq0$ | a non-equivariant $\mathcal V_5$ |
| `C3.1` | C3.1 | $\ddagger$-reality of the truncated saddle at $g_s=0.37$ | complex $\tfrac15$; a $\ddagger$-non-real $\Psi$ |
| `C3.2` | C3.2 | $\ddagger$-reality of $R(\Psi^{\otimes2})$, and agreement with the truncation to $O(g_s^2)$ (Richardson ratio $\simeq4$ at $g_s=0.05$) — the only check that tests a *coefficient* | complex $\tfrac15$; non-equivariant $\mathcal V_5$ |
| `C3.1-deg` | C3.1 | the same as a class, with $\ker\mathcal V_4\neq0$ | — |
| `C3.2-deg` | C3.2 | the same as a class, with $\ker\mathcal V_4\neq0$ (Richardson ratio $\simeq4$) | — |
| `C4.1` | C4.1 | each of (a), (b), (c) separately $\ddagger$-real | complex $\tfrac35$ or $\tfrac1{10}$; a $\ddagger$-non-real $\delta\Psi$ |
| `C4.1-deg` | C4.1 | the same as a class with $\ker\mathcal V_4\neq0$, **and** term (c) independent of the representative of $\Sigma_2$ — the check that exercises H3 | — |
| `C4.2` | C4.2 | both symmetrisation readings $\ddagger$-real, and equal inside $\mathrm{Sym}^2$ | — (see the honesty note below) |
| `C4.3` | C4.3 | the exact law (3.6) $\ddagger$-real | a $\ddagger$-non-real variation direction |

The 14 break legs: `break-C2.1`, `break-C2.1-P`, `break-C2.1-R`, `break-C2.2`, `break-C2.3`,
`break-C2.3-quotient`, `break-R38`, `break-C3.1`, `break-C3.1b`, `break-C3.2`, `break-C3.2b`,
`break-C4.1`, `break-C4.1b`, `break-C4.3`. Each is a deliberate perturbation of the tested
expression, asserted to make the corresponding check fail, so that a `PASS` on the break leg
means the main check is not vacuous. `break-C3.2b` is the wrong-coefficient leg for `C3.2`'s
Richardson ratio ($\tfrac15\to0.25$ in the truncation only, exact saddle unchanged): the deviation
becomes $O(g_s)$ instead of $O(g_s^2)$, so the ratio moves away from $4$ and fails
$|r-4|<0.3$ — the check that was adjusted after failing (§2 commentary) is the one that most
needed this leg, since it was previously the only half of part 4 with no break leg at all.

**What the weak legs do and do not establish.** `break-C3.1` ($\tfrac15\to\tfrac i5$) and
`break-C4.1` ($\tfrac35\to\tfrac{3i}5$) establish only that the reality test `real2()` detects an
imaginary multiple; they test no structure. They are kept for completeness and *supplemented* by
`break-C3.1b` and `break-C4.1b`, which make $\Psi$ resp. $\delta\Psi$ $\ddagger$-non-real and are
substantive: they test that the conclusion depends on A4 and not only on the rationality of the
coefficients. `break-R38` is the most informative of the new legs: without
$\mathcal V_5(\ker\mathcal V_4,\cdot,\cdot)=0$, $P$ maps a kernel direction to a **non-zero
class**, so the $O(g_s^3)$ objects do not descend to $W_q$ at all.

**`C4.2` is near-tautological and its stated falsifier is not implementable.** `to2(a_unsym) -
a_sym` vanishes because `B2.T` annihilates the antisymmetric part by construction; and the
falsifier the first run gave — "a reordering sign in (C2)" — cannot be introduced in a toy with no
Grassmann grading, where $\ddagger$ is $x\mapsto J\bar x$ on an ungraded $\mathbb C^N$. What
`C4.2` does establish is the transcription statement that the two readings agree in
$\mathrm{Sym}^2$ coordinates; the *reality* half of (3.5) is not independently tested by it.

**Not verified by the script**, and not verifiable in this toy:

- PH6 itself (the CFT reality of the worldsheet $\mathcal V_n$ — conjugation invariance of the
  moduli regions and of the measures); PH1 and PH2 (the level-truncation / kernel-stability and
  dressed-kernel invertibility package).
- **The entire graded layer.** $\omega_1(x,y)=x^{\rm T}y$ is symmetric and ungraded, and the
  source and target of $p_{2,2}$ are identified by the same basis `B2`. The toy therefore cannot
  see the $+2$ ghost shift of $p_{2,2}$, cannot see that its target is odd-strand, and cannot see
  the reordering-sign convention of 028 (C2). **None of the three odd-sector questions of §1 can
  fail in it.** It is a faithful representation of the *ungraded linear algebra* of the clauses
  and of nothing more — in particular it does not test that the composite route of (1.7)–(1.8)
  avoids PH7, which is a statement about the graded theory and is established by inspection of
  which spaces carry a $\ddagger$, not by the toy.
- PH5/R38 itself. The degenerate sector *imposes* the condition and checks that the objects then
  descend and are real; whether the actual vertices satisfy it is the numerical question of plan
  Task 15 Q2, not a question this toy can answer.
- The constructed degenerate $\mathcal V_5$ is not totally symmetric, so R38 is imposed in the
  $\mathrm{Sym}^3$ slot only; for a totally symmetric $\mathcal V_5$ the condition propagates to
  the $\mathrm{Sym}^2$ slot, and that propagation — used by (1.8) for the $A$-slot descent of
  $\mathcal V_4^\Psi$ — is not tested here.
- `C2.3` and `C2.3-quotient` test the ungraded transcription of (1.6); since the toy carries no
  grading (above), they check the class-commutation numerically but cannot distinguish the
  transported-convention proof of (1.6) — which needs no odd-strand convention and no PH7 — from
  a statement of (1.6) on the ambiguous odd-strand space, which would need PH7. That distinction
  is made in the record by inspection of which spaces carry a $\ddagger$ (see (1.6)), not by this
  check.

## 5. Depth checks and regime of validity

Which of the depth checklist items were run:

- **Limiting case $g_s\to0$.** (2.1) reduces to $\Psi^{\otimes2}$ and (3.1) to the R11 composite
  law $\delta\Sigma=\delta\Psi\otimes\Psi+\Psi\otimes\delta\Psi$; both are $\ddagger$-real by (C2)
  alone, recovering the known $O(g_s^2)$ statement of the note and 028 Step 2.3's leading term.
  Run, in the derivation (C3.3) and in the script (`C3.2`, `C3.2-deg` compare the two at small
  $g_s$ through a Richardson ratio).
- **Second method for clause 1.** Three routes, not two. (i) The composite route (1.7)–(1.8),
  which is the record's argument and stays on even-strand spaces. (ii) The individual-operator
  route (C2.5): $p_{2,2}$ and $p_{3,2}$ real separately via (C6) in its two-space form, which
  needs the odd-strand $\ddagger$ convention and PH7 — same conclusion, stronger hypotheses.
  (iii) For C2.2 specifically, the one-line kernel argument of (1.5), which uses PH6 at $n=4$ and
  nothing else — neither $p_{2,2}$, nor $\omega_2$-non-degeneracy, nor the odd sector, and which
  *strengthens* the headline "consequence, not hypothesis". The finite-dimensional realisation of
  §4 is **not** counted as a second method: it is a generic instance of the same algebraic
  situation, and it tests the transcription and the kernel bookkeeping, not the argument.
- **Dimensional / grading check (corrected).** By R23's $N_{\rm gh}(p_{k,\ell,g})=3\ell-2k+g$:
  $N_{\rm gh}(p_{2,2})=3\cdot2-2\cdot2+0=+2$, so $p_{2,2}$ maps $N_{\rm gh}=4$ to $N_{\rm gh}=6$;
  $N_{\rm gh}(p_{3,2})=3\cdot2-2\cdot3+0=0$, so $p_{3,2}$ maps $N_{\rm gh}=6$ to $N_{\rm gh}=6$.
  Equivalently, $\omega_1$ saturates at $N_{\rm gh}(A)+N_{\rm gh}(B)=5$, so $\omega_2$ pairs 4
  with 6 and $\mathcal V_4(A,B)=\braket{A,p_{2,2}B}$ forces the $+2$ shift. This agrees with
  `knowledge/reading-map.md` l. 39 ("input 4, output 6") and with the project convention
  $N_{\rm gh}(m_2)=+2$. $\ddagger$ preserves ghost number (C1), so every equation above is
  homogeneous. Run.

  **Correction of the first run.** That run wrote "$p_{2,2}$ maps $N_{\rm gh}=4$ to $4$" and
  "$p_{3,2}$ maps $6$ to $4$" — a third variant of the trap `reading-map.md` l. 39 flags. Both are
  wrong; read that way, $\braket{A,p_{2,2}B}$ would have slot sum 8 and vanish identically. **The
  two errors cancel in the composite $p_{2,2}^{-1}p_{3,2}$** ($6-2=4$ either way), which is why no
  formula of §§2–3 changes. What did change is the framing: the corrected grading is what exposes
  the odd-strand target, and hence the PH7 question that §1 now handles by (1.7).
- **Regime of validity.** Everything in §§1–3 is at the **algebraic layer**: a statement about
  $\ddagger$-equivariant multilinear forms and real maps on a finite-dimensional space, formal in
  $g_s$ unless PH2 is invoked. Four things are *not* at this layer and are carried as hypotheses:
  - **PH6** ($n=4,5$) — the CFT reality of $\mathcal V_4,\mathcal V_5$, where conjugation
    invariance of the moduli regions and measures of the vertex family would have to be checked
    (open for the SL(2,C) family, per the PH6 status cell);
  - **PH1** — invertibility of $p_{2,2}$ on the quotient, a level-truncation statement;
  - **PH2** — invertibility of the dressed kernel $K_\Psi$ on the quotient, which strictly
    extends PH1 and carries the non-perturbative-in-$g_s$ half of (2.6) and (3.6);
  - **PH5/R38** — $\mathcal V_5(\ker\mathcal V_4,\cdot,\cdot)=0$ (or $\ker\mathcal V_4=0$),
    without which the $O(g_s^3)$ objects do not descend to $W_q$ and the statement has no
    subject. Whether $\ker\mathcal V_4\neq0$ for the actual vertices is the numerical test of
    plan Task 15 Q2.

  If any of the four fails, the conclusion fails with it, and the failure is the hypothesis's,
  not this record's.
- **Interpretation.** The reason reality survives is structural and worth one sentence in the
  notes: *the correction to $\Sigma_2$ is built from real maps acting on real data with rational
  coefficients, and inverting a real map on a $\ddagger$-stable quotient produces a real map.*
  The inverse $p_{2,2}^{-1}$, which is the new feature at the quintic order, is harmless for
  reality precisely because reality is an operator property that inversion preserves, and the
  quotient it is defined on is itself $\ddagger$-stable for the same reason the map is real. The
  places where reality could still fail at higher orders are not the inverse but the vertices
  (PH6 at $n\ge6$) and the descent to the quotient (PH5/R38).
- **Not checked.** The gauge-algebra closure at $O(g_s^3)$ (the other open action of the
  2026-09-19 discussion) — out of scope and independent of reality. **PH7 and the odd sector**:
  this record does not settle whether every gauge parameter $\Lambda$ produces a
  $\ddagger$-real $\delta\Psi$; it proves the statement for the variations of A4, and it avoids
  PH7 *internally* by (1.7)–(1.8). The $O(g_s^4)$ statement — the same argument applies verbatim
  provided PH6 extends to $n=6$, PH5/R38 extends to $\mathcal V_6$, and $p_{2,2}$-type inverses
  remain the only inverses appearing, but the $O(g_s^4)$ law (015 §4) was not read for this
  record, so that extension is stated as an expectation, not a result.

## 6. Proposed ledger row (for the orchestrator; not applied here)

> **Reality of $\Sigma_2$ at $O(g_s^3)$ (closes the 2026-09-19 open action).** With
> $\Psi^\ddagger=\Psi$ and $\delta\Psi^\ddagger=\delta\Psi$: the corrected saddle
> $\Sigma_2^*=K_\Psi^{-1}p_{2,2}(\Psi^{\otimes2})$ and the corrected gauge law
> $\delta\Sigma_2=2\,\delta\Psi\odot\Psi+\tfrac{3g_s}5P(\delta\Psi,\Psi,\Psi)
> +\tfrac{g_s}{10}P(\Sigma_2-\Psi^{\otimes2},\delta\Psi)+O(g_s^2)$, with
> $P=p_{2,2}^{-1}p_{3,2}$, both preserve $\Sigma_2^\ddagger=\Sigma_2$ in
> $W_q=\mathrm{Sym}^2\mathcal H_0/\ker\mathcal V_4$ — to all orders of the formal $g_s$
> expansion (PH1), and non-perturbatively in $g_s$ within the quintic truncation wherever
> $K_\Psi$ is invertible on $W_q$ (PH2). Mechanism: $\mathcal V_4,\mathcal V_5$
> $\ddagger$-equivariant $\Rightarrow$ the composites $P=p_{2,2}^{-1}p_{3,2}$ and
> $R=K_\Psi^{-1}p_{2,2}$ are real maps between even-strand spaces, characterised by
> $\mathcal V_4(A,PC)=\mathcal V_5(A,C)$ and $\mathcal V_4^\Psi(A,RB)=\mathcal V_4(A,B)$;
> $\ker\mathcal V_4$ is $\ddagger$-stable and $\ddagger$ descends to $W_q$; all coefficients are
> real rationals times real $g_s$. **$\ddagger$-stability of $\ker\mathcal V_4$ is a consequence
> of PH6 at $n=4$ alone** — one line from $\mathcal V_4(A,B^\ddagger)=\mathcal V_4(A^\ddagger,B)^*$
> — not a new hypothesis. Reality is insensitive to whether $2\,\delta\Psi\otimes\Psi$ is
> symmetrised; the choice affects only whether $\delta\Sigma_2\in\mathrm{Sym}^2$. **PH7 is not
> needed for the statement proved here**, which is about variations already tangent to the real
> locus and whose load-bearing chain stays on even-strand spaces (no $\ddagger$ is applied to the
> odd-strand $N_{\rm gh}=6$ target of $p_{2,2}$ and $p_{3,2}$ anywhere in C1); whether every gauge
> parameter produces such a variation is the odd-sector question (PH7) and is **not settled here**.
> Carve-outs: algebraic layer; PH6 at $n=4,5$; PH1 for the inverse on the quotient; PH2 for the
> non-perturbative form; PH5/R38 for the descent to $W_q$ ($N_{\rm gh}(p_{2,2})=+2$ per R23).
> | `Conditional(PH6 [n=4,5], PH1, PH2, PH5/R38) – Verified` (numpy toy, part 4 of
> `codes/verify-reality-tower.py`: 30 checks, 16 positive and 14 break legs, 48/48 with parts
> 1–3, at seeds 20260914 and 20260922. The toy is **ungraded**: it verifies the linear algebra of
> all three clauses in the $\ker\mathcal V_4=0$ sector and, except for the exact-law check `C4.3`
> and the symmetrisation check `C4.2`, in the $\ker\mathcal V_4\neq0$ sector as well, the latter
> with the PH5/R38 condition imposed by construction in the $\mathrm{Sym}^3$ slot and falsified by
> `break-R38`; it cannot see the ghost grading, the
> odd-strand target, or PH7) | `agent/derivations/039-reality-ogs3.md`;
> `codes/verify-reality-tower.py` part 4

## Annotation 2026-10-01 (node check `agent/reports/critic-r11-r13-c3-20261001T093500.md`, conventions C3)

The record is consolidated; the following sentences are corrected here, not edited in place.


- §3 Commentary, l. 671–673, replace with: "Its antecedent is the odd-sector statement: for $\delta\Psi=Q_B\Lambda+g_s\ell_2(\Psi,\Lambda)+\dots$ it holds iff $\Lambda^\ddagger=-\Lambda$ (conventions C3; Zwiebach (3.18)). The reason is that $(Q\Lambda)^\ddagger=-Q\Lambda^\ddagger$ and $\ell_n(\Psi^{n-1},\Lambda)^\ddagger=-\ell_n(\Psi^{n-1},\Lambda^\ddagger)$ for real $\Psi$; the second identity is PH6 read with the Koszul sign on its two odd arguments. $\ddagger^2=1$ on odd states (PH7, discharged) makes such $\Lambda$ span the parameter space."
- A4 (l. 158–159), C4.4 (l. 234–235), §3 Result (l. 696), §5 (l. 862–865) and §6 (l. 891–892) all say "the odd-sector question (PH7) … not settled here". Replace with: "answered under C3: every $\Lambda$ with $\Lambda^\ddagger=-\Lambda$ gives a real $\delta\Psi$, given PH6 in signed form at $n=3,4,5$ (node check 2026-10-01)".
