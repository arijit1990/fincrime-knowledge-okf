---
type: Source Text
title: 'Online payment fraud: from anomaly detection to risk management - part 3 of 3 (pp. 19-25)'
description: 'Verbatim extracted text, pp. 19-25: Online payment fraud: from anomaly detection to risk management > Open Access'
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
part: 3
parts_total: 3
content_mode: full_text
generated:
  by: process:fincrime-kb-build
  at: '2026-11-17T02:21:50Z'
verified:
- by: process:kb-validate/verbatim-coverage
  at: '2026-11-17T02:21:50Z'
sources:
- id: original
  resource: https://link.springer.com/article/10.1186/s40854-023-00470-w
  title: 'Online payment fraud: from anomaly detection to risk management'
  author: org:academic_publisher
  last_modified: '2023-03-12T00:00:00Z'
---

# Online payment fraud: from anomaly detection to risk management

[previous part](text-002.md) | [source overview](overview.md)

> Verbatim text extracted from the original (Academic publisher / repository, 2023-03-12), part 3 of 3, pp. 19-25. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **academic finding**.[^original]

## Online payment fraud: from anomaly detection to risk management


### Open Access


#### Risk model


##### Results


[pp. 19-20]

The simulation results for online banking are presented in Table 6. The table shows the simulation results without applying fraud detection utilizing a constant FPR level of 0.4% and the triage model for an integrated FPR of 0.4%, respectively. In this simulation, no additional recovery was applied.

The above table shows the strong mitigation of risk due to fraud detection. The triage model performs better than the constant FPR benchmark in all submodels, particularly for the GPD submodel. Recall that the triage model places strong emphasis on detecting large fraudulent transactions, even flagging all transactions larger than CHF 192′ 000.

As a second application, we compare the results of this risk model for the three e-channels with the bank’s overall 2019 risk policy. This means that we compare the capital-at-risk (CaR) limits for market and credit risks with operational risk limits, where the e-channel part is now calculated in our model. The following allocation of CaR holds according to the annual report of the bank1 : Credit Risk, 69%; operational risk,

> 1 CaR for credit risk is VaR on the bank’s quantile level and for market risk CaR was in the past chosen on an annual basis and a risk budgeting process was defined to align present risk with the annual risk budget.

11%; market risk trading, 4%; market risk treasury, 11%; market risk real estate, 2%; and investment, 4%.

Approximately 1% of operational risk capital can be attributed to these three channels. Even if we add another 4–5% of the total volume to all payment services, including corporate banking and interbank payments, less than 10% of the operational risk capital is attributed to payment systems. As payment systems account for a significant portion of operational risk, our results confirm serious doubts about the accuracy of the chosen operational risk capital in banks. Without reliable models and data, capital is determined by utilizing dubious business indicators. Our models, which represent a micro-foundation of risk, show that, at least in payment systems, trustworthy risk quantities can be derived by combining machine learning and statistics.

#### Conclusion


[pp. 20-21]

Defense against sophisticated online banking fraud involve several resources and methods. These include risk models, algorithms, human action, knowledge, computer tools, web technology, and online business systems in the context of risk management.

We show that anomaly detection is not only useful per se, identifying a significant proportion of fraud while controlling false alarms, but that linking anomaly detection with statistical risk management methods can significantly reduce risk. A bank equipped with an anomaly detection system will be exposed to orders of magnitude of higher risks in payments than a bank implementing our end-to-end risk management framework with the three components of fraud detection, fraud detection optimization, and risk modelling.

As fraud is part of regulated operational risk, our model allows us to analytically capture these operational risks without crude benchmarking. This also provides a microeconomic foundation for capital adequacy. In the area of operational risk, these results put internal models that are not risk sensitive or difficult to verify on a solid footing.

A complicated problem, such as online payment fraud detection, requires a comprehensive understanding. A prerequisite for this is access to a large dataset. To evaluate our method, we utilized a real dataset from a private bank. Regardless of the chosen algorithm, feature extraction is an essential part of developing an effective fraud detection method. We utilized historically observed and confirmed fraudulent transaction identifiers as the ground truth. Each feature in the feature vectors for each e-banking session aims to encode deviations from normal customer behavior. Thus, behavioral, transactional, and customer-specific features are important.

