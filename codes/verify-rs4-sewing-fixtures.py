"""Verify the RS4 ghost-zero-mode fixtures behind claim (1.a).

What this verifies (finite matrix realisation of the closed-string ghost
zero-mode algebra b0^pm, c0^pm on the 4-dim zero-mode Fock space):

  1. The zero-mode algebra {b0^a, c0^b} = delta^{ab}, nilpotency, cross-zero,
     with the conventions b0^pm = b0 +- bar b0, c0^pm = (c0 +- bar c0)/2
     (Erbin book, bsft_bv/bos_feynman: {b0^pm,c0^pm}=1).

  2. Erbin's kinetic/propagator inversion K Delta = 1 on the physical field
     (bsft_bv.tex computation, lines 252-273):
         K      = c0^- c0^+ L0^+ delta_{L0^-,0}   (bsft:eq:closed-fixed-kinetic-op)
         Delta  = b0^+ b0^- (1/L0^+) delta_{L0^-,0}  (bsft:eq:propagator-fixed)
     reduces (ghost part) to {c0^-,b0^-}{c0^+,b0^+} = projector onto the
     doubly-down (b0^pm=0) field subspace.

  3. THE CRUX of question (ii) / claim (1.a): the bivector inverse to the
     symplectic form omega_1(A,B)=<A|c0^-|B> is
         omega_1^{-1} = b0^- delta_{L0^-,0}
     i.e. c0^- (= omega_1 as operator) is inverted on ker b0^- by b0^-
     (= omega_1^{-1}), because {c0^-,b0^-}=1.  Hence the propagator factorises
         Delta = (b0^+/L0^+) . omega_1^{-1},   omega_1^{-1} = b0^- delta_{L0^-,0}.

  4. CORRECTION check: the "bare identity, no b-ghost" reading of the frozen-neck
     contraction is WRONG: omega_1^{-1} = b0^- delta != identity.  A single
     b0^- insertion (one ghost) survives; only the length-modulus factor
     b0^+/L0^+ is absent relative to the full propagator.

What this does NOT verify: the non-degeneracy of omega_1 on the physical field
(needs oscillator content beyond zero modes; standard/ledgered), the moduli-
space measure-zero statement, and the |q|=1 stub convergence (analytic, treated
in the note).  Those are argued in the deliverable, not machine-checked here.
"""

from __future__ import annotations

import numpy as np

SEED = 20260709
rng = np.random.default_rng(SEED)

# ---------------------------------------------------------------------------
# Single fermionic zero mode: 2-dim Fock space {|0> (b|0>=0), |1>=c|0>}.
# b|1>=|0>, c|0>=|1>, b|0>=0, c|1>=0.  {b,c}=1.
# ---------------------------------------------------------------------------
b1 = np.array([[0.0, 1.0], [0.0, 0.0]])  # lowers 1->0
c1 = np.array([[0.0, 0.0], [1.0, 0.0]])  # raises 0->1
I2 = np.eye(2)
F1 = np.array([[1.0, 0.0], [0.0, -1.0]])  # fermion parity (-1)^F on one mode

# Two independent modes (holomorphic, antiholomorphic) on the 4-dim tensor
# space.  Antiholomorphic operators carry the holomorphic parity so that the
# two sets anticommute (Koszul/Jordan-Wigner sign).
b0 = np.kron(b1, I2)
c0 = np.kron(c1, I2)
bb0 = np.kron(F1, b1)  # bar b0
cb0 = np.kron(F1, c1)  # bar c0

# Level / twist combinations
bp = b0 + bb0            # b0^+
bm = b0 - bb0            # b0^-
cp = 0.5 * (c0 + cb0)    # c0^+
cm = 0.5 * (c0 - cb0)    # c0^-

I4 = np.eye(4)


def anti(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    return x @ y + y @ x


results: list[tuple[str, bool]] = []


def check(name: str, ok: bool) -> None:
    results.append((name, bool(ok)))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}")


