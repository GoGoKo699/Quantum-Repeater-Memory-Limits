# Quantum repeater memory limits

## How much can scheduling recover from noisy memories?

A repeater chain can save successful elementary pairs, replace old ones and choose which segments to join. Its endpoints can then distill the delivered pairs collectively. This project determines the leading scheduling gain in the resulting entanglement rate when intermediate stations use unencoded memories and Bell swaps.

The chain has $`n`$ elementary edges, one independent generation attempt per edge per slot, and fixed success probability $`p\in(0,1)`$. Interior qubits undergo independent Markov depolarization with visibility attenuation $`e^{-s/\tau}`$ after storage time $`s`$. Endpoint memories are ideal. Classical control, noisy buffer capacity and endpoint LOCC are unrestricted within the [precise Bell-link model](science/model.md). Intermediate purification, quantum error correction and quantum reinjection from the endpoints are outside this model.

Let $`R_n(\tau,p)`$ be the optimal distilled-ebit rate per source slot, with fixed output size and vanishing unconditional error. For fixed $`p`$ and $`1\ll\tau_n\ll n`$, the [sharp scheduling law](science/scheduling.md) is

```math
\boxed{
\ln R_n(\tau_n,p)
=n\ln p+(\ln 3+o(1))\,\tau_n\ln(n/\tau_n).
}
```

At fixed $`\tau`$, the gain over synchronous generation is of order $`n^{\lceil\tau\ln 3\rceil-1}`$. A two-slot schedule attains these orders with two active storage qubits per intermediate node. The converse covers all causal policies in the model, including pipelining and arbitrarily many equally noisy buffers. The leading exponent $`n\ln p+o(n)`$ holds throughout $`\tau_n=o(n)`$.

## How the schedule and converse meet

Every delivered pair has one elementary source leaf on each edge, with birth times $`t_1,\ldots,t_n`$. Its accumulated interior exposure is at least

```math
\mathrm{TV}(t)=\sum_{i=1}^{n-1}|t_{i+1}-t_i|.
```

The corrected raw state has visibility $`e^{-A/\tau}`$ and is separable when $`A\ge\tau\ln3`$. Entangled deliveries must therefore come from a small set of source-time profiles. Each fixed profile requires $`n`$ independent successes. A pointwise count of all potentially successful profiles avoids assuming that profiles selected by an adaptive controller are independent.

The quantum step is equally necessary. Conditional on the observed causal history, each new raw pair is independent of the previously extracted endpoint registers. Entanglement of formation can therefore be charged at each arrival and cannot increase on average under endpoint LOCC. This controls final distilled ebits, including collective processing, retries and postselection. The [adaptive converse](science/adaptive_converse.md) proves this upper bound.

For attainment, partition the chain into contiguous blocks and alternate their orientations. In slot one, each block retains the successful run starting at its designated end. In slot two, it retries the remaining edges. On acceptance there is one change of birth slot inside each block, and adjacent blocks agree on their shared boundary. This gives one unit of exposure per block and many possible places to spend it. The [same-model comparison](science/scheduling.md) shows that mandatory first-success retention with full resets gives half the growing-lifetime coefficient.

## Finite and complementary results

Writing

```math
a_\tau=\lceil\tau\ln3\rceil-1,
\qquad
K(n,a)=\sum_{j=0}^{\min(n-1,a)}2^j\binom{n-1}{j}\binom aj,
```

the converse gives

```math
p^n\le R_n(\tau,p)\le\min\{p,\ p^nK(n,a_\tau)\}.
```

The [finite bounds](science/finite_bounds.md) sharpen the upper bound by weighting each profile with its actual two-qubit entanglement of formation. They give exact equality $`R_n=p^n`$ for $`0\lt\tau\le1/\ln3`$. For ten edges with $`p=1/2`$ and $`\tau=1`$ slot, the weighted envelope is

```math
0.0009765625\ \le\ R_{10}(1,1/2)\ \le\ 0.0011180486153
```

ebits per slot.

A linear lifetime can support a much larger rate. For

```math
\tau=\kappa n,
\qquad
\kappa\gt\frac{2(1-p)}{p(2-p)\ln3},
```

an ASAP/reset construction followed by endpoint recurrence and hashing achieves $`\Omega(1/\ln n)`$ ebits per slot. A separate converse proves exponential suppression for sufficiently small linear coefficients. The coefficient interval between these two sufficient conditions remains unresolved. The [achievability proof](science/achievability.md) accounts for correlated cycle durations, missed deadlines and all distillation failures.

The noise channel matters. With pure phase dephasing and the same coherence attenuation, every diverging lifetime permits a rate with zero leading distance exponent. The [noise comparison](science/noise_comparison.md) supplies an explicit achievable bound and a reproducible finite-chain illustration. A scalar memory lifetime alone does not determine the rate law.

## Reading routes

| Goal | Route |
| --- | --- |
| Learn the project from its foundations | [Learning guide](learning/README.md), [source bridge](learning/SOURCE_BRIDGE.md), [30 milestones](learning/MILESTONES.md) and [worked tutorial](learning/TUTORIAL.md) |
| Understand the physical question and its limits | [Interpretation](science/interpretation.md), then [model](science/model.md) |
| Check the theorem | [Scheduling theorem](science/scheduling.md), [model](science/model.md), [adaptive converse](science/adaptive_converse.md), [finite bounds](science/finite_bounds.md) |
| Check the constructions and noise distinction | [Achievability](science/achievability.md), then [noise comparison](science/noise_comparison.md) |
| Reproduce supporting calculations | [Verification guide](verification/README.md) and its recorded results |
| Compare with prior work | [Related work](references/RELATED_WORK.md) and [bibliography](references/references.bib) |

The [science map](science/README.md) identifies the authoritative page for each claim. The [machine-readable reading map](llms.txt) provides the same boundaries for assisted study.

The learning route uses one educational anchor, Wilde's author notes dated 5 December 2021, with version-specific section pointers and locally supplied explanations of the adaptive repeater argument. The shared milestone map describes the project's understanding targets and dependencies.

## Relation to prior work

The Bell-state noise bookkeeping and ASAP total-variation representation are established ingredients, including in [Goodenough, Coopmans and Towsley](references/RELATED_WORK.md#gct25) and [Kamin and coauthors](references/RELATED_WORK.md#kamin23). The contribution combines the adaptive rate bound with a two-slot schedule that attains the sharp subleading correction and a matching first-success benchmark. The [related-work comparison](references/RELATED_WORK.md) distinguishes this operational bound from specified-policy analyses, finite-chain scheduling optimization and propagation-sensitive memory limits.

## Purpose

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).

The repository is distributed under the [MIT license](LICENSE).
