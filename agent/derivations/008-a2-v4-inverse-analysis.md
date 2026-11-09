# Derivation record 008 — A2(i)/(ii): the inverse quartic vertex $V_4^{-1}$ — coloured grading and Schwinger representation

Date: 2026-07-02
Author: Claude Fable 5 (inline, per state-file resume sequence "Phase A / A2", parts
(i) and (ii); part (iii) is specced in §4 for a dedicated numerics session).
Task source: `knowledge/fable-2026-07-01-assessment-and-results.md` §6bis(a),(b)
(the points on the matrix/double-line picture and the Schwinger parametrization).
Verification: `codes/verify-a2-schwinger.py` (numpy 2.5.0 / scipy 1.18.0; spectral and
quadrature checks — this is numerical, not sympy, by the nature of the statements;
8/8 PASS, executed).
Critic: iter 1 (Opus, blind) → **REVISE, 0 Fatal / 0 Serious — all decisive
arithmetic hand-re-verified** (`agent/reports/critic-a2-v4-inverse-20260702T003000.md`).
All findings (framing/attribution: "real topology" softened to formal
Euler-characteristic bookkeeping; inner-product-dependence of positivity made
explicit; $g_s$ cross-check recast as contrapositive; script checks 1b/3–4 retagged;
un-ledgered normalisation-constant formula removed; "equal mass-squared";
large-$\beta$ positivity argument added) applied in this revision; the critic's
recommendation authorizes promotion as R15 with the §5 carve-outs.
Companion: derivation 007 (A1) supplies the Feynman rules and the telescoping identity
used throughout.

Reused verbatim (not re-derived): **A1/007** (propagator $(12/g_s^2)(V_4|_{\rm Sym^2})^{-1}$,
telescoping, kernel decoupling), **R7** (physical grading, all fields even in this
sector), **H2 closed** (total graded symmetry of $V_4$), companion-project **R4/R5/R6**
(companion SL(2,C) project ledger: tachyon-sector
$\{T^4\}$ exact formula and its finite-momentum extension).

---

## 0. Summary of claims

