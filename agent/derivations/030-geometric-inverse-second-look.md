# 030 — Geometric $1/m_2$, second look: the map of geometric options for the auxiliary channel

**Date:** 2026-09-08 (Task 12, sub-tasks 12a–12d). **Record status: CLOSED 2026-09-08 — blind critic (Fable) REVISE→fixes; narrow confirmation (Opus) residues applied; promoted as R28′ annotation + R30.**
Shared record for 12a–12d; each sub-task appended its sections and moved the single `## Status` line.
**Script:** `codes/verify-geometric-inverse.py` (part 1 = §1 table; part 2 = §3 candidates; part 3 = §4 toy; part 4 = §5.6 scaling lemma; 113/113 PASS, seed 20260908).
**Reuses (does not re-derive):** R23 ($N_{\rm gh}(\mathfrak p_{k,\ell,g})=3\ell-2k+g$, anchor
$N_{\rm gh}(m_2)=+2$), R27 (frozen node $=+5$, two-kernel distinction), R28 / 022 eq. (2.2)
($N_{\rm gh}=2+\nu_f$ for the class of 022 §1), RS4 / 021 ($\omega_1^{-1}=b_0^-\delta_{L_0^-,0}$,
$\mathsf P=(b_0^+/L_0^+)\,\omega_1^{-1}$), R3 (Erbin–Fırat bounded open propagator).

**Literal task (12a).** Fix one convention set; tabulate $N_{\rm gh}$ (as a map on
$\mathrm{Sym}^2\mathcal H_0$ and as a 4-form) for every elementary geometric object that a
candidate $1/m_2$ kernel could be built from; check the table against R23 and 022 (2.2);
restate R28's class and list what it excludes versus what it does not cover.

**Motivating objective (Task 12).** A map of the geometric options for the auxiliary
channel — for each candidate, the obstruction or the construction — so that the options can
be compared: (α) single-strand auxiliary in $\mathcal H$, (β) double-strand auxiliary with a
bounded/diagonal double-tube propagator and a redefined kinetic term, (γ) the present
$V_4$-kinetic auxiliary. 12a's contribution: a ghost-number table that *cannot* be argued
with later, and a precise statement of which candidates R28 does and does not touch.

---

## 0. Verdict table (final, 12d) and five-line summary

Ghost numbers below are "as a map $\mathrm{Sym}^2\mathcal H_0\to\mathrm{Sym}^2\mathcal H_0$"
in the physical grading of §1. Target: $N_{\rm gh}(m_2^{-1})=-2$, two real moduli of $V_4$
to be accounted for. "Status" cells: *to do* until the sub-task that owns the row fills it.

| candidate | ghost count (map) | moduli count | R28 covers? | status |
|---|---|---|---|---|
| (a) diagonal double tube $\mathsf P_{\rm diag}$ (one length, one twist, both strands) | $0$ (fully diagonal, row 9a — does **not** act on $\mathrm{Sym}^2\mathcal H_0$ at all; lives on $\mathcal S_{\rm pair}$, §3.2); $-1$ (shared length only, 9b); $-2$ with both $b^+$ kept | 2; 3 | no (disconnected) | **excluded** (12b §3.2): ghost number for 9a/9b, no dressing rescues; the $b_1b_2$ version is excluded by Prop. 3.2 (commutant). Live as the propagator of a redefined auxiliary (β) → §3.7, §5.3; **open → hand-off Q13 (§6.1)** |
| (b) bounded double tube $\mathsf P_{[0,\lambda]}^{\otimes2}$ | $-2$ ✓ (rows 7/8) | 4 (2 bounded lengths, 2 twists) | no (disconnected) | **excluded** (12b §3.1, Prop. 3.1, for $\hat k\otimes\hat k$: rank across strands unless $\dim=1$; the polarised undressed case is Prop. 3.2's, the polarised dressed case only §5.6's; Prop. 3.2 independently); row 7 also by poles; sums of products = Neumann chain only |
| (c) half-frozen kernel (antighosts > integrated moduli) | connected: $\ge2$ (Lemma 2.1); disconnected row 5$^{\otimes2}$: $-2$ | 0–3 | partly | connected case **excluded** (Lemma 2.1); disconnected case **excluded** (12b §3.2, Prop. 3.2); frozen $b_0^+e^{-sL_0^+}$ admissible as a factor ($\partial_\lambda$ of a bounded tube), not as a $Q$-compatible propagator |
| (d) explicit non-sewing ghost insertions on a connected surface | $2-n_x$ (row 14), reaches $-2$ at $n_x=4$ | $6g+2$ | no | **excluded** (12b §3.3, eq. 3.8), as a uniform construction (§5.6): homogeneous of degree $+1+g$ across the family $tV_4$, $m_2^{-1}$ of degree $-1$; at $t=1$ a fine-tuned dressing $m_2B^tm_2B'=\mathrm{id}$ is not excluded by this argument; the object is a dressed vertex, not $Q$-closed |
| (e) Erbin–Fırat-type change of kinetic term ($m_2\to$ inverse of a bounded tube) | kinetic $+2$, propagator $-2$ ✓ (§1.4(d)); composite needs $n_b^{\rm tot}=8=\dim\mathcal M_{1,4}$ (eq. 3.12) | 2 with rigid $\mathcal W_3$ + diagonal tube on $\mathcal S_{\rm pair}$ or bounded product on $\mathrm{Sym}^2\mathcal H_0$ (Lemma 3.3) | not applicable | counts (i)–(iv) all pass (12c §3.7.6); SZ evaded; **obstruction** as a surface factorisation of $\mathcal V_{0,4}$ (composite is a 2-dim family in $\mathcal M_{1,4}$, genus 1 vs 0); **open** as a correlator identity (branched-cover question, eq. 3.13); toy: every fixture the toy can build — disconnected $\mathcal W_3$, real-positive $g$, and a rank-limited $P$ that is not itself a geometric object — fails at its analytic floor (§4.3); **open → hand-off Q13 (§6.1, Task 13)** |
| (T1) bounded plumbing neck (R27 trap, reopened) | $2+\nu_f$ if connected (single neck); $-2$ as a double tube | 2 (diagonal) | yes (connected) | reproduces the T1 failure mode for case (γ) (12b §3.5); **live** as the propagator of a redefined auxiliary: **(α-neck)** necks of $\mathcal V_4^{\rm stub}$ (Task 14; the faithful Erbin–Fırat transplant — leaves $\mathcal V_{0,4}$'s interior untouched, so does not by itself make the theory cubic), (β) $\mathcal W_3\circ\hat K_{\rm diag}\circ\mathcal W_3$ with moduli count $2$ ✓, factorisation = Q13 (§6.1); **(α-rev) open → hand-off (6.1)/(6.2) (§6.2, Task 14)** |
| (T2) Laplace $t$ as a worldsheet length (R27 trap, reopened) | $e^{-tm_2}$ homogeneous only if $\gamma(t)=-2$ (Lemma 2.2) | — | no | **excluded** (Lemma 2.2 + Prop. 3.2; 12b §3.4): $t$ is the $\Sigma$-worldline proper time in target space; a tube length only under (e) |
| (ref) connected kernel of 022 §1 class | $2+\nu_f$ | any | yes | excluded (R28) |
| (all of the above, finite sums, $V_4$-independent bounds) | degree $\ge0$ in $V_4$ vs $-1$ | any | — | **excluded as a uniform construction** (one that would also invert $tV_4$) by the scaling lemma (§5.6, script part 4); individually, at the actual $V_4$: product kernels (Prop. 3.1, $\hat k\otimes\hat k$), tube-only kernels of any measure (Prop. 3.2), and the Laplace reading (Lemma 2.2) are excluded; explicit-ghost dressings and mixed tube/slice kernels are excluded only as uniform constructions; not covered: $V_4$-dependent bounds, infinite sums, change of kinetic term |


**Five-line summary (12d).**
1. For the present auxiliary (γ), $1/m_2$ has no geometry in any reading: R28 (grading) for connected kernels, Prop. 3.1 (rank, for $\hat k\otimes\hat k$), Prop. 3.2 (commutant), (3.8) (homogeneity, as a uniform construction), Lemma 2.2 (Laplace $t$ is target-space time), and the scaling lemma §5.6 uniformly over all finite sums with $V_4$-independent bounds; (γ) reproduces $V_4$ exactly (R29) and needs none.
2. Geometry for the auxiliary channel exists only by *redefining the kinetic term as the inverse of a chosen bounded propagator* (Erbin–Fırat); this changes the identity to be satisfied, not the kernel.
3. (β) double strand: Harold's 2→2 fixture survives every count exactly as (β2) — rigid $\Omega_{V_4}(\mu_0)$ slices and the diagonal tube $b_1b_2b_1^-b_2^-(1-e^{-\lambda L_{\rm tot}})/L_{\rm tot}$ on $\mathcal S_{\rm pair}$ — but integrating it out gives a torus family, not $\mathcal V_{0,4}$ (proven); the composite also carries a genuine loop momentum that $\mathcal V_{0,4}$ does not, which gives a cheap route to a 'no' (§3.7.3); it is true iff Q13 (double cover branched at the external punctures) holds — hand-off to Task 13.
4. (α-rev) single strand: all counts pass with sphere topology; whether the bounded-neck $\mathcal V_3'$ family covers $\mathcal M'_\times$ once, (6.1)/(6.2), is a decidable moduli-space computation — hand-off to Task 14; note the neck must run to $|q|>1$, with the local coordinate discs of $\mathcal V_3'$ extended to radius $e^{\sigma(\theta)}$ and remaining embedded (Task 14's first count), and a twist-dependent bound forces $\Phi\in\mathcal H$. This is a distinct prescription from **(α-neck)** (§3.5), the faithful Erbin–Fırat transplant, which is consistent but does not cover $\mathcal V_{0,4}$'s interior and so does not by itself make the theory cubic.
5. Ledger: annotate R28 with R28$'$ (§8) and add a row for (α-neck)/(α-rev)/(β) (§8); the paper's §7 chain is unaffected.

---

## 1. Conventions, once, and the $N_{\rm gh}$ table

### 1.1 The convention set (fixed for all of Task 12)

Everything below is stated once; later sub-tasks cite "030 §1.1" instead of re-choosing.

**(C1) Spaces.** $\mathcal H$ = full closed-string state space (all four ghost zero-mode
sectors $\downarrow\downarrow,\downarrow\uparrow,\uparrow\downarrow,\uparrow\uparrow$, 021 §1).
$\mathcal H_0=\ker L_0^-\cap\ker b_0^-$ (field states are $\downarrow\downarrow$: $b_0^\pm\phi=0$).
$\mathrm{Sym}^2\mathcal H_0$ = the $\Sigma$ space. Zero modes $b_0^\pm=b_0\pm\bar b_0$,
$c_0^\pm=\tfrac12(c_0\pm\bar c_0)$, $\{b_0^\pm,c_0^\pm\}=1$ (021 §1, verified there).

**(C2) Ghost number.** $N_{\rm gh}(c)=+1$, $N_{\rm gh}(b)=-1$, $N_{\rm gh}(|0\rangle)=0$, so
$c_1\bar c_1|0\rangle$ has $N_{\rm gh}=2$; physical string field $N_{\rm gh}(\Psi)=2$,
$N_{\rm gh}(\Sigma)=4$. Anomaly: a correlator on $\Sigma_{g,n}$ with $n_b$ antighost and $n_c$
extra ghost insertions is non-zero only if
$$
\sum_{i=1}^n N_{\rm gh}(A_i)\;=\;6(1-g)+n_b-n_c .
\tag{1.1}
$$
Sphere saturation is the $g=0$, $n_b=n_c=0$ case ($=6$); torus $=0$. With the full
antighost measure $n_b=\dim_\R\mathcal M_{g,n}=6g-6+2n$, (1.1) gives $2n$ at every genus
(book `bos_feynman` eq. after l. 318: $N_{\rm gh}(\phi_\alpha)=2n_1-\sum N_{\rm gh}(\mathcal V_i)$,
i.e. the integrated $\mathcal V_{g,n}$ saturates at $2n$). For a disconnected object
(several surface components), (1.1) is applied to each connected piece and the total
anomaly is additive over components; this is the assumption used silently whenever a
candidate kernel is a sum or product over several surfaces (rows 6–9b below).

**(C3) Pairing.** $\omega_1(A,B)=\langle A|c_0^-|B\rangle_{\rm bpz}$ on $\mathcal H_0$; non-zero
only if $N_{\rm gh}(A)+N_{\rm gh}(B)=5$ (one $c_0^-$ in a sphere 2-point function). BPZ itself pairs
at 6. $G_2=\omega_1^{\otimes2}$ on $\mathrm{Sym}^2\mathcal H_0$ pairs at 10. Inverse bivectors:
$\omega_1^{-1}=b_0^-\delta_{L_0^-,0}$ (021 §4; the $b_0^-$ inverts the $c_0^-$ on $\ker b_0^-$),
$G_2^{-1}=(\omega_1^{-1})^{\otimes2}$.

**(C4) Level matching and twist.** Every closed-string sewing carries the twist integral
$\int_0^{2\pi}\frac{d\theta}{2\pi}\,b_0^-e^{i\theta L_0^-}=b_0^-\delta_{L_0^-,0}=\omega_1^{-1}$.
The twist is a compact modulus integrated to a Kronecker delta; it is *never* the modulus
that distinguishes candidates (021 §4.3). The discriminating modulus is always the length
$s\ge0$ with its antighost $b_0^+$: $\int_0^\infty ds\,b_0^+e^{-sL_0^+}=b_0^+/L_0^+$.

**(C5) Sewing fixtures (021, exact, prefactor included).** Propagator
$\mathsf P=\dfrac{b_0^+b_0^-}{L_0^+}\delta_{L_0^-,0}=\dfrac{b_0^+}{L_0^+}\,\omega_1^{-1}$;
bounded propagator $\mathsf P_{[0,\lambda]}=b_0^+\dfrac{1-e^{-\lambda L_0^+}}{L_0^+}\,\omega_1^{-1}$
(closed analogue of R3's $b_0(1-e^{-2\lambda L_0})/L_0$); frozen node $\omega_1^{-1}$ (R27).

**(C6) Three gradings for one object, and the translation between them.** A candidate kernel
is met in three guises; each has its own natural ghost count. Fix the names:

- **operator ghost number** $N^{\rm op}(\mathcal O)$: the net $b/c$ mode count of an explicit
  operator on $\mathcal H$ ($\mathsf P$: $-2$; $\omega_1^{-1}$: $-1$; $b_0^+/L_0^+$: $-1$);
- **bivector content** $S_B$: for a sewing bivector $B=\sum B^{ab}\,\phi_a\otimes\phi_b$
  filling two form slots, the required $N_{\rm gh}(\phi_a)+N_{\rm gh}(\phi_b)$. The bare BPZ
  bivector $\sum_a|\phi_a\rangle\langle\phi_a^c|$ over all of $\mathcal H$ has $S_B=6$; each $b$
  mode multiplying it lowers $S_B$ by one. So $\omega_1^{-1}$: $S_B=5$; $\mathsf P$: $S_B=4$
  (= the book's $N_{\rm gh}(\phi_\alpha)+N_{\rm gh}(\phi_\beta)=4$, `bos_feynman` l. 325);
- **form saturation** $S(\Omega)$: for a multilinear form on $\mathcal H_0$-legs, the required
  $\sum_i N_{\rm gh}(A_i)$ ($V_4$: 8; $G_2$: 10; $\omega_1$: 5);
- **map ghost number** $\gamma(\mathfrak p)$ for $\mathfrak p:\mathcal H_0^{\otimes k}\to
  \mathrm{Sym}^\ell\mathcal H_0$: $N_{\rm gh}(\mathfrak p(A_1..A_k))-\sum_iN_{\rm gh}(A_i)$. This
  is R23's grading ($\gamma(m_2)=+2$, $\gamma(\mathfrak p_{k,\ell,g})=3\ell-2k+g$).

Translations (derived in §1.2, used everywhere after):
$$
\gamma \;=\; 5\ell-S \qquad(\text{form}\leftrightarrow\text{map, } \ell \text{ output legs paired by }\omega_1),
\tag{1.2}
$$
$$
\gamma \;=\; S_B-5\ell \qquad(\text{bivector on }\ell\text{ strands}\leftrightarrow\text{map}),
\tag{1.3}
$$
$$
\gamma \;=\; N^{\rm op}+\ell \qquad(\text{sewing operator on }\ell\text{ strands}\leftrightarrow\text{map: one }b_0^-\text{ per strand is absorbed by the }c_0^-\text{ of }\omega_1).
\tag{1.4}
$$
Target: $\gamma(m_2^{-1})=-2$, i.e. $S=12$ as a 4-form, $S_B=8$ as a bivector on two strands,
$N^{\rm op}=-4$ as a raw two-strand operator.

**(C7) Open-string dictionary (for the cross-check only).** Open: $S_{\rm disk}=3$, BPZ pairing
$\omega(A,B)=\langle A|B\rangle$ at 3 (no $c_0$), field $N_{\rm gh}=1$, integrated $\mathcal V_n$
saturates at $n$, map $\gamma=2\ell-k$ (so $Q_B$: $+1$, $m_2=*$: $0$), and (1.4) becomes
$\gamma=N^{\rm op}$ (no $c_0$ to absorb).

### 1.2 Derivation of the translations (1.2)–(1.4) and the single counting rule

**(1.2), form ↔ map.** Let $\mathfrak p$ have $k$ inputs, $\ell$ outputs, map ghost number
$\gamma$. Its form is $\Omega(B_1..B_\ell;A_1..A_k)=\omega_1^{\otimes\ell}\big(B_1\otimes\cdots\otimes
B_\ell,\;\mathfrak p(A_1..A_k)\big)$. Each $\omega_1$ pairs at 5 (C3), so non-vanishing requires
$\sum_jN(B_j)+\big[\sum_iN(A_i)+\gamma\big]=5\ell$, i.e. $S(\Omega)=5\ell-\gamma$. ∎
Checks: $V_4$ as $m_2$'s form ($\ell=2$): $S=10-2=8$ ✓ (one sphere, 4 legs at 2 each, $S=8$
by (C2)); $V_4$ as the $4\to0$ map: $\gamma=0-8=-8=3\cdot0-2\cdot4$ ✓
R23; $\ell_k$ ($\ell=1$): $\gamma=5-2(k+1)=3-2k$ ✓ book `bos:eq:Ngh-bracket-state`.

**(1.3), bivector ↔ map.** A bivector $B=\sum B^{ab}\phi_a\otimes\phi_b$ on one strand defines
the map $\hat B(A)=\sum_{ab}B^{ab}\phi_a\,\omega_1(\phi_b,A)$. Non-vanishing: $N(\phi_b)+N(A)=5$
and $N(\hat BA)=N(\phi_a)$, so $\gamma=N(\phi_a)-N(A)=N(\phi_a)+N(\phi_b)-5=S_B-5$. On $\ell$
strands the shifts add: $\gamma=S_B-5\ell$. ∎ Check: $\omega_1^{-1}$ has $S_B=5$ and is the
identity map, $\gamma=0$ ✓.

**(1.4), operator ↔ map.** A one-strand sewing operator $\mathcal O$ enters as the bivector
$\mathcal O\cdot\sum_a|\phi_a\rangle\langle\phi_a^c|$ (BPZ bivector, $S_B=6$), so
$S_B(\mathcal O)=6+N^{\rm op}(\mathcal O)$ and by (1.3) $\gamma=1+N^{\rm op}$; $\ell$ strands:
$\gamma=N^{\rm op}+\ell$. ∎ Concretely: $\mathsf P=(b_0^+/L_0^+)\,\omega_1^{-1}$; the
$\omega_1^{-1}=b_0^-\delta$ factor is the identity map on $\mathcal H_0$ and the map is
$\hat{\mathsf P}=b_0^+/L_0^+$ with $\gamma=-1$, while $N^{\rm op}(\mathsf P)=-2$. The $+1$ is
the $c_0^-$ of $\omega_1$ absorbing the $b_0^-$ of the sewing measure. This is the one place
where "$N_{\rm gh}$ of the propagator" is ambiguous in the literature; (1.4) is the
disambiguation used throughout Task 12.

**The single counting rule.** Any candidate kernel is a finite assembly of (i) connected
surface correlators $\Sigma_{g,n}$ with $n_b$ antighost / $n_c$ ghost insertions and (ii)
sewing bivectors filling pairs of slots. Its 4-form saturation is additive,
$$
S_{\rm tot}\;=\;\sum_{\text{surfaces}}\big[6(1-g)+n_b-n_c\big]\;-\;\sum_{\text{bivectors}}S_B ,
\qquad
\gamma\;=\;10-S_{\rm tot}\quad(\ell=2),
\tag{1.5}
$$
since every bivector supplies the ghost number of the two states it inserts and thereby
removes it from what the external legs must supply. **Insertions count; integrations do not.**
Whether a modulus is integrated or its antighost kept on a slice changes the form degree, not
$N_{\rm gh}$. Dropping a modulus *together with its antighost* (R27's freezing) raises
$S$-cost by one, i.e. raises $\gamma$ by one.

*Equivalence with 022 (2.2).* With $V$ vertices of valences $n_v$ (each integrated:
$6+n_b-0=2n_v$), $\nu_f$ frozen nodes ($S_B=5$) and $g_s$ smoothed handles ($S_B=4$):
$\gamma=10-2\sum n_v+5\nu_f+4g_s$, which is 022's $-2\sum n_v+10+5\nu_f+4g_s$ term by term. ∎
(So 022's "$+5$ per output leg / per frozen node, $+4$ per smoothed handle, $-2$ per leg" is
(1.5) in disguise; there is no disagreement — see §1.4 for the one place 022's *prose* is
imprecise.)

*The frozen-handle reading of R23's $+g$ (consistent with R23's operadic self-gluing
description, not stated by it).* Self-gluing an output leg (3) to an input leg
(2) by the plain trace ($\omega_1^{-1}$, $S_B=5$) leaves $\gamma$ unchanged; the naive leg
removal $3\ell-2k\to3(\ell-1)-2(k-1)$ loses 1, hence R23's compensating $+1$ per handle. A
*smoothed* (length-integrated) handle inserts $\mathsf P$ ($S_B=4$) and lowers $\gamma$ by one
relative to the frozen one, so an all-moduli-integrated genus-$g$ surface has $\gamma$
independent of $g$ (its $S=2n$ by (C2)). Both statements are consistent; the table below
lists them as separate rows so that no later sub-task conflates them.

### 1.3 The $N_{\rm gh}$ table

Columns: strands $\ell$ (= output legs of the map); antighost insertions $n_b$ (all $b$'s,
zero-mode or Beltrami); real moduli actually *integrated* $n_\mu$ (twist integrals to a
Kronecker $\delta$ counted as integrated); operator count $N^{\rm op}$ (sewing objects) or
form saturation $S$ (surfaces/forms); map ghost number $\gamma$ by (1.2)–(1.5). Target row is
**bold**. Each entry's one-line derivation follows the table.
Rows 1–9 count the sewing operator's own modes ($b_0^-$'s included; $S_B$); rows 10–14 count insertions on the surface with its punctures attached through $\omega_1$ ($S$); the two differ by one $b_0^-\delta_{L_0^-,0}$ per leg, $n_b^{\rm biv}=n_b^{\rm form}+2\ell$. Row 14 at $g=0$, $n_x=4$ ($n_b=6$) is the connected capless candidate of R40 (2), $n_b=10$ as a bivector. *(Added 2026-10-10, node check `critic-r40-node-check-20261010T132641`, F2.)*

