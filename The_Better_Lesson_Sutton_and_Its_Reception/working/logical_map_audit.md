# Logical-Map Coherence and Source Audit

Status: current audit, 4 August 2026. This file records defects, evidentiary
status, and revision dispositions. It does not supersede the settled argument
in `logical_map.md` or the source records in `research_summaries.md`.

## Artifact decision

The audit has one responsibility: test the authoritative logical map without
turning that map into a history of its own correction. Its consumers are the
next argument revision and the eventual article plan. It can be revised or
retired when the identified burdens have been resolved, independently of the
running synthesis and the source catalogue.

The positive forces are a concise, writing-ready argument and a reproducible,
adversarial record of everything that could still defeat it. The existing
artifacts realize only one force each: `logical_map.md` owns settled logic,
`argument_map.md` owns cumulative development, and `research_summaries.md` owns
source evidence. Merging this audit into the logical map would destroy its
polished role; merging it into the running synthesis would make dispositions
and source coverage difficult to recover. A single current audit file is
therefore **KEEP**. Separate objection, citation-gap, and revision files are
**DEFER** because they would have the same owner, consumer, and lifecycle.

## Overall verdict

The map has a strong central diagnostic: locate the marginal task-specific
discovery in the learning system or in the human training apparatus. Its
conditional positive proposal is also coherent: a bounded human contribution
can constitute a system that generates and evaluates further experience.

The map now has a coherent basis for an argument-first article plan, although
its positive architectural proposal still carries empirical burdens. Two
issues that reached the central inference have been resolved conceptually. The fixed-input closure
test is a decisive sufficient condition, while recurrent human input is tested
by whether the same expanding performance frontier remains reachable after
that input is frozen. Learner-internal credit assignment is admissible when its
distinctions are derived from the constituted system's structure, transitions,
and outcomes; external human semantic preference remains a separate source of
task-specific method discovery.

Three further revisions remain: reconcile the upstream criticism of pretraining
with the accepted finite-post-training case; complete the defense of grounded,
non-self-certifying experience; and limit the domain proposal to objectives that
actually admit reliable evaluation. The essay's role has also been clarified:
the article treats it as a concise articulation of the paradigm under review,
not as the demonstrated historical cause of LLM development.

## Charitable reconstruction

The strongest form of the present argument is:

1. Sutton's lesson concerns methods whose marginal gains continue to be driven
   by computation, especially search and learning, rather than by a continuing
   stream of human discoveries.
2. Human knowledge may constitute the problem, initialize the learner, and
   define legitimate outcomes.
3. A constituted domain can generate candidate actions, consequences, and
   evaluative evidence beyond its finite human seed.
4. Pretraining demonstrates the power of a general scalable method, while its
   next-token objective underdetermines the objective of a deployed assistant.
5. Post-training is compatible with the lesson when it creates a generative
   learning system whose task-specific methods are discovered from its own
   evaluated experience.
6. Post-training departs from the lesson when further progress depends on
   engineers diagnosing each new class of failure and encoding the remedy.
7. The present field-level question is empirical: which post-training systems
   place the marginal epistemic work on each side of that distinction?

This reconstruction survives most of the objections below. Its remaining
burdens concern the empirical classification of current systems, the validity
of generated evaluative experience, and the scope of domains that admit such
evaluation.

## Ranked coherence findings

### 1. Learner-internal credit assignment must be separated from external process targets

**Nodes:** Concepts 4 and 7; E2; E4; E5-R; E6; E7.

The previous E branch assigned discovery to the learning system when
domain-internal evidence selected a remedy, then denied that status when the
system learned causal or progress distinctions across trajectories. Those
claims conflicted. Cross-trajectory generalization from returns is a standard
way for a learner to discover which states and actions predict success.

Sutton and Barto define value functions in terms of expected future return and
present Monte Carlo control as learning values and policies by averaging sample
returns across experience. AlphaZero is an especially direct counterexample to
the current rule: every completed game supplies a terminal result, while the
network learns state-dependent outcome values and a policy shaped by MCTS visit
distributions. It therefore gives different prospective significance to moves
and positions whose realized games may share the same terminal result.

The revised boundary is epistemic provenance. A value model, process evaluator,
or other component belongs to the learner for this purpose when it derives its
distinctions from the constituted domain's formal structure, transitions, and
outcomes. A distinction belongs to the engineers when humans diagnose the
method and encode its legitimacy independently of evidence available to the
learner.

**Force:** Previously critical; resolved at the level of principle. Individual
post-training methods still require provenance classification.

