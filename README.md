# Quantum repeater memory limits

## How much can scheduling recover from noisy memories?

A repeater chain can save successful elementary pairs, replace old ones and choose which segments to join. Its endpoints can then distill the delivered pairs collectively. This project bounds the resulting entanglement rate when intermediate stations use unencoded memories and Bell swaps.

The chain has $`n`$ elementary edges, one independent generation attempt per edge per slot, and fixed success probability $`p\in(0,1)`$. Interior qubits undergo independent Markov depolarization with visibility attenuation $`e^{-s/\tau}`$ after storage time $`s`$. Endpoint memories are ideal. Classical control, noisy buffer capacity and endpoint LOCC are unrestricted within the [precise Bell-link model](science/model.md). Intermediate purification, quantum error correction and quantum reinjection from the endpoints are outside this model.

Let $`R_n(\tau,p)`$ be the optimal number of distilled ebits per source slot, defined using a fixed output size and unconditional error tending to zero. The principal result is

```math
\boxed{
\tau_n=o(n)
\quad\Longrightarrow\quad
\ln R_n(\tau_n,p)=n\ln p+o(n).
}
```

Thus every sublinear memory lifetime has the same leading rate exponent as requiring all elementary sources to succeed in one slot. Adaptive control and endpoint distillation may still improve finite rates and subexponential factors. The result applies to all causal policies in the stated architecture, including pipelining and arbitrarily many equally noisy buffers.

## Why the bound holds

Every delivered pair has one elementary source leaf on each edge, with birth times $`t_1,\ldots,t_n`$. Its accumulated interior exposure is at least

```math
\operatorname{TV}(t)=\sum_{i=1}^{n-1}|t_{i+1}-t_i|.
```

The corrected raw state has visibility $`e^{-A/\tau}`$ and is separable when $`A\ge\tau\ln3`$. Entangled deliveries must therefore come from a small set of source-time profiles. Each fixed profile requires $`n`$ independent successes. A pointwise count of all potentially successful profiles avoids assuming that profiles selected by an adaptive controller are independent.

The quantum step is equally necessary. Conditional on the observed causal history, each new raw pair is independent of the previously extracted endpoint registers. Entanglement of formation can therefore be charged at each arrival and cannot increase on average under endpoint LOCC. This controls final distilled ebits, including collective processing, retries and postselection. The complete proof is in the [adaptive converse](science/adaptive_converse.md).

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
| Understand the physical question and its limits | [Interpretation](science/interpretation.md), then [model](science/model.md) |
| Check the theorem | [Model](science/model.md), [adaptive converse](science/adaptive_converse.md), [finite bounds](science/finite_bounds.md) |
| Check the constructions and noise distinction | [Achievability](science/achievability.md), then [noise comparison](science/noise_comparison.md) |
| Reproduce supporting calculations | [Verification guide](verification/README.md) and its recorded results |
| Compare with prior work | [Related work](references/RELATED_WORK.md) and [bibliography](references/references.bib) |

The [science map](science/README.md) identifies the authoritative page for each claim. The [machine-readable reading map](llms.txt) provides the same boundaries for assisted study.

## Relation to prior work

The Bell-state noise bookkeeping and ASAP total-variation representation are established ingredients, including in [Goodenough, Coopmans and Towsley](references/RELATED_WORK.md#gct25) and [Kamin and coauthors](references/RELATED_WORK.md#kamin23). The contribution here combines a bound for every permitted genealogy, a count of potential successful profiles and a causal endpoint entanglement budget. The [related-work comparison](references/RELATED_WORK.md) distinguishes this operational bound from specified-policy analyses, finite-chain scheduling optimization and propagation-sensitive memory limits.

## Purpose

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).

The repository is distributed under the [MIT license](LICENSE).
