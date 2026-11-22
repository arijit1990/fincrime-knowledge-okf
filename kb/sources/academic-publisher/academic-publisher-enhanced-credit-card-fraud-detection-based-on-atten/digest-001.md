---
type: Source Digest
title: Enhanced credit card fraud detection based on attention mechanism and LSTM deep model - part 1 of 3 (p. 1)
description: 'Verified paraphrased digest, p. 1: Abstract; Abstract > Explore related subjects; Introduction; and 4 more sections'
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
part: 1
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
digest_points: 34
---

# Enhanced credit card fraud detection based on attention mechanism and LSTM deep model (digest)

[source overview](overview.md) | [next part](digest-002.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (p. 1) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **academic finding**.

## Abstract

- **descriptive / method**: The paper proposes a credit card fraud detection system based on sequential modelling of transaction data using an attention mechanism and LSTM deep recurrent neural networks, aiming to identify the most important transactions in the input sequence. (p. 1)[^original]  
  <sub>anchor: "develop a novel system for credit card fraud detection based on sequential modeling of data, using attention mechanism and LSTM deep recurrent neural networks"</sub>
- **descriptive / method**: The model combines three sub-methods: UMAP for selecting useful predictive features, LSTM for incorporating transaction sequences, and an attention mechanism to enhance LSTM performance. (p. 1)[^original]  
  <sub>anchor: "the uniform manifold approximation and projection (UMAP) for selecting the most useful predictive features"</sub>
- **descriptive / finding or result**: The authors state that experiments give strong results in efficiency and effectiveness. (p. 1)[^original]  
  <sub>anchor: "The experimentations of our model give strong results in terms of efficiency and effectiveness."</sub>

## Introduction

- **descriptive / context**: Fraudsters continuously invent novel fraud patterns, including patterns designed to adapt to fraud detection techniques, making credit card fraud detection challenging. (p. 1)[^original]  
  <sub>anchor: "Fraudsters continuously invent novel fraud patterns, especially those that they use to adapt to fraud detection techniques."</sub>
- **descriptive / limitation**: Machine learning models that are never updated are considered inadequate because they do not account for changes and trends in customer spending behaviour, such as during holiday periods and across geographical regions. (p. 1)[^original]  
  <sub>anchor: "Machine learning models that are never updated are inadequate as they do not take account of changes and trends in customer spending behaviors"</sub>
- **expected / expectation**: Financial institutions should continuously establish increasingly sophisticated fraud detection systems to detect fraud immediately and prevent it before it occurs, protect consumers and reduce heavy annual losses. (p. 1)[^original]  
  <sub>anchor: "financial institutions should establish continuously an increasingly sophisticated fraud detection system (FDS)"</sub>
- **descriptive / method**: The proposed system is based on LSTM networks and an attention mechanism, which lets a sequence-based network focus on the most important data items through a data-driven weighted average of local information. (p. 1)[^original]  
  <sub>anchor: "The attention mechanism allows a sequence based neural network to automatically focus on the data items that are the most important"</sub>
- **descriptive / method**: Contribution 1: feature selection and dimension reduction using PCA, t-SNE and UMAP to optimise classifier learning. (p. 1)[^original]  
  <sub>anchor: "Optimizing the process of learning classifiers by using feature selection and dimension reduction algorithms such as PCA, t-SNE and UMAP."</sub>
- **descriptive / method**: Contribution 2: SMOTE is used to address the imbalanced dataset and increase the learning rate. (p. 1)[^original]  
  <sub>anchor: "Overcoming the issue of the imbalanced dataset and incrementing the learning rate by using the Synthetic Minority Oversampling Technique (SMOTE)."</sub>
- **descriptive / method**: Contribution 3: LSTM recurrent networks are used as a dynamic pattern recognition classifier to model long-term dependencies within transaction sequences and build the context of consumer spending behaviour. (p. 1)[^original]  
  <sub>anchor: "Constructing the context of consumer’s spending behavior by using the sequence learner LSTM recurrent neural networks"</sub>
- **descriptive / method**: Contribution 4: an attention mechanism is applied on top of LSTM networks so the classifier learns where to pay selective attention in the input sequence for the global fraud decision. (p. 1)[^original]  
  <sub>anchor: "Applying the attention mechanism upon LSTM recurrent networks, that efficiently allows the classifier to learn where to pay selective attention"</sub>
- **descriptive / finding or result**: Contribution 5: experiments on two datasets are said to show the method is competitive with and an alternative to existing LSTM works. (p. 1)[^original]  
  <sub>anchor: "Performing experiments on two different datasets from which we conclude that our method is competitive and alternative to existing LSTM works."</sub>
- **descriptive / context**: Source code and results are made available at a public GitHub repository to ensure reproducibility. (p. 1)[^original]  
  <sub>anchor: "In order to ensure reproducibility, the source code and results of the proposed model can be found at"</sub>

## Related works

- **descriptive / context**: Payment card fraud detection has used supervised, unsupervised, anomaly detection and ensemble learning approaches, including support vector machines, hidden Markov models, logistic regression, decision trees, random forests and k-nearest neighbours. (p. 1)[^original]  
  <sub>anchor: "A wide range of machine learning approaches based on supervised learning, unsupervised learning, anomaly detection and ensemble learning have been used"</sub>
- **descriptive / definition**: Supervised classification trains on pre-classified datasets of labelled historical transactions to predict whether a new transaction is fraudulent. (p. 1)[^original]  
  <sub>anchor: "where pre-classified datasets containing labeled historical transactions are used for training a classifier"</sub>
- **descriptive / definition**: Unsupervised methods detect unusual behaviour and flag transactions that do not conform to the model as potential fraud, which can reveal new fraud patterns. (p. 1)[^original]  
  <sub>anchor: "Unsupervised classification methods are used to detect unusual behavior of a system"</sub>
- **descriptive / limitation**: Credit card fraud datasets are highly imbalanced, as genuine transactions far outnumber fraudulent ones, so many traditional classifiers fail to detect minority-class objects. (p. 1)[^original]  
  <sub>anchor: "credit card fraud data sets are highly imbalanced since the number of genuine transactions is much higher than the fraudulent ones"</sub>
- **descriptive / limitation**: Traditional classifiers use only individual transaction information such as amount, time and location and ignore sequential information that defines consumer profiles, so they are inadequate. (p. 1)[^original]  
  <sub>anchor: "but ignore detailed sequential information that defines consumers’ profile"</sub>
- **descriptive / context**: RNNs and particularly LSTMs are used in fraud detection given their reputation as accurate sequence-analysis learners and their ability to model sequential dependencies between consecutive transactions. (p. 1)[^original]  
  <sub>anchor: "given their reputation as one of the most accurate learning algorithms in sequence analysis work"</sub>
- **descriptive / context**: Attention was proposed to find context-dependent representations that account for dependencies between sequence items regardless of distance, and has been used in machine translation and image captioning. (p. 1)[^original]  
  <sub>anchor: "This method takes into account dependencies between items in a sequence despite of their distance."</sub>
- **descriptive / context**: Feature selection and extraction are fundamental preprocessing steps that remove redundant, noisy and irrelevant features, reducing computational cost without harming classification accuracy. (p. 1)[^original]  
  <sub>anchor: "by removing redundant, noisy and irrelevant features from the original dataset"</sub>

## Background

- **descriptive / method**: Feature selection uses swarm intelligence based feature selection to explore the datasets and study each feature's influence on predicting the target class. (p. 1)[^original]  
  <sub>anchor: "Swarm intelligence based feature selection approach [ 43 ] will be used to explore our datasets"</sub>

## Feature extraction

- **descriptive / method**: Three dimensionality reduction algorithms are employed: PCA, t-SNE and UMAP, described as among the best for feature extraction in applications such as bioinformatics and visualisation. (p. 1)[^original]  
  <sub>anchor: "we employ three algorithms to reduce the dataset dimensionality, namely Principal Component Analysis (PCA)"</sub>
- **descriptive / definition**: PCA transforms n correlated variables into m uncorrelated principal components that successively maximise variance, derived in decreasing order of importance as linear combinations of the original variables. (p. 1)[^original]  
  <sub>anchor: "aiming to transform the original set of n correlated variables to a new subset of m uncorrelated variables"</sub>
- **descriptive / limitation**: PCA is linear and may perform poorly on features with nonlinear relationships, motivating nonlinear methods such as t-SNE and UMAP. (p. 1)[^original]  
  <sub>anchor: "as a linear algorithm, it may performs poorly on the features with nonlinear relationship"</sub>
- **descriptive / definition**: t-SNE maps high-dimensional data into two or three dimensions while preserving neighbourhood identity, using probability distributions over pairs of points and minimising Kullback–Leibler divergence. (p. 1)[^original]  
  <sub>anchor: "aims to minimize the Kullback–Leibler (KL) divergence between the two distributions"</sub>
- **descriptive / limitation**: t-SNE computes pairwise conditional probabilities for every sample pair, has hyperparameters that are hard to tune, and has a high computational cost. (p. 1)[^original]  
  <sub>anchor: "it computes pairwise conditional probabilities for each pair of samples and involves hyperparameters that are not always simple to tune"</sub>
- **descriptive / definition**: UMAP is a graph-based, Riemannian-geometry-grounded dimensionality reduction technique that builds a weighted k-neighbour graph and finds a low-dimensional projection with a similar fuzzy topological structure. (p. 1)[^original]  
  <sub>anchor: "Unlike t-SNE which utilizes probabilistic model, UMAP is a graph-based algorithm."</sub>
- **descriptive / finding or result**: Compared with t-SNE, UMAP is said to preserve more of the local and global structure with superior runtime performance. (p. 1)[^original]  
  <sub>anchor: "Compared to t-SNE, UMAP is better able to preserve as much of the local and more of the global data structure"</sub>

## Long Short Term Memory networks

- **descriptive / definition**: LSTM is a type of recurrent neural network with feedback connections that learn long-term sequence dependencies, developed to overcome vanishing and exploding gradients in traditional RNNs. (p. 1)[^original]  
  <sub>anchor: "LSTMs were developed to overcome the problem of vanishing and exploding gradient"</sub>
- **descriptive / definition**: An LSTM unit has a memory cell regulated by an input gate, a forget gate and an output gate that control information flow into and out of the cell. (p. 1)[^original]  
  <sub>anchor: "LSTM unit consists of a memory cell that stores information which is updated by three special gates"</sub>
- **descriptive / method**: The LSTM unit computation proceeds in six steps: candidate cell value (Eq. 7), input gate (Eq. 8), forget gate (Eq. 9), memory cell update (Eq. 10), output gate (Eq. 11) and unit output (Eq. 12). (p. 1)[^original]  
  <sub>anchor: "The LSTM unit calculation method can be divided into the steps below:"</sub>

## Attention mechanism

- **descriptive / definition**: Attention mechanisms select the most relevant information rather than all of it, and are widely used in computer vision and language translation. (p. 1)[^original]  
  <sub>anchor: "This mechanism aims to focus only on the most relevant piece of information, rather than all of it"</sub>
- **descriptive / method**: In an RNN encoder–decoder with attention, the context vector is a weighted sum of encoder annotations, with weights given by an alignment model scoring the match between decoder state and each annotation. (p. 1)[^original]  
  <sub>anchor: "A weighted sum of those annotations h t forms the context vector c t"</sub>

---

[source overview](overview.md) | [next part](digest-002.md)

[^original]: Academic publisher / repository, "Enhanced credit card fraud detection based on attention mechanism and LSTM deep model" (2021-12-01). https://link.springer.com/article/10.1186/s40537-021-00541-8
