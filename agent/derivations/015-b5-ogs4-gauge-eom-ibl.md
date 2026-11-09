# Derivation 015 — B5: gauge transformations, EOMs, and IBL$_\infty$ rewriting at $O(g_s^4)$

- **Task:** Request (2026-07-06): completely understand the $O(g_s^4)$ terms.
  Three deliverables, for **both** Route-B $O(g_s^4)$ presentations: (1) gauge
  transformations of $\Sigma_2,\Sigma_3$ with the action invariant at $O(g_s^4)$;
  (2) EOMs and commentary; (3) rewrite in terms of $\IBL_\infty$ products $p_{m,n}$
  and show they satisfy the IBL relations (tree level, $g=0$ only).
- **Author:** orchestrator inline (GLM-5.2), session 2026-07-06, after two empty
  computator dispatches. The computator brief
  `agent/briefs/pending-computator-b5-ogs4-gauge-eom-ibl-20260706T143000.md` is
  retained for provenance; the dispatches produced
  no artifacts, so the work is done inline per the Fable-session precedent
  (2026-07-01/02/03) and the 2026-06-24 $\omega_2$ inline re-derivation.
- **Machine check:** `codes/verify-b5-ogs4-gauge-eom-ibl.py` — **6/6 PASS
  (executed 2026-07-06; re-executed 2026-07-09 on two seeds, 20260706 and 41,
  after the check-3 rewrite below)**.
- **Status:** **R21 (promoted 2026-07-06).** Review history: inline self-critique
  (ACCEPT with Concerns) at promotion; **blind critic pass DONE 2026-07-08 (Opus,
  ST9): REVISE on verification honesty, physics confirmed correct** — the critic
  hand-re-derived the load-bearing steps of this derivation (Φ-map lemma +
  on-shell collapse; the δY₃=0 argument, including its consistency with the
  O(g_s⁵) breakdown in 018 §7) and found no Fatal/no algebra error, but found
  the original check 3 tautological [S1] and checks 4/5/6 described beyond what
  they execute [S2]. **All findings applied 2026-07-09:** check 3 rewritten as a
  genuine three-leg test (independent-route agreement, Y₃-independence of the
  transported variation, and a falsification leg with a Ψ-dependent kernel where
  the R25-type rotation restores invariance); checks 4/5/6 relabelled as the
  on-shell / stationarity / generic-nonzero proxies they are; §0/§5.3/§6 IBL tone
  aligned with §5.4's honesty [C1]; R19 warrant cited for the off-shell equality
  [C2]; relation-$N_{\rm gh}$ labels fixed [M1]; $N_{\rm gh}$ formula attribution
  updated to R23 [M2]; check-2 detail string de-claimed [M3]. Report:
  `agent/reports/critic-b5-st4-r21-r22-20260708T214500.md`.
- **Inputs reused (not re-derived):** R1 (`eq:SHS`), R7 (physical grading,
  $\omega_2$ symmetric), R9 (auxiliarity $\iff$ kernel non-deg), R10 (Gaussian
  elimination $=$ CFL transfer), R11 (composite law), R12 (counting, $\Sigma_3$ at
  $V_7$), R16 ($(2,2,0)$ lemma method), R17 ($O(g_s^3)$ gauge law `eq:dSig3`,
  dressed kernel $K_\Psi$), R19 ($O(g_s^4)$ $\Sigma_2$-only gauge law `eq:dSig4`,
  $W_6$, $\mathcal C$, master-equation-agnostic), R20 (elementary presentation,
  $\mathcal D\neq\mathcal C$, outcome C), R20-Annotation (dressed-$\tilde V_6$
  framing).
- **Conventions:** physical $N_{\rm gh}$ ($\Psi{:}2$, $\Sigma_2{:}4$, $\Sigma_3{:}6$,
  $\delta\Psi{:}2$, $\Lambda{:}1$); finite-dimensional model binding for the
  algebraic layer (CFT analytics of inverses $=$ A2(iii)/T4 carve-out); $e^S$ weight;
  $V_4,V_5,V_6$ totally graded-symmetric geometric vertices (when they appear as
  elementary vertices; the dressed $\tilde V_6$ is composite, see §2).

---

## 0. Executive summary

Two presentations, treated in parallel (both are investigated; the comparison is
the point):

- **(P-elementary)** — R20: $\Sigma_3$ with bare $V_6$ kinetic $M=V_6|_{\Sym^3}$ and
  bare source $u(\Sigma_2)=V_6(\cdot,\Sigma_2,\Psi)$. Does **not** close on-shell
  (residual $(g_s^4/600)vV_4^{-1}v$ survives, R20 outcome C).
- **(P-dressed)** — $\Sigma_3$ with **composite** kinetic
  $\tilde M=M-\tfrac65 N$ and **composite** source
  $\tilde u=u-\tfrac65\Phi^\top V_4^{-1}v(\Sigma_2)$, where $N=\Phi^\top V_4^{-1}\Phi$
  and $\Phi:\Sym^3\to(\Sym^2)^*$ is the linear map $\Phi(X)_I=V_5(\Lambda^2_I,X)$.
  Closes on-shell: $\tilde M(\Psi^{\otimes3},\Psi^{\otimes3})=W_6(\Psi^6)
  =V_6(\Psi^6)-\tfrac65\,vV_4^{-1}v$.

