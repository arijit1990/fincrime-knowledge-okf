---
type: Source Text
title: 'Detection, Attribution, Narration: An End-to-End Pipeline for Explainable Money Mule Identification - part 2 of 4 (pp. 4-7)'
description: 'Verbatim extracted text, pp. 4-7: 3.4 SHAP Attribution Layer; 3.5 LLM Interpretation Module; 4 Experiments and Results; and 4 more sections'
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
part: 2
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

[previous part](text-001.md) | [source overview](overview.md) | [next part](text-003.md)

> Verbatim text extracted from the original (arXiv, 2026-07-20), part 2 of 4, pp. 4-7. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **academic finding**.[^original]

## 3.4 SHAP Attribution Layer


[p. 4]

For each customer selected for explanation—either those exceeding the alert threshold or a user-defined top-N set—we compute exact SHAP values using TreeSHAP [8], which exploits the tree structure of LightGBM for polynomial-time computation. TreeSHAP decomposes the predicted log-odds into additive per-feature contributions, satisfying local accuracy, missingness, and consistency axioms [9].

From the full set of 280 SHAP values per prediction, we select the top 10 features by absolute SHAP magnitude for downstream LLM interpretation. This selection balances two concerns, providing sufficient context for a meaningful narrative while keeping the prompt concise enough for reliable LLM generation. For each selected feature, we extract the feature name, its raw value for the account, the SHAP contribution value, and the direction of influence (i.e., positive = increased probability of the mule, negative = decreased probability).

## 3.5 LLM Interpretation Module


[pp. 4-5]

The final stage translates the structured SHAP output into a naturallanguage narrative that analysts can read during alert triage.

Table 2: Selected Hyperparameters for the Model

|Hyperparameter|Selected Value|
|---|---|
|num_leaves|31|
|max_depth|8|
|learning_rate|0.03|
|min_child_samples|200|
|subsample|0.7|
|colsample_bytree|0.7|
|reg_alpha|0.1|
|reg_lambda|5.0|

Deployment. All LLMs are deployed on-premise on a single NVIDIA H100 GPU to ensure that customer data never leaves the institution’s infrastructure. We evaluated three models, including Gemma-3-27B [15], GPT-OSS-120B [1], and Qwen3-Next-80B-A3BInstruct [17], with one selected for production deployment based on the evaluation described below.

Prompt design. The prompt consists of three elements.

- (1) Prediction context: the customer’s mule probability score and the score percentile.

- (2) SHAP evidence: the top-10 feature attributions, each presented as a (feature name, feature value, SHAP contribution, direction) tuple.

- (3) Instruction template: specifying output structure using a fixed JSON schema with red flags, reasons, and evidence references; tone (factual, concise); and constraints (cite only features present in the SHAP evidence; do not speculate beyond the provided data).

Narrative constraints and review. We constrain LLM-generated narratives through the prompt template and periodic human review to reduce the risk of unsupported or misleading explanations.

- Prompt constraints: the prompt instructs the LLM to cite only features present in the top-10 SHAP input, avoid speculation beyond the provided case data, and structure the output using a fixed JSON schema. The prompt also requires each red flag to reference the specific feature names supporting the explanation.

- Human review: domain experts provide periodic feedback on narrative quality through a lightweight rating mechanism integrated into the alert triage interface, enabling ongoing monitoring of explanation fidelity.

## 4 Experiments and Results


[p. 5]

Table 3: LightGBM model performance on the held-out test set. Precision, recall, and F1-score are reported at the operational threshold of 0.8.

|Metric|Value|
|---|---|
|Precision|0.909|
|Recall|0.816|
|F1-Score|0.860|
|AUC-ROC|0.824|
|AUC-PR|0.943|
|Log-Loss|0.450|

Temporal split. The dataset is divided by a temporal cutoff. Accounts observed before the cutoff form the training and validation sets, and accounts appearing only after the cutoff date form the held-out test set.

## 4.1 Experimental Setup


The dataset is split chronologically into training, validation, and test sets to prevent data leakage. The model is trained on data from January 2025 up to eight weeks before each test period. The eight weeks immediately preceding the test period serve as the validation set to monitor model performance. Testing is conducted over four consecutive weekly periods in December 2025.

Evaluation metrics. We report standard classification metrics where available, including precision, recall, F1-score, and AUC-PR, on the held-out test set. However, the primary metric for evaluating operational impact is _yield rate_ , defined as

The yield rate is measured on live production alerts rather than the held-out test set, reflecting the end-to-end effectiveness of the system, including the analyst-in-the-loop decision process. This metric directly captures what matters operationally: how often an analyst’s time spent reviewing an alert leads to a confirmed case.

