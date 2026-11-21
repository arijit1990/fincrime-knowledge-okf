---
type: Source Digest
title: 'Project Aurora: the power of data, technology and collaboration to combat money laundering across institutions and borders - part 3 of 6 (pp. 39-61)'
description: 'Verified paraphrased digest, pp. 39-61: Project Aurora > Contents'
resource: https://www.bis.org/publications/project-aurora-power-data-technology-and-collaboration-combat-money-laundering-across-institutions-and-borders
tags:
- correspondent_banking
- effectiveness
- international_standard
- intl
- other
- risk_assessment
status: stable
source_id: bis-bcbs-project-aurora-the-power-of-data-technology-and-collaboration
issuer: bis_bcbs
issuer_name: Bank for International Settlements / Basel Committee
jurisdictions:
- INTL
tier: 2
instrument_type: other
normative_force: international_standard
publication_date: '2023-05-31'
legal_status: current
part: 3
parts_total: 6
content_mode: digest
generated:
  by: claude-code-subagent/claude-sonnet-5-5
  at: '2026-11-21T08:43:43Z'
verified:
- by: process:kb-digest-check/anchor-match
  at: '2026-11-21T08:43:43Z'
- by: claude-code-judge-agent/claude-opus-5-5
  at: '2026-11-21T08:43:43Z'
sources:
- id: original
  resource: https://www.bis.org/publications/project-aurora-power-data-technology-and-collaboration-combat-money-laundering-across-institutions-and-borders
  title: 'Project Aurora: the power of data, technology and collaboration to combat money laundering across institutions and borders'
  author: org:bis_bcbs
  last_modified: '2023-05-31T00:00:00Z'
digest_points: 80
---

# Project Aurora: the power of data, technology and collaboration to combat money laundering across institutions and borders (digest)

