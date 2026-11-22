---
type: Source Text
title: NIST AI RMF Playbook - part 5 of 12 (pp. 56-70)
description: 'Verbatim extracted text, pp. 56-70: MANAGE; MAP'
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
part: 5
parts_total: 12
content_mode: full_text
generated:
  by: process:fincrime-kb-build
  at: '2026-11-22T04:56:05Z'
verified:
- by: process:kb-validate/verbatim-coverage
  at: '2026-11-22T04:56:05Z'
sources:
- id: original
  resource: https://airc.nist.gov/airmf-resources/playbook/
  title: NIST AI RMF Playbook
  author: org:nist
  last_modified: '2024-08-02T00:00:00Z'
---

# NIST AI RMF Playbook

[previous part](text-004.md) | [source overview](overview.md) | [next part](text-006.md)

> Verbatim text extracted from the original (NIST, 2024-08-02), part 5 of 12, pp. 56-70. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **industry practice**.[^original]

## MANAGE


[pp. 56-57]

AI Transparency Resources • Artificial Intelligence Ethics Framework For The Intelligence Community. • WEF - Companion to the Model AI Governance Framework – Implementation and Self- Assessment Guide for Organizations. • Datasheets for Datasets.

References Larysa Visengeriyeva et al. “Awesome MLOps,“ GitHub. Accessed January 9, 2023.

MANAGE 4.1 Post-deployment AI system monitoring plans are implemented, including mechanisms for capturing and evaluating input from users and other relevant AI actors, appeal and override, decommissioning, incident response, recovery, and change management.

About AI system performance and trustworthiness can change due to a variety of factors. Regular AI system monitoring can help deployers identify performance degradations, adversarial attacks, unexpected and unusual behavior, near-misses, and impacts. Including pre- and post-deployment external feedback about AI system performance can enhance organizational awareness about positive and negative impacts, and reduce the time to respond to risks and harms.

Suggested Actions • Establish and maintain procedures to monitor AI system performance for risks and negative and positive impacts associated with trustworthiness characteristics. • Perform post-deployment TEVV tasks to evaluate AI system validity and reliability, bias and fairness, privacy, and security and resilience. • Evaluate AI system trustworthiness in conditions similar to deployment context of use, and prior to deployment. • Establish and implement red-teaming exercises at a prescribed cadence, and evaluate their efficacy.

• Establish procedures for tracking dataset modifications such as data deletion or rectification requests. • Establish mechanisms for regular communication and feedback between relevant AI actors and internal or external stakeholders to capture information about system performance, trustworthiness and impact. • Share information about errors, near-misses, and attack patterns with incident databases, other organizations with similar systems, and system users and stakeholders. • Respond to and document detected or reported negative impacts or issues in AI system performance and trustworthiness. • Decommission systems that exceed establish risk tolerances.

Transparency & Documentation

Organizations can document the following • To what extent has the entity documented the post-deployment AI system’s testing methodology, metrics, and performance outcomes? • How easily accessible and current is the information available to external stakeholders?

AI Transparency Resources • GAO-21-519SP - Artificial Intelligence: An Accountability Framework for Federal Agencies & Other Entities, • Datasheets for Datasets.

References Navdeep Gill, Patrick Hall, Kim Montgomery, and Nicholas Schmidt. "A Responsible Machine Learning Workflow with Focus on Interpretable Models, Post-hoc Explanation, and Discrimination Testing." Information 11, no. 3 (2020): 137.

MANAGE 4.2 Measurable activities for continual improvements are integrated into AI system updates and include regular engagement with interested parties, including relevant AI actors.

[pp. 57-59]

About Regular monitoring processes enable system updates to enhance performance and functionality in accordance with regulatory and legal frameworks, and organizational and contextual values and norms. These processes also facilitate analyses of root causes, system degradation, drift, near-misses, and failures, and incident response and documentation.

AI actors across the lifecycle have many opportunities to capture and incorporate external feedback about system performance, limitations, and impacts, and implement continuous improvements. Improvements may not always be to model pipeline or system processes, and may instead be based on metrics beyond accuracy or other quality performance measures. In these cases, improvements may entail adaptations to business or organizational procedures or practices. Organizations are encouraged to develop

