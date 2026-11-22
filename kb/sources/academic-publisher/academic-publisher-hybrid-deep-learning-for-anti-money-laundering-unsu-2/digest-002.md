---
type: Source Digest
title: 'Hybrid deep learning for anti-money laundering: Unsupervised detection of emerging schemes via feature fusion and explainable artificial intelligence - part 2 of 3 (pp. 5-11)'
description: 'Verified paraphrased digest, pp. 5-11: Machine Learning with Applications > Hybrid deep learning for anti-money laundering: Unsupervised detection of emerging schemes via feature fusion and explainable artificial intelligence'
resource: https://doi.org/10.1016/j.mlwa.2026.100856
tags:
- academic_finding
- academic_paper
- data_features
- explainability
- global_academic
- ml_statistics
- network_graph
- transaction_behaviour
status: stable
source_id: academic-publisher-hybrid-deep-learning-for-anti-money-laundering-unsu-2
issuer: academic_publisher
issuer_name: Academic publisher / repository
jurisdictions:
- GLOBAL_ACADEMIC
tier: 3
instrument_type: academic_paper
normative_force: academic_finding
publication_date: '2026-02-25'
legal_status: unknown
part: 2
parts_total: 3
content_mode: digest
generated:
  by: claude-code-subagent/claude-sonnet-5-5
  at: '2026-11-22T14:40:32Z'
verified:
- by: process:kb-digest-check/anchor-match
  at: '2026-11-22T14:40:32Z'
- by: claude-code-judge-agent/claude-opus-5-5
  at: '2026-11-22T14:40:32Z'
sources:
- id: original
  resource: https://doi.org/10.1016/j.mlwa.2026.100856
  title: 'Hybrid deep learning for anti-money laundering: Unsupervised detection of emerging schemes via feature fusion and explainable artificial intelligence'
  author: org:academic_publisher
  last_modified: '2026-02-25T00:00:00Z'
digest_points: 66
---

# Hybrid deep learning for anti-money laundering: Unsupervised detection of emerging schemes via feature fusion and explainable artificial intelligence (digest)

