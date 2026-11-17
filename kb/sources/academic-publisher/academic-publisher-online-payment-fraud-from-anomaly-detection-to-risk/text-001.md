---
type: Source Text
title: 'Online payment fraud: from anomaly detection to risk management - part 1 of 3 (pp. 1-9)'
description: 'Verbatim extracted text, pp. 1-9: Online payment fraud: from anomaly detection to risk management > Open Access'
resource: https://link.springer.com/article/10.1186/s40854-023-00470-w
tags:
- academic_finding
- academic_paper
- global_academic
- model_governance
- model_validation
status: stable
source_id: academic-publisher-online-payment-fraud-from-anomaly-detection-to-risk
issuer: academic_publisher
issuer_name: Academic publisher / repository
jurisdictions:
- GLOBAL_ACADEMIC
tier: 3
instrument_type: academic_paper
normative_force: academic_finding
publication_date: '2023-03-12'
legal_status: unknown
part: 1
parts_total: 3
content_mode: full_text
generated:
  by: process:fincrime-kb-build
  at: '2026-11-17T12:21:45Z'
verified:
- by: process:kb-validate/verbatim-coverage
  at: '2026-11-17T12:21:45Z'
sources:
- id: original
  resource: https://link.springer.com/article/10.1186/s40854-023-00470-w
  title: 'Online payment fraud: from anomaly detection to risk management'
  author: org:academic_publisher
  last_modified: '2023-03-12T00:00:00Z'
---

# Online payment fraud: from anomaly detection to risk management

[source overview](overview.md) | [next part](text-002.md)

> Verbatim text extracted from the original (Academic publisher / repository, 2023-03-12), part 1 of 3, pp. 1-9. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **academic finding**.[^original]

[p. 1]

Vanini _et al. Financial Innovation (2023) 9:66_ https://doi.org/10.1186/s40854-023-00470-w

Financial Innovation

Paolo Vanini1* , Sebastiano Rossi2 , Ermin Zvizdic3 and Thomas Domenig4

*Correspondence: paolo.vanini@unibas.ch

> 1 University of Basel, Basel, Switzerland

2 Novartis AG, Basel, Switzerland

3 swissQuant Group, Zurich, Switzerland

## Online payment fraud: from anomaly detection to risk management


### Open Access


4 IT Couture, Zurich, Switzerland

Online banking fraud occurs whenever a criminal can seize accounts and transfer funds from an individual’s online bank account. Successfully preventing this requires the detection of as many fraudsters as possible, without producing too many false alarms. This is a challenge for machine learning owing to the extremely imbalanced data and complexity of fraud. In addition, classical machine learning methods must be extended, minimizing expected financial losses. Finally, fraud can only be combated systematically and economically if the risks and costs in payment channels are known. We define three models that overcome these challenges: machine learning-based fraud detection, economic optimization of machine learning results, and a risk model to predict the risk of fraud while considering countermeasures. The models were tested utilizing real data. Our machine learning model alone reduces the expected and unexpected losses in the three aggregated payment channels by 15% compared to a benchmark consisting of static if-then rules. Optimizing the machine-learning model further reduces the expected losses by 52%. These results hold with a low false positive rate of 0.4%. Thus, the risk framework of the three models is viable from a business and risk perspective.

#### Abstract


Keywords: Payment fraud risk management, Anomaly detection, Ensemble models, Integration of machine learning and statistical risk modelling, Economic optimization machine learning outputs

Fraud arises in the financial industry via numerous channels, such as credit cards, e-commerce, phone banking, checks, and online banking. Juniper Research (2020) reports that e-commerce, airline ticketing, money transfer, and banking services will cumulatively lose over $ 200 billion due to online payment fraud between 2020 and 2024. The increased sophistication of fraud attempts and the increasing number of attack vectors have driven these results. We focus on online and mobile payment channels and identity theft fraud (i.e., stealing an individual’s personal information to conduct fraud ) (Amiri and Hekmat 2021). The aim is to identify external fraudsters who intend to initiate payments in their interests. As fraudsters gain access to the payment systems as if they were the owners of the accounts, they cannot be identified based on the account access process. However, the fraudster behaves differently during a payment transaction

