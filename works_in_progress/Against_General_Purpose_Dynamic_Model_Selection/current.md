# Against General-Purpose Dynamic Model Selection

## Executive Summary

A model-selection system predicts which model, reasoning level, or configuration will meet a task’s requirements at an acceptable cost. That is an empirical claim. It should be supported by comparative trials on representative work, evaluated by criteria that can distinguish the failures that matter. For runtime selection, the evidence must also connect an observed workflow state to the expected effect of a particular intervention.

Current systems use capability rules, task categories, preference data, benchmark results, historical outcomes, uncertainty estimates, and prompt-based quality predictions. Learned routers and cascades have reduced cost while preserving measured quality on bounded evaluation sets. Commercial routers make similar predictions and expose cost-quality controls. These results establish that routing can work on defined, repeated workloads. They do not establish a general ability to select models for heterogeneous, open-ended work. Router performance depends on its supervision, definition of quality, task distribution, and candidate models; recent evaluations continue to find fragile decisions and strong simple baselines.

Broad generalization is difficult because models differ across knowledge, reasoning, instruction following, context use, specialization, tools, latency, and price. Tasks require different combinations of those capacities, while open-ended quality may involve accuracy, completeness, source integrity, constraint preservation, and user preference. A generic estimate of task difficulty cannot identify the decisive resource.

Workflow integration supplies information that appears during execution, such as errors, retrieved evidence, and intermediate artifacts. It improves selection only when a validated rule relates those observations to comparative outcomes. Cascading introduces a further risk: a failed attempt establishes inadequacy, but not its cause. Retrieval, a different tool, clearer constraints, better decomposition, or human judgment may be more useful than a stronger model. Escalation can otherwise reinforce the original framing and return the same error with greater fluency and cost.

General-purpose systems should therefore allocate models in advance under an explicit policy and reserve dynamic selection for workloads where representative evidence shows a net benefit after routing costs are counted. Verification should remain separate. It can establish that work failed without presuming which model or intervention should follow.

## The Question Is Empirical

A model-selection system chooses which model, reasoning level, or configuration should handle a task. The choice may be made once, before execution, or revised as a workflow develops. Either way, the system makes a prediction: this allocation will produce a better result, or a sufficiently good result at lower cost, than the available alternatives.

That prediction needs evidence.

For a defined class of tasks, the relevant question is:

> What evidence shows that one allocation is more likely than another to meet the required standard at an acceptable cost?

This is a comparative question. It cannot be answered by showing that a model is capable, that a task looks difficult, or that a later attempt succeeded. The system needs some basis for estimating how the alternatives would perform on the same kind of work.

The standard also depends on the purpose. A support chatbot may optimize acceptance rate and latency. A coding system may use tests. A research workflow may care about source quality, factual accuracy, completeness, and constraint preservation. There is no useful definition of “best model” until the required outcome and the value of cost, speed, and risk have been specified.

Dynamic selection has demonstrated value in bounded workloads with repeated tasks and measurable outcomes. The objection is to its use as a general solution before the comparative judgment has been validated.

## What Would Count as Evidence?

The clearest evidence would come from repeated comparisons on representative tasks. Candidate models would attempt the same kinds of work under controlled conditions. Their outputs would be judged by criteria that can detect the failures that matter. The evaluation would use enough cases and repeated samples to distinguish a model effect from ordinary generation variance.

The resulting policy would then need validation on later or held-out work. A router that memorizes the evaluation set has not learned how to allocate new tasks. A policy that works on mathematics may not transfer to legal interpretation, long-form synthesis, or code repair. Model updates, prompt changes, new tools, and altered workflows can make an earlier result stale.

Evidence can be ordered by how directly it bears on the task:

1. **Externally checkable outcomes.** Tests, calculations, schemas, verified citations, and other criteria that do not depend on the model’s own impression.
2. **Stable human or production outcomes.** Expert ratings, acceptance decisions, correction rates, and other observations collected under a defined rubric.
3. **Calibrated predictors trained on those outcomes.** A learned router may generalize beyond recorded cases if its predictions remain accurate on new ones.
4. **Rules or similarity to evaluated cases.** These can be useful baselines when task classes are stable.
5. **Uncalibrated judgment.** Verbal confidence, generic complexity scores, or an LLM’s opinion that a task needs a stronger model.

