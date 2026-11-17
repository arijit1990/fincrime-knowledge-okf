---
type: Source Text
title: FFIEC Bank Secrecy Act/Anti-Money Laundering Examination Manual - part 19 of 32 (pp. 196-206)
description: 'Verbatim extracted text, pp. 196-206: Bank Secrecy Act/ Anti-Money Laundering Examination Manual > Risk Mitigation'
resource: https://bsaaml.ffiec.gov/manual
tags:
- case_management
- customer_risk
- legal_requirement
- regulation
- risk_based_approach
- rulebook_sourcebook
- transaction_behaviour
- us
status: stable
source_id: ffiec-ffiec-bank-secrecy-act-anti-money-laundering-examination-manual
issuer: ffiec
issuer_name: FFIEC
jurisdictions:
- US
tier: 1
instrument_type: rulebook_sourcebook
normative_force: legal_requirement
publication_date: '2020-06-17'
legal_status: current
part: 19
parts_total: 32
content_mode: full_text
generated:
  by: process:fincrime-kb-build
  at: '2026-11-17T12:21:45Z'
verified:
- by: process:kb-validate/verbatim-coverage
  at: '2026-11-17T12:21:45Z'
sources:
- id: original
  resource: https://bsaaml.ffiec.gov/manual
  title: FFIEC Bank Secrecy Act/Anti-Money Laundering Examination Manual
  author: org:ffiec
  last_modified: '2020-06-17T00:00:00Z'
---

# FFIEC Bank Secrecy Act/Anti-Money Laundering Examination Manual

[previous part](text-018.md) | [source overview](overview.md) | [next part](text-020.md)

> Verbatim text extracted from the original (FFIEC, 2020-06-17), part 19 of 32, pp. 196-206. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **legal requirement**.[^original]

## Bank Secrecy Act/ Anti-Money Laundering Examination Manual


### Risk Mitigation


#### Funds Transfers — Overview


[pp. 196-197]

Payment systems in the United States consist of numerous financial intermediaries, financial services firms, and nonbank businesses that create, process, and distribute payments. The domestic and international expansion of the banking industry and nonbank financial services has increased the importance of electronic funds transfers, including funds transfers made through the wholesale payment systems. Additional information on the types of wholesale payment systems is available in the FFIEC _Information Technology Examination Handbook._200

##### Funds Transfer Services

The vast majority of the value of U.S. dollar payments, or transfers, in the United States is ultimately processed through wholesale payment systems, which generally handle largevalue transactions between banks. Banks conduct these transfers on their own behalf as well as for the benefit of other financial service providers and bank customers, both corporate and consumer.

Related retail transfer systems facilitate transactions such as automated clearing houses (ACH); automated teller machines (ATM); point-of-sales (POS);, telephone bill paying; home banking systems; and credit, debit, and prepaid cards. Most of these retail transactions are initiated by customers rather than by banks or corporate users. These individual transactions may then be batched in order to form larger wholesale transfers, which are the focus of this section.

The two primary domestic wholesale payment systems for interbank funds transfers are the Fedwire Funds Service (Fedwire® )201 and the Clearing House Interbank Payments System (CHIPS).202 The bulk of the dollar value of these payments is originated electronically to make large value, time-critical payments, such as the settlement of interbank purchases and sales of federal funds, settlement of foreign exchange transactions, disbursement or repayment of loans; settlement of real estate transactions or other financial market transactions; and purchasing, selling, or financing securities transactions. Fedwire and CHIPS participants facilitate these transactions on their behalf and on behalf of their customers, including nonbank financial institutions, commercial businesses, and correspondent banks that do not have direct access.

Structurally, there are two components to funds transfers: the instructions, which contain information on the sender and receiver of the funds, and the actual movement or transfer of

> 200 Refer to the FFIEC _Information Technology Examination Handbook_ .

> 201 Fedwire  Services is a registered service mark of the Federal Reserve Banks.

> 202 CHIPS is a private multilateral settlement system owned and operated by The Clearing House Payments Co., LLC.

Funds Transfers — Overview

[pp. 197-198]

funds. The instructions may be sent in a variety of ways, including by electronic access to networks operated by the Fedwire or CHIPS payment systems; by access to financial telecommunications systems, such as Society for Worldwide Interbank Financial Telecommunication (SWIFT); or e-mail, facsimile, telephone, or telex. Fedwire and CHIPS are used to facilitate U.S. dollar transfers between two domestic endpoints or the U.S. dollar segment of international transactions. SWIFT is an international messaging service that is used to transmit payment instructions for the vast majority of international interbank transactions, which can be denominated in numerous currencies.

