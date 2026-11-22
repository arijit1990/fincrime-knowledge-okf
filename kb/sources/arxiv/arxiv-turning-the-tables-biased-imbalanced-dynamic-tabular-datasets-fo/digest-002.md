---
type: Source Digest
title: 'Turning the Tables: Biased, Imbalanced, Dynamic Tabular Datasets for ML Evaluation - part 2 of 3 (pp. 7-13)'
description: 'Verified paraphrased digest, pp. 7-13: Turning the Tables: Biased, Imbalanced, Dynamic Tabular Datasets for ML Evaluation > 3 The BAF Dataset Suite; Turning the Tables: Biased, Imbalanced, Dynamic Tabular Datasets for ML Evaluation > 4 Empirical Observations; Turning the Tables: Biased, Imbalanced, Dynamic Tabular Datasets for ML Evaluation > 5 Limitations and Intended Uses; and 1 more sections'
resource: https://arxiv.org/abs/2211.13358
tags:
- academic_finding
- data_features
- datasets_benchmarks
- fraud_screening_synergies
- global_academic
- preprint
- responsible_ai
status: stable
source_id: arxiv-turning-the-tables-biased-imbalanced-dynamic-tabular-datasets-fo
issuer: arxiv
issuer_name: arXiv
jurisdictions:
- GLOBAL_ACADEMIC
tier: 3
instrument_type: preprint
normative_force: academic_finding
publication_date: '2022-11-24'
legal_status: unknown
part: 2
parts_total: 3
content_mode: digest
generated:
  by: claude-code-subagent/claude-sonnet-5-5
  at: '2026-11-22T14:46:06Z'
verified:
- by: process:kb-digest-check/anchor-match
  at: '2026-11-22T14:46:06Z'
- by: claude-code-judge-agent/claude-opus-5-5
  at: '2026-11-22T14:46:06Z'
sources:
- id: original
  resource: https://arxiv.org/abs/2211.13358
  title: 'Turning the Tables: Biased, Imbalanced, Dynamic Tabular Datasets for ML Evaluation'
  author: org:arxiv
  last_modified: '2022-11-24T00:00:00Z'
digest_points: 36
---

# Turning the Tables: Biased, Imbalanced, Dynamic Tabular Datasets for ML Evaluation (digest)

