---
type: Source Text
title: Financial Risk Management and Explainable, Trustworthy, Responsible AI - part 1 of 3 (pp. 1-6)
description: 'Verbatim extracted text, pp. 1-6: Financial Risk Management and Explainable, Trustworthy, Responsible AI; Financial Risk Management and Explainable, Trustworthy, Responsible AI > INTRODUCTION; Financial Risk Management and Explainable, Trustworthy, Responsible AI > RISK MANAGEMENT AND AI; and 6 more sections'
resource: https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2022.779799/full
tags:
- academic_finding
- academic_paper
- global_academic
- ml_statistics
- model_development
status: stable
source_id: academic-publisher-financial-risk-management-and-explainable-trustwort
issuer: academic_publisher
issuer_name: Academic publisher / repository
jurisdictions:
- GLOBAL_ACADEMIC
tier: 3
instrument_type: academic_paper
normative_force: academic_finding
publication_date: '2022-02-28'
legal_status: unknown
part: 1
parts_total: 3
content_mode: full_text
generated:
  by: process:fincrime-kb-build
  at: '2026-11-21T03:48:52Z'
verified:
- by: process:kb-validate/verbatim-coverage
  at: '2026-11-21T03:48:52Z'
sources:
- id: original
  resource: https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2022.779799/full
  title: Financial Risk Management and Explainable, Trustworthy, Responsible AI
  author: org:academic_publisher
  last_modified: '2022-02-28T00:00:00Z'
---

# Financial Risk Management and Explainable, Trustworthy, Responsible AI

[source overview](overview.md) | [next part](text-002.md)

> Verbatim text extracted from the original (Academic publisher / repository, 2022-02-28), part 1 of 3, pp. 1-6. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **academic finding**.[^original]

[p. 1]

PERSPECTIVE published: 28 February 2022 doi: 10.3389/frai.2022.779799

Sebastian Fritz-Morgenthal1 , Bernhard Hein2 and Jochen Papenbrock3 *

1 Bain & Company, Frankfurt, Germany, 2 Ernst & Young, Munich, Germany, 3 NVIDIA GmbH, Würselen, Germany

Edited by: Dror Y. Kenett, Johns Hopkins University, United States

Reviewed by: Hayette Gatfaoui, IESEG School of Management, France Ehi Eric Esoimeme, E-Four and AAF, Nigeria

## Financial Risk Management and Explainable, Trustworthy, Responsible AI


*Correspondence: Jochen Papenbrock jp@firamis.de

Specialty section: This article was submitted to Artificial Intelligence in Finance, a section of the journal Frontiers in Artificial Intelligence

Received: 19 September 2021 Accepted: 11 January 2022 Published: 28 February 2022

This perspective paper is based on several sessions by the members of the Round Table AI at FIRM1 , with input from a number of external and international speakers. Its particular focus lies on the management of the model risk of productive models in banks and other financial institutions. The models in view range from simple rules-based approaches to Artificial Intelligence (AI) or Machine learning (ML) models with a high level of sophistication. The typical applications of those models are related to predictions and decision making around the value chain of credit risk (including accounting side under IFRS9 or related national GAAP approaches), insurance risk or other financial risk types. We expect more models of higher complexity in the space of anti-money laundering, fraud detection and transaction monitoring as well as a rise of AI/ML models as alternatives to current methods in solving some of the more intricate stochastic differential equations needed for the pricing and/or valuation of derivatives. The same type of model is also successful in areas unrelated to risk management, such as sales optimization, customer lifetime value considerations, robo-advisory, and other fields of applications. The paper refers to recent related publications from central banks, financial supervisors and regulators as well as other relevant sources and working groups. It aims to give practical advice for establishing a risk-based governance and testing framework for the mentioned model types and discusses the use of recent technologies, approaches, and platforms to support the establishment of responsible, trustworthy, explainable, auditable, and manageable AI/ML in production. In view of the recent EU publication on AI, also referred to as the EU Artificial Intelligence Act (AIA), we also see a certain added value for this paper as an instigator of further thinking outside of the financial services sector, in particular where “High Risk” models according to the mentioned EU consultation are concerned.

Keywords: risk management, EU AI act, artificial intelligence, machine learning, financial regulation and compliance, explainable AI, trustworthy AI

Citation:

