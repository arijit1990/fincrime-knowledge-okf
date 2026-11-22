---
type: Source Text
title: NIST AI RMF Playbook - part 1 of 12 (pp. 2-17)
description: 'Verbatim extracted text, pp. 2-17: AI RMF AI RMF PLAYBOOK PLAYBOOK; FORWARD; GOVERN'
resource: https://airc.nist.gov/airmf-resources/playbook/
tags:
- industry_practice
- model_governance
- model_monitoring
- responsible_ai
- standard
- us
status: stable
source_id: nist-nist-ai-rmf-playbook
issuer: nist
issuer_name: NIST
jurisdictions:
- US
tier: 2
instrument_type: standard
normative_force: industry_practice
publication_date: '2024-08-02'
legal_status: current
part: 1
parts_total: 12
content_mode: full_text
generated:
  by: process:fincrime-kb-build
  at: '2026-11-22T04:42:14Z'
verified:
- by: process:kb-validate/verbatim-coverage
  at: '2026-11-22T04:42:14Z'
sources:
- id: original
  resource: https://airc.nist.gov/airmf-resources/playbook/
  title: NIST AI RMF Playbook
  author: org:nist
  last_modified: '2024-08-02T00:00:00Z'
---

# NIST AI RMF Playbook

[source overview](overview.md) | [next part](text-002.md)

> Verbatim text extracted from the original (NIST, 2024-08-02), part 1 of 12, pp. 2-17. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **industry practice**.[^original]

## AI RMF AI RMF PLAYBOOK PLAYBOOK


[p. 2]

Table of Contents

GOVERN ........................................................................................................................................................................... 4

GOVERN 1.1 .....................................................................................................................................................................................4 GOVERN 1.2 .....................................................................................................................................................................................5 GOVERN 1.3 .....................................................................................................................................................................................7 GOVERN 1.4 .....................................................................................................................................................................................9 GOVERN 1.5 .................................................................................................................................................................................. 11 GOVERN 1.6 .................................................................................................................................................................................. 12 GOVERN 1.7 .................................................................................................................................................................................. 13 GOVERN 2.1 .................................................................................................................................................................................. 15 GOVERN 2.2 .................................................................................................................................................................................. 17 GOVERN 2.3 .................................................................................................................................................................................. 18 GOVERN 3.1 .................................................................................................................................................................................. 19 GOVERN 3.2 .................................................................................................................................................................................. 21 GOVERN 4.1 .................................................................................................................................................................................. 23 GOVERN 4.2 .................................................................................................................................................................................. 24 GOVERN 4.3 .................................................................................................................................................................................. 27 GOVERN 5.1 .................................................................................................................................................................................. 28 GOVERN 5.2 .................................................................................................................................................................................. 30 GOVERN 6.1 .................................................................................................................................................................................. 32 GOVERN 6.2 .................................................................................................................................................................................. 33

MANAGE........................................................................................................................................................................ 35

MANAGE 1.1 ................................................................................................................................................................................. 35 MANAGE 1.2 ................................................................................................................................................................................. 36 MANAGE 1.3 ................................................................................................................................................................................. 37 MANAGE 1.4 ................................................................................................................................................................................. 39 MANAGE 2.1 ................................................................................................................................................................................. 40 MANAGE 2.2 ................................................................................................................................................................................. 42 MANAGE 2.3 ................................................................................................................................................................................. 48 MANAGE 2.4 ................................................................................................................................................................................. 49 MANAGE 3.1 ................................................................................................................................................................................. 51 MANAGE 3.2 ................................................................................................................................................................................. 52 MANAGE 4.1 ................................................................................................................................................................................. 53 MANAGE 4.2 ................................................................................................................................................................................. 54 MANAGE 4.3 ................................................................................................................................................................................. 56

MAP ................................................................................................................................................................................ 58

