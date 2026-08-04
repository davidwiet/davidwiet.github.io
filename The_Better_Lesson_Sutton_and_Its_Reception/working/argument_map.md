# Running Argument Synthesis

This file preserves the cumulative development of the argument: corrections,
qualifications, examples, objections, research-driven interpretations, and
manuscript constraints. It is intentionally expansive. The concise ordered
logic used to plan and write the article lives in `logical_map.md`.

Status: revised 4 August 2026 after David clarified why Sutton's essay is the
article's object: it articulates a development paradigm whose internal
consistency can be tested independently of its direct historical influence or
ultimate correctness. Bounded human initialization remains the positive basis
of open-ended learning.
David's proposal remains an argument to be tested; verified findings are marked
rather than silently folded into it.

## Target

The article uses post-training alignment as the immediate diagnostic site for an
ultimate claim about pretraining. Post-trained models are demonstrably better
assistants than their base models, so the article cannot advocate simply omitting
post-training. It asks why pretraining produced a substrate that requires human
demonstrations, preferences, constitutions, process labels, policies, and reward
proxies to become useful in deployment. David's proposed answer is that static
next-token pretraining learned capabilities but not a persistent learner acting
within constituted domains. The positive alternative is to organize training
within human-identified, paradigm-like domains whose rules make outcomes
intelligible and permit search, reinforcement learning, and self-generated,
verifiable experience.

The positive criterion is **unbounded learning from bounded human data**. A
finite set of human-made rules, examples, preferences, or methods is not an
objection if it constitutes a system that can thereafter generate and evaluate
new experience without recurring human task-specific intervention. The test is
whether human intervention can terminate while learning continues.

## Why Sutton, and what the article must prove

1. **Conceptual articulation:** Sutton's essay gives unusually clear expression
   to the paradigm shift David sees in system development, especially LLMs:
   general search and learning replace recurring human-authored task methods as
   the scalable source of capability.
2. **Historical modesty:** The article need not claim that Sutton caused the
   shift or that his essay was a technical cornerstone of foundational LLM
   research. The bounded source record supports direct but plural reception and
   limited evidence of causal influence.
3. **Conditional criticism:** The article need not prove Sutton correct. David
   considers the prescription plausible and its results impressive. The central
   claim is that a program cannot coherently retain the rationale and promised
   scalability of general learning while restoring recurring human method
   discovery as the critical path of improvement.
4. **Permitted continuity:** Human constitution of a domain, fixed examples,
   general meta-methods, and temporary assistance under finite resources remain
   compatible with the paradigm. The inconsistency begins when continued
   task-specific discovery remains human-authored while the program still
   presents itself as realizing scalable general learning.
5. **Explicit conceptual source in the Harari conversation:** David said, “My
   fascination with the bitter lesson is precisely for this reason - I see it as
   a paradigm shift,” and later, “My claim about LLM design is never that they
   chose the wrong path; it's that they are inconsistent.” He excluded explicit
   handcrafted-AI programs from this criticism. The surrounding Newtonian and
   teleology example establishes the general demand: an architecture may choose
   a governing framework, but a transition into another explanatory or
   operational regime requires an explicit principle rather than an ad hoc
   exception.

## Core argument

1. Sutton's 2019 lesson favors general search and learning methods that exploit
   increasing computation over systems containing human-discovered solutions.
   Static-data pretraining was a real instance of the lesson when it displaced
   hand-authored linguistic knowledge and learned powerful general
   representations. The article's stronger objection concerns its terminal
   object: prediction over inherited text is not persistent action and
   outcome-grounded development within a constituted domain.
