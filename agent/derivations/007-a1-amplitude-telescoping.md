# Derivation record 007 — A1: explicit amplitude-level telescoping of the Σ-exchange

Date: 2026-07-01
Author: Claude Fable 5 (inline, per state-file resume sequence "Phase A / A1")
Task source: `knowledge/fable-2026-07-01-assessment-and-results.md` §6bis(e) (point 1); discharges the combinatorics **assumed** by R10 route (B) (critic C2 on the
Fable note; critic F2 on derivation 005: "exactly one tree" and the $L!K!$ factors were
asserted, not computed).
Verification: `codes/verify-a1-telescoping.py` (sympy 1.14.0, 7/7 PASS, executed).
Critic: iter 1 (Opus, blind) → **REVISE, 0 Fatal — decisive coefficient chain fully
hand-re-derived and confirmed; all findings convention/scope**
(`agent/reports/critic-a1-telescoping-20260702T000000.md`). All findings applied in
this revision (Issues 1–5, 7); the critic's recommendation authorizes promotion as
R14 with the stated carve-outs.
Toy template: Harold's `sources/notes/qft_stubs.tex`, §general-intermediate, the
$A_4 = 3\cdot(2\mathrm{i}V/12)\cdot((-\mathrm{i}/2)\,4!\,V^{-1})\cdot(2\mathrm{i}V/12)
= \mathrm{i}V$ computation.

Reused verbatim (not re-derived): **R1/R8** (HS action `eq:SHS`, completion of square,
2:1 source-to-kinetic ratio), **R7** (pairing $G_2=\omega_1^{\otimes2}$ graded-symmetric;
physical $N_{\rm gh}$ grading), **R9** (kernel decoupling on $\operatorname{Sym}^2$),
**R13/§3 of the Fable note** (quotient by $\ker V_4$), **H2 closed** (full $S_4$ graded
symmetry of $V_4$, standard for all geometric vertex families).

---

## 0. Claim

Let the $\Sigma$-sector Feynman rules be derived from the boxed HS action (note `eq:SHS`)

$$
S_{\rm HS}=\tfrac12 V_2(\Psi^2)+\frac{g_s}{3!}V_3(\Psi^3)
-\frac{g_s^2}{4!}V_4(\Sigma,\Sigma)+\frac{2g_s^2}{4!}V_4(\Sigma,\Psi^{\otimes2}),
\qquad \Sigma\in\operatorname{Sym}^2\mathcal H_0 .
\tag{A.1}
$$

Then the amputated connected 4-point interaction kernel at $O(g_s^2)$, computed from the
single $\Sigma$-exchange diagram **with all symmetry factors made explicit**, on four
generic distinct external states $\Psi_1,\dots,\Psi_4$, is

$$
\boxed{\;
\Gamma_4^{\Sigma\text{-exch}}
=\underbrace{3}_{\text{pairings}}\times
\underbrace{\frac{g_s^2}{6}V_4(\,\cdot\,,\Psi_i\!\otimes\!\Psi_j)}_{\text{vertex}}
\circ\underbrace{\frac{12}{g_s^2}\,\big(V_4|_{\operatorname{Sym}^2}\big)^{-1}}_{\text{propagator}}
\circ\underbrace{\frac{g_s^2}{6}V_4(\,\cdot\,,\Psi_k\!\otimes\!\Psi_l)}_{\text{vertex}}
= g_s^2\,V_4(\Psi_1,\Psi_2,\Psi_3,\Psi_4),
\;}
\tag{A.2}
$$

identical — coefficient included — to the contact kernel of the quartic-truncated action
$S_{\rm eff}\supset +\tfrac{g_s^2}{4!}V_4(\Psi^{\otimes2},\Psi^{\otimes2})$. The
telescoping $V_4\circ V_4^{-1}\circ V_4=V_4$ collapses the exchange to one insertion of
the original quartic vertex **with coefficient exactly 1** (computed). *Scope [critic
iter 1, Issue 2]:* the further statement that this insertion covers the
$\mathcal V_{0,4}$ contact region while the three $V_3$-plumbing channels sweep
$\mathcal M_{0,4}\smallsetminus\mathcal V_{0,4}$ is the geometric identification
**inherited from the vertex construction** (R2-type content) — the finite-dimensional
layer verified here computes the coefficient, not the region decomposition itself.
This is the SFT transcription of the toy $A_4=\mathrm{i}V_{ijkl}$ computation of
`qft_stubs.tex`, and it upgrades the coefficient part of the Fable note §5 "covering
is inherited by construction" to "computed".

