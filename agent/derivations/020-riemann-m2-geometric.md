# 020 — The Riemann-surface meaning of $m_2^{-1}$, coloured gluing, and the $\Sigma_k$ tower

**Date:** 2026-07-09 (Fable session; Riemann-surface directive, points 2–5).
**Status:** conceptual core, derived by hand this session; machine checks = RS1 (spec in §9);
critic pass = RS3. Reuses (does not re-derive) R14, R15, R16, R23, R26 and the H2-closure
annotation of `knowledge/results.md`.
**Supersedes:** the geometric §5–§7 of `knowledge/cubic-sft-riemann-surfaces.tex`
(Phase 6): the "bounded-length plumbing neck with the full complex modulus" picture of the
$\Sigma$-channel is **wrong for the HS action** — it transposed the open-stub mechanism
(R3), whose auxiliary kinetic operator is built from $e^{-2\lambda L_0}$. In $S_{\rm HS}$
the $\Sigma$ kinetic operator is $V_4$ itself, and R14/R15 establish that the colour-2
edge carries **no modulus**. The old picture must be deleted, not patched (task RS2).

**Objective (restated task).** The literal task: define $m_2^{-1}$ in terms
of Riemann surfaces; explain how gluing two $V_4(\Sigma,\Psi^{\otimes2})$ vertices through
$1/m_2$ "cancels the moduli" of one $V_4$; explain the three-channel covering; explain the
"contact, not worldsheet" statement with an analogy to Witten's open-string product and
the analytic-solution ($KBc$) technology; explain how a colour-2 edge glues two pairs of
punctures without raising the genus; extend to the $\Sigma_k$ tower. The motivating
objective: a Riemann-surface/CFT dictionary precise enough that every operation of the
cubic theory is expressed as (i) a gluing prescription on coordinate patches and (ii) a
CFT-data formula — so the geometric side of the paper can be written with formulas, not
words.

---

## 0. Conventions and the two objects that must never be conflated

Level-matched space $\Hilb_0=\ker L_0^-\cap\ker b_0^-$; physical ghost grading
$\epsilon=N_{\rm gh}\bmod 2$; $\omega_1(A,B)=\langle A|c_0^-|B\rangle_{\rm bpz}$;
$G_2=\omega_1^{\otimes2}$ (graded symmetric, R7); $m_2=G_2^{-1}\circ V_4$ on
$\operatorname{Sym}^2\Hilb_0$ (R9). Basis $\{\phi_a\}$ of $\Hilb_0$, dual $\{\phi^a\}$
with $\omega_1(\phi^a,\phi_b)=\delta^a_b$.

The quartic vertex is an integral over the elementary vertex region
$\mathcal V_{0,4}\subset\mathcal M_{0,4}$ ($\dim_{\mathbb R}=2$) of fixed-surface
correlators:

$$
V_4(A_1,\dots,A_4)\;=\;\int_{\mathcal V_{0,4}} d^2m\;
\big\langle \Sigma_{0,4}(m)\big|\,b(v_m)\,b(\bar v_m)\,
\big|A_1\big\rangle\otimes\cdots\otimes\big|A_4\big\rangle ,
\tag{0.1}
$$

with $\langle\Sigma_{0,4}(m)|$ the 4-punctured-sphere surface state with its local
coordinates, and one $b$-insertion per real modulus. Two selection rules used throughout:

- **Ghost saturation.** A sphere correlator needs total $N_{\rm gh}=6$; each $b$ costs
  $-1$; so $V_{0,n}$ on its region ($\dim_{\mathbb R}=2(n-3)$) is nonzero iff
  $\sum_i N_{\rm gh}(A_i)=6+2(n-3)$. Every elementary vertex of the construction
  saturates identically: $V_4(\Sigma,\Sigma)$: $4{+}4-2=6$; $V_4(\Sigma,\Psi,\Psi)$:
  $4{+}2{+}2-2=6$; $\tilde V_{2k}(\Sigma_k,\Sigma_k)$: $2k{+}2k-2(2k-3)=6$;
  $\tilde V_{2k+1}(\Sigma_k,\Sigma_k,\Psi)$: $4k{+}2-2(2k-2)=6$. **One $b$ per real
  modulus is the sharp diagnostic for "is this parameter a modulus".**
- **Coupling grading.** $g_s^{n-2}$ per $n$-point elementary vertex, $g_s^{-2}\,$…
  none per propagator in the normalisation of R14.

The two objects:

1. **The worldsheet sewing kernel** (colour-1 internal line). Between two surface states,
   insert
   $$
   \mathsf P \;=\; \int_0^\infty\! ds\int_0^{2\pi}\!\frac{d\theta}{2\pi}\;
   b_0^+\,b_0^-\;e^{-sL_0^+ + i\theta L_0^-}
   \;=\;\frac{b_0^+ b_0^-}{L_0^+}\,\delta_{L_0^-,0}
   \;=\;\frac{b_0^+}{L_0^+}\,\omega_1^{-1}
   \tag{0.2}
   $$
   (normalisation **verified exact** against Erbin's book, `bsft:eq:propagator-fixed` /
   `bos:eq:offshell-prop-bpm` — task RS4, derivation 021; the factorised form isolates
   the length-modulus factor $b_0^+/L_0^+$ from the level-matching sewing measure
   $\omega_1^{-1}=b_0^-\delta_{L_0^-,0}$, see §1). The operator
   $e^{-sL_0^+}$ **is** a surface: the CFT path integral on a flat cylinder of length
   $s$, twist $\theta$. Each $(s,\theta)$ is a *different surface*; the double integral
   sweeps a 2-real-parameter family in moduli space; correspondingly there are exactly
   two $b$-insertions. This is how the $s,t,u$ Feynman channels cover
   $\mathcal M_{s},\mathcal M_t,\mathcal M_u\subset\mathcal M_{0,4}$.

