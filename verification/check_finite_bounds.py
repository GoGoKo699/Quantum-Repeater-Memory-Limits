"""Independent checks of the finite combinatorial/entanglement refinements.

Uses only Python's standard library. These checks support the algebraic audit;
they do not replace the proofs in ../science/finite_bounds.md.
"""

import json
import math
from pathlib import Path

RESULTS = Path(__file__).resolve().parent / "results"


def ball_count(length, radius):
    return sum(2**j * math.comb(length, j) * math.comb(radius, j)
               for j in range(min(length, radius) + 1))


def shell_count(length, radius):
    if radius == 0:
        return 1
    return sum(2**j * math.comb(length, j) * math.comb(radius - 1, j - 1)
               for j in range(1, min(length, radius) + 1))


def ball_entropy(alpha):
    if alpha == 0:
        return 0.0
    return math.asinh(alpha) + alpha * math.asinh(1.0 / alpha)


def inverse_ball_entropy(value):
    lo, hi = 0.0, 1.0
    while ball_entropy(hi) < value:
        hi *= 2
    for _ in range(100):
        mid = (lo + hi) / 2
        if ball_entropy(mid) < value:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def h2(x):
    if x <= 0 or x >= 1:
        return 0.0
    return -x * math.log2(x) - (1 - x) * math.log2(1 - x)


def werner_ef(v):
    concurrence = max(0.0, (3 * v - 1) / 2)
    return h2((1 + math.sqrt(max(0.0, 1 - concurrence**2))) / 2)


def hashing_fidelity_threshold():
    lo, hi = 0.5, 1.0
    for _ in range(100):
        mid = (lo + hi) / 2
        if h2(mid) + (1 - mid) * math.log2(3) > 1:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def main():
    # Independent shell-sum reconstruction and Chernoff-bound check.
    checked = 0
    largest_excess = 0.0
    for length in range(1, 26):
        for radius in range(51):
            exact = ball_count(length, radius)
            assert exact == sum(shell_count(length, r) for r in range(radius + 1))
            excess = math.log(exact) - length * ball_entropy(radius / length)
            largest_excess = max(largest_excess, excess)
            assert excess <= 1e-11
            checked += 1

    f_hash = hashing_fidelity_threshold()
    v_hash = (4 * f_hash - 1) / 3
    coefficients = []
    for p in (0.1, 0.2, 0.5, 0.8, 0.9):
        mu = 2 * (1 - p) / (p * (2 - p))
        coefficients.append({
            "p": p,
            "exponential_for_kappa_below": inverse_ball_entropy(-math.log(p)) / math.log(3),
            "recurrence_hashing_suffices_above": mu / math.log(3),
            "direct_hashing_suffices_above": mu / -math.log(v_hash),
        })

    convergence = []
    for alpha in (0.05, 0.2, 1.0, 5.0):
        for length in (100, 1000):
            radius = math.floor(alpha * length)
            convergence.append({
                "L": length, "a": radius, "alpha": alpha,
                "log_K_over_L": math.log(ball_count(length, radius)) / length,
                "limiting_entropy": ball_entropy(alpha),
            })

    n, p, tau = 10, 0.5, 1.0
    cutoff = math.ceil(tau * math.log(3)) - 1
    weighted = sum(shell_count(n - 1, m) * werner_ef(math.exp(-m / tau))
                   for m in range(cutoff + 1))
    report = {
        "checks": {"cases": checked, "largest_log_bound_excess": largest_excess},
        "hashing_threshold": {"fidelity": f_hash, "visibility": v_hash},
        "coefficient_examples": coefficients,
        "entropy_convergence_examples": convergence,
        "weighted_bound_example": {
            "n": n, "p": p, "tau": tau, "a": cutoff,
            "synchronized_lower": p**n,
            "unweighted_upper": min(p, p**n * ball_count(n - 1, cutoff)),
            "weighted_upper": min(p, p**n * weighted),
            "weighted_to_lower_ratio": weighted,
        },
    }
    RESULTS.mkdir(parents=True, exist_ok=True)
    path = RESULTS / "finite_bound_checks.json"
    path.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
