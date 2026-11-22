---
type: Source Text
title: The EBA publishes follow-up Report on the use of machine learning for internal ratings-based models - part 2 of 3 (pp. 8-18)
description: 'Verbatim extracted text, pp. 8-18: 4.Complexity of ML techniques; 4.Complexity of ML techniques > 4.1 Statistical Issues (Overfitting); 4.Complexity of ML techniques > 4.2 Human Skills; and 5 more sections'
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
part: 2
parts_total: 3
content_mode: full_text
generated:
  by: process:fincrime-kb-build
  at: '2026-11-22T10:06:32Z'
verified:
- by: process:kb-validate/verbatim-coverage
  at: '2026-11-22T10:06:32Z'
sources:
- id: original
  resource: https://www.eba.europa.eu/publications-and-media/press-releases/eba-publishes-follow-report-use-machine-learning-internal
  title: The EBA publishes follow-up Report on the use of machine learning for internal ratings-based models
  author: org:eba
  last_modified: '2023-08-28T00:00:00Z'
---

# The EBA publishes follow-up Report on the use of machine learning for internal ratings-based models

[previous part](text-001.md) | [source overview](overview.md) | [next part](text-003.md)

> Verbatim text extracted from the original (European Banking Authority, 2023-08-28), part 2 of 3, pp. 8-18. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **regulatory expectation**.[^original]

## 4.Complexity of ML techniques


[p. 8]

- 17.The DP highlighted the key challenges when developing and validating IRB models using ML techniques. These include aspects related to: i) statistical issues, ii) skill-related issues, and iii) interpretation/explainability issues. In general, it is clear that the use of ML techniques brings specific challenges in relation to the complexities of the approaches used. Finally, this section considers the interaction with the existing regulatory model change framework.

18.In relation to statistical issues:

- a. The DP discussed in detail the challenge of dealing with overfitting (i.e. performance optimisation of the development sample, but not confirmed on the current and foreseeable application portfolio). As such, the DP highlighted that financial institutions are expected to put particular attention on the comparison of the model performances measured within the development sample with those obtained using out-of-sample and out-of-time data sample (related to the requirements in Article 175(4)(b) of the CRR).

- b. In addition, the DP discussed the difficulty to assess the representativeness of data and to fulfil operational data requirements (e.g. data quality or data storage and maintenance) in relation to the inputs of the models, when using ML techniques. Extra care should be taken in evaluating the quality of the data input to avoid cases where the score obtained by a ML technique is used as an explanatory variable for another model which could lead to feedback loops.

- 19.In relation to skill-related issues, the DP identified challenges posed by ML techniques for both the Credit Risk Control Unit (CRCU) and the validation function:

- a. Common general challenges are related to the complexity of ML techniques, which may increase the time, computational/IT and human resources (both in terms of number and level of expertise) for developing and validating them.

- b. Furthermore, the complexity of ML techniques may make the assessment of the modelling assumptions, and whether the selected risk drivers contribute to the risk assessment in line with their economic meaning (as required by Article 174(e) of the CRR), more challenging. This could make it more difficult to comply with the CRR requirement to complement the development and application of the model with human judgement. Expert judgment may also be used when setting the hyperparameters that are required by specific ML techniques.

- c. Lastly, when it comes to the validation function, the DP recalled that it is expected to analyse and challenge the model design, assumptions and methodology (Article 185 CRR). A more complex model will be harder to challenge efficiently. The validation of the hyperparameters may require additional statistical knowledge, and institutions should therefore ensure that the staff in the validation function is appropriately trained.

[p. 9]

- 20.In relation to interpretation issues, the DP pointed to the challenge to comply with Article 171(1)(a) and (b) of the CRR which requires to have consistent and appropriate assignment criteria and to document them in a way that allows the assignment process to be complemented by human judgement.

- 21.The responses to the consultation confirmed that issues related to the overfitting, the skills of developers and validators and the interpretation issues are the main challenges during the development and validation phase.

- 22.The industry confirmed that overfitting is a key challenge regarding the development of ML models. More precisely, one respondent pointed out that the use of ML techniques may be more challenging for low-default portfolios as they often require larger datasets to implement a proper model training, validation and testing.

