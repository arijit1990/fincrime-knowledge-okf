---
type: Source Digest
title: Suptech applications for anti-money laundering - part 2 of 2 (pp. 13-22)
description: 'Verified paraphrased digest, pp. 13-22: Financial Stability Institute > Suptech applications for anti-money laundering1'
resource: https://www.bis.org/publications/fsi-insight-18-suptech-applications-anti-money-laundering
tags:
- effectiveness
- international_standard
- intl
- other
- regulation
status: stable
source_id: bis-bcbs-suptech-applications-for-anti-money-laundering
issuer: bis_bcbs
issuer_name: Bank for International Settlements / Basel Committee
jurisdictions:
- INTL
tier: 2
instrument_type: other
normative_force: international_standard
publication_date: '2019-08-29'
legal_status: current
part: 2
parts_total: 2
content_mode: digest
generated:
  by: claude-code-subagent/claude-sonnet-5-5
  at: '2026-11-21T13:42:23Z'
verified:
- by: process:kb-digest-check/anchor-match
  at: '2026-11-21T13:42:23Z'
- by: claude-code-judge-agent/claude-opus-5-5
  at: '2026-11-21T13:42:23Z'
sources:
- id: original
  resource: https://www.bis.org/publications/fsi-insight-18-suptech-applications-anti-money-laundering
  title: Suptech applications for anti-money laundering
  author: org:bis_bcbs
  last_modified: '2019-08-29T00:00:00Z'
digest_points: 55
---

# Suptech applications for anti-money laundering (digest)

