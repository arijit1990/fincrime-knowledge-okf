---
type: Source Digest
title: Conformalized classifiers with reject option - part 1 of 9 (pp. 1-4)
description: 'Verified paraphrased digest, pp. 1-4: A B S T R A C T'
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
part: 1
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
digest_points: 139
---

# Conformalized classifiers with reject option (digest)

[source overview](overview.md) | [next part](digest-002.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (pp. 1-4) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **academic finding**.

## Abstract

- **descriptive / finding or result**: Under exchangeability, the proposed conformalized classifiers can perfectly estimate accuracy or precision for any rejection level. (p. 1)[^original]  
  <sub>anchor: "Under exchangeability, the proposed conformalized classifiers can perfectly estimate accuracy or precision for any rejection level."</sub>
- **descriptive / finding or result**: In an empirical investigation using 41 publicly available datasets, the conformalized classifiers with a reject option are reported to clearly outperform probabilistic predictors calibrated with state-of-the-art techniques. (p. 1)[^original]  
  <sub>anchor: "In an empirical investigation using 41 publicly available datasets, the conformalized classifiers with a reject option are shown to clearly outperform"</sub>

## 1. Introduction

- **descriptive / context**: In scenarios where acting on erroneous predictions has a high associated cost or risk, letting the classifier refrain from making uncertain predictions can be beneficial, citing Hanczar and Sebag (2014). (p. 1)[^original]  
  <sub>anchor: "in scenarios where acting on erroneous predictions has a high associated cost or risk"</sub>
- **descriptive / context**: In data-driven decision support, machine learning-generated predictive models are often the main source of information; a model provides predictions from a predefined set of class labels given the attribute values of an instance. (p. 1)[^original]  
  <sub>anchor: "In data-driven decision support, machine learning-generated pre- dictive models are often used as the main source of information."</sub>
- **descriptive / definition**: Binary classification is the case where the label set has two classes; many problems such as churn prediction, return prediction, loan application and spam filtering can be represented this way. (p. 1)[^original]  
  <sub>anchor: "Many problems from a variety of areas can be represented as binary classification"</sub>
- **descriptive / context**: For classification with reject option there is a trade-off between the accuracy of predicted instances and the rejection rate; where error costs differ strongly, the trade-off is instead between precision and recall. (p. 1)[^original]  
  <sub>anchor: "For classification with reject option, there is an obvious trade-off between the accuracy of the predicted instances and the rejection rate"</sub>
- **descriptive / definition**: Conformal classifiers output set predictions; for binary classification there are four possible prediction sets, namely the empty set, the set with label 0, the set with label 1, and the set with both labels. (p. 1)[^original]  
  <sub>anchor: "Conformal classifiers (Vovk et al., 2005) output set predictions, where for binary classification the four possible prediction sets are"</sub>
- **descriptive / definition**: Conformal set predictions carry a validity guarantee: in the long run the error rate, meaning the proportion of set predictions not including the true target, equals a significance level chosen by the user. (p. 1)[^original]  
  <sub>anchor: "These predictions come with a validity guarantee, where the error rate"</sub>
- **descriptive / context**: Most classifiers compute a score for each class and output the class label with the maximum likelihood. (p. 1)[^original]  
  <sub>anchor: "output the class label with the maximum likelihood"</sub>
- **descriptive / context**: For binary classifiers, many techniques make the class scores add up to 1.0 and these scores are often treated as probabilities. (p. 1)[^original]  
  <sub>anchor: "For binary classifiers, many techniques make these scores add up to 1.0, and they are often treated as probabilities."</sub>
- **descriptive / definition**: The maximum probability value of a prediction is sometimes referred to as the confidence in that prediction. (p. 1)[^original]  
  <sub>anchor: "the maximum probability value is sometimes referred to as the confidence in the prediction"</sub>
- **expected / requirement**: If classifier probabilities are to be useful beyond selecting the label, they need to be well-calibrated, meaning they correspond to the actual probability of the instance belonging to the predicted class. (p. 1)[^original]  
  <sub>anchor: "correspond to the actual (true) probability of the particular instance belonging to the predicted class"</sub>
- **permissive / context**: If probabilities are not well-calibrated, the probabilities output by a classifier may instead be outright misleading for a user. (p. 1)[^original]  
  <sub>anchor: "If this is not the case, probabilities output by a classifier may instead be outright misleading for a user."</sub>
- **descriptive / context**: For classification with reject option there is a trade-off between the accuracy of predicted instances and the rejection rate. (p. 1)[^original]  
  <sub>anchor: "there is an obvious trade-off between the accuracy of the predicted instances and the rejection rate"</sub>
- **descriptive / context**: Where the costs of false positives and false negatives differ greatly, the trade-off is instead between precision and recall. (p. 1)[^original]  
  <sub>anchor: "the trade-off is instead between precision and recall"</sub>
- **descriptive / definition**: For binary classification, conformal classifiers output set predictions from four possible prediction sets. (p. 1)[^original]  
  <sub>anchor: "for binary classification the four possible prediction sets are"</sub>
- **descriptive / definition**: Conformal classifiers come with a validity guarantee that the error rate, the proportion of set predictions not including the true target, equals a user-provided significance level in the long run. (p. 1)[^original]  
  <sub>anchor: "These predictions come with a validity guarantee, where the error rate"</sub>
- **descriptive / finding or result**: Applying a conformal classifier naively with a reject option would predict singleton label sets and reject instances with cardinality 0 or 2, but the error rate of the singleton predictions would then not meet the user's significance level. (p. 2)[^original]  
  <sub>anchor: "a conformal classifier would, if given the option to reject, predict the instances with singleton label sets, while rejecting instances with cardinality 0 or 2"</sub>
- **descriptive / finding or result**: The error rate of such singleton predictions would most likely be significantly higher than the significance level. (p. 2)[^original]  
  <sub>anchor: "the error rate would most likely be significantly higher than the significance level"</sub>
- **descriptive / context**: In classification with reject option the model is allowed to refrain from making predictions, typically for uncertain instances, while easier instances are predicted. (p. 2)[^original]  
  <sub>anchor: "In classification with reject option (Chow, 1970), however, the model is allowed to refrain from making predictions."</sub>
- **descriptive / context**: Conformal classification has only recently been used for classification with reject option, and a large majority of classification with reject approaches are based on probabilistic predictors. (p. 2)[^original]  
  <sub>anchor: "Instead, a large majority of all classification with reject approaches are based on probabilistic predictors."</sub>
- **descriptive / method**: Platt-Binning, a binning method combining Platt scaling and histogram binning, first applies Platt scaling and then bins the Platt scores into intervals with equal numbers of instances, using the average Platt score as the bin estimate. (p. 2)[^original]  
  <sub>anchor: "Platt-Binning (Singh & Goshtasbpour, 2022) is a binning method that combines Platt scaling and histogram binning."</sub>
- **descriptive / context**: The paper proposes conformalized classifiers with reject option, which need access to a set of test instances and therefore cannot be used in a streaming scenario, but yield well-calibrated probability estimates that inherit conformal validity guarantees. (p. 2)[^original]  
  <sub>anchor: "requires access to a set of test instances, i.e., it cannot be used in a streaming scenario"</sub>
- **descriptive / method**: The paper also shows how a so-called Mondrian conformal classifier can be used to produce well-calibrated precision estimates, for any rejection level. (p. 2)[^original]  
  <sub>anchor: "to produce well-calibrated precision estimates, for any rejection level."</sub>
- **descriptive / method**: Isotonic regression produces a dynamic binning and does not need a predetermined number of bins; it fits a non-decreasing stepwise function on the calibration set. (p. 2)[^original]  
  <sub>anchor: "Isotonic regression (Zadrozny & Elkan, 2001) produces a dynamic binning, i.e., it does not require a predetermined number of bins."</sub>
- **descriptive / context**: The paper is structured so that Section 2 gives background and related work, Section 3 presents the proposed approach, Section 4 describes experiments, Section 5 gives results and Section 6 concludes with suggestions for future work. (p. 2)[^original]  
  <sub>anchor: "Results are presented in Section 5, after which follows some concluding remarks in Section 6"</sub>

## 2. Background

- **descriptive / method**: Platt scaling fits a sigmoid function to classifier outputs to produce calibrated probability estimates for a class. (p. 2)[^original]  
  <sub>anchor: "one early but frequently applied method is Platt scaling (Platt, 1999), where a sigmoid function is fitted to the classifier outputs."</sub>

## 2.1. Probabilistic prediction and calibration

- **recommended / recommendation**: Beta calibration and Platt Binning should be considered state-of-the-art approaches for external calibration of predictive models, excluding deep neural networks. (p. 2)[^original]  
  <sub>anchor: "Beta calibration and Platt Binning should be considered state-of-the-art approaches for external calibration of predictive models, excluding deep neural networks."</sub>
- **descriptive / limitation**: Platt scaling implicitly assumes that the optimal calibration curve is a sigmoid, which may not be the case, but its result is normally significantly better than using no calibration. (p. 2)[^original]  
  <sub>anchor: "While Platt scaling implicitly assumes that the optimal calibration curve is a sigmoid, which may not be the case"</sub>
- **descriptive / finding or result**: Platt scaling is often deemed good enough in practice and remains the most frequently used external calibration technique even today. (p. 2)[^original]  
  <sub>anchor: "making Platt scaling the most frequently used (external) calibration technique even today."</sub>
- **descriptive / method**: Beta calibration, which can be regarded as an extension of Platt scaling, uses a calibration function with three parameters fitted on the calibration data. (p. 2)[^original]  
  <sub>anchor: "Beta calibration can be regarded as an extension of Platt scaling"</sub>
- **descriptive / definition**: A probabilistic predictor is well-calibrated if the probability of a label, given the probability estimate for that label, equals the probability estimate. (p. 2)[^original]  
  <sub>anchor: "A probabilistic predictor is said to be well-calibrated if the probability of a certain label, given a probability estimate for that label, equals the probability estimate"</sub>
- **descriptive / context**: As an example, a large number of predictions with mean probability estimate 0.90 would be expected to have an empirical error rate of 0.1. (p. 2)[^original]  
  <sub>anchor: "we would expect the empirical error rate of these predictions to be"</sub>
- **expected / requirement**: With probabilistic predictors used for reject option, instances below a threshold on the predicted-label probability are rejected, and the estimated accuracy of the remaining instances should be their average probability estimate for the predicted label. (p. 2)[^original]  
  <sub>anchor: "the estimated accuracy of the predicted instances should be their average probability estimate for the predicted label"</sub>
- **descriptive / limitation**: The accuracy estimates for probabilistic reject option approaches obviously require the probability estimates to be well-calibrated. (p. 2)[^original]  
  <sub>anchor: "However, this obviously requires the probability estimates to be well-calibrated."</sub>

## 2.2. Conformal classification

- **descriptive / finding or result**: Techniques such as decision trees and naive Bayes are often very poorly calibrated, and poor calibration also affects modern deep neural networks and traditional neural networks. (p. 2)[^original]  
  <sub>anchor: "techniques like decision trees (Provost & Domingos, 2003) and naive Bayes (Niculescu-Mizil & Caruana, 2005) are often very poorly calibrated"</sub>

## 1. Introduction

- **descriptive / limitation**: If a conformal classifier rejects by cardinality, the error rate of its singleton predictions would most likely not meet the user's significance level and would be significantly higher. (p. 2)[^original]  
  <sub>anchor: "the error rate of the singleton predictions would not meet the significance level provided by the user"</sub>
- **descriptive / limitation**: The empirical accuracy of singleton predictions, for a given significance level or rejection rate, could not be estimated in a straightforward way. (p. 2)[^original]  
  <sub>anchor: "the empirical accuracy of the singleton predictions, given a certain significance level"</sub>
- **descriptive / limitation**: Despite its strong validity guarantees, conformal classification has only recently been used for classification with reject option. (p. 2)[^original]  
  <sub>anchor: "only recently been used for classification with reject option"</sub>
- **descriptive / finding or result**: A large majority of classification with reject approaches are based on probabilistic predictors rather than conformal methods. (p. 2)[^original]  
  <sub>anchor: "a large majority of all classification with reject approaches are based on probabilistic predictors"</sub>
- **descriptive / context**: The overall purpose of the paper is to show how conformal classifiers can provide well-calibrated probability estimates for classification with reject option. (p. 2)[^original]  
  <sub>anchor: "demonstrate how conformal classifiers can be used to provide well-calibrated probability estimates"</sub>
- **descriptive / limitation**: The suggested conformalized procedure requires access to a set of test instances, so it cannot be used in a streaming scenario. (p. 2)[^original]  
  <sub>anchor: "it cannot be used in a streaming scenario"</sub>
- **descriptive / method**: Isotonic regression produces a dynamic binning and does not require a predetermined number of bins; it fits a non-decreasing stepwise function on the calibration set. (p. 2)[^original]  
  <sub>anchor: "produces a dynamic binning, i.e., it does not require a predetermined number of bins"</sub>

## 2. Background

- **descriptive / definition**: Platt-Binning is a binning method that combines Platt scaling and histogram binning. (p. 2)[^original]  
  <sub>anchor: "Platt-Binning (Singh & Goshtasbpour, 2022) is a binning method that combines Platt scaling and histogram binning"</sub>
- **descriptive / method**: In Platt-Binning, the probability estimate for a bin is the average Platt score of the bin rather than the proportion of positive labels. (p. 2)[^original]  
  <sub>anchor: "the probability estimate for a specific bin is the average Platt scores, rather than the proportion of positive labels"</sub>

## 2.1. Probabilistic prediction and calibration

- **recommended / recommendation**: Beta calibration and Platt Binning should be considered state-of-the-art approaches for external calibration of predictive models, excluding deep neural networks. (p. 2)[^original]  
  <sub>anchor: "Beta calibration and Platt Binning should be considered state-of-the-art approaches for external calibration of predictive models"</sub>
- **descriptive / method**: Beta calibration can be regarded as an extension of Platt scaling. (p. 2)[^original]  
  <sub>anchor: "Beta calibration can be regarded as an extension of Platt scaling"</sub>
- **descriptive / definition**: A probabilistic predictor is well-calibrated if the probability of a label given its probability estimate equals that estimate. (p. 2)[^original]  
  <sub>anchor: "A probabilistic predictor is said to be well-calibrated if the probability of a certain label"</sub>
- **descriptive / finding or result**: With a mean probability estimate of 0.90 across many predictions, the empirical error rate would be expected to be 0.1. (p. 2)[^original]  
  <sub>anchor: "if we make a (large) number of predictions, with the (mean) probability estimate 0.90"</sub>
- **descriptive / requirement**: Accuracy estimates for probabilistic reject option depend on the probability estimates being well-calibrated. (p. 2)[^original]  
  <sub>anchor: "this obviously requires the probability estimates to be well-calibrated"</sub>
- **expected / requirement**: Most probabilistic predictors need to be externally calibrated before being relied upon for decision support or automated decisions. (p. 2)[^original]  
  <sub>anchor: "most probabilistic predictors actually need to be (externally) calibrated before being relied upon for decision support"</sub>
- **descriptive / definition**: External calibration methods transform classifier scores into calibrated probability estimates using an additional labeled dataset. (p. 2)[^original]  
  <sub>anchor: "external calibration methods transform classifier scores into calibrated probability estimates using an additional labeled dataset"</sub>
- **descriptive / method**: Calibration techniques are divided into two groups, scaling and binning. (p. 2)[^original]  
  <sub>anchor: "Calibration techniques can be divided into two groups; scaling and binning."</sub>
- **descriptive / method**: Binning techniques sort calibration instances on the model's positive-class scores and return the positive proportion of the bin as the probability estimate. (p. 2)[^original]  
  <sub>anchor: "Binning techniques sort the calibration instances on the model output scores for the positive class"</sub>
- **descriptive / limitation**: Platt scaling implicitly assumes the optimal calibration curve is a sigmoid, which may not be the case. (p. 2)[^original]  
  <sub>anchor: "While Platt scaling implicitly assumes that the optimal calibration curve is a sigmoid, which may not be the case"</sub>
- **descriptive / finding or result**: Platt scaling normally performs significantly better than no calibration and is the most frequently used external calibration technique even today. (p. 2)[^original]  
  <sub>anchor: "making Platt scaling the most frequently used (external) calibration technique even today"</sub>

## 2.2. Conformal classification

- **descriptive / finding or result**: Almost all classifiers can return probability estimates, but these estimates are rarely well-calibrated. (p. 2)[^original]  
  <sub>anchor: "While almost all classifiers are able to return such probability estimates out-of-the-box, these are rarely well-calibrated"</sub>
- **descriptive / finding or result**: Techniques such as decision trees and naive Bayes are often very poorly calibrated. (p. 2)[^original]  
  <sub>anchor: "techniques like decision trees (Provost & Domingos, 2003) and naive Bayes"</sub>
- **descriptive / finding or result**: The poor calibration problem also applies to both modern deep neural networks and traditional neural networks. (p. 2)[^original]  
  <sub>anchor: "the problem of poor calibration also applies to both modern (i.e., deep) neural networks"</sub>
- **descriptive / definition**: In the conformal framework an error is committed when the true target is not in the predicted label set. (p. 2)[^original]  
  <sub>anchor: "an error is committed when the true target is not in the predicted label set"</sub>
- **descriptive / finding or result**: Conformal predictors are valid: the probability of error equals the user-controlled threshold parameter epsilon. (p. 2)[^original]  
  <sub>anchor: "the probability of making an error is equal to the user-controlled threshold parameter"</sub>
- **descriptive / finding or result**: Label set sizes are adjusted so that the probability of the prediction set not including the true label is exactly epsilon. (p. 2)[^original]  
  <sub>anchor: "the probability of the prediction set not including the true label is exactly"</sub>
- **descriptive / definition**: In the conformal prediction framework an error occurs when the true target is not in the predicted label set; the main benefit is that the predictors are valid, with error probability equal to the user-controlled threshold. (p. 3)[^original]  
  <sub>anchor: "The main benefit of conformal prediction is that the resulting predictors are valid"</sub>
- **descriptive / context**: External calibration methods transform classifier scores into calibrated probability estimates using an additional labeled dataset, and most probabilistic predictors need such calibration before being relied upon. (p. 3)[^original]  
  <sub>anchor: "On a high level, external calibration methods transform classifier scores into calibrated probability estimates using an additional labeled dataset."</sub>
- **descriptive / method**: Calibration techniques are divided into scaling techniques, which fit a function to the calibration outputs, and binning techniques, which sort and group calibration instances by score. (p. 3)[^original]  
  <sub>anchor: "Calibration techniques can be divided into two groups; scaling and binning."</sub>
- **descriptive / method**: For binning techniques, the probability estimate for a test instance is the proportion of positive labels in its bin. (p. 3)[^original]  
  <sub>anchor: "the proportion of positive labels in the bin is returned as the probability estimate."</sub>
- **descriptive / definition**: A nonconformity function measures the relative strangeness of an instance with its tentative label compared with instances with known target values; a label is rejected when its p-value is below the significance level. (p. 3)[^original]  
  <sub>anchor: "The nonconformity function measures the (relative) strangeness of the instance"</sub>
- **descriptive / method**: The paper employs the frequently used hinge loss as the nonconformity function, based on the probability estimate of the underlying model for the tentative label. (p. 3)[^original]  
  <sub>anchor: "we employ the frequently used nonconformity function hinge loss"</sub>
- **descriptive / definition**: Confidence-credibility measures are tied to set predictions: confidence is the highest significance level giving a singleton prediction, and credibility is the lowest significance level at which all labels are rejected. (p. 3)[^original]  
  <sub>anchor: "Confidence-credibility measures are tightly connected to the set predictions"</sub>
- **descriptive / method**: In an inductive conformal classifier, the labeled training data is split into a proper training set and a calibration set, the underlying model is trained on the proper training set, and nonconformity scores are computed for the calibration examples. (p. 3)[^original]  
  <sub>anchor: "Train the underlying model ℎ using the proper training set 𝑍𝑡."</sub>

## 2.3. Related work

- **descriptive / context**: A recent survey of classification with reject option identifies uncertainty quantification as a closely related research area. (p. 3)[^original]  
  <sub>anchor: "They identify uncertainty quantification as a research area closely related to classification with reject option."</sub>
- **descriptive / finding or result**: Franc et al. (2023) derive necessary and sufficient conditions for an optimal Bayesian prediction strategy when the underlying distribution is known, covering bounded-improvement and bounded-abstention cases. (p. 3)[^original]  
  <sub>anchor: "derive necessary and sufficient conditions for an optimal prediction strategy using a Bayesian approach"</sub>
- **descriptive / context**: Conformal prediction was first introduced through confidence sets defined as a classifier with reject option, and later derived for reject option in binary classification. (p. 3)[^original]  
  <sub>anchor: "Conformal prediction was first introduced through confidence sets defined as a classifier with reject option in Denis and Hebiri (2015)."</sub>
- **descriptive / finding or result**: A prior approach extended a perfectly calibrated reject option classifier into a conformal classifier that could guarantee both accuracy and precision. (p. 3)[^original]  
  <sub>anchor: "That approach was extended into a conformal classifier with reject option, which could guarantee both accuracy and precision"</sub>
- **descriptive / context**: Hallberg Szabadvary et al. (2025) provided examples covering several conformal prediction settings, from full conformal prediction to offline batch inductive conformal prediction. (p. 3)[^original]  
  <sub>anchor: "examples covering several different conformal prediction settings"</sub>
- **descriptive / context**: This paper builds on Johansson, Sönströd et al. (2023), covering both accuracy and precision guarantees, but modifies and further formalizes the approach and performs a large empirical investigation. (p. 3)[^original]  
  <sub>anchor: "This paper builds on Johansson, Sönströd, et al. (2023), i.e., it covers both accuracy and precision guarantees"</sub>
- **descriptive / method**: Because the study uses many benchmark datasets, statistical inference can be used to determine statistically significant differences in performance. (p. 3)[^original]  
  <sub>anchor: "statistical inference can be used to determine statistically significant differences in performance"</sub>
- **descriptive / requirement**: Under exchangeability of calibration and test sets, the probability that the prediction set includes the true label is exactly 1 minus the significance level. (p. 3)[^original]  
  <sub>anchor: "As long as the calibration set and the test set are exchangeable, the probability for the prediction sets"</sub>
- **descriptive / method**: If instances are divided into categories, a Mondrian conformal classifier can provide guarantees for each category separately, the most common example being a class-conditional classifier. (p. 3)[^original]  
  <sub>anchor: "can provide guarantees for each category separately"</sub>

## 3. Conformal classification with reject option

- **descriptive / method**: Confidence-credibility predictions can be used as an alternative to set predictions and produce for each test instance the predicted class label, the confidence and the credibility. (p. 3)[^original]  
  <sub>anchor: "As an alternative to the set predictions, confidence-credibility pre- dictions can be used."</sub>
- **descriptive / definition**: The predicted class label is the label with the highest p-value. (p. 3)[^original]  
  <sub>anchor: "i.e., the label with the highest"</sub>
- **descriptive / definition**: The credibility is equal to the largest p-value. (p. 3)[^original]  
  <sub>anchor: "The credibility, which is equal to the largest 𝑝-value."</sub>
- **descriptive / definition**: The confidence is calculated as one minus the second largest p-value. (p. 3)[^original]  
  <sub>anchor: "The confidence, calculated as one minus the second largest"</sub>
- **descriptive / limitation**: The validity guarantees apply only a priori; once a predicted label set has been observed, the risk of error is highly dependent on the observed set. (p. 3)[^original]  
  <sub>anchor: "the validity guarantees only apply a priori; when a predicted label set has been observed"</sub>

## 2.2. Conformal classification

- **descriptive / method**: Under mild conditions the conformal prediction set is guaranteed to contain the true target with probability 1 minus epsilon. (p. 3)[^original]  
  <sub>anchor: "under mild conditions, guaranteed to contain the true target"</sub>
- **descriptive / method**: Platt scaling fits a sigmoid function to the classifier outputs. (p. 3)[^original]  
  <sub>anchor: "where a sigmoid function is fitted to the classifier outputs"</sub>
- **descriptive / definition**: The nonconformity function measures the relative strangeness of an instance compared to instances with known target values. (p. 3)[^original]  
  <sub>anchor: "The nonconformity function measures the (relative) strangeness of the instance"</sub>
- **descriptive / method**: Conformal classification on machine learning models normally bases the nonconformity function on the underlying model's prediction, here the hinge loss. (p. 3)[^original]  
  <sub>anchor: "we employ the frequently used nonconformity function hinge loss"</sub>
- **descriptive / definition**: The credibility is equal to the largest p-value. (p. 3)[^original]  
  <sub>anchor: "The credibility, which is equal to the largest"</sub>
- **descriptive / definition**: The confidence is calculated as one minus the second largest p-value. (p. 3)[^original]  
  <sub>anchor: "The confidence, calculated as one minus the second largest"</sub>
- **descriptive / definition**: Confidence and credibility are linked to set predictions: confidence is the highest significance level giving a singleton prediction. (p. 3)[^original]  
  <sub>anchor: "the confidence represents the highest significance level where we get a singleton prediction"</sub>

## 2.3. Related work

- **descriptive / method**: In the inductive conformal classifier procedure the labeled training data is divided into two disjoint subsets, a proper training set and a calibration set. (p. 3)[^original]  
  <sub>anchor: "Divide the labeled training data 𝑍 into two disjoint subsets"</sub>
- **descriptive / method**: The underlying model is trained using the proper training set only. (p. 3)[^original]  
  <sub>anchor: "Train the underlying model ℎ using the proper training set"</sub>
- **descriptive / method**: The nonconformity function is applied to all calibration examples to generate a list of calibration scores. (p. 3)[^original]  
  <sub>anchor: "Apply the nonconformity function, e.g., Eq. (4), to all calibration examples"</sub>
- **descriptive / method**: For a test instance, labels with a p-value below epsilon are rejected and the remaining labels form the predicted label set. (p. 3)[^original]  
  <sub>anchor: "Reject all labels ̃𝑦 where 𝑝̃𝑦 𝑘+1 < 𝜖."</sub>
- **descriptive / method**: The final predicted label set consists of all labels that were not rejected. (p. 3)[^original]  
  <sub>anchor: "Return the final predicted label set 𝛤𝜖 𝑘+1 consisting of all labels that were not rejected"</sub>
- **descriptive / finding or result**: Franc et al. derive necessary and sufficient conditions for an optimal Bayesian prediction strategy when the underlying distribution is known. (p. 3)[^original]  
  <sub>anchor: "derive necessary and sufficient conditions for an optimal prediction strategy using a Bayesian approach"</sub>
- **descriptive / definition**: Franc et al.'s bounded-improvement case provides guaranteed selective risk and maximal cover. (p. 3)[^original]  
  <sub>anchor: "the bounded-improvement (providing guaranteed selective risk and maximal cover)"</sub>
- **descriptive / definition**: Franc et al.'s bounded-abstention case provides guaranteed cover and minimal selective risk. (p. 3)[^original]  
  <sub>anchor: "bounded-abstention (providing guaranteed cover and minimal selective risk)"</sub>
- **descriptive / context**: Existing reject option approaches can give excellent empirical performance but few offer formal guarantees on predictive reliability. (p. 3)[^original]  
  <sub>anchor: "Existing approaches to classification with a reject option can provide excellent empirical performance, but few offer formal guarantees"</sub>
- **descriptive / context**: Most existing approaches rely on heuristically calibrated probabilistic scores, which are difficult to interpret in high-stakes decision support. (p. 3)[^original]  
  <sub>anchor: "Most rely on probabilistic scores that are heuris- tically calibrated and therefore difficult to interpret in high-stakes decision-support settings"</sub>
- **descriptive / context**: A recent survey identifies uncertainty quantification as a research area closely related to classification with reject option. (p. 3)[^original]  
  <sub>anchor: "They identify uncertainty quantification as a research area closely related to classification with reject option"</sub>
- **descriptive / context**: Conformal prediction was first introduced as confidence sets defined as a classifier with reject option. (p. 3)[^original]  
  <sub>anchor: "Conformal prediction was first introduced through confidence sets defined as a classifier with reject option"</sub>
- **descriptive / finding or result**: Johansson et al. (2023) suggested a method producing a perfectly calibrated classifier with reject option. (p. 3)[^original]  
  <sub>anchor: "a method producing a perfectly calibrated classifier with reject option"</sub>
- **descriptive / finding or result**: That approach was later extended into a conformal classifier with reject option guaranteeing both accuracy and precision. (p. 3)[^original]  
  <sub>anchor: "That approach was extended into a conformal classifier with reject option, which could guarantee both accuracy and precision"</sub>
- **descriptive / context**: This paper builds on Johansson, Sönströd et al. (2023), covering accuracy and precision guarantees, with a modified and more formalized approach. (p. 3)[^original]  
  <sub>anchor: "This paper builds on Johansson, Sönströd, et al. (2023)"</sub>
- **descriptive / method**: The paper includes a large and rigorous empirical investigation comparing the conformalized approach with calibrated probabilistic predictors. (p. 3)[^original]  
  <sub>anchor: "In addition, a large and rigorous empirical investigation is performed"</sub>
- **descriptive / requirement**: Conformal validity holds as long as the calibration set and the test set are exchangeable. (p. 3)[^original]  
  <sub>anchor: "As long as the calibration set and the test set are exchangeable"</sub>
- **descriptive / method**: A Mondrian conformal classifier can provide guarantees separately for each category, the most common example being class-conditional. (p. 3)[^original]  
  <sub>anchor: "The most common example is a class-conditional conformal classifier, where the errors are bound for each class"</sub>
- **descriptive / method**: To generate a Mondrian conformal classifier, the p-value formula is redefined per category, with r the number of calibration instances in the category. (p. 3)[^original]  
  <sub>anchor: "To generate a Mondrian conformal classifier, (5) simply needs to be redefined as"</sub>
- **descriptive / data or feature**: In the Mondrian formula r denotes the number of calibration instances in the category. (p. 3)[^original]  
  <sub>anchor: "is the number of calibration instances in the category"</sub>
- **descriptive / finding or result**: The proposed conformalized formulation combines practical readiness of probabilistic predictors with formal validity of conformal methods. (p. 3)[^original]  
  <sub>anchor: "enabling reliable accuracy and precision estimation under controlled rejection"</sub>

## 3. Conformal classification with reject option

- **descriptive / limitation**: Despite the strong guarantees, conformal classifiers are rarely used for decision making. (p. 3)[^original]  
  <sub>anchor: "Despite the strong guarantees, conformal classifiers are rarely used for decision making"</sub>
- **descriptive / limitation**: The difficulty is that it is not straightforward to estimate the probability that singleton predictions are in fact correct. (p. 3)[^original]  
  <sub>anchor: "the problem is that it is not straightforward to estimate the probability that these are in fact correct"</sub>
- **descriptive / limitation**: The error probability of singleton predictions is likely to be significantly higher than epsilon. (p. 3)[^original]  
  <sub>anchor: "the error probability is likely to be (significantly) higher than"</sub>
- **descriptive / limitation**: The validity guarantees apply only a priori; once a predicted label set is observed, the risk of error depends heavily on it. (p. 3)[^original]  
  <sub>anchor: "the validity guarantees only apply a priori"</sub>
- **descriptive / limitation**: When a predicted label set has been observed, the risk of an error is highly dependent on that set. (p. 3)[^original]  
  <sub>anchor: "when a predicted label set has been observed, the risk of an error is highly dependent"</sub>
- **descriptive / data or feature**: Table 1 describes the datasets by number of instances, number of input attributes and proportion of instances in the positive class, with source indicated as OpenML, UCI or Promise. (p. 4)[^original]  
  <sub>anchor: "Dataset descriptions — showing number of instances, number of input attributes and the proportion of instances that belongs to the positive class."</sub>

## Table 1

- **descriptive / data or feature**: Table 1 gives for each dataset the number of instances, number of input attributes, proportion of positive class instances and source; first rows include ailerons, bank8FM, banknote, churn, colic, creditA and deltaA. (p. 4)[^original]  
  <sub>anchor: "showing number of instances, number of input attributes and the proportion of instances that belongs to the positive class"</sub>
- **descriptive / data or feature**: Table 1 rows: ailerons 13750 instances, 40 attributes, positive proportion 0.58, OpenML; kc1 1192, 21, 0.26, Promise. (p. 4)[^original]  
  <sub>anchor: "ailerons 13 750 40 0.58 OpenML kc1 1192 21 0.26 Promise"</sub>
- **descriptive / data or feature**: Table 1 rows: bank8FM 8192 instances, 8 attributes, 0.60, OpenML; kc2 369, 21, 0.27, Promise. (p. 4)[^original]  
  <sub>anchor: "bank8FM 8192 8 0.60 OpenML kc2 369 21 0.27 Promise"</sub>
- **descriptive / data or feature**: Table 1 rows: banknote 1372 instances, 4 attributes, 0.44, OpenML; kin8 nm 8192, 8, 0.49, OpenML. (p. 4)[^original]  
  <sub>anchor: "banknote 1372 4 0.44 OpenML kin8 nm 8192 8 0.49 OpenML"</sub>
- **descriptive / data or feature**: Table 1 rows: churn 5000 instances, 20 attributes, 0.14, UCI; kr-vs-kp 3196, 36, 0.52, UCI. (p. 4)[^original]  
  <sub>anchor: "churn 5000 20 0.14 UCI kr-vs-kp 3196 36 0.52 UCI"</sub>
- **descriptive / data or feature**: Table 1 rows: colic 357 instances, 59 attributes, 0.62, UCI; liver 341, 6, 0.58, UCI. (p. 4)[^original]  
  <sub>anchor: "colic 357 59 0.62 UCI liver 341 6 0.58 UCI"</sub>
- **descriptive / data or feature**: Table 1 rows: creditA 690 instances, 42 attributes, 0.44, UCI; mozilla4 15545, 5, 0.67, OpenML. (p. 4)[^original]  
  <sub>anchor: "creditA 690 42 0.44 UCI mozilla4 15 545 5 0.67 OpenML"</sub>
- **descriptive / data or feature**: Table 1 rows: deltaA 7129 instances, 5 attributes, 0.47, OpenML; pc1req 104, 8, 0.47, Promise. (p. 4)[^original]  
  <sub>anchor: "deltaA 7129 5 0.47 OpenML pc1req 104 8 0.47 Promise"</sub>
- **descriptive / data or feature**: Table 1 rows: deltaE 9517 instances, 6 attributes, 0.50, OpenML; pc4 1343, 37, 0.13, Promise. (p. 4)[^original]  
  <sub>anchor: "deltaE 9517 6 0.50 OpenML pc4 1343 37 0.13 Promise"</sub>
- **descriptive / data or feature**: Table 1 rows: diabetes 768 instances, 8 attributes, 0.35, UCI; phish 11055, 30, 0.56, UCI. (p. 4)[^original]  
  <sub>anchor: "diabetes 768 8 0.35 UCI phish 11 055 30 0.56 UCI"</sub>
- **descriptive / data or feature**: Table 1 rows: EEG_eye 14980 instances, 14 attributes, 0.45, UCI; phoneme 5404, 5, 0.29, OpenML. (p. 4)[^original]  
  <sub>anchor: "EEG_eye 14 980 14 0.45 UCI phoneme 5404 5 0.29 OpenML"</sub>
- **descriptive / data or feature**: Table 1 rows: elevators 16599 instances, 18 attributes, 0.69, OpenML; puma8NH 8192, 8, 0.50, OpenML. (p. 4)[^original]  
  <sub>anchor: "elevators 16 599 18 0.69 OpenML puma8NH 8192 8 0.50 OpenML"</sub>
- **descriptive / data or feature**: Table 1 rows: german 955 instances, 27 attributes, 0.70, UCI; qsarbiodeg 1055, 41, 0.34, OpenML. (p. 4)[^original]  
  <sub>anchor: "german 955 27 0.70 UCI qsarbiodeg 1055 41 0.34 OpenML"</sub>
- **descriptive / data or feature**: Table 1 rows: haberman 283 instances, 3 attributes, 0.28, UCI; sonar 208, 60, 0.53, UCI. (p. 4)[^original]  
  <sub>anchor: "haberman 283 3 0.28 UCI sonar 208 60 0.53 UCI"</sub>
- **descriptive / data or feature**: Table 1 rows: heartC 302 instances, 22 attributes, 0.46, UCI; spambase 4601, 57, 0.39, UCI. (p. 4)[^original]  
  <sub>anchor: "heartC 302 22 0.46 UCI spambase 4601 57 0.39 UCI"</sub>
- **descriptive / data or feature**: Table 1 rows: heartH 293 instances, 20 attributes, 0.36, UCI; spect 218, 22, 0.89, UCI. (p. 4)[^original]  
  <sub>anchor: "heartH 293 20 0.36 UCI spect 218 22 0.89 UCI"</sub>
- **descriptive / data or feature**: Table 1 rows: heartS 270 instances, 13 attributes, 0.44, UCI; spectf 267, 44, 0.79, UCI. (p. 4)[^original]  
  <sub>anchor: "heartS 270 13 0.44 UCI spectf 267 44 0.79 UCI"</sub>
- **descriptive / data or feature**: Table 1 rows: houses 20640 instances, 8 attributes, 0.57, OpenML; transfusion 502, 4, 0.26, UCI. (p. 4)[^original]  
  <sub>anchor: "houses 20 640 8 0.57 OpenML transfusion 502 4 0.26 UCI"</sub>
- **descriptive / data or feature**: Table 1 rows: HTRU2 17897 instances, 8 attributes, 0.09, OpenML; ttt 958, 27, 0.65, UCI. (p. 4)[^original]  
  <sub>anchor: "HTRU2 17 897 8 0.09 OpenML ttt 958 27 0.65 UCI"</sub>
- **descriptive / data or feature**: Table 1 rows: iono 350 instances, 33 attributes, 0.64, UCI; vote 517, 16, 0.28, UCI. (p. 4)[^original]  
  <sub>anchor: "iono 350 33 0.64 UCI vote 517 16 0.28 UCI"</sub>
- **descriptive / data or feature**: Table 1 rows: je4042 270 instances, 8 attributes, 0.50, Promise; wbc 683, 9, 0.35, UCI; je4243 363, 8, 0.56, Promise. (p. 4)[^original]  
  <sub>anchor: "je4042 270 8 0.50 Promise wbc 683 9 0.35 UCI je4243 363 8 0.56 Promise"</sub>

---

[source overview](overview.md) | [next part](digest-002.md)

[^original]: Academic publisher / repository, "Conformalized classifiers with reject option" (2026-02-24). https://doi.org/10.1016/j.mlwa.2026.100838
