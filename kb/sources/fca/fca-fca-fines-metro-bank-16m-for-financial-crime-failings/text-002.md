---
type: Source Text
title: FCA fines Metro Bank £16m for financial crime failings - part 2 of 6 (pp. 8-20)
description: 'Verbatim extracted text, pp. 8-20: 3. DEFINITIONS; Background; Overview of legal and regulatory obligations; and 3 more sections'
resource: https://www.fca.org.uk/news/press-releases/fca-fines-metro-bank-16m-financial-crime-failings
tags:
- data_features
- enforcement
- enforcement_notice
- supervisory_expectation
- transaction_behaviour
- uk
status: stable
source_id: fca-fca-fines-metro-bank-16m-for-financial-crime-failings
issuer: fca
issuer_name: Financial Conduct Authority
jurisdictions:
- UK
tier: 1
instrument_type: enforcement_notice
normative_force: supervisory_expectation
publication_date: '2024-11-11'
legal_status: current
part: 2
parts_total: 6
content_mode: full_text
generated:
  by: process:fincrime-kb-build
  at: '2026-11-22T04:56:05Z'
verified:
- by: process:kb-validate/verbatim-coverage
  at: '2026-11-22T04:56:05Z'
sources:
- id: original
  resource: https://www.fca.org.uk/news/press-releases/fca-fines-metro-bank-16m-financial-crime-failings
  title: FCA fines Metro Bank £16m for financial crime failings
  author: org:fca
  last_modified: '2025-12-05T00:00:00Z'
---

# FCA fines Metro Bank £16m for financial crime failings

[previous part](text-001.md) | [source overview](overview.md) | [next part](text-003.md)

> Verbatim text extracted from the original (Financial Conduct Authority, 2024-11-11), part 2 of 6, pp. 8-20. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **supervisory expectation**.[^original]

## 3. DEFINITIONS


[pp. 8-9] [ref: 3.1]

- 3.1. The definitions below are used in this Notice:

“Account Record(s)” comprise details about the account including the account number.

The “Act” means the Financial Services and Markets Act 2000.

“AML” means Anti-Money Laundering.

The “ATMS” means the Automated Transaction Monitoring System in operation at Metro.

The “Authority” means the Financial Conduct Authority.

“Bad Data” means any records that were rejected from the ATMS.

The “Bad Data Report” means the internal Metro report dealing with Bad Data in more detail than the later Working Group Paper (see below).

The “Business and Commercial Support Team” means the team within Metro responsible for reviewing Customer Records rejected from the ATMS which was known as the “Account Servicing Team” until Q4 2018.

“Compliance Firm 1” was engaged by Metro in December 2018 to undertake a review of the Bank’s financial crime technology to understand whether it was aligned with standard industry practice.

“Compliance Firm 2” was engaged by Metro in December 2019 to review the end-toend architecture of the AML / transaction monitoring features of the ATMS.

“Compliance Report 1” means the compliance report produced by Compliance Firm 1.

“Compliance Report 2” means the compliance report produced by Compliance Firm 2.

“Customer Record(s)” comprise details about the customer including, for example, address and country of residence.

“DS” means Data Store, a separate database which contained a near real-time view of the data within Metro’s core banking records system. The data feed for the ATMS originated from the DS.

The “FCIP” means the Financial Crime Improvement Programme implemented by Metro post-Compliance Report 2.

The “JMLSG” means the Joint Money Laundering Steering Group. The JMLSG produces guidance for the financial services sector relating to compliance with AML and counter terrorist financing legislation and the associated regulations.

The “Lookback Audit” means the audit of the Lookback Review performed by Metro in Q4 2020.

The “Lookback Review” means a transaction monitoring lookback review initiated by Metro, which involved identifying all accounts missing from the ATMS as of 1 July 2019.

“Metro” or the “Bank” means Metro Bank Plc.

The “Operations Risk Board” means the Financial Crime Operations Risk Board at Metro.

The “PRA” means the Prudential Regulation Authority.

“Referential Integrity” means the requirement for the ATMS to have the associated Customer Record (including details about the customer) and Account Record (including the account number) in order to successfully acquire a Transaction Record and monitor that transaction. If Referential Integrity did not exist in Customer, Account and Transaction Records, the ATMS rejected the acquisition of the associated record(s).

