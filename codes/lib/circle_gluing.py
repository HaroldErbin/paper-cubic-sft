"""Geometry of the fixed-halves circle gluing of p_{2,2} (record 074, R80).

Helpers copied from ``codes/verify-circle-gluing-inverse.py`` (record 074; that
script is cited by the ledger and never edited): the s-channel surface map
Z(q) = (q + 4 beta^2)^2 / (16 beta^2 q) of R2, the channel closures of record
032 (3.1), the membership test of M'_x = V_{0,4} and the ray marching that
produces the cut-off sigma_V(theta) of Q_V = {1 < |q| < e^{sigma_V(theta)}}.
Only the grid sizes are parameters here.

References:
    record 074 §1 (1.4); record 032 §1, §3; ledger R2, R80.
"""

from __future__ import annotations

import numpy as np

BETA = 1.5
B2 = BETA**2


def z_of_q(q: np.ndarray, b2: float = B2) -> np.ndarray:
    """s-channel puncture location, R2: Z = (q + 4 beta^2)^2 / (16 beta^2 q)."""
    return (q + 4 * b2) ** 2 / (16 * b2 * q)


def q_of_zs(zs: np.ndarray, b2: float = B2) -> np.ndarray:
    """Root of q^2 + (8 b^2 - 16 b^2 zs) q + 16 b^4 = 0 with |q| < 4 b^2 (032 (3.1))."""
    b = 8 * b2 - 16 * b2 * zs
    disc = np.sqrt(b * b - 4 * 16 * b2**2 + 0j)
    r1 = (-b + disc) / 2
    r2 = (-b - disc) / 2
    return np.where(np.abs(r1) < np.abs(r2), r1, r2)


def min_tu(z: np.ndarray, b2: float = B2) -> np.ndarray:
    """min(|q_t|, |q_u|) with the closures z/(z-1) (t) and 1 - 1/z (u) of 032 (3.1)."""
    qt = q_of_zs(z / (z - 1), b2)
    qu = q_of_zs(1 - 1 / z, b2)
    return np.minimum(np.abs(qt), np.abs(qu))


def sigma_v(
    n_theta: int = 720, n_sigma: int = 3000, b2: float = B2
) -> tuple[np.ndarray, np.ndarray]:
    """Cut-off sigma_V(theta) of Q_V by ray marching in log q (074 (1.4)).

    Args:
        n_theta: number of rays in theta on [0, 2 pi).
        n_sigma: number of radial steps in sigma = ln|q| on (0, ln 4 beta^2).
        b2: beta squared.

    Returns:
        (thetas, sigma_V): the ray angles and, per ray, the last sigma at which
        the surface Z(q) still lies in M'_x (min(|q_t|, |q_u|) > 1).

    """
    thetas = np.linspace(0, 2 * np.pi, n_theta, endpoint=False)
    sigmas = np.linspace(1e-4, np.log(4 * b2) - 1e-4, n_sigma)
    th, sg = np.meshgrid(thetas, sigmas, indexing="ij")
    q = np.exp(sg + 1j * th)
    inside = min_tu(z_of_q(q, b2), b2) > 1.0
    prefix_len = np.argmin(inside, axis=1)
    prefix_len = np.where(inside.all(axis=1), n_sigma, prefix_len)
    return thetas, sigmas[np.clip(prefix_len - 1, 0, n_sigma - 1)]
