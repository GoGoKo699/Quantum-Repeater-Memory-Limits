# What scheduling gains from sublinear memory lifetimes

An unencoded Bell-link chain with sublinear depolarizing memory lifetime has the same leading rate exponent as synchronized generation. The first correction to that exponent is nevertheless large. Two slots suffice to attain it by keeping selected first-slot successes and retrying the other edges. The key choice is where the chain switches from first-slot to second-slot links. Each switch costs one unit of interior storage exposure.

Let $`R_n(\tau,p)`$ be the distilled-ebit rate per source slot in the [Bell-link model](model.md). Hold the elementary success probability $`p\in(0,1)`$ fixed. The protocol horizon tends to infinity at each fixed $`n,\tau,p`$ before the distance and lifetime limits below. All logarithms in the rate formulas are natural.

For $`\tau=\tau_n\to\infty`$ with $`\tau_n/n\to0`$,

```math
\boxed{
\ln R_n(\tau_n,p)
=n\ln p+(\ln 3)\tau_n\ln(n/\tau_n)
+O_p\!\bigl(\tau_n+\ln(n/\tau_n)\bigr).
}
```

The converse allows every policy in the model, including buffering, pipelining, adaptive replacement and endpoint distillation. The protocol uses at most one active memory qubit per incident edge at an intermediate node. It relies on the source clock, same-slot herald availability and zero-duration swaps of the stated model. The endpoints use ideal memory and two-way LOCC on extracted pairs.

Two other regimes clarify what the scheduling choice changes. For fixed $`\tau\gt0`$, put $`a_\tau=\lceil\tau\ln3\rceil-1`$. Then

```math
R_n(\tau,p)=\Theta_{p,\tau}\!\left(p^n n^{a_\tau}\right).
```

If acquisition is restricted to retaining the first successful trial on each edge until global reset or delivery, the growing-lifetime correction has coefficient $`(\ln3)/2`$. The precise restricted class and its matching bounds are given below.

## A finite two-slot policy

Choose an integer $`1\le a\le\lfloor n/2\rfloor`$ with $`a\lt\tau\ln3`$. Partition the edges into $`a`$ consecutive blocks of lengths $`m_1,\ldots,m_a\ge2`$, with $`\sum_jm_j=n`$. Give odd blocks a left-to-right orientation and even blocks a right-to-left orientation. The orientation fixes only the order in which the first-slot flags are read. All first-slot trials run in parallel.

1. In slot 1, attempt every edge. In each block, keep the initial run of successes in the chosen orientation. Require a nonempty run that stops before the end of the block. Discard all successes beyond the runs. If a block fails the requirement, discard the frame. On a remaining frame, swap at every vertex whose two incident selected links are from slot 1.
2. In slot 2, attempt every edge still lacking a selected link. If all these trials succeed, perform the remaining swaps and extract the end-to-end pair. Otherwise discard the frame. Each frame occupies two source slots, including frames already discarded after slot 1.

The first slot keeps a contiguous early segment in each block. Every block therefore has one interior transition between the two birth times. Across neighboring blocks, alternating orientation places late next to late or early next to early. For example, two blocks of four edges can produce the birth-time sequence $`(1,1,2,2\mid2,1,1,1)`$. Only two interior vertices see links arriving in different slots.

At each intermediate vertex, the scheduled swap time is the larger of the two incident birth times. A prior swap elsewhere leaves this vertex's local halves available. A first-slot pair beyond the selected run is discarded before retrying its edge, so at most one active half per incident edge is needed. The [genealogy identity](adaptive_converse.md#source-genealogies-and-storage-exposure) now gives $`A=a`$ for every accepted history. After correcting the Pauli frame, all accepted frames yield the same state $`W(e^{-a/\tau})`$.

For a block of length $`m`$, the event that the retained run has length $`k\in\{1,\ldots,m-1\}`$ and the second slot completes the block has probability

```math
p^k(1-p)p^{m-k}=(1-p)p^m.
```

The single failure factor is for the edge immediately after the first-slot run. The other first-slot flags beyond that edge are unrestricted. Events for different $`k`$ are disjoint, and source outcomes in different blocks are independent. Consequently the probability of an accepted frame is exactly

```math
P_a=p^n(1-p)^a\prod_{j=1}^{a}(m_j-1).
```