The “Regulations” means the Money Laundering Regulations 2007.

[pp. 9-10]

The “Relevant Period” is 6 June 2016 to 17 December 2020.

The “Reports” means the Bad Data Report and the Working Group Paper (see below).

The “Technology Steering Committee” means the Financial Crime Technology (ATMS) Steering Committee at Metro.

The “Time Stamp Code Logic Error” refers to an issue which was caused by an error in the data extraction methodology from the Bank’s DS for loading into the ATMS. This affected Account Records, and because of Referential Integrity it caused associated Transaction Records to be rejected by the ATMS where a customer had opened an account and transacted on the same day.

“Transaction Record(s)” comprise details about individual transactions.

The “Tribunal” means the Upper Tribunal (Tax and Chancery Chamber).

The “Working Group” means the Financial Crime Working Group at Metro.

The “Working Group Paper” means the Financial Crime Working Group paper summarising the issues in relation to Bad Data as understood at the time within Metro dated 19 April 2018.

## Background


[p. 10] [ref: 4.1]

Metro Bank Plc

- 4.1. Metro is an authorised firm that is regulated by the Authority and the PRA. It is 100% owned by Metro Bank Holdings Plc, which is listed on the main market of the London Stock Exchange.

- 4.2. Metro was established in 2010 and offers retail, business, commercial and private banking services.

Principles for Businesses / Senior Management Arrangements, Systems and Controls

- 4.3. Metro was required, pursuant to Principle 3 of the Authority’s Principles for Businesses, to take reasonable care to organise its affairs responsibly and effectively, with adequate risk management systems.

## Overview of legal and regulatory obligations


[pp. 10-11] [ref: 4.4]

- 4.4. Under the chapter of the Authority’s Handbook entitled Senior Management Arrangements, Systems and Controls (“SYSC”), Metro was also required to:

- 4.4.1 establish, implement and maintain adequate policies and procedures sufficient for ensuring the compliance of the firm with its obligations under the regulatory system and for countering the risk that it might be used to further financial crime (SYSC 6.1.1R);

- 4.4.2 ensure that those policies and procedures include systems and controls that enable it to identify, assess, monitor and manage money laundering risk and were comprehensive and proportionate to the nature, scale and complexity of its activities (SYSC 6.3.1R); and

- 4.4.3 carry out a regular assessment of the adequacy of those systems and controls to ensure that they continue to comply with SYSC 6.3.1R (SYSC 6.3.3R).

## Money Laundering Regulations 2007


[pp. 11-12] [ref: 4.5]

- 4.5. Metro had a separate obligation to comply with relevant legal requirements under the Money Laundering Regulations 2007 (the “Regulations”).

_Requirement to carry on ongoing monitoring_

- 4.6. The Regulations required firms to carry out ongoing monitoring of a business relationship on a risk-sensitive basis (Regulation 8). The purpose of conducting ongoing monitoring is to scrutinise transactions to ensure they are consistent with the firm’s knowledge of the customer and to identify patterns of behaviour that appear characteristic of either money laundering or terrorist financing and which, after analysis, may lead to suspicions of money laundering or terrorist financing. Ongoing monitoring can also help firms to know their customers, assess risk and provide assurance that the firm is not being used for the purposes of financial crime.

_Requirement to have appropriate and risk-sensitive policies and procedures_

- 4.7. In order to prevent activities related to money laundering and terrorist financing, the Regulations further required firms to establish and maintain appropriate and risksensitive policies and procedures relating to, amongst other things, the ongoing monitoring of business relationships (Regulation 20(1)(a)). In addition, firms were required to establish and maintain appropriate and risk-sensitive policies and

procedures relating to the monitoring and management of compliance with, and internal communication of, those policies and procedures (Regulations 20(1)(f)).

- 4.8. Those policies and procedures referred to above had to provide for the identification and scrutiny of:

- 4.8.1. complex or unusually large transactions;

- 4.8.2. unusual patterns of transactions with no apparent economic or visible lawful purpose; and

- 4.8.3. any other activity which the firm regarded as particularly likely by its nature to be related to money laundering or terrorist financing.

## Joint Money Laundering Steering Group Guidance


[pp. 12-13] [ref: 4.9]

