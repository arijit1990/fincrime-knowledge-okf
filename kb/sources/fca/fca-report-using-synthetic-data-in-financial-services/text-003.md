---
type: Source Text
title: 'Report: Using Synthetic Data in Financial Services - part 3 of 6 (pp. 20-29)'
description: 'Verbatim extracted text, pp. 20-29: Theme 2: System testing and model validation > Overview of theme; Theme 2: System testing and model validation > Theme 2 in the data lifecycle; Theme 2: System testing and model validation > Current practices; and 1 more sections'
resource: https://www.fca.org.uk/publications/corporate-documents/report-using-synthetic-data-financial-services
tags:
- data_features
- expert_interpretation
- fraud_screening_synergies
- other
- privacy_data_protection
- uk
status: stable
source_id: fca-report-using-synthetic-data-in-financial-services
issuer: fca
issuer_name: Financial Conduct Authority
jurisdictions:
- UK
tier: 1
instrument_type: other
normative_force: expert_interpretation
publication_date: '2024-03-07'
legal_status: current
part: 3
parts_total: 6
content_mode: full_text
generated:
  by: process:fincrime-kb-build
  at: '2026-11-21T18:42:19Z'
verified:
- by: process:kb-validate/verbatim-coverage
  at: '2026-11-21T18:42:19Z'
sources:
- id: original
  resource: https://www.fca.org.uk/publications/corporate-documents/report-using-synthetic-data-financial-services
  title: 'Report: Using Synthetic Data in Financial Services'
  author: org:fca
  last_modified: '2024-03-11T00:00:00Z'
---

# Report: Using Synthetic Data in Financial Services

[previous part](text-002.md) | [source overview](overview.md) | [next part](text-004.md)

> Verbatim text extracted from the original (Financial Conduct Authority, 2024-03-07), part 3 of 6, pp. 20-29. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **expert interpretation**.[^original]

## Theme 2: System testing and model validation


### Overview of theme


[p. 20] [ref: 5.1]

- 5.1 Systems testing and validation is a critical use case for synthetic data. Using real data can have significant privacy, security, and permission implications. In some cases, real or sample data may lack the coverage needed for testing obscure edge cases or validating new data concepts and scenarios. Synthesising data, among other techniques, can act as an alternative approach to using real data or complement real data. In this theme, we explore the use of synthetic data for system testing and model validation in two use cases:

1. Testing whether synthetic data can augment/replace real-world training data in a bank transaction classification engine, and

2. Providing synthetic cross-sector banking, telco, identity, and crime data to explore and validate new data concepts for combatting authorised push payment (APP) Fraud

### Theme 2 in the data lifecycle


[pp. 20-21] [ref: 5.2]

- 5.2 Testing and validation needs manifest all through the data process/product lifecycle, for example in developing propositions, scaling to production, or in software update testcycles. At all these touchpoints, it may be necessary to test ideas and implementations with data. Because many data processes and products utilise sensitive or personal data, testing will naturally require data with similar properties, which may conflict with best practise, for example data minimisation, or regulatory/legal requirements.

- 5.3 In addition, assuming that compliance needs have been met, using real data can require additional steps to be taken, including ensuring that real data is sufficiently de-sensitised, relevant, and diverse for testing. This can be an on-going overhead for organisations to manage. It is time consuming to keep up to date with evolving compliance and product context which may lead to sub-optimal outcomes using older, or heavily amended data due to availability/time pressure.

- 5.4

- Synthetic data potentially supports this use case in the following ways:

- Mitigates many privacy and security concerns

- May in some cases be generated more frequently with shorter lead time than real data can be retrieved, screened, and redacted

- Amplifying absent/rare edge cases, and generating at much larger scales

Theme 2: System testing and model validation

### Current practices


[p. 21] [ref: 5.5]

