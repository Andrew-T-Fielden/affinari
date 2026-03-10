# Affinari

**Affinari is a preference intelligence protocol.**

It provides the schema standard, scoring kernel, and exchange architecture for aligning people with options — across any domain where preference matters.

The first application is **Matteo**, a concierge intelligence tool for private client services. The protocol is domain-agnostic. The same kernel that scores a Mallorca hotel recommendation scores a navigation route, a financial product, or a game AI decision. The domain is defined by the bundle. The kernel doesn't change.

---

## What it does

Affinari encodes individual preference as a vector of weighted traits — not a demographic segment, not a behavioural cluster, not a star rating. A preference vector describes *how a specific person relates to a specific domain at a specific moment*. It is held separately per domain, because the same person can want a restorative hotel and a stimulating dining experience. Systems that type people as a single profile miss this. Affinari holds the distinction.

Scoring runs on weighted Manhattan distance — transparent, auditable, fast, and runnable on commodity hardware without any cloud dependency.

The **doppelganger layer** addresses the cold start problem without pooling client data. Where signal is thin for a new client, the system borrows from the encoded preference signals of clients whose *known* dimensions align — not their records, not their identity, only their abstract preference encoding. The inference crosses the network. The data does not.

---

## Architecture

```
Affinari Holdings
│
├── Protocol layer       Schema standard · Bundle format · Scoring specification
│                        Open, versioned, governed by Affinari Holdings
│
├── Exchange layer       Bundle marketplace · Quality certification · API access
│                        Operators publish, discover, and subscribe to domain bundles
│                        Revenue: listing fees · certification · access tiers
│
└── Application layer    Matteo (concierge intelligence) · first reference implementation
                         Same kernel available for: private banking · travel · retail ·
                         navigation · game AI · financial products · any preference domain
```

---

## The kernel

The scoring kernel takes three inputs and returns a ranked list:

- A **bundle** — schema defining the trait space for a domain, plus items encoded against it
- A **preference vector** — a client's weighted orientation across those traits
- Optional **filters** — required tags, excluded tags, categorical constraints

It returns items ranked by alignment score, with per-trait gap analysis and concierge notes surfaced at the right moment.

The kernel is deterministic. Every result is explainable. There is no black box.

**Scoring:**
```
alignment = 1 − (Σ wᵢ · |preference_i − item_i|) / Σ wᵢ
```

Missing scalars are ignored, not zeroed. Null means no preference stated — architecturally distinct from a preference of zero.

---

## The bundle format

Every domain is described by a single bundle file:

```json
{
  "bundle_version": "1.0.0",
  "schema": {
    "id": "domain_name_v1",
    "name": "Domain Name",
    "engine": {
      "scoring": {
        "method": "manhattan",
        "missing_scalar": "ignore"
      }
    },
    "traits": {
      "scalars": [
        { "id": "trait_id", "name": "Trait Name", "weight": 1.0 }
      ],
      "tags": [
        { "id": "tag_id", "name": "Tag Name" }
      ],
      "categoricals": [
        { "id": "cat_id", "name": "Category", "options": [] }
      ]
    }
  },
  "items": {
    "domain_schema_id": "domain_name_v1",
    "items": []
  }
}
```

Bundles are self-contained, portable, and publishable to the Affinari exchange. Any operator can create a bundle for their domain. The schema standard is the contract between bundle authors and the kernel.

---

## Repositories

| Repository | Description |
|---|---|
| [`affinari`](https://github.com/Andrew-T-Fielden/affinari) | Protocol specification · IP · defensive disclosure · SDK licence |
| [`affinari_lite`](https://github.com/Andrew-T-Fielden/affinari_lite) | Browser-based reference implementation · runs offline · any bundle · live at [affinari_lite](https://andrew-t-fielden.github.io/affinari_lite/) |

The Matteo concierge implementation — TypeScript kernel, Express server, six client profiles, four Mallorca domain bundles, local LLM inference — is the current private reference implementation and is available under a separate commercial licence.

---

## Sovereign deployment

The extraction layer — natural language brief to preference vector — runs on local inference models (Mistral 7B, Llama 3, and equivalents) on commodity hardware including the Apple M-series Mac Mini. No external API call is required on the critical path. Client preference data never leaves the institution's infrastructure.

This is not a compliance feature added to an existing architecture. It is a property of how the system is built. The kernel, the bundles, the client profiles, and the extraction layer can all run air-gapped.

As local inference hardware and models improve, the capability improves automatically. The sovereignty argument strengthens over time without any architectural change.

---

## Differentiation from CRM and clienteling

**CRM** records what happened. It is a transaction log with workflow on top. When the relationship manager leaves, the record stays but the understanding goes with them.

**Clienteling** adds behavioural triggers to CRM — surface the right client at the right moment with the right history. It still works from what the client *did*, not what the client *is*.

**Affinari** encodes underlying preference orientation, not behaviour. Behaviour is noisy — a client books the same hotel every year not because it is their ideal but because they trust it. A preference-based system can see what behaviour cannot reveal.

Three distinctions that are architectural, not positional:

1. **Encoded preference vs recorded behaviour.** The vector describes orientation. Behaviour only partially reveals it.
2. **Cross-domain independence.** The same person holds different preference orientations in different contexts. Affinari holds them separately. No existing CRM or clienteling system does.
3. **Privacy-preserving network effect.** The doppelganger layer enriches individual profiles from network signals without any client record leaving the institution. The inference crosses the network. The data does not.

Affinari does not replace CRM. It is the intelligence layer that makes CRM data useful in the moment of recommendation rather than only in the moment of review.

---

## IP and prior art

This repository contains timestamped documentation establishing the originality of the Affinari system.

- `affinari_defensive_disclosure.md` — formal prior art summary
- `Affinari_SDK_License_v1.txt` — commercial SDK licence terms
- `LICENSE.md` — repository licence

The bundle format, scoring specification, doppelganger architecture, and exchange model were published here and in `affinari_lite` in 2025, prior to any commercial deployment.

All materials © 2025 Andrew T. Fielden. All rights reserved.

---

## Status

Protocol specification: **published**  
Reference implementation (Lite): **live** — [andrew-t-fielden.github.io/affinari_lite](https://andrew-t-fielden.github.io/affinari_lite/)  
Concierge application (Matteo): **working implementation, private**  
Local inference validation: **complete** — Mistral 7B on Apple M4  
Exchange architecture: **specified, pre-launch**  
First domain deployment: **in progress**

---

## Contact

For founding partner discussions, domain licence enquiries, or exchange participation:

**Andrew T. Fielden**  
[flatpackforces@gmail.com](mailto:flatpackforces@gmail.com)  
[github.com/Andrew-T-Fielden](https://github.com/Andrew-T-Fielden)
