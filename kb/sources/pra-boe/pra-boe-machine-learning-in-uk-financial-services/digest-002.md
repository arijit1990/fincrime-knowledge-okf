---
type: Source Digest
title: Machine learning in UK financial services - part 2 of 2 (p. 1)
description: 'Verified paraphrased digest, p. 1: Machine learning in UK financial services > 5: Case studies; Machine learning in UK financial services > Box B: ML methods; Machine learning in UK financial services > 6: Conclusion based on survey findings; and 1 more sections'
resource: https://www.bankofengland.co.uk/report/2022/machine-learning-in-uk-financial-services
tags:
- empirical_observation
- explainability
- model_governance
- responsible_ai
- statistical_report
- uk
status: stable
source_id: pra-boe-machine-learning-in-uk-financial-services
issuer: pra_boe
issuer_name: Prudential Regulation Authority / Bank of England
jurisdictions:
- UK
tier: 1
instrument_type: statistical_report
normative_force: empirical_observation
publication_date: '2026-08-28'
legal_status: current
part: 2
parts_total: 2
content_mode: digest
generated:
  by: claude-code-subagent/claude-sonnet-5-5
  at: '2026-11-21T18:42:15Z'
verified:
- by: process:kb-digest-check/anchor-match
  at: '2026-11-21T18:42:15Z'
- by: claude-code-judge-agent/claude-opus-5-5
  at: '2026-11-21T18:42:15Z'
sources:
- id: original
  resource: https://www.bankofengland.co.uk/report/2022/machine-learning-in-uk-financial-services
  title: Machine learning in UK financial services
  author: org:pra_boe
  last_modified: '2026-08-28T00:00:00Z'
digest_points: 42
---

# Machine learning in UK financial services (digest)

