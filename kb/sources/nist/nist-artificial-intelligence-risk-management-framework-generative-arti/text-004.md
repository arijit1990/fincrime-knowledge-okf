---
type: Source Text
title: 'Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile - part 4 of 6 (pp. 37-48)'
description: 'Verbatim extracted text, pp. 37-48: NIST Trustworthy and Responsible AI NIST AI 600-1 > 3. Suggested Actions to Manage GAI Risks'
resource: https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence
tags:
- industry_practice
- model_governance
- model_monitoring
- model_validation
- responsible_ai
- standard
- us
status: stable
source_id: nist-artificial-intelligence-risk-management-framework-generative-arti
issuer: nist
issuer_name: NIST
jurisdictions:
- US
tier: 2
instrument_type: standard
normative_force: industry_practice
publication_date: '2024-07-26'
legal_status: current
part: 4
parts_total: 6
content_mode: full_text
generated:
  by: process:fincrime-kb-build
  at: '2026-11-22T10:06:32Z'
verified:
- by: process:kb-validate/verbatim-coverage
  at: '2026-11-22T10:06:32Z'
sources:
- id: original
  resource: https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence
  title: 'Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile'
  author: org:nist
  last_modified: '2026-04-08T00:00:00Z'
---

# Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile

[previous part](text-003.md) | [source overview](overview.md) | [next part](text-005.md)

> Verbatim text extracted from the original (NIST, 2024-07-26), part 4 of 6, pp. 37-48. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **industry practice**.[^original]

## NIST Trustworthy and Responsible AI NIST AI 600-1


### 3. Suggested Actions to Manage GAI Risks


[p. 37]

|MS-2.7-001|Apply established security measures to: Assess likelihood and magnitude ofvulnerabilities and threats such as backdoors, compromised dependencies, databreaches, eavesdropping, man-in-the-middle attacks, reverse engineering,autonomous agents, model theft or exposure of model weights, AI inference,bypass, extraction, and other baseline security concerns.|Data Privacy; Information Integrity;Information Security; Value Chainand Component Integration|
|MS-2.7-002|Benchmark GAI system security and resilience related to content provenanceagainst industry standards and best practices. Compare GAI system securityfeatures and content provenance methods against industry state-of-the-art.|Information Integrity; InformationSecurity|
|MS-2.7-003|Conduct user surveys to gather user satisfaction with the AI-generated contentand user perceptions of content authenticity. Analyze user feedback to identifyconcerns and/or current literacy levels related to content provenance andunderstanding of labels on content.|Human-AI Configuration;Information Integrity|
|MS-2.7-004|Identify metrics that reflect the effectiveness of security measures, such as dataprovenance, the number of unauthorized access attempts, inference, bypass,extraction, penetrations, or provenance verification.|Information Integrity; InformationSecurity|
|MS-2.7-005|Measure reliability of content authentication methods, such as watermarking,cryptographic signatures, digital fingerprints, as well as access controls,conformity assessment, and model integrity verification, which can help supportthe effective implementation of content provenance techniques. Evaluate therate of false positives and false negatives in content provenance, as well as truepositives and true negatives for verification.|Information Integrity|
|MS-2.7-006|Measure the rate at which recommendations from security checks and incidentsare implemented. Assess how quickly the AI system can adapt and improvebased on lessons learned from security incidents and feedback.|Information Integrity; InformationSecurity|
|MS-2.7-007|Perform AI red-teaming to assess resilience against: Abuse to facilitate attacks onother systems (e.g., malicious code generation, enhanced phishing content), GAIattacks (e.g., prompt injection), ML attacks (e.g., adversarial examples/prompts,data poisoning, membership inference, model extraction, sponge examples).|tInformation Security; Harmful Biasand Homogenization; Dangerous,Violent, or Hateful Content|
|MS-2.7-008 i|Verify fine-tuning does not compromise safety and security controls.|Information Integrity; InformationSecurity; Dangerous, Violent, orHateful Content|

[pp. 38-39]

|MS-2.7-009|Regularly assess and verify that security measures remain effective and have notbeen compromised.|Information Security|

AI Actor Tasks: AI Deployment, AI Impact Assessment, Domain Experts, Operation and Monitoring, TEVV

MEASURE 2.8: Risks associated with transparency and accountability – as identified in the MAP function – are examined and documented.

