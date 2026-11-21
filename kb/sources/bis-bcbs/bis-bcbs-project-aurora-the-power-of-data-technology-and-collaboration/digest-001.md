---
type: Source Digest
title: 'Project Aurora: the power of data, technology and collaboration to combat money laundering across institutions and borders - part 1 of 6 (pp. 1-18)'
description: 'Verified paraphrased digest, pp. 1-18: Project Aurora; Project Aurora > Preface: How to read this report; Project Aurora > Contents'
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
part: 1
parts_total: 6
content_mode: digest
generated:
  by: claude-code-subagent/claude-sonnet-5-5
  at: '2026-11-21T08:40:40Z'
verified:
- by: process:kb-digest-check/anchor-match
  at: '2026-11-21T08:40:40Z'
- by: claude-code-judge-agent/claude-opus-5-5
  at: '2026-11-21T08:40:40Z'
sources:
- id: original
  resource: https://www.bis.org/publications/project-aurora-power-data-technology-and-collaboration-combat-money-laundering-across-institutions-and-borders
  title: 'Project Aurora: the power of data, technology and collaboration to combat money laundering across institutions and borders'
  author: org:bis_bcbs
  last_modified: '2023-05-31T00:00:00Z'
digest_points: 84
---

# Project Aurora: the power of data, technology and collaboration to combat money laundering across institutions and borders (digest)

