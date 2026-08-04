# Logical Tree and Article Order

Status: provisional control outline, not publication prose.

## Governing thesis

LLMs often succeed because context and training let their outputs approximate
field-specific semantic structures. Whether they learn those structures or
track them through other learned regularities remains domain-dependent and
empirically open. They become unreliable when linguistic transformations cease
to track field-valid transitions. Training that makes field representations and
transition constraints more causally effective—and coordinates different
representations for different tasks and fields—may improve reliability and
discovery.

## 1. Representational foundation

1.1. Language can represent field-specific states and relations, including
structures that are partly constituted by language.

1.2. `e_(D,c)` relates a linguistic expression, its context, and one or more
states in a field-specific semantic space `R_D`.

1.3. The interpretation may be partial, many-to-many, probabilistic, or
contested.

1.4. `T_(D,c)` specifies admissible transitions between states in `R_D`.

1.5. Transition validity is conditional on an adequate initial
interpretation. Valid inference within a false or incomplete representation
need not remain faithful to the world.

1.6. Field-valid reasoning follows transitions licensed by `T_(D,c)`.

1.7. Linguistic well-formedness does not establish field validity.

**Relation:** 1.1–1.7 define representation adequacy and transformation
fidelity as distinct requirements.

## 2. Why LLMs work

2.1. Context can indicate the active field, the relevant use of language, and
the interpretation connecting language with field structure.

2.2. Scale and varied training can support approximate interpretations across
many fields and uses of language.

2.3. Othello-GPT supplies a positive proof of principle: training on move-token
sequences produces causally effective internal variables for board state even
though the board and its rules are never supplied directly.

2.4. The internal variables are organized as task-relative field relations—
mine, yours, empty, and flipped—rather than merely reproducing the input tokens
or the human-default black–white description.

2.5. MetaOthello extends this mechanism: equivalent tasks under permuted
surface tokens yield aligned, causally transferable internal states, while
paired rule variants share state structure and specialize where their rules
conflict.

2.6. Field-tracking behavior can arise from a stable internal field
representation, contextual approximation through other learned regularities,
or a mixture of both.

2.7. Broad, uneven LLM competence results from contextual approximation rather
than uniformly learned field structure.

**Relation:** 1.1–1.7 and 2.1–2.4 establish the possibility of field-appropriate
internal representation; 2.5 extends the mechanism across notation and related
rule systems; 2.6 preserves the mechanistic alternatives; 2.7 states the
article's central explanation.

## 3. Where LLMs reach their limits

3.1. Base language-model pretraining rewards probable token continuation;
post-training adds instruction-following and preference objectives.

3.2. These objectives can induce field representations or proxy behaviors
without directly requiring reliable compliance with every field's transition
constraints.

3.3. When performance depends on proxy approximation, structural complexity
weakens the language–field correlation.

3.4. It predicts that transformation depth accumulates local approximation
errors.

3.5. Linguistic coherence may persist while field fidelity declines.

3.6. Endpoint correctness does not establish path validity.

3.7. A generated rationale does not establish the model's actual
transformation path.

3.8. Claims about internal path validity require explicit semantic
trajectories or causal evidence that intermediate states govern later
transformations.

**Relation:** 1.7 and 3.1–3.4 yield the proxy-drift explanation; 3.5–3.8 state
its consequences for output and path evaluation.

## 4. How to improve LLMs

4.1. Training should make field-appropriate state formation and transformation
causally useful for the task rather than rewarding surface continuation alone.

4.2. Explicit semantic targets can impose this pressure; field-governed data or
interaction can also induce the representation when shortcuts are unavailable.

4.3. Field representations may be supplied, learned, or jointly revised; they
need not reproduce a single human-designed ontology or surface notation.

4.4. The desired generalization is a repertoire of domain- and task-appropriate
internal representations and mechanisms, selected and coordinated through
context.

4.5. A system should infer the active representation, transform or validate
its semantic state, and render the result linguistically.

4.6. Field-representation learning changes the constraints governing the
model's inference whether the representation is supervised or emergent.

4.7. Tool calling delegates an operation to an external executor. Hybrid
systems may combine internal semantic training with external execution or
verification.

**Relation:** 3.1–3.8 motivate 4.1–4.5; 4.6 and 4.7 define separable
interventions; 2.3–2.5 establish internal field representation, notation
invariance, and coordination among related rule systems.

