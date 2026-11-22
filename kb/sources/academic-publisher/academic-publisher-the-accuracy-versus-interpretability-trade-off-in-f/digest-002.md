---
type: Source Digest
title: The accuracy versus interpretability trade-off in fraud detection model - part 2 of 3 (p. 1)
description: 'Verified paraphrased digest, p. 1: The accuracy versus interpretability trade-off in fraud detection model > 3. SOTA Review of Fraud Detection; The accuracy versus interpretability trade-off in fraud detection model > 4. Experimentation'
resource: https://www.cambridge.org/core/journals/data-and-policy/article/accuracy-versus-interpretability-tradeoff-in-fraud-detection-model/3BA1586A6B635E08BE556FAB89AD8770
tags:
- academic_finding
- academic_paper
- fraud_screening_synergies
- global_academic
- ml_statistics
- model_monitoring
status: stable
source_id: academic-publisher-the-accuracy-versus-interpretability-trade-off-in-f
issuer: academic_publisher
issuer_name: Academic publisher / repository
jurisdictions:
- GLOBAL_ACADEMIC
tier: 3
instrument_type: academic_paper
normative_force: academic_finding
publication_date: '2021-01-01'
legal_status: unknown
part: 2
parts_total: 3
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
  resource: https://www.cambridge.org/core/journals/data-and-policy/article/accuracy-versus-interpretability-tradeoff-in-fraud-detection-model/3BA1586A6B635E08BE556FAB89AD8770
  title: The accuracy versus interpretability trade-off in fraud detection model
  author: org:academic_publisher
  last_modified: '2021-01-01T00:00:00Z'
digest_points: 56
---

# The accuracy versus interpretability trade-off in fraud detection model (digest)

