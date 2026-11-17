---
type: Source Text
title: FCA fines HSBC Bank plc £63.9 million for deficient transaction monitoring controls - part 6 of 8 (pp. 36-42)
description: 'Verbatim extracted text, pp. 36-42: _List of correspondent banking relationships_; _Transaction mapping_; _Data quality assessment_; and 2 more sections'
resource: https://www.fca.org.uk/news/press-releases/fca-fines-hsbc-bank-plc-deficient-transaction-monitoring-controls
tags:
- effectiveness
- enforcement
- enforcement_notice
- rules_scenarios
- supervisory_expectation
- uk
status: stable
source_id: fca-fca-fines-hsbc-bank-plc-63-9-million-for-deficient-transaction-mon
issuer: fca
issuer_name: Financial Conduct Authority
jurisdictions:
- UK
tier: 1
instrument_type: enforcement_notice
normative_force: supervisory_expectation
publication_date: '2021-12-16'
legal_status: current
part: 6
parts_total: 8
content_mode: full_text
generated:
  by: process:fincrime-kb-build
  at: '2026-11-17T12:21:45Z'
verified:
- by: process:kb-validate/verbatim-coverage
  at: '2026-11-17T12:21:45Z'
sources:
- id: original
  resource: https://www.fca.org.uk/news/press-releases/fca-fines-hsbc-bank-plc-deficient-transaction-monitoring-controls
  title: FCA fines HSBC Bank plc £63.9 million for deficient transaction monitoring controls
  author: org:fca
  last_modified: '2022-05-06T00:00:00Z'
---

# FCA fines HSBC Bank plc £63.9 million for deficient transaction monitoring controls

[previous part](text-005.md) | [source overview](overview.md) | [next part](text-007.md)

> Verbatim text extracted from the original (Financial Conduct Authority, 2021-12-16), part 6 of 8, pp. 36-42. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **supervisory expectation**.[^original]

## _List of correspondent banking relationships_


[p. 36] [ref: 4.109]

- 4.109. As set out at paragraph 4.92 above, it had been identified in 2014 that HSBC did not maintain a list of correspondent banking relationships. This issue had still not been resolved when ETMS went live in 2017 and persisted during the relevant period. As an interim measure, when ETMS was implemented, HSBC put in place coding that was designed to identify entities that were exhibiting “ _correspondentlike_ ” banking behaviours and ETMS was monitoring around 96% to 97% of correspondent banking customer activity when it went live.

- 4.110. This was subsequently highlighted as a high-risk issue with 13 out of a sample of 30 GBM relationships incorrectly excluded for correspondent banking. It was subsequently clarified that 4 of these customers were not identified using the same interim measure and were highly likely to be conducting correspondent customer banking activity. HSBC subsequently developed an automated capability to identify its correspondent banking customers.

## _Transaction mapping_


[pp. 36-37] [ref: 4.111]

- 4.111. The accurate mapping of transaction types from source systems to transaction monitoring systems is a process to ensure the full suite of scenarios are applied to different products being monitored. Transactions therefore need to be mapped correctly from source systems to transaction monitoring systems to ensure that they are monitored effectively by the correct scenarios.

- 4.112. Transaction mapping had been an issue for HSBC at a UK and global level prior to 2016. These issues persisted after 2016 and included the following:

- (1) Between August 2016 and March 2018, approximately 24m cash transactions with a total value of approximately £24.5bn were not monitored by 2 of the 15 GMSAS scenarios and a UDR. This was because the cash amount was not populated in the necessary transaction field when it was fed into CAMP. This was not fully resolved during the relevant period. Notwithstanding this issue, HSBC later carried out a risk assessment and concluded the impact on the UDR to be of limited financial crime risk; and

- (2) 52 out of 540 transaction codes from 3 source systems that fed into CAMP were incorrect. This included 29 transaction codes involving, in the period of a year, over 17.6m transactions with a value of over £64bn which were categorised as EFT/Wire transactions when they should have been classified as cheques and monetary instruments. This led to a risk that these transactions were inadequately monitored by two GMSAS scenarios.

- 4.113. HSBC had not assessed the financial crime risk posed by transactions not being monitored by the full suite of scenarios during the relevant period. HSBC

