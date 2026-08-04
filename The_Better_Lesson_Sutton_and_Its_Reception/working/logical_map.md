# Logical Structure of *have we learnt the bitter lesson?*

## Thesis

**T.** Sutton's essay serves as a concise articulation of the paradigm shift
toward general methods that convert increasing computation into capability,
independently of the extent of its direct historical influence. Large-scale
pretraining realizes this paradigm through a general learning method.
Post-training realizes the same principle when a generative learning system
makes computational search and learning the marginal source of subsequent
improvement. Bounded constitutive input and evaluative closure provide the
stronger form in which direct task-specific human intervention terminates while
valid learning continues. A development program that makes the general-learning
wager and then restores recurring human method discovery as its critical path
abandons its organizing principle midway, whether or not Sutton's prescription
is ultimately correct.

- **Follows from:** A5, A6, A7-R, B5, C7, D8, E7, F7, G6, H4.

## Concepts

1. **Domain:** a rule-governed field that determines its problems, actions,
   observations, and standards of success.
2. **Constitutive input:** externally supplied information that establishes a
   domain or initializes its learner, including rules, examples, preferences,
   constraints, and methods.
3. **Search:** the generation and testing of candidates within a domain.
4. **Learning:** the retention of a change in policy, representation, rule, or
   heuristic on the authority of evidence produced within the domain.
5. **Generated experience:** observations and evaluations produced through
   interaction whose relevant consequences are determined by the constituted
   environment or an independently valid verifier.
6. **Evaluative closure:** the stronger capacity for constitutive input to
   remain fixed while valid learning continues through generated experience.
7. **Learning system:** the complete adaptive unit comprising the model,
   optimizer, search procedure, evaluator, memory, tools, and persistent agentic
   layer.
8. **Critical-path dependence:** an input is a scaling limit when progress
   across new behavior requires renewed instances of that input, irrespective
   of the input's numerical share of total operations.
9. **Epistemic provenance:** the source of authority for a task-specific
   distinction. A distinction derived from the constituted domain's formal
   structure, transitions, and outcomes belongs to the learner; a human semantic
   preference imposed independently of that evidence belongs to the engineers.
10. **Governing principle:** the rule that determines which method-discovery
    regime is authoritative and licenses transitions among regimes.

## A. Sutton's criterion

1. **A1 — Premise.** Search and learning convert increasing computation into
   increasing discovery.

   - **Supports:** A5.

2. **A2 — Premise.** Human-designed structures provide the initial conditions
   under which search and learning operate.

   - **Supports:** A5 and B5.

3. **A3 — Premise.** Continued dependence on newly supplied human solutions
   makes human discovery the rate-limiting source of improvement.

   - **Supports:** A5 and H2.

4. **A4 — Objection: resource limits.** Finite computational resources can make
   a human-informed method superior within a bounded practical horizon.

   - **Contradicts:** the unrestricted practical application of A1.
   - **A4-R — Reply.** A finite-resource strategy limits the practical horizon
     of Sutton's prescription while leaving its long-run scaling claim intact.
     - **Replies to:** A4.
     - **Limits:** A5 to horizons in which additional computation can be brought
       to bear.

5. **A5 — Intermediate conclusion.** A system follows the Bitter Lesson when
   computational search and learning govern marginal improvement after its
   initial conditions have been established.

   - **Follows from:** A1, A2, A3, and A4-R.
   - **Supports:** T, B5, and D8.

6. **A6 — Consistency premise.** An architecture organized by the Bitter
   Lesson must derive transitions in its method of discovery from an explicit
   governing principle.

   - **Follows from:** A5.
   - **Supports:** T and H4.

7. **A7 — Objection: pragmatic hybridism.** General learning and human-authored
   methods can be combined whenever each supplies a practical advantage.

   - **Contradicts:** the requirement that general learning govern marginal
     improvement.
   - **A7-R — Reply.** Pragmatic hybridism constitutes a coherent alternative
     paradigm when its selection rule is explicit. A program abandons the
     Bitter-Lesson paradigm when recurring human method discovery becomes
     authoritative while the program retains general learning as its stated
     organizing principle.
     - **Replies to:** A7.
     - **Follows from:** A5 and A6.
     - **Supports:** T and H4.

## B. Generative constitution

1. **B1 — Premise.** Search requires a generative field of admissible candidates
   and an evaluator of their consequences.

   - **Supports:** B5 and F2.

2. **B2 — Premise.** Learning requires evidence that authorizes the retention of
   successful changes within that field.

   - **Supports:** B5 and E2.

3. **B3 — Demonstration.** The rules and terminal conditions of chess form a
   bounded specification. Play generates an expanding body of positions,
   strategies, and evidence.

   - **Instantiates:** B1 and B2.
   - **Supports:** B4.

