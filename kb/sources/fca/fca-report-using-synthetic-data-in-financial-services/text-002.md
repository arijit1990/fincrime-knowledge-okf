---
type: Source Text
title: 'Report: Using Synthetic Data in Financial Services - part 2 of 6 (pp. 12-20)'
description: 'Verbatim extracted text, pp. 12-20: Theme and use cases; Theme 1: Data augmentation and bias mitigation > Overview of theme; Theme 1: Data augmentation and bias mitigation > Theme 1 in the data lifecycle; and 2 more sections'
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
part: 2
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

[previous part](text-001.md) | [source overview](overview.md) | [next part](text-003.md)

> Verbatim text extracted from the original (Financial Conduct Authority, 2024-03-07), part 2 of 6, pp. 12-20. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **expert interpretation**.[^original]

## Theme and use cases


[pp. 12-13] [ref: 3.1]

- 3.1 The table below provides an overview of the use cases explored in this report. The use cases below are authored by SDEG members. More detail can be found in Appendix 1.

Theme 1: Data augmentation and bias mitigation

|Use Case Title|Focus|
|---|---|
|1.Transaction sequencesused in fraud detection machinelearning models|The availability of fraudulent financial transaction data totrain a fraud detection machine learning model|
|2.Reject inference in creditscoring|Generating synthetic data to mitigate selection bias in creditscoring training data|

Theme 2: Systems testing and model validation

|Use Case Title|Focus|
|---|---|
|1.Synthetic Open Bankingdata for model testing|Generating synthetic transaction data labels to enhancetraining sets and transactional data to resemble consumerpatterns and behaviours|
|2.Cross-sector synthetic data|Creation of synthetic data relating to individual, banks and|
|for Authorised Push Payment|fraud typologies to complement real data and be used in the|
|Fraud|FCA’s APP Fraud TechSprint|

Theme 3: Internal and external data sharing

|Use Case Title|Focus|
|---|---|
|1.Common data sets forcommunity research intosocietal challenges|The US-UK Challenge using Privacy EnhancingTechnologies to enable data sharing to improve financialcrime prevention and pandemic responses|
|2.Data sharing to increase|Using cross-organisational and international transaction|
|efficiency and effectiveness of|data to develop machine learning models to recognise illicit|
|anti-money laundering controls|payment patterns|

###### About the use cases

The following themes explore different financial services use cases where synthetic data can be used across the data lifecycle. Within each theme, SDEG members detail the use case, methodological decisions, trip hazards and lessons learned from using synthetic data.

The use cases are designed to aid practitioners to use synthetic data effectively and responsibly.

Note, given input from different authors, the tone and language may vary across use cases.

Theme 1: Data augmentation and bias mitigation

## Theme 1: Data augmentation and bias mitigation


### Overview of theme


[pp. 13-14] [ref: 4.1]

4.1 For modern machine learning pipelines, the quality of the output they produce is directly dependent on the quality of the data used to train the models, both personally identifiable information (PII) and non-PII. If the data used during training is of poor quality, incomplete, or biased the outcomes of the models trained on such data sets will be impacted. The key idea driving the use of synthetic data for data augmentation is to enhance the performance of data-driven machine learning pipelines by enhancing the training data. Furthermore, the goal of a machine learning model is not just to perform well on the training data but also post-deployment on the data that the model hasn’t been exposed to before. While synthetic data is not the only technique that can help data-driven machine learning perform well, it provides a unified data-centric solution to this challenge. However, synthetic data is necessarily a distorted version of the real data. Therefore, any inference performed on synthetic data comes with additional model risks or caveats.

- 4.2 Here we will focus on data used to develop predictive statistical or supervised machine learning models since the performance of these models are dependent on the quantity and quality of the data used to train them.

- 4.3 We define data augmentation as increasing the amount and quality of data available for use. This is particularly beneficial for machine learning models, as they rely on rich data to extract patterns from. In cases where there is insufficient volume or diversity in the data, the performance of the model might experience limitations.

- 4.4 In the data augmentation use case we discuss the availability of fraudulent financial transaction data (for example, debit or credit card payments) to train a fraud detection machine learning models. The volume of fraudulent transactions held by a financial organisation may be very low, typically make up fewer than 0.2% of transactions. Augmenting the real-world fraud data with synthetic fraudulent transactions may be used to improve detection performance.

