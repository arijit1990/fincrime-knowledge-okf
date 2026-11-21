---
type: Source Text
title: Machine learning in UK financial services - part 1 of 5 (pp. 2-7)
description: 'Verbatim extracted text, pp. 2-7: Contents; Executive summary; 1 Introduction > 1.1 Context and objectives; and 3 more sections'
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
part: 1
parts_total: 5
content_mode: full_text
generated:
  by: process:fincrime-kb-build
  at: '2026-11-21T03:48:52Z'
verified:
- by: process:kb-validate/verbatim-coverage
  at: '2026-11-21T03:48:52Z'
sources:
- id: original
  resource: https://www.fca.org.uk/publication/research/research-note-on-machine-learning-in-uk-financial-services.pdf
  title: Machine learning in UK financial services
  author: org:fca
---

# Machine learning in UK financial services

[source overview](overview.md) | [next part](text-002.md)

> Verbatim text extracted from the original (Financial Conduct Authority, 2019-10), part 1 of 5, pp. 2-7. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **empirical observation**.[^original]

## Contents


[p. 2]

||Executive summary|3|
|---|---|---|
|1|Introduction|5|
|1.1|Context and objectives|5|
|1.2|Methodology|6|
|2|The state of machine learning adoption|8|
|2.1|Machine learning is already being used live by the majority of respondentsi|8|
|2.2|In many cases firms’ deployment of machine learning has passed the initialdevelopment phase|9|
|2.3|Respondents identify a broad range of use cases|9|
|3|Strategies, governance and third-party providers|12|
|3.1|The majority of respondents have a dedicated machine learning strategy|12|
|3.2|The majority of users apply their existing model risk management framework tomachine learning|13|
|3.3|Only a small share of machine learning applications are implemented bythird-party providers|13|
|4|Firms’ perception of benefits, risks and constraintsi|16|
|4.1|Respondents already see benefits from machine learning and expect these to increase|16|
|4.2|Firms recognise model validation and governance need to keep pace withmachine learning developmentsi|16|
|4.3|Constraints to deployment of machine learning are mostly internal to firmsi|18|
|4.4|Regulation is not seen as an unjustified barrier|19|
|5|How machine learning works|21|
|5.1|Machine learning applications consist of a pipeline of processes|21|
|5.2|Data acquisition and feature engineering are evolving with the adventof machine learning|21|
|5.3|Model engineering and performance evaluation decide which models are deployed|23|
|5.4|Model validation is key to ensuring machine learning models work as intended|25|
|5.5|Complexity can increase due to deployment of machine learning|26|
|5.6|Firms use a range of safeguards to address risks|27|
|6|Conclusion|28|
|6.1|Context|28|
|6.2|What we have learnt|28|
|6.3|Questions for authorities|29|
|6.4|Next steps|29|
|7|Appendix — case studies|30|
|7.1|Purpose and background|30|
|7.2|Methodology|30|
|7.3|Anti-money laundering and countering the financing of terrorism|30|
|7.4|Customer engagement|31|
|7.5|Sales and trading|31|
|7.6|Insurance pricing|32|
|7.7|Insurance claims management|33|
|7.8|Asset management|34|
||Acknowledgements|36|

## Executive summary


[p. 3]

Machine learning (ML) is the development of models for prediction and pattern recognition from data, with limited human intervention. In the financial services industry, the application of ML methods has the potential to improve outcomes for both businesses and consumers.(1) In recent years, improved software and hardware as well as increasing volumes of data have accelerated the pace of ML development. The UK financial sector is beginning to take advantage of this. The promise of ML is to make financial services and markets more efficient, accessible and tailored to consumer needs.(2) At the same time, existing risks may be amplified if governance and controls do not keep pace with technological developments. But the risks presented by ML may be different in each of the contexts it is deployed in.(3) More broadly, ML also raises profound questions around the use of data, complexity of techniques and the automation of processes, systems and decision-making.(4)