Beyond 4 points: because $\Sigma$ enters (A.1) only quadratically, the Gaussian
integration is exact and field-independent up to normalization, so **all** $\Psi$
Green's functions of the HS theory equal those of $S_{\rm eff}$ identically (§4), and
$\Sigma$-loops are impossible **at $O(g_s^2)$ ($\Sigma$ purely quadratic — R12's
$V_5(\Sigma_2,\Sigma_2,\Psi)$, $V_6(\Sigma_2^3)$ self-couplings enter only at higher
order)**. The "exactly one tree" assumption of R10 route (B) is thereby discharged,
not just at 4 points but wholesale.

---

## 1. Setup

### Assumptions and conventions

- **Finite-dimensional model (binding for the combinatorics, as in R7–R10).**
  $\mathcal H_0\cong\mathbb R^N$, basis $e_a$, a level-truncated stand-in for the
  level-matched space $\ker L_0^-\cap\ker b_0^-$. What is verified here is the
  **combinatorial/algebraic layer**: symmetry factors, pairing counts, propagator
  normalization, telescoping. CFT-level analytic questions (spectral theory of
  $V_4^{-1}$ on $\operatorname{Sym}^2$, bounded inverse) are **A2**, not here.
- **Statistics.** Physical grading (R7): $\Psi$ at $N_{\rm gh}=2$, $\Sigma$ at
  $N_{\rm gh}=4$, both Grassmann-**even**. All combinatorial factors below are therefore
  literally bosonic — the same as the scalar toy. For odd components of the full BV
  master field the Koszul signs ride along with the graded $S_4$ symmetry of $V_4$
  (H2, closed) and do not change the *counting*; this graded extension is a remark,
  not re-derived (it belongs with A3/write-up).
