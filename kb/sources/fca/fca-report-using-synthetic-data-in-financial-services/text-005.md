---
type: Source Text
title: 'Report: Using Synthetic Data in Financial Services - part 5 of 6 (pp. 36-42)'
description: 'Verbatim extracted text, pp. 36-42: Considerations of creating synthetic data; Conclusion; Next steps; and 5 more sections'
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
part: 5
parts_total: 6
content_mode: full_text
generated:
  by: process:fincrime-kb-build
  at: '2026-11-16T16:23:02Z'
verified:
- by: process:kb-validate/verbatim-coverage
  at: '2026-11-16T16:23:02Z'
sources:
- id: original
  resource: https://www.fca.org.uk/publications/corporate-documents/report-using-synthetic-data-financial-services
  title: 'Report: Using Synthetic Data in Financial Services'
  author: org:fca
  last_modified: '2024-03-11T00:00:00Z'
---

# Report: Using Synthetic Data in Financial Services

[previous part](text-004.md) | [source overview](overview.md) | [next part](text-006.md)

> Verbatim text extracted from the original (Financial Conduct Authority, 2024-03-07), part 5 of 6, pp. 36-42. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **expert interpretation**.[^original]

## Considerations of creating synthetic data


[pp. 36-37] [ref: 7.1]

7.1 Across the themes and use cases outlined above, there are a number of lessons learned and important points for practitioners to consider when creating synthetic data. Effectively generating synthetic data requires careful consideration of different technical, regulatory and ethical elements. It is important that when the relative merits of using synthetic data are benchmarked, where possible, against alternative techniques and approaches. The points below summarise considerations of creating synthetic data as derived from the report. They do not represent formal guidance or recommendations relating to synthetic data creation.

- 7.2 From the use cases above, there are several considerations relating to synthetic data creation:

##### 1. Regulatory/legal input:

There are regulatory considerations associated with synthetic data creation and usage, which vary according to the methodology, type of data and region. For examples, the use case may include personal data which requires a lawful basis for processing; this would further entail, data retention policies to be introduced as well as, adherence to data protection principles set out in the UK GDPR (and/or other international data protection laws where appropriate).

##### 2. Dependency on real world data:

The quality and accuracy of real-world data can impact the synthetic data being generated, understanding how the synthetic data is generated is an important factor to assessing the appropriateness for each use case. Where data is dynamic, careful monitoring and updates are needed to keep them up to date.

##### 3. Methodology:

It is still an open question regarding what generation methods and combinations of real-life and synthetic data are optimal for model accuracy, ethically desirable and aligned with regulatory frameworks. Where possible, it is important to test multiple generation methods and stress test what combination of real and synthetic data leads to better evaluation metrics. The selection of appropriate technologies and models is also important depending on the use case (e.g., different models might be appropriate for generating, text, tabular data, timeseries images etc. or depending on the distribution of data, or the amount of available real data).

##### 4. Deployment of data:

The accepted degree of privacy, utility and fidelity of synthetic data is likely to be influenced by the intended use of the data, for example, whether it will be used in public domains or within private system testing. In the former, privacy is usually prioritised whereas utility may take precedence in private use cases.

##### 5. Combination of Privacy Enhancing Technologies (PETs):

[p. 37]

Synthetic data is one technique that can be used to protect data privacy and is often used alongside other PETs such as differential privacy, secure multi-party computation and federated learning. It is important to be able to assess where other PETs may enhance the synthetic data or be better suited to use instead of synthetic data, especially where there may be concerns with data leakage. Where possible, comparing synthetic data to an appropriate baseline can help to understand whether synthetic data is the best approach. This can include the use of alternative privacy enhancing or traditional anonymisation techniques, experts’ knowledge of the statistical properties or simulated data to critically evaluate the strength of synthetic data.

##### 6. Biases in generated data:

Biases and inaccuracies in real world data can be replicated in synthetic datasets. Data and model testing and assessments are needed once the data have been generated to help address any biases that are present.

##### 7. Validating the data:

Understanding the privacy, utility and fidelity aspects of the synthetic data set is very important. Acceptable levels of privacy, utility and fidelity of the data should be considered on a case-by-case basis and according to the deployment of the data. For example, privacy is more likely to be the priority element where synthetic data is shared externally than in use cases where synthetic data is created for internal usage and no personal identifiable information is used.

##### 8. Technical and Domain expertise:

A strong level of data science/engineering know how and close collaboration with subject matter experts is needed to balance the variety of methodological choices whilst tailoring synthetic data to the use case in question.

##### 9. Resource and feedback:

Generating and using synthetic data is an iterative process which takes resource, including personnel time. The process can be streamlined by first understanding which stakeholders inside an organisation should be included in the generation and/ or evaluation phases; these may include legal teams, compliance professionals and executives. It is important to consider whether an organisation has the appropriate talent and skills required to generate and use synthetic data. Gathering feedback from fellow data scientists, developers and users following deployment can help to improve synthetic data sets.