4. **B4 — Premise.** Rules and examples can constitute an evaluator or initial
   policy whose operation extends across newly generated cases.

   - **Supported by:** B3 and the finite-alignment evidence in C5.
   - **Supports:** B5 and F1.

5. **B5 — Intermediate conclusion.** Constitutive input can remain bounded while
   generated experience and learned competence expand beyond the human seed
   across the relevant learning horizon.

   - **Follows from:** A2, B1, B2, B3, and B4.
   - **Supports:** T, D3, and F7.

## C. Pretraining and the assistant objective

1. **C1 — Premise.** Pretraining acquires capabilities through a general
   statistical method applied at computational scale.

   - **Instantiates:** A1.
   - **Supports:** C7 and H1.

2. **C2 — Premise.** Next-token prediction and assistant performance constitute
   distinct learning objectives.

   - **Supports:** C3 and C7.

3. **C3 — Evidence.** Post-training improves assistant performance by adding
   supervision and evaluative structure directed toward assistant behavior.

   - **Supported by:** base-versus-post-trained comparisons.
   - **Supports:** C7.

4. **C4 — Objection: post-training success.** The empirical gains of
   post-training refute the proposal to eliminate post-training.

   - **Contradicts:** any inference from C1 to the sufficiency of pretraining.
   - **C4-R — Reply.** C2 and C3 establish the assistant-objective mismatch. C7
     classifies the post-training structure that resolves that mismatch.
     - **Replies to:** C4.
     - **Supports:** C7.

5. **C5 — Evidence.** Small fixed alignment datasets can exert substantial
   control over a capable pretrained model.

   - **Supports:** B4 and D3.
   - **Contradicts:** the claim that useful assistant behavior always requires an
     expanding alignment corpus.

6. **C6 — Objection: finite alignment sufficiency.** A fixed alignment set can
   establish durable assistant behavior.

   - **Contradicts:** a general diagnosis of post-training as recurrent human
     dependence.
   - **C6-R — Reply.** Durable initial behavior satisfies generative
     constitution. Evaluative closure additionally governs continued learning
     after the alignment set has become fixed.
     - **Replies to:** C6.
     - **Supports:** C7 and D8.

7. **C7 — Intermediate conclusion.** Post-training success establishes the
   assistant objective. Its relation to the Bitter Lesson is determined by the
   evaluative structure that produces subsequent improvement.

   - **Follows from:** C1, C2, C3, C4-R, C5, and C6-R.
   - **Supports:** T, D8, and H3.

## D. Evaluative closure

1. **D1 — Premise.** Human outcome judgments can supply valid evaluative
   evidence. Their production remains an independently human input channel.

   - **Supports:** D8 and H2.

2. **D2 — Objection: deployment feedback.** Expanding deployment produces an
   expanding volume of human outcome judgments.

   - **Contradicts:** an inference from D1 to a fixed human-feedback channel.
   - **D2-R — Reply.** Deployment volume establishes the availability of human
     judgments. Computational scalability requires a counterfactual result:
     after further task-specific human feedback is frozen, increasing
     computation and generated experience must continue to expand the reachable
     performance frontier.
     - **Replies to:** D2.
     - **Restores:** D1.
     - **Supports:** D8 and H3.

3. **D3 — Premise.** A learned reward model converts bounded constitutive input
   into scalable evaluation when its judgments remain valid across newly
   generated behavior.

   - **Supported by:** B5 and C5.
   - **Supports:** D8.

4. **D4 — Objection: RLHF automation.** Reward-model training already amortizes
   finite human comparisons across computationally generated samples.

   - **Contradicts:** a categorical classification of RLHF as non-scaling.
   - **D4-R — Reply.** A fixed reward model satisfies evaluative closure
     throughout the behavioral range in which its judgments remain valid.
     Recurrent human refreshes require the fixed-feedback counterfactual. When
     the same expanding frontier remains reachable without them, they provide
     an efficiency advantage. When progress requires new human distinctions,
     the human channel remains on the critical path.
     - **Replies to:** D4.
     - **Supports:** D8.

5. **D5 — Premise.** An AI evaluator can produce preference judgments at
   computational scale.

   - **Supports:** D8.

6. **D6 — Objection: RLAIF scalability.** AI-generated feedback removes human
   label production from the operative learning loop.

   - **Contradicts:** the claim that alignment feedback necessarily scales with
     human labor.
   - **D6-R — Reply.** Evaluative closure requires stable judgments across the
     learner's expanding behavior. Recurrent task-specific human repair of the
     AI evaluator restores human judgment as a necessary input.
     - **Replies to:** D6.
     - **Supports:** D8.