subsequently implemented new controls that aimed to ensure a consistent mappings process with a new exceptions management reporting process.

_Data quality issues_

- 4.114. Certain data elements within CAMP, including country codes, counterparty identifier and financial transaction originator/beneficiary identifier, were of poor quality and had been so for a prolonged period of time. This led to a risk that CAMP would not generate alerts when it should. This failure was a risk with a critical impact putting HSBC in a state of regulatory non-compliance. HSBC’s policies and procedures around data quality were therefore not appropriate or sufficiently risk-sensitive throughout the relevant period.

Data accuracy post 2016 – (Correspondent Banking) ETMS

- 4.115. HSBC also identified transaction mapping issues in ETMS. 24 transaction codes with a total value of £239.6bn were incorrectly mapped into ETMS. These included:

- (1) 4 transaction codes for over 475,000 transactions with a value of over £1.2bn were categorised as wire transactions when these should have been categorised as cash transactions;

[p. 37] [ref: 4.116]

- (2) 18 transaction codes for over 530,000 transactions with a value of over £238bn were categorised as wire transactions when these should have been categorised as cheques and monetary instruments.

- 4.116. This led to a risk that these transactions would be under-monitored at a correspondent banking level by 1 of the ETMS scenarios, which had parameters specific to the different transaction type codes. These transaction mapping issues in ETMS were not resolved during the relevant period and the impact of the associated financial crime risk on transaction monitoring had not been assessed.

- 4.117. HSBC did not undertake a formal data quality assessment for ETMS during the relevant period and so had not addressed the data issues identified from the limited assessment that was carried out prior to its implementation. HSBC continued to identify data quality issues after the implementation of ETMS. These data quality issues impacted the effectiveness of ETMS. This was a very high-risk issue which may indicate a critical level of regulatory impact. This contributed to ETMS as having significant limitations during the relevant period.

## _Data quality assessment_


[pp. 37-38] [ref: 4.118]

- 4.118. The data quality issues that needed to be addressed meant HSBC had to delay the threshold tuning and testing of transactions that did not generate alerts. This in turn meant HSBC was not able to understand whether the ETMS thresholds were

set in such a way that it could identify transactions that were indicative of money laundering.

- 4.119. The failings set out above meant that HSBC still did not have an adequately effective automated transaction monitoring system throughout the relevant period. However, the Authority recognises HSBC’s commitment to its large-scale global remediation programme. In particular, the Authority acknowledges the following successful enhancements.

## Remediation action


[pp. 38-39] [ref: 5.1]

- (1) The introduction of an Extract, Transform and Load system which sat between source systems and CAMP, allowing HSBC to conduct data integrity checks and complete data mapping before the data was fed into CAMP and the equivalent system (COPS) for ETMS; and

- (2) A new methodology for the segmentation of customers based on lines of business, customer type, historic transactional activity and risk rating.

5. FAILINGS

- 5.1. The statutory and regulatory provisions relevant to this Notice are set out in Annex A.

- 5.2. On the basis of the facts and matters set out above, the Authority considers that HSBC failed to comply with ML Regulation 20(1)(a), by failing to establish and maintain appropriate and sufficiently risk-sensitive policies and procedures relating to ongoing monitoring which provided for the identification and scrutiny of:

- (1) complex or unusually large transactions;

- (2) unusual patterns of transactions which have no apparent economic or visible lawful purpose; and

- (3) any other activity which it regarded as particularly likely to be related to money laundering or terrorist financing.

- 5.3. HSBC failed to ensure that its processes and procedures around automated transaction monitoring systems were appropriate and sufficiently risk-sensitive throughout the relevant period. In particular:

- (1) From 2002 until 2016, HSBC’s processes for automated transaction monitoring used the same 6 scenarios which failed to provide appropriate monitoring coverage for the nature, scale and complexity of HSBC’s business. They also did not provide appropriate coverage of the risks presented by its correspondent banking business.

- (2) When 15 new scenarios were rolled out for CAMP in 2016, the scenarios were not tailored to specific UK risks and 124 UK high-risk gaps across certain money laundering and terrorist financing risk indicators were not covered. Efforts to improve coverage of specific UK risks through implementation of UDRs were unsuccessful. This meant that the policies and procedures around this were not appropriate for the risks presented by the business.