#### Introduction


[pp. 1-2]

> © The Author(s) 2023. Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http:// creat iveco mmons. org/ licen ses/ by/4. 0/.

than the account owner and/or the payment has unusual characteristics, such as an unusually high payment amount or transfer to an account in a jurisdiction that does not fit the life context and payment behavior of the customer. The assumption is that algorithms can detect anomalies in behavior during payment transactions.

West and Bhattacharya (2016), Abdallah et al. (2016), Hilal et al. (2021), and Ali et al. (2022) reviewed financial fraud. They found a low number of articles regarding online payment fraud. For example, Ali et al. (2022) cited 20 articles on financial statement fraud and 32 articles on credit card fraud, see Li et al. (2021) for credit card fraud detection. Online payment fraud was not listed. The reviews also clarified that many articles utilized aggregated characteristics. However, we emphasize that fraud in online payments can only be detected based on individual data, as such fraud can only be detected through the possible different behavior of the fraudster and the account holder during payments. As fraudsters learn how best to behave undetected over time, they adapt their behavior. Therefore, self-learning defense methods are expected to outperform staticrule-based algorithms. The correctness of the expectation was shown by Abdallah et al. (2016) and Hilal et al. (2021). Various machine-learning algorithms for fraud detection have been proposed in the literature, including decision trees, support vector machines, and logistic regression to neural networks. Aggarwal and Sathe (2017) discussed various methods for outlier ensembles, and Chandola et al. (2009) provided a taxonomy and overview of anomaly detection methods.

A common feature in many studies is imbalanced data (i.e., the low proportion of fraud events in the dataset, see Wei et al. 2013; Carminati et al. 2015; Zhang et al. 2022a; Singh et al. 2022). Risk detection involves detecting fraudulent transactions and stopping them before execution.

[pp. 2-3]

In addition to the efficiency of the algorithms, the data basis is an important reason for the differences in fraud-detection performance. While many studies have utilized either often less rich synthetic or Kaggle data, we were able to work with real data. Log files, which have substantial information content in our work, are hardly expected in Kaggle data. The difference in the data complexity is also reflected in the number of features. Singh et al. (2022) showed that the feature space consists of 31 features compared to our 147 features. Moreover, the proportion of fraudulent transactions in Singh et al. (2022) is more than a hundred times higher than in our case. Consequently, our data are much more unbalanced than any other study we know of, and the task of finding efficient fraud detection algorithms is more difficult.

However, limiting risk management to the optimal detection of anomalies does not ensure that losses caused by fraud are minimal. Optimal fraud detection can be economically suboptimal if, for example, it is efficient for small amounts of money but unsuccessful for large amounts. Thus, the machine learning outputs for risk identification must be optimized from an economic perspective. We call this optimization the triage model. Yet, neither fraud detection nor the triage model can provide an answer to the question of how large the losses in a payment channel are. Therefore, we develop a statistical risk model that considers the effects of countermeasures on loss potential. The risk model provides risk transparency and makes it possible to assess which measures in the fight against fraud in various payment channels make sense from an economic and risk perspective.

Literature on fraud risk models often refers to qualitative or assessment models for assessing fraud risk or risk assessment models (Sabu et al. 2021). We are not aware of any quantitative fraud risk management framework that explicitly considers the impact of the fraud detection process statistically in risk modelling. For organizational, procedural, and legal risk aspects, we refer to the literature. Montague’s (2010) book focuses on fraud prevention in online payments but does not consider machine learning and risk management in detail. The Financial Conduct Authority’s Handbook (FCA 2021) provides a full listing of the FCA’s legal instruments, particularly those relating to financial crime in financial institutions. Power (2013) highlights the difference between fraud and fraud risk from historical and business perspectives. Van Liebergen (2017) looks at “regtech” applications of machine learning in online banking. Fraud risk events in cryptocurrency payment systems are different from the online banking cases under consideration; see Jung et al. (2019) for fraud acting on a decentralized infrastructure and the review article of Trozze et al. (2022).

