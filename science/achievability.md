# Achievability with a fixed deadline

This page constructs protocols for the Bell-link chain defined in [the model](model.md). All elementary attempts, discarded pairs, recurrence failures and missed deadlines are included in the rate. Endpoint quantum storage and endpoint operations are ideal, as specified in that model.

## From reset cycles to deterministic-horizon rates

**Timing lemma.** Consider iid reset cycles of positive integer duration $`T`$, with finite mean $`M=\mathbb E T`$. A cycle's raw bipartite state may be correlated with its duration. Let $`\rho`$ be the average raw state after discarding the timing record. If LOCC distills $`d`$ ebits per copy from iid copies of $`\rho`$ asymptotically, then the fixed-horizon rate is at least $`d/M`$.

To prove this, use an infinite-run reference experiment, consisting of iid joint classical-quantum cycle outputs. For fixed $`\delta\gt0`$ and horizon $`H`$, select the deterministic number

```math
m_H=\left\lfloor\frac{H}{M+\delta}\right\rfloor.
```

The actual protocol tries to finish exactly these first $`m_H`$ cycles by $`H`$. If it succeeds, it runs a fixed-output distillation map on their raw pairs. Otherwise it discards unfinished ports and outputs a separable dummy on the same output register. The number $`k_H`$ of target Bell pairs is fixed in advance.

Discarding the first $`m_H`$ timing records in the reference experiment gives exactly $`\rho^{\otimes m_H}`$. Let $`\epsilon_m`$ denote the chosen distillation code's trace-distance error on $`m`$ iid inputs. The actual and reference experiments agree whenever

```math
S_{m_H}:=\sum_{j=1}^{m_H}T_j\le H.
```

On the complementary event their normalized output states have trace distance at most one. Averaging the classical-quantum branches therefore bounds the actual, unconditional error by

```math
\epsilon_{m_H}+\Pr(S_{m_H}\gt H).
```

The weak law makes the second term vanish because $`H/m_H\to M+\delta`$. For any $`d'\lt d`$, choose $`k_H=\lfloor d'm_H\rfloor`$. The attained rate tends to $`d'/(M+\delta)`$. Taking the supremum over $`d'`$ and $`\delta`$ proves the lemma.

This argument permits correlations between cycle duration and pair quality. It never conditions on a random number of completions and then asserts that the retained states are iid. A missed deadline contributes to the unconditional error; it is not a free postselection event.

The operational order of limits is essential: first $`H\to\infty`$ for fixed chain length and physical parameters, then compare the resulting rates as $`n\to\infty`$. No uniform finite coding-block guarantee is asserted.

## Synchronized generation

Attempt every edge in each slot and discard all partial successes if any edge fails. An all-success slot has probability $`p^n`$ and supplies a perfect end-to-end Bell pair immediately, with zero interior storage age. Successive inter-delivery times are iid geometric variables of mean $`p^{-n}`$. The timing lemma with one ebit per raw pair gives

```math
R_n(\tau,p)\ge p^n.
```

All failed slots have been included in that mean duration.

## The ASAP/reset protocol

Within a cycle, attempt each unfinished edge until its first success. Write the resulting iid success times as

```math
G_1,\ldots,G_n\sim\operatorname{Geom}(p),
\qquad \Pr(G_i=t)=p(1-p)^{t-1},\quad t=1,2,\ldots.
```

At interior node $`i`$, perform its Bell measurement at $`\max(G_i,G_{i+1})`$. These local measurements use disjoint physical ports; measurements already performed at neighboring nodes do not prevent their execution. Pauli-frame corrections can be completed when the cycle ends. The cycle duration and total interior age are

```math
T_n=\max_iG_i,
\qquad
A_n=\sum_{i=1}^{n-1}|G_i-G_{i+1}|.
```

