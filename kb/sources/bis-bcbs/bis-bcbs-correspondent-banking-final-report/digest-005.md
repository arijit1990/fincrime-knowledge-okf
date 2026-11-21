---
type: Source Digest
title: Correspondent banking - final report - part 5 of 7 (pp. 36-45)
description: 'Verified paraphrased digest, pp. 36-45: 3. Potential measures to facilitate correspondent banking services > 3.5 Payment messages; 3. Potential measures to facilitate correspondent banking services > A correspondent transaction using the serial method; 3. Potential measures to facilitate correspondent banking services > 4. Conclusions'
resource: https://www.bis.org/publications/correspondent-banking-final-report
tags:
- correspondent_banking
- international_standard
- intl
- standard
status: stable
source_id: bis-bcbs-correspondent-banking-final-report
issuer: bis_bcbs
issuer_name: Bank for International Settlements / Basel Committee
jurisdictions:
- INTL
tier: 2
instrument_type: standard
normative_force: international_standard
publication_date: '2016-07-13'
legal_status: current
part: 5
parts_total: 7
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
  resource: https://www.bis.org/publications/correspondent-banking-final-report
  title: Correspondent banking - final report
  author: org:bis_bcbs
  last_modified: '2016-07-13T00:00:00Z'
digest_points: 51
---

# Correspondent banking - final report (digest)