Baseline. We compare against the incumbent rule-based detection system that was in production prior to our pipeline. The rule-based system uses deterministic thresholds on individual transaction features (e.g., transaction velocity, counterparty count, in/out ratios) to flag suspicious accounts. This represents the realistic production baseline rather than an academic benchmark.

## 4.2 Classification Performance


Table 3 summarises the available classification metrics for the LightGBM model on the held-out test set.

Threshold selection and model performance. Each week, the model scores between 20,000 and 30,000 cases, of which analysts can investigate approximately 100. The operating threshold of 0.8 was selected as the F1-optimal cut-off, meaning it is the score above which the balance between precision and recall is maximised. This threshold determines which cases are surfaced as alerts from the full scored population, reducing tens of thousands of cases to a queue that fits within analyst capacity.

Precision-recall trade-off. At threshold 0.8, the model achieves a mean precision of 0.909 and a mean recall of 0.816 across the four December 2025 backtesting weeks. The high precision means that

approximately 9 in 10 cases flagged to analysts are genuine money mules, keeping the workload focused and efficient. The recall of 0.816 reflects the inherent cost of setting a high threshold: roughly 1 in 5 true money mule cases score below 0.8 and are not immediately escalated. This trade-off is a deliberate design choice. Setting the threshold lower would recover more true cases but would also push the weekly alert volumes beyond what analysts can handle, diluting the quality of reviews. The F1 score of 0.860 at this threshold represents the best achievable balance between detection coverage and operational precision given the analyst capacity constraint.

It is important to note that the backtesting evaluation was conducted on the reviewed cases available from that a subset period of the full weekly population. This could be interpreted as an estimate of model performance rather than a count of production alerts.

Beyond the backtesting evaluation, the model’s real-world effectiveness is validated through the yield rate. Over the four weeks of December 2025, analysts reviewed 100 model-selected cases per week. Of these, 89% were confirmed as true money mules, yielding a production precision that directly reflects how useful the model’s prioritisation is in practice.

The yield rate of 89% means that analysts spent the vast majority of their review capacity on genuine cases, with fewer than 11 in every 100 alerts turning out to be false escalations. This level of precision is operationally meaningful in a context where analyst time is the binding constraint. A high yield rate ensures that the 100case weekly capacity is not diluted by noise, allowing investigators to focus their effort on the highest-risk cases.

Calibration. The LightGBM model outputs raw probability scores that were subsequently adjusted using Platt scaling, which is a post-hoc calibration technique that fits a logistic regression on a held-out calibration validation set to map raw model scores to better-aligned probabilities. This ensures that a predicted score of 0.8 more faithfully reflects an empirical probability of 80% of money mule behaviour, rather than being an arbitrary model output.

[pp. 5-6]

Calibration quality is assessed using the Expected Calibration Error (ECE), which measures the weighted average gap between predicted scores and observed positive rates across score bins. The combined ECE across all four December 2025 backtesting weeks is 0.079, indicating acceptable calibration overall.

Figure 2 illustrates the reliability diagram of the model. In the high-score region (score ≥ 0.8), where the operating threshold sits at 0.8, the model curve closely tracks the perfect calibration diagonal, with an ECE of 0.021. The zigzag pattern in the lower score range

Y. Zhang, Y. Zhang, Y. Jin, K. Razis, N. Choo, K. Wong, X. Tang, K. Zhu, W. Lee, and J. Zhao

Figure 2: Reliability diagram for the LightGBM + Platt-scaled model across four December 2025 backtesting weeks (combined). The dashed line represents perfect calibration. The shaded region (score _<_ 0.8) contains sparse labelled bins and is excluded from calibration interpretation. The operating threshold is set at 0.8. Sample sizes per bin are annotated for the high-score region (score ≥ 0.8). ECE ( ≥ 0.8) = 0.021; combined ECE (all bins) = 0.079.

attributes to small bin sample sizes ( _𝑛_ ≤ 8) rather than systematic miscalibration, and falls outside the operationally relevant score range. The _𝑛_ = 102 bin at score ≈ 0.97, representing the largest and most reliable sample. This aligns closely with the diagonal, further supporting calibration quality at the decision boundary.

Figure 3: SHAP beeswarm plot of the top 15 features by mean | SHAP | value. Each point represents one of the 400 scored customers pooled across four December 2025 backtesting weeks (W1-W4). Features are ordered top-to-bottom by decreasing mean absolute SHAP value. Point colour encodes the direction of each feature’s contribution. Red indicates the feature value pushes the model prediction toward higher risk, while blue indicates a risk-reducing effect. The _𝑥_ -axis represents the SHAP value, with positive values increasing predicted risk and negative values decreasing it. Features are grouped into Account demographics (top 3) and Transaction patterns (ranks 4-15).

## 4.3 Feature Importance


[p. 6]

We use mean absolute SHAP values across the test set to assess global feature importance. Figure 3 presents a beeswarm plot of the top 15 features ranked by mean |SHAP|, pooled across 400 scored customers from the four December 2025 backtesting weeks, collectively accounting for approximately 46% of the total mean absolute SHAP mass across all 280 features.

The analysis reveals two dominant feature groups. Account demographic features occupy the top three positions, collectively accounting for 19.5% of total mean absolute SHAP mass. The topranked feature is days_since_birth (mean |SHAP| = 1.31), then account_open_num (1.21) and account_open_days_since_latest (0.81). Directionally, higher values of days_since_birth are associated with increased risk, indicating that older customers are disproportionately flagged, potentially reflecting greater vulnerability to recruitment as money mules. account_open_num exhibits a bimodal distribution, where both very low and very high values push predictions toward higher risk, suggesting that newly created single-account holders and accounts with an unusually large number of linked accounts are flagged. Transaction pattern features (ranks 4-15) contribute a further 26.5%, with credit-to-debit ratio features across multiple lookback windows (7, 30, 90, and 180 days) and minimum credit amount features emerging as the most discriminative among them. Notably, lower transaction activity and lower credit amounts consistently shift SHAP values negative, implying

that financially inactive accounts are a stronger mule signal than volume-driven behaviour. Although multiple ratio features share similar lookback windows and may exhibit collinearity, SHAP values are computed on model output directly and thus reflect marginal contribution after all feature interactions are accounted for.

## 4.4 LLM Explanation Evaluation


[pp. 6-7]

We evaluated three open-weight LLM families, GPT-OSS-120B, Qwen3-Next-80B-A3B, and Gemma-3-27B, on 20 confirmed moneymule alerts under the production prompt template (Appendix A). Each output was scored on a 1-5 scale (higher is better) across four dimensions by blinded independent evaluators:

- Factual accuracy: numeric values, percentile claims, and feature descriptions are faithful to the case input; every cited feature resolves to one present in the top-10 SHAP evidence; no fabricated SHAP values.

- Typology plausibility: each flag maps a real data pattern to a recognised mule typology such as pass-through, velocity spikes, credit-to-debit imbalance, high activity in new accounts, counterparty diversity, or dormant reactivation.

- Completeness: coverage of the material signals, especially raw feature value exceeds 90th percentile of the training population, that an analyst would expect to see in the narrative.

Table 4: LLM model comparison on 20 confirmed money-mule alerts. Rubric dimensions are 1-5 mean scores (higher is better); latency is the mean wall-clock inference time per alert on the same single-H100 on-premise deployment.

|Model|Factual Accuracy|Typology Plausibility|Completeness|Actionability|Latency (s/alert)|
|---|---|---|---|---|---|
|GPT-OSS-120B|4.20|3.50|2.90|3.35|5.7|
|Qwen3-Next-80B-A3B|3.65|3.35|3.30|3.35|20.2|
|Gemma-3-27B|2.55|2.75|2.80|2.60|40.4|

- Actionability: flags are distinct, data-anchored, and suitable for direct use in analyst alert write-up without rewording.

Latency was measured separately as the mean wall-clock inference time per alert on the single-H100 on-premise deployment. Table 4 summarises the results.

[p. 7]

GPT-OSS-120B was selected for production. It has the highest score for factual accuracy (4.20 vs. 3.65 and 2.55) and typology plausibility, an equal score on actionability with Qwen, and is the fastest of the three by 3-7× despite having the largest parameter count. Two factors explain the speed. First, GPT-OSS and Qwen use a mixture-of-experts architecture that activates only a fraction of their parameters per token, while Gemma uses its full 27B parameters at every step. Second, GPT-OSS produces shorter responses on average, with 2.80 red flags per case versus 3.35 for Qwen and 3.55 for Gemma, so fewer tokens are streamed per alert.

Qwen3-Next-80B-A3B is still a viable fallback. It scores highest on completeness by surfacing more red flags per case, but its factual accuracy is lower. It is more prone to SHAP-value fabrication and percentile-claim errors. Gemma-3-27B was ruled out because its factual accuracy and its ∼40 s per-alert latency is uneconomical at operational volumes. Across all three models, the most common failure modes are exaggerated SHAP-value reporting, including occasional 10× magnitude errors, and misinterpretation of credit-todebit ratio semantics. These observations motivated stricter prompt constraints and periodic human review of generated narratives.


---

[previous part](text-001.md) | [source overview](overview.md) | [next part](text-003.md)

[^original]: arXiv, "Detection, Attribution, Narration: An End-to-End Pipeline for Explainable Money Mule Identification" (2026-07-20). https://arxiv.org/abs/2607.17586
