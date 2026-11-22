---
type: Source Digest
title: Conformalized classifiers with reject option - part 4 of 9 (pp. 7-9)
description: 'Verified paraphrased digest, pp. 7-9: A B S T R A C T'
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
part: 4
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
digest_points: 26
---

# Conformalized classifiers with reject option (digest)

[previous part](digest-003.md) | [source overview](overview.md) | [next part](digest-005.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (pp. 7-9) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **academic finding**.

## (untitled section)

- **descriptive / finding or result**: The Mean row of Table 3 lists mean AUC values of 0.782, 0.764, 0.760, 0.734, 0.737 and 0.774 for the first model block (DT), 0.812, 0.796, 0.797, 0.797, 0.791 and 0.806 for the second block (XGB), and 0.812, 0.802, 0.803, 0.801, 0.796 and 0.804 for the third block (RF), in the order the columns were extracted. (p. 7)[^original]  
  <sub>anchor: "Mean 0.782 0.764 0.760 0.734 0.737 0.774 0.812 0.796 0.797 0.797 0.791 0.806"</sub>
- **descriptive / finding or result**: The Rank row of Table 3 gives average ranks of 1.34, 2.91, 3.65, 5.37, 5.32 and 2.41 for the first block, with further rank values for the other two blocks, as extracted; the column order in the extracted table is not clearly aligned with the setup labels. (p. 7)[^original]  
  <sub>anchor: "Rank 1.34 2.91 3.65 5.37 5.32 2.41"</sub>
- **descriptive / method**: For absolute estimation errors at rejection levels 30%, 50%, 70% and 90%, the six setups were compared as parts of a classification with reject option scenario, using Friedman tests followed by Nemenyi post-hoc tests. (p. 7)[^original]  
  <sub>anchor: "we again perform Friedman tests (Friedman, 1937), followed by Nemenyi post-hoc tests (Nemenyi, 1963)."</sub>
- **descriptive / finding or result**: For decision trees on the puma8NH dataset, uncalibrated decision trees are very overconfident at all rejection levels, with an estimation error as high as 0.12 for most rejection levels. (p. 7)[^original]  
  <sub>anchor: "The estimation error is as high as 0.12, for most rejection levels."</sub>
- **descriptive / finding or result**: On puma8NH all calibration methods significantly reduce the decision tree estimation error, but only the Conf setup has an estimation error close to zero at all rejection levels. (p. 7)[^original]  
  <sub>anchor: "Interestingly enough though, only the Conf setup has an estimation error close to zero"</sub>
- **descriptive / finding or result**: For decision trees (Fig. 5), using no calibration is significantly worse than all calibrated setups at all four rejection levels investigated. (p. 7)[^original]  
  <sub>anchor: "using no calibration is significantly worse than all calibrated setups"</sub>
- **descriptive / finding or result**: For decision trees, Conf has the lowest (best) mean rank at all rejection levels; except at the 90% level, its estimation error is significantly lower than that of all other options. (p. 7)[^original]  
  <sub>anchor: "With the exception of the rejection level 90%, the estimation error for Conf is significantly lower than all other options."</sub>
- **descriptive / finding or result**: For random forests on the Sonar dataset (Fig. 3), uncalibrated models are underconfident, with estimation errors between −0.15 and −0.06 across the rejection levels. (p. 7)[^original]  
  <sub>anchor: "estimation errors between −0.15 and −0.06, for the different rejection levels."</sub>
- **descriptive / finding or result**: For random forests on Sonar, all setups give more accurate estimates than no calibration, but Iso is systematically overconfident while Platt is systematically underconfident. (p. 7)[^original]  
  <sub>anchor: "Iso is actually systematically overconfident, while Platt is systematically underconfident."</sub>
- **descriptive / finding or result**: For random forests on Sonar, Beta and PlattBin are slightly overconfident at all rejection levels except 0.8 and 0.9, while Conf is very accurate at all rejection levels. (p. 7)[^original]  
  <sub>anchor: "Beta and PlattBin are slightly overconfident for all rejection levels except 0.8 and 0.9."</sub>
- **descriptive / finding or result**: For XGB (Fig. 6), Conf has the lowest mean rank at all rejection levels and is the only setup significantly better than no calibration at all four rejection levels. (p. 7)[^original]  
  <sub>anchor: "It is also the only setup that is significantly better than using no calibration, on all four rejection levels."</sub>
- **descriptive / finding or result**: For XGB, PlattBin is the second best and Beta the third best option at all rejection levels. (p. 7)[^original]  
  <sub>anchor: "For XGB, PlattBin is the second best, and Beta the third best option"</sub>
- **descriptive / finding or result**: For XGB, Conf is significantly more accurate than all alternatives at the higher rejection levels, 70% and 90%. (p. 7)[^original]  
  <sub>anchor: "Conf is significantly more accurate than all alternatives for the higher rejection levels, i.e., 70% and 90%."</sub>
- **descriptive / finding or result**: On the Diabetes dataset (Fig. 4), uncalibrated XGBoost models are systematically overconfident when estimating their accuracy at all rejection levels. (p. 7)[^original]  
  <sub>anchor: "Calibration again improves the estimations."</sub>
- **descriptive / finding or result**: On the Diabetes dataset, models calibrated using Iso are still overconfident, while Platt scaling yields slightly underconfident models at the higher rejection levels. (p. 7)[^original]  
  <sub>anchor: "models calibrated using Iso are still overconfident"</sub>
- **descriptive / finding or result**: For random forests (Fig. 7), Conf has the lowest mean rank and PlattBin the second lowest at all rejection levels. (p. 7)[^original]  
  <sub>anchor: "Conf has the lowest mean rank, and PlattBin the second lowest, on all rejection levels, for random forests too."</sub>
- **descriptive / finding or result**: For random forests, Conf is the only alternative significantly more accurate than no calibration at all rejection levels, and at 50% and 90% it is significantly better than all other setups. (p. 7)[^original]  
  <sub>anchor: "For two of the four rejection levels (50% and 90%) Conf is significantly better than all other setups."</sub>
- **descriptive / finding or result**: The text states that Beta, PlattBin and Conf produce very accurate estimations, a statement whose surrounding context is cut off in the excerpt. (p. 7)[^original]  
  <sub>anchor: "Beta, PlattBin and Conf, conversely, produces very accurate estimations."</sub>
- **descriptive / data or feature**: Figure 2 shows DT accuracy estimation for rejection rates from 10% to 90% on the puma8NH dataset. (p. 7)[^original]  
  <sub>anchor: "Fig. 2. DT accuracy estimation rejecting 10%–90% on puma8NH dataset."</sub>
- **descriptive / data or feature**: Figure 3 shows RF accuracy estimation for rejection rates from 10% to 90% on the Sonar dataset. (p. 7)[^original]  
  <sub>anchor: "Fig. 3. RF accuracy estimation rejecting 10%–90% on Sonar dataset."</sub>
- **descriptive / data or feature**: Figure 4 shows XGB accuracy estimation for rejection rates from 10% to 90% on the Diabetes dataset. (p. 7)[^original]  
  <sub>anchor: "Fig. 4. XGB accuracy estimation rejecting 10%–90% on Diabetes dataset."</sub>
- **descriptive / method**: Figure 5 reports statistical testing of DT accuracy estimation at a significance level alpha of 0.05. (p. 7)[^original]  
  <sub>anchor: "Fig. 5. Statistical testing accuracy estimation: DT. 𝛼= 0.05."</sub>
- **descriptive / data or feature**: Table 4 is titled as detailed results of Experiment 1 for conformal classification, but its contents are not included in the excerpt. (p. 7)[^original]  
  <sub>anchor: "Table 4 Detailed results Experiment 1: Conformal classification."</sub>
- **descriptive / data or feature**: Table 3 reports Experiment 1 AUC results per dataset in three blocks, one each for decision trees (DT), XGBoost (XGB) and random forests (RF), with six setups per block: Uncal, Iso, Platt, Beta, PlattBin and Conf. The excerpt's column headers list the blocks in the order DT, XGB, RF. (p. 7)[^original]  
  <sub>anchor: "Data sets DT XGB RF Uncal Iso Platt Beta PlattBin Conf"</sub>
- **descriptive / method**: Experiment 1 results are shown as plots, with one plot per model type containing results for all setups. In the left part of each plot, every dot is a rejection level, with estimated accuracy on the x axis and actual (empirical) accuracy on the y axis. The right part shows the estimation error for the different rejection levels. (p. 7)[^original]  
  <sub>anchor: "Results are shown as plots, containing results for all setups for one model type in each plot."</sub>
- **descriptive / data or feature**: The accuracy estimation figures reject between 10% and 90% of cases, as stated in the figure captions (for example the DT figure on the puma8NH dataset). (p. 7)[^original]  
  <sub>anchor: "Fig. 2. DT accuracy estimation rejecting 10%–90% on puma8NH dataset."</sub>

---

[previous part](digest-003.md) | [source overview](overview.md) | [next part](digest-005.md)

[^original]: Academic publisher / repository, "Conformalized classifiers with reject option" (2026-02-24). https://doi.org/10.1016/j.mlwa.2026.100838
