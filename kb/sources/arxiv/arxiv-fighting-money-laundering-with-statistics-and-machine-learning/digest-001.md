---
type: Source Digest
title: Fighting Money Laundering with Statistics and Machine Learning - part 1 of 5 (pp. 1-7)
description: 'Verified paraphrased digest, pp. 1-7: Fighting Money Laundering with Statistics and Machine Learning > 1 Introduction; Fighting Money Laundering with Statistics and Machine Learning > 2 Terminology; Fighting Money Laundering with Statistics and Machine Learning > 3 Client Risk Profiling; and 1 more sections'
resource: https://arxiv.org/abs/2201.04207
tags:
- academic_finding
- customer_risk
- datasets_benchmarks
- global_academic
- ml_statistics
- preprint
status: stable
source_id: arxiv-fighting-money-laundering-with-statistics-and-machine-learning
issuer: arxiv
issuer_name: arXiv
jurisdictions:
- GLOBAL_ACADEMIC
tier: 3
instrument_type: preprint
normative_force: academic_finding
publication_date: '2022-11-01'
legal_status: unknown
part: 1
parts_total: 5
content_mode: digest
generated:
  by: claude-code-subagent/claude-sonnet-5-5
  at: '2026-11-22T14:46:04Z'
verified:
- by: process:kb-digest-check/anchor-match
  at: '2026-11-22T14:46:04Z'
- by: claude-code-judge-agent/claude-opus-5-5
  at: '2026-11-22T14:46:04Z'
sources:
- id: original
  resource: https://arxiv.org/abs/2201.04207
  title: Fighting Money Laundering with Statistics and Machine Learning
  author: org:arxiv
  last_modified: '2022-11-01T00:00:00Z'
digest_points: 85
---

# Fighting Money Laundering with Statistics and Machine Learning (digest)