##### Fedwire

Fedwire is operated by the Federal Reserve Banks and allows a participant to transfer funds from its master account at the Federal Reserve Banks to the master account of any other bank.203 Payment over Fedwire is final and irrevocable when the Federal Reserve Bank either credits the amount of the payment order to the receiving bank’s Federal Reserve Bank master account or sends notice to the receiving bank, whichever is earlier. Although there is no settlement risk to Fedwire participants, they may be exposed to other risks, such as errors, omissions, and fraud.

Participants may access Fedwire by three methods:

- Direct mainframe-to-mainframe (Fedline Direct).

- Internet access over a virtual private network to Web-based applications (FedLine Advantage).

- Off-line or telephone-based access to a Federal Reserve Bank operations site.

##### CHIPS

CHIPS is a privately operated, real-time, multilateral payments system typically used for large-dollar payments. CHIPS is owned by banks, and any banking organization with a regulated U.S. presence may become a participant in the system. Banks use CHIPS for the settlement of both interbank and customer transactions, including, for example, payments associated with commercial transactions, bank loans, and securities transactions. CHIPS also plays a large role in the settlement of USD payments related to international transactions, such as foreign exchange, international commercial transactions, and offshore investments.

203 An entity eligible to maintain a master account at the Federal Reserve is generally eligible to participate in the Fedwire Funds Service. These participants include:

- Depository institutions.

- U.S. agencies and branches of foreign banks.

- Member banks of the Federal Reserve System.

> • The U.S. Treasury and any entity specifically authorized by federal statute to use the Federal Reserve Banks as fiscal agents or depositories.

- Entities designated by the Secretary of the Treasury.

- Foreign central banks, foreign monetary authorities, foreign governments, and certain international organizations.

- Any other entity authorized by a Federal Reserve Bank to use the Fedwire Funds Service.

Funds Transfers — Overview

##### Continuous Linked Settlement (CLS) Bank

[pp. 198-199]

CLS Bank is a private-sector, special-purpose bank that settles simultaneously both payment obligations that arise from a single foreign exchange transaction. The CLS payment-versuspayment settlement model ensures that one payment segment of a foreign exchange transaction is settled if and only if the corresponding payment segment is also settled, eliminating the foreign exchange settlement risk that arises when each segment of the foreign exchange transaction is settled separately. CLS is owned by global financial institutions through shareholdings in CLS Group Holdings AG, a Swiss company that is the ultimate holding company for CLS Bank. CLS Bank currently settles payment instructions for foreign exchange transactions in 17 currencies and is expected to add more currencies over time.

##### SWIFT

The SWIFT network is a messaging infrastructure, not a payments system, which provides users with a private international communications link among themselves. The actual funds movements (payments) are completed through correspondent bank relationships, Fedwire, or CHIPS. Movement of payments denominated in different currencies occurs through correspondent bank relationships or over funds transfer systems in the relevant country. In addition to customer and bank funds transfers, SWIFT is used to transmit foreign exchange confirmations, debit and credit entry confirmations, statements, collections, and documentary credits.

##### Cover Payments

A typical funds transfer involves an originator instructing its bank (the originator’s bank) to make payment to the account of a payee (the beneficiary) with the beneficiary’s bank. A cover payment occurs when the originator’s bank and the beneficiary’s bank do not have a relationship that allows them to settle the payment directly. In that case, the originator’s bank instructs the beneficiary’s bank to effect the payment and advises that transmission of funds to “cover” the obligation created by the payment order has been arranged through correspondent accounts at one or more intermediary banks.

Cross-border cover payments usually involve multiple banks in multiple jurisdictions. For U.S. dollar transactions, the intermediary banks are generally U.S. banks that maintain correspondent banking relationships with non-U.S. originators’ banks and beneficiaries’ banks. In the past, SWIFT message protocols allowed cross-border cover payments to be effected by the use of separate, simultaneous message formats:

- The MT 103 — payment order from the originator’s bank to the beneficiary’s bank with information identifying the originator and the beneficiary; and

- The MT 202 — bank-to-bank payment orders directing the intermediary banks to “cover” the originator’s bank’s obligation to pay the beneficiary’s bank.

