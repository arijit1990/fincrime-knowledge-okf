---
type: Source Text
title: FFIEC Bank Secrecy Act/Anti-Money Laundering Examination Manual - part 32 of 32 (pp. 358-364)
description: 'Verbatim extracted text, pp. 358-364: Bank Secrecy Act/ Anti-Money Laundering Examination Manual > Appendix T: BSA E-Filing System'
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
part: 32
parts_total: 32
content_mode: full_text
generated:
  by: process:fincrime-kb-build
  at: '2026-11-22T04:42:14Z'
verified:
- by: process:kb-validate/verbatim-coverage
  at: '2026-11-22T04:42:14Z'
sources:
- id: original
  resource: https://bsaaml.ffiec.gov/manual
  title: FFIEC Bank Secrecy Act/Anti-Money Laundering Examination Manual
  author: org:ffiec
  last_modified: '2020-06-17T00:00:00Z'
---

# FFIEC Bank Secrecy Act/Anti-Money Laundering Examination Manual

[previous part](text-031.md) | [source overview](overview.md)

> Verbatim text extracted from the original (FFIEC, 2020-06-17), part 32 of 32, pp. 358-364. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **legal requirement**.[^original]

## Bank Secrecy Act/ Anti-Money Laundering Examination Manual


### Appendix T: BSA E-Filing System


[pp. 358-359]

The tracking statuses that indicate errors for filings are as follows:

- _Accepted with Warnings_ . This status only applies to batch filing. The submission has been accepted and will be processed by FinCEN. However it contains some errors that need to be corrected, once the submission has been acknowledged. The warnings may be reviewed through the Submission Warnings page. The filer can also optionally download the warnings by clicking on the Download as XML button to receive full detail of the warnings. The Submission Warnings page provides important details concerning the types of errors received and the location within the submitted file associated with the error. The column titled “Context” provides the location within the submitted file where the error was generated. This field will often list the record type, field description, line number, and document number (if applicable). The document number is equal to the transaction sequence number for each document within a batch submission. The first document within the batch will have transaction sequence number “00001” and will increment by one for each additional document.

- _Transmitted with Warnings_ . This status only applies to batch filing. When a submission that was previously “Accepted With Warnings” is transmitted to FinCEN, the status becomes “Transmitted with Warnings.” The user can click on the transmitted with warnings link to view the warnings that were issued for the submission; however, the bank must wait until they receive the “Acknowledgement” file from FinCEN in order to correct and resubmit their batch submission. The bank must wait for the Acknowledgement file because a BSA-ID is required for corrected submissions. The BSA-ID is not assigned until the file has been “Acknowledged.”

T–5

Appendix T: BSA E-Filing System

- _Rejected._ This status applies to both discrete and batch filing. Both types of submissions (discrete and batch) will receive a status of “Rejected” when an invalid report version is used or the role has not been assigned to the user. Batch submissions will also receive a “Rejected” status if the batch fails to meet the BSA Electronic Filing Requirements upon submission to the BSA E-Filing system. The “Rejected” link in the Track Status provides a listing of the file errors to be corrected. Users have the option of correcting the identified errors in a batch file due to data and/or format issues before resubmitting the file, or users can resubmit the same batch file (without correcting the identified errors) with the override option applied if the batch file has no “Fatal” errors. If the batch file has one or more “Fatal” errors, then the file must be corrected and the override option cannot be applied.

[pp. 359-362]

- _Acknowledge Failed._ This status only applies to batch filing. FinCEN was unable to load the batch filing. Therefore, an acknowledgement file could not be generated.

- _Hold._ This status applies to both discrete and batch filing. The filing was placed on Hold by the system administrator.

T–6

Appendix T: BSA E-Filing System

###### _Acknowledgement Notificaton_

When BSA E-Filing receives acknowledgements from FinCEN for filings, the filer will receive an e-mail containing a link to BSA E-Filing as well as the Secure Message ID that contains their acknowledgement. The user must access BSA E-Filing to view the acknowledgment content. The Secure Message subject field will include the filing tracking ID assigned to the filing upon submission in order to reconcile the acknowledgement with the submitted filings. The text box of the Secure Message will contain the Acknowledgement content for the discrete filing, as shown in the following graphic.

T–7

Appendix T: BSA E-Filing System

A batch filing acknowledgement will arrive as an attachment to a Secure Message as shown in the following graphic.

T–8

Appendix T: BSA E-Filing System

###### _Storing Acknowledgements for Your Records_

BSA E-Filing retains information for a limited time. For this reason, it is recommended that banks download and store acknowledgements for their permanent records. Discrete filing acknowledgements may be saved as a PDF file and batch filing acknowledgements may be saved as separate attachments.

BSA E-Filing Administrative Data Retention Policy:

|Administrative Data Type|Retention Time|
|---|---|
|Acknowledgement Data|30 days after being opened or 60 days after being posted, whichevercomes first|
|Alert Data|30 days afterposting|
|Track Status Data|As of July 1, 2011, 1825 days (i.e. 5 years) after achieving ‘Accepted’ or‘Rejected’ status. Note: The retention period prior to July 1, 2011 was 365days.|

###### _Error Categories_

###### Discrete Filing Errors

[pp. 362-363]