[previous part](digest-001.md) | [source overview](overview.md) | [next part](digest-003.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (pp. 5-11) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **academic finding**.

## 2.4.1. Local outlier factor (LOF)

- **descriptive / method**: Local outlier factor (LOF) was used to benchmark density-based anomaly detection; it computes a local reachable density for each point from its k nearest neighbours and assigns an LOF score, where a score above 1 indicates an anomalous transaction. (p. 5)[^original]  
  <sub>anchor: "where a score greater than 1 indicates an anomaly transaction (Breunig et al., 2000)"</sub>
- **descriptive / limitation**: The authors note LOF is computationally expensive on large datasets and sensitive to k (number of neighbours), creating scalability challenges for financial institutions with large-scale data. (p. 5)[^original]  
  <sub>anchor: "the model is computationally expensive on a large dataset and sensitive to k (number of neighbours)"</sub>

## 2.4.2. Isolation forest (IF)

- **descriptive / method**: Isolation Forest was chosen to address the lack of confirmed suspicious activity labels and the high dimensionality of the combined feature set; it isolates anomalies through random feature partitioning. (p. 5)[^original]  
  <sub>anchor: "This model works by isolating anomalies through random feature partitioning"</sub>
- **descriptive / finding or result**: The authors state Isolation Forest's computational efficiency enables real-time monitoring, which they consider critical for AML systems. (p. 5)[^original]  
  <sub>anchor: "its computational efficiency (( _𝑛_ log _𝑛_ )) enables real-time monitoring, which is critical for AML systems"</sub>
- **descriptive / limitation**: Isolation Forest suffers from axis-parallel bias and is highly sensitive to high-dimensional noise. (p. 5)[^original]  
  <sub>anchor: "it suffers from axis-parallel bias and is highly sensitive to high-dimensional noise"</sub>

## 2.4. Anomaly detection

- **descriptive / method**: Isolation Forest, Local Outlier Factor and One-Class SVM were trained on the non-flagged dataset as unsupervised anomaly detection models, selected for scarce labelled data, high dimensionality and different mathematical intuitions. (p. 5)[^original]  
  <sub>anchor: "We employed anomaly detection models by training the Isolation Forest (IF), Local Outlier Factor (LOF), and One-Class Support Vector Machine"</sub>
- **descriptive / data or feature**: The training set was built exclusively from 26,368 clean (non-flagged) transactions. (p. 5)[^original]  
  <sub>anchor: "The training set was constructed exclusively from 26,368 ‘clean’ (non-flagged) transactions"</sub>
- **descriptive / method**: One-Class SVM was judged appropriate because it learns transaction boundaries, using a kernel to map data into a high-dimensional space and maximise the space around normal transactions while minimising flagged false positives. (p. 5)[^original]  
  <sub>anchor: "maximise the space around the ‘normal’ transactions while minimising the flagged false positives makes it an appropriate model"</sub>
- **descriptive / method**: One-Class SVM maps input vectors into a feature space via a kernel and separates training data from the origin with a maximum margin hyperplane; an RBF kernel was used to capture non-linear interactions between VAE and GNN embeddings. (p. 5)[^original]  
  <sub>anchor: "attempts to separate the training data from the origin with a maximum margin hyperplane"</sub>

## 2.4.3. One-class support vector machine (One-Class SVM)

- **descriptive / method**: The One-Class SVM sensitivity was controlled by two hyperparameters, Nu (ν) and Gamma (γ). (p. 6)[^original]  
  <sub>anchor: "The model’s sensitivity was controlled via two hyperparameters, Nu ( _𝜈_ ) and Gamma ( _𝛾_ )."</sub>
- **descriptive / data or feature**: Figure 3 shows mutual information scores for the final 9 selected features. (p. 6)[^original]  
  <sub>anchor: "Fig. 3. Mutual information (MI) scores for the final 9 selected features."</sub>

## 2.5. Hyperparameter optimisation protocol

- **descriptive / method**: The best model, One-Class SVM, was tuned on the fused feature space with a Grid Search protocol intended to minimise overfitting; the non-flagged training data was split into an inner train set (N = 19,776) and a validation set (N = 10,757). (p. 6)[^original]  
  <sub>anchor: "The process involved partitioning of the non-flagged training data into an inner train set ( _𝑁_ = 19,776) and a validation set ( _𝑁_ = 10,757)"</sub>
- **descriptive / method**: The grid search explored Nu values of 0.001, 0.01, 0.05, 0.1 and 0.2, and Gamma values of scale, auto, 0.01 and 0.1. (p. 6)[^original]  
  <sub>anchor: "Nu ( _𝜈_ ): [0 _._ 001 _,_ 0 _._ 01 _,_ 0 _._ 05 _,_ 0 _._ 1 _,_ 0 _._ 2]"</sub>
- **descriptive / definition**: Average precision was optimised because it focuses on the quality of the top-ranked alerts, the operational priority. (p. 6)[^original]  
  <sub>anchor: "AP was optimised because it focuses on the quality of the top-ranked alerts, which is the operational priority"</sub>
- **descriptive / definition**: Precision @ Top 5% (P@K) measures the proportion of true anomalies within the top 5% of the prioritised alert queue, aligned with high-priority triage needs in resource-constrained compliance teams. (p. 6)[^original]  
  <sub>anchor: "calculating the proportion of true anomalies found within the top 5% of the prioritised alert queue"</sub>
- **descriptive / definition**: Recall @ 95% (R@Q) measures the proportion of total money laundering risk captured above the defined alert review bandwidth. (p. 6)[^original]  
  <sub>anchor: "This metric measures the proportion of the total money laundering risk captured above the defined bandwidth"</sub>

## 2.6. Innovations in the AML detection model

- **descriptive / context**: The authors claim the framework's innovation is a semi-supervised novelty detection strategy using OCSVM trained on a non-flagged dataset, versus traditional unsupervised models such as Isolation Forest. (p. 6)[^original]  
  <sub>anchor: "our framework introduces a significant innovation by adopting a semi-supervised novelty detection strategy"</sub>
- **descriptive / context**: The approach fuses VAE-learned latent embeddings with GNN-captured network topologies to detect non-linear laundering schemes that evade rule-based features, which the authors say aligns with updated FATF Recommendation 16. (p. 6)[^original]  
  <sub>anchor: "aligning directly with updated FATF recommendation 16"</sub>
- **descriptive / definition**: Average precision (AP) is presented as important under high class imbalance because it summarises the precision–recall curve and ranks anomalies above normal transactions. (p. 6)[^original]  
  <sub>anchor: "AP provides a robust assessment by summarising the precision–recall curve"</sub>
- **descriptive / definition**: AUC-ROC was used to evaluate the general separation capability of the model and provide a baseline against standard literature. (p. 6)[^original]  
  <sub>anchor: "We employed AUCROC to evaluate the general separation capabilities of the model"</sub>
- **descriptive / definition**: F1-Score is the harmonic mean of precision and recall, measuring balance between detection sensitivity and false alarm rates. (p. 6)[^original]  
  <sub>anchor: "The harmonic mean of precision and recall was calculated to measure the model’s balance between detection sensitivity and false alarm rates"</sub>

## 2.7.1. Model explainability and deployment

- **descriptive / method**: Model performance was assessed by its ability to differentiate flagged from normal transactions, accounting for class imbalance and the need to prioritise alerts. (p. 6)[^original]  
  <sub>anchor: "The model’s performance was evaluated based on its ability to differentiate between flagged transactions and normal transactions"</sub>
- **descriptive / method**: SHAP (Shapley Additive exPlanations) was used to explain the model's scoring and improve interpretability and transparency. (p. 6)[^original]  
  <sub>anchor: "SHAP (Shapley Additive exPlanations) was employed to provide insights into the model’s scoring"</sub>
- **descriptive / data or feature**: Table 4 gives flagged transactions per rule: transactions above the $10,000 threshold 15,328; high amount ($10,000) or significant deviation 12,491; transaction to a high-risk country per the FATF 6,742; structuring pattern below threshold 1,859; structuring pattern and high-risk country 945. (p. 7)[^original]  
  <sub>anchor: "Transactions above $10,000 threshold|15,328|"</sub>

## 3.3. Feature importance analysis

- **descriptive / method**: SHAP is said to satisfy four axioms (efficiency, symmetry, dummy player and linearity); a Kernel explainer with a background dataset sampled from training and test data approximated the contribution of the 9 features to OCSVM anomaly scores. (p. 7)[^original]  
  <sub>anchor: "it satisfies the four axioms: efficiency, symmetry, dummy player, and linearity"</sub>
- **descriptive / method**: Results were displayed in a Django web application supporting batch processing, alert prioritisation and access limited to authorised compliance personnel. (p. 7)[^original]  
  <sub>anchor: "The model results for compliance professionals, system administrators, regulatory authorities, and policy makers were displayed on a web application developed using the Django framework"</sub>
- **descriptive / method**: The model was deployed on a normal computer (Intel Core i7, 16 GB RAM) without specialised GPU acceleration. (p. 7)[^original]  
  <sub>anchor: "The model deployment in a normal computer with specifications including an Intel Core i7 processor and 16 GB of Random Access Memory (RAM)"</sub>

## 3. Results

- **descriptive / data or feature**: The framework was evaluated on a dataset of 54,258 cross-border financial transactions using a sequential protocol: exploratory data analysis, embedding interpretation, feature selection validation, model training, hyperparameter optimisation and final benchmarking. (p. 7)[^original]  
  <sub>anchor: "was evaluated on a 54,258 cross-border financial transaction dataset"</sub>
- **descriptive / finding or result**: The heuristic rules flagged 20,823 transactions, 39.72% of those under review. (p. 7)[^original]  
  <sub>anchor: "the heuristic rules identified 20,823 transactions, 39.72% of the total transactions under review"</sub>
- **descriptive / finding or result**: Transaction amounts had a heavy-tailed distribution (skewness above 10), which the authors cite as justifying log-transformation, VAE compression and GNN mapping of relationships. (p. 7)[^original]  
  <sub>anchor: "transaction amounts were observed to have a heavy-tailed distribution (skewness _>_ 10)"</sub>

## 3.1. Exploratory data analysis

- **descriptive / data or feature**: The fused feature set comprised 4 rule-based features, 2 VAE embeddings and 3 GNN embeddings. (p. 7)[^original]  
  <sub>anchor: "that is, 4 Rule-based features, 2 VAE embeddings, and 3 GNN embeddings"</sub>
- **descriptive / finding or result**: GNN_Embedding_1 and GNN_Embedding_0 rank immediately after the top rule-based feature, which the authors read as indicating that the customer transaction network gives a strong risk signal. (p. 7)[^original]  
  <sub>anchor: "Notably, GNN_Embedding_1 and GNN_Embedding_0 rank immediately after the top rule-based feature"</sub>

## 3.5. Impact of feature fusion (ablation study)

- **descriptive / finding or result**: Table 7 shows removing deep learning embeddings caused only a minimal shift in global metrics, while SHAP shows specific embeddings such as GNN_Embedding_1 remain locally influential for volume-variability anomaly types. (p. 7)[^original]  
  <sub>anchor: "the removal of deep learning embeddings resulted in a minimal performance shift in the global metrics"</sub>
- **descriptive / finding or result**: Table 6 reports OCSVM performing best on the most critical operational metrics, achieving Precision @ 5% of 99.63%, versus 83.99% for Isolation Forest. (p. 7)[^original]  
  <sub>anchor: "Specifically, OCSVM achieved a Precision @ 5% of 99.63%"</sub>
- **descriptive / finding or result**: LOF achieved a slightly higher ROC-AUC (0.8419) than OCSVM in the reported text, while OCSVM significantly outperformed LOF and Isolation Forest on precision-based metrics. (p. 7)[^original]  
  <sub>anchor: "the Local Outlier Factor (LOF) achieved a slightly higher ROC-AUC (0.8419)"</sub>

## 3.2. Deep learning embeddings

- **descriptive / data or feature**: The VAEs were trained on a subset of 7 numerical features, converging at 30 epochs to output 8 embeddings; the GNNs covered 31,108 unique parties as nodes and 27,123 directed edges, converging at 30 epochs to form 8 GNN embeddings. (p. 7)[^original]  
  <sub>anchor: "The VAEs were successfully trained on a subset of 7 numerical features"</sub>
- **descriptive / method**: Embeddings were validated before fusion by analysing correlation between learned latent vectors and raw input attributes, which the authors say showed the models encoded distinct risk indicators meeting regulatory compliance requirements. (p. 8)[^original]  
  <sub>anchor: "This process demonstrates that the models successfully encoded distinct risk indicators"</sub>
- **descriptive / finding or result**: Grid search showed One-Class SVM performance was highly sensitive to Nu; the optimal configuration was Nu = 0.01 and Gamma = 0.1, with validation AP 0.8537 and validation ROC 0.8517. (p. 8)[^original]  
  <sub>anchor: "The optimal configuration was identified as _𝜈_ = 0 _._ 01 and _𝛾_ = 0.1, achieving a validation AP of 0.8537 and validation ROC 0.8517"</sub>
- **descriptive / finding or result**: On test data the tuned One-Class SVM achieved precision @ 5% of 99.26%, AP of 0.8505 and ROC-AUC of 0.8458, slightly below its validation scores, which the authors say confirms generalisation to unseen data. (p. 8)[^original]  
  <sub>anchor: "achieving a final precision @ 5% of 99.26%, AP of 0.8505 and ROC-AUC of 0.8458 on test result"</sub>
- **descriptive / data or feature**: Table 5 describes learned embeddings: VAE_embedding_2 (correlation with customer_StdDev +0.11) and VAE_embedding_7 (customer_StdDev −0.27) both relate to customer transaction deviation history and capture volatility; GNN_embedding_1 (Transaction_Count +1.00) relates to abnormal activity; GNN_embedding_2 (Volume_Variability +0.89) and GNN_embedding_0 (Volume_Variability +0.88) relate to layering and/or structuring. (p. 8)[^original]  
  <sub>anchor: "GNN_embedding_1|Transaction_Count (+1.00)|Abnormal activity"</sub>
- **descriptive / data or feature**: Table 6 compares Isolation Forest, OCSVM and LOF: ROC-AUC 0.7826, 0.8388 and 0.8459; AP 0.6742, 0.8478 and 0.8019; Precision @ 5% 0.8492, 0.9963 and 0.8976; Recall @ 95% 0.1095, 0.1285 and 0.1157; F1 0.6496, 0.7361 and 0.7409 respectively. (p. 8)[^original]  
  <sub>anchor: "|ROC-AUC|0.7826|0.8388|0.8459|"</sub>

## 3.5. Impact of feature fusion (ablation study)

- **descriptive / finding or result**: Table 8 (5-fold CV on optimised features): full hybrid model reported as N/A; without GNN embeddings AUC 0.8560 ± 0.0037 and AP 0.8737 ± 0.0028; without VAE embeddings AUC 0.7973 ± 0.0071 and AP 0.8158 ± 0.0060; without rule features AUC 0.7858 ± 0.0100 and AP 0.7711 ± 0.0082. (p. 8)[^original]  
  <sub>anchor: "|w/o GNN Embeddings|0.8560 ± 0.0037|0.8737 ± 0.0028|"</sub>
- **descriptive / finding or result**: Table 7 (leave-one-group-out) reports the full model with 9 features (AP 0.8505, ROC-AUC 0.8458, F1 0.7614); removing GNN embeddings (6 features) gave AP 0.8685, ROC-AUC 0.8622, F1 0.7924 and impact −2.12%; removing VAE embeddings (7 features) gave AP 0.8524, ROC-AUC 0.8496, F1 0.7601 and impact −0.22%; removing rule features (5 features) gave AP 0.7188, ROC-AUC 0.7053, F1 0.6030 and impact −15.48%. (p. 8)[^original]  
  <sub>anchor: "|Rule-Features|5|0.7188|0.7053|0.6030|−15.48||"</sub>

## 3.8. Confusion metric analysis

- **descriptive / finding or result**: The confusion analysis reports true positives and 6,056 true negatives; the model rejected 1,275 rule-flagged transactions, reducing compliance noise, and flagged 536 transactions as novel anomalies missed by the rules, giving recall 0.69, precision 0.84 and F1 0.76. (p. 8)[^original]  
  <sub>anchor: "the model flagged 536 transactions as novel anomalies that were not captured by the rules"</sub>
- **descriptive / finding or result**: The authors state that the dynamic filtering strategy addressed the high false positive alert issue described in Demetis (2010). (p. 8)[^original]  
  <sub>anchor: "Using the dynamic filtering strategy, the OCSVM effectively addressed the issue of high false positive alerts described in Demetis (2010)"</sub>

## 3.9. SHAP explanations

- **descriptive / finding or result**: Fig. 5 shows divergence between the hybrid OCSVM and rule-based heuristics; the model strongly aligns with baseline rules on 2,890 transactions. The confusion matrix uses an optimal threshold of 0.2983. (p. 8)[^original]  
  <sub>anchor: "The analysis shows that our model strongly aligns with the baseline rules on 2890 transactions"</sub>
- **descriptive / finding or result**: Fig. 6 SHAP analysis shows each of the 9 features' overall impact; fused VAE, GNN and rule-based embeddings contribute significantly to anomaly decisions. (p. 9)[^original]  
  <sub>anchor: "from VAE, GNN, and rule-based contribute significantly to the model’s anomaly decisions"</sub>

## Table 9

- **descriptive / finding or result**: Grid search results: lower Nu values yielded higher average precision, which the authors say confirms the high quality of the non-flagged training set. (p. 9)[^original]  
  <sub>anchor: "Lower _𝜈_ values yielded higher average precision, confirming the high quality of the non-flagged training set."</sub>

## 4.1. Addressing the limitation of ground truth validation

- **descriptive / limitation**: Confirmed Suspicious Activity Reports are unavailable due to confidentiality, so proxy labels are needed in testing, which the authors say introduces circular evaluation. (p. 9)[^original]  
  <sub>anchor: "the unavailability of confirmed Suspicious Activity Reports (SARs) due to confidentiality, necessitating the use of proxy labels during the testing phase, which introduces circular evaluation"</sub>
- **descriptive / finding or result**: The authors argue the semi-supervised design, training OCSVM only on non-flagged transactions to learn legitimate behaviour, addresses circularity; the model found 536 novel anomalies missed by rules and rejected 1,275 false-positive alerts. (p. 9)[^original]  
  <sub>anchor: "where the model identified 536 novel anomalies missed by the rules thus no 100% alignment with the rules, and rejected 1275 false-positive alerts"</sub>
- **descriptive / finding or result**: SHAP analysis is said to confirm that deep learning embeddings contribute significant decision weight orthogonal to rule-based features. (p. 9)[^original]  
  <sub>anchor: "the SHAP explainability analysis confirms that deep learning embeddings contribute significant decision weight orthogonal to rule-based features"</sub>

## 4.2. Data understanding and the need for deep learning embeddings

- **descriptive / case example**: The framework was tested by a Kenyan financial institution to assess scalability; on the Intel Core i7/16 GB environment it processed a batch of 300,000 transactions in under 5 minutes, about 1,000 transactions per second. (p. 9)[^original]  
  <sub>anchor: "the system processed a batch of 300,000 transactions in under 5 min, equating to a throughput of 1000 transactions per second (TPS)"</sub>
- **descriptive / data or feature**: The deployed AML system comprises a front page with login, a welcome page, top alerts, high-priority alerts, new alerts and all alerts; users upload a batch transaction CSV file that is scored by a trained model using 9 features from GNN, VAE and rule-based systems, then ranked and saved. (p. 9)[^original]  
  <sub>anchor: "The input section involves uploading a batch transaction CSV file"</sub>

## 3.10. Operational efficiency analysis

- **descriptive / finding or result**: Cross-border transfers show a heavily tailed distribution (skewness above 10) and a sparse network; heuristic rules flagged 39.72% of transactions as anomalies. (p. 9)[^original]  
  <sub>anchor: "The EDA reveals that cross-border transfers are characterised by a highly tailed distribution"</sub>
- **descriptive / limitation**: Limitations of the rule-based AML system include many false positive alerts, inability to detect complex laundering schemes, and rigidity against new threats, per Oztas et al. (2024b). (p. 10)[^original]  
  <sub>anchor: "The limitations of the rule-based AML system include the generation of a high number of false positive alerts"</sub>
- **descriptive / finding or result**: The authors find VAE and GNN embeddings compress high-variance transaction amounts into a dense Gaussian latent space and aggregate neighbour statistics into a dense topology embedding, which they say addresses the rule-based limitations. (p. 10)[^original]  
  <sub>anchor: "compressing the highvariance transaction amounts into a dense gaussian latent space"</sub>

## 4.3. The feature fusion strategy

- **descriptive / method**: The concatenated fusion strategy (Section 2.3) is credited with success; mutual information filtering kept only features carrying risk signals: rule features, VAE temporal movements and GNN structuring signals. (p. 10)[^original]  
  <sub>anchor: "By employing the mutual information filtering method, we ensured the final input features contained only the risk signals"</sub>
- **descriptive / finding or result**: The authors argue feature reduction prevented the curse of dimensionality from diluting Euclidean distances used by the RBF kernel, allowing a tighter decision boundary. (p. 10)[^original]  
  <sub>anchor: "This feature reduction prevented the curse of dimensionality from diluting the Euclidean distance metrics used by the RBF kernel"</sub>
- **descriptive / finding or result**: SHAP analysis (Fig. 6) shows the model shifts reliance dynamically across the 9 feature views, which the authors say corroborates multi-view learning reducing uncertainty in anomaly detection. (p. 10)[^original]  
  <sub>anchor: "the model dynamically shifts reliance between these 9 views"</sub>
- **descriptive / finding or result**: The ablation study is said to show the hybrid fusion achieved superior results to its individual components. (p. 10)[^original]  
  <sub>anchor: "the ablation study in 3.5 empirically confirms that our hybrid architecture fusion strategy achieved superior results"</sub>
- **descriptive / finding or result**: SHAP highlights Log_Trans_Amount (rule) as the strongest global predictor, Amount_Difference_From_Avg (rule) as a critical behavioural trigger, and VAE_Embedding_7 as consistently among the top features capturing non-linear spending variance. (p. 10)[^original]  
  <sub>anchor: "Log_Trans_Amount (Rule): High transaction values are the strongest global predictor of risk."</sub>
- **descriptive / method**: The authors conclude that a simple concatenation process preserved orthogonal risk signals from deep learning embeddings. (p. 10)[^original]  
  <sub>anchor: "Therefore a simple concatenation process adopted led to the preservation of the orthogonal risk signals"</sub>

## 4.4. The superiority of boundary learning (OCSVM)

- **descriptive / finding or result**: OCSVM's Precision @ 5% of 99.63% exceeded Isolation Forest (83.99%) and Local Outlier Factor (89.76%) on the optimised feature space. (p. 10)[^original]  
  <sub>anchor: "The main contribution of this study is the superior precision @5% performance of One-Class SVM by 99.63% over Isolation Forest (83.99%) and Local Outlier Factor(89.76%)"</sub>
- **descriptive / finding or result**: The authors conclude that for financial data with dense, clustered normal manifolds, boundary-based methods trained on non-flagged data outperform partition-based ensembles. (p. 10)[^original]  
  <sub>anchor: "boundary-based methods trained on non-flagged data outperform partition-based ensembles"</sub>
- **descriptive / finding or result**: Isolation Forest struggled to define the normal boundary as tightly; the authors suggest the legitimate behavioural manifold is dense and clustered, favouring SVM over tree-based partitioning when only non-flagged data is available. (p. 11)[^original]  
  <sub>anchor: "This suggests that the latent behavioural manifold of legitimate customers is dense and clustered"</sub>
- **descriptive / finding or result**: LOF achieved the overall AUC-ROC of 0.8459; the authors attribute this to its density-based comparison with k-nearest neighbours, which they suggest ranks deviations higher in a high-dimensional fused space. (p. 11)[^original]  
  <sub>anchor: "The Local Outlier Factor (LOF) achieved the overall AUC-ROC of 0.8459"</sub>

---

[previous part](digest-001.md) | [source overview](overview.md) | [next part](digest-003.md)

[^original]: Academic publisher / repository, "Hybrid deep learning for anti-money laundering: Unsupervised detection of emerging schemes via feature fusion and explainable artificial intelligence" (2026-02-25). https://doi.org/10.1016/j.mlwa.2026.100856