Fritz-Morgenthal S, Hein B and Papenbrock J (2022) Financial Risk Management and Explainable, Trustworthy, Responsible AI. Front. Artif. Intell. 5:779799. doi: 10.3389/frai.2022.779799

> 1The Association for Risk Management and Regulation (Gesellschaft für Risikomanagement und Regulierung e.V.), in which banks and associations, initiatives, audit firms, the Federal Financial Supervisory Authority (Bundesanstalt für Finanzdienstleistungsaufsicht, BaFin) and the State of Hessen are involved, was founded in June 2009. The purpose of the Association is to conduct and promote teaching and research in the fields of risk management and regulation, particularly within the framework of the financial industry, primarily through the Frankfurt Institute for Risk Management and Regulation (FIRM).

### INTRODUCTION


[p. 2]

The European Commission is proposing one of the first laws globally to regulate the use of artificial intelligence. AIA is a cross-sectoral regulation of AI, which addresses particularly governance requirements around so-called high-risk AI systems, and which more generally recommends the adoption of principles in the spirit of creating trustworthy AI. Interestingly, credit scoring models are explicitly given as an example of a high-risk use case.

Pursuant to the requirements of the AIA and existing supervisory expectations, those pursuing an AI-first bank/strategy must be equipped with suitable risk management as well as suitable infrastructure and technology (RiskTech, TrustTech, Algo Audit, Regulatory Sandbox).

In this context, the considerations of fairness and explainability should in principle be applied to all types of models, not just AI, but they are amplified for AI because of their higher complexity and a certain level of in-transparency of more complex algorithms. In this respect, we propose that the requirements for explainability and fairness should, as a leading principle, depend on the application purpose of a model rather than on the choice of its model design. A model for automating credit decisions, for example, the results of which affect human lives and are publicly visible, should ideally be free of unwanted bias and meet requirements for model transparency even if it is a classical model. In some legislations, credit customers even have the explicit right to request an explanation of the reasons behind credit decisions pertaining to themselves, even though the depth of the explanation may depend on whether the actual decision was to the positive or to the negative.

This article focuses on the financial sector because this sector has been in a pioneering position regarding regulation that covers the mentioned topics of explainability and fairness. However, the recent EU proposal for an AIA identifies further use cases and industry sectors in which a certain need for compliance with similar requirements is to be expected for the future. In this respect, we believe that the experience from the financial services sector should be profoundly valuable also for other industries sooner rather than later.

This paper is structured as follows:

In section Risk Management and AI, we provide a high-level description of use cases, based on actually existing AI technology within risk management functions of financial institutions and describe how we expect financial services regulators to approach these models. This view is the result of our discussion at the FIRM Working Group and also takes into account a Policy Discussion Paper of Deutsche Bundesbank (Deutsche Bundesbank, 2020).

In section Fairness and Bias, we describe the challenge of potential model bias, and why it is important to work toward fair decision-making algorithms, as stated by the Ethics Guidelines for Trustworthy AI (Independent High-Level Expert Group on Artificial Intelligence, 2019). We start with a definition of bias, explain the principle of fairness, and provide a procedure to test against or validate the potential (un-)fairness of a decisionmaking algorithm.

In our view, fairness is a pre-condition to develop and run algorithms the decisions of which can be trusted. As a

consequence, in section Addressing Trustworthy AI With Technology, we describe how we believe the Trustworthiness of AI models can be assessed. This includes privacy-preserving methods as well as technologies for explainability and transparency. Further, we offer an approach as to how Trustworthy AI can be optimized within a set of multiple objectives. We conclude the section with references to further reading.

In section A European Use Case for Explainable AI in Credit Risk Management, we discuss a specific model in the credit risk management of a major European insurance group, as a tangible use case of explainable AI. Transparency and explainability were prioritized during the build of this model, and both were achieved using SHAP (Shapley Additive exPlanations, as described in section Addressing Trustworthy AI With Technology and references therein).

We conclude with seven key takeaways in section Conclusion.

### RISK MANAGEMENT AND AI


[pp. 2-3]

Our focus in this article is on Financial Services (i.e., regulated entities, but not necessarily fully regulated areas of application), models used in (or close to) regulatory pillar 1 and pillar 2 risk measurement and prediction for risk or economic capital allocation, accounting, compliance (Anti Money Laundering, Fraud Detection, Transaction Monitoring), client classification/credit decisioning, collections optimization, early warning systems, etc. Of course, the generic outcomes of this paper will just as well apply to models that are more remote from risk management, such as robo advisors, customer lifetime value related recommender models, client coverage etc., to the extent that a financial services entity sees value in them.