MAP 1.1........................................................................................................................................................................................... 58 MAP 1.2........................................................................................................................................................................................... 62 MAP 1.3........................................................................................................................................................................................... 63 MAP 1.4........................................................................................................................................................................................... 65 MAP 1.5........................................................................................................................................................................................... 66 MAP 1.6........................................................................................................................................................................................... 68 MAP 2.1........................................................................................................................................................................................... 70

[p. 3]

MAP 2.2........................................................................................................................................................................................... 71 MAP 2.3........................................................................................................................................................................................... 74 MAP 3.1........................................................................................................................................................................................... 77 MAP 3.2........................................................................................................................................................................................... 79 MAP 3.3........................................................................................................................................................................................... 80 MAP 3.4........................................................................................................................................................................................... 82 MAP 3.5........................................................................................................................................................................................... 84 MAP 4.1........................................................................................................................................................................................... 86 MAP 4.2........................................................................................................................................................................................... 88 MAP 5.1........................................................................................................................................................................................... 89 MAP 5.2........................................................................................................................................................................................... 90

MEASURE...................................................................................................................................................................... 93

MEASURE 1.1 ............................................................................................................................................................................... 93 MEASURE 1.2 ............................................................................................................................................................................... 95 MEASURE 1.3 ............................................................................................................................................................................... 96 MEASURE 2.1 ............................................................................................................................................................................... 98 MEASURE 2.2 ............................................................................................................................................................................... 99 MEASURE 2.3 ............................................................................................................................................................................ 102 MEASURE 2.4 ............................................................................................................................................................................ 104 MEASURE 2.5 ............................................................................................................................................................................ 106 MEASURE 2.6 ............................................................................................................................................................................ 108 MEASURE 2.7 ............................................................................................................................................................................ 110 MEASURE 2.8 ............................................................................................................................................................................ 112 MEASURE 2.9 ............................................................................................................................................................................ 115 MEASURE 2.10 ......................................................................................................................................................................... 118 MEASURE 2.11 ......................................................................................................................................................................... 121 MEASURE 2.12 ......................................................................................................................................................................... 126 MEASURE 2.13 ......................................................................................................................................................................... 128 MEASURE 3.1 ............................................................................................................................................................................ 129 MEASURE 3.2 ............................................................................................................................................................................ 131 MEASURE 3.3 ............................................................................................................................................................................ 132 MEASURE 4.1 ............................................................................................................................................................................ 134 MEASURE 4.2 ............................................................................................................................................................................ 137 MEASURE 4.3 ............................................................................................................................................................................ 140

## FORWARD


[p. 4]

About the Playbook

The Playbook provides suggested actions for achieving the outcomes laid out in the AI Risk Management Framework (AI RMF) Core (Tables 1 – 4 in AI RMF 1.0). Suggestions are aligned to each sub-category within the four AI RMF functions (Govern, Map, Measure, Manage).

The Playbook is neither a checklist nor set of steps to be followed in its entirety.

Playbook suggestions are voluntary. Organizations may utilize this information by borrowing as many – or as few – suggestions as apply to their industry use case or interests.

Govern Map Measure Manage

## GOVERN


[pp. 6-7]

Govern

Policies, processes, procedures and practices across the organization related to the mapping, measuring and managing of AI risks are in place, transparent, and implemented effectively.

GOVERN 1.1 Legal and regulatory requirements involving AI are understood, managed, and documented.

About AI systems may be subject to specific applicable legal and regulatory requirements. Some legal requirements can mandate (e.g., nondiscrimination, data privacy and security controls) documentation, disclosure, and increased AI system transparency. These requirements are complex and may not be applicable or differ across applications and contexts.

For example, AI system testing processes for bias measurement, such as disparate impact, are not applied uniformly within the legal context. Disparate impact is broadly defined as a facially neutral policy or practice that disproportionately harms a group based on a protected trait. Notably, some modeling algorithms or debiasing techniques that rely on demographic information, could also come into tension with legal prohibitions on disparate treatment (i.e., intentional discrimination).

