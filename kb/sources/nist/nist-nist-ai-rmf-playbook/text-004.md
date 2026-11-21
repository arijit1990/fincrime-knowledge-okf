---
type: Source Text
title: NIST AI RMF Playbook - part 4 of 12 (pp. 44-56)
description: 'Verbatim extracted text, pp. 44-56: MANAGE'
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
part: 4
parts_total: 12
content_mode: full_text
generated:
  by: process:fincrime-kb-build
  at: '2026-11-21T23:42:13Z'
verified:
- by: process:kb-validate/verbatim-coverage
  at: '2026-11-21T23:42:13Z'
sources:
- id: original
  resource: https://airc.nist.gov/airmf-resources/playbook/
  title: NIST AI RMF Playbook
  author: org:nist
  last_modified: '2024-08-02T00:00:00Z'
---

# NIST AI RMF Playbook

[previous part](text-003.md) | [source overview](overview.md) | [next part](text-005.md)

> Verbatim text extracted from the original (NIST, 2024-08-02), part 4 of 12, pp. 44-56. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **industry practice**.[^original]

## MANAGE


[pp. 44-45]

Organizations can document the following • Are mechanisms in place to evaluate whether internal teams are empowered and resourced to effectively carry out risk management functions? • How will user and other forms of stakeholder engagement be integrated into risk management processes?

AI Transparency Resources • Artificial Intelligence Ethics Framework For The Intelligence Community. • Datasheets for Datasets. • GAO-21-519SP - Artificial Intelligence: An Accountability Framework for Federal Agencies & Other Entities.

References Board of Governors of the Federal Reserve System. SR 11-7: Guidance on Model Risk Management. (April 4, 2011).

David Wright. 2013. Making Privacy Impact Assessments More Effective. The Information Society, 29 (Oct 2013), 307-315.

Margaret Mitchell, Simone Wu, Andrew Zaldivar, et al. 2019. Model Cards for Model Reporting. In Proceedings of the Conference on Fairness, Accountability, and Transparency (FAT* '19). Association for Computing Machinery, New York, NY, USA, 220–229.

Office of the Comptroller of the Currency. 2021. Comptroller's Handbook: Model Risk Management, Version 1.0, August 2021.

Timnit Gebru, Jamie Morgenstern, Briana Vecchione, et al. 2021. Datasheets for Datasets. arXiv:1803.09010.

MANAGE 2.2 Mechanisms are in place and applied to sustain the value of deployed AI systems.

About System performance and trustworthiness may evolve and shift over time, once an AI system is deployed and put into operation. This phenomenon, generally known as drift, can degrade the value of the AI system to the organization and increase the likelihood of negative impacts. Regular monitoring of AI systems’ performance and trustworthiness enhances organizations’ ability to detect and respond to drift, and thus sustain an AI system’s value once deployed. Processes and mechanisms for regular monitoring address system functionality and behavior - as well as impacts and alignment with the values and norms within the specific context of use. For example, considerations regarding impacts on personal or public safety or privacy may include limiting high speeds when operating autonomous vehicles or restricting illicit content recommendations for minors.

Regular monitoring activities can enable organizations to systematically and proactively identify emergent risks and respond according to established protocols and metrics. Options for organizational responses include 1) avoiding the risk, 2)accepting the risk, 3) mitigating the risk, or 4) transferring the risk. Each of these actions require planning and resources. Organizations are encouraged to establish risk management protocols with consideration of the trustworthiness characteristics, the deployment context, and real world impacts.

Suggested Actions • Establish risk controls considering trustworthiness characteristics, including:

[pp. 45-47]

• Data management, quality, and privacy (e.g. minimization, rectification or deletion requests) controls as part of organizational data governance policies. • Machine learning and end-point security countermeasures (e.g., robust models, differential privacy, authentication, throttling). • Business rules that augment, limit or restrict AI system outputs within certain contexts • Utilizing domain expertise related to deployment context for continuous improvement and TEVV across the AI lifecycle. • Development and regular tracking of human-AI teaming configurations.

• Model assessment and test, evaluation, validation and verification (TEVV) protocols. • Use of standardized documentation and transparency mechanisms. • Software quality assurance practices across AI lifecycle. • Mechanisms to explore system limitations and avoid past failed designs or deployments.

• Establish mechanisms to capture feedback from system end users and potentially impacted groups while system is in deployment. • stablish mechanisms to capture feedback from system end users and potentially impacted groups about how changes in system deployment (e.g., introducing new technology, decommissioning algorithms and models, adapting system, model or algorithm) may create negative impacts that are not visible along the AI lifecycle. • Review insurance policies, warranties, or contracts for legal or oversight requirements for risk transfer procedures. • Document risk tolerance decisions and risk acceptance procedures.

Transparency & Documentation

Organizations can document the following • To what extent can users or parties affected by the outputs of the AI system test the AI system and provide feedback? • Could the AI system expose people to harm or negative impacts? What was done to mitigate or reduce the potential for harm? • How will the accountable human(s) address changes in accuracy and precision due to either an adversary’s attempts to disrupt the AI or unrelated changes in the operational or business environment?

AI Transparency Resources • GAO-21-519SP - Artificial Intelligence: An Accountability Framework for Federal Agencies & Other Entities. • Artificial Intelligence Ethics Framework For The Intelligence Community.

References

Safety, Validity and Reliability Risk Management Approaches and Resources AI Incident Database. 2022. AI Incident Database.

AIAAIC Repository. 2022. AI, algorithmic and automation incidents collected, dissected, examined, and divulged.

Alexander D'Amour, Katherine Heller, Dan Moldovan, et al. 2020. Underspecification Presents Challenges for Credibility in Modern Machine Learning. arXiv:2011.03395.

Andrew L. Beam, Arjun K. Manrai, Marzyeh Ghassemi. 2020. Challenges to the Reproducibility of Machine Learning Models in Health Care. Jama 323, 4 (January 6, 2020), 305-306.

Anthony M. Barrett, Dan Hendrycks, Jessica Newman et al. 2022. Actionable Guidance for High-Consequence AI Risk Management: Towards Standards Addressing AI Catastrophic Risks. arXiv:2206.08966.

[pp. 47-48]

Debugging Machine Learning Models, In Proceedings of ICLR 2019 Workshop, May 6, 2019, New Orleans, Louisiana.

Jessie J. Smith, Saleema Amershi, Solon Barocas, et al. 2022. REAL ML: Recognizing, Exploring, and Articulating Limitations of Machine Learning Research. arXiv:2205.08363.

Joelle Pineau, Philippe Vincent-Lamarre, Koustuv Sinha, et al. 2020. Improving Reproducibility in Machine Learning Research (A Report from the NeurIPS 2019 Reproducibility Program) arXiv:2003.12206.

Kirstie Whitaker. 2017. Showing your working: a how to guide to reproducible research. (August 2017). [LINK](https://github.com/WhitakerLab/ReproducibleResearch/blob/master/PRESENTA TIONS/Whitaker_ICON_August2017.pdf),

Netflix. Chaos Monkey.

Peter Henderson, Riashat Islam, Philip Bachman, et al. 2018. Deep reinforcement learning that matters. Proceedings of the AAAI Conference on Artificial Intelligence. 32, 1 (Apr. 2018).

Suchi Saria, Adarsh Subbaswamy. 2019. Tutorial: Safe and Reliable Machine Learning. arXiv:1904.07204.

Kang, Daniel, Deepti Raghavan, Peter Bailis, and Matei Zaharia. "Model assertions for monitoring and improving ML models." Proceedings of Machine Learning and Systems 2 (2020): 481-496.

Managing Risk Bias National Institute of Standards and Technology (NIST), Reva Schwartz, Apostol Vassilev, et al. 2022. NIST Special Publication 1270 Towards a Standard for Identifying and Managing Bias in Artificial Intelligence.

Bias Testing and Remediation Approaches Alekh Agarwal, Alina Beygelzimer, Miroslav Dudík, et al. 2018. A Reductions Approach to Fair Classification. arXiv:1803.02453.

Brian Hu Zhang, Blake Lemoine, Margaret Mitchell. 2018. Mitigating Unwanted Biases with Adversarial Learning. arXiv:1801.07593.

Drago Plečko, Nicolas Bennett, Nicolai Meinshausen. 2021. Fairadapt: Causal Reasoning for Fair Data Pre-processing. arXiv:2110.10200.

Faisal Kamiran, Toon Calders. 2012. Data Preprocessing Techniques for Classification without Discrimination. Knowledge and Information Systems 33 (2012), 1–33.

[p. 48]

Faisal Kamiran; Asim Karim; Xiangliang Zhang. 2012. Decision Theory for Discrimination- Aware Classification. In Proceedings of the 2012 IEEE 12th International Conference on Data Mining, December 10-13, 2012, Brussels, Belgium. IEEE, 924-929.

Flavio P. Calmon, Dennis Wei, Karthikeyan Natesan Ramamurthy, et al. 2017. Optimized Data Pre-Processing for Discrimination Prevention. arXiv:1704.03354.

Geoff Pleiss, Manish Raghavan, Felix Wu, et al. 2017. On Fairness and Calibration. arXiv:1709.02012.

L. Elisa Celis, Lingxiao Huang, Vijay Keswani, et al. 2020. Classification with Fairness Constraints: A Meta-Algorithm with Provable Guarantees. arXiv:1806.06055.

Michael Feldman, Sorelle Friedler, John Moeller, et al. 2014. Certifying and Removing Disparate Impact. arXiv:1412.3756.

Michael Kearns, Seth Neel, Aaron Roth, et al. 2017. Preventing Fairness Gerrymandering: Auditing and Learning for Subgroup Fairness. arXiv:1711.05144.

Michael Kearns, Seth Neel, Aaron Roth, et al. 2018. An Empirical Study of Rich Subgroup Fairness for Machine Learning. arXiv:1808.08166.

Moritz Hardt, Eric Price, and Nathan Srebro. 2016. Equality of Opportunity in Supervised Learning. In Proceedings of the 30th Conference on Neural Information Processing Systems (NIPS 2016), 2016, Barcelona, Spain.

Rich Zemel, Yu Wu, Kevin Swersky, et al. 2013. Learning Fair Representations. In Proceedings of the 30th International Conference on Machine Learning 2013, PMLR 28, 3, 325-333.

Toshihiro Kamishima, Shotaro Akaho, Hideki Asoh & Jun Sakuma. 2012. Fairness-Aware Classifier with Prejudice Remover Regularizer. In Peter A. Flach, Tijl De Bie, Nello Cristianini (eds) Machine Learning and Knowledge Discovery in Databases. European Conference ECML PKDD 2012, Proceedings Part II, September 24-28, 2012, Bristol, UK. Lecture Notes in Computer Science 7524. Springer, Berlin, Heidelberg.

Security and Resilience Resources FTC Start With Security Guidelines. 2015.

[pp. 48-49]

Gary McGraw et al. 2022. BIML Interactive Machine Learning Risk Framework. Berryville Institute for Machine Learning.

Ilia Shumailov, Yiren Zhao, Daniel Bates, et al. 2021. Sponge Examples: Energy-Latency Attacks on Neural Networks. arXiv:2006.03463.

Marco Barreno, Blaine Nelson, Anthony D. Joseph, et al. 2010. The Security of Machine Learning. Machine Learning 81 (2010), 121-148.

Matt Fredrikson, Somesh Jha, Thomas Ristenpart. 2015. Model Inversion Attacks that Exploit Confidence Information and Basic Countermeasures. In Proceedings of the 22nd ACM SIGSAC Conference on Computer and Communications Security (CCS '15), October 2015. Association for Computing Machinery, New York, NY, USA, 1322–1333.

National Institute for Standards and Technology (NIST). 2022. Cybersecurity Framework.

Nicolas Papernot. 2018. A Marauder's Map of Security and Privacy in Machine Learning. arXiv:1811.01134.

Reza Shokri, Marco Stronati, Congzheng Song, et al. 2017. Membership Inference Attacks against Machine Learning Models. arXiv:1610.05820.

Adversarial Threat Matrix (MITRE). 2021.

Interpretability and Explainability Approaches Chaofan Chen, Oscar Li, Chaofan Tao, et al. 2019. This Looks Like That: Deep Learning for Interpretable Image Recognition. arXiv:1806.10574.

Cynthia Rudin. 2019. Stop explaining black box machine learning models for high stakes decisions and use interpretable models instead. arXiv:1811.10154.

Daniel W. Apley, Jingyu Zhu. 2019. Visualizing the Effects of Predictor Variables in Black Box Supervised Learning Models. arXiv:1612.08468.

David A. Broniatowski. 2021. Psychological Foundations of Explainability and Interpretability in Artificial Intelligence. National Institute of Standards and Technology (NIST) IR 8367. National Institute of Standards and Technology, Gaithersburg, MD.

Forough Poursabzi-Sangdeh, Daniel G. Goldstein, Jake M. Hofman, et al. 2021. Manipulating and Measuring Model Interpretability. arXiv:1802.07810.

Hongyu Yang, Cynthia Rudin, Margo Seltzer. 2017. Scalable Bayesian Rule Lists. arXiv:1602.08610.

[pp. 49-51]

P. Jonathon Phillips, Carina A. Hahn, Peter C. Fontana, et al. 2021. Four Principles of Explainable Artificial Intelligence. National Institute of Standards and Technology (NIST) IR 8312. National Institute of Standards and Technology, Gaithersburg, MD.

Scott Lundberg, Su-In Lee. 2017. A Unified Approach to Interpreting Model Predictions. arXiv:1705.07874.

Susanne Gaube, Harini Suresh, Martina Raue, et al. 2021. Do as AI say: susceptibility in deployment of clinical decision-aids. npj Digital Medicine 4, Article 31 (2021).

Yin Lou, Rich Caruana, Johannes Gehrke, et al. 2013. Accurate intelligible models with pairwise interactions. In Proceedings of the 19th ACM SIGKDD international conference on Knowledge discovery and data mining (KDD '13), August 2013. Association for Computing Machinery, New York, NY, USA, 623–631.

Post-Decommission Upol Ehsan, Ranjit Singh, Jacob Metcalf and Mark O. Riedl. “The Algorithmic Imprint.” Proceedings of the 2022 ACM Conference on Fairness, Accountability, and Transparency (2022).

Privacy Resources National Institute for Standards and Technology (NIST). 2022. Privacy Framework.

Data Governance Marijn Janssen, Paul Brous, Elsa Estevez, Luis S. Barbosa, Tomasz Janowski, Data governance: Organizing data for trustworthy Artificial Intelligence, Government Information Quarterly, Volume 37, Issue 3, 2020, 101493, ISSN 0740-624X.

Software Resources • PiML (explainable models, performance assessment) • Interpret (explainable models) • Iml (explainable models) • Drifter library (performance assessment) • Manifold library (performance assessment) • SALib library (performance assessment) • What-If Tool (performance assessment) • MLextend (performance assessment)

- AI Fairness 360:

• Python (bias testing and mitigation) • R (bias testing and mitigation) • Adversarial-robustness-toolbox (ML security) • Robustness (ML security) • tensorflow/privacy (ML security) • NIST De-identification Tools (Privacy and ML security) • Dvc (MLops, deployment) • Gigantum (MLops, deployment) • Mlflow (MLops, deployment) • Mlmd (MLops, deployment) • Modeldb (MLops, deployment)

MANAGE 2.3 Procedures are followed to respond to and recover from a previously unknown risk when it is identified.

[pp. 51-52]

About AI systems – like any technology – can demonstrate non-functionality or failure or unexpected and unusual behavior. They also can be subject to attacks, incidents, or other misuse or abuse – which their sources are not always known apriori. Organizations can establish, document, communicate and maintain treatment procedures to recognize and counter, mitigate and manage risks that were not previously identified.

Suggested Actions • Protocols, resources, and metrics are in place for continual monitoring of AI systems’ performance, trustworthiness, and alignment with contextual norms and values • Establish and regularly review treatment and response plans for incidents, negative impacts, or outcomes. • Establish and maintain procedures to regularly monitor system components for drift, decontextualization, or other AI system behavior factors, • Establish and maintain procedures for capturing feedback about negative impacts. • Verify contingency processes to handle any negative impacts associated with mission- critical AI systems, and to deactivate systems. • Enable preventive and post-hoc exploration of AI system limitations by relevant AI actor groups. • Decommission systems that exceed risk tolerances.

Transparency & Documentation

Organizations can document the following • Who will be responsible for maintaining, re-verifying, monitoring, and updating this AI once deployed? • Are the responsibilities of the personnel involved in the various AI governance processes clearly defined? (Including responsibilities to decommission the AI system.) • What processes exist for data generation, acquisition/collection, ingestion, staging/storage, transformations, security, maintenance, and dissemination? • How will the appropriate performance metrics, such as accuracy, of the AI be monitored after the AI is deployed?

AI Transparency Resources • Artificial Intelligence Ethics Framework For The Intelligence Community. • WEF - Companion to the Model AI Governance Framework – Implementation and Self- Assessment Guide for Organizations. • GAO-21-519SP - Artificial Intelligence: An Accountability Framework for Federal Agencies & Other Entities.

References AI Incident Database. 2022. AI Incident Database.

AIAAIC Repository. 2022. AI, algorithmic and automation incidents collected, dissected, examined, and divulged.

Andrew Burt and Patrick Hall. 2018. What to Do When AI Fails. O’Reilly Media, Inc. (May 18, 2020). Retrieved October 17, 2022.

National Institute for Standards and Technology (NIST). 2022. Cybersecurity Framework.

SANS Institute. 2022. Security Consensus Operational Readiness Evaluation (SCORE) Security Checklist [or Advanced Persistent Threat (APT) Handling Checklist].

Suchi Saria, Adarsh Subbaswamy. 2019. Tutorial: Safe and Reliable Machine Learning. arXiv:1904.07204.

MANAGE 2.4 Mechanisms are in place and applied, responsibilities are assigned and understood to supersede, disengage, or deactivate AI systems that demonstrate performance or outcomes inconsistent with intended use.

[pp. 52-53]

About Performance inconsistent with intended use does not always increase risk or lead to negative impacts. Rigorous TEVV practices are useful for protecting against negative impacts regardless of intended use. When negative impacts do arise, superseding (bypassing), disengaging, or deactivating/decommissioning a model, AI system component(s), or the entire AI system may be necessary, such as when:

• a system reaches the end of its lifetime • detected or identified risks exceed tolerance thresholds • adequate system mitigation actions are beyond the organization’s capacity • feasible system mitigation actions do not meet regulatory, legal, norms or standards. • impending risk is detected during continual monitoring, for which feasible mitigation cannot be identified or implemented in a timely fashion.

Safely removing AI systems from operation, either temporarily or permanently, under these scenarios requires standard protocols that minimize operational disruption and downstream negative impacts. Protocols can involve redundant or backup systems that are developed in alignment with established system governance policies (see GOVERN 1.7), regulatory compliance, legal frameworks, business requirements and norms and l standards within the application context of use. Decision thresholds and metrics for actions to bypass or deactivate system components are part of continual monitoring procedures. Incidents that result in a bypass/deactivate decision require documentation and review to understand root causes, impacts, and potential opportunities for mitigation and redeployment. Organizations are encouraged to develop risk and change management

protocols that consider and anticipate upstream and downstream consequences of both temporary and/or permanent decommissioning, and provide contingency options.

Suggested Actions • Regularly review established procedures for AI system bypass actions, including plans for redundant or backup systems to ensure continuity of operational and/or business functionality. • Regularly review Identify system incident thresholds for activating bypass or deactivation responses. • Apply change management processes to understand the upstream and downstream consequences of bypassing or deactivating an AI system or AI system components. • Apply protocols, resources and metrics for decisions to supersede, bypass or deactivate AI systems or AI system components. • Preserve materials for forensic, regulatory, and legal review. • Conduct internal root cause analysis and process reviews of bypass or deactivation events. • Decommission and preserve system components that cannot be updated to meet criteria for redeployment. • Establish criteria for redeploying updated system components, in consideration of trustworthy characteristics

Transparency & Documentation

[pp. 53-54]

Organizations can document the following • What are the roles, responsibilities, and delegation of authorities of personnel involved in the design, development, deployment, assessment and monitoring of the AI system? • Did your organization implement a risk management system to address risks involved in deploying the identified AI solution (e.g. personnel risk or changes to commercial objectives)? • What testing, if any, has the entity conducted on the AI system to identify errors and limitations (i.e. adversarial or stress testing)? • To what extent does the entity have established procedures for retiring the AI system, if it is no longer needed? • How did the entity use assessments and/or evaluations to determine if the system can be scaled up, continue, or be decommissioned?

AI Transparency Resources • GAO-21-519SP - Artificial Intelligence: An Accountability Framework for Federal Agencies & Other Entities.

References Decommissioning Template. Application Lifecycle And Supporting Docs. Cloud and Infrastructure Community of Practice.

Develop a Decommission Plan. M3 Playbook. Office of Shared Services and Solutions and Performance Improvement. General Services Administration.

MANAGE 3.1 AI risks and benefits from third-party resources are regularly monitored, and risk controls are applied and documented.

About AI systems may depend on external resources and associated processes, including third- party data, software or hardware systems. Third parties’ supplying organizations with components and services, including tools, software, and expertise for AI system design, development, deployment or use can improve efficiency and scalability. It can also increase complexity and opacity, and, in-turn, risk. Documenting third-party technologies, personnel, and resources that were employed can help manage risks. Focusing first and foremost on risks involving physical safety, legal liabilities, regulatory compliance, and negative impacts on individuals, groups, or society is recommended.

Suggested Actions • Have legal requirements been addressed? • Apply organizational risk tolerance to third-party AI systems. • Apply and document organizational risk management plans and practices to third-party AI technology, personnel, or other resources. • Identify and maintain documentation for third-party AI systems and components. • Establish testing, evaluation, validation and verification processes for third-party AI systems which address the needs for transparency without exposing proprietary algorithms . • Establish processes to identify beneficial use and risk indicators in third-party systems or components, such as inconsistent software release schedule, sparse documentation, and incomplete software change management (e.g., lack of forward or backward compatibility). • Organizations can establish processes for third parties to report known and potential vulnerabilities, risks or biases in supplied resources. • Verify contingency processes for handling negative impacts associated with mission- critical third-party AI systems. • Monitor third-party AI systems for potential negative impacts and risks associated with trustworthiness characteristics. • Decommission third-party systems that exceed risk tolerances.

Transparency & Documentation

[pp. 54-56]

Organizations can document the following • If a third party created the AI system or some of its components, how will you ensure a level of explainability or interpretability? Is there documentation?

• If your organization obtained datasets from a third party, did your organization assess and manage the risks of using such datasets? • Did you establish a process for third parties (e.g. suppliers, end users, subjects, distributors/vendors or workers) to report potential vulnerabilities, risks or biases in the AI system? • Have legal requirements been addressed?

AI Transparency Resources • Artificial Intelligence Ethics Framework For The Intelligence Community. • WEF - Companion to the Model AI Governance Framework – Implementation and Self- Assessment Guide for Organizations. • Datasheets for Datasets.

References Office of the Comptroller of the Currency. 2021. Proposed Interagency Guidance on Third- Party Relationships: Risk Management. July 12, 2021.

MANAGE 3.2 Pre-trained models which are used for development are monitored as part of AI system regular monitoring and maintenance.

About A common approach in AI development is transfer learning, whereby an existing pre- trained model is adapted for use in a different, but related application. AI actors in development tasks often use pre-trained models from third-party entities for tasks such as image classification, language prediction, and entity recognition, because the resources to build such models may not be readily available to most organizations. Pre-trained models are typically trained to address various classification or prediction problems, using exceedingly large datasets and computationally intensive resources. The use of pre-trained models can make it difficult to anticipate negative system outcomes or impacts. Lack of documentation or transparency tools increases the difficulty and general complexity when deploying pre-trained models and hinders root cause analyses.

Suggested Actions • Identify pre-trained models within AI system inventory for risk tracking. • Establish processes to independently and continually monitor performance and trustworthiness of pre-trained models, and as part of third-party risk tracking. • Monitor performance and trustworthiness of AI system components connected to pre- trained models, and as part of third-party risk tracking. • Identify, document and remediate risks arising from AI system components and pre- trained models per organizational risk management procedures, and as part of third- party risk tracking. • Decommission AI system components and pre-trained models which exceed risk tolerances, and as part of third-party risk tracking.

Transparency & Documentation

Organizations can document the following • How has the entity documented the AI system’s data provenance, including sources, origins, transformations, augmentations, labels, dependencies, constraints, and metadata? • Does this dataset collection/processing procedure achieve the motivation for creating the dataset stated in the first section of this datasheet? • How does the entity ensure that the data collected are adequate, relevant, and not excessive in relation to the intended purpose? • If the dataset becomes obsolete how will this be communicated?


---

[previous part](text-003.md) | [source overview](overview.md) | [next part](text-005.md)

[^original]: NIST, "NIST AI RMF Playbook" (2024-08-02). https://airc.nist.gov/airmf-resources/playbook/
