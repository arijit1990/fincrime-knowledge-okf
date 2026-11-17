---
type: Source Text
title: 'Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile - part 2 of 6 (pp. 13-24)'
description: 'Verbatim extracted text, pp. 13-24: NIST Trustworthy and Responsible AI NIST AI 600-1 > 2.7. Human-AI Configuration; NIST Trustworthy and Responsible AI NIST AI 600-1 > 2.8. Information Integrity; NIST Trustworthy and Responsible AI NIST AI 600-1 > 2.9. Information Security; and 4 more sections'
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
part: 2
parts_total: 6
content_mode: full_text
generated:
  by: process:fincrime-kb-build
  at: '2026-11-17T07:21:49Z'
verified:
- by: process:kb-validate/verbatim-coverage
  at: '2026-11-17T07:21:49Z'
sources:
- id: original
  resource: https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence
  title: 'Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile'
  author: org:nist
  last_modified: '2026-04-08T00:00:00Z'
---

# Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile

[previous part](text-001.md) | [source overview](overview.md) | [next part](text-003.md)

> Verbatim text extracted from the original (NIST, 2024-07-26), part 2 of 6, pp. 13-24. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **industry practice**.[^original]

## NIST Trustworthy and Responsible AI NIST AI 600-1


### 2.7. Human-AI Configuration


[p. 13]

GAI system use can involve varying risks of misconfigurations and poor interactions between a system and a human who is interacting with it. Humans bring their unique perspectives, experiences, or domainspecific expertise to interactions with AI systems but may not have detailed knowledge of AI systems and how they work. As a result, human experts may be unnecessarily “averse” to GAI systems, and thus deprive themselves or others of GAI’s beneficial uses.

Conversely, due to the complexity and increasing reliability of GAI technology, over time, humans may over-rely on GAI systems or may unjustifiably perceive GAI content to be of higher quality than that produced by other sources. This phenomenon is an example of automation bias, or excessive deference to automated systems. Automation bias can exacerbate other risks of GAI, such as risks of confabulation or risks of bias or homogenization.

There may also be concerns about emotional entanglement between humans and GAI systems, which could lead to negative psychological impacts.

Trustworthy AI Characteristics: Accountable and Transparent, Explainable and Interpretable, Fair with Harmful Bias Managed, Privacy Enhanced, Safe, Valid and Reliable

### 2.8. Information Integrity


[pp. 13-14]

Information integrity describes the “spectrum of information and associated patterns of its creation, exchange, and consumption in society.” High-integrity information can be trusted; “distinguishes fact from fiction, opinion, and inference; acknowledges uncertainties; and is transparent about its level of vetting. This information can be linked to the original source(s) with appropriate evidence. High-integrity information is also accurate and reliable, can be verified and authenticated, has a clear chain of custody, and creates reasonable expectations about when its validity may expire.”11

> 11 This definition of information integrity is derived from the 2022 White House Roadmap for Researchers on Priorities Related to Information Integrity Research and Development.

GAI systems can ease the unintentional production or dissemination of false, inaccurate, or misleading content (misinformation) at scale, particularly if the content stems from confabulations.

GAI systems can also ease the deliberate production or dissemination of false or misleading information (disinformation) at scale, where an actor has the explicit intent to deceive or cause harm to others. Even very subtle changes to text or images can manipulate human and machine perception.

Similarly, GAI systems could enable a higher degree of sophistication for malicious actors to produce disinformation that is targeted towards specific demographics. Current and emerging multimodal models make it possible to generate both text-based disinformation and highly realistic “deepfakes” – that is, synthetic audiovisual content and photorealistic images.12 Additional disinformation threats could be enabled by future GAI models trained on new data modalities.

Disinformation and misinformation – both of which may be facilitated by GAI – may erode public trust in true or valid evidence and information, with downstream effects. For example, a synthetic image of a Pentagon blast went viral and briefly caused a drop in the stock market. Generative AI models can also assist malicious actors in creating compelling imagery and propaganda to support disinformation campaigns, which may not be photorealistic, but could enable these campaigns to gain more reach and engagement on social media platforms. Additionally, generative AI models can assist malicious actors in creating fraudulent content intended to impersonate others.

Trustworthy AI Characteristics: Accountable and Transparent, Safe, Valid and Reliable, Interpretable and Explainable

### 2.9. Information Security


[pp. 14-15]