|MS-2.8-001|Compile statistics on actual policy violations, take-down requests, and intellectualproperty infringement for organizational GAI systems: Analyze transparencyreports across demographic groups, languages groups.|Intellectual Property; Harmful Biasand Homogenization|
|MS-2.8-002 i|Document the instructions given to data annotators or AI red-teamers.|Human-AI Configuration|
|MS-2.8-003|Use digital content transparency solutions to enable the documentation of eachinstance where content is generated, modified, or shared to provide a tamper-proof history of the content, promote transparency, and enable traceability.Robust version control systems can also be applied to track changes across the AIlifecycle over time.|Information Integrity|
|MS-2.8-004 i i|Verify adequacy of GAI system user instructions through user testing.|Human-AI Configuration|
|AI Actor Task i|s: AI Deployment, AI Impact Assessment, Domain Experts, Operation and Monitor|i ing, TEVV|

MEASURE 2.9: The AI model is explained, validated, and documented, and AI system output is interpreted within its context – as identified in the MAP function – to inform responsible use and governance.

|MS-2.9-001|Apply and document ML explanation results such as: Analysis of embeddings,Counterfactual prompts, Gradient-based attributions, Modelcompression/surrogate models, Occlusion/term reduction.|Confabulation|
|MS-2.9-002|Document GAI model details including: Proposed use and organizational value;Assumptions and limitations, Data collection methodologies; Data provenance;Data quality; Model architecture (e.g., convolutional neural network,transformers, etc.); Optimization objectives; Training algorithms; RLHFapproaches; Fine-tuning or retrieval-augmented generation approaches;Evaluation data; Ethical considerations; Legal and regulatory requirements.|Information Integrity; Harmful Biasand Homogenization|

AI Actor Tasks: AI Deployment, AI Impact Assessment, Domain Experts, End-Users, Operation and Monitoring, TEVV

MEASURE 2.10: Privacy risk of the AI system – as identified in the MAP function – is examined and documented.

[pp. 39-40]

|MS-2.10-001|Conduct AI red-teaming to assess issues such as: Outputting of training datasamples, and subsequent reverse engineering, model extraction, andmembership inference risks; Revealing biometric, confidential, copyrighted,licensed, patented, personal, proprietary, sensitive, or trade-marked information;Tracking or revealing location information of users or members of trainingdatasets.|i iHuman-AI Configuration;Information Integrity; IntellectualProperty|
|MS-2.10-002|Engage directly with end-users and other stakeholders to understand theirexpectations and concerns regarding content provenance. Use this feedback toguide the design of provenance data-tracking techniques.|Human-AI Configuration;Information Integrity|
|MS-2.10-003|Verify deduplication of GAI training data samples, particularly regarding syntheticdata.|i i iHarmful Bias and Homogenization|

AI Actor Tasks: AI Deployment, AI Impact Assessment, Domain Experts, End-Users, Operation and Monitoring, TEVV

MEASURE 2.11: Fairness and bias – as identified in the MAP function – are evaluated and results are documented.

[p. 40]

|MS-2.11-001|Apply use-case appropriate benchmarks (e.g., Bias Benchmark Questions, RealHateful or Harmful Prompts,Winogender Schemas15) to quantify systemic bias,stereotyping, denigration, and hateful content in GAI system outputs;Document assumptions and limitations of benchmarks, including any actual orpossible training/test data cross contamination, relative to in-contextdeployment environment.|Harmful Bias and Homogenization|
|MS-2.11-002|Conduct fairness assessments to measure systemic bias. Measure GAI systemperformance across demographic groups and subgroups, addressing bothquality of service and any allocation of services and resources. Quantify harmsusing: field testing with sub-group populations to determine likelihood ofexposure to generated content exhibiting harmful bias, AI red-teaming withcounterfactual and low-context (e.g., “leader,” “bad guys”) prompts. For MLpipelines or business processes with categorical or numeric outcomes that relyon GAI, apply general fairness metrics (e.g., demographic parity, equalized odds,equal opportunity, statistical hypothesis tests), to the pipeline or businessoutcome where appropriate; Custom, context-specific metrics developed incollaboration with domain experts and affected communities; Measurements ofthe prevalence of denigration in generated content in deployment (e.g., sub-sampling a fraction of traffic and manually annotating denigrating content).|i f iHarmful Bias and Homogenization;Dangerous, Violent, or HatefulContent|
|MS-2.11-003|Identify the classes of individuals, groups, or environmental ecosystems whichmight be impacted by GAI systems through direct engagement with potentiallyimpacted communities.|Environmental; Harmful Bias andHomogenization|
|MS-2.11-004|Review, document, and measure sources of bias in GAI training and TEVV data:Differences in distributions of outcomes across and within groups, includingintersecting groups; Completeness, representativeness, and balance of datasources; demographic group and subgroup coverage in GAI system trainingdata; Forms of latent systemic bias in images, text, audio, embeddings, or othercomplex or unstructured data; Input data features that may serve as proxies fordemographic group membership (i.e., image metadata, language dialect) orotherwise give rise to emergent bias within GAI systems; The extent to whichthe digital divide may negatively impact representativeness in GAI systemtraining and TEVV data; Filtering of hate speech or content in GAI systemtraining data; Prevalence of GAI-generated data in GAI system training data.|Harmful Bias and Homogenization|

