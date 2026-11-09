# 046 — Stage 0: the three-tachyon coupling $\{T^3\}(\beta)$ in this project's normalisation

## Status

Complete, with the critic findings of `agent/reports/critic-046-20260921T215500.md` applied
(fix pass `fix-046-20260921T220600`; S4 added `C1.3-c0pm-factor`, rebuilt the parity check,
and added the controls `BREAK-WRONG-PAIRING`, `BREAK-WRONG-C0PM`; `C1.5-sister-J-consistent`
added for C2; A5 relabelled H1). No number changed.
Next: none — the record is final; the orchestrator's action is the `R43` restatement of §4.5.

## 0. Task and objective

**Literal task.** Recompute the off-shell three-tachyon coupling at the SL(2,C) cubic
vertex, $\{T^3\}(\beta)=C_3\beta^6$, end to end in this project's normalisation — from the
book's sphere vacuum normalisation $\langle c_{-1}\bar c_{-1}c_0\bar c_0c_1\bar c_1\rangle=-1$
and the cubic mapping radii $\rho_a=1/\beta$ — and compare the number with the companion
SL(2,C) computation's value for it (`SL: R3`; value from the companion computation, not
reproduced here).

**Motivating objective.** `R43` (record 041) declares the sister → book conversion
$\lambda=\tfrac12$ per sphere correlator. Its *sign* is fixed by two independent routes; its
*magnitude* comes out of the two normalisation declarations tautologically, so the old spec's
clause "verify the table on one shared quantity" is unmet and the sister's `conventions.md`
D1 carries our row as `translation: pending`. Stage 0 is the cheapest shared quantity: both
projects publish a number for it. Closing it turns `R43` from a restatement of two
declarations into a result, and every magnitude imported from the sister project then rests
on something checked.

**What this check can and cannot settle — stated before the computation, not after.**
$\lambda$ *is* the ratio of the two declared vacuum normalisations, so no computation can
determine it from outside those declarations. What a genuine end-to-end recomputation does
test, and what would refute `R43` if it came out otherwise:

1. the **$\lambda$-weight** of $\{T^3\}$ — that it is one sphere correlator, hence $\lambda^1$
   and not $\lambda^2$ or $\lambda^0$ (this is exactly the point on which the earlier
   "factor 2 per strand" rule over-corrected $V_4$);
2. that the **geometric factor** — mapping radii, puncture separations, the treatment of the
   puncture at infinity — is identical on the two sides and contributes $1$, not $27$ or
   $64/27$ (a live possibility: a prescription-dependent factor could arise from the
   branched Witten cubic vertex);
3. that **no further convention** (matter-sector normalisation, momentum delta / volume
   factor, the vertex-to-potential dictionary) differs between the two sides and hides a
   factor in the comparison;
4. the **sign**.

If (1)–(4) all hold and the numbers stand in ratio $\tfrac12$, `R43`'s magnitude is
confirmed in the only sense in which it is confirmable. Any other ratio refutes it.

## 1. The amplitude, written out

The off-shell $n$-point amplitude of closed bosonic SFT, in the book's form
([Erbin 2023], `bos_offshell_amplitudes` eq. at l. 221, local coordinates $f_i$):

$$\{\mathcal V_1\cdots\mathcal V_n\}
 =\Big\langle\ \prod_{i=1}^n f_i\circ\mathcal V_i(0)\ \Big\rangle_{\Sigma_{0,n}} .\tag{1.1}$$

For $n=3$ there is no moduli integral: $\mathcal M_{0,3}$ is a point and the three punctures
are fixed by SL(2,C).

The closed tachyon state is $|T(k)\rangle=c_1\bar c_1|k\rangle$, i.e. the vertex operator
$\mathcal V_T(k;z)=c\bar c\,\e^{\I k\cdot X}(z)$, a primary of weight

$$h=\bar h=\frac{\alpha'k^2}{4}-1 .\tag{1.2}$$

For a primary, $f\circ\mathcal O(0)=\big(f'(0)\big)^h\big(\overline{f'(0)}\big)^{\bar h}\,
\mathcal O(f(0))$, so with $\rho_a:=f_a'(0)$ and $h=\bar h$ real the dressing is