Additionally, some intended users of AI systems may not have consistent or reliable access to fundamental internet technologies (a phenomenon widely described as the “digital divide”) or may experience difficulties interacting with AI systems due to disabilities or impairments. Such factors may mean different communities experience bias or other negative impacts when trying to access AI systems. Failure to address such design issues may pose legal risks, for example in employment related activities affecting persons with disabilities.

Suggested Actions • Maintain awareness of the applicable legal and regulatory considerations and requirements specific to industry, sector, and business purpose, as well as the application context of the deployed AI system. • Align risk management efforts with applicable legal standards. • Maintain policies for training (and re-training) organizational staff about necessary legal or regulatory considerations that may impact AI-related design, development and deployment activities.

Transparency & Documentation

Organizations can document the following • To what extent has the entity defined and documented the regulatory environment— including minimum requirements in laws and regulations?

• Has the system been reviewed for its compliance to applicable laws, regulations, standards, and guidance? • To what extent has the entity defined and documented the regulatory environment— including applicable requirements in laws and regulations? • Has the system been reviewed for its compliance to relevant applicable laws, regulations, standards, and guidance?

AI Transparency Resources GAO-21-519SP: AI Accountability Framework for Federal Agencies & Other Entities.

References Andrew Smith, "Using Artificial Intelligence and Algorithms," FTC Business Blog (2020).

Rebecca Kelly Slaughter, "Algorithms and Economic Justice," ISP Digital Future Whitepaper & YJoLT Special Publication (2021).

Patrick Hall, Benjamin Cox, Steven Dickerson, Arjun Ravi Kannan, Raghu Kulkarni, and Nicholas Schmidt, "A United States fair lending perspective on machine learning," Frontiers in Artificial Intelligence 4 (2021).

AI Hiring Tools and the Law, Partnership on Employment & Accessible Technology (PEAT, peatworks.org).

[pp. 7-8]

GOVERN 1.2 The characteristics of trustworthy AI are integrated into organizational policies, processes, and procedures.

About Policies, processes, and procedures are central components of effective AI risk management and fundamental to individual and organizational accountability. All stakeholders benefit from policies, processes, and procedures which require preventing harm by design and default.

Organizational policies and procedures will vary based on available resources and risk profiles, but can help systematize AI actor roles and responsibilities throughout the AI lifecycle. Without such policies, risk management can be subjective across the organization, and exacerbate rather than minimize risks over time. Policies, or summaries thereof, are understandable to relevant AI actors. Policies reflect an understanding of the underlying metrics, measurements, and tests that are necessary to support policy and AI system design, development, deployment and use.

Lack of clear information about responsibilities and chains of command will limit the effectiveness of risk management.

Suggested Actions Organizational AI risk management policies should be designed to:

• Define key terms and concepts related to AI systems and the scope of their purposes and intended uses. • Connect AI governance to existing organizational governance and risk controls. • Align to broader data governance policies and practices, particularly the use of sensitive or otherwise risky data. • Detail standards for experimental design, data quality, and model training. • Outline and document risk mapping and measurement processes and standards. • Detail model testing and validation processes. • Detail review processes for legal and risk functions. • Establish the frequency of and detail for monitoring, auditing and review processes. • Outline change management requirements. • Outline processes for internal and external stakeholder engagement. • Establish whistleblower policies to facilitate reporting of serious AI system concerns. • Detail and test incident response plans. • Verify that formal AI risk management policies align to existing legal standards, and industry best practices and norms. • Establish AI risk management policies that broadly align to AI system trustworthy characteristics. • Verify that formal AI risk management policies include currently deployed and third- party AI systems.

Transparency & Documentation

Organizations can document the following • To what extent do these policies foster public trust and confidence in the use of the AI system? • What policies has the entity developed to ensure the use of the AI system is consistent with its stated values and principles? • What policies and documentation has the entity developed to encourage the use of its AI system as intended? • To what extent are the model outputs consistent with the entity’s values and principles to foster public trust and equity?

AI Transparency Resources GAO-21-519SP: AI Accountability Framework for Federal Agencies & Other Entities.

