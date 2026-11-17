---
type: Source Text
title: Machine learning in UK financial services - part 2 of 5 (pp. 8-15)
description: 'Verbatim extracted text, pp. 8-15: 2 The state of machine learning adoption > 2.1 Machine learning is already being used live by the majority of respondents; 2 The state of machine learning adoption > 2.2 In many cases firms’ deployment of machine learning has passed the initial development phase; 2 The state of machine learning adoption > 2.3 Respondents identify a broad range of use cases; and 4 more sections'
resource: https://www.fca.org.uk/publication/research/research-note-on-machine-learning-in-uk-financial-services.pdf
tags:
- empirical_observation
- explainability
- model_validation
- responsible_ai
- statistical_report
- uk
status: stable
source_id: fca-machine-learning-in-uk-financial-services
issuer: fca
issuer_name: Financial Conduct Authority
jurisdictions:
- UK
tier: 1
instrument_type: statistical_report
normative_force: empirical_observation
publication_date: 2019-10
legal_status: current
part: 2
parts_total: 5
content_mode: full_text
generated:
  by: process:fincrime-kb-build
  at: '2026-11-17T17:21:51Z'
verified:
- by: process:kb-validate/verbatim-coverage
  at: '2026-11-17T17:21:51Z'
sources:
- id: original
  resource: https://www.fca.org.uk/publication/research/research-note-on-machine-learning-in-uk-financial-services.pdf
  title: Machine learning in UK financial services
  author: org:fca
---

# Machine learning in UK financial services

[previous part](text-001.md) | [source overview](overview.md) | [next part](text-003.md)

> Verbatim text extracted from the original (Financial Conduct Authority, 2019-10), part 2 of 5, pp. 8-15. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **empirical observation**.[^original]

## 2 The state of machine learning adoption


### 2.1 Machine learning is already being used live by the majority of respondents


[pp. 8-9]

ML is increasingly being adopted in UK financial services, according to our survey. Two thirds of respondents report they already use ML live in their business (Chart 1), albeit many only have a limited number of use cases. ‘Live’ in this context means that it is used to support client interaction, business decisions or transactions. Reported use cases range from equity trading, where firms use ML to optimise order-routing and deal execution, to AML where firms use ML to analyse millions of documents for ‘know-your-customer’ checks, to insurance, where firms use ML to estimate more personalised risk premiums.

Chart 1 Two thirds of respondents have live machine learning applications in use

Uses machine learningDoes not use machine learningBankingInvestments andcapital marketsPayments, FMIand otherNon-bank retail lendingInsurance0 5 10 15 20 25 30 35Number of respondents

The median firm uses ML in two distinct areas. To illustrate, the median firm may have one application in, say, credit scoring and another one in, say, compliance. There is a significant spread around this and, at the more advanced end, 15 firms (14% of respondents) have more than 10 distinct live applications.

Insurance and banking are the sectors in our sample with the most live cases (Chart 2). The median insurance firm has 7.5 live applications and the median banking firm has 5.5. This is partly driven by the fact that the insurance and banking sectors in our sample feature a bigger share of large firms, as highlighted in Section 1.2. Larger firms may possibly be more advanced in their ML deployment due to benefits of scale, access to data, ability to attract ML talent, or greater resources. However, more research would be needed to shed light on the specific reasons for sectoral differences.

Looking to the future, respondents expect significant growth in the number of live ML applications. The median respondent expects their number of ML applications to more than double over the next three years (Chart 2). For banking and insurance the expected growth is bigger still, with firms in each sector expecting their number of ML applications to almost triple, to 15.5 and 21.5 respectively. This underlines growing interest in ML and the prospect of increasing use across the financial sector in coming years.

Respondents’ predictions reflect the fact that firms report a growing number of ML applications in development that may be ready to go live in coming years.(16) As shown in the next section, roughly, for any six applications firms use, four additional ones are already being developed.

Chart 2 Respondents expect significant growth in use of machine learning over the next three years

[p. 9]

Median number of applications2520Insurance15Banking105Payments, FHI and otherInvestments and capital markets 02019 20 21

To better understand how respondents are developing ML, we asked firms to indicate the maturity of their ML applications across five distinct categories (Chart 3). In many cases, firms’ ML applications have passed the initial pre-deployment phase — which includes proof of concept and research and development — and entered the deployment phase — where the application is used live within the business. Of the total number of ML applications reported by firms, almost two thirds (56%) are live (Chart 3).

### 2.2 In many cases firms’ deployment of machine learning has passed the initial development phase


Chart 3 For any six applications firms use, four additional ones are under development(a)