**What answers it:** Permit comparison across iterations, value learning,
generalization, and higher-order credit assignment when the system derives the
distinction from outcome-grounded evidence. Exclude a human semantic ranking
that stipulates the proper route independently of that evidence. The
job-discrimination analogy applies only to the latter case: an evaluator ranks
otherwise outcome-equivalent routes by a preference irrelevant to the
constituted objective.

**Disposition:** Resolved in E4-E6. Source alignment with Sutton and Barto and
AlphaZero is restored.

### 2. Sparse supervision does not establish independence from human judgment

**Nodes:** T; A3; A5; D1-D8; H1; H2; H4.

A5 correctly locates Sutton's criterion in the marginal source of improvement.
Fixed human input supplies the cleanest sufficient test. The difficult case is
recurrent feedback whose numerical share declines while its judgments are
amortized across a much larger volume of machine experience.

Christiano et al. trained agents from comparisons covering about 0.1 percent of
interactions and used a labeling schedule whose rate declined as experience
grew. The paper also found that online feedback helped prevent exploitation of
the learned reward. This establishes sparsity and amortization. It does not
establish that the feedback is causally dispensable: a tiny input can remain an
indispensable critical-path component.

The code-breaking example makes the order-of-magnitude issue explicit. A human
who knows the exact code holds the strongest possible informational advantage,
yet a sufficiently fast search process can outrun that fixed contribution.
Current proportions do not determine which component governs the expanding
frontier. A chain scales only as far as its least scalable indispensable link.

**Force:** Critical empirical burden, rather than a conceptual exception.
Sutton does not state a fixed-input theorem, so the article must operationalize
his claim that search and learning continue to scale with computation.

**What would answer it:** Freeze further task-specific human feedback after
bounded constitution and increase computation and system-generated experience.
If the same expanding performance frontier remains reachable, even on a
different learning curve or at higher computational cost, the feedback is an
efficiency advantage rather than the source of continuing discovery. If
progress stalls, drifts, or requires new human correction, the current
architecture has not been shown to scale through computation alone.

**Disposition:** The logical map now makes numerical sparsity non-dispositive
and eliminates the proposed middle class. Every system falls on one side of the
logical alternative: recurrent feedback is redundant to the expanding frontier,
or the system is premature and human discovery remains indispensable. Existing
evidence is insufficient to assign many actual systems because the required
ablations are rarely reported.

### 3. The pretraining diagnosis contains two competing theses

**Nodes:** T; C1-C7; F7.

The project says pretraining chose the wrong learning object because next-token
prediction does not produce a persistent, domain-grounded assistant learner.
It also accepts a capable pretrained substrate followed by bounded
constitutive post-training. LIMA makes the second possibility concrete: a small
fixed demonstration set can select useful assistant behavior from capabilities
largely acquired during pretraining.

If bounded post-training can create the desired closed learning system,
pretraining need not itself have produced the final learning subject. The
defect then belongs to the architecture of the complete deployed system, not
necessarily to representation pretraining. InstructGPT establishes objective
mismatch; it does not establish that pretraining should have optimized the
assistant objective or that a domain-grounded alternative would be superior.

**Force:** Major. The upstream claim is absent from the current C conclusion,
while the stronger wording in `current.md` is not entailed by the evidence.

**What would answer it:** Formulate the target as the complete learning system.
Pretraining may be a successful capability substrate; the design error occurs
when the substrate plus post-training never becomes a persistent learner of the
assistant objective. Preserve a narrower counterfactual hypothesis that a
different initial training regime might reduce the repair burden.

**Disposition:** `current.md` now identifies the stronger pretraining claim as
David's counterfactual hypothesis. The C branch still requires a system-level
reformulation before drafting.

### 4. Generated experience needs an independence condition

**Nodes:** Concepts 5 and 6; B1-B5; D3; D5; D8; F2; F7.

The audited definition counted observations and evaluations produced through
the operation of the learning system. This admitted a circular loop in which a
model generates examples and approves them with a correlated model. The current
map adds an independent-environment-or-verifier condition; its operational test
still needs development.

Silver and Sutton's experience proposal emphasizes action, grounded interfaces,
and consequences. Gao et al. show that optimization can improve a learned proxy
while worsening the underlying objective. DeepSeek-R1, AlphaProof, and
PlanSearch are persuasive positive cases precisely because tests, compilers,
formal proof checking, or rule-based outcomes constrain the learner outside its
own approval signal.

**Force:** Major. Without this condition, evaluative closure can describe a
closed self-confirmation loop rather than learning about a domain.