### 4.1 Statistical Issues (Overfitting)


- 23.One respondent further explained that the complexity of ML models makes it difficult to use an adapted standardised model development and validation process. ML models are constantly evolving and the effectiveness of these techniques derives from the case-by-case choice of the best methodology. It is therefore difficult to implement a standardised model development process without hampering the effectiveness of the ML techniques.

- 24.Respondents to the consultation elaborated on various strategies they use/intend to use to overcome the overfitting issue which are not necessarily exclusively applied for ML techniques used for IRB models. They referred in particular to several statistical techniques, such as specific techniques to build the model (several respondents mentioned specific methods related to the choice of risk drivers, such as feature selection and normalisation), ensure the stability of the model and validate it via the use of out-of-time and out-of-sample tests (several respondent mentioned specific types of cross-validation). In the context of ML models, additional dedicated tools may be necessary, in particular in relation to the hyperparameters of the models. In addition, the respondents also stressed the importance of other approaches, based on an evaluation of the consistency of the model with economic theory (i.e. improving explainability, issue discussed in section 4.3, as a way of increasing the generalisation capacity of the model).

### 4.2 Human Skills


[pp. 9-10]

- 25.The feedback from financial institutions showed that the additional know-how skills include: theoretical knowledge of ML techniques, including how to assess the soundness of a proposed methodology; knowledge about the mathematical and statistical understanding of ML techniques; and how to evaluate model stability and overfitting. Further, additional practical knowledge of ML, including knowledge about hyperparameter tuning methods, about alternative methods for testing the model stability and knowledge of statistical and programming skills (e.g. standard programming libraries for ML), is required. Financial institutions stated that the required knowledge could be gained by hiring ML experts, organising

in-house as well as external trainings, and enhancing mobility within the organisation in order to learn from experts in other areas.

- 26.Some financial institutions confirmed that the use of ML techniques during the model development might create additional challenges to enable human judgement. They confirmed that expertise with ML methods and techniques is important to ensure that the tools used to develop the models are adequate and well understood. One association believed that this is the greatest challenge regarding the development of ML models in the IRB context. Some respondents further acknowledged that the treatment of large amounts of data requires different controls, more capability and IT expertise than traditional methods.

- 27.Financial institution’s feedback was also in line with CRR requirements that it is important to ensure not only a higher level of expertise, but also the possibility that humans can intervene during the process of development and application of the model. They stated that human intervention should be used for feature selection to ensure that those features are complete and sound from a business and economic perspective. The possibility of human intervention is also important during the assessment of the final model.

- 28.However, while financial institutions reported that having the right ML expertise is a main challenge for them, they generally do not outsource or plan to outsource the development of the ML models. If they do so, it is limited to the development phase of the internal model and is carried out via third-party support. One respondent to the consultation further pointed out that for ML models there is often a worry about intellectual property, which can make it more difficult to work with externals.

- 29.Some financial institutions confirmed the challenges pointed out by the DP during the model validation. They stated that the complexity of ML techniques may increase the time, computational/IT and human resources needed for validating. This is because using ML techniques could increase the need for more tests and methodologies to check the stability of the model; for efforts to build challenger models; for checking of data sources where a lot of data are used or data from new sources are used (e.g. social media) and; potentially increase frequency of model monitoring or validation for often changing models. However, for a few respondents, the additional needed know-how does not specifically pose a challenge compared to current model validation practices.

### 4.3 Explainability


[pp. 10-11]

- 30.Another challenge for financial institutions relates to the explainability and interpretability of the results of ML models. A higher level of complexity may lead to better model performance but at the cost of lower explainability and comprehension of the model’s functioning. The feedback from the consultation showed that a key challenge for banks was to find the right balance between improving model performance versus creating additional complexity and decrease interpretability. As discussed in the previous section, this creates some additional needs in terms of skills, such as hiring of new experts that can further ensure good knowledge

of the models, alongside with increasing the interaction among stakeholders. A key element mentioned was also ensuring a proper documentation of the model.

