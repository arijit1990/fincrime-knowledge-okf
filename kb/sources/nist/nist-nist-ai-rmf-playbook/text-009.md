---
type: Source Text
title: NIST AI RMF Playbook - part 9 of 12 (pp. 107-119)
description: 'Verbatim extracted text, pp. 107-119: MEASURE'
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
part: 9
parts_total: 12
content_mode: full_text
generated:
  by: process:fincrime-kb-build
  at: '2026-11-22T14:32:20Z'
verified:
- by: process:kb-validate/verbatim-coverage
  at: '2026-11-22T14:32:20Z'
sources:
- id: original
  resource: https://airc.nist.gov/airmf-resources/playbook/
  title: NIST AI RMF Playbook
  author: org:nist
  last_modified: '2024-08-02T00:00:00Z'
---

# NIST AI RMF Playbook

[previous part](text-008.md) | [source overview](overview.md) | [next part](text-010.md)

> Verbatim text extracted from the original (NIST, 2024-08-02), part 9 of 12, pp. 107-119. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **industry practice**.[^original]

## MEASURE


[pp. 107-108]

Marco Gerardi, Katarzyna Barud, Marie-Catherine Wagner, Nikolaus Forgo, Francesca Fallucchi, Noemi Scarpato, Fiorella Guadagni, and Fabio Massimo Zanzotto. "Active Informed Consent to Boost the Application of Machine Learning in Medicine." arXiv preprint, submitted September 27, 2022.

Shari Trewin. "AI Fairness for People with Disabilities: Point of View." arXiv preprint, submitted November 26, 2018.

Andrea Brennen, Ryan Ashley, Ricardo Calix, JJ Ben-Joseph, George Sieniawski, Mona Gogia, and BNH.AI. AI Assurance Audit of RoBERTa, an Open source, Pretrained Large Language Model. IQT Labs, December 2022.

MEASURE 2.3 AI system performance or assurance criteria are measured qualitatively or quantitatively and demonstrated for conditions similar to deployment setting(s). Measures are documented.

About The current risk and impact environment suggests AI system performance estimates are insufficient and require a deeper understanding of deployment context of use. Computationally focused performance testing and evaluation schemes are restricted to test data sets and in silico techniques. These approaches do not directly evaluate risks and impacts in real world environments and can only predict what might create impact based on an approximation of expected AI use. To properly manage risks, more direct information is necessary to understand how and under what conditions deployed AI creates impacts, who is most likely to be impacted, and what that experience is like.

Suggested Actions • Conduct regular and sustained engagement with potentially impacted communities • Maintain a demographically diverse and multidisciplinary and collaborative internal team

• Regularly test and evaluate systems in non-optimized conditions, and in collaboration with AI actors in user interaction and user experience (UI/UX) roles. • Evaluate feedback from stakeholder engagement activities, in collaboration with human factors and socio-technical experts. • Collaborate with socio-technical, human factors, and UI/UX experts to identify notable characteristics in context of use that can be translated into system testing scenarios. • Measure AI systems prior to deployment in conditions similar to expected scenarios. • Measure and document performance criteria such as validity (false positive rate, false negative rate, etc.) and efficiency (training times, prediction latency, etc.) related to ground truth within the deployment context of use. • Measure assurance criteria such as AI actor competency and experience. • Document differences between measurement setting and the deployment environment(s).

Transparency & Documentation

[pp. 108-109]

Organizations can document the following • What experiments were initially run on this dataset? To what extent have experiments on the AI system been documented? • To what extent does the system/entity consistently measure progress towards stated goals and objectives? • How will the appropriate performance metrics, such as accuracy, of the AI be monitored after the AI is deployed? How much distributional shift or model drift from baseline performance is acceptable? • As time passes and conditions change, is the training data still representative of the operational environment? • What testing, if any, has the entity conducted on theAI system to identify errors and limitations (i.e.adversarial or stress testing)?

AI Transparency Resources • Artificial Intelligence Ethics Framework For The Intelligence Community. • WEF Companion to the Model AI Governance Framework- WEF - Companion to the Model AI Governance Framework, 2020. • Datasheets for Datasets.

References Trevor Hastie, Robert Tibshirani, and Jerome Friedman. The Elements of Statistical Learning: Data Mining, Inference, and Prediction. 2nd ed. Springer-Verlag, 2009.