5.5 Data anonymisation/testing tools are available in the market and are effective in certain scenarios for generating test data for system updates. These include validating Extract, Transform, Load (ETL) and data model pipelines, or for ‘smoke-testing’ data and developing processes that involve machine learning. To be effective, they necessarily remove coherent linkage between datasets for data subjects, mask time-dependence and other correlations between variables which may be desirable to preserve in certain scenarios. Synthetic data, among other techniques, may offer a solution where these characteristics can be retained, while also addressing privacy issues. However, as with other data sharing techniques, the trade-off between utility, fidelity and privacy will still need to be considered.

### Use case 1: Synthetic Open Banking data for model testing


[pp. 21-22]

##### Problem statement

By its nature, transactional data is highly sensitive and time relevant. Express consumer consent is an important aspect of Open Banking and transactional data. In addition, a common challenge with applications using data that can potentially include Personal Identifiable Information (PII) is the security aspects of storing this information and sharing test files with organisations looking to evaluate those models/applications against a range of potential scenarios and edge cases.

Whilst recognising the limitations of synthetic data and that synthetic data cannot substitute real-customer data, especially in areas such as credit decisioning, the analytics research and development functions within organisations might also want to have a first-hand view of the potential of synthetically generated data as well as evaluate and quantify the downstream impacts on model performance and system testing. This use case focuses on a project to create synthetic transaction descriptions (text) to augment and enhance the existing training sets. Although this use case is focused on transactional data, it is expected that these approaches could be generalised for other types of consumer data.

The research project explored in this use case was a proof of concept, and therefore, the stakeholder group involved in the project was limited to the analytics team and Data Scientists that would be generating the synthetic data. It also included product representatives to gain input on the product proposition, and input from legal and commercial teams to review existing data contracts and conditions.

Theme 2: System testing and model validation

##### Synthetic data methodology

There were two aspects when looking to generate synthetic transactional data:

- a. Generating individual transaction descriptions, a text field containing information for the transaction with distributions similar to those found in the real-life data such as Tesco, London, etc.

- b. Generating arrays of synthetic transactional data that, when aggregated to customer level, they would resemble the consumer patterns and behaviours from the real-life data.

These two models are independent of each other and are focusing on either creating bespoke synthetic transactions or synthetic customer profiles for income and expenditure.

For the individual transaction descriptions, a model was used to generate text, one token at a time, predicting the next token based on the context of the previous tokens, and a variant allowed users to guide / control the generation of text by providing specific input or context. Therefore, this such allowed for the introduction of additional information or constraints during the generation of the text descriptions.

For the generation of arrays of synthetic data, the data sample used to create the synthetic data was selected to reflect customers from specific product segments, ensuring some homogeneity in the transactional patterns and spending trends.

##### Evaluating privacy, utility, and fidelity

[pp. 22-23]

The key driver of the research described in this use case was to test existing applications and machine learning models. Privacy is both a motivator behind the use of synthetic data instead of real-consumer transactional data, and a key consideration when evaluating the privacy and fidelity of the synthetically created data, due to legal requirements. Privacy is less of a challenge for synthetically created individual transactions as, by definition, it is not easy to reverse-engineer and identify an individual from a single transaction. Similarly, the aggregated profiles are removed from a detailed list of all of the individual transactions from a unique consumer, thus reducing the risks associated with privacy.

One key challenge was understanding the impact to models when for contractual, regulatory, or system requirements, part of the underlying model training data might need to be deleted while ensuring the ongoing stability of predictive models/capabilities. In this instance fidelity was an important dimension of the evaluation as by varying the requirements for similarity of the synthetic data to the “real-world” data, the range of impacts to the models was evaluated.

For the testing component, fidelity was not as much of a driver compared to privacy or utility. Due to the sensitive nature of transactional data, testing existing Open Banking applications and systems might require large volumes of transactional data that are

Theme 2: System testing and model validation

similar enough to what will be seen in real life to fully evaluate and test the end-to-end capability of a system but not to be able to be linked back to specific consumers and their behaviours.

