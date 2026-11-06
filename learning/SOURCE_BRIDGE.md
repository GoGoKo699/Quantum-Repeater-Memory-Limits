# Source bridge

## Source identity

The single working anchor is Mark M. Wilde, [*From Classical to Quantum Shannon Theory*](https://markwilde.com/qit-notes.pdf), author notes dated **5 December 2021**. This is a draft companion to *Quantum Information Theory*, second edition (2017), not the published volume. The pointers below use this 772-page PDF; no source copy is included here.

## Section map

The topic labels are navigation aids. Page numbers are one-based PDF pages.

| Project prerequisite | Verified draft sections | Start pages |
| --- | --- | --- |
| Composite registers, Bell resources | [§§3.5–3.6](https://markwilde.com/qit-notes.pdf#page=88) | 88, 96 |
| Density descriptions, mixtures | [§§4.1.1–4.1.2](https://markwilde.com/qit-notes.pdf#page=118) | 118, 125 |
| Factors, separability, marginals, records | [§§4.3.1–4.3.4](https://markwilde.com/qit-notes.pdf#page=133) | 133, 135, 137, 144 |
| Channels, recorded outcomes | [§4.4](https://markwilde.com/qit-notes.pdf#page=145); [§4.6.8](https://markwilde.com/qit-notes.pdf#page=167) | 145, 167 |
| Phase, Pauli, depolarizing noise | [§§4.7.2–4.7.4](https://markwilde.com/qit-notes.pdf#page=171) | 171, 172, 173 |
| Bell measurement and correction | [§6.2.4](https://markwilde.com/qit-notes.pdf#page=211) | 211 |
| Operational error | [§§9.1.2, 9.1.5](https://markwilde.com/qit-notes.pdf#page=251); [§9.2](https://markwilde.com/qit-notes.pdf#page=261) | 251, 255, 261 |
| Entropy tools | [§§11.4–11.5](https://markwilde.com/qit-notes.pdf#page=327); [Exercise 11.7.5](https://markwilde.com/qit-notes.pdf#page=336) | 327, 330, 336 |
| Endpoint operations, block targets | [§§19.2–19.3](https://markwilde.com/qit-notes.pdf#page=536) | 536, 538 |

Section 19.2 uses $`E_R`$, not $`E_F`$. Lemma 19.4.1 concerns pure-state concentration, not this project's mixed-state hashing dependency.

## Notation

| Draft notation | Project translation |
| --- | --- |
| $`\lvert\Phi^+\rangle`$ | The density operator is $`\Phi_2=\lvert\phi_2\rangle\langle\phi_2\rvert`$. |
| $`\pi`$ | $`I_d/d`$. |
| $`\lVert\rho-\sigma\rVert_1`$ in §9.1.2 | The project error is half this norm. |
| $`H(A\mid B),\ I(A\rangle B)`$ | $`S(A\mid B),\ -S(A\mid B)`$. |
| Depolarizing parameter in Eq. (4.344) | $`1-e^{-s/\tau}`$; retain $`p`$ for source success. |

The remaining symbols are fixed by the [project model](../science/model.md). There are $`n`$ elementary edges. The deterministic source-time budget is $`H`$, the fixed target size is $`k_H`$, and $`R_n(\tau,p)`$ is measured in ebits per slot. The target error is

```math
\varepsilon_H=\frac12\left\|\rho^{(H)}-\Phi_{2^{k_H}}\right\|_1.
```

Entropies are in bits; $`\ln`$ is the natural logarithm. In the reset protocol,

```math
\mu_p=\mathbb E|G_1-G_2|=\frac{2(1-p)}{p(2-p)}
```

is the mean roughness per interior node. It is distinct from the mean cycle duration $`\mathbb E\max_iG_i`$ and from a coding block length.

## Project-specific steps

The source map supplies the background language. The following steps are established in the linked project proofs and depend on this architecture and stochastic model.

### Conditional factorization

An instrument describes a classical outcome and its conditional quantum state. It does not by itself imply that conditioning leaves different systems independent. The [causal factorization proof](../science/adaptive_converse.md#conditional-product-invariant) establishes the stronger statement

```math
\Omega_h=\sigma_h\otimes\bigotimes_{\ell\in\mathcal L(h)}W(v_\ell(h))
```

for every observed causal history $`h`$. The ingredients are fresh independent source pairs, the joint product Markov memory law, disjoint active-link registers, and the one-way quantum interface with the endpoint bank. The local identity

```math
\mathcal B_m\bigl(W(u)\otimes W(v)\bigr)=\frac14W(uv)
```

must hold for each corrected Bell outcome. Endpoint instruments then act only on $`\sigma_h`$. The induction conditions on available outcomes, never on hidden noise labels or future measurements. The unconditional delivered stream need not be a product state.

### Source histories and profile counting

The [genealogy argument](../science/adaptive_converse.md#source-genealogies-and-storage-exposure) connects a completed link to one elementary source event on every edge. Its storage exposure satisfies

```math
A\ge\mathrm{TV}(t)=\sum_{i=1}^{n-1}|t_i-t_{i+1}|.
```

The project's separability calculation for $`W(v)`$ then restricts an entangled delivery to the integer budget $`a_\tau=\lceil\tau\ln3\rceil-1`$. This is an integer bound on source-time variation even when swaps and storage ages occur at real times.

The [profile count](../science/adaptive_converse.md#counting-potential-successful-profiles) is a separate classical argument. Presample every potential Bernoulli source event, including unused events, and count deterministic successful profiles on that probability space. The resulting pointwise bound gives

```math
\mathbb EN_{\rm ent}(H)
\le Hp^nK(n,a_\tau),
\qquad
K(n,a)=\sum_{j=0}^{\min(n-1,a)}2^j\binom{n-1}{j}\binom aj.
```

Assigning probability $`p^n`$ to a profile selected adaptively by the controller would not justify this step. The proof instead sums over fixed potential profiles before taking expectation.

### An entanglement budget for the entire endpoint stream

The [endpoint budget](../science/adaptive_converse.md#endpoint-entanglement-budget) uses the convex-roof quantity $`E_F`$, together with its explicitly cited average LOCC monotonicity and tensor-product subadditivity. An incoming pair is charged only after the conditional tensor-factor statement has been proved. Extraction obeys

```math
E_F(\sigma_h\otimes W(v_h))
\le E_F(\sigma_h)+\mathbf1\{v_h\gt1/3\}.
```

Average monotonicity controls endpoint measurement branches, and convexity controls forgetting their records. Iterating over the actual execution tree bounds the final output's $`E_F`$ by $`\mathbb EN_{\rm ent}(H)`$. Separable raw marginals alone would not imply this bound for a correlated stream.

The [fixed-target argument](../science/adaptive_converse.md#from-entanglement-budget-to-vanishing-error-ebits) then derives $`E_F\ge-S(A|B)`$ from conditional-entropy concavity and the project's convex-roof definition. A target-preserving isotropic twirl gives

```math
(1-2\varepsilon_H)k_H-h_2(\varepsilon_H)
\le E_F\bigl(\rho^{(H)}\bigr).
```

This makes the target dimension explicit without bounding endpoint ancilla sizes. No identification of $`E_R`$ with $`E_F`$ is made.

### From raw-pair coding to source-time rate

The mixed-state recurrence and hashing inputs are cited in [achievability](../science/achievability.md#a-sufficient-linear-lifetime-coefficient-using-two-way-locc). The additional timing step is project-specific. A raw pair's quality can be correlated with its cycle duration, so conditioning on the number completed by $`H`$ does not automatically leave iid inputs.

The [fixed-deadline construction](../science/achievability.md#from-reset-cycles-to-deterministic-horizon-rates) selects the deterministic number

```math
m_H=\left\lfloor\frac{H}{\mathbb ET+\delta}\right\rfloor,
\qquad\delta\gt0,
```

of first cycles in an infinite-run iid reference. The real protocol uses the same fixed target registers and outputs a dummy if those cycles finish late. Its unconditional error is at most the distillation-code error plus

```math
\Pr(T_1+\cdots+T_{m_H}\gt H).
```

The latter vanishes by the law of large numbers. A raw yield of $`d`$ ebits per pair therefore supplies rate $`d/\mathbb ET`$ as a supremum. Recurrence rejections, failed elementary attempts and late cycles all remain charged. The limit $`H\to\infty`$ is taken at fixed $`n,\tau,p`$ before the large-chain comparison.
