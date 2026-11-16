---
type: Source Text
title: The EBA publishes follow-up Report on the use of machine learning for internal ratings-based models - part 1 of 3 (pp. 1-7)
description: 'Verbatim extracted text, pp. 1-7: MACHINE LEARNING FOR IRB MODELS; 1. Executive Summary; 2. Introduction; and 1 more sections'
resource: https://www.eba.europa.eu/publications-and-media/press-releases/eba-publishes-follow-report-use-machine-learning-internal
tags:
- eu
- explainability
- guidance
- model_governance
- model_validation
- regulatory_expectation
status: stable
source_id: eba-the-eba-publishes-follow-up-report-on-the-use-of-machine-learning
issuer: eba
issuer_name: European Banking Authority
jurisdictions:
- EU
tier: 1
instrument_type: guidance
normative_force: regulatory_expectation
publication_date: '2023-08-28'
legal_status: current
part: 1
parts_total: 3
content_mode: full_text
generated:
  by: process:fincrime-kb-build
  at: '2026-11-16T16:23:02Z'
verified:
- by: process:kb-validate/verbatim-coverage
  at: '2026-11-16T16:23:02Z'
sources:
- id: original
  resource: https://www.eba.europa.eu/publications-and-media/press-releases/eba-publishes-follow-report-use-machine-learning-internal
  title: The EBA publishes follow-up Report on the use of machine learning for internal ratings-based models
  author: org:eba
  last_modified: '2023-08-28T00:00:00Z'
---

# The EBA publishes follow-up Report on the use of machine learning for internal ratings-based models

[source overview](overview.md) | [next part](text-002.md)

> Verbatim text extracted from the original (European Banking Authority, 2023-08-28), part 1 of 3, pp. 1-7. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **regulatory expectation**.[^original]

## MACHINE LEARNING FOR IRB MODELS


[pp. 1-2]

FOLLOW-UP REPORT FROM THE CONSULTATION ON THE DISCUSSION PAPER ON MACHINE LEARNING FOR IRB MODELS

EBA/REP/2023/28 AUGUST 2023

|1.|Executive Summary|3|
|---|---|---|
|2. I|ntroduction|4|
|3.|Selective use of ML for IRB models|6|
|3.1|ML techniques in the core modelling steps|6|
|3.2|ML techniques used for the validation via model challengers|7|
|3.3|ML techniques for collateral valuation|7|
|4.|Complexity of ML techniques|8|
|4.1|Statistical Issues (Overfitting)|9|
|4.2|Human Skills|9|
|4.3|Explainability|10|
|4.4|Categorisation of model changes|12|
|5. I|nteraction with (non-CRR) regulatory frameworks|13|
|5.1|Interaction with GDPR|13|
|5.2|Interaction with AI Act|15|
||5.2.1Clarification on the scope of application of the AI Act|15|
||5.2.2Additional requirements from the AI Act|16|
|6.|Way forward|19|
|Ann|ex I– Principle-based recommendations|20|
||Recommendations regarding the regulatory compliant use of ML techniqueof the IRB framework|s in the context20|

## 1. Executive Summary


[p. 3]

The aim of this follow-up report is to summarise the main conclusions from the consultation on the discussion paper (DP) on Machine learning (ML) used in the context of internal ratings-based (IRB) models. In addition, this report discusses the interaction between prudential requirements on IRB models and two other legal frameworks that have an impact on internal credit risk models that use ML techniques, namely the General Data Protection Regulation (GDPR) and the Artificial Intelligence (AI) Act.

The exponential increase in data availability and storing capacity coupled with the improvements in computing power of recent years provide an opportunity to use ML models. As presented in the DP, the follow-up report focuses on the more complex models than traditional techniques, such as regression analysis or simple decision trees, which are also the most difficult to understand and often less ‘transparent’.

In the context of credit risk, ML models might improve the predictive power and are not new to internal models used for credit approval processes. The result of the consultation suggests that financial institutions use or intend to use ML techniques only in some areas of IRB modelling, primarily for the PD estimation during the risk differentiation phase of the model development. Financial institutions use ML techniques to a lesser extent for model validation and collateral valuation.

The DP discussed as the main pivotal challenge for using ML techniques the complexity, which leads, to challenges in explaining their results. This goes hand in hand with the problem of traceability and ensuring an adequate understanding by the management functions. The result of the consultation suggests that in addition to those points, financial institutions have difficulty addressing the statistical issue of overfitting and acquiring a sufficient level of skilled labour. Furthermore, the industry mentioned the lack of clarity regarding how the prudential requirements on material model changes should be applied when using ML technique. Therefore, the report provides some clarifications on this point, noting the importance of the alignment with the regulatory framework.

