---
type: Source Text
title: The EBA publishes follow-up Report on the use of machine learning for internal ratings-based models - part 3 of 3 (pp. 18-24)
description: 'Verbatim extracted text, pp. 18-24: 5. Interaction with (non-CRR) regulatory frameworks > 5.2 Interaction with AI Act; 6. Way forward; Annex I– Principle-based recommendations > Recommendations regarding the regulatory compliant use of ML techniques in the context of the IRB framework'
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
part: 3
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

[previous part](text-002.md) | [source overview](overview.md)

> Verbatim text extracted from the original (European Banking Authority, 2023-08-28), part 3 of 3, pp. 18-24. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **regulatory expectation**.[^original]

## 5. Interaction with (non-CRR) regulatory frameworks


### 5.2 Interaction with AI Act


#### 5.2.2 Additional requirements from the AI Act


[p. 18]

- 55.Therefore, the EBA is of the view that it would be beneficial to clarify that the aim of the AI Act requirements mentioned in paragraph 51, point c, is to ensure that that financial institutions have a framework in place that ensures the AI system used for CWA and credit scoring performs according to their “intended purpose” , i.e. differentiate customers on the basis of their credit risk without creating a statistical bias. Such a clarification could support the EBA interpretation that a risk-based differentiation, based on a well-functioning model that counts on sound governance and risk management measures in compliance with relevant national and Union law, would be justified by the purpose of the model and therefore would not, per se, produce outcomes that breach fundamental rights in the meaning of the AI Act. Article 8(2) of Commission’s proposal for the AI Act, which states that “t _he intended purpose of the high-risk AI system [] shall be taken into account when ensuring compliance with [those] requirements_ ”, seems to support this view.

- 56.As a consequence, considering that the CRR/CRD framework requires IRB models to produce estimates that are plausible and interpretable and perform without any statistical bias, IRB compliant models are expected to produce differentiation between natural persons justified by the purpose of the model (assessing creditworthiness) where they are used for the purpose of CWA/credit scoring. As part of the plausibility requirement in Article 179 CRR,32 however, financial institutions are expected to review cases where non-financial variables are found as statistically significant for the differentiation of risk with the aim of understanding how they translate into the financial world. A possible approach is to investigate how those non-financial variables impact the financial and credit risk of their obligors and whether alternative variables (e.g. financial ones) could be similarly or more discriminant.

32 Art. 179(1)(a) CRR requires that the estimates shall be plausible and intuitive and shall be based on the material drivers of the respective risk parameters.

## 6. Way forward


[p. 19]

- 57.The conclusions from the consultation on the DP on ML for IRB models and the further considerations elaborated in this report, confirm that the DP reflected adequately the current uses of ML techniques for IRB models, their challenges as well as their benefits. The DP was welcomed by the industry and provides clarity on regulatory expectations as regards the use of ML techniques for IRB models. Its principle-based recommendations provided a consistent and clear understanding on how to ensure that the use of ML techniques comply with the regulatory IRB requirements.

- 58.The responses to the consultation suggest that the DP provided financial institutions with more clarity and could support their eventual projects to use ML techniques for IRB models. However, the rapid developments in ML techniques require that competent authorities continuously monitor the implementation of such techniques by financial institutions as well as the developments of other relevant regulatory and legislative projects that might impact their use. The EBA will therefore engage in regular monitoring of the developments in this field and will amend or complement the principle-based recommendations if relevant.

## Annex I– Principle-based recommendations


### Recommendations regarding the regulatory compliant use of ML techniques in the context of the IRB framework


[pp. 20-21]

The EBA has already identified the four pillars for the development, implementation and adoption of Big Data and Advanced Analytics (BD&AA) in its report on BD&AA – namely data management, technological infrastructure, organisation and governance and analytics methodology, which are necessary to support the rollout of advanced analytics, along with a set of trust elements that should be properly and sufficiently addressed (namely, ethics, explainability and interpretability, traceability and auditability, fairness and bias prevention/detection, data protection and quality, and consumer protection aspects and security).