Reset the factory after delivery. Independent source trials and independent Markov noise after reset make different cycles iid. The ASAP total-variation representation and the Werner-noise description are prior ingredients from [Goodenough, Coopmans and Towsley](../references/RELATED_WORK.md#gct25).

Let $`q=1-p`$ and $`\lambda=-\ln q`$. The mean cycle duration has the positive tail-sum representation

```math
\mathbb ET_n=\sum_{t=0}^{\infty}\left[1-(1-q^t)^n\right].
```

Couple each $`G_i`$ to $`\lceil E_i\rceil`$, where the $`E_i`$ are iid exponential variables of rate $`\lambda`$. With $`H_n=\sum_{j=1}^n1/j`$ this gives

```math
\frac{H_n}{\lambda}\le\mathbb ET_n\le\frac{H_n}{\lambda}+1,
\qquad
\mathbb ET_n=\frac{\ln n}{\lambda}+O(1).
```

Here the bounded term may depend on the fixed parameter $`p`$. The roughness mean is

```math
\mu_p:=\mathbb E|G_1-G_2|
=\frac{2(1-p)}{p(2-p)},
\qquad
\mathbb EA_n=(n-1)\mu_p.
```

Indeed, $`|G_1-G_2|=G_1+G_2-2\min(G_1,G_2)`$, and the minimum is geometric with parameter $`p(2-p)`$. The roughness summands are 1-dependent. Splitting them into odd and even sets proves $`A_n/n\to\mu_p`$ almost surely under the infinite-chain coupling.

## Averaging the raw state

For a given age $`A_n`$, the depolarizing model produces

```math
W(v)=v\Phi_2 +(1-v)\frac{I_4}{4},
\qquad v=e^{-A_n/\tau}.
```

Because this state is affine in visibility, forgetting the timing record gives exactly

```math
W(\bar v_n),
\qquad
\bar v_n=\mathbb E e^{-A_n/\tau}.
```

Jensen's inequality supplies a finite-chain lower bound:

```math
\bar v_n\ge \exp\left[-\frac{(n-1)\mu_p}{\tau}\right].
```

The [Bennett, DiVincenzo, Smolin and Wootters hashing protocol](../references/RELATED_WORK.md#bdsw96) achieves $`\max\{0,1-H(P)\}`$ ebits per Bell-diagonal input with Bell probabilities $`P`$. See also Devetak and Winter's [Theorem 10](https://arxiv.org/pdf/quant-ph/0306078) for the general coherent-information hashing inequality. Thus one may divide the hashing yield of $`W(\bar v_n)`$ by $`\mathbb ET_n`$ using the timing lemma. A zero in this particular lower bound does not imply zero optimal rate.

## A sufficient linear-lifetime coefficient using two-way LOCC

Set $`\tau=\kappa n`$ and

```math
v_*:=e^{-\mu_p/\kappa},
\qquad
F_*:=\frac{1+3v_*}{4}.
```

The Jensen bound gives $`\bar v_n\ge v_*`$ for every $`n`$. If

```math
\kappa\gt\frac{\mu_p}{\ln3},
```

then $`v_*\gt1/3`$ and $`F_*\gt1/2`$. If desired, the endpoints can locally degrade the average Werner state to this common fidelity $`F_*`$.

A fixed number of recurrence rounds followed by hashing has positive yield for every fixed Werner fidelity above $`1/2`$. For explicit resource accounting, write

```math
F_0=F_*,\qquad e_j=\frac{1-F_j}{3},
\qquad q_j=F_j^2+2F_je_j+5e_j^2,
\qquad F_{j+1}=\frac{F_j^2+e_j^2}{q_j}.
```

One round consumes two pairs and produces one retained pair with probability $`q_j`$. After $`\ell`$ rounds followed by hashing, the achievable yield per original raw pair is

```math
D_\ell(F_*)=
2^{-\ell}\left(\prod_{j=0}^{\ell-1}q_j\right)
\max\left\{0,1-h_2(F_\ell)-(1-F_\ell)\log_2 3\right\}.
```

These are the standard [BDSW96 recurrence and hashing formulas](../references/RELATED_WORK.md#bdsw96), Sections 3.2.1 and 3.2.3. The displayed yield includes every discarded input and failed acceptance.

For $`1/2\lt F_j\lt1`$,

```math
F_{j+1}-F_j=
\frac{(1-F_j)(4F_j-1)(2F_j-1)}{9q_j}\gt0.
```

The recurrence therefore converges to one, and a finite $`\ell`$ makes the hashing term positive. For fixed $`\ell`$, independent acceptance counts concentrate. Reserving deterministic slightly smaller counts at each round gives fixed-output LOCC codes; insufficient-count events are included in their vanishing error. The number of rounds and the resulting positive yield depend on $`p,\kappa`$, not on $`n`$.

Applying the timing lemma proves

```math
\boxed{
\kappa\gt\frac{\mu_p}{\ln3}
\quad\Longrightarrow\quad
R_n(\kappa n,p)\ge\frac{D_\ell(F_*)}{\mathbb ET_n}
=\Omega_{p,\kappa}\!\left(\frac1{\ln n}\right).
}
```

Direct hashing alone would require $`\kappa\gt\mu_p/[-\ln v_{\rm hash}]`$, where $`v_{\rm hash}\simeq0.7476138334`$. That stronger condition is unnecessary with two-way endpoint LOCC. The coefficient comparison with the converse, and its unresolved interval, are given in [finite bounds](finite_bounds.md).