7. **D7 — Premise.** Where each new behavioral region requires a new human
   diagnosis and repair, competence expands only through a corresponding
   extension of human judgment.

   - **Supports:** D8 and H2.

8. **D8 — Intermediate conclusion.** Evaluative closure occurs when the human
   contribution can remain fixed and the evaluator continues to support learning
   across the expanding behavior of the system. It is a stronger sufficient
   condition for A5.

   - **Follows from:** A5, B5, C7, D3, D4-R, D5, and D6-R.
   - **Supports:** T, E7, F7, H1, and H2.
   - **D8-O — Objection: sparse recurrent supervision.** Human feedback can
     cover a declining fraction of interactions while its judgments are
     amortized across computationally generated experience.
     - **Contradicts:** the inference from recurrent supervision to a human
       scaling limit.
     - **D8-O-R — Reply.** Numerical sparsity does not establish causal
       independence. A composite learning system scales only as far as its
       least scalable indispensable component. Freeze further task-specific
       human feedback and increase computation: if the same expanding
       performance frontier remains reachable, the feedback is an efficiency
       advantage; if progress stalls, drifts, or requires new human
       distinctions, the human channel is the critical-path source of the
       missing discovery.
       - **Replies to:** D8-O.
       - **Restores:** D8 as the decisive sufficient test.
       - **Supports:** H2, H3, and H4.

## E. The location of discovery

1. **E1 — Premise.** Engineers perform the task-specific discovery when they
   diagnose an operative failure and encode its remedy.

   - **Supports:** E7 and H2.

2. **E2 — Premise.** The learning system performs the task-specific discovery
   when domain-internal evidence selects and retains the remedy.

   - **Supported by:** B2.
   - **Supports:** E7 and H1.

3. **E3 — Premise.** Intermediate actions receive independent evaluation when
   each action completes a subproblem defined by the domain.

   - **Supports:** E7.

4. **E4 — Premise.** The learning system may compare trajectories and
   iterations, generalize across them, and infer the contribution of states,
   actions, and intermediate steps from the constituted domain's transitions,
   formal structure, and outcomes.

   - **Supports:** E7.

5. **E5 — Objection: process evaluation.** Distinguishing reliable methods from
   fortunate errors requires judgments about the path rather than its terminal
   result alone.

   - **Contradicts:** an outcome-only account of learning.
   - **E5-R — Reply.** When the system derives those distinctions from repeated
     domain-internal evidence, the relevant discovery belongs to the learner.
     When human evaluators stipulate the legitimate route independently of such
     evidence, the relevant discovery belongs to the engineers.
     - **Replies to:** E5.
     - **Supports:** E6 and E7.

6. **E6 — Premise.** External method instruction occurs when human semantic
   preference authoritatively ranks routes beyond distinctions derivable from
   the constituted domain's formal structure and outcomes.

   - **Supported by:** E5-R.
   - **Supports:** E7.

7. **E7 — Intermediate conclusion.** Sutton-like learning joins evaluative
   closure with learner-generated task-specific discovery.

   - **Follows from:** D8, E1, E2, E3, E4, E5-R, and E6.
   - **Supports:** T, F7, H1, and H2.

## F. Domain-based post-training

1. **F1 — Premise.** Human researchers constitute a domain through rules,
   interfaces, initial examples, constraints, and standards of success.

   - **Supported by:** B4.
   - **Supports:** F2 and F7.

2. **F2 — Premise.** The domain generates candidates, observations, and
   evaluations in sufficient volume for search and learning.

   - **Supported by:** B1 and B2.
   - **Supports:** F7.

3. **F3 — Objection: fragmentation.** Domain decomposition can block transfer
   and create a routing problem among isolated models.

   - **Contradicts:** an architecture that assigns an independent model to every
     domain.
   - **F3-R — Reply.** A shared pretrained model can participate in several
     domain-specific learning systems. Domain boundaries govern evaluative
     structure and generated experience.
     - **Replies to:** F3.
     - **Supports:** F4 and F7.

4. **F4 — Premise.** A shared pretrained model can participate in several
   domain-specific learning systems.

   - **Supported by:** F3-R.
   - **Supports:** F7.

5. **F5 — Premise.** Human identification of the relevant paradigm supplies the
   starting point of each domain.

   - **Supports:** F7.

6. **F6 — Objection: paradigm change.** A general learner requires the capacity
   to identify and revise its paradigms.

   - **Contradicts:** the completeness of F5 as a general theory of intelligence.
   - **F6-R — Reply.** Domain-based post-training begins from established
     paradigms. Paradigm discovery and revision form a subsequent research
     problem.
     - **Replies to:** F6.
     - **Limits:** F7 to learning within established paradigms.

