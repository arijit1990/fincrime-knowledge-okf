---
type: Source Digest
title: Machine learning methods to detect money laundering in the Bitcoin blockchain in the presence of label scarcity - part 1 of 3 (pp. 1-4)
description: 'Verified paraphrased digest, pp. 1-4: ABSTRACT; CCS CONCEPTS; KEYWORDS; and 2 more sections'
resource: https://arxiv.org/abs/2005.14635
tags:
- academic_finding
- advanced_analytics
- global_academic
- ml_statistics
- model_development
- preprint
status: stable
source_id: arxiv-machine-learning-methods-to-detect-money-laundering-in-the-bitco
issuer: arxiv
issuer_name: arXiv
jurisdictions:
- GLOBAL_ACADEMIC
tier: 3
instrument_type: preprint
normative_force: academic_finding
publication_date: '2020-05-29'
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
  resource: https://arxiv.org/abs/2005.14635
  title: Machine learning methods to detect money laundering in the Bitcoin blockchain in the presence of label scarcity
  author: org:arxiv
  last_modified: '2020-05-29T00:00:00Z'
digest_points: 100
---

# Machine learning methods to detect money laundering in the Bitcoin blockchain in the presence of label scarcity (digest)

[source overview](overview.md) | [next part](digest-002.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (pp. 1-4) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **academic finding**.

## ABSTRACT

- **descriptive / context**: Governments and international organizations are broadening money laundering regulations to include cryptocurrencies, where criminals benefit from pseudonymity. (p. 1)[^original]  
  <sub>anchor: "Governments and international organizations are building tighter regulations around money laundering and are broadening them to include cryptocurrencies"</sub>
- **descriptive / finding or result**: Rule-based AML systems suffer from vulnerabilities because publicly available rule-sets are relatively simple, leading to high false-positive rates and low detection rates. (p. 1)[^original]  
  <sub>anchor: "vulnerabilities derive from the relative simplicity of publicly available rule-sets, leading to high false-positive rates (FPR) and low detection rates"</sub>
- **descriptive / context**: Machine learning can overcome the rigidity of rule-based systems by inferring complex patterns from historical data and can potentially increase detection rates and decrease FPRs. (p. 1)[^original]  
  <sub>anchor: "Machine learning (ML) techniques overcome the rigidity of rule-based systems by inferring complex patterns from historical data"</sub>
- **descriptive / context**: Labels for money laundering are so scarce that traditional supervised algorithms are inapplicable, so the study addresses detection assuming minimal access to labels. (p. 1)[^original]  
  <sub>anchor: "labels are so scarce that traditional supervised algorithms are inapplicable"</sub>
- **descriptive / finding or result**: The authors show that existing state-of-the-art unsupervised anomaly detection solutions are inadequate for detecting illicit patterns in a real Bitcoin transaction dataset. (p. 1)[^original]  
  <sub>anchor: "existing state-of-the-art solutions using unsupervised anomaly detection methods are inadequate to detect the illicit patterns in a real Bit- coin transaction dataset"</sub>
- **descriptive / finding or result**: The proposed active learning solution matches the performance of a fully supervised baseline using just 5% of the labels. (p. 1)[^original]  
  <sub>anchor: "our proposed active learning solution is capable of matching the performance of a fully supervised baseline by using just 5% of the labels"</sub>

## 1 INTRODUCTION

- **descriptive / context**: Supervised methods are often unfeasible because institutions lack large-scale labeled datasets, partly since it is unlikely all or most entities in laundering schemes can be identified and labels from investigations are delayed and manual annotation is costly. (p. 1)[^original]  
  <sub>anchor: "Unfortunately, supervised methods are often unfeasible as institutions do not possess large-scale labeled datasets"</sub>
- **descriptive / context**: Money laundering schemes typically involve large sums, and when detected they usually lead to large fines for financial institutions. (p. 1)[^original]  
  <sub>anchor: "Money laundering schemes usually involve large amounts of money and, when caught, typically result in large fines for financial institutions"</sub>
- **descriptive / finding or result**: The paper argues that existing state-of-the-art unsupervised anomaly detection solutions are inadequate for detecting illicit patterns in a real Bitcoin dataset. (p. 1)[^original]  
  <sub>anchor: "existing state-of-the-art solutions using unsupervised anomaly detection methods are inadequate"</sub>

## ABSTRACT

- **descriptive / context**: Rule-based anti-money laundering systems are said to suffer from high false-positive rates and low detection rates. (p. 1)[^original]  
  <sub>anchor: "leading to high false-positive rates (FPR) and low detection rates [41]"</sub>
- **descriptive / context**: Machine learning can potentially increase detection rates and decrease false-positive rates compared with rule-based systems. (p. 1)[^original]  
  <sub>anchor: "can potentially increase detection rates and decrease FPRs"</sub>
- **descriptive / context**: Labels are so scarce that traditional supervised algorithms are inapplicable to money laundering detection in Bitcoin, the paper states. (p. 1)[^original]  
  <sub>anchor: "labels are so scarce that traditional supervised algorithms are inapplicable"</sub>

## 1 INTRODUCTION

- **descriptive / context**: Weber et al. released a dataset of a sample of 200k labeled Bitcoin transactions and evaluated various supervised models on it. (p. 1)[^original]  
  <sub>anchor: "consisting of a sample of 200k labeled Bitcoin transactions"</sub>
- **descriptive / context**: Supervised methods are often unfeasible because institutions do not possess large-scale labeled datasets. (p. 1)[^original]  
  <sub>anchor: "supervised methods are often unfeasible as institutions do not possess large-scale labeled datasets"</sub>
- **descriptive / finding or result**: The paper claims that detecting money laundering in the Bitcoin network without any labels is impossible because illicit transactions hide within clusters of licit behaviour. (p. 2)[^original]  
  <sub>anchor: "without any labels is impossible since illicit transactions hide within clusters of licit behaviour"</sub>
- **descriptive / context**: The authors claim to be the first to apply active learning to AML on a large transaction dataset and in the cryptocurrency setting. (p. 2)[^original]  
  <sub>anchor: "we are the first work to apply AL to AML on a large transaction dataset and in the cryptocurrency setting, specifically"</sub>
- **descriptive / context**: The study benchmarks unsupervised methods on a real-world dataset with a relatively large number of positive cases, avoiding the typical limitation of synthetic data or real data with few positives. (p. 2)[^original]  
  <sub>anchor: "by bench- marking different methods on a real-world dataset with a relatively large number of positive cases"</sub>
- **descriptive / context**: The paper cites prior active learning work in credit card fraud and network intrusion detection, reporting that as few as 1.5% of the original labels sufficed for near-optimal performance in one study. (p. 2)[^original]  
  <sub>anchor: "reporting the sufficiency of as few as 1.5% of the original labels to achieve near-optimal performance [15]"</sub>
- **descriptive / method**: The study extends Deng et al. to transaction-level analysis in a much larger cryptocurrency dataset, assuming an unlabeled dataset and progressive label acquisition to train a supervised classifier. (p. 2)[^original]  
  <sub>anchor: "We hereby extend the study by Deng et al. [12] to a transaction-level analysis in a much larger cryptocurrency dataset"</sub>

## 2 RELATED WORK

- **descriptive / finding or result**: Many studies assume money laundering cases are outliers, with illicit instances a minority behaving differently from the licit majority, and use unsupervised anomaly detection to model licit behaviour. (p. 2)[^original]  
  <sub>anchor: "many methods assume money laundering cases to be outliers, i.e., illicit instances (a minority) should exhibit significantly different behaviours from legitimate ones"</sub>
- **descriptive / finding or result**: Reported anomaly detection studies show low false-positive rates and good detection rates, but a fair comparison between them is impossible due to heterogeneous evaluation setups. (p. 2)[^original]  
  <sub>anchor: "However, a fair compar- ison between methods is impossible, given the heterogeneity of the evaluation setups"</sub>
- **descriptive / context**: Prior cryptocurrency money laundering studies are scarce and inconclusive; some report supervised models perform well while others report low detection rates for unsupervised methods in extremely imbalanced data. (p. 2)[^original]  
  <sub>anchor: "Previous studies on money laundering in cryptocurrencies in par- ticular are scarce and inconclusive due to a lack of labels for evalua- tion"</sub>

## 3.1 Data

- **descriptive / data or feature**: The Elliptic Bitcoin dataset comprises 49 graphs sampled from the Bitcoin blockchain at sequential time-steps, each a directed acyclic graph starting from one transaction and including subsequent related transactions, covering about two weeks of data. (p. 2)[^original]  
  <sub>anchor: "It in- cludes 49 graphs sampled from the Bitcoin blockchain at different sequential moments in time (time-steps)"</sub>
- **descriptive / data or feature**: The dataset has 203,769 transactions, of which 21% are labeled licit and 2% illicit, based on the category of the bitcoin address that created the transaction; the rest are unlabeled. (p. 2)[^original]  
  <sub>anchor: "The dataset consists of 203,769 transactions, of which 21% are labeled as licit, and 2% as illicit"</sub>
- **descriptive / data or feature**: Illicit categories include scams, malware, terrorist organizations and Ponzi schemes; licit categories include exchanges, wallet providers, miners and licit services. (p. 2)[^original]  
  <sub>anchor: "Illicit categories include scams, malware, terrorist or- ganizations, and Ponzi schemes"</sub>

## 3.2 Methods

- **descriptive / context**: Active learning selects the most informative samples for labeling iteratively from an initially unlabeled pool to reduce labels needed for an effective classifier. (p. 2)[^original]  
  <sub>anchor: "Active Learning has been proposed as a method to reduce the number of labels needed for the training of an effective classifier"</sub>
- **descriptive / finding or result**: Deng et al. applied AL to account-level classification of 92 real-life accounts and reported accurately estimating the threshold hyperplane with only 22% of labels. (p. 2)[^original]  
  <sub>anchor: "In an account-level classification of 92 real-life accounts, they report that their method can accurately estimate the threshold hyperplane with only 22% of the labels"</sub>

## 1 INTRODUCTION

- **descriptive / finding or result**: Using Active Learning with a small share of labels (about 5% of the total), the authors state one can match the results of a supervised baseline. (p. 2)[^original]  
  <sub>anchor: "match the results of a supervised baseline by using Active Learning (AL)"</sub>

## 2 RELATED WORK

- **descriptive / context**: The open question is whether reliable anomaly detection is possible on non-synthetic data, since criminals could intentionally mimic normal behaviour. (p. 2)[^original]  
  <sub>anchor: "as criminals could intentionally mimic normal behaviour"</sub>
- **descriptive / context**: Previous cryptocurrency money laundering studies are described as scarce and inconclusive because of a lack of labels for evaluation. (p. 2)[^original]  
  <sub>anchor: "Previous studies on money laundering in cryptocurrencies in particular are scarce and inconclusive due to a lack of labels"</sub>

## 3.1 Data

- **descriptive / data or feature**: The edges in the graph represent the flow of Bitcoins between transactions. (p. 2)[^original]  
  <sub>anchor: "The edges in the graph represent the flow of Bitcoins between transactions"</sub>
- **descriptive / data or feature**: The Elliptic Bitcoin dataset includes 49 graphs sampled from the Bitcoin blockchain at different sequential time-steps. (p. 2)[^original]  
  <sub>anchor: "It includes 49 graphs sampled from the Bitcoin blockchain at different sequential moments in time"</sub>
- **descriptive / data or feature**: Each graph is a directed acyclic graph starting from one transaction and covering roughly two weeks of related blockchain data. (p. 2)[^original]  
  <sub>anchor: "Each graph is a directed acyclic graph, starting from one transaction, and including subsequent related transactions"</sub>
- **descriptive / data or feature**: The dataset has 203,769 transactions; 21% are labeled licit and 2% illicit, based on the category of the address that created each transaction, and the rest are unlabeled. (p. 2)[^original]  
  <sub>anchor: "The dataset consists of 203,769 transactions, of which 21% are labeled as licit, and 2% as illicit"</sub>
- **descriptive / data or feature**: Illicit categories in the data include scams, malware, terrorist organizations and Ponzi schemes. (p. 2)[^original]  
  <sub>anchor: "Illicit categories include scams, malware, terrorist or- ganizations, and Ponzi schemes"</sub>
- **descriptive / data or feature**: Licit categories in the data include exchanges, wallet providers, miners and licit services. (p. 2)[^original]  
  <sub>anchor: "Licit categories include exchanges, wallet providers, miners, and licit services"</sub>
- **descriptive / data or feature**: Each transaction has 166 features, of which 94 describe the transaction itself. (p. 2)[^original]  
  <sub>anchor: "Each transaction has 166 features, 94 of which represent information about the transaction itself"</sub>
- **descriptive / data or feature**: The other features were constructed by Weber et al. from information one hop backward or forward from the transaction. (p. 2)[^original]  
  <sub>anchor: "The remaining features were constructed by Weber et al. [42] using information one-hop backward/forward from the transaction"</sub>
- **descriptive / data or feature**: All features except the time-step are anonymized and standardized to zero mean and unit variance. (p. 2)[^original]  
  <sub>anchor: "All features, except for the time-step, are fully anonymized and standardized with zero mean and unit variance"</sub>

## 3.2 Methods

- **descriptive / data or feature**: Following Weber et al., the data is split sequentially: the train set holds all labeled samples up to the 34th time-step. (p. 2)[^original]  
  <sub>anchor: "The train set includes all labeled samples up to the 34th time-step (29894 transactions)"</sub>
- **descriptive / context**: Active learning iteratively samples the most informative instances for labeling from an initially unlabeled pool to reduce the labels needed. (p. 2)[^original]  
  <sub>anchor: "by iteratively sampling the most informative samples for labeling from an initially unlabeled pool"</sub>
- **descriptive / finding or result**: Deng et al. report that in an account-level classification of 92 real-life accounts, their method estimated the threshold hyperplane with only 22% of the labels. (p. 2)[^original]  
  <sub>anchor: "In an account-level classification of 92 real-life accounts, they report"</sub>

## 3.1 Data

- **descriptive / data or feature**: Each transaction has 166 features, 94 describing the transaction itself, while the other features are one-hop backward/forward aggregates such as minimum, maximum and standard deviation; all features except time-step are anonymized and standardized. (p. 3)[^original]  
  <sub>anchor: "Each transaction has 166 features, 94 of which represent information about the transaction itself"</sub>

## 3.2 Methods

- **descriptive / method**: Following Weber et al., data is split sequentially: the train set includes labeled samples up to the 34th time-step (29894 transactions) and the test set covers the 35th time-step onward (16670 transactions). (p. 3)[^original]  
  <sub>anchor: "The train set includes all labeled samples up to the 34th time-step (29894 transactions)"</sub>
- **descriptive / method**: All methods are evaluated with the F1-score for the illicit class, referred to as illicit F1-score. (p. 3)[^original]  
  <sub>anchor: "we evaluate all methods using the F1-score for the illicit class, hereafter referred to as illicit F1- score"</sub>

## 3.2.1 Supervised Learning

- **descriptive / method**: The supervised baseline reproduces Weber et al.; unsupervised methods are compared at different contamination levels, the expected proportion of outliers used to set a threshold. (p. 3)[^original]  
  <sub>anchor: "Thus, a fair comparison requires evaluation at different contam- ination levels, defined as the expected proportion of outliers in the dataset"</sub>
- **descriptive / method**: Unlike the original PyOD implementation, the contamination level is applied to test set scores so the desired percentage of anomalies is the same across methods; this is analogous to a fixed alert rate. (p. 3)[^original]  
  <sub>anchor: "we apply it on the test set scores to guarantee that the desired percentage of positive cases (anomalies) in the test set is the same across methods"</sub>
- **descriptive / method**: Illicit F1-scores are evaluated at contamination levels from 0 to 1 in increments of 0.05; the RF baseline threshold is set by its predicted positive rate. (p. 3)[^original]  
  <sub>anchor: "We evaluate the illicit F1-score for each model at contamination levels between 0 and 1, with increments of 0.05"</sub>
- **descriptive / method**: Supervised models (logistic regression, random forest and XGBoost) are trained on all 166 features with default parameters, following Weber et al., and evaluated per time-step. (p. 3)[^original]  
  <sub>anchor: "We train each supervised model on the train set using all 166 features and then evaluate them on the entire test set"</sub>

## 3.2.2 Unsupervised Learning

- **descriptive / definition**: Anomaly detection methods are unsupervised techniques to detect outliers in a dataset. (p. 3)[^original]  
  <sub>anchor: "Anomaly detection methods are un- supervised learning techniques to detect outliers in a dataset"</sub>

## 3.2.3 Active Learning

- **descriptive / definition**: Active learning is an incremental approach that queries instances for labeling, e.g., by human analysts, and uses the growing labeled set to retrain a supervised model. (p. 3)[^original]  
  <sub>anchor: "AL is an incremental learning approach that interactively queries instances for labeling (e.g., by human analysts)"</sub>
- **descriptive / definition**: Outliers are instances unlikely to come from the same distribution as the training data or far from other points in feature space; for semi-supervised discriminators, outliers fall outside a learned boundary around normal instances. (p. 3)[^original]  
  <sub>anchor: "The standard definition of outliers refers to instances that are unlikely to be drawn from the same distribution as the train data"</sub>
- **descriptive / method**: The active learning process starts with an unlabeled pool, a query strategy queries a batch for manual labeling, labeled instances join the labeled pool, and a classifier is trained and evaluated, repeating until performance is satisfactory. (p. 3)[^original]  
  <sub>anchor: "The process starts with a pool of unlabeled instances (the unlabeled pool)"</sub>
- **descriptive / method**: Seven anomaly detection algorithms are tested with PyOD default parameters: LOF, KNN, PCA, OCSVM, CBLOF, ABOD and Isolation Forest. (p. 3)[^original]  
  <sub>anchor: "We test seven common anomaly detection algorithms with read- ily available Python implementations"</sub>
- **descriptive / method**: LOF and KNN compute the distance to each instance's k nearest neighbours; KNN uses that distance as the outlier score, while LOF flags instances whose density is substantially lower than that of their neighbours. (p. 3)[^original]  
  <sub>anchor: "LOF uses the distance to compute the instance’s density, and if the density is substantially lower than the average density"</sub>
- **descriptive / method**: Four query strategies are studied: uncertainty sampling and expected model change (supervised), and elliptic envelope and Isolation Forest (unsupervised), with random sampling as baseline. (p. 3)[^original]  
  <sub>anchor: "we focus on four query strategies trained on the labeled pool to find informative instances in the unlabeled pool"</sub>
- **descriptive / method**: PCA and OCSVM flag observations with large distance to principal components of normal observations, or instances outside the learned decision boundary, respectively. (p. 3)[^original]  
  <sub>anchor: "PCA and OCSVM define anomalies as observations that deviate from normal behaviour"</sub>
- **descriptive / method**: Expected model change queries the instances that most change model parameters, measured by impact on the gradient of the loss, applies only to gradient-based classifiers (LR here), and is a weighted sum over possible labels. (p. 3)[^original]  
  <sub>anchor: "It queries the unlabeled instances that lead to the most significant change in the model parameters"</sub>
- **descriptive / method**: Uncertainty sampling queries instances whose predicted score is closest to 0.5 for a probabilistic binary classifier, using the same classifier type for querying and evaluation. (p. 3)[^original]  
  <sub>anchor: "this translates to querying the in- stances with the predicted score closest to 0.5"</sub>
- **descriptive / method**: The two unsupervised query strategies treat outliers as transactions with high Isolation Forest anomaly scores or large Mahalanobis distance to a Gaussian fitted on the labeled pool. (p. 3)[^original]  
  <sub>anchor: "Outliers are transactions with high anomaly scores (IF) or a large Mahalanobis distance to a multivariate Gaussian distribution"</sub>

## 4.2 Anomaly detection

- **descriptive / method**: Table 1 reports illicit F1-scores of the anomaly detection methods and the RF supervised baseline at different contamination levels, with the RF threshold set so its alert rate equals each contamination level. (p. 3)[^original]  
  <sub>anchor: "In Table 1, we present the illicit F1-score of the explored anomaly detection methods as well as the RF supervised baseline"</sub>

## 3.2 Methods

- **descriptive / data or feature**: The test set holds labeled samples from the 35th time-step onward, inclusive, totalling 16670 transactions. (p. 3)[^original]  
  <sub>anchor: "labeled samples from the 35th time-step, inclusive, onward (16670 transactions)"</sub>
- **descriptive / method**: All methods are evaluated with the F1-score for the illicit class, referred to as the illicit F1-score. (p. 3)[^original]  
  <sub>anchor: "we evaluate all methods using the F1-score for the illicit class"</sub>

## 3.2.1 Supervised Learning

- **descriptive / method**: The supervised baseline reproduces Weber et al.'s results using logistic regression, random forest and XGBoost with default parameters. (p. 3)[^original]  
  <sub>anchor: "We use the scikit-learn [30] implementation of logistic regression (LR) and random forest (RF)"</sub>
- **descriptive / method**: Each supervised model is trained on the train set using all 166 features and evaluated on the entire test set. (p. 3)[^original]  
  <sub>anchor: "We train each supervised model on the train set using all 166 features"</sub>
- **descriptive / method**: Contamination levels are applied to the test set scores rather than the train set scores so that the share of positive cases is the same across methods. (p. 3)[^original]  
  <sub>anchor: "we apply it on the test set scores to guarantee that the desired percentage of positive cases"</sub>
- **descriptive / method**: The illicit F1-score is evaluated for each model at contamination levels between 0 and 1, in increments of 0.05. (p. 3)[^original]  
  <sub>anchor: "We evaluate the illicit F1-score for each model at contamination levels between 0 and 1, with increments of 0.05"</sub>
- **descriptive / context**: The contamination level is analogous to a fixed alert rate in real AML systems, i.e. the share of cases flagged for analyst investigation. (p. 3)[^original]  
  <sub>anchor: "The contamination level here is analogous to a fixed alert rate in real AML systems"</sub>

## 3.2.2 Unsupervised Learning

- **descriptive / method**: The illicit F1-score is also reported per time-step in the test set, following Weber et al. (p. 3)[^original]  
  <sub>anchor: "we also report the illicit F1-score per time-step in the test set"</sub>
- **descriptive / method**: Seven anomaly detection algorithms are tested: LOF, KNN, PCA, OCSVM, CBLOF, ABOD and Isolation Forest, using PyOD implementations with default parameters. (p. 3)[^original]  
  <sub>anchor: "We use the PyOD package implementations [44] with default parameters"</sub>
- **descriptive / method**: KNN computes the distance of each instance to its k nearest neighbour and uses that distance as the outlier score. (p. 3)[^original]  
  <sub>anchor: "KNN defines that distance as the out- lier score"</sub>
- **descriptive / method**: LOF uses the distance to compute an instance's density and flags the instance as anomalous if its density is substantially lower than its neighbours' average. (p. 3)[^original]  
  <sub>anchor: "LOF uses the distance to compute the instance"</sub>
- **descriptive / method**: PCA and OCSVM define anomalies as observations that deviate from normal behaviour. (p. 3)[^original]  
  <sub>anchor: "PCA and OCSVM define anomalies as observations that deviate from normal behaviour"</sub>

## 3.2.3 Active Learning

- **descriptive / method**: CBLOF classifies each cluster as either small or large, after clustering the instances with k-means. (p. 3)[^original]  
  <sub>anchor: "classifies each cluster as either small or large"</sub>
- **descriptive / method**: CBLOF marks instances that belong to small clusters, or that are far from big clusters, as anomalous. (p. 3)[^original]  
  <sub>anchor: "marking instances that belong to small clusters or that are far from big clusters as anomalous"</sub>
- **descriptive / method**: ABOD computes the pairwise cosine similarities between all points and classifies low average radius and variance points as anomalies. (p. 3)[^original]  
  <sub>anchor: "computes the pairwise cosine similarities between all points and classifies those"</sub>
- **descriptive / method**: Isolation Forest isolates anomalies by performing recursive random splits on attribute values. (p. 3)[^original]  
  <sub>anchor: "IF isolates anomalies by performing recursive random splits on attribute values"</sub>
- **descriptive / method**: In Isolation Forest, anomalies are instances that are easy to isolate, meaning they have shorter paths in the tree. (p. 3)[^original]  
  <sub>anchor: "anomalies are instances that are easy to isolate, i.e., have shorter paths"</sub>
- **descriptive / method**: Four query strategies are studied: uncertainty sampling and expected model change are supervised, while elliptic envelope and Isolation Forest are unsupervised. (p. 3)[^original]  
  <sub>anchor: "Two of them, uncertainty sampling and expected model change, are supervised, requiring an underlying supervised model to define queries"</sub>
- **descriptive / method**: Random sampling is used as the baseline query strategy. (p. 3)[^original]  
  <sub>anchor: "We use random sampling as a baseline"</sub>
- **descriptive / method**: The active learning setup is based on earlier work with Feedzai's active learning annotation tool, which was used to run the experiments. (p. 3)[^original]  
  <sub>anchor: "This setup was based on previous work done on Feedzai’s active learning annotation tool"</sub>
- **descriptive / method**: Expected model change assumes instances are more informative if they influence the model more strongly, and applies only to gradient-based classifiers. (p. 3)[^original]  
  <sub>anchor: "Thus, this strategy applies only to gradient-based classifiers"</sub>
- **descriptive / method**: At each iteration, expected model change queries the labels of the instances with the largest expected gradients. (p. 3)[^original]  
  <sub>anchor: "Then, at each iteration, we query the labels of the instances with the largest expected gradients"</sub>
- **descriptive / method**: Uncertainty sampling is one of the most commonly used query strategies and queries the instances the model is most uncertain about. (p. 3)[^original]  
  <sub>anchor: "Uncertainty sampling is one of the most commonly used query strategies"</sub>
- **descriptive / method**: For a binary probabilistic classifier, uncertainty sampling queries instances whose predicted score is closest to 0.5. (p. 3)[^original]  
  <sub>anchor: "the predicted score closest to 0.5"</sub>
- **descriptive / method**: The two unsupervised query strategies are Isolation Forest and elliptic envelope; outliers are transactions with high anomaly scores or a large Mahalanobis distance. (p. 3)[^original]  
  <sub>anchor: "Outliers are transactions with high anomaly scores (IF) or a large Mahalanobis distance to a multivariate Gaussian distribution"</sub>

## 4.3 Active learning

- **descriptive / method**: Active learning uses an unsupervised warm-up learner until the labeled pool contains at least one illicit instance, then switches to a supervised hot learner or keeps the warm-up learner; classifiers are RF, XGBoost and LR. (p. 4)[^original]  
  <sub>anchor: "we use an unsupervised warm-up learner that samples instances until the labeled pool includes at least one illicit instance"</sub>
- **descriptive / method**: AL setups are compared against a random-query baseline (also used as warm-up learner), with a batch size of 50 instances per iteration, each run five times with different random seeds. (p. 4)[^original]  
  <sub>anchor: "We use a batch size of 50 instances sampled at each iteration for all experiments"</sub>
- **descriptive / method**: Performance of each AL setup is assessed through the median illicit F1-score and confidence intervals at each labeled pool size. (p. 4)[^original]  
  <sub>anchor: "We assess the performance of each AL setup through the median illicit F1-score and the confidence intervals at each labeled pool size"</sub>
- **descriptive / method**: The AL setup and parameter choices follow work by Barata et al. developed concurrently at Feedzai. (p. 4)[^original]  
  <sub>anchor: "This setup and parameter choices follow the work by Barata et al. [2] developed at Feedzai concurrently"</sub>

## 4.2 Anomaly detection

- **descriptive / finding or result**: Table 1 reports the illicit F1-score of the explored anomaly detection methods alongside the RF supervised baseline at different contamination levels. (p. 4)[^original]  
  <sub>anchor: "In Table 1, we present the illicit F1-score of the explored anomaly detection methods"</sub>
- **descriptive / method**: At each contamination level, the RF model threshold is set so that its alert rate equals that contamination level. (p. 4)[^original]  
  <sub>anchor: "it leads to an alert rate equal to that contamination level"</sub>

## 4.3 Active learning

- **descriptive / method**: After an initial random sample, an unsupervised warm-up learner samples instances until the labeled pool includes at least one illicit instance. (p. 4)[^original]  
  <sub>anchor: "we use an unsupervised warm-up learner that samples instances until the labeled pool includes at least one illicit instance"</sub>
- **descriptive / method**: Once an illicit instance is in the labeled pool, the setup either switches to a supervised hot learner or keeps using the warm-up learner. (p. 4)[^original]  
  <sub>anchor: "we either switch to a supervised hot learner or continue to use the warm-up learner"</sub>
- **descriptive / method**: The classifiers used in active learning are RF, XGBoost and LR, the three supervised models from the supervised baselines. (p. 4)[^original]  
  <sub>anchor: "As the classifier, we use the three supervised models evaluated in the supervised baselines: RF, XGBoost, and LR"</sub>
- **descriptive / method**: All active learning setups are compared against a baseline that queries random instances at each iteration. (p. 4)[^original]  
  <sub>anchor: "We compare all AL setups against a baseline that queries random instances at each iteration"</sub>
- **descriptive / method**: The batch size is 50 instances sampled at each iteration for all experiments. (p. 4)[^original]  
  <sub>anchor: "We use a batch size of 50 instances sampled at each iteration for all experiments"</sub>
- **descriptive / method**: Each active learning setup is run five times with different random seeds to check robustness. (p. 4)[^original]  
  <sub>anchor: "Each AL setup is run five times with different random seeds"</sub>
- **descriptive / method**: Performance of each active learning setup is assessed through the median illicit F1-score and confidence intervals at each labeled pool size. (p. 4)[^original]  
  <sub>anchor: "We assess the performance of each AL setup through the median illicit F1-score and the confidence intervals"</sub>
- **descriptive / context**: The setup and parameter choices follow earlier work by Barata et al. developed at Feedzai concurrently. (p. 4)[^original]  
  <sub>anchor: "This setup and parameter choices follow the work by Barata et al. [2] developed at Feedzai concurrently"</sub>

---

[source overview](overview.md) | [next part](digest-002.md)

[^original]: arXiv, "Machine learning methods to detect money laundering in the Bitcoin blockchain in the presence of label scarcity" (2020-05-29). https://arxiv.org/abs/2005.14635
