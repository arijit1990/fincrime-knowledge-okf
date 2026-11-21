---
type: Source Digest
title: The Wolfsberg Group - Payment Transparency Standards - part 1 of 3 (p. 1)
description: 'Verified paraphrased digest, p. 1: Introduction; The Standards; The Standards > 1. The PMI(s) and the competent authority(ies); and 2 more sections'
resource: https://wolfsberg-group.org/resources/correspondent-banking/136
tags:
- correspondent_banking
- industry_practice
- intl
- standard
status: stable
source_id: wolfsberg-the-wolfsberg-group-payment-transparency-standards
issuer: wolfsberg
issuer_name: Wolfsberg Group
jurisdictions:
- INTL
tier: 2
instrument_type: standard
normative_force: industry_practice
publication_date: '2023'
legal_status: current
part: 1
parts_total: 3
content_mode: digest
generated:
  by: claude-code-subagent/claude-sonnet-5-5
  at: '2026-11-17T17:28:50Z'
verified:
- by: process:kb-digest-check/anchor-match
  at: '2026-11-17T17:28:50Z'
- by: claude-code-judge-agent/claude-opus-5-5
  at: '2026-11-17T17:28:50Z'
sources:
- id: original
  resource: https://wolfsberg-group.org/resources/correspondent-banking/136
  title: The Wolfsberg Group - Payment Transparency Standards
  author: org:wolfsberg
digest_points: 96
---

# The Wolfsberg Group - Payment Transparency Standards (digest)