7. **F7 — Intermediate conclusion.** Domain-based post-training converts bounded
   constitutive input into evaluatively closed systems that generate their own
   task-specific discoveries within established paradigms.

   - **Follows from:** B5, D8, E7, F1, F2, F3-R, F4, F5, and F6-R.
   - **Supports:** T and H1.

## G. Reception in frontier LLM research and development

1. **G1 — Premise.** Sutton's 2019 essay articulates the transition from
   human-authored solutions to general search and learning methods that exploit
   increasing computation. His later experience program extends that principle
   from inherited human data to agent-generated experience.

   - **Supports:** G3 and G6.

2. **G2 — Evidence.** ImageGPT, Falcon, BIG-bench, PlanSearch, and Activation
   Oracles explicitly invoke the Bitter Lesson in model design, benchmarking,
   search, and interpretability.

   - **Supports:** G3 and G6.

3. **G3 — Premise.** Historical causation and conceptual articulation are
   distinct. An essay can express the governing logic of a technological shift
   without originating that shift or becoming its technical cornerstone. Its
   direct reception assigns several meanings to the lesson: scalable data and
   hardware, generalist methods, computational search, and replacement of
   task-specific probes.

   - **Follows from:** G1 and G2.
   - **Supports:** G6.

4. **G4 — Objection: limited historical influence.** Named citations and design
   statements cannot establish that Sutton caused foundational LLM development
   or supplied a common field-wide doctrine.

   - **Contradicts:** a consensus or cornerstone inference from G2.
   - **G4-R — Reply.** The bounded absence of Sutton citations from five
     foundational LLM papers limits claims of technical dependence. It leaves
     intact the essay's use as an explicit formulation of a paradigm visible in
     independent system development, while the named sources establish a
     traceable and semantically plural reception.
     - **Replies to:** G4.
     - **Supports:** G6.

5. **G5 — Evidence.** Disclosed post-training systems combine recurring human
   judgments and revisions with reward models, AI critics, synthetic data,
   automated search, and verifier-grounded reinforcement learning.

   - **Supports:** G6 and H3.

6. **G6 — Intermediate conclusion.** The essay's limited direct historical
   influence does not determine its analytical importance. It clearly
   articulates the scalable-method paradigm exemplified by large-scale LLM
   development, and named sources establish a real but plural reception. The
   available evidence leaves a field-wide verdict on evaluative closure or the
   locus of discovery unestablished.

   - **Follows from:** G1, G2, G3, G4-R, and G5.
   - **Supports:** T, H3, and H4.

## H. Verdict

1. **H1 — Positive conclusion.** LLM development follows the Bitter Lesson
   wherever additional computation yields additional learner-generated
   discovery after constitutive input has become fixed.

   - **Follows from:** C1, C7, D8, E7, and F7.
   - **Supports:** H4 and T.

2. **H2 — Critical conclusion.** LLM development violates the Bitter Lesson
   wherever progress requires a parallel expansion of task-specific human
   intervention.

   - **Follows from:** A3, D7, E1, and E7.
   - **Supports:** H4 and T.

3. **H3 — Objection: field-level evidence.** An existence case of recurrent
   human feedback cannot establish a general diagnosis of frontier LLM research
   and development, still less of machine learning as a whole.

   - **Contradicts:** the inference from individual post-training systems to a
     field-wide verdict.
   - **H3-R — Reply.** The article's conditional consistency test does not
     require a representative classification of the field. Disclosed systems
     can illustrate the alternatives through H1 and H2 while a field-wide
     verdict remains withheld.
     - **Replies to:** H3.
     - **Follows from:** D2-R, G5, and G6.
     - **Supported by:** G5 and G6.
     - **Limits:** H4 to the available comparative evidence.

4. **H4 — Final conclusion.** Systems whose expanding performance frontier
   remains reachable from fixed constitutive input through learner-generated
   discovery satisfy evaluative closure and have learnt the Bitter Lesson in
   its stronger form. Systems in which recurrent task-specific
   human correction remains the marginal source of progress have failed to
   learn it. Sparse or declining-rate human feedback creates no third category.
   If the same expanding performance frontier remains reachable after further
   task-specific human input is frozen, the recurrent feedback is redundant to
   that frontier. If it is not, the system is premature and human discovery
   remains on its critical path. The lesson's ultimate truth is independent of
   this consistency judgment: a program that adopts the general-learning wager
   while making recurring human method discovery authoritative has abandoned
   the wager midway. Frontier LLM research has received the lesson as a plural
   scaling maxim; the available evidence does not establish a field-wide
   distribution across the two classes.

   - **Follows from:** A6, A7-R, D8-O-R, G6, H1, H2, and H3-R.
   - **Supports:** T.
