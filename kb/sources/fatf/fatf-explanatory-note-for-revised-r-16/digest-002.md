---
type: Source Digest
title: Explanatory note for revised R.16 - part 2 of 3 (pp. 10-21)
description: 'Verified paraphrased digest, pp. 10-21: Explanatory note for revised R.16 > 3.Key Issues addressed in the adopted text; Explanatory note for revised R.16 > 4.Timeline, implementation and transition issues; Recommendation 16. ~~Wire transfers~~ Payment transparency *; and 7 more sections'
resource: https://www.fatf-gafi.org/en/publications/Fatfrecommendations.html
tags:
- correspondent_banking
- data_features
- international_standard
- intl
- other
- regulation
- sanctions_adjacent
status: stable
source_id: fatf-explanatory-note-for-revised-r-16
issuer: fatf
issuer_name: Financial Action Task Force
jurisdictions:
- INTL
tier: 2
instrument_type: other
normative_force: international_standard
publication_date: '2025-10-28'
legal_status: current
part: 2
parts_total: 3
content_mode: digest
generated:
  by: claude-code-subagent/claude-sonnet-5-5
  at: '2026-11-16T16:22:31Z'
verified:
- by: process:kb-digest-check/anchor-match
  at: '2026-11-16T16:22:31Z'
- by: claude-code-judge-agent/claude-opus-5-5
  at: '2026-11-16T16:22:31Z'
sources:
- id: original
  resource: https://www.fatf-gafi.org/en/publications/Fatfrecommendations.html
  title: Explanatory note for revised R.16
  author: org:fatf
  last_modified: '2025-10-28T00:00:00Z'
digest_points: 72
---

# Explanatory note for revised R.16 (digest)

[source overview](overview.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (pp. 10-21) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **international standard**.

## Origin of funds

- **descriptive / typology or red flag**: The origin-of-funds footnotes target a typology where a payment is sent through an FI at which the customer holds no account with the funds, so the transaction is funded ad hoc from an account at a different FI, hiding the true origin account and potentially enabling evasion of risk-based controls. (p. 10)[^original]  
  <sub>anchor: "the transaction is funded ad-hoc from an account with a different FI"</sub>
- **expected / requirement**: Footnote 50 for paragraph 8 (b) and footnote 51 for paragraph 9 (b) of INR.16 require the account number and FI name of the ultimate origin of funds to be included in payment information, so the FI with the ongoing account relationship from which funds were drawn can always be identified. (p. 10)[^original]  
  <sub>anchor: "footnote 50 for paragraph 8 (b) and footnote 51 for paragraph 9 (b) of INR.16"</sub>

## Clarification of net settlement & bundled transactions

- **descriptive / requirement**: Revised R.16 confirms intermediary FIs are not required to unbundle net settlements, but the underlying payments or value transfers remain subject to R.16 requirements along their own payment chains. (p. 10)[^original]  
  <sub>anchor: "confirming that no unbundling by intermediary FIs is required"</sub>
- **descriptive / case example**: In the FATF diagram example, the payment chain follows the instruction route starting at MVTS F (receiving customer X's instruction) and all required information is carried MVTS F to MVTS G to Bank D to Bank E; Bank C has no R.16 obligations for the net settlement it conducts for Banks B and D, as these are FI-to-FI transfers. (p. 11)[^original]  
  <sub>anchor: "Bank C will have no obligations under Recommendation 16 regarding the net settlement"</sub>
- **descriptive / case example**: In the net settlement example, Bank A, MVTS F, MVTS G and Bank E remain bound by their CDD duties for the underlying bundled transactions, as applicable. (p. 11)[^original]  
  <sub>anchor: "Bank A, MVTS F, MVTS G and Bank E will continue to be bound by their CDD duties"</sub>

## Refinement of Glossary definitions

- **descriptive / context**: The February 2024 proposal introduced new glossary terms such as BIC, LEI, Unique Official Identifiers, MVTS network and updated ordering and beneficiary FI notions; respondents asked for more granularity (e.g., 'FI', 'merchant', 'transfer', 'address') and alignment with standards like SWIFT's cover payment definitions. (p. 11)[^original]  
  <sub>anchor: "BIC; LEI; Unique Official Identifiers, MVTS network"</sub>
- **descriptive / context**: Glossary changes were minimal: the 'merchant' definition was removed, the ordering FI definition was targeted to the instruction route, and cash withdrawals were included in the definition of Payment or Value Transfers. (p. 11)[^original]  
  <sub>anchor: "including cash withdrawals in the definition of Payment or Value Transfers"</sub>
- **descriptive / context**: Card payments, cash withdrawals and information requirements such as address may be addressed in more detail in upcoming FATF guidance. (p. 11)[^original]  
  <sub>anchor: "could be addressed in more detail in upcoming FATF guidance"</sub>

## Scope issues (payment market infrastructures (PMIs); virtual assets (VAs); and FinTechs)

- **descriptive / requirement**: Revised R.16 does not directly apply AML/CFT regulation to payment market infrastructures (PMIs); FATF considered this outside R.16 scope and potentially disruptive given PMIs' ISO 20022 transition demands. (p. 12)[^original]  
  <sub>anchor: "The revised R.16 does not directly apply AML/CFT regulation to PMIs"</sub>
- **descriptive / context**: Many PMIs are already accountable to FIs as owners and customers and to national supervision and oversight. (p. 12)[^original]  
  <sub>anchor: "many PMIs are already accountable to FIs as both owners and customers"</sub>
- **descriptive / limitation**: Respondents noted some PMIs, especially some domestic PMIs used for the last mile of cross-border payments, lack capacity to support end-to-end payment transparency; FATF will support PMIs via guidance and coordination with CPMI. (p. 12)[^original]  
  <sub>anchor: "some PMIs lack sufficient capacity to support end-to-end payment transparency"</sub>
- **expected / requirement**: VASPs are not brought directly into R.16 scope; the updated requirements apply to them indirectly through R.15, with travel rule implementation continuing via R.15's tailored framework and the Virtual Asset Contact Group (VACG). VASPs must still comply with the new requirements. (p. 12)[^original]  
  <sub>anchor: "not to bring VASPs directly into the scope of R.16 but to apply the updated requirements indirectly through R.15"</sub>
- **descriptive / context**: INR.15 will be updated if necessary so its reference to R.16 information requirements stays current. (p. 12)[^original]  
  <sub>anchor: "INR.15 will be updated, if necessary"</sub>
- **descriptive / context**: VASP respondents said they already have technology for some new duties, such as identifying misdirected payments through pre-validation checks, and asked for sector-specific guidance. (p. 12)[^original]  
  <sub>anchor: "they already have the technology required for some of new duties"</sub>
- **descriptive / context**: A main driver of the R.16 revision was a level playing field between FIs and other payment service providers such as fintechs; R.16 obligations are not limited to banks, and the focus on activity types over entity types better captures all payment actors. (p. 12)[^original]  
  <sub>anchor: "ensure a level playing field between FIs and other payment service providers"</sub>

## 4.Timeline, implementation and transition issues

- **descriptive / context**: A prerequisite for implementing revised R.16 is that the same information requirements exist in both origin and destination countries and that all parties' technical systems support them. (p. 13)[^original]  
  <sub>anchor: "same information requirements are in place in both the origin and destination countries"</sub>
- **expected / requirement**: Although FATF amendments normally take effect immediately, a transition period applies for revised R.16, with the end of 2030 as the realistic implementation deadline; FATF expects most or all new requirements in effect by then. (p. 13)[^original]  
  <sub>anchor: "the end of 2030, which has been identified as a as a realistic deadline for implementation"</sub>
- **descriptive / limitation**: Some changes, such as cash withdrawals and domestic PMI updates for the new payment chain definition, may need longer; the Payment Advisory Group (PAG) will help develop guidance, monitor implementation and identify tailored deadlines where required. (p. 13)[^original]  
  <sub>anchor: "including identifying the need for tailored deadlines in response to industry challenges"</sub>

## Recommendation 16. Payment transparency

- **expected / requirement**: Revised Recommendation 16 (retitled from 'Wire transfers' to 'Payment transparency') requires countries to ensure FIs include required and accurate originator information and required beneficiary information on payments or value transfers and related messages. (p. 14)[^original]  
  <sub>anchor: "Countries should ensure that financial institutions include required and accurate originator information"</sub>
- **expected / requirement**: Under R.16, originator and beneficiary information should be structured to the extent possible and remain with the payment or value transfer or related message throughout the payment chain. (p. 14)[^original]  
  <sub>anchor: "This information should be structured to the extent possible"</sub>
- **expected / requirement**: R.16 requires countries to ensure FIs monitor payments or value transfers to detect those lacking required originator and/or beneficiary information and take appropriate measures. (p. 14)[^original]  
  <sub>anchor: "for the purpose of detecting those which lack required originator and/or beneficiary informatio"</sub>
- **expected / requirement**: R.16 requires countries to ensure FIs processing payments or value transfers take freezing action and are prohibited from transacting with designated persons and entities under relevant UNSCRs, such as resolution 1267 (1999) and successors, resolution 1373(2001), and proliferation financing resolutions. (p. 14)[^original]  
  <sub>anchor: "such as resolution 1267 (1999) and its successor resolutions, and resolution 1373(2001)"</sub>

## A. OBJECTIVE

- **descriptive / context**: INR.16 paragraph 1: R.16 aims to prevent terrorists, money launderers, perpetrators of predicate offences (e.g., fraud) and other criminals from having unfettered access to payments or value transfers, and to detect such misuse. (p. 15)[^original]  
  <sub>anchor: "perpetrators of money laundering and associated predicate offences (e.g., fraud)"</sub>
- **descriptive / context**: R.16 aims to make basic originator and beneficiary information immediately available to law enforcement/prosecutors (to detect, investigate, prosecute and trace assets), to FIUs (to analyse suspicious or unusual activity), and to ordering, intermediary and beneficiary FIs (to identify and report suspicious transactions and implement freezing and prohibitions). (p. 15)[^original]  
  <sub>anchor: "to financial intelligence units for analysing suspicious or unusual activity"</sub>
- **descriptive / definition**: Footnote 48: 'originator' and 'beneficiary' in R.16 are interchangeable with 'debtor' and 'creditor' used in messaging standards such as ISO 20022. (p. 15)[^original]  
  <sub>anchor: "interchangeable with the terms "debtor" and "creditor" respectively"</sub>
- **descriptive / context**: Footnote 49: R.16 does not specify whether or how transmitted information should be screened against sanctions lists, since various mechanisms can ensure TFS compliance. (p. 15)[^original]  
  <sub>anchor: "Recommendation 16 does not specify whether or how the information transmitted should be screened"</sub>
- **expected / expectation**: INR.16 paragraph 2: countries should be able to trace all payments or value transfers and, given the terrorist financing threat from small transfers, should minimise thresholds while considering the risk of driving transactions underground and financial inclusion. (p. 15)[^original]  
  <sub>anchor: "countries should minimise thresholds, while taking into account the risk of driving transactions underground"</sub>
- **descriptive / context**: The FATF does not intend to impose rigid standards or mandate a single operating process that would harm the payment system or financial inclusion. (p. 15)[^original]  
  <sub>anchor: "It is not the intention of the FATF to impose rigid standards"</sub>

## B. SCOPE

- **descriptive / requirement**: INR.16 paragraph 3: R.16 applies to cross-border and domestic payments or value transfers, including serial payments and cover payments, with differentiated obligations by transaction type per Section C. (p. 15)[^original]  
  <sub>anchor: "including serial payments ~~,~~ and cover payments"</sub>
- **expected / requirement**: INR.16 paragraph 4: information accompanying payments or value transfers should be structured, to the extent possible, per the system's established standards such as ISO 20022, and detailed enough to identify originator and beneficiary. (p. 15)[^original]  
  <sub>anchor: "in accordance with the established standards of the system used such as ISO 20022"</sub>

## C. INFORMATION REQUIREMENTS

- **descriptive / definition**: INR.16 paragraph 6: the payment chain starts at the FI receiving the originator's instructions to transfer funds to the beneficiary and ends at the FI servicing the beneficiary's account or providing cash to the beneficiary. (p. 16)[^original]  
  <sub>anchor: "the payment chain starts at the financial institution that receives the instructions from the originator"</sub>
- **expected / requirement**: INR.16 paragraph 7: payment message information should allow the institutions and authorities in paragraph 1 to identify which FI services the originator's and beneficiary's accounts and in which countries; FIs should ensure account numbers are not used to disguise the country of the servicing FI. (p. 16)[^original]  
  <sub>anchor: "account numbers should not be used to disguise the identification of the country"</sub>

## De-minimis threshold for cross-border payments and value transfers

- **permissive / requirement**: INR.16 paragraph 8: countries may adopt a de minimis threshold no higher than USD/EUR 1,000 for cross-border payments or value transfers other than cash withdrawals. (p. 16)[^original]  
  <sub>anchor: "Countries may adopt a de minimis threshold (no higher than USD/EUR 1,000)"</sub>
- **expected / requirement**: Below the cross-border de minimis threshold, FIs should include the names of originator and beneficiary and their account numbers where accounts are used to process the transaction, or otherwise a unique transaction reference number permitting traceability. (p. 16)[^original]  
  <sub>anchor: "a unique transaction reference number should be included, which permits traceability of the transaction"</sub>
- **permissive / requirement**: Below-threshold cross-border information need not be verified for accuracy unless there is suspicion of ML or TF, in which case the FI should verify information relating to its customer. (p. 16)[^original]  
  <sub>anchor: "Such information need not be verified for accuracy, unless there is a suspicion of money laundering"</sub>
- **expected / requirement**: Footnotes 50 and 51 of INR.16: where funds are drawn from an FI other than the ordering FI, the account number and name of the FI from which funds are drawn should be included. (p. 16)[^original]  
  <sub>anchor: "the account number and the name of financial institution from where the funds are drawn should be included"</sub>

## Payments and value transfers above the de minimis threshold

- **expected / requirement**: INR.16 paragraph 9: cross-border payments above the threshold should always include originator and beneficiary names and account numbers where used (or a unique transaction reference number). (p. 16)[^original]  
  <sub>anchor: "Information accompanying all ~~qualifying~~ cross-border ~~wire~~ payments or value transfers above the applicable threshold"</sub>
- **expected / requirement**: INR.16 paragraph 9(c): above-threshold cross-border transfers should include the originator's address and the beneficiary's country and town name (or nearest alternative); footnote 52 allows country and town name for the originator absent standardised postal address information. (p. 16)[^original]  
  <sub>anchor: "In the absence of standardised postal address information for the originator, the country and town name"</sub>
- **expected / requirement**: INR.16 paragraph 9(d): where the originator is a natural person, the originator's date of birth should be included; footnote 53 says only the year of birth is required when full date of birth is unavailable. (p. 17)[^original]  
  <sub>anchor: "When full information of the date of birth is not available, only the year of birth is required"</sub>
- **expected / requirement**: INR.16 paragraph 9(e): where originator and/or beneficiary is a legal person, include where it exists the connected BIC, or the LEI, or the unique official identifier. (p. 17)[^original]  
  <sub>anchor: "the connected business identifier code (BIC), or (ii) the Legal Entity Identifier (LEI)"</sub>

## De-minimis threshold for domestic payments or value transfers

- **permissive / requirement**: INR.16 paragraph 10: countries may adopt a de minimis threshold no higher than USD/EUR 1,000 for domestic payments; below it FIs should include the originator's name and account number or a unique transaction reference number traceable to originator or beneficiary, which need not be verified absent ML/TF suspicion. (p. 17)[^original]  
  <sub>anchor: "Countries may also adopt a de minimis threshold (no higher than USD/EUR 1,000), for domestic payments"</sub>

## Payments or value transfers above the de-minimis threshold

- **expected / requirement**: INR.16 paragraph 11: domestic payments should include originator information as in paragraph 9, unless it can be made available to the beneficiary FI and authorities by other means, in which case only the account number or a traceable unique transaction reference number is needed. (p. 17)[^original]  
  <sub>anchor: "unless this information can be made available to the beneficiary financial institution and appropriate authorities by other means"</sub>
- **expected / requirement**: INR.16 paragraph 12: the ordering FI should make the information available within three business days of a request from the beneficiary or intermediary FI or competent authorities, and law enforcement should be able to compel immediate production. (p. 17)[^original]  
  <sub>anchor: "Law enforcement authorities should be able to compel immediate production of such information"</sub>

## Exceptions and Differentiated Requirements

- **descriptive / requirement**: INR.16 paragraph 13: no information is required to accompany FI-to-FI transfers and settlements where both originator and beneficiary are FIs acting on their own behalf. (p. 17)[^original]  
  <sub>anchor: "are financial institutions acting on their own behalf"</sub>
- **descriptive / requirement**: INR.16 paragraph 14: underlying customer transaction information need not accompany a net settlement, but R.16 requirements still apply to the underlying transactions themselves. (p. 17)[^original]  
  <sub>anchor: "information about the underlying transactions is not required to accompany the net settlement"</sub>
- **permissive / requirement**: INR.16 paragraph 15: batched cross-border transfers from a single originator may be exempt from paragraphs 8 and 9 originator information requirements if each includes the originator's account number or unique transaction reference number and the batch file contains required and accurate originator information and full beneficiary information fully traceable in the beneficiary country. (p. 18)[^original]  
  <sub>anchor: "bundled in a batch file for transmission to beneficiaries they may be exempted"</sub>

## Card payments

- **expected / requirement**: INR.16 paragraph 16: for card (credit, debit or prepaid) purchases of goods or services, the card number should accompany all resulting transfers and the name and location of the card issuing and merchant acquiring FIs should be made available upon request. (p. 18)[^original]  
  <sub>anchor: "the name and location of the card issuing and merchant acquiring financial institutions55 should be made available upon request"</sub>
- **descriptive / definition**: Footnote 54: 'purchase of goods or services' means purchases from individuals or entities onboarded by the relevant FI to accept card payments following the required CDD. (p. 18)[^original]  
  <sub>anchor: "purchases from individuals/entities who are onboarded by the relevant financial institution to accept card payments"</sub>
- **expected / requirement**: Footnotes 55-56: issuer and acquirer information should enable identifying which FIs hold full cardholder and merchant information and their countries, and should be made available in a timely manner (e.g., with card network assistance) to other FIs in the chain and through them to competent authorities. (p. 18)[^original]  
  <sub>anchor: "with the direct or indirect assistance of the relevant card network"</sub>
- **expected / requirement**: INR.16 paragraph 17: when a card is used for other types of payment or value transfer, such as person-to-person transfers, the applicable domestic or cross-border requirements apply. (p. 18)[^original]  
  <sub>anchor: "subject to the applicable requirements above for domestic or cross-border payments or value transfers"</sub>

## Cash withdrawals

- **descriptive / requirement**: INR.16 paragraph 18: domestic cash withdrawals need only the account number or card number. (p. 18)[^original]  
  <sub>anchor: "No information beyond the account number or card number is required to accompany domestic cash withdrawals"</sub>
- **expected / requirement**: INR.16 paragraph 19: for cross-border cash withdrawals using a card through a different FI, the card number should accompany the withdrawal and the cardholder's name should be sent to the acquiring FI upon request within three business days. (p. 18)[^original]  
  <sub>anchor: "The name of the cardholder should be sent to the acquiring financial institution upon request"</sub>
- **descriptive / requirement**: Footnote 57: the cross-border cash withdrawal requirements do not apply to withdrawals from ATMs operated by the account-holding institution, provided the information is available by other means under Recommendation 18. (p. 18)[^original]  
  <sub>anchor: "do not apply to withdrawals from ATMs operated by the same institution where the account is held"</sub>

## D. RESPONSIBILITIES OF ORDERING, INTERMEDIARY AND BENEFICIARY FINANCIAL INSTITUTIONS INCLUDING MVTS

- **descriptive / definition**: Footnote 58: 'ordering FI' and 'beneficiary FI' are interchangeable with 'debtor agent' and 'creditor agent' in standards like ISO 20022; footnote 59 says Section D responsibilities do not apply to cash withdrawals and card purchases of goods or services. (p. 18)[^original]  
  <sub>anchor: "do not apply to cash withdrawals and card payments for purchase of goods or services"</sub>

## Ordering (debtor) financial institution

- **expected / requirement**: INR.16 paragraph 20: the ordering FI should ensure cross-border transfers above the de minimis threshold contain required and accurate originator information and required beneficiary information. (p. 19)[^original]  
  <sub>anchor: "contain required and accurate originator information, and required beneficiary information"</sub>
- **expected / requirement**: INR.16 paragraph 21: the ordering FI should ensure below-threshold cross-border transfers contain originator and beneficiary names and an account number for each, or a unique transaction reference number. (p. 19)[^original]  
  <sub>anchor: "below the de minimis threshold ~~any applicable threshold~~ contain the name of the originator"</sub>
- **expected / requirement**: INR.16 paragraph 22: the ordering FI should maintain all originator and beneficiary information collected in accordance with Recommendation 11. (p. 19)[^original]  
  <sub>anchor: "should maintain all originator and beneficiary information collected, in accordance with Recommendation 11"</sub>
- **expected / requirement**: INR.16 paragraph 23: the ordering FI should not be allowed to execute a payment or value transfer that does not comply with these requirements. (p. 19)[^original]  
  <sub>anchor: "should not be allowed to execute the"</sub>

## Intermediary financial institution

- **expected / requirement**: INR.16 paragraph 24: FIs processing an intermediary element of cross-border transfers should ensure all accompanying originator and beneficiary information is retained with the transfer. (p. 19)[^original]  
  <sub>anchor: "should ensure that all originator and beneficiary information that accompanies a"</sub>
- **expected / requirement**: INR.16 paragraph 25: where technical limitations prevent required information remaining with a related domestic transfer, the receiving intermediary FI should keep a record of all information received for at least five years. (p. 19)[^original]  
  <sub>anchor: "a record should be kept, for at least five years, by the receiving intermediary financial institution"</sub>
- **expected / requirement**: INR.16 paragraph 26: intermediary FIs should take reasonable measures, consistent with straight-through processing, to identify cross-border transfers lacking required information. (p. 19)[^original]  
  <sub>anchor: "Such measures should be consistent with straight-through processing"</sub>
- **expected / requirement**: INR.16 paragraph 27: intermediary FIs should have effective risk-based policies and procedures for deciding when to execute, reject or suspend a transfer lacking required originator or beneficiary information, and on follow-up action. (p. 19)[^original]  
  <sub>anchor: "when to execute, reject, or suspend a"</sub>

## Beneficiary (creditor) financial institution

- **expected / requirement**: INR.16 paragraph 28: beneficiary FIs should take reasonable measures to identify cross-border transfers lacking required originator or beneficiary information, which may include post-event or, where feasible, real-time monitoring. (p. 19)[^original]  
  <sub>anchor: "Such measures may include post-event monitoring or real-time monitoring where feasible"</sub>
- **expected / requirement**: INR.16 paragraph 29: for cross-border transfers above the de minimis threshold, the beneficiary FI should verify the beneficiary's identity if not previously verified and maintain it per Recommendation 11. (p. 20)[^original]  
  <sub>anchor: "a beneficiary financial institution should verify the identity of the beneficiary, if the identity has not been previously verified"</sub>
- **expected / requirement**: INR.16 paragraph 30: for above-threshold cross-border transfers, beneficiary information should inform the beneficiary FI's monitoring to detect misdirected payments (e.g., ML, fraud or error), and beneficiary FIs should mitigate the risk of transfers to an unintended beneficiary through at least one of options (a), (b) or (c). (p. 20)[^original]  
  <sub>anchor: "with the objective of detecting misdirected payments (e.g. due to possible money laundering, fraud, or error)"</sub>
- **expected / requirement**: INR.16 paragraph 30(a): the beneficiary FI checks, for each transaction, how far the beneficiary name and account number in the message align with its own information. (p. 20)[^original]  
  <sub>anchor: "check the extent to which the name and account number of the beneficiary in the payment message aligns60"</sub>
- **expected / requirement**: INR.16 paragraph 30(b): the beneficiary FI conducts risk-based holistic ongoing monitoring to identify anomalous accounts, transactions and activity, including misaligned beneficiary information. (p. 20)[^original]  
  <sub>anchor: "conduct holistic ongoing monitoring to identify anomalous accounts, transactions, and activity"</sub>
- **permissive / requirement**: INR.16 paragraph 30(c): if both beneficiary and ordering FIs participate in a pre-validation mechanism such as confirmation/verification of payee checking name and account number per transaction, this may be used instead of (a) or (b). (p. 20)[^original]  
  <sub>anchor: "then this prevalidation may be used instead of (a) or (b) above"</sub>
- **descriptive / definition**: Footnote 60: alignment does not require an exact match, and the expected degree of alignment may vary with risk and context. (p. 20)[^original]  
  <sub>anchor: "Alignment does not imply that there must be an exact match"</sub>
- **expected / requirement**: INR.16 paragraph 31: beneficiary FIs should have effective risk-based policies and procedures for when to execute, reject or suspend transfers lacking required information or identified as potentially misdirected, and for follow-up action. (p. 20)[^original]  
  <sub>anchor: "when they identify potentially misdirected payments in the implementation of the requirements under paragraph 30"</sub>

## Money or value transfer service operators

- **expected / requirement**: INR.16 paragraph 32: MVTS providers should be required to comply with all relevant R.16 requirements in the countries where they operate, directly or through agents. (p. 20)[^original]  
  <sub>anchor: "Money or value transfer service (MVTS) providers should be required to comply with all of the relevant requirements"</sub>
- **expected / requirement**: An MVTS provider controlling, or part of a network controlling, both ordering and beneficiary sides should consider information from both sides when deciding whether to file an STR, file an STR in any affected country, and make relevant transaction information available to the FIU. (p. 20)[^original]  
  <sub>anchor: "should file an STR in any country affected by the suspicious"</sub>

---

[source overview](overview.md)

[^original]: Financial Action Task Force, "Explanatory note for revised R.16" (2025-10-28). https://www.fatf-gafi.org/en/publications/Fatfrecommendations.html
