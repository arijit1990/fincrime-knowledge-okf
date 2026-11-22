---
type: Source Digest
title: Precision–recall curve (PRC) classification trees - part 1 of 3 (pp. 1-10)
description: 'Verified paraphrased digest, pp. 1-10: ABSTRACT; 1 Introduction; 2 Class imbalance problem; and 14 more sections'
resource: https://arxiv.org/abs/2011.07640
tags:
- academic_finding
- fraud_screening_synergies
- global_academic
- ml_statistics
- preprint
status: stable
source_id: arxiv-precision-recall-curve-prc-classification-trees
issuer: arxiv
issuer_name: arXiv
jurisdictions:
- GLOBAL_ACADEMIC
tier: 3
instrument_type: preprint
normative_force: academic_finding
publication_date: '2021-04-13'
legal_status: unknown
part: 1
parts_total: 3
content_mode: digest
generated:
  by: claude-code-subagent/claude-sonnet-5-5
  at: '2026-11-22T14:46:05Z'
verified:
- by: process:kb-digest-check/anchor-match
  at: '2026-11-22T14:46:05Z'
- by: claude-code-judge-agent/claude-opus-5-5
  at: '2026-11-22T14:46:05Z'
sources:
- id: original
  resource: https://arxiv.org/abs/2011.07640
  title: Precision–recall curve (PRC) classification trees
  author: org:arxiv
  last_modified: '2021-04-13T00:00:00Z'
digest_points: 59
---

# Precision–recall curve (PRC) classification trees (digest)