2. Base-versus-post-trained comparisons refute the naive claim that current base
   models should simply be left untouched. InstructGPT demonstrates large gains
   on the assistant objective after human-guided post-training. The result proves
   an objective mismatch, not that pretraining learned little or that David's
   alternative would already perform better. LIMA's superficial-alignment
   hypothesis is the strongest counterview: most capabilities may already be
   learned in pretraining while a small amount of tuning selects an assistant
   format. David's ultimate claim is that even a capable substrate was not
   trained as the kind of persistent, outcome-grounded learner deployment needs.
   His compressed principle is “you get what you inspect”: token loss produces a
   predictor, human-preference inspection produces a conforming assistant, and
   domain consequences are required to produce autonomous method discovery. If
   helpful assistance is the intended object, the training algorithm should be
   capable of converging on helpfulness from observed consequences. Humans may
   constitute the goal and constraints, but the learner must discover the route.
   If open-ended helpfulness cannot yet be verified well enough for convergence,
   it is not yet a Sutton-ready domain; human teaching may remain pragmatically
   useful without becoming autonomous learning.
3. An effective search or learning process nevertheless operates over a
   constituted problem class. A domain is paradigm-like: it determines what
   entities count as relevant, which questions and actions are admissible, how
   consequences become evidence, and what distinguishes better from worse
   outcomes. These are not merely boundaries around an already given field;
   they make the field available for learning.
4. The knowledge needed to specify such a system is not equivalent to solution
   knowledge. Chess rules, legal moves, the initial state, and the win condition
   generate an enormous trajectory space without encoding good chess strategy.
5. Once a system is specified generatively and evaluatively, the stock of
   pre-existing human solutions need not govern marginal progress. Compute can
   be spent generating trajectories, searching them, evaluating outcomes, and
   updating the learner.
6. “Amount of existing data is irrelevant” must therefore mean that inherited
   examples cease to be the privileged bottleneck. It cannot mean that learning
   needs little experience: self-play, RL, and synthetic curricula may generate
   vastly more data than the available human record.
7. David's proposed contrast between evaluating an outcome and steering toward
   a desired outcome captures the problem, but purpose alone cannot define the
   boundary. Every learning signal is used to change behavior, and even checkmate
   is a predefined success criterion. The decisive question is whether a behavior
   wins selection because it improves an independently constituted task outcome,
   or whether the behavior or route is itself supplied as the target.
8. Checkmate is an outcome-grounded terminal consequence within a stable,
   constituted game. David's boxer-in-the-arena image illustrates the permitted
   iterative case: humans evaluate each bout and return the boxer for another
   attempt without coaching the method. David now qualifies the example: it
   passes the method-neutrality test but, if a person must judge every bout, it
   does not pass Sutton's scaling test. A thumbs-up is not automatically
   equivalent: it may compress truth, style, agreeableness, compliance, safety,
   and personal preference into one underdetermined signal. It becomes
   checkmate-like only when human satisfaction is itself the domain-valid
   outcome and the response does not prescribe the route; it becomes a scalable
   learning signal only when its production no longer grows through recurring
   human task-specific judgment.
9. David accepts a bounded set of predefined human-made examples without
   reservation on Bitter-Lesson grounds, even if those examples communicate
   preferences or useful methods. His positive claim is not learning forever
   from a fixed total evidence set, but unbounded learning from bounded
   **human-supplied** data. The human seed constitutes a problem and evaluative
   system; computation then produces an expanding stock of new trials,
   observations, comparisons, and consequences.
10. The decisive test is temporal: can direct human task-specific intervention
   cease while valid learning continues? If so, human examples are a fixed seed
   or prior. If every new behavioral frontier requires another human diagnosis,
   distinction, example, or judgment, the system may implement a technically
   valid learning rule but cannot practically satisfy Sutton's scaling
   condition. The names *RLHF* and *RLAIF* do not decide this. A reward model
   trained once from finite human comparisons may qualify; an AI evaluator that
   repeatedly requires new human repairs may not. RLAIF is one candidate means
   of closing the environment, not the criterion itself.
11. Process supervision is governed by epistemic provenance. The learning
   system may compare trajectories and iterations, generalize across them, and
   infer state-, action-, or step-level contribution from the constituted
   domain's formal structure, transitions, and outcomes. The learner may thereby
   distinguish reliable methods from lucky errors. The excluded case is a human
   semantic preference that authoritatively ranks the proper route independently
   of those outcome-derived distinctions. David's job-discrimination analogy
   applies to that external ranking of otherwise outcome-equivalent cases, not
   to distinctions the learner discovers from repeated evidence.
