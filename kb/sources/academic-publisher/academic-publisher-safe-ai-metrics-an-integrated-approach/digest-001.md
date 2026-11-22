---
type: Source Digest
title: 'SAFE AI metrics: An integrated approach - part 1 of 3 (pp. 1-4)'
description: 'Verified paraphrased digest, pp. 1-4: Machine Learning with Applications > SAFE AI metrics: An integrated approach'
resource: https://doi.org/10.1016/j.mlwa.2025.100821
tags:
- academic_finding
- academic_paper
- explainability
- global_academic
- model_governance
- model_validation
- responsible_ai
status: stable
source_id: academic-publisher-safe-ai-metrics-an-integrated-approach
issuer: academic_publisher
issuer_name: Academic publisher / repository
jurisdictions:
- GLOBAL_ACADEMIC
tier: 3
instrument_type: academic_paper
normative_force: academic_finding
publication_date: '2026-02-25'
legal_status: unknown
part: 1
parts_total: 3
content_mode: digest
generated:
  by: claude-code-subagent/claude-sonnet-5-5
  at: '2026-11-22T14:46:02Z'
verified:
- by: process:kb-digest-check/anchor-match
  at: '2026-11-22T14:46:02Z'
- by: claude-code-judge-agent/claude-opus-5-5
  at: '2026-11-22T14:46:02Z'
sources:
- id: original
  resource: https://doi.org/10.1016/j.mlwa.2025.100821
  title: 'SAFE AI metrics: An integrated approach'
  author: org:academic_publisher
  last_modified: '2026-02-25T00:00:00Z'
digest_points: 43
---

# SAFE AI metrics: An integrated approach (digest)

