# Concise Argument Map

Status: provisional logical map, not publication prose.

## Central thesis

LLMs work because broad context often lets their outputs approximate how
language represents field-specific structure. Whether this depends on a learned
field model or other learned regularities remains open. They reach their limit
when increasing structural complexity or longer chains of linguistic
transformation cause the approximation to drift until linguistic coherence no
longer tracks the field reliably. They may improve by learning
language–semantics mappings jointly with field-appropriate representations in
which the resulting semantics can be operated on or checked.

## The three answers

- **Why they work:** context supports approximate identification of a latent
  field, representational practice, and mapping between expressions and domain
  structure.
- **Where they fail:** the linguistic representation becomes a progressively
  poorer proxy as domain complexity and transformation depth increase; surface
  plausibility can outlive semantic correlation.
- **How to improve them:** infer the active use of language, translate or align
  its semantics with a suitable domain representation, reason or validate in
  that representation, and translate the result back.

## Main inferential sequence

1. Human language has many representational uses: it can describe physical,
   mathematical, causal, spatial, social, legal, procedural, and other
   structures whose governing relations are not identical with linguistic
   grammar.
2. A sufficiently context-sensitive model can often infer which use is active
   and approximate a context-sensitive relation `e_(D,c)` between a linguistic
   expression and one or more states in a semantic representation `R_D`.
3. This contextual approximation explains broad competence without requiring
   the model to possess one explicit, complete, universal world representation.
4. Autoregressive pretraining rewards probable linguistic continuation;
   post-training adds instruction and preference objectives. None directly
   requires every generated transformation to remain valid in `R_D`.
5. Two factors increase the opportunity for divergence: greater structural
   complexity in `R_D`, which is harder for the linguistic proxy to track,
   and greater transformation depth, which permits local approximation errors
   to accumulate.
6. Beyond some task-relative threshold, surface quality ceases to be reliable
   evidence of semantic fidelity. The model may still produce meaningful
   language while the correlation no longer supports reliable field-valid
   inference.
7. A correct final state does not repair an invalid route. Field-valid reasoning
   requires every semantic transition in the path to be licensed by the active
   field syntax.
8. Better training should therefore pair linguistic uses with representations
   of their resulting semantics that expose the syntax of valid transformation
   in the field:
   programs, equations, graphs, spatial models, causal structures, perceptual
   states, executable procedures, or other suitable forms.
9. The resulting system should infer the field and representation in use,
   perform or validate transformations in that representation, and render the
   result linguistically. Context remains essential for selecting and
   interpreting the mapping, but is no longer its only constraint.
10. When several fields are intertwined, the system must coordinate multiple
   semantic state spaces, transformation syntaxes, and interfaces among them.
   When the field-defining anchor loses contextual or attentional influence,
   the system can also lose the field syntax that governed the original
   linguistic use.
11. Search, consolidation, tools, perception, action, uncertainty, and abstention
   become parts of a controller that selects representations, preserves their
   syntactical validity through semantic change, and renews their connection to
   the field when necessary.
12. If this controller can explore field-valid semantic transitions without
   remaining confined to familiar linguistic continuations, it may enable
   genuinely novel inference. This is the culminating hypothesis, not an
   established result.
13. In less rigid fields, the same principle requires contextual and plural
   transformation syntax rather than one fixed rule set. Innovation may include
   intelligible violation of a convention, provided the violation remains
   structurally warranted in the evolving field representation.
14. Teaching such syntax requires that its distinctions be represented in the
   training signal. As human articulation, demonstration, agreement, and
   evaluation become weaker, the proposed remedy becomes correspondingly harder
   to realize.
15. Yet within a human-identified field, model scale may detect complex latent
   regularities distributed across more cases and interacting relations than
   humans can grasp unaided. Underdefinition is therefore both a teaching
   obstacle and a possible opportunity for model-assisted structural discovery.
16. A soft-domain instance may proceed from enacted but tacit structure to model
   articulation, human recognition and correction, and prospective testing.
   This turns implicit practice into an explicit candidate representation.
17. A complex claim need not be checked exhaustively. Once it makes observable
   predictions, independent random or stratified sampling can estimate its
   reliability over a declared population, even when humans cannot fully grasp
   the internal pattern.

## Othello as the clearest positive model

Othello-GPT is not merely a caution against surface-only interpretations. It
demonstrates the kind of learning the article proposes in a controlled domain.

The model receives sequences of move tokens. It is not given the board, its
geometry, or the game rules. The large synthetic corpus samples uniformly from
legal play rather than rewarding familiar human strategy. Successful
prediction therefore requires sensitivity to the evolving legal state, not
only imitation of preferred moves.

Mechanistic evidence reveals a transformation from sequential surface input to
field-organized internal state:

`move-token history -> mine/yours/empty board state and flipped pieces -> legal
transition constraints -> next-move token`

