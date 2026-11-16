---
type: Source Text
title: 'Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile - part 3 of 6 (pp. 25-37)'
description: 'Verbatim extracted text, pp. 25-37: NIST Trustworthy and Responsible AI NIST AI 600-1 > 3. Suggested Actions to Manage GAI Risks'
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
part: 3
parts_total: 6
content_mode: full_text
generated:
  by: process:fincrime-kb-build
  at: '2026-11-16T16:23:02Z'
verified:
- by: process:kb-validate/verbatim-coverage
  at: '2026-11-16T16:23:02Z'
sources:
- id: original
  resource: https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence
  title: 'Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile'
  author: org:nist
  last_modified: '2026-04-08T00:00:00Z'
---

# Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile

[previous part](text-002.md) | [source overview](overview.md) | [next part](text-004.md)

> Verbatim text extracted from the original (NIST, 2024-07-26), part 3 of 6, pp. 25-37. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **industry practice**.[^original]

## NIST Trustworthy and Responsible AI NIST AI 600-1


### 3. Suggested Actions to Manage GAI Risks


[p. 25]

|GV-6.1-005|Implement a use-cased based supplier risk assessment framework to evaluate andmonitor third-party entities’ performance and adherence to content provenancestandards and technologies to detect anomalies and unauthorized changes;services acquisition and value chain risk management; and legal compliance.|Data Privacy; InformationIntegrity; Information Security;Intellectual Property; Value Chainand Component Integration|
|GV-6.1-006|Include clauses in contracts which allow an organization to evaluate third-partyGAI processes and standards.|Information Integrity|
|GV-6.1-007|Inventory all third-party entities with access to organizational content andestablish approved GAI technology and service provider lists.|Value Chain and ComponentIntegration|
|GV-6.1-008|Maintain records of changes to content made by third parties to promote contentprovenance, including sources, timestamps, metadata.|Information Integrity; Value Chainand Component Integration;Intellectual Property|
|GV-6.1-009|Update and integrate due diligence processes for GAI acquisition andprocurement vendor assessments to include intellectual property, data privacy,security, and other risks. For example, update processes to: Address solutions thatmay rely on embedded GAI technologies; Address ongoing monitoring,assessments, and alerting, dynamic risk assessments, and real-time reportingtools for monitoring third-party GAI risks; Consider policy adjustments across GAImodeling libraries, tools and APIs, fine-tuned models, and embedded tools;Assess GAI vendors, open-source or proprietary GAI tools, or GAI serviceproviders against incident or vulnerability databases.|iData Privacy; Human-AIConfiguration; InformationSecurity; Intellectual Property;Value Chain and ComponentIntegration; Harmful Bias andHomogenization|
|GV-6.1-010|Update GAI acceptable use policies to address proprietary and open-source GAItechnologies and data, and contractors, consultants, and other third-partypersonnel.|Intellectual Property; Value Chainand Component Integration|
|AI Actor Task i ii|s: Operation and Monitoring, Procurement, Third-party entities||

GOVERN 6.2: Contingency processes are in place to handle failures or incidents in third-party data or AI systems deemed to be high-risk.

[pp. 25-26]

|GV-6.2-001|Document GAI risks associated with system value chain to identify over-relianceon third-party data and to identify fallbacks.|Value Chain and ComponentIntegration|
|GV-6.2-002|Document incidents involving third-party GAI data and systems, including open-data and open-source software.|Intellectual Property; Value Chainand Component Integration|

