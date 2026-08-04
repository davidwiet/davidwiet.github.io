# External Research Summaries

Status: active research record.

This file records externally verifiable research relevant to the article. It
is organized around research questions rather than the order in which searches
were performed. A source's inclusion does not make its claims part of the
article.

## Entry standard

Each substantive entry should record:

- the research question;
- full source identity and stable link;
- source type and why it is authoritative for the point at issue;
- publication date and the date last checked;
- a concise account of what the source establishes;
- material limitations, qualifications, or counterevidence;
- which project claim or open question it bears on;
- project use status: `background`, `candidate evidence`, `adopted evidence`,
  `counterevidence`, or `excluded`.

Paraphrases and direct quotations must be distinguishable. Page, section, or
paragraph locations should be recorded whenever the source permits.

## Current research agenda

### Transformation fidelity

- What structural relation makes a linguistic representation faithful to a
  field-specific semantic structure, and which transformations preserve that
  relation?
- Does greater linguistic context improve performance by helping models infer
  a latent field, representational practice, or mapping from language into a
  field-specific semantic structure?
- What existing work distinguishes transformations licensed by a field's
  semantic-state transition syntax from transformations licensed only by
  linguistic well-formedness?
- Does representational fidelity measurably decay through chained
  intra-linguistic transformation even while fluency, coherence, or confidence
  remains stable?
- How do structural complexity and reasoning-chain length independently and
  jointly affect that decay?
- Which forms of formal execution, retrieval, perception, action, or checking
  preserve or renew the original representation–world correlation?
- Which training objectives align language with field-appropriate semantic
  representations, and do they improve systematic generalization or long-chain
  fidelity over matched context-only training?
- How can semantic-representation training be experimentally separated from
  tool routing and external execution?
- What failure signatures arise when several field representations must be
  composed, and which errors occur at their interfaces?
- Does distance from, interference with, or removal of a field-defining anchor
  cause measurable reversion toward generic linguistic priors?
- In philosophy and other humanities fields, which structural properties can
  be evaluated across multiple defensible interpretations without pretending
  that the domain has one uncontested formalization?
- How often do models reach correct endpoints through field-invalid
  intermediate transitions, and how does that rate change with complexity and
  chain length?
- Which forms of process supervision, step verification, intervention, or
  explicit state tracking measure the transformations actually used rather
  than the plausibility of a retrospective rationale?
- What operational tests distinguish genuine novel inference from memorization,
  retrieval, paraphrase, template recombination, or rediscovery?
- Does training over semantic states and field-valid transitions increase the
  rate of novel, valid, nontrivial discoveries over matched context-only
  training, or does it only improve reliability on familiar problems?
- How do state representation, valid-transition rules, search, and domain value
  each contribute to innovation, and can their effects be separated?
- How can the state–syntax–search–value framework be generalized from rigid
  domains to drama and other fields with plural, graded, contextual, and
  historically variable constraints?
- Can structural story competence be separated experimentally from imitation
  of genre, style, familiar plots, and evaluators' retrospective preferences?
- How does the articulability, demonstrability, and evaluability of a field's
  structure constrain the learnability of its semantic states and transition
  syntax?
- Which combinations of definitions, formal representations, demonstrations,
  counterexamples, interaction, consequences, and expert feedback best transmit
  tacit or contested field structure?
- Within a human-identified paradigm, can model scale recover stable complex
  regularities that humans cannot grasp unaided, and can those regularities be
  converted into testable partial representations?
- Which validation methods distinguish valuable latent structure from spurious
  high-dimensional pattern and persuasive projection?
- Can model-articulated writing-style rules predict or discriminate unseen
  writing and guide controlled generation, beyond eliciting retrospective
  recognition from the author?
- Which sampling designs can validate complex model-discovered structures at
  scale without exhaustive human inspection, while controlling discovery bias,
  label uncertainty, rare regimes, and distribution shift?

### Language as a representational medium

- What kinds of world structure are recoverable from linguistic distribution
  alone?
- Which limitations attributed to language models are limitations of language,
  training objectives, model architecture, available modalities, or
  evaluation?
- What would count as evidence against a principled language-resolution limit?

### Learning, consolidation, and execution

- Which existing architectures distinguish discovery or search from
  consolidation and reusable execution?
- Under what conditions does compiling or hardening a learned regularity reduce
  cost or improve reliability?
- How do program synthesis, modular learning, mixture-of-experts systems,
  tool-using models, and continual learning bear on the proposal without being
  treated as equivalent to it?

### Epistemic stopping and uncertainty

- How do current systems detect that further discrimination is unsupported?
- What adjacent work exists on underdetermination, calibration, abstention,
  representation collapse, irreducible error, and the bias-variance tradeoff?
- Can an epistemic stopping condition be stated operationally without assuming
  access to ground truth?

### Multimodality and world involvement

- Which purported language limits are changed by perception, action,
  experimentation, retrieval, or formal computation?
- Does moving beyond language supply new evidence, a new representation, a new
  verification procedure, or all three?

## Author-position correction — 2 August 2026

The first research pass treated “language can recover world structure” as
counterevidence to a possible project claim. David clarified that he never
disputed this. His thesis concerns the **endurance** of that representational
relation through transformation: linguistic material can faithfully encode an
extra-linguistic structure, yet a transformation licensed by intra-linguistic
grammar need not preserve the structural correlation that gave the original
encoding its fidelity.

Accordingly, the sources below remain relevant but answer mostly preliminary or
secondary questions. The color, space, and time studies support the premise that
language can carry world structure. Reporting bias and underspecification show
other ways correlations can be incomplete or unstable. Neither body of work
directly tests whether chained transformations within a linguistic system
preserve an initially faithful extra-linguistic correlation. That is the new
priority for the next source pass.

## Core-thesis adoption — 2 August 2026

David identified one mechanism as the answer to all three questions in the
provisional title:

- LLMs work because large contexts often let them approximate how language is
  being used to represent structures in another field.
- Their limit appears as underlying structure becomes more complex or the
  reasoning chain becomes longer: the linguistic surface becomes a worse proxy
  until its correlation with the represented structure is no longer reliable or
  meaningful.
- Improvement requires training models to infer uses of language in relation to
  field-appropriate representations of the resulting semantics, not from
  linguistic context alone.

This is an adopted author position, not a conclusion of the 31 July source
pass. That pass supports its initial premise—that language can carry
world-correlated structure—and supplies adjacent work on uncertainty, tools,
and modular execution. It does not yet establish the proposed contextual
mechanism, complexity/depth degradation curve, or semantic-representation
remedy. Those three empirical burdens now define the next deep-research pass.

## Core-thesis elaboration — 2 August 2026

The field-appropriate representation must expose the syntax governing valid
semantic change: mathematical derivation, spatial state transition, or the
development of premises, concepts, distinctions, commitments, objections, and
replies within a philosophical argument. Semantic meaning is supposed to
change. The persistent requirement is that the transition be licensed and
tracked within the represented field rather than generated only by linguistic
plausibility.

This makes semantic-representation training categorically distinct from tool
calling. Tool calling classifies and routes an operation to an external
executor. The core proposal predicts improvement in the model's own reasoning
from mathematical, spatial, argumentative, or other semantic training even
when no calculator or specialist tool is available. A tool may later execute or
verify such a representation, but that is a separate variable. Relevant studies
must therefore distinguish at least four conditions: context-only/no tool,
context-only/tool, semantic training/no tool, and semantic training/tool.

Two further predictions now belong to the research program:

1. Intertwined fields should create distinctive selection, switching, and
   interface errors because several representation systems and mappings must be
   coordinated simultaneously.
2. If the original anchor that selected the field and its transformation syntax
   becomes
   distant, attentionally ineffective, or unavailable outside the context
   window, subsequent output should increasingly follow generic language
   regularities rather than the original domain structure.

Humanities cases offer a demanding test: rhetorical plausibility can survive
while the model changes a premise's role, erases a distinction, or imports a
commitment. Because the underlying structure may be genuinely contested, the
research standard should be departure from a predeclared range of defensible
analyses, not disagreement with one supposedly definitive formalization.

These are adopted author claims and research directions. They have not yet
received a targeted external-source pass.

## Syntactical-validity correction — 2 August 2026

David corrected the phrase “semantic preservation.” The model should transform
semantic meaning; that is the purpose of using language in reasoning. What must
remain valid is the **syntax of the transformation** in the represented field.
A mathematical expression may change, a spatial state may change, and an
argument may develop substantially, provided each transition is licensed by the
relevant mathematical, spatial, or argumentative syntax.

The next source pass must therefore search for domain-valid transition
structures, compositional or type-preserving transformations, and training
objectives that distinguish field-valid semantic change from fluent but
unlicensed linguistic continuation. Work framed merely as “semantic
consistency” is relevant only if it permits semantic development rather than
treating unchanged meaning as the success criterion.

## Path-validity elaboration — 2 August 2026

David added that the conclusion itself may be correct while the route remains
defective: “how on earth did he get there?” The project must therefore evaluate
semantic trajectories, not only terminal answers. For a path
`r_0, r_1, ..., r_n`, terminal correctness concerns `r_n`; field-valid
reasoning requires every `(r_i, r_(i+1))` to belong to `T_D`.

This creates a distinct error category: a correct endpoint after one or more
field-invalid transitions. Such an answer may be accidental, unwarranted, or
brittle even though ordinary accuracy metrics count it as correct. The targeted
research pass should examine process supervision, step-level verification,
shortcut solutions, causal faithfulness of rationales, and methods for exposing
intermediate domain states.

A visible chain of thought is not sufficient evidence. It can be another
linguistically plausible construction rather than the process responsible for
the answer. Candidate evaluations should therefore report terminal accuracy,
valid-success rate, correct-endpoint/invalid-path rate, location of the first
invalid transition, and robustness to perturbations designed to break lucky or
shortcut solutions.

This is an adopted author claim and research direction. It has not yet received
a targeted external-source pass.

## Deep innovation hypothesis — 2 August 2026

David identified the project's deepest idea, explicitly and strictly as a
hypothesis: field-appropriate semantic representations and transformation
syntax may allow a model to make genuinely innovative inferences that transcend
plausible mimicry. Rather than selecting a continuation because it resembles
familiar language, the model could explore a semantic move because it is valid
in the represented field, even when that move is linguistically unusual or has
no close exemplar.

Syntactical constraint is therefore hypothesized to enable rather than suppress
creativity. It could let a system depart from linguistic precedent without
departing from intelligibility. This does not follow automatically from the
earlier claims: valid search can remain derivative or generate endless trivial
results.

Any evidential test must keep four gates separate:

1. novelty relative to training data, retrieval, and provided exemplars;
2. field validity of the entire transformation path;
3. independent correctness of the result; and
4. nontrivial value under predeclared domain criteria.

The comparison must match data, compute, search budget, and tool access. The
hypothesis earns support only if semantic-state and field-syntax training raises
the rate of results passing all four gates relative to context-only training.
Improved accuracy, calibration, or path validity without increased validated
novelty would support the practical architecture while leaving the innovation
hypothesis unsupported.

This claim has not yet received a targeted external-source pass. Relevant
research lanes include computational creativity, novelty measurement, theorem
and algorithm discovery, program synthesis, scientific hypothesis generation,
open-ended search, and evaluations designed to exclude memorization and data
contamination.

### Chess illustration

David proposed chess as the clearest analogy. A corpus-trained model may play by
recognizing a position as similar to positions in many previous games and
selecting a move associated with those examples. A model given an explicit
board representation and legal transition rules can instead search possible
positions and may select a legal move no human in its evidence ever made.

The analogy decomposes the proposed architecture into semantic state, valid
syntax, search, and value. It also supplies a necessary limitation: the rules
alone permit countless unprecedented but strategically poor moves. Innovation
requires novelty and legality to be joined to a field-sensitive evaluation of
nontrivial value.

This is an adopted conceptual illustration, not external evidence for C23. A
targeted source pass should examine rule-grounded self-play and search systems,
novel-move attribution, contamination-resistant game benchmarks, and whether
the chess mechanism transfers to fields whose states, rules, and value criteria
are learned, plural, or contested.

### Drama as the soft-domain complement

David generalized the chess principle to domains with less clear and rigid
rules: if a model understood the underlying structure of drama, it could write
a good story. Here “understood” cannot mean following one formula. A dramatic
state may include character knowledge, desires and conflicts; causal and
temporal dependencies; scene functions; setup and payoff; tension; theme;
genre; and the audience's evolving understanding. Valid development depends on
context and may include purposeful violation of a convention.

The working formalism therefore changes from a single binary transition
relation `T_D` to a contextual family `T_(D,c)` of defensible transformations.
The context `c` may include genre, tradition, purpose, and interpretive frame.
Admissibility and value can be graded and plural without becoming arbitrary,
provided the constraints and range of defensible readings are specified before
evaluation.

This analogy produces a difficult empirical contrast. A pattern model can write
fluent prose resembling stories. A structure-sensitive model should maintain
and deliberately transform the dramatic state across surface styles and novel
plots, while avoiding unearned reversals, forgotten causes, unmotivated
character actions, and thematic conclusions unsupported by the dramatic path.
Evaluation must separate structural coherence from formula compliance and use
multiple defensible value judgments rather than one supposedly objective story
score.

This is an adopted soft-domain hypothesis, not external evidence for C25. The
next source pass should examine computational narrative intelligence, story and
discourse representations, plot and character-state tracking, causal narrative
models, computational creativity, process-based story evaluation, and evidence
about whether current generative models imitate surface patterns or maintain
long-range dramatic structure.

### The teaching bottleneck

David added a second-order limit: even the proposed remedy requires the field's
abstract structure to be represented successfully in a teaching signal. The
less well-defined the relevant states, transformations, and values are for
humans, the harder it should be to teach them to a model.

The teaching signal need not be a verbal rulebook. It may include formal
representations, demonstrations, counterexamples, critiques, simulation,
interaction, environmental consequences, and repeated expert judgments. But
these routes do not escape the representational requirement. The signal must
embody or discriminate the structural distinction the model is expected to
learn.

This predicts a domain gradient: explicit formal domains should support the
clearest supervision and validation; structured empirical domains add
measurement and modeling uncertainty; interpretive domains add tacitness,
plurality, contextual dependence, and evaluator disagreement. The same
architecture may apply throughout, but its attainable fidelity is bounded by
the quality of the available teaching signal.

This is an adopted author hypothesis, not external evidence for C26. The next
source pass should examine tacit knowledge, learning from demonstration and
preferences, concept and reward specification, inter-annotator disagreement,
weak supervision, inverse modeling of latent rules, and identifiability when
training examples underdetermine the governing structure.

### Latent-structure discovery within an identified field

David supplied the positive counterpart to the teaching bottleneck: the very
fields whose structure humans cannot define clearly may be where a properly
used model yields the most valuable insights. Model scale may detect complex
patterns distributed across more examples, dimensions, and interacting
relations than humans can grasp unaided.

The current scope begins after humans have identified the field or paradigm. It
does not claim that the model can autonomously identify, select, revise, or
replace paradigms. Within that scope, the model may propose semantic states,
distinctions, transition structures, interfaces, or value criteria that make
previously tacit regularities available for testing.

This is compatible with the teaching bottleneck. The evidence must still
contain the regularity, even if no human has compressed it into an explicit
rule. The model supplies candidate abstraction, not structure ex nihilo.

The main danger is persuasive projection: a complex model can impose an elegant
pattern on ambiguous material. Candidate structures therefore need rival
formulations, preserved provenance, counterexamples, and tests of held-out
discrimination, prediction or generation, intervention, transfer, explanatory
compression, and practical or intellectual fruitfulness. If the full pattern
remains opaque, reproducible external effects and partial inspectable
projections must substitute for trust in the model's authority.

This is an adopted author hope and empirical hypothesis, not evidence for C27.
The next source pass should examine representation discovery, disentanglement,
scientific discovery from high-dimensional data, interpretable and concept-
based modeling, mechanistic and causal validation of latent variables, model-
assisted theory formation, and the epistemology of instrument-mediated patterns
that exceed unaided human cognition.

### Author-reported writing-style illustration

David recalls asking a model to analyze his writing style. It supplied rules
and patterns he had never consciously applied, yet he recognized them once they
were articulated. This is a compact example of latent structure becoming
explicit: the corpus instantiated the pattern, the model proposed an
abstraction, and the practitioner recognized something in the abstraction that
had previously remained tacit.

The episode is an author report, not external evidence for the general
hypothesis. Recognition may be informative first-person evidence, but it can
also be influenced by vague formulation, suggestion, or confirmation bias. A
stronger study would preregister the extracted rules and test whether they
classify unseen passages, predict stylistic choices, withstand counterexamples,
or guide new text that independent readers recognize as structurally similar
without phrase copying.

The original analysis and its specific rules have not been retrieved into this
project. They should be recovered before the article quotes, paraphrases, or
attributes any particular finding. **Use status:** `candidate illustration`,
not `adopted evidence`.

### Statistical validation by sampling

David observed that even a claim requiring large-scale validation can be tested
through random sampling like another scientific hypothesis. This provides a
concrete validation route for patterns too complex for exhaustive human
comprehension or too broad for case-by-case inspection.

The hypothesis must first be operationalized into observable predictions.
Discovery and confirmation then need separate evidence: freeze the claim and
failure criteria after discovery, declare the target population and sampling
frame, draw an independent random or stratified sample, evaluate predictions
blindly where possible, and report uncertainty and scope.

Soft domains add label uncertainty. A defensible design may require multiple
independent evaluators, stratification across genres or interpretive regimes,
an admissible range of judgments, and explicit reporting of disagreement. The
sampling result generalizes only to the represented population; it does not
establish a universal rule, a causal mechanism without intervention, or
robustness under untested shifts.

This is an adopted methodological principle, not an empirical result for C29.
The next source pass should examine statistical learning and generalization,
holdout and preregistration practices for model-generated hypotheses, selective
inference and multiple testing, probability and stratified sampling, power and
uncertainty, evaluator reliability, and validation of opaque predictive models.

## Focused research pass — 2 August 2026: weather forecasting as a test field

### Question and adopted interpretation

David identified weather forecasting not as a request for a forecast but as a
possible field in which a model can detect patterns that humans cannot grasp
and those patterns can nevertheless be tested. The factual question is whether
current AI weather research shows this combination of high-dimensional learned
regularity, field-appropriate representation, repeated transformation, and
external validation. The interpretive question is what such results would and
would not establish for the article's latent-structure hypothesis.

### Evidence

#### GraphCast: structured state trajectories learned from reanalysis

- **Source:** Remi Lam et al., “[Learning skillful medium-range global weather
  forecasting](https://www.science.org/doi/10.1126/science.adi2336),”
  *Science* 382 (2023), pp. 1416–1421; official
  [Google DeepMind record](https://deepmind.google/research/publications/22598/).
- **Type / checked:** peer-reviewed primary paper and official author record;
  checked 2 August 2026.
- **Finding:** GraphCast represents atmospheric state through 227 dynamic
  variables on a 0.25-degree grid and multi-scale graph, then autoregressively
  predicts six-hour transitions over ten days. The authors report better
  performance than ECMWF HRES on 89.3% of 2,760 evaluated variable/lead-time
  targets.
- **Project bearing:** direct precedent for learning transformations over
  explicit non-linguistic semantic states and testing the result against later
  atmospheric states. It does not show that the learned transition can be
  stated as a new meteorological rule. **Use status:** `supporting precedent`
  for C30, not direct evidence for C27.

#### Pangu-Weather: domain priors and accumulated transition error

- **Source:** Kaifeng Bi et al., “[Accurate medium-range global weather
  forecasting with 3D neural
  networks](https://www.nature.com/articles/s41586-023-06185-3),” *Nature* 619
  (2023), pp. 533–538.
- **Type / checked:** peer-reviewed primary paper; checked 2 August 2026.
- **Finding:** Pangu-Weather maps reanalysis states to later reanalysis states,
  uses an Earth-specific three-dimensional architecture to represent relations
  across pressure levels, and uses hierarchical temporal aggregation to reduce
  cumulative error over medium-range rollouts. The paper reports stronger
  deterministic results than the operational ECMWF system on its tested
  reanalysis variables.
- **Project bearing:** unusually close precedent for the article's coupled
  claims that field-appropriate representation improves transformation and
  that iterated local error accumulates with chain length. Its evidence concerns
  weather models, not language models. **Use status:** `candidate evidence` for
  the general mechanism and `supporting precedent` for C30.

#### NeuralGCM: learned regularity inside field-governed dynamics

- **Source:** Dmitrii Kochkov et al., “[Neural general circulation models for
  weather and climate](https://www.nature.com/articles/s41586-024-07744-y),”
  *Nature* 632 (2024), pp. 1060–1066.
- **Type / checked:** peer-reviewed primary paper; checked 2 August 2026.
- **Finding:** NeuralGCM combines a differentiable solver for large-scale
  atmospheric dynamics with learned components for unresolved processes. The
  authors report competitive weather forecasts, physically consistent
  trajectories, and stable multiyear simulations, while also reporting limits
  under substantially different future climates.
- **Project bearing:** a concrete synthesis of the article's two attractions:
  learned high-dimensional pattern strength and transformations constrained by
  known field syntax. It also shows that performance, physical consistency,
  long-rollout stability, and out-of-distribution generalization are distinct
  tests. **Use status:** `candidate architectural precedent`.

#### GenCast: the target is a distribution of valid futures

- **Source:** Ilan Price et al., “[Probabilistic weather forecasting with
  machine learning](https://www.nature.com/articles/s41586-024-08252-9),”
  *Nature* 637 (2025), pp. 84–90.
- **Type / checked:** peer-reviewed primary paper; checked 2 August 2026.
- **Finding:** GenCast generates stochastic fifteen-day ensembles covering more
  than 80 surface and atmospheric variables. The authors report greater skill
  than ECMWF ENS on 97.2% of 1,320 evaluated targets and stronger results for
  extremes, cyclone tracks, and wind-power applications.
- **Project bearing:** weather exposes an important correction to a simplistic
  `T_D`: because initial conditions are partial and atmospheric dynamics are
  nonlinear, the field-valid target is often a calibrated distribution of
  trajectories, not one uniquely correct next state. **Use status:** `candidate
  evidence` for probabilistic field syntax and `supporting precedent` for C30.

#### WeatherBench 2: reproducible testing requires plural metrics

- **Source:** Stephan Rasp et al., “[WeatherBench 2: A benchmark for the next
  generation of data-driven global weather
  models](https://research.google/pubs/weatherbench-2-a-benchmark-for-the-next-generation-of-data-driven-global-weather-models/),”
  arXiv:2308.15560 (2023), with the maintained
  [evaluation site](https://sites.research.google/gr/weatherbench/).
- **Type / checked:** benchmark paper, public evaluation framework, datasets,
  and code; checked 2 August 2026.
- **Finding:** WeatherBench 2 compares physics-based and learned forecasting
  systems through public ground truth, baselines, deterministic and
  probabilistic scores. Its maintainers explicitly caution that no single
  metric captures forecast quality.
- **Project bearing:** supports the author's validation principle while
  refining “random sampling.” Weather cases are temporally and spatially
  dependent and rare regimes matter. A test should use held-out or prospective
  temporal blocks, event/regime stratification, uncertainty-sensitive metrics,
  and physical-consistency checks. **Use status:** `methodological support`.

### Bounded synthesis

Weather forecasting is a particularly strong example for C27–C30 because it
joins a field specified independently of the model, explicit structured states,
high-dimensional interactions, repeated transformations, and an external
stream of later outcomes. Current results establish that learned systems can
extract and use atmospheric regularities whose full operative form is not
manually programmed, and can be tested reproducibly at scale.

They do **not** yet establish the article's deepest discovery claim. Forecast
skill validates useful prediction, not necessarily a newly articulated
structure, causal mechanism, or humanly intelligible rule. Moreover, most
systems learn from ERA5 reanalysis, which already combines observations with a
physics-based assimilation and modelling system; the supplied representation
and target are not raw, theory-free reality. The strongest use of the example
is therefore two-level:

1. weather forecasting already demonstrates **opaque latent-pattern use** in a
   field-appropriate representation; and
2. a future test could ask whether a model proposes an **explicit candidate
   structure** that produces preregistered gains, transfers across held-out
   regimes, survives physical and intervention-based checks, and adds value
   beyond strong learned and physics-based baselines.

## Research pass — 31 July 2026

### Scope and method

This pass tested four questions: whether text alone preserves world structure;
whether there are identifiable limits to what it preserves; whether a model can
recognize such a limit; and whether existing architectures already instantiate
the proposed separation of discovery, consolidation, execution, and recourse to
other evidence. Searches prioritized peer-reviewed papers and official
conference or journal records. Two unreviewed papers are retained because they
state influential opposing positions; their status is marked explicitly.

The main result establishes useful background rather than correcting the
author's position. The evidence shows that textual distributions transmit
substantial indirect world structure, while selective reporting can leave
distinctions underdetermined, distorted, or unstable under deployment
conditions. Present uncertainty methods can sometimes detect error risk, but
they do not yet identify the cause as a limit of evidence, representation,
learning, transformation fidelity, or decision. Existing systems also implement
many proposed architectural pieces in bounded settings. A targeted second pass
must now test the distinct claim that contextual approximation of a field
becomes less faithful with structural complexity and transformation depth, and
that field-appropriate semantic representations reduce this degradation.

### 1. What world structure is recoverable from language?

#### Bender and Koller: form, communicative intent, and meaning

- **Source:** Emily M. Bender and Alexander Koller, “[Climbing towards NLU: On
  Meaning, Form, and Understanding in the Age of Data](https://aclanthology.org/2020.acl-main.463/),”
  *Proceedings of ACL 2020*, pp. 5185–5198,
  [doi:10.18653/v1/2020.acl-main.463](https://doi.org/10.18653/v1/2020.acl-main.463).
- **Type / checked:** peer-reviewed position paper; checked 31 July 2026.
- **Finding:** the paper distinguishes linguistic form from communicative
  meaning and argues, through its “octopus test,” that a system trained only on
  form has no direct access to communicative intent or the relation between
  expressions and a shared world.
- **Limit:** this is an analytic argument and constructed thought experiment,
  not an empirical demonstration that a text-trained model can recover no
  semantic or perceptual structure. It is also contested by conceptual-role
  accounts of meaning.
- **Project bearing:** clarifies the strongest version of C3, but does not by
  itself establish it. **Use status:** `background` and `candidate evidence`.

#### Merrill et al.: a formal model of learning meaning from form

- **Source:** William Merrill, Yoav Goldberg, Roy Schwartz, and Noah A. Smith,
  “[Provable Limitations of Acquiring Meaning from Ungrounded
  Form](https://arxiv.org/abs/2104.10809),” *Transactions of the Association for
  Computational Linguistics* 9 (2021), pp. 1047–1060,
  [doi:10.1162/tacl_a_00412](https://doi.org/10.1162/tacl_a_00412).
- **Type / checked:** peer-reviewed formal analysis; checked 31 July 2026.
- **Finding:** in the authors' formal setting, distributional learning can
  emulate a semantics when assertion behavior is sufficiently transparent.
  They also construct context-dependent value languages for which semantic
  emulation from assertions is uncomputable. This is useful because it turns a
  general grounding dispute into conditions under which meaning is or is not
  identifiable from observable form.
- **Limit:** the paper explicitly works with idealized language users and formal
  languages. Its impossibility result is not a theorem that natural language or
  current LLMs necessarily have the same limit.
- **Project bearing:** supports a bounded version of C2–C3 and the need to define
  recoverability relative to evidence, task, and decoder. **Use status:**
  `candidate evidence`.

#### Piantadosi and Hill: the conceptual-role counterposition

- **Source:** Steven T. Piantadosi and Felix Hill, “[Meaning without reference
  in large language models](https://arxiv.org/abs/2208.02957)” (arXiv preprint,
  revised 2023).
- **Type / checked:** unreviewed argumentative preprint; checked 31 July 2026.
- **Finding:** the authors argue that inferential and conceptual relations among
  internal states can constitute important aspects of meaning even without
  direct reference. They reject the inference from a next-token objective to
  the conclusion that a model's representations are necessarily meaningless.
- **Limit:** this is principally a philosophical interpretation, not a decisive
  behavioral or causal test of reference, truth, or practical understanding.
- **Project bearing:** direct counterevidence to a medium-essentialist reading
  of C3. The article must concede recoverable conceptual structure and focus on
  which distinctions remain identifiable and reliable. **Use status:**
  `counterevidence`.

#### Color studies: recovery, reporting bias, and degradation by abstraction

- **Sources:** Mostafa Abdou et al., “[Can Language Models Encode Perceptual
  Structure Without Grounding? A Case Study in
  Color](https://aclanthology.org/2021.conll-1.9/),” *CoNLL 2021*,
  [doi:10.18653/v1/2021.conll-1.9](https://doi.org/10.18653/v1/2021.conll-1.9);
  Cory Paik et al., “[The World of an Octopus: How Reporting Bias Influences a
  Language Model's Perception of
  Color](https://aclanthology.org/2021.emnlp-main.63/),” *EMNLP 2021*,
  [doi:10.18653/v1/2021.emnlp-main.63](https://doi.org/10.18653/v1/2021.emnlp-main.63);
  Hernán Loyola et al., “[Perceptual Structure in the Absence of Grounding for
  LLMs: The Impact of Abstractedness and
  Subjectivity](https://aclanthology.org/2023.findings-emnlp.102/),” *Findings of
  EMNLP 2023*,
  [doi:10.18653/v1/2023.findings-emnlp.102](https://doi.org/10.18653/v1/2023.findings-emnlp.102).
- **Type / checked:** three peer-reviewed empirical studies; checked 31 July
  2026.
- **Finding:** Abdou et al. find significant alignment between text-derived
  color representations and the perceptual CIELAB space, especially for warmer
  colors. Paik et al. show that language-model color judgments also track what
  people tend to say about color rather than human perceptual distributions
  themselves, and that multimodal models mitigate this reporting-bias effect.
  Loyola et al., using almost one million examples, find that alignment is
  strongest for relatively concrete, monolexemic descriptions and decreases as
  descriptions become more subjective or abstract.
- **Limit:** color is a narrow perceptual domain; representation-space alignment
  is not equivalent to reference, causal understanding, or reliable task
  performance. The studies nevertheless provide a rare controlled case where
  recovery and distortion can both be measured.
- **Project bearing:** supports C1 and a bounded C3 simultaneously: text carries
  indirect perceptual structure, but selective linguistic reporting changes its
  fidelity and coverage. **Use status:** `candidate evidence` and
  `counterevidence` to absolute formulations.

#### Gurnee and Tegmark: spatial and temporal representations

- **Source:** Wes Gurnee and Max Tegmark, “[Language Models Represent Space and
  Time](https://openreview.net/forum?id=jE8xbmvFin),” *ICLR 2024*; preprint at
  [arXiv:2310.02207](https://arxiv.org/abs/2310.02207).
- **Type / checked:** peer-reviewed representation analysis; checked 31 July
  2026.
- **Finding:** linear probes recover geographical and temporal coordinates at
  multiple scales from Llama-2 and Pythia activations, with identifiable
  neurons carrying spatial and temporal information. This supplies affirmative
  evidence that linguistic training can yield structured internal variables
  correlated with features of the world.
- **Limit:** probe recovery does not establish that those variables are used
  causally, are complete, or form a dynamic causal world model. The authors
  describe space and time as basic ingredients rather than sufficient world
  understanding.
- **Project bearing:** strengthens C1 and rules out “mere surface statistics” as
  the article's explanation. **Use status:** `candidate evidence`.

### 2. What does it mean for evidence to underdetermine a distinction?

#### D'Amour et al.: underspecification as an operational failure mode

- **Source:** Alexander D'Amour et al., “[Underspecification Presents
  Challenges for Credibility in Modern Machine
  Learning](https://jmlr.org/papers/v23/20-1335.html),” *Journal of Machine
  Learning Research* 23.226 (2022), pp. 1–61.
- **Type / checked:** peer-reviewed cross-domain empirical study; checked 31
  July 2026.
- **Finding:** a pipeline is underspecified when it can produce many predictors
  with equivalent in-distribution validation performance that behave differently
  on deployment-relevant stress tests. Across vision, medical imaging, NLP,
  clinical prediction, and genomics, innocuous pipeline choices and random seeds
  selected models with materially different robustness, fairness, or causal
  grounding.
- **Limit:** underspecification concerns the whole training and validation
  pipeline. It does not locate the missing constraint specifically in language,
  nor show that no enriched objective or test could supply it.
- **Project bearing:** offers a non-circular model for C2–C4: distinctions are
  unsupported when the accepted evidence and validation rule leave
  deployment-relevant alternatives observationally equivalent. **Use status:**
  `candidate evidence`.

#### Scaling and repeated data: compute is not new evidence

- **Sources:** Jordan Hoffmann et al., “[Training Compute-Optimal Large Language
  Models](https://proceedings.neurips.cc/paper_files/paper/2022/hash/c1e2faff6f588870935f114ebe04a3e5-Abstract-Conference.html),”
  *NeurIPS 2022*; Niklas Muennighoff et al., “[Scaling Data-Constrained Language
  Models](https://proceedings.neurips.cc/paper_files/paper/2023/hash/9d89448b63ce1e2e8dc7af72c984c196-Abstract-Conference.html),”
  *NeurIPS 2023*, [doi:10.52202/075280-2191](https://doi.org/10.52202/075280-2191).
- **Type / checked:** peer-reviewed large-scale empirical studies; checked 31
  July 2026.
- **Finding:** Hoffmann et al. show that compute-optimal training requires model
  capacity and data to scale together; a 70-billion-parameter model trained on
  four times more data outperformed the much larger Gopher model at the same
  training compute. Muennighoff et al. find that repeated data remains useful
  for roughly four epochs in their studied regimes, after which the value of
  additional repetition decays and eventually approaches zero.
- **Limit:** these are performance scaling results, not proofs of an epistemic
  ceiling. New optimization, regularization, synthetic curricula, or better
  use of old evidence can still improve a learner.
- **Project bearing:** supports only the restrained proposition that additional
  compute and parameters are not interchangeable with additional independent
  evidence. It does not establish C4's “noise” language. **Use status:**
  `background` and `candidate evidence`.

#### Shumailov et al.: recursive synthetic data and collapsing tails

- **Source:** Ilia Shumailov et al., “[AI models collapse when trained on
  recursively generated data](https://www.nature.com/articles/s41586-024-07566-y),”
  *Nature* 631 (2024), pp. 755–759,
  [doi:10.1038/s41586-024-07566-y](https://doi.org/10.1038/s41586-024-07566-y).
- **Type / checked:** peer-reviewed theoretical and empirical study; checked 31
  July 2026.
- **Finding:** when generated outputs recursively replace original data, errors
  compound and the tails of the source distribution disappear, producing model
  collapse in the studied settings.
- **Limit:** recursive retraining on generated data is not the same process as
  inference-time reflection or repeated search. The paper cannot be used as
  direct evidence that “thinking longer” generally creates noise.
- **Project bearing:** a bounded warning that self-generated material does not
  substitute for independent constraint and can progressively erase rare
  structure. **Use status:** `background`.

### 3. Can systems recognize unsupported refinement?

#### Semantic entropy and self-evaluation

- **Sources:** Sebastian Farquhar, Jannik Kossen, Lorenz Kuhn, and Yarin Gal,
  “[Detecting hallucinations in large language models using semantic
  entropy](https://www.nature.com/articles/s41586-024-07421-0),” *Nature* 630
  (2024), pp. 625–630,
  [doi:10.1038/s41586-024-07421-0](https://doi.org/10.1038/s41586-024-07421-0);
  Saurav Kadavath et al., “[Language Models (Mostly) Know What They
  Know](https://arxiv.org/abs/2207.05221)” (arXiv preprint, 2022).
- **Type / checked:** peer-reviewed LLM uncertainty study plus an unreviewed
  large-scale calibration study; checked 31 July 2026.
- **Finding:** semantic entropy groups sampled answers by meaning and predicts
  many knowledge-based confabulations better than token-level uncertainty;
  selective rejection improves accuracy in the evaluated question-answering
  settings. Kadavath et al. find that larger models can often predict whether
  their own answers are correct, although calibration on novel tasks is weak.
- **Limit:** both approaches estimate error risk, not the cause of the risk.
  Semantic entropy covers a subset of hallucinations and depends on multiple
  samples plus semantic equivalence estimation. Neither distinguishes missing
  evidence from a poor representation, failed learning, or bad decision rule.
- **Project bearing:** C5 is feasible in bounded settings, but a general
  “epistemic stopping” detector remains open. **Use status:** `candidate
  evidence`.

#### Selective prediction: abstention can be learned, but its target is supplied

- **Source:** Yonatan Geifman and Ran El-Yaniv, “[SelectiveNet: A Deep Neural
  Network with an Integrated Reject
  Option](https://proceedings.mlr.press/v97/geifman19a.html),” *ICML 2019*, PMLR
  97, pp. 2151–2159.
- **Type / checked:** peer-reviewed method paper; checked 31 July 2026.
- **Finding:** SelectiveNet jointly learns prediction and rejection and improves
  the risk–coverage tradeoff over the evaluated baselines. It demonstrates that
  abstention can be an optimized part of a learned system rather than an
  external post-processing rule.
- **Limit:** the desired coverage, loss, and supervised task are externally
  specified. The model is not discovering that its evidence medium lacks a
  needed distinction.
- **Project bearing:** architectural feasibility for C5, not a solution to its
  strongest version. **Use status:** `candidate evidence`.

#### Calibration under distribution shift

- **Source:** Yaniv Ovadia et al., “[Can You Trust Your Model's Uncertainty?
  Evaluating Predictive Uncertainty Under Dataset
  Shift](https://proceedings.neurips.cc/paper_files/paper/2019/hash/8558cb408c1d76621371888657d2eb1d-Abstract.html),”
  *NeurIPS 2019*.
- **Type / checked:** peer-reviewed benchmark; checked 31 July 2026.
- **Finding:** accuracy and uncertainty calibration generally degrade as dataset
  shift intensifies. Post-hoc calibration and several approximate Bayesian
  methods fail to remain reliable, while methods that marginalize over models,
  especially deep ensembles in the tested cases, are more robust.
- **Limit:** the benchmarks are supervised classification problems and compare
  methods available in 2019. Better methods can reduce, but do not eliminate,
  the requirement to test uncertainty under anticipated shifts.
- **Project bearing:** ordinary confidence cannot serve as C5's stopping rule.
  Any proposed signal must be evaluated under distribution and regime change,
  not only where it was calibrated. **Use status:** `candidate evidence` and
  `counterevidence` to simple self-confidence proposals.

### 4. Do existing architectures discover, consolidate, and execute methods?

#### DreamCoder: amortizing search into reusable program components

- **Source:** Kevin Ellis et al., “[DreamCoder: Bootstrapping Inductive Program
  Synthesis with Wake-Sleep Library
  Learning](https://pldi21.sigplan.org/details/pldi-2021-papers/55/DreamCoder-Bootstrapping-Inductive-Program-Synthesis-with-Wake-Sleep-Library-Learnin),” *Proceedings of
  PLDI 2021*, [doi:10.1145/3453483.3454080](https://doi.org/10.1145/3453483.3454080).
- **Type / checked:** peer-reviewed program-synthesis system; checked 31 July
  2026.
- **Finding:** DreamCoder alternates program search with learning a library of
  recurring program fragments and a neural search policy. Across eight domains,
  learned abstractions let it solve additional problems and search more
  efficiently. This is the closest located implementation of “amortize search
  into method.”
- **Limit:** tasks, primitives, examples, and success criteria are tightly
  constrained. Library learning does not decide whether the evidence itself is
  sufficient, and a discovered program is not automatically a trustworthy
  general method.
- **Project bearing:** bounded support for C6–C7 and a strong prototype
  precedent for C10. **Use status:** `candidate evidence`.

#### Modular meta-learning and sparse conditional computation

- **Sources:** Ferran Alet, Tomas Lozano-Perez, and Leslie P. Kaelbling,
  “[Modular Meta-Learning](https://proceedings.mlr.press/v87/alet18a.html),”
  *CoRL 2018*, PMLR 87, pp. 856–868; William Fedus, Barret Zoph, and Noam
  Shazeer, “[Switch Transformers: Scaling to Trillion Parameter Models with
  Simple and Efficient Sparsity](https://www.jmlr.org/papers/v23/21-0998.html),”
  *JMLR* 23.120 (2022), pp. 1–39.
- **Type / checked:** peer-reviewed architecture papers; checked 31 July 2026.
- **Finding:** modular meta-learning discovers compositions of reusable modules
  across related tasks; Switch Transformers learn sparse, input-conditional
  routing so that different parameter subsets process different tokens at
  approximately constant per-token computational cost.
- **Limit:** these works show learnable modular composition and routing, not
  automatic discovery of epistemic domains. The module palette, objectives,
  and training distribution still constrain what is discovered; mixture-of-
  experts routing is not itself semantic or explanatory.
- **Project bearing:** C9 is technically plausible, but the article should not
  present learned regimes or conditional routing as new. **Use status:**
  `background` and `candidate evidence`.

#### Deep distilling: learned structure condensed into executable code

- **Source:** David Blazek, Pranav Venkatesh, and Charles Lin, “[Automated
  discovery of algorithms from
  data](https://www.nature.com/articles/s43588-024-00593-9),” *Nature
  Computational Science* 4 (2024), pp. 72–80,
  [doi:10.1038/s43588-024-00593-9](https://doi.org/10.1038/s43588-024-00593-9).
- **Type / checked:** peer-reviewed method paper; checked 31 July 2026.
- **Finding:** the authors' “deep distilling” method trains a specially
  structured neural network and losslessly condenses it into concise executable
  code. In selected arithmetic, vision, and optimization tasks, the extracted
  algorithms show strong systematic out-of-distribution generalization and can
  outperform human-designed algorithms.
- **Limit:** the result depends on a specialized architecture and domains with
  extractable symbolic structure. The authors disclose patent-related conflicts
  of interest. It does not establish that arbitrary LLM regularities can or
  should be compiled.
- **Project bearing:** direct bounded evidence for C6's learned-structure-to-
  execution transition. **Use status:** `candidate evidence`.

### 5. When and how can other evidence or computation help?

#### Toolformer: learning when to call predefined tools

- **Source:** Timo Schick et al., “[Toolformer: Language Models Can Teach
  Themselves to Use
  Tools](https://proceedings.neurips.cc/paper_files/paper/2023/hash/d842425e4bf79ba039352da0f658a906-Abstract-Conference.html),”
  *NeurIPS 2023*, [doi:10.52202/075280-2997](https://doi.org/10.52202/075280-2997).
- **Type / checked:** peer-reviewed tool-use method; checked 31 July 2026.
- **Finding:** Toolformer self-supervises the placement and use of calls to a
  calculator, question-answering system, search engine, translation system, and
  calendar. The resulting model learns which tool to call and incorporates its
  output, improving several zero-shot tasks.
- **Limit:** the tools and APIs are supplied in advance, and calls are retained
  when they improve the language-modeling objective. This is learned routing to
  computation, not a general detector of linguistic underdetermination.
- **Project bearing:** strong bounded support for C8 and a precedent for joining
  inference to new constraints. **Use status:** `candidate evidence`.

The color work above supplies the complementary evidential case: Paik et al.'s
multimodal models reduce a distortion caused by linguistic reporting bias. A
calculator changes the available computation or verification rule; a camera or
experiment can change the evidence; retrieval can do either depending on what
is retrieved. C8 should therefore describe these routes separately rather than
grouping them as generic “tools.”

## Targeted research pass — 4 August 2026

### Scope

This pass tested five exposed parts of the logical tree: contextual field
inference, internal field-state correspondence from sequence training,
complexity and depth degradation, path evidence, and field-structured
innovation. It used primary papers and publisher or proceedings records.

### Context can select a latent structure, within a bounded model

#### Xie et al.: in-context learning as latent-concept inference

- **Source:** Sang Michael Xie, Aditi Raghunathan, Percy Liang, and Tengyu Ma,
  “[An Explanation of In-context Learning as Implicit Bayesian
  Inference](https://arxiv.org/abs/2111.02080),” *ICLR 2022*.
- **Type / checked:** peer-reviewed theoretical and synthetic experimental
  paper; checked 4 August 2026.
- **Finding:** in a pretraining distribution modeled as a mixture of hidden
  Markov models, coherent documents require inference of a latent
  document-level concept. Under stated distinguishability assumptions, the
  same mechanism can select a shared latent prompt concept at test time. The
  GINC experiments reproduce in-context learning and show dependence on model
  size, example order, and whether the concept appeared during pretraining.
- **Limit:** the theorem concerns an idealized mixture of HMMs and the
  experiments use a synthetic dataset. “Latent concept” is not yet equivalent
  to the article's field representation, and the result does not establish that
  this mechanism explains broad competence in deployed LLMs.
- **Project bearing:** bounded candidate evidence for C1 and C11. It justifies
  testing contextual field selection rather than presenting that mechanism as
  established. **Use status:** `candidate evidence`.

### Othello as a positive proof of domain-appropriate internal learning

The focused technical account, evidence ladder, methodological objections,
newer follow-up work, and drafting limits are maintained in
[`othello_gpt_deep_research.md`](othello_gpt_deep_research.md). This section
retains only the cross-source synthesis required by the general research
summary.

#### Li et al.: Othello-GPT as counterevidence to a surface-only account

- **Source:** Kenneth Li et al., “[Emergent World Representations: Exploring a
  Sequence Model Trained on a Synthetic
  Task](https://openreview.net/forum?id=DeG07_TcZvT),” *ICLR 2023*; accessible
  manuscript at [arXiv:2210.13382](https://arxiv.org/abs/2210.13382).
- **Type / checked:** peer-reviewed mechanistic case study; checked 4 August
  2026.
- **Finding:** the model receives only sequences drawn from a 60-token move
  vocabulary. Its synthetic training corpus contains 20 million games sampled
  from legal play without strategic preference; the board geometry and rules
  are not supplied. A nonlinear probe recovers board state from the trained
  model. The authors then optimize hidden
  activations so a single tile corresponds to a counterfactual state. Predicted
  moves shift toward the legal-move set for that altered board, including
  unreachable boards; average intervention error falls to 0.12 and 0.06 in the
  natural and unnatural test sets from baselines of 2.68 and 2.59.
- **Limit:** Othello has a small, exact, fully observable state and rigid rules.
  The result does not show that natural-language models reliably learn the
  correct representation in open or hybrid fields.
- **Project bearing:** this is the closest positive example of the author's
  proposed learning principle. A sequence model converts a surface token
  history into internal variables organized by a field state, and those
  variables causally constrain later token generation. It is not independent
  of the sequence evidence from which it was learned, but it is structurally
  distinct from the surface notation. The remaining dispute is whether to call
  the result a learned field model or a highly effective field-corresponding
  predictive state. **Use status:** `central positive exemplar`, with the
  stated scope limit.

#### Nanda et al.: the learned variables follow task-relative field structure

- **Source:** Neel Nanda, Andrew Lee, and Martin Wattenberg, “[Emergent Linear
  Representations in World Models of Self-Supervised Sequence
  Models](https://aclanthology.org/2023.blackboxnlp-1.2/),” *Proceedings of the
  6th BlackboxNLP Workshop* (2023), pp. 16–30,
  [doi:10.18653/v1/2023.blackboxnlp-1.2](https://doi.org/10.18653/v1/2023.blackboxnlp-1.2).
- **Type / checked:** peer-reviewed workshop paper and mechanistic follow-up;
  checked 4 August 2026.
- **Finding:** the apparent nonlinear board representation becomes almost
  perfectly linearly decodable when tiles are classified as `Mine`, `Yours`,
  and `Empty` relative to the current player rather than as absolute black and
  white. Accuracy reaches 99.6 percent in layer 7. Adding the corresponding
  linear directions steers move predictions toward the altered board. The
  model also linearly represents which pieces were flipped and appears to use
  multiple circuits, especially later in games.
- **Limit:** the study analyzes the same small transformer and synthetic
  Othello setting. Linear probes require researchers to propose the relevant
  categories, and the authors report that some legal moves are computed before
  a complete board state in later play. No single decoded representation
  explains every prediction.
- **Project bearing:** strong evidence that a useful internal representation
  need not reproduce surface notation or the human-default description. The
  relational categories `Mine` and `Yours` are selected by the transition task.
  The multiple-circuit result also corrects a simple “one mechanism per field”
  picture: field-appropriate learning may require several task-relative
  mechanisms coordinated within one domain. **Use status:** `adopted evidence`
  and `central positive exemplar`.

### Bounded synthesis: what the Othello example establishes

Othello-GPT instantiates the sequence the article proposes:

`surface move tokens -> latent field state -> field-constrained transition ->
next move token`

It establishes that next-token training can induce internal variables whose
organization is better described by the represented field than by the input
notation, and that these variables can causally affect output. It does not
establish multi-domain selection, linguistic grounding in open domains, or one
complete internal rule system. The article's proposed advance is to make this
kind of field-appropriate internalization reliable across many domains and to
coordinate several representations when a task crosses their boundaries.

A stronger invariance test would train equivalent Othello tasks under permuted
or otherwise different surface encodings. Structural alignment of the learned
states across encodings would support independence from any particular token
scheme. A multi-domain version would then test whether context selects
separable but composable state mechanisms rather than a single generic
linguistic proxy.

#### MetaOthello: an initial controlled invariance and routing result

- **Source:** Aviral Chawla, Galen Hall, and Juniper Lovato,
  “[MetaOthello: A Controlled Study of Multiple World Models in
  Transformers](https://arxiv.org/abs/2602.23164),” preprint, February 2026.
- **Type / checked:** recent preprint; checked 4 August 2026.
- **Finding:** in paired isomorphic Othello tasks with permuted token-to-square
  mappings, the learned board-state representations align up to an orthogonal
  rotation, and rotating hidden activations transfers predictions across most
  layers. In mixed rule variants, the model largely shares board-state
  structure and introduces localized game-identity routing where the rules
  conflict.
- **Limit:** one small architecture, pairwise 50/50 mixtures, exact synthetic
  games, and linear-probe analysis. The variants remain members of one board-
  game family, not independent domains. All-layer steering may over-intervene.
- **Project bearing:** direct provisional support for the proposed surface-
  encoding invariance test and for shared-state-plus-routing as an alternative
  to one isolated mechanism per field. **Use status:** `promising preprint
  evidence`, not a general multi-domain result.

#### Lee et al.: structured factorization is possible but not yet the model's mechanism

- **Source:** Andrew Lee, Fernanda Viégas, and Martin Wattenberg,
  “[Tensor Product Representation Probes Reveal Shared Structure Across Linear
  Directions](https://arxiv.org/abs/2605.09967),” preprint, May 2026.
- **Type / checked:** recent preprint; checked 4 August 2026.
- **Finding:** a structured probe factorizes Othello-GPT's separate square–color
  directions into square embeddings, color embeddings, and a binding matrix,
  reaches about 99 percent board-state accuracy with fewer parameters than the
  independent linear probes, recovers board-aligned geometry, and supports
  composable interventions.
- **Limit:** the structure is specified by the investigators. The authors
  explicitly do not claim that Othello-GPT performs tensor products or natively
  separates square and color subspaces.
- **Project bearing:** candidate evidence that task-relative linear variables
  can admit a richer relational factorization, while preserving the distinction
  between a successful decoder and the model's actual mechanism. **Use status:**
  `candidate preprint evidence`.

### Complexity and depth degradation are real but causally underdetermined

#### Dziri et al.: compositional complexity and rapid decay

- **Source:** Nouha Dziri et al., “[Faith and Fate: Limits of Transformers on
  Compositionality](https://proceedings.neurips.cc/paper_files/paper/2023/hash/deb3c28192f979302c157cb653c15e90-Abstract.html),”
  *NeurIPS 2023*, doi:10.52202/075280-3081.
- **Type / checked:** peer-reviewed empirical and theoretical study; checked 4
  August 2026.
- **Finding:** across multiplication, logic-grid puzzles, and a dynamic
  programming task, the authors represent tasks as computation graphs and find
  performance degradation with increased compositional complexity. Their
  analysis characterizes observed behavior as linearized subgraph matching and
  gives theoretical arguments for rapid decay in abstract autoregressive
  multistep tasks.
- **Limit:** the study does not measure linguistic quality against semantic
  state fidelity and does not identify representational drift as the unique
  cause. Search, computation, data coverage, and architecture remain rival
  explanations.
- **Project bearing:** candidate evidence for the empirical premise of C12,
  but not for the article's causal explanation. **Use status:** `candidate
  evidence`.

#### Nye et al. and Anil et al.: intermediate computation and length

- **Sources:** Maxwell Nye et al., “[Show Your Work: Scratchpads for
  Intermediate Computation with Language
  Models](https://research.google/pubs/show-your-work-scratchpads-for-intermediate-computation-with-language-models/),”
  2021, [arXiv:2112.00114](https://arxiv.org/abs/2112.00114); Cem Anil et al.,
  “[Exploring Length Generalization in Large Language
  Models](https://proceedings.neurips.cc/paper_files/paper/2022/hash/fb7451e43f9c1c35b774bcfad7a5714b-Abstract-Conference.html),”
  *NeurIPS 2022*, doi:10.52202/068431-2793.
- **Type / checked:** primary experimental studies; checked 4 August 2026.
- **Finding:** scratchpad-formatted intermediate computations greatly improve
  selected multistep tasks. Anil et al. also find that naive fine-tuning has
  substantial length-generalization deficiencies not removed by scale alone,
  while in-context scratchpads produce large gains.
- **Limit:** improvement from externalized intermediate tokens does not prove
  that those tokens constitute a faithful internal causal path. The results
  also show that task format and computational workspace can explain failures
  otherwise attributed to semantic drift.
- **Project bearing:** supporting evidence for depth sensitivity and an
  important alternative mechanism. **Use status:** `candidate evidence` and
  `qualification`.

### Field-aligned intermediate supervision has bounded precedents

#### CLRS and Hint-ReLIC: explicit algorithmic trajectories

- **Sources:** Petar Veličković et al., “[The CLRS Algorithmic Reasoning
  Benchmark](https://proceedings.mlr.press/v162/velickovic22a.html),” *ICML
  2022*, PMLR 162:22084–22102; Beatrice Bevilacqua et al., “[Neural Algorithmic
  Reasoning with Causal
  Regularisation](https://proceedings.mlr.press/v202/bevilacqua23a.html),”
  *ICML 2023*, PMLR 202:2272–2288.
- **Type / checked:** peer-reviewed benchmark and method papers; checked 4
  August 2026.
- **Finding:** CLRS supplies input, output, and optional intermediate
  trajectories for thirty classical algorithms, making transition-level and
  out-of-distribution tests possible. Hint-ReLIC uses invariances of correct
  next trajectory steps to regularize a neural reasoner and reports up to
  threefold improvement on CLRS out-of-distribution tests.
- **Limit:** these are specialized graph-based neural reasoners, not general
  LLMs, and the algorithms and trajectories are given. The causal
  regularization result does not isolate the article's proposed
  language-to-field mapping.
- **Project bearing:** concrete precedent for C13 and C20: field-valid
  intermediate states can define training and evaluation targets. **Use
  status:** `candidate evidence`.

#### Lightman et al.: process supervision improves a mathematics system

- **Source:** Hunter Lightman et al., “[Let's Verify Step by
  Step](https://arxiv.org/abs/2305.20050),” 2023.
- **Type / checked:** primary empirical paper and released step-label dataset;
  checked 4 August 2026.
- **Finding:** on a representative subset of MATH, process supervision using
  human labels for intermediate written steps outperforms outcome supervision;
  the authors release PRM800K with 800,000 step-level labels.
- **Limit:** the labels evaluate displayed solution steps, not latent model
  states. Better final performance does not show that the written rationale is
  the internal cause of the answer.
- **Project bearing:** bounded precedent for C20 and C22 and for step-level
  training; not a solution to C21's path-identification problem. **Use status:**
  `candidate evidence`.

### Generated rationales are not reliable path evidence

#### Turpin et al.: causal evidence of unfaithful chain of thought

- **Source:** Miles Turpin et al., “[Language Models Don't Always Say What They
  Think: Unfaithful Explanations in Chain-of-Thought
  Prompting](https://proceedings.neurips.cc/paper_files/paper/2023/hash/ed3fea9033a80fea1376299fa7863f4a-Abstract.html),”
  *NeurIPS 2023*, doi:10.52202/075280-3275.
- **Type / checked:** peer-reviewed intervention study; checked 4 August 2026.
- **Finding:** biasing prompt features systematically alter model answers while
  generated explanations often omit the influence and rationalize the result.
  The intervention makes the gap between stated and actual influence
  observable.
- **Limit:** the study tests selected models and tasks and does not imply that
  every chain of thought is unfaithful.
- **Project bearing:** source support for C21's bounded claim that a generated
  rationale does not establish the path that caused an answer. **Use status:**
  `adopted evidence`.

### The deployed model has more than one training objective

#### Brown et al. and Ouyang et al.: pretraining and post-training

- **Sources:** Tom Brown et al., “[Language Models are Few-Shot
  Learners](https://proceedings.neurips.cc/paper_files/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html),”
  *NeurIPS 2020*; Long Ouyang et al., “[Training Language Models to Follow
  Instructions with Human Feedback](https://arxiv.org/abs/2203.02155),”
  *NeurIPS 2022*.
- **Type / checked:** peer-reviewed model and post-training papers; checked 4
  August 2026.
- **Finding:** GPT-3 demonstrates broad few-shot behavior after autoregressive
  language-model training. InstructGPT adds supervised instruction tuning and
  reinforcement learning from human preferences; human evaluators prefer its
  1.3-billion-parameter model to the 175-billion-parameter GPT-3 baseline on
  the studied prompt distribution.
- **Limit:** preference training does not itself enforce field validity and may
  reward plausibility or user approval. It nevertheless materially changes
  deployed behavior.
- **Project bearing:** corrects an overcompressed premise in C12: probable
  continuation characterizes base pretraining, not the complete objective or
  causal history of an instruction-following assistant. **Use status:**
  `adopted background`.

### Structured search and validation can produce novel results

#### AlphaTensor: discovery inside an exact state and validity structure

- **Source:** Alhussein Fawzi et al., “[Discovering Faster Matrix
  Multiplication Algorithms with Reinforcement
  Learning](https://www.nature.com/articles/s41586-022-05172-4),” *Nature* 610
  (2022): 47–53, doi:10.1038/s41586-022-05172-4.
- **Type / checked:** peer-reviewed research article; checked 4 August 2026.
- **Finding:** AlphaTensor formulates matrix-multiplication algorithm discovery
  as a game over tensor decompositions, combines a learned policy with planning,
  and finds provably correct algorithms that improve known multiplication
  counts in several settings, including a finite-field 4-by-4 result beyond
  Strassen's two-level method.
- **Limit:** this is a specialized reinforcement-learning system with an exact
  representation, enormous search, a validity test, and a supplied objective;
  it is not an LLM and does not address soft-domain syntax.
- **Project bearing:** strong precedent for C24's state–syntax–search–value
  architecture and for object-level machine discovery. **Use status:**
  `adopted precedent`.

#### FunSearch: LLM proposals inside evaluator-governed evolutionary search

- **Source:** Bernardino Romera-Paredes et al., “[Mathematical Discoveries from
  Program Search with Large Language
  Models](https://www.nature.com/articles/s41586-023-06924-6),” *Nature* 625
  (2024): 468–475, doi:10.1038/s41586-023-06924-6.
- **Type / checked:** peer-reviewed research article; checked 4 August 2026.
- **Finding:** FunSearch combines a pretrained code LLM with a user-supplied
  program skeleton, executable evaluator, program database, and evolutionary
  search. It reports new cap-set constructions and improved online bin-packing
  heuristics.
- **Limit:** the method samples on the order of one million programs and relies
  on external execution, scoring, and search. Its discoveries establish
  system-level novelty; they do not show that an unaided LLM internally follows
  a field-valid reasoning path.
- **Project bearing:** strong precedent for C23–C24 and a direct warning against
  conflating LLM contribution with whole-system innovation. **Use status:**
  `adopted precedent`.

#### AlphaGeometry: field representation, neural proposal, symbolic validity

- **Source:** Trieu H. Trinh et al., “[Solving Olympiad Geometry without Human
  Demonstrations](https://www.nature.com/articles/s41586-023-06747-5),”
  *Nature* 625 (2024): 476–482, doi:10.1038/s41586-023-06747-5.
- **Type / checked:** peer-reviewed research article; checked 4 August 2026.
- **Finding:** AlphaGeometry trains a language model on synthetically generated
  geometry proofs to propose auxiliary constructions and interleaves those
  proposals with a symbolic deduction engine. It solves 25 of 30 translated
  olympiad geometry problems and identifies a generalized form of one
  translated theorem.
- **Limit:** only 75 percent of the relevant IMO geometry problems fit the
  specialized representation; deduction is delegated to symbolic engines.
  This is a hybrid tool-using system, not evidence that semantic training alone
  improves an LLM's internal inference.
- **Project bearing:** unusually close architectural precedent for C13, C15,
  C23, and C26. It also demonstrates the representation bottleneck and the need
  to keep semantic training distinct from external validation. **Use status:**
  `adopted precedent`.

### Synthesis of the targeted pass

The source base now supports four bounded propositions:

1. Contextual latent-structure selection is a demonstrated mechanism in a
   stylized setting.
2. Sequence training can create causally effective, task-relative field states
   in at least one controlled domain. Othello-GPT's `Mine`/`Yours`/`Empty`
   organization is a positive example of internal structure distinct from
   surface notation, while the unrestricted label “world model” remains
   contestable.
3. Compositional complexity and length expose systematic failures, although
   their cause remains underdetermined.
4. Explicit trajectories, field constraints, search, and verification can
   improve reasoning systems and produce novel results in formal domains.

The decisive multi-domain proposition remains unsourced because it is the
project's own testable contribution: training should reliably produce or
activate different task-appropriate semantic mechanisms, context should select
and coordinate them, and those mechanisms should reduce invalid-transition
rates relative to a matched surface-dependent baseline. Othello establishes
single-domain feasibility, not this generalization.

## Cross-source synthesis adopted for further argument work

### Relation to the clarified thesis

The following five-layer account remains useful, but it is no longer the
article's central diagnosis. It primarily describes how world structure enters
language, how evidence may underdetermine a task, and how systems respond to
uncertainty. The clarified thesis inserts another layer between recovery and
epistemic control: **syntactical validity through semantic transformation**.
Once a faithful correlation has been encoded, is the resulting semantic
transition valid under the syntax of the represented field, or only plausible
under relations internal to the linguistic domain?

The completed source pass does not answer that question directly. Its most
important positive contribution is to establish that there can be real
world-correlated structure available to be preserved or lost.

### A five-layer account

1. **Representational recovery:** language-trained systems demonstrably recover
   some perceptual, spatial, temporal, and social regularities. The article
   should explain competence from this positive fact.
2. **Syntactical validity through semantic transformation:** a recovered
   correlation remains faithful only if later semantic changes follow valid
   transitions in the represented field or receive an external check. Direct
   evidence remains to be researched.
3. **Identifiability and initial fidelity:** textual evidence is a selective trace of
   the world. Some distinctions are observationally equivalent under the
   available data and validation rule; others are represented with reporting
   bias or lose alignment as descriptions become abstract and subjective.
4. **Epistemic control:** uncertainty, semantic consistency, and abstention can
   detect some risky outputs. These signals are fallible under task novelty and
   distribution shift and do not reveal which layer caused the uncertainty.
5. **Architectural response:** abstraction libraries, modular composition,
   sparse routing, program distillation, and tool calls already work in bounded
   domains. The missing synthesis is a tested meta-criterion that decides among
   further search, consolidation, execution, abstention, and acquisition of a
   genuinely new constraint.

### Three meanings of “limit” that must remain separate

- **Information / identifiability limit:** the admitted observations do not
  distinguish alternatives relevant to the task.
- **Representation / learning limit:** the evidence contains a useful signal,
  but the chosen representation, objective, or learner does not recover it.
- **Decision / calibration limit:** the system may contain the relevant
  information yet cannot reliably select, report, or know when to trust the
  answer.

Current uncertainty techniques do not reliably diagnose which limit is active.
An intervention that adds evidence is therefore diagnostic as well as remedial:
if an otherwise equivalent problem becomes decidable after a targeted query,
perception, experiment, or computation, that result helps locate the missing
constraint.

### Operational definition to test

For a task `T`, admitted evidence `E`, representation `R`, inference procedure
`A`, and a predeclared family of deployment-relevant shifts `S`, call a
distinction `d` **recoverable** only if a fixed decision procedure can
discriminate `d` on held-out or interventionally relevant cases with error and
calibration below precommitted thresholds throughout `S`. Call further
refinement **unsupported** when additional search or sampling over the same
`E/R` does not improve those measures, while a new constraint separates cases
that were previously observationally equivalent.

This definition makes epistemic resolution task-relative. It does not claim an
intrinsic, once-for-all “resolution of language,” because recoverability changes
with the corpus, task, representation, permitted inference, and validation
conditions. It now applies to the secondary identifiability question; it is not
yet an operational definition of transformation fidelity.

### Strongest falsifiable prototype

Construct paired language/domain tasks with a known semantic representation,
such as program states, graphs, spatial configurations, or causal systems. Vary
domain complexity and required transformation depth independently. Compare a
matched text-only contextual model with one trained to predict, transform, or
validate the corresponding domain representation. A further condition can
periodically check the evolving result against an external oracle, executable
model, or targeted observation.

Measure linguistic quality and domain-state fidelity separately after every
step, together with transition validity, confidence, calibration, and compute.
Report terminal accuracy separately from valid-success rate and the rate of
correct endpoints reached through invalid paths. The decisive
prediction is an interaction: in the text-only condition, semantic fidelity
should decline more steeply with complexity and chain length than surface
quality does; semantic-representation training should flatten that decline.
Failure to observe the dissociation weakens the proposed limit. Failure of
field-appropriate representations to improve it weakens the remedy. A separate
learned-gating test can then ask when external renewal is worth its cost.

Tool calling must be crossed independently with training condition rather than
treated as the semantic-representation intervention. After establishing the
single-field result, add (a) a hybrid task with an explicit interface between
two representations and (b) anchor manipulations separating distance,
distractor interference, compression, and hard context-window removal. A later
humanities study can replace one canonical target with multiple defensible
argument maps and score only violations excluded by the predeclared admissible
set.

## Unresolved research questions

- Can “same evidence” be defined for interactive language systems, where model
  outputs may become prompts, scratchpads, or search queries?
- What counts as the correlation syntax of a representation when the mapping is
  approximate, many-to-many, context-sensitive, and purpose-relative?
- How can a system distinguish a field-invalid semantic transition from one
  whose validity is merely unverified, without assuming direct ground truth?
- Which linguistic transformations demonstrably implement field-valid semantic
  transitions, and can those classes be learned rather than hand-coded?
- Which interventions distinguish missing evidence from a representation or
  optimization failure without presupposing the correct answer?
- How should a system trade the suppression of unsupported distinctions against
  the risk of discarding rare but genuine structure?
- What stability criterion permits consolidation while retaining rapid revision
  under domain change?
- Is the strongest contribution a philosophical framework, an engineering
  design pattern, or an empirical result from the proposed prototype?

## Bibliographic and provenance status

The shared Research Library was audited before this pass: 620 works and 213
files were present, with no audit failures and two pre-existing provisional,
titleless warnings. A CSL export search did not locate the principal works
above. The available verified CLI does not currently expose a deterministic
add-by-DOI operation, so no bibliography records or project source manifest
were fabricated or written. The links and identifiers in this file were
checked against publisher, conference, journal, or author records on 31 July
2026; formal admission to the local bibliography remains `REVIEW_REQUIRED`
until the supported verified-intake path exists.
