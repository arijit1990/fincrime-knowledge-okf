---
type: Source Digest
title: Conformalized classifiers with reject option - part 6 of 9 (pp. 10-11)
description: 'Verified paraphrased digest, pp. 10-11: A B S T R A C T'
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
part: 6
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

[previous part](digest-005.md) | [source overview](overview.md) | [next part](digest-007.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (pp. 10-11) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **academic finding**.

## (untitled section)

- **descriptive / finding or result**: Table 5 reports the mean precision across datasets for each setup: for decision trees the Uncal, Iso, Platt, Beta, PlattBin and Conf means are 0.773, 0.779, 0.782, 0.786, 0.765 and 0.775; for XGBoost 0.811, 0.800, 0.806, 0.805, 0.798 and 0.805; for random forest 0.826, 0.809, 0.819, 0.820, 0.808 and 0.820. (p. 10)[^original]  
  <sub>anchor: "Mean 0.773 0.779 0.782 0.786 0.765 0.775 0.811 0.800 0.806 0.805"</sub>
- **descriptive / finding or result**: Table 5 reports mean ranks for each precision setup: decision trees Uncal 3.37, Iso 3.55, Platt 3.22, Beta 3.28, PlattBin 4.44 and Conf 3.15; XGBoost Uncal 1.98, Iso 4.71, Platt 3.32, Beta 3.37, PlattBin 4.05 and Conf 3.59; random forest Uncal 2.02, Iso 4.93, Platt 3.15, Beta 3.37, PlattBin 4.12 and Conf 3.41. (p. 10)[^original]  
  <sub>anchor: "Rank 3.37 3.55 3.22 3.28 4.44 3.15 1.98 4.71 3.32 3.37"</sub>
- **descriptive / context**: Fig. 7 is a statistical testing accuracy estimation for RF, with alpha set at 0.05. (p. 10)[^original]  
  <sub>anchor: "Fig. 7. Statistical testing accuracy estimation: RF. 𝛼= 0.05."</sub>
- **descriptive / finding or result**: For precision, the text states that Uncal performs best overall for random forests and XGBoost, while four of the calibrated setups achieve higher precision for decision trees. (p. 10)[^original]  
  <sub>anchor: "while Uncal performs best overall for random forests and XGBoost"</sub>
- **descriptive / finding or result**: Overall precision differences between setups are small (within 2 percentage points), but some datasets show large differences, especially for decision trees. (p. 10)[^original]  
  <sub>anchor: "overall differences are small (within 2 percentage points)"</sub>
- **descriptive / finding or result**: Among the calibration techniques, Platt, Beta and Conf are reported to achieve very similar precision (the text is truncated at this point in the excerpt). (p. 10)[^original]  
  <sub>anchor: "Of the calibration techniques, Platt, Beta and Conf achieve very"</sub>
- **descriptive / finding or result**: Table 5 reports detailed Experiment 2 precision for decision trees (DT), XGBoost (XGB) and random forest (RF), with each model shown under six setups labelled Uncal, Iso, Platt, Beta, PlattBin and Conf, for each listed dataset. (p. 10)[^original]  
  <sub>anchor: "Table 5 Detailed results Experiment 2: Precision. Data sets DT XGB RF Uncal Iso Platt Beta PlattBin Conf"</sub>
- **descriptive / finding or result**: The text says Platt, Beta and Conf achieve very similar precision for XGBoost and random forest. (p. 10)[^original]  
  <sub>anchor: "Of the calibration techniques, Platt, Beta and Conf achieve very"</sub>
- **descriptive / finding or result**: The text states that the Iso and PlattBin setups do a little worse than these for XGBoost and random forest. (p. 10)[^original]  
  <sub>anchor: "similar precision for XGBoost and random forest, and the Iso and PlattBin do a little worse than these."</sub>
- **descriptive / context**: Table 6 shows detailed Experiment 2 results on recall for all datasets. (p. 11)[^original]  
  <sub>anchor: "Table 6 shows detailed results on recall for all datasets."</sub>
- **descriptive / finding or result**: For recall, Uncal performs best, with the highest average recall and the best mean rank across all three classifier techniques. (p. 11)[^original]  
  <sub>anchor: "Uncal performs best, with the highest average recall and best mean rank"</sub>
- **descriptive / finding or result**: Among the calibrated techniques for recall, Iso and Conf have the highest average recall, and Iso also has the best mean rank of the calibrated techniques. (p. 11)[^original]  
  <sub>anchor: "Iso and Conf have the highest average recall of the calibrated techniques"</sub>
- **descriptive / context**: Table 6 is the detailed Experiment 2 recall table; its values are not present in the excerpt. (p. 11)[^original]  
  <sub>anchor: "Table 6 Detailed results Experiment 2: Recall."</sub>

---

[previous part](digest-005.md) | [source overview](overview.md) | [next part](digest-007.md)

[^original]: Academic publisher / repository, "Conformalized classifiers with reject option" (2026-02-24). https://doi.org/10.1016/j.mlwa.2026.100838
