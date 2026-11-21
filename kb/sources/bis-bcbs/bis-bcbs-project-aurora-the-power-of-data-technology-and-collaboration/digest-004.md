---
type: Source Digest
title: 'Project Aurora: the power of data, technology and collaboration to combat money laundering across institutions and borders - part 4 of 6 (pp. 61-76)'
description: 'Verified paraphrased digest, pp. 61-76: Project Aurora > Contents'
resource: https://www.bis.org/publications/project-aurora-power-data-technology-and-collaboration-combat-money-laundering-across-institutions-and-borders
tags:
- correspondent_banking
- effectiveness
- international_standard
- intl
- other
- risk_assessment
status: stable
source_id: bis-bcbs-project-aurora-the-power-of-data-technology-and-collaboration
issuer: bis_bcbs
issuer_name: Bank for International Settlements / Basel Committee
jurisdictions:
- INTL
tier: 2
instrument_type: other
normative_force: international_standard
publication_date: '2023-05-31'
legal_status: current
part: 4
parts_total: 6
content_mode: digest
generated:
  by: claude-code-subagent/claude-sonnet-5-5
  at: '2026-11-21T08:43:43Z'
verified:
- by: process:kb-digest-check/anchor-match
  at: '2026-11-21T08:43:43Z'
- by: claude-code-judge-agent/claude-opus-5-5
  at: '2026-11-21T08:43:43Z'
sources:
- id: original
  resource: https://www.bis.org/publications/project-aurora-power-data-technology-and-collaboration-combat-money-laundering-across-institutions-and-borders
  title: 'Project Aurora: the power of data, technology and collaboration to combat money laundering across institutions and borders'
  author: org:bis_bcbs
  last_modified: '2023-05-31T00:00:00Z'
digest_points: 119
---

# Project Aurora: the power of data, technology and collaboration to combat money laundering across institutions and borders (digest)