Finally, the possible use of ML techniques in credit risk models may create concerns outside of the scope of prudential considerations. Two of the legal frameworks that addresses those concerns and that interact with the use of ML techniques for IRB models are the GDPR and the AI Act. This followup report discusses the interaction between prudential requirements on IRB models and requirements within those two regulations that may affect IRB models. In particular, the EBA fully supports the objective of the AI act, but is of the view that the text would benefit from further clarifications to ensure that no legal uncertainties remain after its adoption.

Altogether, this follow-up report aims to provide a conclusive picture on the current use of ML techniques for IRB models and analyses possible obstacles to the implementation of ML models in the IRB model space based on some practical issues, the experience made by the industry thus far and the current state of regulatory developments in this area.

## 2. Introduction


[p. 4] [ref: para 1]

1. The availability of financial markets data has undergone an exponential increase. At the same time the capacity to analyse data has increased substantially due to better computing capabilities and a growing use of Big Data and ML techniques.1 The use of ML techniques has also continuously increased in the banking sector over the years, with the main areas of application being fraud detection, AML/CFT, client and transaction profiling/clustering and realtime monitoring of payments.2 In the area of credit risk, EU financial institutions using ML techniques mainly use them in their credit worthiness assessment or credit scoring for credit granting.

2. ML techniques are however less used in the area of credit risk as regards determination of capital requirements. This can be partly ascribed to existing doubts about whether the ML techniques can comply with the regulatory requirements on the use of IRB models. This is in particular relevant, as the majority of financial institutions today use variants of regression analysis when using internal models to determine credit risk capital requirements, whereas the use of decision trees/ random forest or other ML techniques is limited to fewer financial institutions.

3. On 11 November 2021, the EBA published and consulted on the DP on ‘ _Machine learning for IRB models_ ’ with the aim to engage the industry and supervisory community to investigate the possible use of ML for IRB models and to build up a common understanding of the general aspects of ML for IRB models and the related challenges in complying with the regulatory requirements. The DP gave an overview of the challenges and opportunities stemming from the use of more advanced ML techniques, when applied in the context of IRB models to calculate regulatory capital for credit risk. It furthermore identified which characteristics of ML might make it more challenging or easier to comply with the regulatory requirements for IRB models.

4. The DP furthermore included a set of principle-based recommendations,3 to which ML techniques should adhere if banks wish to use them in the context of IRB models. This should ultimately ensure: i) a consistent and clear understanding of the prudential requirements, ii) an understanding of how new sophisticated ML models can adhere to those requirements and iii) that the setting of capital requirements continues to be harmonised across Europe.

5. ML covers a wide range of models with different levels of complexity. Just as in the DP, this report focuses on the more complex ML models,4 which are the most difficult to understand and

> 1 European Supervisory Authorities’ report on Digital Finance and related issues ESAs (January 2022), ESAs Final report on Digital Finance.

> 2 EBA Risk Assessment Questionnaire, Autumn 2022.

> 3 Section 4.3 of the DP on ML for IRB models and Annex I of this report.

[pp. 4-5] [ref: para 6]

> 4 The EBA has in previous communication (i.e. the report on BD&AA) used the definition of ML presented in the standard on IT governance ISO/IEC 38505-1:20175 which defines ML as a ‘process using algorithms rather than procedural coding that enables learning from existing data in order to predict future outcomes’. More details on the definition of ML are provided in section 2.1 of the DP on ML for IRB models. Please further note that this definition of ML may be different to the once used in other regulatory texts, e.g. the AI Act.

challenging to use within the IRB approach. For this report, the term ML should refer to _models characterised by a high number of parameters, that require a large volume of (potentially unstructured) data for their estimation and that are able to reflect non-linear relations between the variables_ . This entails that the use of regression models, which is the most commonly used approach in IRB models today, is not the focus of this report.

6. The EBA sought advice from the industry on 17 questions in the DP. During the three months consultation period, the EBA received 14 responses, of which three were confidential and eight were provided by associations.5 The responses generally reflected, that the implementation of ML techniques by financial institutions for prudential purposes related to credit risk is still at an early stage. The responses received from the industry therefore only reflect the short experience with ML techniques thus far or expectations about future use. Conclusions drawn from the consultation should therefore be taken with caution, as this is also a developing field within the industry.

7. While the EBA continues to monitor the developments of ML techniques for IRB models in the market and the new rules developed by legislators, several conclusions on the current application of such techniques can be drawn from the specific findings of the DP on ML for IRB models and the feedback received from the industry.

8. The industry feedback shows that financial institutions generally agree with the recommendations in the DP, and some elements, such as the application of the model changes framework in the context of ML models are further developed in this report based on the respondents’ feedback. Overall, the principle-based recommendations set out by EBA in the DP, and included in the Annex for reference, can therefore be used as a basis for development of ML models.6

9. In terms of organisation, section 3 elaborates on how financial institutions are currently selectively using ML for IRB modelling and section 4 elaborates on the additional complexity when using ML techniques for IRB models. Section 5 evaluates the interaction of ML techniques potentially used in IRB models with the GDPR and the AI Act. The report concludes with the way forward that the EBA expects to take in relation to the use of ML for IRB models (section 6).

