# Othello-GPT Deep Research

**Status:** focused working research artifact; not publication prose
**Checked:** 4 August 2026
**Scope:** Othello-GPT and directly relevant follow-up work. This file does not
cover the neighboring Sutton/reception article.

## Executive finding

Othello-GPT is strong evidence that autoregressive sequence training can induce
an internal representation organized by a domain rather than merely by its
surface notation. It is not evidence from ordinary natural-language training,
and it does not establish that a transformer learns a complete, unified, or
generally applicable world model.

The original model is a small GPT-style transformer trained from scratch on
sequences of legal Othello moves. It receives neither a board nor the rules. On
synthetic games generated through random legal play, its top predicted
move is legal 99.99 percent of the time. Board occupancy can be decoded from
its hidden activations, and editing those activations changes its move
predictions as the counterfactual board requires. A follow-up finds that the
state is most cleanly represented as `Mine` / `Yours` / `Empty`, relative to the
current player, rather than as absolute black / white occupancy. Those
player-relative variables are almost perfectly linearly decodable and can be
used to steer the model through vector addition.

This evidence exceeds behavioral approximation. The model contains
field-corresponding variables that causally affect its output. It nevertheless
falls short of proving one comprehensive internal rule engine. Later analysis
finds several complementary features and circuits; late in a game, the model
can sometimes identify legal moves before a complete board state is
decodable. State-abstraction research also shows that the Othello task does not
cleanly distinguish a complete world model from a task-sufficient predictive
state, because predicting legal moves already requires most of the board.

For this article, the safest formulation is:

> Othello-GPT shows that sequence prediction can induce causally effective,
> task-relative internal variables whose organization reflects the represented
> field rather than the surface token sequence. It does not show that ordinary
> LLMs reliably learn complete field models across open or interacting domains.

The example is especially valuable because it is not tool calling. During
ordinary inference, no Othello engine reconstructs the board or supplies legal
moves. The rules enter through the distribution that generated the training
sequences. Probes and interventions are research instruments used after
training to inspect the model, not solvers called by the model.

## 1. The experimental question

A move transcript such as `F5 F6 E6 ...` is a one-dimensional token sequence.
The process that generates valid continuations is not one-dimensional. It
depends on an evolving 8-by-8 board, whose pieces change after every move, and
on legality conditions defined over horizontal, vertical, and diagonal
relations.

The experiment asks what an autoregressive transformer must learn when it sees
only the transcript and is trained to predict the next move:

1. Does it memorize familiar continuations or local token correlations?
2. Does it maintain information corresponding to the latent board state?
3. Is that information merely readable by an external classifier, or does the
   model use it to determine its predictions?
4. Is the learned representation tied to the supplied notation or organized by
   task-relevant field relations?
5. Does it constitute a complete model of Othello, or only the state abstraction
   needed to predict legal moves?

The papers answer these questions with progressively stronger tests. No single
test carries the full conclusion.

## 2. What Othello-GPT is—and is not

