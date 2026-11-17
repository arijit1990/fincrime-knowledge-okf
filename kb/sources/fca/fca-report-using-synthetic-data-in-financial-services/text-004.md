---
type: Source Text
title: 'Report: Using Synthetic Data in Financial Services - part 4 of 6 (pp. 29-35)'
description: 'Verbatim extracted text, pp. 29-35: Theme 3: Internal and external data sharing > Overview of theme; Theme 3: Internal and external data sharing > Current practices'
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
part: 4
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
  resource: https://www.fca.org.uk/publications/corporate-documents/report-using-synthetic-data-financial-services
  title: 'Report: Using Synthetic Data in Financial Services'
  author: org:fca
  last_modified: '2024-03-11T00:00:00Z'
---

# Report: Using Synthetic Data in Financial Services

[previous part](text-003.md) | [source overview](overview.md) | [next part](text-005.md)

> Verbatim text extracted from the original (Financial Conduct Authority, 2024-03-07), part 4 of 6, pp. 29-35. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **expert interpretation**.[^original]

## Theme 3: Internal and external data sharing


### Overview of theme


[p. 29] [ref: 6.1]

6.1 The final stage of the data lifecycle centres on data sharing, exploring how synthetic data can be used to overcome intra- and inter-organisational boundaries that inhibit data sharing. We discuss these questions in the context of two use cases, which use synthetic data to increase the efficiency and effectiveness of public goods. This is accomplished via the provisioning of common data sets for community research into societal challenges and anomaly detection controls for financial crime (fraud and AML).

- 6.2 In both use cases, we highlight the advantages and challenges of synthetic data. Synthetic data tends to have a lower privacy risk than real data but cannot guarantee privacy; an implementation-specific risk assessment would generally be required.

- 6.3 Another primary challenge concerns trade-offs between privacy and fidelity (which in turn can affect utility). In practice, public deployments of synthetic data have erred on the side of privacy—for instance, by generating datasets that are based on simulators designed using domain expertise (e.g. simulation and agent-based modelling), rather than based on machine learning models trained on data. This contrasts with techniques often seen in the private release of real data which is utility-led. One notable counterexample is the U.S. census data release. For this, the U.S. Census Bureau used a differential privacy parameter that was larger than that used in the demonstration (that is, adding less noise, thereby providing less privacy but increasing the fidelity and ultimately utility of the release). The increase was justified on grounds that it was necessary to “best balance between the need to release detailed, usable statistics from the 2020 Census with our statutory responsibility to protect the privacy of individuals’ data”. This illustrates some of the challenges that arise regarding external data sharing.

### Current practices


[pp. 29-30] [ref: 6.4]

6.4 There have been several regional cross-bank information sharing pilot initiatives conducted in recent years. These include programmes to support better financial crime detection. Example case studies are presented in section four of Financial Action Task Force report on information sharing. These include programmes to support better financial crime detection. However, data privacy concerns and constraints remain an obstacle to wider use. The emerging field of synthetic data has the potential to reduce these obstacles and facilitate wider cross bank sharing of data models. This will help increase community understanding of the best approaches to detect financial crime such as fraud and money laundering and allow the development of more accurate tools.

Theme 3: Internal and external data sharing

6.5 The use cases described below suggest several important aspects to considers when using synthetic data for data sharing:

1. Synthetic data can be low fidelity while still having high utility, e.g., for a TechSprint or to compare different downstream models. Hence, data holders should decide what is the minimum data fidelity required to achieve their downstream goals; this determination can guide the choice of synthetic data models and techniques.

2. It is essential to understand if and how the privacy or data use restrictions on the original data also apply to synthetic data. For instance, if the original data is subject to UK/EU GDPR restrictions, the data holder should demonstrate that generated synthetic data cannot be linked to any individual from the source data.

3. There are a lack of industry-standard metrics for evaluating the three important properties of the synthetic data that is generated: privacy, utility and fidelity. As such, it is important for synthetic data deployments to justify their choice of metrics for evaluating these properties. This justification may be driven by the particular use case.