- 31.Financial institutions reported that they generally ensure explainability on the global level, i.e. the general ML model decision-making process, and on the local level, i.e. the specific ML prediction outcomes. Figure 1 shows that the most commonly used interpretability tools are Shapley values (40% of respondents), followed by graphical tools (20%), enhanced reporting and documentation of the model methodology (28%) and sensitivity analysis (8%).

Figure 1: Measures to ensure explainability of ML techniques

_Source: EBA feedback from CP on DP on ML for IRB models, 14 respondents._

- 32.Closely related to explainability is the issue of traceability, e.g. how to identify the root cause for an identified issue. Some respondents report that this issue can be addressed by implementing methodological choices in the design of the model that facilitate traceability such as avoiding excessive retraining of the model. Further, the general methods to mitigate explainability issues, for example sensitivity analysis and the use of interpretability tools, are used/intended to be used to handle traceability issues.

- 33.There are other considerations that go hand in hand with the issue of explainability. One of those issues raised by the industry is the communication and acceptance of ML models within the financial institution. They report, however, that this should not create any additional issues, which are not already addressed by the communication tools currently used for senior management and other stakeholders. They would address the larger complexity by training stakeholders and providing targeted documentation that e.g. includes interpretability tools to explain the results of the model for stakeholders that are less knowledgeable on statistical aspects.

### 4.4 Categorisation of model changes


[p. 12]

- 34.The EBA outlined in its principle-based recommendations of the DP that ML models should be stable and need to remain compliant with the requirements on model changes. The industry feedback was generally in line with this approach, but indicated that further clarifications could be provided.

- 35.The EBA is of the view that:

- a. Any update of the rating system used to calculate own funds requirements needs to be assessed according to the prudential model change framework. In particular, a change in the algorithm used for the assignment of obligors to grades or pools should be considered as a change requiring competent authorities' approval if it falls under one of the situations provided in paragraph (2) Section 1, Part II of Annex I of the Commission Delegated Regulation for assessing the materiality of extensions and changes of the IRB Approach and the AMA.8 In this context, for ML models updated at a high frequency and/or automatically updating models, two requirements are especially relevant:

- point (d), since a significant change in the rank ordering or in the distribution of exposures should be considered as a material model change;

- Article 3(3), as no model change should be split into several changes or extensions of lower materiality;

- b. On the other hand, as long as the rating system used to calculate own fund requirements is not updated, the model change framework does not constrain the use of self-training and self-development model challengers (e.g. for the yearly review of estimate) that incorporate additional data when it becomes available.

8 Commission Delegated Regulation (EU) No 529/2014 of 12 March 2014.

## 5. Interaction with (non-CRR) regulatory frameworks


[p. 13]

- 36.The possible decision of going forward with ML techniques in credit risk models should not be based exclusively on prudential terms, but also on other relevant aspects such as ethical and legal aspects as well as consumer and data protection. Two of the legal frameworks that interact with the use of ML techniques for IRB models are the General Data Protection Regulation (GDPR) also through the directive on consumer credit (Directive 2008/48/EC on credit agreements for consumers), and the Artificial Intelligence (AI) Act.

- 37.There has been limited feedback from financial institutions or supervisors on the current interaction between the GDPR and IRB models using ML techniques. This section, therefore, focuses on possible implication of such interaction that was identified by analysing the relevant legal texts.

### 5.1 Interaction with GDPR


- 38.In June 2021, the European Commission published its proposal for a new directive on consumer credit (CCD),9 which aims to replace Directive 2008/48/EC on credit agreements for consumers and to adapt the current rules to the ongoing digitalisation of the market and other trends. The European Parliament published in August 2022 its response to the Commission’s proposal10 that includes several amendments as well as 11 policy mandates for the EBA.11 On 2 December 2022, the Council and the Parliament announced that they had reached provisional political agreement on the revised text of the proposal, which has been published on the 26 April 2023.12

- 39.The text of the proposed CCD from April 2023 includes reference to the GDPR. It refers to _personal data_ under Article 9 of the GDPR13 when prohibiting the use of specific personal data for creditworthiness assessment14 also in the case where data were received from databases located in other EU Members States15 . The proposed CCD further adds the prohibition to use

> 9 Proposal for a Directive of the European Parliament and of the Council on consumer credit (30.06.2021, European Commission).

