# The Better Lesson: Why LLMs Work, Their Limits, and How They Can Improve

Status: active writing project — publication candidate, not yet a finished article.

## Active objective

Turn David's insights developed in the ChatGPT conversation *The Better Lesson*
into a separate written piece provisionally titled *Why LLMs Work, Where They
Reach Their Limits, and How to Make Them Better*. This project has its own
source record and work session and must not be merged into the Sutton/reception
article merely because both conversations used the phrase “the better lesson.”

The immediate objective is to develop the project's working environment before
drafting the publication artifact. Durable research and reasoning must be
written into the project-owned files linked below rather than left only in raw
conversation history.

## Working environment

- [Workspace contract and file map](README.md)
- [External research summaries](working/research_summaries.md)
- [Othello-GPT deep research](working/othello_gpt_deep_research.md)
- [Expanded argument map and development record](working/argument_map.md)
- [Concise logical tree and article order](working/logical_tree.md)
- [Claims and evidence ledger](working/claims_and_evidence.md)
- [Reserved publication artifact](publication/article.md)

`current.md` owns project status, adopted working decisions, corrections, and
open questions. `sessions.md` owns source and session provenance but is not an
argument record.

## Current formulation

The project's core claim now answers its three title questions through one
mechanism:

1. **Why LLMs work:** their enormous contextual awareness often lets them
   approximate particular uses of language as representations of
   field-specific structures.
2. **Where they reach their limits:** as the represented structure becomes more
   complicated, or as a reasoning chain applies more transformations, the gap
   between linguistic surface and underlying structure widens. Eventually the
   linguistic sequence may remain coherent while no reliable or meaningful
   correlation with the represented structure persists.
3. **How to make them better:** train systems to infer different uses of
   language not from linguistic context alone, but in relation to
   field-appropriate representations of the semantics those uses produce.

Language can represent field-specific structure; that is a premise of the
argument. Such structure may be extra-linguistic or partly constituted by
language, as in argument and drama. The thesis concerns the fidelity of the
interpretation and its transformations. Context allows a model to infer an
implicit domain and approximate how language maps into it. But transformations
selected within language can become proxies for valid transformations within
the field. Their approximation error can grow with structural complexity and
accumulate across a reasoning chain.

The internal mechanism remains an open part of the thesis. Field-valid behavior
may arise because the model learned a field model, because other learned
regularities approximate the field in context, because it formed a causally
usable predictive state that falls between those descriptions, or through a
mixture. Accurate output, successful decoding, and even some interventions do
not automatically settle which description is correct.

Othello-GPT nevertheless supplies a positive proof of principle for the desired
direction. Training on legal move-token sequences produces internal variables
organized around the task's board state. Follow-up analysis finds
player-relative `Mine`/`Yours`/`Empty` states and flipped-piece features rather
than a mere copy of the token sequence or an imposed black–white ontology.
Causal interventions on these variables alter move generation as the
counterfactual board predicts. The proposed generalization is to make such
field-appropriate internal learning reliable across multiple domains and to
coordinate several representations when a task combines them.

The 2026 MetaOthello study extends two parts of that generalization. Under a
permuted token-to-square map, learned
states align up to a rotation that transfers causally across most layers. Under
paired Othello rule variants, the model largely shares board-state structure
and routes conflicting cases through localized specialization. This supports
surface invariance and multiple-rule coordination. The next extension carries
the same principle from related rule systems to independent and intertwined
domains.

The proposed alternative is therefore plural rather than one universal formal
language: infer which representational practice is active, form or activate an
appropriate internal representation, operate or check the result under the
field's constraints, and render it back into language. The representation need
not be hand-supplied. Othello shows that field-governed sequence data can induce
it; explicit semantic targets, interaction, and validation offer additional
routes. Search, consolidation, executable methods, formal constraints,
perception, retrieval, action, and tools matter insofar as they help learn,
preserve, or renew these mappings.