Jessica Zosa Forde, A. Feder Cooper, Kweku Kwegyir-Aggrey, Chris De Sa, and Michael Littman. "Model Selection's Disparate Impact in Real-World Deep Learning Applications." arXiv preprint, submitted September 7, 2021.

Inioluwa Deborah Raji, I. Elizabeth Kumar, Aaron Horowitz, and Andrew Selbst. “The Fallacy of AI Functionality.” FAccT '22: 2022 ACM Conference on Fairness, Accountability, and Transparency, June 2022, 959–72.

Amandalynne Paullada, Inioluwa Deborah Raji, Emily M. Bender, Emily Denton, and Alex Hanna. “Data and Its (Dis)Contents: A Survey of Dataset Development and Use in Machine Learning Research.” Patterns 2, no. 11 (2021): 100336.

Christopher M. Bishop. Pattern Recognition and Machine Learning. New York: Springer, 2006.

Md Johirul Islam, Giang Nguyen, Rangeet Pan, and Hridesh Rajan. "A Comprehensive Study on Deep Learning Bug Characteristics." arXiv preprint, submitted June 3, 2019.

Swaroop Mishra, Anjana Arunkumar, Bhavdeep Sachdeva, Chris Bryan, and Chitta Baral. "DQI: Measuring Data Quality in NLP." arXiv preprint, submitted May 2, 2020.

Doug Wielenga. "Paper 073-2007: Identifying and Overcoming Common Data Mining Mistakes." SAS Global Forum 2007: Data Mining and Predictive Modeling, SAS Institute, 2007.

[pp. 109-110]

Software Resources • Drifter library (performance assessment) • Manifold library (performance assessment) • MLextend library (performance assessment) • PiML library (explainable models, performance assessment) • SALib library (performance assessment) • What-If Tool (performance assessment)

MEASURE 2.4 The functionality and behavior of the AI system and its components – as identified in the MAP function – are monitored when in production.

About AI systems may encounter new issues and risks while in production as the environment evolves over time. This effect, often referred to as “drift”, means AI systems no longer meet the assumptions and limitations of the original design. Regular monitoring allows AI Actors to monitor the functionality and behavior of the AI system and its components – as identified in the MAP function - and enhance the speed and efficacy of necessary system interventions.

Suggested Actions • Monitor and document how metrics and performance indicators observed in production differ from the same metrics collected during pre-deployment testing. When differences are observed, consider error propagation and feedback loop risks.

• Utilize hypothesis testing or human domain expertise to measure monitored distribution differences in new input or output data relative to test environments • Monitor for anomalies using approaches such as control limits, confidence intervals, integrity constraints and ML algorithms. When anomalies are observed, consider error propagation and feedback loop risks. • Verify alerts are in place for when distributions in new input data or generated predictions observed in production differ from pre-deployment test outcomes, or when anomalies are detected. • Assess the accuracy and quality of generated outputs against new collected ground- truth information as it becomes available. • Utilize human review to track processing of unexpected data and reliability of generated outputs; warn system users when outputs may be unreliable. Verify that human overseers responsible for these processes have clearly defined responsibilities and training for specified tasks. • Collect uses cases from the operational environment for system testing and monitoring activities in accordance with organizational policies and regulatory or disciplinary requirements (e.g. informed consent, institutional review board approval, human research protections),

Transparency & Documentation

Organizations can document the following • To what extent is the output of each component appropriate for the operational context? • What justifications, if any, has the entity provided for the assumptions, boundaries, and limitations of the AI system? • How will the appropriate performance metrics, such as accuracy, of the AI be monitored after the AI is deployed? • As time passes and conditions change, is the training data still representative of the operational environment?

AI Transparency Resources • GAO-21-519SP - Artificial Intelligence: An Accountability Framework for Federal Agencies & Other Entities. • Artificial Intelligence Ethics Framework For The Intelligence Community.

References Luca Piano, Fabio Garcea, Valentina Gatteschi, Fabrizio Lamberti, and Lia Morra. “Detecting Drift in Deep Learning: A Methodology Primer.” IT Professional 24, no. 5 (2022): 53–60.

[pp. 110-112]

Larysa Visengeriyeva, et al. “Awesome MLOps.“ GitHub.