[pp. 40-42]

> 15 Winogender Schemas is a sample set of paired sentences which differ only by gender of the pronouns used, which can be used to evaluate gender bias in natural language processing coreference resolution systems.

|MS-2.11-005|Assess the proportion of synthetic to non-synthetic training data and verifytraining data is not overly homogenous or GAI-produced to mitigate concerns ofmodel collapse.Harmful Bias and Homogenization|
|---|---|
|AI Actor Tasks: f iOperation and|AI Deployment, AI Impact Assessment, Affected Individuals and Communities, Domain Experts, End-Users,i Monitoring, TEVV|

MEASURE 2.12: Environmental impact and sustainability of AI model training and management activities – as identified in the MAP function – are assessed and documented.

|MS-2.12-001|Assess safety to physical environments when deploying GAI systems.|Dangerous, Violent, or HatefulContent|
|MS-2.12-002|Document anticipated environmental impacts of model development,maintenance, and deployment in product design decisions.|Environmental|
|MS-2.12-003|Measure or estimate environmental impacts (e.g., energy and waterconsumption) for training, fine tuning, and deploying models: Verify tradeoffsbetween resources used at inference time versus additional resources requiredat training time.|Environmental|
|MS-2.12-004|Verify effectiveness of carbon capture or offset programs for GAI training andapplications, and address green-washing concerns.|Environmental|
|AI Actor Tasks: i|AI Deployment, AI Impact Assessment, Domain Experts, Operation and Monitor|i ing, TEVV|

MEASURE 2.13: Effectiveness of the employed TEVV metrics and processes in the MEASURE function are evaluated and documented.

[p. 42]

|MS-2.13-001|Create measurement error models for pre-deployment metrics to demonstrateconstruct validity for each metric (i.e., does the metric effectively operationalizethe desired concept): Measure or estimate, and document, biases or statisticalvariance in applied metrics or structured human feedback processes; Leveragedomain expertise when modeling complex societal constructs such as hatefulcontent.|Confabulation; InformationIntegrity; Harmful Bias andHomogenization|
|AI Actor Tasks: i|AI Deployment, Operation and Monitoring, TEVV||
|MEASURE 3.2:Risk tracking approaches are considered for settings where AI risks are difficult to assess using currently availablemeasurement techniques or where metrics are not yet available.|
|---|
|MS-3.2-001|Establish processes for identifying emergent GAI system risks includingconsulting with external AI Actors.|Human-AI Configuration;Confabulation|
|AI Actor Tasks i|: AI Impact Assessment, Domain Experts, Operation and Monitoring, TEVV||

MEASURE 3.3: Feedback processes for end users and impacted communities to report problems and appeal system outcomes are established and integrated into AI system evaluation metrics.

|MS-3.3-001|Conduct impact assessments on how AI-generated content might affectdifferent social, economic, and cultural groups.|Harmful Bias and Homogenization|
|MS-3.3-002|Conduct studies to understand how end users perceive and interact with GAIcontent and accompanying content provenance within context of use. Assesswhether the content aligns with their expectations and how they may act uponthe information presented.|Human-AI Configuration;Information Integrity|
|MS-3.3-003|Evaluate potential biases and stereotypes that could emerge from the AI-generated content using appropriate methodologies including computationaltesting methods as well as evaluating structured feedback input.|Harmful Bias and Homogenization|

[p. 43]

