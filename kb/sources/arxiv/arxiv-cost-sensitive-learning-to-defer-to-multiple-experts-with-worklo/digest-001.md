---
type: Source Digest
title: Cost-Sensitive Learning to Defer to Multiple Experts with Workload Constraints - part 1 of 5 (pp. 1-7)
description: 'Verified paraphrased digest, pp. 1-7: Cost-Sensitive Learning to Defer to Multiple Experts with Workload Constraints; Cost-Sensitive Learning to Defer to Multiple Experts with Workload Constraints > Marco O.P Sampaio; Cost-Sensitive Learning to Defer to Multiple Experts with Workload Constraints > Abstract; and 3 more sections'
resource: https://arxiv.org/abs/2403.06906
tags:
- academic_finding
- alerts_triage
- global_academic
- model_development
- preprint
status: stable
source_id: arxiv-cost-sensitive-learning-to-defer-to-multiple-experts-with-worklo
issuer: arxiv
issuer_name: arXiv
jurisdictions:
- GLOBAL_ACADEMIC
tier: 3
instrument_type: preprint
normative_force: academic_finding
publication_date: '2024-11-03'
legal_status: unknown
part: 1
parts_total: 5
content_mode: digest
generated:
  by: claude-code-subagent/claude-sonnet-5-5
  at: '2026-11-22T14:46:04Z'
verified:
- by: process:kb-digest-check/anchor-match
  at: '2026-11-22T14:46:04Z'
- by: claude-code-judge-agent/claude-opus-5-5
  at: '2026-11-22T14:46:04Z'
sources:
- id: original
  resource: https://arxiv.org/abs/2403.06906
  title: Cost-Sensitive Learning to Defer to Multiple Experts with Workload Constraints
  author: org:arxiv
  last_modified: '2024-11-03T00:00:00Z'
digest_points: 50
---

# Cost-Sensitive Learning to Defer to Multiple Experts with Workload Constraints (digest)

