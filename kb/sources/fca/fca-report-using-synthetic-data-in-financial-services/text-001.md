---
type: Source Text
title: 'Report: Using Synthetic Data in Financial Services - part 1 of 6 (pp. 1-11)'
description: 'Verbatim extracted text, pp. 1-11: Contents; Disclaimer; Executive Foreword; and 5 more sections'
resource: https://www.fca.org.uk/publications/corporate-documents/report-using-synthetic-data-financial-services
tags:
- data_features
- expert_interpretation
- fraud_screening_synergies
- other
- privacy_data_protection
- uk
status: stable
source_id: fca-report-using-synthetic-data-in-financial-services
issuer: fca
issuer_name: Financial Conduct Authority
jurisdictions:
- UK
tier: 1
instrument_type: other
normative_force: expert_interpretation
publication_date: '2024-03-07'
legal_status: current
part: 1
parts_total: 6
content_mode: full_text
generated:
  by: process:fincrime-kb-build
  at: '2026-11-22T04:42:14Z'
verified:
- by: process:kb-validate/verbatim-coverage
  at: '2026-11-22T04:42:14Z'
sources:
- id: original
  resource: https://www.fca.org.uk/publications/corporate-documents/report-using-synthetic-data-financial-services
  title: 'Report: Using Synthetic Data in Financial Services'
  author: org:fca
  last_modified: '2024-03-11T00:00:00Z'
---

# Report: Using Synthetic Data in Financial Services

[source overview](overview.md) | [next part](text-002.md)

> Verbatim text extracted from the original (Financial Conduct Authority, 2024-03-07), part 1 of 6, pp. 1-11. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **expert interpretation**.[^original]

[pp. 1-2]

Using Synthetic Data in Financial Services The Synthetic Data Expert Group

March 2024

##### About the Synthetic Data Expert Group

The Synthetic Data Expert Group (SDEG) is a specialised sub-group of the Innovation Advisory Group (IAG) and was established in February 2023 by the FCA Innovation department. It operates under the guidance of the IAG Terms of Reference and chaired by the FCA. The SDEG helps to foster collaboration across industry, regulators, academia, and civil society to advance the responsible use of synthetic data to shape digital markets to achieve good outcomes and digital transformation at the FCA.

The SDEG was launched in March 2023 and plans to run until November 2024.

The SDEG is comprised of 21 members who were selected against a set criterion, in an open and competitive process. The group explore issues surrounding the use of synthetic data in UK financial markets by identifying relevant use cases, key theoretical challenges and sharing practical experiences of using synthetic data. Additionally, the group has provided valuable feedback on FCA projects involving synthetic data. More information on SDEG membership can be found in the Appendix.

## Contents


[p. 2]

||Executive Foreword|4|
|---|---|---|
|1.|Introduction|6|
|2.|Context and background|8|
|3.|Theme and use cases|12|
|4.|Theme 1: Data augmentation andbias mitigation|13|
|5.|Theme 2: System testing andmodel validation|20|
|6.|Theme 3: Internal and externaldata sharing|29|
|7.|Considerations of creating synthetic data|36|
|8.|Conclusion|38|
|9.|Next steps|39|

###### Appendix 1

Group members and acknowledgements

###### Appendix 2

FCA synthetic data journey

Appendix 3 Glossary

Appendix 4 References

##### Sign up for our news and publications alerts

See all our latest press releases, consultations and speeches.

## Disclaimer


[p. 3]

This report has been collectively authored by members of SDEG and colleagues across the FCA. The contents of this report reflect the practical experiences members of the SDEG have encountered when generating or using synthetic data. The report is designed to help regulators and industry practitioners better understand the opportunities and challenges of synthetic data.

The contents of this report do not represent the views of the FCA or any participating organisation. It does not endorse or condemn the use of synthetic data and does not imply compliance with UK data protection law.

This report and the applications, discussions and outputs of the Synthetic Data Expert Group should not be taken as an indication of recommendations, guidance or future policy.

## Executive Foreword


[pp. 4-5]

Jessica Rusu, CDIIO, FCA

Data is pivotal to financial services and is needed to help build intelligent systems that drive forward transformation. The FCA data strategy highlights the critical role data can play in developing innovative solutions that help to address key challenges and unlock new opportunities in financial services.

