---
type: Source Digest
title: Enhanced credit card fraud detection based on attention mechanism and LSTM deep model - part 2 of 3 (p. 1)
description: 'Verified paraphrased digest, p. 1: Methods and materials; Methods and materials > Datasets; Methods and materials > Dimensionality reduction; and 5 more sections'
resource: https://link.springer.com/article/10.1186/s40537-021-00541-8
tags:
- academic_finding
- academic_paper
- fraud_screening_synergies
- global_academic
- ml_statistics
- transaction_behaviour
status: stable
source_id: academic-publisher-enhanced-credit-card-fraud-detection-based-on-atten
issuer: academic_publisher
issuer_name: Academic publisher / repository
jurisdictions:
- GLOBAL_ACADEMIC
tier: 3
instrument_type: academic_paper
normative_force: academic_finding
publication_date: '2021-12-01'
legal_status: unknown
part: 2
parts_total: 3
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
  resource: https://link.springer.com/article/10.1186/s40537-021-00541-8
  title: Enhanced credit card fraud detection based on attention mechanism and LSTM deep model
  author: org:academic_publisher
  last_modified: '2021-12-01T00:00:00Z'
digest_points: 32
---

# Enhanced credit card fraud detection based on attention mechanism and LSTM deep model (digest)

[previous part](digest-001.md) | [source overview](overview.md) | [next part](digest-003.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (p. 1) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **academic finding**.

## Methods and materials

- **descriptive / method**: The proposed model first applies data preprocessing, using feature selection and dimensionality reduction on credit card fraud datasets to reduce the number of input features before they enter the model. (p. 1)[^original]  
  <sub>anchor: "our proposed model uses first data preprocessing techniques through applying feature selection and dimensionality reduction over credit card fraud datasets"</sub>
- **descriptive / method**: LSTM is employed as the base dynamic pattern recognition classifier to capture sequential dependency between consecutive credit card transactions. (p. 1)[^original]  
  <sub>anchor: "the sequence learner LSTM is employed as the base dynamic pattern recognition classifier to capture the sequential dependency"</sub>
- **descriptive / method**: An attention mechanism is applied to the hidden-layer outputs of the LSTM to give different focus to them, intended to discover relevant fraud patterns and detect very dissimilar transactions within a consumer's purchases. (p. 1)[^original]  
  <sub>anchor: "attention mechanism is introduced to give different focus to the information outputted from the hidden layers of LSTM"</sub>

## Datasets

- **descriptive / data or feature**: Dataset-1 is a Kaggle dataset of credit card transactions by European cardholders over two days in September 2013, containing 492 frauds out of 284,807 transactions. (p. 1)[^original]  
  <sub>anchor: "consists of credit card transactions made by European cardholders occurring within two days in September 2013, where it has 492 frauds out of 284,807 transactions"</sub>
- **descriptive / data or feature**: Dataset-1 has 31 features: the transaction time, the amount, 28 attributes labelled V1 to V28, and a binary target label 'Class' (1 for fraud, 0 for normal). (p. 1)[^original]  
  <sub>anchor: "It consists of 31 features including the time when a transaction took place, the amount of transactions, and 28 other attributes labeled from V1 to V28"</sub>
- **descriptive / data or feature**: Dataset-2 contains 594,643 transactions made over 180 simulated days, of which 7,200 (about 1.2%) are fraudulent. (p. 1)[^original]  
  <sub>anchor: "The second dataset consists of 594,643 transactions made during 180 simulated days, among which 7200"</sub>
- **descriptive / data or feature**: Dataset-2 is synthetic, created with the BankSim simulation tool, which uses a multi-agent simulation based on aggregated real transaction data from a bank in Spain. (p. 1)[^original]  
  <sub>anchor: "BankSim uses a multi-agent-based simulation methodology based on a sample of aggregated real transaction data that a bank in Spain offers"</sub>
- **descriptive / data or feature**: The original bank data used for BankSim covers transactions from November 2012 to April 2013, and BankSim uses traders, customers and fraudsters as agent categories. (p. 1)[^original]  
  <sub>anchor: "The original bank data is made up of thousands of transactional data records from November 2012 to April 2013"</sub>

## Dataset processing

- **descriptive / finding or result**: Both datasets are highly imbalanced; in Dataset-1 frauds are typically less than 0.171% of transactions. (p. 1)[^original]  
  <sub>anchor: "frauds are typically less than 0.171% of the overall transactions"</sub>

## Feature selection

- **descriptive / finding or result**: Swarm intelligence plots for Dataset-1 led the authors to remove the features Time, V5–V9, V13, V15, V16, V18–V28 and amount as not contributing to fraud prediction. (p. 1)[^original]  
  <sub>anchor: "features labeled Time, V5, V6, V7, V8, V9, V13, V15, V16, V18, V19, V20,V21, V22, V23, V24, V25, V26, V27, V28, amount do not contribute to the fraud prediction"</sub>

## Feature extraction

- **descriptive / method**: PCA, t-SNE and UMAP were each applied to reduce Dataset-1 to three dimensions with default parameters for visual comparison. (p. 1)[^original]  
  <sub>anchor: "We applied the three dimensionality reduction algorithms PCA, t-SNE and UMAP on our credit card datasets"</sub>
- **descriptive / finding or result**: PCA showed poor discrimination, whereas UMAP and t-SNE showed very good discrimination; UMAP was chosen because it better preserves local and global structure with superior runtime. (p. 1)[^original]  
  <sub>anchor: "It can be seen that PCA does not present good discrimination, whereas UMAP and t-SNE show very good discrimination"</sub>

## Implementation and evaluation metrics

- **descriptive / context**: LSTM processes all input elements in the same manner and cannot give more importance to some elements than others. (p. 1)[^original]  
  <sub>anchor: "LSTM networks process the input sequence elements with the same manner, there is no way to give more importance"</sub>
- **descriptive / method**: The attention mechanism is added on top of LSTM layers so the classifier can extract global dependencies and focus on the most relevant transactions. (p. 1)[^original]  
  <sub>anchor: "we propose to add the attention mechanism upon LSTM layers which enables the classifier to automatically extract global dependencies"</sub>
- **descriptive / method**: The LSTM uses tanh as activation function; the model was implemented in the Keras framework, and a baseline LSTM without the attention layer was built for comparison. (p. 1)[^original]  
  <sub>anchor: "This model is based on Keras deep learning framework which is an opensource neural network library written in Python"</sub>
- **descriptive / context**: Fraud detection systems aim to reduce both false positive and false negative rates; false negatives carry severe costs for financial institutions and reduce customer satisfaction. (p. 1)[^original]  
  <sub>anchor: "knowing that the latter (FN) has severe costs on financial institutions as well as a decrease in customer satisfaction"</sub>
- **descriptive / method**: Evaluation uses a confusion matrix yielding accuracy, sensitivity (recall), specificity and precision. (p. 1)[^original]  
  <sub>anchor: "From this matrix, the following evaluation metrics are extracted, namely: Accuracy, Sensitivity (or Recall), Specificity and Precision"</sub>
- **descriptive / definition**: Specificity measures accuracy on legitimate cases, precision measures accuracy among cases classified as fraud, and sensitivity (recall) measures accuracy on actual fraud cases. (p. 1)[^original]  
  <sub>anchor: "Specificity gives the accuracy on negative (legitimate) cases classification"</sub>
- **descriptive / definition**: False positives are normal transactions flagged as fraudulent, causing no significant damage; false negatives are fraud transactions wrongly labelled normal. (p. 1)[^original]  
  <sub>anchor: "False positives (FP) are cases classified by the Fraud Detection System (FDS) as fraudulent transactions but represent in reality normal behaviors"</sub>
- **descriptive / method**: The authors treat sensitivity (recall) as the most appropriate evaluation metric for this domain. (p. 1)[^original]  
  <sub>anchor: "Therefore, we will be interested more to the sensitivity (Recall) metric"</sub>

## Results and discussion

- **descriptive / method**: Each dataset is split 70% training, 15% validation (to avoid overfitting) and 15% test; the same training and test sets were used for comparison with the baseline LSTM. (p. 1)[^original]  
  <sub>anchor: "The first 70% subset of data is the training set used for training the models"</sub>
- **descriptive / finding or result**: On Dataset-1 the LSTM-attention model achieved superior accuracy and sensitivity (recall) compared with the baseline LSTM, which the authors attribute to the data-driven weighted average over transactions. (p. 1)[^original]  
  <sub>anchor: "our model (LSTM-attention) achieved the more superior accuracy and sensitivity (recall) rates"</sub>
- **descriptive / finding or result**: Confusion matrices indicate the proposed model reduces fraudulent transactions classified as normal and catches rare fraud transactions. (p. 1)[^original]  
  <sub>anchor: "our proposed model has a good capability to minimize the number of fraudulent transactions classified as normal"</sub>
- **descriptive / finding or result**: The proposed model was compared with state-of-the-art models on Dataset-1 in accuracy, precision and sensitivity, and it outperformed GRU, LSTM, SVM, KNN and ANN. (p. 1)[^original]  
  <sub>anchor: "our proposed model achieves better results than the compared classification GRU, LSTM, SVM, KNN and ANN methods"</sub>

## Conclusion

- **descriptive / finding or result**: The authors claim the combined pipeline (swarm-based feature selection, UMAP, SMOTE, LSTM and attention) delivers high sensitivity on two datasets and very good performance versus recent works. (p. 1)[^original]  
  <sub>anchor: "it shows its ability to deliver a high sensitivity performance during the detection of fraudulent instances"</sub>

## Dataset processing

- **descriptive / method**: SMOTE is used to generate synthetic training instances from the minority fraud class to improve classification of minority instances. (p. 1)[^original]  
  <sub>anchor: "to generate synthetic training instances from the minority class"</sub>

## Implementation and evaluation metrics

- **descriptive / limitation**: LSTM networks have limitations: they must represent the whole input sequence as a single vector, which can cause information loss and degrades rapidly as the input sequence gets longer. (p. 1)[^original]  
  <sub>anchor: "which can cause information loss since all information needs to be compressed into c"</sub>
- **descriptive / limitation**: The authors state that LSTM performance degrades rapidly as the length of the input sequence increases. (p. 1)[^original]  
  <sub>anchor: "the performance of the LSTM networks degrade rapidly as the length of the input sequence increases"</sub>
- **descriptive / method**: The proposed deep model is composed of six layers, including two LSTM layers each followed by dropout. (p. 1)[^original]  
  <sub>anchor: "Two layered LSTM networks followed by dropout on each layer"</sub>
- **descriptive / method**: An attention layer is added before the LSTM layer in the proposed model, and the LSTM takes the attention layer's output as its input with tanh activation. (p. 1)[^original]  
  <sub>anchor: "an attention layer added before the LSTM layer as depicted in Fig. 9"</sub>
- **descriptive / method**: A dense layer after the two LSTM layers gives two outputs (normal transaction and fraud transaction), then a BatchNormalization layer is applied and its output passes into a softmax classification layer. (p. 1)[^original]  
  <sub>anchor: "At the end of the two LSTM layers, we add a dense layer to obtain two valued outputs"</sub>

## Conclusion

- **descriptive / context**: The authors plan to study a novel credit card fraud detection model relying solely on attention and transformer architectures, without recurrent networks. (p. 1)[^original]  
  <sub>anchor: "we plan to study a novel credit card fraud detection model that relies solely on attention and transformers architecture"</sub>

---

[previous part](digest-001.md) | [source overview](overview.md) | [next part](digest-003.md)

[^original]: Academic publisher / repository, "Enhanced credit card fraud detection based on attention mechanism and LSTM deep model" (2021-12-01). https://link.springer.com/article/10.1186/s40537-021-00541-8