MEASURE 2.5 The AI system to be deployed is demonstrated to be valid and reliable. Limitations of the generalizability beyond the conditions under which the technology was developed are documented.

About An AI system that is not validated or that fails validation may be inaccurate or unreliable or may generalize poorly to data and settings beyond its training, creating and increasing AI risks and reducing trustworthiness. AI Actors can improve system validity by creating processes for exploring and documenting system limitations. This includes broad consideration of purposes and uses for which the system was not designed.

Validation risks include the use of proxies or other indicators that are often constructed by AI development teams to operationalize phenomena that are either not directly observable or measurable (e.g, fairness, hireability, honesty, propensity to commit a crime). Teams can mitigate these risks by demonstrating that the indicator is measuring the concept it claims to measure (also known as construct validity). Without this and other types of validation, various negative properties or impacts may go undetected, including the presence of confounding variables, potential spurious correlations, or error propagation and its potential impact on other interconnected systems.

Suggested Actions • Define the operating conditions and socio-technical context under which the AI system will be validated. • Define and document processes to establish the system’s operational conditions and limits. • Establish or identify, and document approaches to measure forms of validity, including:

• construct validity (the test is measuring the concept it claims to measure) • internal validity (relationship being tested is not influenced by other factors or variables) • external validity (results are generalizable beyond the training condition) • the use of experimental design principles and statistical analyses and modeling.

• Assess and document system variance. Standard approaches include confidence intervals, standard deviation, standard error, bootstrapping, or cross-validation. • Establish or identify, and document robustness measures. • Establish or identify, and document reliability measures. • Establish practices to specify and document the assumptions underlying measurement models to ensure proxies accurately reflect the concept being measured. • Utilize standard software testing approaches (e.g. unit, integration, functional and chaos testing, computer-generated test cases, etc.) • Utilize standard statistical methods to test bias, inferential associations, correlation, and covariance in adopted measurement models.

• Utilize standard statistical methods to test variance and reliability of system outcomes. • Monitor operating conditions for system performance outside of defined limits. • Identify TEVV approaches for exploring AI system limitations, including testing scenarios that differ from the operational environment. Consult experts with knowledge of specific context of use. • Define post-alert actions. Possible actions may include:

• alerting other relevant AI actors before action, • requesting subsequent human review of action, • alerting downstream users and stakeholder that the system is operating outside it’s defined validity limits, • tracking and mitigating possible error propagation • action logging

[pp. 112-113]

• Log input data and relevant system configuration information whenever there is an attempt to use the system beyond its well-defined range of system validity. • Modify the system over time to extend its range of system validity to new operating conditions.

Transparency & Documentation

Organizations can document the following • What testing, if any, has the entity conducted on theAI system to identify errors and limitations (i.e.adversarial or stress testing)? • Given the purpose of this AI, what is an appropriate interval for checking whether it is still accurate, unbiased, explainable, etc.? What are the checks for this model? • How has the entity identified and mitigated potential impacts of bias in the data, including inequitable or discriminatory outcomes? • To what extent are the established procedures effective in mitigating bias, inequity, and other concerns resulting from the system? • What goals and objectives does the entity expect to achieve by designing, developing, and/or deploying the AI system?

AI Transparency Resources • GAO-21-519SP - Artificial Intelligence: An Accountability Framework for Federal Agencies & Other Entities.

References Abigail Z. Jacobs and Hanna Wallach. “Measurement and Fairness.” FAccT '21: Proceedings of the 2021 ACM Conference on Fairness, Accountability, and Transparency, March 2021, 375–85.

Debugging Machine Learning Models. Proceedings of ICLR 2019 Workshop, May 6, 2019, New Orleans, Louisiana.

Patrick Hall. “Strategies for Model Debugging.” Towards Data Science, November 8, 2019.

Suchi Saria and Adarsh Subbaswamy. "Tutorial: Safe and Reliable Machine Learning." arXiv preprint, submitted April 15, 2019.

Google Developers. “Overview of Debugging ML Models.” Google Developers Machine Learning Foundational Courses, n.d.

R. Mohanani, I. Salman, B. Turhan, P. Rodríguez and P. Ralph, "Cognitive Biases in Software Engineering: A Systematic Mapping Study," in IEEE Transactions on Software Engineering, vol. 46, no. 12, pp. 1318-1339, Dec. 2020,

