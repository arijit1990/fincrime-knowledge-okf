---
type: Source Digest
title: A Survey of Predictive Modelling under Imbalanced Distributions - part 1 of 5 (pp. 1-14)
description: 'Verified paraphrased digest, pp. 1-14: A Survey of Predictive Modelling under Imbalanced Distributions; A Survey of Predictive Modelling under Imbalanced Distributions > 1 Introduction; A Survey of Predictive Modelling under Imbalanced Distributions > 2 Problem Definition; and 2 more sections'
resource: https://arxiv.org/abs/1505.01658
tags:
- academic_finding
- fraud_screening_synergies
- global_academic
- ml_statistics
- preprint
status: stable
source_id: arxiv-a-survey-of-predictive-modelling-under-imbalanced-distributions
issuer: arxiv
issuer_name: arXiv
jurisdictions:
- GLOBAL_ACADEMIC
tier: 3
instrument_type: preprint
normative_force: academic_finding
publication_date: '2015-05-07'
legal_status: unknown
part: 1
parts_total: 5
content_mode: digest
generated:
  by: claude-code-subagent/claude-sonnet-5-5
  at: '2026-11-22T14:46:03Z'
verified:
- by: process:kb-digest-check/anchor-match
  at: '2026-11-22T14:46:03Z'
- by: claude-code-judge-agent/claude-opus-5-5
  at: '2026-11-22T14:46:03Z'
sources:
- id: original
  resource: https://arxiv.org/abs/1505.01658
  title: A Survey of Predictive Modelling under Imbalanced Distributions
  author: org:arxiv
  last_modified: '2015-05-07T00:00:00Z'
digest_points: 56
---

# A Survey of Predictive Modelling under Imbalanced Distributions (digest)