- 4.9. SYSC 6.3.5G provides that the Authority, when considering whether a breach of its rules on systems and controls against money laundering has occurred, will have regard to whether a firm has followed relevant provisions in the guidance for the United Kingdom financial sector issued by the Joint Money Laundering Steering Group (“JMLSG”). Guidance concerning monitoring customer activity is set out below and reflects the JMLSG Guidance 2014 and JMLSG Guidance 2017.

- 4.10. Essential to a monitoring system is that it flags up transactions and / or activities for further examination, ensures the reports (referred to in this Notice as “alerts”) are reviewed promptly by the right person and appropriate action is taken on the findings of any further examination (paragraph 5.7.3, Chapter 5, Part 1).

- 4.11. The scope and complexity of the monitoring process will be influenced by a firm’s business activities and whether the firm is large or small (paragraph 5.7.8, Part 1, Chapter 5). A monitoring system may be manual or automated but for firms where there are major issues of volume, a more sophisticated automated system may be necessary (paragraph 5.7.13, Part 1, Chapter 5). The greater the volume of transactions, the less easy it will be for a firm to monitor them without the aid of some form of automation (paragraph 5.7.16, Part 1, Chapter 5). Firms should understand the workings and rationale of an automated system, and should understand the reasons for its output of alerts (paragraph 5.7.15, Part 1, Chapter 5).

The implementation of the ATMS

- 4.12. Having committed to implementing an ATMS, at the planning stage, Metro defined the high-level business requirements for the ATMS. In terms of “core functionality”, Metro stated that the system(s) had to be capable of performing and supporting Metro’s processes, to a standard which complied with all legal and regulatory requirements and the Bank’s own risk appetite. Consequently, the transaction monitoring requirements that were stipulated by Metro as “must haves” for the ATMS included the ability to perform real-time monitoring of all retail and commercial transactions, and the ability to monitor all current and future transaction types across all current and future Metro products.

[pp. 13-14] [ref: 4.13]

- 4.13. In order for monitoring to take place, Customer Records, Account Records and Transaction Records needed to be fed into the ATMS. As a means of feeding the Customer, Account and Transaction Records held in Metro’s core banking system into the ATMS, Metro opted to use the DS, which was a separate database within the Bank which contained a near real-time view of the data within Metro’s core banking records system. Metro decided to use the DS to feed data into the ATMS for a variety of reasons, including operational resilience.

- 4.14. The data feed from the DS to the ATMS comprised “batch files” which contained the Customer Records, Account Records and Transaction Records. In this regard:

- 4.14.1 Customer Records comprised details about the customer including, for example, address and country of residence. Customer Records were sent to the ATMS when a customer record was created for new customers or when an existing customer record was updated, for example, if an existing customer updated their address.

- 4.14.2 Account Records comprised details about the account including the account number.

- 4.14.3 Transaction Records comprised details about individual transactions.

- 4.15. Each of these three sets of records were required in order for the ATMS to effectively monitor customer transactions, as follows: For the ATMS to successfully acquire Transaction Records, the associated Account Records had to be present in the ATMS; for the ATMS to successfully acquire Account Records, the associated Customer Record

had to be present in the ATMS. Requiring the associated Customer Record and Account Record for each Transaction Record was known as “Referential Integrity”. If Referential Integrity did not exist in Customer, Account and Transaction Records, the ATMS would reject the acquisition of an Account Record where a Customer Record was not present and reject the acquisition of a Transaction Record where an Account Record was not present.

- 4.16. Where records were acquired by the ATMS (as opposed to being rejected), they would be subject to ongoing monitoring. Records rejected by the ATMS, which were described within Metro as “Bad Data”, would be put into Bad Data folders (see paragraphs 4.55 to 4.56). In circumstances where a record in the Bad Data folder comprised a failed update to an existing record (for example, the Customer Record was already in the ATMS but a change to this Customer Record was rejected because an updated address did not include a postcode), transactions on the Account Records attached to the existing Customer Record were still monitored.

- 4.17. The ATMS went live on 6 June 2016.

## The Time Stamp Code Logic Error


[pp. 14-15] [ref: 4.18]