Along these lines, instead of concluding which specific ML model might be accepted for which specific prudential function of IRB modelling, this Annex seeks to discuss a set of recommendations in the form of a principle-based approach to which IRB models should adhere. These principles are intended to make clearer how to adhere to the regulatory requirements set out in the CRR for IRB models.

ML models might add value, provided they ensure acceptable monitoring, validation and explainability of the methodology and of the model outcomes. A good level of institutional understanding about their IRB models is a key element, and with even more relevance when ML models are used for regulatory purposes.

ML might be used for different purposes and at various levels: data preparation, risk differentiation, risk quantification and internal validation purposes. All of the following recommendations apply where ML models are used for risk differentiation33 and risk quantification purposes, except for explicit divergent indications.

If institutions want to use ML models for regulatory capital purposes, all the relevant stakeholders should have an appropriate level of knowledge of the model’s functioning . In particular, the EBA recommends that institutions ensure that:

- a. The staff working in the model development unit, Credit Risk Control Unit (CRCU) and the validation unit is sufficiently skilled to develop and validate ML models and, therefore, to assess the relevance and appropriateness of the risk drivers used, as well

> 33 The ML model may be the main model used for risk differentiation purposes or may be used in modules or sub-modules that are combined with other modules, potentially estimated with other simpler techniques. The recommendations are valid for both situations and should be applied at a level consistent with the application of the techniques (for instance, if ML is used only for one module in the PD model, the recommendation should be applied for that module).

as the soundness of the underlying economic rationale in the overall model. For these purposes, appropriate actions are taken, such as, for example, on the organisation of technical in-depth training sessions.

[p. 21]

- b. The management body and senior management are in the position to have a good understanding of the model, by providing them with appropriate high-level documentation. That documentation should at least clarify which indicators or variables are the key drivers for the assignment of exposures to grade or pools, as well as – if relevant – how ML models impact the risk quantification.

It is recommended that institutions find an appropriate balance between model performance and explainability of the results. Indeed, a higher level of complexity may lead to better model performances, but at the cost of lower explainability and comprehension of the model’s functioning. Therefore, institutions are recommended to avoid unnecessary complexity in the modelling approach if it is not justified by a significant improvement in the predictive capacities. Institutions are recommended to avoid:

- a. including an excessive number of explanatory drivers or drivers with no significant predictive information;

- b. using unstructured data if more conventional data is available that provides similar predictive capacities; and

- c. overly complex modelling choices if simpler approaches yielding similar results are available.

In addition, to ensuring that the model is correctly interpreted and understood , institutions are recommended to:

- a. Analyse in a statistical manner: i) the relationship of each single risk driver with the output variable, _ceteris paribus;_ ii) the overall weight of each risk driver in determining the output variable, in order to detect which risk drivers influence model prediction the most. These analyses are particularly relevant where a close and punctual representation of the relationship between model output and input variables is not determinable due to the complexity of the model.

- b. Assess the economic relationship of each risk driver with the output variable to ensure that the model estimates are plausible and intuitive.

- c. Provide a summary document in which the model is explained in an easy manner based on the outcomes of the analyses described in point a. The document is recommended to describe:

- i. The key drivers of the model.

- ii. The main relationships between the risk drivers and the model predictions. The addressees of the document are all the relevant stakeholders, including the staff which uses the model for internal purposes.

- d. Ensure that potential biases in the model (e.g. overfitting to the training sample) are detected.

[p. 22]

Where ML techniques are used, a good level of understanding of the model is required, especially where human judgment is applied, even though the exact concerns can be different depending on where human judgment is applied. In particular, when human judgment is used in the development of the model, staff in charge is recommended to be in the position to assess the modelling assumptions and whether the selected risk drivers contribute to the risk assessment in line with their economic meaning. If human judgment is used in the application, on the other hand, staff in charge of performing overrides is recommended to to be able to consider the behaviour of the model on a specific prediction, taking into account aspects which are not already embedded in it, or identify the cases where the model’s logic could be misleading. Finally, institutions are recommended to grant the performance of the override process of the automated model outputs, considering only those aspects which are insufficiently embedded in the automatic rating.

