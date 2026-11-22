---
type: Source Digest
title: Detecting Mixing Services via Mining Bitcoin Transaction Network With Hybrid Motifs - part 2 of 3 (pp. 6-9)
description: 'Verified paraphrased digest, pp. 6-9: Detecting Mixing Services via Mining Bitcoin Transaction Network with Hybrid Motifs > B. Account Features; Detecting Mixing Services via Mining Bitcoin Transaction Network with Hybrid Motifs > C. Transaction Features; Detecting Mixing Services via Mining Bitcoin Transaction Network with Hybrid Motifs > V. DETECTION MODEL; and 5 more sections'
resource: https://arxiv.org/abs/2001.05233
tags:
- academic_finding
- global_academic
- network_graph
- preprint
- typologies
status: stable
source_id: arxiv-detecting-mixing-services-via-mining-bitcoin-transaction-network
issuer: arxiv
issuer_name: arXiv
jurisdictions:
- GLOBAL_ACADEMIC
tier: 3
instrument_type: preprint
normative_force: academic_finding
publication_date: '2021-01-21'
legal_status: unknown
part: 2
parts_total: 3
content_mode: digest
generated:
  by: claude-code-subagent/claude-sonnet-5-5
  at: '2026-11-22T14:46:04Z'
verified:
- by: process:kb-digest-check/anchor-match
  at: '2026-11-22T14:46:04Z'
- by: claude-code-judge-agent/claude-opus-5-5
  at: '2026-11-22T14:46:04Z'
sources:
- id: original
  resource: https://arxiv.org/abs/2001.05233
  title: Detecting Mixing Services via Mining Bitcoin Transaction Network With Hybrid Motifs
  author: org:arxiv
  last_modified: '2021-01-21T00:00:00Z'
digest_points: 91
---

# Detecting Mixing Services via Mining Bitcoin Transaction Network With Hybrid Motifs (digest)