Information security for computer systems and data is a mature field with widely accepted and standardized practices for offensive and defensive cyber capabilities. GAI-based systems present two primary information security risks: GAI could potentially discover or enable new cybersecurity risks by lowering the barriers for or easing automated exercise of offensive capabilities; simultaneously, it expands the available attack surface, as GAI itself is vulnerable to attacks like prompt injection or data poisoning.

Offensive cyber capabilities advanced by GAI systems may augment cybersecurity attacks such as hacking, malware, and phishing. Reports have indicated that LLMs are already able to discover some vulnerabilities in systems (hardware, software, data) and write code to exploit them. Sophisticated threat actors might further these risks by developing GAI-powered security co-pilots for use in several parts of the attack chain, including informing attackers on how to proactively evade threat detection and escalate privileges after gaining system access.

Information security for GAI models and systems also includes maintaining availability of the GAI system and the integrity and (when applicable) the confidentiality of the GAI code, training data, and model weights. To identify and secure potential attack points in AI systems or specific components of the AI

> 12 See also https://doi.org/10.6028/NIST.AI.100-4, to be published.

value chain (e.g., data inputs, processing, GAI training, or deployment environments), conventional cybersecurity practices may need to adapt or evolve.

For instance, prompt injection involves modifying what input is provided to a GAI system so that it behaves in unintended ways. In direct prompt injections, attackers might craft malicious prompts and input them directly to a GAI system, with a variety of downstream negative consequences to interconnected systems. Indirect prompt injection attacks occur when adversaries remotely (i.e., without a direct interface) exploit LLM-integrated applications by injecting prompts into data likely to be retrieved. Security researchers have already demonstrated how indirect prompt injections can exploit vulnerabilities by stealing proprietary data or running malicious code remotely on a machine. Merely querying a closed production model can elicit previously undisclosed information about that model.

Another cybersecurity risk to GAI is data poisoning, in which an adversary compromises a training dataset used by a model to manipulate its outputs or operation. Malicious tampering with data or parts of the model could exacerbate risks associated with GAI system outputs.

Trustworthy AI Characteristics: Privacy Enhanced, Safe, Secure and Resilient, Valid and Reliable

### 2.10. Intellectual Property


[p. 15]

Intellectual property risks from GAI systems may arise where the use of copyrighted works is not a fair use under the fair use doctrine. If a GAI system’s training data included copyrighted material, GAI outputs displaying instances of training data memorization (see Data Privacy above) could infringe on copyright.

How GAI relates to copyright, including the status of generated content that is similar to but does not strictly copy work protected by copyright, is currently being debated in legal fora. Similar discussions are taking place regarding the use or emulation of personal identity, likeness, or voice without permission. Trustworthy AI Characteristics: Accountable and Transparent, Fair with Harmful Bias Managed, Privacy Enhanced

### 2.11. Obscene, Degrading, and/or Abusive Content


[pp. 15-16]

GAI can ease the production of and access to illegal non-consensual intimate imagery (NCII) of adults, and/or child sexual abuse material (CSAM). GAI-generated obscene, abusive or degrading content can create privacy, psychological and emotional, and even physical harms, and in some cases may be illegal.

Generated explicit or obscene AI content may include highly realistic “deepfakes” of real individuals, including children. The spread of this kind of material can have downstream negative consequences: in the context of CSAM, even if the generated images do not resemble specific individuals, the prevalence of such images can divert time and resources from efforts to find real-world victims. Outside of CSAM, the creation and spread of NCII disproportionately impacts women and sexual minorities, and can have subsequent negative consequences including decline in overall mental health, substance abuse, and even suicidal thoughts.

Data used for training GAI models may unintentionally include CSAM and NCII. A recent report noted that several commonly used GAI training datasets were found to contain hundreds of known images of

CSAM. Even when trained on “clean” data, increasingly capable GAI models can synthesize or produce synthetic NCII and CSAM. Websites, mobile apps, and custom-built models that generate synthetic NCII have moved from niche internet forums to mainstream, automated, and scaled online businesses.

Trustworthy AI Characteristics: Fair with Harmful Bias Managed, Safe, Privacy Enhanced

### 2.12. Value Chain and Component Integration


[p. 16]

GAI value chains involve many third-party components such as procured datasets, pre-trained models, and software libraries. These components might be improperly obtained or not properly vetted, leading to diminished transparency or accountability for downstream users. While this is a risk for traditional AI systems and some other digital technologies, the risk is exacerbated for GAI due to the scale of the training data, which may be too large for humans to vet; the difficulty of training foundation models, which leads to extensive reuse of limited numbers of models; and the extent to which GAI may be integrated into other devices and services. As GAI systems often involve many distinct third-party components and data sources, it may be difficult to attribute issues in a system’s behavior to any one of these sources.