**The central new construction (§2):** the composite $\mathcal C=V_5V_4^{-1}V_5$ of
R19, which sits *inside* the three-$\Sigma_2$ vertex $W_6$ in the minimal
presentation, **relocates** into the $\Sigma_3$-kinetic pairing in the dressed
presentation via the map $\Phi$. The on-shell collapse
$\tilde u(P)=\tilde M\,p_3$ (the dressed analogue of R20's $u(P)=Mp_3$) is an identity,
so $\Sigma_3^*=\Psi^{\otimes3}$ exactly on-shell and the $\Sigma_3$-contact is
$W_6(\Psi^6)$ — the feedback is subtracted *inside* the $\Sigma_3$ sector, not by a
separate three-$\Sigma_2$ composite vertex.

**Gauge law (§4), the headline:**
- **$\Sigma_3$ is Gaussian with a $\Psi$-independent kernel** (both $\tilde M$ and $M$
  are built from $V_4,V_5,V_6$ with no $\Psi$-dependence). Consequently the
  $\Sigma_3$-deviation $Y_3=\Sigma_3-\Sigma_3^*(\Psi,\Sigma_2)$ transforms
  **trivially homogeneously**: $\boxed{\delta Y_3=0}$, i.e.
  $\delta\Sigma_3=\delta\Sigma_3^*(\Psi,\Sigma_2)=(b/2a)\tilde M^{-1}
  [\partial_\Psi\tilde u\,\delta\Psi+\partial_{\Sigma_2}\tilde u\,\delta\Sigma_2]$
  (dressed; bare analogue with $M,u$). **No homogeneous rotation of $Y_3$ at
  $O(g_s^4$)** — the first place such a rotation could appear is $O(g_s^5)$, where
  R12 sources $\Sigma_3$ cubically ($V_7=(3,2,2)$) and the Gaussian structure is lost.
- **$\Sigma_2$ follows the R19 implicit homogeneous law**, with the
  $\Sigma_3$-exchange ($\tilde u^\top\tilde M^{-1}\tilde u$ dressed, or
  $u^\top M^{-1}u$ elementary) folded into the saddle Hessian $\mathcal K$ and the
  cubic kernel $T$. The exact off-shell equality
  $\delta S-\delta S_{\rm eff}^{(6)}=\delta[\mathbb F]$ holds with $\mathbb F$
  $\Sigma$-independent: $\mathbb F_5^{\rm dr}=O(g_s^5)$ (closes), 
  $\mathbb F_4^{\rm elem}=(g_s^4/600)vV_4^{-1}v+\dots$ (R20 residual, does not close
  at $O(g_s^4)$ but the equality is still exact).
- **The comparison:** the gauge-law *structure*
  is **identical** in both presentations — homogeneous, saddle-tracking, no
  independent two-string parameter, $\delta Y_3=0$. The obstruction in the elementary
  presentation is **purely dynamical** (the on-shell contact is $V_6(\Psi^6)$ not
  $W_6(\Psi^6)$; the feedback survives), **not** a gauge-algebra obstruction. The
  gauge law does not "see" the composite-vs-elementary distinction; the master
  equation does not enter the gauge invariance at either presentation, only the
  on-shell matching. This sharpens R19 §7: master-equation-agnosticism holds at the
  level of both the matching *and* the gauge law.

**EOMs (§3):** $\Sigma_3$-EOM Gaussian (exact saddle $\Sigma_3^*=(b/2a)\tilde M^{-1}
\tilde u$); $\Sigma_2$-EOM implicit (R19's $\tilde X_6=0$ with the $\Sigma_3$
back-reaction folded in). Auxiliarity chain: $\Sigma_2$ aux $\iff V_4|_{\Sym^2}$ non-deg
(R9); $\Sigma_3$ aux $\iff\tilde M|_{\Sym^3}$ non-deg (dressed) / $M|_{\Sym^3}$
non-deg (elementary, R20); in the dressed case $\tilde M=M-\tfrac65 N$ requires
*both* $V_4$ and $V_6$ (hence $M$) well-defined, tying the two invertibility
conditions together.

**IBL$_\infty$ rewriting (§5), tree level:** the $O(g_s^4)$ action exercises the
genus-zero products $\ell_4=p_{4,1,0}$, $\ell_5=p_{5,1,0}$, $p_{3,2,0}=\Delta\circ
\ell_4$, $p_{4,2,0}=\Delta\circ\ell_5$ (bare), and the **dressed**
$\tilde p_{4,2,0}=\Delta\circ\tilde\ell_5$ with $\tilde\ell_5$ built from
$\tilde V_6=V_6-\tfrac65\mathcal C$. The IBL component relations through $(4,2,0)$:
the $(k,1,0)$ relations are the $L_\infty$ Jacobi axioms (required, not agnostic);
the $(k,2,0)$ relations are, by the R16 lemma *extension* (proven at $(2,2,0)$
only; its $(3,2,0)$/$(4,2,0)$ instances are structurally expected but their lemma
proofs are NOT done — §5.4), consequences of the $L_\infty$ axioms on the
even-parity sector. The dressed $\tilde p_{4,2,0}$ satisfies the $(4,2,0)$
relation iff the bare $p_{4,2,0}$ does *and* the lower-product relations (through
$\ell_4$) hold — the composite $\mathcal C$ is built from $p_{3,2,0}$ and
$p_{2,2,0}^{-1}$, so it inherits their relations. **The dressing is therefore
structurally expected to introduce no new IBL relation** — pending the
$(3,2,0)$/$(4,2,0)$ lemma proofs, which are the remaining computational core
(flagged in §5.4/§7); the R16 two-lemma method is proven only for $(2,2,0)$, so
the structural verdict rests on the R16 pattern + R19 §7, not on a completed
proof.

---

## 1. Setup: the two presentations

Let $P:=\Psi^{\otimes2}$, $p_3:=\Psi^{\otimes3}\in\Sym^3\Hilb_0$, $v:=V_5(\cdot,P,\Psi)$
(the R17 cubic source covector on $\Sym^2$). Through $O(g_s^3)$ both presentations
share R17:
$$S_{\le3}=S_{\rm HS}[\Psi,\Sigma_2]+\tfrac{g_s^3}{5!}V_5(\Sigma_2,\Sigma_2,\Psi),\qquad
S_{\rm HS}=[\text{shared}]-\tfrac{g_s^2}{4!}V_4(\Sigma_2,\Sigma_2)
+\tfrac{2g_s^2}{4!}V_4(\Sigma_2,P).$$

The $O(g_s^4)$ sector differs:

**(P-elementary)** (R20, with $c_6=0$ for the cleanest comparison — the geometric
$V_6(\Sigma_2,\Sigma_2,\Sigma_2)$ term is omitted, since the dressed presentation
replaces the three-$\Sigma_2$ vertex by the $\Sigma_3$ sector):
$$S_{\rm elem}=S_{\le3}+\tfrac{g_s^4}{6!}\big[-a\,V_6(\Sigma_3,\Sigma_3)
+b\,V_6(\Sigma_3,\Sigma_2,\Psi)\big].$$

**(P-dressed)**: the $\Sigma_3$ sector uses the composite
vertex $\tilde V_6$ in *both* the kinetic and the source:
$$S_{\rm dr}=S_{\le3}+\tfrac{g_s^4}{6!}\big[-a\,\tilde V_6(\Sigma_3,\Sigma_3)
+b\,\tilde V_6(\Sigma_3,\Sigma_2,\Psi)\big].$$

The composite $\tilde V_6$ is constructed in §2. Natural normalisation both
presentations: $(a,b)=(1,2)$ (so $\Sigma_3^*=\Psi^{\otimes3}$ on-shell; see §3).

**Why $c_6=0$ in the dressed presentation.** In R19 (minimal, $\Sigma_2$-only) the
three-$\Sigma_2$ vertex $W_6(\Sigma_2,\Sigma_2,\Sigma_2)$ carries *both* the
$V_6$-contact and the $-\tfrac65\mathcal C$ feedback-subtraction. Introducing
$\Sigma_3$ *replaces* that vertex: the $V_6$-contact becomes the $\Sigma_3$-propagator
collapse, and the $-\tfrac65\mathcal C$ feedback-subtraction moves into the
$\Sigma_3$-kinetic. A residual $c_6 V_6(\Sigma_2,\Sigma_2,\Sigma_2)$ would
double-count the contact (one $V_6(\Psi^6)$ from the $\Sigma_3$ collapse, another
from the $c_6$-vertex), so it is set to zero. (The elementary presentation allows
$c_6\neq0$ to test whether it can substitute for the missing feedback subtraction —
R20 shows it cannot.)

## 2. The dressed composite vertex $\tilde V_6$: the $\Phi$-map construction

The key structural object is the linear map
$$\Phi:\Sym^3\Hilb_0\to(\Sym^2\Hilb_0)^*,\qquad \Phi(X)_I:=V_5(\Lambda^2_I,X),$$
where $\{\Lambda^2_I\}$ is an orthonormal $\Sym^2$ basis and $V_5(\Lambda^2_I,X)$
contracts $V_5$ on 2 of its 5 slots with $\Lambda^2_I$ and on the remaining 3 with
$X\in\Sym^3$ (well-defined by total symmetry of $V_5$). In components,
$\Phi_{IK}=V_5(\Lambda^2_I,\Lambda^3_K)$ for an orthonormal $\Sym^3$ basis
$\{\Lambda^3_K\}$.

**Lemma 2.1 (the Veronese collapse of $\Phi$).** $\Phi(\Psi^{\otimes3})=v$, i.e.
$\Phi_{IK}(p_3)_K=v_I=V_5(\Lambda^2_I,P,\Psi)$. *Proof:* $V_5(\Lambda^2_I,\Psi^{\otimes3})$
$=V_5(\Lambda^2_I,\Psi,\Psi,\Psi)$ (3 slots) $=V_5(\Lambda^2_I,\Psi^{\otimes2},\Psi)$
(2+1 slots) $=V_5(\Lambda^2_I,P,\Psi)=v_I$, using total symmetry of $V_5$ to identify
the 3-$\Psi$ contraction with the $(\Psi^{\otimes2},\Psi)$ split. ✓ (Script check 1.)

**The composite bilinear form on $\Sym^3$:**
$$N:=\Phi^\top V_4^{-1}\Phi:\Sym^3\times\Sym^3\to\R,\qquad
N(A,B)=\Phi(A)^\top V_4^{-1}\Phi(B).$$
$N$ is symmetric ($V_4^{-1}$ symmetric on the even sector, R7) and
$\Psi$-**independent** ($\Phi$ and $V_4^{-1}$ use no $\Psi$). Its Veronese value:
$$N(\Psi^{\otimes3},\Psi^{\otimes3})=\Phi(\Psi^{\otimes3})^\top V_4^{-1}\Phi(\Psi^{\otimes3})
=v^\top V_4^{-1}v\quad\text{(by Lemma 2.1).}$$

**The dressed kinetic and source.** Let $M:=V_6|_{\Sym^3}$ (the bare
$\Sigma_3$-kinetic, R20) and $u(\Sigma_2):=V_6(\cdot,\Sigma_2,\Psi)$ (the bare
source, linear in $\Sigma_2$). Define
$$\boxed{\;\tilde M:=M-\tfrac65\,N,\qquad
\tilde u(\Sigma_2):=u(\Sigma_2)-\tfrac65\,\Phi^\top V_4^{-1}\,v(\Sigma_2),\;}$$
where $v(\Sigma_2)_I:=V_5(\Lambda^2_I,\Sigma_2,\Psi)$ (the $\Sigma_2$-dependent
extension of $v$; on-shell $v(P)=v$). Then:

- **Dressed kinetic on the Veronese diagonal:**
  $\tilde M(\Psi^{\otimes3},\Psi^{\otimes3})=M(p_3,p_3)-\tfrac65 N(p_3,p_3)
  =V_6(\Psi^6)-\tfrac65\,vV_4^{-1}v=:W_6(\Psi^6).$ ✓ (Script check 2.)
- **Dressed source Veronese collapse:**
  $\tilde u(P)=u(P)-\tfrac65\Phi^\top V_4^{-1}v=M\,p_3-\tfrac65\,N\,p_3=\tilde M\,p_3,$
  using $u(P)=Mp_3$ (R20's collapse) and $\Phi^\top V_4^{-1}v=Np_3$ (Lemma 2.1).
  ✓ (Script check 2.) This is the dressed analogue of R20's $u(P)=Mp_3$.

**Reading.** $\tilde V_6$ is not a geometric vertex: it is not totally symmetric under
all $S_6$ strand permutations (the $N$-part is symmetric under
$\Sym^3\times\Sym^3\subset S_6$ and within each $\Sym^3$, but not under mixed
permutations). It is a *composite* bilinear on $\Sym^3$: the composite is
relocated from $W_6$ into the $\Sigma_3$-kinetic pairing; it is not elementary.
The $\Phi$-map is the mechanism of the relocation: it converts the
$\Sigma_2$-channel feedback $vV_4^{-1}v$ (a $\Sym^2$-channel object) into a
$\Sym^3$-kinetic correction $N$.

## 3. Equations of motion

Both presentations have the same $\Sigma_3$-EOM structure (Gaussian, since
$\Sigma_3$ appears only bilinearly + linearly at $O(g_s^4)$):
$$\frac{\partial S}{\partial\Sigma_3}=0\;\Longrightarrow\;
\Sigma_3^*=\tfrac{b}{2a}\,K_3^{-1}\,s(\Sigma_2),$$
with $(K_3,s)=(\tilde M,\tilde u)$ (dressed) or $(M,u)$ (elementary). On-shell
($\Sigma_2=P$): $s(P)=K_3\,p_3$ (the Veronese collapse, §2 dressed / R20 elementary),
so $\Sigma_3^*=\tfrac{b}{2a}p_3=\Psi^{\otimes3}$ for $(a,b)=(1,2)$. The on-shell
$\Sigma_3$-contact:
$$\tfrac{g_s^4}{6!}\cdot\tfrac{b^2}{4a}\,s(P)^\top K_3^{-1}s(P)
=\tfrac{g_s^4}{6!}\cdot\tfrac{b^2}{4a}\,p_3^\top K_3\,p_3
=\begin{cases}\tfrac{g_s^4}{6!}\,W_6(\Psi^6) & \text{(dressed, }b^2/4a=1\text{)},\\
\tfrac{g_s^4}{6!}\,V_6(\Psi^6) & \text{(elementary, }b^2/4a=1\text{)}.\end{cases}$$

**$\Sigma_2$-EOM.** Eliminating $\Sigma_3$ first (exact Gaussian), the effective
$\Sigma_2$ action is $S_{\le3}$ plus an $O(g_s^4)$ quadratic-in-$\Sigma_2$ term
$(g_s^4/6!)(b^2/4a)\,s(\Sigma_2)^\top K_3^{-1}s(\Sigma_2)$. The $\Sigma_2$-EOM is
then the R19 implicit saddle equation $\tilde X_6=0$ (R19 eq. 4, with $K_6,v_6,T$),
**modified** by this additional $O(g_s^4)$ term in the Hessian and source:
- the kinetic kernel gains $+(g_s^4/6!)(b^2/4a)\cdot 2\,(\partial_{\Sigma_2}s)^\top
  K_3^{-1}(\partial_{\Sigma_2}s)$ — an $O(g_s^4)$ correction to $K_6$;
- the source gains $+(\dots)$ — an $O(g_s^4)$ correction to $v_6$.

Both corrections are $\Sigma_2$-quadratic / $\Psi$-cubic structures built from
$V_4,V_5,V_6$ (and $V_4^{-1}$ in the dressed case). The implicit structure is
unchanged: the $\Sigma_2$-saddle is a perturbative fixed point
$\Sigma_2^*(\Psi)=P+O(g_s)$, Neumann-solvable for small $g_s$ (R19).

**Commentary.**
- *Auxiliarity chain.* $\Sigma_2$ auxiliary $\iff V_4|_{\Sym^2}$ non-deg (R9);
  $\Sigma_3$ auxiliary $\iff K_3$ non-deg on $\Sym^3$. In the dressed case
  $\tilde M=M-\tfrac65 N$ requires $V_4$ invertible (for $N$) *and* $\tilde M$
  invertible (for the $\Sigma_3$-propagator) — so the dressed auxiliarity ties R9's
  $V_4|_{\Sym^2}$ condition to the new $V_6|_{\Sym^3}$ condition (R20). In the
  elementary case only $M=V_6|_{\Sym^3}$ is needed (R20). Both are CFT-open
  (A2(iii)/T4 carve-out).
- *Implicit vs Gaussian.* $\Sigma_3$ stays Gaussian through $O(g_s^4)$ (its kinetic
  is bilinear, no cubic-in-$\Sigma_3$ term). $\Sigma_2$ goes implicit as soon as the
  $W_6$/$\tilde V_6$ coupling is added (R19). The pattern persists until $O(g_s^5)$,
  where R12 sources $\Sigma_3$ cubically via $V_7(\Sigma_3,\Sigma_2,\Sigma_2)$
  ($7=3+2+2$) — at that point $\Sigma_3$ too goes implicit.
- *Veronese saddle.* $\Sigma_2^*=P+O(g_s)$, $\Sigma_3^*=\Psi^{\otimes3}$ (exact, both
  presentations, for $(a,b)=(1,2)$). The saddle lives on the Veronese curve
  $\Sigma_k=\Psi^{\otimes k}$.
- *Annotation confirmation.* The dressed $\Sigma_3$-EOM is exactly "$W_6$-composite
  relocated into a kinetic pairing" — confirmed: $\tilde M$
  absorbs the $-\tfrac65\mathcal C$ feedback-subtraction, and the Gaussian
  elimination reproduces $W_6(\Psi^6)$ on-shell.

## 4. Gauge transformations at $O(g_s^4)$

Under the truncated $L_\infty$ transformation of $S_{\rm eff}^{(6)}$ on $\Psi$,
$$\delta\Psi=Q_B\Lambda+g_s\ell_2(\Psi,\Lambda)+\tfrac{g_s^2}{2}\ell_3(\Psi,\Psi,\Lambda)
+\tfrac{g_s^3}{6}\ell_4(\Psi,\Psi,\Psi,\Lambda)+\tfrac{g_s^4}{24}\ell_5(\Psi^{\otimes4},\Lambda),$$
one has $\delta S_{\rm eff}^{(6)}=O(g_s^5)$ (geometric master equation through
$V_{0,6}$). We seek $(\delta\Sigma_2,\delta\Sigma_3)$ such that
$\delta S-\delta S_{\rm eff}^{(6)}=\delta[\mathbb F]$ **exactly** (off-shell,
arbitrary $\delta\Psi$), with $\mathbb F$ $\Sigma$-independent.

### 4.1 The $\Sigma_3$ gauge law: trivial homogeneous

Write $Y_3:=\Sigma_3-\Sigma_3^*(\Psi,\Sigma_2)$. The $\Sigma_3$-sector of $S$ at
$O(g_s^4)$ is the Gaussian
$$\tfrac{g_s^4}{6!}\big[-a\,K_3(Y_3,Y_3)+(\text{linear in }Y_3)\big],\qquad
K_3\in\{\tilde M,M\},$$
and **$K_3$ is $\Psi$-independent** (both $\tilde M=M-\tfrac65 N$ and $M$ are built
from $V_4,V_5,V_6$ and the fixed bases; no $\Psi$ enters). The variation of the
Gaussian in $Y_3$ is
$$\delta\big[-\tfrac{g_s^4}{6!}a\,K_3(Y_3,Y_3)\big]
=-\tfrac{g_s^4}{6!}\,2a\,K_3(\delta Y_3,Y_3).$$
For this to vanish for arbitrary $Y_3$ (the off-shell equality demands the
$\Sigma$-dependent part of $\delta S$ cancel), $K_3(\delta Y_3,Y_3)=0$ for all
$Y_3$, hence $\delta Y_3=0$ (since $K_3$ non-deg, the auxiliarity condition). So:
$$\boxed{\;\delta Y_3=0,\qquad
\delta\Sigma_3=\delta\Sigma_3^*(\Psi,\Sigma_2)
=\tfrac{b}{2a}\,K_3^{-1}\big[(\partial_\Psi s)\,\delta\Psi
+(\partial_{\Sigma_2}s)\,\delta\Sigma_2\big],\;}$$
with $(K_3,s)=(\tilde M,\tilde u)$ (dressed) or $(M,u)$ (elementary). The
$\Sigma_3$-deviation transforms **trivially homogeneously** — no rotation, no
inhomogeneous $\hat Q\Lambda_1$ piece. $\Sigma_3$ transforms as its saddle, exactly
(R11 pattern, extended).

Script check 3 verifies $\delta Y_3=0$ genuinely (rewritten 2026-07-09 after the
blind critic pass — the original version solved for $\delta\Sigma_3$ from the
cancellation condition and then re-evaluated the same condition, a tautology
[S1]). Three legs, both presentations: **(a)** the analytic law
$\delta\Sigma_3^*=(b/2a)K_3^{-1}[\partial_\Psi s\,\delta\Psi
+\partial_{\Sigma_2}s\,\delta\Sigma_2]$ agrees with the central finite difference
of the saddle map $\Sigma_3^*(\Psi\pm\epsilon\delta\Psi,
\Sigma_2\pm\epsilon\delta\Sigma_2)$ computed from the source functions alone (an
independent route, $10^{-10}$); **(b)** transporting the fields with the
saddle-tracking-only law and central-differencing the $\Sigma_3$-sector action at
two different random $Y_3$ gives *equal* variations ($Y_3$-independence,
$10^{-15}$) — this is the direct machine statement of $\delta Y_3=0$;
**(c) falsification:** perturbing the kernel to a $\Psi$-dependent
$K_3+\lambda W(\cdot,\cdot,\Psi)$ (mimicking the $O(g_s^5)$ $\tilde V_7$
dressing, 018 §7) breaks leg (b) by exactly the predicted residual
$-a\tfrac{g^4}{6!}[Y_3^aδK_3Y_3^a-Y_3^bδK_3Y_3^b]$, and the R25-type kernel
rotation $\delta Y_3=-\tfrac12K_3^{-1}(\delta K_3)Y_3$ restores
$Y_3$-independence — the check distinguishes $\Psi$-independent kernels
(rotation $=0$) from $\Psi$-dependent ones, so it would fail if $\delta Y_3=0$
were wrong.

### 4.2 The $\Sigma_2$ gauge law: implicit homogeneous (R19 pattern)

After eliminating $\Sigma_3$, the $\Sigma_2$-effective action is
$$S\big|_{\Sigma_3^*}=S_{\le3}[\Psi,\Sigma_2]
+\tfrac{g_s^4}{6!}\tfrac{b^2}{4a}\,s(\Sigma_2)^\top K_3^{-1}s(\Sigma_2)
=:S_{\le3}+\tfrac{g_s^4}{6!}\tfrac{b^2}{4a}\,\mathcal E(\Sigma_2,\Psi),$$
with $\mathcal E$ the $\Sigma_3$-exchange (dressed: $\tilde u^\top\tilde M^{-1}\tilde u$;
elementary: $u^\top M^{-1}u=\mathcal D$, R20). This is an $O(g_s^4)$
quadratic-in-$\Sigma_2$ addition. Around the joint saddle $\Sigma_2^*(\Psi)$, write
$Y_2:=\Sigma_2-\Sigma_2^*(\Psi)$ and expand (R19's Taylor-of-a-cubic, now with the
$\mathcal E$-term folded in):
$$S\big|_{\Sigma_3^*}=S_{\rm eff}^{(6)}+\Phi_2(Y_2;\Psi)+\mathbb F(\Psi),\qquad
\Phi_2=-\tfrac{g_s^2}{4!}\mathcal K(Y_2,Y_2)+\tfrac{g_s^4}{6!}T(Y_2,Y_2,Y_2),$$
with $\mathcal K$ the saddle Hessian ($K_6$ plus the $\mathcal E$-contribution) and
$T=W_6$-derived (R19). **In the dressed presentation $T_{\rm dr}=0$ at this order**:
$c_6=0$ (no $V_6(\Sigma_2^3)$ term — $\Sigma_3$ replaces the three-$\Sigma_2$
vertex) and $\mathcal E=s^\top K_3^{-1}s$ is *quadratic* in $\Sigma_2$ (since $s$ is
linear in $\Sigma_2$), hence quadratic in $Y_2$ — it contributes to the Hessian
$\mathcal K$ only, not to a cubic $T$. The $\Sigma_2$ law is therefore the
**R17-type** (quadratic-form invariance, no $T$-correction) with an
$O(g_s^4)$-dressed Hessian — a special case of the R19 implicit form with $T=0$. In
the elementary presentation $T_{\rm elem}=c_6 V_6$ (if $c_6\neq0$) plus the
$\mathcal E$-contribution (still quadratic, so no cubic from $\mathcal E$). Demanding
$\delta\Phi_2=0$ under arbitrary $\delta\Psi$ gives the R19 implicit law:
$$\boxed{\;\delta Y_2=\mathcal K^{-1}\Big[-\tfrac12(\delta\mathcal K)(\cdot,Y_2)
+\tfrac{g_s^2}{20}\,T(\cdot,Y_2,\delta Y_2)\Big],\qquad
\delta\Sigma_2=\delta\big[\Sigma_2^*(\Psi)\big]+\delta Y_2,\;}$$
Neumann-solvable for small $g_s$, homogeneous ($\delta Y_2|_{Y_2=0}=0$). With
$\delta Y_3=0$ from §4.1, the **exact** off-shell equality holds:
$$\delta S-\delta S_{\rm eff}^{(6)}=\delta[\mathbb F(\Psi)],\qquad
\mathbb F=\begin{cases}\mathbb F_5^{\rm dr}=O(g_s^5)&\text{(dressed, closes)},\\
\mathbb F_4^{\rm elem}=\tfrac{g_s^4}{600}vV_4^{-1}v+\tfrac{g_s^4}{6!}(c_6+\tfrac{b^2}{4a}-1)
V_6(\Psi^6)+O(g_s^5)&\text{(elementary, R20 residual)}.\end{cases}$$

**Verification status of this subsection (corrected 2026-07-09 [S2]).** Script
check 4 tests the **on-shell** version only: $S(\sigma^*)-S_{\rm eff}^{(6)}
=\mathbb F(\Psi)$ with the $O(g_s^4)$ coefficient of $\mathbb F$
Richardson-extrapolated (dressed $\to0$, elementary $\to$ the R20 residual). The
**off-shell** exactness $\delta S-\delta S_{\rm eff}^{(6)}=\delta[\mathbb F]$ and
the boxed $\delta Y_2$ Neumann law are **analytic**, inherited from R19's
hand-verified off-shell equality (the $\Sigma_3$-exchange addition is quadratic
in $Y_2$, so it deforms the Hessian $\mathcal K$ without changing the R19
structure); they are *not* independently machine-checked here. Check 5 tests
**saddle stationarity** ($O(\epsilon^2)$ response off the saddle) — the
ingredient that makes saddle-tracking consistent — as a proxy; the
gauge-homogeneity statement $\delta Y_2|_{Y_2=0}=0$ itself is analytic (the law
is linear-homogeneous in $Y_2$ by construction), and $\delta Y_3=0$ is check 3's
leg (b).

### 4.3 The comparison: gauge structure is identical, the obstruction is dynamical

| | **(P-dressed)** | **(P-elementary)** |
|---|---|---|
| $\Sigma_3$ kinetic $K_3$ | $\tilde M=M-\tfrac65 N$ (composite, $\Psi$-indep) | $M$ (bare, $\Psi$-indep) |
| $\delta Y_3$ | $0$ (trivial homogeneous) | $0$ (trivial homogeneous) |
| $\Sigma_2$ law | R19 implicit, $\mathcal K_{\rm dr}$, $T_{\rm dr}=0$ | R19 implicit, $\mathcal K_{\rm elem}$, $T_{\rm elem}=c_6 V_6+\dots$ |
| $\delta S-\delta S_{\rm eff}^{(6)}$ | $=\delta[\mathbb F_5]$, $\mathbb F_5=O(g_s^5)$ ✓ | $=\delta[\mathbb F_4]$, $\mathbb F_4=O(g_s^4)\neq0$ ✗ |
| independent $\Lambda_1$? | no (R18 pattern) | no (R18 pattern) |

**The gauge-law structure is identical** in both presentations: $\Sigma_3$ trivial
homogeneous, $\Sigma_2$ implicit homogeneous, no independent two-string parameter.
The elementary presentation's failure is **not** a gauge-algebra obstruction — the
gauge law exists, is homogeneous, and satisfies the exact equality — but a
**dynamical** one: $\mathbb F_4^{\rm elem}\neq0$ because the on-shell
$\Sigma_3$-contact is $V_6(\Psi^6)$ (bare collapse) not $W_6(\Psi^6)$ (dressed
collapse), so the R17 feedback $(g_s^4/600)vV_4^{-1}v$ is not subtracted. The gauge
law "does not see" the composite-vs-elementary distinction; only the on-shell
matching does. This is the structure the comparison was set up to test: the
obstruction lives in the target (the master-equation content of $S_{\rm eff}^{(6)}$,
R19 §7), not in the gauge invariance.

**Warrant for the off-shell claim [C2].** The "dynamical, not gauge-algebraic"
verdict rests on $\mathbb F_4^{\rm elem}$ being a genuinely *off-shell*
$\Sigma$-independent functional, not merely its on-shell value. The warrant is
R19's hand-verified off-shell equality (R19 established
$\delta S-\delta S_{\rm eff}^{(6)}=\delta[\mathbb F]$ off-shell for the minimal
presentation by explicit Taylor expansion around the saddle): the present
$O(g_s^4)$ actions differ from R19's only by the $\Sigma_3$-exchange
$\mathcal E=s^\top K_3^{-1}s$, which is *quadratic* in $\Sigma_2$ (hence in
$Y_2$) and Gaussian in $\Sigma_3$, so the R19 Taylor structure — quadratic form
in $Y_2$ plus a $\Sigma$-independent remainder — is preserved term by term.
Machine-checked here is only the on-shell value (check 4); the off-shell
$\Sigma$-independence of $\mathbb F$ is analytic-by-inheritance, not
independently machine-verified.

## 5. IBL$_\infty$ rewriting (tree level, $g=0$)

### 5.1 The products at $O(g_s^4)$

The genus-zero $\IBL$ products $p_{k,\ell,0}:\E_k\Hilb_0\to\E_\ell\Hilb_0$ the
$O(g_s^4)$ action exercises, in physical $N_{\rm gh}$ (formula
$N_{\rm gh}(p_{k,\ell,0})=3\ell-2k$ — the $g=0$ slice of R23's two-parameter
$N_{\rm gh}(p_{k,\ell,g})=3\ell-2k+g$, which supersedes the stale R15/A3
attribution [M2]):

| product | definition | $N_{\rm gh}$ | enters via |
|---|---|---|---|
| $\ell_4=p_{4,1,0}$ | $\Delta\circ V_5$ (4 in, 1 out) | $-5$ | $V_5$ coupling (R17), $V_5(\cdot,\cdot,\Psi)$ dressing |
| $\ell_5=p_{5,1,0}$ | $\Delta\circ V_6$ (5 in, 1 out) | $-7$ | $V_6$ contact (R19/$\Sigma_3$) |
| $p_{3,2,0}$ | $\Delta\circ\ell_4$ (3 in, 2 out) | $0$ | two-output from $V_5$ |
| $p_{4,2,0}$ | $\Delta\circ\ell_5$ (4 in, 2 out) | $-2$ | two-output from $V_6$ (**bare**) |
| $\tilde p_{4,2,0}$ | $\Delta\circ\tilde\ell_5$ (4 in, 2 out) | $-2$ | two-output from $\tilde V_6$ (**dressed**) |

Here $\tilde\ell_5$ is the bracket built from $\tilde V_6$:
$$\tilde\ell_5=\ell_5-\tfrac65\,\ell_5^{\mathcal C},\qquad
\ell_5^{\mathcal C}:=\Delta\circ\mathcal C\text{-shaped (the }\Phi^\top V_4^{-1}\Phi
\text{ contribution to the two-output product).}$$

**The structural reading of $\tilde p_{4,2,0}$.** The bare $p_{4,2,0}=\Delta\circ
\ell_5$ is the two-output product from the geometric $V_6$. The dressed
$\tilde p_{4,2,0}$ is the two-output product the $\Sigma_3$-sector actually uses (via
$\tilde M$). The dressing $\ell_5^{\mathcal C}$ is a composition of lower products:
$\mathcal C=V_5V_4^{-1}V_5$ is $p_{3,2,0}\circ p_{2,2,0}^{-1}\circ p_{3,2,0}$-shaped
(two $V_5$-raised products joined by the $\Sigma_2$-propagator $p_{2,2,0}^{-1}=
V_4^{-1}$). So:
$$\tilde p_{4,2,0}=p_{4,2,0}-\tfrac65\,(\text{composition of }p_{3,2,0},
p_{2,2,0}^{-1},p_{3,2,0}).$$
**This is the first place a two-output $\IBL$ product is not simply
$\Delta\circ\ell_n$** but a dressed, composite object built from lower products. It
is the IBL-level avatar of R19's $W_6=V_6-\tfrac65\mathcal C$.

### 5.2 The IBL component relations through $(4,2,0)$

Extending `eq:rels` of the pedagogical note, the genus-zero relations the $O(g_s^4)$
action tests (from $\hat p\circ\hat p=0$ at each signature). Convention for the
relation $N_{\rm gh}$ labels (fixed 2026-07-09 [M1]): a $(k,\ell,0)$ *relation*
contains $Q\circ p_{k,\ell,0}$, so its ghost number is the product's plus $Q$'s,
$N_{\rm gh}=(3\ell-2k)+1$ uniformly:

- **$(4,1,0)$:** $Q\circ_1\ell_4+\ell_2\circ_1\ell_3+\ell_3\circ_1\ell_2+\ell_4\circ_1
  \hat Q=0$, $N_{\rm gh}=-4$. **The $L_\infty$ Jacobi through $\ell_4$**:
  $[Q,\ell_4]+[\ell_2,\ell_3]=0$. Holds iff the $L_\infty$ axiom through $\ell_4$
  holds — **$L_\infty$-required**, not agnostic.
- **$(5,1,0)$:** $[Q,\ell_5]+[\ell_2,\ell_4]+\tfrac12[\ell_3,\ell_3]=0$,
  $N_{\rm gh}=-6$. $L_\infty$ Jacobi through $\ell_5$. **$L_\infty$-required.**
- **$(3,2,0)$:** the relation coupling $p_{3,2,0}$ to $Q$, $\ell_2$, $\ell_3$,
  $p_{2,2,0}$, $p_{1,2,0}$, $N_{\rm gh}=+1$ (from $\hat p\circ\hat p=0$ at signature
  $(3,2,0)$; was misprinted $0$ [M1]). By the R16 lemma extension (Lemma A: $Q$-move across $\Delta$; Lemma
  B1: regrouping via $\ell_2$-cyclicity; Lemma B2: coderivation inert on even
  sector), $p_{3,2,0}=\Delta\circ\ell_4$ satisfies $(3,2,0)$ on the even-parity
  sector as a consequence of the $L_\infty$ axioms through $\ell_4$ (i.e. the
  $(4,1,0)$ relation). **$L_\infty$-required** (consequence of $(4,1,0)$).
- **$(4,2,0)$:** the relation coupling $p_{4,2,0}$ to $Q$, $\ell_2,\ell_3,\ell_4$,
  $p_{3,2,0},p_{2,2,0},p_{1,2,0}$, $N_{\rm gh}=-1$ (was misprinted $-3$ [M1]). By the R16 extension,
  $p_{4,2,0}=\Delta\circ\ell_5$ satisfies $(4,2,0)$ on the even-parity sector as a
  consequence of the $L_\infty$ axioms through $\ell_5$ (the $(5,1,0)$ relation).
  **$L_\infty$-required** (consequence of $(5,1,0)$).

### 5.3 The dressed $\tilde p_{4,2,0}$ and the master-equation-agnostic verdict

The dressed product $\tilde p_{4,2,0}=p_{4,2,0}-\tfrac65\,p_{4,2,0}^{\mathcal C}$,
where $p_{4,2,0}^{\mathcal C}$ is the composite built from $p_{3,2,0}\circ
p_{2,2,0}^{-1}\circ p_{3,2,0}$. Its $(4,2,0)$ relation:
$$[\hat Q,\tilde p_{4,2,0}]+\text{(lower composites)}
=\big([\hat Q,p_{4,2,0}]+\text{(lower)}\big)-\tfrac65\big([\hat Q,
p_{4,2,0}^{\mathcal C}]+\text{(lower)}\big).$$
The first bracket $=0$ by $(4,2,0)$ for $p_{4,2,0}$ ($L_\infty$-required). The
second: $p_{4,2,0}^{\mathcal C}$ is a composition of $p_{3,2,0}$ and
$p_{2,2,0}^{-1}$, whose relations are $(3,2,0)$ and $(2,2,0)$ — both
$L_\infty$-required (consequences of $(4,1,0)$ and $(3,1,0)$-Jacobi respectively, R16).
The $\hat Q$-variation of the composite is fixed by the lower products' relations,
so the second bracket $=0$ *as a consequence of the same $L_\infty$ axioms*. Hence:

> **$\tilde p_{4,2,0}$ satisfies the $(4,2,0)$ IBL relation iff the $L_\infty$ axioms
> through $\ell_5$ hold — the dressing introduces no new relation.** The composite
> $\mathcal C$ is built from lower products whose IBL relations are already implied
> by the $L_\infty$ axioms, so the dressed product inherits, it does not extend.

This is the IBL-level restatement of R19 §7 (matching is master-equation-agnostic):
the $O(g_s^4)$ *matching* closes on generic tensors because the composite is
algebraically determined by lower products; the *IBL relations* the products satisfy
are $L_\infty$-required (the $(k,1,0)$ and $(k,2,0)$ chains), but the dressing does
not add a new test — it reorganises existing $L_\infty$ content. The master
equation's entire content sits in the *target* $S_{\rm eff}^{(6)}$ (R19 §7); the IBL
products the cubic action uses are determined by that target, and their relations are
the $L_\infty$ axioms of the $\ell_n$, transferred.

**Presentation-dependence.** The bare $p_{4,2,0}$ (elementary presentation) and the
dressed $\tilde p_{4,2,0}$ (dressed presentation) satisfy the *same* $(4,2,0)$
relation under the *same* $L_\infty$ axioms. The IBL structure does not distinguish
the presentations — consistent with §4.3 (the gauge law does not either). The
difference between the presentations is purely in the *on-shell matching*
(dynamical, §3), not in the homological algebra.

**Scope of this verdict [C1].** The chain above uses the $(3,2,0)$ and $(4,2,0)$
relations for the bare products, whose lemma-based proofs are *not* done
(§5.4) — the R16 two-lemma method is proven only at $(2,2,0)$. The §5.3 verdict
("no new relation from the dressing") is therefore *structurally expected,
pending the $(3,2,0)$/$(4,2,0)$ lemma proofs*, not established at the same
standard as R16.

### 5.4 What is established vs the remaining computational core

**Established (this derivation + script):**
- The product identification and $N_{\rm gh}$ table (§5.1).
- The dressed $\tilde p_{4,2,0}$ as $p_{4,2,0}-\tfrac65(\text{lower composite})$ and
  the structural verdict that its $(4,2,0)$ relation adds no new test (§5.3).
- Script check 6: the $(4,1,0)$ combination $[Q,\ell_4]+[\ell_2,\ell_3]$ is
  **nonzero on generic data** — the falsifiability leg only, on a **dim-4** toy
  (description corrected 2026-07-09 [S2]: the earlier text claimed a symbolic
  imposition of the $L_\infty$ axioms and a dim-16 toy; neither is executed).
  The converse direction — the combination vanishes when the axioms hold — is
  the analytic statement that $(4,1,0)$ *is* the $L_\infty$ Jacobi axiom through
  $\ell_4$ (§5.2), not a machine check.

**Remaining computational core (flagged, not done here):** the full lemma-based
machine proof of $(3,2,0)$ and $(4,2,0)$ for $p_{k,2,0}=\Delta\circ\ell_{k+1}$,
extending R16's two-lemma method (Lemma A: $Q$-move; Lemma B1: regrouping; Lemma B2:
coderivation inertness on the even sector) from $(2,2,0)$ to the higher signatures.
This is a dedicated computational task (the R16 session produced two lemmas + a
dim-16 toy; $(3,2,0)$ and $(4,2,0)$ each need their own lemma chain, with the
$\ell_3\circ\ell_2$ and $\ell_4\circ\ell_2+\ell_3\circ\ell_3$ composites entering).
The structural verdict (consequence of the $L_\infty$ axioms, even-parity sector) is
clear from the R16 pattern + R19 §7; the machine proof confirms it. Candidate
follow-up: a dedicated session on the $(3,2,0)$ and $(4,2,0)$ lemmas, paralleling
R16.