[previous part](digest-001.md) | [source overview](overview.md) | [next part](digest-003.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (p. 1) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **academic finding**.

## 3.1. Dealing with imbalanced data

- **descriptive / method**: Algorithm modification gives more weight to the minority class; the paper notes that performance metrics must be adapted to the class imbalance to optimise parameters and assess algorithm validity. (p. 1)[^original]  
  <sub>anchor: "it is crucial to adapt performance metrics in order to optimize parameters and assess the validity of the algorithm"</sub>
- **descriptive / method**: Cost-sensitive learning gives more weight to fraudulent observations than normal ones, changing the cost function. (p. 1)[^original]  
  <sub>anchor: "Another approach is to give more weight to fraudulent observations than to normal observations."</sub>
- **descriptive / limitation**: Cost-sensitive learning modifies misclassification cost globally and so cannot address long-tailed costs linked to the amount of each operation. (p. 1)[^original]  
  <sub>anchor: "Hence it cannot respond to the issue of long-tailed costs"</sub>
- **descriptive / method**: One possible solution is business under-sampling, dropping low-value fraud using business knowledge, for example isolated fraudulent contactless payments under 10 euro; this focuses detection on costly frauds. (p. 1)[^original]  
  <sub>anchor: "isolated fraudulent contactless payments of less than 10€ are not worth treating"</sub>
- **descriptive / finding or result**: Data-level balancing techniques such as SMOTE tend to be preferred over modifying the algorithm when dealing with fraud data. (p. 1)[^original]  
  <sub>anchor: "using data level balancing techniques, like SMOTE, tends to be preferred instead of modifying the algorithm"</sub>

## 3.2. Dealing with the lack of fully trusted labels

- **recommended / expectation**: Where labelled data is not fully trusted, the paper recommends anomaly detection methods that are semi-supervised or unsupervised. (p. 1)[^original]  
  <sub>anchor: "It is therefore recommended, in the case of not fully trusted labeled data, to use anomaly detection methods"</sub>
- **descriptive / context**: Real fraud datasets often contain frauds among the nonfraudulent observations, since successful fraud tends to go unnoticed. (p. 1)[^original]  
  <sub>anchor: "real fraud datasets often have frauds among the “nonfraudulent” observations"</sub>
- **descriptive / method**: Semi-supervised anomaly detectors are trained on non-fraudulent observations and flag abnormal observations at test time; One-class SVM is the best known, and autoencoder neural approaches have also been developed. (p. 1)[^original]  
  <sub>anchor: "Semi-supervised algorithms are trained on nonfraudulent observations and then detect abnormal"</sub>
- **descriptive / method**: Distance-based unsupervised methods such as k-nearest neighbours and density-based methods such as local outlier factor, its connectivity-based variant COF, and isolation forest are described as anomaly detectors. (p. 1)[^original]  
  <sub>anchor: "Most methods are linked to the neighborhood of the observations"</sub>
- **descriptive / method**: Other unsupervised anomaly methods include cluster-based LOF (CBLOF), DBSCAN, statistical tests and robust principal component analysis based on dimension reduction. (p. 1)[^original]  
  <sub>anchor: "Most recent methods are based on other clustering methods aiming to detect anomalies"</sub>
- **descriptive / finding or result**: Surveys indicate anomaly or outlier detection was one of the main techniques in credit card fraud detection in 2004 and still in 2016. (p. 1)[^original]  
  <sub>anchor: "anomaly or outlier detection was one of the main techniques used in credit card fraud detection in 2004"</sub>
- **descriptive / finding or result**: Anomaly detection is attractive because it handles missing trusted labels and partly addresses concept drift. (p. 1)[^original]  
  <sub>anchor: "this kind of algorithm can easily handle not only the lack of trusted labels"</sub>

## 3.3. Dealing with the drifting of frauds

- **descriptive / definition**: Concept drift occurs as fraudsters adapt behaviour, when the underlying distribution of the target concept depends on hidden contexts, and requires model re-training. (p. 1)[^original]  
  <sub>anchor: "this phenomenon, called concept drift , appears when the underlying distribution of target concept depends on hidden contexts"</sub>
- **descriptive / method**: Supervised classifiers can be continuously updated through regular relearning on a sliding window. (p. 1)[^original]  
  <sub>anchor: "regular relearning on a sliding window"</sub>
- **descriptive / method**: For gradually drifting environments such as bank cheque operations, a retraining frequency or threshold can be chosen; this is called offline learning mode. (p. 1)[^original]  
  <sub>anchor: "It is named offline learning mode"</sub>
- **descriptive / context**: Abrupt changes or voluminous, swift operations such as credit card transactions call for online learning on stream data that adapts to drift, is robust to noise and handles recurring contexts. (p. 1)[^original]  
  <sub>anchor: "new stakes arise adapt to concept drift, be robust to noise and able to treat recurring contexts"</sub>
- **descriptive / method**: Incremental models such as Hoeffding trees require adapting the model for each new example; window-based methods such as FLORA2 use the most recent examples of fixed or adaptive size to save memory and time. (p. 1)[^original]  
  <sub>anchor: "several methods propose to work on a window containing the most recent examples"</sub>
- **descriptive / method**: Drift detection compares distributions using tests such as CUSUM, Shiryaev–Roberts, and the adaptive-window ADWIN; after drift, options include relearning on full history or new data, or reusing an old context model as in FLORA3. (p. 1)[^original]  
  <sub>anchor: "More recent models tend to adapt the size of window to compare distributions, ADWIN is one of these examples"</sub>

## 3.4. Dealing with the need of interpretability

- **descriptive / context**: Practitioners need interpretable results to act; three main approaches are identified: intrinsically interpretable models and post hoc specific or agnostic methods. (p. 1)[^original]  
  <sub>anchor: "practitioners need interpretable results to act"</sub>
- **descriptive / definition**: Intrinsically interpretable models such as linear and logistic regression, decision trees, generalised additive models and business rules are transparent and self-explainable, generally used under legal or policy constraints but possibly not accurate enough for fraud detection. (p. 1)[^original]  
  <sub>anchor: "They are generally applied for use cases with legal or policy constraints"</sub>
- **descriptive / limitation**: The main disadvantage of model-specific post-hoc methods is that each is restricted to one model type, making comparison across different models difficult. (p. 1)[^original]  
  <sub>anchor: "their use is restricted to a single type of model and it is therefore complicated to compare"</sub>
- **descriptive / method**: Model-agnostic post-hoc methods can be global, giving an overall view of the model, or local, explaining a particular case or observation. (p. 1)[^original]  
  <sub>anchor: "They can be macro (or global) in order to obtain an overall view of the model"</sub>
- **descriptive / method**: Visual agnostic methods include partial dependence plots and accumulated local effects plots for global views and individual conditional expectation curves for local views; model reliance and variable interaction tools such as interaction strength and VIN analyse variable importance and interactions. (p. 1)[^original]  
  <sub>anchor: "The main ones are partial dependence plot (PDP) curves"</sub>
- **descriptive / method**: Surrogate models approximate a black box with a more interpretable model; local examples are LIME, MAHE and SHAP and its derivatives. (p. 1)[^original]  
  <sub>anchor: "The best-known local surrogate models are local interpretable model-agnostic explanation"</sub>
- **descriptive / method**: Counterfactual reasoning explains how a prediction changes when the observation changes, and knowledge distillation transfers knowledge from a large model to a smaller interpretable one such as a decision tree. (p. 1)[^original]  
  <sub>anchor: "They aim at answering the question “how is the prediction modified when the observation changes?”"</sub>
- **descriptive / context**: Some authors hold that interpretable models should be strengthened to increase accuracy, while others favour black box models with post hoc interpretability. (p. 1)[^original]  
  <sub>anchor: "some authors believe that it is necessary to strengthen interpretable models to increase accuracy"</sub>

## 3.5. Dealing with accuracy under constrains

- **descriptive / context**: Fraud detection faces financial and operational constraints requiring both precision and interpretability, a trade-off the paper describes as a key issue in machine learning. (p. 1)[^original]  
  <sub>anchor: "This trade-off between precision and interpretability is a key issue in the field of machine learning"</sub>
- **descriptive / finding or result**: Traditional supervised models such as random forest and XGBoost often outperform other combinations of methods designed for fraud specificities on fraud data. (p. 1)[^original]  
  <sub>anchor: "traditional supervised models outperform other combinations of methods designed to overcome the specificities of fraud"</sub>
- **descriptive / context**: Models are ranked on accuracy (x-axis) and interpretability (y-axis); black box researchers seek interpretability while interpretable-model researchers seek precision, and only the most advanced researchers call for hybrid methods. (p. 1)[^original]  
  <sub>anchor: "Only most advanced researchers in both tribes have recently started to call for hybrid methods development"</sub>

## 4. Experimentation

- **descriptive / context**: The experiment is a real-world application under the Cerberus European project financed by the ERDF, in which two private AI actors cooperated on fraud management solutions. (p. 1)[^original]  
  <sub>anchor: "The experimentation takes place in the framework of a European project financed by the ERDF, called Cerberus"</sub>

## 4.1. Experimentation context

- **descriptive / case example**: Bleckwen developed anti-fraud software for instant cash transfer fraud, based on an XGBoost black box score with a local interpretative overlay; operations above an optimal threshold are suspended and must be investigated. (p. 1)[^original]  
  <sub>anchor: "all operations over a given optimal threshold are suspended and must be investigated"</sub>
- **descriptive / method**: Quinten adapted intrinsically interpretable methods based on the Q-Finder algorithm, generating optimised business decision rules from historical data and classifying operations as a binary fraud or not-fraud alert, applied to cheque fraud. (p. 1)[^original]  
  <sub>anchor: "This method generates automatically from historical data optimized business decision rules"</sub>
- **descriptive / context**: Cheque fraud has lower volumes and slower processes, as customers accept a several-hour delay, so instant operation is not needed; a hybrid of rule generation and fraud scoring was tested. (p. 1)[^original]  
  <sub>anchor: "instant operation is not needed as customers accept a several hours delay for this operation"</sub>

## 4.2. Description of the experimentation

- **descriptive / method**: The cheque fraud experiment followed six main steps typical of CRISP-DM data mining processes. (p. 1)[^original]  
  <sub>anchor: "The experiment on cheque fraud management followed six main steps"</sub>
- **descriptive / context**: Interpretability was needed to justify actions such as account suspension and suspicion declarations, and to help investigators analyse a limited number of fraud factors. (p. 1)[^original]  
  <sub>anchor: "Besides the need to justify action (account suspension, declaration of suspicion to authorities, etc.)"</sub>
- **descriptive / context**: Only three persons knew the exact business rules, which were modified manually and kept confidential to avoid leaks to fraudsters. (p. 1)[^original]  
  <sub>anchor: "The exact business rules applied on the first automated alerting task were known only by three persons"</sub>
- **descriptive / context**: The anti-fraud department could handle no more than 30 daily alerts with existing FTE; fraud caused several million euros of losses per year, and the aim was to optimise rules under human resource constraints. (p. 1)[^original]  
  <sub>anchor: "with an anti-fraud department able to handle no more than 30 daily alerts with the existing FTE"</sub>

## 4.2.2. Data understanding

- **descriptive / data or feature**: The data comprised 85 tables from 5 sources covering October 2018 to September 2019, over 16,000,000 historical cheques and more than 200 variables, qualified with the Databook framework. (p. 1)[^original]  
  <sub>anchor: "The collected data represented 85 tables from 5 different sources and covered the period from October 2018"</sub>

## 4.2.3. Data preparation

- **descriptive / data or feature**: Feature engineering produced 343,609 historical cheque deposits described by 300 patterns; 130 were kept as relevant and grouped into 12 categories. (p. 1)[^original]  
  <sub>anchor: "representing 343,609 historical cheque deposits characterized by 300 patterns"</sub>
- **descriptive / method**: Operations under a business-defined amount were excluded, avoiding mixing heavy and frequent fraud profiles and under-sampling non-fraud operations; fraud was 0.1% of cheque deposits. (p. 1)[^original]  
  <sub>anchor: "The rare fraud phenomenon represented 0.1% of the cheque deposits"</sub>
- **descriptive / method**: The learning matrix was split into 9 months for training and 3 months for testing, with three folds stratified on fraudulent clients to optimise a random forest. (p. 1)[^original]  
  <sub>anchor: "split into 9 months of historical data to train the models and 3 months to have a test set"</sub>

## 4.2.4. Modeling

- **descriptive / method**: Q-Finder generates many intersecting rules with good fraud coverage and interpretable variables, but too many false positives; an optimal rule combination with an F-beta score (beta 3, weighting Recall) reduces false positives. (p. 1)[^original]  
  <sub>anchor: "an F-beta score is used with, for example, beta equal to 3 to give more weight to the Recall"</sub>
- **descriptive / finding or result**: The statistical accuracy of the hybrid model on the test set was a Precision of 5.6% and a Recall of 77.8%, from the confusion matrix in Table 2. (p. 1)[^original]  
  <sub>anchor: "the statistical assessment of the accuracy of the model was a Precision of 5.6% and a Recall of 77.8% on the test set"</sub>
- **descriptive / method**: Because concept drift can make rules inaccurate, the score model is enhanced with online learning and a score-threshold rule; when unexplained alerts become too numerous, new optimised rules are learned from recent data. (p. 1)[^original]  
  <sub>anchor: "When the number of alerts not explained by the business rules starts to be too high"</sub>

## 4.2.5. Evaluation

- **descriptive / finding or result**: Most fraud cases detected monthly by a score at a 50% threshold were also detected by the rules, so interpretable rules can be favoured operationally; the combination gives better results while adding only a limited number of daily alerts. (p. 1)[^original]  
  <sub>anchor: "most of the fraudulent operations detected each month by a score with a threshold at 50% are also detected by the rules"</sub>
- **descriptive / finding or result**: Evaluation focused on business indicators; only numbers of fraud cases detected were reported for confidentiality, and the hybrid was judged immediately operational and promising by banking partners. (p. 1)[^original]  
  <sub>anchor: "only the numbers of fraud cases detected will be reported"</sub>

## 4.2.6. Deployment

- **descriptive / finding or result**: The authors conclude that the performance of AI fraud devices is far from solely statistical under investment constraints. (p. 1)[^original]  
  <sub>anchor: "the “performance” of such AI devices are far from being solely statistical"</sub>

## 3.1. Dealing with imbalanced data

- **descriptive / method**: Some algorithms, mainly tree structures, take the class imbalance into account; examples cited are SMOTE Boost, MetaCost and AdaCost. (p. 1)[^original]  
  <sub>anchor: "some algorithms (mainly tree structures) take into account the imbalance of the classes"</sub>

## 3.5. Dealing with accuracy under constrains

- **descriptive / context**: Comparisons between first-generation rule-based industrial systems and recent machine learning approaches have begun to highlight the need for interdisciplinary research to better integrate human factors. (p. 1)[^original]  
  <sub>anchor: "have begun to highlight the need for interdisciplinary research in order to better integrate human factors"</sub>

## 4.2.4. Modeling

- **descriptive / method**: A black box score model was developed in parallel on all operations and is applied after the rules so that alerts can be prioritised by score, which speeds up expert work without deteriorating the intelligible explanation. (p. 1)[^original]  
  <sub>anchor: "a black box score model developed in parallel on all the operations"</sub>
- **descriptive / method**: When alert volume is below the capacity of dedicated human resources, the rule set can be completed with a complementary scoring rule covering operations with a score over a very high threshold, which is harder to interpret but enhances fraud coverage. (p. 1)[^original]  
  <sub>anchor: "If the number of alerts punctually creates an investigative workload that is even less than the capacity"</sub>
- **descriptive / method**: The optimised rule combination uses an F-beta score, for example with beta equal to 3, to give more weight to recall while reducing false positives. (p. 1)[^original]  
  <sub>anchor: "an F-beta score is used with, for example, beta equal to 3 to give more weight to the Recall"</sub>
- **descriptive / finding or result**: The statistical assessment of the model on the test set gave a Precision of 5.6% and a Recall of 77.8%. (p. 1)[^original]  
  <sub>anchor: "a Precision of 5.6% and a Recall of 77.8% on the test set"</sub>
- **descriptive / finding or result**: Over the lifecycle, only exceptional frauds would have passed undetected, and these outliers did not appear to be economically pertinent to detect. (p. 1)[^original]  
  <sub>anchor: "only exceptional frauds would have passed under the radar: these outliers did not appear to be economically pertinent to detect"</sub>

## 4.2.6. Deployment

- **descriptive / context**: The solution is being deployed with two user interfaces designed for collaborative investigation and monitoring tasks. (p. 1)[^original]  
  <sub>anchor: "in association with two user interfaces designed for the collaborative investigation and the monitoring tasks"</sub>
- **descriptive / context**: Further model optimisation, such as an interpretative overlay on score-rule alerts, seems tempting, but other considerations appear more pragmatic, such as fraud perimeter enlargement. (p. 1)[^original]  
  <sub>anchor: "other considerations appear as much more pragmatic, such as fraud perimeter enlargement"</sub>

---

[previous part](digest-001.md) | [source overview](overview.md) | [next part](digest-003.md)

[^original]: Anna Nesvijevskaia, Sophie Ouillade, Pauline Guilmin, Jean‐Daniel Zucker, "The accuracy versus interpretability trade-off in fraud detection model" (2021-01-01). https://www.cambridge.org/core/journals/data-and-policy/article/accuracy-versus-interpretability-tradeoff-in-fraud-detection-model/3BA1586A6B635E08BE556FAB89AD8770
