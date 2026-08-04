# have we learnt the bitter lesson?

Status: active research and argument project — eight research passes complete;
publication candidate, not yet a manuscript.

## Active objective

Turn David's insights developed in the ChatGPT conversation *The Better Lesson
2* into a source-grounded written piece asking what Sutton's essay actually
teaches and whether its lesson has been learnt accurately. The piece should
preserve the conceptual argument before fixing its eventual publication
format. It must distinguish David's claims, Sutton's explicit claims, broad ML
reception, and the narrower LLM-era engineering reception.

The article does not depend on Sutton's essay having caused the LLM revolution
or having served as its acknowledged technical cornerstone. David focuses on
it because it gives unusually clear expression to the paradigm shift he sees in
modern system development, especially LLM development: the move from
human-authored task methods toward general search and learning methods whose
capabilities grow with computation. Its direct historical influence may be
limited while its analytical importance remains substantial.

The argument is an internal consistency test rather than a proof of Sutton's
prescription. David considers the prescription plausible and its results
impressive, but the article need not establish that it is ultimately correct.
Its central criticism is conditional: a development program that makes the
general-learning wager, derives its rationale from that wager, and then places
recurring human method discovery back on the critical path has abandoned its
organizing principle midway.

The ultimate claim has now moved upstream. Post-training remains the immediate
evidence and diagnostic site, but David's conclusion is that its demonstrated
necessity exposes a defect in what pretraining was designed to produce. The
article must determine whether this means pretraining was ineffective, merely
incomplete for assistant use, or organized around the wrong learning object.
Its positive criterion is now explicit: a bounded stock of human-made examples
is fully compatible with the lesson if it constitutes a system capable of
continuing improvement without an unbounded stream of further human
interventions.

The source audit now separates David's upstream hypothesis from the conclusion
established by current evidence. Base/post comparisons establish an objective
mismatch, and LIMA establishes the leverage of a finite post-training seed. The
evidence supports a defect in the complete deployed learning system more
directly than a defect in capability pretraining itself. Whether pretraining
should have produced a different learning subject remains a counterfactual to
be argued and tested.

## Artifact architecture

The project persists knowledge in maintained files rather than raw conversation
history:

- `working/logical_map.md` owns the concise, ordered logic used to plan and
  write the article.
- `working/logical_map_audit.md` owns the current adversarial review of that
  logic: coherence defects, source coverage, unresolved objections, and
  revision dispositions.
- `working/argument_map.md` owns the cumulative running synthesis of the
  conversation, corrections, objections, and exploratory argument development.
- `working/research_summaries.md` owns verified online research.
- `sessions.md` owns source-conversation provenance.
- `current.md` owns active state, formulation, and open work.
- `manuscript/` is reserved for the eventual article and publication package.

The working environment is the current priority. No manuscript draft has begun.

## Current formulation

Post-training alignment is the article's immediate diagnostic target, while
David's upstream hypothesis makes pretraining its ultimate target. Large-scale
language-model pretraining
may still be a strong instance of Sutton's 2019 lesson at the level of learned
representations: a general statistical method trained on huge datasets displaced
hand-authored linguistic knowledge. Sutton himself included “learning on huge
training sets” in his speech-recognition example, so the article must not
manufacture a simple opposition between pretraining and the Bitter Lesson. The
stronger hypothesis is that pretraining learned an extraordinarily capable
substrate while organizing learning around the wrong terminal object for
deployment.

The decisive question begins when a broadly pretrained model is made to behave
as an assistant. Post-training is commonly described as learning from human
feedback, inviting an analogy between a user's thumbs-up and checkmate: both
appear to be outcome signals that return the learner to the arena without
supplying the winning strategy. David's concern is that this description can
become a carte blanche for reintroducing human-built methods while retaining
the rhetoric of general learning.

David's boxer illustration represents the permissible case, not the teaching
case. People surround the arena, evaluate the result, and push the boxer back
in for another attempt without telling the boxer how to fight. The loop may be
repeated and deliberately behavior-changing while remaining outcome-grounded
trial-and-error learning. What would cross the line is not returning the boxer
to the arena, but adding coaching, demonstrations, preferred combinations, or
a scoring rule that rewards a human-selected style independently of winning.

The actual alignment stack mixes categorically different human contributions.
Human approval or dissatisfaction may sometimes constitute genuine feedback
about whether an action achieved a human purpose. But demonstrations, detailed
rater instructions, preference datasets, learned reward proxies, constitutions,
step-level process labels, safety specifications, and prescribed reasoning over
policies can also supply desired behavior, distinctions, or methods. Passing
these through a scalar reward, preference model, or synthetic-data pipeline
does not by itself turn them into environmental consequences.

David sharpens the question: are we evaluating an outcome, or steering the
system toward a desired outcome? These cannot be distinguished by causal purpose
alone. Every training signal is intended to change behavior, including checkmate
in self-play, and every learning system has some predefined success criterion.
The stronger distinction concerns what remains fixed while learning occurs.
In outcome-grounded learning, a behavior is selected because it improves an
independently constituted task outcome. In policy steering, the desired behavior
or route is itself supplied as the target, whether or not its superiority follows
from the task outcome.

