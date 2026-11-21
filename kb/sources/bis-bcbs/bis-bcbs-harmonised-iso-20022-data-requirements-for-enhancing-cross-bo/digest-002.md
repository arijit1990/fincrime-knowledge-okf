---
type: Source Digest
title: Harmonised ISO 20022 data requirements for enhancing cross-border payments - updated report - part 2 of 4 (pp. 8-18)
description: 'Verified paraphrased digest, pp. 8-18: 2. Harmonised ISO 20022 data requirements for enhanced crossborder payments > 2.1 Objective; 2. Harmonised ISO 20022 data requirements for enhanced crossborder payments > 2.2 Guiding principles; 2. Harmonised ISO 20022 data requirements for enhanced crossborder payments > 2.3 Main components of the harmonisation requirements'
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
part: 2
parts_total: 4
content_mode: digest
generated:
  by: claude-code-subagent/claude-sonnet-5-5
  at: '2026-11-17T17:26:18Z'
verified:
- by: process:kb-digest-check/anchor-match
  at: '2026-11-17T17:26:18Z'
- by: claude-code-judge-agent/claude-opus-5-5
  at: '2026-11-17T17:26:18Z'
sources:
- id: original
  resource: https://www.bis.org/publications/harmonised-iso-20022-data-requirements-enhancing-cross-border-payments-updated-report
  title: Harmonised ISO 20022 data requirements for enhancing cross-border payments - updated report
  author: org:bis_bcbs
  last_modified: '2026-02-26T00:00:00Z'
digest_points: 58
---

# Harmonised ISO 20022 data requirements for enhancing cross-border payments - updated report (digest)