[previous part](digest-001.md) | [source overview](overview.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (pp. 13-22) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **international standard**.

## Evaluation of financial institutions’ compliance with AML/CFT requirements

- **descriptive / context**: Paragraph 27 says innovative technologies increase authorities' capacity to process substantial amounts of unstructured data. (p. 13)[^original]  
  <sub>anchor: "Innovative technologies increase the authorities’ capacity to process substantial amounts of unstructured data."</sub>
- **descriptive / case example**: DNB has a tool in development to analyse systemic integrity risk analysis (SIRA) reports, which are banks' self-assessments of their integrity risks; supervisors pose standardised questions and the tool searches across many reports for pieces of information (for example number of high-risk customers) to answer them. (p. 13)[^original]  
  <sub>anchor: "systemic integrity risk analysis (SIRA) reports, which are self-assessments that banks submit about their integrity risks"</sub>
- **descriptive / method**: The DNB SIRA tool aims to assess whether the bank has sufficient understanding of the risks it is exposed to and whether internal controls are adequate, and will use a combination of text mining and supervised machine learning to extract the responses. (p. 13)[^original]  
  <sub>anchor: "The tool will use a combination of text mining and supervised machine learning to extract the responses."</sub>

## Box 2 – CNBV application of machine learning to transactional data

- **descriptive / method**: Box 2: CNBV is testing, with R2A, a machine learning solution to detect unusual transactions not reported by financial institutions; 'manually found' as well as reported unusual transactions train the machine, which then scans the whole data set for other transactions with similar patterns. (p. 13)[^original]  
  <sub>anchor: "In this context, “manually found” as well as reported unusual transactions are used to train the machine"</sub>
- **descriptive / context**: Box 2 states one underlying goal of the CNBV tool is to assess institutions' risk profile based on the number of unreported unusual transactions: institutions with many unreported unusual transactions are deemed more risky and would be subject to more intensive supervision. (p. 13)[^original]  
  <sub>anchor: "financial institutions with a large number of unreported unusual transactions are deemed more risky"</sub>
- **descriptive / data or feature**: Box 2 says the CNBV prototype mainly relies on two data sources: a transactional database of all transactions made by an institution's clients in a given period (including those marked risky and reported to the FIU) and a customer database with personal information including know-your-customer questionnaire data and the client risk rating; it is cloud-based as a cost-effective storage solution for growing volumes of surveillance data. (p. 13)[^original]  
  <sub>anchor: "a transactional database consisting of all transactions made by the clients of a financial institution in a given period"</sub>

## Section 3 – Data analytics tools

- **descriptive / case example**: Paragraph 26 says networks can also be built from unstructured data. MAS applies network analysis to STRs, currently using the structured STR fields, and is exploring extending its solution with information extracted from the unstructured STR text, by applying NLP to extract information such as the relationships of parties mentioned in a single STR. (p. 13)[^original]  
  <sub>anchor: "MAS applies network analysis to STRs."</sub>
- **descriptive / case example**: Paragraph 26 reports that CNBV is developing a prototype that reviews news about selected people and companies involved in money laundering, then searches for those entities in several other data sources (eg social media, transactional data) to build networks of people or companies that may be engaging in money laundering. (p. 13)[^original]  
  <sub>anchor: "CNBV is developing a prototype application that looks at news referring to selected people and companies"</sub>

## Detection of networks of entities involved in suspicious activities

- **descriptive / case example**: Paragraph 28 says several FIUs use network analysis to uncover criminal activity, mainly relying on the STR database but also other sources, combining information from various reporting entities over different periods to uncover hidden relations; UIF has a tool that builds networks using STRs. (p. 14)[^original]  
  <sub>anchor: "FIUs can combine information provided by various reporting entities in different periods of time"</sub>
- **descriptive / case example**: Paragraph 28 adds that UIF is exploring network analysis combined with self-organising map techniques on its gold declaration database (Box 3); ROSFIN is developing a tool using STRs and other information (public contracts, customs declarations, data on directors/founders of companies) to build networks; FINTRAC uses STRs, wire transfers and large cash transactions to construct potential criminal networks in Canada; AUSTRAC applies network analysis to its remittances database to detect suspicious cross-border activities. (p. 14)[^original]  
  <sub>anchor: "AUSTRAC, on the other hand, has been applying network analysis on its remittances database"</sub>

## Box 3 – UIF application of network analysis and self-organising maps to the gold database

- **descriptive / method**: Box 3: in Italy UIF is testing a tool combining network analysis and self-organising maps to search the gold declaration database for fraudulent schemes. Step one builds the network of all gold market participants; step two determines participants' behaviours, defined by a vector of descriptive and centrality network metrics. (p. 14)[^original]  
  <sub>anchor: "The first one is to build the network of all participants in the gold market using network analysis."</sub>
- **descriptive / method**: Box 3 continues: step three reduces the dimensions of these characteristics with principal component analysis; a self-organising map is trained on this data set to identify gold market operators' typical behaviour; finally, using data on behaviours of fraudulent schemes, the trained map is applied to find participants with similar characteristics. (p. 14)[^original]  
  <sub>anchor: "a self-organising map is trained in order to identify gold market operators’ typical behaviour"</sub>

## Assessment of the likelihood of money laundering activity

- **descriptive / case example**: Paragraph 29 says innovative tools may be used to assess the likelihood of money laundering in individual transactions: in Finland RAP's tool scores each STR on criteria such as the number of times the party was reported in the last six months and whether the party has a criminal background or is subject to an ongoing FIU investigation. (p. 14)[^original]  
  <sub>anchor: "assigns a score to each STR based on several criteria such as the number of times"</sub>
- **descriptive / case example**: ROSFIN has a machine learning tool that detects potentially fictitious companies based on a sample of known shell companies; UIF uses big data to monitor wire transfers to and from selected countries, combining structured and, to a lesser extent, unstructured data (for example press articles) to calculate indicators measuring the degree of anomaly of each flow. (p. 14)[^original]  
  <sub>anchor: "uses machine learning to detect potentially fictitious companies based on a sample of known shell companies"</sub>

## Identification of patterns and trends in criminal activities

- **descriptive / context**: Paragraph 30 says FIUs use advanced analytics to identify new ML trends and patterns because methods evolve and authorities need to react quickly; early identification of new typologies lets FIUs disseminate it to market participants and other authorities and supports their own investigations. (p. 15)[^original]  
  <sub>anchor: "The early identification of new typologies allows FIUs to disseminate this information to market participants and other authorities"</sub>
- **descriptive / case example**: Paragraph 31 says automatic classification tools help authorities identify new trends or assess how ML/TF typologies evolve over time and by geographical area; UIF is developing a tool that extracts information from the unstructured part of STRs using NLP and then applies a supervised machine learning technique to classify STRs by money laundering scheme type. (p. 15)[^original]  
  <sub>anchor: "UIF, for example, is currently developing a tool to classify STRs according to the type of money laundering scheme perpetrated."</sub>

## Box 4 – FINTRAC application of text mining to STRs

- **descriptive / method**: Box 4: FINTRAC is developing a text mining tool that analyses narrative portions of STRs and discovers key concepts such as types of offences, criminal groups, jurisdictions of interest, and types of products and services exploited; all STRs will be tagged on this basis to give a multidimensional view of trends. (p. 15)[^original]  
  <sub>anchor: "discovers key concepts related to ML/TF, such as types of offences, criminal groups, jurisdictions of interest"</sub>
- **descriptive / context**: Box 4 says the tagging will provide actionable insights for FINTRAC's strategic intelligence group and help it develop strategic intelligence products such as operational alerts more efficiently and disseminate them to reporting entities to raise awareness of new typologies and trends. (p. 15)[^original]  
  <sub>anchor: "provide actionable insights for its strategic intelligence group"</sub>

## How do AML/CFT authorities develop these tools?

- **descriptive / context**: Paragraph 32 says authorities explore or develop advanced analytics in different ways: some build in-house capabilities, some use ready market solutions, and some actively collaborate with the academic community and promote research. (p. 15)[^original]  
  <sub>anchor: "AML/CFT authorities explore or develop advanced data analytics tools in different ways."</sub>
- **descriptive / case example**: Paragraph 33 says authorities within a central bank, or prudential or conduct authority, generally benefit from the institutional innovation strategy: UIF uses the Bank of Italy's multidisciplinary big data team and infrastructure; DNB has a Supervision Innovation Office coordinating its digital strategy and an informal Data Science Hub; MAS's Supervisory Technology Office supports AML/CFT supervisors' analytics needs by partnering with supervision departments. (p. 15)[^original]  
  <sub>anchor: "DNB, meanwhile, has established a Supervision Innovation Office that coordinates the implementation of the digital strategy"</sub>
- **descriptive / case example**: Paragraph 34 says the mandate of FIUs also leads them to explore advanced analytics and the international community recognised their need for tools; UNODC developed goAML, an integrated database and intelligent analysis system with three primary solutions for collection, analysis and data exchange, deployed by 49 FIUs around the world. (p. 16)[^original]  
  <sub>anchor: "There are now 49 FIUs around the world that have"</sub>
- **descriptive / case example**: Paragraph 34 adds that FIC is considering supplementing goAML with an AI algorithm, FINTRAC has a Data Exploitation Laboratory, and AUSTRAC has analytics, innovation, development, information and infrastructure teams aiming to ensure advanced analytics are in place to enable it to innovate. (p. 16)[^original]  
  <sub>anchor: "FINTRAC has a Data Exploitation Laboratory, which explores and implements data analytics solutions."</sub>
- **descriptive / case example**: Paragraph 35 says for some authorities ready market solutions may be more efficient: ROSFIN bought ready solutions from three external vendors (one offline, fully functional version used without the first vendor's support; one baseline solution from the second vendor integrated by the third vendor, which is cleared to work with restricted data); UIF relies on an external vendor and open source tools for dashboards and visualisation that analyse large data in seconds and combine sources; CNBV relies on an external vendor for several solutions. (p. 16)[^original]  
  <sub>anchor: "ROSFIN, which bought ready solutions involving three external vendors."</sub>
- **descriptive / case example**: Paragraph 36 describes academic collaboration: AUSTRAC has two university projects (AML alert indicators with the Australian National University; smart-contract-based reporting with Swinburne University); ROSFIN collaborates with the Lebedev Physical Institute on network analysis to find hidden relationships and AI techniques including pattern recognition and subgraph detection within a multigraph; UIF organises an annual workshop with Bocconi University, banks' compliance officers, law enforcement and judicial authorities on quantitative methods to counter economic crime. (p. 16)[^original]  
  <sub>anchor: "UIF organises an annual workshop in collaboration with Bocconi University"</sub>

## Computational capacity

- **descriptive / limitation**: Paragraph 37 says computational capacity may be an issue because the tools deal with large volumes of data; UIF relies on the Bank of Italy IT department's infrastructure using Apache Spark, an open source layer that bundles the computational power of a group of heterogeneous computers into one platform, while a few authorities looking at public cloud are prevented by data residency requirements and data security concerns. (p. 17)[^original]  
  <sub>anchor: "data residency requirements as well as data security concerns prevent them from doing so"</sub>

## Data privacy and confidentiality

- **descriptive / limitation**: Paragraph 39 says privacy and confidentiality concerns also constrain use of external resources: specialised skills are needed and sometimes unavailable internally, and resorting to external parties could mean giving them access to confidential information. (p. 17)[^original]  
  <sub>anchor: "Specialised skills are required to develop these tools, and sometimes these are not available internally."</sub>
- **descriptive / case example**: Paragraph 39 reports that an external party hired by one covered authority had to go through lengthy clearance and control processes, which added to the rigid procurement process and caused a significant delay in the project. (p. 17)[^original]  
  <sub>anchor: "has to go through lengthy clearance and control processes"</sub>
- **permissive / recommendation**: Paragraph 39 says technologies that require permission from data owners when external developers need to access confidential data may contribute to dealing with the issue, and creating a testing environment using only testing data is another common process used to address it. (p. 17)[^original]  
  <sub>anchor: "The creation of a testing environment using only testing data is also another common process"</sub>
- **mandatory / limitation**: Paragraph 38 says data privacy and confidentiality requirements provide safeguards that authorities must consider, including regarding which information they can use; for example, the General Data Protection Regulation in Europe could limit the use of some detailed personal information for AML/CFT authorities' profiling activities. (p. 17)[^original]  
  <sub>anchor: "the General Data Protection Regulation in Europe could limit the use of some detailed personal information"</sub>

## Efficiency vs effectiveness

- **descriptive / definition**: Paragraph 40 says assessing efficiency of the tools is more straightforward and more easily quantified than effectiveness; efficiency refers to the amount of resources needed to fulfil a task, while effectiveness refers to the degree to which the desired outcome is achieved. (p. 18)[^original]  
  <sub>anchor: "Efficiency refers to the amount of resources needed to fulfil a certain task, while effectiveness refers to the degree"</sub>
- **descriptive / finding or result**: Paragraph 40 gives efficiency results: ROSFIN's new database management system, allowing strategic analyses of detailed data and detection of large-scale schemes, makes some processes run 43 times faster, and UIF's tool for analysing wire transfers produced an 80% reduction in the time required for analyses. (p. 18)[^original]  
  <sub>anchor: "results in some processes running 43 times faster"</sub>
- **descriptive / method**: Paragraph 41 says assessing effectiveness of some supervisor tools may be feasible, especially risk scoring tools, by comparing tool output with on-site inspection outcomes or other technology; FINTRAC compares its risk model output with inspection outcomes and is developing a machine learning and heuristic challenger model to compare against the production model. (p. 18)[^original]  
  <sub>anchor: "the output of its risk model is compared against the outcome of inspections"</sub>
- **descriptive / limitation**: Paragraph 42 says assessing effectiveness of FIU tools is more challenging because proving money laundering takes time: the FIU passes suspicious activity to law enforcement, which refers cases to courts if prosecution is warranted, and court proceedings can be protracted so it could take years to determine whether the tool correctly identified ML. (p. 18)[^original]  
  <sub>anchor: "it could take years to determine whether the tool has correctly identified ML"</sub>
- **descriptive / limitation**: Paragraph 43 says effectiveness is also generally measured by reduction in false positives, which in theory could lead to more false negatives; false negatives are more damaging in the fight against ML/TF, and this could be mitigated by focusing on the bigger picture through network analysis rather than analysis of individual transactions or entities. (p. 18)[^original]  
  <sub>anchor: "False negatives, however, are more damaging in the fight against ML/TF."</sub>
- **descriptive / limitation**: Paragraph 44 says tools based on supervised machine learning could lose effectiveness over time if not regularly updated with a new data set, because criminal organisations could change behaviour to avoid detection, rendering tools ineffective unless constantly updated with new training data; unsupervised machine learning solutions could also be considered. (p. 18)[^original]  
  <sub>anchor: "Unsupervised machine learning solutions could also be considered to address this problem."</sub>

## Section 4 – Conclusions

- **expected / finding or result**: Paragraph 45 says it is important for AML/CFT authorities to understand the potential of innovative technology for their analytics work; more data are readily available but are not useful unless the relevant information is unlocked, and advanced tools that sift large volumes from different sources can help in identifying, assessing and understanding ML/TF risks. (p. 19)[^original]  
  <sub>anchor: "It is important for AML/CFT authorities to understand the potential of innovative technology"</sub>
- **descriptive / finding or result**: Paragraph 46 says tool development can be organised in different ways (dedicated units, buying ready solutions, external consultants building bespoke solutions, academic partnerships) and no single approach works best for all; factors to consider include the authority's profile (size and resources), the characteristics of the financial system (number of supervised entities, ML/TF risk) and the legal framework (for example data privacy laws influencing usable data and reliance on external parties). (p. 19)[^original]  
  <sub>anchor: "There is no single approach that works best for all authorities."</sub>
- **descriptive / finding or result**: Paragraph 47 says similar technologies underlie the tools so there is scope to learn from counterparts; authorities analyse either individual transactions (to find those needing further scrutiny) or networks of transactions (to find interconnections and entities that may represent a coordinated ML/TF risk), and regular exchange of information offers opportunities for peer learning. (p. 19)[^original]  
  <sub>anchor: "AML/CFT authorities analyse either individual or networks of transactions"</sub>
- **descriptive / limitation**: Paragraph 48 says efficiency gains seem to be the number one benefit but there is a paradox: capacity-constrained authorities typically lack the specialised resources to develop, understand and use the tools, so they need to build capacity first before reaping resource-saving benefits; exploring available market solutions could be a starting point while they develop specialised capacity. (p. 19)[^original]  
  <sub>anchor: "The paradox, however, is that capacity-constrained authorities typically do not have the specialised resources"</sub>
- **descriptive / finding or result**: Paragraph 49 says the tools' benefits are particularly important for jurisdictions struggling to improve AML/CFT capabilities and heavily affected by unintended consequences of international standards; domestic capacity building forms part of the FSB-coordinated action plan to address the decline in correspondent banking, and international organisations provide technical assistance, mostly on fundamentals such as basic supervision and sanctions regimes. (p. 19)[^original]  
  <sub>anchor: "domestic capacity building forms part of the FSB-coordinated action plan to assess and address the decline in correspondent banking"</sub>
- **permissive / recommendation**: Paragraph 49 says that, where appropriate, laying the groundwork for authorities to explore advanced analytics tools (for example developing necessary skills) could be part of technical assistance to such jurisdictions. (p. 19)[^original]  
  <sub>anchor: "laying the ground work for authorities to be able to explore"</sub>
- **descriptive / finding or result**: Paragraph 48: efficiency gains seem to be the number one benefit of advanced data analytics tools, which could help capacity-constrained AML/CFT authorities; authorities have highlighted time savings from using them. (p. 19)[^original]  
  <sub>anchor: "Efficiency gains seem to be the number one benefit of advanced data analytics tools"</sub>
- **permissive / finding or result**: Paragraph 48: the time savings could translate into a reallocation of resources or capacity from more manual work to more judgment-based work. (p. 19)[^original]  
  <sub>anchor: "This could translate into a reallocation of resources or capacity from more manual work to more judgment-based work."</sub>
- **descriptive / finding or result**: Paragraph 48 notes a paradox: capacity-constrained authorities typically lack the specialised resources needed to develop, understand and use these tools, so they need to build capacity first before reaping the resource-saving benefits; exploring available market solutions could be a starting point while they develop specialised capacity. (p. 19)[^original]  
  <sub>anchor: "capacity-constrained authorities typically do not have the specialised resources needed to develop, understand and use these tools"</sub>
- **descriptive / finding or result**: Paragraph 49 says the benefits of these tools are particularly important for jurisdictions that have struggled to improve their AML/CFT capabilities and have therefore been heavily impacted by the unintended consequences of international standards; as mentioned, the jurisdictions most frequently exited by global correspondent banks seem to be those with weak AML/CFT supervisory and regulatory frameworks. (p. 19)[^original]  
  <sub>anchor: "the jurisdictions most frequently exited by global correspondent banks seem to be those with weak AML/CFT supervisory and regulatory frameworks"</sub>
- **descriptive / context**: Paragraph 49 adds that domestic capacity building forms part of the FSB-coordinated action plan to assess and address the decline in correspondent banking, and that international organisations have been providing extensive technical assistance to these jurisdictions to enhance their supervisory and regulatory frameworks. (p. 19)[^original]  
  <sub>anchor: "domestic capacity building forms part of the FSB-coordinated action plan to assess and address the decline in correspondent banking"</sub>
- **descriptive / finding or result**: Paragraph 50 says authorities starting to develop their data infrastructure have a 'late mover' advantage (no legacy systems, seamless collection, validation and management, easier integration of new tools), whereas authorities with mature infrastructure need new processes and tools compatible with existing infrastructure, which limits the new tools they can explore. (p. 20)[^original]  
  <sub>anchor: "new processes and tools need to be compatible with the existing infrastructure"</sub>
- **recommended / recommendation**: Paragraph 51 says development of analytics tools that are international in scope should be considered because ML/TF is an international issue and the tools discussed are all national in scope; the authors note existing efforts such as the Egmont Group initiative and encourage similar international initiatives. (p. 20)[^original]  
  <sub>anchor: "We encourage similar international initiatives towards that end."</sub>
- **descriptive / finding or result**: Paragraph 52 says human judgment continues to be the foundation of success of AML/CFT authorities and having sufficient staff with the right skills, expertise and qualifications is critical; given the challenges of assessing effectiveness, expert human judgment continues to be necessary to interpret and validate tool outcomes. (p. 20)[^original]  
  <sub>anchor: "expert human judgment continues to be necessary to interpret and validate the outcomes of such tools"</sub>
- **expected / recommendation**: Paragraph 52 concludes that suptech tools should be seen as a complement to the work of experienced staff at AML/CFT authorities and not a substitute. (p. 20)[^original]  
  <sub>anchor: "suptech tools should be seen as a complement to the work of experienced staff"</sub>

## Glossary

- **descriptive / definition**: Glossary definitions: artificial intelligence is the theory and development of computer systems able to perform tasks that traditionally required human intelligence; big data is a generic term for the massive volume of data generated by increasing use of digital tools and information systems. (p. 22)[^original]  
  <sub>anchor: "artificial intelligence: the theory and development of computer systems able to perform tasks that traditionally have required human intelligence."</sub>
- **descriptive / definition**: Glossary: cloud computing is an innovation allowing use of an online network ('cloud') of hosting processors to increase the scale and flexibility of computing capacity, which has made possible analysis of very large datasets (big data) and a number of specific fintech applications; machine learning is a method of designing a sequence of actions to solve a problem that optimise automatically through experience with limited or no human intervention. (p. 22)[^original]  
  <sub>anchor: "cloud computing: an innovation in computing that allows for the use of an online network"</sub>
- **descriptive / definition**: Glossary: natural language processing is an interdisciplinary field of computer science, artificial intelligence and computational linguistics focused on programming computers and algorithms to parse, process and understand human language; network analysis is the process of investigating structures through the use of networks and graph theory. (p. 22)[^original]  
  <sub>anchor: "network analysis: the process of investigating structures through the use of networks and graph theory."</sub>
- **descriptive / definition**: Glossary: self-organising maps are a type of artificial neural network trained using unsupervised learning to produce a low-dimensional, discretised representation of the input space of the training samples (a map), and are therefore a method of dimensionality reduction; supervised learning is the machine learning task of learning a function that maps an input to an output based on example input-output pairs. (p. 22)[^original]  
  <sub>anchor: "self-organising maps: a type of artificial neural network that is trained using unsupervised learning"</sub>
- **descriptive / definition**: Glossary: smart contracts are programmable distributed applications that can trigger financial flows or changes of ownership if specific events occur; text mining is the process of exploring and analysing large amounts of unstructured text data aided by software that can identify concepts, patterns, topics, keywords and other attributes; unsupervised learning is a type of machine learning method that helps find previously unknown patterns in a data set without pre-existing labels. (p. 22)[^original]  
  <sub>anchor: "smart contracts: programmable distributed applications that can trigger financial flows or changes of ownership if specific events occur."</sub>

---

[previous part](digest-001.md) | [source overview](overview.md)

[^original]: Bank for International Settlements / Basel Committee, "Suptech applications for anti-money laundering" (2019-08-29). https://www.bis.org/publications/fsi-insight-18-suptech-applications-anti-money-laundering
