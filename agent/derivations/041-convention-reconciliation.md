# 041 — Convention reconciliation: ghost sector, this project ↔ SL(2,C) project ↔ the book

## Status

Done — all four deliverables written (§1 table, §2 verification, §3 Q2 branches, §4
change-sets), claim tree closed, companion script `codes/verify-conventions.py` (42 checks,
0 FAIL, seed 20260922, 7 break controls that all fire). Next: orchestrator decision on Q2, then
the proposed edits of §4.

## Task and objective

**Literal task.** Build the convention translation between this project (cubic closed SFT),
the sister project (`SL(2, C) quartic vertex for closed SFT`) and Erbin 2023 (*String Field
Theory: A Modern Introduction*), for the closed-string ghost sector; verify it on a shared
quantity; assess the consequences of Q2 without deciding it; and list the per-project
change-set.

**Motivating objective.** The two projects exchange numerical vertex data. Until the ghost
conventions are reconciled, every eigenvalue, norm and condition number crossing the
project boundary is uninterpretable (ratios such as $\rho(D^{-1}N)$ are convention-safe).
The next data request note is blocked on this.

**Q1, in my words.** Both projects write the same operator string
$c_{-1}\bar c_{-1}c_0^-c_0^+c_1\bar c_1$ and assign it different numbers ($-1/2$ here and in
the book, $-1$ in the sister project). Three candidate explanations: (a) the base
correlator $\braket{c_{-1}\bar c_{-1}c_0\bar c_0c_1\bar c_1}$ itself differs by a factor 2;
(b) the definition of $c_0^\pm$ differs (with or without the $1/2$); (c) the two
normalisations refer to different base correlators (different states, different measure of
the zero mode, different $\delta^{(D)}$ stripping). Q1 asks which, with the factors shown.

**Q2, in my words.** Independently of Q1, the off-shell measure per complex modulus is
written $(\mathrm i/2\pi)^{N-3}$ by Belopolsky–Zwiebach (eq. 4.10) and, read with the
orientation conventions O1–O4 of the sister project's record 039, the book's
`bos:eq:omega-p` differs from it by $(-1)^{N-3}$. This is a claim that one of two published
transcriptions carries a sign error, not a choice of convention: it changes the sign of $C_4$
(negative to positive), $K_f$ from $+1$ to $-1$, and flips $\operatorname{spec}(m_2)$. The
adopted rule that the book's conventions apply does not settle it. My job is to lay out both branches and what each
does to this project's rows, not to pick one.

## Conventions used here

- Physical ghost number: $N_{\rm gh}(\Psi)=2$, $N_{\rm gh}(\Sigma_k)=2k$, $N_{\rm gh}(m_2)=+2$.
- $\Sigma\in\mathrm{Sym}^2\mathcal H_0/\ker V_4$ (level-matched, kernel quotiented).
- Ordering convention stated explicitly at every occurrence: $c_0^-c_0^+$ vs $c_0^+c_0^-$
  differ by a sign ($c_0^\pm$ are anticommuting and $\{c_0^-,c_0^+\}$ is computed below).
- $\alpha'$ kept explicit; $\hbar=c=1$.

## Claim tree

- **A1** Ghost sector of the closed bosonic string on the sphere, $bc\bar b\bar c$ CFT,
  physical ghost number; $\alpha'$ explicit except where BZ's $\alpha'=2$ is quoted.
- **A2** The book (Erbin 2023) is the authority for Q1: `cft:eq:bn-cn-pm` and
  `bos:eq:ws-closed-vacuum-normalization` are explicit and mutually consistent.
- **A3** For Q2, the book's `bos:eq:omega-p` and BZ eq. 4.10 are treated as *two candidate
  transcriptions*, neither taken as authority.
- **A4** Ordering conventions held fixed throughout: $c_0^-c_0^+$ (not $c_0^+c_0^-$), and the
  base string written $c_{-1}\bar c_{-1}c_0\bar c_0c_1\bar c_1$ (interleaved, holomorphic
  first at each level). Both are used by all three sources.
- **C1** The sister project's $\nu=-1$ and the book's $\nu=-\tfrac12$ differ **only** by the
  overall normalisation of the sphere ghost correlator (resolution **(a)**, refined): the
  definitions of $c_0^\pm$, $b_0^\pm$ and the operator ordering are literally identical on
  both sides, the signs agree, and the single conversion is
  $\langle\,\cdot\,\rangle_{\rm book}=\tfrac12\langle\,\cdot\,\rangle_{\rm sister}$ on every
  ghost-saturating sphere correlator. [by C1.1–C1.4]
  - **C1.1** Book: $c_0^\pm=\tfrac12(c_0\pm\bar c_0)$, $b_0^\pm=b_0\pm\bar b_0$, hence
    $c_0^-c_0^+=\tfrac12c_0\bar c_0$ and $b_0^-b_0^+=2b_0\bar b_0$.
    [cited: Erbin2023 `cft:eq:bn-cn-pm`] [check: C1.1]
  - **C1.2** The sister project uses the *same* definitions, inherited verbatim from
    Belopolsky–Zwiebach: $c_0^\pm=\tfrac12(c_0\pm\bar c_0)$, $b_0^\pm=b_0\pm\bar b_0$ (no
    $\tfrac12$). Hypothesis (b) of the brief is therefore **excluded**, not merely
    insufficient. [cited: SL 039 conventions K1, K5; BZ eq. 2.7 quoted verbatim in the literature review]
  - **C1.3** Base correlators: book $\langle c_{-1}\bar c_{-1}c_0\bar c_0c_1\bar c_1\rangle=-1$;
    sister, implied by $\nu=-1$ and C1.1, $=-2$. [cited: Erbin2023
    `bos:eq:ws-closed-vacuum-normalization`; by C1.1, SL R37 eq. (1.4)] [check: C1.3]
  - **C1.4** The sister's $\nu=-1$ is *derived* there from the kinetic anchor ($S_2$ must
    reproduce $V=-\tau^2$, $K=\tfrac12(\partial\tau)^2$ at $\alpha'=2$), not imported; in the
    book's normalisation the same anchor gives a tachyon field rescaled by $\sqrt2$ ($\Psi_{\rm book}=\sqrt2\Psi_{\rm sister}$) and
    $\kappa_{\rm BZ}=\kappa_{\rm sister}=\sqrt2\,\kappa_{\rm book}$, i.e. the factor 2 is a field/coupling
    normalisation, not a disagreement. [by C1.1, C1.3; eq. (1.5)–(1.7)] [check: C1.4]
