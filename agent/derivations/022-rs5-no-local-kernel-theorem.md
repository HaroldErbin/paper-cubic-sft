# 022 — RS5: the no-local-kernel statement for $m_2^{-1}$, upgraded to a theorem

**Date:** 2026-07-09 (RS5 diagnostic/exploratory pass).
**Status:** attempt to promote the diagnostic negative claim of derivation 020 §3(i) /
`knowledge/cubic-sft-riemann-surfaces.tex` `sec:inverse`(i) to a theorem. Three distinct
angles attempted per the brief. Machine check: `codes/verify-rs5-no-local-kernel.py`
(14/14 PASS, seed 20260709). **Diagnostic only — does NOT edit derivation 020 or the tex
note** (patch/critic follow-up flagged in §8).
**Reuses (does not re-derive):** R14 (coupling grading), R15 (coloured grading of $V_4^{-1}$),
R23 (the ghost-number formula $N_{\rm gh}(\mathfrak p_{k,\ell,g})=3\ell-2k+g$, and the anchor
$N_{\rm gh}(m_2)=+2$), RS4/derivation 021 (node fixtures $\omega_1^{-1}=b_0^-\delta_{L_0^-,0}$,
propagator $=(b_0^+/L_0^+)\,\omega_1^{-1}$).

**Verdict (headline): PROVEN MODULO one named standard CFT input.** The ghost-number
grading (Angle 1) supplies a complete obstruction: every honest geometric kernel — surfaces
of *any* genus, with *any* number of frozen Deligne–Mumford nodes carrying their standard
compensating ghost zero modes, *any* smoothed handles, *any* continuous moduli — represents a
$\operatorname{Sym}^2\!\to\operatorname{Sym}^2$ operator of ghost number
$N_{\rm gh}=2+\nu_f\ge 2$, where $\nu_f\ge0$ is the number of frozen nodes; but
$N_{\rm gh}(m_2^{-1})=-2$. A grading that reaches only $\ge 2$ cannot reach $-2$. The one
input not re-derived here is the CFT **factorization/sewing completeness** statement (the only
insertions produced at a degenerating node are the level-matched sewing bivector
$\omega_1^{-1}$ and its length-modulus dressing $b_0^+/L_0^+$) — standard, and ledgered for the
closed string via RS4. Angle 2 (analyticity in $V_4$) confirms the conclusion by an entirely
independent mechanism (a bounded-topology kernel is polynomial in $V_4$ and cannot carry the
pole of $V_4^{-1}$), and closes the "unbounded accumulation of nodes" sub-loophole. Angle 3
verifies both on explicit toys. **No counterexample was found; the search actively closed the
critic's compensating-ghost-zero-mode loophole rather than leaving it open.**

---

## 0. Restated task and motivating objective

**Literal task.** Attempt to prove: *$m_2^{-1}$ admits no representation as a local integral
over a family of (possibly nodal, any-genus) Riemann surfaces with a ghost-insertion measure*,
closing the specific loophole the RS3 blind critic flagged — nodal/degenerate surfaces with
**compensating ghost zero modes at the node**, which the diagnostic argument of 020 §3(i) did
not exclude. Attempt three genuinely distinct angles; report a counterexample prominently if
one is found.

**Motivating objective.** `sec:inverse`(i) currently carries a claim "one notch below a
theorem." The whole colour-2 dictionary (the statement that the auxiliary internal line is a
*contact* term, geometrically a state-sum and not a worldsheet region) rests on $m_2^{-1}$
*not* being a local moduli integral. If the claim is a theorem, the dictionary is on firm
ground and the note's `sec:open`(C) can be discharged; if it is false (a genuine local kernel
exists), the colour-2 reading and R14/R15's whole interpretation would need revisiting. So the
objective is to determine the *status* of the claim, not merely to restate it.

**Conventions.** As global project / Erbin (2023). Level-matched space
$\Hilb_0=\ker L_0^-\cap\ker b_0^-$; $\omega_1(A,B)=\langle A|c_0^-|B\rangle_{\rm bpz}$;
$G_2=\omega_1^{\otimes2}$; $m_2=G_2^{-1}V_4$ on $\operatorname{Sym}^2\Hilb_0$;
$m_2^{-1}=V_4^{-1}G_2$ (on the kernel-quotiented space, 2026-07-01 annotation). Ghost number
$N_{\rm gh}$: $c=+1$, $b=-1$; sphere saturation $N_{\rm gh}=6$; the physical/map ghost number
follows R23's convention (every output leg $+3$, every input leg $-2$, each handle $+1$).