Process supervision is the decisive middle case. The learning system may
compare trajectories and iterations, generalize across them, and infer which
states, actions, or intermediate steps contributed to success. This is ordinary
higher-order learning when the distinctions are derived from the constituted
domain's transitions, formal structure, and outcomes. A formal proof step may
also receive direct evaluation because validity is itself a determinate local
result. The governing question is the provenance of the distinction: did the
system discover it from evidence available within the domain, or did a human
evaluator stipulate the legitimate method independently of that evidence?

Outcome equivalence must be assessed against the domain's complete legitimate
outcome measure. If one route causes additional harm, violates a rule, consumes
relevant resources, or succeeds too late, the processes are not equally
successful when those consequences belong to the constituted task. But once
all such outcome dimensions are included, an external evaluator has no warrant
to rank equivalent routes by a human semantic preference. The learner remains
free to infer predictive or causal distinctions from repeated evidence.

David identifies the structure as analogous to job discrimination. An employer
purports to evaluate job-relevant performance but wrongfully ranks people on a
characteristic irrelevant to that performance; a human-authored process target
purports to evaluate success but ranks trajectories on a feature irrelevant to
the complete outcome. The shared principle is not that evaluators may never discriminate in
the literal sense of drawing distinctions. They may distinguish any factor that
changes the legitimate outcome. They may not use an outcome-irrelevant feature
to rank otherwise equivalent candidates, performances, or learning paths. This
is currently a structural analogy, not a researched claim about employment law.

A fixed positional schedule that rewards later steps more than preliminary
ones is one valid form of retroactive credit propagation. It is not the
exclusive form. Value functions, advantage estimates, and process models also
belong to the learner when their distinctions are learned solely from the
constituted system's outcome-bearing experience. The learner may thereby
distinguish a reliable method from a lucky error. The prohibited move is for
the human feedback mechanism to pre-label that distinction as an authoritative
semantic preference.

This yields another formulation of the central test: is the learning done by
the model or by the engineers? More precisely, where does the task-specific
epistemic work occur? If engineers or labelers inspect failures, decide which
step was wrong, formulate the better distinction or method, and encode it into
demonstrations, constitutions, rubrics, or process rewards, then the engineers
have learned what improves performance and transferred their discovery into the
system. If the system receives outcomes and discovers for itself which internal
regularities improve future performance, the system is doing the learning.

The relevant learner need not be a single weight-updating model. It may be the
larger learning system: model, search, memory, tools, optimizer, and persistent
agentic application. Nor does the distinction require engineers to disappear.
They may constitute the paradigm, specify legitimate outcomes and constraints,
and improve general learning machinery. The Bitter-Lesson question is whether
continued task-specific improvement depends on repeated human diagnosis of the
method. A useful counterfactual is: if engineers stopped explaining failures
while outcomes continued to arrive, could the system continue to improve?

David now proposes using the same boundary to clarify Sutton's two privileged
methods. **Search** explores a field of possibilities already made available by
the paradigm. The possibilities need not be individually enumerated or known in
advance: chess rules, for example, intensionally generate possible positions and
games far too numerous to list. What search adds is not a new human description
of which possibilities exist or should be preferred, but new evidence produced
by exploring particular candidates and observing how they fare under the
system's existing transition and outcome rules.

**Learning** carries such evidence forward by changing the system's reusable
policy, representation, rule, or heuristic. Mere modification is not sufficient
to make the change learned. From the learner's point of view, the change must be
warranted by evidence that the constituted system itself makes available: the
same admissible actions, consequences, and success criteria by which attempts at
the problem are judged. This need not be an explicit verbal or causal
explanation of *why* the change works. It may be an empirical demonstration that
the change improves outcomes. But if a new method is accepted simply because an
engineer supplied or preferred it, its epistemic warrant remains external to the
learning process.

This requires keeping two kinds of rules apart. The paradigm's **constitutive
rules** define the problem-space and remain fixed within David's present
hypothesis; revising them would raise the separate problem of paradigm shift.
The learner's **operative rules or heuristics** are candidates for revision.
They count as learned to the extent that their generation, testing, selection,
and retention are answerable to evidence produced under the constitutive rules.
A human-proposed heuristic that the system subsequently tests is logically a
hybrid case: its origin is external, while its validation may be internal. But
David rejects treating this as a coequal third method. In Sutton's long-run
scaling frame, human proposal is a bounded, non-scaling channel. Automated
search and learning can keep converting more computation into more generated
and tested possibilities; human method discovery cannot expand at the same
rate. This is what it means for general methods to *outrun* or *outperform* the
human-knowledge approach: not that every human proposal is worthless, but that
systemic discovery eventually overwhelms it as a source of progress.

David's limiting example is brute-force code breaking. Suppose the code belongs
to a finite, already defined space and each attempted code receives an immediate
valid or invalid result. A human knows the correct code; the search system knows
no solution-specific fact at all. Yet if the system can generate and test
candidates quickly enough, it can open the lock before the human can communicate
or enter the answer. The human has the maximum possible informational advantage,
but that advantage is fixed. The searcher's throughput can continue increasing.
In this sense scalable search can outrun not merely human expertise but a human
who already possesses the complete solution.

The example does not show that brute force is more sample- or
operation-efficient: it may test vastly more candidates than the knowledgeable
human. It isolates Sutton's performance claim under abundant computation. Its
validity also depends on the constituted domain: the code space must be bounded,
trials must be cheap and sufficiently parallel or rapid, and the lock must
provide a reliable verifier without a prohibitive attempt limit. Those
conditions do not weaken the example; they show why a well-defined paradigm is
the necessary condition for search to convert computation into discovery.

