---
type: Source Text
title: Financial Risk Management and Explainable, Trustworthy, Responsible AI - part 3 of 3 (pp. 12-14)
description: 'Verbatim extracted text, pp. 12-14: Financial Risk Management and Explainable, Trustworthy, Responsible AI > A EUROPEAN USE CASE FOR EXPLAINABLE AI IN CREDIT RISK MANAGEMENT; Financial Risk Management and Explainable, Trustworthy, Responsible AI > CONCLUSION; Financial Risk Management and Explainable, Trustworthy, Responsible AI > DATA AVAILABILITY STATEMENT; and 2 more sections'
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
part: 3
parts_total: 3
content_mode: full_text
generated:
  by: process:fincrime-kb-build
  at: '2026-11-21T13:42:33Z'
verified:
- by: process:kb-validate/verbatim-coverage
  at: '2026-11-21T13:42:33Z'
sources:
- id: original
  resource: https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2022.779799/full
  title: Financial Risk Management and Explainable, Trustworthy, Responsible AI
  author: org:academic_publisher
  last_modified: '2022-02-28T00:00:00Z'
---

# Financial Risk Management and Explainable, Trustworthy, Responsible AI

[previous part](text-002.md) | [source overview](overview.md)

> Verbatim text extracted from the original (Academic publisher / repository, 2022-02-28), part 3 of 3, pp. 12-14. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **academic finding**.[^original]

## Financial Risk Management and Explainable, Trustworthy, Responsible AI


### A EUROPEAN USE CASE FOR EXPLAINABLE AI IN CREDIT RISK MANAGEMENT


[p. 12]

To ensure traceability, a mechanism of documentation to the best possible standard should be incorporated. Be it, for example, the documentation of data sets, data labeling, or the decisions made by the AI system. The SHAP approach allows its user to trace back and document the variable contributions to decision making. The clustering of SHAP information is one of the new pieces of information added by the approach, so this can be used to enrich the traceability and documentation. Also, the steps to improve the model based on the new information could be documented.

According to the Guidelines of the HLEG, explainability concerns the ability to explain both the technical processes of an AI system and the related human decisions. The explanation must be understandable to all users (to a certain extend).

If this is the task, then what should the term explainability mean? Every human being will favor their own interpretation when a model is “fully explained” in their respective view. Irrespective of this fact, we enumerate a few partly provocative and incomplete definitions of the term. A model could be called “explained” when a majority of the audience of the attempt to explain (potentially represented by a committee) would agree that:

- Further information would not decrease their urge to ask “why” any more

- They feel sufficiently enabled to explain the AI-made decisions to independent third parties

- The documentation/visualization makes its functioning clear or easy to understand.

- XAI “proves the work,” i.e., the explanation enhances their trust in the respective AI so as to accelerate adoption.

- The result ensures compliance with expanding regulatory and public expectations and

- Fosters trust.

It is true that the SHAP approach delivers an explanation of the global and local decision making of a black box machine learning model, so it explains the AI model on all levels. However, our extension facilitates further analysis of the explanations, for example in context with other local decision mechanisms and data points. Thus, a richer set of information about the decision-making mechanism is given. This could lead to a situation where a human narrative arises and a “story that is plausible” can be delivered. In this way, the machine decision making is connected to human decision making. However, as mentioned before, it is not an explanation in terms of a “causal why.”

Even as it becomes clear from the audience-dependent concept we propose for the word “explainability,” an important

aspect of explainability is the clarification of the audience. The audience of a model explanation is manifold:

- Model builders

- Model checkers

- Compliance and governance officers

- Risk managers

- Product owners

- Senior managers

- Supervisors

- Clients/customers

[pp. 12-13]

The SHAP (cluster) information can be understood by the data scientists or model developers and model validators. Most other relevant people in a bank or fintech company would (we claim) understand it with sufficient training. The same should apply to internal and external auditors and supervisors. For customers/and clients it may be sufficient to mention which variables are most important (the client should probably be informed about the reason for a decision/rejection) or what a client could do to improve certain variables to get a positive decision. The SHAP information delivers a consistent and accurate view and language to describe an AI model. However, it cannot be mentioned often enough that it is also only just a model and that correlation is not causation.

The presented approach can also be used to enhance the Z-Inspection⃝R15 process to assess trustworthy AI, especially in the conceptual cluster of transparency/explainability/intelligibility/interpretability16 . The Z-Inspection⃝R process has the potential to play a key role in the context of the new EU Artificial Intelligence (AI) regulation. Our approach draws attention to the problem of a black box AI, which does not in itself provide an immediate possibility to identify the input and decision-making criteria of such systems. In such situations, it is often difficult to know

- (i) how reliable the inferred relationship between input and output is and

- (ii) which causality exists between them. This is called the explanatory gap of AI.

