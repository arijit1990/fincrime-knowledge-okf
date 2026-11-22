---
type: Source Digest
title: Towards automated feature engineering for credit card fraud detection using multi-perspective HMMs - part 3 of 3 (pp. 18-24)
description: 'Verified paraphrased digest, pp. 18-24: 5 Handling the missing value limitations; Conclusion; Conclusion > 5.1 Acknowledgement:; and 1 more sections'
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
part: 3
parts_total: 3
content_mode: digest
generated:
  by: claude-code-subagent/claude-sonnet-5-5
  at: '2026-11-22T14:40:35Z'
verified:
- by: process:kb-digest-check/anchor-match
  at: '2026-11-22T14:40:35Z'
- by: claude-code-judge-agent/claude-opus-5-5
  at: '2026-11-22T14:40:35Z'
sources:
- id: original
  resource: https://arxiv.org/abs/1909.01185
  title: Towards automated feature engineering for credit card fraud detection using multi-perspective HMMs
  author: org:arxiv
  last_modified: '2019-03-09T00:00:00Z'
digest_points: 23
---

# Towards automated feature engineering for credit card fraud detection using multi-perspective HMMs (digest)

[previous part](digest-002.md) | [source overview](overview.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (pp. 18-24) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **academic finding**.

## 5 Handling the missing value limitations

- **descriptive / finding or result**: Because the transaction history was sometimes too short to compute HMM-based features, about 20% of transactions were dismissed for the experiments in section 4.1 and around 40% for the hyperparameter experiments in section 4.3. (p. 18)[^original]  
  <sub>anchor: "we had to dismiss about 20% of the transactions for the experiments described in section 4.1"</sub>
- **descriptive / context**: The authors state there is a strong need to handle structural missing values that depend on the length of user sequences, so that transactions with short history can be integrated. (p. 18)[^original]  
  <sub>anchor: "There is a strong need to tackle the issue of structural missing values depending on the length of users sequences"</sub>
- **descriptive / data or feature**: The authors consider 9 sets of HMM-based features obtained with window sizes of 3, 5 and 7 for either the card-holder or the terminal, giving 16 sets of transactions with different history constraints (terminal history and card-holder history each in [0, 3, 5, 7]). (p. 18)[^original]  
  <sub>anchor: "We therefore have 16 sets of transactions with different history constraints"</sub>
- **descriptive / data or feature**: Table 8 reports, for e-commerce, 5.4e6 transactions with 18472 frauds in total, 4.5e6 with 15650 frauds for history of at least 3, and 3.4e6 with 12493 frauds for history of at least 7; for face-to-face, 6.8e6 transactions with 2764 frauds in total, 5.3e6 with 1305 frauds for history at least 3, and 4.1e6 with 859 frauds for history at least 7. (p. 18)[^original]  
  <sub>anchor: "History >_= 7|3_._4_∗_106|12493|4_._1_∗_106|859|"</sub>
- **descriptive / definition**: A history constraint of at least 3 means every transaction has at least 2 past transactions for the card-holder and for the terminal, so sequences of 3 transactions can be built for both perspectives. (p. 18)[^original]  
  <sub>anchor: "History >_= 3 means that all the transactions have at least 2 transactions in the past for the card-holder and for the terminal"</sub>
- **descriptive / method**: The default0 strategy replaces HMM-based features that could not be calculated for a transaction with the value 0. (p. 19)[^original]  
  <sub>anchor: "the HMM-based features that couldn’t have been calculated for the current transactions are replaced by 0."</sub>
- **descriptive / method**: The weighted PR strategy computes a weighted sum of predictions from 16 Random Forests, each trained on one history constraint, weighting each forest by its PR AUC on the validation set; for example a transaction with terminal history 6 and card-holder history 3 uses the forests [0,0], [0,3], [3,0], [3,3], [5,0] and [5,3]. (p. 19)[^original]  
  <sub>anchor: "Each Random Forest is weighted by it’s efficiency on the validation set."</sub>
- **descriptive / method**: The stacked RF strategy trains a Random Forest classifier on the predictions of the 16 constraint-specialised Random Forests, using 0 as the prediction when a transaction does not satisfy a forest's constraints; the authors note it could stack individual classifiers into a more accurate one. (p. 19)[^original]  
  <sub>anchor: "This approach has the second benefit that we might stack indivual classifiers thereby creating a more accurate new one."</sub>
- **descriptive / context**: The authors did not generate missing values by modelling feature distributions, because the values are missing due to insufficient historical information, and they judged replacing HMM-based features with another model (kNN or Random Forest) inappropriate. (p. 19)[^original]  
  <sub>anchor: "We thought that replacing the value of a model based feature"</sub>
- **descriptive / finding or result**: Table 9 reports whole-test-set PR-AUC: raw features without HMM-based features gave 0.264 for e-commerce and 0.058 for face-to-face; default0 gave 0.320 and 0.145; weighted PR gave 0.275 and 0.040; stacked RF gave 0.317 and 0.133. (p. 20)[^original]  
  <sub>anchor: "raw (no HMM-based features)_|0_._264_±_0_._002|0_._058_±_0_._012|"</sub>
- **descriptive / finding or result**: The simplest strategy, default0, gave the best PR-AUCs with the best stability for both face-to-face and e-commerce transactions, and it is by far the fastest because it trains one Random Forest instead of 16 (weighted PR) or 17 (stacked RF). (p. 20)[^original]  
  <sub>anchor: "We can observe in table 9 that the simplest solution ( _default0_ ) allows for the best PR-AUCs"</sub>
- **descriptive / finding or result**: The weighted PR solution did not yield satisfying results, whereas the stacked RF solution gave good PR-AUCs and useful properties for combining different classifier types. (p. 20)[^original]  
  <sub>anchor: "The _weighted PR_ solution doesn’t allow for satisfying results."</sub>
- **descriptive / finding or result**: The authors claim that handling transactions with structural missing values greatly widens the framework's range of application, and that HMM-based features with small (large) window sizes characterise short (long) term history. (p. 20)[^original]  
  <sub>anchor: "Finding satisfying solutions to integrate transactions with structural missing value increases drastically the range of application"</sub>

## Conclusion

- **descriptive / context**: The HMM-based feature engineering strategy incorporates sequential knowledge into transactions as features, enabling a non-sequential Random Forest classifier to use sequential information. (p. 20)[^original]  
  <sub>anchor: "These HMM-based features enable a non sequential classifier (Random Forest) to use sequential information"</sub>
- **descriptive / method**: The approach models genuine and fraudulent behaviour of merchants and card-holders using two features, timing and amount of transactions, and the HMM-based features are created in a supervised way, lowering the need for expert knowledge. (p. 20)[^original]  
  <sub>anchor: "we model the genuine and fraudulent behaviours of the merchants and the card-holders according to two features: the timing and the amount of the transactions"</sub>
- **descriptive / finding or result**: The authors state the terminal perspective is usually not used in credit card fraud detection and show it greatly helps detection for face-to-face and e-commerce transactions. (p. 20)[^original]  
  <sub>anchor: "The terminal perspective is usually not used in credit card fraud detection and is shown in this paper"</sub>
- **descriptive / finding or result**: The extension to Lucas et al. (2019) reports an increase in precision-recall AUC of 18.1% for face-to-face transactions and 9.3% for e-commerce transactions. (p. 21)[^original]  
  <sub>anchor: "the results show an increase in the precision-recall AUC of 18.1% for the face-to-face transactions and 9.3% for the e-commerce ones."</sub>
- **descriptive / finding or result**: The feature engineering strategy is reported to be relevant across random forest, logistic regression and Adaboost classifiers and robust to hyperparameter choices used to construct the features. (p. 21)[^original]  
  <sub>anchor: "the feature engineering strategy is shown to be relevant for various types of classifiers (random forest, logistic regression and Adaboost)"</sub>
- **descriptive / finding or result**: Several solutions to the structural missing values limitation of the framework were benchmarked. (p. 21)[^original]  
  <sub>anchor: "the structural missing values limitation of the framework is looked at and several solutions are benchmarked."</sub>
- **permissive / context**: The authors suggest similar HMM-based features could be built in any supervised task involving a sequential dataset. (p. 21)[^original]  
  <sub>anchor: "We can imagine building similar HMM-based features in any supervised task that involve a sequential dataset."</sub>
- **descriptive / context**: Source code for calculating and evaluating the HMM-based features is made available for reproducibility. (p. 21)[^original]  
  <sub>anchor: "a source code for calculating and evaluating the proposed HMM-based features can be found"</sub>
- **recommended / recommendation**: As future work, the authors suggest combining predictions of an LSTM with an HMM-based-features-enhanced Random Forest, since Jurgovsky et al. (2018) showed these classifiers do not detect the same frauds in face-to-face transactions. (p. 21)[^original]  
  <sub>anchor: "it would be interesting to combine the predictions of an LSTM with the prediction of some HMM-based features enhanced Random Forest"</sub>

## 5.1 Acknowledgement

- **descriptive / context**: The work was partially funded by the Bavarian Ministry of Economic Affairs, Regional Development and Energy, in the project Internetkompetenzzentrum Ostbayern. (p. 21)[^original]  
  <sub>anchor: "The work has been funded partially by the Bavarian Ministry of Economic Affairs, Regional Development and Energy"</sub>

---

[previous part](digest-002.md) | [source overview](overview.md)

[^original]: arXiv, "Towards automated feature engineering for credit card fraud detection using multi-perspective HMMs" (2019-03-09). https://arxiv.org/abs/1909.01185
