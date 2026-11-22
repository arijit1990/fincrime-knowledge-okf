---
type: Source Digest
title: 'Hybrid deep learning for anti-money laundering: Unsupervised detection of emerging schemes via feature fusion and explainable artificial intelligence - part 1 of 3 (pp. 1-5)'
description: 'Verified paraphrased digest, pp. 1-5: Machine Learning with Applications > Hybrid deep learning for anti-money laundering: Unsupervised detection of emerging schemes via feature fusion and explainable artificial intelligence'
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
  resource: https://doi.org/10.1016/j.mlwa.2026.100856
  title: 'Hybrid deep learning for anti-money laundering: Unsupervised detection of emerging schemes via feature fusion and explainable artificial intelligence'
  author: org:academic_publisher
  last_modified: '2026-02-25T00:00:00Z'
digest_points: 92
---

# Hybrid deep learning for anti-money laundering: Unsupervised detection of emerging schemes via feature fusion and explainable artificial intelligence (digest)

[source overview](overview.md) | [next part](digest-002.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (pp. 1-5) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **academic finding**.

## Abstract

- **descriptive / context**: The paper says traditional rule-based AML transaction monitoring suffers from high false-positive rates and rigidity in detecting complex emerging risk, and that this prompted changes to FATF Recommendation 16 mandating advanced systems for detecting laundering in cross-border payments. (p. 1)[^original]  
  <sub>anchor: "Traditional rule-based anti-money laundering (AML) transaction monitoring systems suffer from high falsepositive rates and rigidity"</sub>
- **descriptive / method**: The study developed a hybrid framework combining VAE-learned behavioural latent factors, GNN-captured relational network signals and rule-based heuristics for anomaly detection. (p. 1)[^original]  
  <sub>anchor: "This study developed a hybrid framework integrating VAE-learned behavioural latent factors, GNN-captured relational network signals"</sub>
- **descriptive / finding or result**: The model was evaluated on 54,258 real-world cross-border transaction records from an East African commercial bank. (p. 1)[^original]  
  <sub>anchor: "The model was evaluated on 54,258 real-world cross-border transaction records from an East African commercial bank."</sub>
- **descriptive / finding or result**: The One-Class SVM, tuned by grid search, was reported as superior to Isolation Forest and Local Outlier Factor benchmarks, with a precision of 99.63% in the top 5% of prioritised alerts. (p. 1)[^original]  
  <sub>anchor: "The One-Class SVM, optimised via a rigorous grid search proved superior compared to Isolation Forest and Local Outlier Factor benchmark"</sub>
- **descriptive / finding or result**: Independent validation by a Kenyan financial institution reported batch processing of 1000 transactions per second on standard hardware (Intel Core i7, 16 GB RAM) and efficient high-priority alert triage. (p. 1)[^original]  
  <sub>anchor: "Independent validation by a Kenyan financial institution confirms a batch processing speed of 1000 transactions per second"</sub>
- **descriptive / method**: Shapley additive explanations were used to provide interpretability of feature contributions to model performance. (p. 1)[^original]  
  <sub>anchor: "Shapley additive explanations analysis further provided the interpretability of the feature contribution to the model performance."</sub>
- **descriptive / finding or result**: The authors claim integrating rule-based features with deep-learning embeddings improves compliance efficiency and offers a pathway for resource-constrained institutions to meet FATF demands upcoming in 2030. (p. 1)[^original]  
  <sub>anchor: "proven pathway for resource-constrained financial institutions to comply with FATF regulatory demands upcoming in 2030."</sub>

## 1. Introduction

- **descriptive / context**: The paper cites UNODC (2019) estimates that illicit money flows represent between 2% and 5% of global GDP, amounting to $800 billion to $2 trillion annually. (p. 1)[^original]  
  <sub>anchor: "Data estimates suggest the illicit money flows represent between 2% and 5% of global GDP, amounting to $800 billion to $2 trillion annually"</sub>
- **descriptive / context**: Developing countries reportedly lost approximately $6.6 trillion between 2003 and 2012 to financial crime, according to Kar and Spanjers (2015). (p. 1)[^original]  
  <sub>anchor: "Developing countries alone lost approximately $6.6 trillion between 2003 and 2012 to financial crime"</sub>
- **descriptive / context**: Digital payment systems, instant payments, digital currencies and virtual assets have complicated the fight against financial crime, enabling anonymity across jurisdictions while increasing financial inclusion. (p. 1)[^original]  
  <sub>anchor: "While these new technologies increase financial inclusion, they also enable criminals to operate with increased anonymity across jurisdictions."</sub>
- **descriptive / context**: Jurisdictions have implemented AML, CTF and CPF laws requiring financial and designated non-financial institutions to establish customer due diligence measures and prompt reporting of suspicious transactions. (p. 1)[^original]  
  <sub>anchor: "requiring financial institutions and designated non-financial institutions to establish measures on customer due diligence and prompt reporting of suspicious transactions"</sub>
- **descriptive / context**: Traditional AML systems, widely used by industry, rely heavily on rule-based approaches, are rigid, and generate many false-positive alerts, increasing compliance cost (Demetis, 2010). (p. 1)[^original]  
  <sub>anchor: "Traditional AML systems, while currently widely used by industry players, rely heavily on rule-based approaches"</sub>

## Abstract

- **descriptive / context**: The hybrid framework was evaluated on 54,258 real-world cross-border transaction records from an East African commercial bank, with the One-Class SVM outperforming Isolation Forest and Local Outlier Factor benchmarks. (p. 1)[^original]  
  <sub>anchor: "The model was evaluated on 54,258 real-world cross-border transaction records"</sub>
- **descriptive / finding or result**: The One-Class SVM, optimised by grid search, achieved a precision of 99.63% in the top 5% of prioritised alerts. (p. 1)[^original]  
  <sub>anchor: "achieving a precision of 99.63% in the top 5% of prioritised alerts."</sub>
- **descriptive / finding or result**: Independent validation by a Kenyan financial institution reported batch processing of 1000 transactions per second on standard hardware (Intel Core i7, 16 GB RAM). (p. 1)[^original]  
  <sub>anchor: "confirms a batch processing speed of 1000 transactions per second on standard computer hardware"</sub>
- **descriptive / finding or result**: Table 1 compares the proposed hybrid framework with traditional rule-based and standalone ML approaches across detection logic, rule features, VAE and GNN embeddings, interpretability and adaptability. (p. 1)[^original]  
  <sub>anchor: "Summary of the AML detection approaches."</sub>

## 1. Introduction

- **descriptive / case example**: The paper notes Turksen et al. (2024) argued rule-based tools are ineffective despite giving audit trails, citing the recent FATF grey-listing of Kenya for weak financial crime compliance strategies. (p. 2)[^original]  
  <sub>anchor: "Turksen et al. (2024) argued that rule-based tools are ineffective despite increasing the compliance transparency by providing the audit trails"</sub>
- **descriptive / finding or result**: Islam et al. (2024) reported a fraud detection system with precision accuracy of 0.99 compared with random forest, decision tree, naive Bayes and k-nearest neighbour models. (p. 2)[^original]  
  <sub>anchor: "Islam et al. (2024) developed a fraud detection system achieving an accuracy of 0.99 in precision compared to the traditional models"</sub>
- **descriptive / context**: The paper states that FATF's June 2025 Plenary updated Recommendation 16 on the safety and security of cross-border payments to facilitate detection of financial crime. (p. 2)[^original]  
  <sub>anchor: "Financial Action Task Force (2025) June 2025 Plenary updated recommendation 16 on increased safety and security of cross-border payments"</sub>
- **descriptive / finding or result**: Lokanan (2024) reported random forest accuracy of 0.89 against MCC 0.79, gradient descent classifier 0.82 and decision tree 0.86 on the PaySim dataset of 1,048,575 records. (p. 2)[^original]  
  <sub>anchor: "Random forest models, for example, as examined by Lokanan (2024) had shown promising results in fraud detection with a performance accuracy of 0.89"</sub>
- **descriptive / limitation**: Supervised models are reportedly hampered by scarce labelled data and high class imbalance in financial crime data; unsupervised methods may overlook complex transaction relationships. (p. 2)[^original]  
  <sub>anchor: "the effectiveness of these supervised models is hampered by the scarcity of labelled data and high class imbalance in financial crime data"</sub>
- **descriptive / finding or result**: Cardoso et al. (2022) reported the laundrograph GNN model outperformed MLP and light GBM on bank data with 66 features, with AUC improved by 12 points. (p. 2)[^original]  
  <sub>anchor: "the laundrograph model outperformed other models, such as multilayer perceptron (MLP) and light gradient boosting machine (GBM)"</sub>
- **descriptive / finding or result**: Eddin et al. (2021) reported a model on a real bank dataset of 400,000 accounts that cut false positives by 80% and detected over 90% of true positive alerts. (p. 2)[^original]  
  <sub>anchor: "found that the model reduced false positives by 80% and detected over 90% of true positive alerts."</sub>
- **descriptive / finding or result**: Poon et al. (2025) proposed LineMVGNN, a line-graph-assisted multi-view GNN, reported to outperform other methods by capturing money flow in transaction networks. (p. 2)[^original]  
  <sub>anchor: "Poon et al. (2025) proposed a line-graph-assisted multi-view graph neural networks (LineMVGNN) model"</sub>
- **descriptive / finding or result**: Talukder et al. (2024) reported a hybrid ensemble achieving 100% AUC and accuracies of 99.66%, 99.66%, 99.73%, 98.56% and 99.79% for the ENS, DT, RF, MLP and KNN models. (p. 2)[^original]  
  <sub>anchor: "achieved a 100% AUC and modest accuracy rate of 99.66%, 99.66%,99.73%, 98.56%, and 99.79% for the ENS, DT, RF, MLP, and KNN models"</sub>
- **descriptive / finding or result**: Esenogho et al. (2022) reported a neural network ensemble with LSTM and adaptive boosting achieving sensitivity of 0.996 and specificity of 0.998. (p. 2)[^original]  
  <sub>anchor: "reported impressive scores on the model performance with a sensitivity of 0.996 and a specificity of 0.998."</sub>
- **descriptive / finding or result**: Jensen and Iosifidis (2023) reported a rule-plus-deep-learning system that cut false positive rates by 33.3%, raised 75 new alerts, led to 26 new clients being reported at Spar Nord Bank, and retained over 98% of false positive alerts. (p. 2)[^original]  
  <sub>anchor: "found that their model reduced false positive rates by 33.3%"</sub>
- **descriptive / limitation**: Existing hybrid approaches often focus on specific crime typologies and lack comprehensive feature fusion, and explainability (e.g. SHAP) is often lacking in some models. (p. 2)[^original]  
  <sub>anchor: "However, these approaches often focus on specific crime typologies and lack comprehensive feature fusion."</sub>
- **descriptive / context**: The FATF reports that new technologies including AML monitoring systems enhance AML/CFT compliance through speed, accuracy and risk profiling, but its 2021 report identified gaps such as explainability and adaptability. (p. 2)[^original]  
  <sub>anchor: "through enhanced speed, accuracy, and risk profiling capabilities."</sub>
- **descriptive / context**: The authors state their model is the first to fuse rule-based features with VAE latent behaviours and GNN relational networks, using a semi-supervised One-Class SVM with SHAP for interpretability. (p. 2)[^original]  
  <sub>anchor: "Our framework is the first to fuse rulebased features with VAE-learned latent transaction behaviours and GNN-captured relational networks"</sub>
- **descriptive / context**: The amended FATF Recommendation 16 (the travel rule) requires financial institutions to acquire and adopt advanced systems to protect against errors and fraud, standardise payment messages and clarify roles in the payment ecosystem. (p. 2)[^original]  
  <sub>anchor: "The amended recommendation requires financial institutions to acquire and adopt advanced systems to protect against errors and fraud"</sub>
- **descriptive / context**: The amended FATF Recommendation 16 requires financial institutions to acquire and adopt advanced systems to protect against errors and fraud, standardise payment messages, and clarify roles in the payment ecosystem. (p. 2)[^original]  
  <sub>anchor: "The amended recommendation requires financial institutions to acquire and adopt advanced systems"</sub>
- **descriptive / context**: The authors state the FATF Recommendation 16 amendment, updated at the June 2025 Plenary, shifts reliance away from traditional AML systems and creates demand for advanced AML systems. (p. 2)[^original]  
  <sub>anchor: "This regulatory recommendation suggests a shift in reliance on traditional AML systems"</sub>
- **descriptive / finding or result**: The validating Kenyan institution reportedly observed processing of more than 300,000 transactions in under five minutes while maintaining alert precision and prioritisation. (p. 3)[^original]  
  <sub>anchor: "than 300,000 transactions under five minutes while maintaining the dynamic alert precision and prioritisation"</sub>
- **descriptive / context**: Table 1 compares traditional rule-based AML, standalone ML (GNN or VAE only) and the proposed hybrid framework across detection logic, rule features, embeddings, interpretability and adaptability. (p. 3)[^original]  
  <sub>anchor: "Summary of the AML detection approaches."</sub>

## 2. Methodology

- **descriptive / method**: The methodology covers data collection and preprocessing, feature engineering, the fusion strategy, semi-supervised anomaly detection modelling and operational deployment. (p. 3)[^original]  
  <sub>anchor: "The remainder of this section is organised into: data collection and preprocessing, feature engineering, the fusion strategy"</sub>

## 2.1. Data collection and preprocessing

- **descriptive / data or feature**: The data came from an anonymised East African bank processing cross-border payments: 54,258 SWIFT-based payment metadata records recorded over 9 months in 2024. (p. 3)[^original]  
  <sub>anchor: "The dataset comprised 54,258 SWIFT-based cross-border payment transaction metadata recorded over 9 months in 2024."</sub>
- **descriptive / data or feature**: Account numbers for originator and beneficiary were removed, while transaction reference numbers, currencies, amounts, value date, anonymised names, beneficiary country and bank identifier were retained. (p. 3)[^original]  
  <sub>anchor: "The original dataset variables, such as the account numbers for the originator and beneficiary, were deducted"</sub>
- **descriptive / method**: Records with missing critical fields such as customer details and transaction reference numbers were removed, leaving 53,783 records. (p. 3)[^original]  
  <sub>anchor: "resulting in 53,783."</sub>
- **descriptive / method**: Amounts were converted to USD using fixed exchange rates for 16 currencies and log-transformed to normalise skewed distributions and address heteroscedasticity. (p. 3)[^original]  
  <sub>anchor: "the transaction amounts were converted to USD equivalents using fixed exchange rates for the 16 currencies and log-transformed"</sub>
- **descriptive / method**: Exploratory data analysis was used to identify outliers and temporal features, informing further feature engineering. (p. 3)[^original]  
  <sub>anchor: "our EDA identified temporal features and outliers, informing further feature engineering."</sub>

## 2.2.1. Rule-based features

- **descriptive / method**: Seven features were engineered from the dataset across temporal, behavioural and risk dimensions, with red flags defined in consultation with AML compliance officers. (p. 3)[^original]  
  <sub>anchor: "The seven features were engineered directly from the dataset, and they were involved in the derivation of statistical and temporal features categorised in three dimensions."</sub>

## 2.1. Data collection and preprocessing

- **descriptive / data or feature**: The dataset comprised 54,258 SWIFT-based cross-border payment transaction records recorded over 9 months in 2024 from an anonymised East African bank, reduced to 53,783 after cleaning of missing critical records. (p. 3)[^original]  
  <sub>anchor: "The dataset comprised 54,258 SWIFT-based cross-border payment transaction metadata recorded over 9 months in 2024."</sub>
- **descriptive / method**: Transaction amounts were converted to USD equivalents using fixed exchange rates for 16 currencies and log-transformed to normalise skew and address heteroscedasticity. (p. 3)[^original]  
  <sub>anchor: "the transaction amounts were converted to USD equivalents using fixed exchange rates for the 16 currencies"</sub>

## 1. Introduction

- **descriptive / method**: The authors claim to map learned embeddings to specific AML typologies to enhance the explainability of latent features, and state SHAP values highlight the fairly distributed feature contribution to decisions. (p. 3)[^original]  
  <sub>anchor: "We operationalise the interpretation of deep learning by mapping the learned embeddings to specific AML typologies"</sub>

## 2.2.1. Rule-based features

- **descriptive / definition**: Table 2 defines Days_Since_Previous as the time delta between a transaction and the previous one for the same ordering party, intended to capture rapid-fire smurfing or dormancy. (p. 4)[^original]  
  <sub>anchor: "Time delta between transaction _𝑡𝑖_ and _𝑡𝑖_−1 for the same ordering party"</sub>
- **descriptive / definition**: Log_Trans_Amount is defined as log(1 + AmountUSD), used to normalise the heavy-tailed distribution for neural network stability. (p. 4)[^original]  
  <sub>anchor: "log(1 +AmountUSD). _Normalises_ _the_ _heavy-tailed_ _distribution_"</sub>
- **descriptive / definition**: Amt_Diff_From_Avg is the absolute deviation of a transaction amount from the customer's historical mean, quantifying abnormality relative to customer history. (p. 4)[^original]  
  <sub>anchor: "Absolute deviation from historical mean"</sub>
- **descriptive / definition**: Customer_StdDev is the standard deviation of the customer's history, capturing volatility, where high values indicate inconsistent or high-risk pass-through behaviour. (p. 4)[^original]  
  <sub>anchor: "Standard deviation (_𝜎_) of the customer’s history."</sub>
- **descriptive / definition**: High_Risk_Country is a binary flag set to 1 when the beneficiary country is on the OFAC list, described as a deterministic regulatory flag with high predictive influence. (p. 4)[^original]  
  <sub>anchor: "Binary flag (1) if Beneficiary Country ∈ (OFAC List)."</sub>
- **descriptive / definition**: Structuring_Flag is a binary flag set to 1 when multiple transactions occur for the same sender-receiver pair on the same date. (p. 4)[^original]  
  <sub>anchor: "Binary flag (1) if multiple transactions _Sender–Receiver pair on the same date."</sub>
- **descriptive / method**: Red flags were applied to each transaction to give yes/no or 1/0 indicators of suspicious transactions, serving as the baseline for regulatory reporting and filter for building the training dataset. (p. 4)[^original]  
  <sub>anchor: "The red flags were used to evaluate each transaction, leading to yes"</sub>
- **descriptive / method**: Binary risk flags were engineered from the OFAC high-risk jurisdiction list and structuring typologies such as split payments below the $10,000 threshold. (p. 4)[^original]  
  <sub>anchor: "Binary flags were engineered based on the OFAC high-risk jurisdiction list and structuring typologies such as split payments below the $10,000 threshold."</sub>
- **descriptive / finding or result**: The authors state risk flags strongly influence classification, acting as dominant predictors of known typologies, consistent with Lokanan (2024) on heuristic features ranking as top contributors. (p. 4)[^original]  
  <sub>anchor: "It is important to note that the risk flags exert a strong influence on the classification of suspicious transactions"</sub>

## 2.2.2. Heuristic features for ground truth proxy

- **descriptive / method**: Because no labelled data from verified suspicious activity reports was available, a heuristic target variable is_rule_flag was created, set to 1 for transactions meeting rule flags. (p. 4)[^original]  
  <sub>anchor: "With the absence of labelled data from a verified suspicious activity report for this model"</sub>
- **descriptive / finding or result**: Applying the rule flags resulted in 20,823 transactions (38.72%) being flagged as is_rule_flag = 1. (p. 4)[^original]  
  <sub>anchor: "resulting in 20,823 (38.72%) transactions being flagged."</sub>
- **descriptive / limitation**: The authors acknowledge the rule-based proxy does not represent true suspicion, but it served as a baseline for evaluating alignment with and augmentation of rule-based systems. (p. 4)[^original]  
  <sub>anchor: "While the proxy representing the known rule logic has limitations of not representing true suspicion"</sub>

## 2.2.3. Variational autoencoders (VAE)

- **descriptive / method**: VAEs were used to capture hidden non-linear transaction behaviour representations that rule-based features might miss, taking the seven preprocessed numerical features as input. (p. 4)[^original]  
  <sub>anchor: "The seven preprocessed numerical features acted as input chosen on their relevance to monitoring laundering schemes"</sub>
- **descriptive / method**: The VAE encoder compressed inputs through dense layers of 32 then 16 units with ReLU activations and batch normalisation to an 8-dimensional latent space via mean and log variance. (p. 4)[^original]  
  <sub>anchor: "The encoder compressed the input features through dense layers of 32 units to 16 units with ReLU activations and batch normalisations to an 8-dimensional latent space"</sub>
- **descriptive / method**: KL divergence loss clipping was incorporated into the sampling layer for stability; the decoder mirrors the encoder to reconstruct the 7 input features. (p. 4)[^original]  
  <sub>anchor: "Kullback– Leibler (KL) divergence loss clipping was incorporated into the sampling layer for stability."</sub>
- **descriptive / finding or result**: The VAE reached a validation loss of 2.7602 over 30 epochs, which the authors interpret as the 8-dimensional latent embeddings encoding the salient variance of the input. (p. 4)[^original]  
  <sub>anchor: "achieving a validation loss of 2.7602) for the 30 epochs"</sub>
- **descriptive / method**: VAE training combined reconstruction error and KL divergence loss, following Higgins et al. (2017) for balancing regularisation and latent space collapse, with the loss managed within the sampling layer. (p. 4)[^original]  
  <sub>anchor: "The VAE training involved a combination of the loss function with the reconstruction error and KL divergence"</sub>

## 2.2.4. Graph neural networks (GNNs)

- **descriptive / method**: The GNN captures the transaction network for relational anomaly detection, such as layered or circular transactions, modelling structure between remitters and beneficiaries. (p. 4)[^original]  
  <sub>anchor: "The GNN captures the transactional network for relational anomaly detection, such as layered or circular transactions"</sub>
- **descriptive / data or feature**: A directed graph built with NetworkX mapped senders and beneficiaries to 31,108 unique party nodes, with 27,123 unique directed edges weighted by USD amount and transaction frequency. (p. 4)[^original]  
  <sub>anchor: "The graph mapped the sender (Ordinary (sender) party name) and the beneficiary (Beneficiary (receiver) party name)"</sub>
- **descriptive / method**: The GNN embedding model was a feed-forward neural network in PyTorch, trained for 30 epochs to minimise mean squared error, with training loss falling from 1.49 to 0.17 and yielding 8-dimensional embeddings. (p. 4)[^original]  
  <sub>anchor: "The training loss decreased significantly from an initial 1.49 to 0.17, deriving a 8-dimensional GNN embeddings"</sub>
- **descriptive / data or feature**: Table 3 reports correlations of GNN embeddings 0 to 7 with average amount, transaction count and volume variability; for example, GNN_Embedding_0 has 0.87, 0.00 and 0.88 respectively. (p. 4)[^original]  
  <sub>anchor: "GNN_Embedding_0|0.87|0.00|0.88|"</sub>

## 2.3. Feature fusion and selection strategy

- **descriptive / method**: Seven rule flags, eight VAE latent embeddings and eight GNN embeddings were concatenated into a unified 23-feature vector per transaction, with standardisation applied before fusion. (p. 4)[^original]  
  <sub>anchor: "This resulted in a unified 23 feature vector"</sub>

## 2.2.1. Rule-based features

- **descriptive / definition**: Table 2 defines the Days_Since_First feature as account tenure, computed as the current date minus the minimum active date, intended to separate established customers from burn-and-churn mule accounts. (p. 4)[^original]  
  <sub>anchor: "Distinguishes established customers from burn-and-churn mule accounts."</sub>
- **descriptive / definition**: Table 2 defines Log_Trans_Amount as the log of one plus the USD amount, normalising the heavy-tailed distribution of transaction values for neural network stability. (p. 4)[^original]  
  <sub>anchor: "Normalises the heavy-tailed distribution of transaction values for neural network stability"</sub>
- **descriptive / definition**: Table 2 defines Amt_Diff_From_Avg as the absolute deviation of a transfer amount from the customer's historical mean, quantifying how abnormal a transfer size is relative to customer history. (p. 4)[^original]  
  <sub>anchor: "Quantifies the abnormality of a transfer size relative to the customer's history."</sub>
- **descriptive / definition**: Table 2 defines Customer_StdDev as the standard deviation of the customer's history, capturing volatility, where high values indicate inconsistent or high-risk pass-through behaviour. (p. 4)[^original]  
  <sub>anchor: "high σ indicates inconsistent or high-risk pass-through behaviour."</sub>
- **descriptive / definition**: High_Risk_Country is a binary flag set to 1 when the beneficiary country appears on the OFAC list, described as a deterministic regulatory flag with high predictive influence. (p. 4)[^original]  
  <sub>anchor: "Binary flag (1) if Beneficiary Country ∈ (OFAC List)."</sub>
- **descriptive / definition**: Structuring_Flag is a binary flag set to 1 when multiple transactions occur between the same sender and receiver pair on the same date. (p. 4)[^original]  
  <sub>anchor: "Binary flag (1) if multiple transactions Sender–Receiver pair on the same date."</sub>
- **descriptive / method**: Binary risk flags were engineered from the OFAC high-risk jurisdiction list and from structuring typologies such as split payments below the USD 10,000 threshold. (p. 4)[^original]  
  <sub>anchor: "Binary flags were engineered based on the OFAC high-risk jurisdiction list and structuring typologies"</sub>
- **descriptive / finding or result**: The authors state that risk flags strongly influence classification of suspicious transactions because they act as dominant predictors for known money laundering typologies. (p. 4)[^original]  
  <sub>anchor: "the risk flags exert a strong influence on the classification of suspicious transactions"</sub>
- **descriptive / context**: Lokanan (2024) is cited as finding that heuristic features such as transfer magnitude and regulatory flags consistently rank as top contributors in financial crime detection models. (p. 4)[^original]  
  <sub>anchor: "heuristic features such as transfer magnitude and regulatory flags consistently rank as top contributors"</sub>

## 2.2.2. Heuristic features for ground truth proxy

- **descriptive / method**: Lacking labelled data from verified suspicious activity reports, a heuristic target variable is_rule_flag was created, set to 1 for transactions meeting the predefined rule flags, yielding 20,823 (38.72%) flagged transactions. (p. 4)[^original]  
  <sub>anchor: "resulting in 20,823 (38.72%) transactions being flagged."</sub>
- **descriptive / limitation**: The authors acknowledge the rule-based proxy target has the limitation of not representing true suspicion, and served only as a baseline for evaluating alignment with rule-based systems. (p. 4)[^original]  
  <sub>anchor: "the proxy representing the known rule logic has limitations of not representing true suspicion"</sub>

## 2.2.3. Variational autoencoders (VAE)

- **descriptive / method**: The VAE encoder compressed seven input features through dense layers of 32 then 16 units with ReLU activations and batch normalisation into an 8-dimensional latent space, with KL divergence loss clipping in the sampling layer. (p. 4)[^original]  
  <sub>anchor: "The encoder compressed the input features through dense layers of 32 units to 16 units with ReLU activations"</sub>
- **descriptive / finding or result**: The VAE reached a validation loss of 2.7602 over 30 epochs, which the authors take to show the 8-dimensional latent embeddings encoded the salient variance of the input. (p. 4)[^original]  
  <sub>anchor: "achieving a validation loss of 2.7602) for the 30 epochs"</sub>

## 2.2.4. Graph neural networks (GNNs)

- **descriptive / method**: The transaction network was modelled as a directed graph built with NetworkX, mapping senders and beneficiaries to nodes, giving 31,108 unique transaction parties and 27,123 unique directed edges weighted by USD amount and frequency. (p. 4)[^original]  
  <sub>anchor: "The graph mapped the sender (Ordinary (sender) party name) and the beneficiary"</sub>
- **descriptive / finding or result**: The GNN embedding model, trained for 30 epochs to minimise mean squared error, reduced training loss from 1.49 to 0.17 and produced 8-dimensional GNN embeddings. (p. 4)[^original]  
  <sub>anchor: "The training loss decreased significantly from an initial 1.49 to 0.17"</sub>

## 2.3. Feature fusion and selection strategy

- **descriptive / context**: The authors note a high-dimensional space risks the curse of dimensionality, where irrelevant features may dilute detection, so a three-step filtration was implemented to prevent overfitting. (p. 5)[^original]  
  <sub>anchor: "thus the risk of ’curse of dimensionality’ where irrelevant features may dilute the detection abilities of the model"</sub>
- **descriptive / method**: Redundancy step: features with pairwise Pearson correlation coefficients above 0.95 were removed, eliminating 5 features. (p. 5)[^original]  
  <sub>anchor: "We employed a pairwise pearson correlation matrix and removed features with coefficients _>_ 0 _._ 95, eliminating 5 features."</sub>
- **descriptive / method**: Information gain step: mutual information between each feature and the heuristic target was calculated to measure discriminative power. (p. 5)[^original]  
  <sub>anchor: "The mutual information (MI) was calculated between each feature and the heuristic target"</sub>
- **descriptive / method**: Latent signal isolation step: a filter retaining features with mutual information between 0.1 and 0.4 was applied to discard weak signals; the exact cut-off symbol in the text is garbled. (p. 5)[^original]  
  <sub>anchor: "We applied a strict filter (0 _._ 1 ≤ MI ≤ 0 _._ 4) to discard weak signals"</sub>
- **descriptive / finding or result**: The three-step filtration reduced the initial 23-feature space to 9 features comprising a balanced mix of signals for the semi-supervised model. (p. 5)[^original]  
  <sub>anchor: "This design led to a reduction of the initial 23 high-dimension space to a set of 9 features"</sub>
- **descriptive / method**: The 7 rule flags, 8 VAE latent embeddings and 8 GNN embeddings were concatenated into a unified 23-feature vector per transaction. (p. 5)[^original]  
  <sub>anchor: "concatenating the three distinct feature set: the 7 engineered rule flags, the 8 VAE latent embeddings"</sub>
- **descriptive / method**: Simple concatenation was preferred because the One-Class SVM kernel learns non-linear feature relationships without manual weight assignment, standardisation of inputs removed scale dominance, and preserved feature columns support SHAP attribution. (p. 5)[^original]  
  <sub>anchor: "A Simple concatenation was preferred based on these factors."</sub>
- **descriptive / method**: Redundant features were removed using a pairwise Pearson correlation matrix, dropping features with coefficients above 0.95 and eliminating 5 features. (p. 5)[^original]  
  <sub>anchor: "We employed a pairwise pearson correlation matrix and removed features with coefficients"</sub>
- **descriptive / method**: Mutual information was computed between each feature and the heuristic target to measure each feature's discriminative power. (p. 5)[^original]  
  <sub>anchor: "The mutual information (MI) was calculated between each feature and the heuristic target"</sub>
- **descriptive / method**: A filter retaining features with mutual information between 0.1 and 0.4 discarded weak signals, reducing the 23-feature space to 9 features. (p. 5)[^original]  
  <sub>anchor: "We applied a strict filter (0 . 1 ≤ MI ≤ 0 . 4) to discard weak signals"</sub>

---

[source overview](overview.md) | [next part](digest-002.md)

[^original]: Academic publisher / repository, "Hybrid deep learning for anti-money laundering: Unsupervised detection of emerging schemes via feature fusion and explainable artificial intelligence" (2026-02-25). https://doi.org/10.1016/j.mlwa.2026.100856