> 10 Report on the proposal for a directive of the European Parliament and of the Council on consumer credits.

> 11 Inter alia Article 18(2)(1a): GLs detailing how creditors are to perform the creditworthiness assessment, specifying the type of data recommended to perform the creditworthiness assessment.

> 12 Proposal for a Directive if the European Parliament and of the Council on consumer credits – Provisional agreement resulting from interinstitutional negotiations (AG (europa.eu)).

> 13 Article 9 GDPR: Processing of personal data revealing racial or ethnic origin, political opinions, religious or philosophical beliefs, or trade union membership, and the processing of genetic data, biometric data for the purpose of uniquely identifying a natural person, data concerning health or data concerning a natural person's sex life or sexual orientation shall be prohibited.

> 14 “The assessment of creditworthiness shall be carried out on the basis of relevant and accurate information on the consumer’s income and expenses and other financial and economic circumstances []. That information shall not include special categories of data referred to Article 9(1) of Regulation (EU) 2016/679.” (Article 18 (2) proposal CCD).

> 15 Article 19(3)a) proposed CCD.

[p. 14]

data collected from social networks and refers to the minimisation principle16 of the GDPR in its requirements for the assessment of the consumers’ creditworthiness. Previously, without taking into account the proposed CCD’s data restrictions, the impact of the GDPR on credit institutions has already been raised in the context of the EBA report on Big Data and advanced analytics17 and the EBA Guidelines on loan origination.18 In the EBA report on Big Data and advanced analytics, it is clarified that GDPR requirements need to be respected.

- 40.ML techniques need a large amount of data, which raises the questions if financial institutions will be able to identify the data that are subject to GDPR restrictions. The compliance with GDPR requirements could therefore be more difficult once ML techniques are used and would require additional review by financial institutions and supervisors.

- 41.Some financial institutions are aware that if the dataset used to build the ML model contains unstructured data, it could be more challenging to detect personal data (in the meaning of Article 9 GDPR), and therefore extra time and extra knowledge may be required during the validation and in preparation for the validation in order to ensure that this dataset is compliant with the GDPR.

- 42.Financial institutions acknowledged this potential challenge even though the result of the consultation suggests that there are currently only very few financial institutions that use unstructured data. The limited use is based on current business needs and technical challenges in storing the data as well as interpretability, data quality and representativeness issues. The future use of unstructured data is, however, not excluded and will be subject to putting in place adequate control functions to meet the quality and completeness regulatory requirements on IRB models.

- 43.In relation to the GDPR data retention requirement,19 the majority of financial institutions that responded to the consultation stated that they do not see this requirement as a problem, and especially not as a problem specifically concerning ML techniques. This is mainly based on the respondent’s understanding that personal data collected for capital requirement purposes under the CRR should be interpreted as a valid reason to store the data.

> 16 “adequate, relevant and limited to what is necessary in relation to the purposes for which they are processed (‘data minimisation’)”, Article (5)(1)(c) GDPR.

> 17 EBA report on big data and advanced analytics: When managing personal data a trustworthy BD&AA system needs to comply with the current regulation on data protection (the GDPR). According to the GDPR, institutions should have a lawful basis for processing personal data, an example being the customer’s consent to processing the data for a specific purpose (recital 40 and Article 6(1)(c) GDPR).

[pp. 14-15]

> 18 The Banking Stakeholder Group raised in its opinion to the EBA GL 2020 06 Final report on GL on loan origination and monitoring the point that the GLs should be integrated with the requirements of the GDPR.

> 19 GDPR data retention rules require any personal data that is collected or processed to be kept only for as long as data are required to achieve the purpose for which the information was collected.

- 44.In April 2021, the European Commission published its proposal on the AI Act as part of its AI package.20 It aims to create a safe and innovation-friendly environment for users, developers and deployers of AI and is also key to build an ecosystem of excellence in AI and strengthening the EU’s ability to compete globally. The European Council21 and European Parliament22 adopted their responses to the proposal on 6 December 2022 and 14 June 2023, respectively. The trilogue will follow, aiming to finalise the AI Act by end-2023.

### 5.2 Interaction with AI Act


[p. 15] [ref: 5.2.1]