The player-relative categories are especially important. Human observers first
looked for black, white, and empty squares and concluded that the representation
was nonlinear. Nanda et al. found an almost perfectly linear representation
when they instead asked whether each square contained one of my pieces, one of
your pieces, or was empty. The model's internal organization followed the
functional structure of the task rather than the surface notation or the first
human ontology imposed on it.

Causal intervention strengthens the inference. Moving internal activations
along those state directions changes output toward the moves legal on the
counterfactual board. The semantic state is therefore not merely readable from
the model; it participates in generation.

This supplies a bounded positive answer to the article's design question.
Sequence learning can construct a field-appropriate semantic mechanism inside
the model rather than outsource field validity to a tool. The proposed
multi-domain generalization is:

`context identifies the field and task -> an appropriate internal state system
is formed or activated -> field-valid transformations govern the state -> the
result is rendered linguistically`

Three qualifications prevent overclaiming:

1. The representation is learned from the move sequences and their legal
   distribution; it is distinct from the surface notation, not independent of
   its evidence.
2. Othello is deterministic, fully observable, and densely represented by
   millions of clean legal games. Open empirical and interpretive domains do
   not supply equally direct training signals.
3. The same model appears to use several circuits, especially late in a game.
   The goal is therefore not one mechanism per domain but a repertoire of
   domain- and task-appropriate mechanisms whose coordination preserves field
   validity.

The first representational-invariance experiment now exists. The 2026
MetaOthello preprint trains equivalent games under permuted token-to-square
mappings and reports internal states aligned up to an orthogonal rotation, with
causal transfer of predictions across most layers. In mixed Othello rule
variants, it finds shared board-state structure plus localized routing and
specialization where the rules conflict. This is direct evidence
for representation beyond one notation and for coordination of related rule
systems.

MetaOthello addresses invariance across notation and coordination among related
rule systems. The next experiment moves from game variants to genuinely
different domains and tests whether context selects and composes their
mechanisms without collapsing them into one generic linguistic proxy.

## Essential distinctions

- **Search / discovery:** open exploration for candidate regularities.
- **Learning / consolidation:** reconstruction of sufficiently stable
  regularities into concepts, rules, or reusable methods.
- **Execution:** application of a consolidated method without repeating the
  original search.
- **Linguistic reach:** what can be stably inferred using linguistic evidence
  and representation.
- **Representational correlation:** the task-relevant structural relation by
  which a linguistic item represents a field-specific semantic structure.
- **Field-appropriate representation (`R_D`):** a representation whose
  states and operations expose relations material to a particular domain;
  it need not be unique, fully formal, or hand-designed.
- **Field syntax (`T_D`):** the rules or relation defining which transitions
  between semantic states in `R_D` are valid.
- **Soft field syntax (`T_(D,c)`):** a contextual family of defensible
  transformations whose constraints may be graded, plural, genre- or
  tradition-sensitive, and revisable rather than binary or exhaustive.
- **Teaching signal (`S_D`):** linguistic, formal, demonstrative, interactive,
  environmental, or evaluative evidence from which a model could learn the
  semantic states, transformation syntax, and value criteria of field `D`.
- **Articulation bottleneck:** the limit imposed when `S_D` fails to express or
  discriminate structural distinctions that humans cannot adequately define,
  demonstrate, agree upon, or evaluate.
- **Latent-structure discovery:** model-assisted detection, within a
  human-identified field or paradigm, of stable complex regularities that have
  not been adequately represented in explicit human theory.
- **Paradigm boundary:** the human-identified rule-constituting scope within
  which the present hypothesis begins; it does not currently assign paradigm
  identification, selection, revision, or replacement to the model.
- **Sample-validatable structure:** a candidate pattern complex enough to resist
  exhaustive inspection but operationalized through predictions that can be
  evaluated on an independent probability sample from a declared population.
- **Semantic transformation:** movement from one meaning or domain state to
  another; this is the intended product of reasoning, not a defect.
- **Contextual approximation:** inference from linguistic context of the active
  field, language use, and approximate mapping into `R_D`.
- **Proxy drift:** widening divergence between operations on the linguistic
  surface and valid operations or states in `R_D`.
- **Semantic-representation training:** learning to predict, construct,
  transform, or validate `R_D` alongside language, whether or not an external
  executor is available.
- **Tool calling:** routing an identified operation to an external executor or
  information source. Tool use may exploit a semantic representation but does
  not itself supply or define one.
- **Field anchor:** the contextual material that identifies the active domain,
  representational practice, and applicable field syntax.
- **Representation interface:** a mapping that carries constraints or results
  between two field-specific representations in a hybrid task.
- **Correlation syntax:** the structural rules governing valid transformations
  of a representation in relation to its field; not merely the surface grammar
  of the linguistic expression.
- **Intra-linguistic transformation:** an operation selected or licensed by
  relations internal to linguistic representations.
