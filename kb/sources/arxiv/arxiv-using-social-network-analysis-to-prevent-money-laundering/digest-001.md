---
type: Source Digest
title: Using social network analysis to prevent money laundering - part 1 of 3 (pp. 1-14)
description: 'Verified paraphrased digest, pp. 1-14: Using Social Network Analysis to Prevent Money Laundering; Using Social Network Analysis to Prevent Money Laundering > Using Social Network Analysis to Prevent Money Laundering; Using Social Network Analysis to Prevent Money Laundering > Keywords; and 5 more sections'
resource: https://arxiv.org/abs/2105.05793
tags:
- academic_finding
- global_academic
- network_graph
- preprint
- typologies
status: stable
source_id: arxiv-using-social-network-analysis-to-prevent-money-laundering
issuer: arxiv
issuer_name: arXiv
jurisdictions:
- GLOBAL_ACADEMIC
tier: 3
instrument_type: preprint
normative_force: academic_finding
publication_date: '2016-09-20'
legal_status: unknown
part: 1
parts_total: 3
content_mode: digest
generated:
  by: claude-code-subagent/claude-sonnet-5-5
  at: '2026-11-22T14:46:06Z'
verified:
- by: process:kb-digest-check/anchor-match
  at: '2026-11-22T14:46:06Z'
- by: claude-code-judge-agent/claude-opus-5-5
  at: '2026-11-22T14:46:06Z'
sources:
- id: original
  resource: https://arxiv.org/abs/2105.05793
  title: Using social network analysis to prevent money laundering
  author: org:arxiv
  last_modified: '2016-09-20T00:00:00Z'
digest_points: 73
---

# Using social network analysis to prevent money laundering (digest)

