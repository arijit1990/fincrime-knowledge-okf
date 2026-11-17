---
type: Source Text
title: FCA fines Metro Bank £16m for financial crime failings - part 5 of 6 (pp. 34-41)
description: 'Verbatim extracted text, pp. 34-41: External Compliance Firms; Internal transactions at Metro and the ATMS; Remediation by Metro; and 4 more sections'
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
part: 5
parts_total: 6
content_mode: full_text
generated:
  by: process:fincrime-kb-build
  at: '2026-11-17T12:21:45Z'
verified:
- by: process:kb-validate/verbatim-coverage
  at: '2026-11-17T12:21:45Z'
sources:
- id: original
  resource: https://www.fca.org.uk/news/press-releases/fca-fines-metro-bank-16m-financial-crime-failings
  title: FCA fines Metro Bank £16m for financial crime failings
  author: org:fca
  last_modified: '2025-12-05T00:00:00Z'
---

# FCA fines Metro Bank £16m for financial crime failings

[previous part](text-004.md) | [source overview](overview.md) | [next part](text-006.md)

> Verbatim text extracted from the original (Financial Conduct Authority, 2024-11-11), part 5 of 6, pp. 34-41. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **supervisory expectation**.[^original]

## External Compliance Firms


[pp. 34-35] [ref: 4.104]

- 4.104. Compliance Firm 1 was engaged by Metro in December 2018 to undertake a review of the Bank’s financial crime technology to understand whether it was aligned with standard industry practice. Following its review, Compliance Firm 1 produced a report dated March 2019 (“Compliance Report 1”).

- 4.105. Compliance Report 1 identified that although the primary financial crime controls were in place within Metro, their configuration was not aligned with standard industry practice. Compliance Report 1 acknowledged that this was likely to mean that current controls were insufficient to mitigate Metro’s key financial crime risks and to meet some regulatory obligations. With specific reference to transaction monitoring, Compliance Report 1 stated that this may overlook customer behaviour which was indicative of money laundering or terrorist financing.

- 4.106. Compliance Report 1 raised the issue of Partnerships data within Metro (see paragraphs 4.61 to 4.64), observing that circa 20% of Transaction Records, primarily in relation to Partnerships data, were being rejected by the ATMS. Compliance Report 1 went on to state that it was important for Metro to have a mechanism in place to review rejected records and ensure these were corrected.

- 4.107. Compliance Report 1 also stated that there did not appear to have been a review of the data feed into the ATMS to confirm that all Customer Records, Account Records and Transaction Records were complete and accurately captured by the ATMS. Compliance Report 1 further stated that, without undertaking this step, it was not possible to have confidence that financial crime risk was being appropriately managed within Metro. This issue was characterised as a Medium Priority Finding (on a scale of Low, Medium, High, Very High Priority Findings), which meant that “ _Action_ [was] _required to strengthen these controls”_ .

- 4.108. In response to Compliance Report 1, Metro established the Financial Crime Technology (ATMS) Steering Committee (the “Technology Steering Committee”) in April 2019. The Technology Steering Committee, amongst other areas, was responsible for overseeing improvements to Metro’s transaction monitoring systems and controls. The Technology Steering Committee also had oversight of the remediation of the Time Code Stamp Logic Error.

- 4.109. Compliance Firm 2 was engaged by Metro to review the end-to-end architecture of the AML / transaction monitoring features of the ATMS. The review took place between December 2019 and January 2020. Compliance Firm 2 then produced a report (“Compliance Report 2”) detailing their findings.

[pp. 35-36] [ref: 4.110]

- 4.110. Compliance Report 2 also raised the issue of Partnerships data within Metro and the exceptions process (see paragraphs 4.57 to 4.73). In particular, Compliance Report 2 noted that there was no escalation process in place for the Business and Commercial Support team to follow in circumstances where it had been unable to remediate rejected Customer Records. In addition, it was noted that the team was unable to effect changes to Partnership Customer Records, that there was no Service Level Agreement in place for re-processing exceptions (i.e. agreed timeframes in place for amending rejected Customer Records via the exceptions process) and, further, that there was no process in place at all to manage Account Records or Transaction Records that had been rejected from the ATMS.

- 4.111. Compliance Report 2 also addressed the issue of internal transactions, which did not need to be monitored (see paragraphs 4.113 to 4.116). In this regard, internal accounts were excluded from the Account Records that were sent to the ATMS, however their associated Transaction Records (such as double entries for the general ledger) were not excluded. This meant that these Transaction Records were rejected as Bad Data by the ATMS, due to Referential Integrity. This specific issue caused the generation of

thousands of Bad Data records each day which, in turn, meant that there was a lack of clear visibility of the true volume of customer transactions being rejected by the ATMS and made the identification of “true” exceptions (i.e. where genuine data quality issues had occurred and needed to be remediated) more difficult to identify, such that Metro was unable to quantify the corresponding AML risk.

