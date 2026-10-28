# Against General-Purpose Dynamic Model Selection

## Executive Summary

Model selection is a comparative empirical problem: which model, reasoning level, or configuration is most likely to meet a task’s requirements at an acceptable total cost? Learned routers and cascades have achieved useful cost–quality trade-offs on evaluated workloads. Those results do not establish reliable selection across heterogeneous, open-ended work.

The central obstacle is not a lack of routing mechanisms. It is the difficulty of predicting comparative outcomes when model capabilities, task requirements, and quality criteria vary. Information gathered during execution can improve a validated prediction, but a failed attempt alone does not identify the appropriate remedy.

For general-purpose systems without representative comparative evidence, this paper recommends explicit advance allocation rather than unsupported case-by-case optimization. That is a conservative operational default, not a finding that fixed allocation always performs better. Dynamic selection earns its place when it improves the full workflow against credible baselines. Verification should assess the result without automatically prescribing model escalation.

## The Question Is Empirical

A model-selection system chooses which model, reasoning level, or configuration should handle a task. This paper distinguishes **request-time routing**, which selects from the incoming task, from **runtime selection**, which revises allocation using observations made during execution. A **cascade** is one runtime design: attempt, evaluate, then escalate if needed. Either form makes a prediction: this allocation will produce a better result, or a sufficiently good result at lower cost, than the available alternatives.

For a defined class of tasks, the relevant question is:

> What evidence shows that one allocation is more likely than another to meet the required standard at an acceptable cost?

This is a comparative question. It cannot be answered by showing that a model is capable, that a task looks difficult, or that a later attempt succeeded. The system needs some basis for estimating how the alternatives would perform on the same kind of work.

The standard also depends on the purpose. A support chatbot may optimize acceptance rate and latency. A coding system may use tests. A research workflow may care about source quality, factual accuracy, completeness, and constraint preservation. There is no useful definition of “best model” until the required outcome and the value of cost, speed, and risk have been specified.

Dynamic selection has demonstrated value in bounded workloads with repeated tasks and measurable outcomes. The objection is to its use as a general solution before the comparative judgment has been validated.

## What Would Count as Evidence?

The clearest evidence would come from repeated comparisons on representative tasks. Candidate models would attempt the same kinds of work under controlled conditions. Their outputs would be judged by criteria that can detect the failures that matter. The evaluation would use enough cases and repeated samples to distinguish a model effect from ordinary generation variance.

The resulting policy would then need validation on later or held-out work. A router that memorizes the evaluation set has not learned how to allocate new tasks. A policy that works on mathematics may not transfer to legal interpretation, long-form synthesis, or code repair. Model updates, prompt changes, new tools, and altered workflows can make an earlier result stale.

Evidence should be assessed by its validity, coverage, independence, and calibration. Tests, calculations, schemas, and citation checks offer externally checkable outcomes, but may miss important requirements. Expert judgments and production outcomes can cover qualities that automated checks omit, provided their rubric and sampling are appropriate. Learned predictors and similarity rules inherit the limitations of the outcomes on which they are trained.

Verbal confidence, generic complexity scores, and uncalibrated model judgments are hypotheses about performance, not substitutes for measuring it. No evidence type is automatically adequate: a passing test suite can be incomplete, and a preference label can reward presentation rather than correctness.

For runtime selection, comparisons must also cover the states in which intervention is proposed. An evaluation of first attempts does not by itself validate a policy for recovering from failed attempts.

## What Current Systems Use

Current model-selection systems draw on several kinds of evidence. They should not be treated as one method.

### Rules and capability gates

The simplest systems route by known requirements. A request needing vision, a large context window, structured output, or a particular tool can be restricted to models that support it. Teams may also assign recurring tasks to models that performed adequately during local evaluation.

These rules are limited, but inspectable. Their claims are modest: this model has the required interface, or this model met the threshold on this task class. They do not require a general theory of prompt difficulty.

### Learned pre-execution routers

