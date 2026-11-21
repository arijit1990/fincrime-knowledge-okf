---
type: Source Text
title: FCA fines Metro Bank £16m for financial crime failings - part 1 of 6 (pp. 1-7)
description: 'Verbatim extracted text, pp. 1-7: FINAL NOTICE; 2. SUMMARY OF REASONS; Bad Data'
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
part: 1
parts_total: 6
content_mode: full_text
generated:
  by: process:fincrime-kb-build
  at: '2026-11-21T23:42:13Z'
verified:
- by: process:kb-validate/verbatim-coverage
  at: '2026-11-21T23:42:13Z'
sources:
- id: original
  resource: https://www.fca.org.uk/news/press-releases/fca-fines-metro-bank-16m-financial-crime-failings
  title: FCA fines Metro Bank £16m for financial crime failings
  author: org:fca
  last_modified: '2025-12-05T00:00:00Z'
---

# FCA fines Metro Bank £16m for financial crime failings

[source overview](overview.md) | [next part](text-002.md)

> Verbatim text extracted from the original (Financial Conduct Authority, 2024-11-11), part 1 of 6, pp. 1-7. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **supervisory expectation**.[^original]

## FINAL NOTICE


[p. 1] [ref: 1.1]

To: Metro Bank Plc Reference Number: 488982 Address: 1 Southampton Row, London, WC1B 5HA Date: 12 November 2024

- 1.1. For the reasons given in this Final Notice, the Authority hereby imposes on Metro Bank Plc (“Metro” or the “Bank”) a financial penalty of £16,675,200 pursuant to section 206 of the Act.

- 1.2 Metro agreed to resolve this matter and qualified for a 30% (stage 1) discount under the Authority’s executive settlement procedures. Were it not for this discount, the Authority would have imposed a financial penalty of £23,821,700 on Metro.

## 2. SUMMARY OF REASONS


[pp. 1-2] [ref: 2.1]

- 2.1. Metro is an authorised firm that is regulated by the Authority and the Prudential Regulation Authority (“PRA”). Metro was established in 2010. It offers retail, business, commercial and private banking services.

- 2.2. The Authority has the operational objective of protecting and enhancing the integrity of the UK financial system. Money laundering through UK financial institutions undermines the integrity of the UK financial system.

- 2.3. Under the Authority’s rules, financial institutions operating in the UK are responsible for minimising their risk of being used for criminal purposes, including the risk of being used to facilitate money laundering or terrorist financing. To mitigate this risk (and as

part of their obligation to take reasonable care to organise and control their affairs responsibly and effectively, with adequate risk management systems), firms must establish and maintain an adequate risk-based anti-money laundering (“AML”) control framework. They must also comply with the applicable Money Laundering Regulations.

- 2.4. The Money Laundering Regulations 2007 (the “Regulations”) were in effect during the Relevant Period, namely from 6 June 2016 to 17 December 2020. The Regulations required firms, amongst other things, to conduct ongoing monitoring of business relationships and to establish and maintain appropriate and risk-sensitive policies and procedures relating to ongoing monitoring. The purpose of conducting ongoing monitoring is to scrutinise transactions in order to ensure that they are consistent with the firm’s knowledge of the customer and to identify patterns of behaviour which appear characteristic of either money laundering or terrorist financing and which, after analysis, may lead to suspicions of money laundering or terrorist financing. Ongoing monitoring can also assist firms in knowing their customers, the assessment of risk and provide assurance that the firm is not being used to facilitate financial crime.

- 2.5. On 6 June 2016 (the start of the Relevant Period), Metro implemented an Automated Transaction Monitoring System (“ATMS”) to monitor customer transactions. As it transpired, there were serious deficiencies in relation to the set-up, operation and oversight of the ATMS which were not identified and/or remedied by Metro within an acceptable period of time. Over the Relevant Period, as a result of the failings set out in this Notice, Metro failed to monitor over 60 million transactions (circa 6.0% of the total transaction volume) with a value of over £51 billion (circa 7.6% of the total transaction value).

[pp. 2-3] [ref: 2.6]

- 2.6. Although the Authority acknowledges that many of these transactions were subsequently reviewed as part of a remediation exercise, the Lookback Review, this process was only completed a number of years after the event in 2022. The remediation resulted in Metro submitting 153 suspicious activity reports and 43 notices to customers closing their accounts. This was in addition to the 1,403 suspicious activity reports in respect of customers included in the Lookback Review and which were submitted prior to the Lookback Review.

- 2.7. Data for the ATMS originated from Metro’s Data Store (“DS”), which was a separate database within the Bank that contained a near real-time view of the data within Metro’s core banking records system. Metro decided that the data feed process to the ATMS should occur from the DS for a number of reasons, including operational resilience. In

order for monitoring to take place, the DS needed to feed Customer Records (comprising details about the customer), Account Records (comprising details of the customer’s account(s)) and Transaction Records (comprising details about the customer’s account transaction(s)) into the ATMS.

The Time Stamp Code Logic Error