| # | object | $\ell$ | $n_b$ | $n_\mu$ | $N^{\rm op}$ / $S$ | $S_B$ (bivector) | $\gamma$ (map) | $S$ as 4-form ($\ell=2$) |
|---|---|---|---|---|---|---|---|---|
| 1 | frozen node $\omega_1^{-1}=b_0^-\delta_{L_0^-,0}$ | 1 | 1 | 1 (twist) | $-1$ | 5 | **0** | — |
| 2 | cylinder as a map on $\mathcal H_0$: $\hat{\mathsf P}=b_0^+/L_0^+$ | 1 | 1 | 1 (length) | $-1$ | — | $-1$ | — |
| 3 | cylinder with $b_0^-$ (sewing op.) $\mathsf P=b_0^+b_0^-\delta/L_0^+$ | 1 | 2 | 2 | $-2$ | 4 | $-1$ | — |
| 4 | bounded cylinder $\mathsf P_{[0,\lambda]}$ | 1 | 2 | 2 (length bounded) | $-2$ | 4 | $-1$ | — |
| 5 | doubly-frozen node $b_0^+b_0^-\delta$ ($=\lim\lambda^{-1}\mathsf P_{[0,\lambda]}$) | 1 | 2 | 1 (twist) | $-2$ | 4 | $-1$ | — |
| 6 | frozen colour-2 node $G_2^{-1}=(\omega_1^{-1})^{\otimes2}$ | 2 | 2 | 2 (twists) | $-2$ | 10 | **0** | 20−10=10 |
| 7 | double tube $\mathsf P\otimes\mathsf P$ | 2 | 4 | 4 | $-4$ | 8 | **$-2$** | 12 |
| 8 | bounded double tube $\mathsf P_{[0,\lambda]}^{\otimes2}$ | 2 | 4 | 4 (lengths bounded) | $-4$ | 8 | **$-2$** | 12 |
| 9a | fully diagonal double tube (shared $s$ and $\theta$): $(b_0^{+(1)}\!+\!b_0^{+(2)})(b_0^{-(1)}\!+\!b_0^{-(2)})\,\delta_{L^-_{\rm tot},0}/L^+_{\rm tot}$ | 2 | 2 | 2 | $-2$ | 10 | **0** | 10 |
| 9b | length-diagonal double tube (shared $s$, independent twists) | 2 | 3 | 3 | $-3$ | 9 | $-1$ | 11 |
| 10 | connected $\Sigma_{g,4}$, all $6g+2$ moduli integrated | 2 | $6g+2$ | $6g+2$ | $S=8$ | — | **$+2$** (any $g$) | 8 |
| 11 | rigid 4-punctured sphere (fixed point of $\mathcal M_{0,4}$, no $b$) | 2 | 0 | 0 | $S=6$ | — | $+4$ | 6 |
| 12 | half-frozen sphere: $b(\mu_1)b(\mu_2)$ kept, moduli not integrated | 2 | 2 | 0 | $S=8$ | — | $+2$ | 8 |
| 13 | 022-class kernel: $V$ vertices, $\nu_f$ frozen nodes, $g_s$ smoothed handles | 2 | $\sum(2n_v-6)+\nu_f+2g_s$ | $\sum(2n_v-6)+\nu_f+2g_s$ | — | — | $2+\nu_f$ | $8-\nu_f$ |
| 14 | connected surface (any $g$, all moduli integrated) with $n_x$ extra $b$-mode insertions on legs/contours | 2 | $6g+2+n_x$ | $6g+2$ | $S=8+n_x$ | — | $2-n_x$ | $8+n_x$ |
| 15 | $G_2=\omega_1^{\otimes2}$ | 2 (identity) | 0 | 0 | $S=10$ | — | 0 | 10 |
| 16 | $m_2=G_2^{-1}V_4$ | 2 | 2 | 2 | $S=8$ | 12 | $+2$ | 8 |
| **17** | **$m_2^{-1}=V_4^{-1}G_2$** | 2 | — | — | — | 8 | **$-2$** | **12** |

**One-line derivations.**
1. $N^{\rm op}=-1$ ($b_0^-$); $S_B=6-1=5$; $\gamma=5-5=0$ by (1.3) (identity map on $\mathcal H_0$).
2. The map itself: $\gamma=N^{\rm op}=-1$ (no pairing to absorb anything; $b_0^+$ preserves $\mathcal H_0$).
3. $S_B=6-2=4$ (book l. 325); $\gamma=4-5=-1$ by (1.3) $=N^{\rm op}+1$ by (1.4); consistent with 2 since $\mathsf P=\hat{\mathsf P}\omega_1^{-1}$.
4. Same insertions as 3; the bound changes the integration range, not the measure.
5. Same insertions as 3; $s$ not integrated (its $b_0^+$ unsoaked). $\gamma=-1$, same as 3–4 — **insertions count, integrations do not.**
6. Two copies of row 1: $S_B=10$, $\gamma=0$. This is R27's "$+5$ per frozen node" in bivector language.
7. Two copies of row 3: $S_B=8$, $\gamma=-2$; $S=20-8=12$ as a 4-form. **Correct ghost number.**
8. Same as 7.
9a. $\int ds\,d\theta\,b(\partial_s)b(\partial_\theta)e^{-sL^+_{\rm tot}+i\theta L^-_{\rm tot}}$ with $b(\partial_s)=b_0^{+(1)}+b_0^{+(2)}$, $b(\partial_\theta)=b_0^{-(1)}+b_0^{-(2)}$: two $b$'s on two BPZ bivectors, $S_B=12-2=10$, $\gamma=0$. Sharing the moduli between strands costs exactly the two antighosts that separate $\gamma=-2$ from $\gamma=0$.
9b. Shared $s$ only: $b_0^{+(1)}+b_0^{+(2)}$ plus $b_0^{-(1)}b_0^{-(2)}$: $S_B=9$, $\gamma=-1$.
10. (1.1) with $n_b=6g-6+8$, $n_c=0$: $S=6-6g+6g+2=8$; $\gamma=10-8=+2$. Genus-independent.
11. No insertions: $S=6$, $\gamma=+4$.
12. Same insertions as 10 at $g=0$; a slice, not an integral: $S=8$, $\gamma=+2$.
13. 022 eq. (2.2) via (1.5) (shown in §1.2); the antighost count is the moduli count of every integrated piece plus one $b_0^-$ per frozen node plus two per smoothed handle.
14. Each extra $b$ beyond the moduli measure (a $b_{-n}$ acting on a leg $=\oint v\,b$ around that puncture; or a $b$ on a contour not tied to a Beltrami direction) raises $S$ by one and lowers $\gamma$ by one; $n_x<0$ for extra $c$'s. $n_x=4$ reaches $\gamma=-2$. See §2 for why 022's class excludes this row by definition.
15. $\omega_1$ pairs at 5, two of them: $S=10$; as the identity map, $\gamma=0$.
16. R23's anchor; from (1.2): $\gamma=10-8=+2$.
17. $\gamma=-\gamma(m_2)=-2$ (022 eq. 2.1); (1.2)–(1.3) give $S=12$, $S_B=8$.

**Reading of the table (for 12b/12c).** Among elementary geometric objects, exactly two
rows have the target $\gamma=-2$ *with moduli*: the double tubes 7 and 8 (two independent
length moduli, two independent $b_0^+$). Row 14 reaches $-2$ only by four $b_0^+$ on its legs (eight zero modes with the $b_0^-$'s): plumbing fixtures on the external legs, not moduli of the kernel's own surface *(replaces "four non-moduli $b$ insertions", 2026-10-10, node check F2)*. Every connected kernel with only moduli-type antighosts sits at $\gamma\ge2$
(rows 10–13). Every "diagonal" or shared-modulus object is short by one or two antighosts
(rows 9a, 9b). Hence the ghost-number filter alone already says: **a geometric $1/m_2$ must
carry two independent $b_0^+$ zero-mode insertions, one per strand — i.e. two independent
length moduli (or their unsoaked remnants, row 5$^{\otimes2}$) — and any surface glued in on
top must be ghost-neutral.** Whether such an object can also be *connected* is the question
of §2 and 12b.

### 1.4 Checks of the table, and the two limiting cases

**(a) Against R23.** Row 16: $\gamma(m_2)=+2$ ✓ (R23's anchor, reproduced by (1.2) from
$S(V_4)=8$, $\ell=2$). Row 17: $-2$ ✓ (022 eq. 2.1). The general R23 formula follows from
(1.2) with the frozen-handle saturation $S=2(k+\ell)-g$: $\gamma=5\ell-2k-2\ell+g=3\ell-2k+g$ ✓;
the $\ell=1$ slice is the book's `bos:eq:Ngh-bracket-state` ($3-2n$, genus-independent
*there* because the book's $\ell_{g,n}$ integrates all handles — row 10's convention, not
R23's; the two agree at $g=0$ and differ by the frozen/smoothed distinction of §1.2 at
$g>0$; neither is wrong).

**(b) Against 022 eq. (2.2).** Row 13 = (2.2) identically (§1.2). For every object *inside*
022's class the table and 022 agree. Two places where 022's **prose** is imprecise, neither
affecting R28 as a theorem but both relevant to Task 12:

- 022 §2.4: "an unmatched $b_0^+$ zero mode not soaked by a modulus integral annihilates the
  correlator" — **not correct as stated.** Row 5, $b_0^+b_0^-\delta_{L_0^-,0}$, is a non-zero
  bivector: $b_0^+b_0^-$ maps $\uparrow\uparrow\to\downarrow\downarrow$ (021 §4.2), the two inserted
  states are field-type, $S_B=4$, and the object equals $\partial_\lambda\mathsf P_{[0,\lambda]}
  \big|_{\lambda=0}$ — the boundary term of a Feynman region, which is exactly the
  $\lambda$-derivative of a stubbed vertex in the Erbin–Fırat mechanism, manifestly non-zero.
  What is true: $b_0^+$ annihilates a state *already restricted to* $\mathcal H_0$; the sewing sum
  runs over all of $\mathcal H$. 022's ghost arithmetic for this node (ghost-neutral in the
  telescoping, $-4+4=0$) is right; only the non-vanishing remark is wrong, and R28's floor
  $\gamma\ge2$ never used it. **Consequence:** candidate (c), half-frozen kernels, is live at
  the ghost-number level (row 5$^{\otimes2}$ has $\gamma=-2$) and must be treated in 12b on
  its merits, not dismissed by 022 §2.4.