|MS-3.3-004|Provide input for training materials about the capabilities and limitations of GAIsystems related to digital content transparency for AI Actors, otherprofessionals, and the public about the societal impacts of AI and the role ofdiverse and inclusive content generation.|Human-AI Configuration;Information Integrity; Harmful Biasand Homogenization|
|MS-3.3-005|Record and integrate structured feedback about content provenance fromoperators, users, and potentially impacted communities through the use ofmethods such as user research studies, focus groups, or community forums.Actively seek feedback on generated content quality and potential biases.Assess the general awareness among end users and impacted communitiesabout the availability of these feedback channels.|Human-AI Configuration;Information Integrity; Harmful Biasand Homogenization|
|AI Actor Tasks: f i i|AI Deployment, Affected Individuals and Communities, End-Users, Operation an|f i i d Monitoring, TEVV|

MEASURE 4.2: Measurement results regarding AI system trustworthiness in deployment context(s) and across the AI lifecycle are informed by input from domain experts and relevant AI Actors to validate whether the system is performing consistently as intended. Results are documented.

[pp. 43-44]

|MS-4.2-001|Conduct adversarial testing at a regular cadence to map and measure GAI risks,including tests to address attempts to deceive or manipulate the application ofprovenance techniques or other misuses. Identify vulnerabilities andunderstand potential misuse scenarios and unintended outputs.|Information Integrity; InformationSecurity|
|MS-4.2-002|Evaluate GAI system performance in real-world scenarios to observe itsbehavior in practical environments and reveal issues that might not surface incontrolled and optimized testing environments.|Human-AI Configuration;Confabulation; InformationSecurity|
|MS-4.2-003|Implement interpretability and explainability methods to evaluate GAI systemdecisions and verify alignment with intended purpose.|Information Integrity; Harmful Biasand Homogenization|
|MS-4.2-004|Monitor and document instances where human operators or other systemsoverride the GAI's decisions. Evaluate these cases to understand if the overridesare linked to issues related to content provenance.|Information Integrity|
|MS-4.2-005|Verify and document the incorporation of results of structured public feedbackexercises into design, implementation, deployment approval (“go”/“no-go”decisions), monitoring, and decommission decisions.|Human-AI Configuration;Information Security|
|AI Actor Tasks: i|AI Deployment, Domain Experts, End-Users, Operation and Monitoring, TEVV||

MANAGE 1.3: Responses to the AI risks deemed high priority, as identified by the MAP function, are developed, planned, and documented. Risk response options can include mitigating, transferring, avoiding, or accepting.

|MG-1.3-001|Document trade-offs, decision processes, and relevant measurement andfeedback results for risks that do not surpass organizational risk tolerance, forexample, in the context of model release: Consider different approaches formodel release, for example, leveraging a staged releaseapproach. Considerrelease approaches in the context of the model and its projected use cases.Mitigate, transfer, or avoid risks that surpass organizational risk tolerances.|Information Security|
|MG-1.3-002|Monitor the robustness and effectiveness of risk controls and mitigation plans(e.g., via red-teaming, field testing, participatory engagements, performanceassessments, user feedback mechanisms).|Human-AI Configuration|

AI Actor Tasks: AI Development, AI Deployment, AI Impact Assessment, Operation and Monitoring

MANAGE 2.2: Mechanisms are in place and applied to sustain the value of deployed AI systems.

[pp. 44-45]

|MG-2.2-001|Compare GAI system outputs against pre-defined organization risk tolerance,guidelines, and principles, and review and test AI-generated content againstthese guidelines.|CBRN Information or Capabilities;Obscene, Degrading, and/orAbusive Content; Harmful Bias andHomogenization; Dangerous,Violent, or Hateful Content|
|MG-2.2-002|Document training data sources to trace the origin and provenance of AI-generated content.|Information Integrity|
|MG-2.2-003|Evaluate feedback loops between GAI system content provenance and humanreviewers, and update where needed. Implement real-time monitoring systemsto affirm that content provenance protocols remain effective.|Information Integrity|
|MG-2.2-004|Evaluate GAI content and data for representational biases and employtechniques such as re-sampling, re-ranking, or adversarial training to mitigatebiases in the generated content.|Information Security; Harmful Biasand Homogenization|
|MG-2.2-005|Engage in due diligence to analyze GAI output for harmful content, potentialmisinformation, and CBRN-related or NCII content.|CBRN Information or Capabilities;Obscene, Degrading, and/orAbusive Content; Harmful Bias andHomogenization; Dangerous,Violent, or Hateful Content|