12. The same boundary can be stated as the locus of task-specific learning. If
    engineers must understand a failure, identify the defective method, and
    encode the correction before performance improves, the engineers have done
    the relevant learning. If a learning system can use outcomes to discover
    better behavior without human method diagnosis, the system has learned. The
    learner may include the model, search, memory, tools, optimizer, and a
    persistent application-level agent; it need not mean model weights alone.
13. Search operates within a possibility space already generated by the
    paradigm's constitutive rules. Its candidates need not be extensionally
    listed in advance. Its new contribution is endogenous evidence about the
    explored candidates: what happens when they are tried and how those results
    score under the domain's existing criteria.
14. Learning converts such evidence into a reusable change in policy,
    representation, operative rule, or heuristic. Change alone is not learning:
    the change must be selected and retained because evidence available within
    the constituted system warrants it, not merely because an engineer inserted
    or preferred it. The warrant may be empirical rather than explanatory.
    Human-proposed candidates that the system later validates are logically
    hybrid, but not a coequal scalable method. Automated search and learning
    *outrun* human discovery by continuing to turn growing computation into more
    generated and tested possibilities, while human proposal is a bounded,
    non-scaling channel. If a human-designed meta-method has disproportionate
    leverage, David treats that as evidence that the relevant dimension of
    algorithmic potential was not yet being exploited, not as evidence for a
    rival human discovery process. The qualification is that an intervention
    which changes what the learner can generate and test may create a new learner
    rather than unlock latent potential in the old one. Continued task-specific
    discovery must still scale without continued human proposal.
15. Existing post-training stacks are hybrids. Outcome judgments and preferences
   coexist with human demonstrations, rater instructions, constitutions,
   step-level process labels, explicit safety specifications, learned reward
   models, and optimization against those proxies. Some elements evaluate
   outcomes; others teach behavior or methods. Converting either kind into a
   scalar reward or preference loss does not erase the distinction.
16. Calling every element *feedback* creates the carte-blanche risk David
    identifies: human-authored solutions and procedures can be reintroduced
    under the vocabulary of experience. The direct criticism of Sutton is that
    his mature allowance for user-guided reward does not supply an operational
    boundary between goal-constituting feedback and solution- or method-bearing
    supervision.
17. Domain decomposition offers a constructive alternative when it is understood
   as paradigm construction rather than topical sorting. Each domain must
   constitute a sufficiently complete action and observation interface, a
   problem or experience generator, and a trustworthy verifier or reward. The
   relevant unit is a rule-governed learning system, not a subset of text.
18. Within such systems, more compute can drive search and learning without an
   endless increase in human-authored data. Code with executable tests, formal
   mathematics with Lean, and games with complete rules are current existence
   cases; writing, medicine, law, and open-world advice remain only partially
   closed because their success criteria are plural or contestable.
19. The positive conclusion is conditional and deliberately limited. Given a
    paradigm already identified by humans, domain-specific post-training may
    shift marginal progress from imported prescriptions toward generated,
    evaluable experience. The hypothesis does not explain how a model identifies,
    selects, or revises paradigms, and does not claim that every human purpose can
    be encapsulated as a reliable learning system.
20. Efficiency and insufficient resources are the cleanest way to decline
    Sutton's prescription, but they reject the regime assumed by the lesson
    rather than internally refute it. If enough computation will not be
    available within the relevant horizon, a human-informed method may be the
    rational choice. The article need not make claims about aggregate resource
    consumption or global economics to acknowledge this boundary.
21. The central danger is abandoning the method midway: paying for a general,
    opaque, compute-intensive learner and then making continued improvement
    depend on recurring human task-specific methods. Such a system can inherit
    both the learner's costs and the human-knowledge approach's bottleneck and
    plateau. This is conditional: human task constitution, general meta-methods,
    and explicit finite-resource bridges need not create the trap. David
    identifies the trapped configuration as a precise description of the
    current LLM-development position: the field has taken the material leap of
    faith in general learning while continuing to rationalize its discoveries
    through human-authored accounts of legitimate methods.