improvements that will maintain traceability and transparency for developers, end users, auditors, and relevant AI actors.

Suggested Actions • Integrate trustworthiness characteristics into protocols and metrics used for continual improvement. • Establish processes for evaluating and integrating feedback into AI system improvements. • Assess and evaluate alignment of proposed improvements with relevant regulatory and legal frameworks • Assess and evaluate alignment of proposed improvements connected to the values and norms within the context of use. • Document the basis for decisions made relative to tradeoffs between trustworthy characteristics, system risks, and system opportunities

Transparency & Documentation

Organizations can document the following • How will user and other forms of stakeholder engagement be integrated into the model development process and regular performance review once deployed? • To what extent can users or parties affected by the outputs of the AI system test the AI system and provide feedback? • To what extent has the entity defined and documented the regulatory environment— including minimum requirements in laws and regulations?

AI Transparency Resources • GAO-21-519SP - Artificial Intelligence: An Accountability Framework for Federal Agencies & Other Entities, • Artificial Intelligence Ethics Framework For The Intelligence Community.

References Yen, Po-Yin, et al. "Development and Evaluation of Socio-Technical Metrics to Inform HIT Adaptation."

Carayon, Pascale, and Megan E. Salwei. "Moving toward a sociotechnical systems approach to continuous health information technology design: the path forward for improving electronic health record usability and reducing clinician burnout." Journal of the American Medical Informatics Association 28.5 (2021): 1026-1028.

Mishra, Deepa, et al. "Organizational capabilities that enable big data and predictive analytics diffusion and organizational performance: A resource-based perspective." Management Decision (2018).

MANAGE 4.3 Incidents and errors are communicated to relevant AI actors including affected communities. Processes for tracking, responding to, and recovering from incidents and errors are followed and documented.

About Regularly documenting an accurate and transparent account of identified and reported errors can enhance AI risk management activities., Examples include:

• how errors were identified, • incidents related to the error, • whether the error has been repaired, and • how repairs can be distributed to all impacted stakeholders and users.

[pp. 59-60]

Suggested Actions • Establish procedures to regularly share information about errors, incidents and negative impacts with relevant stakeholders, operators, practitioners and users, and impacted parties. • Maintain a database of reported errors, near-misses, incidents and negative impacts including date reported, number of reports, assessment of impact and severity, and responses. • Maintain a database of system changes, reason for change, and details of how the change was made, tested and deployed. • Maintain version history information and metadata to enable continuous improvement processes. • Verify that relevant AI actors responsible for identifying complex or emergent risks are properly resourced and empowered.

Transparency & Documentation

Organizations can document the following • What corrective actions has the entity taken to enhance the quality, accuracy, reliability, and representativeness of the data? • To what extent does the entity communicate its AI strategic goals and objectives to the community of stakeholders? How easily accessible and current is the information available to external stakeholders? • What type of information is accessible on the design, operations, and limitations of the AI system to external stakeholders, including end users, consumers, regulators, and individuals impacted by use of the AI system?

AI Transparency Resources • GAO-21-519SP: Artificial Intelligence: An Accountability Framework for Federal Agencies & Other Entities,

References Wei, M., & Zhou, Z. (2022). AI Ethics Issues in Real World: Evidence from AI Incident Database. ArXiv, abs/2206.07635.

McGregor, Sean. "Preventing repeated real world AI failures by cataloging incidents: The AI incident database." Proceedings of the AAAI Conference on Artificial Intelligence. Vol. 35. No. 17. 2021.

Macrae, Carl. "Learning from the failure of autonomous and intelligent systems: Accidents, safety, and sociotechnical sources of risk." Risk analysis 42.9 (2022): 1999-2025.

## MAP


[pp. 62-63]

Map

Context is established and understood.

MAP 1.1 Intended purpose, potentially beneficial uses, context-specific laws, norms and expectations, and prospective settings in which the AI system will be deployed are understood and documented. Considerations include: specific set or types of users along with their expectations; potential positive and negative impacts of system uses to individuals, communities, organizations, society, and the planet; assumptions and related limitations about AI system purposes; uses and risks across the development or product AI lifecycle; TEVV and system metrics.

About Highly accurate and optimized systems can cause harm. Relatedly, organizations should expect broadly deployed AI tools to be reused, repurposed, and potentially misused regardless of intentions.

AI actors can work collaboratively, and with external parties such as community groups, to help delineate the bounds of acceptable deployment, consider preferable alternatives, and identify principles and strategies to manage likely risks. Context mapping is the first step in this effort, and may include examination of the following:

• intended purpose and impact of system use. • concept of operations. • intended, prospective, and actual deployment setting. • requirements for system deployment and operation. • end user and operator expectations. • specific set or types of end users. • potential negative impacts to individuals, groups, communities, organizations, and society – or context-specific impacts such as legal requirements or impacts to the environment. • unanticipated, downstream, or other unknown contextual factors. • how AI system changes connect to impacts.

These types of processes can assist AI actors in understanding how limitations, constraints, and other realities associated with the deployment and use of AI technology can create impacts once they are deployed or operate in the real world. When coupled with the enhanced organizational culture resulting from the established policies and procedures in the Govern function, the Map function can provide opportunities to foster and instill new perspectives, activities, and skills for approaching risks and impacts.

Context mapping also includes discussion and consideration of non-AI or non-technology alternatives especially as related to whether the given context is narrow enough to manage

AI and its potential negative impacts. Non-AI alternatives may include capturing and evaluating information using semi-autonomous or mostly-manual methods.

[pp. 63-64]

Suggested Actions • Maintain awareness of industry, technical, and applicable legal standards. • Examine trustworthiness of AI system design and consider, non-AI solutions • Consider intended AI system design tasks along with unanticipated purposes in collaboration with human factors and socio-technical domain experts. • Define and document the task, purpose, minimum functionality, and benefits of the AI system to inform considerations about whether the utility of the project or its lack of. • Identify whether there are non-AI or non-technology alternatives that will lead to more trustworthy outcomes. • Examine how changes in system performance affect downstream events such as decision-making (e.g: changes in an AI model objective function create what types of impacts in how many candidates do/do not get a job interview). • Determine actions to map and track post-decommissioning stages of AI deployment and potential negative or positive impacts to individuals, groups and communities. • Determine the end user and organizational requirements, including business and technical requirements. • Determine and delineate the expected and acceptable AI system context of use, including:

• social norms • Impacted individuals, groups, and communities • potential positive and negative impacts to individuals, groups, communities, organizations, and society • operational environment