- **Field-valid transformation:** an intra-linguistic operation whose semantic
  transition is licensed by the applicable field syntax or independently
  validated against the represented domain.
- **Terminal correctness:** acceptability of the final semantic state,
  considered independently of how it was reached.
- **Path validity:** the requirement that every adjacent semantic transition
  in a reasoning path be licensed by the active field syntax.
- **Valid success:** terminal correctness plus path validity.
- **Unwarranted success:** a correct endpoint reached through at least one
  field-invalid transition.
- **Generated rationale:** a linguistic account of how an answer was reached;
  it is not evidence of the actual transformation path unless independently
  validated or causally linked to subsequent behavior.
- **Domain value function:** a field-sensitive criterion for ranking valid
  semantic states or paths by relevance, quality, promise, or goal achievement;
  validity alone does not provide it.
- **Epistemic resolution:** for a specified task, the finest distinction that a
  fixed decision procedure can recover from admitted evidence and
  representations while meeting precommitted error and calibration thresholds
  under relevant shifts.
- **Information / identifiability limit:** admitted observations leave relevant
  alternatives equivalent.
- **Representation / learning limit:** a useful signal exists, but the learner
  does not recover it.
- **Decision / calibration limit:** the system cannot reliably select, express,
  or assess an answer even if relevant information is internally available.
- **More computation / new constraint:** refining inference within the same
  information is different from adding perception, action, retrieval, formal
  rules, or other evidence.

## Evidence-driven revisions — 31 July 2026

- **Finding retained, correction withdrawn:** color, space, and time studies
  show measurable world structure in text-trained representations. This does
  not rebut the author's position, which concerns whether later linguistic
  transformations preserve the correlation that carried that structure.
- **Retained in bounded form:** linguistic evidence has selective coverage and
  fidelity. Reporting bias, abstraction, context dependence, and
  underspecified validation leave some distinctions unstable or unidentified.
- **Qualified:** “more refinement produces noise” is a risk, not a law.
  Repeated data and recursively generated data show diminishing returns or
  collapse in particular regimes, but additional inference over fixed evidence
  can still discover real structure.
- **Qualified:** uncertainty is not yet an epistemic-limit detector. Semantic
  entropy, self-evaluation, and selective prediction detect some error risk;
  calibration degrades under shift, and none of them diagnoses which layer
  failed.
- **Novelty narrowed:** program-library learning, modular composition, sparse
  routing, learned tool use, and algorithm distillation already implement parts
  of the proposed design. The open contribution is a principled and testable
  control rule connecting them.

## Author clarification — 2 August 2026

The central limit is **transformation fidelity**, not the initial availability
of world structure in language. The strongest current reconstruction is:

> A linguistic representation does not retain its representational warrant
> merely by remaining well formed under intra-linguistic transformations. Its
> fidelity endures only insofar as those transformations preserve, or renew,
> the structural correlation with the extra-linguistic domain.

The phrase “fidelity is lost” currently has two possible strengths that must be
settled before publication:

1. **Loss of warrant:** after an unverified intra-linguistic transformation,
   fidelity is no longer established by the original correlation, even if the
   result happens to remain correct.
2. **Loss in fact:** intra-linguistic transformation positively degrades the
   correlation and makes the result less faithful.

The first is the more defensible conceptual claim. The second is an empirical
prediction whose strength should be measured across transformation types and
chain lengths rather than assumed universally.

## Core-thesis adoption — 2 August 2026

The article's three questions are now one explanatory sequence:

> Context lets LLMs approximate field-specific representational uses of
> language; complexity and repeated linguistic transformation make that proxy
> drift from the represented structure; field-appropriate semantic
> representations can constrain the mapping and its transformations directly.

This formulation strengthens the empirical version of the thesis. It predicts
not merely loss of warrant, but a measurable interaction: semantic fidelity
should decline as domain complexity and reasoning depth increase, and training
or checking against appropriate semantic representations should reduce that
decline even when surface linguistic quality changes little.

## Domain syntax and tool distinction — 2 August 2026

The semantic content should change; the validity requirement depends on what
the language is doing:

| Linguistic use | Semantic states | Syntactical validity requirement |
| --- | --- | --- |
| Mathematical reasoning | quantities, expressions, equations, propositions | Each step follows a valid mathematical operation or derivational rule. |
| Spatial description | objects, locations, orientation, topology, containment | Each change follows a valid spatial state transition while maintaining required relational consistency. |
| Philosophical argument | premises, conclusions, concepts, distinctions, commitments, objections | Each development preserves the validity of inferential and dialectical relations, including explicit revision where appropriate. |

Semantic transformation is the point: a derivation produces a new result, an
action changes a spatial state, and an objection changes an argument's
dialectical situation. What persists is not meaning but the syntactical
validity of the transition under the field's rules.

This proposal differs from tool calling:

1. Tool calling first identifies a task and delegates an operation to an
   external specialist.