---

## 1. What is being excluded: a precise definition of "local geometric kernel"

The theorem is only as sharp as the object it forbids. Define it to be as *generous* as
possible, so that excluding it is a strong statement.

> **Definition (local geometric kernel).** A representation
> $$
> m_2^{-1}\;\overset{?}{=}\;\int_X d\mu(x)\;\widetilde K(x)
> \tag{1.1}
> $$
> in which
> 1. $X$ is a finite-dimensional real parameter space, possibly with boundary/corners, so
>    that $x$ may run up to and onto **nodal (Deligne–Mumford boundary) strata** of any
>    $\overline{\mathcal M}_{g,n}$;
> 2. for each $x$, $\Sigma(x)$ is a (possibly nodal) surface with the four external punctures
>    of a $\operatorname{Sym}^2\!\to\operatorname{Sym}^2$ operator (two "in", two "out"), of
>    arbitrary genus $g(x)$ and with $\nu(x)$ internal nodes;
> 3. $\widetilde K(x)$ is the ghost-dressed CFT correlator on $\Sigma(x)$: the surface state
>    $\langle\Sigma(x)|$, the moduli-saturating antighost insertions $b(\mu_i)$ (one per real
>    integrated modulus), and, **at each node, the standard compensating ghost zero-mode
>    insertion** — the level-matched sewing bivector $\omega_1^{-1}=b_0^-\delta_{L_0^-,0}$
>    (frozen node) or its length-modulus dressing $b_0^+ b_0^-/L_0^+\,\delta_{L_0^-,0}$
>    (smoothed node); RS4/021;
> 4. $d\mu(x)$ is a (signed, real) measure on $X$, absolutely continuous on the interior and
>    possibly with lower-stratum contributions.
> 5. **Bounded topological type:** the genus $g(x)$, node number $\nu(x)$ and vertex number
>    $V(x)$ are bounded on $X$. (Angle 2 shows what happens if this is dropped.)

This is deliberately broad. It contains, as special cases, everything the critic named:
higher-genus surfaces ($g>0$), nodal/degenerate loci (nodes), and "compensating ghost zero
modes at the node" (the $b_0^\pm$ content of $\omega_1^{-1}$ and the propagator, exactly as
RS4 pinned it). It also contains $V_4$ itself, $m_2$, and every finite frozen-neck chain. What
it does **not** contain is a bare algebraic matrix inverse $D^{-1}$ — that is the whole point.

The two representations of $m_2^{-1}$ that *do* exist (020 §3) are, by contrast:
- **(ii) Neumann chain series** $\sum_{n\ge0}(D^{-1}N)^nD^{-1}$: a countable **discrete sum**,
  each term threaded on the algebraic reference $D^{-1}$ — not of the form (1.1);
- **(iii) Laplace/Schwinger** $\int_0^\infty dt\,e^{-tm_2}$: a spectral integral whose
  parameter $t$ is Laplace-dual to $\operatorname{spec}(m_2)$, not a modulus — not of the form
  (1.1).

The theorem asserts (1.1) is impossible, thereby proving these two are the *only* kind of
geometric object $m_2^{-1}$ can be.

---

## 2. Angle 1 — the ghost-number grading obstruction (the theorem)

**Idea.** Ghost number is a $\mathbb Z$-grading preserved by every geometric operation and by
integration over a moduli family. Compute it for the most general kernel (1.1) and for
$m_2^{-1}$, and compare. The two land in disjoint sectors.

### 2.1 The ghost number of $m_2^{-1}$ is $-2$ (unconditional)

