---
type: Source Text
title: Authorised Push Payment synthetic data - part 1 of 1 (p. 1)
description: 'Verbatim extracted text, p. 1: Authorised Push Payment synthetic data > Synthetic data overview; Authorised Push Payment synthetic data > Key features of the APP fraud dataset; Authorised Push Payment synthetic data > Accessing the data; and 1 more sections'
resource: https://www.fca.org.uk/firms/digital-sandbox/authorised-push-payment-synthetic-data
tags:
- data_features
- dataset
- datasets_benchmarks
- empirical_observation
- fraud_screening_synergies
- uk
status: stable
source_id: fca-authorised-push-payment-synthetic-data
issuer: fca
issuer_name: Financial Conduct Authority
jurisdictions:
- UK
tier: 1
instrument_type: dataset
normative_force: empirical_observation
publication_date: '2025-03-04'
legal_status: current
part: 1
parts_total: 1
content_mode: full_text
generated:
  by: process:fincrime-kb-build
  at: '2026-11-17T17:21:51Z'
verified:
- by: process:kb-validate/verbatim-coverage
  at: '2026-11-17T17:21:51Z'
sources:
- id: original
  resource: https://www.fca.org.uk/firms/digital-sandbox/authorised-push-payment-synthetic-data
  title: Authorised Push Payment synthetic data
  author: org:fca
  last_modified: '2025-12-05T00:00:00Z'
---

# Authorised Push Payment synthetic data

[source overview](overview.md)

> Verbatim text extracted from the original (Financial Conduct Authority, 2025-03-04), part 1 of 1, p. 1. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **empirical observation**.[^original]

[p. 1]

Access your Connect, Online Invoicing System and RegData tasks in one place. Find out more.

- Financial crime

Read about our Authorised Push Payment (APP) fraud synthetic data, which covers individual and business identities, transactions, telecom data, and fraud to improve detection.

In 2022, APP fraud losses reached £485 million, highlighting the urgent need for advanced technological solutions. To address this challenge, the FCA and Payment Systems Regulator (PSR) hosted an APP Fraud TechSprint , identifying a critical barrier: limited access to data for innovation. This led to the creation of a synthetic dataset designed to support fraud detection innovations while safeguarding consumer privacy.

## Authorised Push Payment synthetic data


### Synthetic data overview


The APP synthetic datasets were generated through agent-based simulations, a modelling approach that replicates the behaviours and interactions of approximately 20,000 individuals over two years. They cover a wide range of data, including:

- individual and business identities

- bank account details

- phone call and SMS metadata

- fraud instances (both reported and successful)

The data is structured across 4 synthetic banks and 2 synthetic telecom operators. The banking data is formatted to reflect what would typically be accessible by an individual with high-level access, allowing visibility into fields like unredacted personal information of account holders, detailed transaction narratives, and destination account details for payments. Similarly, the telecom data is unredacted, providing access to call and text histories for each data subject. Both the banking and telecom data encompass information on individuals and businesses, and it is possible to find instances where fraudsters have used business accounts to receive fraudulent payments.

### Key features of the APP fraud dataset


The APP fraud dataset spans across 37 datasets, featuring:

- 15 million transactions

- 58 million data points

- 61,000 attempted fraud events

- a 2-year timeline, with data on 20,000 synthetic individuals

This dataset enables users to model, detect, and mitigate seven types of APP scams, including:

- romance

- investment

- purchase

- advance fee

- policy

- family

- bank impersonation scams

By the end of 2024, the dataset – launched in September 2023 – had been accessed over 135,000 times, supporting 65 users across 42 projects, including 20 projects focused on fraud prevention. The dataset remains available, with future iterations planned as part of FCA Innovation’s ongoing initiatives.

Between January and July 2024, the dataset continued to evolve, incorporating new scam types, enhanced consumer profiles, and additional fraud-related features. These updates have expanded fraud coverage and provided a more comprehensive view of consumer behaviours.

### Accessing the data


The APP fraud dataset is accessible via the FCA Innovation platform and will continue to evolve throughout 2025 with ongoing enhancements and new features. These updates will refine and expand the dataset, ensuring greater value for users.

By providing a richer, more comprehensive view of consumer background data, the dataset enhances analytical capabilities and supports more informed decision-making. Beyond fraud detection, it can also help strengthen Consumer Duty compliance and improve outcomes for Digital Sandbox users.

For more information on how to apply and access the dataset, visit the Digital Sandbox .

The APP fraud dataset evaluation report , conducted by WhiteCap Consulting in September 2024, assessed the completeness, accuracy, and usability of the dataset. The evaluation confirmed that the dataset can be effectively used by innovators testing data for their projects. It also identified data gaps and suggested improvements for future data collection, offering insights that will aid in more comprehensive analysis and decision-making in the fight against APP fraud.

### Use cases and outcomes of this data


The report includes:

- project timeline

- data enhancements

- Digital Sandbox participants and their feedback

These insights help further clarify how the dataset has been used and identify areas for future improvements.

The APP fraud synthetic datasets were created and advanced by Aizle, in collaboration with the FCA and the City of London Corporation (CoLC).

The FCA and CoLC have a long-standing partnership since 2020, initially launching the Digital Sandbox pilot to support the development of technological solutions addressing pandemic-related challenges. Building on this success, the FCA and CoLC continued collaborating to explore the Digital Sandbox's role in fostering innovation, aligning with the Kalifa Review recommendations for a permanent Digital Sandbox to support UK fintech innovation.


---

[source overview](overview.md)

[^original]: Financial Conduct Authority, "Authorised Push Payment synthetic data" (2025-03-04). https://www.fca.org.uk/firms/digital-sandbox/authorised-push-payment-synthetic-data
