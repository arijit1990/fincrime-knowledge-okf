---
type: Source Digest
title: Expanding mandatory ISO 20022 enhanced data in CHAPS from 2027 - part 2 of 2 (p. 1)
description: 'Verified paraphrased digest, p. 1: Expanding mandatory ISO 20022 enhanced data in CHAPS from 2027 > 2: Expanding the requirement for Purpose Codes to all CHAPS payments from November 2027; Expanding mandatory ISO 20022 enhanced data in CHAPS from 2027 > 3: Enhanced data requirements for payment initiation channels outside CHAPS DPs’ control; Expanding mandatory ISO 20022 enhanced data in CHAPS from 2027 > Annex'
resource: https://www.bankofengland.co.uk/paper/2025/ps/expanding-mandatory-iso-20022-enhanced-data-in-chaps-from-2027
tags:
- correspondent_banking
- data_features
- policy_statement
- regulatory_expectation
- sanctions_adjacent
- uk
status: stable
source_id: pra-boe-expanding-mandatory-iso-20022-enhanced-data-in-chaps-from-2027
issuer: pra_boe
issuer_name: Prudential Regulation Authority / Bank of England
jurisdictions:
- UK
tier: 1
instrument_type: policy_statement
normative_force: regulatory_expectation
publication_date: '2026-08-28'
legal_status: current
part: 2
parts_total: 2
content_mode: digest
generated:
  by: claude-code-subagent/claude-sonnet-5-5
  at: '2026-11-21T13:52:44Z'
verified:
- by: process:kb-digest-check/anchor-match
  at: '2026-11-21T13:52:44Z'
- by: claude-code-judge-agent/claude-opus-5-5
  at: '2026-11-21T13:52:44Z'
sources:
- id: original
  resource: https://www.bankofengland.co.uk/paper/2025/ps/expanding-mandatory-iso-20022-enhanced-data-in-chaps-from-2027
  title: Expanding mandatory ISO 20022 enhanced data in CHAPS from 2027
  author: org:pra_boe
  last_modified: '2026-08-28T00:00:00Z'
digest_points: 55
---

# Expanding mandatory ISO 20022 enhanced data in CHAPS from 2027 (digest)