- 5.2.1 Clarification on the scope of application of the AI Act

- 45.The evaluation of a natural person’s creditworthiness (CWA) and credit scoring performed by institutions have been included in the list of high-risk use cases under the rationale that such a evaluation may affect the access to key financial resources and can thus have a significantly adverse impact on natural persons. The scope of the AI Act is reflected in several parts of the legal framework, such as in the definition of ‘artificial intelligence system’ (AI system), and is targeted to systems, which may pose a risk to the person’s access to financial resources.

- 46.Recital 37 of the Commission’s Proposal for the AI Act (as maintained in the Parliament’s proposal and in the Council general approach)explains the rationale that AI systems for CWA are within the scope of ‘high-risk’ systems because they determine “ _persons’ access to financial resources or essential services such as housing, electricity, and telecommunication services_ ” and therefore, “ _AI systems used for this purpose may lead to discrimination of persons or groups and perpetuate historical patterns of discrimination, for example based on racial or ethnic origins, gender, disabilities, age, sexual orientation, or create new forms of discriminatory impacts”._

- 47.In this context, it is important to note that Article 83(2) of the Commission’s proposal for the AI Act states that the AI Act applies to an AI system already in use prior to the general date of application of the AI Act, if and only if, substantial changes to their design or intended purpose occur after the date of application. Therefore, financial institutions that are already using AI systems will only be subject to the AI Act once their models for credit-scoring/credit worthiness assessments of individual consumers undergo significant changes or their intended purpose changes.

- 48.It is the EBA view that it would be strongly beneficial to clarify that the AI Act includes in its scope of high-risk use cases only systems used for the CWA and credit scoring of natural person at the point of loan origination to grant the credit or related financial services, and it therefore does not _apply directly_ to other areas of the credit process such as IRB models used for capital

> 20 https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A52021PC0206.

[pp. 15-16]

> 21 https://data.consilium.europa.eu/doc/document/ST-14954-2022-INIT/en/pdf. One of the changes introduced in the Council version is the change of the definition of ‘Artificial Intelligence system’. The new definition in Article 3.1. is less broad and therefore excludes simple models. It further restricts the scope by prescribing that the systems need to ‘influenc[e] the environments with which the AI system interacts’. The council proposal further included a further requirement on ‘high-risk’ AI systems. Article 6(3) AI Act now states that the classification of high-risk AI system only applies if ‘the output of the system is [not] purely accessory in respect of the relevant action or decision to be taken’. The Parliament does not propose such amendment.

> 22 https://www.europarl.europa.eu/doceo/document/TA-9-2023-0236_EN.pdf.

requirements calculation. This reasoning is based on the aim and the scope of the AI Act, which is reflected in several parts of the legal framework as, by example, in recital 37 mentioned here above and is targeted to the systems, which may pose a risk to natural persons’ access to financial resources.

- 49.The view that the AI Act does not _apply directly to_ IRB models does not preclude that the impact of the AI act on IRB models may be substantial. Most probably there will be _indirect effects_ on the IRB models via the prudential use-test requirements that could be interpreted as requiring a “one rating – one obligor-principle”. The use-test requirement specifies that financial institutions need to ensure that their internal ratings, default and loss estimates, associated systems and processes play an essential role in the risk management and decision-making process, and in the credit approval of the institution.23 Therefore, the non-direct application of the AI Act does not preclude that some of its requirements applicable on the CWA at loan origination may indirectly transmit to IRB models through the prudential use-test requirement.

#### 5.2.2 Additional requirements from the AI Act


[pp. 16-17]

Mapping of the AI Act requirements with the prudential ones

- 50.It is important to ensure that the introduction of the AI Act does not create legal uncertainty about the requirements that may affect IRB models through the use-test and that those requirements do not introduce inconsistencies with respect to the existing regulatory framework applying to the financial institution’s internal models. In order to address the prudential risks arising from IRB models, the general governance and risk management requirements are established in the CRR/CRD (level 1 legislation) with additional details in level 2 legislation, for example the Commission Delegated Regulation on assessment methodology for the IRB approach,24 which includes detailed provisions in areas such as data quality, model validation, model calibration or documentation and record keeping.