Kenneth Li and colleagues introduced Othello-GPT in
[“Emergent World Representations: Exploring a Sequence Model Trained on a
Synthetic Task”](https://openreview.net/forum?id=DeG07_TcZvT), published at
ICLR 2023; the manuscript is also available as
[arXiv:2210.13382](https://arxiv.org/abs/2210.13382).

The model is:

- an eight-layer, eight-head, decoder-only GPT-style transformer;
- equipped with 512-dimensional hidden states;
- randomly initialized and trained from scratch;
- given a 60-token vocabulary, one token for each playable square outside the
  four initially occupied center squares;
- trained autoregressively to predict the next move token from the previous
  move tokens.

The model is not:

- a general-purpose language model;
- pretrained on natural language;
- shown a diagram of the board;
- given row, column, adjacency, or diagonal relations;
- supplied the rules as text or code;
- trained to maximize its probability of winning;
- connected to an Othello engine during inference.

Calling it “GPT” refers to the autoregressive transformer architecture, not to
the use of a pretrained GPT product. The authors’
[public repository](https://github.com/likenneth/othello_world) contains the
training, probing, and intervention code, along with links to datasets and
checkpoints. The published default training setup was computationally
substantial for a small model: the repository reports eight GPUs and about 12
GB of memory per GPU.

## 3. Training data: where the rules enter

The original study compares two corpora.

| Corpus | Contents | Role in the experiment |
|---|---:|---|
| Championship | 7,605 plus 132,921 human games, split 80/20 | Contains strategy, opening conventions, and uneven move preferences. |
| Synthetic | 20 million training games and 3,796,010 validation games | Legal moves are otherwise random; leaves are uniformly sampled from the legal game tree. |

The synthetic corpus is decisive. Human games permit a surface explanation:
the model may learn conventional openings, strategies, and move preferences.
Random legal games remove strategic intent. Under the generator’s policy, the
next-token distribution has the legal-move set as a strict support constraint,
not the preferences of a strong human player. The authors describe the corpus
as uniformly sampled leaves of the legal game tree; this should not be
misstated as necessarily uniform choice among the available moves at every
position.

The model is therefore not trained “without rules” in the sense of receiving
rule-free evidence. The rules govern which sequences occur. It is trained
without an explicit representation of the rules or board. The distinction is:

`explicit rule/state supervision` versus `sequence data generated under the rules`.

This is a concrete instance of field-governed data inducing a latent
field-relative representation. It is not evidence that structure can be
identified from arbitrary text lacking sufficient constraints.

## 4. The evidence ladder

### 4.1 Behavioral competence

On held-out games, the authors count an error when the model’s top prediction
is illegal. The synthetic model’s error rate is 0.01 percent; the championship
model’s is 5.17 percent; an untrained model’s is 93.29 percent.

This establishes extremely accurate legal-move prediction on the validation
distribution. It does not by itself reveal the mechanism. A model can behave
correctly through memorization, shortcuts, state tracking, or a mixture.

The legality metric is also narrower than exact next-token accuracy. In a
randomly generated game, several moves may be legal; any legal top prediction
counts as correct even if it differs from the sampled continuation. This is
appropriate for testing whether the model has identified the legal set, but it
does not test strategy or winning play.

### 4.2 Generalization beyond complete transcript memorization

The authors construct a second 20-million-game corpus that excludes every game
beginning with `C5`, one of the four possible first moves. They then test on
sequences from that omitted branch. The model still has a 0.02 percent illegal
top-move rate.

This is strong evidence against lookup of complete training transcripts: those
test sequences never occurred in training. It does not eliminate all shortcut
accounts. The four openings are symmetric, and equivalent or closely related
board states can sometimes be reached through other histories. The experiment
supports structural generalization, but it is not a proof that every learned
component implements the Othello rules.

### 4.3 Decodable board state

Li et al. freeze the trained model and train separate probes to infer the state
of every square from its hidden activations. A linear probe using the human-
obvious classes `Black` / `White` / `Empty` performs poorly: its error remains
roughly 20–23 percent in the synthetic model. A two-layer nonlinear probe
reaches 1.7 percent error near layer 7, compared with roughly 25–26 percent for
the same nonlinear probe on a randomized network.

This shows that the trained activations contain board-state information in a
form a nonlinear classifier can recover. It does not yet show that the model
uses this information. An expressive probe can sometimes calculate a target
from information distributed in the representation rather than extract a
variable the original model itself relies on.

### 4.4 Causal intervention

The original study next edits the model’s activations. Starting from an
ordinary move prefix, the researchers use the nonlinear probe’s gradients to
make one square register as a different state. They intervene from a selected
layer through the remaining layers, then compare the model’s new predictions
with the legal moves on the counterfactual board.

The benchmark contains 1,000 reachable counterfactual boards and 1,000 boards
that cannot arise through legal play. With intervention beginning at layer 4
and continuing across five layers, the average false-positive-plus-false-
negative error is:

| Benchmark | No effective state change | Probe-guided intervention |
|---|---:|---:|
| Reachable boards | 2.68 | 0.12 |
| Unreachable boards | 2.59 | 0.06 |

The intervention changes the output in the direction predicted by the altered
board, including for board configurations outside the training distribution.
This is the strongest evidence in the original paper. The decoded state is not
merely correlated with output: changing it changes which moves the model treats
as legal.

The unreachable-board result must be described precisely. The model is not
shown an impossible move transcript and asked to generalize. Researchers edit
its hidden activations so the probe reports an unreachable board. The resulting
behavior supports counterfactual causal use of the state variables, while also
raising an off-manifold concern: multi-layer gradient edits may create
activation patterns unlike those produced naturally by the model.

## 5. The representation is task-relative, not the first human ontology

Neel Nanda, Andrew Lee, and Martin Wattenberg revisit the same synthetic model
in [“Emergent Linear Representations in World Models of Self-Supervised
Sequence Models”](https://aclanthology.org/2023.blackboxnlp-1.2/), published in
the 2023 BlackboxNLP workshop proceedings.

Their central correction is representational. A legal move does not depend on
the permanent labels black and white; it depends on which pieces belong to the
player whose turn it is. When the probe predicts `Mine` / `Yours` / `Empty`, the
board becomes almost perfectly linearly decodable.

| Probe target | Representative result |
|---|---:|
| Probabilistic tile baseline | 61.8% accuracy |
| Linear `Black` / `White` / `Empty` | about 75% |
| Nonlinear `Black` / `White` / `Empty` | up to 98.7% |
| Linear `Mine` / `Yours` / `Empty` | up to 99.6% at layer 7 |

The result matters for more than probe simplicity. It shows that the first
human description of a field need not be the one the model adopts. The
player-relative encoding is closer to the invariant structure needed for the
task: each turn exchanges `Mine` and `Yours`, while legality continues to be
computed in the same relational terms.

The follow-up also replaces the original multi-step gradient edit with simple
vector addition. Adding the relevant linear direction changes a square toward
`Mine`, `Yours`, or `Empty` and steers the predicted legal moves. Average error
is 0.10 for color-flipping and 0.02 for erasing a piece, compared with null
baselines of about 2.72–2.73. This makes the causal interpretation more direct,
although intervention strength and application across layers remain researcher
choices.

An independent 2023 preprint by Dean Hazineh, Zechen Zhang, and Jeffery Chiu,
[“Linear Latent World Models in Simple Transformers”](https://arxiv.org/abs/2310.07582),
reports the same player-relative linear encoding and studies it across smaller
architectures. Even a one-layer, one-head model predicts legal moves about 95
percent of the time and contains linearly decodable board information, but the
authors do not find that the shallowest model uses that information causally in
the same way. Four-layer and eight-layer models provide stronger causal
effects. This separates `information can be decoded` from `the model relies on
that information`.

## 6. The model does not use one complete mechanism on every move

The Nanda follow-up finds a linearly decodable `Flipped` feature, identifying
which pieces changed ownership at the current step. Its F1 score reaches 97.13
percent at layer 6. Removing the `Flipped` direction changes subsequent move
prediction in the expected direction, reducing average intervention error from
1.686 to 0.486.

The authors also find evidence for multiple circuits:

- the model rapidly determines which squares are nonempty;
- some attention heads preferentially track the current player’s or opponent’s
  historical moves;
- board-state and move predictions improve iteratively across layers;
- after about move 30, legal moves are sometimes decodable before the complete
  board state is;
- late-game board-probe accuracy declines, yet board-state intervention still
  has a strong causal effect: error 0.112 against a 1.988 null baseline.

The safest interpretation is not that the board representation disappears,
nor that it alone explains every prediction. Othello-GPT appears to combine a
causally used board representation with other task-relative shortcuts or
partial computations. As the legal game tree contracts late in play, a full
reconstruction may not always be needed before some legal moves can be
identified.

This corrects a simple architectural analogy. “A representation appropriate to
the field” need not mean one module, one ontology, or one algorithm per field.
It may mean a coordinated family of state variables and circuits whose use
depends on the subtask and position.

## 7. What should count as a “world model”?

The literature uses “world model” for several different evidential standards.
The following ladder keeps the claims separate:

1. **Behavioral legality:** the model normally outputs a valid continuation.
2. **History-general predictive state:** it generalizes to unseen sequences by
   maintaining information sufficient for continuation.
3. **Decodable field state:** an external probe can recover domain variables
   from hidden activations.
4. **Causally used field state:** intervening on those variables changes output
   as the counterfactual state predicts.
5. **Transition-complete field model:** the model represents the relevant state
   and dynamics broadly enough to simulate interventions, future transitions,
   and tasks not reducible to its training objective.

Othello-GPT clearly reaches levels 1–3 and provides strong evidence for level
4. It provides partial evidence, but not a decisive demonstration, for level 5.

Zichao Li, Yanshuai Cao, and Jackie Cheung sharpen this distinction in
[“Do LLMs Build World Representations? Probing Through the Lens of State
Abstraction”](https://proceedings.neurips.cc/paper_files/paper/2024/hash/b1b16c4b875eb84d3585cb70d23970ca-Abstract-Conference.html),
published at NeurIPS 2024. A model may encode:

- a general state abstraction that preserves transition dynamics and supports
  future-state prediction;
- a value-sensitive abstraction sufficient to compare possible actions; or
- a policy-level abstraction sufficient to choose the task’s action.

These levels are difficult to separate in Othello. The set of legal moves
already reveals much of the board, so the complete board and the coarsest state
needed for legal-move prediction are unusually close. High board-state probe
accuracy can therefore arise because the board is task-necessary, not because
the model learned a general simulator that preserves every aspect of the game
for every possible purpose.

For this article, `causally effective task-relative field representation` is
more precise than an unrestricted `world model`. The narrower phrase preserves
what the experiments establish without deciding a philosophical definition by
terminology.

## 8. Methodological objections and their force

### Objection 1: Legal play could be memorized

The omitted-opening experiment rejects complete transcript lookup, and the
random legal corpus removes human strategy as the main source of predictability.
Memorized openings, symmetry, local correlations, and other shortcuts may still
contribute. The multiple-circuit evidence says they probably do. The causal
board interventions show that shortcut use is not the whole explanation.

**Verdict:** serious against a pure-behavioral argument; insufficient against
the combined behavioral, probing, and intervention evidence.

### Objection 2: A probe can learn the board itself

This is a standard problem in representation research. John Hewitt and Percy
Liang’s [control-task analysis](https://aclanthology.org/D19-1275/) shows that an
expressive probe may memorize a target rather than reveal what the original
representation makes accessible. Tiago Pimentel and colleagues’
[Pareto Probing](https://aclanthology.org/2020.emnlp-main.254/) argues that probe
accuracy must be interpreted alongside probe complexity.

The original nonlinear probe is therefore suggestive but not decisive. The
player-relative linear probe is substantially stronger: it is simple, nearly
perfect, and its directions steer model behavior. Causal use does not make the
probe ontology exhaustive, but it shows the discovered directions are more
than an arbitrary decoder’s reconstruction.

**Verdict:** weakens the original nonlinear-decoding claim; largely answered
for the narrower player-relative variables by linearity plus intervention.

### Objection 3: Researchers imposed the ontology

Both the board probe and `Mine` / `Yours` / `Empty` labels are proposed by
humans. Failure to find a variable may reflect a bad probe target; success shows
that the proposed relation is available, not that no other representation
exists. The change from absolute colors to player-relative roles demonstrates
this danger directly.

**Verdict:** decisive against claims of a complete mechanistic account;
compatible with the positive claim that these task-relative variables exist
and are causally used.

### Objection 4: Interventions may leave the model’s natural activation manifold

The original experiment edits several layers through gradient descent. A
successful output shift could reflect a powerful external manipulation rather
than a naturally traversed internal computation. Simple linear vector
interventions reduce the concern but do not remove it: scale, layer choice, and
simultaneous editing remain experimental decisions.

The strongest future tests would use minimal localized interventions, causal
mediation, activation patching from naturally occurring matched states, and
controls for generic logit disruption.

**Verdict:** limits how literally the edit should be understood; does not erase
the highly structured correspondence between the edited state and the changed
legal-move set.

### Objection 5: Othello is too easy and artificial

Othello is deterministic, fully observable, compact, stationary, and governed
by exact rules. The training corpus is enormous and densely samples legal
behavior. Natural language and humanities fields have disputed ontologies,
partial observation, changing contexts, multiple purposes, and sparse or noisy
feedback.

These are reasons Othello cannot establish the article’s general thesis. They
are also what makes the experiment diagnostic: the latent state is known, the
surface representation is controlled, and interventions have unambiguous
consequences.

**Verdict:** decisive scope limit, not a defect in the proof of principle.

### Objection 6: This is still only learning correlations from tokens

All learned models exploit statistical dependence in their training evidence.
The relevant distinction is not statistical versus non-statistical learning.
It is whether the learned computation remains at the level of surface
continuations or constructs internal variables that track and causally support
the data-generating field.

Othello-GPT provides positive evidence for the latter. It does not show that
the representation is independent of evidence, only that it is structurally
distinct from the evidence’s surface notation.

**Verdict:** the objection dissolves if the article avoids claiming
evidence-independent semantics.

## 9. Newer evidence directly relevant to the article’s extension

### 9.1 Syntax invariance and multiple rule systems: MetaOthello

Aviral Chawla, Galen Hall, and Juniper Lovato’s February 2026 preprint,
[“MetaOthello: A Controlled Study of Multiple World Models in
Transformers”](https://arxiv.org/abs/2602.23164), performs two experiments very
close to those proposed in this project.

First, it trains a model on two isomorphic Othello games with different token-
to-square mappings. Raw probe directions differ, but after orthogonal alignment
their similarity reaches 0.98. A single learned rotation applied to hidden
activations transfers Classic-game states into the scrambled-token game and
recovers near-perfect corresponding predictions across most layers. This is
strong controlled evidence that the representation is not identical with one
surface encoding.

Second, it mixes pairs of Othello variants whose rules differ. The model does
not simply create wholly isolated submodels. It largely shares a board-state
representation, specializes where rules conflict, and constructs a game-
identity signal that routes ambiguous prefixes. Steering the identified
mid-layer circuit changes which rule system governs the prediction. When two
variants diverge more radically, the routing occurs earlier and the model tends
to commit to one interpretation.

This result revises two open questions without closing them:

- **surface invariance:** now directly supported in an isomorphic controlled
  case, but only within one board-game family;
- **multiple field structures:** shared state plus localized routing is a
  plausible alternative to one isolated mechanism per domain, but the study
  tests paired Othello variants, not mathematics, space, argument, and drama in
  one model.

The result is a preprint, not yet treated here as peer-reviewed. Its own limits
are substantial: one eight-layer architecture, pairwise 50/50 mixtures, exact
synthetic rules, and linear-probe-based analysis. All-layer steering may also
over-intervene. It is promising evidence and an experimental template, not a
general solution.

### 9.2 Structured relations beneath linear directions

Andrew Lee, Fernanda Viégas, and Martin Wattenberg’s May 2026 preprint,
[“Tensor Product Representation Probes Reveal Shared Structure Across Linear
Directions”](https://arxiv.org/abs/2605.09967), asks whether 192 separate
square–color directions conceal a more compositional organization. Their probe
factorizes the board readout into square embeddings, color embeddings, and a
binding matrix. With fewer parameters than the independent linear probes, the
structured probe reaches about 99 percent board-state accuracy. Its recovered
square embeddings exhibit board geometry, and its intervention directions can
be composed across several changed squares while preserving the expected move
effects.

This is suggestive for the article’s idea that a field-appropriate
representation should preserve relations, not merely isolated labels. The
authors explicitly do **not** claim that Othello-GPT itself performs tensor
products or natively separates square and color subspaces. The probe shows that
the linear directions admit a structured factorization; the mechanism by which
the model computes that structure remains open.

### 9.3 Breadth across architectures

Yifei Yuan and Anders Søgaard’s 2025 ICLR World Models workshop paper,
[“Revisiting the Othello World Model Hypothesis”](https://arxiv.org/abs/2503.04421),
extends the task across GPT-2, T5, BART, Flan-T5, Mistral, Llama 2, and Qwen 2.5
families and reports up to 99 percent unsupervised grounding accuracy with
similar learned board features. This reduces concern that the phenomenon is
unique to one architecture. Because it is workshop evidence and uses a new
grounding method whose assumptions require separate evaluation, it should
support breadth rather than carry the article’s central causal claim.

Raanan Yehezkel Rohekar and colleagues’ peer-reviewed ICML 2025 paper,
[“A Causal World Model Underlying Next Token Prediction”](https://proceedings.mlr.press/v267/yehezkel-rohekar25a.html),
uses Othello and chess models trained on human games and tests them on random
legal sequences. It reports that a causal-structure confidence score derived
from attention is associated with legal out-of-distribution predictions. This
is additional evidence that legality can generalize beyond human game
distributions, but it uses a different causal account and does not replace the
activation-intervention evidence.

## 10. Relation to the article’s thesis

### Why LLM-like sequence models can work

The Othello transcript carries enough constraints for a transformer to infer a
latent state useful for continuation. High-capacity contextual processing can
therefore do more than match short surface patterns: it can compress a history
into variables corresponding to the process that generated it.

Othello makes the article’s general mechanism concrete. Contextual sequence
learning approximates a field and, under sufficiently constraining data,
internalizes task-relative variables that govern later transformations. The
article proposes the same relationship as an explanation of broad LLM
competence and its uneven limits.

### Where the limit appears

The experiment succeeds under ideal conditions: exact rules, complete
observation, a stable state space, dense legal data, and one narrow objective.
Even here, late-game predictions use several circuits and do not always wait
for a perfectly decoded board. In open or intertwined fields, the model must
also infer which representation is active, resolve ambiguity, preserve several
states, and validate transitions at their interfaces.

Othello therefore illustrates both the possibility and the limit. A field-
corresponding state can emerge, but its completeness, causal role, and
generalization are task- and distribution-dependent.

### How models might be improved

Othello supports two routes rather than only one:

1. **Induced representation:** train on data or interaction whose valid
   continuation makes the latent field state necessary.
2. **Explicit semantic supervision:** directly teach, predict, revise, or
   validate the field state and its permissible transformations.

The first route produced the Othello board representation without board-state
labels. The second may be needed where data underdetermines the desired
structure, where shortcuts permit acceptable training performance, or where
the field’s state is too difficult to infer reliably from surface sequences.

The desired system need not attach one solver to every field. It may learn
shared representational components, domain-specific transformations, and
contextual routing, as MetaOthello tentatively suggests. What must be tested is
whether the internal operations preserve the relevant field relations through
semantic change.

## 11. Why this is not tool calling

Tool calling would proceed as follows:

`move transcript -> classify as Othello -> external engine computes board and legal moves -> return token`.

Othello-GPT instead proceeds as:

`move transcript -> model's hidden state tracks task-relative board variables -> model predicts token`.

No external engine participates in ordinary prediction. The synthetic game
generator is used to create training and evaluation data. The probes are fitted
after training to inspect activations. The intervention code is used by
researchers to test causality. None is a solver selected by the model at
inference time.

This makes Othello-GPT evidence for internal learning. A tool-augmented system
could still be better in practice, and a tool could verify the model’s state,
but that would be an additional architecture rather than the phenomenon the
experiment demonstrates.

## 12. Claims safe and unsafe for the draft

### Safe claims

- Othello-GPT learned to predict legal moves from move sequences without being
  given the board geometry or rules explicitly.
- Random legal training data sharply limits strategy imitation as an
  explanation of its performance.
- Its hidden activations contain nearly linearly decodable player-relative
  board-state variables.
- Intervening on those variables changes predictions in accordance with the
  counterfactual board.
- The learned categories are task-relative and need not mirror the surface
  notation or the first human ontology proposed by investigators.
- The same model appears to combine multiple causally relevant features and
  circuits rather than one exhaustive board algorithm.
- Recent controlled preprint evidence supports invariance across a permuted
  token scheme and shared representation plus routing across Othello rule
  variants.

### Unsafe or overstated claims

- Othello-GPT was taught the rules and then reasoned from them.
- Othello-GPT is a general LLM or evidence about all mechanisms in deployed
  chat models.
- Legal-move accuracy alone proves a world model.
- The probes reveal the model’s one true or complete ontology.
- The model contains a single explicit Othello rulebook.
- The unreachable-board experiment shows ordinary behavioral generalization
  from impossible input transcripts.
- Othello establishes that transformers can already coordinate mathematics,
  space, philosophy, and drama through independent domain representations.
- The tensor-product probe proves that Othello-GPT literally computes tensor
  products.

## 13. Experimental program suggested by the case

### A. Surface-encoding invariance

Train equivalent tasks under multiple coordinate permutations and genuinely
different notations. Compare latent states after aligning only on known field
equivalences. Test whether causal interventions transfer, not merely whether
probe accuracy remains high. MetaOthello now supplies an initial positive
result and a reusable design.

### B. Full state versus task-sufficient abstraction

Train several objectives on the same domain: legal-move prediction, future
board prediction, counterfactual update, explanation, and winning strategy.
Probe which state and transition information survives each objective. This
separates a general dynamics model from the minimum predictive state.

### C. Explicit versus induced semantic representation

Match architecture, data volume, compute, and output objective across:

1. sequence-only training;
2. auxiliary board-state prediction;
3. explicit transition supervision;
4. intervention or consistency losses;
5. executable validation during training.

Measure legality, state fidelity, intervention fidelity, depth robustness, and
out-of-distribution transfer. This directly tests whether explicit semantic
training adds value beyond field-governed sequence data.

### D. Shortcut pressure

Vary whether training data permits surface shortcuts. Compare random legal
games, strategic games, biased openings, sparse state coverage, and adversarial
surface correlations. Test whether semantic supervision prevents the model
from abandoning field state when shortcuts become available.

### E. Multiple domains and interfaces

Begin with several formal fields that have distinct state and transition
structures, not merely variants of one board game. Require tasks that cross
their boundaries. Measure:

- contextual selection of the correct representation;
- representational interference;
- shared versus specialized components;
- causal routing;
- preservation of each field’s invariants;
- validity at the conversion point between fields.

Only after this controlled stage should the design be extended to argument,
law, drama, or other domains with plural and revisable structural judgments.

### F. Reasoning depth and state fidelity

At each step in a long chain, decode or otherwise estimate the field state and
test its invariants. Separate initial interpretation error from transition
error, and determine whether drift accumulates even when the final answer
happens to be correct. This operationalizes the article’s “how on earth did it
get there?” concern.

## 14. Recommended role in the article

Othello-GPT should appear after the article has stated the problem of
linguistic transformations losing field validity. Its role is not to open the
article as a familiar hook. It should supply the first positive technical
answer:

1. a surface sequence can be generated by a richer field state;
2. next-token training can induce a causally effective internal correlate of
   that state;
3. the useful representation may be relational and task-relative rather than a
   copy of notation;
4. this is the kind of internal learning the proposed program seeks to make
   reliable across fields;
5. the article generalizes from this clear case to fields whose representations
   and transition constraints are more difficult to learn and preserve.

Othello-GPT should be presented as the clearest technical instance of the
article's mechanism. The separate question of whether it contains a complete
general-purpose “world model” need not govern the article's thesis.

The qualifications in this research file constrain what may be attributed to
each source. They are not instructions to recast the author's general mechanism
as a tentative thesis or to rehearse source limitations throughout the article.

## 15. Source register

| Source | Status | Use here |
|---|---|---|
| [Li et al., “Emergent World Representations”](https://openreview.net/forum?id=DeG07_TcZvT) | ICLR 2023 conference paper | Original model, datasets, behavior, nonlinear probes, causal interventions. |
| [Original code repository](https://github.com/likenneth/othello_world) | Author-maintained public code and assets | Reproducibility, implementation, datasets, checkpoints. |
| [Nanda, Lee, and Wattenberg, “Emergent Linear Representations”](https://aclanthology.org/2023.blackboxnlp-1.2/) | Peer-reviewed BlackboxNLP 2023 workshop paper | Player-relative linear state, vector steering, flipped features, multiple circuits. |
| [Hazineh, Zhang, and Chiu, “Linear Latent World Models”](https://arxiv.org/abs/2310.07582) | 2023 preprint | Independent parallel linear result, architecture-depth and causal-use distinctions. |
| [Z. Li, Cao, and Cheung, “Do LLMs Build World Representations?”](https://proceedings.neurips.cc/paper_files/paper/2024/hash/b1b16c4b875eb84d3585cb70d23970ca-Abstract-Conference.html) | NeurIPS 2024 conference paper | General versus task-oriented state abstraction; key qualification of “world model.” |
| [Yuan and Søgaard, “Revisiting the Othello World Model Hypothesis”](https://arxiv.org/abs/2503.04421) | ICLR 2025 World Models workshop paper | Cross-architecture breadth; secondary support. |
| [Yehezkel Rohekar et al., “A Causal World Model Underlying Next Token Prediction”](https://proceedings.mlr.press/v267/yehezkel-rohekar25a.html) | ICML 2025 conference paper | OOD legality and attention-based causal-structure evidence in Othello and chess. |
| [Chawla, Hall, and Lovato, “MetaOthello”](https://arxiv.org/abs/2602.23164) | February 2026 preprint | Surface-token invariance, shared state, rule-conflict specialization and routing. |
| [Lee, Viégas, and Wattenberg, “Tensor Product Representation Probes”](https://arxiv.org/abs/2605.09967) | May 2026 preprint | Structured factorization beneath linear directions; explicit mechanistic caveat. |
| [Hewitt and Liang, “Designing and Interpreting Probes with Control Tasks”](https://aclanthology.org/D19-1275/) | EMNLP-IJCNLP 2019 conference paper | Probe expressivity and selectivity objection. |
| [Pimentel et al., “Pareto Probing”](https://aclanthology.org/2020.emnlp-main.254/) | EMNLP 2020 conference paper | Probe accuracy–complexity tradeoff. |

## Open questions

1. Which parts of Othello’s transition function are represented and causally
   used, rather than recoverable from a task-sufficient state?
2. Can the model predict counterfactual future boards over several transitions,
   not only adjust the next legal-move set after an activation edit?
3. Do natural activation-patching experiments reproduce the effects of
   gradient and vector steering without off-manifold concerns?
4. Does explicit board-state or transition supervision improve robustness when
   training data contains strong surface shortcuts?
5. Does the 2026 syntax-invariance result replicate across architectures,
   imbalanced mixtures, many simultaneous rule systems, and non-isomorphic
   notations?
6. How should shared state, specialized transformations, and routing be divided
   when domains overlap only partially?
7. What is the nearest soft-domain analogue of a board state for which causal
   fidelity, not merely interpretive plausibility, can be tested?
8. Which evidence would distinguish a genuinely general field model from a
   collection of predictive states sufficient for the trained tasks?
