# The Better Lesson: Sutton and the Simplified Reception of *The Bitter Lesson*

Status: active writing project — publication candidate, not yet a finished article.

## Active objective

Turn David's insights developed in the ChatGPT conversation *The Better Lesson
2* into a source-grounded written piece on Sutton's essay and its reception.
The piece should preserve the conceptual argument before fixing its eventual
publication format. It must distinguish David's claims, Sutton's explicit
claims, and claims about the essay's broader reception.

## Current formulation

This work argues for a qualified agreement with Richard Sutton's *The Bitter Lesson* while questioning the stronger slogan often drawn from it. The issue is not whether scalable learning and search outperform brittle, hand-coded domain knowledge; that historical lesson may be substantially right. The issue is whether this implies that every learning problem should be collapsed into one undifferentiated optimization regime.

The proposed alternative is that architecture can reduce the conditions under which learning must succeed. Where an inexpensive and stable distinction identifies the relevant regime, subsequent learning or optimization need not repeatedly rediscover that partition inside one monolithic process. Classification and optimization are different computational problems, and keeping them distinct can be more faithful to scalable learning than making one system solve both indiscriminately.

The article therefore does not reject Sutton in favor of expert systems. It distinguishes Sutton's own historical claim from an oversimplified field reception that treats architecture, decomposition, and heterogeneous cognitive regimes as presumptively anti-scaling.

## Argument recovered from the source conversations

David's initial formulation has three movements:

1. **Efficiency.** Brute force can prevail when computation is abundant without
   thereby becoming intrinsically efficient. The relevant question is what
   happens to its resource demands as use and task complexity scale.
2. **Conditions of success.** Open learning is less brittle than a narrowly
   designed solution, but it still works under conditions: usable success
   criteria, feedback, sufficiently stable rules, workable system boundaries,
   and adequate data and computation. These conditions must be investigated,
   not smuggled into a universal scaling claim.
3. **The better lesson.** Scalable design should minimize the conditions under
   which learning must succeed. This preserves unconstrained learning where it
   is productive without assuming that every domain belongs to one
   undifferentiated optimization regime.

The central architectural example separates classification from optimization.
If a cheap and reliable operation can identify whether the system is playing
chess or Go, each strategy learner can optimize within the relevant game rather
than repeatedly rediscovering that partition. The example does not establish
that human engineers should permanently fix the correct domains. It creates the
harder research question: when should a partition be given, learned, revised,
or allowed to disappear?

The title *The Better Lesson* is therefore argumentative rather than merely
playful. It presents the article as a higher-level extraction from Sutton's
historical evidence, not a simple rebuttal of that evidence.

## Open work

- Read and quote Sutton's essay directly before making claims about his position.
- Separate Sutton's explicit argument from the article's critique of its reception.
- Specify the conditions under which an architectural distinction is stable enough to justify.
- Test the chess-and-Go example without treating it as proof.
- Determine whether the efficiency claim is linear, superlinear, or
  exponential in any specified setting; do not preserve “exponential” as a
  general claim without evidence.
