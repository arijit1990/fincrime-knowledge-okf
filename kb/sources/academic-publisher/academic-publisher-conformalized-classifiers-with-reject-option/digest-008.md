---
type: Source Digest
title: Conformalized classifiers with reject option - part 8 of 9 (pp. 12-15)
description: 'Verified paraphrased digest, pp. 12-15: A B S T R A C T'
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
part: 8
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
digest_points: 30
---

# Conformalized classifiers with reject option (digest)

[previous part](digest-007.md) | [source overview](overview.md) | [next part](digest-009.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (pp. 12-15) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **academic finding**.

## Experiment 2: Conformal classification (Table 7)

- **descriptive / finding or result**: Across all 41 datasets in Table 7, the mean error at epsilon 0.01 is about 0.010 for each model, with mean AvgC of 1.824 (DT), 1.650 (XGB) and 1.635 (RF). (p. 12)[^original]  
  <sub>anchor: "Mean 0.010 0.010 0.010 1.824 1.650 1.635 0.049 0.049 0.050"</sub>
- **descriptive / finding or result**: At epsilon 0.1 the table's mean error is about 0.098 (DT), 0.100 (XGB) and 0.100 (RF), with mean AvgC of 1.309, 1.232 and 1.205. (p. 12)[^original]  
  <sub>anchor: "0.098 0.100 0.100 1.309 1.232 1.205"</sub>
- **descriptive / finding or result**: Average ranks by AvgC in Table 7 are 2.85, 2.29 and 1.58 for DT, XGB and RF at epsilon 0.01; 2.80, 2.25 and 1.60 at 0.05; and 2.78, 2.29 and 1.61 at 0.1, with RF ranked best. (p. 12)[^original]  
  <sub>anchor: "Rank – – – 2.85 2.29 1.58 – – – 2.80 2.25 1.60 – – – 2.78 2.29 1.61"</sub>
- **descriptive / data or feature**: Table 7 reports detailed Experiment 2 conformal classification results for each data set, giving Error and AvgC for DT, XGB and RF at significance levels 0.01, 0.05 and 0.1. (p. 12)[^original]  
  <sub>anchor: "Table 7 Detailed results Experiment 2: Conformal classification. Data sets"</sub>
- **descriptive / finding or result**: At epsilon 0.05 the table's mean error is 0.049 for DT and XGB and 0.050 for RF, with mean AvgC of 1.500 for DT, 1.385 for XGB and 1.361 for RF. (p. 12)[^original]  
  <sub>anchor: "0.049 0.049 0.050 1.500 1.385 1.361"</sub>

## Experiment 2: Precision estimation

- **descriptive / finding or result**: Beta calibration is slightly over-confident across all reject levels in the examined example. (p. 13)[^original]  
  <sub>anchor: "Beta is slightly over-confident across all reject levels."</sub>
- **descriptive / method**: Absolute estimation errors for precision are assessed at the four rejection levels 30%, 50%, 70% and 90%, comparing six setups per technique using Friedman tests followed by Nemenyi post-hoc tests. (p. 13)[^original]  
  <sub>anchor: "we look at absolute estimation errors for precision, for the different setups on the four rejection levels of 30%, 50%, 70%, and 90%."</sub>
- **descriptive / finding or result**: Figure 9 shows XGB precision estimation with rejection from 10% to 90% on the Elevators dataset. (p. 13)[^original]  
  <sub>anchor: "Fig. 9. XGB: precision estimation rejecting 10%–90% on Elevators dataset."</sub>
- **descriptive / finding or result**: Figure 10 shows RF precision estimation with rejection from 10% to 90% on the pc4 dataset. (p. 13)[^original]  
  <sub>anchor: "Fig. 10. RF: precision estimation rejecting 10%–90% on pc4 dataset."</sub>
- **descriptive / finding or result**: For decision trees, using no calibration (Uncal) is significantly worse than all other setups at the four chosen rejection levels, with its average rank close to 6 in each case. (p. 13)[^original]  
  <sub>anchor: "using no calibration (Uncal) is significantly worse than all other setups, for the four chosen rejection levels."</sub>
- **descriptive / finding or result**: For decision trees, Iso, Beta, Platt and PlattBin show no significant differences at any of the four rejection levels; rank differences are small at 30% and 50% but increase at 70% and 90%, where Platt scaling achieves better results overall. (p. 13)[^original]  
  <sub>anchor: "there are no significant differences between Iso, Beta, Platt and PlattBin at any of the four rejection levels."</sub>
- **descriptive / finding or result**: For decision trees the Mondrian conformal classifier (Conf) gives significantly better precision estimates than all other setups at all four rejection levels, with its advantage growing as rejection increases; at 90% its mean rank is just above 1.0. (p. 13)[^original]  
  <sub>anchor: "at the 90% rejection level, the mean rank is just above 1.0, indicating the best performance on almost all datasets."</sub>
- **descriptive / finding or result**: For XGB, Conf is significantly better than all competing approaches at all rejection levels (Figure 12, alpha 0.05). (p. 13)[^original]  
  <sub>anchor: "Most importantly, Conf is actually significantly better than all competing approaches, for all rejection levels."</sub>
- **descriptive / finding or result**: For random forests, Conf significantly outperforms all probabilistic approaches at all rejection levels (Figure 13, alpha 0.05). (p. 13)[^original]  
  <sub>anchor: "Conf again significantly outperforms all probabilistic approaches, for all rejection levels, see Fig. 13."</sub>
- **descriptive / finding or result**: Summarising Experiment 2 for precision estimation, the conformal approach is the most accurate: for almost all underlying models and rejection rates its estimates were significantly more accurate than all probabilistic alternatives. (p. 13)[^original]  
  <sub>anchor: "for almost all underlying models and rejection rates, the confor- mal estimations were significantly more accurate than all probabilistic alternatives."</sub>

## Concluding remarks

- **descriptive / finding or result**: The experiments show the benefit of conformalized classifiers in a classification with reject scenario, giving a decision-maker a direct way to control the accuracy or precision versus rejection rate trade-off. (p. 13)[^original]  
  <sub>anchor: "the suggested approach provides a decision-maker with a direct way of controlling the accuracy (or precision) vs. rejection rate."</sub>

## Experiment 2: Precision estimation

- **descriptive / finding or result**: Conf gives the best precision estimate at all rejection levels in the example discussed, but its results vary somewhat more than in the two previous examples. (p. 13)[^original]  
  <sub>anchor: "Conf achieves the best precision estimate at all rejection levels, but exhibits a bit more variation"</sub>
- **descriptive / finding or result**: For PlattBin and Conf, actual precision decreases slightly at the highest rejection levels; the excerpt says calibration does not capture this, which increases errors at the highest rejection level. (p. 13)[^original]  
  <sub>anchor: "Notably, for PlattBin and Conf, actual precision decreases slightly at the highest rejection levels"</sub>

## 6. Concluding remarks

- **descriptive / finding or result**: A large-scale empirical study using 41 benchmark datasets found the proposed method produces highly reliable accuracy and precision estimates. (p. 14)[^original]  
  <sub>anchor: "Through a large-scale empirical study using 41 benchmark datasets, we demonstrated that the proposed method produces highly reliable"</sub>
- **descriptive / finding or result**: Compared with uncalibrated and calibrated probabilistic predictors, the conformalized classifiers consistently outperformed the alternatives and were the only method that avoided systematic bias in accuracy and precision estimates across rejection levels. (p. 14)[^original]  
  <sub>anchor: "it was the only method that avoided systematic bias in accuracy and precision estima- tions for the different rejection levels."</sub>
- **descriptive / finding or result**: The method was robust across multiple classification models, including decision trees, random forests and XGBoost. (p. 14)[^original]  
  <sub>anchor: "the method proved to be robust across multiple classification models, including decision trees, random forests, and XGBoost."</sub>
- **descriptive / context**: Conformalized classifiers with a reject option are presented as useful where incorrect predictions carry significant costs, with harder instances handled separately, e.g. through human oversight. (p. 14)[^original]  
  <sub>anchor: "By allow- ing harder instances to be handled separately, e.g., through human oversight, this approach ensures a more controlled decision-making process."</sub>
- **descriptive / finding or result**: Conformal calibration is described as offering exact, distribution-free guarantees on predictive reliability for any underlying model, without additional training or tuning. (p. 14)[^original]  
  <sub>anchor: "conformal calibration offers exact, distribution-free guarantees on pre- dictive reliability for any underlying model, without additional training or tuning."</sub>
- **permissive / recommendation**: A natural extension is to investigate alternative Mondrian taxonomies, including class-conditional conformal prediction, which could provide further improvements in performance estimation. (p. 14)[^original]  
  <sub>anchor: "A natural extension of this work is to investigate alternative Mon- drian taxonomies, including class-conditional conformal prediction, which could provide further improvements"</sub>
- **descriptive / context**: Bayesian inference and ensemble methods such as Monte Carlo dropout and deep ensembles often yield well-calibrated probability estimates in practice, but they give only approximate uncertainty quantification and typically require model-specific assumptions or repeated training and sampling. (p. 14)[^original]  
  <sub>anchor: "they provide only approximate uncertainty quantification and typically require model- specific assumptions or repeated training and sampling."</sub>
- **descriptive / context**: The approach is particularly relevant for decision-support systems in high-importance domains, examples given being medical diagnostics, financial risk assessment and industrial process monitoring, where erroneous predictions may have significant consequences. (p. 15)[^original]  
  <sub>anchor: "Examples include areas such as medical diagnostics, financial risk assessment, and industrial process monitoring"</sub>
- **descriptive / context**: When a specific class is of primary interest, as in the precision estimation experiment, all other classes can be aggregated to form an effective binary setting, allowing the same reject mechanism to be applied. (p. 15)[^original]  
  <sub>anchor: "all other classes can be aggregated to form an effective binary setting, allowing the same"</sub>
- **expected / recommendation**: A full treatment of the multi-class case is identified as an important direction for future work. (p. 15)[^original]  
  <sub>anchor: "A full treatment of the multi-class case, is an important direction for future work."</sub>
- **descriptive / limitation**: The conformalized estimator's errors come from empty and incorrect singleton prediction sets, so for multi-class problems, where errors can arise from any non-full prediction set, the procedure does not directly extend beyond two classes. (p. 15)[^original]  
  <sub>anchor: "meaning that the present procedure does not directly extend beyond two classes."</sub>
- **descriptive / context**: When one class is of primary interest, as in the precision estimation experiment, the other classes can be aggregated into an effective binary setting so the same reject mechanism applies. (p. 15)[^original]  
  <sub>anchor: "all other classes can be aggregated to form an effective binary setting, allowing the same"</sub>

---

[previous part](digest-007.md) | [source overview](overview.md) | [next part](digest-009.md)

[^original]: Academic publisher / repository, "Conformalized classifiers with reject option" (2026-02-24). https://doi.org/10.1016/j.mlwa.2026.100838