## Demonstrative example

The limiting thought experiment is brute-force code breaking. In a finite code
space with an immediate verifier and unrestricted rapid trials, a search system
that knows none of the solution can defeat a human who knows the exact code by
testing candidates faster than the human can enter or communicate it. Perfect
human knowledge supplies a fixed informational advantage; scalable search
supplies an increasing rate advantage. The example concerns time-to-success,
not operation efficiency, and fails if the constituted domain imposes lockouts,
unbounded growth, or costly verification.

The example also supplies the reply to sparse recurrent feedback. A composite
system scales only as far as its least scalable indispensable component. A
human operation can be one among billions and still govern the frontier if the
system cannot make the same continuing progress without it. Elon Musk gave a
parallel illustration in *Moonshots* #220: a spreadsheet with even “a few
cells” completed manually could not compete with an all-computer spreadsheet;
when Dave Blundin proposed one cell, Musk agreed. This is an illustration of
critical-path competition, not evidence about RLHF.

AlphaZero supplies the purest example: a compact, human-supplied system
specification replaces dependence on historical solution data and permits
self-play. AlphaProof supplies the closer LLM-era analogue: Lean provides a
formal action space and exact verification, allowing tree search, RL, and
problem-specific test-time learning. Its steady held-out improvement during
training supports David's mechanism, while its roughly 80 million generated
formal problems and enormous compute budget show why the claim concerns the
source and evaluability of experience rather than low data volume.

## Strongest objection

The strongest objection to the feedback distinction is that, for a general
assistant, human response may genuinely be part of the environment and human
satisfaction may genuinely be the objective. Silver and Sutton explicitly allow
this. The answer cannot be that human origin disqualifies a signal. David's
revision instead distinguishes finite constitution from continuing dependence.
Human examples may define the objective or even communicate methods without
violating the lesson merely because of their origin. Human feedback may also
genuinely report a consequence and therefore be epistemically valid, while
still failing as the long-run engine of Bitter-Lesson progress if producing
each additional judgment requires proportional human labor. The human
contribution may be rich, but it must become bounded rather than remain the
marginal source of new task-specific distinctions.

The strongest objection to making RLAIF the scalable successor is that ordinary
RLHF already trains a machine reward model from a finite body of human
comparisons, while RLAIF may merely ask an AI judge to reproduce a human-authored
preference policy. The acronyms therefore do not locate the principled boundary.
The reply must ask whether human judgments recur as the policy enters new
regions, and whether a finite human seed has constituted an evaluator stable
enough to remain valid as search enters those regions. RLAIF removes the human
label-throughput bottleneck; it does not by itself show that evaluator
staleness, reward exploitation, or new cases can be handled without recurring
human repairs.

The strongest objection to the locus-of-learning test is that engineers,
labelers, reward models, and the trained model form one coupled learning system.
The reply is not to deny hybrid learning but to locate the marginal task-specific
epistemic work. Who must formulate the new distinction that closes the error
loop? Does improvement continue after new task-specific human examples,
judgments, and diagnoses stop? Engineers may constitute tasks and improve general
meta-methods without performing every task-specific discovery for the learner.

The strongest objection to the upstream pretraining claim is that post-training
may reveal rather than create most useful capabilities. LIMA shows that a small
curated dataset can turn a strong base model into a competitive assistant and
argues that alignment mainly selects an interaction format. The reply cannot be
that the substrate lacks knowledge. Indeed, if a fixed small dataset permanently
selects the needed interaction policy, LIMA supports David's acceptance of a
finite human seed. It does not show that the resulting assistant can improve
persistently after that seed is fixed. David's alternative remains unproven
until bounded human initialization plus generated experience matches current
post-training gains and continues beyond them.