- 022 §2.3 Theorem, second sentence ("no honest CFT surface correlator — of any genus, with
  any number of frozen nodes …, any smoothed handles, and any continuous moduli — can equal a
  … operator of ghost number $-2$"): true only with the Definition's item 3 read strictly
  (antighosts = moduli-saturating $b(\mu_i)$ + node insertions). Row 14 objects are honest
  correlators with $\gamma=2-n_x$; they are outside the class by *definition*, and what
  excludes them is 022 Angle 2 (bounded-topology kernels are polynomial in $V_4$'s matrix
  elements), not Angle 1. The ledger text of R28 should say so (12d).

**(c) Limiting case 1 — the frozen limit of the bounded tube.** With $\omega_1^{-1}$ factored
out (C5),
$$
\mathsf P_{[0,\lambda]}=b_0^+\!\int_0^\lambda\! ds\,e^{-sL_0^+}\;\omega_1^{-1},
\qquad
\frac{1-e^{-\lambda L_0^+}}{L_0^+}=\lambda-\frac{\lambda^2}{2}L_0^++O(\lambda^3),
\tag{1.6}
$$
regular at $L_0^+=0$ (the closed-string form of R3's mechanism). Two distinct "frozen
limits" exist and the table keeps them apart:
- *slice*: take the integrand at $s=0$ and drop the antighost of the modulus no longer
  integrated — gives $\omega_1^{-1}$, row 1, $\gamma=0$: **R27's frozen node** ✓;
- *shrink*: $\lim_{\lambda\to0}\lambda^{-1}\mathsf P_{[0,\lambda]}=b_0^+\omega_1^{-1}$, row 5,
  $\gamma=-1$: the doubly-frozen node, one antighost more than moduli.
The difference between the two is one $b_0^+$, i.e. one unit of $\gamma$ — the rule
"insertions count, integrations do not" in its simplest instance. Machine check: script
part 1, checks `frozen-slice` and `frozen-shrink` on a random finite spectrum.

**(d) Limiting case 2 — the open-string (Erbin–Fırat) count, via (C7).** Open auxiliary
$\Sigma\in\mathcal H$, $N_{\rm gh}=1$; kinetic operator $Q_B/(1-e^{-2\lambda L_0})$, $\gamma=+1$;
Siegel-gauge propagator $b_0(1-e^{-2\lambda L_0})/L_0$, $\gamma=N^{\rm op}=-1$; one real
modulus (strip length $\in[0,2\lambda]$), one antighost; $\gamma_{\rm kin}+\gamma_{\rm prop}=0$ ✓.
The same rule applied per closed strand gives kinetic $c_0^+L_0^+/(1-e^{-\lambda L_0^+})$ with
$\gamma=+1$ and propagator $\hat{\mathsf P}_{[0,\lambda]}$ with $\gamma=-1$; on two strands,
$\gamma=+2=\gamma(m_2)$ and $-2=\gamma(m_2^{-1})$. So a change of kinetic term of
Erbin–Fırat type (candidate (e)) is **ghost-number consistent** with the $\Sigma$ sector as it
stands — the reason it survives to 12c. (Aside: the review's transfer-table guess
"$(c_0^-L_0^-)/(1-\text{collar})$" for the closed kinetic operator is not the right analogue;
by (C5) it is $c_0^+L_0^+$ that pairs with $b_0^+/L_0^+$.)

## 2. R28's class restated: excluded versus not covered

### 2.1 The class (022 Definition (1.1), quoted in compressed form)

$m_2^{-1}\overset{?}{=}\int_Xd\mu(x)\,\widetilde K(x)$ with: (1) $X$ finite-dimensional real,
may reach nodal strata; (2) each $\Sigma(x)$ *a* (possibly nodal) surface with the four
external punctures, any genus, $\nu(x)$ internal nodes; (3) $\widetilde K(x)$ = surface state
$\times$ moduli-saturating antighosts $b(\mu_i)$, one per integrated real modulus, $\times$ at
each node the standard sewing insertion ($\omega_1^{-1}$ frozen, $\mathsf P$ smoothed);
(4) $d\mu$ a real signed measure; (5) bounded topological type. Proven there:
$\gamma(\widetilde K)=2+\nu_f\ge2\ne-2$ (Angle 1); a bounded-topology kernel is polynomial in
$V_4$'s matrix elements and cannot carry the pole of $V_4^{-1}$ (Angle 2).

### 2.2 Excluded (by proof) versus not covered (by definition)

| candidate (§0 row) | in 022's class? | ghost number (§1.3) | what obstructs, if anything is known |
|---|---|---|---|
| connected assemblies of vertex regions, frozen/smoothed nodes, all Beltrami antighosts | **yes** | $2+\nu_f$ | **excluded** by Angle 1 (R28) |
| (a) diagonal double tube, rows 9a/9b | no — item (2) requires *one* surface; a double tube is two disjoint cylinders | $0$ / $-1$ | **excluded by ghost number alone** (this record): sharing a length between the strands removes one $b_0^+$; sharing the twist removes one $b_0^-$; each costs one unit of $\gamma$ |
| (b) double tube, rows 7/8 | no (disconnected) | $-2$ ✓ | ghost obstruction **does not apply**. What does: *factorisation*. $K=\hat k\otimes\hat k$ (symmetrised) inverts $m_2$ iff $V_4(A_1A_2;A_3A_4)=\omega_1(A_1,\hat k^{-1}A_3)\,\omega_1(A_2,\hat k^{-1}A_4)+$sym, i.e. iff the $\mathcal V_{0,4}$ correlator factorises into two 2-point forms — a rank/Schmidt-rank statement across the two strands, testable on a level-truncated $V_4$. For row 7 additionally the $1/L_0^+$ poles (absent in $m_2^{-1}$, cf. R3); row 8 is pole-free, so only factorisation stands. **12b.** |
| (c) half-frozen kernels | partly: un-integrating a Beltrami modulus while keeping its $b$ is *not* in item (3) | connected: $\ge2$ (Lemma 2.1); disconnected, row 5$^{\otimes2}$: $-2$ | connected case **excluded** by Lemma 2.1 below (extends R28); disconnected case reduces to (b)'s factorisation obstruction. 022 §2.4's "annihilates" remark is not the obstruction (§1.4(b)). **12b** for the disconnected case. |
| (d) explicit non-sewing ghost insertions, row 14 | no — item (3) allows only Beltrami and node antighosts | $2-n_x$, any value | ghost obstruction **void**. Expected obstruction: Angle 2 — a $b$-mode on a leg ($\oint v\,b$ = trivial Beltrami) keeps the kernel *linear* in $V_4$'s matrix elements, so it cannot carry the pole of $V_4^{-1}$; to be made precise in **12b** (state the linearity, exhibit a failing leg). |
| (T1) bounded plumbing neck (single connected neck between two vertex regions) | yes if the vertex regions are 022-vertices | $2+\nu_f$ | excluded by Angle 1 as a *connected* object. Reopened only in the sense of (b)/(e): a *double* bounded neck. **12b.** |
| (T2) Laplace integrand $e^{-tm_2}$ as a surface family | no — $t$ is not a modulus of any surface | see Lemma 2.2 | **excluded by grading** (Lemma 2.2 restates 020 §8's T2 refutation; the caveat on sector identification below is new). |
| (e) change of kinetic term (Erbin–Fırat type) | not applicable — R28 concerns the inverse of the *given* $m_2=G_2^{-1}V_4$ | kinetic $+2$, propagator $-2$ (§1.4(d)) | ghost-consistent; the question is whether a closed-string $V_4$ factorises through a bounded double tube between two $\mathrm{Sym}^2$-valued vertices, and at what genus/coupling the resulting exchange sits (R27: a two-strand tube between two spheres is genus 1). **12c.** |

**Lemma 2.1 (connected kernels have $\gamma\ge2$ whatever is integrated).** On a connected
$\Sigma_{g,4}$ the antighost insertions available to a kernel in 022's item (3) are
$b(\mu)$ for Beltrami classes $\mu\in H^1(T\Sigma(-\sum p_i))$, of real dimension
$\dim_\R\mathcal M_{g,4}=6g+2$; trivial classes $\mu=\bar\partial v$ give $b(\bar\partial v)=\oint v\,b$,
which acts on the leg states (row 14, outside item (3)). By linearity of $b(\mu)$ in
$\mu$, a product of more than $\dim_\R\mathcal M_{g,4}=6g+2$ such factors contains a
linearly dependent one and vanishes by Grassmann oddness; hence $n_b\le6g+2$. Nodes add $\mathsf P$ ($S_B=4$, ghost-neutral
relative to the two legs it fills), $b_0^+b_0^-\delta$ (also $S_B=4$) or $\omega_1^{-1}$
($S_B=5$, $+1$). By (1.5), $\gamma=10-\big[\sum_{\rm pieces}(6-6g_p+n_{b,p})-\sum_{\rm nodes}S_B\big]$
is minimised when every piece carries its full Beltrami measure and every node is
ghost-neutral, which is row 10/13 with $\nu_f=0$: $\gamma=2$. Un-integrating never changes
$n_b$; dropping a $b$ raises $\gamma$. Hence $\gamma\ge2$. ∎ (Machine check: script part 1,
`lemma-2.1-floor`, random graphs with random subsets of moduli un-integrated.)

**Lemma 2.2 (the Laplace parameter must carry $N_{\rm gh}=-2$; restates 020 §8's T2
refutation "refuted by ghost counting" — the caveat below is new).** $\gamma(m_2)=+2$, so
$m_2^n$ has $\gamma=2n$ and $e^{-tm_2}=\sum_n(-t)^nm_2^n/n!$ is ghost-homogeneous only if
$\gamma(t)=-2$. A worldsheet length or any real modulus has $\gamma=0$. Therefore no
identification of $t$ with a modulus of a surface family is compatible with the grading:
T2 is excluded by ghost number, independently of the spectral conditions of R15. ∎
*Caveat (for 12b and the ledger):* the same argument shows $m_2$ maps the $N_{\rm gh}=4$ sector
of $\mathrm{Sym}^2\mathcal H_0$ to the $N_{\rm gh}=6$ sector, so on any ghost-graded truncation
$m_2$ is nilpotent and $m_2^{-1}$ is the inverse of the *rectangular block* $4\to6$. The
"spectrum of $m_2$" of R15/R27(iii)/RS6 is the spectrum of the matrix of $V_4$ under a
non-canonical identification of the 4- and 6-sectors (a metric on $\mathcal H_0$). This does
not affect R28, but the Laplace form's status should be restated with this proviso (12d).

### 2.3 Row set for §0 and the agenda of 12b/12c

The §0 rows are exactly the candidates of §2.2. 12b takes (a)–(d) and T1/T2 with the
obstructions named above to be either proven (factorisation test for (b)/(c), linearity for
(d)) or turned into a construction; 12c takes (e) and the toy. The ghost-number filter of
§1.3 is the entrance condition for every candidate: **two independent $b_0^+$ (one per
strand) and nothing ghost-positive glued in on top.**

## Working notes (12a)

None outstanding: all intermediate results were consolidated into §1–§2.

## Verification (12a)

Script `codes/verify-geometric-inverse.py`, part 1, seed 20260908, **68/68 PASS**, exit 0.
- Every §1.3 row recomputed by rule (1.5) (surfaces) or (1.3) (bivectors), and independently
  by (1.4) ($N^{\rm op}+\ell$) where the row is a sewing operator; 4-form column by (1.2).
- Rows 15–17 and R23's formula from (1.2) with $S=2(k+\ell)-g$ (50 random $(k,\ell,g)$).
- 022 eq. (2.2): 022's leg-telescoping constants and rule (1.5) are the same polynomial
  (equivalence proven in §1.2), so their agreement on 2330 random 022-class graphs is a
  **transcription/arithmetic check** — it catches typos, not an independent derivation —
  and likewise for the Lemma 2.1 floor $\gamma\ge2$ leg and the "R27 freezing (dropping $k$
  antighosts) raises $\gamma$ by exactly $k$" leg, both arithmetic identities of rule
  (1.5); the break-on-purpose legs below confirm exactly that these catch transcription
  errors, nothing more.
- Frozen limit (1.6) on the explicit zero-mode Fock space $\otimes$ a random 5-level $L_0^+$:
  shrink limit $=\lambda\,b_0^+\omega_1^{-1}$ (rel. err $<10^{-3}$ at $\lambda=10^{-4}$), ghost
  shifts $-2$ (shrink) vs $-1$ (slice) measured with the zero-mode ghost-number operator;
  regularity at $L_0^+\to0$; series to $O(\lambda^3)$.
- Open-string (C7) count; Lemma 2.2 on a graded toy ($[N,m_2]=2m_2$, $m_2^2=0$, $e^{-tm_2}$
  inhomogeneous, block $6\to4$ invertible) — decorative: true for any grading-raising
  nilpotent, not specific to $m_2$.
- Break-on-purpose: mis-counted diagonal tube (4 $b$'s) caught; sphere with one antighost
  dropped caught; 022 constant $+5\to+4$ breaks the two-bookkeeping agreement; shrink limit
  $\ne\omega_1^{-1}$ alone.
- One FAIL on the first run, diagnosed as a typo in the *check* (helper computed
  $(1-e^{-\lambda L})/(\lambda L)$); fixed, no change to any result.
- Not machine-checked: the Beltrami-dimension input of Lemma 2.1 ($n_b\le\dim_\R\mathcal M$ on
  a connected surface, trivial classes act on legs) — standard Riemann–Roch, taken from the
  literature; and Lemma 2.2's caveat on sector identification (a statement about what R15's
  "spectrum" means, not a computation).

## 3. Candidates (a)–(d) outside R28's class, and T1/T2 reopened (12b)

**Literal task (12b).** For each of (a) disconnected/product kernels, (b) half-frozen
kernels (Harold's 2024 diagonal double tube), (c) explicit non-sewing ghost insertions,
(d) the Laplace integrand $e^{-tm_2}$ read as a surface family: carry the candidate to a
construction or to an obstruction, with ghost count (§1.3 rows), moduli count, and a boxed
verdict; then reopen T1 and T2 of 020 §8 as "original objection → what is different now →
verdict". Fill the §0 rows. Conventions: §1.1 (C1)–(C7), translations (1.2)–(1.5), verbatim.

**Objective served.** The map of geometric options for the auxiliary channel; the
answer here is *which* of (α)/(β)/(γ) each candidate feeds, not "R28 stands". Note that
the brief's labels differ from §0's: brief (a) = product kernels = §0 row (b); brief (b) =
half-frozen = §0 rows (a)+(c); brief (c) = explicit ghosts = §0 row (d); brief (d) = Laplace
integrand = §0 row (T2). The subsections below follow the **brief's** lettering and name the
§0 row they fill.

### 3.1 (a) Disconnected kernels: products of single-strand propagators [§0 row (b)]

**Setup.** A product kernel is $K=\hat k\otimes\hat k$ restricted to $\mathrm{Sym}^2\mathcal H_0$,
with $\hat k:\mathcal H_0\to\mathcal H_0$ a single-strand map of $\gamma=-1$ — rows 2, 4 of
§1.3 ($b_0^+/L_0^+$, $b_0^+(1-e^{-\lambda L_0^+})/L_0^+$), or any of these composed with a
ghost-neutral single-strand surface (a 2-punctured surface with all moduli integrated has
$\gamma=5-2\cdot2=+1$ by (1.2) with $\ell=1$, $S=4$; composed with one $\hat{\mathsf P}$ it
is $0$, so "vertex insertions on a strand" never change the count below and are covered
by the same argument). $K$ has $\gamma=-2$ (row 7/8) and, per strand, $n_b=2$, $n_\mu=2$
(length, twist): **4 real moduli in total**, two more than $V_4$ has. Proposition 3.1
below is proven for this single-kernel form only. The *polarised* sum
$\hat k_1\otimes\hat k_2+\hat k_2\otimes\hat k_1$ is not covered by it: its undressed case
(both $\hat k_i$ functions of $L_0^+$) falls to the commutant obstruction of Prop. 3.2
(§3.2), and its *dressed* case (a strand operator built from a 2-punctured surface that
need not commute with $L_0^+$) is excluded only as a uniform construction, by the scaling
lemma of §5.6.

Sector bookkeeping (needed once, then used silently): $\mathcal H_0=\ker L_0^-\cap\ker b_0^-$
is spanned by the zero-mode sectors $\downarrow\downarrow$ and $c_0^+\downarrow\downarrow$
(since $\{b_0^-,c_0^+\}=0$). $b_0^+$ kills $\downarrow\downarrow$ and maps
$c_0^+\downarrow\downarrow\to\downarrow\downarrow$ bijectively; so $\hat k$ is a bijection
$(\mathcal H_0)_3:=c_0^+(\mathcal H_0)_2\to(\mathcal H_0)_2$ whenever its $L_0^+$-function has
no zero on the spectrum ($1/L_0^+$: off-shell; $(1-e^{-\lambda L_0^+})/L_0^+$: always, real
spectrum). This is the same rectangular-block structure as Lemma 2.2's caveat: $m_2^{-1}$
maps $\mathrm{Sym}^2(\mathcal H_0)_3\to\mathrm{Sym}^2(\mathcal H_0)_2$, and so does $K$. Write
$\hat k^{-1}:(\mathcal H_0)_2\to(\mathcal H_0)_3$ for the block inverse and define the
bilinear form on the field sector
$$
\beta(B,C):=\omega_1\big(B,\hat k^{-1}C\big),\qquad B,C\in(\mathcal H_0)_2 ,
\tag{3.1}
$$
non-degenerate ($\omega_1$ pairs 2 with 3 non-degenerately, $\hat k^{-1}$ is a bijection),
and BPZ-symmetric or antisymmetric ($\hat k^{-1}=c_0^+f(L_0^+)$ with $f$ BPZ-even; the sign
is convention-dependent and both cases are treated).

**Derivation.** $m_2K=\mathrm{id}$ on $\mathrm{Sym}^2(\mathcal H_0)_3$ reads
$V_4(P,KQ)=G_2(P,Q)$ for all $P\in\mathrm{Sym}^2(\mathcal H_0)_2$, $Q\in\mathrm{Sym}^2(\mathcal H_0)_3$.
Put $P=B_1B_2$, $Q=\hat k^{-1}C_1\,\hat k^{-1}C_2$ (symmetric products), so $KQ=C_1C_2$ and
$G_2(P,Q)=\beta(B_1,C_1)\beta(B_2,C_2)+\beta(B_1,C_2)\beta(B_2,C_1)$ (the normalisation of the
symmetric product is common to both sides). Hence the product kernel inverts $m_2$ iff
$$
V_4(B_1,B_2,C_1,C_2)=\beta_{13}\beta_{24}+\beta_{14}\beta_{23},
\qquad \beta_{ij}:=\beta(X_i,X_j),\ (X_1..X_4)=(B_1,B_2,C_1,C_2),
\tag{3.2}
$$
for all field-sector arguments. The left side is $S_4$-symmetric (closed-string vertex on
Grassmann-even fields). Apply the transposition $(23)$, $B_2\leftrightarrow C_1$, to the
right side and demand equality:
$$
\beta_{13}\beta_{24}+\beta_{14}\beta_{23}=\beta_{12}\beta_{34}+\beta_{14}\beta_{32}.
\tag{3.3}
$$
*Case $\beta$ symmetric.* The $\beta_{14}$ terms cancel: $\beta_{13}\beta_{24}=\beta_{12}\beta_{34}$.
Set $X_2=X_4=X$, $X_1=Y$, $X_3=Z$: $\beta(Y,Z)\,\beta(X,X)=\beta(Y,X)\,\beta(Z,X)$. A non-zero
symmetric form has some $X$ with $\beta(X,X)\ne0$ (polarisation), so
$\beta(Y,Z)=\beta(Y,X)\beta(Z,X)/\beta(X,X)$: $\beta$ has rank one. Non-degenerate and rank
one forces $\dim(\mathcal H_0)_2=1$.
*Case $\beta$ antisymmetric.* (3.3) becomes $\beta_{13}\beta_{24}+2\beta_{14}\beta_{23}-\beta_{12}\beta_{34}=0$;
set $X_1=X_3=X$ (so $\beta_{13}=0$): $2\beta(X,X_4)\beta(X_2,X)-\beta(X,X_2)\beta(X,X_4)
=3\beta(X,X_4)\beta(X_2,X)=0$ for all $X,X_2,X_4$, so $\beta=0$, contradicting non-degeneracy.

**Result (Proposition 3.1).** *A product kernel $\hat k\otimes\hat k$ — with $\hat k$ any
single-strand object whose block $(\mathcal H_0)_3\to(\mathcal H_0)_2$ is invertible, bounded
or unbounded, dressed or not — inverts an $S_4$-symmetric $V_4$ only if the field sector
(modulo $\ker V_4$) is one-dimensional.* The obstruction is **rank across the strands**:
(3.2) says $V_4$'s (13)(24)-flattening is "one product plus its swap", i.e. operator Schmidt
rank $\le2$ across the strand cut, whereas $S_4$ symmetry forces the same tensor to have
that structure in the (12)(34) and (14)(23) cuts too, which (3.3) shows is impossible above
rank one. In words: $V_4$ *does not factorise on unentangled states*; the
exchange $\Sigma$ carries genuine entanglement between its two strands, and a product of
tubes has none. $\boxed{\text{(a) product kernels: obstruction, }\gamma=-2\ \checkmark,\ 4\text{ moduli }(\ne2),\ \text{rank}>1\text{ across the strands (Prop. 3.1)}}$

**Two further, independent obstructions for the unbounded product (row 7).** (i) *Poles.*
$\hat{\mathsf P}\otimes\hat{\mathsf P}$ carries $1/(L_0^{+(1)}L_0^{+(2)})$: as a function of the
external momenta the left side of (3.2) would have a double pole where both strands are
on-shell, while $m_2^{-1}=V_4^{-1}G_2$ has its singularities at $\det V_4=0$, not at
$L_0^{+(i)}=0$ — which is all the argument below uses. So row 7 fails already as a function, before any rank
consideration — the same reason the Erbin–Fırat construction uses the *bounded* strip.
(ii) *Level matching.* $\hat{\mathsf P}^{\otimes2}$ imposes $L_0^{-(1)}=L_0^{-(2)}=0$ per strand, which
is what $\mathrm{Sym}^2\mathcal H_0$ requires; fine for (a), but note for §3.2 that the diagonal
tube imposes only $L_0^{-(1)}+L_0^{-(2)}=0$ and therefore does not even act on $\mathrm{Sym}^2\mathcal H_0$.

**Sums of product kernels — what evades Prop. 3.1 and at what price.** Polarised products
$\hat k_1\otimes\hat k_2+\hat k_2\otimes\hat k_1$ span the symmetric part of
$\mathrm{End}(\mathcal H_0)^{\otimes2}$, whose restriction to $\mathrm{Sym}^2\mathcal H_0$ is *all* of
$\mathrm{End}(\mathrm{Sym}^2\mathcal H_0)$ (surjectivity: an element of
$\mathrm{Sym}^2V\otimes\mathrm{Sym}^2V^*$ is invariant under the simultaneous swap and is its
own image under $P_{12}P_{34}$; dimensions $d^2(d^2+1)/2\ge[d(d+1)/2]^2$ for all $d$). So a
*finite sum* of products always exists algebraically — with $V_4$-dependent coefficients and
factors. The minimal number of terms is the symmetric operator Schmidt rank of $m_2^{-1}$
across the strands, $\ge2$ by Prop. 3.1 and generically $\binom{d+1}{2}$-ish (12c's toy can
measure it); no term is preferred, no continuous modulus appears. The Neumann chain R27
$\sum_n(D^{-1}N)^nD^{-1}$ is such a sum when $D$ is chosen strand-factorised (e.g.
$D=G_2^{-1}\times$ the strand-diagonal part of $V_4$, itself of the form $\hat d\otimes\hat d$ on
a level basis): then $D^{-1}=\hat d^{-1}\otimes\hat d^{-1}$ *is* a product kernel and each
$N$ is a frozen-neck sphere. **Price:** (1) the factors $\hat d^{-1}$ are $V_4$-data, not
surface data (no $b_0^+$, no length: $\gamma(\hat d^{-1})=-1$ is carried by the inverse of a
diagonal *vertex* block, not by an antighost); (2) the sum is discrete and scheme-dependent
($D$ is a choice); (3) convergence $\rho(D^{-1}N)<1$ is exactly the spectral condition
R15 attaches to the Laplace form. This is the *only* way product kernels enter $m_2^{-1}$,
and it is R27's representation (ii), not a new one.

**Moduli count, restated for §0.** Product of two tubes: 4 real moduli, all integrated,
against the 2 of $V_4$; the 2 extra are not "cancelled" by anything — Prop. 3.1 shows no
choice of the single-strand measure (the function $f(L_0^+)$ in $\hat k=b_0^+f(L_0^+)$) repairs
the rank, so the surplus of moduli is a symptom, not the cause. Machine check: script part
2, `prod-rank-S4`, `prod-rank-d1-control`, `prod-sum-spans`.

### 3.2 (b) Half-frozen kernels: the diagonal double tube and its relatives [§0 rows (a), (c)]

**The 2024 shared-parameter proposal** (`hb_sft_action.tex` §Worldsheet interpretation):
glue two 4-punctured spheres on two punctures at once by $z_2^{(1)}z_2^{(2)}=f(q)$
with *one* gluing parameter; the notes already record (i) two independent parameters give 4 moduli
instead of 2, (ii) setting them equal gives loop-building configurations, and (§Trivial kinetic term) (iii) a trivial $\Sigma$ propagator
(fixed twist and length) gives the wrong ghost number, repairable by $\ell_1'=c_0^-$. All
three points are confirmed and sharpened by the table: (i) = rows 7/8 (4 moduli), (ii) =
R27's genus formula (a two-strand tube between two spheres is genus 1; the shared-parameter
family is a 2-real-dimensional slice of $\mathcal M_{1,4}$, $\dim_\R=8$, with six Beltrami
directions dropped *together with their antighosts*), (iii) = rows 9a/9b ($\gamma=0,-1$, short
of $-2$ by exactly the antighosts of the dropped directions).

**Three objects, kept apart.** With $L_i:=L_0^{+(i)}$, $b_i:=b_0^{+(i)}$, all with the
per-strand twist projection $(\omega_1^{-1})^{\otimes2}=G_2^{-1}$ factored out:
- **9a/9b, Harold's diagonal tube:** $\hat D_{\rm diag}=(b_1+b_2)/(L_1+L_2)$ — the Beltrami
  antighost of the *shared* length direction is $b(\partial_s)=b_1+b_2$; one $b^+$ for one
  length. $\gamma=-1$ as a map on $\mathcal H_0^{\otimes2}$ (9b); 9a shares the twist as well,
  keeps only $b_0^{-(1)}+b_0^{-(2)}$ and projects on $L_0^{-(1)}+L_0^{-(2)}=0$ only, so it does
  not act on $\mathrm{Sym}^2\mathcal H_0$ at all (one $c_0^-$ of $G_2$ finds no $b_0^-$): it lives on
  the larger *pair-level-matched* space $\ker(L_0^{-(1)}+L_0^{-(2)})\cap\ker(b_0^{-(1)}+b_0^{-(2)})$.
- **half-frozen product,** row 5$^{\otimes2}$: $b_1b_2\,e^{-s_1L_1-s_2L_2}$ at frozen $s_1,s_2$
  (or $b_1b_2e^{-s(L_1+L_2)}$ at one frozen $s$): 2 antighosts, 0 length moduli; $\gamma=-2$ ✓.
- **correlated double tube,** the general two-length family with a joint measure:
  $$
  \hat K_\mu=b_1b_2\,g(L_1,L_2),\qquad g(L_1,L_2)=\int ds_1ds_2\,\mu(s_1,s_2)\,e^{-s_1L_1-s_2L_2},
  \tag{3.4}
  $$
  $\gamma=-2$ ✓ for every $\mu$. $\mu=\mu_1\otimes\mu_2$ is §3.1's product; $\mu=\delta(s_1-s_2)\chi_{[0,\lambda]}$
  is the *correctly antighosted* diagonal tube $b_1b_2(1-e^{-\lambda(L_1+L_2)})/(L_1+L_2)$ —
  the shared-parameter tube with **both** $b^+$ kept, which is $b_1\hat D_{\rm diag}$:
  one Beltrami antighost plus one extra insertion (a candidate-(c) object, cf. §3.3), 3
  integrated moduli (one length, two twists) against 4 antighosts — the honest "half-frozen"
  kernel of the brief. Note $b_1(b_1+b_2)=(b_1+b_2)b_2=b_1b_2$: which strand carries the
  extra $b$ is immaterial.

**Legitimacy of a frozen $b_0^+e^{-sL_0^+}$.** As an operator it is non-zero and equals
$\partial_\lambda\mathsf P_{[0,\lambda]}|_{\lambda=s}$ (§1.4(b)); BRST: $[Q,b_0^+e^{-sL_0^+}]
=L_0^+e^{-sL_0^+}=-\partial_se^{-sL_0^+}$, a total $s$-derivative. Integrated over $[0,\lambda]$
this is the boundary term $1-e^{-\lambda L_0^+}$ that the Erbin–Fırat stubbed vertex absorbs
(R3, $\{Q,P_{[0,2\lambda]}\}=1-e^{-2\lambda L_0}$); at frozen $s$ nothing is integrated and
$[Q,\cdot]\ne0$ with no vertex to absorb it. Inside an HS action the auxiliary is
integrated out exactly, so what gauge invariance of $S_{\rm eff}$ requires is that the
composite $V_3'\circ K\circ V_3'$ satisfy the $L_\infty$ relation with the other vertices;
$[Q,K]\ne0$ must then be cancelled by the $Q$-variation of the $\Sigma\Psi\Psi$ vertices,
i.e. the vertex family must have $-\partial_s(\text{stub})$ as its BRST variation. The
natural mechanism for this is that the vertices are themselves $s$-dependent stubbed
vertices — the Erbin–Fırat mechanism again, with the frozen insertion as the derivative
of the bounded one (asserted as the natural route here, not derived as the only
possibility). **Verdict on legitimacy:** admissible as an insertion, not as a stand-alone
propagator; it can appear as a factor ($\partial_\lambda$ of a bounded-tube propagator) but
its use as *the* propagator requires the change of kinetic term of candidate (e), 12c.

**Derivation of the obstruction for the whole family (3.4).** Every object above is built
from $b_0^{\pm(i)}$ and functions of $L_0^{\pm(i)}$ only, hence commutes with $L_1$, $L_2$ (and
on $\mathrm{Sym}^2$ with the symmetric functions $L_1+L_2$, $L_1L_2$). If $\hat K_\mu m_2=\mathrm{id}$
on the $4\to6$ block then $m_2=\hat K_\mu^{-1}$ on that block also commutes with them, so
$$
V_4(P,Q)=G_2(P,m_2Q)=0\quad\text{unless}\quad e_j(L)\big|_P=e_j(L)\big|_Q,\ j=1,2 ,
\tag{3.5}
$$
for $L_0^+$-eigenvectors $P,Q\in\mathrm{Sym}^2(\mathcal H_0)_2$ ($G_2$ pairs equal $L_0$'s). Explicitly,
in an $L_0^+$-eigenbasis with $\eta_{BC}:=\omega_1(B,c_0^+C)$,
$$
V_4(B_1,B_2,C_1,C_2)\;=\;\frac{\eta_{B_1C_1}\eta_{B_2C_2}+\eta_{B_1C_2}\eta_{B_2C_1}}{g(L_{C_1},L_{C_2})}
\tag{3.6}
$$
— $V_4$ would have to be *diagonal in the BPZ-pair basis with entries depending only on the
$L_0^+$ eigenvalues*. Take four tachyons $T(k_i)$ with $\sum k_i=0$, $P=T(k_1)T(k_2)$,
$Q=T(k_3)T(k_4)$: $e_1(L)|_P=\tfrac{\alpha'}{4}(k_1^2+k_2^2)-2$, and (3.5) demands
$V_4(T_1..T_4)=0$ whenever $k_1^2+k_2^2\ne k_3^2+k_4^2$ — false: the vertex-region integral of
four tachyons is non-zero at generic momenta (R15's level-0 non-vanishing is its
equal-momentum instance). Hence no $\mu$ in (3.4) works.

**Result (Proposition 3.2, commutant obstruction).** *Any two-strand kernel built from
zero modes $b_0^{\pm(i)}$ and functions of $L_0^{\pm(i)}$ alone — products, bounded products,
half-frozen products, Harold's diagonal tube with or without the extra antighost, any
correlated measure $\mu(s_1,s_2)$ — commutes with the strand $L_0^+$'s, while $m_2^{-1}$ does
not (3.5). Such a kernel can invert $m_2$ only if $V_4$ is level-diagonal per strand, which
it is not.* The obstruction is independent of the ghost count (it kills the
$\gamma=-2$ members as well as 9a/9b) and of the moduli count. It is *not* an
obstruction to using such a tube as the propagator of a **differently defined** auxiliary
(case (β)/(e)): there the kinetic term is defined as $\hat K_\mu^{-1}$, level-diagonal by
construction, and the non-diagonal part of $V_4$ must sit in the two $\Sigma\Psi\Psi$
vertices — exactly where Erbin–Fırat put it ($V_4^{\rm stub}=V_3\circ P_{[0,2\lambda]}\circ V_3$).
$\boxed{\text{(b) half-frozen / diagonal: obstruction as }1/m_2\text{ (Prop. 3.2); }\gamma=-2\text{ only with }b_1b_2\text{, 3 moduli; admissible as a factor / as a redefined propagator}\to\text{12c}}$

**Can a dressing rescue 9a/9b?** By (1.5), $\gamma$ is lowered only by antighost insertions
beyond the moduli measure; any surface glued on (vertices, handles, all integrated) is
ghost-neutral or positive (rows 10, 13). Lowering $\hat D_{\rm diag}$ from $-1$ to $-2$ needs
one extra $b$ on a strand: that is $b_1\hat D_{\rm diag}=\hat K_{\mu=\delta}$, covered by Prop. 3.2.
Dressing with a *connected* surface between the tubes and the vertices gives a connected
kernel, $\gamma\ge2$ by Lemma 2.1. So: no dressing rescues 9a/9b as an inverse of the
present $m_2$ — the §0 row (a) verdict "excluded by ghost number" is confirmed and
strengthened (the ghost-repaired version is excluded by Prop. 3.2). Machine check: script
part 2, `commutant-L0`, `commutant-generic-V4`, `commutant-diag-V4-control`.

### 3.3 (c) Explicit non-sewing ghost insertions [§0 row (d)]

**What the class is.** Row 14: a connected surface family (any genus $g$, all $6g+2$
moduli integrated with their Beltrami antighosts, $\gamma=+2$) carrying $n_x$ further
$b$-mode insertions not tied to any modulus; $\gamma=2-n_x$, target $n_x=4$. Since the
Beltrami classes are already exhausted by the measure (Grassmann-odd $b(\mu)$, one per
class, Lemma 2.1), every further antighost is either $b(\bar\partial v)=\oint v\,b$ for a
trivial class — a mode $\beta=\sum_nv_nb_n$ acting on one leg — or a $b$ on a closed contour
$C$ with a vector field $v$ holomorphic near $C$, which contour-deforms to a sum of leg
actions on the punctures $C$ encloses (plus nothing else: no other insertions on a bare
surface). Hence, after the moduli integral,
$$
K_x(A_1,A_2;A_3,A_4)\;=\;\sum_\alpha\Omega_\alpha\big(\beta^\alpha_1A_1,\beta^\alpha_2A_2,\beta^\alpha_3A_3,\beta^\alpha_4A_4\big),
\qquad\text{map form: }\ \hat K_x=\sum_\alpha B_\alpha^{t}\,\hat\Omega_\alpha\,B'_\alpha ,
\tag{3.7}
$$
with $\Omega_\alpha$ integrated surface forms ($\Omega=V_4$ when the surface is the
$\mathcal V_{0,4}$ region itself; other genera/regions allowed, finitely many),
$\hat\Omega_\alpha=G_2^{-1}\Omega_\alpha$, and $B_\alpha=\beta^\alpha_1\otimes\beta^\alpha_2$,
$B'_\alpha=\beta^\alpha_3\otimes\beta^\alpha_4$ **fixed leg operators**: products of $b$/$c$
modes, universal (they know the ghost CFT and nothing about the matter correlator, the
vertex region, or the momenta). $c$-insertions ($n_x<0$) raise $\gamma$ and go the wrong way
for a $\mathrm{Sym}^2\to\mathrm{Sym}^2$ map of $\gamma=-2$; the one legitimate role of a $c_0^+$ on a
strand is the sector map $(\mathcal H_0)_2\to(\mathcal H_0)_3$ of §3.1, which belongs to the
*kinetic* operator, not to the propagator. The moduli count of (3.7) is $6g+2$ per term —
already $\ne2$ for $g\ge1$; at $g=0$ it is 2, the right number, with $n_b=6$: four more
antighosts than moduli. So (c) passes the ghost and the moduli filters at $g=0$.

**BRST.** For a leg mode $\beta=\oint vb$, $[Q,\beta]=\oint vT=T(v)$, whose action on a leg
is the Schiffer variation of the local coordinate at that puncture; so
$[Q,K_x]=\sum_\alpha\sum_i\Omega_\alpha(\ldots,T(v_i)A_i,\ldots)$ is a derivative of the surface
form with respect to its coordinate data, non-zero in general ($\{Q,b_0^+\}=L_0^+$
vanishes only on-shell). $K_x$ is not $Q$-closed; it could only enter a gauge-invariant
action as a *dressed vertex* whose $Q$-variation is cancelled by neighbouring terms — the
role the R19/R25 dressings play — not as the propagator of a $Q$-compatible kinetic term.

**Derivation of the obstruction (homogeneity in the vertex data).** Suppose $\hat K_x$
inverts $m_2$ for the vertex $V_4$: $m_2\hat K_x=\mathrm{id}$ on the $4\to6$ block. Consider the
one-parameter family $V_4\to\lambda V_4$ (in the theory: the overall normalisation of the
vertex, i.e. $g_s^2$; or any continuous deformation of the vertex region, of the local
coordinates, or of the external momenta — all of which move $V_4$ along a curve in the space
of symmetric forms on $\mathrm{Sym}^2$; the argument below uses only the one-parameter family $tV_4$). Then $m_2\to\lambda m_2$ and $m_2^{-1}\to\lambda^{-1}m_2^{-1}$:
*the true inverse is homogeneous of degree $-1$ in the vertex data.* In (3.7), the
$g=0$ terms with $\Omega=V_4$ scale as $\lambda^{+1}$, and a genus-$g$ term as
$\lambda^{1+g}$ in the $g_s^2$-grading ($g_s^{2+2g}$ for four legs; the leg operators
$B_\alpha,B'_\alpha$ are $\lambda$-independent). Thus
$$
m_2[\lambda V_4]\;\hat K_x[\lambda V_4]\;=\;\sum_\alpha\lambda^{2+g_\alpha}\,m_2B_\alpha^t\hat\Omega_\alpha B'_\alpha
\;\ne\;\mathrm{id}\quad\text{for }\lambda\ne1 ,
\tag{3.8}
$$
even if it equals $\mathrm{id}$ at $\lambda=1$ (no non-empty sum of positive powers is constant
in $\lambda$). This is a **uniformity hypothesis**: the construction is required to invert
$tV_4$ for the whole family $t\ne0$, not merely the actual $V_4$ at $t=1$ — the weakest
uniformity a kernel "built from surface data" can be asked to satisfy, and the same
hypothesis underlies the scaling lemma of §5.6. At $t=1$ a fine-tuned dressing
$m_2B^tm_2B'=\mathrm{id}$ for the *actual* $V_4$ is **not excluded** by this argument: the
script's `explicit-ghost-scaling` leg exhibits exactly such a loophole (an involutive $M$
with $B=B'=1$ satisfies $MB^tMB'=1$ at $\lambda=1$ and fails only at $\lambda=2$). The
same first-order statement without the scaling: for the natural case
$\Omega=V_4$, the condition $MB^tMB'=\mathrm{id}$ along the family $tM$ is violated by the
directional derivative along $\delta M=M$, which gives $2\,\mathrm{id}\ne0$ — again a
statement about a family of $M$'s, not about the single point $M=V_4$. So (c) is excluded
**as a uniform construction** (3.8) — which is 022 Angle 2 made explicit: a
bounded-topology kernel is polynomial (here: linear) in the surface correlator, and
$m_2^{-1}$ has the pole of $V_4^{-1}$ at $\det V_4=0$. The four extra antighosts fix the
*grading*; nothing in (3.7) can produce a *pole* uniformly in the vertex data.

**What identity such an object does satisfy.** With $\Omega=V_4$: $\hat K_x=B^tm_2B'$ is
$m_2$ conjugated by leg operators — a dressed quartic *contact term* $\tilde V_4(\cdot)=
V_4(\beta_1\cdot,\beta_2\cdot,\beta_3\cdot,\beta_4\cdot)$, of the type an R19/R25 dressing
subtracts or adds; it satisfies $m_2\hat K_xm_2=m_2B^tm_2B'm_2$ (a length-3 chain with
insertions), which is the frozen-neck algebra of R27, not an inverse relation. A kernel
of this kind is a *vertex*, not a *propagator*, whatever the antighosts on its legs.

**Result.** $\boxed{\text{(c) explicit ghost insertions: obstruction as a uniform construction — }\gamma=-2\text{ at }n_x=4,\ 2\text{ moduli at }g=0,\ \text{but degree }+1\text{ (not }-1)\text{ uniformly in }tV_4\text{ (3.8); no }t=1\text{ obstruction is exhibited; the object is a dressed vertex}}$
Machine check: script part 2, `explicit-ghost-scaling` (an explicit $B,B'$ and an
involutive $M$ with $MB^tMB'=1$; the identity FAILS at $\lambda=2$), `explicit-ghost-family`
(directional derivative $2\,\mathrm{id}$), and a leg confirming that $B^tm_2B'$ obeys the
chain identity, not the inverse identity, for a random $V_4$.

### 3.4 (d) The Laplace integrand $e^{-tm_2}$ as a surface family [§0 row (T2)]

**What is being asked.** R15/020 (3.2): $m_2^{-1}=\int_0^\infty dt\,e^{-tm_2}$ when
$\mathrm{spec}(m_2)\subset\{\Re>0\}$; unconditionally $\int_0^\infty dt\,m_2e^{-tm_2^2}$. The
question is whether the *integrand* at fixed $t$ is the state of some surface, what $t$
is, and where the spectral condition bites geometrically.

**The integrand as a family.** $m_2^n$ is the length-$n$ chain of frozen-neck 4-punctured
spheres (R27: $n-1$ colour-2 edges, resolved genus $n-1$, no neck moduli, coupling $g_s^{2n}$,
$\gamma=2n$). Hence
$$
e^{-tm_2}=\sum_{n\ge0}\frac{(-t)^n}{n!}\,m_2^n
\tag{3.9}
$$
is a **generating function over chain lengths**: $t$ is a fugacity conjugate to the number
of frozen necks (equivalently, to the resolved genus, or to the power of $g_s^2$), with
Poisson weights. Two comparisons fix its status:
- $e^{-sL_0^+}$ is the state of *one* surface (the cylinder $[0,s]\times S^1$) because its
  generator $L_0^+$ is the local worldsheet Hamiltonian; the semigroup is continuous and
  $s$ is a modulus (row 2). $m_2$ is an *integrated vertex*, non-local on the worldsheet;
  the semigroup $\{m_2^n\}$ is discrete (R27 (2)); (3.9) is a sum over surfaces of all
  resolved genera, not a surface. By (1.5) a surface family has a $t$-independent
  $\gamma$; (3.9) is inhomogeneous unless $\gamma(t)=-2$ (Lemma 2.2). **No surface has
  $e^{-tm_2}$ as its state.**
- In target-space QFT the Schwinger representation $1/(p^2+m^2)=\int dt\,e^{-t(p^2+m^2)}$ is
  the *worldline* proper time of the particle. $\Sigma$ is a field on target space with
  kinetic operator $m_2$; $e^{-tm_2}$ is the **worldline evolution of the composite
  $\Sigma$-quantum** for proper time $t$, with "mass operator" $m_2$ (a matrix on
  $\mathrm{Sym}^2\mathcal H_0$, as $p^2+m^2$ is a matrix on the particle's internal space). This is
  the honest geometric reading of $t$: second-quantised, one-dimensional, in target
  space — the worldline of the auxiliary particle, whose "vertices" along the line are
  the frozen necks. It is geometry of the $\Sigma$-Feynman graph, not of the worldsheet.

**Where the spectral condition bites.** For the worldsheet cylinder, $\int_0^\infty ds\,
e^{-sL_0^+}$ diverges on the tachyon ($L_0^+<0$) and is defined by analytic continuation
in the external momenta — the standard closed-string proper-time story, harmless because
$L_0^+$ depends on momentum and the continuation is canonical. For the $\Sigma$-worldline,
a negative eigenvalue of $m_2$ is a *tachyonic mode of the auxiliary particle*; an indefinite
Gram form at level 1 — **unverified
and uncited here** (R15 itself records the sign as open) — would mean such modes
exist at fixed momentum; the claim is flagged, not relied upon. No continuation repairs
this if it holds: by Lemma 2.2's caveat, the
sign of an eigenvalue of $m_2$ depends on the identification of the $N_{\rm gh}=4$ and $6$
sectors (a metric on $\mathcal H_0$), i.e. it is not even canonical. The unconditional form
uses the generator $m_2^2$ (length-2 chains, always positive on a symmetric invertible
block): the $\Sigma$-worldline with a squared mass operator, $\int dt\,m_2e^{-tm_2^2}$ —
still a worldline, still not a worldsheet.

**What would make $t$ a worldsheet length.** Only a $\Sigma$ kinetic operator that is a
function of $L_0^+$'s: if $\kappa_\Sigma=\hat K_\mu^{-1}$ for a tube kernel (3.4), then
$\kappa_\Sigma^{-1}=\int ds_1ds_2\,\mu\,b_1b_2e^{-s_1L_1-s_2L_2}$ and the Schwinger parameters
*are* the tube lengths. That is candidate (e) — redefining the kinetic term — and it is
the only route by which T2's picture becomes true; for the present $m_2=G_2^{-1}V_4$ it
is false by Lemma 2.2 and, independently, by Prop. 3.2 ($m_2$ is not a function of the
$L_0$'s).

**Result.** $\boxed{\text{(d) Laplace integrand: no worldsheet surface; }t=\Sigma\text{-worldline proper time (target space); reproduces the T2 failure mode for }m_2=G_2^{-1}V_4\text{; becomes a tube length only under (e)}}$
Machine checks: Lemma 2.2 (part 1); part 2 `laplace-indefinite-diverges` (direct form
diverges on an indefinite toy, converges on a positive one), `laplace-squared-unconditional`
(the squared form recovers the inverse on the indefinite toy).

### 3.5 T1 and T2 reopened

**T1 — the bounded-neck picture of the $\Sigma$ line.**
*Original objection* (020 §8, R27): "the bounded-length $\Sigma$-neck picture (Phase-6 note
§5) — wrong construction"; "WRONG — transposed R3's open-stub mechanism, which belongs to a
different construction". The Phase-6 picture put a single bounded plumbing neck between
the two $\Sigma\Psi\Psi$ vertices and called it the $\Sigma$ propagator of the paper's
action, whose kinetic term is $V_4$ (case (γ)).
*What is different now.* Nothing for case (γ): a single connected neck has $\gamma=2+\nu_f$
(R28, Lemma 2.1), a double neck of any measure is level-diagonal (Prop. 3.2), and the
paper's $\Sigma$ exchange reproduces the *whole* $\mathcal V_{0,4}$ region (R14, R27 (5)), which
contains no neck. What is different is the *definition* of the auxiliary: Erbin–Fırat
define the kinetic operator as the inverse of the bounded strip, so the bounded neck is
the propagator of an auxiliary whose kinetic term is *not* $V_4$. Two such sectors:
- **(α-neck) single strand, $\Sigma\in\mathcal H$** — the faithful transplant of the
  Erbin–Fırat mechanism; kept distinct below from **(α-rev)** (§5.4/§6.2), the
  reversed-range $|q|>1$ prescription, which is *not* a transplant of this construction:
  propagator $\hat{\mathsf P}_{[0,\lambda]}$ (row 4,
  $\gamma=-1$, 2 moduli: bounded length and twist), kinetic $c_0^+L_0^+/(1-e^{-\lambda L_0^+})$
  ($\gamma=+1$, §1.4(d) — the Siegel-gauge form of the full kinetic operator
  $Q_B/(1-e^{-\lambda L_0^+})$ used in §5.4/§6.2; the same object in two gauges, $\gamma=+1$
  either way), vertex $V_3$. Its exchange, summed over the three channels, is the
  union of the three bounded-neck Feynman regions $\{e^{-\lambda}\le|q|\le1\}$ — exactly the
  part of $\mathcal V_4^{\rm stub}$ that stubbing $\mathcal V_3$ by $\lambda/2$ moves out of the
  propagator (closed analogue of R3's mechanism; ghost count consistent). It does **not**
  produce the interior of $\mathcal V_{0,4}$, which is present for closed strings and absent
  in Witten's OSFT — the one place the closed/open transfer is not verbatim. So (α-neck)
  covers the necks and *leaves $\mathcal V_{0,4}$'s interior as an elementary quartic
  vertex*: it does not by itself make the theory cubic. (γ) covers the interior; neither
  replaces the other.
- **(β) double strand, propagator a tube kernel $\hat K_\mu$ (3.4)**, e.g. the correctly
  antighosted diagonal tube $b_1b_2(1-e^{-\lambda(L_1+L_2)})/(L_1+L_2)$: $\gamma=-2$ ✓, kinetic
  $\hat K_\mu^{-1}$ level-diagonal with $\gamma=+2$ ✓; the non-diagonal part of $V_4$ must sit
  in the two vertices, $V_4=W_3\circ\hat K_\mu\circ W_3$. Moduli: if $W_3$ is Harold's
  $\mathcal W_3$ on $\mathcal P_{0,3}$ (one colour-2 puncture, **no** moduli) and the tube is
  diagonal (one length, one twist), the count is $0+2+0=2=\dim_\R\mathcal V_{0,4}$ — Harold's
  2024 objection (i) *disappears* under (β) with the diagonal tube, and objection (ii)
  (loops) is R27's resolved genus, which costs nothing in the coloured grading. What
  remains open is whether the algebraic factorisation $M=W^tgW$ ($g$ level-diagonal, $M$
  the Gram matrix of $V_4$; always solvable as matrices) admits a $W$ that is a surface
  form on $\mathcal P_{0,3}$ with a pair puncture, and with which ghost count on the pair
  space (§3.2: 9a lives on the pair-level-matched space, one $b_0^-$ short of $G_2$).
  **Hand-off to 12c (candidate (e)).**
*Verdict.* $\boxed{\text{T1: for the paper's }\Sigma\text{ (case γ) it reproduces the T1 failure mode, in those words; as the propagator of a redefined auxiliary it is a live construction — (α-neck) for the necks (Task 14, not itself cubic-making), (β) diagonal tube with }\mathcal W_3\text{ vertices, moduli count }2\ \checkmark\text{, factorisation open (12c)}}$

**T2 — the Schwinger $t$ as a neck length.**
*Original objection* (020 §8): "reading the Schwinger $t$ of $m_2^{-1}$ as a worldsheet
length — refuted by ghost counting"; 008 §3(d): $t$ conjugates the vertex form itself, no
$g_s$-grading, collapse in sandwiched position.
*What is different now.* For $m_2=G_2^{-1}V_4$: nothing — Lemma 2.2 (grading) and Prop. 3.2
($m_2$ is not a function of the $L_0$'s) both stand, and §3.4 adds the positive reading
($t$ = $\Sigma$-worldline proper time in target space, (3.9) a fugacity expansion). For a
redefined kinetic term $\kappa_\Sigma=\hat K_\mu^{-1}$ (cases (α-neck)/(α-rev), (β)): the Schwinger
parameters of $\kappa_\Sigma^{-1}$ are literally the tube lengths, and the objection is void
by construction — but then the object being inverted is a tube, not $V_4$, and the
question "is $t$ a length" has become "is $V_4$ a stubbed exchange", i.e. T1/(e).
*Verdict.* $\boxed{\text{T2: reproduces the T2 failure mode for }m_2=G_2^{-1}V_4\text{, in those words; }t\text{ is a target-space worldline time; it is a worldsheet length only after the change of kinetic term (e)}}$

### 3.6 Verdict lines for §0 and hand-offs to 12c

| brief label | §0 row | ghost (map) | moduli | verdict | mechanism |
|---|---|---|---|---|---|
| (a) product kernels | (b) | $-2$ ✓ | 4 | **obstruction** | Prop. 3.1 ($\hat k\otimes\hat k$; rank across strands, $S_4$ symmetry) — the polarised undressed case is Prop. 3.2's, the polarised dressed case only §5.6's; row 7 also poles; sums = Neumann chain (R27 (ii)), $V_4$-dependent factors |
| (b) diagonal / half-frozen | (a), (c) | 9a: 0; 9b: $-1$; $b_1b_2$-diagonal: $-2$ ✓ | 2 / 3 | **obstruction** as $1/m_2$ | Prop. 3.2 (commutant: tube kernels are level-diagonal, $m_2$ is not); frozen $b_0^+e^{-sL_0^+}$ admissible only as a factor / under (e) |
| (c) explicit ghosts | (d) | $2-n_x$, $-2$ at $n_x=4$ | $6g+2$ (2 at $g=0$) | **obstruction** (as a uniform construction; §5.6) | homogeneity (3.8): degree $+1+g$ in the vertex data vs $-1$, uniformly in $tV_4$; at $t=1$ a fine-tuned dressing is not excluded by this argument; the object is a dressed vertex |
| (d) Laplace integrand | (T2) | inhomogeneous (Lemma 2.2) | — | **obstruction** (no surface) | $t$ = $\Sigma$-worldline proper time in target space; tube length only under (e) |
| T1 | (T1) | $2+\nu_f$ single neck; $-2$ double tube | 2 (diagonal) | failure mode reproduced for (γ); **live construction** for (α-neck)/(β) | (α-neck): bounded necks of $\mathcal V_4^{\rm stub}$, not the interior (not itself cubic-making); (β): $\mathcal W_3\circ\hat K_{\rm diag}\circ\mathcal W_3$, moduli $2$ ✓, factorisation open → 12c |
| T2 | (T2) | — | — | failure mode reproduced for (γ) | void by construction under (e) |

**What 12c inherits.** (i) Prop. 3.2 is the sharpest single statement: *every* tube-only
kernel is level-diagonal, so under (e) the whole non-diagonal content of $V_4$ must be in
the vertices; the toy for (e) is therefore "given a level-truncated symmetric $M$ and a
level-diagonal positive $g$ (the inverse of the chosen tube), is $M=W^tgW$ with $W$ of
surface type", not "does a tube invert $M$" (that is settled, negatively). (ii) The
diagonal tube with both antighosts, $b_1b_2(1-e^{-\lambda(L_1+L_2)})/(L_1+L_2)$, is the
candidate propagator that matches $V_4$'s moduli count with moduli-free $\mathcal W_3$
vertices — Harold's 2024 fixture, repaired by one antighost. (iii) Its natural home is the
pair-level-matched space (§3.2, first bullet), not $\mathrm{Sym}^2\mathcal H_0$; the ghost count of
$\mathcal W_3$ on that space is to be done in 12c with (1.5) (a colour-2 puncture is one
puncture carrying a pair state; do not count it as two). (iv) The tautology trap is avoided throughout §3: every obstruction is proven against the
identity $V_4\circ K=G_2$ where it can fail (rank, commutant, homogeneity, grading), not
by comparison with $V_4^{-1}$ formed algebraically. One exception, harmless: the script's
`prod-rank-S4: d=2 Gauss-Newton` leg (part 2) does form $M^{-1}$ and fits $\mathrm{Sym}^2k$
to it as a least-squares distance — a numerical search, not a candidate built *from*
$M^{-1}$; Prop. 3.1's analytic proof does not rely on it.

**Self-review of 12b.** *Objective:* the map now has a mechanism per candidate, and two
of them (Prop. 3.1, 3.2) are one-paragraph arguments that can be checked by hand. *Weakest
step:* the claim "$V_4$ is not level-diagonal per strand" rests on the generic-momentum
non-vanishing of the 4-tachyon vertex-region integral — standard, and R15's level-0
non-vanishing is one instance; a zero-momentum-only statement would need the
dilaton-theorem coupling $V_4(D,T,T,T)\ne0$, which is literature, not derived here.
*Not checked:* the BRST paragraphs of §3.2–3.3 are operator identities
($[Q,b_0^+e^{-sL}]=Le^{-sL}$, $[Q,\oint vb]=T(v)$) taken as standard; the (β) moduli count is
a count, not a construction. *A stronger physicist in five minutes:* would ask whether
Prop. 3.2 also kills (β) — it does not, because in (β) the kinetic term is diagonal by
definition and $V_4$ is reconstructed with vertices, but they would then ask whether
$W$ can be a surface; that is 12c's toy and is stated as such above.

## Working notes (12b)

None outstanding: every intermediate step of 12b was written directly into §3.1–§3.6.
One point discovered along the way and promoted into §3.2 rather than left here: the
brief's "half-frozen" object (antighosts > moduli) is *not* Harold's 9a/9b (which has
fewer antighosts than moduli, "quarter-frozen"), but $b_1b_2\,g(L_1,L_2)$ — the diagonal
tube with both $b^+$ kept — and it is the first object in Task 12 that passes the ghost
filter *and* the moduli filter (3 or, with $\mathcal W_3$ vertices under (β), 2) and is killed
only by the commutant argument, which is specific to the present $m_2$.

## Verification (12b)

Script `codes/verify-geometric-inverse.py`, part 2, seed 20260908, **92/92 PASS** (68 part 1
+ 24 part 2), exit 0. All toys are finite-dimensional $S_4$-symmetric complex tensors on
$\mathrm{Sym}^2\mathbb C^d$; every check compares a candidate against the identity $V_4K=G_2$
(or a consequence of it), not against $V_4^{-1}$ formed algebraically (tautology trap; one exception: the part 2 Gauss–Newton leg fits $\mathrm{Sym}^2k$ to $M^{-1}$ as a least-squares distance — a numerical search, not a candidate built from $M^{-1}$).
- **Prop. 3.1** `prod-rank-S4`: the product form (3.2) fails $(23)$-symmetry for random
  non-degenerate symmetric and antisymmetric $\beta$ at $d=2,3,4$ (residual $O(10)$);
  `prod-rank-d1-control`: symmetric at $d=1$ and for rank-one $\beta$ at $d=3$ (the two
  cases the proposition allows); Gauss–Newton search for $k$ with $\mathrm{Sym}^2k=M^{-1}$
  from 20 random starts for a random $S_4$-symmetric $M$ at $d=2$: best residual $18.6$;
  `prod-sum-spans`: polarised products span $\mathrm{End}(\mathrm{Sym}^2\mathbb C^2)$ (rank 9);
  break-on-purpose: rank-one $\beta$ perturbed by $10^{-3}$ is caught.
- **Prop. 3.2** `commutant-L0` (decorative: a tube kernel commuting with $e_1(L),e_2(L)$
  by construction is an arithmetic check, not independent evidence): a tube kernel with a
  random 6-point joint measure $\mu(s_1,s_2)$ commutes with $e_1(L),e_2(L)$;
  `commutant-generic-V4`: a random $S_4$-symmetric
  $M$ at $d=3$ does not, and the least-squares best level-diagonal $K$ leaves
  $\|MK-1\|=1.8$; `commutant-diag-V4-control`: a level-diagonal $M$ *is* inverted by the
  tube (the check can pass); $(b_1+b_2)b_1$ and $(b_1+b_2)b_2$ both square to zero and
  agree entrywise up to sign on the two-strand zero-mode Fock space.
- **Eq. (3.8), as a uniform construction** `explicit-ghost-scaling`: symmetric involutive
  $M$ with $B=B'=1$ satisfies $MB^tMB'=1$ at $\lambda=1$ and fails it at $\lambda=2$ — this
  leg *supports the scaling claim* (the construction fails away from $t=1$); it does
  **not** exhibit a $t=1$ obstruction for candidate (c) and in fact exhibits the $t=1$
  loophole (§3.3, §7): at $\lambda=1$ the identity holds exactly for this fine-tuned
  $(M,B,B')$. `explicit-ghost-family`: directional derivative
  $=2MB^tMB'\ne0$, likewise a scaling-only statement; a random dressed vertex $B^tMB'$
  (decorative: a random product is not expected to be an inverse) gives $\|MK_x-1\|>0.1$
  while $M^{-1}$ gives $<10^{-10}$ (the check distinguishes an inverse from a non-inverse,
  nothing more).
- **§3.4** `laplace-indefinite-diverges`: $\|e^{-30m}\|=7.7\times10^{11}$ on a toy with one
  negative eigenvalue vs $4.4\times10^{-11}$ on the positive control;
  `laplace-squared-unconditional`: $\int_0^{40}dt\,me^{-tm^2}$ recovers $m^{-1}$ to $10^{-3}$.
- Not machine-checked: the contour-deformation identification of extra antighosts with
  leg operators (§3.3, standard); the BRST identities $[Q,b_0^+e^{-sL_0^+}]=L_0^+e^{-sL_0^+}$
  and $[Q,\oint vb]=T(v)$ (standard); the generic-momentum non-vanishing of the 4-tachyon
  vertex-region integral (literature; R15 level-0 is one instance); the (β) moduli count
  and the existence of a surface-type $W$ in $M=W^tgW$ (12c).

### 3.7 (e) The change of kinetic term (Erbin–Fırat mechanism, closed string, two strands) [§0 row (e)] (12c)

**Literal task (12c).** Decide whether an HS-type action
$S=\tfrac12V_2+\tfrac{g_s}{3!}V_3+\tfrac12\langle\Sigma,K\Sigma\rangle-\langle\Sigma,J(\Psi,\Psi)\rangle$
with $K^{-1}$ a *geometric* (bounded, possibly diagonal) double tube and $J$ a 4-leg vertex
reproduces $V_4$ when $\Sigma$ is integrated out — i.e. whether the vertex region
$\mathcal V_{0,4}$ factorises geometrically as $V_4=J\circ K^{-1}\circ J$. Four counts
(real dimension, ghost number via (1.5), Sonoda–Zwiebach hypotheses, on-shell content) and a
boxed verdict; then the finite-dimensional toy of §4 with a demonstrated failure.

**Motivating objective.** Case (β) of Task 12: is there an honest geometry for the auxiliary
channel if one is willing to *redefine* the auxiliary's kinetic term (Erbin–Fırat's move),
as opposed to inverting the present $m_2=G_2^{-1}V_4$ (settled negatively by §3.1–3.5)?

Conventions: §1.1 (C1)–(C7), translations (1.2)–(1.5) verbatim; $L_i:=L_0^{+(i)}$,
$b_i:=b_0^{+(i)}$ as in §3.2; the candidate propagator is the $b_1b_2$-diagonal tube
$\hat K_{\rm diag}^{-1}=b_1b_2\,\frac{1-e^{-\lambda(L_1+L_2)}}{L_1+L_2}$ (§3.2, (3.4) with
$\mu=\delta(s_1-s_2)\chi_{[0,\lambda]}$), or the bounded product $\mathsf P_{[0,\lambda]}^{\otimes2}$ (row 8).

#### 3.7.1 The open-string mechanism, restated in the closed-string dictionary

**Open string (review C9ETB6WE §1–3, R3).** Siegel gauge, integrating $\Sigma$ out of
$-g_o^2S=\tfrac12\langle\Psi,c_0L_0\Psi\rangle+\tfrac12\langle\Sigma,\tfrac{c_0L_0}{1-e^{-2\lambda L_0}}\Sigma\rangle
-\tfrac13\langle\Sigma-e^{-\lambda L_0}\Psi,(\Sigma-e^{-\lambda L_0}\Psi)^{*2}\rangle$ at leading order
gives $\Sigma=P_{[0,2\lambda]}(\tilde\Psi*\tilde\Psi)$, $\tilde\Psi:=e^{-\lambda L_0}\Psi$,
$P_{[0,2\lambda]}=b_0(1-e^{-2\lambda L_0})/L_0$, and the induced quartic term
$$
V_4^{\rm stub}(\Psi^4)\;\propto\;\big\langle\tilde\Psi*\tilde\Psi,\;P_{[0,2\lambda]}\,(\tilde\Psi*\tilde\Psi)\big\rangle
\;=\;\big(V_3^{\rm stub}\circ P_{[0,2\lambda]}\circ V_3^{\rm stub}\big)(\Psi^4),
\tag{3.9}
$$
summed over the three pairings (automatic: a quartic form in one field is its own
$S_4$-symmetrisation). Three facts make (3.9) *geometric*:

- **(G1) topology.** Two disks glued along a strip of length $\ell\in[0,2\lambda]$ are a
  disk: the composite is a 1-real-parameter family in $\mathcal M_{0,4}^{\rm open}$
  ($\dim_\R=1$), and the union over the three channels is exactly the region of
  $\mathcal M^{\rm open}_{0,4}$ that the stubbed cubic vertices leave uncovered
  (Schnabl–Stettinger). Same genus, same moduli space as the target.
- **(G2) ghost count (C7).** $S(V_3^{\rm stub})=3$ each, strip bivector $S_B=2$ (one $b_0$):
  $S=3+3-2=4=$ the integrated open $\mathcal V_4$. ✓ (One antighost for one modulus.)
- **(G3) regularity.** $P_{[0,2\lambda]}\to2\lambda b_0$ at $L_0\to0$: the auxiliary has no
  on-shell pole and no cohomology (R3); the kinetic operator $c_0L_0/(1-e^{-2\lambda L_0})$ is
  *defined* as the inverse of the bounded strip, so the "inverse of the vertex" never appears.

**Closed transplant, case (β).** Auxiliary $\Sigma\in\mathcal S$, where $\mathcal S$ is
$\mathrm{Sym}^2\mathcal H_0$ or the pair-level-matched space
$\mathcal S_{\rm pair}:=\ker(L_0^{-(1)}+L_0^{-(2)})\cap\ker(b_0^{-(1)}+b_0^{-(2)})\supset\mathrm{Sym}^2\mathcal H_0$
(§3.2). Action
$$
S=\tfrac12V_2(\Psi,\Psi)+\tfrac{g_s}{3!}V_3(\Psi^3)+\tfrac12\langle\Sigma,K\Sigma\rangle-\langle\Sigma,J(\Psi,\Psi)\rangle ,
\qquad
K^{-1}\in\{\hat K^{-1}_{\rm diag},\ \mathsf P_{[0,\lambda]}^{\otimes2},\ \hat K_\mu^{-1}\ (3.4)\},
\tag{3.10}
$$
$J:\mathcal H_0^{\otimes2}\to\mathcal S$ a "vertex" $\mathcal W_3$ with two ordinary punctures
and one pair puncture. Integrating $\Sigma$ out: $S_{\rm eff}\supset-\tfrac12\langle J(\Psi,\Psi),K^{-1}J(\Psi,\Psi)\rangle$,
so the requirement is
$$
\frac{g_s^2}{4!}V_4(\Psi^4)\;\overset{!}{=}\;-\tfrac12\sum_{\text{3 pairings}}\langle J(\Psi_i,\Psi_j),K^{-1}J(\Psi_k,\Psi_l)\rangle
\;=:\;-\tfrac12\,\mathrm{Sym}_{S_4}\big(J\circ K^{-1}\circ J\big)(\Psi^4).
\tag{3.11}
$$
(R14 is the special case $J\propto V_4$, $K^{-1}\propto V_4^{-1}$, where each pairing already
gives $V_4$ and the 3 collapses into the normalisation — the tautology.) Two readings of
(3.11) are kept apart below and in §4: **single-channel**, $V_4=J\circ K^{-1}\circ J$ as a
$2+2$ form (requires the right side to be $S_4$-symmetric by itself), and **three-channel**,
(3.11) as written — the honest transplant of (3.9), where each channel covers one third of
the region.

**What the pair puncture is.** A state of $\mathcal S$ is a *pair* of closed-string states;
the CFT has no local operator for it at a single point. So $\mathcal W_3$ "with a pair
puncture" is a 4-punctured sphere (or a family of them) in which two punctures $(z_3,z_4)$
are *bundled*: $J(\Psi_1,\Psi_2)=\sum_{ab}\phi_a\otimes\phi_b\;\big\langle\Psi_1\Psi_2\phi_a^c\phi_b^c\big\rangle_{\mathcal W_3}$,
i.e. $J$ is a 4-form of the same kind as $V_4$ itself (a slice or a sub-region of
$\mathcal M_{0,4}$ with local coordinates and antighosts), read as a map $2\to2$. This is
008's colour-2 leg (008 §2). The transplant of (G1)–(G3) is then the content of the four
counts (i)–(iv) below; (G1) is where the closed string differs.

#### 3.7.2 Count (i): real dimensions

Target: $\mathcal V_{0,4}\subset\mathcal M_{0,4}$, $\dim_\R=2$, one channel's share of it
also 2-dimensional (a region, not a curve). Composite $J\circ K^{-1}\circ J$: real dimension
$=2m_J+n_\mu(K^{-1})$ with $m_J$ the number of real moduli integrated in each $\mathcal W_3$
(the two $J$'s are the same object, so the count is symmetric) and $n_\mu(K^{-1})$ the
tube's integrated moduli, counting twists (C4) separately because on $\mathcal S_{\rm pair}$
the shared twist is *not* a Kronecker delta.

| tube $K^{-1}$ | lengths | twists | $n_\mu$ | $m_J$ forced by "$=2$" |
|---|---|---|---|---|
| bounded product $\mathsf P_{[0,\lambda]}^{\otimes2}$ (row 8) | 2 | 2 (both $\to\delta_{L_0^{-(i)},0}$ on $\mathrm{Sym}^2\mathcal H_0$) | 4 (2 effective) | none: $4>2$; with twists as deltas $2+2m_J=2\Rightarrow m_J=0$ |
| $b_1b_2$-diagonal, independent twists ((3.4), $\mu=\delta\chi$) | 1 | 2 (deltas) | 3 (1 effective) | $1+2m_J=2$: impossible for integer $m_J$ — one $J$ modulus, or a *half*-integrated pair |
| $b_1b_2$-diagonal, shared twist (on $\mathcal S_{\rm pair}$) | 1 | 1 (genuine, projects on $L^-_{\rm tot}=0$ only) | 2 | $m_J=0$: **rigid $J$** |
| fully diagonal 9a | 1 | 1 | 2 | $m_J=0$ |

*Reading.* (a) The product tube overshoots by 2 unless the twists are discounted as level
deltas, in which case the two independent lengths already exhaust the target and $J$ must
be rigid — the first observation of §3.2. (b) The diagonal tube with one shared length
and one shared twist, acting on $\mathcal S_{\rm pair}$, is the *unique* tube in the table with
exactly 2 genuine moduli, and it forces $m_J=0$: **$\mathcal W_3$ is a rigid surface** (a
point of $\mathcal P_{0,4}$ with its local coordinates), so that the whole 2-dimensional
family of composite surfaces is swept by the tube alone — Harold's fixture. (c) On
$\mathrm{Sym}^2\mathcal H_0$ (both twists integrated to deltas) the same tube has one genuine
modulus and the count $1+2m_J=2$ has no integer solution: the region would have to be
swept by one tube length and one $J$-direction, i.e. $J$ a one-parameter *curve* in
$\mathcal P_{0,4}$ with one Beltrami antighost — a legitimate but odd object (a 1-form on
$\mathcal M_{0,4}$), kept as a variant (b′) below.

**Dimension of the composite family as a surface.** The two 4-punctured spheres glued along
two tubes form $\Sigma_{1,4}$ (R27, 008 (B.2): $\chi=-4$, $n=4$, $g=1$),
$\dim_\R\mathcal M_{1,4}=8$. The rigid-$J$ + diagonal-tube family is a 2-dimensional
sub-family of $\mathcal M_{1,4}$ — it has the *dimension* of $\mathcal V_{0,4}$ but lives in the
wrong moduli space. That is the transplant failure of (G1): open strips glue disks to a
disk; closed double tubes glue spheres to a torus. The single-tube gluing (which does give
a sphere and does reproduce a Feynman region) is route (α-neck)/(α-rev), Task 14, not (β).

$\boxed{\text{(i): }2m_J+n_\mu=2\ \Rightarrow\ \text{diagonal tube (1 length + 1 shared twist on }\mathcal S_{\rm pair})\text{ and rigid }\mathcal W_3;\ \text{composite family}\subset\mathcal M_{1,4},\ \dim 2\text{ of }8}$

#### 3.7.3 Count (ii): ghost number of $\mathcal W_3$ on the pair-level-matched space, and the missing six units

**Rule.** By (1.5) with two surfaces ($\mathcal W_3$ twice, each a 4-punctured sphere with
$n_b^J$ antighost insertions, $n_c=0$) and one two-strand bivector $K^{-1}$ with $n_b(K)$
antighosts ($S_B=12-n_b(K)$, two BPZ bivectors at 6 each):
$$
S\big(J\circ K^{-1}\circ J\big)=2\,(6+n_b^J)-\big(12-n_b(K)\big)=2n_b^J+n_b(K)
\;\overset{!}{=}\;S(V_4)=8 .
\tag{3.12}
$$
The same number read on the glued surface $\Sigma_{1,4}$ by (1.1): $6(1-1)+n_b^{\rm tot}$ with
$n_b^{\rm tot}=2n_b^J+n_b(K)$ — consistent, and it says that the composite has the sphere's
saturation iff $n_b^{\rm tot}=8=\dim_\R\mathcal M_{1,4}$: **the full antighost measure of the
torus**, whatever the split between $J$ and the tube. The pair puncture is one puncture of
$\mathcal S$ but two of the CFT surface; (3.12) counts it as two CFT punctures with one
bivector, which is the only reading in which the anomaly (1.1) applies.

**Two counts together.** With count (i), $2m_J+n_\mu(K)=2$ ($m_J$ = moduli of $J$ integrated,
$n_\mu(K)$ = genuine tube moduli on the space in question), (3.12) gives a parity lemma:

*Lemma 3.3.* $n_b(K)$ and $n_\mu(K)$ must both be even; $m_J=1-\tfrac12n_\mu(K)$,
$n_b^J=4-\tfrac12n_b(K)$.

| space | tube (antighosts) | $n_b(K)$ | $n_\mu(K)$ | $n_b^J$ | $m_J$ | verdict |
|---|---|---|---|---|---|---|
| $\mathrm{Sym}^2\mathcal H_0$ | $\mathsf P_{[0,\lambda]}^{\otimes2}$: $b_1b_2b^-_1b^-_2$, 2 lengths | 4 | 2 | 2 | 0 | **(β1)** passes both |
| $\mathrm{Sym}^2\mathcal H_0$ | $b_1b_2b_1^-b_2^-$, shared length ((3.4), $\mu=\delta\chi$) | 4 | 1 | 2 | $\tfrac12$ | ✗ parity |
| $\mathcal S_{\rm pair}$ | $b_1b_2\,b^-_{\rm tot}$, shared length + shared twist | 3 | 2 | $\tfrac52$ | 0 | ✗ parity |
| $\mathcal S_{\rm pair}$ | $b_1b_2b^-_1b^-_2$, shared length + shared twist (one $b^-$ non-moduli) | 4 | 2 | 2 | 0 | **(β2)** passes both |
| $\mathcal S_{\rm pair}$ | 9a: $(b_1+b_2)\,b^-_{\rm tot}$ | 2 | 2 | 3 | 0 | **(β3)** passes both, $J$ needs one non-moduli $b$ |
| any | 9b: $(b_1+b_2)b^-_1b^-_2$ | 3 | 1 or 3 | $\tfrac52$ | — | ✗ parity |

So Harold's fixture survives the two counts in exactly the forms (β1)–(β3), all with
**$m_J=0$: a rigid $\mathcal W_3$ that is not integrated over anything but carries two (or
three) unsoaked antighosts** — in (β1)/(β2) it is the integrand $\Omega_{V_4}(\mu_0)=
\langle\,\cdots b(\partial_{\mu_1})b(\partial_{\mu_2})\rangle_{\mu_0}$ of the $V_4$ measure at a
single point $\mu_0\in\mathcal P_{0,4}$ (row 12), and the composite is
$$
V_4\overset{?}{=}\mathrm{Sym}_{S_4}\Big[\Omega_{V_4}(\mu_0)\circ K^{-1}\circ\Omega_{V_4}(\mu_0)\Big]
\qquad(K^{-1}\text{ of type (β1) or (β2)}).
\tag{3.13}
$$
The ghost number of $\mathcal W_3$ as a map $\mathcal H_0^{\otimes2}\to\mathcal S$ is then, by
(1.2) with $S=6+n_b^J=8$ and $\ell=2$: $\gamma(\mathcal W_3)=10-8=+2$ — the same as $m_2$'s.
On $\mathcal S_{\rm pair}$ the pairing is not $G_2$ (one $c_0^-$ of $G_2$ has no $b^-$ to absorb
on states that are only $b^-_{\rm tot}$-annihilated; §3.2), and the natural pairing is
$\omega_{\rm pair}(A,B)=\langle A|c_0^{-}{}_{\rm tot}|B\rangle$, at saturation $11$ instead of $10$;
the form saturation of $J$ is unchanged (it is a CFT correlator), so $\gamma_{\rm pair}(\mathcal W_3)=11-8=+3$
and $\gamma_{\rm pair}(K^{-1})=-2$ for the 3-antighost tube ($S_B=12-3=9$ paired at
saturation 11, $\gamma_{\rm pair}=9-11=-2$) — the parity failure of the
third row seen from the other side.

**Where the missing six units come from — stated, not solved.** Read as a surface of the
single $c=26$ CFT, the composite is $\Sigma_{1,4}$ with anomaly $0$; $V_4$ is $\Sigma_{0,4}$
with anomaly $6$. (3.12) fills the gap with six antighost insertions beyond $V_4$'s two:
four Beltrami antighosts of the two frozen $\mathcal W_3$ slices, plus the two tube
antighosts that are not the two integrated tube directions. Six unintegrated antighosts on a
genus-1 surface are, by (1.5), exactly R27's "frozen directions": the composite is
$\int_{\text{2-dim}}\big(\text{8-form on }\mathcal M_{1,4}\big)$, a 2-dimensional integral of a
top form of the *torus* moduli space, whereas $V_4$ is a 2-dimensional integral of a top form
of the *sphere* moduli space. (3.13) would identify the two for all external states. The one
picture in which such an identity is not absurd on its face: $\Sigma_{1,4}$ is the double
cover of $\Sigma_{0,4}$ branched at the four punctures (every elliptic curve is
$y^2=\prod_{i=1}^4(x-x_i)$), and the two strands of $\mathcal S$ are the two sheets; the
composite would then be a *sphere* correlator of the $\mathbb Z_2$-covering theory with
branch-point (twist-field) insertions at the four punctures, and the six units would be
the ghost number carried by the four twist fields. Whether the pair puncture, the diagonal
tube and the frozen antighosts assemble into that covering picture is the **branched-cover
question**, which 12c does not attempt; it is the entry point for 12d's hand-off. Note that
the $\lambda\to0$ slice of (β1)/(β2) is R27's frozen-neck chain of length 2, so R27's genus
formula is the same statement at zero tube length.

**The concrete correlator-level difference (the loop momentum).** Independently of the
branched-cover picture, the composite carries a piece $V_4$ does not: the intermediate sum
over $\mathcal S_{\rm pair}$ inside $\langle\Omega_{V_4}(\mu_0)(\Psi_1\Psi_2),\,K^{-1}\,
\Omega_{V_4}(\mu_0)(\Psi_3\Psi_4)\rangle$ runs over the pair's relative momentum $k_a$
($k_b=-k_1-k_2-k_a$ fixed), i.e. a genuine $\int d^Dk_a$ — the torus's loop momentum —
absent from the tree-level $\mathcal V_{0,4}$ integral. This is the correlator-level
content of "genus 1 vs 0" and gives a cheap "no" route to Q13 (§6.1) independent of the
$\lambda$-function computation: compare the analytic structure in the external momenta
(pair-channel thresholds from $\int d^Dk_a\,g(L_a+L_b)$, absent in $\mathcal V_{0,4}$). See
Lunin & Mathur (2001), *Correlation functions for $M^N/S_N$ orbifolds*, hep-th/0006196,
for the covering-space dictionary (torus correlator of the CFT $\leftrightarrow$ sphere
correlator of the $\mathbb Z_2$ symmetric-orbifold CFT with twist fields; $\mathrm{Sym}^2
\mathcal H_0$ is precisely the untwisted sector) that Task 13 should use to make this
precise. Aside, out of scope here: the same relative-momentum sum sits inside R27's frozen
chains $m_2^n$, $n\ge2$; its status there is part of A2(iii)/H1–H2, not decided by this
record.

$\boxed{\text{(ii): }2n_b^J+n_b(K)=8=\dim_\R\mathcal M_{1,4};\ \text{with (i), Lemma 3.3 leaves (β1)–(β3), all with a rigid }\mathcal W_3=\Omega_{V_4}(\mu_0)\ (\gamma=+2)\text{; the six units are unintegrated antighosts on a torus; branched cover = open}}$

#### 3.7.4 Count (iii): Sonoda–Zwiebach hypotheses violated by a $2+2$ vertex

Review JY32WEUE, hypothesis → evasion map (its lines 160–176), applied to (3.10)–(3.13):

| SZ hypothesis | status under (β) | how |
|---|---|---|
| 1. single closed-string field, vertex operators of the CFT | **violated** | field content $\Psi\oplus\Sigma$; $\Sigma\in\mathcal S$ is a pair state, not a CFT state; the review's "[paper silent]" evasion, made concrete |
| 2. symmetric vertex ($S_3$ acting by phases on local coordinates) | **violated** | $J=\mathcal W_3$ has legs (1,1,pair); its symmetry group is $S_2\times S_2$ (swap the two $\Psi$'s; swap the two sheets of the pair puncture), not $S_3$ — the paper's case (iii) |
| 3. standard propagator, one sewing $z_3w_3=t$ | **violated** | the diagonal tube is two simultaneous sewings $z^{(1)}w^{(1)}=z^{(2)}w^{(2)}=t$, $e^{-\lambda}\le|t|\le1$, one parameter; the rectangle-group argument (one channel = one disk of $t$) has no version for a bounded annulus of $t$ shared by two necks — the paper's case (ii) |
| 4. BRST invariance as off-shell duality along $C_{st},C_{tu},C_{su}$ | **reappears** as a requirement, not evaded | gauge invariance of $S_{\rm eff}$ demands that the three channel families of (3.11) glue to the sphere region $\mathcal V_{0,4}$ *and* match the Feynman regions $V_3\circ\mathsf P\circ V_3$ along $\partial\mathcal V_{0,4}$ (the $\lvert q\rvert=1$ locus, R2), which is a family of **spheres**; the composite at its outer edge $s=\lambda$ is a family of tori |
| 5. three channel regions cover $\mathcal M_{0,4}$ once | **inapplicable** | $\mathcal V_{0,4}$ is covered by definition ($V_4$ exists); the question is whether a torus family can *equal* it, not whether it is covered |
| 6. $L_0=\bar L_0$ external states | unchanged | the pair space only relaxes level matching on the internal $\Sigma$ leg |

*Reading.* The no-go theorem does not forbid (β): three of its six hypotheses fail, one is
inapplicable. But its *mechanism* — duality along channel boundaries — is exactly where
(G1) bites again: the boundary of the region to be reproduced is the sphere locus $|q|=1$ of
R2, and the composite family reaches it (if at all) with a torus. So SZ is evaded at the
level of hypotheses and re-encountered at the level of the boundary-matching condition.

$\boxed{\text{(iii): SZ hypotheses 1, 2, 3 violated, 5 inapplicable, 4 reappears as boundary matching sphere}\leftrightarrow\text{torus; the theorem does not apply, its boundary condition does}}$

#### 3.7.5 Count (iv): on-shell content of the bounded double tube

With $L_{\rm tot}:=L_1+L_2$ and $\omega$-factors stripped (C5), the three tubes of §3.7.3:
$$
\hat K^{-1}_{(\beta1)}=b_1b_2\,\frac{1-e^{-\lambda L_1}}{L_1}\,\frac{1-e^{-\lambda L_2}}{L_2},
\qquad
\hat K^{-1}_{(\beta2)}=b_1b_2\,\frac{1-e^{-\lambda L_{\rm tot}}}{L_{\rm tot}},
\qquad
\hat K^{-1}_{(\beta3)}=(b_1+b_2)\,\frac{1-e^{-\lambda L_{\rm tot}}}{L_{\rm tot}} .
\tag{3.14}
$$
All three are entire in the $L$'s: (β1) $\to\lambda^2b_1b_2$ at $L_1=L_2=0$, (β2)/(β3)
$\to\lambda\,b_1b_2$, $\lambda(b_1+b_2)$ at $L_{\rm tot}=0$ (the closed form of R3's
$(1-e^{-2\lambda L_0})/L_0\to2\lambda$; (1.6) per strand). Consequences, in parallel with the
open case (R3):

- **No pole, no propagating $\Sigma$.** The unbounded diagonal tube $1/L_{\rm tot}$ has a pole
  on the *pair* mass shell $L_1+L_2=0$, which contains off-shell pairs $L_1=-L_2\ne0$ — a
  continuum of unphysical two-string thresholds (this is what §3.1 called "row 7 also by
  poles" for the product $1/L_1L_2$). The bound removes it: the $\Sigma$ propagator is a
  bounded operator on every level, and $\Sigma$ carries no cohomology provided
  $\Sigma\in(\ker L_{\rm tot})^c$, where $(b_1+b_2)/L_{\rm tot}$ is a contracting homotopy for
  $Q_{\rm tot}=Q^{(1)}+Q^{(2)}$ (from $\{Q_{\rm tot},b_1+b_2\}=L_{\rm tot}$, standard). On
  $\ker L_{\rm tot}$ itself the kinetic operator $Q_{\rm tot}/(1-e^{-\lambda L_{\rm tot}})$ is
  singular exactly as in the open case, and the same restriction $(\ker L_0)^c$ that
  Erbin–Fırat impose is needed (review C9ETB6WE §2).
- **Kinetic operator.** In Siegel gauge $K=c^+_2c^+_1\,\big[\hat K^{-1}\big]^{-1}$ on the
  $\downarrow\downarrow\otimes\downarrow\downarrow$ sector, i.e. $c_1^+c_2^+L_1L_2/[(1-e^{-\lambda L_1})(1-e^{-\lambda L_2})]$
  for (β1) and $c_1^+c_2^+L_{\rm tot}/(1-e^{-\lambda L_{\rm tot}})$ for (β2): $\gamma=+2$ by
  §1.4(d), level-diagonal by construction (Prop. 3.2 is void here). $\lambda\to0$: $K\to c_1^+c_2^+/\lambda^2$
  resp. $/\lambda$ and $\Sigma$ decouples (the $\Sigma$ exchange vanishes like $\lambda^2$, $\lambda$);
  $\lambda\to\infty$: the unbounded tube with its pair-threshold pole returns.
- **What is on-shell about it.** Nothing in (3.14) knows about $V_4$; the whole on-shell
  content of the auxiliary exchange (the poles of the 4-point amplitude) comes from the
  $\Psi$ propagators in the Feynman regions, as in the open case. The $\lambda$-derivative
  $\partial_\lambda\hat K^{-1}_{(\beta2)}=b_1b_2\,e^{-\lambda L_{\rm tot}}$ is the frozen object
  of §3.2 with $[Q,\cdot]=-\partial_s(\ldots)$, whose integrated form is the boundary term
  $1-e^{-\lambda L_{\rm tot}}$ that a $\lambda$-dependent $\mathcal W_3$ must absorb for gauge
  invariance — the *stubbed-vertex* structure $\mathcal W_3=\mathcal W_3(\lambda)$, which in the
  open case is $e^{-\lambda L_0}$ on each leg and in the closed case would be the collar of
  a stubbed $\mathcal V_3$ on the two ordinary legs *and a collar on the pair puncture* —
  the latter being a double tube again, i.e. a self-consistent but not obviously
  convergent recursion. Not pursued here.

$\boxed{\text{(iv): all three bounded tubes are entire in }L\text{ (no pole, no }\Sigma\text{ cohomology on }(\ker L_{\rm tot})^c\text{), }\gamma(K)=+2\text{, }\lambda\to0\text{ decoupling; the on-shell content of the exchange sits entirely in the }\Psi\text{ legs — (G3) transplants without change}}$

#### 3.7.6 Verdict

| count | open string (Erbin–Fırat) | closed string, case (β) | passes? |
|---|---|---|---|
| (i) real dimension | strip $[0,2\lambda]$: 1 = $\dim\mathcal M^{\rm open}_{0,4}$, rigid $V_3$ | $2m_J+n_\mu(K)=2$: diagonal tube on $\mathcal S_{\rm pair}$ (1 length + 1 shared twist) or bounded product on $\mathrm{Sym}^2\mathcal H_0$ (2 lengths), rigid $\mathcal W_3$ | ✓ (with $m_J=0$) |
| (ii) ghost number | $3+3-2=4$ ✓ | $2n_b^J+n_b(K)=8$: $n_b^{\rm tot}=\dim\mathcal M_{1,4}$; Lemma 3.3 leaves (β1)–(β3), $\mathcal W_3=\Omega_{V_4}(\mu_0)$ with $\gamma=+2$ | ✓ (with 6 unintegrated antighosts) |
| (iii) Sonoda–Zwiebach | not applicable (open) | hypotheses 1, 2, 3 violated, 5 inapplicable; boundary matching (4) reappears | ✓ evaded / boundary condition open |
| (iv) on-shell content | regular at $L_0=0$, no cohomology | (3.14) entire in $L$, no cohomology on $(\ker L_{\rm tot})^c$, $\lambda\to0$ decoupling | ✓ |
| (G1) topology of the composite | disk $\cup_{\rm strip}$ disk $=$ disk, family $\subset\mathcal M^{\rm open}_{0,4}$ | sphere $\cup_{\rm 2\ tubes}$ sphere $=$ **torus**, family $\subset\mathcal M_{1,4}$ (008 (B.2), R27) | ✗ |

**Verdict.** The change of kinetic term transplants to the closed string at the level of
every *count*: a $\Sigma$ with a bounded diagonal (or bounded product) double-tube propagator,
a level-diagonal kinetic operator of the Erbin–Fırat form, and rigid $\mathcal W_3$ vertices
that are the $V_4$ integrand at one point of $\mathcal P_{0,4}$ is ghost-consistent,
moduli-consistent, evades the Sonoda–Zwiebach hypotheses and has the right on-shell
structure. What does **not** transplant is the geometric factorisation itself: (3.9) is an
identity between families of surfaces of the same topology, and its closed analogue (3.13)
equates a 2-parameter family of tori with the full antighost measure of $\mathcal M_{1,4}$,
integrated over two of its eight directions, to a 2-parameter family of spheres. As a
statement about *surfaces* this is false (genus is a topological invariant of the glued
surface; proven by (B.2)): $\mathcal V_{0,4}$ does not factorise geometrically as
$J\circ K^{-1}\circ J$ in the single CFT with a double tube, for any $J$ and any tube. As a
statement about *correlators* — that the torus family, evaluated on all external states,
could equal the sphere family — (3.13) is not disproved here; it is the branched-cover
question of §3.7.3, and the frozen-neck chain (R27) is its $\lambda\to0$ slice. Hence:

$\boxed{\text{(e): ghost }+2/-2\ \checkmark,\ \text{moduli }2\ \checkmark\text{ (rigid }\mathcal W_3\text{, diagonal tube on }\mathcal S_{\rm pair}\text{)},\ \text{SZ evaded}\ \checkmark,\ \text{on-shell}\ \checkmark;\ \textbf{obstruction} \text{ as a surface factorisation of }\mathcal V_{0,4}\text{ (genus 1 vs 0, proven);}\ \textbf{open} \text{ as a correlator identity (branched cover)} }$

Three distinct angles were used (research skill §3): the two counts (i)–(ii) (algebraic,
pass), the topology of the composite (G1) (proof of obstruction at the surface level),
and the finite-dimensional toy of §4 (which can decide rank/parameter/signature questions
and is *blind* to the connected-surface question — stated there). The verdict is "not a
geometric factorisation" with proof, and "open as an identity" without a claim either way.

## 4. The toy computation: surface-built kernels against a generic $V_4$ (12c)

### 4.1 Set-up and the tautology guard

**Toy data (008 §1–2 conventions, 022's machinery).** $\mathcal H_0\to\mathbb C^d$, $d=3$, with
$L_0^+$ levels $\ell=(-1,0,1)$ (tachyon-like, massless, massive); $\mathrm{Sym}^2\mathbb C^3$ of
dimension $N=6$, product basis $e_ae_b$ ($a\le b$); $G_2=1$ (orthonormal basis, 008's
auxiliary inner product — nothing physical rides on it); $V_4$ a random complex
$S_4$-symmetric 4-tensor, Gram matrix $M_{(ab),(ce)}=V_4(e_ae_b,e_ce_e)$, rank $6$ (singular
values $3.95,\dots,0.13$, seed 20260908); tube kernel $g(\lambda)=\mathrm{diag}\big[(1-e^{-\lambda(\ell_a+\ell_b)})/(\ell_a+\ell_b)\big]$,
eq. (3.14) (β2) with the antighosts stripped, $\lambda=0.7$; a product tube
$\mathrm{Sym}^2(P)$ for a single-strand $P$. A "vertex" $J$ is a matrix $W\in\mathbb C^{r\times N}$
($r=\dim$ of the truncated $\Sigma$ space), $J\circ K^{-1}\circ J\leftrightarrow W^tgW$;
the three-channel sum (3.11) is $\mathrm{Sym}_3(T)=T_{abce}+T_{acbe}+T_{aebc}$ with
$T_{abce}=(W^tgW)_{(ab),(ce)}$.

**Identities tested (each can fail).** (I1) single channel $M=W^tgW$; (I2) three channels
$V_4=\mathrm{Sym}_3[W^tgW]$; (I3) $M\,g(\lambda)=1$ (the tube as $1/m_2$); (I4)
$M\,K_{(n)}=1$ for the Neumann chain $K_{(n)}=\sum_{k\le n}(-D^{-1}N)^kD^{-1}$, $M=D+N$, $D$
the level-diagonal part. $W$ is found by nonlinear least squares (`scipy.least_squares`,
6–8 random starts, real parametrisation of complex unknowns); $M^{-1}$ is never formed to
*build* a candidate (it appears only inside the Eckart–Young bound, as a yardstick).

**The tautology guard, made explicit.** Over $\mathbb C$ every symmetric $M$ is $W^tW$
(Takagi), hence $W^tgW$ for any invertible $g$: with an *unconstrained* $W$ of full row
count, (I1) cannot fail — check `takagi-unconstrained-W`, residual $3.6\times10^{-15}$. So
the toy has content only through what constrains $W$ or $g$: (a) the **rank** of $W$ or of
$g$ (a $\Sigma$ space smaller than $\mathrm{rank}\,M$, or a product tube built from a
rank-deficient strand), (b) the **structure** of $W$ (disconnected $\mathcal W_3$, $W=\mathrm{Sym}^2w$),
(c) the **signature** (real $W$, positive $g$). A connected rigid $\mathcal W_3$
($\Omega_{V_4}(\mu_0)$ of §3.7.3) is, in a finite-dimensional toy, indistinguishable from a
generic symmetric $2+2$ tensor: on it the toy is **blind by construction**, and this is the
honest boundary of §4 — the connected case is decided by §3.7.6's genus argument (surface
level) and left open at correlator level.

### 4.2 Candidate kernels and identities tested

1. **Rank-limited $\Sigma$ space** (I1), $r=4<6$: the composite has rank $\le r$, so
   $\min_W\|M-W^tgW\|_F\ge\big(\sum_{k>r}\sigma_k^2\big)^{1/2}$ (Eckart–Young). Found residual
   $0.3376$ = the bound $0.3376$ to four digits: the least-squares floor is exactly the
   rank bound — **demonstrated failure, rank type**.
2. **Product tube from a rank-2 strand** (I1), $g=\mathrm{Sym}^2(P)$, $\mathrm{rank}\,P=2$:
   $\mathrm{rank}\,\mathrm{Sym}^2(P)=\rho(\rho+1)/2=3<6$ (checked), residual $2.074$ = bound
   $2.074$. This is the brief's "product kernel against a $V_4$ whose rank exceeds what a
   product kernel can carry": a product double tube carries at most $\rho(\rho+1)/2$ of the
   $N=d(d+1)/2$ pair-levels, the deficit being every pair-level with a strand outside
   $\mathrm{range}\,P$.
3. **Disconnected $\mathcal W_3$** ($W=\mathrm{Sym}^2w$, $d^2=9$ parameters against
   $\binom{d+3}{4}=15$ independent components of $V_4$), full-rank $g(\lambda)$: (I2)
   residual $3.58$, (I1) residual $2.90$ — **demonstrated failure, structure type**.
   Positive control: a $V_4$ *generated* as $\mathrm{Sym}_3[\mathrm{Sym}^2(w_0)^t\,g\,\mathrm{Sym}^2(w_0)]$
   is recovered to $10^{-13}$; break-on-purpose: the same control perturbed by
   $10^{-2}\times$(random $S_4$ tensor) is caught with residual $3.9\times10^{-2}$.
4. **Bounded diagonal tube as $1/m_2$** (I3), $\lambda\in[0.05,20]$ scanned (400 points):
   $\min_\lambda\|Mg(\lambda)-1\|=2.53$; control: a level-diagonal $M$ is inverted to
   $10^{-12}$. Prop. 3.2 with the actual profile (3.14).
5. **Neumann chain on the level-diagonal part** (I4): $\rho(D^{-1}N)=2.48>1$ for the
   generic $M$; residuals $28,\ 8.2\times10^2,\ 1.8\times10^5$ at $n=2,6,12$ — the chain
   *diverges*; control: $M+3\|M\|\,\mathbb 1$ (diagonally dominant) converges to $4\times10^{-11}$
   at $n=12$. R27's only surface-flavoured representation is not even asymptotic for a
   random tensor in the toy; its threading on an algebraic $D^{-1}$ is the point
   (convergence for the actual $V_4$ is A2(iii), open; R29's script found examples with
   both $\rho<1$ and $\rho>1$).
6. **Signature** (I1, real): a real random $S_4$ tensor gives an $M$ with 3 negative
   eigenvalues; with $g>0$ and real $W$, $W^tgW\succeq0$, residual $2.641=\|M_-\|_F$ exactly.
   The three-channel sum has no such bound: $\mathrm{Sym}_3$ of a positive single-channel
   tensor is itself indefinite (2 negative eigenvalues) — so the unverified sign claim
   (indefinite Gram matrix at level 1, uncited here; R15 itself records the sign as open) would obstruct a *single-channel*
   real factorisation but not the honest three-channel (3.11).

### 4.3 Results table

Seed 20260908; $d=3$, $N=6$, levels $(-1,0,1)$, $\lambda=0.7$; residuals are Frobenius norms.

| candidate kernel / $W$ class | identity tested | residual | rank / parameter bound | verdict |
|---|---|---|---|---|
| unconstrained complex $W$, $r=N$, $g(\lambda)$ | (I1) $M=W^tgW$ | $3.6\times10^{-15}$ | none (Takagi) | tautology — no test |
| unconstrained $W$, $r=4$, $g(\lambda)$ | (I1) | $0.3376$ | $\ge(\sigma_5^2+\sigma_6^2)^{1/2}=0.3376$ | **fails** (rank) |
| product tube $\mathrm{Sym}^2(P)$, $\mathrm{rank}\,P=2$, free $W$ | (I1) | $2.074$ | rank $\rho(\rho+1)/2=3<6$; bound $2.074$ | **fails** (rank) |
| disconnected $\mathcal W_3$, $W=\mathrm{Sym}^2w$, $g(\lambda)$ | (I2) three-channel | $3.58$ | $9$ params vs $15$ components | **fails** (structure) |
| same | (I1) single-channel | $2.90$ | same | **fails** |
| same, $V_4$ generated by a product $W_0$ | (I2) | $1.1\times10^{-13}$ | — | passes (control) |
| same, control perturbed by $10^{-2}$ | (I2) | $3.9\times10^{-2}$ | — | caught (break-on-purpose) |
| bounded diagonal tube $g(\lambda)$, $\lambda$ scanned | (I3) $Mg=1$ | $\min_\lambda 2.53$ | Prop. 3.2 | **fails** |
| same, level-diagonal $M$ | (I3) | $<10^{-12}$ | — | passes (control) |
| Neumann chain $K_{(n)}$ on $D=\mathrm{diag}\,M$ | (I4) $MK_{(n)}=1$ | $28\to1.8\times10^5$ ($n=2\to12$) | $\rho(D^{-1}N)=2.48>1$ | **diverges** |
| same, diagonally dominant $M$ | (I4) | $4\times10^{-11}$ ($n=12$) | $\rho<1$ | converges (control) |
| real $W$, $g>0$, real indefinite $M$ (3 neg.) | (I1) | $2.641=\|M_-\|_F$ | signature | **fails** (single channel only) |
| three-channel sum of a PSD single channel | inertia | 2 negative eigenvalues | — | no signature bound for (3.11) |

**Interpretation for the objective.** Every kernel the toy can build from surface data
*without* a connected $\mathcal W_3$ fails the factorisation identity for a stated, checkable
reason (rank, parameter count, signature, divergence), and each failure sits exactly at its
analytic floor (Eckart–Young, $\|M_-\|$) — so the least-squares search is not the weak
point. The one class the toy cannot probe — a connected rigid $\mathcal W_3$ of the
$\Omega_{V_4}(\mu_0)$ type — is precisely the class that survives the counts of §3.7 and is
decided, at the surface level, by the genus argument. The map is therefore:
(β) with a disconnected or rank-limited fixture — dead by counting; (β) with a connected
fixture — not a factorisation of $\mathcal V_{0,4}$ as surfaces, open as a torus/sphere
correlator identity (branched cover).

## Working notes (12c)

None outstanding: the parity lemma (Lemma 3.3) and the surviving combinations (β1)–(β3)
were found while writing §3.7.3 and promoted there directly. Two remarks not promoted:
(1) the variant (b′) of §3.7.2 ($J$ a 1-form on $\mathcal M_{0,4}$, one tube length on
$\mathrm{Sym}^2\mathcal H_0$) fails Lemma 3.3's parity and was not pursued; (2) the bug found
and fixed in the script during 12c was in the *check* (the $\Sigma$-space kernel $g$ must be
truncated to $r\times r$ when $W$ has $r$ rows), not in any result — recorded per the
diagnose-before-fix rule.

## Verification (12c)

Script `codes/verify-geometric-inverse.py`, part 3, seed 20260908, **106/106 PASS**
(68 part 1 + 24 part 2 + 14 part 3), exit 0; summary of part 3 pasted in §4.3. Method:
finite-dimensional toy on $\mathrm{Sym}^2\mathbb C^3$; every identity is one that can fail
(I1)–(I4); no candidate is built from $M^{-1}$; the Eckart–Young and $\|M_-\|$ floors are
independent analytic yardsticks against which the numerical residuals are compared (they
agree to four digits — a falsifiable statement that would fail if the optimiser were
stuck). Break-on-purpose legs: the rank-$N$ Takagi control (the fit *can* reach $10^{-15}$),
the generated-$V_4$ control recovered to $10^{-13}$ and its $10^{-2}$ perturbation caught,
the level-diagonal and diagonally-dominant controls for (I3)/(I4).
- Machine-checked: rank bounds (1)–(2), disconnected-$\mathcal W_3$ failure (3), Prop. 3.2 with
  the (3.14) profile (4), Neumann divergence (5), signature bound and its absence in the
  three-channel sum (6); the positivity of $g(\lambda)$ on the levels used (entire, §3.7.5)
  is implicit in (6).
- Not machine-checked (and stated as such): counts (i)–(iv) of §3.7 are integer
  bookkeeping by (1.5) and (1.1) (the rule itself is checked in part 1); the genus of the
  composite (008 (B.2), R27, verified there); the BRST identities of §3.7.5 (standard); the
  existence or non-existence of a *connected* $\mathcal W_3$ satisfying (3.13) — the toy is
  blind to it (§4.1), and it is left open as the branched-cover question.


---

## 5. The three cases compared: what "geometric" can mean for the auxiliary channel (12d)

**Literal task (12d).** Write §5–§8: the cases (α)/(β)/(γ) compared in one table with a
precise statement of what "geometric $1/m_2$" can and cannot mean in each; the hand-offs
to Tasks 13 and 14 as precise questions with the counts done; the self-review; the
proposed ledger text; and the finalised §0 table with a five-line summary.

**Motivating objective (restated).** The question is whether the auxiliary channel
has *any* honest geometry, and under which redefinition. The answer needed is the
map: for each case, the obstruction or the construction, so that (α), (β) and (γ) can be compared — not "R28 stands".

**Inherited choices (from the 12c Status line).** The identity tested is the three-channel
sum (3.11); the (β) fixture is (β2) of §3.7.3, eq. (3.13): rigid $\mathcal W_3=\Omega_{V_4}(\mu_0)$
and the diagonal tube $b_1b_2b_1^-b_2^-\,(1-e^{-\lambda L_{\rm tot}})/L_{\rm tot}$ on
$\mathcal S_{\rm pair}$; the open item is the branched-cover question of §3.7.3.

### 5.1 What "geometric" can mean — three precise readings

"Geometric $1/m_2$" has been used in the project for three logically different
statements. For a map $K:\mathrm{Sym}^2\mathcal H_0\to\mathrm{Sym}^2\mathcal H_0$ (or on
$\mathcal S_{\rm pair}$) with $N_{\rm gh}(K)=-2$, they are:

- **(G-i) Surface kernel.** $K$ *is* the sewing form of a (family of) Riemann surface(s)
  of the single $c=26$ CFT with its antighost measure: the 022 class, or its §2 extension
  (disconnected pieces, half-frozen moduli, non-sewing $b$ insertions; §1.3 rows 1–14).
  Falsifiable test: ghost count (§1.3), moduli count, and the identity $V_4\circ K=G_2$
  (or (3.11)) where it can fail.
- **(G-ii) Factorisation geometry** (the Erbin–Fırat sense, R3/§3.7.1). $K$ is not a
  surface; the *kinetic operator* $K^{-1}$ is *defined* as the inverse of a bounded tube
  family, and the geometry is the statement $V_4=\mathrm{Sym}[J\circ K\circ J]$ with $J$
  surface data (rigid or integrated vertex slices). Falsifiable test: (3.11)/(3.13) with
  $J$ restricted to surface type; the tautology trap is avoided because $K$ is chosen
  *before* $V_4$ is looked at.
- **(G-iii) Correlator identity.** The composite $J\circ K\circ J$ is a surface family of
  a *different* topology (here: a 2-parameter family in $\mathcal M_{1,4}$ with six
  unintegrated antighosts) that nevertheless evaluates, on all external states, to the
  $\mathcal V_{0,4}$ family — geometry in a covering or orbifold CFT rather than in the
  single CFT. Test: not yet formulated as a computation; it is the branched-cover
  question (§3.7.3, §6.1).

Reading (G-i) is what R28 and §3 address; (G-ii) is what 12c's counts address; (G-iii)
is the only reading left open by this record. The three cases of the objective differ
in which readings are even available:

| case | auxiliary | $K$ fixed by | (G-i) | (G-ii) | (G-iii) |
|---|---|---|---|---|---|
| (γ) | $\Sigma\in\mathrm{Sym}^2\mathcal H_0$, kinetic $m_2=G_2^{-1}V_4$ | $V_4$ (algebraic inverse) | excluded (R28 + §3) | void (Prop. 3.2) | only as the Neumann chain, R27 (ii) |
| (β) | $\Sigma\in\mathcal S_{\rm pair}$ (or $\mathrm{Sym}^2\mathcal H_0$), kinetic $=K^{-1}$ | chosen tube | not asked ($K$ is a tube by construction) | **obstruction** at surface level (genus 1 vs 0, §3.7.6) | **open** |
| (α-rev) | $\Phi\in\mathcal H$ (single strand), kinetic $=\mathsf P_{[0,\lambda]}^{-1}$, reversed range | chosen bounded cylinder | $K$ is the cylinder, row 4 | to be computed (Task 14) | not needed (same topology) |

The one-sentence answer to this question follows from the table and is proved in
§5.2–5.4: **for the auxiliary as it stands (γ), no reading of "geometric" applies to
$1/m_2$, and (γ) reproduces $V_4$ exactly and is purely algebraic; geometry for the
auxiliary channel exists only after redefining the kinetic term as the inverse of a
chosen propagator — as a factorisation (G-ii) it is available in the single-strand case
**(α-rev)**, the reversed-range prescription of §5.4, which keeps the same topology on
both sides and is an open computation conditional on the coordinate-extension
precondition of §5.4/§6.2, while **(α-neck)**, the faithful Erbin–Fırat transplant
(§3.5), is consistent but leaves $\mathcal V_{0,4}$'s interior untouched and so does not
by itself make the theory cubic; in the double-strand case (β) it is provably not a
factorisation of surfaces and survives only as the correlator identity (G-iii), i.e.
(β) $\Leftrightarrow$ Q13 (§6.1).**

### 5.2 Case (γ): the present $V_4$-kinetic auxiliary

*Data.* $m_2=G_2^{-1}V_4$ on $\mathrm{Sym}^2\mathcal H_0/\ker V_4$, $\gamma(m_2)=+2$ (row 16),
$\gamma(m_2^{-1})=-2$, $S(m_2^{-1})=12$ (row 17); $V_4$ carries two integrated real moduli.

*What "geometric" cannot mean here — the obstruction per reading.*

1. (G-i), 022 class: $\gamma=2+\nu_f\ge2\ne-2$ (R28, row 13). Extended class, §3:
   product kernels (row 7/8, $\gamma=-2$ ✓, 4 moduli): rank across strands for $\hat
   k\otimes\hat k$, Prop. 3.1 (the polarised undressed case is Prop. 3.2's, the polarised
   dressed case only §5.6's); diagonal/half-frozen (rows 9a/9b/5$^{\otimes2}$): commutant,
   Prop. 3.2 — every tube-only kernel is level-diagonal per strand, $m_2$ is not; explicit
   ghosts (row 14, $n_x=4$): homogeneity (3.8), degree $+1+g$ vs $-1$ in the vertex data,
   as a **uniform construction** (§5.6; no $t=1$ obstruction is exhibited for the actual
   $V_4$ alone); Laplace $t$: not a worldsheet length (Lemma 2.2, T2). The entrance
   condition of §2.3 (two independent $b_0^+$, nothing ghost-positive on top) is met only
   by the tube-type rows, and those fail the factorisation identity for a structural
   reason each.
2. (G-ii): void. The Erbin–Fırat move needs $m_2$ *to be* the inverse of a tube family;
   Prop. 3.2 shows no tube family (bounded or not, diagonal or product) has $V_4$'s
   non-diagonal level structure. Applying the move here would mean replacing $m_2$ — that
   is case (β), not (γ).
3. (G-iii): the only surface-flavoured expansion is the Neumann chain
   $m_2^{-1}=\sum_n(D^{-1}N)^nD^{-1}$ (R27 (ii), R28): the $n$-th term is a genus-$n$
   frozen-neck chain (surface data, $\gamma=+2n$) threaded on $n+1$ algebraic $D^{-1}$
   factors ($\gamma=-2(n+1)$). Not geometric in any reading, and in the toy it diverges
   ($\rho(D^{-1}N)=2.48$, §4.3) — its convergence would be a spectral hypothesis on $V_4$
   on top of H1/H2 of R29.

*What integrating out reproduces.* $V_4$ exactly, coefficient 1, by the telescoping
identity (R29) under H1 (left inverse on the quotient) and H2 (completeness of the
$\mathrm{Sym}^2$ sum). This is the defining virtue of (γ): the quartic vertex is
reproduced with no error term and no new parameter.

*Obstruction or open point.* No geometric open point remains for $m_2^{-1}$ in (γ): every
reading has a proof of obstruction (R28; Prop. 3.1 for $\hat k\otimes\hat k$, Prop. 3.2; (3.8) as a uniform construction; Lemma 2.2; §5.6 uniformly over the enlarged class). The open
points are spectral, not geometric: (i) H1/H2 in the untruncated theory (R29); (ii) the
Laplace form $\int_0^\infty dt\,e^{-tm_2}$ is conditional on the spectrum of $m_2$ (R15);
if $m_2$ has an indefinite spectrum at some level — an unverified, uncited claim,
since R15 itself records the sign as open — the
$t$-integral would not converge on all of $\mathrm{Sym}^2\mathcal H_0$ without a contour
choice, so even the *target-space* worldline reading of $m_2^{-1}$ (T2) is conditional on
a sign question that is open, not settled.

*What it buys for classical solutions.* Algebra only. The action is cubic, the $\Sigma$
equation is algebraic ($\Sigma\propto m_2^{-1}(\Psi\otimes\Psi)$ on the quotient), and
substituting it back gives the quartic equation of motion of the $V_4$ theory. What
(γ) does *not* offer is a propagator picture for $\Sigma$: no Schwinger parameter that
is a worldsheet length, hence no wedge-state/sliver-type algebra for the auxiliary
sector, no analytic solution technology transplanted from Witten's OSFT along the
$\Sigma$ line (R27's OSFT mapping applies to the $\Psi$ line). The gain is that the
$\Sigma$ sector is *finite-dimensional per level* and purely algebraic — level-truncated
solutions of the cubic system are a polynomial problem of lower degree than the quartic
one, at the price of a quadratic growth in the field content: $\mathrm{Sym}^2$ of $N$
level-truncated states has $N(N+1)/2$ components, not $2N$.

### 5.3 Case (β): double strand, kinetic term = inverse of a bounded double tube

*Data (fixture (β2), §3.7.3, Lemma 3.3).* Auxiliary $\Sigma\in\mathcal S_{\rm pair}$ (pair-level-matched,
$b^-_{\rm tot}$-annihilated; not $\mathrm{Sym}^2\mathcal H_0$). Propagator
$K=b_1b_2\,b_1^-b_2^-\,(1-e^{-\lambda L_{\rm tot}})/L_{\rm tot}$: $n_b=4$, $n_\mu=2$ (one shared
length $s\in[0,\lambda]$, one shared twist), $\gamma(K)=-2$ ✓, entire in $L_{\rm tot}$ (§3.7.5).
Kinetic operator $K^{-1}=c_1^+c_2^+\,L_{\rm tot}/(1-e^{-\lambda L_{\rm tot}})$ (on the
complement of $\ker L_{\rm tot}$), $\gamma=+2$ ✓ $=\gamma(m_2)$. Vertices: rigid
$\mathcal W_3=\Omega_{V_4}(\mu_0)$, the $V_4$ integrand at one point of $\mathcal P_{0,4}$ with its two
Beltrami antighosts unsoaked (row 12), $\gamma=+2$, zero moduli. Composite:
$2m_J+n_\mu(K)=2=\dim_\R\mathcal M_{0,4}$ ✓; $2n_b^J+n_b(K)=8=\dim_\R\mathcal M_{1,4}$ (eq. 3.12).

*What integrating $\Sigma$ out reproduces.* Not $V_4$, but
$\widetilde V_4:=\mathrm{Sym}_{S_4}[\Omega_{V_4}(\mu_0)\circ K\circ\Omega_{V_4}(\mu_0)]$, eq. (3.13): a
2-real-parameter family of four-punctured *tori* (sphere $\cup_{\rm two\ tubes}$ sphere,
008 (B.2)) carrying the full 8-antighost measure of $\mathcal M_{1,4}$ but integrated over
two of its eight directions. The exchange collapses to a contact term with the right
ghost number and the right number of moduli — and the wrong topology.

*Obstruction (proven).* As a factorisation of surfaces, (3.13) is false for every rigid
or integrated $J$ and every tube (bounded, unbounded, diagonal, product): genus is a
topological invariant of the glued surface, and $\mathcal V_{0,4}\subset\mathcal M_{0,4}$
(§3.7.6 (G1)). The toy of §4 confirms the count-level part: every fixture the toy can
build — disconnected $\mathcal W_3$, real-positive $g$, and a rank-limited $P$ that is not itself
a geometric object — fails (3.11)/(I1) at its analytic floor (§4.3).

*Open point.* (G-iii): whether the torus family, evaluated on all external states of the
single CFT, equals the sphere family — plausible only in the picture $\Sigma_{1,4}\to\Sigma_{0,4}$
as a double cover branched at the four punctures with the two strands as the two
sheets, the six unintegrated antighosts being the ghost number of four branch-point
(twist-field) insertions. This is the yes/no question of §6.1. Its $\lambda\to0$ slice is
R27's frozen-neck chain of length 2, so a "yes" would also give R27's resolved genus a
CFT meaning.

*Concrete correlator-level obstruction (feeds §6.1's hand-off).* Independently of the
branched-cover picture, the composite carries a piece $V_4$ does not: the intermediate sum
over $\mathcal S_{\rm pair}$ in $\langle J(\Psi_1\Psi_2),K^{-1}J(\Psi_3\Psi_4)\rangle$ runs
over the pair's *relative momentum* ($k_a$ free, $k_b=-k_1-k_2-k_a$), i.e. the composite
carries a genuine $\int d^Dk_a$ — the torus's loop momentum — absent from the tree-level
$\mathcal V_{0,4}$ integral (§3.7.3). This is what "genus 1" means physically and gives a
cheap route to a "no" independent of the $\lambda$-function computation: compare the
analytic structure in the external momenta (pair-channel thresholds from
$\int d^Dk_a\,g(L_a+L_b)$ against none in $\mathcal V_{0,4}$). (BRST note, not checked:
$Q_{\rm tot}$ does not automatically preserve $\mathcal S_{\rm pair}$ —
$[Q_{\rm tot},b^-_{\rm tot}]=L^-_{\rm tot}$ only, so $b^-_{\rm tot}$-annihilation is
preserved on $\ker L^-_{\rm tot}$, but the kinetic operator's $c_1^+c_2^+$ form is
Siegel-gauge on both strands, which on $\mathcal S_{\rm pair}$ needs the stronger
condition $b_1^+=b_2^+=0$, not merely pair-level matching.)

*What it buys for classical solutions — conditional on (G-iii).* If (3.13) holds as a
correlator identity, the $\Sigma$ line acquires a genuine worldsheet Schwinger parameter:
$K=\int_0^\lambda ds\,\int d\theta\,b_1b_2b_1^-b_2^-\,e^{-sL_{\rm tot}+i\theta L^-_{\rm tot}}$ is a
bounded family of diagonal double tubes, and $e^{-sL_{\rm tot}}$ acting on $\mathcal S_{\rm pair}$
generates a wedge-type semigroup on the pair space — the closed-string, two-strand
analogue of the sliver-frame algebra along the auxiliary line. This is the *only* case in
the map where the auxiliary line gets the 2024 "2→2 plumbing fixture" literally (tube
length + twist, one antighost each, plus the two non-moduli antighosts). If (G-iii) fails,
(β) is a different theory from the $V_4$ theory: its quartic effective vertex is
$\widetilde V_4\ne V_4$ off shell, and on shell its 4-point amplitude is not an
$\mathcal M_{0,4}$ integral at all, so it is not a closed SFT of the standard kind.
Either way, (β) is not a representation of the *present* $1/m_2$; it is a candidate
replacement of $m_2$.

### 5.4 Case (α-rev): single strand, reversed-range prescription, structural difference from (β), counts for Task 14

This is **(α-rev)**: the $|q|>1$ prescription intended to cover $\mathcal V_{0,4}$'s
interior and thereby remove the quartic vertex — distinct from **(α-neck)** (§3.5), the
faithful transplant of the Erbin–Fırat mechanism, which covers only the necks and leaves
the interior untouched.

*Data (Task 14's route; ghost numbers from §1.3 rows 2–4 and R23).* Auxiliary
$\Phi\in\mathcal H_0$ (single strand), $N_{\rm gh}(\Phi)=2$ (same as $\Psi$), coupled through
Harold's asymmetric $\mathcal V_3'$ on its special leg: $S_{\rm cub}=\omega_1(\Phi,\mathcal V_3'(\Psi,\Psi))$,
ghost check $2+(2+2-1)=5$ ✓ ($\omega_1$ pairs at 5). Kinetic operator
$\mathcal K_\lambda=Q_B/(1-e^{-\lambda L_0^+})$ on $\mathcal H_0$ (closed transplant of Erbin–Fırat's
$Q_B/(1-e^{-2\lambda L_0})$, §1.4(d) via (C7)), $\gamma(\mathcal K_\lambda)=+1$ (that of $Q_B$);
kinetic term $\omega_1(\Phi,\mathcal K_\lambda\Phi)$, $2+2+1=5$ ✓. Siegel-gauge propagator
$\hat{\mathsf P}_{[0,\lambda]}=b_0^+(1-e^{-\lambda L_0^+})/L_0^+$ as a map ($\gamma=-1$, row 2 with
bounded range), $\mathsf P_{[0,\lambda]}=\hat{\mathsf P}_{[0,\lambda]}\omega_1^{-1}$ as the sewing
object (row 4: $n_b=2$, $n_\mu=2$, $\gamma=-1$); entire in $L_0^+$, value $\lambda b_0^+$ at
$L_0^+=0$, no cohomology carried by $\Phi$ (same argument as §3.7.5 (iv)).

*Composite counts.* $\mathcal V_3'$ as a map $\mathcal H_0^{\otimes2}\to\mathcal H_0$: R23 with
$k=2,\ell=1,g=0$: $\gamma=3-4=-1$; as $\mathcal H_0\to\mathcal H_0^{\otimes2}$ ($k=1,\ell=2$): $+4$.
Exchange $\mathcal V_3'\circ\hat{\mathsf P}_{[0,\lambda]}\circ\mathcal V_3'$: $\gamma=-1-1+4=+2=\gamma(m_2)$ ✓
(R23, $k=\ell=2$); as a 4-form, saturation $6+2=8=S(V_4)$ ✓. Moduli: $0+2+0=2=\dim_\R\mathcal M_{0,4}$ ✓.
Topology: sphere $\cup_{\rm one\ tube}$ sphere $=$ **sphere** ✓. Ghost anomaly: $6$ on both
sides; no missing units. Summed over the three channels with $\Phi$ single-strand, the
exchange is automatically $S_3$-symmetric in the $\Psi$ legs; full $S_4$ symmetry of the
resulting quartic term is a condition on $\mathcal V_3'$ (its special leg is distinguished) —
Task 14 must check it, as the open-string case checks cyclicity.

*Structural difference from (β).* Everything that obstructs (β) at the surface level is
absent in (α-rev): one strand means one tube, one tube means $\chi$ is additive with no
handle, and the composite family lives in the *same* $\mathcal M_{0,4}$ as $\mathcal V_{0,4}$.
The factorisation (G-ii) is therefore a statement about two 2-real-dimensional regions
of $\mathcal M_{0,4}$ — a covering question, decidable by a cross-ratio sweep — not a
statement across genera. The price is that (α-rev) is not a representation of $1/m_2$ either:
it replaces the $\mathrm{Sym}^2$ auxiliary by a single-string one and the quartic vertex
by whatever the sewing family covers, and R2 fixes the boundary of that family: the
$|q|=1$ (twist-only) gluing of two $\mathcal V_3'$ traces $\partial\mathcal V_{0,4}$, so a
bounded neck *inside* the unit disc, $|q|\in[e^{-\lambda},1]$, lies in the Feynman side of
that boundary, and the vertex-region interior $\mathcal M_\times$ is reached only by
$s\in[-\sigma(\theta),0]$, i.e. $|q|\in[1,e^{\sigma(\theta)}]$ — the reversed-range question of
`notes_4_point_summary.tex`. Two counts follow that Task 14 must carry:

- **Reversed range.** With $s\in[-\sigma,0]$ the propagator is
  $b_0^+(e^{\sigma L_0^+}-1)/L_0^+$: same ghost and moduli counts as row 4, still entire in
  $L_0^+$, but the kinetic operator $Q_B\,L_0^+/(e^{\sigma L_0^+}-1)$ is not the Laplace
  transform of a positive measure ($e^{\sigma L_0^+}$ grows). Harmless for a finite-range
  integral; it means the auxiliary's kinetic term is a *definition* of the same kind as
  Erbin–Fırat's, not a Schwinger representation.
- **Twist-dependent bound.** A $\theta$-dependent $\sigma(\theta)$ replaces
  $\int d\theta\,e^{i\theta L_0^-}=2\pi\delta_{L_0^-,0}$ by $\int d\theta\,e^{i\theta L_0^-}(e^{\sigma(\theta)L_0^+}-1)/L_0^+$,
  which is not proportional to $\delta_{L_0^-,0}$: the operator is then not a map on
  $\mathcal H_0$ but on the unconstrained $\mathcal H$, and the auxiliary $\Phi$ must be allowed
  level-mismatched components ($L_0^-\ne0$). $\sigma$ constant $\Leftrightarrow$ $\Phi\in\mathcal H_0$.
  This is a count, not an obstruction; it says the "auxiliary in $\mathcal H$" of plan
  Task 14 must be taken literally if Harold's $\sigma(\theta)$ is non-constant.
- **Coordinate-extension precondition (Task 14's first count, to be checked before the
  cross-ratio sweep).** (α-rev) requires the local coordinate discs of $\mathcal V_3'$ at
  the glued legs to extend to radius $e^{\sigma(\theta)}$ and *remain embedded* — disjoint
  from each other and from the other punctures' discs. For SZ-type vertices the unit
  discs are tangent at $|q|=1$ (this is exactly why R2's $|q|=1$ curve is
  $\partial\mathcal V_{0,4}$), so any $\sigma>0$ risks overlapping coordinate discs on the
  composite, which would be fatal for its use as a *sewable* vertex in five-point Feynman
  regions even if the four-point cross-ratio sweep (6.1) looks fine. This condition is a
  property of Harold's $\mathcal V_3'$ that may decide (α-rev) on paper, before any
  numerical sweep.

### 5.5 Comparison table

| case | auxiliary space | kinetic operator ($\gamma$) | propagator geometry ($\gamma$, moduli) | integrating out reproduces | obstruction or open point | what it buys for classical solutions |
|---|---|---|---|---|---|---|
| (γ) present | $\Sigma\in\mathrm{Sym}^2\mathcal H_0/\ker V_4$, $N_{\rm gh}=4$ | $m_2=G_2^{-1}V_4$ ($+2$), fixed by $V_4$ | none: $m_2^{-1}$ ($-2$) is the algebraic inverse; every surface reading excluded (R28; Prop. 3.1 for $\hat k\otimes\hat k$, Prop. 3.2; (3.8) as a uniform construction; Lemma 2.2; §5.6 uniformly) | $V_4$ exactly, coefficient 1 (R29, under H1/H2) | no geometric open point; spectral ones only (H1/H2 untruncated; Laplace form conditional, R15; Neumann chain diverges in the toy) | algebra only: cubic action, quadratic e.o.m., $\Sigma$ eliminated algebraically; no worldsheet Schwinger parameter, no wedge/sliver algebra on the $\Sigma$ line |
| (β) double strand, redefined | $\Sigma\in\mathcal S_{\rm pair}$ (pair-level-matched), $N_{\rm gh}=4$ | $K^{-1}=c_1^+c_2^+L_{\rm tot}/(1-e^{-\lambda L_{\rm tot}})$ ($+2$), chosen | bounded diagonal double tube $b_1b_2b_1^-b_2^-(1-e^{-\lambda L_{\rm tot}})/L_{\rm tot}$ ($-2$; 2 moduli + 2 non-moduli $b$), entire in $L_{\rm tot}$ | a 2-parameter family of 4-punctured **tori** with the full $\mathcal M_{1,4}$ antighost measure, (3.13) — not $V_4$ as surfaces | **obstruction** (proven): genus 1 vs 0, no surface factorisation of $\mathcal V_{0,4}$ for any $J$, any tube; toy fixtures fail at their floors (§4.3). **Open**: correlator identity via branched double cover (§6.1) | conditional on (G-iii): a literal 2→2 plumbing fixture on the auxiliary line, $e^{-sL_{\rm tot}}$ a wedge-type semigroup on $\mathcal S_{\rm pair}$; otherwise a different theory ($\widetilde V_4\ne V_4$, on-shell 4-point not an $\mathcal M_{0,4}$ integral) |
| (α-rev) single strand, redefined (Task 14) | $\Phi\in\mathcal H_0$ (or $\mathcal H$ if $\sigma(\theta)$ non-constant), $N_{\rm gh}=2$ | $\mathcal K_\lambda=Q_B/(1-e^{-\lambda L_0^+})$ ($+1$), chosen; reversed range $Q_BL_0^+/(e^{\sigma L_0^+}-1)$ | bounded cylinder $b_0^+(1-e^{-\lambda L_0^+})/L_0^+$ ($-1$; 2 moduli: length + twist), entire in $L_0^+$; coupled via rigid $\mathcal V_3'$ ($-1$ / $+4$) | a 2-parameter family of 4-punctured **spheres**: $\sum_{s,t,u}\mathcal V_3'\circ\hat{\mathsf P}\circ\mathcal V_3'$, $\gamma=+2$ ✓, 2 moduli ✓, same $\mathcal M_{0,4}$ as $\mathcal V_{0,4}$ | subject to the coordinate-extension precondition of §5.4/§6.2 (local discs of $\mathcal V_3'$ must extend to radius $e^{\sigma(\theta)}$ and remain embedded); **open, decidable**: does the bounded-neck family of two $\mathcal V_3'$ cover $\mathcal M_\times$ (complement of the $|q|\le1$ regions of the same family, R2) exactly once? A cross-ratio sweep answers it (§6.2); $S_4$ symmetry of the sum is a further condition on $\mathcal V_3'$ | if yes: the quartic vertex becomes a cubic one with a single-string auxiliary whose propagator is an honest bounded cylinder — Erbin–Fırat's payoff transplanted (analytic-solution technology along $\Phi$ as along $\Psi$); the auxiliary is not $\mathrm{Sym}^2$ and $m_2$ disappears |

**Reading of the map.** The row that answers "is there any honest geometry for the
auxiliary channel" is not (γ): $1/m_2$ has none, in any reading, with a proof per
reading (the explicit-ghost and mixed tube/slice cases as uniform constructions only). Geometry enters only through a *redefinition of the kinetic term as the inverse
of a chosen propagator*. A third redefinition, (α-neck) (§3.5), is the faithful Erbin–Fırat transplant: it is consistent, but it covers only the necks and leaves $\mathcal V_{0,4}$'s interior as an elementary quartic vertex, so it does not by itself make the theory cubic. Of the redefinitions that would remove the quartic vertex, (α-rev) keeps the topology and turns
the question into a moduli-space covering computation (subject to the coordinate-extension
precondition of §5.4); (β) keeps the $\mathrm{Sym}^2$ structure
(and the IBL/BV apparatus of the paper) but changes the genus, and survives only if a
torus/sphere correlator identity holds. The two are not competing representations of
the same object; they are two different cubic theories, and only (γ) is guaranteed to
reproduce $V_4$.

### 5.6 R28 over the enlarged class of §2: sharpened statement

R28 (022) proves $\gamma=2+\nu_f\ne-2$ for the 022 class. §3 excluded each extension of
§2 by a different argument (rank, commutant, homogeneity, grading). One argument covers
the whole enlarged class at once, and it is R28's Angle 2 made uniform:

*Scaling lemma.* Let $\mathcal C$ be the set of kernels $K:\mathrm{Sym}^2\mathcal H_0\to\mathrm{Sym}^2\mathcal H_0$
that are finite sums of compositions of (i) vertex data of the $V_4$ theory — integrated
vertices, rigid or half-frozen slices $\Omega_{V_4}(\mu)$, with any number of extra
$b$-insertions — and (ii) $V_4$-independent operators: tubes of any kind with
$V_4$-independent bounds, frozen or doubly-frozen nodes, $G_2$, $G_2^{-1}$, explicit
ghost modes. Under $V_4\to tV_4$ ($t\ne0$), each term of $K\in\mathcal C$ scales as $t^{d}$
with $d\in\mathbb Z_{\ge0}$ the number of vertex-data factors it contains, while
$m_2^{-1}\to t^{-1}m_2^{-1}$. If $K=m_2^{-1}$ for the family $tV_4$, then
$\sum_d t^{d+1}K_d=m_2^{-1}(1)$ for all $t$, a polynomial identity in $t$ with zero constant
term on the left and a nonzero constant on the right: contradiction. $\square$

*Scope and what it does not cover.*
- It requires the construction to be *uniform* in the vertex data (to hold for the
  family $tV_4$ — the weakest uniformity one can ask; $tV_4$ is not itself a consistent
  vertex, but any kernel built "from surface data" must not know that). A kernel
  fine-tuned to one $V_4$ is not excluded by scaling; for that case the $t=1$
  arguments of §3 apply: rank (Prop. 3.1) for products of the form $\hat k\otimes\hat k$,
  commutant (Prop. 3.2) for tube-only kernels, Cayley–Hamilton floor (R28 Angle 3) for
  fixed-degree polynomials. Candidate (c) (eq. (3.8), explicit ghost insertions) has **no**
  $t=1$ obstruction: it is excluded only as a uniform construction (§3.3).
- It does not cover $V_4$-*dependent* moduli bounds ($\lambda=\lambda(V_4)$): a tube with
  $\lambda\propto t^{-1}$ scales as $t^{-1}$ at leading order ($\mathsf P_{[0,\lambda]}\to\lambda\,b_0^+b_0^-\delta$),
  so tube$\circ\Omega\circ$tube has degree $-1$. But then the bound *is* the algebraic
  inverse in disguise (a scalar function of $V_4$'s spectrum, R27's $D^{-1}$ threading in
  another guise), and at $\lambda\to0$ the kernel is a scalar times R27's frozen chain of
  length 2, excluded by the Cayley–Hamilton floor. This is the precise boundary of
  "geometric": *moduli bounds are geometric data only if they are independent of $V_4$.*
- It does not cover infinite sums (the Neumann chain, R27 (ii), degree $-1$ term by term
  because of the $n+1$ algebraic $D^{-1}$ factors) — not geometric by construction.
- It says nothing about (β)/(α-neck)/(α-rev), where the identity tested is not $V_4K=G_2$
  but a factorisation $V_4=J\circ K\circ J$ with $K$ fixed *before* $V_4$; scaling there
  constrains $J$ ($J\propto t^{1/2}$), not $K$.

*R28 sharpened (R28$'$).* Over the enlarged class of §2, no construction *uniform in the
vertex data* (one that would also invert $tV_4$) equals $m_2^{-1}$: this is the scaling
lemma above (script part 4, Vandermonde floor with break-on-purpose). At the actual $V_4$
(i.e. at $t=1$), individually: product kernels (Prop. 3.1, for $\hat k\otimes\hat k$),
tube-only kernels of any measure (Prop. 3.2), and the Laplace reading (Lemma 2.2) are
excluded; ghost grading excludes the 022 class (R28) at every $t$. Explicit-ghost
dressings (3.8) and mixed tube/slice kernels are excluded **only** as uniform
constructions — no $t=1$ obstruction is exhibited for them here. The remaining geometric
option for the auxiliary channel is a change of kinetic term, (α-neck)/(α-rev) or (β),
which changes the identity to be satisfied rather than the kernel. Machine check of the
scaling lemma: script part 4 (§7).

## 6. Hand-offs (12d)

### 6.1 To Task 13 (branched covers): the one yes/no question

*Set-up handed over (all from §3.7.3–3.7.6, fixture (β2)).* $\Sigma_{1,4}(s,\theta)$ := the
surface obtained from two copies of the rigid four-punctured sphere $\Omega_{V_4}(\mu_0)$
— punctures $\{1,2,a,b\}$ on the first, $\{3,4,a',b'\}$ on the second — by gluing
$a\sim a'$ and $b\sim b'$ with the *same* plumbing parameter $q=e^{-s+i\theta}$ on both
necks (the diagonal tube of (β2): one shared length $s\in[0,\lambda]$, one shared twist). It is
a four-punctured torus (008 (B.2), R27) carrying eight antighosts: two Beltrami $b$'s per
slice, two $b^+$ and two $b^-$ on the tubes, of which only $b(\partial_s)$, $b(\partial_\theta)$
are soaked by an integration. The ghost anomaly is $0$ on the torus and $6$ on the sphere
$\mathcal V_{0,4}$ it is supposed to reproduce; the six unsoaked antighosts are the
difference. The $\lambda\to0$ slice is R27's frozen chain of length 2 ($k=2$, $g=1$).

*The question (yes/no).*

> **Q13.** For the (β2) fixture, does $\Sigma_{1,4}(s,\theta)$ admit, for all
> $(s,\theta)\in[0,\lambda]\times S^1$, a holomorphic involution $\iota$ that exchanges the two
> necks (the two strands, $a\text{-neck}\leftrightarrow b\text{-neck}$) and has exactly the
> four external punctures $1,2,3,4$ as fixed points — so that $\Sigma_{1,4}(s,\theta)\to
> \Sigma_{1,4}/\iota\cong\Sigma_{0,4}$ is the double cover branched at the four external
> punctures with the two strands as the two sheets — **and** is the quotient family
> $\{\Sigma_{1,4}(s,\theta)/\iota\}$, as $(s,\theta)$ ranges over $[0,\lambda]\times S^1$, the
> $\mathcal V_{0,4}$ family (a 2-real-dimensional region of $\mathcal M_{0,4}$ with the
> correct boundary)?

*Counts done here that constrain the answer.*
- Riemann–Hurwitz: $\chi(T^2)=0=2\chi(S^2)-b\Rightarrow b=4$ branch points — the four
  external punctures are exactly the right number; no other fixed points allowed.
- Existence of $\iota$ on each slice: $\iota$ restricted to sphere 1 is a Möbius involution
  fixing $1,2$ and swapping $a\leftrightarrow b$; it exists iff the pair punctures are
  harmonic with respect to the external ones, cross-ratio $(1,2;a,b)=-1$ (and likewise
  $(3,4;a',b')=-1$), a condition on the rigid slice $\mu_0$ and on the local coordinates
  at $a,b$ (they must be exchanged by $\iota$, up to the phase absorbed by the twist).
  So "yes" is possible only for a symmetric choice of $\mu_0$, which Task 13 must state.
- Compatibility with the tube: $\iota$ swaps the necks, so it requires equal plumbing
  parameters on both — precisely the *diagonal* tube (shared $s,\theta$) and not the
  product tube (β1). This is why (β2) rather than (β1) is the fixture handed over; the
  product tube cannot be a double cover for generic $(q_a,q_b)$.
- The quotient's position in $\mathcal M_{0,4}$: the torus modulus $\tau(s,\theta)$ determines
  the branch cross-ratio through the modular $\lambda$-function, $x=\lambda(\tau)$; the
  region swept by $x(s,\theta)$ for $s\in[0,\lambda_{\max}]$ is what must be compared with
  $\mathcal V_{0,4}$, whose boundary is R2's $|q|=1$ curve. Task 13 should locate
  $x(0,\theta)$ (the frozen chain) relative to $\partial\mathcal V_{0,4}$ first — this is
  the worked $k=2$ example the plan asks for.
- Anomaly bookkeeping to check in the covering picture: the torus correlator of one
  $bc$ system equals a sphere correlator of the $\mathbb Z_2$-orbifold of two $bc$ systems
  (untwisted $b^+c^+$, antiperiodic $b^-c^-$) with four twist fields; sphere saturation for
  two systems is $12$, the external states pulled back supply what they supply on the
  torus. **Assumption used:** this forces total twist-field ghost number $6$ ($3/2$ each in
  the covering-theory grading) only if the six unsoaked antighosts of §3.7.3 are absorbed
  into the twist-field vertex operators themselves; if instead they remain as separate
  insertions on the cover, the count is $12$ ($3$ each). Task 13 must state which reading
  applies before comparing with the bosonised $\mathbb Z_2$ twist field of the antiperiodic
  $\lambda=2$ system (background charge $Q=-3$) and reporting match or mismatch; a mismatch
  is a "no" to the second half of Q13 independent of the first.
- **Loop-momentum content (a cheap route to "no", independent of the counts above).**
  The (β2) composite carries a piece $\mathcal V_{0,4}$ does not: the intermediate sum
  over $\mathcal S_{\rm pair}$ inside $\langle J(\Psi_1\Psi_2),K^{-1}J(\Psi_3\Psi_4)\rangle$
  runs over the pair's relative momentum ($k_a$ free, $k_b=-k_1-k_2-k_a$), i.e. a genuine
  $\int d^Dk_a$ — the torus's loop momentum (§3.7.3) — absent from the tree-level
  $\mathcal V_{0,4}$ integral. This is the correlator-level content of "genus 1 vs 0" and
  can be tested independently of the $\lambda$-function computation above: compare the
  analytic structure in the external momenta (pair-channel thresholds from
  $\int d^Dk_a\,g(L_a+L_b)$, absent in $\mathcal V_{0,4}$). See Lunin & Mathur (2001),
  hep-th/0006196, for the covering-space dictionary this test and the branched-cover
  picture both rest on.

*What a "yes" and a "no" mean for the map.* Yes: (β) is a construction — the auxiliary
line has an honest 2→2 plumbing fixture, and (3.13) holds as a correlator identity of
the covering theory; R27's resolved genus becomes literal. No: (β) is excluded as a
representation of the $V_4$ theory (the toy and the genus argument then close every
reading), and the map reduces to (α-rev)/(α-neck) as the only live geometric option.

### 6.2 To Task 14 (the $\mathcal V_3'$ route): counts and the identity to test

*Counts (from §5.4; all in the physical grading of §1.1).*

| object | space | $N_{\rm gh}$ / $\gamma$ | moduli | remark |
|---|---|---|---|---|
| auxiliary $\Phi$ | $\mathcal H_0$ ($\mathcal H$ if $\sigma(\theta)$ non-constant) | $2$ | — | single strand; same ghost number as $\Psi$ |
| $\mathcal V_3'$ as $\mathcal H_0^{\otimes2}\to\mathcal H_0$ (special leg out) | — | $-1$ (R23, $k=2,\ell=1$) | 0 | rigid; cubic term $\omega_1(\Phi,\mathcal V_3'(\Psi,\Psi))$ at saturation 5 ✓ |
| $\mathcal V_3'$ as $\mathcal H_0\to\mathcal H_0^{\otimes2}$ (special leg in) | — | $+4$ ($k=1,\ell=2$) | 0 | |
| kinetic $\mathcal K=Q_B\,L_0^+/(e^{\sigma L_0^+}-1)$ (reversed range; $\to Q_B/(1-e^{-\lambda L_0^+})$ for $[0,\lambda]$) | $\mathcal H_0$ | $+1$ | — | kinetic term at saturation $2+2+1=5$ ✓; not a positive Laplace transform for $\sigma>0$ |
| propagator $\hat{\mathsf P}=b_0^+(e^{\sigma L_0^+}-1)/L_0^+$ | $\mathcal H_0$ | $-1$ (row 2/4) | 2 (length $\in[-\sigma,0]$, twist) | entire in $L_0^+$; $\sigma b_0^+$ at $L_0^+=0$; no cohomology |
| exchange $\mathcal V_3'\circ\hat{\mathsf P}\circ\mathcal V_3'$, one channel | $\mathcal H_0^{\otimes2}\to\mathcal H_0^{\otimes2}$ | $+2=\gamma(m_2)$ ✓; 4-form saturation 8 ✓ | $2=\dim_\R\mathcal M_{0,4}$ ✓ | topology sphere ✓; anomaly 6 = 6 ✓ |
| three channels summed | | | | $S_3$ in the $\Psi$ legs automatic; full $S_4$ is a condition on $\mathcal V_3'$ |

*The identity to test (two levels, both required by plan Task 14 (i)–(ii)).*

1. *Regions.* With $\mathcal F'_\alpha:=\{Z_4^{(\alpha)}(q):|q|\le1\}$ the Feynman regions of the
   $\mathcal V_3'$ family itself (R2 gives $\partial\mathcal F'_\alpha$ at $|q|=1$) and
   $\mathcal M'_\times:=\mathcal M_{0,4}\setminus\bigcup_\alpha\mathcal F'_\alpha$,
   $$
   \bigcup_{\alpha=s,t,u}\Big\{Z_4^{(\alpha)}\big(e^{\sigma+i\theta}\big):\ \sigma\in[0,\sigma(\theta)],\ \theta\in S^1\Big\}\overset{?}{=}\mathcal M'_\times
   \quad\text{once, without overlap,}
   \tag{6.1}
   $$
   for some bound $\sigma(\theta)\ge0$ — the reversed-range question. Reported as a region
   per channel with sampling density, gap and overlap measured against $\mathcal M'_\times$.
2. *Operators.* With $\Phi$ integrated out,
   $$
   V_4^{(\alpha)}[\Psi]:=\sum_{\alpha}\omega_1\!\big(\mathcal V_3'(\Psi,\Psi),\ \hat{\mathsf P}_{[-\sigma,0]}\,\mathcal V_3'(\Psi,\Psi)\big)
   \overset{?}{=}\int_{\mathcal M'_\times}\Omega_{V_4}
   \tag{6.2}
   $$
   on shell (four tachyons at generic momenta suffice), where the right-hand side is the
   $\mathcal M'_\times$ integral of the SZ measure — the closed analogue of Erbin–Fırat's
   $V_4^{\rm stub}=V_3\circ P_{[0,2\lambda]}\circ V_3$. (6.2) can fail even if (6.1) holds
   (wrong local coordinates on $\mathcal M'_\times$, or the $S_4$ condition), and (6.1) can
   fail with (6.2) holding on shell only by accident; both are to be reported.

*Three counts Task 14 must carry (§5.4).* (i) The bound $\sigma$ must be constant for
$\Phi\in\mathcal H_0$; a $\theta$-dependent $\sigma(\theta)$ (the general form of Harold's
question) forces $\Phi\in\mathcal H$ with level-mismatched components and the twist
projector replaced by $\int d\theta\,e^{i\theta L_0^-}(e^{\sigma(\theta)L_0^+}-1)/L_0^+$ — a
departure from the $b_0^-,L_0^-$ constraints, to be stated if used. (ii) The tautology
guard of §4.1 transplants unchanged: $\hat{\mathsf P}$ is fixed before $V_4$ is looked at, and
(6.2) is tested against an $\mathcal M_{0,4}$ integral it can fail. (iii) **The
coordinate-extension precondition (§5.4), to be checked first, before the cross-ratio
sweep (6.1).** (α-rev) requires the local coordinate discs of $\mathcal V_3'$ at the glued
legs to extend to radius $e^{\sigma(\theta)}$ and remain embedded; for SZ-type vertices the
unit discs are tangent at $|q|=1$, so any $\sigma>0$ risks overlapping discs on the
composite, fatal for its use as a sewable vertex in five-point Feynman regions even if
(6.1) looks fine on the four-point cross-ratio sweep alone.

*Structural remark for the verdict.* (α-rev) is the only case in the map whose factorisation
question lives in one moduli space; a "no" to (6.1) for every $\sigma(\theta)$ is a
covering obstruction of the same kind as SZ's, not a ghost or genus one, and would leave
(γ) as the only cubic theory that reproduces $V_4$.

## 7. Self-review (12d)

**1. Objective versus literal task.** The literal task (§5–§8, §0 final) is done. The
objective — a map with an obstruction or a construction per option, so that the options can
be compared — is answered by §5.5 and §5.1's one-sentence verdict: no geometry for $1/m_2$ in
(γ), with a proof per reading (R28, Prop. 3.1/3.2, (3.8), Lemma 2.2, and the scaling
lemma of §5.6 uniformly over the enlarged class); geometry only under a change of
kinetic term, where (α-rev) is an open computation in one moduli space (conditional on
the coordinate-extension precondition of §5.4), (α-neck) is consistent but does not by
itself make the theory cubic, and (β) is an open correlator identity across genera. What
is *not* delivered is a decision between (α-rev)/(α-neck) and (β): both are handed off as
yes/no questions (Q13, (6.1)/(6.2)), and the map is honest about that. The 2024
"2→2 plumbing fixture" is located precisely: it is (β2), it survives every count, and it
lives or dies with Q13.

**2. Weakest step.** The scaling lemma's uniformity assumption (§5.6): a kernel built from
surface data is required to work for the family $tV_4$. This is the weakest link
because $tV_4$ with fixed $V_3$ is not a consistent SFT vertex, so a critic can ask
whether a construction fine-tuned to the *actual* $V_4$ (which satisfies the BV
boundary condition) escapes. The shoring up: at $t=1$, product kernels (Prop. 3.1),
tube-only kernels (Prop. 3.2, commutant) and R28's grading each have their own $t=1$
obstruction; candidate (c) (eq. (3.8), explicit ghost insertions) does **not** — it is
excluded only as a uniform construction, and the script's `explicit-ghost-scaling` leg
exhibits the $t=1$ loophole explicitly (an involutive $M$ with $B=B'=1$ inverts $M$
exactly at $t=1$). The toy of §4 tested the actual identity at $t=1$ with generic
$S_4$-symmetric data, for the classes it can build. The residual gap is a construction
that uses the BV relation between $V_4$ and $V_3\circ V_3$ — i.e. one that knows
$\partial\mathcal V_{0,4}$ — and that is exactly the $\mathcal V_3'$ route (α-rev), which
is handed off rather than excluded. Second weakest: the $3/2$-per-twist-field count in
§6.1 is a bookkeeping requirement derived from saturation *under the assumption* that the
six unintegrated antighosts are absorbed into the twist fields (§6.1), not a computed
twist-field charge; it is handed to Task 13 as a check, not asserted.

**3. Not checked, and why acceptable.** (i) The covering-theory anomaly of §6.1 (bosonised
twist-field charge) — CFT-level, Task 13's deliverable. (ii) The $S_4$ symmetry of the
three-channel $\mathcal V_3'$ exchange — depends on the explicit maps, Task 14's
deliverable. (iii) Whether the (β2) kinetic operator $c_1^+c_2^+L_{\rm tot}/(1-e^{-\lambda L_{\rm tot}})$
is BRST-compatible on $\mathcal S_{\rm pair}$ (the analogue of $[Q_B,\mathcal K_\lambda]=0$) —
12c's (iv) checked the propagator's on-shell content, not the kinetic operator's
$Q$-commutator; irrelevant unless Q13 is answered "yes", at which point it is the first
thing to do. (iv) The scaling lemma's script check is a finite-dimensional
linear-algebra floor; it verifies the *lemma*, not that any specific CFT object is
polynomial in $V_4$ — that classification is by inspection of §1.3's rows (each is
either $V_4$-independent or a slice/integral of $V_4$'s own measure).

**4. What a stronger physicist would find in five minutes.** (a) That (β)'s obstruction
and Q13 are the same statement seen from two sides — the six missing units *are* the
genus — so the branched-cover question is not an extra loophole but the only form in
which (β) can be true; the map should therefore be read as "(β) ⇔ Q13". Stated in
§5.3/§6.1. (b) That the harmonic condition $(1,2;a,b)=-1$ makes Q13's first half a
constraint on $\mu_0$ that can be checked on paper in Task 13's first hour, before any
$\lambda$-function computation. Stated in §6.1. (c) That (α-rev)'s reversed neck range
($|q|>1$) is what makes it differ from (α-neck), the faithful Erbin–Fırat transplant —
there (α-neck) the bounded neck fills a region the stub *removed*, here (α-rev) it must
enter a region that no cubic vertex family reaches (R2) — and that (α-rev) is a different
mechanism, not a transplant. Stated in §5.4/§6.2; a critic may push that (α-rev) should be
called "a cubic theory with a new quartic-region prescription" rather than "the
Erbin–Fırat mechanism for closed strings". *Literature flag, not verified here:*
closed-string extensions of the stub construction beyond the faithful (α-neck) transplant
appear to exist in the 2023–2024 literature (open case: Schnabl–Stettinger 2023, §3.7.1;
closed-string extensions appear in the 2023–2024 literature) — Task 13/14 should locate
and verify the exact references before citing them, and check what those constructions do
and do not cover relative to (α-neck)/(α-rev). (d) That none of this changes the
paper's §7 chain (R29): (γ) reproduces $V_4$ and needs no geometry for $1/m_2$.

**Not settled (explicit list).**
- The relative-momentum (loop-momentum) sum identified in the (β2) composite (§3.7.3,
  §6.1) also sits inside R27's frozen chains $m_2^n$, $n\ge2$; its status there is part of
  A2(iii)/H1–H2 and is not decided by this record.
- Q13 (§6.1): whether the (β2) composite is a double cover of $\mathcal V_{0,4}$ branched
  at the external punctures — and hence whether (3.13) holds as a correlator identity;
  the loop-momentum test of §3.7.3/§6.1 gives an independent, cheaper route to "no".
- (6.1)/(6.2) (§6.2): whether the bounded-neck $\mathcal V_3'$ family covers $\mathcal M'_\times$
  once, and whether the on-shell exchange reproduces the $\mathcal M'_\times$ integral;
  the coordinate-extension precondition of §5.4/§6.2 must be checked first.
- BRST compatibility of the (β2) and (α-rev) kinetic operators (a $Q$-commutator, not
  done); §5.3 notes that $Q_{\rm tot}$ does not automatically preserve $\mathcal S_{\rm pair}$.
- Constructions fine-tuned to the actual $V_4$ through its BV boundary relation are
  not excluded by the scaling lemma; they are (α-rev)'s territory.
- The sign fact of R15 (indefinite Gram matrix at level 1) is noted, not used, and is
  itself unverified/uncited beyond R15 recording the sign as open: it would affect the
  Laplace form of $m_2^{-1}$ in (γ), not any geometric statement here.

## 8. Proposed ledger text (12d; not applied)

*Annotation to R28 (append to the row, one sentence).* "Sharpened by 030 §5.6 (R28$'$):
over the enlarged class of 030 §2, no construction *uniform in the vertex data* (one
that would also invert $tV_4$) equals $m_2^{-1}$ — scaling, 030 §5.6 (script part 4,
Vandermonde floor with break-on-purpose); at the actual $V_4$, product kernels
(Prop. 3.1, $\hat k\otimes\hat k$), tube-only kernels of any measure (Prop. 3.2) and the
Laplace reading (Lemma 2.2) are excluded individually; explicit-ghost dressings (3.8) and
mixed tube/slice kernels are excluded only as uniform constructions; not covered:
$V_4$-dependent bounds (= the algebraic inverse in disguise), infinite sums (Neumann),
and a change of kinetic term."

*New row (proposed ID R30, status: hand-checked and script-checked arithmetic for the
counts / Proven for the obstruction / Open for the identity).* "**Geometry of the
auxiliary channel after a change of kinetic term (030 §3.7, §4, §5).** (β) double strand:
$\Sigma\in\mathcal S_{\rm pair}$ with propagator
$b_1b_2b_1^-b_2^-(1-e^{-\lambda L_{\rm tot}})/L_{\rm tot}$ ($\gamma=-2$, 2 moduli) and rigid
$\mathcal W_3=\Omega_{V_4}(\mu_0)$ passes ghost, moduli, on-shell and SZ counts (the form
that matches Harold's one-parameter fixture with both antighosts); integrating $\Sigma$
out gives a 2-parameter family of 4-punctured *tori* with the $\mathcal M_{1,4}$
antighost measure, not $\mathcal V_{0,4}$ (genus, proven); equality with $V_4$ is open
exactly as the branched-double-cover question Q13 (030 §6.1), for which the loop-momentum
content of the composite (030 §3.7.3, §6.1) gives an independent and cheaper route to a 'no'. (α-rev) single strand in $\mathcal H_0$
(or $\mathcal H$) with $\mathcal K=Q_B L_0^+/(e^{\sigma L_0^+}-1)$ (the reversed range $|q|>1$; $Q_B/(1-e^{-\lambda L_0^+})$ for the forward range) and rigid
$\mathcal V_3'$: all counts pass with sphere topology, subject to a coordinate-extension
precondition on $\mathcal V_3'$'s local discs (030 §5.4); whether the neck family covers
$\mathcal M'_\times$ is the open computation (6.1)/(6.2) (030 §6.2, Task 14). (α-neck),
the faithful Erbin–Fırat transplant (030 §3.5), is consistent but leaves
$\mathcal V_{0,4}$'s interior untouched and does not by itself make the theory cubic.
(γ) unchanged: no geometry for $1/m_2$, $V_4$ reproduced (R29). Toy (script part 3):
every fixture the toy can build — disconnected $\mathcal W_3$, real-positive $g$, and a
rank-limited $P$ that is not itself a geometric object — fails at its analytic floor."

## Working notes (12d)

Consolidated into §5–§8; nothing pending. One derivation-level remark kept here: the
Riemann–Hurwitz and harmonic-cross-ratio counts of §6.1 were done in the file, not
checked by script (they are two-line classical facts: $\chi(T^2)=2\chi(S^2)-4$; a
Möbius involution with two prescribed fixed points swaps a pair iff the pair is harmonic
to the fixed points).

## Verification (12d)

Script part 4 (`codes/verify-geometric-inverse.py`, seed 20260908), 7 checks, total
113/113 PASS: scaling-lemma floor for $d=0,1,2,3$ (direct least-squares residual equals
the independently computed Vandermonde distance $\sqrt n\,\mathrm{dist}(\mathbf 1,\mathrm{span}\{t^{k+1}\})$,
all $>3.3$); break-on-purpose legs — a $t^{-1}$ term (the algebraic inverse) drives the
residual to $10^{-14}$, and $|T|=3\le d+1$ points allow interpolation (residual
$10^{-14}$), which is why the lemma is a statement "for all $t$"; a concrete
tube$\circ$slice$\circ$tube kernel (degree 1) sits above the $d=1$ floor (a consistency
check on the floor's shape, not a new falsification). Not machine
checked: §5's comparison (a synthesis), §6's Riemann–Hurwitz and harmonic counts
(classical), the twist-field charge (Task 13), the $\mathcal V_3'$ counts beyond the
ghost-number arithmetic of R23 (which part 1 already checks).

## Critic-1 resolution

Mechanical fix pass applied per `agent/reports/critic-030-geometric-inverse-20260908T080000.md`.
Item → sites edited (script docstring line ~61 counted separately at the end).

- **S1 (two "(α)"s conflated; missing coordinate-extension condition).** Renamed
  (α)→(α-neck)/(α-rev) at every restatement site: §0 rows (T1), summary lines 4–5; §3.5
  (the "(α) single strand" bullet and its Verdict box); §3.6 table (row T1, T2 remark);
  §5.1 (the (G-i)/(G-ii)/(G-iii) table row and the one-sentence answer, rewritten per the
  critic's "Depth and Objective" honest comparison); §5.4 (section header + intro
  sentence + all body occurrences); §5.5 (comparison table (α) row → (α-rev) row, and the
  "Reading of the map" paragraph); §6.1 (the closing "map reduces to" sentence); §6.2
  (structural remark); §7 (items 1, 2, 4(c), "Not settled" list); §8 (R30 draft). Added
  the coordinate-extension precondition (embedded local discs at radius $e^{\sigma(\theta)}$,
  SZ-vertex tangency at $|q|=1$) to §5.4 (new bullet), §6.2 (new count (iii)), §0 summary
  line 4, §5.5's (α-rev) row, and the R30 draft. Added the Siegel-gauge/$Q_B$
  identification once, in §3.5.
- **S2 (uniformity hypothesis for eq. (3.8)/candidate (c); R28$'$ overclaim).** §3.3
  (deleted "and never at generic momenta"; stated the uniformity hypothesis explicitly;
  added the $t=1$ fine-tuned-dressing non-exclusion, citing the script's
  `explicit-ghost-scaling` loophole; softened the boxed Result); §0 row (d) and last row;
  §3.6 row (c); §5.2 item 1; §5.6 (both the "Scope" bullet and the R28$'$ paragraph,
  replaced with the critic's exact wording); §7 items 1–2 (removed "homogeneity" from the
  $t=1$ obstruction list); §8 (R28 annotation replaced verbatim with the critic's text);
  Verification (12b) (the eq. (3.8) bullet reframed as supporting the scaling claim, not
  a $t=1$ exclusion).
- **S3 (Prop. 3.1 scope).** §3.1 Setup (restricted the boxed statement's scope to
  $\hat k\otimes\hat k$; removed the polarised-kernel parenthetical; added the sentence
  routing the polarised undressed case to Prop. 3.2 and the polarised dressed case to
  §5.6); §0 row (b); §3.6 row (a); §5.2 item 1; §5.5 (γ) row; §5.6 "Scope" bullet.
- **S4 (loop-momentum content of Q13).** New paragraph in §3.7.3 ("The concrete
  correlator-level difference (the loop momentum)"), including the Lunin–Mathur
  hep-th/0006196 citation; new paragraph in §5.3 ("Concrete correlator-level
  obstruction"), including the BRST one-sentence note; new bullet in §6.1's "Counts done
  here" list, including the second Lunin–Mathur citation; new bullet in §7's "Not
  settled" list on the same sum inside R27's frozen chains $m_2^n$, $n\ge2$.

**Concern/Minor items (one-sentence or replacement-text fixes).**

| item | site(s) edited |
|---|---|
| $-3\to-2$ slip | §3.7.3 (with the corrected $S_B=9$, $\gamma_{\rm pair}=-2$ arithmetic shown) |
| §5.2 quadratic-growth correction | §5.2 ("doubling" → $N(N+1)/2$ vs $2N$) |
| Lemma 2.1 sentence (linearity, not "used at most once") | §2.2, Lemma 2.1 statement |
| Lemma 2.2 attribution (020's T2 refutation; caveat is new) | §2.2 table cell (T2 row) and the Lemma 2.2 heading |
| §3.1 pole sentence (singularities at $\det V_4=0$) | §3.1, "Two further, independent obstructions", item (i) |
| §3.2 "only if" → "natural mechanism" | §3.2, "Legitimacy of a frozen $b_0^+e^{-sL_0^+}$" |
| §6.1 twist-field assumption (6 vs 12, absorbed-into-twist-fields) | §6.1, anomaly-bookkeeping bullet |
| sign fact of R15 (unverified/uncited, not invented) | §3.4, §4.2 item 6, §5.2 (open point), §7 "Not settled" (4 sites) |
| "not even asymptotic" → "for a random tensor in the toy" | §4.2 item 5 |
| R30 "only form" softening; "Verified for the counts" → "hand-checked and script-checked arithmetic" | §8, R30 draft |
| docstring line 61 / §3.6(iv) scope sentence | `codes/verify-geometric-inverse.py` docstring; §3.6(iv) |
| Siegel-gauge vs $Q_B$ identification | §3.5 |
| BRST one-sentence note in §5.3 | §5.3, new paragraph |
| additivity assumption in §1.1 | §1.1 (C2) |
| row-9a header (does not act on $\mathrm{Sym}^2\mathcal H_0$) | §0 row (a) |
| R23 "consistent with" | §1.2, "frozen-handle reading of R23's $+g$" |
| Lunin–Mathur reference (hep-th/0006196) | §3.7.3, §6.1 |
| labelling of decorative script checks as "transcription/arithmetic checks" | Verification (12a) (two-bookkeeping/Lemma 2.1 floor bullet, Lemma 2.2 toy bullet), Verification (12b) (`commutant-L0`, random-dressed-vertex leg), Verification (12d) (tube-slice-tube leg) |
| closed-string stub literature — flag, do not cite | §7 item 4(c) |

No numbers were changed except the single $-3\to-2$ slip in §3.7.3; no re-derivation was
performed.

## Critic-2 (narrow confirmation, Opus, 2026-09-08) resolution

Applied directly by the orchestrator (all wording, replacement text supplied): §5.5 "Reading of the map" gains the (α-neck) sentence and "Of the redefinitions that would remove the quartic vertex"; §5.5 proof-per-reading qualifier; §5.2 closing parenthesis qualified ((3.8) uniform, Prop. 3.1 for $\hat k\otimes\hat k$, §5.6); §8 R30: loop momentum = route to a 'no' (not an obstruction), reversed-range operator $Q_BL_0^+/(e^{\sigma L_0^+}-1)$; §0 summary line 3 parenthesis; rank-limited fixture qualified as non-geometric in §0 row (e), §5.3, §8 R30; Verification (12b) scope sentence; §3.3 open-set parenthetical replaced by the one-parameter family. Cap of 2 critic iterations reached; R28′ annotation and R30 row promoted to the ledger with these edits.

## Status — last completed: critic-2 residues applied (orchestrator); promoted to ledger (R28′ annotation, R30); next: none (record closed)
