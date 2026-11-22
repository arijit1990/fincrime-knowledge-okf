---
type: Source Digest
title: Conformalized classifiers with reject option - part 7 of 9 (pp. 11-12)
description: 'Verified paraphrased digest, pp. 11-12: A B S T R A C T'
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
part: 7
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
digest_points: 19
---

# Conformalized classifiers with reject option (digest)

[previous part](digest-006.md) | [source overview](overview.md) | [next part](digest-008.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (pp. 11-12) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **academic finding**.

## ABSTRACT

- **descriptive / data or feature**: Table 6 reports recall for Experiment 2 across many datasets for decision tree (DT), XGBoost (XGB) and random forest (RF) models, each under Uncal, Iso, Platt, Beta, PlattBin and Conf calibration variants, with a Mean row and a Rank row. (p. 11)[^original]  
  <sub>anchor: "Table 6 Detailed results Experiment 2: Recall. Data sets DT XGB RF Uncal Iso Platt Beta PlattBin Conf"</sub>
- **descriptive / finding or result**: Table 6 reports dataset-level recall for Experiment 2 that varies widely; for example, on the haberman dataset DT Uncal recall is 0.303 and on kc1 it is 0.365, while on german and spect several models exceed 0.99 recall. (p. 11)[^original]  
  <sub>anchor: "haberman 0.303 0.122 0.042 0.050 0.003 0.257 0.312 0.066 0.013"</sub>
- **descriptive / finding or result**: The text notes that, as with accuracy, AUC and precision, there are large differences on individual datasets, for example PlattBin obtaining really poor recall on some datasets, which brings down the average. (p. 11)[^original]  
  <sub>anchor: "Similarly to accuracy, AUC and precision, there are large differences on individual datasets, e.g. with PlattBin obtaining really poor recall on some datasets, bringing down the average."</sub>
- **descriptive / finding or result**: Some calibration methods are said to under-estimate precision at higher rejection levels; Iso and Beta are described as slightly over-confident with an increasing trend towards higher rejection levels, whereas Conf achieves almost perfect precision estimation at all rejection levels. (p. 11)[^original]  
  <sub>anchor: "under-estimating precision for the higher rejection levels. Iso and Beta are ever so slightly over-confident"</sub>
- **descriptive / method**: Table 7 reports detailed error and efficiency results on precision for the Mondrian classifier (Conf) at epsilon values 0.01, 0.05 and 0.1. (p. 11)[^original]  
  <sub>anchor: "Table 7 shows detailed error and efficiency results on precision, for the Mondrian classifier (Conf) and"</sub>
- **descriptive / finding or result**: Overall, empirical error rates for precision match the epsilon values closely and show relatively small deviations at the dataset level. (p. 11)[^original]  
  <sub>anchor: "empirical error rates for precision are seen to match 𝜖 values closely, and have relatively small deviations on the dataset level."</sub>
- **descriptive / finding or result**: Decision trees are the weakest models overall and on most datasets, with ranks of 2.98, 2.85 and 2.85 for epsilon values 0.01, 0.05 and 0.1 respectively. (p. 11)[^original]  
  <sub>anchor: "Decision trees are again the weakest models, both overall and on most datasets, as reflected in ranks of 2.98, 2.85 and 2.85"</sub>
- **descriptive / finding or result**: Random forests perform better than XGBoost in the precision conformal results. (p. 11)[^original]  
  <sub>anchor: "Random forests again perform better than XGBoost."</sub>
- **descriptive / finding or result**: For epsilon values of 0.05 and especially 0.1, the Mondrian classifier has fewer than 1.0 class labels in the prediction set for quite a few datasets, which the text says indicates that empty prediction sets are needed to obtain the requested error rate. (p. 11)[^original]  
  <sub>anchor: "the Mondrian classifier has less than 1.0 class labels in the prediction set for quite a few datasets"</sub>
- **descriptive / finding or result**: Figure 9 shows precision estimation for XGBoost on the Elevators dataset; Uncal is over-confident at lower rejection levels but approaches accurate estimation as rejection level increases. (p. 11)[^original]  
  <sub>anchor: "Uncal is again over-confident for the lower rejection levels, but approaching accurate precision estimation"</sub>
- **descriptive / finding or result**: On Elevators, Platt scaling starts with a good precision estimate at the 10% rejection level but becomes gradually more under-confident, ending about 4 percentage points off at the 90% rejection level. (p. 11)[^original]  
  <sub>anchor: "ending up about 4 percentage points off at the 90% rejection level."</sub>
- **descriptive / finding or result**: On Elevators with XGBoost, Iso and PlattBin give very good precision estimates, while Conf and Beta produce perfect calibration, matching actual precision exactly at all rejection levels. (p. 11)[^original]  
  <sub>anchor: "Conf and Beta are seen to produce perfect calibration, with the estimated precision matching the actual precision exactly"</sub>
- **descriptive / method**: To study precision estimation under the reject option, the authors plot actual (empirical) versus estimated precision on three datasets in Figs. 8 to 10 for rejection levels from 10% to 90%. (p. 11)[^original]  
  <sub>anchor: "we start by looking at plots of actual (empirical) versus estimated precision on three different datasets, in Figs. 8–10"</sub>
- **descriptive / finding or result**: Fig. 8 shows decision tree results on the Delta-E dataset; Uncal is very over-confident (about 6 percentage points) at all rejection levels. (p. 11)[^original]  
  <sub>anchor: "Uncal is very over-confident (about 6 percentage points) for all rejection levels."</sub>
- **descriptive / finding or result**: On Delta-E with decision trees, PlattBin is markedly under-confident at the lowest rejection level but improves with increasing rejection level, while Platt scaling shows the opposite pattern, starting accurate at the 10% level. (p. 11)[^original]  
  <sub>anchor: "PlattBin is markedly under-confident at the lowest rejection level, but its precision estimation improves"</sub>
- **descriptive / finding or result**: Fig. 10 shows precision estimation for random forests on the medium-sized, imbalanced pc4 dataset, where the proportion of positive instances is 0.13, so the number of predicted positive instances is low at higher rejection levels. (p. 11)[^original]  
  <sub>anchor: "where the proportion of positive instances is 0.13. This means that at the higher rejection levels"</sub>
- **descriptive / finding or result**: On pc4, all techniques perform worse than on the Delta-E and Elevators datasets; Uncal is very under-confident with an error of 10 to 15 percentage points in precision estimation. (p. 12)[^original]  
  <sub>anchor: "Uncal is here very under-confident, with an error of 10–15 percentage points in precision estimation."</sub>
- **descriptive / finding or result**: On pc4, Platt is systematically over-confident by 7 to 8 percentage points across all rejection levels, and Iso is over-confident at lower rejection levels with increasing error at higher levels. (p. 12)[^original]  
  <sub>anchor: "Platt is systematically over-confident by 7–8 percentage points across all rejection levels"</sub>
- **descriptive / context**: Table 7 is captioned as detailed results for Experiment 2 on conformal classification. (p. 12)[^original]  
  <sub>anchor: "Table 7 Detailed results Experiment 2: Conformal classification."</sub>

---

[previous part](digest-006.md) | [source overview](overview.md) | [next part](digest-008.md)

[^original]: Academic publisher / repository, "Conformalized classifiers with reject option" (2026-02-24). https://doi.org/10.1016/j.mlwa.2026.100838