• Perform context analysis related to time frame, safety concerns, geographic area, physical environment, ecosystems, social environment, and cultural norms within the intended setting (or conditions that closely approximate the intended setting. • Gain and maintain awareness about evaluating scientific claims related to AI system performance and benefits before launching into system design. • Identify human-AI interaction and/or roles, such as whether the application will support or replace human decision making. • Plan for risks related to human-AI configurations, and document requirements, roles, and responsibilities for human oversight of deployed systems.

Transparency & Documentation

Organizations can document the following • To what extent is the output of each component appropriate for the operational context?

• Which AI actors are responsible for the decisions of the AI and is this person aware of the intended uses and limitations of the analytic? • Which AI actors are responsible for maintaining, re-verifying, monitoring, and updating this AI once deployed? • Who is the person(s) accountable for the ethical considerations across the AI lifecycle?

AI Transparency Resources • GAO-21-519SP: AI Accountability Framework for Federal Agencies & Other Entities, • “Stakeholders in Explainable AI,” Sep. 2018. • "Microsoft Responsible AI Standard, v2".

References

Socio-technical systems Andrew D. Selbst, danah boyd, Sorelle A. Friedler, et al. 2019. Fairness and Abstraction in Sociotechnical Systems. In Proceedings of the Conference on Fairness, Accountability, and Transparency (FAccT'19). Association for Computing Machinery, New York, NY, USA, 59–68.

[pp. 64-65]

Problem formulation Roel Dobbe, Thomas Krendl Gilbert, and Yonatan Mintz. 2021. Hard choices in artificial intelligence. Artificial Intelligence 300 (14 July 2021), 103555, ISSN 0004-3702.

Samir Passi and Solon Barocas. 2019. Problem Formulation and Fairness. In Proceedings of the Conference on Fairness, Accountability, and Transparency (FAccT'19). Association for Computing Machinery, New York, NY, USA, 39–48.

Context mapping Emilio Gómez-González and Emilia Gómez. 2020. Artificial intelligence in medicine and healthcare. Joint Research Centre (European Commission).

Sarah Spiekermann and Till Winkler. 2020. Value-based Engineering for Ethics by Design. arXiv:2004.13676.

Social Impact Lab. 2017. Framework for Context Analysis of Technologies in Social Change Projects (Draft v2.0).

Solon Barocas, Asia J. Biega, Margarita Boyarskaya, et al. 2021. Responsible computing during COVID-19 and beyond. Commun. ACM 64, 7 (July 2021), 30–32.

Identification of harms Harini Suresh and John V. Guttag. 2020. A Framework for Understanding Sources of Harm throughout the Machine Learning Life Cycle. arXiv:1901.10002.

Margarita Boyarskaya, Alexandra Olteanu, and Kate Crawford. 2020. Overcoming Failures of Imagination in AI Infused System Development and Deployment. arXiv:2011.13416.

Microsoft. Foundations of assessing harm. 2022.

Understanding and documenting limitations in ML Alexander D'Amour, Katherine Heller, Dan Moldovan, et al. 2020. Underspecification Presents Challenges for Credibility in Modern Machine Learning. arXiv:2011.03395.

Arvind Narayanan. "How to Recognize AI Snake Oil." Arthur Miller Lecture on Science and Ethics (2019).

Jessie J. Smith, Saleema Amershi, Solon Barocas, et al. 2022. REAL ML: Recognizing, Exploring, and Articulating Limitations of Machine Learning Research. arXiv:2205.08363.

Margaret Mitchell, Simone Wu, Andrew Zaldivar, et al. 2019. Model Cards for Model Reporting. In Proceedings of the Conference on Fairness, Accountability, and Transparency (FAT* '19). Association for Computing Machinery, New York, NY, USA, 220–229.

[pp. 65-66]

Matthew Arnold, Rachel K. E. Bellamy, Michael Hind, et al. 2019. FactSheets: Increasing Trust in AI Services through Supplier's Declarations of Conformity. arXiv:1808.07261.

Matthew J. Salganik, Ian Lundberg, Alexander T. Kindel, Caitlin E. Ahearn, Khaled Al- Ghoneim, Abdullah Almaatouq, Drew M. Altschul et al. "Measuring the Predictability of Life Outcomes with a Scientific Mass Collaboration." Proceedings of the National Academy of Sciences 117, No. 15 (2020): 8398-8403.

Michael A. Madaio, Luke Stark, Jennifer Wortman Vaughan, and Hanna Wallach. 2020. Co- Designing Checklists to Understand Organizational Challenges and Opportunities around Fairness in AI. In Proceedings of the 2020 CHI Conference on Human Factors in Computing Systems (CHI ‘20). Association for Computing Machinery, New York, NY, USA, 1–14.

Timnit Gebru, Jamie Morgenstern, Briana Vecchione, et al. 2021. Datasheets for Datasets. arXiv:1803.09010.

Bender, E. M., Friedman, B. & McMillan-Major, A., (2022). A Guide for Writing Data Statements for Natural Language Processing. University of Washington. Accessed July 14, 2022.

Meta AI. System Cards, a new resource for understanding how AI systems work, 2021.

When not to deploy Solon Barocas, Asia J. Biega, Benjamin Fish, et al. 2020. When not to design, build, or deploy. In Proceedings of the 2020 Conference on Fairness, Accountability, and Transparency (FAT* '20). Association for Computing Machinery, New York, NY, USA, 695.

Post-decommission Upol Ehsan, Ranjit Singh, Jacob Metcalf and Mark O. Riedl. “The Algorithmic Imprint.” Proceedings of the 2022 ACM Conference on Fairness, Accountability, and Transparency (2022).

Statistical balance Ziad Obermeyer, Brian Powers, Christine Vogeli, and Sendhil Mullainathan. 2019. Dissecting racial bias in an algorithm used to manage the health of populations. Science 366, 6464 (25 Oct. 2019), 447-453.

Assessment of science in AI Arvind Narayanan. How to recognize AI snake oil.

Emily M. Bender. 2022. On NYT Magazine on AI: Resist the Urge to be Impressed. (April 17, 2022).

[pp. 66-67]

MAP 1.2 Inter-disciplinary AI actors, competencies, skills and capacities for establishing context reflect demographic diversity and broad domain and user experience expertise, and their participation is documented. Opportunities for interdisciplinary collaboration are prioritized.

About Successfully mapping context requires a team of AI actors with a diversity of experience, expertise, abilities and backgrounds, and with the resources and independence to engage in critical inquiry.

Having a diverse team contributes to more broad and open sharing of ideas and assumptions about the purpose and function of the technology being designed and developed – making these implicit aspects more explicit. The benefit of a diverse staff in managing AI risks is not the beliefs or presumed beliefs of individual workers, but the behavior that results from a collective perspective. An environment which fosters critical inquiry creates opportunities to surface problems and identify existing and emergent risks.

Suggested Actions • Establish interdisciplinary teams to reflect a wide range of skills, competencies, and capabilities for AI efforts. Verify that team membership includes demographic diversity, broad domain expertise, and lived experiences. Document team composition. • Create and empower interdisciplinary expert teams to capture, learn, and engage the interdependencies of deployed AI systems and related terminologies and concepts from disciplines outside of AI practice such as law, sociology, psychology, anthropology, public policy, systems design, and engineering.

Transparency & Documentation

Organizations can document the following • To what extent do the teams responsible for developing and maintaining the AI system reflect diverse opinions, backgrounds, experiences, and perspectives?

• Did the entity document the demographics of those involved in the design and development of the AI system to capture and communicate potential biases inherent to the development process, according to forum participants? • What specific perspectives did stakeholders share, and how were they integrated across the design, development, deployment, assessment, and monitoring of the AI system? • To what extent has the entity addressed stakeholder perspectives on the potential negative impacts of the AI system on end users and impacted populations? • What type of information is accessible on the design, operations, and limitations of the AI system to external stakeholders, including end users, consumers, regulators, and individuals impacted by use of the AI system? • Did your organization address usability problems and test whether user interfaces served their intended purposes? Consulting the community or end users at the earliest stages of development to ensure there is transparency on the technology used and how it is deployed.

AI Transparency Resources • GAO-21-519SP: AI Accountability Framework for Federal Agencies & Other Entities. • WEF Model AI Governance Framework Assessment 2020. • WEF Companion to the Model AI Governance Framework- 2020. • AI policies and initiatives, in Artificial Intelligence in Society, OECD, 2019.

References Sina Fazelpour and Maria De-Arteaga. 2022. Diversity in sociotechnical machine learning systems. Big Data & Society 9, 1 (Jan. 2022).

Microsoft Community Jury , Azure Application Architecture Guide.

[pp. 67-68]

Fernando Delgado, Stephen Yang, Michael Madaio, Qian Yang. (2021). Stakeholder Participation in AI: Beyond "Add Diverse Stakeholders and Stir".

Kush Varshney, Tina Park, Inioluwa Deborah Raji, Gaurush Hiranandani, Narasimhan Harikrishna, Oluwasanmi Koyejo, Brianna Richardson, and Min Kyung Lee. Participatory specification of trustworthy machine learning, 2021.

Donald Martin, Vinodkumar Prabhakaran, Jill A. Kuhlberg, Andrew Smart and William S. Isaac. “Participatory Problem Formulation for Fairer Machine Learning Through Community Based System Dynamics”, ArXiv abs/2005.07572 (2020).

MAP 1.3 The organization’s mission and relevant goals for the AI technology are understood and documented.

About Defining and documenting the specific business purpose of an AI system in a broader context of societal values helps teams to evaluate risks and increases the clarity of “go/no- go” decisions about whether to deploy.

Trustworthy AI technologies may present a demonstrable business benefit beyond implicit or explicit costs, provide added value, and don't lead to wasted resources. Organizations can feel confident in performing risk avoidance if the implicit or explicit risks outweigh the advantages of AI systems, and not implementing an AI solution whose risks surpass potential benefits.

For example, making AI systems more equitable can result in better managed risk, and can help enhance consideration of the business value of making inclusively designed, accessible and more equitable AI systems.

Suggested Actions • Build transparent practices into AI system development processes. • Review the documented system purpose from a socio-technical perspective and in consideration of societal values. • Determine possible misalignment between societal values and stated organizational principles and code of ethics. • Flag latent incentives that may contribute to negative impacts. • Evaluate AI system purpose in consideration of potential risks, societal values, and stated organizational principles.

Transparency & Documentation

Organizations can document the following • How does the AI system help the entity meet its goals and objectives? • How do the technical specifications and requirements align with the AI system’s goals and objectives? • To what extent is the output appropriate for the operational context?

AI Transparency Resources • Assessment List for Trustworthy AI (ALTAI) - The High-Level Expert Group on AI – 2019, [LINK](https://altai.insight-centre.org/), • Including Insights from the Comptroller General’s Forum on the Oversight of Artificial Intelligence An Accountability Framework for Federal Agencies and Other Entities, 2021,

References M.S. Ackerman (2000). The Intellectual Challenge of CSCW: The Gap Between Social Requirements and Technical Feasibility. Human–Computer Interaction, 15, 179 - 203.

[pp. 69-70]

McKane Andrus, Sarah Dean, Thomas Gilbert, Nathan Lambert, Tom Zick (2021). AI Development for the Public Interest: From Abstraction Traps to Sociotechnical Risks.

Abeba Birhane, Pratyusha Kalluri, Dallas Card, et al. 2022. The Values Encoded in Machine Learning Research. arXiv:2106.15590.

Board of Governors of the Federal Reserve System. SR 11-7: Guidance on Model Risk Management. (April 4, 2011).

Iason Gabriel, Artificial Intelligence, Values, and Alignment. Minds & Machines 30, 411–437 (2020).

PEAT “Business Case for Equitable AI”.

MAP 1.4 The business value or context of business use has been clearly defined or – in the case of assessing existing AI systems – re-evaluated.

About Socio-technical AI risks emerge from the interplay between technical development decisions and how a system is used, who operates it, and the social context into which it is deployed. Addressing these risks is complex and requires a commitment to understanding how contextual factors may interact with AI lifecycle actions. One such contextual factor is how organizational mission and identified system purpose create incentives within AI system design, development, and deployment tasks that may result in positive and negative impacts. By establishing comprehensive and explicit enumeration of AI systems’ context of of business use and expectations, organizations can identify and manage these types of risks.

Suggested Actions • Document business value or context of business use • Reconcile documented concerns about the system’s purpose within the business context of use compared to the organization’s stated values, mission statements, social responsibility commitments, and AI principles. • Reconsider the design, implementation strategy, or deployment of AI systems with potential impacts that do not reflect institutional values.

Transparency & Documentation

Organizations can document the following • What goals and objectives does the entity expect to achieve by designing, developing, and/or deploying the AI system? • To what extent are the system outputs consistent with the entity’s values and principles to foster public trust and equity? • To what extent are the metrics consistent with system goals, objectives, and constraints, including ethical and compliance considerations?

AI Transparency Resources • GAO-21-519SP: AI Accountability Framework for Federal Agencies & Other Entities. • Intel.gov: AI Ethics Framework for Intelligence Community - 2020. • WEF Model AI Governance Framework Assessment 2020.

References Algorithm Watch. AI Ethics Guidelines Global Inventory.

Ethical OS toolkit.

Emanuel Moss and Jacob Metcalf. 2020. Ethics Owners: A New Model of Organizational Responsibility in Data-Driven Technology Companies. Data & Society Research Institute.

Future of Life Institute. Asilomar AI Principles.


---

[previous part](text-004.md) | [source overview](overview.md) | [next part](text-006.md)

[^original]: NIST, "NIST AI RMF Playbook" (2024-08-02). https://airc.nist.gov/airmf-resources/playbook/