[source overview](overview.md) | [next part](digest-002.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (pp. 1-18) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **international standard**.

## 1. Acronyms, abbreviations and definitions

- **descriptive / definition**: Project Aurora defines AML (anti-money laundering) as all kinds of actions, including rules, legislation, principles, regulations, processes and tools specific to the financial sector, with the objective of tackling the laundering of illicitly obtained funds by criminals. (p. 7)[^original]  
  <sub>anchor: "with the objectiveof tacklingthe launderingof illicitlyobtained funds bycriminals."</sub>
- **descriptive / definition**: Artificial neural networks (ANN) are a subset of machine learning inspired by a simplification of neurons in a brain, and can be applied to model complicated network relationships and patterns. (p. 7)[^original]  
  <sub>anchor: "Artificial neural networks are a subset of machine learning, inspired by a simplification ofneurons in a brain."</sub>
- **descriptive / definition**: CAL (collaborative analysis and learning) is a collective term for approaches in which parties either collaborate by sharing and analysing data in a centralised manner, or collaborate in a decentralised manner using federated learning to train a model on local data and update those learnings in a common model shared with all parties. (p. 7)[^original]  
  <sub>anchor: "either collaborate by sharing and analysing data in a centralised manner"</sub>
- **descriptive / definition**: Hybrid CAL comprises both centralised and decentralised approaches. (p. 7)[^original]  
  <sub>anchor: "Hybrid CAL comprises both centralised and decentralised"</sub>
- **descriptive / definition**: CFT (countering the financing of terrorism) is closely related to anti-money laundering and involves similar actions and forces, aiming to tackle terrorist financing. (p. 7)[^original]  
  <sub>anchor: "Countering the financing of terrorism is closely related to anti-money laundering and involvessimilar actions and forces."</sub>
- **descriptive / definition**: CLS (complex layering schemes) involve a complex network of multiple accounts across different financial institutions that are often used for money laundering. (p. 7)[^original]  
  <sub>anchor: "Complex layering schemes involve a complex network of multiple accounts across"</sub>
- **descriptive / definition**: FL (federated learning) is a decentralised machine learning framework enabling multiple entities to train a shared model collaboratively without exchanging raw data. (p. 7)[^original]  
  <sub>anchor: "Federated learning is a decentralised machine learning framework that enables multipleentities to train a shared model"</sub>
- **descriptive / definition**: GNN (graph neural networks) are a class of artificial neural networks that operate on graph-structured data containing a set of relationships between actors (edges and nodes). (p. 7)[^original]  
  <sub>anchor: "Graph neural networks are a class of artificial neural networks that operate on graph-structured data"</sub>
- **descriptive / definition**: HE (homomorphic encryption) is a specific kind of encryption that allows computation on data without revealing the underlying data. (p. 7)[^original]  
  <sub>anchor: "Homomorphic encryption is a specific kind of encryption that allows computation of datawithout revealingthe underlyingdata."</sub>
- **descriptive / definition**: ISO 20022 provides a common language and structure for financial messages that can be used within and across different payment systems and jurisdictions. (p. 7)[^original]  
  <sub>anchor: "The ISO 20022 standard provides a common language and structure for financial messagesthat can be used"</sub>
- **descriptive / definition**: KYC (know your customer/client) is described as mandatory standards used in the investment and financial services industry to verify customers and understand their risk and financial profiles. (p. 7)[^original]  
  <sub>anchor: "Know your customer/client are mandatory standards used in the investment and financialservices industryto verifycustomers"</sub>
- **descriptive / definition**: Money mule networks consist of individuals who intentionally or unintentionally launder money by receiving and transferring illegal profits on behalf of someone else. (p. 7)[^original]  
  <sub>anchor: "Money mules consist of individuals who intentionally, or unintentionally, launder money"</sub>
- **descriptive / definition**: Monitoring scenarios means transaction data visible on three levels for analysis: the view of each financial institution (siloed), the national view of a single country and the cross-border view across countries. (p. 7)[^original]  
  <sub>anchor: "Transaction data visible on three different levels for analysis, ie the view of each financialinstitution (siloed)"</sub>
- **descriptive / definition**: MPC (secure multi-party computation) is a cryptographic toolbox allowing multiple parties to make calculations using their combined data without revealing their individual data. (p. 7)[^original]  
  <sub>anchor: "Secure multi-party computation is a cryptographic toolbox that allows multiple parties tomake calculations"</sub>
- **descriptive / definition**: PETs (privacy-enhancing technologies) are a broad range of technologies designed to extract data value without risking fundamental data protection principles. (p. 7)[^original]  
  <sub>anchor: "Privacy-enhancing technologies are a broad range of technologies that are designed to"</sub>
- **descriptive / definition**: Other abbreviations in the glossary: BIS (Bank for International Settlements), CPMI (Committee on Payments and Market Infrastructures), FATF (Financial Action Task Force), FIU (financial intelligence unit), FSB (Financial Stability Board), IPS (instant payment system), LEA (law enforcement agency), LEI (legal entity identifier), LDP (local differential privacy), PII (personally identifiable information), PPP (public-private partnership) and TMU (transaction monitoring utility). (p. 7)[^original]  
  <sub>anchor: "The project specific acronyms, abbreviations and definitions used in Project Aurora are listed in bold."</sub>
- **descriptive / definition**: Smurfing is the act of breaking up the proceeds of illicit funds into small amounts that can easily be hidden amongst other small transactions. (p. 8)[^original]  
  <sub>anchor: "The act of breaking up the proceeds of illicit funds into small amounts that can easily behidden"</sub>
- **descriptive / definition**: Synthetic data is information on real-world data that is artificially trained to reproduce the characteristics and structure of the original data. (p. 8)[^original]  
  <sub>anchor: "Information on real-world data that is artificially trained to reproduce the characteristics andstructure of the original data."</sub>
- **descriptive / definition**: TBML (trade-based money laundering) is a method used by criminals to launder the proceeds of illicit activities through the international trade system. (p. 8)[^original]  
  <sub>anchor: "Trade-based money laundering is a method used by criminals to launder the proceeds of illicitactivities through the international trade system."</sub>
- **descriptive / definition**: VASPs (virtual asset service providers) are any natural or legal persons who exchange, hold, safekeep, sell, convert or otherwise transfer virtual assets, for example cryptocurrency exchanges. (p. 8)[^original]  
  <sub>anchor: "Virtual asset service providers are any natural or legal persons who exchange, hold, safekeep,sell, convert or otherwise transfer virtual assets"</sub>

## 2.1 Background

- **descriptive / context**: Financial institutions currently monitor transactions for suspicious activities in a siloed way, which is ineffective because many payment transactions are complex and involve interconnected networks spanning multiple institutions and borders; criminals operate in networks and exploit this complexity. (p. 10)[^original]  
  <sub>anchor: "Currently, financial institutions monitor transactions for suspicious activities in a siloed way."</sub>
- **expected / expectation**: A network view of payments data is essential to combat money laundering, because both legitimate and illicit transactions flow through payment systems. (p. 10)[^original]  
  <sub>anchor: "A network view of payments data is essential to combat money laundering."</sub>
- **descriptive / data or feature**: Financial institutions report exposure to rising financial crime: 67% are exposed to financial crimes involving digital payments and over 60% to various forms of money laundering (Lexis Nexis 2022). (p. 10)[^original]  
  <sub>anchor: "with 67% exposed to financial crimes involving digital payments and over 60% to various forms of money laundering.1"</sub>
- **descriptive / data or feature**: The amount of money laundered globally is estimated at between 2 and 5% of global GDP, or between $2 trillion and $5 trillion. (p. 10)[^original]  
  <sub>anchor: "The amount of money laundered globally is estimated to be between 2 and 5% of global GDP"</sub>
- **descriptive / data or feature**: The estimated total sum seized annually is less than 1% of the laundered amount, between $20 billion and $50 billion. (p. 10)[^original]  
  <sub>anchor: "the estimated total sum seized annually amounts to less than 1% of this"</sub>
- **descriptive / limitation**: The UNODC source states $800 billion to $2 trillion based on global GDP at the time of writing; recalculated on 2022 global GDP of approximately $100 trillion it becomes $2 trillion to $5 trillion, and it is difficult to estimate the total amount that goes through the laundering cycle. (p. 10)[^original]  
  <sub>anchor: "The source states $800 billion to $2 trillion based on global GDP at the time of writing."</sub>
- **descriptive / data or feature**: A 2022 study found financial institutions face compliance costs of approximately $274 billion globally, an increase of approximately 28% on the 2020 figure of approximately $214 billion. (p. 10)[^original]  
  <sub>anchor: "an increase of approximately 28% on the 2020 figure of approximately $214 billion.5"</sub>
- **descriptive / data or feature**: Between 2019 and 2022 average compliance costs grew by approximately 54% in the United States, 80% in Canada, 30% in Germany and 23% in France. (p. 10)[^original]  
  <sub>anchor: "grew by approximately 54% in the United States, 80% in Canada, 30% in Germany and 23% in France."</sub>
- **descriptive / data or feature**: Asked about major factors driving compliance costs, 68% of financial institutions cited increasing AML regulation and another 68% cited evolving criminal threats. (p. 10)[^original]  
  <sub>anchor: "increasing anti-money laundering (AML) regulation was cited by 68% of financial institutions, while another 68% cited evolving criminal threats."</sub>
- **descriptive / context**: Cost drivers combined with the risk of sanction have contributed to financial institutions adopting a defensive approach to AML compliance, which can lead to over-reporting to authorities and a drain on public resources. (p. 10)[^original]  
  <sub>anchor: "This defensive approach can lead to over-reporting to authorities, which can become a drain on public resources."</sub>
- **descriptive / context**: The defensive approach can also result in termination of customer relationships to reduce overall exposure to financial crime risk, known as de-risking. (p. 10)[^original]  
  <sub>anchor: "termination of customer relationships to reduce overall exposure to financial crime risk"</sub>
- **descriptive / context**: The FATF has identified data-sharing and collaborative analytics as critical for effective AML and CFT efforts. (p. 10)[^original]  
  <sub>anchor: "data-sharing and collaborative analytics are critical for effective antimoney laundering and countering the financing of terrorism"</sub>
- **permissive / context**: Sharing information could also support customer due diligence measures such as institutional risk assessment, customer onboarding, risk management of a business relationship and identification of the beneficial owner, and could help identify and share patterns and flows such as typologies. (p. 10)[^original]  
  <sub>anchor: "Sharing information could also support customer due diligence measures such as institutional risk assessment"</sub>
- **descriptive / context**: In its stocktake on data pooling, collaborative analytics and data protection, the FATF outlined technologies and approaches that could improve AML/CFT efforts: different approaches to data-sharing, privacy-enhancing technologies, advanced analytics, data standardisation and data protection. (p. 11)[^original]  
  <sub>anchor: "different approaches to data-sharing,12 privacy-enhancing technologies (PET),13 advanced analytics,14 data standardisation15 and data protection.16"</sub>
- **descriptive / context**: Digital transformation to enhance AML/CFT efforts is a strategic priority of the FATF. (p. 11)[^original]  
  <sub>anchor: "Digital transformation to enhance AML/CFT efforts is a strategic priority of the FATF.17"</sub>
- **descriptive / definition**: Advanced analytics such as machine learning, federated learning, deep learning, network analysis and natural language processing can analyse large amounts of structured and unstructured data more efficiently and identify patterns and trends more effectively. (p. 11)[^original]  
  <sub>anchor: "Advanced analytics such as machine learning, federated learning, deep learning, network analysis and natural language processing"</sub>

## 2.2 Data, technology and innovation

- **descriptive / context**: In 2020 the G20 leaders endorsed a Roadmap for enhancing cross-border payments; as part of its prioritisation plan the FATF is considering updating Recommendation 16 (the travel rule) to reflect developments in payment system architecture, including adoption of ISO 20022 messaging standards. (p. 11)[^original]  
  <sub>anchor: "the FATF is also considering updating its recommendation 16 (the travel rule)18 to take into account developments"</sub>
- **descriptive / context**: Updating the travel rule for ISO 20022 is intended to improve the consistency and usability of payment message data in cross-border payments and could facilitate more efficient AML/CFT checks. (p. 11)[^original]  
  <sub>anchor: "This is to improve the consistency and usability of payment message data in cross-border payments"</sub>
- **descriptive / definition**: Collaborative approaches to analysis include centralised, decentralised or hybrid arrangements at national and cross-border level, discussed further in section 4.4. (p. 11)[^original]  
  <sub>anchor: "Collaborative approaches to analysis include centralised, decentralised or hybrid"</sub>
- **descriptive / context**: Protection of individual and fundamental privacy rights can be a concern when using data and technology to fight financial crime; data privacy and protection and countering financial crime are important public interests that are not opposed to each other. (p. 11)[^original]  
  <sub>anchor: "Data privacy and protection, and countering financial crime are important public interests that are not opposed to each other."</sub>
- **expected / expectation**: Data privacy and protection and countering financial crime should be supported by the right technological tools and by a balanced legal framework. (p. 11)[^original]  
  <sub>anchor: "They should be supported by the right technological tools and by a balanced legal framework."</sub>
- **descriptive / definition**: A footnote explains that privacy-enhancing technologies, also called cryptography or encryption technologies, include homomorphic encryption, secure multi-party computation, differential privacy and zero-knowledge proofs, and that they can enable secure, privacy-protected information-sharing and analysis. (p. 11)[^original]  
  <sub>anchor: "such as homomorphic encryption, secure multi-party computation, differential privacy and zero-knowledge proofs"</sub>
- **permissive / context**: Technology and collaboration could help financial institutions, central banks, supervisors and other public authorities tackle AML challenges through collaborative analytics and learning (CAL); such initiatives could use payment-system-level data and public-private collaborative approaches to analyse privacy-protected data, in order to reveal suspicious networks and activities that may not be detected by financial institutions acting in isolation. (p. 11)[^original]  
  <sub>anchor: "to reveal suspicious networks and activities that may not be detected by financial institutions acting in isolation."</sub>

## 2.3 Project Aurora

- **descriptive / method**: Project Aurora is a proof of concept (PoC) investigating privacy-enhancing technologies and advanced analytics for different CAL approaches to detecting money laundering. (p. 12)[^original]  
  <sub>anchor: "The PoC investigates the use of privacy-enhancing technologies and advanced analytics for different CAL approaches"</sub>
- **descriptive / method**: PoC part 1 generates a synthetic data set of transactions between financial institutions, individuals and businesses within a country and across borders, with complex money laundering events embedded, using a minimum set of data fields common to different payment ecosystems such as IPS and potential CBDC systems plus fields required in any CAL arrangement. (p. 12)[^original]  
  <sub>anchor: "The data set consists of a minimum set of data fields, which are common to different payment ecosystems"</sub>
- **descriptive / method**: PoC part 2 tests three simulated monitoring scenarios (single financial institution, national and cross-border views of the synthetic data) using machine learning models and network analysis, comparing their performance in detecting money launderers and suspicious networks. (p. 12)[^original]  
  <sub>anchor: "Testing three different simulated monitoring scenarios (views the synthetic data at the single financial institution level"</sub>
- **descriptive / method**: PoC part 3 tests and compares different CAL approaches (centralised, decentralised or hybrid at national and cross-border levels) with privacy-enhancing technologies applied to the data and analysed with advanced analytics, to examine how PETs could support privacy and data protection. (p. 12)[^original]  
  <sub>anchor: "Testing and comparing the performance of different CAL approaches"</sub>
- **descriptive / definition**: In the report, performance has two parts, effectiveness and efficiency, referring to the fraction of money laundering activities detected in the data while keeping false positives low; machine learning refers to artificial intelligence and machine learning. (p. 12)[^original]  
  <sub>anchor: "Performance is made up of two parts: effectiveness and efficiency."</sub>

## 2.4 Key findings and takeaways

- **descriptive / finding or result**: Project Aurora demonstrates the advantages and potential of combining payments data with privacy-enhancing technologies, machine learning models and network analysis to detect complex money laundering schemes. (p. 12)[^original]  
  <sub>anchor: "Project Aurora demonstrates the advantages and potential of using payments data in combination with privacy-enhancing technologies"</sub>
- **descriptive / finding or result**: The project demonstrates that CAL approaches are more effective in detecting money laundering networks than the current siloed approach in which institutions analyse in isolation. (p. 12)[^original]  
  <sub>anchor: "approaches are more effective in detecting money laundering networks than the current siloed approach"</sub>
- **descriptive / finding or result**: A holistic view of payments data is essential to identify and combat suspicious activities beyond single institutions and national borders, and could improve monitoring by revealing money laundering networks in transaction networks. (p. 12)[^original]  
  <sub>anchor: "A holistic view of payments data is essential to effectively identify and combat suspicious activities"</sub>
- **permissive / finding or result**: At national level the explored analysis could be run via transaction monitoring utilities or CAL arrangements connecting payments data ecosystems (financial institutions, fintech, VASPs, card schemes, e-money or others); at cross-border level similar analysis could take place in a CAL arrangement. (p. 12)[^original]  
  <sub>anchor: "could be performed via transaction monitoring utilities or CAL arrangements in which different ecosystems of payments data"</sub>
- **permissive / finding or result**: Operators of IPS or potential CBDC systems with AML monitoring capabilities (central banks or private sector entities) could use these approaches to provide participants with additional tools and support to enhance monitoring efficiency. (p. 12)[^original]  
  <sub>anchor: "Operators of these systems could provide participants with additional tools and support to enhance their monitoring efficiency.22"</sub>
- **descriptive / limitation**: There could be limitations on the types of money laundering activities and actors that can be detected depending on design choices and data available. (p. 13)[^original]  
  <sub>anchor: "There could be limitations on the types of money laundering activities and actors that could be detected"</sub>
- **descriptive / finding or result**: Using network analysis to detect anomalous and suspicious networks shifts focus from individual behaviour to the overall behaviour of suspicious networks, resulting in improved detection capabilities. (p. 13)[^original]  
  <sub>anchor: "shifts the focus from individual behaviour to the overall behaviour of suspicious networks"</sub>
- **descriptive / finding or result**: Project Aurora demonstrates potential to improve money laundering detection while reducing the number of incorrect alerts. (p. 13)[^original]  
  <sub>anchor: "Project Aurora demonstrates the potential to improve the detection of money laundering while reducing the number of incorrect alerts."</sub>
- **descriptive / finding or result**: Optimal machine learning performance was observed in a simulated cross-border scenario where sensitive transaction data are protected (using encryption or a combination of privacy-preserving methods), consolidated into a centralised system and analysed with network analysis. (p. 13)[^original]  
  <sub>anchor: "optimal performance of machine learning models is observed in a simulated cross-border scenario"</sub>
- **descriptive / limitation**: Although Project Aurora simulated a centralised cross-border CAL approach, in reality data protection, data localisation, legal and regulatory challenges would be complex; a decentralised CAL approach using federated learning at cross-border level may offer an alternative but could trade off effectiveness in detecting money laundering. (p. 13)[^original]  
  <sub>anchor: "in reality the challenges associated with data protection, data localisation, legal, regulatory and other factors would be complex"</sub>
- **permissive / finding or result**: A centralised approach consolidating privacy-enhanced transaction data nationally, combined with countries collectively training a model via federated learning applied locally, could support cross-border AML collaboration while upholding the data sovereignty of individual countries. (p. 13)[^original]  
  <sub>anchor: "while upholding the data sovereignty of individual countries.24"</sub>

## 2.4.3 Leveraging Project Aurora

- **descriptive / finding or result**: Project Aurora indicates that how well this kind of analysis performs depends on how broad the available data are; the report adds that data quality and standardised data identifiers and fields are important factors. (p. 13)[^original]  
  <sub>anchor: "Project Aurora shows that the performance of such analysis is only as good as the breadth of data available."</sub>
- **permissive / context**: The adoption of ISO 20022 could be an opportune moment to promote greater international consistency in data identifiers and fields, and in their shared, machine-readable definitions, which could be used for financial crime detection and to enable CAL arrangements. (p. 13)[^original]  
  <sub>anchor: "The adoption of ISO 20022 could be an opportune moment to catalyse greater international consistency"</sub>
- **permissive / context**: As an example, the legal entity identifier (LEI) could be included in ISO 20022 payment messages; when combined with the additional data fields available in those messages, the LEI could help identify a greater range of money laundering activities involving legal entities. (p. 13)[^original]  
  <sub>anchor: "When combined with the additional data fields available in these messages, the LEI could help identify a greater range"</sub>
- **expected / expectation**: Data protection agencies should be brought in early so that they take part in co-design with other stakeholders in CAL arrangements, helping to identify and mitigate risks and resolve uncertainties, for example by considering the role and application of PETs. (p. 13)[^original]  
  <sub>anchor: "Data protection agencies should be engaged at an early stage to be part of co-design processes"</sub>
- **expected / expectation**: To leverage Project Aurora, three aspects should be kept in mind. (p. 14)[^original]  
  <sub>anchor: "To leverage Project Aurora, three aspects should be kept in mind:"</sub>
- **expected / expectation**: First, the data fields and sources needed to detect financial crime may vary with criminals' techniques, and it is essential to understand different types of financial crime and identify the data fields and sources that may indicate their occurrence. (p. 14)[^original]  
  <sub>anchor: "It is essential to have a thorough understanding of different types of financial crimes"</sub>
- **expected / expectation**: Standards being developed for identification of beneficial owners would also be important. (p. 14)[^original]  
  <sub>anchor: "standards being developed for identification of beneficial owners, would be important too."</sub>
- **descriptive / context**: The LEI is the global standard for legal entity identification; it could link data associated with legal entities to transaction data within and across borders, connect more data sets, capture different relationships, and address monitoring problems from inconsistent entity identification. (p. 14)[^original]  
  <sub>anchor: "The legal entity identifier (LEI) is the global standard for legal entity identification."</sub>
- **expected / expectation**: Second, further discussion on the public benefits of CAL arrangements for AML, followed by legislative clarity to support such arrangements, would be necessary. (p. 14)[^original]  
  <sub>anchor: "further discussion on the public benefits of CAL arrangements for AML followed by legislative clarity"</sub>
- **expected / expectation**: Third, effective CAL arrangements, as a public-interest tool within a broader strategic framework for financial crime prevention and disruption, would require public-private collaboration, and any approach would need to consider prioritisation of risks and responses, the data required, trust between participants and the legal certainty needed. (p. 14)[^original]  
  <sub>anchor: "would require collaboration between the public and private sectors to contribute to and deliver such a strategic approach"</sub>
- **permissive / context**: National strategies for AML monitoring and analysis could also include appropriate cross-border CAL initiatives to gain a broader view of money laundering networks and the flow of funds. (p. 14)[^original]  
  <sub>anchor: "National strategies for AML monitoring and analysis could also include the appropriate cross-border CAL initiatives"</sub>
- **descriptive / context**: The White House (2021) US and UK prize challenge is cited as advancing privacy-enhancing technologies as an opportunity to leverage data while protecting privacy and intellectual property and enabling cross-border and cross-sector collaboration. (p. 14)[^original]  
  <sub>anchor: "the US and UK prize challenge to advance privacy-enhancing technologies"</sub>

## 3.1 What is money laundering?

- **descriptive / definition**: Money laundering is the act of hiding the origin of illegal assets, often through a series of transactions that may appear legitimate, during which the nominal owner and form of assets can change to hide any connection with the original assets. (p. 16)[^original]  
  <sub>anchor: "Money laundering is the act of hiding the origin of illegal assets"</sub>
- **descriptive / context**: Money laundering fuels corruption, organised crime, terrorism, modern slavery and environmental crime; these activities may discourage foreign investment, distort international capital flows, cause welfare losses and undermine the integrity and stability of the financial system and wider economy. (p. 16)[^original]  
  <sub>anchor: "Money laundering fuels corruption, organised crime, terrorism, modern slavery and environmental crime."</sub>
- **descriptive / context**: Money launderers exploit the complexity of the global financial system, information asymmetries from gaps in regulatory data visibility and information sharing, and differences in national laws; according to the FATF all large-scale money laundering schemes invariably contain cross-border elements. (p. 16)[^original]  
  <sub>anchor: "all large-scale money laundering schemes invariably contain cross-border elements."</sub>
- **descriptive / limitation**: Financial institutions are the first line of defence, but most rely on siloed data and isolated systems for suspicious transaction monitoring, limiting their ability to detect complex cross-border and cross-institutional money laundering networks. (p. 16)[^original]  
  <sub>anchor: "most FIs rely on siloed data and isolated systems for their suspicious transaction monitoring"</sub>
- **descriptive / context**: Combatting financial crime is only as strong as the weakest link and is a continuous process requiring human and technological processes to adapt to evolving risks; new laundering techniques constantly emerge as criminals obfuscate source, destination and flow of funds. (p. 16)[^original]  
  <sub>anchor: "Combatting financial crime is only as strong as the weakest link and is a continuous process"</sub>
- **descriptive / context**: The report states that the consequences of money laundering are far-reaching and that, in today's interconnected world, its impact is not limited to individual financial institutions (FIs) or individual countries. (p. 16)[^original]  
  <sub>anchor: "the impact of these activities is not confined to individual financial institutions (FIs) or individual countries"</sub>
- **descriptive / context**: Citing the FATF that all large-scale money laundering schemes invariably contain cross-border elements, the report concludes that money laundering is a challenge requiring coordinated global efforts, which are essential to protect the integrity and stability of the financial system. (p. 16)[^original]  
  <sub>anchor: "money laundering is a challenge that requires coordinated global efforts"</sub>

## 3.2 The money laundering process

- **descriptive / typology or red flag**: Money laundering typically involves three simplified stages (placement, layering, integration), though the process is not as linear as the diagram shows. (p. 17)[^original]  
  <sub>anchor: "Money laundering typically involves the following simplified three stages"</sub>
- **descriptive / typology or red flag**: Stage 1, placement: the launderer introduces illicit funds into the financial system, for example by transferring funds to accounts or wallets they control, with the method depending on the source and type of funds such as cash, bank deposits or cryptoassets. (p. 17)[^original]  
  <sub>anchor: "In the placement stage a money launderer introduces illicit funds into the financial system."</sub>
- **descriptive / typology or red flag**: Stage 2, layering: the launderer moves funds from placement through different layers, involving transfers between financial institutions or conversion to different assets, to obfuscate the source; large-scale schemes use complex layering structures. (p. 17)[^original]  
  <sub>anchor: "moves the funds from the placement stage through different layers"</sub>
- **descriptive / typology or red flag**: Money mule networks use individuals who, intentionally or unintentionally, receive and transfer illegal profits for someone else, adding layers between the source and criminals; professional networks often include multiple accounts across institutions and jurisdictions, making funds hard to trace. (p. 17)[^original]  
  <sub>anchor: "Professional money mule networks often include multiple accounts across different financial institutions and jurisdictions"</sub>
- **descriptive / typology or red flag**: Smurfing breaks larger transactions into smaller ones to avoid detection, which can use multiple bank accounts, credit cards and shell companies, sometimes across different countries. (p. 17)[^original]  
  <sub>anchor: "Smurfing is the act of breaking up larger transactions into smaller ones to avoid detection."</sub>
- **descriptive / typology or red flag**: Stage 3, integration: laundered funds are reintegrated into the economy by being transferred to accounts controlled by the criminal or invested in assets such as real estate, valuable or luxury items, or business ventures. (p. 17)[^original]  
  <sub>anchor: "the laundered funds are reintegrated into the economy by being transfered to accounts controlled by the criminal"</sub>

---

[source overview](overview.md) | [next part](digest-002.md)

[^original]: Bank for International Settlements / Basel Committee, "Project Aurora: the power of data, technology and collaboration to combat money laundering across institutions and borders" (2023-05-31). https://www.bis.org/publications/project-aurora-power-data-technology-and-collaboration-combat-money-laundering-across-institutions-and-borders