**What would answer it:** Define generated experience as interaction whose
relevant consequences are determined by the constituted environment or an
independently valid verifier, rather than by the candidate policy's own
endorsement. Treat proxy validity under optimization and behavioral expansion
as an empirical invariant, not an assumption carried by the word *valid*.

**Disposition:** The generated-experience definition now includes an
independently valid environment or verifier. Operational tests of independence
and validity under optimization remain required.

### 5. Historical influence and analytical importance require separate claims

**Nodes:** the former G3 and G4; current G1-G6 and H3-H4.

The title asks what “we” have learned, so the map needs a bounded account of who
*we* denotes and how the essay entered LLM discourse. It does not need to prove
that Sutton caused the development paradigm it examines. Historical dependence
and conceptual articulation are different relations.

Direct reception is stronger than the map records. Falcon says its design was
inspired by the Bitter Lesson; BIG-bench and PlanSearch cite it; OpenAI's
ImageGPT cites Sutton; and Anthropic's Activation Oracles explicitly call their
approach Bitter-Lesson compliant. The current sample also shows several
different meanings: corpus and hardware scaling, generalist models, search,
and avoidance of task-specific probes. Conversely, five foundational LLM
scaling papers in the existing bounded check did not cite Sutton, and recent
Llama 3 and Gemini 2.5 reports document hybrid post-training without presenting
it as a test of Sutton.

**Force:** Major if the article claims Sutton as the historical source of the
LLM paradigm; minor under the clarified articulation claim.

**What answers it:** Define *we* as the inspected frontier-LLM research and
engineering discourse. Use the direct reception cases to establish a real but
plural connection, the absent citations to limit causal claims, and Sutton's
text as a formulation against which the paradigm's internal consistency can be
tested. The article's criticism then remains valid whether Sutton is ultimately
right or wrong.

**Disposition:** Resolved in `logical_map.md`. The reception branch now
distinguishes causal influence from conceptual articulation and withholds both
consensus and field-distribution claims. The consistency test applies to any
program that adopts the general-learning wager; it does not require classifying
the field as a whole.

### 6. Domain constitution does not guarantee evaluative closure

**Nodes:** B4; B5; F1; F2; F7.

F2 assumes that a domain generates candidates, observations, and evaluations in
sufficient volume. F1 does not entail that assumption. “Helpful assistant” is
plural, context-sensitive, and partly normative; unlike checkmate or proof
checking, it lacks one stable independent terminal condition. Human-written
examples can initialize a policy without constituting a reliable evaluator for
new cases. LIMA supports the former and supplies no evidence for the latter.

Ongoing human revision can also represent legitimate governance of changing
goals rather than failure to automate a fixed task. Constitutional AI,
InstructGPT, and Gemini explicitly encode policies or preferences whose
authority is human and institutionally revisable. A closed evaluator may be
undesirable where the constitutive values themselves remain contested.

**Force:** Major practical limit.

**What would answer it:** Make F2 a substantive empirical condition. Limit the
positive proposal to paradigms with outcome measures that are sufficiently
observable, discriminating, and stable. Separate ongoing revision of legitimate
goals from recurring human diagnosis of task methods. The former changes the
constituted task; the latter is the target of the learning-locus critique.

**Disposition:** Revision and scope limit required.

### 7. Bounded constitution does not imply unbounded competence

**Nodes:** B3-B5; F2; F7.

Chess, code, and formal proof show that a bounded specification can generate an
enormous experience space. They do not establish infinite improvement. Chess is
finite and performance has a ceiling; every learner can saturate because of
capacity, exploration, distribution shift, or an uninformative evaluator. The
No Free Lunch result further shows that useful generalization depends on the
problem class and its assumptions.

**Force:** Moderate. The article needs only improvement beyond the finite human
seed, not literal infinity.

**What would answer it:** Replace claims of indefinitely expanding competence
with open-ended or compute-scalable improvement over the relevant horizon.
State the existence of an informative generator, an adequate learner, and
reachable better policies as conditions rather than consequences of bounded
rules alone.

**Disposition:** The logical map now limits expansion to the relevant learning
horizon. The learner, exploration, and informative-signal conditions remain to
be integrated into the domain branch.

### 8. The resource reply overstated Sutton's premise

**Nodes:** A4 and A4-R.

Sutton argues historically that computation becomes cheaper and that general
methods dominate in the long run. He also says human knowledge helps in the
short run and that the approaches need not conflict. He does not prove that
adequate resources exist for every task and horizon. A finite-resource
objection limits the practical prescription without simply leaving a formally
defined Sutton regime.

