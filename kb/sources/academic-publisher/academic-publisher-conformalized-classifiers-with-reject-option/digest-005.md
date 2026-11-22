---
type: Source Digest
title: Conformalized classifiers with reject option - part 5 of 9 (pp. 9-10)
description: 'Verified paraphrased digest, pp. 9-10: A B S T R A C T'
resource: https://doi.org/10.1016/j.mlwa.2026.100838
tags:
- academic_finding
- academic_paper
- alerts_triage
- global_academic
- ml_statistics
- model_validation
status: stable
source_id: academic-publisher-conformalized-classifiers-with-reject-option
issuer: academic_publisher
issuer_name: Academic publisher / repository
jurisdictions:
- GLOBAL_ACADEMIC
tier: 3
instrument_type: academic_paper
normative_force: academic_finding
publication_date: '2026-02-24'
legal_status: unknown
part: 5
parts_total: 9
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
  resource: https://doi.org/10.1016/j.mlwa.2026.100838
  title: Conformalized classifiers with reject option
  author: org:academic_publisher
  last_modified: '2026-02-24T00:00:00Z'
digest_points: 13
---

# Conformalized classifiers with reject option (digest)

[previous part](digest-004.md) | [source overview](overview.md) | [next part](digest-006.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (pp. 9-10) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **academic finding**.

## (untitled section)

- **descriptive / data or feature**: Table 4 reports detailed Experiment 1 (conformal classification) results for many benchmark datasets at significance levels epsilon = 0.01, 0.05 and 0.1, giving the error rate and average set size (AvgC) for each of three classifiers: DT, XGB and RF. (p. 9)[^original]  
  <sub>anchor: "Table 4 Detailed results Experiment 1: Conformal classification."</sub>
- **descriptive / finding or result**: For the bank8FM dataset, Table 4 gives error rates of about 0.010, 0.050 and 0.100 at epsilon 0.01, 0.05 and 0.1 respectively, with AvgC values of 1.706 (DT), 1.187 (XGB) and 1.183 (RF) at epsilon 0.01. (p. 9)[^original]  
  <sub>anchor: "bank8FM 0.010 0.010 0.010 1.706 1.187 1.183 0.050 0.049 0.050 1.067 1.024 1.023 0.101 0.100 0.099 0.959 0.934 0.935"</sub>
- **descriptive / finding or result**: Across the datasets, the table's mean row shows an error rate of 0.010 for all three classifiers at epsilon 0.01, and mean AvgC values of 1.787 (DT), 1.583 (XGB) and 1.569 (RF) at that level. (p. 9)[^original]  
  <sub>anchor: "Mean 0.010 0.010 0.010 1.787 1.583 1.569 0.050 0.050 0.049 1.429 1.314 1.295"</sub>
- **descriptive / data or feature**: Figure 6 is a statistical testing figure for accuracy estimation using the XGB classifier at significance level alpha = 0.05. (p. 9)[^original]  
  <sub>anchor: "Fig. 6. Statistical testing accuracy estimation: XGB. 𝛼= 0.05."</sub>

## 5.2. Experiment 2 — Precision estimation

- **descriptive / finding or result**: The authors summarise Experiment 1 by stating that the conformalized approach clearly outperformed the alternatives. (p. 9)[^original]  
  <sub>anchor: "Summarizing Experiment 1, the conformalized approach clearly out- performed the alternatives."</sub>
- **descriptive / method**: Experiment 2 aims to estimate precision for a given reject level. (p. 9)[^original]  
  <sub>anchor: "In Experiment 2, the purpose is to estimate precision, given a certain reject level."</sub>
- **descriptive / data or feature**: Table 5 is titled as the detailed results of Experiment 2 on precision; its body is not included in the excerpt. (p. 9)[^original]  
  <sub>anchor: "Table 5 Detailed results Experiment 2: Precision."</sub>

## (untitled section)

- **descriptive / finding or result**: The mean row of Table 4 gives mean error rates of 0.010 at epsilon 0.01, 0.050, 0.050 and 0.049 at epsilon 0.05, and 0.100, 0.100 and 0.099 at epsilon 0.1 (DT, XGB, RF), with mean AvgC values of 1.787, 1.583 and 1.569 at epsilon 0.01, 1.429, 1.314 and 1.295 at epsilon 0.05, and 1.235, 1.164 and 1.146 at epsilon 0.1. (p. 9)[^original]  
  <sub>anchor: "Mean 0.010 0.010 0.010 1.787 1.583 1.569 0.050 0.050 0.049 1.429 1.314 1.295 0.100 0.100 0.099 1.235 1.164 1.146"</sub>
- **descriptive / finding or result**: The rank row of Table 4, which sits under the AvgC columns, gives average ranks of 2.98 (DT), 1.68 (XGB) and 1.34 (RF) at epsilon 0.01, 2.85, 1.83 and 1.32 at epsilon 0.05, and 2.85, 1.85 and 1.29 at epsilon 0.1. (p. 9)[^original]  
  <sub>anchor: "Rank – – – 2.98 1.68 1.34 – – – 2.85 1.83 1.32 – – – 2.85 1.85 1.29"</sub>

## 5.2. Experiment 2 — Precision estimation

- **permissive / finding or result**: With the suggested setup, a user can easily balance the need for accurate prediction against acceptable rejection levels. (p. 9)[^original]  
  <sub>anchor: "With the suggested setup, a user can easily balance the need for accurate prediction"</sub>
- **descriptive / data or feature**: Table 5 is the detailed results table for Experiment 2 on precision; the extracted text ends before its figures. (p. 9)[^original]  
  <sub>anchor: "Table 5 Detailed results Experiment 2: Precision."</sub>
- **descriptive / finding or result**: The authors summarise that the conformalized approach clearly outperformed the alternatives in Experiment 1. (p. 9)[^original]  
  <sub>anchor: "Summarizing Experiment 1, the conformalized approach clearly out- performed the alternatives."</sub>
- **descriptive / method**: In Experiment 2 the purpose is to estimate precision, given a certain reject level. (p. 9)[^original]  
  <sub>anchor: "In Experiment 2, the purpose is to estimate precision, given a certain reject level."</sub>

---

[previous part](digest-004.md) | [source overview](overview.md) | [next part](digest-006.md)

[^original]: Academic publisher / repository, "Conformalized classifiers with reject option" (2026-02-24). https://doi.org/10.1016/j.mlwa.2026.100838
