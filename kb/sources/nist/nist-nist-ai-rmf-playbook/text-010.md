---
type: Source Text
title: NIST AI RMF Playbook - part 10 of 12 (pp. 119-130)
description: 'Verbatim extracted text, pp. 119-130: MEASURE'
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
part: 10
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

[previous part](text-009.md) | [source overview](overview.md) | [next part](text-011.md)

> Verbatim text extracted from the original (NIST, 2024-08-02), part 10 of 12, pp. 119-130. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **industry practice**.[^original]

## MEASURE


[pp. 119-120]

Joshua A. Kroll. “Outlining Traceability: A Principle for Operationalizing Accountability in Computing Systems.” FAccT '21: Proceedings of the 2021 ACM Conference on Fairness, Accountability, and Transparency, March 1, 2021, 758–71.

Jennifer Cobbe, Michelle Seng Lee, and Jatinder Singh. “Reviewable Automated Decision- Making: A Framework for Accountable Algorithmic Systems.” FAccT '21: Proceedings of the 2021 ACM Conference on Fairness, Accountability, and Transparency, March 1, 2021, 598– 609.

MEASURE 2.9 The AI model is explained, validated, and documented, and AI system output is interpreted within its context – as identified in the MAP function – and to inform responsible use and governance.

About Explainability and interpretability assist those operating or overseeing an AI system, as well as users of an AI system, to gain deeper insights into the functionality and trustworthiness of the system, including its outputs.

Explainable and interpretable AI systems offer information that help end users understand the purposes and potential impact of an AI system. Risk from lack of explainability may be managed by describing how AI systems function, with descriptions tailored to individual differences such as the user’s role, knowledge, and skill level. Explainable systems can be debugged and monitored more easily, and they lend themselves to more thorough documentation, audit, and governance.

Risks to interpretability often can be addressed by communicating a description of why

an AI system made a particular prediction or recommendation.

Transparency, explainability, and interpretability are distinct characteristics that support

each other. Transparency can answer the question of “what happened”. Explainability can answer the question of “how” a decision was made in the system. Interpretability can answer the question of “why” a decision was made by the system and its

meaning or context to the user.

Suggested Actions • Verify systems are developed to produce explainable models, post-hoc explanations and audit logs. • When possible or available, utilize approaches that are inherently explainable, such as traditional and penalized generalized linear models , decision trees, nearest-neighbor and prototype-based approaches, rule-based models, generalized additive models , explainable boosting machines and neural additive models. • Test explanation methods and resulting explanations prior to deployment to gain feedback from relevant AI actors, end users, and potentially impacted individuals or groups about whether explanations are accurate, clear, and understandable. • Document AI model details including model type (e.g., convolutional neural network, reinforcement learning, decision tree, random forest, etc.) data features, training algorithms, proposed uses, decision thresholds, training data, evaluation data, and ethical considerations. • Establish, document, and report performance and error metrics across demographic groups and other segments relevant to the deployment context.

[pp. 121-122]

• Explain systems using a variety of methods, e.g., visualizations, model extraction, feature importance, and others. Since explanations may not accurately summarize complex systems, test explanations according to properties such as fidelity, consistency, robustness, and interpretability. • Assess the characteristics of system explanations according to properties such as fidelity (local and global), ambiguity, interpretability, interactivity, consistency, and resilience to attack/manipulation. • Test the quality of system explanations with end-users and other groups. • Secure model development processes to avoid vulnerability to external manipulation such as gaming explanation processes. • Test for changes in models over time, including for models that adjust in response to production data. • Use transparency tools such as data statements and model cards to document explanatory and validation information.

Transparency & Documentation

Organizations can document the following • Given the purpose of the AI, what level of explainability or interpretability is required for how the AI made its determination? • Given the purpose of this AI, what is an appropriate interval for checking whether it is still accurate, unbiased, explainable, etc.? What are the checks for this model? • How has the entity documented the AI system’s data provenance, including sources, origins, transformations, augmentations, labels, dependencies, constraints, and metadata? • What type of information is accessible on the design, operations, and limitations of the AI system to external stakeholders, including end users, consumers, regulators, and individuals impacted by use of the AI system?

