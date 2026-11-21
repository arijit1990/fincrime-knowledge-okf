---
type: Source Text
title: Finance and Insurance - part 1 of 1 (p. 1)
description: 'Verbatim extracted text, p. 1: Finance and Insurance; Finance and Insurance > Duality Technologies | Date Added: July 2021 | Proof of concept | Homomorphic Encryption |; Finance and Insurance > Hazy | Date Added: June 2023 | Product | Synthetic Data |; and 2 more sections'
resource: https://www.gov.uk/guidance/repository-of-privacy-enhancing-technologies-pets-use-cases/finance-and-insurance
tags:
- expert_interpretation
- other
- privacy_data_protection
- public_private_partnership
- uk
status: stable
source_id: uk-gov-other-finance-and-insurance
issuer: uk_gov_other
issuer_name: UK Government (other department)
jurisdictions:
- UK
tier: 1
instrument_type: other
normative_force: expert_interpretation
publication_date: '2024-11-07'
legal_status: current
part: 1
parts_total: 1
content_mode: full_text
generated:
  by: process:fincrime-kb-build
  at: '2026-11-21T23:42:13Z'
verified:
- by: process:kb-validate/verbatim-coverage
  at: '2026-11-21T23:42:13Z'
sources:
- id: original
  resource: https://www.gov.uk/guidance/repository-of-privacy-enhancing-technologies-pets-use-cases/finance-and-insurance
  title: Finance and Insurance
  author: org:uk_gov_other
  last_modified: '2024-11-07T00:00:00Z'
---

# Finance and Insurance

[source overview](overview.md)

> Verbatim text extracted from the original (UK Government (other department), 2024-11-07), part 1 of 1, p. 1. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **expert interpretation**.[^original]

## Finance and Insurance


[p. 1]

8 Use Cases

AUSTRAC is building a platform to identify financial crime across major Australian financial institutions. They have built an algorithm designed to flag suspicious links between two or more accounts and/or trace suspicious funds as they move between accounts at various financial institutions. It does this by connecting databases held by different organisations and PETs are used to protect the privacy of customers who are innocent. The project is being delivered as part of a private-public partnership, including 28 member financial institutions, and they aim to gather insights from over 100 millions accounts

LinkedIn

FFIS

This project allows a party to query data that is owned by another party and receive the results without any sensitive parameters being disclosed to the external data owner. It aims to accelerate triage in fraud and anti-money laundering (AML) investigations. The privacy of the entity and the investigation is preserved throughout, even when complex SQL-like queries are made.

### Duality Technologies | Date Added: July 2021 | Proof of concept | Homomorphic Encryption |


#### Supporting links


RUSI-FFIS report (Chapter 7)

Enveil has designed and developed an approach for financial institutions to identify matching customer information in external datasets without disclosing information about that customer. This allows financial institutions to investigate suspicious activity without revealing personal information, especially in the case that the customer being investigated is ultimately innocent. This proof of concept has been executed using synthetic data and also showed that information can still be made visible for audit, traceability and trust building where required.

RUSI-FFIS report (Chapter 7)

In their Fostering Better Finance project, Accenture used synthetic data to build prototype applications aimed at early identification of vulnerable customers based on their transactions. The project used a synthetic data generator model, produced by Hazy, a privacy tech company specialising in commercial use of synthetic data. The goal of the project was to offer earlier intervention for risks faced by customers, hence, providing better support to the vulnerable individuals with their finances. Accenture reported that use of the synthetic data allowed them to launch the project 8 times faster than expected. This is due to reduced risk from not using sensitive customer data, which, in turn, creates reduced security and governance barriers for working together with the banking client on building the project. This allowed prototypes to be built, in advance, before being tested with real customer data, hence, curtailing the risk of compromising potentially sensitive information about individuals.

### Hazy | Date Added: June 2023 | Product | Synthetic Data |


#### Supporting links


Hazy case study

This project allowed a subsidiary of a large bank to build a machine-learning sales prediction model using data from other subsidiaries of the same bank located in other countries. The product ensured that there was no data was disclosed during cross-border movement, enabling the subsidiary in question to exploit 300,000 more data points when training the model. The analyst doing the computation only ever saw the outputs of the model. The inputs were encrypted throughout the process. This product has been commercially deployed and can run on real customer data. There have been no data interoperability issues, enabling full use of distributed datasets.

### Inpher Inc. | Date Added: July 2021 | Product | Homomorphic Encryption, Multi-party Computation |


#### Supporting links


[ RUSI-FFIS report (Chapter 7) ]

With the use of partial homomorphic encryption, this pilot project allows financial institutions to learn statistics about a population from disparate private and public datasets without collecting any identifiable information. During analysis, raw data from multiple datasets is presented in tokenised form. The results of this project would enable a public authority to gather aggregate statistics about a population which would inform public policy in a privacy-preserving way. Even if a party intercepts the data at any point in the process, they would not be able to decrypt or link the various datasets.

RUSI-FFIS report (Chapter 7)

### Secretarium/Danie | Date Added: June 2023 | Product | Multi-party Computation, Trusted Execution Environment |


The DANIE consortium is made up of banks and data providers, who upload their banking data to a shared platform for analysis with a number of aims, including: 1) improving the quality of client data, 2) anti money laundering and 3) fraud detection. The DANIE platform was launched in 2020 and uses encryption and trusted execution environments such that no humans have access to the data that is being processed. DANIE uses a privacy enhancing system provided by Secretarium, and both Secretarium and DANIE are finance initiatives that emerged from Société Générale’s incubator programme in London. Additional benefits of involvement in this collaboration for participant organisations include ensuring EU reporting requirements are being met by preventing fines for reporting inaccurate data, reducing resources expended on data reviews and remediation, and improved environmental performance for data management and analysis due to the efficiencies created by the central processing system, offered by Secretarium.

#### Supporting links


Royal Society report 2023 (p. 87)

Societe Generale Article

DANIE webpage

In Germany, insurance services company Provinzial collaborated with data privacy services firm Statice, using their synthetic data to train machine learning models which optimised their predictive analytics (in particular a “next best offer” recommender engine). A key outcome of this was saving over three months that would have otherwise been spent evaluating data privacy risks, thus addressing both expense of company time and data privacy in the process of optimising their systems.

Statice case study


---

[source overview](overview.md)

[^original]: UK Government (other department), "Finance and Insurance" (2024-11-07). https://www.gov.uk/guidance/repository-of-privacy-enhancing-technologies-pets-use-cases/finance-and-insurance
