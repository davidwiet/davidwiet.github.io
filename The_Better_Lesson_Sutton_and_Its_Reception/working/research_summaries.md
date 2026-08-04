# Online Research Summaries

Status: first deep-research pass completed 31 July 2026; targeted LLM-data,
experience, reception, bounded-system, post-training-alignment, and feedback-
scalability passes completed 2 August 2026; credit-provenance and fixed-feedback
interpretation revised, with the Musk illustration verified, 4 August 2026.
This is the canonical research record for the article, not manuscript prose.
Resource and global-economics records are retained as research history but are
no longer part of the planned argument.

## Questions investigated

- **Factual:** What does Sutton's 2019 essay actually claim? What architectures
  and training arrangements were used in the game-playing examples? What does
  the empirical literature report about shared models, routing, modularity,
  transfer, interference, compute scaling, and energy use?
- **Interpretive:** Does Sutton's claim entail one monolithic learner? Has a
  traceable reception extended the essay from opposition to hand-authored
  domain content into suspicion of decomposition or engineered scaffolding?
- **Normative:** What kinds of built-in distinctions remain compatible with the
  lesson, and when should a boundary be given, learned, revised, or dissolved?
- **New focal question:** Is enlarging a corpus of human-produced data the kind
  of scalable learning Sutton meant, and how does it differ from continual,
  consequence-grounded experience?
- **Constructive question:** Under what conditions can enough prior knowledge
  encapsulate a domain so that compute produces new, evaluable experience
  rather than requiring an indefinitely expanding stock of human examples?
- **Post-training question:** Which alignment interventions report the outcome
  of an attempt, and which supply desired behavior, policies, distinctions, or
  solution methods while being described generically as feedback?
- **Feedback-scaling question:** Can the evaluative signal be generated and
  corrected as computation grows without recurring human judgment becoming the
  marginal source of improvement, and does AI-generated feedback preserve
  outcome grounding rather than merely automate a human teaching policy?
- **Process-supervision question:** Can fine-grained signals be derived from the
  same outcome criterion as a solution to credit assignment, or do they encode
  an independently preferred behavior or route?

## Findings that may now anchor the argument

1. **Sutton does not argue for one model or one parameter set.** He argues for
   general methods that exploit increasing computation, especially search and
   learning, and against placing our discovered descriptions of the world into
   the agent. He explicitly says computation and human knowledge need not
   conflict, acknowledges convolution and invariances, and leaves the criterion
   for acceptable inductive structure underdeveloped.
2. **The relevant distinction is not architecture versus scale.** Sutton's 2025
   OaK proposal is itself a structured model-based RL architecture with learned
   components, subtasks, options, models, planning, and continually created
   abstractions. A more faithful distinction is fixed world-content versus
   meta-methods capable of learning and revising useful structure.
3. **AlphaZero supports algorithmic generality but not a single joint learner.**
   The same algorithm, hyperparameters, and convolutional architecture were
   reused across chess, shogi, and Go, but the researchers trained separate
   instances. The game boundary and rule-based encodings were supplied. This is
   a strong precedent for David's distinction, although no classifier learned
   or inferred the game in the reported experiment.
4. **The modularity literature supports adaptive sharing, not permanent total
   separation.** Learned branching and conditional routing can reduce negative
   transfer and computation, while shared representations can improve latency,
   transfer, and generalization. The empirical question is where and how much
   to share, and whether the routing boundary remains learnable and revisable.
5. **Unified learners are genuine counterevidence.** Gato and Multi-Game
   Decision Transformer show that one set of weights can act across markedly
   heterogeneous tasks or dozens of games. They refute any universal claim that
   separate downstream learners must be better, but do not establish that one
   shared model is always more sample-, compute-, or energy-efficient.
6. **Two receptions must be distinguished.** Broad ML scholarship uses Sutton
   to endorse scalable, data-driven, general methods, but the inspected sources
   do not show a broad commitment to monolithic learning. The strongest move
   from Sutton to skepticism about scaffolding, decomposition, or specialized
   components occurs in contemporary LLM and agent-engineering commentary. The
   current sample establishes named examples, not consensus in either ML
   research or the LLM industry.
7. **The affirmative resource argument is out of scope, but resource sufficiency
   remains a boundary premise.** The research rejects a generic exponential-
   resource claim, and David has retired arguments about aggregate efficiency or
   global economics. He now retains insufficient resources as the cleanest way
   to decline Sutton's prescription: if enough computation will not exist within
   the relevant horizon, one has left the regime assumed by the lesson rather
   than refuted its conditional conclusion. The source records remain below to
   preserve the research trail.
8. **“Human knowledge” needs to be disaggregated.** The inspected cases now
   suggest four roles: constituting the task through rules, objectives,
   interfaces, and verifiers; supplying outcome-grounded feedback at terminal
   or process resolution; specifying desired solutions, behavior, or policy;
   and designing meta-methods or inductive structure through which the system
   can learn. Sutton most clearly rejects the third, relies on the first two in
   his canonical examples, and accepts at least some of the fourth. This is an
   interpretive synthesis to be tested, not a quotation from Sutton.
9. **Static-data pretraining is both inside and at the limit of the 2019
   lesson.** Sutton explicitly cites deep learning with huge training sets as a
   successful replacement for human-authored speech knowledge. More data is
   therefore not inherently contrary to his position. The sharper distinction
   is between scaling a developer-run training process over inherited examples
   and scaling an agent's persistent capacity to generate evidence through
   action and adapt to consequences.
10. **The “next victim” interpretation is Sutton's own later view.** In a 2025
    interview, Sutton says LLMs exploit massive computation only up to the
    Internet's limits while also inserting human knowledge; he expects systems
    learning from experience to supersede them as another Bitter Lesson case.
    Silver and Sutton's “Era of Experience” develops the same contrast in
    detail. The article should not present it as a newly discovered correction
    of Sutton.
11. **The essay is better described as an influential frame than a demonstrated
    technical cornerstone of LLM development.** A bounded full-source search of
    Kaplan et al. (2020), Brown et al. (2020), Hoffmann et al. (2022), Chowdhery
    et al. (2022), and the GPT-4 technical report (2023) found no citation to
    Richard Sutton or *The Bitter Lesson*. Absence of citation cannot establish
    absence of influence, and later commentary explicitly links the essay to
    scaling. It does show that the foundational technical claims did not depend
    overtly on Sutton's essay.
12. **The current industry is already partly moving toward experience-like
    regimes.** OpenAI publicly describes o1 as scaling reinforcement learning
    and its deep-research model as learning end-to-end from multi-step browsing
    and tool-use tasks. Silver and Sutton cite execution feedback, formal
    verifiers, and self-generated proofs as early transition cases. The article
    should target static-data maximalism rather than describe all current LLM
    development as corpus enlargement.
13. **A direct criticism of Sutton remains, but it must be precise.** Silver and
    Sutton acknowledge that experience and human data are not opposites, allow
    human interaction as grounded experience, and propose user-guided reward.
    Sutton separately acknowledges that researchers currently supply useful
    generalization structure. What their account underdevelops is how action
    spaces, observations, instruments, objectives, verifiers, and selected
    environmental signals constitute the problem and limit the independence and
    scope of discovery. “Grounded” feedback relocates rather than automatically
    removes prior human framing.
14. **There is now direct evidence of an LLM-era Bitter Lesson reception.** The
    Falcon technical report says its design was inspired by Sutton and makes
    scalability across performance, data, and hardware an organizing
    principle. BIG-bench cites Sutton when arguing against prioritizing tasks
    likely to yield to scale, and PlanSearch invokes the lesson to distinguish
    learning from search. These examples establish a traceable technical and
    scholarly reception; they still do not establish field-wide consensus or
    causal influence over the Transformer itself.
15. ***Attention Is All You Need* is a precursor, not reception evidence.** It
    appeared in 2017, two years before Sutton's essay. Its removal of recurrence
    in favor of a parallelizable, general architecture later exemplified the
    scalable-method philosophy, but the paper is also a major human-designed
    architectural intervention. It can illustrate retrospective affinity, not
    historical dependence on Sutton.
16. **The bounded-system hypothesis has strong conditional existence cases.**
    PlanSearch improves code generation by spending inference compute on
    diverse plans evaluated against coding tasks. DeepSeek-R1 obtains effective
    large-scale RL in mathematics, code, and logic where rule-based rewards,
    compilers, and tests are reliable. AlphaProof combines Lean verification,
    tree search, RL, and self-generated problems, with continuing gains on a
    held-out distribution. The common factor is not a topical label but an
    environment or verifier that can distinguish admissible progress.
17. **The data claim must distinguish inherited data from generated
    experience.** AlphaProof reportedly expands about one million
    natural-language problems into roughly eighty million formal problems, and
    self-play or test-time RL can generate further trajectories. Encapsulation
    does not make the volume of learning experience irrelevant; it can make the
    finite stock of pre-existing human solutions cease to govern marginal
    improvement.
18. **A domain must be functional rather than merely taxonomic.** A usable
    learning system needs a problem or state space, an action or hypothesis
    language, a transition process or generator, a feedback mechanism, and a
    held-out task distribution. “Law,” “medicine,” or “physics” does not by
    itself supply these conditions. Broad pretraining may still be required to
    furnish the prior competence from which a bounded specialist begins.
19. **The positive architecture may combine a shared substrate with
    paradigm-specific learning systems, not necessarily separate foundation
    models.** Domain-specific search and RL can coexist with a general
    pretrained model and cross-domain transfer. Conditional routing is an
    available architectural possibility, but the present hypothesis does not
    explain how the applicable paradigm is identified. The article should argue
    for decomposing feedback and learning regimes where their conditions differ,
    not for epistemically isolated topical models.
20. **Claims that Sutton recanted or contradicted the Bitter Lesson are a real
    reception phenomenon, but they identify a tension rather than a simple
    reversal.** In a 2023 X exchange, a respondent asked whether Sutton's
    agreement with data-efficient new architectures ran counter to the lesson;
    Sutton replied that massive computation does not remove the need for data
    efficiency. After his 2025 Dwarkesh interview, Zvi Mowshowitz described the
    position as at least “kinda” backtracking, while other commenters called it
    recanting or revisionist history. The mistake is to equate the 2019
    principle with scaling static data and parameters. Yet the objection is not
    wholly baseless: the 2019 essay praised huge training sets and primarily
    opposed human knowledge built into methods, whereas Sutton's later account
    also classifies human-produced training content as inherited knowledge.
    His meta-principle is continuous, but the extension of its target requires
    explanation.
21. **Representative post-training stacks are hybrids, not streams of natural
    outcome feedback.** InstructGPT used human-written demonstrations, detailed
    instructions to labelers, ranked model outputs, a learned reward model, and
    PPO. Each element has a different epistemic role even though the pipeline is
    commonly grouped under reinforcement learning from human feedback.
22. **Preference optimization need not involve an acting learner receiving a
    consequence.** DPO rewrites the standard RLHF objective as a direct loss over
    static preferred/dispreferred response pairs. This establishes that
    *feedback* in current alignment terminology can mean offline supervised
    fitting to recorded human judgments rather than environmental interaction.
23. **Some alignment methods explicitly install human-authored normative
    structure.** Constitutional AI begins with a written list of principles and
    uses those principles in critique, revision, preference modeling, and RL.
    Deliberative alignment directly teaches a model human-written safety
    specifications and trains it to reason over them. These are strong examples
    of instruction or policy constitution, not merely terminal approval.
24. **Process supervision directly distinguishes outcome from path-level
    intervention.** Lightman et al. define outcome supervision as feedback on a
    final result and process supervision as feedback on each intermediate
    reasoning step. Their PRM800K dataset contains 800,000 human step-level
    labels. This validates process resolution as a distinct intervention point,
    but does not decide whether a particular step label merely evaluates local
    contribution to the outcome or supplies a preferred reasoning method.
25. **A learned approval signal is not automatically equivalent to a domain's
    terminal condition.** Reward-model overoptimization can improve the learned
    proxy while reducing performance under the underlying evaluator. The
    checkmate analogy therefore requires a validity argument: what generated
    the judgment, what it represents, and whether optimization preserves its
    connection to the actual outcome.
26. **Silver and Sutton permit human feedback, so human origin is not the right
    dividing line.** Their proposed bi-level scheme allows user satisfaction at
    the top level and grounded environmental measures below it. The unresolved
    issue is which human interventions constitute the objective or report its
    consequences, and which import desired answers, procedures, or policies.
    This boundary claim is an interpretation of the combined evidence, not a
    distinction Silver and Sutton themselves formulate.
27. **David's one-shot/ongoing distinction opens the issue but does not settle
    it.** A learning system can undergo repeated trials while receiving only
    terminal win/loss results, and fine-grained signals can sometimes be derived
    from those results. The stronger candidate distinction asks whether the
    signal remains answerable to the constituted outcome or supplies an
    additional behavioral target. This is analytical synthesis, not an
    empirical finding from a single source.
28. **Evaluating and steering are not mutually exclusive causal descriptions.**
    Any feedback used for learning steers future behavior, and every engineered
    learning system has a desired result. The stronger distinction is between a
    policy selected because it improves a constituted outcome and a policy or
    route supplied as an additional target. This is analytical synthesis.
29. **Reward-shaping theory supplies a formal version of the distinction.** Ng,
    Harada, and Russell show that some added intermediate rewards preserve the
    original optimal policy, while unrestricted shaping can produce a policy
    that is suboptimal under the original task reward. Policy invariance
    therefore describes an important technical boundary, although its theorem
    assumes an MDP rather than an open-ended language task. The stronger project
    question concerns provenance: whether the learner derives the shaping
    distinction from outcome-bearing experience or receives a human-authored
    semantic process target.
30. **Process supervision can in principle be recovered from outcomes.** Jia,
    Rakhlin, and Xie show under stated coverage assumptions that trajectory-level
    rewards can be transformed into per-step rewards, and that a policy's
    advantage function can serve as an optimal process reward model when
    rollouts or a verifier are available. This is admissible under David's
    revised criterion when the learning system derives the credit assignment
    solely from the constituted domain's evidence.
31. **Automated process rewards already operationalize this possibility.**
    Setlur et al. define step-level progress as the change in probability of
    eventual correctness and learn automated process advantage verifiers. Yuan
    et al. use symbolic or algorithmic oracles to provide dense turn-level
    rewards. Both may qualify when their distinctions are derived from the
    constituted outcome system; each still requires analysis of proxy validity
    and any human-authored process target embedded in the evaluator.