## Conclusion


[p. 38] [ref: 8.1]

8.1 Synthetic data presents a valuable resource for a variety of financial services use cases, including understanding consumer behaviours, enhancing financial operations and as a tool to develop collaborative solutions to important societal issues. In the examples explored throughout this report, synthetic data plays a crucial role across the data life cycle, suggesting diverse applications to help address broader public challenges in financial services. In these use cases, synthetic data emerges as a tool with the potential to help augment data quality and quantity, mitigate biases, and facilitate the testing of systems and models whilst protecting privacy concerns, whilst still subject to the fundamental validation trade-off. Moreover, synthetic data can contribute to overcoming organisational boundaries by fostering collaboration and advancing interdisciplinary efforts to address societal challenges.

- 8.2 The quality of machine learning and artificial intelligence models is intricately linked to the quality of their data inputs. Synthetic data emerges as a valuable technique among various machine learning approaches, to enhance the performance of data-driven machine learning models. In practice, synthetic data could contribute to a range of applications, from fraud detection and reject inference to the generation of synthetic identities and customer patterns for testing open-banking solutions.

- 8.3 From the use cases explored in this report, there are several important considerations for practitioners to think about when creating synthetic data. These are centred around ensuring clarity on regulatory and legal aspects which may vary depending on the approach and the use case. Additionally, thorough evaluation of the methodology, including whether synthetic data is the best approach, whether other privacy enhancing technologies alone or in combination with synthetic data may improve model quality, should be considered.

- 8.4 Validating synthetic data is an ongoing challenge for practitioners, and existing applications indicate various approaches are currently taken to evaluate aspects such as privacy, utility and fidelity, and often vary according to the specific use case and where the data is being deployed. The use cases in the report reflect the importance of needing a high level of technical and domain expertise within the generation process and, the value of gaining feedback from users and other data scientists on the synthetic data to make continuous improvements.

- 8.5 Organisations need to be thoughtful of ethical considerations and intentional about the use of synthetic data beyond technical development. To effectively generate synthetic data, firms are likely to benefit from introducing internal governance processes that support the responsible and legal use of synthetic data. This includes being able to communicate effectively with technical and non-technical stakeholders to understand the risks and build appropriate governance procedures alongside internal guidelines.

- 8.6 The integration of synthetic data within the financial services landscape represents a forward-looking approach to harnessing the power of data. As organisations navigate this evolving landscape, strategic governance, developed with ethical considerations of the points above, will help to realise the full potential of synthetic data.

## Next steps


[p. 39] [ref: 9.1]

- 9.1 Synthetic data has a role to play in addressing societal challenges requiring collaboration, for example, between organisations, regulators, law enforcement, academics and other subject matter experts. The next phase of the SDEG will look to further understand where synthetic data is used to drive beneficial innovation in financial services, and how stakeholders can collaborate to overcome potential barriers.

- 9.2 Synthetic data presents a potential solution to data scarcity and quality issues by bringing different stakeholders together to generate novel data sets. However, there are still open questions for practitioners to consider including when it is ethically permissible to use synthetic data. Through the SDEG, we hope to enable beneficial innovation and contribute to the safe and responsible development, usage, and deployment of synthetic data in financial services.

- 9.3 To engage with us on synthetic data related matters, discuss the report or contribute to the collaboration framework, please reach out to SyntheticDataEG@fca.org.uk.

## Group members and acknowledgements


[p. 40]

1. The use cases in this report are authored by the SDEG members. With thanks to their contributions, insights and expertise that have shaped this report.

2. The FCA launched an expression of interest for the Synthetic Data Expert Group in February 2023 and the members were appointed in March. The SDEG is a sub-group of the IAG and operates within the IAG Terms of Reference and is chaired by the FCA.

- Alexandra Ebert, MostlyAI

- Caroline Louveaux, Mastercard

- Carsten Maple, University of Warwick

- David Buckley, Responsible Technology Adoption Unit

### Members of the Synthetic Data Expert Group:


- David Tracy, Smart Data Foundry

- Elena Strbac, Standard Chartered

- Giulia Fanti, Carnegie Mellon University

- Ismini Psychoula, Ofcom

- Janet Bastiman, Napier

- June Brawner, The Royal Society

- Lee Gregory, Barclays

- Luk Arbuckle, Privacy Analytics

- Lukasz Szpruch, Alan Turing Institute

- Marilena Karanika, Experian

- Michael Meehan, Howso

- Nick Clark, Cambridge Regulatory Innovation Hub

- Oxana Samko, HSBC

- Paul Comerford, Information Commissioner’s Office (ICO)

- Robin Glover, Swift

- Tom Fiddian, Innovate UK

### FCA Contributions


[pp. 40-41]

3. Emelie Bratt, Henrike Mueller, Leo Gosland, Matt Lowe, Pavle Avramovic, Rebecca Humphry, Simran Singh and Yu Bian.

4. With thanks to the BIS Innovation Hub Nordic Centre Team and Imperial College London who provided feedback on the report.