[previous part](digest-001.md) | [source overview](overview.md) | [next part](digest-003.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (pp. 6-9) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **academic finding**.

## B. Account Features

- **descriptive / finding or result**: Finding 4: there is a large variety among unlabeled addresses in account features because several types of unlabeled addresses exist; differences among labeled addresses are smaller, shown by a relatively low standard deviation. (p. 6)[^original]  
  <sub>anchor: "There exists a large variety among the unlabeled addresses in terms of account features because"</sub>
- **descriptive / finding or result**: Finding 5: for AF6, labeled addresses have output amounts that usually equal their input amounts, while unlabeled addresses keep a positive net income on average. (p. 6)[^original]  
  <sub>anchor: "the amount value of output transactions usually equals to that of input transactions for labeled addresses"</sub>
- **descriptive / finding or result**: Finding 5 interprets this as showing that addresses of mixing services act as intermediaries by sending out what they receive. (p. 6)[^original]  
  <sub>anchor: "addresses belonging to mixing services act like intermediaries by sending out what they have received"</sub>

## C. Transaction Features

- **descriptive / context**: Mixing services may use many intermediary addresses (such as hubs) to split and integrate funds, because direct payouts of approximately equal amounts would reveal the link between senders and recipients. (p. 6)[^original]  
  <sub>anchor: "mixing services may use many addresses acting like"</sub>
- **descriptive / definition**: A transaction cycle is defined as an ordered pair of continuous input and output streams that describes money flowing through an intermediary address. (p. 6)[^original]  
  <sub>anchor: "consisting of an ordered pair of continuous input and output streams"</sub>
- **descriptive / case example**: Fig. 6 shows ten continuous transactions of a Bitcoin Fog address, distributed across three transaction cycles, in each of which the address sent out what it received with an increased balance of 0. (p. 6)[^original]  
  <sub>anchor: "These ten transactions are distributed in three transaction cycles"</sub>
- **descriptive / finding or result**: Many labeled addresses show similar transaction behaviour, which the authors suppose is associated with the nature of being an intermediary. (p. 6)[^original]  
  <sub>anchor: "We observe that many labeled addresses have similar transaction behavior like this"</sub>
- **descriptive / data or feature**: TF1 is the standard deviation of the increased balance in every transaction cycle; the expected increased balance for an intermediary address is 0. (p. 6)[^original]  
  <sub>anchor: "Standard deviation of the increased balance in every transaction cycle"</sub>
- **descriptive / data or feature**: TF2 is the average time interval between the first input transaction and the last output transaction in each cycle, denoted T-bar. (p. 6)[^original]  
  <sub>anchor: "between the first input transaction and the last output transaction in each cycle"</sub>
- **descriptive / data or feature**: TF3 is the average number of addresses that jointly participate as the inputs of a transaction. (p. 6)[^original]  
  <sub>anchor: "Average number of addresses that jointly participate as the inputs of a transaction"</sub>
- **descriptive / data or feature**: TF4 is the average number of addresses that jointly participate as the outputs of a transaction. (p. 6)[^original]  
  <sub>anchor: "Average number of addresses that jointly participate as the outputs of a transaction"</sub>
- **descriptive / data or feature**: TF5 is the total number of unique addresses that jointly participate as the inputs. (p. 6)[^original]  
  <sub>anchor: "Total number of unique addresses that jointly participate as the inputs"</sub>
- **descriptive / data or feature**: TF6 is the total number of unique addresses that jointly participate as the outputs. (p. 6)[^original]  
  <sub>anchor: "Total number of unique addresses that jointly participate as the outputs"</sub>
- **descriptive / finding or result**: The observations on TF1 to TF6 are based on the statistics reported in Table IV. (p. 6)[^original]  
  <sub>anchor: "We obtain some observations based on the statistics of TF1TF6 in Table IV."</sub>
- **descriptive / finding or result**: Finding 6: the average time interval of transaction cycles of mixing services is mostly within 3 hours, per the cumulative proportion curve in Fig. 7, while unlabeled addresses show no such pattern. (p. 7)[^original]  
  <sub>anchor: "the average time interval of transaction cycles of mixing services is mostly within 3 hours"</sub>
- **descriptive / context**: One possible explanation offered is that mixing services are designed to process Bitcoins within a specific time because they are user-oriented. (p. 7)[^original]  
  <sub>anchor: "mixing services are designed to process Bitcoins within a specific time"</sub>
- **descriptive / method**: The time window of motifs is preliminarily set to δ = 3 hours for descriptive statistics and mixing detection. (p. 7)[^original]  
  <sub>anchor: "we preliminarily set δ = 3 hours as the time window of motifs"</sub>
- **descriptive / finding or result**: Finding 7: the TF1 values of mixing-service addresses are closer to 0, meaning their balance over each transaction cycle is close to 0. (p. 7)[^original]  
  <sub>anchor: "The TF1 results of addresses belonging to mixing services are closer to 0"</sub>
- **descriptive / finding or result**: Finding 7: mixing-service addresses have more co-input addresses than co-output addresses, possibly because their coins are obfuscated with coins of other addresses. (p. 7)[^original]  
  <sub>anchor: "these addresses have more co-input addresses than co-output addresses"</sub>
- **descriptive / finding or result**: The co-input versus co-output pattern may be explained by coins of a mixing-service address being often obfuscated with coins of other addresses. (p. 7)[^original]  
  <sub>anchor: "the coins of an address belonging to a mixing service are often obfuscated with coins of other addresses"</sub>

## V. DETECTION MODEL

- **descriptive / context**: The detection task has only a small number of verified labeled mixing-service addresses while the rest are unlabeled, an extreme class imbalance that may hinder supervised classification. (p. 7)[^original]  
  <sub>anchor: "we only access a small number of verified labeled addresses belonging to mixing services while the rest addresses are unlabeled"</sub>
- **descriptive / method**: The authors develop a Positive and Unlabeled (PU) learning model with a two-stage strategy: first select reliable negatives from unlabeled instances, then train a classifier on positives and reliable negatives. (p. 7)[^original]  
  <sub>anchor: "we develop a Positive and Unlabeled (PU) learning model with a two-stage strategy"</sub>
- **descriptive / method**: In stage one, a set of spy instances is sampled from the positive instances using the spy technique from reference [9], with a default sample rate of 15%. (p. 7)[^original]  
  <sub>anchor: "we sample a set of spy instances from the positive instances with a default sample rate 15%"</sub>
- **descriptive / method**: In stage one, the non-spy positive instances are labelled 1, while spy instances and unlabeled instances are labelled -1. (p. 7)[^original]  
  <sub>anchor: "the spy instances as well as the unlabeled instances are set with label -1"</sub>
- **descriptive / method**: Stage one uses logistic regression as the classifier for selecting reliable negative instances. (p. 7)[^original]  
  <sub>anchor: "Here we employ the widely considered logistic regression as the classifier"</sub>
- **descriptive / method**: Unlabeled instances are selected as reliable negatives when their predicted positive probability is lower than a threshold θ chosen from the spy instances' prediction probabilities. (p. 7)[^original]  
  <sub>anchor: "the reliable negative instances are selected out from the unlabeled instances if"</sub>
- **descriptive / method**: The threshold θ is the value that maximises the difference between the cumulative proportion of unlabeled instances and spy instances under a minute increment Δp. (p. 7)[^original]  
  <sub>anchor: "The threshold θ is selected as the value that can maximize the increment difference"</sub>
- **descriptive / method**: The increment Δp used in the threshold computation is set to 0.005 in the model. (p. 7)[^original]  
  <sub>anchor: "∆p = 0.005 in our model"</sub>
- **descriptive / method**: In stage two, different penalty weights are set for positive and reliable negative instances in the loss function, to account for their possible imbalance. (p. 7)[^original]  
  <sub>anchor: "we set different penalty weights for different kinds of instances in the loss function"</sub>
- **descriptive / method**: The stage-two classifier is a biased logistic regression with log loss and an L2-norm regularisation term. (p. 7)[^original]  
  <sub>anchor: "we apply a biased logistic regression classifier so that the loss term is set to be log loss"</sub>
- **descriptive / method**: The penalty coefficients C+ and C− are set to be inversely proportional to the numbers of positive and reliable negative instances. (p. 7)[^original]  
  <sub>anchor: "C+ and C− are inversely proportional to the number of positive and reliable negative instances"</sub>
- **descriptive / method**: An unlabeled address is detected as associated with mixing services when its predicted probability of being positive exceeds a probability threshold ε. (p. 7)[^original]  
  <sub>anchor: "An unlabeled address is detected as an address associated with mixing services when its probability"</sub>

## VI. EXPERIMENTAL RESULTS

- **descriptive / method**: The authors initialise the time window δ = 3 hours and the probability threshold ε = 0.6, averaging all results over 100 independent experiments on standardised features. (p. 7)[^original]  
  <sub>anchor: "We initialize the time window δ = 3 hours and the probability threshold ε = 0.6."</sub>
- **descriptive / data or feature**: Table V 2014 TPR: OCSVM 0.8986±0.0080, IF 0.8991±0.0084, LR 0.1681±0.0107, DT 0.7052±0.0162, IS1 0.8265±0.0061, IS2 0.8265±0.0061, our method 0.9165±0.0060. (p. 7)[^original]  
  <sub>anchor: "PERFORMANCE COMPARISON OF DIFFERENT METHODS (WITH STANDARD DEVIATION)."</sub>
- **descriptive / data or feature**: Table V 2014 FPR: OCSVM 0.2026±0.0064, IF 0.1285±0.0139, LR 0.0±0.0 (marked overfitting), DT 0.0±0.0 (marked overfitting), IS1 0.0406±0.0003, IS2 0.0363±0.0003, our method 0.0334±0.0010. (p. 7)[^original]  
  <sub>anchor: "PERFORMANCE COMPARISON OF DIFFERENT METHODS (WITH STANDARD DEVIATION)."</sub>
- **descriptive / data or feature**: Table V 2014 G-Mean: OCSVM 0.8465±0.0033, IF 0.8851±0.0068, LR 0.4098±0.0130, DT 0.8397±0.0097, IS1 0.8905±0.0033, IS2 0.8924±0.0033, our method 0.9412±0.0029. (p. 7)[^original]  
  <sub>anchor: "PERFORMANCE COMPARISON OF DIFFERENT METHODS (WITH STANDARD DEVIATION)."</sub>
- **descriptive / data or feature**: Table V 2015 TPR: OCSVM 0.8972±0.0105, IF 0.8996±0.0106, LR 0.0598±0.0096, DT 0.6210±0.0245, IS1 0.7832±0.0112, IS2 0.7832±0.0112, our method 0.9149±0.0081. (p. 7)[^original]  
  <sub>anchor: "PERFORMANCE COMPARISON OF DIFFERENT METHODS (WITH STANDARD DEVIATION)."</sub>
- **descriptive / data or feature**: Table V 2015 FPR: OCSVM 0.1900±0.0124, IF 0.1598±0.0147, LR 0.0±0.0 (marked overfitting), DT 0.0±0.0 (marked overfitting), IS1 0.0438±0.0003, IS2 0.0448±0.0003, our method 0.0379±0.0016. (p. 7)[^original]  
  <sub>anchor: "PERFORMANCE COMPARISON OF DIFFERENT METHODS (WITH STANDARD DEVIATION)."</sub>
- **descriptive / data or feature**: Table V 2015 G-Mean: OCSVM 0.8524±0.0047, IF 0.8693±0.0075, LR 0.2437±0.0197, DT 0.7879±0.0156, IS1 0.8654±0.0062, IS2 0.8650±0.0062, our method 0.9382±0.0038. (p. 7)[^original]  
  <sub>anchor: "PERFORMANCE COMPARISON OF DIFFERENT METHODS (WITH STANDARD DEVIATION)."</sub>
- **descriptive / data or feature**: Table V 2016 TPR: OCSVM 0.8953±0.0105, IF 0.9005±0.0105, LR 0.0004±0.0005, DT 0.3916±0.0388, IS1 0.9388±0.0061, IS2 0.9388±0.0061, our method 0.9318±0.0066. (p. 7)[^original]  
  <sub>anchor: "PERFORMANCE COMPARISON OF DIFFERENT METHODS (WITH STANDARD DEVIATION)."</sub>
- **descriptive / data or feature**: Table V 2016 FPR: OCSVM 0.1652±0.0106, IF 0.2224±0.0273, LR 0.0±0.0 (marked overfitting), DT 0.0±0.0 (marked overfitting), IS1 0.0591±0.0004, IS2 0.0586±0.0003, our method 0.0356±0.0010. (p. 7)[^original]  
  <sub>anchor: "PERFORMANCE COMPARISON OF DIFFERENT METHODS (WITH STANDARD DEVIATION)."</sub>
- **descriptive / data or feature**: Table V 2016 G-Mean: OCSVM 0.8645±0.0051, IF 0.8366±0.0135, LR 0.0115±0.0150, DT 0.6250±0.0314, IS1 0.9398±0.0031, IS2 0.9400±0.0031, our method 0.9479±0.0031. (p. 7)[^original]  
  <sub>anchor: "PERFORMANCE COMPARISON OF DIFFERENT METHODS (WITH STANDARD DEVIATION)."</sub>
- **descriptive / context**: Table V footnote: IS1 and IS2 use two different inter links counting functions, namely relative inter links and total inter links respectively, citing reference [8]. (p. 7)[^original]  
  <sub>anchor: "IS1 and IS2 use two different inter links counting function"</sub>
- **descriptive / limitation**: Table V footnote: the marked FPRs imply overfitting problems for LR and DT, because positive instances are more likely to be predicted as negative. (p. 7)[^original]  
  <sub>anchor: "The marked FPRs imply that there exist overfitting problems in LR and DT"</sub>

## A. Experimental Settings

- **descriptive / context**: The three datasets were obtained with transaction data from a Bitcoin client and labels from WalletExplorer. (p. 8)[^original]  
  <sub>anchor: "we obtain three datasets with transaction data from a Bitcoin client as well as labels from WalletExplorer"</sub>
- **descriptive / data or feature**: Addresses with only input or only output transactions were filtered out: 131 labeled addresses (0.9% of the labeled class) and 1,635,904 unlabeled addresses (22.2% of the unlabeled class). (p. 8)[^original]  
  <sub>anchor: "131 labeled addresses and 1,635,904 unlabeled addresses are filtered from the three datasets"</sub>
- **descriptive / context**: The filtering rests on the observation that mixing services act as intermediaries, so their addresses should not have only inputs or only outputs. (p. 8)[^original]  
  <sub>anchor: "addresses with either only input transactions or output transactions do not satisfy this obvious feature"</sub>
- **descriptive / finding or result**: 96.2% of the filtered labeled addresses have only one transaction record and were judged unsuitable for feature learning. (p. 8)[^original]  
  <sub>anchor: "96.2% of the filtered labeled addresses have only one transaction record"</sub>
- **descriptive / limitation**: Transactions of the filtered labeled addresses lie close to the snapshot time boundaries, so some extra transactions may not be captured in the three snapshots. (p. 8)[^original]  
  <sub>anchor: "there may be some extra transactions not being captured in our three snapshots"</sub>
- **descriptive / method**: For stage one, 70% of unlabeled addresses and 70% of labeled addresses form the training set. (p. 8)[^original]  
  <sub>anchor: "we select 70% unlabeled addresses and 70% labeled addresses to form the training set"</sub>
- **descriptive / method**: For stage two, the training set consists of 70% reliable negative instances plus the labeled addresses used in stage one. (p. 8)[^original]  
  <sub>anchor: "the training set is made up of 70% reliable negative instances as well as the labeled addresses used in stage one"</sub>
- **descriptive / method**: The testing set consists of the remaining 30% reliable negative instances and 30% labeled addresses; each dataset has its own trained model. (p. 8)[^original]  
  <sub>anchor: "The testing set is formed by the remaining 30% reliable negative instances and 30% labeled addresses"</sub>
- **descriptive / method**: Evaluation uses true positive rate (TPR), false positive rate (FPR) and Geometric Mean (G-Mean). (p. 8)[^original]  
  <sub>anchor: "we evaluate the performance of our model in terms of true positive rate (TPR), false positive rate (FPR)"</sub>
- **descriptive / context**: G-Mean was suggested in reference [17] and is widely used as a comprehensive metric for classification on imbalanced datasets. (p. 8)[^original]  
  <sub>anchor: "G- Mean was suggested in [17] and has been widely used as a comprehensive metric"</sub>
- **descriptive / method**: G-Mean takes into account the accuracy of both positive and negative instances. (p. 8)[^original]  
  <sub>anchor: "Taking both the accuracy of positive instances and negative instances into account, G-Mean is defined"</sub>
- **descriptive / method**: All reported results are averaged over 100 independent experiments using standardised features as model inputs. (p. 8)[^original]  
  <sub>anchor: "All the reported results are averaged over 100 independent experiments with the standardized features as the model inputs"</sub>
- **descriptive / limitation**: The experiments use three transaction snapshots from 2014-2016, so the authors discuss how far these data are relevant to current transactions and addresses. (p. 8)[^original]  
  <sub>anchor: "since our experiments are conducted on three transaction snapshots during 2014-2016"</sub>

## B. Method Comparison

- **descriptive / method**: The model is based on PU learning with a two-stage strategy, which the authors describe as a semi-supervised learning method. (p. 8)[^original]  
  <sub>anchor: "Our model is based on PU learning with a two-stage strategy, which is actually a semi-supervised learning method"</sub>
- **descriptive / method**: Baselines are one-class SVM (OCSVM), isolation forest (IF), logistic regression (LR), decision tree (DT) and InterScore (IS). (p. 8)[^original]  
  <sub>anchor: "we compare our model with several baseline methods including one-class support vector machine (OCSVM)"</sub>
- **descriptive / method**: IS detects mixing service entities containing multiple addresses using community anomaly detection, since such addresses have more inter-community connections. (p. 8)[^original]  
  <sub>anchor: "IS is a Bitcoin mixing detection method which can detect mixing service entities containing multiple addresses"</sub>
- **descriptive / method**: When implementing IS, the label of an address is taken as equal to the label of its entity. (p. 8)[^original]  
  <sub>anchor: "we consider the label of an address is equal to the label of its entity when implementing IS"</sub>
- **descriptive / method**: The proportion of outliers is set to 10% when fitting OCSVM and IF. (p. 8)[^original]  
  <sub>anchor: "the proportion of outliers in the datasets is set to be 10% when fitting OCSVM and IF"</sub>
- **descriptive / finding or result**: Unsupervised methods (OCSVM, IF and IS) find most positive instances but have higher false positive rates than other methods. (p. 8)[^original]  
  <sub>anchor: "they have a higher false positive rate than other methods"</sub>
- **descriptive / limitation**: IS captures only one topology feature of being an intermediary, so it lacks generalisation and its performance differs significantly across datasets. (p. 8)[^original]  
  <sub>anchor: "it is in lack of generalization so that its performance is significantly differentiated in different datasets"</sub>
- **descriptive / finding or result**: The supervised methods LR and DT overfit and perform relatively poorly. (p. 8)[^original]  
  <sub>anchor: "The two supervised methods including LR and DT lead to the problem of overfitting and relatively poor performance"</sub>
- **descriptive / finding or result**: Two possible reasons are given for LR and DT's poor performance: extreme class imbalance, and treating all unlabeled addresses as negatives, which may introduce noise. (p. 8)[^original]  
  <sub>anchor: "these two methods treat all unlabeled addresses as negative instances, which may induce noises to the datasets"</sub>
- **descriptive / finding or result**: Selecting reliable negatives before a supervised method improves the detection rate of positives over direct supervised approaches and gives the best G-Mean. (p. 8)[^original]  
  <sub>anchor: "obtain the best results in terms of G- Mean"</sub>

## C. Feature Performance Comparison

- **descriptive / finding or result**: Detection with basic features only is relatively poor, while network motifs, which reveal higher-order features, achieve decent performance. (p. 8)[^original]  
  <sub>anchor: "The detection performance is relatively poor when we only use the basic features"</sub>

## B. Method Comparison

- **descriptive / finding or result**: The authors report that the PU framework achieves a high true positive rate exceeding 91% and a low false positive rate below 4% on extremely imbalanced datasets. (p. 8)[^original]  
  <sub>anchor: "a high true positive rate exceeding 91% and a low false positive rate below 4% on extremely imbalanced datasets"</sub>

## C. Feature Performance Comparison

- **descriptive / finding or result**: Combining hybrid motifs with basic features improves nearly all metrics, showing hybrid motifs are indispensable for Bitcoin mixing detection. (p. 9)[^original]  
  <sub>anchor: "hybrid motifs play an indispensable role in the task of Bitcoin mixing detection"</sub>
- **descriptive / data or feature**: Table VI 2014 results: basic features TPR 0.8744±0.0145, FPR 0.1779±0.0128, G-Mean 0.8479±0.0120; temporal motifs 0.8728±0.0070, 0.0455±0.0009, 0.9127±0.0036; ATH motifs 0.7059±0.0111, 0.1508±0.0013, 0.7742±0.0059; hybrid motifs 0.8912±0.0064, 0.0318±0.0007, 0.9289±0.0032. (p. 9)[^original]  
  <sub>anchor: "PERFORMANCE COMPARISON OF DIFFERENT FEATURES (WITH STANDARD DEVIATION)."</sub>
- **descriptive / data or feature**: Table VI 2014 results (combinations): basic with temporal motifs TPR 0.9032±0.0064, FPR 0.0362±0.0014, G-Mean 0.9330±0.0033; basic with ATH motifs 0.8797±0.0089, 0.1350±0.0091, 0.8723±0.0075; basic with hybrid motifs 0.9165±0.0060, 0.0334±0.0010, 0.9412±0.0029. (p. 9)[^original]  
  <sub>anchor: "PERFORMANCE COMPARISON OF DIFFERENT FEATURES (WITH STANDARD DEVIATION)."</sub>
- **descriptive / data or feature**: Table VI 2015 results: basic features TPR 0.8146±0.0115, FPR 0.1388±0.0038, G-Mean 0.8376±0.0064; temporal motifs 0.8453±0.0098, 0.1423±0.0024, 0.8515±0.0043; ATH motifs 0.8426±0.0100, 0.0716±0.0009, 0.8845±0.0051; hybrid motifs 0.8823±0.0088, 0.0667±0.0020, 0.9074±0.0041. (p. 9)[^original]  
  <sub>anchor: "PERFORMANCE COMPARISON OF DIFFERENT FEATURES (WITH STANDARD DEVIATION)."</sub>
- **descriptive / data or feature**: Table VI 2015 results (combinations): basic with temporal motifs TPR 0.8864±0.0092, FPR 0.0878±0.0079, G-Mean 0.8992±0.0065; basic with ATH motifs 0.8543±0.0095, 0.0852±0.0018, 0.8840±0.0048; basic with hybrid motifs 0.9149±0.0081, 0.0379±0.0016, 0.9382±0.0038. (p. 9)[^original]  
  <sub>anchor: "PERFORMANCE COMPARISON OF DIFFERENT FEATURES (WITH STANDARD DEVIATION)."</sub>
- **descriptive / data or feature**: Table VI 2016 results: basic features TPR 0.6442±0.0317, FPR 0.3812±0.0077, G-Mean 0.6311±0.0129; temporal motifs 0.9271±0.0073, 0.0584±0.0012, 0.9343±0.0035; ATH motifs 0.6639±0.0145, 0.3154±0.0043, 0.6741±0.0061; hybrid motifs 0.9123±0.0071, 0.0356±0.0011, 0.9380±0.0034. (p. 9)[^original]  
  <sub>anchor: "PERFORMANCE COMPARISON OF DIFFERENT FEATURES (WITH STANDARD DEVIATION)."</sub>
- **descriptive / data or feature**: Table VI 2016 results (combinations): basic with temporal motifs TPR 0.9335±0.0067, FPR 0.0508±0.0011, G-Mean 0.9413±0.0031; basic with ATH motifs 0.8150±0.0112, 0.1995±0.0047, 0.8077±0.0047; basic with hybrid motifs 0.9318±0.0066, 0.0356±0.0010, 0.9479±0.0031. (p. 9)[^original]  
  <sub>anchor: "PERFORMANCE COMPARISON OF DIFFERENT FEATURES (WITH STANDARD DEVIATION)."</sub>
- **descriptive / context**: Table VI footnote: hybrid motifs are a combination of temporal and ATH motifs. (p. 9)[^original]  
  <sub>anchor: "Hybrid motifs are a combination of Temporal and ATH motifs."</sub>
- **descriptive / method**: The authors analyse feature importance using the absolute LR weights averaged over the three datasets across 100 independent experiments. (p. 9)[^original]  
  <sub>anchor: "we analyze the impact of the features according to their absolute value of weight averaged over the three datasets"</sub>
- **descriptive / finding or result**: The top 10 important features are TF3, AF5, AF4, NF17, NF11, NF16, NF12, NF14, TF6 and TF1. (p. 9)[^original]  
  <sub>anchor: "We find that the top 10 important features are TF3, AF5, AF4, NF17, NF11, NF16, NF12, NF14, TF6 and TF1"</sub>
- **descriptive / finding or result**: The ranking shows basic features also play an important role in the detection process. (p. 9)[^original]  
  <sub>anchor: "illustrating that the basic features also play an important role in the detection process"</sub>

## D. Parameter Sensitivity Analysis

- **descriptive / method**: A sensitivity analysis examines the time window δ and probability threshold ε; Fig. 8 plots TPR, FPR and G-Mean against δ over values 0.25, 0.5, 1, 2 up to 6 hours. (p. 9)[^original]  
  <sub>anchor: "Fig. 8 shows the results in terms of TPR, FPR and G-Mean of our model versus time window"</sub>
- **descriptive / data or feature**: Fig. 8 caption: parameter analysis of time window δ; the numeric values behind the plotted curves are not given in the extracted text. (p. 9)[^original]  
  <sub>anchor: "Patameter analysis of time window δ."</sub>
- **descriptive / data or feature**: Probability threshold analysis for 2014: TPR is 0.9318, 0.9165, 0.8962, 0.8653 and 0.8016 at ε = 0.5, 0.6, 0.7, 0.8 and 0.9; FPR is 0.0535, 0.0334, 0.0191, 0.0093 and 0.0028. (p. 9)[^original]  
  <sub>anchor: "PATAMETER ANALYSIS OF PROBABILITY THRESHOLD ε."</sub>
- **descriptive / data or feature**: Probability threshold analysis for 2015: TPR is 0.9339, 0.9149, 0.8863, 0.8420 and 0.7652 at ε = 0.5, 0.6, 0.7, 0.8 and 0.9; FPR is 0.0686, 0.0379, 0.0182, 0.0083 and 0.0032. (p. 9)[^original]  
  <sub>anchor: "PATAMETER ANALYSIS OF PROBABILITY THRESHOLD ε."</sub>
- **descriptive / data or feature**: Probability threshold analysis for 2016: TPR is 0.9438, 0.9318, 0.9184, 0.8990 and 0.8510 at ε = 0.5, 0.6, 0.7, 0.8 and 0.9; FPR is 0.0502, 0.0356, 0.0221, 0.0114 and 0.0037. (p. 9)[^original]  
  <sub>anchor: "PATAMETER ANALYSIS OF PROBABILITY THRESHOLD ε."</sub>
- **descriptive / finding or result**: In the probability-threshold table, TPR and FPR both fall as ε rises from 0.5 to 0.9 on all three snapshot datasets; for example 2014 TPR drops from 0.9318 to 0.8016 and FPR from 0.0535 to 0.0028. (p. 9)[^original]  
  <sub>anchor: "PATAMETER ANALYSIS OF PROBABILITY THRESHOLD ε."</sub>
- **descriptive / finding or result**: Current transaction data (2020, 1,500,000 consecutive transactions since Mar. 25, 2020): OCSVM TPR 0.6474±0.0974, FPR 0.0572±0.0162, G-Mean 0.7788±0.0567; IF 0.8537±0.0774, 0.5431±0.0539, 0.6220±0.0350.[^original]  
  <sub>anchor: "PERFORMANCE COMPARISON OF DIFFERENT METHODS ON CURRENT TRANSACTION DATA (WITH STANDARD DEVIATION)."</sub>
- **descriptive / finding or result**: Current transaction data: LR gives TPR 0.0±0.0, FPR 0.0±0.0 (marked overfitting), G-Mean 0.0±0.0; DT gives TPR 0.0685±0.0599, FPR 0.0±0.0 (marked overfitting), G-Mean 0.2236±0.1368.[^original]  
  <sub>anchor: "PERFORMANCE COMPARISON OF DIFFERENT METHODS ON CURRENT TRANSACTION DATA (WITH STANDARD DEVIATION)."</sub>
- **descriptive / finding or result**: Current transaction data: IS1 gives TPR 0.8189±0.0629, FPR 0.4121±0.0007, G-Mean 0.6933±0.0268; IS2 gives TPR 0.8189±0.0629, FPR 0.4006±0.0008, G-Mean 0.7001±0.0270.[^original]  
  <sub>anchor: "PERFORMANCE COMPARISON OF DIFFERENT METHODS ON CURRENT TRANSACTION DATA (WITH STANDARD DEVIATION)."</sub>
- **descriptive / finding or result**: Current transaction data: the proposed method gives TPR 0.7874±0.0671, FPR 0.0991±0.0104 and the highest G-Mean of 0.8413±0.0327 among the methods listed.[^original]  
  <sub>anchor: "PERFORMANCE COMPARISON OF DIFFERENT METHODS ON CURRENT TRANSACTION DATA (WITH STANDARD DEVIATION)."</sub>
- **descriptive / context**: The current-data table footnote describes a dataset of consecutive transactions since Mar. 25, 2020, though the extracted text is partly garbled.[^original]  
  <sub>anchor: "PERFORMANCE COMPARISON OF DIFFERENT METHODS ON CURRENT TRANSACTION DATA (WITH STANDARD DEVIATION)."</sub>

---

[previous part](digest-001.md) | [source overview](overview.md) | [next part](digest-003.md)

[^original]: Jiajing Wu, Jieli Liu, Weili Chen, Huawei Huang, Zibin Zheng, Yan Zhang, "Detecting Mixing Services via Mining Bitcoin Transaction Network With Hybrid Motifs" (2021-01-21). https://arxiv.org/abs/2001.05233