Second, existing results do not eliminate pretraining data. DeepSeek-R1-Zero
starts from a pretrained base model; AlphaProof uses a language-model formalizer
and a million natural-language seed problems. The defensible claim concerns the
marginal source of further improvement after a capable prior and system
specification exist.

Third, splitting can block transfer and create a hard routing problem. A useful
architecture may require a shared general substrate and domain-specific learning
loops rather than isolated models. How a system identifies the applicable
paradigm is outside the present hypothesis, not a problem the article claims to
have solved.

Fourth, a verifier may be precise and still specify the wrong target. Tests can
be incomplete, reward models can be hacked, and measurable proxies can diverge
from the human purpose. “Steady improvement” is meaningful only relative to a
validated metric and held-out distribution.

Fifth, Sutton and Silver now make the human-data versus experience distinction
themselves. David's independent contribution must be the encapsulation thesis:
experience becomes generative only after prior knowledge has defined a system,
and the availability and adequacy of such systems determine the reach of the
lesson.

Sixth, critics can argue that Sutton's later treatment of LLM corpora as
imported human knowledge changes the 2019 target. The original essay praises
deep learning on huge training sets and focuses on knowledge built into methods;
the later account contrasts human-produced training content with experience.
Calling this a recantation mistakes continuity in the governing principle—use
search and learning to exploit growing computation—but calling it no change at
all misses a real expansion in what Sutton classifies as the human-knowledge
approach. The article should distinguish stable principle from revised scope.

Seventh, finite resources can make a human-informed hybrid outperform pure
search or learning within the actual project horizon. This is a genuine
engineering objection and Sutton explicitly allows short-term help from human
knowledge. The reply is not that resource constraints are unreal. It is that
they delimit the regime of the lesson. The “worst of both worlds” diagnosis
applies only when the system has already incurred the costs of generality while
recurring human task-specific prescription remains the rate-limiting source of
improvement.

## Required reply

The article must define two testable boundaries. First, a candidate domain
qualifies only if its paradigm establishes: (1) an admissible state or problem
space, (2) an action or hypothesis language, (3) a transition process or
generator of new instances, (4) feedback that reliably discriminates progress,
and (5) a task distribution against which improvement generalizes. Second, an
intervention qualifies as outcome-grounded feedback insofar as it (a) is
generated by a consequence relevant to the constituted domain; (b) lets the
learner derive credit through comparison, aggregation, and generalization
across outcome-bearing experience; (c) evaluates intermediate steps directly
when they independently complete a subproblem; (d) excludes human semantic
preferences that stipulate the legitimate method beyond distinctions derivable
from the domain; and (e) remains a valid signal rather than a hackable proxy.
The article must distinguish fully verifiable, partially grounded, and
open-world domains. It may name paradigm identification and revision as limits,
but must not quietly make
them premises David has already supplied.

For each post-training intervention, the article must also identify the locus of
learning: who notices the relevant failure pattern, formulates the task-specific
correction, and selects it by evidence? The operational counterfactual is whether
improvement could continue if engineers stopped diagnosing methods while valid
outcome evidence continued to arrive. For recurrent human feedback, freeze
further task-specific input and increase compute-generated experience: the
human channel is non-rate-limiting only if the same expanding performance
frontier remains reachable.

The article must distinguish: (1) the constitutive rules that generate the
problem-space and its outcome criteria; (2) the object-level candidates explored
by search; (3) the operative policies, representations, rules, or heuristics
revised through learning; and (4) the evidence that warrants each revision. It
must not require a verbal explanation of why a learned change works, but it must
ask whether the change earned its authority from evidence available within the
constituted system. Candidate origin, validation, and retention may be tracked
separately when diagnosing hybrid cases, but occasional human-proposed
candidates must not be presented as a coequal source of scalable discovery.

The article must state the resource conditional explicitly. It may acknowledge
that finite-resource projects rationally leave Sutton's regime, but should not
revive aggregate efficiency or global-economics claims. When invoking the
midway trap, it must establish both sides: the system has incurred material
costs of general learning, and continued gains remain dependent on recurring
human task-specific method design rather than domain constitution, outcome
feedback, or a general meta-method.

The article must use base-versus-post-trained evidence against itself before
advancing the upstream thesis. It must concede that current post-training repairs
a real assistant-objective mismatch, distinguish capability acquisition from
interaction-policy selection and persistent learning, and present
domain-grounded convergence on helpfulness as a testable alternative rather than
an already demonstrated replacement.

The article must distinguish finite human initialization from recurring human
dependence. It may not object to a fixed set of human-made examples merely
because they contain preferences, solutions, or methods. State “infinite
learning from finite data” precisely as unbounded learning from bounded
human-supplied data, with total machine-generated experience allowed to grow.
The operational closure test is whether direct task-specific human intervention
can cease while valid learning continues. The outcome-versus-method distinction
still governs the ongoing learning loop, but it does not make a finite seed
illegitimate on Bitter-Lesson grounds.

The article must avoid treating *RLHF* or *RLAIF* as a conclusion. A reward model
trained once from a finite comparison set may satisfy the closure criterion; an
AI evaluator that repeatedly needs human repairs may fail it. Diagnose whether
the evaluator remains stable and corrigible as the policy reaches new cases,
not which acronym names the pipeline.

The article may use David's “leap of faith followed by rationalization” as the
rhetorical compression of this diagnosis. It must distinguish retrospective
interpretation from prescriptive rationalization: explaining a method after
outcome-grounded selection is not the target; making a human account of the
method authoritative for reward or acceptance is.

The Harari conversation supplies the article's philosophical frame rather than
an analogy. The target is architectural inconsistency: adopting general learning
as the governing paradigm, then invoking human-authored methods without a
principle that justifies the transition. An explicitly handcrafted program may
be less plausible to David, but it is outside this criticism because it has not
made and then withdrawn the general-learning commitment.

## Research-driven synthesis candidate

The LLM revolution may have learnt the Bitter Lesson in pretraining and blurred
it in post-training. Vast human data enabled a general learning process, and a
finite human-authored demonstration set, constitution, or reasoning rubric may
legitimately initialize another one. The Bitter-Lesson question is whether that
human contribution can become fixed while computation continues producing new
evaluated experience and improvement. Enough knowledge to constitute a domain
can be more generative than an indefinitely expanding corpus of its past
solutions. Put most simply: can the humans stop adding task-specific knowledge
without making the learning stop?

This formulation is provisional. It sharpens David's proposal in light of the
evidence but should not replace his wording without an argument-writing pass.

## Four kinds of human contribution

1. **Task-constituting conditions:** rules, action and observation interfaces,
   objectives, verifiers, and boundaries that determine what counts as an
   attempt or success.
2. **Outcome-grounded evaluative feedback:** a terminal verdict, learner-derived
   credit inferred by comparing and generalizing across outcome-bearing trials,
   or an evaluation of a step that independently constitutes a completed
   subproblem. The learning system may infer causal and predictive distinctions;
   human evaluators do not stipulate a preferred method independently of them.
3. **Instructional solution content:** target answers, demonstrations, process
   corrections, domain heuristics, representations, or discovered
   strategies. A bounded initial set is compatible with David's thesis if it
   seeds continuing independent learning. It becomes the clearest target of
   Sutton's warning when further progress depends on continually expanding it
   in place of the learner's own discovery.
4. **Meta-method and inductive structure:** architectures, invariances, search
   procedures, routing mechanisms, and procedures for creating or revising
   abstractions. Sutton's essay permits some of these, and OaK explicitly
   develops them.

The article's candidate contribution is not that human input is good. It is
that these roles have different relations to the Bitter Lesson and different
effects on independence. A system may discover a solution no human knew while
remaining dependent on a human-constituted verifier; conversely, a huge corpus
may supply no explicit heuristic while importing nearly the whole inherited
human answer-space. The hard cases are conditions that covertly encode a
preferred solution, measurements that mistake a proxy for the goal, and
meta-methods that are presented as neutral feedback despite carrying a
human-authored procedure.