[source overview](overview.md) | [next part](digest-002.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (pp. 1-14) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **academic finding**.

## Abstract

- **descriptive / data or feature**: The study analyses the central database of a factoring company mainly operating in Italy over a period of 19 months, including financial operations and information about company clients. (p. 2)[^original]  
  <sub>anchor: "We worked on real world data by analyzing the central database of a factoring company, mainly operating in Italy, over a period of 19 months"</sub>
- **descriptive / finding or result**: The authors find that client risk profiles can be predicted using social network metrics. (p. 2)[^original]  
  <sub>anchor: "We find that risk profiles can be predicted by using social network metrics."</sub>
- **descriptive / finding or result**: In the dataset, the most dangerous social actors handle bigger or more frequent financial operations, are more peripheral in the transactions network, mediate transactions across economic sectors, and operate in riskier countries or Italian regions. (p. 2)[^original]  
  <sub>anchor: "the most dangerous social actors deal with bigger or more frequent financial operations; they are more peripheral in the transactions network"</sub>
- **descriptive / method**: To spot potential criminal clusters, the authors propose a visual analysis of tacit links among companies sharing the same owner or representative. (p. 2)[^original]  
  <sub>anchor: "we propose a visual analysis of the tacit links existing among different companies who share the same owner or representative"</sub>

## Introduction

- **descriptive / context**: Money laundering is the process that turns proceeds of crime into clean legitimate assets; it is often linked to terrorism, drugs and arms trafficking and exploitation of human beings. (p. 2)[^original]  
  <sub>anchor: "Money laundering, known as the process that transforms the proceeds of crime into clean legitimate assets, is a common phenomenon"</sub>
- **descriptive / context**: Money laundering can weaken a country's economy by financing crime and corruption, making it less attractive to foreign private investors, and it raises operational risk and harms financial institution stability. (p. 2)[^original]  
  <sub>anchor: "makes a country less attractive for foreign private investors: money laundering increases the operational risk of financial transactions"</sub>

## 1. The problem of Money Laundering

- **descriptive / definition**: A factoring company buys accounts receivable from third parties at a discounted price, paying the seller with assets to meet its cash needs and taking full responsibility for collecting the debts. (p. 3)[^original]  
  <sub>anchor: "a company that buys accounts receivable from third parties at a discounted price, thus repaying the seller with assets"</sub>
- **descriptive / context**: The authors state that recording and monitoring factoring transactions is vital to identify clients with higher risk profiles, and that their model is intended to be replicable by any factoring company to profile clients and third parties and assign risk classes. (p. 3)[^original]  
  <sub>anchor: "we tried to develop a model which can be replicated by any factoring company to better profile its clients and the involved third parties"</sub>
- **descriptive / method**: The study differs from past work by using a relational approach and new ways to sort relationship data into several interaction networks. (p. 3)[^original]  
  <sub>anchor: "Our models differentiate from past studies since we use a relational approach"</sub>
- **descriptive / context**: Past research indicates that factoring may be linked to asset cloaking or to trade based money laundering, which can involve fictitious invoicing or price misinterpretation. (p. 3)[^original]  
  <sub>anchor: "Past research shows how this kind of business may be linked to asset cloaking"</sub>
- **descriptive / context**: The authors argue that illegal transactions require interaction between social actors, so analysis should include relationship networks via Social Network Analysis, not only individual attributes. (p. 4)[^original]  
  <sub>anchor: "by contrast, we suggest to focus not just on the individual attributes of these actors, but to include the study of their relationship networks"</sub>

## 1.1. European/Italian Guidelines and Recording of Financial Data

- **descriptive / context**: Directive 2005/60/EU, implemented in Italy in 2007, requires financial intermediaries to record every financial operation in a specific database accessible to the Bank of Italy's Financial Intelligence Unit when needed. (p. 4)[^original]  
  <sub>anchor: "financial intermediaries operating in Italy now have the duty to keep track of every financial operation"</sub>
- **mandatory / requirement**: The database required under the Italian implementation must meet minimum technical requirements on quality and type of information stored. (p. 4)[^original]  
  <sub>anchor: "the new database has to meet minimum technical requirements in terms of quality and type of information stored"</sub>
- **mandatory / requirement**: Credit and financial institutions can no longer keep anonymous accounts and must apply customer due diligence measures, including reporting suspicious activities such as transactions exceeding a certain amount, with exceptions and reinforcements depending on the case. (p. 4)[^original]  
  <sub>anchor: "credit and financial institutions can no longer keep anonymous accounts and need to apply customer due diligence measures"</sub>
- **descriptive / context**: For a factoring company, customer due diligence involves recording customer identity and, for firms, the owner data and the person responsible for the money transfer or financial operation. (p. 4)[^original]  
  <sub>anchor: "For a factoring company, customer due diligence implies gathering and recording the identity of customers and, when these are firms"</sub>
- **descriptive / context**: For a factoring company, the nature, amount and scope of transactions are also investigated and controlled over time. (p. 4)[^original]  
  <sub>anchor: "The nature, the amount and the scope of the transactions are also investigated and controlled over time"</sub>
- **descriptive / context**: Aggregated operation data is transmitted monthly to the FIU, which carries out a more systemic analysis at national level. (p. 4)[^original]  
  <sub>anchor: "Aggregated data about operations is transmitted monthly to the FIU"</sub>
- **mandatory / requirement**: The FIU must be informed every time an institution suspects money laundering or terrorist financing. (p. 4)[^original]  
  <sub>anchor: "the FIU must be informed every time an institution suspects money laundering or terrorist financing"</sub>
- **expected / expectation**: Identification of suspicious actors and transactions should be the outcome of a process that cannot rely only on individual judgements and should, at least partly, be automated. (p. 5)[^original]  
  <sub>anchor: "This identification should be the outcome of a process that cannot rely only on individual judgements, but should"</sub>
- **descriptive / context**: National guidelines suggest assessing financial actors by legal status, core activity, possibly suspicious behaviour and geographic area, and assessing operations by typology, amount, reason, frequency and consistency with previous activity and geography. (p. 5)[^original]  
  <sub>anchor: "National guidelines suggest taking into account a list of criteria referred to financial actors"</sub>

## 2. Detecting Money Laundering

- **descriptive / context**: Historically, most suspicious activity was identified by detecting anomalies in regular client transaction flows compared over time. (p. 5)[^original]  
  <sub>anchor: "most of the suspicious activities were identified by considering anomalies in the regular transactions flows of a client"</sub>
- **descriptive / context**: A computer-based approach seems reasonable where data is big and client knowledge is sometimes missing, such as banks with thousands of customers interacting online or sporadically. (p. 5)[^original]  
  <sub>anchor: "then a computer-based approach seems a reasonable solution to extract relevant information"</sub>
- **descriptive / context**: Rule-based classification is frequent; Rajput and colleagues (2014) presented an ontology-based expert system using the Semantic Web Rule Language to detect suspicious transactions. (p. 5)[^original]  
  <sub>anchor: "presented an ontology-based expert system to detect suspicious transactions, using the Semantic Web Rule Language"</sub>
- **descriptive / context**: Khanuja and Adane (2014) combined forensic database analysis with Dempster-Shafer theory of evidence to generate reports of suspicious actors automatically. (p. 5)[^original]  
  <sub>anchor: "Khanuja and Adane (2014) combined the analysis of forensic databases with the Dempster Shefer Theory of Evidence"</sub>
- **descriptive / context**: Tang and Yin (2005) developed a support vector machine classification system to handle large data volumes with more accurate predictions than traditional rules. (p. 5)[^original]  
  <sub>anchor: "developed a classification system based on support vector machine in order to handle large amounts of data"</sub>
- **descriptive / context**: Some studies used Bayesian approaches to assign risk scores to customer behaviour, and Panigrahi et al. combined Bayesian rules with past operation history, which the authors report as outperforming other fuzzy techniques. (p. 5)[^original]  
  <sub>anchor: "to combine Bayesian rules with database information about past operation history"</sub>
- **descriptive / context**: The Panigrahi et al. combination of Bayesian rules and operation history is reported as outperforming other fuzzy techniques. (p. 5)[^original]  
  <sub>anchor: "(Panigrahi, Kundu, Sural, & Majumdar, 2009), outperforming other fuzzy techniques"</sub>
- **descriptive / context**: Castellón González and Velásquez (2013) combined decision trees, neural networks, Bayesian networks and clustering to detect false invoicing of taxpayers. (p. 6)[^original]  
  <sub>anchor: "combined decision trees, neural networks, Bayesian networks and clustering algorithms to detect false invoicing of taxpayers"</sub>
- **descriptive / context**: Roith and Patel (2015) reviewed data mining and AML methods and argued that clustering techniques are the best solution. (p. 6)[^original]  
  <sub>anchor: "arguing that clustering techniques are the best solution"</sub>
- **descriptive / limitation**: Axelsson and Lopez-Rojas (2012) noted machine learning limitations, including data-dependent parameters, limited adaptability and scalability, misclassification risk, class imbalance and difficulty interpreting behavioural patterns, and proposed Multi-Agent Based Simulation as an integration or alternative. (p. 6)[^original]  
  <sub>anchor: "the class unbalance problem, or the difficulties in the interpretation of the underlying behavioral patterns"</sub>
- **descriptive / context**: Perez and Lavalle (2011) detected outliers by building user models on historical data and comparing new transactions against them, stressing individual patterns without a general rule. (p. 6)[^original]  
  <sub>anchor: "Perez and Lavalle (2011) based their methodology on the detection of outliers in transactions"</sub>
- **descriptive / limitation**: The authors see a main limitation in the historical data requirement of user-model approaches, which makes it harder to identify illicit operations by newcomers. (p. 7)[^original]  
  <sub>anchor: "we see a main limitation laying in the model requirement of historical data"</sub>
- **descriptive / context**: Ngai et al. (2011) produced one of the first systematic literature reviews, structuring work by fraud activity, data mining application class and technique. (p. 7)[^original]  
  <sub>anchor: "Ngai et al. (2011) produced one of the first systemic literature reviews"</sub>
- **descriptive / context**: Ahmed et al. (2015) surveyed anomaly detection in financial domains, focusing on clustering-based techniques and stressing validation on real-world data. (p. 7)[^original]  
  <sub>anchor: "they specifically focused on clustering based techniques, discussing their assumptions"</sub>
- **descriptive / limitation**: Access to real financial organisation data is often very difficult due to privacy and competition, and the authors state they succeeded in collecting such data and validating their models. (p. 7)[^original]  
  <sub>anchor: "Accessing real data from financial organizations is often very difficult, due to privacy reasons and competition"</sub>
- **descriptive / context**: The authors argue for relational data approaches, proposing social network metrics such as betweenness centrality to complete client risk profiles and offer parameters harder for launderers to manipulate. (p. 7)[^original]  
  <sub>anchor: "we propose to include social network metrics (Wasserman & Faust, 1994) in the monitoring system"</sub>
- **descriptive / context**: Sparrow (1991) showed the value of link-form data for questions such as who is central in a criminal network, which names look like aliases, and whether smurfing is present. (p. 8)[^original]  
  <sub>anchor: "Authors like Sparrow (1991) proved the advantage of representing data in link form"</sub>
- **descriptive / context**: Didimo et al. (2011) developed a system for visual analysis of financial networks using automatic k-core clustering and centrality scores per node. (p. 8)[^original]  
  <sub>anchor: "developed a system for the visual analysis of financial networks, which relies on automatic _k-core_ clustering"</sub>
- **descriptive / limitation**: Network visual analysis loses its power when the graph is extremely big. (p. 8)[^original]  
  <sub>anchor: "Network visual analysis can be very useful for AML, but it loses its power when the graph is extremely big"</sub>
- **descriptive / context**: The authors note that it remains unclear which AML method performs best and that neither a single strategy nor only European guidelines seems sufficient, proposing a mixed relational approach as future research rather than a tested claim. (p. 8)[^original]  
  <sub>anchor: "it is still unclear which set of methods might better perform"</sub>

## 3. Case Study and Research Design

- **descriptive / data or feature**: The case study analyses the central database of a medium-large Italian factoring company, with operations from November 2013 to June 2015, a company operating for more than 20 years; company and data are anonymised. (p. 8)[^original]  
  <sub>anchor: "we analyzed the central database of a medium-large factoring company in Italy, where the financial operations from November 2013 to June 2015 are recorded"</sub>
- **mandatory / requirement**: Under Italian law, each financial institution must record all transactions of at least 15,000 euros, and smaller transactions when their aggregate value is equal to or above 15,000 euros, to address smurfing. (p. 8)[^original]  
  <sub>anchor: "each financial institution has to record all the transactions amounting to at least 15,000 euros"</sub>

## 2. Detecting Money Laundering

- **descriptive / limitation**: Some previous SNA research proved to be highly data dependent, often requiring the integration of multiple sources. (p. 8)[^original]  
  <sub>anchor: "Some previous research following the SNA approach proved to be extremely data dependent"</sub>
- **descriptive / limitation**: The authors' method is most useful when near on-time decisions are needed and a single data source, such as a medium-large financial institution's database, is available. (p. 8)[^original]  
  <sub>anchor: "Our method proves its highest utility when almost on-time decisions are required and a single data source is available"</sub>

## 3.1. Networks Extraction and Risk Factors

- **descriptive / context**: In factoring, a factor buys a receivable from a seller, and later receives payment from the debtor who owes the payment on the invoice. (p. 9)[^original]  
  <sub>anchor: "the factoring company ( _factor_ ) purchases a receivable (usually an invoice) at a discounted price from a _seller,_"</sub>
- **descriptive / typology or red flag**: Suspicious cases include those where seller and debtor share the same beneficial owner, and illicit activity linked to fictitious invoicing or inflated prices when goods or services are not really supplied. (p. 9)[^original]  
  <sub>anchor: "drawing the attention on suspicious cases where, for instance, the seller and the debtor share the same beneficial owner"</sub>
- **descriptive / finding or result**: Castellón González and Velásquez (2013) reported that evasion by false invoicing historically represented between 15% and 25% of total VAT evasion, increasing in crisis years. (p. 10)[^original]  
  <sub>anchor: "evasion by false invoicing has historically represented between 15% and 25% of total VAT evasion"</sub>
- **descriptive / finding or result**: In data analysed by Irwin, Choo and Liu (2012), fictitious invoicing was used in 10% of money laundering cases and fictitious sales/purchases in 9% of cases. (p. 10)[^original]  
  <sub>anchor: "fictitious invoicing was used in the 10% of cases of money laundering and fictitious sales/purchases in the 9% of cases"</sub>
- **descriptive / method**: The authors focus on money transfers from the debtor to the factor, the operations used to put dirty money into the clean circuit, with particular attention to wirings involving companies abroad. (p. 10)[^original]  
  <sub>anchor: "we focused our analysis on the money transfers made from the debtor to the factor (point 4)"</sub>
- **descriptive / data or feature**: The complete transactions network contains 559 nodes (sellers, debtors and nodes with a double role) and 33,670 links representing money transfers in Italy and abroad, with the factoring company not represented. (p. 10)[^original]  
  <sub>anchor: "It includes 559 nodes (sellers/debtors and nodes with a double role) and 33,670 links"</sub>
- **descriptive / method**: Several networks were derived by filtering the full graph on three FIU-reported risk factors: geographic area, economic sector, and amount of operations, with a separate network for each. (p. 10)[^original]  
  <sub>anchor: "we filtered the original graph considering some of the major risk factors reported by the Financial Intelligence Unit"</sub>
- **descriptive / context**: The database does not allow distinguishing legal from illegal transactions, and the aim is to assess client risk profiles rather than identify specific illegal transfers. (p. 11)[^original]  
  <sub>anchor: "The database of the factoring company does not contain sufficient information to distinguish between legal and illegal transactions"</sub>
- **descriptive / method**: In the Transaction Network, each arc is weighted from 1 to 3 by transaction amount: score 1 below 50,000 euros, score 2 between 50,000 and 249,999 euros, and score 3 for higher amounts. (p. 11)[^original]  
  <sub>anchor: "we assigned a score of 1 to all the transactions with an amount below 50,000 euros"</sub>
- **descriptive / finding or result**: The authors report that this amount binning leads to much better performance of the predictive models. (p. 11)[^original]  
  <sub>anchor: "Operating this binning leads, in our case study, to a much better performance of the predictive models"</sub>
- **permissive / method**: Other thresholds, or weighting arcs by nominal transaction amount, are possible; the choice is left to the analyst. (p. 11)[^original]  
  <sub>anchor: "Other thresholds are also possible – as well as weighting the arcs with the nominal amount of each transactions"</sub>
- **descriptive / limitation**: Aggregating values across operations between two nodes only partly addresses smurfing, given the lack of information to separate legal from illegal transfers. (p. 11)[^original]  
  <sub>anchor: "since one can also consider the aggregated value of multiple operations existing between two nodes"</sub>
- **descriptive / method**: In the geographic and sector networks, each node receives a risk level and each link a risk score equal to the average of the risk levels of the nodes it connects; the average was found most effective, though maximum is possible. (p. 12)[^original]  
  <sub>anchor: "we assign a risk score to each link, calculated as the average of the risk level of the nodes it connects"</sub>
- **descriptive / method**: Economic sectors were coded using the Italian ATECO 2007 classification, developed by ISTAT in line with the European nomenclature. (p. 12)[^original]  
  <sub>anchor: "we referred to the ATECO 20071 national classification of economic activities, developed by the Italian National Institute of Statistics (ISTAT)"</sub>
- **descriptive / method**: Seller and debtor companies were split into high or low fraud-risk sectors by two company experts, using FIU national reports and counts of suspicious and illicit transactions. (p. 12)[^original]  
  <sub>anchor: "This classification was made by two experts working together for the factoring company"</sub>
- **descriptive / typology or red flag**: The sectors classified as high risk are public procurement, construction, ferrous materials, car sales, road haulage, high tech goods sales, cleaning and maintenance services, consultancy, precious metals and gemstones, artworks sales, oil and grain wholesale, advertising, online IT services, supermarket, betting and gambling, weapons and explosives, waste management and waste water treatment; all other sectors are low risk. (p. 12)[^original]  
  <sub>anchor: "we here list all the sectors classified as high risk (all the remaining sectors were classified as low risk)"</sub>
- **descriptive / context**: The authors state that they did not aim to find or defend the best sector classification method; their contribution was testing the experts' classification. (p. 12)[^original]  
  <sub>anchor: "our contribute here was more about testing the effectiveness of the classification made by the company experts"</sub>
- **recommended / recommendation**: The authors suggest revising each sector classification year by year according to updates of national reports. (p. 12)[^original]  
  <sub>anchor: "We also suggest revising each classification year by year, according to the updates of national reports"</sub>
- **descriptive / method**: Geographic risk for Italian regions combines three measures: percentage of crimes per province from ISTAT, number of suspicious operations from FIU reports, and whether the region has a bigger Mafia presence; each gets an ordinal score from 1 to 3 by percentile band (lowest 30%, middle 40%, highest 30%) and the three are averaged. (p. 13)[^original]  
  <sub>anchor: "we calculated a partial risk score (ordinal, ranging from 1 to 3) according to whether the Italian region was approximately in the lowest 30%"</sub>
- **descriptive / method**: Foreign states were assessed using the Italian Ministry of Economy and Finance white list, tax haven lists, OECD tax exchange compliance, the Corruption Perception Index, and the FATF Public Statement of jurisdictions with strategic deficiencies. (p. 13)[^original]  
  <sub>anchor: "the list of jurisdictions that have strategic deficiencies and pose a risk to the international financial system (FATF Public Statement)"</sub>
- **descriptive / finding or result**: Transactions involving foreign states represent less than 1% of total money transfers in the dataset, so they are almost negligible. (p. 13)[^original]  
  <sub>anchor: "transactions involving foreign states are almost negligible in our dataset, representing less than 1% of the total money transfers"</sub>
- **descriptive / method**: The Tacit Link Network connects clients with a factoring relationship who share the same beneficial owner or authorised representative, treated as an implicit risk factor for tacit illicit agreements. (p. 13)[^original]  
  <sub>anchor: "the implicit connection among clients who have a factoring relationship and share the same beneficial owner"</sub>
- **descriptive / finding or result**: The Tacit Link Network has 90 connected nodes after removing isolates, and is analysed visually. (p. 13)[^original]  
  <sub>anchor: "We found 90 connected nodes and, after having removed the isolates, we carried out a visual analysis"</sub>
- **descriptive / definition**: By owner the authors mean the single person making the financial operation in his or her name, or the person managing the company who makes a specific operation. (p. 13)[^original]  
  <sub>anchor: "By _owner_ we intend the single person who is making the financial operation on his/her name"</sub>
- **descriptive / definition**: Representatives are people, usually employees, who are authorised to operate on behalf of a company. (p. 13)[^original]  
  <sub>anchor: "those people (usually employees) who are authorized to operate on behalf of a company"</sub>
- **descriptive / context**: The authors say the tacit link risk factor is not sufficiently stressed in the common guidelines. (p. 13)[^original]  
  <sub>anchor: "a risk factor not sufficiently stressed in the common guidelines"</sub>
- **descriptive / finding or result**: The authors claim that analysing tacit links is vital for spotting tacit, potentially illicit, agreements. (p. 13)[^original]  
  <sub>anchor: "We claim such analysis is vital to spot tacit, potentially illicit, agreements."</sub>
- **descriptive / method**: Before calculating metrics, loops (nodes linked to themselves, due to missing debtor data) were removed; for sector and geographic graphs, multiple arcs were merged by averaging their weights, which the authors say gave the best results though it is optional. (p. 14)[^original]  
  <sub>anchor: "Before operating the calculus we removed the loops (cases where nodes link to themselves, due to missing data about the debtor)"</sub>
- **descriptive / method**: The model was finally restricted to high-risk links by filtering out medium and low risk links, to improve model performance. (p. 14)[^original]  
  <sub>anchor: "we focused on high risk operations, by filtering out medium and low risk links"</sub>

---

[source overview](overview.md) | [next part](digest-002.md)

[^original]: Andrea Fronzetti Colladon, Elisa Remondi, "Using social network analysis to prevent money laundering" (2016-09-20). https://arxiv.org/abs/2105.05793