[source overview](overview.md) | [next part](digest-002.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (pp. 1-10) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **academic finding**.

## Abstract

- **descriptive / definition**: The paper proposes a tree-based algorithm, the PRC classification tree, that uses the area under the precision-recall curve (AUPRC) for variable selection in classification. (p. 1)[^original]  
  <sub>anchor: "we propose a novel tree-based algorithm based on the area under the precision-recall curve (AUPRC) for variable selection in the classification context"</sub>
- **descriptive / method**: The PRC classification tree modifies two stages of tree building: maximising AUPRC for node variable selection, and maximising the F-measure (harmonic mean of recall and precision) for threshold selection. (p. 1)[^original]  
  <sub>anchor: "The first stage is to maximize the area under the precision-recall curve in node variable selection."</sub>
- **descriptive / finding or result**: The authors report that the PRC classification tree and the PRC random forest work well especially for class-imbalanced data sets and outperform the classic CART and random forest on synthetic and real data. (p. 1)[^original]  
  <sub>anchor: "We have demonstrated that our methods outperform their classic counterparts, the usual CART and random forest for both synthetic and real data."</sub>
- **descriptive / finding or result**: The earlier ROC classification tree from the same group has shown good performance on imbalanced data, and the combined PRC-ROC tree is claimed to show promise in identifying the minority class. (p. 1)[^original]  
  <sub>anchor: "The combination of them, the PRC-ROC tree, also shows great promise in identifying the minority class."</sub>

## Introduction

- **descriptive / context**: Skewed class distributions are common in real-world problems, especially in domains such as disease diagnosis, fraud detection, bankruptcy prediction and suspect identification. (p. 1)[^original]  
  <sub>anchor: "It is especially prevalent in certain application domains with great need for machine learning and better predictive analysis"</sub>

## 1 Introduction

- **descriptive / context**: Classification is a form of supervised learning in which a training set of correctly identified observations is available; the constructed classifier predicts class labels for new inputs, such as in financial crisis prediction. (p. 1)[^original]  
  <sub>anchor: "classification is considered an instance of supervised learning, i.e., learning where a training set of correctly identified observations is available"</sub>
- **descriptive / definition**: In a decision tree, inner nodes represent features with thresholds, branches lead to terminal nodes called leaves labelled with class decisions; trees are built by recursive splitting using a locally optimal criterion such as information gain or Gini impurity, then pruned to prevent overfitting. (p. 1)[^original]  
  <sub>anchor: "The inner tree nodes represent features with thresholds leading to the branching of edges eventually ended up in terminal nodes called leaves"</sub>
- **descriptive / finding or result**: With class imbalance, more branches may need to be built to identify the minority class. (p. 1)[^original]  
  <sub>anchor: "In the presence of the class imbalance, more branches may need to be built in order to identify the minority class."</sub>
- **descriptive / context**: CART is described as a well-known tree algorithm. (p. 1)[^original]  
  <sub>anchor: "CART is a well-known tree algorithm[4]."</sub>
- **descriptive / definition**: A random forest is an ensemble of many decision trees whose decisions are combined; it is a bagging algorithm with two built-in randomness sources: bootstrap sampling of the data for each tree and random selection of a feature subset for each split, intended to reduce tree correlation and overfitting. (p. 1)[^original]  
  <sub>anchor: "A random forest (RF) or random decision forest[5] is an ensemble learning method obtained by generating many decision trees"</sub>
- **descriptive / method**: The bootstrap resampling method, introduced by Efron, is implemented by sampling with replacement from an existing sample, independently, with the same size. (p. 1)[^original]  
  <sub>anchor: "It is implemented by sampling with replacement from an existing sample data independently with same size"</sub>
- **descriptive / context**: SVM is described as a discriminative classifier based on a separating hyperplane that, for two-group classification, outputs the hyperplane with maximal margin; Akbani is cited as showing SVMs can be ineffective when the class distribution is skewed. (p. 2)[^original]  
  <sub>anchor: "Akbani[9] illustrates that SVMs can be ineffective in determining the class boundary when the distribution is skewed."</sub>
- **descriptive / finding or result**: Neural networks perform poorly on imbalanced data according to some experiments, because the minority class cannot be adequately weighted. (p. 2)[^original]  
  <sub>anchor: "The principal reason is the minority class cannot be adequately weighted[10]."</sub>
- **descriptive / context**: The paper aims to develop a better decision tree and random forest and compare them with CART, RF, SVM and neural network, plus weighted versions of CART and RF. (p. 2)[^original]  
  <sub>anchor: "compare them to these four original and fundamental algorithms: CART, Random Forest (RF), SVM, and Neural Network"</sub>

## 2 Class imbalance problem

- **descriptive / context**: Solutions to class imbalance are divided into three broad categories: cost-sensitive learning, data-level approaches and algorithm-level approaches. (p. 2)[^original]  
  <sub>anchor: "Basically they can be divided into 3 broad categories, i.e., cost-sensitive learning, data level and algorithm level approaches."</sub>
- **descriptive / definition**: Cost-sensitive learning aims to minimise total misclassification cost by assigning different costs to false positives and false negatives; labelling a minority positive as negative may be costlier. (p. 2)[^original]  
  <sub>anchor: "The goal of this type of learning is to minimize the total cost of misclassification."</sub>
- **descriptive / context**: Weighted random forest, weighted SVM and cost-sensitive decision trees and neural networks are examples of cost-sensitive extensions of learning algorithms. (p. 2)[^original]  
  <sub>anchor: "Weighted Random Forest is the extended version that makes random forest more suitable for learning from extremely imbalanced data"</sub>

## 2.2 Data level approaches

- **descriptive / definition**: Data-level approaches are resampling techniques that undersample the majority class or oversample the minority class to reach a 1:1 class ratio. (p. 2)[^original]  
  <sub>anchor: "we can either undersample the majority class or oversample the minority class to attain the balanced distribution"</sub>
- **descriptive / limitation**: Undersampling discards possibly valuable information and can lead to underfitting. (p. 2)[^original]  
  <sub>anchor: "However an obvious drawback is that we are removing information that may be valuable which can then lead to an underfitting problem."</sub>
- **descriptive / limitation**: Oversampling methods such as SMOTE and ADASYN are widely used, but oversampling can cause overfitting and poor generalisation. (p. 2)[^original]  
  <sub>anchor: "However, it can cause overfitting and poor generalization."</sub>

## 2.3 Algorithm level approaches

- **descriptive / context**: Algorithm-level modification requires in-depth knowledge of both the classifier learning algorithm and the application domain. (p. 2)[^original]  
  <sub>anchor: "To develop an algorithmic solution, one needs in-depth knowledge of both the classifier learning algorithm and the application domain."</sub>
- **descriptive / finding or result**: The PRC classification tree and random forest were developed from a different perspective from the ROC-based trees, as the authors describe in the following chapter. (p. 2)[^original]  
  <sub>anchor: "are developed from a different perspective as will be introduced in details in the following chapter."</sub>
- **descriptive / finding or result**: Song suggested choosing the threshold with the largest harmonic mean of sensitivity and specificity as the node splitting criterion; Yan extended the bi-class ROC tree and ROC RF to multiple classes. (p. 3)[^original]  
  <sub>anchor: "Song suggested choosing the threshold with the largest harmonic mean of sensitivity and specificity as the node splitting criterion"</sub>

## 2.4 Ensemble methods

- **descriptive / context**: Boosting-based approaches for imbalance include cost-weighted AdaBoost, SMOTE combined with boosting, WOTBoost, RUSBoost, MEBoost, DataBoost and EUSBoost. (p. 3)[^original]  
  <sub>anchor: "Nitesh[30] combined the SMOTE algorithm and the boosting procedure and WOTBoost[31] adjusted its oversampling strategy"</sub>

## 2.5 Performance evaluation

- **descriptive / limitation**: Accuracy may be misleading on unbalanced data: assigning the prevalent class to every observation can give high accuracy while performance on the rare class is very poor. (p. 3)[^original]  
  <sub>anchor: "Suppose we give every observation the prevalent class label, the accuracy can be high but the performance for the rare class is very poor."</sub>
- **descriptive / data or feature**: Table 1 is the confusion matrix with true positives, false negatives, false positives and true negatives. (p. 3)[^original]  
  <sub>anchor: "This can be denoted as the confusion matrix shown in Tabel 1."</sub>

## 2.5.2 F-measure

- **descriptive / definition**: Recall (true positive rate) is the share of actual positives correctly classified; precision (positive predictive value) is the share of predicted positives that are correctly classified. (p. 3)[^original]  
  <sub>anchor: "the true positive rate is defined as recall referring to the percentage of positive class samples that are correctly classified."</sub>
- **descriptive / definition**: F-measure is the harmonic mean of precision and recall; it tends to be closer to the smaller of the two and is high only when both are reasonably high. (p. 4)[^original]  
  <sub>anchor: "In general, F-measure tends to be closer to the smaller one of the measures."</sub>

## 3.1 ROC Curve and AUC

- **descriptive / definition**: The ROC curve plots TPR against FPR across thresholds; AUC summarises separability, with higher values indicating stronger class discrimination, and is estimated with the trapezoidal rule. (p. 4)[^original]  
  <sub>anchor: "The higher AUC refers to a stronger ability of distinguishing between classes."</sub>

## 3.2 PRC and AUPRC

- **descriptive / definition**: The precision-recall curve plots precision against recall computed at each threshold; precision is the fraction of positive predictions that are truly positive and recall is the fraction of truly positive examples predicted positive. (p. 4)[^original]  
  <sub>anchor: "Precision-Recall curve plots Precision which is the fraction of observations with a positive predicted value that are truly positive versus Recall"</sub>
- **descriptive / finding or result**: A perfect classifier's PRC passes through the upper right corner (100% precision and 100% recall), and the closer a point is to that corner the better the test. (p. 4)[^original]  
  <sub>anchor: "The perfect classifier will have a PRC that passes through the upper right corner"</sub>
- **expected / expectation**: If the AUC is less than 0.5, representing random guessing, the negative predictions should be converted into positive ones to obtain a better result. (p. 5)[^original]  
  <sub>anchor: "we should convert the negative predictions into positive ones to get a better result"</sub>
- **descriptive / finding or result**: PR curves are not affected by adding true-negative cases (patients without disease), and the number of true negatives is not used in constructing the PRC; PRC curves intersect each other more often than ROC curves. (p. 5)[^original]  
  <sub>anchor: "Ekelund[37] illustrates that the precision-recall curves are not impacted by the addition of patients without disease"</sub>
- **descriptive / finding or result**: ROC may give an optimistic view on imbalanced data because the classifier is more likely to assign observations to the majority class; the Precision-Recall plot is more informative than ROC for evaluating binary classifiers on imbalanced datasets. (p. 5)[^original]  
  <sub>anchor: "The Precision-Recall plot is more informative than the ROC Plot when evaluating binary classifiers on imbalanced datasets[38]"</sub>
- **descriptive / method**: The authors therefore propose classification trees based on maximising the area under the Precision-Recall curve. (p. 5)[^original]  
  <sub>anchor: "Therefore, we propose the classification trees based on maximizing the area under the Precision-Recall curve."</sub>
- **descriptive / definition**: For AUPRC, the corresponding baseline value is the ratio of positive cases in the distribution. (p. 5)[^original]  
  <sub>anchor: "For AUPRC, the corresponding baseline value is the ratio of positive cases in the distribution"</sub>
- **descriptive / method**: For estimating AUPRC, the authors apply the trapezoidal approach, where r is the function of recall and p is of precision and the trajectory is partitioned in n-1 sections. (p. 5)[^original]  
  <sub>anchor: "For the estimation of AUPRC, we also applied the trapezoidal approach"</sub>
- **descriptive / finding or result**: The Precision-recall curve is usually a tortuous curve, fluctuating up and down, so PRC curves tend to intersect each other much more often than ROC curves. (p. 5)[^original]  
  <sub>anchor: "The Precision-recall curve is usually a tortuous curve, fluctuating up and down."</sub>
- **descriptive / finding or result**: The PRC is not impacted by the addition of patients without disease (true negatives), according to Ekelund as cited by the authors. (p. 5)[^original]  
  <sub>anchor: "Ekelund[37] illustrates that the precision-recall curves are not impacted by the addition of patients without disease"</sub>
- **descriptive / finding or result**: For imbalanced data, the ROC may give an optimistic view because the classifier is more likely to assign observations to the majority class. (p. 5)[^original]  
  <sub>anchor: "for imbalanced data, the ROC may tend to give an optimistic view since the classifier is more likely to assign the observation as the majority class."</sub>
- **descriptive / finding or result**: The Precision-Recall plot is described as more informative than the ROC plot for evaluating binary classifiers on imbalanced datasets. (p. 5)[^original]  
  <sub>anchor: "The Precision-Recall plot is more informative than the ROC Plot when evaluating binary classifiers on imbalanced datasets"</sub>

## 3.3 Feature selection

- **descriptive / method**: In the PRC classification tree, features are selected by Algorithm 2, which picks the feature with the largest AUPRC for each node split, computed by Algorithm 1. (p. 6)[^original]  
  <sub>anchor: "Typically, the feature that yields the largest AUPRC value should be selected."</sub>
- **descriptive / method**: Algorithm 2 selects the feature with the largest AUPRC by calling the AUPRC_calculation function (Algorithm 1) for each feature and keeping the maximum. (p. 6)[^original]  
  <sub>anchor: "In Algorithm 2, the function “AUPRC_calculation” is implemented by Algorithm 1."</sub>

## 3.4 Threshold selection

- **descriptive / method**: The split threshold is the one giving the largest F1-score (harmonic mean of precision and recall) among the unique values of the chosen feature; the F-score ignores true negatives, which is said to make it more effective for imbalanced data. (p. 7)[^original]  
  <sub>anchor: "Note that the F-score does not take the true negatives into account."</sub>

## 3.5 PRC Tree algorithm

- **descriptive / method**: Instead of Gini impurity or information gain, PRC tree features and thresholds are selected by AUPRC and F1-score respectively; each node stores a nodescore (class percentages) and a nodelabel (majority class), and splitting continues until a stopping criterion is met. (p. 7)[^original]  
  <sub>anchor: "Instead of measuring by traditional Gini impurity or information gain, the features and threshold are selected by AUPRC and F1-score respectively."</sub>

## 3.4 Threshold selection

- **descriptive / method**: The splitting threshold is chosen as the cutoff with the largest F1-score over the thresholds of the selected feature, the F-score being the harmonic mean of precision and recall. (p. 7)[^original]  
  <sub>anchor: "The basic goal is to choose the cutoff point with the largest F1 after comparing all the scores"</sub>
- **descriptive / finding or result**: The authors state that the F-score does not take true negatives into account, which is why it is more effective than other measures for imbalanced data. (p. 7)[^original]  
  <sub>anchor: "Note that the F-score does not take the true negatives into account."</sub>

## 3.5 PRC Tree algorithm

- **descriptive / method**: Instead of Gini impurity or information gain, the PRC tree selects features by AUPRC and thresholds by F1-score. (p. 7)[^original]  
  <sub>anchor: "Instead of measuring by traditional Gini impurity or information gain, the features and threshold are selected by AUPRC and F1-score respectively."</sub>
- **descriptive / method**: Algorithm 4 (PRC_Tree) takes stopping criteria (maximum depth, minimum leaf size) and the number of features Nf sampled per split, and recursively splits until nodes are pure or stopping criteria are met. (p. 8)[^original]  
  <sub>anchor: "stopping criterion (maximum tree depth, minimum leaf size); Nf , the number of features used in each split."</sub>

## 3.6 PRC random forest

- **descriptive / method**: The PRC random forest uses the PRC tree as base classifier; Nt sets the number of trees, each built on a bootstrap sample with Nf features randomly chosen at each split. (p. 8)[^original]  
  <sub>anchor: "The parameter Nt is used to decide the number of trees to form the “forest”."</sub>
- **descriptive / finding or result**: The PRC random forest is claimed to have competitive predictive performance and to provide a reliable feature importance estimate. (p. 8)[^original]  
  <sub>anchor: "The PRC random forest has competitive predictive performance and provides a reliable feature importance estimate."</sub>

## 3.5 PRC Tree algorithm

- **descriptive / method**: The nodelabel of each node is the majority class of that node, so the terminal node gives the majority target label. (p. 8)[^original]  
  <sub>anchor: "The corresponding nodelabel is the majority class of this node."</sub>

## 3.6 PRC random forest algorithm

- **descriptive / method**: The PRC random forest uses the PRC tree as the base classifier and is reported to have competitive predictive performance and a reliable feature importance estimate. (p. 8)[^original]  
  <sub>anchor: "The PRC random forest has competitive predictive performance and provides a reliable feature importance estimate."</sub>
- **descriptive / method**: In the PRC random forest, the number of features Nf for each node split is randomly chosen from the feature set, which the authors say can decrease prediction error. (p. 8)[^original]  
  <sub>anchor: "As discussed before, the number of features Nf for each node split is randomly chosen from the feature set F."</sub>

## 3.7 PRC-ROC Classification Trees

- **descriptive / method**: The authors state that combining the PRC and ROC classification trees in meaningful and optimal ways is comprehensive. (p. 8)[^original]  
  <sub>anchor: "As an aside, it is comprehensive to combine the PRC and ROC classification trees in meaningful and optimal ways."</sub>
- **descriptive / method**: Out-of-bag samples can be used for objective performance judgements based on training data only, and OOB accuracy is used to tune the optimal weight parameter for the weighted average of both areas. (p. 8)[^original]  
  <sub>anchor: "Based on the training data and OOB accuracy score, we can tune the parameter to find the optimal weighted parameter for a given data."</sub>

## 3.7.1 Feature selection

- **descriptive / method**: In the PRC-ROC tree, Algorithm 7 selects the feature with the largest weighted average of AUPRC and AUC, using Algorithm 6 for AUC calculation; the weighting parameter is tuned on training data using OOB accuracy. (p. 9)[^original]  
  <sub>anchor: "Instead of AUPRC, it lets the weighted average of AUPRC and AUC decide which feature variable is useful to include in every split of tree node."</sub>

## 3.7 PRC-ROC Classification Trees

- **descriptive / method**: The PRC-ROC tree feature selection uses the weighted average of AUPRC and AUC to choose the feature with the largest value. (p. 9)[^original]  
  <sub>anchor: "We will use the weighted average of both areas to do the feature selection."</sub>

## 3.7.1 Feature selection

- **descriptive / method**: Algorithm 7 selects the feature with the largest weighted average of AUPRC and AUC, obtained by calling AUPRC_calculation and AUC_calculation for each feature. (p. 10)[^original]  
  <sub>anchor: "Output: Feature fi with the largest weighted average of AUPRC and AUC."</sub>

---

[source overview](overview.md) | [next part](digest-002.md)

[^original]: Jiaju Miao, Wei Zhu, "Precision–recall curve (PRC) classification trees" (2021-04-13). https://arxiv.org/abs/2011.07640