2. **The colour-2 contraction** (colour-2 internal edge). Between two
   $V_4(\cdot\,;\Psi\Psi)$ vertices, insert the *state-space* kernel
   $$
   \mathsf S \;=\;\frac{12}{g_s^2}\,\big(V_4|_{\operatorname{Sym}^2}\big)^{-1}
   \;=\;\frac{12}{g_s^2}\,m_2^{-1}\,G_2^{-1}
   \tag{0.3}
   $$
   (R14). **No $q$, no $s$-integral, no length-modulus insertion $b_0^+/L_0^+$, no
   $L_0^+$** (the level-matching sewing measure $b_0^-\delta_{L_0^-,0}$ *per strand* is
   retained — see §1's corrected (1.a); it is not a length modulus). It is an inverse of
   an *already moduli-integrated* object. Everything below unpacks what that means
   geometrically.

---

## 1. What a single colour-2 contraction is: frozen-neck sewing

Before inverting anything, ask what the *bare* contraction $G_2^{-1}$ (two $\omega_1^{-1}$
bivectors) does between two surface states. The sewing theorem says: inserting a complete
set of states $\sum_a|\phi_a\rangle\langle\phi^a|$ at a pair of punctures, with the
plumbing weight $q^{L_0}\bar q^{\bar L_0}$, glues the two surfaces into one with neck
parameter $q$; integrating $q$ with the $b$-ghost measure produces the family (0.2).
Dropping the length-modulus weight ($s$ **fixed at $0$**, i.e. $|q|=1$, no
$s$-integration, no $b_0^+$) still glues the surfaces — but into a **single point** of
the bigger moduli space, not a family. **Verified against the primary source
(task RS4, derivation 021):** the sum $\sum_a|\phi_a\rangle\langle\phi^a|$, with the
$\omega_1$-dual $\langle\phi^a|$, is *exactly* the bivector
$\omega_1^{-1}=b_0^-\delta_{L_0^-,0}$ — since $\omega_1(A,B)=\langle A|c_0^-|B\rangle$
and $\{c_0^-,b_0^-\}=1$ on $\ker b_0^-$, so $b_0^-c_0^-=\mathrm{id}$ there. This retains
**one** $b$-ghost ($b_0^-$) plus the level-matching projector; what is genuinely dropped
relative to the full propagator (0.2) is only the length-modulus factor $b_0^+/L_0^+$.
So:

> **(1.a)** One $\omega_1^{-1}=b_0^-\delta_{L_0^-,0}$ contraction between two punctures is
> plumbing with the **length** modulus frozen (no $b_0^+/L_0^+$, no $s$-integral),
> retaining the level-matching sewing measure $b_0^-\delta_{L_0^-,0}$: a legitimate CFT
> surface, of measure zero in its moduli space. **Verified-against-primary-source**
> (derivation 021, cross-checked two independent ways — operator factorisation of
> Erbin's $K\Delta=1$ and explicit ghost zero-mode matrices — plus a 27/27-PASS
> companion script). The earlier phrasing "no $b$-ghost insertion" was imprecise: the
> discriminant between a colour-1 (propagating) and colour-2 (contact) line is the
> *length*-modulus $b_0^+/L_0^+$, not the presence of any $b$-ghost at all — the
> level-matching $b_0^-\delta_{L_0^-,0}$ is common to both and is not a length modulus.
> Remaining open item on this front: (iii) of derivation 021 — $|q|=1$ sewing for the
> *stubbed* vertex local coordinates converges via the stub's $e^{-\frac{s_0}2 L_0^+}$
> suppression at an effective neck $s_0>0$, consistent-with the book's plumbing range,
> not independently re-derived from scratch here.

A colour-2 edge is **two** simultaneous $\omega_1^{-1}$ contractions. Gluing two
4-punctured spheres over two puncture pairs: $\chi$ is additive under sewing
(two 4-punctured spheres: $\chi=-2-2=-4$; result has $n_{\rm ext}=4$, so
$-4=2-2g-4$), hence

$$
g = 1 .
\tag{1.1}
$$

So the *resolved* surface behind one colour-2 edge is a **genus-one** surface at a frozen
point of its neck moduli. For a chain of $k$ vertices and $k-1$ colour-2 edges:
$\chi=-2k$, $n_{\rm ext}=4$, so $g=k-1$ — this is R15's two-gradings statement, now with
its surface identified: the chain $m_2^{\,k-1}$-type composite *is* a family of
genus-$(k-1)$ surfaces whose only unfrozen moduli are the $k$ vertex-region moduli
$m_1,\dots,m_k$ ($k$ complex out of $\dim_{\mathbb C}\mathcal M_{k-1,4}=3k-2$: a
measure-zero slice for $k\ge2$).

**Why this genus is *formal* (R15, sharpened).** Three independent physical gradings all
follow the *coloured* graph (edge = one edge), not the resolved surface:

| grading | resolved-surface prediction (chain of $k$) | actual (R14 rules) |
|---|---|---|
| coupling | $g_s^{2g+2}=g_s^{2k}$ at genus $g=k-1$ (with the external normalisation absorbed) — relative $g_s^{2(k-1)}$ suppression | uniform $g_s^{2}$: $k$ vertices $\times\, g_s^2$, $(k{-}1)$ propagators $\times\, g_s^{-2}$ |
| moduli / $b$-count | $2(3k-2)$ real moduli, $2(3k-2)$ $b$'s | $2k$ real moduli ($k$ vertex regions), $2k$ $b$'s; the $2(2k-2)$ neck moduli and their $b$'s are absent |
| $N_{\rm gh}$ | — | R23: $N_{\rm gh}(p_{k,\ell,g})=3\ell-2k+g$ consistently on the coloured tree |

This is exactly the 't Hooft double-line situation run in reverse: the resolved
("ribbon") genus exists as Euler-characteristic bookkeeping, but there is **no coupling
attached to it** because the neck moduli are never integrated — the handle is frozen, so
the amplitude never *pays* for it. The physical expansion parameter organises coloured
graphs, and in the coloured grading the chain is a **tree** ($L_c=E-V+1=0$).

---

## 2. $m_2$ as an integral operator, and $m_2^n$ as a discrete surface family

Raise the indices of (0.1): $m_2=G_2^{-1}V_4:\operatorname{Sym}^2\Hilb_0\to
\operatorname{Sym}^2\Hilb_0$ is the integral operator

$$
m_2 \;=\; \int_{\mathcal V_{0,4}} d^2m\; K(m),
\qquad
K(m) \;=\; \big(\omega_1^{-1}\otimes\omega_1^{-1}\big)\,
\big\langle\Sigma_{0,4}(m)\big|\,b\,\bar b ,
\tag{2.1}
$$

i.e. one fixed surface per moduli point, indices raised by the frozen-neck bivectors.
Composition uses (1.a): the product of two such operators is the frozen-neck gluing of
their surfaces,

$$
m_2^2=\int_{\mathcal V}\!\!\int_{\mathcal V} d^2m\,d^2m'\;K(m)K(m'),
\qquad
K(m)K(m') \;=\; \big[\text{genus-1 frozen-neck surface } \Sigma(m)\#_{q=1}\Sigma(m')\big]^{\sharp},
\tag{2.2}
$$