Our framework opens interesting directions for future research. Roughly speaking, the framework goes in only one direction, from machine learning methods in fraud detection to statistical risk modelling. The feedback process from the risk model to the triage model and from the triage model back to the fraud detection model is a challenging task that can be addressed utilizing reinforcement-learning methods. With such a feedback loop, the entire risk-management framework becomes a learning system. Another research direction is to extend the optimization of fraud detection (triage model) by considering transaction-dependent loss risks and other features such as customer segmentation. More emphasis is placed on segments that are known or suspected to be less

alert or more vulnerable to fraudulent attacks. This resulted in a higher-dimensional triage model.

#### Appendix A


[p. 21]

The structure of our ensemble results from several design decisions based on both insights from the field (online banking) and experience in building machine learning models. Our ensemble model was built according to the following guidelines:

Customer-specific models The features used in our approach encode patterns in customers’ session behaviour and transactions. These patterns vary widely from client to client, which is why we chose to use a client-specific model rather than a global model.

Global feature space Although behaviours vary, we have chosen to use the same feature representation for each session/transaction, which allows us to assign weights to specific (model, feature) pairs based on their performance across all clients. This in turn allows for consistent scoring across all clients and information sharing between clients when fraudulent activity occurs. In other words, our approach makes it easy for learners to adjust their weights.

Separation of models based on feature type We have chosen to form separate ensembles, one based on behavioural features and one based on transactional features, rather than concatenating all features into a single vector and forming a single ensemble based on concatenation. This ensures better interpretability and reduces the likelihood of constructing nonsensical feature subspaces during feature bagging.

Modified Bootstrap aggregation (Bagging) To build an ensemble of weak learners, we use a modification of bootstrap aggregation (bagging). Bagging is a meta-algorithm for ensembles that is used to reduce the variance and improve the stability of the prediction as well as to avoid overfitting.

#### Bagging Pipeline


[pp. 21-22]

_Observational sampling (bagging):_ Bagged ensembles for classification generate additional data for training by resampling with replacement from the initial training data to produce multiple sets of the same size of initial training data, one for each base learner. This is done to reduce the prediction variance. For the two outlier detection ensembles, we used variable subsampling (without replacement) to avoid problems associated with repeated data and to mimic random selection of the neighbourhood count hyperparameter (cf. Aggarwal and Sathe 2017).

_Feature bagging:_ An important task in outlier detection is to identify the appropriate features on which to base the analysis. However, these features may differ depending on the fraud mechanism. Therefore, instead of pre-selecting features, a more robust approach is to create an ensemble of models that focus on different feature sets and assign different weights to the models that use different features depending on their performance. The procedure is applied to each base learner bj as follows:

- Randomly select a number rbj in range [d/10, d − 1] , where _d_ denotes the feature dimension.

- Sample a subspace of features of size rbj

- Train the base learner bj on the sampled subspace.

_No Hyperparameter bagging:_ Due to limited fraud, tuning the hyperparameters via validation may lead to overfitting. For this reason, similar to feature selection, we could instead randomly select a set of different hyperparameters. In our case, however, IF and BDT are not expected to be sensitive to the choice of hyperparameters, and resampling the hyperparameter from LOF would be redundant to the subsampling of the data performed. We therefore set all hyperparameters to reasonable ones found in the literature.

_Sharing bagged features and parameters across customers_ : Subspaces for sampled features and parameters for local outlier factors are shared between all client models and all types of base models (manifested in the respective weak learners). This allows, for example, the introduction of supervision in the aggregation step and increased interpretability of the model, as it is easier to identify features relevant to the detection of certain types of fraud.