Learned routers predict comparative performance from the prompt or a representation of it. RouteLLM, for example, trains routers on preference data showing when a stronger model’s response is preferred to a weaker one. Its published evaluation reported substantial cost reductions on the tested benchmarks while preserving the strong model’s measured quality. The paper also reported transfer when the candidate models changed. Those are meaningful results, but they concern the benchmarks, model pairs, preference data, and evaluation procedure used in the study. [RouteLLM](https://arxiv.org/abs/2406.18665)

Other work trains on answer correctness, uncertainty, or large collections of recorded model outcomes. RouterEval assembled more than 200 million performance records across twelve evaluations and thousands of models, providing a large-scale resource for comparative evaluation. Its authors also found considerable room for improvement in existing methods. [RouterEval](https://arxiv.org/abs/2503.10657)

The sophistication of the predictor is not itself evidence of better allocation. A 2025 study found that a well-tuned nearest-neighbour method could match or outperform more complex routers across its evaluation suite. Historical similarity may be enough when model performance is locally consistent, and it is easier to inspect. [When Simple kNN Beats Complex Learned Routers](https://arxiv.org/abs/2505.12601)

### Commercial prompt routers

Amazon Bedrock predicts the response quality of two models from the same family and routes according to a configured quality-difference threshold. The service exposes the selected model and lets the operator choose the trade-off. Amazon also states that the router cannot adapt its decisions from application-specific performance data, may not be optimal for specialized uses, and depends on its initial training data. It recommends evaluating the router on the intended application before production use. [Amazon Bedrock Intelligent Prompt Routing](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-routing.html)

OpenRouter’s current Auto Router classifies the task and ranks eligible models using recent community spending for that task type, subject to capability filters and a selected cost tier. It exposes the chosen model. Session stickiness prefers the previous model while it remains a leading candidate, rather than guaranteeing that a conversation stays on one model. These are documented routing signals and controls, not direct evidence of comparative quality for a particular user’s workload. [OpenRouter Auto Router](https://openrouter.ai/docs/guides/routing/routers/auto-router)

These systems show that general prompt routing is available as a product. Product availability is different from general validation. The operator still has to decide whether the router’s quality prediction corresponds to the outcomes that matter in the application.

### Cascades

A cascade tries one model, evaluates its output, and calls another model when a threshold is not met. FrugalGPT demonstrated large cost reductions on its evaluated datasets by learning combinations of models and escalation rules. This is good evidence for cascades on workloads resembling those tests. [FrugalGPT](https://arxiv.org/abs/2305.05176)

A cascade can lower expected cost when the initial call is cheap, its acceptance rule reliably distinguishes adequate outputs, and escalation improves rejected cases enough to repay the additional work. False acceptance and unnecessary escalation must both be counted.

## What Has Been Established

The research supports three conclusions.

First, models have complementary performance. A fixed “best” model can be beaten on some benchmark distributions by selecting among candidates. There is genuine value available to a router.

Second, routing can reduce cost while retaining measured quality when the workload is repeated and the supervision is informative. Preference data, correctness labels, calibrated uncertainty, and historical outcomes can all support useful policies.

Third, the success is conditional. The router inherits the definition of quality in its training and evaluation data. A preference score may reward fluency, style, or agreement. An automated judge may reproduce model biases. A benchmark may test short answers while the application requires long-context synthesis and careful omission detection.

Recent evaluations make the limitation concrete. A study of preference-based and commercial routers found efficiency gains alongside fragile, category-driven behavior. One router sent all coding and mathematics prompts to the most powerful model even when smaller models were adequate, while weaker routing on jailbreak prompts introduced safety concerns. [How Robust Are Router-LLMs?](https://arxiv.org/abs/2504.07113)

Newer evidence reinforces the importance of baselines without settling the general question. LLMRouterBench, published in Findings of ACL 2026 and covering more than 400,000 instances, 21 datasets, and 33 models, found model complementarity but also found that several routing approaches did not reliably outperform a simple baseline. Complementarity creates an opportunity; it does not show that a deployable selector can capture it. [LLMRouterBench](https://aclanthology.org/2026.findings-acl.1881/)

An October 2026 preprint evaluated six commercial routers across fourteen settings and eight task categories. None outperformed random selection between two carefully chosen models at matched cost. This is evidence against the tested routing selections on that benchmark, not against every possible router: the study used English, single-turn tasks and one sampled outcome per query–model pair. Its strongest practical implication is to test roster selection and cost-matched random mixtures before crediting prompt-specific routing. [Dynamic LLM Routers are Often Misguided](https://arxiv.org/html/2610.02762v1)

Positive evidence also extends beyond single-turn routing. An August 2026 preprint reported that six of seven learned routers exceeded an always-largest-model baseline on average across five tested multi-agent topologies. One of these, EloRouter, uses a query-independent ranking, so beating the always-largest baseline does not isolate the value of dynamic decisions. It remains evidence about those tasks, model pools, metrics, and baselines; a separate personalization experiment in the study found that an automated persona-based preference ranking differed from a small human evaluation. The result strengthens the case for testing integrated policies while illustrating the dependence on how quality is measured. [LLMRouter](https://arxiv.org/html/2608.06867v1)

Taken together, these studies support conditional benefits and serious baseline sensitivity. They do not establish a general faculty for inspecting arbitrary work and determining the right allocation.

## Why Generalization Is Difficult

Model capability is multidimensional. Models differ in learned knowledge, reasoning behavior, instruction following, context use, domain specialization, tool use, calibration, latency, and price. A reasoning-effort control changes part of that configuration; it does not by itself supply external evidence or grant access to a tool.

Tasks also demand different combinations of those capacities. A short factual question may depend on an obscure source. A long transformation may require little reasoning but strict constraint preservation. A coding failure may come from an unavailable API rather than weak planning. Prompt length and apparent complexity alone do not identify the decisive resource.

Open-ended quality is equally difficult to reduce to one score. A polished answer may be factually wrong. A concise answer may omit the one qualification that changes the decision. A stronger model may improve conceptual discrimination while changing style in a way the user dislikes. The utility policy can combine these concerns, but the evidence must still measure them.

The models themselves are moving targets. Providers update model weights, post-training, inference systems, tools, and product policies. A router trained on last quarter’s model pair may retain some value, but that transfer is an empirical question too.

These complications do not prove that general routing is impossible. They raise the amount and specificity of evidence needed to justify it. A generic label such as “complex task” cannot carry that burden.

## Workflow Integration Adds Information, Not Validity

Workflow integration makes intermediate artifacts, tool results, errors, and progress available as routing features. That can make runtime selection more informative than request-time routing. It does not eliminate the need to test whether those features predict the relative benefit of the available interventions.

The development task is to define the observed state, compare actions from that state, and validate the resulting policy on new cases. Where the choice itself changes later observations, evaluate the complete policy as well as its component predictions. A locally useful switch need not improve end-to-end quality, latency, or cost.

## Cascading and the Causal Error

Cascading deserves separate attention because it introduces a tempting inference:

> The attempt failed, so the task needs a stronger model.

Failure does not identify its cause. The missing resource may be information, access to a file, a specialized tool, clearer constraints, better decomposition, a different representation, or human judgment. The request may also be impossible as stated.

If evidence is missing, a stronger model can produce a better-defended hallucination. If the premise is wrong, it can develop the wrong argument more thoroughly. If a tool is unavailable, more reasoning does not supply it.

An intelligent recovery policy would compare interventions from the observed state. It would ask whether retrieval, reframing, another tool, more context, a specialized model, or additional inference compute has the best expected effect. A cascade usually considers a much smaller menu: accept the cheap answer or apply more model.

Success after escalation does not prove that escalation was necessary. The stronger model may have helped, but the original model might also have succeeded on another sample. A prompt repair or retrieval call may have worked better. An observed success alone cannot distinguish these explanations. Representative randomized trials, controlled replays, or appropriately controlled offline evaluations with adequate action coverage can estimate comparative effects; every incident need not have every alternative rerun.

This can create a compute bias: when the architecture considers only model upgrades, non-model remedies are excluded before their value is tested. A controlled comparison should therefore include retrying the same model and plausible changes to information, tools, or task framing—not just escalating versus stopping.

## The Full Cost

Routing can add classification, model or embedding calls, policy maintenance, logging, and context transfer. Cascades may repeat generation and increase latency. Long conversations can lose cache efficiency or behavioral consistency when models change.

These costs are workload-dependent, not necessarily large. Measure the complete process: routing overhead, accepted failures, recovery work, output quality, and average and tail latency as well as the selected model’s price. Report trade-offs rather than hiding them in a single score when stakeholders value them differently.

Compare the router with fixed-model allocation, capability rules, task-class policies, and appropriate similarity-based methods under the same quality target or resource budget. The relevant question is whether the added mechanism improves an attainable operating point, not whether it beats an arbitrarily weak default.

## Verification Is a Different Architecture

Verification determines whether a result meets its criteria. Allocation chooses the resource that attempts the task. Recovery chooses what to change after a failure. These functions can cooperate without being collapsed into one decision.

A verifier should expose what failed and the strength of that assessment. A recovery policy can then use that evidence to choose another model, obtain information, change tools, correct the approach, or stop. Keeping the decisions distinct preserves useful failure detection even where the best remedy remains uncertain.

## A Defensible Policy

Where comparative evidence is insufficient, general-purpose systems should use an explicit advance allocation policy based on capability requirements, available evaluations, cost constraints, and the user’s tolerance for risk. This recommendation favors an inspectable baseline over an unvalidated optimizer; it does not establish superior quality or lower cost. The baseline itself needs evaluation and revision.

Dynamic selection is justified where:

- the workload is defined and reasonably stable;
- success can be measured;
- candidate models have been compared on representative tasks;
- the router generalizes to new cases;
- its full cost is lower than the benefit;
- runtime features improve prediction when runtime integration is used.

The user should retain an override because cost, latency, reproducibility, and risk are partly matters of preference.

A fixed policy is not necessarily a fixed model: different task classes can receive different allocations, and a learned router can itself remain fixed after training. The distinction here is between justified allocation rules and unsupported case-by-case predictions, not between all automation and manual choice.

The same standard should govern future improvements. A new router, confidence score, or agent monitor should be tested against fixed models, simple rules, and similarity-based baselines. It should be revalidated after material changes to the models or workflow.

## Conclusion

The case against general-purpose dynamic model selection is a case against an unearned inference: success on evaluated workloads does not establish reliable allocation across arbitrary work. Bounded routing successes remain valuable, and broader success is an empirical possibility rather than something ruled out in principle.

Use explicit allocation as the baseline, test dynamic policies against credible alternatives, and separate detection of failure from choice of remedy. The mechanism should follow the evidence—not stand in for it.

## References

- Amazon Web Services. “[Understanding Intelligent Prompt Routing in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-routing.html).”
- Chen, Lingjiao, Matei Zaharia, and James Zou. “[FrugalGPT: How to Use Large Language Models While Reducing Cost and Improving Performance](https://arxiv.org/abs/2305.05176).” 2023.
- Feng, Tao, et al. “[LLMRouter: Unified Infrastructure for Developing, Evaluating, and Deploying LLM Routers](https://arxiv.org/abs/2608.06867).” 2026. Preprint.
- Huang, Zhongzhan, et al. “[RouterEval: A Comprehensive Benchmark for Routing LLMs to Explore Model-level Scaling Up in LLMs](https://arxiv.org/abs/2503.10657).” 2025.
- Kassem, Aly M., Bernhard Schölkopf, and Zhijing Jin. “[How Robust Are Router-LLMs? Analysis of the Fragility of LLM Routing Capabilities](https://arxiv.org/abs/2504.07113).” 2025.
- Li, Hao, et al. “[LLMRouterBench: A Massive Benchmark and Unified Framework for LLM Routing](https://aclanthology.org/2026.findings-acl.1881/).” Findings of ACL, 2026.
- Li, Yang. “[Rethinking Predictive Modeling for LLM Routing: When Simple kNN Beats Complex Learned Routers](https://arxiv.org/abs/2505.12601).” 2025.
- Ong, Isaac, et al. “[RouteLLM: Learning to Route LLMs with Preference Data](https://arxiv.org/abs/2406.18665).” 2024.
- OpenRouter. “[Auto Router](https://openrouter.ai/docs/guides/routing/routers/auto-router).”
- Wang, Sam, et al. “[Dynamic LLM Routers are Often Misguided](https://arxiv.org/abs/2610.02762).” 2026. Preprint.
