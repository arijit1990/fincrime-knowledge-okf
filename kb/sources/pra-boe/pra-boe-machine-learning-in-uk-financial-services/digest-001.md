---
type: Source Digest
title: Machine learning in UK financial services - part 1 of 2 (p. 1)
description: 'Verified paraphrased digest, p. 1: Machine learning in UK financial services > Executive summary; Machine learning in UK financial services > 1: Introduction; Machine learning in UK financial services > Box A: Definitions of ML, application, algorithm and model; and 4 more sections'
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
part: 1
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
digest_points: 68
---

# Machine learning in UK financial services (digest)

[source overview](overview.md) | [next part](digest-002.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (p. 1) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **empirical observation**.

## Executive summary

- **descriptive / finding or result**: The number of UK financial services firms using machine learning (ML) continues to rise: 72% of firms responding to the survey reported using or developing ML applications, which are becoming widespread across more business areas. (p. 1)[^original]  
  <sub>anchor: "72% of firms that responded to the survey reported using or developing ML applications"</sub>
- **descriptive / finding or result**: 79% of ML applications are in the latter stages of development, meaning deployed across a considerable share of business areas and/or critical to some business areas, so applications are more advanced and embedded in day-to-day operations. (p. 1)[^original]  
  <sub>anchor: "79% of ML applications are in the latter stages of development"</sub>
- **descriptive / finding or result**: 79% of respondents that use ML have a strategy for the development, deployment, monitoring and use of the technology. (p. 1)[^original]  
  <sub>anchor: "have a strategy for the development, deployment, monitoring and use of the technology"</sub>
- **descriptive / finding or result**: The most commonly identified current ML benefits are enhanced data and analytics capabilities, increased operational efficiency, and improved detection of fraud and money laundering. (p. 1)[^original]  
  <sub>anchor: "improved detection of fraud and money laundering"</sub>
- **descriptive / finding or result**: Respondents do not see ML, as currently used, as high risk. Top consumer risks relate to data bias and representativeness; top risks for firms are lack of explainability and interpretability of ML applications. (p. 1)[^original]  
  <sub>anchor: "Respondents do not see ML, as currently used, as high risk."</sub>
- **descriptive / finding or result**: The greatest constraint to ML adoption and deployment is legacy systems; difficulty integrating ML into business processes is next highest. (p. 1)[^original]  
  <sub>anchor: "The greatest constraint to ML adoption and deployment is legacy systems."</sub>
- **descriptive / finding or result**: Almost half of responding firms said PRA and/or FCA regulations constrain ML deployment, and a quarter of firms (25%) said this is due to lack of clarity in existing regulation. (p. 1)[^original]  
  <sub>anchor: "A quarter of firms (25%) said this is due to a lack of clarity within existing regulation."</sub>

## 1.1: Context and objectives

- **descriptive / context**: ML can bring benefits to consumers, firms, markets and the economy, and many firms already deploy it, but ML can also raise novel challenges (such as ethical issues) and amplify risks to consumers, firm safety and soundness and potentially financial stability. Regulators therefore need to monitor ML deployment and understand use cases, application maturity, benefits and risks. (p. 1)[^original]  
  <sub>anchor: "ML can also raise novel challenges (such as ethical issues) and amplify risks to consumers"</sub>
- **descriptive / context**: The Bank of England and FCA ran a joint ML survey in 2019, whose key findings included the need for further public-private dialogue for safe and responsible ML adoption. They established the Artificial Intelligence Public-Private Forum (AIPPF) in 2020 to explore barriers, challenges and mitigations. This report builds on the 2019 survey and the AIPPF final report. (p. 1)[^original]  
  <sub>anchor: "The Bank and FCA established the Artificial Intelligence Public-Private Forum (AIPPF) in 2020"</sub>
- **descriptive / context**: The joint report analyses responses to the 2022 survey and covers: a quantitative overview of ML use; firms' ML implementation strategies; share of applications developed in-house or by third-party providers; governance approaches; views on benefits; views on risks; constraints on development and deployment; and a snapshot of methods, data, safeguards, performance metrics, validation techniques and perceived complexity. (p. 1)[^original]  
  <sub>anchor: "the share of ML applications developed in-house or by third-party providers"</sub>
- **descriptive / context**: The report closes with ML case studies on typical use cases: insurance pricing and underwriting, credit underwriting, marketing, and fraud prevention and anti-money laundering (AML). (p. 1)[^original]  
  <sub>anchor: "Fraud prevention and anti-money laundering (AML)."</sub>

## 1.2: Methodology

- **descriptive / method**: 168 firms received the questionnaire and 71 responded (42% overall response rate). The Bank surveyed 48 dual-regulated firms, 17 firms applying for PRA authorisation as a deposit-taker and eight Bank-regulated financial market infrastructures (FMIs), receiving 51 responses (70%). The FCA surveyed 95 FCA-regulated firms and received 20 responses (21%). (p. 1)[^original]  
  <sub>anchor: "168 firms received the questionnaire and 71 submitted responses (42% overall response rate)"</sub>
- **descriptive / method**: The Bank selected firms to survey each type of FMI and PRA-regulated firm and cover a significant share of them, plus several firms small by market share but considered advanced in ML use for horizon-scanning, and some FCA-regulated small firms going through PRA authorisation for deposit-taking permissions. (p. 1)[^original]  
  <sub>anchor: "considered to be advanced in the use of ML and therefore of interest for horizon-scanning purposes"</sub>
- **descriptive / limitation**: The combined sample is skewed towards larger firms, with no responses from smaller fintech firms or start-ups. Firms may be more likely to respond if already using or developing ML. The sample gives broad representation by activity, size and ML application areas, but the sample and findings should not be seen as representative of all firm types or the entire UK financial services industry. (p. 1)[^original]  
  <sub>anchor: "the combined sample is skewed towards larger firms with no responses received from smaller fintech firms or start-ups"</sub>

## Table A: Sector classification used in the survey and report

- **descriptive / context**: Results are anonymised and aggregated by sector (Table A): Banking covers building societies, international banks, retail banks and UK deposit-takers; Insurance covers general, health, life, and personal and commercial lines insurers; Non-bank lending covers credit brokers, consumer credit lenders and non-bank lenders; Investment and capital markets covers alternatives, asset managers, fund managers, wealth managers and stockbrokers, and wholesale brokers; FMIs, payments and other covers credit reference agencies, e-money issuers, exchanges, financial market infrastructures and multilateral trading facilities. (p. 1)[^original]  
  <sub>anchor: "|Banking|Building societies, international banks, retail banks, UK deposit-takers|"</sub>

## Footnotes

- **descriptive / context**: Table A is sourced to the Bank of England and the FCA. All charts in the report are based on data from survey respondents, and in designing the survey the Bank and FCA considered the Legislative and Regulatory Reform Act 2006 principle that regulatory activities should be transparent and proportionate. (p. 1)[^original]  
  <sub>anchor: "regulatory activities should be carried out in a way which is transparent and proportionate"</sub>
- **descriptive / definition**: For the survey, ML is a methodology whereby computer programmes build a model to fit a set of data, usable for predictions, recommendations or decisions without being explicitly programmed, learning from sample data or experience. Approaches include supervised, unsupervised and reinforcement learning. The survey excludes simple linear regression, defined as any regression technique that does not employ subset selection, shrinkage or dimension reduction methods. (p. 1)[^original]  
  <sub>anchor: "For the purpose of this survey, this excludes simple linear regression"</sub>

## Box A: Definitions of ML, application, algorithm and model

- **descriptive / definition**: An 'ML application' is an entire system, including data collection, feature engineering, model engineering and deployment, plus underlying IT infrastructure (for example virtualisation, data storage and integrated development environment); it may include multiple models and algorithms. Respondents classified applications separately if they serve different business purposes or differ significantly in set-up or components. (p. 1)[^original]  
  <sub>anchor: "‘ML application’ refers to an entire system, including data collection, feature engineering, model engineering, and deployment."</sub>
- **descriptive / definition**: An 'algorithm' is a set of mathematical instructions or rules that helps calculate an answer to a problem; a 'model' is a quantitative method, system or approach applying statistical, economic, financial or mathematical theories, techniques and assumptions to process input data into output, where inputs and outputs may be quantitative or qualitative (including expert judgement). In ML, an algorithm is a procedure run on data to create a model. (p. 1)[^original]  
  <sub>anchor: "In ML, an algorithm is a procedure that is run on data to create a model."</sub>

## 2.1: Financial services firms use an increasing number of ML applications

- **descriptive / finding or result**: 72% of responding firms reported using or developing ML applications, versus 67% in the 2019 survey (the sample size and composition differed). As in 2019, banking and insurance respondents have the highest number of ML applications. (p. 1)[^original]  
  <sub>anchor: "This compares to 67% of respondents to the 2019 survey"</sub>
- **descriptive / finding or result**: Respondents expect the overall median number of ML applications to rise over 3.5 times in three years, in line with the 2019 survey trend; the largest expected increase is in insurance, where median applications per firm are expected to rise by 163%. (p. 1)[^original]  
  <sub>anchor: "the median number of applications per firm expected to increase by 163%"</sub>

## 2.2: Deployment stage

- **descriptive / finding or result**: 79% of ML applications are in deployment (Chart 3): 65% deployed across a considerable share of business areas and a further 14% critical to the business area. Pre-deployment stages held 44% of applications in 2019 versus 10% in 2022 (the 2019 question differed somewhat), suggesting applications are more advanced and embedded in day-to-day operations. (p. 1)[^original]  
  <sub>anchor: "65% of applications are already deployed across a considerable share of business areas"</sub>

## Chart 3: Overall, 80% of ML applications are in deployment or critical stages

- **descriptive / finding or result**: The Chart 3 title states that 80% of ML applications are in deployment or critical stages, whereas the surrounding text gives 79%. (p. 1)[^original]  
  <sub>anchor: "Overall, 80% of ML applications are in deployment or critical stages"</sub>
- **descriptive / finding or result**: Banks, insurance and FMIs/payments/other firms have broadly similar splits across deployment stages (Chart 4). Non-bank lenders have the highest share of applications critical to business areas (42%) with only 3% in pre-deployment. Investment and capital markets respondents have the largest number of applications in the pilot or small-share stage and no critical applications. (p. 1)[^original]  
  <sub>anchor: "Non-bank lenders have the highest percentage of ML applications (42%) that are critical to business areas"</sub>
- **descriptive / finding or result**: By use case (Chart 5), 'customer engagement' and 'risk management' have the most applications, at 28% and 23% of all reported applications. The 'miscellaneous' category (including human resources and legal) is third at 18%. The fewest are in 'investment banking' (0.9%) and 'treasury' (0.4%), treasury also being lowest in 2019. (p. 1)[^original]  
  <sub>anchor: "account for 28% and 23% of all reported applications respectively"</sub>

## Chart 5: Over half of ML applications are in customer engagement or risk management

- **descriptive / finding or result**: By maturity per business area (Chart 6), 'customer engagement' has the highest share of post-deployment applications (97%). 'Investment banking' and 'treasury' have the highest shares at pre-development stages, 58% and 40% respectively. Treasury (40%) and credit (34%) have the most applications rated 'critical to business area'. Investment banking and asset management have no critical ML applications. (p. 1)[^original]  
  <sub>anchor: "‘customer engagement’ (97%) has the highest percentage of post-deployment applications"</sub>
- **descriptive / finding or result**: The survey compared internally implemented ML applications with those implemented externally by third parties (where the majority of development or deployment was done by a third party). The line between internal and external is increasingly blurred because ML systems rely on a mix of internal and external components (data inputs, models, software packages, cloud storage); for example, firms may build models internally but use third-party data sets or third-party cloud platforms. (p. 1)[^original]  
  <sub>anchor: "the line between ‘internal’ and ‘external’ implementation is becoming increasingly blurred"</sub>

## 2.4: Internal versus external implementation and cloud computing

- **descriptive / finding or result**: A 2020 Bank survey suggested more outsourcing to external vendors, but this survey did not show that: 83% of respondents develop and implement ML applications internally (76% in 2019). Investment and capital markets has the largest use of third-party ML applications (39%). (p. 1)[^original]  
  <sub>anchor: "83% of respondents develop and implement ML applications internally at their firm"</sub>
- **descriptive / finding or result**: Overall 18% of ML applications run on cloud computing platforms (22% in 2019), with marked sector differences (Chart 8): insurance 74%, investment and capital markets 39%, non-bank lenders 11%, banks 8%. The insurance figure is significantly higher than the 31% reported by insurers in 2019. (p. 1)[^original]  
  <sub>anchor: "insurance firms reported that nearly three quarters (74%) of their applications run on cloud computing platforms"</sub>

## Chart 8: Almost three quarters of insurance firms' ML applications run on the cloud

- **descriptive / finding or result**: Firms use a wide range of third-party data and model providers (Chart 9), but cloud service providers are concentrated: the top two providers account for 75% of firms using cloud services and the top provider for 43%. (p. 1)[^original]  
  <sub>anchor: "the top two providers accounting for 75% of firms that use cloud services"</sub>
- **descriptive / finding or result**: In 2022, 79% of respondents had some form of strategy for the development, deployment, monitoring and use of ML (Figure 1), up from mostly banking and insurance in 2019. By sector: insurance 100%, non-bank lenders 83%, banks 78%, investment and capital markets 70%, FMIs/payments/other 60%. (p. 1)[^original]  
  <sub>anchor: "100% of insurance firms had a strategy, as did 83% of non-bank lenders, 78% of banks"</sub>

## 3.1: Firms’ ML strategies

- **descriptive / finding or result**: Respondents use elements of existing strategies to support ML: 38% have a model risk management (MRM) strategy incorporating ML and 25% include ML in a wider data, innovation or technology strategy. Wider governance frameworks and ethical principles such as fairness or bias in decision-making also feed the ML strategy. (p. 1)[^original]  
  <sub>anchor: "38% of respondents have a model risk management (MRM) strategy that incorporates ML"</sub>
- **descriptive / finding or result**: 29% of firms have specific teams responsible for developing and deploying ML, often cross-functional teams enabling deployment across multiple business cases and sometimes also monitoring ML model risks and outputs. Many firms not using ML say it is not a priority given their size, scope or focus. (p. 1)[^original]  
  <sub>anchor: "29% of firms have specific teams that are responsible for the development and deployment of ML"</sub>

## 3.2: Firm ML governance and accountability

- **descriptive / context**: The report says good governance is essential for safe adoption and use of ML: it underpins effective risk management across the ML lifecycle through rules, controls, policies and processes, ensures accountability for ML applications and is vital for safe and responsible use. (p. 1)[^original]  
  <sub>anchor: "Good governance is essential for the safe adoption and use of ML in financial services."</sub>
- **descriptive / finding or result**: Many respondents use existing governance frameworks (such as MRM and operational risk management) for ML (Chart 10); 80% have data governance frameworks in place; just over two thirds (67%) have AI/ML-specific principles, guidelines and standards, possibly reflecting that ML can pose novel challenges needing specific governance principles (as noted in the AIPPF final report). (p. 1)[^original]  
  <sub>anchor: "Just over two thirds of respondents (67%) have AI/ML specific principles, guidelines, and standards in place"</sub>

## 3.3: Lessons learnt from ML deployment

- **descriptive / finding or result**: The most common lesson respondents cite is the need for good and effective governance frameworks (such as MRM), in particular clear lines of ownership of the ML application within the business to allow effective risk management. (p. 1)[^original]  
  <sub>anchor: "clear lines of ownership of the ML application within the business to allow for effective risk management"</sub>
- **descriptive / finding or result**: Respondents emphasised continuous review and assessment of ML applications to ensure accurate and fair outputs, including assessing potential bias in decisions affecting consumers; knowing when to retire and replace models; understanding models and outputs for explainability and transparency; and, for some, clear metrics, a framework and baseline metrics to define and measure successful outcomes. (p. 1)[^original]  
  <sub>anchor: "key to know when best to retire and replace ML models"</sub>
- **descriptive / finding or result**: Respondents said well-trained teams are crucial for implementing and monitoring ML; cross-functional, multi-disciplinary teams tend to be most effective at developing and deploying safe and responsible ML; and comprehensive staff training and culture matter for safe and responsible adoption. (p. 1)[^original]  
  <sub>anchor: "cross-functional, multi-disciplinary teams tend to be the most effective at developing and deploying ML applications"</sub>

## 4.1: Benefits, risks and trade-offs

- **descriptive / context**: ML can bring benefits to consumers (more personalised products and services, better engagement), firms (improved data analytics, operational efficiencies) and, in aggregate, the financial system and economy. It can also amplify existing challenges and risks, many traceable to three drivers and lifecycle stages: (i) data, (ii) models and (iii) governance (Figure 2). (p. 1)[^original]  
  <sub>anchor: "(i) data, (ii) models, and (iii) governance (Figure 2)"</sub>
- **descriptive / context**: Historical biases in data sets and poor-quality data can feed into modelling and cause model risk; ML can increase model complexity, lack of explainability and other model risk; effective governance and accountability are key mitigants, but weak ML governance can exacerbate the issues and is itself a challenge. (p. 1)[^original]  
  <sub>anchor: "historical biases in data sets and poor-quality data can feed into the modelling and cause subsequent model risk"</sub>

## Figure 2: Stages of ML lifecycle

- **descriptive / context**: Figure 2 (stages of the ML lifecycle) is sourced to the Artificial Intelligence Public-Private Forum. (p. 1)[^original]  
  <sub>anchor: "- Source: Artificial Intelligence Public-Private Forum."</sub>
- **descriptive / finding or result**: Although one might expect greater perceived risk to go with greater perceived benefit, survey responses show no significant association between average perceived risk and average perceived benefit (Chart 11). (p. 1)[^original]  
  <sub>anchor: "the survey responses show no significant association between average perceived risk and average perceived benefit"</sub>
- **descriptive / finding or result**: Benefits are most likely in enhanced data and analytics capabilities, increased operational efficiency and improved combatting of fraud and money laundering (Chart 12). All benefits are expected to increase over three years, the greatest increase being in better personalisation and improved customer engagement. (p. 1)[^original]  
  <sub>anchor: "improved combatting of fraud and money laundering (Chart 12)"</sub>

## Overview

- **descriptive / finding or result**: The primary drivers of ML risk are interconnected risks at the data level, feeding the model level and raising broader challenges for the firm and its governance of ML systems. Respondents rated risks across those three drivers plus risks to consumers, regulation and others such as cybersecurity and outsourcing. (p. 1)[^original]  
  <sub>anchor: "interconnected risks at the data level, which feed into the model level"</sub>
- **descriptive / finding or result**: Respondents rate current risk as low to medium in all categories and expect similar levels over three years. The highest perceived risks are for consumers, while for firms respondents see model-related risks, rather than data or governance, as highest (Chart 13). (p. 1)[^original]  
  <sub>anchor: "respondents consider the current levels of risk to be low to medium across all risk categories"</sub>

## Chart 13: Overall levels are low to medium across all risk categories

- **descriptive / finding or result**: Respondents said lack of explainability in both the workings and outcomes of ML applications is a key risk, which can lead to inaccurate consumer outcomes and then reputational and legal risk to firms. Many also highlighted data quality, structure and bias. (p. 1)[^original]  
  <sub>anchor: "the lack of explainability in both the workings and outcomes of ML applications are a key risk"</sub>
- **descriptive / finding or result**: More than half of firms (52%) are concerned about ethical and bias issues from ML, which can reduce consumers' ability to use products and services, damage reputation and cause operational costs and service breakdowns. Respondents also highlighted outsourcing risk, including third-party compliance with firms' governance and data sharing frameworks. (p. 1)[^original]  
  <sub>anchor: "More than half of firms (52%) noted that the use of ML causes concern about potential ethical and bias issues"</sub>
- **descriptive / finding or result**: Top ML-related risks as reported: biases in data, algorithms and outcomes (52%); data quality and structure issues (43%); lack of explainability in the model and outcome (36%), leading to inaccurate predictions (34%) and in turn poor decisions and reputational damage (11%); inadequate controls or governance (25%); outsourcing or third-party risks (16%). (p. 1)[^original]  
  <sub>anchor: "biases in data, algorithms and outcomes (52%); data quality and structure issues (43%)"</sub>
- **descriptive / finding or result**: 14% of respondents report ML may amplify existing risks and challenges. Half say ML in their firms could lead to novel risks, 23% see no novel risks and 27% gave no comment. (p. 1)[^original]  
  <sub>anchor: "Half of the survey respondents say the use of ML within their firms could lead to novel risks"</sub>
- **descriptive / finding or result**: Among novel risks identified, 13% of respondents highlighted unethical and biased outcomes, particularly harmful for vulnerable consumers, and 9% highlighted increased reputational damage from deploying risky ML. (p. 1)[^original]  
  <sub>anchor: "13% of respondents highlighted the risk related to unethical and biased outcomes"</sub>
- **descriptive / finding or result**: On mitigation, respondents said effective governance frameworks (such as MRM and data-quality validation) are key, including assessment and review of ML models from development through deployment; clear lines of accountability are key, with some using 'human in the loop' processes so a human is accountable for autonomous decisions; and some suggested consumer protection and prudential regulation could mitigate some ML risks. (p. 1)[^original]  
  <sub>anchor: "‘human in the loop’ processes to ensure there is a human accountable for any autonomous decisions"</sub>

## Risks to consumers

- **descriptive / finding or result**: Respondents expect most consumer risks to decrease over three years, except risks related to third-party data, ML ethics and model complexity. The top three consumer risks are data bias and representativeness, bad consumer outcomes and identification of vulnerability; the risks expected to fall most are 'weak model implementation' and 'skills base and culture'. (p. 1)[^original]  
  <sub>anchor: "data bias and representativeness, bad consumer outcomes, and identification of vulnerability"</sub>
- **descriptive / finding or result**: The overall level of perceived risk to firms is similar to that for consumers but specific risks rank differently. The three highest perceived risks to firms are explainability and interpretability, data bias and representativeness, and model complexity. (p. 1)[^original]  
  <sub>anchor: "explainability and interpretability, data bias and representativeness, and model complexity"</sub>

## Chart 14: Most ML risks to consumers expected to decrease over the next three years

- **descriptive / context**: Chart 14 shows that most ML risks to consumers are expected to decrease over the next three years. (p. 1)[^original]  
  <sub>anchor: "Most ML risks to consumers expected to decrease over the next three years"</sub>

## Risks to firms

- **descriptive / finding or result**: Most risks to firms are expected to stay constant over three years; as with consumer risks, use of third-party data, ML ethics and model complexity are expected to increase, while skills base and culture and effective governance structure are expected to decrease most. Results largely align with AIPPF findings. (p. 1)[^original]  
  <sub>anchor: "The risks expected to decrease the most are skills base and culture and effective governance structure."</sub>
- **descriptive / finding or result**: The greatest perceived constraint on deploying ML is legacy systems and technology infrastructure (as in 2019), since ML applications often need up-to-date hardware, database infrastructure and operating systems; developing, deploying or integrating ML with legacy systems is the second highest reported challenge. (p. 1)[^original]  
  <sub>anchor: "The greatest perceived constraint is legacy systems and associated technology infrastructure"</sub>

## 4.4: Constraints to deployment

- **descriptive / finding or result**: The third highest challenge is that ML is not a priority at this time, and the fourth is a lack of sufficient skills. As the AIPPF final report notes, skills gaps can be significant in development and implementation and also in ongoing monitoring and risk management; skills may also be insufficient to understand and manage third-party models or data. (p. 1)[^original]  
  <sub>anchor: "the fourth biggest challenge is a lack of sufficient skills"</sub>
- **descriptive / finding or result**: Financial services regulation may constrain ML if perceived compliance burden and costs outweigh benefits. Almost half of firms said PRA and/or FCA regulations constrain ML deployment, though 30% called it a small constraint and only 5% a large constraint (Chart 17). A quarter said this was due to lack of clarity in existing regulation and 22% thought existing regulation is itself a constraint. (p. 1)[^original]  
  <sub>anchor: "only 5% noting that sectoral regulation is a large constraint (Chart 17)"</sub>

## 4.5: Regulation

- **descriptive / context**: The Bank, PRA and FCA are exploring, via the joint Discussion Paper, how the current regulatory framework applies to AI/ML, whether further clarification would help and how policy can best support safe and responsible AI/ML adoption. (p. 1)[^original]  
  <sub>anchor: "how the current regulatory framework applies to AI/ML, whether additional clarification"</sub>

## 5.1: Purpose and background

- **descriptive / method**: 45 firms responded to the first case study (most advanced application) and 34 to the second (critical business area), with limited overlap. Ten respondents using ML elsewhere said they do not use it in any critical business area. Case studies were selected by response numbers and so reflect the most commonly reported use cases in the sample. (p. 1)[^original]  
  <sub>anchor: "45 firms responded to the first case study (most advanced ML application) and 34 responded"</sub>
- **descriptive / finding or result**: Across both case studies the ML techniques most often used are at the more complex end of the spectrum: tree-based models, regression (excluding simple linear regression) and neural networks (Chart 18). The 'other' category included Bayesian approaches, alternating least squares, grid search techniques and image recognition techniques. Some firms were unsure of the underlying model because a third-party provider built it. (p. 1)[^original]  
  <sub>anchor: "The most commonly used ML methods are tree-based models, regression (excluding simple linear regression), and neural networks"</sub>

## Chart 18: Tree-based models are the most popular ML techniques

- **descriptive / finding or result**: Firms often use tree-based ensembles such as random forests and XGBoost, which average predictions from many often large decision trees, and respondents said these have been relatively successful for prediction in traditional financial data analysis. Neural networks tend to forecast from historical information and find complex relations between non-linear variables. Logistic and penalised regression are used for forecasting and time series modelling. Most applications used on average a combination of two methods, and one firm used nine separate techniques in one application. (p. 1)[^original]  
  <sub>anchor: "In one use case, a firm used nine separate ML techniques in a single application."</sub>
- **descriptive / data or feature**: Almost all use cases in both advanced and critical deployments relied on structured data. Fewer than 10% of respondents used novel data sources, such as unstructured and semi-structured data, in critical areas, though these were more common in some advanced-deployment case studies. (p. 1)[^original]  
  <sub>anchor: "Almost all the use cases where ML was deployed in both advanced and critical areas relied on structured data."</sub>

## Executive summary

- **descriptive / finding or result**: Survey respondents anticipate that the overall median count of ML applications will grow 3.5-fold across the following three years, with insurance expected to see the biggest increase in absolute terms and banking next. (p. 1)[^original]  
  <sub>anchor: "firms expect the overall median number of ML applications to increase by 3.5 times over the next three years"</sub>
- **descriptive / finding or result**: Firms address ML use through their existing governance frameworks: among respondents using ML, 80% report that their applications are covered by data governance frameworks, while model risk management and operational risk frameworks are also widespread, at 67%. (p. 1)[^original]  
  <sub>anchor: "80% of respondents that use ML say their applications have data governance frameworks in place"</sub>

## 1.2: Methodology

- **descriptive / method**: The FCA distributed the survey to a representative selection of firms drawn from these sectors: payment services, e-money issuers, consumer credit providers, motor finance providers, retail finance providers, credit brokers, debt purchasers, debt administrators, non-bank lenders, lifetime mortgage providers, credit referencing agencies, crowdfunders, custody services, exchanges, multilateral trading facilities, fund management, alternatives, principal trading firms, wholesale brokers, and wealth manager and stock brokers. Firms that had answered the 2019 survey were also included. (p. 1)[^original]  
  <sub>anchor: "credit referencing agencies, crowdfunders, custody services, exchanges, fund management, alternatives, lifetime mortgage providers"</sub>

## 2.2: Deployment stage

- **descriptive / method**: Because ML applications move through several development and deployment stages, the survey had firms state how many applications sit at each of five stages: proof-of-concept or experimental; front-line research and development and/or benchmarking of existing models; pilot and/or used in a small share of a business area; deployed across a considerable share of a business area; and critical to a business area. (p. 1)[^original]  
  <sub>anchor: "(i) proof-of-concept or experimental, (ii) front-line research and development and/or used for benchmarking existing models"</sub>

## 4.5: Regulation

- **descriptive / method**: The survey posed more detailed questions about two case studies, namely the firm's most advanced ML application by deployment and the ML application used within a critical business area (even if only on a small scale); the aim was to examine the specific business contexts in which ML models were used. (p. 1)[^original]  
  <sub>anchor: "the most advanced ML application in terms of deployment and (ii) the ML application deployed"</sub>

---

[source overview](overview.md) | [next part](digest-002.md)

[^original]: Prudential Regulation Authority / Bank of England, "Machine learning in UK financial services" (2026-08-28). https://www.bankofengland.co.uk/report/2022/machine-learning-in-uk-financial-services