[pp. 3-4]

The development and validation of the three linked models are the main contributions of our work. To our knowledge, this is the first study to develop, validate, and link components of the risk management process. The output of the anomaly detection model (i.e., the ROC curves), is the input for the triage model, which provides economically optimized ROC curves. Fraud statistics data were utilized to calibrate the various components in the risk model. With these three models, the fraud risk management process can be qualitatively implemented at the same level as the risk management of market or counterparty risks (see Bessis (2011) to describe risk management in banks).

The performance of our risk management framework is the second contribution, although the performance comparison of our fraud detection method with the literature is limited and cautious, due the use of synthetic data instead of real data, a consideration of different channels in payments with different behavioral characteristics of bank customers, and the publication of incomplete statistics. Nevertheless, we compared our work with Wei et al. (2013) and Carminati et al. (2015), both of which analyze online banking fraud based, in part, on real data. The true positive rate (TPR) at a false positive rate (FPR) of 1% was 45% . In Wei et al. the TPR is between 49% and 60% , but unfortunately, the FPR is unknown. In the relevant scenario of Carminati et al. (2015), the TPR is 70% with an FPR of 14% . This FPR is not acceptable to any bank. Processing by specialists leads to high costs. We discuss all these statements in detail in the "Validation results" section. Considering all three models, the theoretical and practical importance of our approach becomes clear. The expected losses in a scenario of CHF 2.023 million, which utilizes the results of machine learning without economic optimization in the triage model, common in the literature, are reduced to CHF 0.800 million with the triage model (i.e., a reduction in the loss potential by more than 60% follows). In addition, if fraud detection is implemented without a risk model, fraud risk can be massively overestimated. Applying our models to three different payment channels, the overestimation of risk ranged from 54% to over 700%.

The remainder of this paper is organized as follows. In "Fraud risk management framework" section, the model selection for the fraud risk management framework is motivated and described. In "Online payment fraud anomaly detection" section, we consider the anomaly-detection model. "Fraud detection triage model" section links fraud

detection to an economic perspective utilizing the triage model. "Risk model" presents the statistical risk model. "Conclusion" section concludes.

#### Fraud risk management framework


[p. 4]

We provide an overview of the three interrelated quantitative models in the context of risk management: online payment anomaly detection, triage model, and risk model.

The goal of anomaly detection is to detect fraudulent activities in e-banking systems and to maintain the number of false alarms at an acceptable level. The implementation of the model consists of three steps: pre-filter, feature extraction, and machine learning.

Non-learning pre-filters ensure that both obvious fraud and normal transactions are sorted early to reduce the false positive rate. Only transactions that pass the pre-filter step are passed on to the machine-learning model. Banks utilize non-customer-based static if-then rules, such as blacklists or whitelists. Pre-filters free the algorithms from obvious cases. The adaptability and flexibility of the machine-learning model is necessary to counter the ever-improving attacks of fraudsters with effective fraud detection.

##### Online payment fraud anomaly detection


Our data face the following general challenges in payment fraud detection (per Wei et al. 2013): large transaction volume with the need for real-time fraud detection, a highly imbalanced dataset, dynamic fraud behavior, limited forensic information, and varying customer behavior.

Given the extremely imbalanced data, fully supervised algorithms typically struggle. Aggarwal and Sathe (2017) proposed unsupervised and weakly supervised approaches based on features that encode deviations from normal behavior. For each customer participating in an e-banking session, we assess whether the agent’s behavior is consistent with the account holder’s normal behavior. The key information for behavioral analysis lies in the sequence of the customer’s clicks during the session. We show that, unlike online e-commerce transactions (see Wei et al. 2013), transaction data, customer behavior data, account data, and booking data are also important for the performance of the algorithm. More precisely, these features are divided into behavioral, transactional, and customer-related features. Starting with nearly 800 features, 147 were extracted utilizing a Bagged Decision Tree Model (BDT). These numbers are many times higher than those for credit card fraud with one to two dozen features (see Table 8 in Hilal et al. 2022). The high dimensionality of the feature space also arises in machine learning corporate default prediction models, where several steps are needed to extract all noisy features (see Kou et al. 2021).

