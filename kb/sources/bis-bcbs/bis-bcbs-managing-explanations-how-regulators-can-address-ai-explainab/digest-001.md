---
type: Source Digest
title: 'Managing explanations: how regulators can address AI explainability - part 1 of 3 (pp. 1-12)'
description: 'Verified paraphrased digest, pp. 1-12: Abstract; Contents; Managing explanations: how regulators can address AI explainability issues > Section 1 – Introduction; and 2 more sections'
resource: https://www.bis.org/publications/fsi-paper-24-managing-explanations-how-regulators-can-address-ai-explainability
tags:
- explainability
- guidance
- international_standard
- intl
- model_governance
- model_validation
status: stable
source_id: bis-bcbs-managing-explanations-how-regulators-can-address-ai-explainab
issuer: bis_bcbs
issuer_name: Bank for International Settlements / Basel Committee
jurisdictions:
- INTL
tier: 2
instrument_type: guidance
normative_force: international_standard
publication_date: '2025-09-08'
legal_status: current
part: 1
parts_total: 3
content_mode: digest
generated:
  by: claude-code-subagent/claude-sonnet-5-5
  at: '2026-11-21T13:42:23Z'
verified:
- by: process:kb-digest-check/anchor-match
  at: '2026-11-21T13:42:23Z'
- by: claude-code-judge-agent/claude-opus-5-5
  at: '2026-11-21T13:42:23Z'
sources:
- id: original
  resource: https://www.bis.org/publications/fsi-paper-24-managing-explanations-how-regulators-can-address-ai-explainability
  title: 'Managing explanations: how regulators can address AI explainability'
  author: org:bis_bcbs
  last_modified: '2025-09-08T00:00:00Z'
digest_points: 62
---

# Managing explanations: how regulators can address AI explainability (digest)