- 2.8. Almost three years later, on 17 April 2019, during testing of an upgrade to Metro’s core banking records system, an issue referred to in this Notice as the “Time Stamp Code Logic Error” was identified by the Bank. The Bank notified the Authority about this issue on 29 May 2019.

- 2.9. In essence, the Time Stamp Code Logic Error meant that a large number of transactions had not been fed into the ATMS for ongoing monitoring, since its implementation on 6 June 2016. This issue was caused by an error in the data extraction methodology from the Bank’s DS for loading into the ATMS, which caused certain Transaction Records to be rejected by the ATMS. Specifically, where a customer had opened an account and transacted on the same day, the associated Account Record was not included in the data feed, and therefore those Transaction Records and ensuing Transaction Records were rejected by the ATMS until there was an update to the Account Record, whereupon the ATMS could reconfigure. Over an approximately three-year period from Metro’s implementation of the ATMS, the Time Stamp Code Logic Error impacted in the region of 166,000 accounts, meaning that over 46.5 million transactions related to those accounts with an associated value of over £31.5 billion had not been monitored.

[pp. 3-4] [ref: 2.10]

- 2.10. A tactical fix to remedy the Time Stamp Code Logic Error was implemented on 21 July 2019. Following application of the fix, for transactions intended for monitoring by the ATMS, at least 99.7% of Transaction Records were consistently fed into the ATMS, however Metro was not aware of this (for the reasons summarised in paragraphs 2.12 and 2.14) until after the Relevant Period.

- 2.11. The failure by Metro to identify the Time Stamp Code Logic Error in a timely manner arose, in part, as a result of the fact that, before the Lookback Review in July 2019,Metro did not check the completeness of data fed into the ATMS. Metro performed a number of ad hoc reconciliations over the course of 2020, however these did not relate to Transaction Records. These reconciliations were inadequate in the absence of a formal procedure for checking the completeness of the data (including Customer, Account and Transaction Records) in the ATMS on an ongoing basis. Prior to 17 December 2020,

Metro failed put in place an effective reconciliation process between the DS and the destination ATMS in order to ensure that all Customer, Account and Transaction Records were loading correctly. This failure to check the completeness of data fed into the ATMS during the Relevant Period significantly impacted Metro’s ability, on an ongoing basis, to identify which Customer, Account and Transaction Records were sent, or not sent, to the ATMS and consequently its ability to ensure that all of these records were monitored appropriately.

- 2.12. On 17 December 2020 (the end of the Relevant Period), the DS commenced sending daily “count files” to the ATMS. The count files included figures for all Customer, Account and Transaction Records, and enabled Metro to compare the total number of records received by the ATMS, plus the records rejected by the ATMS and placed into Bad Data folders, to the total number of records sent to the ATMS from the DS, on an ongoing basis. Where the totals did not match, emails were generated and sent to Financial Crime Operations in order to alert them to the disparity. Prior to this control being implemented, Metro had no mechanism for checking on an ongoing basis whether all records that were intended to be monitored by the ATMS were successfully received by the ATMS from the DS.

## Bad Data


[pp. 4-5] [ref: 2.13]

- 2.13. Metro also failed to put in place adequate systems and controls for managing an issue which was referred to internally as “Bad Data” and its “exceptions process” which was meant to deal with Bad Data was inadequate. In this regard, there were rules within the ATMS to prevent data loading where there were data quality issues, such as missing or incomplete data or a failure to meet prescribed criteria. Where a mandatory field was missing, the whole data record would be rejected by the ATMS and where a nonmandatory field was missing, the record might be rejected in part. “Bad Data” (as referred to within Metro) was the term used for any Customer, Account and Transaction Records that had been rejected from the ATMS. For Customer Records, these could be new records or updates to existing records.

- 2.14. The records which were rejected from the ATMS as Bad Data were placed into Bad Data folders, however Metro failed to put into place a regular review process for the Account and Transaction Records in the Bad Data folders, which were only intermittently reviewed as part of wider work to understand the Bad Data issues. In addition, it was only on 14 December 2020, when Metro implemented a fix to remove internal transactions, in respect of which monitoring was not required, from the data feed from

the DS into the ATMS, that the Bank had clear visibility of the true volume of customer transactions (as opposed to internal transactions) being rejected by the ATMS for the first time since the ATMS went live in June 2016.

- 2.15. Whilst there was an “exceptions process” within Metro which was meant to deal with one aspect of Bad Data, namely rejected Customer Records, a lack of adequate systems and controls for managing Bad Data and deficiencies in relation to the exceptions process meant that Customer, Account and Transaction Records that should have been routinely loaded into the ATMS but had been rejected, were not subject to ongoing monitoring either in a timely fashion or at all. Therefore, this impacted the generation of alerts in respect of suspicious or uncharacteristic account activity and exposed Metro to financial crime risk.

Oversight and Governance