Our e-fraud model operates according to the following principles.

- The model learns the “normal” behavior of each customer based on historical payment data and online banking log data.

- Each new transaction is checked against the learned “normal” behavior to determine if it is an anomaly by extracting the 147 features from the data.

- If an anomaly is detected, it is flagged as suspected fraud.

- Detected transactions that are not found to be fraudulent after manual review are reported back to the model for learning purposes.

[p. 5]

As there are very few known fraud cases, all base learners are trained on fraud-free data only in step one. Fraud cases are only utilized in step two of ensemble aggregation when the base learners are combined to form the final predictive function. The first step is to define base learners who are rich enough to detect a wide range of suspicious transactions or online user sessions. We consider three base learners: the density-based outlier detection model (unsupervised, Local Outlier Factor (LOF)), the isolation-based outlier detection model (unsupervised, Isolation Forest (IF)), and a model for normal customer behavior (supervised, Bagged Decision Trees (BDT)) as base learners (see Breunig et al. (2000), Chandola et al. (2009); Zhang et al. (2022b) for LOF, Liu et al. (2012); Tokovarov and Karczmarek (2022) for IF). We refer to individual instances of LOF, IF, or BDT as base learners. The BDT model is not only a base model, but it is also utilized for feature selection in the other two base models: LOF and IF. The LOF method is suitable for outlier detection, where each observation is assigned an outlier level based on its distance from the nearest cluster of neighboring observations. The aim is to detect outliers in inhomogeneous data, for which classical global outlier methods typically do not provide satisfactory results. Conversely, IF explicitly isolates anomalies without capturing all normal instances. These two methods consider the heterogeneity in the data.

In the second stage, the base learner’s fraud score was aggregated. We consider two approaches to determine the weights in the ensembles: a simple averaging and a supervised approach, although our model largely consists of unsupervised procedures because of the limited availability of fraud cases for which we can extract all the required features. However, we introduce supervision where we utilize scarce labelled data to adjust the importance of certain base learners in the voting scheme, ultimately deciding whether an observation is fraudulent. The penalized logistic regression chosen for classification allows for a better interpretation of the model, as the weights can be utilized to identify base learners, subsets of features, and subsets of samples that have been particularly useful in detecting a particular type of fraud.

##### Triage model


[pp. 5-6]

The fraud detection model calculates scores and, in comparison with a threshold value, decides whether a transaction is flagged as an anomaly. This process results in the probability of detection for a given investigation effort, as indicated by the ROC curve. By making the threshold dependent on the transaction size, we can ensure that larger transaction amounts are more likely detected than smaller ones. This gives up part of the true positive rate (TPR) to reduce overall economic losses (i.e., the TPR decreases for a given FPR). This economic optimization that leads to adjusted ROC curves defines the triage model.

To minimize expected cumulative losses, the constant fraud anomaly detection threshold becomes a function of the transaction amount. Here, the transaction amounts are random variables whose distributions are estimated. In the optimization problem, the transaction function is chosen to maximize the average cumulative sum of the detected fraudulent transactions, where the expected FPR must not exceed a certain threshold. Utilizing this optimal threshold function, the fitted ROC curves were obtained.

The optimization problem has a unique solution if the ROC curve is a concave function of the false positive rate function of the threshold and if the acceptance set of the

expected false positive function constraint is convex. With the chosen piecewise linear false positive constraint function, the assumptions regarding the existence of an optimum are satisfied. The ROC curves that result when fraud anomalies are detected serve as inputs for the optimization. However, because only a vanishingly small number of fraud cases exist, the TPR values for certain FPR levels are subject to considerable uncertainty. Hence, cubic spline functions were utilized for the ROC curve of the optimization.

The UK Finance (2019) report states that the recovery value for online and mobile banking in the UK is 18% of the potential loss. Therefore, we introduced an extension to the optimization program to include recovery.

##### Risk model


[p. 6]

