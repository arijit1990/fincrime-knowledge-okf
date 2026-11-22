---
type: Source Digest
title: Precision–recall curve (PRC) classification trees - part 2 of 3 (pp. 10-16)
description: 'Verified paraphrased digest, pp. 10-16: 3 Methodology > 3.7.2 Threshold selection; 3 Methodology > 3.7.3 PRC-ROC Tree algorithm; 3 Methodology > Algorithm 9 PRC-ROC_Tree; and 11 more sections'
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
part: 2
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
digest_points: 71
---

# Precision–recall curve (PRC) classification trees (digest)

[previous part](digest-001.md) | [source overview](overview.md) | [next part](digest-003.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (pp. 10-16) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **academic finding**.

## 3.7.2 Threshold selection

- **descriptive / method**: The PRC-ROC Tree picks the threshold for each split as the value giving the largest harmonic mean of recall, precision and specificity for the chosen feature. (p. 10)[^original]  
  <sub>anchor: "we select the largest harmonic mean of three performance metrics, i.e., recall, precision and specificity in the chosen feature variable"</sub>
- **descriptive / definition**: The F-score used for threshold selection is defined as the harmonic mean of precision, recall and specificity. (p. 10)[^original]  
  <sub>anchor: "The F-score in this case becomes the harmonic mean of precision, recall and specificity"</sub>
- **descriptive / method**: Algorithm 8 aims to choose the cutoff point with the largest harmonic mean after comparing the scores for all candidate thresholds of the selected feature. (p. 10)[^original]  
  <sub>anchor: "The main goal is to choose the cutoff point with the largest harmonic mean after comparing all the scores"</sub>
- **descriptive / method**: Algorithm 8 takes the PRC_AUC matrix (recall, precision and false positive arrays) of the selected feature and the threshold set, loops over the sorted unique values of the feature, and returns the value with the maximum F3 score. (p. 10)[^original]  
  <sub>anchor: "Output: Selected splitting threshold θ. Require: function HarmonicMean."</sub>

## 3.7.3 PRC-ROC Tree algorithm

- **descriptive / method**: Each node of the PRC-ROC Tree stores a nodescore, the percentage of each class in the node. (p. 10)[^original]  
  <sub>anchor: "Each node has scores for different classes, measuring the percentage of each class in it."</sub>
- **descriptive / method**: The nodelabel of each node is the majority class of that node, so terminal nodes give the majority target label. (p. 10)[^original]  
  <sub>anchor: "The corresponding nodelabel is the majority class of this node."</sub>
- **descriptive / method**: A PRC-ROC Tree with K terminal nodes and depth L produces predictions in which each of the K partitions is a product of up to L indicator functions of features chosen by the AUPRC_AUC algorithm. (p. 10)[^original]  
  <sub>anchor: "Each partition is a product of up to L indicator function of the features which are selected by AUPRC_AUC algorithm."</sub>
- **descriptive / method**: Algorithm 9 grows the tree recursively: at each node it samples Nf features from the feature set, selects a feature by AUPRC_AUC, picks a threshold by the F3 score, and splits the data. (p. 11)[^original]  
  <sub>anchor: "sample Nf features from the feature set F ′"</sub>
- **descriptive / method**: Algorithm 9 stops splitting when a stopping criterion is met, the stated criteria being maximum tree depth and minimum leaf size. (p. 11)[^original]  
  <sub>anchor: "stopping criterion (maximum tree depth, minimum leaf size)"</sub>
- **descriptive / method**: Splitting is applied recursively to the resulting subsets until the nodes are pure or the stopping criteria is met. (p. 11)[^original]  
  <sub>anchor: "until resulting nodes are pure or the stopping criteria is met"</sub>

## 3.7.4 PRC-ROC random forest algorithm

- **descriptive / method**: The PRC-ROC random forest uses the PRC-ROC tree as its base classifier. (p. 11)[^original]  
  <sub>anchor: "We can build our PRC-ROC random forest by treating the PRC-ROC tree as the base classifier"</sub>
- **descriptive / finding or result**: The authors state that the PRC-ROC random forest has competitive predictive performance and gives a reliable feature importance estimate. (p. 11)[^original]  
  <sub>anchor: "The PRC-ROC random forest has competitive predictive performance and provides a reliable feature importance estimate."</sub>
- **descriptive / method**: Algorithm 10 builds the forest from Nt bootstrap samples, with a parameter Nf giving the number of features randomly chosen for each node split. (p. 11)[^original]  
  <sub>anchor: "Number of trees Nt; Number of features for each node split Nf."</sub>
- **descriptive / finding or result**: The authors state that random selection of Nf features per split can decrease the prediction error of the model. (p. 11)[^original]  
  <sub>anchor: "It can decrease the prediction error of the model by doing so."</sub>

## 3.8 Complexity of algorithm

- **descriptive / finding or result**: For a dataset of size n, each PRC-ROC tree takes O(Nf * n log(n)) time, where Nf is the number of features for each node split. (p. 11)[^original]  
  <sub>anchor: "For each tree, it will take O(Nf ∗ nlog(n)), where Nf is the number of features for each node split."</sub>
- **descriptive / finding or result**: The PRC-ROC random forest complexity is O(Nt * Nf * n log(n)), where Nt is the number of trees. (p. 11)[^original]  
  <sub>anchor: "For the random forest algorithm, the complexity would be O(Nt ∗ Nf ∗ nlog(n)) and Nt is the number of the trees."</sub>
- **descriptive / context**: The experiments are in two parts: a simulation study on imbalanced simulated binary data, and experiments on several real-world data sets. (p. 12)[^original]  
  <sub>anchor: "The experimental studies fall into two parts."</sub>

## 4 Experimental Studies

- **descriptive / method**: Five performance metrics are used to compare algorithms: accuracy, specificity, precision, recall and F1-score. (p. 12)[^original]  
  <sub>anchor: "Five performance metrics as follows are used to make evaluation between different algorithms in our analysis."</sub>
- **descriptive / definition**: Accuracy is the number of correct predictions made by the model divided by all predictions made. (p. 12)[^original]  
  <sub>anchor: "Accuracy is the number of correct predictions made by the model over all kinds of predictions made."</sub>
- **descriptive / definition**: Specificity is the proportion of the majority class that is predicted correctly. (p. 12)[^original]  
  <sub>anchor: "Specificity is a measure that tells us what proportion of the majority class, are predicted correctly."</sub>
- **descriptive / definition**: Precision is the proportion of predicted minority-class cases that are actually positive. (p. 12)[^original]  
  <sub>anchor: "Precision shows us what proportion of the predicted minority class which is actually positive."</sub>
- **descriptive / definition**: Recall (sensitivity) is the proportion of actual minority-class cases that the algorithm identifies as positive. (p. 12)[^original]  
  <sub>anchor: "Recall or sensitivity tells us the proportion of cases that actually belong to the minority class"</sub>
- **descriptive / definition**: F1-score measures both precision and recall and is their harmonic mean. (p. 12)[^original]  
  <sub>anchor: "F1-score, measuring both precision and recall, is the harmonic mean of them."</sub>

## 4.1 Simulation study

- **descriptive / method**: The simulation setting uses 5,000 simulated data sets for each binary classification case. (p. 12)[^original]  
  <sub>anchor: "the number of simulated data sets for classifying binary cases is set to 5,000 each."</sub>
- **descriptive / method**: Feature variables for each class are drawn from a multivariate Gaussian distribution with a specified mean and standard deviation. (p. 12)[^original]  
  <sub>anchor: "The feature variables for each class are generated from multivariate Gaussian distribution with specific mean and standard deviation."</sub>
- **expected / definition**: The text states that a data set whose minority proportion is between 20% and 40% should be placed in the mild category. (p. 12)[^original]  
  <sub>anchor: "the data set whose minority proportion is between 20% and 40% should be placed in the mild category."</sub>
- **descriptive / definition**: The moderate imbalance category is defined as a minority proportion from 1% to 20%. (p. 12)[^original]  
  <sub>anchor: "The criterion for moderate category is from 1% to 20% and the extreme case is when the proportion is less than 1%."</sub>
- **descriptive / definition**: The extreme imbalance category is defined as a minority proportion less than 1%. (p. 12)[^original]  
  <sub>anchor: "the extreme case is when the proportion is less than 1%."</sub>
- **descriptive / definition**: A feature dimension of 5 is treated as low and 20 as higher dimension. (p. 12)[^original]  
  <sub>anchor: "the dimension of features set to be 5 is considered as low feature category and 20 for the higher dimension."</sub>
- **descriptive / context**: Noisy data may make it difficult to learn the rare class, and real data contain random or systematic errors, with random errors referred to as noise. (p. 12)[^original]  
  <sub>anchor: "the noisy data may also make it difficult to learn the rare class."</sub>
- **descriptive / method**: Simulation comparisons include CART, weighted CART and ROC Tree; CART and weighted CART are implemented with R package rpart. (p. 12)[^original]  
  <sub>anchor: "The CART and weighted CART are implemented by functions in R package"</sub>
- **descriptive / method**: Random forest is fit with the randomForest package and weighted random forest with the wsrf package. (p. 12)[^original]  
  <sub>anchor: "Random forest (RF) is fit by the function in package"</sub>

## 4.1.1 Easy to classify, mild imbalanced data set with low feature dimension

- **descriptive / method**: Scenario 1 uses 30% minority data points and five Gaussian features with standard deviation 1, with feature means of 0 for the majority class and 3 for the minority class. (p. 12)[^original]  
  <sub>anchor: "The means of the features for the majority and minority class are set to 0 and 3 respectively."</sub>
- **descriptive / finding or result**: In scenario 1 both PRC algorithms have better F1 score and accuracy than ROC, and the PRC is slightly better than CART. (p. 12)[^original]  
  <sub>anchor: "Both PRC algorithms have better performance in F1 score and accuracy than ROC."</sub>
- **descriptive / finding or result**: In scenario 1 the PRC-ROC tree achieves the best performance in all aspects among the single trees. (p. 12)[^original]  
  <sub>anchor: "In addition, the PRC-ROC tree achieves the best performance in all aspects in the first block."</sub>
- **descriptive / finding or result**: In scenario 1 PRC-ROC RF has the highest recall, accuracy and F1-score among the random forest algorithms. (p. 12)[^original]  
  <sub>anchor: "PRC-ROC RF yields the highest recall, accuracy and F1-score among the random forest algorithms."</sub>
- **descriptive / finding or result**: In scenario 1 the PRC-ROC Tree is reported as the best single tree in all aspects, and PRC-ROC RF has the highest recall, accuracy and F1-score among the random forest methods. (p. 12)[^original]  
  <sub>anchor: "the PRC-ROC tree achieves the best performance in all aspects in the first block"</sub>

## 4.1.2 Easy to classify, moderate imbalanced data set with higher feature dimension

- **descriptive / method**: Scenario 2 raises the imbalance to moderate and the number of features from 5 to 15. (p. 13)[^original]  
  <sub>anchor: "The number of features changes from 5 to 15."</sub>
- **descriptive / finding or result**: In scenario 2 the ROC Tree is perfect in specificity and precision but its recall is not ideal. (p. 13)[^original]  
  <sub>anchor: "The ROC Tree is perfect in specificity and precision, but the performance of recall is not ideal."</sub>
- **descriptive / finding or result**: The authors conclude that the PRC still outperforms both CART trees in scenario 2. (p. 13)[^original]  
  <sub>anchor: "We can conclude that the PRC still outperforms both CART in this scenario."</sub>
- **descriptive / finding or result**: In the five-dimensional evaluation PRC-ROC is better than PRC. (p. 13)[^original]  
  <sub>anchor: "Furthermore, PRC-ROC is better than PRC in the five-dimensional evaluation."</sub>
- **descriptive / finding or result**: In scenario 2 weighted RF performs better than the other algorithms in the second block. (p. 13)[^original]  
  <sub>anchor: "In the second block, the weighted RF work better than other algorithms under this situation."</sub>

## 4.1.3 Easy to classify, extreme imbalanced data set with low feature dimension

- **descriptive / method**: Scenario 3 has only 1% of simulated data points in the minority class, with the same feature setting as scenario 1. (p. 13)[^original]  
  <sub>anchor: "Under this scenario, only 1% of the simulated data points belong to the minority class."</sub>
- **descriptive / finding or result**: In scenario 3 the PRC achieves a higher recall than the weighted version, and both PRC methods clearly outperform CART and ROC, especially in recall. (p. 13)[^original]  
  <sub>anchor: "Both PRC methods apparently outclass than CART and ROC especially in recall."</sub>
- **descriptive / finding or result**: In scenario 3 PRC-ROC obtains larger values than the other methods for specificity, precision and F1-score. (p. 13)[^original]  
  <sub>anchor: "PRC-ROC obtains larger values in specificity, precision and F1-score than other methods"</sub>
- **descriptive / finding or result**: In scenario 3 the weighted RF achieves the best specificity and precision among the methods, while PRC-ROC RF yields the highest recall, accuracy and F1-score among the random forest algorithms. (p. 13)[^original]  
  <sub>anchor: "Although the weighted RF achieves the best specificity and precision"</sub>

## 4.1.4 Hard to classify, mild imbalanced data set with higher feature dimension and noise

- **descriptive / method**: Scenario 4 uses 30% minority data, with majority-class feature mean 0 and minority-class mean -1, all Gaussian with standard deviation 1. (p. 14)[^original]  
  <sub>anchor: "The means of the features for the majority and minority class are set to 0 and -1 respectively."</sub>
- **descriptive / method**: Scenario 4 has ten normal features and five noise features, with the noise features given mean 1. (p. 14)[^original]  
  <sub>anchor: "The setting for this scenario is with ten normal features and five noise features."</sub>
- **descriptive / finding or result**: Scenario 4 data show many overlaps between classes compared with the previous setting. (p. 14)[^original]  
  <sub>anchor: "We can see many overlaps compared to the previous setting."</sub>
- **descriptive / finding or result**: In scenario 4 PRC-ROC surpasses the other tree algorithms on every metric except recall. (p. 14)[^original]  
  <sub>anchor: "PRCROC surpasses other tree-algorithms in every metrics except the recall value."</sub>
- **descriptive / finding or result**: In scenario 4 PRC-ROC RF outperforms the other random forest methods. (p. 14)[^original]  
  <sub>anchor: "For the comparison of the random forest methods, PRC-ROC RF outperforms others."</sub>

## 4.1.5 Hard to classify, extreme imbalanced data set with higher feature dimension and noise

- **descriptive / method**: Scenario 5 is extreme imbalance with the same feature distribution as scenario 4. (p. 14)[^original]  
  <sub>anchor: "In this extreme data set, the features’ distribution is the same as scenario 4."</sub>
- **descriptive / finding or result**: In scenario 5 the PRC-ROC tree has the best performance in the last four dimensions and a large gain in F1 score. (p. 14)[^original]  
  <sub>anchor: "The PRC-ROC tree attains the best performance in the last four dimensions and makes huge improvement in F1 score."</sub>
- **descriptive / finding or result**: In scenario 5 the ROC RF has the highest F1-score in the second block. (p. 14)[^original]  
  <sub>anchor: "The ROC RF achieves the highest F1-score in the second block."</sub>
- **descriptive / finding or result**: Across most cases the two PRC trees perform better than both CART trees on imbalanced data, whether easy or hard to differentiate. (p. 14)[^original]  
  <sub>anchor: "the comparisons under most of those cases illustrate that two PRC trees achieve better performance than the both CART trees"</sub>
- **descriptive / finding or result**: In the extreme data set the PRC tree is more powerful at identifying the minority class and achieves higher precision and recall than CART. (p. 14)[^original]  
  <sub>anchor: "Especially in the case of the extreme data set, the PRC tree is more powerful to identify the minority class"</sub>
- **descriptive / finding or result**: The PRC Tree is better than the ROC Tree when the main goal is identifying rare cases and reaching satisfactory F1 score. (p. 15)[^original]  
  <sub>anchor: "The PRC Tree is better than the ROC Tree when the main goal is to identify the rare cases"</sub>
- **descriptive / context**: The ROC Tree and PRC Tree have different focuses when dealing with imbalanced data. (p. 15)[^original]  
  <sub>anchor: "The ROC and PRC Tree have different focuses when dealing with imbalanced data."</sub>
- **descriptive / finding or result**: PRC-ROC is slightly better than PRC in the five-dimensional evaluation in most cases, as it inherits the advantages of both trees. (p. 15)[^original]  
  <sub>anchor: "PRC-ROC is slightly better than PRC in our 5-dimensional evaluation in most cases"</sub>
- **descriptive / finding or result**: The two PRC random forests show some advantages in classifying minority cases in the second block. (p. 15)[^original]  
  <sub>anchor: "the two PRC RFs also show some advantages in classifying the minority cases."</sub>

## 4.2 Real-world data set experiment

- **descriptive / finding or result**: The PRC and PRC-ROC trees showed an advantage on the severely skewed simulated data sets. (p. 15)[^original]  
  <sub>anchor: "The PRC and PRC-ROC Tree have shown their advantage in classifying the simulated data set which is severely skewed."</sub>
- **descriptive / method**: Real-world experiments use datasets from Kaggle and the UCI Machine Learning Repository to test the feasibility of PRC random forests against random forest, SVM, neural network, weighted CART and ROC random forest. (p. 15)[^original]  
  <sub>anchor: "We will compare the performance with standard classification algorithms such as random forest, SVM and neural network."</sub>
- **descriptive / method**: The neural network is realised with the neuralnet package, and SVM is fitted with the e1071 package. (p. 15)[^original]  
  <sub>anchor: "the package “neuralnet”[42] is for realizing neural network."</sub>
- **descriptive / data or feature**: Table 7 lists three real-world datasets: Default of Credit Card Clients (UCI, 30000 observations, 3.7% minority, 23 features); Financial Distress Prediction (Kaggle, 3672 observations, 22% minority, 83 features); Breast Cancer Wisconsin (UCI, 569 observations, 37% minority, 30 features). (p. 15)[^original]  
  <sub>anchor: "The Table 7 summarizes the basic information of the three selected data sets."</sub>
- **descriptive / definition**: For the credit data the dependent variable is default payment, coded Yes = 1 and No = 0, with 23 independent features. (p. 15)[^original]  
  <sub>anchor: "this study employed a binary variable, default payment (Yes = 1, No = 0), as the dependent variable."</sub>
- **descriptive / definition**: For the financial distress data a company is considered healthy (0) if its 'Financial Distress' value is greater than -0.50, otherwise financially distressed (1); there are 83 explanatory variables. (p. 15)[^original]  
  <sub>anchor: "if it is greater than -0.50 the company should be considered as healthy (0)."</sub>
- **descriptive / definition**: For the breast cancer data the binary outcome is whether a tumour is benign (0) or malignant (1), from 30 attributes. (p. 15)[^original]  
  <sub>anchor: "whether a tumor is benign (0) or malignant (1)"</sub>
- **descriptive / method**: The out-of-bag error is an error estimation technique often used to evaluate the accuracy of a random forest. (p. 15)[^original]  
  <sub>anchor: "The out-of-bag error is an error estimation technique often used to evaluate the accuracy of a random forest."</sub>
- **descriptive / method**: Data are split into training and testing sets, the OOB error estimates the error rate on the training sample, and a separate test set validates the random forest models. (p. 15)[^original]  
  <sub>anchor: "use the OOB to estimate the error rate of the training sample"</sub>
- **descriptive / finding or result**: The text states that the minimum out-of-bag values are coloured red in the table, though the colour is not reproducible in the extracted text. (p. 15)[^original]  
  <sub>anchor: "The following table shows the out-of-bag error of all the corresponding random forests and the minimum values are colored in red."</sub>
- **descriptive / finding or result**: Table 8 reports out-of-bag error rates: Credit card data RF 0.1900, Weighted RF 0.2300, ROC RF 0.2446, PRC RF 0.1921; Financial distress RF 0.0414, Weighted RF 0.0500, ROC RF 0.0345, PRC RF 0.0000; Breast cancer RF 0.1000, Weighted RF 0.0912, ROC RF 0.0714, PRC RF 0.0455. (p. 16)[^original]  
  <sub>anchor: "Table 8: Summary of Out-of-bag error rate"</sub>

---

[previous part](digest-001.md) | [source overview](overview.md) | [next part](digest-003.md)

[^original]: Jiaju Miao, Wei Zhu, "Precision–recall curve (PRC) classification trees" (2021-04-13). https://arxiv.org/abs/2011.07640