Discrete filing reports have been designed to prevent most errors. If a filer submitting a report leaves certain fields blank (such as those fields noted with an *), the discrete report will not transmit. These errors would be comparable to a batch filer’s primary errors. Similarly, secondary errors (such as invalid zip codes), will also prevent the report from transmitting. If a filer attempts to validate a report that contains errors, the filer will get a message saying, “There are validation errors.” A separate window containing up to seven (7) errors will appear. If more than seven (7) errors are detected, the window will record the number of additional errors in the report and note through a statement such as “Message limit exceeded. Remaining X errors not reported.” The system will not allow submission until these remaining errors are remedied.

A discrete report is validated for errors upon submission. Once accepted and acknowledged by the system, only the BSA ID assigned for the filing is returned to the filer. No additional errors are sent back along with acknowledgement message for discrete filing.

###### Batch Filing Errors

There are two types of errors identified in batch files: format errors that may result in automatic rejection of a batch file and file errors that represent errors in data entered in individual fields. Fatal format errors prevent the batch file from being processed. For example, error F18 “A required 9Z record is missing from the submitted file” is a fatal format error because each batch file must contain a 9Z record. Error C404, for a CTR filing, “Person street address is blank” is a file error because it indicates data is missing from a street address field. For a SAR filing, error S224 “Financial institution type is blank” is a file error because it indicates data is missing from a record. A batch file with large numbers of file errors can be rejected by the BSA E-Filing Program if the number of errors exceeds programming limits.

T–9

Appendix T: BSA E-Filing System

File errors are classified as primary or secondary errors, depending on their importance. Primary errors are file errors that violate electronic filing requirements or report instructions and so degrade data quality that they must be corrected. Primary errors make it difficult for regulators, analysts, and law enforcement investigators to locate the reports in the database or identify the nature and circumstances of the filing. Examples of such errors include blank last names or legal names, missing financial institution Employer Identification Numbers, or invalid entries in the transaction date field. Attachment A – Error Code List identifies primary errors by adding an asterisk (*) to the four digit error code.

[pp. 363-364]

Secondary errors are file errors that violate electronic filing requirements or report instructions but have a lesser impact on data quality. Examples of secondary errors are ZIP Codes that end in four zeroes (e.g. 123450000), blank or invalid financial institution address information, or invalid telephone numbers.

###### _Error Correction_

A detailed description of error codes can be found in Attachment A - Error Code List in the FinCEN Currency Transaction Report Electronic Filing Requirements and the FinCEN Suspicious Activity Report Electronic Filing Requirements.

Attachment B – Error Correction Instructions are also contained in the Electronic Filing Requirements documents and identify the requirements and procedures for correcting FinCEN errors reported to batch filers during the FinCEN acknowledgement process.

There are also batch file specifications for the FinCEN DOEP and the FinCEN FBAR in the Electronic Filing Requirements documents for those types of submissions.

###### _Correction Requirements_

Filers should immediately correct and resubmit a batch file rejected for fatal errors or for large numbers of file errors when notified by FinCEN the batch file was not accepted. Rejection of a batch file does not relieve the filer of the responsibility to file within the required time frames established by the BSA regulations.

An accepted batch file containing primary errors, must be re-filed as corrected reports with the primary errors and any secondary errors corrected. FinCEN reports that contain only secondary errors need not be corrected.

###### _Naming Conventions_

The “Filing Name” fields on the BSA E-Filing Header page are for the bank to use as an internal filing in such a manner as to distinguish it from other filings submitted. As such, each file name should be unique. This will be especially useful when using the Track Status feature in BSA E-Filing. Naming conventions optimize the bank’s ability to distinguish files from one another, but not to disclose sensitive information contained on the BSA reports. Having a standard naming convention will be even more important if the organization has multiple people responsible for filing. Each filer will want to distinguish their filings from ones submitted by other filers within the organization. Conventions may include a filer’s abbreviated name or initials, date of submission, and a sequence number of filings in one day

T–10

Appendix T: BSA E-Filing System

(to the extent that multiple filings are submitted in one day). So, for example the third filing prepared by John Smith on April 1st, 2014 might be named JoeSmithCTR04012014-3.

Once a naming convention has been developed, banks should ensure appropriate personnel are trained accordingly.

###### _Work-In-Progress Reports_

The Work-in-Progress (WIP) system collects and stores data from FinCEN’s BSA E-Filing System and develops trending information and reports on BSA electronic filing patterns. Key functionality of the WIP system includes:

[p. 364]

- Identifying, capturing and storing data on errors found in e-filed BSA documents;

- Providing statistical outputs of trend metrics, such as filing patterns and behavior, data quality issues, and filing errors; and

- Reporting feedback to BSA filers about their overall E-Filing data quality.

Every month, the Supervisory User will receive two filer feedback reports from the BSA E- Filing Secure Messenger. These reports are intended to show trending errors for a given form type and identify systemic problems the filer may be experiencing. The two reports are identified below:

- Potential Data Quality Issues by Form Type. This report provides a monthly ranking and frequency of filing errors by form type; and

- Filing Statistics by Form Type. This report provides filing counts by form type over a calendar year.

T–11


---

[previous part](text-031.md) | [source overview](overview.md)

[^original]: FFIEC, "FFIEC Bank Secrecy Act/Anti-Money Laundering Examination Manual" (2020-06-17). https://bsaaml.ffiec.gov/manual