Use case 1: Common data sets for community research into societal challenges

##### Problem statement

Synthetic data is being increasingly used by government, industry, academic stakeholders to support community understanding of societal challenges and potential solutions. For example, popular machine learning platforms like Kaggle are increasingly featuring synthetic datasets of fraud, and several major banks have documented their use of synthetic data to improve fraud models, among other objectives (See market initiatives section for some examples).

Building on the TechSprint example, we have also recently seen an uptake in collaborative initiatives, such as the US-UK PETs Prize Challenge, which explored how privacy enhancing technologies could be used to drive innovative solutions that enhance artificial intelligence models without revealing sensitive data and maintaining end-toend privacy guarantees. The Challenge focused on societal issues including pandemic planning and forecasting, and financial crime prevention. The US-UK challenge involved government agencies, regulatory bodies, organisations and assessors from both nations.

##### Synthetic data methodology

[pp. 30-31]

The synthetic data was generated using a multi-layered technique with off-the shelf tools. The initial synthetic data set was then further manipulated using a combination of manual and algorithmic techniques to increase privacy. Data elements with highest sensitivity involving personal data were exclusively created artificially. This layered approach enabled the benefits of specific tools to be utilized that on their own would be insufficient to meet privacy requirements when sharing data externally.

Theme 3: Internal and external data sharing

##### Evaluating privacy, utility, and fidelity

For the PETs Prize challenge, the data is used for benchmarking the effectiveness of solutions, by a diverse community of researchers external to the data provider. As such data fidelity was deprioritised. High fidelity representations of personal data were not considered relevant for such purposes and would have unnecessarily increased data privacy risk. Hence, as the data set was not derived from real, sensitive data, there was no need to quantify the final dataset’s privacy using common metrics like differential privacy. While fraud was a component of the data set, the primary objective of the challenge was research into privacy enhancing technologies, including synthetic data, rather than fraud detection accuracy and therefore a high level of fidelity was not essential.

For the PETs Prize Challenge, utility and fidelity were not measured using quantitative metrics. Rather, the data’s utility was determined by the contestants’ ability to evaluate and compare different technologies and techniques to the data; this is a qualitative notion of utility.

Similarly, the PETs prize data set did not require quantitative measures of privacy. The data set was generated under a principle of ‘proportionality’ that states that data sets should not contain a higher data privacy risk than is necessary for the specific purpose of the use case.

##### Trip hazards and risk of poor practice

One challenge that stems from using low-fidelity synthetic data (as in the PETs challenge) is generalisability. That is, what conclusions can one draw from synthetic data that was generated by a (known or unknown) process. For example, for low fidelity approaches such as the synthetic data used for the PET prize challenge, using such data to draw conclusions on the volume or value of fraud a specific solution may detect could be counterproductive as the data distributions do not align with real world distributions.

Note that similar challenges arise in high-fidelity synthetic data; it is often unclear what conclusions one can draw from synthetic data. The level of data fidelity required to obtain similar results with synthetic data and real data is data set and problem dependent.

A data set that produces near identical results to real data with a specific synthetic data generation technique does not imply the synthetic data technique will give similar levels of accuracy on other data sets. A synthetic data generator that models each feature of a data set independently may give accurate results on problems where single variables in isolation are strong indicators of fraud but may give poor results where multi-dimensional relationships are key to fraud detection.

##### Lessons learned

[pp. 31-33]

Lower fidelity synthetic data sets can provide significant value where fidelity is not essential for the use case. For the PETs prize data, significant community insights into the strengths and weaknesses of different approaches to privacy enhancing technologies were obtained and shared within the community.

Transparency on the fidelity of the data is key to ensuring appropriate use and assessing the reliability of any conclusions being drawn from that data.

Theme 3: Internal and external data sharing

Use Case 2: Data sharing to increase efficiency and effectiveness of anomaly detection controls for fraud and anti-money laundering

##### Problem statement

