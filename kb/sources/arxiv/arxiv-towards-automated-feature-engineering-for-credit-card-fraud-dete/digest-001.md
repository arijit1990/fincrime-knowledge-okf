---
type: Source Digest
title: Towards automated feature engineering for credit card fraud detection using multi-perspective HMMs - part 1 of 3 (pp. 1-11)
description: 'Verified paraphrased digest, pp. 1-11: Abstract; Introduction; 1 Related Work > 1.1 Credit card fraud detection; and 2 more sections'
resource: https://arxiv.org/abs/1909.01185
tags:
- academic_finding
- data_features
- global_academic
- ml_statistics
- preprint
- transaction_behaviour
status: stable
source_id: arxiv-towards-automated-feature-engineering-for-credit-card-fraud-dete
issuer: arxiv
issuer_name: arXiv
jurisdictions:
- GLOBAL_ACADEMIC
tier: 3
instrument_type: preprint
normative_force: academic_finding
publication_date: '2019-03-09'
legal_status: unknown
part: 1
parts_total: 3
content_mode: digest
generated:
  by: claude-code-subagent/claude-sonnet-5-5
  at: '2026-11-22T14:46:06Z'
verified:
- by: process:kb-digest-check/anchor-match
  at: '2026-11-22T14:46:06Z'
- by: claude-code-judge-agent/claude-opus-5-5
  at: '2026-11-22T14:46:06Z'
sources:
- id: original
  resource: https://arxiv.org/abs/1909.01185
  title: Towards automated feature engineering for credit card fraud detection using multi-perspective HMMs
  author: org:arxiv
  last_modified: '2019-03-09T00:00:00Z'
digest_points: 60
---

# Towards automated feature engineering for credit card fraud detection using multi-perspective HMMs (digest)