[source overview](overview.md) | [next part](digest-002.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (p. 1) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **industry practice**.

## Introduction

- **descriptive / context**: The Wolfsberg Group has always viewed payment transparency as a foundational element of an effective financial crime compliance programme, beginning with its support for FATF Special Recommendation VII on wire transfers in its 2002 Statement on the Suppression of the Financing of Terrorism, and developed in its 2007 Statement on Payment Message Standards (made jointly with The Clearing House Association). (p. 1)[^original]  
  <sub>anchor: "payment transparency as a foundational element to an effective financial crime compliance programme"</sub>
- **descriptive / context**: The Group provided significant institutional support to SWIFT (and partnering competent authorities) in embedding the MT202COV, and most recently published Payment Transparency Standards in 2017, which included strong advocacy for ISO 20022. (p. 1)[^original]  
  <sub>anchor: "significant institutional support to SWIFT (and partnering competent authorities) in embedding the MT202COV"</sub>
- **descriptive / context**: Since 2017, innovation in payment services and open banking has pushed the international financial system to be more efficient, competitive and inclusive, but the associated operational and financial crime risks have not necessarily always been quantified. (p. 1)[^original]  
  <sub>anchor: "the associated operational and financial crime risks have not necessarily always been quantified"</sub>
- **descriptive / context**: The Group decided to replace the 2017 Payment Transparency Standards to reflect the evolution in payment methods, infrastructure and landscape, building on the 2017 document and maintaining the same basic criteria and definitions of formatting payment message information. (p. 1)[^original]  
  <sub>anchor: "maintaining the same basic criteria and definitions of formatting payment message information"</sub>
- **descriptive / definition**: The revised Standards use terminology applicable across the industry, including new market entrants who may not be regulated to the same degree as banks: FIs are referred to as "payment service providers" (PSPs); in line with ISO 20022, the ordering FI or payer PSP is the "debtor agent PSP", the intermediary FI the "intermediary agent PSP", and the beneficiary FI or payee PSP the "creditor agent PSP", whether the agent is a bank or non-bank FI (NBFI). (p. 1)[^original]  
  <sub>anchor: "the ordering FI or payer PSP is defined as the “debtor agent PSP”"</sub>
- **descriptive / limitation**: The revised Standards begin to identify how capabilities within the ISO 20022 structure can be used to enhance payment transparency, though such advances are recognised as becoming widespread only as adoption of, and adherence to, ISO 20022 increases. (p. 1)[^original]  
  <sub>anchor: "such advances will only become widespread as adoption of, and adherence to, ISO 20022 standards increases"</sub>
- **descriptive / context**: The revised Standards expand the list of key stakeholders to include payment market infrastructures (PMIs) and their competent authorities, recommending specific areas where clearer guidance from these actors would result in better harmonisation in applying payment transparency standards across PSPs. (p. 1)[^original]  
  <sub>anchor: "Expand the list of key stakeholders previously addressed by the Standards to include payment market infrastructures (PMIs)"</sub>
- **descriptive / context**: The revised Standards re-establish the core principle that a payment is a payment, so the debtor agent (the ordering FI), bank or non-bank, maintains the obligation to ensure a new payment is structured appropriately, identifying clearly the debtor and creditor in any transfer of funds. (p. 1)[^original]  
  <sub>anchor: "a payment is a payment, and as such the debtor agent (the ordering FI)"</sub>
- **descriptive / context**: The revised Standards clarify the roles and responsibilities of the intermediary agent and the creditor agent, including their limited ability to identify suspicious activity and/or conduct sanctions screening when the information accompanying a payment is limited. (p. 1)[^original]  
  <sub>anchor: "including their limited ability to identify suspicious activity and/or conduct sanctions screening"</sub>
- **descriptive / context**: Payment flow diagrams (Appendix A) identify payment transparency challenges, including payments with high levels of intermediation, several individual payments bundled into a single message instruction (especially cross-border), payments associated with "goods and services", and payments that appear domestic but are actually cross-border. (p. 1)[^original]  
  <sub>anchor: "situations where a payment that may appear to be domestic in nature is actually a cross-border payment"</sub>

## The Standards

- **expected / expectation**: The Payment Standards should apply to cross-border payments; domestic payments, as applicable under local regulations, including domestic PMIs; all fiat currencies, including digital representations of fiat currencies such as Central Bank Digital Currencies (CBDCs); payments regardless of value; and debtor, intermediary and creditor agent PSPs. (p. 1)[^original]  
  <sub>anchor: "These Payment Standards should apply to"</sub>
- **expected / expectation**: The Standards' coverage of payments regardless of value includes transactions using a credit, debit or prepaid card where the underlying intent of the transaction is to effect a person-to-person transfer of funds. (p. 1)[^original]  
  <sub>anchor: "where the underlying intent of the transaction is to effect a person-to-person transfer of funds"</sub>
- **descriptive / context**: The Standards recognise instances where local regulation establishes practical exceptions or exemptions to traditional payment transparency requirements (e.g., card transactions for the purchase of goods or services), highlight the risk of misuse of these provisions, and propose additional guidance on the roles and responsibilities for interpreting the correct application of such exclusions. (p. 1)[^original]  
  <sub>anchor: "the Standards highlight the risk of misuse of these provisions"</sub>
- **descriptive / context**: The Standards will be of use to parties working on new payment methods and platforms, payments and compliance specialists, and parties drafting regulation and regulatory guidance on information requirements for funds transfers. (p. 1)[^original]  
  <sub>anchor: "parties drafting regulation and regulatory guidance to address information requirements on funds transfers"</sub>
- **descriptive / context**: The sections that follow address applicability, roles and responsibilities across key stakeholders: (1) the PMI(s) and the competent authority(ies); (2) all PSPs irrespective of role; (3) debtor agent PSPs; (4) intermediary agent PSPs; and (5) creditor agent PSPs. (p. 1)[^original]  
  <sub>anchor: "(2) all PSPs, irrespective of their role in the payment chain"</sub>

## 1. The PMI(s) and the competent authority(ies)

- **expected / expectation**: Clarity is required for PSPs on the permissible activity that may pass through a PMI and on the roles and responsibilities of the debtor, intermediary and creditor agent PSPs in channelling and receiving funds through it. (p. 1)[^original]  
  <sub>anchor: "Clarity is required for PSPs on the permissible activity that may pass through a PMI"</sub>
- **expected / expectation**: The PMI rulebook should also clearly state the compliance obligations of the debtor, intermediary and creditor agent PSPs in their relationship with the PMI. (p. 1)[^original]  
  <sub>anchor: "should also clearly state the compliance obligations of the debtor, intermediary and creditor agent PSPs"</sub>
- **recommended / recommendation**: The rule-setting body of the PMI should consider ensuring that the financial crime compliance and payment transparency roles and responsibilities of all PMI participants (direct, indirect, agents, sponsored, "reachable BIC" participants and similar), and any associated due diligence requirements, are defined, including for PSPs not formally registered with the PMI that use correspondent relationships with PMI participants to settle payments via the PMI. (p. 1)[^original]  
  <sub>anchor: "roles and responsibilities of all participants associated with the PMI"</sub>
- **recommended / recommendation**: The rule-setting body of the PMI should consider establishing the levels of intermediation permitted by PMI participants and how they are captured in supported message formats, with guidance explicitly addressing, if applicable, cases where permitted intermediation exceeds the field or character space available to capture all intermediary agent PSPs, and instances where the payment started in a different PMI, if permitted. (p. 1)[^original]  
  <sub>anchor: "Establishing the levels of intermediation permitted by PMI participants"</sub>
- **recommended / recommendation**: The rule-setting body of the PMI should consider determining what types of payments may be cleared via the PMI and the corresponding formatting requirements, which may include a provision for PSPs to indicate cross-border payments (including combinations of internal net settlement cross-border payments and domestic PMIs), bundled payments, use of structured data to improve data quality, and payments for the purchase of "goods or services" where distinct approaches to transparency may be permitted. (p. 1)[^original]  
  <sub>anchor: "Determining what types of payments are permitted to be cleared via the PMI"</sub>
- **recommended / recommendation**: The rule-setting body of the PMI should consider identifying technological enhancements for evolving payments and settlements, such as adding fields or character space to capture intermediary agent PSPs and additional information on cross-border, bundled or goods-and-services card payments, or indicators for domestic payments that originated cross-border; these enhancements are indispensable for PSPs to uphold many of the Standards. (p. 1)[^original]  
  <sub>anchor: "These technological enhancements are indispensable for PSPs to be able to uphold many of the Standards"</sub>
- **expected / expectation**: Special attention should be placed on distinguishing forms of bundling: "one-to-many" (e.g., salary disbursements) or "many-to-one" (e.g., merchant servicing), where the risks are less significant, versus "many-to-many" (e.g., remittances from various debtors bundled into a single payment then unbundled at destination to pay several creditors), which leads to less transparency for intermediary agent PSPs and increased risk, particularly with cross-border payments. (p. 1)[^original]  
  <sub>anchor: "to “many-to-many” (e.g. remittances from various debtors/originators bundled into a single payment"</sub>
- **expected / expectation**: The competent authority should be responsible for clarifying the criteria a debtor agent PSP must apply in determining whether a card, digital wallet, electronic money instrument or similar device is used for a purchase of goods or services as opposed to a person-to-person transfer, and the distinction between a "top up" of an available balance on a payment application or wallet (normally domestic) and the later instruction of those funds to a creditor in a person-to-person transfer (especially when cross-border). (p. 1)[^original]  
  <sub>anchor: "Providing clarity on the criteria that a debtor agent PSP must apply in determining"</sub>
- **expected / expectation**: It is critical that the competent authority recognises, in guidance, supervisory activity and enforcement, how methods that limit transparency in a payment (which are permitted by regulation) impact the effectiveness of intermediary and creditor agent PSP controls for monitoring suspicious activity and enforcing sanctions compliance; this understanding should be reflected in rules promulgated by the authority and in supervisory examinations. (p. 1)[^original]  
  <sub>anchor: "It is critical that the competent authority recognises in guidance, in their supervisory activity, and in enforcement"</sub>
- **expected / expectation**: Intermediary agent PSPs can only be expected to conduct real time sanctions screening on the information included in the message, and should not be held responsible, for instance, for enforcing sanctions compliance for multiple underlying debtors or creditors in a "many-to-many" bundled payment where debtor or creditor information is not provided. (p. 1)[^original]  
  <sub>anchor: "can only be expected to conduct real time sanctions screening on the information that is included in the message"</sub>

## 2. All PSPs, irrespective of their role in the payment chain

- **expected / expectation**: PSPs should accurately reflect the roles of all participating parties and agents in appropriate fields to the fullest extent permitted by the PMI, pending technological enhancements by PMIs (e.g., in transitioning to ISO 20022). (p. 1)[^original]  
  <sub>anchor: "PSPs should accurately reflect the roles of all participating parties and agents in appropriate fields"</sub>
- **expected / expectation**: Payment information should be readily understandable by parties in the payment chain, in accordance with applicable laws and regulations, the PMI's rulebook and the message format, such that the next PSP in the chain can monitor and screen all parties effectively, even in circumstances of high payment intermediation. (p. 1)[^original]  
  <sub>anchor: "Payment information should be readily understandable by parties in the payment chain"</sub>
- **expected / expectation**: PSPs should ensure that products and services provided to their FI and non-FI customers meet the PSP's own payment transparency requirements. (p. 1)[^original]  
  <sub>anchor: "PSPs should ensure that products and services provided to their FI and non-FI customers"</sub>
- **expected / expectation**: PSPs should adopt payment transparency requirements consistent with these Standards and strongly encourage compliance with these requirements through their relationships with other PSPs. (p. 1)[^original]  
  <sub>anchor: "PSPs should adopt payment transparency requirements consistent with these Standards"</sub>

## 3. Debtor agent PSPs – ordering institutions/payer PSPs

- **descriptive / expectation**: The debtor agent PSP is responsible for identifying, verifying and conducting CDD on its customers (including any non-customer user of its origination services, e.g., an occasional transaction or walk-in customer), and related record keeping in line with all applicable regulations. (p. 1)[^original]  
  <sub>anchor: "Identifying, verifying, and conducting customer due diligence (CDD) on its customers"</sub>
- **descriptive / expectation**: The debtor agent PSP is responsible for ensuring that messages contain all required information in compliance with FATF Recommendation 16, or as stipulated by applicable local regulations and guidance. (p. 1)[^original]  
  <sub>anchor: "Ensuring that messages contain all required information in compliance with FATF Recommendation 16"</sub>
- **descriptive / expectation**: The debtor agent PSP is responsible for determining, based on the information provided by the debtor in the payment message, whether the payments represent potentially suspicious activity or violate applicable sanctions programmes. (p. 1)[^original]  
  <sub>anchor: "if the payments represent potentially suspicious activity or violate applicable sanctions programmes"</sub>
- **descriptive / expectation**: The debtor agent PSP is responsible for maintaining adequate records that permit the reconstruction of messages as required by local regulations. (p. 1)[^original]  
  <sub>anchor: "Maintaining adequate records that permit the reconstruction of messages"</sub>
- **descriptive / expectation**: The debtor agent PSP is responsible for implementing reasonable controls to determine whether the intent of the payment is domestic or cross-border, indicating that intent clearly in the message where appropriate tags/fields are available and to the fullest extent permitted by the relevant PMI, and providing all required information as required by applicable laws, regulations and guidance. (p. 1)[^original]  
  <sub>anchor: "Implementing reasonable controls to determine if the intent of the payment is domestic or cross-border"</sub>
- **descriptive / expectation**: The debtor agent PSP is responsible, to the fullest extent permitted by the PMI, for using the fields available in the payment message according to their intended purpose so all PSPs can identify and understand payment information, including using the Legal Entity Identifier (LEI) or Bank Identifier Code (BIC) or equivalent reference codes where permitted and available, and using the correct payment message for the type of payment while maximising available capabilities (e.g., category purpose codes under ISO 20022). (p. 1)[^original]  
  <sub>anchor: "using Legal Entity Identifier (LEI) or Bank Identifier Code (BIC) or equivalent reference codes"</sub>
- **descriptive / expectation**: The debtor agent PSP is responsible for applying the appropriate criteria, as determined by the competent authority and PMI rulebook, on bundling (opting to bundle a series of payments into one payment under a "one-to-many", "many-to-one" or "many-to-many" scenario), in accordance with its business model. (p. 1)[^original]  
  <sub>anchor: "Applying the appropriate criteria, as determined by the competent authority and associated PMI rulebook, on bundling"</sub>
- **descriptive / expectation**: The debtor agent PSP is responsible for adopting applicable regulatory exceptions or exemptions that permit distinct types of information in a payment because of its status as a purchase of a "good or service" (e.g., goods and services purchased via credit cards). (p. 1)[^original]  
  <sub>anchor: "Adopting applicable regulatory exceptions or exemptions that permit distinct types of information in a payment"</sub>
- **descriptive / expectation**: The debtor agent PSP's responsibilities also extend to cases where it applies a collection agent model, in which the debtor or creditor agent PSP considers the funds "their own" and plays the role of the actual debtor or creditor, and to initiating what will ultimately be a cross-border payment using domestic PMIs. (p. 1)[^original]  
  <sub>anchor: "whereby the debtor or creditor agent PSP considers the funds “their own”"</sub>
- **expected / expectation**: To ensure technical formatting requirements are met, the debtor agent PSP should, as the ordering institution, include the Name, Address and Account number of the debtor (the originator) as the preferred approach to comply with local laws and regulations, which generally align to FATF Recommendation 16 guidance. (p. 1)[^original]  
  <sub>anchor: "Include Name, Address and Account number of the debtor, who is the originator of the payment"</sub>
- **mandatory / requirement**: In the absence of an account number, a unique transaction reference (UTR) number or similar code must be included. (p. 1)[^original]  
  <sub>anchor: "In the absence of an account number, a unique transaction reference (UTR) number or similar code must be included"</sub>
- **descriptive / definition**: For the debtor, 'Name' refers to the name of the customer ordering the payment as verified by the debtor agent PSP. (p. 1)[^original]  
  <sub>anchor: "‘Name’ refers to the name of the customer ordering the payment (the debtor) as verified by the debtor agent PSP"</sub>
- **expected / expectation**: The PSP should set out in its policies and procedures which names are to be recorded in its systems and which of those names should be used for payments; for accounts held in joint names, the PSP should set out in policy which names are recorded and which are used for payments. (p. 1)[^original]  
  <sub>anchor: "The PSP should set out in its relevant policies and procedures which names are to be recorded in its systems"</sub>
- **mandatory / requirement**: The PSP's name policies must be in line with all the regulations applicable to the PSP. (p. 1)[^original]  
  <sub>anchor: "These policies must be in line with all the regulations applicable to the PSP"</sub>
- **expected / expectation**: For legal entity customers (e.g., companies, partnerships), multiple names may exist (registered legal name, trading name, "doing business as" name, commonly abbreviated name), and the PSP should place preference on the registered legal entity name verified as part of CDD. (p. 1)[^original]  
  <sub>anchor: "The PSP should place preference on the registered legal entity name verified as part of CDD"</sub>
- **descriptive / case example**: Illustration: for a company, the registered legal name (e.g., Eastern Finmark Corporation) is the name given in the partnership agreement, articles of incorporation or other documents and used when communicating with government or other businesses, whereas a trade name/DBA (e.g., Finmark or EFC) is the name used for advertising and sales purposes that differs from the legal name. (p. 1)[^original]  
  <sub>anchor: "The name a business uses for advertising and sales purposes that is different from its legal name"</sub>
- **descriptive / definition**: For the debtor, 'Address' refers to an address of the customer as verified or identified during CDD under applicable laws and regulations by the debtor agent PSP. (p. 1)[^original]  
  <sub>anchor: "as verified or identified during CDD in accordance with the applicable laws and regulations by the debtor agent PSP"</sub>
- **expected / expectation**: Address information should be sufficient to identify clearly the location of the party/parties for sanctions screening and AML/CTF monitoring, and should include country and other aspects of address in accordance with resident country conventions such as city, state/province/municipality, street name, building number and name, and postal code. (p. 1)[^original]  
  <sub>anchor: "Address information should be sufficient to identify clearly the location of the party/parties for sanctions screening"</sub>
- **descriptive / case example**: Multiple addresses may exist, e.g., registered address (the official address of an incorporated company or other legal entity, generally part of the public record) and place of business address (where the real activity of the company is carried out, i.e., where operations are planned, controlled, managed and executed); the illustration uses a London registered address and an Angola branch place-of-business address. (p. 1)[^original]  
  <sub>anchor: "where the operations of the company are planned, controlled, managed, and executed"</sub>
- **expected / expectation**: The PSP should use the address verified as part of CDD; value may be found in utilising the "most relevant" address, and the PSP should set out in policies and procedures which addresses are to be recorded, verified and used for payments (a "more relevant" address should be verified given its heightened relevance). (p. 1)[^original]  
  <sub>anchor: "The PSP should use the address verified as part of CDD"</sub>
- **descriptive / context**: Where multiple account holders with different addresses exist, the address of the primary or first named account holder is likely to be sufficient. (p. 1)[^original]  
  <sub>anchor: "the address of the primary or first named account holder is likely to be sufficient"</sub>
- **mandatory / requirement**: These address policies must be in line with all regulations applicable to the debtor agent PSP and, when applicable under a correspondent relationship, the requirements established by the intermediary agent PSP that will facilitate settlement of the payment for the debtor agent PSP's benefit. (p. 1)[^original]  
  <sub>anchor: "These policies must be in line with all the regulations applicable to the debtor agent PSP"</sub>
- **permissive / recommendation**: Policies may also set out where a unique identifier code such as a BIC or LEI is sufficient to identify the debtor, where the debtor is an entity that can be identified appropriately without full name and address information. (p. 1)[^original]  
  <sub>anchor: "Policies may also set out where a unique identifier code such as a BIC"</sub>
- **recommended / recommendation**: Inclusion of the creditor address is strongly encouraged and represents best practice, and will facilitate faster processing, improve transaction monitoring quality and reduce unnecessary requests for information (RFIs). (p. 1)[^original]  
  <sub>anchor: "The inclusion of the address is strongly encouraged, represents best practice"</sub>
- **descriptive / definition**: For the creditor, 'Name' refers to the name of the beneficiary as provided by the originator of the transaction (the debtor); it is not subject to verification and the PSP should pass on the name as supplied by its customer. (p. 1)[^original]  
  <sub>anchor: "The name will not be subject to verification and the PSP should pass on the name as supplied by its customer"</sub>
- **descriptive / definition**: For the creditor, 'Address' refers to the address of the creditor as provided by the debtor (originator); where possible it should include country, state/province/municipality, city, street name, building number or name and postal code per resident country conventions, and should be passed on to the next PSP as supplied by the debtor, not subject to verification by the debtor agent PSP. (p. 1)[^original]  
  <sub>anchor: "will not be subject to verification by the debtor agent PSP"</sub>
- **expected / expectation**: For creditor addresses, having only a P.O. box as an address should be avoided except where no alternative exists. (p. 1)[^original]  
  <sub>anchor: "Having only a P.O. box as an address should be avoided except where no alternative exists"</sub>
- **mandatory / requirement**: The creditor name and address policies must be in line with the regulation of the applicable jurisdiction(s) of the PSP and the requirements established by the correspondent intermediary agent PSP, when applicable. (p. 1)[^original]  
  <sub>anchor: "These policies must be in line with the regulation of the applicable jurisdiction(s) of the PSP"</sub>
- **expected / expectation**: The debtor agent PSP should implement controls to address "on behalf of" (OBO) payments. (p. 1)[^original]  
  <sub>anchor: "Implement controls to address “on behalf of” (OBO) payments"</sub>
- **expected / expectation**: OBO situations should be managed by the debtor agent PSP with regard to the CDD requirements stated and identified by using the ultimate debtor and/or ultimate creditor fields of a payment message. (p. 1)[^original]  
  <sub>anchor: "identified by using the ultimate debtor and/or ultimate creditor fields of a payment message"</sub>
- **mandatory / requirement**: Under the OBO scenario for a payment factory function (where the factory within the corporate entity pays or collects on behalf of other group entities), the arrangements must be understood by the debtor agent PSP before corporate entities are allowed to pay on behalf of other parties, to ensure the OBO relationship is permissible under local regulation, e.g., regarding custodial or fiduciary relationships. (p. 1)[^original]  
  <sub>anchor: "these arrangements must be understood by the debtor agent PSP to ensure the OBO relationship is permissible under local regulation"</sub>
- **descriptive / case example**: In the law firm scenario, the transaction initiated by the legal entity is on behalf of its own customer, who is the ultimate debtor; the legal entity is not itself a PSP but uses its account with the debtor agent PSP to conduct a transaction for a third party who is not a customer of the debtor agent PSP. (p. 1)[^original]  
  <sub>anchor: "The legal entity is not itself a PSP, but it is using its account with the debtor agent PSP"</sub>
- **descriptive / context**: These OBO scenarios are distinct from a PSP maintaining another PSP as a customer and processing its transactions for underlying customers; there is then a clear debtor agent PSP initiating the payment, processed by the intermediary agent PSP that maintains the PSP as customer (the relationship-owning PSP), all roles and responsibilities in the revised Standards apply, and the flow is akin to a correspondent relationship rather than OBO. (p. 1)[^original]  
  <sub>anchor: "This type of flow is not the same as an OBO scenario, and rather is akin to a correspondent relationship"</sub>
- **expected / expectation**: The debtor agent PSP should set out in its policy what ultimate debtor/originator information its customers should provide, and clearly communicate those expectations to its customers. (p. 1)[^original]  
  <sub>anchor: "Set out in its policy what ultimate debtor/originator information should be provided by its customers"</sub>
- **expected / expectation**: To the extent identifiable from customer instructions, and practically achievable given the PMI's message format, the debtor agent PSP should include the full name and address of the ultimate debtor in addition to those of its customer in the payment message; this information may be more relevant for financial crime compliance purposes than customer information, is not subject to verification, and should be passed on as supplied by the customer. (p. 1)[^original]  
  <sub>anchor: "include the full name and address of the ultimate debtor in addition to that of the debtor agent PSP"</sub>
- **expected / expectation**: Where neither ultimate debtor nor customer (debtor) information can both be provided in the same payment message (due to limits in the number or length of fields), the PSP should set out in its policy whether to provide debtor information, as detailed in sub-section A, instead of ultimate debtor information. (p. 1)[^original]  
  <sub>anchor: "the PSP should set out in its policy whether to provide information on the debtor"</sub>
- **mandatory / requirement**: That policy must be in line with the regulations of the applicable jurisdictions for the PSP and the requirements established by the correspondent intermediary agent PSP (when applicable) that will facilitate settlement of the payment for the debtor agent PSP's benefit (the relationship-owning PSP). (p. 1)[^original]  
  <sub>anchor: "These policies must be in line with the regulations of the applicable jurisdictions for the PSP"</sub>
- **expected / expectation**: The debtor agent PSP should be prepared to source and share additional information on the debtor or ultimate debtor with other PSPs in the payment chain when requested. (p. 1)[^original]  
  <sub>anchor: "Be prepared to source and share additional information on the debtor or ultimate debtor to other PSPs"</sub>
- **expected / expectation**: The debtor agent PSP should maintain a clear position in policy on where it permits OBO transactions based on customer type and underlying business models, enabling it to embed controls for oversight and monitoring of OBO transactions, including whether the business model fits within expected OBO type payments and whether ultimate debtor information is provided on a regular basis. (p. 1)[^original]  
  <sub>anchor: "should maintain a clear position in policy where they permit OBO transactions based on customer type"</sub>

## Introduction

- **descriptive / context**: The revised Standards set out the operational and financial crime risks of newer payment services as they relate to payment transparency. Because globally uniform standards and guidelines are absent and continue to differ between jurisdictions, they describe a responsible way forward for every stakeholder in payments. (p. 1)[^original]  
  <sub>anchor: "in the absence of globally uniform standards and guidelines, which continue to vary across jurisdictions"</sub>
- **descriptive / context**: The Group notes that it is no longer as clear where one actor's role in ensuring payment transparency begins and ends, as it was when electronic payments were nearly all started through a regulated bank and sent mainly as SWIFT messages. (p. 1)[^original]  
  <sub>anchor: "almost entirely initiated via a regulated bank and moved mainly through SWIFT messages"</sub>
- **expected / expectation**: The Group states that the roles and responsibilities of every actor in a payment chain, nested parties included, now have to be addressed across the different payment communication channels, whatever the nature of the stakeholder and whether or not it is a bank. (p. 1)[^original]  
  <sub>anchor: "It is now necessary to address the roles and responsibilities of all actors in a payment chain, including nested parties"</sub>
- **descriptive / context**: The Group observes that legacy payment infrastructure is handling growing data volumes, that stakeholders including supervisors need a better grasp of how new actors with distinctive payment models strain payment transparency requirements, and that terminology is shifting as messages move to the more structured ISO 20022 framework. (p. 1)[^original]  
  <sub>anchor: "understanding by all stakeholders (including supervisors) needs to improve"</sub>

## The Standards

- **descriptive / context**: The Standards acknowledge that some jurisdictions allow collection agent models, in which the PSP can count as the legal debtor or creditor of a payment, acts for itself, and is shown that way in the payment message. (p. 1)[^original]  
  <sub>anchor: "collection agent models are permitted whereby the PSP may be considered the legal debtor or creditor of a payment"</sub>
- **descriptive / limitation**: The Standards are not meant to apply directly to digital assets. They should nonetheless be useful to digital asset service providers that are committed to the basic principles of payment transparency and to those developing digital assets, including when designing CBDCs. (p. 1)[^original]  
  <sub>anchor: "The Standards are not intended to apply directly to digital assets"</sub>

## 1. The PMI(s) and the competent authority(ies)

- **expected / expectation**: Because PMIs often use different message formats, the PMI rulebook should address in a consistent way how far the PMI allows intermediated payments and how those payments, including the parties, are to be captured in the PMI's message format. (p. 1)[^original]  
  <sub>anchor: "the PMI rulebook should specifically address, in a consistent way, the degree to which the PMI permits intermediated payments"</sub>
- **expected / expectation**: The competent authority should be responsible for giving guidance on when bundled payments are allowed (if host country regulation allows them) and on when a PSP is only handling final settlement or disbursement of transactions. (p. 1)[^original]  
  <sub>anchor: "Providing guidance on the circumstances under which bundled payments are permitted"</sub>
- **expected / expectation**: The competent authority should be responsible for clarifying what applies to PSPs that use substitutes for payment account numbers, where the host country permits this, such as virtual receivable account numbers or tokenised account numbers. (p. 1)[^original]  
  <sub>anchor: "Clarifying applicable requirements for PSPs when using alternatives to payment account numbers"</sub>
- **expected / expectation**: The competent authority should be responsible for deciding when a PSP may regard itself as the debtor or creditor, for instance under a collection agent model where it acts on its own behalf. (p. 1)[^original]  
  <sub>anchor: "Determining the circumstances under which a PSP is permitted to consider itself the debtor or creditor"</sub>
- **expected / expectation**: The competent authority should be responsible for clarifying the AML/CTF and sanctions compliance expectations of an intermediary agent PSP in the PMI, taking account of, for example, 'by, at, or through' reporting requirements in some jurisdictions, while recognising how hard it is for an intermediary agent PSP to monitor whether the debtor agent or other intermediary agent PSPs interpret and apply payment transparency requirements properly. (p. 1)[^original]  
  <sub>anchor: "Clarifying the Anti-Money Laundering and Counter-Terrorist Financing (AML/CTF) and sanctions compliance expectations of an intermediary agent PSP"</sub>

## 2. All PSPs, irrespective of their role in the payment chain

- **expected / expectation**: PSPs should not leave out, remove or change debtor or creditor information in payment messages or orders in order to stop other PSPs in the payment process from detecting it; the only valid reasons for changes are fixing errors or adding message detail that helps settlement and increases transparency. (p. 1)[^original]  
  <sub>anchor: "PSPs should not omit, delete, or alter debtor or creditor information in payment messages or orders"</sub>
- **expected / expectation**: Subject to all applicable laws, PSPs should cooperate as fully as is practicable when other PSPs in the payment process ask for information on the parties and the nature of the transaction, including through legally permissible information sharing arrangements. (p. 1)[^original]  
  <sub>anchor: "PSPs should cooperate as fully as practicable with other PSPs in the payment process"</sub>
- **expected / expectation**: For products offering faster cross-border payments, for example by combining domestic PMIs with cross-border transfers, PSPs should choose the domestic PMI(s) that make the cross-border nature of the payment, and the information on its parties passed to the next PSP, as transparent as possible and readily understood by every intermediary and/or creditor agent PSP. (p. 1)[^original]  
  <sub>anchor: "PSPs should select the domestic PMI(s) that maximise the transparency of the cross-border nature of the payment"</sub>
- **expected / expectation**: PSPs should switch to more structured and detailed payment formats, such as ISO 20022, as early as they can, because this raises data quality and so improves transparency aims and the results of transaction monitoring and screening. (p. 1)[^original]  
  <sub>anchor: "PSPs should move to adopt and use more structured and detailed payment formats at the earliest opportunity"</sub>

## 3. Debtor agent PSPs – ordering institutions/payer PSPs

- **expected / expectation**: Unique transaction reference (UTR) numbers should be used only for transfers that are not made from or to a payment account. Account numbers, or a similar static number linked to the debtor, are expected on every payment where the debtor agent PSP has set up a payment account for its customer, the debtor. (p. 1)[^original]  
  <sub>anchor: "UTR numbers should only be used in the case of a transfer not made from or to a payment account"</sub>
- **expected / expectation**: For natural person customers, the name held in the PSP's systems should be the customer's full name as verified during CDD. (p. 1)[^original]  
  <sub>anchor: "should be the full name of the customer that was verified as part of CDD"</sub>
- **expected / expectation**: A debtor address consisting only of a post office (P.O.) box should be avoided, unless no alternative exists because of market practices or limitations and local regulations support it. (p. 1)[^original]  
  <sub>anchor: "Having only a post office (P.O.) box as an address should be avoided"</sub>
- **expected / expectation**: Where possible the address should be fully structured; at the least it should use a hybrid structure, with town and country name structured and street name, building number and similar parts possibly unstructured because of local naming conventions. (p. 1)[^original]  
  <sub>anchor: "Address should be fully structured, when possible, and at a minimum employ a hybrid structure"</sub>
- **descriptive / context**: Where the payment message does not govern the format through structured fields, spelling out full country names as recognised by the United Nations will make addresses clearer. (p. 1)[^original]  
  <sub>anchor: "using full country names as recognised by the United Nations"</sub>
- **permissive / recommendation**: ISO 3166 2-character country codes may be used, as a preferred approach, instead of the full country name in the debtor/originator and creditor/beneficiary fields of PACS008, PACS009 and PACS009COV, Swift MT103, MT202 and MT202COV and related structured messages. (p. 1)[^original]  
  <sub>anchor: "may be used as a preferred approach for PACS008, PACS009 and PACS009COV"</sub>
- **expected / expectation**: As the ordering institution, the debtor agent PSP should include the creditor's (beneficiary or payee) name, address and account number, and the ultimate creditor if applicable, to the fullest extent the relevant PMI permits. (p. 1)[^original]  
  <sub>anchor: "Include Name, Address, and Account number of the creditor (the beneficiary or the payee), and ultimate creditor if applicable"</sub>
- **mandatory / requirement**: Where there is no creditor account number, a unique transaction reference number or similar code must be included in the payment. (p. 1)[^original]  
  <sub>anchor: "In the absence of an account number, a unique transaction reference number or similar code must be included"</sub>
- **expected / expectation**: The debtor agent PSP should state in its policy which creditor names and addresses it should ask its customers (the debtor) to supply for use in payment messages. (p. 1)[^original]  
  <sub>anchor: "The debtor agent PSP should set out in its policy which creditor name(s) and address(es) should be requested"</sub>
- **descriptive / definition**: An 'on behalf of' (OBO) payment arises when the debtor agent's customer pays for an ultimate originator or ultimate debtor. There are primarily two kinds: payments for the underlying customers of traditional corporate entities, such as a multinational with subsidiaries and a centralised treasury department running a payment factory function, and payments by businesses acting for third parties, such as law firms. (p. 1)[^original]  
  <sub>anchor: "There are primarily two types of OBO payments: those made for the underlying customers of traditional corporate entities"</sub>
- **expected / expectation**: The OBO concept should not be used where a payment is made on behalf of another PSP, because that is a correspondent relationship and should be treated as one. (p. 1)[^original]  
  <sub>anchor: "Importantly, the concept of OBO payments should not be applied when the payment is"</sub>
- **expected / expectation**: In correspondent relationships it is important to tell apart PSPs that are properly licensed and registered with the local regulator to provide payment services from legal entities that may act as a PSP without the licences or registrations required in the local market. As an example, a PSP with global operations may be licensed in its home jurisdiction but lack the licences needed in the local jurisdiction where the payment account is held. (p. 1)[^original]  
  <sub>anchor: "it is important to distinguish PSPs that are appropriately licensed and registered with the local regulatory authority"</sub>
- **expected / expectation**: To support payment transparency in OBO scenarios, the debtor agent PSP should carry out enough CDD on its customer to confirm to a reasonable degree that payments for OBO parties fit with the customer's line of business or expected activity. (p. 1)[^original]  
  <sub>anchor: "Undertake sufficient CDD on its customer to confirm to a reasonable degree that payments for OBO parties are consistent"</sub>

---

[source overview](overview.md) | [next part](digest-002.md)

[^original]: Wolfsberg Group, "The Wolfsberg Group - Payment Transparency Standards" (2023). https://wolfsberg-group.org/resources/correspondent-banking/136