# ---------------------------------------------------------------------------
# Check 1: zero-mode algebra {b0^a,c0^b}=delta, nilpotency, anticommuting sets
# ---------------------------------------------------------------------------
check("{b0,c0}=1", np.allclose(anti(b0, c0), I4))
check("{bar b0,bar c0}=1", np.allclose(anti(bb0, cb0), I4))
check("{b0,bar b0}=0", np.allclose(anti(b0, bb0), 0))
check("{b0,bar c0}=0", np.allclose(anti(b0, cb0), 0))
check("{b0^+,c0^+}=1", np.allclose(anti(bp, cp), I4))
check("{b0^-,c0^-}=1", np.allclose(anti(bm, cm), I4))
check("{b0^+,c0^-}=0", np.allclose(anti(bp, cm), 0))
check("{b0^-,c0^+}=0", np.allclose(anti(bm, cp), 0))
check("b0^+ nilpotent", np.allclose(bp @ bp, 0))
check("b0^- nilpotent", np.allclose(bm @ bm, 0))

# ---------------------------------------------------------------------------
# Physical field subspace: doubly-down state |dd> annihilated by b0^+ and b0^-.
# ---------------------------------------------------------------------------
dd = np.zeros(4)
dd[0] = 1.0  # |0>_h (x) |0>_abar  = b0=bar b0=0
check("b0^+ |dd>=0", np.allclose(bp @ dd, 0))
check("b0^- |dd>=0", np.allclose(bm @ dd, 0))

# Projector onto the doubly-down line
P_dd = np.outer(dd, dd)

# Dual state |uu> = c0 bar c0 |dd> : annihilated by c0^pm (Erbin's phi^c sector).
uu = np.zeros(4)
uu[3] = 1.0
check("c0^+ |uu>=0", np.allclose(cp @ uu, 0))
check("c0^- |uu>=0", np.allclose(cm @ uu, 0))

# ---------------------------------------------------------------------------
# Check 2: Erbin's K Delta = 1 (ghost part), bsft_bv.tex lines 252-273.
# Delta acts on the DUAL states |uu> (mapping uu -> dd); K maps dd -> uu; so
# K Delta = 1 on the dual (uu) subspace, Delta K = 1 on the field (dd) subspace.
# Ghost part reduces to {c0^-,b0^-}{c0^+,b0^+} = identity on each.
# ---------------------------------------------------------------------------
Kghost = cm @ cp          # from K = c0^- c0^+ L0^+ delta
Dghost = bp @ bm          # from Delta = b0^+ b0^- (1/L0^+) delta
KD = Kghost @ Dghost      # acts on dual states uu
DK = Dghost @ Kghost      # acts on field states dd
check("K.Delta |uu> = |uu> (Erbin bsft_bv)", np.allclose(KD @ uu, uu))
check("Delta.K |dd> = |dd> (Erbin bsft_bv)", np.allclose(DK @ dd, dd))
# Equivalent anticommutator form {c0^-,b0^-}{c0^+,b0^+}
KDanti = anti(cm, bm) @ anti(cp, bp)
check("{c-,b-}{c+,b+}|uu>=|uu>", np.allclose(KDanti @ uu, uu))
check("K.Delta = {c-,b-}{c+,b+} on uu", np.allclose(KD @ uu, KDanti @ uu))

# ---------------------------------------------------------------------------
# Check 3 (CRUX): omega_1^{-1} = b0^- inverts omega_1 = c0^- on ker b0^-.
# Interpretation: omega_1(A,B) = <A|c0^-|B>, so c0^- is the "omega_1 map".
# On the field (b0^-=0), c0^- maps it to a dual state; b0^- maps back:
#     b0^- c0^- |dd> = |dd>.
# Hence the inverse-pairing bivector is realised by b0^- (times delta_{L0^-,0}).
# ---------------------------------------------------------------------------
check("b0^- c0^- |dd> = |dd>  (omega_1^{-1}=b0^- on ker b0^-)",
      np.allclose(bm @ cm @ dd, dd))
# c0^- takes |dd> out of the field subspace (into the up sector): nonzero
check("c0^- |dd> != 0 (omega_1 raises into dual sector)",
      not np.allclose(cm @ dd, 0))

# ---------------------------------------------------------------------------
# Check 3b: full propagator factorisation Delta = (b0^+/L0^+) . (b0^- delta).
# Take a generic positive scalar L0^+ = ell on the physical line (matter energy);
# ghost operator identity: b0^+ b0^- = b0^+ . b0^-  (trivial as operators) but
# the POINT is the grouping: the "frozen" factor is b0^- (=omega_1^{-1}), the
# "length" factor is b0^+/ell.  Verify the operator equality of the two groupings
# and that omega_1^{-1}=b0^- carries exactly one ghost (not zero).
# ---------------------------------------------------------------------------
ell = 3.7  # generic positive L0^+ eigenvalue
Delta_op = (bp @ bm) / ell                    # Delta ghost part / L0^+
frozen = bm                                   # omega_1^{-1} = b0^- delta
length = bp / ell                             # b0^+ / L0^+
check("Delta = (b0^+/L0^+) . omega_1^{-1}",
      np.allclose(Delta_op, length @ frozen))

# ---------------------------------------------------------------------------
# Check 4 (CORRECTION): the frozen-neck contraction is NOT the bare identity.
# omega_1^{-1} = b0^- delta != identity ; it carries one b-ghost.
# ---------------------------------------------------------------------------
check("omega_1^{-1}=b0^- is NOT the identity (correction to 'no b-ghost')",
      not np.allclose(bm, I4))
# Ghost number lowered by one: b0^- shifts the ghost grading by -1.
Ngh = np.diag([0.0, 1.0, 1.0, 2.0])  # c0,bar c0 counts; |dd>=0 ... |uu>=2
# b0^- maps a ghost-number-g state to ghost-number-(g-1): check on |uu>
lowered = bm @ uu
# lowered should live in ghost number 1 subspace (indices 1,2)
gh_lowered = 0.0
if not np.allclose(lowered, 0):
    gh_lowered = (lowered @ Ngh @ lowered) / (lowered @ lowered)
check("b0^- lowers ghost number by 1 (Ngh(omega_1^{-1})=-1)",
      not np.allclose(lowered, 0) and abs(gh_lowered - 1.0) < 1e-9)

# ---------------------------------------------------------------------------
# Falsification legs: confirm the checks can FAIL when the fixture is wrong.
# (a) If the frozen contraction were the bare identity, K.(id).(id) would not
#     reproduce K Delta = 1.
# (b) If we drop b0^- from Delta, inversion fails.
# ---------------------------------------------------------------------------
bad_KD = Kghost @ (bp @ I4)  # replace b0^- by identity in Delta ghost part
check("FALSIFY: identity-instead-of-b0^- breaks K.Delta (expect mismatch)",
      not np.allclose(bad_KD @ uu, uu))
bad_frozen = I4  # bare identity reading
check("FALSIFY: Delta != (b0^+/L0^+).identity (bare-identity reading wrong)",
      not np.allclose(Delta_op, length @ bad_frozen))

# ---------------------------------------------------------------------------
# Random-point robustness of the operator identities (checks are algebraic, but
# confirm on a random physical-subspace vector, not just |dd>).
# ---------------------------------------------------------------------------
alpha = rng.standard_normal() + 1j * rng.standard_normal()
check("K.Delta on random dual multiple", np.allclose(KD @ (alpha * uu), alpha * uu))
check("b0^- c0^- on random field multiple",
      np.allclose(bm @ cm @ (alpha * dd), alpha * dd))

# ---------------------------------------------------------------------------
print(f"\nseed = {SEED}")
n_fail = sum(1 for _, ok in results if not ok)
print(f"{len(results) - n_fail}/{len(results)} checks PASS")
if n_fail:
    raise SystemExit(f"{n_fail} check(s) FAILED")
print("ALL CHECKS PASS")