AI Transparency Resources • GAO-21-519SP - Artificial Intelligence: An Accountability Framework for Federal Agencies & Other Entities. • Artificial Intelligence Ethics Framework For The Intelligence Community. • WEF Companion to the Model AI Governance Framework- WEF - Companion to the Model AI Governance Framework, 2020.

References Chaofan Chen, Oscar Li, Chaofan Tao, Alina Jade Barnett, Jonathan Su, and Cynthia Rudin. "This Looks Like That: Deep Learning for Interpretable Image Recognition." arXiv preprint, submitted December 28, 2019.

Cynthia Rudin. "Stop Explaining Black Box Machine Learning Models for High Stakes Decisions and Use Interpretable Models Instead." arXiv preprint, submitted September 22, 2019.

David A. Broniatowski. "NISTIR 8367 Psychological Foundations of Explainability and Interpretability in Artificial Intelligence. National Institute of Standards and Technology (NIST), 2021.

Alejandro Barredo Arrieta, Natalia Díaz-Rodríguez, Javier Del Ser, Adrien Bennetot, Siham Tabik, Alberto Barbado, Salvador Garcia, et al. “Explainable Artificial Intelligence (XAI): Concepts, Taxonomies, Opportunities, and Challenges Toward Responsible AI.” Information Fusion 58 (June 2020): 82–115.

[p. 122]

Zana Buçinca, Phoebe Lin, Krzysztof Z. Gajos, and Elena L. Glassman. “Proxy Tasks and Subjective Measures Can Be Misleading in Evaluating Explainable AI Systems.” IUI '20: Proceedings of the 25th International Conference on Intelligent User Interfaces, March 17, 2020, 454–64.

P. Jonathon Phillips, Carina A. Hahn, Peter C. Fontana, Amy N. Yates, Kristen Greene, David A. Broniatowski, and Mark A. Przybocki. "NISTIR 8312 Four Principles of Explainable Artificial Intelligence." National Institute of Standards and Technology (NIST), September 2021.

Margaret Mitchell, Simone Wu, Andrew Zaldivar, Parker Barnes, Lucy Vasserman, Ben Hutchinson, Elena Spitzer, Inioluwa Deborah Raji, and Timnit Gebru. “Model Cards for Model Reporting.” FAT *19: Proceedings of the Conference on Fairness, Accountability, and Transparency, January 2019, 220–29.

Ke Yang, Julia Stoyanovich, Abolfazl Asudeh, Bill Howe, HV Jagadish, and Gerome Miklau. “A Nutritional Label for Rankings.” SIGMOD '18: Proceedings of the 2018 International Conference on Management of Data, May 27, 2018, 1773–76.

Marco Tulio Ribeiro, Sameer Singh, and Carlos Guestrin. "'Why Should I Trust You?': Explaining the Predictions of Any Classifier." arXiv preprint, submitted August 9, 2016.

Scott M. Lundberg and Su-In Lee. "A unified approach to interpreting model predictions." NIPS'17: Proceedings of the 31st International Conference on Neural Information Processing Systems, December 4, 2017, 4768-4777.

Dylan Slack, Sophie Hilgard, Emily Jia, Sameer Singh, and Himabindu Lakkaraju. “Fooling LIME and SHAP: Adversarial Attacks on Post Hoc Explanation Methods.” AIES '20: Proceedings of the AAAI/ACM Conference on AI, Ethics, and Society, February 7, 2020, 180– 86.

David Alvarez-Melis and Tommi S. Jaakkola. "Towards robust interpretability with self- explaining neural networks." NIPS'18: Proceedings of the 32nd International Conference on Neural Information Processing Systems, December 3, 2018, 7786-7795.

FinRegLab, Laura Biattner, and Jann Spiess. "Machine Learning Explainability & Fairness: Insights from Consumer Lending." FinRegLab, April 2022.

[pp. 123-124]

Miguel Ferreira, Muhammad Bilal Zafar, and Krishna P. Gummadi. "The Case for Temporal Transparency: Detecting Policy Change Events in Black-Box Decision Making Systems." arXiv preprint, submitted October 31, 2016.

Himabindu Lakkaraju, Ece Kamar, Rich Caruana, and Jure Leskovec. "Interpretable & Explorable Approximations of Black Box Models." arXiv preprint, July 4, 2017.

Software Resources • SHAP • LIME • Interpret • PiML • Iml • Dalex

MEASURE 2.10 Privacy risk of the AI system – as identified in the MAP function – is examined and documented.

About Privacy refers generally to the norms and practices that help to safeguard human autonomy, identity, and dignity. These norms and practices typically address freedom from intrusion, limiting observation, or individuals’ agency to consent to disclosure or control of facets of their identities (e.g., body, data, reputation).

Privacy values such as anonymity, confidentiality, and control generally should guide choices for AI system design, development, and deployment. Privacy-related risks may influence security, bias, and transparency and come with tradeoffs with these other characteristics. Like safety and security, specific technical features of an AI system may promote or reduce privacy. AI systems can also present new risks to privacy by allowing inference to identify individuals or previously private information about individuals.

Privacy-enhancing technologies (“PETs”) for AI, as well as data minimizing methods such as de-identification and aggregation for certain model outputs, can support design for privacy- enhanced AI systems. Under certain conditions such as data sparsity, privacy enhancing techniques can result in a loss in accuracy, impacting decisions about fairness and other values in certain domains.

Suggested Actions • Specify privacy-related values, frameworks, and attributes that are applicable in the context of use through direct engagement with end users and potentially impacted groups and communities. • Document collection, use, management, and disclosure of personally sensitive information in datasets, in accordance with privacy and data governance policies

• Quantify privacy-level data aspects such as the ability to identify individuals or groups (e.g. k-anonymity metrics, l-diversity, t-closeness). • Establish and document protocols (authorization, duration, type) and access controls for training sets or production data containing personally sensitive information, in accordance with privacy and data governance policies. • Monitor internal queries to production data for detecting patterns that isolate personal records. • Monitor PSI disclosures and inference of sensitive or legally protected attributes

• Assess the risk of manipulation from overly customized content. Evaluate information presented to representative users at various points along axes of difference between individuals (e.g. individuals of different ages, genders, races, political affiliation, etc.).

[pp. 124-125]

• Use privacy-enhancing techniques such as differential privacy, when publicly sharing dataset information. • Collaborate with privacy experts, AI end users and operators, and other domain experts to determine optimal differential privacy metrics within contexts of use.

Transparency & Documentation

Organizations can document the following • Did your organization implement accountability-based practices in data management and protection (e.g. the PDPA and OECD Privacy Principles)? • What assessments has the entity conducted on data security and privacy impacts associated with the AI system? • Did your organization implement a risk management system to address risks involved in deploying the identified AI solution (e.g. personnel risk or changes to commercial objectives)? • Does the dataset contain information that might be considered sensitive or confidential? (e.g., personally identifying information) • If it relates to people, could this dataset expose people to harm or legal action? (e.g., financial, social or otherwise) What was done to mitigate or reduce the potential for harm?

