---
type: Source Digest
title: 'SAFE AI metrics: An integrated approach - part 3 of 3 (pp. 9-13)'
description: 'Verified paraphrased digest, pp. 9-13: Machine Learning with Applications > SAFE AI metrics: An integrated approach'
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
part: 3
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
digest_points: 29
---

# SAFE AI metrics: An integrated approach (digest)

[previous part](digest-002.md) | [source overview](overview.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (pp. 9-13) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **academic finding**.

## Abstract

- **descriptive / finding or result**: For Swapping perturbations, the arithmetic mean aggregation gives relatively right-skewed, bell-shaped distributions across all six models, the geometric mean gives right-skewed distributions with longer tails, and the RMS values give bimodal distributions with two unclear peaks, suggesting two distinct subgroups or performance regimes. (p. 9)[^original]  
  <sub>anchor: "the arithmetic mean is relatively right-skewed and bell-shaped distributions across all six models"</sub>
- **descriptive / finding or result**: The contrasting responses to different perturbation types are consistent across all analysed datasets, and different models excel under different perturbation regimes. (p. 9)[^original]  
  <sub>anchor: "These contrasting responses to different perturbation types are consistent across all analyzed datasets"</sub>
- **descriptive / context**: Arithmetic Mean captures general performance, Geometric Mean emphasizes balanced improvements across dimensions, RMS highlights variance sensitivity, and TOPSIS provides distance-based ranking. (p. 9)[^original]  
  <sub>anchor: "While Arithmetic Mean captures general performance, Geometric Mean emphasizes balanced improvements across dimensions"</sub>
- **permissive / recommendation**: The multi-aggregation approach can enable informed candidate selection for credit lending applications where accuracy, explainability and robustness must be optimised together under realistic perturbation scenarios. (p. 9)[^original]  
  <sub>anchor: "This approach can enable informed candidate selection for credit lending applications"</sub>
- **descriptive / data or feature**: Figure 11 shows Rank Graduation Accuracy (RGA), Rank Graduation Explainability (RGE) and Rank Graduation Robustness (RGR) curves for the California HMDA dataset under Swapping; these three curves are the basis of the unified metric. (p. 9)[^original]  
  <sub>anchor: "The three curves are the basis of the unified metric."</sub>
- **descriptive / data or feature**: Figure 12 shows arithmetic mean histograms for the California HMDA dataset under Swapping, indicating integrated performance of all models. (p. 9)[^original]  
  <sub>anchor: "Arithmetic Mean Histograms for the California HMDA dataset (Swapping)"</sub>
- **descriptive / method**: In the sensitivity test, a dominant weight of 0.9 is given to one dimension (accuracy, robustness or explainability) and weights of 0.05 to each of the other two; the resulting ranking should theoretically align with the raw ranking of the emphasised criterion. (p. 9)[^original]  
  <sub>anchor: "the resulting ranking should theoretically align with the raw ranking of the emphasized criterion"</sub>
- **descriptive / finding or result**: The authors say the contradictory patterns in compliance scores, where different models excel under different perturbation regimes, indicate that further research is needed to develop unified model selection frameworks. (p. 9)[^original]  
  <sub>anchor: "indicate that further research is needed to develop unified model selection frameworks"</sub>
- **descriptive / method**: The weight validation uses one representative dataset (New York HMDA) and one integration method for simplicity, under three weighting scenarios: Accuracy Focus, Robustness Focus and Explainability Focus, each giving 0.9 to one dimension and 0.05 to the other two. (p. 10)[^original]  
  <sub>anchor: "we show this on one representative dataset and for one integration method"</sub>
- **descriptive / finding or result**: The authors report that the framework responds correctly to weight adjustments, with model rankings shifting to reflect the emphasised dimension, which they take to show weighted aggregation can be integrated into the compliance framework. (p. 11)[^original]  
  <sub>anchor: "The results confirm that the framework correctly responds to weight adjustments"</sub>

## 5. Conclusions

- **descriptive / definition**: The work develops a unified framework for measuring S.A.F.E-AI system trustworthiness across multiple risk dimensions, introducing three novel metrics. (p. 11)[^original]  
  <sub>anchor: "developing a unified framework for measuring S.A.F.E-AI system trustworthiness across multiple risk dimensions"</sub>
- **descriptive / definition**: AURGA (Area Under the Rank Graduation Accuracy Curve) evaluates performance consistency by measuring accuracy degradation as the highest- to lowest-ranked predictions are progressively removed. (p. 11)[^original]  
  <sub>anchor: "The metric captures how accuracy changes when progressively removing contributions from the highest- to lowest-ranked predictions."</sub>
- **descriptive / definition**: AURGR (Area Under the Rank Graduation Robustness Curve) assesses model stability under data perturbations using both Swapping and Gaussian noise approaches. (p. 11)[^original]  
  <sub>anchor: "Assesses model stability under data perturbations using both Swapping and Gaussian noise approaches."</sub>
- **descriptive / definition**: AURGE (Area Under the Rank Graduation Explainability Curve) evaluates transparency by systematically removing features and measuring the impact on explanatory power, using a greedy approach that captures how rapidly explainability is lost. (p. 11)[^original]  
  <sub>anchor: "Evaluates model transparency by systematically removing features and measuring the impact on explanatory power"</sub>

## Abstract

- **permissive / recommendation**: The authors state that weighted aggregation can be integrated into the compliance framework in future applications, so organisations can tailor model selection to their regulatory requirements, risk appetite or operational priorities. (p. 11)[^original]  
  <sub>anchor: "can be naturally integrated into the compliance framework in future applications"</sub>

## Conclusions

- **permissive / expectation**: The authors note that the analysis could be conducted for classification problems in other fields such as health care and manufacturing, not only the credit lending database used. (p. 12)[^original]  
  <sub>anchor: "similar analysis can be conducted for classification problems arising in other fields, such as health care and manufacturing"</sub>

## Declaration of competing interest

- **descriptive / finding or result**: Model selection for compliance scoring requires a multi-faceted evaluation accounting for absolute performance and relative stability; compliance performance depends on perturbation type. (p. 12)[^original]  
  <sub>anchor: "model selection for compliance scoring applications requires a nuanced, multi-faceted evaluation"</sub>
- **descriptive / finding or result**: Linear models are more resilient to Gaussian noise but more vulnerable to Swapping perturbations, whereas tree-based models show the opposite trend. (p. 12)[^original]  
  <sub>anchor: "Linear models exhibit resilience to Gaussian noise but are more vulnerable to Swapping perturbations"</sub>
- **descriptive / data or feature**: The proposed Compliance Score framework integrates Arithmetic Mean, Geometric Mean, RMS and TOPSIS aggregation methods and is adaptable to organisational priorities through weighted schemes. (p. 12)[^original]  
  <sub>anchor: "integrates multiple aggregation methods (Arithmetic Mean, Geometric Mean, RMS, and TOPSIS)"</sub>
- **descriptive / finding or result**: The strong correlation between RGE scores and Shapley values supports the validity of the perturbation-based explainability approach, though discrepancies for lower-ranked features suggest further investigation is needed. (p. 12)[^original]  
  <sub>anchor: "The strong correlation between RGE scores and Shapley values supports the validity"</sub>
- **permissive / recommendation**: Auditors and regulators could use the unified metric to assess the compliance of any AI application and highlight where compliance should be improved, for example in security, accuracy, explainability and fairness regarding explainability of protected variables. (p. 12)[^original]  
  <sub>anchor: "the unified metric provides a clear tool that can be employed by auditors and regulators to assess the compliance"</sub>
- **permissive / recommendation**: Auditors and regulators could give different weights to the four dimensions in line with evolving policies and their implementations, referring to European Commission (2023) and NIST (2023). (p. 12)[^original]  
  <sub>anchor: "The same auditors and regulators could also give different weights to the four dimensions"</sub>
- **expected / limitation**: The proposal should be extended beyond tabular data to consider image processing, natural language processing and large language models, as in Liang et al. (2022). (p. 12)[^original]  
  <sub>anchor: "the proposal should be extended beyond tabular data, to consider, for example, image processing and natural language processing and large language models"</sub>

## Table 10

- **descriptive / finding or result**: In Table 10 the Random baseline shows accuracy-focus AURGA 0.3024 and TOPSIS 0.30114, and explainability-focus TOPSIS 0.21793; its robustness and explainability rank entries appear garbled in the extracted text (printed as 71.000 and 11.000), so they cannot be reliably read. (p. 12)[^original]  
  <sub>anchor: "Random|0.3024|0.30114|71.000|0.93164|11.000|0.21793|1|"</sub>

## Declaration of competing interest

- **expected / limitation**: The authors state that their proposal should be compared with methods that integrate individual existing metrics, such as Nguyen and Do (2025), in real case scenarios. (p. 12)[^original]  
  <sub>anchor: "our proposal should be compared with methods that integrate individual existing metrics, such as Nguyen and Do (2025)"</sub>
- **descriptive / limitation**: Reconciling conflicting model recommendations when different perturbation scenarios favour different architectures is identified as a further research challenge. (p. 13)[^original]  
  <sub>anchor: "reconciling conflicting model recommendations when different perturbation scenarios favor different architectures"</sub>
- **permissive / recommendation**: Dynamic weighting schemes adapting to regulatory requirements or business contexts, possibly incorporating stakeholder preferences via interactive multi-criteria decision-making, are proposed as a promising direction; standardised benchmarking protocols and extension to continuous outcome variables are also suggested. (p. 13)[^original]  
  <sub>anchor: "Dynamic weighting schemes that adapt to specific regulatory requirements or business contexts"</sub>
- **descriptive / context**: The authors declare no known competing financial interests or personal relationships that could have influenced the work. (p. 13)[^original]  
  <sub>anchor: "The authors declare that they have no known competing financial interests"</sub>
- **expected / recommendation**: Future research should investigate how the Compliance Score framework can be adapted to meet evolving regulatory requirements, including integrating fairness metrics beyond the presented measures and emerging AI governance standards and audit requirements in financial services. (p. 13)[^original]  
  <sub>anchor: "investigation into how the Compliance Score framework can be adapted to meet evolving regulatory requirements"</sub>

---

[previous part](digest-002.md) | [source overview](overview.md)

[^original]: Academic publisher / repository, "SAFE AI metrics: An integrated approach" (2026-02-25). https://doi.org/10.1016/j.mlwa.2025.100821