**Force:** Moderate.

**What would answer it:** Present resource sufficiency as a condition on the
article's application. A finite-horizon human-informed strategy does not refute
Sutton's long-run historical pattern, but it can defeat an immediate practical
recommendation.

**Disposition:** Resolved in the logical map as a practical-horizon limit. The
retired global-economics argument remains retired.

### 9. The field-level verdict lacks an observable classification method

**Nodes:** G3; G3-R; G4.

The map correctly says existence cases cannot establish a field-wide verdict,
but “the distribution of current systems” is not yet measured. Training details
are incomplete and the marginal cause of a gain is a counterfactual causal
claim. Llama 3 supplies a strong recurrent-human case: six post-training rounds
collected new preference annotations and SFT data, while synthetic generation
and reward modeling amortized part of that input. Gemini 2.5 similarly reports
successive human/model iterations, human-revised responses, a data reward model,
AI critics, and automated red teaming. These establish hybrid workflows, not
the fraction of gains caused by each component.

**Force:** Major evidentiary limit on a declarative answer to the title.

**What answers it within the article's scope:** Treat disclosed systems as
bounded illustrations. Verifier-grounded stages establish that the positive
architecture is possible; recurring human work in assistant pipelines motivates
the criticism but does not prove causal dependence. Preserve the title's
question form and decline a field-wide classification.

**Disposition:** Resolved as a scope limit. A comparative causal survey would be
a separate technical project rather than a prerequisite for this article.

## Additional objections the map does not yet contain

1. **Fixed-feedback falsifiability:** a disclosed system may lack the ablations
   needed to determine whether sparse human feedback is an efficiency aid or an
   indispensable source of new distinctions.
2. **Credit-assignment provenance:** an automated evaluator can still inherit a
   human-authored process target; its scale does not by itself show that the
   learner discovered the distinctions it applies.
3. **Governance rather than teaching:** recurrent human intervention can revise
   contested goals and constraints rather than prescribe methods within a fixed
   goal.
4. **Self-confirming closure:** a fixed AI judge and policy can jointly optimize
   a proxy while losing contact with the intended outcome.
5. **No-guarantee objection:** a generative domain and verifier make learning
   possible, not inevitable or indefinitely improving.
6. **Unlocking-versus-replacing falsifiability:** treating every powerful human
   meta-method as evidence of previously untapped algorithmic potential risks
   immunizing the thesis against counterexamples. The distinction needs an
   operational test: whether the prior learner could express, generate, test,
   and retain the intervention within its existing learning grammar.
7. **Cross-domain consequences:** domain-specific evaluators can conflict or
   omit externalities. A shared substrate does not itself solve routing,
   aggregation, or conflicts among standards.
8. **Observability:** proprietary pipelines may not disclose the ablations
   needed to locate marginal discovery, limiting any industry-wide conclusion.

## Claim-to-source audit

