# Affinari

Any system that has state, makes decisions, and acts in an 
environment faces the same fundamental problem: how does it know 
what to do?

Affinari answers that question with a single mechanism applicable 
to any domain. Encode what matters as a weighted trait schema. 
Measure the distance between current state and target coherence. 
Act to reduce that distance. Repeat.

That mechanism runs boids. It runs forest fire simulations. It runs game AI. 
It navigates boats. It governs agentic AI. It matches hotel 
preferences. It validates inference. It models how biological 
intelligence constructs behaviour.

The domain changes. The mechanism never does.

---

## The Mechanism

Every domain has structure. Structure can be encoded as traits. 
Traits can be weighted. Weighted traits define a target 
configuration — a schema of what coherence looks like in this 
domain.

Given a current state and a target schema, the distance between 
them is calculable. Given a calculable distance, behaviour that 
reduces it is derivable. Given behaviour that reduces distance, 
coherence emerges.

That is Affinari. No more is required.

The scoring kernel:
```
coherence = 1 − (Σ wᵢ · |state_i − target_i|) / Σ wᵢ
```

Weighted Manhattan distance in normalised trait space. 
Transparent. Deterministic. Auditable. Explainable. Runnable 
on commodity hardware without external dependency.

Missing values are ignored, not zeroed. Absence of information 
is architecturally distinct from a value of zero.

---

## The OMCA Loop

Coherence-seeking behaviour operates as a continuous cycle:
```
OBSERVE   → Read current state as a trait vector
MODULATE  → Adjust weights and context
CALCULATE → Compute coherence with target schema
ACTUATE   → Act to reduce distance from target
              ↓
           REPEAT
```

This loop is the complete operational expression of Affinari. 
It requires no external services, no training data, no cloud 
infrastructure. It requires a trait space, a schema, and a 
kernel.

---

## What It Runs

**Boids**
Each agent observes the position and velocity traits of its 
neighbours. The schema defines what a coherent flock looks like. 
The kernel calculates distance. The agent actuates to reduce it. 
Emergent flocking behaviour arises from local coherence-seeking 
with no central controller and no global plan.

**Forest fire**
Each cell observes fuel and dryness traits. Burn and grow 
profiles define target configurations. The kernel calculates 
affinity. Cells transition state accordingly. The result is 
self-organised coherence — not criticality and collapse but 
stable dynamic behaviour emerging from local trait interactions.

**Game AI and navigation**
Agents observe environment state as a trait vector. Goal profiles 
define target configurations. The kernel calculates coherence. 
Agents navigate, decide, and adapt. Schemas self-modify through 
outcome feedback — weights adjust based on what worked. This is 
not training. It is continuous coherence-seeking with memory.

**Robotics**
Sensor state observed as traits. Target behaviour encoded as 
schema. Kernel calculates coherence. Actuators reduce distance. 
The same loop that flocks birds navigates physical systems in 
the real world.

**Preference matching (Matteo)**
Client preference encoded as a weighted trait vector. Available 
services encoded against the same schema. Kernel ranks by 
coherence. The result is transparent, explainable matching 
with per-trait gap analysis. No black box. No behavioural 
surveillance. No correlation mining. Declared preference 
matched against structured offering.

**Inference governance (GatedClaw)**
Proposed agent action observed as a trait vector. Authority 
schema defines what is permitted. Fit'd calculates coherence. 
Verdict produced with full alignment report. The intelligence 
that governs the agent is in the schema. The agent cannot 
manipulate it because it operates outside the agent entirely.

These are not different products. They are one mechanism 
applied to different schemas.

---

## The Doppelganger Layer

Where signal is thin — a new client, a novel situation, an 
under-specified state vector — the doppelganger layer infers 
from aligned patterns in the network.

Entities whose known trait dimensions align with the current 
entity contribute their encoded patterns to fill the gaps. Not 
their records. Not their identity. Only their abstract 
structural encoding.

This mirrors how biological intelligence handles novelty. The 
brain does not start from scratch with unfamiliar situations. 
It borrows from similar past experiences, constructs a 
prediction, and adjusts based on outcome. Lisa Feldman Barrett's 
theory of constructed cognition demonstrates that behaviour 
itself emerges from this continuous coherence-seeking against 
accumulated pattern — emotion, perception, and action are all 
constructions built from prior experience meeting current state.

The doppelganger layer is a formal implementation of that 
process. The inference crosses the network. The data does not.

This capability has profound implications beyond preference 
matching. An expanding, evolving human trait schema built on 
declared preference could model individual human behaviour at 
a level that makes Cambridge Analytica look primitive. Affinari 
is built on declared preference and schema governance precisely 
because this implication was understood from the beginning. 
The ethical architecture is not a feature added to a capable 
system. It is the foundation the system was built on.

---

## On Language and Intelligence

Language is how intelligence is communicated between humans. 
It is the interface, not the thing itself.

Large language models are extraordinarily capable synthesisers 
of human language. They produce fluent, plausible, contextually 
appropriate text at scale. This is genuinely useful. It is not 
intelligence. Fluency is not reasoning. Plausibility is not 
correctness. The synthesis of language patterns is not the 
expression of structured intelligence.