References Off. Comptroller Currency, Comptroller’s Handbook: Model Risk Management (Aug. 2021).

GAO, “Artificial Intelligence: An Accountability Framework for Federal Agencies and Other Entities,” GAO@100 (GAO-21-519SP), June 2021.

NIST, "U.S. Leadership in AI: A Plan for Federal Engagement in Developing Technical Standards and Related Tools".

[pp. 9-10]

Lipton, Zachary and McAuley, Julian and Chouldechova, Alexandra, Does mitigating ML’s impact disparity require treatment disparity? Advances in Neural Information Processing Systems, 2018.

Jessica Newman (2023) “A Taxonomy of Trustworthiness for Artificial Intelligence: Connecting Properties of Trustworthiness with Risk Management and the AI Lifecycle,” UC Berkeley Center for Long-Term Cybersecurity.

Emily Hadley (2022). Prioritizing Policies for Furthering Responsible Artificial Intelligence in the United States. 2022 IEEE International Conference on Big Data (Big Data), 5029-5038.

SAS Institute, “The SAS® Data Governance Framework: A Blueprint for Success”.

ISO, “Information technology — Reference Model of Data Management, “ ISO/IEC TR 10032:200.

“Play 5: Create a formal policy,” Partnership on Employment & Accessible Technology (PEAT, peatworks.org).

"National Institute of Standards and Technology. (2018). Framework for improving critical infrastructure cybersecurity.

Kaitlin R. Boeckl and Naomi B. Lefkovitz. "NIST Privacy Framework: A Tool for Improving Privacy Through Enterprise Risk Management, Version 1.0." National Institute of Standards and Technology (NIST), January 16, 2020.

“plainlanguage.gov – Home,” The U.S. Government.

GOVERN 1.3 Processes and procedures are in place to determine the needed level of risk management activities based on the organization's risk tolerance.

About Risk management resources are finite in any organization. Adequate AI governance policies delineate the mapping, measurement, and prioritization of risks to allocate resources toward the most material issues for an AI system to ensure effective risk management. Policies may specify systematic processes for assigning mapped and measured risks to standardized risk scales.

AI risk tolerances range from negligible to critical – from, respectively, almost no risk to risks that can result in irredeemable human, reputational, financial, or environmental losses. Risk tolerance rating policies consider different sources of risk, (e.g., financial, operational, safety and wellbeing, business, reputational, or model risks). A typical risk measurement approach entails the multiplication, or qualitative combination, of measured or estimated impact and likelihood of impacts into a risk score (risk ≈ impact x likelihood). This score is then placed on a risk scale. Scales for risk may be qualitative, such as red- amber-green (RAG), or may entail simulations or econometric approaches. Impact

assessments are a common tool for understanding the severity of mapped risks. In the most fulsome AI risk management approaches, all models are assigned to a risk level.

[pp. 10-11]

Suggested Actions • Establish policies to define mechanisms for measuring or understanding an AI system’s potential impacts, e.g., via regular impact assessments at key stages in the AI lifecycle, connected to system impacts and frequency of system updates. • Establish policies to define mechanisms for measuring or understanding the likelihood of an AI system’s impacts and their magnitude at key stages in the AI lifecycle. • Establish policies that define assessment scales for measuring potential AI system impact. Scales may be qualitative, such as red-amber-green (RAG), or may entail simulations or econometric approaches. • Establish policies for assigning an overall risk measurement approach for an AI system, or its important components, e.g., via multiplication or combination of a mapped risk’s impact and likelihood (risk ≈ impact x likelihood). • Establish policies to assign systems to uniform risk scales that are valid across the organization’s AI portfolio (e.g. documentation templates), and acknowledge risk tolerance and risk levels may change over the lifecycle of an AI system.

Transparency & Documentation

Organizations can document the following • How do system performance metrics inform risk tolerance decisions? • What policies has the entity developed to ensure the use of the AI system is consistent with organizational risk tolerance? • How do the entity’s data security and privacy assessments inform risk tolerance decisions?