##### Trip hazards and risk of poor practice

System testing is considered one of the highest priority use cases as before organisations onboard into the Open Banking journey, it is important to ensure that the end-to-end processes and systems are ready for use. Furthermore, it is important to establish the capabilities to do extensive system testing by feeding large volumes of transactional data to understand both capacity/speed of processing, as well as accuracy of outputs and ability to handle edge cases. There are risks if the limitations are not well understood and organisations dive into the creation of synthetic data for credit or customer management decisions without evaluation of the potential negative impacts.

##### Lessons learned

For the individual text description creation, the success of the similarity of the synthetically created data was evaluated by assessing the impact on model performance, for models currently using transactional data obtained by a range of different real-life sources. The final accuracy of challenger models trained on different datasets, by adjusting the ratio of real-life data, and synthetically created data, was compared to the accuracy of the predictive model trained on only real-life data.

It is not always the case of choosing whether to use synthetic data or real-life data. It is important to also understand the potential implications of having to remove some of the real-life data from existing training or validation sets, and evaluating the impacts on model predictiveness and accuracy.

[pp. 23-24]

|Data source|Description|Accuracy change|
|---|---|---|
|Real-life data only|Only real-life data used fortraining|Benchmark|
|Synthetic data + real-life data|50% synthetic data,50% real data used|-2.5% of the benchmark|
|Synthetic data + real-life data|70% synthetic data,30% real data used|-5.0% of the benchmark|
|Synthetic data only|Only synthetic data used fortraining|-32.0% of the benchmark|

In summary, the preliminary findings indicated that for the research in this use case, a threshold of at least 30% real data or an optimisation of the ratio of real-world and synthetic data was needed to maintain strong model accuracy. Further research could be undertaken to compare the accuracy using different synthetic data generation tools to identify whether certain approaches or configurations may lead to better results.

Theme 2: System testing and model validation

For the creation of arrays of data, a 70% overall data quality was achieved with an approximately 60% similarity of synthetic data vs real data in terms of marginal distributions. The results also suggested that over 90% of the synthetic data rows were not copies of real data, an important question in the beginning of this research project. Finally, the model managed to capture specific underlying conditions in the real data and avoided creating arrays that would have no likelihood in appearing in a real-life dataset.

An alternative evaluation of the impacts on model performance and model accuracy was to potentially consider using as a benchmark the smaller dataset of real data against the enhanced dataset. This would align with the analytical motivation of maintaining model performance and model accuracy in cases where a proportion of real-life data was needed to be deleted for regulatory, governance, consent, or system migration reasons.

Both points above support the potential of using synthetically generated data for software and system testing as a first step prior to fully relying on synthetic data for training and validation of certain types of predictive models and use cases.

Use case 2: Cross-sector synthetic data for authorised push payment fraud

##### Problem statement

The FCA and PSR ran an authorised push payment (APP) fraud TechSprint in September 2022. A key driver for this data was to help the participants create solutions to tackle the TechSprint problem statements:

1. Real-time APP fraud prevention using new and existing technologies: what are the barriers and limitations to current (real-time) APP fraud prevention technologies and processes, and how might we encourage the firms we regulate to improve and adopt them?

2. Enhanced Data Sharing: how financial services firms and multiple sectors can share data and relevant analytics, securely in real-time, to spot and prevent fraud?

3. Spotting fraud at source: communicating them to those in the chain, including PSPs so that they can take affirmative action and protect consumers.

[pp. 24-25]

The FCA on-boarded real pseudonymised banking data to be used by participants in the TechSprint. It had several limiting factors: Redaction of certain fields like the transaction narrative; No interoperability between different banks’ data; A ‘stand-alone’ perspective in a multi-sector problem space encompassing banking, payments, telco, and fincrime; No labelled fraud examples for concept development/validation.

To overcome these obstacles, the FCA and PSR collaborated with a third party to design and then build a synthetic dataset to complement the real data, with:

- Synthetic identity, account, and transaction data from a banking perspective

- The ability to track payments between account holders in each synthetic bank

Theme 2: System testing and model validation

- Synthetic identity, account, and call and short message service metadata capturing communication between the synthetic people and businesses

- Multiple typologies of APP Fraud scams

- ‘Ground truth’ of attempted and successful scams, identifying the scammer and victim

##### Synthetic data methodology

Generating synthetic ‘double’ data using artificial intelligence/machine learning approaches would require real data that has the full scope of the synthetic data requirements:

1. Unredacted original data

2. Referential integrity across multiple bank and telco providers

3. Accurately and completely labelled fraud attempts and successes

Achieving this task within the three-month timeline leading up to the TechSprint was unrealistic given various challenges related to data regulation, risk, and other factors. Furthermore, uncertainty surrounding the scalability of artificial intelligence and machine learning methods raised question about their ability to effectively scale across multiple tables, and how large a dataset would be possible to generate.

For these reasons, an agent-based simulation approach was used. This eliminates the need for real data as an input, however, it does require expert judgement and development in creating the scenario, baseline agent behaviours, and specific properties (e.g. fraud typologies) to meet the dataset requirements. Synthetic consumers, merchants, and other organisations (e.g. employers) were created to interact with each other within the simulation over a 2-year time period. As the focus was consumer fraud, most businesses were only ‘semi-simulated’, i.e. Business-toBusiness interaction was almost entirely out of scope, and merchants and employers were assumed to have infinite stock and cash to meet consumer need. The exception to this was that businesses set up for scams had a few extra behaviour types, as per the scam activity they initiated.

Once the ‘baseline’ simulation was established, simulated fraudsters were introduced to attempt scams according to the typical typology execution path, for example initiating a text message exchange with a potential victim while impersonating a family member. Each agent in the simulation had a ‘vulnerability’ attribute which influenced the success rate of each scam attempt. If a scam was successful, then it would initiate payments from the victim to scammer in line with the scam typology.

[pp. 25-26]

The interactions between all the actors in the simulation were logged, and then processed into meaningful formats for the TechSprint participants, i.e. flat file tables with a recognisable schema aligned with what would be found in real-world banking and telco datasets.

The participants were then able to ‘see’ the holistic data picture of dominant ‘business as usual’ banking and telco behaviour, with data revealing scam activity also present. The

Theme 2: System testing and model validation

scam behaviour was calibrated so that the activity was more prevalent than in the real world, enabling easier proposition development to meet the TechSprint objectives. In a similar fashion, data problems like quality, matching, and labelling were ‘solved’ in the data generation process so that the focus would be on the TechSprint questions, and not solving real-world data logistics issues.

For example, in many data-driven initiatives require time-consuming data permission, transformation, linkage, and quality problems to be solved – often on the critical delivery path. By using synthetic data to explore problems, test hypotheses, and create solutions, the value of the potential delivered outcomes can be assessed before (or in parallel with) addressing expensive real data tasks. Furthermore, if the synthetic data is sufficiently high utility and fidelity, the assets developed when processing the synthetic data may be readily recycled for use on the real data. This 1) mitigates ‘wastage’ of effort and 2) may also better inform the upstream real data task requirements, leading to even better outcomes than might originally have been realised.

##### Evaluating privacy, utility, and fidelity

In this use case, privacy barriers were non-existent, as no real-world data about individuals or organisations was used, and so the problem reduces to a direct utilityfidelity trade-off. During development, the priority was agreed to be utility. There was high fidelity/low utility data already available in the form of the redacted banking data, and so the synthetic dataset was calibrated to enable analysis of APP fraud across multiple data perspectives:

1. Ability to analyse across different companies in same sector, for example tracking payments from accounts in one bank to another.

2. Ability to analyse across different sectors, for example correlating a scam victim’s banking data with their phone or text message records.