[previous part](digest-001.md) | [source overview](overview.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (p. 1) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **empirical observation**.

## Model validation

- **descriptive / context**: The report says model validation is key to ensuring ML models work as intended. Validation techniques may be used pre-deployment (while the application is trained and tested) or post-deployment (while live) to continuously assess whether the model and ML application perform within accepted thresholds. (p. 1)[^original]  
  <sub>anchor: "Model validation is key to ensuring ML models work as intended."</sub>
- **descriptive / definition**: Table B validation method 'Outcome monitoring against a benchmark': decisions or actions associated with the ML system are monitored using one or more metrics, and performance is assessed against a benchmark value of those metrics. (p. 1)[^original]  
  <sub>anchor: "Performance is assessed against a certain benchmark value of those metrics."</sub>
- **descriptive / definition**: Table B validation method 'Outcome monitoring against non-ML model or A-B testing': decisions or actions are monitored using one or more metrics and performance is compared with that of a separate non-ML model; the same approach is used in A-B (split) testing. (p. 1)[^original]  
  <sub>anchor: "Performance is assessed by comparing it to the performance of a separate, non-ML model."</sub>
- **descriptive / definition**: Table B validation method 'Black box' testing: input-output testing without reference to the internal structure of the ML application, where the developer experiments by feeding the model different data inputs to understand how it makes predictions. (p. 1)[^original]  
  <sub>anchor: "Input-output testing without reference to the internal structure of the ML application."</sub>
- **descriptive / definition**: Table B validation method 'Explainability tools': tools aimed at explaining the inner workings of the ML model, going beyond input-output testing. (p. 1)[^original]  
  <sub>anchor: "Tools aimed at explaining the inner workings of the ML model (going beyond input-output testing)."</sub>
- **descriptive / definition**: Table B validation method 'Validation of engineered features': features engineered for the ML application are scrutinised, including their potential impacts on model performance. (p. 1)[^original]  
  <sub>anchor: "Engineering features used in the ML application are scrutinised, including potential impacts on model performance."</sub>
- **descriptive / definition**: Table B validation method 'Data-quality validation': one or more techniques ensure data issues (such as class imbalances, missing or erroneous data) are understood and considered in model development and deployment; examples are data certification, source-to-source verification and data issues tracking. (p. 1)[^original]  
  <sub>anchor: "Examples of these include data certification, source-to-source verification or data issues tracking."</sub>

## Table B: Firms use a variety of validation techniques to assess ML

- **descriptive / context**: Table B (validation techniques) is sourced to the Bank of England and the FCA. (p. 1)[^original]  
  <sub>anchor: "- Sources: Bank of England and Financial Conduct Authority."</sub>
- **descriptive / finding or result**: Chart 19 shows the most common validation method is outcome-focused monitoring and testing against benchmarks, letting firms compare ML performance with historical benchmarks such as profitability, customer satisfaction or pricing. Data-quality validation, including detecting errors, biases and risks in data, is next. Overall these methods were used by 81% of respondents; in over half of cases (63%) outcomes were benchmarked against a non-ML model; black box testing was used in less than half of cases. (p. 1)[^original]  
  <sub>anchor: "In over half of the cases (63%), outcomes were benchmarked against a non-ML model."</sub>

## Complexity

- **descriptive / limitation**: Firms found it difficult to define model 'complexity' clearly and assessed it by the number of components, data sources and algorithms in the ML application, so firms rate the complexity of models and applications quite differently. (p. 1)[^original]  
  <sub>anchor: "it was difficult to clearly define what model ‘complexity’ means"</sub>
- **descriptive / method**: Respondents' best-estimate complexity ratings were grouped into 'Low', 'Medium' or 'High'. Some firms stressed low complexity as important where deployment was critical or the model needed to be explainable; others cited large data volumes, varying (including third-party) data sources, interaction of different applications and number of trainable parameters as reasons for medium or high complexity. (p. 1)[^original]  
  <sub>anchor: "the number of trainable parameters, as factors that would result in the application to be considered medium or high complexity"</sub>

## Chart 20: Respondents rated more than a third of ML use cases as ‘High’ complexity

- **descriptive / finding or result**: Most respondents build ML applications in-house but sometimes rely on third parties for platforms and infrastructure such as cloud computing. One firm using third-party-provided models found it hard to classify their complexity because it did not know the underlying model types or have oversight of development. Per Chart 20, two thirds of ML applications are of medium to high complexity (more than a third of use cases rated 'High'). (p. 1)[^original]  
  <sub>anchor: "two thirds of ML applications are considered to be of medium to high complexity"</sub>
- **descriptive / finding or result**: Firms use a range of mechanisms and controls to manage ML risks, including novel challenges such as the added complexity of ML techniques, explainability issues and the continuous lifecycle of some ML applications. (p. 1)[^original]  
  <sub>anchor: "additional complexity of ML techniques, issues with explainability, and the continuous lifecycle of some ML applications"</sub>

## Safeguards

- **descriptive / finding or result**: 42% of respondents said they use some form of monitoring but did not specify safeguards. The most common controls are 'alert systems', 'human-in-the-loop' and 'back-up systems'. (p. 1)[^original]  
  <sub>anchor: "42% of respondents said that they use some form of monitoring"</sub>
- **descriptive / definition**: Alert systems flag unusual or unexpected actions to employees; human-in-the-loop systems execute ML decisions only after human review or approval; back-up systems (sometimes called 'shadow models') perform the same or a similar function as the ML application and can replace it if needed. (p. 1)[^original]  
  <sub>anchor: "‘back-up systems’ (sometimes also known as ‘shadow models’) perform the same or similar function as the ML application"</sub>

## Most advanced use cases

- **descriptive / finding or result**: The most common areas where ML use is most advanced are credit underwriting and insurance pricing/underwriting (Chart 21). Among insurers the most advanced deployment is typically in core business supporting pricing or underwriting; other sectors varied more. (p. 1)[^original]  
  <sub>anchor: "credit underwriting and insurance pricing/underwriting"</sub>
- **descriptive / case example**: Other most-advanced ML deployments listed: expected loss accounting models; claims handling; monitoring for insider trading or market manipulation; directing queries within customer interfaces; 'know your customer' (KYC) checks; trading strategy and execution; payments authorisation; and staff wellness programmes. (p. 1)[^original]  
  <sub>anchor: "monitoring for insider trading or market manipulation; to direct queries within customer interfaces"</sub>

## Most critical use cases

- **descriptive / finding or result**: ML uses in critical areas varied considerably even among similar firms (Chart 22); the most commonly cited were as an input to compliance, AML and KYC. Critical credit underwriting uses resembled the advanced ones, supporting lending decisions, sometimes within scorecards and sometimes as a direct input to automated underwriting (retail credit). (p. 1)[^original]  
  <sub>anchor: "Those most commonly cited were as an input to compliance, AML and KYC."</sub>
- **descriptive / case example**: In risk management, respondents described ML in models predicting expected cash flows, redemptions, delinquencies, inappropriate account use (for example a personal account used for business purposes) or excess losses. (p. 1)[^original]  
  <sub>anchor: "inappropriate account use (eg a personal account being used for business purposes)"</sub>
- **descriptive / case example**: Other critical-area ML activities: insurance underwriting (particularly life insurance); claims handling; monitoring for insider trading or market manipulation; informing trading strategies; directing queries in customer interfaces; managing fund transfers; IT security; and managing a network of third-party experts. Marketing or cross-selling was much less cited than in the most advanced cases, with only one respondent calling it critical (optimising mortgage rates to retain customers). (p. 1)[^original]  
  <sub>anchor: "with only one respondent describing the use of ML in this area as critical"</sub>

## Insurance pricing and underwriting

- **descriptive / case example**: Respondents gave examples in motor risk pricing, life insurance underwriting and novel data sets for pricing or risk management. One insurer uses an ML application to pre-approve consumers for life insurance using data already available from bank accounts and credit rating. (p. 1)[^original]  
  <sub>anchor: "pre-approve consumers for life insurance using data already available from bank accounts and credit rating"</sub>

## Credit underwriting

- **descriptive / case example**: ML credit underwriting use cases typically supplemented existing credit scorecards, at loan application or pre-approval. ML is used to process unstructured data or large volumes, significantly reducing manual processing. (p. 1)[^original]  
  <sub>anchor: "ML applications are used to process unstructured data or large data volumes"</sub>
- **descriptive / case example**: One firm described its most advanced ML use as determining the key input to deciding whether to extend credit: the model uses features at the point of a new credit card application to predict likelihood of customer delinquency within the first year of the loan. (p. 1)[^original]  
  <sub>anchor: "predict likelihood of customer delinquency within the first year of the loan"</sub>
- **descriptive / case example**: ML-based credit decisioning for personal loans was not widespread but was starting to be introduced, including loan underwriting in auto finance. One early-stage model predicts the probability the applicant enters significant arrears in the first 12 months of the loan. Real-time authorisations increasingly draw on the consumer's own historical authorisation data. (p. 1)[^original]  
  <sub>anchor: "predicts the probability of the applicant entering significant arrears in the first 12 months"</sub>

## Marketing

- **descriptive / case example**: ML applications in marketing and customer engagement use the potential customer's inputs in the online quote journey to predict a tailored bundle of product or service options (which can then be manually adapted) rather than a default combination; others prevent policy lapses; some firms use product recommendation ML to identify new sales opportunities. One respondent called this its most advanced ML application owing to its use of broad financial behaviour features from global data assets. (p. 1)[^original]  
  <sub>anchor: "use the inputs provided by the potential customer as part of the online quote journey to predict a bundle of tailored product or service options"</sub>

## Fraud prevention and anti-money laundering

- **descriptive / case example**: Automated fraud screening of customer transactions is taking place on retail non-plastics channels (internet banking, telephony, branch and Open Banking). As fraudulent transaction risks for investment funds grow, ML-based transaction monitoring and detection are being developed, often combining ML and a rule-based engine to monitor activity and highlight anomalies in bond claims and online portal journeys. (p. 1)[^original]  
  <sub>anchor: "often involves a combination of ML and rule-based engine monitor activity and highlights anomalies in bond claims"</sub>

## Box B: ML methods

- **descriptive / definition**: Advanced regression includes penalised regression techniques such as ridge regression and LASSO. Penalised regression applies regularisation to standard regression models (such as logistic regression), penalising the regression weights so models use fewer input variables or generalise better to new data; these models tend to be less complex and more interpretable. (p. 1)[^original]  
  <sub>anchor: "Advanced regression includes penalised regression techniques such as ridge regression and least absolute shrinkage and selection operator (LASSO)."</sub>
- **descriptive / definition**: Tree-based models use decision trees that produce an output through a cascade of binary (yes/no) decisions and handle regression and classification. The most common algorithms are typically ensemble methods in which a collection of decision trees vote on or average their outputs. (p. 1)[^original]  
  <sub>anchor: "a cascade of binary (yes/no) decisions"</sub>
- **descriptive / definition**: Neural networks are loosely based on neuronal structures in the brain and consist of layers of nodes with weighted connections to nodes in other layers; they learn by adjusting these weights in response to training data, can be used for regression and classification, and have wide applications including computer vision and natural language processing. (p. 1)[^original]  
  <sub>anchor: "The neural network learns by adjusting these weights in response to training data."</sub>
- **descriptive / definition**: Natural language processing (NLP) applies algorithms, often neural networks, to identify and extract natural language rules so that unstructured language data are converted into a form computers can understand. (p. 1)[^original]  
  <sub>anchor: "unstructured language data are converted into a form that computers can understand"</sub>
- **descriptive / definition**: Dimensionality reduction techniques reduce the number of variables under consideration by constructing combinations of them into a smaller set of principle variables; approaches divide into feature selection and feature extraction. (p. 1)[^original]  
  <sub>anchor: "Approaches can be divided into feature selection and feature extraction."</sub>

## 6: Conclusion based on survey findings

- **descriptive / finding or result**: ML adoption in UK financial services has increased since 2019 and is more mature and widespread: 72% of firms in the 2022 survey reported using or developing ML applications, and respondents expect the median number of applications to rise over 3.5 times in three years. The Bank and FCA will continue monitoring ML developments and conduct similar surveys. (p. 1)[^original]  
  <sub>anchor: "the Bank and FCA will continue to monitor ML developments and conduct similar surveys going forward"</sub>
- **descriptive / finding or result**: Firms use ML across a greater range of business areas. While AML and fraud detection applications are widespread, ML is also used by banks for enhanced credit risk analytics, by other lenders to automate loan underwriting, by insurers to analyse driving behaviour and claims risk, and by investment and capital markets firms to extract unstructured alternative investment data from multiple sources. (p. 1)[^original]  
  <sub>anchor: "in insurers, to analyse driving behaviour and claims risk"</sub>
- **descriptive / finding or result**: 79% of ML applications among respondents are deployed across a considerable share of business areas and/or are critical to the business area. In 2019, 44% of applications were still in pre-deployment (proofs-of-concept) and only 32% were deployed across a considerable share or all of a business area. (p. 1)[^original]  
  <sub>anchor: "only 32% were deployed across a considerable share or all of a business area"</sub>
- **descriptive / finding or result**: 79% of 2022 respondents had a strategy for ML development, deployment, monitoring and use, and 80% say their ML governance fits into their data governance framework. The Bank and FCA consider good governance essential for safe and responsible ML adoption in financial services. (p. 1)[^original]  
  <sub>anchor: "the Bank and the FCA consider good governance essential for the safe and responsible adoption of ML"</sub>
- **descriptive / finding or result**: Respondents rate current risk to consumers and firms as low to medium. Top consumer risks relate to data bias and representativeness; top firm risks are lack of explainability and interpretability. (p. 1)[^original]  
  <sub>anchor: "Respondents consider the current levels of risk to consumers and firms as low to medium."</sub>
- **descriptive / finding or result**: The greatest constraints on ML are legacy systems and technology infrastructure (as in 2019), followed closely by lack of sufficient skills. Almost half of firms said PRA and/or FCA regulations constrain ML deployment, with 11% of those saying it is a large constraint; of those who thought regulation a constraint, over half cited lack of clarity in existing regulation. (p. 1)[^original]  
  <sub>anchor: "with 11% of those saying that these are a large constraint"</sub>
- **descriptive / context**: The Bank, PRA and FCA published a Discussion Paper on how the UK regulatory framework applies to AI/ML, whether additional clarification may help, and how policy can best support safe and responsible adoption. Readers of the survey are encouraged to engage with the DP and respond. (p. 1)[^original]  
  <sub>anchor: "Readers of this survey are encouraged to engage with the DP and submit a response."</sub>

## 7: Acknowledgements

- **descriptive / method**: A footnote states that the risk and benefit scores are individual firm averages across all benefit and risk categories, rated on a scale of 0 to 1, where 1 is highest risk or benefit and 0 is no risk or benefit. (p. 1)[^original]  
  <sub>anchor: "rated on a scale of 0 to 1, with 1 being highest risk or benefit and 0 being no risk or benefit"</sub>

## Insurance pricing and underwriting

- **descriptive / case example**: Motor insurance use cases: firms apply ML models to estimate expected claim frequency and severity for every new-business and renewal quote. Some motor technical risk models are moving from traditional generalised linear models to ML models based on techniques such as gradient boosting, which aim to predict the cost of a written policy and feed later processes from performance monitoring through to pricing. Some respondents model telematics risk with Deep Neural Networks to estimate driver behaviour, predict claim magnitude and set the consumer's premium. In other firms ML models assess motor claim liability and give the claim handler a recommendation, involving automated early liability decisioning that can improve later claim journeys and consumer outcomes. (p. 1)[^original]  
  <sub>anchor: "Some motor technical risk models are being migrated from traditional generalised linear models to ML models"</sub>

## Fraud prevention and anti-money laundering

- **descriptive / finding or result**: Both this survey and the 2019 survey found that ML is becoming a common technique for fraud detection and AML in payments transactions, particularly card authorisations passing through the payments network. The ML application gives each transaction a risk score as it is processed, so card issuers can prevent potential fraud losses before the transaction completes. (p. 1)[^original]  
  <sub>anchor: "the ML application assigns a risk score, allowing card issuers to stop potential fraud losses"</sub>

## 6: Conclusion based on survey findings

- **descriptive / finding or result**: The greatest benefits identified at present are enhanced data and analytics capabilities, increased operational efficiency, and improved combatting of fraud and money laundering. Although small overall, all benefits are expected to increase over the next three years as the technology becomes more widely used, which may improve personalisation of financial products and services and overall customer engagement. (p. 1)[^original]  
  <sub>anchor: "While small overall, all benefits are expected to increase over the next three years"</sub>

---

[previous part](digest-001.md) | [source overview](overview.md)

[^original]: Prudential Regulation Authority / Bank of England, "Machine learning in UK financial services" (2026-08-28). https://www.bankofengland.co.uk/report/2022/machine-learning-in-uk-financial-services