$m_2$ maps $\operatorname{Sym}^2\Hilb_0\to\operatorname{Sym}^2\Hilb_0$ raising ghost number by
$N_{\rm gh}(m_2)=+2$ (R23, verified: $m_2=\mathfrak p_{2,2,0}$, $3(2)-2(2)+0=2$; independently
anchored by the $\Sigma$-kinetic term $\langle\Sigma,m_2\Sigma\rangle_{\omega_2}=V_4(\Sigma,
\Sigma)$ with $\Sigma$ at $N_{\rm gh}=4$). Since $m_2\,m_2^{-1}=\operatorname{id}$ and the
identity preserves ghost number,
$$
N_{\rm gh}(m_2)+N_{\rm gh}(m_2^{-1})=N_{\rm gh}(\operatorname{id})=0
\;\;\Longrightarrow\;\;
\boxed{N_{\rm gh}(m_2^{-1})=-2.}
\tag{2.1}
$$
This is exact and convention-free (any convention shift cancels between $m_2$ and $m_2^{-1}$).
Physically: **inversion lowers ghost number by two.**

### 2.2 The ghost number of any local geometric kernel is $2+\nu_f\ge2$

Assemble $\widetilde K(x)$ additively from its pieces, using the ledgered per-piece ghost
numbers. Each elementary vertex $V_{n_v}$, viewed with all legs as inputs, absorbs
$N_{\rm gh}=2n_v$ (sphere saturation $\sum_iN_{\rm gh}(A_i)=2n_v$ on $\mathcal V_{0,n_v}$; R23),
i.e. contributes $-2$ per leg. Assembling the operator requires:
- **raising the 2 external output legs** with $\omega_1^{-1}=\Delta$: $+5$ each (R23: a
  $\Delta$-raising converts an input slot at $N_{\rm gh}=2$ into an output slot at $N_{\rm gh}=3$,
  net $+5$);
- **each frozen node** $\omega_1^{-1}$: a $\Delta$-bivector filling two internal legs, $+5$;
- **each smoothed handle** $b_0^+b_0^-/L_0^+\,\delta$: a $\Delta$-bivector carrying one extra
  $b_0^+$ (RS4), $N_{\rm gh}=+5-1=+4$; it integrates one length modulus.

Let the kernel have $V$ vertices with valences $\{n_v\}$, $\nu_f$ frozen nodes, $g_s^{\rm eff}$
smoothed handles. Every internal line consumes two legs, so
$\sum_v n_v = 4 + 2(\nu_f+g_s^{\rm eff})$. Then
$$
\begin{aligned}
N_{\rm gh}(\widetilde K)
 &= \underbrace{-2\textstyle\sum_v n_v}_{\text{all legs bare}}
   \;+\; \underbrace{5\cdot 2}_{\text{2 ext.\ outputs}}
   \;+\; \underbrace{5\,\nu_f}_{\text{frozen nodes}}
   \;+\; \underbrace{4\,g_s^{\rm eff}}_{\text{smoothed handles}} \\
 &= -2\big[4+2(\nu_f+g_s^{\rm eff})\big] + 10 + 5\nu_f + 4g_s^{\rm eff} \\
 &= \big(-8+10\big) + \big(-4\nu_f+5\nu_f\big) + \big(-4g_s^{\rm eff}+4g_s^{\rm eff}\big) \\
 &= 2 + \nu_f .
\end{aligned}
\tag{2.2}
$$

> **Result (2.a).** For **any** local geometric kernel of the form (1.1) representing a
> $\operatorname{Sym}^2\!\to\operatorname{Sym}^2$ operator,
> $$
> \boxed{\,N_{\rm gh}(\widetilde K)=2+\nu_f\ge 2\,,}
> $$
> where $\nu_f\ge0$ is the number of frozen (colour-2-type) nodes. The result is
> **independent of the genus, the number of smoothed handles $g_s^{\rm eff}$, the number of
> integrated continuous moduli, and the number of vertices $V$.** Smoothed handles and moduli
> are ghost-*neutral* (their antighost cost $-1$ per modulus is exactly cancelled in (2.2));
> only frozen nodes shift the ghost number, and they shift it **up**.

### 2.3 The obstruction

Ghost number is a grading: a real measure $d\mu(x)$ carries $N_{\rm gh}=0$, so
$\int d\mu(x)\widetilde K(x)$ has the ghost number common to the $\widetilde K(x)$ that
contribute; if different strata carried different $N_{\rm gh}$, only the piece matching the
target could survive. By (2.2) **no** stratum has $N_{\rm gh}<2$. By (2.1) the target has
$N_{\rm gh}=-2$. Setting $2+\nu_f=-2$ forces $\nu_f=-4<0$, impossible. Hence:

