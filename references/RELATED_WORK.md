# Related work and attribution

The scientific contribution is a rate bound over adaptive scheduling policies in a specified unencoded repeater architecture. The ingredients inherited from quantum repeater analysis and entanglement theory are identified below. The [model](../science/model.md) fixes the operational comparison.

## Repeater timing and accumulated noise

<a id="gct25"></a>
### GCT25: exact analysis of swap-ASAP chains

Kenneth Goodenough, Tim Coopmans and Don Towsley, **On noise in swap ASAP repeater chains: exact analytics, distributions and tight approximations**, *Quantum* **9**, 1744 (2025). [Published article](https://quantum-journal.org/papers/q-2025-05-15-1744/) · [arXiv:2404.07146v5](https://arxiv.org/abs/2404.07146v5).

This is the closest structural predecessor. It represents the accumulated noise of a swap-as-soon-as-possible chain through differences of adjacent elementary generation times, and develops exact generating functions, fidelity distributions and asymptotic approximations. It also analyzes a global cutoff policy. Its principal model permits perfect endpoint memories and treats the relevant Pauli noise channels.

The storage-exposure identity, Bell-noise multiplication, ASAP construction and synchronized-success benchmark are inherited here. The new argument counts all feasible low-variation source histories in a presampled Bernoulli field. It therefore bounds arbitrary causal discarding, replacement, buffering and pipelining policies without assuming the first-success acquisition process used to analyze ASAP.

<a id="kamin23"></a>
### Kamin23: rates for imperfect memories and immediate swapping

Lars Kamin, Evgeny Shchukin, Frank Schmidt and Peter van Loock, **Exact rate analysis for quantum repeaters with imperfect memories and entanglement swapping as soon as possible**, *Physical Review Research* **5**, 023086 (2023). [Published article](https://doi.org/10.1103/PhysRevResearch.5.023086) · [arXiv source](https://arxiv.org/html/2203.10318v1).

This work analyzes waiting times, accumulated dephasing and secret-key rates for several parallel and sequential repeater schemes. Its optimality statements depend on the specified acquisition and swapping classes and chain sizes; its discussion distinguishes buffer replacement from simultaneous multiplexing. The time-dependent memory channel in the principal rate analysis is dephasing, while state preparation and local operations can introduce depolarizing errors.

The present theorem concerns distilled ebits, independent memory depolarization and all admitted adaptive policies at fixed generation bandwidth. It does not assert that ASAP is optimal at finite chain length. The [phase-noise comparison](../science/noise_comparison.md) explains why a dephasing raw-quality statement cannot be substituted for the depolarizing distilled-rate converse.

<a id="razavi09"></a>
### Razavi09: memory imperfections and distance scaling

Mohsen Razavi, Marco Piani and Norbert Lütkenhaus, **Quantum repeaters with imperfect memories: Cost and scalability**, *Physical Review A* **80**, 032301 (2009). [Published article](https://doi.org/10.1103/PhysRevA.80.032301) · [arXiv:0810.5334](https://arxiv.org/abs/0810.5334).

The connection between memory lifetime and distance scalability is established prior work. Razavi and colleagues analyze an optimized partial-nesting protocol with large memory banks, physical heralding delays and rate per employed memory. Their analysis gives exponential restrictions without purification and identifies the importance of memory coherence on propagation-time scales.

The present obstruction remains after classical propagation time and local processing time are set to zero. It arises from the sum of interior storage exposures, with one generation attempt per elementary edge per slot. The different noise, scheduling, throughput and resource conventions are essential to the comparison.

## Adaptive policies and network bounds

<a id="inesta23"></a>
### Inesta23: optimal policies with cutoffs

Álvaro G. Iñesta, Gayane Vardoyan, Lara Scavuzzo and Stephanie Wehner, **Optimal entanglement distribution policies in homogeneous repeater chains with cutoffs**, *npj Quantum Information* **9**, 46 (2023). [Published article](https://doi.org/10.1038/s41534-023-00713-9).

This work uses Markov decision processes to optimize entanglement distribution under imposed storage cutoffs and compares global-knowledge policies with local policies. Such finite-state optimization determines useful policies within its operational model. Our converse instead bounds the full admitted class without enumerating its state or action space; the comparison is about a distance exponent rather than a finite-chain policy optimum.

<a id="haldar24"></a>
### Haldar24: policies learned by reinforcement learning

Stav Haldar, Pratik J. Barge, Sumeet Khatri and Hwang Lee, **Fast and reliable entanglement distribution with quantum repeaters: Principles for improving protocols using reinforcement learning**, *Physical Review Applied* **21**, 024041 (2024). [Published article](https://doi.org/10.1103/PhysRevApplied.21.024041) · [arXiv:2303.00777v4](https://arxiv.org/html/2303.00777v4).

Adaptive, state-dependent cutoffs and coordination can improve waiting time and fidelity over fixed or dynamic swap-ASAP policies. Haldar and colleagues also construct nested policies for larger chains. These improvements are compatible with the present theorem: the bound does not rule out finite-chain or subexponential gains. It fixes the leading exponential rate in the stated sublinear-lifetime regime.

<a id="laurenza22"></a>
### Laurenza22: capacity bounds with lossy repeater stations

Riccardo Laurenza, Nathan Walk, Jens Eisert and Stefano Pirandola, **Rate limits in quantum networks with lossy repeaters**, *Physical Review Research* **4**, 023158 (2022). [Published article](https://doi.org/10.1103/PhysRevResearch.4.023158) · [arXiv:2110.10168](https://arxiv.org/abs/2110.10168).

Node splitting and channel-simulation methods provide rate limits when repeater stations introduce losses. The time-dependent analysis emphasizes that a memory's effective channel depends on its storage duration and hence on the chosen repeater protocol. Here the random successful source times are included explicitly, and the profile count bounds the storage patterns available to every admitted policy.

## Entanglement facts used in the proofs

<a id="bdsw96"></a>
### BDSW96: formation, recurrence and hashing

Charles H. Bennett, David P. DiVincenzo, John A. Smolin and William K. Wootters, **Mixed-state entanglement and quantum error correction**, *Physical Review A* **54**, 3824–3851 (1996). [Published article](https://doi.org/10.1103/PhysRevA.54.3824) · [arXiv:quant-ph/9604024](https://arxiv.org/abs/quant-ph/9604024).

The endpoint argument uses standard entanglement of formation, its average monotonicity under LOCC, and its subadditivity. The constructions use the hashing yield for Bell-diagonal states. A finite number of recurrence rounds followed by hashing gives a positive yield for every fixed two-qubit Werner fidelity above one half. These entanglement-theoretic ingredients are not new contributions of this project.

<a id="wootters98"></a>
### Wootters98: exact two-qubit entanglement of formation

William K. Wootters, **Entanglement of Formation of an Arbitrary State of Two Qubits**, *Physical Review Letters* **80**, 2245–2248 (1998). [Published article](https://doi.org/10.1103/PhysRevLett.80.2245) · [arXiv:quant-ph/9709029](https://arxiv.org/abs/quant-ph/9709029).

The [weighted finite bound](../science/finite_bounds.md) uses this exact formula for each arriving Werner pair. It sharpens the simpler count that assigns one ebit to every entangled raw pair.

<a id="vidal00"></a>
### Vidal00: monotonicity on average

Guifré Vidal, **Entanglement monotones**, *Journal of Modern Optics* **47**, 355–376 (2000). [Published article](https://doi.org/10.1080/09500340008244048) · [arXiv:quant-ph/9807077](https://arxiv.org/abs/quant-ph/9807077).

The convex-roof monotone theorem supplies average LOCC monotonicity of entanglement of formation. The adaptive endpoint budget applies this property at each recorded endpoint instrument; it does not require additivity of entanglement of formation.

<a id="horodecki99"></a>
### Horodecki99: isotropic twirling

Michał Horodecki, Paweł Horodecki and Ryszard Horodecki, **General teleportation channel, singlet fraction, and quasidistillation**, *Physical Review A* **60**, 1888–1898 (1999). [Published article](https://doi.org/10.1103/PhysRevA.60.1888) · [arXiv:quant-ph/9807091](https://arxiv.org/abs/quant-ph/9807091).

The bilateral isotropic twirl preserves the target singlet fraction and is an LOCC operation. In the converse, applying it to the fixed target registers gives a dimension-explicit lower bound on their entanglement of formation. The argument charges any reported success branch by its probability.

## What the comparison establishes

The prior works supply the noise bookkeeping, practical scheduling motivations and standard distillation machinery. The distinct contribution is the adaptive source-profile envelope and its conversion to an endpoint-distilled entanglement-rate bound. That conversion yields the exact sublinear-lifetime exponent, finite weighted bounds and a noise-channel distinction within one explicit resource model.

The result is an architecture theorem. It makes no unrestricted quantum-network capacity claim and does not compare all hardware resources through a single scalar coherence time. The [interpretation](../science/interpretation.md) explains how bandwidth, intermediate quantum processing and source timing enter that boundary.

A machine-readable bibliography is available in [references.bib](references.bib).