[source overview](overview.md) | [next part](digest-002.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (pp. 1-7) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **academic finding**.

## Abstract

- **descriptive / context**: The paper reviews statistical and machine learning methods for anti-money laundering in banks and proposes a terminology built on two elements: client risk profiling and suspicious behavior flagging. (p. 1)[^original]  
  <sub>anchor: "We propose a unifying terminology with two central elements: (i) client risk profiling and (ii) suspicious behavior flagging."</sub>
- **descriptive / finding or result**: The authors find that client risk profiling is characterized by diagnostics, meaning efforts to find and explain risk factors. (p. 1)[^original]  
  <sub>anchor: "We find that client risk profiling is characterized by diagnostics, i.e., efforts to find and explain risk factors."</sub>
- **descriptive / finding or result**: Suspicious behavior flagging is characterized by non-disclosed features and hand-crafted risk indices. (p. 1)[^original]  
  <sub>anchor: "On the other hand, suspicious behavior flagging is characterized by non-disclosed features and hand-crafted risk indices."</sub>
- **descriptive / limitation**: One major challenge identified for future research is the need for more public data sets, which may potentially be addressed by synthetic data generation. (p. 1)[^original]  
  <sub>anchor: "One major challenge is the need for more public data sets. This may potentially be addressed by synthetic data generation."</sub>

## 1 Introduction

- **descriptive / context**: UNODC officials estimate money laundering amounts to 2.1-4% of the world economy. (p. 1)[^original]  
  <sub>anchor: "Officials from the United Nations Office on Drugs and Crime estimate that money laundering amounts to 2.1-4% of the world economy [1]."</sub>
- **descriptive / context**: Illicit financial flows help criminals avoid prosecution and undermine public trust in financial institutions. (p. 1)[^original]  
  <sub>anchor: "The illicit financial flows help criminals avoid prosecution and undermine public trust in financial institutions [2–4]."</sub>
- **descriptive / context**: Several organizations assert that modern statistical and machine learning methods hold great promise for improving AML operations, including identifying new laundering types and better prioritising AML resources. (p. 1)[^original]  
  <sub>anchor: "Multiple intergovernmental and private organizations assert that modern statistical and machine learning methods hold great promise to improve anti-money laundering (AML) operations"</sub>
- **descriptive / context**: The scientific literature on statistical and machine learning methods for AML is described as relatively small and fragmented. (p. 1)[^original]  
  <sub>anchor: "The scientific literature on statistical and machine learning methods for AML, however, remains relatively small and fragmented"</sub>
- **descriptive / context**: The FATF recommendations form the international AML framework; within it, any interaction with criminal proceeds practically corresponds to money laundering from a bank perspective, regardless of intent or transaction complexity. (p. 1)[^original]  
  <sub>anchor: "Within the framework, any interaction with criminal proceeds practically corresponds to money laundering from a bank perspective"</sub>
- **mandatory / requirement**: The framework requires that banks know the identity of, and money laundering risk associated with, their clients. (p. 1)[^original]  
  <sub>anchor: "know the identity of, and money laundering risk associated with, clients, and"</sub>
- **mandatory / requirement**: The framework requires that banks monitor and report suspicious behavior. (p. 1)[^original]  
  <sub>anchor: "monitor and report suspicious behavior."</sub>
- **descriptive / context**: The authors are intentionally vague about what constitutes suspicious behavior, to reflect FATF's recommendations. (p. 1)[^original]  
  <sub>anchor: "we, to reflect FATF’s recommendations, are intentionally vague about what constitutes ”suspicious” behavior."</sub>
- **descriptive / context**: Banks use electronic AML systems to raise alarms for human inquiry; officers then dismiss or report alarms to national financial intelligence units. (p. 1)[^original]  
  <sub>anchor: "banks use electronic AML systems to raise alarms for human inquiry. Bank officers then dismiss or report the alarms to national financial intelligence units"</sub>
- **descriptive / context**: Traditional AML systems rely on predefined and fixed expert rules, which are easy to interpret but inefficient. (p. 1)[^original]  
  <sub>anchor: "Although the rules are formulated by experts, they are essentially ‘if-this-then-that’ statements; easy to interpret but inefficient."</sub>
- **descriptive / finding or result**: Over 98% of all AML alarms can be false positives. (p. 1)[^original]  
  <sub>anchor: "Indeed, over 98% of all AML alarms can be false positives [17]."</sub>
- **descriptive / context**: Banks are not allowed to disclose information about alarms and generally receive little feedback on filed reports. (p. 1)[^original]  
  <sub>anchor: "Banks are not allowed to disclose information about alarms and generally receive little feedback on filled reports."</sub>
- **descriptive / context**: Money launderers may change behaviour in response to AML efforts, for example by smurfing (splitting up large transactions) to avoid reporting thresholds. (p. 1)[^original]  
  <sub>anchor: "In response, money launderers may employ smurfing (i.e., split up large transactions)."</sub>
- **mandatory / requirement**: US banks must, by law, report all currency transactions over $10,000, regardless of whether they constitute money laundering. (p. 1)[^original]  
  <sub>anchor: "banks in the United States must, by law, report all currency transactions over $10,000 (regardless of whether they constitute money laundering or not) [18]."</sub>
- **descriptive / context**: Profiles built from KYC information are often used to set the intervals for ongoing due diligence checks on that information. (p. 1)[^original]  
  <sub>anchor: "The profiles are, in turn, often used to determine intervals for ongoing due diligence, i.e., checks on KYC information."</sub>
- **descriptive / context**: Because money laundering has no direct victims, it can potentially go undetected for longer than other financial crimes such as credit card or wire fraud. (p. 1)[^original]  
  <sub>anchor: "as money laundering has no direct victims, it can potentially go undetected for longer than other types of financial crime"</sub>

## (untitled section)

- **descriptive / recommendation**: The authors list other possible research directions as semi-supervised and deep learning, interpretability, and fairness of the results. (p. 1)[^original]  
  <sub>anchor: "Other possible research directions include semi-supervised and deep learning, interpretability, and fairness of the results."</sub>

## 1 Introduction

- **descriptive / context**: The paper focuses on AML in banks and aims to give a technical review for researchers and practitioners, a terminology for policy discussions, and guidance on open challenges. (p. 2)[^original]  
  <sub>anchor: "we focus on AML in banks and aim to provide a technical review that researchers and industry practitioners"</sub>
- **descriptive / context**: The paper's aims are to propose a unified terminology, review selected exemplary methods, and present recent machine learning concepts that may improve AML. (p. 2)[^original]  
  <sub>anchor: "(i) propose a unified terminology for AML in banks, (ii) review selected exemplary methods, and (iii) present recent machine learning concepts that may improve AML."</sub>
- **descriptive / context**: Sections 3 and 4 review client risk profiling and suspicious behavior flagging respectively, each split into unsupervised and supervised methods; Section 5 covers future directions and Section 6 concludes. (p. 2)[^original]  
  <sub>anchor: "Note that both Sections 3 and 4 contain subsections that further distinguish between unsupervised and supervised methods."</sub>

## 2 Terminology

- **descriptive / context**: The authors argue banks face two principal data analysis problems in AML: client risk profiling and suspicious behavior flagging. (p. 2)[^original]  
  <sub>anchor: "we argue that banks face two principal data analysis problems in AML: (i) client risk profiling and (ii) suspicious behavior flagging."</sub>
- **descriptive / definition**: Unsupervised methods use data sets of client feature vectors without labels, while supervised methods use feature vectors paired with given labels such as risk scores. (p. 2)[^original]  
  <sub>anchor: "Unsupervised methods utilize data sets on the form _{_ x _c | c_ = 1 _, . . . , n}_ where _n_ denotes some number of clients."</sub>

## 2.1 Client Risk Profiling

- **descriptive / definition**: Client risk profiling assigns general risk scores to clients via a mapping of client features onto a generic set P, capturing money laundering risk; the example set is low, medium and high risk. (p. 3)[^original]  
  <sub>anchor: "where _ρ_ ( x _c_ ) captures the _money laundering risk_ associated with client _c_ ."</sub>
- **descriptive / definition**: Client risk profiling in this terminology works at the client level rather than the transaction level. (p. 3)[^original]  
  <sub>anchor: "We stress that client risk profiling in our terminology is characterized by working on the client, not transaction, level."</sub>

## 2.2 Suspicious Behavior Flagging

- **descriptive / definition**: Suspicious behavior flagging raises alarms on clients, accounts or transactions, with an AML system being a function that flags a transaction when its score meets a threshold. (p. 3)[^original]  
  <sub>anchor: "Suspicious behavior flagging is used to raise alarms on clients, accounts, or transactions."</sub>
- **descriptive / context**: The authors argue all AML systems rest on one premise: given that detailed investigation of all records is too expensive, investigation should concentrate on those most likely to be fraudulent, so a good system must model the probability a transaction should be reported. (p. 3)[^original]  
  <sub>anchor: "Thus, a good AML system needs to model the probability"</sub>
- **descriptive / method**: Because it can be difficult to judge a single transaction, the level of analysis may be changed to account-level features or sets of transaction feature vectors, or to client level. (p. 3)[^original]  
  <sub>anchor: "It can be difficult to determine if a transaction, in itself, is money laundering. As a remedy, the level of analysis may be changed"</sub>
- **descriptive / context**: Suspicious behavior flagging and client risk profiling can overlap at the client level, since the client risk profile can serve as a flagging score. (p. 3)[^original]  
  <sub>anchor: "Indeed, we could use _F_ ( x _c_ ) as a risk profile for client _c_ ."</sub>

## 3 Client Risk Profiling

- **descriptive / finding or result**: Studies on client risk profiling are characterised by diagnostics; unsupervised methods search for new risky observations or risk factors, while supervised methods have an explanatory focus. (p. 3)[^original]  
  <sub>anchor: "Specifically, unsupervised methods are used to search for new ”risky” observations or risk factors."</sub>
- **descriptive / finding or result**: Studies using unsupervised methods generally use relatively large data sets, whereas supervised studies use small labelled data sets, likely because of the cost of labelling. (p. 3)[^original]  
  <sub>anchor: "We also find that studies employing unsupervised methods generally use relatively large data sets."</sub>
- **descriptive / finding or result**: All reviewed client risk profiling studies use private data sets, but most share a fair amount of information about their features, unlike the suspicious behavior flagging literature. (p. 3)[^original]  
  <sub>anchor: "we note that while all studies use private data sets, most share a fair amount of information about the features that they use."</sub>

## 3.1 Unsupervised Client Risk Profiling

- **descriptive / method**: Alexandre and Balsa apply K-means clustering to build risk profiles, using about 2.4 million clients from an undisclosed financial institution with average transaction size and number as disclosed features. (p. 4)[^original]  
  <sub>anchor: "Toevaluatetheapproach,theauthorsemployadata set with approximately 2.4 million clients from an undisclosed financial institution."</sub>
- **descriptive / method**: Alexandre and Balsa also train decision trees to find classification rules that emulate the clusters, presumably because bank officers find rules easier to work with than K-means. (p. 4)[^original]  
  <sub>anchor: "The motivation is, presumably, that bank officers find it easier to work with rules than with _K_ -means."</sub>
- **descriptive / method**: Cao and Do apply clustering with slope to 8,020 transactions from a Vietnamese bank, changing the analysis to individual clients and clustering on discretised features using histogram height-to-width ratios. (p. 4)[^original]  
  <sub>anchor: "Starting with 8,020 transactions from a Vietnamese bank, the authors first change the level of analysis to individual clients."</sub>
- **descriptive / method**: Paula et al. use an autoencoder neural network to find outlier Brazilian export firms. (p. 4)[^original]  
  <sub>anchor: "Paula _et al._ [28] use an autoencoder neural network to find outlier Brazilian export firms."</sub>
- **descriptive / finding or result**: Alexandre and Balsa implement K-means with K = 7 clusters, designating two of them as risky. (p. 4)[^original]  
  <sub>anchor: "The authors implement _K_ = 7 clusters, designating two of them as risky."</sub>
- **descriptive / finding or result**: Cao and Do simulated 25 accounts with money laundering behaviour, some of which were easily identifiable in the produced clusters. (p. 4)[^original]  
  <sub>anchor: "They finally simulate 25 accounts with money laundering behavior, some easily identifiable in the produced clusters."</sub>
- **descriptive / limitation**: The source notes that much may depend on the nature of the simulations used in the Cao and Do study. (p. 4)[^original]  
  <sub>anchor: "Much may, however, depend on the nature of the simulations."</sub>
- **descriptive / method**: The Paula et al. autoencoder has five layers with 18, 6, 3, 6 and 18 neurons, with the first two forming an encoder, the middle layer giving a latent representation, and the last two forming a decoder. (p. 5)[^original]  
  <sub>anchor: "The authors specifically use 5 layers with 18, 6, 3, 6, and 18 neurons."</sub>
- **descriptive / data or feature**: The Paula et al. data set contains 819,990 firms, with features on debit and credit transactions, export volumes, taxes paid and previous customs inspections. (p. 5)[^original]  
  <sub>anchor: "The approach is tested on a data set with 819 _,_ 990 firms."</sub>
- **descriptive / finding or result**: Paula et al. measure risk by autoencoder reconstruction error and identify 20 high-risk firms. (p. 5)[^original]  
  <sub>anchor: "This way, they identify 20 high-risk firms."</sub>

## 3.2 Supervised Client Risk Profiling

- **descriptive / method**: Colladon and Remondi combine social network analysis with logistic regression, building three client graphs from 33,670 transactions of an Italian factoring firm, weighted by transaction size, connected clients' business sectors and geographic factors. (p. 5)[^original]  
  <sub>anchor: "Using 33,670 transactions from an Italian factoring firm, the authors first construct three graphs"</sub>
- **descriptive / data or feature**: Colladon and Remondi graph features include in-, out- and total-degrees, closeness, betweenness and constraint, with labels available for 288 clients indicating connection to a money laundering trial. (p. 5)[^original]  
  <sub>anchor: "A label _yc ∈{_ 0 _,_ 1 _}_ is also collected for 288 clients"</sub>
- **descriptive / finding or result**: Colladon and Remondi find in-degrees over G3 and total-degrees over G1 are associated with higher risk, while constraint over G2 and closeness over G1 are associated with lower risk. (p. 5)[^original]  
  <sub>anchor: "Results indicate that in-degrees over _G_ 3 and total-degrees over _G_ 1 are associated with higher risk."</sub>
- **descriptive / finding or result**: The Colladon and Remondi approach is described by the review as achieving an impressive performance; no numeric result is given in the excerpt. (p. 5)[^original]  
  <sub>anchor: "The approach achieves an impressive performance."</sub>
- **descriptive / data or feature**: Rambharat and Tschirhart use panel data from a US financial institution on 494 clients over 13 periods, with risk profiles low, medium and two types of high risk. (p. 5)[^original]  
  <sub>anchor: "The data tracks risk profiles _ycp ∈{_ 1 _,_ 2 _,_ 3 _,_ 4 _}_ , assigned to _c_ = 1 _, . . . ,_ 494 clients over _p_ = 1 _, ..,_ 13 periods."</sub>
- **descriptive / method**: Rambharat and Tschirhart use an ordinal random effects model with Gaussian errors and fixed effects, with features including business departments, four non-specified law enforcement actions and time dummies. (p. 5)[^original]  
  <sub>anchor: "To model the data, the authors use an ordinal random effects model where errors and fixed effects are assumed to follow Gaussian distributions."</sub>
- **descriptive / method**: Martínez-Sánchez et al. use decision trees on 181 clients of a Mexican financial institution, labelled high-risk or low-risk, with features on seniority, residence and economic activity. (p. 6)[^original]  
  <sub>anchor: "The authors use data on 181 clients, all labeled as either high-risk or low-risk."</sub>
- **descriptive / limitation**: Martínez-Sánchez et al. use no train-test split, which makes their focus on diagnostics apparent; they find clients with more seniority are comparatively riskier. (p. 6)[^original]  
  <sub>anchor: "Notably, no train-test split is used. This makes the focus on diagnostics apparent."</sub>
- **descriptive / method**: Badal-Valero et al. combine Benford's Law features from financial statements of 335 suppliers with four machine learning models to detect colluders. (p. 6)[^original]  
  <sub>anchor: "Badal-Valero _et al._ [37] combine Benford’s Law and four machine learning models."</sub>
- **descriptive / data or feature**: Badal-Valero et al. study 335 suppliers to a company on trial for money laundering, of which 23 were investigated and labelled as colluders, with the others treated as benevolent. (p. 6)[^original]  
  <sub>anchor: "Of these, 23 suppliers have been investigated and labeled as colluders."</sub>
- **descriptive / method**: Badal-Valero et al. models include logistic regression, feedforward neural network, decision tree and random forest, and address class imbalance with weighting and synthetic minority oversampling. (p. 6)[^original]  
  <sub>anchor: "These include a logistic regression, feedforward neural network, decision tree, and random forest."</sub>
- **descriptive / finding or result**: Badal-Valero et al. report synthetic minority oversampling works best, but the review notes this conclusion is apparently based on simulated evaluation data. (p. 6)[^original]  
  <sub>anchor: "However, the conclusion is apparently based on simulated evaluation data."</sub>
- **descriptive / method**: González and Valásquez model Chilean firms using false invoices with a decision tree, feedforward neural network and Bayesian network. (p. 6)[^original]  
  <sub>anchor: "Gonz´alez and Val´asquez [41] employ a decision tree, feedforward neural network, and Bayesian network to model Chilean firms using false invoices."</sub>
- **descriptive / data or feature**: González and Valásquez use data on 582,161 firms, of which 1,692 are labelled fraudulent or non-fraudulent, with features on previous audits and taxes paid. (p. 6)[^original]  
  <sub>anchor: "The authors use data on 582,161 firms, 1,692 of which have been labeled as either fraudulent or non-fraudulent."</sub>
- **descriptive / finding or result**: González and Valásquez find self-organizing maps and neural gas produce clusters with some behavioural patterns but do not appear useful for false invoice detection, while the feedforward neural network performs best on labelled data. (p. 6)[^original]  
  <sub>anchor: "While the methods do produce clusters with some behavioral patterns, they do not appear useful for false invoice detection."</sub>

## 4 Suspicious Behavior Flagging

- **descriptive / finding or result**: The suspicious behavior flagging literature is characterised by many short and suggestive papers, with very few applying outlier or anomaly detection. (p. 6)[^original]  
  <sub>anchor: "We find that the literature on suspicious behavior flagging is characterized by a large proportion of short and suggestive papers."</sub>
- **descriptive / finding or result**: The authors find ample scope to use both unsupervised and supervised methods for suspicious behavior flagging, contrary to Canhoto. (p. 6)[^original]  
  <sub>anchor: "our review demonstrates that there is ample scope to employ both unsupervised and supervised methods"</sub>
- **descriptive / finding or result**: Unsupervised flagging studies often contain little performance evaluation, whereas supervised studies use part of their labelled data for evaluation. (p. 6)[^original]  
  <sub>anchor: "Studies using unsupervised methods, however, often contain little performance evaluation."</sub>
- **descriptive / finding or result**: There is some evidence that supervised methods might perform better than unsupervised ones, but differing data and the small literature make a conclusion difficult. (p. 6)[^original]  
  <sub>anchor: "there is some evidence that supervised methods might perform better than unsupervised methods"</sub>
- **descriptive / limitation**: Non-disclosed features and hand-crafted risk indices generally make it difficult to compare studies. (p. 6)[^original]  
  <sub>anchor: "non-disclosed features and hand-crafted risk indices generally make it difficult to compare studies."</sub>

## 4.1 Unsupervised Suspicious Behavior Flagging

- **descriptive / method**: Larik and Haider combine principal component analysis and a modified K-means on about 8.2 million transactions, then flag transactions with a hand-crafted risk index based on cluster transaction sizes and frequencies. (p. 6)[^original]  
  <sub>anchor: "Given data on approximately 8.2 million transactions, the authors first seek to cluster clients."</sub>

## 3.2 Supervised Client Risk Profiling

- **descriptive / finding or result**: The Rambharat and Tschirhart study illustrates that banks can benefit from a granular risk rating of high-risk clients. (p. 6)[^original]  
  <sub>anchor: "Thestudydoes, however, illustrate that banks can benefit from a granular risk rating of high-risk clients."</sub>
- **descriptive / definition**: In the Rambharat and Tschirhart ordinal model, the cut-off values theta-m transform a continuous latent variable into the observed risk profile category. (p. 6)[^original]  
  <sub>anchor: "_θm_ represents a cut-off value transforming a continuous latent variable"</sub>
- **descriptive / definition**: Decision trees are flowchart-like models whose internal nodes split the feature space into mutually exclusive subregions. (p. 6)[^original]  
  <sub>anchor: "Decision trees [36] are flowchart-like models where internal nodes split the feature space into mutually exclusive subregions."</sub>
- **descriptive / definition**: Random forests combine multiple decision trees. (p. 6)[^original]  
  <sub>anchor: "Random forests [39], in particular, combine multiple decision trees."</sub>
- **descriptive / method**: Every tree in a random forest uses a random subset of features in every node split. (p. 6)[^original]  
  <sub>anchor: "Every tree uses a random subset of features in every node split."</sub>

## 4.1 Unsupervised Suspicious Behavior Flagging

- **descriptive / limitation**: Larik and Haider's evaluation is limited because no labels are available. (p. 7)[^original]  
  <sub>anchor: "As no labels are available, evaluation is limited."</sub>
- **descriptive / method**: Rocha-Salazar et al. combine fuzzy logic risk scores, clustering methods and principal component analysis, identifying one high-risk cluster that is scored with a hand-crafted risk index. (p. 7)[^original]  
  <sub>anchor: "Rocha-Salazar _et al._ [53] mix fuzzy logic, clustering, and principal component analysis to raise alarms."</sub>
- **descriptive / finding or result**: Rocha-Salazar et al. find fuzzy C-means produces the best clusters among strict competitive learning, fuzzy C-means, self-organizing maps and neural gas. (p. 7)[^original]  
  <sub>anchor: "The authors find that fuzzy _C_ -means [55], in particular, produces the best clusters."</sub>
- **descriptive / data or feature**: Rocha-Salazar et al. use data from a Mexican financial institution, training on 26,751 private and 3,572 business transactions and testing on 1,000 private and 600 business transactions. (p. 7)[^original]  
  <sub>anchor: "Training is done with 26,751 private and 3,572 business transactions; testing with 1,000 private and 600 business transactions."</sub>
- **descriptive / finding or result**: Rocha-Salazar et al. report good results on balanced accuracy, defined as the average of the true positive and true negative rates. (p. 7)[^original]  
  <sub>anchor: "The approach shows good results on balanced accuracy (i.e., the average of the true positive and true negative rate)."</sub>
- **descriptive / method**: Raza and Haider combine fuzzy C-means clustering with per-cluster q-step dynamic Bayesian networks trained on transaction sequences, with a hand-crafted risk index built on posterior probabilities. (p. 7)[^original]  
  <sub>anchor: "Raza and Haider [56] propose a combination of clustering and dynamic Bayesian networks."</sub>
- **descriptive / data or feature**: Raza and Haider use transaction features covering amount, period and type, and the approach is implemented on about 8.2 million transactions, presumably the same data as Larik and Haider. (p. 7)[^original]  
  <sub>anchor: "The approach is implemented on a data set with approximately 8.2 million transactions"</sub>
- **descriptive / method**: Camino et al. flag clients using an isolation forest, a one-class support vector machine and a Gaussian mixture model, combined into a single ensemble. (p. 7)[^original]  
  <sub>anchor: "Camino _et al._ [58] flag clients with three outlier detection techniques"</sub>
- **descriptive / method**: In the Camino et al. approach, isolation forests flag observations isolated by comparatively few random feature splits, one-class SVMs flag points violating a maximum margin hyperplane, and Gaussian mixtures flag observations in low-density regions. (p. 7)[^original]  
  <sub>anchor: "Observations isolated by comparatively few feature splits (averaged over all trees) are then considered outliers."</sub>
- **descriptive / data or feature**: Camino et al. test on a data set from an AML software company containing one million transactions with client-level summary statistic features. (p. 7)[^original]  
  <sub>anchor: "This contains one million transactions with client-level features recording summary statistics."</sub>
- **descriptive / limitation**: Camino et al. report positive feedback from the data-supplying company; otherwise their evaluation is limited. (p. 7)[^original]  
  <sub>anchor: "The authors report positive feedback from the data-supplying company; otherwise, evaluation is limited."</sub>
- **descriptive / method**: Sun et al. apply extreme value theory to flag outliers in transaction streams, using features counting balanced states and effective fan-ins, modelled with a generalized Pareto distribution and a probabilistic limit p. (p. 7)[^original]  
  <sub>anchor: "Sun _et al._ [62] apply extreme value theory [63] to flag outliers in transaction streams."</sub>
- **descriptive / data or feature**: Sun et al. define a balanced state as when money transferred into an account is transferred out again, and effective fan-ins as transfers into an account surpassing a limit followed by a balanced state. (p. 7)[^original]  
  <sub>anchor: "The first records the number of times an account has reached a balanced state"</sub>
- **descriptive / finding or result**: Sun et al. test their approach on real bank data with simulated noise and outliers. (p. 7)[^original]  
  <sub>anchor: "The approach is tested on real bank data with simulated noise and outliers."</sub>

---

[source overview](overview.md) | [next part](digest-002.md)

[^original]: arXiv, "Fighting Money Laundering with Statistics and Machine Learning" (2022-11-01). https://arxiv.org/abs/2201.04207
