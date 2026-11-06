# From noisy waiting to an entanglement-rate limit

Two distant laboratories want reliable shared entanglement. A chain of intermediate stations can create Bell pairs over short elementary links and join them into a longer pair. Generation succeeds at random times. Successful qubits wait in memory, where noise changes the resource they carry.

The central quantity is the **accumulated storage exposure of the qubits that supplied the final pair**. It can grow in proportion to chain length even when collecting all elementary successes takes only logarithmic time. This project turns that observation into a bound covering every permitted adaptive scheduling policy and collective endpoint distillation.

The [thirty-milestone map](MILESTONES.md) gives the detailed understanding targets. The [Wilde source bridge](SOURCE_BRIDGE.md) supplies the state, channel, entropy and operational foundations; the linked project proofs establish the repeater-specific steps developed here.

## 1. The resource and the rules

A Bell pair is a shared two-qubit state

```math
|\phi_2\rangle=\frac{|00\rangle+|11\rangle}{\sqrt2},
\qquad \Phi_2=|\phi_2\rangle\langle\phi_2|.
```

Each qubit separately has a maximally mixed state, yet the joint state is entangled. One perfect Bell pair supplies one **ebit**. A density operator also describes imperfect pairs and statistical mixtures, including uncertainty caused by an inaccessible noise environment. These distinctions begin in [M01–M02](MILESTONES.md#m01).

The [model](../science/model.md) has $`n`$ elementary edges. Each edge permits at most one attempt per slot, independently successful with fixed probability $`p`$. Success is heralded and supplies a fresh perfect Bell pair. Arbitrarily many noisy interior buffers are allowed. Interior stations may join adjacent interval links by ideal Bell measurements, track Pauli corrections, discard links and reset buffers. Classical communication and local processing take no modeled time.

Every occupied interior qubit undergoes independent Markov depolarization: storage for time $`s`$ contracts its Bloch vector by $`e^{-s/\tau}`$. The lifetime $`\tau`$ is measured in source-slot units. The assumption concerns the joint noise process, not just separate decay curves.

Endpoint memories are ideal. The endpoints can process completed pairs jointly by local operations and classical communication, abbreviated **LOCC**. Extracted systems never reenter the chain, and unfinished terminal qubits cannot interact with the endpoint bank. Interior purification, encoding, error detection, backtracking swaps and accessible noise-environment records are excluded. These resource boundaries are collected in [M13](MILESTONES.md#m13).

## 2. A complete three-edge history

Consider vertices $`0,1,2,3`$ and retained elementary birth times

```math
(t_1,t_2,t_3)=(1,3,2).
```

Edge 1 supplies its pair at time 1, edge 3 at time 2, and the middle edge at time 3. At time 3, both interior stations possess the two local qubits needed for their Bell measurements. The measurements use distinct physical registers and can occur in either order with zero processing time.

| Interior node | Birth times of its two qubits | Swap time | Local exposure |
| --- | --- | ---: | ---: |
| 1 | 1 and 3 | 3 | $`(3-1)+(3-3)=2`$ |
| 2 | 3 and 2 | 3 | $`(3-3)+(3-2)=1`$ |

The completed pair arrives at time $`T=3`$ with total interior exposure $`A=3`$. The endpoint qubits also waited, but their memories are ideal and add no noise exposure.

Now delay only node 1's swap until time 4. Node 2 can still join edges 2 and 3 at time 3, creating a link from vertex 1 to vertex 3. At time 4, node 1 joins that link to edge 1. Its two local qubits have each waited an additional slot, so $`A=5`$ and $`T=4`$. Delaying one interior swap by $`\delta`$ adds $`2\delta`$ exposure.

For a general completed lineage, let $`s_i`$ be the swap time at interior node $`i`$. Then

```math
A=\sum_{i=1}^{n-1}(2s_i-t_i-t_{i+1})
\ge\sum_{i=1}^{n-1}|t_i-t_{i+1}|
=\mathrm{TV}(t).
```

The inequality holds because a swap cannot precede either input's birth. The adjacent-time total variation is a lower bound on exposure; the delayed schedule has the same $`\mathrm{TV}=3`$ but larger $`A`$.

Completion time is a different quantity. Changing the births to $`(1,3,1)`$ leaves ASAP completion at time 3 but raises exposure to 4. The [genealogy and exposure proof](../science/adaptive_converse.md#source-genealogies-and-storage-exposure), developed in [M16–M17](MILESTONES.md#m16), extends this bookkeeping to arbitrary permitted schedules and buffers.

## 3. Exposure determines a state, not just a fidelity

Under depolarization, the corrected output is

```math
W(v)=v\Phi_2+(1-v)\frac{I_4}{4},
\qquad v=e^{-A/\tau}.
```

The visibility $`v`$ records the surviving Bell component. This state is entangled exactly when $`v\gt1/3`$. Take $`\tau=3`$ in the worked example. Immediate swapping gives $`v=e^{-1}\gt1/3`$, whereas the delayed swap gives $`v=e^{-5/3}\lt1/3`$. The delayed depolarizing output is separable.

Pure phase noise gives a different state at the same attenuation:

```math
Z(v)=\frac{1+v}{2}\Phi^+
     +\frac{1-v}{2}\Phi^-,
```

where $`\Phi^+=\Phi_2`$ and $`\Phi^-`$ projects onto $`(|00\rangle-|11\rangle)/\sqrt2`$. Unlike $`W(v)`$, this state occupies only two Bell components and remains entangled for every $`v\gt0`$. Both schedules therefore retain phase-noisy entanglement.

Equal coherence attenuation does not specify the full quantum state. The distinction matters because the endpoints can distill many raw pairs collectively. A raw-state calculation alone has not yet bounded that final rate. The threshold appears in [M18](MILESTONES.md#m18), and its operational noise comparison is completed in [M29](MILESTONES.md#m29).

## 4. Count potential successes before a policy selects them

The three-edge example also distinguishes two probability statements. Under first-success acquisition, the history $`(1,3,2)`$ requires edge 2 to fail twice and edge 3 once before succeeding. Its probability is

```math
p^3(1-p)^3.
```

A different controller can attempt edge 1 only at time 1, edge 3 only at time 2, and edge 2 only at time 3. All three designated attempts succeed with probability $`p^3`$. When they do, the retained profile and storage exposure are identical. Selected source times therefore need not follow the first-success distribution.

The converse supplies an independent Bernoulli variable for every potential edge-slot trial, including unused trials. Every completed pair consumes one source leaf on each edge; two outputs cannot reuse the same leaves. Each **fixed potential tuple** requires $`n`$ independent successes and has probability $`p^n`$. This is not a probability assigned after conditioning on the controller's adaptive selection.

An entangled depolarizing delivery requires

```math
\mathrm{TV}(t)\le A\lt\tau\ln3.
```

Birth times are integers, even when swap times are real. Thus the exact integer budget is

```math
a_\tau=\lceil\tau\ln3\rceil-1,
\qquad \mathrm{TV}(t)\le a_\tau.
```

There are at most $`H`$ choices for the first birth time within $`H`$ slots. The signed integer increments with total absolute value at most $`a`$ number

```math
K(n,a)=\sum_{j=0}^{\min(n-1,a)}
2^j\binom{n-1}{j}\binom aj.
```

Choose the nonzero positions, their signs and their positive magnitudes. Counting every successful potential profile gives

```math
\mathbb E N_{\mathrm{ent}}(H)
\le Hp^nK(n,a_\tau).
```

The [pointwise injection](../science/adaptive_converse.md#counting-potential-successful-profiles) behind this expectation is the central step in [M19](MILESTONES.md#m19). It includes replacements, selective discards, pipelining and feedback without treating chosen histories as independent.

## 5. Why the count also constrains endpoint distillation

Separable raw marginals alone would not justify a bound for a correlated stream. The proof establishes a stronger [causal invariant](../science/adaptive_converse.md#conditional-product-invariant): conditional on the complete observed history $`h`$, the state factors as

```math
\Omega_h=\sigma_h\otimes
\bigotimes_{\ell\in\mathcal L(h)}W(v_\ell(h)).
```

Here $`\sigma_h`$ is the entire extracted endpoint bank and $`\mathcal L(h)`$ is the set of active links. The endpoint bank may already contain complicated collective processing.

Fresh generation adds an independent factor. Product memory channels preserve factorization. For each corrected Bell outcome $`m`$,

```math
\mathcal B_m(W(u)\otimes W(v))
=\frac14W(uv).
```

The factor $`1/4`$ is the outcome probability; the normalized output is $`W(uv)`$. The outcome supplies a correction label, not a hidden-noise record. In the three-edge example, the two measurements have sixteen branches of probability $`1/16`$, all giving the same corrected state. Endpoint instruments act only on $`\sigma_h`$. Their outcomes can change subsequent scheduling while preserving the invariant on each causal branch. Hidden errors and future measurement outcomes are never conditioned on.

On extraction, the new endpoint state is $`\sigma_h\otimes W(v)`$. Entanglement of formation, $`E_F`$, is a mixed-state resource measure obtained by minimizing average pure-state entanglement over ensemble decompositions. Its subadditivity gives

```math
E_F(\sigma_h\otimes W(v))
\le E_F(\sigma_h)+E_F(W(v)).
```

A separable arrival contributes zero; any two-qubit arrival contributes at most one ebit. LOCC cannot increase expected $`E_F`$ across all measurement branches. Consequently the endpoint budget is bounded by $`\mathbb E N_{\mathrm{ent}}(H)`$. This uses neither additivity of $`E_F`$ nor equality between $`E_F`$ and an achievable distillation yield. [M15](MILESTONES.md#m15) and [M20](MILESTONES.md#m20) connect the invariant to this accounting.

## 6. Charge a fixed output, including failures

A rate protocol has a deterministic source horizon $`H`$ and predetermined target size $`k_H`$. Its output is compared with $`k_H`$ perfect ebits using

```math
\varepsilon_H=
\frac12\left\|\rho^{(H)}-\Phi_{2^{k_H}}\right\|_1.
```

The output averages over every branch, including failures and aborts. A rare successful branch cannot supply a rate while its probability is ignored. The definition takes $`H\to\infty`$ at fixed $`n,\tau,p`$, requiring $`\varepsilon_H\to0`$, before studying increasing chain length.

Nearly perfect target registers require nearly $`k_H`$ units of the entanglement budget. The [fixed-target argument](../science/adaptive_converse.md#from-entanglement-budget-to-vanishing-error-ebits) applies a free bilateral twirl preserving target overlap. Conditional-entropy concavity and the resulting isotropic spectrum give, for $`\varepsilon_H\le1/2`$,

```math
E_F(\rho^{(H)})
\ge(1-2\varepsilon_H)k_H-h_2(\varepsilon_H),
```

where $`h_2`$ is binary entropy. Only the designated target registers enter; the endpoint ancillas can be arbitrarily large. Combining the budget and source count gives

```math
(1-2\varepsilon_H)k_H-h_2(\varepsilon_H)
\le H\min\{p,\ p^nK(n,a_\tau)\}.
```

The additional bound $`p`$ charges every delivery to a distinct successful trial on one fixed edge. These steps join [M21–M22](MILESTONES.md#m21).

For a matching lower bound, attempt every edge each slot and discard partial successes. An all-edge-success slot produces a perfect pair immediately, with probability $`p^n`$. Over many slots, any fixed target rate below $`p^n`$ has vanishing shortage probability.

If $`\tau_n=o(n)`$, then $`\ln K(n,a_{\tau_n})=o(n)`$. The two bounds therefore imply

```math
\boxed{\ln R_n(\tau_n,p)=n\ln p+o(n).}
```

The correction divided by $`n`$ vanishes. Scheduling may still improve finite rates and subexponential factors. When $`\tau\le1/\ln3`$, the cutoff is zero and the stronger exact equality $`R_n=p^n`$ holds. The scaling argument is developed in [M24](MILESTONES.md#m24).

## 7. Constructive rates and the remaining gap

The ASAP/reset construction uses iid geometric first-success times $`G_i`$. Its duration and exposure are

```math
T_n=\max_iG_i,
\qquad A_n=\sum_{i=1}^{n-1}|G_i-G_{i+1}|.
```

At fixed $`p`$, $`\mathbb ET_n=\Theta(\ln n)`$, while $`\mathbb EA_n=(n-1)\mu_p`$, with $`\mu_p=2(1-p)/(p(2-p))`$. These are inherited ASAP ingredients, attributed in [achievability](../science/achievability.md#the-asapreset-protocol).

The average raw visibility is $`\mathbb E e^{-A_n/\tau}`$, not generally $`e^{-\mathbb EA_n/\tau}`$. A cycle's quality and duration are correlated. To meet a fixed deadline, choose a deterministic number of cycles below $`H/\mathbb ET_n`$ and compare with an infinite-run iid reference. The actual protocol declares failure if those cycles finish late. The timeout probability vanishes and is charged to the unconditional error. This [timing lemma](../science/achievability.md#from-reset-cycles-to-deterministic-horizon-rates), central to [M27](MILESTONES.md#m27), avoids an unjustified iid claim about pairs selected merely because they arrived by the deadline.

For $`\tau=\kappa n`$ and $`\kappa\gt\mu_p/\ln3`$, Jensen's inequality supplies a common entangled Werner input. Finitely many endpoint recurrence rounds followed by hashing give a positive constant yield, including all acceptance costs. The resulting rate is $`\Omega(1/\ln n)`$.

The linear-coefficient boundary remains open. At $`p=1/2`$, exponential suppression is proved for $`\kappa\lt0.194817\ldots`$, while the construction works for $`\kappa\gt1.213652\ldots`$. The intervening region and equality cases are unresolved; inverse-logarithmic throughput is an achievable rate, not an optimality claim. See [M25](MILESTONES.md#m25), [M28](MILESTONES.md#m28) and [finite bounds](../science/finite_bounds.md#5-exponential-suppression-for-small-linear-coefficients).

Finite bounds can nevertheless be sharp. Charging each arrival its actual $`E_F`$ places the ten-edge example $`p=1/2,\tau=1`$ between $`0.0009765625`$ and approximately $`0.0011180486`$ ebits per slot; [M23](MILESTONES.md#m23) explains that refinement.

For pure phase noise, positive hashing yield survives at every positive visibility. The [noise comparison](../science/noise_comparison.md) proves zero leading chain-length exponent for every diverging lifetime, including sublinear ones. That rate can still be tiny and require large coding blocks.

The [global synthesis](MILESTONES.md#m30) is therefore resource-specific: unlimited noisy buffering and ideal classical coordination leave the depolarizing exponent intact at fixed source bandwidth. Increasing generation bandwidth, changing the noise channel, adding intermediate quantum error mitigation or coupling protected endpoint systems back into unfinished links changes the question. The result establishes a precise limit for the stated architecture, with its inherited ingredients and remaining gaps visible.