Losses from transaction fraud are included in operational risk incurred by banks. As for other operational risks, one of the key questions from a risk-management perspective is whether the allocated resources and countermeasures are adequate. To answer this, one needs some way of quantifying the risk incurred, ideally a Value-at-Risk (VaR)-model that fits the general risk framework of the bank. Simply, the model calculates the loss L = E(�) × E(τ) where � is the expected event frequency (fraud), and τ is the expected loss per event. The challenge is to determine the distributions of these variables in a tractable and plausible manner and define a model while having very scarce data on past events. We chose the path of an aggregated simulation of many scenarios per e-channel to account for the inherent uncertainty in the choice of these parameters.

Unlike market or credit risk, fraud risk is borne by comparatively few individuals or groups who utilize very specific strategies and technologies to overcome vulnerability in the payment process. Simultaneously, defenders analyze attack plans and update their countermeasures. In this constantly changing environment, neither the frequency of attacks nor the transaction amounts can be assumed to be statistically regular with great certainty. Therefore, we propose a simple, flexible stochastic model composed of basic building blocks. With such a model, risk managers can quickly adjust the model as needed, perform what-if analyses, or simulate changes in payment infrastructure.

The basic model structure for the e-fraud risk model consists of (i) independent models for the three channels, whose components and parameters can be flexibly assembled and adjusted, (ii) sub-models in each channel based on three model types, and (iii) a recovery model for each channel. The three model types for the three different online payment channels in this study are a Beta model (restricted distribution of transaction amounts), a Generalized Pareto Distribution (GPD, unrestricted distribution of transaction amounts), and a “mass attack model” (many simultaneous Beta-type attacks).

Countermeasures against fraud and recovery measures after fraud events play an essential role in determining risk potential. Therefore, they were integrated into the risk models. Countermeasures against online fraud can be divided into those that strengthen the general infrastructure of the payment process and those that focus on defense against actual attacks. The former is conceptually part of the risk model described above, as it affects the frequency and possibly the transaction size of the attacks. However, the latter is better understood in the context of recovery and is considered in the triage model.

#### Online payment fraud anomaly detection


##### Data


[p. 7]

Raw data consisted of transaction data, interaction data between customer and e-banking interface, account, booking, and customer reference data. All users with fewer than 10 logged online sessions were removed as input for ensemble learning. The removed cases were handled separately by utilizing a case-back model.

The transaction history in our dataset consists of 140 million transactions over three years. One hundred fraud cases are reported, but only 11 cases can be linked to the recorded 900’000 online session logs: a 0.0012% fraud rate. Only 900’000 of the 140 million transactions were possible as the log files were only stored in the bank for three months. This change occurred after the project.

A feature vector is created for each e-banking session based on raw data. The interaction pattern features consist of _n_ -grams constructed from customers’ request sequences and normalized deviations from the expected duration between each pair of consecutive requests sent by a customer in an online session. Particular attention was paid to the typical time required to complete a two-step verification process during enrolment. Payment pattern characteristics were calculated for weekday, weekly, and monthly seasonality. These include normalized deviations from the expected payment amount and remaining account balance. Technical data included the IP address of the online session, the HTML agent, and the number of JavaScript scripts executed. Finally, we utilized historically observed confirmed fraudulent transaction identifiers as the ground truth for the weakly monitored part of the pipeline.

Several quality checks were performed. Consistency tests ensure that the session interaction data and transactions match, for example, that the account exists or that a recipient is listed in the transaction. We also checked for missing or non-parsable values, the latter removed.

The data are extracted from several different data sources within the bank in a twostep Python extract, transform, and load (ETL) process, and converted into features for the algorithm. First, we introduce all raw data into a standard structured format for all data sources. Then, we perform the feature engineering described in the following sections to compute the data input for the ensemble.

Our fraud rate 0.0012% is much lower than that reported in the literature. The figures in the two online banking fraud papers, Wei et al. (2013) and Carminati et al. (2015), are 0.018% and 1% , respectively. For credit card fraud, the fraud case number is larger, such as 2% in Piotr et al. (2008). Outside the banking fraud sector, anomalies account for up to 40% of the observations (see Pang et al. 2020). Similar numbers hold in Zhang et al. (2022b), who tested their ensemble-based outlier detection methods on 35 real datasets from various sectors outside the financial sector, with an average fraud rate of 26%.