We assume that models would need to be ready to undergo regular supervisory or statutory or internal auditor review, and in certain instances of pillar 1 modeling even need to receive supervisory approval. In the absence of more complete and detailed guidance for model risk and model governance of other model types, the requirements for pillar 1 approved internal models have frequently received the largest amount of attention when it came to developing model governance frameworks in the past. Benchmarking results across the market indicate that this realm is therefore the one with the most mature status quo, shaped by long standing and continuously developing supervisory scrutiny, and at the same time by the need to streamline to a business practice that seems viable under profitability considerations.

Our starting point is therefore to apply a typical regulatory model approval process as a blueprint. We focus on model approval because from the perspective of what we are interested in, both development, initial and (guidelines for) periodic validation, and the associated model change processes are assessed during model approval. We also want to address which additional requirements (over and above standard models) AI/ML models would most likely need to fulfill for regulatory approval.

Given the considerations around the model change processes of regulated pillar 1 models we will explore static models first.

After that, the generalization to self-learning/self-modifying models could happen theoretically through an iterative application of the above-mentioned model approval process, under certain additional efficiency requirements. Given efficiency constraints, the entailing effort will effectively limit the frequency in which such model changes can be afforded, unless the materiality of the model changes can be monitored in some way and a layered process can be introduced that limits effort for immaterial changes.

The classification and measurement of this materiality of model changes is also at the core of the regulatory/supervisory model change process, and might allow for a first step toward supervisory acceptance of self-learning models in case, e.g., the self-learning process can be steered to an extent where only immaterial model changes (according to supervisory definition) are suggested, and then carried through under appropriate governance. The authors doubt though, that a self-learning process that effectively produces material model changes would be accepted in the more strictly regulated areas of application in the foreseeable future, particularly in pillar 1 capital models.

[p. 3]

Depending on their application however, the authors hold the view that self-learning models should not generally be discouraged. Particularly:

- Within anti financial crime, anti-money laundering and fraud detection methods, there is tangible competition between fraudsters on the one hand and methods to detect them and prevent their deeds on the other. A targeted introduction of self-learning models in this space could therefore lead to better prevention. Compared to currently (still) wide-spread methods, especially in anti-money laundering (i.e., decision trees and expert based systems), these models have proven their capability to significantly decrease false alarm rates. This might outweigh the need for model stability from other areas of application of models.

- Also, for trading models (including algo trading/robo advice), as well as models to decide about capital and liquidity allocation optimization, the authors believe that self-learning capabilities might be desirable from an overall perspective. However, given that these models are used for economic decision making, portfolio allocation etc., the depth of their explainability to different stakeholder groups will be of greater importance than for the first group of models above.

- More questionable, however, is the use of self-learning models for the calculation of regulatory capital for credit risk, credit decision making, client segmentation and classification, given the much higher transparency requirements for regulation and customer protection laws, as well as the different character and somewhat slower clock speed of classical credit risk.

- Generally, self-learning models are prone toward bias/drift over time. Hence, adequate validation methods and processes need to be applied to manage these issues.

### FAIRNESS AND BIAS


Through a short discussion of the notions of bias and fairness and a high-level look at their interplay, the following section effectively makes a case for the need to keep (or make) models

explainable. Besides potential bias and (un-)fairness, the level of differentiability and continuity as well as potential cliff effects and behavior under extreme parameter settings (stability concerns) of models also need to be well-understood. This adds further weight to a case for model explainability, even though neither of the mentioned aspects will be explored in more detail in this perspective paper.

The Independent High-Level Expert Group on Artificial Intelligence (2019) states that bias is an inclination of prejudice toward or against a person, object, or position. Bias drives the value of many predictive models, such as most risk prediction models (wanted bias) but it can also be detrimental to it. Bias can be good or bad, intentional or unintentional. In certain cases, bias can result in unwanted discriminatory and/or unfair outcomes, labeled in this document as unfair bias.

### Definitions of Bias and Fairness


[pp. 3-4]