[previous part](digest-001.md) | [source overview](overview.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (p. 1) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **regulatory expectation**.

## 2.5: UK alignment

- **expected / expectation**: The Bank agrees on the importance of communications and industry co-ordination, is enhancing how it engages with industry to resolve obstacles, and expects industry to reinforce its communications and requirements to realise the benefits of purpose codes; it is also working with the Standards Advisory Panel on payments standards at a strategic level, including UK retail payments with Pay.UK and a strategic discussion on payment fraud standards. (p. 1)[^original]  
  <sub>anchor: "we expect industry to reinforce our communications and requirements, to realise the benefits of purpose codes"</sub>
- **descriptive / finding or result**: A respondent noted CHAPS DPs are building internal controls to comply with enhanced data requirements without technical rejection from Swift and CHAPS; for full compliance by November 2027 DPs will need full understanding of technical rejection to develop controls managing non-compliance risk, and the respondent asked for formalised testing for all CHAPS DPs of their full control suite, including the technical rejection control at Swift and RTGS. (p. 1)[^original]  
  <sub>anchor: "CHAPS DPs are building the internal controls to be compliant with the enhanced data requirements"</sub>

## 2.6: Purpose Code not provided

- **descriptive / finding or result**: One respondent was concerned that not rejecting payments lacking Purpose Codes means initiators may populate them incorrectly or not at all, exacerbated by discouragement of default codes such as OTHR; reasonable and proportionate controls would need an internal strategy with systematic controls plus extensive client outreach, including agreeing with specific channels which codes suit their payment flows. (p. 1)[^original]  
  <sub>anchor: "the use of default codes (such as OTHR) is discouraged"</sub>
- **descriptive / finding or result**: Another respondent said that where payments originate outside its group it cannot enforce provision of a purpose code unless all CHAPS DPs decide to reject inbound payments without one; another suggested creating a 'Not provided' code for when a purpose code is not received from an Indirect participant. (p. 1)[^original]  
  <sub>anchor: "a ‘Not provided’ code could be created for when a purpose code is not received from an Indirect participant"</sub>
- **descriptive / finding or result**: Another respondent said that for file-submitted payments where the client has not populated the Purpose Code, it will neither populate it itself nor stop or reject the payment since CHAPS does not reject payments without Purpose Codes, but plans to educate clients to use Purpose Codes for all file payments. (p. 1)[^original]  
  <sub>anchor: "is not going to populate it themselves and is not going to stop/reject those payments either"</sub>
- **descriptive / finding or result**: A separate respondent said that although CHAPS is not yet technically rejecting via the schema, its vendor must build the mandatory requirements into CHAPS payment validation, so a CBPR+ instruction to make a CHAPS payment without the required enhanced data would fall to a repair queue and not straight-through-process, risking a decline in CHAPS STP rates with resourcing implications; it must decide whether to reject such instructions or process with customer education and monitoring, and will need monitoring processes to understand customer behaviour and meet periodic assurance. (p. 1)[^original]  
  <sub>anchor: "the payment will fall to a repair queue and will not straight-through-process"</sub>
- **descriptive / finding or result**: A final respondent concluded that industry needs to align on the treatment of messages that lack Purpose Codes where they should be present. (p. 1)[^original]  
  <sub>anchor: "the industry needs to align on the treatment of messages which do not have Purpose Codes"</sub>
- **descriptive / requirement**: The Bank's response: it has previously published that it will not reject CHAPS payments solely due to incomplete or incorrect enhanced data before end-2028 at the earliest, and supports DP feedback on customer communications and an approach of monitoring and following up when Purpose Codes are not provided. (p. 1)[^original]  
  <sub>anchor: "We have previously published that we will not reject CHAPS payments solely due to incomplete or incorrect enhanced data"</sub>
- **descriptive / finding or result**: One respondent made the point that the more data is entered, the greater the chance of error and misunderstanding; accuracy matters if the data is relied on for treatment purposes (e.g. financial crime), and data protection and permissions implications would need to be explored with any processing complying with applicable data protection requirements. (p. 1)[^original]  
  <sub>anchor: "the more data is to be entered, the greater chance of error and incorrect understanding"</sub>

## 2.7: The risks of greater data

- **descriptive / context**: The Bank recognises the data risk point as important for all payments data irrespective of value, and continues to support best practice around data protection. (p. 1)[^original]  
  <sub>anchor: "irrespective of value, and we continue to support best practice around data protection"</sub>
- **descriptive / finding or result**: An end-user said manually keyed payments are likely less of an issue with shorter lead-in times to the November 2027 deadline, but for bulk submissions and reporting end-users need PSPs to share technical guides as soon as possible; without good quality timely information it will be impossible to plan downstream system changes, and corporate and government customers do not always have enough time to implement changes. (p. 1)[^original]  
  <sub>anchor: "for bulk submissions, reporting etc, end-users need their PSPs to be sharing technical guides as soon as possible"</sub>

## 2.8: Lateness of communications to end-users

- **descriptive / context**: The Bank publishes mandatory enhanced data requirements with at least 18 months' notice so CHAPS DPs can communicate with customers in time, continues to engage certain end-users, and follows up with CHAPS DPs not giving customers requirements in sufficient time. (p. 1)[^original]  
  <sub>anchor: "We publish our mandatory enhanced data requirements with at least 18 months’ notice"</sub>
- **descriptive / finding or result**: One respondent acting as intermediary bank with significant pacs.008 volumes (mostly FI to FI flow) said providing assurance through CHAPS Reference Manual attestation on the integrity of overseas instigators or its own corporates would be nearly impossible, as it has limited visibility of the true purpose of payment. (p. 1)[^original]  
  <sub>anchor: "providing assurance through CHAPS Reference Manual attestation on the integrity of instigators overseas"</sub>

## 2.9: Not knowing the true purpose

- **descriptive / finding or result**: Another respondent felt that where customers choose the Purpose Code, the PSP has no viable means to validate that customers using proprietary channels choose the correct Purpose Code in every use case. (p. 1)[^original]  
  <sub>anchor: "the PSP does not have viable means to validate that their customers making payments from proprietary channels"</sub>
- **descriptive / requirement**: The Bank reminds DPs of their regulatory requirements (including under AML, financial crime and tax regimes) to obtain information relating to their customers and their customers' transactions. (p. 1)[^original]  
  <sub>anchor: "we remind DPs of their regulatory requirements (including under AML, financial crime and tax regimes)"</sub>
- **descriptive / context**: The Bank continues to give at least 18 months' notice ahead of expanding CHAPS enhanced data requirements, and almost all respondents confirmed this should enable industry to prepare for the expanded purpose code requirements. (p. 1)[^original]  
  <sub>anchor: "We continue to provide at least 18 months’ notice ahead of expanding any CHAPS enhanced data requirements."</sub>
- **descriptive / context**: In Section 6.1 of the 2024 Policy Statement the Bank proposed expanding enhanced data requirements to CHAPS payments from all initiation channels from November 2027, an ambitious timeline responding to industry feedback on mandating to increase usage; by November 2027 other major jurisdictions are expected to have migrated to ISO 20022, end-2027 is the CPMI harmonisation deadline for market infrastructures for cross-border payments, and CHAPS DPs are expected to have had time to increase enhanced data use and client communications. (p. 1)[^original]  
  <sub>anchor: "End-2027 is also the deadline for market infrastructures to meet the Committee on Payments and Market Infrastructures (CPMI) harmonisation requirements"</sub>

## 3: Enhanced data requirements for payment initiation channels outside CHAPS DPs’ control

- **descriptive / finding or result**: Some respondents supported expanding mandatory requirements to all channels as vital for benefits across all participants, while several explained significant obstacles for DPs in ensuring enhanced data in payments initiated through channels DPs do not control (as defined in the CHAPS Operational Reference Manual); DPs argued they cannot directly control readiness of customers, indirect participants and vendors. (p. 1)[^original]  
  <sub>anchor: "channels that DPs do not control (as defined in the CHAPS Operational Reference Manual)"</sub>
- **expected / requirement**: The Bank will not expand mandatory requirements to initiation channels outside CHAPS DPs' control but reminds CHAPS DPs of their responsibilities to communicate CHAPS requirements to all those to whom DPs provide CHAPS access, as set out in paragraphs 37.1 to 37.17 of the CHAPS Reference Manual. (p. 1)[^original]  
  <sub>anchor: "we remind CHAPS DPs of their responsibilities to communicate CHAPS requirements to all those to whom DPs provide CHAPS access"</sub>
- **expected / expectation**: The Bank expects increasing volumes of CHAPS payments to move into DPs' control as more payment systems migrate to ISO 20022, will promote awareness through speeches, DPs' client briefings and white-label materials where appropriate, and expects CHAPS DPs to communicate the benefits of enhanced data to other payment system operators and users. (p. 1)[^original]  
  <sub>anchor: "We expect increasing volumes of CHAPS payments moving into CHAPS DPs’ control as more payment systems migrate to ISO 20022."</sub>
- **descriptive / context**: The Bank supports industry and itself building the value benefits case, noting some benefits may be quantifiable today while richer, structured data sets the foundation for future innovation and benefits that may not all be quantifiable ex ante; it supports the suggestion that payments lacking mandated enhanced data continue to settle while DPs report and escalate with payment initiators, and supports the need for data cleansing, downstream integration and ongoing assessment of internal changes. (p. 1)[^original]  
  <sub>anchor: "payments which do not include mandated enhanced data continue to settle, but DPs report and escalate with payment initiators"</sub>

## 3.1: Readiness of customers, indirect participants, and vendors

- **descriptive / finding or result**: Respondents argued CHAPS DPs cannot directly control readiness of customers, indirect participants and vendors; it may be difficult or impossible to implement source controls for channels DPs do not control (e.g. a bespoke form created by a customer of a customer), and rejecting non-compliant payments would be the most extreme approach but would slow processing and seem disproportionate. (p. 1)[^original]  
  <sub>anchor: "the origin of a payment instruction could be a bespoke form created by the customer of a customer"</sub>
- **descriptive / finding or result**: Multiple respondents said DPs with corporate customers depend on clients to update systems and processes or must add friction to payment initiation, with implications across internal functions and for terms and conditions with corporate customers, who may resist constant changes and varying data requirements; one said 'reasonable and proportionate controls' require an internal strategy of systematic controls plus extensive client outreach; respondents asked the Bank to collaborate more with the largest indirect participants, software providers and corporates and to learn their readiness timelines. (p. 1)[^original]  
  <sub>anchor: "‘reasonable and proportionate controls’ to ensure the data is provided will require implementation of an internal strategy"</sub>
- **descriptive / context**: The Bank's response: it accepts DPs cannot be held directly responsible for readiness of customers, indirect participants and vendors and so will not at this stage expand mandatory requirements to initiation channels outside DPs' control, but stresses DPs' responsibilities to communicate CHAPS requirements to all those they give CHAPS access; as CHAPS operator it can set requirements directly on DPs and relies on them to spread changes across the ecosystem. (p. 1)[^original]  
  <sub>anchor: "we can set requirements directly upon CHAPS DPs and rely upon CHAPS DPs to spread these positive changes further"</sub>
- **descriptive / context**: Pay.UK will apply the same approach for Faster Payments direct participants and will continue to collaborate with the Bank and support DPs to encourage adoption and best usage practices. (p. 1)[^original]  
  <sub>anchor: "Pay.UK will apply the same approach for Faster Payments direct participants."</sub>
- **recommended / recommendation**: The Bank strongly encourages DPs to design systematic controls to ensure enhanced data is included, and to provide customer education for successful implementation. (p. 1)[^original]  
  <sub>anchor: "We strongly encourage DPs to design systematic controls to ensure that enhanced data is included"</sub>

## 3.2: International harmonisation

- **descriptive / finding or result**: One respondent wanted the Bank to align its timeline and enhanced data requirements with CBPR+ and other international standards, otherwise DPs bear separate IT development and testing effort and cost and must prioritise technical resources across Asia, Europe and the US. (p. 1)[^original]  
  <sub>anchor: "aligning our timeline and enhanced data requirements with CBPR+/other international payments standards"</sub>
- **descriptive / context**: Part of the Bank's decision not to expand mandatory enhanced data requirements to channels outside DPs' control is to avoid diverging too far from international harmonisation; Pay.UK is committed to the same cross-border and international data harmonisation through enhanced ISO 20022 data. (p. 1)[^original]  
  <sub>anchor: "to avoid diverging too far from international harmonisation"</sub>

## 3.3: Domestic harmonisation

- **descriptive / finding or result**: One respondent warned consumers often do not know the rail underlying their payment, so a customer paying 25,000 pounds via Faster Payments with one PSP needs no Purpose Code but the same amount routed via CHAPS at another PSP does; it called for standardised communications wording and harmonised requirements across payment types including Faster Payments; another asked the Bank, Open Banking and Pay.UK to align on future enhanced data requirements (V4 of the Open Banking standards includes an uplift to ISO 20022) and wanted to understand impacts on Open Banking journeys. (p. 1)[^original]  
  <sub>anchor: "£25,000 via another PSP is routed via CHAPS and a Purpose Code is required"</sub>
- **descriptive / context**: The Bank's decision not to expand requirements to channels outside DPs' control is partly informed by feedback on not departing too far from other domestic standards; it engages regularly with Open Banking and Pay.UK on roadmaps, and in July 2025 Pay.UK outlined its approach to richer ISO 20022 enhanced data, aligned as far as possible with CHAPS enhanced data. (p. 1)[^original]  
  <sub>anchor: "In July 2025, Pay.UK outlined their approach to richer ISO 20022 enhanced data"</sub>

## 3.4: Benefits cases

- **descriptive / finding or result**: One respondent asked the Bank to keep engaging CHAPS participants on unlocking customer benefit; another asked for time to be invested in a detailed benefits case, e.g. how data insights and analytics generate value and what additional functionality is needed, citing data-driven fraud mitigation as a leading case, which requires a whole set of supporting processes to be available at once, with clarity on who drives the fraud mitigation use case and the data validation process to avoid false positives. (p. 1)[^original]  
  <sub>anchor: "the process for data validation to avoid false positives"</sub>
- **descriptive / context**: The Bank will continue to facilitate industry experts to develop benefits cases, aims its policy at realising enhanced data benefits where they outweigh implementation burden, welcomes fraud mitigation and analytics as initial benefits cases, and believes consistent, broad enhanced data usage lays a foundation for future benefits not yet apparent. (p. 1)[^original]  
  <sub>anchor: "where they outweigh the implementation burden"</sub>

## 3.5: Congestion of change initiatives

- **descriptive / finding or result**: Respondents agreed organisations must coordinate change capacity across payment developments, citing the National Payments Vision, Open Banking, combatting fraud, central bank digital currency, Account-to-Account payments and the way forward for retail payments; two respondents raised implications for building societies and other indirect participants (e.g. building societies with CHAPS mortgage volumes face a large lift with limited change capability across legacy payment gateway, processing and core banking estates), and one said ERP software providers will be stretched by individualised customisation and complex legacy integration. (p. 1)[^original]  
  <sub>anchor: "building societies with CHAPS mortgage volumes will be required to provide data"</sub>
- **descriptive / context**: Respondents asked for continued engagement and early communication from the Bank; the Bank's decision not to expand requirements outside DPs' control is partly informed by feedback on industry and regulatory congestion, and it reminds DPs of their responsibilities to ensure indirect participants are aware of and ready to meet CHAPS requirements (paragraphs 37.1 to 37.17 of the CHAPS Reference Manual). (p. 1)[^original]  
  <sub>anchor: "we remind DPs of their responsibilities to ensure that indirect participants are aware of and ready to meet CHAPS requirements"</sub>
- **descriptive / finding or result**: Respondents on payments without enhanced data noted that rejecting a payment for non-compliant format may be seen as a competitive differentiator between FIs, particularly for cross-border payments, so the Bank should clearly communicate and fairly arbitrate any rules-based rejection criteria; another said payments could keep flowing with procedures to report and escalate participants not meeting requirements. (p. 1)[^original]  
  <sub>anchor: "rejecting a customer’s payment due to a non-compliant format may be seen by the market as a competitive differentiator"</sub>

## 3.6: Payments without enhanced data

- **descriptive / context**: The Bank supports DPs reporting and escalating without rejecting payments at this stage, due to the financial stability implications. (p. 1)[^original]  
  <sub>anchor: "We support the approach of DPs reporting and escalating without rejecting payments at this stage"</sub>
- **descriptive / finding or result**: One respondent noted payment providers vary in structured data levels and data quality and integrity testing experience, so stakeholders and data sources may need data cleansing and cross-referencing for consistency across data sources, possibly across complex legacy systems and multiple functions; payments teams could operationalise ISO 20022 but other functions may be less agile, causing downstream impacts. (p. 1)[^original]  
  <sub>anchor: "relevant stakeholders and data sources may need to undertake data cleansing exercises"</sub>
- **recommended / recommendation**: The Bank supports the importance of data cleansing, is mindful of varying integration at CHAPS DPs, encourages DPs to ensure ISO 20022 requirements are taken into account when upstream systems are upgraded, and believes consistent quality enhanced data is crucial to building user confidence. (p. 1)[^original]  
  <sub>anchor: "We encourage CHAPS DPs to ensure that ISO 20022 requirements are taken into account when upstream systems are being upgraded."</sub>

## 3.8: Ongoing assessment

- **expected / expectation**: One respondent said channel, system, process and ledger changes to capture, process and store ISO data must continue to be assessed to estimate effort needed to comply by 2027 and beyond; the Bank agrees on the necessity of DPs making continuous assessments of these changes to meet CHAPS requirements and realise ISO 20022 enhanced data benefits. (p. 1)[^original]  
  <sub>anchor: "We agree with the necessity of DPs making continuous assessments of their channels, systems, process, and ledger changes"</sub>
- **descriptive / finding or result**: One respondent asked whether all CHAPS DPs will come into scope together or in a staggered approach similar to Confirmation of Payee, flagging possible market impacts on corporates and end-customers preferring not to move to enhanced data requirements in a staged roll-out. (p. 1)[^original]  
  <sub>anchor: "whether all CHAPS DPs will come into scope at the same time or whether we intend a staggered approach"</sub>

## 3.9: Staggered rollout

- **descriptive / context**: As with previous mandating, all CHAPS DPs come into scope of enhanced data requirements at the same time; if a staggered approach were adopted in future the Bank would consider market impacts on corporates and other end-customers. (p. 1)[^original]  
  <sub>anchor: "As with previous mandating, all CHAPS DPs come into scope of our enhanced data requirements at the same time."</sub>
- **descriptive / context**: The Bank accepts the CHAPS DP population is diverse and will engage with DPs who, due to specific constraints, may be unable to meet requirements when they come into force, including a clear understanding of their remediation plans and associated timeframes. (p. 1)[^original]  
  <sub>anchor: "We will engage with CHAPS DPs who, due to specific constraints, may be unable to meet the requirements"</sub>

## 3.10: Consolidated view

- **descriptive / context**: Two respondents asked for a consolidated view of all ISO 20022 fields to be updated, since each mandatory direction requires firms to modify systems multiple times; the Bank responded with the consolidated view in Box A. (p. 1)[^original]  
  <sub>anchor: "Two respondents asked for a consolidated view of all the ISO 20022 fields to be updated"</sub>

## Annex

- **descriptive / finding or result**: Annex, Legal Entity Identifiers: respondents supported the Bank's LEI approach; one noted LEI mandating supports the EU Transfer of Funds Regulation (TFR); another said the widest possible use of the LEI can significantly reduce administrative hurdles for CHAPS DPs while giving a secure means to monitor money-laundering and terrorist financing risks; another envisaged LEI use growing in ecommerce and digital certificates and expected the Bank to move to mandate LEI data for all CHAPS payments. (p. 1)[^original]  
  <sub>anchor: "the widest possible use of the LEI can significantly reduce administrative hurdles for CHAPS DPs"</sub>
- **descriptive / finding or result**: A fourth respondent said the global, interoperable LEI lets CHAPS DPs enhance customer due diligence and sanctions screening and identify 'who owns whom' in the financial system for more efficient resolution planning; the Bank's initiative is in line with recommendations of other bodies, including the FSB G20 Roadmap for Enhancing Cross-border Payments (LEI's role in sanctions compliance, customer due diligence and wire transfers) and Swift's Guiding principles for screening ISO 20022 payments endorsed by the PMPG and Wolfsberg Group (LEI supports targeted sanctions screening and AML/CFT). (p. 1)[^original]  
  <sub>anchor: "allowing CHAPS DPs to proceed with more efficient resolution planning"</sub>
- **descriptive / finding or result**: The Annex says FATF Recommendation 16 (the 'Travel Rule') has been updated to state that for originators and beneficiaries information accompanying all qualifying payments or value transfers 'should always contain' their BIC, LEI or unique official identifier; the Reserve Bank of India has mandated the LEI in all payment transactions totalling 50 crore rupees and more; and the EU AML Regulation references the LEI as a useful tool for identity checks on customers and beneficial owners of legal persons. (p. 1)[^original]  
  <sub>anchor: "information accompanying all qualifying payments or value transfers should always contain"</sub>
- **descriptive / finding or result**: As part of the EU AML package the EU TFR was recast so transfers are accompanied by data points (which may include LEIs where available) on the originator and beneficiary (for non-individuals), and the regulation on instant credit transfers in euros lets PSPs allow LEI use for payee verification. (p. 1)[^original]  
  <sub>anchor: "the EU TFR was recast to ensure that transfers are accompanied by various data points"</sub>
- **descriptive / case example**: Several respondents asked the Bank to work with Pay.UK to add LEIs to Bank Reference Data (the basis for the Extended Industry Sort Code Database, EISCD); the Bank and Pay.UK delivered this in July 2025, which prompted CHAPS DPs to improve data quality of BICs and sort codes and update processes, and Pay.UK is exploring whether it is repeatable or other sort-code enhancements are needed. (p. 1)[^original]  
  <sub>anchor: "we worked with Pay.UK to successfully deliver this change in July 2025"</sub>
