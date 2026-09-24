# Classification is the edge. Orientation is the floor.

*A position statement, Andrew Fielden, Affinari Holdings — 24 September 2026.*

*Written in response to the "System One Models" / Jev launch of September 2026, which supplied a vocabulary that makes this distinction legible. I do not claim to be the only person who has seen it. I claim to have been building on it, and I am putting it plainly on record here, dated, alongside code that already embodies it.*

---

## What I agree with

A general-purpose language model is a word-guesser: it predicts the next token, one at a time, and that shape is genuinely wrong for the job of making a fast, structured, trustworthy decision inside software. Putting a purpose-built reader at the edge — one that takes unstructured state in and returns typed, calibrated values out, in parallel, cheaply — is the right move. Jev does that well, and the people building routers, gates and rerankers on top of it are right that a fast typed classifier is a better primitive for those jobs than a chat model wrapped in string-parsing.

So the classification layer is real, and it is shared ground. My own long-standing test for whether a thing belongs in a category — does it read like a duck across the traits that matter — *is* classification. A fast typed classifier does the same work. I concede this cleanly, because everything that follows depends on being honest about it.

## Where it stops

A classifier answers one question at a time. Ask it three questions about the same input and you get three independent answers — three marginal distributions, each with its own confidence, computed side by side. Nothing in that output relates any one answer to any other. The classifier does not know that "frustrated" *and* "urgent" *and* "technical" mean anything as a combination, because it never forms the combination.

A bag of independent marginals is not a decision. It is not even a position. Reading the traits is the setup. The work — the part that turns reads into behaviour — is composing those marginals into a single joint and orienting that joint against a target: not "which bucket is this," but "how far, and in which direction, from where it should be." That is the operation nobody in the current ecosystem is performing. The public projects forming around System One models so far are, almost without exception, edge tooling: routers, gates, filters, rerankers, classifiers. Every one reads. None composes. None orients. The floor is real, and on the present evidence it is largely unoccupied.

## Actuation does not run through the model — deliberately

The demonstrations that impress people — an agent driving, dodging, acting many times a second — are not the model actuating. The model classifies; a deterministic harness around it acts. The intelligence that *moves* is the loop, not the reader. This is worth saying plainly because the credit is routinely misassigned: the applause is for the actuation, and it is handed to the classifier.

Affinari's actuation does not close through a model call. It closes through geometry — a coherence measure over the joint, evaluated in-process, with no inference in the loop. This is not a performance optimisation over the model-in-the-loop approach; it is a different account of what actuation is. Theirs: actuation is a fast classifier's output wired to effectors. Mine: actuation is oriented motion in a coherence field, and the reader — Jev, an LLM, a sensor, whatever supplies the trait values — sits only at the perception edge and never touches the act.

The model belongs at the language edge, never in the decision core. That is not a slogan; it is a load-bearing constraint, and it is why an oriented core runs at frame rate across many agents where a metered model call, at tens to hundreds of milliseconds and a per-call cost, structurally cannot.

## The target moves

The hardest and most honest criticism of the classifier is that the schema is a hard prior: someone has to author it, it does not scale as edge cases multiply, and it breaks on the case it was never given — the colour that isn't in the list, the hazard nobody modelled. This is correct, and it is not answered by a nicer authoring surface. A better text box for writing a frozen schema inherits the whole problem.

It is answered by a schema that evolves — that adapts against revealed outcomes, with provenance on every change, so the authoring burden is bounded rather than exhaustive. Static schema versus evolving schema is the real line. The unmodelled case is not a gap to be pre-specified away; it is an event the system is built to absorb and learn from. A frozen prior cannot do this. That is the difference between shipping the inheritance and shipping the capacity to learn from it.

## Two clocks, and it is governance, not speed

Orientation runs on two rates. A fast tick: local geometry, a step along the coherence gradient, no inference, frame rate. A slow tick: semantic ingestion of the genuinely new, and evolution of the schema itself — deliberately paced. The temptation, once ingestion becomes cheap, is to collapse the two into one and re-decide everything every frame. That works for a pure reflex, and it is elegant. It is also only valid because it throws away the two things the slow tick exists to protect: a target that does not chase every twitch of input, and a space that holds still long enough to be oriented against. The separation of the clocks is a governance separation, not a cost compromise. Making the read cheap does not earn the right to merge them.

## Meeting the unknown

Novelty in a hostile frame does not stall the fast tick. The context supplies provisional traits — caution, low information, widen distance — before identification completes, and those provisional values are enough to act on safely *now*, while the slow tick resolves identity underneath. Caution first, identity later; the shortcut a parent gives a child before the child has met the thing to be wary of. Thereafter the new object accretes observed traits, and the slow tick moderates the inherited caution against them — provenance keeping what was inherited distinct from what was earned, so a borrowed prior is never mistaken for ground truth.

The rate of that moderation is an open problem, and I will not pretend otherwise. Too slow and the system fears the harmless thing forever; too fast and one calm encounter lowers a guard that should have held. It is precisely the parameter humans get wrong in both directions — the trauma that never updates, the trust that updates on nothing. The claim here is not that I have the right rate. It is that keeping inheritance and observation *provenanced and separable* makes the two failure modes visible and constrainable, where in a human they are fused into one signal that cannot be audited. Uncertainty, throughout, is expressed structurally — as which target one orients to, or as a constraint — never as a weight on a trait's contribution. The core stays unweighted; importance is structural, not tuned.

## The inversion

The field's reflex is to make the model do as much as possible. Even the work that escapes token-generation escapes only halfway: it builds a *better model* to do the work, keeps the intelligence in the model, and treats determinism as the container the model sits inside. The move I am making is the opposite. Make the model do as little as possible — read the language edge, and nothing else. Put the intelligence in structure the model never touches: the joint, the geometry, the target, the governed evolution. Determinism is not the container. It is the value. The model is the edge organ.

## What I am claiming, and what I am not

I am not claiming to own this, to have arrived first, or to be the only one doing it. This is too large for any of that, and I am not interested in the fight. I am claiming that this is the position I hold and have been building — and that the code embodying the stance predates the vocabulary now making it legible. A bounded-agency gate (GatedClaw) was published and timestamped on 25 March 2026; the bounded-negotiation work (Fit'd) and the continuous-field navigation loop (the Affinari boids), which runs at tick rate with no model anywhere in it, sit alongside it. The reader is not the decision. Orientation is the floor. And the floor is empty enough to be worth planting a flag on.

*— A.F.*