Where ML models are frequently updated, the reason for such regular updates are recommended to be analysed in detail and monitored by the institution. Generally, a break in the economic conditions or in the institutions’ processes or in the underlying data might justify a model update. As credit risk is, however, not supposed to change frequently (in contrast to e.g. the market risk), such updates are expected, in general, not to occur frequently. Therefore, the parameters of the model should generally be stable. In addition, any update of the rating system used to calculate own fund requirement needs to be assessed according to the model change framework.34 In particular, a change in the algorithm used for the assignment of obligors to grades or pools should be considered as a change requiring competent authorities' approval, as per paragraph (2) Section 1, Part II of Annex I of the CDR for assessing the materiality of extensions and changes of the IRB approach and the AMAIn this context, for ML models updated at a high frequency and/or automatically updating models, two requirements are especially relevant:

- point (d) of paragraph (2) Section 1, Part II of Annex I, since a significant change in the rank ordering or in the distribution of exposures should be considered as a material model change;

- Article 3(3), as no model change should be split into several changes or extensions of lower materiality.

For complex ML models with limited explainability or for frequently updated models, a reliable validation is particularly important and might require increased depth and/or frequency. The institutions are recommended to take care of:

- i. Overfitting issues: ML models are very prone to suffer from overfitting, i.e. performance optimisation of the development sample, which leads to very high performance of the development sample that may not be confirmed on the current and foreseeable application portfolio. Therefore, the institution is recommended to put particular attention on the

[pp. 22-24]

34 CDR for assessing the materiality of extensions and changes of the IRB Approach and the AMA.

comparison of the model performances measured within the development sample with those obtained using out-of-sample and out-of-time data sample.

- ii. Challenging the model design: the hyperparameters used to describe the structure of the model and to customise the learning algorithm are often based on human judgment. Therefore, the validation unit is recommended to place particular attention on verifying the rationale behind the choice of these hyperparameters. This check may prove to be particularly challenging for complex models considering that a deep knowledge of the methodology is required to understand all implications of hyperparameters. If, on the contrary, hyperparameters are selected by minimising the error of the model, it is expected that this process does not introduce an undesired bias.

- iii. Representativeness and data quality issues: If ML techniques used for risk differentiation and risk quantification purposes are fed with a large amount of data, sufficient data quality needs to be ensured. Where these data are external data, institutions are recommended to place particular care on the assessment of the representativeness of the external data with respect to the application portfolio. In particular, institutions are recommended to verify whether a diminished representativeness leads to a reduction in the performance of the model measured strictly on the internal customers. Institutions are also recommended to be particularly careful when using unstructured data in ensuring accuracy, completeness and appropriateness of the data.

- iv. Analysis of the stability of the estimates, also in light of the institution’s rating philosophy. It is recommended to analyse the stability both:

- In the assignment process of each debtor/exposure to grades or pools. Indeed, ML algorithms may introduce point-in-time (PiT) elements in the models that may hamper the stability of the rating assignment process compared to more through-the-cycle (TtC) models leading to potential rapid changes in capital requirements;

- Of the relationship between the output variable and the drivers in subsequent releases of the model based on ML techniques especially in light of the model change policy, to provide an assessment of whether changes between inputs and outputs require regulatory approval, _ex ante_ or _ex post_ notification.

Where ML techniques are used for data preparation purposes, institutions are recommended to ensure that there are clear rules and documentation. Institutions are expected to ensure the appropriateness of the methodology applied to data by means of the application of a proper set of checks and controls.

##### EUROPEAN BANKING AUTHORITY

Tour Europlaza, 20 avenue André Prothin CS 30154 92927 Paris La Défense CEDEX, FRANCE

Tel. +33 1 86 52 70 00

E-mail: info@eba.europa.eu

https://eba.europa.eu


---

[previous part](text-002.md) | [source overview](overview.md)

[^original]: European Banking Authority, "The EBA publishes follow-up Report on the use of machine learning for internal ratings-based models" (2023-08-28). https://www.eba.europa.eu/publications-and-media/press-releases/eba-publishes-follow-report-use-machine-learning-internal