- **Vertex.** $V_{abcd}$ totally symmetric (H2). As a bilinear form on
  $\mathcal H_0^{\otimes2}$: $V_4(A,B)=V_{abcd}A^{ab}B^{cd}$. Total symmetry implies
  (i) pair-exchange symmetry $V_4(A,B)=V_4(B,A)$, and (ii) $V_4$ annihilates
  $\wedge^2\mathcal H_0$ in each slot (R9's decoupling).
- **Path-integral convention.** $Z=\int\!\mathcal D\Psi\,\mathcal D\Sigma\;e^{S}$,
  correlators by Wick contraction; the project's notes carry no explicit
  $\mathrm{i}$'s. The dictionary to the toy's $e^{\mathrm{i}S}$ convention is §5.
- **External states.** $\Psi(t)=\sum_{i=1}^4 t_i\Psi_i$ with generic **distinct**
  $\Psi_i\in\mathcal H_0$; the amputated 4-point interaction kernel is
  $\Gamma_4=\partial_{t_1}\partial_{t_2}\partial_{t_3}\partial_{t_4}\,
  W_{\rm int}\big|_{t=0}$. Distinct externals expose every symmetry factor (this is
  exactly where R10 was schematic: it worked with the diagonal $\Psi^{\otimes2}$).
- **Sign of the comparison quartic.** $S_{\rm eff}=\tfrac12V_2+\tfrac{g_s}{3!}V_3
  +\tfrac{g_s^2}{4!}V_4(\Psi^{\otimes2},\Psi^{\otimes2})$, the sign fixed by R8/R10
  (completion of the square on (A.1): $-\tfrac{g_s^2}{4!}V_4(\Sigma,\Sigma)
  +\tfrac{2g_s^2}{4!}V_4(\Sigma,\Psi^{\otimes2})
  =-\tfrac{g_s^2}{4!}V_4(X,X)+\tfrac{g_s^2}{4!}V_4(\Psi^{\otimes2},\Psi^{\otimes2})$,
  $X=\Sigma-\Psi^{\otimes2}$). The `eq:SHSderive` **prose** slip in the overview (it
  calls $-\tfrac{g_s^2}{4!}V_4(\Psi^4)$ "the original quartic") is noted again; boxed
  equations are unaffected (critic F6 on derivation 005; still pending the author's approval for
  the one-line fix in the note).
- **Non-degeneracy.** $V_4|_{\operatorname{Sym}^2}$ invertible, OR degenerate with the
  propagator defined as the pseudo-inverse on a complement of the kernel — §6 shows the
  result is unchanged (kernel decoupling, R13/§3).

### Both theories share every $\Psi$-sector rule

$V_2$, $V_3$ and the $\Psi$-propagator are common to $S_{\rm HS}$ and $S_{\rm eff}$, so
the three $V_3$-exchange channels (s/t/u plumbing families) are *identical* diagrams in
both theories. The only $O(g_s^2)$ difference is [quartic contact] vs [Σ-exchange];
comparing those two kernels is the entire task.

---

## 2. Σ-Feynman rules from eq:SHS

Write the $\Sigma$-sector of (A.1) as
$$
S_\Sigma=-\tfrac12\,M(\Sigma,\Sigma)+B(\Sigma),\qquad
M:=\frac{g_s^2}{12}\,V_4\Big|_{\operatorname{Sym}^2},\qquad
B:=\frac{g_s^2}{12}\,V_4(\,\cdot\,,\Psi^{\otimes2}).
\tag{A.3}
$$
(Check: $-\tfrac12 M(\Sigma,\Sigma)=-\tfrac{g_s^2}{24}V_4(\Sigma,\Sigma)$ — yes,
$\tfrac1{24}=\tfrac1{4!}$; and $B(\Sigma)=\tfrac{g_s^2}{12}V_4(\Sigma,\Psi^{\otimes2})
=\tfrac{2g_s^2}{4!}V_4(\Sigma,\Psi^{\otimes2})$.)

**Propagator.** For $e^{S}$ with $S\supset-\tfrac12 M(\Sigma,\Sigma)$ the Wick
contraction is the inverse of $M$ **on $\operatorname{Sym}^2\mathcal H_0$**, i.e. with
respect to the symmetric identity:
$$
\langle\Sigma^{ab}\,\Sigma^{cd}\rangle=P^{ab,cd},
\qquad
M_{ab,ef}\,P^{ef,cd}=\big(\mathbb 1_{\rm Sym}\big)_{ab}{}^{cd}
=\tfrac12\big(\delta_a^c\delta_b^d+\delta_a^d\delta_b^c\big),
\qquad
P=\frac{12}{g_s^2}\,\big(V_4|_{\operatorname{Sym}^2}\big)^{-1}.
\tag{A.4}
$$
This is where the factor-2 bookkeeping lives; three equivalent housekeepings, which the
script cross-validates against each other:

1. **Ordered tensor indices** with the symmetric identity (A.4) — used in the algebra
   below.
2. **Orthonormal unordered-pair basis** $\lambda_I$ ($\lambda_{I;ab}\lambda_{J;ab}
   =\delta_{IJ}$; diagonal $E_{aa}$ and off-diagonal $(E_{ab}+E_{ba})/\sqrt2$), the
   toy's convention: $\sigma^I=\Sigma^{ab}\lambda_{I;ab}$, $V_{IJ}=V_4(\lambda_I,
   \lambda_J)$, $\langle\sigma^I\sigma^J\rangle=\tfrac{12}{g_s^2}(V^{-1})^{IJ}$. The two
   agree because completeness reads $\sum_I\lambda_I^{ab}\lambda_I^{cd}
   =\tfrac12(\delta^{ac}\delta^{bd}+\delta^{ad}\delta^{bc})=\mathbb 1_{\rm Sym}$.
   (The completeness relation as printed in `qft_stubs.tex` has a typo:
   "$\delta_{i\ell}+\delta_{jk}$" for the product $\delta_{i\ell}\delta_{jk}$.)
