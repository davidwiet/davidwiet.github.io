# LLM Tool Continuity and Team Architecture

Status: publication candidate — conceptual outline, not a finished article.

## Current formulation

Tool use interrupts a model invocation. A returned tool result can be linked to the request that produced it, yet that link alone does not preserve the represented relation between the system, the external computation, and the result. The system can therefore narrate one continuous act where the operative process was actually discontinuous.

The proposed alternative is not to make later invocations imitate a single continuing person through increasingly complete context transfer. It is to organize the work as a human-directed team of bounded contributors. Model invocations, tools, deterministic processes, and people receive defined work packages, carry out bounded functions, and produce accountable handoffs.

Continuity is therefore procedural rather than autobiographical. Context may be filtered, enriched, compressed, branched, or recombined, provided that the governing purpose, active constraints, authority boundaries, provenance, decisions, and unresolved questions are preserved or their alteration is explicit and reviewable.

The article is not a claim that handoffs, external state, specialization, or human participation are novel components. Its claim is that the single-agent picture makes these real mechanisms look exceptional or supplementary, where a team-and-handoff picture makes them architectural defaults.

## Open work

- Separate descriptive claims about current systems from interpretive and design claims.
- Define the distinction between functional stages, execution episodes, and handoffs.
- Develop the philosophical hinge without treating it as proof of the architecture.
- Decide the article's intended audience and evidence standard.
