---
type: Source Digest
title: 'Partnering in the Fight Against Financial Crime: Data Protection, Technology and Private Sector Information Sharing - part 3 of 7 (pp. 21-30)'
description: 'Verified paraphrased digest, pp. 21-30: SECTION FOUR: Presentation of information sharing case studies'
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
part: 3
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
digest_points: 44
---

# Partnering in the Fight Against Financial Crime: Data Protection, Technology and Private Sector Information Sharing (digest)

[previous part](digest-002.md) | [source overview](overview.md) | [next part](digest-004.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (pp. 21-30) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **international standard**.

## SECTION FOUR: Presentation of information sharing case studies

- **descriptive / context**: The case studies are examples where entities and authorities have endeavoured to balance AML/CFT/CPF and DPP objectives within the applicable legal framework to advance private sector information sharing. Most were designed, implemented and co-ordinated with both AML/CFT/CPF and DPP authorities; digital transformation assisted but other measures were also required. One example is in a fraud context because it involved a certification/approval regime by a DPP authority (Box 4.4). (p. 21)[^original]  
  <sub>anchor: "Most of these projects have been designed, implemented, and co-ordinated with both AML/CFT/CPF and DPP authorities."</sub>
- **descriptive / definition**: The case studies reflect two scenarios: (a) pre-suspicion information sharing, meaning sharing and analysis of large volumes of de-identified/pseudonymised/encrypted information to identify suspicious transactions; and (b) post-suspicion information sharing, meaning narrow, targeted sharing using personally identifiable information related to suspicious transactions to advance specific investigations. Depending on the regime they involve different DPP considerations, with pre-suspicion sharing generally subject to stricter limitations in line with individual privacy rights. (p. 21)[^original]  
  <sub>anchor: "with pre-suspicion sharing generally being subject to stricter limitations"</sub>
- **descriptive / limitation**: Case studies are based on information from the authorities and institutions involved or public information; the legal reasoning and facts presented represent the views of the relevant jurisdictions/stakeholders rather than the FATF. Most focus on FI-to-FI sharing but some include sharing with public authorities. (p. 21)[^original]  
  <sub>anchor: "represent the views of the relevant jurisdictions/stakeholders rather than the FATF"</sub>

## Box 4.1. TriBank pilot (UK)

- **descriptive / case example**: Box 4.1 (UK, TriBank pilot, following the FutureFlow ICO Sandbox): pre-suspicion private-to-private sharing in bulk of transactional data with pseudonymised account identifiers, to identify clusters/typologies. Led by a consultancy with three UK banks (data controllers) and one technology provider, FutureFlow (data processor). Before the pilot, the UK ICO engaged with FutureFlow and considered key data protection issues in a regulatory sandbox. (p. 21)[^original]  
  <sub>anchor: "pre-suspicion information sharing in bulk of transactional data that has undergone pseudonymisation in bulk"</sub>
- **descriptive / method**: TriBank aimed to improve detection of linked unusual transactions that could indicate potential ML/TF. When a transaction was flagged as unusual, the relevant bank would re-identify it and, consistent with usual policies, investigate further and if warranted submit an STR. (p. 22)[^original]  
  <sub>anchor: "the relevant bank would re-identify the transaction and, consistent with its usual policies and procedures, investigate further"</sub>
- **descriptive / data or feature**: TriBank used pseudonymised historical transactions of small to medium enterprises over a year. Pseudonymisation minimised DPP risk, but because the data could be re-identified it was considered personal data. After pseudonymisation the data included account identifier (account number, sort code, IBAN etc.), transaction value(s), transaction IDs and time-stamps. (p. 22)[^original]  
  <sub>anchor: "because it could be re-identified, the data was considered personal data under the applicable legal framework"</sub>
- **descriptive / finding or result**: Lawful basis in TriBank: each bank, as data controller, had to decide under domestic law which lawful basis applied. Banks shared only pseudonymised transaction data pre-suspicion, and once an unusual or higher-risk pattern was detected they would share only narrowly focused targeted information to investigate specific activity as necessary. (p. 22)[^original]  
  <sub>anchor: "the banks shared only pseudonymised transaction data pre-suspicion"</sub>
- **descriptive / finding or result**: The FutureFlow/ICO sandbox suggested the most appropriate lawful basis was likely 'legitimate interest' (Article 6.1(f) GDPR), and the ICO issued a public opinion to this end in a sandbox report. (p. 22)[^original]  
  <sub>anchor: "most appropriate lawful basis was likely ‘legitimate interest’ (Article 6.1(f) of the GDPR"</sub>
- **descriptive / finding or result**: Participants also explored 'compliance with a legal obligation' (Article 6.1(c) GDPR) for sharing and analysing pseudonymised data, but it was unlikely that sharing data on the broad account base before any firm indication of suspicious activity (pre-suspicion) would be seen as a reasonable and proportionate way of complying with the specific legal obligation. Participants felt this basis may be more appropriate for further sharing to support investigations alerted by the platform, limited to accounts subject to an identified suspicion. (p. 22)[^original]  
  <sub>anchor: "it was unlikely that sharing of data on the broad underlying account base, prior to any firm indication"</sub>
- **descriptive / finding or result**: Proportionality in TriBank: data related only to small to medium enterprises (legal persons) and was pseudonymised; clusters, once identified, could be re-identified only by the specific banks that submitted the data. Banks would properly investigate reports before suspects experienced any change in service level, i.e. services are not removed purely on a finding by the common platform. (p. 23)[^original]  
  <sub>anchor: "suspects do not have their banking services removed purely on the basis of a finding/report by the common platform"</sub>
- **descriptive / method**: Technologies in TriBank: a sample of transactional data was pseudonymised using a hashing convention and placed in a common platform (AML utility), which cleaned and de-duplicated the pooled dataset and applied analytics algorithms to map complex non-linear cross-bank account relationships to identify potential 'pre-suspicions' for individual banks to investigate. (p. 23)[^original]  
  <sub>anchor: "pseudonymised using a hashing convention and placed in a common platform (AML utility)"</sub>
- **descriptive / case example**: The ICO, though not involved in the TriBank pilot itself, worked with FutureFlow in the sandbox to assess data protection risks and mitigations through a data protection impact assessment (DPIA), and issued a public opinion on the basis for processing. (p. 23)[^original]  
  <sub>anchor: "had worked with FutureFlow (the technology provider and data processor) as part of the sandbox environment"</sub>
- **descriptive / finding or result**: TriBank results: without knowledge of the underlying transacting accounts, large and complex clusters could be identified automatically and brought forward for further analysis. However, after bank investigations these clusters were explainable in a number of cases, suggesting analysis of pseudonymised transaction data alone is unlikely to deliver the information needed to detect ML, or that further work is required to integrate known ML typologies or other intelligence feeds to pinpoint suspicious clusters. (p. 23)[^original]  
  <sub>anchor: "analysis of pseudonymised transaction data alone is unlikely to be able to deliver the required information for detecting ML"</sub>
- **descriptive / method**: The technology provider envisaged a two-tier DPP framework: a first phase on legitimate interest with bulk pseudonymised data (protecting privacy of most customers not implicated), and, once a typology, cluster, abnormal activity or pre-suspicion forms, further sharing of individual account information based on compliance with law (to investigate and submit STRs, or a legal gateway in AML/CFT/CPF legislation). (p. 23)[^original]  
  <sub>anchor: "The technology provider envisaged an operating model with a two-tier DPP framework."</sub>
- **descriptive / definition**: Box 4.1 notes: the GDPR defines a data processor as a person that processes personal data on behalf of a controller (art. 4(8)); a regulatory sandbox lets firms test innovations in live but generally limited, time-bound experiments in a controlled environment under regulator supervision; TriBank was conducted after, not within, the sandbox testing, which concluded in November 2020 when the UK was still subject to the GDPR (UK law equivalent article 6.1(f) UK GDPR). A DPIA is required where an initiative is likely to involve a high risk to individuals' rights and freedoms (GDPR/UK GDPR art. 35). (p. 24)[^original]  
  <sub>anchor: "A DPIA is required where an initiative is likely to involve"</sub>

## Box 4.2. COSMIC (Singapore)

- **descriptive / case example**: Box 4.2 (Singapore, COSMIC): a secure digital platform owned and operated by the Monetary Authority of Singapore (MAS) for risk discovery and data analytics collaboration, pre-STR and post-STR. Participating FIs will share customer information to assess suspicion and warn each other of potentially suspicious activity where a customer's profile or behaviour crosses materiality 'red flag' tests in priority risk areas; shared information includes risk analysis, customer or transaction data. Sharing will initially be permissive/voluntary, with MAS planning to make it mandatory in higher-risk situations after an initial stabilisation phase. (p. 24)[^original]  
  <sub>anchor: "MAS plans to make sharing mandatory in higher-risk situations after an initial phase"</sub>
- **descriptive / finding or result**: Currently Singapore FIs are not permitted to warn each other about potentially suspicious customer activity or share customer information indiscriminately, due to information security and privacy concerns; criminals exploit this by transacting through networks of entities with accounts at different FIs, so each FI alone lacks enough information. Sharing information on customers that cross material risk thresholds of strong probative value is intended to break down silos, enhance detection of illicit networks, increase disruption in priority risk areas and support cross-border disruption and deterrence. (p. 24)[^original]  
  <sub>anchor: "Criminals have been able to exploit this weakness by conducting transactions through a network of entities"</sub>
- **descriptive / case example**: COSMIC participants: MAS co-develops COSMIC with the Commercial Affairs Department (CAD) of the Singapore Police Force and six major banks as initial users, and worked closely with the Personal Data Protection Commission (PDPC) so sharing aligns with PDPC principles. Participants are discussing key performance indicators to measure success. As AML supervisor MAS will integrate platform data with its supervisory surveillance and ensure appropriate use; the Suspicious Transaction Office (STRO), Singapore's FIU, will have direct access and use the information for its own analytics. (p. 25)[^original]  
  <sub>anchor: "COSMIC project participants are discussing specific key performance indicators to measure the project’s success."</sub>
- **descriptive / method**: COSMIC modes of sharing: where a customer exhibits red flag behaviour and an FI needs more risk information to assess suspicion, it may request risk information from other FIs linked to the activity (Request); where unusual activity crosses a higher risk threshold, an FI would have to proactively provide risk information to other FIs linked to the customer's activities (Provide); where the higher threshold of red flags is met and the FI has filed an STR and decided to terminate the relationship, the FI should place an Alert on the customer on the COSMIC 'watchlist'. (p. 25)[^original]  
  <sub>anchor: "the FI should place an Alert on this customer on the “watchlist” in COSMIC"</sub>
- **descriptive / context**: In the initial phase sharing on COSMIC via Request, Provide and Alert will be non-mandatory; thereafter MAS expects sharing via Provide and Alert to be mandatory, and it will also be mandatory for participating FIs to respond to Request messages after the initial phase. (p. 25)[^original]  
  <sub>anchor: "In the initial phase, sharing information on COSMIC via Request, Provide and Alert will be non-mandatory."</sub>
- **descriptive / finding or result**: Lawful basis for COSMIC: the Personal Data Protection Act (PDPA) provides a legislative route for other written law to prevail over PDPA requirements. MAS is amending the Financial Services and Markets Act to set out a COSMIC regulatory framework for risk information sharing between FIs for AML/CFT/CPF purposes, permitted only between FIs participating in COSMIC and within the prescribed modes of Request, Provide and Alert. (p. 25)[^original]  
  <sub>anchor: "MAS is making legislative amendments to the Financial Services and Markets Act to set out a regulatory framework for COSMIC"</sub>
- **descriptive / data or feature**: COSMIC data points: risk analysis, transaction and customer information, e.g. particulars of directors, authorised signatories or beneficial owners (name, date of incorporation or birth, residential and/or business address, nationality or place of incorporation, unique identification number), plus transaction data or other red flag information. Participating FIs are required to use pre-defined data templates covering case and FI identifiers; red flags and risk description; customer profile; account profile (type, status, open/closure date); transactional details (originating and beneficiary names, account numbers, FIs, date, amount, currency); and details of customers placed on an alert list and reasons. (p. 25)[^original]  
  <sub>anchor: "Participating FIs are required to share information using pre-defined data templates."</sub>
- **descriptive / finding or result**: COSMIC proportionality: sharing initially targets three priority risk areas identified through the national risk assessment and AML/CFT/CPF strategies: misuse of legal persons, trade-based money laundering and proliferation financing. For sharing to occur, a customer's behaviour or profile must exhibit multiple red flags or indicators of sufficient materiality and be probative of financial crime concerns. (p. 26)[^original]  
  <sub>anchor: "misuse of legal persons, trade-based money laundering and proliferation financing"</sub>
- **descriptive / finding or result**: Because COSMIC aims to assess suspicion and warn other FIs, notifying the customer that their information is shared could tip off criminals; to protect legitimate customers COSMIC has several layers of safeguards. (p. 26)[^original]  
  <sub>anchor: "notifying the customer that their information is being shared could lead to criminals being tipped off"</sub>
- **mandatory / requirement**: COSMIC safeguard one: an FI must assess whether the customer has crossed the stipulated materiality risk tests, based on probative combinations of red flags, before initiating sharing; an FI responding to a request will also be required to assess and be satisfied that the requested information may assist in assessing and determining ML/TF/PF risk before sharing it. (p. 26)[^original]  
  <sub>anchor: "FI must assess whether the customer has crossed the stipulated materiality risk tests"</sub>
- **mandatory / requirement**: Under Singapore's planned COSMIC arrangements, FIs will be required to put in place a process for reviewing customer relationships, including giving the customer an adequate opportunity to address its concerns before the relationship is exited. (p. 26)[^original]  
  <sub>anchor: "FIs will also be required to put in place a process for reviewing customer relationships"</sub>
- **expected / expectation**: FIs should not rely solely on information received from COSMIC, but should review the customer relationship holistically, taking into account other sources of information including the customer's explanation, before deciding whether to exit the relationship. (p. 26)[^original]  
  <sub>anchor: "FIs should not rely solely on the information received from COSMIC"</sub>
- **descriptive / context**: Customers already have pre-existing legal channels to correct customer information that FIs collect from them, such as identity information; this avenue remains available with the customer's bank and the correction is updated into COSMIC. (p. 26)[^original]  
  <sub>anchor: "Customers already have pre-existing channels, provided in law, to correct customer information"</sub>
- **expected / expectation**: COSMIC-related data should be stored in a secure environment with appropriate encryption, and COSMIC data should not be stored on individuals' laptops unless exceptionally warranted. (p. 26)[^original]  
  <sub>anchor: "COSMIC data should not be stored on individuals’ laptops unless exceptionally warranted."</sub>
- **mandatory / requirement**: Audit logs will be required for any viewing, editing or downloading of information involving sensitive data in the COSMIC context. (p. 26)[^original]  
  <sub>anchor: "Audit logs will be required for any viewing, editing or downloading of information involving sensitive data."</sub>
- **mandatory / requirement**: COSMIC safeguard two: the legislative framework will prescribe safeguards on the use and confidentiality of platform information and require FIs to guard against inappropriate sharing; require that information disclosed is accurate and complete; and require FIs to promptly notify MAS and relevant participant FIs of any error and rectify it as soon as possible. (p. 27)[^original]  
  <sub>anchor: "prescribe safeguards on the use and confidentiality of information obtained from the platform"</sub>
- **mandatory / requirement**: COSMIC data transfers: FIs and their officers will not be permitted to disclose COSMIC information to anyone else except as expressly provided in legislation; any further disclosure must be relevant, proportionate and necessary for assessing ML/TF/PF risk, for example for operational purposes, outsourcing of risk management functions, or to local and overseas affiliates for group-wide risk management. Disclosure to prescribed persons will require additional safeguards against leakage, unauthorised disclosure and unintended legal risk to the sharing FI. (p. 27)[^original]  
  <sub>anchor: "FIs and their officers will not be permitted to disclose information obtained from COSMIC to any other person"</sub>
- **expected / expectation**: COSMIC confidentiality/data security: participating FIs should appropriately classify COSMIC-related data and implement info-security measures to prevent leakage, as a baseline complying with MAS Technology Risk Management Guidelines (industry best practices) and Notices on Technology Risk Management and Cyber Hygiene (required IT controls and cyber hygiene). (p. 27)[^original]  
  <sub>anchor: "Participating FIs should appropriately classify COSMIC-related data and implement info-security measures"</sub>
- **descriptive / method**: COSMIC technologies: information is shared in a structured format on an online platform with user-authentication and data encryption plus entity resolution and network link analysis; MAS will use COSMIC information within its broader AML/CFT/CPF analytics surveillance framework to identify illicit networks and emerging trends. (p. 27)[^original]  
  <sub>anchor: "entity resolution and network linked analysis"</sub>
- **descriptive / limitation**: MAS recognises that strengthening collaboration among an initial group of banks may lead illicit actors to shift activity to FIs not on COSMIC ('risk migration'); MAS is strengthening surveillance to uncover such scenarios, stepping up supervisory engagement with non-COSMIC FIs to warn them and guide tighter controls, and will keep collaborating with FIs through the AML/CFT/CPF Industry Partnership (ACIP), involving non-COSMIC FIs in priority ML/TF investigations where warranted. (p. 28)[^original]  
  <sub>anchor: "may raise the risk of illicit actors shifting their activities to FIs that do not participate on COSMIC"</sub>

## Box 4.3. Transaction Monitoring Netherlands (TMNL)

- **descriptive / case example**: Box 4.3 (Netherlands, TMNL): Transactie Monitoring Nederland is a pre-suspicion private-to-private initiative of five Dutch banks aiming at faster, better, more effective transaction monitoring and enhancing banks' 'gatekeeper' role; the long-term ambition is an industry-wide transaction monitoring utility for better ML/TF detection and higher quality information to law enforcement. Founded July 2020, it operates in the 'Minimal Viable Product' (MVP) stage aiming to identify unusual patterns individual banks cannot (so-called 'multibank alerts'). (p. 28)[^original]  
  <sub>anchor: "to ultimately create an industry- wide utility for transaction monitoring"</sub>
- **descriptive / data or feature**: In the MVP stage: all TMNL activities are on top of regular AML/CTF procedures of the founding banks; focus is multibank monitoring of patterns spanning accounts at several banks; TMNL is a detection utility only, with all alert review and client measures (including filing Unusual Transaction Reports with the FIU) done by banks; client scope is business entities only; and privacy-sensitive data items are pseudonymised. (p. 28)[^original]  
  <sub>anchor: "TMNL is in the MVP stage a detection utility only, all alert review and client measures"</sub>
- **descriptive / method**: TMNL process: banks transfer pseudonymised transaction data to TMNL; its analytical models generate alerts on potential unusual patterns; the entities in a pattern ('case') are alerted to the banks for review, which happens within the bank environment because the client information required is available only there. (p. 29)[^original]  
  <sub>anchor: "banks transfer pseudonymised transaction data to TMNL"</sub>
- **descriptive / finding or result**: TMNL aims to identify illicit money flows and patterns spanning multiple banks that individual banks cannot uncover in isolation, on the presumption that money laundering organisations deliberately and increasingly create complex schemes across a web of banks and accounts. Initial testing in a Proof of Concept and the first alerts from several advanced analytics models confirmed numerous multibank cases, a subset of which banks reported to the FIU. (p. 29)[^original]  
  <sub>anchor: "confirmed that numerous of such multibank cases were found of which a subset has been reported by the banks to the FIU"</sub>
- **descriptive / case example**: TMNL participants: five Dutch banks (ABN Amro, ING Bank, Rabobank, Triodos Bank and De Volksbank), all shareholders of the TMNL legal entity, formally a fully private initiative; in practice the banks work with government partners on strategic and regulatory matters and align with law enforcement on AML intelligence and typologies translated into analytical models detecting multibank patterns. (p. 29)[^original]  
  <sub>anchor: "formally a fully private initiative"</sub>
- **descriptive / method**: TMNL mode of sharing: banks prepare transaction data in their own environment, pseudonymising all data items that could directly or indirectly relate to individual entities; TMNL pools and relates participating banks' data in analytical models on a highly secured IT platform. Alerts returned include a specific ID that only the receiving bank can relate to its own client records, and this translation must be done at the bank before investigators review the alert. (p. 29)[^original]  
  <sub>anchor: "The alerts sent back to banks include a specific ID that only the respective receiving bank can relate back"</sub>
- **descriptive / data or feature**: TMNL data scope is restricted to business entities and to what is required for its objectives and possible under current legal frameworks: transaction information (account number, transaction type, amount) and limited account and client information (IDs, account and client type, client industry). Because of the pseudonymisation scheme TMNL cannot identify individual clients in the banks' datasets and can only alert banks on multibank transaction patterns. (p. 29)[^original]  
  <sub>anchor: "TMNL cannot identify individual clients in the datasets of the banks"</sub>
- **descriptive / method**: TMNL privacy measures: the banks and TMNL assume some data could be personal data, so TMNL treats all data as personal data. Key technique is pseudonymisation, in which items that could relate to individual clients (IDs, account numbers, names) are transformed into hashed values using a set of private keys preserved by a third party and in secured modules during data preparation. Because the secret keys are common across banks, TMNL can still interrelate data items common across banks (e.g. a client's chamber of commerce number and account number) without knowing client identity. (p. 30)[^original]  
  <sub>anchor: "Since the secret keys are common across banks, transaction data can still be interrelated by TMNL"</sub>
- **descriptive / finding or result**: Lawful basis for TMNL: the Dutch Ministries of Finance and Justice are working on an amendment to the Dutch AML/CTF Act, part of the National Action Plan against Money Laundering, which seeks to let banks share more transaction data and information on presumed unusual transactions, lift the ban on outsourcing transaction monitoring, and allow use of the Civil Service Number in collective monitoring. In anticipation, TMNL started with a limited client scope on the basis of legitimate interest, after extensive legal analysis of how processing fits within the pre-amendment legal framework. (p. 30)[^original]  
  <sub>anchor: "TMNL has started with a limited scope of clients based on legitimate interest"</sub>

---

[previous part](digest-002.md) | [source overview](overview.md) | [next part](digest-004.md)

[^original]: Financial Action Task Force, "Partnering in the Fight Against Financial Crime: Data Protection, Technology and Private Sector Information Sharing" (2022-07). https://www.fatf-gafi.org/en/publications/Digitaltransformation/Partnering-in-the-fight-against-financial-crime.html