Software Resources • Drifter library (performance assessment) • Manifold library (performance assessment) • MLextend library (performance assessment) • PiML library (explainable models, performance assessment) • SALib library (performance assessment) • What-If Tool (performance assessment)

MEASURE 2.6 AI system is evaluated regularly for safety risks – as identified in the MAP function. The AI system to be deployed is demonstrated to be safe, its residual negative risk does not exceed the risk tolerance, and can fail safely, particularly if made to operate beyond its knowledge limits. Safety metrics implicate system reliability and robustness, real-time monitoring, and response times for AI system failures.

[pp. 113-114]

About Many AI systems are being introduced into settings such as transportation, manufacturing or security, where failures may give rise to various physical or environmental harms. AI systems that may endanger human life, health, property or the environment are tested thoroughly prior to deployment, and are regularly evaluated to confirm the system is safe during normal operations, and in settings beyond its proposed use and knowledge limits.

Measuring activities for safety often relate to exhaustive testing in development and deployment contexts, understanding the limits of a system’s reliable, robust, and safe behavior, and real-time monitoring of various aspects of system performance. These activities are typically conducted along with other risk mapping, management, and governance tasks such as avoiding past failed designs, establishing and rehearsing incident response plans that enable quick responses to system problems, the instantiation of redundant functionality to cover failures, and transparent and accountable governance. System safety incidents or failures are frequently reported to be related to organizational dynamics and culture. Independent auditors may bring important independent perspectives for reviewing evidence of AI system safety.

Suggested Actions • Thoroughly measure system performance in development and deployment contexts, and under stress conditions.

• Employ test data assessments and simulations before proceeding to production testing. Track multiple performance quality and error metrics. • Stress-test system performance under likely scenarios (e.g., concept drift, high load) and beyond known limitations, in consultation with domain experts. • Test the system under conditions similar to those related to past known incidents or near-misses and measure system performance and safety characteristics • Apply chaos engineering approaches to test systems in extreme conditions and gauge unexpected responses. • Document the range of conditions under which the system has been tested and demonstrated to fail safely.

• Measure and monitor system performance in real-time to enable rapid response when AI system incidents are detected. • Collect pertinent safety statistics (e.g., out-of-range performance, incident response times, system down time, injuries, etc.) in anticipation of potential information sharing with impacted communities or as required by AI system oversight personnel. • Align measurement to the goal of continuous improvement. Seek to increase the range of conditions under which the system is able to fail safely through system modifications in response to in-production testing and events. • Document, practice and measure incident response plans for AI system incidents, including measuring response and down times. • Compare documented safety testing and monitoring information with established risk tolerances on an on-going basis. • Consult MANAGE for detailed information related to managing safety risks.

Transparency & Documentation

[pp. 114-115]

Organizations can document the following • What testing, if any, has the entity conducted on the AI system to identify errors and limitations (i.e.adversarial or stress testing)? • To what extent has the entity documented the AI system’s development, testing methodology, metrics, and performance outcomes? • Did you establish mechanisms that facilitate the AI system’s auditability (e.g. traceability of the development process, the sourcing of training data and the logging of the AI system’s processes, outcomes, positive and negative impact)? • Did you ensure that the AI system can be audited by independent third parties? • Did you establish a process for third parties (e.g. suppliers, end-users, subjects, distributors/vendors or workers) to report potential vulnerabilities, risks or biases in the AI system?

AI Transparency Resources • GAO-21-519SP - Artificial Intelligence: An Accountability Framework for Federal Agencies & Other Entities. • Artificial Intelligence Ethics Framework For The Intelligence Community.

References AI Incident Database. 2022.

AIAAIC Repository. 2022.

Netflix. Chaos Monkey.

IBM. “IBM's Principles of Chaos Engineering.” IBM, n.d.

Suchi Saria and Adarsh Subbaswamy. "Tutorial: Safe and Reliable Machine Learning." arXiv preprint, submitted April 15, 2019.

Daniel Kang, Deepti Raghavan, Peter Bailis, and Matei Zaharia. "Model assertions for monitoring and improving ML models." Proceedings of Machine Learning and Systems 2 (2020): 481-496.