Errors in third-party GAI components can also have downstream impacts on accuracy and robustness. For example, test datasets commonly used to benchmark or validate models can contain label errors. Inaccuracies in these labels can impact the “stability” or robustness of these benchmarks, which many GAI practitioners consider during the model selection process.

Trustworthy AI Characteristics: Accountable and Transparent, Explainable and Interpretable, Fair with Harmful Bias Managed, Privacy Enhanced, Safe, Secure and Resilient, Valid and Reliable

### 3. Suggested Actions to Manage GAI Risks


[pp. 16-17]

The following suggested actions target risks unique to or exacerbated by GAI.

In addition to the suggested actions below, AI risk management activities and actions set forth in the AI RMF 1.0 and Playbook are already applicable for managing GAI risks. Organizations are encouraged to apply the activities suggested in the AI RMF and its Playbook when managing the risk of GAI systems.

Implementation of the suggested actions will vary depending on the type of risk, characteristics of GAI systems, stage of the GAI lifecycle, and relevant AI actors involved.

Suggested actions to manage GAI risks can be found in the tables below:

- The suggested actions are organized by relevant AI RMF subcategories to streamline these activities alongside implementation of the AI RMF.

- Not every subcategory of the AI RMF is included in this document.13 Suggested actions are listed for only some subcategories.

> 13 As this document was focused on the GAI PWG efforts and primary considerations (see Appendix A), AI RMF subcategories not addressed here may be added later.

- Not every suggested action applies to every AI Actor14 or is relevant to every AI Actor Task. For example, suggested actions relevant to GAI developers may not be relevant to GAI deployers. The applicability of suggested actions to relevant AI actors should be determined based on organizational considerations and their unique uses of GAI systems.

Each table of suggested actions includes:

- Action ID: Each Action ID corresponds to the relevant AI RMF function and subcategory (e.g., GV1.1-001 corresponds to the first suggested action for Govern 1.1, GV-1.1-002 corresponds to the second suggested action for Govern 1.1). AI RMF functions are tagged as follows: GV = Govern; MP = Map; MS = Measure; MG = Manage.

- Suggested Action: Steps an organization or AI actor can take to manage GAI risks.

- GAI Risks: Tags linking suggested actions with relevant GAI risks.

- AI Actor Tasks: Pertinent AI Actor Tasks for each subcategory. Not every AI Actor Task listed will apply to every suggested action in the subcategory (i.e., some apply to AI development and others apply to AI deployment).

The tables below begin with the AI RMF subcategory, shaded in blue, followed by suggested actions.

GOVERN 1.1: Legal and regulatory requirements involving AI are understood, managed, and documented.

|GV-1.1-001|Align GAI development and use with applicable laws and regulations, includingthose related to data privacy, copyright and intellectual property law.|Data Privacy; Harmful Bias andHomogenization; IntellectualProperty|

AI Actor Tasks: Governance and Oversight

[pp. 17-18]

> 14 AI Actors are defined by the OECD as “those who play an active role in the AI system lifecycle, including organizations and individuals that deploy or operate AI.” See Appendix A of the AI RMF for additional descriptions of AI Actors and AI Actor Tasks.

GOVERN 1.2: The characteristics of trustworthy AI are integrated into organizational policies, processes, procedures, and practices.

|GV-1.2-001|Establish transparency policies and processes for documenting the origin andhistory of training data and generated data for GAI applications to advance digitalcontent transparency, while balancing the proprietary nature of trainingapproaches.|Data Privacy; InformationIntegrity; Intellectual Property|
|GV-1.2-002|Establish policies to evaluate risk-relevant capabilities of GAI and robustness ofsafety measures, both prior to deployment and on an ongoing basis, throughinternal and external evaluations.|CBRN Information or Capabilities;Information Security|

AI Actor Tasks: Governance and Oversight

GOVERN 1.3: Processes, procedures, and practices are in place to determine the needed level of risk management activities based on the organization’s risk tolerance.

[p. 18]