- **C2** The translation table is loop-consistent: the conversion factors compose to the
  identity around book → this project → sister → book, and every derived quantity carries
  the power of $\tfrac12$ dictated by its number of sphere correlators.
  [by C2.1–C2.3] [check: C2]
  - **C2.1** This project's declared conventions are the book's, unchanged; the
    book → this-project leg is the identity. [cited: the project conventions, *Physics conventions*]
  - **C2.2** Counting of correlators: $g$, $\{T^N\}$, $C_N$ carry one factor
    ($\times\tfrac12$ sister → book); $G_2$ on $\mathrm{Sym}^2$ is a product of two $g$'s and
    carries $\times\tfrac14$; hence $m_2=G_2^{-1}V_4$ carries $\times2$ and
    $\operatorname{spec}(m_2)$ doubles in magnitude with its signs unchanged.
    [by C1; eq. (2.1)–(2.4)] [check: C2.2]
  - **C2.3** $K_f$, $\hat\lambda=\lambda/C_4$, the rank of $V_4$, the signature $(2,1)$ of
    $G_2$, eigenvalue ratios and $\rho(D^{-1}N)$ are invariant under the Q1 conversion; the
    $t^4$ sewing identity scales homogeneously ($\tfrac12$ on both sides).
    [by C2.2; eq. (2.5)] [check: C2.3]
- **C3** Item 2 (verification on a shared quantity): the ghost three-point function
  $\mathcal G_3=\langle c\bar c(z_1)c\bar c(z_2)c\bar c(z_3)\rangle$ is computed here from the
  book's base correlator by mode algebra and Grassmann reordering, giving
  $\mathcal G_3^{\rm book}=-|z_{12}z_{13}z_{23}|^2$, against the sister's own
  $\mathcal G_3^{\rm sister}=2\nu|z_{12}z_{13}z_{23}|^2=-2|z_{12}z_{13}z_{23}|^2$: the ratio
  is exactly $\tfrac12$, as the table requires, and the *signs agree*. The check has real
  content in the sign and in the identity $\mathcal G_3=\langle{\rm base}\rangle\,
  |z_{12}z_{13}z_{23}|^2$; it has no content in the magnitude, which is the convention being
  translated. [by C3.1, C3.2] [check: C3]
  - **C3.1** $\langle c(z_1)c(z_2)c(z_3)\rangle=\langle c_{-1}c_0c_1\rangle\,z_{12}z_{13}z_{23}$
    (Vandermonde from the mode expansion). [eq. (3.2)–(3.4)] [check: C3.1]
  - **C3.2** Interleaved → separated reordering of three $c\bar c$ pairs costs exactly one
    sign, $(-1)$; hence $\mathcal G_3=\langle c_{-1}\bar c_{-1}c_0\bar c_0c_1\bar c_1\rangle\,
    |z_{12}z_{13}z_{23}|^2$ in *any* of the three normalisations.
    [eq. (3.5)–(3.7)] [check: C3.2]
  - **C3.3** No quantity is at present computed *independently* on both sides from a vertex
    integral: this project ships no vertex engine and imports every ghost-sector number.
    The cheapest quantity that would serve is Stage 0, $\{T^3\}(\beta)=C_3\beta^6$, which in
    the book's normalisation is $\beta^6$ against the sister's
    (companion value, not reproduced here). [by C1, C3]
- **C4** Q2 changes the *relative* normalisation of the cubic and quartic vertices, so it is
  a question of fact and not of convention; on this project's side it changes no ledger row's
  statement and only one reading. [by C4.1–C4.3]
  - **C4.1** The two measure prefactors differ by $(-1)^{N-3}$ per genus-0 amplitude:
    $(2\pi\mathrm i)^{-(N-3)}=(-\mathrm i/2\pi)^{N-3}$ against BZ's $(\mathrm i/2\pi)^{N-3}$.
    [cited: Erbin2023 `bos:eq:omega-p`; BZ eq. 4.10] [check: C4.1]
  - **C4.2** $\operatorname{sign}(C_4/C_3^2)$ and $K_f$ are physical (fixed by factorisation),
    the overall sign of $C_N$ (potential vs action side) is not; so exactly one of the two
    transcriptions is correct. [by SL R37, SL R30; §3.1]
  - **C4.3** On this project's side the flip touches only *which* Laplace/Schwinger
    representation of $V_4^{-1}$ converges (R15 clause 2, a conditional statement whose
    truth does not move), plus one sentence of
    `knowledge/topics/sl2c-data-request-2026-09-22.md` §1. No row, no hypothesis, no
    magnitude changes. $K_f$ appears nowhere in this project's ledger. [by R15; §3.2]