|GV-6.2-003|Establish incident response plans for third-party GAI technologies: Align incidentresponse plans with impacts enumerated in MAP 5.1; Communicate third-partyGAI incident response plans to all relevant AI Actors; Define ownership of GAIincident response functions; Rehearse third-party GAI incident response plans ata regular cadence; Improve incident response plans based on retrospectivelearning; Review incident response plans for alignment with relevant breachreporting, data protection, data privacy, or other laws.|Data Privacy; Human-AIConfiguration; InformationSecurity; Value Chain andComponent Integration; HarmfulBias and Homogenization|
|GV-6.2-004|Establish policies and procedures for continuous monitoring of third-party GAIsystems in deployment.|Value Chain and ComponentIntegration|
|GV-6.2-005|Establish policies and procedures that address GAI data redundancy, includingmodel weights and other system artifacts.|Harmful Bias and Homogenization|
|GV-6.2-006|Establish policies and procedures to test and manage risks related to rollover andfallback technologies for GAI systems, acknowledging that rollover and fallbackmay include manual processing.|Information Integrity|
|GV-6.2-007|Review vendor contracts and avoid arbitrary or capricious termination of criticalGAI technologies or vendor services and non-standard terms that may amplify ordefer liability in unexpected ways and/or contribute to unauthorized datacollection by vendors or third-parties (e.g., secondary data use). Consider: Clearassignment of liability and responsibility for incidents, GAI system changes overtime (e.g., fine-tuning, drift, decay); Request: Notification and disclosure forserious incidents arising from third-party data and systems; Service LevelAgreements (SLAs) in vendor contracts that address incident response, responsetimes, and availability of critical support.|Human-AI Configuration;Information Security; Value Chainand Component Integration|
|AI Actor Tasks: i ii|AI Deployment, Operation and Monitoring, TEVV, Third-party entities||

[pp. 26-27]

MAP 1.1: Intended purposes, potentially beneficial uses, context specific laws, norms and expectations, and prospective settings in which the AI system will be deployed are understood and documented. Considerations include: the specific set or types of users along with their expectations; potential positive and negative impacts of system uses to individuals, communities, organizations, society, and the planet; assumptions and related limitations about AI system purposes, uses, and risks across the development or product AI lifecycle; and related TEVV and system metrics.

|MP-1.1-001|When identifying intended purposes, consider factors such as internal vs.external use, narrow vs. broad application scope, fine-tuning, and varieties ofdata sources (e.g., grounding, retrieval-augmented generation).|Data Privacy; IntellectualProperty|

|MP-1.1-002|Determine and document the expected and acceptable GAI system context ofuse in collaboration with socio-cultural and other domain experts, by assessing:Assumptions and limitations; Direct value to the organization; Intendedoperational environment and observed usage patterns; Potential positive andnegative impacts to individuals, public safety, groups, communities,organizations, democratic institutions, and the physical environment; Socialnorms and expectations.|Harmful Bias and Homogenization|
|MP-1.1-003|Document risk measurement plans to address identified risks. Plans mayinclude, as applicable: Individual and group cognitive biases (e.g., confirmationbias, funding bias, groupthink) for AI Actors involved in the design,implementation, and use of GAI systems; Known past GAI system incidents andfailure modes; In-context use and foreseeable misuse, abuse, and off-label use;Over reliance on quantitative metrics and methodologies without sufficientawareness of their limitations in the context(s) of use; Standard measurementand structured human feedback approaches; Anticipated human-AIconfigurations.|Human-AI Configuration; HarmfulBias and Homogenization;Dangerous, Violent, or HatefulContent|
|MP-1.1-004|Identify and document foreseeable illegal uses or applications of the GAI systemthat surpass organizational risk tolerances.|i iCBRN Information or Capabilities;Dangerous, Violent, or HatefulContent; Obscene, Degrading,and/or Abusive Content|
|AI Actor Tasks:|AI Deployment||

MAP 1.2: Interdisciplinary AI Actors, competencies, skills, and capacities for establishing context reflect demographic diversity and broad domain and user experience expertise, and their participation is documented. Opportunities for interdisciplinary collaboration are prioritized.

[pp. 27-28]