[source overview](overview.md) | [next part](digest-002.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (pp. 1-7) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **academic finding**.

## Abstract

- **descriptive / context**: Learning to defer (L2D) aims to improve human-AI collaboration by learning when to defer decisions to humans who are more likely to be correct than an ML classifier. (p. 1)[^original]  
  <sub>anchor: "aims to improve human-AI collaboration systems by learning how to defer decisions to humans"</sub>
- **descriptive / limitation**: Existing L2D research overlooks three real-world aspects: neglecting cost-sensitive scenarios with different costs for type I and type II errors, requiring concurrent human predictions for every training instance, and not handling human work-capacity constraints. (p. 1)[^original]  
  <sub>anchor: "neglecting cost-sensitive scenarios, where type I and type II errors have different costs"</sub>
- **descriptive / definition**: The authors propose DeCCaF, which uses supervised learning to model the probability of human error with only one expert prediction per instance and uses constraint programming to globally minimise error cost subject to workload limitations. (p. 1)[^original]  
  <sub>anchor: "employing supervised learning to model the probability of human error under less restrictive data requirements"</sub>
- **descriptive / finding or result**: DeCCaF was tested in cost-sensitive fraud detection scenarios with teams of 9 synthetic fraud analysts, each with individual work-capacity constraints. (p. 1)[^original]  
  <sub>anchor: "We test DeCCaF in a series of cost-sensitive fraud detection scenarios with different teams of 9 synthetic fraud analysts"</sub>
- **descriptive / finding or result**: DeCCaF performs significantly better than the baselines across a wide array of scenarios, achieving an average 8.4% reduction in misclassification cost. (p. 1)[^original]  
  <sub>anchor: "achieving an average 8 _._ 4% reduction in the misclassification cost"</sub>
- **descriptive / context**: The code used for the experiments is publicly available at a GitHub repository. (p. 1)[^original]  
  <sub>anchor: "The code used for the experiments is available at"</sub>

## 1 Introduction

- **descriptive / context**: Human-AI collaboration (HAIC) research argues that humans have complementary strengths and weaknesses to AI, and collaborative humans with models may achieve synergistic performance above either alone. (p. 2)[^original]  
  <sub>anchor: "humans collaborating with an ML model may achieve synergistic performance: a higher performance than humans or models alone"</sub>
- **descriptive / context**: Learning to defer is described as the state-of-the-art framework for managing assignments in HAIC, and aims to improve on rejection learning by also estimating human confidence and passing the instance to the most likely correct decision-maker. (p. 2)[^original]  
  <sub>anchor: "L2D aims to improve upon previous approaches, such as rejection learning"</sub>
- **descriptive / limitation**: Only a small subset of L2D research addresses the multi-expert setting, and Verma et al. (2023) are described as proposing the only two consistent multi-expert formulations, both assuming every expert's predictions exist for all training instances. (p. 2)[^original]  
  <sub>anchor: "Verma et al. (2023) propose the only two consistent multi-expert L2D formulations"</sub>
- **descriptive / limitation**: In real applications, data is often limited, with only a single expert or a small subset of experts providing predictions per instance, so collecting every expert's predictions could be costly or unfeasible. (p. 2)[^original]  
  <sub>anchor: "This means that a practitioner aiming to train L2D algorithms would have to purposefully collect the set of every expert’s predictions"</sub>
- **descriptive / limitation**: Current multi-expert L2D methods neglect human capacity limitations; deferring all cases to a consistently superior expert would be optimal but is not feasible in practice. (p. 2)[^original]  
  <sub>anchor: "the optimal assignment would be to defer all cases to that expert, which in practice is not feasible"</sub>
- **descriptive / limitation**: Current work neglects cost-sensitive scenarios, where misclassification cost can be class or instance dependent, for example false alarms in medicine being less harmful than missed diagnoses. (p. 2)[^original]  
  <sub>anchor: "the cost of misclassification can be class or even instance-dependent"</sub>
- **descriptive / definition**: DeCCaF is a deferral approach for cost-sensitive human-AI decision-making that respects human capacity constraints and is composed of three components: an ML classifier, a human expertise model (HEM), and an assigner computing the best assignments given misclassification costs and capacity constraints. (p. 2)[^original]  
  <sub>anchor: "DeCCaF: a novel deferral approach to manage assignments in cost-sensitive human-AI decisionmaking"</sub>
- **descriptive / finding or result**: Across all scenarios, DeCCaF performs similarly to, or significantly better than, L2D baselines as measured by average misclassification costs. (p. 3)[^original]  
  <sub>anchor: "DeCCaF performs similarly to, or significantly better than L2D baselines, as measured by average misclassification costs"</sub>
- **descriptive / context**: The paper lists contributions: a novel L2D method using constraint programming for optimal assignments, a novel benchmark of complex feature-dependent synthetic expert decisions in financial fraud detection, and experimental evidence of outperforming baselines. (p. 3)[^original]  
  <sub>anchor: "A novel benchmark of complex, feature-dependent synthetic expert decisions"</sub>
- **descriptive / context**: The paper's section overview states the training method for the classifier-rejector framework is shown to produce optimal unconstrained deferral, and a constraint-based global assignment formulation is proposed for capacity constraints. (p. 3)[^original]  
  <sub>anchor: "demonstrating that it produces optimal unconstrained deferral"</sub>

## 2.1 Current L2D Methods

- **descriptive / definition**: Rejection learning (ReL) defers to humans the instances that the model rejects to predict, for example by rejecting when model uncertainty exceeds a threshold. (p. 3)[^original]  
  <sub>anchor: "rejecting to predict if the uncertainty estimate is above a given threshold"</sub>
- **descriptive / context**: Madras et al. (2018b) criticised ReL for ignoring human performance and proposed L2D with jointly trained classifier and assignment system accounting for human error in the training loss. (p. 4)[^original]  
  <sub>anchor: "Madras et al. (2018b) criticize ReL, arguing that it does not consider the performance of the human involved in the task"</sub>
- **descriptive / finding or result**: Mozannar & Sontag (2020b) showed the Madras et al. loss is inconsistent and proposed a consistent surrogate loss with better test results; Verma & Nalisnick (2022b) showed that surrogate has a degenerate parameterization causing miscalibration of expert correctness probabilities. (p. 4)[^original]  
  <sub>anchor: "Verma & Nalisnick (2022b) critique the approach of Mozannar & Sontag (2020b)"</sub>
- **descriptive / context**: Verma et al. (2023) proposed the first consistent and calibrated surrogate losses for the multi-expert setting. (p. 4)[^original]  
  <sub>anchor: "Verma et al. (2023) propose the first consistent and calibrated surrogate losses for the multi-expert setting"</sub>
- **descriptive / limitation**: All the surrogate-loss studies target the 0-1 loss and so are not directly applicable to cost-sensitive scenarios, whether class-dependent or instance-specific costs. (p. 4)[^original]  
  <sub>anchor: "All aforementioned studies focus on deriving surrogates for the 0 _−_ 1 loss"</sub>
- **descriptive / limitation**: The authors argue joint learning is unsuitable for real-world use because the instances most likely deferred are those where the classifier performs worst, making the system susceptible to changes in human availability. (p. 4)[^original]  
  <sub>anchor: "We argue that joint learning is not be suitable for real-world applications"</sub>
- **descriptive / limitation**: The key barrier to adopting current L2D methods is that they require predictions from every human in the team for every training instance; data-efficient work exists only for the single-expert setting. (p. 4)[^original]  
  <sub>anchor: "the key barrier to the adoption of current L2D methods is that they require predictions from every human in the team"</sub>
- **descriptive / finding or result**: Few multi-expert L2D works consider control of the number of deferrals; Mao et al. (2024) do so using a constant deferral cost per expert within their realizable H-consistent two-stage losses. (p. 4)[^original]  
  <sub>anchor: "only Mao et al. (2024) consider control of the amount of deferrals in multi-expert L2D"</sub>
- **descriptive / limitation**: Fixed deferral-cost formulations would not be adequate for real systems, where expert availability may vary drastically over time, such as schedules or days off. (p. 4)[^original]  
  <sub>anchor: "it would not be adequate for a real-world system, where the availability of experts may vary drastically over time"</sub>
- **descriptive / context**: Zhou et al. (2022) allow hard constraints on tokens per expert and experts per token at inference in sparse mixture-of-experts models, enabling dynamic limits on compute without retraining. (p. 4)[^original]  
  <sub>anchor: "This approach allows for dynamic limitation of the compute resources necessary, without needing to retrain their models"</sub>
- **descriptive / context**: The proposed algorithm is multi-expert, usable in cost-sensitive scenarios, trained under restrictive data requirements, and takes individual human work-capacity constraints imposed only at inference time. (p. 4)[^original]  
  <sub>anchor: "taking into account individual human work-capacity constraints that are imposed only at inference time"</sub>
- **descriptive / finding or result**: In the multi-expert setting, the two-stage one-vs.-all approach of Verma et al. (2023) outperformed the adaptation of the softmax loss of Mozannar & Sontag (2020a), which uses joint learning, because of calibration problems. (p. 4)[^original]  
  <sub>anchor: "the two-stage one-vs.-all approach of Verma et al. (2023) outperforms their adaptation of the softmax loss of Mozannar & Sontag (2020a)"</sub>
- **descriptive / finding or result**: Mozannar & Sontag (2020b) argue the main classifier should specialise on instances that will be assigned to it, by jointly training classifier and rejector without penalising classifier mistakes on deferred instances. (p. 4)[^original]  
  <sub>anchor: "Mozannar & Sontag (2020b) argue that the main classifier should specialize on the instances that will be assigned to it"</sub>
- **descriptive / limitation**: Existing multi-expert L2D methods rarely consider work-capacity constraints; only Mao et al. (2024) control the amount of deferrals, via a constant per-expert deferral cost. (p. 4)[^original]  
  <sub>anchor: "only Mao et al. (2024) consider control of the amount of deferrals in multi-expert L2D"</sub>

## 2.2 Simulation of Human Experts

- **descriptive / context**: Due to the lack of sizeable public real-world multi-expert datasets, most authors use label noise to simulate expert predictions on established ML datasets. (p. 5)[^original]  
  <sub>anchor: "most authors use _label noise_ to produce arbitrarily accurate expert predictions"</sub>
- **descriptive / limitation**: Synthetic experts in prior work are simplistic, being either feature-independent or dependent on only a single feature or concept, and this approach has been criticised. (p. 5)[^original]  
  <sub>anchor: "The main drawback of these synthetic experts is that their expertise is rather simplistic"</sub>
- **descriptive / method**: The authors propose instance-dependent label noise (IDN) to simulate more complex and realistic synthetic experts, since human errors depend on task difficulty and hence on features. (p. 5)[^original]  
  <sub>anchor: "In this work, we propose an IDN approach to simulate more complex and realistic synthetic experts"</sub>

## 3 Method

- **descriptive / method**: DeCCaF trains a human expertise model (HEM) predicting the probability that deferral to a given expert yields a correct decision, trains an ML classifier estimating likelihood of correct automatic prediction, and then uses constraint programming to maximise global probability of correct decisions under workload constraints. (p. 5)[^original]  
  <sub>anchor: "We then employ constraint programming (CP) to maximize the global probability of obtaining correct decisions under workload constraints"</sub>

## 3.1 Deferral Formulation

- **descriptive / definition**: Each instance has a ground-truth label, a feature vector, a specific misclassification cost, a prediction from one expert, and an index identifying which expert made that prediction; the training set consists of one such expert prediction per instance. (p. 5)[^original]  
  <sub>anchor: "a prediction _mj,i ∈Y_ from a given expert"</sub>
- **descriptive / method**: The classifier-rejector formulation uses a classifier h and a rejector r that either outputs 0 (classifier decides) or the index of the expert to which the decision is deferred. (p. 5)[^original]  
  <sub>anchor: "if r ( x i ) = j , the decision on instance i will be deferred to expert j"</sub>
- **descriptive / method**: The 0-1 loss is used as learning objective: the system incurs loss 1 when the classifier is wrong on automatic predictions and loss 1 when the deferred expert is wrong. (p. 5)[^original]  
  <sub>anchor: "When expert _j_ makes the prediction (i.e., _r_ ( _x_ ) = _j_ ), the system incurs a loss of 1 if the human is incorrect"</sub>

## 3 Method

- **expected / requirement**: The authors state it is crucial that the assigner can be trained with limited human prediction data, with only one expert prediction per instance. (p. 5)[^original]  
  <sub>anchor: "it is crucial that the assigner can be trained with limited human prediction data"</sub>
- **expected / requirement**: The authors state that, for the method to be applicable in real-world scenarios, it is crucial that the method be robust to variations in expert work-capacity at inference. (p. 5)[^original]  
  <sub>anchor: "it is crucial that the assigner can be trained with limited human prediction data (only one expert prediction per instance)"</sub>

## 3.1 Deferral Formulation

- **descriptive / finding or result**: Verma et al. (2023) show that Bayes-optimal classifier and rejector minimising the 0-1 loss exist; the 0-1 loss is non-convex and computationally hard, so prior work used consistent convex surrogates. (p. 6)[^original]  
  <sub>anchor: "As _L_ 0 _−_ 1 is non-convex, thus computationally hard to optimize"</sub>
- **descriptive / method**: Rather than deriving a consistent surrogate loss for jointly training h and r, the authors train the classifier and rejector separately, and prove convergence to the Bayes-optimal pair under limited data. (p. 6)[^original]  
  <sub>anchor: "rather than deriving a consistent surrogate loss for simultaneously training _h_ and _r_ , we train both components separately"</sub>
- **descriptive / method**: The classifier is trained as a binary classifier using a proper binary composite loss with a well-defined inverse link function, such as the logistic loss; the resulting score yields calibrated estimates of P(y=1|x) in the large-sample limit. (p. 6)[^original]  
  <sub>anchor: "producing calibrated estimates of _P_ ( _y_ = 1 _|_ _x_ )"</sub>
- **descriptive / method**: For simplicity, the authors consider the binary classification case, where Y is the set {0,1}. (p. 6)[^original]  
  <sub>anchor: "For simplicity, we consider the binary classification case"</sub>
- **descriptive / method**: The rejector uses a human expertise model (HEM) scoring function predicting whether an expert is correct, conditioned on the expert index, trained on the single-expert-per-instance training set. (p. 7)[^original]  
  <sub>anchor: "we resort to a human expertise model (HEM) with scoring function"</sub>
- **permissive / method**: Additional information available to experts, such as an ML model score, could be included in the HEM scoring function input so that correctness estimates condition on all information available to the expert. (p. 7)[^original]  
  <sub>anchor: "should additional information _e_ _∈E_ be available to the experts"</sub>
- **descriptive / finding or result**: With the HEM scoring function, the rejector estimates P(y = m_j | x, j) and, in the large-sample limit, agrees with the Bayes-optimal rejector, so the classifier-rejector pair converges to the minimisers of the 0-1 loss. (p. 7)[^original]  
  <sub>anchor: "implies that _r_ ˆ will agree with the Bayes-optimal rejector _r__∗_"</sub>

## 3.2 Definition of Capacity Constraints

- **descriptive / method**: Capacity is applied over batches of instances corresponding to pre-defined time periods, since balancing workload over a month differs from balancing it daily. (p. 7)[^original]  
  <sub>anchor: "human capacity must be applied over batches of instances, not over the whole dataset at once"</sub>
- **descriptive / definition**: Capacity constraints are represented by a batch-assignment vector b and a human capacity matrix H of nonnegative integers, where H(b,j) is the number of instances in batch b that expert j can process. (p. 7)[^original]  
  <sub>anchor: "where element _Hb,j_ is a nonnegative integer denoting the number of instances in batch _b_ that human expert _j_ can process"</sub>

## 3.1 Deferral Formulation

- **permissive / method**: By conditioning the model's output on the expert index, the single team model can still adapt to each individual expert's decision-making processes, should that be beneficial. (p. 7)[^original]  
  <sub>anchor: "we still allow the model to adapt to each individual expert’s decision-making processes, should that be beneficial"</sub>
- **descriptive / method**: Per-expert scoring functions would be similar to the approach of Verma et al. (2023), which the authors contrast with their single shared team model. (p. 7)[^original]  
  <sub>anchor: "which would be similar to the approach of Verma et al. (2023)"</sub>

---

[source overview](overview.md) | [next part](digest-002.md)

[^original]: arXiv, "Cost-Sensitive Learning to Defer to Multiple Experts with Workload Constraints" (2024-11-03). https://arxiv.org/abs/2403.06906