## 6. Result and comparison with the ledger

**Candidate R21.** The $O(g_s^4)$ terms, completely understood:

1. **Gauge transformations (both presentations).** $\Sigma_3$ transforms trivially
   homogeneously ($\delta Y_3=0$, Gaussian + $\Psi$-independent kernel);
   $\Sigma_2$ follows the R19 implicit homogeneous law with the $\Sigma_3$-exchange
   folded into the Hessian. Exact off-shell equality
   $\delta S-\delta S_{\rm eff}^{(6)}=\delta[\mathbb F]$ with $\mathbb F$
   $\Sigma$-independent ($O(g_s^5)$ dressed / $O(g_s^4)$ elementary R20-residual).
   No independent two-string parameter (R18 pattern at three consecutive orders).
   The gauge structure is **identical** across presentations; the elementary failure
   is dynamical, not gauge-algebraic.
2. **EOMs.** $\Sigma_3$ Gaussian (exact saddle $\Psi^{\otimes3}$ on-shell);
   $\Sigma_2$ implicit (R19 $\tilde X_6=0$ with $\Sigma_3$ back-reaction). Auxiliarity
   chain $V_4|_{\Sym^2}$ (R9) + $K_3|_{\Sym^3}$ (R20), tied together in the dressed
   case.
3. **IBL$_\infty$ rewriting (tree level).** Products $\ell_4,\ell_5,p_{3,2,0},
   p_{4,2,0},\tilde p_{4,2,0}$ identified with $N_{\rm gh}=3\ell-2k$ (R23, $g=0$
   slice). Relations $(4,1,0),(5,1,0),(3,2,0),(4,2,0)$: the $(k,1,0)$ are
   $L_\infty$ Jacobi axioms; the $(k,2,0)$ are *structurally expected*
   consequences (R16 extension — proven at $(2,2,0)$ only; the
   $(3,2,0)$/$(4,2,0)$ lemma proofs are pending, §5.4). The dressed
   $\tilde p_{4,2,0}$ is structurally expected to introduce no new IBL relation —
   the composite is built from lower products whose relations are already
   $L_\infty$-implied — with the same pending-proof caveat. IBL structure does
   not distinguish presentations (consistent with §4.3).