32. **A current research line goes further and internalizes process signals.**
    Ding et al. train a model to identify, correct, and reuse failed trajectories
    under outcome-only supervision, explicitly contrasting internally generated
    process signals with external human annotations. This preprint supplies
    positive evidence for the revised criterion: discovery of useful process
    distinctions can belong to the learning system rather than the evaluator.
33. **Process-level reward must be classified by epistemic provenance.**
    *Terminal or propagated outcome* transmits a completed result. *Independent
    subproblem evaluation* judges a step that is itself a completed outcome
    under domain rules. *Learner-derived credit* infers step or state value by
    comparing and generalizing across outcome-bearing trials. *External semantic
    process targeting* supplies a preferred route on human authority. David
    permits the first three and rejects the fourth as task-specific method
    discovery performed by the engineers. This taxonomy is the project's
    synthesis, not terminology standardized by the literature.
34. **David replaced path neutrality with epistemic provenance.** The learner
    may compare trajectories, aggregate evidence, generalize across iterations,
    and distinguish reliable methods from lucky errors. The distinction must be
    derived solely from the constituted domain's formal structure, transitions,
    and outcomes. A human evaluator may not make its own semantic account of the
    legitimate method authoritative. This is David's revised criterion.
35. **Positional weighting remains a valid special case.** A fixed schedule may
    reward later steps more than preliminary ones because they are temporally
    closer to the observed outcome. It is one form of retroactive propagation,
    not the exclusive admissible form of credit assignment.
36. **“Same degree of success” requires a complete outcome description.** If a
    route differs in harm, rule compliance, relevant resource use, delay, or any
    other consequence that belongs to the constituted task, the outcomes are not
    equivalent. Once all legitimate outcome dimensions are represented, an
    external human evaluator may not introduce a residual preference among
    genuinely equivalent methods. The learner may still infer predictive
    distinctions from repeated evidence. This is analytical synthesis.
37. **David retains the job-discrimination analogy for external ranking.** The
    structural analogy is that an evaluator claims to judge a legitimate
    outcome while ranking otherwise equivalent cases by an outcome-irrelevant
    human preference. It does not apply to distinctions learned from outcome
    evidence. This is a user-proposed analogy; no legal research has yet been
    performed, so the article must not represent it as employment-law doctrine.
38. **David proposes the locus of learning as a central diagnostic.** The
    question is whether the model learns how to improve or whether engineers
    inspect failures, discover the relevant task-specific distinction or method,
    and encode their discovery into demonstrations, rubrics, constitutions, or
    rewards. This is a user-proposed formulation of the argument.
39. **The relevant learner may be larger than the model.** Search, memory,
    tools, optimization, and a persistent application-level agent can change
    future behavior even when an individual model invocation or its weights do
    not update online. The defensible contrast is therefore *learning system
    versus human training apparatus*, not necessarily model weights versus
    engineers. This is analytical clarification.
40. **Human task constitution is compatible with system learning.** Engineers
    inevitably establish paradigms, objectives, constraints, interfaces, and
    general learning machinery. The Bitter-Lesson boundary concerns repeated
    task-specific epistemic work: who must explain each new failure and
    formulate the correction? A useful counterfactual is whether improvement
    continues when engineers keep supplying valid outcomes but stop diagnosing
    methods. This is analytical synthesis.
41. **The locus test makes hybrid attribution possible.** Demonstrations and
    process rubrics place more task-specific discovery in the human apparatus;
    isolated outcome feedback places more discovery in the learning system.
    Many post-training pipelines mix both. The article should identify the
    marginal source of each improvement rather than force the whole pipeline
    into a binary category. This is analytical synthesis.
42. **David proposes clarifying Sutton's search and learning separately.**
    Search explores possibilities already made available by the paradigm and
    learns new facts from testing particular candidates. Learning is not merely
    the accumulation of rules or heuristics; a method change must be warranted
    from within the same rule-governed system used to attempt and evaluate the
    task. This is a user-proposed development of the argument.
43. **A search space can be available without being enumerated.** “Accessible in
    advance” should mean intensionally generable under the paradigm's rules, not
    that every option is already represented as an item in a list. Search adds
    evidence about generated candidates rather than new human stipulations about
    the space or preferred route. This is analytical clarification.
44. **Internal warrant is stronger and safer than requiring an explanation of
    why.** A learning system may establish a heuristic empirically through
    improved outcomes without producing a causal or verbal demonstration. The
    decisive condition is that the evidence selecting and retaining the change
    is available under the constituted domain's existing actions,
    consequences, and success criteria. This is analytical clarification.
45. **Constitutive rules and operative rules have different statuses.** The
    former create the problem-space and remain fixed within David's present
    paradigm-bound hypothesis. The latter are policies, representations, or
    heuristics that learning may revise. Treating an externally supplied
    operative rule as authoritative without internal evidence makes its warrant
    external to the learner. This is analytical synthesis.
46. **Hybrid attribution is possible but asymptotically secondary.** A candidate
    method may originate with a human, be validated by system-generated outcome
    evidence, and be retained by an automated learner. Those roles can be
    separated when diagnosing a pipeline. David's correction is that this
    logical hybrid should not be presented as a coequal method: relative to
    automated systemic search, the human-proposed possibility set becomes
    negligible at scale. This is a user correction to the prior analytical
    emphasis.
47. **“Outrun” and “outperform” name a difference in scaling processes.**
    Sutton says human knowledge can help in the short term but that general
    search and learning dominate in the long run because they continue to
    exploit increasing computation. He does not quantify a candidate ratio
    tending to zero. Moreover, one human-designed meta-method can have
    disproportionate leverage. The faithful inference is that a continuing
    stream of human-proposed domain methods is a bounded, non-scaling source of
    discovery that systemic generation and testing eventually overwhelms. This
    is source-grounded analytical synthesis.
48. **David treats exceptional human leverage as evidence of untapped
    algorithmic potential.** If one human-designed meta-method produces an
    enormous improvement, the relevant dimension of the algorithm's potential
    was not yet being exploited. The human intervention may open a field of
    possibilities, but automated search and learning generate and test the
    discoveries within it at scale. The intervention therefore does not establish
    human proposal as a competitive discovery process. This is a user correction
    to the prior qualification.
49. **Unlocking a learner must be distinguished from replacing it.** If an
    intervention exposes possibilities already generable and testable under the
    existing learning grammar, it reveals latent potential. If it changes the
    hypothesis language, representation space, update rules, or kinds of methods
    the learner can express, it may constitute a new learner. David's current
    hypothesis does not claim autonomous discovery of paradigms or of every
    meta-method. This is a scope-preserving analytical qualification.
50. **David's brute-force code breaker is the limiting case of outrunning human
    knowledge.** A human possesses the exact solution while the system possesses
    no solution-specific information. Given a finite code space, immediate
    verification, and sufficiently rapid trials, systemic search can nevertheless
    reach and use the code before the human can transmit or enter it. Human
    knowledge has a fixed distance advantage; search has a scalable rate
    advantage. This is a user-proposed thought experiment.
51. **The code-breaker example isolates performance rather than efficiency.**
    Brute force may require vastly more trials than direct use of the known code.
    It wins only on the chosen metric, such as wall-clock time to opening, and
    only where the constituted domain supplies a bounded option space, cheap
    trials, a decisive verifier, and no prohibitive lockout. These conditions
    make the example a compact demonstration of the encapsulation thesis as well
    as Sutton's scaling intuition. This is analytical qualification.
52. **David treats efficiency or insufficient resources as the direct objection
    to Sutton's prescription.** Sutton's initial premise is that enough resources
    become available for general search and learning to keep scaling. Rejecting
    that premise may justify a more efficient human-informed method, but it is a
    “take it or leave it” rejection of the applicable regime rather than an
    internal refutation of the lesson. This is a user-proposed framing.
53. **Abandoning the scalable method midway risks the worst of both worlds.** A
    project may incur the training cost, opacity, and unpredictability of a
    general learner, then make continued improvement dependent on recurring
    human diagnoses and prescribed methods. It thereby loses both the relative
    simplicity of an explicit expert system and the autonomous scaling promise
    of search and learning. David confirms this as a precise description of the
    current LLM post-training position. This is a user-proposed diagnosis.
54. **The midway trap is conditional, not a verdict on every hybrid.** Human
    contributions that constitute the task, improve a general meta-method, or
    bridge a genuinely finite-resource horizon may combine advantages rather
    than disadvantages. The trap requires both incurred general-learning costs
    and continuing dependence on human task-specific method design as the
    marginal source of progress. This is dialectical qualification.
55. **David describes the current position as taking the leap of faith while
    continuing to rationalize.** The field has made the material wager on a
    resource-intensive general learner whose discoveries cannot be specified in
    advance, but withdraws the wager epistemically when human-authored
    explanations, distinctions, and preferred paths remain authoritative in
    post-training. This is a user-proposed rhetorical and conceptual
    formulation.
56. **Retrospective explanation is not the target of the rationalization
    critique.** Interpretation, auditing, and safety constraints may be necessary
    without prescribing a task-specific method. The contradiction arises when a
    human rational reconstruction selects which method receives reward or
    acceptance independently of the constituted outcome. This is dialectical
    qualification.
57. **Base-versus-post-trained comparisons refute the naive anti-post-training
    claim.** In InstructGPT's human evaluation, the 1.3B post-trained model was
    preferred to the 175B GPT-3 base model, while the matched 175B InstructGPT
    model was preferred to the 175B base model 85% of the time. The post-trained
    models also improved measured truthfulness and reduced some hallucination and
    toxicity outcomes. Current base models therefore cannot simply be assumed to
    be better assistants without human-guided post-training. This is primary
    empirical evidence.
58. **The comparison establishes objective mismatch rather than generic
    pretraining failure.** The InstructGPT paper explicitly distinguishes
    next-token prediction on internet text from helpful and safe instruction
    following. Post-training success shows that the base objective underdetermines
    the deployed assistant objective. It does not show that pretraining learned
    poor representations, nor that a proposed alternative training regime would
    already outperform the current pipeline. This is source-grounded synthesis.
59. **LIMA is the strongest counterinterpretation.** Its superficial-alignment
    hypothesis says almost all knowledge and capabilities are learned during
    pretraining while alignment selects the subdistribution of formats used with
    users. A 65B LLaMA model tuned on only 1,000 curated demonstrations performed
    competitively in the paper's preference evaluations. This supports treating
    pretraining as a strong capability substrate and post-training partly as
    elicitation or interface learning. This is peer-reviewed primary evidence.
60. **David's ultimate claim is that pretraining chose the wrong learning
    object.** The claim need not deny its capability gains. Static next-token
    prediction trains a model of inherited human text, not a persistent learner
    acting within constituted domains and improving from consequences. The need
    for post-training is therefore interpreted as an upstream design deficit,
    while the superiority of domain-grounded training remains a counterfactual
    hypothesis to be demonstrated. This is a user-proposed revision bounded by
    the evidence.
61. **“You get what you inspect” states the objective-design principle.** Token
    prediction inspection produces a capable predictor; demonstrations and
    preference inspection produce behavior conforming to those signals; domain
    consequence inspection would require the learner to discover successful
    methods. Optimization may succeed in every phase while the evaluative object
    remains wrong for persistent Sutton-like development. This is a user-proposed
    rhetorical and conceptual formulation.
62. **David's design criterion is convergence on helpfulness without human method
    instruction.** If a helpful assistant is the intended system, training should
    expose helpful consequences to an algorithm capable of discovering the
    methods that produce them. Humans may specify helpfulness, constraints, and
    valid outcomes; “on its own” applies to method discovery, not autonomous
    invention of the goal. This is a user-proposed consequence of the upstream
    claim.
63. **Open-ended helpfulness may not yet be a Sutton-ready domain.** Unlike
    checkmate, formal proof, or executable tests, helpfulness across general
    assistant use lacks one stable, independently verifiable consequence. If it
    cannot be constituted and observed well enough for convergence,
    demonstrations and preferences may improve the product while compensating
    for the missing learning environment. They do not by themselves establish
    autonomous discovery of helpfulness. This is dialectical synthesis and an
    explicit open problem.
64. **Method-neutrality and scalability are independent tests.** David partially
    revises the earlier treatment of human outcome feedback. A person may report
    whether an attempt succeeded without teaching a method, so the report can be
    epistemically legitimate; yet a learning loop that requires a new human
    judgment for each additional attempt does not turn increasing computation
    into proportionally more evaluative experience. The boxer example therefore
    remains method-neutral while failing, by itself, as the long-run mechanism
    of the Bitter Lesson. This is a user-proposed correction derived from
    Sutton's scaling criterion.
65. **The principled boundary does not coincide with the names RLHF and RLAIF.**
    Canonical RLHF collects human comparisons, trains a preference or reward
    model to generalize them, and then uses that model to score many policy
    samples automatically. Human labor is therefore partly amortized rather than
    literally present at every reinforcement-learning step. Whether an RLHF
    system remains human-bottlenecked depends on whether new human judgments are
    repeatedly needed as the policy and task distribution change. This is a
    source-grounded technical qualification.
66. **Iterated online RLHF supplies a concrete recurring-human case.** Bai et
    al. report updating preference models and RL policies weekly with fresh
    human feedback. This shows that at least one influential RLHF design made
    continued human judgment a recurring improvement input rather than a bounded
    initial condition. It supports David's scaling concern without proving that
    every possible RLHF architecture has the same dependence. This is primary
    technical evidence.
67. **RLAIF can relocate human input to environment construction.**
    Constitutional AI uses human-written principles as its only direct oversight
    for harmfulness labels, then has models generate critiques, revisions, and
    preference labels used to train a reward model. Lee et al. similarly use an
    off-the-shelf LLM to label preferences and report performance comparable to
    RLHF on summarization, helpful dialogue, and harmless dialogue, including
    improvement with same-size or same-checkpoint labelers. This supports
    David's proposal that human feedback may seed or constitute a scalable AI-
    feedback environment. This is primary technical evidence.
68. **RLAIF solves feedback supply, not automatically feedback closure.** An
    AI evaluator can generate labels at machine scale while merely reproducing a
    constitution, prompt, or preference policy inherited from humans and
    pretraining. The learner may then discover how to satisfy an automated
    teacher rather than how to produce independently verified domain outcomes.
    RLAIF is Bitter-Lesson-compatible only if the finite human seed constitutes
    an evaluator that remains usable across new cases without recurring human
    diagnosis of every new failure. Finding 70 qualifies the earlier emphasis on
    method-neutrality: human examples may contain preferences or methods during
    bounded initialization. The decisive scaling question is whether that input
    must continue. This is bounded dialectical synthesis; the cited experiments
    do not establish evaluator closure.