[source overview](overview.md) | [next part](digest-002.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (pp. 1-14) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **academic finding**.

## Abstract

- **descriptive / context**: Imbalanced target distributions are common in applications such as fraud detection and unusual stock returns, where the rare target values are often the most relevant to end users and carry different costs and benefits. (p. 1)[^original]  
  <sub>anchor: "the least common values of this target variable are associated with events that are highly relevant for end users"</sub>
- **descriptive / context**: The survey covers existing techniques for both classification (nominal target) and regression (numeric target) tasks, discusses challenges, proposes a taxonomy of methods and refers to related problems. (p. 1)[^original]  
  <sub>anchor: "Although most of the existing work addresses classification tasks (nominal target variables), we also describe methods"</sub>

## 1 Introduction

- **descriptive / context**: Predictive modelling builds a model of an unknown function from a training sample; classification applies when the target is nominal and regression when it is numeric. (p. 1)[^original]  
  <sub>anchor: "Dependingonthetypeofthe variable _Y_ , we face either a classification task (nominal _Y_ ) or a regression task"</sub>
- **descriptive / context**: The most frequent model-fitting criteria are the error rate for classification and the mean squared error for regression. (p. 1)[^original]  
  <sub>anchor: "The most frequent criteria are the error rate for classification and the mean squared error for regression."</sub>
- **descriptive / context**: Examples where accuracy in a sub-range of the target domain matters include diagnosis of rare diseases and forecasting rare extreme returns on financial markets; such sub-ranges are poorly represented in training samples. (p. 1)[^original]  
  <sub>anchor: "Examples include diagnostic of rare diseases, forecasting rare extreme returns on financial markets"</sub>
- **descriptive / finding or result**: Without addressing evaluation metrics and learning focus, models tend to be biased to frequent, uninteresting cases and standard metrics fail to capture competence on rare cases. (p. 1)[^original]  
  <sub>anchor: "models will tend to be biased to the most frequent (and uninteresting for the user) cases"</sub>
- **descriptive / finding or result**: Existing surveys address only classification imbalance; this paper's coverage of assessment measures and approaches for both classification and regression is presented as innovative. (p. 2)[^original]  
  <sub>anchor: "Therefore, the coverage of performance assessment measures and approaches to tackle both classification and regression tasks is an innovative aspect"</sub>
- **descriptive / context**: The paper claims its taxonomy extends previous taxonomies by including post-processing strategies. (p. 2)[^original]  
  <sub>anchor: "Our proposal extends previous taxonomies by including post-processing strategies."</sub>
- **descriptive / context**: The stated contributions are a general definition of imbalanced domains, a review of performance measures, a taxonomy of approaches and a description of key techniques. (p. 2)[^original]  
  <sub>anchor: "provide a general definition of the problem of imbalanced domains suitable for classification and regression tasks"</sub>

## 2 Problem Definition

- **descriptive / definition**: A relevance function maps target values to an importance range where 1 is maximal importance and 0 minimal relevance; a relevance threshold splits training cases into a relevant subset DR and a normal subset DN. (p. 3)[^original]  
  <sub>anchor: "where 1 is maximal importance and 0 minimum relevance"</sub>
- **descriptive / definition**: Imbalance is described by three assertions: relevance is non-uniform over the target domain, relevant cases are far fewer than normal cases, and standard criteria assume uniform relevance. (p. 3)[^original]  
  <sub>anchor: "The cardinality of the set of examples _DR_ is much smaller than the cardinality of _DN_"</sub>
- **descriptive / finding or result**: Models may be sub-optimal relative to user preferences and the evaluation metrics may be misleading when they ignore those preferences. (p. 3)[^original]  
  <sub>anchor: "the obtained models are sub-optimal with respect to the user-preference biases"</sub>
- **descriptive / finding or result**: Traditional metrics are described as inadequate because they ignore user preferences, with solutions proposed mainly for classification. (p. 3)[^original]  
  <sub>anchor: "traditional metrics are not adequate as they do not take into account the user preferences"</sub>
- **descriptive / context**: The paper categorises solutions to model inadequacy into three strategies: modifying learning algorithms, changing data before learning, and transforming model predictions. (p. 3)[^original]  
  <sub>anchor: "We propose a categorisation of these approaches that considers three types of strategies"</sub>
- **descriptive / finding or result**: Common metrics can lead to sub-optimal classifiers and misleading conclusions because they are insensitive to skewed domains, so choosing proper metrics is key; adequate metrics should also be usable to drive learning. (p. 4)[^original]  
  <sub>anchor: "selecting proper evaluation metrics plays a key role in the task of correctly handling data imbalance"</sub>

## 3 Performance Metrics for Imbalanced Domains

- **descriptive / context**: Most work on imbalance addresses classification, so there are far more solutions for classification than regression; the section covers classification first, then regression. (p. 4)[^original]  
  <sub>anchor: "As the problem of imbalanced domains has been addressed mainly in classification problems"</sub>

## 3.1 Metrics for Classification Tasks

- **descriptive / definition**: The two-class confusion matrix records true positives and true negatives (correct) and false positives and false negatives (wrong) for a classifier. (p. 4)[^original]  
  <sub>anchor: "the number of True Positives (TP) and True Negatives (TN), and the instances that were wrongly classified"</sub>
- **descriptive / finding or result**: Accuracy and its complement error rate are the most frequently used classification metrics but are unsuitable when minority cases matter more, since they reduce the impact of rare examples. (p. 4)[^original]  
  <sub>anchor: "Considering a user preference bias towards the minority (positive) class examples, _accuracy_ is not suitable"</sub>
- **descriptive / case example**: Illustration: if only 1% of examples are minority class, predicting the majority class for all gives 99% accuracy while every minority case is misclassified. (p. 4)[^original]  
  <sub>anchor: "an high _accuracy_ of 99% is achievable by predicting the majority class for all examples"</sub>
- **descriptive / finding or result**: Several measures trade off against each other, making it impractical to monitor them all at once, which motivated new metrics such as F-measure, geometric mean and ROC curves. (p. 4)[^original]  
  <sub>anchor: "it is impractical to simultaneously monitor several measures"</sub>
- **mandatory / requirement**: The source states that metrics used in imbalanced domains must consider user preferences. (p. 4)[^original]  
  <sub>anchor: "The metrics used in imbalanced domains must consider the user preferences and, thus, should take into account the data distribution."</sub>
- **expected / expectation**: The source states that metrics for imbalanced domains should take the data distribution into account. (p. 4)[^original]  
  <sub>anchor: "should take into account the data distribution."</sub>
- **descriptive / definition**: The F-beta measure combines precision and recall; beta sets the relative weight of recall against precision, with beta equal to 1 giving equal weight, larger beta favouring recall and beta below 1 favouring precision. (p. 5)[^original]  
  <sub>anchor: "large values of _β_ will increase the weight of _recall_ whilst values less than 1 will give more importance to _precision_"</sub>
- **descriptive / definition**: G-Mean is the geometric mean of the accuracies of the two classes, aiming to maximise both while achieving balance. (p. 6)[^original]  
  <sub>anchor: "it computes the _geometric mean_ of the accuracies of the two classes"</sub>
- **descriptive / definition**: The ROC curve shows the trade-off between true positive rate (benefits) and false positive rate (costs); each classifier is one point in ROC space and a curve traces thresholds. (p. 6)[^original]  
  <sub>anchor: "The ROC curve allows the visualisation of the relative trade-off between benefits ( _TPrate_ ) and costs ( _FPrate_ )"</sub>
- **descriptive / finding or result**: Comparing ROC curves is difficult unless one dominates; ROC lacks a single score, motivating AUC, which the survey notes is still not biased toward the minority class. (p. 6)[^original]  
  <sub>anchor: "Still, it is not biased towards the minority class."</sub>
- **recommended / expectation**: Precision-recall curves are recommended for highly skewed domains, where ROC curves may give an excessively optimistic view of performance. (p. 6)[^original]  
  <sub>anchor: "_PR curves_ are recommended for highly skewed domains where _ROC_ curves may provide an excessively optimistic view"</sub>
- **descriptive / finding or result**: A strong relation between PR and ROC curves was reported by Davis and Goadrich (2006). (p. 6)[^original]  
  <sub>anchor: "A strong relation between _PR_ and _ROC_ curves was found by Davis and Goadrich (2006)."</sub>
- **descriptive / definition**: The F-beta value is high when both recall (a measure of completeness) and precision (a measure of exactness) are high. (p. 6)[^original]  
  <sub>anchor: "This metric value is high when both _recall_ (a measure of completeness) and _precision_ (a measure of exactness) are high."</sub>
- **descriptive / finding or result**: F-beta is described as more informative about a classifier's effectiveness at correctly predicting the cases that matter to the user, and is commonly used. (p. 6)[^original]  
  <sub>anchor: "is more informative about the effectiveness of a classifier on predicting correctly the cases that matter"</sub>
- **descriptive / definition**: Dominance (Garcia et al., 2008) addresses AUC and G-Mean's inability to explain each class's contribution; it ranges from -1 to +1, with +1 meaning perfect minority accuracy and all majority cases missed, and -1 the opposite. (p. 7)[^original]  
  <sub>anchor: "A value of +1 represents situations where perfect _accuracy_ is achieved on the minority (positive) class"</sub>
- **descriptive / definition**: Index of balanced accuracy (IBA) combines a measure of how balanced the class accuracies are with an unbiased overall accuracy measure, weighted by (1 + alpha times dominance). (p. 7)[^original]  
  <sub>anchor: "which quantifies a trade-off between an index of how balanced both class accuracies are"</sub>
- **descriptive / context**: Other classification metrics include optimized precision, adjusted geometric mean, H-measure and B42, each aimed at a specific shortcoming of other metrics. (p. 8)[^original]  
  <sub>anchor: "Several other metrics exist such as _optimized precision_ (Ranawana and Palade, 2006)"</sub>

## 3.2 Metrics for Regression Tasks

- **descriptive / finding or result**: Few evaluation metrics exist for regression under imbalance; MSE and mean absolute deviation are inadequate because they assume uniform relevance and measure only error magnitude. (p. 8)[^original]  
  <sub>anchor: "These measures assume an uniform relevance of the target variable domain and evaluate only the magnitude of the error."</sub>
- **expected / expectation**: For imbalanced regression the metric must also be sensitive to where errors fall within the target domain, as users focus on poorly represented values. (p. 8)[^original]  
  <sub>anchor: "the metric must also be sensitive to the errors location within the target variable domain"</sub>
- **descriptive / finding or result**: Simple weighting is not a sufficient fix because it would neglect the errors of predicting a rare value when it is a normal one. (p. 8)[^original]  
  <sub>anchor: "it would neglect the errors of predicting a rare value when it is a normal one"</sub>
- **descriptive / finding or result**: Asymmetric loss functions proposed in finance (e.g. LIN-LIN, QUAD-EXP) can only distinguish over- from under-prediction and so remain unsuitable for imbalance with preferences for specific value ranges. (p. 8)[^original]  
  <sub>anchor: "they can only distinguish between over- and underpredictions"</sub>
- **descriptive / definition**: The RROC space for regression plots total overestimation and total underestimation on the axes; RROC curves arise from shifting predictions by a constant to match an asymmetric operating condition. (p. 9)[^original]  
  <sub>anchor: "_RROC_ space is defined by plotting the total overestimation and under-estimation on the _x_ -axis and _y_ -axis"</sub>
- **descriptive / limitation**: The Area Over the RROC curve was shown equivalent to error variance, but RROC still distinguishes only over from under predictions. (p. 9)[^original]  
  <sub>anchor: "In spite of the importance of this approach, it still only distinguishes over from under predictions."</sub>
- **descriptive / definition**: Regression Error Characteristic (REC) curves, proposed by Bi and Bennett (2003), plot the cumulative distribution of error; accuracy is the percentage of points predicted within a tolerance epsilon. (p. 9)[^original]  
  <sub>anchor: "which is defined as the percentage of points predicted within a given tolerance _ϵ_"</sub>
- **descriptive / finding or result**: The area over a REC curve is described as a biased estimate of a model's expected error, and REC curves are not sensitive to error location in the target domain. (p. 9)[^original]  
  <sub>anchor: "The _Area Over the Curve_ ( _AOC_ ) can also be evaluated and is a biased estimate of the expected error of a model"</sub>
- **descriptive / definition**: Regression Error Characteristic Surfaces (RECS), proposed by Torgo (2005), add a dimension giving the cumulative distribution of the target variable, showing how errors at a REC point are distributed across target values. (p. 10)[^original]  
  <sub>anchor: "These surfaces incorporate an additional dimension into _REC_ curves representing the cumulative distribution of the target variable"</sub>
- **descriptive / method**: Zooming on RECS supports two analyses: where given prediction error values occur across the target domain, and what type of errors a model makes in a range of particular interest. (p. 10)[^original]  
  <sub>anchor: "The first involves checking how certain values of prediction error are distributed across the domain of the target variable"</sub>
- **descriptive / definition**: Utility-based regression holds that prediction usefulness depends on both the numeric loss and the relevance of the predicted and true target values, with relevance a continuous function of the target. (p. 11)[^original]  
  <sub>anchor: "the usefulness of a prediction dependes on both the numeric error of the prediction"</sub>
- **descriptive / method**: Ribeiro (2011) describes methods to automatically derive relevance functions, based on the observation that relevance is inversely proportional to the target variable's probability, aiming at accuracy for rare extreme values. (p. 11)[^original]  
  <sub>anchor: "the notion of relevance is inversely proportional to the target variable probability"</sub>
- **descriptive / finding or result**: Precision and recall were adapted to regression with non-uniform relevance by Torgo and Ribeiro (2009) and Ribeiro (2011), defining events via utility. (p. 11)[^original]  
  <sub>anchor: "the notions of precision and recall were adapted to regression problems with non-uniform relevance"</sub>
- **descriptive / finding or result**: Mean Utility and Normalized Mean Utility, derived from utility, let different regression models be compared according to user preference bias. (p. 12)[^original]  
  <sub>anchor: "These metrics are derived from the utility and enable the comparison of different regression models"</sub>

## 4 Modelling Strategies

- **descriptive / context**: Approaches to learning under imbalance are grouped into four categories: data pre-processing, special-purpose learning methods, prediction post-processing and hybrid methods. (p. 12)[^original]  
  <sub>anchor: "the existing approaches to learn under imbalanced data distributions can be grouped into the following four main categories"</sub>
- **descriptive / finding or result**: Data pre-processing changes the data distribution so standard algorithms focus on relevant cases; it can be applied to any learning tool, but relating data changes to the target loss function is difficult. (p. 12)[^original]  
  <sub>anchor: "The main inconvenient of this strategy is that it may be difficult to relate the modifications in the data distribution with the target loss function."</sub>
- **descriptive / finding or result**: Special-purpose learning methods alter algorithms to incorporate user goals directly, but are restricted to modified algorithms, must be relearned if the loss changes, and need deep knowledge of implementations. (p. 12)[^original]  
  <sub>anchor: "if the target loss function changes, the model must be relearned"</sub>

## 4 Modelling Strategies for Handling Imbalanced Domains

- **descriptive / finding or result**: Prediction post-processing models do not reflect the user preferences. (p. 12)[^original]  
  <sub>anchor: "the models do not reflect the user preferences"</sub>
- **descriptive / finding or result**: Data pre-processing is expected to yield models that are more interpretable in terms of the user's goals, because the data distribution was changed to match those goals. (p. 12)[^original]  
  <sub>anchor: "and thus it is expected that the models are more interpretable in terms of these goals."</sub>
- **descriptive / finding or result**: Special-purpose learning methods are expected to yield models that are more comprehensible to the user. (p. 12)[^original]  
  <sub>anchor: "it is expected that the models obtained this way are more comprehensible to the user."</sub>
- **descriptive / finding or result**: A post-processing advantage is that the user does not need to be aware of the user preference biases at learning time. (p. 12)[^original]  
  <sub>anchor: "it is not necessary to be aware of the user preference biases at learning time"</sub>
- **descriptive / limitation**: Post-processing models' interpretability is meaningless because they were obtained by optimising a loss function not in accordance with the user preference bias. (p. 12)[^original]  
  <sub>anchor: "the models interpretability is meaningless as they were obtained optimising a loss function"</sub>

## 4 Modelling Strategies

- **descriptive / context**: Hybrid methods combine approaches of different types to exploit their best characteristics; Figure 7 summarises the categories and their sub-methods such as re-sampling, cost-sensitive learning, active learning and weighting the data space. (p. 13)[^original]  
  <sub>anchor: "Hybrid methods combine approaches of different types trying to take advantage of their best characteristics"</sub>

---

[source overview](overview.md) | [next part](digest-002.md)

[^original]: Paula Branco, Luı́s Torgo, Rita P. Ribeiro, "A Survey of Predictive Modelling under Imbalanced Distributions" (2015-05-07). https://arxiv.org/abs/1505.01658