- 51.In some areas, the requirements are similar with the requirements for high-risk AI systems in the AI Act. The EBA worked on a preliminary detailed mapping between the AI Act requirements for high-risk use cases and the requirements applicable to IRB models under CRR/CRD. For the majority of the AI Act requirements that, as described above in principle apply only to AI systems used at the loan origination stage and not to IRB models, this mapping seems to suggest that i) the AI Act deems to be fulfilled if financial institutions comply with financial sector legislation or ii) they are consistent with requirements under the CRR/CRD that apply to IRB models for the purpose of capital requirements calculation. The remaining requirements of the AI Act:

- a. Relate specifically to administrative obligations under the AI Act that may apply to financial institutions if they are providers of high-risk AI systems and are therefore not relevant for

> 23 Article 144(1)(b) of the CRR

> 24 Delegated Regulation 2022/439.

IRB models (e.g. EU declaration of conformity,25 reporting to market surveillance authorities26 ).

- b. Apply to the CWA/credit scoring performed by the financial institution and do not affect the performance of the models but rather relate to procedural obligations of the financial institution (e.g. additional technical documentation held for 10 years,27 development of inhouse instruction28 ). In other words, these are requirements that can be complied with by fine-tuning the IRB models to use them for the purpose of CWA (e.g. expanding documentation) and with no interaction with the functioning of the IRB model.

- c. Apply to CWA/credit scoring performed by the financial institution and may affect the current use of the model and its performance, depending on how they are interpreted (e.g. ensure testing for biases, ensure human oversight with the aim to prevent/minimise risks to fundamental rights29 ).

[pp. 17-18]

Clarification on the interaction between the intended use of the model and the risk to fundamental rights

- 52.The effects of the AI act requirements on CWA/credit scoring models used for the purpose of granting loans to natural persons, as mentioned in point c in the previous paragraph, are however unclear as they depend on the interpretation given to the AI Act text. This is the area where the indirect impact of the AI act on IRB models will likely be the most significant.

- 53.The EBA supports the intention behind the AI act, namely the application of a robust framework ensures that the use of complex modelling techniques does not lead to a breach of fundamental rights, in particular in the form of introducing unlawful discrimination. However, the EBA also acknowledges that what constitutes an undue differentiation in the context of CWA that could be considered as a discrimination, and therefore a risk to fundamental rights, may be subject to different interpretations and may give rise to legal uncertainty that would negatively impact all stakeholders.30 In this context, the EBA supports a similar level of clarity than the one that can be observed on the interaction with other regulations.31

- 54.As a background, in order to provide the appropriate clarification, it is important to keep in mind that financial institution’s ability to assess risk is paramount to prevent harm to consumers as CWA is intended to protect financial institutions and in turns also consumers (ensuring that they can afford the credit) against the risk of over-indebtedness and bankruptcy. As such, failure to

> 25 Article 48 of the AI Act (version 11 May 2023 - EU Parliament compromise amendments)

> 26 Article 22 of the AI Act.

> 27 Article 50 of the AI Act.

> 28 Article 13(2) of the AI Act.

> 29 Article 14(2) of the AI Act.

> 30 From customers, that would not have a clear view of their rights, to banks, who would face uncertainties on their legal obligation, and Competent Authorities, that would find it more difficult to enforce the requirements and with higher risk of a non-harmonised application across EU.

> 31 For instance, on the interaction with GDPR, the Article 9 clearly defines which input variables are deemed problematic in the form of a closed list.

complete an accurate CWA may have negative effects on both banks and borrowers and affect financial stability. In this context, one can note that the prudential framework (CRR/CRD) exactly aims to prevent those effects by ensuring that banks hold capital which is commensurate to the risk to which banks are exposed, but it is not intended to consider specific risks to fundamental rights of people, including risks of unlawful discrimination. Therefore, considerations towards the interest of individuals are important.


---

[previous part](text-001.md) | [source overview](overview.md) | [next part](text-003.md)

[^original]: European Banking Authority, "The EBA publishes follow-up Report on the use of machine learning for internal ratings-based models" (2023-08-28). https://www.eba.europa.eu/publications-and-media/press-releases/eba-publishes-follow-report-use-machine-learning-internal
