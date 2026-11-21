---
type: Source Text
title: NIST AI RMF Playbook - part 6 of 12 (pp. 70-82)
description: 'Verbatim extracted text, pp. 70-82: MAP'
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
part: 6
parts_total: 12
content_mode: full_text
generated:
  by: process:fincrime-kb-build
  at: '2026-11-21T18:42:19Z'
verified:
- by: process:kb-validate/verbatim-coverage
  at: '2026-11-21T18:42:19Z'
sources:
- id: original
  resource: https://airc.nist.gov/airmf-resources/playbook/
  title: NIST AI RMF Playbook
  author: org:nist
  last_modified: '2024-08-02T00:00:00Z'
---

# NIST AI RMF Playbook

[previous part](text-005.md) | [source overview](overview.md) | [next part](text-007.md)

> Verbatim text extracted from the original (NIST, 2024-08-02), part 6 of 12, pp. 70-82. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **industry practice**.[^original]

## MAP


[pp. 70-71]

Leonard Haas, Sebastian Gießler, and Veronika Thiel. 2020. In the realm of paper tigers – exploring the failings of AI ethics guidelines. (April 28, 2020).

MAP 1.5 Organizational risk tolerances are determined and documented.

About Risk tolerance reflects the level and type of risk the organization is willing to accept while conducting its mission and carrying out its strategy.

Organizations can follow existing regulations and guidelines for risk criteria, tolerance and response established by organizational, domain, discipline, sector, or professional requirements. Some sectors or industries may have established definitions of harm or may have established documentation, reporting, and disclosure requirements.

Within sectors, risk management may depend on existing guidelines for specific applications and use case settings. Where established guidelines do not exist, organizations will want to define reasonable risk tolerance in consideration of different sources of risk (e.g., financial, operational, safety and wellbeing, business, reputational, and model risks) and different levels of risk (e.g., from negligible to critical).

Risk tolerances inform and support decisions about whether to continue with development or deployment - termed “go/no-go”. Go/no-go decisions related to AI system risks can take stakeholder feedback into account, but remain independent from stakeholders’ vested financial or reputational interests.

If mapping risk is prohibitively difficult, a "no-go" decision may be considered for the specific system.

Suggested Actions • Utilize existing regulations and guidelines for risk criteria, tolerance and response established by organizational, domain, discipline, sector, or professional requirements.

• Establish risk tolerance levels for AI systems and allocate the appropriate oversight resources to each level. • Establish risk criteria in consideration of different sources of risk, (e.g., financial, operational, safety and wellbeing, business, reputational, and model risks) and different levels of risk (e.g., from negligible to critical). • Identify maximum allowable risk tolerance above which the system will not be deployed, or will need to be prematurely decommissioned, within the contextual or application setting. • Articulate and analyze tradeoffs across trustworthiness characteristics as relevant to proposed context of use. When tradeoffs arise, document them and plan for traceable actions (e.g.: impact mitigation, removal of system from development or use) to inform management decisions. • Review uses of AI systems for “off-label” purposes, especially in settings that organizations have deemed as high-risk. Document decisions, risk-related trade-offs, and system limitations.

Transparency & Documentation

Organizations can document the following • Which existing regulations and guidelines apply, and the entity has followed, in the development of system risk tolerances? • What criteria and assumptions has the entity utilized when developing system risk tolerances? • How has the entity identified maximum allowable risk tolerance? • What conditions and purposes are considered “off-label” for system use?

[pp. 71-72]

AI Transparency Resources • GAO-21-519SP: AI Accountability Framework for Federal Agencies & Other Entities. • WEF Model AI Governance Framework Assessment 2020. • WEF Companion to the Model AI Governance Framework- 2020.

References Board of Governors of the Federal Reserve System. SR 11-7: Guidance on Model Risk Management. (April 4, 2011).

The Office of the Comptroller of the Currency. Enterprise Risk Appetite Statement. (Nov. 20, 2019).

Brenda Boultwood, How to Develop an Enterprise Risk-Rating Approach (Aug. 26, 2021). Global Association of Risk Professionals (garp.org). Accessed Jan. 4, 2023.

Virginia Eubanks, 1972-, Automating Inequality: How High-tech Tools Profile, Police, and Punish the Poor. New York, NY, St. Martin's Press, 2018.

GAO-17-63: Enterprise Risk Management: Selected Agencies’ Experiences Illustrate Good Practices in Managing Risk.