## 5. Domain scope and teaching constraint

5.1. Formal fields specify states and transitions explicitly.

5.2. Structured empirical fields represent uncertain states and probabilistic
transitions.

5.3. Interpretive fields admit plural, contextual families of defensible
transitions.

5.4. Hybrid tasks may require several simultaneous representations and
explicit constraints at their interfaces.

5.5. One field may recruit several complementary mechanisms; field
appropriateness does not imply one representation per domain.

5.6. A field syntax remains substantive only when it excludes some
transformations.

5.7. Learnability depends on the field's capacity to represent, demonstrate,
or evaluate its structural distinctions.

**Relation:** 5.1–5.7 specify the scope and teaching conditions of 4.1–4.5.

## 6. Empirical predictions

6.1. Field fidelity should decline faster than linguistic quality as structural
complexity and transformation depth increase.

6.2. Field-aligned training should reduce that decline relative to text-only
training matched for data, compute, capacity, and search.

6.3. Outcome-only evaluation should count some correct answers reached through
field-invalid paths.

6.4. Hybrid-task errors should cluster at field selection, field switching, and
representation interfaces.

6.5. Weakening the field-defining anchor should increase drift toward generic
linguistic plausibility.

6.6. Field-aligned training should improve reasoning without tool access;
tools may provide an additional gain.

6.7. The central diagnosis gains support only if its predictions distinguish
representational drift from search, memory, compute, and initial-interpretation
failures.

6.8. Causal interventions should distinguish a field representation that
governs output from a decodable correlate or a context-bound proxy.

6.9. Equivalent surface encodings of the same field should induce structurally
aligned internal states if the model has learned the field rather than one
notation's correlations.

6.10. Multi-domain training should produce separable but composable internal
mechanisms, with errors measurable at selection and interface points.

**Relation:** 6.1–6.10 independently test the diagnosis, mechanism, remedy, and tool
distinction.

## 7. Innovation and latent-structure discovery

7.1. Field syntax can license a valid transition without linguistic precedent.

7.2. Search explores licensed transitions.

7.3. A field-sensitive value criterion ranks their significance.

7.4. Semantic representation, field syntax, search, and value may jointly
produce novel, valid, nontrivial inferences.

7.5. Object-level discovery finds new paths within an accepted representation
and transition syntax.

7.6. Representation-level discovery proposes a new or revised representation,
transition syntax, or value criterion.

7.7. Representation-level proposals cannot validate themselves. Their
consequences require independent tests and comparison with rivals.

7.8. Novelty requires comparison with training data, retrieval, and available
exemplars; validity and value require independent domain tests.

7.9. Results produced by an LLM, search procedure, and evaluator establish
system-level innovation unless the LLM's independent contribution is isolated.

**Relation:** 4.1–4.4 and 7.1–7.3 support 7.4; 7.5–7.9 distinguish two kinds of
discovery and their evidential burdens.

## 8. Testing sequence

8.1. A formal-domain experiment independently varies initial representation
quality, structural complexity, transformation depth, and tool access.

8.2. The experiment compares text-only and field-aligned training under
matched data, compute, capacity, and search.

8.3. It records linguistic quality, state fidelity, transition validity,
terminal accuracy, first-invalid-step depth, and causal sensitivity to
interventions on candidate field states.

8.4. An encoding-invariance test repeats one field under permuted or otherwise
equivalent surface notations and compares the learned internal structure.

8.5. A multi-domain extension tests representation selection, interference,
composition, and interface validity.

8.6. Weather forecasting tests high-dimensional learned regularities against
held-out or prospective trajectories, probabilistic scores, regime variation,
and physical consistency.

8.7. Philosophy or drama tests transformations against several predeclared,
defensible structural analyses.

8.8. A discovery experiment freezes a model-proposed structure and validates
its predictions on independent random or stratified samples.

8.9. The central thesis gains support if surface–fidelity dissociation survives
the alternative explanations in 3.6 and field-aligned training reduces it.

8.10. The innovation hypothesis additionally requires novel, valid, and
nontrivial domain results.

**Relation:** 8.1–8.8 test increasingly general forms of the thesis; 8.9 and
8.10 define separate standards of support.

## Core dependency

`contextual interpretation -> field representation -> valid transition ->
proxy drift under complexity or depth -> field-aligned training -> controlled
test -> possible object-level or representation-level discovery`

The Sutton/reception article remains outside this structure.