_Model aggregation:_ Each base model provides a decision function δ(x) for a given observation _x_ . The base model ensemble directly aggregates (majority voting or averaging) the weak learner results based on different subsamples to form a single hypothesis that determines the class membership of an observation. Usually, this aggregation is directly extended after a normalisation step to include models of different types, parameters or feature groups. In our approach, however, this final aggregation is performed based on a monitoring step that uses knowledge of available frauds to assign different weights to each pair (model, feature set). Essentially, these weights quantify how appropriate each model and feature pair is for fraud detection.

#### Appendix B


[pp. 22-23]

We refer to a composite Poisson process whose marginal distribution corresponds to a beta distribution as a beta model or as a GPD model if the marginal distribution corresponds to a generalised Pareto distribution. The mass attack model is a nested compound Poisson process. The outer Poisson process models the mass attack event, while an inner Poisson process models the number of affected transactions. The extent of damage of the individual affected transactions is modelled with a beta distribution.

- Online banking:

- Beta model: Intensity 35, α = 0.42, β = 2.4 and scale : 71.000. By shifting and scaling, explicitly by the transformation x → α + (β − α)x , the beta distribution is shifted from [0, 1] to the interval [α, β] . The parameter α is called location, and β − α scale.

- GPD model: Intensity 3, shape = 0.25, location = 60.000, scale = 100.000.

- Mass Attack model: Intensity 0.1, intensity nested model 1000, Beta model α = 0.42, β = 2.4 and scale : 20.000.

- Mobile banking:

- Beta model: Intensity 45, α = 0.42, β = 2.4 and scale : 20′ 000.

- Mass Attack model: Intensity 0.1, intensity nested model 1000, Beta model α = 0.42, β = 2.4 and scale : 20′ 000.

- Ebics:

- GPD model:shape = 0.25, location = 100′ 000, scale = 300′ 000.

- Recovery model:

- The recovery model models the percentage recovery in a fraud case. It has the following form:

- With a probability p1 = 65% , a complete recovery is simulated, i.e. no damage remains. This resulted from the fact that in the 159 fraud cases considered, it was actually possible to reduce the loss amount to zero even in 80% of the cases.

- With a probability p2 = 18% , a recovery of zero is simulated, i.e. the damage corresponds to the full amount of the offence.

- With probability 1 − p1 − p2 , a recovery between 0 and 1 is simulated. A beta distribution is chosen as the distribution of these partial recoveries.

[pp. 23-24]

The beta distribution parameters for the online banking channel were fitted on the fraud cases recorded from 13/03/2013 to 13/03/2018. These are 159 fraud cases, of which both the initial fraud transaction amounts and the effective loss amount, i.e. the residual amount after recovery, were recorded. Of the 159 cases, 152 have a fraud amount between CHF 0 and 60,000, while the remaining 7 fraud amounts range between CHF 100,000 and 300,000. A beta distribution was fitted on the 152 cases with fraud amounts up to 60,000 CHF, whereby the scaling parameter, i.e. the upper limit of the distribution, was defined as a free parameter of the fitting procedure and estimated by it to be 71,000 CHF. Similar procedures apply to the marginal distribution fits of the GPD and mass attack models.

There exists significant statistical uncertainty and variability in the driving forces of the defined models. Putting the intended flexibility of the model structure into practice, we distinguish between ’easily accessible’ parameters, which should be subject to discussion at any time in the context of risk assessments, and ’deeper’ parameters, whose mode of action is less obvious and whose adjustment is subject to the process of model reviews. Roughly speaking, Poisson intensities, which determine the expected frequency of events, as well as upper and lower boundaries of the marginal distributions belong to the former category, while shape parameters for the Beta and GPD marginal distributions belong to the latter.

##### Abbreviations

CHF Swiss Franc $ US Dollar ROC Receiver operating curve AUC Area under the ROC curve TPR True positive rate FPR False poistive rate BDT Bagged decision tree LOF Local outlier factor IF Isolation forest VaR Value-at-risk

GPD Generalized pareto distribution EBICS Payment channel for corporate banking clients ETL Extract, transform, load is a three-phase process where data is extracted, transformed and loaded into an output data container

##### Acknowledgements