To address transparency concerns, SWIFT adopted a new message format for cover payments (the MT 202 COV) that contains mandatory fields for originator and beneficiary information. Effective November 21, 2009, the MT 202 COV is required for any bank-tobank payment for which there is an associated MT 103. The MT 202 COV provides

Funds Transfers — Overview

[p. 199]

intermediary banks with additional originator and beneficiary information to perform sanctions screening and suspicious activity monitoring. The introduction of the MT 202 COV does not alter a U.S. bank’s OFAC or BSA/AML obligations.

The MT 202 format remains available for bank-to-bank funds transfers that have no associated MT 103 message. For additional detail about transparency in cover payments, refer to _Transparency and Compliance for U.S. Banking Organizations Conducting CrossBorder Funds Transfers_ (December 18, 2009), which can be found at each federal banking agencies’ Web site.

##### Informal Value Transfer Systems

An informal value transfer system (IVTS) (e.g., hawalas) is a term used to describe a currency or value transfer system that operates informally to transfer money as a business.204 In countries lacking a stable financial sector or with large areas not served by formal banks, IVTS may be the only method for conducting financial transactions. Persons living in the United States may also use IVTS to transfer funds to their home countries.

IVTS may legally operate in the United States as a Money Services Business, and specifically as a type of money transmitter, so long as they abide by applicable state and federal laws. This includes registering with FinCEN and complying with BSA/AML provisions applicable to all money transmitters. A more sophisticated form of IVTS operating in the United States often interacts with other financial institutions in storing currency, clearing checks, remitting and receiving funds, and obtaining other routine financial services, rather than acting independently of the formal financial system.

##### Payable Upon Proper Identification Transactions

One type of funds transfer transaction that carries particular risk is the payable upon proper identification (PUPID) service. PUPID transactions are funds transfers for which there is no specific account to deposit the funds into and the beneficiary of the funds is not a bank customer. For example, an individual may transfer funds to a relative or an individual who does not have an account relationship with the bank that receives the funds transfer. In this case, the beneficiary bank may place the incoming funds into a suspense account and ultimately release the funds when the individual provides proof of identity. In some cases, banks permit noncustomers to initiate PUPID transactions. These transactions are considered extremely high risk and require strong controls.

> 204 Sources of information on IVTS include:

> • FinCEN Advisory FIN-2010-A011, _Informal Value Transfer Systems_ , September 2010

- FinCEN Advisory 33, _Informal Value Transfer Systems_ , March 2003.

> • U.S. Treasury _Informal Value Transfer Systems Report to the Congress in Accordance with Section 359 of the Patriot Act_ , November 2002.

[pp. 199-200]

> • Financial Action Task Force on Money Laundering (FATF), _Interpretative Note to Special Recommendation VI: Alternative Remittance_ , June 2003.

> • FATF, _Combating the Abuse of Alternative Remittance Systems, International Best Practices_ , October 2002.

Funds Transfers — Overview

##### Risk Factors

Funds transfers may present a heightened degree of risk, depending on such factors as the number and dollar volume of transactions, geographic location of originators and beneficiaries, and whether the originator or beneficiary is a bank customer. The size and complexity of a bank’s operation and the origin and destination of the funds being transferred determine which type of funds transfer system the bank uses. The vast majority of funds transfer instructions are conducted electronically; however, examiners need to be mindful that physical instructions may be transmitted by other informal methods, as described earlier.

Cover payments effected through SWIFT pose additional risks for an intermediary bank that does not receive either a MT 103 or an adequately completed MT 202 COV that identifies the originator and beneficiary of the funds transfer. Without this data, the intermediary bank is unable to monitor or filter payment information. This lack of transparency limits the U.S. intermediary bank’s ability to appropriately assess and manage the risk associated with correspondent and clearing operations, monitor for suspicious activity, and screen for OFAC compliance.

IVTS pose a heightened concern because they are able to circumvent the formal system. The lack of recordkeeping requirements coupled with the lack of identification of the IVTS participants may attract money launderers and terrorists. IVTS also pose heightened BSA/AML concerns because they can evade internal controls and monitoring oversight established in the formal banking environment. Principals that operate IVTS frequently use banks to settle accounts.

The risks of PUPID transactions to the beneficiary bank are similar to other activities in which the bank does business with noncustomers. However, the risks are heightened in PUPID transactions if the bank allows a noncustomer to access the funds transfer system by providing minimal or no identifying information. Banks that allow noncustomers to transfer funds using the PUPID service pose significant risk to both the originating and beneficiary banks. In these situations, both banks have minimal or no identifying information on the originator or the beneficiary.