**What is new vs the ledger:**
- The $\Phi$-map construction of $\tilde V_6$ (§2) — the mechanism by which R19's
  composite $\mathcal C$ relocates into the $\Sigma_3$-kinetic. Confirms the
  R20-Annotation in detail.
- The $\Sigma_3$ gauge law ($\delta Y_3=0$, §4.1) — new; R20 deferred it.
- The comparison showing the gauge structure is presentation-independent (§4.3) —
  the obstruction is dynamical.
- The IBL product table through $O(g_s^4)$ and the dressed-product structural verdict
  (§5) — new; the note's `eq:rels` stops at $(2,2,0)$.

**What is NOT done (flagged for a follow-up):**
- The full lemma-based machine proof of $(3,2,0)$ and $(4,2,0)$ (§5.4) — a dedicated
  computational session, paralleling R16.
- CFT-level analytics of $\tilde M^{-1}$ and the composite kernel (A2(iii)/T4).
- BV classification of the implicit homogeneous $\Sigma_2$ law — **SETTLED**
  (derivation 016 / R22, ST4): the $\delta Y_2$ law is the same BV object as the
  $O(g_s^3)$ $\delta\tilde X$ — the forced transformation law of the auxiliary field
  $Y_2$ within a **contractible pair**, generator $\propto Y_2$ (on-shell-vanishing),
  no independent parameter; *neither* HT-trivial (effective $\mu$ graded-symmetric,
  even fields require antisymmetric) *nor* nontrivial. "Implicit homogeneous" =
  field-dependent-kinetic corner (nonzero, Neumann-implicit rotation); the §4.1
  $\delta Y_3=0$ = field-**independent**-kinetic corner (rotation vanishes; the R11
  corner). See `agent/derivations/016-st4-bv-homogeneous-law.md`.
- The all-orders formulation (013 §8 / R20-Annotation uniform principle).

## 7. Open / carve-outs

(a) CFT-level analytics of $V_4^{-1},V_6^{-1},\tilde M^{-1},\mathcal C$ = A2(iii)/T4
(the dressed auxiliarity ties $V_4|_{\Sym^2}$ and $V_6|_{\Sym^3}$ together).
(b) Region identification inherited (R14(b) language); the composite $\tilde V_6$ is
algebraic, not a moduli-region object.
(c) The full $(3,2,0),(4,2,0)$ lemma proof (§5.4) — structural verdict clear, machine
proof is the follow-up.
(d) BV classification of the implicit homogeneous law — **SETTLED** (derivation 016 /
R22, ST4): auxiliary-field/contractible-pair law, neither HT-trivial nor nontrivial;
"implicit homogeneous" ($\delta Y_2$) and "trivial homogeneous" ($\delta Y_3=0$) are
the field-dependent vs field-independent kinetic corners of one BV class.
(e) The all-orders formulation: the dressed presentation suggests a uniform principle
(R20-Annotation: pair $\Sigma_k$ with the running effective vertex $V_{n,\rm eff}$,
then HS) — the $O(g_s^4)$ gauge/EOM/IBL structure here is its first instance.
(f) Perturbative-branch statements (R19 carve-out (g)); the toy saddle can fold at
large $g_s$.
