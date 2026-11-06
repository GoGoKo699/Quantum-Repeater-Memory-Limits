# Reproducible finite checks

Three standalone programs check the finite combinatorics, local noisy Bell swaps, and numerical bound calculations used in this repository. They use no Monte Carlo or external data. The analytical claims are proved in the [science pages](../science/model.md); these checks do not certify the all-policy converse or the endpoint-distillation argument.

## Run

From the repository root, with ordinary Python execution, run:

```bash
python -m pip install -r verification/requirements.txt
python verification/run_all.py
```

The dependency-installation command is unnecessary if the listed versions are already available. The recorded run used **CPython 3.12.14, NumPy 2.3.5 and Matplotlib 3.10.8**. NumPy is required for the density-matrix check. Matplotlib is required only for figure generation; the other calculations use Python's standard library.

The wrapper invokes the following exact commands and stops on the first failure:

```bash
python verification/check_repeater_small.py
python verification/check_finite_bounds.py
python verification/repeater_bounds.py --plot
```

All three commands were rerun successfully after packaging. Run without `-O`, since assertions implement the finite checks. `python verification/run_all.py --no-plot` runs the same numerical checks without generating the figure. Each script locates its output directories relative to its own file, independently of the caller's working directory. Existing generated outputs are replaced on rerun.

## What is checked

| Program | Scope | Recorded result |
| --- | --- | --- |
| [check_repeater_small.py](check_repeater_small.py) | Brute-force integer balls for dimensions 0–4 and budgets 0–4; eight exact threshold cases; six density-matrix parameter cases with one or two Bell swaps | 25 integer cases, 8 threshold cases and all 60 Bell-outcome branches passed |
| [check_finite_bounds.py](check_finite_bounds.py) | Independent shell-sum reconstruction and lattice-entropy bound for dimensions 1–25 and radii 0–50; coefficient and weighted-bound examples | All 1,275 finite cases passed; no positive log-bound excess |
| [repeater_bounds.py](repeater_bounds.py) | Positive transfer recursion for ASAP visibility, checked against a closed two-edge formula at three lifetimes; exact integer profile counts and finite rate-bound illustrations | All 3 analytic comparisons passed; 11 sublinear-exponent rows, 9 ASAP noise rows and 9 coefficient rows generated |

The swap check applies independent local depolarizing channels to two- and three-link Bell states. It checks the corrected Werner output, each Bell outcome's probability, and the partial-transpose threshold. Its largest Frobenius state error and largest outcome-probability error were both **2.220446049250313 × 10⁻¹⁶**, against tolerances of $`10^{-12}`$. This is a local finite-state calculation, not a simulation of arbitrary adaptive schedules.

The transfer recursion's largest discrepancy from the two-edge formula was **5.551115123125783 × 10⁻¹⁷**. The finite weighted-bound example at $`n=10,p=1/2,\tau=1`$ reproduced

```math
0.0009765625\le R_{10}\le0.0011180486152733,
```

compared with the unweighted profile upper bound $`0.0185546875`$. See [finite bounds](../science/finite_bounds.md) for the proof and interpretation.

## Outputs

- [results/run_summary.json](results/run_summary.json) records the Python and package versions, commands, exit codes, counts and key numerical results. The same directory contains each command's complete output log.
- [results/check_repeater_small_results.json](results/check_repeater_small_results.json) contains every integer, threshold and density-matrix case.
- [results/finite_bound_checks.json](results/finite_bound_checks.json) contains the finite-bound checks and coefficient examples.
- [results/repeater_bounds.json](results/repeater_bounds.json) contains the transfer checks and all computed examples. The associated tables are [sublinear_exponent_bounds.csv](results/sublinear_exponent_bounds.csv), [asap_noise_comparison.csv](results/asap_noise_comparison.csv) and [linear_coefficient_bounds.csv](results/linear_coefficient_bounds.csv).
- [figures/sublinear_noise_contrast.svg](figures/sublinear_noise_contrast.svg) is the publication figure. `--plot` also writes a PNG preview in the same directory.

The figure displays bounds on normalized loss exponents, not optimized rate estimates. The SVG omits a generation timestamp and uses a fixed identifier salt. Numerical results are deterministic for a fixed Python and numerical environment; exact byte identity across different software versions is not promised.

## Assumptions and numerical limits

The calculation uses the [stated Bell-link model](../science/model.md): independent Bernoulli elementary generation, independent Markov memory noise, ideal swaps, ideal endpoint storage, and the allowed endpoint processing. The ASAP calculation uses iid first-success times $`G_i\sim\operatorname{Geom}(p)`$, with support starting at one, cycle duration $`\max_iG_i`$, and roughness $`\sum_i|G_i-G_{i+1}|`$. It does not optimize over scheduling policies.

Integer profile and shell counts use arbitrary-precision integer arithmetic. The strict cutoff is

```math
a=\lceil\tau\ln3\rceil-1.
```

It bounds the integer source-time total variation even when total physical memory age is real. The boundary check supplies $`\tau\ln3`$ directly as exact decimal values, including integers. The general numerical examples evaluate the product in binary64 and do not sit at integer boundaries; a floating-point value extremely close to a boundary is not an exact threshold certificate.

The ASAP visibility calculation truncates all source times at $`L`$. With $`q=1-p`$, its omitted probability is

```math
1-(1-q^L)^n\le nq^L.
```

The omitted tail of the mean-cycle sum is at most $`nq^L/p`$. Both analytic support-truncation bounds are chosen below $`10^{-14}`$. **These bounds do not include floating-point roundoff.** Stored endpoints are binary64 evaluations of mathematical bounds, not interval-arithmetic certificates. Logarithmic rate columns avoid numerical underflow for very small rates.

The recurrence calculation includes every acceptance probability and the factor of one half per round. Its displayed yield is an achievable recurrence-plus-hashing lower bound, not optimal two-way distillability. A zero depolarizing yield in the ASAP table applies to the displayed timing-forgetting construction; it does not show that every allowed policy has zero rate. The lifetime coefficients bound established regions and leave an unresolved interval, as described in [achievability](../science/achievability.md) and [finite bounds](../science/finite_bounds.md).
