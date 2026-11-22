---
type: Source Digest
title: Conformalized classifiers with reject option - part 3 of 9 (pp. 6-7)
description: 'Verified paraphrased digest, pp. 6-7: A B S T R A C T'
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
part: 3
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
digest_points: 9
---

# Conformalized classifiers with reject option (digest)

[previous part](digest-002.md) | [source overview](overview.md) | [next part](digest-004.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (pp. 6-7) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **academic finding**.

## A B S T R A C T

- **descriptive / context**: Table 2 reports detailed Experiment 1 accuracy results for many data sets, comparing classifiers DT, XGB and RF, each under six calibration variants: Uncal, Iso, Platt, Beta, PlattBin and Conf. (p. 6)[^original]  
  <sub>anchor: "Table 2 Detailed results Experiment 1: Accuracy. Data sets DT XGB RF"</sub>
- **descriptive / data or feature**: Table 2 rows give per-data-set accuracy values for ailerons, bank8FM, banknote, churn, colic, creditA, deltaA, deltaE, diabetes, EEG_eye, elevators, german, haberman, heartC, heartH and heartS, each across the DT, XGB and RF variants. The first row reports ailerons with DT Uncal 0.852 and DT Conf 0.839, ending in RF Conf 0.870. (p. 6)[^original]  
  <sub>anchor: "ailerons 0.852 0.848 0.848 0.839 0.828 0.847 0.883 0.879 0.880"</sub>
- **descriptive / data or feature**: Table 2 continues with accuracy rows for houses, HTRU2, iono, je4042, je4243, kc1, kc2, kin8 nm, kr-vs-kp, liver, mozilla4, pc1req, pc4, phish, phoneme, puma8NH, qsarbiodeg, sonar, spambase, spect, spectf, transfusion, ttt, vote and wbc, with the same six calibration variants for each of DT, XGB and RF. (p. 6)[^original]  
  <sub>anchor: "kr-vs-kp 0.978 0.975 0.975 0.973 0.964 0.974 0.993 0.989"</sub>
- **descriptive / data or feature**: Table 2 includes a summary Mean row giving average accuracy across the data sets. For DT Uncal the mean is 0.821 and for DT Conf it is 0.815 (with Uncal and Conf values for XGB and RF also listed in the row). (p. 6)[^original]  
  <sub>anchor: "Mean 0.821 0.823 0.822 0.809 0.810 0.815 0.850 0.847 0.850 0.850"</sub>
- **descriptive / context**: Figure 1 presents statistical tests of predictive performance at a significance level alpha of 0.05. (p. 6)[^original]  
  <sub>anchor: "Fig. 1. Statistical tests, predictive performance."</sub>
- **descriptive / finding or result**: In the Table 2 Rank row for accuracy, the DT Uncal variant has rank 2.32, the DT Platt variant rank 2.88, and the DT Conf variant rank 3.83. (p. 6)[^original]  
  <sub>anchor: "Rank 2.32 2.39 2.88 4.78 4.80 3.83 2.02 5.17 2.73 3.34"</sub>
- **descriptive / finding or result**: Across the 18 accuracy variants in Table 2, the RF Uncal variant has the best (lowest) Rank value of 1.49, ahead of the XGB Uncal variant at 2.02 and the DT Uncal variant at 2.32. (p. 6)[^original]  
  <sub>anchor: "Rank 2.32 2.39 2.88 4.78 4.80 3.83 2.02 5.17 2.73 3.34 4.37 3.37 1.49 5.02 2.79 3.35 4.88 3.46"</sub>
- **descriptive / finding or result**: The Table 2 Mean accuracy row gives 0.821 for DT Uncal, 0.850 for XGB Uncal and 0.859 for RF Uncal, with the other calibration variants reported in the same row. (p. 6)[^original]  
  <sub>anchor: "Mean 0.821 0.823 0.822 0.809 0.810 0.815 0.850 0.847 0.850 0.850 0.845 0.845 0.859 0.852 0.855 0.855 0.850 0.853"</sub>
- **descriptive / context**: Table 3 gives detailed Experiment 1 results for AUC; the excerpt contains only the caption and no AUC values. (p. 6)[^original]  
  <sub>anchor: "Table 3 Detailed results Experiment 1: AUC."</sub>

---

[previous part](digest-002.md) | [source overview](overview.md) | [next part](digest-004.md)

[^original]: Academic publisher / repository, "Conformalized classifiers with reject option" (2026-02-24). https://doi.org/10.1016/j.mlwa.2026.100838