[previous part](digest-001.md) | [source overview](overview.md) | [next part](digest-003.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (pp. 7-13) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **academic finding**.

## 3.4 BAF Variants

- **descriptive / context**: The BAF suite contains one base dataset and five additional variants carrying additional controlled data bias patterns; each variant follows the same underlying distribution as the base dataset. (p. 7)[^original]  
  <sub>anchor: "The BAF suites contains one base dataset and 5 additional dataset variants with additional controlled data bias patterns."</sub>
- **descriptive / context**: Apart from prevalence and group disparities in some cases, biases present in the base dataset are also present in the variants, and the goal is to offer a diverse set of algorithmic fairness challenges. (p. 7)[^original]  
  <sub>anchor: "save for prevalence and group disparities in some cases, whatever biases were present in the base dataset are also present in the variants."</sub>
- **descriptive / data or feature**: Table 1 summarises the generated variants with approximate group sizes, prevalence and separability values for the original dataset; values in parentheses apply to the test set. Original: majority 80%, minority 20%, prevalence 1% and 2% respectively. Base: majority 77%, minority 23%, prevalence 0.9% and 1.8%. Global prevalence is 1.8%. (p. 7)[^original]  
  <sub>anchor: "A summary of the generated variants can be found in Table 1."</sub>
- **descriptive / data or feature**: Variant I: majority 90% and minority 10% with equal prevalence of 1.1% in both groups; no separability disparity is listed. (p. 7)[^original]  
  <sub>anchor: "Variant I. Contrary to the Base and Original datasets, the groups in the protected attribute of this variant do not have disparate fraud rates."</sub>
- **descriptive / context**: In Variant I the groups do not have disparate fraud rates, but the minority group shrinks from about 20% of the dataset to 10%, so models must be robust to an even smaller under-explored minority group. (p. 7)[^original]  
  <sub>anchor: "the group size disparity is aggravated, reducing the size of the minority group from approximately 20% of the dataset to 10%."</sub>
- **descriptive / data or feature**: Variant II: groups are equal in size (50%/50%) but prevalence is steeper, with one group having five times the fraud rate of the other (prevalence 0.4% majority and 1.9% minority), instead of about two times; it serves as a stress test for prevalence disparity bias. (p. 7)[^original]  
  <sub>anchor: "one group has five times the fraud rate of the other, instead of approximately two times — while group sizes are equal."</sub>
- **descriptive / data or feature**: Variant III: the separability disparity makes the classification task simpler for the majority group by manipulating correlations between the protected attribute, appended features and the target; groups are balanced in size and prevalence (1.1% each). (p. 8)[^original]  
  <sub>anchor: "This dataset features the Separability disparity presented in Section 3.3, whereby the classification task is made relatively simpler for the majority group"</sub>
- **descriptive / recommendation**: The authors note that this bias type calls for more nuanced interventions, since re-sampling to balance prevalence and group size is ineffective in Variant III because they are already balanced; models must balance countering feature-protected attribute relations with learning useful patterns. (p. 8)[^original]  
  <sub>anchor: "re-sampling the data to balance prevalence and group size is ineffective, as they are already balanced."</sub>
- **descriptive / data or feature**: Variant IV introduces a temporal aspect: like Variant II it has prevalence disparities over the first six months (0.3% majority and 1.7% minority in training, 1.5% for both on the test set) but no disparity for the remainder; group sizes are 50%/50%. (p. 8)[^original]  
  <sub>anchor: "similar to Variant II, it features prevalence disparities over the first six months, but no disparity for the remainder."</sub>
- **descriptive / context**: The authors suggest the observed Variant IV disparity could be caused by a biased training data collection process, and that accounting for such time-varying biases is fundamental because real-world use cases are susceptible to biases outside the practitioner's control. (p. 8)[^original]  
  <sub>anchor: "Taking such aspects into account is fundamental to model realistic dataset variants"</sub>
- **descriptive / data or feature**: Variant V keeps group size and prevalence balanced (1.1% each) but adds a separability bias on the first six months and removes it on the remainder, a feature distribution shift over time in features related to both the protected attribute and the target. (p. 8)[^original]  
  <sub>anchor: "we add a separability bias component on the first six months, and remove it on the remainder."</sub>
- **descriptive / context**: Variant V is analogous to a common fraud detection phenomenon in which fraudsters adapt to detection outcomes; fraud detection is an adversarial classification setting (a subset of performative prediction), so features useful for detection may become obsolete. (p. 8)[^original]  
  <sub>anchor: "fraud detection is an adversarial classification setting [48] (a subset of performative prediction [49])"</sub>
- **descriptive / context**: In Variant V the features that change are related to the protected attribute and the target, which can drastically change the landscape of performance-fairness trade-offs. (p. 8)[^original]  
  <sub>anchor: "In Variant V, these features are related to the protected attribute and the target, which can lead to drastic changes"</sub>

## 4 Empirical Observations

- **descriptive / method**: The authors assessed fairness-blind models by sampling 100 hyperparameter configurations of LightGBM and training them on each dataset, measuring performance as TPR at 5% FPR and fairness as predictive equality (ratio of group FPRs). (p. 8)[^original]  
  <sub>anchor: "we sampled 100 hyperparameter configurations of LightGBM — a popular algorithm for tabular data — and trained them on each dataset."</sub>
- **descriptive / context**: The predictive equality metric is considered appropriate for the punitive setting because a positive classification translates into denial of banking services, and it aims to avoid disproportionately denying legitimate individuals of particular groups access. (p. 8)[^original]  
  <sub>anchor: "This metric is appropriate for our _punitive_ setting [45], as a positive classification translates into denial of banking services."</sub>
- **recommended / recommendation**: The authors strongly encourage practitioners to explore other fairness and performance metrics as well as fairness-aware models on these datasets. (p. 8)[^original]  
  <sub>anchor: "we strongly encourage practitioners to explore other fairness and performance metrics, as well as fairness-aware models on these datasets."</sub>
- **descriptive / finding or result**: Models trained on the datasets, using the first 6 months for training and the rest for testing, occupy significantly different areas of the fairness-accuracy space depending on dataset. (p. 8)[^original]  
  <sub>anchor: "models are distributed in significantly different areas of the fairness-accuracy space, depending on the dataset they were used on."</sub>
- **descriptive / finding or result**: The base dataset alone poses a demanding fairness challenge, with top-performing models around 0.3 FPR ratio, implying older-group applicants are more than three times as likely to be flagged as fraudulent as younger-group applicants. (p. 8)[^original]  
  <sub>anchor: "the top performing models lying around 0.3 FPR ratio."</sub>
- **descriptive / finding or result**: Figure 1 caption: opaque points mark the top 5 models by performance (TPR) on the Base dataset, shown across all variants; the top performing Base models are not necessarily the best on other variants. (p. 8)[^original]  
  <sub>anchor: "Opaque points represent the top 5 models in terms of performance (TPR) in the Base dataset, across all variants."</sub>
- **descriptive / finding or result**: Many models were fairer under Variant I than the baseline, though fairness variance is higher, leaving room for improvement; Variant II fairness matched the baseline, which the authors note as surprising. (p. 9)[^original]  
  <sub>anchor: "many models produced fairer results under Variant 1, when compared to the baseline."</sub>
- **descriptive / finding or result**: Under Variant III, models increased performance at a comparable level of fairness to the base dataset and Variant II. (p. 9)[^original]  
  <sub>anchor: "models under Variant III were able to increase performance, at a comparable level of fairness of the base dataset and Variant II."</sub>
- **descriptive / finding or result**: Model performance deteriorated under Variant IV relative to Variant II, which the authors attribute to learned training-set patterns not carrying over to the test set; Variant V showed a similar but more pronounced degradation and no fairness gains. (p. 9)[^original]  
  <sub>anchor: "model performance deteriorated under the Variant IV variant, relative to its counterpart Variant II."</sub>
- **descriptive / finding or result**: Best-performing models on the baseline were not necessarily the best on the temporal variants IV and V; several other models achieved better fairness-accuracy trade-offs, showing performant static-environment models may fall short in dynamic settings. (p. 9)[^original]  
  <sub>anchor: "several other models achieved better fairness-accuracy trade-offs under these datasets."</sub>
- **descriptive / finding or result**: The authors conclude the suite seems an adequate tool to benchmark fairness and performance of models for static and dynamic environments, and limited analysis to fairness-blind models to encourage experimentation with fairness-aware methods. (p. 9)[^original]  
  <sub>anchor: "the proposed suite seems to be an adequate tool to benchmark the fairness and performance of ML models"</sub>

## 5 Limitations and Intended Uses

- **descriptive / limitation**: The authors identify two main challenges. The first concerns differential privacy guarantees: the original data is aggregated features and the suite is synthetic, so re-identification is not trivial, but it remains a potential issue without theoretical privacy guarantees. (p. 9)[^original]  
  <sub>anchor: "The first regards guarantees of differential privacy."</sub>
- **descriptive / method**: To address privacy, Laplacian noise was applied to the original data's features before training, giving a privacy level depending on the privacy budget; continuous features that could reveal personal information (applicant income and age) were categorically encoded, and no generated instance exactly matched an original instance. (p. 9)[^original]  
  <sub>anchor: "we applied Laplacian noise to the original data’s features prior to training"</sub>
- **descriptive / finding or result**: Differentially private GAN methods PATECTGAN and DPCTGAN did not yield good data utility, which the authors plan to address in future work. (p. 9)[^original]  
  <sub>anchor: "did not yield good results in terms of data utility."</sub>
- **descriptive / limitation**: The second challenge is that many application fields were filled in by the applicant, possibly with wrongful information either intentionally by fraudsters or accidentally by legitimate applicants; the authors know of no solution to this problem. (p. 9)[^original]  
  <sub>anchor: "Many of the fields in applications were filled by the applicant."</sub>
- **descriptive / limitation**: The study used only the original split (initial 6 months for training, remainder for testing); the authors say this can and should be adapted, e.g. with validation data for hyperparameters or thresholds, or a sliding window approach. (p. 9)[^original]  
  <sub>anchor: "These, however, can and should be adapted to other scenarios"</sub>
- **descriptive / method**: The protected attribute age was thresholded at 50, a compromise between group size (approximately 80/20) and prevalence (approximately two times larger for the older group). (p. 9)[^original]  
  <sub>anchor: "we defined a threshold for the studied protected attribute (age), at the value of 50."</sub>
- **descriptive / limitation**: The age threshold of 50 is not intended to be mandatory; other thresholds or group definitions should be taken into consideration. (p. 9)[^original]  
  <sub>anchor: "This threshold, however, is not intended to be mandatory; other thresholds or group definitions should be taken into consideration."</sub>
- **expected / recommendation**: The dataset should only be used for evaluating ML methods and Fair ML interventions, because banking fraud patterns are highly dynamic and context-dependent. (p. 9)[^original]  
  <sub>anchor: "this dataset should only be used for the purpose of evaluating ML methods and Fair ML interventions"</sub>
- **expected / recommendation**: Models trained on this data should not be directly employed in real-world fraud detection scenarios, given the risk of under-performing or outputting biased decisions. (p. 9)[^original]  
  <sub>anchor: "Models trained on this data should not be directly employed in real-world fraud detection scenarios"</sub>

## 4 Empirical Observations

- **descriptive / finding or result**: Under Variant V, models show a performance degradation similar to but more pronounced than under Variant III, and no fairness gains. (p. 9)[^original]  
  <sub>anchor: "show a similar, yet much more pronounced performance degradation phenomenon, and no gains in fairness"</sub>

## 5 Limitations and Intended Uses

- **descriptive / finding or result**: The authors expect that the work will improve the quality of evaluation of novel ML methods. (p. 9)[^original]  
  <sub>anchor: "We expect that with this work, the quality of evaluation of novel ML methods increases"</sub>
- **recommended / recommendation**: The authors encourage other authors and practitioners to experiment with different ML or Fair ML algorithms on this suite and hope it encourages similar datasets from others. (p. 10)[^original]  
  <sub>anchor: "We encourage other authors and practitioners to experiment with different ML or Fair ML algorithms on this suite of datasets."</sub>

---

[previous part](digest-001.md) | [source overview](overview.md) | [next part](digest-003.md)

[^original]: arXiv, "Turning the Tables: Biased, Imbalanced, Dynamic Tabular Datasets for ML Evaluation" (2022-11-24). https://arxiv.org/abs/2211.13358