I am pleased to introduce the Synthetic Data Expert Group’s report, which explores how synthetic data can be used to overcome data challenges and sheds light on practical applications in financial services. The Synthetic Data Expert Group (SDEG) is a subgroup of the Innovation Advisory Group (IAG), tasked with exploring the use of synthetic data in financial markets.

This report reflects a diverse range of perspectives, expertise and skills. It is a culmination of extensive research and collaboration within the SDEG, focusing on three key themes across the data lifecycle; data augmentation and bias mitigation, system testing and model validation, and internal and external data sharing for fraud controls. These themes represent key areas where synthetic data offers transformative implications while remaining cognisant of the associated risks and pitfalls inherent in these advancements.

Synthetic data is one of the many privacy enhancing technologies that can expand data usage and support data sharing without revealing underlying sensitive information contained in the data. Although there are still open questions which are being researched, synthetic data has the potential to help contribute to some of the large public policy issues in financial services, such as financial crime and fraud, and drive societal good through fostering a fairer financial landscape.

For example, synthetic data can serve as a tool for enhancing the robustness of fraud detection models and improve their adaptability to evolving threats. The exploration of synthetic data in credit scoring highlights its potential to mitigate biases, cultivating a fairer and more inclusive financial landscape. As technology advances, rigorous system testing and model validation becomes increasingly important. The Groups findings show

how synthetic data can help simulate diverse scenarios, supporting the resilience and accuracy of financial systems. The report also addresses the complexities of internal and external data sharing for fraud and anti-money laundering controls. Synthetic data emerges as a promising approach to facilitate collaboration while safeguarding sensitive information. Striking the right balance between information sharing and data protection is crucial, and this report provides valuable insights into this.

The deep expertise offered by SDEG members in this report provides valuable insights into some practical applications of synthetic data that can help shape the future landscape of data usage in the financial sector.

In conclusion, I would like to commend the SDEG’s extensive efforts in producing this report and thank all its members alongside FCA colleagues. I believe that the insights and conclusions provided will serve as a cornerstone for industry practitioners, policymakers, and regulators, and provide a new mechanism for cross-sector collaboration. Further understanding the potential benefits and drawbacks of synthetic data is important for advancing the resilience, fairness, and efficiency of the financial services sector.

Sincerely,

Jessica Rusu, Chief Data, Information and Intelligence Officer, FCA

## Introduction


[p. 6] [ref: 1.1]

- 1.1 As financial services become more digital, an increasing volume of data is recorded. Vast data pools can help firms to better understand business operations and reporting, test and develop new products and/or services, improve decision making and lead to consumer benefit through more personalised services and innovative financial products. Access to data enables institutions to use more advanced modelling techniques and train artificial intelligence (AI) models more effectively. Despite a rise in the amount of data that is generated, challenges remain for institutions to access and share data that could drive societal benefit.

- 1.2 Synthetic data is one of the many Privacy Enhancing Techniques (PETs) that can be used to mitigate against the privacy risks of data sharing. Synthetic data is a privacypreserving technique that can be used to address the challenges associated with sharing sensitive data such as personal or financial data. It works by generating statistically realistic but artificial data that can be used to create advanced modelling techniques and train AI models without compromising individual privacy or data protection laws.

- 1.3 The FCA’s feedback statement on the Synthetic Data Call for Input identified data availability, quality and regulatory uncertainty as some of the key challenges industry are currently facing when trying to generate and use synthetic data. In response to the feedback statement, in March 2023 the FCA set up the Synthetic Data Expert Group (SDEG), bringing together 21 experts from across industry to help overcome barriers to adoption relating to synthetic data in financial services and regulatory circles.

- 1.4 The generation of synthetic data has the potential to help industry and regulatory bodies address pressing societal challenges and perennial issues in financial services, such as fraud and financial crime. This work supports the FCA’s three-year strategy by leveraging shared expertise and providing insights to help shape digital markets to achieve good outcomes and digital transformation at the FCA.

### Aims of the report


[pp. 6-7] [ref: 1.5]

- 1.5 This report provides insight into the experiences of the SDEG members in generating and applying synthetic data in the context of financial services. It aims to help industry and regulatory practitioners to develop a comprehensive understanding of the techniques, tools, practical challenges and opportunities associated with synthetic data to contribute to the effective and safe deployment of synthetic data.

- 1.6 The insights of this report will be of interest to industry participants including financial services, regulators and policymakers internationally. The key findings will serve as a helpful guide by explaining the steps to consider when creating and using synthetic data,

