# Affinari Preference Passport

## A Proposed OAuth 2.0 Extension for Portable Personal Preference Data

**Status:** Concept specification — prior art disclosure  
**Author:** Andrew T. Fielden  
**Date:** March 2026  
**Repository:** [github.com/Andrew-T-Fielden/affinari](https://github.com/Andrew-T-Fielden/affinari)

---

## Overview

The Affinari Preference Passport is a proposed extension to the OAuth 2.0 authorisation framework that enables individuals to hold, control, and share their encoded preference data across institutional and application boundaries — with explicit, scoped, revocable consent.

Where OAuth 2.0 standardised portable identity and permission delegation, and OpenID Connect extended it with a portable identity layer, the Preference Passport extends it with a portable preference layer.

The analogy is precise. A user who has established a preference profile with one Affinari-compliant service should be able to share specific preference scopes with another Affinari-compliant service, under their own control, without either institution holding or transferring the underlying data.

---

## The Problem

Preference data is currently held by institutions, not individuals.

A private banking client's preference profile — their orientation toward restorative versus stimulating experiences, their relationship with luxury, their response to local versus international flavour — is encoded implicitly in the institution's CRM as transaction history and relationship manager notes. The client cannot access it, cannot correct it, cannot share it, and loses it entirely when they change institutions.

A concierge service member's preference profile exists in their Lifestyle Manager's head and in accumulated service history. When the Lifestyle Manager leaves, the profile is lost. When the member changes services, the profile starts from zero.

The Preference Passport inverts this. The individual holds the preference token. Institutions request access to specific preference scopes. The individual grants, limits, and revokes access. The preference data follows the person, not the institution.

---

## OAuth 2.0 Extension Model

The Preference Passport follows the same extension pattern as OpenID Connect — a specific scope definition, a specific token type, and a specific claims structure, built on standard OAuth 2.0 infrastructure.

Institutions already using OAuth 2.0 for authentication can implement the Preference Passport extension without replacing existing identity infrastructure. The preference token travels alongside the identity token. Same consent flow, additional scope, additional claims.

### Preference Scopes

Preference scopes follow the domain structure of the Affinari bundle schema. A scope grants access to preference data within a specific domain.

```
affinari:preferences:gifts
affinari:preferences:travel
affinari:preferences:dining
affinari:preferences:accommodation
affinari:preferences:experiences
```

Scopes are additive. A token granting `affinari:preferences:gifts` does not grant access to `affinari:preferences:travel`. The individual controls each domain independently.

### Preference Token Structure

A preference token carries the encoded preference vector for the granted scope, not the underlying personal data that generated it.

```json
{
  "sub": "[subject identifier]",
  "iss": "[issuing Affinari exchange node]",
  "aud": "[requesting institution]",
  "scope": "affinari:preferences:gifts",
  "exp": "[expiry timestamp]",
  "affinari_vector": {
    "schema_id": "gifts_v1",
    "traits": {
      "understated": 0.8,
      "experiential": 0.7,
      "luxury": 0.6,
      "local_flavour": 0.9,
      "floral": 0.4
    },
    "confidence": 0.75,
    "last_updated": "[timestamp]"
  }
}
```

The token carries the vector, not the history. The institution receives what they need to make preference-aligned recommendations. They do not receive the source data, the transaction history, or any information about how the vector was derived.

---

## Consent Architecture

### Individual Control

The individual holds a Preference Passport account — either directly with Affinari Holdings or through a participating institution acting as an identity provider.

From their Preference Passport, they can:

- View their current preference vectors by domain
- See which institutions have active access to which scopes
- Set expiry periods for each grant
- Revoke access to any scope at any time
- Export their complete preference profile
- Delete their profile entirely

### Institutional Request Flow

A participating institution requests a preference scope during or after the standard OAuth authentication flow. The individual receives a consent prompt specifying which institution is requesting access, which scope, and for what duration. They approve or decline. Approval issues a scoped preference token to the requesting institution. The token expires automatically unless renewed with continued consent.

### Temporary Inference Vectors

Where a preference vector is inferred rather than verified — for example, a gift being sent to a third party whose preferences are described by the sender rather than directly captured — the token is marked as inferred and carries a reduced confidence score. Inferred vectors are never stored as verified preference data without explicit consent from the subject.

```json
{
  "affinari_vector": {
    "confidence": 0.35,
    "source": "inferred",
    "inferred_by": "[sender subject identifier — hashed]",
    "expires": "[session expiry — not persisted]"
  }
}
```

Inferred vectors expire at session end unless the subject explicitly converts them to a verified profile through their own consent flow.

---

## The Gift Receiver Flow

A natural entry point for the Preference Passport is the gift receipt scenario.

1. A Coutts client asks their relationship manager to send a gift to a third party — Kathy — whose preferences are not in the Coutts system.
2. The relationship manager captures what the client knows about Kathy as a natural language brief. The Affinari extraction layer converts this to a low-confidence inferred vector for this session only.
3. The gift is selected, scored against the inferred vector, and sent.
4. Accompanying the gift is a card containing a Preference Passport invitation — not a marketing message, but a personal invitation: *"This gift was chosen carefully. If you'd like future gifts to be even better chosen, we'd love to know a little more about what you enjoy."*
5. Kathy follows the link, answers a short preference capture flow, and establishes a Preference Passport with her own verified vectors.
6. Her verified profile replaces the inferred vector for future gifts. She controls what she shares and with whom.

This flow simultaneously:
- Solves the third-party preference problem without GDPR exposure
- Creates a natural, value-driven onboarding path for new Preference Passport holders
- Grows the preference network through gift relationships rather than direct marketing
- Maintains consent and individual control throughout

---

## Privacy and GDPR Compliance

The Preference Passport is designed to be GDPR compliant by architecture, not by policy.

**Data minimisation:** Institutions receive encoded preference vectors, not personal data. The vector carries what is needed for preference alignment and nothing else.

**Purpose limitation:** Scopes are domain-specific. A gift preference scope cannot be used for travel recommendations without separate consent.

**Individual rights:** The individual can access, correct, export, and delete their preference data at any time. These rights are structural, not procedural.

**Consent:** Every grant is explicit, scoped, and time-limited. Inferred vectors are never persisted without the subject's own consent.

**Data residency:** The preference vector, like the Affinari kernel itself, can be computed and held on-premises. The token infrastructure does not require cloud dependency. Sovereign deployment is architecturally supported.

---

## Relationship to Affinari Holdings

The Preference Passport is a protocol extension governed by Affinari Holdings as part of the Affinari standard. It is not a product offered by any specific application or licensee.

Participating institutions implement the Preference Passport extension under their Affinari licence. The governance of the scope definitions, token format, and consent requirements sits with Affinari Holdings, ensuring interoperability across the exchange.

An individual's Preference Passport is portable across all Affinari-compliant services. Switching institutions does not mean starting over.

---

## Prior Art Statement

This concept was developed by Andrew T. Fielden as a natural extension of the Affinari preference intelligence protocol, first published in this repository in 2025. The OAuth extension model, the domain-scoped preference token structure, the inferred versus verified vector distinction, the gift receiver onboarding flow, and the governance model described in this document are original contributions to the prior art record as of the date of this document.

---

## Status and Next Steps

This document is a concept specification and prior art disclosure. It is not a complete technical specification. The following remain to be defined:

- Full token schema and validation rules
- Exchange node discovery and federation model
- Scope namespace governance process
- Reference implementation
- Formal IETF draft (if pursued as an open standard)

Enquiries regarding participation, implementation, or licensing: [flatpackforces@gmail.com](mailto:flatpackforces@gmail.com)

---

*© 2026 Andrew T. Fielden. All rights reserved.*