3. **Full $\mathcal H_0^{\otimes2}$ with Moore–Penrose pseudo-inverse**: since the
   totally symmetric $V$ annihilates $\wedge^2$ in each slot, its $N^2\times N^2$
   matrix has rank $\le\dim\operatorname{Sym}^2$ and its pseudo-inverse restricts to
   the $\operatorname{Sym}^2$ inverse and vanishes on $\wedge^2$ — the $\wedge^2$
   sector drops out of the rules automatically (R9's decoupling, now diagrammatic).

Note that the contracted quantity $v^{\mathsf T}G^{-1}v$ (source–propagator–source) is
**basis-invariant**, so *any* consistently used scheme gives the right answer — in
particular the fully entrywise unordered-pair scheme ($I=(a\!\le\!b)$, entrywise matrix
$\tilde V_{IJ}=V_{abcd}$, entrywise source $\tilde T_I=T^{ab}$): with multiplicities
$m_I\in\{1,2\}$ and $D=\operatorname{diag}(m_I)$, the Gram matrix is $G=D\tilde VD$ and
the covariant source $v=D\tilde T$, so $v^{\mathsf T}G^{-1}v=\tilde T^{\mathsf T}
\tilde V^{-1}\tilde T$ — **the weights cancel** (this D-cancellation is why the toy's
$V_{IJ}^{-1}$ propagator is robust). The genuine factor-2 trap is the *inconsistent
mix*: differentiating $B$ with respect to the unordered variables $\sigma_I$ produces
the $m_I$-weighted source $\partial B/\partial\sigma_I=m_I\tilde T_I$, which must then
be contracted with the inverse **Gram** matrix $D^{-1}\tilde V^{-1}D^{-1}$, not with
$\tilde V^{-1}$; the mix is wrong by $m_Im_J$ factors. The script exhibits both the
cancellation lemma and the failing mix (check 5) and verifies the propagator identity
(A.4) componentwise.

**Vertex.** With $\Psi(t)=\sum_i t_i\Psi_i$,
$B(\Sigma)=\tfrac{g_s^2}{12}\sum_{i,j}t_it_j\,V_4(\Sigma,\Psi_i\!\otimes\!\Psi_j)$, so
the $\Sigma\Psi_i\Psi_j$ vertex for $i\neq j$ is
$$
\frac{\partial^2 B}{\partial t_i\,\partial t_j}
=\frac{g_s^2}{12}\cdot 2\cdot V_4(\Sigma,\Psi_i\!\otimes\!\Psi_j)
=\frac{g_s^2}{6}\,V_4(\Sigma,\Psi_i\!\otimes\!\Psi_j),
\tag{A.5}
$$
the factor 2 from the two assignments of $\{\Psi_i,\Psi_j\}$ to the two $\Psi$ slots
($V_4(\Sigma,\Psi_i\otimes\Psi_j)=V_4(\Sigma,\Psi_j\otimes\Psi_i)$ by symmetry of $V$;
only the $\operatorname{Sym}^2$ part of $\Psi_i\otimes\Psi_j$ enters, consistently with
$\Sigma\in\operatorname{Sym}^2$). Each vertex has **exactly one** $\Sigma$ leg.

---

## 3. The Σ-exchange 4-point diagram

Expand $e^{B(\Sigma)}$ inside the Gaussian: the first non-trivial connected term is
$$
\frac{1}{2!}\,\big\langle B(\Sigma)\,B(\Sigma)\big\rangle_{\rm Wick}
=\frac12\,B_{ab}\,P^{ab,cd}\,B_{cd}
\equiv\frac12\,B\,P\,B .
\tag{A.6}
$$
Differentiate four times; $B$ is quadratic in $t$, so the four derivatives split $2+2$
over the two $B$ factors:
$$
\Gamma_4^{\Sigma\text{-exch}}
=\partial_{t_1}\partial_{t_2}\partial_{t_3}\partial_{t_4}\Big[\tfrac12\,BPB\Big]
=\frac12\times 2\times\!\!\sum_{\substack{\text{pairings}\\ \{i,j\},\{k,l\}}}\!\!
\Big(\frac{\partial^2B}{\partial t_i\partial t_j}\Big)\,P\,
\Big(\frac{\partial^2B}{\partial t_k\partial t_l}\Big),
\tag{A.7}
$$
with the three pairings $\{1,2\}\{3,4\}$, $\{1,3\}\{2,4\}$, $\{1,4\}\{2,3\}$. The
factor $\tfrac12\times2$: $1/2!$ from the exponential, $\times2$ for which $B$ factor
receives which derivative pair — they cancel, the standard cancellation the toy leaves
implicit. Inserting (A.4)–(A.5), each pairing contributes
$$
\frac{g_s^2}{6}\cdot\frac{12}{g_s^2}\cdot\frac{g_s^2}{6}\;
V_4\Big(\Psi_i\!\otimes\!\Psi_j\,,\;(V_4|_{\operatorname{Sym}^2})^{-1}
V_4(\,\cdot\,,\Psi_k\!\otimes\!\Psi_l)\Big)
=\frac{g_s^2}{3}\,V_4(\Psi_i\!\otimes\!\Psi_j,\Psi_k\!\otimes\!\Psi_l),
\tag{A.8}
$$
by the **telescoping identity** $V_4\circ(V_4|_{\operatorname{Sym}^2})^{-1}\circ V_4
=V_4$ on symmetric tensors — legitimate here because both attached tensors
$\Psi_i\!\otimes\!\Psi_j$ enter only through their symmetric parts. By total symmetry
of $V$ (H2), $V_4(\Psi_i\otimes\Psi_j,\Psi_k\otimes\Psi_l)
=V_{abcd}\Psi_1^a\Psi_2^b\Psi_3^c\Psi_4^d\equiv V_4(\Psi_1,\Psi_2,\Psi_3,\Psi_4)$ for
**each** of the three pairings. *This is exactly where the full $S_4$ symmetry (H2) is
load-bearing — pair-exchange symmetry alone would leave the three pairings unequal;
note the script's random $V=\sum_r c_ru_r^{\otimes4}$ is automatically totally
symmetric, so the script exercises H2's consequences but cannot detect its failure
[critic Issue 7].* Hence
$$
\Gamma_4^{\Sigma\text{-exch}}
=3\times\frac{g_s^2}{3}\,V_4(\Psi_1,\Psi_2,\Psi_3,\Psi_4)
=g_s^2\,V_4(\Psi_1,\Psi_2,\Psi_3,\Psi_4).
\tag{A.9}
$$

**Contact side.** From $S_{\rm eff}\supset+\tfrac{g_s^2}{4!}V_4(\Psi(t)^{\otimes2},
\Psi(t)^{\otimes2})$:
$$
\Gamma_4^{\rm contact}
=\partial_{t_1}\!\cdots\partial_{t_4}\,\frac{g_s^2}{4!}\,V_4(\Psi(t)^{4})
=\frac{g_s^2}{4!}\times 4!\times V_4(\Psi_1,\Psi_2,\Psi_3,\Psi_4)
=g_s^2\,V_4(\Psi_1,\Psi_2,\Psi_3,\Psi_4).
\tag{A.10}
$$
$\Gamma_4^{\Sigma\text{-exch}}=\Gamma_4^{\rm contact}$, coefficient included. $\square$

**Sensitivity.** The equality is *quadratically* sensitive to the 2:1
source-to-kinetic ratio of `eq:SHS`: replacing the source coefficient
$\tfrac{2g_s^2}{4!}\to\tfrac{c\,g_s^2}{4!}$ rescales $\Gamma_4^{\Sigma\text{-exch}}$ by
$(c/2)^2$ — for $c=1$ the exchange reproduces only $\tfrac14$ of the contact term.
*Epistemic status [critic Issue 3]:* since the code builds each vertex $\propto c$,
the $(c/2)^2$ scaling is structural rather than an independent falsification; the
genuinely falsifiable content of script check 4 is the inequality
$\Gamma(c{=}1)\neq\Gamma^{\rm contact}$. The check is a consistency/sensitivity
statement, not independent corroboration (same caveat as R11's check).

---

## 4. Exactness beyond four points, and R10's combinatorics discharged

$\Sigma$ appears in (A.1) only through $S_\Sigma=-\tfrac12M(\Sigma,\Sigma)+B(\Sigma)$.
Therefore:

1. **Exact Gaussian statement.** $\int\!\mathcal D\Sigma\,e^{S_\Sigma}
   =\det(2\pi M^{-1})^{1/2}\,e^{\frac12 BM^{-1}B}$ (formal/Wick-defined Gaussian: $M$
   is in general indefinite, so the determinant factor requires the usual analytic
   continuation — what matters is that it is **field-independent regardless of
   signature**, since $M$ does not involve $\Psi$ [critic Issue 5]), and
   $\tfrac12BM^{-1}B=\tfrac{g_s^2}{4!}V_4(\Psi^{\otimes2},\Psi^{\otimes2})$
   *as a polynomial identity in $\Psi$* (script check 2 verifies this at all orders in
   the $t_i$ simultaneously, not only the $t_1t_2t_3t_4$ coefficient). Hence
   $Z_{\rm HS}[J]=\mathcal N\,Z_{\rm eff}[J]$ with $\mathcal N$ field-independent:
   **every** connected $\Psi$ Green's function coincides, to all orders in $g_s$, within
   the truncation.
2. **Diagrammatic reading.** Each $\Sigma\Psi\Psi$ vertex has exactly one $\Sigma$ leg,
   and there is no $\Sigma$ self-coupling at this order; hence $\Sigma$ lines only pair
   vertices ("one tree" per exchange — R10's assumption, now a two-line lemma), a
   $\Sigma$ loop is impossible, and the only $\Sigma$-trace is the field-independent
   $\det^{1/2}$ normalization. In any tree diagram every internal $\Sigma$ line
   telescopes as in (A.8), collapsing to one $V_4$ insertion with coefficient 1; multiple
   exchanges collapse independently (guaranteed globally by item 1).
3. **Moduli covering, explicit.** The $O(g_s^2)$ 4-point function of the HS theory is
   [three $V_3$-plumbing channels, identical rules, sweeping
   $\mathcal M_{0,4}\smallsetminus\mathcal V_{0,4}$] $+$ [$\Sigma$-exchange $=$ the
   $\mathcal V_{0,4}$ contact insertion, coefficient 1]. The vertex-region decomposition
   of $\mathcal M_{0,4}$ is inherited verbatim — the Fable note §5 statement, now with
   the coefficient computed rather than argued. In the 2-coloured-operad reading
   (§6bis(a)) the $\Sigma$-exchange is a single colour-2 (double-line) edge composition;
   nothing new is added here to that dictionary.

---

## 5. Dictionary to the toy ($\lambda_I$ basis) — `qft_stubs.tex`
*(Revised per critic iter 1, Issue 1: the toy's quoted rules are internally
consistent in its own weight convention; the earlier "toy vertex sign slip" claim is
retracted.)*

The toy writes its action as $S=-\int[\,\mathcal B\,]$ with bracket
$\mathcal B\supset\tfrac1{4!}V\phi^4+\tfrac{1}{12}V_{ijkl}\phi_i\phi_j\sigma_{kl}
-\tfrac1{4!}V_{ijkl}\sigma_{ij}\sigma_{kl}$, and its quoted Feynman rules (vertex
$+2\mathrm iV_{Iij}/12$, propagator $(-\mathrm i/2)4!\,V^{-1}_{IJ}=-12\mathrm i
V^{-1}$, direct quartic $+\mathrm iV$) are **mutually self-consistent with the
path-integral weight $e^{\mathrm i\int\mathcal B}=e^{-\mathrm iS}$**: from
$\mathcal B\supset\tfrac1{12}V\phi\phi\sigma$ the vertex is
$\mathrm i\cdot\tfrac{V}{12}\cdot2=+\tfrac{2\mathrm iV_{Iij}}{12}$; in the
orthonormal basis $V_{ijkl}\sigma_{ij}\sigma_{kl}=V_{IJ}\sigma^I\sigma^J$, so the
$\sigma$ kinetic exponent is $\mathrm i\cdot(-\tfrac12)(\tfrac{V}{12})\sigma\sigma$
(i.e. $K=V/12$) and
$$
\langle\sigma\sigma\rangle=-\mathrm i\,K^{-1}=-12\,\mathrm i\,V^{-1}
=\Big(\frac{-\mathrm i}{2}\Big)\,4!\;V^{-1}_{IJ},
$$
**exactly the toy's quoted propagator**, and the direct 4-point vertex from
$\mathcal B\supset\tfrac1{4!}V\phi^4$ is $\mathrm i V$ — reproduced by the exchange:
$$
A_4=3\cdot\Big(\frac{2\mathrm i V_{Iij}}{12}\Big)
\Big(\frac{-\mathrm i}{2}4!\,V^{-1}_{IJ}\Big)
\Big(\frac{2\mathrm i V_{Jkl}}{12}\Big)=\mathrm i\,V_{ijkl}.
$$
The factor chain $3\cdot\tfrac16\cdot12\cdot\tfrac16=1$ is identical to (A.9)'s; the
$\mathrm i$'s are pure convention and drop out of the SFT-side computation, which
uses the real $e^{S}$ weight throughout (§1) and is therefore convention-clean. The
SFT transcription is *literal*: $\Psi\leftrightarrow\phi_i$ (vector-like),
$\Sigma\leftrightarrow\sigma_{ij}$ (matrix-like), $\Sigma$-propagator
$\leftrightarrow V_{IJ}^{-1}$ contracted along the double line (§6bis(a)).

---

## 6. Degenerate $V_4$: the kernel never enters the diagram

Suppose $\ker(V_4|_{\operatorname{Sym}^2})\neq0$ (the (5.1) question, defused in Fable
note §3/R13). Define the propagator as the pseudo-inverse $P^+$ on a complement of the
kernel. Then:

- the source is automatically kernel-orthogonal: $B(\xi)=\tfrac{g_s^2}{12}
  V_4(\xi,\Psi^{\otimes2})=0$ for $\xi\in\ker$, so no diagram ever routes flux through
  the kernel;
- the telescoping $V_4\,P^+\,V_4=V_4$ is an identity of the pseudo-inverse, so (A.8)
  and hence (A.9) are unchanged;
- the kernel directions are zero-action, unsourced spectators — the quotient definition
  $\Sigma\in\operatorname{Sym}^2\!\mathcal H_0/\ker V_4$ (R13) removes them entirely.

Script check 6 exercises this with a rank-deficient totally symmetric $V$ built as a
sum of fourth powers $\sum_r c_r\,u_r^{\otimes4}$ with fewer terms than
$\dim\operatorname{Sym}^2$.

The statement in the toy note (`qft_stubs.tex`: zero modes of $V_{IJ}$ mean that some
fields do not enter in the quartic term) is precisely this statement.

---

## 7. What this does and does not establish

**Established (algebraic/combinatorial layer, machine-checked):**
- Σ-Feynman rules (A.4)–(A.5) with the three pair-index bookkeepings proven equivalent;
- the exchange = contact identity (A.9)–(A.10) with all symmetry factors explicit, on
  generic distinct external states — R10 route (B)'s assumed combinatorics discharged;
- the exact all-Green's-function statement (§4.1) and the impossibility of Σ-loops
  **at $O(g_s^2)$** (Σ purely quadratic);
- the coefficient (exactly 1) of the collapsed $V_4$ insertion; the $\mathcal M_{0,4}$
  region decomposition itself is inherited from the vertex construction, not computed
  here (critic Issue 2);
- robustness under $\ker V_4\neq0$ via pseudo-inverse (§6);
- the literal dictionary to Harold's toy $A_4$ computation, including the origin of the
  $(-\mathrm i/2)\,4!$ propagator normalization.

**Not established here (open, tracked elsewhere):**
- CFT-level meaning of $V_4^{-1}$ on the infinite-dimensional $\operatorname{Sym}^2$
  (spectral/sectoriality questions, Schwinger representation) — **A2(ii)**;
- actual kernel size of $V_4|_{\operatorname{Sym}^2}$ at low levels — **A2(iii)**
  (SL(2,C) companion-vertex numerics);
- $O(g_s^3)$ and the $V_5(\Sigma_2,\Sigma_2,\Psi)$ coefficient — **Phase B1**;
- graded (odd-component) Koszul-sign version of the counting — remark only, deferred to
  the write-up (A3);
- CFT-normalized reality/$\mathrm i$-conventions of the closed-string measure (write-up
  phase, per Fable-note Appendix).
