# 042 — Q2: the orientation of the off-shell measure

## 1. Task and objective

**Literal task.** Decide, by derivation, which of two transcriptions of the genus-0
off-shell measure prefactor is correct:

| Label | Source | Prefactor per amplitude | Per complex modulus |
|---|---|---|---|
| **BZ** | Belopolsky–Zwiebach eq. 4.10 | $(\mathrm i/2\pi)^{N-3}$ | $+\mathrm i/2\pi$ |
| **BK** ("book") | Erbin (2023) `bos:eq:omega-p`, read with orientation conventions O1–O4 of SL(2,C) record 039 | $(2\pi\mathrm i)^{-(N-3)}$ | $-\mathrm i/2\pi$ |

Ratio: $(-1)^{N-3}$.

**Motivating objective.** Three documents (this project, the SL(2,C) quartic-vertex
project, Harold's book) must agree on the measure before any of them publishes a number
that depends on it. $C_3$ is untouched; $C_4/C_3^2$, $K_f$ and $\operatorname{sign}
\operatorname{spec}(m_2)$ all flip with the choice, so this is a right/wrong question,
not a convention. The verdict decides which document gets an erratum.

**Hypothesis under test** (from a prior session's memory note, recorded belief, not a
proof): `bos:eq:omega-p` is off by one sign per complex modulus; BZ is consistent.

## 2. Orientation convention declared (O-Q2)

Sign conventions are the whole content here, so the orientation is fixed once, up front,
and cited at every step.

- **OQ1 (complex coordinate).** For a complex modulus $m$, write $m=m_r+\mathrm i m_i$
  with $m_r,m_i$ real, $\bar m=m_r-\mathrm i m_i$.
- **OQ2 (positive orientation).** The ordered pair $(m_r,m_i)$ is positively oriented:
  the volume form on the modulus plane is $\dd m_r\wedge\dd m_i$, and the integration
  region is traversed so that $\int \dd m_r\wedge\dd m_i>0$ for a region of positive
  area. Equivalently $\dd m\wedge\dd\bar m=-2\mathrm i\,\dd m_r\wedge\dd m_i$.
- **OQ3 (area element).** $\dd^2m:=2\,\dd m_r\,\dd m_i$ (Polchinski/Erbin convention),
  to be verified against the book rather than assumed — see §3, input (d).
- **OQ4 (multi-modulus ordering).** For $N-3$ complex moduli $m^{(1)},\dots,m^{(N-3)}$
  the positively oriented real frame is
  $(m^{(1)}_r,m^{(1)}_i,m^{(2)}_r,m^{(2)}_i,\dots)$ — pairs kept adjacent and in the
  order $r$ then $i$. This is the ordering that makes the $N$-dependence a pure
  $(N-3)$-th power, and it is the ordering under which the two candidates differ by
  exactly $(-1)^{N-3}$.
- **OQ5 (contour).** Contours $C_\alpha$ are traversed with the $\sigma_\alpha$
  coordinate patch on the left (the book's stated rule, l. 133), i.e.
  counterclockwise in $\sigma_\alpha$ around the puncture at $\sigma_\alpha=0$, so that
  $\oint\frac{\dd\sigma}{2\pi\mathrm i}\sigma^{-1}=+1$.

These are **conventions** (free, cannot be wrong). The prefactor, once they are fixed, is
a **transcription** (a claim, can be wrong).

## 3. Inputs the $N=4$ derivation needs

- (a) The book's $B_s$ (`bos:eq:beltrami-form`), including the $1/2\pi\mathrm i$ already
  inside the contour integral, and where the same normalisation sits in BZ's $B$ —
  needed to know whether the two prefactors are even measured in the same units.
- (b) The decomposition of $B_{m_r},B_{m_i}$ into holomorphic/antiholomorphic
  $\mathcal B,\bar{\mathcal B}$, and the Grassmann reordering that produces the factor
  $-2\mathrm i$.
- (c) The action of $\mathcal B\bar{\mathcal B}$ on a puncture-position modulus, i.e.
  $b_{-1}\bar b_{-1}$ stripping $c\bar c$ from $\mathcal V=c\bar c V$, with its sign.
- (d) The book's definition of $\dd^2 z$ — settled: $\dd^2z=2\,\dd x\,\dd y$ and the normalisation of the on-shell genus-0
  $N$-point amplitude it must reproduce — the *independent* anchor that fixes the
  prefactor (free-constant rule: the prefactor must not be fitted from
  $C_4/C_3^2$, the identity under test).
- (e) The base correlator normalisation $\langle c_{-1}\bar c_{-1}c_0^-c_0^+c_1\bar
  c_1\rangle=-\tfrac12$ (R43) and $N_{\rm gh}$ conventions.
- (f) SL(2,C) record 039 §6–§7 (O1–O4) — to state whether this derivation is
  independent of R37 or inherits from it.

## 4. $N=4$: the prefactor from the on-shell reduction

### Setup

Assumptions in force: OQ1–OQ5 (§2), the project conventions of R43, genus 0, $N=4$,
external states on-shell, $\mathscr V_i=c\bar cV_i$ with $V_i$ a matter primary of weight
$(1,1)$. Punctures $1,2,3$ fixed at $z_1,z_2,z_3$; the single complex modulus is the
position $z_4=x+\mathrm i y$ of the fourth puncture. Local coordinates $F_i(w)=z_i+w$
(trivial; on-shell the $f_i$-dependence drops out of the correlator, so this is no loss).

Two symbols are kept free and are the whole subject of the derivation:

- $\kappa$, the **phase of the measure prefactor per complex modulus**, i.e. the prefactor
  is $\kappa/2\pi$ per complex modulus. BZ claims $\kappa=+\mathrm i$; the book's
  `bos:eq:omega-p` claims $\kappa=-\mathrm i$ (since $(2\pi\mathrm i)^{-1}=-\mathrm i/2\pi$).
- $\eta$, the **antiholomorphic contour convention**, defined by
  $$\oint_{C}\frac{\dd\bar w}{2\pi\mathrm i}\,\bar w^{-n-2}=:\eta\,\delta_{n,-1},
  \qquad \eta=\pm1. \tag{4.1}$$

$\eta$ is a convention (free), $\kappa$ is a transcription (a claim). **Free-constant
discipline:** neither is fitted from $C_4/C_3^2$, $K_f$, or any SL(2,C) quantity; the
independent anchor is the Faddeev–Popov gauge-fixed on-shell amplitude, step (e) below.

### Derivation

**(a) The value of $\eta$ under the book's own contour rule.** The book states
(`bos_offshell_amplitudes.tex` l. 85) "The contours run anti-clockwise", and writes the
antiholomorphic piece of $B(V)$ as $\oint_C\frac{\dd\bar z}{2\pi\mathrm i}\bar b(\bar
z)\bar v(\bar z)$ over that same contour $C$. Taken literally — $\dd\bar z$ the honest
differential of $\bar z$ along an anticlockwise circle — parametrise $w=r\e^{\mathrm
i\theta}$, $\theta:0\to2\pi$, so $\bar w=r\e^{-\mathrm i\theta}$,
$\dd\bar w=-\mathrm i r\e^{-\mathrm i\theta}\dd\theta$:
$$\oint\frac{\dd\bar w}{2\pi\mathrm i}\,\bar w^{-n-2}
 =\frac{1}{2\pi\mathrm i}\int_0^{2\pi}\!\!(-\mathrm i r\e^{-\mathrm i\theta})\,
   r^{-n-2}\e^{\mathrm i(n+2)\theta}\dd\theta
 =-\frac{r^{-n-1}}{2\pi}\int_0^{2\pi}\!\!\e^{\mathrm i(n+1)\theta}\dd\theta
 =-\delta_{n,-1}. \tag{4.2}$$
Hence the **literal anticlockwise reading gives $\eta=-1$**. The alternative, widespread
reading — treat $\bar w$ as an independent variable with its own anticlockwise contour, so
that $\oint\frac{\dd\bar w}{2\pi\mathrm i}=+\Res_{\bar w}$ — gives $\eta=+1$. This is O3 of
the SL(2,C) record 039. Both are legitimate conventions; they are **not** the same
convention, and the book never says which it means.

**(b) The two $B$'s of the modulus $z_4$.** With $F_4(w)=z_4+w$ the Schiffer vectors are
$\partial F_4/\partial x=1$, $\partial F_4/\partial y=\mathrm i$, and their conjugates
$\partial\bar F_4/\partial x=1$, $\partial\bar F_4/\partial y=-\mathrm i$. Insert in
`bos:eq:beltrami-form`, writing $\mathcal B:=\oint\frac{\dd w}{2\pi\mathrm i}b(w)=b_{-1}$
and $\bar{\mathcal B}:=\oint\frac{\dd\bar w}{2\pi\mathrm i}\bar b(\bar w)=\eta\,\bar
b_{-1}$ by (4.1):
$$B_x=b_{-1}+\eta\,\bar b_{-1},
\qquad
B_y=\mathrm i\big(b_{-1}-\eta\,\bar b_{-1}\big). \tag{4.3}$$

**(c) The product, in the order $B_xB_y$ fixed by OQ4.** Using $b_{-1}^2=\bar b_{-1}^2=0$
and $\bar b_{-1}b_{-1}=-b_{-1}\bar b_{-1}$:
$$B_xB_y
 =\mathrm i\big(b_{-1}+\eta\bar b_{-1}\big)\big(b_{-1}-\eta\bar b_{-1}\big)
 =\mathrm i\big(-\eta\,b_{-1}\bar b_{-1}+\eta\,\bar b_{-1}b_{-1}\big)
 =-2\mathrm i\,\eta\;b_{-1}\bar b_{-1}. \tag{4.4}$$
This is the step that carries the $\dd m\wedge\dd\bar m=-2\mathrm i\,\dd m_r\wedge\dd m_i$
factor named in the brief: the $-2\mathrm i$ of (4.4) is the same $-2\mathrm i$, appearing
on the ghost side rather than on the measure side. For $\eta=+1$, (4.4) reads
$B_xB_y=+2\mathrm i\,\bar b_{-1}b_{-1}$, which is 039's stated form — my algebra and 039's
agree at this step.

**(d) The action on the fourth puncture.** $\mathscr V_4=c\bar cV_4$ corresponds to
$c_1\bar c_1\lvert V_4\rangle$. With $\{b_m,c_n\}=\delta_{m+n,0}$, $b_{-1}\lvert
V\rangle=\bar b_{-1}\lvert V\rangle=0$, and $b_{-1}$ anticommuting with $\bar c_1$:
$$\bar b_{-1}c_1\bar c_1\lvert V_4\rangle=-c_1\bar b_{-1}\bar c_1\lvert V_4\rangle
 =-c_1\lvert V_4\rangle,
\qquad
b_{-1}\bar b_{-1}c_1\bar c_1\lvert V_4\rangle=-\lvert V_4\rangle. \tag{4.5}$$
The $B$'s stand to the left of all $\mathscr V_i$ in `bos:eq:omega-p`; $B_xB_y$ is
Grassmann-even and each $\mathscr V_i=c\bar cV_i$ is Grassmann-even, so moving the pair
onto puncture 4 costs no sign. With (4.4),
$$\big\langle B_xB_y\,\textstyle\prod_{i=1}^4\mathscr V_i\big\rangle
 =(-2\mathrm i\eta)(-1)\big\langle c\bar cV_1\,c\bar cV_2\,c\bar cV_3\,V_4(z_4)\big\rangle
 =2\mathrm i\eta\,\big\langle\cdots V_4\big\rangle. \tag{4.6}$$

**(e) Assembling the 2-form and integrating.** With the prefactor $\kappa/2\pi$ and OQ2
($\int\dd x\wedge\dd y=+\int\dd x\,\dd y$), and with $\dd^2z=2\,\dd x\,\dd y$ (the book's
convention, `bos_path_integral_closed_complex.tex` l. 124–126: $\dd^2x=\tfrac12\dd^2z$,
$\dd^2z=\dd z\,\dd\bar z$ — this confirms OQ3):
$$\int_{\mathcal S_{0,4}}\omega_2
 =\frac{\kappa}{2\pi}\,2\mathrm i\eta\int\dd x\,\dd y\,\langle\cdots V_4\rangle
 =\frac{\kappa\,\mathrm i\,\eta}{2\pi}\int\dd^2z_4\,\langle\cdots V_4\rangle
 =\frac{\kappa\,\mathrm i\,\eta}{2\pi}\;A^{\rm FP}_{0,4}. \tag{4.7}$$

### Commentary

- (4.2): the only input is that $\dd\bar z$ is the differential of $\bar z$ along the
  *same* anticlockwise contour. This is where the ambiguity lives, and it is invisible in
  the formula as printed.
- (4.4): the two binary choices — order $B_xB_y$ vs $B_yB_x$ (OQ4) and the sign of $\eta$ —
  enter only through their product; the sign of the Schiffer vector $v$ drops out because
  two $B$'s appear (039 O3 makes the same remark).
- (4.6)–(4.7): $A^{\rm FP}_{0,4}:=\int\dd^2z_4\langle\prod_{i\le3}c\bar cV_i\,V_4\rangle$
  is the book's own on-shell four-point amplitude (`bos_offshell.tex` l. 151), i.e. the
  Faddeev–Popov gauge-fixed Polyakov amplitude with three punctures fixed. It is the
  anchor, and it is independent of everything under test.

### Result

$$\boxed{\;\int_{\mathcal S_{0,4}}\omega_2\Big|_{\text{on-shell}}
 =\frac{\kappa\,\mathrm i\,\eta}{2\pi}\;A^{\rm FP}_{0,4}\;}\tag{4.8}$$

Only the **product** $\chi:=\kappa\,\mathrm i\,\eta\in\{+1,-1\}$ is observable. Table of
the four readings:

| Prefactor | $\oint\dd\bar w/2\pi\mathrm i$ | $\kappa$ | $\eta$ | $\chi=\kappa\mathrm i\eta$ |
|---|---|---|---|---|
| BZ $(\mathrm i/2\pi)$ | literal anticlockwise | $+\mathrm i$ | $-1$ | $+1$ |
| BZ $(\mathrm i/2\pi)$ | $+\Res_{\bar w}$ (039 O3) | $+\mathrm i$ | $+1$ | $-1$ |
| Book $(2\pi\mathrm i)^{-1}$ | literal anticlockwise | $-\mathrm i$ | $-1$ | $-1$ |
| Book $(2\pi\mathrm i)^{-1}$ | $+\Res_{\bar w}$ (039 O3) | $-\mathrm i$ | $+1$ | $+1$ |

**This is the central finding.** The rows are not four claims about one quantity: they are
two claims ($\chi=\pm1$) reached by two independent binary choices. The book's prefactor
read with the book's own stated contour rule (row 3) and BZ's prefactor read with 039's O3
(row 2) give the **same** $\chi=-1$. The $(-1)^{N-3}$ discrepancy of the brief is
reproduced exactly by flipping *either* $\kappa$ *or* $\eta$ — which is why comparing the
two printed prefactors without also comparing the two contour conventions is not a
well-posed comparison.

### Verification

`codes/verify-q2-orientation.py`, 16 named checks, 0 FAIL, seed 20260922, 4 break
controls that all fire. Checked: (4.2) by direct numerical contour integration for
$n=-3\ldots1$ at five radii;
(4.3)–(4.4) by symbolic Grassmann algebra in an explicit $4$-dimensional ghost
representation; (4.5) in the same representation; the $\mathrm i$-counting of (4.7); the
$N=5$ power law of §5; and the reality constraint of §5.3. Not machine-checkable and not
claimed: the value of $\chi$ itself (§6).

## 5. General $N$, and the checks

### 5.1 $N=5$ and the pure power

For $N$ punctures the moduli are the positions $z_4,\dots,z_N$, $N-3$ complex moduli.
Under OQ4 the positively oriented real frame is
$(x_4,y_4,x_5,y_5,\dots)$ and the component of the top form is
$$\omega_{2(N-3)}\big(\partial_{x_4},\partial_{y_4},\dots\big)
 =\Big(\frac{\kappa}{2\pi}\Big)^{N-3}
   \big\langle (B_{x_4}B_{y_4})(B_{x_5}B_{y_5})\cdots\textstyle\prod_i\mathscr V_i
   \big\rangle. \tag{5.1}$$
Each pair $B_{x_j}B_{y_j}$ is a contour pair around puncture $j$ only, is Grassmann-even,
and therefore commutes past every other pair and past every $\mathscr V_i$ (also
Grassmann-even). Each pair contributes the factor $2\mathrm i\eta$ of (4.6) on its own
puncture, independently:
$$\int_{\mathcal S_{0,N}}\omega_{2(N-3)}\Big|_{\text{on-shell}}
 =\Big(\frac{\kappa\,\mathrm i\,\eta}{2\pi}\Big)^{N-3} A^{\rm FP}_{0,N},
\qquad
A^{\rm FP}_{0,N}=\int\prod_{j=4}^{N}\dd^2z_j\,
 \Big\langle\prod_{i=1}^{3}c\bar cV_i\prod_{j=4}^{N}V_j\Big\rangle. \tag{5.2}$$
At $N=5$ this is $\chi^2/(2\pi)^2=+1/(2\pi)^2$: the sign is a **pure power of $\chi$**,
with no extra $N$-dependent sign from the Grassmann reordering. Verified explicitly for
$N=5$ in the companion script (the two pairs commuted in both orders). The result holds
for all $N\ge3$ at genus 0 by the same argument; nothing in it is special to $N=4,5$.

### 5.2 Limiting case $N=3$

$N-3=0$: prefactor $1$, no $B$'s, $\omega_0=\langle\mathscr V_1\mathscr V_2\mathscr
V_3\rangle=A^{\rm FP}_{0,3}$. Both transcriptions and both $\eta$'s agree, as they must:
$C_3$ is untouched. ✓

### 5.3 Reality / $\mathrm i$-counting

$A^{\rm FP}_{0,N}$ and $\int\omega$ must be proportional by a *real* factor (the amplitude
is real-analytic in the momenta; no convention introduces a stray phase). From (5.2) this
forces $\kappa\,\mathrm i\,\eta\in\mathbb R$, i.e. $\kappa\in\{\pm\mathrm i\}$ for
$\eta=\pm1$. This is an independent confirmation that the prefactor's phase per complex
modulus must be $\pm\mathrm i$ — it rules out $1/2\pi$, $-1/2\pi$, and any other phase, and
it is the reason both sources carry an $\mathrm i$. It does **not** choose the sign.

### 5.4 Dimensions

The prefactor is dimensionless; $B_s$ carries the dimension of $\partial x_s$ inverse,
matched by $\dd x_s$; $\alpha'$ never enters. Both candidates are dimensionally
identical, as expected — the dispute is a pure phase. ✓

## 6. Verdict

**Q2 as posed — "which of the two printed prefactors is the correct transcription?" — has
no answer, because the two printed prefactors are not statements about the same quantity.**
The observable is $\chi=\kappa\,\mathrm i\,\eta$ of (4.8); a prefactor without a declared
$\oint\dd\bar w/2\pi\mathrm i$ convention determines no physics. This is a genuine
resolution, not a failure to decide: the derivation shows that the $(-1)^{N-3}$ in dispute
is produced identically by the two conventions, so the disagreement between the two
documents is a disagreement of *reading*, not of fact.

The well-posed remainder, and its answer:

1. **Is the book internally in conflict with BZ?** No. Read with the book's own stated
   contour rule ("the contours run anti-clockwise", l. 85, with $\dd\bar z$ literal, hence
   $\eta=-1$ by (4.2)), `bos:eq:omega-p` gives $\chi=-1$ — the same $\chi$ that the SL(2,C)
   project obtained from BZ's $\kappa=+\mathrm i$ read with O3 ($\eta=+1$). **The book and
   BZ agree**; the apparent $(-1)^{N-3}$ conflict came from reading the book's prefactor
   with 039's $\eta=+1$, which is not the book's own convention.
2. **What is the value of $\chi$?** $\chi=-1$, i.e. $\int\omega=(-1/2\pi)^{N-3}A^{\rm
   FP}_{0,N}$, on the strength of SL(2,C) 039 §6–§7 (two routes: the Feynman region
   reproducing the exchange term of the action, and the tachyon-pole residue of the
   on-shell four-point function), promoted as R37 `Verified`. **This clause is not
   independent of R37** — see §6.1. Rows 2 and 3 of the §4 table both give $\chi=-1$, so
   this clause is *consistent with* both sources read in their own conventions, but the
   derivation here does not re-derive the value.
3. **Is there an erratum in the book?** Not an error — an **ambiguity**. `bos:eq:omega-p`
   is correct under the book's own contour rule. What is missing is an explicit statement
   of the $\oint\dd\bar w/2\pi\mathrm i$ convention next to `bos:eq:B-form-V`, without which
   a reader who adopts $+\Res_{\bar w}$ (a common convention, and the one 039 adopted)
   obtains the wrong sign per complex modulus. Proposed text in §7.

The book's TODO at l. 137 asks for a check of the sign of the
measure $\dd m_r\wedge\dd m_i$ and is consistent with this: with $\eta=-1$ the prefactor is
$-\mathrm i/2\pi=(2\pi\mathrm i)^{-1}$, "the minus", precisely when the measure is written
as $\dd m_r\wedge\dd m_i$ (OQ2/OQ4). The external remark on the minus sign and the book's printed form agree. Used
as a cross-check only, not as evidence.

### 6.1 Independence from R37

- **Independent of R37**: the entire content of §4 and §5 — the identity (4.8), the
  entanglement of $\kappa$ with $\eta$, the table, the value $\eta=-1$ implied by the
  book's own contour rule, and the pure-power law. None of these use 039, $C_4$, $K_f$,
  the plumbing fixture, or the exchange term. The anchor is the Faddeev–Popov amplitude.
- **Inherits from R37**: only clause 2 of the verdict, the numerical value $\chi=-1$. My
  anchor fixes $\int\omega=\chi\,(2\pi)^{-1}A^{\rm FP}$ per modulus, i.e. it fixes the
  magnitude $1/2\pi$ and the reality of $\chi$, but not its sign: the sign requires knowing
  whether the SFT normalisation of $A_{0,N}$ is $+$ or $-$ relative to the Faddeev–Popov
  one, and that is fixed by the exchange-term comparison (039 route (a)) or the
  factorisation residue (039 route (b)), neither of which is redone here.
- Consequently the verdict of §6 clause 1 — the part that decides whether any document
  needs correcting — is **independent of R37**, and clause 2 is not.

### 6.2 The literal reading, confirmed by citation — N6 closed

Clause 1 rests on one reading: that in `bos:eq:B-form-V` the symbol $\dd\bar z$ means the
differential of $\bar z$ along the anticlockwise contour the book declares, hence
$\eta=-1$ by (4.2). This was, until now, the literal reading of what is printed, and the
only reading under which the book's own words at l. 85 do any work — but a reading of an
unstated convention, for which only the author could confirm the intent.

**It is now confirmed twice over, in print, by the book's own author.** de Lacroix, Erbin,
Kashyap, Sen, Verma (2017), *Closed Superstring Field Theory and its Applications*,
arXiv:1703.06410, IJMPA 32 (2017) 1730021 (`deLacroix:2017:ClosedSuperstringField`), states
the decisive line in its appendix (around eq. (B.5)):

> "According to the convention described in §2.2 the coordinate systems $w^a$ will be on
> the left of $C^a$ for $1\le a\le4$. Therefore, the contour $C^a$ runs anti-clockwise
> around $v_a$. Integration over holomorphic coordinates is accompanied by a factor of
> $(2\pi\mathrm i)^{-1}$ and integration over antiholomorphic coordinates is accompanied by
> a factor of $(-2\pi\mathrm i)^{-1}$."

The explicit minus on the antiholomorphic factor is exactly $\eta=-1$. A supporting line,
below eq. (3.3), states the same convention for a single contour: "where $\oint$ includes a
factor of $1/2\pi\mathrm i$ and the integration is carried out over an anti-clockwise
contour." The phrase invoked in the first quotation — "the coordinate systems will be on
the left of $C^a$" — is the *same* convention statement the book itself makes at
`chapters/bos_offshell_amplitudes.tex` l. 133 ("the contour orientations are defined by
having the $\sigma_\alpha$ coordinate system on the left"). The two documents share the
convention, so this citation fixes the book's own $\eta$, not merely a second opinion.

(The other citation, `deLacroix:2017:LecturesNotesSuperstring`, "Lectures Notes on
Superstring Perturbation Theory", for an "example 3.5, pages 31–32", is a *different*
document from arXiv:1703.06410 and was not checked — its example is correctly absent from
1703.06410. It is not needed: the confirmation above is already decisive.)

**Consequence.** The reading is no longer an assumption resting on the author's intent alone —
it is stated in print. Clause 1 of §6 stands unconditionally: the book and BZ agree,
$\eta=-1$, and **the book needs no erratum — only the clarification sentence already
drafted in §7.** Row 4 of the §4 table ($\eta=+1$) is excluded; the erratum branch this
subsection used to flag as the alternative does not occur. N6 (claim tree, below) is
closed on this point.

## 7. Consequences per project

### This project (Cubic closed SFT)

Nothing changes. Record 041 found Q2 "nearly inert" here and that is confirmed: with
$\chi=-1$, the branch that 041 calls **branch A** (BZ, $C_4<0$ on the potential side) is
the one in force. The single Q2-dependent word left unapplied by 041 §5.1 item 6 —
"negative" in the "negative potential-side" entry of
`knowledge/topics/sl2c-data-request-2026-09-22.md` §1 — **stands as written**; the Q2 caveat
on it can be dropped rather than added. R15's statement is unchanged (041 §4.3); clause (3)
"sign open" closes as $C<0$, so the Schwinger form to use is the unconditional
$\int_0^\infty\dd t\,m_2\e^{-tm_2^2}$.

### SL(2,C) quartic vertex project (read-only; these are requests, not edits)

R8, R30, R36, R37, R41, R49 all stand: their $\chi=-1$ is confirmed as the value consistent
with the book read in the book's own convention. Two wording requests:

- 039 §7.5's footnote-ready statement says the book's form "would give $C_4>0$ and
  $K_f=-1$". That is true *only* under O3 ($\eta=+1$), and O3 is not the book's convention.
  The footnote should instead read that the book's $(2\pi\mathrm i)^{-(N-3)}$ and BZ's
  $(\mathrm i/2\pi)^{N-3}$ **agree** once each is read with its source's
  $\oint\dd\bar w/2\pi\mathrm i$ convention, and that the project adopts $\eta=+1$ with
  BZ's prefactor, i.e. $\chi=-1$. As written the footnote asserts a conflict with the book
  that does not exist.
- 039 O3 should state $\eta=+1$ explicitly as a *choice* (it does say "$\oint
  \dd\bar w/2\pi\mathrm i$ read as $+\Res_{\bar w}$", which is exactly $\eta=+1$ — the
  addition needed is only the remark that the book's literal reading is $\eta=-1$, so that
  the pairing with BZ's prefactor is not mistaken for a disagreement with the book).
- The line-number drift already noted in 041 (039 cites l. 131 for the TODO; it is l. 137)
  is unchanged.

### The book

No erratum to the equation. One clarification, proposed for
`chapters/bos_offshell_amplitudes.tex` near `bos:eq:B-form-V` (l. 79–86):

> The contours run anti-clockwise, and $\dd\bar z$ denotes the differential of $\bar z$
> along that same contour, so that $\oint_C\frac{\dd\bar z}{2\pi\mathrm i}\,\bar
> z^{-n-2}=-\delta_{n,-1}$ (and not $+\delta_{n,-1}$, as would follow from treating
> $\bar z$ as an independent variable with its own anti-clockwise contour). With this
> convention $B(\partial_{m_r})B(\partial_{m_i})=+2\mathrm i\,b_{-1}\bar b_{-1}$ for a
> puncture-position modulus $m=m_r+\mathrm i m_i$, and the normalisation $(2\pi\mathrm
> i)^{-\mathcal M^c_{g,n}}$ of \eqref{bos:eq:omega-p} is the one for which
> $\int\omega$ reproduces the gauge-fixed amplitude with $\dd m_r\wedge\dd m_i$ positively
> oriented.

The TODO at l. 137 can then be discharged: the minus whose sign the TODO asks to check is the one already in
$(2\pi\mathrm i)^{-1}$, and it is correct given the contour convention above.

## Claim tree

Assumptions: OQ1–OQ5 (§2); R43 conventions; genus 0; on-shell external states;
trivial local coordinates (no loss on-shell).

- **Root R**: $\displaystyle\int_{\mathcal S_{0,N}}\omega_{2(N-3)}\big|_{\rm on-shell}
  =\big(\kappa\mathrm i\eta/2\pi\big)^{N-3}A^{\rm FP}_{0,N}$, hence the observable is
  $\chi=\kappa\mathrm i\eta$ and the two printed prefactors do not conflict once each is
  read with its own contour convention. — **Proven**, from N1–N5.
  - **N1**: the book's stated anticlockwise rule taken literally gives $\eta=-1$,
    eq. (4.2). — Proven (direct computation); verified `Q2-N1-ETA-LITERAL`.
  - **N2**: $B_x=b_{-1}+\eta\bar b_{-1}$, $B_y=\mathrm i(b_{-1}-\eta\bar b_{-1})$,
    eq. (4.3), from `bos:eq:beltrami-form` with $F_4(w)=z_4+w$. — Proven; verified
    `Q2-N2-B-DECOMPOSITION`.
  - **N3**: $B_xB_y=-2\mathrm i\eta\,b_{-1}\bar b_{-1}$, eq. (4.4). — Proven from N2;
    verified `Q2-N3-BXBY`. Agrees with 039's $2\mathrm i\bar b_{-1}b_{-1}$ at $\eta=+1$.
  - **N4**: $b_{-1}\bar b_{-1}c_1\bar c_1\lvert V\rangle=-\lvert V\rangle$, eq. (4.5). —
    Proven; verified `Q2-N4-GHOST-STRIP` in an explicit representation.
  - **N5**: the $N$-dependence is the pure power $(\kappa\mathrm i\eta/2\pi)^{N-3}$,
    eq. (5.2). — Proven from N3, N4 and Grassmann parity; verified `Q2-N5-PURE-POWER` at
    $N=5$.
  - **N6** (separate, *not* used by R): $\chi=-1$. — **Inherited** from SL(2,C) R37
    (`Verified` there, two routes); **not re-derived here**. Consistent with N1+book, and
    that consistency now rests on a literature-confirmed reading rather than an assumed one
    (§6.2, de Lacroix–Erbin–Kashyap–Sen–Verma 2017,
    `deLacroix:2017:ClosedSuperstringField`); also consistent with 039's O3+BZ. — Closed.

Open gaps: none. N1–N5 are proven. N6's only pending item — the literal-reading assumption
that the record's §6.2 could not close without the author — is now confirmed by citation
(§6.2); it is no longer open. N6's numeric value $\chi=-1$ remains, by design, anchored to
SL(2,C) R37 rather than re-derived here (§6.1): that is a scope choice made when this
record was written, not an open question.
Hypotheses in force: none.

## Status

Complete. §4 ($N=4$), §5 ($N=5$ and general $N$), §6 (verdict), §7 (consequences) written;
claim tree closed; companion script `codes/verify-q2-orientation.py` run, 16 PASS / 0 FAIL.
N6's one open item — the literal-reading assumption of §6.2 — is now confirmed by citation
(de Lacroix–Erbin–Kashyap–Sen–Verma 2017, `deLacroix:2017:ClosedSuperstringField`); no
erratum needed, only the clarification text of §7. Nothing else changes.
Next: orchestrator — relay the two wording requests to the SL(2,C) project and the
clarification text to the book.