It is understandable to the authors why banking supervisors would oppose the use of such unexplained black box AI models in the financial sector, at least in areas of application where they themselves are responsible for monitoring and challenging the regulatory compliance of such models. They must assume that an unexplained AI model is not only unexplained to them, but that also the developers of the model and its users lack understanding of the model’s driving forces and rationales. However, this should not lead to a general rejection of the use of AI models. In our view, supervisors will have to further adjust their approaches and potentially further transform their skills to also escort the introduction of AI/ML in banking, including the demand for appropriate XAI setups where necessary. On the

> 15http://z-inspection.org/.

> 16See Zicari et al. (2021).

other hand, banks and other financial institutions will need to expect that supervisors will demand sound explanations of what their AI/ML systems actually do, and what their business purpose is. Approaches like the SHAP clustering are a contribution to both: banks and supervisors.

### CONCLUSION


[p. 13]

Based on the discussions at the Round Table AI at FIRM (Frankfurt Institute for Risk Management and Regulation), the activities in the Gaia-x project FAIC as well as the work around building the “European Use Case for Explainable AI in Credit Risk Management” we have identified seven conclusions and takeaways that express our persepctive on “Financial Risk Management and Explainable, Trustworthy, Responsible AI”:

1. There need to be general principles, requirements, and tests to control model risk and fitness-for-purpose for each model. Particularly because AI is not a fixed category, we are talking about a spectrum of mathematical models of varying complexity, of which gradually increasingly complex ones are becoming feasible. The mentioned governance elements (principles, requirements, tests to control model risk etc.) should focus on models’ respective purposes, influence on human lives, and business impact, rather than model design or complexity. To satisfy these requirements of course, special tests will be necessary for more complex or even dynamic models. This holds true especially for the implementation of those models and their utilization in a scaling enterprise production environment.

2. To this end, it will be necessary and useful to combine the expertise and approaches of classical risk management and governance with those of data science and AI knowledge.

3. Many aspects of AI governance, algorithmic auditing, and risk management of AI systems can be addressed with technology and computing platforms.

4. In fact, an entire industry is about to emerge in this area. Many of the necessary techniques essentially consist of the use of somewhat less complex and more transparent models in their own right, with associated cost for maintenance and operation, and with inherent (more indirect and smaller) risks to operate them. Hence, there will always be residual risk and consequentially a need for human oversight. The level of residual risk should be covered via OpRisk Management (IT risk, mal-decisioning risk, reputational risk) and by AI incident management or AI model insurance.

5. Explainability, interpretability, and transparency of models, data, and decision making will be key to even enable an appropriate possibility to manage remaining model risks (“Explaining Explainable AI”). All three need to be directed toward the internal stakeholders of financial institutions, but—depending on model purpose—also toward

- the outside world, particularly to clients/consumers and supervisors. Each stakeholder needs to be informed about the model aspects in a different and specific way. There are technologies and experts to support interfacing the different domains involved.

6. One aspect of the “Explainable AI” agenda is to enable the fairness of AI decision making or decision support from a societal perspective (linked to the ESG agenda). The associated fairness considerations, starting from the need to explicitly define a notion of fairness and enable its implementation and ongoing validation, are by no means exclusive to AI modeling techniques. They pertain to classical decision making to the same extent; however, due to their lack of innate transparency, the cost of fairness will be higher for AI models. This should be taken into account in the business decisions around the choice of model design.

7. We propose that the final decision about which model should be used, which one needs to be reviewed, and which models should be discontinued, should always be made by a human being. This ensures that the responsibility resides with the respective human decision maker, but is also an important control for drift in self-learning models.

### DATA AVAILABILITY STATEMENT


The original contributions presented in the study are included in the article/supplementary materials, further inquiries can be directed to the corresponding author/s.

All authors listed have made a substantial, direct, and intellectual contribution to the work and approved it for publication.

This work relies on the support from the European Union’s Horizon 2020 research and innovation program FIN-TECH: A Financial supervision and Technology compliance training programme under the grant agreement No. 825215 (Topic: ICT35-2018, Type of action: CSA).

We are grateful to in-depth discussions and input from:

- Yogesh Mudgal from AIRS

### ACKNOWLEDGMENTS


[pp. 13-14]

- Sri Krishnamurthy, QuantUniversity

- Wolfram Peters, CRO Credit Suisse Asset Management

- Christian Duve, V29 Legal

- Patrick Hall, bnh.ai

- Oliver Maspfuhl, Commerzbank.

- AIRS (Artificial Intelligence/Machine Learning Risk and Security Working Group) (2020). Artificial Intelligence Risk and Governance. Retrieved from: https://ai. wharton.upenn.edu/artificial-intelligence-risk-governance/

- Batarseh, F. A., Freeman, L., and Huang, C. H. (2021). A survey on artificial intelligence assurance. J. Big Data 8:60. doi: 10.1186/s40537-021-00445-7

### REFERENCES