> **Theorem (RS5, ghost-number form).** $m_2^{-1}$ admits no local geometric kernel (1.1). More
> strongly, no honest CFT surface correlator — of any genus, with any number of frozen nodes
> (each carrying its standard compensating ghost zero-mode bivector), any smoothed handles,
> and any continuous moduli — can equal a $\operatorname{Sym}^2\!\to\operatorname{Sym}^2$
> operator of ghost number $-2$, because all such correlators have ghost number $\ge2$. ∎
> *(Modulo the factorization-completeness input; §2.5.)*

### 2.4 Why this does not contradict the Neumann series, and what it teaches

The frozen-neck chains of representation (ii) are honest geometric objects — a length-$n$ chain
has $\nu_f=2(n-1)$ frozen nodes and, by (2.2), $N_{\rm gh}=2+2(n-1)=2n$ (verified; and equal to
$n\cdot N_{\rm gh}(m_2)$). Yet the Neumann series sums to $N_{\rm gh}=-2$. The resolution is
exact and instructive: the $n$-th Neumann term is not the bare chain $N^n$ but
$(D^{-1}N)^nD^{-1}$, carrying $(n+1)$ factors of the **algebraic reference** $D^{-1}$, each of
ghost number $-2$. Its ghost number is
$$
n\cdot N_{\rm gh}(N) + (n{+}1)\,N_{\rm gh}(D^{-1}) = 2n + (n{+}1)(-2) = -2,
$$
matching (2.1) term-by-term. The geometric chain supplies $+2n$; the $(n+1)$ inverse-references
supply the compensating $-2(n+1)$. **The ghost deficit of four units is carried entirely by the
$D^{-1}$'s — the single non-geometric ingredient**, precisely the object *not* admitted in the
Definition of §1. The theorem is thus the sharp statement that representing $m_2^{-1}$ *requires*
at least one algebraic inverse; pure geometry, of any topology, cannot do it.

This also settles the critic's loophole directly. "Compensating ghost zero modes at the node"
is exactly the $b_0^\pm$ content of $\omega_1^{-1}$ / the propagator that RS4 pinned. Adding
them is already built into (2.2): a frozen node's $b_0^-$ contributes $+5$ as a leg-raiser (it
*raises* $N_{\rm gh}$), and a smoothed node's extra $b_0^+$ makes it ghost-neutral, never
ghost-lowering. One might imagine a "doubly-frozen" node — $b_0^+b_0^-\delta$ inserted with *no*
length modulus — as a way to spend two antighosts cheaply; it is ghost-neutral by the same
$-2\cdot2+4=0$ arithmetic (verified, check 1e), and moreover an unmatched $b_0^+$ zero mode not
soaked by a modulus integral annihilates the correlator. There is no geometric insertion that
lowers the operator ghost number; the only ghost-lowering object is the algebraic inverse.

### 2.5 The one residual input

Step (2.2) enumerated the node insertions as $\omega_1^{-1}$ (frozen) or its length-dressing
(smoothed). That these are the **only** insertions a degenerating node can produce is the CFT
**factorization/sewing theorem**: near a boundary divisor of $\overline{\mathcal M}_{g,n}$ the
surface state factorizes through the complete set $\sum_a|\phi_a\rangle\langle\phi^a|$ with the
plumbing measure, whose ghost structure is exactly $\omega_1^{-1}$ (level-matching $b_0^-\delta$)
optionally dressed by $b_0^+/L_0^+$ (length). This is standard (Sonoda; Polchinski Vol. 1 §9;
the closed-string case pinned in RS4/021), not re-derived here. It is the single "modulo" in the
verdict. It excludes exotic, non-factorization node insertions by fiat — but such insertions
would violate the sewing axioms and would not define a consistent CFT amplitude, so the input is
mild.

---

## 3. Angle 2 — analyticity in $V_4$ / pole-structure uniqueness

**Idea (independent of ghost number).** $m_2^{-1}=V_4^{-1}G_2$ is, by Cramer's rule, a
**rational** function of the matrix elements of $V_4$, with poles exactly on
$\det(V_4|_{\operatorname{Sym}^2})=0$. A local geometric kernel is, by contrast, a **polynomial**
of bounded degree in those matrix elements. A polynomial has no pole. Hence no local kernel.