##### Risk Mitigation

Funds transfers can be used in the placement, layering, and integration stages of money laundering. Funds transfers purchased with currency are an example of the placement stage. Detecting unusual activity in the layering and integration stages is more difficult for a bank because transactions may appear legitimate. In many cases, a bank may not be involved in the placement of the funds or in the final integration, only the layering of transactions. Banks should consider all three stages of money laundering when evaluating or assessing funds transfer risks.

[pp. 200-201]

Banks need to have sound policies, procedures, and processes to manage the BSA/AML risks of its funds transfer activities. Such policies may encompass more than regulatory recordkeeping minimums and be expanded to cover OFAC obligations. Funds transfer policies, procedures, and processes should address all foreign correspondent banking activities, including transactions in which U.S. branches and agencies of foreign banks are intermediaries for their head offices.

Funds Transfers — Overview

Obtaining CDD information is an important risk mitigation step in providing funds transfer services. Because of the nature of funds transfers, adequate and effective CDD policies, procedures, and processes are critical in detecting unusual and suspicious activities. An effective risk-based suspicious activity monitoring and reporting system is equally important. Whether this monitoring and reporting system is automated or manual, it should be sufficient to detect suspicious trends and patterns typically associated with money laundering.

Institutions should have processes for managing correspondent banking relationships in accordance with section 312 of the USA PATRIOT Act and corresponding regulations (31 CFR 1010.610). Correspondent bank due diligence should take into account the correspondent’s practices with regard to funds transfers effected through the U.S. bank.

U.S. banks can mitigate risk associated with cover payments by managing correspondent banking relationships, by observing The Clearing House Payments Co., LLC and the Wolfsberg Group’s best practices (discussed below) and the SWIFT standards when sending messages, and by conducting appropriate transaction screening and monitoring.

In May 2009, the Basel Committee on Banking Supervision issued a paper on cross-border cover payment messages (BIS Cover Payments Paper).205 The BIS Cover Payments Paper supported increased transparency and encouraged all banks involved in international payments transactions to adhere to the message standards developed by The Clearing House Payments Co., LLC and the Wolfsberg Group in 2007. These are:

- Financial institutions should not omit, delete, or alter information in payment messages or orders for the purpose of avoiding detection of that information by any other financial institution in the payment process;

- Financial institutions should not use any particular payment message for the purpose of avoiding detection of information by any other financial institution in the payment process;

- Subject to all applicable laws, financial institutions should cooperate as fully as practicable with other financial institutions in the payment process when requested to provide information about the parties involved; and

- Financial institutions should strongly encourage their correspondent banks to observe these principles.

In addition, effective monitoring processes for cover payments include:

- Monitoring funds transfers processed through automated systems in order to identify suspicious activity. This monitoring may be conducted after the transfers are processed, on an automated basis, and may use a risk-based approach. The MT 202 COV provides intermediary banks with useful information, which can be filtered using risk factors

[pp. 201-203]

> 205 Refer to the Basel Committee on Banking Supervision’s _Due diligence and transparency regarding cover payment messages related to cross-border wire transfers_ . In addition, during August 2009, the committee, along with the Clearinghouse Payments Co. LLC, released Q&As in order to enhance understanding of the MT 202 COV.

Funds Transfers — Overview

developed by the intermediary bank. The monitoring process may be similar to that for MT 103 payments.

- Given the volume of messages and data for large U.S. intermediary banks, a manual review of every payment order may not be feasible or effective. However, intermediary banks should have, as part of their monitoring processes, a risk-based method to identify incomplete fields or fields with meaningless data. U.S. banks engaged in processing cover payments should have policies to address such circumstances, including those that involve systems other than SWIFT.

Originating and beneficiary banks should establish effective and appropriate policies, procedures, and processes for PUPID activity including:

- Specifying the type of identification that is acceptable.

- Maintaining documentation of individuals consistent with the bank’s recordkeeping policies.

- Defining which bank employees may conduct PUPID transactions.

- Establishing limits on the amount of funds that may be transferred to or from the bank for noncustomers (including type of funds accepted (i.e., currency or official check) by originating bank).

- Monitoring and reporting suspicious activities.

- Providing enhanced scrutiny for transfers to or from certain jurisdictions.

- Identifying disbursement method (i.e., by currency or official check) for proceeds from a beneficiary bank.