The Bank of England (BoE) and Financial Conduct Authority (FCA) have a keen interest in the way that ML is being deployed by financial institutions. That is why we conducted a joint survey in 2019 to better understand the current use of ML in UK financial services. The survey was sent to almost 300 firms, including banks, credit brokers, e-money institutions, financial market infrastructure firms, investment managers, insurers, non-bank lenders and principal trading firms, with a total of 106 responses received.

The survey asked about the nature of deployment of ML, the business areas where it is used and the maturity of applications.(5) It also collected information on the technical characteristics of specific ML use cases. Those included how the models were tested and validated, the safeguards built into the software, the types of data and methods used, as well as considerations around benefits, risks, complexity and governance.

Although the survey findings cannot be considered to be statistically representative of the entire UK financial system, they do provide interesting insights.

The key findings of our survey are:

- ML is increasingly being used in UK financial services. Two thirds of respondents report they already use it in some form. The median firm uses live ML applications in two business areas and this is expected to more than double within the next three years.

- In many cases, ML development has passed the initial development phase, and is entering more mature stages of deployment. One third of ML applications are used for a considerable share of activities in a specific business area. Deployment is most advanced in the banking and insurance sectors.

- From front-office to back-office, ML is now used across a range of business areas. ML is most commonly used in anti-money laundering (AML) and fraud detection as well as in customer-facing applications (eg customer services and marketing). Some firms also use ML in areas such as credit risk management, trade pricing and execution, as well as general insurance pricing and underwriting.

[pp. 3-4]

> (1) Carney, M (2018), ‘AI and the Global Economy’.

> (2) Carney, M (2018), ‘AI and the Global Economy’.

> (3) www.fca.org.uk/news/speeches/future-regulation-ai-consumer-good. icial intelligence’.

> (4) Proudman, J (2019), ‘Managing machines: the governance of artificial intelligence’.

> (5) In this report the term application means the integrated whole of a ML application, including data collection, feature engineering, model engineering and deployment. It also includes the underlying IT infrastructure (eg data storage, integrated development environment). A ML application could include multiple models and ML algorithms. ML applications should be seen as separate if they fulfil different business purposes or if their set up / components differ significantly.

- Regulation is not seen as an unjustified barrier but some firms stress the need for additional guidance on how to interpret current regulation. Firms do not think regulation is an unjustified barrier to ML deployment. The biggest reported constraints are internal to firms, such as legacy IT systems and data limitations. However, firms stressed that additional guidance around how to interpret current regulation could serve as an enabler for ML deployment.

- Firms thought that ML does not necessarily create new risks, but could be an amplifier of existing ones. Such risks, for instance ML applications not working as intended, may occur if model validation and governance frameworks do not keep pace with technological developments.

- Firms validate ML applications before and after deployment. The most common validation methods are outcome-focused monitoring and testing against benchmarks. However, many firms note that ML validation frameworks still need to evolve in line with the nature, scale and complexity of ML applications.

- Firms use a variety of safeguards to manage the risks associated with ML. The most common safeguards are alert systems and so-called ‘human-in-the-loop’ mechanisms. These can be useful for flagging if the model does not work as intended (eg in the case of model drift, which can occur as ML applications are continuously updated and make decisions that are outside their original parameters).

- Firms mostly design and develop ML applications in-house. However, they sometimes rely on third-party providers for the underlying platforms and infrastructure, such as cloud computing.

- The majority of users apply their existing model risk management framework to ML applications. But many highlight that these frameworks might have to evolve in line with increasing maturity and sophistication of ML techniques. This was also highlighted in the BoE’s response to the Future of Finance report.(6) In order to foster further conversation around ML innovation, the BoE and the FCA have announced plans to establish a publicprivate group to explore some of the questions and technical areas covered in this report.

(6) Bank of England (2019), ‘The Future of Finance — our response’.

## 1 Introduction


### 1.1 Context and objectives


[p. 5]