Larysa Visengeriyeva, et al. “Awesome MLOps.“ GitHub.

McGregor, S., Paeth, K., & Lam, K.T. (2022). Indexing AI Risks with Incidents, Issues, and Variants. ArXiv, abs/2211.10384.

MEASURE 2.7 AI system security and resilience – as identified in the MAP function – are evaluated and documented.

About AI systems, as well as the ecosystems in which they are deployed, may be said to be resilient if they can withstand unexpected adverse events or unexpected changes in their environment or use – or if they can maintain their functions and structure in the face of internal

and external change and degrade safely and gracefully when this is necessary. Common security concerns relate to adversarial examples, data poisoning, and the exfiltration of models, training data, or other intellectual property through AI system endpoints. AI systems that can maintain confidentiality, integrity, and availability through protection mechanisms that prevent unauthorized access and use may be said to be secure.

Security and resilience are related but distinct characteristics. While resilience is the ability

to return to normal function after an unexpected adverse event, security includes resilience

but also encompasses protocols to avoid, protect against, respond to, or recover

[pp. 116-117]

from attacks. Resilience relates to robustness and encompasses unexpected or adversarial use (or abuse or misuse) of the model or data.

Suggested Actions • Establish and track AI system security tests and metrics (e.g., red-teaming activities, frequency and rate of anomalous events, system down-time, incident response times, time-to-bypass, etc.). • Use red-team exercises to actively test the system under adversarial or stress conditions, measure system response, assess failure modes or determine if system can return to normal function after an unexpected adverse event. • Document red-team exercise results as part of continuous improvement efforts, including the range of security test conditions and results. • Use red-teaming exercises to evaluate potential mismatches between claimed and actual system performance. • Use countermeasures (e.g, authentication, throttling, differential privacy, robust ML approaches) to increase the range of security conditions under which the system is able to return to normal function. • Modify system security procedures and countermeasures to increase robustness and resilience to attacks in response to testing and events experienced in production. • Verify that information about errors and attack patterns is shared with incident databases, other organizations with similar systems, and system users and stakeholders (MANAGE-4.1). • Develop and maintain information sharing practices with AI actors from other organizations to learn from common attacks. • Verify that third party AI resources and personnel undergo security audits and screenings. Risk indicators may include failure of third parties to provide relevant security information. • Utilize watermarking technologies as a deterrent to data and model extraction attacks.

Transparency & Documentation

Organizations can document the following • To what extent does the plan specifically address risks associated with acquisition, procurement of packaged software from vendors, cybersecurity controls, computational infrastructure, data, data science, deployment mechanics, and system failure? • What assessments has the entity conducted on data security and privacy impacts associated with the AI system? • What processes exist for data generation, acquisition/collection, security, maintenance, and dissemination? • What testing, if any, has the entity conducted on the AI system to identify errors and limitations (i.e. adversarial or stress testing)? • If a third party created the AI, how will you ensure a level of explainability or interpretability?

AI Transparency Resources • GAO-21-519SP - Artificial Intelligence: An Accountability Framework for Federal Agencies & Other Entities. • Artificial Intelligence Ethics Framework For The Intelligence Community.

References Matthew P. Barrett. “Framework for Improving Critical Infrastructure Cybersecurity Version 1.1.” National Institute of Standards and Technology (NIST), April 16, 2018.

Nicolas Papernot. "A Marauder's Map of Security and Privacy in Machine Learning." arXiv preprint, submitted on November 3, 2018.

[pp. 117-118]

Gary McGraw, Harold Figueroa, Victor Shepardson, and Richie Bonett. “BIML Interactive Machine Learning Risk Framework.” Berryville Institute of Machine Learning (BIML), 2022.

Mitre Corporation. “Mitre/Advmlthreatmatrix: Adversarial Threat Landscape for AI Systems.” GitHub, 2023.

National Institute of Standards and Technology (NIST). “Cybersecurity Framework.” NIST, 2023.

Upol Ehsan, Q. Vera Liao, Samir Passi, Mark O. Riedl, and Hal Daumé. 2024. Seamful XAI: Operationalizing Seamful Design in Explainable AI. Proc. ACM Hum.-Comput. Interact. 8, CSCW1, Article 119. https://doi.org/10.1145/3637396