and the types of problem statements where synthetic data can be useful. Whilst the use cases in this report are explored in relation to financial services, the insights can also be applied to other sectors.

- 1.7 Applications of synthetic data are diverse. Responses to the Feedback Statement and wider research indicate themes are beginning to emerge around how synthetic data can be used. Based on these themes and the expertise of members, we have selected three elements of the data lifecycle to illustrate the utility of synthetic data.

1. Data augmentation and bias mitigation: The transformation of data to expand and/or reduce the inherent bias associated with the underlying data for model generation.

2. Systems testing and model validation: The generation of synthetic data to rigorously test the robustness of AI, machine learning systems and validate their performance under diverse scenarios.

3. Internal and external data sharing: The responsible sharing of synthetic data and associated models within an organisation (internal) and/or to support external facing financial services.

- 1.8 Each theme serves as an illustration of the different opportunities and challenges that can arise when using synthetic data effectively and responsibly in financial services and how elements such as privacy, utility and fidelity are considered in practice.

- 1.9 Within each of the three themes, SDEG members identified two use cases where synthetic data has proved beneficial in financial services and provide learnings and insights on each. The use cases include fraud detection, credit scoring, open banking, authorised push payment (APP) fraud and anti-money laundering (AML). A full overview of the themes and use cases are found on page 12.

- 1.10 Through exploring different applications across the data lifecycle, the report shows examples of how synthetic data can be used to drive societal good through fostering a more inclusive and fair financial landscape that is underpinned by responsible and robust modelling techniques.

## Context and background


### Synthetic data and privacy enhancing technologies (PETs)


[pp. 8-9] [ref: 2.1]

- 2.1 Synthetic data can be challenging to define because it is currently used across a broad spectrum of sectors in addition to financial services and for a wide range of activities. Accounting for this, the Royal Society define synthetic data as:

- _“...data that has been generated using a purpose built mathematical model or algorithm, with the aim of solving a (set of) data science task(s).”_

- 2.2 There are different generation techniques that can be used to create synthetic data. These often include the use of agent-based modelling, econometric techniques, deep learning architectures such as Generative Adversarial Networks (GANs), Variational Auto-encoders (VAEs), gaussian copulas or a mixture of techniques.

2.3 The chosen approach is often dictated by a range of factors such as the complexity of the data inputs, the use case/problem statement in question and the desired outcome and results. Synthetic data is not the only technique that can be used to protect data privacy. There are other PETs, such as differential privacy or homomorphic encryption, that may be more appropriate to use than synthetic data. It is also common to use several PETs in-combination with each other. The box below provides more information on different types of PETs.

###### Privacy Enhancing Technologies (PETs) at a glance

PETs are a group of emerging technologies that enable the sharing of datasets whilst preserving privacy.

The Information Commissioner’s Office (ICO) define PETs as “…technologies that can help organisations share and use people’s data responsibly, lawfully, and securely, including by minimising the amount of data used and by encrypting or anonymising personal information”

Examples of PETs include:

- Homomorphic encryption: an encryption method that enables computational operations on encrypted data.

- Secure multi-party computation: is a tool that enables distributed computation, where analysis can occur on combined data sets without different parties revealing the private source data to one-another.

- Federated Learning: a machine learning approach where a model is trained on individual devices without sharing the raw data.

- Differential privacy: differential privacy adds ‘statistical noise’ to a dataset to mitigate the privacy risk, and can be used to statistically quantify the privacy risk of a dataset.

- Zero-Knowledge proof: a method whereby one party can prove to another party that a given statement is true without revealing the statement’s contents.

- Synthetic data: data generated using data synthesis algorithms, replicating the patterns and statistical properties of real data (which may be personal information).

More information on the PETs above can be found here.

Box 1: Information on PETs has been summarised from ICO Final Guidance on Privacy Enhancing Technologies (ICO, 2023) and the FCA’s feedback Statement on Synthetic Data Call for Input (FCA, 2023).

### Evaluating privacy, utility and fidelity


[pp. 9-10] [ref: 2.4]

2.4 A common challenge when generating synthetic data is validating that the data that has been created is fit for purpose, with the appropriate characteristics for the use case in question, yet private enough to protect the underlying data. The FCA, ICO and Alan Turing Institute held a joint roundtable in March 2023 to explore the emerging techniques that are used to validate synthetic date and industry/academic perspectives on validation approaches.