and generally $m_2^n$ = the integral over the $n$ vertex moduli of the genus-$(n-1)$
frozen-neck chain. **Key structural fact:**

> **(2.a)** $\{m_2^n\}_{n\ge0}$ is a *discrete* semigroup of (families of) surfaces,
> graded by chain length $n$, with $m_2^n m_2^{n'}=m_2^{n+n'}$ realised by frozen-neck
> concatenation. Contrast $\{e^{-sL_0^+}\}_{s\ge0}$: a *continuous* semigroup, graded by
> cylinder length, $s+s'$ realised by cylinder concatenation.

This is the precise content of "contact term": $L_0^+$ is the **generator** of a
geometric flow (each instant of Schwinger time deforms the surface), while $m_2$ is a
**finished surface** (each application appends one complete, already-integrated vertex
region through a rigid neck). There is no operator whose exponential flow generates
$\mathcal V_{0,4}$ from a point — the vertex region is an input of the construction, not
an orbit.

Consequently, in $e^{-t m_2}=\sum_n \frac{(-t)^n}{n!}m_2^n$ the parameter $t$ multiplies
*fixed* chains by scalar weights: varying $t$ re-weights the discrete family and deforms
no geometry. $t$ is Laplace-dual to $\operatorname{spec}(m_2)$ (interaction data), $s$ is
Laplace-dual to $\operatorname{spec}(L_0^+)$ (worldsheet energies). And the $b$-ghost
diagnostic (RS4-sharpened): the $s$-integral carries an *additional*, length-modulus
$b_0^+$ on top of whatever $b_0^-\delta_{L_0^-,0}$'s the sewn strands already carry;
varying $t$ inserts no *new* $b$ beyond the fixed $b_0^-$'s already built into each
$m_2$ factor (§1) — if $t$ were a length modulus, the ghost saturation of §0 would fail
by one unit on every $\Sigma$-exchange.

---

## 3. Three representations of $m_2^{-1}$, and what each means in surfaces

$m_2^{-1}$ exists iff $\ker V_4|_{\operatorname{Sym}^2}=0$ (R9; defused-as-blocker by the
2026-07-01 annotation: quotient by the kernel). Three ways to *present* it:

**(i) Gram inverse (the definition — no surface).** In a basis of
$\operatorname{Sym}^2\Hilb_0$, $(V_4)_{IJ}$ is a Gram-type matrix of vertex-region
integrals and $m_2^{-1}=(V_4)^{-1}G_2$ is its matrix inverse. Inversion is a *global
spectral operation*: it does not commute with the moduli integral in (2.1), and there is
no kernel $\tilde K(m)$ with $m_2^{-1}=\int d^2m\,\tilde K(m)$ over any moduli region.
**$m_2^{-1}$ is not a surface, nor an integral over surfaces with a local measure.**
*(Upgraded 2026-07-09, task RS5, derivation 022: now a THEOREM modulo the standard CFT
factorization/sewing-completeness input.)* Any local geometric kernel — any genus, any
number of frozen or smoothed nodes with their standard compensating ghost insertions,
any continuous moduli — has $N_{\rm gh}=2+\nu_f\ge2$ (022 eq. 2.2), while
$N_{\rm gh}(m_2^{-1})=-2$ unconditionally (R23 + $m_2m_2^{-1}=\mathrm{id}$, 022 eq. 2.1);
independently confirmed by analyticity (a bounded-topology kernel is polynomial in
$V_4$'s matrix elements; $m_2^{-1}=V_4^{-1}G_2$ has a pole at $\det V_4=0$). The Neumann
series (3.1) is reconciled term by term: its ghost deficit is carried entirely by the
$(n{+}1)$ non-geometric $D^{-1}$ factors. The original diagnostic version (any such
representation would carry $b$-insertions and $g_s$-weights that the exchange amplitude
demonstrably does not have, §1 table) survives as the intuition behind the proof.

**(ii) Neumann chain series (the surface representation — discrete, scheme-dependent).**
Split $m_2=D-N$ with $D$ an invertible reference (e.g. the level-diagonal part of
$V_4$ read through $G_2$). Then

$$
m_2^{-1}\;=\;\sum_{n\ge0}\,(D^{-1}N)^n\,D^{-1},
\qquad\text{convergent iff }\rho(D^{-1}N)<1 .
\tag{3.1}
$$

Each term is a **chain of $n$ frozen-neck surfaces** (the $N$-insertions) threaded on the
reference $D^{-1}$. This is the honest answer to "define $m_2^{-1}$ in terms of Riemann
surfaces": *a convergent weighted **sum** over the discrete family of frozen-neck chains,
not an integral over a continuous moduli family.* The reference split $D$ is a choice
(like a subtraction scheme); the sum, when convergent, is not.

**(iii) Laplace/Schwinger (spectral — conditions attached, R15).** If
$\operatorname{spec}(m_2)\subset\{\Re>0\}$ (an inner-product-dependent statement, open at
CFT level = A2(iii)):

$$
m_2^{-1}=\int_0^\infty dt\; e^{-t m_2};
\qquad\text{unconditionally (symmetric invertible): } 
m_2^{-1}=\int_0^\infty dt\; m_2\,e^{-t m_2^2}.
\tag{3.2}
$$

The integrand at fixed $t$ is a resummed generating function of chains; **the Laplace
integral does not commute with the chain expansion** ($\int_0^\infty t^n dt$ diverges
termwise) — so (3.2) does *not* provide a term-by-term surface expansion; (3.1) does.
The $t$-parameter is spectral, exactly as in §2.

**The "moduli cancellation" is the Gram identity, not a pointwise
statement.** The telescoping

$$
V_4\circ m_2^{-1}G_2^{-1}\circ V_4
\;=\;
\int_{\mathcal V}\!\!\int_{\mathcal V} d^2m\, d^2m'\;
\big\langle\Sigma(m)\big|b\bar b\;\big[\mathsf S\big]\;\big\langle\Sigma(m')\big|b\bar b
\;=\;
\int_{\mathcal V} d^2m\;\big\langle\Sigma(m)\big|b\bar b
\tag{3.3}
$$

holds only after **both** moduli integrals **and** the intermediate two-string state sum
are performed — it is $\sum_{K} G_{IK}(G^{-1})^{KL}G_{LJ}=G_{IJ}$ with $G$ the Gram
operator. No point of $\mathcal V\times\mathcal V$ is mapped to a point of
$\mathcal V$; there is no local map of coordinate patches realising (3.3). The
cancellation of "one $V_4$'s worth of moduli" ($4\to2$ real) happens in the state-space
(spectral) direction, transverse to the moduli direction. This is the sharp reason all
earlier attempts to find a *worldsheet locus* implementing $m_2^{-1}$ failed: there is
none to find.

---

## 4. The three channels: combinatorial covering, not geometric covering

Feynman rules of $S_{\rm HS}$ (R14): $\Sigma$-propagator $\frac{12}{g_s^2}V_4^{-1}$,
vertex $\frac{g_s^2}{6}V_4(\cdot\,,\Psi_i\otimes\Psi_j)$. The 4-point $\Sigma$-exchange
with distinct externals sums over the **3 perfect matchings** $\{12|34\},\{13|24\},
\{14|23\}$; each channel telescopes *individually*:

$$
\frac{g_s^2}{6}\,V_4(\Psi_i\Psi_j,\;\cdot\;)\;
\frac{12}{g_s^2}\,V_4^{-1}\;
\frac{g_s^2}{6}\,V_4(\;\cdot\;,\Psi_k\Psi_l)
\;=\;\frac{g_s^2}{3}\,V_4(\Psi_1,\Psi_2,\Psi_3,\Psi_4),
\tag{4.1}
$$

using full graded symmetry of $V_4$ (H2, closed). Summing the three matchings gives
$g_s^2\,V_4(\Psi_1,\dots,\Psi_4)$ = exactly the contact kernel of
$+\frac{g_s^2}{4!}V_4(\Psi^{\otimes2},\Psi^{\otimes2})$ on distinct externals.

**Geometric reading — the covering of $\mathcal M_{0,4}$ in the cubic theory:**

| channel | kernel | image in $\mathcal M_{0,4}$ | multiplicity |
|---|---|---|---|
| $\Psi$-exchange $s,t,u$ | two $V_3$'s $+$ (0.2) | the three propagator regions $\mathcal M_{s},\mathcal M_t,\mathcal M_u$, **disjointly**, each swept once by $(s,\theta)$ | geometric, $\times1$ |
| $\Sigma$-exchange, each of 3 matchings | two $V_4(\Sigma,\Psi\Psi)$'s $+$ (0.3) | **all of $\mathcal V_{0,4}$**, from the vertex-region integrals already inside the two vertices | combinatorial, $\times3$ with weight $\tfrac13$ each |

So the answer to "how does the moduli covering happen, with three channels, non-trivially":
the three $\Sigma$-channels do **not** partition $\mathcal V_{0,4}$ into three
sub-regions (nothing like the $s,t,u$ tiling happens). Each channel reproduces the
*entire* vertex region — its moduli come from the vertex integrals (0.1) that each
$V_4(\Sigma,\Psi\Psi)$ carries within itself, not from the edge — and the $3\times\frac13$
bookkeeping is pure symmetry-factor arithmetic. The colour-2 edge adds no region and no
degeneration: the covering statement of the HS theory is
$\mathcal M_{0,4}=\mathcal M_s\sqcup\mathcal M_t\sqcup\mathcal M_u\sqcup\mathcal V_{0,4}$
with the first three supplied geometrically (colour-1 necks, continuous moduli) and the
last supplied combinatorially (colour-2 edges, multiplicity $3$, weight $\frac13$).

*(Contrast kept explicit to avoid the Phase-6 conflation: the R2 statement — twist-only
gluing of two asymmetric cubic $\mathcal V_3'$ reproducing $\partial\mathcal V_{0,4}$ —
belongs to the vertex-decomposition programme, a different construction from the HS
$\Sigma$-exchange, whose vertices are the quartic $V_4(\Sigma,\Psi\Psi)$ regions
themselves.)*

---

## 5. Coloured operad: why two pairs of punctures glue without genus

The clean formalisation makes §1's "formal genus" a non-issue by choosing the right
objects. Take a multi-sorted (coloured) operadic structure with **objects (colours)**

$$
C_1=\Hilb_0,\qquad C_2=\operatorname{Sym}^2\Hilb_0,\qquad\dots,\qquad
C_k=\operatorname{Sym}^k\Hilb_0,\qquad N_{\rm gh}(C_k)=2k~\text{(fields)} ,
\tag{5.1}
$$

each with its own pairing ($\omega_1$ on $C_1$; $G_k=\omega_1^{\otimes k}$ on $C_k$).
Then:

- $m_2$ is a **unary** operation $C_2\to C_2$ (one input, one output, one colour);
- the HS vertex $V_4(\Sigma,\Psi,\Psi)$ is a $(C_2;C_1,C_1)$-corolla;
- the cobracket $p_{1,2,0}$ is a $(C_1\to C_2)$ colour-changing unary operation;
- composition = contraction of one $C_k$-edge with $G_k^{-1}$.

In this category a colour-2 edge is **one edge**; a tree is a tree; genus is the coloured
loop number $L_c=E-V+1$. The "two punctures at once" of the strand picture is the
*resolution functor* $\rho:C_2\hookrightarrow C_1\otimes C_1$, which is a morphism of
vector spaces but **not** of the graded operadic structures — it fails to preserve
exactly the three gradings of the table in §1. Formally, with $E_s=\sum_e k_e$ elementary
strand-sewings across coloured edges $e$ of strand numbers $k_e$:

$$
\boxed{\;g_{\rm res}\;=\;E_s-V+1\;=\;L_c+\sum_{e}(k_e-1)\;}
\tag{5.2}
$$

(derivation: $\chi$ is additive under sewing and each of the $E_s$ puncture-pair sewings
preserves total $\chi=\sum_v(2-n_v)$; solve $2-2g_{\rm res}-n_{\rm ext}=\sum_v(2-n_v)$
with $n_{\rm ext}=\sum_v n_v-2E_s$). The coloured (physical) grading uses $L_c$; the
resolved (formal) genus exceeds it by $k_e-1$ per colour-$k$ edge. **A colour-2 edge
raises the resolved genus by one and the physical genus by zero** — the discrepancy is
not a paradox but the statement that $\rho$ is not a map of operads. In the properad/PROP
language: multi-edge gluings between two vertices are exactly what properads grade by
graph genus (Vallette 2007); treating $\operatorname{Sym}^2\Hilb_0$ as a single colour
converts the multi-edge gluing into a dioperadic (single-edge, tree-level) composition
(Gan 2003). The construction chooses the second description, and the amplitudes agree
with it (§1 table). *(Literature anchors to be verified when cited in the tex:
Getzler–Kapranov modular operads; Gan dioperads math/0201074; Vallette PROPs
math/0411542; 't Hooft 1974 for the double-line analogy.)*

**CFT-data statement of the colour-2 composition.** Contracting a $C_2$ edge inserts, at
two punctures of one vertex region and two of another,

$$
\sum_{a,b,c,d}\big(V_4^{-1}\big)^{(ab),(cd)}\;
|\phi_a\rangle|\phi_b\rangle\;\otimes\;|\phi_c\rangle|\phi_d\rangle
\tag{5.3}
$$

— a fixed (moduli-independent) two-string state sandwich. Compare the colour-1 insertion
(0.2), which is $\sum_a\int ds\,d\theta\;e^{-sh_a+i\theta\bar h_a}\,b\text{-dressed}\,
|\phi_a\rangle\langle\phi^a|$: the difference between the two kernels — presence/absence
of the $(s,\theta)$ family and its $b$'s — *is* the entire geometric distinction between
propagating and auxiliary, and it sits in the edge kernel, not in the vertices.

---

## 6. The Witten/OSFT dictionary

The analytic-solution technology of open SFT (Schnabl 2005; Erler–Schnabl 2009; Erler's
lectures 1912.00521) is built on the algebra $K,B,c$: $K$ generates worldsheet strips,
$e^{-tK}$ = wedge of width $t$ (a surface per $t$), $B$ its $b$-ghost partner, $c$ a
boundary insertion. The closed HS construction has a precise entry-by-entry analogue:

| open string ($KBc$) | closed HS | status |
|---|---|---|
| $K$: strip **generator**; $e^{-tK}$ = one surface per $t$ (continuous semigroup) | $L_0^+$: cylinder generator; $e^{-sL_0^+}$ = one surface per $s$ | both geometric |
| Witten $*$: half-string overlap, **moduli-free** vertex; covers $\mathcal M$ with $1/K$ alone (Giddings–Martinec–Witten 1986) | vertex regions $\mathcal V_{0,n}$: moduli-free *as vertices* (moduli pre-integrated); do **not** cover $\mathcal M$ alone (Sonoda–Zwiebach) — hence the tower | the no-go is the closed-string difference |
| wedge algebra $e^{-t_1K}e^{-t_2K}=e^{-(t_1+t_2)K}$: width additive, continuous | chain monoid $m_2^{n}m_2^{n'}=m_2^{n+n'}$: length additive, **discrete** (§2.a) | the central structural analogy |
| $\dfrac{1}{1+K}=\int_0^\infty dt\,e^{-t}e^{-tK}$: geometric because every fibre is an honest positive-width strip | $m_2^{-1}=\sum_n (D^{-1}N)^nD^{-1}$ (3.1): "geometric" because every term is an honest frozen-neck chain | both are resolvent presentations with positive spectral data |
| inverse wedge $e^{+K}$ ("negative width"): formal, non-geometric; legal only in combinations with net positive width, $e^{K}e^{-2K}=e^{-K}$ | $m_2^{-1}$ bare: formal, non-surface (§3.i); legal sandwiched, $V_4V_4^{-1}V_4=V_4$ (R14/R15) | telescoping = "net positive width" |
| $1/K$ dangerous: $\operatorname{spec}(K)$ reaches $0$ (sliver); needs the security strip / phantom terms | $1/m_2$ conditional: $\operatorname{spec}(m_2)$ bounded from $0$ = (5.1)/A2(iii); kernel quotiented by the 2026-07-01 annotation | same spectral condition, different space |

Two uses of the dictionary. *(a)* It answers "what does an analytic-solution practitioner
mean by manipulating non-geometric elements": exactly what R14 licenses — formal
inverses are permitted whenever the full expression telescopes to net-geometric objects,
and the amplitude-level identities (4.1) are the closed-string counterpart of the
wedge-width bookkeeping that makes $\psi=\frac{1}{1+K}c(1+K)Bc\frac{1}{1+K}$-type
solutions well-defined. *(b)* It locates the genuinely open analytic question:
Erler-style control of $1/(1+K)$ rests on knowing $\operatorname{spec}(K)\ge0$; the
closed analogue — positivity/gap of $m_2$ on $\operatorname{Sym}^2\Hilb_0$ — is A2(iii),
and the dictionary suggests importing the OSFT toolkit (resolvent estimates, level
truncation of the spectral density) rather than seeking a worldsheet representation that
does not exist.

*(Interpretive status: the table's OSFT-side facts are literature; the closed-side facts
are R14/R15/R9; the correspondence itself is an organising analogy, not a theorem.)*

---

## 7. The $\Sigma_k$ tower: colours, cables, and the continued fraction

Scheme B (R25/R26) adds, per level $k$: kinetic $\tilde V_{2k}(\Sigma_k,\Sigma_k)$, odd
coupling $\tilde V_{2k+1}(\Sigma_k,\Sigma_k,\Psi)$, source $L_k$ coupling $\Sigma_{k-1}$
to $\Sigma_k$. Everything in §§1–6 extends verbatim with colour set $\{C_k\}$:

- **Edges are $k$-strand cables.** A colour-$k$ edge contracts $G_k^{-1}$ =
  $k$ simultaneous frozen-neck sewings; by (5.2) it adds $k-1$ to the resolved genus and
  $0$ to the physical one. A single $\Sigma_3$ edge already hides a frozen genus-2
  surface; the classical (coloured-tree) cubic action thus resums, at order $g_s^{2K}$,
  frozen configurations of resolved genus up to $\sum(k_e-1)$ — with **no** $g_s$-cost,
  no neck moduli, no $b$'s: the same three-grading table certifies the coloured reading
  at every $k$.
- **Vertex regions.** $\tilde V_{2k}$ lives on (dressed) $\mathcal V_{0,2k}$
  ($\dim_{\mathbb R}=2(2k-3)$), and the §0 saturation holds identically at every $k$ —
  the tower is ghost-consistent as a family of *bona fide* elementary vertex regions.
- **Dressing = amputated colour-2 subtrees.** $\tilde V_{2k}=V_{2k}+(\text{terms
  containing } V_4^{-1},\dots)$: in coloured-graph language the dressed kernel is the
  bare $2k$-punctured region *minus* its colour-reducible parts — "vertex = amplitude
  minus exchanges", now at the level of kernels with frozen necks, which is why no
  moduli bookkeeping accompanies the subtraction (scheme A's $W_n$ statement, R19/R25).
- **The continued fraction is nested telescoping.** R26's
  $\hat H_k=\hat M_k-g^2\frac{(2k)!}{(2k+2)!}L_{k+1}^\top\hat H_{k+1}^{-1}L_{k+1}$
  reads geometrically as: the effective colour-2 kernel at level $k$ = the level-$k$
  vertex region corrected by chains passing through ever-higher strand numbers; every
  $\hat H_{k+1}^{-1}$ appears sandwiched between $L_{k+1}$'s, so the whole fraction
  telescopes to contact support — the all-orders version of (4.1). Convergence in $g$ of
  the fraction (R26 open item (iv)) is the tower analogue of the spectral condition in
  §6(b).

**Figures to draw (spec for RS2).**
F1: the three $\Sigma$-exchange matchings in double-line notation, all mapping onto the
same shaded $\mathcal V_{0,4}$, vs the $s,t,u$ cylinder channels mapping onto disjoint
regions (two-panel).
F2: chain of $k$ 4-punctured spheres with $k{-}1$ frozen double-necks; underside: the
resolved genus-$(k-1)$ surface; caption = the three-grading table.
F3: a $\Sigma_3$ (3-strand cable) edge between two $\mathcal V_{0,6}$ regions; resolved
genus-2 surface.
F4: colour-1 edge vs colour-2 edge kernels side by side ((0.2) vs (5.3)): cylinder family
with $(s,\theta)$ and two $b$'s, vs rigid two-strand sandwich.
F5: scheme-B tower as a coloured tree (cables of increasing strand number), with the
continued fraction as nested boxes.

---

## 8. Self-review, open points, overclaim flags

1. *Does this answer the motivating objective?* Yes for Q2–Q4 (formula-level dictionary:
   (0.2) vs (0.3)/(5.3); (2.1)–(2.2); (3.1)–(3.3); (4.1); (5.2)) and Q5 (§7). Not a
   proof of new CFT facts: the load-bearing new *derivations* are (5.2) (elementary,
   checkable) and the structural statements (1.a)/(2.a)/(3.i) whose sharp parts reduce to
   the ghost/coupling/moduli diagnostics already ledgered (R14/R15/R23).
2. *Weakest step (RESOLVED, RS4/derivation 021):* (1.a) — the identification "one
   $\omega_1^{-1}$ contraction = frozen-length plumbing" is now
   **verified-against-primary-source**, with one correction: $\omega_1^{-1}=
   b_0^-\delta_{L_0^-,0}$ carries the level-matching $b_0^-$ (not "no $b$-ghost" as
   originally stated); only the length-modulus $b_0^+/L_0^+$ is dropped. Stub
   convergence at $|q|=1$ (021 §5) is consistent-with the book's plumbing range, not
   independently re-derived. The remaining genuinely open geometric item is the
   spectrum of $m_2$ (A2(iii), §6 of this derivation).
3. *Not checked:* nothing numerical yet — RS1 script spec in §9; the properad/dioperad
   citations need verification before entering the tex (RS2).
4. *What would a stronger physicist find?* Possibly a cleaner statement of §3.i as an
   actual no-go ("no local moduli kernel for $m_2^{-1}$") — currently it is a
   diagnostics-based argument (any such kernel forces $b$/$g_s$ structure absent from
   the exchange), one notch below a theorem; worth a critic pass (RS3) on whether the
   diagnostic argument has a loophole (e.g. kernels supported on degenerate/nodal loci
   carrying compensating ghost insertions).
   **ANSWERED (2026-07-09, task RS5, derivation 022):** promoted to a theorem, modulo
   the standard factorization/sewing-completeness input — ghost-grading obstruction
   ($N_{\rm gh}=2+\nu_f\ge2$ for every local geometric kernel vs $-2$ for $m_2^{-1}$),
   independently confirmed by analyticity; the nodal/compensating-ghost loophole is
   closed (all standard node insertions raise or preserve $N_{\rm gh}$, never lower it).
   See §3.i (patched) and `codes/verify-rs5-no-local-kernel.py` (14/14 PASS).

**Do-not-reintroduce list (traps that produced the earlier unsatisfactory answers):**
(T1) the bounded-length $\Sigma$-neck picture (Phase-6 note §5) — wrong construction;
(T2) reading the Schwinger $t$ of $m_2^{-1}$ as a worldsheet length — refuted by ghost
counting; (T3) resolving colour-2 edges into worldsheet plumbing necks with a **length**
modulus — adds genus, $g_s$, and a $b_0^+/L_0^+$ that the amplitude does not have (the
colour-2 edge *does* carry $b_0^-\delta_{L_0^-,0}$ per strand, RS4-corrected; the trap
is specifically adding a length modulus, not adding any $b$-ghost whatsoever);
(T4) expecting the three
$\Sigma$-channels to tile $\mathcal V_{0,4}$ geometrically — the covering is
combinatorial (§4); (T5) conflating the R2 $\mathcal V_3'$ twist-gluing (vertex
decomposition programme) with the HS $\Sigma$-exchange; (T6) demanding a pointwise
moduli cancellation in (3.3) — it is a Gram identity.

---

## 9. Verification spec (RS1 — companion script `codes/verify-riemann-m2-geometry.py`)

Finite-dimensional model: $\Hilb=\mathbb R^d$ (graded if cheap), random symmetric
invertible $V_4$ on $\operatorname{Sym}^2$, random invertible $G_2$; seeds printed; every
check must be falsifiable (perturb-and-fail leg).

1. **Channel arithmetic (re-verifies R14 as restated in (4.1)):** build vertex/propagator
   per §4; check each single matching $=\frac{g_s^2}{3}V_4$ exactly and the sum
   $=g_s^2 V_4$; falsify by perturbing the $12/g_s^2$ normalisation.
2. **No local moduli kernel (toy form of §3.i):** model $V_4=\sum_i w_i K_i$ (discrete
   "moduli points" $i$, rank-structured $K_i$); verify $(\sum w_iK_i)^{-1}\neq\sum w_i
   K_i^{-1}$ and that no reweighting $\sum \tilde w_i K_i$ equals the inverse (least-squares
   residual bounded away from 0 over random draws) — demonstrating inversion is not
   implementable by a measure on the same kernel family.
3. **Gram sandwich (3.3):** $\sum_K G_{IK}(G^{-1})^{KL}G_{LJ}=G_{IJ}$ with $G$ assembled
   from the discrete kernel family; falsification leg.
4. **Neumann chains (3.1):** $D$ = diagonal part; verify convergence iff
   $\rho(D^{-1}N)<1$ (exhibit both regimes) and equality with the matrix inverse.
5. **Laplace (3.2) (extends R15):** positive-spectrum case integrates to the inverse;
   termwise chain expansion of the integrand diverges (partial-sum blowup at fixed
   large $t$); unconditional odd-chain form checked on an indefinite example.
6. **Genus formula (5.2):** random coloured multigraphs (no self-loops), strand numbers
   $k_e\in\{1,2,3\}$; compute $\chi$ by explicit puncture/sewing counting and compare
   $g_{\rm res}=L_c+\sum(k_e-1)$; include the chain ($g=k-1$) and single-edge ($g=1$,
   eq. (1.1)) instances.
7. **Saturation identities (§0):** $\sum N_{\rm gh}-2(n-3)=6$ for the vertex list incl.
   tower entries at symbolic $k$ (sympy); R23 cross-check $N_{\rm gh}(p_{k,\ell,g})=
   3\ell-2k+g$ on the low table.
8. **Sewing-vs-sandwich dimension count (toy of §5/(0.2) vs (5.3)):** compare the
   parameter-family dimensions: colour-1 edge contributes a 2-parameter family (model
   $q^{L_0}$ with $L_0$ diagonal), colour-2 edge contributes a 0-parameter sandwich;
   verify the composite "amplitude support" dimensions add accordingly.

Checks 1–5 are numpy; 6–7 sympy/pure python; 8 numpy. Estimated: one computator run.

---

## 10. Session addendum (2026-07-09, follow-up questions) — formal definitions and the explicit $m_2^{-1}$-cancellation mechanism

Two follow-up questions, worked out in chat and folded into the
canonical write-up `knowledge/cubic-sft-riemann-surfaces.tex` (§§`sec:frozen`,
`sec:inverse`; this addendum records the same content compactly for the internal
derivation record — the tex is now the more complete presentation, with worked
examples and a boxed one-sentence summary; read it for the full prose).

### 10.1 Formal definitions (tex `\Cref{def:frozenneck,def:colour2edge,def:chain}`)

**Frozen-neck contraction.** The gluing obtained from ordinary plumbing
(0.2)/eq:sewing by fixing the neck modulus at $q=1$ instead of integrating over
it, and omitting the $b$-ghost insertions: insertion of the bare bivector
$\omega_1^{-1}=\sum_a|\phi_a\rangle\langle\phi^a|$ at two punctures, no
$q^{L_0}\bar q^{\bar L_0}$ weight, no $\int ds\,d\theta$. Contrast made explicit:
ordinary plumbing sews and then *lets the neck stretch* (a family); a frozen-neck
contraction sews at one *pinned* value of $q$ (a single surface).

**Colour-2 edge** = two simultaneous frozen-neck contractions, one per puncture
of a $\Sigma$-pair. $\chi$-additivity ⇒ $g=1$ for a single edge (eq. (1.1)).

**Length-$k$ chain** = $k$ copies of $\mathcal V_{0,4}$ joined in series by $k-1$
colour-2 edges; the surface underlying one term of $m_2^{k-1}$. Worked examples
added: $k=2$ (single edge, $g=1$, 2 unfrozen vertex moduli = 2 complex out of the
would-be genus-1 surface's larger moduli space) and $k=3$ ($g=2$, checked
independently via $\chi=-2-2-2=-6$, $n_{\rm ext}=4\Rightarrow g=2$, matching (5.2)
at $k=3$: $g=k-1=2$ ✓).

### 10.2 The explicit $m_2^{-1}$-cancellation mechanism

This sharpens the abstract Gram-identity statement of §3 eq. (3.3) into an
explicit operator derivation (reproduces, in the surface language, the
combinatorial telescoping already proven algebraically in derivation 007/R14,
eq. A.6–A.9 — not new algebra, but a new *reading* of why it works geometrically).

Setup: $P=\operatorname{Sym}(\Psi_1\otimes\Psi_2)$,
$Q=\operatorname{Sym}(\Psi_3\otimes\Psi_4)\in\operatorname{Sym}^2\mathcal H_0$, basis
$\{e_I\}$. Vertex 1's amplitude $v_I=V_4(e_I,\Psi_1,\Psi_2)=V_4(e_I,P)$ is an
honest, freshly-performed $\int_{\mathcal V_{0,4}}d^2m$ integral. By the
*definition* of $m_2$ ($G_2(m_2X,Y)=V_4(X,Y)$ for all $X,Y$), this integral,
once fully done, equals $G_2(e_I,m_2P)$ — the modulus $m$ is now hidden inside
the state $m_2P$. Same for vertex 2: $w_J=G_2(e_J,m_2Q)$, its own modulus $m'$
folded into $m_2Q$.

The propagator contracts these two *already-integrated* covectors:
$$
\sum_{I,J}v_I\,(m_2^{-1}G_2^{-1})^{IJ}\,w_J
= G_2(m_2P,\,m_2^{-1}m_2\,Q)
= G_2(m_2P,Q) = V_4(P,Q) = V_4(\Psi_1,\Psi_2,\Psi_3,\Psi_4).
$$

**The mechanism, stated once:** $m_2^{-1}$ does not touch either vertex's moduli
integral *while it is being performed* — both are completed first, producing
$m_2P$ and $m_2Q$ — and it then **algebraically cancels the $m_2$-map built into
one specific factor** ($m_2^{-1}m_2=\mathrm{id}$ on $Q$'s slot, as placed; by
$G_2$-symmetry of $m_2$ the same computation with factors swapped cancels the
other factor's $m_2$ instead, same answer by symmetry). What remains, $V_4(P,Q)$,
is **one fresh copy of $V_4$'s own moduli integral**, saturated directly by all
four external legs with an independent third modulus $m''$ — *not* a leftover
half of each of the two original integrals. This is why $\dim_{\mathbb C}=1$
survives out of the naive $1+1=2$: not by discarding half a 2-complex-dimensional
family, but by an operator cancellation removing one *whole* $m_2$-factor,
leaving a single, independently saturated $V_4$.

**Why no pointwise/worldsheet-locus implementation of $m_2^{-1}$ can exist** (this
is the sharp version of trap T6 and of §3.i's diagnostic argument): the
information that "removes one vertex's moduli" lives entirely in the algebraic
step $m_2^{-1}m_2=\mathrm{id}$, which happens *after* both moduli integrals are
complete and acts in the state-space (spectral) direction — never on $m$ or $m'$
individually, and never via any degeneration or pinch of a worldsheet. Every
earlier attempt to locate a worldsheet region "where the cancellation happens"
was looking for something that structurally cannot exist.

**Status:** proven at the level of the finite-dimensional Gram/operator algebra
(uses only the definition of $m_2$ and $m_2^{-1}m_2=\mathrm{id}$ — no new
assumption beyond what R14/derivation 007 already established); the surface
identification of each vertex integral (i.e. that $v_I$, $w_J$ really are
$\mathcal V_{0,4}$ moduli integrals in the CFT sense) rests on (1.a)/RS4 as
before. Not yet added to RS1's script — candidate check 9 for a future
verification pass (verify $v^T(V_4^{-1})w = V_4(P,Q)$ numerically on random
symmetric invertible $V_4$, both by direct construction of $v,w$ from $P,Q$ via
$v=G_2 m_2 P$ and by the matrix telescoping route, confirming they agree).
