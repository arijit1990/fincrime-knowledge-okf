---
type: Source Digest
title: 'Sound Practices for Responsible Adoption of Artificial Intelligence (AI): Consultation report - part 4 of 7 (pp. 30-42)'
description: 'Verified paraphrased digest, pp. 30-42: 3. AI lifecycle management; 3. AI lifecycle management > 3.1. Stages of AI development and deployment; 3. AI lifecycle management > 3.2. Materiality and risk assessment; and 4 more sections'
resource: https://www.fsb.org/uploads/P100626.pdf
tags:
- consultation
- data_governance
- hypothesis
- intl
- model_governance
- model_monitoring
- model_validation
- responsible_ai
status: stable
source_id: fsb-sound-practices-for-responsible-adoption-of-artificial-intelligenc
issuer: fsb
issuer_name: Financial Stability Board
jurisdictions:
- INTL
tier: 2
instrument_type: consultation
normative_force: hypothesis
publication_date: '2026-06-10'
legal_status: consultation
part: 4
parts_total: 7
content_mode: digest
generated:
  by: claude-code-subagent/claude-sonnet-5-5
  at: '2026-11-22T04:55:52Z'
verified:
- by: process:kb-digest-check/anchor-match
  at: '2026-11-22T04:55:52Z'
- by: claude-code-judge-agent/claude-opus-5-5
  at: '2026-11-22T04:55:52Z'
sources:
- id: original
  resource: https://www.fsb.org/uploads/P100626.pdf
  title: 'Sound Practices for Responsible Adoption of Artificial Intelligence (AI): Consultation report'
  author: org:fsb
  last_modified: '2026-06-10T00:00:00Z'
digest_points: 58
---

# Sound Practices for Responsible Adoption of Artificial Intelligence (AI): Consultation report (digest)