- 4.5 Robust model performance also relies on high quality training data, representative of that on which it will be used. In particular, training data should be free of material biases such as under-representation or omission of key segments. A common source of bias is when data is filtered by a selection process, such as consumer lending decisions for credit. The second use case explores the use of synthetic data to mitigate bias resulting from a lack of information on the payment performance of previously rejected credit applicants when developing credit scores.

Theme 1: Data augmentation and bias mitigation

### Theme 1 in the data lifecycle


[p. 14] [ref: 4.6]

- 4.6 Augmenting data and mitigating bias generally occur as part of the data preparation phase, but their necessity may only become apparent after an initial model has been developed and analysed, leading to an iteration of the lifecycle.

- 4.7 The techniques discussed herein are applicable in the financial services sector but are also applicable everywhere that data augmentation and bias mitigation are needed, such as for image recognition, autonomous vehicles, home and auto insurance claims, and healthcare. To use healthcare as an example, bias in synthetic data could perpetuate existing biases, such as where certain types, classifications, illnesses, etc. are lacking. Data augmentation could be useful to combat data scarcity and potential imbalances in the data, but could also perpetuate existing biases.

### Current practices for data sharing and cross sector applicability


[pp. 14-15]

Use case 1: Transaction sequences used in fraud detection machine learning models

##### The problem statement

Financial services companies issuing cards, or providing other payment services, have a duty to protect their customers from third party fraud, whereby criminals steal payment instrument details and transact as if they were the customer. Typically, payment service providers will implement automated systems, often including machine learning models, for detecting and blocking attempts by fraudsters to make such transactions.

To train such models effectively, a sufficient volume and variety of historical fraudulent and genuine transaction attempts are required; however, attempted fraudulent transactions typically make up a very small percentage of all transactions, and the number of such transactions may be insufficient to train an effective and accurate model.

Generating synthetic data replicating fraudulent transaction patterns and including it in the training data can be a viable way to improve the model detection rate and reduce false positives (genuine transactions incorrectly classified as fraud). To achieve a model performance improvement, these synthetically produced fraudulent transactions need to be as realistic as possible.

##### Synthetic data methodology

One option for such synthetic data generation is an instance-based machine learning method using historical real fraudulent transactions to produce a set of statistically similar, synthetic fraudulent transactions. We outline the procedure below.

Theme 1: Data augmentation and bias mitigation

Consider a hypothetical set of historical fraudulent card transaction data, with three key fields: Transaction Amount (£s), Merchant Type (e.g. electronic goods retailer, food retailer, etc) and Channel (e.g. online, in-store, etc). These data will have joint distributions among each of the fields which can be used in the creation of synthetic data. To generate the first synthetic record, the process selects one field at random and picks a random value according to the distribution of that field e.g. Transaction Amount of £2,000. Next, another field is selected at random, and a value selected base on its distribution conditional on the first feature e.g. Merchant Type of electronic good retailer, given the Transaction Amount of £2,000. And so on for Channel, and any other relevant fields.

|TransactionAmount|Merchant Type|Channel|Time|
|---|---|---|---|
|£2,000|Electronics|Online|10:22 GMT|
|£142|Food|In-store|12:48 GMT|
|£617|Digital Goods|Online|21:01 GMT|

Once values for each field have been generated, the synthetic data record should be analysed for privacy, to ensure that the process did not accidentally recreate a record from the original dataset (or one that used to reidentify any of the original data) and discarded if necessary. This process may then repeat until sufficient synthetic data has been generated.

##### Evaluating privacy, utility and fidelity

[pp. 15-16]

Generally, if privacy of the original data is of concern, the synthetic data should protect the privacy of the individuals or organisations whose data was used to generate it. This use case, however, assumes that the synthetic data will be used to augment the original data, and therefore the privacy of the synthetic data with respect to the original data is not as concerning as utility and to some extent, the fidelity.

