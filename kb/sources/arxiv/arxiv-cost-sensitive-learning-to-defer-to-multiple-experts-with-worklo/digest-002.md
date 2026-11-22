---
type: Source Digest
title: Cost-Sensitive Learning to Defer to Multiple Experts with Workload Constraints - part 2 of 5 (pp. 7-14)
description: 'Verified paraphrased digest, pp. 7-14: Cost-Sensitive Learning to Defer to Multiple Experts with Workload Constraints > 3 Method; Cost-Sensitive Learning to Defer to Multiple Experts with Workload Constraints > 4 Experiments; Cost-Sensitive Learning to Defer to Multiple Experts with Workload Constraints > 5 Results'
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
part: 2
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
digest_points: 46
---

# Cost-Sensitive Learning to Defer to Multiple Experts with Workload Constraints (digest)

[previous part](digest-001.md) | [source overview](overview.md) | [next part](digest-003.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (pp. 7-14) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **academic finding**.

## 3.3 Global Loss Minimization under Capacity Constraints

- **descriptive / finding or result**: The point-wise classifier-rejector formulation yields optimal solutions that ignore work-capacity limits; if one expert were more likely correct than all colleagues and the ML classifier everywhere, the point-wise optimum would defer every instance to that expert, which is infeasible in practice. (p. 7)[^original]  
  <sub>anchor: "Should an expert be more likely to be correct than all their colleagues and the ML classifier over the entire feature space"</sub>
- **descriptive / context**: The authors state that a point-wise formulation is inadequate for optimising assignments over a set of instances under expert capacity constraints, but the calibrated scoring functions from training remain useful for estimating probabilities of correctness. (p. 7)[^original]  
  <sub>anchor: "A point-wise formulation of _h_ˆ and _r_ ˆ is clearly inadequate to optimize the assignments over a set of instances"</sub>
- **descriptive / method**: The assignment decision for each instance takes one of J+2 values: values 1 and 2 represent automatic prediction of class 0 or 1, and value j+2 represents deferral to the j-th expert. (p. 7)[^original]  
  <sub>anchor: "where _ai_ = _y_ + 1, with _y ∈Y_ , is an automatic prediction of class _y_ for instance _i_"</sub>
- **descriptive / method**: Assignments for a batch of nB instances are represented by a binary nB x (2+J) matrix A, where each element indicates whether a given decision is taken for a given instance. (p. 8)[^original]  
  <sub>anchor: "consider the _nB ×_ (2+ _J_ ) matrix of assignments _A_ , where each element _Ai,ai_ is a binary variable"</sub>
- **descriptive / method**: The first constraint enforces human capacity with an equality constraint on the number of instances per decision-maker, which may be relaxed to an inequality giving a maximum; the second requires each instance to be assigned to exactly one decision-maker. (p. 8)[^original]  
  <sub>anchor: "this constraint may be changed to an inequality expressing the maximum number of assignments per decision-maker"</sub>
- **descriptive / method**: The assignment problem is solved with the CP-SAT constraint programming solver from Google Research's OR-Tools. (p. 8)[^original]  
  <sub>anchor: "We solve the assignment problem 9 using the constraint programming solver CP-SAT from Google Research’s OR-Tools"</sub>
- **descriptive / context**: The authors note that solution times for these combinatorial problems grow exponentially with problem size. (p. 8)[^original]  
  <sub>anchor: "as solution times grow exponentially with the problem’s size"</sub>
- **descriptive / context**: CP-SAT is a parallel portfolio solver that runs different search strategies on the available cores, on the assumption that different heuristics may compensate for each other's weaknesses. (p. 8)[^original]  
  <sub>anchor: "CP-SAT is a parallel portfolio solver, leveraging the available processor cores to run different solution search strategies"</sub>
- **descriptive / context**: CP-SAT was chosen because it has repeatedly been shown to be the best-performing publicly available solver across many constraint programming problems in the MiniZinc challenge, which seeks optimal or near-optimal solutions within a time limit. (p. 8)[^original]  
  <sub>anchor: "We selected CP-SAT in our implementation as it has been repeatedly shown to be the bestperforming publicly available solver"</sub>
- **descriptive / finding or result**: Although feasible solutions are found quickly, proving optimality can take very long, so a time limit is often set; on the authors' machine no significant improvements were obtained for timeout limits above 60 seconds. (p. 8)[^original]  
  <sub>anchor: "no significant improvements were obtained for timeout limits above 60 seconds"</sub>

## 3.4 Cost-Sensitive Learning

- **descriptive / method**: Cost sensitivity is handled by instance re-weighting, multiplying each point-wise training loss by the instance's misclassification cost, so that surrogate loss minimisation targets misclassification cost rather than error rate. (p. 8)[^original]  
  <sub>anchor: "where each point-wise loss over the training set is multiplied by the cost _ci_ associated with said instance"</sub>
- **descriptive / definition**: The paper notes that instances may have different misclassification costs, in which case a surrogate for the 0-1 loss is not adequate. (p. 8)[^original]  
  <sub>anchor: "instances may have different misclassification costs, in which case a surrogate for the 0-1 loss is not adequate"</sub>
- **descriptive / method**: Assuming each instance has an associated misclassification cost, the goal is to learn a classifier that minimises the expected cost rather than the 0-1 error. (p. 8)[^original]  
  <sub>anchor: "Assuming that each instance _x_ _i_ has an associated misclassification cost _ci_ , the goal is then to learn a classifier that minimizes the expected cost"</sub>
- **descriptive / method**: Following Zadrozny et al. (2003), minimising error rate under a re-weighted distribution is equivalent to minimising expected misclassification cost under the original distribution, so the classifier is trained on the re-weighted distribution using log-loss. (p. 9)[^original]  
  <sub>anchor: "selecting the decision rule _h_ to minimize the error rate under _D_˜ is equivalent to selecting _h_ to minimize the expected misclassification cost"</sub>
- **descriptive / method**: The scoring function g is trained by re-weighting the log-loss instances, and the rejector g⊥ is trained by re-weighting the HEM loss. (p. 9)[^original]  
  <sub>anchor: "We follow the same approach with respect to the rejector, reweighting the instances in _L_ HEM"</sub>
- **descriptive / method**: The Minimize-Loss step may be any optimisation algorithm minimising an empirical loss, such as gradient descent or gradient boosting. (p. 9)[^original]  
  <sub>anchor: "the function “Minimize-Loss” represents any optimization algorithm that minimizes an empirical loss"</sub>

## 4.1 Experimental Setup

- **descriptive / data or feature**: The base dataset is the publicly available bank-account-fraud dataset (Version 1) of about one million synthetically generated bank account opening applications, labelled fraudulent (1) or legitimate (0), generated from anonymised real applications. (p. 9)[^original]  
  <sub>anchor: "This tabular dataset is comprised of one million synthetically generated bank account opening applications"</sub>
- **descriptive / data or feature**: The decision maker either accepts (0) or rejects (1) each application. (p. 9)[^original]  
  <sub>anchor: "the task of a decision maker (automated or human) is to either accept (0) or reject (1) it"</sub>
- **descriptive / data or feature**: The dataset has high class imbalance, with 1.1% fraud prevalence, and its data distribution changes over time (concept drift), which can severely affect predictive performance. (p. 9)[^original]  
  <sub>anchor: "with 1.1% fraud prevalence over the entire dataset"</sub>
- **descriptive / method**: Algorithm 2 (DeCCaF inference for a batch) fills a probability matrix from the classifier and rejector scoring functions, then solves the assignment optimisation with the CP solver under the batch capacity constraints. (p. 10)[^original]  
  <sub>anchor: "Optimization Problem in (7)"</sub>
- **descriptive / context**: In alert review settings, an Alert Model screens instances and only flagged instances are reviewed by humans, so humans predict on only a fraction of the feature space; the L2D system works alongside the Alert Model. (p. 10)[^original]  
  <sub>anchor: "In an alert review setting, humans only predict on a fraction of the feature space"</sub>
- **descriptive / method**: The alert rate is the fraction of instances flagged for human review, determined by the false positive rate of the Alert Model on validation; two scenarios are used, 5% FPR and 15% FPR. (p. 10)[^original]  
  <sub>anchor: "We create distinct alert review scenarios by varying the alert rate _ar ∈{_ 5%FPR _,_ 15%FPR _}_"</sub>
- **descriptive / method**: The Alert Model is a LightGBM classifier trained to predict fraud on the first three months of data and validated on the fourth month. (p. 10)[^original]  
  <sub>anchor: "We train the Alert Model to predict the fraud label on the first three months of the dataset"</sub>
- **descriptive / context**: The task is cost-sensitive: wrongly rejecting a legitimate application (false positive) must be weighed against wrongly accepting a fraudulent one (false negative); accuracy is considered inadequate given low fraud prevalence. (p. 10)[^original]  
  <sub>anchor: "Due to the low fraud prevalence, metrics such as accuracy are not adequate to measure the performance"</sub>
- **descriptive / context**: Jesus et al. (2022) optimised a Neyman-Pearson criterion, maximising recall at 5% FPR, which implicitly fixes a relationship between false positive and false negative costs; the cost-sensitive method needs an explicit cost structure. (p. 10)[^original]  
  <sub>anchor: "The optimization objective used by Jesus et al. (2022) is a Neyman-Pearson criterion"</sub>
- **descriptive / method**: The cost ratio lambda equals the false positive cost divided by the false negative cost, with correct classifications carrying no cost, and the objective is to minimise expected misclassification cost. (p. 10)[^original]  
  <sub>anchor: "the relevant parameter is the ratio _λ_ = _c_ FP _/c_ FN"</sub>
- **descriptive / finding or result**: The approach in Appendix A.2 gives a theoretical cost ratio lambda_t of 0.057. (p. 10)[^original]  
  <sub>anchor: "which yields the theoretical value _λt_ = 0 _._ 057"</sub>
- **descriptive / method**: Experiments test cost ratios lambda_t/5, lambda_t and 5 lambda_t (about 0.0114, 0.057 and 0.285), which combined with the two alert rates give six scenarios; the authors note these variations are not strictly comparable with the Neyman-Pearson optimisation. (p. 11)[^original]  
  <sub>anchor: "Combining the different alert rates with these values of _λ_ , we obtain 6 distinct text scenarios"</sub>
- **descriptive / method**: Synthetic expert decisions are generated with instance-dependent noise, so each label is flipped with a probability that depends on the instance features and, where applicable, on the Alert Model score. (p. 11)[^original]  
  <sub>anchor: "Our expert generation approach is based on _instance-dependent noise_"</sub>
- **descriptive / method**: Each expert's error probabilities are a sigmoid function of pre-processed features and the Alert Model score, governed by five parameters (beta0, beta1, alpha, w, wM), with alpha controlling feature dependence and beta0 and beta1 the base error probability. (p. 11)[^original]  
  <sub>anchor: "Each expert’s probabilities of the two types of error depend on five parameters"</sub>
- **descriptive / requirement**: The authors assume that an expert's decisions must, on average, incur a lower cost than automatically rejecting all flagged transactions, so that the setup is realistic. (p. 11)[^original]  
  <sub>anchor: "we assume an expert’s decisions must, on average, incur a lower cost than simply automatically rejecting all flagged transactions"</sub>
- **descriptive / method**: In each of the six settings a different team of 9 synthetic experts is generated by fixing feature weights and sampling expected misclassification cost, then solving for beta0 and beta1. (p. 12)[^original]  
  <sub>anchor: "we generate a different team of 9 synthetic experts by first fixing their feature weights _w_"</sub>
- **descriptive / method**: Expert data availability is simulated by deploying the Alert Model in months 4-7 and deferring each alert to a randomly chosen expert, yielding one expert prediction per instance, with 5 random seeds per scenario. (p. 12)[^original]  
  <sub>anchor: "we assume that the Alert Model is deployed in months 4-7, and that each alert is deferred to a randomly chosen expert"</sub>
- **descriptive / method**: Capacity is enforced so that the assigner distributes instances equally among the 9 experts and the classifier, giving 1/10 of the test set to each, since querying the classifier is much cheaper than querying a human. (p. 12)[^original]  
  <sub>anchor: "this means that 1/10 of the test set will be deferred to each expert/classifier"</sub>
- **descriptive / method**: Four test capacity settings sample each expert/classifier capacity from a normal distribution N(Ntest/10, Ntest/50), giving 25 test variations per scenario from 5 training seeds crossed with these settings. (p. 12)[^original]  
  <sub>anchor: "we also create four distinct test settings where each expert/classifier has a different capacity"</sub>

## 4.2 Baselines

- **descriptive / method**: The One vs. All (OvA) baseline is the multi-expert learning-to-defer method of Verma et al. (2023), with a classifier over K classes and a rejector over J experts, adapted to cost sensitivity via the rescaling approach. (p. 12)[^original]  
  <sub>anchor: "we use the multi-expert learning to defer OvA algorithm, proposed by Verma et al. (2023)"</sub>

## 4.1 Experimental Setup

- **descriptive / data or feature**: Each expert in the 5% FPR alert rate settings receives a set of 2.9K predictions, and for the 15% FPR settings 2.9K predictions are sampled from each expert so that all scenarios have the same amount of data. (p. 12)[^original]  
  <sub>anchor: "this results in a set of 2.9K predictions per expert"</sub>
- **descriptive / data or feature**: The source refers to the expert team as 9 experts in the expert-team description and also mentions sampling from 10 experts for the 15% FPR scenarios, an inconsistency as written. (p. 12)[^original]  
  <sub>anchor: "we also sample 2.9K predictions from each of the 10 experts"</sub>

## 4.2 Baselines

- **descriptive / method**: Because the OvA method does not support capacity constraints, it defers to the highest-scoring rejector expert and, when that expert's capacity is exhausted, to the second-highest, and so on. (p. 13)[^original]  
  <sub>anchor: "If the capacity of the selected expert is exhausted, deferral is done to the second highest scoring expert"</sub>
- **descriptive / method**: The Random Assignment baseline defers alerts randomly across experts and model until each capacity constraint is met, representing average team performance. (p. 13)[^original]  
  <sub>anchor: "alert deferral is done randomly throughout the experts/model until each of their capacity constraints are met"</sub>
- **descriptive / method**: The Only Classifier baseline makes all final decisions on alerts with the classifier h, and the Full Rejection baseline automatically rejects all alerts. (p. 13)[^original]  
  <sub>anchor: "In this baseline, all final decisions on the alerts are made by the classifier _h_"</sub>

## 4.3 Deferral System Training

- **descriptive / method**: The classifier h and the HEM are LightGBM models trained on alerts from months 4 to 6 and validated on month 7, selected to minimise weighted log-loss with weight 1 for positives and lambda for negatives. (p. 13)[^original]  
  <sub>anchor: "trained on the sample of alerts raised over months 4 to 6, and validated on month 7"</sub>
- **descriptive / method**: For OvA, the training set is split by each expert's predictions to fit each rejector scoring function, and the same classifier h is used for both deferral systems. (p. 13)[^original]  
  <sub>anchor: "we will use the same classifier _h_ for both deferral systems"</sub>

## 5.1 Classifier h - Performance and Calibration

- **descriptive / finding or result**: Classifier h ROC-AUC is about 0.70 to 0.76 across scenarios, with expected calibration error (ECE) ranging from 1.1% (alert rate 0.05, lambda 0.011) to 4.8% (alert rate 0.05, lambda 0.057). (p. 13)[^original]  
  <sub>anchor: "expected calibration error (ECE) and ROC-AUC for classifier _h_ for all testing scenarios"</sub>

## 5.2 Expert Decision Modeling - Performance and Calibration

- **descriptive / method**: Expert correctness models (HEM and OvA rejectors) are evaluated by ROC-AUC for each individual expert per training seed, and then by calibration, under the re-weighted distribution. (p. 13)[^original]  
  <sub>anchor: "We will again check that the scoring functions _g⊥_ (HEM) and _g⊥,j_ (OvA) are able to model individual expert correctness"</sub>
- **descriptive / finding or result**: The authors find the cost ratio λ has a significant impact on the two methods' ranking in terms of calibration, which they present as showing the importance of testing L2D methods across a wide variety of cost structures. (p. 14)[^original]  
  <sub>anchor: "showing the importance of testing L2D methods under a wide variety of cost-structures"</sub>

---

[previous part](digest-001.md) | [source overview](overview.md) | [next part](digest-003.md)

[^original]: arXiv, "Cost-Sensitive Learning to Defer to Multiple Experts with Workload Constraints" (2024-11-03). https://arxiv.org/abs/2403.06906