1. In advancing its commitment to innovation, the FCA has undertaken a number of synthetic data related initiatives, commencing with a DataSprint in June 2020. During the DataSprint multi-disciplinary teams collaborated in the digital sandbox to create synthetic datasets mimicking real-world financial scenarios to help innovators develop new solutions. Focusing on banking, lending, blacklists, and telecommunications, the sprints aimed to combat fraud, support financial resilience, aid vulnerable consumers, and enhance access to finance for SMEs.

## FCA synthetic data journey


[p. 41]

2. Building on this foundation, the FCA, in partnership with the City of London Corporation, launched two digital sandbox pilots. These initiatives granted participants access to synthetic data assets, an API marketplace, coding environments, and expert mentors.

- i. The first pilot, involving 28 organisations, underscored the value of synthetic data, emphasising the need for more referentially linked datasets and finer granularity. Subsequently, the Kalifa review recommended a permanent digital sandbox, a testament to the initial pilot’s success.

- ii. The second pilot, from November 2021 to March 2022, focused on solving regulatory challenges related to Environmental, Social and Governance (ESG) data and disclosure. The synthetic data generation journey for the second pilot aimed to deepen the FCA’s understanding of data generation requirements, process and methodologies.

3. Building on the evaluation from the two pilots, the FCA officially launched the permanent digital sandbox in August 2023, followed by the release of Authorised Push Payment Fraud Synthetic data in September 2023. This comprehensive offering invites applications from innovators, data providers, and mentors. Throughout this support lifecycle, the FCA actively collects and evaluates opportunities and challenges associated with synthetic data, informing our understanding of its impact to the UK financial service industry, consumers and markets.

4. These initiatives help the FCA to grow technical understanding on existing barriers to synthetic data preventing innovation and positively shape digital markets by working with industry to tackle societal issues.

May 23 – Blog – CanNov 21 – Mar 22 synthetic data enable Aug 23 –Jul/Aug 2020 – – Digital Sandbox Feb 23 – Feedback data sharing in financial Permanent digitalFCA Data Sprint Sustainability Pilot statement (FS23/1) services? sandbox openOct 20 – Feb 21 Mar 22 – Call for input Mar 23 – Synthetic data Jun 23 – FCA Sep 23 – FCA & City of– First Digital on Synthetic Data expert group launched Research Article: London Corporation launchSandbox Pilot Exploring Synthetic Authorised Push PaymentData Validation Fraud Data Set

## Glossary


[p. 42]

1. The terms below are not regulatory definitions, they included solely for the purpose of providing explanations and clarification in reference to the terms used in this document.

|Word|Description|
|---|---|
|Agent-based modelling|A simulation modelling technique to analyse a system by itsindividual agents and associated interactions (Bonabeau, 2002).|
|Data Protection Act|The Data Protection Act 2018 is the UK’s implementation ofthe General Data Protection Regulation (UK GDPR). It controlshow personal data is used by organisations, businesses or thegovernment.|
|Digital Sandbox cohort|The Digital Sandbox cohort is an 11-week initiative hosted by theFCA and the City of London Corporation, designed to stimulateand foster the development of innovative products and solutionswithin financial services. Participants are given access to data,mentors and collaboration platforms to prototype and test theirproof of concepts, with the aim of reducing time to market.|
|Fidelity|Refers to measures that directly compare the synthetic datasetwith the real dataset i.e. the statistical similarity of the syntheticdataset to the input real data (ICO).|
|General AdversarialNetwork|A type of machine learning model where two neural networksengage in a competitive process employing deep learningtechniques to enhance the precision of their predictions.|
|Privacy|Measures the risk that specific individuals (or other sensitive data)can be re-identified from the synthetic dataset.|
|Personal IdentifiableInformation (PII)|Any representation of information that relates to an identified oridentifiable individual, either directly or indirectly.|
|Synthetic data|Microdata records created to improve data utility while preventingdisclosure of confidential respondent information. Synthetic datais created by statistically modelling original data and then usingthose models to generate new data values that reproduce theoriginal data’s statistical properties. (ONS)|
|TechSprint|The FCA TechSprints are events that bring together participantsfrom across and outside financial services to develop technologybased ideas or proof of concepts to address specific industrychallenges. The events usually last between 2-5 days, and helpus to shine a light on issues and expand the discussion andawareness of potential solutions.|
|Utility|A synthetic dataset’s ‘usefulness’ for a given task or set of tasks,for example for training AI or Machine Learning models (ICO).|

Sources: Office for National Statistics (ONS), Information Commissioner’s Office (ICO), Alan Turing Institute, Bonabeau (2002)


---

[previous part](text-004.md) | [source overview](overview.md) | [next part](text-006.md)

[^original]: Financial Conduct Authority, "Report: Using Synthetic Data in Financial Services" (2024-03-07). https://www.fca.org.uk/publications/corporate-documents/report-using-synthetic-data-financial-services