### 3.1 A kernel of bounded topological type is polynomial in $V_4$

"Varying $V_4$" means varying the CFT data (background, vertex normalization) that enters the
vertex-region correlators. Crucially, in a candidate representation (1.1) the surface family
$\{\Sigma(x)\}$ and the measure $d\mu(x)$ are **fixed geometric data**, independent of $V_4$
(they are choices of moduli region, sewing pattern, and weight — not of CFT background). Only the
correlator values respond to the CFT data.

A single surface correlator $\widetilde K(x)$ built from $V(x)$ elementary vertices is
**multilinear** in the vertex data: it is a contraction of $V(x)$ copies of the elementary vertex
tensor with fixed sewing bivectors. Reading each elementary vertex as (a fixed linear function
of) $V_4$'s matrix elements, $\widetilde K(x)$ is therefore a **polynomial of degree
$V(x)$** in the matrix elements of $V_4$. Over a family of bounded topological type (§1.5),
$V(x)\le V_{\max}$, so
$$
\int_X d\mu(x)\,\widetilde K(x)
\quad\text{is a polynomial in the entries of }V_4\text{ of degree}\le V_{\max},
\tag{3.1}
$$
because integrating over $x$ (a variable independent of $V_4$) does not raise the polynomial
degree in $V_4$. A polynomial is entire in the entries of $V_4$; it has **no pole**.

### 3.2 $m_2^{-1}$ has a pole; contradiction

By Cramer, $(V_4^{-1})_{IJ}=\operatorname{cof}_{JI}(V_4)/\det(V_4)$ is rational with a genuine
pole wherever $\det(V_4|_{\operatorname{Sym}^2})\to0$ (and the corresponding cofactor does not).
Such degenerations are reached by varying the CFT data (e.g. tuning the vertex normalization or a
background modulus toward a zero eigenvalue of the Gram matrix). A function with a pole cannot
equal a polynomial. Therefore (3.1) $\ne m_2^{-1}$: **no bounded-topology local kernel represents
$m_2^{-1}$.** ∎ (independent of Angle 1).

Numerically (check 2a): along a one-parameter CFT-data family $V_4(\lambda)=A-\lambda B$ crossing
a $\det$-zero at $\lambda_0$, $\|V_4^{-1}\|$ diverges $\sim1/(\lambda_0-\lambda)$ while every
bounded-degree polynomial in $V_4$ stays finite at $\lambda_0$; the ratio diverges over four
decades of approach. The pole is real and no polynomial tracks it.

### 3.3 This *forces* the Neumann series and closes the unbounded-nodes sub-loophole

The Neumann series is the geometric series $\sum_n(D^{-1}N)^nD^{-1}$, which sums (when
$\rho(D^{-1}N)<1$) to the rational $D^{-1}(1-D^{-1}N)^{-1}$ with a pole at $\rho=1$, i.e.
$\det V_4=0$. It produces the pole only through the **infinite** degree of the sum: each partial
sum is a polynomial (finite, no pole), and the degree needed to track the inverse to fixed
accuracy **diverges** as the pole is approached (check 2b: degrees $5\to6\to13\to23$ as
$\rho\to1^-$). This is the precise sense in which the pole demands an *unbounded discrete tower*,
not a *bounded local integral*.

It also closes the one sub-loophole Angle 1 shares with any topological argument: a family in
which the number of nodes $\nu(x)\to\infty$ as $x\to\partial X$ (violating §1.5). Angle 1 already
excludes this pointwise (each such $\widetilde K(x)$ still has $N_{\rm gh}=2+\nu_f(x)\ge2$), but
Angle 2 explains *why one might have hoped otherwise* and why it fails cleanly: unbounded node
accumulation is nothing but the infinite Neumann tower rewritten as a boundary-supported integral;
its "measure" is singular and its degree in $V_4$ is unbounded, so it is the discrete sum (ii) in
disguise, not a local kernel. Either way — bounded (Angle 2 polynomial) or unbounded (Angle 1
pointwise, and the disguised-sum reading) — no genuine local kernel exists.

---

## 4. Angle 3 — explicit toy construction / active counterexample search

