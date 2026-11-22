---
type: Source Digest
title: Cost-Sensitive Learning to Defer to Multiple Experts with Workload Constraints - part 5 of 5 (pp. 27-29)
description: 'Verified paraphrased digest, pp. 27-29: Cost-Sensitive Learning to Defer to Multiple Experts with Workload Constraints > C Synthetic Experts; Cost-Sensitive Learning to Defer to Multiple Experts with Workload Constraints > D OvA Classifiers and HEM'
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
part: 5
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
digest_points: 13
---

# Cost-Sensitive Learning to Defer to Multiple Experts with Workload Constraints (digest)

[previous part](digest-004.md) | [source overview](overview.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (pp. 27-29) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **academic finding**.

## C.3 Expert Properties

- **descriptive / finding or result**: Figure 7 reports Cost of Full Alert Rejection values of 0.264, 0.240, 0.053, 0.048, 0.011 and 0.010 across its panels; the excerpt does not state explicitly which value belongs to which panel. (p. 27)[^original]  
  <sub>anchor: "Cost of Full Alert Rejection = 0.053Cost of Full Alert Rejection = 0.048"</sub>
- **descriptive / finding or result**: Figure 7 plots expert and classifier h performance using FNR and FPR as axes, for each combination of ar (0.05 and 0.15) and λ (0.0114, 0.057 and 0.285). (p. 27)[^original]  
  <sub>anchor: "Figure 7: Expert and Classifier _h_ performance plots for each _{ar, λ}_ pair"</sub>
- **descriptive / finding or result**: Figure 8 shows, for each ar and λ pair, the fraction of instances in which a given row (expert or classifier h) is correct and a given column is incorrect; the panels cover ar of 0.05 and 0.15 and λ of 0.0114, 0.057 and 0.285. (p. 28)[^original]  
  <sub>anchor: "Figure 8: Fraction of instances in which ROW is correct and COLUMN is incorrect."</sub>

## D OvA Classifiers and HEM

- **descriptive / method**: Both the OvA Classifiers and the HEM are modelled with LightGBM classifiers. (p. 29)[^original]  
  <sub>anchor: "We model both the OvA Classifiers and the HEM with LightGBM (Ke et al., 2017) classifiers."</sub>
- **descriptive / data or feature**: The LightGBM models are trained on the alerts raised by the Alert Model and the corresponding expert predictions, drawn from months four to six of the BAF dataset. (p. 29)[^original]  
  <sub>anchor: "ranging from months four to six of the BAF dataset"</sub>
- **descriptive / method**: Both methods are trained by minimizing the weighted log-loss. (p. 29)[^original]  
  <sub>anchor: "Both methods are trained by minimizing the weighted log-loss."</sub>
- **descriptive / method**: Hyperparameters are chosen by Bayesian search (Akiba et al., 2019) over an extensive grid, with 120 total trials, of which 100 are start-up trials, and validation performed on the seventh month. (p. 29)[^original]  
  <sub>anchor: "for 120 total trials, with 100 start-up trials, with validation done on the seventh month."</sub>
- **descriptive / method**: The hyperparameter search space for the OvA Classifiers and HEM is detailed in Table 7. (p. 29)[^original]  
  <sub>anchor: "The hyperparameter search space is detailed in Table 7."</sub>
- **descriptive / method**: Table 7 fixes boosting_type to "dart" and sets enable_bundle to a choice of False or True. (p. 29)[^original]  
  <sub>anchor: "|enable_bundle|[False,True]||"</sub>
- **descriptive / method**: Table 7 sets n_estimators to the interval [50,250] and max_depth to [2,20], both sampled uniformly. (p. 29)[^original]  
  <sub>anchor: "|n_estimators|[50,250]|Unif.|"</sub>
- **descriptive / method**: Table 7 sets num_leaves to [100,1000] and min_child_samples to [5,100], both sampled on a log scale. (p. 29)[^original]  
  <sub>anchor: "|min_child_samples|[5,100]|Log.|"</sub>
- **descriptive / method**: Table 7 sets learning_rate to [0.005, 0.5] on a log scale. (p. 29)[^original]  
  <sub>anchor: "|learning_rate|[0.005, 0.5]|Log.|"</sub>
- **descriptive / method**: Table 7 sets reg_alpha and reg_lambda to [0.0001, 0.1], both on a log scale. (p. 29)[^original]  
  <sub>anchor: "|reg_lambda|[0.0001, 0.1]|Log.|"</sub>

---

[previous part](digest-004.md) | [source overview](overview.md)

[^original]: arXiv, "Cost-Sensitive Learning to Defer to Multiple Experts with Workload Constraints" (2024-11-03). https://arxiv.org/abs/2403.06906