[source overview](overview.md) | [next part](digest-002.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (pp. 1-4) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **academic finding**.

## 1. Literature review and motivation

- **descriptive / context**: AI governance regulations, guidelines and standards have been developed by regulators, policymakers and standards bodies to address emerging AI risks, but a standardized set of AI risk metrics is still lacking in academic literature and professional practice. (p. 1)[^original]  
  <sub>anchor: "a standardized set of risk metrics for AI systems is still lacking, in both the academic literature and in the professional practice"</sub>
- **descriptive / definition**: Accuracy principle: AI systems make correct predictions, often quantified with RMSE for continuous outcomes and AUC for binary classifications. (p. 1)[^original]  
  <sub>anchor: "it is often quantified using metrics such as Root Mean Squared Error (RMSE) for continuous outcomes"</sub>
- **descriptive / definition**: Fairness principle: AI systems should behave similarly for different population groups, commonly evaluated with parity-based metrics such as demographic parity or equalized odds. (p. 1)[^original]  
  <sub>anchor: "is commonly evaluated using parity-based metrics such as demographic parity or equalized odds"</sub>
- **descriptive / definition**: Explainability principle: the output of AI systems should be understood in terms of its drivers, to allow monitoring and control, and is mostly measured by post-hoc techniques such as Shapley Values and LIME. (p. 1)[^original]  
  <sub>anchor: "is mostly measured by post-hoc techniques such as Shapley Values and LIME"</sub>

## Abstract

- **descriptive / finding or result**: The experimentation on real and simulated datasets shows the integrated metric improves compliance monitoring and enables consistent evaluation of AI risks. (p. 1)[^original]  
  <sub>anchor: "shows that the integrated metric improves compliance monitoring and enables a consistent evaluation of AI risks"</sub>

## 1. Literature review and motivation

- **descriptive / definition**: Babaei et al. (2025) summarised existing governance guidelines and introduced four measurable principles, abbreviated S.A.F.E. The excerpt's first letter is given as Sustainability in the body text, while the abstract refers to Security. (p. 1)[^original]  
  <sub>anchor: "introduced four measurable principles under the acronym S.A.F.E:"</sub>
- **descriptive / definition**: The Sustainability principle, as summarised from Babaei et al. (2025), states that AI systems are robust and resilient to adversarial attacks, such as cyber attacks or data poisoning, and is commonly measured by red teaming procedures. (p. 1)[^original]  
  <sub>anchor: "This principle requires that AI systems are robust and resilient to adversarial attacks"</sub>

## Abstract

- **descriptive / method**: The paper evaluates the outputs of machine learning models under three risk dimensions, each tied to a different input perturbation: data removal (for accuracy), data poisoning (for security) and feature removal (for explainability). (p. 1)[^original]  
  <sub>anchor: "data removal (for accuracy); data poisoning (for security); and feature removal"</sub>

## 1. Literature review and motivation

- **descriptive / finding or result**: Widely used metrics and procedures (red teaming, AUC, RMSE, Shapley values, fairness parity measures) address individual aspects of the S.A.F.E-AI principles but are generally applied in isolation and lack internal consistency, limiting comprehensive assessment of AI risk. (p. 2)[^original]  
  <sub>anchor: "they are generally applied in isolation and lack internal consistency"</sub>
- **descriptive / case example**: Nguyen and Do (2025) introduce RAISE, a unified framework that quantifies performance across explainability, fairness, robustness and sustainability, leading to a unified responsibility score for tabular data that can be traded off against accuracy. (p. 2)[^original]  
  <sub>anchor: "they propose to standardize and integrate the existing individual metrics for the latter four dimension"</sub>
- **descriptive / case example**: Liang et al. (2022) propose a similar multi-metric approach to evaluate Large Language models across seven dimensions: accuracy, calibration, robustness, fairness, bias, toxicity and efficiency. (p. 2)[^original]  
  <sub>anchor: "considering a multi-metric framework that integrates seven dimensions: accuracy, calibration, robustness, fairness, bias, toxicity and efficiency"</sub>
- **descriptive / context**: The advantage of a unified metric approach is a transparent way to evaluate AI outputs, giving a single, interpretable, task-agnostic S.A.F.E-AI score that helps providers, users and regulators monitor and manage AI risks. (p. 2)[^original]  
  <sub>anchor: "which leads to a single, interpretable, and taskagnostic S.A.F.E-AI score"</sub>
- **descriptive / method**: The authors' proposal integrates sustainability, accuracy, fairness and explainability into a single metric, using tabular data as the reference case, but measures all dimensions with one common metric derived from the Lorenz curve and its relationship to the ROC curve, rather than different metrics. (p. 2)[^original]  
  <sub>anchor: "we do not consider different metrics but, rather, measure all dimensions with a common metric"</sub>
- **descriptive / limitation**: A possible disadvantage of the proposal is that it uses new metrics rather than existing ones, which need to be understood, especially in comparison with standard ones. (p. 2)[^original]  
  <sub>anchor: "A possible disadvantage is that we are not using existing metrics but, rather, new ones"</sub>

## 2. Proposal

- **descriptive / method**: The RGB framework of Babaei et al. (2025) consists of three mathematical constructs: the Lorenz curve, the dual Lorenz curve and the concordance curve, which form the basis for the proposed risk and compliance metrics. (p. 2)[^original]  
  <sub>anchor: "consists of three fundamental mathematical constructs: the Lorenz curve, the dual Lorenz curve, and the concordance curve"</sub>
- **descriptive / definition**: The Lorenz curve of Y* is built by arranging Y* values in non-decreasing order, using pairs based on non-decreasing ranks and the mean of Y*; the dual Lorenz curve orders the same Y* values in non-increasing order. (p. 2)[^original]  
  <sub>anchor: "arranging the _𝑌_∗ values in a non-decreasing order"</sub>
- **descriptive / definition**: The concordance curve orders the Y* values according to the ranks of Y**, rather than their own ranks. (p. 2)[^original]  
  <sub>anchor: "A concordance curve C can be constructed by ordering the _𝑌_∗ values not in terms of their own ranks"</sub>
- **descriptive / finding or result**: The concordance curve coincides with the Lorenz curve when the rankings of Y* and Y** are identical, matches the dual Lorenz curve when rankings are perfectly reversed, and the gap between them at any point reflects how far the rank orderings differ. (p. 2)[^original]  
  <sub>anchor: "Importantly, the concordance curve coincides exactly with the Lorenz curve when the rankings"</sub>

## 2.1. Rank Graduation Accuracy (RGA)

- **descriptive / context**: In the NIST Risk Management Framework, accuracy is described as the degree to which results or estimates approximate actual or accepted reference values. (p. 2)[^original]  
  <sub>anchor: "accuracy is described as the degree to which results or estimates approximate actual or accepted reference values"</sub>
- **descriptive / finding or result**: The RGA measure is equal to the AUROC when applied to binary outcomes, and it extends naturally to ordinal and continuous targets. (p. 2)[^original]  
  <sub>anchor: "An important property is that the RGA measure is equal to the AUROC when applied to binary outcomes."</sub>
- **descriptive / definition**: Rank Graduation Accuracy (RGA) is a general, response-agnostic accuracy measure, obtained by dividing the area under the concordance curve by its maximum value; it equals AUROC for binary outcomes and extends to ordinal and continuous targets. (p. 3)[^original]  
  <sub>anchor: "An important property is that the RGA measure is equal to the AUROC when applied to binary outcomes"</sub>
- **descriptive / finding or result**: RGA values lie between 0 and 1: 1 for a perfectly concordant model, 0 for a perfectly discordant model, and 0.5 for random predictions. (p. 3)[^original]  
  <sub>anchor: "with _𝑅𝐺𝐴_ = 1 for a perfectly concordant model"</sub>
- **descriptive / method**: The RGA is decomposed into partial RGA values, each for a segment of the ranked predictions, giving a more detailed view of how parts of the data contribute to overall accuracy. (p. 3)[^original]  
  <sub>anchor: "provides a more detailed view of how different parts of the data contribute to the overall accuracy"</sub>
- **descriptive / method**: Data are removed from highest-ranked to lowest-ranked values; the dataset is split into k equal segments, partial RGA contributions are normalised by the area between dual Lorenz and Lorenz curves so they sum to the full RGA, and a cumulative vector is built by subtracting each slice contribution. (p. 3)[^original]  
  <sub>anchor: "we remove data proceeding from the highestranked values to the lowest-ranked values"</sub>
- **descriptive / method**: The Area Under the Rank Graduation Accuracy Curve (AURGA) is defined from the piecewise constant RGA function over the proportion of highest-ranked segments considered. (p. 3)[^original]  
  <sub>anchor: "The Area Under the Rank Graduation Accuracy Curve (AURGA) and formally write the formula"</sub>
- **descriptive / data or feature**: Figure 2 illustrates RGA for a Random Forest model applied to the California HMDA dataset, used in the application. (p. 3)[^original]  
  <sub>anchor: "Fig. 2 shows an illustration of how RGA can be derived, for a Random Forest model"</sub>

## 2.2. Rank Graduation Robustness (RGR)

- **descriptive / context**: Robustness literature covers adversarial attacks, natural corruptions, distribution shifts and algorithmic stability; this work focuses on adversarial attacks, measuring how performance degrades under systematic perturbations. (p. 3)[^original]  
  <sub>anchor: "In this work, we focus on adversarial attacks by measuring how model performance degrades"</sub>
- **descriptive / definition**: Rank Graduation Robustness (RGR) compares, for each feature, the ranks of predictions on original versus perturbed input, measured as the area under the concordance curve divided by its maximum. (p. 3)[^original]  
  <sub>anchor: "which, for each feature, compares the ranks of predictions on original versus perturbed input"</sub>
- **descriptive / finding or result**: RGR lies between 0 and 1: 1 for a fully robust model, 0 for a fully perturbed model, and 0.5 when perturbations lead to a random model. (p. 3)[^original]  
  <sub>anchor: "with _𝑅𝐺𝑅_ = 1 for a full robust model"</sub>
- **descriptive / finding or result**: Figure 2 shows the Random Forest classifier on the California HMDA dataset outperforms the random baseline in RGA up to 90% data removal. (p. 3)[^original]  
  <sub>anchor: "The Figure shows the superiority of the Random Forest model, up to a 90% data removal."</sub>
- **descriptive / method**: Two perturbation strategies are used: percentile swapping, which swaps values between the lower (p-th percentile) and upper ((1-p)-th percentile) tails of each variable to give distribution-preserving perturbations, and Gaussian noise added to all features simultaneously to simulate measurement errors and sensor noise. (p. 4)[^original]  
  <sub>anchor: "A percentile swapping method introduces controlled, distribution-preserving perturbations"</sub>
- **descriptive / method**: The Area Under the Robustness Curve (AURGR) is proposed as a single summary of robustness, computed from the RGR score plotted against perturbation intensity, which starts at 1 without perturbation and decreases monotonically. (p. 4)[^original]  
  <sub>anchor: "we propose to calculate the Area Under the Robustness Curve (AURGR) as a single summary metric"</sub>
- **descriptive / method**: Perturbation intensities are evaluated from 0% to 50% raw, where 50% means complete tail swapping for percentile swapping or the multiplier of the data standard deviation for Gaussian noise, then normalised by dividing by the maximum value to make AURGR comparable across methods. (p. 4)[^original]  
  <sub>anchor: "We evaluate RGR at raw perturbation intensities ranging from 0% to 50%"</sub>
- **descriptive / finding or result**: Figure 3 shows the Random Forest on the California HMDA dataset under percentile swap perturbation is superior to the random baseline up to 50% data perturbation; the percentile swap curve shows no initial sharp drop because perturbations are localised to extreme values. (p. 4)[^original]  
  <sub>anchor: "The Figure shows the superiority of the Random Forest model, up to a 50% data perturbation."</sub>
- **descriptive / finding or result**: Figure 4 shows the Random Forest on the California HMDA dataset under Gaussian noise perturbation has clear superiority over the random baseline up to a 20% data perturbation; Gaussian noise affects all observations at once and immediately degrades performance. (p. 4)[^original]  
  <sub>anchor: "The Figure shows a clear superiority of the model, up to a 20% data perturbation."</sub>

## 2.3. Rank Graduation Explainability (RGE)

- **descriptive / context**: Explainable AI is increasingly important for trust, safety and meaningful oversight; linear and logistic regression are relatively easy to interpret, whereas random forests and deep neural networks are often seen as black boxes. (p. 4)[^original]  
  <sub>anchor: "modern high-capacity models, such as random forests and deep neural networks, are often seen as"</sub>
- **descriptive / context**: Explainability is usually defined as the ability to represent how an AI system operates in a form understandable to humans, which is vital for user monitoring, intervention and correction. (p. 4)[^original]  
  <sub>anchor: "Explainability is usually defined as the ability to represent how an AI system operates"</sub>
- **descriptive / limitation**: Shapley-based methods, the most popular XAI approach, are computationally demanding and become impractical with a large number of input variables; the RGE metric proposed in Babaei et al. (2025) is presented as overcoming this drawback. (p. 4)[^original]  
  <sub>anchor: "Shapley-based methods are computationally demanding and become impractical when dealing with a large number of input variables"</sub>
- **descriptive / method**: The Area Under the Explainability Curve (AURGE) is proposed as a single summary of explainability, where p is the fraction of features excluded; a reversed RGE is used so the curve starts at 1 with no features removed and ends at 0.5 with all features removed. (p. 4)[^original]  
  <sub>anchor: "We flip the original RGE so that at _𝑝_ = 0 (no features removed) it starts at 1"</sub>
- **descriptive / data or feature**: Figure 5 illustrates RGE derivation using the same Random Forest model and California HMDA dataset as the previous examples. (p. 4)[^original]  
  <sub>anchor: "Fig. 5 shows an illustration of how RGE can be derived using the same Random Forest model"</sub>
- **descriptive / method**: Rank Graduation Explainability (RGE) is obtained by dividing the area under the concordance curve by its maximum value and taking the complement of the result. (p. 4)[^original]  
  <sub>anchor: "The RGE metric is obtained dividing the area under the concordance"</sub>
- **descriptive / definition**: RGE equals 0.5 if the model without the k-th predictor corresponds to the random model, with the concordance curve coinciding with the 45-degree line. (p. 4)[^original]  
  <sub>anchor: "if the model without the _𝑘_ th predictor corresponds to the random model"</sub>
- **descriptive / method**: The paper proposes an Area Under the Explainability Curve (AURGE) as a single summary metric of model explainability, based on the RGE framework. (p. 4)[^original]  
  <sub>anchor: "Based on the RGE framework, we propose the Area Under the Explainability Curve"</sub>

---

[source overview](overview.md) | [next part](digest-002.md)

[^original]: Academic publisher / repository, "SAFE AI metrics: An integrated approach" (2026-02-25). https://doi.org/10.1016/j.mlwa.2025.100821
