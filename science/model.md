# Operational model

We study entanglement distribution through a line of elementary Bell-pair sources. Intermediate stations store unencoded qubits and join adjacent links by Bell measurements. The controller may choose generation attempts, swaps and discards from the entire causal classical record. The endpoint laboratories may distill every completed pair jointly and return classical information to the controller. The [adaptive converse](adaptive_converse.md) bounds this full adaptive process at fixed elementary generation bandwidth.

Throughout, entropies and entanglement are measured in bits. The symbol $`\ln`$ denotes the natural logarithm. Write

```math
|\phi_d\rangle=d^{-1/2}\sum_{j=0}^{d-1}|j\rangle|j\rangle,
\qquad
\Phi_d=|\phi_d\rangle\langle\phi_d|,
```

and define the Bell-centered isotropic state

```math
W(v)=v\Phi_2+(1-v)\frac{I_4}{4},\qquad 0\le v\le1.
\tag{1}
```

For two qubits this family is locally unitarily equivalent to the Werner family used in repeater models. We use the isotropic convention so that every corrected elementary pair is centered on $`\Phi_2`$.

## Sources, buffers and control

The chain has vertices $`0,1,\ldots,n`$ and elementary edges $`i=(i-1,i)`$, where $`n\ge1`$. It starts with no active links. Sources operate on a common clock. A successful trial indexed by $`(i,t)`$, with $`t\in\{1,2,\ldots\}`$, prepares one perfect Bell pair on edge $`i`$ at time $`t`$. Each edge permits at most one trial per slot. The potential trial outcomes form an independent Bernoulli process of parameter $`p\in(0,1)`$, independent of the memory noise, initial quantum registers and the controller's random seeds. The controller chooses whether to use a trial before learning that trial's outcome. A success is flagged and supplies a fresh Bell pair that is initially independent of all extant quantum registers; failure supplies no shared quantum system.

Each station may have arbitrarily many buffer qubits. Every finite experiment uses finitely many registers, but no bound on their number is imposed as a function of $`n`$ or the experiment's duration. The resource restriction is one elementary generation attempt per edge per slot, rather than a bound on buffer size.

An active link $`\ell=[a,b]`$, with $`0\le a\lt b\le n`$, consists of one qubit at vertex $`a`$ and one at vertex $`b`$, together with its classical identity and known Pauli frame. Distinct active links always occupy distinct quantum registers. Their spatial intervals may overlap. The permitted intermediate quantum operation is a Bell measurement that joins two distinct links $`[a,b]`$ and $`[b,c]`$, with $`a\lt b\lt c`$, into $`[a,c]`$. It consumes both measured qubits at $`b`$ and both input link identities. Its output occupies the two unmeasured endpoint qubits. The controller may also apply or track Pauli corrections, discard chosen links, reset unused buffers and relabel equally noisy local buffer registers. There is no intermediate purification, encoding, error detection, or coherent operation coupling links other than the stated Bell measurement.

Generation outcomes, all swap outcomes and the control record are available through free classical communication. Local operations have zero duration. Controls may occur at arbitrary causal real times between source births. Thus memory ages need not be integers; the elementary birth times are integers. Every finite-horizon protocol is a finite quantum instrument tree with arbitrary finite-dimensional local ancillas and an unrestricted number of finite LOCC rounds. The bound also holds for limits of such protocols on fixed target registers.

## Memory law

Every occupied qubit at an intermediate vertex evolves under

```math
\mathcal D_s(X)=e^{-s/\tau}X+
\bigl(1-e^{-s/\tau}\bigr)\operatorname{Tr}(X)\frac{I_2}{2},
\qquad \tau\gt 0.
\tag{2}
```

Between successive control events, the evolution on all occupied intermediate registers is the tensor product of these channels. The law is Markovian: after any observed causal history, later increments have this same product-channel action and no dependence on earlier environment states. There is no accessible environment record. Moving a qubit between buffers at the same vertex preserves its quantum state and does not restart its accumulated exposure. The qubits at vertices $`0`$ and $`n`$ have ideal storage.

Equation (2) is a property of the joint process, not merely of one-qubit marginals. Correlated noise with the same single-memory decay curve is not covered.

## Endpoint interface

The endpoint laboratories have ideal quantum storage and may perform arbitrary two-way LOCC on their extracted registers, including collective distillation, postselection and classical feedback to the controller. Initially these registers contain no shared entanglement. Their quantum interface with the chain is one-way: when a complete link $`[0,n]`$ is extracted, its two qubits move into the endpoint registers and its active-link identity is removed. Extracted quantum systems never reenter the chain. Before this extraction, endpoint processing does not couple an active link's terminal qubit to the laboratory's other quantum systems or measure it. Pauli frame corrections and ideal storage of terminal qubits are allowed.

This interface allows adaptive distillation of the entire delivered stream. It excludes using previously delivered quantum resources to purify or encode links that are still being assembled.

## Observed histories and operational rate

Let $`h`$ denote the complete observed classical transcript through a control event. It includes source flags, Bell outcomes, scheduling choices, recorded random coins and endpoint LOCC outcomes, including privately recorded outcomes when useful for analysis. It contains no hidden noise labels and no future measurement outcomes. Conditional states below refer only to histories of positive probability. Using this enlarged observed transcript in a proof grants the endpoints extra classical information if necessary; it does not provide a noise-environment record.

A protocol of horizon $`H\in\mathbb N`$ uses source slots $`1,\ldots,H`$, then outputs fixed target registers of dimension $`2^{k_H}`$ at each endpoint. Final endpoint LOCC is free. Its error is

```math
\varepsilon_H=
\frac12\left\|\rho^{(H)}_{A_HB_H}-\Phi_{2^{k_H}}\right\|_1,
\tag{3}
```

where $`\rho^{(H)}`$ is averaged over all outcomes, including failures and aborts. An aborted branch can be filled with a fixed separable target state. The distilled-ebit rate $`R_n(\tau,p)`$ is the supremum of $`\liminf_{H\to\infty}k_H/H`$ over protocol sequences with $`\varepsilon_H\to0`$. The limit in $`H`$ is taken at each fixed $`n,\tau,p`$. All retries, discarded links and unfavorable outcomes therefore contribute to elapsed source time.
