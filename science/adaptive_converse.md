# Adaptive entanglement converse

The [operational model](model.md) fixes the source bandwidth, memory law, interval-swap architecture, and one-way quantum interface with the endpoint laboratories. The argument below permits arbitrary classical control and arbitrary endpoint LOCC within that model.

## Finite converse and consequences

For an integer $`a\ge0`$, define

```math
K(n,a)=\sum_{j=0}^{\min(n-1,a)}
2^j\binom{n-1}{j}\binom aj,
\qquad
a_\tau=\lceil\tau\ln3\rceil-1.
\qquad\text{(4)}
```

Since $`\tau\gt 0`$, the integer $`a_\tau`$ is nonnegative. Put

```math
b_n(\tau,p)=\min\{p,\ p^nK(n,a_\tau)\}.
\qquad\text{(5)}
```

**Theorem 1 (adaptive endpoint-distillation converse).** Every protocol in the stated model with horizon $`H`$, fixed target size $`k\ge1`$, and trace-distance error $`0\le\varepsilon\le1/2`$ satisfies

```math
(1-2\varepsilon)k-h_2(\varepsilon)
\ \le\ H b_n(\tau,p),
\qquad\text{(6)}
```

where $`h_2`$ is the binary entropy. Consequently,

```math
p^n\le R_n(\tau,p)\le b_n(\tau,p).
\qquad\text{(7)}
```

The result permits arbitrary noisy buffering, pipelining, selective discards, history-dependent cutoffs, nonstationary control and endpoint-distillation feedback. It does not assume independent waiting times selected by the controller or a renewal structure for the protocol.

Two direct consequences are

```math
0\lt \tau\le\frac1{\ln3}
\quad\Longrightarrow\quad
R_n(\tau,p)=p^n,
\qquad\text{(8)}
```

and, for fixed $`p\in(0,1)`$,

```math
\tau_n=o(n)
\quad\Longrightarrow\quad
\lim_{n\to\infty}-\frac1n\ln R_n(\tau_n,p)
=\ln\frac1p.
\qquad\text{(9)}
```

The argument consists of a conditional quantum-state invariant, a source genealogy bound, and an entanglement budget for the endpoint laboratories.

## Conditional product invariant

### Two elementary channel identities

The depolarizing semigroup acts on one half of (1) as

```math
(\mathcal D_s\otimes\mathrm{id})[W(v)]
=W(ve^{-s/\tau}).
\qquad\text{(10)}
```

Independent exposure on both halves multiplies the visibility by the product of their attenuation factors.

For links on registers $`AB`$ and $`CD`$, let $`\mathcal B_m`$ denote the Bell measurement outcome $`m`$ on $`BC`$, including its known Pauli correction on the unmeasured registers. For every outcome $`m`$,

```math
\mathcal B_m\bigl(W(u)_{AB}\otimes W(v)_{CD}\bigr)
=\frac14 W(uv)_{AD}.
\qquad\text{(11)}
```

The right side is subnormalized. In particular, every outcome has probability $`1/4`$, independent of $`u`$ and $`v`$, and the corrected conditional output is the same for all outcomes. One obtains (11) by expanding each input into its Bell and maximally mixed parts. The Bell-Bell term contributes $`\Phi_2/4`$. Each of the other three terms contributes $`I_4/16`$. Their coefficients sum to $`1-uv`$. This calculation uses the averaged density matrices and does not condition on an unobserved Pauli-error trajectory.

Known Pauli frames can be corrected after every event without time cost. Equivalently, one may maintain virtual corrected registers, because the depolarizing channel is Pauli covariant and Bell outcomes update the frames classically.

### Lemma 2 (causal factorization)

After every observed history $`h`$, the reduced state of the extracted endpoint registers and all active-link registers has the form

```math
\Omega_h=
\sigma_h\otimes
\bigotimes_{\ell\in\mathcal L(h)}W(v_\ell(h)),
\qquad\text{(12)}
```

in the corrected Pauli frame. Here $`\sigma_h`$ is an arbitrary bipartite endpoint state, $`\mathcal L(h)`$ is the set of active links, and every visibility $`v_\ell(h)`$ is determined by the observed genealogy and exposure times. All unused local ancillas can be omitted. In particular, a complete link about to be extracted is conditionally independent of the previously extracted endpoint quantum systems and all other active links.

**Proof.** Initially the active-link set is empty and the endpoint state is separable. We verify preservation of (12) under each allowed event.