The effectiveness of fraud and anti-money laundering (AML) systems is limited by the breadth of data available within their design and implementation. Organised fraud and AML operations often involve a network of accounts involving active or passive (unwitting) actors spanning multiple financial institutions. Each institution may have different demographic distributions and (perhaps thus) different transaction distributions.

As such, models that benefit from access to transaction data insights from multiple financial institutions have the potential to be more effective than solutions focused on transactions within a single bank.

##### Synthetic data methodology

This use case is based on research into synthetic data generation for development of machine learning anomaly detection models carried out at a network level using synthetic data derived from cross border transaction patterns across thousands of financial institutions and over 200 countries. This project was a collaboration between a payment network and a national research centre.

Such analytics can be used to create detailed synthetic models of both regular (legitimate) and illicit (money laundering or fraudulent) payment patterns including patterns that may not be observable from the lens of a single institution. A separate notable example with similar objectives to the project described here is Project Aurora.

For accurate machine learning research, a high-fidelity data set was needed for which advanced techniques were necessary to generate the synthetic data. To ensure utility, the synthetic data needed to preserve specific statistical characteristics of the original data, including:

- The diversity of behaviours observed across the different entities within payments. This can range from entities that transact a single time to entities that transact many times a day.

- The temporal aspects of payments. Payments from a specific entity are typically not uniform but occur in bursts or are clustered around specific periods of a day, week or month.

- Entity relationships. Payments can involve multiple counterparties and intermediaries. Accurate modelling of network relationships and topologies across entities was essential for accuracy.

- Preservation of multivariate relationships between transaction variables (e.g. currencies, banks, countries, amounts).

- Preservation of sequences of interactions. Payments are not independent, but instead show sequences where outgoing payments depend on incoming payments that were received by the same entity at an earlier time.

Theme 3: Internal and external data sharing

The technologies experimented with the aim to achieve the above goals were refined over time, using a self-built set of benchmarking tools that compared the statistical properties of real data with their synthetic equivalent.

[pp. 33-34]

It was observed that the preservation of temporal patterns within the network data was essential for the effectiveness of fraud solutions and typical approaches for synthetic data such as generative adversarial networks (GANs) and diffusion models currently lack such capabilities.

The chosen solution consisted of two parts:

- An _encoder_ that captures the detailed statistical properties of the real data.

- A _decoder_ that takes the encoded data as input and generates synthetic data as output.

For the encoder the most effective technique discovered was Temporal Graph Networks (TGNS). TGNs were originally developed for use in social media analytics due to their ability to learn complex systems.

For the decoder, originally a Recurrent Neural Network (RNN) was used but this was found to be ineffective in preserving the temporal patterns within the data. It was discovered that by utilizing a Transformer approach (utilising a variant of the Transformer models within Large Language Models) the temporal statistical characteristics of the original data were preserved.

For the specific use case, the TGN when combined with Transformers provided significantly higher fidelity and utility than alternatives while also sufficiently meeting privacy requirements. The applicability of these techniques for a broader set of use cases is however currently unknown and subject of further research.

##### Evaluating privacy, utility, and fidelity

As mentioned above, benchmarking tools were created comparing performance of real data with synthetic data as an aid to measuring utility and fidelity. In these measures, the real and synthetic datasets are compared to produce metrics such as period lengths of temporal self-similarity, distributions of graph centralities and clustering statistics, and distributions of temporal motifs.

For measuring data privacy especially, privacy associated with aggregated statistics within synthetic data, metrics were derived including Jensen-Shannon distance that compared distance between real and synthetic equivalents. Given the commercial interests of the financial institutions involved, single-payment privacy was inadequate, and some of these measures focused on ensuring a distance between synthetic and real data sets at an aggregate level. This avoids revealing potential sensitive market insights such as market shares, country footprints and/or currency portfolio make-ups.

It is intended that these types of privacy metrics can be used within a synthetic data governance framework where different uses (e.g. internal or external) would require different thresholds. However, whilst this approach was taken for this use case, we note that distance-based privacy metrics alone are known to be ineffective at protecting all