[previous part](digest-003.md) | [source overview](overview.md) | [next part](digest-005.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (pp. 61-76) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **international standard**.

## 4.4 Part C: Testing privacy-enhancing technologies for AML

- **descriptive / finding or result**: HE allowed computations on encrypted data without decrypting it. (p. 61)[^original]  
  <sub>anchor: "HE allowed computations to be performed on encrypted data without the need to decrypt it"</sub>
- **descriptive / finding or result**: LDP obfuscated data before sharing, making it difficult to link data to specific individuals. (p. 61)[^original]  
  <sub>anchor: "LDP obfuscated the data before sharing, thereby making it difficult to link data to specific individuals"</sub>
- **descriptive / finding or result**: Implementing federated learning showed it is a promising PET that could provide stronger privacy guarantees, as data remain in each party's systems and only model updates are shared. (p. 61)[^original]  
  <sub>anchor: "FL is a promising PET that could provide stronger privacy guarantees"</sub>

## Privacy risks and attacks

- **descriptive / limitation**: Although the PETs provide privacy advantages, like any other technology they have limitations and potential risks. (p. 61)[^original]  
  <sub>anchor: "they, like any other technology, have limitations and potential risks."</sub>
- **expected / expectation**: It is crucial to obtain legal clarity on the classification of privacy-enhanced data, especially personal data, so individuals and businesses understand their rights and how data are used and protected, promoting transparency and trust between institutions and clients. (p. 61)[^original]  
  <sub>anchor: "It is crucial to obtain legal clarity regarding the classification of privacy-enhanced data, especially personal data."</sub>
- **descriptive / limitation**: The report's privacy section does not aim to provide a legal assessment but discusses perspectives and risks of using PETs for data protection. (p. 61)[^original]  
  <sub>anchor: "This section does not aim to provide a legal assessment"</sub>
- **descriptive / definition**: Encrypting data does not necessarily make them anonymous: anonymisation ensures data cannot be traced back to individuals, whereas pseudonymisation often replaces identifiable information with a unique identifier. (p. 61)[^original]  
  <sub>anchor: "encrypting data does not necessarily mean that the data become anonymous"</sub>
- **descriptive / definition**: Depending on the PET used, PII data are pseudonymised rather than anonymised when encrypted, and may still be traced back to an individual if an identifier is linked with external information, for example via a decryption key. (p. 61)[^original]  
  <sub>anchor: "depending on the PET used, PII data are pseudonymised, rather than anonymised, when encrypted."</sub>
- **permissive / context**: The potential risk of model leakage in federated learning (which affects CAL 3 and 4) could be reduced by using secure multiparty computation and secure aggregation. (p. 61)[^original]  
  <sub>anchor: "The potential risk of model leakage could be mitigated with secure multiparty computation and secure aggregation."</sub>
- **recommended / recommendation**: The report states that further experimentation on mitigating model leakage with secure multiparty computation and secure aggregation would be beneficial. (p. 61)[^original]  
  <sub>anchor: "secure multiparty computation and secure aggregation. Further experimentation would be beneficial."</sub>
- **expected / expectation**: The report says it is important to assess the strengths and weaknesses of each privacy-enhancing technique for the particular use case, and to consider combining different privacy-enhancing solutions. (p. 61)[^original]  
  <sub>anchor: "It is important to evaluate the strengths and weaknesses of each technique in the context of a use case"</sub>
- **descriptive / limitation**: With HE, encrypted data remain linked to an individual or business who can be re-identified with the decryption keys, so encryption of personal data could be considered pseudonymous rather than anonymous. (p. 62)[^original]  
  <sub>anchor: "the individual can be re-identified with the necessary decryption keys"</sub>
- **descriptive / limitation**: With HE there is a risk that an attacker could use side-channel attacks or other methods to decrypt data; a side-channel attack exploits weaknesses in a system's physical implementation, such as power consumption, electromagnetic leaks or sound, to extract sensitive data. (p. 62)[^original]  
  <sub>anchor: "there is a risk that an attacker could use side-channel attacks68 or other methods to decrypt data."</sub>
- **descriptive / limitation**: LDP protects sensitive information by adding random noise before sharing, making linkage to specific entities harder, but a threat actor may still be able to use external information to identify individuals. (p. 62)[^original]  
  <sub>anchor: "it may still be possible for a threat actor to use external information to identify individuals."</sub>
- **descriptive / limitation**: Federated learning could be vulnerable to data leakage attacks in which original data are reconstructed from model updates, posing a risk for both CAL 3 and CAL 4. (p. 62)[^original]  
  <sub>anchor: "FL could be vulnerable to data leakage attacks, where the original data could be reconstructed from the model updates."</sub>
- **descriptive / context**: The concept of link-ability could be relevant if illicit activity is identified in the pseudonymised data set and needs to be traced back to an identified person, subject to appropriate controls. (p. 62)[^original]  
  <sub>anchor: "The concept of link-ability could be relevant if illicit activity is identified in the pseudonymised data set"</sub>

## 4.4.5 Summary

- **descriptive / finding or result**: The experiment shows all CAL arrangements are superior to having no such arrangement for detecting financial crime; each has strengths and weaknesses but overall detection improves and false positives fall. (p. 62)[^original]  
  <sub>anchor: "the experiment shows that all CAL arrangements are superior to scenarios in which there is no such arrangement"</sub>
- **descriptive / finding or result**: The key takeaway is that sharing information and network analysis can provide innovative solutions in the fight against financial crime. (p. 62)[^original]  
  <sub>anchor: "sharing information and network analysis can provide innovative solutions in the fight against financial crime"</sub>
- **descriptive / finding or result**: Centralised cross-border (CAL 2) is the most effective method for detecting money laundering with machine learning models. (p. 62)[^original]  
  <sub>anchor: "Centralised cross-border (CAL 2) is the most effective method for detecting money laundering when using machine learning models."</sub>
- **descriptive / finding or result**: CAL 2 performs three times better in detecting money launderers and reduces false positives by 80% compared with rule-based monitoring with no CAL arrangement. (p. 62)[^original]  
  <sub>anchor: "It performs three times better in detecting money launderers and reduces the number of false positives by 80%"</sub>
- **descriptive / finding or result**: CAL 2 is also best at detecting a much larger network of money launderers, making it the most efficient at detecting cross-border money laundering. (p. 62)[^original]  
  <sub>anchor: "best at detecting a much larger network of money launderers"</sub>
- **descriptive / finding or result**: The centralised national (CAL 1) and hybrid (CAL 3) methods also showed significant improvements over rule-based monitoring with no CAL arrangement. (p. 62)[^original]  
  <sub>anchor: "The centralised national (CAL 1) and hybrid centralised national plus decentralised cross-border (CAL 3) methods also showed significant improvements"</sub>
- **descriptive / finding or result**: The hybrid model CAL 3 detected almost twice as many money launderers, reduced false positives by over 75% and detected a larger part of the money laundering network, compared with rule-based monitoring with no CAL arrangement. (p. 63)[^original]  
  <sub>anchor: "The hybrid model, CAL 3, detected almost twice as many money launderers, reduced false positives by"</sub>
- **descriptive / limitation**: National models cannot detect networks outside their borders, even if they perform better than rule-based monitoring. (p. 63)[^original]  
  <sub>anchor: "the national models cannot detect networks outside their borders, even if they perform better than rule-based monitoring"</sub>
- **descriptive / finding or result**: The fully decentralised CAL 4 improved each simulated institution's local detection, detecting twice as many money launderers as rule-based monitoring with no CAL arrangement, and reduced false positives by 40%. (p. 63)[^original]  
  <sub>anchor: "detecting twice as many money launderers compared with the rule-based monitoring with no CAL arrangement"</sub>
- **descriptive / limitation**: CAL 4 was not as effective as other CAL arrangements in detecting the full money laundering network, because underlying transaction data are not shared and each institution could only analyse its own data. (p. 63)[^original]  
  <sub>anchor: "not as effective as other CAL arrangements in detecting the full money laundering network"</sub>
- **descriptive / finding or result**: The PoC protected personal and sensitive data by encrypting and obfuscating specific data fields using a combination of PETs. (p. 63)[^original]  
  <sub>anchor: "the PoC successfully protected personal and sensitive data by encrypting and obfuscating specific data fields"</sub>
- **expected / expectation**: Because PETs have limitations and risks, it is important that there is legal clarity on the classification of privacy levels of data when encrypted; encryption does not necessarily mean data are anonymous and some PETs may only provide pseudonymisation. (p. 63)[^original]  
  <sub>anchor: "it is important that there is legal clarity regarding the classification of privacy levels of the data when encrypted"</sub>
- **descriptive / finding or result**: Combining different privacy-enhancing solutions could mitigate information security and privacy risks. (p. 63)[^original]  
  <sub>anchor: "Combining different privacy-enhancing solutions could mitigate information security and privacy risks."</sub>

## 5. Further considerations

- **descriptive / context**: Project Aurora's combination of machine learning, network analysis and PETs on synthetic data showed that CAL approaches using these technologies and payments data could be a more effective way to detect suspicious networks and illicit flows across institutions and borders. (p. 65)[^original]  
  <sub>anchor: "could be a more effective way to detect suspicious networks and illicit flows across institutions and borders"</sub>
- **descriptive / limitation**: The PoC rests on simplifying assumptions; in reality such an undertaking would face several challenges that would need to be addressed. (p. 65)[^original]  
  <sub>anchor: "in reality such an undertaking would face several challenges that would need to be addressed"</sub>

## 5.1.1 Additional data and money laundering typologies

- **descriptive / limitation**: Not all money laundering typologies can be detected solely through transaction data analysis with a minimum set of data points; depending on the typology, additional data sources and data points may be required. (p. 65)[^original]  
  <sub>anchor: "Not all money laundering typologies can be detected solely through transaction data analysis"</sub>
- **descriptive / typology or red flag**: Personal use of business accounts can be detected by monitoring KYC data such as ultimate beneficial owner (UBO) labels, tax reports and business expense receipts, or by observing large transactions from legal entities to individuals. (p. 65)[^original]  
  <sub>anchor: "This typology can be detected by monitoring know-your-customer (KYC) data such as ultimate beneficial owner (UBO) labels"</sub>
- **descriptive / typology or red flag**: Transacting with politically exposed persons (PEPs) can be detected by flagging entities and counterparties of transactions as PEPs; in a collaborative data aggregation setting this would require sharing the flag among relevant parties. (p. 65)[^original]  
  <sub>anchor: "This typology can be detected by flagging entities and counterparties of transactions as PEPs."</sub>
- **descriptive / typology or red flag**: Off-ramping into crypto assets: launderers can use cryptoassets and VASPs to hide their trail of money. (p. 65)[^original]  
  <sub>anchor: "money launderers can use these channels to hide their trail of money"</sub>
- **descriptive / typology or red flag**: Off-ramping typologies may begin in the traditional financial system but can quickly move into public blockchains where pseudonymous addresses make it difficult to link transactions to individuals or entities. (p. 65)[^original]  
  <sub>anchor: "quickly move into public blockchains in which it can be difficult to link specific transactions to individuals or entities"</sub>
- **descriptive / typology or red flag**: Detecting off-ramping typologies is stated to require additional information from VASPs (for example KYC data) and analysis of the relevant blockchain. (p. 65)[^original]  
  <sub>anchor: "Additional information from the VASPs (eg KYC data) and analysis of the relevant blockchain are necessary"</sub>
- **descriptive / typology or red flag**: Trade-based money laundering (TBML) exploits international trade to move value, often using complex financial transactions and multiple intermediaries to obscure origin and movement of funds, and artificially inflating or deflating prices of legitimate products. (p. 65)[^original]  
  <sub>anchor: "TBML involves the exploitation of international trade to move value around the world"</sub>
- **descriptive / limitation**: Although CAL arrangements can yield better results in detecting complex schemes like TBML, there can still be a lack of access to vital data for such investigations, such as invoices, shipping records, product price indices and more. (p. 66)[^original]  
  <sub>anchor: "such as invoices, shipping records, product price indices and more."</sub>

## 5.1.2 Real-world data are crucial for understanding the feasibility and impact

- **expected / expectation**: There is a need to undertake real-world pilots of CAL arrangements at scale, ideally over longer periods and in parallel with current approaches, to understand actual effectiveness, uncover further issues and support policy, data and legal discussions. (p. 66)[^original]  
  <sub>anchor: "there is a need to undertake real-world pilots at scale, ideally conducted over longer periods of time"</sub>
- **descriptive / context**: There is currently no clear consensus on how CAL approaches, particularly cross-border, can be arranged; the arrangements explored in Project Aurora could be fed into these discussions. (p. 66)[^original]  
  <sub>anchor: "There is currently no clear consensus on how CAL approaches, particularly in a cross-border context, can be arranged."</sub>
- **expected / expectation**: Designing CAL arrangements would require consideration of key issues including funding, membership, governance, objectives and performance monitoring. (p. 66)[^original]  
  <sub>anchor: "These include funding, membership, governance, objectives and performance monitoring."</sub>
- **expected / expectation**: Consideration of the nature of analytical capabilities and the scope of crimes covered by the analysis would be necessary. (p. 66)[^original]  
  <sub>anchor: "consideration of the nature of analytical capabilities and the scope of the crimes covered by the analysis would be necessary"</sub>
- **expected / expectation**: Issues of visibility, control, liability for data and analysis, audit and assurance, and the role of public agencies also require examination. (p. 66)[^original]  
  <sub>anchor: "Issues relating to visibility, control, liability for data and analysis, audit and assurance"</sub>
- **descriptive / context**: ISO 20022 messaging standards include additional standardised data points which could potentially improve CAL efforts to combat financial crime. (p. 66)[^original]  
  <sub>anchor: "ISO 20022 messaging standards include additional standardised data points which could potentially improve CAL efforts"</sub>
- **permissive / recommendation**: Further practical work on how ISO 20022-based data could be leveraged for use cases including financial crime, including identifying enhancements to the standard, could be beneficial. (p. 66)[^original]  
  <sub>anchor: "Further practical work to better understand how ISO 20022-based data could be leveraged for a variety of use cases"</sub>
- **permissive / recommendation**: Objectives for achieving a standardised data framework for national and cross-border financial crime detection could be considered. (p. 66)[^original]  
  <sub>anchor: "Objectives for achieving a standardised data framework for national and cross-border financial crime detection could be considered."</sub>
- **descriptive / context**: Additional issues for developing CAL arrangements include defining the types of data to be utilised, the use of PETs and desired privacy protection levels, ensuring cyber and information security, defining operating procedures and professional standards, and engaging law enforcement agencies. (p. 67)[^original]  
  <sub>anchor: "defining the types of data to be utilised, the use of privacy-enhancing technologies and desired privacy protection levels"</sub>
- **descriptive / context**: Questions to support the design of real-world pilots are in Annex D. (p. 67)[^original]  
  <sub>anchor: "Questions to support the design of real-world pilots can be found in Annex D."</sub>

## 5.1.3 Limitations of payments data and the need for other data

- **descriptive / finding or result**: Network-wide transaction data give a large analytical advantage in discovering previously unknown accounts linked to high-risk or suspicious activity. (p. 67)[^original]  
  <sub>anchor: "Network-wide transaction data provide a large analytical advantage in discovering previously unknown accounts linked to high-risk"</sub>
- **descriptive / limitation**: Approaches with less visibility, or limits and thresholds on input data, benefit from data minimisation and less privacy intrusion, but there is a trade-off of reduced efficacy in identifying network-wide risks not visible to individual members. (p. 67)[^original]  
  <sub>anchor: "there is a trade-off, in terms of reduced efficacy, in being able to identify network-wide risks"</sub>
- **descriptive / context**: The principles of data minimisation and purpose limitation are important. (p. 67)[^original]  
  <sub>anchor: "The principles of data minimisation and purpose limitation are important."</sub>
- **descriptive / limitation**: Payments-level data alone may not give a complete view of financial crime risk, and additional data such as KYC, tax authority or corporate registry data could be required depending on the crime targeted. (p. 67)[^original]  
  <sub>anchor: "payments-level data alone may not provide a complete view of financial crime risk"</sub>
- **descriptive / limitation**: A principal challenge in current AML system design is that an individual institution's visibility on payments is limited to those made by its customers and relevant counterparties, and its KYC awareness is limited to its direct customer interactions. (p. 67)[^original]  
  <sub>anchor: "visibility on payments of individual financial institutions is limited to those made by customers and relevant counterparties"</sub>
- **descriptive / limitation**: National and international payments infrastructure could have much greater visibility on payment flows between institutions but no visibility on KYC data. (p. 67)[^original]  
  <sub>anchor: "could have much greater visibility on payment flows between financial institutions, but no visibility on KYC data"</sub>

## 5.1.4 Data protection

- **expected / expectation**: For responsible and ethical data sharing and processing it is important to establish a transparent process and open dialogue, which can facilitate clear legislation and guidelines and promote innovation and consistency in collaboration frameworks. (p. 67)[^original]  
  <sub>anchor: "it is important to establish a transparent process and open dialogue"</sub>
- **expected / expectation**: Protecting data and privacy and combatting financial crime are significant public interests that need to be balanced; they are not mutually exclusive but complementary. (p. 67)[^original]  
  <sub>anchor: "are significant public interests that need to be balanced"</sub>
- **expected / expectation**: It is crucial to uphold the rights of those whose data are shared while strictly limiting processing of data to its intended purpose to prevent misuse of personal information. (p. 67)[^original]  
  <sub>anchor: "It is crucial to uphold the rights of those whose data are being shared"</sub>

## 5.2.1 Technical challenges with CAL arrangements

- **descriptive / limitation**: Data quality and consistency challenge: differences in data collection, storage and processing methods among institutions may cause inconsistencies, discrepancies or biases in shared data, affecting detection model performance. (p. 67)[^original]  
  <sub>anchor: "Differences in data collection, storage and processing methods among financial institutions may lead to inconsistencies"</sub>
- **mandatory / requirement**: To address data quality and consistency, FIs must agree on standard data collection and processing methods and implement data quality control mechanisms to ensure consistency and accuracy in shared data. (p. 67)[^original]  
  <sub>anchor: "FIs must agree on standard data collection and processing methods and implement data quality control mechanisms"</sub>
- **descriptive / limitation**: Feature selection and engineering challenge: consistently identifying the most important factors for detecting money laundering becomes challenging in collaborative settings with multiple institutions. (p. 67)[^original]  
  <sub>anchor: "Ensuring consistent identification of the most important factors or characteristics for detecting money laundering becomes challenging"</sub>
- **permissive / recommendation**: To address feature selection, financial institutions can work together to establish a shared framework for selecting and analysing the important factors. (p. 67)[^original]  
  <sub>anchor: "financial institutions can work together to establish a shared framework for selecting and analysing these important factors"</sub>
- **descriptive / limitation**: Computational cost and information overload challenge: many machine learning models and PETs face high computational costs which may increase non-linearly with large data volumes, and data volumes would be very large depending on jurisdiction and institutions involved. (p. 67)[^original]  
  <sub>anchor: "Many machine learning models and PETs currently face the challenge of high computational costs"</sub>

## 5.2 Technology

- **descriptive / finding or result**: In Project Aurora, the potential risk of machine learning bias is limited because the synthetic data generation process is simple and transparent and the statistical simulation does not add bias to the training sample. (p. 67)[^original]  
  <sub>anchor: "the potential risk of machine learning bias is mitigated because the synthetic data generation process is simple and transparent"</sub>

## 5.2.1 Technical challenges with CAL arrangements

- **expected / expectation**: The private and public sectors should cooperate to find an efficient solution for the monitoring system. (p. 68)[^original]  
  <sub>anchor: "The private and public sectors should cooperate to find an efficient solution for the monitoring system."</sub>
- **descriptive / limitation**: Model divergence challenge: with federated learning there is a risk the model underfits or overfits if training data sets contain limited information or differ greatly in data structure. (p. 68)[^original]  
  <sub>anchor: "there is a risk that the model might not work well, either underfitting or overfitting"</sub>
- **expected / expectation**: To prevent model divergence, financial institutions should collaborate on reviewing the model and consolidate the data structure and standards. (p. 68)[^original]  
  <sub>anchor: "financial institutions should collaborate on reviewing the model, and consolidate the data structure and standards"</sub>
- **descriptive / limitation**: Lack of real-world labels globally: it can be difficult to obtain accurate and trustworthy information to identify money laundering globally, and information held by one institution or country may not apply elsewhere. (p. 68)[^original]  
  <sub>anchor: "it can be difficult to obtain accurate and trustworthy information"</sub>
- **permissive / recommendation**: To address the lack of labels, financial institutions can create a way for experts to provide feedback on the system, helping ensure it receives accurate information and improves over time. (p. 68)[^original]  
  <sub>anchor: "financial institutions can create a way for experts to provide feedback on the system"</sub>
- **expected / expectation**: Fairness and impartiality: when machine learning is used for AML it is essential to evaluate the fairness and impartiality of the monitoring model and the policy recommendations. (p. 68)[^original]  
  <sub>anchor: "it is essential to evaluate the fairness and impartiality of the monitoring model and the policy recommendations"</sub>
- **descriptive / finding or result**: Variables usually associated with bias and discrimination, such as gender and other demographic information, are not part of the synthetic data, and the project's models are explainable, which helps examine potential model biases. (p. 68)[^original]  
  <sub>anchor: "variables usually associated with bias and discrimination, eg gender and other demographic information, are not part"</sub>
- **descriptive / limitation**: Governance, risk management and information security: a CAL arrangement could be a potential honeypot of data and, given its relevance to disrupting organised crime, at risk of cyber attacks, infiltration and data corruption from threats such as organised crime, insiders, kleptocrats and malign state actors. (p. 68)[^original]  
  <sub>anchor: "CAL arrangements could be at risk of cyber security attacks, infiltration and data corruption attempts"</sub>
- **expected / expectation**: Governance, risk management, conduct and assurance processes will need to mitigate cyber security and information security risks for CAL arrangements. (p. 68)[^original]  
  <sub>anchor: "Governance, risk management, conduct and assurance processes will need to mitigate cyber security and information security risks."</sub>
- **descriptive / limitation**: Utility: a CAL arrangement is only as good as the number of participants and data sources available. (p. 68)[^original]  
  <sub>anchor: "Any CAL arrangement would only be as good as the number of participants and data sources available."</sub>

## 5.2.2 Machine readable typologies that facilitate information sharing

- **descriptive / context**: In cyber security, real-time indicators are shared and standards enabling automated exchange of cyber threat intelligence have been implemented to combat immediate threats. (p. 69)[^original]  
  <sub>anchor: "standards to enable the automated exchange of cyber threat intelligence have been implemented,70"</sub>
- **descriptive / limitation**: In AML, data to be shared such as financial crime typologies are not standardised in definition or description and are unstructured and analogue, making them hard to use for data analysis. (p. 69)[^original]  
  <sub>anchor: "are not standardised in their definitions or descriptions, and are unstructured and analogue in format."</sub>
- **permissive / recommendation**: Representing typologies as knowledge graphs suitable for information-sharing and analysis by advanced analytical systems could provide a solution, which public and private sectors could collaborate on and which could build on existing efforts such as the European Financial Intelligence Public Private Partnership (EFIPPP). (p. 69)[^original]  
  <sub>anchor: "Representing typologies as knowledge graphs, that may be suitable for information-sharing and analysis"</sub>
- **descriptive / context**: EFIPPP consists of large financial institutions, FIUs and law enforcement agencies from multiple jurisdictions and shares information on typologies such as investment frauds, trade-based money laundering, virtual assets and narcotics. (p. 69)[^original]  
  <sub>anchor: "EFIPPP consists of large financial institutions, FIUs and law enforcement agencies from multiple jurisdictions."</sub>

## What is a knowledge graph and how could it apply to AML efforts?

- **descriptive / definition**: A knowledge graph is a dynamic data structure that encodes information as a network of data points (nodes) and relationships between them (edges), and can include semantics such as synonyms, taxonomies or ontologies. (p. 69)[^original]  
  <sub>anchor: "A knowledge graph is a type of dynamic data structure that encodes information as a network of different data points"</sub>
- **descriptive / context**: Knowledge graphs can support entity resolution, determining whether data fields with different names or descriptions are the same thing, which is useful at scale where data consistency matters, as in AML. (p. 69)[^original]  
  <sub>anchor: "whether one or more data fields with different names or descriptions are in fact the same thing (entity resolution)"</sub>
- **descriptive / context**: Knowledge graphs give a comprehensive view of information with relationships, context and meaning, can drive new insights, and can be updated dynamically as new information, such as missing data items or hidden relationships, becomes available. (p. 69)[^original]  
  <sub>anchor: "Knowledge graphs can be updated dynamically as new information becomes available"</sub>
- **descriptive / method**: Knowledge graphs support exploration, deduction and inference: a graph query can look for features warranting investigation, graph algorithms can identify new patterns, and graph embeddings can learn from graph data to find new connections based on shared characteristics, including customer behaviour features. (p. 69)[^original]  
  <sub>anchor: "a graph query can look for specific features that warrant further investigation and graph algorithms can identify new patterns"</sub>
- **permissive / context**: Knowledge graphs could be particularly useful for AML by representing typology knowledge in digital form, which could be encoded and made available to financial institutions and authorities for advanced analytical systems, supporting collaboration, information-sharing, better detection and timely responses. (p. 70)[^original]  
  <sub>anchor: "Knowledge graphs could be particularly useful for AML by representing knowledge about typologies in digital form."</sub>
- **descriptive / data or feature**: A typology knowledge graph could conceptually include: data fields, data types, data sources, security and privacy classifications; synonyms, taxonomies or ontologies; transaction features; behaviours; actors and activities; explainable criteria; suspicious and related activities; and references to laws, regulations or guidelines. (p. 70)[^original]  
  <sub>anchor: "data fields, data types, data sources, security and privacy classifications;"</sub>
- **descriptive / limitation**: Further analysis and experimentation would be required for the typology knowledge graph concept. (p. 70)[^original]  
  <sub>anchor: "Further analysis and experimentation would be required."</sub>

## 5.2.3 Explainability

- **expected / expectation**: Understanding how machine learning models arrive at their results (model-explainability) is critical; different models need different approaches, and explainability is crucial for transparency, fairness and accountability. (p. 70)[^original]  
  <sub>anchor: "Understanding how machine learning models arrive at their final results is critical"</sub>
- **descriptive / context**: Being flagged as a suspicious customer can significantly affect individuals and businesses, from inconvenience to financial exclusion. (p. 70)[^original]  
  <sub>anchor: "Being flagged as a suspicious customer can have a significant impact on individuals and businesses"</sub>
- **expected / expectation**: It is important for financial institutions to understand and explain how models work and how findings are calculated, to avoid black box models that can lead to unfair, biased or discriminatory AML practices. (p. 70)[^original]  
  <sub>anchor: "It is therefore important for financial institutions to understand and explain how the models work"</sub>
- **descriptive / finding or result**: The features used in the PoC are inherently explainable because they are created by aggregating data points on pre-defined criteria, and examining the data points without aggregation shows what information went into each feature. (p. 71)[^original]  
  <sub>anchor: "By investigating the data points without aggregation, one can understand the information that went into each feature."</sub>
- **expected / expectation**: While explainability is critical, it is also crucial to consider model governance, legal risks and regulatory compliance at an early stage. (p. 71)[^original]  
  <sub>anchor: "crucial to consider other factors such as model governance, legal risks and regulatory compliance at an early stage"</sub>
- **descriptive / definition**: Model governance involves establishing a framework to ensure machine learning models are developed, deployed and maintained responsibly and accountably. (p. 71)[^original]  
  <sub>anchor: "establishing a framework to ensure that machine learning models are developed, deployed and maintained in a responsible"</sub>
- **permissive / recommendation**: Model governance could include maintaining an overview of the machine learning models in use, allocating appropriate resources for ongoing evaluation, weighing the trade-off between improved performance and high complexity/low explainability, and fostering the sharing of best practices. (p. 71)[^original]  
  <sub>anchor: "creating and maintaining an overview of the machine learning models that are being used"</sub>

## 5.3.1 Instant payment systems, CBDC systems and financial crime

- **descriptive / context**: CBDC systems may bring new participants and different ways of facilitating payments, creating new vectors for financial crime. (p. 71)[^original]  
  <sub>anchor: "may result in new participants and may enable different ways of facilitating payments, creating new vectors for financial crime"</sub>
- **expected / expectation**: It is crucial to assess potential criminal misuse of instant payment and CBDC systems and whether they could create new avenues for combating financial crime. (p. 71)[^original]  
  <sub>anchor: "It is crucial to assess the potential misuse of these systems by criminals"</sub>
- **expected / expectation**: It is important that operators (private sector or central banks) work with participating financial institutions to ensure appropriate financial crime controls are in place. (p. 71)[^original]  
  <sub>anchor: "It is therefore important that operators (eg private sector or central banks) work together with financial institutions"</sub>

## 5.3.2 Legal and regulatory considerations

- **recommended / recommendation**: To realise the potential benefits of CAL arrangements that use payments data, the report says a national and cross-border strategy for public-private partnerships to combat financial crime would be beneficial. (p. 71)[^original]  
  <sub>anchor: "a national and cross-border strategy for public-private partnerships to combat financial crime would be beneficial"</sub>

## 5.3.1 Instant payment systems, CBDC systems and financial crime

- **permissive / recommendation**: Operators could conduct preparatory work with public and private organisations, collaborating with government agencies and financial institutions on information and best practices, to understand domestic and cross-border typologies (money laundering, terrorist financing, other illicit activities) that may emerge in instant payment and CBDC systems. (p. 72)[^original]  
  <sub>anchor: "Operators could conduct preparatory work with public and private organisations to develop a clear understanding"</sub>
- **permissive / context**: The approaches explored in the project could be used by operators of IPS or CBDC systems with AML monitoring and analysis capabilities to enable greater detection of suspicious activity networks, subject to limits on the types of launderers detectable with the data available. (p. 72)[^original]  
  <sub>anchor: "The approaches explored in this project could be used by operators considering IPS or CBDC systems"</sub>
- **expected / expectation**: It is important to ensure financial crime measures do not interfere with the efficiency and speed of payments while still providing guidance and regulation so participants take adequate measures. (p. 72)[^original]  
  <sub>anchor: "It is important to ensure that financial crime measures do not interfere with the efficiency and speed of payments"</sub>
- **expected / expectation**: A legal framework would need to be in place to govern the use of instant payment and CBDC systems for AML and other financial crime prevention. (p. 72)[^original]  
  <sub>anchor: "A legal framework would need to be in place to govern the use of these systems for AML"</sub>

## 5.3.2 Legal and regulatory considerations

- **expected / expectation**: A public-private partnership for CAL would require a clear legal basis to enable information-sharing and collaborative analytics. (p. 72)[^original]  
  <sub>anchor: "Such a public-private partnership would require a clear legal basis to enable information-sharing and collaborative analytics."</sub>
- **descriptive / context**: Depending on the CAL arrangement and technologies, different legal, privacy, ethical, policy and regulatory implications may need to be considered, and legislation allowing one type of collaboration may or may not support another. (p. 72)[^original]  
  <sub>anchor: "Legislation that allows for one type of collaboration may or may not support another."</sub>
- **permissive / recommendation**: Policymakers could reflect on the holistic capabilities needed, which could include development of financial crime threat typologies, network detection, transaction monitoring, incident reporting, evidence recording and reporting packs. (p. 72)[^original]  
  <sub>anchor: "the development of financial crime threat typologies, network detection, transaction monitoring, incident reporting, evidence recording and reporting packs"</sub>
- **expected / expectation**: Collaboration between public authorities and the private sector in creating an appropriate legal and regulatory framework is essential to support CAL arrangements. (p. 72)[^original]  
  <sub>anchor: "Collaboration between public authorities and the private sector in creating an appropriate legal and regulatory framework is essential"</sub>
- **descriptive / limitation**: Without a legal basis, data privacy risks, civil damages, defamation, competition law risk, bank secrecy and AML framework prohibitions against tipping off could hinder CAL initiatives; tipping off is a legal prohibition on disclosing that a suspicious transaction report or related information is being filed with an FIU. (p. 72)[^original]  
  <sub>anchor: "data privacy risks, civil damages, defamation, competition law risk, bank secrecy and AML framework prohibitions against tipping off74"</sub>

## 6. Conclusion

- **descriptive / finding or result**: Project Aurora demonstrated that analysis of payments data is highly valuable for AML, offering greater visibility and improved detection of suspicious networks and illicit flows across institutions and borders. (p. 73)[^original]  
  <sub>anchor: "Project Aurora has demonstrated that analysis of payments data is highly valuable for AML."</sub>
- **descriptive / finding or result**: The main findings suggest behavioural-based transaction monitoring and analysis at national or international levels is more effective in detecting money launderers and suspicious networks than current siloed, rule-based monitoring, and graph neural networks appear optimal for this use case. (p. 74)[^original]  
  <sub>anchor: "behavioural-based transaction monitoring and analysis at national or international levels is more effective in detecting money launderers and suspicious networks"</sub>
- **descriptive / finding or result**: PETs can be leveraged to allow secure, privacy-preserving CAL arrangements, including federated-learning model training across institutions and borders, supporting privacy-preserving international AML monitoring. (p. 74)[^original]  
  <sub>anchor: "Privacy-enhancing technologies can be leveraged to allow secure and privacy-preserving CAL arrangements"</sub>
- **descriptive / limitation**: There are several barriers to overcome and potential limitations of the technologies and approaches; future advances may remove some. (p. 74)[^original]  
  <sub>anchor: "There are several barriers to overcome, as well as some potential limitations associated with the technologies and approaches."</sub>
- **descriptive / context**: Initiatives that could positively affect data-driven efforts against financial crime include the G20 roadmap for cross-border payments, national transaction monitoring utilities, behaviour-focused advanced analytics, migration to ISO 20022 and the ongoing review of FATF Recommendation 16. (p. 74)[^original]  
  <sub>anchor: "the migration of payments systems to the ISO 20022 messaging standard and the ongoing review of FATF recommendation 16"</sub>
- **permissive / recommendation**: Greater cross-functional dialogue between payments, financial crime and data protection experts could support development of data standards, for example leveraging ISO 20022, greater use of the LEI, beneficial ownership standards and standardised typology representation. (p. 74)[^original]  
  <sub>anchor: "Greater cross-functional dialogue between experts on payments, financial crime and data protection could support the development of data standards."</sub>
- **descriptive / context**: The conclusion says the technologies and approaches discussed could play a role in catalysing public-private partnerships and collaborative analytics and learning. (p. 74)[^original]  
  <sub>anchor: "could play a role in catalysing approaches to public-private partnerships, and collaborative analytics and learning"</sub>
- **descriptive / context**: The conclusion states that stronger cooperation between the private and public sectors, between different disciplines and across national borders is a key driver of innovation to improve AML efforts. (p. 74)[^original]  
  <sub>anchor: "Strengthened cooperation between the private and public sectors, between different disciplines and across national borders"</sub>
- **recommended / recommendation**: Policymakers have already recognised the need for a strategic approach to encouraging and co-designing the capabilities needed for private-private information-sharing to detect financial crime; the report adds that further strategic work on public-private initiatives would be valuable. (p. 74)[^original]  
  <sub>anchor: "further strategic work on public-private initiatives would be valuable"</sub>

## Further work

- **expected / expectation**: Real-world proofs of concept or pilots with a range of actors across the payments landscape would be needed to test feasibility and effectiveness at scale and surface legal, regulatory, data protection and technical issues. (p. 75)[^original]  
  <sub>anchor: "real-world proofs of concept (or pilots) with a range of different actors across the payments landscape would be needed"</sub>
- **permissive / recommendation**: The machine readable typology concept using knowledge graphs could be explored further with public and private sector experts as a technical and process design exercise. (p. 75)[^original]  
  <sub>anchor: "The machine readable typology concept using knowledge graphs proposed in this report could be explored further"</sub>
- **permissive / context**: Instant payment systems and potential CBDC systems could play a key role in detecting money launderers and suspicious networks depending on design; PETs and data minimisation could be important in achieving this. (p. 75)[^original]  
  <sub>anchor: "Instant payment systems and potential CBDC systems could also play a key role in detecting money launderers and suspicious networks"</sub>
- **permissive / recommendation**: CBDC systems could provide a new vector for money launderers, so early preparatory work to simulate potential financial crime typologies affecting CBDC systems could be beneficial. (p. 76)[^original]  
  <sub>anchor: "undertaking some preparatory work at an early stage to simulate potential financial crime typologies75"</sub>
- **descriptive / context**: Some known typologies may extend to CBDC systems and some characteristics may be common, but new typologies emerge all the time. (p. 76)[^original]  
  <sub>anchor: "new typologies emerge all the time, although some characteristics may be common"</sub>

---

[previous part](digest-003.md) | [source overview](overview.md) | [next part](digest-005.md)

[^original]: Bank for International Settlements / Basel Committee, "Project Aurora: the power of data, technology and collaboration to combat money laundering across institutions and borders" (2023-05-31). https://www.bis.org/publications/project-aurora-power-data-technology-and-collaboration-combat-money-laundering-across-institutions-and-borders
