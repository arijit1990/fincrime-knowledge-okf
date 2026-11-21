---
type: Source Digest
title: Harmonised ISO 20022 data requirements for enhancing cross-border payments - updated report - part 4 of 4 (pp. 24-30)
description: 'Verified paraphrased digest, pp. 24-30: References; Annex 1: Harmonisation requirements core ISO 20022 message > Credit transfers (pacs.008, pacs.009, pacs.002); Annex 1: Harmonisation requirements core ISO 20022 message > Payment returns (camt.056, camt.029, pacs.004); and 1 more sections'
resource: https://www.bis.org/publications/harmonised-iso-20022-data-requirements-enhancing-cross-border-payments-updated-report
tags:
- correspondent_banking
- data_features
- international_standard
- intl
- standard
status: stable
source_id: bis-bcbs-harmonised-iso-20022-data-requirements-for-enhancing-cross-bo
issuer: bis_bcbs
issuer_name: Bank for International Settlements / Basel Committee
jurisdictions:
- INTL
tier: 2
instrument_type: standard
normative_force: international_standard
publication_date: '2026-02-26'
legal_status: current
part: 4
parts_total: 4
content_mode: digest
generated:
  by: claude-code-subagent/claude-sonnet-5-5
  at: '2026-11-17T17:26:57Z'
verified:
- by: process:kb-digest-check/anchor-match
  at: '2026-11-17T17:26:57Z'
- by: claude-code-judge-agent/claude-opus-5-5
  at: '2026-11-17T17:26:57Z'
sources:
- id: original
  resource: https://www.bis.org/publications/harmonised-iso-20022-data-requirements-enhancing-cross-border-payments-updated-report
  title: Harmonised ISO 20022 data requirements for enhancing cross-border payments - updated report
  author: org:bis_bcbs
  last_modified: '2026-02-26T00:00:00Z'
digest_points: 17
---

# Harmonised ISO 20022 data requirements for enhancing cross-border payments - updated report (digest)

[previous part](digest-003.md) | [source overview](overview.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (pp. 24-30) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **international standard**.

## Credit transfers (pacs.008, pacs.009, pacs.002)

- **descriptive / context**: Harmonised and agreed implementation guidance, including harmonised data models, for the interbank customer credit transfer (pacs.008) and FI credit transfer (pacs.009) is core to increased efficiency of cross-border payments. (p. 25)[^original]  
  <sub>anchor: "are core to the increased efficiency of cross-border payments"</sub>
- **descriptive / context**: Although FIs or payment platforms may have different mechanisms for updates on payment processing status, the payment status report (pacs.002) is the standard ISO 20022 message designed for that purpose and is included in the core set so harmonised data models can cover a variety of use cases and statuses. (p. 25)[^original]  
  <sub>anchor: "the payment status report (pacs.002) is the standard ISO 20022 message type designed to fulfil that purpose through messaging"</sub>

## Payment returns (camt.056, camt.029, pacs.004)

- **descriptive / context**: The interbank payment cancellation request (camt.056) and response (camt.029) are in the core set because timely cancellation of cross-border payments depends on harmonised implementation of the appropriate messaging standards and the minimum data required by customers when trying to cancel; this enables seamless processing of return requests in the interbank space. (p. 25)[^original]  
  <sub>anchor: "timely cancellation of cross-border payments depends on the use of a harmonised implementation"</sub>
- **descriptive / context**: The payment status request (pacs.028) allows FIs to follow up and obtain the latest available payment status of cross-border payments and is the ISO 20022 standard for this purpose. The investigation request (camt.110) and investigation response (camt.111) are also part of the core message set. (p. 25)[^original]  
  <sub>anchor: "allows FIs to follow up and obtain the latest available payment status of cross-border payments"</sub>
- **descriptive / limitation**: Footnote 21: camt.029 currently covers more functionality than responding to a return request, and the standard is likely to change as a result of ongoing redevelopment of exception and investigation messages, likely removing functionalities unrelated to payment cancellations; elements responding to a payment cancellation request are assumed not to be impacted. (p. 25)[^original]  
  <sub>anchor: "the message standard is likely to change in the future as a result of the ongoing"</sub>

## Other referenced messages

- **descriptive / context**: Beyond the core set, other ISO 20022 messages inform the harmonised data models, with implementation guidance in the technical annex. The customer-to-bank payment initiation message (pain.001) documents data elements customers initiating cross-border payments should provide for the most efficient experience, and the bank-to-customer payment status report (pain.002) is referenced to ensure consistency of data elements reported back to the initiating customer. (p. 25)[^original]  
  <sub>anchor: "Customer-to-bank payment initiation (pain.001) messages to document data elements to be provided by customers"</sub>
- **descriptive / limitation**: Footnote 22: an account servicer might have all data needed to report payment initiation status to the customer, from the initiation or from the interbank payment status report (pacs.002), but entities other than the account servicer and customer may be involved in initiating cross-border payments (for example relay scenarios). (p. 26)[^original]  
  <sub>anchor: "there may be situations in which entities other than the account servicer and the customer are involved in the initiation"</sub>
- **descriptive / context**: The customer-to-bank payment cancellation request and response (camt.055 and camt.029) are referenced to enhance the cancellation process by customers who initiated a cross-border payment. (p. 26)[^original]  
  <sub>anchor: "to enhance the payment cancellation process by customers that initiated a cross-border payment"</sub>
- **descriptive / context**: The request for payment message (pain.013) is used by customer creditors to request movement of funds from a debtor account. Industry workgroups are discussing use cases and the message is likely to gain significant traction in coming years, so it is referenced to carry data elements enabling a seamless cross-border customer credit transfer following a successful request; the related pain.014, camt.055 and camt.029 are referenced for the same purpose. (p. 26)[^original]  
  <sub>anchor: "Industry workgroups are currently actively discussing use cases for this message"</sub>
- **descriptive / context**: The bank-to-customer account report (camt.052), statement (camt.053) and debit/credit notification (camt.054) are standard account reporting messages that play an important role in cross-border payment reporting. Because they contain data elements beyond cross-border payment activity, the CPMI established harmonisation requirements only for data elements related to cross-border payment activity. (p. 26)[^original]  
  <sub>anchor: "the CPMI has established harmonisation requirements only for data elements related to cross-border payment activity"</sub>

## Annex 3: Acronyms and abbreviations

- **descriptive / definition**: The acronym table gives AML as anti-money laundering, BIC as business identifier code, and camt as cash management message. (p. 27)[^original]  
  <sub>anchor: "|AML|anti-money laundering|
|---|---|
|BIC|business identifier code|
|camt|cash management message|"</sub>
- **descriptive / definition**: In the acronym table, CBPR+ stands for Cross-border Payments and Reporting plus, CGI for common global implementation, and CtB for customer-to-bank. (p. 27)[^original]  
  <sub>anchor: "|CBPR+|Cross-border Payments and Reporting plus|
|CGI|common global implementation|
|CtB|customer-to-bank|"</sub>
- **descriptive / definition**: The table lists E&I as exceptions and investigations, FI as financial institution, and HVPS+ as High-value Payment System plus. (p. 27)[^original]  
  <sub>anchor: "|E&I|exceptions and investigations|
|FI|financial institution|
|HVPS+|High-value Payment System plus|"</sub>
- **descriptive / definition**: The table lists IP+ as Instant Payments plus, ISO as International Organization for Standardization, and LEI as Legal Entity Identifier. (p. 27)[^original]  
  <sub>anchor: "|IP+|Instant Payments plus|
|ISO|International Organization for Standardization|
|LEI|Legal Entity Identifier|"</sub>
- **descriptive / definition**: In the acronym table, MT means message type, pacs means payments clearing and settlement message, and pain means payment initiation message. (p. 27)[^original]  
  <sub>anchor: "|MT|message type|
|pacs|payments clearing and settlement message|
|pain|payment initiation message|"</sub>
- **descriptive / definition**: The table lists PMPG as Payments Market Practice Group, PSP as payment service provider, and SLA as service-level agreement. (p. 27)[^original]  
  <sub>anchor: "|PMPG|Payments Market Practice Group|
|PSP|payment service provider|
|SLA|service-level agreement|"</sub>
- **descriptive / definition**: The table lists STP as straight through processing, UETR as unique end-to-end transaction reference, UTC as Universal Time Coordinated, and XML as Extensible Markup Language. (p. 27)[^original]  
  <sub>anchor: "|STP|straight through processing|
|UETR|unique end-to-end transaction reference|
|UTC|Universal Time Coordinated|
|XML|Extensible Markup Language|"</sub>

---

[previous part](digest-003.md) | [source overview](overview.md)

[^original]: Bank for International Settlements / Basel Committee, "Harmonised ISO 20022 data requirements for enhancing cross-border payments - updated report" (2026-02-26). https://www.bis.org/publications/harmonised-iso-20022-data-requirements-enhancing-cross-border-payments-updated-report