2.5 The roundtable identified three key elements to consider when evaluating synthetic data; privacy, utility, and fidelity. This means the synthetic data that has been created is private enough to protect the individuals/firms behind the data, has enough utility for the task at hand and has the desired statistical properties of the real data. Any data sharing technology, including synthetic data, is subject to a trade-off between privacy, utility and fidelity.

###### Definitions only for the purpose of this report

Privacy: Measures the risk that specific individuals (or other sensitive data) can be re-identified from the synthetic dataset.

Utility: A synthetic dataset’s ‘usefulness’ for a given task or set of tasks, for example for training AI or Machine Learning models.

Fidelity: Refers to measures that directly compare the synthetic dataset with the real dataset i.e., the statistical similarity of the synthetic dataset to the input real data.

Box 2: Concepts to consider when validating synthetic data. Source: Synthetic Data - what, why and how? (Jordan et al. 2022)

- 2.6 Measuring the privacy, utility, and fidelity of synthetic data sets is crucial. Assessment of privacy safeguards preserves confidentiality and ensures legal, regulatory, and ethical standards are met. Evaluating the utility and fidelity ensures the relevance and accuracy of the synthetic data against unwanted access, and directly impacts the reliability of machine learning models trained on the data for real-world applications.

- 2.7 There are different approaches one can take to evaluate the privacy, utility, and fidelity of synthetic data. The selection of metrics and qualitative judgments may depend on factors such as the problem statement, use case and end application of the data.

- 2.8 For each of the use cases in this report, the authors provide an overview of the tradeoffs and key considerations of evaluating the privacy, utility, and fidelity of the problem statement in question. Validating these properties are essential to the effective and safe deployment of synthetic data. As such, we expect this to be an ongoing area of research and continue to see developments in how these characteristics can be evaluated.

### Market initiatives


[pp. 10-11] [ref: 2.9]

- 2.9 There is increasing awareness of synthetic data’s effectiveness in addressing data challenges within the financial sector. The Information Commissioner’s Office (ICO) actively contributed to this landscape by disseminating guidance on PETs and exploring the practical applications of synthetic data for achieving data minimisation objectives. This commitment is further emphasised by the Responsible Technology Adoption (RTA) unit’s PETs Adoption Guide, highlighting the integration of privacy-enhancing technologies within regulatory frameworks. In the UK, academic institutions including the Alan Turing Institute and the Royal Society, actively contribute to the ongoing dialogue on privacy-preserving research.

- 2.10 The relevance of synthetic data is underscored by innovation challenges such as the UK-US PETs Challenge led by governmental, standard-setting and research institutions in the United Kingdom and the United States, and research initiatives from bodies like the OECD and the United Nations. A notable recent contribution by the Bank for International Settlements (BIS) Innovation Hub’s Nordic Centre, Project Aurora, explored how PETs could be used to address AML challenges through collaboration analytics and learning. This project demonstrated the complexity associated with using PETs, machine learning models and network analysis to counter money laundering and enhance detection models. In the US, the National Institute of Standards and Technology (NIST) has a comprehensive work programme supporting synthetic data generation, including the creation of a suite of open source tools and prize challenges to advance data sharing.

- 2.11 In the financial sector, there are a growing number of organisations using synthetic data to develop algorithms for generating realistic datasets. Topics of interest often focus on areas such as anti-money laundering, customer journey analysis, payment processes, documentation, and equity market data. In industry, many technology firms are employing synthetic data techniques to navigate complex data sharing challenges.

- 2.12 For instance, within Microsoft’s AI Lab project, specifically the synthetic data generator, has been devised to safeguard privacy during the sharing and analysis of sensitive datasets. Amazon Science has published work on generating synthetic data to overcome challenges associated with expensive and complex data collection. Specifically, Amazon’s approach involves employing a Large Language Model (LLM)-based “teacher” model to generate synthetic training data for a specific task, subsequently fine-tuning a smaller “student” model with the generated data. These initiatives reflect a broader industry trend, signalling the exploration of synthetic data beyond financial services.

- 2.13 In summary, the increasing level of research and experimentation of synthetic data across a diverse range of domains indicates its potential in fostering beneficial innovation and support developments in financial services.


---

[source overview](overview.md) | [next part](text-002.md)

[^original]: Financial Conduct Authority, "Report: Using Synthetic Data in Financial Services" (2024-03-07). https://www.fca.org.uk/publications/corporate-documents/report-using-synthetic-data-financial-services