[previous part](digest-003.md) | [source overview](overview.md) | [next part](digest-005.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (pp. 30-42) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **hypothesis**.

## 3. AI lifecycle management

- **descriptive / context**: Section 3 covers management of AI risks across the stages of AI development and deployment (the 'AI lifecycle'). Sound practices 5 to 10 relate to certain stages, while sound practices 11 and 12 (cyber and ICT risk management; third-party risk management) apply across all stages. The report notes there is no standard one-size-fits-all lifecycle and use cases may involve stages of varying length. (p. 30)[^original]  
  <sub>anchor: "there is no standard, one-size-fits-all stages or AI lifecycle"</sub>

## 3.1. Stages of AI development and deployment

- **descriptive / context**: The report provides an illustrative AI lifecycle of seven stages to help institutions manage AI risks. Footnote 45 says institutions may develop their own lifecycle processes or adopt the stages of other regulation, guidance or standards, for example the NIST AI Risk Management Framework's four-stage lifecycle (plan, design, develop, deploy). (p. 30)[^original]  
  <sub>anchor: "illustrative AI lifecycle with seven distinct stages is provided"</sub>
- **descriptive / definition**: Lifecycle stage 1, Inception: identifying the needs, goals and feasibility of the AI use case, including defining the context, potential use case(s), materiality and risk assessment. Stage 2, Design and development: defining system architecture and data flows and selecting the AI model or system; key activities are data governance, component selection and implementing initial safety controls, and it may include training a model or customising or fine-tuning third-party or open source models. (p. 30)[^original]  
  <sub>anchor: "Identifying the needs, goals, and feasibility of the AI use case"</sub>
- **descriptive / definition**: Stage 3, Verification and validation: testing that the use case meets specified requirements (verification) and performs as intended in real-world scenarios (validation). Stage 4, Deployment: releasing the model or system into its operational environment, including setting up human oversight and monitoring. Stage 5, Operation and monitoring: running the model, logging activity and monitoring performance, safety and security risks including data drift. (p. 31)[^original]  
  <sub>anchor: "performs as intended in real-world scenarios (validation)"</sub>
- **descriptive / definition**: Stage 6, Re-evaluation: periodically assessing whether the use case still meets its objectives under changing conditions, which may lead to retraining or updating. Stage 7, Retirement: decommissioning the model or system and addressing long-term data and access risks such as archiving or data disposal. (p. 31)[^original]  
  <sub>anchor: "Decommissioning the AI model or system as well as addressing long-term data and access risks"</sub>

## 3.2. Materiality and risk assessment

- **permissive / context**: In assessing materiality and risk, identifying relevance to 'critical operations' and assessing criticality and risks of third-party service relationships, institutions can build on the work of standard-setting bodies and authorities' regulations or guidance on AI risk management, model risk management, operational resilience and third-party risk management. Footnotes note that some jurisdictions use terms such as 'important business services', 'critical or important functions' or 'material third-party arrangements'; third-party services here are those whose failure or disruption could significantly impair viability, critical operations or ability to meet key legal and regulatory obligations. (p. 31)[^original]  
  <sub>anchor: "can build on the work of the SSBs as well as financial authorities’ respective regulations or guidance"</sub>
- **expected / expectation**: Sound Practice 5 (Materiality and risk assessment) describes financial institutions as using an effective, systematic approach to judge the materiality and risk of AI use cases when a use case begins and afterwards. (p. 31)[^original]  
  <sub>anchor: "implement an effective and systematic approach to assess the materiality and risk of AI use cases"</sub>
- **permissive / expectation**: Institutions can develop a specific framework for assessing materiality and risk of AI use cases, or adapt and enhance existing frameworks (model risk, operational resilience, third-party risk) for AI-specific risks. Existing criteria can be directly relevant, for example complexity of the underlying model, criticality to operations, or the nature of data shared with third-party providers; regardless of approach, it is important to capture all relevant dimensions of materiality and risk systematically. (p. 32)[^original]  
  <sub>anchor: "develop a specific framework for assessing the materiality and risk of their AI use cases"</sub>
- **descriptive / context**: Materiality and risk profile of an AI use case are interrelated but different concepts, and institutions may assess them within a single process. Both are relevant in deciding the appropriate, proportionate level of risk management and mitigation, including guardrails and level of human oversight. (p. 32)[^original]  
  <sub>anchor: "The materiality and risk profile of an AI use case are interrelated but are different concepts"</sub>

## Assess materiality and risks of AI use cases at the inception stage and thereafter

- **descriptive / definition**: The materiality of an AI use case is its importance to the institution's viability, critical operations and ability to meet key legal and regulatory obligations (including towards customers). Materiality assessment typically considers the criticality of the operations or business lines the use case supports and its relative importance to them, ranging from narrow administrative tasks (for example automated document sorting) to being essential to effective functioning. (p. 32)[^original]  
  <sub>anchor: "importance to the financial institution’s viability, critical operations, and its ability to meet key legal and regulatory obligations"</sub>

## 3.2. Materiality and risk assessment

- **expected / expectation**: Financial institutions systematically assess the risks an AI use case may create or amplify, including those arising from the AI's autonomy, capabilities, complexity, extent of access to systems and sensitive data, and scope of action. A footnote adds that this may include the institution's evolving understanding of what the AI is capable of doing and allowed to do, and notes there are examples of AI agents, models or systems being capable of performing actions they were not initially designed or expected to do. (p. 32)[^original]  
  <sub>anchor: "the AI’s autonomy, capabilities, complexity, the extent of access to systems and sensitive data"</sub>

## Assess materiality and risks of AI use cases at the inception stage and thereafter

- **expected / expectation**: Materiality may change over time because institutions often deploy AI first in non-critical areas and scale progressively to critical operations. Besides assessing materiality at inception, institutions reassess it at regular intervals and upon certain events or milestones, for example a decision to scale the use case up to critical operations. (p. 33)[^original]  
  <sub>anchor: "reassess it at regular intervals and upon certain events or milestones"</sub>
- **descriptive / definition**: The risks of an AI use case are attributes that can cause harm to the institution (including financial, legal and regulatory, and operational risks) or its customers. A use case can pose high risk even if not material: for example an AI agent on a low materiality task may still have access to ICT assets or much sensitive data and could cause significant harm if it accidentally or intentionally acts outside defined parameters. (p. 33)[^original]  
  <sub>anchor: "An AI use case can pose high risks even if it is not material"</sub>
- **expected / expectation**: The risk assessment also covers cyber/ICT vulnerabilities, data dependencies, explainability, reliability, substitutability, susceptibility to performance degradation and third-party or supply chain dependencies; the feasibility of human oversight and level of reliance on the use case's outputs; and relevant legal and regulatory requirements. (p. 33)[^original]  
  <sub>anchor: "cyber/ICT vulnerabilities, data dependencies, explainability, reliability, substitutability"</sub>
- **expected / expectation**: For each AI use case, institutions assess both inherent risk (the risk before risk management and mitigation is applied) and residual risk (the risk left after management and mitigation). (p. 33)[^original]  
  <sub>anchor: "assess both inherent risk (i.e. the risk posed before relevant risk management and mitigation is applied)"</sub>
- **expected / expectation**: Institutions take a dynamic approach to AI risk assessment because the risk landscape can change quickly. Besides assessing risks at inception, they generally repeat risk assessments periodically or upon events (for example after detecting incidents or performance degradation); reassessment can lead to risks being given a higher or lower tiering (footnote 54: for example complexity-related risks can reduce over time as technology and adoption mature). (p. 33)[^original]  
  <sub>anchor: "generally repeat risk assessments periodically or upon the occurrence of certain events"</sub>

## 3.3. Selection

- **expected / expectation**: Sound Practice 6 (Selection): when selecting AI models or systems, financial institutions consider business objectives, operational and technical needs, and the materiality and risks of AI use cases. (p. 33)[^original]  
  <sub>anchor: "financial institutions consider business objectives, operational and technical needs"</sub>
- **descriptive / context**: Institutions have the ultimate choice whether to adopt AI for specific use cases, considering alignment to business strategy and assessment of benefits and risks. If they adopt AI, at selection they decide whether to develop in-house, procure from third-party providers, use open-source tools or combine these, and which model or system type (traditional, GenAI or agentic) suits the use case. (p. 33)[^original]  
  <sub>anchor: "have the ultimate choice of whether to adopt AI for specific use cases"</sub>
- **expected / expectation**: In making selection decisions institutions consider factors including materiality and risks; customer impact; intended use; whether the use case applies across the institution or to a specific business line or function; infrastructure and technical requirements; data needs and availability; readiness including expertise and skills; legal and regulatory requirements; available resources; costs; and, if applicable, third-party dependencies and risks. (p. 34)[^original]  
  <sub>anchor: "readiness of the financial institution, including expertise and skills"</sub>
- **descriptive / context**: Considerations may involve trade-offs: high performing models can be more complex, computationally intensive and less explainable or transparent than simpler lower-performing ones. The most complex models may not invariably be the most appropriate, and a simpler, less costly, more explainable model may still meet business needs. (p. 34)[^original]  
  <sub>anchor: "The most complex AI models or systems may not invariably be the most appropriate"</sub>
- **expected / expectation**: Cost assessment includes commercial, computing, energy, financial and staff costs of different models plus costs of business continuity and contingency planning with third-party AI providers; institutions consider ways to improve cost efficiency, and selection is informed by research into model capabilities and inputs from business users, control functions, subject matter and technical experts and industry practices. (p. 34)[^original]  
  <sub>anchor: "commercial, computing, energy, financial and staff costs of different AI models or systems"</sub>
- **expected / expectation**: Once a model or system is selected, institutions implement appropriate, documented change management processes throughout the AI lifecycle, in particular for high materiality or risk use cases. (p. 34)[^original]  
  <sub>anchor: "implement appropriate, documented change management processes throughout the AI lifecycle"</sub>

## 3.4. Data governance

- **expected / expectation**: Sound Practice 7 (Data governance): financial institutions establish appropriate data governance to maintain data that is fit-for-purpose for training, testing and using AI (accurate, complete, consistent, reliable, secure). Effective data governance is described as essential for effective AI risk management and high-quality data underpinning reliable outputs. (p. 34)[^original]  
  <sub>anchor: "establish appropriate data governance to maintain data that is fit-for purpose for training, testing, and using AI"</sub>
- **expected / expectation**: Data governance and quality matter whether the model is built in-house or relies on third-party models, systems or data; in the latter case there may be contractual, legal or practical limits on accessing or processing third-party data, and institutions then consider alternative or compensating ways to ensure sound data governance and quality, including assessing the providers' data governance practices, processes and data quality controls. (p. 34)[^original]  
  <sub>anchor: "financial institutions consider alternative or compensating ways to deliver the overall outcomes"</sub>
- **descriptive / context**: AI-specific data governance considerations include: the role of data in shaping design choices and outputs; variety of data (multimodal, unconventional such as social media feeds, and synthetic); forms (structured, semi-structured, unstructured); velocity (real-time or near real-time, for example trading data and social media feeds); volume, particularly for GenAI; and data's ability to influence the behaviour of AI agents, creating risks in how agents ingest, interpret, memorise, use and re-use data. (p. 35)[^original]  
  <sub>anchor: "how agents ingest, interpret, memorise, use, and re-use data"</sub>

## Establish effective data governance frameworks

- **expected / expectation**: Institutions adopt a centralised data governance framework, decentralised but consistent frameworks, or a hybrid. It may be pre-existing and cover data generally, provided it covers data used for AI and addresses AI-specific considerations. (p. 35)[^original]  
  <sub>anchor: "adopt a centralised data governance framework, decentralised but consistent frameworks, or a hybrid framework"</sub>
- **expected / expectation**: The data governance framework also addresses data issues in third-party AI models, systems or applications the institution deploys, including where it provides prompts, internal documents or other context to a third-party tool, or the tool accesses the institution's data for outputs (for example an LLM accessing confidential or sensitive data for Retrieval-Augmented Generation). (p. 36)[^original]  
  <sub>anchor: "where the financial institution provides prompts, internal documents, or other context to a third-party tool"</sub>
- **expected / expectation**: An effective data governance framework addresses: alignment with risk appetite and strategy; clear accountability where the institution uses its own, public and/or third-party data; basic data literacy for all staff and targeted training for staff working with data; resources for AI data processing including computation and storage; procedures for classification and labelling of data including metadata; guidelines for unconventional data and different formats; data security including controls for authorised access and data recovery and for confidential and personal data (including privacy enhancing techniques); and an adaptable but consistent approach to assessing data quality and performance. (p. 36)[^original]  
  <sub>anchor: "procedures for the classification and labelling of data, including metadata"</sub>

## Effectively manage different stages of AI data use

- **descriptive / method**: Managing stages of AI data use typically includes: an initial assessment of availability, quality, quantity and suitability of data (which may influence the design choice and whether to use internal, public or third-party data); a data collection stage tracking and documenting authenticity and origin (data provenance), which can include due diligence on public or third-party data (footnote 55: for example checking GenAI-generated data for accuracy and hallucinations before using it to train another model). (p. 36)[^original]  
  <sub>anchor: "tracks and documents the authenticity and origin of data (data provenance)"</sub>
- **descriptive / method**: Further stages: data classification documenting materiality, risk, sensitivity, intended and prohibited uses and other characteristics; data preparation (aggregating, annotating, cleaning, enriching, labelling or updating), described as essential and the most resource-intensive (footnote 56: this may embed instructions in metadata on sensitivity, legal requirements and permitted and prohibited uses, acting as guardrails on AI actions, 'policy aware' data); a data quality assessment after preparation and before deployment identifying gaps, limitations and mitigating or compensating measures; and post-deployment monitoring to remediate problems such as data drift. (p. 36)[^original]  
  <sub>anchor: "a data preparation stage which may involve aggregating, annotating, cleaning, enriching, labelling, or updating data"</sub>
- **expected / expectation**: Documenting key steps across these stages is integral to tracking how data is enhanced, enriched, transformed and used as it flows through the institution ('data lineage'), which can enhance data quality, facilitate auditability and aid remediation of issues and risks including root cause analysis. (p. 36)[^original]  
  <sub>anchor: "Documenting key steps throughout these stages is integral for tracking and understanding how data is enhanced"</sub>

## 3.5. Explainability and transparency

- **expected / expectation**: Sound Practice 8 (Explainability and transparency): financial institutions understand differences in explainability of various types of AI; if appropriate and feasible they adopt more explainable AI or consider compensating controls; and they provide appropriate transparency tailored to different stakeholders. (p. 37)[^original]  
  <sub>anchor: "If appropriate and feasible, financial institutions adopt more explainable AI, or consider compensating controls"</sub>
- **descriptive / definition**: In this report explainability is the ability of a model or system to give clear and interpretable outputs or decisions, specifically the extent to which humans can understand how it generates outputs from inputs, including (i) factors, logic or processes contributing to outputs, (ii) relative importance of input variables or features, and (iii) how methodological relationships vary across context or use cases. It stems from model characteristics and is not binary but a continuum. Footnote 57 defines the related concept interpretability as the ease or difficulty of predicting what a model will do. (p. 37)[^original]  
  <sub>anchor: "the extent to which humans can understand how an AI model or system generates outputs from inputs"</sub>
- **descriptive / definition**: Transparency is the extent to which appropriate information about a model or system is made available to relevant stakeholders, including the board and senior management, counterparties and customers interacting with it, and authorities. Explainability and transparency are complementary but not synonymous: even with appropriate information available, a model may have inherent explainability limits and neither developers nor deployers may understand how it translates inputs into outputs. (p. 37)[^original]  
  <sub>anchor: "Explainability and transparency are complementary but not synonymous"</sub>

## Explainability

- **expected / expectation**: Institutions identify, understand and (where appropriate) communicate the degree of explainability of models and systems for specific use cases, recognising that (i) importance of explainability may vary with autonomy, materiality and risk, and (ii) explainability is not an end in itself but enables accountability, assessment of conceptual soundness and compliance with legal and regulatory requirements. (p. 37)[^original]  
  <sub>anchor: "explainability is not an end in itself but enables accountability"</sub>
- **descriptive / context**: Choices to address explainability issues include building explainability into development, using explainability methods, and applying compensating controls where explainability is limited; the appropriate choice depends on the use case. (p. 37)[^original]  
  <sub>anchor: "building explainability into AI model or system development, using explainability methods"</sub>
- **expected / expectation**: Where justified, financial institutions consider trade-offs between explainability and performance. Limited explainability might be acceptable in some use cases; for instance, in certain fraud detection use cases the greater predictive power of less explainable AI may justify using it. By contrast, AI heavily relied on for credit decisioning, insurance underwriting or other activities with potentially high customer impact may warrant greater explainability. (p. 37)[^original]  
  <sub>anchor: "in certain fraud detection use cases the superior predictive power of less explainable forms of AI may warrant their use"</sub>

## Build explainability into model development

- **permissive / expectation**: During design and development institutions may create or select more explainable forms of AI if they do not perform significantly differently from more complex, less explainable forms, and acknowledge that, all else equal, lower explainability increases uncertainty about the model or system. (p. 38)[^original]  
  <sub>anchor: "may create or select more explainable forms of AI if they do not perform significantly differently"</sub>
- **descriptive / method**: Explainability methods are usually applied after the model generates outputs ('post-hoc explainability'; examples in footnote 58: partial dependence plots and feature importance analysis) and generally when explainability challenges arise in development. Institutions understand that methods vary in applicability, maturity and scope, have limitations that may add uncertainty, have prerequisite conditions to function, and can involve trade-offs. (p. 38)[^original]  
  <sub>anchor: "usually after the AI model or system generates its outputs (‘post-hoc explainability’)"</sub>

## Apply explainability methods

- **expected / expectation**: Institutions use explainability methods as part of a broader suite of AI risk management and mitigation tools rather than standalone solutions; avoid over-reliance on a single method, combining two or more methods where appropriate ('triangulation'); and recognise that explanations may be susceptible to assumptions, data characteristics or feature correlations and that some methods themselves rely on additional models. (p. 38)[^original]  
  <sub>anchor: "avoid over-reliance on a single method"</sub>
- **descriptive / context**: Explainability methods can give insight into model behaviour at global or local level, both relevant depending on the use case, materiality, risk and AI type. Agentic systems executing sequential decisions may warrant approaches examining intermediate decisions and steps, not only final output, and logs of agent activity can help humans track actions in real time or after the fact; footnote 61 says institutions deploying multi-step agentic systems are developing approaches to trace and evaluate the full reasoning path. (p. 39)[^original]  
  <sub>anchor: "look not just at the agent’s final output but intermediate decisions and steps"</sub>
- **descriptive / definition**: Global explainability describes how a model or system behaves overall (for an ML credit scoring model, the key drivers of output across all relevant borrowers; for an agentic system, typical execution patterns and common decision pathways). Local explainability explains how a given single output was delivered (for the credit model, key drivers for an individual borrower; for the agentic system, the specific sequence of reasoning steps, tool invocations and intermediate decisions behind the specific outcome). (p. 39)[^original]  
  <sub>anchor: "refers to how an AI model or system behaves overall"</sub>

## Case study: Project Noor

- **descriptive / case example**: Project Noor ('light' in Arabic) is a BIS Innovation Hub initiative to equip financial supervisors with independent, practical tools to evaluate and interpret the inner workings of AI models used by banks. Led by the BIS Innovation Hub Hong Kong Centre with the HKMA, UK FCA and Saudi Central Bank, it will prototype the latest explainable AI (XAI) techniques in a controlled setting, converting model logic into plain language and visuals showing which factors influenced a decision and its sensitivity, while preserving privacy, so supervisors can verify model transparency and test robustness. (p. 39)[^original]  
  <sub>anchor: "equip financial supervisors with independent, practical tools to evaluate and interpret the inner workings of AI models"</sub>

## Deploy compensating controls

- **expected / expectation**: Where explainability is constrained by model complexity, limited access to information about the model or system, or third-party dependencies, institutions deploy compensating controls including: guardrails such as stricter limits on permissible use cases; benchmarking and/or challenger models or systems (footnote 64: a new, alternative or retrained model tested against the deployed 'champion' model); sensitivity and stress testing; enhanced data governance; more extensive validation and testing; and increased human oversight such as heightened scrutiny of outputs after deployment. (p. 39)[^original]  
  <sub>anchor: "financial institutions deploy compensating controls including"</sub>
- **expected / expectation**: Compensating controls are particularly important in high materiality, high-risk use cases, where they can help institutions accept limited explainability while mitigating risk. If they cannot mitigate the risk from limited explainability in line with risk appetite and tolerance, the institution considers alternatives such as a more explainable AI or non-AI model or system, even if performance is inferior. (p. 40)[^original]  
  <sub>anchor: "such as deploying a more explainable AI or non-AI model or system, even if performance is inferior"</sub>

## Transparency

- **descriptive / context**: Transparency keeps internal and external stakeholders informed about models affecting them: for internal stakeholders (including those deploying third-party models) it enables assessing whether the model remains fit-for-purpose and performs as intended; for customers it helps them understand the role AI plays in products and how it may have influenced outcomes. (p. 40)[^original]  
  <sub>anchor: "Transparency is key for ensuring that both internal and external stakeholders are appropriately informed"</sub>
- **expected / expectation**: Institutions make available appropriate information on their use of AI to internal and external stakeholders, which may include intended, permitted and prohibited uses, capability and limitations, training data if available, and development process. The optimal level varies by recipient, stage of development and deployment, and whether the model is internal or procured from a third party. (p. 40)[^original]  
  <sub>anchor: "make available appropriate information relating to their use of AI to internal and external stakeholders"</sub>
- **expected / expectation**: Institutions tailor the information they provide to different stakeholders to support effective challenge and accountability, oversight and use of AI, while keeping proportionality and avoiding undue complexity; the information given to customers, authorities, auditors, risk managers, and the board and senior management differs given their needs, expertise, responsibilities and decision making. (p. 40)[^original]  
  <sub>anchor: "tailor the information they provide to different stakeholders to support effective challenge and accountability"</sub>

## Transparency to customers and end-users

- **expected / expectation**: Institutions consider the information customers need to understand the nature and limitations of products or services where AI plays a material role. Appropriate transparency does not necessarily entail disclosing AI use to end-users in all circumstances, but may include informing them (i) that they are interacting with AI (for example chatbots), (ii) if AI might materially influence decisions affecting them, (iii) of limitations of the model or system, and/or (iv) of their rights to appropriate explanations, contestability or redress mechanisms if applicable. The section can also apply to investors. (p. 40)[^original]  
  <sub>anchor: "does not necessarily entail financial institutions disclosing to end-users that they are using AI in all circumstances"</sub>
- **permissive / recommendation**: Institutions may also consider offering 'opt-out' options or channels that allow customers to request a review of AI-generated outputs or human assistance. (p. 40)[^original]  
  <sub>anchor: "Financial institutions may also consider offering “opt-out” options or channels"</sub>

## Transparency

- **expected / expectation**: Financial institutions tailor the information they give different stakeholders to support effective challenge, accountability, oversight and use of AI, while keeping proportionality and avoiding undue complexity. Appropriate transparency involves explaining how AI models or systems produce their outputs (subject to the explainability limitations noted earlier) in a way the intended audience can understand. What is provided to customers, authorities, auditors, risk managers, the board and senior management differs, reflecting their differing needs, expertise, responsibilities and decision making. (p. 40)[^original]  
  <sub>anchor: "Appropriate transparency involves providing information about how AI models or systems produce their outputs"</sub>

## 3.6. Performance management

- **expected / expectation**: Institutions evaluate AI performance across different dimensions, proportionately and over time (including ongoing monitoring), adapting assessment to the objectives and anticipated outcomes of each use case, and adjust the frequency, intensity, scope and types of assessment based on factors including the materiality and risk of the use case; material or high risk use cases may justify higher performance requirements and lower tolerance for errors. (p. 41)[^original]  
  <sub>anchor: "adjust the frequency, intensity, scope, and types of performance assessment based on factors including"</sub>

## Assess dimensions of AI performance

- **expected / expectation**: Further factors for adjusting assessment: the model's attributes, including complexity and scope of action (more complex models may be harder to evaluate; broader scope may have greater downstream consequences); the use case's prior performance track record, which may signal where closer scrutiny is needed and helps calibrate benchmarks; any recent changes to the model or system or its data; and any significant changes to relevant real-world conditions. (p. 41)[^original]  
  <sub>anchor: "A model's or system’s performance track record may signal where closer scrutiny is needed"</sub>

## 3.6. Performance management

- **expected / expectation**: Sound Practice 9 (Performance management) describes financial institutions as evaluating the performance of AI use cases in proportion to their materiality and risk, including through performance assessments, testing and ongoing monitoring. (p. 41)[^original]  
  <sub>anchor: "evaluate the performance of AI use cases proportionately to their materiality and risk"</sub>

## Assess dimensions of AI performance

- **descriptive / context**: Performance assessment types used for non-AI models can help assess AI (for example accuracy, benchmarking, range of output, robustness). Assessing traditional AI generally compares a quantitative output with predetermined targets or thresholds (predicted versus actual values) and is conceptually straightforward and easier to automate. (p. 42)[^original]  
  <sub>anchor: "comparing a quantitative output with predetermined targets or thresholds"</sub>
- **descriptive / limitation**: GenAI produces a range of potentially acceptable outputs rather than a single correct one, so assessment is harder to automate and may involve more human judgment and qualitative metrics such as coherence or relevance. Assessing agentic AI performance is a live area of research and can be more complex because it must consider both whether the agent achieved its objective and whether its actions were appropriate. (p. 42)[^original]  
  <sub>anchor: "Assessing the performance of agentic AI is a live area of research"</sub>
- **expected / expectation**: Institutions assess performance dimensions individually and collectively, with weighting and measures set by the use case. Dimensions often include accuracy (how close output is to target or realised outcomes, measurable in different ways and along various horizons, with some models better short-term and others medium or long-term). (p. 42)[^original]  
  <sub>anchor: "how close the output aligns with target or realised outcomes"</sub>
- **descriptive / typology or red flag**: Range of output (also called 'confidence band' or 'distribution of outcomes') is whether output is centrally clustered or widely dispersed, with a narrower range generally preferred, indicating the uncertainty of an output and whether a point estimate is representative. Robustness is how well the AI performs in new conditions (ability to generalise to new data); some forms of AI may experience natural degradation over time. The excerpt ends within this list of dimensions. (p. 42)[^original]  
  <sub>anchor: "whether output is centrally clustered or more widely dispersed, with a narrower range generally preferred"</sub>

---

[previous part](digest-003.md) | [source overview](overview.md) | [next part](digest-005.md)

[^original]: Financial Stability Board, "Sound Practices for Responsible Adoption of Artificial Intelligence (AI): Consultation report" (2026-06-10). https://www.fsb.org/uploads/P100626.pdf