[previous part](digest-001.md) | [source overview](overview.md) | [next part](digest-003.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (pp. 8-18) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **international standard**.

## 2.1 Objective

- **descriptive / context**: The harmonisation requirements are overarching data requirements across a core set of ISO 20022 messages that complement existing market usage guidelines. They represent ISO 20022 data use practices that, when consistently applied, will improve the efficiency (straight-through processing) of cross-border payments. (p. 8)[^original]  
  <sub>anchor: "They represent ISO 20022 data use practices that, when consistently applied, will improve the efficiency"</sub>
- **descriptive / finding or result**: Existing ISO 20022 usage guidelines (for example CBPR+) are detailed, which can make it hard to identify which message elements are critical for efficient end-to-end processing. Current implementation guidance also includes compromises for phased adoption, such as allowing continued use of unstructured data, resulting in temporary underutilisation of ISO 20022's potential. (p. 8)[^original]  
  <sub>anchor: "current implementation guidance includes compromises, such as allowing the continued use of unstructured data"</sub>
- **descriptive / context**: The harmonisation requirements are set for the end of 2027, with implementation recommended even earlier where possible. They are not, and should not be, regarded as regulatory requirements; non-conformance would not result in payments being rejected, but such payments are likely to face reduced efficiency and a greater risk of failure or delay than harmonised ones. (p. 8)[^original]  
  <sub>anchor: "Non-conformance with the requirements described in this report would not result in those payments being rejected."</sub>
- **descriptive / context**: Requirements are defined for the interbank clearing and settlement messages in scope, but the joint task force also considered the end-to-end chain because efficiency depends on the quality of data provided by the customer initiating the payment. Harmonised data models for customer-to-bank payment initiation (payment and request for payment) are documented in the technical annex, and the end-to-end approach also aims to avoid misalignment across usage guidelines for initiation, interbank clearing and settlement, and reporting. (p. 8)[^original]  
  <sub>anchor: "the potential efficiency of a cross-border payment depends on the quality of data provided by the customer initiating the payment"</sub>

## 2.2 Guiding principles

- **descriptive / context**: Principle "G20 objectives-focused": the CPMI sought to recommend only requirements that relate to at least one of the Roadmap's aspects of cost, speed, access and transparency of cross-border payments, and, as the targets cover the entire chain, the requirements focus on the end-to-end payment chain. (p. 8)[^original]  
  <sub>anchor: "the CPMI has sought only to recommend requirements that relate to at least one of these aspects"</sub>

## 2.1 Objective

- **descriptive / context**: Footnote 4 notes that ISO 20022 market practice guidance was written separately by different industry bodies: CGI-MP for payment initiation and reporting, and CBPR+ (cross-border correspondent banking), IP+ (cross-border instant payments) and HVPS+ (high-value payment systems) for interbank clearing and settlement. (p. 8)[^original]  
  <sub>anchor: "Market practice guidance for the use of ISO 20022 has been defined independently by different industry organisations"</sub>

## 2.2 Guiding principles

- **descriptive / context**: Principle "Platform- and network-neutral": the requirements do not presume use of any specific cross-border payments platform, messaging network or service provider, and are not intended to tilt the playing field towards specific providers; they aim to cover broad use cases and support a level playing field. (p. 9)[^original]  
  <sub>anchor: "The requirements do not presume the use of any specific cross-border payments platform, messaging networks or service providers"</sub>
- **descriptive / context**: Principle "Orientation to a presumed future state": the requirements presume the state after the end of the MT and ISO 20022 coexistence period on 22 November 2025, after which the temporary compromises made during transition in the cross-border payments space will no longer be needed. (p. 9)[^original]  
  <sub>anchor: "end of the coexistence period between the MT and ISO 20022 standards on 22 November 2025"</sub>
- **descriptive / context**: Principle "Ambitious yet realistic": requirements are meant to be meaningful for the Roadmap objectives but realistic in effort needed to align by end-2027 and given ongoing industry work on market practice guidelines. They were calibrated using expert opinions from the joint task force, public consultation feedback and industry engagements on the basis of the greatest good for the greatest number; some more ambitious proposals were deemed too costly or not mature enough. (p. 9)[^original]  
  <sub>anchor: "on the basis of the greatest good for the greatest number"</sub>

## 2.3 Main components of the harmonisation requirements

- **descriptive / definition**: The harmonisation requirements consist of three components: a core message set, general requirements applicable to all messages in it, and minimum required data models ("harmonised data models") for individual messages in scope, which are set out in a separate technical annex. (p. 9)[^original]  
  <sub>anchor: "a core message set, general requirements and minimum required data models"</sub>

## 2.3.1 Core message set

- **descriptive / data or feature**: The core ISO 20022 message set in scope (Table 1) covers: credit transfers (pacs.008 Customer Credit Transfer, pacs.009 Financial Institution Credit Transfer, pacs.002 Payment Status Report); payment returns (camt.056 Payment Cancellation Request, camt.029 Payment Cancellation Response, pacs.004 Payment Return); and payment investigations (pacs.028 Payment Status Request, camt.110 Investigation Request, camt.111 Investigation Response). The set extends beyond credit transfers to payment return and other exception processes. (p. 10)[^original]  
  <sub>anchor: "|Cdit tf|pacs.008|Customer Credit Transfer|
|re ransers|pacs.009|Financial Institution Credit Transfer|"</sub>
- **descriptive / data or feature**: Other customer-to-bank messages inform the harmonised data models (Table 2) but are not in the core set: pain.001 Customer Credit Transfer Initiation, pain.013 Request for Payment, pain.014 Request for Payment Response, camt.055 Payment Cancellation Request (CtB) and camt.029 Payment Cancellation Response. They contain data elements that, when harmonised, may make interbank cross-border flows more efficient; requirements for them are in the technical annex. (p. 10)[^original]  
  <sub>anchor: "they contain data elements that, when harmonised, may make interbank cross-border payment flows more efficient"</sub>
- **descriptive / context**: For bank-to-customer reporting messages (camt.052, camt.053, camt.054), the requirements identify only the data elements that need to be reported to the debtor and/or creditor for cross-border payments, highlighted in bold in the credit transfer and payment return data models in the annex; no further guidance is given on them. (p. 10)[^original]  
  <sub>anchor: "the harmonisation requirements identify only the data elements that need to be reported to the debtor and/or creditor"</sub>

## 2.3.2 General requirements

- **descriptive / context**: The CPMI proposes 12 general requirements for the use of ISO 20022 for cross-border payments, applying to all messages in the core set. Several directly affect speed (requirements 1-3, 5 and 7-11) and transparency (requirements 1, 2, 4-10 and 12), and most may help lower PSP costs through improved processing efficiency (Table 3). (p. 10)[^original]  
  <sub>anchor: "the CPMI proposes 12 general requirements for the use of ISO 20022 for cross-border payments"</sub>

## Harmonisation requirements and G20 objectives

- **descriptive / context**: The 12 requirements are: Fundamental - (1) use the appropriate ISO 20022 message for a specific business function; (2) use ISO externalised codes for payments and payment-related processes; (3) support/restrict the character set to current market practice; (4) use a common time convention across all ISO 20022 messages in cross-border payments. Transparency - (5) include a unique end-to-end reference for all cross-border payments; (6) support transparency on amounts, currency conversions and charges. Data structuring - (7) include account identifiers to the extent possible; (8) uniquely identify all FIs involved in an internationally recognised and standardised way; (9) identify all entities involved in a standardised and structured way; (10) identify all persons involved in a standardised and structured way; (11) provide a common minimum level of postal address information structured to the extent possible; (12) provide for transport of customer remittance information end to end by enabling inclusion of a minimum size of structured or unstructured remittance information, or a reference to it when sent separately. (p. 11)[^original]  
  <sub>anchor: "To use the appropriate ISO 20022 message for a specific business function"</sub>
- **descriptive / method**: For each requirement the report explains the business rationale, the technical solution at ISO 20022 message level, the benefits for enhanced cross-border payments, and an estimate of overall implementation effort based on input from the Harmonisation Panel. (p. 11)[^original]  
  <sub>anchor: "an estimate of the overall effort required to implement the proposed solution"</sub>

## Background and rationale (Requirement 1)

- **descriptive / finding or result**: There is some risk of inconsistent use of ISO 20022 messages or deviation from their scope, which can undermine processing efficiency. For example, instead of the return message pacs.004, some markets use a regular credit transfer message (pacs.008 or pacs.009) with customised proprietary coding to identify it as a return, forcing FIs working across markets to perform the same business function in different ways. (p. 12)[^original]  
  <sub>anchor: "certain markets opt to use a regular credit transfer message"</sub>

## Solution (Requirement 1)

- **descriptive / expectation**: Use of the ISO 20022 messages in the core set for cross-border payments, in accordance with their scope as defined by the standard, is expected to resolve the problem, improve processing speed by reducing processing times and enhance transparency. Harmonised usage may indirectly help lower costs by reducing bespoke mapping and letting PSPs access the market through a wider choice of solution providers. (p. 12)[^original]  
  <sub>anchor: "is expected to improve the speed of cross-border payments by reducing processing times"</sub>

## Potential implementation effort (Requirement 1)

- **descriptive / context**: ISO 20022 message scopes are defined under the ISO 20022 methodology and endorsed by the ISO 20022 Registration Management Group, so conforming should not cause friction. Jurisdictions may provide certain business functions through alternative solutions (for example APIs or proprietary formats aligned with the harmonised data models) without compromising efficiency, and the requirement does not preclude such solutions. (p. 12)[^original]  
  <sub>anchor: "This requirement does not preclude the use of such alternative solutions."</sub>
- **descriptive / context**: ISO 20022 messages are maintained yearly and harmonised data models should be documented on the latest available release. Whether a new release requires a change to the data models depends on whether enhancements are relevant to cross-border efficiency and whether commonly agreed industry best practices have evolved to require revision. (p. 13)[^original]  
  <sub>anchor: "the harmonised data models for the CPMI core message set should be documented based on the latest available release"</sub>
- **recommended / expectation**: Whether a jurisdiction upgrades to the latest ISO 20022 release in a given year depends on factors including whether it has identified a need to do so and whether changes to the harmonised data models can be accommodated within its current message version while preserving data integrity. If data integrity cannot be preserved, the jurisdiction should consider upgrading to a more recent release. (p. 13)[^original]  
  <sub>anchor: "the jurisdiction should consider upgrading to a more recent ISO 20022 release."</sub>
- **expected / expectation**: Footnote 6: elements introduced in the latest release that are new mandatory elements deemed necessary by the broader community to be carried end to end, or are subject to harmonised data model restrictions (R, RC or C in the annex column), are subject to preserving data integrity, and jurisdictions should plan an upgrade to the release introducing them. New mandatory elements not deemed necessary end to end, and new optional elements with no restriction (blank) or not allowed (N), may not necessitate an upgrade. (p. 13)[^original]  
  <sub>anchor: "Jurisdictions should plan for an upgrade to the release of the ISO 20022 message where these elements are introduced"</sub>

## Background and rationale (Requirement 2)

- **descriptive / finding or result**: ISO 20022 allows information to be given through globally agreed externalised codes or locally defined proprietary codes. Proprietary codes increase the risk of misunderstanding and the need for human intervention, reducing the potential for automated processing. (p. 13)[^original]  
  <sub>anchor: "Use of proprietary codes increases the risk of misunderstanding and the need for human intervention"</sub>
- **descriptive / context**: Registered ISO 20022 externalised codes facilitate common understanding (for example purpose code "PENS" unambiguously identifies a pension payment). Bilaterally and multilaterally agreed proprietary codes may continue to be used for point-to-point information beyond the harmonised data models; such use does not necessarily inhibit automated processing and can be considered (for example a service level proprietary code referring to a bilateral agreement). (p. 13)[^original]  
  <sub>anchor: "may continue to be used to communicate point-to-point information that is beyond the harmonised data models"</sub>

## Link to the G20 Roadmap (Requirement 2)

- **descriptive / finding or result**: Using ISO 20022 codes from published lists lets all parties unambiguously understand the information, increasing end-to-end speed and transparency and preventing manual intervention and interpretation where externalised codes may be used (for example externalised payment purpose codes identifying the underlying nature of a payment). (p. 13)[^original]  
  <sub>anchor: "all those involved in the processing of a cross-border payment can unambiguously understand the information"</sub>
- **descriptive / context**: Footnote 7: externalised codes are published with definitions on iso20022.org so code lists can be updated without changing message schemas or requiring communities to upgrade message versions; requests to add codes are validated and approved by ISO 20022 Standard Evaluation Groups (SEGs) of industry experts that review lists quarterly. Footnote 8: not all codes are externalised in the latest core message set; some remain embedded in the schema, and using these globally agreed codes is perfectly acceptable. (p. 13)[^original]  
  <sub>anchor: "Any request to add codes is subject to validation and approval by the ISO 20022 Standard Evaluation Groups"</sub>

## Potential implementation effort (Requirement 2)

- **permissive / context**: Codes that are used purely domestically may stay unregistered provided they do not harm interoperability or create data quality problems for cross-border transactions. (p. 13)[^original]  
  <sub>anchor: "Codes used solely for domestic purposes can remain unregistered, if they do not impair interoperability"</sub>
- **expected / expectation**: Even where domestic-only codes remain unregistered, jurisdictions should still publish them so that they are publicly available. (p. 13)[^original]  
  <sub>anchor: "Jurisdictions should still make these codes publicly available."</sub>
- **expected / expectation**: Implementation effort for externalised codes varies by market and may be more significant where proprietary codes relevant to the cross-border leg are used and systems must be adjusted. PSPs should provide guidance on how to map current proprietary codes to ISO 20022 externalised codes, and should address gaps, if any, by requesting registration and publication of additional codes on the externalised lists. (p. 14)[^original]  
  <sub>anchor: "PSPs should provide guidance on how to map current proprietary codes to ISO 20022 externalised codes"</sub>

## Background and rationale (Requirement 3)

- **descriptive / finding or result**: Efficient cross-border processing depends on a common character set so all participants can interpret information; otherwise payments risk being delayed or even returned. (p. 14)[^original]  
  <sub>anchor: "Otherwise, payments risk being delayed or even returned."</sub>
- **descriptive / requirement**: Requirement 3: use a restricted character set in cross-border payment messages limited to the currently agreed Latin character set (lower case a-z, upper case A-Z, numerals 0-9), complemented for a limited selection of data elements, as allowed by the CBPR+ usage guidelines, by the characters / - ? : ( ) . , ' + ! # & % * = ^ _ ` { | } ~ " ; @ [ \ ] $ > <. It applies to free-formatted text elements for person, entity and FI name and address information and remittance information. (p. 14)[^original]  
  <sub>anchor: "Use of a restricted character set in cross-border payment messages limited to the currently agreed Latin character set"</sub>

## Solution (Requirement 3)

- **recommended / recommendation**: It is recommended that jurisdictions add local language mapping where necessary to facilitate efficient processing of inward and outward cross-border payments. The CPMI may re-evaluate the character set in future through consultations with market practice groups. (p. 14)[^original]  
  <sub>anchor: "It is also recommended that jurisdictions add local language mapping where necessary"</sub>
- **descriptive / finding or result**: A common character set will primarily support the speed of cross-border payments, with an indirect impact on reducing costs over the longer term. Implementation effort is estimated to be low since the restricted set is today the default convention. Domestic or regional jurisdictions allowing a broader character set agree and publish guidance on converting broader characters into the restricted set for the cross-border leg. (p. 14)[^original]  
  <sub>anchor: "The level of effort required to implement this requirement is estimated to be low"</sub>

## Potential implementation effort (Requirement 4)

- **descriptive / finding or result**: Inconsistent use of time indications in ISO 20022 messages may cause confusion and complicate meeting time-sensitive processing requests. (p. 14)[^original]  
  <sub>anchor: "The inconsistent use of time indications in ISO 20022 messages may cause confusion"</sub>
- **descriptive / requirement**: Requirement 4 (common time convention): use either Universal Time Coordinated (UTC) or local time with a UTC offset. A standardised approach supports the G20 target for increased speed and transparency in processing times. (p. 14)[^original]  
  <sub>anchor: "The use of either Universal Time Coordinated (UTC) or local time with a UTC offset."</sub>
- **descriptive / context**: The effort to implement the time convention requirement is not expected to be large, since it only asks for time conventions that most systems and solutions already widely support in order to state times unambiguously. (p. 14)[^original]  
  <sub>anchor: "The implementation effort is not expected to be significant, as the requirement simply calls for using time conventions"</sub>
- **expected / expectation**: Payment systems and solution providers are expected to support a minimum of one time convention (UTC, local time with a UTC offset, or both); they need not support every convention that ISO 20022 offers. (p. 14)[^original]  
  <sub>anchor: "Payment systems and solution providers are expected to support at least one convention, not necessarily all conventions"</sub>

## Background and rationale (Requirement 5)

- **descriptive / requirement**: Requirement 5: use the unique end-to-end transaction reference (UETR), as defined in technical standard RFC 4122 (version 4), as the unique identification for all cross-border payments. (p. 15)[^original]  
  <sub>anchor: "Use of the unique end-to-end transaction reference (UETR), as defined in the technical standard RFC 4122 (version 4)"</sub>
- **descriptive / finding or result**: Using the UETR enables easier tracking and improves transparency, simplifies exception and investigation (E&I) handling and facilitates automated processing that enhances speed, and is expected to indirectly reduce costs through automation of E&I management. (p. 15)[^original]  
  <sub>anchor: "It will also simplify exception and investigation (E&I) handling"</sub>

## Link to the G20 Roadmap (Requirement 5)

- **descriptive / context**: Footnote 10: the UETR complies with RFC 4122 (version 4) created by the IETF; no centralised authority is needed to administer unique identifications because UETRs can be generated by a decentralised algorithm. The UETR is one implementation example of the universally unique identifiers (UUIDs) defined in RFC 4122 (version 4) and documented under ISO 9834-8:2005, which are easy to implement from an IT perspective. (p. 15)[^original]  
  <sub>anchor: "An advantage of the UETR is that no centralised authority is required to administer the creation of unique identifications"</sub>

## Background and rationale (Requirement 5)

- **descriptive / finding or result**: So that entities can readily track and reconcile a cross-border payment, the message must carry a unique, unambiguous reference from end to end; the transaction identification typically used for this does not guarantee uniqueness across all cross-border payments and all the entities involved. (p. 15)[^original]  
  <sub>anchor: "is not sufficient to ensure uniqueness across all cross-border payments and involved entities"</sub>

## Potential implementation effort (Requirement 5)

- **descriptive / limitation**: Although UETR use has become common for some communities, usage throughout the whole chain (including generation by corporations or PSPs on the originator's behalf and end-to-end transmission) could entail some cost and effort. (p. 16)[^original]  
  <sub>anchor: "could entail some cost and effort"</sub>
- **descriptive / finding or result**: Cross-border payments often lack transparency on total costs; proprietary messaging standards do not necessarily enable or require complete information on the amount instructed by the payer, currency conversions applied or processing charges levied along the chain. (p. 16)[^original]  
  <sub>anchor: "Cross-border payments often lack transparency on the total costs of the payment."</sub>

## Link to the G20 Roadmap (Requirement 6)

- **descriptive / finding or result**: The requirement enhances transparency through complete, structured information from the amount instructed by the payer, any currency conversion and FI charges. Increased transparency could indirectly affect costs through increased competition as end users learn the costs of different FIs. (p. 16)[^original]  
  <sub>anchor: "Increased transparency could also indirectly affect costs because of increased competition"</sub>
- **descriptive / limitation**: To include complete amount and charge information, some FIs may need to update systems if they perform currency conversions as an agent or take charges, and complete transparency could have major implications for business models and competition among FIs providing cross-border payment services. (p. 16)[^original]  
  <sub>anchor: "could have major implications for business models and competition among FIs"</sub>
- **descriptive / context**: Footnote 12: fees charged by the PSP providing the account to the account owner via account analysis or billing are not covered. The current agent can only see previous agents' charges and currency conversion, not the next agents' charges, and requirement 6 does not require the first agent to acquire all fee and conversion information before payment initiation, although local requirements may require it. (p. 16)[^original]  
  <sub>anchor: "requirement 6 does not require the first agent to acquire all fee and conversion information prior to the payment initiation"</sub>

## Background and rationale (Requirement 7)

- **descriptive / finding or result**: The lack of unique account identifiers can result in misdirection or return of payments; remediation usually requires manual intervention to identify the person or entity to be credited, slowing processing and potentially raising costs. (p. 16)[^original]  
  <sub>anchor: "The lack of unique identifiers for accounts can potentially result in the misdirection or return of payments."</sub>

## Potential implementation effort (Requirement 6)

- **descriptive / requirement**: Requirement 6 on transparency: a cross-border payment is to include the amount and currency instructed by the payer, any currency conversion applied to that amount, any charges deducted by any FI handling the payment along the chain, and the interbank settlement amount. (p. 16)[^original]  
  <sub>anchor: "Provide the following elements in a cross-border payment: the amount and currency of the payment as instructed by the payer"</sub>
- **mandatory / requirement**: Under the same requirement, every element other than the interbank settlement amount must pass along the whole payment chain without alteration. (p. 16)[^original]  
  <sub>anchor: "Except for the interbank settlement amount, all other information must be carried unchanged along the end-to-end payment chain"</sub>

## Solution (Requirement 7)

- **descriptive / finding or result**: Correct account information should increase processing efficiency, raise the proportion of payments processed faster, reduce returns and misapplied payments and cut exceptions and investigations, potentially lowering costs. Impact should be very limited as most payments already carry account identifiers, though jurisdictions and entities not using unique account identifiers may incur costs and effort. (p. 17)[^original]  
  <sub>anchor: "Correct account information will reduce the number of returns and misapplied payments"</sub>

## Background and rationale (Requirement 8)

- **descriptive / finding or result**: Identification and routing of FIs may be complicated where jurisdiction-specific FI identification schemes are used for specific corridors, forcing parties to consult local databases or use name and address information. Internationally recognised standardised identifiers with global directories enhance message flow, and easier validation and screening of FI information could facilitate pre-validation and reduce the risk of costly late rejections. (p. 17)[^original]  
  <sub>anchor: "reduce the risk of costly rejections late in the life cycle of a cross-border payment"</sub>

## Link to the G20 Roadmap (Requirement 8)

- **descriptive / finding or result**: Globally standardised, publicly available identifiers such as the BIC (where possible with the LEI) increase processing speed by facilitating validation, routing and screening, and are likely to reduce false positives from compliance screening filters (for example sanctions checks and AML screening). Eliminating ambiguity over FI identification directly improves transparency, and fewer manual interventions indirectly lower costs. (p. 17)[^original]  
  <sub>anchor: "is likely to reduce the number of false positives by compliance screening filters"</sub>

## Solution (Requirement 7)

- **descriptive / requirement**: Requirement 7: where available, a structured account identifier, or a proxy identifier for the account, is to be given, in order to support straight through processing (STP) and cut errors in payment processing. (p. 17)[^original]  
  <sub>anchor: "Provide a structured account identifier (or proxy identifier for the account) where available"</sub>

## Solution (Requirement 8)

- **descriptive / requirement**: Requirement 8: the FIs involved in a cross-border payment are to be identified by their BIC, the globally recognised, publicly available business identifier code defined in ISO 9362. (p. 17)[^original]  
  <sub>anchor: "Identify FIs involved in cross-border payments via the globally recognised and publicly available business identifier code (BIC)"</sub>
- **recommended / recommendation**: Using the legal entity identifier (LEI) defined in ISO 17442 alongside the BIC as an additional FI identifier is encouraged. (p. 17)[^original]  
  <sub>anchor: "complementary FI identifier to the BIC, is encouraged"</sub>
- **descriptive / context**: The FI identification requirement, as detailed in the technical annex in the harmonised data model for FIs (ISO 20022 'Agent'), will be reviewed each year to reflect regulatory changes and how well the identifiers support efficient payment routing and screening along the chain. (p. 17)[^original]  
  <sub>anchor: "will be reviewed annually to reflect regulatory changes, and the status of the identifiers"</sub>

## Link to the G20 Roadmap (Requirement 8)

- **descriptive / definition**: Footnote 13 says a BIC has eight or 11 characters, and for unique, unambiguous identification of the FI it may need the 11-character form so that the branch identification is explicit. (p. 17)[^original]  
  <sub>anchor: "the BIC may need to comprise 11 characters to explicitly include the branch identification"</sub>
- **descriptive / context**: Footnote 14 records that, following requests in a 2023 public consultation, the October 2023 report treated the BIC and LEI as equally recognised and publicly accessible ISO identifiers from the data-model viewpoint; the Harmonisation Panel accepts that current market practice and adoption levels call for at least the BIC, while acknowledging the benefits of the LEI as an added identifier. (p. 17)[^original]  
  <sub>anchor: "existing market practices and adoption rates require at least the BIC"</sub>

---

[previous part](digest-001.md) | [source overview](overview.md) | [next part](digest-003.md)

[^original]: Bank for International Settlements / Basel Committee, "Harmonised ISO 20022 data requirements for enhancing cross-border payments - updated report" (2026-02-26). https://www.bis.org/publications/harmonised-iso-20022-data-requirements-enhancing-cross-border-payments-updated-report