The proposal is not reducible to tool calling. A tool-using model classifies a
problem and delegates some operation to an external solver. The present claim
is that training against field-appropriate semantic representations can improve
the model's own transformations even when no external solver exists. Tools may
execute or verify a representation, but they are one optional use of semantic
alignment rather than its definition.

## Thesis-status correction — 4 August 2026

**Status:** adopted; supersedes the instruction to present the general
mechanism as merely a hypothesis supported by bounded examples.

The three-part mechanism is what David thinks explains why LLMs work, where
they fail, and how they can be improved. The article should state and argue it
as its thesis. It does not need to preface that thesis with the observation
that no bounded example establishes every instance of LLM competence.

Source limits serve one purpose: they prevent the article from attributing to a
study more than that study demonstrates. They do not determine the status of
the author's explanation. Othello-GPT and the other examples instantiate,
clarify, and support parts of the mechanism; they are not a tribunal whose
failure to prove the entire thesis requires repeated reservations.

Hypothesis language remains appropriate only where the project itself treats a
claim as conjectural, especially the possibility of genuinely innovative
inference and the more speculative latent-structure discoveries. It should not
be generalized to the article's core explanation.

## Open work

- Define “syntax” broadly enough to mean the relational structure governing a
  representation–world correlation, without confusing it with surface grammar
  or presupposing a simple one-to-one correspondence.
- Define when a semantic transition loses field validity and when its validity
  is merely unwarranted or unverified, including approximate and probabilistic
  cases.
- Formalize `R_D`, `T_D`, and the interpretation mapping for at least one formal
  and one non-formal field.
- Define “contextual awareness” and specify how a model's context supports the
  inference of a latent field, representational practice, or language use.
- Distinguish a learned field model from a causally exploitable predictive
  proxy and from behavioral approximation alone; specify interventions and
  counterfactual tests capable of separating them.
- Replicate and generalize MetaOthello's initial result that equivalent surface
  encodings produce structurally aligned internal representations, extending
  beyond one architecture, one permutation design, and one game family.
- Test whether a multi-domain model forms or activates distinct but composable
  domain- and task-appropriate mechanisms, and whether context routes among
  them without destructive interference.
- Specify how structural complexity and reasoning-chain length separately and
  jointly predict degradation of representation–domain correlation.
- Characterize “field-appropriate representation” without assuming that every
  field has one canonical, uncontested, or fully formal semantics.
- State the field-specific syntax of valid semantic transformation for
  mathematics, spatial reasoning, argument structure, and at least one
  genuinely hybrid task.
- Separate the effect of semantic-representation training from the effect of
  tool access in a factorial comparison.
- Test whether mixed-field tasks fail at representation selection, at the
  interface between representations, or during transformations within one
  field.
- Test whether increasing distance from the original field-defining anchor,
  including context-window removal and attention dilution, predicts proxy
  drift toward generic linguistic plausibility.
- Separate terminal-answer accuracy from transition-path validity, including
  the frequency with which a correct answer is reached through an invalid path.
- Determine how to test the transformations actually used by the system rather
  than accepting a generated chain-of-thought explanation as a faithful report
  of its internal process.
- Define “plausible mimicry,” “novel inference,” and “innovation” so that the
  culminating hypothesis can be tested rather than asserted rhetorically.
- Design a novelty audit that excludes memorized, retrieved, paraphrased, or
  trivially recombined results and separately measures path validity and
  nontrivial domain value.
- Separate the contribution of field rules, search, and value or goal
  evaluation; rules can license an unprecedented move without making it useful.
- Generalize `T_D` from rigid formal rules to plural, contextual, and graded
  constraints without making “field validity” so loose that every plausible
  continuation qualifies.
- Specify the articulation or teaching bottleneck: how adequately each field's
  semantic states, transformation syntax, and value criteria can be expressed
  through definitions, formal representations, examples, counterexamples,
  feedback, simulation, or interaction.
