# Thirty milestones for understanding the repeater memory limit

This map follows the scientific problem: how independent link-generation attempts, noisy quantum storage, classical scheduling and endpoint distillation combine to determine an entanglement rate. Its understanding targets are intrinsic to the project. The [canonical science pages](../science/README.md) remain authoritative for assumptions, theorem statements, proofs and numerical bounds.

The map has two phases. **M01–M12 supply background and preliminaries**, starting from an individual quantum state and an elementary source, then connecting operations, entanglement and error to an operational rate. **M13–M30 develop the narrative and innovation**, assembling the local channel identities, causal invariant, genealogy and profile count into the converse, then connecting finite bounds, achievable rates and the noise comparison. This allocation gives the joint classical and quantum argument more space than its prerequisites. Each phase ends by integrating its components.

The single educational anchor is **Mark M. Wilde, *From Classical to Quantum Shannon Theory*, author notes dated 5 December 2021**, a companion draft to *Quantum Information Theory*, second edition (2017). All Wilde section numbers below refer to that notes version. The [source identity and bridge](SOURCE_BRIDGE.md#source-identity) specify the edition, verified section pointers and notation translation. The anchor supplies foundations; it does not contain the project's repeater converse. Entries explicitly distinguish **anchor foundations**, **local project derivations** and **primary research dependencies**. The latter identify imported scientific ingredients without adding another educational anchor.

| Phase | Milestones | Integration point |
| --- | --- | --- |
| [Background and preliminaries](#background) | [M01](#m01)–[M12](#m12) | A complete operational entanglement-distribution question |
| [Narrative and innovation](#innovation) | [M13](#m13)–[M30](#m30) | The theorem, its constructions, physical meaning and boundaries |

<a id="background"></a>
## Phase I: background and preliminaries

<a id="m01"></a>
### M01. States, mixtures and observed records

**Central question.** What does a density operator describe about one quantum memory and uncertainty in its preparation?

**Understanding target.** Distinguish a pure-state vector, a density operator, a weighted ensemble and a classical record identifying an ensemble member. Explain how forgetting a record produces a weighted average, and why the same density operator can have different ensemble descriptions.

**Dependencies and story role.** This is the starting point. Probability weights and weighted averages enter alongside the quantum-state notation, so later conditioning and rate statements have a common language.

**Conceptual connection.** The repeater's visibility parameter describes a density operator after inaccessible noise has been averaged out. Forgetting a timing record is also an averaging operation, but that record was available to the controller.

**Source pointers.** Anchor foundations: [Wilde §§4.1.1–4.1.2](SOURCE_BRIDGE.md#section-map). Project objects: [state conventions](../science/model.md) and [averaging the raw state](../science/achievability.md#averaging-the-raw-state).

<a id="m02"></a>
### M02. Two memories and one shared ebit

**Central question.** How can two qubits with individually random states supply a shared quantum resource?

**Understanding target.** Identify the Bell state $`\Phi_2`$ and its reduced states. Distinguish a tensor-product state, a separable mixture and an entangled state. Recognize that distinct physical registers need not have a product state.

**Dependencies and story role.** Builds on [M01](#m01) and moves from one memory to a pair shared between stations. It defines the resource that the sources supply and the endpoints ultimately seek.

**Conceptual connection.** The converse must establish tensor-product independence under the allowed process. Register separation and separability of individual marginals do not establish that independence by themselves.

**Source pointers.** Anchor foundations: [Wilde §§3.5–3.6 and §§4.3.1–4.3.3](SOURCE_BRIDGE.md#section-map). Project conventions: [Bell-state family](../science/model.md) and [causal factorization](../science/adaptive_converse.md#lemma-2-causal-factorization).

<a id="m03"></a>
### M03. Heralded sources and random waiting

**Central question.** What does a link-generation flag reveal, and what determines the time to a first success?

**Understanding target.** Interpret an independent Bernoulli trial of probability $`p`$, a flagged failure and a geometric waiting time. Distinguish success at a specified trial from first success at that trial: the latter also specifies earlier failures. Separate randomness in whether a fresh pair exists from hidden noise on a stored pair.

**Dependencies and story role.** Uses the probability weights of [M01](#m01) and the pair resource of [M02](#m02). It introduces the elementary stochastic supply before considering a network of such supplies.

**Conceptual connection.** Generation bandwidth counts opportunities per slot. The later adaptive count uses potential successful trials, while the ASAP construction uses first-success times.

**Source pointers.** Local probability preliminaries and model specialization: [sources, buffers and control](../science/model.md#sources-buffers-and-control) and [the ASAP/reset protocol](../science/achievability.md#the-asapreset-protocol). No Wilde section is claimed as a source of this geometric-clock model.

<a id="m04"></a>
### M04. Storage as a quantum channel

**Central question.** How does elapsed storage change a quantum state?

**Understanding target.** Read a quantum channel as a transformation of density operators. Explain composition over successive storage intervals, and distinguish depolarization from phase dephasing. Identify the stronger assumption that the whole memory process has independent Markov increments, rather than merely the same decay curve on each separate qubit.

**Dependencies and story role.** Builds on [M01](#m01) and [M02](#m02), adding physical evolution to the source picture in [M03](#m03).

**Conceptual connection.** Multiplicative attenuation will make ancestral storage exposures additive. The difference between the two noise channels will later change which raw pairs remain useful for distillation.

**Source pointers.** Anchor foundations: [Wilde §4.4 and §§4.7.2–4.7.4](SOURCE_BRIDGE.md#section-map). Project laws: [memory law](../science/model.md#memory-law) and [the phase-channel definition](../science/noise_comparison.md).

<a id="m05"></a>
### M05. Instruments and causal conditioning

**Central question.** What quantum state is justified after a recorded measurement outcome?

**Understanding target.** Relate an instrument's subnormalized output to its outcome probability and normalized conditional state. Distinguish conditioning on observed records from conditioning on unobserved noise labels or future outcomes. Explain the mixture obtained when an outcome record is forgotten.

**Dependencies and story role.** Uses [M01](#m01), [M02](#m02) and [M04](#m04). It supplies the event-by-event language for an adaptive protocol.

**Conceptual connection.** A scheduler can respond to recorded outcomes. The proof must show what those records reveal about the currently stored quantum systems, rather than assume that conditioning preserves independence.

**Source pointers.** Anchor foundations: [Wilde §4.3.4 and §4.6.8, especially Definition 4.6.10](SOURCE_BRIDGE.md#section-map). Project usage: [observed histories](../science/model.md#observed-histories-and-operational-rate).

<a id="m06"></a>
### M06. Bell measurements and joining links

**Central question.** How can a local measurement join two shared Bell pairs into a longer link?

**Understanding target.** Explain the Bell measurement, its classical outcome label and the associated Pauli correction or frame. Track which local qubits are consumed and which remote qubits survive. Distinguish this operation from copying a pair or protecting it with an error-correcting encoding.

**Dependencies and story role.** Builds on the Bell resource in [M02](#m02) and the instrument description in [M05](#m05). It introduces the physical junction from which the permitted repeater operations are assembled.

**Conceptual connection.** Teleportation provides the local mechanism. The precise noisy-state swapping identity used by this project is a separate statement established in [M14](#m14).

**Source pointers.** Anchor foundations: [Wilde §3.6 and §6.2.4](SOURCE_BRIDGE.md#section-map). Project operation: [interval Bell swaps](../science/model.md#sources-buffers-and-control). Primary repeater dependency: [GCT25](../references/RELATED_WORK.md#gct25).

<a id="m07"></a>
### M07. Local operations and classical coordination

**Central question.** What can separated laboratories do with free classical communication and local quantum processing?

**Understanding target.** Identify LOCC and explain why it preserves separability. Distinguish a probabilistic local branch from the complete instrument with all branch probabilities. Understand that classical coordination is free in the model while shared entanglement remains a resource.

**Dependencies and story role.** Combines the shared-state picture of [M02](#m02) with the recorded operations of [M05](#m05) and [M06](#m06). It establishes the operational resource framework.

**Conceptual connection.** The endpoint laboratories receive broad processing power. A converse for their eventual output must account for collective operations and their probability costs.

**Source pointers.** Anchor foundations: [Wilde §19.2](SOURCE_BRIDGE.md#section-map). Project specialization: [endpoint interface](../science/model.md#endpoint-interface).

<a id="m08"></a>
### M08. Entropy and coherent information

**Central question.** Which information quantities connect a mixed shared state to its entanglement resources?

**Understanding target.** Interpret entropy in bits, joint and conditional entropy, and coherent information $`-S(A|B)`$. Recognize that quantum conditional entropy can be negative. Distinguish a state's Bell spectrum from a single fidelity or visibility parameter.

**Dependencies and story role.** Builds on the states and subsystems of [M01](#m01) and [M02](#m02). It supplies the information quantities used by the endpoint budget and by distillation.

**Conceptual connection.** The Bell spectrum determines a hashing yield. Conditional entropy also supplies a lower bound on the resource needed for a nearly perfect output.

**Source pointers.** Anchor foundations: [Wilde §§11.4–11.5 and §11.7, including Exercise 11.7.5](SOURCE_BRIDGE.md#section-map). Project uses: [target conversion](../science/adaptive_converse.md#from-entanglement-budget-to-vanishing-error-ebits) and [averaging the raw state](../science/achievability.md#averaging-the-raw-state).

<a id="m09"></a>
### M09. An entanglement budget for mixed states

**Central question.** How can the entanglement carried by mixed inputs be bounded through probabilistic processing?

**Understanding target.** Interpret entanglement of formation $`E_F`$ as a convex-roof quantity. Distinguish convexity, monotonicity on average under LOCC and tensor-product subadditivity. Recognize that these properties neither assert additivity nor identify $`E_F`$ with the achievable distillation rate.

**Dependencies and story role.** Combines entanglement from [M02](#m02), allowed processing from [M07](#m07) and entropy from [M08](#m08). It provides the resource-accounting tool used in the converse.

**Conceptual connection.** A separable tensor-factor arrival contributes zero to this budget, while a two-qubit arrival contributes at most one ebit. The causal qualification will be essential in [M20](#m20).

**Source pointers.** Anchor orientation: [Wilde §19.2](SOURCE_BRIDGE.md#section-map), whose relative-entropy measure is not $`E_F`$. Primary dependencies for $`E_F`$: [BDSW96](../references/RELATED_WORK.md#bdsw96) and [Vidal00](../references/RELATED_WORK.md#vidal00). Canonical project definitions and properties: [endpoint entanglement budget](../science/adaptive_converse.md#endpoint-entanglement-budget).

<a id="m10"></a>
### M10. Approximate outputs and isotropic twirling

**Central question.** What does it mean to deliver a nearly perfect target state?

**Understanding target.** Interpret half the trace norm distance as an error criterion and relate it to the target-projector probability. Explain how a bilateral random-unitary twirl preserves that probability while simplifying the state. Distinguish unconditional output error from error conditioned on a favorable branch.

**Dependencies and story role.** Uses [M01](#m01), [M02](#m02), [M05](#m05) and [M07](#m07). It defines the quality requirement before introducing an asymptotic output rate.

**Conceptual connection.** The project applies the twirl only to fixed target registers. It thereby avoids making the error bound depend on the size of ancillary endpoint storage.

**Source pointers.** Anchor foundations: [Wilde §9.1.2 and §9.1.5](SOURCE_BRIDGE.md#section-map); the project uses half the source's trace-norm distance. Primary twirling dependency: [Horodecki99](../references/RELATED_WORK.md#horodecki99). Project application: [vanishing-error target bound](../science/adaptive_converse.md#from-entanglement-budget-to-vanishing-error-ebits).

<a id="m11"></a>
### M11. Distillation yield and its costs

**Central question.** How can many noisy pairs yield fewer nearly perfect pairs?

**Understanding target.** Distinguish raw-pair supply from distilled-ebit yield. Explain the roles of one-way hashing and two-way recurrence, including discarded inputs and failed acceptance. Recognize that a zero hashing lower bound need not mean zero distillable entanglement.

**Dependencies and story role.** Combines [M07](#m07)–[M10](#m10). It turns the abstract shared-state framework into an achievable output resource per supplied pair.

**Conceptual connection.** Endpoint distillation changes the meaning of useful raw quality. It is indispensable both to the linear-lifetime construction and to the phase-noise comparison.

**Source pointers.** Anchor orientation: [Wilde §§19.2–19.4](SOURCE_BRIDGE.md#section-map), concerning LOCC and pure-state manipulation. Mixed-state hashing and recurrence are primary dependencies from [BDSW96, §§3.2.1 and 3.2.3](../references/RELATED_WORK.md#bdsw96), not claims about Wilde's pure-state hashing lemma. Project construction: [two-way endpoint distillation](../science/achievability.md#a-sufficient-linear-lifetime-coefficient-using-two-way-locc).

<a id="m12"></a>
### M12. An operational rate question

**Central question.** How do source timing, quantum quality and allowed operations combine into a meaningful rate?

**Understanding target.** Assemble a fixed time horizon, a predetermined target size and an unconditional error criterion into an entanglement rate. Explain why the coding horizon tends to infinity at fixed chain length before studying growth in chain length. Distinguish latency, raw-pair throughput, distilled yield and a bound on the optimal rate.

**Dependencies and story role.** Integrates the stochastic supply of [M03](#m03), the noise and instrument framework of [M04](#m04)–[M07](#m07), and the quality and distillation concepts of [M08](#m08)–[M11](#m11). This is the synthesis of Phase I.

**Conceptual connection.** A rate claim becomes meaningful only after its resources, error accounting and limits are fixed. Phase II specializes this framework to the architecture and then proves its restrictions.

**Source pointers.** Local operational definition: [observed histories and rate](../science/model.md#observed-histories-and-operational-rate). Project explanation of the order of limits: [fixed-deadline conversion](../science/achievability.md#from-reset-cycles-to-deterministic-horizon-rates). The timed repeater definition is a project specification, not an imported textbook theorem.

<a id="innovation"></a>
## Phase II: narrative and innovation

<a id="m13"></a>
### M13. The exact architecture and resource boundary

**Central question.** Which improvements are already granted to the controller, and which would change the problem?

**Understanding target.** Identify fixed source success probability and per-edge generation bandwidth, unlimited equally noisy buffers, monotone interval Bell swaps, independent product memory noise, free classical communication and ideal endpoint storage. Explain the completed-pair extraction interface and why quantum reinjection into unfinished links is excluded.

**Dependencies and story role.** Specializes [M03](#m03), [M04](#m04), [M06](#m06), [M07](#m07) and [M12](#m12). It fixes the objects and operations to which every subsequent argument applies.

**Conceptual connection.** Extra storage capacity, extra generation bandwidth and extra quantum processing are distinct resources. The converse grants the first while holding the latter two to the stated model.

**Source pointers.** Local project specification: [sources and control](../science/model.md#sources-buffers-and-control), [memory law](../science/model.md#memory-law) and [endpoint interface](../science/model.md#endpoint-interface). Physical translation: [buffer capacity and source bandwidth](../science/interpretation.md#buffer-capacity-and-source-bandwidth).

<a id="m14"></a>
### M14. Closure under storage and individual swap outcomes

**Central question.** What can one storage interval or one recorded Bell outcome change in the link state?

**Understanding target.** Explain the attenuation of $`W(v)`$ and the corrected conditional swap output proportional to $`W(uv)`$. Identify why each Bell outcome has probability one quarter for these inputs and provides no hidden-noise label. Keep this local calculation distinct from a statement about a full adaptive network.

**Dependencies and story role.** Uses [M02](#m02), [M04](#m04)–[M06](#m06) and [M13](#m13). It supplies the quantum identities from which the global invariant is built.

**Conceptual connection.** Multiplication of visibility makes storage exposure additive, while the outcome-resolved identity permits causal conditioning without changing the corrected state family.

**Source pointers.** Canonical local derivation: [two elementary channel identities](../science/adaptive_converse.md#two-elementary-channel-identities). Inherited repeater ingredient: [GCT25](../references/RELATED_WORK.md#gct25). Anchor foundations are those identified in [M04](#m04)–[M06](#m06).

<a id="m15"></a>
### M15. A causal product invariant

**Central question.** Why is the arriving pair independent of the previously extracted endpoint registers at the instant of extraction?

**Understanding target.** Follow the conditional factorization into an endpoint state and active-link factors through every allowed event. Explain why endpoint LOCC outcomes may control future scheduling without breaking it. Distinguish this current-history invariant from independence of the unconditional delivered stream.

**Dependencies and story role.** Combines [M05](#m05), [M07](#m07), [M13](#m13) and [M14](#m14). It establishes the quantum statement needed to cover arbitrary causal feedback.

**Conceptual connection.** Independent source resets, product Markov increments and the one-way quantum interface work together. Disjoint source leaves alone would not establish the required quantum independence under a different noise or feedback model.

**Source pointers.** Local project proof: [Lemma 2, causal factorization](../science/adaptive_converse.md#lemma-2-causal-factorization). Load-bearing assumptions: [memory law](../science/model.md#memory-law) and [endpoint interface](../science/model.md#endpoint-interface).

<a id="m16"></a>
### M16. A consumable source genealogy

**Central question.** Which elementary successes supplied the quantum systems in one completed pair?

**Understanding target.** Track one immutable source label per edge through monotone interval joins. Explain why inputs are consumed, why one completed output cannot reuse another output's leaves, and why overlapping spatial intervals need not share physical registers or source labels.

**Dependencies and story role.** Uses [M03](#m03), [M06](#m06) and [M13](#m13). It identifies the classical source profile associated with each physical delivery.

**Conceptual connection.** The genealogy turns a complicated schedule into a fixed set of required source successes. Its uniqueness will make the later profile count valid even with unlimited buffering and pipelining.

**Source pointers.** Local project proof: [Lemma 3 and source genealogies](../science/adaptive_converse.md#source-genealogies-and-storage-exposure). Architectural restriction: [interval joins](../science/model.md#sources-buffers-and-control).

<a id="m17"></a>
### M17. Accumulated exposure and source-time variation

**Central question.** Why can completion be quick while the completed pair carries substantial memory noise?

**Understanding target.** Relate each ancestral qubit's storage time to its birth and local swap. Explain why their total exposure dominates the total variation of adjacent source birth times. Recognize that remote swaps and local buffer relabeling do not erase exposure already incurred.

**Dependencies and story role.** Combines the noise bookkeeping in [M04](#m04) and [M14](#m14) with the genealogy in [M16](#m16). It connects the physical storage process to a geometric constraint on source profiles.

**Conceptual connection.** The duration until the last success and the sum of interior storage exposures are different quantities. Ideal endpoint memories remove terminal exposure but do not remove the interior sum.

**Source pointers.** Canonical derivation: [storage exposure, Eqs. (15)–(17)](../science/adaptive_converse.md#source-genealogies-and-storage-exposure). Physical interpretation: [completion time versus exposure](../science/interpretation.md#accumulated-exposure-and-completion-time-are-different-resources). Prior ASAP identity: [GCT25](../references/RELATED_WORK.md#gct25).

<a id="m18"></a>
### M18. The separability threshold becomes an integer cutoff

**Central question.** Which source profiles can still deliver an entangled depolarizing output?

**Understanding target.** Explain the threshold $`v\gt1/3`$ for the two-qubit state family and its conversion to an exposure constraint. Identify why integer birth times give the exact cutoff $`a_\tau=\lceil\tau\ln3\rceil-1`$ on source-time variation even when actual control times and exposure are real.

**Dependencies and story role.** Uses [M02](#m02), [M04](#m04) and [M17](#m17). It turns a quantum condition into a finite set of admissible profile increments.

**Conceptual connection.** This threshold identifies which raw pairs can contribute entanglement; the later endpoint budget turns that condition into a bound allowing collective distillation. It is specific to this noise family and does not apply to every channel with the same attenuation time.

**Source pointers.** Canonical local derivation: [the entanglement threshold](../science/adaptive_converse.md#the-entanglement-threshold). Exact integer convention: [finite cutoff](../science/finite_bounds.md#1-exact-cutoff-and-synchronized-regime).

<a id="m19"></a>
### M19. Potential profiles bound adaptive selection

**Central question.** How can all adaptive schedules be bounded without assuming their selected waiting times are independent?

**Understanding target.** Distinguish the presampled Bernoulli field from the random profile selected by a policy. Explain the pointwise injection from entangled deliveries into low-variation successful potential profiles, the anchor-time factor and the signed integer-ball count $`K(n,a)`$. The constituent successes of each fixed potential tuple occur jointly with probability $`p^n`$; a specified first-success history also includes its preceding failures.

**Dependencies and story role.** Combines [M03](#m03), [M16](#m16) and [M18](#m18). This is the policy-independent classical mechanism of the converse.

**Conceptual connection.** Adaptive control chooses among available histories. Counting all admissible potential histories before taking expectations avoids assigning an unjustified iid law to the chosen history.

**Source pointers.** Local project proof: [counting potential successful profiles](../science/adaptive_converse.md#counting-potential-successful-profiles). Finite-horizon refinement: [anchor-span correction](../science/finite_bounds.md#appendix-a-finite-horizon-boundary-correction).

<a id="m20"></a>
### M20. The endpoint entanglement budget

**Central question.** Why can collective endpoint processing not extract an arbitrary rate from many separable arrivals?

**Understanding target.** Combine conditional tensor factorization with subadditivity to charge each arrival by its own $`E_F`$. Explain zero charge for a separable arrival, the one-ebit upper charge for a two-qubit arrival, and average monotonicity through selective endpoint operations. Identify why neither unconditional stream independence nor additivity is assumed.

**Dependencies and story role.** Uses [M07](#m07), [M09](#m09), [M15](#m15) and [M18](#m18). It connects the counted raw deliveries to a bound on the endpoint laboratories' whole quantum state.

**Conceptual connection.** Counting individually entangled raw pairs is sufficient here because the causal invariant prevents hidden inter-arrival quantum correlations from supplying an uncharged resource.

**Source pointers.** Local project amortization: [endpoint entanglement budget](../science/adaptive_converse.md#endpoint-entanglement-budget). Imported measure properties: [BDSW96](../references/RELATED_WORK.md#bdsw96) and [Vidal00](../references/RELATED_WORK.md#vidal00).

<a id="m21"></a>
### M21. A budget bound becomes a target bound

**Central question.** How does an entanglement budget constrain a nearly perfect fixed-size output?

**Understanding target.** Connect target overlap, isotropic twirling and conditional entropy to the finite-error lower bound on the target's $`E_F`$. Explain why ancillary dimensions do not enter and why a reported success branch must be charged by its probability.

**Dependencies and story role.** Combines [M08](#m08), [M10](#m10), [M12](#m12) and [M20](#m20). It turns an abstract monotone budget into the operational output criterion.

**Conceptual connection.** An upper bound on a resource measure becomes a rate converse only after the demanded output is shown to require that resource, with its error and branch probabilities included.

**Source pointers.** Canonical project conversion: [vanishing-error ebits and the success-probability bound](../science/adaptive_converse.md#from-entanglement-budget-to-vanishing-error-ebits). Anchor entropy and distance foundations: [Wilde §9.1.5 and §11.7](SOURCE_BRIDGE.md#section-map). Primary twirling dependency: [Horodecki99](../references/RELATED_WORK.md#horodecki99).

<a id="m22"></a>
### M22. The finite adaptive converse and exact synchronized regime

**Central question.** How do the source count and endpoint budget become a theorem about the best permitted rate?

**Understanding target.** Assemble the profile bound, one-edge source budget and target conversion into the finite converse. Compare it with synchronized generation and explain the exact equality for $`0\lt\tau\le1/\ln3`$. Distinguish a universal upper bound from a construction that supplies a lower bound.

**Dependencies and story role.** Integrates [M13](#m13), [M19](#m19) and [M21](#m21). It completes the first global result of Phase II.

**Conceptual connection.** The upper bound covers the entire permitted policy class, while the lower bound needs only one explicit protocol. Agreement in the short-lifetime regime establishes optimality there without solving every scheduling problem.

**Source pointers.** Canonical statement: [finite converse and consequences](../science/adaptive_converse.md#finite-converse-and-consequences). Lower construction: [synchronized generation](../science/achievability.md#synchronized-generation). Exact equality: [finite synchronized regime](../science/finite_bounds.md#1-exact-cutoff-and-synchronized-regime).

<a id="m23"></a>
### M23. Charging the amount of entanglement

**Central question.** What is lost by assigning a full ebit to every entangled raw pair?

**Understanding target.** Explain the entanglement-weighted shell count and why pairs near the separability threshold contribute little to $`E_F`$. Interpret the finite-chain example as an interval containing the optimal rate, rather than an estimate of the optimum or an output distribution.

**Dependencies and story role.** Refines [M09](#m09), [M18](#m18)–[M20](#m20) and [M22](#m22). It makes the global converse quantitatively useful before taking a large-chain limit.

**Conceptual connection.** A continuous quantum resource weight can sharpen a combinatorial count that previously used only a binary entangled-or-separable distinction.

**Source pointers.** Local weighted envelope: [finite bounds, §2](../science/finite_bounds.md#2-an-entanglement-weighted-envelope) and [the finite example](../science/finite_bounds.md#3-a-finite-example). Primary exact two-qubit ingredient: [Wootters98](../references/RELATED_WORK.md#wootters98).

<a id="m24"></a>
### M24. Profile entropy and the exact sublinear exponent

**Central question.** Can the number of available low-variation histories compensate for the probability of their required successes?

**Understanding target.** Relate the logarithm of the profile count to its allowed variation per edge. Explain why, at fixed $`p`$, a sublinear lifetime gives only subexponential profile multiplicity and therefore leaves the leading rate exponent equal to $`\ln(1/p)`$. Distinguish this exponent statement from the absence of polynomial or other subexponential scheduling gains.

**Dependencies and story role.** Combines [M12](#m12), [M19](#m19) and [M22](#m22). It converts the finite envelope into the principal scaling law.

**Conceptual connection.** The competition is between the multiplicity of admissible histories and the independent-success factor. The exact exponent follows when the multiplicity is too small to change the leading exponential cost.

**Source pointers.** Local asymptotic proof: [sublinear-lifetime exponent](../science/adaptive_converse.md#synchronized-generation-and-the-sublinear-lifetime-exponent). Sharper local counting analysis: [entropy of the profile count](../science/finite_bounds.md#4-entropy-of-the-profile-count). Meaning of the remaining improvements: [what scheduling can still improve](../science/interpretation.md#what-scheduling-can-still-improve).

<a id="m25"></a>
### M25. Small linear lifetime coefficients

**Central question.** Does a lifetime proportional to chain length immediately remove exponential suppression?

**Understanding target.** Interpret the profile entropy function $`f`$ and the condition $`f(\kappa\ln3)\lt\ln(1/p)`$ for a negative rate exponent at $`\tau_n\sim\kappa n`$. Explain the meaning of the sufficient converse coefficient $`\kappa_{\mathrm{count}}`$ and why it is not an identified optimal transition.

**Dependencies and story role.** Develops [M18](#m18) and [M24](#m24) at the linear scale. It supplies the upper-bound side of the eventual comparison with an achievable coefficient.

**Conceptual connection.** Establishing the required order of a resource and determining its exact critical coefficient are different achievements. The entropy envelope gives quantitative information without solving the whole linear regime.

**Source pointers.** Local derivations: [profile entropy](../science/finite_bounds.md#4-entropy-of-the-profile-count) and [exponential suppression for small linear coefficients](../science/finite_bounds.md#5-exponential-suppression-for-small-linear-coefficients).

<a id="m26"></a>
### M26. What an ASAP/reset factory produces

**Central question.** What timing and state quality result from first-success acquisition and immediate local swaps?

**Understanding target.** Explain the feasibility of the local swap schedule, the logarithmic mean completion time and the linear mean accumulated exposure. Distinguish the average visibility from visibility evaluated at average exposure. Recognize that a cycle's duration and state quality can be correlated even though different reset cycles are iid.

**Dependencies and story role.** Uses [M03](#m03), [M04](#m04), [M06](#m06), [M13](#m13) and [M17](#m17). It begins the constructive side with a concrete allowed protocol.

**Conceptual connection.** The inherited ASAP factory exposes the resource that the converse detects: quick completion can coexist with extensive memory exposure. Its state and timing statistics are inputs to a separate rate argument.

**Source pointers.** Canonical construction: [ASAP/reset protocol](../science/achievability.md#the-asapreset-protocol) and [averaging the raw state](../science/achievability.md#averaging-the-raw-state). Inherited repeater analysis: [GCT25](../references/RELATED_WORK.md#gct25).

<a id="m27"></a>
### M27. Converting reset cycles into a fixed-deadline rate

**Central question.** When can a yield per raw pair be divided by mean cycle duration?

**Understanding target.** Explain the deterministic cycle count, infinite-run reference and charged missed-deadline event used by the timing lemma. Identify the error in declaring pairs iid merely because they completed before a random stopping boundary. Keep the coding limit at fixed chain length explicit.

**Dependencies and story role.** Combines [M10](#m10)–[M12](#m12) with the correlated cycle output in [M26](#m26). It makes the construction satisfy the same operational definition used by the converse.

**Conceptual connection.** Classical timing and quantum quality cannot be separated by uncharged selection. The reference experiment supplies the iid inputs required by a distillation code while deadline failures remain in the error budget.

**Source pointers.** Local project lemma: [from reset cycles to deterministic-horizon rates](../science/achievability.md#from-reset-cycles-to-deterministic-horizon-rates). Rate criterion: [observed histories and operational rate](../science/model.md#observed-histories-and-operational-rate).

<a id="m28"></a>
### M28. A sufficient linear lifetime for distillation

**Central question.** How much lifetime suffices for a positive constant distillation yield per reset cycle?

**Understanding target.** Connect the Jensen visibility bound at $`\tau=\kappa n`$ to a common entangled Werner input when $`\kappa\gt\mu_p/\ln3`$. Explain how finitely many endpoint recurrence rounds followed by hashing give a constant positive yield after all acceptance costs. Combine this with [M27](#m27) to obtain the inverse-logarithmic achievable rate.

**Dependencies and story role.** Integrates [M11](#m11) and [M25](#m25)–[M27](#m27). It supplies the constructive half of the linear-lifetime comparison.

**Conceptual connection.** The needed purification occurs at the ideal endpoints, within the model. The sufficient coefficient differs from the converse coefficient, and the achievable throughput is not asserted to be optimal.

**Source pointers.** Canonical construction and cost accounting: [two-way LOCC coefficient](../science/achievability.md#a-sufficient-linear-lifetime-coefficient-using-two-way-locc). Coefficient comparison: [finite bounds, §5](../science/finite_bounds.md#5-exponential-suppression-for-small-linear-coefficients). Imported recurrence and hashing: [BDSW96](../references/RELATED_WORK.md#bdsw96).

<a id="m29"></a>
### M29. The noise channel changes the rate exponent

**Central question.** Why can memories with the same coherence attenuation have different asymptotic entanglement rates?

**Understanding target.** Compare the Bell spectra of depolarizing and pure phase outputs at the same visibility. Explain why phase outputs have positive hashing yield at every positive visibility and why every diverging phase lifetime permits a zero leading chain-length exponent. Contrast this with the depolarizing result for sublinear lifetimes without interpreting a small achievable rate as a practical finite-block guarantee.

**Dependencies and story role.** Combines [M04](#m04), [M08](#m08), [M11](#m11), [M24](#m24), [M26](#m26) and [M27](#m27). It exposes the decisive role of the quantum noise family after both converse and construction are understood.

**Conceptual connection.** A scalar lifetime does not specify the Bell spectrum or its separability threshold. The operational consequence depends on the channel and the collective processing allowed at the endpoints.

**Source pointers.** Canonical local comparison: [phase coherence and its achievable rate](../science/noise_comparison.md#phase-coherence-remains-distillable-at-every-positive-visibility). Anchor channel foundations: [Wilde §§4.7.2–4.7.4](SOURCE_BRIDGE.md#section-map). Imported hashing ingredient: [BDSW96](../references/RELATED_WORK.md#bdsw96).

<a id="m30"></a>
### M30. The complete contribution and its limits

**Central question.** What has the project resolved, and which changes of resources or regimes require a different conclusion?

**Understanding target.** Connect the architecture, causal invariant, genealogy, profile envelope and endpoint budget into one account of the result. Distinguish inherited ASAP and entanglement ingredients from the adaptive converse. Explain the allowed finite and subexponential gains, the unresolved linear-coefficient interval, buffering versus generation multiplexing, and the consequences of changing intermediate quantum operations, endpoint quantum feedback or noise correlations.

**Dependencies and story role.** Integrates [M13](#m13), [M22](#m22)–[M25](#m25) and [M28](#m28)–[M29](#m29). This is the global synthesis of Phase II and of the map.

**Conceptual connection.** The result is an architecture theorem with a precisely charged source clock. Its physical meaning depends on fixed generation probability and bandwidth, the memory channel and the permitted quantum interface; it is not a capacity theorem for every repeater architecture.

**Source pointers.** Canonical synthesis: [interpretation](../science/interpretation.md), especially [bandwidth](../science/interpretation.md#buffer-capacity-and-source-bandwidth), [the unresolved coefficient boundary](../science/interpretation.md#a-linear-lifetime-is-an-order-threshold-not-a-solved-phase-boundary) and [physical units and scope](../science/interpretation.md#physical-units-and-model-boundary). Attribution: [what the comparison establishes](../references/RELATED_WORK.md#what-the-comparison-establishes). Authoritative assumptions: [model](../science/model.md).

## Continuing through the scientific sources

The [source bridge](SOURCE_BRIDGE.md) connects the single anchor to these project-specific targets. The [scientific reading map](../science/README.md) gives direct routes to the canonical proofs, and the [repository overview](../README.md) places the result and its supporting artifacts in context.