|MG-2.2-006|Use feedback from internal and external AI Actors, users, individuals, andcommunities, to assess impact of AI-generated content.|Human-AI Configuration|
|MG-2.2-007|Use real-time auditing tools where they can be demonstrated to aid in thetracking and validation of the lineage and authenticity of AI-generated data.|Information Integrity|
|MG-2.2-008|Use structured feedback mechanisms to solicit and capture user input about AI-generated content to detect subtle shifts in quality or alignment withcommunity and societal values.|Human-AI Configuration; HarmfulBias and Homogenization|
|MG-2.2-009|Consider opportunities to responsibly use synthetic data and other privacyenhancing techniques in GAI development, where appropriate and applicable,match the statistical properties of real-world data without disclosing personallyidentifiable information or contributing to homogenization.|Data Privacy; Intellectual Property;Information Integrity;Confabulation; Harmful Bias andHomogenization|
|AI Actor Tasks: i|AI Deployment, AI Impact Assessment, Governance and Oversight, Operation an|i d Monitoring|

[pp. 45-46]

MANAGE 2.3: Procedures are followed to respond to and recover from a previously unknown risk when it is identified.

|MG-2.3-001|Develop and update GAI system incident response and recovery plans andprocedures to address the following: Review and maintenance of policies andprocedures to account for newly encountered uses; Review and maintenance ofpolicies and procedures for detection of unanticipated uses; Verify responseand recovery plans account for the GAI system value chain; Verify response andrecovery plans are updated for and include necessary details to communicatewith downstream GAI system Actors: Points-of-Contact (POC), Contactinformation, notification format.|Value Chain and ComponentIntegration|
|AI Actor Tasks i|: AI Deployment, Operation and Monitoring||

MANAGE 2.4: Mechanisms are in place and applied, and responsibilities are assigned and understood, to supersede, disengage, or deactivate AI systems that demonstrate performance or outcomes inconsistent with intended use.

|MG-2.4-001|Establish and maintain communication plans to inform AI stakeholders as part ofthe deactivation or disengagement process of a specific GAI system (including foropen-source models) or context of use, including reasons, workarounds, useraccess removal, alternative processes, contact information, etc.|Human-AI Configuration|

|MG-2.4-002|Establish and maintain procedures for escalating GAI system incidents to theorganizational risk management authority when specific criteria for deactivationor disengagement is met for a particular context of use or for the GAI system as awhole.|Information Security|
|MG-2.4-003|Establish and maintain procedures for the remediation of issues which triggerincident response processes for the use of a GAI system, and provide stakeholderstimelines associated with the remediation plan.|Information Security|
|MG-2.4-004|Establish and regularly review specific criteria that warrants the deactivation ofGAI systems in accordance with set risk tolerances and appetites.|Information Security|

AI Actor Tasks: AI Deployment, Governance and Oversight, Operation and Monitoring

MANAGE 3.1: AI risks and benefits from third-party resources are regularly monitored, and risk controls are applied and documented.

[pp. 46-47]

|MG-3.1-001|Apply organizational risk tolerances and controls (e.g., acquisition andprocurement processes; assessing personnel credentials and qualifications,performing background checks; filtering GAI input and outputs, grounding, finetuning, retrieval-augmented generation) to third-party GAI resources: Applyorganizational risk tolerance to the utilization of third-party datasets and otherGAI resources; Apply organizational risk tolerances to fine-tuned third-partymodels; Apply organizational risk tolerance to existing third-party modelsadapted to a new domain; Reassess risk measurements after fine-tuning third-party GAI models.|Value Chain and ComponentIntegration; Intellectual Property|
|MG-3.1-002|Test GAI system value chain risks (e.g., data poisoning, malware, other softwareand hardware vulnerabilities; labor practices; data privacy and localizationcompliance; geopolitical alignment).|Data Privacy; Information Security;Value Chain and ComponentIntegration; Harmful Bias andHomogenization|
|MG-3.1-003|Re-assess model risks after fine-tuning or retrieval-augmented generationimplementation and for any third-party GAI models deployed for applicationsand/or use cases that were not evaluated in initial testing.|Value Chain and ComponentIntegration|
|MG-3.1-004|Take reasonable measures to review training data for CBRN information, andintellectual property, and where appropriate, remove it. Implement reasonablemeasures to prevent, flag, or take other action in response to outputs thatreproduce particular training data (e.g., plagiarized, trademarked, patented,licensed content or trade secret material).|Intellectual Property; CBRNInformation or Capabilities|

|MG-3.1-005|Review various transparency artifacts (e.g., system cards and model cards) forthird-party models.|Information Integrity; InformationSecurity; Value Chain andComponent Integration|
|AI Actor Tasks: i ii|AI Deployment, Operation and Monitoring, Third-party entities||