Automated Clearing House Transactions — Overview

#### Automated Clearing House Transactions — Overview


[p. 203]

Objective. _Assess the adequacy of the bank’s systems to manage the risks associated with automated clearing house (ACH) and international ACH transactions (IAT) and management’s ability to implement effective monitoring and reporting systems._

The use of the ACH has grown markedly over the last several years due to the increased volume of electronic check conversion206 and one-time ACH debits, reflecting the lower cost of ACH processing relative to check processing.207 Check conversion transactions, as well as one-time ACH debits, are primarily low-dollar value, consumer transactions for the purchases of goods and services or the payment of consumer bills. ACH is primarily used for domestic payments, but the Federal Reserve Banks’ FedGlobal system208 can currently accommodate cross-border payments to several countries around the world.

In September 2006, the Office of the Comptroller of the Currency issued guidance titled _Automated Clearinghouse Activities — Risk Management Guidance._ The document provides guidance on managing the risks of ACH activity. Banks may be exposed to a variety of risks when originating, receiving, or processing ACH transactions, or outsourcing these activities to a third party.209

##### ACH Payment Systems

Traditionally, the ACH system has been used for the direct deposit of payroll and government benefit payments and for the direct payment of mortgages and loans. As noted earlier, the ACH has been expanding to include one-time debits and check conversion. ACH transactions are payment instructions to either credit or debit a deposit account. Examples of credit payment transactions include payroll direct deposit, Social Security, dividends, and interest payments. Examples of debit transactions include mortgage, loan, insurance premium, and a variety of other consumer payments initiated through merchants or businesses.

In general, an ACH transaction is a batch-processed, value-dated, electronic funds transfer between an originating and a receiving bank. An ACH credit transaction is originated by the accountholder sending funds (payer), while an ACH debit transaction is originated by the

206 In the electronic check conversion process, merchants that receive a check for payment do not collect the check through the check collection system, either electronically or in paper form. Instead, merchants use the information on the check to initiate a type of electronic funds transfer known as an ACH debit to the check writer’s account. The check is used to obtain the bank routing number, account number, check serial number, and dollar amount for the transaction, and the check itself is not sent through the check collection system in any form as a payment instrument. Merchants use electronic check conversion because it can be a more efficient way for them to obtain payment than collecting the check.

207 Refer to the NACHA Web site.

[pp. 203-204]

208 The Federal Reserve Banks operate FedACH, a central clearing facility for transmitting and receiving ACH payments, and FedGlobal, which sends cross-border ACH credits payments to more than 35 countries around the world, plus debit payments to Canada only.

> 209 Refer to OCC Bulletin 2006-39, “ _Automated Clearing House Activities: Risk Management Guidance_ ” (September 1, 2006).

Automated Clearing House Transactions — Overview

accountholder receiving funds (payee). Within the ACH system, these participants and users are known by the following terms:

- Originator. An organization or person that initiates an ACH transaction to an account either as a debit or credit.

- Originating Depository Financial Institution (ODFI). The Originator’s depository financial institution that forwards the ACH transaction into the national ACH network through an ACH Operator.

- ACH Operator. An ACH Operator processes all ACH transactions that flow between different depository financial institutions. An ACH Operator serves as a central clearing facility that receives entries from the ODFIs and distributes the entries to the appropriate Receiving Depository Financial Institution. There are currently two ACH Operators: FedACH and Electronic Payments Network (EPN).

- Receiving Depository Financial Institution (RDFI). The Receiver’s depository institution that receives the ACH transaction from the ACH Operators and credits or debits funds from their receivers’ accounts.

- Receiver. An organization or person that authorizes the Originator to initiate an ACH transaction, either as a debit or credit to an account.

- Gateway. A financial institution, ACH Operator, or ODFI that acts as an entry or exit point to or from the United States. A formal declaration of status as a Gateway is not required. ACH operators and ODFIs acting in the role of Gateways have specific warranties and obligations related to certain international entries. A financial institution acting as a Gateway generally may process inbound and outbound debit and credit transactions. ACH Operators acting as Gateways may process outbound debit and credit entries, but can limit inbound entries to credit entries only and reversals.

##### International ACH Payments

[pp. 204-205]