NIST Risk Management Framework.

MAP 1.6 System requirements (e.g., “the system shall respect the privacy of its users”) are elicited from and understood by relevant AI actors. Design decisions take socio-technical implications into account to address AI risks.

About AI system development requirements may outpace documentation processes for traditional software. When written requirements are unavailable or incomplete, AI actors may inadvertently overlook business and stakeholder needs, over-rely on implicit human biases such as confirmation bias and groupthink, and maintain exclusive focus on computational requirements.

Eliciting system requirements, designing for end users, and considering societal impacts early in the design phase is a priority that can enhance AI systems’ trustworthiness.

[pp. 72-73]

Suggested Actions • Proactively incorporate trustworthy characteristics into system requirements. • Establish mechanisms for regular communication and feedback between relevant AI actors and internal or external stakeholders related to system design or deployment decisions. • Develop and standardize practices to assess potential impacts at all stages of the AI lifecycle, and in collaboration with interdisciplinary experts, actors external to the team that developed or deployed the AI system, and potentially impacted communities . • Include potentially impacted groups, communities and external entities (e.g. civil society organizations, research institutes, local community groups, and trade associations) in the formulation of priorities, definitions and outcomes during impact assessment activities. • Conduct qualitative interviews with end user(s) to regularly evaluate expectations and design plans related to Human-AI configurations and tasks. • Analyze dependencies between contextual factors and system requirements. List potential impacts that may arise from not fully considering the importance of trustworthiness characteristics in any decision making. • Follow responsible design techniques in tasks such as software engineering, product management, and participatory engagement. Some examples for eliciting and documenting stakeholder requirements include product requirement documents (PRDs), user stories, user interaction/user experience (UI/UX) research, systems engineering, ethnography and related field methods.

• Conduct user research to understand individuals, groups and communities that will be impacted by the AI, their values & context, and the role of systemic and historical biases. Integrate learnings into decisions about data selection and representation.

Transparency & Documentation

Organizations can document the following • What type of information is accessible on the design, operations, and limitations of the AI system to external stakeholders, including end users, consumers, regulators, and individuals impacted by use of the AI system? • To what extent is this information sufficient and appropriate to promote transparency? Promote transparency by enabling external stakeholders to access information on the design, operation, and limitations of the AI system. • To what extent has relevant information been disclosed regarding the use of AI systems, such as (a) what the system is for, (b) what it is not for, (c) how it was designed, and (d) what its limitations are? (Documentation and external communication can offer a way for entities to provide transparency.) • How will the relevant AI actor(s) address changes in accuracy and precision due to either an adversary’s attempts to disrupt the AI system or unrelated changes in the operational/business environment, which may impact the accuracy of the AI system? • What metrics has the entity developed to measure performance of the AI system? • What justifications, if any, has the entity provided for the assumptions, boundaries, and limitations of the AI system?

AI Transparency Resources • GAO-21-519SP: AI Accountability Framework for Federal Agencies & Other Entities. • Stakeholders in Explainable AI, Sep. 2018. • High-Level Expert Group on Artificial Intelligence set up by the European Commission, Ethics Guidelines for Trustworthy AI.

[pp. 73-74]

References National Academies of Sciences, Engineering, and Medicine 2022. Fostering Responsible Computing Research: Foundations and Practices. Washington, DC: The National Academies Press.

Abeba Birhane, William S. Isaac, Vinodkumar Prabhakaran, Mark Diaz, Madeleine Clare Elish, Iason Gabriel and Shakir Mohamed. “Power to the People? Opportunities and Challenges for Participatory AI.” Equity and Access in Algorithms, Mechanisms, and Optimization (2022).

Amit K. Chopra, Fabiano Dalpiaz, F. Başak Aydemir, et al. 2014. Protos: Foundations for engineering innovative sociotechnical systems. In 2014 IEEE 22nd International Requirements Engineering Conference (RE) (2014), 53-62.