The authors are thankful to P. Senti, B. Zanella, A. Andreoli and R. Brun all from Zurich Cantonal Bank for the discussions and for providing us with the resources to perform his study. The authors are grateful to P. Embrechts (ETH Zurich) for the model discussions.

##### Author contributions

Sebastiano Rossi and Ermin Zvizdic designed the fraud detection model and analysed the data. Thomas Domenig and Paolo Vanini designed the triage model. Thomas Domenig designed the risk model and did the calculations for the triage and risk model. Paolo Vanini wrote the manuscript with contributions from all authors. Paolo Vanini was involved in the analysis of the triage and risk model. Ermin Zvizdic led the project in the bank. All authors read and approved the final manuscript.

##### Funding

[p. 24]

This research received no specific grant from any funding agency in the public, commercial, or not-for-profit sectors.

##### Availability of data and materials

The bank provided real transaction data and data on transactions (“raw data”) of the customers. The legal basis of the Swiss Federal Data Protection Act (2020) prevents the raw data from leaving the bank in any form or being accessible to any party other than the bank.

##### Competing interests

The authors declare that they have no competing interests.

Received: 22 March 2022 Accepted: 18 February 2023

##### References

##### Declarations


Abdallah A, Maarof MA, Zainal A (2016) Fraud detection system: a survey. J Netw Comput Appl 68:90–113 Ali A, Shukor AR, Siti HO, Abdu S (2022) Financial fraud detection based on machine learning: a systematic literature review. Review Appl Sci 12:9637

Amiri M, Hekmat S (2021) Banking fraud: a customer-side overview of categories and frameworks of detection and prevention. J Appl Intell Syst Inf Sci 2(2):58–68

Aggarwal CC, Sathe S (2017) Outlier ensembles: an introduction. Springer

Bessis J (2011) Risk management in banking. Wiley, New York

Bolton RJ, Hand DJ (2002) Statistical fraud detection: a review. Stat Sci 17(3):235–249

Bolton RJ, Hand DJ (2001) Unsupervised profiling methods for fraud detection, Credit Scoring and Credit Control VII, pp

235–255

Breunig MM, Kriegel H-P, Ng RT, Sander J (2000) LOF: Identifying density based local outliers. In: Proceedings of the 2000 ACM SIGMOD international conference on management of data, pp 93–104

Carminati M, Caron R, Maggi F, Epifani I, Zanero S (2015) BankSealer: a decision support system for online banking fraud analysis and investigation. Comput Secur 53:175–186

Chandola V, Banerjee A, Kumar V (2009) Anomaly detection: a survey. ACM Comput Surveys 41(3):1–58

Embrechts P, Klüppelberg C, Mikosch T (2013) Modelling extremal events: for insurance and finance (Vol 33). Springer Science & Business Media

FCA (2021) Financial conduct authority handbook. www. handb ook. fca. org. uk

Fei Tony L, Kai T, Zhi-Hua Z (2008) Isolation forest. In: 2008 Eighth IEE E International Conference on Data Mining, IEEE, pp. 413-422

Haixiang G, Yijing L, Shang J, Mingyun G, Yuanyue H, Bing G (2017) Learning from class-imbalanced data: review of methods and applications. Expert Syst Appl 73:220–2

Hilal W, Gadsden SA, Yawney J (2021) A review of anomaly detection techniques and applications in financial fraud. Exp Syste Appl 116429.

Hilal W, Gadsden SA, Yawney J (2022) Financial fraud: a review of anomaly detection techniques and recent advances. Expert Syst Appl 193:11

[pp. 24-25]

Jung E, Le Tilly M, Gehani A, Ge Y (2019, July) Data mining-based ethereum fraud detection. In: 2019 IEEE international conference on blockchain (Blockchain) (pp 266-273). IEEE

Juniper Research (2020) Online payment fraud: Emerging threats, segment analysis and market forecasts 2020-2024.

www. junip erres earch. com

KPMG (2019) Global banking fraud survey, KPMG International

