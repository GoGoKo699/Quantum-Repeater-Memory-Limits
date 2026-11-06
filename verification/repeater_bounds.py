#!/usr/bin/env python3
"""Finite bounds for the stated Bell-link repeater model.

No Monte Carlo. K is computed as an exact integer. ASAP visibility uses a
positive transfer recursion with a rigorously bounded support-truncation error.
Floating-point roundoff is not enclosed by interval arithmetic.
Run from the repository root: python verification/repeater_bounds.py [--plot]
"""
from __future__ import annotations
import argparse
import csv
import json
import math
from pathlib import Path

BASE = Path(__file__).resolve().parent
OUT = BASE / "results"
FIGURES = BASE / "figures"
LN2, LN3 = math.log(2.0), math.log(3.0)


def profile_count(n: int, a: int) -> int:
    """Number of z in Z^(n-1) with ||z||_1 <= a, exactly."""
    if n < 1 or a < 0:
        raise ValueError("n >= 1 and a >= 0 are required")
    term = total = 1
    d = n - 1
    for j in range(1, min(d, a) + 1):
        term = term * 2 * (d - j + 1) * (a - j + 1) // (j * j)
        total += term
    return total


def strict_age_budget(tau: float) -> int:
    """Integer TV budget. Exact equality boundaries require exact cutoff input."""
    return math.ceil(tau * LN3) - 1


def roughness_mean(p: float) -> float:
    return 2 * (1 - p) / (p * (2 - p))


def mean_cycle_bounds(n: int, p: float, tol: float = 1e-14):
    """Positive tail sum for E max of n Geom(p), with support tail bound."""
    q = 1 - p
    L = max(1, math.ceil(math.log(tol * p / n) / math.log(q)))
    terms = [1.0]
    for t in range(1, L):
        terms.append(-math.expm1(n * math.log1p(-(q ** t))))
    lower = math.fsum(terms)
    tail = n * q ** L / p
    return lower, lower + tail, L, tail


def asap_visibility(n: int, p: float, tau: float, tol: float = 1e-14):
    """E exp(-sum |G_i-G_(i+1)|/tau), truncating every G at L.

    z_s^(1)=w_s, z_s^(k+1)=w_s sum_t r^|s-t| z_t^(k).
    Exponential-kernel multiplication costs O(L) using two sweeps.
    The omitted probability is exactly 1-(1-q^L)^n, at most n q^L.
    """
    q, r = 1 - p, math.exp(-1 / tau)
    L = max(1, math.ceil(math.log(tol / n) / math.log(q)))
    w = [p * q ** t for t in range(L)]
    z = w[:]
    for _ in range(n - 1):
        forward = [0.0] * L
        carry = 0.0
        for s in range(L):
            carry = z[s] + r * carry
            forward[s] = carry
        carry = 0.0
        new = [0.0] * L
        for s in range(L - 1, -1, -1):
            # Combine the left sweep and the strictly-right contribution.
            new[s] = w[s] * (forward[s] + r * carry)
            carry = z[s] + r * carry
        z = new
    lower = math.fsum(z)
    omitted = -math.expm1(n * math.log1p(-(q ** L)))
    return lower, min(1.0, lower + omitted), L, omitted


def entropy(probabilities):
    return -math.fsum(x * math.log2(x) for x in probabilities if x > 0)


def werner_hashing(v: float) -> float:
    e = max(0.0, (1 - v) / 4)
    return max(0.0, 1 - entropy([(1 + 3 * v) / 4, e, e, e]))


def phase_hashing(v: float) -> float:
    # Stable near v=0: 1-h2((1+v)/2) =
    # ((1+v)log(1+v)+(1-v)log(1-v))/(2 log 2).
    if v <= 0:
        return 0.0
    if v >= 1:
        return 1.0
    if v < 1e-3:
        # Positive series; omitted terms here are below roundoff for v<1e-3.
        return (v*v/2 + v**4/12 + v**6/30 + v**8/56) / LN2
    return ((1 + v) * math.log1p(v) + (1 - v) * math.log1p(-v)) / (2 * LN2)


def recurrence_hashing(v: float, max_rounds: int = 100):
    """Best yield among 0..max_rounds BBPSSW rounds followed by hashing.

    Each acceptance probability is multiplied, with a factor 1/2 per round.
    The result is an achievable yield, not optimal two-way distillability.
    """
    F = (1 + 3 * v) / 4
    if F <= 0.5:
        return 0.0, 0
    weight, best, best_round = 1.0, 0.0, 0
    for j in range(max_rounds + 1):
        e = (1 - F) / 3
        value = weight * max(0.0, 1 - entropy([F, e, e, e]))
        if value > best:
            best, best_round = value, j
        accept = F * F + 2 * F * e + 5 * e * e
        weight *= accept / 2
        if weight <= best:  # All later yields are bounded by current weight.
            break
        F = (F * F + e * e) / accept
    return best, best_round


