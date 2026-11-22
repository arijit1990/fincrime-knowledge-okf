---
type: Source Digest
title: Cost-Sensitive Learning to Defer to Multiple Experts with Workload Constraints - part 3 of 5 (pp. 14-19)
description: 'Verified paraphrased digest, pp. 14-19: Cost-Sensitive Learning to Defer to Multiple Experts with Workload Constraints > 5 Results; Cost-Sensitive Learning to Defer to Multiple Experts with Workload Constraints > 6 Conclusions and Future Work; Cost-Sensitive Learning to Defer to Multiple Experts with Workload Constraints > References'
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
part: 3
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
digest_points: 33
---

# Cost-Sensitive Learning to Defer to Multiple Experts with Workload Constraints (digest)

[previous part](digest-002.md) | [source overview](overview.md) | [next part](digest-004.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (pp. 14-19) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **academic finding**.

## 5.2 Expert Decision Modeling - Performance and Calibration

- **descriptive / finding or result**: For both alert rates, the ROCAUC of the expert-team correctness models consistently falls below 0.50 when λ = 0.0114, indicating these models cannot reliably rank the probabilities of correctness of the expert team under those conditions. (p. 14)[^original]  
  <sub>anchor: "the value of the ROCAUC consistently falls below 0.50 when"</sub>
- **descriptive / finding or result**: Even where ROCAUC is below 0.50, L2D methods can theoretically still improve performance by choosing which instances to defer to the classifier h, whose probabilities of correctness are shown to be reliably modeled. (p. 14)[^original]  
  <sub>anchor: "L2D methods can still theoretically achieve improvements in performance by choosing which instances should be deferred"</sub>
- **descriptive / finding or result**: The relative ranking of L2D methods can change significantly when the data distribution and cost structure of the experimental setting are altered. (p. 14)[^original]  
  <sub>anchor: "This demonstrates how the performance ranking of different L2D methods can change significantly by altering the data distribution"</sub>

## 5.3 Deferral under Capacity Constraints

- **descriptive / method**: Deferral quality is measured as the average misclassification cost per 100 instances, with results reported with 95% confidence intervals; the proposed method is referred to as DeCCaF. (p. 14)[^original]  
  <sub>anchor: "we evaluate the quality of deferral as measured by the average misclassification cost per 100 instances"</sub>
- **descriptive / finding or result**: On average both L2D methods outperform the non-L2D approaches, and DeCCaF is significantly better than them in most scenarios. (p. 14)[^original]  
  <sub>anchor: "both L2D methods outperform the non-L2D approaches, and that DeCCaF is significantly better in most scenarios"</sub>
- **descriptive / limitation**: With only 25 test seeds, the 95% confidence interval approximation may be unreliable, since it is derived based on the central limit theorem. (p. 14)[^original]  
  <sub>anchor: "As the number of test seeds (25) is relatively low, the approximation of the 95% confidence interval may be unreliable"</sub>
- **descriptive / data or feature**: Table 3 reports expected misclassification cost per 100 instances (assuming cFP = λ, cFN = 1) for each alert rate and λ pair, averaged across 25 test variations, with 95% confidence intervals; FR and OC are the Full Rejection and Only Classifier baselines. (p. 14)[^original]  
  <sub>anchor: "Expected misclassification cost per 100 instances (E[ _C_ ] _/_ 100, assuming _c_ FP = _λ, c_ FN = 1)"</sub>
- **descriptive / finding or result**: Table 3 cost for alert rate 0.05, λ=0.0114: FR 0.96, OC 0.96, Random 0.80±0.08, OvA 0.84±0.06, DeCCaF 0.79±0.04. (p. 14)[^original]  
  <sub>anchor: "0_._80_±_0_._08|0_._84_±_0_._06|0_._79_±_0_._04"</sub>
- **descriptive / finding or result**: Table 3 cost for alert rate 0.05, λ=0.057: FR 4.79, OC 4.58, Random 4.0±0.2, OvA 3.63±0.07, DeCCaF 3.4±0.04. (p. 14)[^original]  
  <sub>anchor: "4_._79|4_._58|4_._0_±_0_._2|3_._63_±_0_._07|3_._4_±_0_._04"</sub>
- **descriptive / finding or result**: Table 3 cost for alert rate 0.05, λ=0.285: FR 23.95, OC 14.08, Random 12.2±0.2, OvA 11.13±0.04, DeCCaF 10.2±0.2. (p. 14)[^original]  
  <sub>anchor: "23_._95|14_._08|12_._2_±_0_._2|11_._13_±_0_._04|10_._2_±_0_._2"</sub>
- **descriptive / finding or result**: Table 3 cost for alert rate 0.15, λ=0.0114: FR 1.05, OC 1.07, Random 0.87±0.05, OvA 0.87±0.02, DeCCaF 0.74±0.03. (p. 14)[^original]  
  <sub>anchor: "1_._05|1_._07|0_._87_±_0_._05|0_._87_±_0_._02|0_._74_±_0_._03"</sub>
- **descriptive / finding or result**: Table 3 cost for alert rate 0.15, λ=0.057: FR 5.27, OC 4.01, Random 3.5±0.1, OvA 3.55±0.03, DeCCaF 3.19±0.03. (p. 14)[^original]  
  <sub>anchor: "5_._27|4_._01|3_._5_±_0_._1|3_._55_±_0_._03|3_._19_±_0_._03"</sub>
- **descriptive / finding or result**: Table 3 cost for alert rate 0.15, λ=0.285: FR 26.36, OC 6.93, Random 6.0±0.1, OvA 5.23±0.08, DeCCaF 4.85±0.09. (p. 14)[^original]  
  <sub>anchor: "26_._36|6_._93|6_._0_±_0_._1|5_._23_±_0_._08|4_._85_±_0_._09"</sub>
- **descriptive / finding or result**: DeCCaF's performance relative to random assignment changes drastically with scenario properties, performing no better than random assignment at alert rate 5% FPR and λ = 0.0114. (p. 14)[^original]  
  <sub>anchor: "the relative performance of DeCCaF when compared to random assignment changes drastically depending on the scenario properties"</sub>

## 5.2 Expert Decision Modeling - Performance and Calibration

- **descriptive / finding or result**: In the bottom row of Figure 2, HEM achieves significantly lower ECE at λ = 0.057, while the reweighted OvA baseline outperforms HEM at λ = 0.285. (p. 14)[^original]  
  <sub>anchor: "we observe that HEM achieves significantly lower ECE for _λ_ = 0 _._ 057, with the reweighted OvA baseline outperforming HEM"</sub>
- **descriptive / finding or result**: The performance ranking of different L2D methods can change significantly when the data distribution and cost structure of the experimental setting are altered. (p. 14)[^original]  
  <sub>anchor: "This demonstrates how the performance ranking of different L2D methods can change significantly by altering the data distribution"</sub>

## 5.3 Deferral under Capacity Constraints

- **descriptive / finding or result**: Table 4 reports, for each scenario, the percentage of test variations in which DeCCaF outperforms other deferral baselines; across all scenarios DeCCaF outperforms the full rejection and Only Classifier baselines. (p. 15)[^original]  
  <sub>anchor: "In Table 4, we report the percentage of test variations, for each scenario, in which our method outperforms other deferral baselines"</sub>
- **descriptive / finding or result**: Table 4 values for alert rate 0.05: λ=0.0114 gives OvA 0.52, Random 0.56, FR 0.88, OC 0.88; λ=0.057 gives 0.76, 1.00, 1.00, 1.00; λ=0.285 gives 0.96, 1.00, 1.00, 1.00. (p. 15)[^original]  
  <sub>anchor: "0.05|0.0114|0.52|0.56|0.88|0.88|"</sub>
- **descriptive / finding or result**: Table 4 values for alert rate 0.15: λ=0.0114 gives OvA 0.84, Random 0.88, FR 1.00, OC 1.00; λ=0.057 gives 1.00, 0.96, 1.00, 1.00; λ=0.285 gives 0.96, 1.00, 1.00, 1.00. (p. 15)[^original]  
  <sub>anchor: "0.15|0.0114|0.84|0.88|1.00|1.00|"</sub>
- **descriptive / finding or result**: DeCCaF is significantly better than the OvA baseline in 5 of 6 scenarios, including both scenarios with λ = λt; the one inconclusive comparison is the most imbalanced scenario, with higher prevalence and lowest false-positive cost. (p. 15)[^original]  
  <sub>anchor: "DeCCaF performs significantly better than the OvA baseline in 5 out of 6 scenarios"</sub>
- **descriptive / finding or result**: The authors conclude from these results that there are benefits in jointly modeling human decision-making processes. (p. 15)[^original]  
  <sub>anchor: "We therefore conclude that there are benefits in jointly modeling the human decision-making processes."</sub>
- **descriptive / method**: Varying data availability experiment repeats runs with λ = λt = 0.057 while training OvA and DeCCaF on less data. (p. 15)[^original]  
  <sub>anchor: "repeating the experiments for _λ_ = _λt_ = 0 _._ 057, but training the OvA and DeCCaF methods with less data"</sub>
- **descriptive / finding or result**: Figure 3 shows that reducing training data significantly affects both methods, and DeCCaF performs either similarly to or better than the OvA baseline. (p. 15)[^original]  
  <sub>anchor: "both methods are significantly impacted by reducing the amount of training data"</sub>

## 6 Conclusions and Future Work

- **descriptive / context**: The work extends multi-expert L2D research to limited data availability, expert work-capacity constraints, cost-sensitive objectives and significant class imbalance. (p. 15)[^original]  
  <sub>anchor: "We consider limited data availability, the existence of human expert work-capacity constraints, cost-sensitive optimization objectives"</sub>
- **descriptive / context**: The authors propose a novel architecture intended to better model human behaviour and globally optimise system performance under capacity constraints. (p. 15)[^original]  
  <sub>anchor: "We propose a novel architecture that aims to better model human behaviour and to globally optimize the system"</sub>
- **descriptive / finding or result**: Across a wide variety of training and testing conditions in a realistic cost-sensitive task, variations in cost structure, data distribution and human behaviour significantly affect the relative performance of deferral strategies, and DeCCaF performs significantly better than baselines in many scenarios. (p. 15)[^original]  
  <sub>anchor: "empirically demonstrating that variations in the cost structure, data distribution, and human behavior can have significant impact"</sub>
- **descriptive / recommendation**: Future work plans to test adding fairness incentives to the misclassification cost optimisation method to study its impact on fairness. (p. 15)[^original]  
  <sub>anchor: "we plan on testing the addition of fairness incentives to our misclassification cost optimization method"</sub>

## 5.3 Deferral under Capacity Constraints

- **descriptive / data or feature**: Table 4 reports, for each alert-rate and λ pair, the percentage of the 25 test variations in which DeCCaF beats OvA, Random, FR and OC. (p. 15)[^original]  
  <sub>anchor: "Percentage of the 25 test variations, for each { _ar_ , _λ_ } pair, where DeCCaF beats other methods."</sub>
- **descriptive / finding or result**: In a binomial significance test with α = 0.05, DeCCaF is significantly better than other methods for values in the range 0.68 to 1, while values between 0.28 and 0.68 mean the best method cannot be concluded. (p. 15)[^original]  
  <sub>anchor: "DeCCaF is significantly better than other methods for values _∈_ [0 _._ 68 _,_ 1], while values _∈_ [0 _._ 28 _,_ 0 _._ 68] mean that we cannot conclude which method is best."</sub>

## 6 Conclusions and Future Work

- **descriptive / recommendation**: For scenarios with instance-specific misclassification costs (for example transaction fraud), the authors plan to study direct cost estimation using regression models instead of classification. (p. 16)[^original]  
  <sub>anchor: "For scenarios where the misclassification costs are instance-specific ( _i.e._ , transaction fraud), we will also study"</sub>
- **descriptive / context**: Without intelligent assignment, cases are distributed randomly across the human team, giving each expert an i.i.d. data distribution, whereas a multi-expert L2D system gives each expert a separate distribution of deferred cases. (p. 16)[^original]  
  <sub>anchor: "In a system without intelligent assignment, cases are distributed randomly throughout the human team"</sub>
- **descriptive / limitation**: An L2D system could assign the hardest cases to a highly skilled expert, damaging that expert's performance and creating unfair disparities in routinely evaluated analyst performance. (p. 16)[^original]  
  <sub>anchor: "this system could choose to assign the hardest cases to said expert, damaging their performance"</sub>
- **permissive / recommendation**: The authors could periodically assign randomly selected instances to each expert to evaluate them on an i.i.d. set, which would also be useful data for retraining the system as human behaviour may change. (p. 16)[^original]  
  <sub>anchor: "we could periodically assign randomly selected instances to each expert, in order to evaluate them in an i.i.d set"</sub>

---

[previous part](digest-002.md) | [source overview](overview.md) | [next part](digest-004.md)

[^original]: arXiv, "Cost-Sensitive Learning to Defer to Multiple Experts with Workload Constraints" (2024-11-03). https://arxiv.org/abs/2403.06906