AI Transparency Resources • GAO-21-519SP: AI Accountability Framework for Federal Agencies & Other Entities.

References Board of Governors of the Federal Reserve System. SR 11-7: Guidance on Model Risk Management. (April 4, 2011).

The Office of the Comptroller of the Currency. Enterprise Risk Appetite Statement. (Nov. 20, 2019).

Brenda Boultwood, How to Develop an Enterprise Risk-Rating Approach (Aug. 26, 2021). Global Association of Risk Professionals (garp.org). Accessed Jan. 4, 2023.

GAO-17-63: Enterprise Risk Management: Selected Agencies’ Experiences Illustrate Good Practices in Managing Risk.

GOVERN 1.4 The risk management process and its outcomes are established through transparent policies, procedures, and other controls based on organizational risk priorities.

About Clear policies and procedures relating to documentation and transparency facilitate and enhance efforts to communicate roles and responsibilities for the Map, Measure and Manage functions across the AI lifecycle. Standardized documentation can help organizations systematically integrate AI risk management processes and enhance accountability efforts. For example, by adding their contact information to a work product document, AI actors can improve communication, increase ownership of work products, and potentially enhance consideration of product quality. Documentation may generate downstream benefits related to improved system replicability and robustness. Proper documentation storage and access procedures allow for quick retrieval of critical information during a negative incident. Explainable machine learning efforts (models and explanatory methods) may bolster technical documentation practices by introducing additional information for review and interpretation by AI Actors.

[pp. 11-12]

Suggested Actions • Establish and regularly review documentation policies that, among others, address information related to:

• AI actors contact informations • Business justification • Scope and usages • Expected and potential risks and impacts • Assumptions and limitations • Description and characterization of training data • Algorithmic methodology • Evaluated alternative approaches • Description of output data • Testing and validation results (including explanatory visualizations and information) • Down- and up-stream dependencies • Plans for deployment, monitoring, and change management • Stakeholder engagement plans

• Verify documentation policies for AI systems are standardized across the organization and remain current. • Establish policies for a model documentation inventory system and regularly review its completeness, usability, and efficacy. • Establish mechanisms to regularly review the efficacy of risk management processes. • Identify AI actors responsible for evaluating efficacy of risk management processes and approaches, and for course-correction based on results.

• Establish policies and processes regarding public disclosure of the use of AI and risk management material such as impact assessments, audits, model documentation and validation and testing results. • Document and review the use and efficacy of different types of transparency tools and follow industry standards at the time a model is in use.

Transparency & Documentation

Organizations can document the following • To what extent has the entity clarified the roles, responsibilities, and delegated authorities to relevant stakeholders? • What are the roles, responsibilities, and delegation of authorities of personnel involved in the design, development, deployment, assessment and monitoring of the AI system? • How will the appropriate performance metrics, such as accuracy, of the AI be monitored after the AI is deployed? How much distributional shift or model drift from baseline performance is acceptable?

AI Transparency Resources • GAO-21-519SP: AI Accountability Framework for Federal Agencies & Other Entities. • Intel.gov: AI Ethics Framework for Intelligence Community - 2020.

References Bd. Governors Fed. Rsrv. Sys., Supervisory Guidance on Model Risk Management, SR Letter 11-7 (Apr. 4, 2011).

Off. Comptroller Currency, Comptroller’s Handbook: Model Risk Management (Aug. 2021).

Margaret Mitchell et al., “Model Cards for Model Reporting.” Proceedings of 2019 FATML Conference.

Timnit Gebru et al., “Datasheets for Datasets,” Communications of the ACM 64, No. 12, 2021.

Emily M. Bender, Batya Friedman, Angelina McMillan-Major (2022). A Guide for Writing Data Statements for Natural Language Processing. University of Washington. Accessed July 14, 2022.

M. Arnold, R. K. E. Bellamy, M. Hind, et al. FactSheets: Increasing trust in AI services through supplier’s declarations of conformity. IBM Journal of Research and Development 63, 4/5 (July-September 2019), 6:1-6:13.