1. **(i) Coloured grading.** In the 2-coloured (multi-string) description — colour 1 =
   single-string leg carrying $\mathcal H_0$, colour 2 = double-string leg carrying
   $\operatorname{Sym}^2\mathcal H_0$ — the Σ-propagator $V_4^{-1}$ is **one elementary
   edge** (a double line), and the HS diagrams are graded by the **coloured** loop
   number, not by the genus of the underlying uncoloured surface. The underlying
   surface of a length-$k$ chain of 4-punctured spheres joined by $k-1$ colour-2 edges
   (= $2(k-1)$ simultaneous ordinary plumbings) has $\chi=-2k$, $n=4$, hence
   $g=k-1$ — a *formal Euler-characteristic bookkeeping of a hypothetical worldsheet
   resolution at fixed/degenerate plumbing* (the genus-$(k-1)$ moduli, dimension
   $3g-3+n=3k-2>0$ for $k\ge2$, never appear: the chain carries no moduli integral)
   [critic iter 1], and in any case *not* the diagram grading, exactly as a nonplanar
   matrix-model diagram is not thereby a loop diagram ('t Hooft double line). This
   formalizes §6bis(a) and dissolves the "genus tension" (Fable-note critic C3) in the
   sharp form: **coloured-tree $\neq$ uncoloured-genus-0, and the coloured grading is
   the physical one for the auxiliary theory.**
2. **(ii) Schwinger representation.** The naive
   $V_4^{-1}=\int_0^\infty\!dt\,e^{-tV_4}$ holds **iff** $V_4|_{\operatorname{Sym}^2}$
   is positive definite — which is *not* to be expected (an indefinite spectrum is the
   generic situation and is empirically undecided, §4). The **always-valid** variant
   for real-symmetric invertible $V_4$ is
   $$
   V_4^{-1}=\int_0^\infty\!dt\;V_4\,e^{-tV_4^2},
   \tag{B.1}
   $$
   whose integrand expands in **odd** chains $V_4^{2k+1}$ only (underlying genus
   $0,2,4,\dots$), with the Gaussian-in-$t$ damping replacing sign conditions. In
   sandwiched position the $t$-integral **collapses**:
   $\int_0^\infty dt\,V_4(V_4e^{-tV_4^2})V_4=V_4$ — consistent with A1's telescoping;
   the Schwinger time $t$ is a spectral parameter, **not** a modulus of any surface
   (the colour-2 edge carries no modulus), in sharp contrast with
   $1/L_0^+=\int ds\,e^{-sL_0^+}$ where $s$ *is* the cylinder length.
3. **Level-0 anchor (empirical input to the kernel/positivity questions).** From the
   companion SL(2,C) computation (R5): the zero-momentum tachyon-diagonal matrix element
   $V_4(T^{\otimes2},T^{\otimes2})=\{T^4\}$ is a nonzero constant times a strictly
   positive moduli integral over $\mathcal V_{0,4}$ (value from the companion SL(2,C)
   computation, not reproduced here),
   hence **nonzero**: no kernel in the level-0 diagonal block. R6 extends this to
   tachyons of equal mass-squared $k_a^2\equiv k^2$ (R6's scope; it does *not* collapse
   for unequal $k_a^2$): the Koba–Nielsen integrand is strictly positive, so the
   diagonal kernel element is nonvanishing wherever the contact integral converges.
   The **sign** (hence the positivity question in (ii)) is *not* settled — the overall
   normalisation constant is open, and its sign is not yet fixed.
4. **(iii) spec.** The full rank/spectrum test at low level needs matrix elements with
   massless insertions, which the companion project's tachyon-only collapse (its R1/R4)
   does **not** cover — the modular Jacobian is no longer $\equiv1$ and all four
   Schiffer vectors contribute. §4 gives the precise task spec (a dedicated
   computator/numerical-verifier session with the companion-project machinery).

---

## 1. Setup

Conventions as in derivation 007 §1 (finite-dimensional stand-in, physical grading,
everything Grassmann-even in this sector, $e^S$ convention). $V_4$ denotes the
symmetric bilinear form on $\operatorname{Sym}^2\mathcal H_0$ (kernel quotiented per
R13/§3 when degenerate); "spectrum" refers to the eigenvalues of its matrix in an
orthonormal basis of $\operatorname{Sym}^2\mathcal H_0$ w.r.t. an auxiliary
positive-definite inner product (level-truncation Euclidean product). **This auxiliary
choice is not canonical** — the BPZ pairing $\omega_1$ is not positive definite — and
in infinite dimensions "self-adjointness of $V_4$" depends on it; this is flagged as
an open regularity input (§5), same family as the closed-range condition of R10
route (B). Sharp consequence [critic iter 1]: **the (B.3)-vs-(B.1) dichotomy —
"is $V_4$ positive definite?" — is a statement about the pair $(V_4,G)$ with $G$ the
chosen inner product, not about the vertex form alone** (the tested operator is
$G^{-1}V_4$); only the *form-inverse* $V_4^{-1}$ (upper indices) entering the
propagator is canonical, recovered as $(G^{-1}V_4)^{-1}G^{-1}$. Nothing physical rides
on the choice: the sandwiched collapse (B.4) is $G$-independent.

## 2. (i) The coloured grading and the double-line edge

**Definitions.** Work in the 2-coloured setting of §6bis(a): objects
$c_1=\mathcal H_0$, $c_2=\operatorname{Sym}^2\mathcal H_0$. The HS action's
ingredients are coloured corollas:

- $V_3(\Psi^3)$: corolla $(1,1,1)$;
- $V_4(\Sigma,\Psi^{\otimes2})$: corolla $(2,1,1)$ — the 4-punctured-sphere vertex
  with two punctures bundled into one colour-2 leg;
- $-\tfrac{g_s^2}{4!}V_4(\Sigma,\Sigma)$: the colour-2 kinetic form $(2,2)$.

Composition along a colour-1 edge is ordinary plumbing (with the $\Psi$ propagator);
composition along a colour-2 edge contracts with $V_4^{-1}$ (A1's propagator, up to
the $12/g_s^2$ normalization) — **one** elementary composition, drawn as a double
line. The coloured loop number of a diagram is
$L_c=E-V+1$ (connected), counting *both* colours of edges, each as one edge.

**Two gradings, one $\chi$-arithmetic.** Consider the length-$k$ chain: $k$ corollas
$(2,1,1)$ or $(2,2)$ joined linearly by $k-1$ colour-2 edges (this is the $V_4^k$
power appearing in any expansion of $V_4^{-1}$, e.g. a Neumann or Schwinger series).

- **Coloured grading:** it is a *tree*: $E=k-1$, $V=k$, $L_c=0$.
- **Underlying uncoloured surface:** each colour-2 edge is two simultaneous ordinary
  plumbings, so the surface is $k$ 4-punctured spheres glued along $2(k-1)$ necks:
  $$
  \chi=\sum_{i=1}^k\chi(S^2\smallsetminus4\,\mathrm{pts})=-2k,\qquad
  n_{\rm ext}=4k-4(k-1)=4,\qquad
  2-2g-n=\chi\;\Rightarrow\;g=k-1 .
  \tag{B.2}
  $$
  (Gluing along circles preserves $\chi$ additivity, $\chi(S^1)=0$.)

Both computations are correct; they grade **different things**. The auxiliary theory's
perturbative expansion, its power counting in $g_s$, and its tree/loop split are
governed by $L_c$ (the coloured grading): a Σ-exchange is a tree-level event no matter
how much genus the underlying uncoloured surface carries — precisely as a nonplanar
contraction in a matrix model is still a tree diagram of the matrix field. The
uncoloured genus is bookkeeping of the *worldsheet realization*, relevant only if one
insists on resolving the colour-2 edge into ordinary plumbings (which A1 shows is
never necessary in amplitudes: the edge telescopes away).

**Retraction honoured.** Per §6bis(a), "the 2→2 plumbing is iterated ordinary
plumbing" is *not* a statement about the coloured operad — there the colour-2
composition is elementary; the iteration is only how it decomposes in the uncoloured
modular operad. Nothing in this section claims otherwise.

**$g_s$-counting cross-check.** With $V_4\sim g_s^2$ and propagator $\sim g_s^{-2}$
(A1), the length-$k$ chain carries $g_s^{2k}\cdot g_s^{-2(k-1)}=g_s^2$: every chain
contributes at the same order as one $V_4$ — as it must, since the chains resum to
$V_4$ by telescoping in sandwiched position; the count is thus a **consistency
requirement, not independent corroboration** [critic iter 1]. The genuinely
inferential content is the *contrapositive*: grading by the uncoloured genus would
predict a $g_s^{2(k-1)}$ suppression of the length-$k$ chain, which contradicts the
actual uniform $g_s^2$ — so the uncoloured grading is **inconsistent with the coupling
expansion**, while the coloured grading agrees with it. That is the argument (in its
honest form) for the coloured grading being the physical one.

## 3. (ii) Schwinger parametrization of $V_4^{-1}$

**Assumptions.** $A:=V_4|_{\operatorname{Sym}^2}$ real symmetric (H2 + choice of
auxiliary inner product, §1), invertible on the quotient (R13). Finite-dimensional
statements; the infinite-dimensional upgrade needs $A$ self-adjoint and $0\notin$
spectrum (closed range), flagged open.

**(a) Direct form — conditional.**
$$
A^{-1}=\int_0^\infty\!dt\,e^{-tA}
\qquad\Longleftrightarrow\qquad
\operatorname{spec}(A)\subset(0,\infty).
\tag{B.3}
$$
For sectorial $A$ (spectrum in a half-plane) a rotated contour works; for genuinely
indefinite real spectrum — the situation to be *expected* for a vertex form with both
signs, cf. §4 — no rotation of (B.3) converges.

**(b) Squared form — unconditional (for symmetric invertible $A$).**
$$
A^{-1}=\int_0^\infty\!dt\;A\,e^{-tA^2},
\tag{B.1}
$$
valid because $A^2$ is positive definite whenever $A$ is symmetric invertible;
spectrally, $\lambda^{-1}=\int_0^\infty\lambda\,e^{-t\lambda^2}dt$ for every real
$\lambda\neq0$. This is the form worth carrying: **no positivity assumption on the
vertex**.

**(c) Surface reading.** Expanding the exponentials:
- (B.3) generates all chain lengths: $e^{-tA}=\sum_k\frac{(-t)^k}{k!}A^k$ — the
  length-$k$ ladders of §2, genus $k-1$ in the uncoloured reading;
- (B.1) generates **odd** chains only: $A\,e^{-tA^2}=\sum_k\frac{(-t)^k}{k!}A^{2k+1}$
  — genus $0,2,4,\dots$ ladders. Both expansions are statements about the
  **integrand** only: term-by-term $t$-integration diverges ($\int_0^\infty t^k dt$),
  so neither is a convergent ladder expansion of $V_4^{-1}$ itself [critic iter 1].
  The absence of even chains is the spectral parity of the inverse ($A^{-1}$ is an odd
  function of $A$) — a formal-curiosity remark (these ladders never appear in
  amplitudes anyway; the edge telescopes, A1), recorded because it constrains any
  attempted surface organization of $V_4^{-1}$ to odd-length ladders.

**(d) The Schwinger time is not a modulus.** In $1/L_0^+=\int_0^\infty ds\,e^{-sL_0^+}$
the parameter $s$ is the length of a flat cylinder — a bona fide modulus of the glued
surface, and the $s$-integral *is* (part of) the moduli integral. In (B.1)/(B.3) the
$t$-parameter conjugates the *vertex form itself*; the colour-2 edge carries no
modulus (A1: the propagator has no $b$-ghost insertions and no moduli integral), and
$t$ is a spectral regulator. Two structural facts make this concrete:

1. **Collapse in sandwiched position.** In any amplitude the representation sits
   between two vertices, and the $t$-integral collapses *before* any surface
   interpretation is needed:
   $$
   \int_0^\infty\!dt\;V_4\big(V_4e^{-tV_4^2}\big)V_4
   =V_4\,V_4^{-1}V_4=V_4 ,
   \tag{B.4}
   $$
   (and likewise with (B.3) in the positive-definite case). This is §6bis(b)'s
   consistency requirement (iii), now an identity rather than a demand.
2. **No $g_s$-grading of $t$.** The $t$-expansion reshuffles terms all at the same
   $O(g_s^2)$ (§2 $g_s$-cross-check); a modulus would not do that.

**(e) What would make (B.3) available after all.** If the (iii) numerics (§4) found
$V_4|_{\operatorname{Sym}^2}$ positive definite on the physical quotient (in a natural
inner product), the direct heat-kernel form with its uniform ladder expansion would be
preferred (better convergence, single exponential). The known level-0 data (§4) is
compatible with either sign; the question is genuinely empirical at this point. Until
then, (B.1) is the safe default.

## 4. Numerical anchors and the (iii) task spec

**What is already known (companion project, SL(2,C) vertex).**

- **R5 (companion ledger):** the zero-momentum 4-tachyon contact term $\{T^4\}$ is a
  constant (symbolic there) times a strictly positive moduli integral over
  $\mathcal V_{0,4}$; the closed form and the values are from the companion SL(2,C)
  computation, not reproduced here. Since the integral is positive and the constant is
  nonzero, the Sym² direction $T\otimes T$ has a **nonvanishing diagonal element**: the
  level-0 (zero-momentum tachyon) block of $V_4|_{\operatorname{Sym}^2}$ is $1\times1$
  and invertible — the first concrete piece of the (5.1)-kernel question, now empirical.
  (Script check 5 re-derives the integral from the companion closed form and confirms
  its positivity over the range tested.)
- **R6 (companion ledger):** for external tachyons of equal mass-squared (R6's scope;
  no collapse for unequal $k_a^2$) the diagonal kernel element
  at momentum $k$ is a strictly positive integral over $\mathcal V_{0,4}$ of the
  Koba–Nielsen integrand wherever it converges, hence
  **no zero of the diagonal element at any $k$** where the integral converges. The
  momentum-space kernel of $V_4$ is nondiagonal (Fable note §5 (2.5)), so this is a
  diagonal statement only — but it rules out the simplest kernel scenario (a
  momentum-locus zero of the tachyon block).

**Sign caveat.** The overall normalisation constant is open (it depends on the
absolute-normalization chain of the companion project, O3): the *sign* of the
tachyon-diagonal element — the input needed to choose (B.3) vs (B.1) — is not yet
fixed. Strebel-scheme literature values exist
($v_4=72.39$ in Moeller's conventions) but sit in a different prescription and a
convention chain that must be fixed once; do not import them as a sign statement for
the SL(2,C) vertex.

**Task spec for (iii)** (dedicated session, computator + numerical-verifier, companion
machinery required):

1. **States.** Zero-momentum low-level basis of $\mathcal H_0$: tachyon $T$ and the
   level-$(1,1)$ massless block ($\alpha_{-1}^\mu\bar\alpha_{-1}^\nu c_1\bar c_1|0;k=0\rangle$,
   i.e. graviton/dilaton/B-field polarizations; plus the ghost-dilaton if the chosen
   basis includes it). $\operatorname{Sym}^2$ of that list.
2. **Objects.** Gram matrix $G_{IJ}=V_4(\lambda_I,\lambda_J)$ on
   $\operatorname{Sym}^2$ with the companion SL(2,C) vertex at its standard parameter
   value (and one more value for the stub-scaling cross-check
   $\beta^{2N}\times$level corrections).
3. **Hard part (why companion R1/R4 do not suffice):** for non-tachyon insertions the
   $b$-ghost measure keeps the $m\ge0$ frame-shape moments and the modular Jacobian is
   no longer $\equiv1$; all four Schiffer vectors contribute (R4 scope note).
   The integrand must be assembled from the explicit Möbius maps
   ($F_a$, in the companion notes) with the full
   $\langle\Sigma_{0,4}|b(v)\dots$ insertions — closed-form ingredients all exist in
   the companion notes; what is new is the bookkeeping and the 2D quadrature over
   $\mathcal V_{0,4}$.
4. **Deliverables.** Rank of $G$ (the (5.1) kernel-size test), its spectrum/sign
   structure (the (B.3)-vs-(B.1) input), and the $\beta$-dependence of both. Verdict
   format: Confirmed/Disputed/Inconclusive per the numerical-verifier protocol.
5. **Cheap first pass** (worth doing before the full massless block): the
   $2\times2$ block on $\{T\otimes T,\;T\otimes D\}$ where $D$ is the zero-momentum
   ghost-dilaton — the $T\otimes D$ row already exercises the $\mathcal J\neq1$
   machinery at minimal state complexity.

## 5. What this does and does not establish

**Established here (machine-checked where marked):**
- the two-gradings statement (B.2) with the $g_s$-power cross-check in contrapositive
  form — the uncoloured grading is inconsistent with the coupling expansion, the
  coloured one agrees [script checks 3–4 are arithmetic self-consistency guards of the
  stated formulas, not independent corroboration — critic iter 1];
- the unconditional Schwinger representation (B.1) for symmetric invertible $V_4$, its
  odd-chain expansion, and the sandwiched collapse (B.4) [script checks 1–2, 6];
- the conditionality of the naive form (B.3) — valid iff positive definite [script
  check 1b demonstrates the divergence of the naive real-axis form on an indefinite
  draw; the stronger "no contour rotation converges for genuinely indefinite real
  spectrum" is an analytic statement, not machine-tested — critic iter 1];
- the level-0 empirical anchor: nonvanishing tachyon-diagonal element, from the companion
  closed form re-derived in the script [check 5].

**Not established (open, routed):**
- spectrum/rank of the actual SL(2,C) $V_4$ beyond the tachyon diagonal — **(iii)**,
  specced in §4;
- the sign of the tachyon-diagonal element (open normalization constant) — with (iii);
- infinite-dimensional self-adjointness/closed-range for $V_4|_{\operatorname{Sym}^2}$
  and the canonical choice of auxiliary inner product — open regularity input,
  recorded alongside R10 route (B)'s bounded-inverse condition;
- any claim that the coloured operad composition *is* a geometric sewing operation on
  a new class of surfaces (coloured punctures) — that is Phase-6/TODO-2.1 territory,
  not touched here.