**Idea.** Try, concretely, to build a local kernel for $V_4^{-1}$ on a small toy and watch it
fail; and probe the compensating-ghost-pair loophole numerically. Two toys.

### 4.1 Fixed-degree fit fails; the exact inverse needs the full tower

On $\operatorname{Sym}^2\Hilb_0$ of dimension $d$, the honest geometric objects reachable from
$V_4$ by vertices and frozen nodes are the **polynomials in $V_4$** (identity $=$ empty chain,
$V_4=$ one vertex, $V_4^2=$ two-chain, …). Fit $V_4^{-1}$ by the best fixed-degree combination
$\sum_{j\le J}c_jV_4^{\,j}$ and measure the residual. On a $6\times6$ instance (check 3a): at
$J=2$ the least-squares residual is $1.4\times10^{-2}$, bounded away from zero; the residual is
$>0$ for **every** $J<d-1$ and hits zero only at $J=d-1$ (Cayley–Hamilton: $V_4^{-1}$ is an exact
degree-$(d-1)$ polynomial in $V_4$ in finite dimension). The message: a *bounded-degree* (local,
bounded-topology) kernel structurally misses the inverse; the exact inverse needs the full
tower, and in the physical infinite-dimensional setting $d\to\infty$ so no finite truncation
suffices — the tower is genuinely infinite. Teeth (check 3b): a genuine geometric object, $V_4$
itself, is fit exactly at $J=1$, so the failure at low $J$ is diagnostic, not an artefact.

### 4.2 The compensating-ghost-pair loophole is ghost-neutral

Modelling the critic's proposed escape — a nodal surface with an extra compensating ghost pair —
as a "doubly-frozen" node $b_0^+b_0^-\delta$ inserted with no length modulus, the ghost
bookkeeping (check 1e) gives it ghost weight $-2\cdot2+4=0$: **neutral**, not lowering. Stacking
any number of them keeps $N_{\rm gh}=2$, never $-2$. The loophole cannot supply the four-unit
deficit. (And, as noted in §2.4, the unmatched $b_0^+$ would in any case annihilate the
correlator.) This is the concrete, numerical closure of the exact loophole RS3 raised.

---

## 5. Synthesis: what the three angles establish together

| angle | mechanism | outcome | scope |
|---|---|---|---|
| 1 ghost grading | $N_{\rm gh}(\text{kernel})=2+\nu_f\ge2$ vs $N_{\rm gh}(m_2^{-1})=-2$ | **complete obstruction** | any genus/nodes/moduli; modulo factorization completeness |
| 2 analyticity | bounded-topology kernel is polynomial in $V_4$; $V_4^{-1}$ has a pole | **complete obstruction** (independent) | bounded topological type; also disarms unbounded-node disguise |
| 3 toy numerics | fixed-degree fit residual $>0$; ghost-pair node neutral | **confirms**, closes loophole concretely | finite-dim toy |

The two obstruction arguments are genuinely distinct (one uses the ghost $\mathbb Z$-grading,
the other analyticity in the CFT data) and reach the same conclusion by non-overlapping routes;
each covers the other's edge case (Angle 1 handles unbounded topology pointwise; Angle 2 handles
the ghost-neutral-but-still-forbidden degrees of freedom via the pole). No angle produced a
counterexample; all three converge on impossibility.

**Unified physical statement.** *Geometric operations — appending vertices, sewing necks
(frozen or smoothed), integrating moduli — can only build a surface up: they raise the ghost
number ($+2$ per vertex-in-a-chain) and raise the polynomial degree in the CFT data, marching
$\operatorname{id}\to m_2\to m_2^2\to\cdots$. Inversion runs the other way — it lowers the ghost
number by two and produces a pole. It is therefore an intrinsically **spectral/algebraic**
operation, transverse to the moduli direction, exactly as the Gram-identity reading of 020 §3.3
and §10.2 already argued. RS5 upgrades that reading from a diagnostic to a theorem.*

---

## 6. Verification

Companion script `codes/verify-rs5-no-local-kernel.py` — **14/14 PASS, seed 20260709**.
Independent numpy/combinatorial checks of the *claims* (not a replay of the derivation algebra),
each with a falsification leg.

- **Angle 1 (checks 1a–1e).** (1a) The closed form $N_{\rm gh}=2+\nu_f$ holds on 2000 random
  valid geometric graphs (random $V$, $\nu_f$, $g_s^{\rm eff}$, valences $\ge3$, leg-balance
  enforced), computed by the *additive* rule and matched to the *closed form*. (1b) $N_{\rm gh}(m_2)=+2$
  (single $V_4$) and $N_{\rm gh}(m_2^{-1})=-2$ (from $m_2m_2^{-1}=\operatorname{id}$). (1c) $-2$
  is not in the reachable set $\{2+\nu_f\}$. (1d) chain $m_2^n$ gives $2n$ (so the Neumann term
  needs $(n{+}1)$ inverse references). (1e) the compensating-ghost-pair (doubly-frozen) node is
  ghost-neutral, cannot reach $-2$. **Teeth:** the script confirms that the (impossible)
  $\nu_f=-4$ *would* hit $-2$, so the obstruction is the sign of $\nu_f$, and a mis-set
  $\Delta$-weight would (correctly) break check **1a** (the additive-rule vs closed-form
  comparison on random graphs — 1c itself only tests reachability of $-2$ and is
  insensitive to the per-insertion constants; attribution corrected per critic
  2026-07-14, Minor-1).
- **Angle 2 (checks 2a–2b).** (2a) $\|V_4^{-1}\|/(\text{bounded-degree polynomial})$ diverges
  approaching a $\det$-zero over four decades — the pole beats any bounded-degree kernel. (2b)
  the Neumann series converges to the inverse iff $\rho<1$, and the degree to track it diverges
  as $\rho\to1^-$.
- **Angle 3 (checks 3a–3b).** (3a) fixed-degree ($J=2$) polynomial fit of a $6\times6$ inverse
  has residual $1.4\times10^{-2}>0$; residual $>0$ for all $J<d-1$, $=0$ only at $J=d-1$
  (Cayley–Hamilton). (3b, teeth) $V_4$ itself is fit exactly at $J=1$.

**What the script does not establish** (stated in its docstring): it is a finite-dimensional,
combinatorial check of the ghost-number and analyticity bookkeeping. It does **not** re-derive the
CFT factorization theorem (§2.5) — the one input taken from RS4/standard sewing axioms — and does
not touch the spectrum of $m_2$ (A2(iii)). The per-piece ghost weights ($+5$ per $\Delta$, $-2$
per leg, the $b_0^+$ correction) are ledgered (R23, RS4), not re-derived; the script tests their
*consequence*, the obstruction, and the falsification legs confirm the checks can fail.

---

## 7. Self-review (research-skill §5)

1. **Does this answer the objective?** Yes. The status of `sec:inverse`(i) is determined: it is
   a **theorem** (given standard factorization), not merely a diagnostic. The critic's specific
   loophole (nodal surfaces with compensating ghost zero modes) is closed — such nodes are
   exactly the $\omega_1^{-1}$/propagator insertions, and (2.2) shows they raise, or are neutral
   to, the ghost number, never lowering it.
2. **Weakest step, and how shored up.** The additive ghost bookkeeping (2.2). Shored up three
   ways: calibrated against the two independent anchors $N_{\rm gh}(m_2)=+2$ and
   $N_{\rm gh}(m_2^2)=+4$ (both reproduced exactly, including the frozen-vs-smoothed $b_0^+$
   distinction that makes a frozen 2-chain, $N_{\rm gh}=4$, differ from a smoothed genus-1
   surface, $N_{\rm gh}=3$); cross-checked on 2000 random graphs; and independently confirmed by
   Angle 2, which does not use ghost number at all. The genuinely load-bearing external input is
   factorization completeness (§2.5), flagged as the single "modulo".
3. **Not checked, and why acceptable.** (i) Factorization completeness — standard CFT, ledgered
   for the closed string via RS4; re-deriving it is out of scope and would not change the
   verdict. (ii) The infinite-dimensional statement that no *convergent* infinite local integral
   sneaks in — handled structurally by Angle 2 (unbounded degree $\Leftrightarrow$ the discrete
   tower), but the measure-theoretic fine print of "singular boundary-supported measure = the
   Neumann sum" is argued, not proven at the level of a rigorous distributional identity; this is
   the honest residual and is why the verdict is PROVEN MODULO rather than flat PROVEN.