[p. 14]

- Bracke, P., Datta, A., Jung, C., and Sen, S. (2019). Machine Learning Explainability in Finance: an Application to Default Risk Analysis. Bank England staff working paper no. 816. doi: 10.2139/ssrn.3435104

- Bruno, G., Hiren, J., Rafael, S., and Bruno, T. (2020). Computing Platforms for Big Data Analytics and Artificial Intelligence. IFC Reports 11. Bank for International Settlements. Retrieved from: https://ideas.repec.org/p/bis/bisifr/ 11.html

- Bussmann, N., Giudici, P., Marinelli, D., Papenbrock, J. (2020). Explainable machine learning in credit risk management. Comput. Econ. 57, 203–216. doi: 10.1007/s10614-020-10042-0

- Deutsche Bundesbank (2020). Policy Discussion Paper The Use of Artificial Intelligence and Machine Learning in the Financial Sector. Retrieved from: https://www.bundesbank.de/resource/blob/598256/d7d26167bceb18ee7 c0c296902e42162/mL/2020-11-policy-dp-aiml-data.pdf

- Gill, N., Hall, P., Montgomery, K., and Schmidt, N. (2020). A responsible machine learning workflow with focus on interpretable models, post-hoc explanation, and discrimination testing. Infm. 1, 137. doi: 10.3390/info11030137

- Hall, P., Cox, B., Dickerson, S., Ravi Kannan, A., Kulkarni, R., and Schmidt, N. (2021). A United States fair lending perspective on machine learning. Front. Artif. Intell. 4:78. doi: 10.3389/frai.2021.695301

- Hutchinson, B., and Mitchell, M. (2019). “50 years of test (un) fairness: lessons for machine learning,” in Proceedings of the Conference on Fairness, Accountability, and Transparency (New Orleans, LA), 49–58. doi: 10.1145/3287560.3287600

- Independent High-Level Expert Group on Artificial Intelligence (2019). Ethics Guidelines for Trustworthy AI. Brussels: European Commission. Retrieved from: https://ec.europa.eu/newsroom/dae/document.cfm?doc_id=60419

- Jaeger, M., Krügel, S., Marinelli, D., Papenbrock, J., Schwendner, P. (2021). Interpretable machine learning for diversified portfolio construction. J. Financ. Data Sci. doi: 10.3905/jfds.2021.1.066

- Liu, H., Wang, Y., Fan, W., Liu, X., Li, Y., Jain, S., et al. (2021). Trustworthy AI: A Computational Perspective. Cornel University. Available online at: https://arxiv. org/abs/2107.06641

- Loftus, J. R., Russell, C., Kusner, M. J., and Silva, R. (2018). Causal reasoning for algorithmic fairness. arXiv [Preprint].arXiv:180 5.05859.

- Papenbrock, J., Schwendner, P., Jaeger, M., Krügel, S. (2021). Matrix evolutions: synthetic correlations and explainable machine learning for constructing robust investment portfolios. The J. Financ. Data Sci. doi: 10.3905/jfds.2021.1.056

- Tiwald, P., Ebert, A., Soukup, D. (2021). Representative and Fair Synthetic Data. Retrieved from: https://arxiv.org/abs/2104.03007

- Zhang, J., and Bareinboim, E. (2018). “Fairness in decision-making-the causal explanation formula,” in Thirty-Second AAAI Conference on Artificial Intelligence (New Orleans, LA). Available online at: https://ojs. aaai.org/index.php/AAAI/article/view/11564 (accessed April 25, 2018).

- Zicari, R. V., Brodersen, J., Brusseau, J., Düdder, B., Eichhorn, T., Ivanov, T. (2021). Z-Inspection⃝R : a process to assess trustworthy AI. IEEE Trans. Technol. Soc. 2, 83–97. doi: 10.1109/TTS.2021.3066209

Conflict of Interest: SF-M was employed by Bain & Company. BH was employed by Ernst & Young. JP was employed by NVIDIA GmbH.

Publisher’s Note: All claims expressed in this article are solely those of the authors and do not necessarily represent those of their affiliated organizations, or those of the publisher, the editors and the reviewers. Any product that may be evaluated in this article, or claim that may be made by its manufacturer, is not guaranteed or endorsed by the publisher.

Copyright © 2022 Fritz-Morgenthal, Hein and Papenbrock. This is an open-access article distributed under the terms of the Creative Commons Attribution License (CC BY). The use, distribution or reproduction in other forums is permitted, provided the original author(s) and the copyright owner(s) are credited and that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction is permitted which does not comply with these terms.


---

[previous part](text-002.md) | [source overview](overview.md)

[^original]: Sebastian G. Fritz-Morgenthal, Bernhard Hein, Jochen Papenbrock, "Financial Risk Management and Explainable, Trustworthy, Responsible AI" (2022-02-28). https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2022.779799/full