2. Semantic-representation training changes what constrains the model's own
   inference; it can improve performance even when no tool exists.
3. A tool can execute or verify a semantic representation, so tool use and
   semantic alignment can cooperate, but neither entails the other.

The clean comparison is therefore factorial: text-only versus semantic-
representation training, crossed with tool unavailable versus tool available.
If semantic training helps only when a tool is called, the stronger claim about
improving the model's own reasoning is not supported.

## New limit predictions — 2 August 2026

- **Hybrid-field penalty:** tasks that intertwine fields should produce errors
  not only within each field but at selection, switching, and interface points,
  where results must be translated without losing constraints.
- **Anchor-decay effect:** when the original cue that selected a field becomes
  distant, attentionally weak, or unavailable outside the context window,
  later outputs should increasingly follow generic linguistic priors rather
  than the field's transformation syntax.
- **Humanities boundary drift:** even where no unique formalization exists, a
  model should measurably change premise roles, conceptual distinctions,
  commitments, or dialectical positions while retaining rhetorical
  plausibility. Evaluation should use a defensible set of readings or bounds,
  not pretend that one annotation is the sole underlying truth.

## Strongest pressure points

1. “Syntax” may be mistaken for surface grammar. Here it means the structure of
   valid transitions among semantic states in a field; the argument must show
   that this use is coherent in many-to-many and context-sensitive domains.
2. Semantic change must not be treated as degradation. The required criterion
   separates field-valid transformation from merely language-licensed
   transformation, regardless of how much the resulting meaning changes.
3. Corpora themselves contain examples of field-valid transformations, so an
   LLM may learn approximate domain syntaxes without direct
   world access. The thesis must concern lack of guarantee and failure regimes,
   not deny this possibility.
4. No “original representation” is unmediated. Its fidelity is already partial,
   contextual, and purpose-relative, so preservation cannot require literal
   identity or a simple isomorphism.
5. Cross-modal systems still encode their evidence in representations; moving
   beyond language does not escape mediation. Its value lies in renewing or
   testing the correlation, not in attaining representation-free access.
6. A stopping mechanism may suppress rare but genuine structure as noise;
   recursive synthetic-data collapse makes preserving the tails especially
   important.
7. Consolidated methods can become brittle when domains change.
8. Existing systems may already instantiate parts of the proposal, reducing
   its novelty to a synthesis or research framing.
9. Efficiency gains in a toy domain would not establish a general architecture
   claim.
10. “Field-appropriate” can conceal a hand-coded ontology. The architecture
    needs a principled way to learn, select, combine, and revise representations
    where a field has multiple legitimate semantic schemes.
11. Current LLMs may already learn useful domain representations internally.
    The empirical comparison must therefore test explicit or supervised
    semantic alignment against matched text-only models, not assume the
    baseline contains none.
12. Context-window loss is mechanically clear, but “fading from attention” may
    conflate several mechanisms: position effects, distractor competition,
    compression, state overwriting, or failure to retrieve the anchor. These
    must be manipulated separately before attributing a cause.
13. Humanities boundaries may reflect evaluator interpretation rather than a
    unique underlying structure. Strong evidence requires preserved source
    provenance, multiple defensible analyses, and predeclared violations that
    all or most analyses exclude.
14. Field validity is not innovation. A perfectly valid search can generate
    familiar, trivial, or useless results; novelty and domain value require
    separate criteria.
15. “Not found in the prompt” is not novelty. Training-data contamination,
    retrieval, paraphrase, template recombination, and rediscovery must be
    excluded before attributing an inference to innovation.
16. Syntactical constraint may merely improve reliability without expanding the
    reachable semantic space. The innovation hypothesis requires a matched
    comparison showing more novel, valid, valuable results—not just fewer
    errors.
17. Rules plus unconstrained search can generate indefinitely many novel but
    worthless states. The innovation mechanism also needs a defensible value or
    goal criterion that does not simply reintroduce imitation as the standard.
18. Soft-domain syntax can become vacuous if every aesthetically successful
    outcome is declared valid after the fact. Constraints, admissible readings,
    and evaluative criteria must be stated before reviewing the generated work.
19. A model may learn genre formulae rather than dramatic structure. Tests must
    vary surface style and familiar plots while preserving or perturbing deeper
    character, causal, temporal, and scene-function relations.
20. “Humans cannot state the rules” does not mean the structure cannot be
    taught: demonstrations, counterexamples, consequences, and iterative
    judgments may embody tacit distinctions. The relevant question is whether
    the total teaching signal discriminates them reliably.
21. Conversely, examples do not magically solve under-articulation. If the
    training signal does not distinguish a valid transformation from a merely
    plausible one, the model cannot be expected to infer that distinction
    dependably.
22. Pattern complexity can shield error from scrutiny. A representation humans
    cannot grasp must earn confidence through reproducible consequences rather
    than model authority or linguistic persuasiveness.