- 4.112. In this way, both Compliance Firm 1 and Compliance Firm 2 identified risks in relation to (amongst other things) managing Bad Data, the inability of the Business and Commercial Support Team to remediate Partnerships data and the exceptions process, which broadly reflect the Authority’s concerns that are summarised at paragraphs 4.57 to 4.73 above. Some of these risks had also been identified in the Reports prepared in 2018 yet Metro did not take steps to address these risk areas until Compliance Firm 1 and Compliance Firm 2 had submitted their reports, in March 2019 and January 2020 respectively.

## Internal transactions at Metro and the ATMS


[pp. 36-37] [ref: 4.113]

- 4.113. As mentioned above, internal Metro transactions did not require monitoring in the same way as external transactions, as these transactions were executed within Metro itself. Despite this, internal transactions were included in the data feed from the DS into the ATMS. These internal transactions were rejected as Bad Data on the grounds of Referential Integrity as there was no corresponding Account Record in the ATMS (see also paragraph 4.111).

- 4.114. On 14 December 2020, Metro implemented a fix to remove internal transactions from the data feed from the DS into the ATMS. This enabled the Bank to have clear visibility of the true volume of customer transactions being rejected by the ATMS on an ongoing basis for the first time since the ATMS went live in June 2016.

- 4.115. This fix took Metro four and half years to implement, and during this time the ongoing picture of the volume of customer transactions rejected by the ATMS was obscured by the internal transactions which did not need to be monitored in the first place. The Authority acknowledges that Metro approximately quantified the number of internal transactions in the Bad Data folders during the Lookback Review as at a singular point in time prior to December 2019.

- 4.116. In combination with the lack of an effective reconciliation process to confirm that all data from the DS was being loaded into the ATMS, the inclusion of internal transactions

in the data feed from the DS to the ATMS meant that Metro was unable to properly quantify the extent to which its customer transactions were subject to ongoing monitoring (or otherwise) and, therefore, the level of AML risk in relation to unmonitored transactions during the Relevant Period.

## Remediation by Metro


[p. 37] [ref: 4.117]

- 4.117. Metro has taken recommendations from both Compliance Report 1 and Compliance Report 2 and implemented these, either in whole or in part, in an overarching Financial Crime Improvement Programme (“FCIP”). Further, Metro has advised the Authority that remediation activity to address the issues identified in Compliance Report 2 has been included within the scope of either the Bank’s FCIP or the programme of work overseen by the Bank’s Executive Data Governance Working Group.

- 4.118. In particular, with reference to the issues identified in this Notice, Metro has made:

- 4.118.1. significant enhancements to the Bank’s end-to-end architecture and data controls to ensure that the data that is fed into the ATMS is complete and accurate: Metro has achieved a reconciliation rate of Transaction Records fed into the ATMS of at least 99.7% by volume since 22 July 2019;

- 4.118.2. material improvements to the controls for the oversight of Bad Data; and

- 4.118.3. a significant investment in additional resource and capability to manage the Bank’s ATMS, to review and assess the quality and effectiveness of the ATMS and to review and investigate possible suspicious activity.

## 5. FAILINGS


[pp. 37-39] [ref: 5.1]

- 5.1. The regulatory provisions relevant to this Notice are referred to in Annex A.

- 5.2. Principle 3 required Metro to take reasonable care to organise and control its affairs responsibly and effectively, with adequate risk management systems.

- 5.3. SYSC 6.1.1R required Metro to establish, implement and maintain adequate policies and procedures sufficient to ensure Metro’s compliance with its obligations under the regulatory system and for countering the risk that it might be used to further financial crime.

- 5.4. SYSC 6.3.1R required Metro to ensure that those policies and procedures included systems and controls that (1) enabled it to identify, assess, monitor and manage money laundering risk, and (2) were comprehensive and proportionate to the nature, scale and complexity of its activities.

- 5.5. SYSC 6.3.3R required Metro to carry out a regular assessment of the adequacy of those systems and controls to ensure that they remained compliant.

- 5.6. During the Relevant Period, Metro failed to meet these requirements and, in doing so, breached Principle 3. In particular:

- 5.6.1. From the implementation of the ATMS on 6 June 2016, Metro failed to take any steps to check the completeness of data feeding into the ATMS, prior to identifying the Time Stamp Code Logic Error on 17 April 2019. Throughout the Relevant Period, Metro did not have controls in place to check, on an ongoing basis, that transactions that should have been monitored by the ATMS were being received by the ATMS and this contributed to the situation whereby the Time Stamp Code Logic Error continued for nearly three years before it was identified.

- 5.6.2. There was no adequate process in place to deal with Bad Data rejected from the ATMS: Metro did not take sufficient steps to ensure that the exceptions process for dealing with rejected Customer Records was adequate and there were no processes in place to deal with rejected Account Records and Transaction Records.

- 5.6.3. Bad Data was recognised as a risk and a serious issue at comparatively less senior grades within Metro and individual staff members investigated and attempted to escalate this to more senior staff and Committees in 2017 and 2018. However, reference to Bad Data was removed from the Financial Crime Steering Group’s January 2018 minutes, on the basis that the Bad Data issue did not appear to be substantiated, which meant there was no action to track and monitor this risk. Despite the issue not having been resolved, the Financial Crime Steering Group did not discuss Bad Data again until after the Time Stamp Code Logic Error had been identified in April 2019. Likewise, the Working Group and the Operations Risk Board escalated Bad

