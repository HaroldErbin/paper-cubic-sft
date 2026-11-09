# 048 – χ-scheme $O(g_s^5)$ matching: model, lower legs, saddle harness, and the seven tests

Briefs: `agent/briefs/active-computator-chi-matching-20260922T154000.md` (sub-task 1),
`agent/briefs/active-computator-chi-matching-2-20260922T164500.md` (sub-task 2). Companion
script: `codes/verify-chi-ogs5-matching.py`. Continuation of record 038 (R42).

## Status

Fix pass 2 after critic iteration 2 complete (2026-09-22): §12 resolution table; **new §8.8**
settles which order the C6 statistic measures (eq. (8.3), two gates stated before their
numbers, diagnostic run `agent/scratch/c6-order-diagnostic.log`, script `c6_diagnostic`,
$\approx$ 13 min); §8.5 gate discrepancy and the withdrawn seed-23 attribution; §8.7 ladder
wording; §9 R42 appendix; §10 item 4; claim tree C6, C9, `Open gaps`. The main run was **not**
re-run — no check changed — so the counts and numbers of §8.1–§8.4, §8.6, §9 stand: 108
independent + 9 derived checks + 24 break legs, two failures (`C6-scan`, `C6-artefact`, seed
23 at $b'_\chi=0.1$), exit 1.

C1–C5, C7, C8 established on three seeds. C6: its $O(g_s^5)$ out-of-span statement is
established on three seeds; two gaps remain inside it (what the coefficient measures; the
cause of the two failing scan legs). Next: orchestrator — promote R49, the PH16 note and the
PH15 line as written; the R42 appendix is rewritten in §9 and now carries the C6 qualification.

## Task and objective

**Literal task.** In the finite-dimensional random-tensor model of `codes/verify-chi-partner.py`,
test whether the χ-scheme action $S^\chi_5$ of 038 §6.1 reproduces the closed-SFT tree effective
action through $O(g_s^5)$. Sub-task 1: skeleton, model, joint Newton saddle in
$(\Sigma_2,\chi,\Sigma_3)$ at fixed $\Psi$ with Richardson extrapolation, calibration on the
$O(g_s^3)$ and $O(g_s^4)$ legs with $(a_\chi,b_\chi)=(1,2)$ (R24), and the projection basis
$\{V_7(\Psi^7),S_1,S_2,S_3\}$ with its Gram matrix. Nothing new is fitted there. Sub-task 2:
measure the $O(g_s^5)$ deficit, project it, fit $(c_\chi,d_\chi,a_7)$ each from its own
direction, and run the seven tests C1–C7 of 038 §6.2.

**Objective.** R42 is a counting result; the matching is what tests it. Its sharpest predictions
are the diagonality of the $3\times3$ system, the absence of $S_3$ (N3) and of any component
outside the span (N3′), and $\beta(c_6)=7(2+c_6)/5$. The harness built in sub-task 1 must be
trusted before any of those is measured, hence the calibration-first order.

## Conventions and model

No `knowledge/conventions.md` in this project; conventions are those of `codes/verify-chi-partner.py`
and 038, restated only where the model needs them:

- $\mathcal H_0=\mathbb R^N$, $N=4$; $V_k$ are fully symmetric random $k$-tensors (Gaussian,
  symmetrised), $k=2,\dots,7$; $\Psi\in\mathbb R^N$ random. No $L_\infty$ input (A4 of 038).
- $\Sigma_2,\chi\in\mathrm{Sym}^2$, $\Sigma_3\in\mathrm{Sym}^3$ (dimensions 10, 10, 20).
  $P=\Psi\otimes\Psi$, $p_3=\Psi^{\otimes3}$.
- Contractions $V_k(A,B,\dots)$ are full index contractions of the symmetric tensor with the
  slot arguments (einsum); $V_k(\Psi^k)$ is the contact.
- Target: $S_{\rm eff}(g)=\sum_{k=2}^{7}\frac{g^{k-2}}{k!}V_k(\Psi^k)$, the tree effective
  action of the polynomial toy (all exchange classes cancel by the HS pairs; the contact is what
  must be reproduced, as in `verify-chi-partner.py`).
- Mismatch $D_n(g)=[S^\chi_5(\text{saddle};g)-S_{\rm eff}(g)]/g^n$; Richardson
  $2D_n(g_0/2)-D_n(g_0)$ removes the $O(g)$ term.
- Basis invariants as in `codes/verify-chi-ogs5-count.py` (`invariants`): $x=V_4^{-1}v$ on
  $\mathrm{Sym}^2$, $v=V_5(\cdot,P,\Psi)$, $S_1=V_5(x,x,\Psi)$, $S_2=V_6(x,P,P)$, $S_3$ the
  strand-split representative. Same normalisation, reused verbatim.

### Action transcribed from 038 §6.1

$$
\begin{aligned}
S^\chi_5=\;&\tfrac12V_2(\Psi^2)+\tfrac{g}{3!}V_3(\Psi^3)
  -\tfrac{g^2}{4!}V_4(\Sigma,\Sigma)+\tfrac{2g^2}{4!}V_4(\Sigma,P)
  +\tfrac{g^3}{5!}V_5(\Sigma,\Sigma,\Psi)\\
 &+\tfrac{g^2}{4!}a_\chi V_4(\chi,\chi)+\tfrac{g^3}{5!}b_\chi V_5(\chi,\Sigma,\Psi)
  +\tfrac{g^3}{5!}c_\chi V_5(\chi,\chi,\Psi)\\
 &+\tfrac{g^4}{6!}c_6V_6(\Sigma,\Sigma,\Sigma)
  +\tfrac{g^4}{6!}\big[-c_{\Sigma_3}V_6(\Sigma_3,\Sigma_3)+2c_{\Sigma_3}V_6(\Sigma_3,\Sigma_2,\Psi)\big]
  +\tfrac{g^4}{6!}d_\chi V_6(\chi,\Sigma,\Sigma)\\
 &+\tfrac{g^5}{7!}a_7V_7(\Sigma_3,\Sigma_3,\Psi)
  \;\big[+\tfrac{g^3}{5!}b'_\chi V_5(\chi,\Sigma_3)\ \text{break leg only}\big].
\end{aligned}\tag{1.1}
$$

### Free constants (all listed before assembly)

| constant | value | fixed by |
|---|---|---|
| $a_\chi,b_\chi$ | $(1,2)$ | R24, $O(g_s^4)$ sector; $a_\chi=1$ is the $GL(2)$ normalisation |
| $c_6,c_{\Sigma_3}$ | $(0,1)$ | pinned by convention (A4); sum $=1$ from the $O(g_s^4)$ sextic contact; scanned in C7 |
| $b'_\chi$ | $0$ | condition (E4), A3; switched on only as the break leg C6 |
| $\Sigma_3$ kinetic normalisation $\lambda$ | $1$ | field rescaling $\Sigma_3\to\lambda\Sigma_3$; C3 tests independence |
| basis normalisation of $S_1,S_2,S_3$ | as in `verify-chi-ogs5-count.py` | convention only; the fitted $c_\chi,d_\chi$ are quoted against it |
| $c_\chi,d_\chi,a_7$ | fitted in sub-task 2 | each from its own projection direction (A6) |

Nothing is fitted from the closure residual; the closure test (residual slope $\ge6$) uses
none of the fitted constants twice.

## Claim tree

Assumptions (the nine conditions of `agent/reports/computator-038-fixpass2-20260921T201500.md`):

- **A1** Field content $(\Psi,\Sigma_2,\chi,\Sigma_3)$, elementary (bare geometric) vertices only; action (1.1).
- **A2** $(a_\chi,b_\chi)=(1,2)$ from R24; only $b_\chi^2/a_\chi=4$ is physical.
- **A3** $b'_\chi=0$: no $V_5(\chi,\Sigma_3)$ mixing (E4).
- **A4** Sextic split pinned $c_6=0$, $c_{\Sigma_3}=1$; $d_\chi$ reported as $d_\chi(c_6)$; $c_6$ never fitted from the closure residual.
- **A5** $V_7$ partition on $(3,3,1)$: $a_7V_7(\Sigma_3,\Sigma_3,\Psi)$.
- **A6** Only $(c_\chi,d_\chi,a_7)$ are fitted, each from its own direction in 038 (5.1).
- **A7** Joint Newton saddle in $(\Sigma_2,\chi,\Sigma_3)$ + Richardson; no sequential closed-form elimination.
- **A8** Standing hypotheses PH14, PH15, PH16, PH23 and the carve-out 038 A4/A5–A7 (finite-dimensional algebraic layer, generic tensors).
- **A9** The seven tests of 038 §6.2 are the claims C1–C7 below, including the $c_6$ scan.
- **A10** (local, model) $N=4$, seeds $\{7,23,11\}$, $\Psi$ random per seed; Richardson at $g_0=10^{-2}$; slope windows as stated in §3; $O(g_s^5)$ extrapolation as in §7.1.

Hypotheses: none new; PH14–PH16, PH23 cited by ID (A8).

Claims (C0 is the harness, sub-task 1; C1–C7 are the seven tests of 038 §6.2; C8 the
extrapolator and its predictions; C9 the root):

- **C0** Under PH14–PH16, PH23, the harness is right: with $(a_\chi,b_\chi)=(1,2)$, $c_6=0$, $c_{\Sigma_3}=1$ and $c_\chi=d_\chi=a_7=0$, the joint saddle reproduces $S_{\rm eff}$ through $O(g_s^4)$ ($D_3\to0$, $D_4\to0$), and the no-χ and $b_\chi=1$ break legs reproduce the R24 values. [by C0.1–C0.4]
  - **C0.1** The analytic gradient of (1.1) agrees with a finite-difference gradient at random $(\Sigma_2,\chi,\Sigma_3)$. [eq. (3.1); by check: C0.1-gradient]
  - **C0.2** $O(g_s^3)$ leg: $D_3\to0$. [by A1, A2, A7; by check: C0.2-D3]
  - **C0.3** $O(g_s^4)$ leg: $D_4\to0$ at $c_6=0$ (Σ₃ pair supplies the sextic contact) and for $c_6\in\{0,\tfrac12,1\}$; without χ, $D_4\to vV_4^{-1}v/600$; with $b_\chi=1$, $D_4\to\tfrac34vV_4^{-1}v/600$ (R24 break legs). [by A1, A2, A4, R24; by check: C0.3-D4-closure, C0.3-D4-nochi, C0.3-D4-chi(1,1)]
  - **C0.4** Residual with the $O(g_s^4)$ action is $O(g_s^5)$: log-log slope of $D_4$ in $[0.7,1.5]$, three seeds. [by check: C0.4-slope]
- **C0.5** The projection basis $\{V_7(\Psi^7),S_1,S_2,S_3\}$ sampled on random $\Psi$ probes has a non-singular Gram matrix (rank 4, condition number reported; §5). [by check: C0.5-gram]
- **C8** (sub-task 2) The extrapolator (7.1) with the probe-adapted window of §7.1 measures the $O(g^5)$ coefficient of the mismatch; $\alpha=-42/25$ and $\beta(c_6)=7(2+c_6)/5$ are its predicted $S_1,S_2$ components, and $-1$ its predicted $V_7$ component; the ladder satisfies the stopping rule of §8.7. [§7.2, eq. (7.5)–(7.6); by A1, A2, A4, A7, C0; by check: C8-stop. The 018 triple $(1,\frac{42}{25},-\frac{14}{5})$ is a dressed-scheme coincidence, not a check (038 §3.3)]
- **C1** (test 1) Diagonality: perturbing $c_\chi$ moves only the $S_1$ component, $d_\chi$ only $S_2$, $a_7$ only $V_7$, with the sizes (7.5) predicts. [§8.2; by C8, C0.5; by check: C1-diag, C1-size]
- **C2** (test 2) The deficit has no $S_3$ component (N3) and no component orthogonal to the four-element set (N3′), reported separately. [§8.1; by C8, C0.5; by check: C2-S3, C2-perp, C2-V7. Seed 23 at $1.8\cdot10^{-2}$ against a $5\cdot10^{-2}$ gate, converging (§8.7)]
- **C3** (test 3) The deficit is independent of the $\Sigma_3$ kinetic normalisation; the one $M^{-1}$ composite is $O(g_s^6)$; and $c_5$ is unchanged under a perturbation $M\to M+\varepsilon\Delta$ of the $\Sigma_3$ kinetic form with $\Delta p_3=0$, which leaves the leading saddle and the $O(g_s^4)$ contact fixed (N4, falsifiable form). [§8.3; by A1, A7, C8; by check: C3-reparam, C3-Minv, C3-N4]
- **C4** (test 4) $\alpha,\beta$ of 038 (3.1) measured; $(c_\chi,d_\chi,a_7)=(1,2+c_6,1)$, each from its own direction; $b_\chi^2/a_\chi=4$ survives (N7). [§8.1; by C8, C1, A6; by check: C4-alpha, C4-beta, C4-fit, C4-outofsample]
- **C5** (test 5) $O(g_s^3)$, $O(g_s^4)$ legs untouched by the fitted couplings; closure residual slope $\ge6$. [§8.4; by C0.2, C0.3, C4; by check: C5-D3, C5-D4, C5-slope]
- **C6** (test 6) Break leg: $b'_\chi\ne0$ produces a component outside $\mathrm{span}\{V_7,S_1,S_2,S_3\}$ whose coefficient exceeds the smallest one C2-perp detects, grows with $b'_\chi$, and is flat under refinement of the extrapolator. The superseded design (uncompensated $b_\chi$) measured instead the reparametrisation $b_{\rm eff}=b_\chi+b'_\chi$ of the $O(g_s^4)$ sector. [§8.5, §8.8, eq. (8.1)–(8.3); by A3 lifted, C8, C2; by check: C6-outside, C6-scan, C6-artefact, C6-ladder, and the order diagnostic §8.8 — **established as an $O(g_s^5)$ out-of-span statement on three seeds** ($10.7$, $3.5$, $33.9$ times $\gamma_{\min}$; window-refinement gate 2 of §8.8 flat to $1$–$8\%$ where an $O(g_s^4)$ leakage would have grown threefold). **[GAP]** The coefficient does *not* measure the $\Sigma_3$ mixing direction: its $b_{\rm eff}^2$ law ($2.00$, $1.97$, $2.00$) identifies the dominant structure as the $b_{\rm eff}^2b_\chi'^2$ composite dressing of (8.3), not the $b_{\rm eff}b'_\chi$ mixing source. The two scan legs at $b'_\chi=0.1$ fail on seed 23 for a reason **not identified** (§8.5, attribution withdrawn on fix pass 2)]
- **C7** (test 7) Scan $c_6\in\{0,\tfrac12,1\}$: $\beta(c_6)=7(2+c_6)/5$, $\alpha$ independent of $c_6$, $d_\chi(c_6)=2+c_6$. [§8.6; by C8, C4; by check: C7-beta, C7-alpha]
- **C9** (root) Under A1–A10 and PH14–PH16, PH23, the χ-scheme action $S^\chi_5$ of 038 §6.1 reproduces the tree effective action of the random-tensor model through $O(g_s^5)$, with the couplings of C4, and R42's count is confirmed. [§9; by C0, C1, C2, C3, C4, C5, C7; C6 is the falsification leg: its $O(g_s^5)$ out-of-span statement is established on three seeds (§8.5, §8.8), its reading as a measurement of the $\Sigma_3$ mixing direction is a gap]

Open gaps: two, both inside C6 and neither touching C1–C5, C7. (i) The C6 out-of-span coefficient is an $O(g_s^5)$ quantity (§8.8 gate 2) but is dominated by the $b_{\rm eff}^2b_\chi'^2$ composite-dressing structure of (8.3), not by the $b_{\rm eff}b'_\chi$ $\Sigma_3$-mixing structure; separating the two needs the explicit $S_4$ column (§8.8, §10 item 2). (ii) The two auxiliary scan legs at $b'_\chi=0.1$ fail on seed 23 for an unidentified reason (§8.5); the fix-pass-1 attribution to the $O(g_s^4)$ compensation defect is withdrawn.
Hypotheses in force: PH14, PH15, PH16, PH23

## Sub-tasks

1. Skeleton; model + joint saddle + Richardson; calibration C0.1–C0.4; basis C0.5.
2. Measure $7!c_5$ at $c_\chi=d_\chi=a_7=0$ on $\Psi$ probes, project on the basis (C2, C4),
   fit $(c_\chi,d_\chi,a_7)$ each from its own direction (C4), then C1, C3, C5, C6, C7.

## 3. Model and harness

\subsection*{Setup}

Uses A1, A2, A3, A4, A5, A7, A10. Symbols: $S=\Sigma_2$, $C=\chi$, $T=\Sigma_3$ (full symmetric
tensors), $y\in\mathbb R^{40}$ their independent components ($10+10+20$), $E_k$ the embedding
$y\mapsto$ full tensor of $\mathrm{Sym}^k$, $k_{sp}$ the coefficient of $V_4(\Sigma,P)$
($k_{sp}=2$ nominal; a break-leg knob only).

\subsection*{Derivation}

The saddle equations are the reduced gradients $E_k^{\!\top}\partial S/\partial(\text{full entries})$,
i.e. the full-entry gradient summed over the distinct permutations of each index multiset. From
(1.1), with entries treated as independent and every $V_k$ fully symmetric:

$$
\begin{aligned}
\partial_S S^\chi_5&=-\tfrac{g^2}{12}V_4(\cdot,S)+\tfrac{k_{sp}g^2}{24}V_4(\cdot,P)
 +\tfrac{g^3}{60}V_5(\cdot,S,\Psi)+\tfrac{b_\chi g^3}{120}V_5(\cdot,C,\Psi)
 +\tfrac{c_6g^4}{240}V_6(\cdot,S,S)\\
 &\quad+\tfrac{2c_{\Sigma_3}g^4}{720}V_6(\cdot,T,\Psi)+\tfrac{d_\chi g^4}{360}V_6(\cdot,C,S),\\
\partial_C S^\chi_5&=\tfrac{a_\chi g^2}{12}V_4(\cdot,C)+\tfrac{b_\chi g^3}{120}V_5(\cdot,S,\Psi)
 +\tfrac{c_\chi g^3}{60}V_5(\cdot,C,\Psi)+\tfrac{d_\chi g^4}{720}V_6(\cdot,S,S)
 +\tfrac{b'_\chi g^3}{120}V_5(\cdot,T),\\
\partial_T S^\chi_5&=-\tfrac{c_{\Sigma_3}g^4}{360}V_6(\cdot,T)+\tfrac{2c_{\Sigma_3}g^4}{720}V_6(\cdot,S,\Psi)
 +\tfrac{a_7g^5}{2520}V_7(\cdot,T,\Psi)+\tfrac{b'_\chi g^3}{120}V_5(C,\cdot).
\end{aligned}\tag{3.1}
$$

The root-finder sees $(\partial_S,\partial_C)/g^2$ and $\partial_T/g^4$ (the $\Sigma_3$
kinetic is $O(g^4)$), started from $(S,C,T)=(P,0,p_3)$, `scipy.optimize.root(method='hybr')`,
`tol=1e-14`, accepted only if the scaled gradient is $<10^{-9}$ (assertion). Leading saddle:
$S=P+O(g)$, $C=O(g)$, $T=p_3+O(g)$ (038 N2), which makes the $\Sigma_3$ HS pair reproduce
$\tfrac{g^4}{6!}c_{\Sigma_3}V_6(\Psi^6)$ and the $\Sigma_2$ pair $\tfrac{g^2}{4!}V_4(\Psi^4)$ at
leading order, as the calibration must find.

The mismatch $D_n(g)=[S^\chi_5(\text{saddle})-S_{\rm eff}(g)]/g^n$ is extrapolated by the
two-point Richardson $2D_n(g_0/2)-D_n(g_0)$ at $g_0=10^{-2}$; the log-log slope of $|D_4|$ is
fitted on $g\in\{1,0.7,0.5,0.35,0.2\}\times3\cdot10^{-2}$.

\subsection*{Commentary}

(3.1): the prefactors are the multiplicities of the differentiated slot: $V_4(S,S)\to2$,
$V_5(S,S,\Psi)\to2$, $V_6(S,S,S)\to3$, $V_6(T,T)\to2$, $V_7(T,T,\Psi)\to2$, $V_6(C,S,S)\to2$ for
$S$ and $1$ for $C$. Under $c_{\Sigma_3}=0$ (the $c_6=1$ endpoint of the scan) and $a_7=b'_\chi=0$
the $T$-gradient vanishes identically: $\Sigma_3$ decouples and the solver's $T$-block is
trivially stationary; this is the physics ($c_{\Sigma_3}=0$ means no $\Sigma_3$), not a
convergence artefact. A different scaling per sector is what keeps `hybr`'s tolerance
meaningful at $g\sim10^{-3}$ for the $O(g^4)$ block.

The gradient (3.1) is not trusted from its transcription: check C0.1 compares it with a central
finite difference in the reduced coordinates at $g=0.3$ with every coupling switched on
($c_\chi,d_\chi,a_7,c_6,b'_\chi\neq0$), and the break leg halves the $d_\chi$ term of $\partial_S$.

## 4. Calibration entries

All numbers from `codes/verify-chi-ogs5-matching.py`, run 2026-09-22, seeds $(7,23,11)$,
$N=4$, nominal couplings $(a_\chi,b_\chi,c_6,c_{\Sigma_3})=(1,2,0,1)$, $c_\chi=d_\chi=a_7=b'_\chi=0$.
Scale $=|vV_4^{-1}v|/600$ (the R24 residual) $=0.655,\;7.04,\;2.136$ for the three seeds.

| check | seed 7 | seed 23 | seed 11 | gate |
|---|---|---|---|---|
| C0.1 gradient vs FD, max rel | $1.1\cdot10^{-10}$ | $3.0\cdot10^{-10}$ | $1.5\cdot10^{-10}$ | $<10^{-7}$ |
| C0.1 break (½ on $d_\chi$ term of $\partial_S$), rel dev | $4.0\cdot10^{-3}$ | $3.3\cdot10^{-3}$ | $1.6\cdot10^{-3}$ | $>10^{-3}$ |
| C0.2 $R[D_3]$ | $-9.1\cdot10^{-5}$ | $-4.1\cdot10^{-3}$ | $-1.7\cdot10^{-4}$ | $<10^{-3}\max(1,\text{scale})$ |
| C0.2 break ($k_{sp}=1.9$), $R[D_3]$ | $+15.7$ | $-21.8$ | $-9.1$ | $>10^{-2}$ |
| C0.3 $\lvert R[D_4]\rvert/\text{scale}$, $c_6=0$ | $4.1\cdot10^{-4}$ | $9.3\cdot10^{-3}$ | $1.6\cdot10^{-4}$ | $<10^{-2}$ |
| C0.3 same, $c_6=\tfrac12$ | $3.9\cdot10^{-4}$ | $9.5\cdot10^{-3}$ | $1.8\cdot10^{-4}$ | $<10^{-2}$ |
| C0.3 same, $c_6=1$ | $3.8\cdot10^{-4}$ | $9.6\cdot10^{-3}$ | $2.0\cdot10^{-4}$ | $<10^{-2}$ |
| C0.3 no-χ: $R[D_4]$ vs $vV_4^{-1}v/600$ | $0.6548$ vs $0.6551$ | $6.991$ vs $7.040$ | $-2.1360$ vs $-2.1363$ | rel $<10^{-2}$ |
| C0.3 χ(1,1): $R[D_4]$ vs $\tfrac34vV_4^{-1}v/600$ | $0.4912$ vs $0.4913$ | $5.266$ vs $5.280$ | $-1.6022$ vs $-1.6023$ | rel $<10^{-2}$ |
| C0.4 slope of $\lvert D_4\rvert$ | $0.957$ | $0.781$ | $1.029$ | $[0.7,1.5]$ |

Entries, in the order they closed:

1. **C0.1 closed.** Analytic gradient (3.1) agrees with central differences to $10^{-10}$ at a
   generic point with all couplings on; a factor-2 error in one term is detected at
   $10^{-3}$. The harness's stationarity condition is the one of (1.1).
2. **C0.2 closed.** $D_3\to0$ on all seeds. Break leg: a wrong HS source coefficient
   $k_{sp}=1.9$ leaves $R[D_3]\sim10$, i.e. the leg is sensitive to the $O(g^2)$/$O(g^3)$
   structure of the action, not vacuous. Seed 23 sits at $4\cdot10^{-3}$, an order above the
   other seeds: this seed has the largest R24 residual (7.04) and the worst-conditioned $V_4$;
   the same seed was the noisy one in `verify-chi-partner.py` (R24, critic M2).
3. **C0.3 closed.** With χ(1,2) and the $\Sigma_3$ pair at $c_6=0$ the $O(g_s^4)$ mismatch
   vanishes to $4\cdot10^{-4}$ (seeds 7, 11) and $9\cdot10^{-3}$ (seed 23) of the R24 scale.
   This is the first time the $\Sigma_3$ HS pair supplies the sextic contact in the χ scheme
   (R24 closed with $c_6=1$, no $\Sigma_3$); the scan $c_6\in\{0,\tfrac12,1\}$ confirms that
   the split is invisible at $O(g_s^4)$, as 038 §3.3 says. The two R24 break legs reproduce
   the predicted nonzero values: no-χ gives $vV_4^{-1}v/600$ and $b_\chi=1$ gives
   $(1-b_\chi^2/4)$ of it, both to $<10^{-2}$ relative (seed 23: $7\cdot10^{-3}$, $2.6\cdot10^{-3}$).
4. **C0.4 closed.** The residual of the $O(g_s^4)$ action is $O(g_s^5)$: slopes $0.96$, $0.78$,
   $1.03$ (the value $0.78$ of seed 23 again reflects its conditioning; R24's run reported
   $0.93$ on its seeds). The three seeds are the "three seeds" the brief asks for.
5. **Diagnostic for the continuation (not a check).** $R[D_5]$ at $c_\chi=d_\chi=a_7=0$, i.e. the
   raw $O(g_s^5)$ deficit before any fit, is stable between $g_0=10^{-2}$ and
   $2\cdot10^{-2}$ to $1.6\cdot10^{-4}$, $7.8\cdot10^{-3}$, $1.2\cdot10^{-5}$ (seeds 7, 23, 11):
   values $+1.8925$, $+101.95$, $+3.2286$. The $g^{-5}$ amplification is therefore not at the
   float-noise floor at $g_0=10^{-2}$; seed 23 will need a three-point Richardson or a larger
   $g_0$ window in the fit.

Seed 23's $10^{-2}$-level closure is a **performance number under the pass gate**, not a
sign of an $O(g_s^4)$ defect: it moves with the conditioning of $V_4^{-1}$ (the no-χ and
χ(1,1) legs, which do not close, are reproduced at the same $10^{-2}$ level on that seed), and
the scaling leg C0.4 is the safeguard, as it was for R24.

## 5. Projection basis

The basis $\{V_7(\Psi^7),S_1,S_2,S_3\}$ is built by `basis()`, a verbatim copy of `invariants()`
of `codes/verify-chi-ogs5-count.py` (same $x=V_4^{-1}v$, same $S_3$ strand-split
representative), so the components the continuation fits are in 038's normalisation. The
four functions of $\Psi$ are sampled on $N_\Psi=40$ random probes per seed; each column is
normalised and the Gram matrix $G$ of the normalised columns is diagonalised.

| seed | rank | $\mathrm{cond}(G)$ | $\lambda_{\min}(G)$ | break: $+V_7\rvert_{322}$ column, $\lambda_{\min}$ |
|---|---|---|---|---|
| 7 | 4 | $4.8\cdot10^{1}$ | $5.7\cdot10^{-2}$ | $1.2\cdot10^{-16}$ (rank stays 4) |
| 23 | 4 | $4.3\cdot10^{3}$ | $9.1\cdot10^{-4}$ | $-1.6\cdot10^{-16}$ (rank stays 4) |
| 11 | 4 | $2.5\cdot10^{1}$ | $1.1\cdot10^{-1}$ | $1.9\cdot10^{-16}$ (rank stays 4) |

**C0.5 closed**: the Gram matrix is non-singular on every seed, and the rank test detects a
genuinely dependent fifth column ($V_7(p_3,P,P)=V_7(\Psi^7)$ by symmetry).

*Conditioning entry.* With $N_\Psi=12$ probes the condition numbers were $5\cdot10^4$,
$5\cdot10^2$, $2.5\cdot10^4$ and the off-diagonal entries between $S_1,S_2,S_3$ reached
$0.99$; with $40$ probes they drop to the table above, and with $120$ probes to $33$, $640$,
$15$ (scratch run, same construction). The cause is the heavy tail of $S_{1,2,3}$ as functions
of $\Psi$: all three contain $V_4^{-1}v$, which is large near the zero set of $\det V_4$ on
$\mathrm{Sym}^2$, so a few probes dominate the sample Gram matrix and inflate the apparent
collinearity. Consequence for the continuation: use $\ge40$ probes and weight each probe row
(e.g. by $1/\max_k|\text{column}_k|$ or by trimming the largest $|x|$ probes) before the least
squares, and report the projection coefficients with their conditioning; seed 23 stays the
worst-conditioned on every leg of this run. The basis itself is fine — 038's
`N3/A7-independence` (rank 4) is reproduced — but the *fit* will be sensitive to the probe set
unless the tail is controlled.

## 6. Result of sub-task 1, verification, self-review

\subsection*{Result}

$$
\boxed{\text{The joint }(\Sigma_2,\chi,\Sigma_3)\text{ harness reproduces the }O(g_s^3),O(g_s^4)
\text{ legs with }(a_\chi,b_\chi)=(1,2),\ (c_6,c_{\Sigma_3})=(0,1),\text{ residual }O(g_s^5)}
$$

on three seeds, with the R24 break legs (no χ, $b_\chi=1$) reproduced at their predicted
nonzero values and the $c_6$ split invisible at $O(g_s^4)$ as 038 §3.3 states. The projection
basis $\{V_7(\Psi^7),S_1,S_2,S_3\}$ is non-singular (rank 4) on every seed. C0 holds. Nothing
was fitted. The raw $O(g_s^5)$ deficit $R[D_5]$ at $c_\chi=d_\chi=a_7=0$ is measured to be
numerically stable (§4 item 5), so sub-task 2 could start from the fit directly.

The result is conditional on PH14–PH16 and PH23 only in the sense that the *question* (does
$S^\chi_5$ close) is posed under them; the calibration numbers themselves are facts about the
finite-dimensional toy at the stated seeds.

\subsection*{Verification}

`codes/verify-chi-ogs5-matching.py`: 27 checks + 9 break legs for C0, all PASS, seeds printed,
nonzero exit on failure. Falsifiability of each check: C0.1 — a factor-2 bug in
one gradient term is detected (break leg); C0.2 — a wrong HS source coefficient produces
$|R[D_3]|\sim10$ (break leg); C0.3 — the two R24 legs that *do not* close are checked against
their predicted nonzero values, so a harness that returned $0$ for everything would fail them;
C0.4 — a residual at $O(g^4)$ would give slope $\approx0$; C0.5 — the redundant column is
detected. Dimensional check: $g$ is dimensionless in the toy and every term of (1.1) carries
$g^{\#\text{slots}-2}$, checked by the vanishing of $D_3$, $D_4$. Limiting cases: no χ and
$b_\chi=1$ reduce to R24's numbers; $c_{\Sigma_3}=0$ decouples $\Sigma_3$ and reduces to R24's
$c_6=1$ action, closure unchanged. Not verified at this stage: anything at $O(g_s^5)$;
independence of the results from $N=4$ (single dimension, as in R24/R42).

\subsection*{Self-review}

1. Objective: served in its first step — the harness is now trusted on the legs where the
   answer is known, which is what makes a non-closure at $O(g_s^5)$ interpretable.
2. Weakest step: seed 23's $10^{-2}$-level closure and its $4\cdot10^3$ Gram conditioning. Shored
   up by the scaling leg (slope $0.78$, residual still $O(g^5)$) and by the same-seed break legs
   being reproduced at the same precision; the continuation should add a fourth seed and drop
   seed 23 from any coefficient average, keeping it as a robustness seed only.
3. Not checked: $N>4$; a three-point Richardson; the $b'_\chi$ leg (C6) — its term is in the
   action and gradient and covered by C0.1, but its effect is the continuation's.
4. Five-minute find: the heavy tail of $V_4^{-1}v$ in the probe sample (§5) — a naive least
   squares of $D_5$ on the basis would be dominated by two or three probes; the continuation
   must weight or trim before fitting, and should report the projection with and without the
   largest-$|x|$ probes.

## 7. Sub-task 2: extrapolator, and the predictions the tests are gated on

\subsection*{Setup}

Uses A1–A10 and C0 (the harness, §3–§6). New symbols: $X=\Sigma_2-P$, $W=V_5(\cdot,\cdot,\Psi)$
on $\mathrm{Sym}^2$, $v=V_5(\cdot,P,\Psi)$, $x=V_4^{-1}v$, $g_6=V_6(\cdot,P,P)$,
$u=V_6(\cdot,P,\Psi)$, $L X=V_6(\cdot,X,\Psi)$ on $\mathrm{Sym}^3$, $M=V_6|_{\mathrm{Sym}^3}$,
$p_3=\Psi^{\otimes3}$, $S_1=v^\top V_4^{-1}WV_4^{-1}v=V_5(x,x,\Psi)$, $S_2=\langle g_6,x\rangle$.

### 7.1 The extrapolator (change of method, stated and justified)

Sub-task 1 used the two-point Richardson $2D_n(g_0/2)-D_n(g_0)$. At $n=5$ that is not good
enough: it removes only the $O(g)$ term of $D_5$, leaves an $O(g^2)$ truncation error, and
amplifies the float noise of $S$ by $g^{-5}$. It is replaced by a **fit of the mismatch in
powers of $g$**,

$$ S^\chi_5(\text{saddle};g)-S_{\rm eff}(g)=\sum_{k=4}^{7}c_kg^k+O(g^8), \tag{7.1} $$

least squares on eight geometrically spaced $g$ (column-scaled; condition number reported).
The quantity every test below is about is $7!\,c_5$. The Richardson entries of §4 are
untouched and still run; (7.1) is used only at $O(g_s^5)$. This is the "three-point
Richardson or larger $g_0$ window" that §6 item 3 of sub-task 1 said seed 23 would need.

**Probe-adapted window (C-w).** The expansion (7.1) has a *probe-dependent* radius: the
saddle displacement is $X\simeq\frac g5V_4^{-1}v$, so the effective expansion parameter is
$g\lVert x\rVert$, and $\lVert x\rVert$ ranges over four decades on the probe sample (§5, the
heavy tail). A single window therefore mixes converged and truncated probes. The window is
chosen per probe from a ladder of one-decade windows spaced every half decade, with lower ends
$5\cdot10^{-3}$, $1.5\cdot10^{-3}$, $5\cdot10^{-4}$, $1.5\cdot10^{-4}$, $5\cdot10^{-5}$, by two
criteria, both internal to the representation and neither looking at the predicted
$\alpha,\beta$:

1. **round-off floor** — $\min_g\lvert S-S_{\rm eff}\rvert$ must exceed $10^3$ times the
   round-off of that difference, $\varepsilon\max_g\lvert S-S_{\rm free}\rvert$ with
   $S_{\rm free}=\frac12V_2(\Psi^2)+\frac g6V_3(\Psi^3)$. Those two terms are the same
   expression in the action and in $S_{\rm eff}$, cancel to the last bit, and must not enter
   the noise scale — with $\varepsilon\max_g\lvert S\rvert$ instead the guard is too
   pessimistic by four to six decades and rejects windows that are in fact clean (seed 23).
   Measured floors are either exactly $0$ (total cancellation: the window is pure round-off)
   or above $4\cdot10^4$, so the threshold is not a tuned number;
2. among the windows that pass 1, the **smallest relative residual of (7.1)**.

Criterion 1 is not optional and was added after criterion 2 alone failed: the fit has four
parameters for eight points, so on the smallest window it can fit round-off with a small
residual and return a $c_5$ wrong by four orders of magnitude (seed 7, first run: one probe
picked $[5\cdot10^{-5},5\cdot10^{-4}]$ and pulled $\alpha$ to $-2.3\cdot10^4$). The window is
fixed once per probe at $c_\chi=d_\chi=a_7=0$ and reused for the other coupling configurations
of that probe, but a configuration whose residual exceeds $10^{-5}$ triggers a re-selection for
that probe; the number of re-selections and the worst residual are printed for every
configuration.

### 7.2 The numbers the tests are gated on (derived here, before measuring)

038 §3.3 carries the $1/n!$ prefactors "symbolically" and quotes only $\beta$. The gates below
need $\alpha$ too, and need the sign convention fixed, so both are derived here from the same
four rows.

Completing the square in the $\Sigma_2$ sector, $-\frac{g^2}{4!}V_4(\Sigma,\Sigma)
+\frac{2g^2}{4!}V_4(\Sigma,P)=\frac{g^2}{4!}V_4(P,P)-\frac{g^2}{4!}V_4(X,X)$ and
$\frac{g^3}{5!}V_5(\Sigma,\Sigma,\Psi)=\frac{g^3}{5!}[V_5(\Psi^5)+2\langle v,X\rangle+W(X,X)]$,
so the $X$-action is $\frac12X^\top KX+J^\top X$ with

$$ K=-\frac{g^2}{12}V_4+\frac{g^3}{60}W,\qquad J=\frac{g^3}{60}v+\delta J,\qquad
   X_*=-K^{-1}J=\frac g5V_4^{-1}v+O(g^2). \tag{7.2} $$

**Row 1.** $-\frac12J^\top K^{-1}J$ with $K^{-1}=-\frac{12}{g^2}[V_4^{-1}+\frac g5V_4^{-1}WV_4^{-1}+O(g^2)]$:

$$ -\tfrac12J^\top K^{-1}J=\frac{g^4}{600}v^\top V_4^{-1}v+\frac{g^5}{3000}S_1+\dots \tag{7.3} $$

**Row 3.** The χ sector is $\frac12\chi^\top K_\chi\chi+j_\chi^\top\chi$ with
$K_\chi=\frac{a_\chi g^2}{12}V_4+\frac{c_\chi g^3}{60}W$ and
$j_\chi=\frac{b_\chi g^3}{120}(v+WX)+\frac{d_\chi g^4}{720}g_6$, so
$\chi_*=-\frac{b_\chi g}{10a_\chi}V_4^{-1}v+O(g^2)$ and, at $(a_\chi,b_\chi)=(1,2)$,

$$ -\tfrac12j_\chi^\top K_\chi^{-1}j_\chi
  =-\frac{g^4}{600}v^\top V_4^{-1}v-\frac{g^5}{1500}S_1
   +\frac{c_\chi g^5}{3000}S_1-\frac{d_\chi g^5}{3600}S_2+\dots \tag{7.4} $$

**Rows 2 and 4** are 038 (3.3a)–(3.3d) unchanged: the two sextic sources add
$\delta J=\frac{2+c_6}{720}g^4g_6$ and their cross term with $\frac{g^3}{60}v$ through
$K^{-1}$ gives $+\frac{2+c_6}{3600}g^5S_2$.

Adding, and subtracting the target $\frac{g^5}{7!}V_7(\Psi^7)$:

$$ \boxed{\;7!\,c_5=\alpha S_1+\beta(c_6)S_2-V_7(\Psi^7)
   +\frac{7!\,c_\chi}{3000}S_1-\frac{7!\,d_\chi}{3600}S_2+a_7V_7(\Psi^7)\;} \tag{7.5} $$

$$ \alpha=-\frac{7!}{3000}=-\frac{42}{25},\qquad
   \beta(c_6)=\frac{7!\,(2+c_6)}{3600}=\frac{7(2+c_6)}{5}. \tag{7.6} $$

\subsection*{Commentary}

(7.3) vs (7.4): the $O(g^4)$ terms cancel — that is R24's $b_\chi^2/a_\chi=4$, already
verified as C0.3. The two $S_1$ terms do **not** cancel: $\frac1{3000}-\frac2{3000}=-\frac1{3000}$,
which is $\alpha$. The $c_\chi$ term of (7.4) can be read either as the direct substitution
$\frac{g^3c_\chi}{120}V_5(\chi_*,\chi_*,\Psi)$ or as the $W$-correction to $K_\chi^{-1}$; both
give $+\frac{c_\chi}{3000}g^5S_1$, and they are the same term, not two. Likewise the $d_\chi$
term is $\frac{g^4d_\chi}{720}V_6(\chi_*,P,P)$, equivalently the $\delta j_\chi$ cross term.

**Relation to the 018 triple (not a check).** 038 §3.3 writes the deficit as
$V_7(\Psi^7)-7!A_5^\chi$ with components $(1,-\alpha,-\beta)=(1,\frac{42}{25},-\frac{14}{5})$
on $\{V_7,S_1,S_2\}$ — numerically the triple 018 §3 reports for the *dressed*-scheme
deficit. 038 §3.3 (ll. 571–574, 590–593) is explicit that this coincidence **is not a check**:
the 018 triple lives on the dressed-scheme basis with its own normalisation, and 038 carried
$\alpha$ symbolically rather than taking 018's value. The same caution applies here: the
$\alpha$ derived above is derived from the four rows, and the numerical agreement with 018 is
noted as a coincidence of normalisations, not used as corroboration. The sign convention is
fixed by (7.5): $7!c_5$ is *action minus target*, the negative of 038's deficit.

### 7.3 Gates, fixed before any $O(g_s^5)$ number was read

| test | quantity | gate | source of the gate |
|---|---|---|---|
| C2 | $V_7$ coefficient of $7!c_5$ | $-1\pm0.03$ | (7.5), exact |
| C4 | $\alpha$ | rel. $<5\%$ of $-42/25$ | (7.6) |
| C4 | $\beta(0)$ | rel. $<5\%$ of $14/5$ | 038 (3.3d) |
| C2 | $S_3$ share of $7!c_5$ | $<5\%$ | N3 (038 §3.2) |
| C2 | share $\perp\mathrm{span}\{V_7,S_1,S_2,S_3\}$ | $<5\%$ | N3′ (038 §3.1.5) |
| C1 | largest off-direction share of $\partial(7!c_5)/\partial\{c_\chi,d_\chi,a_7\}$ | $<5\%$ | diagonality of (5.1) |
| C1 | on-direction responses | $42/25$, $-7/5$, $1$, rel. $<5\%$ | (7.5) |
| C4 | fitted $(c_\chi,d_\chi,a_7)$ | $(1,2,1)$, rel. $<5\%$ | (7.5) set to zero |
| C5 | $R[D_3]$, $R[D_4]$ at the fitted point | as C0.2, C0.3 | R24 |
| C5 | log-log slope of $\lvert S-S_{\rm eff}\rvert$ after the fit | $>5.7$ | closure at $O(g_s^6)$ |
| C3 | $c_5$ under $T\to\mu T$ (kinetic $\mu^2$, source $\mu$, $a_7\mu^2$) | rel. $<10^{-3}$ | field redefinition |
| C3 | slope of $\frac{c_{\Sigma_3}g^4}{720}X^\top L^\top M^{-1}LX$ | $>5.7$ | N4, 038 row 4 |
| C6 | $\perp$ share of $\partial(7!c_5)/\partial b'_\chi$ | $>0.10$ | ~~falsification leg for (E4)~~ **superseded, see below** |
| C7 | $\beta(c_6)$, $c_6\in\{0,\frac12,1\}$ | $7(2+c_6)/5$, rel. $<5\%$ | 038 (3.3d) |
| C7 | spread of $\alpha$ over $c_6$ | $<2\%$ | $\alpha$ split-independent |

Break legs that must fire: an injected $S_3$ admixture at 20 % of $\lVert7!c_5\rVert$ must be
seen by the $S_3$ gate; the pre-fit slope must be $\approx5$, not $6$; rescaling the
$\Sigma_3$ kinetic *without* the source (not a field redefinition) must move $c_5$.

**Gates added on the fix pass** (critic iteration 1), each fixed before the corresponding
number was read; the superseded C6 gate above is kept struck through rather than moved:

| test | quantity | gate | source of the gate |
|---|---|---|---|
| C6 | out-of-span coefficient of the *compensated* $b'_\chi=0.5$ response, in $V_7$-column units | $>\gamma_{\min}$ | complement of C2-perp (§8.5) |
| C6 | growth of that coefficient from $b'_\chi=0.1$ to $0.5$ | ratio $>3$ (linearity gives $5$) | (8.2), response linear in $b'_\chi$ |
| C6 | $S_1$ response, uncompensated minus compensated, at $b'_\chi=0.1$ | $-0.344$, rel. $<10\%$ | $7![(2+b'_\chi)^2-4]/(-6000)$, (8.2) item 1 |
| C6 | out-of-span coefficient across the ladder (converged settings) | max/min $<3$ | flatness is the falsifier of "refinement removes only truncation" |
| C3 | $c_5$ under $M\to M+\varepsilon\Delta$, $\Delta p_3=0$, $\varepsilon=0.3$ | rel. $<10^{-4}$ | N4: $M^{-1}$ invisible at $O(g_s^5)$ |
| C3 | same with $\Delta p_3\ne0$ (break leg) | rel. $>10^{-3}$ | leading saddle moved |
| C8 | $\lvert\Delta\alpha\rvert$, $\lvert\Delta\beta\rvert$ between the last two ladder settings | $<0.084$, $<0.14$ | stopping rule = the C4 gate widths |
| C2 | $\gamma_{\min}$: smallest out-of-span coefficient the 5 % gate detects | reported, not gated | translation of the share gate into a coefficient bound |

**Gates added on fix pass 2** (critic iteration 2), both stated in the docstring of
`c6_diagnostic` before the corresponding numbers were read; the verdict of the first is
recorded as *void* in §8.8, on a derivation ((8.3)) and not on its number:

| test | quantity | gate | source of the gate |
|---|---|---|---|
| C6 | exponent $p$ of the out-of-span coefficient in $b_{\rm eff}$ at $b'_\chi=0.5$ | $\le1.2$ $O(g_s^5)$, $\ge1.8$ $O(g_s^4)$ defect | the $O(g_s^5)$ out-of-span structures of (8.2) were taken to be at most linear in $b_{\rm eff}$ — **wrong, see (8.3)** |
| C6 | out-of-span coefficient over windows scaled $1$, $1/3$, $1/10$ | max/min $<2$ $O(g_s^5)$; $\approx3$, $\approx10$ growth = $O(g_s^4)$ leakage | a $g^5$ coefficient is window-independent; a $g^4$ leakage grows as $1/g$ |
| C6 | same statistic at **order 4** over the same windows (control) | must be flat, else the shift is unclean and the test void | the order-4 coefficient is measured directly |

**The C6 gate factor was stated twice, differently** ($1\times\gamma_{\min}$ in this table, in
the code and in §8.5; $10\times$ in one script comment, now corrected). The $1\times$ is the
one applied and the only one with a derivation; the discrepancy and the verdict under both
readings are recorded in §8.5.

## 8. Results: C1–C7

All numbers from `codes/verify-chi-ogs5-matching.py`, run 2026-09-22, seeds $(7,23,11)$,
$N=4$, $N_\Psi=40$ probes per seed, nominal $(a_\chi,b_\chi,c_6,c_{\Sigma_3})=(1,2,0,1)$,
$b'_\chi=0$ except in C6. Probe-adapted windows per §7.1; the upper ends actually selected are
$\{1.5,5\}\cdot10^{-2}$ (seeds 7, 11) and $\{0.5,1.5,5\}\cdot10^{-2}$ (seed 23); worst order-fit
residual $10^{-6}$, $1.7\cdot10^{-5}$, $2.5\cdot10^{-6}$; Gram condition number of the weighted
projection $2.5$, $6.9$, $2.2$ (the probe weighting of §7.1 is what brings the $4.3\cdot10^3$
of §5 down to this).

### 8.1 C2 and C4 — the projection of the raw deficit, and the fit

$7!c_5$ at $c_\chi=d_\chi=a_7=0$, projected on $\{V_7(\Psi^7),S_1,S_2,S_3\}$:

| quantity | predicted | seed 7 | seed 23 | seed 11 |
|---|---|---|---|---|
| $V_7$ coefficient | $-1$ | $-0.9987$ | $-1.0159$ | $-0.9996$ |
| $\alpha$ | $-42/25=-1.68$ | $-1.6799$ | $-1.6736$ | $-1.6799$ |
| $\beta(0)$ | $14/5=2.8$ | $2.7992$ | $2.8062$ | $2.8000$ |
| $S_3$ share (N3) | $0$ | $2.2\cdot10^{-5}$ | $1.2\cdot10^{-4}$ | $4.9\cdot10^{-5}$ |
| $\perp$ share (N3′) | $0$ | $8.7\cdot10^{-4}$ | $1.8\cdot10^{-2}$ | $4.8\cdot10^{-4}$ |
| fitted $c_\chi$ | $1$ | $1.00007$ | $1.00006$ | $0.99981$ |
| fitted $d_\chi(0)$ | $2$ | $1.99953$ | $2.01549$ | $1.99913$ |
| fitted $a_7$ | $1$ | $0.99946$ | $1.01518$ | $0.99994$ |

**Coefficient bound behind the $\perp$ gate (added on the fix pass).** The $5\,\%$ gate of
C2-perp is relative to the weighted deficit norm, which $S_1$ and $S_2$ dominate, so on its own
it says little about a named alternative. It is translated into a bound on the coefficient of
an out-of-span direction: injecting a probe-space direction orthogonal to the four columns and
normalised to the weighted norm of the $V_7(\Psi^7)$ column — an $S_4$-type stand-in, since
$S_4$ of 038 §3.1.4 is still not constructed — the smallest coefficient the gate detects is
$\gamma_{\min}=$ $0.260$, $0.593$, $0.161$ (seeds 7, 23, 11), in the normalisation where the $V_7$ coefficient of the deficit is
$1$. The measured out-of-span coefficients at $b'_\chi=0$ are $4.5\cdot10^{-3}$, $0.259$, $1.5\cdot10^{-3}$, i.e. below
$\gamma_{\min}$ on every seed; C6 (§8.5) produces one above it. What C2-perp asserts is
therefore: *no fourth invariant enters the $O(g_s^5)$ deficit with a coefficient above
$\gamma_{\min}$*, against $-1$ for $V_7$, $-1.68$ for $S_1$ and $2.80$ for $S_2$.

**The $O(g^4)$ coefficient of the fit** (asserted but never reported before): $\max_{\rm probe}
\lvert7!c_4\rvert=$ $0.211$, $54.1$, $7.7\cdot10^{-2}$, median $8.3\cdot10^{-4}$, $0.247$, $6.0\cdot10^{-5}$, against ${\rm rms}\lvert7!c_5\rvert=$ $2.67\cdot10^{4}$, $5.56\cdot10^{6}$, $1.74\cdot10^{4}$ — six
to eight decades below the $O(g^5)$ signal, which is the measured form of "the mismatch starts
at $g^5$". Order-fit condition numbers $8.94\cdot10^3$ on every seed (the column-scaled design of (7.1)); no probe fell to the fallback branch of the
window selection (one window in the whole run, during seed 23's selection in the whole run).

**C2 established.** The deficit is $-V_7(\Psi^7)+\alpha S_1+\beta S_2$ with no $S_3$ (N3) and
nothing outside the span (N3′), on all three seeds and under the trim of the 10 % heaviest
$\lVert x\rVert$ probes (the trimmed columns move the numbers by less than the gate width).
The $S_3$ detector is not vacuous: an injected $S_3$ admixture at 20 % of $\lVert7!c_5\rVert$
is seen at $7\cdot10^{-2}$, $3.1\cdot10^{-1}$, $8.9\cdot10^{-2}$, three decades above the
measured shares.

**C4 established**, including the $V_7$ coefficient $-1$ predicted exactly by (7.5). The three
couplings come out at the values (7.5) gives when its three directions are set to zero, each
fitted from its own direction only. $(a_\chi,b_\chi)=(1,2)$ is untouched (N7): the $O(g_s^4)$
leg still closes at the fitted point (C5 below), and it closes only at $b_\chi^2/a_\chi=4$.
Out-of-sample, at the seed's own $\Psi$ — not one of the 40 fitted probes — the $O(g^5)$
coefficient drops by $9.1\cdot10^{-5}$, $7.2\cdot10^{-4}$, $1.7\cdot10^{-4}$ of its unfitted
value: three couplings, common to all $\Psi$, and not a per-probe fit.

### 8.2 C1 — diagonality

Response of $7!c_5$ to a unit perturbation of each coupling, projected:

| response | predicted | seed 7 | seed 23 | seed 11 |
|---|---|---|---|---|
| $\partial/\partial c_\chi$, on $S_1$ | $42/25=1.68$ | $1.6798$ | $1.6735$ | $1.6802$ |
| largest off-direction share | $0$ | $8.6\cdot10^{-4}$ | $1.9\cdot10^{-2}$ | $4.3\cdot10^{-4}$ |
| $\partial/\partial d_\chi$, on $S_2$ | $-7/5=-1.4$ | $-1.3999$ | $-1.3923$ | $-1.4006$ |
| largest off-direction share | $0$ | $1.9\cdot10^{-3}$ | $1.5\cdot10^{-2}$ | $1.6\cdot10^{-3}$ |
| $\partial/\partial a_7$, on $V_7$ | $1$ | $0.9993$ | $1.0007$ | $0.9997$ |
| largest off-direction share | $0$ | $1.8\cdot10^{-3}$ | $4.9\cdot10^{-3}$ | $1.8\cdot10^{-3}$ |

**C1 established.** The coefficient-to-invariant map of 038 (5.1) is diagonal at $O(g_s^5)$ to
$2\cdot10^{-3}$ (seeds 7, 11) and $2\cdot10^{-2}$ (seed 23) of the on-direction response, and
the on-direction sizes are the ones (7.5) predicts. That the *same* measurement machinery
does produce a large off-span component when the count says it should is C6.

### 8.3 C3 — the $\Sigma_3$ kinetic normalisation (N4)

Two legs, because the naive one is vacuous: with the sextic contact held fixed, a pure
rescaling of the $\Sigma_3$ kinetic is a field redefinition and cannot move anything.

- **Reparametrisation.** $T\to\mu T$, $\mu=1.7$, implemented as kinetic $\times\mu^2$,
  source $\times\mu$, $a_7\times\mu^2$: $c_5$ changes by exactly $0$ (bit-identical) on all
  three seeds. Break leg: rescaling the kinetic *without* the source — not a field
  redefinition, and it changes the $O(g_s^4)$ contact — moves $c_5$ by $6.4\cdot10^2$,
  $8.1\cdot10^1$, $2.6\cdot10^2$ relative. The leg fires.
- **Visibility of $M^{-1}$.** The one composite 038 row 4 identifies,
  $\frac{c_{\Sigma_3}g^4}{720}X^\top L^\top M^{-1}LX$ evaluated at the saddle, has log-log
  slope $5.991$, $6.010$, $6.003$: it is $O(g_s^6)$, invisible at the order tested. This is
  the falsifiable form of N4 — a slope of $4$ or $5$ would put $M^{-1}$ in the deficit.
- **N4, falsifiable form** (added on the fix pass; the critique is right that the two legs
  above do not test N4 beyond C0). Perturb the $\Sigma_3$ kinetic form alone,
  $M\to M+\varepsilon\Delta$ with $\Delta=z\otimes z$, $\lVert\Delta\rVert=0.3\lVert V_6\rVert$
  and $\langle z,p_3\rangle=0$, so that $\Delta p_3=0$. Then $(M+\varepsilon\Delta)p_3=Mp_3=u$:
  the leading saddle $T_*=p_3$ and the $O(g_s^4)$ sextic contact are untouched, and the only
  $\Delta$-dependence of the saddle value is
  $\frac{c_{\Sigma_3}g^4}{720}(LX)^\top(M+\varepsilon\Delta)^{-1}(LX)=O(g^6)$. A visible
  $M^{-1}$ at $O(g_s^5)$ would therefore move $c_5$; N4 says it does not.
  Measured: rel. $3.4\cdot10^{-6}$, $3.2\cdot10^{-5}$, $1.4\cdot10^{-5}$ (gate $<10^{-4}$). Break leg: the same $\Delta$ *without* the $p_3$ projection removed
  ($\Delta p_3\ne0$, leading saddle moved) changes $c_5$ by rel. $2.0\cdot10^{-3}$, $5.4\cdot10^{-2}$, $3.4\cdot10^{-2}$ — three decades
  above. The test is run at the unfitted couplings, where $c_5$ is the full deficit; at the
  fitted point $c_5$ is zero by construction and a relative change there has no scale.

**C3 established**, now including a leg that can fail.

### 8.4 C5 — lower legs and closure

At the fitted $(c_\chi,d_\chi,a_7)$: $R[D_3]=4.4\cdot10^{-7}$, $-3.0\cdot10^{-5}$,
$1.9\cdot10^{-6}$; $\lvert R[D_4]\rvert/\lvert vV_4^{-1}v/600\rvert=4.3\cdot10^{-5}$,
$3.4\cdot10^{-4}$, $6.0\cdot10^{-5}$ — both at or below the C0.2/C0.3 levels, so the
$O(g_s^3)$ and $O(g_s^4)$ legs are untouched. Log-log slope of $\lvert S-S_{\rm eff}\rvert$
after the fit: $5.86$, $6.66$, $6.04$ (gate $>5.7$); the same slope before the fit is $4.93$,
$4.90$, $5.05$. **C5 established**, and the break leg (slope $\approx5$ without the fitted
couplings) fires on every seed.

The closure test uses none of the fitted constants twice: $(c_\chi,d_\chi,a_7)$ are read off
the $S_1$, $S_2$, $V_7$ directions of the *unfitted* deficit, and what is then tested is the
$g$-scaling of the total mismatch, a quantity no fit entered.

### 8.5 C6 — the $b'_\chi$ falsification leg (redesigned on the fix pass)

\subsection*{Setup}

A3 is lifted here and only here. The critique (§1, §5) is that the superseded design —
$b'_\chi=0.5$ at fixed $b_\chi=2$ — does not isolate the structure it is meant to test. That
is correct, and the mechanism is sharper than "a mere reparametrisation": it is derived first,
because it also fixes what the leg can and cannot be compensated for.

\subsection*{Derivation}

Write $N:\mathrm{Sym}^3\to\mathrm{Sym}^2$, $N T=V_5(\cdot,T)$, so that $N^\top$ is the map
appearing in the $\Sigma_3$ equation. With $b'_\chi\neq0$ the $\Sigma_3$ saddle equation (3.1)
reads, at leading order,

$$ -\frac{c_{\Sigma_3}g^4}{360}MT+\frac{c_{\Sigma_3}g^4}{360}(u+LX)
   +\frac{b'_\chi g^3}{120}N^\top\chi=0
\;\Longleftrightarrow\;
   MT=(u+LX)+\frac{3b'_\chi}{c_{\Sigma_3}\,g}N^\top\chi. \tag{8.1} $$

The mixing is $O(g^3)$ while the $\Sigma_3$ kinetic is $O(g^4)$, so the second term carries
$g^{-1}$; with $\chi_*=O(g)$ it is $O(1)$, i.e. **the $\Sigma_3$ saddle moves at leading
order**, not perturbatively. Substituting (8.1) into the χ equation and using
$NM^{-1}u=Np_3=v$:

$$ \Big[\frac{a_\chi g^2}{12}V_4+\frac{b_\chi'^2g^2}{40\,c_{\Sigma_3}}NM^{-1}N^\top\Big]\chi
   =-\frac{(b_\chi+b'_\chi)g^3}{120}\,v-\frac{b'_\chi g^3}{120}NM^{-1}LX+O(g^4). \tag{8.2} $$

\subsection*{Commentary}

(8.2) has two consequences, and they are what the redesign is built on.

1. **At $O(b'_\chi)$ the source is $(b_\chi+b'_\chi)v$**: switching $b'_\chi$ on at fixed
   $b_\chi$ is the reparametrisation $b_{\rm eff}=b_\chi+b'_\chi$ of the $O(g_s^4)$ sector,
   which breaks R24's $b_\chi^2/a_\chi=4$ ($6.25$ at $b'_\chi=0.5$) and, at $O(g_s^5)$, shifts
   the $S_1$ coefficient by the *exactly predictable* amount
   $7!\,[\,(2+b'_\chi)^2-4\,]/(-6000)$ — $-1.89$ at $b'_\chi=0.5$, $-0.344$ at
   $b'_\chi=0.1$. That in-span response is large, physical-looking and has nothing to do with
   the $\Sigma_3$ mixing. It is compensated by $b_\chi=2-b'_\chi$.
2. **The compensation is exact only at $O(b'_\chi)$.** The χ kinetic operator itself picks up
   $\frac{b_\chi'^2}{40c_{\Sigma_3}}NM^{-1}N^\top$, of relative size $\frac{12b_\chi'^2}{40}
   =0.3\,b_\chi'^2$ against $\frac{a_\chi}{12}V_4$, and that correction *is* an $M^{-1}$
   object. So no choice of $b_\chi$ keeps the $O(g_s^4)$ sector closed once $b'_\chi\neq0$:
   the very structure the leg switches on feeds back into the sector the calibration uses.
   This is why the leg is run as a **scan** in $b'_\chi$ ($0.1$ and $0.5$, compensated): the
   compensation defect falls as $b_\chi'^2$ while the out-of-span response falls as
   $b'_\chi$.

\subsection*{Result}

**Gate, restated before the numbers were read** (the old $0.10$ share gate is recorded as
mis-specified in §8.7 (iii), not moved). A *share* divides by the response norm, which item 1
above inflates; the statistic is therefore the **absolute out-of-span coefficient**, measured
in the units of the $V_7(\Psi^7)$ column — the same units as the C2-perp sensitivity
$\gamma_{\min}$ of §8.1, so the two statements are exactly complementary:

- C2-perp certifies *no* out-of-span coefficient above $\gamma_{\min}$ at $b'_\chi=0$;
- C6 must produce one **above $\gamma_{\min}$** at $b'_\chi=0.5$ (compensated), and
- the coefficient must **grow with $b'_\chi$** — ratio $>3$ between $b'_\chi=0.5$ and
  $b'_\chi=0.1$, where exact linearity would give $5$;
- and the diagnosis of item 1 is itself gated: at $b'_\chi=0.1$, the $S_1$ response of the
  uncompensated leg minus that of the compensated leg must equal $-0.344$ to $10\%$.

All legs measured against the same $b'_\chi=0$ baseline of §8.1; $\gamma$ denotes the
$\gamma_{\min}$ of that seed ($0.260$, $0.593$, $0.161$). "Out-of-span" is the absolute
coefficient of §8.1, in $V_7$-column units.

| leg | quantity | seed 7 | seed 23 | seed 11 |
|---|---|---|---|---|
| $b'_\chi=0$ (baseline) | out-of-span | $0.0045$ | $0.259$ | $0.0015$ |
| $b'_\chi=0.5$, $b_\chi=1.5$ (**production**) | out-of-span | $2.770\ (10.7\gamma)$ | $2.080\ (3.5\gamma)$ | $5.455\ (33.9\gamma)$ |
| $b'_\chi=0.5$, $b_\chi=1.5$ | $\perp$ share | $0.621$ | $0.065$ | $0.877$ |
| $b'_\chi=0.1$, $b_\chi=1.9$ | out-of-span | $0.233\ (0.9\gamma)$ | $1.165\ (2.0\gamma)$ | $0.755\ (4.7\gamma)$ |
| growth $0.1\to0.5$ | ratio (gate $>3$) | $11.9$ | $\mathbf{1.79}$ | $7.2$ |
| $S_1$ artefact at $b'_\chi=0.1$ | $-0.344$ predicted | $-0.335$ | $\mathbf{-0.610}$ | $-0.320$ |
| $b'_\chi=0.5$, $b_\chi=2$ (**superseded**) | out-of-span | $4.328\ (16.7\gamma)$ | $3.236\ (5.5\gamma)$ | $8.522\ (53.0\gamma)$ |
| $b'_\chi=0.5$, $b_\chi=2$ (**superseded**) | $\perp$ share | $0.829$ | $0.094$ | $0.888$ |
| $\max\lvert7!c_4\rvert$ of the leg, $b'_\chi=0.5$ comp. | (baseline: $0.21$, $54$, $0.077$) | $3.8\cdot10^{4}$ | $1.3\cdot10^{6}$ | $2.9\cdot10^{4}$ |
| $\max\lvert7!c_4\rvert$ of the leg, $b'_\chi=0.1$ comp. | | $2.8\cdot10^{3}$ | $8.0\cdot10^{5}$ | $5.5\cdot10^{3}$ |

The superseded share row reproduces the numbers of the first run ($0.829$, $0.0943$, $0.888$
against the old $0.10$ gate); they are kept here and marked superseded, not deleted.

**The gate of §7.3 is met on all three seeds** — the leg produces an out-of-span component at
$10.7$, $3.5$ and $33.9$ times the largest coefficient C2-perp certifies is absent at
$b'_\chi=0$ — **but that is not enough to establish C6**, which claims an $O(g_s^5)$
statement. §8.8 measures which order the statistic carries; read §8.5 as the measurement and
§8.8 as the verdict.

Two things must be said about the margin before anything is built on it.

- **Seed 23's margin is $3.5\gamma_{\min}$**, not "$3.5$–$34\times$": a calibration leg that
  clears its own detection threshold by a factor $3.5$ on one seed of three is a weak
  calibration, and the range hides that.
- **The gate factor was stated twice, differently.** The gate table of §7.3, the code
  (`run2`, `C6-outside`: `pabs > gmin`) and this section all apply $1\times\gamma_{\min}$ — the
  exact complement of C2-perp, and the only factor with a derivation behind it. A comment in
  the script's constant block (ll. 505–507 before fix pass 2) instead read "$10\times$". The
  timeline cannot be recovered from the artefacts: the script carries a single modification
  time (16:41) covering both passages, it is untracked in git, and the fix-pass run produced
  no saved log. What *is* on the record is that three independent statements (§7.3 gate
  table, the gate comment next to the code, the code itself) say $1\times$ and one comment
  said $10\times$, and that the $10\times$ was never applied to a number. The comment has been
  corrected, and the verdict is reported under both readings: at $1\times$ the three seeds
  clear the gate; at $10\times$ seed 23 ($3.5\gamma_{\min}$) would not, and the leg would be
  met on two seeds of three. The discrepancy changes the seed count of the gate and nothing
  else: §8.8 settles what the statistic measures, and does so on the same numbers under
  either factor.

**Two legs of the scan fail on seed 23, and the attribution below is withdrawn** (fix pass 2,
critic iteration 2 node 3). The growth ratio is $1.79$ against the gate $3$, and the $S_1$
artefact is $-0.610$ against the predicted $-0.344$ ($77\%$ off; $3\%$ and $7\%$ on the other
two seeds). Both failures are at $b'_\chi=0.1$.

The first pass attributed them to item 2 of (8.2) — the compensation defect — on the strength
of a comparison that was mis-stated by three decades: the leg's $\max\lvert7!c_4\rvert$ against
the baseline ${\rm rms}\lvert7!c_5\rvert$ was quoted as "$14\%$ on seed 23 against
$1.0\cdot10^{-1}$ and $3.1\cdot10^{-1}$ *per mille* on seeds 7 and 11". The quantities are
$2.78\cdot10^{3}$, $8.04\cdot10^{5}$, $5.48\cdot10^{3}$ against $2.665\cdot10^{4}$,
$5.564\cdot10^{6}$, $1.741\cdot10^{4}$ (seeds 7, 23, 11; re-measured on fix pass 2,
`agent/scratch/c6-order-diagnostic.log`), i.e. **$10\%$, $14\%$, $32\%$** — the digits
$1.0\cdot10^{-1}$ and $3.1\cdot10^{-1}$ were fractions mislabelled as per mille. Three
consequences:

- the relative $O(g_s^4)$ mismatch does **not** single out seed 23: seed 11 carries the
  largest one ($32\%$) and passes both legs (ratio $7.2$, artefact $7\%$ off);
- on seed 23 the leg's own $c_4$ does not behave as an $O(b_\chi'^2)$ defect either — it grows
  by $1.6\times$ from $b'_\chi=0.1$ to $0.5$ ($8.04\cdot10^{5}\to1.28\cdot10^{6}$) where
  $b_\chi'^2$ predicts $25\times$, and it is nearly flat in $b_{\rm eff}$ at $b'_\chi=0.5$
  ($1.23$, $1.28$, $1.34$, $1.41\cdot10^{6}$ at $b_{\rm eff}=1.5,2,2.5,3$; §8.8), whereas the
  defect of (8.2) item 2 is $\propto b_{\rm eff}^2b_\chi'^2$. Seeds 7 and 11 do follow the
  defect law ($13.7\times$ and $5.2\times$ over the same $b'_\chi$ range);
- "the production leg, whose signal is five times larger" is also wrong as stated: the leg's
  own $\max\lvert7!c_4\rvert$ at $b'_\chi=0.5$ is $143\%$, $23\%$ and $165\%$ of the baseline
  ${\rm rms}\lvert7!c_5\rvert$, so the $O(g_s^4)$ contamination grows *faster* than the
  response on the two well-conditioned seeds.

**Standing statement.** Two auxiliary legs of C6 fail on seed 23 at $b'_\chi=0.1$ for a reason
not yet identified. The failures are recorded, the script exits 1, and nothing downstream
leans on them. What is now established about the leg as a whole is a separate and more serious
matter: see §8.8.

### 8.6 C7 — the sextic split

| $c_6$ | $\beta$ predicted | seed 7 | seed 23 | seed 11 | $d_\chi(c_6)$ predicted |
|---|---|---|---|---|---|
| $0$ | $14/5=2.8$ | $2.7992$ | $2.8062$ | $2.8000$ | $2$ |
| $1/2$ | $7/2=3.5$ | $3.4991$ | $3.5004$ | $3.4996$ | $5/2$ |
| $1$ | $21/5=4.2$ | $4.1991$ | $4.1931$ | $4.2007$ | $3$ |

$\alpha$ over the scan: spread $1.7\cdot10^{-4}$, $1.2\cdot10^{-4}$, $3.0\cdot10^{-4}$ —
split-independent, as 038 §3.3 says. The fitted $d_\chi(c_6)$ tracks $2+c_6$: $(2.00,2.50,3.00)$,
$(2.02,2.51,3.01)$, $(1.999,2.499,3.001)$, so $\beta(1)/\beta(0)=3/2$ to $3\cdot10^{-3}$.

**C7 established.** The affine law of (3.3d) is the sharpest quantitative prediction of the
count that involves a number 038 derived rather than fitted, and it holds on three seeds at
three values of the split.

### 8.7 Seed 23 and the extrapolation (convergence study)

Seed 23 is the ill-conditioned seed of R24 and of §4–§5. Its $O(g_s^5)$ numbers moved as the
extrapolator was refined, and the question the critique raises is whether the refinement
removes truncation or removes signal. Both the baseline and the C6 response are therefore
reported at the same three settings, on every seed.

**Stopping rule (stated on the fix pass, before the re-run).** Refine the ladder until the
shift of $\alpha$ and $\beta$ between successive settings is below the width of the gate they
are tested against — $0.05\lvert\alpha\rvert=0.084$ and $0.05\beta(0)=0.14$. The production
setting is accepted only if the last step of the ladder satisfies it (check `C8-stop`).

**Falsifier of "refinement removes only truncation".** A genuine out-of-span component is a
property of the action, not of the extrapolator, so it must be *flat* across the converged
settings, whereas a truncation artefact shrinks with them. The quantity that carries this is
the C6 out-of-span coefficient (§8.5) at the same settings, in the same units as the baseline
one. Gate: max/min $<3$ over the two settings the stopping rule calls converged. The coarsest
setting is reported but is not a valid measurement of anything — its $\alpha$ shift exceeds
the gate width, which is what the stopping rule says.

| extrapolator | seed | $\alpha$ | $\beta(0)$ | $S_3$ share | $\perp$ share | $\perp$ coeff. | C6 $\perp$ coeff. |
|---|---|---|---|---|---|---|---|
| one window $[5\cdot10^{-3},5\cdot10^{-2}]$ | 7 | $-1.6800$ | $2.7991$ | $5.2\cdot10^{-5}$ | $8.9\cdot10^{-4}$ | $0.0046$ | $2.770$ |
| ladder of 3 decades | 7 | $-1.6800$ | $2.7991$ | $5.2\cdot10^{-5}$ | $8.9\cdot10^{-4}$ | $0.0046$ | $2.770$ |
| ladder of 5 half-decades (production) | 7 | $-1.6799$ | $2.7992$ | $2.2\cdot10^{-5}$ | $8.7\cdot10^{-4}$ | $0.0045$ | $2.770$ |
| one window | 23 | $-1.8213$ | $2.8903$ | $4.5\cdot10^{-2}$ | $0.458$ | $8.062$ | $3.6\cdot10^{4}$ |
| ladder of 3 decades | 23 | $-1.6199$ | $2.8727$ | $6.8\cdot10^{-3}$ | $6.3\cdot10^{-2}$ | $0.865$ | $2.521$ |
| ladder of 5 half-decades (production) | 23 | $-1.6736$ | $2.8062$ | $1.2\cdot10^{-4}$ | $1.8\cdot10^{-2}$ | $0.259$ | $2.080$ |
| one window | 11 | $-1.6796$ | $2.7995$ | $2.8\cdot10^{-5}$ | $6.9\cdot10^{-4}$ | $0.0022$ | $5.455$ |
| ladder of 3 decades | 11 | $-1.6796$ | $2.7995$ | $2.8\cdot10^{-5}$ | $6.9\cdot10^{-4}$ | $0.0022$ | $5.455$ |
| ladder of 5 half-decades (production) | 11 | $-1.6799$ | $2.8000$ | $4.9\cdot10^{-5}$ | $4.8\cdot10^{-4}$ | $0.0015$ | $5.455$ |

Seeds 7 and 11 are flat in every column: their windows are the same at all three settings, so
the refinement has nothing to remove — which is itself the control the study needs.

Seed 23 is the case at issue. Refining the ladder takes its baseline out-of-span coefficient
from $8.06$ to $0.865$ to $0.259$ — a factor $31$ — while the C6 out-of-span coefficient,
measured with the same windows on the same probes, goes $3.6\cdot10^{4}\to2.52\to2.08$.

Three qualifications, all added on fix pass 2:

- The **coarsest C6 value on seed 23 is $3.6\cdot10^{4}$**, four decades off, against $8.06$
  for the baseline. "Off the scale" understates it: the C6 leg's extrapolation is far more
  fragile on this seed than the baseline's, which is consistent with the $O(g_s^4)$ content
  of the leg established in §8.8. Only the two converged settings are used.
- The right comparison for a *common additive* truncation artefact is the **absolute** shift,
  not the ratio. Over the converged pair C6 moves by $0.44$ and the baseline by $0.61$ —
  comparable, which is what a shared artefact of $\sim0.5$ would give. That reading still
  supports the conclusion (baseline true out-of-span $\approx0$, C6's $\approx1.6$, above
  $\gamma_{\min}=0.593$), but the record's earlier "C6 moves by $1.21$ while the baseline moves
  by $3.4$" compared a ratio against an absolute statistic and is replaced here.
- One refinement step is the whole evidence, and the stopping rule (above) was stated before
  the re-run but **after** the production ladder had been chosen (iteration 1). The rule
  therefore *confirms* a choice; it did not make it.

So the study is **consistent with** the earlier reading — seed 23's remaining
$1.8\cdot10^{-2}$ $\perp$ share is method, not a fourth invariant — and it does not establish
it. What it does establish is narrower and is used as such: the C6 coefficient is not an
artefact of window truncation, which is the input §8.8 needs.

**Stopping rule, applied.** Between the last two settings seed 23 moves by
$\lvert\Delta\alpha\rvert=0.054<0.084$ and $\lvert\Delta\beta\rvert=0.066<0.14$: the rule is
satisfied at the production setting, and the other two seeds move by less than $10^{-3}$. The
rule is *not* satisfied between the first two settings ($\lvert\Delta\alpha\rvert=0.201$),
which is why the coarsest row is reported but not used. Seed 23's $\alpha$ is non-monotone —
$-1.821\to-1.620\to-1.674$, overshooting the prediction at the middle setting — so the ladder
is not a monotone convergence, only a bounded one; the rule is stated on the *shift*, not on
monotonicity, precisely because the shift is what the gate width can be compared against. One
further refinement step was not run (the window would fall below the round-off guard of §7.1
on most probes, which is the fallback branch that fired once in this run).

**Three gates were mis-specified and are recorded as such.** (i) The out-of-sample residual was
first gated against $\lvert V_7(\Psi^7)\rvert$, which is not the scale of the deficit (the
deficit is dominated by $S_1,S_2$, larger by two to four decades); it is gated against the
unfitted $\lvert7!c_5\rvert$ in §8.1. (ii) The first window criterion used
$\varepsilon\max_g\lvert S\rvert$ as the noise floor, which ignores the bit-exact cancellation
of $V_2,V_3$ (§7.1). (iii) **The C6 gate "$\perp$ share $>0.10$" was mis-specified**: the
share divides by the norm of a response that the $b_{\rm eff}$ reparametrisation of (8.2)
item 1 inflates, so it measures the $S_4$-type part against an artefact, and its $0.10$ was
in any case a number with no derivation behind it. The superseded design's numbers are kept
in §8.5; the gate is replaced by the absolute coefficient statement of §8.5, not moved.
None of the three re-specifications touches a *physics* gate: the fifteen numbers of
§8.1–§8.6 are compared against predictions fixed in §7.2 before any of them was read.

### 8.8 Which order does the C6 statistic measure? (fix pass 2)

\subsection*{Setup}

Critic iteration 2 observed a regularity in the §8.5 table: at $b'_\chi=0.5$ the ratio of the
out-of-span coefficient between the superseded ($b_\chi=2$, $b_{\rm eff}=2.5$) and the
compensated ($b_\chi=1.5$, $b_{\rm eff}=2$) design is $4.328/2.770=1.5625$, $3.236/2.080=1.556$,
$8.522/5.455=1.562$ on seeds 7, 23, 11 — i.e. $(2.5/2)^2$, a $b_{\rm eff}^2$ law, on three
seeds. The question it raises is whether the statistic C6 gates on is an $O(g_s^5)$ quantity at
all, or the $O(g_s^4)$ compensation defect of (8.2) item 2, which is $\propto b_{\rm eff}^2$.

Two gates were written down before the corresponding numbers were read; both are in the
docstring of `c6_diagnostic` in the companion script, and the run is
`agent/scratch/c6-order-diagnostic.log`.

**Gate 1 ($b_{\rm eff}$ exponent).** Fit $p$ in (out-of-span coefficient of $7!c_5$)
$\sim b_{\rm eff}^{\,p}$ over $b_{\rm eff}\in\{1.5,2,2.5,3\}$ at fixed $b'_\chi=0.5$
($b_\chi=b_{\rm eff}-b'_\chi$). On the enumeration of $O(g_s^5)$ out-of-span structures
available at the time — $b_{\rm eff}b'_\chi$, $b_\chi b_\chi'^2$, $b_\chi'^3$, all at most
linear in $b_{\rm eff}$ — $p\le1.2$ was to mean $O(g_s^5)$ and $p\ge1.8$ the $O(g_s^4)$ defect.

**Gate 2 (order in $g$).** Refit the production leg on the per-probe window scaled by $1$,
$1/3$, $1/10$. A genuine $O(g_s^5)$ coefficient is window-independent (the contamination from
the untruncated orders $\ge8$ *shrinks* as the window moves down); a leakage of the $O(g_s^4)$
defect into the $g^5$ column grows as $1/g$, i.e. by $\approx3$ and $\approx10$ over the same
shifts. Gate: max/min $<2$ over the settings $\Rightarrow$ genuine $O(g_s^5)$; growth tracking
$1/g$ $\Rightarrow$ leakage. Control, not tuned: the leg's out-of-span coefficient *at order
4* must itself be window-independent, otherwise the shift is not clean and the test is void.

\subsection*{Derivation}

Gate 1's premise is wrong, and the derivation below is why. Expand (8.2) one order further.
With $\kappa=\frac{3b_\chi'^2}{10\,c_{\Sigma_3}a_\chi}NM^{-1}N^\top$ the χ kinetic operator is
$K=\frac{a_\chi g^2}{12}(V_4+\kappa)$, and the source, keeping the $O(g)$ pieces
($X_1=x/5$ as in §8.5 item 1, $LX=O(g)$), is
$J=\frac{g^3}{120}\big[b_{\rm eff}\,(v+g\,V_5(\cdot,X_1,\Psi))+b'_\chi\,NM^{-1}LX\big]$.
Then

$$ S_\chi=-\tfrac12 J^\top K^{-1}J
   =-\frac{g^4}{2400\,a_\chi}\,
     \big[b_{\rm eff}(v+gV_5(\cdot,X_1,\Psi))+b'_\chi NM^{-1}LX\big]^\top
     \big(V_4^{-1}-V_4^{-1}\kappa V_4^{-1}+O(b_\chi'^4)\big)\big[\cdots\big]. \tag{8.3} $$

Sorting by order in $g$ and by coupling:

| order | structure | coupling | in span? |
|---|---|---|---|
| $g^4$ | $v^\top V_4^{-1}v$ | $b_{\rm eff}^2$ | — (the R24 closure value) |
| $g^4$ | $-v^\top V_4^{-1}\kappa V_4^{-1}v$ | $b_{\rm eff}^2b_\chi'^2$ | **out** (the compensation defect) |
| $g^5$ | $2\,v^\top V_4^{-1}V_5(\cdot,X_1,\Psi)$ | $b_{\rm eff}^2$ | in ($S_1$) |
| $g^5$ | $-2\,v^\top V_4^{-1}\kappa V_4^{-1}V_5(\cdot,X_1,\Psi)$ | $b_{\rm eff}^2b_\chi'^2$ | **out** |
| $g^5$ | $2\,v^\top V_4^{-1}NM^{-1}LX_1$ | $b_{\rm eff}b'_\chi$ | **out** |
| $g^6$ | $b_\chi'^2(NM^{-1}LX)^\top V_4^{-1}(NM^{-1}LX)$ | $b_\chi'^2$ | out |

The fourth row is the structure the enumeration behind gate 1 missed: the $b_\chi'^2$
composite in $K^{-1}$ dresses the $S_1$ direction as well as the $O(g_s^4)$ contraction, and
carries **the same $b_{\rm eff}^2b_\chi'^2$ law as the $O(g_s^4)$ defect**. A $b_{\rm eff}^2$
exponent therefore does not separate the two candidates; only the power of $g$ does.

\subsection*{Result}

**Gate 1, measured** (out-of-span coefficient of $7!c_5$ at $b'_\chi=0.5$):

| $b_{\rm eff}$ | seed 7 | seed 23 | seed 11 |
|---|---|---|---|
| $1.5$ | $1.558$ | $1.194$ | $3.069$ |
| $2.0$ (production) | $2.770$ | $2.080$ | $5.455$ |
| $2.5$ (superseded) | $4.328$ | $3.236$ | $8.522$ |
| $3.0$ | $6.233$ | $4.668$ | $12.272$ |
| fitted exponent $p$ | $\mathbf{2.00}$ | $\mathbf{1.97}$ | $\mathbf{2.00}$ |

The gate fires on the $O(g_s^4)$ side on all three seeds, and the superseded/compensated ratio
at $b'_\chi=0.1$ confirms the law where the leg is weakest — $1.1019$, $1.1558$, $1.1026$
against $(2.1/2)^2=1.1025$ (a $b_{\rm eff}^1$ law would give $1.05$). **The verdict of gate 1
is void**, by the derivation above: the fourth row of (8.3) is an $O(g_s^5)$ structure with the
same law. The measurement is kept because it *is* informative — it says the leg's out-of-span
content at $b'_\chi=0.5$ is dominated by the $b_{\rm eff}^2b_\chi'^2$ composite dressing, not
by the $b_{\rm eff}b'_\chi$ $\Sigma_3$-mixing source. The $b'_\chi$ exponent at fixed
$b_{\rm eff}=2$ (compensated: $1.56$, $0.26$, $1.21$) is between the $1$ of the mixing term and
the $2$ of the composite terms, which is the same statement with a noisier estimator.

**Gate 2, measured** (production leg, $b'_\chi=0.5$, $b_\chi=1.5$):

| window | seed 7 | seed 23 | seed 11 | order-4 control (max/min) |
|---|---|---|---|---|
| $\times1$ (production) | $2.7702$ | $2.0802$ | $5.4547$ | |
| $\times1/3$ | $2.7923$ | $2.2503$ | $5.5283$ | |
| $\times1/10$ | $7.0397$ | $1.7007$ | $7.6064$ | |
| max/min, all three | $2.54$ | $1.32$ | $1.39$ | $1.00$, $1.00$, $1.00$ |
| max/min, $\times1$ and $\times1/3$ only | $1.008$ | $1.082$ | $1.014$ | |

Leakage of the $O(g_s^4)$ defect predicts $\approx3$ over the $\times1/3$ shift and
$\approx10$ over the $\times1/10$ shift. Measured over the $\times1/3$ shift: $1.008$, $1.082$,
$1.014$ — flat to $1\%$–$8\%$ against a predicted factor $3$. **The fitted $c_5$ out-of-span
coefficient is not a leakage of the $O(g_s^4)$ defect.**

The $\times1/10$ setting is excluded, and the exclusion is post hoc — it is argued from the
fit, not from the number it produced. At $g\in[5\cdot10^{-4},5\cdot10^{-3}]$ the $g^5$ term of
the mismatch is $c_5g^5\sim5.3\cdot3\cdot10^{-17}\approx2\cdot10^{-16}$ on an action of order
one, i.e. **at the double-precision floor**, while the leg's $g^4$ term is three decades above
it; this is exactly the regime the round-off guard `SNR_MIN` of §7.1 exists to keep the
production windows out of, and the worst relative fit residual rises from $10^{-6}$ to
$8\cdot10^{-6}$ there. Its values ($7.04$, $1.70$, $7.61$) are also not the $\approx10\times$
growth leakage predicts; they are noise in both directions. The order-4 control is $1.00$ on
every seed and every setting, so the window shift itself is clean.

\subsection*{Verification}

The order-4 control is what makes gate 2 falsifiable: the same estimator, on the same shifted
windows, returns a stable value for a coefficient that *is* $O(g_s^4)$, so the procedure can
distinguish a stable coefficient from a $1/g$-growing one. Gate 1's estimator is likewise
demonstrably able to return the value that would have cleared the leg: it returns $-0.39$,
$0.32$, $0.63$ for the out-of-span coefficient of the leg's $7!c_4$ *difference*, i.e. very
different exponents on a neighbouring quantity, so the $2.00$, $1.97$, $2.00$ of gate 1 is not
an artefact of the fitting.

\subsection*{Commentary — what C6 does and does not establish}

- **Established.** With $b'_\chi\neq0$ (compensated, $b_\chi=2-b'_\chi$) the $O(g_s^5)$ deficit
  acquires a component outside $\mathrm{span}\{V_7,S_1,S_2,S_3\}$ whose coefficient exceeds
  $\gamma_{\min}$ on three seeds ($10.7$, $3.5$, $33.9\gamma_{\min}$), is stable under a $1/3$
  window refinement to $1\%$–$8\%$ where a leakage of the $O(g_s^4)$ defect would have grown
  threefold, and grows with $b'_\chi$ on two seeds of three. That is an $O(g_s^5)$ statement,
  and it is the statement C6 is written as.
- **Not established.** That the coefficient measures the $\Sigma_3$ *mixing* — the
  $b_{\rm eff}b'_\chi\,v^\top V_4^{-1}NM^{-1}LX_1$ row of (8.3). The $b_{\rm eff}^2$ exponent
  says the dominant out-of-span structure at $b'_\chi=0.5$ is instead the composite dressing
  $b_{\rm eff}^2b_\chi'^2\,v^\top V_4^{-1}\kappa V_4^{-1}V_5(\cdot,X_1,\Psi)$. Both are
  $O(g_s^5)$ and both vanish at $b'_\chi=0$, so C6 as a *calibration of C2-perp* stands; C6 as
  a measurement of the mixing direction does not.
- **Not established either.** The two failing scan legs on seed 23 (§8.5), whose cause remains
  unidentified: they are auxiliary and their withdrawal does not touch the two items above.
- **What would settle the mixing reading.** Construct $S_4$ (038 §3.1.4) as a fifth column and
  project the leg's out-of-span part on the two structures of (8.3) separately — they are both
  in closed form — instead of gating on the norm of their sum. Proposed as follow-up; not built
  in this pass.

## 9. Result, verification, self-review (sub-task 2)

\subsection*{Result}

$$\boxed{\;7!\,A_5^\chi=-\frac{42}{25}S_1+\frac{7(2+c_6)}{5}S_2,\qquad
\text{closure at }c_\chi=1,\;d_\chi=2+c_6,\;a_7=1,\;\text{residual }O(g_s^6)\;}$$

in the finite-dimensional random-tensor model, on three seeds, under PH14–PH16, PH23 and the
conditions A1–A10. The χ scheme of 038 §6.1 **closes at $O(g_s^5)$**: the deficit lies in
$\mathrm{span}\{V_7(\Psi^7),S_1,S_2\}$ with no $S_3$ and no orthogonal remainder, the
coefficient map is diagonal, the three couplings each follow from their own direction, and
the total mismatch then scales as $g^6$. R42 is a counting result and its seven tests are
what makes it a matching result. **Tests 1–5 and 7 are established on three seeds.** Test 6,
the $b'_\chi$ falsification leg, is established on three seeds *in the form C6 states* — a
component outside $\mathrm{span}\{V_7,S_1,S_2,S_3\}$ at $O(g_s^5)$, above $\gamma_{\min}$, and
shown to be an order-5 coefficient rather than a leakage of the $O(g_s^4)$ defect (§8.8
gate 2) — but its coefficient is dominated by the composite-dressing structure of (8.3),
not by the $\Sigma_3$-mixing structure the leg is named after; that reading is a gap. Two
auxiliary scan legs of C6 fail on seed 23 at $b'_\chi=0.1$ for a reason not identified; the
attribution written on fix pass 1 was based on a mis-stated comparison and is withdrawn
(§8.5).

### Scope

The statement is a fact about the finite-dimensional algebraic layer (038 A4): generic
symmetric tensors $V_2\ldots V_7$ on $\mathbb R^4$, no $L_\infty$ structure, no worldsheet
input, a single dimension $N=4$, three seeds. It does **not** establish: closure at
$O(g_s^6)$ or beyond; anything about the negative-norm χ direction at the quantum level; the
CFT realisability of the bare $V_7$ slot restriction of A5; the $b'_\chi\ne0$ branch as a
*theory* (C6 runs it only as a break leg, and does not resolve its two $O(g_s^5)$ out-of-span
structures from one another). What it
does establish is that every prediction 038 makes at this order is reproduced by an
independent route — a joint Newton saddle plus a $g$-expansion — that shares none of 038's
enumeration arguments.

### Proposed ledger wording

Rewritten on the fix pass. Sign convention stated explicitly; C6 status appended; the new row
numbered **R49** (R43 is taken); the 018 clause corrected to what 038 §3.3 actually says.
Nothing is written to `knowledge/` from here — the orchestrator owns the ledger.

- **R42 — confirmed.** Add to the row: *verified numerically at $O(g_s^5)$ in the
  random-tensor model (048): with the deficit taken as action minus target, $7!\times$ the
  $O(g^5)$ coefficient of $S^\chi_5(\text{saddle})-S_{\rm eff}$ is
  $-V_7(\Psi^7)-\frac{42}{25}S_1+\frac{7(2+c_6)}{5}S_2$ — the negative of 038's deficit
  $V_7(\Psi^7)-7!A_5^\chi$; the $3\times3$ coefficient system is diagonal, closure at
  $(c_\chi,d_\chi,a_7)=(1,2+c_6,1)$, residual $O(g_s^6)$; three seeds,
  `codes/verify-chi-ogs5-matching.py`. Falsification leg C6, redesigned with the compensated
  coupling $b_\chi=2-b'_\chi$ (the first design measured the reparametrisation
  $b_{\rm eff}=b_\chi+b'_\chi$ of the $O(g_s^4)$ sector instead): at $b'_\chi\ne0$ the
  $O(g_s^5)$ deficit acquires a component outside the span, with coefficient $10.7$, $3.5$ and
  $33.9$ times the largest one the orthogonality test certifies absent at $b'_\chi=0$, stable
  under a threefold window refinement where a leakage of the $O(g_s^4)$ sector would have grown
  threefold (048 §8.8). Which of the two $O(g_s^5)$ out-of-span structures of 048 (8.3) carries
  it is open — the measured $b_{\rm eff}^2$ law points to the composite dressing rather than to
  the $\Sigma_3$ mixing — and two auxiliary scan legs fail on the ill-conditioned seed for an
  unidentified reason. This amends the row's clause "that branch has not been run": it has now
  been run as a break leg, an out-of-span component is detected, and $S_4$ is still not
  constructed. Analytically, 048 (8.2) sharpens condition (E4): once $b'_\chi\ne0$ the χ
  kinetic operator acquires the $M^{-1}$ composite $\frac{b_\chi'^2}{40c_{\Sigma_3}}NM^{-1}
  N^\top$ at $O(g_s^2)$, so the $O(g_s^4)$ closure of R24 fails for **every** $b_\chi$ — one
  order below where 038 needed (E4).* Status `Conditional(PH14, PH15, PH16, PH23) – Verified`
  for the closure statement; the C6 clause is `Verified` for the existence of the out-of-span
  component and open for its structure.
- **New row (proposed), R49.** *$\alpha=-42/25$ and $\beta(c_6)=7(2+c_6)/5$ are the $S_1$ and
  $S_2$ components of the χ-scheme $O(g_s^5)$ deficit, in the convention where the deficit is
  $7!$ times the $O(g^5)$ coefficient of $S^\chi_5(\text{saddle})-S_{\rm eff}$ (038's deficit
  is its negative). 038 carried $\alpha$ symbolically; 048 §7.2 derives it, and both are
  verified on three seeds (048 §8.1, §8.6). The numerical coincidence with the 018
  dressed-scheme triple is not a check (038 §3.3).* `Conditional(PH14, PH15, PH16, PH23) –
  Verified`.
- **PH16 (H-B5).** The registered wording — which already carries the amendment of
  `agent/reports/computator-038-fixpass2-20260921T201500.md` ll. 154–202 — **is the one this
  run supports**: the coupling that closes the $S_1$ direction is $V_5(\chi,\chi,\Psi)$ with
  $c_\chi=1$, not the $V_6(\chi,\chi,\Sigma)$ of the pre-amendment wording, and the $\Sigma_3$
  partner that is forced is the right-sign one with its even HS pair (its removal is the C3
  break leg). PH16 stays a hypothesis: this run tests its $O(g_s^5)$ consequence, not the
  hypothesis itself.
- **PH15.** The closure measured here is tree-level evidence in favour of PH15, whose
  falsifier names "an $O(g_s^5)$ contribution of the χ sector not reproduced by the target":
  no such contribution was found. Not a discharge — the falsifier is about the physical
  theory, not the toy.

\subsection*{Verification}

`codes/verify-chi-ogs5-matching.py`, seeds $(7,23,11)$, $N=4$, re-run on the fix pass
2026-09-22: **108 independent checks + 9 derived checks + 24 break legs**, two failures
(`C6-scan` and `C6-artefact`, both seed 23, both at $b'_\chi=0.1$, §8.5), exit code 1, run
time $\approx$ 22 min. The nine `C4-fit` checks are tallied separately as *derived*: each is a
corollary of `C4-alpha`/`C4-beta`/`C2-V7` and the matching `C1-size`, so the earlier figure
"102 checks" overstated the independent content by nine.

Summary line of the run:

```
CHECK COUNT: 108 independent checks + 9 derived checks (corollaries of others)
             + 24 break legs; 1 windows came from the fallback branch of choose_window
SUMMARY: FAILURES: C6-scan, C6-artefact
```

Falsifiability, check by check: C2's $S_3$ leg is calibrated by an injected admixture that it
does see ($7.0\cdot10^{-2}$, $3.1\cdot10^{-1}$, $8.9\cdot10^{-2}$, three decades above the
measured shares); C2's orthogonality gate is now stated as a coefficient bound $\gamma_{\min}$
and calibrated by C6, which produces a coefficient $10.7$, $3.5$ and $33.9$ times larger
(the seed-23 margin is $3.5$, and is quoted on its own rather than inside a range); C1's diagonality is
a statement about numbers that C6 shows can be large; C3's reparametrisation has a break leg
that moves $c_5$ by two decades, its $M^{-1}$ leg is a slope that would read $4$ or $5$ if the
composite were visible, and its new N4 leg ($M\to M+\varepsilon\Delta$, $\Delta p_3=0$) has a
break leg three decades above it; C5's slope reads $4.9$–$5.0$ before the fit and $5.9$–$6.7$
after; C8's stopping rule is checked against the gate widths. The predictions of §7.2 were
derived and written into the record before any $O(g_s^5)$ number was read, and the gates added
on the fix pass (§7.3) were fixed before the re-run; they include two exact coefficients
($V_7\to-1$, and the $-0.344$ reparametrisation signature of §8.5), one of which fails on the
ill-conditioned seed and is reported as failing.

Dimensional check: $g$ is dimensionless in the toy and every term of (1.1) carries
$g^{\#\text{slots}-2}$; the mismatch fit (7.1) starting at $k=4$ with $c_4$ consistent with
zero is that statement measured, and $c_4$ is now reported (§8.1): $\max\lvert7!c_4\rvert
=0.211$, $54.1$, $7.7\cdot10^{-2}$ against ${\rm rms}\lvert7!c_5\rvert=2.67\cdot10^{4}$,
$5.56\cdot10^{6}$, $1.74\cdot10^{4}$, i.e. five to six decades down. Limiting cases:
$c_\chi=d_\chi=a_7=0$ reproduces the $O(g_s^4)$ closure of C0.3; $c_{\Sigma_3}\to0$ decouples
$\Sigma_3$; the $c_6$ endpoints are the C7 scan. Second route: §7.2 is an independent analytic
derivation of the same two numbers, and the numerics agree with it to $5\cdot10^{-5}$ on the
converged seeds; the C6 mechanism of §8.5 is a third short derivation whose $-0.344$ prediction
is measured to $3\%$–$7\%$ on the converged seeds.

Regression: §8.1–§8.4, §8.6 reproduce the pre-fix-pass numbers to the last quoted digit
($\alpha=-1.6799$, $-1.6736$, $-1.6799$; $\beta(0)=2.7992$, $2.8062$, $2.8000$), so nothing in
the main result depends on the changes made here.

Not verified: $N>4$; more than three seeds; $O(g_s^6)$; the $b'_\chi$ leg above $b'_\chi=0.5$
and, on seed 23, its behaviour at small $b'_\chi$; the $(3,2,2)$ partner
$V_7(\Sigma_3,\Sigma_2,\Sigma_2)$ and the partner $V_6(\chi,\Sigma_3,\Psi)$ of $d_\chi$ (038
§6.1 lists them as equivalent at this order; the equivalence was not measured); the explicit
$S_4$ of 038 §3.1.4, for which the C2-perp bound still uses a random orthogonal stand-in.

\subsection*{Self-review}

1. **Objective.** Served for tests 1–5 and 7, established on three seeds; test 6 is
   established in its stated form but not in its intended reading (§8.8). The run also
   produced the number 038 lacked
   ($\alpha=-42/25$) and, with it, two exact predictions ($V_7\to-1$, and the $-0.344$
   signature that identifies what the first C6 design was measuring).
2. **Weakest step.** The C6 leg, throughout. Fix pass 1 read its out-of-span coefficient as
   a measurement of the $\Sigma_3$ mixing; §8.8 shows it is dominated by the composite
   dressing of (8.3), which has the same $b'_\chi$-vanishing property but a different
   structure, so the leg calibrates C2-perp and does not name a direction. The shoring-up is
   gate 2 of §8.8 (the coefficient is an order-5 quantity, not a leakage of the order-4
   defect), the ladder study of §8.7, and the fact that the $10.7$/$3.5$/$33.9$ margins are
   unchanged. Not shored up: the two failing scan legs on seed 23, whose cause is unidentified
   after the fix-pass-1 attribution was withdrawn.
3. **Not checked, and why acceptable.** $N>4$ and a fourth seed: the whole R24/R42 line is at
   $N=4$; worth doing, not load-bearing. $O(g_s^6)$: out of scope by 038 §6.3. The explicit
   $S_4$: the C2-perp bound is stated against a random out-of-span stand-in, which bounds the
   coefficient of *any* out-of-span direction the weighting does not suppress, but does not
   name one.
4. **What a stronger physicist finds in five minutes.** (i) The $S_4$ of 038 §3.1.4, still not
   constructed: as a fifth column it would turn both C2-perp and C6 from "something outside
   the span" into "this invariant, with this coefficient", and would remove the stand-in from
   item 3. (ii) An extrapolator that fits the $O(g_s^4)$ mismatch away explicitly — since
   (8.2) says the $b'_\chi$ leg must break it — would let C6 be scanned on the
   ill-conditioned seed instead of only established there.

## 10. Follow-up

Two gaps open inside this record, both inside C6 (see the claim tree `Open gaps` line and
§8.8). For the orchestrator:

1. **Ledger** — promote per §9: R42 confirmed with the sign convention and the C6 status,
   the new row as **R49**, the PH16 note ("the registered wording is the one supported"), and
   the PH15 line. The orchestrator writes `knowledge/results.md`; nothing was edited here.
2. **Construct $S_4$ explicitly** (038 §3.1.4) and add it as a fifth projection column, so
   that N3′ and C6 are tested against a named alternative rather than a stand-in.
3. **Seed 23, small $b'_\chi$** — the two failing legs have no identified cause (§8.5): the
   relative $O(g_s^4)$ mismatch is largest on seed 11, which passes, and seed 23's leg $c_4$
   does not follow the $b_\chi'^2$ law. Candidates to try: a fourth, better-conditioned seed;
   an extrapolator that removes the leg's own $O(g_s^4)$ mismatch before fitting $c_5$; and
   the conditioning of the $V_4$ inverse on that seed, which §4–§5 already flag.
4. **Separate the two $O(g_s^5)$ out-of-span structures of (8.3)** — both are in closed form;
   projecting on them (equivalently, adding the explicit $S_4$ column of item 2) turns C6 from
   "a component outside the span" into "this structure, with this coefficient", and is what
   would make C6 a measurement of the $\Sigma_3$ mixing. This is the open gap of §8.8.
5. **Paper** — 038 §6.3's scheme comparison can now be written with measured numbers: the χ
   route closes at $O(g_s^5)$ at the cost of the joint saddle (no sequential Gaussianity),
   and the $b'_\chi$ mixing is *not* a free option: at $b'_\chi\ne0$ the χ kinetic operator
   acquires an $M^{-1}$ composite at $O(g_s^2)$ — the $\frac{b_\chi'^2}{40c_{\Sigma_3}}
   NM^{-1}N^\top$ of (8.2) — so the $O(g_s^4)$ closure of R24 fails for **every** $b_\chi$, and
   condition (E4) is forced one order below where 038 needed it. (The saddle displacement
   (8.1) on its own is not an obstruction: a saddle may move.)

## 11. Fix pass after critic iteration 1 (`agent/reports/critic-048-20260922T163000.md`)

Resolution table — every finding of the critique, what was changed, where. Severity as in the
critique. "Record" means this file; "script" means `codes/verify-chi-ogs5-matching.py`.

| # | finding (critique §) | severity | what was changed | where |
|---|---|---|---|---|
| 1 | C6 mis-designed: $b'_\chi$ shifts $b_\chi$ at leading order (§5, §1) | Serious | C6 re-run with the compensated coupling $b_\chi=2-b'_\chi$; new gate stated before reading the number; old design kept as a printed diagnostic and marked superseded | §8.5 (rewritten), §7.3, §8.7 item (iii), script `run2` |
| 2 | C6 not reported across the extrapolator ladder (§4) | Serious | ladder study extended: baseline **and** compensated-C6 $\perp$ share at the three settings, all seeds | §8.7 (table), script `ladder_study` |
| 3a | deficit sign convention in the proposed R42 wording (§3) | Concern | wording rewritten as the $O(g^5)$ coefficient of $S^\chi_5(\text{saddle})-S_{\rm eff}$, sign convention stated | §9 ledger wording |
| 3b | C6 status missing from the proposed R42 wording (§5) | Concern | C6 status appended to the row | §9 ledger wording |
| 3c | "038 quoted $\alpha$ from 018" / "corroboration" (§2) | Concern | both corrected to what 038 §3.3 says: $\alpha$ carried symbolically, the 018 triple is not a check | §7.2 commentary, §9 (R49) |
| 3d | no stopping rule for the ladder (§4) | Concern | rule stated, applied to the measured shifts, non-monotone $\alpha$ acknowledged | §8.7 |
| 3e | C2-perp 5 % gate not a coefficient bound (§4) | Concern | gate translated into the smallest detectable coefficient of a named out-of-span direction ($S_4$-type), measured per seed | §8.1, script `C2-perp` sensitivity leg |
| 3f | C3 near-tautological, no falsifiable N4 test (§6) | Concern | N4 test added: $M\to M+\varepsilon\Delta$ with $\Delta p_3=0$, plus its break leg ($\Delta p_3\ne0$) | §8.3, script `C3-N4` |
| 4a | order-fit condition number claimed but not printed (§4) | Minor | computed and printed (worst per configuration) | §7.1, §8 header, script `order_coeffs` |
| 4b | $c_4$ asserted consistent with zero, never reported (§4) | Minor | printed per seed and reported | §8.1, §9 Verification |
| 4c | nine C4-fit checks are corollaries (§6) | Minor | re-tallied as DERIVED, separate count | §9 Verification, script `report` |
| 4d | fallback-branch count of `choose_window` not logged (§4) | Minor | counted and printed | §8 header, script |
| 5 | ledger wordings (R42 appendix, new row as R49, PH16 note) | — | rewritten in §9 | §9 |
| — | A3 lifted in C6 also lifts the $b_\chi$ calibration (§1) | Concern | stated in §8.5 with the leading-order mechanism | §8.5 |
| — | PH15: closure is tree-level evidence in its favour (§3) | Minor | one line added | §9 |
| — | section numbering skips 1–2 (§7) | Minor | not changed (cosmetic; renumbering would break the citations of the critique) | — |

**Outcomes of the two Serious findings.**

1. The compensated C6 clears its gate on all three seeds, seed 23 included
   ($3.5\gamma_{\min}$). The critique's premise — that $b_\chi=2-b'_\chi$ *keeps the
   $O(g_s^4)$ leg closed* — is only true at $O(b'_\chi)$: (8.2) shows the χ kinetic operator
   picks up $\frac{b_\chi'^2}{40c_{\Sigma_3}}NM^{-1}N^\top$ at the same order $g^2$, so no
   choice of $b_\chi$ closes that sector at $b'_\chi\neq0$. Hence the scan in $b'_\chi$.
   *(Superseded by §12: clearing the gate is not the same as establishing what the leg
   measures, and the attribution of the two seed-23 failures to this defect is withdrawn.)*
2. The C6 coefficient across the ladder is consistent with being flat on the converged
   settings (max/min $1.21$ on seed 23, absolute shift $0.44$ against the baseline's $0.61$)
   while the baseline's coefficient falls by $31\times$ over all three settings. The falsifier
   the critique asked for was run and did not fire. *(Wording corrected in §8.7 on fix pass 2:
   "consistent with", not "establishes".)*

**Gate changes, all stated before the numbers were read** (§7.3, second table): the C6
statistic is the absolute out-of-span coefficient against $\gamma_{\min}$, not a share against
$0.10$; the old gate is recorded as mis-specified in §8.7 (iii) with its numbers kept in §8.5.

## 12. Fix pass 2 after critic iteration 2 (`agent/reports/critic-048-iter2-20260922T175500.md`)

One node needed a computation (§8.8, new); the rest is wording. Resolution table.

| # | finding (critic node) | severity | what was changed | where |
|---|---|---|---|---|
| 1 | node 2 (2): the out-of-span coefficient scales as $b_{\rm eff}^2$, which no $O(g_s^5)$ structure of (8.2) predicts | Serious | **new §8.8**: two gates stated before their numbers; (8.3) derived, exhibiting the $O(g_s^5)$ structure the critic's enumeration (and mine) missed, which carries $b_{\rm eff}^2b_\chi'^2$; gate 1 measured ($p=2.00,1.97,2.00$) and its verdict recorded **void** by (8.3); gate 2 (order in $g$) measured and settles the order | §8.8 (new), script `c6_diagnostic`, log `agent/scratch/c6-order-diagnostic.log` |
| 2 | node 2 (1): gate stated twice, $1\times$ vs $10\times$ | Serious | timeline **not recoverable** (single file mtime, untracked, no saved fix-pass log); the three applied statements are $1\times$ and the lone $10\times$ was a comment never applied; comment corrected in the script, discrepancy and the verdict under **both** readings recorded; seed 23's margin quoted as $3.5$, not inside "$3.5$–$34\times$" | §8.5 (Result), script ll. 503–513 |
| 3 | node 3: attribution of the two failing scan legs contradicted by the record's own table | Fatal for that clause | ratios re-measured ($10\%$, $14\%$, $32\%$ — the "per mille" was a mislabelling by $10^3$); attribution **withdrawn** in all six locations (§8.5, §9 result, §9 self-review 2, claim tree C6, `Open gaps`, R42 appendix), plus §10 item 3 and §11 outcomes; two further disconfirmations recorded (seed 11 has the largest mismatch and passes; seed 23's leg $c_4$ grows $1.6\times$ where $b_\chi'^2$ predicts $25\times$ and is flat in $b_{\rm eff}$) | §8.5, §9, §10, §11, claim tree |
| 4 | node 1: §10 item 4 names the wrong consequence of (8.1)–(8.2) | Concern | replaced by the (E4) sharpening — the $M^{-1}$ composite at $O(g_s^2)$, closure fails for every $b_\chi$ — and the same sentence added to the R42 appendix | §10 item 4, §9 R42 appendix |
| 5 | node 4: ladder "establishes" → "consistent with"; ratio vs absolute shift; stopping rule stated after the ladder choice; coarsest C6 value on seed 23 | Concern | all four written into §8.7 | §8.7 |
| 6 | node 5: R42 appendix (a) stale attribution, (b) stale "that branch has not been run", (c) missing (E4) sharpening, (d) the $3.5$–$34\times$ clause conditional on node 2 | Serious | (a)–(c) done; (d) the clause is replaced by the per-seed margins plus the §8.8 qualification of what the coefficient measures | §9 |
| 7 | node 6: claim tree C9 line stale ("two seeds of three") | Concern | C6, C9 and `Open gaps` rewritten against §8.8 | claim tree |
| — | R49, PH16 note, PH15 line | — | untouched, as instructed (promoted by the orchestrator as written) | §9 |

**Outcome — the C6 verdict, with its order.**

- The C6 out-of-span coefficient **is an $O(g_s^5)$ quantity**, not a leakage of the
  $O(g_s^4)$ compensation defect: under a threefold window refinement it moves by $0.8\%$,
  $8.2\%$, $1.4\%$ where a leakage would have grown by $\approx3$, with an order-4 control
  stable to $1.00$ (§8.8 gate 2). C6 in the form the claim tree states it — "$b'_\chi\ne0$
  produces a component outside the span, above $\gamma_{\min}$, growing with $b'_\chi$, flat
  under refinement" — stands on three seeds, with the growth clause failing on seed 23.
- The leg **does not measure the $\Sigma_3$ mixing direction**. The $b_{\rm eff}^2$ law says
  the dominant structure is the composite dressing of (8.3), not the $b_{\rm eff}b'_\chi$
  mixing source. This is a new gap, recorded in the claim tree, the Result and the R42
  appendix, and the way to close it (project on the two structures of (8.3), or construct
  $S_4$) is §10 item 3b.
- The two failing scan legs on seed 23 have **no identified cause**.

Nothing in C1–C5, C7, C8 or the boxed result of §9 changed on this pass; the numbers of
§8.1–§8.4 and §8.6 were not re-run and are not touched by any of it.