23. High-dimensional regularity may be spurious, unstable, or useless even when
    statistically detectable. Held-out transfer, intervention, competing
    explanations, and nontrivial use must test it.
24. The hypothesis must not silently expand into autonomous paradigm choice.
    Current scope begins after humans identify the field or paradigm in which
    latent patterns are sought.
25. Human recognition can reflect suggestion, vagueness, or confirmation bias.
    A candidate articulation should make predictions about unseen cases or
    controlled generation that could fail.
26. A random sample is only as good as its sampling frame and labels. Coverage
    gaps, dependence, distribution shift, evaluator disagreement, and repeated
    hypothesis search can all create false confidence.
27. Discovery and confirmation must be separated. Testing a model-generated
    hypothesis on the same cases that produced it does not supply independent
    validation; multiple candidate searches also require appropriate control of
    selection effects.

## What would change the argument

- Evidence that linguistic transformations remain field-valid as reliably as
  explicitly domain-trained or externally checked transformations would weaken
  the central diagnosis.
- A demonstration that intra-linguistic training reliably learns the needed
  field syntaxes across unfamiliar domains and long transformation chains would
  show that renewed grounding or formal constraint is less necessary than the
  thesis predicts.
- Evidence that consolidation never improves cost or reliability over repeated
  search would undermine the learning–execution proposal.
- Evidence that no reliable signal can distinguish supported from unsupported
  refinement would turn the architectural proposal into an aspiration rather
  than a mechanism.
- Evidence that current architectures already solve these problems would shift
  the article from proposing a new direction to interpreting and unifying
  existing work.

## Narrow experimental wedge

Construct paired language/domain tasks with a known semantic representation—
for example, descriptions of program states, graphs, spatial configurations, or
causal systems. Vary domain complexity and required transformation depth
independently. Compare a matched text-only contextual model with one trained to
predict, transform, or validate the corresponding domain representation.

Measure (a) surface linguistic quality, (b) correlation with the true domain
state after each step, (c) confidence and calibration, and (d) compute cost.
The decisive prediction is an interaction: semantic fidelity in the text-only
condition should decline more steeply with complexity and chain length than
surface quality does, while semantic-representation training should flatten
that decline. Failure to observe the dissociation weakens the limit claim;
failure of domain representations to improve it weakens the proposed remedy.

Add two extensions only after the single-field result is established. First,
cross two fields with an explicit interface and localize error to within-field
or interface transformations. Second, manipulate the field anchor through
distance, distractors, compression, and hard context-window removal. For tool
calling, use a `2 x 2` design—text-only/semantic training by tool absent/present—
so external execution cannot be mistaken for improved semantic representation.

## Syntactical-validity correction — 2 August 2026

The invariant is the syntactical validity of semantic transformation, not a
fixed semantic meaning. Let `R_D` be a semantic state space for field `D`, let
`e_(D,c)` relate language in context to one or more states in that space, and
let `T_(D,c)` specify admissible transitions. A linguistic move is field-valid
when its selected interpretations stand in the relevant transition relation.
Proxy drift occurs when language licenses a move that the field does not.

## Endpoint versus path — 2 August 2026

For a semantic trajectory `r_0, r_1, ..., r_n`, terminal evaluation tests only
`r_n`. Field-valid reasoning requires `(r_i, r_(i+1))` to belong to `T_D` for
every step. This explains the familiar reaction “the answer may be right, but
how did it get there?” The concern is not stylistic transparency: it is that a
correct endpoint can be accidental, unwarranted, or non-robust because the
transformation path left the field syntax.

Examples:

- a mathematical answer obtained through an invalid cancellation;
- a correct spatial location reached through mutually inconsistent
  intermediate relations;
- a philosophical conclusion supported only after an equivocation, an imported
  premise, or a silent change in a concept's argumentative role.

A generated chain of thought does not by itself solve the problem. It can be a
post-hoc linguistic path whose surface plausibility is no more field-valid than
the answer. Strong evaluation needs explicit semantic states, step verifiers,
controlled interventions, or tests showing that later behavior depends on the
purported intermediate structure.

## Deep innovation hypothesis — 2 August 2026

**Status:** strictly hypothetical.

Plausible mimicry selects continuations largely because they resemble
linguistic patterns already represented in the model's evidence. Field-syntax
reasoning could support a different mode of generation: propose a semantic
transition because it is valid in `T_D`, even when its linguistic realization
is unusual or lacks a close precedent.

The hypothesis is not that validity automatically produces creativity. It is:

> Relative to a matched context-only model, a system trained over semantic
> states and field-valid transitions will produce more inferences that are
> simultaneously novel, path-valid, independently correct, and nontrivially
> valuable.

Four gates must remain separate:

1. **Novelty:** the result is not memorized, retrieved, paraphrased, or a trivial
   recombination of available exemplars.
2. **Path validity:** every semantic transition is licensed by `T_D`.
3. **Independent correctness:** the result survives evaluation in the field,
   not merely linguistic review.