[pp. 12-14]

Navdeep Gill, Abhishek Mathur, Marcos V. Conde (2022). A Brief Overview of AI Governance for Responsible Machine Learning Systems. ArXiv, abs/2211.13130.

John Richards, David Piorkowski, Michael Hind, et al. A Human-Centered Methodology for Creating AI FactSheets. Bulletin of the IEEE Computer Society Technical Committee on Data Engineering.

Christoph Molnar, Interpretable Machine Learning, lulu.com.

David A. Broniatowski. 2021. Psychological Foundations of Explainability and Interpretability in Artificial Intelligence. National Institute of Standards and Technology (NIST) IR 8367. National Institute of Standards and Technology, Gaithersburg, MD.

OECD (2022), “OECD Framework for the Classification of AI systems”, OECD Digital Economy Papers, No. 323, OECD Publishing, Paris.

GOVERN 1.5 Ongoing monitoring and periodic review of the risk management process and its outcomes are planned, organizational roles and responsibilities are clearly defined, including determining the frequency of periodic review.

About AI systems are dynamic and may perform in unexpected ways once deployed or after deployment. Continuous monitoring is a risk management process for tracking unexpected issues and performance changes, in real-time or at a specific frequency, across the AI system lifecycle.

Incident response and “appeal and override” are commonly used processes in information technology management. These processes enable real-time flagging of potential incidents, and human adjudication of system outcomes.

Establishing and maintaining incident response plans can reduce the likelihood of additive impacts during an AI incident. Smaller organizations which may not have fulsome governance programs, can utilize incident response plans for addressing system failures, abuse or misuse.

Suggested Actions • Establish policies to allocate appropriate resources and capacity for assessing impacts of AI systems on individuals, communities and society. • Establish policies and procedures for monitoring and addressing AI system performance and trustworthiness, including bias and security problems, across the lifecycle of the system. • Establish policies for AI system incident response, or confirm that existing incident response policies apply to AI systems. • Establish policies to define organizational functions and personnel responsible for AI system monitoring and incident response activities. • Establish mechanisms to enable the sharing of feedback from impacted individuals or communities about negative impacts from AI systems. • Establish mechanisms to provide recourse for impacted individuals or communities to contest problematic AI system outcomes. • Establish opt-out mechanisms.

Transparency & Documentation

Organizations can document the following • To what extent does the system/entity consistently measure progress towards stated goals and objectives? • Did your organization implement a risk management system to address risks involved in deploying the identified AI solution (e.g. personnel risk or changes to commercial objectives)? • Did your organization address usability problems and test whether user interfaces served their intended purposes?

AI Transparency Resources • GAO-21-519SP: AI Accountability Framework for Federal Agencies & Other Entities. • WEF Model AI Governance Framework Assessment 2020.

[pp. 14-15]

References National Institute of Standards and Technology. (2018). Framework for improving critical infrastructure cybersecurity.

National Institute of Standards and Technology. (2012). Computer Security Incident Handling Guide. NIST Special Publication 800-61 Revision 2.

GOVERN 1.6 Mechanisms are in place to inventory AI systems and are resourced according to organizational risk priorities.

About An AI system inventory is an organized database of artifacts relating to an AI system or model. It may include system documentation, incident response plans, data dictionaries, links to implementation software or source code, names and contact information for relevant AI actors, or other information that may be helpful for model or system maintenance and incident response purposes. AI system inventories also enable a holistic view of organizational AI assets. A serviceable AI system inventory may allow for the quick resolution of:

• specific queries for single models, such as “when was this model last refreshed?” • high-level queries across all models, such as, “how many models are currently deployed within our organization?” or “how many users are impacted by our models?”

AI system inventories are a common element of traditional model risk management approaches and can provide technical, business and risk management benefits. Typically inventories capture all organizational models or systems, as partial inventories may not provide the value of a full inventory.