- **descriptive / case example**: From June 2025 the PRA has been publishing LEIs for regulated investment firms, building societies and banks incorporated in the UK, and the list will be enriched in the coming months with LEIs for regulated legal entities incorporated overseas operating through a UK branch. (p. 1)[^original]  
  <sub>anchor: "From June 2025, the PRA has been publishing LEIs for regulated investment firms, building societies, and banks"</sub>

## 2.9: Not knowing the true purpose

- **descriptive / context**: Section 2.9 states a general expectation, in the form of a belief about data quality, that the originator of a payment is closest to its purpose and so best placed to provide the highest quality data (in line with the ISO 20022 definition). (p. 1)[^original]  
  <sub>anchor: "we expect the originator of the payment to be closest to the payment’s purpose"</sub>
- **descriptive / context**: Section 2.9 makes clear that the Bank has not made it a requirement for the originator to provide this data. (p. 1)[^original]  
  <sub>anchor: "but we have not set this as a requirement"</sub>
- **descriptive / context**: Section 2.9 says it is through widespread use of Purpose Codes that the CHAPS industry can begin to build the ability to identify, and follow up on, Purpose Codes that do not reflect the account's activity. (p. 1)[^original]  
  <sub>anchor: "It is precisely through the widespread usage of Purpose Codes that the CHAPS industry can begin to develop the ability"</sub>