def werner_entanglement_of_formation(v: float) -> float:
    c = max(0.0, (3*v-1)/2)
    if c <= 0:
        return 0.0
    small = c*c/(2*(1+math.sqrt(max(0.0,1-c*c))))
    return entropy([small,1-small])


def weighted_profile_upper(n: int, p: float, tau: float) -> float:
    a = strict_age_budget(tau)
    previous, terms = 0, []
    for age in range(a+1):
        ball = profile_count(n,age)
        terms.append((ball-previous)*werner_entanglement_of_formation(math.exp(-age/tau)))
        previous = ball
    return min(p,p**n*math.fsum(terms))


def volume_exponent(alpha: float) -> float:
    if alpha == 0:
        return 0.0
    return math.asinh(alpha) + alpha * math.asinh(1 / alpha)


def bisect_increasing(fun, target: float, lo: float, hi: float):
    for _ in range(100):
        mid = (lo + hi) / 2
        if fun(mid) < target:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def write_csv(path: Path, rows):
    with path.open('w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]), lineterminator='\n')
        writer.writeheader()
        writer.writerows(rows)


def main(plot=False):
    OUT.mkdir(parents=True, exist_ok=True)
    p = 0.5
    ap = roughness_mean(p)
    # One targeted analytic check of the newly implemented visibility recursion.
    checks = []
    for tau in (0.3, 1.0, 7.0):
        low, high, _, tail = asap_visibility(2, p, tau)
        qr = (1 - p) * math.exp(-1 / tau)
        exact = p / (2 - p) * (1 + qr) / (1 - qr)
        err = abs(low - exact)
        assert low - 5e-14 <= exact <= high + 5e-14
        checks.append(dict(n=2, p=p, tau=tau, analytic=exact,
                           transfer=low, omitted_probability=tail, discrepancy=err))

    small_counts = [dict(n=n, a=a, K=profile_count(n, a))
                    for n in (2, 4, 8) for a in (0, 1, 2, 3, 5)]
    exponent_rows = []
    for n in (16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384):
        tau = math.sqrt(n)
        a = strict_age_budget(tau)
        K = profile_count(n, a)
        log_lower = n * math.log(p)
        log_upper = min(math.log(p), log_lower + math.log(K))
        _, mu_upper, _, _ = mean_cycle_bounds(n, p)
        log_phase = -2 * ap * (n - 1) / tau - math.log(2 * LN2 * mu_upper)
        log_phase = max(log_phase, log_lower)  # Synchronized generation also works.
        exponent_rows.append(dict(n=n, p=p, tau=tau, strict_tv_budget=a,
            log10_K=math.log10(K), log10_depol_lower=log_lower/math.log(10),
            log10_depol_upper=log_upper/math.log(10),
            depol_exponent_lower=-log_upper/n,
            depol_exponent_upper=-log_lower/n,
            phase_exponent_upper=-log_phase/n,
            log10_phase_lower=log_phase/math.log(10), cycle_mean_upper=mu_upper))

    asap_rows = []
    for n in (16, 64, 256):
        mu_low, mu_up, _, mu_tail = mean_cycle_bounds(n, p)
        for label, tau in [('sqrt(n)', math.sqrt(n)), ('2n', 2*n), ('8n', 8*n)]:
            v_low, v_up, L, omitted = asap_visibility(n, p, tau)
            dep = werner_hashing(v_low)
            rec, rounds = recurrence_hashing(v_low)
            phase = phase_hashing(v_low)
            asap_rows.append(dict(n=n, p=p, lifetime=label, tau=tau,
                visibility_truncated=v_low, visibility_upper=v_up,
                visibility_support_error=omitted, time_cutoff=L,
                cycle_mean=mu_low, cycle_mean_tail=mu_tail,
                depol_hash_yield=dep, depol_recurrence_hash_yield=rec,
                recurrence_rounds=rounds, phase_hash_yield=phase,
                depol_hash_rate=dep/mu_up,
                depol_recurrence_hash_rate=rec/mu_up,
                phase_hash_rate=phase/mu_up))

    alpha = bisect_increasing(volume_exponent, -math.log(p), 0, 3)
    vh = bisect_increasing(werner_hashing, 1e-14, 1/3, 1)
    coefficient_rows = []
    for kappa in (0.1, 0.2, 0.5, 1.0, 1.25, 1.5, 2.0, 4.0, 8.0):
        v_star = math.exp(-ap/kappa)
        rec, rounds = recurrence_hashing(v_star)
        coefficient_rows.append(dict(p=p, kappa=kappa,
            asymptotic_converse_exponent=max(0, -math.log(p)-volume_exponent(kappa*LN3)),
            uniform_visibility_lower=v_star,
            uniform_recurrence_hash_yield=rec,
            recurrence_rounds=rounds,
            uniform_direct_hash_yield=werner_hashing(v_star)))

    constants = dict(p=p, roughness_mean=ap,
        converse_alpha_threshold=alpha,
        converse_kappa_threshold=alpha/LN3,
        sufficient_two_way_kappa=ap/LN3,
        hashing_visibility_threshold=vh,
        sufficient_direct_hash_kappa=ap/(-math.log(vh)),
        notes='Thresholds delimit proved regions; the intervening frontier is open. '
              'Time-support error bounds do not enclose binary64 roundoff.')
    weighted_example = dict(n=10,p=p,tau=1.0,
        synchronized_lower=p**10,
        unweighted_upper=p**10*profile_count(10,strict_age_budget(1.0)),
        weighted_upper=weighted_profile_upper(10,p,1.0))
    result = dict(constants=constants, weighted_example=weighted_example,
                  analytic_recursion_checks=checks,
                  small_exact_counts=small_counts,
                  sublinear_exponent_bounds=exponent_rows,
                  asap_noise_comparison=asap_rows,
                  linear_coefficient_bounds=coefficient_rows)
    (OUT/'repeater_bounds.json').write_text(json.dumps(result, indent=2)+'\n')
    write_csv(OUT/'sublinear_exponent_bounds.csv', exponent_rows)
    write_csv(OUT/'asap_noise_comparison.csv', asap_rows)
    write_csv(OUT/'linear_coefficient_bounds.csv', coefficient_rows)
    print(json.dumps(dict(constants=constants,
         maximum_recursion_check_discrepancy=max(x['discrepancy'] for x in checks),
         selected_exponent_rows=[exponent_rows[j] for j in (3,5,7,9,10)],
         asap_noise_comparison=asap_rows), indent=2))

    if plot:
        FIGURES.mkdir(parents=True, exist_ok=True)
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
        plt.rcParams.update({'font.size':10, 'axes.spines.top':False,
                             'axes.spines.right':False, 'svg.fonttype':'none',
                             'svg.hashsalt':'quantum-repeater-memory-limits'})
        ns=[r['n'] for r in exponent_rows]
        dl=[r['depol_exponent_lower'] for r in exponent_rows]
        du=[r['depol_exponent_upper'] for r in exponent_rows]
        pu=[r['phase_exponent_upper'] for r in exponent_rows]
        fig,ax=plt.subplots(figsize=(7.4,4.8),layout='constrained')
        ax.fill_between(ns,dl,du,color='#0072B2',alpha=.12,
                        label='Allowed interval from depolarizing bounds')
        ax.plot(ns,dl,'o-',color='#0072B2',markersize=4,
                label='Depolarization: converse lower bound')
        ax.plot(ns,pu,'s-',color='#D55E00',markersize=4,
                label='Pure phase: achievable upper bound')
        ax.axhline(LN2,color='#333333',linestyle=':',linewidth=1.3,
                   label='Synchronized exponent: ln 2')
        ax.set_xscale('log',base=2)
        ax.set_xlabel('Elementary edges n')
        ax.set_ylabel('Normalized loss exponent  −ln(rate) / n')
        ax.set_title('Same lifetime, different asymptotic rate bounds\n'
                     'p = 1/2,  τ = √n slots, ideal endpoint storage')
        ax.set_ylim(0,.735)
        ax.grid(True,alpha=.18)
        ax.legend(loc='center right',frameon=False,fontsize=8.6)
        fig.savefig(FIGURES/'sublinear_noise_contrast.png',dpi=180)
        svg_path = FIGURES/'sublinear_noise_contrast.svg'
        fig.savefig(svg_path,metadata={'Date':None})
        # Preserve newlines as separators in multiline XML/path attributes.
        svg_text = svg_path.read_text()
        svg_path.write_text('\n'.join(line.rstrip() for line in svg_text.splitlines()) + '\n')
        plt.close(fig)


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--plot',action='store_true')
    main(parser.parse_args().plot)