MANAGE 3.2: Pre-trained models which are used for development are monitored as part of AI system regular monitoring and maintenance.

[p. 47]

|MG-3.2-001|Apply explainable AI (XAI) techniques (e.g., analysis of embeddings, modelcompression/distillation, gradient-based attributions, occlusion/term reduction,counterfactual prompts, word clouds) as part of ongoing continuousimprovement processes to mitigate risks related to unexplainable GAI systems.|Harmful Bias and Homogenization|
|MG-3.2-002|Document how pre-trained models have been adapted (e.g., fine-tuned, orretrieval-augmented generation) for the specific generative task, including anydata augmentations, parameter adjustments, or other modifications. Access toun-tuned (baseline) models supports debugging the relative influence of the pre-trained weights compared to the fine-tuned model weights or other systemupdates.|Information Integrity; Data Privacy|
|MG-3.2-003|Document sources and types of training data and their origins, potential biasespresent in the data related to the GAI application and its content provenance,architecture, training process of the pre-trained model including information onhyperparameters, training duration, and any fine-tuning or retrieval-augmentedgeneration processes applied.|Information Integrity; Harmful Biasand Homogenization; IntellectualProperty|
|MG-3.2-004|Evaluate user reported problematic content and integrate feedback into systemupdates.|Human-AI Configuration,Dangerous, Violent, or HatefulContent|
|MG-3.2-005|Implement content filters to prevent the generation of inappropriate, harmful,false, illegal, or violent content related to the GAI application, including for CSAMand NCII. These filters can be rule-based or leverage additional machine learningmodels to flag problematic inputs and outputs.|iInformation Integrity; Harmful Biasand Homogenization; Dangerous,Violent, or Hateful Content;Obscene, Degrading, and/orAbusive Content|
|MG-3.2-006|Implement real-time monitoring processes for analyzing generated contentperformance and trustworthiness characteristics related to content provenanceto identify deviations from the desired standards and trigger alerts for humanintervention.|Information Integrity|

[p. 48]

|MG-3.2-007|Leverage feedback and recommendations from organizational boards orcommittees related to the deployment of GAI applications and contentprovenance when using third-party pre-trained models.|Information Integrity; Value Chainand Component Integration|
|MG-3.2-008|Use human moderation systems where appropriate to review generated contentin accordance with human-AI configuration policies established in the Governfunction, aligned with socio-cultural norms in the context of use, and for settingswhere AI models are demonstrated to perform poorly.|Human-AI Configuration|
|MG-3.2-009|Use organizational risk tolerance to evaluate acceptable risks and performancemetrics and decommission or retrain pre-trained models that perform outside ofdefined limits.|CBRN Information or Capabilities;Confabulation|
|AI Actor Tasks: i ii|AI Deployment, Operation and Monitoring, Third-party entities||

MANAGE 4.1: Post-deployment AI system monitoring plans are implemented, including mechanisms for capturing and evaluating input from users and other relevant AI Actors, appeal and override, decommissioning, incident response, recovery, and change management.

|MG-4.1-001|Collaborate with external researchers, industry experts, and communityrepresentatives to maintain awareness of emerging best practices andtechnologies in measuring and managing identified risks.|Information Integrity; Harmful Biasand Homogenization|
|MG-4.1-002|Establish, maintain, and evaluate effectiveness of organizational processes andprocedures for post-deployment monitoring of GAI systems, particularly forpotential confabulation, CBRN, or cyber risks.|CBRN Information or Capabilities;Confabulation; InformationSecurity|
|MG-4.1-003|Evaluate the use of sentiment analysis to gauge user sentiment regarding GAIcontent performance and impact, and work in collaboration with AI Actorsexperienced in user research and experience.|Human-AI Configuration|
|MG-4.1-004|Implement active learning techniques to identify instances where the model failsor produces unexpected outputs.|Confabulation|
|MG-4.1-005|Share transparency reports with internal and external stakeholders that detailsteps taken to update the GAI system to enhance transparency andaccountability.|Human-AI Configuration; HarmfulBias and Homogenization|
|MG-4.1-006|Track dataset modifications for provenance by monitoring data deletions,rectification requests, and other changes that may impact the verifiability ofcontent origins.|Information Integrity|


---

[previous part](text-003.md) | [source overview](overview.md) | [next part](text-005.md)

[^original]: NIST, "Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile" (2024-07-26). https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence
