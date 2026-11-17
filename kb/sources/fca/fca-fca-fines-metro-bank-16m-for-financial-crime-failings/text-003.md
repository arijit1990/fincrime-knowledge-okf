---
type: Source Text
title: FCA fines Metro Bank £16m for financial crime failings - part 3 of 6 (pp. 20-26)
description: 'Verbatim extracted text, pp. 20-26: Bad Data; Bad Data folders; The exceptions process for Bad Data'
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
part: 3
parts_total: 6
content_mode: full_text
generated:
  by: process:fincrime-kb-build
  at: '2026-11-17T07:21:49Z'
verified:
- by: process:kb-validate/verbatim-coverage
  at: '2026-11-17T07:21:49Z'
sources:
- id: original
  resource: https://www.fca.org.uk/news/press-releases/fca-fines-metro-bank-16m-financial-crime-failings
  title: FCA fines Metro Bank £16m for financial crime failings
  author: org:fca
  last_modified: '2025-12-05T00:00:00Z'
---

# FCA fines Metro Bank £16m for financial crime failings

[previous part](text-002.md) | [source overview](overview.md) | [next part](text-004.md)

> Verbatim text extracted from the original (Financial Conduct Authority, 2024-11-11), part 3 of 6, pp. 20-26. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **supervisory expectation**.[^original]

## Bad Data


[pp. 20-21] [ref: 4.47]

- 4.47. “Bad Data” (as referred to within Metro) was a term used for any Customer, Account and Transaction Record that had been rejected from the ATMS. These rejected records were placed into Bad Data folders.

- 4.48. There were rules within the ATMS to prevent data loading where there were data quality issues, such as missing or incomplete data or a failure to meet prescribed criteria. Where a mandatory field was missing, the whole record would be rejected. Where a nonmandatory field was missing, the record might be rejected in part.

- 4.49. As referred to above at paragraph 4.15, for the ATMS to successfully acquire Transaction Records, the associated Account Records had to be in the ATMS. Likewise, for the ATMS to successfully acquire Account Records, the associated Customer Records had to be in the ATMS. This requirement was referred to as Referential Integrity and, if Referential

Integrity did not exist in respect of each of those records, the ATMS would reject their acquisition.

- 4.50. The main reasons that Customer Records were rejected by the ATMS during the Relevant Period related to issues with the address, the postcode and the country of residence of the customer (as a result of the fact that the relevant fields were either blank, incorrect or did not conform to specifications).

- 4.51. The singular reason that Account Records were rejected by the ATMS during the Relevant Period was because they were “ _Missing Primary Customer Record_ ” on the basis that, where the Customer Record was not in the ATMS (as described in the previous paragraph), the associated Account Record was rejected because of the requirement for Referential Integrity. As set out in paragraph 4.19 above, the Time Stamp Code Logic Error resulted in Account Records being excluded from the ATMS data feed, rather than being rejected by the ATMS.

- 4.52. The main reason that Transaction Records were rejected by the ATMS was “ _Account Number not known to_ [the ATMS]” on the basis that, where the Account Record was not in the ATMS (as described in the previous paragraph), the associated Transaction Records were rejected because of the requirement for Referential Integrity. During the Relevant Period, the primary reason that _“Account Number [was] not known to_ [the ATMS] _”_ was because of the Time Stamp Code Logic Error.

- 4.53. In this way, if the Customer Record was not acquired into the ATMS, for whatever reason, then there could be no Account Record in the ATMS. With no Account Record in the ATMS, no transactions could be monitored on the account until the Customer Record, and following this the Account Record, were successfully acquired into the ATMS.

[p. 21] [ref: 4.54]

- 4.54. Furthermore, even if the Account Record was successfully accepted into the ATMS at some point in the future, there was no facility to "replay” the transactions that had been missed in the ATMS, as the ATMS did not have the functionality to process transaction data retrospectively (see paragraph 4.21). In this way, the ATMS could not remediate unmonitored transactions automatically and any transactions that had been made by the customer up to that point could not be monitored by the ATMS. However, the Authority acknowledges that Metro took steps to remediate certain transactions within the Bad Data folders through the Lookback Review.

## Bad Data folders


[p. 22] [ref: 4.55]

- 4.55. Records rejected by the ATMS (i.e. Bad Data) were put into Bad Data folders. Upon this occurrence, the ATMS would also generate a file which provided details of the reasons why the ATMS could not acquire the records, for example because a mandatory field was not present.

- 4.56. However, despite some members of staff being aware that large amounts of Bad Data, particularly in relation to Transaction Records, were being deposited into the Bad Data folders, Metro failed to put in place a process for dealing with the rejected Account and Transaction Records in the Bad Data folders, which were only intermittently reviewed as part of work by these individuals to understand the Bad Data issues. As regards the rejected Customer Records in the Bad Data folders, these were meant to be dealt with by Metro’s “exceptions process” however this was inadequate for the reasons set out below in paragraphs 4.57 to 4.73.

## The exceptions process for Bad Data


[pp. 22-23] [ref: 4.57]

- 4.57. There was an exceptions process within Metro which was meant to deal with Customer Records (as opposed to Account Records and Transaction Records) which had been rejected from the ATMS as Bad Data during the Relevant Period. The exceptions process was managed by Metro’s Business and Commercial Support Team (formerly the Account Servicing Team until Q4 2018).

- 4.58. Initially, IT Operations within Metro produced daily reports in the form of a spreadsheet, which set out details of the Customer Records that required remediation (in order to correct the issues that were causing them to be treated as Bad Data). The Business and Commercial Support Team was then responsible for remediating the Customer Records which were referred to in the daily reports, where they were able to do so (for example, by correcting data which was in the wrong format or inserting missing data). However, the Business and Commercial Support Team did not have the necessary permissions to remediate all types of Customer Records (see paragraphs 4.61 to 4.64) and, furthermore, there were occasions when the daily reports were not emailed to the Business and Commercial Support Team for processing, such that a backlog of remediation work built up between September 2016 and March 2017.

- 4.59. To address the issue of the daily reports not being emailed to the Business and Commercial Support Team in a timely manner, the process of generating the daily reports was automated by IT Operations in April 2017. From this time, the daily reports were automatically placed in a shared folder within Metro which the Business and Commercial Support Team could access. As before, the Business and Commercial Support Team was then responsible for remediating the Customer Records in the daily reports, however it remained the case that they were not able to do so where they did not have the necessary permissions.

- 4.60. Further, there was no escalation process in place if the Business and Commercial Support Team could not correct a Customer Record. In effect, this meant that there was no designated procedure for correcting certain types of Customer Records, such that those Customer Records and the associated Account and Transaction Records would continue to be rejected by the ATMS and would go unmonitored.

- 4.61. One type of Customer Record that the Business and Commercial Support Team was not able to correct was Partnership records. The Partnerships service from Metro offered a range of banking services for a variety of approved intermediaries including pension providers, Independent Financial Advisers, wealth managers and accountants.

[pp. 23-24] [ref: 4.62]

- 4.62. The Bad Data Report (see paragraphs 4.90 to 4.93), completed by April 2018, stated that 62% (2,772 of 4,448) of the Customer Records rejected from the ATMS were from the Partnerships area within Metro. The Bad Data Report also stated that there was a spike of Bad Data which, in all likelihood, was related to Partnerships in December 2017 when 74% of Bad Data related to customers was believed to have originated from that part of the business.

- 4.63. The Business and Commercial Support Team was not responsible for Partnerships Customer Records and they did not have access to those records in Metro’s core banking system, meaning that they were unable to view and amend them. As a result, as of May 2018, the Business and Commercial Support Team could only rectify approximately a third of the Customer Records that were detailed in the daily reports that were produced as part of the exceptions process.

- 4.64. In this way, at the time the Bad Data Report was written, no steps were being taken by Metro to review or rectify the necessary Partnerships Customer Records relevant for the ATMS as part of the exceptions process.

- 4.65. Where it was possible for the Business and Commercial Support Team to remediate Customer Records as envisaged under the exceptions process, this entailed updating the Customer Record in Metro’s core banking records system and contacting the relevant relationship manager for further information where necessary.

- 4.66. However, there was an absence of defined procedures in relation to how the Business and Commercial Support Team should go about correcting all types of Customer Records which, coupled with inadequate oversight of the exceptions process, meant that Metro had inadequate controls around ensuring that the remediation of the rejected Customer Records was undertaken properly and seen through to completion in an appropriate timeframe. The potential risk associated with the lack of defined process for remediating Customer Records was articulated by more junior Metro staff prior to the ATMS going live in March 2016 and yet it was still being referenced as an ongoing concern in the Bad Data Report which was finalised over two years later. In this way, the exceptions process was insufficiently defined and had inadequate oversight, despite more junior staff at Metro recognising this as a risk area.

- 4.67. If a Customer Record could be corrected, it was automatically fed into the ATMS the following day in the normal “business as usual” processes that picked up new and changed Customer Records. Once a Customer Record had been remediated in this way, in circumstances where the associated Account Record had been rejected by the ATMS because of Referential Integrity, it was possible for the ATMS to acquire the Account Record without the need for remediation of the Account Record itself (although this did not occur automatically).

[pp. 24-25] [ref: 4.68]

- 4.68. However, there was no process for ensuring that Account Records associated with rejected Customer Records were acquired into the ATMS, once the Customer Records had been corrected. The Authority acknowledges that Metro undertook some reconciliations in 2020 (see paragraphs 4.28 to 4.30), following which it remediated certain missing records and manually loaded these into the system.

- 4.69. Likewise, there was no process to deal with Transaction Records which were rejected by the ATMS and put into Bad Data folders, although the Lookback Review which took place in July 2019 following Metro’s identification of the Time Stamp Code Logic Error did involve the review of Transaction Records associated with the Account Records that were identified as missing from the ATMS as at 1 July 2019 (see paragraphs 4.33 to 4.45 above). Further, as referred to above, there was no facility to "replay” the transactions that had been missed in the ATMS as the ATMS did not have the

functionality to process transaction data retrospectively (see paragraphs 4.21 and 4.54).

- 4.70. Moreover, in terms of governance, no management information was generated in relation to the exceptions process and no periodic reporting on Bad Data to any individuals, teams or committees took place during the Relevant Period.

- 4.71. The Authority therefore considers that Metro failed to put in place adequate systems and controls for managing Bad Data and in relation to the exceptions process which meant that Customer, Account and Transaction Records that should have been routinely loaded into the ATMS were not being so loaded, either in a timely fashion or at all.

- 4.72. As a result, every time a Bad Data record was created for a new Customer Record, an Account Record or a Transaction Record, the ongoing monitoring ordinarily performed by the ATMS, which in turn would have generated alerts for Metro’s AML teams, was not performed for these records. Consequently, unusual or uncharacteristic transactional activity was not highlighted to the Metro AML teams who would ordinarily use this information to identify suspicious activity. As such, in respect of Bad Data, there was a risk of Metro missing suspicious activity and thereby inadvertently being used to further financial crime.

- 4.73. The Authority considers that an effective process for managing Bad Data so as to ensure that the associated records were subject to ongoing monitoring was a key part of Metro’s AML control framework and should have been in place since the inception of the ATMS in 2016. Further, in the absence of this, substantive remedial action should have taken place when the risks in relation to Bad Data and the exceptions process were being discussed within Metro throughout 2018 (see paragraphs 4.78 to 4.103).

Impact of Bad Data

[pp. 25-26] [ref: 4.74]

- 4.74. Of the total number of transactions not monitored by Metro in the period 6 June 2016 to 21 July 2019, at least 46,662,134 transactions (£31,637,046,957 in value) are attributable to the Time Stamp Code Logic Error, and Metro is not able to precisely attribute 13,807,299 (£19,686,082,418 in value) between the Time Stamp Code Logic Error and other Bad Data issues.

- 4.75. However, through work undertaken following the end of the Relevant Period, Metro determined that, for transactions intended for monitoring by the ATMS, at least 99.7%

of Transaction Records were consistently fed into the ATMS from 21 July 2019, the point Metro implemented the fix for the Time Stamp Code Logic Error (see paragraph 4.22). This indicates that the Time Stamp Code Logic Error is likely to have been the single material failure resulting in Bad Data Transaction Records during the Relevant Period. Following the application of the fix for the Time Stamp Code Logic Error, the number of rejected Transaction Records significantly decreased from 1,352,665 for July 2019 to 438 in August 2019.

- 4.76. During the entirety of the Relevant Period, the total number of transactions entered into the ATMS was at least 1,008,426,668, with at least 60,483,951 (circa 6.0%) being rejected due to the Time Stamp Code Logic Error or other issues with Bad Data. The total value of the transactions entered into the ATMS during this period was at least £675,818,015,000, with the total value of rejected transactions as a result of the failings described in this Notice being at least £51,250,294,000 (circa 7.6%). This equated to a high volume and high value of transactions that were not monitored, with Metro having insufficient understanding as to why, during the Relevant Period.

- 4.77. Further, the failure to put in place an effective reconciliation process between the DS and the ATMS until 17 December 2020 meant that, during the Relevant Period, Metro was not appropriately monitoring the quantity of rejected Transaction Records.


---

[previous part](text-002.md) | [source overview](overview.md) | [next part](text-004.md)

[^original]: Financial Conduct Authority, "FCA fines Metro Bank £16m for financial crime failings" (2024-11-11). https://www.fca.org.uk/news/press-releases/fca-fines-metro-bank-16m-financial-crime-failings