The last category may still correlate with performance. The problem is that its reliability is unknown until it is tested against one of the stronger forms of evidence.

Runtime selection requires an additional kind of evidence. Suppose a workflow observes a test failure, a missing citation, or a stalled plan. To justify changing models, it needs to know that the proposed model performs better from that state. The failure establishes that the present attempt is inadequate. It does not establish which intervention will help.

## What Current Systems Use

Current model-selection systems draw on several kinds of evidence. They should not be treated as one method.

### Rules and capability gates

The simplest systems route by known requirements. A request needing vision, a large context window, structured output, or a particular tool can be restricted to models that support it. Teams may also assign recurring tasks to models that performed adequately during local evaluation.

These rules are limited, but inspectable. Their claims are modest: this model has the required interface, or this model met the threshold on this task class. They do not require a general theory of prompt difficulty.

### Learned pre-execution routers

Learned routers predict comparative performance from the prompt or a representation of it. RouteLLM, for example, trains routers on preference data showing when a stronger model’s response is preferred to a weaker one. Its published evaluation reported substantial cost reductions on the tested benchmarks while preserving the strong model’s measured quality. The paper also reported transfer when the candidate models changed. Those are meaningful results, but they concern the benchmarks, model pairs, preference data, and evaluation procedure used in the study. [RouteLLM](https://arxiv.org/abs/2406.18665)

Other work trains on answer correctness, uncertainty, or large collections of recorded model outcomes. RouterEval assembled more than 200 million performance records across twelve evaluations and thousands of models, illustrating how much comparative data a serious routing problem can require. Its authors also found considerable room for improvement in existing methods. [RouterEval](https://arxiv.org/abs/2503.10657)

The sophistication of the predictor is not itself evidence of better allocation. A 2025 study found that a well-tuned nearest-neighbour method could match or outperform more complex routers across its evaluation suite. Historical similarity may be enough when model performance is locally consistent, and it is easier to inspect. [When Simple kNN Beats Complex Learned Routers](https://arxiv.org/abs/2505.12601)

### Commercial prompt routers

Amazon Bedrock predicts the response quality of two models from the same family and routes according to a configured quality-difference threshold. The service exposes the selected model and lets the operator choose the trade-off. Amazon also states that the router cannot adapt its decisions from application-specific performance data, may not be optimal for specialized uses, and depends on its initial training data. It recommends evaluating the router on the intended application before production use. [Amazon Bedrock Intelligent Prompt Routing](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-routing.html)

OpenRouter’s Auto Router chooses among a curated pool after analyzing the prompt. It exposes the chosen model and a cost-quality control. It pins a model within a session to preserve consistency and cache use, limiting rerouting during a conversation. Its public documentation describes the factors considered, but does not provide enough evaluation detail to infer reliability for a particular user’s open-ended workload. [OpenRouter Auto Router](https://openrouter.ai/docs/guides/routing/routers/auto-router)

These systems show that general prompt routing is available as a product. Product availability is different from general validation. The operator still has to decide whether the router’s quality prediction corresponds to the outcomes that matter in the application.

### Cascades

A cascade tries one model, evaluates its output, and calls another model when a threshold is not met. FrugalGPT demonstrated large cost reductions on its evaluated datasets by learning combinations of models and escalation rules. This is good evidence for cascades on workloads resembling those tests. [FrugalGPT](https://arxiv.org/abs/2305.05176)

A cascade answers a narrower economic question than a general router. If the first call is cheap, failure is detectable, and the second model reliably performs better on those failures, the expected cost can fall. None of those conditions should be assumed outside the evaluated workload.

## What Has Been Established

The research supports three conclusions.

First, models have complementary performance. A fixed “best” model can be beaten on some benchmark distributions by selecting among candidates. There is genuine value available to a router.

Second, routing can reduce cost while retaining measured quality when the workload is repeated and the supervision is informative. Preference data, correctness labels, calibrated uncertainty, and historical outcomes can all support useful policies.

Third, the success is conditional. The router inherits the definition of quality in its training and evaluation data. A preference score may reward fluency, style, or agreement. An automated judge may reproduce model biases. A benchmark may test short answers while the application requires long-context synthesis and careful omission detection.

Recent evaluations make the limitation concrete. A study of preference-based and commercial routers found efficiency gains alongside fragile, category-driven behavior. One router sent all coding and mathematics prompts to the most powerful model even when smaller models were adequate, while weaker routing on jailbreak prompts introduced safety concerns. [How Robust Are Router-LLMs?](https://arxiv.org/abs/2504.07113)

The field is building larger benchmarks, calibrated uncertainty methods, and techniques for correcting biased preference supervision. Reliable supervision and generalization remain open problems.

Current evidence therefore supports dynamic selection for a defined distribution, not a general faculty that can inspect any task and determine the correct amount or kind of intelligence to apply.

## Why Generalization Is Difficult

Model capability is multidimensional. Models differ in learned knowledge, reasoning behavior, instruction following, context use, domain specialization, tool use, calibration, latency, and price. A reasoning-effort control changes part of that configuration; it does not supply missing knowledge or grant access to a tool.

Tasks also demand different combinations of those capacities. A short factual question may depend on an obscure source. A long transformation may require little reasoning but strict constraint preservation. A coding failure may come from an unavailable API rather than weak planning. Prompt length and apparent complexity reveal little about the decisive resource.

Open-ended quality is equally difficult to reduce to one score. A polished answer may be factually wrong. A concise answer may omit the one qualification that changes the decision. A stronger model may improve conceptual discrimination while changing style in a way the user dislikes. The utility policy can combine these concerns, but the evidence must still measure them.

The models themselves are moving targets. Providers update model weights, post-training, inference systems, tools, and product policies. A router trained on last quarter’s model pair may retain some value, but that transfer is an empirical question too.

These complications do not prove that general routing is impossible. They raise the amount and specificity of evidence needed to justify it. A generic label such as “complex task” cannot carry that burden.

## Workflow Integration Adds Information, Not Validity

Some allocation decisions use only information available before execution. Others depend on intermediate artifacts, tool results, errors, or progress. This is often presented as a separate solution: an integrated agent can watch the task and adapt.

A coding workflow may observe that a patch failed the tests three times. A research workflow may find that the available sources do not support a claim. Those observations can become useful routing features if comparative data show that a particular model or reasoning level performs better under those conditions. Without that link, the workflow has only described the problem more precisely.

Workflow-integrated selection is therefore a subtype of system judgment. It can improve the timing and resolution of a validated allocation method. It cannot create the validation.

This establishes the proper order of development:

1. show that an allocation rule predicts comparative outcomes;
2. determine which inputs the rule needs;
3. integrate it when some of those inputs arise only during execution.

## Cascading and the Causal Error

Cascading deserves separate attention because it introduces a tempting inference:

> The attempt failed, so the task needs a stronger model.

Failure does not identify its cause. The missing resource may be information, access to a file, a specialized tool, clearer constraints, better decomposition, a different representation, or human judgment. The request may also be impossible as stated.

If evidence is missing, a stronger model can produce a better-defended hallucination. If the premise is wrong, it can develop the wrong argument more thoroughly. If a tool is unavailable, more reasoning does not supply it.

An intelligent recovery policy would compare interventions from the observed state. It would ask whether retrieval, reframing, another tool, more context, a specialized model, or additional inference compute has the best expected effect. A cascade usually considers a much smaller menu: accept the cheap answer or apply more model.

Success after escalation does not prove that escalation was necessary. The stronger model may have helped, but the original model might also have succeeded on another sample. A prompt repair or retrieval call may have worked better. Without the counterfactual, the system can record correlation and mistake it for diagnosis.

This creates a compute bias. The architecture is built to allocate models, so model power becomes its default remedy. Over time, successful retries can reinforce the policy even when their success came from stochastic variation.

## The Full Cost

Routing adds classification, model or embedding calls, policy maintenance, logging, and context transfer. Cascades may repeat generation and increase latency. Long conversations can lose cache efficiency or behavioral consistency when models change.

These costs may be small in a high-volume application. They are still predictable. The benefit depends on the router choosing well often enough to repay them.

The hidden costs are harder to count:

- repeated commitment to the original framing;
- more fluent restatement of unsupported claims;
- neglect of non-model remedies;
- greater authority attached to an expensive answer;
- misleading attribution when a retry succeeds;
- operational data that reward escalation without testing alternatives.

A router should therefore be compared with fixed allocation and simple rules after the whole process is counted. If a nearest-neighbour lookup or stable task policy performs as well, the dynamic system has not earned its complexity.

## Verification Is a Different Architecture

Verification determines whether a result meets its criteria. Model allocation chooses the resource that attempts the task. Recovery chooses what to change after a failure.

A test suite may identify a broken program with high confidence. It does not follow that another model is the best repair method. A citation audit may expose an unsupported claim without showing that more inference compute will find a source. A human reviewer may identify a conceptual error without diagnosing insufficient model capacity.

Verification can guide recovery. Its result may support another model when comparative evidence warrants that choice. It may instead call for retrieval, correction, reframing, or stopping.

Keeping the functions separate preserves the value of verification without turning every detected problem into an escalation trigger.

## A Defensible Policy

General-purpose systems should allocate models in advance under an explicit policy. The policy can use known capability requirements, available evaluations, cost constraints, and the user’s tolerance for risk. It should be revised when better comparative evidence appears.

Dynamic selection is justified where:

- the workload is defined and reasonably stable;
- success can be measured;
- candidate models have been compared on representative tasks;
- the router generalizes to new cases;
- its full cost is lower than the benefit;
- runtime features improve prediction when runtime integration is used.

The user should retain an override because cost, latency, reproducibility, and risk are partly matters of preference.

Fixed allocation is not a claim that one model fits every task. Different task classes can receive different advance policies. The point is to avoid pretending that unsupported case-by-case prediction becomes reliable because it is automatic.

The same standard should govern future improvements. A new router, confidence score, or agent monitor should be tested against fixed models, simple rules, and similarity-based baselines. It should be revalidated after material changes to the models or workflow.

## Conclusion

Model selection is a comparative empirical problem. A router needs evidence that its chosen allocation is more likely than the alternatives to meet a defined standard at an acceptable cost.

Current research shows that such evidence can support useful routing on bounded, measurable workloads. It does not establish a general ability to allocate models across heterogeneous, open-ended work. Multidimensional model differences and unstable definitions of quality make broad transfer difficult.

Workflow integration can provide evidence that appears during execution, but it cannot validate the rule applied to that evidence. Cascading adds a further risk by treating failure as a reason to apply more model power without establishing that model power is the missing resource.

The prudent default is advance allocation under a stable policy, with dynamic selection reserved for cases where representative comparative evidence shows a net benefit. Verification should test the work. It should not decide the remedy by default.

## References

- Chen, Lingjiao, Matei Zaharia, and James Zou. “[FrugalGPT: How to Use Large Language Models While Reducing Cost and Improving Performance](https://arxiv.org/abs/2305.05176).” 2023.
- Huang, Zhongzhan, et al. “[RouterEval: A Comprehensive Benchmark for Routing LLMs to Explore Model-level Scaling Up in LLMs](https://arxiv.org/abs/2503.10657).” 2025.
- Kassem, Aly M., Bernhard Schölkopf, and Zhijing Jin. “[How Robust Are Router-LLMs? Analysis of the Fragility of LLM Routing Capabilities](https://arxiv.org/abs/2504.07113).” 2025.
- Li, Yang. “[Rethinking Predictive Modeling for LLM Routing: When Simple kNN Beats Complex Learned Routers](https://arxiv.org/abs/2505.12601).” 2025.
- Ong, Isaac, et al. “[RouteLLM: Learning to Route LLMs with Preference Data](https://arxiv.org/abs/2406.18665).” 2024.
- Amazon Web Services. “[Understanding Intelligent Prompt Routing in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-routing.html).”
- OpenRouter. “[Auto Router](https://openrouter.ai/docs/guides/routing/routers/auto-router).”