## 3.5: Congestion of change initiatives

- **descriptive / context**: Industry feedback under Section 3.5: two respondents asked the Bank to consider implementation implications for building societies and other indirect participants, whose compliance onus lies with their sponsor bank or direct participant; one of them concluded that there must be clear mechanisms for indirect participants to be supported by their sponsor banks and/or to access the appropriate data effectively. (p. 1)[^original]  
  <sub>anchor: "there must be clear mechanisms for indirect participants to be supported by their sponsor banks"</sub>

## Annex

- **descriptive / context**: Annex feedback on LEIs: one respondent highlighted the role of the Validation Agent model in helping DPs enrich their internal databases with LEIs so they can meet the CHAPS requirements in good time, and noted that several CHAPS DPs' parent organisations already benefit from being Validation Agents. (p. 1)[^original]  
  <sub>anchor: "highlighted the role of the Validation Agent model in supporting DPs to enrich their internal databases with LEIs"</sub>
- **descriptive / context**: The same respondent encouraged that the LEI be regularly updated in line with the Global LEI system policy, so that DPs can draw on all the benefits of the LEI for know-your-customer procedures and the verification procedure stays credible and accurate. (p. 1)[^original]  
  <sub>anchor: "the LEI should be regularly updated in accordance with the Global LEI system policy"</sub>

---

[previous part](digest-001.md) | [source overview](overview.md)

[^original]: Prudential Regulation Authority / Bank of England, "Expanding mandatory ISO 20022 enhanced data in CHAPS from 2027" (2026-08-28). https://www.bankofengland.co.uk/paper/2025/ps/expanding-mandatory-iso-20022-enhanced-data-in-chaps-from-2027