Different from the notion of Bias, in all the following discussions, the notions of unfairness and fairness always refer to any chosen, mathematical definition of fairness an institution is applying with respect to a given model, based on ethical and strategic deliberations about the purpose to which the model in view is applied in this institution. Popular notions of fairness include demographic parity (also called statistical parity, e.g., blondes and brunettes have the same chance to get a loan), equalized odds (blondes and brunettes who all meet certain other requirements have the same chance to get a loan) or the well-calibratedness (among those who got a loan, blondes, and brunettes are equally represented as in any random sample). A more in-depth description can for example be found in Loftus et al. (2018), Zhang and Bareinboim (2018), and Hutchinson and Mitchell (2019).

Bias can arise in many ways in any statistical model. However, it may require more targeted efforts to be detected in AI systems. We see that at least the following distinct root causes for bias typically appear:

- Bias inherent in training data (e.g., certain populations underrepresented or certain populations with different coincidence structures to the model’s target variable, data being “polluted” with erroneous entries, outliers, noise, or training data are sourced from past human decision-making which contained bias).

- Algorithmic bias (caused by characteristics of the methodology).

For example, in any data-driven statistical model, particularly an AI system such as one produced through machine learning, bias in data collection and training can result in this model or AI system demonstrating bias. In logic-based AI, such as a rule-based system, bias can be caused by the way in which a knowledge engineer might have viewed the rules that apply in a particular setting, and subsequently codified this view in a model. Any specific bias can also arise in a formerly bias-free model due to self-learning and adaptation through interaction. It can arise through personalization, whereby users are presented with recommendations or information feeds that are tailored to the tastes of other users form a seemingly comparable group, because this bias was present in the tastes of that comparison group.

It does not necessarily relate to human bias or human-driven data collection. It can evolve, for example, through the limited contexts in which a system is used, in which case there is no opportunity to generalize it to other contexts. For a United States Fair Lending Perspective on Machine Learning (see Hall et al., 2021).

### The Principle of Fairness


[p. 4]

During their development, deployment and use, AI systems which impact human lives should be fair in the sense that their output obeys a chosen, reasonable definition of fairness. Next to ethical deliberations, this will help to minimize reputational risk from reactions of or on behalf of adversely affected customers, or at least help to defend respective decisions. We acknowledge that there are different mathematical interpretations of fairness, which partly contradict each other and must be defined based on corporate strategy and ethics2 .

This means that in principle, for each model with fairness requirements, a specific definition of fairness needs to be chosen with respect to each explanatory variable or model feature. However, we also observe that any concept of fairness entails both a substantive and a procedural dimension upon implementation. For the present paper, we will retreat to discussing these overarching aspects that are invariant under changes of the fairness definition. For this reason, it is enough to speak about “fairness” as though it was a clearly defined notion for the rest of this paper. The substantive dimension of fairness (i.e., independently of any chosen particular definition of fairness) implies a commitment to:

1. ensuring a fair (in some sense “equal and just”) distribution of both benefits and costs,

2. ensuring that the effect a model has on individuals and groups is free from unfair bias, discrimination, and stigmatization.

The procedural dimension of fairness entails the ability to contest and seek effective redress against decisions made by AI systems and by the human beings who operate them. To do so, the decision in question must have an accountable owner, this owner must be identifiable (effectively a human or a committee of humans in the relevant governance roles for the model in question), and the decision-making processes needs to be explicable.

Fairness and bias interplay in an important way where bias in the model becomes ethically disputable for at least one group of stakeholders to a given model. This could be the case for any one of the above-mentioned root causes of bias. A typical example would be the question of whether different health insurance premiums for men and women can be or should be derived from potentially measurable differences in actual cost causation in historical data. Similarly, suppose the training data for a credit pricing model say that kebab stands have historically failed significantly more often or less often than Currywurst stands; is a model that therefore provides correspondingly different interest rate conditions for the two discriminatory? A different societal fact of today is still that men earn more on average than

> 2Ethics embeds the following dimensions: Privacy, Avoidance of Bias, Fairness, Explainability, Transparency, Impact.

women. It is an open question how this fact could proliferate into loan approval rates or into the risk premium on corresponding interest rates. However, any bank should be aware that this type of gender bias can easily arise in models even though gender itself is not an explanatory variable in the model. Here, each individual bank should clarify which bias is acceptable to it, and which definition of fairness it thinks it can justifiably pursue; it may be that a higher loan rejection rate for women would be statistically justifiable from the training data (and might comply with an equalized odds fairness definition), but a bank still would not want a corresponding model for ethical (or reputational) reasons.