That said, it was important that the data appeared realistic and contained recognisable and detectable patterns, and manifestations of key behaviours. For example, for the typical income and spending data, key behaviours like common purchases, bill payments and salaries were included. Networks of synthetic people who knew each other were generated, and individuals more frequently communicated and sent payments within them. Behaviours and communication types were parameterised with a combination of expert knowledge, and reference public domain data.

[pp. 26-27]

With these baseline behaviours, the scam pathologies could be implemented. These were designed and calibrated with subject matter experts, as well as quantitatively benchmarked against industry data, such as the UK Finance Annual Fraud report, which defines each distinct scam typology, and the typical frequency and amounts of each. Utility and Fidelity were then evaluated with expert feedback during development, and user feedback during and after the TechSprint.

Theme 2: System testing and model validation

##### Trip hazards and risk of poor practice

Agent Simulation is a less common approach to generating synthetic data. Although there are generic off the shelf simulation toolsets available, specific data synthesis tooling is less common (versus artificial intelligence/machine learning methods) at this point in time, and so there is a requirement for very strong data science/engineering expertise to adapt them to this usage. Furthermore, there is a strong reliance on expert knowledge to calibrate and validate the behaviours and output data and achieve the required fidelity and utility.

The focus in this use case has been on utility, and so while the data can clearly be used to build and develop tools like machine learning predictive models, their predictive value in the ‘real world’ requires careful testing and assessment. The main use case for synthetic data made in this way is for innovating and testing new data concepts where the real data is prohibitively difficult to obtain or create.

##### Lessons learned

Users continue to provide feedback, which will form the roadmap for future improvements. The range of Business as Usual (BaU) behaviours has been kept relatively simple in the initial release following feedback in the TechSprint, and the option remains to adjust the volume and complexity of the population and their possible actions as users interact with the data. Similarly, the signal/noise ratio of fraud may be adjusted depending on user feedback.

By creating data in this way, with no ‘real world’ training data and hence zero risk of unintended disclosure of sensitive personal and/or commercial data, it has been possible to release the data to an extended user group, and to then ‘crowd source’ the potential improvements. Because of this, the utility and fidelity will grow over time as the user group guides the priority enhancements needed.

###### Regulatory considerations for systems testing and model validation

For the Transaction Categorisation research project, the data sample used was approved for research and analytical purposes and pre-existing scripts were used to remove any potential Personal Identifiable Information (PII).

In live applications/products, depending on the source of the data, limitations on the time windows to retain this data might apply. A potential concern could be around the suitability of using historical data when the economy and consumer behaviours might have significantly shifted from those patterns. This was deemed to be more a generic discussion on building predictive models on historic data – there are approaches to minimise the potential risks – and less a regulatory concern for the use of synthetic data per se.

[pp. 27-29]

In the TechSprint use case, the objective of the data synthesis was not to meet a regulatory requirement, nor was it generated/governed within regulatory

Theme 2: System testing and model validation

guidance. Instead, the purpose was to generate a dataset that would be currently very difficult or impossible to exist either as ‘real’ data, or as a synthetic double that mimicked real data. The motivation for doing so was to test potential new regulatory, legal, and ethical issues, arising from the potential usage of data in this way. By bringing together academic, industry, regulator, advisory, law enforcement, consumer and other subject matter experts, the analysis of these concepts was made more practical and less abstract and a usable and ‘real enough’ dataset was generated, helping to drive discussions on these important issues.

Note: this box provides an overview of the important regulatory considerations relating to use case one and two above from SDEG members. These considerations are not a comprehensive list and should not be taken as indication of a policy position or guidance.

Theme 3: Internal and external data sharing


---

[previous part](text-002.md) | [source overview](overview.md) | [next part](text-004.md)

[^original]: Financial Conduct Authority, "Report: Using Synthetic Data in Financial Services" (2024-03-07). https://www.fca.org.uk/publications/corporate-documents/report-using-synthetic-data-financial-services