##### Feature extraction


[pp. 7-8]

For weak supervision, we utilized historically observed confirmed fraudulent transaction identifiers as the ground truth. For training and inference, we created a feature vector for each e-banking session based on the raw data. Each feature aims to encode deviation from expected (“normal”) customer behavior, as observed in historical

interactions with the online banking interface and executed transactions. Three types of features are considered.

The underlying motivation for utilizing features derived from customers’ online session logs is that a large fraction of online payment fraud involves hijacking, where a foreign agent (human or robot fraudster) takes control of the e-banking session. Consequently, it is expected that the timing and sequence of requests posted by the user in a fraudulent session will be significantly different from those in a non-fraudulent session. We utilize the information about user request types (e.g., “get account balance”, “create payment”) and corresponding timestamps to construct the following features:

##### _Behavioral features_


[p. 8]

- _Normalized n-gram frequency of user’s requests within the online session._ We utilized single, pairs and triplets of consecutive requests (1-, 2- and 3-grams) to derive a fixed-size representation. We performed normalization by dividing the number of occurrences for each request with the total number of requests in each session.

- _Normalized time between consecutive user request n-grams._ For each pair of recorded consecutive n-grams, we transformed absolute time between them into deviations by computing z-scores relative to respective historical observations.

- _Technical attributes of a session_ (e.g., IP address of the online session, HTML agent, screen size, and the number of executed Javascript scripts) in binary format - 0 if previously observed, otherwise 1.

##### _Transactional features_


Transactional features aim to quantify how anomalous aggregate payments scheduled in an online session are compared with previously executed payments and the remaining balance on the account. They are designed to capture attempts to empty a victim’s account through a single large or many small transactions, while being mindful of seasonal patterns (e.g., holidays, travel expenses, bills, etc.).

- _Normalized ratio of the payment amount relative to remaining account balance._ We normalize by computing z-scores relative to historically observed ratios.

- _Deviation of the scheduled payment amount from the seasonally expected amount._ We compute four deviations per session using z-scores relative to historical payments executed in the same hour of the day, day of the week, week of the month, and month of the year, respectively.

- _Scheduled time for payment execution_ in binary format - 0 if immediate, 1 if lagged.

A short payment history and many accounts with relatively infrequent transactions proved detrimental to seasonality modelling, hence, these features were omitted from the final model.

##### _Customer‑related features_


[p. 9]

Customer-related features provide insight into peer groups, relationships with other customers, and the service packages they utilize. These include:

- _Sociodemographic_ (e.g., age, nationality, profession, and income)

- _Seniority of client relationship_

- _Product usage_ (i.e., savings, investment accounts, and mortgages)

- _Relationship to other customers_ (i.e., shared accounts, spouses, and family)

These features were not considered within the scope of our study because of data limitations and time constraints.

Bagged decision trees (BDT) are trained utilizing the concept of transfer learning, which assumes that distinguishing between the behaviors of different clients within their online sessions is a related problem in distinguishing between fraudulent and non-fraudulent sessions. The underlying motivation considers that a large fraction of online payment fraud involves hijacking or when a foreign agent (human or robot fraudster) takes control of the e-banking session. As fraudulent sessions are rare and non-fraudulent sessions abound, the utilization of transfer learning enables the extraction of custom patterns from a much broader dataset and the use of supervised learning. Transfer learning comprises two phases. A learning phase where one discriminates behavioral characteristics of each customer vs. non-customers and a prediction phase where discrimination between non-fraudulent and fraudulent users sessions were considered in this study. The “non-customer” class label is then attributed to fraudulent behavior.


---

[source overview](overview.md) | [next part](text-002.md)

[^original]: Paolo Vanini, Sebastiano Rossi, Ermin Zvizdic, Thomas Domenig, "Online payment fraud: from anomaly detection to risk management" (2023-03-12). https://link.springer.com/article/10.1186/s40854-023-00470-w