69. **Human feedback's permitted role is bounded and meta-level.** On David's
    revised account, humans may define the goal, write constitutive principles,
    seed or calibrate an evaluator, and audit it outside the operative learning
    loop. Human judgment cannot remain the marginal source of task-specific
    improvement as computation increases. If evaluator failures repeatedly
    require engineers to formulate new distinctions before learning can
    continue, the human bottleneck has moved one level up rather than
    disappeared. Finding 70 further clarifies that the bounded seed may itself
    contain human methods. This is a user-proposed formulation.
70. **Finite human-made examples are affirmatively compatible with David's
    thesis.** David does not object to human examples, preferences, or method
    knowledge merely because of their origin. If a limited predefined set is
    sufficient to establish a learning system that continues improving without
    additional task-specific human intervention, he accepts the arrangement
    completely. The target of criticism is unbounded dependence on new human
    inputs, not finite human initialization. This explicitly corrects any
    stronger reading of findings 64, 68, or 69.
71. **“Infinite learning from finite data” means unbounded learning from bounded
    human data.** It cannot literally mean extracting unlimited new evidence
    from a fixed total dataset. The finite human seed must establish a
    generative and evaluative system that produces a growing body of machine-
    generated trials, observations, comparisons, and consequences. Human data
    remains bounded while total experience grows. This is the precise form of
    David's slogan and connects it to the earlier domain hypothesis.
72. **The closure test asks whether human intervention can terminate while
    learning continues.** A paradigm or domain has been sufficiently
    encapsulated for Sutton-like learning when direct human task-specific
    examples, judgments, and diagnoses can stop without stopping further valid
    improvement. If new behavioral regions repeatedly require humans to add the
    missing distinction, the system specification was not closed enough to
    support the claimed learning regime. This is a user-proposed operational
    criterion.
73. **Technical learning validity is weaker than practical Bitter-Lesson
    adequacy.** A human may supply a semantically legitimate reward after every
    action, so the reinforcement-learning system can be technically coherent.
    But if an unbounded number of such interventions is necessary, the reward
    channel cannot exploit increasing computation independently of human labor
    and will not practically satisfy Sutton's necessary scaling condition. This
    preserves the boxer example as valid feedback while denying it the status of
    a scalable architecture.
74. **RLHF and RLAIF must be classified by critical-path dependence, not by
    acronym or recurrence alone.** A reward
    model trained once from a bounded human comparison set may satisfy the
    closure test if it remains reliable under continued optimization. An RLAIF
    evaluator may fail the same test if policy expansion repeatedly exposes
    cases that require new human repairs. RLAIF is one possible means of turning
    finite human data into scalable evaluation, not the definition of success.
    This is dialectical synthesis from the existing technical evidence.
75. **LIMA becomes qualified positive evidence for finite initialization.** Its
    result that a small curated demonstration set can select useful assistant
    behavior from a capable pretrained model is compatible with David's finite-
    seed thesis. It does not demonstrate the second stage: persistent learning
    after the demonstration set is fixed. The article should therefore use LIMA
    both as a counter to claims of poor pretraining and as evidence that bounded
    human alignment data can have large leverage without becoming a continuing
    discovery process. This is source-grounded reinterpretation.
76. **Sparse feedback establishes amortization, not independence.** Sutton's
    essay locates the long-run difference in whether general search and learning
    continue to exploit increasing computation. Christiano et al. show that
    human comparisons can cover about 0.1 percent of interactions and decline in
    rate while a learned reward function amortizes them. They do not show that
    the same expanding performance frontier remains reachable when further
    feedback is frozen. Numerical sparsity therefore does not settle whether the
    human channel is an indispensable critical-path component.
77. **Canonical credit assignment is admissible under the revised criterion.**
    Sutton and Barto define value functions through expected future return and
    describe Monte Carlo control as learning values and policies by averaging
    sampled returns. AlphaZero trains state values against final outcomes and
    its policy toward MCTS distributions. These are positive cases of the
    learning system deriving semantic and causal distinctions from its own
    outcome-bearing experience.
78. **The learner/evaluator boundary is epistemic provenance.** A value model,
    critic, process verifier, or other evaluator belongs to the learner when it
    derives its task-specific distinctions from the constituted domain's formal
    structure, transitions, and outcomes. The discovery belongs to the engineers
    when human evaluators diagnose and encode the legitimate method independently
    of that evidence. Automation alone does not decide the classification.
79. **Generated experience must be non-self-certifying.** Silver and Sutton's
    experience regime emphasizes action, grounded interfaces, and
    consequence-based rewards. Gao et al. show that a learned proxy can improve
    while the underlying objective worsens. DeepSeek-R1, PlanSearch, and
    AlphaProof are stronger positive cases because tests, compilers, formal
    verification, or rule-based outcomes constrain the learner independently of
    its own endorsement. Machine-generated volume by itself does not establish
    evaluative closure.
80. **The upstream pretraining claim must be made at system level.** InstructGPT
    establishes an objective mismatch between next-token prediction and
    assistant behavior. LIMA shows that a capable pretrained substrate plus a
    small fixed alignment set can select useful assistant behavior. Together
    they leave open whether pretraining itself chose the wrong object or whether
    the complete deployed architecture failed to turn that substrate into a
    persistent assistant learner. The evidence supports the latter diagnosis
    more directly.
81. **Current disclosed post-training systems strengthen the recurrent-human
    existence case while remaining hybrids.** Llama 3 used six rounds in which
    new preference annotations and SFT data were collected, alongside reward
    modeling, rejection sampling, synthetic data, and DPO. Gemini 2.5 reports
    successive iterations with human-discovered failures, human revisions,
    amortized preference data, AI critics, automated evaluations, and automated
    red teaming. These cases show recurring human epistemic input in major
    pipelines. They do not isolate the marginal contribution of that input or
    prove a field-wide dependence.
82. **The direct reception record is broader than the initial sample.** OpenAI's
    ImageGPT work cited Sutton's essay in 2020, and Anthropic's 2025 Activation
    Oracles work explicitly calls its generalist, data-scalable approach
    Bitter-Lesson compliant. Alongside Falcon, BIG-bench, and PlanSearch, this
    establishes reception across model design, benchmarking, search, and
    interpretability. The meanings differ enough that the article must analyze
    the reception rather than count citations as agreement on one doctrine.
83. **Open-ended helpfulness raises a governance objection as well as a
    verification problem.** InstructGPT aligns to the preferences of a
    particular labeler/researcher group; Constitutional AI and Gemini encode
    institutionally authored policies and rubrics. Continued human revision may
    alter the legitimate objective rather than prescribe a method inside a
    fixed objective. The article should separate governance of changing values
    from recurring task-specific diagnosis and keep the positive closure claim
    conditional on a sufficiently stable constituted goal.
84. **Bounded constitution supports expansion beyond the seed, not literal
    infinite competence.** AlphaZero, AlphaProof, DeepSeek-R1, and PlanSearch
    establish large or continuing gains over reported horizons. They do not
    establish indefinite improvement, and the No Free Lunch result warns that
    useful generalization depends on the selected problem class. The polished
    argument should use *open-ended* or *compute-scalable over the relevant
    horizon* unless it is explicitly discussing an ideal limit.
85. **The fixed-feedback counterfactual operationalizes the scaling claim.**
    After bounded constitution, freeze further task-specific human feedback and
    increase computation and system-generated experience. If the same expanding
    performance frontier remains reachable, even at a different cost or along a
    different learning curve, the feedback is an efficiency advantage. If
    progress stalls, drifts, or requires new human distinctions, the human
    channel remains on the critical path. This is David's positive empirical
    criterion, not a result established by the surveyed systems. The alternatives
    are logically exhaustive—redundant feedback or a premature system—even when
    the available evidence cannot yet assign a particular system.
86. **The code-breaking example exposes the order-of-magnitude issue.** A human
    can know the exact code while a sufficiently fast brute-force system knows
    none of it and still wins. The current fraction of human operations is not
    decisive: a composite system scales only as far as its least scalable
    indispensable component. This is David's limiting thought experiment.
87. **Musk's spreadsheet example independently illustrates the weakest-link
    principle.** In *Moonshots* #220, Musk said a spreadsheet with even “a few
    cells” completed manually could not compete with an all-computer
    spreadsheet; after Dave Blundin proposed one cell, Musk agreed. The example
    illustrates critical-path competition and does not supply evidence about
    RLHF or post-training.
88. **Historical influence and conceptual articulation are independent
    questions.** The bounded absence of Sutton citations from five foundational
    LLM papers limits claims that his essay caused those developments or served
    as their technical cornerstone. It does not prevent the essay from clearly
    articulating a general-method paradigm visible in LLM development. This is
    David's reason for retaining Sutton as the article's focal text.
89. **The article's main criticism is immanent and conditional.** It need not
    establish that Sutton's prescription is true. It asks whether a development
    program can adopt the general-learning wager and its promise of scalable
    discovery, then restore recurring human method discovery as the critical
    path while retaining the original rationale. David considers the paradigm
    plausible and its results impressive; those judgments motivate the inquiry
    without serving as premises of the consistency test.
90. **The Harari conversation contains David's direct paradigm-and-consistency
    formulation.** David said his fascination with the Bitter Lesson arises
    precisely because he sees it as a paradigm shift. He then clarified that his
    claim about LLM design is not that it chose the wrong path, but that it is
    inconsistent. He explicitly excluded continued handcrafted-AI research from
    this criticism and used a Newtonian framework's opportunistic invocation of
    teleology as the parallel case. The resulting philosophical criterion is
    that transitions between governing explanatory or operational regimes need
    an explicit principle. This is user-authored argument provenance from
    *Yuval Noah Harari Analysis*, not an analogy inferred from the conversation's
    later source-retrieval failure.

## Source records

### Richard Sutton, “The Bitter Lesson”

- **Author / date:** Richard S. Sutton, 13 March 2019.
- **Link:** http://www.incompleteideas.net/IncIdeas/BitterLesson.html
- **Observed / last verified:** 2026-07-31 / 2026-07-31.
- **Type and authority:** Primary source; Sutton's own essay. The official page
  was retrieved directly after the browser renderer returned an error.
- **Summary:** Across chess, Go, speech, and vision, Sutton describes a recurring
  long-run victory of general methods that exploit increasing computation over
  attempts to encode human domain knowledge. He names search and learning as
  the methods that appear to scale and urges researchers to build meta-methods
  that discover useful approximations rather than agents containing our own
  discovered concepts.
- **Supports:** Qualified acceptance of Sutton's historical lesson; the need to
  distinguish learned structure from hand-authored descriptions of the world.
- **Qualifications:** Sutton says the two approaches need not conflict. His
  vision example accepts convolution and certain invariances. He criticizes
  simple built-in notions of objects, space, agents, and symmetry, but does not
  argue for a single network, single objective, or single parameter set. His
  speech-recognition example explicitly credits deep learning, more
  computation, and “learning on huge training sets”; the essay cannot support a
  categorical opposition between data accumulation and learning.
- **Does not establish:** That all architectural decomposition is anti-scaling;
  that "brute force" is the best description of search and learning; or that
  the historical pattern holds under every cost, feedback, or deployment regime.
- **Verified quotation candidate:** “The search for them should be by our
  methods, not by us.” Final paragraph.
- **Use:** Primary textual anchor; define Sutton before evaluating the reception.

### David Silver and Richard S. Sutton, “Welcome to the Era of Experience”

- **Author / date:** David Silver and Richard S. Sutton; 2025 preprint of a
  forthcoming MIT Press book chapter.
- **Link:** https://storage.googleapis.com/deepmind-media/Era-of-Experience%20/The%20Era%20of%20Experience%20Paper.pdf
- **Observed / last verified:** 2026-08-02 / 2026-08-02.
- **Type and authority:** Primary position paper by Sutton and Silver; official
  DeepMind-hosted PDF.
- **Summary:** Calls the current LLM paradigm an “era of human data”: massive
  human-produced corpora, expert examples, and human preferences. It argues
  that high-quality human data is approaching a limit and that static synthetic
  generation will also be outstripped. The proposed successor learns
  continually from agent-generated interaction, inhabits long streams,
  observes and acts through grounded interfaces, receives consequence-based
  rewards, and updates a world model. The paper identifies execution feedback,
  formal proof interaction, and RL reasoning as early transition cases.
- **Supports:** David's distinction between adding inherited data and developing
  an agent that generates and learns from consequential experience; the claim
  that a human-data ceiling is already recognized by Sutton.
- **Qualifications:** The authors say adaptation may occur through weight
  updates or in-context response to environmental feedback. They explicitly
  state that experience and human data are not exact opposites, allow humans to
  be part of the environment, and propose user-guided reward functions. The
  paper therefore does not support defining experience as human-free.
- **Does not establish:** That current methods can safely or generally learn in
  open-ended real environments; that selected metrics are adequate proxies for
  complex human goals; or that “the world” supplies unambiguous rewards without
  human framing.
- **Use:** Essential originality check and strongest primary support for the
  data-versus-experience distinction.

### Long Ouyang et al., “Training language models to follow instructions with human feedback”

- **Author / date:** Long Ouyang et al.; 2022.
- **Link:** https://arxiv.org/abs/2203.02155
- **Observed / last verified:** 2026-08-02 / 2026-08-02.
- **Type and authority:** Primary technical paper for InstructGPT.
- **Summary:** The pipeline first collected prompts and human-written examples
  of desired behavior for supervised fine-tuning. Labelers then ranked sampled
  model outputs; a reward model learned to predict those preferences; PPO
  optimized the policy against that learned reward. The labelers were trained
  and given detailed instructions. The paper explicitly says the pretraining
  objective of predicting the next token on internet text differs from helpful
  and safe instruction following.
- **Supports:** The empirical claim that a canonical RLHF system mixes
  demonstrations, instructional infrastructure, preference judgments, proxy
  modeling, and optimization rather than receiving only natural outcome signals.
  It also establishes that post-training materially improves the assistant
  objective: the 1.3B InstructGPT model was preferred to 175B GPT-3, and 175B
  InstructGPT was preferred to matched 175B GPT-3 85% ± 3% of the time on the
  paper's held-out API-prompt evaluation.
