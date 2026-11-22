---
type: Source Digest
title: Illicit Financial Flows from Cyber-Enabled Fraud - part 3 of 6 (pp. 28-41)
description: 'Verified paraphrased digest, pp. 28-41: 2. Risk environment: Cyber-enabled Fraud; 3. Other emerging ML vulnerabilities; 4. National operational responses and strategies'
resource: https://egmontgroup.org/wp-content/uploads/2023/11/Final_Illicit-financial-flows-from-cyber-enabled-fraud.pdf
tags:
- emerging_threats
- empirical_observation
- fraud_screening_synergies
- intl
- typologies
- typology_report
- virtual_assets
status: stable
source_id: egmont-illicit-financial-flows-from-cyber-enabled-fraud
issuer: egmont
issuer_name: Egmont Group of FIUs
jurisdictions:
- INTL
tier: 2
instrument_type: typology_report
normative_force: empirical_observation
publication_date: 2023-11
legal_status: current
part: 3
parts_total: 6
content_mode: digest
generated:
  by: claude-code-subagent/claude-sonnet-5-5
  at: '2026-11-22T04:52:43Z'
verified:
- by: process:kb-digest-check/anchor-match
  at: '2026-11-22T04:52:43Z'
- by: claude-code-judge-agent/claude-opus-5-5
  at: '2026-11-22T04:52:43Z'
sources:
- id: original
  resource: https://egmontgroup.org/wp-content/uploads/2023/11/Final_Illicit-financial-flows-from-cyber-enabled-fraud.pdf
  title: Illicit Financial Flows from Cyber-Enabled Fraud
  author: org:egmont
digest_points: 50
---

# Illicit Financial Flows from Cyber-Enabled Fraud (digest)