In this use case the utility of the data is met by synthesising fraudulent transaction data that is statistically similar to the training data in the ways described above. For utility, many different tests could be performed. We use the maximum mean discrepancy (MMD), Chi-squared, the Kolmogorov-Smirnov test and the Mann-Whitney test. To test fidelity, we compare the performance of the original and synthetic data across numerous machine learning models, including a classification comparison using the Fowlkes-Mallows index, and a clustering comparison performed using a combination of an intrinsic measurement (Calinski-Harabasz score) and an extrinsic measurement (a particular formulation of mutual information).

##### Trip hazards and risk of poor practice

##### _Lawful basis for processing_

The data for this use case is pseudonymised personal data, and as such, a lawful basis for processing should be established for any processing, including creating synthetic data in the way described. Only fields which are truly necessary for the generation of

Theme 1: Data augmentation and bias mitigation

synthetic data should be used, and in this case no fields which individually constitute personal information (such as names) are necessary and should be removed before analysis commences.

##### _Model Performance_

That aside, a primary concern is to ensure that a model trained on the real and synthetic data exhibits improved performance. It is important that this performance improvement is seen not just on the composite set of synthetic and real training data (which is selffulfilling, assuming model training has been performed without error), but on a holdout sample unseen by the model, and ideally on the real data alone, even if the volume is low.

##### _Model Validation_

It is also important to record the data generation process in sufficient detail that users can understand potential strengths and weaknesses. This can be achieved via auditable ‘data cards’ and is particularly important if the synthetic data is to be released to other data processors, in which case the data card should include details of the type of statistical information from the real data that the synthetic data may reveal.

The risk of revealing information about the real data is usually higher if a large volume of synthetic data is to be released to other data processors, and care should be taken to ensure that the synthetic data do not allow inferences to be made about the real data. This risk decreases the higher the dimensionality of the synthetic data.

##### Lessons learned

[p. 16]

Using synthetic data to augment the availability of fraudulent transactions works well, especially in the context where the synthetic fraudulent transaction data is used to augment (and not replace) the original fraudulent transaction data, as long as there is a lawful basis for making synthetic data from the original data.

##### The problem statement

Determining the credit worthiness of applicants for consumer credit is an important activity for lenders. For decades, automated processes based on statistical models (‘credit scores’) have been the norm, and whilst there exists a body of best-practice in the industry, this is evolving in the light of new technology and heightened expectations around bias, fairness and privacy.

### Use case 2: Reject inference in credit scoring


[pp. 16-17]

Credit scores are developed to predict the likelihood of default, based on a number of factors such as an applicant’s previous repayment history and credit utilisation. This is then used to make a lending decision.

Whist many lenders may have sufficient data from their previous lending, they suffer from a significant bias: the data does not contain repayment information for credit

Theme 1: Data augmentation and bias mitigation

applications which did not result in lending, either because the application was rejected, or was accepted but not drawn down. The latter are generally fewer and low risk, so can be safely excluded from the development. The rejects, however, may make up a significant proportion of applications and are systematically biased: they were selected by the incumbent lending strategy, not at random, and have a higher risk of default. It is therefore vital that their risk is not underestimated (to avoid lending irresponsibly) or indeed too overestimated (to avoid financial exclusion).

One solution to this challenge involves creating synthetic data on previous rejected applicants i.e. inferring whether they would have repaid the loan in the counterfactual situation that they were accepted for credit. This is known as ‘reject inference’. Whilst it is possible to source payment performance on similar loans granted by other lenders from Credit Reference Agencies (CRAs) – known as ‘reject referencing’ – this doesn’t guarantee complete or representative coverage, so some inference using synthetic data generation is always required.

##### Synthetic data methodology

Statistical modelling such as linear and logistic regression is traditionally used to generate synthetic payment performance for reject inference. However, the methodology is not straightforward due to the systematic biases described above. Techniques to mitigate this can be divided into two classes: those that rely on data with known payment performance alone, and those that augment with external performance data, typically from CRAs.

Using performance on accepts alone requires a methodology to mitigate the systematic bias: a model developed on accepted applicants is likely to underestimate risk when applied to rejected applicants. Based on analysis of the inferred risk of segments of rejects, expert judgement can be applied to adjust it to match expectations.

Empirical studies have been performed using variations of this methodology, by treating a subset of accepted applicants as if they were rejects and masking payment performance, applying the methodology, then using the masked performance to assess the accuracy of the inferred risk. They show that more systematic approaches given the best results. For example, intuitively, one would expect the reject inference model to underpredict the most on applicants with a profile (e.g. credit history) that is most different to the accepted population. This difference in profile can be estimated using an ‘Accept/Reject’ model, which predicts the likelihood that an applicant will be accepted. Those with a lower probability of being accepted have a profile most different to the accepts, so should have their inferred probabilities increased the most.

[pp. 17-18]

Whilst reject inference without external data can give acceptable results, using applicant performance on similar credit granted at a similar time with other lenders is generally an improvement. There do, however, remain a variety of methodological choices to make such as: which credit granted at other lenders is similar enough to serve as a reference; how close in time should it be to the original application; how should rejected applicants that didn’t open another credit account soon after be treated? There is no formula for these choices, they must be made on a case-by-case basis.

Theme 1: Data augmentation and bias mitigation

##### Evaluating privacy, utility, and fidelity

The nature of this use case – attaching synthetic counterfactual estimates of default risk to actual historical credit applicants – results in a different formulation of the privacy, utility, fidelity trade-off compared to generating completely new synthetic records from a benchmark dataset.

Lenders have been permitted for many decades to use consented, pseudonymised data on their previous credit applicants to develop credit scores, and the sharing of consumer credit data via CRAs is a well-established and secure process. As long as lenders and CRAs follow these good practices, generally generating synthetic data for reject inference on rejected applicants should not further impact their privacy.

Fidelity for this use case is not well defined because for a counterfactual outcome there is no ‘ground truth’ to compare to. That said, approximate benchmarks may be obtained via reject referencing, or masking the performance of some accepts, and it is good practice to use them where possible.

Ultimately, the utility of the reject inference is determined by how accurate and reasonable the predictions of the final model developed on actual and inferred outcomes are. Consideration should be given to whether the model is sufficiently conservative on previously rejected applicants, whether it correlates well with other risk indicators (such as income and credit history) and whether it is intuitive across sub-populations.

##### Trip hazards and risk of poor practice

The key risk of poor reject inference is the under- or overestimation of risk on applicants with a similar profile to those rejected historically. The best way to mitigate this is to conduct extensive validation to ensure the credit score has a reasonable behaviour on rejects. Key areas to be aware of are:

- Performance of the final model should be split by accepts and rejects to ensure that it performs well on both;

- The size of the reject population is important: for example, if 80% of historical applications were rejected, the inferred performance will dominate the model;

- Usually, the model should have better discrimination on the whole population than on accepts alone, since the rejects should be easier to rank.

##### Lessons learned

[pp. 18-20]

Validating synthetic data representing counterfactual outcomes requires extensive analysis and subject matter expertise to ensure the outputs are reasonable and relevant to the use case. A balance must be struck between overly complicated approaches which do not allow the overlay of expertise, and overly simplistic approaches which do not effectively differentiate the risk of applicants. Above all, one cannot create information from nothing. The use of external data for reference rejects can significantly improve the utility of synthetic data and consequently the performance of the credit score.

Theme 1: Data augmentation and bias mitigation

###### Regulatory considerations for data augmentation and bias mitigation

These use cases typically require the processing of pseudonymised personal data, so as usual a lawful basis for processing must be established. The most common basis is consumer consent, which is typically obtained as part of the terms and conditions of a credit product. This generally covers the processing and sharing of data for analytics in support of responsible lending and fraud prevention, including the creation of synthetic data.

Any resulting models must also conform to relevant legislation and regulation governing their use, such as The FCA Consumer Credit Sourcebook and the Equality Act 2010. Given that use of synthetic data in this way has an impact on model risk, the PRA’s supervisory statement on management of model risk (SS1/23) is also relevant for banks.

Note: this box provides an overview of the important regulatory considerations relating to use case one and two above from SDEG members. These considerations are not a comprehensive list and should not be taken as indication of a policy position or guidance.

Theme 2: System testing and model validation


---

[previous part](text-001.md) | [source overview](overview.md) | [next part](text-003.md)

[^original]: Financial Conduct Authority, "Report: Using Synthetic Data in Financial Services" (2024-03-07). https://www.fca.org.uk/publications/corporate-documents/report-using-synthetic-data-financial-services