When Affinari interfaces with human language — in Matteo, in 
GatedClaw, in any application where natural language is the 
input or output — an LLM acts as the translator between human 
expression and the structured intelligence of the Affinari 
kernel. This is exactly the role language plays in human 
communication. We use language to share intelligence. We do 
not mistake a fluent speaker for a wise one.

The LLM translates. The schema reasons. The kernel decides. 
These are different functions and must remain architecturally 
separate for the system to be trustworthy.

Fit'd is the mechanism that enforces that separation.

---

## Fit'd

Fit'd applies a schema to any inference output to check whether 
it is producing aligned results, stating where it fits and 
where it doesn't.

It operates at both ends of any language interface:

**Input gate** — validates that what enters the inference 
engine conforms to the schema. Prompt injection, malicious 
instructions, and out-of-scope inputs are caught before 
inference runs. The intelligence is not accessible to 
manipulation through the language interface.

**Output gate** — validates that what the inference engine 
proposes conforms to the schema before actuation. Misaligned 
outputs, unauthorised actions, and policy violations are 
caught before they have real world consequence.

Every Fit'd decision produces a timestamped alignment report:

- Alignment score
- Schema criteria satisfied
- Schema criteria violated  
- Items requiring human review
- Plain English summary

Not a filter. Not a blocklist. An alignment report with full 
audit trail. Human-readable. Regulator-ready. Reproducible.

The first published implementation of Fit'd applied to agentic 
AI governance is GatedClaw, published 25th March 2026.
→ github.com/Andrew-T-Fielden/gatedclaw

---

## Self-Modification

Schemas are not static. Weights adjust based on outcomes. 
Trait definitions refine as the domain is better understood. 
New traits emerge from gap analysis — when Fit'd encounters 
inputs or outputs that don't map to existing schema dimensions, 
that is information about what the schema is missing.

This is not training in the machine learning sense. No gradient 
descent. No loss function. No opaque weight updates. It is 
explicit, inspectable schema evolution — human-gated by default 
because every schema change is a named decision with a timestamp 
and a reason.

The system that identifies its own gaps and proposes 
improvements, which a human reviews and approves before they 
take effect, is auditable in a way that a self-training model 
can never be.

---

## Sovereign Deployment

The complete stack runs without external dependency. OMCA 
kernel, Fit'd validation, schema library, bundle matching — 
all on commodity hardware. Local inference for language 
interface where required (Mistral 7B, Llama 3, and equivalents 
on Apple M-series and equivalent). No cloud call required on 
the critical path. No data leaves the deployment environment.

This is not a compliance feature. It is a property of the 
architecture.

---

## The Standards Body

Schemas for each domain are governed by an open standards body 
with participation from domain practitioners — tourist boards, 
hotel groups, financial services compliance functions, 
healthcare administrators, legal practitioners. The schema is 
the contract between domain knowledge and the kernel. The 
standards body ensures that contract reflects genuine expertise 
rather than technical convenience.

Private bespoke schemas coexist with open standards within the 
same architecture. An organisation with specific requirements 
that cannot be publicly standardised uses the same kernel 
against their own schema.

---

## Architecture
```
Affinari Holdings
│
├── Protocol layer    OMCA loop definition
│                     Schema standard · Bundle format
│                     Scoring specification
│                     Fit'd validation specification
│                     Open, versioned, governed by 
│                     Affinari Holdings
│
├── Fit'd layer       Input gate · Output gate
│                     Alignment reporting · Audit trail
│                     Model-agnostic · Origin-agnostic
│
├── Exchange layer    Bundle marketplace
│                     Quality certification
│                     Schema library · API access
│
└── Application layer Matteo — concierge intelligence
                      GatedClaw — agentic AI governance
                      Navigation · Robotics · Game AI
                      Boids · Forest fire · Simulation
                      Any coherence-seeking domain
```

---

## IP and Prior Art

- `affinari_defensive_disclosure.md` — formal prior art summary
- `Affinari_SDK_License_v1.txt` — commercial SDK licence
- `LICENSE.md` — repository licence

OMCA loop, Fit'd validation mechanism, bundle format, scoring 
specification, doppelganger architecture, and exchange model 
published 2025.

GatedClaw — first reference implementation of Fit'd applied 
to agentic AI governance — published 25th March 2026.

All materials © 2025-2026 Andrew T. Fielden. 
All rights reserved.

---

## Repositories

| Repository | Description |
|---|---|
| [`affinari`](https://github.com/Andrew-T-Fielden/affinari) | Protocol · IP · defensive disclosure · SDK licence |
| [`affinari_lite`](https://github.com/Andrew-T-Fielden/affinari_lite) | Browser reference implementation · offline · live |
| [`gatedclaw`](https://github.com/Andrew-T-Fielden/gatedclaw) | Fit'd governance for agentic AI · tested against OpenClaw |

---

## Status

Protocol specification: **published**
OMCA reference implementations: **boids · forest fire · 
navigation · live**
Affinari Lite: **live**
Fit'd validation: **published**
GatedClaw: **working, public** — 25 March 2026
Matteo (concierge): **working, private**
Local inference validation: **complete**
Exchange architecture: **specified, pre-launch**
First domain deployment: **in progress — Rhodes, Greece**

---

## Contact

**Andrew T. Fielden**
Affinari Holdings
[flatpackforces@gmail.com](mailto:flatpackforces@gmail.com)
[github.com/Andrew-T-Fielden](https://github.com/Andrew-T-Fielden)