Software Resources • adversarial-robustness-toolbox • counterfit • foolbox • ml_privacy_meter • robustness • tensorflow/privacy • projectGuardRail

MEASURE 2.8 Risks associated with transparency and accountability – as identified in the MAP function – are examined and documented.

About Transparency enables meaningful visibility into entire AI pipelines, workflows, processes or organizations and decreases information asymmetry between AI developers and operators and other AI Actors and impacted communities. Transparency is a central element of effective AI risk management that enables insight into how an AI system is working, and the ability to address risks if and when they emerge. The ability for system users, individuals, or impacted communities to seek redress for incorrect or problematic AI system outcomes is

one control for transparency and accountability. Higher level recourse processes are typically enabled by lower level implementation efforts directed at explainability and interpretability functionality. See Measure 2.9.

Transparency and accountability across organizations and processes is crucial to reducing AI risks. Accountable leadership – whether individuals or groups – and transparent roles, responsibilities, and lines of communication foster and incentivize quality assurance and risk management activities within organizations.

Lack of transparency complicates measurement of trustworthiness and whether AI systems or organizations are subject to effects of various individual and group biases and design blindspots and could lead to diminished user, organizational and community trust, and decreased overall system value. Enstating accountable and transparent organizational structures along with documenting system risks can enable system improvement and risk management efforts, allowing AI actors along the lifecycle to identify errors, suggest improvements, and figure out new ways to contextualize and generalize AI system features and outcomes.

[pp. 118-119]

Suggested Actions • Instrument the system for measurement and tracking, e.g., by maintaining histories, audit logs and other information that can be used by AI actors to review and evaluate possible sources of error, bias, or vulnerability. • Calibrate controls for users in close collaboration with experts in user interaction and user experience (UI/UX), human computer interaction (HCI), and/or human-AI teaming. • Test provided explanations for calibration with different audiences including operators, end users, decision makers and decision subjects (individuals for whom decisions are being made), and to enable recourse for consequential system decisions that affect end users or subjects. • Measure and document human oversight of AI systems:

• Document the degree of oversight that is provided by specified AI actors regarding AI system output. • Maintain statistics about downstream actions by end users and operators such as system overrides. • Maintain statistics about and document reported errors or complaints, time to respond, and response types. • Maintain and report statistics about adjudication activities.

• Track, document, and measure organizational accountability regarding AI systems via policy exceptions and escalations, and document “go” and “no/go” decisions made by accountable parties. • Track and audit the effectiveness of organizational mechanisms related to AI risk management, including:

• Lines of communication between AI actors, executive leadership, users and impacted communities. • Roles and responsibilities for AI actors and executive leadership. • Organizational accountability roles, e.g., chief model risk officers, AI oversight committees, responsible or ethical AI directors, etc.

Transparency & Documentation

Organizations can document the following • To what extent has the entity clarified the roles, responsibilities, and delegated authorities to relevant stakeholders? • What are the roles, responsibilities, and delegation of authorities of personnel involved in the design, development, deployment, assessment and monitoring of the AI system? • Who is accountable for the ethical considerations during all stages of the AI lifecycle? • Who will be responsible for maintaining, re-verifying, monitoring, and updating this AI once deployed? • Are the responsibilities of the personnel involved in the various AI governance processes clearly defined?

AI Transparency Resources • GAO-21-519SP - Artificial Intelligence: An Accountability Framework for Federal Agencies & Other Entities. • Artificial Intelligence Ethics Framework For The Intelligence Community.

References National Academies of Sciences, Engineering, and Medicine. Human-AI Teaming: State-of- the-Art and Research Needs. 2022.

Inioluwa Deborah Raji and Jingying Yang. "ABOUT ML: Annotation and Benchmarking on Understanding and Transparency of Machine Learning Lifecycles." arXiv preprint, submitted January 8, 2020.

Andrew Smith. "Using Artificial Intelligence and Algorithms." Federal Trade Commission Business Blog, April 8, 2020.

Board of Governors of the Federal Reserve System. “SR 11-7: Guidance on Model Risk Management.” April 4, 2011.


---

[previous part](text-008.md) | [source overview](overview.md) | [next part](text-010.md)

[^original]: NIST, "NIST AI RMF Playbook" (2024-08-02). https://airc.nist.gov/airmf-resources/playbook/