### Technical Validation—Considerations


In our view, a typical full scope model validation including the requirement to test for fairness/unwanted bias fully covers what needs to be known about the models we have in mind. It should be able to uncover all more than immaterial model risk, independently of the question which model type is used. Keep in mind that performing the necessary tests, e.g., around conceptual soundness or around model plausibility, would of course entail a different technical need for validation analyses to be performed, depending on whether the model under review is more or less transparent or complex. For technical validation, we advocate that the following criteria be considered:

- An important first step is the preparation and cleansing of the respective training and test data sets. The focus of this is to identify potentially erroneous data entries, outliers, and noise; and to transform where possible, otherwise eliminate.

- The basic determination of the “model tests” should be derived solely from the problem to be solved and the use of the model results, and not from the properties of the model. Otherwise, there is a danger of overlooking undiscovered weaknesses of a particular methodology. For example, a credit decisioning model, discriminatory power, stability, calibration, explainability to non-expert stakeholders (e.g., credit applicants) and freedom of unwanted bias are relevant tests, and this does not depend on whether the model is a score card or a neural network. For an anti-money laundering alert model, calibration is far less important, while the false positive ratio frequently replaces a more general look at discriminatory power, etc.

- Areas that are more difficult to be tested (for example, historically unprecedented capital market scenarios) should be identified and considered when applying the model. In credit risk models, this corresponds to a (well-governed) override/overruling process, in accounting models this could be management overlays/top-level adjustments as we have frequently seen them through the current COVID related economic anomalies.

- The intensity with which a specific model is validated further depends on the specific model risk appetite. The amount of residual risk which the model user wants to accept should hence be explicitly stated and aligned with the general risk appetite of an institution.

- For models that support critical decisions (significant impact on individual customers, large monetary impact, etc.) and hence have a higher impact on reputational risk, a plausibility

[p. 5]

check or “explanation” of the results should be performed irrespective of whether they are inherently transparent or not. This explanation should identify the main drivers of the model results and make them understandable. While this basic task is again in our view independent of model type, the technicalities of its conduction are not. For example, in a linear model of scorecard type, the explanation is considerably easier to achieve than in an in-transparent and (likely) highly non-linear model. Achieving this explanation also for the mentioned non-linear and intransparent models is the goal of what we call “explainable AI.” Together with other aspects, Explainability, on the other hand, is an integral part of what we call “trustworthy AI”). Intensity again corresponds to risk appetite. This overall approach corresponds to the usual process of model risk management:

1. Design a risk strategy and risk appetite

2. Derive a model risk strategy and model risk appetite

3. Perform a model risk assessment and categorization of models (e.g., low/medium/high risk)

4. Declare appropriate risk mitigation measures (surcharges, buffers, increase of validation intensity, strengthening of internal controls and governance) or acceptance of risk.

5. Ensure you can comply with legal requirements, e.g., rejected borrowers may have the right to be informed about reasons for rejection, depending on legislation.

- The auditability of the model and its decisions needs to be guaranteed to enable accountability for the model’s results. Again, while this basic requirement holds for all model types, it will lead to more technical work for (e.g.,) selflearning models. Specifically, the full data history, parameters and meta-data of self-learning models must be archived either periodically at a frequency that is informed by the model’s update frequency, or after each meaningful change of the model. In short: If I don’t know what the (selflearning) model looked like yesterday, how can I reproduce yesterday’s results?

The last-mentioned point about self-learning models is of course not the only aspect in which the validation of self-learning models delivers higher technical hurdles to answer the same basic questions as for other models. For example, if model stability is an aspect of model plausibility, then jumps in model parameters should be examined across model changes. If the model keeps updating itself, this will cause higher effort and will have to be done in a more automated way etc.

Generally speaking, a set of basic standard testing and validation procedures should be applied to all models.

However, one must differentiate between various use cases. Additionally, the model specific shape and effort to conduct the corresponding tests will vary depending on model type (e.g., if you know that it is reinforcement learning, then you know the mechanics and weaknesses of the approach). The more complex a model is, the more one must study its behavior and cannot do normal tests anymore. For example, it is quite common to use AI-based synthetic datasets to test the model.

To switch perspectives for once, the following list of technical efforts and base rules will likely have to be used to achieve the

aims and targets of the general, basic tests in the case that more complex AI/ML models are used:

1. Create enhanced incident management: what to do if the AI model is broken

2. Create more capable infrastructure to observe and monitor potential model and/or data drift

3. Be more rigid around stressing the model (with human test data and AI-based synthetic data)

4. Design and implement the infrastructure for the complete historization of models, data, runtime environments

5. Design and carry through multi-criteria choice for the best model according to the Pareto optimum (efficiency line of the best trade-off relations between several, quite competing goals such as accuracy, transparency, fairness, explainability, energy consumption, while being compliant with data privacy and other regulations).

6. Conduct the identification of risks and side effects of integration into existing processes, requirements, and complexities for use, etc.

Figure 1 sketches a simplified flowchart for a model development, application and validation cycle. We have used Credit Scoring as example, but the process steps can also be applied to other types of AI model development.

Indulging in a reverie far beyond the financial services space, the authors believe that the promotion of fairness in AI could even help to increase societal fairness overall. Equal opportunities in terms of access to education, goods, services, and technology could be driven to a next and better level. In line with generally accepted ethical values, the use of AI systems should never lead to people being deceived or unjustifiably impaired in their freedom of choice. Additionally, fairness implies that AI practitioners should respect the principle of proportionality between means and ends and consider carefully how to balance competing interests and objectives.

### ADDRESSING TRUSTWORTHY AI WITH TECHNOLOGY


Successful and ethical AI adoption means harnessing the amazing potential of AI while simultaneously implementing the principles of fair, trustworthy, and explainable AI. Some of these principles can be addressed by scaling digital technologies like computing platforms and then deploying smart models or specific algorithms. An entire industry including the corresponding academic and non-academic research is currently being built around this topic (see for example Liu et al., 2021 and references therein). The following paragraphs provide a list of examples of applications and technologies that should be considered to implement Trustworthy AI.

Some technology is used to ensure that AI systems comply with privacy laws and regulations and meet societal norms for personal data and information privacy.

### Privacy-Preserving Technologies and Methods


[p. 6]

FIGURE 1 | Simplified flowchart for a model development, application and validation cycle.

One technology area is differential privacy and multiparty computation for distributed/federated privacy-preserving machine learning. The term differential privacy is used to describe both the property of an AI system that looking at the output, one cannot tell whether any individual’s data was included in the original dataset or not, and methods to establish this property. Federated learning enables multiple entities who do not trust each other (fully), to collaborate in training a Machine Learning (ML) model on their combined dataset; without actually sharing data.

Another methodological area is the AI-based generation of synthetic data with a wide range of applications, ranging from shortening cycles for quantitative risk modeling, minimizing the effort to comply with regulation, to accelerating development and testing processes. Smaller data sets can be amplified to improve model explainability. Adverse data scenarios can be tested to stress a model.

Synthetic data can also support the collaboration between FinTech companies and incumbent banks: for a closer collaboration, banks need to test the capabilities of thirdparty analytical providers. During this phase, they will not typically want to share their original data, but synthetic ones will provide a way forward.

Generative Adversarial Networks (GANs) are an approach to generative modeling using deep learning methods. Given a training data set, this technique learns to generate new data with the same statistical properties as the original training set. Since many approaches to generating synthetic data require computational power, the industry uses accelerated computing platforms for data generation.

Synthetic data emerges with the promise to provide an unlimited amount of representative, realistic training samples, that can be shared further without disclosing the privacy of

individual subjects. However, in as much as e.g., GANs propagate the statistical properties of their training data, synthetic data must be assumed to be as flawed from a fairness perspective as actual data were and it should be considered unwise to use these data without further care, in the general case. Frameworks are needed to incorporate fairness constraints into the selfsupervised learning process, that allows to then simulate an unlimited amount of representative as well as fair synthetic data. These frameworks will then provide the methods to govern and control privacy as well as bias within AI at its very source: the training data (see Tiwald et al., 2021).


---

[source overview](overview.md) | [next part](text-002.md)

[^original]: Sebastian G. Fritz-Morgenthal, Bernhard Hein, Jochen Papenbrock, "Financial Risk Management and Explainable, Trustworthy, Responsible AI" (2022-02-28). https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2022.779799/full