- **Qualifications:** A ranked final response can communicate approval without
  explicitly prescribing an internal reasoning method. The paper also says the
  model is aligned to the preferences of a particular group of labelers and
  researchers, not to human values in general. The primary evaluation therefore
  measures the assistant objective post-training was designed to improve; it
  does not compare against David's proposed domain-grounded alternative.
- **Does not establish:** That RLHF necessarily teaches a particular method or
  that every human preference is invalid as feedback; that pretraining learned
  poor capabilities; or that post-training would be unnecessary under any
  feasible alternative pretraining regime.
- **Use:** Primary counterexample to treating *human feedback* as one uniform
  epistemic category and primary evidence that a simple anti-post-training claim
  is empirically untenable.

### Yuntao Bai et al., “Training a Helpful and Harmless Assistant with Reinforcement Learning from Human Feedback”

- **Author / date:** Yuntao Bai et al.; 2022.
- **Link:** https://arxiv.org/abs/2204.05862
- **Observed / last verified:** 2026-08-02 / 2026-08-02.
- **Type and authority:** Primary technical paper on preference modeling and
  RLHF for helpful and harmless assistants.
- **Summary:** The system collects human comparison judgments, trains preference
  models to predict them, and optimizes policies against those learned rewards.
  The paper also explores an iterated online regime in which preference models
  and RL policies are updated weekly with fresh human feedback.
- **Supports:** Both sides of the revised distinction. A reward model amortizes
  human judgments across many automated policy evaluations, so human feedback
  need not be supplied at every RL step. The weekly refresh regime nevertheless
  shows how continuing improvement can remain dependent on recurring human
  labels.
- **Qualifications:** The paper establishes an implemented workflow and its
  empirical gains, not a theorem that human-feedback systems must or cannot
  scale. A finite human seed may generalize widely; distribution shift and reward
  model staleness determine whether further human intervention is needed.
- **Does not establish:** That every RLHF system violates Sutton's lesson; that
  human-origin signals cannot report valid consequences; or that replacing human
  labels with AI labels yields an outcome-grounded evaluator.
- **Use:** Primary evidence for separating the origin of the seed signal from
  the source of continuing marginal evaluations.

### Yuntao Bai et al., “Constitutional AI: Harmlessness from AI Feedback”

- **Author / date:** Yuntao Bai et al.; 2022.
- **Link:** https://arxiv.org/abs/2212.08073
- **Observed / last verified:** 2026-08-02 / 2026-08-02.
- **Type and authority:** Primary technical paper introducing Constitutional AI
  and reinforcement learning from AI feedback.
- **Summary:** Humans provide a list of principles rather than labels identifying
  harmful outputs. A model generates critiques and revisions in a supervised
  phase; in the RL phase, a model compares sampled responses, those AI
  preferences train a preference model, and that model supplies the reward.
- **Supports:** A concrete implementation of the role David now permits: bounded
  human input can constitute an evaluative scheme whose subsequent labels are
  generated computationally. The paper reports self-supervised preference labels
  equaling or exceeding human-feedback harmlessness performance in its tests.
- **Qualifications:** The constitution remains human-authored; the system also
  uses a helpful RLHF model and human evaluation. AI-generated volume therefore
  does not imply independence from human preferences or external validation.
- **Does not establish:** That the AI judge observes domain-native consequences,
  that its judgments remain reliable under unlimited policy optimization, or
  that it can discover and repair defects in its own evaluative principles.
- **Use:** Primary existence case for human constitution followed by scalable AI
  feedback, and for the distinction between scalable evaluation and autonomous
  outcome grounding.

### Harrison Lee et al., “RLAIF vs. RLHF: Scaling Reinforcement Learning from Human Feedback with AI Feedback”

- **Author / date:** Harrison Lee et al.; ICML 2024.
- **Link:** https://arxiv.org/abs/2309.00267
- **Observed / last verified:** 2026-08-02 / 2026-08-02.
- **Type and authority:** Peer-reviewed primary comparison of RLHF and RLAIF.
- **Summary:** The paper replaces human preference labels with labels from an
  off-the-shelf LLM, trains a reward model from those labels, and also tests a
  direct variant that uses LLM scores during RL. It reports RLAIF performance on
  par with or better than RLHF across summarization, helpful dialogue, and
  harmless dialogue; same-size and same-checkpoint labelers also improve over
  supervised-finetuning baselines. The authors estimate AI labeling at more than
  ten times lower cost than human annotation.
- **Supports:** The narrow claim that AI feedback can remove the throughput and
  cost dependence on fresh human labels while preserving task performance in the
  reported settings.
- **Qualifications:** The labeler is instruction-tuned and prompted with
  evaluative criteria; human annotators supply the ultimate paper evaluation;
  the tasks and distributions are bounded. Canonical reward models can also
  become stale as the optimized policy moves out of distribution.
- **Does not establish:** Open-ended scalable oversight, independent access to
  helpfulness, or correction of a mistaken AI evaluator without new human
  intervention.
- **Use:** Strongest direct empirical support for the scalability motivation
  behind David's proposed human-feedback-to-RLAIF transition, with clear limits.

### Zhou et al., “LIMA: Less Is More for Alignment”

- **Author / date:** Chunting Zhou et al.; NeurIPS 2023.
- **Link:** https://proceedings.neurips.cc/paper_files/paper/2023/file/ac662d74829e4407ce1d126477f4a03a-Paper-Conference.pdf
- **Observed / last verified:** 2026-08-02 / 2026-08-02.
- **Type and authority:** Peer-reviewed primary research.
- **Summary:** The paper fine-tunes a pretrained 65B LLaMA model on 1,000
  carefully curated prompt-response demonstrations without RLHF. It proposes the
  superficial-alignment hypothesis: almost all knowledge and capabilities are
  learned in pretraining, while alignment teaches which subdistribution of
  formats to use in interaction. Its human-preference evaluation found LIMA
  competitive with several much more heavily aligned systems, and 30 additional
  hand-written dialogue examples sharply improved multi-turn behavior.
- **Supports:** A strong counterinterpretation of base-versus-post-training
  differences. Pretraining may already contain most capabilities, with relatively
  small post-training acting as elicitation, formatting, or interface selection
  rather than task-specific knowledge acquisition. It also supplies qualified
  positive evidence for David's finite-seed thesis: a bounded human-made dataset
  can have substantial and durable leverage over assistant behavior.
- **Qualifications:** The experiment still uses curated human demonstrations,
  evaluates a bounded prompt set through human and GPT-4 preferences, and does
  not establish persistent action, outcome-grounded learning, or general safety.
- **Does not establish:** That every form of alignment is superficial; that
  pretraining alone yields a deployable assistant; or that static-text
  pretraining creates the developing learner David proposes. It does not test
  whether learning continues after the finite alignment set is fixed.
- **Use:** Strongest primary objection to saying post-training gains prove that
  pretraining learned the wrong capabilities; forces the article to target the
  learning object and persistence rather than the quality of the substrate.

### Rafael Rafailov et al., “Direct Preference Optimization”

- **Author / date:** Rafael Rafailov et al.; 2023.
- **Link:** https://arxiv.org/abs/2305.18290
- **Observed / last verified:** 2026-08-02 / 2026-08-02.
- **Type and authority:** Primary technical paper for DPO.
- **Summary:** DPO derives an equivalent policy objective that fits a language
  model directly to preferred and dispreferred response pairs with a simple
  classification-style loss, avoiding a separately trained reward model and
  online reinforcement-learning loop.
- **Supports:** Current alignment terminology can call static, offline
  preference fitting *learning from feedback* even when the learner is not
  acting in an environment and observing a consequence.
- **Qualifications:** The preference pairs may themselves have arisen from
  genuine assessments of outcomes. The training form does not decide the
  semantic content or validity of the judgments.
- **Does not establish:** That preference optimization is ineffective or that
  it always imports solution methods.
- **Use:** Separate the source and content of a signal from the mathematical
  machinery used to optimize it.

### Anthropic, “Constitutional AI: Harmlessness from AI Feedback”

- **Author / date:** Anthropic; 2022.
- **Link:** https://www.anthropic.com/news/constitutional-ai-harmlessness-from-ai-feedback
- **Observed / last verified:** 2026-08-02 / 2026-08-02.
- **Type and authority:** Official primary description of the method and its
  accompanying paper.
- **Summary:** Researchers provide a written constitution of principles. The
  model uses those principles to critique and revise its responses; an AI then
  compares candidate outputs to train a preference model used for reinforcement
  learning.
- **Supports:** Alignment can introduce explicit human-authored normative rules
  and procedures even when most individual comparison labels are generated by
  another model.
- **Qualifications:** A constitution may be task- or value-constituting rather
  than a domain solution in Sutton's sense. The article must argue which role a
  particular principle plays instead of dismissing all explicit rules.
- **Does not establish:** That constitutional rules determine the model's full
  reasoning process or eliminate autonomous generalization.
- **Use:** Strong test case for the boundary between constituting objectives,
  prescribing behavior, and learning from consequences.

### Hunter Lightman et al., “Let's Verify Step by Step”

- **Author / date:** Hunter Lightman et al.; 2023.
- **Link:** https://arxiv.org/abs/2305.20050
- **Observed / last verified:** 2026-08-02 / 2026-08-02.
- **Type and authority:** Primary technical paper comparing outcome and process
  supervision.
- **Summary:** The paper defines outcome supervision as feedback on a final
  result and process supervision as feedback on every intermediate reasoning
  step. It reports better results from process supervision on a subset of MATH
  and releases PRM800K, containing 800,000 human step-level labels.
- **Supports:** The alignment literature already distinguishes final evaluation
  from intervention along the solution path. Process labels are a concrete case
  in which supervision operates at finer resolution.
- **Qualifications:** A correctness label on a step evaluates that step; it does
  not necessarily demonstrate the correct replacement or reward a policy beyond
  what eventual correctness requires. Process supervision can be outcome-
  decomposing, method-shaping, or a mixture; resolution alone does not decide.
- **Does not establish:** That process supervision is inferior, anti-general,
  or incompatible with every defensible reading of Sutton.
- **Use:** Primary empirical anchor for David's teaching-method analogy and its
  necessary qualification.

### Andrew Y. Ng, Daishi Harada, and Stuart Russell, “Policy Invariance under Reward Transformations”

- **Author / date:** Andrew Y. Ng, Daishi Harada, and Stuart Russell; 1999.
- **Link:** https://people.eecs.berkeley.edu/~russell/papers/icml99-shaping.pdf
- **Observed / last verified:** 2026-08-02 / 2026-08-02.
- **Type and authority:** Primary ICML paper; author-hosted copy.
- **Summary:** The paper asks which additions to an MDP's reward function leave
  its optimal policy unchanged. It proves policy invariance for potential-based
  shaping rewards and shows that other transformations may yield a policy that
  is suboptimal under the original reward unless further assumptions hold.
- **Supports:** An intermediate reward can accelerate learning without changing
  what ultimately counts as optimal. Conversely, badly chosen process rewards
  can steer the learner away from the original task.
- **Qualifications:** The guarantee is formalized for MDP reward transformations
  under explicit assumptions. General-assistant behavior does not come with a
  fully specified MDP or readily enumerable set of optimal policies.
- **Does not establish:** That policy invariance is the only philosophically
  relevant criterion or that all human process labels violate it.
- **Use:** Technical basis for distinguishing policy-preserving shaping from
  goal-changing reward design. Under David's revised criterion, outcome-derived
  credit may rank paths; the remaining question is whether a human semantic
  process target was independently supplied.

### Zeyu Jia, Alexander Rakhlin, and Tengyang Xie, “Do We Need to Verify Step by Step?”

- **Author / date:** Zeyu Jia, Alexander Rakhlin, and Tengyang Xie; submitted
  2025, current version 2026.
- **Link:** https://arxiv.org/abs/2502.10581
- **Observed / last verified:** 2026-08-02 / 2026-08-02.
- **Type and authority:** Primary theoretical preprint.
- **Summary:** Under stated data-coverage assumptions, the paper relates
  trajectory-level outcome rewards to per-step reward learning and argues that
  outcome supervision is not statistically harder than process supervision by
  more than polynomial factors in horizon. With rollouts or a verifier, it
  proves that a policy's advantage function can serve as an optimal process
  reward model.
- **Supports:** Process rewards can be derived from outcome information rather
  than supplied externally as human method knowledge.
- **Qualifications:** The result depends on coverage, realizability, and formal
  sequential-decision assumptions; it does not make long-horizon credit
  assignment easy in practice.
- **Does not establish:** That human process labels are unnecessary in all
  current systems, that their empirical advantages are illusory, or that the
  outcome signal remains valid in open-ended domains.
- **Use:** Positive evidence that fine-grained credit can be discovered by the
  learner from outcome-bearing experience rather than supplied as human method
  knowledge.

### Amrith Setlur et al., “Rewarding Progress”

- **Author / date:** Amrith Setlur et al.; 2024.
- **Link:** https://arxiv.org/abs/2410.08146
- **Observed / last verified:** 2026-08-02 / 2026-08-02.
- **Type and authority:** Primary technical preprint.
- **Summary:** The paper defines useful process reward as step-level progress:
  the change in the probability of eventually producing a correct response. It
  trains automated process advantage verifiers and applies them to search and
  online reinforcement learning.
- **Supports:** Fine-grained process evaluation can be anchored to eventual
  correctness rather than to a human-prescribed reasoning trace.
- **Qualifications:** The approach still relies on the choice and reliability
  of the prover policy and on tasks with measurable correctness.
- **Does not establish:** That the same construction works for plural,
  open-world assistant goals.
- **Use:** Concrete positive example of learner-derived process credit anchored
  in eventual correctness; evaluate separately whether its correctness proxy is
  valid across the target domain.

### Fei Ding et al., “Internalizing Outcome Supervision into Process Supervision”

- **Author / date:** Fei Ding et al.; 2026.
- **Link:** https://arxiv.org/abs/2605.05226
- **Observed / last verified:** 2026-08-02 / 2026-08-02.
- **Type and authority:** Primary recent preprint; not treated as settled field
  consensus.
- **Summary:** Starting with outcome-only supervision, the method identifies and
  corrects failed reasoning trajectories and reuses them to create localized
  learning signals. The authors explicitly contrast this internally generated
  process supervision with externally annotated step labels.
- **Supports:** Process-level guidance may be generated by the learner's own
  search, failure analysis, and correction rather than supplied by humans.