|MP-1.2-001|Establish and empower interdisciplinary teams that reflect a wide range ofcapabilities, competencies, demographic groups, domain expertise, educationalbackgrounds, lived experiences, professions, and skills across the enterprise toinform and conduct risk measurement and management functions.|Human-AI Configuration; HarmfulBias and Homogenization|
|MP-1.2-002|Verify that data or benchmarks used in risk measurement, and users,participants, or subjects involved in structured GAI public feedback exercisesare representative of diverse in-context user populations.|Human-AI Configuration; HarmfulBias and Homogenization|
|AI Actor Tasks:|AI Deployment||

MAP 2.1: The specific tasks and methods used to implement the tasks that the AI system will support are defined (e.g., classifiers, generative models, recommenders).

|MP-2.1-001|Establish known assumptions and practices for determining data origin andcontent lineage, for documentation and evaluation purposes.|Information Integrity|
||Institute test and evaluation for data and content flows within the GAI system,||
|MP-2.1-002|i i lincluding but not limited to, original data sources, data transformations, anddecision-making criteria.|Intellectual Property; Data Privacy|
|AI Actor Tasks:|TEVV||

MAP 2.2: Information about the AI system’s knowledge limits and how system output may be utilized and overseen by humans is documented. Documentation provides sufficient information to assist relevant AI Actors when making decisions and taking subsequent actions.

|MP-2.2-001|Identify and document how the system relies on upstream data sources,including for content provenance, and if it serves as an upstream dependency forother systems.|Information Integrity; Value Chainand Component Integration|
|MP-2.2-002|Observe and analyze how the GAI system interacts with external networks, andidentify any potential for negative externalities, particularly where contentprovenance might be compromised.|Information Integrity|
|AI Actor Tasks:|End Users||

MAP 2.3: Scientific integrity and TEVV considerations are identified and documented, including those related to experimental design, data collection and selection (e.g., availability, representativeness, suitability), system trustworthiness, and construct validation

|MP-2.3-001|Assess the accuracy, quality, reliability, and authenticity of GAI output bycomparing it to a set of known ground truth data and by using a variety ofevaluation methods (e.g., human oversight and automated evaluation, provencryptographic techniques, review of content inputs).|Information Integrity|

[pp. 29-30]

|MP-2.3-002|Review and document accuracy, representativeness, relevance, suitability of dataused at different stages of AI life cycle.|Harmful Bias and Homogenization;Intellectual Property|
|MP-2.3-003|Deploy and document fact-checking techniques to verify the accuracy andveracity of information generated by GAI systems, especially when theinformation comes from multiple (or unknown) sources.|Information Integrity|
|MP-2.3-004|Develop and implement testing techniques to identify GAI produced content (e.g.,synthetic media) that might be indistinguishable from human-generated content.|Information Integrity|
|MP-2.3-005|Implement plans for GAI systems to undergo regular adversarial testing to identifyvulnerabilities and potential manipulation or misuse.|Information Security|

AI Actor Tasks: AI Development, Domain Experts, TEVV

MAP 3.4: Processes for operator and practitioner proficiency with AI system performance and trustworthiness – and relevant technical standards and certifications – are defined, assessed, and documented.

|MP-3.4-001|Evaluate whether GAI operators and end-users can accurately understandcontent lineage and origin.|Human-AI Configuration;Information Integrity|
|MP-3.4-002|Adapt existing training programs to include modules on digital contenttransparency.|Information Integrity|
|MP-3.4-003|Develop certification programs that test proficiency in managing GAI risks andinterpreting content provenance, relevant to specific industry and context.|Information Integrity|
|MP-3.4-004 i i|Delineate human proficiency tests from tests of GAI capabilities.|Human-AI Configuration|
|MP-3.4-005|Implement systems to continually monitor and track the outcomes of human-GAIconfigurations for future refinement and improvements.|Human-AI Configuration;Information Integrity|
|MP-3.4-006|Involve the end-users, practitioners, and operators in GAI system in prototypingand testing activities. Make sure these tests cover various scenarios, such as crisissituations or ethically sensitive contexts.|Human-AI Configuration;Information Integrity; Harmful Biasand Homogenization; Dangerous,Violent, or Hateful Content|

