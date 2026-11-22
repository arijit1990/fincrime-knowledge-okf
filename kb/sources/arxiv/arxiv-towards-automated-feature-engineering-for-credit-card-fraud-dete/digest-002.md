---
type: Source Digest
title: Towards automated feature engineering for credit card fraud detection using multi-perspective HMMs - part 2 of 3 (pp. 11-18)
description: 'Verified paraphrased digest, pp. 11-18: 3 Experimental Setup > 3.1 Dataset Description; 3 Experimental Setup > 3.2 Feature Engineering and Dataset Partitioning; 4 Results > 4.1 Improvement in fraud detection when using HMM-based features; and 2 more sections'
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
part: 2
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
digest_points: 64
---

# Towards automated feature engineering for credit card fraud detection using multi-perspective HMMs (digest)

[previous part](digest-001.md) | [source overview](overview.md) | [next part](digest-003.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (pp. 11-18) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **academic finding**.

## 3.1 Dataset Description

- **descriptive / data or feature**: The dataset was provided by an industrial partner and contains anonymized transactions of all Belgian credit cards between 01.03.2015 and 31.05.2015, used to quantify the detection gain from HMM-based features. (p. 11)[^original]  
  <sub>anchor: "This dataset contains the anonymized transactions from all the belgian credit cards between 01.03.2015 and 31.05.2015."</sub>
- **descriptive / definition**: The classification task is to predict whether each transaction is genuine or fraudulent. (p. 11)[^original]  
  <sub>anchor: "The classification task is to predict the class of the transactions (genuine or fraudulent)."</sub>
- **descriptive / data or feature**: Transactions are described by continuous, categorical and binary features characterising the card-holder, the transaction and the terminal. (p. 11)[^original]  
  <sub>anchor: "Transactions are represented by vectors of continuous, categorical and binary features that characterize the card-holder, the transaction and the terminal."</sub>
- **descriptive / data or feature**: Card-holder features include a unique card-holder ID, age, gender and similar attributes; terminal features include a unique terminal ID, merchant category code and country. (p. 11)[^original]  
  <sub>anchor: "The terminal is characterized by a unique terminal-ID, a merchant category code, a country."</sub>
- **descriptive / context**: Face-to-face transactions differ from e-commerce transactions; for example, merchants are usually closed at night and PIN authentication significantly reduces the number of fraudulent transactions. (p. 11)[^original]  
  <sub>anchor: "The merchant is usually closed at night, the necessity of a PIN authentication decreases significantly the number of fraudulent transactions"</sub>
- **descriptive / finding or result**: Jurgovsky et al. (2018) reported on the same Belgian dataset that LSTM approaches performed better on face-to-face than on e-commerce transactions. (p. 11)[^original]  
  <sub>anchor: "some machine learning approaches (LSTM) gave better results on faceto-face transactions than on e-commerce transactions."</sub>

## 3.2 Feature Engineering and Dataset Partitioning

- **descriptive / method**: Terminal-centred aggregated features were computed in addition to the card-holder-centred aggregated features of Whitrow et al. (2008), so that HMM-based and aggregated features are comparable. (p. 11)[^original]  
  <sub>anchor: "we calculate terminal-centered aggregated features in addition to (Whitrow et al., 2008) card-holder centered aggregated features"</sub>
- **descriptive / data or feature**: AGGCH1 counts transactions issued by the user in 24h and AGGCH2 gives the amount spent by the user in 24h. (p. 11)[^original]  
  <sub>anchor: "AGGCH1|# transactions issued by user in 24h."</sub>
- **descriptive / data or feature**: AGGCH3 counts transactions in the country in 24h and AGGCH4 gives the amount spent in the country in 24h. (p. 11)[^original]  
  <sub>anchor: "AGGCH3|# transactions in the country in 24h."</sub>
- **descriptive / data or feature**: AGGTM1 counts transactions in the terminal in 24h and AGGTM2 gives the amount spent in the terminal in 24h. (p. 11)[^original]  
  <sub>anchor: "AGGTM1|# transactions in terminal in 24h."</sub>
- **descriptive / data or feature**: AGGTM3 counts transactions with this card type in 24h and AGGTM4 gives the amount spent with this card type in 24h. (p. 11)[^original]  
  <sub>anchor: "AGGTM3|# transactions with this card type in 24h."</sub>
- **descriptive / method**: The data were split temporally into training, validation and testing sets, with a 7-day gap before the testing set to reflect that ground truth is delayed by about one week while investigators verify alerts. (p. 11)[^original]  
  <sub>anchor: "We chose to separate the time period corresponding to the training and validation set and the time period corresponding to the testing set with a gap of 7 days."</sub>
- **descriptive / method**: Transactions in the gap period are used to compute aggregated and HMM-based features for the testing set but not to train the classifiers. (p. 12)[^original]  
  <sub>anchor: "The transactions appearing during this gap of 7 days before the testing set are used in order to calculate the value"</sub>
- **descriptive / data or feature**: The training set covers 01.03.2015 to 26.04.2015, the validation set (used to tune the random forests) covers 27.04.2015 to 30.04.2015, and the testing set covers 08.05.2015 to 31.05.2015. (p. 12)[^original]  
  <sub>anchor: "the training set contains all the transactions between 01.03.2015 to 26.04.2015, the validation set used for the tuning"</sub>

## 4.1 Improvement in fraud detection when using HMM-based features

- **descriptive / context**: The AUC difference between e-commerce and face-to-face transactions is attributed to class imbalance, which is 17 times stronger for face-to-face transactions. (p. 12)[^original]  
  <sub>anchor: "the imbalancy is 17 times stronger for the face-to-face transactions than for the e-commerce transactions."</sub>
- **descriptive / data or feature**: Fraud rates are 0.2 frauds per 1000 transactions for face-to-face and 3.7 frauds per 1000 transactions for e-commerce. (p. 12)[^original]  
  <sub>anchor: "For face-to-face, there are 0.2 frauds per 1000 transactions whereas for e-commerce there are 3.7 frauds per 1000"</sub>
- **descriptive / finding or result**: On e-commerce transactions, raw features alone gave PR-AUC 0.212 ± 0.009 without HMM features and 0.298 ± 0.0006 with HMM features, an increase of 40.5%. (p. 12)[^original]  
  <sub>anchor: "0.212 _±_ 0.009|HMM-features0.298 _±_ 0.0006|increase through HMMs40.5%"</sub>
- **descriptive / finding or result**: On e-commerce transactions, raw+aggCH gave PR-AUC 0.343 ± 0.001 without and 0.375 ± 0.0006 with HMM features, an increase of 9.3%. (p. 12)[^original]  
  <sub>anchor: "raw+aggCH|0.343 _±_ 0.001|0.375 _±_ 0.0006|9.3%|"</sub>
- **descriptive / finding or result**: On e-commerce transactions, raw+all agg gave PR-AUC 0.383 ± 0.002 without and 0.397 ± 0.003 with HMM features, an increase of 3.6%. (p. 12)[^original]  
  <sub>anchor: "raw+all agg|0.383 _±_ 0.002|0.397 _±_ 0.003|3.6%|"</sub>
- **descriptive / definition**: raw+aggCH is treated as the state-of-the-art feature engineering strategy, containing raw features plus Whitrow's aggregated features. (p. 13)[^original]  
  <sub>anchor: "We refer to the feature set raw+aggCH as the state of the art feature engineering strategy"</sub>
- **descriptive / method**: The main experiments used HMMs with 5 hidden states and HMM-based features with a window size of 3 (the transaction plus 2 past transactions of the card-holder and terminal). (p. 13)[^original]  
  <sub>anchor: "the HMMs were created with 5 hidden states and the HMM-based features were calculated with a window-size of 3"</sub>
- **descriptive / finding or result**: Section 4.3 reports that the HMM hyperparameters (hidden states and window size) did not significantly change the increase in PR-AUC. (p. 13)[^original]  
  <sub>anchor: "did not change significantly the increase in Precision-Recall AUC"</sub>
- **descriptive / finding or result**: On face-to-face transactions, raw features alone gave PR-AUC 0.082 ± 0.001 without and 0.152 ± 0.001 with HMM features, an increase of 85.4%. (p. 13)[^original]  
  <sub>anchor: "0.082 _±_ 0.001|HMM features0.152 _±_ 0.001|increase through HMMs85.4%"</sub>
- **descriptive / finding or result**: On face-to-face transactions, raw+aggCH gave PR-AUC 0.144 ± 0.001 without and 0.170 ± 0.001 with HMM features, an increase of 18.1%. (p. 13)[^original]  
  <sub>anchor: "raw+aggCH|0.144 _±_ 0.001|0.170 _±_ 0.001|18.1%|"</sub>
- **descriptive / finding or result**: On face-to-face transactions, raw+all agg gave PR-AUC 0.167 ± 0.001 without and 0.177 ± 0.0006 with HMM features, an increase of 6.0%. (p. 13)[^original]  
  <sub>anchor: "raw+all agg|0.167 _±_ 0.001|0.177 _±_ 0.0006|6.0%|"</sub>
- **descriptive / method**: Random Forest hyperparameters were tuned by grid search optimising PR-AUC on the validation set, with PR-AUC chosen for imbalanced data following Davis and Goadrich (2006). (p. 13)[^original]  
  <sub>anchor: "We tuned the Random Forest hyperparameters (table 3) through a grid search that optimizes the Precision-Recall Area under the Curve"</sub>
- **descriptive / method**: The Random Forest hyperparameters were tuned by grid search optimising the Precision-Recall AUC on the validation set, following Davis and Goadrich (2006) for the choice of metric (Table 3). (p. 13)[^original]  
  <sub>anchor: "We tuned the Random Forest hyperparameters (table 3) through a grid search that optimizes the Precision-Recall Area under the Curve"</sub>
- **descriptive / method**: Results are averages of 3 runs reported as mean ± standard deviation, and the AUCs were stable across runs with low standard deviations. (p. 14)[^original]  
  <sub>anchor: "The AUC numbers correspond to the average _±_ standard deviation on 3 different runs."</sub>
- **descriptive / finding or result**: Adding sequence descriptors (HMM-based or Whitrow aggregated features) to raw features significantly improved PR-AUC for both face-to-face and e-commerce transactions. (p. 14)[^original]  
  <sub>anchor: "both show a significant improvement in precision-recall AUC when adding sequence descriptors"</sub>
- **descriptive / finding or result**: For e-commerce, improvement ranges from 3.6% for the best feature set without HMM features (raw+all-agg) to 40.5% for the worst (raw). (p. 14)[^original]  
  <sub>anchor: "this improvement ranges from 3.6% for the best feature set without HMM-based features"</sub>
- **descriptive / finding or result**: For face-to-face, improvement ranges from 6.0% for the best feature set without HMM features (raw+all agg) to 85.4% for the worst (raw). (p. 14)[^original]  
  <sub>anchor: "this improvement ranges from 6.0% for the best feature set without HMM-based features"</sub>
- **descriptive / finding or result**: Adding HMM features to raw+aggCH increased PR-AUC by 18.1% for face-to-face and 9.3% for e-commerce transactions. (p. 15)[^original]  
  <sub>anchor: "leads to an increase of 18.1% of the PR-AUC for the face-to-face transactions and to an increase of 9.3%"</sub>
- **descriptive / finding or result**: Adding terminal-centred aggregated features increased PR-AUC by 16.0% for face-to-face transactions. (p. 15)[^original]  
  <sub>anchor: "The relative increase in PR-AUC when adding terminal centered aggregated features to the feature set is of 16.0%"</sub>
- **descriptive / finding or result**: Adding terminal-centred aggregated features increased PR-AUC by 11.7% for e-commerce transactions. (p. 15)[^original]  
  <sub>anchor: "is of 11.7% for the e-commerce transactions."</sub>
- **descriptive / finding or result**: Sequence-based features substantially increase PR-AUC on both channels, and HMM features improve prediction on both and help classifiers reach the best accuracy levels. (p. 15)[^original]  
  <sub>anchor: "The addition of HMM-based features improves the prediction on both e-commerce and face-to-face transactions"</sub>

## 4.2 Robustness over different machine learning algorithms

- **descriptive / method**: To check robustness, the same experiments were repeated with AdaBoost and logistic regression classifiers. (p. 15)[^original]  
  <sub>anchor: "we did the same experiments with adaboost and logistic regression classifier."</sub>
- **descriptive / method**: Gradient boosting (AdaBoost) and logistic regression hyperparameters were tuned by grid search optimising PR-AUC on the validation set. (p. 15)[^original]  
  <sub>anchor: "We tuned the gradient boosting and logistic regression hyperparameters (table 5) through a grid search"</sub>
- **descriptive / finding or result**: The authors conclude the improvement from HMM features over the state-of-the-art aggregation strategy is significant and reliable across classifiers and datasets, with a larger relative improvement for weaker classifiers such as logistic regression. (p. 15)[^original]  
  <sub>anchor: "the improvement observed when integrating the proposed multiple perspectives HMM-based feature engineering"</sub>
- **descriptive / finding or result**: Logistic regression gave a significant decrease in detection efficiency compared with random forest. (p. 16)[^original]  
  <sub>anchor: "We observe a significant decrease in detection efficiency with logistic regression classifier compared to random forest classifier."</sub>
- **descriptive / finding or result**: Logistic regression with raw features gave PR-AUC 0.015 ± 0.0001 without and 0.049 ± 0.001 with HMM features on e-commerce (increase 267%). (p. 16)[^original]  
  <sub>anchor: "raw|0.015 _±_ 0.0001|0.049 _±_ 0.001|267%|"</sub>
- **descriptive / finding or result**: Logistic regression on e-commerce raw+aggCH gave 0.092 ± 0.005 without and 0.121 ± 0.003 with HMM features (increase 31.5%); raw+all agg gave 0.096 ± 0.004 and 0.124 ± 0.005 (increase 29.2%). (p. 16)[^original]  
  <sub>anchor: "raw+aggCH|0.092 _±_ 0.005|0.121 _±_ 0.003|31.5%|"</sub>
- **descriptive / finding or result**: Logistic regression on face-to-face raw features gave PR-AUC 0.0094 ± 0.0001 without and 0.030 ± 0.002 with HMM features (increase 219%). (p. 16)[^original]  
  <sub>anchor: "raw|0.0094 _±_ 0.0001|0.030 _±_ 0.002|219%|"</sub>
- **descriptive / finding or result**: Logistic regression on face-to-face raw+aggCH gave 0.014 ± 0.001 without and 0.0247 ± 0.02 with HMM features (increase 76.4%); raw+all agg gave 0.0161 ± 0.0003 and 0.0315 ± 0.0007 (increase 95.6%). (p. 16)[^original]  
  <sub>anchor: "raw+aggCH|0.014 _±_ 0.001|0.0247 _±_ 0.02|76.4%|"</sub>
- **descriptive / limitation**: Logistic regression is weak with categorical features label-encoded, because label encoding implies an irrelevant order between categories. (p. 16)[^original]  
  <sub>anchor: "Logistic regression classifier is known to be weak to categorical features encoded with a label encoder"</sub>
- **descriptive / finding or result**: The evolution with logistic regression when adding the proposed feature strategy is consistent with that observed with random forest. (p. 16)[^original]  
  <sub>anchor: "the evolution observed when including the proposed feature engineering strategy to logistic regression classifier is consistent"</sub>
- **descriptive / finding or result**: AdaBoost with trees of depth 1, as advised in the literature by Freund and Schapire (1997), gave significantly worse fraud detection than AdaBoost with depth-4 trees. (p. 16)[^original]  
  <sub>anchor: "shallow adaboost classifiers with a tree depth restricted to 1 as adviced in the litterature Freund and Schapire (1997)"</sub>
- **descriptive / limitation**: Deeper AdaBoost trees carry an increased risk of overfitting. (p. 16)[^original]  
  <sub>anchor: "The downside of deeper trees is the increased risk of overfitting of the adaboost classifiers."</sub>
- **permissive / method**: Overfitting in AdaBoost could be monitored by tracking PR-AUC on the validation and training sets across the number of added trees. (p. 16)[^original]  
  <sub>anchor: "Monitoring the number of iterations (tree added) after which the classifier starts to overfit could be done by tracking the PR-AUC"</sub>
- **permissive / context**: The authors state that logistic regression results may be improved by one-hot or frequency encoding, as suggested in other credit card fraud detection work by Pozzolo et al. (2015) and Jurgovsky et al. (2018). (p. 16)[^original]  
  <sub>anchor: "The results obtained with logistic regression classifiers may be improved using one-hot encoding or frequency encoding"</sub>
- **descriptive / finding or result**: AdaBoost e-commerce raw features gave PR-AUC 0.103 ± 0.001 without and 0.163 ± 0.007 with HMM features (increase 58.3%). (p. 17)[^original]  
  <sub>anchor: "raw|0.103 _±_ 0.001|0.163 _±_ 0.007|58.3%|"</sub>
- **descriptive / finding or result**: AdaBoost e-commerce raw+aggCH gave 0.238 ± 0.009 without and 0.247 ± 0.011 with HMM features (increase 3.8%); raw+all agg gave 0.263 ± 0.004 and 0.264 ± 0.006 (increase 0.4%). (p. 17)[^original]  
  <sub>anchor: "raw+aggCH|0.238 _±_ 0.009|0.247 _±_ 0.011|3.8%|"</sub>
- **descriptive / finding or result**: AdaBoost face-to-face raw features gave PR-AUC 0.034 ± 0.003 without and 0.058 ± 0.009 with HMM features (increase 70.6%). (p. 17)[^original]  
  <sub>anchor: "raw|0.034 _±_ 0.003|0.058 _±_ 0.009|70.6%|"</sub>
- **descriptive / finding or result**: AdaBoost face-to-face raw+aggCH gave 0.048 ± 0.002 without and 0.079 ± 0.006 with HMM features (increase 64.6%); raw+all agg gave 0.053 ± 0.003 and 0.061 ± 0.004 (increase 15.1%). (p. 17)[^original]  
  <sub>anchor: "raw+aggCH|0.048 _±_ 0.002|0.079 _±_ 0.006|64.6%|"</sub>
- **descriptive / method**: Because of AdaBoost's design, PR-AUC on the training set should rise with each added tree, whereas on the validation set it would fall once the classifier overfits. (p. 17)[^original]  
  <sub>anchor: "the PR-AUC on the training set should increase for each tree added"</sub>

## 4.3 Robustness to hyperparameters changes

- **descriptive / method**: Nine sets of HMM-based features were built with different combinations of number of hidden states and sequence window size used for the likelihood score, then added to the raw features and tested on the test set. (p. 17)[^original]  
  <sub>anchor: "we constructed 9 sets of HMM-based features with different combinations of the HMM-based features hyperparameters"</sub>
- **descriptive / finding or result**: For e-commerce (Table 6, raw = 0.203 ± 0.005), the combination of window size 3 and 5 hidden states gave the best average PR-AUC of 0.315 ± 0.008 over 3 runs. (p. 17)[^original]  
  <sub>anchor: "We observe that, the combination of parameter _{_ window size: 3, hidden states: 5 _}_ gives the best AUCs on average"</sub>
- **descriptive / finding or result**: Table 6 e-commerce PR-AUCs: hidden states 3 gave 0.280 ± 0.013 (window 3), 0.292 ± 0.015 (window 5), 0.295 ± 0.019 (window 7); hidden states 5 gave 0.315 ± 0.008, 0.310 ± 0.006, 0.297 ± 0.007; hidden states 7 gave 0.307 ± 0.003, 0.307 ± 0.004, 0.296 ± 0.011. (p. 17)[^original]  
  <sub>anchor: "Table 6: PR-AUCs for E-commerce HMM hyperparameters"</sub>
- **descriptive / finding or result**: For face-to-face (Table 7, raw = 0.089 ± 0.011), the best PR-AUC was 0.159 ± 0.020 with 3 hidden states and window size 3; other cells range from 0.123 to 0.150. (p. 17)[^original]  
  <sub>anchor: "Table 7: PR-AUCs for Face-to-face HMM hyperparameters"</sub>
- **descriptive / context**: Window size 3 and 5 hidden states was the combination chosen for the HMM-based features in section 4.1. (p. 17)[^original]  
  <sub>anchor: "A window size of 3 and 5 hidden states was the combination of hyperparameter chosen"</sub>
- **descriptive / limitation**: Standard deviations are too high to confidently say that any one hyperparameter combination is better than all the others. (p. 18)[^original]  
  <sub>anchor: "the standard deviation values ( _±_ ) are too high to confidently say that a hyperparameters"</sub>
- **permissive / recommendation**: In a real-world case, a hyperparameter search can be worthwhile but requires computing several sets of HMM-based features. (p. 18)[^original]  
  <sub>anchor: "In a real world case, doing the hyperparameter search can be worth it but requires to calculate several set of HMM-based features."</sub>
- **descriptive / finding or result**: Overall the HMM-based feature strategy is relatively stable across hyperparameter choices. (p. 18)[^original]  
  <sub>anchor: "Overall we can conclude that the HMM-based feature engineering strategy is relatively stable over the hyperparameters."</sub>
- **descriptive / finding or result**: Adding all nine HMM-based feature sets gave a slight improvement of 13.3% on face-to-face transactions but an 8.5% decrease on e-commerce transactions. (p. 18)[^original]  
  <sub>anchor: "adding all 9 newly calculated HMM-based features sets provided a slight improvement on the face-to-face transactions (13.3%)"</sub>
- **descriptive / context**: The authors suggest different hyperparameter settings may capture different information, with window size viewed as describing short, mid and long-term transaction history. (p. 18)[^original]  
  <sub>anchor: "For example the window-size parameter could be seen as: description of short-term/midterm/long-term history"</sub>

---

[previous part](digest-001.md) | [source overview](overview.md) | [next part](digest-003.md)

[^original]: arXiv, "Towards automated feature engineering for credit card fraud detection using multi-perspective HMMs" (2019-03-09). https://arxiv.org/abs/1909.01185