[source overview](overview.md) | [next part](digest-002.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (pp. 1-11) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **academic finding**.

## Abstract

- **descriptive / context**: The paper models credit card transaction sequences from three binary perspectives: fraud presence, fixing the cardholder or payment terminal, and spent amount or elapsed time; the eight combinations each yield a Hidden Markov Model whose likelihoods are used as extra features in a Random Forest. (p. 1)[^original]  
  <sub>anchor: "Combinations of the three binary perspectives give eight sets of sequences from the (training) set of transactions."</sub>
- **descriptive / finding or result**: The authors claim the multi-perspective HMM approach improves detection of fraudulent transactions when combined with the state-of-the-art expert-based feature engineering strategy. (p. 1)[^original]  
  <sub>anchor: "allows for an increase in the detection of fraudulent transactions when combined with the state of the art expert based feature engineering strategy"</sub>
- **descriptive / finding or result**: The approach is reported to extend beyond e-commerce transactions and to be robust across datasets, hyperparameters and classifiers; the paper also compares strategies for structural missing values. (p. 1)[^original]  
  <sub>anchor: "we show that this approach goes beyond ecommerce transactions and provides a robust feature engineering over different datasets, hyperparameters and classifiers"</sub>

## Introduction

- **descriptive / context**: Bolton and Hand (2001) showed the need for attributes describing transaction history when using unsupervised peer group analysis. (p. 2)[^original]  
  <sub>anchor: "Bolton and Hand (2001) showed the necessity to use attributes describing the history of the transaction"</sub>
- **descriptive / definition**: Whitrow et al. (2008) create descriptive statistics, such as the number of transactions or total amount spent by a cardholder in the past 24 hours for a merchant category or country, as historical features. (p. 2)[^original]  
  <sub>anchor: "These descriptive features can be for example the number of transactions or the total amount spent by the card-holder in the past 24 hours"</sub>
- **descriptive / context**: Bahnsen et al. (2016) considered the Whitrow et al. (2008) strategy to represent the state of the art feature engineering technique for credit card fraud detection. (p. 2)[^original]  
  <sub>anchor: "Bahnsen et al. (2016) considered Whitrow et al. (2008) strategy to epitomized the state of the art feature engineering technique"</sub>
- **descriptive / finding or result**: First weakness identified: aggregated descriptive statistics ignore fine-grained temporal dependencies between transactions, e.g. a fraud pattern of small test transactions followed by large ones. (p. 2)[^original]  
  <sub>anchor: "Such aggregated features do not consider fine-grained temporal dependencies between the transactions."</sub>
- **descriptive / finding or result**: Second weakness identified: fixed time windows (e.g. 24 h) do not match the varying transaction frequencies of different cardholders. (p. 2)[^original]  
  <sub>anchor: "Fixed size aggregated statistics can’t account for that fact."</sub>
- **descriptive / finding or result**: Third weakness identified: aggregated features use only cardholder history and do not exploit fraudulent transactions or terminal sequences. (p. 2)[^original]  
  <sub>anchor: "these features consider only the history of the card-holder and do not exploit information of fraudulent transactions for feature engineering"</sub>
- **descriptive / method**: The authors propose generating history-based features with Hidden Markov Models that quantify similarity between an observed sequence and past fraudulent or genuine sequences of cardholders or terminals. (p. 2)[^original]  
  <sub>anchor: "They quantify the similarity between an observed sequence and the sequences of past fraudulent or genuine transactions observed for the cardholders or the terminals."</sub>
- **descriptive / context**: The introduction notes that the feature set describing a credit card transaction usually ignores detailed sequential information. (p. 2)[^original]  
  <sub>anchor: "the feature set describing a credit card transaction usually ignores detailed sequential information"</sub>
- **descriptive / context**: The introduction states that typical models use only raw transactional features such as time, amount and merchant category, citing Donato et al. (1999). (p. 2)[^original]  
  <sub>anchor: "Typical models only use raw transactional features, such as time, amount, merchant category, etc"</sub>
- **descriptive / method**: The genuine-only perspective is framed as a classic anomaly detection scheme, measuring a new sequence's likelihood against historical honest sequences. (p. 3)[^original]  
  <sub>anchor: "This is a classic anomaly detection scheme where the likelihood of a new sequence of transactions is measured against historical honest sequences of transactions"</sub>
- **descriptive / method**: The other four features use sequences containing at least one fraudulent transaction, intended to reduce false positives since a risky sequence should also be relatively close to risky behaviour. (p. 3)[^original]  
  <sub>anchor: "it is also expected for it to be relatively close to a risky behavior. Thus, these last features should decrease the number of false positive."</sub>
- **descriptive / context**: Investigators can only verify a limited number of alerts each day, so false positives are a crucial issue, as stated by Pozzolo et al. (2017). (p. 3)[^original]  
  <sub>anchor: "this is a crucial issue since the investigators can only verify a limited number of alerts each day"</sub>
- **descriptive / data or feature**: The study uses a real-world credit card transaction dataset provided and labelled by a large European card processing company. (p. 3)[^original]  
  <sub>anchor: "By using a real world credit card transactions dataset provided and labeled by a large European card processing company"</sub>
- **descriptive / method**: Performance is measured by the Precision-Recall AUC metric, comparing Random Forest classifiers with and without the HMM-based features. (p. 3)[^original]  
  <sub>anchor: "we use the Precision-Recall AUC metric. We fed Random Forest classifiers with transactional data"</sub>
- **descriptive / context**: The paper extends a earlier poster by Lucas et al. (2019) with additional experiments, showing gains for face-to-face as well as e-commerce transactions. (p. 3)[^original]  
  <sub>anchor: "the framework is shown to increase the detection of fraudulent transactions not only for e-commerce transactions but also for face-to-face transactions"</sub>
- **descriptive / context**: Prior work on the same dataset by Jurgovsky et al. (2018) found that a detection gain on one transaction type did not extend to all types. (p. 3)[^original]  
  <sub>anchor: "showed that some increase in detection observed on one type of transactions couldn’t be extended to all types of transactions"</sub>
- **descriptive / finding or result**: The feature engineering is reported as relevant for random forest, logistic regression and AdaBoost classifiers and robust to the number of hidden states and sequence length. (p. 3)[^original]  
  <sub>anchor: "the feature engineering strategy is shown to be relevant for various types of classifiers (random forest, logistic regression and Adaboost)"</sub>
- **descriptive / limitation**: A structural missing value limitation: HMM-based features cannot be computed for some users with few transactions, leaving 20% to 40% of transactions without them depending on sequence length. (p. 4)[^original]  
  <sub>anchor: "From 20% to 40% of the transactions (depending on the choice of the length of the sequences modeled by the HMM) are not associated with HMM-based features."</sub>
- **descriptive / finding or result**: After comparing several solutions, the authors report a steady improvement of detection over all transactions of the dataset. (p. 4)[^original]  
  <sub>anchor: "we were able to obtain a steady improvement of the detection over all the transactions of the dataset"</sub>
- **descriptive / context**: The paper's sections cover related work, the HMM feature construction, the experimental protocol, face-to-face and e-commerce results, a hyperparameter study, and structural missing value strategies. (p. 4)[^original]  
  <sub>anchor: "Finally, in section 5 we compare different solutions to tackle the issue of structural missing values."</sub>

## 1.1 Credit card fraud detection

- **descriptive / context**: Maes et al. (2002) evaluated artificial neural networks and Bayesian belief networks with ROC AUC on Europay International's dataset. (p. 4)[^original]  
  <sub>anchor: "(Maes et al., 2002) evaluated Artificial Neural Network and Bayesian belief network with ROC AUC on Europay International’s dataset."</sub>
- **descriptive / context**: Bhattacharyya et al. (2011) compared SVM, Random Forest and logistic regression on a real-world dataset using many metrics. (p. 4)[^original]  
  <sub>anchor: "(Bhattacharyya et al., 2011) compared Support Vector Machine, Random Forest and logistic regression on a real world dataset"</sub>
- **descriptive / context**: Bahnsen et al. (2013) adjusted Bayes Minimum Risk using real financial costs for Random Forest and linear regression classifiers. (p. 4)[^original]  
  <sub>anchor: "(Bahnsen et al., 2013) adjusted Bayes Minimum Risk using real financial costs"</sub>
- **descriptive / context**: Pozzolo et al. (2014) tested an architecture handling temporal concept drift in a transaction stream with Random Forest, SVM and neural networks. (p. 4)[^original]  
  <sub>anchor: "tested an architecture to take into account temporal concept drift in the credit card transaction data stream"</sub>
- **descriptive / context**: Mahmoudi and Duman (2015) applied a modified Fisher discriminant function to account for the higher false negative cost. (p. 5)[^original]  
  <sub>anchor: "applied a modified Fisher discriminant func- tion to take into account the higher false negative cost"</sub>
- **descriptive / finding or result**: Jurgovsky et al. (2018) found LSTM improves fraud detection over Random Forest with aggregated features for face-to-face transactions only. (p. 5)[^original]  
  <sub>anchor: "They showed that, in the case of face-to-face transactions only, sequence modelling with Long Short Term Memory networks (LSTM) improves fraud detection"</sub>
- **descriptive / method**: Random Forest is chosen because it performed well in prior literature and preliminary experiments; feature importance is the decrease of Gini impurity at a node weighted by the proportion of data reaching it. (p. 5)[^original]  
  <sub>anchor: "Random Forests offer the possibility to calculate the importance of a feature which is defined as the decrease of gini impurity"</sub>
- **descriptive / context**: Some authors used only raw features for fraud detection, e.g. Mahmoudi and Duman (2015) and Minegishi and Niimi (2011). (p. 5)[^original]  
  <sub>anchor: "Some authors used only raw features in order to detect fraudulent transactions"</sub>
- **descriptive / method**: Saia and Carta (2019) applied Fourier and wavelet transforms to move transactions into a frequency domain before machine learning, raising outliers from a different view. (p. 5)[^original]  
  <sub>anchor: "Saia and Carta (2019) used Fourier and wavelet transforms in order to move the transaction in a new domain"</sub>
- **descriptive / finding or result**: Whitrow et al. (2008) reported a 28% increase in detection of fraudulent transactions using aggregated features with Random Forest. (p. 6)[^original]  
  <sub>anchor: "They showed a 28% increase in the detection of fraudulent transactions by using these aggregated features with a Random Forest"</sub>
- **descriptive / context**: Jha et al. (2012) applied Whitrow's aggregation strategy to logistic regression on a real-world dataset. (p. 6)[^original]  
  <sub>anchor: "(Jha et al., 2012) applied Whitrow’s transaction aggregation strategy to logistic regression"</sub>
- **descriptive / method**: Krivko (2010) proposed a rule-based approach comparing recent spending with the cardholder's average or the average across all cardholders. (p. 6)[^original]  
  <sub>anchor: "presented a rule-based approach using the difference between the recent amount spent by the card holder"</sub>
- **descriptive / finding or result**: Bahnsen et al. (2016) reported that adding time-of-transaction periodic features to Whitrow's features raises savings by an average of 13% across Random Forest, logistic regression and Bayes minimum risk models. (p. 6)[^original]  
  <sub>anchor: "increases the savings by an average of 13% with Random Forest, Logistic Regression and Bayes minimum Risk model"</sub>
- **descriptive / method**: Vlasselaer et al. (2015) built network-based features counting transactions between cardholders and terminals to produce a time-dependent suspiciousness score. (p. 6)[^original]  
  <sub>anchor: "It consists in using the numbers of transactions between card holders and terminals in the graph of the transactions"</sub>
- **descriptive / finding or result**: Vlasselaer et al. (2015) reported a 3.4% increase in ROC AUC when adding network-based features to Whitrow's features with Random Forests. (p. 6)[^original]  
  <sub>anchor: "They showed a 3.4% increase of the ROC AUC by using these network-based features"</sub>
- **descriptive / context**: The authors use Whitrow's cardholder-centric aggregated features as the state of the art baseline for comparison. (p. 6)[^original]  
  <sub>anchor: "we consider Whitrow’s cardholder centric aggregated features as the state of the art baseline for comparison"</sub>

## 1.2 Sequence Classification

- **descriptive / context**: Dietterich (2002) reviewed sequential classification based on sliding windows, which do not capture inner dependencies between consecutive events. (p. 6)[^original]  
  <sub>anchor: "However, sliding windows methods don’t take into account inner dependencies between consecutive events."</sub>
- **descriptive / method**: Srivastava et al. (2008) used multinomial HMMs on an artificial dataset, with hidden states tied to purchase types and observations of big, medium or small amount, comparing sequence likelihood to a threshold. (p. 7)[^original]  
  <sub>anchor: "In their multinomial HMMs, the transactions were characterized with a symbol (’big amount’, ’medium amount’, ’small amount’)"</sub>
- **descriptive / finding or result**: Graves (2012) observed LSTMs outperform HMMs on speech and handwriting recognition by learning long-term dependencies. (p. 7)[^original]  
  <sub>anchor: "Graves (2012) observed that Long Short Term Memory networks are better than other sequential algorithms such as HMMs"</sub>
- **descriptive / finding or result**: Wiese and Omlin (2009) found LSTMs relevant for card fraud because they model time series of differing length per cardholder. (p. 7)[^original]  
  <sub>anchor: "Wiese and Omlin (2009) compared feed forward neural network combined with Support Vector Machines and LSTM"</sub>
- **descriptive / finding or result**: Jurgovsky et al. (2018) found LSTM gives a small improvement over Random Forest for face-to-face transactions and no improvement for e-commerce transactions. (p. 7)[^original]  
  <sub>anchor: "LSTM offers a small improvemnt over Random Forest in the case of face-to-face transactions. There is no improvement for e-commerce transactions."</sub>

## 2 Multiple perspectives Hidden Markov Model based feature engineering

- **descriptive / limitation**: Existing descriptive features ignore the seller's history and do not model dependencies between transactions in a sequence, and the aggregation choice relies on expert knowledge. (p. 7)[^original]  
  <sub>anchor: "First, they do not take into account the history of the seller even if it is clearly identified in most credit card transactions dataset."</sub>
- **descriptive / method**: The authors chose HMMs, generative probabilistic models common for sequence modelling, to reduce dependence on expert knowledge and favour automated supervised feature engineering. (p. 7)[^original]  
  <sub>anchor: "In order not to depend on expert knowledge, we favor automated feature engineering in a supervised context."</sub>
- **descriptive / method**: Eight new HMM-based features are proposed in addition to Whitrow's descriptive features, each quantifying similarity between a transaction's history and one of eight distributions learned on supervised sequence sets. (p. 7)[^original]  
  <sub>anchor: "we propose to create eight new HMM-based features. They quantify the similarity between the history of a transaction and eight distributions"</sub>
- **descriptive / definition**: The three binary perspectives are genuine versus fraudulent history, cardholder versus terminal, and amount versus time-delta, giving eight (2 cubed) HMMs. (p. 7)[^original]  
  <sub>anchor: "therefore learn eight (23 ) different HMMs"</sub>
- **descriptive / method**: Eight HMM parameter sets are optimised using all eight perspective combinations, so that the 8 features cover genuineness and fraudulence of both terminal and cardholder histories. (p. 7)[^original]  
  <sub>anchor: "At the end the set of 8 HMM-based features will provide information about the genuineness and the fraudulence of both terminal and card holder histories."</sub>
- **descriptive / method**: Four training datasets are created: genuine cardholder sequences, compromised cardholder sequences (at least one fraud), genuine terminal sequences, and compromised terminal sequences. (p. 8)[^original]  
  <sub>anchor: "sequences of transactions from compromised credit cards (with at least one fraudulent transaction)"</sub>
- **descriptive / data or feature**: The observed HMM variable is either the transaction amount or the time-delta between consecutive transactions of a cardholder. (p. 8)[^original]  
  <sub>anchor: "the amount of time elapsed between two consecutive transactions of a card-holder (time-delta)."</sub>
- **descriptive / context**: The HMM main hypothesis is that the observed distribution is generated by a simpler latent model, with complexity partly due to additive Gaussian noise in state evolution and emission. (p. 9)[^original]  
  <sub>anchor: "Hidden Markov Models main hypothesis is that behind the observed distribution, there is a simpler latent model"</sub>
- **descriptive / definition**: The transition matrix gives, for each hidden state, a multinomial distribution over the next state; hidden states satisfy the Markov property. (p. 9)[^original]  
  <sub>anchor: "Each row i of the transition matrix is a multinomial distribution of the next state given that the current state is i"</sub>
- **descriptive / definition**: The emission matrix gives the conditional distribution of observed variables given the hidden state; it is multinomial for categorical and Gaussian for continuous variables. (p. 9)[^original]  
  <sub>anchor: "Usually, the distribution is considered multinomial for categorical observed variables or gaussian for continuous observed variables."</sub>
- **descriptive / method**: Transition and emission matrices are optimised with the iterative Baum-Welch expectation-maximisation algorithm, repeated until convergence of the likelihood. (p. 9)[^original]  
  <sub>anchor: "The transition and emission conditional probability matrices of the HMMs are optimized by an iterative Expectation-Maximisation algorithm known as the Baum-Welch algorithm"</sub>
- **descriptive / finding or result**: Training likelihood increases over iterations until it reaches a ceiling set by the model's hyperparameters. (p. 10)[^original]  
  <sub>anchor: "This likelihood increases over the iterations until it reaches a ceiling"</sub>
- **descriptive / finding or result**: The procedure yields 8 trained HMMs covering four behaviour types (genuine and fraudulent terminal, genuine and fraudulent cardholder) for both amount and time-delta observations. (p. 10)[^original]  
  <sub>anchor: "At the end, we obtain 8 trained HMMs modeling 4 types of behaviour"</sub>
- **descriptive / method**: Online algorithm: for each transaction and each perspective combination, the sequence of the current and two previous transactions is scored by the HMM and an anomaly score is the log-likelihood. (p. 10)[^original]  
  <sub>anchor: "AnomalyScore ← log_ ( _P_ ([ _txi, txi−_ 1 _, txi−_ 2] _|HMMj_ ))"</sub>
- **descriptive / method**: HMM features are likelihoods that the current transaction plus the two previous ones from the terminal or cardholder are generated by each model; the Viterbi algorithm computes the most probable hidden state sequence. (p. 11)[^original]  
  <sub>anchor: "The HMM-based features proposed in this paper (table 1) are the likelihoods that a sequence made of the current transaction and the two previous ones"</sub>
- **descriptive / data or feature**: Table 1 maps the 8 features: for cardholders, amount and time-delta features under genuine (HMM1, HMM2) and fraudulent (HMM5, HMM6) sequences; for terminals, amount (HMM3, HMM7) and time-delta (HMM4, HMM8) under genuine and fraudulent sequences. (p. 11)[^original]  
  <sub>anchor: "Set of 8 HMM-based features describing 8 combinations of perspectives"</sub>

---

[source overview](overview.md) | [next part](digest-002.md)

[^original]: arXiv, "Towards automated feature engineering for credit card fraud detection using multi-perspective HMMs" (2019-03-09). https://arxiv.org/abs/1909.01185
