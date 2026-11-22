---
type: Source Digest
title: Explainable Fraud Detection with GNNExplainer and Shapley Values - part 3 of 3 (pp. 27-36)
description: 'Verified paraphrased digest, pp. 27-36: 5. Experiments and Results > 5.1. Fraud Detection; 5. Experiments and Results > 5.2. Fraud Explanation; 6. Conclusion > 6.1. Discussion; and 3 more sections'
resource: https://arxiv.org/abs/2509.12262
tags:
- academic_finding
- explainability
- global_academic
- network_graph
- preprint
status: stable
source_id: arxiv-explainable-fraud-detection-with-gnnexplainer-and-shapley-values
issuer: arxiv
issuer_name: arXiv
jurisdictions:
- GLOBAL_ACADEMIC
tier: 3
instrument_type: preprint
normative_force: academic_finding
publication_date: '2025-12-09'
legal_status: unknown
part: 3
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
  resource: https://arxiv.org/abs/2509.12262
  title: Explainable Fraud Detection with GNNExplainer and Shapley Values
  author: org:arxiv
  last_modified: '2025-12-09T00:00:00Z'
digest_points: 40
---

# Explainable Fraud Detection with GNNExplainer and Shapley Values (digest)

[previous part](digest-002.md) | [source overview](overview.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (pp. 27-36) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **academic finding**.

## 5.1. Fraud Detection

- **descriptive / context**: The J.P.Morgan dataset is highly imbalanced, with 1,467,358 nonfraudulent transactions and 30,819 fraudulent transactions, so Average Precision and AUC are used to avoid misleading interpretation of a high accuracy result. (p. 27)[^original]  
  <sub>anchor: "Considering that the J.P.Morgan dataset is highly imbalanced with 1,467,358 nonfraudulent transactions"</sub>
- **descriptive / finding or result**: GAT achieved accuracy 0.8845, loss 0.2234, average precision 0.8132 and AUC 0.8679 on fraud detection. (p. 27)[^original]  
  <sub>anchor: "|GAT|0.8845|0.2234|0.8132|0.8679|"</sub>
- **descriptive / finding or result**: GEM achieved accuracy 0.8923, loss 0.2454, average precision 0.8023 and AUC 0.8865 on fraud detection. (p. 27)[^original]  
  <sub>anchor: "|GEM|0.8923|0.2454|0.8023|0.8865|"</sub>
- **descriptive / finding or result**: The xFraud detector on the original data achieved accuracy 0.8946, loss 0.2421, average precision 0.8774 and AUC 0.8821. (p. 27)[^original]  
  <sub>anchor: "|xFraud detector(original data)|0.8946|0.2421|0.8774|0.8821|"</sub>
- **descriptive / finding or result**: The xFraud detector without the Line of Business and Sector fields achieved accuracy 0.9310, loss 0.2312, average precision 0.9212 and AUC 0.8915. (p. 27)[^original]  
  <sub>anchor: "|xFraud detectorwithout Line ofBusiness andSector fields|0.9310|0.2312|0.9212|0.8915|"</sub>
- **descriptive / finding or result**: The overall performance of the three detection models was consistent with the authors' prediction; the two baselines GAT and GEM performed worse than the xFraud detector because of their limitations in processing typed features and relations. (p. 27)[^original]  
  <sub>anchor: "The 2 baseline models GAT and GEM do not perform as well as xFraud detector due to their limitations in processing type features and relations."</sub>
- **descriptive / finding or result**: The xFraud detector without Line of Business and Sector fields, but with dAmount and dTime fields, achieved accuracy 0.9461, loss 0.2127, average precision 0.9370 and AUC 0.9640. (p. 27)[^original]  
  <sub>anchor: "|xFraud detectorwithout Line ofBusiness andSector fields,and with_dAmount_and_dTime_fields|0.9461|0.2127|0.9370|0.9640|"</sub>

## 5.2. Fraud Explanation

- **descriptive / method**: The proposed explainer outputs a GNNExplainer subgraph, two bar charts (node features and edge missingness SHAP), and relevant original tabular data for context. (p. 28)[^original]  
  <sub>anchor: "The proposed explainer gives us a GNNExplainer (Ying et al, 2019) subgraph, 2 bar charts for node features and edge missingness SHAP."</sub>
- **descriptive / method**: The authors analyse two fraud cases of two transaction types (withdrawal and quick payment) and one non-fraud case, expecting the fraud cases to match account takeover (ATO) fraud patterns. (p. 28)[^original]  
  <sub>anchor: "We will analyse 2 fraud cases of 2 different transaction types (withdrawal and quick payment) and 1 non-fraud case."</sub>
- **descriptive / finding or result**: For fraud case WITHDRAWAL-975088, the edge from JPMC-CLIENT-974815 to the node being explained has the negative SHAP value with the highest absolute value; removing it would make non-fraud prediction more likely. (p. 28)[^original]  
  <sub>anchor: "has a negative SHAP value with the highest absolute value. This means that if this edge is removed, it is more likely for the model to predict WITHDRAWAL-975088 as non-fraud."</sub>
- **descriptive / finding or result**: For WITHDRAWAL-975088, dTime has a high negative correlation with the prediction, so lower dTime makes fraud more likely, consistent with the finding that fraud transactions tend to be executed rapidly. (p. 28)[^original]  
  <sub>anchor: "dTime_ has a high negative correlation with the current node’s prediction."</sub>

## 5.1. Fraud Detection

- **descriptive / finding or result**: The authors report that adding dAmount and dTime as features to transaction nodes improves performance significantly over all 4 metrics. (p. 28)[^original]  
  <sub>anchor: "The results show that adding _dAmount_ and _dTime_ as features to transaction nodes improves the performance significantly over all 4 metrics."</sub>
- **descriptive / finding or result**: Based on the Section 4.2 data analysis, dAmount and dTime were expected to improve model performance, while the original Line of Business and Sector fields may not. (p. 28)[^original]  
  <sub>anchor: "Based on the data analysis in Section 4.2, _dAmount_ and _dTime_ are expected to improve the model performance, while the original Line of Business and Sector fields may not."</sub>

## 5.2. Fraud Explanation

- **descriptive / case example**: In the WITHDRAWAL-975088 subgraph, client JPMC-CLIENT-974815 made several successive quick payments to accounts in unusual countries (Gabon and Northern Mariana Islands) before the withdrawal, matching the ATO pattern of rapid instant payments followed by withdrawal. (p. 29)[^original]  
  <sub>anchor: "These quick payments are sent to accounts at unusual countries like Gabon and Northern Mariana Islands."</sub>
- **descriptive / finding or result**: For QUICK-PAYMENT-158942, dTime and Amount have negative correlation with fraud, so faster and smaller transactions make ATO fraud more likely; dAmount has a high positive correlation, meaning a large transaction right after a small one indicates fraud. (p. 29)[^original]  
  <sub>anchor: "In contrast, _dAmount_ has a hight positive correlation with the fraud prediction"</sub>
- **descriptive / case example**: QUICK-PAYMENT-158942 appears to be part of an ATO fraud, as client JPMC-CLIENT-158905 makes several quick payments within a short period following a withdrawal. (p. 29)[^original]  
  <sub>anchor: "QUICKPAYMENT-158942 appears to be a part of an ATO fraud as the client involved (JPMCCLIENT-158905) makes several quick payments within a short period of time following a withdrawal."</sub>
- **descriptive / case example**: CLIENT-158925 and JPMC-CLIENT-158905 send money back and forth more than once, which the authors say indicates abnormal movement of money. (p. 29)[^original]  
  <sub>anchor: "We can also see that CLIENT-158925 and JPMC-CLIENT-158905 send money back and forth more than once, indicating abnormal movement of money."</sub>
- **descriptive / finding or result**: For WITHDRAWAL-975088 and QUICK-PAYMENT-158942, the edge missingness SHAP values show that most fraud-indicative information comes from the clients making and receiving the relevant transactions. (p. 30)[^original]  
  <sub>anchor: "where most fraud indicative information comes from the clients making and receiving the relevant transactions."</sub>
- **descriptive / case example**: Non-fraud case WITHDRAWAL-1007467: client JPMC-CLIENT-1007409 makes no quick payments and the receiver is in the USA, a common transaction country, so the fraud patterns of Figures 16 and 17 are absent. (p. 30)[^original]  
  <sub>anchor: "JPMC-CLIENT-1007409 does not make any quick payments, and the receiver resides in USA which is a common country for a transaction."</sub>
- **descriptive / finding or result**: For WITHDRAWAL-1007467, removing the edge between the client and the transaction would be unlikely to change the prediction, as less information reaches the transaction node and its risk score stays low. (p. 30)[^original]  
  <sub>anchor: "it is unlikely for the model to change its prediction. This is reasonable since less information is passed to the transaction node"</sub>
- **descriptive / finding or result**: For WITHDRAWAL-1007467, dTime has a positive correlation with non-fraud prediction (non-fraud accounts take more time between consecutive transactions) and Amount has a negative correlation (smaller USD amounts tend to be non-fraudulent); only direct features had significant impact. (p. 30)[^original]  
  <sub>anchor: "_dTime_ has a positive correlation with the non-fraud prediction"</sub>
- **descriptive / case example**: Non-fraud case WITHDRAWAL-1006655: client JPMC-CLIENT1006498 transacts with two accounts, one in the USA and one in Anguilla; the detector did not treat transacting with two accounts in two countries as an ATO indicator. (p. 31)[^original]  
  <sub>anchor: "we can see that JPMC-CLIENT1006498 makes transactions with 2 different accounts, 1 in USA and 1 in Anguilla."</sub>
- **descriptive / context**: The authors note that in some payment systems, transacting on two accounts in two countries could be a decisive factor for flagging a transaction as fraud (citing Bukszpan, 2012). (p. 31)[^original]  
  <sub>anchor: "In some payment systems, this could be a decisive factor for a model to flag a transaction as fraud (Bukszpan, 2012)."</sub>

## 6.1. Discussion

- **descriptive / finding or result**: The authors propose a composite explainer combining GNNExplainer, node feature Shapley values and edge missingness Shapley values, presented as a more comprehensive solution than existing GNN explainers. (p. 31)[^original]  
  <sub>anchor: "we propose a composite explainer consisting of GNNExplainer, node features and edge missingness Shapley values"</sub>
- **descriptive / finding or result**: The adapted xFraud detector achieved good accuracy, average precision and AUC on the J.P.Morgan dataset, which the authors say is expected because xFraud's detection task is the same. (p. 31)[^original]  
  <sub>anchor: "We adapt the xFraud detector to our J.P.Morgan dataset and obtain good performance in terms of accuracy, average precision, and AUC."</sub>
- **descriptive / context**: The J.P.Morgan dataset was generated with a multi-agent simulator, making fraud patterns consistent and capturing agent interactions fully in a graph dataset. (p. 31)[^original]  
  <sub>anchor: "the J.P.Morgan dataset is generated"</sub>
- **descriptive / finding or result**: The authors attribute the inferior performance of GAT and GEM to a lack of type feature processing. (p. 32)[^original]  
  <sub>anchor: "We also confirm that the 2 baseline models GAT and GEM give inferior performance due to a lack of type feature processing."</sub>
- **descriptive / finding or result**: Using knowledge of real-world fraud cases, the generated visualisations are said to show patterns matching typical ATO scenarios described in Section 5.2. (p. 32)[^original]  
  <sub>anchor: "we can analyse the generated visualization to confirm that there exists patterns indicating the flagged fraud transactions"</sub>

## 6.2. Limitation

- **descriptive / limitation**: The synthetic J.P.Morgan dataset is simplistic in entity types and fraud patterns compared with real-world fraud, which can involve complicated money movements across accounts and third-party systems. (p. 32)[^original]  
  <sub>anchor: "the synthetic J.P.Morgan dataset is quite simplistic in terms of entity types and fraud patterns"</sub>
- **descriptive / limitation**: Fraudsters may hide patterns, for example by stretching transactions out rather than executing them rapidly, though this could require a trade-off between safety and profits for them. (p. 32)[^original]  
  <sub>anchor: "instead of executing transactions rapidly, they could stretch them out in order not to stand out"</sub>
- **descriptive / limitation**: The visualisations from the composite explainer are often only readable to data analysts or fraud investigators with payment fraud knowledge. (p. 32)[^original]  
  <sub>anchor: "the generated visualization from the composite explainer is often only readable to data analysts or fraud investigators"</sub>
- **descriptive / limitation**: Because the composite explainer has three explanation components, they may conflict, and the analyst or investigator must resolve any contradictions using context and domain knowledge. (p. 32)[^original]  
  <sub>anchor: "there is a possibility of conflicts existing among them"</sub>

## 6.3. Future Scope

- **descriptive / limitation**: The xFraud detector does not use temporal information from the original data, since Rao et al (2020) want the model to view all of a user's transactions at any time. (p. 32)[^original]  
  <sub>anchor: "The xFraud detector does not take into temporal information from the original data"</sub>
- **descriptive / context**: T-GNNExplainer (Xia et al, 2023) uses temporal graph networks but has not been tested on a real-world dataset, and its event-specific subgraphs need better visualisation. (p. 32)[^original]  
  <sub>anchor: "T-GNNExplainer (Xia et al, 2023) is a solution that utilizes temporal graph networks"</sub>
- **descriptive / context**: Rao et al (2022) propose DyHGN, which uses temporal graph networks for fraud detection and works well on eBay's real-world datasets, but its explanation uses only Shapley values, not GNNExplainer subgraphs. (p. 33)[^original]  
  <sub>anchor: "While this model works well on eBay’s real-world datasets, explanation for DyHGN is only given by Shapley values"</sub>
- **descriptive / context**: The authors reason that since DyHGN's authors also wrote xFraud, which used GNNExplainer, there must have been significant challenges preventing explanation subgraphs for temporal graph networks. (p. 33)[^original]  
  <sub>anchor: "there must have been significant challenges preventing them from generating explanation subgraphs"</sub>
- **descriptive / limitation**: The project focuses on ATO fraud, and the synthetic J.P.Morgan dataset does not capture the many other fraud scenarios of varying complexity. (p. 33)[^original]  
  <sub>anchor: "This project focus on ATO fraud, but there are a myriad of fraud scenarios"</sub>
- **descriptive / context**: Financial datasets are hard to obtain, especially those with semantically labelled fields, because institutions and payment providers usually want to keep such information private. (p. 33)[^original]  
  <sub>anchor: "financial datasets are not easily obtained, especially datasets with semantically labelled fields"</sub>
- **descriptive / limitation**: PaySim and BankSim are popular synthetic payment fraud generators, but their fraud scenarios are too simplistic, so models trained on them give no convincing proof of real-world applicability. (p. 33)[^original]  
  <sub>anchor: "their fraud scenarios are too simplistic and training a model on such data does not give convincing proof"</sub>
- **recommended / recommendation**: For independent researchers, the authors consider a synthetic data generator that could capture typical and modern fraud scenarios and involve more entities to be desirable. (p. 33)[^original]  
  <sub>anchor: "a synthetic data generator that could capture typical and modern fraud scenarios and involve more entities is desirable"</sub>

---

[previous part](digest-002.md) | [source overview](overview.md)

[^original]: arXiv, "Explainable Fraud Detection with GNNExplainer and Shapley Values" (2025-12-09). https://arxiv.org/abs/2509.12262