- **Qualifications:** The reported method concerns reasoning benchmarks, and its
  claims require replication and testing beyond those settings.
- **Does not establish:** That internally generated corrections are always valid
  or independent of the verifier and task representation supplied by humans.
- **Use:** Shows that moving method judgment from human annotators into the
  learner does not eliminate the project’s objection to judging methods.

### Huining Yuan et al., “Verifiable Process Rewards for Agentic Reasoning”

- **Author / date:** Huining Yuan et al.; 2026.
- **Link:** https://arxiv.org/abs/2605.10325
- **Observed / last verified:** 2026-08-02 / 2026-08-02.
- **Type and authority:** Primary recent preprint; not treated as settled field
  consensus.
- **Summary:** The paper converts symbolic or algorithmic oracles into dense
  turn-level rewards for deduction, constraint reasoning, and probabilistic
  inference, reporting improved credit assignment and transfer over sparse
  outcome or rollout-based baselines.
- **Supports:** Intermediate actions can sometimes have objective, verifier-
  grounded outcomes of their own; process supervision need not be a disguised
  preferred method.
- **Qualifications:** The benefit depends on oracle reliability, and the authors
  identify extension to less structured open-ended domains as unresolved.
- **Does not establish:** That general assistant behavior admits reliable
  intermediate verification.
- **Use:** Existence case for higher-resolution outcome evaluation.

### OpenAI, “Deliberative alignment: reasoning enables safer language models”

- **Author / date:** OpenAI; 2024.
- **Link:** https://openai.com/index/deliberative-alignment/
- **Observed / last verified:** 2026-08-02 / 2026-08-02.
- **Type and authority:** Official primary description of an alignment method.
- **Summary:** OpenAI describes directly teaching models human-written safety
  specifications and how to reason over them before answering. The method uses
  specification-aware synthetic reasoning traces for supervised fine-tuning
  and a policy-aware reward model for reinforcement learning.
- **Supports:** A clear current example in which post-training explicitly
  supplies policies and a procedure for applying them, not merely approval of a
  completed real-world outcome.
- **Qualifications:** Safety specifications may legitimately constitute the
  objective and constraints of deployment. Calling them human-built does not by
  itself show they should be removed.
- **Does not establish:** That the trained model follows one fixed internal
  reasoning path or that specification-based alignment cannot scale.
- **Use:** Strongest case for testing whether alignment reintroduces human-built
  methods under a broad feedback vocabulary.

### Leo Gao, John Schulman, and Jacob Hilton, “Scaling Laws for Reward Model Overoptimization”

- **Author / date:** Leo Gao, John Schulman, and Jacob Hilton; 2022.
- **Link:** https://arxiv.org/abs/2210.10760
- **Observed / last verified:** 2026-08-02 / 2026-08-02.
- **Type and authority:** Primary empirical paper on optimization against learned
  reward models.
- **Summary:** The authors study an imperfect learned reward model as a proxy for
  a ground-truth reward and find that sufficient optimization can worsen
  performance under the ground-truth evaluator even while proxy reward rises.
- **Supports:** A learned thumbs-up predictor is not automatically a stable
  terminal condition like checkmate. Its relation to the intended outcome must
  be independently validated under optimization.
- **Qualifications:** The experiment uses a synthetic setup in which the
  ground-truth reward is available for evaluation; many human objectives lack
  such a clean reference measure.
- **Does not establish:** That reward models never generalize or that human
  preference is an illegitimate objective.
- **Use:** Evidence for making proxy validity part of the operational feedback
  criterion.

### Richard Sutton interview with Dwarkesh Patel

- **Author / date:** Richard S. Sutton interviewed by Dwarkesh Patel, 2025.
- **Link:** https://www.dwarkesh.com/p/richard-sutton
- **Observed / last verified:** 2026-08-02 / 2026-08-02.
- **Type and authority:** Primary interview evidence for Sutton's present view;
  the interviewer's reception claims remain commentary, not prevalence data.
- **Summary:** Patel says people have used *The Bitter Lesson* to justify LLM
  scaling. Sutton replies that LLMs use massive computation up to the limits of
  the Internet but also insert large amounts of human knowledge. He predicts
  that experience-based systems may supersede them as another instance of the
  lesson. He defines the scalable method as trying actions and observing what
  works, distinguishes next-token prediction from predicting environmental
  consequences, and argues for continual learning of a world transition model.
- **Supports:** The recursive formulation: LLM pretraining can resemble a
  Bitter Lesson success now and become the human-knowledge method displaced by
  a later experiential system. It also provides direct evidence that the
  scaling interpretation exists in prominent LLM discourse.
- **Qualifications:** Sutton calls whether LLMs count as a Bitter Lesson case a
  sociological or industry question. He allows starting from human knowledge,
  admits that researchers currently supply useful generalization, and treats
  the separate AlphaZero games as an experimental choice rather than a limit of
  the general agent idea.
- **Does not establish:** How widespread the scaling interpretation is; that a
  new architecture rather than an LLM-based agent is required; or that grounded
  experience removes human assumptions.
- **Use:** Define what can and cannot still be advanced as a criticism of
  Sutton himself.

### Bounded check of foundational LLM scaling and model papers

- **Sources / dates:** Kaplan et al., “Scaling Laws for Neural Language Models”
  (2020), arXiv:2001.08361; Brown et al., “Language Models are Few-Shot
  Learners” (2020), arXiv:2005.14165; Hoffmann et al., “Training Compute-Optimal
  Large Language Models” (2022), arXiv:2203.15556; Chowdhery et al., “PaLM”
  (2022), arXiv:2204.02311; OpenAI, “GPT-4 Technical Report” (2023),
  arXiv:2303.08774.
- **Observed / last verified:** 2026-08-02 / 2026-08-02.
- **Type and authority:** Primary technical papers; source archives were
  downloaded from arXiv and searched in full for “Bitter Lesson,” “Richard
  Sutton,” and “Sutton.”
- **Result:** No paper cited Richard Sutton or *The Bitter Lesson*. Matches for
  “Sutton” in PaLM and the GPT-4 report referred to coauthor Charles Sutton, not
  Richard Sutton.
- **Supports:** The limited claim that the essay is not an overt technical
  dependency of these canonical papers and should not be called the technical
  cornerstone of LLM development on current evidence.
- **Qualifications:** This is a purposive five-paper sample, not a bibliometric
  study. Citation absence does not rule out tacit influence, shared intellectual
  background, or later use as a research heuristic.
- **Does not establish:** The prevalence or causal influence of the essay across
  labs, internal decisions, talks, curricula, or engineering culture.
- **Use:** Calibrate the article's reception claim and motivate a later bounded
  reception history rather than abandoning the article.

### Ashish Vaswani et al., “Attention Is All You Need”

- **Publication:** NeurIPS 2017.
- **Link:** https://research.google/pubs/attention-is-all-you-need/
- **Observed / last verified:** 2026-08-02 / 2026-08-02.
- **Type and authority:** Peer-reviewed primary research; official Google
  Research record.
- **Summary:** Introduces the Transformer, replacing recurrent and convolutional
  sequence models with attention. The reported architecture was more
  parallelizable, trained faster in the tested translation setting, and
  generalized to English constituency parsing.
- **Supports:** A retrospective account in which a general, hardware-scalable
  architecture helped make subsequent language-model scaling possible.
- **Qualifications:** The paper predates Sutton's 2019 essay and does not cite
  or receive it. The Transformer is itself a consequential human-designed
  architecture rather than evidence that architectural insight became
  unnecessary.
- **Does not establish:** That Sutton's essay caused the Transformer or the LLM
  scaling program; that attention alone explains later progress; or that data
  and compute dominate architecture under every regime.
- **Use:** Historical precursor and retrospective affinity only; never direct
  reception evidence.

### Guilherme Penedo et al., “The Falcon Series of Open Language Models”

- **Publication:** Technical report, arXiv:2311.16867, 29 November 2023.
- **Link:** https://arxiv.org/abs/2311.16867
- **Observed / last verified:** 2026-08-02 / 2026-08-02.
- **Type and authority:** Primary technical report by the Falcon LLM team.
- **Summary:** Describes Falcon's models, web-heavy training data, architecture,
  scaling-law work, and hardware-aware training. The authors explicitly say
  their design was “inspired by the bitter lesson” and organized around
  scalability in performance, data, and hardware; they treat the Transformer
  as an example of hardware-scalable design.
- **Supports:** The strongest located evidence that Sutton's essay was not only
  attached to LLMs retrospectively but used explicitly as an LLM design
  rationale.
- **Qualifications:** One model family and lab do not establish a field-wide
  philosophy. The report operationalizes the lesson largely as scalable model,
  corpus, and hardware engineering rather than as continual experiential
  learning.
- **Does not establish:** That Sutton caused the broader LLM scaling program or
  that all frontier laboratories shared Falcon's explicit rationale.
- **Use:** Principal laboratory specimen for the article's reception claim.

### Xuezhi Wang et al., “Planning in Natural Language Improves LLM Search for Code Generation”

- **Publication:** ICLR 2025.
- **Link:** https://proceedings.iclr.cc/paper_files/paper/2025/file/071a637d41ea290ac4360818a8323f33-Paper-Conference.pdf
- **Observed / last verified:** 2026-08-02 / 2026-08-02.
- **Type and authority:** Peer-reviewed primary research.
- **Summary:** PlanSearch first generates diverse natural-language observations
  and plans, then implements them. The authors frame the Bitter Lesson as two
  routes for converting computation into capability—learning and search—and
  argue that LLM progress had exploited the former more successfully. On the
  paper's HumanEval+ evaluation, Claude 3.5 Sonnet rose from 41.4% pass@1 to
  77.0% pass@200, compared with 60.6% for repeated direct sampling.
- **Supports:** Direct LLM-era reception and David's positive mechanism: extra
  inference compute can improve results without acquiring new human-authored
  training examples when a bounded task and executable evaluation make search
  productive.
- **Qualifications:** The method still generates many candidate plans and
  programs, so it replaces inherited examples with test-time experience rather
  than eliminating data or compute. Code benchmarks have unusually crisp
  specifications and tests, which may be incomplete.
- **Does not establish:** Comparable gains in domains without executable
  verification, persistent learning across tasks, or low total resource use.
- **Use:** Bridge between the reception history and the encapsulation thesis.

### DeepSeek-AI, “DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning”

- **Publication:** *Nature* 645, 2025; initial technical report 2025.
- **Link:** https://www.nature.com/articles/s41586-025-09422-z
- **Observed / last verified:** 2026-08-02 / 2026-08-02.
- **Type and authority:** Peer-reviewed primary research.
- **Summary:** DeepSeek-R1-Zero applies large-scale reinforcement learning to a
  pretrained base model without supervised fine-tuning as the preliminary
  reasoning stage. The successful reward signals are concentrated in settings
  with rule-based accuracy or format checks, including mathematics, logic, and
  code, where answers, tests, or compilers can evaluate outputs.
- **Supports:** The proposition that a reliable verifier makes Sutton-like RL
  practical and lets a capable prior generate its own reasoning experience.
- **Qualifications:** The learner starts from a data-intensive pretrained base.
  The authors warn that model-based rewards can be hacked, and the narrow RL
  stage did not by itself supply the broader writing and open-domain qualities
  required of the final system; additional stages and preference data were
  used.
- **Does not establish:** Independence from inherited data, adequate rewards
  for open-ended human tasks, or that an exactly scored benchmark captures the
  purpose of a domain.
- **Use:** Evidence for both the power and the boundary of evaluative closure.

### Thomas Hubert et al., “Olympiad-level formal mathematical reasoning with reinforcement learning”

- **Publication:** Online 12 November 2025; *Nature* 651, 2026.
- **Link:** https://www.nature.com/articles/s41586-025-09833-y
- **Observed / last verified:** 2026-08-02 / 2026-08-02.
- **Type and authority:** Peer-reviewed primary research on AlphaProof.
- **Summary:** AlphaProof learns theorem proving in Lean using reinforcement
  learning, tree search, formal verification, and automatically generated
  formal problems. Roughly one million natural-language problems were
  autoformalized into about eighty million formal problems. Training improved
  performance consistently on held-out problems, and later agents required
  fewer search simulations.
- **Supports:** The closest current analogue to David's chess example: enough
  structure to generate admissible attempts and verify them enables sustained
  improvement from search and self-generated experience rather than dependence
  on a fixed corpus of human proofs.
- **Qualifications:** The system required an extensive pretrained/formalization
  stack, human-supplied seed problems, a formal language, immense generated
  data, and substantial compute. Lean verification establishes formal validity,
  not relevance to every mathematical or human purpose.
- **Does not establish:** That broad domains can be encapsulated similarly or
  that encapsulation reduces total data volume.
- **Use:** Strongest empirical existence case and strongest correction to an
  unqualified “data is irrelevant” claim.

### David H. Wolpert and William G. Macready, “No Free Lunch Theorems for Optimization”

- **Publication:** *IEEE Transactions on Evolutionary Computation* 1(1), 1997,
  DOI 10.1109/4235.585893.
- **Link:** https://ieeexplore.ieee.org/document/585893
- **Observed / last verified:** 2026-08-02 / 2026-08-02.
- **Type and authority:** Peer-reviewed theoretical primary source.
- **Summary:** Averaged uniformly over the relevant class of objective
  functions, performance advantages of one optimization algorithm are offset
  by disadvantages elsewhere. Effective optimization therefore depends on the
  problem class and assumptions under which an algorithm is evaluated.
- **Supports:** A theoretical caution against treating search as universally
  productive without specifying the problem class; narrowing or structuring a
  domain is what makes inductive advantage possible.
- **Qualifications:** The theorem's averaging assumptions are deliberately
  broad and do not describe the distribution of real human problems.
- **Does not establish:** David's particular encapsulation threshold, that
  topical decomposition is optimal, or any quantitative reduction in required
  examples.
- **Use:** Optional conceptual anchor; not empirical proof of the proposal.

### OpenAI, “Learning to reason with LLMs” and “Introducing deep research”

- **Author / date:** OpenAI, 12 September 2024 and 2 February 2025 (deep
  research page later updated).
- **Links:** https://openai.com/index/learning-to-reason-with-llms/ ;
  https://openai.com/index/introducing-deep-research/
- **Observed / last verified:** 2026-08-02 / 2026-08-02.
- **Type and authority:** Primary lab descriptions of model-training direction;
  technically incomplete product/research announcements rather than
  reproducible papers.