Across all four categories, the locus-of-learning test asks where each new
task-specific distinction originates and who must close the error-correction
loop. The closure version asks whether task-specific human contributions can
eventually become fixed while the system continues to generate, evaluate, and
retain discoveries. It allows task constitution, finite examples, and general
meta-method design to remain human work while reserving continuing discovery of
successful methods for the learning system.

## Evidentiary dependencies

- **Substantially answered:** Sutton's explicit 2019 and 2025 positions;
  AlphaZero's separate trained instances; explicit use of the Bitter Lesson in
  Falcon's LLM design rationale, BIG-bench's research-allocation argument, and
  PlanSearch's learning-versus-search framing; and the existence of current
  search/RL systems built around executable or formal verification.
- **Partly answered:** the Bitter Lesson's influence on LLM development.
  *Attention Is All You Need* predates Sutton's essay and the bounded sample of
  five foundational scaling papers did not cite it, while Falcon and later
  scholarship explicitly use it as a design or interpretive frame. This
  supports a traceable reception, not a field-wide causal or consensus claim.
- **Substantially answered:** whether the alleged contradiction is itself part
  of the reception. Public replies in 2023 and post-interview commentary in
  2025 explicitly describe Sutton as contradicting, backtracking, recanting, or
  revising the lesson. No sustained peer-reviewed version was located.
- **Partly answered:** the encapsulation mechanism. PlanSearch, DeepSeek-R1,
  and AlphaProof show that search or RL becomes unusually productive where
  programs, tests, compilers, or proof assistants provide discriminating
  feedback. The current existence cases cluster in games, code, mathematics,
  and other highly verifiable settings.
- **Substantially answered:** the empirical composition of representative
  post-training methods. InstructGPT mixes demonstrations, rater instructions,
  preferences, reward modeling, and PPO; DPO fits static preference pairs;
  Constitutional AI and deliberative alignment install explicit principles or
  specifications; process supervision labels intermediate steps. These are not
  one undifferentiated form of terminal feedback.
- **Still open:** an operational encapsulation threshold; whether partially
  grounded or open-world domains can supply outcome feedback adequate for
  sustained learning; an operational line between evaluation and instruction;
  paradigm identification and revision; and David's precise novelty relative
  to Whiteson's “Sweet Lesson,” Aryandoust/Liang's “Better Lessons,” and Sutton
  and Silver's “Era of Experience.”

## Logical-map and source audit — 2 August 2026 (historical finding)

The formal audit preserved the locus-of-learning diagnostic but rejected that
version of the map as writing-ready. Its most serious issue was internal: the map said
that domain-internal evidence assigns discovery to the learning system, then
denies that status when a learner derives semantic credit from terminal
outcomes. Sutton and Barto's value functions and AlphaZero do precisely this.
The conflict is sharpened by the map's definition of the learning system, which
includes the evaluator even while E5-R treats discovery by an evaluator as
external. The required resolution was to distinguish learner-internal value or
credit inference from a separately imposed process target.

The audit also separates two standards that the previous synthesis had merged.
Sutton's standard concerns the marginal source of improvement: computation,
search, and learning must continue to dominate, while human discoveries cease
to bottleneck progress. David's evaluative-closure test is stronger: direct
task-specific human intervention can terminate while valid learning continues.
Christiano et al. show why the distinction matters. Their recurrent human
comparisons covered about 0.1 percent of interactions and decreased in rate as
experience grew. This established numerical sparsity and motivated a
counterfactual test; it did not establish that the human feedback was causally
non-rate-limiting.

The upstream pretraining diagnosis also requires reconciliation. InstructGPT
establishes that next-token prediction and assistant behavior are different
objectives. LIMA establishes that a small fixed post-training set can select
useful assistant behavior from a capable pretrained substrate. If bounded
post-training can constitute the desired persistent learning system,
representation pretraining need not itself have produced the final learning
subject. The safer target is the complete deployed architecture: it is defective
when pretraining plus post-training never becomes a domain-grounded learner of
the assistant objective. A claim that pretraining itself should have been
different remains a testable counterfactual rather than a consequence of the
base/post comparison.

