---
type: Source Digest
title: 'FiFAR: A Fraud Detection Dataset for Learning to Defer - part 3 of 3 (pp. 5-8)'
description: 'Verified paraphrased digest, pp. 5-8: 4.2 Baselines; 4.3 Results; 5 CONCLUSIONS AND FUTURE WORK; and 1 more sections'
resource: https://arxiv.org/abs/2312.13218
tags:
- academic_finding
- alerts_triage
- global_academic
- ml_statistics
- model_development
- preprint
status: stable
source_id: arxiv-fifar-a-fraud-detection-dataset-for-learning-to-defer
issuer: arxiv
issuer_name: arXiv
jurisdictions:
- GLOBAL_ACADEMIC
tier: 3
instrument_type: preprint
normative_force: academic_finding
publication_date: '2023-12-20'
legal_status: unknown
part: 3
parts_total: 3
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
  resource: https://arxiv.org/abs/2312.13218
  title: 'FiFAR: A Fraud Detection Dataset for Learning to Defer'
  author: org:arxiv
  last_modified: '2023-12-20T00:00:00Z'
digest_points: 28
---

# FiFAR: A Fraud Detection Dataset for Learning to Defer (digest)

[previous part](digest-002.md) | [source overview](overview.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (pp. 5-8) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **academic finding**.

## 4.2 Baselines

- **descriptive / context**: The authors found no current learning-to-defer method able to account for individual expert capacity constraints, so they provide three baselines. (p. 5)[^original]  
  <sub>anchor: "we found no current method able to take individual capacity constraints into account"</sub>
- **descriptive / method**: Rejection Learning (ReL) uses the model score as a measure of model confidence and, applied batch-wise within capacity constraints, orders cases in each batch by descending model score. (p. 5)[^original]  
  <sub>anchor: "we use the model score as a measure of model confidence"</sub>
- **descriptive / method**: In the ReL baseline, the top 5% of cases in a batch by model score are automatically predicted positive (declined). (p. 5)[^original]  
  <sub>anchor: "The top 5% cases are automatically predicted positive (declined)."</sub>
- **descriptive / method**: In the ReL baseline, the following cases are randomly assigned to experts in the team until their capacity constraints are met, and all left-over cases with the lowest model score are classified negatively (accepted). (p. 5)[^original]  
  <sub>anchor: "Then, the following cases are randomly assigned to experts within our team until their capacity constraints are met."</sub>
- **descriptive / method**: Human Expertise Aware Rejection Learning instead of random assignment models each expert's behaviour to optimise assignments, training a LightGBM model on instance features and expert_id to predict whether the expert's prediction is a false positive, false negative, true positive or true negative. (p. 5)[^original]  
  <sub>anchor: "we train a LightGBM model on the instance features and the expert_id to predict"</sub>
- **descriptive / method**: The human-expertise model yields, for each instance, predicted probabilities that the expert makes a false positive or a false negative mistake, used to calculate the predicted loss of deferring an instance to an expert. (p. 5)[^original]  
  <sub>anchor: "For each instance, we then have a prediction for the probability that the expert will make either a FP, or a FN mistake"</sub>
- **descriptive / method**: The Greedy variant (ReLgreedy) moves through the batch case by case, assigning each case to the expert with lowest predicted loss, falling back to the next-lowest-loss expert when capacity constraints would be violated, until constraints are met. (p. 5)[^original]  
  <sub>anchor: "The algorithm moves through the batch case by case, assigning each case to the expert with lowest predicted loss."</sub>
- **descriptive / method**: The Integer Linear Programming variant (ReLlinear) minimises loss over an entire batch by solving a linear programming problem subject to capacity constraints to find the optimal batch assignment. (p. 5)[^original]  
  <sub>anchor: "we minimize the loss over an entire batch by solving a linear programming problem subject to our capacity constraints"</sub>
- **descriptive / definition**: For fairness, predictive equality (PE) is measured as the ratio of false positive rates across age groups, computed by dividing the lowest group FPR by the highest group FPR. (p. 5)[^original]  
  <sub>anchor: "The ratio is calculated by dividing the FPR of the group with lowest observed FPR by the FPR of the group with the highest FPR."</sub>

## 4.3 Results

- **descriptive / finding or result**: Table 1 compares the three L2D baselines with a 'Model only' system across scenarios, using cost-sensitive loss and predictive equality as metrics. (p. 6)[^original]  
  <sub>anchor: "In Table 1 we show results for the discussed L2D baselines as well as a “Model only” system."</sub>
- **descriptive / finding or result**: Across all considered scenarios, rejection learning performed best, despite the attempts to model human behaviour. (p. 6)[^original]  
  <sub>anchor: "throughout all the considered scenarios, rejection learning performs best, despite our attempts to model human behavior"</sub>
- **descriptive / limitation**: The authors suggest the poor performance of the expertise-modelling variants may stem from the low volume of false negatives and true positives in training data, leading to poor probability estimates and ranking of expert error probability. (p. 6)[^original]  
  <sub>anchor: "This may be due to the low volume of FNs and TPs in the training data"</sub>
- **descriptive / finding or result**: Appendix Table 6 shows the proposed methods mostly mitigate FP errors, lowering FPR but negatively impacting recall. (p. 6)[^original]  
  <sub>anchor: "our methods mostly mitigate FP errors, resulting in a lower FPR, but negatively impacting the recall as well"</sub>
- **descriptive / finding or result**: Reducing false positives led to higher predictive equality, which the authors interpret as the expertise model learning that experts make more FP mistakes on older clients' applications. (p. 6)[^original]  
  <sub>anchor: "experts tend to make more FP mistakes on older clients’ applications"</sub>
- **descriptive / finding or result**: Table 2 varies the pool of available experts; ReLlinear outperforms ReL when the pool contains only agreeing, sparse or unfair experts. (p. 6)[^original]  
  <sub>anchor: "ReLlinear outperforms ReL when the expert pool contains only agreeing, sparse or unfair experts."</sub>
- **descriptive / finding or result**: The authors suggest ReLlinear's advantage may be because these experts are simpler to model, having a clear dominating feature or simpler feature dependencies. (p. 6)[^original]  
  <sub>anchor: "as they have a clear dominating feature, or simpler feature dependencies"</sub>
- **descriptive / recommendation**: The authors conclude it is important to consider variable complexity of human behaviour when evaluating human-AI collaboration systems. (p. 6)[^original]  
  <sub>anchor: "This illustrates the importance of considering variable complexity of human behavior when evaluating HAIC systems."</sub>
- **descriptive / finding or result**: For ReLlinear, the authors report that expert absence appeared to have no significant effect on loss at a 20% deferral rate, but at a 50% deferral rate it appeared to significantly increase loss. (p. 6)[^original]  
  <sub>anchor: "in the cases with 50% deferral rate, it seems that introducing expert absence significantly increases the loss"</sub>
- **descriptive / context**: The authors state that the ReLlinear result illustrates the importance of testing the system under a wide variety of conditions. (p. 6)[^original]  
  <sub>anchor: "This illustrates the importance of testing the system under a wide variety of conditions."</sub>

## 5 CONCLUSIONS AND FUTURE WORK

- **descriptive / finding or result**: The paper introduces the FiFAR Dataset and illustrates its use with three L2D baselines tested under 300 different scenarios, enabling benchmarking of L2D algorithms under real-world constraints. (p. 7)[^original]  
  <sub>anchor: "we provide three L2D baselines tested under 300 different scenarios"</sub>
- **descriptive / limitation**: The main limitation is that the baselines do not include established L2D literature methods, as these do not currently consider capacity constraints. (p. 7)[^original]  
  <sub>anchor: "The main limitation of our work is that our baselines do not include any established methods in the L2D literature"</sub>
- **descriptive / limitation**: The authors state their synthetic experts cannot replace humans in human-AI collaboration systems, since real expert data would be needed to train a real-world system. (p. 7)[^original]  
  <sub>anchor: "our synthetic experts can not replace, in any way, humans involved in HAIC systems"</sub>
- **expected / expectation**: Where human predictions are accessible and pertinent to the use case, researchers should prefer real human predictions over synthetic expert predictions. (p. 7)[^original]  
  <sub>anchor: "researchers should prefer these over synthetic expert predictions, as they constitute real human behavior"</sub>
- **descriptive / limitation**: Synthetic experts may amplify biases because they establish a monotonic relationship between each feature and error probabilities. (p. 7)[^original]  
  <sub>anchor: "our synthetic experts may amplify biases, due to the fact that they establish a monotonic relationship between each feature and the probabilities of error"</sub>
- **descriptive / limitation**: Increasing the weight of a feature correlated with a protected attribute could make a synthetic expert with a positive weight for that feature in false positive probability show higher bias against the protected group. (p. 7)[^original]  
  <sub>anchor: "an expert with a positive weight for said feature in the false positive probability would exhibit a higher bias against said protected group"</sub>
- **recommended / recommendation**: A careful analysis of the final predictive equality of each synthetic expert is encouraged. (p. 7)[^original]  
  <sub>anchor: "a careful analysis of the final predictive equality of each expert is encouraged"</sub>
- **descriptive / context**: It can be argued that using synthetic experts for research may affect the livelihood of large-scale annotation workers such as MTurk, which researchers often use. (p. 7)[^original]  
  <sub>anchor: "we are affecting the livelihood of large-scale annotation workers (i.e. MTurk)"</sub>
- **descriptive / limitation**: The authors note that in some use cases requiring domain-specific expertise, annotation services may not be adequate, and obtaining real human expert data may be impossible or unfeasible. (p. 7)[^original]  
  <sub>anchor: "such annotation services may not be adequate, and it may be impossible/unfeasible to obtain real human expert data"</sub>

---

[previous part](digest-002.md) | [source overview](overview.md)

[^original]: arXiv, "FiFAR: A Fraud Detection Dataset for Learning to Defer" (2023-12-20). https://arxiv.org/abs/2312.13218