$$\prod_a \rho_a^{h}\bar\rho_a^{\bar h}=\prod_a|\rho_a|^{2h}
 =\prod_a|\rho_a|^{\alpha'k_a^2/2-2}.\tag{1.3}$$

Hence

$$\{T^3\}=\Big(\prod_{a=1}^3|\rho_a|^{\alpha'k_a^2/2-2}\Big)\,
 \big\langle c\bar c\,\e^{\I k_1X}(z_1)\,c\bar c\,\e^{\I k_2X}(z_2)\,
 c\bar c\,\e^{\I k_3X}(z_3)\big\rangle .\tag{1.4}$$

### 1.1 Which kinematics — zero momentum, not on shell

The on-shell condition $\alpha'k_a^2=4$ and a $\beta$-dependent coupling are incompatible,
and it is the on-shell reading that must go: $\{T^3\}(\beta)=C_3\beta^6$ is **not** the
on-shell coupling.

- On shell, $\alpha'k^2=4$ gives $h=\bar h=0$ by (1.2), the dressing (1.3) is $1$, and
  $\{T^3\}$ is $\beta$-independent. This is required — the on-shell three-point function is a
  physical S-matrix element and cannot depend on the stub length. `SL: R3` says the same.
- The quantity both projects publish is the **zero-momentum off-shell** coupling, the
  coefficient of $\tau^3$ in the tachyon potential: $k_a=0$, $h=\bar h=-1$, dressing exponent
  $\alpha'k^2/2-2=-2$ per puncture. That is where the six powers of $\beta$ live. It is also
  what makes the quantity *prescription-dependent* (`SL: R3`), which is harmless here because
  both sides use the same prescription — and is precisely why it is a good convention probe.

The same counting checks against $\{T^4\}$: four punctures at zero momentum carry
$\beta^{8}$, which is the $\beta^8$ of `R15` clause (3).

So the computation below is at $k_a=0$, $h=\bar h=-1$, and §1.2 records the exponent as a
derived quantity, not a quoted one.

### 1.2 Factors to be tracked

Every factor that could carry a convention difference, and where it is fixed:

| # | Factor | Fixed by | Status |
| --- | --- | --- | --- |
| F1 | Sphere ghost vacuum normalisation $\nu$ | book `bos:eq:ws-closed-vacuum-normalization` | the convention under translation |
| F2 | $c_0^\pm=\tfrac12(c_0\pm\bar c_0)$, $b_0^\pm=b_0\pm\bar b_0$, ordering $c_0^-c_0^+$ | book `cft:eq:bn-cn-pm`; BZ eq. 2.7 | identical on both sides (`R43`) |
| F3 | Dressing exponent $\alpha'k^2/2-2$ at $k=0$ | (1.2)–(1.3) | derived here |
| F4 | Mapping radii $\rho_a$ of the cubic maps | the SL(2,C) cubic-vertex construction (geometry, not a convention) | computed here |
| F5 | Puncture separations $\lvert z_{12}z_{13}z_{23}\rvert^2$ and the $\infty$ puncture | SL(2,C) frame | computed here, three frames |
| F6 | Matter zero-momentum factor / momentum delta $(2\pi)^D\delta^D(0)$ | book normalisation; stripped as the volume $V_D$ | hypothesis H1, identical on both sides |
| F7 | Interleaved $\to$ separated ghost reordering sign | 041 (3.5)–(3.6) | cancels; imported as a *result*, re-checked |
| F8 | Vertex-to-potential dictionary and overall $V=-S$ sign | sister `SL: R8` | common to both sides, cancels in the ratio |

**No constant is fitted.** F1 comes from the book, F4–F5 from the maps, F3 from the weight.
Nothing is taken from the ratio under test. F8 is the one place where a sign is *inherited*
rather than derived, and §4 states exactly what that does and does not cost.

## 2. Map data

\subsection*{Setup}

A1, A3 (assumptions and hypotheses are listed in the claim tree at the end of the record).
$\rho_a:=f_a'(0)$ in the $z$-chart for the finite punctures; for the puncture at
$z=\infty$ the radius is taken in the chart $u=1/z$, i.e. $\rho_\infty:=\frac{d}{dw}(1/f_\infty)(0)$.

\subsection*{Derivation}

$$f_0'(w)=\frac{4\beta}{(2\beta+w)^2},\qquad
 f_1'(w)=-\frac{4\beta}{(2\beta+w)^2},\qquad
 \frac{1}{f_\infty(w)}=\frac{2w}{2\beta+w}=f_0(w),\tag{2.1}$$

$$\rho_0=\frac1\beta,\qquad \rho_1=-\frac1\beta,\qquad \rho_\infty=\frac1\beta,
 \qquad |\rho_a|=\frac1\beta\ \ \forall a.\tag{2.2}$$

\subsection*{Commentary}

(2.1): the identity $1/f_\infty=f_0$ is exact, not asymptotic, so the $\infty$ puncture is a
puncture of exactly the same local geometry as the other two — the three-punctured sphere is
symmetric, as it must be for a cyclic cubic vertex.

(2.2): $\rho_1$ is negative. This is a phase of the local coordinate, not a sign of the
amplitude: since $h=\bar h$ is a real integer, the dressing sees only
$\rho_1^{h}\bar\rho_1^{\bar h}=|\rho_1|^{2h}$. Writing $\prod_a|f_a'(0)|^{h+\bar h}$, as the
sister derivation does, is therefore legitimate here and would not be for $h\neq\bar h$.

\subsection*{Result}

$$\prod_{a}|\rho_a|^{-2}=\beta^6\quad\text{in the }(0,1,\infty)\text{ frame.}\tag{2.3}$$

**This number alone is meaningless.** The mapping radius is not SL(2,C)-invariant: under a
global Möbius map $\gamma$ applied to all three local coordinates, $\rho_a\to\gamma'(z_a)\rho_a$.
The $(0,1,\infty)$ frame is exactly the frame in which two of the three puncture separations
diverge, so (2.3) and the correlator's $|z_{12}z_{13}z_{23}|^2$ are separately ill-defined and
only their product is not. §3 assembles them invariantly. The $\beta^6$ does **not** come
from the dressing alone — it comes from the
dressing *in the frame-independent combination with the puncture separations*, and in a
generic frame the two pieces are individually not $\beta^6$ and $1$.

## 3. The ghost correlator and the invariant assembly

\subsection*{Setup}

A1, A2, A4 (see the claim tree). At $k_a=0$ the matter operators reduce to the identity and
(1.4) becomes a pure ghost correlator times the stripped volume factor of H1.

\subsection*{Derivation}

**The ghost three-point function.** Record 041 §3.1 derives, from the mode expansion and the
book's vacuum normalisation alone,

$$\mathcal G_3:=\langle c\bar c(z_1)\,c\bar c(z_2)\,c\bar c(z_3)\rangle
 =\langle c_{-1}\bar c_{-1}c_0\bar c_0c_1\bar c_1\rangle\,|z_{12}z_{13}z_{23}|^2
 =2\nu\,|z_{12}z_{13}z_{23}|^2,\tag{3.1}$$

using $c_0^-c_0^+=\tfrac12c_0\bar c_0$, so that $2\nu=\langle c_{-1}\bar c_{-1}c_0\bar c_0
c_1\bar c_1\rangle$. With the book's value (A2),

$$2\nu_{\rm book}=-1,\qquad \mathcal G_3^{\rm book}=-\,|z_{12}z_{13}z_{23}|^2 .\tag{3.2}$$

The sister project writes the same identity as
$\langle c\bar c\,c\bar c\,c\bar c\rangle=-2\langle ccc\rangle_o\langle\bar c\bar c\bar c\rangle_o$
with $\langle c(z_1)c(z_2)c(z_3)\rangle_o=z_{12}z_{13}z_{23}$ (their eq. (2)), i.e.
$2\nu_{\rm sister}=-2$. The *functional form* (3.1) is common to both; only $\nu$ differs.

**Assembly.** Combining (1.4) at $k=0$ with (3.1),

$$\{T^3\}(\beta)=2\nu\;\underbrace{\Big(\prod_a|\rho_a|^{-2}\Big)\,
 |z_{12}z_{13}z_{23}|^2}_{=:J(\beta)} .\tag{3.3}$$

$J$ is SL(2,C)-invariant: under $z\to\gamma(z)$ applied to all three maps,
$z_{ab}\to\gamma'(z_a)^{1/2}\gamma'(z_b)^{1/2}z_{ab}$ exactly for a Möbius map, so
$z_{12}z_{13}z_{23}\to\prod_a\gamma'(z_a)\cdot z_{12}z_{13}z_{23}$, while
$\prod_a|\rho_a|^{-2}\to\prod_a|\gamma'(z_a)|^{-2}\prod_a|\rho_a|^{-2}$: the two factors
cancel.

**Route A — generic finite frame (the computation that carries the result).** Apply a generic
real Möbius map $\gamma(z)=\frac{az+b'}{cz+d}$, $c\neq0$, to all three maps, so that all three
punctures become finite and no regulator is needed. Computing $F_a=\gamma\circ f_a$, their
radii $F_a'(0)$ and their images $F_a(0)$ symbolically and forming $J$:

$$J(\beta)=\frac{\big[(p_0-p_1)(p_0-p_\infty)(p_1-p_\infty)\big]^2}{\big[F_0'(0)F_1'(0)F_\infty'(0)\big]^2}
 =\beta^6\qquad\text{identically in }a,b',c,d.\tag{3.4}$$

**Route A$'$ — one explicit frame, by hand.** Take $\gamma(z)=1/(z-2)$, i.e.
$(a,b',c,d)=(0,1,1,-2)$. Then $p_0=-\tfrac12$, $p_1=-1$, $p_\infty=0$, and
$\gamma'(z)=-(z-2)^{-2}$ gives $\gamma'(0)=-\tfrac14$, $\gamma'(1)=-1$, while
$\gamma\circ f_\infty(w)=\frac{2w}{2\beta-3w}$ has radius $1/\beta$ directly. Hence

$$|\rho_0|=\frac{1}{4\beta},\quad|\rho_1|=\frac1\beta,\quad|\rho_\infty|=\frac1\beta
 \ \Rightarrow\ \prod_a|\rho_a|^{-2}=16\beta^6,\qquad
 |p_{01}p_{0\infty}p_{1\infty}|^2=\Big|\tfrac12\cdot(-\tfrac12)\cdot(-1)\Big|^2=\tfrac1{16},\tag{3.5}$$

$$J=16\beta^6\cdot\tfrac1{16}=\beta^6 .\tag{3.6}$$

Here neither factor is $\beta^6$ nor $1$ — this is the concrete demonstration that the
$\beta^6$ is not "from the dressing alone".

**Route B — the $(0,1,\infty)$ frame with the standard $h=-1$ prescription at infinity.**
$c(\infty)=\lim_{Z\to\infty}Z^{-2}c(Z)$ gives $\langle c(0)c(1)c(\infty)\rangle_o=
\lim_{Z\to\infty}Z^{-2}(0-1)(0-Z)(1-Z)=-1$, so $|z_{12}z_{13}z_{23}|^2\to1$ and
$J=\beta^6\cdot1=\beta^6$, in agreement with (3.4).

\subsection*{Commentary}

(3.1): imported from record 041, where it is derived from the mode expansion (a Vandermonde
determinant) and checked symbolically. The one delicate sign is the parity of the
interleaved $\to$ separated reordering of six odd objects, which cancels against the
permutation acting on the zero-mode string (F7). It is re-checked here rather than assumed:
`C1.3-reorder-parity` and `C1.3-parity-cancels` build the operator-side permutation from the
(chirality, insertion) labels and the mode-side one from the (chirality, level) labels and
the pairing of saturating modes to insertions, so the cancellation is exhibited as the
equality of two interleaving parities built from different label sets; it holds because both
strings interleave the two chiralities along an ordered index with the same mode-to-insertion
pairing, which is an input from the mode expansion rather than a result of the check (control
`BREAK-WRONG-PAIRING` shows the cancellation fails if that pairing is altered). The step
$c_0^-c_0^+=\tfrac12c_0\bar c_0$, which converts
$\nu_{\rm book}=-\tfrac12$ into the $2\nu_{\rm book}=-1$ that carries the whole book-side
number, is checked separately (`C1.3-c0pm-factor`, control `BREAK-WRONG-C0PM`).

(3.4): $a,b',c,d$ real is sufficient for the comparison, since $J$ is then a rational function
and $|\cdot|^2=(\cdot)^2$; the complex case follows by the same cancellation argument given
above (3.4), and Route A$'$ plus Route B already pin the value.

(3.6) vs (2.3): the two frames give $\prod|\rho_a|^{-2}=16\beta^6$ and $\beta^6$ and separation
factors $1/16$ and $1$. Only $J$ is common.

\subsection*{Result}

$$\boxed{\ J(\beta)=\beta^6,\qquad
 \{T^3\}(\beta)=2\nu\,\beta^6
 \ \stackrel{\rm book}{=}\ -\beta^6
 .\ }\tag{3.7}$$

The companion computation's value is obtained by inserting its own $2\nu$ (value from the
companion computation, not reproduced here).

## 4. Result, ratio, and the verdict on `R43`

### 4.1 The numbers

From (3.7), with $2\nu_{\rm book}=-1$:

| $\beta$ | $\{T^3\}_{\rm book}$ (this work) |
| --- | --- |
| $\tfrac32$ | $-729/64=-11.390625$ |
| $2$ | $-64$ |
| general | $-\beta^6$ |

The companion computation's raw values (not reproduced here) stand to these in the ratio
$\tfrac12$ book/sister, at both $\beta$ and in general. The companion's published row
`SL: R3` quotes the potential-side sign; §4.2 explains the flip. The comparison is of raw with
raw, and assumes H1 (the same matter and volume factors stripped on both sides).

### 4.2 The overall sign, stated honestly

The signs in the table are the signs of the amplitude (1.1) assembled literally, on both
sides, from each project's own vacuum normalisation. They agree, and the ratio is $+\tfrac12$.

One observation, recorded rather than repaired. The sister's published row `SL: R3` states
the potential-side sign, whereas their own formulas assembled literally give the opposite
sign: the same flip is built into their absolute normalisation, whose alternating sign is the
potential-side $V=-S$ convention (F8). So the published value is a potential-side number and
the raw one is the action-side one. Applying the same dictionary here gives
$\{T^3\}_{\rm book}=+\beta^6$, i.e. $C_3^{\rm book}=+1$.

This does not touch the comparison: the dictionary sign is one factor common to both sides and
cancels in the ratio, and the ratio is the claim under test. It is flagged because a reader
comparing $-\beta^6$ here with the potential-side value there would read a ratio of $-\tfrac12$ and think
the sign half of `R43` had failed. The rule is: compare like with like — raw amplitude with
raw amplitude, or potential-side with potential-side.

### 4.3 What was established, item by item against §0

1. **$\lambda$-weight $=1$.** $\{T^3\}$ is one sphere correlator: (3.3) contains exactly one
   factor of $\nu$, multiplying a purely geometric $J$ that carries no normalisation. So it
   scales with $\lambda^1$, not $\lambda^2$. This is the item on which the superseded "factor
   2 per strand" rule was wrong for $V_4$, and it is now checked on a quantity with published
   numbers on both sides. **Confirmed.**
2. **Geometric factor.** $J(\beta)=\beta^6$, proved frame-independent by the Möbius
   cancellation above (3.4) and evaluated in three frames — a generic symbolic one, an
   explicit finite one by hand (3.5)–(3.6), and the $(0,1,\infty)$ frame with the standard
   prescription at infinity (the script adds the $\Lambda$-regulated version of the last).
   These are consistency evaluations of one invariance argument, not independent derivations.
   No factor of $27$, $64/27$ or anything else appears: the two sides use the *same* cubic
   prescription, as `SL: R3` says, and the $J$ implied by the companion computation's raw value with
   their $2\nu_{\rm sister}=-2$ is the $\beta^6$ computed here (`C1.5-sister-J-consistent`).
   **Confirmed.**
3. **No further hidden convention.** The remaining candidates were F6 (matter/volume) and F8
   (dictionary). F6 is H1, identical on both sides and stripped the same way — the book's
   normalisation carries the momentum delta $(2\pi)^D\delta^D(k-k')$ explicitly, and at
   $k=0$ both projects strip the same $V_D$. **Conditional on H1.** The dictionary F8 is
   isolated and shown to cancel in §4.2; the matter/volume factor F6 is H1, assumed identical
   on both sides and not derived — see §5 for its falsifier.
4. **Sign.** Equal on both sides; the ratio is $+\tfrac12$. **Confirmed**, consistent with the
   two independent sign routes of record 041 §3.

**Verdict.** `R43`'s magnitude $\lambda=\tfrac12$ is **confirmed, conditionally on H1**, in the
strongest sense in which it is confirmable: an end-to-end recomputation of a shared quantity in
this project's normalisation reproduces exactly half the sister's published value, with equal
sign, and the three ways in which the table could have been wrong — wrong $\lambda$-power, a
geometric or prescription mismatch, a further unnoticed convention — are each excluded, the
third conditionally on H1. The spec clause "verify the convention table on one shared
quantity" is met, conditionally on H1.

### 4.4 Second method (transcription check, not independent evidence)

Route: take the companion's published $\{T^3\}$ and apply the declared conversion
$\times\lambda=\tfrac12$ (`R43`). This gives $\beta^6$, matching §4.1 in magnitude and
matching §4.2's potential-side value $+\beta^6$ in sign.

**This is not independent evidence for the magnitude.** It uses the very rescaling under test,
and it would agree with any $\lambda$. Its content is narrower and still worth having: it
confirms that the companion's cubic-coupling row is transcribed consistently with the
$V_4\times\tfrac12$ row, i.e. that both are $\lambda^1$ entries. The independent content of
this record is §3–§4.3.

### 4.5 Recommendation for the ledger

`R43`'s Scope paragraph currently reads that "the *magnitude* $\lambda=\tfrac12$ is the
convention being translated and comes out tautologically from the two declarations — an
independent fix needs the Stage-0 recomputation". That clause should be replaced by: the
magnitude is confirmed by the Stage-0 recomputation (record 046), which reproduces
$|\{T^3\}_{\rm book}|=\beta^6$ against the companion's value (raw values of equal sign,
ratio $\tfrac12$; potential-side dictionary in 046 §4.2) from the book's vacuum
normalisation and the cubic mapping radii, with the $\lambda$-weight and the geometric factor
each checked separately and the absence of a further convention holding conditionally on the
declared hypothesis H1 (matter normalisation and volume stripping common to both projects;
falsifier in §5); what remains declarative is $\lambda$'s *definition* as the ratio of two
vacuum normalisations, which no computation can change. The row already names the predicted
value, $\{T^3\}(\beta)=\beta^6$ (041 §3.2); this record derives it from the book's vacuum
normalisation and the map geometry without using $\lambda$, so the prediction is confirmed
rather than restated. The restated row is `Conditional(PH24 = H1) – Verified`. The
verification cell gains record 046 and `codes/verify-stage0-translation.py`.

## 5. Scope

**Covered.** Sphere, tree level, $n=3$, no moduli integral. Zero external momentum
($\alpha'k_a^2=0$), hence the off-shell prescription-dependent cubic coupling. The SL(2,C)
(Möbius) cubic vertex $f_a(w)$ of A3, for any $\beta$ in the range (companion value, not reproduced here) — the result $J=\beta^6$ is
exact in $\beta$, not an expansion. Any SL(2,C) frame. The comparison is against the companion
computation's raw value, whose published row `SL: R3` differs from it by the potential-side
sign (§4.2).

**Not covered.**

- *On-shell* $\{T^3\}$: $\beta$-independent by §1.1 and a different quantity; nothing here
  tests it, and it could not test the translation anyway (a $\beta$-independent number still
  scales with $\lambda$, but so does everything).
- Quantities with a different $\lambda$-weight: $G_2$ ($\lambda^2$) and $V_4$ ($\lambda^1$,
  four-punctured sphere) are **not** checked here. What §4.3 item 1 establishes is the
  *principle* by which the weight is counted — one sphere correlator, one $\lambda$ — on a
  case where it is testable. Applying it to $V_4$ remains an inference from that principle,
  not a measurement; a Stage-1 analogue would require a four-point vertex engine, which this
  project does not have.
- Q2, the measure orientation $(2\pi\I)^{-1}$ vs $\I/2\pi$ per complex modulus. It is absent
  from a three-point function, which has no moduli — so Stage 0 is structurally blind to it.
  This is a limitation of the anchor, not a gap in the computation.
- H1 (matter normalisation and volume stripping) is a declared hypothesis, not derived. It is
  the one place where a common convention is assumed rather than checked. Falsified by: either project
  normalising the sphere matter one-point function differently from
  $\langle k,0|\,\cdot\,|k',0\rangle\propto(2\pi)^D\delta^D(k-k')$. Both write the zero-momentum
  amplitude with no explicit matter factor, and the book's vacuum normalisation
  `bos:eq:ws-closed-vacuum-normalization` carries the delta explicitly; a mismatch would show
  up as a $k$-independent constant, which would be visible in the on-shell three-point
  function against the known Virasoro–Shapiro normalisation. That check was not run.
- Higher genus, the superstring, and any statement about $\alpha'$-dependence (there is none
  here: $\alpha'$ enters only through $h$ via (1.2), and $k=0$).

[Correspondence with the companion project removed.]

## Claim tree

- **A1** Closed bosonic string, sphere, tree level, $\alpha'$ explicit, physical ghost number
  $N_{\rm gh}(\Psi)=2$; the project conventions.
- **A2** Book normalisation: $\langle c_{-1}\bar c_{-1}c_0\bar c_0c_1\bar c_1\rangle=-1$,
  equivalently $\nu_{\rm book}=\langle c_{-1}\bar c_{-1}c_0^-c_0^+c_1\bar c_1\rangle=-\tfrac12$
  ([Erbin 2023] `bos:eq:ws-closed-vacuum-normalization`, `cft:eq:bn-cn-pm`).
- **A3** SL(2,C) cubic vertex of the sister project: punctures at $z=0,1,\infty$ with
  $f_0(w)=\frac{2w}{2\beta+w}$, $f_1(w)=\frac{2\beta-w}{2\beta+w}$,
  $f_\infty(w)=\frac{2\beta+w}{2w}$, $\beta$ in a range (companion value, not reproduced here). Geometric
  data shared by both sides, not a convention of either.
- **A4** Zero external momentum, $k_a=0$ (see §1.1).
- **H1** *(hypothesis)* The matter sphere normalisation and the momentum delta
  $(2\pi)^D\delta^D(0)=V_D$ are stripped identically on both sides, so they contribute no
  factor to the ratio. **Motivation:** both projects write the zero-momentum amplitude with no
  explicit matter factor, and the book's vacuum normalisation
  `bos:eq:ws-closed-vacuum-normalization` carries the momentum delta explicitly, so the
  stripping is the same operation on both sides. **Falsifier / discharge:** either project
  normalising the sphere matter one-point function differently from
  $\langle k,0|\,\cdot\,|k',0\rangle\propto(2\pi)^D\delta^D(k-k')$; a mismatch would be a
  $k$-independent constant and would show up in the on-shell three-point function against the
  known Virasoro–Shapiro normalisation. That cross-check was not run (§5).
- **C1** $\{T^3\}(\beta)=2\nu\beta^6$; in this project's normalisation its magnitude is
  $\beta^6$, and the ratio to the sister project's raw value is
  exactly $\tfrac12$ with equal sign; against their published `SL: R3` the potential-side
  dictionary must be applied first (§4.2). So `R43`'s $\lambda=\tfrac12$ is confirmed in the
  sense of §0, conditional on H1. [by C1.1–C1.5; eq. (3.7)]
  - **C1.1** The $\beta$-dependence of the zero-momentum coupling is $\beta^6$, from the
    dressing exponent $\alpha'k^2/2-2=-2$ per puncture; on shell ($\alpha'k^2=4$) the exponent
    is $0$ and $\{T^3\}$ is $\beta$-independent. [by A1, A4; eq. (1.2)–(1.3), §1.1]
    [check: C1.1]
  - **C1.2** The SL(2,C)-invariant geometric factor
    $J=\prod_a|\rho_a|^{-2}|z_{12}z_{13}z_{23}|^2$ equals $\beta^6$ exactly, in every SL(2,C)
    frame; neither of its two factors separately equals $\beta^6$ or $1$ in a generic frame.
    [by A3; eq. (2.2), (3.4)–(3.6)] [check: C1.2]
  - **C1.3** $\mathcal G_3=\langle c\bar c(z_1)c\bar c(z_2)c\bar c(z_3)\rangle
    =2\nu|z_{12}z_{13}z_{23}|^2$, the functional form being common to both projects; with A2,
    $2\nu_{\rm book}=-1$. [by A2; eq. (3.1)–(3.2). The book-side value uses A2 alone; the
    identification of the sister's $c_0^\pm$ conventions with ours is F2, from `R43`'s $c_0^\pm$ clause — not from `R43`'s magnitude.] [check: C1.3]
  - **C1.4** $\{T^3\}$ is a single sphere correlator, hence linear in $\nu$ and of
    $\lambda$-weight 1 — not 2 as a per-strand count would give. [by C1.2, C1.3; eq. (3.3)]
    [check: C1.4]
  - **C1.5** $\{T^3\}_{\rm book}/\{T^3\}_{\rm sister}=\tfrac12$ exactly at $\beta=\tfrac32$ and
    $\beta=2$, signs equal; $|\{T^3\}_{\rm book}|(\tfrac32)=729/64=11.39$ against the
    companion's value (not reproduced here) (conditional on H1). [by C1.1–C1.4, H1; §4.1] [check: C1.5]
  - **C1.6** No further convention differs between the two sides in this quantity
    (conditional on H1). The candidates are H1 (matter/volume) and the vertex-to-potential
    dictionary; the latter is shown to cancel in the ratio (§4.2), the former is the declared
    hypothesis, not derived — see §5. [by H1; §4.3 item 3]

Open gaps: none.
Hypotheses in force: H1 = **PH24** (shared matter normalisation and volume stripping; motivation and
falsifier in §5; the on-shell Virasoro–Shapiro cross-check that would discharge it was not
run).

## Verification

`codes/verify-stage0-translation.py`, run under `.venv/bin/python`, seed `20260921`.
17 named checks, all PASS, 0 FAIL, and 5 break-on-purpose controls, all confirmed to fire:

| Check | What it tests | Method |
| --- | --- | --- |
| `C1.1-exponent-form`, `C1.1-zero-momentum`, `C1.1-on-shell` | C1.1 | symbolic weight $h=\alpha'k^2/4-1$, $\beta$-power at $k=0$ and on shell |
| `C1.2-generic-moebius` | C1.2 | $J$ computed from $\gamma\circ f_a$ for a *symbolic* Möbius $\gamma=(az+b)/(cz+d)$; reduces to $\beta^6$ identically in $a,b,c,d$ |
| `C1.2-explicit-frame`, `C1.2-dressing-alone-frame-dependent` | C1.2 | $\gamma(z)=1/(z-2)$; also records that the dressing alone is $16\beta^6$ there |
| `C1.2-lambda-regulated` | C1.2 | the $\Lambda$-regulated $(0,1,\infty)$ frame; $\Lambda$ cancels |
| `C1.2-complex-frame` | C1.2 | one fixed generic complex frame, modulus squared throughout |
| `C1.5-sister-J-consistent` | C1.2, C1.5 | our computed $J$ against the $J$ implied by the companion computation's raw value with their $2\nu_{\rm sister}=-2$ — the non-tautological half of the ratio |
| `C1.3-vandermonde` | C1.3 | $\langle ccc\rangle$ rebuilt from the mode sum by an explicit Grassmann reduction (inversion counting), compared with $z_{12}z_{13}z_{23}$ |
| `C1.3-reorder-parity`, `C1.3-parity-cancels` | C1.3 | parity of the interleaved $\to$ separated permutation of six odd objects, built from the operator labels (chirality, insertion) and from the zero-mode labels (chirality, level, with the mode-to-insertion pairing) |
| `C1.3-c0pm-factor` | C1.3 | $c_0^-c_0^+=\tfrac12c_0\bar c_0$ expanded in the Grassmann engine, hence $2\nu_{\rm book}=-1$ from $\nu_{\rm book}=-\tfrac12$ |
| `C1.4-lambda-weight-one` | C1.4 | structural bookkeeping, not a falsifiable check (the claim is established by (1.1)–(3.3)): $\nu\to\lambda\nu$ scales $\{T^3\}$ by $\lambda^1$ |
| `C1.5-ratio-one-half`, `C1.5-signs-equal`, `C1.5-magnitudes` | C1.5 | exact rational arithmetic at $\beta=\tfrac32,2$ |
| `BREAK-WRONG-NU` | control | setting $\nu_{\rm book}=-1$ (the sister's value) makes the ratio $1$ — `C1.5-ratio-one-half` fails |
| `BREAK-WRONG-EXPONENT` | control | dressing exponent $-1$ instead of $-2$ ($\beta^3$) — `C1.5-magnitudes` fails |
| `BREAK-WRONG-GEOMETRY` | control | rescaling one map by $2$ — the four falsifiable `C1.2` checks and `C1.5-sister-J-consistent` fail (`C1.2-dressing-alone-frame-dependent` is not emitted under the control); frame invariance is what detects the perturbation |
| `BREAK-WRONG-PAIRING` | control | reversing the pairing of antiholomorphic modes to insertions flips the mode-side parity and not the operator-side one — `C1.3-parity-cancels` fails |
| `BREAK-WRONG-C0PM` | control | the un-halved convention $c_0^\pm=c_0\pm\bar c_0$ gives coefficient $2$ and $2\nu_{\rm book}=-\tfrac14$ — `C1.3-c0pm-factor` fails |

**Falsifiability.** `C1.2-generic-moebius` is the load-bearing check and cannot be vacuous:
its input is a symbolic family of frames and its output is a single $\beta$-monomial; the
break control shows it returns a messy $a,b,c,d$-dependent expression as soon as the map data
is wrong. `C1.3-vandermonde` compares a mode-sum construction against a closed form derived
independently, and `C1.3-parity-cancels` and `C1.3-c0pm-factor` each have their own control.
`C1.5-ratio-one-half`, `C1.5-signs-equal` and `C1.5-magnitudes` are exact arithmetic on two
declared normalisations, with the same $J$ on both sides; the comparison's non-tautological
content sits in `C1.2-generic-moebius` and in `C1.5-sister-J-consistent`, which confronts our
computed $J$ with the one implied by the sister's published number, together with the
sister's own published value. `C1.4-lambda-weight-one` is structural bookkeeping: $\{T^3\}$ is
linear in $\nu$ by construction of the monomial, and the physical claim (one sphere
correlator, not two) rests on (1.1)–(3.3). What is *not* falsifiable by any check here is H1
— see §5.

**Not machine-checkable here.** The statement that the two projects strip the same matter and
volume factors (H1) is a reading of two conventions, not a computation; it is declared as a
hypothesis in the claim tree and its falsifier is stated there and in §5.