Suggested Actions • Establish policies that define the creation and maintenance of AI system inventories. • Establish policies that define a specific individual or team that is responsible for maintaining the inventory. • Establish policies that define which models or systems are inventoried, with preference to inventorying all models or systems, or minimally, to high risk models or systems, or systems deployed in high-stakes settings. • Establish policies that define model or system attributes to be inventoried, e.g, documentation, links to source code, incident response plans, data dictionaries, AI actor contact information.

Transparency & Documentation

Organizations can document the following • Who is responsible for documenting and maintaining the AI system inventory details? • What processes exist for data generation, acquisition/collection, ingestion, staging/storage, transformations, security, maintenance, and dissemination? • Given the purpose of this AI, what is an appropriate interval for checking whether it is still accurate, unbiased, explainable, etc.? What are the checks for this model?

AI Transparency Resources • GAO-21-519SP: AI Accountability Framework for Federal Agencies & Other Entities. • Intel.gov: AI Ethics Framework for Intelligence Community - 2020.

References “A risk-based integrity level schema”, in IEEE 1012, IEEE Standard for System, Software, and Hardware Verification and Validation. See Annex B.

Off. Comptroller Currency, Comptroller’s Handbook: Model Risk Management (Aug. 2021). See “Model Inventory,” pg. 26.

[pp. 15-17]

VertaAI, “ModelDB: An open-source system for Machine Learning model versioning, metadata, and experiment management.” Accessed Jan. 5, 2023.

GOVERN 1.7 Processes and procedures are in place for decommissioning and phasing out of AI systems safely and in a manner that does not increase risks or decrease the organization’s trustworthiness.

About Irregular or indiscriminate termination or deletion of models or AI systems may be inappropriate and increase organizational risk. For example, AI systems may be subject to regulatory requirements or implicated in future security or legal investigations. To maintain trust, organizations may consider establishing policies and processes for the systematic and deliberate decommissioning of AI systems. Typically, such policies consider user and

community concerns, risks in dependent and linked systems, and security, legal or regulatory concerns. Decommissioned models or systems may be stored in a model inventory along with active models, for an established length of time.

Suggested Actions • Establish policies for decommissioning AI systems. Such policies typically address:

• User and community concerns, and reputational risks. • Business continuity and financial risks. • Up and downstream system dependencies. • Regulatory requirements (e.g., data retention). • Potential future legal, regulatory, security or forensic investigations. • Migration to the replacement system, if appropriate.

• Establish policies that delineate where and for how long decommissioned systems, models and related artifacts are stored. • Establish practices to track accountability and consider how decommission and other adaptations or changes in system deployment contribute to downstream impacts for individuals, groups and communities. • Establish policies that address ancillary data or artifacts that must be preserved for fulsome understanding or execution of the decommissioned AI system, e.g., predictions, explanations, intermediate input feature representations, usernames and passwords, etc.

Transparency & Documentation

Organizations can document the following • What processes exist for data generation, acquisition/collection, ingestion, staging/storage, transformations, security, maintenance, and dissemination? • To what extent do these policies foster public trust and confidence in the use of the AI system? • If anyone believes that the AI no longer meets this ethical framework, who will be responsible for receiving the concern and as appropriate investigating and remediating the issue? Do they have authority to modify, limit, or stop the use of the AI? • If it relates to people, were there any ethical review applications/reviews/approvals? (e.g. Institutional Review Board applications)

AI Transparency Resources • GAO-21-519SP: AI Accountability Framework for Federal Agencies & Other Entities. • Intel.gov: AI Ethics Framework for Intelligence Community - 2020. • Datasheets for Datasets.

References Michelle De Mooy, Joseph Jerome and Vijay Kasschau, “Should It Stay or Should It Go? The Legal, Policy and Technical Landscape Around Data Deletion,” Center for Democracy and Technology, 2017.


---

[source overview](overview.md) | [next part](text-002.md)

[^original]: NIST, "NIST AI RMF Playbook" (2024-08-02). https://airc.nist.gov/airmf-resources/playbook/