[pp. 5-6]

> 5 The 14 responses (link) received came from six individual financial institutions and advisory services from DE, FR, IT and NL and from eight associations, representing financial and other institutions EU-wide or specifically in DE, ES, FR and IT. The associations generally represent a broad range of different types of financial institutions, such as wholesale, cooperative, mutual, retail, commercial and financial institutions.

> 6 As explained further down in this report, the principle based recommendation related to model changes has been refined based on the feedback received during the consultation.

- 10.In the DP, the potential challenges and benefits of using ML techniques were evaluated for different steps of the IRB modelling (risk differentiation, risk quantification, validation and others). During the consultation, financial institutions were asked to identify their use cases within those four steps. The findings of the consultation show that, if applied, ML techniques are used for some steps of the IRB Approach only. The following section elaborates on the main use case areas.

## 3. Selective use of ML for IRB models


[pp. 6-7] [ref: 3.1]

- 3.1 ML techniques in the core modelling steps

- 11.The feedback from the industry consultation showed that most of the institutions use or intend to use ML techniques for the development of PD models, even though the other parameters (LGD, EAD, ELBE and CCF models) were also mentioned, ML techniques are less frequently used for these parameters. One respondent further explained that ML techniques are used for the validation of the PD segmentation for the institution’s expected credit loss (ECL) model.

- 12.In the core modelling steps (i.e. risk differentiation and risk quantification) of the internal models, the industry confirmed that ML techniques were mainly used for risk differentiation. On the top of the arguments provided in the DP, namely that the use of complex ML techniques is not needed for the risk quantification, one respondent suggested that this choice is related to data availability. This is because the risk differentiation can be based on shorter time series, whereas risk quantification has to be based on long-run averages that require extended historical observation periods, which might not yet be available for new data sources which could be used by ML techniques.

- 13.Some of the use cases mentioned by the respondents for the model development were the use of random forests and Gradient Boosting Trees for the selection of risk drivers and clustering techniques for estimation of PD and LGD score ranges. In practice, the use was either for the input data, or to rank the exposures (e.g. scoring):

- a. For the input data, ML techniques can be useful in order to select the relevant variables that feed into the model through, for example, transformation of new data (text mining methods), completing missing data and the treatment and use of unstructured data.

- b. When it comes to ranking, the use of ML techniques might be especially beneficial in terms of model performance when risk differentiation performance has historically been poor, in particular for modelling non-linear relationships. The DP stated as a main benefit of using ML techniques that the use of such techniques can improve the models’ discriminatory power and provide useful tools for the identification of all relevant risk drivers or as a supporting

analysis for alternative assumptions or approaches (Article 190(2) of the CRR).7 These benefits have been confirmed by the industry.

- 3.2 ML techniques used for the validation via model challengers

- 14.Some respondents further reported that they use/intend to use ML techniques during the model validation. ML techniques are used, on the top of standard performance metrics used to assess the models, to develop challenger models (for example, for a robustness analysis and to challenge the variables of the final model developed) and for benchmarking purposes in the initial as well as ongoing validation. As such, ML techniques are mainly used in this context in order to improve the performance of challenger models and can be used as supportive analysis with regard to alternative assumptions or approaches.

[p. 7] [ref: 3.3]

- 15.The respondents also confirmed the challenges mentioned in the DP related to the interpretation of the outcome of the validation, including the resolution of its finding, and the increase in operational requirements (e.g. data quality, storage and maintenance). Most of the respondents further mentioned that specific skills and technical knowledge are needed to carry out the validation when the internal credit model uses ML techniques.

- 3.3 ML techniques for collateral valuation

- 16.Only a few respondents mentioned that ML techniques are used for collateral valuation, and if so, they are used for the estimation and monitoring of real estate values. However, supervisors in several jurisdictions are of the view that financial institutions might apply ML techniques for collateral valuation more frequently than indicated by the consultation responses, and reported that there are ongoing projects, where ML techniques are applied for collateral valuation. Those projects are already in the implementation phase. In one of the jurisdictions, it was reported that the development and implementation of the ML system to estimate real estate values is carried out by an external provider.

7 Article 41(b) of the Commission Delegated Regulation (EU) 2022/439 of 20 October 2021 (RTS on AM) and paragraph 220(b) of the Guidelines on PD estimation, LGD estimation and treatment of defaulted assets (GL on PD and LGD).


---

[source overview](overview.md) | [next part](text-002.md)

[^original]: European Banking Authority, "The EBA publishes follow-up Report on the use of machine learning for internal ratings-based models" (2023-08-28). https://www.eba.europa.eu/publications-and-media/press-releases/eba-publishes-follow-report-use-machine-learning-internal