4. **Nontrivial value:** the result matters under predeclared domain criteria;
   validity alone is insufficient.

The experiment must match data, compute, tools, and opportunities for search.
If semantic-state training improves reliability but not the rate of results
passing all four gates, the architectural proposal may still be useful while
the innovation hypothesis fails.

### Chess as the clearest illustration

| Function | Chess | General architecture |
| --- | --- | --- |
| Semantic state | board position | field-appropriate representation `R_D` |
| Valid syntax | legal moves and state transitions | transition relation `T_D` |
| Exploration | search through possible continuations | search through semantic paths |
| Value | positional or game-outcome evaluation | domain-sensitive ranking of valid results |

A corpus imitator can play by recognizing familiar positions and reproducing
moves associated with them. A state-and-rule system can search legal
continuations and select a move absent from its human-game evidence. That move
is genuinely interesting only if it is also strategically valuable: novelty
plus legality is not enough.

The analogy therefore sharpens rather than proves the deep hypothesis. It shows
how field syntax can decouple generation from precedent, while search and value
make that freedom usable. It does not establish that analogous representations,
transition rules, or value functions can be learned in less formal fields.

### Drama as the soft-domain complement

| Function | Chess | Drama |
| --- | --- | --- |
| Semantic state | board position | characters, knowledge, desires, conflicts, causal history, dramatic situation |
| Transformation syntax | binary legal moves | contextual constraints on action, revelation, reversal, setup/payoff, scene function, and thematic development |
| Search | legal continuations | possible developments of plot, character, conflict, and audience understanding |
| Value | strategic evaluation and game outcome | plural judgments of coherence, force, surprise, significance, and aesthetic achievement |

A pattern imitator can produce a story resembling familiar stories. A
structure-sensitive model would track the evolving dramatic state and generate
developments warranted by it. Because dramatic syntax is contextual, a valid
move may violate a genre convention when the violation performs an intelligible
function. The opposite failure is not unconventionality but an unearned change:
a reversal without preparation, a character action disconnected from the
represented motivations, a forgotten causal condition, or a thematic claim
that the dramatic path did not establish.

Drama therefore tests the same principle under much harder conditions. The
model needs a family `T_(D,c)` of defensible transformations rather than one
fixed `T_D`, and a plural value assessment rather than a single winning
condition. Evidence must show structural development across multiple
defensible readings, not merely formula compliance or evaluator preference.

### The articulation bottleneck

The architecture cannot learn `R_D`, `T_(D,c)`, or a domain value function
without evidence that represents them. Let `S_D` denote the total teaching
signal: definitions, formal structures, demonstrations, counterexamples,
critiques, simulations, interaction, environmental consequences, and expert
judgments. Learnability depends on whether distinctions material to the field
are recoverable from `S_D`.

This creates a gradient:

1. **Explicit formal domains:** states and valid transitions can be specified
   and mechanically checked.
2. **Structured empirical domains:** states and transformations can be modeled,
   but observations, approximation, and representation choice introduce error.
3. **Soft interpretive domains:** states, valid developments, and values are
   partly tacit, plural, context-sensitive, and contested even among experts.

The principle remains the same across the gradient, but the teaching problem
becomes harder. A richer representation does not remove this limit; it succeeds
only if humans or environments can supply a signal that embodies distinctions
the representation is meant to learn.

This is a second-order limit on the proposed remedy. It also prevents a false
promise: domain representations cannot simply be requested or invented by the
model when the field itself has not made the relevant structure sufficiently
articulable, demonstrable, or evaluable. The strongest soft-domain research
must therefore study not only model architecture but the quality and agreement
structure of `S_D`.

### Latent-structure discovery within a paradigm

The teaching bottleneck has a positive counterpart. A human-identified field
may contain stable structure that no person has successfully compressed into an
explicit theory because the pattern spans too many cases, dimensions, or
interacting relations. Model scale may permit detection and use of such
regularities.

This creates two discovery levels:

1. **Object-level:** search for a novel valid path inside a known `R_D` and
   `T_D`.
2. **Representation-level:** within the given paradigm, propose a candidate
   `R_D`, `T_(D,c)`, interface, or value model that makes previously tacit or
   inaccessible regularity explicit enough to test.

The model does not establish a structure by articulating it. Candidate
structures should compete on predeclared criteria: held-out discrimination,
prediction or generation, robustness to counterexamples and interventions,
transfer, explanatory compression, and practical or intellectual fruitfulness.
Where the full pattern remains beyond human comprehension, partial inspectable
projections and reproducible external effects must carry the evidential burden.

The governing metaphor is an instrument rather than an oracle. The model may
extend human pattern-detection capacity, but humans still establish the paradigm
and the procedures by which a candidate regularity earns provisional authority.

### Tacit-to-explicit recognition loop

David's writing-style experience supplies a concrete soft-domain example:

`enacted structure -> model articulation -> author recognition/correction -> prospective test`

He reports that a model identified stylistic rules and patterns he had not been
consciously applying, but which he recognized once stated. The example fits the
current boundary: David had already identified the domain—his writing—and the
model proposed latent structure within it.

The author's recognition is relevant because first-person practical knowledge
can confirm that a description captures an intention or habit not previously
verbalized. It is not sufficient by itself. Stronger tests ask whether the
rules:

- classify unseen passages as his or not his;
- predict choices in new writing;
- survive passages that appear to be counterexamples;
- generate recognizably similar structure without phrase copying; and
- improve deliberate control of style when applied prospectively.

The example is therefore an illustration of how tacit structure might become
explicit and testable, not evidence that every model-generated stylistic theory
is accurate.

### Sampling as scalable validation

Exhaustive human comprehension and exhaustive case checking are not required
for scientific validation. If a candidate latent structure yields observable
predictions, the following sequence can test it:

`discovery corpus -> frozen hypothesis -> declared population -> independent sample -> blinded evaluation -> uncertainty estimate`

Random sampling supports an estimate of generalization to the sampled
population. Stratification is appropriate when rare regimes, hybrid fields, or
important subgroups would otherwise be underrepresented. In soft domains,
evaluation should use multiple independent judges or a predeclared admissible
range rather than silently treating one contested judgment as ground truth.

The result is bounded. A successful sample does not establish a universal law,
causal mechanism, or robustness to every distribution shift. It does establish
that an opaque or large-scale candidate pattern can earn empirical support
without every case or internal dimension being humanly inspected.

This supplies the validation bridge for model-as-instrument reasoning: humans
need not comprehend the entire detected pattern, but they must be able to define
observable consequences and a sampling procedure capable of proving the model
wrong.

### Weather forecasting test case

Weather supplies a structured empirical bridge between chess and drama:

`observed/reanalysed atmospheric state -> learned transition -> future-state distribution -> later verification`

- `R_weather` is not prose but a multilevel, multivariable spatial state of the
  atmosphere and relevant Earth-system components.
- `T_weather` is probabilistic and approximate. Validity involves dynamical and
  thermodynamic constraints, cross-variable relations, coherent trajectories,
  calibrated uncertainty, and skill against later states.
- Model scale can exploit interactions too numerous for unaided human pattern
  recognition, while each forecast creates observable consequences on which
  the learned regularity can fail.
- The field therefore supports both object-level tests of learned pattern use
  and representation-level tests of candidate meteorological discoveries.

The case illustrates the central thesis only because training and evaluation
occur in field-appropriate atmospheric representations. It is not an instance
of an LLM inferring weather reliably from linguistic context alone. Nor does
forecast accuracy by itself establish an explicit discovery: an opaque model
may encode a useful regularity without producing a human-interpretable rule or
causal account.

A clean discovery test would freeze a candidate relation and its forecast
consequences before evaluation, compare it with strong physical and learned
baselines, and score held-out or prospective forecasts across ordinary and rare
regimes. Because weather cases are dependent and extremes are rare, temporal
blocking and regime stratification are generally more defensible than assuming
an independently drawn simple random sample.

## Coherence and objection audit — 4 August 2026

### Coherent core

The argument's strongest form joins three claims without making any of them
universal:

1. Linguistic sequence learning can produce behavior that tracks
   field-specific structure, either through an internal representation of that
   structure or through other regularities that approximate it.
2. Fluent generation does not guarantee that every semantic transition remains
   valid within that structure.
3. Training that makes field states and transition constraints more causally
   effective may improve reliability and, when combined with search and
   evaluation, discovery.

This formulation preserves the author's claim that language represents the
world while avoiding the stronger and false claim that sequence models can
only imitate linguistic surfaces.

### Necessary distinctions

#### Initial interpretation and later transformation

A valid transition preserves fidelity only relative to an adequate starting
representation. An initially false, incomplete, or purpose-inappropriate
interpretation can support internally valid reasoning whose conclusion remains
world-false. The empirical design must therefore vary and measure initial state
fidelity separately from transition validity.

#### Field structure and extra-linguistic structure

“Extra-linguistic” is too narrow for arguments, law, drama, and other practices
whose relevant structures are partly constituted by language. The governing
category is field-specific semantic structure not reducible to surface
continuation. Some instances are fully external to language; others are
linguistically articulated without being governed by ordinary linguistic
probability alone.

#### Interpretation as relation rather than function

`e_D: L -> R_D` suggests one context-free semantic state for each expression.
Actual interpretation may be partial, context-sensitive, many-to-many,
probabilistic, purpose-relative, or contested. `e_(D,c)` should therefore be
treated as a relation or distribution unless a test domain warrants a simpler
function.

#### One field and several concurrent representations

Hybrid tasks need not switch cleanly from one domain to another. A single step
may simultaneously carry mathematical, spatial, causal, social, and
argumentative constraints. The framework must permit several active
representations plus explicit interface constraints.