The UK economy is increasingly powered by big data, platform business models, advanced analytics, smartphone technology and peer-to-peer networks.(7) At the same time, innovation in the financial sector is dramatically changing the markets we regulate(8) but also the way in which we regulate.(9)(10) As an industry, financial services are (and will always be) very data-reliant. Hence, this new data-driven economy goes hand in hand with fundamental changes to the structure and nature of the financial system supporting it.(11) And ML is a principal driver contributing to this new finance.(12)

ML has wide-ranging applications in financial services and, when combined with increasing computational power, has the ability to analyse large data sets, detect patterns and solve problems at speed. The use of ML has the potential to generate analytical insights, support new products and services, and reduce market frictions and inefficiencies.(13) If this potential is achieved, consumers could benefit from more tailored, lower cost products and firms could become more responsive, learner and effective.

It is important that regulatory authorities understand ML; including the current state of deployment, maturity of applications, use cases, benefits and risks. This was the motivation behind the BoE and FCA joint survey, which was carried out during the first half of 2019. The objective was to gain an understanding of the use of ML in the UK financial sector. The results, together with ongoing dialogue with the industry and other authorities, both domestically and internationally, will help identify where there are policy questions that need to be answered in the future, in order to support the safe and productive deployment of ML within the financial sector.

This joint BoE-FCA report is the result of the analysis of the responses to the survey and presents:

- a quantitative overview of the use of ML across the respondent firms;

- the ML implementation strategies of firms that responded to the survey;

- approaches to the governance of ML;

- the share of applications developed by third-party providers;

- respondents’ views on the benefits of ML;

- perceptions of risks and ethical considerations;

- perspectives on constraints to development and deployment of ML; and

- a snapshot of the use of different methods, data, safeguards performance metrics, validation techniques and perceived levels of complexity.

> (7) Carney, M (2019), ‘A platform for innovation — remarks’.

> (8) www.fca.org.uk/news/speeches/innovation-hub-innovation-culture. inancial-conduct-regulation-restless-world.

> (9) www.fca.org.uk/news/speeches/financial-conduct-regulation-restless-world.

> (10) Chakraborty, C and Joseph, A (2017), ‘Machine learning at central banks’, _Bank of England Staff Working Paper No. 674_ . Turrell _et al_ (2018), ‘Using online job vacancies to understand the UK labour market from the bottom-up’, _Bank of England Staff Working Paper No. 742_ . Proudman, J (2018), ‘Cyborg supervision — the application of advanced analytics in prudential supervision’. intech’,

> (11) See Mnohoghitnei, I, Scorer, S, Shingala, K and Thew, O, ‘Embracing the promise of fintech’, _Bank of England Quarterly Bulletin_ , 2019 Q1.

> (12) Carney, M (2018), ‘AI and the Global Economy’.

> (13) www.fsb.org/wp-content/uploads/P011117.pdf.

### What is the difference between artificial intelligence and machine learning?


[p. 6]

Artificial intelligence (AI) is the theory and development of computer systems able to perform tasks which previously required human intelligence.(1) AI is a broad field, of which ML is a sub-category.

ML is a methodology whereby computer programmes fit a model or recognise patterns from data, without being explicitly programmed and with limited or no human intervention. This contrasts with so-called ‘rules-based algorithms’ where the human programmer explicitly decides what decisions are being taken under which states of the world (Figure A).

Figure A Machine learning algorithms make decisions without being explicitly programmed

Rules-based algorithms Machine learningHuman Human setsexplicitly optimisationprograms criteriarulesOptimising programme + DataIf Then If Then Programmecomes upA X ? ? with rulesB Y ? ?C and D Z ? ?

Many ML algorithms constitute an incremental (rather than fundamental) change in statistical methods. They introduce more flexibility in statistical modelling. For instance, many ML models are not constrained by the linear relationships often imposed in traditional economic and financial analysis.

However, over the last decade, computing power and the amount of data processed has grown exponentially. This has allowed ML models to become an order of magnitude larger and more complex than more traditionally used techniques. As a result, ML models can often make better predictions than traditional models or find patterns in large amounts of data from increasingly diverse sources.

(1) www.fsb.org/2017/11/artificial-intelligence-and-machine-learning-in-financial-service/.

The report closes with a non-exhaustive selection of case studies, describing a sample of typical use cases, including:

- Anti-money laundering and countering the financing of terrorism

- Customer engagement

- Sales and trading

- Insurance pricing

- Insurance claims management

- Asset management

### 1.2 Methodology


[pp. 6-7]

When designing the survey, the BoE and FCA considered the Legislative and Regulatory Reform Act 2006 principle that regulatory activities should be carried out in a way which is transparent and proportionate.

In total, 287 firms received the questionnaire and 106 submitted responses. The BoE surveyed 58 dual-regulated firms(14) and received 47 (81%) responses.(15) The FCA surveyed 229 FCA-regulated firms and received 63 (28%) responses.

The BoE selected firms with the aim of surveying each type of BoE and Prudential Regulation Authority (PRA)-regulated firm. This sample was determined to cover a significant share of BoE and PRA firms. It also included several firms that are small in terms of their market share but were considered to be advanced in the use of ML and therefore of interest for horizon-scanning purposes.

The FCA sample was built according to the following criteria. Sample selection reflected the need to represent firms that, due to their size and the number of customers, have the potential to affect the highest number of consumers, or are more likely to be anticipating future trends in the market, thus affecting consumers in the future. To meet these two objectives, for each FCA supervised sector, the FCA selected a sample of ‘large firms’ (among the largest sector firms in terms of income). Further, for each sector the FCA selected a sample of ‘fast growing firms’ (the sector firms with the highest income growth rate). This was judged to be the best way to get both an accurate snapshot of the state of ML at firms affecting a very large number of UK consumers, and a glimpse of where the market is heading.

Overall, the combined sample is skewed somewhat towards larger firms. In addition, it can be surmised that some firms did not respond to the survey because they have no ML applications and therefore the responses lean more towards firms that currently use ML. Therefore, the sample and survey findings should not be seen as representative for all types of firms or the entire UK financial services industry. The findings presented in this report should instead be considered as a snapshot of ML adoption. Our hope is that this will serve as a benchmark for future research and will stimulate debate.

The case studies presented in the Appendix were selected based on the number of responses received, ie we selected the most common use cases reported by participating firms.

The results presented in this report are anonymised and aggregated with the respondents grouped into the sectors listed in Box 2.

All charts in this report are based on data from the BoE and FCA survey.

### Sector classification used in the report


[p. 7]

|Sector|Type of firms included(1)|
|---|---|
|Banking|Building Societies, International Banks, Retail Banks, UK Deposit Takers, Wholesale Banks.|
|Insurance|General Insurers, Insurance Intermediaries, Life Insurers, Personal and Commercial Lines Insurers.|
|Non-Bank Lending|Debt Administrators, Credit Brokers, Crowdfunders, Debt Purchasers/Collectors, Lifetime MortgageProviders, Consumer Credit Lenders, Motor Finance Providers, Non-bank Lenders, Retail Finance Providers.|
|Investments and Capital Markets|Alternatives, Corporate Finance Firms, Fund Managers, Principal Trading Firms, Wealth Managers andStockbrokers, Wholesale Brokers.|
|Payments, Financial MarketInfrastructure (FMI)and other|Credit Reference Agencies, Custody Services, E-money Issuers, Exchanges, Financial Market Infrastructure,Multilateral Trading Facilities, Payment Services Firms, Platforms, Price Comparison Websites,Providers of Credit Information Services.|

(1) Listed alphabetically and based on BoE, PRA and FCA classifications.

> (14) Regulated by both PRA and FCA as well as Financial Market Infrastructure firms, which are regulated by the BoE not PRA.

> (15) In addition, four BoE/PRA-regulated firms did not submit complete responses because they do not have any ML applications.


---

[source overview](overview.md) | [next part](text-002.md)

[^original]: Financial Conduct Authority, "Machine learning in UK financial services" (2019-10). https://www.fca.org.uk/publication/research/research-note-on-machine-learning-in-uk-financial-services.pdf