- 4.18. On 17 April 2019, during testing of an upgrade to Metro’s core banking records system, Metro identified the Time Stamp Code Logic Error. This issue was caused by an error in the data extraction methodology from the Bank’s DS for loading into the ATMS, which caused certain transactions to be rejected by the ATMS. This issue had been present since the introduction of the ATMS by Metro in June 2016 and, as such, it had not been identified for a period of almost three years, despite the fact that it resulted in large numbers of transactions not being monitored (see paragraphs 4.74 to 4.76).

- 4.19. Metro discovered that, in circumstances where (a) a customer had opened an account and (b) made transactions on the same day, the Customer Records and Transaction Records were extracted from the source data and included in the data feed from the DS to the ATMS in the correct way, but the Account Records were not being included in the data feed from the DS to the ATMS. This was due to a technical flaw whereby the timestamp on the Account Records was “processing day +1”, whereas the logic used to populate the ATMS batch file looked for a timestamp of “processing day -1”. Because of this incompatibility, the Account Records were not extracted from the DS.

- 4.20. Due to Referential Integrity, where there was an absence of an Account Record in the ATMS, all Transaction Records related to that account would be rejected. Thus the Time Stamp Code Logic Error caused all transactions on the affected accounts to be rejected from the ATMS. At the time of the Lookback Review, Metro understood this issue to occur from the opening of the account until there was a day on which there were no transactions on the account, and the ATMS could reconfigure. Following the end of the Relevant Period, Metro established that the issue occurred if and until there was an update to the Account Record, and the ATMS could reconfigure.

- 4.21. In addition, it was not possible to load transactions into the ATMS retrospectively as each Transaction Record had a date-stamp on it and, once the system date had moved beyond this date-stamp, the transaction could not be loaded into the ATMS.

- 4.22. Metro notified the Authority about the Time Stamp Code Logic Error on 29 May 2019 and a tactical fix to remedy the Time Stamp Code Logic Error was implemented on 21 July 2019.

- 4.23. However, by this time, the Time Stamp Code Logic Error had impacted in the region of 166,000 accounts, meaning that over 46.5 million transactions related to those accounts with an associated value of over £31.5 billion had not been monitored.

[pp. 15-16] [ref: 4.24]

- 4.24. The Authority considers it a serious failure in the operation and oversight of the ATMS that the Time Stamp Code Logic Error was allowed to persist for over three years, since the implementation of the ATMS, before being identified and rectified. During the intervening period, large numbers of transactions which should have been monitored for AML purposes were not, meaning that there was an enhanced risk of Metro being used to facilitate money laundering during the Relevant Period.

The Time Stamp Code Logic Error and lack of an effective reconciliation process

- 4.25. The failure by Metro to identify the Time Stamp Code Logic Error in a timely manner arose, in part, as a result of the fact that, before the Lookback Review in July 2019, Metro took no steps to check the completeness of data fed into the ATMS. Throughout 2020, Metro performed a number of ad-hoc reconciliations to check the completeness of the data feed, but these only related to Customer Records and Account Records and did not cover Transaction Records. Prior to 17 December 2020, Metro failed to put in place an effective reconciliation process between the DS and the destination ATMS in

order to ensure that all Customer, Account and Transaction Records were loading correctly.

- 4.26. Data reconciliation in this context is the process of validating data that is fed from a firm’s source systems to the transaction monitoring system to confirm it is complete. If the data differs between the source systems and the ATMS, then this suggests that transactions are not being loaded into the ATMS and as a result not being monitored by the ATMS, which would therefore not generate alerts where appropriate.

- 4.27. In this way, the Authority considers that an effective reconciliation process between the DS and the ATMS was a key part of the Bank’s transaction monitoring system which should have been in place from the inception of the ATMS in June 2016. However, prior to the Lookback Review in July 2019 (see paragraphs 4.33 to 4.45) there was no reconciliation between the DS and the ATMS. Further, there was no set procedure for undertaking regular reconciliations between the DS and the ATMS, so as to ensure that all Customer, Account and Transaction Records were being correctly received by the ATMS on an ongoing basis, from the ATMS going live on 6 June 2016 until the implementation of a count check control in December 2020.

- 4.28. Metro performed a number of ad hoc reconciliations over the course of 2020, relating to Account Records and Customer Records, but not Transaction Records:

[pp. 16-17] [ref: 4.28.1]

- 4.28.1. In March 2020, Metro performed a reconciliation of Account Records present in the DS and Account Records present in the ATMS. This identified that 125 accounts of the 374,593 accounts opened in the period to 31 March 2020 ought to have fed into the ATMS but had failed to do so and, of these, 106 accounts had failed to load due to data validation issues.

- 4.28.2. In July 2020, Metro compared the volume of customers in the DS against the volume of customers in the ATMS. The exercise found that there was a discrepancy of 3,135 between active Customer Records for transaction monitoring in the ATMS (1,138,196) and the expected figure from the DS (1,141,331).

- 4.28.3. In September 2020, Metro checked the number of Customer Records that were not updated successfully in the ATMS against the overall population of Customer Records in the DS. This established that 3,282 Customer Records had been rejected due to data validation issues however, of these, 955

Customer Records were inactive. Of the remaining population of 2,327 active records, only 30 customer records that could not be updated were in scope for transaction monitoring.

- 4.29. These reconciliations provided Metro with assurance, at the point they were completed, of the coverage of the Customer and Account Records in the ATMS. Following each of these exercises, Metro took steps to remediate the records identified as missing and manually load these into the system.

- 4.30. However, the performance of these ad hoc reconciliations was inadequate, in the absence of a formal procedure for checking the completeness of the data (including Customer, Account and Transaction Records) in the ATMS on an ongoing basis.

- 4.31. On 17 December 2020, the DS commenced sending daily “count files” along with each of the batch files to the ATMS. The count files included figures for all Customer, Account and Transaction Records and enabled Metro to compare the total number of records received by the ATMS, plus the records rejected from the ATMS and placed into Bad Data folders, to the total number of records sent to the ATMS from the DS on an ongoing basis. Where the totals did not match, emails were generated and sent to Financial Crime Operations in order to alert them to the disparity. Prior to this control being implemented, Metro had no mechanism for checking on an ongoing basis whether all records that were intended to be monitored by the ATMS were successfully received by the ATMS from the DS. As such, the Authority considers that Metro only put into place an effective reconciliation process as part of its monitoring system on 17 December 2020 (marking the end of the Relevant Period).

[pp. 17-18] [ref: 4.32]

- 4.32. The Authority considers that it was a serious failure on the part of Metro not to ensure that there was an effective reconciliation process in relation to the data received by the ATMS at the time it was implemented. The Authority further considers that, if an effective reconciliation process had been put in place in June 2016, then the Time Stamp Code Logic Error could have been identified and rectified sooner, and the missing transactions could have been monitored for potentially suspicious activity well before Metro commenced its remediation project in July 2019.

Time Stamp Code Logic Error Remediation Project - the Lookback Review and the Lookback Audit

- 4.33. A remediation project, the transaction monitoring lookback review (the “Lookback Review”), was initiated by Metro in July 2019 after it identified the Time Stamp Code Logic Error.

- 4.34. As part of the Lookback Review, Metro undertook a reconciliation exercise comparing a full list of the accounts in the DS with the accounts in the ATMS as of 1 July 2019, with a view to identifying and remediating all accounts missing from the ATMS. Metro identified that approximately 238,000 accounts were missing from the ATMS. Of these, 166,358 accounts were missing because of the Time Stamp Code Logic Error.

- 4.35. The remaining 71,627 accounts were not affected by the Time Stamp Code Logic Error and were missing from the ATMS for other reasons. There had been no transactions on 71,378 of these accounts and the remaining 249 accounts had been opened prior to the implementation of the ATMS. Metro did not undertake a targeted root cause analysis to understand why the 71,627 accounts were missing from the ATMS at that time as it instructed a third-party, Compliance Firm 2, to undertake a review of the end-to-end architecture of the AML / transaction monitoring features of the ATMS in December 2019.

[pp. 18-19] [ref: 4.36]

- 4.36. At the time of the Lookback Review, the 238,000 accounts that were identified as missing from the ATMS were incorrectly thought to be associated with 152,225 customers (see paragraph 4.40 below for further details of how this was confirmed to be an underestimation of the number of customers, during the Lookback Audit). At this time, Metro understood that these customers had a further 143,823 associated accounts, which had previously been fed into the ATMS and had been subject to ongoing monitoring. However, these associated accounts were included within the scope of the Lookback Review _“in order to ensure that the customer focused detection scenarios operated correctly”_ , on the basis that the behaviour of each customer would not have been evaluated correctly had a full set of their accounts not been included in the review _._ As a result, there were over 381,000 accounts within the scope of the Lookback Review _._