Andrew D. Selbst, danah boyd, Sorelle A. Friedler, et al. 2019. Fairness and Abstraction in Sociotechnical Systems. In Proceedings of the Conference on Fairness, Accountability, and Transparency (FAT* '19). Association for Computing Machinery, New York, NY, USA, 59–68.

Gordon Baxter and Ian Sommerville. 2011. Socio-technical systems: From design methods to systems engineering. Interacting with Computers, 23, 1 (Jan. 2011), 4–17.

Roel Dobbe, Thomas Krendl Gilbert, and Yonatan Mintz. 2021. Hard choices in artificial intelligence. Artificial Intelligence 300 (14 July 2021), 103555, ISSN 0004-3702.

Yilin Huang, Giacomo Poderi, Sanja Šćepanović, et al. 2019. Embedding Internet-of-Things in Large-Scale Socio-technical Systems: A Community-Oriented Design in Future Smart Grids. In The Internet of Things for Smart Urban Ecosystems (2019), 125-150. Springer, Cham.

Victor Udoewa, (2022). An introduction to radical participatory design: decolonising participatory design processes. Design Science. 8. 10.1017/dsj.2022.24.

MAP 2.1 The specific task, and methods used to implement the task, that the AI system will support is defined (e.g., classifiers, generative models, recommenders).

About AI actors define the technical learning or decision-making task(s) an AI system is designed to accomplish, or the benefits that the system will provide. The clearer and narrower the task definition, the easier it is to map its benefits and risks, leading to more fulsome risk management.

Suggested Actions • Define and document AI system’s existing and potential learning task(s) along with known assumptions and limitations.

Transparency & Documentation

[pp. 74-75]

Organizations can document the following • To what extent has the entity clearly defined technical specifications and requirements for the AI system? • To what extent has the entity documented the AI system’s development, testing methodology, metrics, and performance outcomes? • How do the technical specifications and requirements align with the AI system’s goals and objectives? • Did your organization implement accountability-based practices in data management and protection (e.g. the PDPA and OECD Privacy Principles)? • How are outputs marked to clearly show that they came from an AI?

AI Transparency Resources • Datasheets for Datasets.

• WEF Model AI Governance Framework Assessment 2020. • WEF Companion to the Model AI Governance Framework- 2020. • ATARC Model Transparency Assessment (WD) – 2020. • Transparency in Artificial Intelligence - S. Larsson and F. Heintz – 2020.

References Leong, Brenda (2020). The Spectrum of Artificial Intelligence - An Infographic Tool. Future of Privacy Forum.

Brownlee, Jason (2020). A Tour of Machine Learning Algorithms. Machine Learning Mastery.

MAP 2.2 Information about the AI system’s knowledge limits and how system output may be utilized and overseen by humans is documented. Documentation provides sufficient information to assist relevant AI actors when making informed decisions and taking subsequent actions.

About An AI lifecycle consists of many interdependent activities involving a diverse set of actors that often do not have full visibility or control over other parts of the lifecycle and its associated contexts or risks. The interdependencies between these activities, and among the relevant AI actors and organizations, can make it difficult to reliably anticipate potential impacts of AI systems. For example, early decisions in identifying the purpose and objective of an AI system can alter its behavior and capabilities, and the dynamics of deployment setting (such as end users or impacted individuals) can shape the positive or negative impacts of AI system decisions. As a result, the best intentions within one dimension of the AI lifecycle can be undermined via interactions with decisions and conditions in other, later activities. This complexity and varying levels of visibility can introduce uncertainty. And, once deployed and in use, AI systems may sometimes perform poorly, manifest unanticipated negative impacts, or violate legal or ethical norms. These risks and incidents can result from a variety of factors. For example, downstream decisions can be influenced by end user over-trust or under-trust, and other complexities related to AI-supported decision-making.

Anticipating, articulating, assessing and documenting AI systems’ knowledge limits and how system output may be utilized and overseen by humans can help mitigate the uncertainty associated with the realities of AI system deployments. Rigorous design processes include defining system knowledge limits, which are confirmed and refined based on TEVV processes.

Suggested Actions • Document settings, environments and conditions that are outside the AI system’s intended use.

[pp. 76-77]

• Design for end user workflows and toolsets, concept of operations, and explainability and interpretability criteria in conjunction with end user(s) and associated qualitative feedback. • Plan and test human-AI configurations under close to real-world conditions and document results. • Follow stakeholder feedback processes to determine whether a system achieved its documented purpose within a given use context, and whether end users can correctly comprehend system outputs or results. • Document dependencies on upstream data and other AI systems, including if the specified system is an upstream dependency for another AI system or other data. • Document connections the AI system or data will have to external networks (including the internet), financial markets, and critical infrastructure that have potential for negative externalities. Identify and document negative impacts as part of considering the broader risk thresholds and subsequent go/no-go deployment as well as post- deployment decommissioning decisions.

Transparency & Documentation

Organizations can document the following • Does the AI system provide sufficient information to assist the personnel to make an informed decision and take actions accordingly? • What type of information is accessible on the design, operations, and limitations of the AI system to external stakeholders, including end users, consumers, regulators, and individuals impacted by use of the AI system? • Based on the assessment, did your organization implement the appropriate level of human involvement in AI-augmented decision-making?

AI Transparency Resources • Datasheets for Datasets. • WEF Model AI Governance Framework Assessment 2020. • WEF Companion to the Model AI Governance Framework- 2020. • ATARC Model Transparency Assessment (WD) – 2020. • Transparency in Artificial Intelligence - S. Larsson and F. Heintz – 2020.

References

Context of use International Standards Organization (ISO). 2019. ISO 9241-210:2019 Ergonomics of human-system interaction — Part 210: Human-centred design for interactive systems.

National Institute of Standards and Technology (NIST), Mary Theofanos, Yee-Yin Choong, et al. 2017. NIST Handbook 161 Usability Handbook for Public Safety Communications: Ensuring Successful Systems for First Responders.

Human-AI interaction Committee on Human-System Integration Research Topics for the 711th Human Performance Wing of the Air Force Research Laboratory and the National Academies of Sciences, Engineering, and Medicine. 2022. Human-AI Teaming: State-of-the-Art and Research Needs. Washington, D.C. National Academies Press.

Human Readiness Level Scale in the System Development Process, American National Standards Institute and Human Factors and Ergonomics Society, ANSI/HFES 400-2021

Microsoft Responsible AI Standard, v2.

[p. 77]

Saar Alon-Barkat, Madalina Busuioc, Human–AI Interactions in Public Sector Decision Making: “Automation Bias” and “Selective Adherence” to Algorithmic Advice, Journal of Public Administration Research and Theory, 2022;, muac007.

Zana Buçinca, Maja Barbara Malaya, and Krzysztof Z. Gajos. 2021. To Trust or to Think: Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making. Proc. ACM Hum.-Comput. Interact. 5, CSCW1, Article 188 (April 2021), 21 pages.

Mary L. Cummings. 2006 Automation and accountability in decision support system interface design.The Journal of Technology Studies 32(1): 23–31.

Engstrom, D. F., Ho, D. E., Sharkey, C. M., & Cuéllar, M. F. (2020). Government by algorithm: Artificial intelligence in federal administrative agencies. NYU School of Law, Public Law Research Paper, (20-54).

Susanne Gaube, Harini Suresh, Martina Raue, et al. 2021. Do as AI say: susceptibility in deployment of clinical decision-aids. npj Digital Medicine 4, Article 31 (2021).

Ben Green. 2021. The Flaws of Policies Requiring Human Oversight of Government Algorithms. Computer Law & Security Review 45 (26 Apr. 2021).

Ben Green and Amba Kak. 2021. The False Comfort of Human Oversight as an Antidote to A.I. Harm. (June 15, 2021).

Grgić-Hlača, N., Engel, C., & Gummadi, K. P. (2019). Human decision making with machine assistance: An experiment on bailing and jailing. Proceedings of the ACM on Human- Computer Interaction, 3(CSCW), 1-25.

Forough Poursabzi-Sangdeh, Daniel G Goldstein, Jake M Hofman, et al. 2021. Manipulating and Measuring Model Interpretability. In Proceedings of the 2021 CHI Conference on Human Factors in Computing Systems (CHI '21). Association for Computing Machinery, New York, NY, USA, Article 237, 1–52.

C. J. Smith (2019). Designing trustworthy AI: A human-machine teaming framework to guide development. arXiv preprint arXiv:1910.03515.

[p. 78]

T. Warden, P. Carayon, EM et al. The National Academies Board on Human System Integration (BOHSI) Panel: Explainable AI, System Transparency, and Human Machine Teaming. Proceedings of the Human Factors and Ergonomics Society Annual Meeting. 2019;63(1):631-635. doi:10.1177/1071181319631100.

MAP 2.3 Scientific integrity and TEVV considerations are identified and documented, including those related to experimental design, data collection and selection (e.g., availability, representativeness, suitability), system trustworthiness, and construct validation.

About Standard testing and evaluation protocols provide a basis to confirm assurance in a system that it is operating as designed and claimed. AI systems’ complexities create challenges for traditional testing and evaluation methodologies, which tend to be designed for static or isolated system performance. Opportunities for risk continue well beyond design and deployment, into system operation and application of system-enabled decisions. Testing and evaluation methodologies and metrics therefore address a continuum of activities. TEVV is enhanced when key metrics for performance, safety, and reliability are interpreted in a socio-technical context and not confined to the boundaries of the AI system pipeline.

Other challenges for managing AI risks relate to dependence on large scale datasets, which can impact data quality and validity concerns. The difficulty of finding the “right” data may lead AI actors to select datasets based more on accessibility and availability than on suitability for operationalizing the phenomenon that the AI system intends to support or inform. Such decisions could contribute to an environment where the data used in processes is not fully representative of the populations or phenomena that are being modeled, introducing downstream risks. Practices such as dataset reuse may also lead to disconnect from the social contexts and time periods of their creation. This contributes to issues of validity of the underlying dataset for providing proxies, measures, or predictors within the model.

Suggested Actions • Identify and document experiment design and statistical techniques that are valid for testing complex socio-technical systems like AI, which involve human factors, emergent properties, and dynamic context(s) of use. • Develop and apply TEVV protocols for models, system and its subcomponents, deployment, and operation. • Demonstrate and document that AI system performance and validation metrics are interpretable and unambiguous for downstream decision making tasks, and take socio- technical factors such as context of use into consideration. • Identify and document assumptions, techniques, and metrics used for testing and evaluation throughout the AI lifecycle including experimental design techniques for data collection, selection, and management practices in accordance with data governance policies established in GOVERN.

[pp. 79-80]

• Identify testing modules that can be incorporated throughout the AI lifecycle, and verify that processes enable corroboration by independent evaluators. • Establish mechanisms for regular communication and feedback among relevant AI actors and internal or external stakeholders related to the validity of design and deployment assumptions. • Establish mechanisms for regular communication and feedback between relevant AI actors and internal or external stakeholders related to the development of TEVV approaches throughout the lifecycle to detect and assess potentially harmful impacts • Document assumptions made and techniques used in data selection, curation, preparation and analysis, including:

• identification of constructs and proxy targets, • development of indices – especially those operationalizing concepts that are inherently unobservable (e.g. “hireability,” “criminality.” “lendability”).

• Map adherence to policies that address data and construct validity, bias, privacy and security for AI systems and verify documentation, oversight, and processes. • Identify and document transparent methods (e.g. causal discovery methods) for inferring causal relationships between constructs being modeled and dataset attributes or proxies. • Identify and document processes to understand and trace test and training data lineage and its metadata resources for mapping risks. • Document known limitations, risk mitigation efforts associated with, and methods used for, training data collection, selection, labeling, cleaning, and analysis (e.g. treatment of missing, spurious, or outlier data; biased estimators). • Establish and document practices to check for capabilities that are in excess of those that are planned for, such as emergent properties, and to revisit prior risk management steps in light of any new capabilities. • Establish processes to test and verify that design assumptions about the set of deployment contexts continue to be accurate and sufficiently complete. • Work with domain experts and other external AI actors to:

• Gain and maintain contextual awareness and knowledge about how human behavior, organizational factors and dynamics, and society influence, and are represented in, datasets, processes, models, and system output. • Identify participatory approaches for responsible Human-AI configurations and oversight tasks, taking into account sources of cognitive bias. • Identify techniques to manage and mitigate sources of bias (systemic, computational, human- cognitive) in computational models and systems, and the assumptions and decisions in their development..

• Investigate and document potential negative impacts due related to the full product lifecycle and associated processes that may conflict with organizational values and principles.

Transparency & Documentation

[pp. 80-81]

Organizations can document the following • Are there any known errors, sources of noise, or redundancies in the data? • Over what time-frame was the data collected? Does the collection time-frame match the creation time-frame • What is the variable selection and evaluation process? • How was the data collected? Who was involved in the data collection process? If the dataset relates to people (e.g., their attributes) or was generated by people, were they informed about the data collection? (e.g., datasets that collect writing, photos, interactions, transactions, etc.) • As time passes and conditions change, is the training data still representative of the operational environment? • Why was the dataset created? (e.g., were there specific tasks in mind, or a specific gap that needed to be filled?) • How does the entity ensure that the data collected are adequate, relevant, and not excessive in relation to the intended purpose?

AI Transparency Resources • Datasheets for Datasets. • WEF Model AI Governance Framework Assessment 2020. • WEF Companion to the Model AI Governance Framework- 2020. • GAO-21-519SP: AI Accountability Framework for Federal Agencies & Other Entities. • ATARC Model Transparency Assessment (WD) – 2020. • Transparency in Artificial Intelligence - S. Larsson and F. Heintz – 2020.

References

Challenges with dataset selection Alexandra Olteanu, Carlos Castillo, Fernando Diaz, and Emre Kiciman. 2019. Social Data: Biases, Methodological Pitfalls, and Ethical Boundaries. Front. Big Data 2, 13 (11 July 2019).

Amandalynne Paullada, Inioluwa Deborah Raji, Emily M. Bender, et al. 2020. Data and its (dis)contents: A survey of dataset development and use in machine learning research. arXiv:2012.05345.

Catherine D'Ignazio and Lauren F. Klein. 2020. Data Feminism. The MIT Press, Cambridge, MA.

Miceli, M., & Posada, J. (2022). The Data-Production Dispositif. ArXiv, abs/2205.11963.

Barbara Plank. 2016. What to do about non-standard (or non-canonical) language in NLP. arXiv:1608.07836.

Dataset and test, evaluation, validation and verification (TEVV) processes in AI system development National Institute of Standards and Technology (NIST), Reva Schwartz, Apostol Vassilev, et al. 2022. NIST Special Publication 1270 Towards a Standard for Identifying and Managing Bias in Artificial Intelligence.

[pp. 81-82]

Inioluwa Deborah Raji, Emily M. Bender, Amandalynne Paullada, et al. 2021. AI and the Everything in the Whole Wide World Benchmark. arXiv:2111.15366.

Statistical balance Ziad Obermeyer, Brian Powers, Christine Vogeli, and Sendhil Mullainathan. 2019. Dissecting racial bias in an algorithm used to manage the health of populations. Science 366, 6464 (25 Oct. 2019), 447-453.

Amandalynne Paullada, Inioluwa Deborah Raji, Emily M. Bender, et al. 2020. Data and its (dis)contents: A survey of dataset development and use in machine learning research. arXiv:2012.05345.

Solon Barocas, Anhong Guo, Ece Kamar, et al. 2021. Designing Disaggregated Evaluations of AI Systems: Choices, Considerations, and Tradeoffs. Proceedings of the 2021 AAAI/ACM Conference on AI, Ethics, and Society. Association for Computing Machinery, New York, NY, USA, 368–378.

Measurement and evaluation Abigail Z. Jacobs and Hanna Wallach. 2021. Measurement and Fairness. In Proceedings of the 2021 ACM Conference on Fairness, Accountability, and Transparency (FAccT ‘21). Association for Computing Machinery, New York, NY, USA, 375–385.

Ben Hutchinson, Negar Rostamzadeh, Christina Greer, et al. 2022. Evaluation Gaps in Machine Learning Practice. arXiv:2205.05256.

Laura Freeman, "Test and evaluation for artificial intelligence." Insight 23.1 (2020): 27-30.

Existing frameworks National Institute of Standards and Technology. (2018). Framework for improving critical infrastructure cybersecurity.

Kaitlin R. Boeckl and Naomi B. Lefkovitz. "NIST Privacy Framework: A Tool for Improving Privacy Through Enterprise Risk Management, Version 1.0." National Institute of Standards and Technology (NIST), January 16, 2020.

MAP 3.1 Potential benefits of intended AI system functionality and performance are examined and documented.

About AI systems have enormous potential to improve quality of life, enhance economic prosperity and security costs. Organizations are encouraged to define and document system purpose and utility, and its potential positive impacts and benefits beyond current known performance benchmarks.

It is encouraged that risk management and assessment of benefits and impacts include processes for regular and meaningful communication with potentially affected groups and communities. These stakeholders can provide valuable input related to systems’ benefits and possible limitations. Organizations may differ in the types and number of stakeholders with which they engage.


---

[previous part](text-005.md) | [source overview](overview.md) | [next part](text-007.md)

[^original]: NIST, "NIST AI RMF Playbook" (2024-08-02). https://airc.nist.gov/airmf-resources/playbook/