| Map claim | Status against source base | Best evidence or problem |
| --- | --- | --- |
| A1, A3, A5 | Supported with qualification | Sutton 2019 supports long-run compute, search, learning, and plateau claims; it does not require literally fixed human input. |
| A2 | Partly supported | Sutton accepts convolution, invariances, rules, and meta-methods; his criterion for permissible built-in structure remains underdeveloped. |
| A4-R | Overstated | Sutton supplies a long-run historical argument, not a proof of resource sufficiency in every horizon. |
| A6, A7-R | Analytical consistency principle | David's Harari-conversation formulation supplies direct provenance: the criticism concerns an architecture that changes governing regimes without an explicit transition principle, while an openly handcrafted or openly pragmatic paradigm remains outside that criticism. |
| B1, B2 | Analytical premises | Consistent with RL and search, but they are the article's reconstruction rather than direct quotations from Sutton. |
| B3 | Supported existence case | AlphaZero and AlphaGo Zero show rule-bounded self-play and outcome learning. |
| B4 | Split support | Chess supports a rule-based evaluator; LIMA supports a finite initial policy, not an evaluator that continues learning. |
| B5 | Supported only as possibility | AlphaZero, DeepSeek-R1, PlanSearch, and AlphaProof show expansion beyond a human seed, not unlimited competence. |
| C1 | Supported and temporally qualified | Sutton 2019 treats huge-data deep learning as a success; Sutton and Silver 2025 identify static human data as a coming limit. |
| C2, C3, C7 | Supported after wording correction | InstructGPT supports objective mismatch and assistant gains; post-training includes SFT and static preferences as well as evaluators. |
| C5 | Supported | LIMA supports high leverage from 1,000 curated demonstrations; it does not support continued learning after the set is fixed. |
| D1 | Too categorical | Humans can supply useful judgments, but validity and rate-limiting status vary. InstructGPT identifies a particular labeler group; Christiano et al. show sparse amortized feedback. |
| D3-D6 | Supported conditionally | InstructGPT, Bai et al., Constitutional AI, RLAIF, Christiano et al., and Gao et al. support both amortization and proxy-failure risks. |
| D7, D8 | Operational user thesis, not established by existing ablations | Recurring repairs can bottleneck progress; sparsity alone does not establish independence. The fixed-feedback counterfactual is the proposed test. |
| E1, E2 | Analytical attribution test | Plausible and useful, but requires a stable boundary between evaluator, learner, and engineers. |
| E3 | Supported existence case | Verifiable process rewards can evaluate independently completed formal subproblems. |
| E4, E5-R, E6 | Supported distinction | Sutton and Barto, AlphaZero, and outcome-derived process-reward work support learner-internal credit inference; excluding externally stipulated human method preference is the article's provenance criterion. |
| F1, F4-F6 | Supported as architecture and scope | AlphaZero and modular/shared-model research support supplied domains plus shared substrates; paradigm recognition remains outside the hypothesis. |
| F2, F7 | Conditional, not general | Strong for formal games, code, and proof; unestablished for open-ended assistant helpfulness. |
| G1-G6 | Supported as articulation plus bounded reception | Sutton's text states the paradigm; named cases establish plural uptake; absent citations in the foundational-paper sample limit causal and cornerstone claims. |
| H1, H2 | Defensible as a counterfactual test | Fixed input is sufficient; recurrent feedback is compatible only if the same expanding frontier remains reachable when further feedback is frozen. |
| H3, H4 | Supported as a conditional consistency test; evidence insufficient for field distribution | The test does not require Sutton to be correct or representative classification, while no system distribution or causal decomposition establishes a field-wide verdict. |

## Sources located for previously weak claims

1. **Sutton and Barto, *Reinforcement Learning: An Introduction* (2018):**
   canonical evidence that value learning and Monte Carlo control derive
   state/action distinctions by generalizing expected return across experience.
2. **Silver et al., AlphaZero (2018):** direct evidence that terminal game
   outcomes train state-dependent value predictions while MCTS supplies
   differentiated policy targets.
3. **Christiano et al., “Deep Reinforcement Learning from Human Preferences”
   (2017):** evidence that human supervision can cover about 0.1 percent of
   interactions, decline in rate as experience grows, and still be collected
   online to prevent reward exploitation.
4. **Burns et al., “Weak-to-Strong Generalization” (2023):** limited evidence
   that a stronger model can exceed a weak supervisor on some tasks; the method
   failed on ChatGPT preference data and does not establish persistent closure.
5. **The Llama 3 Herd of Models (2024):** a documented six-round post-training
   case with fresh human preference annotations, SFT data, synthetic data,
   reward modeling, rejection sampling, and DPO.
6. **Gemini 2.5 technical report (2025):** a current hybrid case combining
   successive human revisions, amortized human preference data, AI critics,
   predefined rubrics, and automated red teaming.
7. **OpenAI ImageGPT (2020) and Anthropic Activation Oracles (2025):** additional
   direct LLM-era and interpretability-era reception evidence, strengthening a
   named reception history without establishing consensus.
8. **Musk in Moonshots #220 (recorded 22 December 2025; published 6 January
   2026):** an illustrative statement that even a few manually completed cells
   would prevent a spreadsheet from competing with an all-computer one. The
   example expresses critical-path competition; it is not evidence about RLHF.

## Revision order

1. **Completed:** replace path neutrality with the distinction between
   learner-internal outcome-derived credit and externally imposed human process
   targets.
2. **Conceptually completed; empirically open:** operationalize the human
   critical-path question through a fixed-feedback scaling test.
3. Reframe the upstream pretraining claim at the level of the complete learning
   system.
4. **Partly completed:** add grounded independence and proxy-validity
   conditions; operationalize their validation.
5. **Completed:** distinguish Sutton's conceptual articulation from direct
   historical influence, preserve bounded reception, and define the inspected
   field without making reception history the article's main burden.
6. **Partly completed:** replace literal unboundedness with improvement over the
   relevant horizon; limit the domain inference to empirically adequate
   evaluators.
7. **Completed:** bound the empirical cases to illustration and preserve the
   evidentiary limit on any field-level answer.