The definition of generated experience now needs an independence condition.
Machine-generated examples and AI judgments can form a self-confirming loop.
Silver and Sutton's grounded-interface proposal, Gao et al.'s reward-model
overoptimization, and the positive cases of tests, compilers, game rules, and
formal verification together support a stronger requirement: the relevant
consequences must be fixed by the constituted environment or by an independently
valid verifier rather than by the candidate policy's own endorsement.

The source audit added two representative post-training cases. Llama 3 used six
rounds with new human preferences and SFT data as well as synthetic generation,
reward modeling, rejection sampling, and DPO. Gemini 2.5 describes successive
human/model iterations, human-revised responses, amortized preference data, AI
critics, predefined rubrics, and automated red teaming. Both strengthen the
existence claim that recurring human epistemic input remains important in
frontier workflows. Neither isolates its marginal causal contribution, proves
that it is rate-limiting, or licenses a field-wide verdict.

The reception record also broadened. OpenAI's ImageGPT cited Sutton in 2020;
Anthropic's 2025 Activation Oracles work calls its generalist, data-scalable
approach Bitter-Lesson compliant. Together with Falcon, BIG-bench, and
PlanSearch, these sources establish a real but semantically plural reception.
The logical map now contains the reception branch required by its title. It
defines *we* as the inspected frontier-LLM research and engineering discourse,
shows the different meanings attached to the lesson, and retains the question
form because the evidence does not establish a representative distribution of
compliant and noncompliant systems.

Finally, domain constitution remains conditional. A bounded set of rules and
examples can generate vast experience without guaranteeing infinite competence
or an adequate evaluator. Open-ended helpfulness is plural and partly normative;
continued human revision may legitimately change the constituted goal rather
than teach a method within a fixed goal. The argument should separate governance
of changing values from recurrent human diagnosis of task methods and limit its
positive architectural claim to domains with sufficiently observable,
discriminating, and stable outcomes.

## Resolution of the central audit findings — 4 August 2026

David generalized the process-supervision rule. Cross-trajectory comparison,
value learning, causal inference, aggregation, and higher-order credit
assignment are admissible when their authority comes solely from the
constituted system's formal structure, transitions, and outcomes. Discovery by
such an evaluator belongs to the learning system. A human evaluator who
diagnoses the proper method and encodes that diagnosis supplies an external
semantic process target; the discovery then belongs to the engineers. This
epistemic-provenance boundary supersedes the earlier isolation and path-
neutrality rule.

David also rejected numerical sparsity as an answer to the scaling question. A
chain is only as strong as its weakest link, and a tiny human contribution can
remain the indispensable source of progress. The positive test is to freeze
further task-specific human feedback after bounded constitution and increase
computation and system-generated experience. If the same expanding performance
frontier remains reachable, the feedback is an efficiency advantage and becomes
negligible as a source of discovery. If progress stalls, drifts, or requires new
human distinctions, the current system has not been shown to scale through
computation alone. These are the two logical alternatives: the recurrent
feedback is redundant to the learning frontier, or the system is premature and
human discovery remains on its critical path. Empirical uncertainty about a
particular system does not create a third category.

The code-breaking example demonstrates the relevant order of magnitude: perfect
human solution knowledge can be outrun by scalable search. Musk's “few cells”
spreadsheet example supplies an independent illustration of the same weakest-
link principle. Neither example substitutes for a fixed-feedback ablation in an
actual post-training system.

## Bounded empirical extraction — 4 August 2026

The aborted comparative case study yielded three points worth retaining. First,
a successful verifier-grounded training stage does not classify the whole
assistant pipeline that contains it. Second, visible recurrence of human input
establishes a hybrid workflow but does not by itself prove that the input is
causally indispensable. Third, DeepSeek-R1-Zero and AlphaProof provide bounded
positive illustrations of learner-governed progress under fixed formal
evaluation. These points protect the argument from overclaiming; they do not
require a system-by-system technical survey.