Theme 3: Internal and external data sharing

privacy concerns for synthetic data. As highlighted by recent research, membership inference attacks can be a valuable approach to evaluate privacy and identify where data may not be adequately protected against from a privacy perspective.

##### Trip hazards and risk of poor practice

Synthetic data can play an important role in supporting sharing data with privacy protection. However, there is a risk of insufficient protection through differential privacy could lead to exposure of sensitive information. This is particularly acute when dealing with aggregated data, which might contain unique or identifiable patterns.

[pp. 34-35]

Therefore, it is important to determine the level of privacy at priory with consideration of the protection provided. Once a synthetic data set is released the privacy has been fixed, and it is not possible to independently release further synthetic data from the same source data without impacting the overall privacy budget, i.e., two synthetic data releases generated using the same original data reveal more information than the data set either on their own.

Also, when releasing synthetic datasets, it is important to label when the data was generated, the generator type, the data source and the validity of the data. That is, those circumstances in which the data is useful. Synthetic data is in general best released for specific purposes.

Implementing advanced synthetic data generation techniques, such as TNG combined with Transformer models, requires deep expertise and precision. Errors in the process could compromise the synthetic data’s relevance and reliability.

The success heavily depends on accurately replicating the complex statistical characteristics of original transaction data, including the diversity of entity behaviours, temporal payment patterns, entity relationships, and multivariate transaction variables. Any inaccuracies in these areas could lead to ineffective or misleading anomaly detection.

##### Lessons learned

Achieving a balanced approach in synthetic data generation is crucial for maintaining its utility for anomaly detection while protecting sensitive features in the data.

Cross-disciplinary collaborations, as demonstrated between a payment network and a national research centre, are vital for addressing complex challenges such as financial crime, combining domain knowledge with advanced data science techniques.

Engaging in discussions with the owner or provider of the origin/source data is important to comprehend the required level of protection, i.e., the privacy budget, alongside grasping the fidelity needs and key use cases from the data users to gauge utility accurately.

The necessity for continuous refinement and validation of synthetic data generation methodologies is underscored, with benchmarking against real data serving as a vital tool for assessing and amplifying its fidelity and utility, thereby ensuring the effectiveness of developed machine learning models.

Theme 3: Internal and external data sharing

Furthermore, establishing robust synthetic data governance frameworks, inclusive of privacy metrics and considerations capable of adeptly managing privacy nuances, is essential, to safeguard data integrity and confidentiality, while optimising its utility.

###### Regulatory considerations for internal and external data sharing

As explored across the two use cases in this section, elements around data privacy are important for internal and external data sharing. No (synthetic) data can contain or imply the identity or personal details of individuals, legal entities or financial institutions. Even single words with free-text can be problematic if that word is associated with a well-known company. It should not be possible to infer the identity of an actor within a transaction by cross referencing the transaction with other public or private data. Examples include: the amount or time of transaction can act as a signature if sufficiently unique.

[p. 35]

As detailed in use case two, the system should not reveal commercially sensitive information even within aggregated statistics and distance-based privacy metrics alone are not always effective at guarding all privacy concerns. For example, by analysing the statistical characteristics of the synthetic data, information may be inferred on market share distributions or activity totals within a specific business area. Whether such inferences are commercially sensitive can be use case specific. _Model stealing attacks_ within encoder/decoder models were identified as a specific risk that required a risk assessment from third party domain experts.

Note: this box provides an overview of the important regulatory considerations relating to use case one and two above from SDEG members. These considerations are not a comprehensive list and should not be taken as indication of a policy position or guidance.


---

[previous part](text-003.md) | [source overview](overview.md) | [next part](text-005.md)

[^original]: Financial Conduct Authority, "Report: Using Synthetic Data in Financial Services" (2024-03-07). https://www.fca.org.uk/publications/corporate-documents/report-using-synthetic-data-financial-services
