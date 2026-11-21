---
type: Source Digest
title: Harmonised ISO 20022 data requirements for enhancing cross-border payments - updated report - part 3 of 4 (pp. 18-23)
description: 'Verified paraphrased digest, pp. 18-23: 2. Harmonised ISO 20022 data requirements for enhanced crossborder payments > 2.3 Main components of the harmonisation requirements; 3. Implementation and maintenance; 4. Conclusion'
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
part: 3
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
digest_points: 43
---

# Harmonised ISO 20022 data requirements for enhancing cross-border payments - updated report (digest)

[previous part](digest-002.md) | [source overview](overview.md) | [next part](digest-004.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (pp. 18-23) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **international standard**.

## Potential implementation effort (Requirement 8)

- **descriptive / limitation**: Not all FIs currently have a BIC or LEI, and entities choosing to obtain them will incur some implementation costs and effort. Even in jurisdictions with lower BIC and LEI registration rates, coverage is still relatively broad; both identifiers are publicly accessible and supported by flexible registration and rigorous data quality programmes. (p. 18)[^original]  
  <sub>anchor: "Not all FIs currently have a BIC or LEI."</sub>

## Potential implementation effort (Requirement 9)

- **descriptive / finding or result**: Identifying all entities involved in a cross-border payment in a standardised, structured way supports automated straight through processing. Legacy messaging standards make it difficult for FIs to assess whether correct information on all entities has been provided, partly because information is insufficiently structured and "bulked" (for example name and postal address in one text field), which complicates screening and causes many false positives requiring manual intervention, lowering speed and raising costs. (p. 18)[^original]  
  <sub>anchor: "insufficiently structured and “bulked” information (eg name and postal address information combined in one text field)"</sub>
- **descriptive / finding or result**: ISO 20022 allows more structured and granular data than legacy standards (for example separate fields for name and address components), which, if used correctly, would facilitate screening and decrease transaction processing time. (p. 18)[^original]  
  <sub>anchor: "ISO 20022 allows for more structured and granular data to be carried compared with legacy messaging standards"</sub>

## Solution (Requirement 9)

- **expected / requirement**: Footnote 17: FATF Recommendation 16 requires that all cross-border payments or value transfers above the applicable de minimis threshold (if any) should always contain: (a) name of originator and beneficiary; (b) account number of originator and beneficiary where an account is used to process the transaction, or in its absence a unique transaction reference number permitting traceability; (c) address of the originator and the country and town name (or nearest alternative) of the beneficiary; (d) date of birth of the originator where a natural person; and (e) where originator and/or beneficiary is a legal person, where it exists, the connected BIC, or the LEI, or the unique official identifier. (p. 18)[^original]  
  <sub>anchor: "should always contain: (a) the name of the originator and beneficiary"</sub>
- **descriptive / requirement**: Requirement 9 asks that the name and postal address of entities be given in the proper, explicit structured message elements, following the harmonised data model for person/entity (ISO 20022 'Party') in the technical annex. (p. 18)[^original]  
  <sub>anchor: "Provide the name and postal address information using the appropriate and explicit structured message elements"</sub>
- **recommended / recommendation**: For the postal address under Requirement 9, it is recommended that the minimum required attributes (Country and Town Name) be supplemented, as far as possible, with others such as Street Name, Building Number and Post Code, since these may be demanded by applicable law along the end-to-end payment chain. (p. 18)[^original]  
  <sub>anchor: "it is recommended to complement the minimum required attributes"</sub>
- **permissive / recommendation**: Further address detail is always better given in structured form, but extra attributes may go in a free-formatted Address Line when that is necessary. (p. 18)[^original]  
  <sub>anchor: "additional attributes may be provided in a free-formatted Address Line if necessary"</sub>
- **expected / expectation**: The Requirement 9 solution should keep domestic implementations of structured addresses consistent. (p. 18)[^original]  
  <sub>anchor: "This solution should ensure consistency for domestic implementations of structured addresses"</sub>
- **recommended / recommendation**: For entities such as corporations, it is recommended that name and postal address be supplemented with a BIC or LEI where further information about the entity can be found via the BIC directory or the LEI database respectively. (p. 18)[^original]  
  <sub>anchor: "it is recommended to complement the Name and Postal Address information with a BIC or LEI"</sub>
- **descriptive / context**: Footnotes 15 and 16 note that Swift provides a free web-based BIC data search tool and GLEIF provides a free web-based LEI data search tool. (p. 18)[^original]  
  <sub>anchor: "Swift offers a free web-based BIC data search tool"</sub>
- **descriptive / context**: The FATF Recommendation 16 changes are expected to be fully implemented by the end of 2030, and the FATF will produce guidance to help industry prepare, expected by the end of 2026 (FATF (2025)). The CPMI's harmonised data model for persons and entities is identifier-neutral and aligned with the updated expectations, providing an early-alignment framework for the end-2030 FATF deadline while preserving flexibility in compliant identifier schemes; once FATF guidance is finalised the data model will be reviewed for consistency. (p. 19)[^original]  
  <sub>anchor: "The CPMI’s harmonised ISO 20022 data model for persons and entities is identifier-neutral"</sub>

## Link to the G20 Roadmap (Requirement 9)

- **descriptive / finding or result**: Processing with minimum required attributes in structured entity fields facilitates automation of payment and screening. Structured postal addresses and internationally recognised identifiers such as a BIC or LEI will reduce false positives and manual interventions, increasing speed. Minimum data requirements also facilitate validating whether the necessary information is provided (though not necessarily its quality), and can improve transparency and lower costs. (p. 19)[^original]  
  <sub>anchor: "will reduce the number of false positives and thus manual interventions, helping to increase the speed of a cross-border payment"</sub>
- **descriptive / limitation**: Implementation will entail some effort as communities become familiar with ISO 20022's structured, granular fields, but this aligns with what most payment systems and participants currently practise and should not impose a significant additional burden; it sets a baseline expectation. For payment systems not intending to migrate to ISO 20022, the requirement may impose additional effort to translate and populate the structured data elements. (p. 19)[^original]  
  <sub>anchor: "should not impose a significant additional burden"</sub>

## Background and rationale (Requirement 10)

- **descriptive / finding or result**: Identifying all persons involved in a cross-border payment in a standardised, structured way supports more automated straight through processing. Legacy standards make it difficult for FIs to assess whether correct information on all persons has been provided, partly because of insufficiently structured "bulked" information (for example name and postal address in one field), causing many false positives that need manual remediation, lowering speed and raising costs. ISO 20022's structured, granular data would, if used consistently, facilitate screening and decrease processing time. (p. 19)[^original]  
  <sub>anchor: "Existing legacy messaging standards make it difficult for FIs to assess whether the necessary and correct information on all persons"</sub>

## Solution (Requirement 10)

- **permissive / recommendation**: For persons, additional address attributes may be provided in a free-formatted Address Line if necessary, though structured provision is always preferred. If the full date of birth is not available, providing only the year of birth is acceptable (footnote 19: using only the year of birth requires a change to the global ISO 20022 message standard). (p. 19)[^original]  
  <sub>anchor: "providing only the year of birth is acceptable.19"</sub>
- **descriptive / requirement**: Requirement 10 asks that the name, postal address and date of birth of persons be given in the proper, explicit structured message elements, per the harmonised data model for person/entity (ISO 20022 'Party'). (p. 19)[^original]  
  <sub>anchor: "Provide the name, postal address and date of birth information using the appropriate and explicit structured message elements"</sub>
- **recommended / recommendation**: For the postal address under Requirement 10, it is recommended that the minimum attributes Country and Town Name be extended where possible with Street Name, Building Number and Post Code, as these may be required under applicable law along the end-to-end chain. (p. 19)[^original]  
  <sub>anchor: "it is recommended to complement to the extent possible the minimum required attributes"</sub>
- **permissive / recommendation**: As under Requirement 9, further address attributes may be placed in a free-formatted Address Line if necessary, although structured provision is always preferred, and the solution should keep domestic implementations of structured addresses consistent. (p. 19)[^original]  
  <sub>anchor: "additional attributes may be provided in a free-formatted Address Line if necessary"</sub>
- **descriptive / context**: Where the full date of birth is unavailable, giving only the year of birth is acceptable; footnote 19 adds that using the year alone requires a change to the global ISO 20022 message standard. (p. 19)[^original]  
  <sub>anchor: "date of birth is not available, providing only the year of birth is acceptable"</sub>
- **permissive / recommendation**: Further structured identifiers (passport, national identification and drivers' licence numbers are given as examples) may be added to, but cannot replace, the minimum required name, postal address and date of birth. (p. 19)[^original]  
  <sub>anchor: "may supplement but not substitute for the minimum required name, postal address and date of birth information"</sub>

## Link to the G20 Roadmap (Requirement 10)

- **descriptive / finding or result**: Processing with minimum data attributes in structured person fields facilitates automation of payment and screening; structured postal addresses reduce false positives and manual interventions, increasing speed; minimum data requirements facilitate validating whether necessary information is provided (not necessarily its quality), with a positive effect on costs. (p. 20)[^original]  
  <sub>anchor: "Establishing minimum data requirements facilitates validation of whether the necessary information is provided"</sub>
- **descriptive / limitation**: Implementation will entail some effort as communities become familiar with ISO 20022's structured fields; the requirement sets a baseline expectation. Additional effort may be required to capture and share information such as date of birth. (p. 20)[^original]  
  <sub>anchor: "Additional efforts may be required to capture and share information, such as date of birth."</sub>

## Background and rationale (Requirement 11)

- **descriptive / finding or result**: Unstructured addresses in cross-border payments (for example a single free-formatted field combining street name, town, postal code and country) can cause delays and additional costs, and lead to false positives due to lack of context. Structured postal address information (isolated Town Name, Postal Code, Country) allows more targeted, automated and accurate screening and reduces false positives. (p. 20)[^original]  
  <sub>anchor: "Unstructured addresses can lead to false positives due to the absence of contextual information"</sub>
- **descriptive / limitation**: Agreeing a common minimum level of postal address information is harder cross-border because address formats and conventions vary greatly across jurisdictions. Specifying a common minimum level of structured postal address information to be passed on by intermediaries throughout the chain would enhance processing. (p. 20)[^original]  
  <sub>anchor: "address formats and conventions vary greatly across jurisdictions"</sub>

## Link to the G20 Roadmap (Requirement 11)

- **descriptive / finding or result**: Structured addresses will speed up overall processing, especially by facilitating screening and preventing manual interventions (for example for sanctions checks), thereby reducing costs through enhanced straight-through processing, and provide increased transparency regarding parties involved. (p. 20)[^original]  
  <sub>anchor: "will speed up overall processing of cross-border payments, especially where it will facilitate screening processes"</sub>

## Solution (Requirement 11)

- **descriptive / requirement**: Requirement 11 asks for postal address information in structured form, steering clear of unstructured free-formatted address options wherever that is feasible. (p. 20)[^original]  
  <sub>anchor: "Provide structured postal address information, avoiding unstructured, free-formatted address options wherever feasible."</sub>
- **recommended / recommendation**: Under Requirement 11 it is recommended to supplement the minimum attributes Country and Town Name with Street Name, Building Number and Post Code as far as possible, since applicable law may require them along the end-to-end chain. (p. 20)[^original]  
  <sub>anchor: "It is recommended to complement the minimum required attributes"</sub>
- **permissive / recommendation**: Under Requirement 11, further address attributes may go in a free-formatted Address Line if necessary, though structured provision is always preferred. (p. 20)[^original]  
  <sub>anchor: "additional attributes may be provided in a free-formatted Address Line if necessary"</sub>
- **expected / expectation**: The Requirement 11 solution should maintain consistency across domestic implementations of structured addresses. (p. 20)[^original]  
  <sub>anchor: "This solution should ensure consistency in domestic implementations of structured address"</sub>

## Link to the G20 Roadmap (Requirement 11)

- **descriptive / limitation**: Persons, entities and FIs in cross-border payments, especially FIs initiating payments, may need to update systems and processes to collect, store and manage address information in a more structured way. (p. 21)[^original]  
  <sub>anchor: "may need to update their systems and processes to collect, store and manage address information"</sub>

## Potential implementation effort (Requirement 12)

- **descriptive / finding or result**: Today's proprietary standards often do not provide for structured remittance information or limit the size of remittance information that can be carried along the chain, which can cause data truncation and reconciliation difficulties between end customers. (p. 21)[^original]  
  <sub>anchor: "This can create problems such as data truncation and reconciliation difficulties between end customers."</sub>
- **descriptive / requirement**: Requirement 12: provide for the transport of customer remittance information across the end-to-end chain by enabling inclusion of a minimum size of structured or unstructured remittance information with the payment, or a reference to it when sent separately. All FIs in the chain should have minimum capabilities to include and transport remittance information. Per the harmonised data models, Remittance Information takes the form of either a single occurrence of a maximum of 140 characters of unstructured (free-formatted) remittance information, or multiple occurrences of structured Remittance Information of up to 9,000 characters (excluding XML tags). (p. 21)[^original]  
  <sub>anchor: "either a single occurrence of a maximum of 140 characters of unstructured"</sub>

## Link to the G20 Roadmap (Requirement 12)

- **descriptive / finding or result**: Automated reconciliation of cross-border payments by end customers will help improve transparency and indirectly reduce costs. FIs may need to update systems and processes to source and transmit required remittance information unaltered along the chain. (p. 21)[^original]  
  <sub>anchor: "Automated reconciliation of cross-border payments by the end customers will help improve transparency"</sub>
- **descriptive / limitation**: Footnote 20: separating remittance information from the payment may trigger delays in the chain due to lack of transparency regarding the underlying payment details. Using hyperlinks may require specific approval from relevant authorities or market-wide common standards to mitigate potential security implications. (p. 21)[^original]  
  <sub>anchor: "Separating remittance information from the payment may trigger delays in the cross-border payments chain"</sub>

## 3. Implementation and maintenance

- **descriptive / context**: Successful alignment relies on a concerted global effort to implement the harmonised data models across the cross-border payments ecosystem. Broad and consistent use of these market practice requirements will require time and sustained public-private collaboration, and widespread adoption is an important contribution to the G20 Roadmap objectives. (p. 22)[^original]  
  <sub>anchor: "will require time and sustained collaboration between the public and private sectors"</sub>
- **recommended / expectation**: The industry is encouraged to align with the requirements by the end of 2027, allowing a two-year implementation period after the MT/ISO 20022 coexistence phase ended in November 2025. Existing market practice groups (for example CBPR+, HVPS+, IP+ and local ones) are urged to incorporate the harmonisation requirements into their respective guidance. It is desirable for payment system operators and FIs to lead implementation, relying on the core message set underpinned by the harmonised data models. (p. 22)[^original]  
  <sub>anchor: "The industry is encouraged to align with these requirements by the end of 2027"</sub>
- **descriptive / context**: Collective action by end users, FIs and industry organisations is critical to aligning and structuring the information in ISO messages. The PIE task force's dedicated task team will continue to engage with payment system operators globally, and organisations providing payment-related services such as reference data solutions play a key role. (p. 22)[^original]  
  <sub>anchor: "Collective action by end users, FIs and industry organisations is critical to aligning and structuring the information"</sub>
- **descriptive / context**: The CPMI established the Harmonisation Panel for ISO 20022 to govern and maintain the requirements at least until the end of 2027, preventing the data models from becoming outdated. Its key responsibilities are (i) reviewing and, where necessary, recommending updates to the requirements or data models to the CPMI; (ii) encouraging operators and industry stakeholders to adopt them; and (iii) informing payment system stakeholders of any updates. (p. 22)[^original]  
  <sub>anchor: "The Harmonisation Panel’s key responsibilities include: (i) reviewing and, where necessary, recommending updates"</sub>
- **recommended / recommendation**: While acknowledging that regulatory reporting needs can differ by jurisdiction, the report encourages authorities to publish their requirements in standardised formats that are publicly accessible and to make full use of ISO 20022's capabilities. (p. 22)[^original]  
  <sub>anchor: "authorities are encouraged to make their requirements publicly accessible in standardised formats"</sub>

## 4. Conclusion

- **descriptive / finding or result**: Growing adoption of ISO 20022 is a crucial opportunity to promote cross-border interoperability. Compared with proprietary standards it allows richer, more structured data, improving the efficiency of transaction screening for compliance and other purposes and yielding faster, cheaper cross-border payments; the end of the Swift MT/ISO 20022 coexistence period in November 2025 has added momentum. (p. 23)[^original]  
  <sub>anchor: "improving the efficiency of transaction screening for compliance and other purposes"</sub>
- **descriptive / limitation**: Variability and inconsistency in how ISO 20022 is deployed across jurisdictions could undermine some benefits; inefficiencies are caused by misaligned message flows and inconsistent data usage along the chain, and variations in practical implementation could perpetuate frictions even as the standard is adopted. (p. 23)[^original]  
  <sub>anchor: "variations in its practical implementation could perpetuate frictions in cross-border payment processing"</sub>
- **expected / expectation**: The harmonised requirements are overarching data requirements that complement more detailed market usage guidelines. They represent ISO 20022 data use practices that, in the view of CPMI and industry messaging experts, should be consistently applied in cross-border payments to ensure the most efficient (straight through) processing, and should take effect by the end of 2027, allowing a two-year implementation period after the end of the coexistence period. (p. 23)[^original]  
  <sub>anchor: "should be consistently applied in cross-border payments to ensure the most efficient"</sub>
- **recommended / recommendation**: Realising the benefits depends critically on widespread adoption; limited or incomplete uptake would perpetuate fragmentation and hinder interoperability. Market participants are strongly encouraged to begin preparations to align with the harmonisation requirements without delay. (p. 23)[^original]  
  <sub>anchor: "market participants are strongly encouraged to begin preparations to align with the harmonisation requirements without delay"</sub>

---

[previous part](digest-002.md) | [source overview](overview.md) | [next part](digest-004.md)

[^original]: Bank for International Settlements / Basel Committee, "Harmonised ISO 20022 data requirements for enhancing cross-border payments - updated report" (2026-02-26). https://www.bis.org/publications/harmonised-iso-20022-data-requirements-enhancing-cross-border-payments-updated-report