|GV-1.3-001|Consider the following factors when updating or defining risk tiers for GAI: Abusesand impacts to information integrity; Dependencies between GAI and other IT ordata systems; Harm to fundamental rights or public safety; Presentation ofobscene, objectionable, offensive, discriminatory, invalid or untruthful output;Psychological impacts to humans (e.g., anthropomorphization, algorithmicaversion, emotional entanglement); Possibility for malicious use; Whether thesystem introduces significant new security vulnerabilities; Anticipated systemimpact on some groups compared to others; Unreliable decision makingcapabilities, validity, adaptability, and variability of GAI system performance overtime.|Information Integrity; Obscene,Degrading, and/or AbusiveContent; Value Chain andComponent Integration; HarmfulBias and Homogenization;Dangerous, Violent, or HatefulContent; CBRN Information orCapabilities|
|GV-1.3-002|Establish minimum thresholds for performance or assurance criteria and review aspart of deployment approval (“go/”no-go”) policies, procedures, and processes,with reviewed processes and approval thresholds reflecting measurement of GAIcapabilities and risks.|CBRN Information or Capabilities;Confabulation; Dangerous,Violent, or Hateful Content|
|GV-1.3-003|Establish a test plan and response policy, before developing highly capable models,to periodically evaluate whether the model may misuse CBRN information orcapabilities and/or offensive cyber capabilities.|CBRN Information or Capabilities;Information Security|

[pp. 19-20]

|GV-1.3-004|Obtain input from stakeholder communities to identify unacceptable use, inaccordance with activities in the AI RMF Map function.|CBRN Information or Capabilities;Obscene, Degrading, and/orAbusive Content; Harmful Biasand Homogenization; Dangerous,Violent, or Hateful Content|
|GV-1.3-005|Maintain an updated hierarchy of identified and expected GAI risks connected tocontexts of GAI model advancement and use, potentially including specialized risklevels for GAI systems that address issues such as model collapse and algorithmicmonoculture.|Harmful Bias and Homogenization|
|GV-1.3-006|Reevaluate organizational risk tolerances to account for unacceptable negative risk(such as where significant negative impacts are imminent, severe harms areactually occurring, or large-scale risks could occur); and broad GAI negative risks,including: Immature safety or risk cultures related to AI and GAI design,development and deployment, public information integrity risks, including impactson democratic processes, unknown long-term performance characteristics of GAI.|Information Integrity; Dangerous,Violent, or Hateful Content; CBRNInformation or Capabilities|
|GV-1.3-007|Devise a plan to halt development or deployment of a GAI system that posesunacceptable negative risk.|CBRN Information and Capability;Information Security; InformationIntegrity|
|AI Actor Task|s: Governance and Oversight||

GOVERN 1.4: The risk management process and its outcomes are established through transparent policies, procedures, and other controls based on organizational risk priorities.

|GV-1.4-001|Establish policies and mechanisms to prevent GAI systems from generatingCSAM, NCII or content that violates the law.|Obscene, Degrading, and/orAbusive Content; Harmful Biasand Homogenization;Dangerous, Violent, or HatefulContent|
|GV-1.4-002|Establish transparent acceptable use policies for GAI that address illegal use orapplications of GAI.|CBRN Information orCapabilities; Obscene,Degrading, and/or AbusiveContent; Data Privacy; CivilRights violations|
|AI Actor Tas|ks: AI Development, AI Deployment, Governance and Oversight||

GOVERN 1.5: Ongoing monitoring and periodic review of the risk management process and its outcomes are planned, and organizational roles and responsibilities are clearly defined, including determining the frequency of periodic review.

[pp. 20-21]

|GV-1.5-001|Define organizational responsibilities for periodic review of content provenanceand incident monitoring for GAI systems.|Information Integrity|
|GV-1.5-002|Establish organizational policies and procedures for after action reviews of GAIsystem incident response and incident disclosures, to identify gaps; Updateincident response and incident disclosure processes as required.|Human-AI Configuration;Information Security|
|GV-1.5-003|Maintain a document retention policy to keep history for test, evaluation,validation, and verification (TEVV), and digital content transparency methods forGAI.|Information Integrity; IntellectualProperty|
|AI Actor Task i|s: Governance and Oversight, Operation and Monitoring||

GOVERN 1.6: Mechanisms are in place to inventory AI systems and are resourced according to organizational risk priorities.

