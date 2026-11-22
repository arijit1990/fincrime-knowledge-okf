---
type: Source Digest
title: Conformalized classifiers with reject option - part 2 of 9 (pp. 4-6)
description: 'Verified paraphrased digest, pp. 4-6: A B S T R A C T'
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
part: 2
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
digest_points: 33
---

# Conformalized classifiers with reject option (digest)

[previous part](digest-001.md) | [source overview](overview.md) | [next part](digest-003.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (pp. 4-6) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **academic finding**.

## Abstract

- **descriptive / context**: Conformal classification has a drawback: if the label set contains all labels it cannot be an error, while an empty set must be an error; for two-class problems with few empty predictions, nearly all errors come from singleton predictions. (p. 4)[^original]  
  <sub>anchor: "if the label set contains all labels, it cannot be an error; while an empty set must be an error"</sub>
- **descriptive / context**: Because of this drawback, researchers and practitioners have moved away from conformal classification for uncertainty quantification in decision support, instead using probabilistic predictors. (p. 4)[^original]  
  <sub>anchor: "researchers and practitioners have moved away from conformal classification when it comes to uncertainty quantification for decision support"</sub>
- **descriptive / method**: Procedure for classification with reject option: sort predicted instances by confidence, pick one instance as a threshold to reject all instances with lower confidence and predict those with higher confidence. (p. 4)[^original]  
  <sub>anchor: "Pick one instance 𝛽𝑖 from this sorted sequence to reject all instances with a lower confidence"</sub>
- **descriptive / method**: For two-class problems where a batch of predictions can be observed, the error rate of singleton predictions for a given significance level can be estimated, since errors consist of empty predictions and incorrect singleton predictions; the expected number of errors is the significance level times the number of predictions k. (p. 4)[^original]  
  <sub>anchor: "we know that the errors consist of all empty predictions and incorrect singleton predictions"</sub>
- **descriptive / context**: The procedure differs from Johansson, Sönströd et al. (2023), which did not consider empty predictions; that earlier version would normally be slightly optimistic for the lowest rejection levels. (p. 4)[^original]  
  <sub>anchor: "Consequently, the previous version would normally be slightly optimistic for the lowest rejection levels."</sub>
- **descriptive / method**: The expected error rate of singleton predictions is corrected from the nominal significance level by subtracting the proportion of empty predictions and dividing by the proportion of singleton predictions, which quantifies reliability of non-rejected predictions. (p. 4)[^original]  
  <sub>anchor: "Eq. (8) thus provides a way to correct the nominal error rate 𝜖 for the fact that not all predictions are singletons."</sub>
- **descriptive / finding or result**: The proposed formulation retains the validity guarantees of standard conformal prediction while giving an interpretable mapping between rejection rate and expected predictive accuracy; estimation does not require knowing true test labels. (p. 4)[^original]  
  <sub>anchor: "the proposed formulation retains the validity guaran- tees of standard conformal prediction"</sub>
- **descriptive / method**: Expected accuracy of predicted instances is computed with equation (8) from the significance level, the proportion of empty predictions P(e), and the number of predicted instances P(s) at that level; epsilon equals 1 minus the confidence of the chosen instance beta_i. (p. 4)[^original]  
  <sub>anchor: "The expected accuracy of the predicted instances can be readily calculated using (8)"</sub>
- **descriptive / method**: P(e) corresponds to the instances with a credibility lower than epsilon, and P(s) is the number of predicted instances at epsilon, i.e., all instances with a confidence higher than beta_i. (p. 4)[^original]  
  <sub>anchor: "P(e) corre- sponds to the instances with a credibility lower than"</sub>
- **descriptive / requirement**: Two properties are sought for classification with reject option: predicted instances should be sortable by likelihood of being correct, giving a clear trade-off between non-rejected instances and accuracy; and predictive performance of non-rejected instances should be accurately estimable. (p. 5)[^original]  
  <sub>anchor: "It should be possible to sort the predicted instances based on their likelihood of being correct"</sub>
- **descriptive / method**: The approach builds on inductive conformal prediction: nonconformity scores and p-values are computed only once on the calibration set, and inference involves simple comparisons and ranking, with overhead negligible compared to Platt scaling or isotonic regression. (p. 5)[^original]  
  <sub>anchor: "The proposed approach builds on inductive conformal prediction, which is computationally efficient"</sub>
- **descriptive / method**: Mondrian conformal classifiers can be used with the procedure, giving different guarantees depending on the taxonomy; with categories determined by the underlying model's predicted label, the guarantee for the positive-class category is for precision. (p. 5)[^original]  
  <sub>anchor: "the guarantees for the category where the underlying model predicted the positive class (label 1), will in fact be for precision"</sub>
- **descriptive / method**: Procedure steps: predicted instances are sorted on increasing confidence, producing a sequence of instances, from which a threshold instance is picked. (p. 5)[^original]  
  <sub>anchor: "The predicted instances are sorted on increasing confidence producing the sequence"</sub>

## 4. Method

- **descriptive / data or feature**: Datasets are small and some imbalanced: for churn, HTRU2 and pc4 the proportion of positive instances is below 20%; for haberman, kc1, kc2 and transfusion it is between 20% and 30%. (p. 5)[^original]  
  <sub>anchor: "in churn, HTRU2 and pc4, the proportion of positive instances is less than 20%"</sub>
- **descriptive / context**: The empirical study aims to show how conformal classifiers can serve as the basis for classifiers with reject option, estimating accuracy or precision with statistical guarantees. (p. 5)[^original]  
  <sub>anchor: "capable of estimating the accuracy or precision level, with statistical guarantees"</sub>
- **descriptive / context**: Datasets were not chosen to represent specific domains but to give a broad, reproducible basis using widely used benchmark datasets of moderate size. (p. 5)[^original]  
  <sub>anchor: "provide a broad and reproducible basis for evaluation using widely used benchmark datasets of moderate size"</sub>

## 5. Results

- **descriptive / method**: Three classifiers were used: standard decision trees (scikit-learn), random forests (scikit-learn) and XGBoost (XGB Python package); defaults were used except 300 trees for random forests and XGB and min_leaf of 7 for decision trees. (p. 5)[^original]  
  <sub>anchor: "All parameters were left at default values, except the number of trees that was set to 300"</sub>
- **descriptive / method**: Experiment 1 estimates accuracy at a given reject level; Experiment 2 estimates precision. Six setups were used for each model type in both experiments. (p. 5)[^original]  
  <sub>anchor: "In Experiment 1, the models should estimate their accuracy, given a certain reject level."</sub>
- **descriptive / method**: The suggested conformalized approach is compared to probabilistic predictors, either uncalibrated or calibrated with one of four state-of-the-art techniques. (p. 5)[^original]  
  <sub>anchor: "we compare the suggested approach to using probabilistic predictors, either without calibration or calibrated"</sub>

## 5.1. Experiment 1

- **descriptive / method**: Calibration setups Platt, Iso (isotonic regression) use scikit-learn CalibratedClassifierCV with prefit; Beta uses the betacal package from Kull et al. (2017); PlattBin uses Platt-Binning. (p. 5)[^original]  
  <sub>anchor: "Models are calibrated using isotonic re- gression, also using the CalibratedClassifierCV method"</sub>
- **descriptive / method**: Conf setup: a standard conformal classifier with reject option in Experiment 1; a Mondrian version with categories by predicted label in Experiment 2, so only positive-class instances enter the calibration set there. (p. 5)[^original]  
  <sub>anchor: "Consequently, only instances belonging to the positive class are included in the calibration set in Experiment 2."</sub>

## 5.1. Experiment 1: Accuracy estimation

- **descriptive / method**: Uncal setup: raw model scores are used as probability estimates; the accuracy or precision estimate for a subset is the mean probability estimate for the predicted label of those instances. (p. 5)[^original]  
  <sub>anchor: "the accuracy or precision estimate for a certain subset of instances is the mean probability estimate"</sub>
- **descriptive / method**: In Experiment 1 all instances are considered for Uncal, whereas Experiment 2 considers only the instances predicted as the positive class. (p. 5)[^original]  
  <sub>anchor: "In Experiment 1, all instances are considered, but Experiment 2 considers only the instances predicted as the positive class."</sub>

## 4. Method

- **descriptive / expectation**: If the suggested procedure is based on standard conformal classifiers, the predictive performance guarantees are for predictive accuracy, and they hold under the same assumptions as conformal classification. (p. 5)[^original]  
  <sub>anchor: "If the suggested procedure is based on standard confor- mal classifiers, the guarantees will be for predictive accuracy."</sub>

## 5. Results

- **descriptive / method**: Reject proportions of 10% to 90% were evaluated using repeated hold-out with 100 repetitions of a 75/25 train/test split; calibration setups further split training data 67% training and 33% calibration, while Uncal trained on the entire training set. (p. 6)[^original]  
  <sub>anchor: "The protocol employed was repeated hold-out with 100 rep- etitions of a 75∕25 split"</sub>

## 5.1. Experiment 1

- **descriptive / finding or result**: Uncalibrated models give the best predictive performance when only performance is targeted, since no calibration set is needed; differences from calibrated setups are most often very small, about 0.01 for decision trees against the worst calibrated setup, and smaller for RF and XGB. (p. 6)[^original]  
  <sub>anchor: "Averaging over the 41 datasets, the difference between Uncal and the worst setup using calibration is approximately 0.01 for decision trees"</sub>
- **descriptive / method**: Statistical comparison used a Friedman test followed by a Nemenyi post-hoc test, following the procedure recommended in García and Herrera (2009). (p. 6)[^original]  
  <sub>anchor: "a Friedman test (Friedman, 1937), followed by a Nemenyi post-hoc test (Nemenyi, 1963)"</sub>
- **descriptive / finding or result**: For random forests, no calibration gives significantly higher accuracy and AUC than all calibrated setups; Platt scaling generally performs well; the conformalized approach is best calibrated for AUC but only third best for accuracy. (p. 6)[^original]  
  <sub>anchor: "The conformalized approach is the best calibrated setup for AUC, but only the third best for accuracy."</sub>
- **descriptive / finding or result**: Efficiency (average number of class labels in prediction sets) is lower for higher significance levels and easier datasets; decision trees are the weakest models overall and on most datasets; random forests generally beat XGBoost. (p. 6)[^original]  
  <sub>anchor: "Random forest models perform generally better than XGBoost overall"</sub>
- **descriptive / case example**: For the easy kr-vs-kp dataset at epsilon 0.05 and 0.10, the average number of labels is below 1.0, indicating empty prediction sets are necessary to reach the desired error rate. (p. 6)[^original]  
  <sub>anchor: "the average number of class labels included in the prediction is actually below 1.0"</sub>
- **descriptive / data or feature**: In total 41 publicly available two-class datasets are used, drawn from the UCI repository, PROMISE Software Engineering Repository or OpenML. (p. 6)[^original]  
  <sub>anchor: "In total, 41 publicly available two-class datasets are used for the ex- perimentation."</sub>
- **descriptive / data or feature**: Tables 2 and 3 report accuracy and AUC results at dataset level for all model types (DT, RF, XGB) and setups; Table 4 reports empirical error rates and efficiency for the conformal classifier. (p. 6)[^original]  
  <sub>anchor: "Tables 2 and 3 show accuracy and AUC results, on the dataset level"</sub>

## 5.1. Experiment 1: Accuracy estimation

- **descriptive / finding or result**: The conformal classification underlying the conformalized calibrator is empirically valid: setups almost perfectly match the chosen epsilon values 0.01, 0.05 and 0.10 overall, with very small dataset-level deviations (Table 4). (p. 6)[^original]  
  <sub>anchor: "all setups are, as expected, empirically valid, almost perfectly matching the chosen 𝜖-values overall"</sub>

---

[previous part](digest-001.md) | [source overview](overview.md) | [next part](digest-003.md)

[^original]: Academic publisher / repository, "Conformalized classifiers with reject option" (2026-02-24). https://doi.org/10.1016/j.mlwa.2026.100838
