---
type: Source Digest
title: 'The AI Public-Private Forum: Final report - part 3 of 5 (pp. 19-27)'
description: 'Verified paraphrased digest, pp. 19-27: X Y 28 5,536'
resource: https://www.bankofengland.co.uk/research/fintech/ai-public-private-forum
tags:
- data_governance
- explainability
- industry_practice
- industry_report
- model_governance
- responsible_ai
- uk
status: stable
source_id: pra-boe-the-ai-public-private-forum-final-report
issuer: pra_boe
issuer_name: Prudential Regulation Authority / Bank of England
jurisdictions:
- UK
tier: 1
instrument_type: industry_report
normative_force: industry_practice
publication_date: '2026-08-28'
legal_status: current
part: 3
parts_total: 5
content_mode: digest
generated:
  by: claude-code-subagent/claude-sonnet-5-5
  at: '2026-11-21T23:50:20Z'
verified:
- by: process:kb-digest-check/anchor-match
  at: '2026-11-21T23:50:20Z'
- by: claude-code-judge-agent/claude-opus-5-5
  at: '2026-11-21T23:50:20Z'
sources:
- id: original
  resource: https://www.bankofengland.co.uk/research/fintech/ai-public-private-forum
  title: 'The AI Public-Private Forum: Final report'
  author: org:pra_boe
  last_modified: '2026-08-28T00:00:00Z'
digest_points: 77
---

# The AI Public-Private Forum: Final report (digest)

