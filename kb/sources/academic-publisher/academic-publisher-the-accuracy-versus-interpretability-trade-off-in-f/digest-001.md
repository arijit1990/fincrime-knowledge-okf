---
type: Source Digest
title: The accuracy versus interpretability trade-off in fraud detection model - part 1 of 3 (p. 1)
description: 'Verified paraphrased digest, p. 1: The accuracy versus interpretability trade-off in fraud detection model; The accuracy versus interpretability trade-off in fraud detection model > Abstract; The accuracy versus interpretability trade-off in fraud detection model > Information; and 3 more sections'
resource: https://www.cambridge.org/core/journals/data-and-policy/article/accuracy-versus-interpretability-tradeoff-in-fraud-detection-model/3BA1586A6B635E08BE556FAB89AD8770
tags:
- academic_finding
- academic_paper
- fraud_screening_synergies
- global_academic
- ml_statistics
- model_monitoring
status: stable
source_id: academic-publisher-the-accuracy-versus-interpretability-trade-off-in-f
issuer: academic_publisher
issuer_name: Academic publisher / repository
jurisdictions:
- GLOBAL_ACADEMIC
tier: 3
instrument_type: academic_paper
normative_force: academic_finding
publication_date: '2021-01-01'
legal_status: unknown
part: 1
parts_total: 3
content_mode: digest
generated:
  by: claude-code-subagent/claude-sonnet-5-5
  at: '2026-11-22T14:46:03Z'
verified:
- by: process:kb-digest-check/anchor-match
  at: '2026-11-22T14:46:03Z'
- by: claude-code-judge-agent/claude-opus-5-5
  at: '2026-11-22T14:46:03Z'
sources:
- id: original
  resource: https://www.cambridge.org/core/journals/data-and-policy/article/accuracy-versus-interpretability-tradeoff-in-fraud-detection-model/3BA1586A6B635E08BE556FAB89AD8770
  title: The accuracy versus interpretability trade-off in fraud detection model
  author: org:academic_publisher
  last_modified: '2021-01-01T00:00:00Z'
digest_points: 47
---

# The accuracy versus interpretability trade-off in fraud detection model (digest)