- **Summary:** OpenAI describes o1 as trained with large-scale reinforcement
  learning whose performance improves with more train-time RL and more
  test-time reasoning compute, under constraints different from pretraining.
  It describes deep research as trained end-to-end on multi-step browsing and
  tool-use tasks, learning to react to information, backtrack, and execute
  trajectories.
- **Supports:** Current frontier LLM development is not accurately summarized as
  merely feeding models larger static corpora; RL, interaction, execution, and
  search are already major directions.
- **Qualifications:** The announcements do not disclose enough detail to
  determine whether training constitutes persistent real-world experience in
  Silver and Sutton's stronger sense. Most deployed instances still do not
  continually update across a lifetime of interaction.
- **Use:** Prevent a historically frozen description of the “current LLM
  industry.”

### Richard Sutton, “The OaK Architecture: A Vision of SuperIntelligence from Experience”

- **Author / date:** Richard S. Sutton, NeurIPS invited talk, 3 December 2025.
- **Link:** https://nips.cc/virtual/2025/invited-talk/109601
- **Observed / last verified:** 2026-07-31 / 2026-07-31.
- **Type and authority:** Primary source; official conference abstract.
- **Summary:** Sutton proposes a model-based RL architecture in which components
  learn continually, step sizes are meta-learned, and state/time abstractions
  are created through feature construction, subtasks, options, option models,
  and planning.
- **Supports:** Sutton's mature position is compatible with substantial internal
  architecture when the relevant knowledge and abstractions are learnable and
  revisable from experience.
- **Qualifications:** This is a vision and architecture outline, not evidence
  that OaK solves the partition-selection problem better than alternatives.
- **Does not establish:** That David's classifier/optimizer decomposition is
  correct, or that any externally supplied task boundary is acceptable.
- **Use:** Prevent the article from treating architecture itself as Sutton's
  target; sharpen the fixed-versus-learned distinction.

### Shimon Whiteson, contemporaneous “Sweet Lesson” response

- **Author / date:** Shimon Whiteson, 15 March 2019 (thread preserved by Thread
  Reader).
- **Link:** https://threadreaderapp.com/thread/1106534178676506624.html
- **Observed / last verified:** 2026-07-31 / 2026-07-31.
- **Type and authority:** Contemporaneous expert response; secondary mirror of
  an original social-media thread, not a peer-reviewed paper.
- **Summary:** Whiteson argues that successful scalable methods still depend on
  retained human knowledge such as convolutions and problem assumptions. He
  says the unresolved question is what knowledge to incorporate, when, and how.
- **Supports:** The most direct prior formulation of the criterion problem at
  the heart of this article.
- **Qualifications:** The response treats some architectural components as
  human knowledge without fully separating task content, inductive bias, and
  learnable meta-method.
- **Does not establish:** Which priors improve total cost or generalization, or
  that more domain knowledge is generally better.
- **Use:** Essential reception/counterargument. The article must differentiate
  David's proposal from Whiteson's earlier “Sweet Lesson,” not unknowingly
  reproduce it.

### David Silver et al., “A General Reinforcement Learning Algorithm that Masters Chess, Shogi, and Go Through Self-Play”

- **Author / date:** David Silver et al., *Science* 362, 7 December 2018. DOI:
  10.1126/science.aar6404.
- **Link:** https://gwern.net/doc/reinforcement-learning/model/alphago/2018-silver.pdf
- **Observed / last verified:** 2026-07-31 / 2026-07-31.
- **Type and authority:** Peer-reviewed primary research.
- **Summary:** AlphaZero reused the same algorithm, hyperparameters, settings,
  and convolutional architecture across three games without game-specific
  tuning apart from stated exceptions. It encoded states and actions from each
  game's basic rules and trained separate randomly initialized instances for
  chess, shogi, and Go. At the end of each self-play game, the rules supplied a
  loss, draw, or win outcome. The network learned state-dependent value
  predictions against that terminal outcome and policy predictions against the
  differentiated visit distribution produced by MCTS.
- **Supports:** Generality can reside in a reusable learning method while
  trained models and environments remain separate. The game boundary need not
  be rediscovered inside a jointly trained policy. It also shows that a
  paradigmatic outcome-grounded learner can infer semantic differences among
  positions and moves from many completed trajectories. This is admissible
  learner-internal credit under the revised provenance criterion.
- **Qualifications:** The boundary, rules, encodings, and training runs were
  supplied by the experimenters. This is not an evaluated routing system.
- **Does not establish:** That a classifier plus specialists beats a joint
  learner, or that the game split is optimal for every objective.
- **Verified quotation candidate:** “We trained separate instances of AlphaZero
  for chess, shogi, and Go.” p. 3.
- **Use:** Corrected chess/Go example and historical bridge to Sutton.

### Jonas Pfeiffer et al., “Modular Deep Learning”

- **Author / date:** Jonas Pfeiffer, Sebastian Ruder, Ivan Vulić, Edoardo Maria
  Ponti, 2023, arXiv:2302.11529.
- **Link:** https://arxiv.org/abs/2302.11529
- **Observed / last verified:** 2026-07-31 / 2026-07-31.
- **Type and authority:** Scholarly survey/preprint; broad map rather than one
  controlled experiment.
- **Summary:** Surveys modules, routing, aggregation, and training; distinguishes
  fixed routing based on metadata from learned hard or soft routing. Motivations
  include negative interference, parameter efficiency, systematic
  generalization, planning, and transfer.
- **Supports:** Decomposition and route selection are separable design
  questions; modularity can itself be learned and can coexist with shared
  parameters.
- **Qualifications:** Modules can block positive transfer among related tasks;
  the survey emphasizes benefits and tradeoffs across heterogeneous settings.
- **Does not establish:** A universal superiority of modular over dense models,
  or a general criterion for when a supplied partition is valid.
- **Use:** Taxonomy and vocabulary for the article's central distinction.

### Pengsheng Guo, Chen-Yu Lee, and Daniel Ulbricht, “Learning to Branch for Multi-Task Learning”

- **Publication:** ICML 2020, PMLR 119:3854–3863.
- **Link:** https://proceedings.mlr.press/v119/guo20e.html
- **Observed / last verified:** 2026-07-31 / 2026-07-31.
- **Type and authority:** Peer-reviewed primary research.
- **Summary:** Shared networks can improve latency and performance, but
  over-sharing can cause negative transfer. The method learns where to share or
  branch through differentiable, end-to-end topology search and is evaluated on
  synthetic data, CelebA, and Taskonomy.
- **Supports:** The choice between unified and separate learning can itself be
  optimized; learned branching is a concrete synthesis of both poles.
- **Qualifications:** Evidence comes from a bounded set of supervised
  multi-task benchmarks and a tree-structured design space.
- **Does not establish:** That task classification is cheap, or that learned
  branching scales to arbitrary open-ended domains.
- **Use:** Primary evidence for revisable architectural decomposition.

### Louis Kirsch, Julius Kunze, and David Barber, “Modular Networks: Learning to Decompose Neural Computation”

- **Publication:** NeurIPS 2018.
- **Link:** https://proceedings.neurips.cc/paper/2018/hash/310ce61c90f3a46e340ee8257bc70e93-Abstract.html
- **Observed / last verified:** 2026-07-31 / 2026-07-31.
- **Type and authority:** Peer-reviewed primary research.
- **Summary:** Learns both a data-dependent decomposition and the modules
  end-to-end, using conditional computation to expand capacity without a
  proportional increase in resource use; modules specialize in interpretable
  contexts in the reported image and language experiments.
- **Supports:** A system can discover its own partitions while gaining some
  computational advantages of modularity.
- **Qualifications:** Superior reported baselines are task-specific; routing
  itself adds optimization and systems complexity.
- **Does not establish:** That the learned modules correspond to stable domains
  or retain advantages at current frontier scale.
- **Use:** Direct reply to the objection that architecture must freeze a human
  distinction.

### Sneha Kudugunta et al., “Beyond Distillation: Task-level Mixture-of-Experts for Efficient Inference”

- **Publication:** Findings of EMNLP 2021, DOI 10.18653/v1/2021.findings-emnlp.304.
- **Link:** https://aclanthology.org/2021.findings-emnlp.304/
- **Observed / last verified:** 2026-07-31 / 2026-07-31.
- **Type and authority:** Peer-reviewed primary research.
- **Summary:** Compares token-, sentence-, and task-level routing in multilingual
  translation. Task routing produced deployable subnetworks; on WMT it improved
  average BLEU by 1.0 over token routing across 30 language pairs and peak
  throughput by 1.9×, with a 2.6× throughput result at 200 language pairs.
- **Supports:** A cheap, known task label can be computationally useful when it
  selects a specialist subnetwork.
- **Qualifications:** Language-pair identity is supplied, and translation is a
  structured domain; performance and throughput do not measure every cost.
- **Does not establish:** That fixed task identity is sufficient for arbitrary
  routing or better than learned token routing in every setting.
- **Use:** Closest empirical analogue to David's classifier/optimizer proposal.

### William Fedus, Barret Zoph, and Noam Shazeer, “Switch Transformers”

- **Publication:** *Journal of Machine Learning Research* 23(120), 2022.
- **Link:** https://jmlr.org/papers/v23/21-0998.html
- **Observed / last verified:** 2026-07-31 / 2026-07-31.
- **Type and authority:** Peer-reviewed primary research.
- **Summary:** A learned sparse router selects different parameters by input,
  allowing parameter count to grow without proportional per-example compute.
  The reported models achieved up to 7× pretraining speed at equal resources
  and 4× over T5-XXL in stated comparisons.
- **Supports:** Conditional computation is a scalable learning method, not a
  retreat to hand-coded expert systems.
- **Qualifications:** MoE introduces communication costs, training instability,
  balancing problems, and serving complexity.
- **Does not establish:** Lower total lifecycle cost or meaningful conceptual
  specialization of experts.
- **Use:** Evidence that routing can be part of the scaling paradigm itself.

### Aidan Clark et al., “Unified Scaling Laws for Routed Language Models”

- **Publication:** 2022, arXiv:2202.01169.
- **Link:** https://arxiv.org/abs/2202.01169
- **Observed / last verified:** 2026-07-31 / 2026-07-31.
- **Type and authority:** Primary empirical/theoretical research preprint.
- **Summary:** Models routing-network performance across two partially
  independent axes—parameter count and computation—and evaluates several
  routing techniques over five orders of magnitude in size.
- **Supports:** “Scale” is not one scalar quantity; routed architectures can
  expand learned capacity separately from active computation.
- **Qualifications:** The derived laws concern tested language-model families
  and loss, not general intelligence or deployment utility.
- **Does not establish:** That routing always dominates dense scaling.
- **Use:** Evidence that routed architectures are themselves part of scalable
  ML; not a premise in a general efficiency argument.

### Scott Reed et al., “A Generalist Agent”

- **Publication:** 12 May 2022, arXiv:2205.06175.
- **Link:** https://arxiv.org/abs/2205.06175
- **Observed / last verified:** 2026-07-31 / 2026-07-31.
- **Type and authority:** Primary technical report.
- **Summary:** Gato uses one network and one set of weights across Atari, image
  captioning, dialogue, and robotic control, using context and tokenization to
  determine the appropriate outputs.
- **Supports:** Heterogeneous tasks can coexist in one trained network; shared
  learning may exploit positive transfer and common representations.
- **Qualifications:** Tasks still have designed tokenizations, datasets, action
  formats, and contextual cues. The report does not demonstrate optimal
  efficiency against an equivalently resourced modular system.
- **Does not establish:** That one model should absorb all regimes, or that
  learned context selection eliminates architectural conditions.
- **Use:** Strong counterexample to any categorical separate-learners thesis.

### Kuang-Huei Lee et al., “Multi-Game Decision Transformers”

- **Publication:** NeurIPS 2022.
- **Link:** https://proceedings.neurips.cc/paper_files/paper/2022/hash/b2cac94f82928a85055987d9fd44753f-Abstract-Conference.html
- **Observed / last verified:** 2026-07-31 / 2026-07-31.
- **Type and authority:** Peer-reviewed primary research.
- **Summary:** One offline-trained transformer with one set of weights played up
  to 46 Atari games simultaneously at close-to-human aggregate performance and
  adapted to new games through fine-tuning.
- **Supports:** A unified game learner can work and scale; David's chess/Go
  example must remain illustrative rather than presumptive.
- **Qualifications:** Atari games share interfaces and data normalization, and
  close-to-human aggregate performance is not a direct comparison with a
  routed ensemble under equal total resources.
- **Does not establish:** That full sharing is universally best or that explicit
  routing cannot improve cost or reduce interference.
- **Use:** Strongest empirical objection to the example's intuitive force.

### BIG-bench collaboration, “Beyond the Imitation Game”

- **Publication:** BIG-bench collaboration, 2022 preprint / later TMLR article,
  arXiv:2206.04615.
- **Link:** https://arxiv.org/abs/2206.04615
- **Observed / last verified:** 2026-07-31 / 2026-07-31.
- **Type and authority:** Large scholarly benchmark project.
- **Summary:** Evaluates dense and sparse language models across a broad task
  collection and explicitly cites Sutton when motivating the avoidance of
  research effort on problems likely to be solved “by scale alone.” Aggregate
  results improve with scale while absolute performance remains poor on many
  tasks.
- **Supports:** A traceable scholarly extension of Sutton from historical
  diagnosis to research-allocation advice.
- **Qualifications:** The paper also documents limits, unpredictability, and
  metric-sensitive apparent emergence.
- **Does not establish:** Which problems scale will solve, or that architecture
  and decomposition should be avoided.
- **Use:** Concrete scholarly reception; quote only with the surrounding limits.

### Mojtaba Yousefi and Jack Collins, “Learning the Bitter Lesson: Empirical Evidence from 20 Years of CVPR Proceedings”

- **Publication:** NLP4Science workshop at EMNLP, 16 November 2024, pp. 175–187.
- **Link:** https://aclanthology.org/2024.nlp4science-1.15.pdf
- **Observed / last verified:** 2026-07-31 / 2026-07-31.
- **Type and authority:** Peer-reviewed workshop paper about reception/trends.
- **Summary:** Three LLMs score random samples of 200 CVPR titles and abstracts
  per year (2005–2024) on five author-defined dimensions. The reported scores
  trend upward for learning-over-engineering and scalability and often correlate
  with citations.