|GV-1.6-001|Enumerate organizational GAI systems for incorporation into AI system inventoryand adjust AI system inventory requirements to account for GAI risks.|Information Security|
|GV-1.6-002|Define any inventory exemptions in organizational policies for GAI systemsembedded into application software.|Value Chain and ComponentIntegration|
|GV-1.6-003|In addition to general model, governance, and risk information, consider thefollowing items in GAI system inventory entries: Data provenance information(e.g., source, signatures, versioning, watermarks); Known issues reported frominternal bug tracking or external information sharing resources (e.g., AI incidentdatabase,AVID,CVE,NVD, or OECD AI incident monitor); Human oversight rolesand responsibilities; Special rights and considerations for intellectual property,licensed works, or personal, privileged, proprietary or sensitive data; Underlyingfoundation models, versions of underlying models, and access modes.|Data Privacy; Human-AIConfiguration; InformationIntegrity; Intellectual Property;Value Chain and ComponentIntegration|
|AI Actor Tasks|: Governance and Oversight||

GOVERN 1.7: Processes and procedures are in place for decommissioning and phasing out AI systems safely and in a manner that does not increase risks or decrease the organization’s trustworthiness.

[pp. 21-22]

|GV-1.7-001|Protocols are put in place to ensure GAI systems are able to be deactivated whennecessary.|Information Security; Value Chainand Component Integration|
|GV-1.7-002|Consider the following factors when decommissioning GAI systems: Dataretention requirements; Data security, e.g., containment, protocols, Data leakageafter decommissioning; Dependencies between upstream, downstream, or otherdata, internet of things (IOT) or AI systems; Use of open-source data or models;Users’ emotional entanglement with GAI functions.|Human-AI Configuration;Information Security; Value Chainand Component Integration|
|AI Actor Tasks i|: AI Deployment, Operation and Monitoring||

GOVERN 2.1: Roles and responsibilities and lines of communication related to mapping, measuring, and managing AI risks are documented and are clear to individuals and teams throughout the organization.

|GV-2.1-001|Establish organizational roles, policies, and procedures for communicating GAIincidents and performance to AI Actors and downstream stakeholders (includingthose potentially impacted), via community or official resources (e.g., AI incidentdatabase,AVID,CVE,NVD, or OECD AI incident monitor).|Human-AI Configuration; ValueChain and Component Integration|
|GV-2.1-002|Establish procedures to engage teams for GAI system incident response withdiverse composition and responsibilities based on the particular incident type.|Harmful Bias and Homogenization|
|GV-2.1-003|Establish processes to verify the AI Actors conducting GAI incident response tasksdemonstrate and maintain the appropriate skills and training.|Human-AI Configuration|
|GV-2.1-004|When systems may raise national security risks, involve national securityprofessionals in mapping, measuring, and managing those risks.|CBRN Information or Capabilities;Dangerous, Violent, or HatefulContent; Information Security|
|GV-2.1-005|Create mechanisms to provide protections for whistleblowers who report, basedon reasonable belief, when the organization violates relevant laws or poses aspecific and empirically well-substantiated negative risk to public safety (or hasalready caused harm).|CBRN Information or Capabilities;Dangerous, Violent, or HatefulContent|
|AI Actor Tasks|: Governance and Oversight||

GOVERN 3.2: Policies and procedures are in place to define and differentiate roles and responsibilities for human-AI configurations and oversight of AI systems.

[pp. 22-23]

|GV-3.2-001|Policies are in place to bolster oversight of GAI systems with independentevaluations or assessments of GAI models or systems where the type androbustness of evaluations are proportional to the identified risks.|CBRN Information or Capabilities;Harmful Bias and Homogenization|
|GV-3.2-002|Consider adjustment of organizational roles and components across lifecyclestages of large or complex GAI systems, including: Test and evaluation, validation,and red-teaming of GAI systems; GAI content moderation; GAI systemdevelopment and engineering; Increased accessibility of GAI tools, interfaces, andsystems, Incident response and containment.|Human-AI Configuration;Information Security; Harmful Biasand Homogenization|
|GV-3.2-003|Define acceptable use policies for GAI interfaces, modalities, and human-AIconfigurations (i.e., for chatbots and decision-making tasks), including criteria forthe kinds of queries GAI applications should refuse to respond to.|Human-AI Configuration|
|GV-3.2-004|Establish policies for user feedback mechanisms for GAI systems which includethorough instructions and any mechanisms for recourse.|Human-AI Configuration|
|GV-3.2-005|Engage in threat modeling to anticipate potential risks from GAI systems.|CBRN Information or Capabilities;Information Security|
|AI Actors: AI D|esign||

GOVERN 4.1: Organizational policies and practices are in place to foster a critical thinking and safety-first mindset in the design, development, deployment, and uses of AI systems to minimize potential negative impacts.