For a memory interval of duration $`s`$ selected from the current history, the joint memory law acts as a tensor product on the current active registers and as the identity on the endpoint bank. Equation (10) updates each link's visibility without creating correlations. Independence of later noise increments is needed at this step even when the duration or memory assignment depends on earlier endpoint outcomes.

A successful source trial appends a fresh $`W(1)`$ factor. Its success or failure flag is independent of every extant quantum register conditional on the current history. A failed trial appends no factor. Discarding a link takes a partial trace over one tensor factor. Buffer relabeling and known Pauli corrections also preserve the asserted product form.

A Bell swap acts on two active-link factors. Equation (11) shows that every normalized outcome replaces those two factors by $`W(uv)`$, with all other factors unchanged. Thus choosing later actions from Bell outcomes, or retaining only specified Bell outcomes, does not reveal a hidden error record or change the conditional state of another factor.

Extraction of $`\ell=[0,n]`$ removes its factor from the active set and changes the endpoint factor to

```math
\sigma'_h=\sigma_h\otimes W(v_\ell(h)).
\qquad\text{(13)}
```

Finally, consider an endpoint LOCC instrument with outcome $`y`$ and completely positive map $`\Lambda_{y|h}`$ on the extracted registers. Applied to (12), its unnormalized output is

```math
\Lambda_{y|h}(\sigma_h)\otimes
\bigotimes_{\ell\in\mathcal L(h)}W(v_\ell(h)).
\qquad\text{(14)}
```

The outcome probability is $`\mathrm{Tr}\Lambda_{y|h}(\sigma_h)`$. Normalization changes only the endpoint factor, so (12) holds after adding $`y`$ to the transcript. The scheduler may then choose any allowed action from this enlarged history. A classical random choice that does not arise from a quantum measurement simply refines the transcript without changing the conditional quantum state; a choice produced by an endpoint measurement is already covered by (14).

These events generate every finite protocol in the model, proving the invariant by induction. $`\square`$

Conditioning on earlier endpoint measurements is therefore harmless, even though those measurements can influence future source choices and ages. Conditioning on hidden noise labels or on future endpoint outcomes would be a different operation and is not used in the proof. The unconditional delivered stream need not be a product state. Equation (12) is the causal conditional statement required below.

## Source genealogies and storage exposure

Assign an immutable label $`(i,t)`$ to the Bell pair born from a successful trial on edge $`i`$ at time $`t`$. Give each active link its source genealogy. Generation creates one leaf; a swap takes the union of its two input genealogies; discard deletes a genealogy; extraction transfers it out of the active system.

**Lemma 3 (interval genealogy).** Every active link $`[a,b]`$ has exactly one elementary source leaf on each edge $`a+1,\ldots,b`$, and none on other edges. Genealogies of distinct active links are disjoint as sets of source labels. Once a source leaf belongs to an extracted link, it cannot appear in any later active or extracted link.

**Proof.** The assertion holds for every elementary source pair. A permitted swap joins $`[a,b]`$ and $`[b,c]`$, whose edge sets partition the interval from $`a`$ to $`c`$. The swap consumes both input identities and creates one link with their union. Its source leaves have not been used by any other active link. Discard and extraction remove the corresponding link identity, and the one-way endpoint interface prevents extracted systems from becoming new inputs. Induction proves all claims. $`\square`$

For a particular extracted link, write its elementary birth times as $`t_1,\ldots,t_n`$. At each intermediate vertex $`i`$, exactly one ancestral swap joins the parts to its left and right. Let $`s_i`$ be the time of that swap. The two measured qubits at vertex $`i`$ are the surviving local halves of the elementary leaves on edges $`i`$ and $`i+1`$. Operations at other vertices do not replace these qubits. They have been stored for durations $`s_i-t_i`$ and $`s_i-t_{i+1}`$, possibly under different local buffer labels. Therefore

```math
s_i\ge\max(t_i,t_{i+1}),
\qquad
A=\sum_{i=1}^{n-1}(2s_i-t_i-t_{i+1})
\ge\sum_{i=1}^{n-1}|t_i-t_{i+1}|.
\qquad\text{(15)}
```

The exposure $`A`$ counts every intermediate ancestral qubit's occupied time exactly once. It includes exposure incurred before and after remote swaps. Terminal storage contributes zero because the endpoint qubits are ideal. Applying (10) along each storage interval and (11) at each ancestral swap gives the extracted state

```math
W(e^{-A/\tau}).
\qquad\text{(16)}
```

Equation (15) is valid for any real swap times. Define the source-profile total variation by

```math
\mathrm{TV}(t)=\sum_{i=1}^{n-1}|t_i-t_{i+1}|.
\qquad\text{(17)}
```

Although $`A`$ can be real, $`\mathrm{TV}(t)`$ is an integer because source births are synchronized to integer slots.

### The entanglement threshold

The partial transpose of $`W(v)`$ has eigenvalues $`(1+v)/4`$ with multiplicity three and $`(1-3v)/4`$ with multiplicity one. It is entangled for $`v\gt 1/3`$. Separability at the boundary also follows directly from the finite product decomposition

```math
W(1/3)=\frac16\sum_{|\psi\rangle\in\mathcal S}
|\psi\rangle\langle\psi|\otimes
|\overline\psi\rangle\langle\overline\psi|,
\qquad\text{(18)}
```

where $`\mathcal S`$ contains the two eigenstates of each Pauli matrix and the bar denotes complex conjugation in the computational basis. For $`0\le v\le1/3`$,

```math
W(v)=3vW(1/3)+(1-3v)I_4/4
```

is separable. Thus the raw density matrix (16), conditioned on its observed causal history, is entangled exactly when

```math
A\lt \tau\ln3.
\qquad\text{(19)}
```

Every entangled raw delivery consequently has

```math
\mathrm{TV}(t)\le A\lt \tau\ln3,
\qquad
\mathrm{TV}(t)\le a_\tau.
\qquad\text{(20)}
```

The final integer inequality, rather than an integer bound on $`A`$, explains the ceiling and the subtraction of one in (4).

## Counting potential successful profiles

Independently sample $`X_{i,t}\sim\mathrm{Bernoulli}(p)`$ for every potential edge-slot trial, including trials that the controller never uses. Revealing $`X_{i,t}`$ only when that trial is chosen realizes exactly the stipulated source process. The variables remain independent on this underlying probability space even though the chosen trial indices and the delivered genealogies can be highly dependent.

Let $`N_{\mathrm{ent}}(H)`$ count raw pairs extracted by time $`H`$ whose conditional state (16) is entangled. By Lemma 3, different extracted pairs have different source profiles. Every counted profile belongs to

```math
\mathcal T_{H,a_\tau}=
\{t\in\{1,\ldots,H\}^n:
\mathrm{TV}(t)\le a_\tau\},
```

and every one of its source trials succeeded. Consequently the following is a pointwise inequality on the whole execution, before taking any expectation:

```math
N_{\mathrm{ent}}(H)
\le
\sum_{t\in\mathcal T_{H,a_\tau}}
\prod_{i=1}^{n}X_{i,t_i}.
\qquad\text{(21)}
```

It does not assert that a profile selected by the controller has probability $`p^n`$. Instead, each deterministic potential profile appearing on the right has that probability. Taking expectations therefore gives

```math
\mathbb E N_{\mathrm{ent}}(H)
\le p^n|\mathcal T_{H,a_\tau}|.
\qquad\text{(22)}
```

There are $`H`$ choices for $`t_1`$. For each choice, the integer increments $`z_i=t_{i+1}-t_i`$ satisfy $`\sum_i|z_i|\le a`$. Choosing their $`j`$ nonzero locations, their signs, and their positive magnitudes gives exactly

```math
\left|\left\{z\in\mathbb Z^{n-1}:\|z\|_1\le a\right\}\right|
=\sum_{j=0}^{\min(n-1,a)}2^j\binom{n-1}{j}\binom aj
=K(n,a).
\qquad\text{(23)}
```

For fixed $`j`$, the number of positive integer $`j`$-tuples whose sum is at most $`a`$ is $`\binom aj`$. Some anchored increment vectors leave the interval $`\{1,\ldots,H\}`$, so allowing all of them is an overcount. Hence

```math
|\mathcal T_{H,a}|\le HK(n,a),
\qquad
\mathbb E N_{\mathrm{ent}}(H)
\le Hp^nK(n,a_\tau).
\qquad\text{(24)}
```

Every raw delivery also consumes a distinct successful source trial on any fixed elementary edge. Thus

```math
N_{\mathrm{ent}}(H)\le N_{\mathrm{raw}}(H)
\le\sum_{t=1}^{H}X_{1,t},
\qquad
\mathbb E N_{\mathrm{ent}}(H)\le Hp.
\qquad\text{(25)}
```