- **Supports:** Sutton's vocabulary has been operationalized as generality,
  learning, and scalable computation, and used to narrate computer vision's
  history.
- **Qualifications:** No human-expert ground truth; only titles/abstracts; one
  venue; dimensions are prompt-defined and correlated; citation regressions do
  not show causation. The authors acknowledge these limitations.
- **Does not establish:** A field consensus, a monolithic interpretation, or the
  causal superiority of “alignment” with the lesson.
- **Use:** Evidence about an academic reception, primarily as an object of
  methodological analysis rather than decisive validation.

### Dulhan Jayalath et al., “The Brain's Bitter Lesson”

- **Publication:** 2024 preprint, arXiv:2406.04328.
- **Link:** https://arxiv.org/abs/2406.04328
- **Observed / last verified:** 2026-07-31 / 2026-07-31.
- **Type and authority:** Primary research preprint.
- **Summary:** Uses neuroscience-informed self-supervised objectives and a
  purpose-designed architecture to exploit nearly 400 hours of heterogeneous
  MEG data from 900 subjects, reporting 15–27% improvements over prior models.
- **Supports:** Researchers can invoke the Bitter Lesson while still designing
  domain-informed objectives, conditioning, and architecture.
- **Qualifications:** Results concern a specialized neuroimaging task and the
  paper's own baselines; the title's rhetorical use is not a general theory.
- **Does not establish:** That domain knowledge is unnecessary or that scale
  alone caused the gains.
- **Use:** Counterexample to equating reception of Sutton with rejection of
  architecture.

### Arsam Aryandoust and Paul Pu Liang, “From Bitter to Better Lessons in AI: Embracing Human Expertise as Data”

- **Publication:** Submitted to NeurIPS 2025 Position Paper Track, 22 May 2025;
  modified 29 October 2025.
- **Link:** https://openreview.net/forum?id=LAXgS0xzPf
- **Observed / last verified:** 2026-07-31 / 2026-07-31.
- **Type and authority:** Unaccepted position-paper submission; related
  argument, not settled evidence.
- **Summary:** Proposes treating human expertise expressed in language,
  mathematics, and software as data. It surveys settings where expert knowledge
  narrows hypothesis spaces and reports an automated analysis of expert
  integration in NeurIPS papers.
- **Supports:** There is already a named “better lessons” literature; David's
  novelty must be located in reducing conditions of successful learning and in
  classification/optimization, not in the generic rehabilitation of expertise.
- **Qualifications:** Position paper; its empirical trend analysis and its
  conceptual equation of expertise with data require separate scrutiny.
- **Does not establish:** That expertise-as-data avoids the same scalability or
  rigidity problems Sutton identifies.
- **Use:** Essential novelty check and foil.

### Jared Kaplan et al., “Scaling Laws for Neural Language Models”

- **Publication:** 2020, arXiv:2001.08361.
- **Link:** https://arxiv.org/abs/2001.08361
- **Observed / last verified:** 2026-07-31 / 2026-07-31.
- **Type and authority:** Primary empirical research preprint.
- **Summary:** Reports power-law relationships between language-model loss and
  parameters, data, and training compute over multiple orders of magnitude, with
  diminishing returns and compute-optimal allocation questions.
- **Supports:** Scaling benefits can be smooth and predictable without implying
  linear efficiency; marginal improvements can require rapidly increasing
  resources.
- **Qualifications:** Findings concern transformer cross-entropy in the tested
  regime and have since been revised in compute-allocation details.
- **Does not establish:** Exponential resource consumption for AI generally or
  that architecture has negligible effects outside the tested range.
- **Use:** Retained background only; excluded from the planned article after
  the 2 August scope decision.

### Google DeepMind, “An Empirical Analysis of Compute-Optimal Large Language Model Training”

- **Publication:** 2022 research summary of Hoffmann et al., *Training
  Compute-Optimal Large Language Models*.
- **Link:** https://deepmind.google/blog/an-empirical-analysis-of-compute-optimal-large-language-model-training/
- **Observed / last verified:** 2026-07-31 / 2026-07-31.
- **Type and authority:** Primary lab summary tied to the Chinchilla experiments.
- **Summary:** At Gopher's training-compute budget, a model four times smaller
  trained on four times more data was preferable; the 70B Chinchilla model
  outperformed the 280B Gopher on nearly every reported task at equal training
  compute.
- **Supports:** Even within scaling, allocation and architecture/training choices
  materially affect efficiency and downstream inference cost.
- **Qualifications:** It does not compare the full modularity question and uses
  a specific benchmark set and compute budget.
- **Does not establish:** That smaller models are always better or that scaling
  is exhausted.
- **Use:** Retained background only; excluded from the planned article after
  the 2 August scope decision.

### Alexandra Sasha Luccioni, Yacine Jernite, and Emma Strubell, “Power Hungry Processing”

- **Publication:** ACM FAccT 2024; arXiv:2311.16863; DOI
  10.1145/3630106.3658542.
- **Link:** https://arxiv.org/abs/2311.16863
- **Observed / last verified:** 2026-07-31 / 2026-07-31.
- **Type and authority:** Peer-reviewed primary measurement study.
- **Summary:** Measures energy and carbon for 1,000 inferences across tested
  task-specific and multipurpose models. Multipurpose generative models were
  several orders of magnitude more energy-intensive for some classification
  and extractive-QA comparisons; gaps were smaller for summarization. Model
  family, size, output length, and task type all mattered.
- **Supports:** Routing cheap, well-defined tasks to adequate specialists can
  reduce deployment energy; universal models have opportunity costs.
- **Qualifications:** Tested models are not a complete frontier sample, task
  quality varies, and embodied/generalist utility is not captured by per-task
  inference measurements.
- **Does not establish:** That specialists always dominate at matched quality or
  total lifecycle cost.
- **Use:** Retained background only; excluded from the planned article after
  the 2 August scope decision.

### Stanford HAI, *2026 AI Index Report: Research and Development*

- **Organization / date:** Stanford Institute for Human-Centered AI, 2026.
- **Link:** https://hai.stanford.edu/ai-index/2026-ai-index-report/research-and-development
- **Observed / last verified:** 2026-07-31 / 2026-07-31.
- **Type and authority:** Current institutional synthesis based partly on
  estimates; transparency is itself reported as declining.
- **Summary:** Reports that global AI compute capacity grew about 3.3× per year
  since 2022 and that estimated training compute continued to rise even as
  frontier laboratories disclosed fewer details.
- **Supports:** Rapid aggregate expansion of AI compute infrastructure.
- **Qualifications:** Capacity is not actual utilization, model efficiency, or
  a causal measure of the Bitter Lesson; many frontier figures are estimates.
- **Does not establish:** A law of exponential resource demand or that scaling
  is economically or environmentally inefficient on net.
- **Use:** Retained background only; excluded from the planned article after
  the 2 August scope decision.

### International Energy Agency, *Key Questions on Energy and AI*

- **Organization / date:** IEA, 16 April 2026.
- **Link:** https://www.iea.org/reports/key-questions-on-energy-and-ai/executive-summary
- **Observed / last verified:** 2026-07-31 / 2026-07-31.
- **Type and authority:** Current official energy-system analysis and forecast.
- **Summary:** The IEA estimates per-task AI energy use has fallen by at least an
  order of magnitude annually in recent years, while AI-focused data-centre
  electricity consumption rose 50% in 2025. Its central projection roughly
  doubles total data-centre electricity use from 485 TWh in 2025 to 950 TWh in
  2030 and triples the AI-focused portion, driven by uptake and more intensive
  uses alongside efficiency gains.
- **Supports:** Per-task efficiency and aggregate demand move in opposite
  directions; deployment scale and task mix must be separated from algorithmic
  efficiency.
- **Qualifications:** Forecasts are uncertain and cover data centres, not only
  AI models; data disclosure remains incomplete.
- **Does not establish:** That AI energy demand grows exponentially without
  bound or that modular routing alone changes aggregate demand.
- **Use:** Retained background only; excluded from the planned article after
  the 2 August scope decision.

### Richard S. Sutton and Andrew G. Barto, *Reinforcement Learning: An Introduction*

- **Publication:** Second edition, MIT Press, 2018.
- **Links:** https://mitpress.mit.edu/9780262039246/reinforcement-learning/ ;
  https://incompleteideas.net/book/RLbook2020.pdf
- **Observed / last verified:** 2026-08-02 / 2026-08-02.
- **Type and authority:** Canonical primary textbook by the principal author of
  the Bitter Lesson and a cofounder of reinforcement learning; official
  publisher record and author-hosted text.
- **Summary:** The book defines state and action values by expected future
  return under a policy. Its Monte Carlo methods learn value functions and
  optimal policies by averaging complete returns across sampled episodes, and
  its temporal-difference methods learn from partial returns and bootstrapping.
  State- and action-dependent credit is therefore inferred from regularities
  across experience rather than supplied by an external teacher.
- **Supports:** Semantic credit assignment from outcomes is internal to standard
  reinforcement learning and cannot be attributed to an external teacher merely
  because it distinguishes actions or states.
- **Qualifications:** The textbook does not address David's proposed moral or
  epistemic analogy, and standard RL can still use a misspecified or human-
  authored reward. It establishes what Suttonian learning does, not that every
  process reward is legitimate.
- **Does not establish:** That learned credit is always correct, robust to
  distribution shift, or suitable for open-ended assistant objectives.
- **Use:** Canonical support for the revised distinction between learner-derived
  credit and externally supplied process targets.

### Paul F. Christiano et al., “Deep Reinforcement Learning from Human Preferences”

- **Publication:** NeurIPS 2017; arXiv:1706.03741.
- **Links:** https://papers.nips.cc/paper/7017-deep-reinforcement-learning ;
  https://arxiv.org/abs/1706.03741
- **Observed / last verified:** 2026-08-02 / 2026-08-02.
- **Type and authority:** Peer-reviewed primary research introducing a scalable
  preference-learning approach for deep reinforcement learning.
- **Summary:** Human raters compared short trajectory segments while a reward
  predictor and policy were trained asynchronously. The reported feedback
  covered about 0.1 percent of agent interactions and ranged from minutes to
  several hours of human time. The labeling schedule decreased as the number of
  experienced frames grew. The authors also report that collecting feedback
  online improved performance and reduced exploitation of reward-model
  weaknesses.
- **Supports:** Human feedback can remain recurrent, sparse, and amortized
  rather than growing in direct proportion to machine experience. Online human
  correction may serve proxy validity rather than simply teach a task method.
- **Qualifications:** The human label count still grows, the experiments are
  bounded, and no fixed-feedback ablation establishes that the same expanding
  performance frontier remains reachable without new labels. Sparsity and a
  declining labeling rate do not establish causal non-rate-limitation.
- **Does not establish:** That all recurrent supervision satisfies Sutton, that
  human comparisons are outcome-grounded, or that reward predictors remain
  reliable under open-ended policy improvement.
- **Use:** Strongest primary test case for the fixed-feedback counterfactual. It
  establishes amortization while leaving critical-path dependence unresolved.

### Elon Musk in *Moonshots* #220

- **Speaker / dates:** Elon Musk in conversation with Peter Diamandis and Dave
  Blundin; recorded 22 December 2025; published 6 January 2026.
- **Links:** Official episode: https://www.youtube.com/watch?v=RSNuB9pj9P8 ;
  official episode page:
  https://www.diamandis.com/podcast/elon-musk-agi-timeline-copy-code ;
  transcript:
  https://singjupost.com/moonshots-220-w-elon-musk-on-agi-abundance-and-the-future-of-humanity-transcript/
- **Observed / last verified:** 2026-08-04 / 2026-08-04.
- **Type and authority:** Primary recorded interview; non-academic illustrative
  source. The transcript was checked against the official recording at about
  1:05:21.
- **Summary:** Musk argues that a computerized spreadsheet with even “a few
  cells” completed manually could not compete with an all-computer spreadsheet.
  Blundin sharpens the example to one cell and Musk agrees, applying the analogy
  to fully AI-run companies.
- **Supports:** An independent illustration of the critical-path claim that a
  numerically tiny human component can determine competitive scaling.
- **Qualifications:** The statement is an analogy and prediction, not an
  experiment or an analysis of machine-learning feedback loops. The verified
  wording is “a few cells” and “one cell,” not a five-percent threshold.
- **Does not establish:** That RLHF is rate-limiting, that a particular company
  is fully automated, or that the fixed-feedback counterfactual has been passed
  by any post-training system.
- **Use:** Illustrative support for the weakest-link explanation alongside the
  code-breaking thought experiment; never use as technical evidence for RLHF.

### Collin Burns et al., “Weak-to-Strong Generalization”

- **Publication:** 2023; OpenAI research paper and official research page.
- **Links:** https://openai.com/index/weak-to-strong-generalization/ ;
  https://cdn.openai.com/papers/weak-to-strong-generalization.pdf
- **Observed / last verified:** 2026-08-02 / 2026-08-02.
- **Type and authority:** Primary lab research on scalable oversight.
- **Summary:** The authors use weaker models to supervise stronger pretrained
  models and report partial recovery of strong-model capabilities on several
  NLP tasks, including correct generalization on cases where the weak
  supervisor fails. The official account also states that the approach did not
  work on ChatGPT preference data and retains important disanalogies from human
  oversight of superhuman systems.
- **Supports:** A bounded or weaker supervisor need not cap every behavior at
  its own performance level; generalization can carry a learner beyond the
  literal labels it receives.
- **Qualifications:** The result is partial, task-dependent, and not a
  persistent experience-learning system.
- **Does not establish:** Evaluative closure, autonomous helpfulness, or that
  weak human preferences can supervise open-ended assistants.
- **Use:** Secondary counterexample to simple supervisor-capability and
  one-label-per-improvement assumptions.

### Llama Team, “The Llama 3 Herd of Models”

- **Publication:** Technical report, arXiv:2407.21783, 2024.
- **Link:** https://arxiv.org/abs/2407.21783
- **Observed / last verified:** 2026-08-02 / 2026-08-02.
- **Type and authority:** Primary technical report from Meta's Llama team.
- **Summary:** The paper separates massive next-token pretraining from
  post-training for instruction following, human preferences, capabilities,
  and safety. The reported post-training used SFT, rejection sampling, reward
  modeling, and DPO across six rounds. Each cycle collected new human preference
  annotations and SFT data while also sampling synthetic data from the latest
  models. Annotators compared responses, edited preferred responses, and were
  given progressively harder prompts as the model improved.