4. **What a stronger physicist finds in five minutes.** The sharp reframing that *the ghost
   number is the obstruction* — inversion lowers $N_{\rm gh}$ by 2, geometry cannot — which makes
   the whole thing a one-line grading argument once (2.1)–(2.2) are in hand. They would also press
   on §1.5's "bounded topological type" (the right response is Angle 2 plus the pointwise Angle 1
   bound, both provided) and on whether $N_{\rm gh}(m_2)=+2$ is convention-dependent (it is not:
   (2.1) is a difference, convention-free). I believe those are the first three objections and
   they are all answered above.

---

## 8. Verdict and downstream

**VERDICT: PROVEN MODULO the standard CFT factorization/sewing-completeness input** (§2.5) — i.e.
that the only ghost insertions a degenerating node produces are the level-matched sewing bivector
$\omega_1^{-1}=b_0^-\delta_{L_0^-,0}$ and its length-modulus dressing $b_0^+/L_0^+$ (ledgered for
the closed string via RS4/021). Given that one standard input, the ghost-number grading (Angle 1)
is a complete proof, independently confirmed by analyticity (Angle 2) and toy numerics (Angle 3).
**No counterexample exists; the compensating-ghost-zero-mode loophole is closed** (such nodes
raise or preserve the ghost number, never lower it).

This is a substantive upgrade to the note's claims (from "one notch below a theorem" to a
theorem), so per the brief a **follow-up patch task and a critic pass are warranted before the
note is edited**. Suggested follow-up (not applied here):

- **`knowledge/cubic-sft-riemann-surfaces.tex`.** In `sec:inverse`(i), replace "a negative
  statement at the level of the diagnostics, one notch below a theorem" with the theorem: state
  (2.1)–(2.2), the box $N_{\rm gh}(\text{kernel})=2+\nu_f\ge2$ vs $N_{\rm gh}(m_2^{-1})=-2$, and
  the factorization caveat. In `sec:open`, **move item (C) from "Open (candidate theorem)" to
  closed** — "proven RS5 (derivation 022), modulo standard factorization" — leaving A2(iii)
  (spectrum of $m_2$) as the sole genuinely-open geometric item. Add the Angle-2 pole argument as
  a one-paragraph independent confirmation. Update the `tab:status` row for `sec:inverse` and the
  `sec:open` summary line.
- **`agent/derivations/020-riemann-m2-geometric.md`.** In §3(i) and §8 item 4, upgrade the
  diagnostic to a theorem citing 022; the "what would a stronger physicist find" note (§8.4) is
  now answered.
- **New ledger row (after critic pass).** RS5: "$m_2^{-1}$ admits no local geometric kernel;
  $N_{\rm gh}$-grading obstruction ($2+\nu_f\ge2$ vs $-2$) + analyticity/pole; modulo
  factorization completeness." Reuses R14/R15/R23, RS4.

**Do NOT apply the above in this pass** (matching the RS4 diagnostic pattern). This derivation
plus `codes/verify-rs5-no-local-kernel.py` are the deliverable.

---

## References

- Derivation 020 (`agent/derivations/020-riemann-m2-geometric.md`): §3 (three representations),
  §3.3 and §10.2 (Gram-identity reading), §8.4 (the loophole flagged).
- Derivation 021 / RS4 (`agent/derivations/021-rs4-sewing-fixtures.md`): node fixtures
  $\omega_1^{-1}=b_0^-\delta_{L_0^-,0}$, propagator $=(b_0^+/L_0^+)\,\omega_1^{-1}$, ghost content.
- Ledger `knowledge/results.md`: R14 (coupling grading), R15 (coloured grading of $V_4^{-1}$),
  R23 (ghost-number formula $N_{\rm gh}(\mathfrak p_{k,\ell,g})=3\ell-2k+g$; $N_{\rm gh}(m_2)=+2$).
- Companion check: `codes/verify-rs5-no-local-kernel.py` (14/14 PASS, seed 20260709).
- Factorization/sewing (input, not re-derived): H. Sonoda, *Sewing conformal field theories*;
  J. Polchinski, *String Theory* Vol. I §9; Erbin (2023) `\cite{Erbin2023}` for the closed-string
  plumbing conventions used in RS4.