[source overview](overview.md) | [next part](digest-002.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (pp. 1-12) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **international standard**.

## Abstract

- **descriptive / definition**: The paper defines explainability as the extent to which a model's output can be explained to a human, and says it is essential for transparency, accountability, regulatory compliance and consumer trust. (p. 3)[^original]  
  <sub>anchor: "Explainability, or the extent to which a model’s output can be explained to a human, is essential"</sub>
- **descriptive / limitation**: Complex AI models such as deep learning and LLMs are often difficult to explain; existing explainability techniques have notable limitations including inaccuracy, instability and susceptibility to misleading explanations. (p. 3)[^original]  
  <sub>anchor: "these techniques have notable limitations, including inaccuracy, instability and susceptibility of misleading explanations"</sub>
- **descriptive / finding or result**: Global standard-setting bodies have issued mostly high-level model risk management (MRM) requirements; only a few national authorities have issued specific guidance, tending to focus on models used for regulatory purposes. Many guidelines may not have been developed with advanced AI in mind and do not explicitly mention explainability, which is implicit in provisions on governance, development, documentation, validation, deployment, monitoring and independent review; complex AI models would find compliance challenging and third-party models exacerbate this. (p. 3)[^original]  
  <sub>anchor: "do not explicitly mention the concept of model explainability"</sub>
- **expected / recommendation**: The paper says it is imperative that financial authorities seek to foster sound MRM practices relevant in the context of AI as institutions expand AI use to critical business areas. (p. 3)[^original]  
  <sub>anchor: "it is imperative that financial authorities seek to foster sound MRM practices that are relevant in the context of AI"</sub>
- **descriptive / recommendation**: The paper states there may be a need to recognise trade-offs between explainability and model performance, so long as risks are properly assessed and effectively managed; allowing complex AI models with limited explainability but superior performance could help manage risks and enhance client experiences, provided adequate safeguards are introduced. (p. 3)[^original]  
  <sub>anchor: "there may be a need to recognise trade-offs between explainability and model performance"</sub>
- **permissive / context**: For regulatory capital use cases, the abstract says complex AI models may be limited to particular risk categories and exposures, or made subject to output floors. (p. 3)[^original]  
  <sub>anchor: "complex AI models may be restricted to certain risk categories and exposures or subject to output floors"</sub>
- **mandatory / expectation**: The abstract states that regulators must also invest in upskilling staff to evaluate AI models effectively, so that financial institutions can harness AI's potential without compromising regulatory objectives. (p. 3)[^original]  
  <sub>anchor: "Regulators must also invest in upskilling staff to evaluate AI models effectively"</sub>

## Section 1 – Introduction

- **descriptive / finding or result**: Crisanto et al (2024) and FSB (2024) find that most AI applications in the financial sector are for internal productivity-enhancing purposes; institutions appear cautious about critical business applications, especially customer interactions, but AI use is expected to become more prevalent including in critical areas. (p. 5)[^original]  
  <sub>anchor: "most applications are for internal productivity-enhancing purposes"</sub>
- **descriptive / definition**: There is no commonly agreed definition of explainability: US regulatory agencies (and FSB (2024)) define it as how an AI approach uses inputs to produce outputs; the OECD AI Principles define it, customer-centrically, as enabling people affected by an AI outcome to understand how it was arrived at through easy-to-understand information; IAIS (2025) defines meaningful explanations as understandable, transparent and relevant insights into how an AI system makes decisions or predictions; PRA (2023) describes it as the degree to which a model's workings can be understood in non-technical terms. (p. 5)[^original]  
  <sub>anchor: "US regulatory agencies define explainability as “how an AI approach uses inputs to produce outputs”"</sub>
- **descriptive / finding or result**: FINMA (2024) points out some AI model results cannot be understood, explained or reproduced and so cannot be critically assessed; lack of explainability can make it hard for regulators to ascertain compliance with model requirements; IAIS (2025) notes explainability-related model risk can let unwarranted or unlawful trends (for example underpricing risks) go undetected, affecting insurers' profitability and balance sheets. (p. 5)[^original]  
  <sub>anchor: "some AI model results cannot be understood, explained or reproduced and therefore cannot be critically assessed"</sub>
- **descriptive / context**: When internal models were first allowed in the Basel Framework, the BCBS emphasised that a black box not well understood by bank personnel does not provide confidence over the rating process or the estimation of PDs (BCBS (2001)); Basel III tempered such models by removing advanced options for certain risk categories and introducing input and output floors (BCBS (2017)). (p. 5)[^original]  
  <sub>anchor: "a ‘black box’ that is not well understood by bank personnel does not provide confidence over the rating process"</sub>
- **descriptive / context**: A key regulatory/supervisory concern is the explainability of AI models, especially for critical business activities; the examples given are customer-facing, core activities such as underwriting or determination of capital requirements. (p. 5)[^original]  
  <sub>anchor: "especially for critical business activities (eg customer-facing, core activities such as underwriting or determination of capital requirements)"</sub>
- **descriptive / finding or result**: Footnote 1 cites IIF-EY (2025) as showing that AI explainability is the top issue raised by financial institutions when engaging with regulators/supervisors on AI. (p. 5)[^original]  
  <sub>anchor: "AI explainability is the top issue raised by financial institutions when engaging with regulators/supervisors on AI"</sub>
- **descriptive / definition**: Footnotes 3 and 4: interpretability is often considered distinct; IBM considers interpretability focused on understanding the inner workings of a model whereas explainability aims to give reasons for output; OCC (2021) defines AI explainability as the extent to which AI decisioning processes and outcomes are reasonably understood by bank personnel. Footnote 2 gives Intesa Sanpaolo's use of machine learning to calculate credit risk regulatory capital as an example. (p. 6)[^original]  
  <sub>anchor: "OCC (2021) defines AI explainability as the extent to which AI decisioning processes"</sub>
- **descriptive / finding or result**: Lack of explainability could contribute to heightened systemic risk; FSB (2024) identifies model risk, data quality and governance as sources of AI-related vulnerabilities, saying complexity, limited explainability and difficulty assessing data quality could increase model risks for firms lacking robust AI governance. (p. 6)[^original]  
  <sub>anchor: "The lack of AI model explainability could potentially contribute to heightened systemic risk"</sub>
- **descriptive / finding or result**: From a consumer protection perspective, IAIS (2025) points out explainability and transparency are key to building trust and holding firms accountable for risks such as unlawful discrimination; complexity can make outcomes hard to explain to consumers and increase the risk that biases go undetected. (p. 6)[^original]  
  <sub>anchor: "explainability and transparency are key to building trust and holding firms accountable for risks posed to consumers"</sub>
- **descriptive / context**: For financial institutions, lack of explainability is an obstacle to adopting AI models and amplifies their model risk; overcoming it matters to avoid missed use cases improving customer experience, compliance, risk management and efficiency. (p. 6)[^original]  
  <sub>anchor: "The use of AI models that lack explainability amplifies financial institutions’ model risk"</sub>
- **descriptive / expectation**: Supervisors generally expect firms to be able to explain AI models used for critical activities or to inform decision-making, to ascertain whether outputs are appropriate and hold firms accountable; a supervisor is unlikely to trust results that cannot be understood. (p. 6)[^original]  
  <sub>anchor: "supervisors generally expect firms to be able to explain AI models that are used for critical activities"</sub>
- **descriptive / context**: Some supervisors recognise overly stringent explainability requirements could impede socially desirable innovation; some authorities implicitly allow or explicitly recognise (EBA (2023), Bank of England and FCA (2024)) that some institutions may use AI models for regulatory capital, indicating the need for authorities to critically review current model guidance in light of AI explainability challenges. (p. 6)[^original]  
  <sub>anchor: "overly stringent explainability requirements could impede socially desirable innovation"</sub>
- **descriptive / context**: Existing international standards and jurisdictional MRM requirements are typically high-level and may not capture AI specificities, so a clearer articulation of explainability for AI would supplement them; IAIS (2025) is cited as international guidance to insurance supervisors on supervising AI use, including explainability expectations. (p. 7)[^original]  
  <sub>anchor: "a clearer articulation of the concept of explainability with regards to AI models would be helpful"</sub>
- **descriptive / context**: The paper aims to describe current MRM guidance, discuss challenges applying it to AI models with limited explainability, and put forward considerations; Section 2 covers MRM requirements affected, Section 3 explainability methods and challenges, Section 4 potential adjustments, Section 5 concludes; footnote 10 repeats that IIF-EY (2025) finds explainability/black box nature the top regulator-firm AI issue. (p. 7)[^original]  
  <sub>anchor: "Section 4 describes potential adjustments to existing MRM requirements to address these challenges"</sub>

## Section 2 – MRM and explainability

- **descriptive / context**: Insurance Core Principle 16 (Enterprise risk management for solvency purposes) addresses use of models for risk measurement including technical provisions; BCBS principles on risk data aggregation and risk reporting call for accurate and reliable generation of risk data, and its stress testing principles provide that models should be fit for purpose and subject to challenge and regular review. (p. 7)[^original]  
  <sub>anchor: "models should be fit for purpose and subject to challenge and regular review"</sub>
- **descriptive / context**: More detailed standard-setter requirements for models in regulatory capital include IAIS ICP 17 (Capital adequacy) and BCBS guidance on the internal ratings-based approach (credit risk) and internal models approach (market risk). (p. 7)[^original]  
  <sub>anchor: "particularly the internal ratings-based (IRB) approach for credit risk and the internal models approach (IMA) for market risk"</sub>
- **descriptive / requirement**: The capital-use standards require effective governance and controls for internal models, assign ultimate responsibility to the board and senior management for understanding the consequences and limitations of model outputs, require institutions to ascertain that methodology and assumptions are conceptually sound, fit for purpose and have good predictive power, and require documentation of model design and assumptions. (p. 7)[^original]  
  <sub>anchor: "assign ultimate responsibility to the board and senior management for understanding the consequences and limitations of model outputs"</sub>
- **descriptive / context**: IAIS (2025) elaborates how existing ICPs apply to insurers' use of AI, covering governance and risk management areas needing particular attention, technical aspects such as data governance and model validation, and activities supporting supervisors and insurers in managing AI-introduced or enhanced risks; Box 1 outlines explainability-related guidance. (p. 7)[^original]  
  <sub>anchor: "IAIS (2025) elaborates on how existing ICPs apply in the context of insurers’ use of AI"</sub>

## Box 1: IAIS Application Paper on the supervision of artificial intelligence – explainability-related guidance

- **expected / expectation**: Under ICP 7 (Corporate governance), IAIS says there should be clear accountability within an insurer for setting expectations on AI systems so that the output generated is explainable, fair and unbiased. (p. 7)[^original]  
  <sub>anchor: "There should be clear accountability within an insurer for setting expectations on AI systems"</sub>
- **expected / expectation**: Under ICP 8 (Risk management and internal controls), insurers should have effective risk management and internal controls to minimise the risk that AI systems adversely affect their financial soundness. (p. 8)[^original]  
  <sub>anchor: "Insurers should have effective risk management and internal controls to minimise the risk that AI systems have an adverse impact"</sub>
- **descriptive / context**: Under ICP 19 (Conduct of business), transparency and explainability of claims decisions and claims dispute resolution influenced by AI systems are especially important. (p. 8)[^original]  
  <sub>anchor: "The transparency and explainability of claims decisions and claims dispute resolution influenced by AI systems are especially important"</sub>
- **expected / expectation**: Under ICP 8 and ICP 19, supervisors should require insurers to meaningfully explain outcomes of the AI systems they use, especially in use cases with material impact on consumers or solvency or used to satisfy legal requirements. (p. 8)[^original]  
  <sub>anchor: "Supervisors should require insurers to meaningfully explain the outcomes of the AI systems that they use"</sub>
- **permissive / recommendation**: Insurers could restrict deployment of AI systems to those that are simple and explainable, or restrict use of complex AI systems to challenging and fine-tuning more traditional mathematical models. (p. 8)[^original]  
  <sub>anchor: "Insurers could restrict deployment of AI systems to those that are simple and explainable"</sub>
- **permissive / recommendation**: Where AI system risks are high and/or the explanation tools themselves have limitations, insurers could instead consider alternative simpler models. (p. 8)[^original]  
  <sub>anchor: "insurers could instead consider alternative simpler models"</sub>
- **expected / expectation**: Where an AI system cannot provide sufficient confidence under new or unexpected conditions, insurers should ensure it can fail safely or escalate to human intervention. (p. 8)[^original]  
  <sub>anchor: "insurers should ensure it can fail safely or escalate to human intervention"</sub>
- **recommended / recommendation**: For highly complex AI systems where the desired level of explainability cannot be achieved, insurers should consider adopting and documenting complementary governance measures such as guardrails (for example enhanced data management) and human oversight. (p. 8)[^original]  
  <sub>anchor: "insurers should consider adopting and documenting complementary governance measures such as the use of guardrails"</sub>
- **expected / expectation**: The level and depth of explanation of an AI model should be tailored to different stakeholders; auditors and supervisors will require more comprehensive technical information than policyholders. (p. 8)[^original]  
  <sub>anchor: "The level and depth of explanation of an AI model should be tailored to the different stakeholders"</sub>

## Section 2 – MRM and explainability

- **descriptive / context**: Only a few national financial authorities have MRM guidelines; building on standard setters' work, they usually focus on models used for calculating regulatory capital. Footnote 15 states guidelines that simply transpose standard-setter capital-model rules (for example the ECB guide to internal models) are not included. (p. 8)[^original]  
  <sub>anchor: "there are only a few financial authorities with MRM guidelines in place"</sub>

## Box 1: IAIS Application Paper on the supervision of artificial intelligence – explainability-related guidance

- **permissive / recommendation**: Under the IAIS guidance in Box 1, deployment of complex AI systems could be made conditional on deploying explainability tools such as Shapley values or LIME, which can illustrate the influence of different variables on AI outcomes, enhancing transparency and trust, with recognition of the limitations of such techniques. (p. 8)[^original]  
  <sub>anchor: "could be conditional on the accompanying deployment of explainability tools such as Shapley values or LIME"</sub>

## Section 2 – MRM and explainability

- **descriptive / data or feature**: Table 1 lists MRM guidelines reviewed: Canada, OSFI, Draft guideline E-23 Model risk management, November 2023 (original issued 2017; consultation closed March 2024, no final version yet); Japan, FSA, Principles for model risk management, November 2021; United Arab Emirates, CBUAE, Model management standards, November 2022; United Kingdom, PRA, Model risk management principles for banks, May 2023. (p. 9)[^original]  
  <sub>anchor: "Financial Services Agency of Japan(FSA)|Principles for model riskmanagement|November 2021"</sub>
- **descriptive / data or feature**: Table 1 also lists the United States: Federal Reserve Board/OCC, Supervisory guidance on model risk management, April 2011; and OCC, Model risk management (Comptroller's Handbook), August 2021, which aligns with the FRB/OCC 2011 guidance but updates it to cover AI-related issues. (p. 9)[^original]  
  <sub>anchor: "Supervisory guidance on modelrisk management|April 2011"</sub>
- **descriptive / finding or result**: All reviewed MRM guidelines cover governance and oversight, model development and documentation, model validation and implementation, and monitoring and maintenance; they require model risk assessment to allow a risk-based application, all cover risks of third-party models, and a couple explicitly mention model explainability. (p. 9)[^original]  
  <sub>anchor: "All guidelines cover governance and oversight, model development and documentation, model validation and implementation, monitoring and maintenance"</sub>
- **descriptive / expectation**: Governance: MRM guidelines emphasise the role of the board and senior management in ensuring effective implementation of the MRM framework, and many expect them to have sufficient understanding of the models and provide effective challenge. (p. 9)[^original]  
  <sub>anchor: "many guidelines also expect them to have sufficient understanding of the models and provide effective challenge"</sub>
- **descriptive / requirement**: Model development and documentation: MRM guidelines require transparent model documentation including theory, assumptions, logic, specifications and limitations; some require the methodology be clear and well articulated to all stakeholders (CBUAE) and that merits and limitations be understood and communicated to model users and stakeholders (PRA). (p. 9)[^original]  
  <sub>anchor: "MRM guidelines require that model documentation be transparent16 and include, among others, the theory, assumptions, logic, specifications and limitations"</sub>
- **descriptive / context**: Footnote 16: Prenio and Yong (2021) explain transparency is a precondition for supervisory assessment of AI models and depends on whether models are built in-house, open or closed source, or third-party proprietary (including big techs); the US Federal Office for Information Security (2024) emphasises transparency should cover the whole AI life cycle and ecosystem, and regulators without a full view of the ecosystem may be unable to properly assess explainability. (p. 9)[^original]  
  <sub>anchor: "Regulators without a full view of the AI ecosystem may not be in a position"</sub>
- **descriptive / requirement**: Model validation: guidelines require validation to assess suitability and conceptual soundness, performed by validators independent from model development; one guideline (OSFI) explicitly expects validation to ensure the model is understandable to relevant stakeholders. (p. 9)[^original]  
  <sub>anchor: "explicitly expects model validation to ensure that the model is understandable to relevant stakeholders"</sub>
- **descriptive / expectation**: Deployment and ongoing monitoring: the FRB/OCC guideline provides that business areas using the model should be able to question its assumptions if outputs do not seem to make sense; the CBUAE guideline says the monitoring objective is to assess whether operating environment changes have affected performance, stability, key assumptions and/or reliability. (p. 10)[^original]  
  <sub>anchor: "business areas using the model should be able to question the model"</sub>
- **descriptive / expectation**: Independent review or internal audit: guidelines generally only expect internal audit to assess effectiveness of MRM framework implementation, but some (BCBS (2022, 2024b), PRA (2023)) also specify independent review to assess appropriateness and soundness of models. (p. 10)[^original]  
  <sub>anchor: "also specify the need for independent review in order to assess the appropriateness and soundness of models"</sub>
- **descriptive / finding or result**: Bank of England and FCA (2024) finds half of survey respondents had only partial understanding of the AI technologies they use due to third-party models; firms are generally expected to comply with MRM requirements even for third-party models. (p. 10)[^original]  
  <sub>anchor: "half of survey respondents reported having only a partial understanding of the AI technologies they use"</sub>
- **descriptive / context**: The requirement to assess a model's riskiness so as to apply MRM requirements on a risk basis exacerbates the implementation challenges for AI explainability. (p. 10)[^original]  
  <sub>anchor: "risk-based application of MRM requirements exacerbates the implementation challenges"</sub>
- **expected / expectation**: Factors that firms need to consider in assessing the riskiness of a model include materiality of use, complexity of the model, uncertainty about inputs, approaches and assumptions, and potential customer impact. (p. 10)[^original]  
  <sub>anchor: "The factors that firms need to consider in assessing the riskiness of a model include materiality of use"</sub>
- **descriptive / finding or result**: The riskier the model, the more frequent and intensive the application of MRM requirements; AI models that lack explainability and are used in high-risk areas will therefore likely receive a high-risk rating, so, somewhat ironically, the MRM guidelines make explainability more relevant for models that lack it. (p. 10)[^original]  
  <sub>anchor: "The riskier the model, the more frequent and intensive the application of the MRM requirements"</sub>
- **descriptive / context**: Footnote 17 notes that the PRA MRM guidelines explicitly list lack of explainability as a factor driving model complexity, and that OCC (2021) states examiners should assess whether model ratings take explainability into account. (p. 10)[^original]  
  <sub>anchor: "lack of explainability is explicitly mentioned as one of the factors that drives model complexity"</sub>
- **mandatory / requirement**: On third-party models, the FRB/OCC and FSA guidelines allow validation to be adjusted (FRB/OCC: banks may rely more on sensitivity analysis and benchmarking; FSA: validation may be based on best available information), whereas the CBUAE guidelines state that a third-party model not fully understood by the firm must not be considered fit for purpose. (p. 11)[^original]  
  <sub>anchor: "if a third-party model is not fully understood by the firm, then it must not be considered fit for purpose"</sub>
- **descriptive / finding or result**: Firms' responsibility towards customers affected by model outcomes is not explicitly covered in existing MRM guidelines, whereas recent AI policy issuances highlight external transparency, external accountability and procedural fairness: informing customers they interact with AI and about AI-driven decisions affecting them, simple explanations of how the model contributes to a decision, and channels for complaints and redress. (p. 11)[^original]  
  <sub>anchor: "recent AI policy issuances highlight the concepts of external transparency, external accountability and procedural fairness"</sub>
- **expected / recommendation**: The paper says external-facing elements should be covered by MRM guidelines since they could result in significant reputational risk, and that implementing them is also constrained by lack of explainability. (p. 11)[^original]  
  <sub>anchor: "These are important elements that should be covered by MRM guideless since they could result in significant reputational risk"</sub>
- **descriptive / context**: Footnote 18: the MAS FEAT Principles state institutions using AI should give data subjects channels to inquire about, appeal and request review of AI-driven decisions; the EU AI Act has similar provisions; Article 22 of the EU GDPR says the data subject has the right not to be subject to a decision based solely on automated processing, including profiling, producing legal effects or similarly significantly affecting him or her. (p. 11)[^original]  
  <sub>anchor: "the data subject shall have the right not to be subject to a decision based solely"</sub>

## Section 3 – Challenges in enforcing explainability requirements in the context of AI

- **descriptive / limitation**: Advanced AI models such as deep neural networks are hard to explain because of many parameters and over-parametrisation (more parameters than data points); unlike linear regression they involve large volumes of non-linear reasoning, and while they may offer superior predictive performance this often comes at the expense of explainability, raising accountability, fairness and ethics concerns. (p. 11)[^original]  
  <sub>anchor: "difficult to explain due to their many parameters and over-parametrisation"</sub>
- **descriptive / limitation**: Footnote 20: De Nederlandsche Bank and the Dutch AFM (2024) highlight AI models might not meet IRB requirements such as that projected results be "plausible and intuitive", since AI can produce non-intuitive results that nevertheless better estimate credit exposure; footnote 21: EBA (2023) highlights the trade-off between explainability and performance. (p. 11)[^original]  
  <sub>anchor: "AI can sometimes produce results that are not intuitive but nevertheless can turn out"</sub>
- **descriptive / limitation**: LLMs are trained on vast data sets and produce outputs from interactions among billions of parameters; they predict the next token probabilistically via a random draw, so output may vary with unchanged input and an unlikely draw can yield hallucinations. Training data and processes are often opaque, and even with open-access weights it is hard to assess future behaviour and delineate capabilities and limitations. (p. 11)[^original]  
  <sub>anchor: "the model’s output may vary even when the input remains unchanged"</sub>

## 3.1 Existing methods for explaining AI models and potential limitations

- **descriptive / context**: Policy discussions mostly use "explainability" while academic literature mostly uses "interpretability"; the terms can convey different meanings, so the paper adopts an understanding based on a review of academic papers (Retzlaff et al (2024), Gilpin et al (2019), Doshi-Velez and Kim (2017)). (p. 11)[^original]  
  <sub>anchor: "In most policy discussions, the term “explainability” is used, whereas in most academic literature, the term “interpretability” is used"</sub>

## Section 3 – Challenges in enforcing explainability requirements in the context of AI

- **descriptive / context**: The probabilistic nature of LLMs (next-token prediction using a random draw) underpins their ability to address complex queries effectively, but it also introduces potential adverse effects, such as output varying for unchanged input and, in extreme cases, 'hallucinations'. (p. 11)[^original]  
  <sub>anchor: "This probabilistic nature underpins the model’s ability to address complex queries effectively"</sub>

## 3.1 Existing methods for explaining AI models and potential limitations

- **descriptive / definition**: The paper defines explainability as the extent to which a model's output can be explained to a human, answering "why did the model produce this output?"; interpretability is the extent to which the inner workings of an AI model can be understood by a human, answering "how did the AI model arrive at this output?". (p. 12)[^original]  
  <sub>anchor: "Interpretability refers to the extent to which the inner workings of an AI model can be understood by a human"</sub>
- **descriptive / context**: The two concepts are interlinked: inherently interpretable models are explainable but not the reverse. A model can be interpreted by assessing how it is trained on training and testing data and tracing how the algorithm processes new input; for complex models where this is not possible one can explain it by describing its behaviour, which requires reasoning and justification for decisions. (p. 12)[^original]  
  <sub>anchor: "Inherently interpretable models are explainable, but the reverse is not true"</sub>
- **descriptive / context**: The paper says explainability is non-binary: a supervisor's conclusion may be "yes, to a certain extent", and the threshold of acceptance depends on the context and the assessor's requirements. (p. 12)[^original]  
  <sub>anchor: "the conclusion could be “yes, to a certain extent”"</sub>

---

[source overview](overview.md) | [next part](digest-002.md)

[^original]: Bank for International Settlements / Basel Committee, "Managing explanations: how regulators can address AI explainability" (2025-09-08). https://www.bis.org/publications/fsi-paper-24-managing-explanations-how-regulators-can-address-ai-explainability
