# What the memory limit means

A repeater chain can wait for neighboring elementary links, keep successful pairs, discard stale pairs and choose which available segments to join. The [adaptive converse](adaptive_converse.md) asks how much these classical decisions can improve the eventual entanglement rate when the intermediate quantum processing consists of Bell swaps.

## Accumulated exposure and completion time are different resources

In the parallel first-success protocol, obtaining one success on every edge takes a mean time of order $`\log n`$ at fixed link probability $`p`$. The memory noise carried by the completed pair depends on a different quantity:

```math
A=\sum_{i=1}^{n-1}\lvert G_i-G_{i+1}\rvert.
```

The two qubits consumed by an interior swap can have spent different times in memory. Adding these contributions over the chain gives mean exposure proportional to $`n`$, even though the last elementary success arrives after only logarithmic time. This distinction is already visible in the ASAP noise analysis of [GCT25](../references/RELATED_WORK.md#gct25).

The new converse does not assume this acquisition policy. Every delivered pair has a source-time profile, and its exposure dominates that profile's total variation. A depolarizing output can remain entangled only when this total variation is small. For each anchored first source time, the number of such profiles grows subexponentially when the lifetime is sublinear in $`n`$, while every profile requires $`n`$ successful source events. This establishes the exact leading rate exponent for the whole permitted policy class.

## What scheduling can still improve

For fixed $`p`$ and $`\tau_n=o(n)`$, the statement

```math
\ln R_n(\tau_n,p)=n\ln p+o(n)
```

fixes the leading exponential dependence. It allows polynomial and larger subexponential advantages over synchronized generation. It also allows substantial improvements at finite length. Learned or optimized cutoff policies can therefore outperform ASAP, as in [Haldar24](../references/RELATED_WORK.md#haldar24), without contradicting the theorem.

Two finite statements make the result more concrete. When $`\tau\le1/\ln3`$ slots, the optimal rate is exactly $`p^n`$. At $`n=10`$, $`p=1/2`$ and $`\tau=1`$ slot, the entanglement-weighted converse places the optimum between $`0.0009765625`$ and approximately $`0.0011180486`$ ebits per slot. The derivations and numerical conventions are in [finite bounds](finite_bounds.md).

## Buffer capacity and source bandwidth

The converse allows arbitrarily many equally noisy stored pairs. Its resource restriction is one generation attempt per elementary edge per slot. Replacing an aged pair with a newer one or storing several candidates changes which source profile is selected, but does not change the probability of a fixed profile.

Increasing the number of simultaneous generation attempts changes that probability. For example, suppose each edge receives $`M`$ independent attempts per slot and retains one successful pair. Its effective success probability is

```math
p_M=1-(1-p)^M.
```

For $`n\ge2`$, choosing $`M_n=\lceil\ln n/[-\ln(1-p)]\rceil`$ gives $`p_{M_n}\ge1-1/n`$. Synchronized generation then achieves at least $`(1-1/n)^n`$ ebits per slot. This lower bound tends to $`e^{-1}`$, so the achieved rate has limit inferior at least $`e^{-1}`$. This construction pays a logarithmically increasing generation bandwidth on every edge. It does not obtain that rate from additional storage capacity at the fixed bandwidth of the theorem. No optimal bandwidth tradeoff is asserted.

## Endpoint distillation and the noise channel

Raw fidelity and distillable entanglement answer different questions. A low-fidelity pair can still be a useful input to collective endpoint processing. The converse therefore bounds the endpoints' accumulated entanglement of formation, rather than imposing a target fidelity on each raw delivery.

For depolarization, a completed pair becomes separable once its visibility falls to $`1/3`$. Conditional on the observed causal history, the arriving pair is a tensor factor of the endpoint state. A separable arrival therefore adds no entanglement of formation, and later adaptive endpoint processing cannot increase the expected budget. This finite separability threshold is what permits the count of low-variation source histories to control the final ebit rate.

Under pure dephasing, the output instead occupies two Bell states and has a positive hashing yield at every positive visibility. The [noise comparison](noise_comparison.md) proves that every diverging lifetime permits a rate with zero leading distance exponent. That rate can still be very small. The result uses unlimited ideal endpoint storage and takes the coding horizon to infinity at each fixed chain length.

## A linear lifetime is an order threshold, not a solved phase boundary

For $`\tau_n=\kappa n`$, the finite-volume entropy bound proves exponential suppression for a nonempty interval of small coefficients. A recurrence-and-hashing construction proves an inverse-logarithmic rate whenever

```math
\kappa\gt \frac{\mu_p}{\ln3},
\qquad
\mu_p=\frac{2(1-p)}{p(2-p)}.
```

At $`p=1/2`$, the proved exponential region is $`\kappa\lt0.194817\ldots`$, while the construction works for $`\kappa\gt1.213652\ldots`$. The interval between these sufficient regions and their boundaries is unresolved. The statements establish the required order of lifetime and useful coefficient bounds without identifying an exact transition.

## Physical units and model boundary

If a generation slot lasts $`\Delta t`$, a dimensionless memory lifetime $`\tau`$ represents physical lifetime $`\tau\Delta t`$, and a rate $`R_n`$ represents $`R_n/\Delta t`$ ebits per unit time. Fixed $`p`$ and fixed $`\Delta t`$ correspond to adding elementary segments with the same source operating conditions. Allowing them to change with chain length changes the asymptotic question.

Perfect fresh Bell pairs, independent Markov noise and instantaneous ideal local operations are part of the model. They make the synchronized lower bound attainable and isolate the obstruction due to memory storage. The result already grants instantaneous classical communication, so it is not a light-travel-time lower bound. Earlier propagation-sensitive memory-scaling analyses, including [Razavi09](../references/RELATED_WORK.md#razavi09), address a different source of delay.

Intermediate purification, encoding or quantum error correction changes the available quantum operations. Quantum feedback from protected endpoint registers into unfinished links changes the causal product invariant. Common memory noise or accessible environment records changes the statistical model. None is covered by substituting a different scalar lifetime into the present theorem. The exact allowed operations and endpoint interface are specified once in the [model](model.md).