[source overview](overview.md) | [next part](digest-002.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (p. 1) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **academic finding**.

## Abstract

- **descriptive / context**: The paper is a state-of-the-art review of machine learning approaches for fraud detection in banking, addressing class imbalance, lack of trusted labels, concept drift, and the accuracy-interpretability trade-off. (p. 1)[^original]  
  <sub>anchor: "This state-of-the-art review sheds some light on a technology race between black box machine learning models"</sub>

## Policy Significance Statement

- **descriptive / context**: Transparency of algorithms and interpretability of results indicating fraud suspicions could be a critical issue, going beyond statistical accuracy to address societal choices. (p. 1)[^original]  
  <sub>anchor: "the transparency of algorithms and the interpretability of their results, pointing to suspicions of fraud, could be a critical issue"</sub>

## Abstract

- **descriptive / finding or result**: The review says hybrid approaches can offer pragmatic, short-term answers to banks and policy makers, without drawing stakeholders with economic and ethical stakes into the technology race. (p. 1)[^original]  
  <sub>anchor: "Finally, it discusses how concrete and promising hybrid approaches can provide pragmatic, short-term answers to banks and policy makers"</sub>

## Policy Significance Statement

- **descriptive / context**: Customers whose transactions were wrongly suspended ask banks for explanations, and the anti-laundering authority TRACFIN in France expects argued reporting on suspicious deposits or transfers. (p. 1)[^original]  
  <sub>anchor: "customers with erroneously suspended transactions ask for explanations, anti-laundry authorities, such as TRACFIN in France"</sub>
- **descriptive / context**: TRACFIN expects argued reporting on suspicious deposits or transfers. (p. 1)[^original]  
  <sub>anchor: "expect argued reporting on suspicious deposits or transfers"</sub>
- **descriptive / context**: Legal authorities need concrete facts, in particular to distinguish between criminal and civil liability. (p. 1)[^original]  
  <sub>anchor: "legal authorities need concrete facts, in particular to distinguish between criminal and civil liability"</sub>

## 2. Fraud Detection Activities

- **descriptive / definition**: Fraud is defined as all acts of cheating carried out by deceit and in bad faith for the purpose of obtaining an advantage. (p. 2)[^original]  
  <sub>anchor: "Fraud can be defined as all acts of cheating carried out by deceit and in bad faith for the purpose of obtaining an advantage."</sub>

## 2.1. Overview of fraud types in banking industry

- **descriptive / context**: Fraud is characterised by banking product, operation type, channel and fraudster purpose, and these dimensions depend on local market specificities and trends. (p. 2)[^original]  
  <sub>anchor: "These dimensions are strongly linked to local or national market specificities and trends"</sub>
- **descriptive / finding or result**: OSMP reports for 2018 state that online transaction volumes are rising quickly while cheques are decreasing. (p. 2)[^original]  
  <sub>anchor: "OSMP reports in 2018 that the volume of online transactions is quickly rising"</sub>
- **descriptive / typology or red flag**: Fraud modi operandi include phishing, malware, impersonation, payment theft or forgery, and account takeover, with tactics combining dimensions and changing rapidly. (p. 2)[^original]  
  <sub>anchor: "including phishing, malwares, impersonation, payment theft or forgery, account takeover, and so on"</sub>

## 2.2. Description of different tasks in fraud management

- **descriptive / context**: Wilhelm (2003) describes the fraud management lifecycle as seven steps: deterrence, prevention, detection, mitigation, analysis, policy, investigation and prosecution. (p. 2)[^original]  
  <sub>anchor: "The global fraud management lifecycle has been described (Wilhelm, Reference Wilhelm 2003 ) as a set of seven steps"</sub>
- **descriptive / context**: In retail banking the process is simplified to four tasks: alerting, investigation, action against suspected fraudsters, and a posteriori monitoring. (p. 2)[^original]  
  <sub>anchor: "the process can be simplified to a set of four main tasks"</sub>

## 2.2.1. Task 1: Alerting

- **descriptive / limitation**: Business filters that are too tight let fraud pass through, while filters that are too loose suspend too many operations, creating customer risk and alert handling cost. (p. 2)[^original]  
  <sub>anchor: "the business filters are too tight (fraud passes through the barrier) or too loose"</sub>

## 2. Fraud Detection Activities

- **descriptive / context**: The Basel commission identified fraud, especially external fraud, as a major operational risk in 2004, and this risk affects the calculation of the minimum solvency ratio for banks. (p. 2)[^original]  
  <sub>anchor: "the Basel commission identified fraud, and particularly external fraud, as a major operational risk in 2004"</sub>

## 2.2.1. Task 1: Alerting

- **descriptive / finding or result**: For most operations, such as cash withdrawal, card payments, check deposit or online transfers, alerting is usually automated as fixed, manually adjustable business rules that suspend the operation and issue an alert. (p. 2)[^original]  
  <sub>anchor: "For most of them, such as cash withdrawal, credit card payments, check deposit, or online transfers"</sub>

## 2.2.3. Task 3: Action

- **descriptive / finding or result**: Most fraud cases are revealed only once they have succeeded, so action may be needed after a fraud has passed through the earlier steps. (p. 2)[^original]  
  <sub>anchor: "most cases of fraud are revealed once they succeeded"</sub>

## 2.2.2. Task 2: Investigation

- **descriptive / requirement**: Fraud experts need access to right and interpretable information for each investigated operation to justify suspicion and resulting action; prioritisation of alerts is very welcome given limited human resources. (p. 3)[^original]  
  <sub>anchor: "Fraud experts need for this task to have access to the right and interpretable information"</sub>

## 2.2.3. Task 3: Action

- **descriptive / requirement**: Action must be ethically justified by accusations proving fraud or strong suspicion, and by consistency between potential loss and the cost of action; costly action for many low-impact frauds is not acceptable. (p. 3)[^original]  
  <sub>anchor: "The action must be ethically justified not only in terms of accusations proving fraud or a strong suspicion"</sub>

## 2.2.4. Task 4: Monitoring

- **descriptive / requirement**: Monitoring uses post-hoc analysis to understand fraudster behaviour and failures, feeding continuous improvement such as fine-tuning the detection model; the main issue is flexibility to capture changing fraud patterns. (p. 3)[^original]  
  <sub>anchor: "The fourth and final task requires post-hoc analysis to understand the evolution of fraudsters’ behavior"</sub>

## 2.2.5. Other tasks

- **descriptive / context**: Other operational tasks offer learning about fraudster behaviour to strengthen deterrence and prevention, an alternative to fine-tuning the model; further automation innovations are excluded from the paper. (p. 3)[^original]  
  <sub>anchor: "this opportunity is an important alternative to the fine tuning of the FDM itself"</sub>

## 2.2.6. Process issues

- **descriptive / finding or result**: According to LexisNexis' True Cost of Fraud Study, fraud costs in financial services grew 9.3% from 2017 to 2018, more than revenue growth. (p. 3)[^original]  
  <sub>anchor: "fraud costs in financial services from 2017 to 2018 have grown 9.3%, which is more than the revenue growth"</sub>
- **descriptive / finding or result**: The same study finds alerting solutions still underperform with too many false alerts, and one-quarter of fraud costs go to manual review measured in FTE. (p. 3)[^original]  
  <sub>anchor: "one-fourth of fraud costs remain dedicated to manual review, usually measured in full time equivalent (FTE)"</sub>
- **descriptive / context**: The total cost of fraud is the sum of losses from criminal operations, false alerts and investment to guard against them, and this investment must remain lower than expected gains. (p. 3)[^original]  
  <sub>anchor: "The total cost of fraud is the sum of the losses associated with criminal operations and false alerts"</sub>
- **descriptive / context**: The paper poses the question whether to learn explainable models, which may be less accurate than black box models at alerting, or accurate black box models with post-hoc interpretation. (p. 3)[^original]  
  <sub>anchor: "Should the community learn the most explainable models to support tasks 2–4 at the risk that they may be less accurate"</sub>

## 2.3. Modeling fraud detection and assessing performance

- **descriptive / context**: Fraud detection can use unsupervised learning or anomaly detection, or supervised learning from labelled examples; five main performance issues are identified. (p. 3)[^original]  
  <sub>anchor: "From an AI point of view, the first problem may be addressed using unsupervised learning or anomaly detection"</sub>

## 2.3.1. Fraud remains a rare event

- **descriptive / finding or result**: With 3% fraudulent transactions, a classifier labelling all transactions as legitimate would reach 97% accuracy while detecting no fraud. (p. 3)[^original]  
  <sub>anchor: "An algorithm that classifies by default all transactions as negatives (nonfraudulent) will have an accuracy of 97%"</sub>

## 2.3.2. Fraud costs may vary

- **descriptive / finding or result**: Cost-sensitive metrics assign different weights to TP, FP, TN and FN, but fraud cost also includes the financial risk of each operation, and frequent low-amount frauds may not be worth analysing. (p. 3)[^original]  
  <sub>anchor: "Indeed, frequent but low amount frauds, in case of a long-tailed distribution, may not be worth analyzing"</sub>
- **descriptive / limitation**: Machine learning approaches rarely distinguish misclassification costs by observation characteristics, which can drown signals of high-impact frauds. (p. 3)[^original]  
  <sub>anchor: "Machine learning approaches rarely distinguish costs of the error according to these varying characteristics"</sub>

## 2.3.1. Fraud remains a rare event

- **descriptive / finding or result**: The confusion matrix supports a more appropriate assessment of performance in an imbalanced setting. (p. 3)[^original]  
  <sub>anchor: "Confusion matrix, for instance, supports a more appropriate assessment of performances in an imbalanced setting"</sub>
- **descriptive / finding or result**: The Precision-Recall curve and the associated AUC tend to fit imbalanced data better, according to Davis and Goadrich (2006) and Saito and Rehmsmeier (2015). (p. 3)[^original]  
  <sub>anchor: "Precision–Recall curve and the AUC associated tends to generally better fit imbalanced data"</sub>
- **descriptive / context**: The receiver operating characteristic (ROC) curve is also a very popular metric in the field of fraud analytics. (p. 3)[^original]  
  <sub>anchor: "The receiver operating characteristic (ROC) curves is also a very popular metric in the field of fraud analytics."</sub>

## 2.3.3. Fraud is difficult to label

- **descriptive / limitation**: Fraud labels are unreliable: some operations labelled not fraudulent are later revealed as fraud or never detected; this label noise makes confidence in TN and FP much lower than in TP and FN. (p. 4)[^original]  
  <sub>anchor: "the confidence on both the TN and FP in the confusion matrix is clearly much lower than that of the TP and FN"</sub>

## 2.3.4. Fraud patterns may quickly change

- **descriptive / limitation**: Fraudsters imitate good customer behaviour and test system loopholes, so the statistical properties of fraud change over time; without retraining, supervised model performance declines rapidly. (p. 4)[^original]  
  <sub>anchor: "without retraining, the model performance declines rapidly"</sub>
- **descriptive / finding or result**: Traditional supervised models recognise known fraud behaviour easily but struggle to adapt to new behaviours, and a key bank question is balancing retraining frequency against its cost. (p. 4)[^original]  
  <sub>anchor: "recognizing old fraud behaviors that have appeared in the learning base is easy, but adapting to new behaviors"</sub>

## 2.3.5. Fraud must be explained

- **descriptive / requirement**: Investigation requires a justification to support human action against a fraudster, so interpretability of fraud detection models is expected. (p. 4)[^original]  
  <sub>anchor: "This requirement explains why FDM interpretability is expected"</sub>
- **descriptive / definition**: Descriptive accuracy is the quality with which a model can explain its decisions; it is harder to measure than predictive accuracy but is a key quality assessment. (p. 4)[^original]  
  <sub>anchor: "The quality with which a model can explain its decision is referred to as “descriptive accuracy”"</sub>
- **descriptive / context**: Descriptive accuracy can be achieved either by building interpretable models or by post-hoc procedures explaining black box models. (p. 4)[^original]  
  <sub>anchor: "either building interpretable models or develop post-hoc procedure that explains decisions from black box models"</sub>

## 3. SOTA Review of Fraud Detection

- **expected / limitation**: Supervised algorithms, though often applied to fraud detection, should be used with caution because of fraud specificities. (p. 4)[^original]  
  <sub>anchor: "they should be used with caution in this context because of the specificities of fraud"</sub>
- **descriptive / finding or result**: Fraud datasets show strong class imbalance, sometimes with fraud below 1% of the dataset, and overlapping classes, which make classical supervised algorithms ineffective. (p. 4)[^original]  
  <sub>anchor: "the “fraud” class representing sometimes less than 1% of the whole dataset"</sub>
- **descriptive / method**: Imbalance handling gives more weight to the minority class via under-sampling the majority, over-sampling the minority, or hybrid methods combining both. (p. 4)[^original]  
  <sub>anchor: "under-sampling negative observations, over-sampling positive observations, or hybrid methods allowing to combine under- and over-sampling"</sub>

## 3.1. Dealing with imbalanced data

- **descriptive / method**: Random under-sampling removes majority-class observations randomly; other under-sampling methods such as near miss, condensed nearest neighbour, Tomek links, ENN, OSS and NCL select observations to keep or remove. (p. 4)[^original]  
  <sub>anchor: "The most basic method consists in removing elements of the majority class in a random way"</sub>
- **descriptive / finding or result**: Under-sampling methods are described as controversial and perform more poorly than over-sampling methods, according to Batista et al. (2004). (p. 4)[^original]  
  <sub>anchor: "However, these methods are controversial and have poorer performance than oversampling methods"</sub>
- **descriptive / method**: Over-sampling by random duplication of minority observations causes overfitting, whereas SMOTE and its variants (BorderlineSMOTE, KMeansSMOTE, SVMSMOTE, ADASYN) generate new synthetic minority observations. (p. 4)[^original]  
  <sub>anchor: "but this method generates overfitting because of the duplicates"</sub>
- **descriptive / finding or result**: GANs have proven effective for over-sampling data of all kinds, including fraudulent data, according to Fiore et al. (2019) and Shehnepoor et al. (2020). (p. 4)[^original]  
  <sub>anchor: "generative adversarial networks (GANs) have proven to be effective in over-sampling data of all kinds, including fraudulent data"</sub>

## 3. SOTA Review of Fraud Detection

- **descriptive / context**: The fraud class and the legitimate class overlap, which together with strong class imbalance makes classical supervised machine learning algorithms ineffective. (p. 4)[^original]  
  <sub>anchor: "there is an overlap of both classes (see Section 2.3.3 )"</sub>

## 3.1. Dealing with imbalanced data

- **permissive / method**: Hybrid methods can combine over-sampling and under-sampling, with SMOTE-ENN and SMOTE-Tomek cited as two main examples (Batista et al., 2004). (p. 4)[^original]  
  <sub>anchor: "As recommended, hybridizing methods can combine both over-sampling and under-sampling"</sub>
- **descriptive / method**: Smote-ENN and SMOTE-Tomek are named as the two main examples of hybrid over- and under-sampling methods. (p. 4)[^original]  
  <sub>anchor: "Smote-ENN and SMOTE-Tomek being two main examples"</sub>

---

[source overview](overview.md) | [next part](digest-002.md)

[^original]: Anna Nesvijevskaia, Sophie Ouillade, Pauline Guilmin, Jean‐Daniel Zucker, "The accuracy versus interpretability trade-off in fraud detection model" (2021-01-01). https://www.cambridge.org/core/journals/data-and-policy/article/accuracy-versus-interpretability-tradeoff-in-fraud-detection-model/3BA1586A6B635E08BE556FAB89AD8770