NACHA —The Electronic Payments Association (NACHA) issued International ACH Transaction (IAT) operating rules and formats that became effective on September 18, 2009.210 NACHA has since issued a number of modifications and refinements to their IAT operating rules. The IAT is a Standard Entry Class code for ACH payments that enables financial institutions to identify and monitor international ACH payments, and perform screening to ensure compliance with OFAC requirements. The rules require Gateways to classify payments that are transmitted to or received from a financial agency211 outside the territorial jurisdiction of the United States as IATs. The classification depends on where the financial agency that handles the payment transaction (movement of funds) is located and not the location of any other party to the transaction (e.g., the Originator or Receiver).

Under NACHA operating rules, all U.S. financial institutions that participate in the ACH Network must be able to utilize the IAT format.

210 For additional information on the IAT, refer to the NACHA Web site.

> 211 “Financial agency” means an entity that is authorized by applicable law to accept deposits or is in the business of issuing money orders or transferring funds.

Automated Clearing House Transactions — Overview

##### Definition of IAT

An IAT is an ACH entry that is part of a payment transaction involving a financial agency’s office that is not located in the territorial jurisdiction of the United States. An office of a financial agency is involved in the payment transaction if one or more of the following conditions are met:

- Holds an account that is credited or debited as part of a payment transaction; or

- Receives funds directly from a person or makes payment directly to a person as part of a payment transaction; or

- Serves as an intermediary in the settlement of any part of a payment transaction.

##### IAT Defined Terms

An “inbound entry” originates in another country and is transmitted to the United States. For example, an inbound entry could be a customer’s on-line purchase from an overseas vendor. An inbound entry could also be funding for a company payroll. Each subsequent IAT used for direct deposit would be an inbound IAT entry.

An “outbound entry” originates in the United States and is transmitted to another country. For example, IAT pension payments going from a U.S. ODFI to a U.S. RDFI in which the funds are then transferred to an account in another country would be outbound IAT entries.

##### Payment Transaction Guidance

A payment transaction is:

- An instruction of a sender to a bank to pay, or to obtain payment of, or to cause another bank to pay or to obtain payment of, a fixed or determinate amount of money that is to be paid to, or obtained from, a Receiver, and

[pp. 205-206]

- Any and all settlements, accounting entries, or disbursements that are necessary or appropriate to carry out the instruction.

##### Identification of IAT Parties

The NACHA operating rules define parties as part of an IAT entry:

- Foreign Correspondent Bank: A participating depository financial institution (DFI) that holds deposits owned by other financial institutions and provides payment and other services to those financial institutions.

- Foreign Gateway: A Gateway that acts as an entry point to or exit point from a foreign country.

Automated Clearing House Transactions — Overview

##### Information Available Under the IAT Format

Data available to banks under the IAT format may assist banks in their OFAC, anti-money laundering, and monitoring efforts.212 Originator and receiver information available to banks under the IAT format include:

- Originator name and address.

- Receiver name and address.

- Originator and Receiver account numbers.

- ODFI name (inbound IAT, foreign DFI), identification number, and branch country code.

- RDFI name (outbound IAT, foreign DFI), identification number, and branch country code.

- Country code.

- Currency code.

- Foreign Exchange indicator.

Effective March 14, 2014, a Gateway must identify within an inbound IAT entry:

- The ultimate foreign beneficiary of the funds transfer when the proceeds from a debit inbound IAT entry are “for further credit to” an ultimate foreign beneficiary that is other than the Originator of the debit IAT entry, or

- The foreign party funding a credit inbound IAT entry when that party is not the Originator of the credit IAT entry.

Refer to www.nacha.org/c/IATIndustryInformation.cfmfor more information on additional data available to banks under the new IAT format.

##### Third-Party Service Providers

A third-party service provider (TPSP) is an entity other than an Originator, ODFI, or RDFI that performs any functions on behalf of the Originator, the ODFI, or the RDFI with respect to the processing of ACH entries. For example, a bank may hire a TPSP to conduct ACH activities on behalf of the bank.213 NACHA operating rules define TPSPs and relevant subsets of TPSPs that include “Third-Party Senders” and “Sending Points.”214 A third-party

212 For convenience, this information is sometimes referred to as “Travel Rule” information, but as a technical matter the funds transfer recordkeeping and travel rules at 31 CFR 1010.410(f)) do not apply to ACH transactions and NACHA operating rules have not changed.


---

[previous part](text-018.md) | [source overview](overview.md) | [next part](text-020.md)

[^original]: FFIEC, "FFIEC Bank Secrecy Act/Anti-Money Laundering Examination Manual" (2020-06-17). https://bsaaml.ffiec.gov/manual