Initial experiments44%Development phase Pre-deployment phaseIncreasing Small-scalematurity deploymentMedium-scale56%deploymentDeployment phaseFull deployment0 10 20 30 40Share of firms’ applications, per cent

(a) Small-scale deployment refers to 0-30% of a business line; medium-scale deployment refers to 31-60% of a business line; full deployment refers to 60-100% of a business line.

### 2.3 Respondents identify a broad range of use cases


[pp. 9-10]

Respondents use ML in a wide range of business areas. Chart 4A presents a heatmap, showing what share of firms in the overall sample have at least one application in a given business area. It highlights that back-office functions, such as risk management and compliance see the most frequent use cases at the moment, which include, for instance, AML and fraud detection. However, ML is also increasingly being applied to front-office areas, like

(16) While keeping in mind that many proof of concept and research and development projects will not make it to the deployment stage.

Chart 4A The most frequent and also mature use cases are risk management and compliance, and customer engagement(a)

Firms with at least one application as a percentage of all respondent firms

Percent of respondent firms0 10 20 30 40 50Risk Management and ComplianceCustomer EngagementOtherCreditSales and TradingGeneral InsuranceMiscellaneousInvestment Banking (M&A, ECM, DCM)Asset ManagementPayments, Clearing, Custody and SettlementLife InsuranceTreasuryInitial Development Small-scale Medium-scale Fullexperiments phase deployment deployment deployment

(a) Small-scale deployment refers to 0-30% of a business line; medium-scale deployment refers to 31-60% of a business line; full deployment refers to 60-100% of a business line.

customer management as well as sales and trading. Overall, the business areas with the most frequent and mature levels of ML deployment are: risk management and compliance; customer engagement; credit; securities sales and trading and general insurance.

Widespread use in back-office areas partly reflects the fact that this type of activity is performed by most types of firms; while for instance, not all firms in the sample would be expected to undertake insurance activities or investment banking. In addition, AML and fraud detection are well established use cases because the need to connect large data sets and undertake pattern detection is a set-up that lends itself well to ML.(17) It is noted that treasury management (which is an activity conducted in most firms) is not yet an area where ML applications are commonly in use.

Overleaf we break down the most common and mature use cases by sector. The charts show that banking and insurance have a relatively higher share of mature use cases than other sectors. The charts also highlight that, in banking and insurance, use cases are spread across most areas of the business. In banking, following risk management and compliance, customer engagement is the area with the second most use cases. And, for insurers, general insurance distribution and underwriting have more use cases than back-office functions.

[pp. 10-11]

(17) www.iif.com/Publications/ID/1421/Machine-Learning-in-Anti-Money-Laundering and www.accenture.com/_acnmedia/pdf-61/accenture-leveraging-machinelearning-anti-money-laundering-transaction-monitoring.pdf.

Maturity of ML, by business area, in the Banking sector

Percent of respondent firms in Banking0 10 20 30 40 50Risk Management and ComplianceCustomer EngagementOtherCreditSales and TradingInvestment Banking (M&A, ECM, DCM)MiscellaneousPayments, Clearing, Custody and SettlementAsset ManagementGeneral InsuranceLife InsuranceTreasuryInitial Development Small-scale Medium-scale Fullexperiments phase deployment deployment deployment

#### Chart 4B Banking and insurance have the most mature cases, across a range of business areas(a)


[p. 11]

Maturity of ML, by business area, in the Insurance sector

Percent of respondent firms in Insurance0 10 20 30 40 50General InsuranceRisk Management and ComplianceCustomer EngagementLife InsuranceAsset ManagementSales and TradingOtherMiscellaneousInvestment Banking (M&A, ECM, DCM)CreditTreasuryPayments, Clearing, Custody and SettlementInitial Development Small-scale Medium-scale Fullexperiments phase deployment deployment deployment

Maturity of ML, by business area, in the Investments and Capital Markets sector

Percent of respondent firms in Investments and capital markets0 10 20 30 40 50Asset ManagementRisk Management and ComplianceOtherSales and TradingCustomer EngagementPayments, Clearing, Custody and SettlementInvestment Banking (M&A, ECM, DCM)TreasuryMiscellaneousLife InsuranceGeneral InsuranceCreditInitial Development Small-scale Medium-scale Fullexperiments phase deployment deployment deploymentMaturity of ML, by business area, in the Non-Bank Lending sectorPercent of respondent firms in Non-Bank Lending0 10 20 30 40 50Customer EngagementCreditRisk Management and ComplianceOtherTreasuryMiscellaneousInvestment Banking (M&A, ECM, DCM)Sales and TradingPayments, Clearing, Custody and SettlementLife InsuranceGeneral InsuranceAsset ManagementInitial Development Small-scale Medium-scale Fullexperiments phase deployment deployment deploymentMaturity of ML, by business area, in the Payments, FMI and otherPercent of respondent firms in Payments, FMI and other0 10 20 30 40 50Risk Management and ComplianceCustomer EngagementCreditSales and TradingOtherMiscellaneousPayments, Clearing, Custody and SettlementTreasuryLife InsuranceInvestment Banking (M&A, ECM, DCM)General InsuranceAsset ManagementInitial Development Small-scale Medium-scale Fullexperiments phase deployment deployment deployment

(a) Small-scale deployment refers to 0-30% of a business line; medium-scale deployment refers to 31-60% of a business line; full deployment refers to 60-100% of a business line.

## 3 Strategies, governance and third-party providers


### 3.1 The majority of respondents have a dedicated machine learning strategy


[p. 12]

ML is emerging as a strategic priority for many of the firms in our sample. Currently, 52% of respondents have a dedicated strategy for research, development and deployment. Firms highlight three types of approaches (Chart 5): 19% are establishing or already have a dedicated centre of excellence that works to promote ML deployment across the organisation. Whilst 13% of respondents identify ML as important enough to develop a stand-alone firm-wide ML strategy. Furthermore, 20% of firms include ML as part of their overarching innovation or technology strategy but have not set up dedicated structures to promote it independently. Finally, the remaining 48% of respondents say they do not have a dedicated ML strategy. This includes firms that do and do not use ML.

Chart 5 The majority of firms have an explicit strategy for machine learning

DedicatedML strategyPart of wider technology strategy Stand-alone ML strategy ML centre of excellenceNo dedicatedML strategy0 10 20 30 40 50 60Per cent of respondents

Amongst respondents, the insurance (81%), banking (67%) and investment and capital markets (45%) sectors have the highest proportion of firms with a ML strategy. On the other hand, only 37% of payments, FMI and other firms and 28% of non-bank lending firms have a ML strategy.

Some smaller banks and a number of firms from all sectors report they do not have a strategy despite using ML. Several reasons were cited, including that the level of ML is sufficiently small that it does not justify a specific strategy, and ML, as with other technologies, is used to support specific business areas and their respective strategies. Many of the firms that do not use ML report that it is not a priority given the size, scope or focus of their organisation.

### 3.2 The majority of users apply their existing model risk management framework to machine learning(18)


[p. 13]

Of the respondents that use ML, more than half (57%) say their applications are governed through their existing model risk management framework or enterprise risk function, including all three lines of defence.(19) Furthermore, 12% of ML users are establishing specialist committees to advise the respective governance bodies and risk management functions on ML-specific questions, and some have created ML principles that are embedded in the governance framework. Four firms also say they are in the process of establishing a ML ethics function that would address the particular ethical issues raised by ML models and the use of new data sources.

Several firms highlight the need for their risk management frameworks to evolve given their increasing use of ML, for instance, to address challenges related to the explainability of ML models(20) and potential model drift (where model outcomes change over time due to new or different data). Firms note that explainability plays an important part in ML model development, standards and governance procedures. With regard to model drift, some respondents highlight the need for model lifecycle management platforms to enable continuous monitoring of model performance.

Several respondents recognise the importance of ensuring employees at different levels of their organisation have the right knowledge and skill sets to understand the functions and implications of ML. They said this could include embedding individuals with ML expertise within the model risk management and data governance functions. Another aspect of this was making arrangements for senior decision makers to be informed by subject matter experts or to undertake training to ensure they understand the technical aspects of ML as well as the potential legal, regulatory and ethical considerations.

A quarter of ML users highlight data-related challenges and mention specific governance, risk management and control functions to deal with these. This includes assessing data sources that are used for modelling purposes in order to detect and address biased or incorrect data, as well as ensuring appropriate sign-off for access to specific data sets when testing and deploying ML models. From an organisational perspective, several firms said ML falls under both the model risk management and data control frameworks.

In Box 3, we highlight some theoretical implications that an increased use of ML could have for BoE, PRA and FCA supervisors.

### 3.3 Only a small share of machine learning applications are implemented by third-party providers


The majority (76%) of ML use cases are developed and implemented internally by firms, with the remaining 24% implemented by third-party providers (Chart 6). However, firms told us they often use off-the-shelf ML models, open source software and ML libraries developed by third-party providers, which are then further developed or adapted to specific use cases and deployed internally. Respondents from the non-bank lending sector have the highest use of third-party ML applications (36%), which may be because the average size of the firms in this sector in our sample was smaller and, therefore, they may have less capacity to internally develop applications. Or it may be due to the relative ability of third-party providers to integrate products into these firms given their processes and architecture.

> (18) It is important to note that this report does not assess the adequacy of governance frameworks in relation to the use of ML.

> (19) Often referred to as the ‘three lines of defence’, each of the three lines has an important role to play. The business line — the first line of defence — has ‘ownership’ of risk, whereby it acknowledges and manages the risk that it incurs in conducting its activities. The risk management function is responsible for further identifying, measuring, monitoring and reporting risk on an enterprise-wide basis as part of the second line of defence, independently from the first line of defence. The compliance function is also deemed part of the second line of defence. The internal audit function is charged with the third line of defence, conducting risk-based and general audits and reviews to provide assurance to the board that the overall governance framework, including the risk governance framework, is effective and that policies and processes are in place and consistently applied. See www.bis.org/bcbs/publ/d328.pdf. inance: an application to default risk analysis’,

> (20) Bracke, P, Datta, A, Jung, C and Sen, S (2019), ‘Machine learning explainability in finance: an application to default risk analysis’, _Bank of England Staff Working Paper No. 816_ .

### Algorithm complexity, supervision and governance


[p. 14]

Supervisors like the BoE, the PRA and the FCA are technology neutral. That means, in principle, they do not require or prohibit the use of particular technologies. However, the EBA Guidelines on Information and Communication Technology (ICT) Risk Assessment(1) highlight that the ‘depth, detail and intensity of ICT assessment should be proportionate to the size, structure and operational environment of the institution as well as the nature, scale and complexity of its activities’. So, while it will always depend on a multitude of factors whether a ML application poses a meaningful prudential or conduct risk, ML use can alter the nature, scale and complexity of IT applications and thus, a firm’s IT risks. There are three dimensions to this (all of which we asked about in the survey):

- ML applications are more complex. ML models are often very large, non-linear and non-parametric. This makes it harder to comprehensively understand their properties and to validate them. This means certain forms of risk-taking could go undetected. This type of complexity can constitute a significant change to existing systems.

- ML uses a broader range of data. ML applications may often use entirely new types of complex, including unstructured, data. For instance, this could be data from news sources, satellite images or social media.

- ML systems are larger in scale. ML systems increasingly consist of a multitude of interacting components. This can make it harder to validate if they always interact as intended. In many cases, this change is incremental.

Chapter 5 explains in detail the various aspects of how ML can make systems more complex and how different types of data are being used.

However, the deployment of ML could also reduce risks. For instance, ML has the potential to reduce human bias, support the identification of market abuse practices, increase the effectiveness and efficiency of fraud detection and AML processes, as well as lead to better risk assessment and management.(2)

- (1) https://eba.europa.eu/documents/10180/1841624/Final+Guidelines+on+ICT+Risk+Assessment+under+SREP+%28EBA-GL-2017-05%29.pdf/ef88884a-2f0448a1-8208-3b8c85b2f69a.

(2) www.iif.com/Publications/ID/1421/Machine-Learning-in-Anti-Money-Laundering.

Firms also sometimes rely on third-parties when it comes to the underlying platforms and infrastructure, such as cloud computing. Overall, 22% of ML applications are run on the cloud, highlighting the link between in-house development of ML applications and running of these systems on internal servers (Chart 7). It is important to note, this figure differs by sector and non-bank lending firms have the highest share (39%) of applications run on cloud, which again may reflect the higher use of third-party ML applications.

In addition to internal data, firms use data collected by third-parties in 40% of use cases. This includes data from different industries and non-traditional data sets (eg information about consumer characteristics for credit scoring, or information about automobiles for insurance pricing and claims processing), which can be combined with existing data to generate new insights, better predictions or more customised products.

#### Data from third-party sources


##### Chart 6 Most machine learning applications are implemented internally


[p. 15]

Internal implementationExternal implementationInsuranceBankingInvestments andcapital marketsPayments, FMIand otherNon-bank lending0 20 40 60 80 100Per cent of applications

Chart 7 Most machine learning applications are run on internal servers and not on the cloud

Non-bank lendingInsuranceInvestments andcapital marketsBankingPayments, FMIand other0 20 40 60 80 100Per cent of applications run on the cloud


---

[previous part](text-001.md) | [source overview](overview.md) | [next part](text-003.md)

[^original]: Financial Conduct Authority, "Machine learning in UK financial services" (2019-10). https://www.fca.org.uk/publication/research/research-note-on-machine-learning-in-uk-financial-services.pdf