AI Actor Tasks: AI Design, AI Development, Domain Experts, End-Users, Human Factors, Operation and Monitoring

MAP 4.1: Approaches for mapping AI technology and legal risks of its components – including the use of third-party data or software – are in place, followed, and documented, as are risks of infringement of a third-party’s intellectual property or other rights.

[p. 30]

|MP-4.1-001|Conduct periodic monitoring of AI-generated content for privacy risks; address anypossible instances of PII or sensitive data exposure.|Data Privacy|
|MP-4.1-002|Implement processes for responding to potential intellectual property infringementclaims or other rights.|Intellectual Property|
|MP-4.1-003|Connect new GAI policies, procedures, and processes to existing model, data,software development, and IT governance and to legal, compliance, and riskmanagement activities.|Information Security; Data Privacy|
|MP-4.1-004|Document training data curation policies, to the extent possible and according toapplicable laws and policies.|Intellectual Property; Data Privacy;Obscene, Degrading, and/orAbusive Content|
|MP-4.1-005|Establish policies for collection, retention, and minimum quality of data, inconsideration of the following risks: Disclosure of inappropriate CBRN information;Use of Illegal or dangerous content; Offensive cyber capabilities; Training dataimbalances that could give rise to harmful biases; Leak of personally identifiableinformation, including facial likenesses of individuals.|CBRN Information or Capabilities;Intellectual Property; InformationSecurity; Harmful Bias andHomogenization; Dangerous,Violent, or Hateful Content; DataPrivacy|
|MP-4.1-006|Implement policies and practices defining how third-party intellectual property andtraining data will be used, stored, and protected.|Intellectual Property; Value Chainand Component Integration|
|MP-4.1-007|Re-evaluate models that were fine-tuned or enhanced on top of third-partymodels.|Value Chain and ComponentIntegration|
|MP-4.1-008|Re-evaluate risks when adapting GAI models to new domains. Additionally,establish warning systems to determine if a GAI system is being used in a newdomain where previous assumptions (relating to context of use or mapped riskssuch as security, and safety) may no longer hold.|CBRN Information or Capabilities;Intellectual Property; Harmful Biasand Homogenization; Dangerous,Violent, or Hateful Content; DataPrivacy|
|MP-4.1-009|Leverage approaches to detect the presence of PII or sensitive data in generatedoutput text, image, video, or audio.|Data Privacy|

[p. 31]

||Conduct appropriate diligence on training data use to assess intellectual property,i||
|MP-4.1-010|and privacy, risks, including to examine whether use of proprietary or sensitive|Intellectual Property; Data Privacy|
||training data is consistent with applicable laws.||

AI Actor Tasks: Governance and Oversight, Operation and Monitoring, Procurement, Third-party entities

MAP 5.1: Likelihood and magnitude of each identified impact (both potentially beneficial and harmful) based on expected use, past uses of AI systems in similar contexts, public incident reports, feedback from those external to the team that developed or deployed the AI system, or other data are identified and documented.

