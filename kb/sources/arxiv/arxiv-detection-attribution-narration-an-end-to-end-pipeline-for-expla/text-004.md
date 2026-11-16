---
type: Source Text
title: 'Detection, Attribution, Narration: An End-to-End Pipeline for Explainable Money Mule Identification - part 4 of 4 (pp. 9-10)'
description: 'Verbatim extracted text, pp. 9-10: A Prompt Template; A Prompt Template > Listing 1: System prompt.; B Example LLM Outputs and Analyst Reviews'
resource: https://arxiv.org/abs/2607.17586
tags:
- academic_finding
- data_features
- explainability
- global_academic
- model_development
- preprint
status: stable
source_id: arxiv-detection-attribution-narration-an-end-to-end-pipeline-for-expla
issuer: arxiv
issuer_name: arXiv
jurisdictions:
- GLOBAL_ACADEMIC
tier: 3
instrument_type: preprint
normative_force: academic_finding
publication_date: '2026-07-20'
legal_status: unknown
part: 4
parts_total: 4
content_mode: full_text
generated:
  by: process:fincrime-kb-build
  at: '2026-11-16T16:23:02Z'
verified:
- by: process:kb-validate/verbatim-coverage
  at: '2026-11-16T16:23:02Z'
sources:
- id: original
  resource: https://arxiv.org/abs/2607.17586
  title: 'Detection, Attribution, Narration: An End-to-End Pipeline for Explainable Money Mule Identification'
  author: org:arxiv
  last_modified: '2026-07-20T00:00:00Z'
---

# Detection, Attribution, Narration: An End-to-End Pipeline for Explainable Money Mule Identification

[previous part](text-003.md) | [source overview](overview.md)

> Verbatim text extracted from the original (arXiv, 2026-07-20), part 4 of 4, pp. 9-10. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **academic finding**.[^original]

## A Prompt Template


[p. 9]

- You are a financial crime analyst specializing in detecting Money Mule activities. Your task is to analyze individual cases by examining:

- - Feature values (value_raw): Metrics describing transaction behavior or customer profiles, along with their corresponding 90th percentile (ref_p90, above_p90) and 50th percentile (ref_p50) benchmarks across all cases.

- Feature meanings (feature_meaning): Clear explanations of what each feature name (name) represents.

|- SHAP values (shap) and absolute SHAP values (abs_shap):Indicators of each feature's impact on the model's predictionfor the case.- Overall risk score and percentile (model_score andscore_percentile): The case's risk assessment and its relativestanding among all evaluated cases.|
|---|
|Based on this information, identify potential suspicious patternsor red flags that explain why the case has its current riskscore. Please explain your findings in plain language,avoiding technical jargon, so that analysts withoutspecialized technical knowledge can easily understand. Pleasealso keep it simple.|
|Please respond strictly in valid JSON following exactly thisschema:|
|{"case_id": "","red_flags": [{"potential_pattern": "pattern>","reason": "to the issue>","evidence_references": ["", "..."]}]}|

### Listing 1: System prompt.


|Analyze the following case:|
|---|
|Input data for a case:|
||
|Output (JSON format only):|

Listing 2: User message.

This appendix presents two representative LLM-generated red flag narratives produced by the production pipeline (Section 4.4), together with the corresponding analyst verdicts recorded after manual review. For readability, we present the narrative content extracted from the JSON outputs rather than the full raw JSON objects. In both cases the analyst confirmed the alert as adverse and classified it under the money-mule typology (MM/UML).

## B Example LLM Outputs and Analyst Reviews


[pp. 9-10]

- The ratio of transactions in the past 7 days compared to the past 180 days is significantly higher than typical, and the total transaction value in the past 7 days is also elevated. This suggests a recent increase in activity that could be suspicious. The customer holds a relatively high number of open accounts (5), and the entity has been around for a considerable time (over 32 years). This, combined with the recent activity surge, could indicate an attempt to use established accounts for illicit purposes. The days since the last account opening is relatively short, which could indicate a sudden increase in account activity. This, combined with the recent surge in transaction activity, could be a red flag.

Listing 3: Example 1 — LLM-generated red flag narrative.

KDD’26 - MLF workshop, August 9 - 13, 2026, Jeju, Korea Y. Zhang, Y. Zhang, Y. Jin, K. Razis, N. Choo, K. Wong, X. Tang, K. Zhu, W. Lee, and J. Zhao

The model flags this case as very high risk (99.44 percentile). This is driven by a combination of factors. The customer receives money from a very high number of different people (97 Listing 4: Example 2 — LLM-generated red flag narrative. counterparties in the last 180 days) and sends money to a larger than typical number of countries (9 countries in the last 180 days). The number of open accounts is also a contributing factor. This, combined with a relatively low total transaction value and the age of the account, suggests potential money mule activity.


---

[previous part](text-003.md) | [source overview](overview.md)

[^original]: arXiv, "Detection, Attribution, Narration: An End-to-End Pipeline for Explainable Money Mule Identification" (2026-07-20). https://arxiv.org/abs/2607.17586