- Define and test the latent-structure discovery hypothesis: whether, within a
  human-identified field or paradigm, model scale can detect valuable complex
  patterns across distributed examples and relations that humans cannot grasp
  unaided.
- Develop weather forecasting as a structured-empirical test case for that
  hypothesis: distinguish accurate use of an opaque learned regularity from
  discovery of an explicit meteorological structure, and validate on
  temporally separated, regime-aware forecast cases rather than assuming
  ordinary independent random samples.
- Turn the author-reported writing-style episode into a bounded test: retrieve
  the original analysis if needed, distinguish recognition from suggestibility,
  and test extracted rules on unseen writing and controlled style generation.
- Specify a statistical validation protocol for model-discovered structures:
  separate discovery from confirmation, freeze observable predictions, sample
  randomly or stratify from a declared population, and report uncertainty,
  evaluator disagreement, and distribution limits.
- Separate transformation-induced loss of fidelity from three adjacent
  failures: missing information, failure to recover an available signal, and
  failure to calibrate or select an answer.
- Determine whether this becomes a theoretical essay, technical paper, or a linked series with the Sutton article.
- Specify paired world/language domains, field-valid and
  language-only transformation baselines, text-only and semantic-representation
  training conditions, fidelity measures, structural complexity, chain lengths,
  thresholds, and external-renewal policy before building the prototype.
- Test whether the proposed controller can preserve rare genuine structure
  while refusing unsupported differentiation and revising consolidated methods
  after a regime change.
- Complete a second research pass on interactive information acquisition,
  semantic invariance under transformation, representation drift, iterated
  inference, active learning, metareasoning/value of computation, and continual
  revision.

## Architecture decision — 31 July 2026

**Status:** adopted.

The project separates its working environment from its eventual article.
Project-owned Markdown artifacts, not raw conversation history, preserve
research, logical structure, claim status, decisions, and open work. Original
sources remain authoritative for their own content; summaries do not promote
source claims into project commitments. The article remains isolated until
prose is intentionally drafted for publication.

## Logical-tree separation — 2 August 2026

**Status:** adopted.

The existing `working/argument_map.md` is retained because it preserves useful
conceptual development, definitions, examples, qualifications, and research
history. It no longer owns the compact presentation structure. The separate
`working/logical_tree.md` owns article order, distinct claims, inferential
dependencies, critical bridge premises, and the final conclusion.

This boundary is deliberate: the expanded map may continue to accumulate
working knowledge, while the logical tree must remain short enough to expose
the argument at a glance and govern later drafting. Neither file is publication
prose.

## Logical-tree refinement — 3 August 2026

**Status:** adopted.

The logical tree remains the primary skeleton for drafting. It states the
article's governing explanation directly; its account of path validity
distinguishes generated rationales from evidence of actual transformations; and
its domain gradient and teaching constraint now precede and qualify the
innovation hypothesis. Full-draft generation should use the tree together with
the claims ledger, research summaries, and expanded argument map. A separate
paragraph-level outline remains optional.

## Coherence and source audit — 4 August 2026

**Status:** adopted as a revision of the working environment.

The logical tree now separates initial interpretation from later transition
validity, treats interpretation as context-sensitive and potentially plural,
admits fields partly constituted by language, and distinguishes object-level
discovery from representation-level revision. It also records alternative
explanations for degradation: search, computation, memory, ordinary task
difficulty, and a defective initial interpretation.

The targeted primary-source pass supplies examples and supporting evidence for contextual
latent-concept inference, compositional and length degradation, explicit
intermediate-state training, unfaithful generated rationales, and
state–search–evaluation discovery systems. The article's causal bridge is that
field-aligned training makes the relevant semantic structure more causally
effective during generation and thereby reduces invalid transitions under
complexity and depth. This is the proposed explanation and remedy; the sources
clarify its mechanisms and demonstrate realizable components.

Othello-GPT supports a narrower claim than the unrestricted statement “the
model learned the field,” but a stronger claim than behavioral approximation.
Its hidden state encodes task-relative board variables that targeted
counterfactual interventions can use to steer legal-move predictions, including
on unreachable boards. The example therefore demonstrates field-organized,
causally effective internal learning while leaving the philosophical boundary
between a learned field model and a field-corresponding predictive state open.

## Othello exemplar decision — 4 August 2026

**Status:** adopted as the article's clearest positive technical example.

David identifies Othello-GPT as an instance of the kind of learning the article
advocates: a sequence model develops an internal representation appropriate to
the represented domain rather than remaining confined to its surface token
representation. Nanda et al.'s follow-up strengthens the example by showing
that the internal categories are player-relative—`Mine`, `Yours`, and
`Empty`—and causally steerable through simple linear directions.

The article should use Othello to demonstrate internal field representation and
MetaOthello to extend the mechanism across notation and related rule systems.
It then advances the same principle across different and interacting domains:
a model should form or activate domain- and task-appropriate internal
representations and coordinate them. “One mechanism per domain” is not adopted
literally; the same Othello model appears to use several complementary
circuits. The governing principle is appropriate internal structure and valid
coordination, not a fixed one-to-one modular decomposition.

## Research decision — 31 July 2026

**Status:** retained as research background; its interpretation of the central
thesis was corrected on 2 August 2026. Publication prose remains undrafted.

The first source-grounded research pass is recorded in
`working/research_summaries.md`. It changes the argument in five ways:

1. Language-only models demonstrably recover bounded perceptual, spatial, and
   temporal structure. This finding does not correct or contradict the author's
   position, which never denied that language can represent world structure.
2. Identifiability and initial fidelity under specified evidence and validation
   conditions remain secondary limits. Reporting bias, abstraction, context
   dependence, and underspecification provide bounded cases; they do not
   directly test syntactical validity through semantic transformation.
3. “Further refinement produces noise” remains an open conditional hypothesis.
   Existing work on repeated data and recursive synthetic training is adjacent
   evidence, not a direct test of inference over fixed evidence.
4. Learned uncertainty and abstention are feasible but fallible under novelty
   and distribution shift. Confidence alone is not accepted as an epistemic
   stopping rule.
5. Libraries of reusable programs, modular learning, sparse routing, learned
   tool calls, and algorithm distillation already instantiate pieces of the
   proposed architecture. The research contribution must be a tested
   meta-criterion connecting search, consolidation, execution, abstention, and
   new-constraint acquisition.

These judgments are promoted into the claim ledger only at their stated bounded
scope. The neighboring Sutton/reception project and its source conversation
remain outside this evidence base.

## Author clarification — 2 August 2026

**Status:** adopted correction to the working thesis.

The 31 July synthesis misidentified the thesis as a possible denial that text
contains recoverable world structure. David's actual claim concerns what
happens **after** an extra-linguistic structure has been represented in
language. The representation remains faithful only insofar as subsequent
operations preserve the structural correlation that made it a representation.
Transformation according only to intra-linguistic grammar can retain linguistic
coherence while losing that correlation.

A provisional formal statement is:

- let `R_D` be a space of possible semantic states for field `D`;
- let `e_(D,c)` relate a linguistic expression and context to one or more states
  in `R_D`;
- let `T_D` specify the field's syntactically valid transitions between
  semantic states;
- a linguistic transformation from `l_1` to `l_2` is field-valid only when the
  selected interpretations stand in the relevant relation `T_(D,c)`.

The semantic state is expected to change from `e_D(l_1)` to `e_D(l_2)`; that is
the point of using language to reason. What must persist is the syntactical
validity of the transition. Linguistic well-formedness does not establish
membership in `T_D`.

## Core-thesis decision — 2 August 2026

**Status:** adopted as the organizing claim for the article.

David identified the transformation-fidelity account as the single explanation
linking why LLMs work, where they fail, and how to improve them. The operative
contrast is now:

- **contextual approximation:** infer from linguistic context how an expression
  is being used to represent an underlying field;
- **proxy drift:** as underlying structure or transformation chains become more
  complex, operations on the linguistic surface cease to track operations in
  the represented field reliably;
- **semantically grounded improvement:** train the model against appropriate
  representations of the resulting semantics in the relevant field, not only
  against further linguistic context.

The identifiability, uncertainty, abstention, modularity, and tool-use research
remains supporting material. It no longer supplies the article's central
explanatory structure.

## Core-thesis elaboration — 2 August 2026

**Status:** adopted.

Field-appropriate fidelity means maintaining the syntax that determines which
semantic transformations are valid in the represented field:

- in mathematics, each step must follow a valid mathematical transformation,
  even though it may produce a new expression or establish a new truth;
- in spatial reasoning, changes to objects, positions, orientations,
  containment, and other relations must follow the domain's valid state-update
  rules;
- in philosophy, the identity and function of premises, conclusions,
  distinctions, concepts, commitments, objections, and replies may develop,
  but their transformation must remain valid within the argument's structure.

Semantic meaning is not the invariant. Transforming meaning is the purpose of
the operation. What must remain intact is the syntactical validity of the move
from one semantic state to the next: the change must be licensed by the
represented field rather than merely by linguistic continuation.

Semantic-representation training is distinct from tool calling. Tool calling
routes an identified problem to an external procedure and often treats the
model as a suboptimal executor for that procedure. The thesis predicts that
mathematical, spatial, or argumentative-structure training can improve the
model's own reasoning even without a calculator or other external solver.
Accordingly, tool availability and semantic-representation training must be
tested as separate experimental variables.

Two additional limit predictions are adopted:

1. **Field interaction:** tasks combining multiple fields require the model to
   coordinate several semantic state spaces, transition syntaxes, and mappings;
   failures should cluster at field identification, switching, and interface
   points.
2. **Anchor decay:** the linguistic cue that selected the field also selected
   the relevant field syntax. When that cue falls outside the context
   window or loses effective influence within attention, later transformations
   should revert toward generic linguistic regularities and drift from the
   original field structure.

Humanities examples are especially revealing because a model can remain
rhetorically plausible while changing a premise's role, collapsing a
distinction, or importing a commitment the argument did not contain. Their
underlying structures may be plural or contestable, so the evidential target is
not one indisputable formalization but departure from defensible structural
bounds.

## Syntactical-validity correction — 2 August 2026

**Status:** adopted correction.

The earlier wording “preserve semantic invariants” was misleading. The model
should not preserve semantic meaning unchanged; producing a transformed
meaning is the point of inference. The persistent requirement is instead the
validity of the transformation under the syntax of the represented field.

Thus the architecture does not freeze a semantic representation. It maintains
or recovers the rules governing admissible transitions among semantic states.
Drift occurs when a transition is licensed by linguistic grammar or contextual
plausibility but not by the relevant mathematical, spatial, argumentative, or
other field syntax.

## Path-validity elaboration — 2 August 2026

**Status:** adopted.

A correct conclusion does not establish valid reasoning. For a semantic path
`r_0, r_1, ..., r_n`, correctness of the terminal state `r_n` is distinct from
the requirement that every transition `(r_i, r_(i+1))` belong to the active
field syntax `T_D`. A model may reach the right mathematical answer through an
invalid derivation, the right spatial endpoint through an impossible route, or
a plausible philosophical conclusion through premises that do not support it.

The project therefore distinguishes:

- **terminal correctness:** whether the final semantic state is acceptable;
- **path validity:** whether every semantic transition is licensed by the
  field;
- **valid success:** a correct endpoint reached through a valid path;
- **accidental or unwarranted success:** a correct endpoint reached after at
  least one field-invalid transition.

A generated explanation is not automatically evidence of the path the system
actually used; it may itself be a plausible post-hoc linguistic construction.
Testing must use explicit domain-state trajectories, stepwise interventions,
or other procedures that can reveal whether intermediate field structure
governs later transformations. Outcome-only benchmarks systematically miss the
defect at the center of the article.

## Deep innovation hypothesis — 2 August 2026

**Status:** adopted as the project's deepest hypothesis; strictly unestablished.

Training a model to represent semantic states and the field syntax of valid
transitions may do more than reduce error. It may allow the model to make
genuinely new inferences beyond plausible linguistic mimicry. A context-only
model is pulled toward continuations that resemble familiar linguistic uses.
A model able to search semantic states under an explicitly trained or learned
field syntax could
instead propose a transition that is linguistically unusual or absent from its
training examples while remaining valid in the represented field.

On this account, syntactical constraint is not the opposite of creativity. It
is what could make departure from linguistic precedent intelligible rather than
arbitrary. The field syntax supplies a space in which an unfamiliar semantic
path can be explored, checked, and developed without requiring it to resemble a
previously encountered verbal pattern.

This possibility must not be presented as an established consequence. A valid
new path can still be trivial, useless, or already implicit in training data.
Evidence would require all of the following:

1. novelty relative to training, retrieval, and available exemplars;
2. validity of every transition under the field syntax;
3. independent validation of the result in the represented field;
4. nontriviality or value by predeclared domain criteria; and
5. an advantage over a matched context-only model that cannot be explained by
   additional data, compute, tool access, or memorized templates.

The culminating empirical prediction is that semantic-state and field-syntax
training will increase the rate of **novel, valid, nontrivial** inferences—not
merely novel-looking language—relative to matched linguistic training alone.

### Chess illustration

Chess supplies the cleanest conceptual contrast. One model may play by
recognizing a position as similar to positions in a large corpus of human games
and producing a move typical of those examples. Another may represent the board
state, know the legal transition rules, search reachable positions, and evaluate
their strategic value. The second system can in principle choose a strong legal
move that no human in its evidence ever played.

The analogy separates four functions:

- the board representation supplies the semantic state;
- the rules supply the syntax of valid transformation;
- search explores semantic paths; and
- evaluation distinguishes promising novelty from merely unprecedented moves.

Rules alone do not produce intelligence or innovation: almost any legal but bad
move may be novel. The deep hypothesis requires field syntax to be joined to
search and a domain-sensitive value criterion. Its claim is that this
combination can generate valid possibilities beyond recognition and imitation
of familiar linguistic patterns.

### From chess to drama

Chess is the clearest rigid case, not the model for every field. In drama there
is no single exhaustive rulebook or binary test of legality. The relevant
structure includes characters and their knowledge, desires and conflicts;
causal and temporal relations; scene functions; setup and payoff; shifts in
tension; thematic patterns; genre expectations; and the audience's developing
understanding.

The same principle nevertheless applies. A model that only recognizes verbal
patterns from previous stories may generate prose that resembles drama. A model
that represents the evolving dramatic state and the context-sensitive syntax
of valid dramatic transformation could develop that state deliberately and may
therefore write a good story rather than merely a familiar-sounding one.

For a soft domain, `T_D` should be understood as a contextual family `T_(D,c)`
of defensible transformations, where `c` includes genre, tradition, purpose,
and interpretive frame. Constraints may be graded, plural, and revisable. A
convention can be violated when the violation itself has an intelligible
dramatic function; the test is not conformity but structurally warranted
development.

This soft-domain extension increases the evidential burden. “Good story” cannot
be reduced to syntactical validity, and no one representation or evaluator
should be treated as definitive. The innovation hypothesis would require
coherent transformation of dramatic structure, nontrivial aesthetic value, and
judgment across multiple defensible critical perspectives—not merely fluent
prose or compliance with a formula.

### The teaching bottleneck

The proposed architecture does not escape representation. A model can learn a
field's abstract structure only insofar as that structure is successfully
represented in its training signal—linguistically, formally, demonstratively,
interactively, or through another explicit and discriminating form. Structured
representations can carry distinctions that prose alone carries poorly, but
they must still be designed, produced, or elicited.

Accordingly, the difficulty of semantic-state and field-syntax training should
increase as humans become less able to:

1. identify the relevant semantic states;
2. state or demonstrate valid and invalid transformations;
3. agree on the contextual conditions governing those transformations; and
4. evaluate the quality of unfamiliar results consistently.

This is not a claim that every rule must be verbalized. Demonstrations,
counterexamples, critiques, simulations, environmental consequences, and
iterative expert judgments may embody structure that people cannot state as a
compact rule. But if the teaching signal neither expresses nor reliably
discriminates a structural distinction, the model has no dependable basis for
learning it.

The remedy therefore introduces its own principled limit: improvement is
bounded by the articulability, demonstrability, and evaluability of the field's
structure. Chess is comparatively easy to teach because states and legal
transitions are explicit. Drama is harder not because it lacks structure, but
because that structure is plural, tacit, context-sensitive, and difficult even
for humans to specify and judge consistently.

### Latent-structure discovery hypothesis

**Status:** adopted as a hope and research hypothesis; not an established
capability.

The fields hardest to teach may also offer the greatest opportunity for a
properly used model. Within a field or paradigm already identified by humans,
recurring structure can be distributed across examples, practices, partial
theories, criticisms, and expert judgments without having been made explicit as
one representation or rule system. A model's scale and contextual reach may let
it detect high-dimensional patterns across more cases and interacting relations
than unaided human cognition can grasp at once. It may then use those patterns
or help propose partial representations of them.

This is a second level of the innovation hypothesis:

1. **Object-level discovery:** find a new valid path within a sufficiently
   specified `R_D` and `T_D`.
2. **Latent-structure discovery:** within an already identified field, propose a
   candidate `R_D`, `T_(D,c)`, or value framework for regularities that remain
   partly tacit or too complex for humans to grasp directly.

This does not claim that the model autonomously identifies, selects, revises,
or replaces the field's paradigm. The paradigm supplies the rule-constituting
scope within which pattern discovery begins.

The second level also does not escape the teaching bottleneck. The candidate structure
must be recoverable from some evidence, and the model cannot establish its own
proposal merely by making it coherent. Proper use requires candidate generation
rather than immediate adoption: preserve source provenance, produce rival
formulations, test cases and counterexamples, seek predictions or fruitful new
questions, compare explanatory compression, and revise under human and domain
feedback.

The central danger is persuasive projection: an elegant linguistic scheme may
organize ambiguous material without corresponding to a valuable underlying
structure. A candidate earns provisional confidence only if it discriminates
meaningful cases, survives adversarial examples, improves explanation or
generation, transfers beyond the examples that suggested it, and remains
contestable by alternative interpretations.

Full human comprehension of the detected pattern may not be immediately
possible. In that case, value must be established indirectly through stable
held-out discrimination, successful prediction or generation, intervention,
transfer, compression into partial inspectable models, and reproducible gains
over simpler accounts. The model should function as an instrument for detecting
structure, not as an oracle whose inaccessible pattern is accepted on
authority.

Thus underdefinition is both the largest obstacle and the possible site of the
largest gain. The hypothesis is that a properly governed model can help turn
tacit regularity into an explicit, testable proposal—not that whatever pattern
it articulates should be treated as a discovery.

### Author experience: tacit writing style made explicit

**Status:** author-reported illustration, not general empirical evidence.

David recalls asking a model to analyze his writing style. The model articulated
rules and patterns he had never consciously used, yet he recognized them once
they were pointed out. The sequence exemplifies the proposed mechanism:

1. the writing already enacted recurring structure;
2. the model detected and articulated candidate regularities across the texts;
3. the author's first-person recognition supplied an independent kind of check;
4. tacit practice became an explicit and revisable representation.

This is stronger than the model merely producing a flattering description, but
recognition alone is not decisive evidence. A rigorous version would test
whether the proposed rules discriminate unseen writing, predict stylistic
choices, survive counterexamples, and guide new writing in the same style
without copying phrases. The original analysis should be retrieved before any
specific stylistic rule is quoted or attributed in publication.

As a working illustration, the episode shows the hoped-for use of model
strength in a soft domain: not replacing the author's judgment, but making
previously unconscious structure available for recognition, correction,
testing, and deliberate use.

### Statistical validation without exhaustive comprehension

**Status:** adopted methodological principle.

A model-discovered structure may be too complex for exhaustive human inspection
or may concern a population too large to check case by case. It can still be
tested like another scientific hypothesis if it yields observable predictions.
The project does not require humans to grasp every component of the pattern
before testing whether it generalizes reliably.

The minimum protocol is:

1. use one body of evidence for discovery;
2. freeze the candidate hypothesis, predictions, and failure criteria;
3. define the target population and sampling frame;
4. draw an independent random sample, or a predeclared stratified sample where
   important regimes would otherwise be missed;
5. evaluate predictions blindly where possible; and
6. report estimated error, uncertainty, evaluator disagreement, and the scope
   of the population to which the result generalizes.

In a soft domain, labels may themselves be plural or uncertain. Validation may
therefore require multiple independent evaluators, a declared range of
defensible judgments, inter-rater analysis, and separate reporting for disputed
cases. Sampling can estimate reliability over the specified population; it
does not prove a universal rule, establish causation without intervention, or
guarantee performance after distribution shift.

This closes an important epistemic gap in the latent-structure hypothesis.
Human comprehension need not scale to every case, but validation can scale by
sampling. The model remains an instrument whose claims earn confidence through
precommitted, reproducible tests rather than through opacity or authority.

### Weather forecasting as a test field

**Status:** adopted as a candidate structured-empirical example; existing AI
weather results are supporting precedent, not a direct test of the LLM thesis.

David's phrase “weather forecast” identifies a possible field in which
model-detected patterns can be tested. Weather is unusually useful because the
field is defined independently of language, atmospheric states have explicit
multivariate spatial representations, transformations unfold through time, and
new outcomes arrive continuously. A candidate regularity can therefore be
frozen as a set of probabilistic forecasts and evaluated prospectively against
later observations or analyses.

The relevant inference is not “the model issued a weather forecast, therefore
it discovered the governing structure.” Predictive skill can show that a
learned regularity captures usable information without showing that the model
has articulated an interpretable meteorological rule, identified a causal
mechanism, or learned every physically valid transition. The case must
distinguish three achievements:

1. **opaque pattern use:** a learned representation improves held-out forecast
   skill;
2. **explicit structure discovery:** the model proposes a meteorological
   relation or representation with frozen observable consequences; and
3. **field-valid dynamics:** forecast trajectories also satisfy relevant
   physical, cross-variable, spatiotemporal, and probabilistic constraints.

Existing weather models show why the example fits the article. GraphCast
autoregressively transforms a structured atmospheric state rather than a
verbal description. Pangu-Weather adds Earth-specific three-dimensional priors
and changes temporal aggregation to reduce accumulated forecast error.
NeuralGCM places learned components inside a differentiable dynamical solver,
providing a direct example of learned pattern strength combined with
field-governed transformations. GenCast represents distributions of possible
trajectories rather than treating one deterministic continuation as the field's
only valid future.

Weather also sharpens the sampling principle. Forecast cases are spatially and
temporally dependent, rare extremes matter disproportionately, and climate or
operational regimes can shift. Validation should therefore use temporally
separated prospective or held-out periods, event- and regime-stratified
analysis, appropriate deterministic and probabilistic scores, and explicit
checks of physical consistency. This is a more rigorous version of the
author's point that even a pattern too complex for exhaustive human
understanding can be tested through sampled consequences.