Kou G, Xu Y, Peng Y, Shen F, Chen Y, Chang K, Kou S (2021) Bankruptcy prediction for SMEs using transactional data and two-stage multiobjective feature selection. Decis Support Syst 140:113429

Krawczyk B (2016) Learning from imbalanced data: open challenges and future directions. Prog Artif Intell 5(4):221–232

Li T, Kou G, Peng Y, Philip SY (2021) An integrated cluster detection, optimization, and interpretation approach for financial data. IEEE Trans Cybern 52(12):13848–13861

Liu FT, Ting KM, Zhou ZH (2008) Isolation forest. In: 2008 eighth IEEE international conference on data mining, pp 413422. IEEE

Liu FT, Ting KM, Zhou ZH (2012) Isolation-based anomaly detection. ACM Trans Knowl Discov Data (TKDD) 6(1):1–39 McNeil AJ, Frey R, Embrechts P (2015) Quantitative risk management: concepts, techniques and tools-revised edition. Princeton University Press, Princeton

Montague DA (2010) Essentials of online payment security and fraud prevention, vol 54. Wiley, New York

Molloy I, Chari S, Finkler U, Wiggerman M, Jonker C, Habeck T, Schaik RV (2016) Graph analytics for real-time scoring of cross-channel transactional fraud. In: International conference on financial cryptography and data security, pp 22–40. Springer, Berlin, Heidelberg

Pang G, Shen C, Cao L, Hengel AVD (2020) Deep learning for anomaly detection: a review. arXiv preprint arXiv: 2007. 02500

Piotr J, Niall AM, Hand JD, Whitrow C, David J (2008) Off the peg and bespoke classifiers for fraud detection. Comput Stat Data Anal 52:4521–4532

Power M (2013) The apparatus of fraud risk. Account Organ Soc 38(6–7):525–543

Sabu AI, Mare C, Safta IL (2021) A statistical model of fraud risk in financial statements. Case for Romania companies. Risks 9(6):116

[p. 25]

Shen H, Kurshan E (2020) Deep Q-network-based adaptive alert threshold selection policy for payment fraud systems in retail banking. arXiv preprint arXiv: 2010. 11062

Singh A, Ranjan RK, Tiwari A (2022) Credit card fraud detection under extreme imbalanced data: a comparative study of data-level algorithms. J Exper Theor Artif Intell 34(4):571–598

Tokovarov M, Karczmarek P (2022) A probabilistic generalization of isolation forest. Inform Sci 584:433–449

Trozze A, Kamps J, Akartuna EA, Hetzel FJ, Kleinberg B, Davies T, Johnson SD (2022) Cryptocurrencies and future financial crime. Crime Sci 11(1):1–35

Van Liebergen B (2017) Machine learning: a revolution in risk management and compliance? J Financ Trans 45:60–67

Vanini P (2022) Reinforcement Learning in Fraud Detection, Preprint University of Basel

Wei W, Li J, Cao L, Ou Y, Chen J (2013) Effective detection of sophisticated online banking fraud on extremely imbalanced data. World Wide Web 16(4):449–475

West J, Bhattacharya M (2016) Intelligent financial fraud detection: a comprehensive review. Comput Secur 57:47–66

Zhang W, Xie R, Wang Q, Yang Y, Li J (2022a) A novel approach for fraudulent reviewer detection based on weighted topic

modelling and nearest neighbors with asymmetric Kullback-Leibler divergence. Decis Support Syst 157:113765

Zhang G, Li Z, Huang J, Wu J, Zhou C, Yang J, Gao J (2022b) efraudcom: An ecommerce fraud detection system via competitive graph neural networks. ACM Trans Inform Syst (TOIS) 40(3):1-29.

Zhou ZH (2012) Ensemble methods: foundations and algorithms. CRC Press, Boca Raton

Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.


---

[previous part](text-002.md) | [source overview](overview.md)

[^original]: Paolo Vanini, Sebastiano Rossi, Ermin Zvizdic, Thomas Domenig, "Online payment fraud: from anomaly detection to risk management" (2023-03-12). https://link.springer.com/article/10.1186/s40854-023-00470-w