[previous part](digest-002.md) | [source overview](overview.md) | [next part](digest-004.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (pp. 28-41) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **empirical observation**.

## 2. Risk environment: Cyber-enabled Fraud

- **descriptive / case example**: Case from Austria: in a series of phishing-related frauds, criminals tricked victims into installing remote access tools on their computers. In many cases accounts were opened with VASPs in the victim's name without their knowledge, using data stolen through those tools, and the criminals are suspected to have used the tools to guide victims through online account verification while hiding the real interfaces. (p. 28)[^original]  
  <sub>anchor: "In many of the cases, accounts were created with VASPs in the victim’s name, without their knowledge."</sub>
- **descriptive / case example**: In the same Austrian series, victims were finally tricked into sending funds to these VASP accounts, which the criminals could directly use for subsequent laundering; victims were estimated to have lost over EUR 600 000 in total. (p. 28)[^original]  
  <sub>anchor: "victims were estimated to have lost over EUR 600 000 through this series."</sub>

## 3. Other emerging ML vulnerabilities

- **descriptive / context**: The preventive measures required of FIs, DNFBPs and VASPs under the FATF Standards (Recommendations 9 to 23) provide a foundation to stop CEF proceeds entering the financial and other sectors; the section focuses on emerging ML vulnerabilities CEF syndicates could exploit. (p. 29)[^original]  
  <sub>anchor: "provide a foundation to prevent CEF proceeds from entering the financial and other sectors"</sub>

## 3.1. Risks arising from digital financial institutions

- **descriptive / finding or result**: New digital financial institutions such as payment service providers (PSPs) and e-money issuers have emerged; traditional FIs may have more resources and relatively more robust controls, which may lead to displacement, where criminals exploit vulnerabilities in these alternative providers to launder funds. (p. 29)[^original]  
  <sub>anchor: "This may lead to displacement, where criminals seek to exploit vulnerabilities"</sub>
- **descriptive / finding or result**: The payments network can be fragmented, with nested relationships (payment institutions transacting with one another or providing accounts to smaller providers who offer other services), which intensifies difficulty tracing transactions across the payment chain and may challenge ensuring immediate availability of basic originator and beneficiary information. Footnote 17 notes the FATF is considering revisions to Recommendation 16 (wire transfers) for payment system architecture developments. (p. 29)[^original]  
  <sub>anchor: "This fragmentation can also intensify the difficulties in tracing transactions across various types of institutions"</sub>
- **expected / expectation**: In line with FATF Standards there should be robust regulatory supervision over newer financial institutions, including proper licensing or registration and preventing criminals or associates from controlling them. Regulatory authorities should ensure all transacting institutions have sufficient oversight over their respective perimeter; all institutions have a responsibility to conduct or ensure proper CDD and transaction monitoring on the ordering and beneficiary nodes. (p. 29)[^original]  
  <sub>anchor: "there should be robust regulatory supervision over newer financial institutions"</sub>

## Box 17. PSP sector abuse

- **descriptive / case example**: Box 17 (France): French supervisory analysis in the first half of 2021 identified the main PSPs used to receive fraudulent wire transfers; they typically offered 'banking as a service', some with a branch in France solely to offer French IBANs with minimal physical presence. They were found to be approximately 200 times more risky than other institutions, and most had poor identity verification and transaction monitoring. (p. 30)[^original]  
  <sub>anchor: "these main PSPs were approximately 200 times more risky than other institutions"</sub>
- **descriptive / typology or red flag**: Box 17 continued: criminals opened accounts with misused identities and quickly checked whether accounts had been flagged as fraudulent by trying small transactions first and changing the destination if needed, then moved fraudulent funds quickly to one or several accounts; splitting amounts between accounts lets them circumvent PSP restrictions such as cash withdrawal limits or stay under internally defined monitoring thresholds. (p. 31)[^original]  
  <sub>anchor: "Splitting the amounts between several accounts enables criminals to circumvent restrictions"</sub>

## 3.2. Virtual IBAN abuse

- **descriptive / finding or result**: Virtual IBANs (vIBANs) are issued to clients by various institutions including banks and PSPs; while used legitimately (e.g. to facilitate and categorise payments from multiple parties), several jurisdictions flagged vIBAN abuse as a tool for CEF-related ML. (p. 31)[^original]  
  <sub>anchor: "several jurisdictions have flagged the abuse of vIBANs as a tool used for CEF-related ML"</sub>

## Box 18. What is a vIBAN?

- **descriptive / definition**: Box 18 (Europol Financial Intelligence PPP): vIBANs function and look identically to conventional IBANs, composed of up to 34 alphanumeric characters, so they are indistinguishable from regular IBANs. A regular IBAN matches 1:1 with a physical bank account; a virtual IBAN is a bank-issued reference number not matched to an account that reroutes incoming payments to a physical IBAN, cannot hold funds and always has a zero balance, and a holder can have several vIBANs that centralise payments into a single physical account. (p. 31)[^original]  
  <sub>anchor: "A regular IBAN is matched 1:1 with a bank account"</sub>

## 3.2. Virtual IBAN abuse

- **descriptive / typology or red flag**: Because IBANs and vIBANs look identical, criminals can trick victims into thinking they are paying a bank account when it may be a vIBAN used, for example, to credit an e-wallet. vIBANs can be reissued by a financial institution's client, particularly another financial institution (Figure 2 shows a cascading net of vIBAN providers issuing and re-issuing vIBANs), making it hard to identify the country of origin of the vIBAN and the location of the master account. (p. 31)[^original]  
  <sub>anchor: "vIBANs can be reissued by a financial institution’s client, particularly if the client is another financial institution"</sub>
- **descriptive / finding or result**: Criminals can abuse vIBANs to mask ultimate beneficial ownership and obscure movement of illicit money, making it difficult to identify the true master account, the issuing FI and proper transaction monitoring, and hindering authorities in locating physical accounts and freezing funds since vIBANs are only reference numbers. As a good practice, some jurisdictions worked with vIBAN-issuing banks to quickly identify the payment institution linked to master accounts once CEF is identified. (p. 33)[^original]  
  <sub>anchor: "some jurisdictions have worked with banks issuing vIBANs to quickly identify the payment institution"</sub>

## Box 19. vIBANs abused for CEF

- **descriptive / case example**: Box 19 (Luxembourg): between February and March 2023 FIU Luxembourg received reports of 'Hi Mum' scams, where victims got WhatsApp messages from a local number from fraudsters pretending to be their child, with a Luxembourg IBAN included. The IBANs were vIBANs issued by a Luxembourg bank to a Luxembourg PSP offering prepaid cards to European customers, which can be loaded by transfers to the vIBANs, intended for further laundering. (p. 33)[^original]  
  <sub>anchor: "so-called “Hi Mum” Scams, where victims received WhatsApp messages"</sub>
- **descriptive / case example**: Box 19 result: of six identified vIBANs used in the scam, FIU Luxembourg blocked or recalled EUR 40 000 of EUR 55 000 defrauded, helped by FIU co-operation with the issuing bank, which quickly identified the payment institution holding the end customer's underlying account. (p. 33)[^original]  
  <sub>anchor: "FIU Luxembourg was able to block or recall EUR 40 000 out of EUR 55 000 defrauded funds"</sub>

## 3.3. Non-traditional sectors

- **descriptive / finding or result**: Many jurisdictions highlighted working with non-traditional sectors (social media platforms, e-commerce, telecommunication and internet service providers) against CEF-related ML. Though not regulated for AML/CFT, they hold useful information, especially when used for CEF and mule recruitment: social media, telecom and ISPs can give digital forensic information (IP addresses, phone numbers, email addresses) to identify perpetrators, and where fraudulent websites or advertisements are used they hold related payment information (e.g. payment details for website hosting, advertisements). (p. 33)[^original]  
  <sub>anchor: "While these nontraditional sectors are not regulated for AML/CFT, they possess useful information"</sub>
- **descriptive / typology or red flag**: E-commerce, social media, streaming or gaming platforms can be abused as a conduit to launder CEF proceeds: their wide use lets users receive donations, gifts, tokens or credits from viewers and the public, and criminals may exploit the absence of AML/CFT requirements to launder proceeds. (p. 34)[^original]  
  <sub>anchor: "Criminals may take advantage of the absence of AML/CFT requirements"</sub>

## Box 20. Phishing proceeds laundered through social media and streaming platform

- **descriptive / case example**: Box 20 (Germany): nineteen bank accounts suffered losses in a phishing attack on certain banks' customers; German FIU analysis showed transactions went through payment accounts owned by two users and then to a social media and streaming platform, where funds recharged user accounts with 'coins' that buy virtual gifts transferable to content creators who convert coins to regular currency and withdraw it. IP data showed the fraudulent transactions used the same login IP addresses, suggesting a common criminal laundering large parts of the proceeds through the platform to cash out later; investigations are ongoing. (p. 34)[^original]  
  <sub>anchor: "These funds were subsequently sent to a social media and streaming platform."</sub>

## 4. National operational responses and strategies

- **descriptive / context**: Chapter 4 covers key information sources jurisdictions rely on to detect and investigate CEF, then domestic co-ordination and cooperation structures and how they are used to investigate and prevent CEF and related ML. (p. 35)[^original]  
  <sub>anchor: "This Chapter first discusses key sources of information that jurisdictions rely on to detect and investigate CEF."</sub>

## 4.1. Key sources of detection

- **descriptive / finding or result**: There are two primary information sources for detecting and investigating CEF-related ML: victim reporting and suspicious transaction reports (STRs). Jurisdictions also run initiatives to enhance reporting, and competent authorities use digital strategies and tools to analyse and identify criminal clusters for more targeted enforcement. (p. 35)[^original]  
  <sub>anchor: "there are two primary sources of information for detecting and investigating CEF-related ML"</sub>

## Victim reporting

- **descriptive / finding or result**: In frauds such as BEC and phishing, victims usually discover relatively quickly they have been defrauded (e.g. a legitimate counterparty asks for missed payments); in other CEF such as investment scams, romance fraud or phishing, victims may realise only after some time. (p. 35)[^original]  
  <sub>anchor: "victims usually discover relatively quickly that they have been defrauded"</sub>
- **descriptive / finding or result**: Timely victim reporting lets authorities act quickly to trace proceeds and may raise the likelihood of successful enforcement. Victims may report to law enforcement (including dedicated fraud units), notify their FIs, payments providers and VASPs, or, in some jurisdictions, approach financial consumer protection bodies instead of law enforcement. (p. 35)[^original]  
  <sub>anchor: "Timely victim reporting is important to enable competent authorities to act quickly to trace illicit proceeds"</sub>
- **descriptive / limitation**: CEF is likely under-reported, especially where victims suffered negligible loss, and emotional factors such as embarrassment or fear may deter victims from coming forward. (p. 36)[^original]  
  <sub>anchor: "CEF is likely under-reported by victims, especially where they had only suffered negligible loss"</sub>
- **descriptive / recommendation**: As a good practice to increase victim reporting, some jurisdictions created dedicated reporting platforms including online portals; these can offer a structured reporting format to standardise data capture, facilitating cluster analysis of victim reports and identification of trends and patterns, and can include CEF prevention and victim assistance resources. (p. 36)[^original]  
  <sub>anchor: "some jurisdictions have created dedicated platforms for victims to report CEF, including online portals"</sub>

## Box 21. United Kingdom Action Fraud

- **descriptive / case example**: Box 21 (United Kingdom): Action Fraud is the national report centre for fraud and cybercrime, run by the City of London Police with the National Fraud Intelligence Bureau (NFIB), offering public outreach and victim support and a 24/7 online reporting portal. Reports go to the NFIB, which assesses and analyses them nationally to identify ultimate perpetrators and sends them to local police forces; the NFIB also uses reports to take down bank accounts, websites and phone numbers used by fraudsters. (p. 36)[^original]  
  <sub>anchor: "The NFIB also uses these reports to take down bank accounts, websites and phone numbers used by fraudsters."</sub>

## Suspicious Transaction Reports

- **descriptive / finding or result**: Because victims may under-report, STRs are described as a vital independent source for detecting CEF-related financial flows. (p. 36)[^original]  
  <sub>anchor: "STRs are a vital independent source of detection for CEF-related financial flows."</sub>
- **descriptive / finding or result**: Data gathered from FIUs showed that most CEF-related STRs were filed by the banking sector, while MVTS and VASPs submit fewer STRs; the latter could be because in some jurisdictions the VASP sector is not fully regulated in line with the FATF Standards. (p. 36)[^original]  
  <sub>anchor: "most CEF-related STRs were filed by the banking sector"</sub>
- **expected / expectation**: The report says banks should continue to strengthen their capabilities to detect CEF and related ML, because CEF syndicates continuously evolve their modus operandi. (p. 36)[^original]  
  <sub>anchor: "banks should continue to strengthen their capabilities to detect CEF and related ML"</sub>
- **expected / recommendation**: It is important to ensure timely analysis of CEF-related STRs given possible dissipation of proceeds. Some FIUs use prioritisation systems to focus on higher-risk STRs (including CEF-related), and others train FIU officers on CEF ML risks to screen and categorise incoming CEF STRs, facilitating timely analysis and swift law enforcement follow-up. (p. 37)[^original]  
  <sub>anchor: "It is important to ensure a timely analysis of CEF-related STRs, given the possible dissipation"</sub>

## Box 22. Prioritisation and clustering of CEF-related STRs

- **descriptive / case example**: Box 22 (Chile): FIU Chile received more than 1,500 STRs from 2021 to 2022 on an online trading platform fraud scheme and applied clustering techniques, finding patterns across them. It used a text mining tool with key words and known phrases, identified geographical clusters allowing a targeted combined referral to the Public Prosecutor's Office, and found funds were withdrawn via ATMs and passed to a higher-hierarchy person in the group. (p. 37)[^original]  
  <sub>anchor: "FIU Chile received more than 1,500 STRs from 2021 to 2022"</sub>

## Suspicious Transaction Reports

- **descriptive / finding or result**: Beyond detection, many jurisdictions issued CEF-related guidelines or educational seminars for bank and other sector personnel on latest CEF trends and ML typologies, and some FIUs developed strategic analysis papers on CEF; Annex A compiles risk indicators to help detection. These aim to improve detection and prevention by frontline bank staff and others. (p. 37)[^original]  
  <sub>anchor: "Many jurisdictions have issued some form of CEF-related guidelines or organised educational seminars"</sub>

## Co-ordination amongst competent authorities

- **expected / expectation**: Given the cross-cutting nature of CEF, the report identifies a clear need for strong domestic coordination across agencies. (p. 37)[^original]  
  <sub>anchor: "there is a clear need for strong domestic coordination across agencies"</sub>
- **descriptive / finding or result**: Some jurisdictions coordinate through a whole-of-government strategic approach guiding their CEF-related policies, using an overarching cross-functional body made up of key ministries from the judicial, enforcement, regulatory and info-communications sectors; this lets them identify key vulnerabilities and devise holistic policy responses across the key sectors. (p. 37)[^original]  
  <sub>anchor: "Some jurisdictions have approached co-ordination through a whole-of-government strategic approach"</sub>

## Box 23. Strategic analysis on CEF-related mules

- **descriptive / case example**: Box 23 (Spain): the Spanish FIU's strategic analysis profiled money mules as bank accounts opened by a single individual at three or more financial institutions within 20 days. Using Bank Account Registry (BAR) data from December 2020 to February 2022, it found nearly 40 000 other accounts linked to about 10 000 individuals; 15% of the accounts had hits in FIU databases, were classed high risk, and led to a pilot with four financial institutions. (p. 38)[^original]  
  <sub>anchor: "bank accounts opened by a single individual at three or more financial institutions within 20 days"</sub>
- **descriptive / case example**: Box 23 continued: the pilot aimed to prevent CEF and other fraud, improve co-operation with the private sector, help financial institutions detect gaps in their systems and gain further CEF information; it resulted in a cross-checking system leveraging the BAR to proactively detect CEF-related ML networks. (p. 38)[^original]  
  <sub>anchor: "implementation of a cross-checking system leveraging the BAR to proactively detect CEFrelated ML networks"</sub>

## Co-ordination amongst competent authorities

- **descriptive / finding or result**: Operational co-ordination can involve technical agencies, including developing communication channels among FIUs, police and prosecutors for centralised reporting, streamlined information and evidence exchange and freeze/seize instructions (possibly with automated data triage to spot matters of interest and find the appropriate LEA), which also mitigates duplicated law enforcement effort as CEF criminals can target victims across a jurisdiction. (p. 38)[^original]  
  <sub>anchor: "Developing communication channels among FIUs, police, and prosecutors to ensure centralised reporting"</sub>
- **descriptive / finding or result**: Operational co-ordination can also involve leveraging technical cybercrime experts, particularly on network intrusions and technical infrastructure crimes, as well as privacy protection agencies, reflecting CEF's multi-faceted nature and the relevance of digital forensic evidence (IP addresses, identifiers linked to internet domains) in identifying syndicates and furthering ML investigations. (p. 39)[^original]  
  <sub>anchor: "Leveraging technical cybercrime experts, particularly relating to network intrusions"</sub>

## Box 24. Joint Policing Cybercrime Co-ordination Centre

- **descriptive / case example**: Box 24 (Australia): the AFP-led Joint Policing Cybercrime Coordination Centre (JPC3) includes federal and state law enforcement, government analysts including AUSTRAC, and industry partners such as bank analysts. It coordinates the policing response to high harm high volume cybercrime; enhances intelligence sharing and target development; coordinates joint taskforces; provides national coordination of capability uplift via cross skilling, joint training and collaborative tool development; and communicates nationally consistent prevention, awareness and media activities. AUSTRAC has a financial cybercrime team providing financial intelligence on cyber-enabled and cyber-dependent crime with a financial nexus. (p. 39)[^original]  
  <sub>anchor: "Coordinates Australia’s policing response to high harm high volume cybercrime"</sub>
- **descriptive / case example**: Box 24 continued: in January 2020 the AFP established Operation DOLOS, a multi-agency taskforce (state and territory police, intelligence and cyber-security agencies, the FIU and the financial sector) countering transnational cybercriminals conducting or facilitating BEC; it works with Australians and small to medium businesses targeted by BEC and disrupts proceeds flows, and between 1 July 2022 and 30 June 2023 it prevented more than AUD30.6 million being lost from Australian and international victims. (p. 39)[^original]  
  <sub>anchor: "Operation DOLOS has prevented more than AUD30.6million from being lost"</sub>

## Operational partnerships with the private sector

- **descriptive / finding or result**: Jurisdictions collaborate with the private sector through public-private partnerships (PPPs), which can improve detection, identify hidden ML networks through tactical information exchange and enhance operational asset recovery response. (p. 39)[^original]  
  <sub>anchor: "These PPPs can help improve detection efforts, identify hidden ML networks through tactical information exchange"</sub>
- **descriptive / finding or result**: Given the noticeable rise of CEF and its associated ML risk, many jurisdictions have set up centralised response centres within LEAs or regulators to step up action against CEF and raise public awareness. (p. 39)[^original]  
  <sub>anchor: "many jurisdictions have established centralised response centres in LEAs or regulators"</sub>
- **permissive / recommendation**: The report presents it as a good practice that representatives of FIs and VASPs could be based inside such centralised response centres, giving near-real-time access to financial data and tracing across financial entities and sectors, and speeding up the competent authorities' ability to intercept and freeze funds. (p. 39)[^original]  
  <sub>anchor: "representatives of FIs and VASPs could be co-located within such centralised response centres"</sub>

## Box 25. Project: Rapid Actions to Prevent Scams

- **descriptive / case example**: Box 25 (Sri Lanka): FIU Sri Lanka's Rapid Actions to Prevent Scams (RAPS) project acts immediately once a victim reports potential CEF, bringing the FIU and FI compliance officers together to detect illicit account activity rapidly. Scammer credentials identified from public complaints are shared with FI compliance officers, who monitor accounts and act to disrupt fraud, and the information is also shared with Sri Lanka Police for investigation. (p. 40)[^original]  
  <sub>anchor: "to act immediately once a victim reports potential CEF"</sub>

## Box 26. Co-location of bank officers

- **descriptive / case example**: Box 26 (Saudi Arabia): a Joint Operations Room (JOR) hosted by banks brings all banks and related financial institutions together under one umbrella to follow up and monitor confirmed financial fraud cases affecting customers; it operates 24/7 to provide quick and effective co-operation among Saudi banks, limit fraud development, respond swiftly to complaints and take immediate action where possible. (p. 40)[^original]  
  <sub>anchor: "The JOR operates 24/7 and aims to provide quick and effective co-operation"</sub>

## Operational partnerships with the private sector

- **descriptive / finding or result**: Such partnerships also provide a platform to exchange best practices and common typologies and to co-develop recommended measures to disrupt illicit activity. (p. 40)[^original]  
  <sub>anchor: "These partnerships also provide a useful platform to exchange best practices, and common typologies"</sub>

## Box 27. Europol Financial Intelligence Public Private Partnership

- **descriptive / case example**: Box 27 (Europol): the Europol Financial Intelligence Public Private Partnership (EFIPPP) is the first transnational public-private information sharing mechanism for AML/CFT, bringing together law enforcement, FIUs and private entities across EU and non-EU countries. Its Threats and Typologies Working Group has work streams on CEF topics including BEC, investment fraud, mule accounts, virtual IBANs and crypto assets; it aims to produce strategic typology reports and also provides a platform to discuss operational co-operation. (p. 40)[^original]  
  <sub>anchor: "first transnational information sharing public-private mechanism for AML/CFT"</sub>

## Operational partnerships with the private sector

- **descriptive / finding or result**: PPP composition varies: many jurisdictions focus on traditional stakeholders (banks and other FIs) but there is increasing involvement of DNFBPs, VASPs and non-traditional sectors (e.g. telecommunications operators, internet service providers), depending on the PPP's aims and objectives. (p. 41)[^original]  
  <sub>anchor: "there is an increasing involvement of DNFBPs, VASPs and other non-traditional sectors"</sub>

## Box 28. Co-operation with telecommunications sector

- **descriptive / case example**: Box 28 (China): the Anti-Telecommunication Network Fraud Law of the People's Republic of China took effect on December 1, 2022 and brings together public authorities (law enforcement, financial, telecommunications and Internet information agencies), FIs (banks and non-bank payment service providers), telecom operators and ISPs to build an early warning and dissuasion system identifying potential victims and enabling timely dissuasive measures. (p. 41)[^original]  
  <sub>anchor: "to establish an early warning and dissuasion system"</sub>
- **descriptive / case example**: Box 28 continued: FIs can use this system when opening bank and payment accounts and providing payment and settlement services, to enhance CDD and take risk mitigation measures preventing accounts from being used for fraud. (p. 41)[^original]  
  <sub>anchor: "The system is used to enhance customer due diligence processes"</sub>

## 4.3. Useful domestic enforcement strategies

- **descriptive / context**: The enforcement strategies described leverage the information sources in section 4.1 to identify, investigate and prevent CEF and related ML, and typically involve multiple agencies and private sector entities, so strong domestic co-ordination and co-operation is typically required to implement them. (p. 41)[^original]  
  <sub>anchor: "This means that strong domestic co-ordination and co-operation is typically required to implement these strategies"</sub>

## Proper delineation of responsibility

- **descriptive / finding or result**: Many jurisdictions report increases in CEF losses and case volumes in recent years; while individual cases may involve small losses, the volume of scams means the total proceeds accumulated by each syndicate is potentially large. (p. 41)[^original]  
  <sub>anchor: "the volume of such scams means that the total proceeds of crime accumulated by each syndicate is potentially large"</sub>

---

[previous part](digest-002.md) | [source overview](overview.md) | [next part](digest-004.md)

[^original]: Egmont Group of FIUs, "Illicit Financial Flows from Cyber-Enabled Fraud" (2023-11). https://egmontgroup.org/wp-content/uploads/2023/11/Final_Illicit-financial-flows-from-cyber-enabled-fraud.pdf
