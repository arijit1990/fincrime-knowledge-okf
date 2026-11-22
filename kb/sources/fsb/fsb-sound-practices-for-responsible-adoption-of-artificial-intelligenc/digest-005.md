---
type: Source Digest
title: 'Sound Practices for Responsible Adoption of Artificial Intelligence (AI): Consultation report - part 5 of 7 (pp. 42-53)'
description: 'Verified paraphrased digest, pp. 42-53: 3. AI lifecycle management > 3.6. Performance management; 3. AI lifecycle management > 3.7. Human oversight; 3. AI lifecycle management > 3.8. Cyber and ICT risk management; and 1 more sections'
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
part: 5
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
digest_points: 54
---

# Sound Practices for Responsible Adoption of Artificial Intelligence (AI): Consultation report (digest)

[previous part](digest-004.md) | [source overview](overview.md) | [next part](digest-006.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (pp. 42-53) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **hypothesis**.

## Assess dimensions of AI performance

- **descriptive / typology or red flag**: Stability is how reliable a model's or system's outputs are over time, including whether the same task or query at different times produces different outputs (footnote 69: the 'capability-reliability' gap, where a model can execute operations but not consistently enough to be reliable). Sensitivity or stress testing feeds extreme inputs or assumptions into the model to determine effects on outputs and can identify limitations, uncertainties and the conditions under which performance deteriorates or fails. (p. 42)[^original]  
  <sub>anchor: "how reliable an AI model’s or system’s outputs are over time"</sub>
- **expected / expectation**: Institutions specify thresholds across all relevant performance dimensions to indicate which results constitute acceptable performance, warrant further investigation or indicate significant issues. Where possible, setting clear thresholds ante hoc (before outputs are generated) is generally preferable to deciding post hoc what is adequate, although this may be harder for some AI such as agentic AI; institutions generally review thresholds periodically to confirm they remain appropriate. (p. 42)[^original]  
  <sub>anchor: "establishing clear performance thresholds _ante hoc_ (i.e. before outputs are generated) is generally preferable"</sub>

## Carry out developmental testing

- **expected / expectation**: Institutions carry out testing during design and development ('developmental testing') to understand early whether a model needs adjustment or additional calibration. It typically covers the performance dimensions where feasible and may also be used to decide whether a use case or its underlying model is worth pursuing further. (p. 42)[^original]  
  <sub>anchor: "carry out testing during the design and development stage (‘developmental testing’)"</sub>
- **permissive / typology or red flag**: Developmental testing, considering how well a model performs according to intended use, may include checking for overfitting (a model narrowly focused on its training data, performing well on it but poorly on new data, contributing to lack of robustness and inability to generalise; footnote 70 says evidence suggests AI models may be more prone to overfitting than non-AI models). (p. 43)[^original]  
  <sub>anchor: "performing well for that training data but poorly on new data"</sub>
- **permissive / typology or red flag**: Developmental testing may also check for unacceptable bias, including statistical biases such as trading platforms favouring large-cap stocks or stocks in certain sectors, which can also lead to legal or regulatory breaches or discrimination against groups. Institutions test for unacceptable bias in the training data, design choice or how output is used; bias can be hard to detect if the institution lacks access to the underlying dataset or the model has explainability limitations. (p. 43)[^original]  
  <sub>anchor: "trading platforms favouring largecap stocks or stocks in certain sectors"</sub>
- **descriptive / limitation**: For GenAI and agentic AI, small linguistic changes to an LLM prompt can significantly change the output, increasing unpredictability; there may be no 'ground truth' (verified true data for training and testing), so assessment may be less straightforward and institutions may include subject-matter experts as evaluators, a multi-disciplinary set of evaluators helping assess all dimensions. (p. 43)[^original]  
  <sub>anchor: "small linguistic changes to the input (prompt) of a LLM can significantly change the output"</sub>

## Case study: Developmental testing

- **descriptive / case example**: A large internationally active bank developing an ML model in trading, expected to beat its non-AI model, found in testing that it did not consistently outperform the existing model including on stability, that the training dataset was not representative of the production data, and that other aspects did not align with deployment conditions. Given these results and the model's higher complexity making it harder to assess, the bank postponed deployment and kept using the non-AI model. (p. 43)[^original]  
  <sub>anchor: "the training dataset was found to be not representative of the production data"</sub>

## Conduct ongoing monitoring and testing

- **expected / expectation**: After developmental testing confirms responsible deployment, institutions undertake ongoing monitoring and testing to (i) confirm the model performs well over time and relative to a range of realised outcomes and (ii) support early identification of material deviations from intended design and timely response. For agentic AI, monitoring may involve regular, routinised assessment of specific actions or consequences, not just output review. (p. 43)[^original]  
  <sub>anchor: "support early identification of material deviations in results from the intended design"</sub>
- **expected / expectation**: Institutions align the frequency, horizon, intensity and type of ongoing monitoring and testing to the characteristics, materiality and risks of each use case. Key steps may include testing over time with new data or data not used in training; repeating pre-deployment tests; monitoring performance degradation; checking for data or model drift; periodically confirming that performance metrics remain appropriate; and assigning staff to try to 'break' the model or find vulnerabilities, weaknesses and uncertainties ('red-teaming'). (p. 44)[^original]  
  <sub>anchor: "assigning staff to try to ‘break’ the AI model or system"</sub>
- **expected / expectation**: Institutions also use benchmarking where appropriate, comparing a model's output with output from other relevant models, systems or information. It is especially helpful when there are insufficient realised outcomes to test against or when triangulating accurate outputs, and most helpful when the alternative output comes from a model taking a different perspective, such as different data sources or methodologies. (p. 44)[^original]  
  <sub>anchor: "Benchmarking is most helpful when the alternative output has been produced by a model or system"</sub>
- **expected / expectation**: As the number of AI use cases (particularly high materiality and risk) grows, institutions assess the resource implications, scalability and viability of different performance assessment and monitoring types and, where appropriate, explore ways to augment assessments potentially through automation. (p. 44)[^original]  
  <sub>anchor: "assess the resource implications, scalability, and viability of different types of performance assessment and monitoring"</sub>
- **expected / expectation**: For models that dynamically update by drawing in new data, altering inputs or changing feature relationships, institutions maintain comprehensive, objective and appropriate testing (including developing new tests and additional bias checks as needed), conduct more frequent and intensive ongoing monitoring, and alert relevant stakeholders about updates. (p. 44)[^original]  
  <sub>anchor: "conduct more frequent and intensive ongoing monitoring, and alert relevant stakeholders about updates"</sub>
- **expected / expectation**: Institutions respond to performance results according to the model, materiality, risk level and nature of findings: poor results can indicate the model needs updating, redeveloping or retiring; mild concern might warrant further testing and closer monitoring; and in certain cases compensating controls such as an overlay or other adjustment to outputs may be appropriate. (p. 44)[^original]  
  <sub>anchor: "poor results can indicate that the AI model or system needs updating, redeveloping, or retiring"</sub>
- **descriptive / context**: Compensating controls can also include more intensive human oversight or limiting use of the model to lower-risk areas until concerns abate, and in many cases may be only temporary measures until more substantial steps address underlying issues. (p. 45)[^original]  
  <sub>anchor: "limiting the use of the AI model or system to lower-risk areas until concerns abate"</sub>

## 3.7. Human oversight

- **descriptive / definition**: Effective human oversight has a tangible positive impact (improving decision-making, preventing harm or providing redress). Effective oversight is meaningful: humans have sufficient ability, authority and incentive to intervene, as opposed to nominal or 'tick-the-box' compliance oversight. (p. 45)[^original]  
  <sub>anchor: "humans having sufficient ability, authority, and incentive to intervene"</sub>

## Design and develop appropriate and meaningful human oversight of AI

- **expected / expectation**: Institutions design and develop AI to enable effective and meaningful human oversight (as far as technically possible), including: enabling staff to assess outputs and understand capabilities and limitations; preventing automation bias (overreliance) through incentive alignment for thorough review, such as performance metrics that reward quality of oversight decisions (footnote 71: for example a model designed to seek human feedback in specific scenarios or give confidence scores); creating feedback mechanisms to learn from oversight decisions, including tracking human overrides, analysing patterns and refining the system and oversight processes; and assessing whether overseers provide effective oversight. (p. 45)[^original]  
  <sub>anchor: "preventing automation bias (i.e. overreliance)71 by creating incentive alignment for thorough, thoughtful review"</sub>

## 3.7. Human oversight

- **expected / expectation**: Sound Practice 10 (Human oversight) describes financial institutions as putting in place appropriate and effective human oversight that is relevant to the materiality, risk, autonomy, complexity and explainability of the different AI use cases. (p. 45)[^original]  
  <sub>anchor: "implement appropriate and effective human oversight relevant to the materiality, risk, autonomy, complexity, and explainability"</sub>

## Design and develop appropriate and meaningful human oversight of AI

- **expected / expectation**: When getting an AI model or system from an open-source repository or a third-party AI provider, financial institutions consider, as part of due diligence, how far the model or system was designed to allow those deploying it to exercise effective and meaningful human oversight. (p. 45)[^original]  
  <sub>anchor: "the extent to which the AI model or system has been designed to enable effective and meaningful human oversight"</sub>
- **expected / expectation**: As a further due diligence consideration, where applicable, financial institutions consider how far the third-party AI provider will itself provide human oversight, for example, for a GenAI model, the extent of human oversight when the provider deploys model updates and new versions. (p. 45)[^original]  
  <sub>anchor: "the extent to which the third-party AI provider will provide human oversight"</sub>

## Select appropriate forms of human oversight

- **expected / expectation**: Institutions select the most appropriate form(s) of human oversight considering materiality, risk and other factors including technical feasibility, proportionality, resource effectiveness and legal, regulatory and supervisory considerations. Common forms may include but are not limited to those in the next points. (p. 46)[^original]  
  <sub>anchor: "select the most appropriate form(s) of human oversight taking into account the materiality, risk"</sub>
- **descriptive / definition**: 'Human-in-the-loop' is human approval of all AI decisions, which might suit situations where accuracy matters more than speed (for example health insurance claim approval). 'AI-in-the-loop' integrates AI into oversight to augment monitoring, using AI as a supportive layer while humans stay in control (for example humans monitor and respond to AI-enabled automated alerts, with agentic systems escalating to humans when accuracy metrics are breached or on request per footnote 72); it may become warranted as institutions scale use cases. (p. 46)[^original]  
  <sub>anchor: "human approval of all decisions made by AI, which might be appropriate in situations where accuracy is more important"</sub>
- **descriptive / definition**: 'Human-on-the-loop' is human intervention periodically or only where necessary, for example when outputs have a low confidence score or an override is needed (an AI chatbot handles routine inquiries with human agents alerted when sentiment analysis detects frustration or request volume exceeds capability). (p. 46)[^original]  
  <sub>anchor: "human intervention periodically or only where necessary"</sub>

## Additional considerations for GenAI and agentic AI

- **expected / expectation**: Steps that financial institutions take for human oversight of GenAI and agentic AI include having a human intervene when an LLM begins producing offensive, illegal or inappropriate output; having humans periodically review and spot-check GenAI outputs for consistency and stability over time; and, as a form of testing, having humans try to push an LLM or AI agent to act outside its defined parameters ("jailbreak"). (p. 46)[^original]  
  <sub>anchor: "requiring a human to intervene when an LLM starts generating offensive, illegal, or inappropriate output"</sub>
- **expected / expectation**: Further steps taken for agentic AI include giving each AI agent an individual identifier that is documented, to support monitoring and identity management, and placing boundaries on agents, such as defining prohibited actions or actions needing human approval at appropriate checkpoints (high risk actions or steps outside the agent's initial human-defined scope). (p. 46)[^original]  
  <sub>anchor: "assigning and documenting individual identifiers to AI agents to facilitate monitoring and identity management"</sub>
- **expected / expectation**: Another step is testing the behaviour of AI agents, including through 'red-teaming' (footnote 74: a structured testing effort to find flaws and vulnerabilities in an AI model or system, often in a controlled environment and in collaboration with AI developers). This can include testing how agents interact with other agents both before and after deployment. (p. 46)[^original]  
  <sub>anchor: "testing the behaviour of AI agents, including through ‘red-teaming’."</sub>
- **expected / expectation**: Steps taken also include defining and, if appropriate, limiting AI agents' ability to interact with their external environment (APIs, data, ICT systems and other agents) until institutions are confident the agents can do so safely. (p. 46)[^original]  
  <sub>anchor: "defining and, if appropriate, limiting AI agents’ abilities to interact with their external environment"</sub>
- **expected / expectation**: Institutions also place controls on AI agents that execute financial transactions, especially with customers' funds. These controls include human approval or dual authorisation above a certain transaction value, restricting agents' direct access to payment systems so a human must carry out execution, and keeping audit trails of agent transactions. (p. 46)[^original]  
  <sub>anchor: "human approval or dual authorisation for transactions above a certain value"</sub>

## Select appropriate forms of human oversight

- **descriptive / definition**: 'Human-in-command' is high-level oversight, including deciding the extent of autonomy, setting guardrails and managing overall impact, aimed at highly autonomous AI such as agentic AI. 'Kill switch' covers mechanisms enabling human intervention to halt or constrain AI operations, from complete shutdown (usable in disabling algorithmic trading) to graduated degradation from autonomous to human operation. 'Contestability' covers mechanisms for human appeal and redress of AI outputs (for example customers appealing AI-enabled loan denials if they suspect unacceptable bias). (p. 47)[^original]  
  <sub>anchor: "mechanisms enabling human intervention to halt or constrain AI operations"</sub>

## Set clear responsibility for human oversight throughout the AI lifecycle

- **expected / expectation**: Because responsible individuals may change through the lifecycle, institutions allocate responsibility for post-deployment monitoring to staff who were not part of design and development to promote objectivity; document who the responsible staff are at different stages (for example through responsibility matrices); and tailor staff training to the lifecycle stage(s) they will be responsible for. (p. 47)[^original]  
  <sub>anchor: "allocate responsibility for monitoring an AI use case after deployment to staff who were not part of design and development"</sub>

## Additional considerations for GenAI and agentic AI

- **expected / expectation**: Institutions analyse human oversight patterns to check that oversight is effective, for example by investigating cases where humans consistently approve agent recommendations without modification (rubber-stamping) or override agents in ways that suggest pervasive misalignment. (p. 47)[^original]  
  <sub>anchor: "analysing human oversight patterns to verify that human oversight is effective"</sub>
- **expected / expectation**: Institutions define an appropriate frequency and operating model for human oversight for the use case, with triggers for moving between forms of oversight based on performance metrics or user requests. In some cases monitoring may need to be continuous or performed by AI, but even when machines do most of the active monitoring, financial institutions and individuals retain ultimate accountability. (p. 47)[^original]  
  <sub>anchor: "financial institutions and individuals retain ultimate accountability"</sub>
- **expected / expectation**: Institutions monitor and document the process followed by AI agents, including key intermediate steps, paying particular attention to tool access patterns that may indicate scope creep or misuse (for example querying more databases than the task needs or accessing customer records more broadly than required). This may cover the reasoning at each autonomous decision point, the APIs, data and other tools used, and the final outcome including the agent's interpretation of success. It can improve staff understanding of how an agent met its objectives (short of full explainability) and support forms of oversight such as contestability, kill switches or overrides. (p. 47)[^original]  
  <sub>anchor: "monitoring and documenting the process of AI agents (including key intermediate steps)"</sub>
- **expected / expectation**: As the use of AI agents across the institution grows, institutions adapt their human resources controls and processes to AI agents so that agents are treated as synthetic employees. (p. 47)[^original]  
  <sub>anchor: "adapting human resources controls and processes to AI agents in a way that treats them as synthetic employees"</sub>

## Adapt or enhance cyber security and ICT risk management to address AI risks

- **expected / expectation**: To manage AI cyber and ICT risks, institutions adapt and enhance, as needed, existing cyber and ICT risk management practices, drawing on extensive regulation, guidance and supervisory expectations from the FSB, standard-setting bodies, G7, national authorities, cybersecurity agencies and others. The report says these measures can even be effective mitigants against advanced AI model capabilities. (p. 48)[^original]  
  <sub>anchor: "adapt and enhance, as needed, existing practices on cyber and ICT risk management"</sub>

## 3.8. Cyber and ICT risk management

- **expected / expectation**: Sound Practice 11 (Cyber and ICT risk management) describes financial institutions as managing AI-related cyber and ICT risks, including, where appropriate, by building AI cyber and ICT risk scenarios into tests and exercises, sharing relevant information, and using AI tools in cyber and ICT risk management. (p. 48)[^original]  
  <sub>anchor: "Financial institutions manage AIrelated cyber and ICT risks, including, where appropriate"</sub>
- **expected / expectation**: Among the listed measures for adapting cyber security and ICT risk management to AI is authentication and identity and access management (IAM), including 'dynamic IAM' for AI agents to address the limitations of IAM for human users, and phishing-resistant multi-factor authentication (MFA) to mitigate some of the risks of advanced AI models. (p. 48)[^original]  
  <sub>anchor: "‘dynamic IAM’ for AI agents to address the limitations of IAM for human users"</sub>

## Adapt or enhance cyber security and ICT risk management to address AI risks

- **descriptive / method**: Existing measures listed include: cyber and ICT governance and cyber hygiene; reducing attack surface through strong network security (documenting which systems are internet-connected and whether the connections are necessary, and segmenting and micro-segmenting the most valuable ICT assets); measures to monitor, prevent and remedy 'shadow AI'; secure development practices for AI; and authentication and identity and access management including 'dynamic IAM' for AI agents and phishing-resistant multi-factor authentication. Footnote 80 describes dynamic IAM as granting, modifying or revoking permissions in real time based on context such as behaviour, device security posture and location. (p. 49)[^original]  
  <sub>anchor: "documenting which systems are connected to the Internet and whether these connections are necessary for functionality"</sub>
- **descriptive / method**: Further listed measures: a multi-layered 'defence-in-depth' strategy so remaining layers still mitigate risk if one or more are breached, particularly important for advanced AI that can sometimes compromise layers such as detection; secure-by-design principles including threat modelling, security considerations in design, secure coding and code reviews; and applying 'least privilege' to AI agents and their sub-agents (minimum permissions and access controls needed for their tasks). (p. 49)[^original]  
  <sub>anchor: "adopting a multi-layered cyber defence strategy (’defence-in-depth’) to AI"</sub>
- **descriptive / method**: Further listed measures: implementing security patches and updates promptly but securely. Some advanced AI is adept at discovering vulnerabilities faster and in greater volume, which may accelerate patching; institutions assess whether they can keep pace with compressed exploitation windows from AI-driven reconnaissance and exploitation, and where patches are unavailable or cannot be applied immediately consider compensating controls such as virtual patching (a policy enforcement layer that mitigates exploitation, for example by monitoring and intercepting attempts, without fixing the vulnerability). Also enhancing monitoring and logging of anomalies and cyber incidents with controls on data provenance, cross-validation of datasets and model behaviour tracking. (p. 50)[^original]  
  <sub>anchor: "Financial institutions assess if they can keep pace with compressed exploitation windows"</sub>

## Understand and monitor AI cyber and ICT risks

- **expected / expectation**: Institutions use specialist information sources to identify common, emerging and new AI cyber and ICT risks, including: the OWASP Machine Learning Security Top 10 (with separate OWASP top 10 lists for agentic and LLM applications); MITRE ATLAS, a knowledge base of adversary tactics and techniques for ML systems across the AI lifecycle; and NIST AI 100-2 E2025, Adversarial Machine Learning, a taxonomy and terminology of attacks and mitigation. (p. 50)[^original]  
  <sub>anchor: "use specialist sources of information to identify common, emerging, and new AI cyber and ICT risks"</sub>

## Use AI-powered tools to manage AI cyber and ICT risks

- **recommended / recommendation**: Institutions consider adopting AI-powered cyber and ICT risk management tools, including: AI-powered firewalls to protect against data exfiltration, harmful content and prompt injection attacks; active liveness detection tools to detect deepfakes; AI-powered behavioural analysis to detect anomalous behaviour, which can help detect distillation, pre-positioning or prompt injection attacks; and advanced AI models to identify and remediate vulnerabilities. (p. 50)[^original]  
  <sub>anchor: "consider adopting AI-powered cyber and ICT risk management tools"</sub>
- **recommended / recommendation**: Further tool types considered: threat modelling and vulnerability identification using adversary tactics and techniques against AI-enabled systems based on threat intelligence; data loss prevention tools using contextual understanding and behavioural monitoring against attacks such as privilege escalation; AI-augmented incident response (automating playbooks, speeding forensic examinations and threat hunting in security operations centres); and advanced or agentic AI for autonomous cyber and ICT risk management, including automating vulnerability management such as patching, security testing including source code reviews, penetration testing and adversarial simulation. Cyber security AI agents could even be used to combat agentic AI cyber-attacks; footnote 88 notes fewer AI tools exist for incident recovery, a possible area for future development. (p. 51)[^original]  
  <sub>anchor: "data loss prevention tools that use contextual understanding and behavioural monitoring to protect data"</sub>

## Incorporate AI cyber and ICT risk scenarios in tests and exercises

- **expected / expectation**: Institutions incorporate AI cyber and ICT risks in scenario testing, other cyber and ICT testing (for example vulnerability scans) and exercises, especially for high materiality or risk use cases. Scenario testing lets them assess and strengthen their ability to respond and recover so critical operations stay within agreed tolerance for disruption in severe but plausible scenarios. (p. 51)[^original]  
  <sub>anchor: "incorporate AI cyber and ICT risks in their scenario testing, other forms of cyber and ICT testing"</sub>

## Case study: UK Cross-Market Operational Resilience Group

- **descriptive / case example**: Some authorities and industry groups keep scenario libraries and some have begun including AI and cyber ICT scenarios. The UK Cross-Market Operational Resilience Group (CMORG), a public-private forum, maintains a Dynamic Scenario Library of severe but plausible scenarios; its 2026 edition added AI and cyber ICT scenarios, including a threat actor using GenAI and agentic AI to bypass a financial institution's internal controls and create staff accounts for criminal activity at scale (data theft, unauthorised transactions, fraud). (p. 51)[^original]  
  <sub>anchor: "threat actor using GenAI and agentic AI to bypass a financial institutions’ internal controls and create staff accounts"</sub>
- **expected / expectation**: Exercises such as tabletop, sector-wide and simulation exercises are another valuable way to assess how institutions and the sector (including third-party providers) coordinate and respond to incidents. Institutions incorporate AI cyber and ICT risks in other testing too; red teaming can test GenAI performance and vulnerability to adversarial attacks such as prompt injection and model inversion and the effectiveness of controls. (p. 51)[^original]  
  <sub>anchor: "another valuable way to assess the ability of financial institutions and the financial sector as a whole"</sub>
- **permissive / context**: Controlled environments are also used to test capabilities and risks of emerging AI, for example to monitor agent behaviour before production. There might be potential to incorporate AI scenarios and tools in threat-led penetration testing (TLPT) in future, but further work is needed to understand ethical, legal and practical implications. (p. 51)[^original]  
  <sub>anchor: "further work is needed to understand the ethical, legal, and practical implications of doing so"</sub>

## 3.9. Third-party risk management

- **expected / expectation**: Institutions leverage existing technology-neutral third-party risk management publications of the FSB, standard-setting bodies, international bodies and national authorities as a foundation for third-party AI risks, adapting them for AI-specific risks. In particular they conduct appropriate due diligence on prospective providers and select an appropriate provider considering business needs, risk and legal and regulatory obligations. (p. 52)[^original]  
  <sub>anchor: "conduct appropriate due diligence on prospective third-party AI providers"</sub>

## Collaborate and share information

- **expected / expectation**: Sound Practice 12 (Third-party AI risk management) describes financial institutions as appropriately managing the risks of using third-party AI, with a focus on performance, transparency, data quality, supply chain and concentration risks, and business continuity. (p. 52)[^original]  
  <sub>anchor: "appropriately manage risks from AI third-party use with a focus on performance, transparency, data quality"</sub>

## 3.9. Third-party risk management

- **expected / expectation**: In managing third-party AI risks, financial institutions include contract terms with third-party AI providers that enable effective oversight, including monitoring (which, per a footnote, may include monitoring how third-party providers of non-AI critical services embed AI into them); access, audit and information rights; business continuity and contingency planning; provisions on data access, quality and security, including responsibility for updating data and information on the jurisdictions where it will be processed; and termination. (p. 52)[^original]  
  <sub>anchor: "access, audit, and information rights; business continuity and contingency planning"</sub>
- **expected / expectation**: Financial institutions appropriately oversee the provision of third-party AI services and may, where appropriate, use independent auditors and pooled audits. (p. 52)[^original]  
  <sub>anchor: "appropriately oversee the provision of third-party AI services"</sub>

## Use AI transparency and assurance tools

- **expected / expectation**: Institutions enhance third-party AI transparency through channels including legal and regulatory disclosures, AI model and system cards, certifications and standards, and leverage disclosure obligations where available. In some jurisdictions AI developers must publish or make available to deploying organisations information on intended, prohibited and restricted uses; data; capabilities, characteristics and limitations (including explainability); feasibility of human oversight; and cyber and ICT security, and providers may also face incident reporting obligations. (p. 53)[^original]  
  <sub>anchor: "enhance third-party AI transparency through various channels"</sub>
- **expected / expectation**: Contractual arrangements with third-party AI providers provide for use of transparency and assurance tools; model and system cards contain information on data, functionality, use cases, potential biases, errors and limitations. AI certifications and standards give assurance on provider governance; a third-party audit is required to obtain certain certifications such as ISO/IEC42001, adding independent validation. These tools can help balance institutions' information needs with providers' need to retain commercially sensitive proprietary information. (p. 53)[^original]  
  <sub>anchor: "A third-party audit is required to obtain certain AI certifications such as ISO/IEC42001"</sub>
- **descriptive / limitation**: A current limitation is that AI transparency tools are generally not tailored to the financial sector and may not address institution-specific risks and regulatory requirements; for example model or system cards may describe how a model was built and its capabilities without guidance on integrating it safely into an institution's environment, including constraints and guardrails. (p. 53)[^original]  
  <sub>anchor: "generally not tailored to the financial sector and may not cater to financial institution-specific risks"</sub>
- **permissive / recommendation**: Financial institutions could collaborate with authorities and third-party AI providers to develop targeted AI transparency and assurance tools, such as financial sector-specific model or system cards; examples exist in some jurisdictions, such as a shared AI responsibility model. (p. 53)[^original]  
  <sub>anchor: "could collaborate with authorities and third-party AI providers to develop targeted AI transparency and assurance tools"</sub>

---

[previous part](digest-004.md) | [source overview](overview.md) | [next part](digest-006.md)

[^original]: Financial Stability Board, "Sound Practices for Responsible Adoption of Artificial Intelligence (AI): Consultation report" (2026-06-10). https://www.fsb.org/uploads/P100626.pdf