Equations (24) and (25) give $`\mathbb E N_{\mathrm{ent}}(H)\le Hb_n`$. The source labels and the pointwise count are unaffected by leftover links or by preparing later links while an earlier pair is still being assembled. This is why the bound applies to steady operation as well as to protocols that reset globally.

## Endpoint entanglement budget

For a finite-dimensional bipartite state $`\rho`$, the entanglement of formation is defined by [BDSW96](../references/RELATED_WORK.md#bdsw96)

```math
E_F(\rho)=\inf_{\rho=\sum_xq_x|\psi_x\rangle\langle\psi_x|}
\sum_xq_x S\!\left(\mathrm{Tr}_B|\psi_x\rangle\langle\psi_x|\right).
\qquad\text{(26)}
```

We use convexity, monotonicity on average under LOCC instruments, and subadditivity,

```math
E_F(\rho\otimes\omega)\le E_F(\rho)+E_F(\omega).
\qquad\text{(27)}
```

These standard properties follow from the convex-roof construction and entropy concavity; average monotonicity is covered by Vidal's convex-roof monotone theorem [V00](../references/RELATED_WORK.md#vidal00). Subadditivity follows directly by taking products of pure-state ensembles in (26). Additivity is not required. A separable state has zero entanglement of formation, and a two-qubit state has at most one ebit. Equations (18) and (19) therefore imply

```math
E_F\bigl(W(e^{-A/\tau})\bigr)
\le\mathbf1\{A\lt \tau\ln3\}.
\qquad\text{(28)}
```

Let $`\sigma_h`$ be the extracted endpoint factor in (12). At an extraction event, (13), (27), and (28) give

```math
E_F(\sigma'_h)
\le E_F(\sigma_h)+\mathbf1\{A_h\lt \tau\ln3\}.
\qquad\text{(29)}
```

At an endpoint LOCC event with normalized conditional states $`\sigma_{hy}`$ and probabilities $`q(y|h)`$, average monotonicity gives

```math
\sum_yq(y|h)E_F(\sigma_{hy})\le E_F(\sigma_h).
\qquad\text{(30)}
```

Other allowed network events leave the endpoint factor unchanged on every normalized child history. This includes stochastic source and Bell outcomes because of Lemma 2. Applying (29) and (30) successively on the finite execution tree, with terminated branches padded by identities, yields

```math
\sum_h\Pr(h)E_F(\sigma_h^{\mathrm{final}})
\le \mathbb E N_{\mathrm{ent}}(H).
\qquad\text{(31)}
```

The initial value is zero because no shared endpoint entanglement is supplied. Discarding ancillary endpoint registers is local. Forgetting the classical transcript uses convexity. The averaged state of the fixed output registers therefore obeys

```math
E_F\bigl(\rho^{(H)}_{A_HB_H}\bigr)
\le\sum_h\Pr(h)E_F(\sigma_h^{\mathrm{final}})
\le\mathbb E N_{\mathrm{ent}}(H)
\le Hb_n(\tau,p).
\qquad\text{(32)}
```

In particular, a separable incoming raw pair cannot assist previous endpoint entanglement beyond this budget. It is important here that the incoming pair is a tensor factor conditional on the current history. Separability of each raw marginal alone would not establish (29) for a correlated stream.

## From entanglement budget to vanishing-error ebits

For any bipartite state,

```math
E_F(\rho)\ge -S(A|B)_\rho.
\qquad\text{(33)}
```

Indeed, conditional entropy is concave, and for each pure state $`\psi_x`$ in a decomposition of $`\rho`$, $`S(A|B)_{\psi_x}=-S(A)_{\psi_x}`$. Taking the infimum over decompositions proves (33).

Let $`\rho`$ be the state of the two $`d=2^k`$ dimensional target registers and suppose $`\frac12\|\rho-\Phi_d\|_1\le\varepsilon\le1/2`$. Measuring $`\{\Phi_d,I-\Phi_d\}`$ gives

```math
F=\mathrm{Tr}(\Phi_d\rho),\qquad
\delta=1-F\le\varepsilon.
\qquad\text{(34)}
```

Apply the bilateral twirl $`U\otimes\overline U`$, using shared classical randomness. It is an LOCC channel and maps $`\rho`$ to the isotropic state [HHH99](../references/RELATED_WORK.md#horodecki99)

```math
\mathcal T_d(\rho)=
(1-\delta)\Phi_d+
\frac{\delta}{d^2-1}(I-\Phi_d).
\qquad\text{(35)}
```

The twirl has a finite convex realization by Carathéodory's theorem applied to the finite-dimensional space of channels, so a continuum of control outcomes is not needed. Its marginal on either endpoint is $`I_d/d`$, and its joint entropy is $`h_2(\delta)+\delta\log_2(d^2-1)`$. Equations (33), (35), and LOCC monotonicity imply

```math
\begin{aligned}
E_F(\rho)
&\ge E_F(\mathcal T_d(\rho))\\
&\ge \log_2d-h_2(\delta)-\delta\log_2(d^2-1)\\
&\ge (1-2\varepsilon)k-h_2(\varepsilon).
\end{aligned}
\qquad\text{(36)}
```

The last inequality uses $`\delta\le\varepsilon\le1/2`$, the monotonicity of $`h_2`$ on this interval, and $`\log_2(d^2-1)\le2k`$. Only the fixed target registers appear, so the dimension of the endpoint ancillas does not enter.

Combining (32) and (36) proves (6). Dividing by $`H`$ and taking a vanishing-error sequence proves $`R_n(\tau,p)\le b_n(\tau,p)`$. The same finite inequality passes to norm limits of finite protocols on the fixed targets.

There is also an explicit version for a reported success branch. If success has probability $`s`$ and its success-conditioned $`k`$-ebit target has error $`\varepsilon\le1/2`$, then (31), convexity within the success histories, and (36) give

```math
s\bigl[(1-2\varepsilon)k-h_2(\varepsilon)\bigr]
\le Hb_n(\tau,p).
\qquad\text{(37)}
```

Thus rare postselection is charged by its probability. Conditioning on success alone cannot be substituted for the unconditional rate definition (3).

## Synchronized generation and the sublinear-lifetime exponent

Attempt every edge in every slot and discard all partial successes whenever at least one edge fails. If all edges succeed in the same slot, perform all intermediate Bell swaps immediately and extract the completed pair. It has $`A=0`$ and is exactly $`\Phi_2`$. Successful slots are independent with probability $`p^n`$. Keeping the resulting pairs in ideal endpoint storage and using a deterministic target smaller than the number normally collected gives any rate below $`p^n`$, with the shortage probability tending to zero by the law of large numbers. This proves the lower bound in (7).

If $`0\lt \tau\ln3\le1`$, then $`a_\tau=0`$ and $`K(n,0)=1`$. The two sides of (7) coincide, proving (8). The case $`n=1`$ also gives $`R_1=p`$ exactly, as required for a single ideal elementary source.

For general $`a\ge0`$, at most $`a`$ increments in (23) can be nonzero. Their signs contribute at most $`2^a`$. Nonnegative magnitude vectors with sum at most $`a`$ are counted by a weak-composition formula, giving

```math
K(n,a)\le2^a\binom{n+a-1}{a}.
\qquad\text{(38)}
```

If $`a=o(n)`$ and $`a\ge1`$,

```math
\ln K(n,a)
\le a\ln2+a\ln\!\left(\frac{e(n+a-1)}a\right)=o(n).
\qquad\text{(39)}
```

For $`a=0`$, the same conclusion is immediate. Since $`\tau_n=o(n)`$ implies $`a_{\tau_n}=o(n)`$, (7) gives

```math
n\ln p
\le\ln R_n(\tau_n,p)
\le n\ln p+o(n),
```

which proves (9). The hypothesis that $`p`$ is fixed matters. A sequence of increasing generation probabilities or parallel trial bandwidth is a different asymptotic resource model.

## Attribution and proof boundary

The Bell-state swapping rule, the multiplicative visibility description, and the total-variation exposure of the ASAP policy are established ingredients in the repeater literature. Goodenough, Coopmans and Towsley analyze this structure and its statistics for swap-ASAP chains [GCT25](../references/RELATED_WORK.md#gct25). Kamin and coauthors study accumulated dephasing and exact rates for specified distribution and swapping schemes [KSSV23](../references/RELATED_WORK.md#kamin23). The present use of (15) is a deterministic lower bound for every permitted source genealogy, combined with the pointwise potential-profile count (21) and the causal entanglement budget (31).

The proof does not treat intermediate distillation, encoded storage, error detection, coherent quantum reinjection at the endpoints, shared hidden memory noise, or source pairs correlated with existing registers. It also does not treat swap genealogies that backtrack along the chain. Unlimited buffers alone introduce none of these operations and are already included. The restriction to the stated Bell-link architecture remains essential to both the genealogy and factorization lemmas.