|GV-4.1-001|Establish policies and procedures that address continual improvement processesfor GAI risk measurement. Address general risks associated with a lack ofexplainability and transparency in GAI systems by using ample documentation andtechniques such as: application of gradient-based attributions, occlusion/termreduction, counterfactual prompts and prompt engineering, and analysis ofembeddings; Assess and update risk measurement approaches at regularcadences.|Confabulation|
|GV-4.1-002|Establish policies, procedures, and processes detailing risk measurement incontext of use with standardized measurement protocols and structured publicfeedback exercises such as AI red-teaming or independent external evaluations.|CBRN Information and Capability;Value Chain and ComponentIntegration|

|GV-4.1-003|Establish policies, procedures, and processes for oversight functions (e.g., seniorleadership, legal, compliance, including internal evaluation) across the GAIlifecycle, from problem formulation and supply chains to system decommission.|Value Chain and ComponentIntegration|

[pp. 23-24]

AI Actor Tasks: AI Deployment, AI Design, AI Development, Operation and Monitoring

GOVERN 4.2: Organizational teams document the risks and potential impacts of the AI technology they design, develop, deploy, evaluate, and use, and they communicate about the impacts more broadly.

|GV-4.2-001|Establish terms of use and terms of service for GAI systems.|Intellectual Property; Dangerous,Violent, or Hateful Content;Obscene, Degrading, and/orAbusive Content|
|GV-4.2-002|Include relevant AI Actors in the GAI system risk identification process.|Human-AI Configuration|
|GV-4.2-003|Verify that downstream GAI system impacts (such as the use of third-partyplugins) are included in the impact documentation process.|Value Chain and ComponentIntegration|
|AI Actor Tasks i|: AI Deployment, AI Design, AI Development, Operation and Monitoring||

GOVERN 4.3: Organizational practices are in place to enable AI testing, identification of incidents, and information sharing.

|GV4.3--001|Establish policies for measuring the effectiveness of employed contentprovenance methodologies (e.g., cryptography, watermarking, steganography,etc.)|Information Integrity|
|GV-4.3-002|Establish organizational practices to identify the minimum set of criterianecessary for GAI system incident reporting such as: System ID (auto-generatedmost likely), Title, Reporter, System/Source, Data Reported, Date of Incident,Description, Impact(s), Stakeholder(s) Impacted.|Information Security|

|GV-4.3-003|Verify information sharing and feedback mechanisms among individuals andorganizations regarding any negative impact from GAI systems.|Information Integrity; DataPrivacy|
|AI Actor Task f i|s: AI Impact Assessment, Affected Individuals and Communities, Governance an|f i d Oversight|

GOVERN 5.1: Organizational policies and practices are in place to collect, consider, prioritize, and integrate feedback from those external to the team that developed or deployed the AI system regarding the potential individual and societal impacts related to AI risks.

|GV-5.1-001|Allocate time and resources for outreach, feedback, and recourse processes in GAIsystem development.|iHuman-AI Configuration; HarmfulBias and Homogenization|
|GV-5.1-002|Document interactions with GAI systems to users prior to interactive activities,particularly in contexts involving more significant risks.|Human-AI Configuration;Confabulation|

AI Actor Tasks: AI Design, AI Impact Assessment, Affected Individuals and Communities, Governance and Oversight

[p. 24]

GOVERN 6.1: Policies and procedures are in place that address AI risks associated with third-party entities, including risks of infringement of a third-party’s intellectual property or other rights.

|GV-6.1-001|Categorize different types of GAI content with associated third-party rights (e.g.,copyright, intellectual property, data privacy).|Data Privacy; IntellectualProperty; Value Chain andComponent Integration|
|GV-6.1-002|Conduct joint educational activities and events in collaboration with third partiesto promote best practices for managing GAI risks.|Value Chain and ComponentIntegration|
|GV-6.1-003|Develop and validate approaches for measuring the success of contentprovenance management efforts with third parties (e.g., incidents detected andresponse times).|Information Integrity; Value Chainand Component Integration|
|GV-6.1-004|Draft and maintain well-defined contracts and service level agreements (SLAs)that specify content ownership, usage rights, quality standards, securityrequirements, and content provenance expectations for GAI systems.|Information Integrity; InformationSecurity; Intellectual Property|


---

[previous part](text-001.md) | [source overview](overview.md) | [next part](text-003.md)

[^original]: NIST, "Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile" (2024-07-26). https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence
