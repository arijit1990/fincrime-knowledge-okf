---
type: Source Digest
title: 'Partnering in the Fight Against Financial Crime: Data Protection, Technology and Private Sector Information Sharing - part 5 of 7 (pp. 40-50)'
description: 'Verified paraphrased digest, pp. 40-50: SECTION FOUR: Presentation of information sharing case studies'
resource: https://www.fatf-gafi.org/en/publications/Digitaltransformation/Partnering-in-the-fight-against-financial-crime.html
tags:
- data_features
- international_standard
- intl
- other
- privacy_data_protection
- public_private_partnership
- technology_architecture
status: stable
source_id: fatf-partnering-in-the-fight-against-financial-crime-data-protection-t
issuer: fatf
issuer_name: Financial Action Task Force
jurisdictions:
- INTL
tier: 2
instrument_type: other
normative_force: international_standard
publication_date: 2022-07
legal_status: current
part: 5
parts_total: 7
content_mode: digest
generated:
  by: claude-code-subagent/claude-sonnet-5-5
  at: '2026-11-17T02:29:22Z'
verified:
- by: process:kb-digest-check/anchor-match
  at: '2026-11-17T02:29:22Z'
- by: claude-code-judge-agent/claude-opus-5-5
  at: '2026-11-17T02:29:22Z'
sources:
- id: original
  resource: https://www.fatf-gafi.org/en/publications/Digitaltransformation/Partnering-in-the-fight-against-financial-crime.html
  title: 'Partnering in the Fight Against Financial Crime: Data Protection, Technology and Private Sector Information Sharing'
  author: org:fatf
digest_points: 59
---

# Partnering in the Fight Against Financial Crime: Data Protection, Technology and Private Sector Information Sharing (digest)