- (3) Thresholds used prior to 2016 had too many settings to allow testing to determine whether they were appropriate; they were also found to be ineffective in the 2014 external report.

- (4) From August 2016 until the end of the relevant period, the thresholds for CAMP were potentially not capturing all suspicious activity that needed to be identified.

[pp. 39-40] [ref: 5.4]

- (5) Extreme thresholds for certain scenarios that were introduced after 2016, in both CAMP and ETMS, were set in such a way that it was almost impossible for those scenarios to detect unusual activity; for example, in a CAMP scenario 52% of RBWM customers (5.4m customers) and over 570,000 CMB customers needed a 500,000% (or 5,000 times) increase in their monthly transactional activity to trigger an alert. This meant that the processes were not sufficiently risk-sensitive.

- (6) The suppression rules at one point in 2011 inadvertently suppressed all alerts in Wales with 1,780 SARs having to be retrospectively filed as a result. These rules also suppressed alerts that were indicative of unusual and sometimes suspicious activity, as demonstrated by the cases of Customer A, Customer C, Customer D and the 68 SARs for the period 2008 to 2016 that were subsequently filed after a lookback exercise in 2017. The use of these rules as part of HSBC’s automatic transaction monitoring were therefore not appropriate or sufficiently risk-sensitive.

- (7) HSBC delayed the implementation of its decision to remove the suppression rules for all high-risk accounts and those associated with high-risk countries for a year and a half which meant it delayed ensuring that its policies and procedures were appropriate and sufficiently risk-sensitive for identifying potentially high-risk transactions.

- (8) Inaccurate and incomplete data was fed into the CAMP system prior to 2016, often affecting millions of transactions which in turn impacted the effectiveness of the processes for transaction monitoring.

- (9) After 2016, HSBC continued to encounter data completeness and accuracy issues in CAMP and ETMS. These prevented the systems from effectively monitoring transactions and meant that HSBC’s processes and procedures were neither appropriate nor sufficiently risk-sensitive during the relevant period.

- 5.4. The Authority also considers that HSBC failed to comply with ML Regulation 20(1)(f), by failing to establish and maintain appropriate and sufficiently risksensitive policies and procedures for the monitoring and management of compliance with, and internal communication of policies and procedures for ongoing monitoring.

- 5.5. Policies that were put in place to do this included the CAMP maintenance guide and a service level agreement to ensure that alerts were reviewed within a specific timeframe. However, HSBC failed to establish and maintain these compliance procedures in the following ways:

- (1) The processes set out in the CAMP maintenance guide required that scenarios be reviewed annually, and that HSBC should not just rely on the scenarios that were already being used, but this was not followed. It was not until 2014 that HSBC considered that it needed new scenarios to monitor certain money laundering and terrorist financing typologies that presented a financial crime risk and even then, these scenarios were only identified at a global level.

[pp. 40-41]

- (2) When new scenarios were rolled out for CAMP in 2016 and when ETMS was introduced in 2017, HSBC did not implement policies and procedures to ensure that it could carry out adequate or timely risk assessments for these scenarios. This failure meant that HSBC had limited assurance that these systems were covering sufficient money laundering and terrorist financing risks in the UK to minimise the risk of financial crime.

- (3) Between 2016 and March 2018, nearly 35% of alerts generated by the LRT scenario in CAMP took more than 90 days to review, as prescribed by HSBC’s own policy for ensuring compliance with processes. The structuring scenario design issue also contributed towards the backlog of alerts. This, in turn, contributed towards the delay of the swift identification of unusual activity, increasing the risk that money laundering and terrorist financing went either completely undetected or were not detected for a significant period of time.

- (4) Prior to 2016, HSBC did not have appropriate and risk-sensitive procedures to ensure that it followed the CAMP maintenance guide’s requirement that account and customer thresholds be reviewed annually. This was demonstrated by thresholds being seldom updated and HSBC having no defined processes or documentation for tuning thresholds.

- (5) HSBC set the post 2016 CAMP thresholds in just a week; consequently, there was little opportunity to examine their effectiveness and ensure that they were appropriate and sufficiently risk-sensitive. Such thresholds were not tuned to ensure they were appropriate and sufficiently risk-sensitive throughout the relevant period. This contributed to HSBC not reviewing a significant number of its alerts within the 90-day period specified in its policies.