AI Transparency Resources • WEF Companion to the Model AI Governance Framework- WEF - Companion to the Model AI Governance Framework, 2020. ( • Datasheets for Datasets.

References Kaitlin R. Boeckl and Naomi B. Lefkovitz. "NIST Privacy Framework: A Tool for Improving Privacy Through Enterprise Risk Management, Version 1.0." National Institute of Standards and Technology (NIST), January 16, 2020.

Latanya Sweeney. “K-Anonymity: A Model for Protecting Privacy.” International Journal of Uncertainty, Fuzziness and Knowledge-Based Systems 10, no. 5 (2002): 557–70.

Ashwin Machanavajjhala, Johannes Gehrke, Daniel Kifer, and Muthuramakrishnan Venkitasubramaniam. “L-Diversity: Privacy beyond K-Anonymity.” 22nd International Conference on Data Engineering (ICDE'06), 2006.

Ninghui Li, Tiancheng Li, and Suresh Venkatasubramanian. "CERIAS Tech Report 2007-78 t- Closeness: Privacy Beyond k-Anonymity and -Diversity." Center for Education and Research, Information Assurance and Security, Purdue University, 2001.

J. Domingo-Ferrer and J. Soria-Comas. "From t-closeness to differential privacy and vice versa in data anonymization." arXiv preprint, submitted December 21, 2015.

Joseph Near, David Darais, and Kaitlin Boeckly. "Differential Privacy for Privacy-Preserving Data Analysis: An Introduction to our Blog Series." National Institute of Standards and Technology (NIST), July 27, 2020.

Cynthia Dwork. “Differential Privacy.” Automata, Languages and Programming, 2006, 1–12.

[pp. 125-126]

Zhanglong Ji, Zachary C. Lipton, and Charles Elkan. "Differential Privacy and Machine Learning: a Survey and Review." arXiv preprint, submitted December 24,2014.

Michael B. Hawes. "Implementing Differential Privacy: Seven Lessons From the 2020 United States Census." Harvard Data Science Review 2, no. 2 (2020).

Harvard University Privacy Tools Project. “Differential Privacy.” Harvard University, n.d.

John M. Abowd, Robert Ashmead, Ryan Cumings-Menon, Simson Garfinkel, Micah Heineck, Christine Heiss, Robert Johns, Daniel Kifer, Philip Leclerc, Ashwin Machanavajjhala, Brett Moran, William Matthew Spence Sexton and Pavel Zhuravlev. "The 2020 Census Disclosure Avoidance System TopDown Algorithm." United States Census Bureau, April 7, 2022.

Nicolas Papernot and Abhradeep Guha Thakurta. "How to deploy machine learning with differential privacy." National Institute of Standards and Technology (NIST), December 21, 2021.

Claire McKay Bowen. "Utility Metrics for Differential Privacy: No One-Size-Fits-All." National Institute of Standards and Technology (NIST), November 29, 2021.

Helen Nissenbaum. "Contextual Integrity Up and Down the Data Food Chain." Theoretical Inquiries in Law 20, L. 221 (2019): 221-256.

Sebastian Benthall, Seda Gürses, and Helen Nissenbaum. “Contextual Integrity through the Lens of Computer Science.” Foundations and Trends in Privacy and Security 2, no. 1 (December 22, 2017): 1–69.

Jenifer Sunrise Winter and Elizabeth Davidson. “Big Data Governance of Personal Health Information and Challenges to Contextual Integrity.” The Information Society: An International Journal 35, no. 1 (2019): 36–51.

MEASURE 2.11 Fairness and bias – as identified in the MAP function – is evaluated and results are documented.

About Fairness in AI includes concerns for equality and equity by addressing issues such as harmful bias and discrimination. Standards of fairness can be complex and difficult to define because perceptions of fairness differ among cultures and may shift depending on application. Organizations’ risk management efforts will be enhanced by recognizing and considering these differences. Systems in which harmful biases are mitigated are not necessarily fair. For example, systems in which predictions are somewhat balanced across demographic groups may still be inaccessible to individuals with disabilities or affected by the digital divide or may exacerbate existing disparities or systemic biases.

[pp. 126-127]

Bias is broader than demographic balance and data representativeness. NIST has identified three major categories of AI bias to be considered and managed: systemic, computational and statistical, and human-cognitive. Each of these can occur in the absence of prejudice, partiality, or discriminatory intent.

• Systemic bias can be present in AI datasets, the organizational norms, practices, and processes across the AI lifecycle, and the broader society that uses AI systems. • Computational and statistical biases can be present in AI datasets and algorithmic processes, and often stem from systematic errors due to non-representative samples. • Human-cognitive biases relate to how an individual or group perceives AI system information to make a decision or fill in missing information, or how humans think about purposes and functions of an AI system. Human-cognitive biases are omnipresent in decision-making processes across the AI lifecycle and system use, including the design, implementation, operation, and maintenance of AI.

Bias exists in many forms and can become ingrained in the automated systems that help make decisions about our lives. While bias is not always a negative phenomenon, AI systems can potentially increase the speed and scale of biases and perpetuate and amplify harms to individuals, groups, communities, organizations, and society.

Suggested Actions • Conduct fairness assessments to manage computational and statistical forms of bias which include the following steps:

• Identify types of harms, including allocational, representational, quality of service, stereotyping, or erasure • Identify across, within, and intersecting groups that might be harmed

• Quantify harms using both a general fairness metric, if appropriate (e.g. demographic parity, equalized odds, equal opportunity, statistical hypothesis tests), and custom, context-specific metrics developed in collaboration with affected communities • Analyze quantified harms for contextually significant differences across groups, within groups, and among intersecting groups • Refine identification of within-group and intersectional group disparities.

• Evaluate underlying data distributions and employ sensitivity analysis during the analysis of quantified harms. • Evaluate quality metrics including false positive rates and false negative rates. • Consider biases affecting small groups, within-group or intersectional communities, or single individuals.

• Understand and consider sources of bias in training and TEVV data:

• Differences in distributions of outcomes across and within groups, including intersecting groups. • Completeness, representativeness and balance of data sources. • Identify input data features that may serve as proxies for demographic group membership (i.e., credit score, ZIP code) or otherwise give rise to emergent bias within AI systems. • Forms of systemic bias in images, text (or word embeddings), audio or other complex or unstructured data.

[pp. 127-128]

• Leverage impact assessments to identify and classify system impacts and harms to end users, other individuals, and groups with input from potentially impacted communities. • Identify the classes of individuals, groups, or environmental ecosystems which might be impacted through direct engagement with potentially impacted communities. • Evaluate systems in regards to disability inclusion, including consideration of disability status in bias testing, and discriminatory screen out processes that may arise from non- inclusive design or deployment decisions. • Develop objective functions in consideration of systemic biases, in-group/out-group dynamics. • Use context-specific fairness metrics to examine how system performance varies across groups, within groups, and/or for intersecting groups. Metrics may include statistical parity, error-rate equality, statistical parity difference, equal opportunity difference, average absolute odds difference, standardized mean difference, percentage point differences. • Customize fairness metrics to specific context of use to examine how system performance and potential harms vary within contextual norms. • Define acceptable levels of difference in performance in accordance with established organizational governance policies, business requirements, regulatory compliance, legal frameworks, and ethical standards within the context of use

• Define the actions to be taken if disparity levels rise above acceptable levels. • Identify groups within the expected population that may require disaggregated analysis, in collaboration with impacted communities. • Leverage experts with knowledge in the specific context of use to investigate substantial measurement differences and identify root causes for those differences. • Monitor system outputs for performance or bias issues that exceed established tolerance levels. • Ensure periodic model updates; test and recalibrate with updated and more representative data to stay within acceptable levels of difference. • Apply pre-processing data transformations to address factors related to demographic balance and data representativeness. • Apply in-processing to balance model performance quality with bias considerations. • Apply post-processing mathematical/computational techniques to model results in close collaboration with impact assessors, socio-technical experts, and other AI actors with expertise in the context of use. • Apply model selection approaches with transparent and deliberate consideration of bias management and other trustworthy characteristics. • Collect and share information about differences in outcomes for the identified groups. • Consider mediations to mitigate differences, especially those that can be traced to past patterns of unfair or biased human decision making. • Utilize human-centered design practices to generate deeper focus on societal impacts and counter human-cognitive biases within the AI lifecycle. • Evaluate practices along the lifecycle to identify potential sources of human-cognitive bias such as availability, observational, and confirmation bias, and to make implicit decision making processes more explicit and open to investigation. • Work with human factors experts to evaluate biases in the presentation of system output to end users, operators and practitioners. • Utilize processes to enhance contextual awareness, such as diverse internal staff and stakeholder engagement.

Transparency & Documentation

[pp. 128-129]

Organizations can document the following • To what extent are the established procedures effective in mitigating bias, inequity, and other concerns resulting from the system? • If it relates to people, does it unfairly advantage or disadvantage a particular social group? In what ways? How was this mitigated? • Given the purpose of this AI, what is an appropriate interval for checking whether it is still accurate, unbiased, explainable, etc.? What are the checks for this model? • How has the entity identified and mitigated potential impacts of bias in the data, including inequitable or discriminatory outcomes? • To what extent has the entity identified and mitigated potential bias—statistical, contextual, and historical—in the data?

• Were adversarial machine learning approaches considered or used for measuring bias (e.g.: prompt engineering, adversarial models)

AI Transparency Resources • GAO-21-519SP - Artificial Intelligence: An Accountability Framework for Federal Agencies & Other Entities. • Artificial Intelligence Ethics Framework For The Intelligence Community. • WEF Companion to the Model AI Governance Framework- WEF - Companion to the Model AI Governance Framework, 2020. • Datasheets for Datasets.

References Ali Hasan, Shea Brown, Jovana Davidovic, Benjamin Lange, and Mitt Regan. “Algorithmic Bias and Risk Assessments: Lessons from Practice.” Digital Society 1 (2022).

Richard N. Landers and Tara S. Behrend. “Auditing the AI Auditors: A Framework for Evaluating Fairness and Bias in High Stakes AI Predictive Models.” American Psychologist 78, no. 1 (2023): 36–49.

Ninareh Mehrabi, Fred Morstatter, Nripsuta Saxena, Kristina Lerman, and Aram Galstyan. “A Survey on Bias and Fairness in Machine Learning.” ACM Computing Surveys 54, no. 6 (July 2021): 1–35.

Michele Loi and Christoph Heitz. “Is Calibration a Fairness Requirement?” FAccT '22: 2022 ACM Conference on Fairness, Accountability, and Transparency, June 2022, 2026–34.

Shea Brown, Ryan Carrier, Merve Hickok, and Adam Leon Smith. “Bias Mitigation in Data Sets.” SocArXiv, July 8, 2021.

Reva Schwartz, Apostol Vassilev, Kristen Greene, Lori Perine, Andrew Burt, and Patrick Hall. "NIST Special Publication 1270 Towards a Standard for Identifying and Managing Bias in Artificial Intelligence." National Institute of Standards and Technology (NIST), 2022.

Microsoft Research. “AI Fairness Checklist.” Microsoft, February 7, 2022.

[pp. 129-130]

Samir Passi and Solon Barocas. “Problem Formulation and Fairness.” FAT* '19: Proceedings of the Conference on Fairness, Accountability, and Transparency, January 2019, 39–48.

Jade S. Franklin, Karan Bhanot, Mohamed Ghalwash, Kristin P. Bennett, Jamie McCusker, and Deborah L. McGuinness. “An Ontology for Fairness Metrics.” AIES '22: Proceedings of the 2022 AAAI/ACM Conference on AI, Ethics, and Society, July 2022, 265–75.

Zhang, B., Lemoine, B., & Mitchell, M. (2018). Mitigating Unwanted Biases with Adversarial Learning. Proceedings of the 2018 AAAI/ACM Conference on AI, Ethics, and Society. https://arxiv.org/pdf/1801.07593.pdf

Ganguli, D., et al. (2023). The Capacity for Moral Self-Correction in Large Language Models. arXiv. https://arxiv.org/abs/2302.07459

Arvind Narayanan. “Tl;DS - 21 Fairness Definition and Their Politics by Arvind Narayanan.” Dora's world, July 19, 2019.

Ben Green. “Escaping the Impossibility of Fairness: From Formal to Substantive Algorithmic Fairness.” Philosophy and Technology 35, no. 90 (October 8, 2022).

Alexandra Chouldechova. “Fair Prediction with Disparate Impact: A Study of Bias in Recidivism Prediction Instruments.” Big Data 5, no. 2 (June 1, 2017): 153–63.

Sina Fazelpour and Zachary C. Lipton. “Algorithmic Fairness from a Non-Ideal Perspective.” AIES '20: Proceedings of the AAAI/ACM Conference on AI, Ethics, and Society, February 7, 2020, 57–63.

Hemank Lamba, Kit T. Rodolfa, and Rayid Ghani. “An Empirical Comparison of Bias Reduction Methods on Real-World Problems in High-Stakes Policy Settings.” ACM SIGKDD Explorations Newsletter 23, no. 1 (May 29, 2021): 69–85.

ISO. “ISO/IEC TR 24027:2021 Information technology — Artificial intelligence (AI) — Bias in AI systems and AI aided decision making.” ISO Standards, November 2021.

Shari Trewin. "AI Fairness for People with Disabilities: Point of View." arXiv preprint, submitted November 26, 2018.


---

[previous part](text-009.md) | [source overview](overview.md) | [next part](text-011.md)

[^original]: NIST, "NIST AI RMF Playbook" (2024-08-02). https://airc.nist.gov/airmf-resources/playbook/