- **C5** Change-set per project, §4. [by C1–C4]

Open gaps: none
Hypotheses in force: none. **Q2 is left undecided by design** (brief constraint); §3 is
stated branch by branch and nothing in §1, §2 or §4's Q1 part depends on the branch.

## 1. Translation table (deliverable 1)

Conversion column reads **sister → book** (equivalently sister → this project, since the
book → this-project leg is the identity, C2.1). "One sphere correlator" means the factor is
$\tfrac12$; a quantity built from $k$ independent sphere correlators carries $(\tfrac12)^k$.

| Object | This project | SL(2,C) project | Book (Erbin 2023) | Conversion sister → book, with its one-line derivation |
|---|---|---|---|---|
| $c_0^\pm$ definition | $\tfrac12(c_0\pm\bar c_0)$ | $\tfrac12(c_0\pm\bar c_0)$ (039 K1, from BZ 2.7) | $\tfrac12(c_0\pm\bar c_0)$ (`cft:eq:bn-cn-pm`) | $\times1$ — literally the same definition; hypothesis (b) of the brief is excluded |
| $b_0^\pm$ definition | $b_0\pm\bar b_0$ | $b_0\pm\bar b_0$ (039 K1, "no $\tfrac12$") | $b_0\pm\bar b_0$ (`cft:eq:bn-cn-pm`) | $\times1$ — normalised to match $L_m^\pm$; $[b^+_m,c^+_n]=[b^-_m,c^-_n]=\delta_{m+n}$ in all three |
| $c_0^-c_0^+$ in terms of $c_0\bar c_0$ | $\tfrac12c_0\bar c_0$ | $\tfrac12c_0\bar c_0$ | $\tfrac12c_0\bar c_0$ | $\times1$ — $\tfrac14(c_0-\bar c_0)(c_0+\bar c_0)=\tfrac14(c_0\bar c_0-\bar c_0c_0)=\tfrac12c_0\bar c_0$ |
| $b_0^-b_0^+$ in terms of $b_0\bar b_0$ | $2b_0\bar b_0$ | $2b_0\bar b_0$ | $2b_0\bar b_0$ | $\times1$ — same computation without the $\tfrac14$ |
| ordering used for $\nu$ | $c_0^-c_0^+$ | $c_0^-c_0^+$ | $c_0^-c_0^+$ | $\times1$; note $\{c_0^-,c_0^+\}=0$ so $c_0^+c_0^-=-c_0^-c_0^+$: the opposite ordering would flip every sign in this table |
| base correlator $\langle c_{-1}\bar c_{-1}c_0\bar c_0c_1\bar c_1\rangle$ | $-1$ | $-2$ (implied by $\nu=-1$) | $-1$ (`bos:eq:ws-closed-vacuum-normalization`, $(2\pi)^D\delta^{(D)}$ stripped) | $\times\tfrac12$ — one sphere correlator. **This single row is the whole of Q1** |
| $\nu=\langle c_{-1}\bar c_{-1}c_0^-c_0^+c_1\bar c_1\rangle$ | $-\tfrac12$ | $-1$ (039 eq. 1.4, R37; $=$ BZ's working value, eqs. 2.8/4.3) | $-\tfrac12$ | $\times\tfrac12$ — $\nu=\tfrac12\langle{\rm base}\rangle$ in both, by the $c_0^-c_0^+$ row |
| pairing $g(A,B)=\langle A\lvert c_0^-c_0^+\rvert B\rangle$ | same definition | same definition (R16) | same definition (the book's $\langle A,B\rangle$ uses $c_0^-$ alone; see note (i) below) | $\times\tfrac12$ on values; definition identical |
| $g(T,T)$, $T=c_1\bar c_1\lvert0\rangle$ | $-\tfrac12$ | $-1$ (R16) | $-\tfrac12$ ($=\nu$, same operator string) | $\times\tfrac12$ |
| $g(D,D)$, $D=D_h-D_a$ | $+1$ | $+2$ (R16) | $+1$ | $\times\tfrac12$ |
| $G_2$ on $\mathrm{Sym}^2\{T,D\}$ | $\tfrac14\mathrm{diag}(1,-1,4)$ | $\mathrm{diag}(1,-1,4)$ (R49) | $\tfrac14\mathrm{diag}(1,-1,4)$ | $\times\tfrac14$ — **two** correlators: $G_2\sim g\otimes g$ |
| $V_4$ on $\mathrm{Sym}^2$ ($\{T^4\}$, $\{T^3D\}$, …) | — (imported) | R7(b), R40, R44, R35 values | — | $\times\tfrac12$ — **one** four-punctured sphere correlator, not two |
| $m_2=G_2^{-1}V_4$, $\operatorname{spec}(m_2)$ | — (imported) | all negative (R49; companion value, not reproduced here) | — | $\times2$ (magnitudes), signs unchanged by Q1 |
| $C_3$ | — | (companion value, not reproduced here) (R3, R8) | $+1$ | $\times\tfrac12$ |
| $C_4$ | — | negative, potential side (R8, R37; value from the companion SL(2,C) computation, not reproduced here) | negative **under Q1 alone**; positive if Q2 is resolved in the book's favour | $\times\tfrac12$ (Q1) and $\times(-1)$ (Q2, undecided) |
| measure factor per complex modulus | — (inherits) | $\mathrm i/2\pi$ (BZ 4.10, K8) | $(2\pi\mathrm i)^{-1}=-\mathrm i/2\pi$ (`bos:eq:omega-p`) | $\times(-1)$ per modulus, i.e. $(-1)^{N-3}$ per genus-0 amplitude. **This is Q2, and it is not a convention** |
| $K_f$ | not used (absent from the ledger) | $+1$ (R30, R36) | $+1$ under Q1; $-1$ under Q2-book | invariant under Q1 (see §2.3); flips under Q2 |
| $\hat\lambda=\lambda/C_4$ | — | positive (R49) | same | invariant under Q1 **and** under Q2 |
| $\operatorname{spec}(m_2)$ sign | read by R15 clause 2 | negative (potential side, $C_4<0$) | negative under Q1 alone; positive under Q2-book | Q1: unchanged. Q2: flips |

Notes.

(i) The book's *inner product* $\langle A,B\rangle=\langle{\rm bpz}(A)\,c_0^-B\rangle$ inserts
$c_0^-$ only (`bos_worldsheet_cft.tex`, computation block at l. 1333). The pairing $g$ of the
table is the ghost-number-saturating one with $c_0^-c_0^+$, which is what both projects use
on ghost-number-2 states (on those, $c_0^-$ alone gives $0$; this is R16's documented
refinement of the RS6 spec's shorthand, not a disagreement with the book).

(ii) BZ's literal eq. 2.7 reads $+1$ for $\nu$; their working value in eqs. 2.8 and 4.3 is
$-1$, and the sister project's 039 §7.4 records that BZ eqs. 2.6–2.8 are mutually
inconsistent by one sign. The book's $-\tfrac12$ agrees in **sign** with BZ's working value,
not with BZ's literal 2.7. A statement in the sister project's ledger that the ghost norm
$\langle c_{-1}\bar c_{-1}c_0^-c_0^+c_1\bar c_1\rangle$ matches [Erbin 2023] with no
rescaling is wrong twice over (wrong sign, and a rescaling by $\tfrac12$ does
exist).

(iii) The note `knowledge/topics/sl2c-data-request-2026-09-22.md` §1 currently warns of "a
factor (2 per strand, 4 on $\mathrm{Sym}^2$)" on *every* magnitude. That over-corrects $V_4$:
the per-strand counting is right for $G_2$ and wrong for $V_4$, which is a single sphere
correlator. The net factor on $m_2$ is $2$, not $1$ and not $4$.

### 1.1 The conversion, derived

Every ghost-saturating sphere correlator is a multiple of the base correlator times a
kinematic factor fixed by the CFT (weights, mode algebra), so a change of the base
normalisation acts on all of them by one overall constant:

$$\langle\,\cdot\,\rangle_{\rm book}=\lambda\,\langle\,\cdot\,\rangle_{\rm sister},
\qquad \lambda=\frac{-1}{-2}=\frac12. \tag{1.1}$$

Equivalently, in terms of the action
$S=\tfrac12\langle\Psi,Q\Psi\rangle+\sum_{N\ge3}\frac{\kappa^{N-2}}{N!}\{\Psi^N\}$,

$$S_{\rm book}[\Psi]=\tfrac12\,S_{\rm sister}[\Psi], \tag{1.2}$$

which is undone by the field and coupling redefinition

$$\Psi=\sqrt2\,\Psi',\qquad \kappa_{\rm sister}=\sqrt2\,\kappa_{\rm book}, \tag{1.3}$$

($\Psi$ the book's field, $\Psi'$ the sister's) since $\tfrac12\cdot\tfrac{(\sqrt2)^2}{2}=\tfrac12$ on the kinetic term and
$\tfrac12\,\kappa_{\rm book}^{N-2}2^{N/2}=(\sqrt2\kappa_{\rm book})^{N-2}=\kappa_{\rm sister}^{N-2}$ on the $N$-th interaction; equivalently $S_{\rm book}[\Psi;\kappa]=S_{\rm sister}[\Psi/\sqrt2;\sqrt2\kappa]$. **Hence Q1 is
a pure field/coupling normalisation and changes no physical statement.**

The kinetic anchor makes this concrete. With the sister's K1–K3,

$$S_2=\tfrac12\langle T|c_0^-Q|T\rangle
 =\nu\int \dd^Dx\Big(\frac{\alpha'}{4}(\partial\tau)^2-\tau^2\Big). \tag{1.4}$$

Imposing $S_2=-\int(\tfrac12(\partial\tau)^2-\tau^2)$ at $\alpha'=2$ gives $\nu=-1$ (the
sister's eq. 1.4). In the book's normalisation the same expression reads

$$S_2=-\tfrac12\int \dd^Dx\Big(\tfrac12(\partial\tau)^2-\tau^2\Big)
 =-\int \dd^Dx\Big(\tfrac12(\partial\tilde\tau)^2-\tilde\tau^2\Big),
 \qquad \tau=\sqrt2\,\tilde\tau, \tag{1.5}$$

the same potential for the canonically normalised field. The tachyon mass is
$\nu$-independent in both,

$$m_T^2=-\frac{4}{\alpha'}, \tag{1.6}$$

which is the invariant statement behind the whole row. The overall sign of $\nu$, by
contrast, is **not** free: it is fixed by $V=-\tau^2$, and both sources give it negative,

$$\operatorname{sign}\nu_{\rm book}=\operatorname{sign}\nu_{\rm sister}=-1. \tag{1.7}$$

### Verdict on Q1

**Resolution (a), refined.** It is a genuine factor-2 difference, and it lives entirely in the
vacuum normalisation of the sphere ghost correlator — the book normalises the *unbarred*
string $c_{-1}\bar c_{-1}c_0\bar c_0c_1\bar c_1$ to $-1$, BZ and the sister project normalise
the $c_0^-c_0^+$ string to magnitude $1$. It is **not** (b): the $c_0^\pm$ definitions are
literally identical on both sides, $\tfrac12(c_0\pm\bar c_0)$, as BZ eq. 2.7 states in so many
words. It is **not** (c) in the sense of a different base operator string or a different
state: the strings, the ordering, and the momentum-delta stripping all agree. The signs
agree. The recollection behind Q1 is correct on each point.

## 2. Loop and scaling checks on the table (depth)

### 2.1 Loop composition

book $\to$ this project ($\times1$, C2.1) $\to$ sister ($\times2$) $\to$ book
($\times\tfrac12$) $=$ identity, on every row of the table, with the power of $\lambda$ fixed
by the number of sphere correlators:

$$\nu,\;g,\;\{T^N\},\;C_N:\ \lambda^1;\qquad
G_2\sim g^{\otimes2}:\ \lambda^2;\qquad
m_2=G_2^{-1}V_4:\ \lambda^{-2}\lambda^{1}=\lambda^{-1}=2. \tag{2.1}$$

Entry-wise check of the $G_2$ row, which is where the $\lambda^2$ has to show up:

$$G_2=\begin{pmatrix} g(T,T)^2 & & \\ & \tfrac12 g(T,T)g(D,D) & \\ & & g(D,D)^2\end{pmatrix}
 =\begin{cases}\mathrm{diag}(1,-1,4) & \text{sister }(g=-1,+2)\\[2pt]
 \mathrm{diag}(\tfrac14,-\tfrac14,1) & \text{book }(g=-\tfrac12,+1)\end{cases} \tag{2.2}$$

— ratio $\tfrac14$ in every entry, as required, and $\operatorname{sign}$ and signature
$(2,1)$ unchanged.

### 2.2 What scales and what does not

$$\operatorname{spec}(m_2)_{\rm book}=2\,\operatorname{spec}(m_2)_{\rm sister}
 \quad(\text{companion values, not reproduced here}), \tag{2.3}$$

$$\lVert m_2^{-1}\rVert_2\ \to\ \tfrac12\lVert m_2^{-1}\rVert_2,\qquad
 \text{gap}\ \to\ 2\times\text{gap}. \tag{2.4}$$

Invariant under Q1: all signs; the rank of $V_4$; the signature of $G_2$; every ratio of
eigenvalues; $\hat\lambda=\lambda/C_4$; $\rho(D^{-1}N)$ and the Neumann term counts of PH21
(the splitting $V_4=D-N$ is homogeneous of degree 0 in $\lambda$); the conditioning
$\kappa(X)$ on a fixed normalisation of the eigenvector columns; and $m_T^2=-4/\alpha'$.

### 2.3 $K_f$ is invariant — a non-trivial composition check

The $t^4$ sewing identity (SL R30) reads contact $=$ exchange:

$$C_4\cdot(\text{companion value, not reproduced here}) \;=\; 3\,\{T^3\}^2\,P_T\,K_f. \tag{2.5}$$

Under $\lambda=\tfrac12$: the left side carries $C_4\to\lambda C_4$; on the right,
$\{T^3\}^2\to\lambda^2\{T^3\}^2$ and $P_T\propto 1/g(T,T)\to\lambda^{-1}P_T$, so the right
side carries $\lambda^{2-1}=\lambda$ as well. The identity is homogeneous of degree 1 in
$\lambda$ and $K_f$ is unchanged. Had I miscounted the correlators in any of the three
factors, this check would have failed by a power of 2 — it is the sharpest consistency test
available on the table and it is not circular (it composes three rows fixed independently).

## 3. Verification on a shared quantity (deliverable 2)

### 3.1 The quantity: the ghost three-point function on the sphere

The sister project states (039 eq. 3.2)

$$\mathcal G_3:=\langle c\bar c(z_1)\,c\bar c(z_2)\,c\bar c(z_3)\rangle
 =2\nu\,|z_{12}z_{13}z_{23}|^2
 \;\stackrel{\nu=-1}{=}\;-2\,|z_{12}z_{13}z_{23}|^2. \tag{3.1}$$

I compute the same object **from the book's base correlator alone**, without using (3.1) or
$\nu$, and then compare through the table.

\subsection*{Setup}

A1, A2, A4. $c(z)=\sum_n c_n z^{-n+1}$, $\bar c(\bar z)=\sum_n\bar c_n\bar z^{-n+1}$ (039 K6,
standard in the book's `cft_brst`), state–operator map $c\bar c(0)\leftrightarrow
c_1\bar c_1|0\rangle$ in this order.

\subsection*{Derivation}

Only the modes $\{c_{-1},c_0,c_1\}$ saturate, with $z$-exponents $1-n\in\{2,1,0\}$:

$$\langle c(z_1)c(z_2)c(z_3)\rangle
 =\langle c_{-1}c_0c_1\rangle\sum_{\sigma\in S_3}\operatorname{sgn}(\sigma)\,
 z_1^{e_{\sigma(1)}}z_2^{e_{\sigma(2)}}z_3^{e_{\sigma(3)}},
 \qquad e=(2,1,0). \tag{3.2}$$

$$\sum_\sigma\operatorname{sgn}(\sigma)\,\prod_i z_i^{e_{\sigma(i)}}
 =\det\!\big[z_i^{e_j}\big]
 =-\prod_{i<j}(z_j-z_i)
 =z_{12}z_{13}z_{23}, \tag{3.3}$$

$$\langle c(z_1)c(z_2)c(z_3)\rangle=\langle c_{-1}c_0c_1\rangle\,z_{12}z_{13}z_{23},
\qquad
\langle \bar c(\bar z_1)\bar c(\bar z_2)\bar c(\bar z_3)\rangle
 =\langle \bar c_{-1}\bar c_0\bar c_1\rangle\,\bar z_{12}\bar z_{13}\bar z_{23}. \tag{3.4}$$

Reordering the interleaved product into the separated one costs the parity of the
permutation $(1,2,3,4,5,6)\mapsto(1,3,5,2,4,6)$ acting on six odd objects:

$$c\bar c(z_1)c\bar c(z_2)c\bar c(z_3)
 = -\,c(z_1)c(z_2)c(z_3)\,\bar c(\bar z_1)\bar c(\bar z_2)\bar c(\bar z_3), \tag{3.5}$$

and the same permutation relates the two orderings of the zero-mode string:

$$c_{-1}\bar c_{-1}c_0\bar c_0c_1\bar c_1
 = -\,c_{-1}c_0c_1\,\bar c_{-1}\bar c_0\bar c_1. \tag{3.6}$$

The two signs cancel, and with the book's
$\langle c_{-1}\bar c_{-1}c_0\bar c_0c_1\bar c_1\rangle=-1$,

$$\boxed{\;\mathcal G_3
 =\langle c_{-1}\bar c_{-1}c_0\bar c_0c_1\bar c_1\rangle\,|z_{12}z_{13}z_{23}|^2
 =2\nu\,|z_{12}z_{13}z_{23}|^2
 \stackrel{\rm book}{=}-|z_{12}z_{13}z_{23}|^2.\;} \tag{3.7}$$

\subsection*{Commentary}

(3.3): the determinant of $[z_i^{e_j}]$ with $e=(2,1,0)$ is the Vandermonde with its columns
reversed — one transposition, hence the leading minus, and
$-\prod_{i<j}(z_j-z_i)=-(-z_{12})(-z_{13})(-z_{23})=z_{12}z_{13}z_{23}$.

(3.5)–(3.6): the permutation has three inversions among the odd entries, parity $-1$. This is
the only sign in the computation that is easy to get wrong, and it is the one that makes the
two conventions agree rather than differ by a sign; it is checked by explicit permutation
parity in the script (`C3.2`).

(3.7): the middle equality uses $c_0^-c_0^+=\tfrac12c_0\bar c_0$, i.e.
$2\nu=\langle{\rm base}\rangle$. The identity $\mathcal G_3=2\nu|z_{12}z_{13}z_{23}|^2$ is
therefore true in *any* normalisation — which is exactly why the comparison below tests the
sign and not the magnitude.

\subsection*{Result}

$$\frac{\mathcal G_3^{\rm book}}{\mathcal G_3^{\rm sister}}
 =\frac{-1}{-2}=\frac12=\lambda, \tag{3.8}$$

the table's conversion factor, and the signs agree.

\subsection*{Verification}

`codes/verify-conventions.py`, checks `C3.1` (Vandermonde coefficient against a direct
symbolic Grassmann evaluation of the mode sum), `C3.2` (permutation parity of (3.5)–(3.6),
computed by inversion counting and independently by a Clifford/matrix realisation of six
anticommuting generators), `C3` (the ratio (3.8)), with break controls on the parity and on
the base value.

### 3.2 What this check does and does not establish

**Does.** It establishes the *sign* of the conversion — the only part of Q1 that could have
been a genuine disagreement — by two logically independent routes: the book's declared
vacuum normalisation plus mode algebra (here), and the sister's kinetic anchor "$V=-\tau^2$
for a canonically normalised tachyon" (039 eq. 1.4, which uses no vacuum normalisation at
all). It also establishes that the derived identity $\mathcal G_3=2\nu|z_{12}z_{13}z_{23}|^2$
is common to both, so the table's $\lambda^1$ counting is right on this row.

**Does not.** It does not test the magnitude $\lambda=\tfrac12$: that magnitude *is* the
convention being translated, and any check built from the two normalisations reproduces it
tautologically. There is at present no quantity computed independently from a vertex integral
on both sides — this project ships no vertex engine and imports every ghost-sector number, so
the brief's item 2 cannot be met in its strongest form with the available files, and I do not
claim it is.

**Cheapest quantity that would serve** (C3.3): Stage 0, $\{T^3\}(\beta)=C_3\beta^6$ with the
SL(2,C) cubic maps $\rho_a=1/\beta$. In the book's normalisation $C_3=+1$, so
$\{T^3\}_{\rm book}=\beta^6$ against the sister's (companion value, not reproduced here)
(R3). Recomputing it here from (3.7) plus the mapping radii — half a day of work, no moduli
integral — would give a genuinely independent determination of $C_3$ in this project's
conventions and would upgrade the magnitude half of the check from tautology to result.
That is the request to record.

## 4. Q2: the measure orientation — decision (deliverable 3)

### 4.0 The arithmetic, which is not in dispute

$$\omega_p^{\rm book}\propto(2\pi\mathrm i)^{-\mathcal M^c_{g,n}}
 =\Big(\frac{-\mathrm i}{2\pi}\Big)^{N-3},
\qquad
\omega^{\rm BZ}\propto\Big(\frac{\mathrm i}{2\pi}\Big)^{N-3},
\qquad
\frac{\omega^{\rm book}}{\omega^{\rm BZ}}=(-1)^{N-3}. \tag{4.1}$$

(`bos_offshell_amplitudes.tex` eq. `bos:eq:omega-p`, l. 149–158, at genus 0
$\mathcal M^c_{0,N}=N-3$; BZ eq. 4.10.) At $N=3$ the two agree; at $N=4$ they differ by a
sign. Read with the sister project's orientation conventions O1–O4 — $\dd x\wedge\dd y>0$ on
$\mathcal M_{0,4}$, $B(\partial_x)B(\partial_y)$ in that order, $\oint\dd\bar w/2\pi\mathrm i
=+\operatorname{Res}_{\bar w}$, BPZ bra with $I(z)=\pm1/z$ — the book's reading gives
$C_4>0$ and $K_f=-1$; BZ's gives $C_4<0$, $K_f=+1$.

### 4.1 Why this is a question of fact, not of convention

$C_3$ is untouched by (4.1) and $C_4$ is not. The ratio $C_4/C_3^2$ is fixed by
factorisation of the four-point amplitude on the tachyon pole — a physical requirement — so
the two transcriptions cannot both be right. Equivalently: $K_f$ is determined, and it is
$+1$ or $-1$, not a choice. What *is* conventional and must not be confused with it: the
overall sign of $C_N$ from the potential-vs-action side ($V=-S$), and the $\lambda$ of §1,
neither of which moves $C_4/C_3^2$.

### 4.2 The evidence, both ways

**For BZ's $\mathrm i/2\pi$ (branch A, status quo in the sister project).**

- SL R37 is a `Verified` row (40/40 checks) resting on derivation 039 §6 and §7: two routes —
  the Feynman region of $\mathcal M_{0,4}$ reproducing the exchange term of the action, and
  the tachyon-pole residue of the on-shell four-point function — both fix
  the sign of $\mathcal M_4\mathcal B_4$, i.e. BZ's sign. The routes share the exchange term and
  the factorisation principle; they are independent only in the string-side evaluation, and
  039 says so.
- The $t^4$ sewing identity closes with $K_f=+1$ and nothing fitted (SL R30, R36).
- The book's own source flags the sign of $2\pi\mathrm i$ in the measure
  $\dd m_r\wedge\dd m_i$ as to be checked (a TODO in `bos_offshell_amplitudes.tex`). The
  external argument for the minus sign is a second vote for branch A.

**For the book's $(2\pi\mathrm i)^{-1}$ (branch B).**

- Harold's ruling that all projects adopt the book's conventions, taken at face value.
- The prefactor in the book is uniform in $p$ and in $g$, and the book states it as a
  definition rather than deriving it from an orientation; if the intended orientation
  differs from O1–O4 at any one of the four places, the apparent conflict dissolves and both
  sources say the same thing. Nothing I read rules this out: 039's own footnote-ready
  statement is careful to call it "a statement about a reading of the book, not about an
  error in it".

**My reading, offered and not acted on.** Branch A is better supported: two derivations
against one unmotivated definition, plus the book's own TODO and the external argument for the opposite sign. But
the cheap decisive move is not to weigh votes — it is to settle the orientation the book
intends, which is one question: *with $B(\partial_x)B(\partial_y)$ in that order
and $\dd x\wedge\dd y$ positive, is `bos:eq:omega-p`'s $(2\pi\mathrm i)^{-\mathcal M^c}$
meant literally?* If yes, branches A and B genuinely conflict and the book has an erratum at
that equation; if the intended orientation is the other one, there is nothing to decide and
the book's $C_4$ is negative after the $\lambda$ of §1.

### 4.3 Consequences on this project's side

| Object here | Branch A (BZ, $C_4<0$ potential side) | Branch B (book, $C_4>0$) |
|---|---|---|
| R15 clause (2), Schwinger form of $V_4^{-1}$ | $\operatorname{spec}(m_2)$ all negative ⇒ $\int_0^\infty\dd t\,e^{-tm_2}$ **diverges**; the unconditional form $\int_0^\infty\dd t\,m_2e^{-tm_2^2}$ is the one to use | $\operatorname{spec}(m_2)$ all positive ⇒ the direct Laplace form **converges**, at rate the gap, and equals $m_2^{-1}$ |
| R15's *statement* | unchanged — the row is an iff ("valid **iff** positive definite"), and its truth does not depend on the branch | unchanged |
| R15 clause (3), "sign open ($C$ symbolic)" | now closed as $C<0$ | now closed as $C>0$ — either way the row's carve-out is discharged, by the branch chosen |
| PH1 (a) (invertibility / kernel stabilisation) | unaffected: (companion value, not reproduced here), in both | unaffected |
| PH5 (no kernel at generic momentum) | unaffected — a rank statement | unaffected |
| PH21 (Neumann chain convergence) | unaffected: $\rho(D^{-1}N)$ (companion value, not reproduced here) are invariant under an overall sign of $V_4$ ($D$ and $N$ flip together) | unaffected |
| PH3, PH18 (zeros of $\det V_4^{(L)}(P^2)$) | unaffected: a determinant's zeros do not move under $V_4\to-V_4$ | unaffected |
| $K_f$ | absent from this project's ledger (0 occurrences) | absent |
| magnitudes: gap, $\lVert m_2^{-1}\rVert$, eigenvalues | unchanged by Q2 (changed by Q1 only, $\times2$) | unchanged by Q2 |
| `knowledge/topics/sl2c-data-request-2026-09-22.md` §1, row 3 | "negative potential-side" stands | must read "positive" |

**Upshot for this project: Q2 is nearly inert here.** It changes no row's statement, no
hypothesis, and no magnitude. It changes one reading (which Laplace representation to use in
R15) and one word in a note. The reason is structural: everything this project currently
reads from the sister is either a rank, a ratio, or a magnitude, and Q2 is a global sign on
$V_4$. The stakes of Q2 are on the sister project's side (R8, R30, R36, R37, R41, R49 and
the paper-2 footnote), not here — which is worth saying plainly when the decision is put.

## 5. Change-set per project (deliverable 4)

### 5.1 This project — proposed, **not applied**

| # | File | Edit | Depends on Q2? |
|---|---|---|---|
| 1 | the project conventions, *Shared files and conventions* → Physics conventions | After "normalization $\langle c_{-1}\bar c_{-1}c_0^-c_0^+c_1\bar c_1\rangle=-1/2$, no factor $i$", add: "with $c_0^\pm=\tfrac12(c_0\pm\bar c_0)$, $b_0^\pm=b_0\pm\bar b_0$, in the ordering $c_0^-c_0^+$; equivalently $\langle c_{-1}\bar c_{-1}c_0\bar c_0c_1\bar c_1\rangle=-1$ (Erbin 2023, `bos:eq:ws-closed-vacuum-normalization`). Sister-project numbers are quoted with $\nu=-1$: convert by $\times\tfrac12$ per sphere correlator (record 041)." No value changes. | no |
| 2 | `knowledge/results.md` | New row (next free ID) — *Convention anchor: the ghost-sector translation between this project, the SL(2,C) project and Erbin 2023; $\lambda=\tfrac12$ per sphere correlator, $\tfrac14$ on $G_2$, $\times2$ on $\operatorname{spec}(m_2)$; $c_0^\pm$, $b_0^\pm$, ordering and signs identical on all three sides.* Status `Verified` (`codes/verify-conventions.py`), source `agent/derivations/041-convention-reconciliation.md#C1`. | no |
| 3 | `knowledge/results.md`, R15 | Annotation: clause (3)'s "sign open ($C$ symbolic, sister O3)" is closed by SL R37 modulo Q2; state which Schwinger representation applies on the branch adopted. The row's statement is unchanged. | yes (wording only) |
| 4 | `knowledge/topics/sl2c-data-request-2026-09-22.md` §1, ¶2 | Replace "every magnitude below therefore carries an unresolved factor (2 per strand, 4 on $\mathrm{Sym}^2$), unless the difference turns out to be a $c_0^\pm$ normalisation convention …, which is not decided here" by the settled statement: the $c_0^\pm$ definitions agree, the difference is the vacuum normalisation, convert $V_4$ by $\tfrac12$, $G_2$ by $\tfrac14$, $\operatorname{spec}(m_2)$ by $2$ (record 041). | no |
| 5 | same note, §2 head | The "Blocking open item: the convention translation" is discharged for Q1; re-scope it to Q2 and to the Stage-0 recomputation of §3.2, or delete it and point to record 041. | no |
| 6 | same note, §1 table row 3 | Add the Q2 caveat to "negative potential-side". | yes |
| 7 | `codes/verify-conventions.py` | New file (written with this record). | no |

### 5.2 Companion SL(2,C) project

[Correspondence with the companion project removed.]

## 6. Convention versus physics — the explicit statement

| Quantity | Under Q1 ($\lambda=\tfrac12$) | Under Q2 ($(-1)^{N-3}$) | Status |
|---|---|---|---|
| $\nu$, $g$, $G_2$, $V_4$, $\{T^N\}$, $C_N$, $\operatorname{spec}(m_2)$ magnitudes, $\lVert m_2^{-1}\rVert$ | scale | — | convention (field/coupling normalisation) |
| $\operatorname{sign}\nu$, $m_T^2=-4/\alpha'$, rank $V_4$, signature of $G_2$, eigenvalue ratios, $\hat\lambda$, $\rho(D^{-1}N)$, zeros of $\det V_4(P^2)$ | invariant | invariant | physics |
| $C_4/C_3^2$, $K_f$, $\operatorname{sign}\operatorname{spec}(m_2)$ | invariant | **flip** | physics — hence Q2 is a right/wrong question, not a choice |
| overall sign of $C_N$ (potential vs action side, $V=-S$) | — | — | convention, independent of Q2 and composing with it |

Any claimed physical consequence that moves under Q1 is an error; nothing in §2–§3 moves.
Something physical *does* move under Q2, which is exactly why it cannot be settled by a
ruling about which conventions to use.

*Annotation 2026-10-01 (bookkeeping, no re-derivation).* Node check `agent/reports/critic-r43-rescaling-node-20261001T153000.md` found the coupling relation of C1.4 and eq. (1.3) written inverted; corrected to $\kappa_{\rm sister}=\sqrt2\,\kappa_{\rm book}$ ($\Psi_{\rm book}=\sqrt2\Psi_{\rm sister}$ unchanged), the direction the record's own algebra already had. No number in the record depends on it. The companion script gains a direction-sensitive check with a reversed-map break leg.