- (6) HSBC failed to carry out any testing of the alerts that were generated, and transactions that did not generate an alert, during the relevant period. This meant that HSBC could not be sure that alerts being generated were indeed indicative of unusual activity and were adequately identifying unusual activity; this contributed to these systems having significant limitations throughout the relevant period.

- (7) HSBC set the ETMS thresholds in a manner focused only on projected alert volumes in each customer segment and without documentation, so these were not demonstrably appropriate or risk-sensitive.

- (8) HSBC did not have appropriate policies and procedures in place to ensure that its staff adequately followed the CAMP maintenance guide’s requirement that suppression rules be reviewed annually. In some cases, the rules needed to be reverse engineered in order for HSBC to understand how the rules operated. HSBC also failed to consider whether there were wider issues with the suppression rules and whether these policies and procedures were appropriate after one rule was found to be suppressing all alerts in Wales.

[p. 41]

- (9) HSBC failed to check the completeness and accuracy of data that was being fed into CAMP and ETMS throughout the relevant period despite being recommended to do so by a number of external advisory parties over a prolonged period of time. This meant that HSBC did not have appropriate or sufficiently risk-sensitive policies and procedures in this regard during the relevant period. HSBC also failed to carry out a data quality assessment for ETMS.

- (10) HSBC failed to maintain a list of correspondent banking relationships which meant that not all relevant data for correspondent banking was being fed into the transaction monitoring systems. This was an example of policies and procedures to ensure compliance with internal policies and procedures not being appropriate or sufficiently risk-sensitive. As a result, HSBC failed to adequately monitor all of its respondent banks’ activity.

## 6. SANCTION


[pp. 41-42] [ref: 6.1]

- 6.1. Pursuant to Regulations 36(a) and 42(1) of the ML Regulations, the Authority may impose a penalty of such amount as it considers appropriate on a relevant person who fails to comply with the ML Regulations at issue in this notice.

- 6.2. HSBC is a relevant person pursuant to Regulations 3(2) and 3(3) of the ML Regulations.

- 6.3. In deciding whether HSBC has failed to comply with the relevant requirements of the ML Regulations, the Authority has considered whether HSBC followed the

relevant JMLSG Guidance as the JMLSG meets the requirements set out in Regulation 42(3) of the ML Regulations (being guidance approved by the Treasury).

- 6.4. In accordance with Regulation 42(2) of the ML Regulations, the Authority has considered whether it can be satisfied that HSBC took all reasonable steps and exercised all due diligence to ensure that the requirements of the ML Regulations would be complied with. The Authority has concluded that it cannot, for the reasons set out in Section 5 of this Notice.

- 6.5. Regulation 42(1) of the ML Regulations states that the Authority may impose a penalty of such amount that it considers appropriate on a relevant person for failure to comply with the ML Regulations at issue in this Notice.

- 6.6. The Authority has concluded that a financial penalty is the appropriate sanction in the circumstances of this particular case.

- 6.7. During the relevant period, paragraph 19.15.5 of the Enforcement Guide stated that, when imposing or determining the level of a financial penalty under the ML Regulations, the Authority's policy includes having regard, where relevant, to relevant factors in DEPP 6.2.1G and DEPP 6.5 to DEPP 6.5D.

- 6.8. DEPP 6.5A sets out the details of the 5-step framework that applies in respect of the financial penalties imposed on firms.

- 6.9. The application of the Authority’s penalty policy is set out below in relation to HSBC’s breaches of the ML Regulations relating to:

- (1) HSBC’s RBWM and CMB business (paragraphs 6.10 to 6.34); and

- (2) HSBC’s Correspondent Banking business (paragraphs 6.35 to 6.59).


---

[previous part](text-005.md) | [source overview](overview.md) | [next part](text-007.md)

[^original]: Financial Conduct Authority, "FCA fines HSBC Bank plc £63.9 million for deficient transaction monitoring controls" (2021-12-16). https://www.fca.org.uk/news/press-releases/fca-fines-hsbc-bank-plc-deficient-transaction-monitoring-controls