- 2.16. Bad Data was recognised as a risk and a serious issue at comparatively less senior grades within Metro and individual staff members investigated and attempted to escalate this issue to more senior staff and Committees in 2017 and 2018. In particular, the issue was raised at Metro’s Financial Crime Steering Group, which was responsible for overseeing financial crime issues, in January 2018 when it agreed to undertake a review of the issue. However, this decision was subsequently removed from the final minutes of the Financial Crime Steering Group’s meeting with the intention of revisiting the issue once it was better understood, and it was not discussed again until April 2019 when the Time Stamp Code Logic Error was identified.

[pp. 5-6] [ref: 2.17]

- 2.17. Members of Metro’s Financial Crime Working Group (“Working Group”), which reported into the Financial Crime Steering Group, and the Financial Crime Operations Risk Board (“Operations Risk Board”), escalated the issue of Bad Data to senior staff in Metro in 2018. The risk in relation to this issue was passed to a more junior member of staff to liaise with a senior member of staff, although the Authority understands that Metro has no formal records to demonstrate that such an escalation took place. In any event, no substantive action was taken.

- 2.18. Metro instructed two external compliance firms, one at the end of 2018, and a second at the end of 2019. These external reviews enabled Metro better to understand the issues with its ATMS and to implement a remediation programme to improve the applicable controls. Metro subsequently made significant enhancements to the Bank’s

end-to-end architecture and data controls to ensure that the data fed into the ATMS is complete and accurate.

- 2.19. Metro was required, pursuant to Principle 3 of the Authority’s Principles for Businesses, to take reasonable care to organise and control its affairs responsibly and effectively, with adequate risk management systems. Under the Authority’s rules, Metro was also required to:

- 2.19.1. establish, implement and maintain adequate policies and procedures sufficient for ensuring the compliance of the firm with its obligations under the regulatory system and for countering the risk that it might be used to further financial crime;

- 2.19.2. ensure that those policies and procedures included systems and controls that (1) enabled it to identify, assess, monitor and manage money laundering risk and (2) were comprehensive and proportionate to the nature, scale and complexity of its activities; and

- 2.19.3. carry out a regular assessment of the adequacy of those systems and controls to ensure that they remained compliant.

- 2.20. During the Relevant Period, Metro failed to meet these requirements and, in doing so, breached Principle 3. In particular:

- 2.20.1. From the implementation of the ATMS on 6 June 2016, Metro failed to take any steps to check the completeness of data feeding into the ATMS, prior to identifying the Time Stamp Code Logic Error on 17 April 2019. Throughout the Relevant Period, Metro did not have controls in place to check, on an ongoing basis, that transactions that should have been monitored by the ATMS were being received by the ATMS and this contributed to the situation whereby the Time Stamp Code Logic Error continued for nearly three years before it was identified.

[pp. 6-7] [ref: 2.20.2]

- 2.20.2. There was no adequate process in place to deal with Bad Data rejected from the ATMS: Metro did not take sufficient steps to ensure that the exceptions process for dealing with rejected Customer Records was adequate and there were no processes in place to deal with rejected Account Records and Transaction Records.

- 2.20.3. Bad Data was recognised as a risk and a serious issue at comparatively less senior grades within Metro and individual staff members investigated and attempted to escalate this issue to more senior staff and Committees in 2017 and 2018. However, reference to Bad Data was removed from the Financial Crime Steering Group’s January 2018 minutes, on the basis that the Bad Data issue did not appear to be substantiated, which meant there was no action to track and monitor this risk. Members of the Working Group and the Operations Risk Board also escalated the issue of Bad Data to senior staff in 2018. Although the risk was passed to a more junior member of staff to liaise with a senior member of staff, no substantive action took place.

- 2.20.4. During the Relevant Period Metro did not have a sufficient understanding of the level of AML risk associated with unmonitored transactions. This was, in part, due to the fact that the true picture of the volume of transactions rejected by the ATMS (and which therefore went unmonitored) was obscured by the presence of internal transactions which did not need to be monitored. This issue took Metro over four years to resolve and it was only on 14 December 2020, shortly before the end of the Relevant Period, that Metro implemented a fix to remove internal transactions from the data feed into the ATMS.

- 2.21. These transaction monitoring failings resulted in over 60 million transactions with a value of over £51 billion not being monitored during the Relevant Period. Whilst m any of these transactions were subsequently reviewed as part of a remediation exercise, there was a lengthy delay in the identification of suspicious activity an d this increased the risk of Metro inadvertently being used for the purposes of financial crime.

- 2.22. The Authority acknowledges the historic nature of the failings identified in this Notice, and Metro has remediated these issues. The Authority also acknowledges that Metro has invested extensively in remediating and enhancing its financial crime framework since the events in question.

- 2.23. The Authority hereby imposes on Metro a financial penalty of £16,675,200 pursuant to section 206 of the Act.


---

[source overview](overview.md) | [next part](text-002.md)

[^original]: Financial Conduct Authority, "FCA fines Metro Bank £16m for financial crime failings" (2024-11-11). https://www.fca.org.uk/news/press-releases/fca-fines-metro-bank-16m-financial-crime-failings
