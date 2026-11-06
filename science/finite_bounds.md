# Finite rate bounds and linear coherence coefficients

The successful-profile count yields explicit bounds at finite chain length, including an exact synchronized regime and a sharper bound that charges each raw pair by its entanglement of formation. It also identifies a range of linear coherence times for which the distilled-ebit rate remains exponentially small.

We use the [model](model.md) and rate definition $`R_n(\tau,p)`$ from the [adaptive converse](adaptive_converse.md): one elementary attempt per edge per slot, arbitrarily many equally noisy interior buffers, monotone interval Bell swaps, ideal endpoint memories, and arbitrary endpoint LOCC on completed pairs. Throughout this page, $`\ln`$ denotes the natural logarithm and $`h_2`$ is binary entropy in bits. Write

```math
L=n-1,
\qquad
a_\tau=\lceil\tau\ln3\rceil-1,
\qquad
W(v)=v\Phi_2+(1-v)\frac{I_4}{4}.
```

## 1. Exact cutoff and synchronized regime

For a delivered pair with elementary source times $`t_1,\ldots,t_n`$, its accumulated interior exposure satisfies

```math
A\ge\operatorname{TV}(t)
=\sum_{i=1}^{n-1}|t_i-t_{i+1}|.
```

Its conditional state is $`W(e^{-A/\tau})`$, which is entangled exactly when $`A\lt\tau\ln3`$. Source times are integer slot indices. Consequently,

```math
\operatorname{TV}(t)\le A\lt\tau\ln3
\quad\Longrightarrow\quad
\operatorname{TV}(t)\le a_\tau.
```

The integer cutoff applies to source-time variation. Swap times and the total exposure $`A`$ may be real.

The number of signed integer increment vectors with $`L`$ coordinates and total absolute value at most $`a`$ is

```math
K_L(a)=\sum_{j=0}^{\min(L,a)}
2^j\binom Lj\binom aj.
```

This is $`K(n,a)`$ in the adaptive converse. Choose the $`j`$ nonzero coordinates, their signs, and their positive magnitudes. The number of positive $`j`$-tuples with sum at most $`a`$ is $`\binom aj`$. Anchoring the first source time gives at most $`H K_L(a)`$ profiles within $`H`$ source slots, hence

```math
p^n\le R_n(\tau,p)
\le\min\{p,\ p^nK_L(a_\tau)\}.
```

When $`0\lt\tau\le1/\ln3`$, the cutoff is $`a_\tau=0`$. Every entangled raw output then requires all its elementary leaves to have been generated in one common slot. Since $`K_L(0)=1`$, the upper bound matches synchronized generation:

```math
\boxed{
R_n(\tau,p)=p^n
\qquad
\text{for }0\lt\tau\le\frac1{\ln3}.
}
```

This equality concerns the optimal distilled-ebit rate, including arbitrary endpoint distillation. Independently, $`R_1(\tau,p)=p`$ for every $`\tau`$, since a single elementary edge has no noisy interior memory.

## 2. An entanglement-weighted envelope

The indicator count charges one ebit for every entangled raw arrival. Retaining its actual entanglement of formation gives a stronger finite bound.

For the two-qubit state $`W(v)`$, the concurrence and entanglement of formation are

```math
c(v)=\max\!\left\{0,\frac{3v-1}{2}\right\},
\qquad
E_F(W(v))=
h_2\!\left(\frac{1+\sqrt{1-c(v)^2}}2\right).
```