- **Supports:** A major disclosed LLM pipeline in which recurring human
  diagnosis, preference, and response editing remained part of iterative
  improvement, while computational generation and reward modeling amortized
  those inputs.
- **Qualifications:** The report does not provide an ablation that isolates the
  marginal gain from each human or automated component, and six rounds do not
  establish an indefinitely recurrent requirement.
- **Does not establish:** That all frontier labs use the same workflow or that
  Llama 3 could not continue improving with human inputs fixed.
- **Use:** Representative system-level case for the field audit, not evidence of
  field-wide consensus.

### Google DeepMind et al., “Gemini 2.5” technical report

- **Publication:** *Gemini 2.5: Pushing the Frontier with Advanced Reasoning,
  Multimodality, Long Context, and Next Generation Agentic Capabilities*, 2025.
- **Link:** https://storage.googleapis.com/deepmind-media/gemini/gemini_v2_5_report.pdf
- **Observed / last verified:** 2026-08-02 / 2026-08-02.
- **Type and authority:** Primary technical report from the model developer.
- **Summary:** The safety and helpfulness pipeline constructs metrics from
  human-authored policies, uses human/model interactions to find failures,
  revises responses through synthetic recipes and human intervention, and
  repeats the process across model iterations. Reinforcement Learning from
  Human and Critic Feedback combines a data reward model that amortizes human
  preferences with a prompted critic applying predefined rubrics. Automated
  red teaming generates thousands of examples while human experts and policy
  work continue to update seeds, rubrics, and judgments.
- **Supports:** A current hybrid in which AI feedback scales evaluation volume
  while recurring human epistemic and governance inputs remain visible. It also
  supplies an explicit distinction between amortized human preference data and
  AI critics.
- **Qualifications:** The human revisions include both task-method correction
  and legitimate policy governance; the report does not causally decompose
  their contributions to model gains.
- **Does not establish:** That recurring human input is the rate-limiting factor
  or that the evaluator could not operate over new behavior with its human
  inputs fixed.
- **Use:** Current primary case for testing the closure, locus, and governance
  distinctions.

### OpenAI, “Image GPT”

- **Publication:** Official research page and ICML paper, 17 June 2020.
- **Link:** https://openai.com/index/image-gpt/
- **Observed / last verified:** 2026-08-02 / 2026-08-02.
- **Type and authority:** Primary lab research record.
- **Summary:** The work applies a largely domain-agnostic autoregressive
  Transformer to pixel sequences and evaluates the learned representations for
  image classification. Its reference list cites Sutton's 2019 essay.
- **Supports:** Direct evidence that the Bitter Lesson entered OpenAI research
  discourse early in the scaling era, beyond later retrospective commentary.
- **Qualifications:** A citation establishes reception, not that Sutton caused
  the method or that every author adopted one interpretation of the essay.
- **Does not establish:** Field-wide influence, a post-training philosophy, or
  an experiential-learning reading of the lesson.
- **Use:** Add to the bounded reception history.

### Adam Karvonen and James Chua, “Activation Oracles”

- **Publication:** “Activation Oracles: Training and Evaluating LLMs as
  General-Purpose Activation Explainers,” Anthropic Alignment Science, 19
  December 2025.
- **Link:** https://alignment.anthropic.com/2025/activation-oracles/
- **Observed / last verified:** 2026-08-02 / 2026-08-02.
- **Type and authority:** Primary current research description from Anthropic.
- **Summary:** The authors train models to answer arbitrary natural-language
  questions about model activations. They explicitly call the method
  Bitter-Lesson compliant because performance scales with data quantity and
  diversity and the generalist interface can replace task-specific probes.
- **Supports:** Direct contemporary reception in interpretability and a clear
  example of *Bitter-Lesson compliant* meaning generality plus scalable data
  rather than continual consequence-grounded experience.
- **Qualifications:** This is one research project and one stated
  interpretation. The work also retains a researcher-supplied query and
  activation interface.
- **Does not establish:** Consensus at Anthropic or across interpretability,
  nor Sutton's endorsement of the classification.
- **Use:** Demonstrate that the reception is real but semantically plural.

## Reception samples not admitted as field-level evidence

- A 24 November 2023 [X exchange by Sutton](https://twitter.com/RichardSSutton/status/1728129341287198885),
  preserved with context in a [contemporaneous Reddit
  thread](https://www.reddit.com/r/singularity/comments/18302yc/richard_sutton_argues_against_data_is_all_you/),
  contains the explicit question whether his agreement with Yann LeCun's call
  for more data-efficient architectures “run[s] counter to the Bitter Lesson.”
  Sutton answered that the lesson calls for the right learning algorithms and
  that massive computation does not remove the need for data efficiency. This
  is the earliest located direct specimen of the purported contradiction, not
  evidence of scholarly consensus.
- Zvi Mowshowitz's 29 September 2025 detailed reaction to the Dwarkesh
  interview, [“On Dwarkesh Patel's Podcast With Richard
  Sutton”](https://www.lesswrong.com/posts/fpcRpBKBZavumySoe/on-dwarkesh-patel-s-podcast-with-richard-sutton),
  says Sutton's LLM position seems “at least kinda” like backtracking on the
  Bitter Lesson and argues that Sutton uses *scalable* in an unfamiliar way.
  A commenter on the associated Substack page says Sutton is backtracking;
  another Reddit reaction calls it revisionist history and says he is “sort of
  recanting.” These are clear named or attributable reception specimens but not
  peer-reviewed analyses.
- Abhishek Gautam's 24 February 2026 essay, [“Richard Sutton Says LLMs Are a
  Dead End. He Might Be
  Right”](https://abhs.in/blog/richard-sutton-llms-dead-end-bitter-lesson-explained),
  presents the strongest version of the apparent inconsistency: perhaps Sutton
  is making the same mistake as earlier critics who said the reigning scalable
  method lacked a necessary structure. The author treats this as a live
  objection rather than concluding that Sutton contradicted himself.
- Atharva Raykar's 14 October 2025 engineering essay, [“Artisanal shims for the
  bitter lesson age”](https://blog.nilenso.com/blog/2025/10/14/bitter-lesson-applied-ai/),
  extends Sutton to application design: prescriptive workflows and prompt
  scaffolds should be removable as goal-directed models improve. It is a clear
  instance of the strong reception, not evidence of consensus.
- Georg Heiler's 14 April 2026 essay, [“The Bitter Lesson Stops at the Lab
  Door”](https://georgheiler.com/2026/04/14/the-bitter-lesson-stops-at-the-lab-door/),
  offers an engineering counter-reception: deterministic interfaces, review,
  and constraints remain load-bearing around learned components. It is useful
  as a deployment foil, not empirical research.

The bounded search located no peer-reviewed paper making a sustained case that
Sutton's 2025 position logically contradicts his 2019 essay. The explicit
recantation claim currently belongs to social-media and essay reception.
- Recent pages that merely repeat Sutton, use “bitter lesson” for an unrelated
  result, rely on generated summaries, or make unsupported claims about field
  consensus were screened out.

## Research-driven constraints for the eventual manuscript

- Attribute “one monolithic learner” only to named interpreters who actually
  make that extension; do not put it in Sutton's mouth.
- Present Whiteson's 2019 response and Aryandoust/Liang's 2025 position paper so
  the article's novelty is explicit.
- State the chess/Go example historically: AlphaZero reused a general method but
  trained separate instances; David's reliable game indicator is a proposed
  extension.
- Treat learned routing, shared trunks with branches, and conditional experts as
  serious synthesis candidates, not merely evidence for preassigned modules.
- Preserve unified models as counterevidence and formulate criteria that could
  recommend sharing as well as separation.
- Keep resource and global-economics material out of the planned manuscript.
  The records remain here only as a transparent trail of a researched and then
  retired affirmative argument. Resource sufficiency may appear narrowly as
  Sutton's boundary premise and as the finite-horizon reason to decline his
  regime; do not turn that clarification into a claim about aggregate costs.
- Do not use *feedback* as a catch-all for demonstrations, preference rankings,
  process labels, constitutions, specifications, learned reward proxies, and
  environmental outcomes. Name the role of each intervention.
- Do not make iteration the decisive boundary. Repeated terminal outcomes can
  support trial-and-error learning without specifying a method; use both the
  origin/timing and information content of the signal.
- Treat derivation from outcomes as evidence that credit assignment belongs to
  the learner, provided the signal is grounded in the constituted domain and no
  human semantic process target has been inserted independently of it. Policy
  invariance and proxy validity remain separate tests.
- Treat retroactivity as an evidential constraint, not merely a timestamp: a
  process score assigned after completion is still instructional if it imports
  an independent preference about the route.
- Preserve epistemic provenance. Permit cross-trajectory comparison,
  aggregation, value learning, and semantic causal credit when the learning
  system derives them from the constituted domain's formal structure,
  transitions, and outcomes. Exclude human semantic rankings that stipulate the
  legitimate route independently of that evidence.
- Permit direct intermediate evaluation when the step is itself an independently
  completed, domain-verifiable subproblem; treat learned usefulness within a
  larger method as admissible learner-derived credit.
- Prefer *outcome-grounded* to *natural* feedback. Include outcome-trained
  process models only when their distinctions arise from the learning system's
  evidence rather than a separately supplied human method preference.
- For each intervention, identify the locus of task-specific epistemic work:
  who recognizes the relevant failure pattern, formulates the correction, and
  selects it by evidence? Test whether improvement continues when outcome
  evidence remains available but human method diagnosis stops.
- Use *learning system* rather than *model* when memory, search, tools,
  optimization, or a persistent agentic application participate in adaptation.
  Do not mistake the absence of online weight updates for the absence of system
  learning.
- Describe search spaces as generatively specified rather than necessarily
  enumerated in advance. Search contributes evidence about explored candidates;
  it does not require that every possible candidate already exist as stored
  data.
- Distinguish constitutive rules from revisable operative rules and heuristics.
  For a learned change, identify separately who generated the candidate, what
  evidence warranted it, and what mechanism retained it. Do not require verbal
  explanation when empirical domain-grounded validation is sufficient.
- Do not elevate a human-proposed, system-validated candidate into a coequal
  hybrid method. Preserve it as an attribution edge case. Explain Sutton's
  *outrun* and *outperform* language through the asymmetry between bounded human
  method discovery and automated methods that continue converting growing
  computation into generated and tested possibilities, not through an
  unsupported numerical limit.
- Treat unusually large leverage from a human meta-method as presumptive evidence
  that the relevant dimension of algorithmic potential was not yet being tapped,
  not as evidence that human proposal scales. Still distinguish an intervention
  that unlocks possibilities within the learner's existing grammar from one that
  constructs a materially new learner.
- Use the brute-force code-breaker only as a limiting thought experiment about
  time-to-success. State its domain assumptions: a finite candidate space,
  reliable immediate verification, sufficiently cheap and rapid trials, and no
  prohibitive attempt limit. Do not redescribe its rate advantage as operation
  or sample efficiency.
- State the “worst of both worlds” claim conditionally. Establish that the system
  has already incurred the costs of general learning and that recurring human
  task-specific prescriptions remain the marginal source of improvement. Do not
  apply it to task constitution, outcome feedback, general meta-method design,
  or a deliberately finite-resource expert system without further argument.
- When using *rationalize*, distinguish explanation after outcome-grounded
  selection from a human rational reconstruction that becomes authoritative for
  method selection. The former may support interpretation or auditing; the
  latter is the midway retreat the article criticizes.
- Do not infer from post-training gains that pretraining learned poor
  capabilities. State the narrower upstream claim: next-token prediction and
  assistant helpfulness are different learning objects. Treat LIMA's
  superficial-alignment hypothesis as the strongest counterview, and acknowledge
  that superiority of domain-grounded initial or continued training remains a
  counterfactual to be demonstrated.
- Formulate “converges on helpfulness on its own” as autonomous method discovery,
  not autonomous value creation. Humans may constitute helpfulness, constraints,
  and outcome criteria. If general helpfulness cannot be made sufficiently
  observable and verifiable, name the absence of a Sutton-ready domain rather
  than redescribing human demonstrations as experience.
- Distinguish finite human initialization from recurring human dependence. A
  fixed set of human-made examples may include preferences, solutions, and even
  methods without violating the Bitter Lesson merely because of its content.
  Use “infinite learning from finite data” only as the ideal limit of open-ended
  learning from bounded human-supplied data; the inspected systems establish
  expansion beyond the seed over finite horizons, while the total stock of
  machine-generated experience may continue growing.
- Apply the closure test: can direct task-specific human intervention terminate
  while valid learning continues? The boxer illustration supplies technically
  valid, method-neutral feedback but fails as a scalable architecture when
  every bout requires another human verdict. Recurring human audit may remain
  external governance, but learning must not depend on it for each new
  task-specific distinction. Sparse recurrent input creates no third category:
  the fixed-feedback test shows either that it is redundant to the expanding
  frontier or that the system is premature and remains human-dependent.
- Do not classify the architecture by the labels *RLHF* or *RLAIF*. A fixed
  reward model learned from finite human comparisons may qualify; an AI
  evaluator requiring endless human repair may not. Test stability under new
  policy behavior, reward exploitation, and whether the human input remains
  bounded.
- Treat paradigm identification and paradigm shift as explicit scope limits.
  David's hypothesis starts with a paradigm already identified by humans.
- Require generated experience to receive its relevant consequences from the
  constituted environment or an independently valid verifier. A policy and
  correlated AI judge cannot establish closure through self-confirmation alone.
- Separate recurring governance of changing or contested goals from recurring
  human diagnosis of methods inside a fixed goal. The closure claim applies
  directly only to a sufficiently stable constituted objective.
- Define the reception field as the inspected frontier-LLM research and
  engineering discourse. Use named sources to establish plural uptake, while
  reserving consensus and field-distribution claims for representative evidence.
- Treat Sutton's essay as a clear articulation of the paradigm under analysis,
  independently of whether it caused foundational LLM development. State the
  limited historical-influence finding once and do not turn reception history
  into the article's central evidentiary burden.
- Present the article's criticism as an internal consistency test. Its force
  depends on a development program adopting the general-learning wager and then
  placing recurring human method discovery on the critical path; it does not
  depend on proving Sutton's prescription ultimately correct.
- Preserve the Harari conversation as direct provenance for David's paradigm-
  shift and architectural-consistency argument. The article should express the
  principle self-sufficiently: choosing a different paradigm is coherent, while
  silently crossing between paradigms without a governing rule is not.