The same example clarifies why a small percentage of human work is not by
itself a scalable compromise. A composite learning system advances only as far
as its least scalable indispensable component: a chain is only as strong as its
weakest link. The human who knows the code may contribute one operation among
billions, yet the system still depends on that operation if it cannot reach the
same expanding performance frontier without the answer. The decisive question
concerns causal necessity under scale, not the present fraction of work.

Elon Musk offered a parallel illustration in *Moonshots* #220. He argued that a
spreadsheet with even “a few cells” completed manually could not compete with
an all-computer spreadsheet; after Dave Blundin sharpened the example to one
cell, Musk agreed. The episode was recorded on 22 December 2025 and published
on 6 January 2026 ([official episode](https://www.youtube.com/watch?v=RSNuB9pj9P8),
[episode page](https://www.diamandis.com/podcast/elon-musk-agi-timeline-copy-code)).
This is an independent illustration of critical-path competition, not evidence
about RLHF.

David now identifies efficiency or insufficient resources as the one direct
way to resist Sutton's prescription. But this is primarily a challenge to the
regime in which the Bitter Lesson applies. Sutton's argument begins from the
availability of enough computation, and from general methods that can continue
to exploit more of it. If adequate resources will not exist within the relevant
time horizon, one may rationally choose a more efficient human-informed method;
one has then declined Sutton's premise rather than refuted his conditional
conclusion. The article need not revive its retired claims about aggregate
resource consumption or global economics to state this boundary.

The sharper criticism concerns abandoning Sutton's method midway. A project may
pay the costs of generality—large-scale training, search, opacity, and a system
not organized as an explicit expert program—then make further improvement
depend on continuing human diagnoses, demonstrations, rubrics, or preferred
methods. It thereby preserves the costs and unpredictability of a general
learner while reinstating the bottleneck and eventual plateau of hand-designed
knowledge. It is neither the cheap, legible expert system one might choose under
strict resource limits nor the scalable learner promised by the Bitter Lesson.

This “worst of both worlds” claim is conditional, not an indictment of every
hybrid. Human input may efficiently constitute the domain, supply a general
meta-method, or bridge a genuinely finite-resource horizon. The trap occurs when
the system has already been built as a general learner but recurring
task-specific human prescription remains the marginal source of improvement.
That is the form of mid-course abandonment the article should test in LLM
post-training. David confirms that this is a precise description of where
current LLM development stands.

David compresses the predicament as **taking the leap of faith and then
continuing to rationalize**. The material wager has already been made: enormous
resources are committed to a general learner precisely because its successful
methods cannot all be specified in advance. But the wager is withdrawn
epistemically when post-training still requires the learner's behavior to pass
continually through new human-authored explanations, distinctions, and preferred
paths before it is accepted. We entrust discovery to learning, then keep trying
to reason our way through each new frontier ourselves.

The separate *Yuval Noah Harari Analysis* conversation states this philosophical
structure directly. David described his fascination with the Bitter Lesson as
arising from seeing it as a paradigm shift, then clarified: “My claim about LLM
design is never that they chose the wrong path; it's that they are inconsistent.”
The criticism does not apply to someone who explicitly continues to pursue
handcrafted AI. It applies to an architecture that adopts general learning as
its governing principle and then silently changes explanatory or operational
regimes when convenient. David's Newtonian example makes the demand precise: a
mechanistic framework cannot invoke teleology when it suits the argument without
an explicit principle licensing the transition. The article applies that same
demand for architectural consistency to the transition from scalable learning
to recurring human-authored method.

The double meaning of *rationalize* is useful but must be controlled. Explaining
or interpreting a method after it has been selected by outcome evidence need
not interfere with learning. Nor is the human constitution of safety constraints
or legitimate outcomes an illicit demand for rationality. The contradiction
arises when a human rational reconstruction becomes the authority that selects
the method—when the system is rewarded for following our account of why a
solution should work rather than for demonstrating that it works under the
domain's outcome criteria.

The simple comparison between base and post-trained models corrects any stronger
version of this criticism. Post-training plainly improves performance on the
assistant objective. In InstructGPT, human evaluators preferred the 1.3-billion-
parameter post-trained model to the 175-billion-parameter GPT-3 base model, and
the matched 175-billion-parameter comparison strongly favored InstructGPT. The
article therefore cannot imply that an existing base model would perform better
if engineers simply stopped post-training it. Current post-training repairs a
real mismatch.

David draws the ultimate conclusion upstream: **pretraining was not done right
in the first place**. The strongest defensible meaning is not that pretraining
failed to learn language, knowledge, or capabilities. It is that pretraining was
organized around the wrong learning object for the deployed system. Predicting
the next token in inherited human text is a determinate and highly productive
task, but it is not the task of acting persistently within a constituted domain,
observing consequences, and improving from outcome-grounded experience.
Post-training becomes necessary because the base learner was never trained as
that kind of subject.

The empirical result establishes an objective mismatch, not the superiority of
David's proposed replacement. InstructGPT's own account says next-token
prediction and helpful, safe instruction-following are different objectives.
Conversely, LIMA provides the strongest counterinterpretation: it reports that
almost all knowledge and capabilities are acquired in pretraining and that only
a small, curated set may be needed to teach the format or style of assistant
interaction. On that view, pretraining produced the right capability substrate
and post-training mainly exposes or routes what is already there.

David's claim survives this objection only in the more exact form: a substrate
can contain impressive capabilities without being a Sutton-like developing
learner. Even “superficial” alignment leaves the deployed system dependent on an
externally supplied interaction policy and does not create persistent,
outcome-grounded improvement. The article's positive hypothesis is therefore
counterfactual and remains to be demonstrated: training should have been
organized from the outset—or at least continued—within human-identified domains
that generate actions, consequences, verifiable outcomes, and new experience,
rather than requiring an indefinitely expanding stock of human-authored
assistant behavior to repair each new mismatch after static-text pretraining.

David's compressed formulation is **you get what you inspect**. Pretraining
inspects next-token prediction and therefore produces an extraordinarily capable
predictor. Human-guided post-training inspects conformity to demonstrations,
preferences, specifications, or chosen process features and therefore improves
those measured behaviors. A Sutton-like developing system would instead inspect
consequences within a constituted domain, requiring the learner to discover
which methods produce success. The issue is not that optimization failed, but
that each phase successfully learned what its evaluative apparatus made visible.

David states the corresponding design demand directly: **if the intended system
was a helpful assistant, pretraining should have used an algorithm capable of
converging on helpfulness on its own**. “On its own” does not require the learner
to invent helpfulness as a value. Humans may constitute the goal, legitimate
constraints, and outcome measures. It requires the learner to discover the
methods that produce helpful consequences after any bounded human seed, rather
than receive an unbounded sequence of human examples of what helpful behavior
should look like. The goal and initial examples may be ours; the continuing
route must be the learner's.

This exposes the central unresolved difficulty rather than hiding it. Open-ended
helpfulness is not presently a clean verifier like checkmate or a compiler. If
helpful consequences cannot be defined, observed, and attributed well enough to
support convergence, then the general-assistant problem is not yet a
Sutton-ready domain. Demonstrations and preference labels may still produce a
more useful product, but they compensate for the missing learning system; they
do not show that the learner discovered helpfulness from experience.

David now prevents this scalability criticism from becoming an objection to
finite human knowledge as such. If a bounded set of predefined, human-made
examples is enough to initialize the system, he accepts it completely. This is
not a concession external to his argument; it is the positive architecture he
has been proposing: **infinite learning from finite data**.

The phrase must be made exact. It means unbounded or open-ended learning from a
bounded stock of **human-supplied** data, not literal learning forever from a
fixed total evidence set. The human seed may specify rules, principles,
preferences, examples, or even useful methods. What makes it generative is that
the resulting system can then produce new trials, observations, comparisons,
and consequences computationally. Total experience may grow without bound even
though imported human examples do not.

The decisive distinction is therefore temporal rather than genealogical:

1. **Finite constitution:** humans may provide a bounded initialization that
   makes the domain, objective, evaluator, or initial policy available.
2. **Continuing learning:** after that setup, further task-specific improvement
   must be driven by machine-generated and machine-evaluated experience rather
   than an unbounded sequence of new human examples or judgments.

This yields a closure test for a successfully constituted domain: **can direct
human task-specific intervention cease while valid learning continues?** If it
can, the human examples function as a finite seed or fixed prior. If every new
region of behavior requires humans to diagnose the failure, add a distinction,
or supply another preferred example, the supposed domain was not encapsulated
well enough to support Sutton-like learning.

Sparse or declining-rate feedback creates no third category. Its status is
settled by a fixed-feedback counterfactual: freeze further task-specific human
input after bounded constitution, then increase computation and system-generated
experience. If the same expanding performance frontier remains reachable, even
at a different computational cost or along a different learning curve, the
feedback was an efficiency advantage and becomes negligible as a source of
discovery. If progress stalls, drifts, or requires new human distinctions, the
human channel remains on the critical path and the architecture has not been
shown to scale through computation alone. The experiment determines whether the
feedback is redundant or the system premature; uncertainty about the result is
an evidentiary gap rather than an intermediate architecture.

The earlier outcome-versus-method distinction remains useful, but it no longer
disqualifies a finite setup merely because human examples contain solution or
method knowledge. It diagnoses what happens inside the continuing learning
loop. The boxer repeatedly returned to the arena receives method-neutral
feedback, so the learning rule can be technically valid; but if a human must
judge every bout forever, the system cannot practically satisfy Sutton's
scaling condition. Semantic validity of the reward is not enough when reward
production remains an indispensable human dependency.

The names *RLHF* and *RLAIF* become secondary under this criterion. Canonical
RLHF already amortizes a body of human comparisons into an automated reward
model. If a fixed, finite body of comparisons really suffices and the reward
model continues to support learning under new policy behavior, that arrangement
is compatible with David's claim. Bai et al.'s iterated online RLHF, however,
refreshed the preference model and policy weekly with new human feedback; to the
extent such refreshes remain necessary indefinitely, the human contribution has
not terminated.

RLAIF is one candidate for crossing this closure boundary. Humans may use a
finite constitution, comparison set, or calibration sample to establish an AI
evaluator, after which AI systems generate the volume of subsequent feedback.
Constitutional AI makes this architecture explicit, and Lee et al. report
comparable task performance from AI-generated and human-generated preferences.
But RLAIF is not privileged by name. The relevant question is whether its
finite human seed actually closes the environment. If the evaluator becomes
stale, exploitable, or unable to judge new cases and engineers must repeatedly
repair it with new task-specific distinctions, direct human intervention
remains indefinitely necessary and the human bottleneck has merely moved up one
level. A domain-native verifier, a stable learned evaluator, or another
automated consequence mechanism can all qualify if they let learning continue
after the human input has become fixed.

This is an interpretation of Sutton's scaling argument, not a quantitative
limit he proves. David further rejects treating the exceptional leverage of a
human-designed meta-method as a counterweight. If one such intervention can
transform performance, that ordinarily shows that the system had not yet begun
to exploit the relevant dimension of algorithmic search or learning. The human
contribution may unlock a field; the growing body of discoveries within it is
then produced by the scalable method. Its leverage is therefore evidence of
untapped algorithmic potential, not of human proposal as a rival discovery
process.

One boundary remains. If the intervention only exposes possibilities already
generable and testable under the learner's existing grammar, it unlocks the
potential of that learner. If it changes what hypotheses, representations, or
methods the learner can express and test, it creates a materially new learner
rather than revealing latent potential in the old one. David's current
paradigm-bound hypothesis does not claim that a system can discover such changes
to its own constitutive or algorithmic grammar. The article should therefore
distinguish unlocking a scalable method from redesigning the meta-method, while
refusing to treat either case as evidence that a continuing stream of human
task-specific heuristics can scale competitively.

This suggests replacing *natural feedback* with the less ambiguous term
*outcome-grounded feedback*. The diagnostic question becomes: is the
intermediate distinction derived by the learner from the constituted domain's
formal structure, transitions, and outcomes, or supplied as an authoritative
human semantic preference? Terminal verdicts, independently verified
subproblems, and cross-trajectory credit inference can all be outcome-grounded.
Their formal resolution differs; their epistemic authority comes from the same
system the learner is trying to master.

The remaining direct criticism of Sutton is therefore a missing boundary
criterion. Sutton and Silver explicitly allow human interaction, satisfaction,
and user-guided reward to count as grounded experience. That is defensible when
human response is part of the domain's objective. But without a distinction
between signals answerable to an outcome and signals that independently specify
a policy, the category of *experience* can absorb precisely the human-built
structure the Bitter Lesson warns against. The issue is not whether feedback
comes from a human or arrives at the end; it is what role the contribution plays
in defining the target of learning.

## Positive proposal under test: enough knowledge to encapsulate the system

David's new positive claim is that Sutton-like learning can occur only within a
well-defined system. The knowledge required at the outset need not contain
solutions, but it must be sufficient to encapsulate the system: what states and
actions are possible, how actions produce consequences, and what counts as
success or failure. Chess rules are a compact generative specification of an
enormous space of possible games. Once that specification exists, historical
game records are not the privileged or limiting source of improvement; search
and self-play can generate new experience.

David clarifies that *domain* is paradigm-like in the rule-constituting sense.
It is not a taxonomic slice of a pre-existing world. It establishes a field in
which entities become relevant, questions and moves become admissible,
consequences become legible as evidence, and success and failure can be judged.
The domain therefore does not merely bound learning from outside; it creates
the problem-space within which search and learning have determinate meaning.
David's current hypothesis begins after such a paradigm has been identified.
It does not claim that a model can discover which paradigm applies, identify
new paradigms, or revise and replace them.

The corresponding criticism of general-purpose LLM development is not that its
training lacks any boundary or metric. Pretraining has a precise system—token
sequences and predictive loss—but that system does not coincide with the open
range of goals for which the resulting model is used. The missing object is a
task environment whose feedback reliably measures truth, usefulness, or success
across those heterogeneous uses. Accumulating examples can partially compensate
for this mismatch without supplying the action–consequence loop required for
Sutton-like discovery.

David's constructive proposal is therefore domain decomposition understood as
paradigm construction. A rule-constituted field with a sufficiently complete
interface, problem or experience generator, and trustworthy verifier or reward
can convert additional compute into search, reinforcement learning, and
self-generated experience. Marginal improvement within such a domain may then
cease to depend on indefinitely expanding the human-authored corpus.

This claim requires two qualifications. First, *domain* must mean more than a
topic label: splitting “medicine,” “law,” or “physics” into datasets does not by
itself constitute a field of admissible problems, moves, evidence, and success
criteria. Second, the claim concerns dependence on pre-existing human examples,
not the amount of experience required. AlphaProof, for example, learns within
the formal Lean environment but uses tens of millions of generated problems and
very large amounts of computation. The proposed shift is from inherited
examples to generated, evaluable experience—not from much data to little data.

Paradigm identification and paradigm shift are therefore scope limitations and
future research questions, not hidden requirements of the present proposal.
The proposal is conditional: given a human-identified paradigm, train and
evaluate the model differently within the field that paradigm constitutes.

## Research status — 4 August 2026

The first deep online-research pass and seven targeted follow-up passes are
preserved in `working/research_summaries.md`. They cover Sutton's essay and later OaK
architecture; the contemporaneous “Sweet Lesson” reply; AlphaZero; learned
branching, modular networks, task routing, sparse experts, and routed scaling;
unified generalist counterexamples; scholarly and engineering reception; and
the relationship between foundational LLM scaling papers and the Bitter Lesson;
Sutton and Silver's later “era of experience” position; current reinforcement
learning and tool-use developments; representative current post-training
pipelines; canonical reinforcement-learning credit assignment; and the
now-retired compute/energy line.

The eighth pass audited the logical map against the full source base and added
targeted primary sources where its support was weak. The audit is persisted in
`working/logical_map_audit.md`. Its two central conceptual objections are now
resolved. Learner-internal credit inference is admissible when it is derived
from the constituted system's formal structure and outcomes; an externally
imposed human semantic process target is not. Sparse recurrent feedback is
classified through the fixed-feedback counterfactual rather than by its
percentage of interactions. The article does not need to classify current
systems exhaustively. Verifier-grounded stages such as DeepSeek-R1-Zero and
AlphaProof establish the bounded possibility of learner-governed progress;
disclosed assistant pipelines establish recurring human input without proving
its causal indispensability. These cases support the conditional argument and
its evidentiary limits rather than a technical survey. Evaluator validity and
domain sufficiency remain open.

The third pass established explicit LLM-era reception and tested the bounded-
system proposal. *Attention Is All You Need* predates Sutton's essay and is an
architectural precursor rather than reception evidence. The Falcon model report
explicitly says its design philosophy was inspired by the Bitter Lesson and
operationalizes that philosophy as performance, data, and hardware scalability.
BIG-bench invokes Sutton to identify problems likely to be solved by scale, and
an ICLR 2025 code-search paper treats learning and search as the lesson's two
scaling axes. DeepSeek-R1-Zero, PlanSearch, and AlphaProof provide conditional
support for the positive thesis: when a domain supplies reliable verification,
more compute can improve performance through RL or search. They also expose the
limits—narrow domain coverage, dependence on a pretrained base or generated
curriculum, and potentially enormous experience requirements.

The fourth pass tested the new post-training focus. InstructGPT combined
human-written demonstrations, detailed labeling instructions, ranked outputs,
a learned reward model, and PPO; it was never simply a stream of thumbs-up
signals. DPO makes the distinction even clearer by reducing preference
alignment to classification over a static preference dataset rather than
learning through environmental interaction. Constitutional AI and deliberative
alignment explicitly introduce human-authored principles or safety
specifications and procedures for applying them. Reward-model overoptimization
shows that maximizing the learned proxy can reduce performance under the
underlying evaluator. Silver and Sutton nevertheless allow human satisfaction
as a top-level signal combined with grounded environmental measures, leaving
the conceptual boundary between feedback and imported method unresolved.

The fifth pass tested process supervision as a middle case. Classical reward-
shaping theory distinguishes intermediate rewards that preserve the original
optimal policy from rewards that change it. More recent work shows that process
rewards can be derived from outcome-only trajectories, rollout-based advantage
estimates, formal or algorithmic verifiers, and internally corrected failed
trajectories. David's revised criterion admits these methods when the learning
system derives their distinctions solely from the constituted domain's formal
structure and outcome-bearing experience. It excludes externally supplied
human semantic rankings that define the proper method independently of that
evidence. This restores canonical value learning and AlphaZero to the positive
case while retaining the locus-of-learning test.

The earlier research corrections constrain the article:

- Sutton's target is fixed human-discovered world content, not architecture as
  such. His own later architecture contains learned components and abstractions.
- AlphaZero trained separate chess, shogi, and Go instances while reusing the
  same general method and architecture. The chess/Go example is historically
  better grounded than expected, but the proposed classifier remains David's.
- The empirical synthesis is adaptive sharing: fixed routing, learned routing,
  shared trunks, and unified models can each win under different conditions.
- “Field reception” is too broad. The monolithic/end-to-end extension should be
  attributed to named LLM-era engineering interpretations unless a later study
  establishes wider prevalence.
- The affirmative efficiency and aggregate resource-consumption argument is
  retired from the article. Resource sufficiency remains relevant only as the
  boundary premise of Sutton's conditional claim and as part of the
  finite-horizon objection. The piece will not move into global economics.
- The 2019 essay itself treats huge training sets as an instance of scalable
  learning. The article cannot claim that accumulating training data is simply
  contrary to Sutton's original lesson.
- A bounded check of five foundational LLM scaling and model papers found no
  citation to Richard Sutton or *The Bitter Lesson*. This does not disprove
  intellectual influence, but it rules out treating the sampled papers as
  evidence that the essay was their technical cornerstone. The article instead
  uses Sutton as a clear articulation of a development paradigm whose presence
  in LLM development can be assessed independently of direct textual influence.
- Frontier LLM work is no longer exhausted by enlarging pretraining corpora:
  large-scale reinforcement learning, execution feedback, tool use, and
  agent-generated trajectories are active development directions. The article
  must therefore keep pretraining/data maximalism as context and examine the
  composition of post-training alignment, not treat the whole current LLM
  industry as static-data scaling.
- Explicit reception evidence now exists. Falcon's builders directly identify
  the Bitter Lesson as their design philosophy and connect it to scaling model
  performance, data, and hardware; BIG-bench and PlanSearch make related
  scholarly extensions. The article can document a real LLM reception without
  claiming that Sutton caused the Transformer or the original scaling results.
- *Attention Is All You Need* cannot be evidence of Sutton's influence because
  it predates his essay. It is relevant as the scalable architecture that later
  writers retrospectively place within the lesson.
- A well-defined domain can replace dependence on pre-existing solution data
  with self-generated, verifiable experience, but it does not make data or
  experience volume irrelevant. Domain splitting is productive only when it
  supplies a generator or environment and an adequate verifier or reward.
- Explicit “recanting” and “backtracking” reactions to Sutton exist, including
  a 2023 exchange he answered directly and detailed responses to his 2025
  interview. They mistake the continuity of his preference for scalable search
  and learning, but they notice a real change of scope: the 2019 essay praised
  huge training sets while opposing human knowledge built into methods; the
  later critique also treats human-produced training content as inherited
  knowledge. The article should analyze this as stable principle plus expanded
  target, not dismiss it as either simple contradiction or simple continuity.
- David's domain hypothesis does not currently include paradigm recognition or
  paradigm shift. It proposes different training within a paradigm already
  identified by humans. Whether a model can identify, select, or revise
  paradigms remains open and must not be added as a required premise.
- The article is principally about post-training alignment, not pretraining.
  Its central test is whether an intervention supplies outcome feedback or
  reintroduces demonstrations, distinctions, policies, reasoning procedures, or
  other human-built methods under the permissive label *feedback*.
- One-shot versus iterative is not by itself the boundary between feedback and
  alignment. Repeated terminal outcomes can support autonomous learning without
  teaching a strategy. Intermediate reward is permissible when its distinctions
  are derived from the constituted system's outcomes, including by comparison
  and generalization across trials, or when a step is itself an independently
  completed subproblem.
- Rollouts, value functions, advantage estimates, and process models may
  distinguish reliable methods from lucky mistakes when the learner derives
  the distinction from outcome-bearing experience. A human-authored semantic
  judgment that specifies the proper method is a separate target.
- Content-blind retroactive propagation, including greater weight for later
  steps, remains a valid special case rather than the governing restriction.
- The job-discrimination analogy applies to an external evaluator that ranks
  otherwise outcome-equivalent processes by an outcome-irrelevant human
  preference. It does not apply to distinctions the learner discovers from
  repeated outcome evidence. The analogy remains conceptual unless its legal
  details are separately researched.

The logical-map audit adds the following constraints:

- Separate **Sutton's criterion**, under which computation must govern marginal
  progress and human input must cease to bottleneck it, from David's stronger
  **closure criterion**, under which direct task-specific human intervention can
  terminate while valid learning continues.
- Do not infer independence from numerical sparsity. Christiano et al. establish
  amortized, declining-rate human feedback, not that the system reaches the same
  expanding frontier when further feedback is frozen. Treat the human channel
  as non-rate-limiting only after that counterfactual is supported.
- Preserve the resolved credit-assignment boundary. Sutton and Barto's value
  learning and AlphaZero's outcome-trained state values belong to the learner;
  an independently supplied human semantic process target belongs to the
  engineers.
- Reframe the upstream pretraining claim at the level of the complete learning
  system. InstructGPT establishes objective mismatch and LIMA establishes the
  power of a finite alignment seed; neither proves that capability pretraining
  itself should have optimized the deployed assistant objective.
- Require generated experience to be grounded by a constituted environment or
  independently valid verifier. A model-generated example approved by a
  correlated model is not evidence of closure merely because it is produced at
  machine scale.
- Treat domain sufficiency as an empirical condition. Rules and examples can
  initialize a learner without supplying stable evaluation for open-ended
  helpfulness, and continuing human revision may govern legitimate changing
  values rather than teach a method within one fixed domain.
- Replace literal claims of infinite competence with open-ended or compute-
  scalable improvement over a stated horizon. The inspected systems expand
  learning beyond finite human seeds; they do not establish endless progress.
- Add a reception branch to the logical chain. ImageGPT and Activation Oracles
  broaden the direct reception record, while Llama 3 and Gemini 2.5 provide
  representative hybrid post-training cases. Together they support a bounded
  frontier-LLM case study, not a verdict about machine learning as a whole.

A promising four-part distinction now organizes the next pass. Human input can
(a) constitute the task by specifying rules, interfaces, objectives, and
verifiers; (b) provide outcome-grounded signals, either terminal, learned by
comparison and generalization across trials, or independently verified as
completed subproblems;
(c) encode a preferred solution, behavior, semantic process ranking, or policy
independently of the outcome; or (d) provide general meta-methods and inductive
structure through which learning occurs. Sutton's warning bears most directly
on (c), while his successful examples depend on (a) and (b), and his acceptance
of invariances and OaK shows that he does not simply reject (d). The article's
contribution may lie in preventing these roles from being collapsed into
“human knowledge” or “feedback.”

The emerging organizing question is the locus of learning. Who must discover a
new task-specific distinction before the next improvement can occur: the
learning system, or the engineers and evaluators around it? This does not reduce
every hybrid pipeline to one side. It asks which party performs the marginal
epistemic work and whether performance can continue improving without repeated
human method diagnosis.

## Argument recovered from the source conversations

David's active formulation now has four movements:

1. **Fulfilment and reversal.** Static-data pretraining first realized the
   Bitter Lesson by replacing hand-designed linguistic solutions with a general
   learning method, but may reverse into a human-knowledge approach when progress
   is identified with ingesting an ever larger inherited human record.
2. **Training versus developing learning.** More exogenous examples can improve
   a model, but that is different from a persistent agent generating evidence
   through action, observing consequences, and changing in response. The
   article must state this as a distinction between learning regimes, not deny
   that pretraining is learning.
3. **Conditions and relative independence.** Experiential learning still works
   under constituted conditions: objectives, feedback or verifiers, action and
   observation interfaces, sufficiently stable causal relations, workable
   system boundaries, and adequate experience. Those conditions both enable and
   limit learning, and preserve a qualified dependence on prior human knowledge.
4. **Encapsulation and domainization.** Once enough prior knowledge encapsulates
   a domain's possible actions, consequences, and success criteria, new human
   solution examples need not remain the marginal source of progress. Search
   and learning can generate their own experience. Dividing open-ended LLM use
   into verifiable learning systems may therefore redirect scaling from corpus
   accumulation toward domain-grounded discovery.

The architectural argument about regimes, routing, and separate learners now
serves the conditions thesis rather than defining the main target. AlphaZero
reused one general algorithm and architecture in separately trained chess,
shogi, and Go instances, but human designers supplied each game's rules,
interfaces, reward, and experimental boundary. The important point is not that
separate models are superior. It is that autonomous discovery took place only
inside a richly constituted problem, and generality of method did not erase
those conditions.

The working title *have we learnt the bitter lesson?* is deliberately
interrogative. The article can no longer claim simply to replace Sutton's lesson
with a better one; the research suggests instead that Sutton's own claim is
often sound, while its level of generality and its enabling conditions are easy
to misidentify. The title also distinguishes this piece from existing “Sweet
Lesson” and “Better Lessons” responses.

## Open work

- State the fixed-feedback dilemma as a conceptual test. Use current systems
  only as bounded illustrations: verifier-grounded stages show the positive
  possibility, while recurrent human input in assistant pipelines motivates the
  criticism without proving a field-wide causal diagnosis.
- Preserve the epistemic-provenance rule for process supervision: learner-
  internal value and credit inference is permitted, while a separately imposed
  human semantic process target is excluded.
- Preserve the distinction between historical influence and conceptual
  articulation. Present the limited direct-reception finding once, then use
  Sutton as the article's analytical lens rather than turning the article into
  a reception history.
- Define David's novelty relative not only to Whiteson's 2019 “Sweet Lesson”
  and Aryandoust and Liang's 2025 “Better Lessons,” but also to Sutton and
  Silver's 2025 “Era of Experience.” The current candidate is the claim that
  experience relocates rather than eliminates dependence on prior human
  knowledge, because the conditions of experience constitute and limit the
  learnable problem.
- Use the named reception cases only to show that the connection to LLM
  development is real and plural; no field-wide causal or consensus claim is
  required by the article's conditional consistency test.
- Explain why the public “Sutton recanted” reaction is wrong at the level of
  principle but intelligible at the level of scope: his later critique expands
  *human knowledge* from hand-designed method content to human-produced
  training content.
- Develop exact criteria separating static inherited data, self-generated but
  ungrounded synthetic data, episodic execution feedback, and persistent
  consequence-grounded learning.
- Define the proposed “encapsulation” threshold: which combination of state and
  action representation, transition or generator, objective, verifier, and task
  distribution is sufficient to make a domain self-generating for learning.
- Distinguish domain decomposition from topical specialization. Test which
  candidate domains are genuinely verifiable, partially grounded, or remain
  open-world, and how routing and cross-domain transfer should work.
- Decide how explicitly to invoke *paradigm*. David uses it in the
  rule-constituting sense: the domain establishes admissible entities,
  questions, moves, evidence, and standards of success. The article must retain
  that meaning without importing unneeded claims about scientific communities,
  historical revolutions, or incommensurability.
- Keep paradigm recognition and revision outside the current hypothesis. They
  may be named as limitations or future questions, but the article should not
  imply that David has proposed a mechanism for them.
- Develop an operational distinction among (a) task constitution, (b) outcome-
  grounded feedback that is terminal, inferred across trials, or attached to an
  independently completed subproblem, (c) policy-specifying supervision
  that adds desired answers, behavior, routes, or semantic step rankings, and
  (d) general meta-methods. Test current post-training methods for provenance of
  credit, proxy validity, and independent human or model judgment of method
  quality.
- Test the proposed locus-of-learning criterion across representative post-
  training pipelines. For each new failure, identify who must formulate the
  task-specific explanation and correction; whether engineers supply only
  outcomes or also method knowledge; and whether improvement could continue if
  human method diagnosis stopped while outcome evidence continued.
- Develop the conditions-of-success section around concrete contrasts:
  AlphaZero's complete formal environment, mathematical proof verifiers,
  coding execution feedback, and open-ended domains with delayed, plural, or
  unsafe-to-obtain consequences.
- Test the four-way distinction among task constitution, outcome-grounded
  evaluation, policy-specifying intervention, and learnable meta-methods. It
  must explain difficult boundary cases rather than merely rename them.
- Decide whether the job-discrimination analogy belongs in the eventual article.
  If retained beyond a structural comparison, research the relevant legal and
  philosophical distinctions before using employment-law language.
- Only after those decisions, create a body-first article plan in `manuscript/`;
  do not draft publication prose from the raw research record.