[previous part](digest-004.md) | [source overview](overview.md) | [next part](digest-006.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (pp. 36-45) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **international standard**.

## 3.5.1 General considerations

- **descriptive / context**: Correspondent banking transactions are channelled and settled through a chain of bilateral relationships between respondent and correspondent banks, sometimes also involving payment systems. Section 3.5 focuses on payment message flows and formats, describes commonly used payment processes and messaging methods, and identifies issues the industry and authorities might consider to facilitate cross-border correspondent banking. (p. 36)[^original]  
  <sub>anchor: "This section focuses on the payment message flows and formats."</sub>
- **descriptive / context**: SWIFT message formats are non-proprietary and can be used over other networks, but the SWIFT network is used in the overwhelming majority of correspondent banking relationships. The description therefore focuses on SWIFT message formats and assumes respondent, correspondent and intermediary banks all have SWIFT access. (p. 36)[^original]  
  <sub>anchor: "the network used in the overwhelming majority of correspondent banking relationships is the SWIFT network"</sub>
- **descriptive / context**: Footnote 35 explains that the working group concentrated on cross-border payments, but the full chain of a cross-border correspondent banking payment can also contain transfers between institutions inside one jurisdiction, normally run through payment systems, and payment systems may in some cases also carry payments across different jurisdictions. (p. 36)[^original]  
  <sub>anchor: "the complete payment chain of cross-border correspondent banking payments may also include transfers between institutions in a single jurisdiction"</sub>

## 3.5.2 Message flows

- **descriptive / definition**: A simple cross-border correspondent transaction is a payment from a customer of the respondent bank to a customer of the correspondent bank in a different jurisdiction (customers can be individuals, SMEs, corporates, public sector agencies or other financial institutions). Where the respondent has a direct bilateral account relationship with the correspondent, payment information and settlement instruction can travel in a single message; the SWIFT standard for customer payment messages is the MT 103 (MX equivalent pacs.008, though MT formats are normally used in correspondent banking). (p. 37)[^original]  
  <sub>anchor: "The SWIFT standard for these customer payment messages is the MT 103."</sub>
- **descriptive / context**: In many cases the originating respondent bank has no direct bilateral account relationship with the receiving bank, so a chain of one or more intermediary banks, which also provide correspondent services, is needed. Such relationships are very common, and payment chains can be long, involving banks in more than two jurisdictions. (p. 37)[^original]  
  <sub>anchor: "Payment chains can be quite long, involving banks in more than two jurisdictions."</sub>
- **descriptive / definition**: When the originating institution has no direct account relationship with the receiving bank there are two basic ways to channel the transaction through SWIFT: the serial method and the cover method. Both can be used in full compliance with AML/CFT and relevant regulatory requirements provided all relevant data fields of the payment message are accurately populated. (p. 38)[^original]  
  <sub>anchor: "the serial method and the cover method"</sub>
- **descriptive / definition**: The serial method sends an MT 103 (or equivalent) from the originating bank to the receiving bank through one or more intermediaries, as an extended concatenation of simple transactions. Payment information and settlement instruction travel together in the MT 103, with a direct account relationship between each connected pair of banks in the chain. (p. 38)[^original]  
  <sub>anchor: "The serial method involves sending an MT 103 (or equivalent) from the originating bank to the receiving bank"</sub>
- **descriptive / definition**: The cover method decouples settlement from payment information: the MT 103 with payment information is sent directly through SWIFT from the originating bank to the receiving bank, while the settlement instruction (the cover payment) goes via intermediary banks along the path of direct correspondent relationships. (p. 38)[^original]  
  <sub>anchor: "The cover method decouples the settlement from the payment information."</sub>
- **descriptive / finding or result**: Cover payments were traditionally made with the MT 202 (the standard SWIFT interbank transfer message), which was not designed to carry detailed information on the ordering customer and final beneficiary. Intermediary banks therefore could not properly screen these transactions for AML/CFT and sanctions, and could even remain unaware that the MT 202 related to a commercial correspondent banking payment. (p. 38)[^original]  
  <sub>anchor: "intermediary banks were not able to screen these transactions properly according to AML/CFT and sanctions requirements"</sub>
- **descriptive / definition**: The MT 202 COV, a message standard for interbank transfers related to correspondent banking cover payments, was implemented in the 2009 standards release following joint effort by SWIFT, banks and authorities. It keeps the principle of cover payments via interbank transfer messages and is designed to carry the identities of the ordering customer and final beneficiary and other information included in the underlying MT 103. (p. 39)[^original]  
  <sub>anchor: "the MT 202 COV, a new message standard for interbank transfers related to correspondent banking cover payments"</sub>
- **mandatory / requirement**: If the code "COV" is used in field 119 of the message user header, it is mandatory to fill in an additional sequence including a copy of selected fields from the underlying customer credit transfer (the MT 103). Adoption of the MT 202 COV has led to a ban on plain MT 202 messages in correspondent banking whenever an underlying customer transaction is involved. (p. 39)[^original]  
  <sub>anchor: "it is mandatory to fill in an additional sequence in the message to include a copy of selected fields"</sub>
- **descriptive / context**: Footnote 39: introduction of the MT 202 COV did not end the MT 202 interbank transfer message, which remains appropriate for pure interbank transactions unrelated to commercial correspondent banking services. (p. 39)[^original]  
  <sub>anchor: "which remains appropriate for pure interbank transactions"</sub>
- **descriptive / finding or result**: Both the serial MT 103 and the cover MT 202 COV methods can be used in full compliance with AML/CFT and regulatory requirements. When all relevant data fields are accurately populated, both give all banks involved the necessary payment information to screen adequately and fulfil regulatory requirements. (p. 39)[^original]  
  <sub>anchor: "both methods, ie the serial MT 103 and the cover MT 202 COV methods, can be used in full compliance"</sub>
- **expected / expectation**: From the AML/CFT standpoint, whether the serial or the cover method is used, the report says it is of the utmost importance to make sure that every necessary item of information is accurately put in the payment message. (p. 39)[^original]  
  <sub>anchor: "it is of the utmost importance to ensure that all necessary information is accurately included in a payment message"</sub>
- **descriptive / finding or result**: According to the report, any apparent difference in AML/CFT risk between the two methods comes from which party supplies, or fails to supply, the required information in the message, not from the method itself. (p. 39)[^original]  
  <sub>anchor: "Any perceived difference in AML/CFT risk does not lie in the method used"</sub>
- **expected / expectation**: The Wolfsberg Group endorsed four payment message standards: (i) financial institutions should not omit, delete or alter information in payment messages or orders to avoid detection by other financial institutions in the payment process; (ii) they should not use any particular payment message to avoid detection of information; (iii) subject to applicable laws, they should cooperate as fully as practicable with other institutions in the payment process when asked for information about parties involved; and (iv) they should strongly encourage their correspondent banks to observe these principles. (p. 40)[^original]  
  <sub>anchor: "financial institutions should not omit, delete, or alter information in payment messages or orders"</sub>
- **mandatory / requirement**: When using the MT 202 COV, the originating bank must correctly flag the MT 202 as a cover message and ensure all information relevant for AML/CFT procedures is provided. (p. 40)[^original]  
  <sub>anchor: "the originating bank must correctly flag the MT 202 message as a cover message"</sub>
- **descriptive / typology or red flag**: If the originating bank does not provide the cover information, perhaps through technical problems or even fraudulent intent, other banks in the chain will not receive all relevant information. Since an MT 202 without the cover indicator is a simple interbank payment, intermediaries will accept it unaware that information is missing, so a bank could unknowingly accept a message with incomplete information and might not be able to fulfil its regulatory obligations. (p. 40)[^original]  
  <sub>anchor: "since an MT 202 payment without the cover indicator is a simple interbank payment"</sub>
- **descriptive / limitation**: With the MT 103 in the serial method, a bank may likewise be unaware of inaccurate or missing information, because the method itself gives no assurance against deceptive practices or fraudulent intent. A missing mandatory field can be detected (a message sent via SWIFTNet FIN will be rejected), but determining whether the ordering customer or beneficiary customer information is accurate is a completely different exercise, especially for intermediaries. (p. 40)[^original]  
  <sub>anchor: "it is a completely different exercise to seek to determine whether the information"</sub>
- **expected / expectation**: Regardless of method, it is of the utmost importance for banks in correspondent banking to ensure all information needed to comply with the relevant FATF recommendations (especially Recommendation 16) is available within a payment message. Originating banks are in the best position to ensure the message reflects the originator's identity, and beneficiary banks to know whether it accurately identifies the beneficiary. (p. 41)[^original]  
  <sub>anchor: "originating banks are in the best position to ensure that payment messages properly reflect the identity of a payment originator"</sub>
- **descriptive / context**: The PMPG has published market practice guidelines and white papers on information in payment messages, including guidelines for the MT 202 COV, expanded US wire formats, remt.001 in cross-border payment processes, FATF SRVII and FATF Recommendation 16, and white papers on extended remittance information (ERI), payment notification and the use of an IBAN. The report says this guidance seems granular enough and will be regularly reviewed by the PMPG. (p. 41)[^original]  
  <sub>anchor: "It seems that the guidance provided by the PMPG is granular enough"</sub>
- **descriptive / context**: If a bank does not accurately populate a payment message, other banks may take this into account when assessing the correspondent banking relationship. (p. 41)[^original]  
  <sub>anchor: "other banks may take this into account when assessing the correspondent banking relationship."</sub>

## Fees and costs

- **descriptive / finding or result**: By current market practice banks do not deduct fees from MT 202/MT 202 COV messages, so intermediaries on a cover payment deduct no additional fees. For the MT 103, a fee is typically deducted from the payment amount by each intermediary bank, so the beneficiary does not receive the full amount of the original payment order. (p. 41)[^original]  
  <sub>anchor: "banks do not deduct fees from MT 202/MT 202 COV messages"</sub>
- **descriptive / finding or result**: With the cover method two SWIFT messages must be sent by the originating bank and two processed by the receiving bank. Most correspondent banking costs arise not from payment processing but from compliance and IT work on system modifications. (p. 41)[^original]  
  <sub>anchor: "most of the costs involved in correspondent banking arise not from the actual payments processing"</sub>
- **descriptive / limitation**: Comprehensive cost calculations can only be done by individual banks, so it is not possible to say a priori which payment method is cheaper. Some commenting banks suggested the cost differences between the two methods have been exaggerated and have not been key determinants of the method used. (p. 41)[^original]  
  <sub>anchor: "it is not possible to say a priori which payment method is cheaper"</sub>

## Message flow

- **descriptive / finding or result**: The cover method is generally considered faster. With two separate flows the receiving bank knows funds are coming and can investigate if the MT 202 COV does not arrive, but depending on commercial policy this knowledge may allow earlier crediting or pressure the bank (for example for large corporates) to credit its customer before receiving funds. This is especially critical where the beneficiary bank has the MT 103 but the MT 202 COV is stopped or rejected on compliance grounds. (p. 41)[^original]  
  <sub>anchor: "In general, the cover method is considered to be faster."</sub>
- **expected / expectation**: Banks need to ensure that appropriate unwinding procedures are in place to reverse a credit on the account should the need arise, and the receiving bank always needs to match both message flows. (p. 41)[^original]  
  <sub>anchor: "banks need to ensure that appropriate unwinding procedures are in place to reverse a credit on the account"</sub>
- **descriptive / finding or result**: According to consultation input, clearing system limitations and time zones keep both methods relevant: clearing systems in some jurisdictions do not support all charge code options (for example OUR), so the serial method cannot provide a full value transfer, and the serial method may affect same-day value into some markets (for example payments into Asia from outside Asia). (p. 41)[^original]  
  <sub>anchor: "clearing systems in some jurisdictions do not support all the charge code options"</sub>

## Payment advice

- **expected / expectation**: Having weighed the characteristics of the serial and cover methods, the report says banks engaged in correspondent banking need to choose for themselves which method suits them best. (p. 41)[^original]  
  <sub>anchor: "banks involved in correspondent banking activities need to decide individually which method best meets their needs"</sub>
- **expected / expectation**: The report says that to meet all AML/CFT obligations it is crucial that the message used is filled in accurately, while the choice of message type is not critical. (p. 41)[^original]  
  <sub>anchor: "In order to fulfil all obligations with regard to AML/CFT it is crucial that the message used is accurately populated"</sub>
- **recommended / recommendation**: Recommendation: banks are advised to determine individually which payment method best serves their own and their clients' needs, and to agree the method to use with the other banks involved. (p. 41)[^original]  
  <sub>anchor: "It is recommended that banks decide individually which payment method best meets their own and their clients"</sub>
- **descriptive / finding or result**: In the serial MT 103 the information and settlement reach the receiving bank at the same time, eliminating any lag. The receiving bank will not know a payment is coming until all intermediaries have processed the MT 103; if need be this can be solved by alternative means, such as SWIFT FINInform sending a copy of the MT 103 to the receiving bank (which then needs procedures to avoid erroneous double-processing). (p. 42)[^original]  
  <sub>anchor: "the information and the settlement reach the receiving bank at the same time"</sub>
- **descriptive / limitation**: If banks intend to engage in deceptive practices, it is almost impossible for correspondent banks, especially intermediaries, to detect this irrespective of method. A bank that deliberately chooses MT 202 instead of MT 202 COV to avoid including additional transaction information is unlikely to be more honest when using a serial MT 103. (p. 42)[^original]  
  <sub>anchor: "it is almost impossible for correspondent banks, especially for intermediary institutions, to detect this"</sub>
- **recommended / recommendation**: The Wolfsberg Group and the PMPG are invited to review their principles governing use-cases for payment messages (such as PMPG market practice guidelines and white papers). The documents should include information about the data that should be contained in payment messages and the data fields to be used for CDD information. AMLEG is invited to consider further developing guidance on supervisors' role in ensuring banks meet FATF Recommendations and guidance on the quality of payment message content. (p. 42)[^original]  
  <sub>anchor: "are invited to review their principles governing the use-cases for payment messages"</sub>

## 3.5.3 Usage of the LEI as additional information in payment messages

- **descriptive / finding or result**: Payment messages currently have neither a dedicated code nor a dedicated line/field for the LEI. The LEI can be used in free format fields, but no validations check whether an LEI is included or syntactically correct. (p. 42)[^original]  
  <sub>anchor: "Currently, payment messages include neither a dedicated code nor a dedicated line/field for the LEI."</sub>
- **expected / recommendation**: In the long term the industry could evaluate including the LEI in payment messages for unambiguous identification of parties. As payment messages evolve, a discussion on dedicated codes or data items for the LEI should take place when format changes would be discussed anyway, for example if ISO 20022-compliant formats are considered for correspondent banking, which would imply changes to bank IT systems. No LEI generally exists for individuals. (p. 42)[^original]  
  <sub>anchor: "a discussion on the development of such dedicated codes or data items for the LEI should take place"</sub>
- **permissive / recommendation**: Meanwhile, as LEI use becomes widespread or even compulsory for banks and corporate customers, relevant stakeholders (for example the PMPG) may wish to analyse how the LEI can be used on an optional basis in a more structured way within current MT 103 and MT 202 COV messages. (p. 42)[^original]  
  <sub>anchor: "may wish to analyse how the LEI can be used on an optional basis in a more structured way"</sub>

## 3.5.2 Message flows

- **descriptive / context**: Footnote 48 adds that, in securities messaging, the LEI can already serve as a party identifier across ISO 15022 category 5 messages. (p. 42)[^original]  
  <sub>anchor: "the LEI can be used as a party identifier across ISO 15022 category 5 messages"</sub>

## 3.5.3 Usage of the LEI as additional information in payment messages

- **descriptive / method**: Options for including the LEI in the payment message are: (i) specific data fields in correspondent banking formats such as the MT 103 or MT 202 COV (and equivalents); (ii) a dedicated LEI code within the message; or (iii) a market practice allowing the LEI in an existing field. Because of the long-term move from MT to ISO 20022-compliant MX formats, the report says this solution should have only very limited impact on necessary investments. (p. 43)[^original]  
  <sub>anchor: "(iii) the development of a market practice in which the LEI can be included in an existing field"</sub>
- **permissive / recommendation**: As part of the future migration to ISO 20022-based message formats, ISO and SWIFT might wish to consider developing dedicated codes or data items for the structured inclusion of the LEI in payment messages. (p. 43)[^original]  
  <sub>anchor: "might wish to consider developing dedicated codes or data items for the structured inclusion of the LEI"</sub>
- **permissive / recommendation**: In the meantime, LEI use in payment messages could be allowed on an optional basis in other standards for those who want to use it earlier. For efficient cross-border processing, optional use may need to be introduced simultaneously in a harmonised way in many jurisdictions. (p. 43)[^original]  
  <sub>anchor: "may need to be simultaneously introduced in a harmonised way in many jurisdictions"</sub>
- **descriptive / limitation**: If the LEI were included on an optional basis, it would need to be clarified in advance how to deal with contradictions between the LEI and other party references (for example an account number) in the message. (p. 43)[^original]  
  <sub>anchor: "how to deal with any contradictions between the LEI and other party references"</sub>
- **descriptive / finding or result**: Due to its limitations and high transition costs, the report says it seems premature to promote a requirement for mandatory inclusion of the LEI in payment messages. (p. 43)[^original]  
  <sub>anchor: "it seems premature to promote a requirement for the mandatory inclusion of the LEI in payment messages"</sub>
- **expected / recommendation**: Recommendation: the use of the LEI as additional information in payment messages should be possible on an optional basis in the current relevant payment messages (MT 202 COV and MT 103). Relevant stakeholders (for example the PMPG) should work to define a common market practice for including the LEI in current messages without changing the current message structure. (p. 43)[^original]  
  <sub>anchor: "should be possible on an optional basis in the current relevant payment messages"</sub>
- **recommended / recommendation**: As part of a potential future migration to ISO 20022-based formats, ISO and SWIFT are encouraged to consider developing dedicated codes or data items for the inclusion of the LEI in these payment messages. (p. 43)[^original]  
  <sub>anchor: "are encouraged to consider developing dedicated codes or data items for the inclusion of the LEI"</sub>

## 4. Conclusions

- **descriptive / finding or result**: Correspondent banking services are an essential component of the global payment system, especially for cross-border transactions. Correspondent banks often cite as reasons for the decline in relationships compliance with AML/CFT regulations, increased perception of risk and uncertainties about the potential impact of non-compliance. (p. 43)[^original]  
  <sub>anchor: "Correspondent banking services are an essential component of the global payment system"</sub>
- **descriptive / finding or result**: The impact of the decline is uneven across jurisdictions and banks. Some correspondents specialise in for-profit provision and focus on respondents with volumes justifying rising costs; others maintain services only as far as they support cross-selling; some relationships depend on perceived risk in the respondent's jurisdiction. Some respondent banks might be cut off from international payment networks, implying a risk that cross-border payment systems become fragmented, reducing options. (p. 44)[^original]  
  <sub>anchor: "This trend implies a risk that cross-border payment systems will become fragmented"</sub>
- **descriptive / context**: The working group limited its analysis to measures that could improve efficiency of procedures while reducing compliance costs and perceived uncertainties, without altering applicable rules and basic channels for correspondent banking. The measures were translated into five recommendations (KYC utilities; increased LEI use; information-sharing initiatives; payment messages; LEI as additional information in payment messages). (p. 44)[^original]  
  <sub>anchor: "The potential measures were translated into five recommendations."</sub>
- **descriptive / limitation**: The CPMI believes its recommendations might alleviate some costs and concerns but stresses that in isolation they will not resolve all issues. Withdrawal from correspondent banking is very complex, AML/CFT compliance costs are one element among business considerations and economies of scope and scale, enhanced technical tools address only part of compliance costs and not uncertainty about how far CDD should go, and the measures will not immediately help banks without access to gain access. (p. 44)[^original]  
  <sub>anchor: "in isolation, these measures will not resolve all the issues."</sub>
- **expected / expectation**: As a next step before any implementation, the measures should be further analysed by all relevant authorities and stakeholders to gauge the impact of each measure and avoid unintended consequences. The CPMI expects relevant stakeholders to initiate any necessary reviews or investigations in light of the five recommendations as soon as possible. (p. 44)[^original]  
  <sub>anchor: "The CPMI expects that the relevant stakeholders will initiate any necessary reviews or investigations"</sub>
- **descriptive / context**: The CPMI will (i) encourage, mainly through CPMI members' participation in the FSB Correspondent Banking Coordination Group, review or investigation of the recommendations by relevant stakeholders and (ii) from the technical perspective of payment systems, facilitate implementation by contributing to stakeholders' work or workstreams. (p. 44)[^original]  
  <sub>anchor: "participation of CPMI members in the FSB Correspondent Banking Coordination Group"</sub>

---

[previous part](digest-004.md) | [source overview](overview.md) | [next part](digest-006.md)

[^original]: Bank for International Settlements / Basel Committee, "Correspondent banking - final report" (2016-07-13). https://www.bis.org/publications/correspondent-banking-final-report