This is the [Wootters formula](../references/RELATED_WORK.md#wootters98), specialized to the isotropic Bell-state family. Define

```math
e_\tau(m)=E_F(W(e^{-m/\tau})).
```

The function $`e_\tau(m)`$ is nonincreasing in $`m`$, is at most one, and vanishes for $`m\ge\tau\ln3`$.

The number of increment vectors at exact radius $`m`$ is

```math
g_L(0)=1,
\qquad
g_L(m)=\sum_{j=1}^{\min(L,m)}
2^j\binom Lj\binom{m-1}{j-1}
\quad(m\ge1).
```

Equivalently, $`g_L(m)=K_L(m)-K_L(m-1)`$, with $`K_L(-1)=0`$. Define the weighted volume

```math
Q_L(\tau)=\sum_{m=0}^{a_\tau}g_L(m)e_\tau(m).
```

**Weighted finite converse.** For every permitted protocol with horizon $`H`$, fixed target of $`k`$ ebits, and unconditional half-trace-distance error $`0\le\varepsilon\le1/2`$,

```math
(1-2\varepsilon)k-h_2(\varepsilon)
\le H\min\{p,\ p^nQ_L(\tau)\}.
```

In particular,

```math
\boxed{
R_n(\tau,p)
\le\min\{p,\ p^nQ_L(\tau)\}
\le\min\{p,\ p^nK_L(a_\tau)\}.
}
```

**Proof.** The conditional product invariant in the [adaptive converse](adaptive_converse.md) makes each incoming raw pair a tensor factor of the endpoint state, conditional on the causal classical history. Subadditivity of $`E_F`$ bounds the increase upon arrival by that pair's $`E_F`$; endpoint LOCC cannot increase the expected budget.

If a raw pair has source increment vector $`d`$, then $`A\ge\|d\|_1`$ and therefore

```math
E_F(W(e^{-A/\tau}))\le e_\tau(\|d\|_1).
```

Different raw outputs consume different source tuples. Thus their total entanglement charge is bounded, for every execution, by the sum of these weights over all successful potential source profiles. Each deterministic profile requires one independent source success on every edge and has probability $`p^n`$. There are at most $`H g_L(m)`$ profiles of radius $`m`$. Taking expectations gives the budget $`H p^nQ_L(\tau)`$. Charging every raw pair to a distinct source success on one fixed edge also gives $`Hp`$. The fixed-target entanglement lower bound from the adaptive converse completes the proof.

The argument does not assume that adaptively selected profiles are independent, that the unconditional output stream is a product, or that $`E_F`$ is additive. Subadditivity and the causal conditional product statement suffice.

## 3. A finite example

Take $`n=10`$, $`p=1/2`$, and $`\tau=1`$ slot. Then $`a_\tau=1`$, $`g_9(0)=1`$, and $`g_9(1)=18`$. The weighted bound reduces to

```math
R_{10}(1,1/2)
\le 2^{-10}\left[1+18E_F(W(e^{-1}))\right].
```

The resulting rates, in ebits per source slot, are:

| Bound | Value |
| --- | ---: |
| Synchronized achievable lower bound | 0.0009765625 |
| Unweighted profile-count upper bound | 0.0185546875 |
| Entanglement-weighted upper bound | 0.0011180486153 |

The weighted upper bound is a factor $`1.1448818`$ above synchronized generation. Profiles with one unit of variation are numerous, but their raw Werner states lie close to the separability threshold and carry little entanglement of formation. Charging their full one-ebit maximum obscures this finite-size restriction.

## 4. Entropy of the profile count

For $`L\ge1`$ and $`0\lt z\lt1`$,

```math
\sum_{d\in\mathbb Z^L}z^{\|d\|_1}
=\left(\frac{1+z}{1-z}\right)^L.
```

For every integer $`a\ge0`$, it follows that

```math
K_L(a)
\le\inf_{0\lt z\lt1}
z^{-a}\left(\frac{1+z}{1-z}\right)^L.
```

If $`a\gt0`$ and $`\alpha=a/L`$, the minimizer satisfies $`\alpha=2z/(1-z^2)`$, giving

```math
z_\alpha=\frac{\alpha}{\sqrt{1+\alpha^2}+1},
\qquad
\ln K_L(a)\le L f(\alpha),
```

where

```math
f(\alpha)=\operatorname{arsinh}(\alpha)
 +\alpha\operatorname{arsinh}(1/\alpha),
\qquad f(0)=0.
```

The case $`a=0`$ follows by a limit. The function is continuous and strictly increasing, and

```math
f(\alpha)=\alpha\ln(2e/\alpha)+o(\alpha)
\qquad(\alpha\downarrow0).
```

This finite bound immediately gives $`\ln K_L(a)=o(n)`$ for $`a=o(n)`$ and therefore the exact sublinear-coherence rate exponent.

The same function is the exact exponential growth rate of the lattice volume: if $`a/L\to\alpha\gt0`$, then $`L^{-1}\ln K_L(a)\to f(\alpha)`$. For a lower bound, draw independent integer coordinates with probabilities proportional to $`z^{|d_i|}`$, choosing their mean absolute value slightly below $`\alpha`$. The law of large numbers puts almost all weight inside a narrow shell below $`\alpha L`$. Undoing this change of measure and letting the mean approach $`\alpha`$ matches the displayed upper exponent.

## 5. Exponential suppression for small linear coefficients

Suppose $`\tau_n/n\to\kappa\gt0`$. Then $`a_{\tau_n}/n\to\kappa\ln3`$, and the profile envelope implies

```math
\limsup_{n\to\infty}\frac1n\ln R_n(\tau_n,p)
\le\min\{0,\ \ln p+f(\kappa\ln3)\}.
```

Define

```math
\kappa_{\mathrm{count}}(p)
=\frac{f^{-1}(\ln(1/p))}{\ln3}.
```

For every fixed $`\kappa\lt\kappa_{\mathrm{count}}(p)`$, the upper bound has a strictly negative exponent. Thus a sufficiently small linear coherence coefficient still forces exponential suppression of the distilled-ebit rate.

The [ASAP construction](achievability.md) gives a complementary sufficient coefficient. With

```math
\mu_p=\frac{2(1-p)}{p(2-p)},
\qquad
\kappa_{\mathrm{rec}}(p)=\frac{\mu_p}{\ln3},
```

every fixed $`\kappa\gt\kappa_{\mathrm{rec}}(p)`$ supports

```math
R_n(\kappa n,p)=\Omega_{p,\kappa}(1/\ln n).
```

The average raw Werner visibility is at least $`e^{-\mu_p/\kappa}\gt1/3`$. The endpoints can degrade it to a fixed entangled Werner state, apply finitely many recurrence rounds, and then hash. Positive yield for every fixed Werner fidelity above $`1/2`$ is the [recurrence-plus-hashing result of Bennett, DiVincenzo, Smolin and Wootters](../references/RELATED_WORK.md#bdsw96). The deadline construction and all recurrence acceptance factors are included in [achievability](achievability.md).

Some illustrative coefficients are:

| Elementary success probability $`p`$ | Exponential suppression proved for $`\kappa\lt\kappa_{\mathrm{count}}`$ | Inverse-logarithmic rate achievable for $`\kappa\gt\kappa_{\mathrm{rec}}`$ |
| ---: | ---: | ---: |
| 0.1 | 1.634192 | 8.623319 |
| 0.2 | 0.762399 | 4.045508 |
| 0.5 | 0.194817 | 1.213652 |
| 0.8 | 0.042745 | 0.379266 |
| 0.9 | 0.016883 | 0.183887 |

The region between these sufficient conditions is unresolved. At $`p=1/2`$, for example, the arguments do not decide the optimal scaling for coefficients between approximately $`0.1948`$ and $`1.2137`$. They also do not settle equality at either threshold or prove an optimal inverse-logarithmic throughput above the sufficient coefficient.

Weighting profiles by $`E_F`$ improves finite bounds but does not change the lattice envelope's leading exponent at $`\tau=\kappa n`$. For any fixed positive margin below radius $`\kappa n\ln3`$, the weight is bounded below by a positive constant. Taking that margin to zero recovers the same profile entropy $`f(\kappa\ln3)`$. A sharper coefficient boundary requires information beyond this counting envelope.

## Appendix: a finite-horizon boundary correction

The factor $`H`$ used to anchor a profile can be sharpened when the horizon is short. For an increment vector $`d`$, define

```math
S_0=0,
\qquad S_j=\sum_{i=1}^j d_i,
\qquad
\operatorname{span}(d)=\max_jS_j-\min_jS_j.
```

Exactly $`(H-\operatorname{span}(d))_+`$ choices of the first source time place the whole profile in slots $`1,\ldots,H`$. Thus the finite weighted target bound can be strengthened to

```math
(1-2\varepsilon)k-h_2(\varepsilon)
\le
\min\!\left\{
Hp,
p^n\!\sum_{\|d\|_1\le a_\tau}
(H-\operatorname{span}(d))_+
e_\tau(\|d\|_1)
\right\}.
```

Here $`x_+=\max\{x,0\}`$. Replacing every anchor count by $`H`$ gives the simpler weighted envelope above. At fixed $`n,\tau`$, the normalized anchor count tends to one as $`H\to\infty`$, so this correction affects finite deadlines rather than the asymptotic rate coefficient.