- 4.37. Once the number of accounts missing from the ATMS had been identified, in effect, the Lookback Review replicated the ATMS transaction monitoring scenarios over the accounts which were missing from the ATMS and the associated accounts of those customers. This resulted in the generation of 10,162 alerts indicating that unusual or

uncharacteristic transactional activity had taken place on those customers’ accounts, which the Bank’s alert review team then reviewed (see paragraph 4.43).

- 4.38. In Q4 2020, Metro performed an audit of the Lookback Review (the “Lookback Audit”). The Lookback Audit identified that a coding error had occurred which had led to a material reduction in the scope of customers that had been included in the Lookback Review. The Lookback Audit report, which was finalised in May 2021, concluded that, as a result of this error, a potentially significant number of customers (over 1,400) and over 4,000 alerts had been excluded from the Lookback Review.

- 4.39. After the Lookback Audit, an additional alert file was generated, containing an additional 4,946 alerts across 1,742 customers.

- 4.40. Following the Lookback Audit, it was confirmed that the circa 238,000 accounts that were identified as missing from the ATMS were, in fact, associated with 212,205 customers (as opposed to 152,225 customers as incorrectly identified by the Lookback Review) and that these customers had 290,011 associated accounts (as opposed to 143,823 associated accounts) that had previously been subject to transaction monitoring. The additional 146,188 accounts were also included in the review to enable a more comprehensive assessment, once again, on the basis that the behaviour of each customer would not have been evaluated correctly had a full set of their accounts not been included in the review.

[pp. 19-20] [ref: 4.41]

- 4.41. Overall, the Lookback Review and the Lookback Audit considered approximately 112.7 million transactions of approximately 212,000 customers across approximately 528,000 accounts and generated 15,108 alerts.

- 4.42. In total, 46,662,134 previously unmonitored transactions were included in the scope of the Lookback Review. The value of these transactions was £31,637,046,957.

- 4.43. These unmonitored transactions were only reviewed after the event, during the periods April 2020 to October 2020 (as part of the Lookback Review) and January 2022 to March 2022 (following the Lookback Audit of the Lookback Review). Following each of these reviews, the Bank submitted a number of additional suspicious activity reports (124 and 29, respectively). Metro also issued notices to customers closing their accounts (36 and 7, respectively). Prior to the Lookback Review, Metro had made 1,403 suspicious activity reports in respect of customers included in the Lookback Review.

- 4.44. The Authority considers that there was a lengthy delay in the identification of certain suspicious activity and, therefore, an increased risk that money laundering and/or terrorist financing had gone undetected for a significant period of time.

- 4.45. The Lookback Audit concluded in March 2022, almost three years after the Lookback Review first commenced and almost six years after the ATMS had been implemented.

The Time Stamp Code Logic Error and Bad Data

- 4.46. As explained above, the Time Stamp Code Logic Error occurred due to an error in the data feed methodology whereby, in circumstances where a customer account was opened and a transaction on that account took place on the same day, the Account Records were not included in the data feed from the DS to the ATMS. This, in turn, meant that transactions on customer accounts affected by the Time Stamp Code Logic Error were then rejected by the ATMS as Bad Data, as Referential Integrity required that Transaction Records had to have the associated Customer and Account Records in the ATMS in order for the Transaction Records to be accepted by the ATMS. Aside from the Time Stamp Code Logic Error, the ATMS also rejected Customer, Account and Transaction Records as Bad Data for other reasons. The Authority’s findings in relation to Bad Data and the inadequate manner in which Metro dealt with this issue are set out in paragraphs 4.47 to 4.73 below.


---

[previous part](text-001.md) | [source overview](overview.md) | [next part](text-003.md)

[^original]: Financial Conduct Authority, "FCA fines Metro Bank £16m for financial crime failings" (2024-11-11). https://www.fca.org.uk/news/press-releases/fca-fines-metro-bank-16m-financial-crime-failings