[previous part](digest-004.md) | [source overview](overview.md) | [next part](digest-006.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (pp. 40-50) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **international standard**.

## Box 4.6 AML Bridge (Estonia)

- **descriptive / finding or result**: A lesson from AML Bridge is that unclear regulations are the biggest barrier to private-to-private data sharing: banks were only willing to start sharing in a way explicitly permitted under the relevant legislation and regulations. (p. 40)[^original]  
  <sub>anchor: "Unclear regulations are the biggest barrier to private-to-private data sharing"</sub>
- **descriptive / finding or result**: A lesson from AML Bridge is that the GDPR is not a barrier but an enabler of financial crime data sharing: the consistent framework across private banks and regulators lets all participants quickly agree whether a particular form of private-to-private sharing is acceptable. (p. 40)[^original]  
  <sub>anchor: "The GDPR is not a barrier, but an enabler of financial crime data sharing"</sub>
- **descriptive / finding or result**: A lesson from AML Bridge is that regulators, especially supervisors and data protection authorities, must be involved from the beginning. Its success comes partly from governance that kept all stakeholders informed and actively involved, and banks gained confidence to innovate because there was no risk of a negative surprise from the FSA or DPA. (p. 40)[^original]  
  <sub>anchor: "Regulators (especially supervisors and data protection authorities) must be involved from the beginning"</sub>
- **descriptive / finding or result**: A lesson from AML Bridge is that, within banks, executive sponsorship is a necessary precondition to kick off new data sharing initiatives: creating and implementing one takes significant effort from many teams across many months and has to be a priority for senior bank leadership. (p. 40)[^original]  
  <sub>anchor: "executive sponsorship is a necessary precondition to kick off new data sharing initiatives"</sub>
- **descriptive / context**: Government oversight of AML Bridge is provided by the Financial Supervision Authority (a member and observer of the Steering Committee), the FIU (a Steering Committee member) and the Data Protection Authority (a Steering Committee observer). (p. 40)[^original]  
  <sub>anchor: "Government oversight of AML Bridge is provided by the Financial Supervision Authority"</sub>
- **descriptive / definition**: The case study defines APP (authorised push payment) fraud as fraud where an individual is deceived into sending a payment to a bank account controlled by the fraudster, often by the fraudster obtaining information on the victim and impersonating a legitimate company; it may also include investment or romance scams. Because the victim authorises the payment, it is often difficult or impossible to reverse. (p. 40)[^original]  
  <sub>anchor: "APP fraud is where an individual is deceived into sending a payment to a bank account controlled by the fraudster."</sub>

## Box 4.7. safeFBDC (Germany)

- **descriptive / context**: The safeFBDC (safe Financial Big Data Cluster) prototype forms part of the European GAIA-X initiative, which seeks a single ecosystem of cloud and data services covered by European data law. It is a platform where AI applications for Europe's financial sector are built and offered, allowing secure data exchange while individual data sovereignty is preserved. (p. 40)[^original]  
  <sub>anchor: "safeFBDC (safe Financial Big Data Cluster) prototype project is part of the European GAIA-X initiative"</sub>
- **descriptive / method**: In the safeFBDC AML use case, banks' financial data are pooled on the safeFBDC platform and applications are built on it to combat money laundering. (p. 40)[^original]  
  <sub>anchor: "financial data from banks are brought together on the safeFBDC platform and applications are set up to combat money laundering"</sub>

## Box 4.7 safeFBDC (Germany)

- **descriptive / context**: The intended outcome of safeFBDC is pooling financial data across the industry to significantly improve the performance of AI algorithms, driving efficiency and transparency. The AML use case realises a graph network approach to identify money laundering activity. (p. 41)[^original]  
  <sub>anchor: "the AML use case realises a graph network approach to identify money laundering activity"</sub>
- **descriptive / method**: safeFBDC uses a decentralised ecosystem in which data is stored in federated silos owned by the banks and only pooled in a closed environment for the runtime of the algorithm. The pooled data is deleted right after processing finishes. (p. 41)[^original]  
  <sub>anchor: "A decentralised ecosystem allows data to be stored in federated silos owned by the banks"</sub>
- **descriptive / data or feature**: Initially safeFBDC will use SEPA transactions. Requirements for a minimal viable dataset have been formalised with specific attention to the trade-off between censoring end-client level information and the learning performance the algorithm requires. (p. 41)[^original]  
  <sub>anchor: "Initially, SEPA transactions will be used."</sub>
- **descriptive / method**: In safeFBDC, data is encrypted at rest and in transit, and static decentralised tokenisation of personal identifiable data ensures safety even in the event of a leak. The prototype infrastructure does not allow any user to interact directly with the data; only algorithms pre-approved by the data owners can access it. (p. 41)[^original]  
  <sub>anchor: "Static decentralised tokenisation of the personal identifiable data ensures safety even in the event of a leak."</sub>
- **descriptive / context**: As an early stage project where data is not yet being transferred, safeFBDC participants were still identifying the most appropriate legal basis for sharing. Data owners must pre-approve algorithms that can run on the data, so the owner controls which data is processed, how, and how results are handled. Personal data is transferred but, because of tokenisation and the closed data pool design, is not shared with other entities, and specific regulations (such as the requirement to perform AML monitoring and report suspicious transactions) form a more general legal basis. (p. 41)[^original]  
  <sub>anchor: "participants are still in the process of identifying the most appropriate legal basis for sharing"</sub>
- **descriptive / method**: On proportionality, safeFBDC works with a minimal viable dataset assumption and aims at a no trust environment. Data leaves the data owner's control only for the time of calculation, in a secure and closed space, and is deleted right after the calculations. (p. 41)[^original]  
  <sub>anchor: "The initiative works with a minimal viable dataset assumption, focusing on creating a no trust environment."</sub>
- **descriptive / method**: In safeFBDC, transaction data accuracy and completeness are ensured because banks provide data directly to the platform, with emphasis on high standards of data validation and testing, including back-testing, of algorithms; this also ensures integrity of the output data. (p. 41)[^original]  
  <sub>anchor: "Transaction data accuracy and completeness are ensured because banks provide data directly to the platform."</sub>

## Box 4.7. safeFBDC (Germany)

- **descriptive / context**: Deutsche Börse Group, a German company, leads the safeFBDC workstream. Other participants are three technology providers (Spotixx, HAWK:AI and Google), four financial institutions (Commerzbank, Deutsche Bank, Helaba and ING) and a state authority, the Hessian Ministry of Economics, Energy, Transport and Housing. (p. 41)[^original]  
  <sub>anchor: "three technology providers (Spotixx, HAWK:AI and Google), four financial institutions (Commerzbank, Deutsche Bank, Helaba and ING)"</sub>

## Box 4.7 safeFBDC (Germany)

- **descriptive / context**: For safeFBDC transparency/notification, AML monitoring and reporting are deeply embedded in a bank's workflow, so established systems can and will be used as core pillars of the new approach. (p. 42)[^original]  
  <sub>anchor: "meaning that established systems can and will be used as core pillars in the new approach"</sub>
- **descriptive / method**: In safeFBDC the algorithms report suspicious patterns, which are then subject to further comprehensive investigation. The data owner controls the algorithm output, preventing sensitive information being disclosed; alerts are generated from suspicious patterns detected by the model, and otherwise disclosure and data transfer practices remain unchanged. (p. 42)[^original]  
  <sub>anchor: "The algorithms report suspicious patterns which is then subject to further comprehensive investigation."</sub>
- **descriptive / method**: In safeFBDC, personal data does not leave the data owner's data space without being pseudonymised. All security standards for encryption are followed and key management can be handled by each data owner; any change to access authorisation is logged and can be validated, and algorithms can only be executed upon the digital signature of each data owner. (p. 42)[^original]  
  <sub>anchor: "Personal data does not leave the data space of the data owner without being pseudonymised."</sub>

## Box 4.8 EuroDaT (Germany)

- **descriptive / context**: EuroDaT is a project funded by the German Federal Ministry for Economic Affairs and Climate Action (BMWK) that aims to build a European data trustee enabling data sharing, with a focus on financial data, in a manner compliant with GAIA-X. One envisaged use case is fraud detection. It aims to facilitate semi- or fully-autonomous sharing while remaining DPP-compliant and keeping a low barrier of entry for participants. (p. 42)[^original]  
  <sub>anchor: "EuroDaT is a project funded by the German Federal Ministry for Economic Affairs and Climate Action (BMWK)."</sub>
- **descriptive / method**: EuroDaT explicitly does not want data pooled or centrally stored. It intends to act as an information platform through which data is piped for individual queries, connecting individual data providers and users rather than acting as a repository. Data is transmitted for each individual process according to contractual or other legal connections, stored temporarily in flash vaults inaccessible even to the trustee, analysed by algorithms provided by the data giver, data receiver or a third party, with results passed on as agreed; the trustee then erases the data permanently. (p. 42)[^original]  
  <sub>anchor: "EuroDaT explicitly does not want data to be pooled or centrally stored."</sub>

## Box 4.8. EuroDaT (Germany)

- **descriptive / context**: EuroDaT aims to vary its participants by use case. They include a Hessen state ministry, several academic bodies (ZEVEDI, University of Saarland, Goethe University Frankfurt, DFKI) and technology providers (ATOS, Deloitte, d-fine, Lexemo). (p. 42)[^original]  
  <sub>anchor: "academics (ZEVEDI, University of Saarland, Goethe University Frankfurt, DFKI)"</sub>

## Box 4.8 EuroDaT (Germany)

- **descriptive / data or feature**: There is currently neither a limit nor a proscription on the types of data or specific data points that can or will be shared through EuroDaT. (p. 43)[^original]  
  <sub>anchor: "There is currently neither a limit nor proscription on the types of data"</sub>
- **descriptive / context**: As an early stage framework where data is not yet being transferred, EuroDaT participants were still identifying the most appropriate legal basis. Because of the project's flexibility, each data transaction must be analysed on its own terms, and different data types fall under different DPP regimes and bases for sharing. (p. 43)[^original]  
  <sub>anchor: "each data transaction must be analysed on its own terms"</sub>
- **descriptive / context**: EuroDaT will establish an infrastructure for data analysis and does not decide on data processing itself; responsibility for DPP concerns lies primarily with its clients, who decide on data processing. EuroDaT plans to offer a data taxonomy to make categorising data easier and help identify and avoid data protection risks. (p. 43)[^original]  
  <sub>anchor: "The responsibility for DPP concerns lies primarily with the clients, who make the decision on data processing."</sub>
- **descriptive / context**: In EuroDaT, responsibility for maintaining data accuracy and completeness lies with the providing parties, and depending on the use case it may be necessary to develop common standards. The current AML use case plans to build on existing systems and enable better cooperation between banks without requiring disclosure of data, so current models on transparency/notification should be transferable. (p. 43)[^original]  
  <sub>anchor: "The responsibility for maintaining the data for accuracy and completeness therefore lies with the providing parties."</sub>
- **descriptive / context**: EuroDaT envisions clients maintaining full control over their data, so further transfer or disclosure of any data shall be contractually prohibited and ideally also technically impossible, since the trustee has no access to the actual data sets. (p. 43)[^original]  
  <sub>anchor: "further transfer or disclosure of any data shall be both contractually prohibited but ideally also technically impossible"</sub>
- **descriptive / limitation**: The EuroDaT trustee is founded on data being processed only as determined in advance by the data giver, in an environment guaranteeing no access by unauthorised third parties, and it logs both contractual agreements and the access granted under them. The case study states that this means the trustee cannot guarantee that data is processed lawfully, because doing so would require identifying information about the data, which runs counter to the trustee's principal idea. (p. 43)[^original]  
  <sub>anchor: "This also means that the trustee cannot guarantee that data is processed lawfully."</sub>
- **descriptive / limitation**: The trustee cannot take the burden of considering DPP principles away from its users: the responsible party (the financial institutions) will always have to ensure they possess and process data lawfully. This is proving a challenge, as most interested third parties, including financial institutions, look to the trustee to address DPP requirements. (p. 43)[^original]  
  <sub>anchor: "the trustee cannot take the burden of considering DPP principles away from its users"</sub>
- **descriptive / limitation**: At this early stage, working with the EuroDaT trustee is still considerable work for third parties including the financial sector. Data controllers are in the best position to describe their own DPP considerations, and only by working closely together can the trustee and third parties hope to standardise and automate future taxonomies of data and their processing. (p. 44)[^original]  
  <sub>anchor: "working with the trustee, especially at this early stage, is still considerable work for third parties"</sub>

## SECTION FIVE: What are the potential issues that arise in implementing private sector information sharing for AML/CFT/CPF in line with DPP frameworks and requirements?

- **descriptive / context**: Section Five sets out common issues in designing and implementing private sector information sharing for AML/CFT/CPF, based on feedback from focus group discussions on the case studies, public authorities and industry engagement; Section 6 contains recommendations. The FATF states that each potential initiative needs to be considered case by case depending on its unique characteristics and the relevant DPP requirements. (p. 44)[^original]  
  <sub>anchor: "each potential initiative needs to be considered on a case-by-case basis"</sub>
- **descriptive / context**: Between October 2021 and June 2022 the FATF project team conducted six focus group discussions and presentations with jurisdictions including Estonia, Germany, the Netherlands, Singapore, the United Kingdom and the United States, plus other engagement with public and private sector stakeholders in Europe by the Secretariat. (p. 45)[^original]  
  <sub>anchor: "the FATF project team has conducted six focus group discussions and presentations with jurisdictions"</sub>

## Policy issues

- **descriptive / finding or result**: The case studies indicate that involvement and engagement of public authorities appears to be a significant factor in the success of private-sector AML/CFT/CPF information sharing initiatives, though authorities can play different roles and degrees of involvement. A total absence of government engagement, especially in the early stages, has often increased the challenges to private sector information exchange. (p. 45)[^original]  
  <sub>anchor: "a total absence of government engagement, especially in the early stages, has often increased the challenges"</sub>
- **descriptive / typology or red flag**: Without a clear contact point or leading agency spearheading sharing initiatives, information shared between private sector institutions may not necessarily align with national AML/CFT/CPF objectives and priorities. Participation by only a few selected or interested financial institutions (as in some use cases such as COSMIC, Box 4.2) has the potential to lead to risk migration, i.e. criminals shifting transactions to non-participating financial institutions. (p. 45)[^original]  
  <sub>anchor: "has the potential to lead to risk migration, i.e., criminals may shift their transactions to non-participating financial institutions"</sub>
- **descriptive / limitation**: Successful information sharing can be hampered by a lack of engagement, or the absence of a communication or co-ordination mechanism, between AML/CFT/CPF and DPP authorities. Such a lack can result in conflicts from a lack of mutual understanding of the critical public interests in both protecting the public from crime and terrorism and protecting privacy and personal data. (p. 45)[^original]  
  <sub>anchor: "successful information sharing can be hampered by a lack of engagement between AML/CFT/CPF and DPP authorities"</sub>
- **descriptive / limitation**: Participants in the case-study projects highlighted that without government support, private sector entities have had difficulty gaining support from peers and feedback from DPP authorities. That support and feedback is necessary to explain the utility of sharing initiatives (for example improving STR quality) and why sharing meets wider public interests, including AML/CFT/CPF objectives, reducing low quality or false positive/negative STRs, and preventing de-risking. (p. 46)[^original]  
  <sub>anchor: "without government support, private sector entities have experienced difficulties gaining the support of peers"</sub>
- **descriptive / limitation**: The FATF states there is yet to be a 'model template' of private sector information sharing that may comply with and advance both AML/CFT/CPF and DPP requirements. Data protection legislation is largely principles-based, so DPP authorities must consider each sharing proposal case by case, may not be comfortable endorsing a specific project for fear that endorsement is perceived as confirming all DPP requirements are met, and without co-ordination with AML/CFT/CPF authorities are unlikely to give the guidance financial institutions need. (p. 46)[^original]  
  <sub>anchor: "there has yet to be a “model template” of private sector information sharing"</sub>
- **descriptive / definition**: In a footnote, the report describes de-risking as financial institutions ending or restricting relationships with clients or client categories in order to avoid risk rather than manage it as the FATF's risk-based approach envisages. It adds that extra information may in some cases resolve suspicions and so secure fair access to financial services. (p. 46)[^original]  
  <sub>anchor: "De-risking is the phenomenon of financial institutions terminating or restricting business relationships with clients"</sub>
- **descriptive / context**: Section 6 recommendations addressing the policy issues include active facilitation by the public sector (paras 51-52), regular dialogue between DPP and AML/CFT/CPF authorities (paras 53-55), and early and ongoing engagement between the private sector and DPP authorities (para 60). (p. 47)[^original]  
  <sub>anchor: "active facilitation by the public sector (para.51-52), regular dialogue between DPP and AML/CFT/CPF authorities (para.53-55)"</sub>

## Legal issues

- **descriptive / limitation**: The range of national and international DPP laws and regulations poses challenges for private-to-private sharing projects: interested financial institutions have devoted substantial effort to reviewing laws, regulations and supervisory instruments to ascertain the legality of sharing arrangements in each jurisdiction. (p. 47)[^original]  
  <sub>anchor: "Interested financial institutions have devoted substantial effort to reviewing laws, regulation and other supervisory/regulatory instruments"</sub>
- **descriptive / limitation**: A legal question raised is whether sharing for AML/CFT/CPF purposes with other financial institutions, or across borders between entities within the same group, is lawful and compliant under AML/CFT/CPF and DPP rules and customer contractual arrangements. As a first step, institutions need to determine whether information to be shared is personal or non-personal under the relevant legal framework, and so whether DPP rules apply. DPP rules often require sharing to be 'necessary' or 'proportionate', to achieve 'legitimate interest', and/or to be explicitly permitted in legislation. (p. 47)[^original]  
  <sub>anchor: "institutions need to determine whether information proposed to be shared qualifies as personal or non-personal information"</sub>
- **descriptive / limitation**: Some participants found it challenging to demonstrate that sharing was 'necessary' before testing an initiative to obtain clear and definitive results. Private sector entities may be unwilling to take legal risk where they perceive legal uncertainty under DPP laws, lack input from the leading government policy departments, or the initiative is not required for STR reporting by national governments or the FATF Standards; the latter is particularly common for data shared before a suspicion is formed, given stricter requirements. (p. 47)[^original]  
  <sub>anchor: "noted the challenge of demonstrating that sharing was"</sub>
- **descriptive / limitation**: Pre-suspicion sharing of personal information is often subject to much stricter limitations because it applies to a broad set of data, and in some jurisdictions sharing at this stage may not be permitted under DPP laws. Institutions in certain jurisdictions may therefore need to carefully consider mechanisms to eliminate personal data shared at the pre-suspicion stage (for example use of PETs or adjustments in data scope). (p. 47)[^original]  
  <sub>anchor: "Pre-suspicion sharing of personal information is often subject to much stricter limitations"</sub>
- **descriptive / limitation**: For post-suspicion sharing, some financial institutions may seek further guidance on using information obtained from a sharing initiative for functions other than reporting STRs (for example updating customer due diligence information, risk assessment and management, or terminating the customer relationship), and whether such secondary uses would be fair, legitimate, necessary, proportionate or compatible with the original purpose of detecting suspicious activity. (p. 48)[^original]  
  <sub>anchor: "some financial institutions may seek further guidance on how to use information obtained from an information sharing initiative"</sub>
- **descriptive / limitation**: Where consent may be relied on as a lawful basis, it assumes the institution has met usual DPP transparency requirements (for example informing customers of the types of third parties with access to personal data). Existing consent notices have typically focused on sharing with operational agencies such as FIUs or law enforcement, not other financial institutions; changing consent provisions poses logistical challenges, and later withdrawal of consent would be problematic. (p. 48)[^original]  
  <sub>anchor: "such notice of sharing typically has focused on sharing with operational agencies such as FIUs or law enforcement agencies"</sub>
- **descriptive / finding or result**: Relying on consent may be problematic in some jurisdictions where consent could be construed as coerced or not freely given, for example if the customer has no other option to receive the financial services or consent is demanded as a condition of service. The FATF concludes that consent is unlikely to be the most viable, or the sole, lawful basis for AML/CFT/CPF related sharing. (p. 48)[^original]  
  <sub>anchor: "consent is unlikely to be the most viable, or the sole, lawful basis for AML/CFT/CPF related sharing"</sub>
- **descriptive / limitation**: Institutions in sharing initiatives would need to devise additional measures to ensure that sharing of customer/transaction data, and any resulting adjustment of customer relationships or risk rating, does not lead to tipping-off or go against the FATF Standards (for example Recommendation 21), as highlighted in section 6.5 of the Phase 1 Stocktake Report. Some participants were confused whether sharing with a third party (not the client) could constitute tipping off, and the private sector at times found it challenging to design measures meeting both sharing and confidentiality objectives without supervisor or regulator guidance. (p. 48)[^original]  
  <sub>anchor: "will not lead to tipping-off or go against the relevant FATF Standards"</sub>
- **permissive / recommendation**: The FATF states that future initiatives could also consider designing platforms in a manner that prevents tipping off (for example using encrypted queries on decentralised data). (p. 48)[^original]  
  <sub>anchor: "Future initiatives could also consider designing platforms in a manner that prevents tipping off"</sub>
- **descriptive / limitation**: In some cases, while data use may be relevant to criminal investigations, such uses can limit participating financial institutions' ability to be transparent with the data subject and provide the avenues for redress required by DPP rules. (p. 48)[^original]  
  <sub>anchor: "such uses can limit the ability of participating financial institutions to be transparent with the data subject"</sub>
- **descriptive / context**: The report notes that FATF's tipping-off rules (Recommendation 21) serve to protect the confidentiality of criminal investigations, and that such rules are required to be set out in domestic law or regulation. (p. 48)[^original]  
  <sub>anchor: "are required to be set out in domestic law or regulation"</sub>
- **descriptive / context**: The FATF Standards (Recommendation 2) also call for co-operation and co-ordination so that AML/CFT requirements are compatible with DPP rules. (p. 48)[^original]  
  <sub>anchor: "The FATF Standards (Recommendation 2) also require co-operation and co-ordination"</sub>
- **descriptive / context**: Depending on domestic DPP laws, exceptions and exemptions to privacy rights for purposes of prevention, investigation, detection or prosecution of crime may apply. The case studies highlight the need for agreed safeguards (for example the requirement for financial institutions using alerts from an AML facility to undertake their own investigation) and for possibilities for data subjects to appeal decisions removing access to financial services and to provide clarifying or additional information. (p. 49)[^original]  
  <sub>anchor: "The case studies highlight the need for agreed safeguards"</sub>
- **descriptive / context**: Section 6 recommendations addressing the legal issues include active facilitation by the public sector (paras 51-52), data protection by design (paras 58-59), early and ongoing engagement between the private sector and DPP authorities (para 60), and developing indicators and metrics to measure success (para 61). (p. 49)[^original]  
  <sub>anchor: "pursuing data protection by design (para.58-59)"</sub>

## Operational issues

- **descriptive / context**: Challenges identified in the FATF Phase 1 Stocktake Report remain valid in recent private sector information sharing initiatives, and are relevant to both public and private sector entities, at institution or sector level. The Section 6 recommendations aim to ensure that initiatives are effective, efficient and timely and avoid delaying detection of potential suspicious transactions, customers or criminal networks, while complying with DPP requirements. (p. 49)[^original]  
  <sub>anchor: "avoid delaying the detection of potential suspicious transactions or customers/criminal network"</sub>

## Operational issues - Data scope

- **descriptive / finding or result**: Some case studies found it challenging to determine the scope of data shared while achieving the initiative's aims. To comply with DPP requirements (lawfulness and data minimisation), some initiatives reduced the scope and types of data shared. This is particularly relevant for pre-suspicion sharing, where some projects focused on data types that generally contain less or no personally identifiable data (for example transactions by legal persons), and others reduced the number of data points shared. (p. 50)[^original]  
  <sub>anchor: "some of the sharing initiatives have adjusted and reduced the scope and types of data shared"</sub>
- **descriptive / limitation**: As a result of narrowing data scope, some initiatives faced challenges meeting original goals and had to revise their sharing objectives and expected outcomes. Feedback from some private sector participants indicates that narrowing scope, while helping DPP compliance, can reduce or undermine project utility and may raise questions whether the data shared is sufficient to meaningfully help institutions understand suspicious transactions across institutions. (p. 50)[^original]  
  <sub>anchor: "this can also reduce or undermine the utility of the project"</sub>

## Operational issues - Data accuracy and reliability

- **descriptive / limitation**: Some case studies used privacy enhancing technologies (PETs) to mask customers' personal identity. Participants noted that PETs can pose operational challenges depending on use: in some projects the specific PETs may not have been fit-for-purpose, making it harder to determine the accuracy of data received/shared and affecting reliability and quality of sharing. (p. 50)[^original]  
  <sub>anchor: "the specific PETs used may not have been fit- for-purpose"</sub>
- **descriptive / limitation**: Project participants had to spend additional resources tracing back the identity of relevant shared data before meaningful follow-up such as monitoring or filing an STR. These challenges can be magnified by data preparation and interoperability issues, and where records cannot be effectively linked there is a risk of ambiguous record linkage (information relating to two unconnected persons being erroneously linked). (p. 51)[^original]  
  <sub>anchor: "project participants had to spend additional resources to trace back the identity of the relevant shared data"</sub>

## Operational issues - Data security

- **descriptive / limitation**: Regardless of whether PETs are used, private sector participants would need to devise a secured sharing channel. This is a fundamental step because any leakage of data stored and communicated in a sharing initiative could have serious consequences, including for customers' data rights, AML/CFT/CPF effectiveness, public trust in the initiative and institutions, and financial and non-financial harm to individuals. (p. 51)[^original]  
  <sub>anchor: "any leakage of data stored and communicated as part of the sharing initiative could have serious consequences"</sub>

---

[previous part](digest-004.md) | [source overview](overview.md) | [next part](digest-006.md)

[^original]: Financial Action Task Force, "Partnering in the Fight Against Financial Crime: Data Protection, Technology and Private Sector Information Sharing" (2022-07). https://www.fatf-gafi.org/en/publications/Digitaltransformation/Partnering-in-the-fight-against-financial-crime.html