Let $`D_{\leftrightarrow}(W(v))`$ be the asymptotic two-way distillable entanglement per iid input pair, measured with fixed output size and vanishing unconditional error. It is positive for $`v\gt1/3`$, as shown by [recurrence followed by hashing](achievability.md#a-sufficient-linear-lifetime-coefficient-using-two-way-locc). The frames reset all chain registers between trials. Source outcomes and memory increments are independent, and the corrected accepted state is the same for every successful history. The number of source slots between accepted frames is twice a geometric variable of mean $`1/P_a`$. The [deterministic-horizon timing lemma](achievability.md#from-reset-cycles-to-deterministic-horizon-rates) yields

```math
\boxed{
R_n(\tau,p)\ge\frac{P_a}{2}D_{\leftrightarrow}(W(e^{-a/\tau})).
}
```

This rate includes the two slots spent on every rejected frame. Endpoint distillation can use any verified achievable yield in place of $`D_{\leftrightarrow}`$.

## Matching the profile converse

The [adaptive converse](adaptive_converse.md#finite-converse-and-consequences) gives $`R_n\le p^n K(n,a_\tau)`$, where $`K(n,a_\tau)`$ counts signed integer source-time increments of total variation at most $`a_\tau`$. For fixed $`a_\tau`$, its explicit finite sum is $`O(n^{a_\tau})`$. When $`a_\tau=0`$, synchronized generation attains the bound exactly. When $`a_\tau\ge1`$, use $`a=a_\tau`$ balanced blocks in the two-slot construction. The distillation yield is a positive constant at fixed $`\tau`$, and $`\prod_j(m_j-1)=\Theta_\tau(n^{a_\tau})`$. This proves the fixed-lifetime rate law, including the strict entanglement cutoff when $`\tau\ln3`$ is an integer.

In the growing sublinear regime, the [profile-volume bound](finite_bounds.md#4-entropy-of-the-profile-count) gives

```math
\ln K(n,a_\tau)\le a_\tau\ln(n/a_\tau)+O(a_\tau).
```

Here $`a_\tau=\tau\ln3+O(1)`$. Replacing $`a_\tau`$ by $`\tau\ln3`$ in the first term costs $`O(\ln(n/\tau))`$, while the constant $`\ln3`$ inside the resulting logarithm contributes only $`O(\tau)`$. This gives the upper bound in the first rate formula.

For the lower bound, take $`a=\lfloor\tau\ln3-1\rfloor`$ and balanced blocks. Eventually $`a\ge1`$ and $`n/a\ge4`$. Each factor $`m_j-1`$ is between $`n/(2a)`$ and $`n/a`$, so

```math
\ln P_a=n\ln p+a\ln(n/a)+O_p(a).
```

The choice of $`a`$ leaves at least one unit of exposure below the separability threshold. The accepted Bell fidelity $`F=(1+3e^{-a/\tau})/4`$ obeys

```math
F-\frac12=\frac{\exp((\tau\ln3-a)/\tau)-1}{4}\ge\frac{1}{4\tau}.
```

To bound the distillation cost, write $`q_F=F^2+2F(1-F)/3+5(1-F)^2/9`$ for the success probability of one recurrence round. The [recurrence formula](achievability.md#a-sufficient-linear-lifetime-coefficient-using-two-way-locc) gives, while $`1/2\lt F\le7/8`$,

```math
F_{\mathrm{next}}-F
=\frac{(1-F)(4F-1)(2F-1)}{9q_F}
\ge\frac{F-1/2}{36}.
```

Thus $`O(\ln\tau)`$ rounds suffice to reach fidelity at least $`7/8`$. Each round retains at least $`q_F/2\ge1/8`$ output pairs per input pair in the asymptotic yield. At $`7/8`$ the hashing yield is bounded below by the positive constant $`1-h_2(7/8)-(1/8)\log_2 3`$. As in the existing recurrence proof, each round can reserve a fixed count strictly below its expected output, with shortfalls included in the error. The attainable two-way yield is therefore at least a negative power of $`\tau`$ up to a constant. The logarithm of the distillation factor costs at most $`O(\ln\tau)`$ in the lower bound, which fits inside the stated remainder. This estimate uses an arbitrarily long coding horizon at each fixed $`n,\tau,p`$.

## First-success acquisition has half the correction

Consider the following restriction on acquisition. At most one chain attempt is active at a time, with at most one start per source slot. Each attempt begins empty with a fresh common first slot. It attempts every unresolved edge in every occupied slot and uses that edge's first success as its only selected pair. It may stop early using the causal record. It may deliver at most one complete link and carries no active links into the next attempt. Endpoint distillation is unrestricted within the original model. This class includes first-success swapping as soon as possible with global restart deadlines. The restriction concerns acquisition. Immediate swaps are still used by the two-slot selection policy above.

Let $`R_n^{\mathrm{first}}(\tau,p)`$ denote the rate optimized within this class. For $`\tau=\tau_n\to\infty`$ and $`\tau_n/n\to0`$,

```math
\boxed{
\ln R_n^{\mathrm{first}}(\tau_n,p)
=n\ln p+\frac{\ln3}{2}\tau_n\ln(n/\tau_n)
+O_p\!\bigl(\tau_n+\ln(n/\tau_n)\bigr).
}
```

### Upper bound for every horizon

Complete the prospective source history of one attempt with independent latent trials even if the actual attempt stops early. Conditional on the record when it starts, the prospective waiting times $`G_i`$ are independent geometric variables with parameter $`p`$ on $`\{1,2,\ldots\}`$. An entangled delivery from that attempt requires $`\sum_i|G_{i+1}-G_i|\le a_\tau`$ by the exposure bound. This implication holds regardless of the stopping rule, swap times and endpoint history.

Write $`q=1-p`$, $`u_i=G_i-1`$ and $`a=a_\tau`$. The geometric arrival law used by [Goodenough, Coopmans and Towsley](../references/RELATED_WORK.md#gct25) gives the exact weight $`p^n q^{\sum_i u_i}`$ for a profile. Their roughness generating function collects the same weights by total variation. Here we bound the low-variation part by counting runs of equal arrival time.

Subtract the minimum of the profile from every coordinate. The shifted profile has minimum zero and the same total variation. Summing over the common shift multiplies its weight by $`1/(1-q^n)\le1/p`$. Compress the shifted profile into consecutive runs of equal height. The list of signed nonzero jumps determines all run heights because their minimum is zero. A list of $`\ell`$ jumps has at most $`2^\ell\binom a\ell`$ possibilities: choose the signs and the positive magnitudes with sum at most $`a`$. Summing over $`0\le\ell\le a`$ gives at most $`3^a`$ lists.

For any such list, at most $`a`$ runs have positive height. A positive run of height $`h\ge1`$ and length $`L\ge1`$ contributes weight $`q^{hL}\le q^L`$. Summing its possible lengths gives at most $`q/(1-q)`$. If the profile has $`k+1`$ zero runs, its $`k`$ interior positive excursions each cost at least two units of variation. Thus $`k\le\lfloor a/2\rfloor`$. Given the positive-run lengths with total $`S`$, the remaining $`n-S`$ sites can be distributed among the zero runs in at most $`\binom{n-1}{k}`$ ways. When $`a\le n-1`$, this is at most $`\binom{n-1}{\lfloor a/2\rfloor}`$. Combining the bounds gives

```math
\Pr(\mathrm{TV}(G)\le a)
\le\frac{p^n}{p}\left[3\max\left\{1,\frac{q}{p}\right\}\right]^a
\binom{n-1}{\lfloor a/2\rfloor}.
```

In $`H`$ source slots there can be at most $`H`$ attempt starts. The chance of a future entangled delivery conditional on each start history is bounded by the same probability. Summing over start slots bounds the expected entangled deliveries up to horizon $`H`$ by $`H\Pr(\mathrm{TV}(G)\le a)`$, even with adaptive stopping. Each arrival increases the [conditional entanglement-of-formation budget](adaptive_converse.md#endpoint-entanglement-budget) by at most one ebit if entangled and zero if separable. The [fixed-target continuity bound](adaptive_converse.md#from-entanglement-budget-to-vanishing-error-ebits) therefore gives $`R_n^{\mathrm{first}}\le\Pr(\mathrm{TV}(G)\le a)`$ after the horizon limit.

At fixed $`a=a_\tau`$, the binomial upper bound is $`O(n^{\lfloor a/2\rfloor})`$. In the growing sublinear regime, its logarithm is $`(a/2)\ln(n/a)+O(a+\ln(n/a))`$. Substituting $`a_\tau=\tau\ln3+O(1)`$ gives the displayed upper correction and remainder.

### Matching first-success policy

Run two-slot frames. In slot 1, attempt every edge. For slot 2, retry precisely the edges that failed in slot 1. Keep a finished pair only if the late edges are exactly $`k`$ mutually nonadjacent interior edges and each succeeds on its retry. Swap whenever both incident links have arrived. The late edges exclude the two terminal edges, so each contributes two units of exposure. If $`2k\lt\tau\ln3`$, the accepted raw state is $`W(e^{-2k/\tau})`$.

For each legal choice of the $`k`$ late edges, the probability of this birth profile is $`p^n q^k`$. The choices are disjoint. Compressing the required gaps between chosen edges shows that their number is $`\binom{n-k-1}{k}`$. Independence across reset frames and the same timing lemma give

```math
R_n^{\mathrm{first}}(\tau,p)\ge
\frac12 p^n q^k \binom{n-k-1}{k}
D_{\leftrightarrow}(W(e^{-2k/\tau})).
```

At fixed lifetime, take $`k=\lfloor a_\tau/2\rfloor`$. The endpoint yield is a positive constant, and the binomial factor is of order $`n^k`$. For $`k=0`$, synchronized generation already gives the required lower bound. Together with the horizon-independent converse, this proves

```math
R_n^{\mathrm{first}}(\tau,p)=\Theta_{p,\tau}\!\left(p^n n^{\lfloor a_\tau/2\rfloor}\right).
```

For the growing sublinear lifetime, take $`k=\lfloor(\tau\ln3-1)/2\rfloor`$, which is positive and $`o(n)`$ in the stated regime. Then $`\ln\binom{n-k-1}{k}=k\ln(n/k)+O(k)`$ and the exposure remains at least one unit below the separability threshold. The recurrence estimate above bounds the logarithmic loss due to distillation by $`O(\ln\tau)`$. These estimates give the matching lower correction.

The source-time pattern explains the change in coefficient. First-success acquisition pays for every first-slot failure on a late edge. Sparse isolated late edges attain its correction and spend two transitions apiece. The alternating-block policy chooses extended late runs after the first-slot flags and pays for one first-slot failure per block. It needs one transition per independently chosen switch location. The adaptive converse confirms that this change attains the optimal first correction under the original source bandwidth and noise assumptions.