|MP-5.1-001|Apply TEVV practices for content provenance (e.g., probing a system's syntheticdata generation capabilities for potential misuse or vulnerabilities.|Information Integrity; InformationSecurity|
|MP-5.1-002|Identify potential content provenance harms of GAI, such as misinformation ordisinformation, deepfakes, including NCII, or tampered content. Enumerate andrank risks based on their likelihood and potential impact, and determine how wellprovenance solutions address specific risks and/or harms.|Information Integrity; Dangerous,Violent, or Hateful Content;Obscene, Degrading, and/orAbusive Content|
|MP-5.1-003|Consider disclosing use of GAI to end users in relevant contexts, while consideringthe objective of disclosure, the context of use, the likelihood and magnitude of therisk posed, the audience of the disclosure, as well as the frequency of thedisclosures.|Human-AI Configuration|
|MP-5.1-004|Prioritize GAI structured public feedback processes based on risk assessmentestimates.|Information Integrity; CBRNInformation or Capabilities;Dangerous, Violent, or HatefulContent; Harmful Bias andHomogenization|
|MP-5.1-005|Conduct adversarial role-playing exercises, GAI red-teaming, or chaos testing toidentify anomalous or unforeseen failure modes.|Information Security|
|MP-5.1-006|Profile threats and negative impacts arising from GAI systems interacting with,manipulating, or generating content, and outlining known and potentialvulnerabilities and the likelihood of their occurrence.|Information Security|

AI Actor Tasks: AI Deployment, AI Design, AI Development, AI Impact Assessment, Affected Individuals and Communities, EndUsers, Operation and Monitoring

[p. 32]

MAP 5.2: Practices and personnel for supporting regular engagement with relevant AI Actors and integrating feedback about positive, negative, and unanticipated impacts are in place and documented.

|MP-5.2-001|Determine context-based measures to identify if new impacts are present due tothe GAI system, including regular engagements with downstream AI Actors toidentify and quantify new contexts of unanticipated impacts of GAI systems.|Human-AI Configuration; ValueChain and Component Integration|
|MP-5.2-002|Plan regular engagements with AI Actors responsible for inputs to GAI systems,including third-party data and algorithms, to review and evaluate unanticipatedimpacts.|Human-AI Configuration; ValueChain and Component Integration|
|AI Actor Tasks f iUsers, Human i|: AI Deployment, AI Design, AI Impact Assessment, Affected Individuals and ComiFactors, Operation and Monitoring|f munities, Domain Experts, End-|

MEASURE 1.1: Approaches and metrics for measurement of AI risks enumerated during the MAP function are selected for implementation starting with the most significant AI risks. The risks or trustworthiness characteristics that will not – or cannot – be measured are properly documented.

|MS-1.1-001 ii|Employ methods to trace the origin and modifications of digital content.|Information Integrity|
|MS-1.1-002|Integrate tools designed to analyze content provenance and detect dataanomalies, verify the authenticity of digital signatures, and identify patternsassociated with misinformation or manipulation.|Information Integrity|
|MS-1.1-003|Disaggregate evaluation metrics by demographic factors to identify anydiscrepancies in how content provenance mechanisms work across diversepopulations.|Information Integrity; HarmfulBias and Homogenization|
|MS-1.1-004|Develop a suite of metrics to evaluate structured public feedback exercisesinformed by representative AI Actors.|Human-AI Configuration; HarmfulBias and Homogenization; CBRNInformation or Capabilities|
|MS-1.1-005|Evaluate novel methods and technologies for the measurement of GAI-relatedrisks including in content provenance, offensive cyber, and CBRN, whilemaintaining the models’ ability to produce valid, reliable, and factually accurateoutputs.|Information Integrity; CBRNInformation or Capabilities;Obscene, Degrading, and/orAbusive Content|

[p. 33]

|MS-1.1-006|Implement continuous monitoring of GAI system impacts to identify whether GAIoutputs are equitable across various sub-populations. Seek active and directfeedback from affected communities via structured feedback mechanisms or red-teaming to monitor and improve outputs.|Harmful Bias and Homogenization|
|MS-1.1-007|Evaluate the quality and integrity of data used in training and the provenance ofAI-generated content, for example by employing techniques like chaosengineering and seeking stakeholder feedback.|Information Integrity|
|MS-1.1-008|Define use cases, contexts of use, capabilities, and negative impacts wherestructured human feedback exercises, e.g., GAI red-teaming, would be mostbeneficial for GAI risk measurement and management based on the context ofuse.|Harmful Bias andHomogenization; CBRNInformation or Capabilities|
|MS-1.1-009|Track and document risks or opportunities related to all GAI risks that cannot bemeasured quantitatively, including explanations as to why some risks cannot bemeasured (e.g., due to technological limitations, resource constraints, ortrustworthy considerations). Include unmeasured risks in marginal risks.|Information Integrity|
|AI Actor Tasks|: AI Development, Domain Experts, TEVV||

MEASURE 1.3: Internal experts who did not serve as front-line developers for the system and/or independent assessors are involved in regular assessments and updates. Domain experts, users, AI Actors external to the team that developed or deployed the AI system, and affected communities are consulted in support of assessments as necessary per organizational risk tolerance.

|MS-1.3-001|Define relevant groups of interest (e.g., demographic groups, subject matterexperts, experience with GAI technology) within the context of use as part ofplans for gathering structured public feedback.|Human-AI Configuration; HarmfulBias and Homogenization; CBRNInformation or Capabilities|
|MS-1.3-002|Engage in internal and external evaluations, GAI red-teaming, impactassessments, or other structured human feedback exercises in consultationwith representative AI Actors with expertise and familiarity in the context ofuse, and/or who are representative of the populations associated with thecontext of use.|Human-AI Configuration; HarmfulBias and Homogenization; CBRNInformation or Capabilities|
|MS-1.3-003|Verify those conducting structured human feedback exercises are not directlyinvolved in system development tasks for the same GAI model.|Human-AI Configuration; DataPrivacy|

[pp. 33-34]

AI Actor Tasks: AI Deployment, AI Development, AI Impact Assessment, Affected Individuals and Communities, Domain Experts, End-Users, Operation and Monitoring, TEVV

MEASURE 2.2: Evaluations involving human subjects meet applicable requirements (including human subject protection) and are representative of the relevant population.

|MS-2.2-001|Assess and manage statistical biases related to GAI content provenance throughtechniques such as re-sampling, re-weighting, or adversarial training.|Information Integrity; InformationSecurity; Harmful Bias andHomogenization|
|MS-2.2-002|Document how content provenance data is tracked and how that data interactswith privacy and security. Consider: Anonymizing data to protect the privacy ofhuman subjects; Leveraging privacy output filters; Removing any personallyidentifiable information (PII) to prevent potential harm or misuse.|Data Privacy; Human AIConfiguration; InformationIntegrity; Information Security;Dangerous, Violent, or HatefulContent|
|MS-2.2-003|Provide human subjects with options to withdraw participation or revoke theirconsent for present or future use of their data in GAI applications.|Data Privacy; Human-AIConfiguration; InformationIntegrity|
|MS-2.2-004|Use techniques such as anonymization, differential privacy or other privacy-enhancing technologies to minimize the risks associated with linking AI-generatedcontent back to individual human subjects.|Data Privacy; Human-AIConfiguration|
|AI Actor Task|s: AI Development, Human Factors, TEVV||

MEASURE 2.3: AI system performance or assurance criteria are measured qualitatively or quantitatively and demonstrated for conditions similar to deployment setting(s). Measures are documented.

|MS-2.3-001|Consider baseline model performance on suites of benchmarks when selecting amodel for fine tuning or enhancement with retrieval-augmented generation.|Information Security;Confabulation|
|MS-2.3-002 i|Evaluate claims of model capabilities using empirically validated methods.|Confabulation; InformationSecurity|
|MS-2.3-003|Share results of pre-deployment testing with relevant GAI Actors, such as thosewith system release approval authority.|Human-AI Configuration|

[pp. 35-36]

|MS-2.3-004|Utilize a purpose-built testing environment such as NIST Dioptra to empiricallyevaluate GAI trustworthy characteristics.|CBRN Information or Capabilities;Data Privacy; Confabulation;Information Integrity; InformationSecurity; Dangerous, Violent, orHateful Content; Harmful Bias andHomogenization|
|AI Actor Tasks|: AI Deployment, TEVV||

MEASURE 2.5: The AI system to be deployed is demonstrated to be valid and reliable. Limitations of the generalizability beyond the conditions under which the technology was developed are documented.

|Action ID|Suggested Action|Risks|
|MS-2.5-001|Avoid extrapolating GAI system performance or capabilities from narrow, non-systematic, and anecdotal assessments.|Human-AI Configuration;Confabulation|
|MS-2.5-002|Document the extent to which human domain knowledge is employed toimprove GAI system performance, via, e.g., RLHF, fine-tuning, retrieval-augmented generation, content moderation, business rules.|Human-AI Configuration|
|MS-2.5-003|Review and verify sources and citations in GAI system outputs during pre-deployment risk measurement and ongoing monitoring activities.|Confabulation|
|MS-2.5-004|Track and document instances of anthropomorphization (e.g., human images,mentions of human feelings, cyborg imagery or motifs) in GAI system interfaces.|Human-AI Configuration|
|MS-2.5-005|Verify GAI system training data and TEVV data provenance, and that fine-tuningor retrieval-augmented generation data is grounded.|Information Integrity|
|MS-2.5-006|Regularly review security and safety guardrails, especially if the GAI system isbeing operated in novel circumstances. This includes reviewing reasons why theGAI system was initially assessed as being safe to deploy.|Information Security; Dangerous,Violent, or Hateful Content|
|AI Actor Tasks|: Domain Experts, TEVV||

MEASURE 2.6: The AI system is evaluated regularly for safety risks – as identified in the MAP function. The AI system to be deployed is demonstrated to be safe, its residual negative risk does not exceed the risk tolerance, and it can fail safely, particularly if made to operate beyond its knowledge limits. Safety metrics reflect system reliability and robustness, real-time monitoring, and response times for AI system failures.

[pp. 36-37]

|MS-2.6-001|Assess adverse impacts, including health and wellbeing impacts for value chainor other AI Actors that are exposed to sexually explicit, offensive, or violentinformation during GAI training and maintenance.|Human-AI Configuration; Obscene,Degrading, and/or AbusiveContent; Value Chain andComponent Integration;Dangerous, Violent, or HatefulContent|
|MS-2.6-002|Assess existence or levels of harmful bias, intellectual property infringement,data privacy violations, obscenity, extremism, violence, or CBRN information insystem training data.|Data Privacy; Intellectual Property;Obscene, Degrading, and/orAbusive Content; Harmful Bias andHomogenization; Dangerous,Violent, or Hateful Content; CBRNInformation or Capabilities|
|MS-2.6-003|Re-evaluate safety features of fine-tuned models when the negative risk exceedsorganizational risk tolerance.|Dangerous, Violent, or HatefulContent|
|MS-2.6-004|Review GAI system outputs for validity and safety: Review generated code toassess risks that may arise from unreliable downstream decision-making.|Value Chain and ComponentIntegration; Dangerous, Violent, orHateful Content|
|MS-2.6-005|Verify that GAI system architecture can monitor outputs and performance, andhandle, recover from, and repair errors when security anomalies, threats andimpacts are detected.|Confabulation; InformationIntegrity; Information Security|
|MS-2.6-006|Verify that systems properly handle queries that may give rise to inappropriate,malicious, or illegal usage, including facilitating manipulation, extortion, targetedimpersonation, cyber-attacks, and weapons creation.|i i iCBRN Information or Capabilities;Information Security|
|MS-2.6-007|Regularly evaluate GAI system vulnerabilities to possible circumvention of safetymeasures.|CBRN Information or Capabilities;Information Security|

AI Actor Tasks: AI Deployment, AI Impact Assessment, Domain Experts, Operation and Monitoring, TEVV

MEASURE 2.7: AI system security and resilience – as identified in the MAP function – are evaluated and documented.


---

[previous part](text-002.md) | [source overview](overview.md) | [next part](text-004.md)

[^original]: NIST, "Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile" (2024-07-26). https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence
