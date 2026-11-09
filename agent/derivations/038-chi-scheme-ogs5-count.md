# 038 — Can the χ scheme reach $O(g_s^5)$ with elementary couplings? A paper count

**Date:** 2026-09-21. **Brief:** `agent/briefs/active-computator-038-chi-count-20260921T153600.md`.
**Type:** planning-grade counting argument (no matching computation), to be followed by a
real $O(g_s^5)$ match.

**Literal task.** Enumerate the elementary cubic couplings of $(\Psi,\Sigma_2,\Sigma_3,\chi,\dots)$
allowed at $O(g_s^5)$ by coupling order, ghost number (R23) and symmetry; list the tree
contributions they generate at that order after eliminating the auxiliaries; decide whether
they can produce both $O(g_s^5)$ feedback structures $S_1,S_2$ with independent coefficients
without disturbing the $O(g_s^4)$ relation $b_\chi^2/a_\chi=4$ of 017 (R24).

**Motivating objective.** The rigor audit found that all $O(g_s^4)$–$O(g_s^5)$ exclusions
(R19, R20, R25) fixed the field content, and the one relaxation tried (R24, the wrong-sign
partner $\chi$) succeeded. If the $\chi$ scheme continues with elementary couplings, an
all-geometric cubic tower becomes the leading candidate for the project. This count decides
whether the expensive matching is worth running, and with which couplings.

**Status:** all sections written; two fix passes of 2026-09-21 completed. First pass (critic
`agent/reports/critic-038-20260921T164800.md`): the order-7 spanning claim is now an
enumeration (§3.1), the deficit table is derived row by row (§3.3), and the script carries a
joint-saddle scaling test of the order formula. Second pass (critic
`agent/reports/critic-038-iter2-20260921T191500.md`): the prefactors of rows 2 and 4 are
carried, so the free sextic split $c_6+c_{\Sigma_3}=1$ is shown to move the $S_2$ component of
the deficit (3.3c–d) — (5.1) is unique *given the split*, which §6.1 pins to $c_6=0$ and §6.2
item 7 asks the matching to scan; H1's kinetic clause is derived from the doublet $GL(2)$
(§2.4); the $b'_\chi\ne0$ parenthetical of §3.1.5 is withdrawn. Verification
(`codes/verify-chi-ogs5-count.py`, seeds 11, 29, 7): **63/63 PASS**, counted as **30
independent checks + 6 implied + 12 identities + 9 break legs + 6 weak break legs**, exit 0.
Last completed step: §7 (verification and self-review, updated for the second fix pass).
Next step: none in this record — hand over to the $O(g_s^5)$ χ-scheme matching computation
(see §6 "spec for the matching"), which must carry the seven tests of §6.2, the condition
$b'_\chi=0$ of (E4) and the pinned split $c_6=0$, $c_{\Sigma_3}=1$ of §6.1.

**Outcome (conditional).** Enough freedom, under H-B3, H-B4, H-B5, H1 and $b'_\chi=0$; the
coefficient values additionally depend on the pinned sextic split $c_6$.

---

## Claim tree

**Assumptions (record level).**

- **A1 (ghost/strand bookkeeping, R23).** Physical ghost number $\Ngh(\Psi)=2$,
  $\Ngh(\Sigma_k)=\Ngh(\chi_k)=2k$; a sphere vertex $V_n$ saturates at $\sum\Ngh=2n$. Hence
  the **strand count** $s$ ($s(\Psi)=1$, $s(\Sigma_k)=s(\chi_k)=k$) is conserved: a coupling
  built on $V_n$ has $\sum_i s_i=n$.
- **A2 (coupling order).** $V_n$ carries $g^{n-2}$ (normalisation $g^{n-2}V_n/n!$).
- **A3 (cubic action).** Every term is at most trilinear in the fields.
- **A4 (standing carve-out).** Tree level, on-shell-in-auxiliaries matching at generic
  off-shell $\Psi$, finite-dimensional algebraic layer; CFT-level status untouched (as in
  R19–R26).
- **A5 (auxiliarity).** $V_4$ on $\Sym^2\Hilb_0$ and $V_6|_{33}$ on $\Sym^3\Hilb_0$ are
  invertible (the R38 $\ker V_4$ caveat is inherited unchanged).
- **A6 (naive-contact rule, 018 §3).** The on-shell $O(g_s^5)$ contribution of an
  $O(g_s^5)$ coupling equals its naive contact at the leading saddles (the $\hat M^{-1}$ and
  $\hat s$ expansions restore the $1/7!$).
- **A7 (independence, 018 check 0).** $\{V_7(\Psi^7),S_1,S_2,S_3\}$ are independent functions
  of $\Psi$ at generic vertices. (A7 is *not* used for spanning; spanning is derived in
  §3.1.5.)
- **A8 (lower orders fixed, §3.1.3).** The couplings of $\mathrm{ord}\le4$ are those fixed by
  the already-closed $O(g_s^{\le4})$ matching (R21, R24, 018 §1): no coupling is admitted that
  gives an auxiliary a source earlier than §2.2 assumes.

*Note on A1 and the wrong-sign field.* $\Ngh(\chi_k)=2k$ is insensitive to the sign of the
kinetic form, so strand conservation gives χ **exactly the same coupling menu as $\Sigma_k$**.
Rule 1 therefore supplies no protection whatever for the χ-specific exclusions of §4.2(e) and
for $b'_\chi=0$: those come entirely from H1 and from (E4) respectively.

**Hypotheses.**

- **H-B3** (brief): the feedback invariant is generic at the actual string vertices.
- **H-B4** (brief): the opposite-sign $\chi$ is a harmless non-propagating auxiliary
  (contact kernel, no pole).
- **H-B5** (brief): the $\chi$ tower stays elementary.
- **H1** (declared here, §2.4): the *source-deprivation* of $\chi$ — no $V_4(\chi,\Psi^{\otimes2})$,
  no $V_4(\chi,\Sigma)$ — is a frame choice in the two-dimensional $\Sym^2$ doublet
  $(\Sigma,\chi)$, not a tuning. Since the second fix pass, only half of this is hypothetical:
  the absence of the kinetic mixing $V_4(\chi,\Sigma)$ (and $a_\chi=1$) **follows** from the
  doublet $GL(2)$ by a parameter count (§2.4, part 0); what is hypothetical is the alignment of
  the source doublet by the residual $\group{O}(1,1)$, which requires it to be timelike,
  $\lambda_\chi^2<a_\chi\lambda_\Sigma^2$ [corrected 2026-10-01: dual norm, Addendum N10.7; the inequality was printed with the wrong form].

**Root claim (N0).** With field content $(\Psi,\Sigma_2,\chi,\Sigma_3)$, **elementary
(bare geometric) vertices only**, and the condition $b'_\chi=0$ of (E4) (no $V_5(\chi,\Sigma_3)$
mixing), the $O(g_s^5)$ matching has exactly enough free couplings to close, and the
$O(g_s^4)$ relation $b_\chi^2/a_\chi=4$ is undisturbed. Outcome: **enough freedom**,
conditional on H-B3, H-B4, H-B5, H1 **and $b'_\chi=0$**. The *rank* statement is independent
of the free sextic split $c_6+c_{\Sigma_3}=1$; the *values* of the fitted coefficients are
not — (5.1) is unique only at a fixed split, pinned to $c_6=0$ in §6.1. [§5, §6]

Nodes:

- **N1** Order formula: the leading on-shell order of a coupling is
  $\mathrm{ord}=\big(\sum_i s_i-2\big)+\sum_i o_i$, with $o_i$ the saddle order of leg $i$. [§2.1;
  numerically tested, verification §7]
- **N2** Saddle orders in the χ scheme: $o(\Psi)=o(\Sigma_2)=o(\Sigma_3)=0$ (Veronese),
  $o(\chi)=1$ (composite, $\chi_*\propto gV_4^{-1}v$). [§2.2; numerically tested, §7]
- **N3** Strand-locality lemma: an all-elementary presentation generates only whole-slot
  tree contractions; strand-split invariants ($\mathcal C$-type, hence $S_3$) are not in its
  image. [§3.2]
- **N3′ (spanning lemma)** Under A3, A8, H1 and $b'_\chi=0$, the complete list of order-7
  whole-slot invariants an all-elementary χ-scheme presentation can generate is
  $\{V_7(\Psi^7),S_1,S_2\}$ — no fourth invariant, and none containing $M^{-1}$. With
  $b'_\chi\ne0$ a fourth invariant $S_4$ and a marginal χ–$\Sigma_3$ mixing chain appear. [§3.1.4–§3.1.5]
- **N4** The $O(g_s^5)$ deficit of the χ scheme lies in $\mathrm{span}\{V_7(\Psi^7),S_1,S_2\}$,
  and carries no $\Sigma_3$-propagator ($M^{-1}$) composite. [§3.3; uses A6, A8, N3, N3′]
- **N5** $\Sigma_3$ with its even HS pair at $O(g_s^4)$ is **forced** in the χ scheme too:
  on $(\Psi,\Sigma_2,\chi)$ no cubic coupling reaches 7 strands with an $O(1)$ saddle. [§4.1]
- **N6** The generator table at $O(g_s^5)$: $V_7|_{331}/V_7|_{322}\to V_7(\Psi^7)$;
  $V_5(\chi,\chi,\Psi)\to S_1$; $V_6(\chi,\Sigma,\Sigma)\to S_2$ (and $V_6(\chi,\Sigma_3,\Psi)\to S_2$,
  redundant). The induced $3\times3$ system is triangular (in fact diagonal) hence
  nonsingular. [§4.2, §5; uses A6, A8, H1]
- **N7** Non-disturbance: the two new χ couplings contribute first at $O(g_s^5)$, so
  $b_\chi^2/a_\chi=4$ is untouched; the $\Sigma_3$ pair changes only the sextic **contact
  split** $c_6+c_{\Sigma_3}=1$ at $O(g_s^4)$ — that split is, however, $O(g_s^5)$-visible: it
  weights the two $S_2$ sources and moves $\beta$, hence $d_\chi$ (3.3d). [§5.2, §3.3]
- **N8** One $\chi$ suffices at $O(g_s^5)$: every $\chi_3$ coupling lands at $O(g_s^6)$ unless
  $\chi_3$ is given an $O(g_s^4)$ source, in which case it degenerates into a second $\Sigma_3$. [§4.3]
- **N9 (falsifier)** The same count reproduces R20 (failure without χ at $O(g_s^4)$: deficit
  rank 2, generator rank 1) and R24 (closure with χ: rank 2 = rank 2), and 018 §5(a)
  (scheme-A failure at $n=7$). [§5.3]

**Open gaps:** none blocking the outcome. Four scope items, not gaps in the count:
(i) the *values* of the two new coefficients require the matching computation (out of scope
by the brief); (ii) the count is order-by-order — it says nothing about $O(g_s^6)$ and beyond
(§6.3); (iii) the outcome holds for $b'_\chi=0$ (E4); with the χ–$\Sigma_3$ mixing switched on
the invariant list is larger and the system is no longer diagonal, and the $k\ge4$ chains are
order-neutral so the dependence on $b'_\chi$ is not linear — whether that branch is still
balanced has not been run; (iv) the sextic split $c_6$ is an $O(g_s^5)$-visible input (3.3d)
that the count *pins* by convention ($c_6=0$, §6.1) rather than derives — the fitted $d_\chi$
is quoted at a stated split, and §6.2 item 7 makes the $c_6$-dependence a prediction.

**Hypotheses in force:** H-B3, H-B4, H-B5. [H1 discharged: §2.4 part 0 + Addendum N10; edited 2026-10-01, see the Annotation block at the end for the other H1 references.]

---

## 1. The counting rules

### Setup

Fields and their strand counts (A1): $\Psi$ ($s=1$, $\Ngh=2$), $\Sigma_2$ and its wrong-sign
partner $\chi$ ($s=2$, $\Ngh=4$, both in $\Sym^2\Hilb_0$), $\Sigma_3$ and a hypothetical
$\chi_3$ ($s=3$, $\Ngh=6$, in $\Sym^3\Hilb_0$). "Elementary" means: every kernel in the action
is a bare geometric vertex $V_n$ restricted to a slot partition — no composite
($V_4^{-1}$-containing) kernel such as R19's $\mathcal C$, R21's $N=\Phi^\top V_4^{-1}\Phi$ or
018's $\tilde A_{S_1},\tilde A_{S_2}$.

### Rule 1 — strand conservation

R23 gives $\Ngh(p_{k,\ell,g})$; the slice used here is the saturation rule it rests on:
the $n$-punctured sphere correlator saturates at $\sum\Ngh=2n$, which was the decisive
independent anchor of R23 ($V_4$ saturates at $8=4+4$, giving $\Ngh(m_2)=+2$). With
$\Ngh=2s$ for all fields, saturation is strand conservation:

$$ V_n(A_1,\dots,A_m)\ \text{allowed}\iff \sum_{i=1}^m s(A_i)=n. \tag{1.1} $$

### Rule 2 — coupling order

With the standard normalisation $g^{n-2}V_n/n!$ (A2), a term built on $V_n$ carries
$g^{n-2}$. Combining with (1.1), **the $g$-power of a term is fixed by its field content
alone**:

$$ \boxed{\ \text{a term with legs of strands }(s_1,\dots,s_m)\ \text{carries}\ g^{\,\sum_i s_i-2}\ } \tag{1.2} $$

Checks: $V_2(\Psi,\Psi)$, $g^0$; $V_3(\Psi^3)$, $g^1$; $V_4(\Sigma,\Sigma)$ and
$V_4(\Sigma,\Psi,\Psi)$, $g^2$; $V_5(\Sigma,\Sigma,\Psi)$, $g^3$; $V_6(\Sigma,\Sigma,\Sigma)$
and $V_6(\Sigma_3,\Sigma_2,\Psi)$ and $V_6(\Sigma_3,\Sigma_3)$, $g^4$ — the whole content of
R21/017/018 reproduced.

### Rule 3 — cubic

Terms are at most trilinear (A3). Quadratic terms (kinetic and kinetic mixing) are kept in
the enumeration: they are the ones that carry the composite-generating mechanism.

## 2. The order formula and the saddle orders

### 2.1 Saddle order

Eliminating the auxiliaries means substituting their saddle values. Write
$F_*=g^{o(F)}\,\hat F+O(g^{o(F)+1})$; $o(F)$ is the **saddle order**. A term evaluated on the
saddles therefore contributes at

$$ \boxed{\ \mathrm{ord}(\text{term})=\Big(\sum_i s_i-2\Big)+\sum_i o(F_i)\ } \tag{2.1} $$

with $o(\Psi)=0$. This is the whole counting tool: (1.2) for the vertex prefactor, plus one
unit per subleading saddle.

### 2.2 When is a saddle $O(1)$?

An auxiliary $F$ with kinetic term at order $g^{2s(F)-2}$ (its $V_{2s}$ pairing) and a source
(a term linear in $F$) at the same order has $F_*=O(1)$; if the leading source sits $p$ orders
higher, $F_*=O(g^p)$.

- $\Sigma_2$: kinetic $-\frac{g^2}{4!}V_4(\Sigma,\Sigma)$, source $\frac{2g^2}{4!}V_4(\Sigma,P)$
  at the same order $g^2$ $\Rightarrow$ $o=0$, $\Sigma_*=P=\Psi^{\otimes2}$ (Veronese).
- $\Sigma_3$ **with** its even HS pair ($-\frac{g^4}{6!}M(\Sigma_3,\Sigma_3)+\frac{2g^4}{6!}V_6(\Sigma_3,\Sigma_2,\Psi)$):
  both at $g^4$ $\Rightarrow$ $o=0$, $\Sigma_{3*}=p_3=\Psi^{\otimes3}$ (018 §1; with bare
  kernels the collapse $u(P)=Mp_3$ is the Veronese identity
  $V_6(\cdot,P,\Psi)=V_6(\cdot,\Psi^{\otimes3})$, trivially true).
- $\Sigma_3$ **without** that pair: leading source at $g^5$, kinetic at $g^4$ $\Rightarrow$
  $o=1$ — this is 018 §5(a)(iii)/(check 5), the scheme-A failure.
- $\chi$ (017): kinetic $+\frac{g^2}{4!}a_\chi V_4(\chi,\chi)$ at $g^2$, **no** $g^2$ source
  (deprived, §2.4), leading source $\frac{g^3}{5!}b_\chi V_5(\chi,\Sigma,\Psi)$ at $g^3$
  $\Rightarrow$ $o(\chi)=1$ and

  $$ \chi_*=-\frac{g\,b_\chi}{10\,a_\chi}V_4^{-1}v+O(g^2),\qquad v:=V_5(\cdot,P,\Psi). \tag{2.2} $$

  (The $1/a_\chi$ was missing in the earlier version; it is invisible at the R24 normalisation
  $a_\chi=1$ used everywhere below and in the script, but (2.2) is quoted as a general formula.)

**This is the mechanism.** A source-deprived auxiliary has a saddle that is both subleading
*and composite* ($V_4^{-1}$ inside). Fields with $o=0$ collapse to Veronese powers of $\Psi$
and can only ever produce **contacts**; fields with $o\ge1$ are the only elementary way to
produce **composites**. R24's χ is exactly a field engineered to have $o=1$.

### 2.3 The two consequences

(i) *Composite generation is bought at the price of one $g$ per χ-leg* — (2.1).
(ii) *The structure generated is read off by substituting (2.2)*: a coupling with $k$ χ-legs
produces the invariant obtained by putting $V_4^{-1}v$ in each of those slots and Veronese
values in the others.

### 2.4 H1 — source-deprivation as a frame choice

The χ scheme *stipulates* that the $g^2$ couplings $V_4(\chi,\Psi^{\otimes2})$ and
$V_4(\chi,\Sigma)$ are absent (017 §1: "χ has no $V_4(\chi,\Psi^{\otimes2})$ source"). Were
either present, (2.1) gives $o(\chi)=0$ and the scheme collapses: χ becomes a second
$\Sigma_2$ and generates no composite. No grading protects the stipulation — a charge
assignment killing $V_4(\chi,\Sigma)$ also kills the needed $V_5(\chi,\Sigma,\Psi)$ (with
$q(\chi)=1$, $V_4(\chi,\chi)$ forces $\Z_2$, then $V_5(\chi,\Sigma,\Psi)$ and $V_4(\chi,\Sigma)$
carry the same charge $1+q(\Sigma)$ and stand or fall together).

**H1 (declared).** The absence of a χ-source is a *frame choice in the $\Sym^2$ doublet*
$(\Sigma,\chi)$, not a tuning.

**Motivation, part 0 — the two stipulations are settled by one $GL(2)$, in two steps.** H1
covers two absences, $V_4(\chi,\Psi^{\otimes2})$ and $V_4(\chi,\Sigma)$, and they are *not* on
the same footing: the second is a statement about the kinetic form, the first about the
source, and the $\group{O}(1,1)$ argument below only reaches the first. The field-redefinition
group acting on the $\Sym^2$ doublet by constant linear maps is $GL(2,\R)$, 4 parameters; the
$O(g^2)$ kinetic form is $Q_{ab}\otimes V_4$ with $Q$ symmetric, 3 parameters, transforming as
$Q\to g^\top Qg$. The stabiliser of $\mathrm{diag}(-1,+1)$ is $\group{O}(1,1)$, of dimension 1,
so the orbit of a nondegenerate split-signature $Q$ has dimension $4-1=3$: it is the whole
space of such forms. Hence

> any split-signature doublet kinetic form can be brought to $\mathrm{diag}(-1,+1)\otimes V_4$
> by a constant field redefinition,

which (i) **removes the $V_4(\chi,\Sigma)$ mixing as a kinetic diagonalisation, not as an
assumption**, and (ii) shows that $a_\chi=1$ is a *normalisation* of $\chi$, not an input —
consistent with R24's $(a_\chi,b_\chi)=(1,2)$, where only the $\group{O}(1,1)$-invariant ratio
$b_\chi^2/a_\chi=4$ is physical. The residual $\group{O}(1,1)$ (1 parameter) is exactly what
the source alignment below consumes, so the parameter count is saturated: $3+1=4$. This
matters for the enumeration, not only for tidiness: a $V_4(\chi,\Sigma)$ mixing would be an
$e=0$ $\Sym^2$–$\Sym^2$ interior node (§3.1.3), marginal and order-neutral in exactly the way
$V_5(\chi,\Sigma_3)$ is, and would generate an infinite chain destroying N3′ before (E4) is
reached. The redefinition also reshuffles the higher couplings
($V_5(\Sigma,\Sigma,\Psi)$, $V_5(\chi,\Sigma,\Psi)$, $V_5(\chi,\chi,\Psi)$, …); that is
harmless, since those coefficients are free and are *defined* in this frame — $b_\chi=2$ in
particular.

*Only the second step is a hypothesis.* Diagonalising the form is a theorem (given split
signature and nondegeneracy, i.e. H-B4 and A5); what remains hypothetical in H1 is the source
alignment below, which needs the source doublet to be timelike.

**Motivation, part 1 (source alignment):** the $O(g^2)$ sector is a split-signature
quadratic form $\mathrm{diag}(-1,+a_\chi)\otimes V_4$ with a doublet-valued source
$J=(j_\Sigma,j_\chi)$, and the group preserving the form is $\group{O}(1,1)$ acting on the
doublet. At $O(g^2)$ the *only* $\Sym^2$-valued source available is $V_4(\cdot,P)$ — by
strand conservation it is the unique $\sum s=4$ term linear in an auxiliary — so
$j_\Sigma=\lambda_\Sigma V_4(\cdot,P)$ and $j_\chi=\lambda_\chi V_4(\cdot,P)$ are
**proportional to the same vector**: the doublet source is a single $\group{O}(1,1)$ vector
with components $(\lambda_\Sigma,\lambda_\chi)$, and a boost aligns it with the $\Sigma$
direction unless $\lambda_\chi^2\ge a_\chi\lambda_\Sigma^2$ [inequality corrected 2026-10-01, Addendum N10.7] — a
condition on two numbers which the $O(g_s^2)$ matching constrains to the unit hyperboloid
(Addendum (A.3)), so that the condition is forced and not chosen [rewritten 2026-10-01, Addendum
N10.2; the earlier text called the numbers "chosen" and the frame choice "under our control"]. The
frame choice is therefore always available (Addendum N10.4), which is a stronger motivation than
an appeal to genericity of $J$. 017 §3 exhibits the same $\group{O}(1,1)$ (the light-cone combinations
$\Pi_\pm=\tilde X\mp\tilde\chi$) and records that the boost is broken at $O(g^3)$ — i.e.
exactly *after* the frame has been fixed by the $O(g^2)$ data. **Falsifier / discharge:** H1
fails if the $O(g_s^5)$ matching closes only with a nonzero $V_4(\chi,\Psi^{\otimes2})$ — i.e.
if the residual after fitting $(c_\chi,d_\chi,a_7)$ is nonzero while a nonzero
$V_4(\chi,\Psi^{\otimes2})$ removes it — or if the $O(g^3)$ boost breaking regenerates a
$g^2$-order χ-source under the field redefinition that restores the frame at $O(g^3)$ (a
one-loop-in-$g$ consistency question, checkable by carrying the redefinition to $O(g^3)$ and
re-reading the $g^2$ sector). It is discharged if the $\group{O}(1,1)$ frame is shown to be
preserved order by order (an ST7-type question).

## 3. Which invariants an elementary presentation can generate

### 3.1 The order-7 basis, and the enumeration that closes it

The invariants of $\Psi$ of order 7 that appear below are $V_7(\Psi^7)$ and

$$ S_1=v^\top V_4^{-1}WV_4^{-1}v,\quad S_2=g_6^\top V_4^{-1}v,\quad S_3=\mathcal C(P,P,V_4^{-1}v), $$

with $W=V_5(\cdot,\cdot,\Psi)$, $g_6=V_6(\cdot,P,P)$, $\mathcal C=V_5V_4^{-1}V_5$. A7 says they
are *independent* (018 check 0); the count needs the strictly stronger statement that the
first three **span** what the χ-scheme presentation can generate at order 7. That statement is
established here by enumeration, not assumed. (In the first version of this record it was
asserted; the enumeration below is the fix, and it produces one substantive new condition,
(E4).)

#### 3.1.1 The objects to be enumerated

In the *collapsed* picture (saddles substituted), an on-shell term of an all-elementary
presentation is a **whole-slot tree** (§3.2): nodes are bare vertices $V_n$ with their slot
partition, internal lines are the auxiliary propagators $V_4^{-1}$ (on $\Sym^2$, a Σ- or
χ-line) or $M^{-1}$ (on $\Sym^3$, a $\Sigma_3$-line), and each external slot carries the
**leading Veronese value** of the field it holds: $\Psi$ (1 strand), $\Sigma_*=P$ (2),
$\Sigma_{3*}=p_3$ (3). Two bookkeeping conventions make the list finite and non-redundant:

- **χ is never external.** $o(\chi)=1$ means χ has no $O(1)$ value; every χ slot is the end of
  a propagator line.
- **Resummed ends.** A Σ-line whose far end is the bare source $V_4(\cdot,P)$, or a
  $\Sigma_3$-line whose far end is the bare source $u=V_6(\cdot,P,\Psi)$, is not a separate
  tree: $V_4^{-1}V_4(\cdot,P)=P$ and $M^{-1}u=p_3$ *are* the external Veronese values already
  counted. Such ends are excluded from the list of admissible tree-ends.

Each node is cubic (A3): $\ell+m\le3$ with $\ell$ internal and $m$ external slots, and
$n=\sum_{\text{slots}}(\text{strands})$.

#### 3.1.2 Degree $=7$ and order $=g^5$ are the same condition

For a tree with $k$ nodes, $L_2$ lines of type $V_4^{-1}$ and $L_3$ of type $M^{-1}$: each
line removes 2 (resp. 3) strands from each of its two endpoints, and carries $g^{-2}$
(resp. $g^{-4}$), the inverse of the $g^2V_4$ (resp. $g^4M$) kinetic form. Hence

$$ d=\sum_i n_i-4L_2-6L_3,\qquad \mathrm{ord}=\sum_i(n_i-2)-2L_2-4L_3, \tag{3.0} $$

so $d-\mathrm{ord}=2k-2(L_2+L_3)=2$ by the tree relation $k=L_2+L_3+1$. Therefore

$$ \boxed{\ d=7\iff\mathrm{ord}=5\ } $$

— the enumeration of $O(g_s^5)$ contributions and the enumeration of degree-7 whole-slot
invariants are literally the same problem. This is the structural reason the count can be run
at all.

#### 3.1.3 Assumption A8 and the node census

- **A8 (lower orders fixed).** The couplings of $\mathrm{ord}\le4$ are the ones fixed by the
  already-closed $O(g_s^{\le4})$ matching (R21, R24, 018 §1): no coupling is admitted that
  gives an auxiliary a source *earlier* than §2.2 assumes. Such a coupling changes the saddle
  order $o(F)$ and therefore re-opens a matching that is already closed; it is excluded by the
  lower order, not by this count. Excluded by A8: $V_3(\Sigma,\Psi)$ and $V_3(\chi,\Psi)$
  ($\mathrm{ord}=1,2$; they would give $o=-1$), $V_5(\Sigma_3,\Sigma_2)$ and
  $V_5(\Sigma_3,\Psi,\Psi)$ ($\mathrm{ord}=3$; $o(\Sigma_3)=-1$). $V_4(\chi,\Sigma)$ and
  $V_4(\chi,P)$ are excluded separately by H1 (§2.4).

With A8, H1 and A3, the admissible nodes are listed by their number of internal slots $\ell$
and their external strand total $e$. The only datum the enumeration needs is the **minimum
$e$** of each type.

| node type | $e$ | vertex | status |
|---|---|---|---|
| $\Sym^2$ end ($\ell=1$) | 1 | $V_3(\cdot,\Psi)$ | excluded (A8) |
| | 2 | $V_4(\cdot,P)$ | resummed (Σ) / excluded by H1 (χ) |
| | 3 | $V_5(\cdot,P,\Psi)=v$ | **admissible** (from $V_5(\Sigma,\Sigma,\Psi)$, $V_5(\chi,\Sigma,\Psi)$) |
| | 4 | $V_6(\cdot,P,P)=g_6=V_6(\cdot,p_3,\Psi)$ | **admissible** ($V_6(\Sigma^3)$, $V_6(\chi,\Sigma,\Sigma)$, $V_6(\Sigma_3,\Sigma_2,\Psi)$, $V_6(\chi,\Sigma_3,\Psi)$) |
| | 5 | $V_7(\cdot,p_3,P)$ | admissible ($V_7(\Sigma_3,\Sigma_2,\Sigma_2)$) |
| | 6 | $V_8(\cdot,p_3,p_3)$ | none: $\sum s=8\Rightarrow\mathrm{ord}\ge6$ |
| $\Sym^3$ end ($\ell=1$) | 1 | $V_4(\cdot_3,\Psi)$ | excluded (A8), $\mathrm{ord}=2$ |
| | 2 | $V_5(\cdot_3,P)$, $V_5(\cdot_3,\Sigma_2)$ | excluded (A8) |
| | 3 | $u=V_6(\cdot_3,P,\Psi)$; $M=V_6(\cdot_3,\Sigma_3)$ | resummed; kinetic form |
| | 4 | $V_7(\cdot_3,p_3,\Psi)$ | **admissible** ($V_7(\Sigma_3,\Sigma_3,\Psi)$) |
| | $\ge5$ | — | needs $V_{\ge8}$ |
| $\Sym^2$–$\Sym^2$ interior ($\ell=2$) | 0 | $V_4(\cdot,\cdot)$ | kinetic form (cancels a line) / $V_4(\chi,\Sigma)$ excluded by H1 |
| | 1 | $V_5(\cdot,\cdot,\Psi)=W$ | **admissible** |
| $\Sym^2$–$\Sym^3$ interior | 0 | $V_5(\cdot_2,\cdot_3)$ | $V_5(\Sigma,\Sigma_3)$ excluded (A8); $V_5(\chi,\Sigma_3)$ **optional**, see (E4) |
| | 1 | $V_6(\cdot_2,\cdot_3,\Psi)$ | admissible |
| $\Sym^3$–$\Sym^3$ interior | 0 | $M$ | kinetic form |
| | 1 | $V_7(\cdot_3,\cdot_3,\Psi)$ | admissible |
| centre ($\ell=3$) | 0 | $V_6(\Sigma,\Sigma,\Sigma)$, … | admissible |

**Minima to be used:** $\Sym^2$ end $e\ge3$; $\Sym^3$ end $e\ge4$; interior $e\ge1$ except the
optional $V_5(\chi,\Sigma_3)$ ($e=0$); centre $e\ge0$.

#### 3.1.4 The enumeration ($\sum_i e_i=7$)

**No branching.** A node with $\ell=3$ makes the tree have at least three leaves; each leaf has
$e\ge3$, so $\sum e\ge9>7$. Hence **every tree is a path**, with exactly two ends.

**$k=1$.** A single $V_7$ with $\le3$ slots of $\le3$ strands summing to 7: the partitions
$(3,3,1)$ and $(3,2,2)$. Both evaluate to $V_7(\Psi^7)$. → **$V_7(\Psi^7)$**, one direction.

**$k=2$** (one line, two ends).
*(a) $\Sym^2$ line:* $e_1+e_2=7$ with both $\ge3$, so $\{3,4\}$ is the only split:
$v^\top V_4^{-1}g_6$. → **$S_2$**. (The split $\{5,2\}$ would need an $e=2$ end, which is
resummed or excluded.)
*(b) $\Sym^3$ line:* both ends $\ge4$, so $\sum e\ge8>7$. **None.** This is the derivation of
the second half of N4: *no $M^{-1}$ composite exists at $O(g_s^5)$*, previously asserted.

**$k=3$** (a path $A$–$B$–$C$).
*(a) $L_2=2$:* $e_A,e_C\ge3$, $e_B\ge1$; the minimum $3+1+3=7$ is attained, and uniquely:
ends $=v$, interior $=W$. → **$S_1$**, and nothing else with three nodes.
*(b) $L_2=L_3=1$:* $\Sym^2$ end $\ge3$, $\Sym^3$ end $\ge4$, mixed interior $\ge1$ unless it is
the optional $V_5(\chi,\Sigma_3)$. With $e_B\ge1$: $\ge8$, none. With $e_B=0$: $3+0+4=7$,
attained — see (E4).
*(c) $L_3=2$:* two $\Sym^3$ ends, $\ge8$. None.

*One tree, several couplings.* The enumeration counts *trees*, i.e. directions; each tree is
realised by more than one coupling of the action — the $k=2$ tree by a Σ-line
($V_6(\Sigma,\Sigma,\Sigma)$ against the $\Sigma$ source) and by a χ-line
($V_6(\chi,\Sigma,\Sigma)$), the $k=3$ tree by row 1 and row 3 of §3.3. This is harmless for a
direction count and is why §4.2 has to be read alongside §3.1; a reader checking *coefficients*
must collect all realisations of a tree, as §3.3 does.

**$k\ge4$.** Paths only, two ends with $e\ge3$ each and $k-2\ge2$ interiors. If no interior has
$e=0$, $\sum e\ge3+3+(k-2)\ge8$. The only $e=0$ interior available is the optional
$V_5(\chi,\Sigma_3)$; with it, the chains of (E4) below. Without it: **none**.

#### 3.1.5 Result of the enumeration (replaces the assertion; N3′)

> **Spanning lemma.** With the χ-scheme field content, A3, A8, H1 and the resummation
> convention of §3.1.1, the complete list of order-7 whole-slot tree invariants generated by
> an all-elementary presentation is
> $$\{\,V_7(\Psi^7),\ S_1,\ S_2\,\}, \tag{3.0'}$$
> **provided the optional coupling $V_5(\chi,\Sigma_3)$ is set to zero.** No fourth invariant
> exists, and in particular no invariant containing $M^{-1}$.

$S_3$ is absent for the reason of §3.2 (it is not a whole-slot contraction at all, so it never
enters the enumeration); the lemma now also excludes any *whole-slot* fourth invariant, which
§3.2 alone did not.

**(E4) The one escape, and why it is a condition and not a gap.** $V_5(\chi,\Sigma_3)$ has
$\sum s=5$ and one χ-leg, hence $\mathrm{ord}=3+1=4$: it is admissible at $O(g_s^4)$ and A8
does **not** exclude it. It is invisible there, because $V_5(\cdot,p_3)=V_5(\cdot,\Psi^{\otimes3})=v$
makes its $O(g_s^4)$ contribution proportional to $v^\top V_4^{-1}v$ — a mere reparametrisation
of $b_\chi$. At $O(g_s^5)$ it is not invisible: it is a χ–$\Sigma_3$ kinetic **mixing that is
marginal in $g$** (a $g^3$ mixing between a $g^2$ and a $g^4$ kinetic term:
$g^3=\sqrt{g^2g^4}$), so the $(\chi,\Sigma_3)$ mass matrix ceases to be block-diagonal at
leading order. Concretely the $k=3$ tree (b) above gives a fourth invariant

$$ S_4=V_7\big(M^{-1}V_5(V_4^{-1}v,\cdot),\,p_3,\,\Psi\big), \tag{3.2} $$

and the $k\ge4$ chains alternating $V_4^{-1}$ and $M^{-1}$ through further
$V_5(\chi,\Sigma_3)$ insertions are the geometric series of that mixing — each added pair costs
$\sum(n-2)=6$ and returns $2+4=6$, i.e. is exactly order-neutral, which is the same statement
that the mixing is marginal. The series resums into the inverse of the full $2\times2$ block
kinetic form; the invariant content stays finite but is no longer $(3.0')$.

Consequence for the outcome: **$b'_\chi=0$ (no $V_5(\chi,\Sigma_3)$) is an explicit condition
of the count**, added to the action of §6.1 and to the tests of §6.2. It is a legitimate
choice, not a tuning, for two reasons, the second stronger than the first:

1. *Costless.* Nothing at $O(g_s^{\le4})$ forces $b'_\chi\ne0$ — it is redundant there — so
   setting it to zero costs no matching freedom.
2. *Frame-independent.* $V_5(\Sigma_3,\cdot)$ is a **doublet-valued** coupling with components
   $(b_\Sigma,b'_\chi)$ on $(\Sigma,\chi)$, and A8 already forces $b_\Sigma=0$
   ($V_5(\Sigma_3,\Sigma_2)$ has $\mathrm{ord}=3$, i.e. $o(\Sigma_3)=-1$). Adding $b'_\chi=0$
   makes the *whole covector* vanish, and a vanishing covector is invariant under the doublet
   $GL(2)$ of §2.4. So (E4) is a frame-independent statement, unlike H1's $j_\chi=0$.
   Conversely, $b'_\chi\ne0$ together with $b_\Sigma=0$ is *not* $GL(2)$-stable: a boost
   regenerates $b_\Sigma\ne0$, which A8 forbids — and the $GL(2)$ is already entirely spent
   fixing the frame of §2.4, so keeping $b_\Sigma=0$ there would be a second tuning in a frame
   chosen for another purpose. Strand conservation forbids any other linear redefinition
   reaching $\Sigma_3$ from a $\Sym^2$ field, and eliminating auxiliaries creates no new action
   couplings, so nothing regenerates $b'_\chi$.

What switching it on would change is **not** quantified here. The $k\ge4$ chains above are
order- and degree-neutral, so $b'_\chi\ne0$ produces an infinite family of degree-7 trees that
resums into the inverse of the full $2\times2$ block kinetic form: the dependence on $b'_\chi$
is not linear, and the linear freedom count of §5 does not apply to that branch at all. It
destroys the diagonality of (5.1) and makes the $\Sigma_3$ propagator visible at $O(g_s^5)$.
Whether that branch is still balanced has not been run — see open gap (iii). The outcome
**enough freedom** is therefore stated for $b'_\chi=0$.

### 3.2 Strand-locality lemma (N3)

**Claim.** In an all-elementary presentation, every term of the on-shell action is a *whole-slot
tree contraction*: a tree whose nodes are bare $V_n$'s, whose internal lines are the
auxiliary propagators $V_4^{-1}$ (on $\Sym^2$) or $M^{-1}$ (on $\Sym^3$), and whose external
lines are single $\Psi$ strands.

**Proof.** Each vertex of the action takes its arguments as *whole fields* in slots; the
only single-strand argument available is $\Psi$. Gaussian elimination of an auxiliary $F$
replaces a pair of $F$-slots by $(\text{kinetic form on }\Sym^{s(F)})^{-1}$, which is an
operator on the whole $\Sym^{s(F)}$ space, hence joins one complete slot to one complete
slot. No step ever routes the strands of a single slot into two different vertex blocks. $\square$

**Corollary.** $S_3$ is not generated. $\mathcal C(A,B,C)$ requires the two strands of one
$\Sym^2$ argument to sit in *different* $V_5$ blocks
($\mathcal C\sim V_5(A,X,b_1)V_4^{-1}(X,Y)V_5(Y,C,b_2)$ with $b_1,b_2$ the strands of $B$) —
a strand-split contraction, which by the lemma is outside the image of any elementary
presentation. Its appearance in the minimal scheme's $A_5^{\min}$ (013) is traced to the
*composite* vertex $W_6=V_6-\frac65\mathcal C$ of R19, not to any elementary structure.

*Relation to R28′.* This is a different, weaker statement than the R28′ degree argument: it
is a statement about which contractions a Feynman expansion can produce, at the algebraic
layer, not about the worldsheet realisability of a kernel.

### 3.3 The $O(g_s^5)$ deficit is two-dimensional (N4)

Apply §2 to the χ scheme at $O(g_s^5)$. Notation for the expansions around the leading
saddles: $\Sigma_*=P+X$ with $X=O(g)$, $\Sigma_{3*}=p_3+Y$ with $Y=O(g)$, $\chi_*=O(g)$, and

$$ W=V_5(\cdot,\cdot,\Psi),\quad v=V_5(\cdot,P,\Psi),\quad g_6=V_6(\cdot,P,P),\quad
   L=V_6(\cdot,\cdot,\Psi):\Sym^2\to\Sym^3,\quad u=V_6(\cdot,P,\Psi). $$

Each row below is written out; the $1/n!$ prefactors are carried symbolically (they fix
$\alpha,\beta$, which are out of scope, not the invariant produced).

**Row 1 — running of the $\Sigma_2$ kernel.** Completing the square in the $g^2$ sector,
$-\frac{g^2}{4!}V_4(\Sigma,\Sigma)+\frac{2g^2}{4!}V_4(\Sigma,P)
=\frac{g^2}{4!}V_4(P,P)-\frac{g^2}{4!}V_4(X,X)$, while
$\frac{g^3}{5!}V_5(\Sigma,\Sigma,\Psi)=\frac{g^3}{5!}\big[V_5(\Psi^5)+2\langle v,X\rangle+W(X,X)\big]$.
So $X$ has kernel $K_\Psi=-\frac{g^2}{12}V_4+\frac{g^3}{60}W$ and source $\frac{2g^3}{5!}v$;
its exchange is $\propto g^6\,v^\top K_\Psi^{-1}v$ with
$K_\Psi^{-1}\propto g^{-2}\big(V_4^{-1}+\tfrac g5V_4^{-1}WV_4^{-1}+O(g^2)\big)$. Leading term
$g^4\,v^\top V_4^{-1}v$ (the R17 feedback, already matched at $O(g_s^4)$); first correction
$g^5\,v^\top V_4^{-1}WV_4^{-1}v=g^5S_1$. The $W(X,X)$ term of the expansion is the same
$S_1$ with $X\to$ its leading value $\propto gV_4^{-1}v$, i.e. the same $k=3$ tree of §3.1.4
counted once. → **$S_1$.**

**Row 2 — the $V_6(\Sigma,\Sigma,\Sigma)$ tadpole for $X$.**
$\frac{g^4c_6}{6!}V_6(P+X,P+X,P+X)=\frac{g^4c_6}{6!}\big[V_6(\Psi^6)+3\langle g_6,X\rangle+O(X^2)\big]$;
the $X$-linear piece is an $O(g^4)$ addition to the $X$-source, namely

$$ \delta J^{(2)}=\frac{3g^4c_6}{6!}\,g_6=\frac{g^4c_6}{240}\,g_6, \tag{3.3a} $$

and its cross term with the $O(g^3)$ source $\frac{2g^3}{5!}v=\frac{g^3}{60}v$ through
$K_\Psi^{-1}\propto g^{-2}V_4^{-1}$ gives $g^{3+4-2}\,g_6^\top V_4^{-1}v=g^5S_2$. → **$S_2$.**

**Row 3 — subleading χ source.** The χ source is
$j_\chi=\frac{g^3b_\chi}{5!}V_5(\cdot,\Sigma_*,\Psi)=\frac{g^3b_\chi}{5!}\big(v+WX+O(g^2)\big)$
and the χ kinetic form is $\frac{g^2a_\chi}{12}V_4$, so the χ-exchange is
$\propto g^{6-2}a_\chi^{-1}b_\chi^2\,(v+WX)^\top V_4^{-1}(v+WX)$: leading
$g^4\,v^\top V_4^{-1}v$ (017's mechanism, which is what fixes $b_\chi^2/a_\chi=4$), cross term
$2g^4\,v^\top V_4^{-1}WX$ with $X\propto gV_4^{-1}v$, i.e. $g^5S_1$. → **$S_1$.**
(The second-order χ saddle $\chi^{(2)}\propto V_4^{-1}WV_4^{-1}v$ contracted against $v$ is
the same term, reorganised.)

**Row 4 — the $\Sigma_3$ cross term.** With the even HS pair
$\frac{g^4c_{\Sigma_3}}{6!}\big[-M(\Sigma_3,\Sigma_3)+2V_6(\Sigma_3,\Sigma_2,\Psi)\big]$ the
$\Sigma_3$ source is $\frac{2g^4c_{\Sigma_3}}{6!}V_6(\cdot,\Sigma_*,\Psi)=\frac{2g^4c_{\Sigma_3}}{6!}(u+LX)$
and the exchange is $\propto g^{8-4}(u+LX)^\top M^{-1}(u+LX)$. Three pieces:

- $u^\top M^{-1}u$: the Veronese collapse $u=Mp_3$ gives $\langle u,p_3\rangle=V_6(\Psi^6)$ —
  the $O(g_s^4)$ sextic contact, **no $M^{-1}$ left**;
- $2u^\top M^{-1}LX=2\langle p_3,LX\rangle=2V_6(X,p_3,\Psi)=2V_6(X,\Psi^{\otimes4})=2\langle g_6,X\rangle$,
  again **no $M^{-1}$**, and with $X\propto gV_4^{-1}v$ this is $g^5S_2$; carrying the prefactor,
  the saddle value of the $\Sigma_3$ sector is $\frac{g^4c_{\Sigma_3}}{6!}(u+LX)^\top M^{-1}(u+LX)$,
  so this piece adds to the $X$-source

  $$ \delta J^{(4)}=\frac{2g^4c_{\Sigma_3}}{6!}\,g_6=\frac{g^4c_{\Sigma_3}}{360}\,g_6; \tag{3.3b} $$
- $X^\top L^\top M^{-1}LX=O(g^2)$ relative to the first, i.e. $O(g_s^6)$ — the first place the
  $\Sigma_3$ propagator survives.

→ **$S_2$**, and the derivation of N4's second clause (no $M^{-1}$ composite at $O(g_s^5)$),
matching 018 §2's scope note that $A_5^{\rm dr}$ is $\tilde M^{-1}$-independent.

**The $S_2$ component moves with the free sextic split.** Rows 2 and 4 are the *only* two
sources of $S_2$, and they are weighted by the two halves of the $O(g_s^4)$ sextic contact
split $c_6+c_{\Sigma_3}=1$, which §5.2 leaves free. Adding (3.3a) and (3.3b),

$$ \delta J=\Big(\frac{c_6}{240}+\frac{c_{\Sigma_3}}{360}\Big)g^4g_6
   =\frac{3c_6+2c_{\Sigma_3}}{720}\,g^4g_6=\frac{2+c_6}{720}\,g^4g_6. \tag{3.3c} $$

With $K_\Psi=-\frac{g^2}{12}V_4+O(g^3)$ the $X$-exchange is $-\frac12J^\top K_\Psi^{-1}J
=\frac{6}{g^2}J^\top V_4^{-1}J$, and the cross term of $\frac{g^3}{60}v$ with (3.3c) is

$$ \frac{12}{g^2}\cdot\frac{g^3}{60}\cdot\frac{(2+c_6)g^4}{720}\;g_6^\top V_4^{-1}v
   =\frac{2+c_6}{3600}\,g^5S_2. \tag{3.3d} $$

So the $S_2$ coefficient of (3.1) is $\beta=\frac{7!(2+c_6)}{3600}=\frac{7(2+c_6)}{5}$ — it
varies by 50 % over the allowed range $c_6\in[0,1]$ ($14/5$ at $c_6=0$, $21/5$ at $c_6=1$),
while $\alpha$ (rows 1 and 3) does not depend on the split at all. **The split is therefore an
$O(g_s^5)$-visible input**, and a matching run that does not pin it returns a $d_\chi$ that
depends on an unstated number. It is pinned in §6.1 and scanned in §6.2.

*Remark (suggestive, not a derivation).* $\beta(c_6{=}0)=14/5$ coincides numerically with the
$|-14/5|$ that 018 §3 reports as the $\tilde A_{S_2}$ component of the dressed-scheme deficit.
The two live in different generator bases with their own normalisations, so this is not a
check; it is a cheap consistency test for the matching to run once $\beta$ is computed.

**No fifth source.** This is now a corollary of §3.1.5 rather than an assertion: the four rows
are the four ways of assembling the *only* non-contact whole-slot trees of degree 7 that
exist, $S_1$ ($k=3$) and $S_2$ ($k=2$), out of the admissible node list, and the spanning
lemma says there is no other degree-7 whole-slot invariant at all (in particular none with
$M^{-1}$, which the $k=2$/(b) and $k=3$/(c) cases of §3.1.4 exclude independently of the
collapse arguments above). By §3.2 no $S_3$. The condition $b'_\chi=0$ of (E4) is in force.

*A6 in the enlarged setting.* The naive-contact rule was derived in 018 §3 for the dressed
kernels with content $(\Psi,\Sigma_2,\Sigma_3)$ and no χ. Re-examined here: the only new
$\Sigma_3$ source in the χ scheme is $d'_\chi V_6(\chi,\Sigma_3,\Psi)$, whose contribution to
$\hat s$ is removed by the same collapse $M^{-1}u=p_3$ (row 4), leaving
$V_6(\chi_*,p_3,\Psi)=S_2$; the $1/7!$ restoration of A6 is therefore unchanged. A6 is used,
not transferred silently.

*The matching target is scheme-independent.* 018 §3's coefficients
$(1,\frac{42}{25},-\frac{14}{5})$ are the components of the deficit on the *dressed-scheme*
generator basis $\{V_7|_{331},\tilde A_{S_1},\tilde A_{S_2}\}$, not the target; the target is
$V_7(\Psi^7)$ in both schemes, and $A_5^{\rm dr}$ is itself strand-local (018 §2, "no $S_3$").
$S_3$ appears only in the *minimal* presentation's $A_5^{\min}$ (013), through R19's composite
$W_6$. So the χ scheme is never required to produce $S_3$. Hence

$$ 7!\,A_5^{\chi}=\alpha\,S_1+\beta(c_6)\,S_2,\qquad \text{deficit to close}=V_7(\Psi^7)-7!A_5^\chi
   \in\mathrm{span}\{V_7(\Psi^7),S_1,S_2\}, \tag{3.1} $$

with $\beta(c_6)=\frac{7(2+c_6)}{5}$ by (3.3d).

**Three directions to hit.**

## 4. The $O(g_s^5)$ menu

### 4.1 $\Sigma_3$ is forced (N5)

By (2.1), a term contributes a *contact* ($\Psi^7$, no propagator) at $O(g_s^5)$ only if all
legs have $o=0$ and $\sum s_i=7$. On the 017 content $(\Psi,\Sigma_2,\chi)$ the available
$o=0$ strands are $1$ and $2$, so a cubic term reaches at most $2+2+2=6<7$: **the χ scheme
cannot produce the $V_7(\Psi^7)$ contact without a three-strand field with an $O(1)$ saddle.**
By §2.2 that field must carry its even HS pair at $O(g_s^4)$. So 018 §5(a)'s conclusion
transfers verbatim: the χ scheme does **not** avoid the $\Sigma_k$ tower; it avoids only the
*dressing of the vertices*. The tower $\Sigma_n$ for $V_{2n}$ and $V_{2n+1}$ is
forced in the χ scheme too.

### 4.2 The complete $O(g_s^5)$ generator list

Solve $\big(\sum s_i-2\big)+\sum o_i=5$ over $\{\Psi(1,0),\Sigma_2(2,0),\Sigma_3(3,0),
\chi(2,1),\chi_3(3,o_3)\}$, at most trilinear.

**(a) $\sum o=0$, $\sum s=7$.** Partitions of 7 into $\le3$ parts of size $\le3$:
$(3,3,1)$ and $(3,2,2)$ — i.e. $V_7(\Sigma_3,\Sigma_3,\Psi)$ and $V_7(\Sigma_3,\Sigma_2,\Sigma_2)$.
On the saddles both give $V_7(p_3,p_3,\Psi)=V_7(P,P,\Psi^{\otimes3})=V_7(\Psi^7)$: **one
direction, the partition split is presentation freedom** (018 §5(c) recovered by counting).

**(b) $\sum o=1$, $\sum s=6$, one χ-leg.** Remaining two legs sum to 4:
$V_6(\chi,\Sigma_2,\Sigma_2)$ and $V_6(\chi,\Sigma_3,\Psi)$. On the saddles,
$V_6(V_4^{-1}v,P,P)$ and $V_6(V_4^{-1}v,p_3,\Psi)$ — the same invariant $S_2$, because the
four non-χ strands are all $\Psi$ in both cases. **One direction, $S_2$; again a free
partition.**

**(c) $\sum o=2$, $\sum s=5$, two χ-legs.** Only $(2,2,1)$: $V_5(\chi,\chi,\Psi)$. On the
saddles $W(V_4^{-1}v,V_4^{-1}v)=v^\top V_4^{-1}WV_4^{-1}v=S_1$. **One direction, $S_1$.**
(The quadratic $V_5(\chi_3,\chi)$ also has $\sum s=5$; see 4.3.)

**(d) already fixed at $O(g_s^4)$ and below:** $V_4(\chi,\chi)$ ($\mathrm{ord}=2+2=4$, value
$v^\top V_4^{-1}v$ — the 017 mechanism), $V_5(\chi,\Sigma,\Psi)$ ($\mathrm{ord}=3+1=4$, the
χ source), $V_6(\Sigma,\Sigma,\Sigma)$, the $\Sigma_3$ pair.

**(d′) admissible at $O(g_s^4)$ but set to zero by (E4):** $V_5(\chi,\Sigma_3)$
($\mathrm{ord}=3+1=4$). At $O(g_s^4)$ it is a redundant reparametrisation of $b_\chi$, because
$V_5(\cdot,p_3)=V_5(\cdot,\Psi^{\otimes3})=v$; at $O(g_s^5)$ it is a marginal χ–$\Sigma_3$
kinetic mixing that adds the invariant $S_4$ of (3.2) and destroys the diagonality of §5.1.
Since nothing at lower order forces it, the count sets $b'_\chi=0$ and says so.

**(e) excluded by §2.4/H1:** $V_4(\chi,\Psi^{\otimes2})$, $V_4(\chi,\Sigma)$ ($\mathrm{ord}=3$,
and they destroy $o(\chi)=1$). Note that strand conservation (Rule 1) does *not* exclude
them: χ has the same menu as $\Sigma$ (note under A1), so these exclusions rest on H1 alone.

**(f) higher:** $V_6(\chi,\chi,\Sigma)$ ($\mathrm{ord}=6$), $V_6(\chi,\chi,\chi)$ ($7$),
$V_7(\chi,\dots)$ ($\ge6$), $V_7(\chi_3,\Sigma_3,\Psi)$ ($6$).

### 4.3 One χ suffices at $O(g_s^5)$ (N8)

Every $\chi_3$ option fails to reach $O(g_s^5)$ usefully. The core argument is a
**self-consistency** one, not a case split: the first two bullets below are premise and
conclusion, and the third is a separate exclusion of the one coupling neither bullet covers.

- *Premise.* Suppose $\chi_3$ is source-deprived, $o(\chi_3)=1$. Then any coupling of
  $\mathrm{ord}\le5$ containing $\chi_3$ has $\sum s\le5-1+2=6$ and is therefore linear in
  $\chi_3$ with at most $6-3=3$ further strands — i.e. it *is* a $g^{\le4}$ source for
  $\chi_3$ (e.g. $V_6(\chi_3,\Sigma_2,\Psi)$, $\sum s=6$, $\mathrm{ord}=5$, sources $\chi_3$ at
  $g^4$ against its $g^4$ kinetic term). Such a coupling contradicts $o(\chi_3)=1$. Hence
  under $o(\chi_3)=1$ every admissible $\chi_3$ coupling has $\mathrm{ord}\ge6$ (the cheapest
  being $V_7(\chi_3,\cdot,\cdot)$), and $\chi_3$ is irrelevant at $O(g_s^5)$.
- *The alternative.* $\chi_3$ given the $O(g_s^4)$ source $V_6(\chi_3,\Sigma_2,\Psi)$: then $o(\chi_3)=0$ and
  $\chi_3$ is a second $\Sigma_3$ with the opposite kinetic sign — it only re-splits the
  sextic contact and re-weights $\alpha,\beta$; no new direction.
- the mixing $V_5(\chi_3,\chi)$ ($\mathrm{ord}=3+o(\chi_3)+1$): it sources $\chi_3$ at $g^4$
  against a $g^4$ kinetic, so $\chi_{3*}=O(1)$ but composite, $\chi_{3*}\sim M^{-1}V_5(\cdot,V_4^{-1}v)$,
  and its exchange contributes an $M^{-1}$-composite **at $O(g_s^4)$** — a structure absent
  from the $O(g_s^4)$ deficit. It must be set to zero. (Same conclusion as (e): the coupling
  is excluded by the lower order, not by $O(g_s^5)$.)

So the wrong-sign tower does **not** have to mirror the $\Sigma$-tower at this order — 017
§5(b)'s question answered for $O(g_s^5)$, undecided beyond (§6.3).

## 5. The closure count

### 5.1 The system

Three directions to hit, three independent generators:

| direction | generator | free coefficient | leading coefficient of the generator |
|---|---|---|---|
| $V_7(\Psi^7)$ | $\frac{g^5}{7!}[a_7V_7(\Sigma_3,\Sigma_3,\Psi)+b_7V_7(\Sigma_3,\Sigma_2,\Sigma_2)]$ | $a_7+b_7$ | $1$ |
| $S_1$ | $\frac{g^3}{5!}c_\chi V_5(\chi,\chi,\Psi)$ | $c_\chi$ | $\propto c_\chi b_\chi^2$ |
| $S_2$ | $\frac{g^4}{6!}[d_\chi V_6(\chi,\Sigma,\Sigma)+d'_\chi V_6(\chi,\Sigma_3,\Psi)]$ | $d_\chi+d'_\chi$ | $\propto b_\chi(d_\chi+d'_\chi)$ |

By §4.2 the map (coefficients) $\to$ (invariants) is **diagonal** at $O(g_s^5)$: the $V_7$
couplings produce no composite, $V_5(\chi,\chi,\Psi)$ produces only $S_1$,
$V_6(\chi,\Sigma,\cdot)$ only $S_2$. With $b_\chi=2\ne0$ the system is nonsingular, so the
matching conditions

$$ a_7+b_7=1,\qquad c_\chi=\frac{\alpha}{\kappa_1b_\chi^2},\qquad
   d_\chi+d'_\chi=\frac{\beta(c_6)}{\kappa_2b_\chi},\qquad \beta(c_6)=\frac{7(2+c_6)}{5}
   \tag{5.1} $$

($\kappa_{1,2}$ pure numbers from the $1/n!$ bookkeeping) have a **unique solution given the
sextic split $c_6$** — not a unique solution outright. By (3.3d) the right-hand side of the
third equation is affine in $c_6$, so (5.1) carries a *one-parameter family* of presentations
labelled by $c_6\in[0,1]$, along which $d_\chi+d'_\chi$ varies by 50 %. Together with the
usual Veronese-diagonal-null presentation freedom (013 §3(c)) and the two free partition
splits $(a_7:b_7)$, $(d_\chi:d'_\chi)$, this is the complete solution set. The *rank*
statement — three independent generators for three directions — is untouched by the split:
$c_6$ moves the target, not the generator matrix. §6.1 pins $c_6=0$ so that the matching has
no unstated input.

### 5.2 Non-disturbance of $b_\chi^2/a_\chi=4$ (N7)

- $V_5(\chi,\chi,\Psi)$ and $V_6(\chi,\Sigma,\cdot)$ have $\mathrm{ord}=5$: they cannot touch
  $O(g_s^4)$. Equivalently: the first modifies the χ kinetic to
  $K_\chi=a_\chi V_4+\frac{g}{5}c_\chi W$ and the second the χ source by a $g^4$ piece; both
  corrections enter the χ-exchange $j^\top K_\chi^{-1}j$ one order below the leading
  $O(g^4)$ term $-\frac{b_\chi^2}{4a_\chi}\frac{g^4}{600}v^\top V_4^{-1}v$. The ratio
  $b_\chi^2/a_\chi=4$ is fixed by that leading term alone. **Undisturbed.**
- The $\Sigma_3$ HS pair does act at $O(g_s^4)$, but only through its **contact**
  $M(p_3,p_3)=V_6(\Psi^6)$: the collapse $u(P)=Mp_3$ removes $M^{-1}$, and the linear-in-$X$
  term is $O(g^5)$. So the only $O(g_s^4)$ change is the sextic contact split,
  $c_6+c_{\Sigma_3}=1$ in place of $c_6=1$ — the R20/018 $c_6$ freedom, not the χ ratio.
  **One order up the split is no longer free in its effect:** by (3.3c)–(3.3d) it weights the
  two $S_2$ sources differently and moves $\beta$, hence the fitted $d_\chi$ (§5.1). It is a
  presentation freedom at $O(g_s^4)$ and an input at $O(g_s^5)$.

### 5.3 Falsifier: does the count reproduce what is known? (N9)

The brief's test: a count that would have predicted failure at $O(g_s^4)$ is wrong.

1. **R20 (no-go, content $\Sigma_2\oplus\Sigma_3$, $O(g_s^4)$).** Deficit at $O(g_s^4)$:
   $\{V_6(\Psi^6),\,v^\top V_4^{-1}v\}$, rank 2. Generators with $\mathrm{ord}=4$ on content
   with all $o=0$: $\sum s=6$, i.e. $(2,2,2)$, $(3,2,1)$, $(3,3)$ — every one of them
   collapses to the Veronese contact $V_6(\Psi^6)$, rank 1. $1<2$ $\Rightarrow$ **no closure.**
   R20 re-derived in two lines.
2. **R24 (closure with χ, $O(g_s^4)$).** Adding χ with $o=1$ gives, at $\mathrm{ord}=4$, the
   pair $V_4(\chi,\chi)$ + $V_5(\chi,\Sigma,\Psi)$ whose joint on-shell value is
   $\propto v^\top V_4^{-1}v$ — the missing second direction. Rank 2 = rank 2
   $\Rightarrow$ **closure, with one condition on the invariant combination**, which is the
   forced ratio $b_\chi^2/a_\chi=4$ (only the $\group{O}(1,1)$-invariant ratio is fixed,
   matching 017's $\lambda$-twist remark). **The count predicts 017, it does not predict its
   failure.**
3. **018 §5(a), scheme A at $n=7$.** Without the $\Sigma_3$ pair, $o(\Sigma_3)=1$, so (2.1)
   gives $\mathrm{ord}=5+1+1=7$ for the $(3,3,1)$ coupling and $\mathrm{ord}=5+1=6$ for
   $(3,2,2)$: no $V_7$ contact at $O(g_s^5)$ for any kernel. 018 §5(a)(iii) quotes $O(g^6)$,
   which is the $(3,2,2)$ branch — the cheaper of the two — and 018's check-5 log-slope
   $5.98$ measures exactly that branch. The two records agree; read quickly they look
   inconsistent only because 018 quotes the minimum and 038 the $(3,3,1)$ case.
   **Reproduced.**
4. **R19/R21.** The dressed presentations sit outside the lemma of §3.2 (their kernels are
   composite), which is why they can hit $v^\top V_4^{-1}v$ with $o=0$ fields only — the
   count says the two routes to a composite are "dress the vertex" or "deprive a field of its
   source", and R19/R21 take the first, R24 the second.

## 6. Outcome and spec for the matching

### 6.1 Outcome: **enough freedom** (conditional on H-B3, H-B4, H-B5, H1, and $b'_\chi=0$)

With content $(\Psi,\Sigma_2,\chi,\Sigma_3)$, elementary vertices only, and the condition
$b'_\chi=0$ of (E4), the $O(g_s^5)$ matching is a nonsingular $3\times3$ (in fact diagonal)
system — **conditional on H-B3 (genericity of the feedback invariant at the actual vertices),
H-B4 (χ is a harmless non-propagating auxiliary), H-B5 (the χ tower stays elementary) and H1
(source-deprivation is a frame choice)**. Minimal action to be matched:

$$
\begin{aligned}
S^\chi_5=\;&\tfrac12V_2(\Psi^2)+\tfrac{g}{3!}V_3(\Psi^3)
  -\tfrac{g^2}{4!}V_4(\Sigma,\Sigma)+\tfrac{2g^2}{4!}V_4(\Sigma,P)
  +\tfrac{g^3}{5!}V_5(\Sigma,\Sigma,\Psi)\\
 &+\tfrac{g^2}{4!}a_\chi V_4(\chi,\chi)+\tfrac{g^3}{5!}b_\chi V_5(\chi,\Sigma,\Psi)
  +\tfrac{g^3}{5!}\,\mathbf{c_\chi}\,V_5(\chi,\chi,\Psi)\\
 &+\tfrac{g^4}{6!}c_6V_6(\Sigma,\Sigma,\Sigma)
  +\tfrac{g^4}{6!}\big[-c_{\Sigma_3}V_6(\Sigma_3,\Sigma_3)+2c_{\Sigma_3}V_6(\Sigma_3,\Sigma_2,\Psi)\big]
  +\tfrac{g^4}{6!}\,\mathbf{d_\chi}\,V_6(\chi,\Sigma,\Sigma)\\
 &+\tfrac{g^5}{7!}\,\mathbf{a_7}\,V_7(\Sigma_3,\Sigma_3,\Psi),
\end{aligned}
$$

with $(a_\chi,b_\chi)=(1,2)$ from R24, $c_6+c_{\Sigma_3}=1$ from the sextic contact, and the
three bold coefficients fixed by (5.1). The coupling $V_5(\chi,\Sigma_3)$ is **absent by the
condition (E4)**, not by omission.

***The sextic split is pinned: $c_6=0$, $c_{\Sigma_3}=1$.*** By (3.3d) the split is visible at
$O(g_s^5)$, so it cannot be left with only its sum fixed. Two reasons for this choice, both
internal to the record rather than a matter of taste:

- the $\Sigma_3$ HS pair is **forced** at $O(g_s^4)$ by N5 (§4.1), whereas
  $V_6(\Sigma,\Sigma,\Sigma)$ is not forced by anything; the minimal action carries the forced
  term and drops the optional one;
- with $c_6=0$ the action above is **at most quadratic in $\Sigma_2$** (the remaining
  $\Sigma$-dependence is $V_4(\Sigma,\Sigma)$, $V_4(\Sigma,P)$, $V_5(\Sigma,\Sigma,\Psi)$,
  $b_\chi V_5(\chi,\Sigma,\Psi)$, $c_{\Sigma_3}V_6(\Sigma_3,\Sigma_2,\Psi)$ and
  $d_\chi V_6(\chi,\Sigma,\Sigma)$, all of degree $\le2$), so the $\Sigma_2$ elimination stays
  an exact Gaussian at fixed $(\chi,\Sigma_3)$ — a concrete implementation gain against
  $c_6\ne0$, which makes it cubic. (It does not restore the *sequential* Gaussianity lost to
  $V_6(\chi,\Sigma,\Sigma)$: the Σ kernel then depends on χ, see §6.2.)

The choice is a presentation convention, not a physical input: §6.2 item 7 asks the matching
to scan $c_6$ and check the predicted affine law $\beta(c_6)=\frac{7(2+c_6)}{5}$, which turns
the pinning into a falsifiable prediction rather than a hidden assumption.

*Optional presentation partners* (same invariants at this order):
$V_7(\Sigma_3,\Sigma_2,\Sigma_2)$ for $a_7$, $V_6(\chi,\Sigma_3,\Psi)$ for $d_\chi$. Caveat
carried over from 018 §5: the $(3,2,2)$ partner $V_7(\Sigma_3,\Sigma_2,\Sigma_2)$ is
*equivalent only at $O(g_s^5)$* — 018 gives two reasons not to take it, namely that its
$S_1,S_2$ realisations require $\mathcal C$-style strand-splitting of a $\Sigma_2$ slot, and
that a $(3,2,2)$ coupling makes the eliminated $\Sigma_2$-action quartic, destroying the
closed-form $\mathbb F$ at the next order. Take $a_7$ on $(3,3,1)$.

*Reality.* With the project convention $\Sigma^\ddagger=\Sigma$, $\chi^\ddagger=\chi$ and real
geometric vertices, every monomial above is real for real coefficients; the new couplings
$V_5(\chi,\chi,\Psi)$ and $V_6(\chi,\Sigma,\Sigma)$ are real and symmetric in their repeated
slots, so real $c_\chi,d_\chi$ give a real action. Reality places no constraint beyond
$c_\chi,d_\chi,a_7\in\R$, which (5.1) delivers since $\alpha,\beta,b_\chi$ are real.

### 6.2 What the matching must test

1. The **predicted diagonality**: perturbing $c_\chi$ must move only the $S_1$ residual, and
   $d_\chi$ only the $S_2$ residual (the falsification leg — this is the count's sharpest
   prediction).
2. The **absence of $S_3$ and of any fourth invariant** in the residual: project the
   numerically computed $A_5^\chi$ on $\{V_7(\Psi^7),S_1,S_2,S_3\}$ *and* test that the part
   orthogonal to the whole four-element set vanishes (a residual not spanned by the four is
   as fatal as a nonzero $S_3$). A nonzero $S_3$ falsifies the strand-locality lemma N3
   (§3.2); a nonzero orthogonal remainder falsifies the spanning lemma N3′ (§3.1.5) — the two
   are separate predictions and must be reported separately.
3. The **absence of an $M^{-1}$ composite** at $O(g_s^5)$ (N4), i.e. $A_5^\chi$ independent of
   the $\Sigma_3$ kinetic normalisation.
4. The values $\alpha,\beta$ of (3.1), hence $c_\chi,d_\chi$; and a check that
   $b_\chi^2/a_\chi=4$ survives refitting at $O(g_s^5)$ (N7).
5. The $O(g_s^3)$ and $O(g_s^4)$ legs untouched (Richardson slope $\ge6$ on the residual).
6. That switching on $b'_\chi$ (the $V_5(\chi,\Sigma_3)$ mixing) *does* produce a residual
   component outside $\mathrm{span}\{V_7,S_1,S_2,S_3\}$ — the falsification leg for (E4) and
   for the spanning lemma's dependence on it.
7. **The sextic split.** Run at the pinned $c_6=0$, $c_{\Sigma_3}=1$ of §6.1, then **scan
   $c_6\in[0,1]$** (at least the two endpoints and one interior point) and check the predicted
   affine law $\beta(c_6)=\frac{7(2+c_6)}{5}$ of (3.3d), equivalently
   $\beta(1)/\beta(0)=3/2$ and $\alpha$ independent of $c_6$. This is both a check of the
   row-2/row-4 prefactors and the guarantee that the reported $d_\chi$ is quoted at a stated
   split. Report $d_\chi(c_6)$, not a bare $d_\chi$.

**Implementation constraint: the elimination is not sequentially Gaussian.** With
$V_6(\chi,\Sigma,\Sigma)$ present, eliminating χ (Gaussian, with a $\Sigma$-dependent source)
leaves an action **quartic** in $\Sigma_2$, so the subsequent $\Sigma_2$ elimination is no
longer an exact Gaussian — the structural property that 018 §1/§6 built the all-orders
scheme-B argument on. The matching must therefore use a **joint Newton saddle** in
$(\Sigma_2,\chi,\Sigma_3)$ followed by Richardson extrapolation, as in
`codes/verify-chi-partner.py`, not a sequential closed-form elimination. This is also a real
cost of the χ route against the dressed route, and belongs in that comparison (§6.3).

**Free-constant discipline.** The $O(g_s^4)$ legs fix $(a_\chi,b_\chi)$ and the *sum*
$c_6+c_{\Sigma_3}=1$; only $(c_\chi,d_\chi,a_7)$ are fitted, each from its own direction in
(5.1). Nothing is fitted from the identity that tests closure — the closure test is the
vanishing of the residual at $O(g_s^6)$ slope, which uses none of them twice.

**The one constant the $O(g_s^4)$ sector does *not* fix** is the split itself: $c_6$ and
$c_{\Sigma_3}$ are separately free there and separately visible here (3.3d). It is therefore
**not** true that every constant of §6.1 comes from an independent sector; the earlier version
of this paragraph said so and was wrong. The discipline is restored by *convention plus
prediction*, not by an independent sector: $c_6$ is pinned to $0$ by the two reasons of §6.1
and its effect is predicted in closed form ($\beta\propto2+c_6$), so the matching can test the
convention instead of inheriting it silently. What must never be done is to fit $c_6$ from the
closure residual — that would turn the split into a second free parameter fitted from the
identity under test, on the same footing as $d_\chi$, and closure would then be vacuous.

### 6.3 Regime of validity

The count holds at $O(g_s^5)$ only, at the finite-dimensional algebraic layer (A4), under
A5–A7 and H-B3/H-B4/H-B5/H1. It says nothing about:

- $O(g_s^6)$ and beyond. A first look: at order 8 the contacts need $\sum s=8$, reachable as
  $(3,3,2)$ without a $\Sigma_4$, but the composite directions multiply (e.g.
  $V_6(\chi,\chi,\Sigma)$ and the first $M^{-1}$ composites both enter at $\mathrm{ord}=6$),
  so the generator-vs-deficit race must be re-run order by order. The count gives no
  all-orders statement.
- the quantum status of the negative-norm χ direction (017 §3, open), and the BV/gauge
  structure of the enlarged content (ST7).
- CFT-level realisability of the bare $V_7$ slot restrictions.
- the $b'_\chi\ne0$ branch of (E4), i.e. the χ scheme with a marginal χ–$\Sigma_3$ mixing.
- the physical meaning, if any, of the sextic split $c_6$. It is a presentation freedom at
  $O(g_s^4)$ that becomes an $O(g_s^5)$-visible input (3.3d); the count pins it ($c_6=0$,
  §6.1) but does not derive it, and at $O(g_s^6)$ the same question will return for every
  contact split of the tower.

A cost of the χ route, for the comparison with the dressed route: the loss of sequential
exact Gaussianity (§6.2) removes the closed-form $\mathbb F$ that 018 §1/§6 used, so the
χ scheme's all-orders argument would have to be rebuilt on a joint saddle.

### 6.4 Amendment the ledger row PH16 (H-B5) needs

PH16 predicts the cancelling couplings to be "$V_6(\chi,\Sigma,\Sigma)$,
$V_6(\chi,\chi,\Sigma)$, then partners of $\Sigma_3$". This record **refines** it (it does not
contradict it): at $O(g_s^5)$, $V_6(\chi,\chi,\Sigma)$ has $\mathrm{ord}=6$ (§4.2(f)) and is
irrelevant; the coupling actually needed is $V_5(\chi,\chi,\Psi)$, which is not in PH16's
list; and what is forced at this order is a **right-sign** $\Sigma_3$ with its even HS pair
(N5), not a wrong-sign partner of $\Sigma_3$ (N8). The amended wording is given in the fix
report; the ledger is not edited here.

## 7. Verification and self-review

### Verification

`codes/verify-chi-ogs5-count.py`, seeds 11, 29 and 7, $N=4$, generic symmetric $V_4\ldots V_7$,
12 random $\Psi$ probes per seed, plus a joint-saddle scaling module per seed. Executed
2026-09-21 (second fix pass): **63/63 PASS**, exit 0, counted as **30 independent falsifiable
checks + 6 implied checks + 12 bookkeeping identities + 9 break legs + 6 weak break legs**
(21 lines per seed, three seeds). Two rounds of honesty corrections are folded in here:

- lines that compare an einsum with itself on a fully symmetric tensor cannot fail; they are
  tagged `(IDENT)` and excluded from the substantive count (first fix pass);
- two lines that *can* fail but are **implied** by a check printed above them are tagged
  `(DUP)`: `N6e-generator-rank` (its three columns are a subset of the four whose rank is
  found to be 4 in `N3/A7-independence`) and `N9-R24-rank2` (the same two columns as the
  $r_{20}=2$ leg of `N9-R20-rank1`, given the collapse identity). Likewise the two
  `…-not-4` break legs are implied by the $|s-5|<0.3$ checks they accompany and are tagged
  `(WEAK)`. So the honest independent count is **10 checks and 3 break legs per seed**, not
  12 and 5 (this fix pass).

**Scaling module (new).** The order formula (2.1) and the saddle orders are now measured, not
only asserted. Instrument copied from `codes/verify-chi-partner.py` (which is left untouched):
generic symmetric $T_4,T_5,T_6$, a joint Newton saddle in $(\Sigma,\chi)$ on the symmetric
subspace, and a log-log slope fit over $g\in[3\times10^{-3},1.5\times10^{-2}]$ (window A) and,
for the coupling rows, also over $g\in[10^{-3},5\times10^{-3}]$ (window B, added in this fix
pass).

| tested | prediction of (2.1) | seed 11 | seed 29 | seed 7 |
|---|---|---|---|---|
| $\|\chi_*\|$ | $g^1$ ($o(\chi)=1$) | $1.004$ | $1.000$ | $1.015$ |
| $\|\chi_*/g+\frac{b_\chi}{10a_\chi}V_4^{-1}v\|$ | $\ge g^1$ (eq. 2.2 with its coefficient) | $1.001$ | $1.001$ | $0.999$ |
| $\|\Sigma_*-P\|$ | $g^1$ ($o(\Sigma)=0$, $X=O(g)$) | $1.002$ | $1.001$ | $0.999$ |
| χ sector $a_\chi V_4(\chi,\chi)+b_\chi V_5(\chi,\Sigma,\Psi)$ | $g^4$ | $4.010\,/\,4.003$ | $3.997\,/\,3.999$ | $4.029\,/\,4.010$ |
| $c_\chi V_5(\chi,\chi,\Psi)$ | $g^5$ | $5.005\,/\,5.002$ | $5.020\,/\,5.007$ | $5.013\,/\,5.004$ |
| $d_\chi V_6(\chi,\Sigma,\Sigma)$ | $g^5$ | $4.959\,/\,4.987$ | $5.155\,/\,5.056$ | $4.849\,/\,4.958$ |
| $e_\chi V_6(\chi,\chi,\Sigma)$ | $g^6$ | $6.018\,/\,5.969$ | $6.062\,/\,6.021$ | $6.068\,/\,6.028$ |

(coupling rows: window A / window B.)

Four distinct predicted exponents $(4,5,5,6)$ are resolved, so the test discriminates: a
coupling landing one order away from (2.1) would be seen (the weak break legs restate this
for the two $g^5$ rows).

*The spread of the $d_\chi V_6(\chi,\Sigma,\Sigma)$ slope is contamination by the next order,
not a wrong exponent.* On window A the three seeds give $4.959$, $5.155$, $4.849$ — deviations
of both signs, which excludes a systematic mis-assignment of the order (that would bias all
seeds the same way) and points to an $O(g^6)$ admixture whose sign depends on the random
tensors. The diagnosis is now tested rather than asserted: on window B, one decade lower,
every deviation shrinks towards $5$ ($4.987$, $5.056$, $4.958$, i.e. by factors $3.2$, $2.8$,
$2.9$ — consistent with the $\sim3\times$ reduction in $g$ of a next-order admixture). The
cancellation is $\sim3$ digits out of 16 (an $O(g^5)$ signal subtracted from an $O(g^4)$
base), so round-off is not the limiting effect. The other three rows are stable to $\pm0.07$. This tests N1, N2, the $O(g_s^5)$ placement of the two new couplings
in N6, and the $\mathrm{ord}=6$ clause of §4.2(f)/N8. The $\Sigma_3$ sector is not in the
module, so the predicted $\mathrm{ord}=5$ of $V_7(\Sigma_3,\Sigma_3,\Psi)$ is not measured.

- **N3/A7-independence** — $\{V_7(\Psi^7),S_1,S_2,S_3\}$ independent (normalised SVD rank 4,
  smallest/largest singular value $1.5\times10^{-1}$), and $\{S_1,S_2,S_3\}$ rank 3, i.e.
  $S_3\notin\mathrm{span}\{S_1,S_2\}$. This is what makes the strand-locality lemma
  load-bearing rather than vacuous: the invariant it excludes is a genuinely new direction.
  ($S_3$ is implemented as the strand-split representative of §3.2: the two indices of
  $X=V_4^{-1}v$ routed into two different $V_5$ blocks.)
- **N6c (χ-partition redundancy) — identity, not evidence** — $V_6(\chi_*,p_3,\Psi)=V_6(\chi_*,P,P)$
  to $3\times10^{-16}$: the $(2,3,1)$ and $(2,2,2)$ χ-couplings produce the *same* invariant
  $S_2$. For a fully symmetric $t_6$ the two einsums are literally the same contraction; the
  line documents the Veronese bookkeeping and cannot fail.
- **N6d (V₇-partition redundancy) — identity, same status** — $V_7(p_3,p_3,\Psi)=V_7(p_3,P,P)=V_7(\Psi^7)$
  to $3\times10^{-15}$.
- **N6e-generator-rank (the closure count proper) — implied** — the three leading generator
  values $\{V_7(\Psi^7),\,V_5(\chi_*,\chi_*,\Psi),\,V_6(\chi_*,P,P)\}$ have rank 3 as functions
  of $\Psi$ (sv ratio $0.40$). N6c/N6d show that generators *do* degenerate in this setting, so
  rank 3 is a real outcome and not an automatic one — but it is *not new evidence*: these three
  columns are a subset of the four whose rank is 4 in `N3/A7-independence`, so the line is
  tagged `(DUP)`. The falsifiable core of the closure count is that first check together with
  the three genuine break legs.
- **N6e-generator-labels — identity** — $V_6(\chi_*,P,P)=S_2$ to $9\times10^{-15}$ and
  $V_5(\chi_*,\chi_*,\Psi)=S_1$ to exactly 0: *both* legs are the same contraction written
  twice and carry no evidential weight on their own (the earlier text conceded this only for
  the $S_1$ leg). Their content is supplied by the two break legs below.
- **N9-R20** — the $O(g_s^4)$ falsifier, negative leg. Collapse leg (identity):
  $V_6(\Sigma,\Sigma,\Sigma)$, $V_6(\Sigma_3,\Sigma_2,\Psi)$, $V_6(\Sigma_3,\Sigma_3)$ all
  equal $V_6(\Psi^6)$ ($10^{-15}$). Rank leg (falsifiable): rank 1 without χ *and* rank 2
  with χ — the pair is the substantive statement, since a 1 on the right or a 2 on the left
  would break R20.
- **N9-R24 — implied** — positive leg: $\{V_6(\Psi^6),V_4(\chi_*,\chi_*)=v^\top V_4^{-1}v\}$
  has rank 2 — χ supplies the missing direction. **The count predicts 017's closure**, which is
  the brief's falsifier. Given the collapse identity above, these are the same two columns as
  the $r_{20}=2$ leg of N9-R20, so the line is tagged `(DUP)`: the statement stands, the
  evidence is N9-R20's.
- **Break legs (mandatory)** — (i) replacing $\chi_*=V_4^{-1}v$ by $V_4^{-1}g_6$ destroys the
  $S_1$ identification (rel. dev. $0.8$–$1.0$), so the labelling check is not tautological;
  (ii) **new, replacing the decorative $1.0001$ perturbation**: recomputing $V_6(\chi_*,P,P)$
  with an *independent* sextic tensor breaks the $S_2$ identification (rel. dev. $1.4$–$1.6$)
  — a wrong physical input, not a wrong last digit; (iii) feeding the rank test the two
  *redundant* $V_7$ partitions as if independent returns rank 2, not 3. Legs (i)–(iii) are the
  genuine ones. A fourth pair of legs — the two $g^5$ slope rows asserted to differ from $4$ by
  more than $0.5$ — is **implied** by the $|s-5|<0.3$ checks above them and cannot fail while
  those pass; it is retagged `(WEAK)` and kept only as a readability restatement. The
  discrimination it claims is genuinely delivered instead by the four distinct measured
  exponents $(4,5,5,6)$ and by the two-window comparison.

*What is not verified:* the values $\alpha,\beta$ of the deficit (3.1) — that is the matching
computation, deliberately out of scope for a counting brief. The $c_6$-dependence
$\beta=\frac{7(2+c_6)}{5}$ of (3.3d) is derived by hand from the prefactors of rows 2 and 4
and is **not** machine-checked here (it would require the $\Sigma_3$ sector, absent from the
scaling module); §6.2 item 7 turns it into a prediction for the matching instead. Also not
verified: the strand-locality lemma (§3.2)
and the spanning lemma N3′ (§3.1.5) are proved combinatorially, not machine-checked, since
they are statements about which contractions *can* occur, not numerical identities (the
script tests their discriminating consequence, $S_3\notin\mathrm{span}\{S_1,S_2\}$); and the
$\Sigma_3$ sector is absent from the scaling module, so the $\mathrm{ord}=5$ of
$V_7(\Sigma_3,\Sigma_3,\Psi)$ rests on (2.1) alone.

### Self-review

1. *Objective vs literal task.* The literal task was the count; the objective was to decide
   whether the expensive $O(g_s^5)$ χ-matching is worth running. Answer: yes, with a
   four-coupling action and a sharp falsifiable prediction (diagonality, no $S_3$). The count
   also produced two results the brief did not ask for and that change the picture: $\Sigma_3$
   is **forced** in the χ scheme (so "all-geometric" buys elementary *vertices*, not a shorter
   field tower), and the general mechanism — composites come either from dressing a vertex or
   from depriving a field of its source — which re-derives R19/R20/R24/018 §5 uniformly.
2. *Weakest step.* H1 — and after the second fix pass only *half* of H1. Its kinetic clause
   (no $V_4(\chi,\Sigma)$, and $a_\chi=1$) is now a theorem: the doublet $GL(2)$ has enough
   parameters to diagonalise any nondegenerate split-signature form (§2.4, part 0). What
   remains hypothetical is the *source alignment*, which needs the source doublet to be
   timelike. It is
   argued from the residual $\group{O}(1,1)$ of the $O(g^2)$ doublet and is consistent with 017's
   boost-breaking-at-$O(g^3)$ note, but it is not protected, and a field redefinition
   $\Sigma\to\Sigma+\epsilon\chi$ regenerates $V_4(\chi,\Sigma)$. Shored up by declaring it,
   by its falsifier, and by noting that the frame is fixed by data (the $g^2$ sector) that
   precedes every coupling used here.
3. *Not checked.* The deficit coefficients $\alpha,\beta$; any order beyond $O(g_s^5)$; the
   CFT layer. Acceptable: the brief asked for a paper count and explicitly deferred the
   matching, and the count's predictions are stated so the matching can falsify them.
4. *What the fix pass found.* Carrying out the enumeration the first version had asserted
   produced a real condition, not just a proof of what was already believed: the coupling
   $V_5(\chi,\Sigma_3)$ is admissible at $O(g_s^4)$, invisible there, and opens a marginal
   χ–$\Sigma_3$ mixing with a fourth invariant at $O(g_s^5)$ (E4). The outcome survives
   because the coupling can be set to zero at no cost, but "enough freedom" now carries an
   explicit condition it did not carry before. This is the answer to the previous version's
   item 4: the asserted completeness *was* the weak point.
   — *And what the second fix pass found:* carrying the $1/n!$ prefactors that §3.3 had left
   symbolic turned a declared *presentation freedom* into an *input*: the sextic split
   $c_6+c_{\Sigma_3}=1$, free at $O(g_s^4)$, weights the two $S_2$ sources differently and
   moves $\beta$ by 50 % (3.3c–d). Left unpinned, it would have produced a fitted $d_\chi$
   depending on an unstated number — the free-constant failure mode the project has already
   hit once. The lesson generalises beyond this record: *a split that is invisible at the
   order where it is introduced is not thereby free at the next order*, and every "only the
   sum is fixed" statement in the tower deserves the same one-order-up check.
5. *What a stronger physicist would find in five minutes.* Most likely the observation that
   the diagonality of (5.1) is an artifact of working at the *first* order where each
   generator switches on: at $O(g_s^6)$ the same couplings feed several invariants at once and
   the system stops being triangular. That does not affect the $O(g_s^5)$ outcome but it is
   the reason not to extrapolate "enough freedom" to all orders (§6.3). Second candidate: that
   $V_6(\chi,\Sigma,\Sigma)$ and $V_6(\chi,\Sigma_3,\Psi)$ being redundant at $O(g_s^5)$ need
   not stay redundant at $O(g_s^6)$, so the partition choice made now is a real choice later —
   record it as such.

---

## Addendum 2026-09-26 — PH23: the $\Sym^2$ source doublet is timelike by the $O(g_s^2)$ matching

**Brief:** `agent/briefs/active-computator-ph23-20260926T103000.md` (Task 9h).
**Addendum status:** complete 2026-09-26 (A.0–A.7); verification 54/54 PASS, 9/9 break legs fire (`agent/scratch/ph23-run1.log`). Node-checked 2026-09-30 (all N10.1–N10.8 hold); wording fixes applied 2026-10-01 (see the Annotation block at the end). Next: the ledger edits of A.5 (orchestrator), texts in the fix report.

**Literal task.** PH23 (= the source clause of H1, §2.4) states that the source doublet of the
$\Sym^2$ pair $(\Sigma,\chi)$ is timelike, so that the residual $\group{O}(1,1)$ aligns it with
$\Sigma$ and $\chi$ has no $O(g_s^2)$ source. Decide whether the timelike sign is a free choice
of the presentation or is fixed by a consistency condition; state at which order a single boost
stops aligning the doublet; machine-check both.

**Motivating objective.** PH23 sits under R24 and R42 (the χ scheme). A paper-level statement
needs either a derivation of PH23 or its clean reclassification as a scheme convention.

**Notation.** The brief's doublet $(s_\Sigma,s_\chi)=(a,b)\,V_4(\cdot,P)$ is written here
$(\lambda_\Sigma,\lambda_\chi)\,V_4(\cdot,P)$, as in §2.4, to avoid a clash with R24's
$(a_\chi,b_\chi)=(1,2)$. The $O(g^2)$ doublet sector, before any frame choice, is

$$ S^{(2)}_{\rm aux}=\frac{g^2}{4!}\Big[\,Q_{ab}\,V_4(\phi^a,\phi^b)+2\lambda_a\,V_4(\phi^a,P)\Big],
\qquad \phi=(\phi^1,\phi^2)\in\R^2\otimes\Sym^2\Hilb_0, \tag{A.1} $$

with $Q$ a real symmetric nondegenerate $2\times2$ matrix and $\lambda\in\R^2$ — five numbers,
acted on by the constant redefinitions $\phi=G\phi'$, $G\in GL(2,\R)$:
$Q\to G^\top QG$, $\lambda\to G^\top\lambda$ (λ is a covector). The frame of §2.4 is
$Q=\mathrm{diag}(-1,+a_\chi)$, $\phi=(\Sigma,\chi)$; R24's frame is $a_\chi=1$, $\lambda=(1,0)$.

### A.0 Addendum claim tree (nodes N10–N10.8; to be merged into the record tree)

Uses record assumptions A2, A3, A5, A8, node N1 (order formula), condition (E4) $b'_\chi=0$, and
the ledger rows R24 (Verified), R42/R49 (cited for the $O(g^5)$ values only) and R35
(Conditional(PH6), for N10.8 only). The kinetic form is taken of split signature, as the χ scheme
defines it; N10.8 shows this is forced.

- **N10** PH23 is not a hypothesis. Its sign clause (the source doublet is timelike) is
  **derived** from the $O(g_s^2)$ matching; its alignment clause is a **frame convention**, the use
  of the residual $\group{O}(1,1)$, unique up to $\chi\to-\chi$; the alignment holds at $O(g_s^2)$
  only, which is what R24 and R42 use. [by N10.1–N10.6]
  - **N10.1** For any nondegenerate $Q$, the on-shell value of the $O(g^2)$ doublet sector is
    $-\langle\lambda,\lambda\rangle\frac{g^2}{4!}V_4(\Psi^4)$, $\langle\lambda,\lambda\rangle=\lambda^\top Q^{-1}\lambda$,
    a $GL(2)$ invariant. [by A5; eq. (A.2)] [check: N10.1]
  - **N10.2** The $O(g_s^2)$ matching is exactly $\langle\lambda,\lambda\rangle=-1$. [by A3, A8, N1,
    N10.1; eq. (A.3)] [check: N10.2]
  - **N10.3** Hence the doublet is strictly timelike with unit norm ($\lambda_\Sigma^2-\lambda_\chi^2=1$
    at $a_\chi=1$); null and spacelike doublets, and non-unit timelike ones, fail the matching.
    [by N10.2; eq. (A.4)] [check: N10.3]
  - **N10.4** $GL(2,\R)$ acts transitively on the consistent $O(g^2)$ data with stabiliser
    $\{\mathrm{diag}(1,\pm1)\}$; the aligned frame $(Q_0,\lambda_0)$ always exists and is a convention.
    [by N10.2; eq. (A.8)] [check: N10.4]
  - **N10.5** No matching condition through $O(g_s^5)$ constrains λ beyond N10.2: the $O(g^3)$
    condition is $\langle\lambda,\mu\rangle=-1$, the $O(g^4)$ closure $\langle\mu,\mu\rangle=0$, and at
    $O(g^5)$ every condition is $GL(2)$-covariant, so the set of λ admitting a consistent completion
    is $\group{O}(1,1)$-invariant – empty or the whole hyperboloid; it is non-empty by 048 (R42
    appendix, Numerical), which is cited only for the existence of a closure. [by A2, N10.4, R24;
    eqs. (A.9)–(A.10), A.4 "No further condition"; R42 for non-emptiness only] [check: N10.5
    (through $O(g^4)$ only)] [revised 2026-10-01, critic node check]
  - **N10.6** The alignment fails at $O(g_s^3)$ necessarily: the $O(g^3)$ source $\mu\otimes v$ has
    $v$ cubic in $\Psi$ (never parallel to $u$) and $\mu$ null and nonzero (so $\mu_\chi\ne0$ in every
    frame with diagonal kinetic form; frame-free: λ and μ are linearly independent, so no
    $G\in GL(2)$ frees one field of both its $O(g^2)$ and $O(g^3)$ sources); in the aligned frame χ's source is $\frac{g^3b_\chi}{5!}v$, R24's mechanism.
    [by A2, A3, A8, (E4), N10.4, N10.5, R24; eqs. (A.5), (A.11)] [check: N10.6]
  - **N10.7** Correction: the timelike condition printed in H1 (claim tree, l. 82) and in §2.4 part 1
    (l. 275), $a_\chi\lambda_\chi^2<\lambda_\Sigma^2$ (both now corrected in place),
    should read $\lambda_\chi^2<a_\chi\lambda_\Sigma^2$ (dual norm); identical at $a_\chi=1$, no downstream
    change. [by N10.1; A.3] [check: N10.7]
  - **N10.8** (side claim, not used by N10) With real coefficients, the $O(g^2)$–$O(g^4)$ matching
    of the χ scheme forces split signature. Conditional on PH6 at the string level.
    [by R35, N10.2, N10.5; A.3]

Open gaps (addendum): none.
Hypotheses in force (addendum): none for N10; PH6 (through R35) for the side claim N10.8 only.
Record-level consequence: H1 is discharged (kinetic clause §2.4 part 0, source clause N10), so
the record's `Hypotheses in force` line becomes H-B3, H-B4, H-B5 — to be applied to the tree at
the top by the orchestrator (this addendum is append-only).

### A.1 The $O(g_s^2)$ doublet sector and its on-shell value (N10.1)

**Setup.** Record assumptions A2, A3, A5; (A.1) with arbitrary nondegenerate $Q$ and
$\lambda\in\R^2$. Dual pairing on doublet covectors: $\langle\alpha,\beta\rangle:=\alpha^\top Q^{-1}\beta$.
$K:=V_4$ viewed as a symmetric operator on $\Sym^2\Hilb_0$ (invertible, A5); $u:=V_4(\cdot,P)=KP$.

**Derivation.**

$$
\begin{aligned}
0&=\frac{\partial S^{(2)}_{\rm aux}}{\partial\phi^a}
 =\frac{2g^2}{4!}\Big[Q_{ab}\,K\phi^b+\lambda_a\,KP\Big]
 &&\Longrightarrow\quad \phi_*^a=\hat\phi^a\,P,\qquad \hat\phi:=-Q^{-1}\lambda,
 \\
S^{(2)}_{\rm aux}\big|_*
&=\frac{g^2}{4!}\Big[\hat\phi^\top Q\hat\phi+2\lambda^\top\hat\phi\Big]V_4(P,P)
 =\frac{g^2}{4!}\Big[\lambda^\top Q^{-1}\lambda-2\lambda^\top Q^{-1}\lambda\Big]V_4(P,P)
 \\
&=-\frac{g^2}{4!}\,\langle\lambda,\lambda\rangle\,V_4(\Psi^4).
\end{aligned}
\tag{A.2}
$$

**Commentary.** The saddle is proportional to $P$ in both components because the source is
(A.1)'s single vector $u$ in both: this is PH23's motivation, and it is what makes the sector
one-dimensional in $\Sym^2$. $V_4(P,P)=V_4(\Psi^4)$ is the Veronese identity. For the single
HS field ($Q=-1$, $\lambda=1$) (A.2) returns $+\frac{g^2}{4!}V_4(\Psi^4)$, the known HS value
(§2.2).

**Result.** $S^{(2)}_{\rm aux}|_*=-\langle\lambda,\lambda\rangle\,\frac{g^2}{4!}V_4(\Psi^4)$: the
on-shell value depends on $(Q,\lambda)$ only through the $GL(2)$ invariant
$\langle\lambda,\lambda\rangle=\lambda^\top Q^{-1}\lambda$ (under $\phi=G\phi'$:
$\lambda'^\top Q'^{-1}\lambda'=\lambda^\top GG^{-1}Q^{-1}G^{-\top}G^\top\lambda=\lambda^\top Q^{-1}\lambda$).

### A.2 The matching condition fixes the sign (N10.2, N10.3)

**Setup.** Order formula (2.1) (N1), A3, A8. Target: $S_{\rm eff}$ at $O(g^2)$ is
$+\frac{g^2}{4!}V_4(\Psi^4)$ (the closed-SFT quartic, same sign convention as 017 and
`codes/verify-chi-partner.py`).

**Derivation.** The terms of the cubic presentation that contribute to the on-shell action at
$O(g^2)$ have $(\sum_is_i-2)+\sum_io_i=2$ by (2.1). With $\sum_i o_i=0$ they have $\sum_is_i=4$:
the terms of (A.1), $V_4(\Psi^4)$ (quartic in one field, excluded by A3) and $V_4(\Sigma_3,\Psi)$
(excluded by A8). With $\sum_io_i\ge1$ they have $\sum_is_i\le3$: $V_3(\phi,\Psi)$, $V_2(\phi)$
(sources at $g^1$, $g^0$, excluded by A8 for the reason A8 states: they would give the doublet
a negative saddle order). The $O(g)$ correction to the saddle does not contribute at $O(g^2)$
(stationarity). Hence the $O(g^2)$ matching is exactly

$$ -\langle\lambda,\lambda\rangle\,V_4(\Psi^4)=+V_4(\Psi^4)\quad\forall\Psi
\qquad\Longrightarrow\qquad
\boxed{\ \langle\lambda,\lambda\rangle=\lambda^\top Q^{-1}\lambda=-1\ } \tag{A.3} $$

($V_4(\Psi^4)\not\equiv0$ at the string vertex, and at generic tensors). In the frame of §2.4,
$Q=\mathrm{diag}(-1,+a_\chi)$, $a_\chi>0$:

$$ \lambda_\Sigma^2-\frac{\lambda_\chi^2}{a_\chi}=1,\qquad\text{and at }a_\chi=1:\quad
-\lambda_\Sigma^2+\lambda_\chi^2=-1,\quad
(\lambda_\Sigma,\lambda_\chi)=\pm(\cosh\eta,\sinh\eta),\ \eta\in\R. \tag{A.4} $$

**Commentary.** (A.3) is a consistency condition of the scheme at the lowest order at which
the doublet enters; nothing is chosen in it. In terms of the free parameters of §2.4 part 0:
once the kinetic form is brought to $\mathrm{diag}(-1,+1)$ (3 of the 4 $GL(2)$ parameters), the
brief's $(a,b)=(\lambda_\Sigma,\lambda_\chi)=\pm(\cosh\eta,\sinh\eta)$, and the only free parameter left
is the rapidity $\eta$ of the residual $\group{O}(1,1)$ — the sign and the norm are not free. The brief's Minkowski norm of the doublet,
$-\lambda_\Sigma^2+\lambda_\chi^2$, equals $-1$: the doublet is **strictly timelike, with unit
norm**. No condition forces $|\lambda_\Sigma|\le|\lambda_\chi|$; the $O(g^2)$ matching forbids it.
A null doublet gives on-shell value $0$ (the quartic vertex is not reproduced), a spacelike one
gives the quartic with the wrong sign, and no rescaling repairs either, because the on-shell
value depends only on the invariant $\langle\lambda,\lambda\rangle$. The word "timelike" is
convention-independent in the following sense: the kinetic direction called $\Sigma$ is by
definition the one whose Gaussian reproduces the quartic with its actual sign (§2.2, $Q=-1$ for
$+V_4$); had the target carried the opposite sign, $\Sigma$'s kinetic sign would flip with it,
and (A.3) would again place the source in $\Sigma$'s cone. What (A.3) says intrinsically is:
*the source lies on the unit hyperboloid of the cone of kinetic directions that reproduce the
quartic*.

**Result.** The sign clause of PH23 is **derived**: under A3 and A8 the $O(g_s^2)$ matching
forces $\langle\lambda,\lambda\rangle=-1$, strictly timelike.

### A.3 Normal form: what is chosen and what is not (N10.4, N10.7, N10.8)

**Setup.** $\mathcal D:=\{(Q,\lambda):\ Q=Q^\top$ nondegenerate of split signature,
$\langle\lambda,\lambda\rangle=-1\}$, the $O(g^2)$ data allowed by (A.3). $Q_0:=\mathrm{diag}(-1,+1)$,
$\lambda_0:=(1,0)$, $\Lambda(\eta):=\begin{pmatrix}\cosh\eta&\sinh\eta\\\sinh\eta&\cosh\eta\end{pmatrix}$.

**Derivation.** Given $(Q,\lambda)\in\mathcal D$:

$$
\begin{aligned}
&\text{(i) Sylvester: } Q=R\,\mathrm{diag}(w_1,w_2)R^\top,\ w_1<0<w_2;\quad
G_1:=R\,\mathrm{diag}(|w_1|^{-1/2},|w_2|^{-1/2}),\quad G_1^\top QG_1=Q_0;\\
&\text{(ii) } \lambda_1:=G_1^\top\lambda\ \text{ has }\ -\lambda_{1,\Sigma}^2+\lambda_{1,\chi}^2
 =\langle\lambda,\lambda\rangle=-1\ \Rightarrow\ \lambda_1=\epsilon(\cosh\eta_1,\sinh\eta_1),\
 \epsilon=\pm1;\\
&\text{(iii) } G:=\epsilon\,G_1\Lambda(-\eta_1):\qquad G^\top QG=Q_0,\qquad
 G^\top\lambda=\epsilon^2\Lambda(-\eta_1)\Lambda(\eta_1)(1,0)^\top=\lambda_0 .
\end{aligned}
\tag{A.8}
$$

Stabiliser: $G^\top Q_0G=Q_0$ puts $G$ in $\group{O}(1,1)$, whose elements are
$\mathrm{diag}(\epsilon_1,\epsilon_2)\Lambda(\eta)$; $G^\top\lambda_0=\lambda_0$ fixes the first row of $G$
to $(1,0)$, hence $\eta=0$, $\epsilon_1=1$: $\mathrm{Stab}(Q_0,\lambda_0)=\{\mathrm{diag}(1,\pm1)\}$.

**Commentary.** Step (ii) is where (A.3) enters: $\lambda_1$ lies on the unit hyperboloid, so
the rapidity $\eta_1=\operatorname{artanh}(\lambda_{1,\chi}/\lambda_{1,\Sigma})$ is finite. For a
null or spacelike $\lambda_1$ the ratio is $\ge1$ in modulus, no real $\eta_1$ exists, and
$|\lambda'_\chi|\ge\sqrt{\langle\lambda,\lambda\rangle}$ in every $\group{O}(1,1)$ frame
(check `N10.4-spacelike-no-boost`). Parameter count: $\dim\mathcal D=3+2-1=4=\dim GL(2)$ with a
finite stabiliser, consistent with (A.8) giving a single orbit.

**Result (N10.4).** $GL(2,\R)$ acts transitively on $\mathcal D$ with stabiliser
$\{\mathrm{diag}(1,\pm1)\}$: **every** consistent $O(g_s^2)$ doublet presentation is a constant field
redefinition of R24's, $Q_0=\mathrm{diag}(-1,+1)$, $\lambda_0=(1,0)$. The $O(g^2)$ doublet sector
has no free parameter modulo redefinitions. The alignment clause of PH23 is the choice of this
representative — a frame convention, always available, consuming the residual
$\group{O}(1,1)$ — and after it the frame is rigid up to $\chi\to-\chi$, which flips the sign of
$b_\chi$ (only $b_\chi^2/a_\chi$ is physical, R24). Together with §2.4 part 0 (kinetic form:
3 of the 4 parameters) this completes the count $3+1=4$: part 0's "consumed by the source
alignment" holds because (A.3) guarantees the source is alignable.

**N10.7 (correction to §2.4 part 1).** §2.4 prints the timelike condition as
$a_\chi\lambda_\chi^2<\lambda_\Sigma^2$. The source is a covector, the invariant is the dual norm
$\langle\lambda,\lambda\rangle=-\lambda_\Sigma^2+\lambda_\chi^2/a_\chi$, and the condition is
$\lambda_\chi^2<a_\chi\lambda_\Sigma^2$. The two agree at $a_\chi=1$, the only value used in 038,
048, R24 and R42, so no downstream statement changes. Counterexample to the printed form:
$a_\chi=4$, $\lambda=(1,1)$ is dual-timelike ($\langle\lambda,\lambda\rangle=-3/4$) and is aligned
by the $Q$-preserving boost $D\Lambda(-\eta)D^{-1}$, $D=\mathrm{diag}(1,a_\chi^{-1/2})$,
$\eta=\operatorname{artanh}\tfrac12$, while $a_\chi\lambda_\chi^2=4>1=\lambda_\Sigma^2$
(checks `N10.7-*`).

**N10.8 (the signature is forced too; side remark).** If $Q$ is positive definite,
$\langle\lambda,\lambda\rangle>0$ contradicts (A.3). If $Q$ is negative definite, the dual form is
definite, so the null condition (A.10) below forces $\mu=0$, contradicting (A.9)
$\langle\lambda,\mu\rangle=-1$. With real coefficients, the $O(g^2)$–$O(g^4)$ matching of the χ
scheme therefore admits split signature only: H-B4's *signature* is derived, its *harmlessness*
(no propagating state) is what PH15 still carries. At the string level the reality of the
coefficients is R35, Conditional(PH6). N10 does not use N10.8: PH23 is posed for split signature.

### A.4 Higher orders: the alignment fails at $O(g_s^3)$, necessarily (N10.5, N10.6)

**Setup.** A2, A3, A8, (E4) with $b'_\chi=0$. The $O(g^3)$ couplings of the doublet, in any
frame: $\frac{g^3}{5!}B_{ab}V_5(\phi^a,\phi^b,\Psi)$, $B=B^\top$. The other $\sum s=5$ terms linear
in a doublet leg are $V_5(\phi,\Psi,\Psi,\Psi)$ (A3), $V_5(\Sigma,\Sigma_3)$ (A8) and
$V_5(\chi,\Sigma_3)$ ($b'_\chi=0$). R24's frame: $B=\begin{pmatrix}1&b_\chi/2\\ b_\chi/2&c_\chi\end{pmatrix}$.
$v:=V_5(\cdot,P,\Psi)=W P$ with $W:=V_5(\cdot,\cdot,\Psi)$; $w:=V_6(\cdot,P,P)$.

**Derivation.** The saddle equation is $\frac{2g^2}{4!}(Q\otimes K)\phi=-J(\phi)$ with
$J(\phi):=\frac{2g^2}{4!}\lambda\otimes u+\frac{2g^3}{5!}(B\otimes W)\phi$. $J$ evaluated on the
leading saddle $\phi=\hat\phi\otimes P$ is the **effective doublet source** through $O(g^3)$:

$$ J=\frac{2g^2}{4!}\Big[\lambda\otimes u+\frac g5\,\mu\otimes v\Big]+O(g^4),\qquad
\mu:=B\hat\phi,\quad \hat\phi=-Q^{-1}\lambda . \tag{A.5} $$

Expanding $S$ around $\hat\phi\otimes P$ with $\phi=\hat\phi\otimes P+\delta$, the conditions through
$O(g^4)$ are

$$
\begin{aligned}
O(g^3):&\quad \frac{g^3}{5!}\,\hat\phi^\top B\hat\phi\ V_5(P,P,\Psi)=\frac{g^3}{5!}V_5(\Psi^5)
 \iff \hat\phi^\top\mu=1\iff \boxed{\langle\lambda,\mu\rangle=-1}, \qquad &\text{(A.9)}\\
O(g^4):&\quad \delta_*=-\frac g5\,(Q^{-1}\mu)\otimes K^{-1}v,\qquad
 S\supset\frac{g^2}{4!}\frac{g^2}{25}\langle\mu,\mu\rangle\,vK^{-1}v-\frac{2g^3}{5!}\frac g5\langle\mu,\mu\rangle\,vK^{-1}v
 =-\frac{g^4}{600}\langle\mu,\mu\rangle\,vV_4^{-1}v,\\
&\quad\text{closure without a composite (sextic contact matched by } V_6(\Sigma^3)\text{, R24)}
 \iff \boxed{\langle\mu,\mu\rangle=0}. &\text{(A.10)}
\end{aligned}
$$

In R24's frame ($Q=\mathrm{diag}(-1,a_\chi)$, $\lambda=\lambda_0$, $\hat\phi=(1,0)$, $\mu=(1,b_\chi/2)$):
(A.9) is $B_{\Sigma\Sigma}=1$ and $\langle\mu,\mu\rangle=-1+b_\chi^2/(4a_\chi)$, so (A.10) **is** R24's
forced ratio $b_\chi^2/a_\chi=4$; the no-χ residual $+\frac{g^4}{600}vV_4^{-1}v$ (R17) is
$\mu=(1)$, $Q=(-1)$; the parabola $1-b_\chi^2/4$ of `verify-chi-partner.py` check (3) is
$-\langle\mu,\mu\rangle$.

**The χ scheme through $O(g_s^4)$ in covariant form.**

$$ \langle\lambda,\lambda\rangle=-1,\qquad\langle\lambda,\mu\rangle=-1,\qquad\langle\mu,\mu\rangle=0 :
\tag{A.11} $$

the $O(g^2)$ source is unit timelike, the $O(g^3)$ source is **null** with unit projection on it.
In the aligned frame $\mu=(1,\pm1)$, i.e. $b_\chi=\pm2\sqrt{a_\chi}$: the two null directions are
the two signs of $b_\chi$ exchanged by the stabiliser $\chi\to-\chi$, and the light-cone
combinations $\Pi_\pm$ of 017 §3 are exactly the null directions of the doublet.

**Alignment at $O(g^3)$ (N10.6).** After a constant redefinition $G$, the χ-component of (A.5) is
$(G^\top\lambda)_\chi\,u+\frac g5(G^\top\mu)_\chi\,v$. It fails to vanish; the two items below are two forms of one fact, $\mu\not\parallel\lambda$, seen in the aligned frame and in all frames with diagonal kinetic form.

1. *Degree.* $u$ is quadratic in $\Psi$ and $v$ cubic, so they are never proportional as
   functions of $\Psi$ (not merely at generic vertices; at fixed generic $\Psi$ they are also
   independent vectors of $\Sym^2\Hilb_0$). Vanishing needs both coefficients zero; the first
   fixes $G$ up to the stabiliser, and then the second is $\pm\mu_\chi=\pm b_\chi/2\ne0$.
2. *Nullity.* By (A.10) and (A.9), $\mu$ is null and nonzero, so $|\mu'_\chi|=|\mu'_\Sigma|\ne0$
   in **every** $\group{O}(1,1)$ frame (every frame with diagonal kinetic form; frame-free: λ and μ
   are linearly independent, since $\mu=c\lambda$ would give $\langle\mu,\mu\rangle=-c^2=0$, hence
   $\mu=0$, against $\langle\lambda,\mu\rangle=-1$): no boost, finite or $g$-dependent, removes the $O(g^3)$
   source of χ, whether or not the $O(g^2)$ source is aligned.

A $g$-dependent redefinition $G(g)=G_0+gG_1$ changes the $O(g^3)$ χ-source by a multiple of $u$
only, and produces $g^3V_4$, $g^4V_5$ couplings outside A2; a $\Psi$-dependent shift
$\chi\to\chi+c\,g\,V_4^{-1}v$ is a composite redefinition, outside the elementary class (it is
the integration of χ that the scheme exists to avoid). At $O(g^4)$ a third direction $w$
(quartic in $\Psi$) enters through $V_6(\chi,\Sigma,\Sigma)$ and its redundant partner
$V_6(\chi,\Sigma_3,\Psi)$ ($V_6(\cdot,p_3,\Psi)=w$ by Veronese); its χ-coefficient $d_\chi=2+c_6$ is
fixed at $O(g^5)$ (R42, R49) and is nonzero at the pinned $c_6=0$.

**No further condition on λ (N10.5).** A constant $G\in GL(2)$ maps each $g^{n-2}V_n$ term to a
combination of $g^{n-2}V_n$ terms (A2 preserved; the menu is $GL(2)$-closed once every doublet
component of a vertex is admitted) and leaves the on-shell action unchanged. A presentation
consistent through $O(g^5)$ is therefore mapped to a consistent one, and $G^\top\lambda$ sweeps the
whole unit hyperboloid (both sheets) as $G$ runs over $\{\pm1\}\times\group{O}(1,1)$. The higher
conditions — (A.9), (A.10), and at $O(g^5)$ the values $(c_\chi,d_\chi,a_7)=(1,2+c_6,1)$ of 048 —
constrain the higher couplings *relative to* λ, never λ itself. At $O(g^5)$ this rests on the
covariance argument alone: the set of consistent presentations is $GL(2)$-invariant, so its
λ-projection at fixed $Q_0$ is $\group{O}(1,1)$-invariant, hence empty or the whole hyperboloid;
R42 (048, Numerical) is cited only for the existence of a closure, i.e. non-emptiness
[revised 2026-10-01, critic node check]. The frame-dependent-looking
conditions are covariant: A8's exclusion of $V_5(\Sigma,\Sigma_3)$ together with $b'_\chi=0$ is
$V_5(\phi^a,\Sigma_3)=0$ for both $a$, which zero maps to zero; $c_6$ is a $\Sigma_3$-sector split.

**Commentary.** (A.5) is the first-order iteration of the saddle equation; its χ-component in
the aligned frame, $\frac{g^3b_\chi}{5!}v$, reproduces (2.2). The degree argument (1) is the answer
to the brief's question as posed — new $\Sym^2$ sources not parallel to $V_4(\cdot,P)$ appear at
$O(g^3)$; the nullity argument (2) is stronger and was not anticipated: it is R24's closure
condition read in the doublet geometry, and it shows that the $O(g^3)$ misalignment is not a
genericity accident to be tuned away but a *requirement* of the $O(g^4)$ closure.

**Result (N10.5, N10.6).** The alignment of the doublet source holds at $O(g_s^2)$ exactly and
fails at $O(g_s^3)$ necessarily: (A.11) forces a null, hence never alignable, $O(g^3)$ source.
Through $O(g_s^5)$ no condition constrains λ beyond (A.3).

### A.5 Consequences: PH23, H1, R24, R42 (proposed)

- **PH23 is not a hypothesis, and not a free choice either.** Its *sign* clause is derived
  (N10.2–N10.3: the $O(g_s^2)$ matching forces $\langle\lambda,\lambda\rangle=-1$); its *alignment*
  clause is a frame convention (N10.4: the aligned frame always exists and is unique up to
  $\chi\to-\chi$). Proposed status: **discharged** — "derived sign + frame convention", with the
  convention made explicit as a candidate `local` entry of `knowledge/conventions.md`:
  *χ-scheme doublet frame: kinetic form $\mathrm{diag}(-1,+1)\otimes V_4$ on $(\Sigma,\chi)$,
  $O(g_s^2)$ source $(1,0)\otimes V_4(\cdot,P)$, sign of χ fixed by $b_\chi>0$*.
- **H1 of this record is fully discharged**: the kinetic clause by §2.4 part 0, the source clause
  by N10. The record's `Hypotheses in force` line becomes H-B3, H-B4, H-B5 (= PH14, PH15, PH16);
  H-B4 keeps only its harmlessness content (N10.8 derives the signature, given real
  coefficients).
- **038's two falsifier clauses of H1 are void.** (i) "the $O(g_s^5)$ matching closes only with
  a nonzero $V_4(\chi,\Psi^{\otimes2})$": by N10.5 a closure with $\lambda_\chi\ne0$ is the boost of a
  closure with $\lambda_\chi=0$, so the clause cannot trigger. (ii) "the $O(g^3)$ boost breaking
  regenerates a $g^2$ χ-source under the redefinition restoring the frame at $O(g^3)$": the frame
  is fixed by the $O(g^2)$ data alone, there is nothing to restore, and the only redefinitions
  compatible with A2 are the constant ones of N10.4.
- **Source-deprivation is an $O(g_s^2)$ statement, and that is all R24 and R42 use.** $o(\chi)=1$
  (§2.2, N2) needs exactly "no $O(g^2)$ source"; the $O(g^3)$ source $\frac{g^3b_\chi}{5!}v$ is the
  mechanism, and (A.11) shows it is *required* by the $O(g^4)$ closure (a null $O(g^3)$ source).
  Wording to use: "χ has no $O(g_s^2)$ source", never "χ has no source". R24's critic concern [C2]
  (boost broken at $O(g^3)$) is the same fact; this addendum gives its two reasons.
- **Ledger edits proposed.** PH23: `open` → discharged (038 Addendum N10). R24 carries no PH23
  (its statuses are Conditional(PH1, PH5) and Conditional(PH1, PH5, PH6); PH23's "Used by" lists
  R42 and R49 only), so there is nothing to drop there. R42 (both Status lines): drop PH23 and
  keep `PH14 [$O(g_s^4)$, $O(g_s^5)$], PH15, PH16`. R49 heading: `Conditional(PH14 [$O(g_s^4)$,
  $O(g_s^5)$], PH15, PH16) – Proven`. PH23 is also cited in R49's Scope and in PH16's Scope:
  both lose PH23 and cite its discharge (038 Addendum N10). R24 annotation (N10.8 is the
  frame-free form of R24's existing clause 'reality + $b_\chi^2/a_\chi=4$ ⇒ $a_\chi>0$', 028 §3, not a
  new result): *covariant form of the χ scheme through $O(g_s^4)$, (A.11): unit-timelike $O(g^2)$
  source, null $O(g^3)$ source with $\langle\lambda,\mu\rangle=-1$; $b_\chi^2/a_\chi=4$ is the nullity
  $\langle\mu,\mu\rangle=0$; split signature forced given real coefficients (N10.8, via R35,
  Conditional(PH6))*. [corrected 2026-10-01 after the node check; final texts in the fix report.]

**Scope of the negative statements** ("null and spacelike doublets fail", N10.3; "no frame
aligns the $O(g^3)$ source", N10.6). *Class:* cubic presentations (A3) of the $\Sym^2$ sector by
a doublet with elementary, $g$-independent-coefficient couplings (A2) and no lower-order
sources (A8: no $V_2(\phi)$, $V_3(\phi,\Psi)$, $V_4(\Sigma_3,\Psi)$, $V_5(\Sigma,\Sigma_3)$); physical
reason: this is the χ scheme as defined by R24 and 038, and A8 protects the already-closed
lower orders. *Relevant cases outside:* a direct quartic contact $V_4(\Psi^4)$ (drops cubicity,
the project's point); composite (Ψ-dependent) redefinitions of χ (drop elementarity); with
more than two $\Sym^2$ auxiliaries the same computation gives $\langle\lambda,\lambda\rangle=-1$ for
the multiplet source, so the sign statement survives, but the uniqueness of the frame (N10.4)
does not — none of these is the χ scheme. *Weakest relaxation that evades N10.3:* a quartic
contact with coefficient $1+\langle\lambda,\lambda\rangle$, i.e. giving up A3.

### A.6 Verification

`codes/verify-ph23-doublet.py` (numpy, $N=3$, $\dim\Sym^2=6$, seed 20260926; models on seeds
20260926–20260928), log `agent/scratch/ph23-run1.log`: **54/54 PASS, 9/9 break legs fire,
exit 0**, 1.7 s. The on-shell action is computed by an exact linear solve of the saddle at each
$g$, and the Taylor coefficients $c_2,c_3,c_4$ of $S_{\rm aux}(\text{saddle})-S_t$ are extracted by a
Chebyshev fit on $g\in[-0.1,0.1]$ — a path that never uses (A.2), (A.9), (A.10); the target
vertices are independent `einsum` contractions of $T_4,T_5$ with $\Psi$.

| node | checks | what they establish |
|---|---|---|
| N10.1 | `N10.1[0-2]`, `N10.1-veronese[0-2]`; break `BREAK-N10.1-Q-not-Qinv[0-2]` | (A.2) against the linear solve at non-diagonal split $Q$ (3 seeds); $Q$ in place of $Q^{-1}$ fails |
| N10.2, N10.3 | `N10.2-c2-closed-form[4 cases]`, `N10.2-timelike-matches`, `N10.3-{null,spacelike-unit,timelike-nonunit}-fails` | fitted $c_2=-(\langle\lambda,\lambda\rangle+1)V_4/4!$; matching iff unit timelike |
| N10.4 | `N10.4-normal-form[0-4]`, `N10.4-chi-saddle-zero[0-4]`, `N10.4-invariance[0-4]`, `N10.4-stabiliser-discrete`, `N10.4-spacelike-no-boost`; breaks `BREAK-N10.4-{spacelike,null}-aligned` | (A.8) on 5 random consistent $(Q,\lambda)$ with $\lambda_\chi\ne0$: χ saddle $\le1.1\times10^{-15}$ after alignment; spacelike: $\min_\eta\lvert\lambda'_\chi\rvert=\sqrt3$ exactly |
| N10.7 | `N10.7-dual-norm-criterion`, `N10.7-printed-038-inequality-wrong` | counterexample $a_\chi=4$, $\lambda=(1,1)$ |
| N10.6 | `N10.6-u-v-independent[0-2]`, `N10.6-degrees[0-2]`, `N10.6-chi-source-O(g3)`, `N10.6-mu-null`, `N10.6-mu-never-aligned`, `N10.6-no-joint-boost`, `N10.6-R24-closure-is-nullity`, `N10.6-c4-closed-form[b=1]`; breaks `BREAK-N10.6-{u-v-parallel,timelike-mu-never-aligned,mu-parallel-lam,b1-closes}` | $O(g^3)$ χ-source $=g^3b_\chi v/5!$ by finite differences; no boost on $\lvert\eta\rvert\le4$ kills it ($\min\lvert J'_\chi\rvert=1.4\times10^{-2}$ at $g=0.2$; zero when $\mu\parallel\lambda$); fitted $c_4=-\langle\mu,\mu\rangle vK^{-1}v/600$ at $b_\chi=1$ to $8\times10^{-11}$ relative (gate $10^{-6}$), and $c_4=0$ at $b_\chi=2$ |
| N10.5 | `N10.5-c3-closed-form`, `N10.5-covariance[0-3]`, `N10.5-recover-aligned[0-3]` | (A.9) against the fit; four random $GL(2)$ frames with $\lambda_\chi\ne0$ match through $O(g^4)$ and are brought back to $\lambda_0$, $b_\chi=\pm2$ by (A.8) |

*Weak checks, stated as such (node check 2026-10-01).* Of the 54 checks, 25 are identities or
implied by another check and are not evidence for their node: `N10.4-invariance[0-4]` (true for
any invertible $G$), `N10.4-chi-saddle-zero[0-4]` (implied by `normal_form`: block-diagonal
$H$, $J_\chi=0$), `N10.6-degrees[0-2]` (true by construction of `set_psi`), together with the
ones listed next. Of the 9 break legs, 7 perturb a passing check; `BREAK-N10.4-{spacelike,null}-aligned`
restate `normal_form`'s own guard `abs(ratio) < 1` and perturb nothing. Load-bearing: `N10.1[0-2]`,
`N10.2-*`, `N10.3-*`, `N10.5-c3-closed-form`, the invariant part of `N10.5-covariance`,
`N10.6-c4-closed-form`, `N10.6-R24-closure-is-nullity`, `N10.6-u-v-independent`,
`N10.6-chi-source-O(g3)`, `N10.7-dual-norm-criterion`. `N10.6-mu-null` evaluates $\langle\mu,\mu\rangle$ at R24's $B$
(arithmetic); the independent support of (A.10) is the fitted $c_4$ pair.
`N10.6-mu-never-aligned` and `N10.4-stabiliser-discrete` are grid illustrations of identities
proved in A.3–A.4. `N10.5-covariance` tests invariance of the on-shell action under constant
redefinitions — expected, but it is what N10.5 asserts, and it is run through the exact solve.
*Not machine-checked:* the $O(g^5)$ part of N10.5 (argued from $GL(2)$-closure of the menu; the
048 matching is cited, not re-run in a boosted frame); the exclusion of other $O(g^2)$ terms
(A3, A8: structural); N10.8 (two lines of algebra); everything at the CFT level (A4).
*Diagnosed failure during the run:* the first run (`agent/scratch/ph23-run0-fitscale-bug.log`,
53/54) failed `N10.6-c4-closed-form[b=1]` by exactly $10^2$: the fit coefficients were read in the
rescaled variable $g/0.1$. Typo in the check (first case of the diagnosis order); fixed by
converting to the monomial basis in $g$; the zero-valued checks were unaffected in substance.

### A.7 Self-review

1. *Objective.* Answered: PH23 is reclassified, and more strongly than the brief's two options —
   the sign is derived, the alignment is a convention, and the $O(g^3)$ failure is required by
   R24's closure. A paper-level statement can cite (A.3), (A.8), (A.11) and needs no hypothesis
   for the $\Sym^2$ frame.
2. *Weakest step.* N10.2's claim that nothing else contributes at $O(g^2)$: it rests on A3 and A8,
   i.e. on the scheme's definition, not on a computation. It is the correct dependency (the
   question is about the scheme), and the scope paragraph names what lies outside.
3. *Not checked.* The $O(g^5)$ conditions in a boosted frame (argued by covariance only); the
   string-level non-vanishing of $V_4(\Psi^4)$ is taken as evident.
4. *What a stronger physicist would see.* That (A.11) is the natural language for the whole
   χ tower: each order adds a source covector, and the closure conditions are Gram-matrix
   conditions on them in the dual form. Whether the $O(g^4)$ source $\nu$ (coefficient of $w$) and
   the $O(g^5)$ conditions also take a Gram form — e.g. $\langle\mu,\nu\rangle$ or $\langle\nu,\nu\rangle$
   fixed — would turn 048's fitted $(c_\chi,d_\chi)$ into geometric statements. Not attempted here.

### Annotation (2026-10-01): H1 after the Addendum

The body above is append-only; H1 is discharged (kinetic clause §2.4 part 0; source clause Addendum
N10). Reading of each remaining reference, by line in the pre-annotation file (the Addendum
insertions above shifted later lines by a few; locate by text):

| Location | Old reading | New reading |
|---|---|---|
| l. 35 (Outcome), l. 88 (root N0), l. 756 (§6.1 heading), l. 761, l. 868 (§6.3) | "conditional on H-B3, H-B4, H-B5, H1" | conditional on H-B3, H-B4, H-B5 (and $b'_\chi=0$ where stated); H1 is a frame convention whose existence is proven |
| l. 134 (`Hypotheses in force`) | H-B3, H-B4, H-B5, H1 | edited: H-B3, H-B4, H-B5 |
| l. 68, l. 102 (N3′), l. 113, l. 348, l. 350, l. 357, l. 367, l. 414, l. 452, l. 647–649 | exclusions of $V_4(\chi,\Psi^{\otimes2})$, $V_4(\chi,\Sigma)$ "by H1" / "rest on H1 alone" | by the §2.4 frame: kinetic diagonalisation (part 0) plus source alignment (N10.4), a frame convention whose existence is proven |
| l. 82 (tree, H1 statement), l. 275 | $a_\chi\lambda_\chi^2<\lambda_\Sigma^2$ | $\lambda_\chi^2<a_\chi\lambda_\Sigma^2$ (corrected in place, N10.7) |
| l. 275–277 ("numbers we choose … under our control") | condition on chosen numbers | numbers constrained to the unit hyperboloid by the $O(g_s^2)$ matching (N10.2); text rewritten in place |
| l. 280–287 (falsifier / discharge paragraph of H1) | H1 fails if … / discharged if … | both falsifier clauses void and discharge achieved (A.5) |
| l. 452 | "(E4) is a frame-independent statement, unlike H1's $j_\chi=0$" | unchanged in content: $j_\chi=0$ is the frame convention of N10.4 |
| Self-review, "weakest step: H1" | H1 | resolved by the Addendum (A.7 item 2 names the remaining dependency, A3/A8) |