#### Object-level and representation-level discovery

Fixed field syntax supports new inferences inside an accepted paradigm.
Discovering or revising the representation and its syntax is a meta-level
process that proposes hypotheses about the field. Those hypotheses cannot be
licensed by the very syntax they revise; they require rival models and
independent tests.

### Source-driven corrections

- Othello-GPT shows that next-move sequence training produces task-relative
  field variables that counterfactual interventions can use to steer later
  predictions. Nanda et al.'s `Mine`/`Yours`/`Empty` result makes this a positive
  example of internal organization by the represented field rather than by
  surface notation. The unrestricted label “world model” remains contestable,
  but the functional learning result is strong enough to anchor the article.
- In-context learning has a theoretical account as latent-concept inference in
  coherent sequence distributions. It supplies a concrete model of contextual
  field selection within the article's broader explanation.
- Compositional and length-generalization studies document the degradation the
  article explains: increasing depth or structure can preserve plausible
  sequence production while weakening reliable field-valid transformation.
- Instruction tuning and reinforcement learning from human feedback add
  behavioral objectives after autoregressive pretraining. “The model selects
  probable continuations” describes the base training objective, not the whole
  causal account of a deployed assistant.
- Process supervision and explicit intermediate trajectories can improve
  performance and evaluation. A written process trace still does not by itself
  reveal the model's internal causal path.
- AlphaGeometry, AlphaTensor, and FunSearch show that explicit states,
  constraints, search, and evaluation can produce strong or novel results.
  Their evidence is architectural precedent: the result belongs to the whole
  system unless the model's independent contribution is isolated.

### Objections requiring an answer or a control

1. **Ordinary difficulty:** More complex structures and longer chains are
   harder for any reasoner. A decline alone does not identify proxy drift.
2. **Emergent representation:** If language training already learns usable
   world models, explicit semantic training may be unnecessary or redundant.
   The reply must first determine whether the relevant structure is present and
   causally governs generation. A decodable correlate, a proxy policy, and a
   governing representation are different mechanisms.
3. **Inductive-bias confound:** Field-aligned training adds supervision and
   structure. Any gain may come from more data, compute, capacity, or easier
   optimization rather than semantic alignment. Controls must match these
   resources.
4. **Representation imposition:** A human-designed `R_D` may distort a superior
   distributed representation already learned by the model. The proposal must
   allow learned and plural representations and test whether the constraint
   improves out-of-distribution fidelity.
5. **Soft-domain vacuity:** If every defensible interpretation receives its own
   syntax, no transition may be excluded. A soft-domain test must predeclare
   genuine boundary violations and permit several admissible analyses without
   accepting everything.
6. **Human comparison:** Humans also reason through language and commit
   structurally invalid transitions. The article must state whether it proposes
   an LLM-specific limit, a general limit of linguistically mediated reasoning,
   or an LLM-specific severity and remedy within a broader human problem.
7. **Internal–external boundary:** Tool use, symbolic modules, recurrent state,
   and learned simulators form a continuum. The useful distinction is whether
   training changes the model's own transition policy or delegates execution,
   not whether one component is metaphysically “inside.”
8. **Innovation suppression:** Enforcing accepted syntax can prevent errors but
   also suppress paradigm revision, productive analogy, or rule-breaking art.
   Object-level validity constraints must be paired with a separately governed
   meta-level process for proposing and testing new structures.
9. **System-level novelty:** Search plus a verifier can produce discoveries
   even if the LLM supplies only diverse proposals. This supports the proposed
   architecture but does not prove “true” innovation inside the language model.
10. **Unobservable paths:** A correct domain-state trace may be a generated
    justification rather than the computation that caused the answer. Causal
    interventions on intermediate states are stronger evidence than readable
    chains alone.

### Governing causal bridge

The diagnosis and remedy are connected by one causal bridge:

`field-aligned training -> field representation becomes more causally effective
during generation -> invalid-transition rate falls under controlled complexity
and depth`

Existing representations and specialized systems show that the components are
realizable. The article's contribution is the general explanatory connection
between their causal role and the preservation of valid transformation.

It also needs a mechanism-discrimination test:

`field-valid behavior -> intervene on candidate field state -> observe whether
later transformations change in the field-predicted way`

Successful decoding alone shows correlation. Successful, specific intervention
shows that a state-corresponding internal variable can govern output. It still
does not decide whether that variable constitutes a learned field model or a
predictive proxy induced by sequence structure. Distinguishing those accounts
requires tests of transition structure, counterfactual generalization, and
independence from familiar sequence statistics.

## Scope boundary

This map concerns why language-based systems work, how representational and
evidential limits arise, and what architecture might respond to them. Claims
about Richard Sutton's essay or its reception belong to the neighboring
`The_Better_Lesson_Sutton_and_Its_Reception` project.