Data to senior staff within Metro in 2018, but no substantive action took place.

[p. 39] [ref: 5.6.4]

- 5.6.4. During the Relevant Period, Metro did not have a sufficient understanding of the level of AML risk associated with unmonitored transactions. This was, in part, due to the fact that the true picture of the volume of transactions rejected by the ATMS (and which therefore went unmonitored) was obscured by the presence of internal transactions which did not need to be monitored. This issue took Metro over four years to resolve and it was only on 14 December 2020, shortly before the end of the Relevant Period, that Metro implemented a fix to remove internal transactions from the data feed into the ATMS.

- 5.7. These transaction monitoring failings resulted in over 60 million transactions with a value of over £51 billion not being monitored during the Relevant Period. Whilst m any of these transactions were subsequently reviewed as part of a remediation exercise, there was a lengthy delay in the identification of suspicious activity and this increased the risk of Metro inadvertently being used for the purposes of financial crime.

## Financial penalty


[ref: 6.1]

- 6.1. The Authority’s policy for imposing a financial penalty is set out in Chapter 6 of the Decision Procedure and Penalties manual (“DEPP”). In respect of conduct occurring on or after 6 March 2010, the Authority applies a five-step framework to determine the appropriate level of financial penalty. DEPP 6.5A sets out the details of the five-step framework that applies in respect of financial penalties imposed on firms.

- 6.2. Pursuant to DEPP 6.5A.1G, at Step 1 the Authority seeks to deprive a firm of the financial benefit derived directly from the breach where it is practicable to quantify this.

## Step 1: disgorgement


[pp. 39-40] [ref: 6.3]

- 6.3. The Authority has not identified any financial benefit that Metro derived directly from its breach.

- 6.4. Step 1 is therefore £0.

- 6.5. Pursuant to DEPP 6.5A.2G, at Step 2 the Authority determines a figure that reflects the seriousness of the breach. Where the amount of revenue generated by a firm from a particular product line or business area is indicative of the harm or potential harm that its breach may cause, that figure will be based on a percentage of the firm’s revenue from the relevant products or business area.

## Step 2: the seriousness of the breach


[pp. 40-41] [ref: 6.6]

- 6.6. The Authority considers that the revenue generated by Metro is indicative of the harm or potential harm caused by its breach. The Authority has therefore determined a figure based on a percentage of Metro’s relevant revenue. Metro’s relevant revenue is the total revenue derived by Metro from its customers during the period of the breach. The period of Metro’s breach was from 6 June 2016 to 17 December 2020 inclusive. The Authority considers Metro’s relevant revenue for this period to be £2,117,492,472.

- 6.7. In deciding on the percentage of the relevant revenue that forms the basis of the Step 2 figure, the Authority considers the seriousness of the breach and chooses a percentage between 0% and 20%. This range is divided into five fixed levels which represent, on a sliding scale, the seriousness of the breach; the more serious the breach, the higher the level. For penalties imposed on firms there are the following five levels:

Level 1 – 0% Level 2 – 5% Level 3 – 10% Level 4 – 15% Level 5 – 20%

- 6.8. In assessing the seriousness level, the Authority takes into account various factors which reflect the impact and nature of the breach, and whether it was committed deliberately or recklessly. DEPP 6.5A.2G(11) lists factors likely to be considered ‘level 4 or 5 factors’. Of these, the Authority considers the following factors to be relevant:

- 6.8.1. The breach revealed serious or systematic weaknesses in the firm’s procedures or in the management systems or internal controls relating to all or part of the firm’s business; and

- 6.8.2. The breach created a significant risk that financial crime would be facilitated,

occasioned or otherwise occur.

- 6.9. DEPP 6.5A.2G(12) lists factors likely to be considered ‘level 1, 2 or 3 factors’. Of these, the Authority considers the following factors to be relevant:

- 6.9.1. There was no or little loss or risk of loss to consumers, investors or other market users individually and in general.

- 6.10. Taking all of these factors into account, the Authority considers the seriousness of the breach to be level 4 and so the Step 2 figure is 15% of £2,117,492,472.

- 6.11. Step 2 is therefore £317,623,870.

[p. 41] [ref: 6.12]

- 6.12. Pursuant to DEPP 6.5.3G(3), the Authority may decrease the level of penalty arrived at after applying Step 2 of the framework if it considers that the penalty is disproportionately high for the breaches concerned. Notwithstanding the serious and long-running nature of the breaches, the Authority considers that the level of penalty would nonetheless be disproportionate if it were not reduced and should be adjusted.

- 6.13. In order to achieve a figure that (at Step 2) is proportionate to the breach, and having taken into account previous cases, the Step 2 figure is reduced to £23,821,790.


---

[previous part](text-004.md) | [source overview](overview.md) | [next part](text-006.md)

[^original]: Financial Conduct Authority, "FCA fines Metro Bank £16m for financial crime failings" (2024-11-11). https://www.fca.org.uk/news/press-releases/fca-fines-metro-bank-16m-financial-crime-failings
