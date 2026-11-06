"""Finite checks of integer profiles and local noisy Bell swapping; not a general proof."""

import itertools
import json
import math
from decimal import Decimal, ROUND_CEILING
from pathlib import Path

import numpy as np

RESULTS = Path(__file__).resolve().parent / "results"
RESULTS.mkdir(parents=True, exist_ok=True)


def profile_count(d, a):
    return sum(2**k * math.comb(d, k) * math.comb(a, k)
               for k in range(min(d, a) + 1))


profile_cases = []
for d in range(5):
    for a in range(5):
        brute = sum(sum(abs(x) for x in z) <= a
                    for z in itertools.product(range(-a, a + 1), repeat=d))
        formula = profile_count(d, a)
        coarse = 2**a * math.comb(d + a, a)
        assert brute == formula
        assert formula <= coarse
        profile_cases.append({"increments": d, "age_budget": a,
                              "count": formula, "coarse_bound": coarse})


threshold_cases = []
for text_x in ["0.1", "0.999", "1", "1.001", "2", "2.75", "3", "4.1"]:
    x = Decimal(text_x)  # x = tau * ln(3), supplied exactly for this check.
    admissible = [age for age in range(8) if Decimal(age) < x]
    exact = int(x.to_integral_value(rounding=ROUND_CEILING)) - 1
    assert max(admissible) == exact
    threshold_cases.append({"tau_log_3": text_x, "largest_admissible_integer_tv": exact})


I = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.diag([1, -1]).astype(complex)
paulis = [I, X, Y, Z]
bell = np.array([1, 0, 0, 1], dtype=complex) / np.sqrt(2)
bell_density = np.outer(bell, bell.conj())
bell_basis = [np.kron(I, op) @ bell for op in paulis]


def local_op(op, site, qubits):
    out = np.array([[1]], dtype=complex)
    for q in range(qubits):
        out = np.kron(out, op if q == site else I)
    return out


def apply_depolarizing(rho, site, attenuation):
    qubits = int(round(math.log2(rho.shape[0])))
    weights = [(1 + 3 * attenuation) / 4] + [(1 - attenuation) / 4] * 3
    out = np.zeros_like(rho)
    for w, pauli in zip(weights, paulis):
        op = local_op(pauli, site, qubits)
        out += w * (op @ rho @ op.conj().T)
    return out


def project_bell(rho, left, right, outcome):
    qubits = int(round(math.log2(rho.shape[0])))
    remaining = [q for q in range(qubits) if q not in (left, right)]
    k = np.zeros((2**(qubits - 2), 2**qubits), dtype=complex)
    for col in range(2**qubits):
        bits = [(col >> (qubits - 1 - q)) & 1 for q in range(qubits)]
        row = 0
        for q in remaining:
            row = 2 * row + bits[q]
        k[row, col] = bell_basis[outcome][2 * bits[left] + bits[right]].conj()
    raw = k @ rho @ k.conj().T
    probability = float(np.trace(raw).real)
    return probability, raw / probability


def corrected_swap_chain(rho, outcomes):
    probability = 1.0
    for outcome in outcomes:
        prob, rho = project_bell(rho, 1, 2, outcome)
        probability *= prob
        # After deleting the two measured qubits, the right endpoint of the
        # growing link is the second remaining qubit. Correct its Bell frame.
        op = local_op(paulis[outcome], 1, int(round(math.log2(rho.shape[0]))))
        rho = op @ rho @ op.conj().T
    return probability, rho


swap_cases = []
for links, ages, tau in [
    (2, [0, 0, 0, 0], 3.0),
    (2, [0, 1, 2, 0], 3.0),
    (2, [1, 2, 1, 3], 0.7),
    (3, [0, 0, 0, 0, 0, 0], 2.0),
    (3, [0, 1, 2, 1, 3, 0], 10.0),
    (3, [1, 2, 1, 2, 1, 3], 2.0),
]:
    rho = np.array([[1]], dtype=complex)
    for _ in range(links):
        rho = np.kron(rho, bell_density)
    for q, age in enumerate(ages):
        rho = apply_depolarizing(rho, q, math.exp(-age / tau))
    visibility = math.exp(-sum(ages) / tau)
    target = visibility * bell_density + (1 - visibility) * np.eye(4) / 4
    max_state_error = 0.0
    max_probability_error = 0.0
    for outcomes in itertools.product(range(4), repeat=links - 1):
        probability, output = corrected_swap_chain(rho, outcomes)
        state_error = float(np.linalg.norm(output - target, ord="fro"))
        probability_error = abs(probability - 4**(-(links - 1)))
        max_state_error = max(max_state_error, state_error)
        max_probability_error = max(max_probability_error, probability_error)
        assert state_error < 1e-12
        assert probability_error < 1e-12
    # For a Werner/isotropic two-qubit state, PPT has one candidate negative
    # eigenvalue (1 - 3v)/4. Here it is also the smallest eigenvalue.
    partial_transpose = target.reshape(2, 2, 2, 2).transpose(0, 3, 2, 1).reshape(4, 4)
    minimum = float(np.linalg.eigvalsh(partial_transpose).min())
    assert abs(minimum - (1 - 3 * visibility) / 4) < 1e-12
    swap_cases.append({"links": links, "qubit_storage_ages": ages, "tau": tau,
                       "total_age": sum(ages), "visibility": visibility,
                       "all_bell_outcomes_checked": 4**(links - 1),
                       "max_frobenius_state_error": max_state_error,
                       "max_outcome_probability_error": max_probability_error,
                       "minimum_partial_transpose_eigenvalue": minimum})


result = {
    "profile_checks": profile_cases,
    "strict_tv_threshold_checks": threshold_cases,
    "one_and_two_swap_checks": swap_cases,
    "scope": "Finite numerical checks only: integer L1 counts, uniform Bell outcomes, depolarizing visibility multiplication, and the strict integer total-variation budget. The integer-age enumeration also applies when storage ages are integers. No all-policy, asymptotic, or LOCC-distillation proof is certified by this script.",
}
(RESULTS / "check_repeater_small_results.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps({"profile_cases_passed": len(profile_cases),
                  "strict_threshold_cases_passed": len(threshold_cases),
                  "swap_parameter_cases_passed": len(swap_cases),
                  "total_bell_outcome_branches_checked": sum(x["all_bell_outcomes_checked"] for x in swap_cases),
                  "largest_state_error": max(x["max_frobenius_state_error"] for x in swap_cases),
                  "largest_probability_error": max(x["max_outcome_probability_error"] for x in swap_cases)}, indent=2))