[previous part](digest-002.md) | [source overview](overview.md) | [next part](digest-004.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (pp. 39-61) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **international standard**.

## 4.3 Part B: Application of machine learning to the synthetic data set

- **descriptive / method**: Part B applies a few machine learning models to the synthetic data from Part A and compares their performance in different monitoring scenarios (Graph 11) to explore the possibilities and limitations of suspicious transaction monitoring under different views of data across financial institutions and borders. (p. 39)[^original]  
  <sub>anchor: "The performance of machine learning models is compared in different monitoring scenarios"</sub>
- **descriptive / definition**: Silo monitoring scenario: each financial institution conducts transaction monitoring independently, using only its own transaction data. (p. 39)[^original]  
  <sub>anchor: "Silo: each financial institution conducts transaction monitoring independently, using only their own transaction data."</sub>
- **descriptive / definition**: National monitoring scenario: transaction data are visible at country level, each country sees only its own data, and monitoring and model training are done at country level; this could be an instant payment system, national transaction monitoring utility, other collaborative arrangement or potential CBDC system. (p. 39)[^original]  
  <sub>anchor: "National: transaction data are visible on a country level. Each country can only see its own transaction data."</sub>
- **descriptive / definition**: Cross-border monitoring scenario: transaction data are visible at cross-border level, and monitoring and model training are undertaken at cross-border level. (p. 39)[^original]  
  <sub>anchor: "Transaction monitoring and model training are undertaken at a cross-border level."</sub>

## 4.3.1 Machine learning models

- **descriptive / definition**: Supervised models are trained on data with labels indicating whether a transaction is illicit or legitimate, can leverage prior knowledge to identify suspicious patterns, can predict specific outcomes with higher accuracy provided there are sufficient labelled representative data, and can be easily shared where data structure is similar. (p. 39)[^original]  
  <sub>anchor: "Supervised models are trained on data containing labels indicating whether a transaction is illicit or legitimate."</sub>
- **descriptive / definition**: Unsupervised models do not rely on labelled data and aim to identify patterns, outliers and relationships without prior knowledge; this is advantageous when labelled data are scarce, difficult to create or expensive to purchase, which can often be the case in AML, and can uncover hidden or unexpected patterns not obvious to AML experts. (p. 39)[^original]  
  <sub>anchor: "Unsupervised models do not rely on labelled data; instead, they aim to identify patterns, outliers and relationships"</sub>
- **descriptive / limitation**: For unsupervised models, assessing the quality of the model's output without labelled data can be a challenge. (p. 39)[^original]  
  <sub>anchor: "However, assessing the quality of the model's output without the use of labelled data can be a challenge."</sub>
- **descriptive / method**: Table 2 (models explored): logistic regression is a supervised, widely used linear statistical model that estimates the probability of a money laundering event from input data and is a simple, interpretable method. (p. 40)[^original]  
  <sub>anchor: "Widely used linear statistical model. It estimatesthe probability of a money laundering eventbased on the input data."</sub>
- **descriptive / method**: Table 2: the artificial neural network is a supervised neural network model that can discover complex, non-linear relationships in the data for detecting money laundering, approximating the unknown function linking transaction data properties to money laundering labels. (p. 40)[^original]  
  <sub>anchor: "Neural network model that can discovercomplex,non-linear relationships in the datafor detectingmoney laundering."</sub>
- **descriptive / method**: Table 2: the graph neural network is a supervised advanced model that identifies complex relations in data represented as graphs and uses the structure of the transaction network to detect money laundering events. (p. 40)[^original]  
  <sub>anchor: "An advanced model that can identify complexrelations in data represented as graphs, makingthem useful for detecting money laundering."</sub>
- **descriptive / method**: Table 2: isolation forest is an unsupervised model that detects unusual patterns by randomly dividing observations into groups and isolating anomalies that appear early in the process, making it a good choice for detecting money laundering activities. (p. 40)[^original]  
  <sub>anchor: "Detects unusual patterns in data by randomlydividing the observations into groups, andisolating anomalies that appear early in theprocess"</sub>
- **descriptive / method**: A rule-based approach is included in the model comparison as a benchmark replicating common practice, so that rule-based and machine learning approaches use the same data and can be compared. (p. 40)[^original]  
  <sub>anchor: "so that both a rule-based approach and the machine learning approaches use the same data and can be compared."</sub>
- **descriptive / method**: The project uses three supervised models of varying complexity (logistic regression as a simple linear classifier, artificial neural network capturing linear and non-linear relationships, graph neural network extracting information from the network) and one unsupervised model (isolation forest), chosen because they are widely employed in AML research. (p. 40)[^original]  
  <sub>anchor: "These models are chosen because they are widely employed in AML research."</sub>

## Assumptions

- **descriptive / data or feature**: Model features were derived from financial crime research and consultations with compliance experts and include ratios of unique counterparties, transaction values, counts, ratios and accumulated values of different transaction types, speed of movement of funds, and the sum of squared distances to report thresholds or accumulated funds; the PoC assumes consistent use of these features (see Annex B). (p. 40)[^original]  
  <sub>anchor: "The features used in the models have been derived from financial crime research and consultations with compliance experts."</sub>

## 4.3.2 Testing the models

- **descriptive / method**: Trained models were tested for performance and efficiency on the three monitoring scenarios, assessing predictive ability from true positives and false negatives in identifying suspicious transactions and networks. (p. 41)[^original]  
  <sub>anchor: "they were tested and evaluated for performance and efficiency on the three different monitoring scenarios"</sub>
- **descriptive / context**: Network-level assessment matters because certain transactions may not look suspicious alone but may show abnormal behaviour patterns as part of the overall network. (p. 41)[^original]  
  <sub>anchor: "certain transactions may not appear suspicious on their own but may exhibit patterns of abnormal behaviour"</sub>
- **descriptive / method**: Primary metric 1 is recall, the detection rate of money launderers (true positives divided by true positives plus false negatives), showing how well the model detects actual money laundering; high recall means most activities are detected and few left undetected. (p. 41)[^original]  
  <sub>anchor: "recall54 – measures the detection rate of money launderers"</sub>
- **descriptive / method**: Primary metric 2 is reduction of false positive cases, capturing the models' ability to reduce false positives compared with rule-based monitoring. (p. 41)[^original]  
  <sub>anchor: "reduction of false positive cases – is a metric used to capture the machine learning models"</sub>
- **descriptive / method**: Other metrics included precision (correctly identified money launderers divided by all identified, correctly and incorrectly; high precision means few false positives) and F1 score (useful for imbalanced data sets, as money laundering instances are relatively rare); in this experiment precision and F1 findings are similar to recall. (p. 41)[^original]  
  <sub>anchor: "Other metrics included precision55 and F1 score.56,57"</sub>
- **descriptive / limitation**: The machine learning models were not fine-tuned for best performance on the synthetic data but used in their most general form, assuming equal time and effort on setting up each model; in the synthetic data, money launderers are flagged when illicit payments are embedded in the transaction data. (p. 41)[^original]  
  <sub>anchor: "were not fine-tuned to achieve the best possible performance on the synthetic data"</sub>

## Assumptions

- **descriptive / limitation**: Stationary patterns assumption of the proof of concept: the patterns of illicit transactions and the various data features associated with money laundering are assumed to stay stable over time; on that basis the report says there should be enough information to train machine learning models on historical data in order to make predictions. (p. 41)[^original]  
  <sub>anchor: "the patterns of illicit transactions and the different data features associated with money laundering remain stable over time."</sub>

## 4.3.3 Results

- **descriptive / finding or result**: Result 1: machine learning models outperform rule-based monitoring (Graph 12 compares four machine learning models and one rule-based model across the three monitoring scenarios). (p. 42)[^original]  
  <sub>anchor: "Result 1: Machine learning models outperform rule-based monitoring."</sub>
- **descriptive / finding or result**: In the experiment, rule-based monitoring detected only up to 25% of money launderers in the siloed scenario, whereas the machine learning models detected more than twice as many. (p. 42)[^original]  
  <sub>anchor: "the rule-based monitoring approach detected only up to 25% of the money launderers in a siloed monitoring scenario"</sub>
- **descriptive / finding or result**: The graph neural network (GNN) performed best of the five tested models when a broader set of data was available; with a cross-border view of transaction data it can detect approximately 80% of money launderers in the synthetic data. (p. 42)[^original]  
  <sub>anchor: "the model can detect approximately 80% of the money launderers in the synthetic data."</sub>
- **descriptive / limitation**: Improvements for logistic regression and isolation forest are relatively small across scenarios, mainly because all models were trained in the same way without model-specific tuning to keep them comparable; in a real case more specification would be needed, whereas GNNs by design leverage graph structure and capture complex relationships better. (p. 42)[^original]  
  <sub>anchor: "The improvements in the logistic regression and isolation forest are relatively small in the various monitoring scenarios."</sub>
- **descriptive / finding or result**: Result 2: machine learning models become more efficient when based on larger sets of transaction data, giving a better view of transaction networks; a holistic view and monitoring of data enhances detection of complex money laundering networks. (p. 43)[^original]  
  <sub>anchor: "Machine learning models become more efficient when they are based on larger sets of transaction data"</sub>
- **descriptive / finding or result**: A cross-border monitoring scenario is more effective than national and siloed ones in detecting actors in a complex layering scheme. (p. 43)[^original]  
  <sub>anchor: "A cross-border monitoring scenario is more effective than national and siloed ones in detecting actors in complex layering scheme."</sub>
- **descriptive / finding or result**: Siloed and national monitoring scenarios may enable detection of a subset of the individual entities in a money laundering network but lack broader context and cannot gain visibility of the broader network. (p. 43)[^original]  
  <sub>anchor: "Siloed and national monitoring scenarios may enable the detection of a subset of the individual entities"</sub>
- **descriptive / finding or result**: A national monitoring scenario is still useful for detecting suspicious networks within a country's own jurisdictional boundaries. (p. 43)[^original]  
  <sub>anchor: "a national monitoring scenario is still useful for detecting suspicious networks within a country"</sub>
- **descriptive / finding or result**: Result 3: when data are analysed in a national monitoring scenario all models, including the rule-based model, become more efficient, and further improvements are seen for some models in the cross-border scenario. (p. 44)[^original]  
  <sub>anchor: "when data are analysed in a national monitoring scenario, all models, including the rule-based monitoring model, become more efficient."</sub>
- **descriptive / finding or result**: Using siloed rule-based monitoring as benchmark, the GNN in the siloed scenario could reduce false positives by 40% compared with the rule-based approach. (p. 44)[^original]  
  <sub>anchor: "could reduce the number of false positives by 40% compared with the rule-based approach."</sub>
- **descriptive / finding or result**: Most supervised machine learning models reduce false positives versus the rule-based model: by approximately 40% when monitoring is done in silos and approximately 75% with a national view of transaction data, with further improvements under the cross-border view. (p. 44)[^original]  
  <sub>anchor: "approximately 40% when monitoring is done in silos, whereas it is approximately 75% when undertaken with a national view"</sub>
- **descriptive / finding or result**: Machine learning models are more effective than rule-based ones due to their ability to learn complex data patterns and adjust to sophisticated scenarios. (p. 44)[^original]  
  <sub>anchor: "Machine learning models are more effective than rule-based ones due to their ability to learn complex data patterns"</sub>
- **descriptive / finding or result**: The overall performance of supervised machine learning models is better than that of unsupervised models, and labelling helps the model better distinguish between suspicious and normal transactions. (p. 44)[^original]  
  <sub>anchor: "The overall performance of supervised machine learning models is better than for unsupervised models."</sub>
- **descriptive / finding or result**: A graph neural network model works best when monitoring is done at national or cross-border levels, because it can learn more from a larger observed network structure. (p. 44)[^original]  
  <sub>anchor: "A graph neural network model works best when monitoring is done at the national or cross-border levels"</sub>

## 4.3.4 Summary

- **descriptive / finding or result**: Project Aurora's Part B showed machine learning models can be more effective than traditional rule-based monitoring, particularly when they incorporate network features, tested on siloed, national and cross-border views of synthetic transaction data. (p. 46)[^original]  
  <sub>anchor: "The results showed that machine learning models can be more effective than the traditional rule-based approach"</sub>
- **descriptive / finding or result**: Holistic transaction monitoring across multiple payment systems and borders enhances detection of sophisticated money laundering networks while reducing false positives; supervised models are more effective in reducing false positives, suggesting that machine learning combined with national or cross-border monitoring arrangements could be valuable in AML. (p. 46)[^original]  
  <sub>anchor: "holistic transaction monitoring, which includes monitoring across multiple payment systems and borders, enhances the detection"</sub>

## 4.4 Part C: Testing privacy-enhancing technologies for AML

- **descriptive / limitation**: Implementing CAL arrangements could be challenging because of concerns about data protection, privacy, security, competition and legal compliance. (p. 48)[^original]  
  <sub>anchor: "implementing such CAL arrangements could be challenging due to concerns relating to data protection, privacy, security, competition and legal compliance."</sub>
- **descriptive / method**: Part C has three stages: test different PETs in simulated CAL arrangements (centralised, decentralised, hybrid); apply the best performing Part B models to each arrangement; and evaluate their detection on privacy-enhanced data and the feasibility of each PET in each arrangement. (p. 48)[^original]  
  <sub>anchor: "Testing different PETs in different simulated CAL arrangements (centralised, decentralised and hybrid)."</sub>

## 4.4.1 Privacy-enhancing technologies explored

- **descriptive / method**: Three PETs are explored: homomorphic encryption (HE), local differential privacy and federated learning. (p. 48)[^original]  
  <sub>anchor: "Three PETs are explored in this PoC:"</sub>
- **descriptive / definition**: Homomorphic encryption is an emerging technology enabling computations on encrypted data, useful for privacy-preserving deep learning and cloud computing, for example analysing transaction data in AML while protecting personally identifiable information (PII). (p. 48)[^original]  
  <sub>anchor: "enables computations to be performed on encrypted data"</sub>
- **descriptive / limitation**: The computational overhead of HE can lead to increased processing times and resource requirements, though this is rapidly changing; an ISO standard (ISO/IEC 18033-6:2019) for homomorphic encryption has been developed. (p. 48)[^original]  
  <sub>anchor: "An ISO standard (ISO/IEC 18033-6:2019) for homomorphic encryption has also been developed."</sub>
- **descriptive / definition**: Local differential privacy obscures individual records locally at the financial institution level while allowing accurate analysis, giving some privacy protection of non-PII data in money laundering detection, but adding noise to raw data can reduce model performance. (p. 48)[^original]  
  <sub>anchor: "Local differential privacy obscures individual records in a data set"</sub>
- **descriptive / limitation**: If a model is sensitive to the noise introduced by local differential privacy its performance can be worse after applying the PET; the project tested the machine learning methods under LDP to show whether performance is affected. (p. 48)[^original]  
  <sub>anchor: "the model performance can be worse after applying the PET"</sub>
- **descriptive / definition**: Federated learning is a decentralised technique letting multiple entities train a shared model without sharing raw data, helping with data privacy, security, access rights, localisation and access to heterogeneous data. (p. 48)[^original]  
  <sub>anchor: "Federated learning is a decentralised machine learning technique that enables multiple entities to train a shared model collaboratively"</sub>
- **descriptive / limitation**: Federated learning faces challenges including increased processing and communication overhead, data quality, trustworthiness of data and participants, and a reduced ability to detect money laundering networks across different financial institutions versus centralised approaches. (p. 48)[^original]  
  <sub>anchor: "increased processing and communication overhead, data quality, trustworthiness of the data and participants"</sub>
- **descriptive / context**: The choice of PETs depends on the requirements, resources and constraints of the institutions involved in AML, and a hybrid approach using multiple PETs may achieve better results by leveraging each PET's strengths. (p. 49)[^original]  
  <sub>anchor: "A hybrid approach that makes use of multiple PETs may achieve better results"</sub>
- **descriptive / limitation**: Multi-party computation (MPC), zero-knowledge proofs (ZKPs) and private set intersection (PSI) were not tested at this stage but are worth considering for future investigations; the Alliance for Privacy Preserving Detection of Financial Crime is researching MPC, ZKPs and synthetic data generation for KYC, AML and fraud detection. (p. 49)[^original]  
  <sub>anchor: "they were not tested at this stage.62 Nevertheless, these PETs are worth considering for future investigations."</sub>

## Limitations in using homomorphic encryption

- **descriptive / finding or result**: HE was first used as the primary PET because it could allow all data to be encrypted and shared into a centralised pool for analysis while protecting security and privacy. (p. 49)[^original]  
  <sub>anchor: "In the first part of the experiment, homomorphic encryption was used as the primary PET."</sub>
- **descriptive / limitation**: Fully implementing HE in the PoC proved unfeasible because of the size of the encrypted financial transaction data, even with open source FHE libraries on distributed infrastructure with up to 70GB of RAM, so combinations of HE and other PETs such as local differential privacy were explored. (p. 49)[^original]  
  <sub>anchor: "implementing this PET fully in the PoC proved unfeasible due to the size of the encrypted financial transaction data."</sub>

## 4.4.2 Testing a combination of privacy-enhancing technologies in four different collaborative analytics and learning arrangements

- **descriptive / method**: Project Aurora tests PETs in four CAL arrangements, using HE and local differential privacy (LDP) as PETs, with decentralised model training using federated learning (FL) at financial institution or national level. (p. 50)[^original]  
  <sub>anchor: "Project Aurora experiments with privacy-enhancing technologies in four different collaborative analytics and learning (CAL) arrangements."</sub>
- **descriptive / method**: CAL 1 (centralised national): data are encrypted with HE, obfuscated with LDP and shared in a centralised national system, where models are trained and applied on national-level data. (p. 50)[^original]  
  <sub>anchor: "CAL 1 (centralised national) – data are encrypted using HE, obfuscated using LDP"</sub>
- **descriptive / method**: CAL 2 (centralised cross-border): data are encrypted with HE, obfuscated with LDP and shared in a centralised cross-border system whose data set represents all shared transactions, with models trained and applied at cross-border level. (p. 50)[^original]  
  <sub>anchor: "CAL 2 (centralised cross-border) – data are encrypted using HE, obfuscated using LDP"</sub>
- **descriptive / method**: CAL 3 (hybrid national and cross-border): data are encrypted with HE and obfuscated with LDP and shared into a centralised national system, then each country collaborates on training a model using federated learning without sharing transaction data across borders. (p. 51)[^original]  
  <sub>anchor: "CAL 3 (hybrid national and cross-border)65 – data are encrypted using HE and obfuscated using LDP."</sub>
- **descriptive / method**: CAL 4 (decentralised national and cross-border): participants collaboratively train a model using federated learning locally on their own data and share model updates to a common global model, which aggregates the updates and is then shared. (p. 51)[^original]  
  <sub>anchor: "participants collaboratively train a machine learning model using federated learning locally on their own data"</sub>

## Combining homomorphic encryption and local differential privacy – applying PETs according to the sensitivity of the data

- **descriptive / method**: To address HE's limitations, PII data including sensitive account identifiers were protected with HE while LDP was used on transaction flow data, showing PETs could be combined and matched to the sensitivity of data fields. (p. 51)[^original]  
  <sub>anchor: "personal identifiable information (PII) data, including sensitive account identifiers, are protected using HE"</sub>
- **descriptive / context**: In CAL 3, transaction data can be processed on a central server (for example in each country) while still letting countries collaboratively train models and improve national analysis without sharing transaction data directly. (p. 51)[^original]  
  <sub>anchor: "Transaction data can be processed on a central server (eg in each country)"</sub>
- **descriptive / method**: In CAL 1 each financial institution encrypts (HE) and obfuscates (LDP) its own data and shares it to a central server in its home country; findings (flags) could be analysed centrally or sent back to each institution, but the experiment made no assumptions about where results would be shared. (p. 52)[^original]  
  <sub>anchor: "this experimentation did not make any assumptions about where the results and findings would be shared."</sub>
- **descriptive / method**: In CAL 2 each financial institution encrypts and obfuscates its own data with HE and LDP and shares it to a cross-border central system; findings (flags) could be analysed centrally or sent back to each country or institution. (p. 52)[^original]  
  <sub>anchor: "Each financial institution shares transaction data on a cross-border central system."</sub>

## Using federated learning (FL) for decentralised and hybrid CAL arrangements

- **descriptive / method**: Federated learning is used for the decentralised arrangement (CAL 4) and partially for the hybrid arrangement (CAL 3). (p. 53)[^original]  
  <sub>anchor: "For the decentralised CAL arrangement (CAL 4), and partially for the hybrid CAL arrangement (CAL 3), federated learning is utilised."</sub>
- **descriptive / method**: The aim of FL is to collaborate on training a money laundering detection model without sharing transaction data: institutions train on their own data and share only model updates with other institutions through a trusted central server, improving accuracy and robustness versus isolated training. (p. 53)[^original]  
  <sub>anchor: "share only the model updates (learnings) with other financial institutions through a trusted central server."</sub>
- **descriptive / method**: In CAL 3 each institution encrypts its data and shares with a national central server, and each country trains the FL model on its own data and shares model updates with other countries; in CAL 4 each institution trains the FL model on its own data and shares updates with institutions within and across borders, with no transaction data shared with other countries. (p. 53)[^original]  
  <sub>anchor: "No transaction data are shared with other countries."</sub>

## 4.4.3 Results: applying machine learning models in combination with privacy-enhancing technologies

- **descriptive / method**: The graph neural network, artificial neural network and logistic regression, found superior in Part B, were applied in each CAL arrangement to evaluate performance on privacy-enhanced data, information loss from PETs and the optimal CAL arrangement. (p. 54)[^original]  
  <sub>anchor: "graph neural network, artificial neural network and logistic regression"</sub>
- **descriptive / method**: A rule-based model was tested against CAL 2 versus a siloed view to compare it with the machine learning models and evaluate efficiency gains; metrics are recall and reduction in false positives, expressed as the percentage of launderers found and time savings from fewer false positives. (p. 54)[^original]  
  <sub>anchor: "a rule-based model is tested against a CAL 2 (centralised cross-border) arrangement versus a siloed view"</sub>
- **descriptive / finding or result**: Result 1: PET-enabled CAL approaches can improve performance by up to three times in comparison with rule-based monitoring without CAL; the evaluation metric is recall, the percentage of money launderers found by the model. (p. 54)[^original]  
  <sub>anchor: "PET-enabled CAL approaches can improve performance by up to three times in comparison with rule-based monitoring without CAL."</sub>
- **descriptive / finding or result**: On average the machine learning model under national or cross-border CALs with PETs can detect two or three times more money launderers than rule-based monitoring with no CAL arrangement. (p. 55)[^original]  
  <sub>anchor: "can detect two or three times more money launderers than with rulebased monitoring with no CAL arrangement."</sub>
- **descriptive / finding or result**: CAL 1 (centralised national) had the lowest recall of the four arrangements, detecting approximately 60% of money launderers. (p. 55)[^original]  
  <sub>anchor: "CAL 1 (centralised national model) yields the lowest recall score amongst the four CAL arrangements."</sub>
- **descriptive / finding or result**: CAL 2 (centralised cross-border) had the highest recall, detecting approximately 75% of money launderers. (p. 55)[^original]  
  <sub>anchor: "CAL 2 (centralised cross-border model) yields the highest recall score"</sub>
- **descriptive / finding or result**: CAL 3 (hybrid) detects 70% of money launderers, slightly lower recall than CAL 2. (p. 55)[^original]  
  <sub>anchor: "CAL 3 (hybrid model) can detect 70% of money launderers, a slightly lower recall compared with CAL 2."</sub>
- **descriptive / finding or result**: CAL 4 (fully decentralised) showed slightly lower performance than CAL 3, implying that a fully decentralised approach preserving privacy while enabling global collaboration may trade off detection capability against centralised and hybrid arrangements. (p. 55)[^original]  
  <sub>anchor: "may involve a trade-off in terms of its detection capabilities compared with the centralised and hybrid CAL arrangements."</sub>
- **descriptive / finding or result**: Result 2: a centralised cross-border CAL arrangement performs better at detecting cross-border networks; the quantity of launderers detected differs from identification of networks, a broad data set is needed to identify complex criminal networks, and CAL 2 can detect more launderers and discover the underlying cross-country network structure (Graph 21, CLS event 3). (p. 55)[^original]  
  <sub>anchor: "it is essential to differentiate between the quantity of money launderers detected and the identification of money laundering networks."</sub>
- **descriptive / finding or result**: The improved detection under different CALs is due to increased data availability and an improved view of the transaction network. (p. 55)[^original]  
  <sub>anchor: "increased data availability and an improved view of the transaction network"</sub>
- **descriptive / finding or result**: Result 3: PET-enabled CAL with machine learning-based network analysis appears to reduce false positives by up to 80% compared with the siloed rule-based method. (p. 57)[^original]  
  <sub>anchor: "appears to reduce the number of false positives by up to 80% compared with the siloed rule-based method."</sub>
- **descriptive / finding or result**: Graph 22 suggests the four PET-enabled CAL arrangements can reduce false positives by between 40 and 80% versus the siloed rule-based method, with CAL 2 (centralised cross-border) showing the highest reduction. (p. 57)[^original]  
  <sub>anchor: "can reduce false positives by between 40 and 80% compared with the siloed rule-based method"</sub>
- **descriptive / finding or result**: CAL 1 (centralised national) and CAL 3 (hybrid) show false positive reductions comparable to CAL 2. (p. 57)[^original]  
  <sub>anchor: "CAL 1 (centralised national) and 3 (hybrid), show reductions in false positives that are comparable to CAL 2."</sub>
- **descriptive / finding or result**: CAL 4 (decentralised national and cross-border) was only able to reduce false positive cases by 40%. (p. 57)[^original]  
  <sub>anchor: "CAL 4 (decentralised national and cross-border) was only able to reduce false positive cases by 40%."</sub>
- **descriptive / finding or result**: Result 4: CAL 1 can discover part of a money laundering network within a country's borders but cannot detect a network outside its own country. (p. 57)[^original]  
  <sub>anchor: "CAL 1 enables the discovery of a part of the money laundering network within a country"</sub>
- **descriptive / finding or result**: CAL 3 likewise detects networks within a country's borders, but the federated learning model enhanced each country's capability to detect networks within its own jurisdiction. (p. 57)[^original]  
  <sub>anchor: "the implementation of a federated learning model enhanced each country"</sub>
- **descriptive / finding or result**: Result 5: fully decentralised CAL 4 improves each financial institution's local detection of money launderers but may miss network linkages between launderers. (p. 57)[^original]  
  <sub>anchor: "CAL 4 improves each financial institution"</sub>

## 4.4.4 Privacy evaluation of PETs when encrypting transaction data.

- **descriptive / finding or result**: The experiment showed that homomorphic encryption and local differential privacy are techniques that can be used to protect personally identifiable information data and transaction data. (p. 61)[^original]  
  <sub>anchor: "techniques that can be used to protect personally identifiable information data and transaction data."</sub>

---

[previous part](digest-002.md) | [source overview](overview.md) | [next part](digest-004.md)

[^original]: Bank for International Settlements / Basel Committee, "Project Aurora: the power of data, technology and collaboration to combat money laundering across institutions and borders" (2023-05-31). https://www.bis.org/publications/project-aurora-power-data-technology-and-collaboration-combat-money-laundering-across-institutions-and-borders