[previous part](digest-002.md) | [source overview](overview.md) | [next part](digest-004.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (pp. 19-27) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **industry practice**.

## X Y 28 5,536

- **descriptive / definition**: Figure 3 (data types), continued: semi-structured data is less organised than structured data with some hierarchy (tags, structure) present, some data objects without fixed meaning, for example HTML, JSON and XML; unstructured data (images or text) is the least organised, is information that does not follow a pre-existing data model and requires analytical techniques to transform it into meaningful information. The figure is sourced to the Bank of England. (p. 19)[^original]  
  <sub>anchor: "Information that does not follow a pre-existing data model"</sub>
- **descriptive / finding or result**: Paragraph 63: the extent and cost of data cleansing needed to use unstructured data effectively can be significant but is an essential stage to ensure models are trained on accurate and relevant data. Validating aggregated data without knowing its granular structure also presents a risk, as it may contain biases and inaccuracies. (p. 19)[^original]  
  <sub>anchor: "Validating aggregated data without knowing the granular structure of those data also presents a risk"</sub>
- **descriptive / context**: Paragraph 64: synthetic data is data generated algorithmically rather than from actual events or direct measurement. There is huge interest in using it to share data while preserving privacy, and synthetic datasets are used in building and testing models where there are insufficient real data. (p. 19)[^original]  
  <sub>anchor: "data generated algorithmically rather than from actual events or direct measurement"</sub>
- **descriptive / finding or result**: Paragraph 65: it is relatively easy to train AI models on synthetic data but it may take longer to ensure they are suitable for use because they also need testing on actual data. Suitable pipelines to generate and explore synthetic data quickly, with a separate process to validate models on real data, are needed to ensure quality and accuracy and improve speed to market. (p. 19)[^original]  
  <sub>anchor: "models trained on synthetic data also need to be tested on actual data"</sub>

## Data governance and privacy

- **descriptive / finding or result**: Paragraph 67: firms' data management and governance is sometimes organised in silos, which can be inefficient given growing reliance on data insights, particularly for AI systems needing a more holistic cross-functional approach; silos and lack of internal data access also risk inconsistent behaviours and processes. (p. 19)[^original]  
  <sub>anchor: "Silos and lack of internal access to data also create a risk of inconsistent behaviours and processes."</sub>
- **descriptive / finding or result**: Paragraph 68: managing data privacy, access and availability is a key element of any data governance framework, as is full compliance with data protection and additional requirements on customer data. Extra privacy risks may emerge when individual datasets are combined with other internal or external sources that are not covered by the same decision process. (p. 19)[^original]  
  <sub>anchor: "additional privacy risks that emerge when individual datasets are combined with other (internal or external) sources"</sub>
- **descriptive / context**: Paragraph 66 of the AI Public-Private Forum report says data ownership and accountability structures across the organisation, including data consent management, play a key part in the overall data governance structure, and that the use of AI raises the question of where to split data ownership and AI ownership (for example through specific data roles, AI data roles, or joint roles). (p. 19)[^original]  
  <sub>anchor: "Data ownership and accountability structures across the organisation, including data consent management, play a key part"</sub>
- **expected / expectation**: Paragraph 66 of the AI Public-Private Forum report states that, whatever split of data and AI roles an organisation adopts, it should also highlight and ensure collective responsibility. (p. 19)[^original]  
  <sub>anchor: "Whatever the split in roles, the organisation should also highlight and ensure collective responsibility."</sub>

## Data standards and regulation

- **descriptive / finding or result**: Paragraph 70: as firms develop data strategies for AI, there is a growing call for AI-specific data standards. The sector already has data standards and regulation such as BCBS 239 and MiFID II, but additional incremental standards may be needed for most elements of traditional data governance, including documentation, quality, retention, privacy, sovereignty and security. The Alternative Data Council has started to produce standards for investment firms' purchase and use of third-party alternative data. (p. 20)[^original]  
  <sub>anchor: "additional incremental standards may be needed for most elements of traditional data governance"</sub>

## Box 4: BCBS 239

- **descriptive / definition**: Box 4: BCBS 239 is the Basel Committee's standard on 'Principles for effective risk data aggregation and risk reporting', aimed at strengthening bank risk data aggregation and internal risk reporting. Published in 2013 and effective from January 2016, it applies to Global Systemically Important Banks (G-SIBs). (p. 20)[^original]  
  <sub>anchor: "published in 2013 and came into effect from January 2016"</sub>
- **descriptive / definition**: Box 4: BCBS 239 details eleven key principles under three sections: [I] overarching governance and infrastructure, [II] risk data aggregation capabilities and [III] risk reporting practices, plus two additional sections on supervisory principles and on timelines and transitional arrangements (see Annex II). (p. 20)[^original]  
  <sub>anchor: "The standard details eleven key principles structured under three sections"</sub>
- **permissive / recommendation**: Paragraph 71: adapting BCBS 239 to include requirements on representativeness and data cards could advance the data standards debate. BCBS 239 currently includes requirements on accuracy, timeliness, flexibility and completeness but not representativeness (very important for training AI models) and lacks metadata standards. A data card would be a short document giving key information about the data, including metadata, in a structured way, similar to AI model cards. The adaptation could be piloted for a single use-case first (for example consumer credit). (p. 20)[^original]  
  <sub>anchor: "they do not include standards on representativeness, which is very important when training AI models"</sub>
- **descriptive / finding or result**: Paragraph 72: related standards may be needed for technologies integrating data processes with AI modelling, mainly techniques for sharing datasets while protecting private personal data, such as differential privacy, federated learning and homomorphic encryption (Box 5). Most are not unique to AI but become significantly more important in its context. (p. 20)[^original]  
  <sub>anchor: "differential privacy, federated learning, and homomorphic encryption"</sub>

## Box 5: Privacy-preserving methods for sharing data

- **descriptive / definition**: Box 5: differential privacy is a method for sharing characteristics of a dataset without disclosing information on individuals in it; federated learning trains models across distributed and/or decentralised networks using local data without exchanging those data; homomorphic encryption uses cryptographic techniques allowing calculations on encrypted data without decrypting them. (p. 20)[^original]  
  <sub>anchor: "Homomorphic encryption involves the use of cryptographic techniques allowing users to carry out calculations on encrypted data"</sub>
- **descriptive / definition**: Footnote 41: MiFID II is a European Union directive (2014/65/EU) regulating financial markets, with Article 64 setting specific data standards to increase transparency in over-the-counter markets. (p. 20)[^original]  
  <sub>anchor: "a European Union directive (2014/65/EU) for regulating financial markets"</sub>
- **descriptive / finding or result**: Paragraph 73: equal access to and fair pricing of third-party data is a reasonable aim but carries risks: a push for equal access may disrupt markets' ability to identify high-quality datasets and providers, and may add data-handling risk as data move between multiple parties in the value chain. (p. 20)[^original]  
  <sub>anchor: "a push for equal access may disrupt the potential for markets to identify high-quality datasets and providers"</sub>
- **descriptive / finding or result**: Paragraph 74: lack of trust in third-party data quality prevents some firms from using such data, and regulations allowing firms to trust third-party data would let them do more. Data federation, a database management process letting multiple independent databases function as one (such as the approach proposed by GAIA-X), is a possible solution allowing data sharing with strong governance for access, traceability and auditability. (p. 20)[^original]  
  <sub>anchor: "Lack of trust in third-party data quality is preventing some firms from using such data."</sub>
- **descriptive / recommendation**: Paragraph 75: additional guidance on existing UK and international data regulation could be useful, as could international alignment on data and AI governance and coordination across industry and regulators. Instead of a prescriptive approach to third-party data regulation, a good alternative is food-labelling style disclosure: the vendor must supply information on the age of the data, how representative they are, when permission was last sought and so on. (p. 20)[^original]  
  <sub>anchor: "a good alternative is the example of food labelling"</sub>

## Data governance and privacy

- **expected / expectation**: Paragraph 69 of the AI Public-Private Forum report says there is a need to increase data skills across different business areas and teams, because otherwise having a human-in-the-loop might not be an effective safeguard. (p. 20)[^original]  
  <sub>anchor: "There is also a need to increase data skills across different business areas and teams."</sub>
- **descriptive / finding or result**: Paragraph 69 of the AI Public-Private Forum report observes that Board members and senior managers are not always aware of, or do not fully appreciate, the importance of issues such as data quality. (p. 20)[^original]  
  <sub>anchor: "Board members and senior managers are not always aware of, or do not fully appreciate, the importance"</sub>

## Box 5: Privacy-preserving methods for sharing data

- **descriptive / finding or result**: Paragraph 77: developing standards for data cards (and model cards) could be a useful initial step; a use-case specific data card, with a representativeness requirement coupled with existing BCBS 239 standards, could form an updated data standard for that use-case. Data cards are only a partial solution because their benefits tend to come at the end of an AI project; a more anticipatory approach to governance is key to managing AI risks. (p. 21)[^original]  
  <sub>anchor: "data cards are only a partial solution to some of the issues outlined above"</sub>

## Suggestions for good practice – Data

- **expected / recommendation**: Good practice suggestions for data: firms should have processes for tracking and measuring data flows within, into and out of the organisation, and carry out regular data audits and assessments of data usage, including alignment with business objectives. (p. 21)[^original]  
  <sub>anchor: "Have processes in place for tracking and measuring data flows within, as well as into and out of, the organisation."</sub>
- **expected / recommendation**: Good practice suggestions for data: firms should have a clear assessment of the value of the data they hold and use, for specific projects and for the firm as a whole, to inform the cost/benefit analysis of the AI project; clear understanding and documentation of the provenance of data used by AI models, especially third-party data; and clear understanding of the limitations and challenges of using alternative and/or synthetic data. (p. 21)[^original]  
  <sub>anchor: "Have clear understanding and documentation of the provenance of data used by AI models, especially in the case of third-party data."</sub>

## Model risk

- **descriptive / context**: Paragraphs 78-79: the third AIPPF meeting and workshops focused on AI model risk, firms' challenges and emerging best practice through current model risk management (MRM) and new approaches. Modelling and its risks are not new to financial services but AI is a step change that may amplify existing model risks and introduce new ones, so MRM is becoming increasingly important as a primary framework for managing AI-related risks. (p. 21)[^original]  
  <sub>anchor: "MRM is becoming increasingly important as a primary framework for managing AI-related risks in financial services"</sub>

## Suggestions for good practice � Data

- **expected / recommendation**: The Forum's good practice suggestions for data say firms should consider adoption and use of AI holistically, harmonising data and model processes where possible. (p. 21)[^original]  
  <sub>anchor: "Consider adoption and use of AI holistically, harmonising, where possible, data and model processes."</sub>
- **expected / recommendation**: In the same good practice suggestions, firms should in particular aim to coordinate their data management and strategy with their AI management and strategy. (p. 21)[^original]  
  <sub>anchor: "they should aim to coordinate data management and strategy with AI management and strategy"</sub>

## Box 6: What do we mean by model and model risk?

- **descriptive / definition**: Box 6: in the report, a model is a theoretical construct specifying the relationship between sets of input and output variables. A widely used financial services definition is that in the Federal Reserve's SR11-7: a 'quantitative method, system, or approach' applying statistical, economic, financial or mathematical theories, techniques and assumptions to process input data into quantitative estimates. (p. 22)[^original]  
  <sub>anchor: "a theoretical construct that specifies the relationship between sets of input and output variables"</sub>
- **descriptive / definition**: Box 6: model risk is the risk arising from use of models and can result from inadequate model specification, poor implementation or incorrect use. Although limited to capital models for banks, building societies and designated investment firms, the EU CRD IV (Article 3.1.11) defines model risk as the potential loss an institution may incur, as a consequence of decisions principally based on internal model output, due to errors in development, implementation or use. (p. 22)[^original]  
  <sub>anchor: "the risk arising from use of models and can result, among other causes, from inadequate model specification"</sub>

## Key findings – Model risk

- **descriptive / finding or result**: Key finding: most risks from AI models are not new and can arise from non-AI models; what is new is the scale of AI use, the speed of AI systems and the opacity or complexity of the models. Coupled with data risks, including alternative, unstructured data, these can create or amplify challenges, and inadvertent risks can emerge because of unknowns with AI, especially when multiple models interact in a network. (p. 22)[^original]  
  <sub>anchor: "Inadvertent risks can also emerge because there are unknowns with AI"</sub>
- **descriptive / finding or result**: Key finding: complexity is the key challenge for managing AI model risk, covering input complexity (multiple input layers and dimensions), relationships between variables, intricacies of models (for example deep learning) and outputs (actions, algorithms, unstructured such as images or text, and/or quantitative). (p. 22)[^original]  
  <sub>anchor: "Complexity is the key challenge for managing the risks arising from AI models."</sub>
- **descriptive / finding or result**: Key finding: explainability is a key issue with AI systems; approaches should not focus solely on model features and parameters but also on consumer engagement and clear communications. Identifying and managing change in AI models and monitoring and reporting performance are key to ensuring models behave as expected, including monitoring for changes in a model's functional form and outputs. (p. 22)[^original]  
  <sub>anchor: "Explainability is a key issue with AI systems."</sub>

## Model risk, governance, and lifecycle

- **expected / expectation**: Paragraph 80: model risk exists at all stages of the data and model lifecycles (Figure 4) and a firm's MRM processes should be aligned with those stages. Model risk is not specific to AI, but AI's complexity, speed and scale present new challenges and amplify existing risks; AI models can also introduce less well understood non-financial risks such as data privacy and protection, cybersecurity and transfer learning (use of knowledge gained in one domain to solve problems in a related one). (p. 23)[^original]  
  <sub>anchor: "a firm’s MRM processes should be aligned with those stages"</sub>
- **expected / expectation**: Paragraph 81: dynamic AI models learn continuously from live data so outputs change; they could outperform static models by adapting to data drift or concept drift, but firms should align governance processes and assessment of model risk to the adaptation cycle. Most AI applications currently used in financial services are static. (p. 23)[^original]  
  <sub>anchor: "firms should align governance processes and assessment of model risk to the adaptation cycle"</sub>
- **descriptive / definition**: Box 7: model, data or concept drift are common shifts in underlying data, variable relationships or statistical characteristics leading to underperformance and potentially inaccurate outputs. Data drift is unanticipated changes in data inputs or structures not part of training; model drift is reduced performance due to changes in the relationship between input and output variables; concept drift is changes in the statistical properties of the model's target or output variables. (p. 23)[^original]  
  <sub>anchor: "Data drift refers to unanticipated changes in data inputs or structures that were not part of the model training process."</sub>
- **mandatory / requirement**: Paragraph 82 of the AI Public-Private Forum report states that MRM functions and processes within organisations must adapt to the various challenges that AI models introduce or increase. (p. 23)[^original]  
  <sub>anchor: "MRM functions and processes within organisations must adapt to the various challenges that AI models introduce or increase"</sub>
- **descriptive / finding or result**: Paragraph 82 says MRM for AI models requires, among other things, a greater understanding of the use of hyperparameters; understanding and managing explainability and reproducibility issues; and attention to data privacy and bias risks, which can also flow through to models and algorithms. These issues become even more challenging with third-party models. (p. 23)[^original]  
  <sub>anchor: "MRM for AI models requires, among other things: greater understanding of the use of hyperparameters"</sub>
- **descriptive / finding or result**: Paragraph 83 notes that risks can also arise from how a model is used and its business application; examples given are the size of a firm, the number of customers affected by the model, and customers' understanding or perception of the technology. (p. 23)[^original]  
  <sub>anchor: "Risks can also arise in how a model is used and its business application"</sub>
- **recommended / recommendation**: Paragraph 85: the Bank and the FCA should consider creating model risk regulations such as the Federal Reserve's SR11-7. Some UK banks have used the SR11-7 principles and the PRA's Model Risk Management Principles for Stress Testing (SS3/18) as templates to help with lack of clarity in UK guidance. (p. 24)[^original]  
  <sub>anchor: "The Bank and the FCA should consider creating model risk regulations such as the Federal Reserve’s SR11-7."</sub>

## Complexity

- **descriptive / finding or result**: Paragraph 86: AI models in financial services, and wider data modelling and analytics methods, are becoming more complex. Smaller firms, especially recent entrants, can sometimes use more complex AI than larger firms because they are not constrained by legacy systems, and may be incentivised to use complex models to compensate for a lack of data. (p. 24)[^original]  
  <sub>anchor: "Smaller firms, especially recent entrants, can sometimes use more complex AI compared to larger firms"</sub>
- **descriptive / finding or result**: Paragraph 87: complexity of the underlying AI models is the key MRM challenge; increasing complexity of inputs and how models work means traditional MRM may become less effective. Monitoring outputs and performance may make more sense for AI MRM than the traditional focus on assessing inputs, though outputs themselves are becoming more complex. (p. 24)[^original]  
  <sub>anchor: "traditional MRM may become less effective"</sub>
- **descriptive / finding or result**: Paragraph 88: reproducibility (model development documented so the process can be repeated with identical results) is important, especially if customers ask about a decision later. The scale of AI and data poses a challenge because it is unclear what should be logged (for example test data, training data, live business data, source code, explainability metrics) and for how long, all at a cost; models may be stochastic and hard to predict, affecting reproducibility. (p. 24)[^original]  
  <sub>anchor: "the principle that model development should be documented in such a way that the process can be repeated with identical results"</sub>
- **descriptive / finding or result**: Paragraph 89: a tiered, risk-based approach to MRM has benefits, accounting for an implicit trade-off between the risks an AI model poses and the complexity an organisation will bear. Some highly complex models are used in low materiality applications, while high materiality applications tend to use less complex models because explainability to consumers, internal compliance and regulators is very important. (p. 24)[^original]  
  <sub>anchor: "high materiality applications in financial services tend to use less complex models"</sub>
- **descriptive / finding or result**: Paragraph 91: firms will likely use more complex AI models for material use-cases in the near future as they gain proficiency. The MRM challenge is what to do if those models do not perform as expected or their outputs deteriorate beyond acceptable risk tolerance, and how to understand how these complex models shape outcomes. (p. 24)[^original]  
  <sub>anchor: "firms will use more complex AI models for material use-cases in the near future"</sub>

## Explainability

- **descriptive / finding or result**: Paragraph 92: some AI models, such as deep neural networks, lack clear understanding of their inner workings (the black-box problem), prompting calls for more clarity on the level of explainability or interpretability necessary, particularly for regulated activities. (p. 24)[^original]  
  <sub>anchor: "the lack of clear understanding of their inner workings i.e. the black-box problem"</sub>
- **descriptive / finding or result**: Paragraph 93: what an 'explanation' means depends on context; a good external explanation for a customer differs from internal explanations for data scientists or non-technical executives, and they may need separate processes. Even without a requirement to explain to customers, firms would need internal explanations to better understand the AI system's workings and capabilities. (p. 24)[^original]  
  <sub>anchor: "Even if there were no requirement to provide explanations to customers"</sub>

## Model risk, governance, and lifecycle

- **descriptive / finding or result**: Paragraph 84 says that reporting model risk across model types and use-cases, and integrating it with other risks across a firm, can be very difficult, especially where it is not linked to underlying business risks and outcomes. (p. 24)[^original]  
  <sub>anchor: "can be very difficult, especially if this is not linked to underlying business risks and outcomes"</sub>
- **recommended / recommendation**: Paragraph 84 says it is useful to think of model risk as a residual risk, or a root cause, of other risks such as credit, liquidity and reputational risk. (p. 24)[^original]  
  <sub>anchor: "It is useful to think of model risk as a residual risk"</sub>
- **permissive / finding or result**: Paragraph 84 says data risk and model risk can both be aggregated when placed within an operational risk framework and linked to real business outcomes. (p. 24)[^original]  
  <sub>anchor: "Both data risk and model risk can be aggregated when put in the context of an operational risk framework"</sub>

## Complexity

- **permissive / finding or result**: Paragraph 90 says model complexity is not a new issue, and existing IT complexity and dependency can, for example, be partly managed through microservices architectures with techniques such as complex unit testing; this could provide a starting point for managing some AI complexity issues. (p. 24)[^original]  
  <sub>anchor: "existing IT complexity (and dependency) can, for example, be partly managed through microservices architectures"</sub>
- **expected / expectation**: Paragraph 90 says there is a need for systems-level testing of more complex models. (p. 24)[^original]  
  <sub>anchor: "There is also a need for systems-level testing of more complex models."</sub>
- **permissive / finding or result**: Paragraph 90 says the more traditional, linear, sequential approach to developing and producing models may not be appropriate for AI models. (p. 24)[^original]  
  <sub>anchor: "The more traditional, linear, sequential approach to model development and production may not be appropriate for AI models."</sub>

## Explainability

- **descriptive / finding or result**: Paragraph 95: it could be argued the focus should be on customer experience, so that explainability, while important, becomes part of a broader requirement on firms to communicate decisions in meaningful and actionable ways, focusing also on consumer engagement and clear communications. Paragraph 96: firms' design principles and guidelines are not usually communicated to end-users, and communicating internal principles more effectively could be a useful adjunct to model explainability. (p. 25)[^original]  
  <sub>anchor: "communicate decisions in meaningful and actionable ways"</sub>

## Change management, validation, monitoring, and reporting

- **descriptive / finding or result**: Paragraph 97: identifying and managing change in an AI model is a key MRM lifecycle process (Figure 5). A material change may require going through the entire MRM lifecycle and governance process, which is time- and resource-intensive, so developers and firms sometimes set high thresholds for significant change; they can because there is no clear guidance or conceptual clarity on what is a material change, and it is unclear when many small incremental changes become material (analogous to the Ship of Theseus). (p. 25)[^original]  
  <sub>anchor: "there is no clear guidance (or indeed conceptual clarity) on what constitutes a material change"</sub>

## Complexity

- **descriptive / finding or result**: Paragraph 90 states that the maturing of MLOps (the use of ML to automate operational processes) is leading to continuous ML for AI processes, analogous to continuous delivery or deployment, with a focus on orchestration, testing and monitoring. (p. 25)[^original]  
  <sub>anchor: "leading to the application of continuous ML (analogous to continuous delivery or continuous deployment) for AI processes"</sub>

## Explainability

- **descriptive / context**: Paragraph 94 distinguishes between regulating models themselves with a high level of explainability and treating them as black boxes while regulating their inputs, outputs and outcomes; which is more appropriate depends on the context and materiality of the use-case and potentially the regulatory context. (p. 25)[^original]  
  <sub>anchor: "There is a difference between regulating models themselves with a high-level of explainability"</sub>
- **descriptive / finding or result**: Paragraph 94 says clear guidelines on appropriate degrees of explainability for specific use-cases could increase confidence in using the technology in financial services, but could equally hamper desirable innovation. (p. 25)[^original]  
  <sub>anchor: "could increase confidence when using the technology in financial services, but it could equally hamper desirable innovation"</sub>
- **expected / expectation**: Paragraph 94 says that where explainability is not possible, the ability to explain the safeguards put in place to protect against negative outcomes should be considered. (p. 25)[^original]  
  <sub>anchor: "the ability to explain the safeguards that are put in place to protect against negative outcomes should be considered"</sub>
- **descriptive / context**: Paragraph 94 describes striking the right balance as a key consideration for regulators and policy makers as well as firms and third parties. (p. 25)[^original]  
  <sub>anchor: "Striking the right balance is a key consideration for regulators and policy makers"</sub>

## Change management, validation, monitoring, and reporting

- **expected / expectation**: Paragraph 100: monitoring is increasingly important for AI systems but is not always a priority, especially during validation. The validation step itself should ensure appropriate monitoring is in place for the model, including oversight of performance by First-Line-of-Defence (1LOD) and Second-Line-of-Defence (2LOD) teams. (p. 26)[^original]  
  <sub>anchor: "The validation step itself should ensure that there is appropriate monitoring in place for the model"</sub>
- **descriptive / finding or result**: Paragraph 101: two key documents from ongoing validation and monitoring are (i) a monitoring plan covering aspects like frequency, metrics and mitigating actions and (ii) a change plan covering which model infrastructure elements may adapt over time, setting guardrails and the extent of adaptation, and a documentation process for any change. (p. 26)[^original]  
  <sub>anchor: "a monitoring plan covering aspects like the frequency, metrics, and mitigating actions"</sub>
- **expected / expectation**: Paragraph 102: it is a question how firms can best monitor and document the harms and risks raised by AI. While automated monitoring and change management increase efficiency, firms should understand clearly who is responsible for the automated pipeline and specifically the monitoring aspects; clear lines of accountability are crucial for automating AI model monitoring and change management. (p. 26)[^original]  
  <sub>anchor: "firms should understand clearly who is responsible for the automated pipeline"</sub>
- **descriptive / finding or result**: Paragraph 103: differentiating validation from ongoing monitoring is important for managing AI model risk, because monitoring may need to be real-time for certain AI models and conducted by 1LOD functions, whereas traditionally it was done periodically by the Third-Line-of-Defence (3LOD) and audit functions, an approach that may no longer be effective. (p. 26)[^original]  
  <sub>anchor: "the latter may need to be real-time for certain AI models and conducted by 1LOD functions"</sub>
- **expected / expectation**: Paragraph 98 says a vital part of MRM is identifying and managing model drift and defining when a change to a model's data or parameters might constitute a new model. (p. 26)[^original]  
  <sub>anchor: "A vital part of MRM is identifying and managing model drift"</sub>
- **descriptive / finding or result**: Paragraph 98 gives as an example that a change in a model's functional form (such as its number of parameters), or a significant change in outcomes, would make it a new model requiring re-evaluation; this applies especially to reinforcement learning models that can change their behaviour over time. (p. 26)[^original]  
  <sub>anchor: "then that would constitute a new model which needs to be re-evaluated"</sub>
- **descriptive / finding or result**: Paragraph 99 says firms' current change management processes may not suit rapidly changing AI models, because the time needed to complete the change process undermines going through it at all, even when the firm determines a material change has occurred. (p. 26)[^original]  
  <sub>anchor: "Current change management processes within firms may not be suitable for rapidly changing AI models"</sub>
- **expected / expectation**: Paragraph 99 says firms' change management processes have to adapt to meet the need for faster re-training and validation. (p. 26)[^original]  
  <sub>anchor: "change management processes have to adapt to meet the need for faster re-training and validation"</sub>
- **descriptive / finding or result**: Paragraph 99 reports that validation tends to happen periodically (often quarterly or annually) and most firms currently use a waterfall (sequential) approach, which does not work for fast-paced, continual updates of AI models. (p. 26)[^original]  
  <sub>anchor: "validation tends to happen periodically (often quarterly or annually) and most firms currently use a waterfall (sequential) approach"</sub>
- **descriptive / finding or result**: Paragraph 104 says relevant thresholds and metrics for effective AI risk monitoring and change management are specific to the context and use-case. (p. 26)[^original]  
  <sub>anchor: "Relevant thresholds and metrics for effective AI risk monitoring and change management are context and use-case specific."</sub>
- **expected / expectation**: Paragraph 104 says the metrics used should be relevant to the business impact of the model. (p. 26)[^original]  
  <sub>anchor: "The metrics should be relevant to the business impact of the model."</sub>
- **permissive / finding or result**: Paragraph 104 says understanding business outcomes and metrics may help inform the choice of model; firms could ask whether a less complex or non-AI model achieves the same outcome, which in certain circumstances reduces the need for complex models. (p. 26)[^original]  
  <sub>anchor: "firms could ask themselves whether less complex or non-AI model achieve the same outcome"</sub>
- **descriptive / finding or result**: Paragraph 105: one approach to monitoring and auditing third-party models is to shift responsibility from vendor to client via contract, which occurs in most cases because vendors are unlikely to accept liability for clients' use and many clients train third-party models on their own proprietary data. There may be ethical concerns, in particular from civil society wanting providers to take greater responsibility; the draft EU AI regulation proposes holding both vendor and client accountable for credit-scoring AI models. (p. 27)[^original]  
  <sub>anchor: "shift responsibility from vendor to client via contractual agreements"</sub>
- **descriptive / finding or result**: Paragraph 106: use of third-party models and data has increased significantly in recent years, accelerated by the pandemic and the need for cheaper, easy-to-deploy AI; alongside clear benefits there are many challenges, particularly in ensuring full due diligence of the outsourced model. (p. 27)[^original]  
  <sub>anchor: "particularly in ensuring full due diligence of the model that is being outsourced"</sub>
- **expected / expectation**: Paragraph 107: a further question is how firms and senior managers can comply, and demonstrate compliance, with their responsibilities when relying on third-party providers. Contractual relationships can set obligations for responsible practice on both sides, which should include regular monitoring of performance and outcomes both internally and with the third-party provider (a 'shared responsibility model'). (p. 27)[^original]  
  <sub>anchor: "These should include regular monitoring for performance and outcomes, both internally and with the third-party provider"</sub>

## Backup and remediation

- **expected / expectation**: Paragraph 108: given potential AI model risks, backup options and remediation actions need to be considered before a model is put into production so firms can respond appropriately and in a timely manner if AI model performance or output deteriorates beyond the accepted risk threshold. (p. 27)[^original]  
  <sub>anchor: "backup options and remediation actions need to be a consideration before the model is put into production"</sub>
- **expected / expectation**: Paragraph 109: as with monitoring and change management, backup options and remediation actions should be context specific and linked to business outcomes. For example, if an Optical Character Recognition AI model analysing customer documents fails, firms should ask whether they can still process customers that day, whether they have enough human agents while the model is not operating, and whether another model can be used instead. (p. 27)[^original]  
  <sub>anchor: "backup options and remediation actions should be context specific and linked to business outcomes"</sub>
- **descriptive / finding or result**: Paragraph 110 describes one potential solution to model failure as quickly retraining and replicating the model, but notes that retraining is hard, time consuming, and can involve a long governance process. (p. 27)[^original]  
  <sub>anchor: "retraining is hard, time consuming, and can involve a long governance process"</sub>
- **recommended / recommendation**: Paragraph 110 says it is useful for firms to have a simple backup or shadow model they can switch to while they retrain, with the updated AI model to follow once it has passed the appropriate checks. (p. 27)[^original]  
  <sub>anchor: "it is useful to have a simple backup or shadow that firms can switch to and use"</sub>

---

[previous part](digest-002.md) | [source overview](overview.md) | [next part](digest-004.md)

[^original]: Prudential Regulation Authority / Bank of England, "The AI Public-Private Forum: Final report" (2026-08-28). https://www.bankofengland.co.uk/research/fintech/ai-public-private-forum
