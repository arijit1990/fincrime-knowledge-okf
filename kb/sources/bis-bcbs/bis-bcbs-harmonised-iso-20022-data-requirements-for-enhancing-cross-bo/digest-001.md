---
type: Source Digest
title: Harmonised ISO 20022 data requirements for enhancing cross-border payments - updated report - part 1 of 4 (pp. 1-7)
description: 'Verified paraphrased digest, pp. 1-7: Table of contents; Executive summary; 1. Introduction > 1.1 Purpose of the report; and 6 more sections'
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
part: 1
parts_total: 4
content_mode: digest
generated:
  by: claude-code-subagent/claude-sonnet-5-5
  at: '2026-11-17T17:26:07Z'
verified:
- by: process:kb-digest-check/anchor-match
  at: '2026-11-17T17:26:07Z'
- by: claude-code-judge-agent/claude-opus-5-5
  at: '2026-11-17T17:26:07Z'
sources:
- id: original
  resource: https://www.bis.org/publications/harmonised-iso-20022-data-requirements-enhancing-cross-border-payments-updated-report
  title: Harmonised ISO 20022 data requirements for enhancing cross-border payments - updated report
  author: org:bis_bcbs
  last_modified: '2026-02-26T00:00:00Z'
digest_points: 23
---

# Harmonised ISO 20022 data requirements for enhancing cross-border payments - updated report (digest)

[source overview](overview.md) | [next part](digest-002.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (pp. 1-7) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **international standard**.

## Table of contents

- **descriptive / context**: The harmonisation requirements give public and private sector payment system operators and participants guidance on implementing ISO 20022 consistently, to support the Roadmap objectives of faster, cheaper, more accessible and more transparent cross-border payments. (p. 3)[^original]  
  <sub>anchor: "faster, cheaper, more accessible and more transparent cross-border payments"</sub>
- **descriptive / context**: The CPMI's harmonised ISO 20022 data requirements for enhanced cross-border payment processing (the 'harmonisation requirements') are described as a main output of the G20 Roadmap for Enhancing Cross-border Payments. (p. 3)[^original]  
  <sub>anchor: "are a key deliverable under the G20 Roadmap for Enhancing Cross-border Payments (Roadmap)"</sub>
- **descriptive / context**: ISO 20022 is presented as an international financial messaging standard that could allow payment processing to use more consistent and structured data. (p. 3)[^original]  
  <sub>anchor: "ISO 20022 is an international financial messaging standard with the potential to enable more consistent and structured data in payment processing"</sub>

## Executive summary

- **descriptive / context**: The harmonisation requirements are not, and should not be regarded as, regulatory requirements. Implementation is the decision of individual entities and is not mandatory for transmitting cross-border or domestic payments, although the CPMI encourages payment system operators and participants to implement practices that support consistent formatting and transmittal of payment messages. (p. 4)[^original]  
  <sub>anchor: "are not, and should not be regarded as, regulatory requirements"</sub>
- **descriptive / context**: Fragmentation and mixed use of payment messaging standards continue to be a major friction in cross-border payments. Using a common standard and ISO 20022's materially greater messaging capability can promote interoperability, but variability in how ISO 20022 is deployed across the globe could undercut some benefits. A joint task force of the CPMI and the Payments Market Practice Group (PMPG) defined harmonised data requirements, and the CPMI report to the G20 was published in October 2023. (p. 4)[^original]  
  <sub>anchor: "variability in the ways in which ISO 20022 is deployed across the globe could undercut some of its benefits"</sub>
- **descriptive / context**: The harmonisation requirements were guided by high-level criteria: focus on measures deemed most critical to the Roadmap objectives; neutrality with respect to cross-border payment solutions; flexibility for market participants to align at their own pace until end-2027, following the successful migration to ISO 20022 in November 2025; and requirements that are realistic and achievable within the Roadmap time frame. (p. 4)[^original]  
  <sub>anchor: "market participants have the flexibility to align their cross-border payment messaging practices"</sub>
- **descriptive / context**: Realising the benefits depends crucially on widespread and consistent implementation: limited, incomplete or inconsistent implementation could lead to further fragmentation and limit interoperability, whereas widespread alignment will generate a network effect that could encourage further uptake. The requirements further refine existing market practice guidance to be incorporated into international and local usage guidelines. (p. 4)[^original]  
  <sub>anchor: "Limited, incomplete or inconsistent implementation could lead to further fragmentation and limit interoperability."</sub>
- **descriptive / context**: The CPMI will maintain the harmonisation requirements at least until the end of 2027, during the G20 cross-border payments programme, and has set up a joint panel of members from ISO 20022 global market practice groups. The updated report takes into account standardisation and regulatory developments since 2023, clarifies points where participants sought guidance, and sets out an updated and expanded data model in a separate technical annex, allowing more regular updates in line with the ISO 20022 release schedule, if and as needed. (p. 4)[^original]  
  <sub>anchor: "The CPMI will maintain the harmonisation requirements at least until the end of 2027"</sub>

## 1.1 Purpose of the report

- **descriptive / context**: The harmonisation requirements, originally published in 2023, apply to interbank payments (where "bank" or "interbank" covers bank and non-bank payment service providers unless otherwise specified), clearing and settlement, and exceptions and investigations messages, though the approach is relevant to the entire cross-border payment chain. They were developed by a joint CPMI and PMPG task force of ISO 20022 experts and reflect comments from a public consultation by the CPMI in early 2023. (p. 5)[^original]  
  <sub>anchor: "apply to interbank payments,1 clearing and settlement, as well as exceptions and investigations messages"</sub>
- **recommended / expectation**: The CPMI believes alignment of ISO 20022 usage guidelines in cross-border payments with the harmonisation requirements may lead to improvements in cost, speed and transparency. With this updated report the CPMI recommends that payment system operators and participants continue to align their ISO 20022 usage guidelines with the requirements before the end of 2027. (p. 5)[^original]  
  <sub>anchor: "the CPMI recommends that payment system operators and participants continue to align their ISO 20022 usage guidelines"</sub>

## 1.2 Frictions from fragmented messaging standards

- **descriptive / finding or result**: The Roadmap identified fragmentation of payment messaging standards as one of the major frictions behind the high cost, slow speed and lack of transparency in cross-border payments. Interoperability across payment systems has historically been supported by the Swift Message Type (MT) standard, but translations between Swift MT and domestic proprietary standards sometimes led to data truncation and fragmentation, delaying processing and raising costs. (p. 5)[^original]  
  <sub>anchor: "translations between the Swift MT and domestic proprietary standards sometimes led to data truncation and fragmentation issues"</sub>
- **descriptive / finding or result**: Insufficient and unstructured data in some fields of the Swift MT standard, in particular for party identification, undermined automated straight through processing, slowing cross-border payments while increasing their cost. (p. 5)[^original]  
  <sub>anchor: "in particular for party identification, undermined automated straight through processing"</sub>

## 1.3 Benefits of ISO 20022 as a common international standard

- **descriptive / definition**: ISO 20022 is a global and open standard for financial information providing a common language for every kind of financial transaction, including cross-border payments, and allowing richer, more structured data to be shared via standardised messages than most current proprietary standards. (p. 5)[^original]  
  <sub>anchor: "ISO 20022 is a global and open standard for financial information."</sub>
- **descriptive / finding or result**: Structured data enhance the efficiency of transaction screening for compliance (for example sanctions and anti-money laundering) as well as other purposes such as fraud prevention. (p. 5)[^original]  
  <sub>anchor: "The structured data enhance the efficiency of transaction screening for compliance"</sub>
- **descriptive / finding or result**: The 2025 CPMI-FSB monitoring survey of central banks and other authorities indicated that 79% of both RTGS systems and fast payment systems (FPS) either have implemented or have concrete plans to implement ISO 20022 by 2027. Even where proprietary formats are retained for domestic payments, ISO 20022 design practices and the harmonisation requirements can guide evolution of domestic formats to enhance interoperability and prevent data truncation. (p. 6)[^original]  
  <sub>anchor: "79% of both real-time gross settlement (RTGS) systems and fast payment systems (FPS)"</sub>

## 1.4 Continued harmonisation challenges

- **descriptive / limitation**: Variability and inconsistency in how ISO 20022 is deployed across jurisdictions risks undermining its benefits. Many cross-border inefficiencies are caused by misaligned message flows and inconsistent data usage along the end-to-end payment chain, so frictions could persist even as ISO 20022 is adopted. (p. 6)[^original]  
  <sub>anchor: "misaligned message flows and inconsistent data usage along the end-to-end payment chain"</sub>

## 1.5 Collaboration with industry on ISO 20022 harmonisation for cross-border payments

- **descriptive / context**: A joint task force of messaging specialists from the CPMI and PMPG developed harmonisation requirements and harmonised data models (defined for this purpose as a set of requirements on minimum data elements needed to enable consistent message formats for cross-border payments) for ISO 20022 messages relevant to cross-border payments. They were published in the CPMI report of October 2023, designed to supplement existing usage guidelines and market practices and to help achieve the Roadmap's speed, cost and transparency goals. (p. 6)[^original]  
  <sub>anchor: "A joint task force comprising messaging specialists from the CPMI and the Payments Market Practice Group (PMPG)"</sub>
- **descriptive / context**: Several key market infrastructures have publicly expressed support for the harmonisation requirements. For medium-term governance and maintenance the CPMI established in 2025 a panel of global ISO 20022 market practice groups, the Harmonisation Panel for ISO 20022; this updated and extended report replaces the October 2023 report. (p. 6)[^original]  
  <sub>anchor: "the CPMI established a panel of global ISO 20022 market practice groups in 2025"</sub>

## 1.6 Organisation of the report

- **descriptive / context**: The report is organised as: Section 2 on the harmonisation requirements, their objective, guiding principles and major components (core message set and harmonisation requirements); Section 3 on efforts to align with the requirements and data models; Section 4 concluding. The harmonised data models, an integral part of the requirements, are in a technical annex and may be updated in line with the ISO 20022 release schedule, if and as needed. (p. 6)[^original]  
  <sub>anchor: "The harmonised data models, which form an integral part of the harmonisation requirements, are provided in a technical annex"</sub>

## 1.4 Continued harmonisation challenges

- **permissive / context**: If payment system operators and other providers adopt the harmonisation requirements widely, that may encourage implementation among value-chain entities reluctant to spend on updating their message standards. (p. 6)[^original]  
  <sub>anchor: "may help encourage implementation by entities in the value chain that are hesitant to invest"</sub>

## Box 1 - Current state of alignment with harmonisation requirements and future plans

- **descriptive / finding or result**: Approximately 19% of FPS and 13% of RTGS systems are currently aligned with the harmonisation requirements, and the number of aligned RTGS systems has more than doubled, driven primarily by seven systems implementing plans to align. An additional 12% of FPS and around 25% of RTGS systems plan to align in future, while around 44% of FPS and 43% of RTGS systems are considering it (based on 57 FPS and 80 RTGS systems). (p. 7)[^original]  
  <sub>anchor: "Approximately 19% of FPS and 13% of RTGS systems are currently aligned with them."</sub>
- **descriptive / finding or result**: FPS and RTGS systems in the Middle East and Africa are most likely to implement the harmonisation requirements. If systems considering or planning to align follow through, around two thirds of FPS and RTGS systems could align in the next few years. Reasons given for not planning to align included a current focus on domestic payments and alignment with other market practices or rulebooks similar to the harmonised requirements. (p. 7)[^original]  
  <sub>anchor: "around two thirds of FPS and RTGS systems could align with the harmonisation requirements in the next few years"</sub>
- **descriptive / context**: The CPMI-convened Payments Interoperability and Extension (PIE) industry task force has identified ISO 20022 harmonisation for cross-border payments as a focus area. A dedicated task team published a first report in January 2025 and an updated report is planned for early 2026. Engagement confirms strong momentum toward ISO 20022 adoption, although progress remains uneven across regions and payment domains, and a growing number of market infrastructures are expected to be fully aligned by the end of 2027 based on stated roadmaps. (p. 7)[^original]  
  <sub>anchor: "progress remains uneven across regions and payment domains"</sub>

---

[source overview](overview.md) | [next part](digest-002.md)

[^original]: Bank for International Settlements / Basel Committee, "Harmonised ISO 20022 data requirements for enhancing cross-border payments - updated report" (2026-02-26). https://www.bis.org/publications/harmonised-iso-20022-data-requirements-enhancing-cross-border-payments-updated-report
