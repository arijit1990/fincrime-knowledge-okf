---
type: Source Text
title: A Literature Review on Bias in Supervised Machine Learning - part 1 of 3 (pp. 1-13)
description: 'Verbatim extracted text, pp. 1-13: Research Note; Research Note > FCA research notes in financial regulation; Research Note > Contents; and 3 more sections'
resource: https://www.fca.org.uk/publication/research-notes/literature-review-bias-in-supervised-machine-learning.pdf
tags:
- academic_finding
- academic_paper
- data_governance
- model_validation
- responsible_ai
- uk
status: stable
source_id: fca-a-literature-review-on-bias-in-supervised-machine-learning
issuer: fca
issuer_name: Financial Conduct Authority
jurisdictions:
- UK
tier: 1
instrument_type: academic_paper
normative_force: academic_finding
publication_date: '2024-12-11'
legal_status: current
part: 1
parts_total: 3
content_mode: full_text
generated:
  by: process:fincrime-kb-build
  at: '2026-11-21T23:42:13Z'
verified:
- by: process:kb-validate/verbatim-coverage
  at: '2026-11-21T23:42:13Z'
sources:
- id: original
  resource: https://www.fca.org.uk/publication/research-notes/literature-review-bias-in-supervised-machine-learning.pdf
  title: A Literature Review on Bias in Supervised Machine Learning
  author: org:fca
  last_modified: '2024-12-11T00:00:00Z'
---

# A Literature Review on Bias in Supervised Machine Learning

[source overview](overview.md) | [next part](text-002.md)

> Verbatim text extracted from the original (Financial Conduct Authority, 2024-12-11), part 1 of 3, pp. 1-13. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **academic finding**.[^original]

## Research Note


[pp. 1-2]

A Literature Review on Bias in Supervised Machine Learning

Daniel Bogiatzis-Gibbons, Lawrence Charles, Harry Dewing, Camilla Gretschel, Maria Jomy, Annette Reid, Ryan Slack

The FCA is committed to encouraging debate on all aspects of financial regulation and to creating rigorous evidence to support its decision-making. To facilitate this, we publish a series of Research Notes, extending across economics and other disciplines.

The main factor in accepting papers is that they should make substantial contributions to knowledge and understanding of financial regulation. If you want to contribute to this series or comment on these papers, please contact Kieran Keohane (Kieran.Keohane@fca.org.uk).

### FCA research notes in financial regulation


#### Disclaimer


[p. 2]

Research notes contribute to the work of the FCA by providing rigorous research results and stimulating debate. While they may not necessarily represent the position of the FCA, they are one source of evidence that the FCA may use while discharging its functions and to inform its views. The FCA endeavours to ensure that research outputs are correct, through checks including independent referee reports, but the nature of such research and choice of research methods is a matter for the authors using their expert judgement. To the extent that research notes contain any errors or omissions, they should be attributed to the individual authors, rather than to the FCA.

#### Authors


All the authors at the time of writing work for the FCA, and Daniel is a PhD candidate in Politics at Birkbeck College, University of London.

We would like to thank Edward Barrett, Wenjin Li, Lucas Lafone, Freddie Levett, Brittany Bainbridge, Ayesha Dayaji, Vicki Jordan, Henrike Mueller, and Dara Jeyasundaram for their in-depth reviews of the content of this note.

All our publications are available to download from www.fca.org.uk. If you would like to receive this paper in an alternative format, please call 020 7066 9644 or email publications_graphics@fca.org.uk or write to Editorial and Digital Department, Financial Conduct Authority, 12 Endeavour Square, London E20 1JN.

### Contents


[p. 3]

|Non-Technical Summary|3|
|---|---|
|1Introduction|4|
|Background|4|
|Key points|6|
|2What is bias and how does it come about?|7|
|What is bias?|7|
|The general idea of bias|7|
|Protected Characteristics|7|
|Vulnerability|8|
|Other Demographic Characteristics|8|
|Bias in an algorithmic (vs. human) context|8|
|What contributes to model bias?|9|
|Problem-framing|9|
|Data collection|10|
|Algorithm training|11|
|Bias metrics and what they measure|12|
|3De-biasing algorithms where data on demographic characteristics|or|
|characteristics of vulnerability are available|14|
|What is de-biasing in a supervised machine learning context in the current acade|mic|
|literature?|14|
|De-biasing techniques|15|
|Pre-processing|15|
|In-processing|16|
|Post-processing|17|
|Considerations|17|
|4Mitigating bias when data on demographic characteristics|or|
|characteristics of vulnerability cannot be collected or proxied|19|
|Collaborative online platforms|19|
|Summarising contextual research|20|
|Common features and their associations with demographic characteristics orcharacteristics of vulnerability|20|
|Model complexity|21|
|Exploratory bias analysis|21|
|5Conclusion|23|
|Annex 1 - References|25|
|Annex 2 – Glossary|30|

### Non-Technical Summary


[p. 4]

This note provides a review of available academic and ‘grey’ literature to explore how biases may arise and may be mitigated in Supervised machine learning models used to make predictions or assist in decision-making about individuals. It is a research piece as part of a broader academic conversation.

In this note, bias refers to _unjustified differences in predictions or decision-making based on the demographic characteristics, or wider life or social circumstances of a person, such as characteristics of vulnerability_ (see Chapter 2). These disparities may arise from several sources, discussed in the literature, including historical biases in data, modelling choices, or how humans selectively use predictive models (for instance, if human judgment is used, advertently or not, more to help a particular group).

This note focusses on the technical measurement and mitigation aspects of bias. We do not provide any opinion on what constitutes unfair treatment or discrimination from a legal standpoint, or more generally what is required of organisations to meet any applicable legal requirements, including data protection law.

There are a range of different ways to measure bias outlined in the academic literature (see Chapter 3), which reflect different interpretations of what constitutes fairness. One promising metric is conditional demographic disparity, which asks whether the same proportion of two or more groups would, for example, get a loan based on similar characteristics (e.g., both being employed). However, any measurement of bias will inevitably need to be considered in fuller context of the social and economic situation a model is deployed in and not used just mechanically.

- When data on demographic characteristics or wider life or social circumstances can be collected or proxied, several methodologies that may help mitigate bias (see Chapter 4) were identified from the literature, for example by flagging cases for human review where potentially biased or less confident predictions are made.

In cases where demographic characteristics or wider life or social circumstances cannot be measured, we identified two alternatives from the literature that could help mitigate the potential for bias to occur (see Chapter 5).

- Firstly, using existing evidence on potential biases to inform decision-making, for example identifying features that may lead to bias based on a market level view.

- Secondly, intuition-based evaluation of generated variables or rules which help identify potential biases.

Overall, addressing bias in machine learning models requires careful consideration of context, as this will ultimately inform which demographic characteristic/s if any might be of concern, as well as the methods that are appropriate (if any) to measure and mitigate any potential bias.

### 1 Introduction


#### Background


[p. 5]

Artificial intelligence (AI) models represent a potentially important growth industry for the UK. Within financial services, AI has the potential to improve consumer outcomes, for example through better targeting of consumer support. However, AI does not come without risks.

In its AI Update (FCA 2024), the FCA highlighted how key elements of its regulatory framework relating to consumer protection would be relevant to upholding fairness in the use of AI systems. As part of this, the Update flags the FCA’s Guidance on the Consumer Duty which highlights that firms using AI technologies in a way that embeds or amplifies bias, leading to worse outcomes for some groups of consumers, might not be acting in good faith for their consumers, unless differences in outcome can be justified objectively.

This note focusses on bias in supervised machine learning models, which are in essence cases where some available outcome (such as future risk of defaulting on a loan) is predicted based on past training data. Specifically, it focusses on how differences in predictions for groups sharing different demographic characteristics or characteristics of vulnerability might be measured, understood, and mitigated.

For the purposes of this note, when referring to “demographic characteristics” we mean:

- the set of protected characteristics protected by equalities legislation (age, disability, gender reassignment, marriage or civil partnership, pregnancy and maternity, race, religion or belief, sex, and sexual orientation), and

- broader demographic characteristics (such as socio-economic status or region)

By “characteristics of vulnerability” we mean the indicators set out in our Guidance for firms on the fair treatment of vulnerable customers (FCA, 2021) related to the 4 key drivers of health, life events, resilience, and capability.

Empirical work on AI shows how there could be potential differences in predicted risk or outcomes in financial services based on demographic characteristics. For example, a recent paper shows that more complex credit scoring models disadvantage minority borrowers in a US context, partly by inferring race, and partly through more accurate targeting of individual risk (Fuster et al., 2022). In a UK context, there has been historical work on patterns of redlining by landlords in the UK which could generate potential for long-run differences in the riskiness of areas in which members of minority ethnic groups tend to live (Wetherell, 2020).

In this note, we focus on one kind of AI called supervised machine learning, where a set of known inputs like prior credit history is used to predict a fixed future output, such as the risk of defaulting on a new loan or credit card (Hastie, Tibshirani, and Friedman,

[p. 6]

2001). We will usually refer to cases of binary classification i.e., where there are only two possible outcomes such as an individual defaulting on a loan or not, in part because this is where the academic literature is best developed. We also focus on differences in average outcomes by different demographic groups, which relates to what is called distributive justice in political science, or who gets what outcome or is charged what price on the basis of some inalienable characteristic of that person (see e.g. Gabriel, 2022).

By bias we specifically mean unjustified differences by group membership in predictions of risk or other future outcomes like willingness to pay, that typically feed into decisions about the prices to charge and decisions to provide products to individual consumers with adverse impacts for the impacted groups. Bias is intentionally defined here more narrowly than ethical notions of fairness.

Our underlying research focused on the following technical question: how can these differences in predictions be measured when using supervised learning, and how can they be mitigated in that context? We focus on both how existing literature suggests this can be done when demographic characteristics or characteristics of vulnerability can be measured for or proxied (that is predicted using a probabilistic model based on some other data such as a person’s name), as well as alternatives when this is not feasible. However, we are aware that even if differences in predictions and ultimate outcomes exist for persons from different demographic groups, there are then separate questions around the causes of and any justifications for such differences. For this, it will be important to consider the broader context in which a model is being used and, where appropriate, any non-discriminatory business or other justifications for any measured differences.

Given the focus and aims of the work presented here readers should be aware that this note:

- constitutes research to spark debate and contribute to academic discussion, rather than any form of guidance or direction about what firms or practitioners should do.

- does not set out any particular expectations for how firms should approach managing AI risks (in all cases, firms will need to consider the risks relating to AI adoption in the context of their specific use cases and in light of applicable requirements))

- is not a comment or statement about the direction of the broader debates on what constitutes fairness or discrimination in the AI space.

- will not cover risks from language models (including Large Language Models such as ChatGPT and older models such as BERT) often stemming from biases in their underlying embeddings, which are covered in a separate Research Note Dwyer, Francis, and Tyagi (2024).

[pp. 6-7]

This note is primarily intended for those with some understanding of statistics or AI but is written in non-technical language. This Research Note should help signpost important considerations in the technical development of these models, as well as first-line mitigation strategies, that is those before a broader set of ethical, commercial, and legal considerations would need to be explored. Readers may also want to consider the RTA (2020) report into bias in algorithmic decision-making, as well as ICO (2023) guidance.

We identified the following key findings from our research:

1. Systematic differences in a supervised learning context in predictions or decisionmaking across demographic characteristics or characteristics of vulnerability can result from human inputs, historical biases in data, or choices in the modelling process itself.

#### Key points


[p. 7]

2. There are a variety of different metrics that can be used to measure these differences in supervised learning predictions, which reflect varying notions of what bias (and ultimately fairness) means. Based on existing literature, one useful notion of bias is conditional demographic disparity, which asks, for example, whether the same proportion of two groups of people get a loan, on the basis that they have suitable characteristics such as being employed.

3. If a demographic characteristic can either be collected or proxied, there are several feasible approaches for removing bias. These include methods for preprocessing data (including removing biased features or adjusting features to remove bias), adjusting modelling to choose a less biased alternative model, and post-processing (including flagging cases where the model makes biased or less confident predictions for human review).

4. Finally, in the circumstance that characteristics or life circumstances cannot be measured or proxied there are two alternatives: creating industry knowledge bases, and intuition-based consideration of whether variables or rules generated might cause biases.

### 2 What is bias and how does it come about?


#### What is bias?


##### The general idea of bias


[p. 8]

For the purpose of undertaking this literature review, we first wanted to consider what bias is, for which we have drawn on extensive reading of literatures on related concepts such as fairness and discrimination in machine learning, AI, and statistics. We did this in order to frame the rest of the review and to set broad parameters for the types of bias we wanted to consider. We set out in this section a concept of bias that underpins this piece, although this is a contested area of research, and other notions are required for example when using pricing or language models.

In this sub-section, we define bias qualitatively and in general, before proceeding in the next two sub-sections to explore how it arises, and how it can be measured.

In general, in the behavioural and decision theory literatures, a bias is generally understood as any systematic decision-making error. For the purposes of this review, we will focus on biases resulting from a predictive modelling process that occur based on some demographic characteristics or wider life or social circumstances of a person, such as characteristics of vulnerability.

The nature of the bias that may arise and the impact it could have on end users and consumers is likely to vary depending on the context in which a particular model is used, and the customers served. For example, more significant impacts could arise in contexts such as loan decisions.

We focus on bias in the form of unjustified differences in predictions or outcomes for groups of consumers with particular demographic characteristics or life circumstances.

In terms of the scope of the characteristics considered in this review, it could denote any characteristic of a person or group of people or any fact about their wider life circumstances. For illustrative purposes, we opt to discuss three sets of groupings in this review.

##### Protected Characteristics


[pp. 8-9]

The first grouping are the protected characteristics set out by the _Equality Act 2010_ :

- Age,

- Gender reassignment,

- Being married or in a civil partnership,

- Being pregnant or on maternity leave,

- Disability,

- Race including colour, nationality, ethnic or national origin,

- Religion or belief,

- Sex, and

- Sexual orientation.

The second grouping that one might consider under a bias lens could encompass the concept of vulnerability, as in the FCA’s Vulnerable Consumer Guidance (2021). The FCA’s general view is that vulnerability is a spectrum of risk, as depending on life circumstances any person can be vulnerable. However, when considering bias in this area, one might use what the FCA terms “characteristics of vulnerability” which are generally associated with four key drivers:

##### Vulnerability


[p. 9]

- Health – health conditions or illnesses that may make it difficult to undertake dayto-day tasks.

- Life events – such as bereavement, job loss, or relationship breakdown.

- Resilience – low ability to withstand financial or emotional shocks.

- Capability – low knowledge of financial matters or low confidence in managing money, literacy, numeracy, or digital skills.

Finally, there are wider demographic characteristics that may nonetheless be worth considering in the context of bias like region of the UK, occupation, or income level.

There are a number of overlaps and interactions between these three distinct categories of characteristics. For example, health conditions will be relevant both to the protected characteristic of disability as well as characteristics of vulnerability. There may also be correlations between the numbers of vulnerable persons within different demographic groups (i.e., those sharing particular protected or wider demographic characteristics). However, we thought setting these different groupings out would provide useful framing for our note.

##### Bias in an algorithmic (vs. human) context


[pp. 9-10]

Group bias is a property both of _predictive algorithms_ (of which we only address supervised machine learning examples here), that is rules for making statements about the likelihood of some future event, and _decisions_ about individuals, possibly made with the assistance of an algorithm. This is usually measured on average across the members of the different subgroups.

For example, in comparing white and non-white individuals, group bias in a _predictive algorithmic_ context would mean the differences by group membership in prediction, like the risk of defaulting on a loan. Those differences could refer to different levels of accuracy for different subgroups, or different predictions made about people with otherwise similar profiles, for example but for their race (see Verma and Rubin, 2018, or Section 2).

When human decision-makers become involved, it would mean the difference in _final decisions_ made. For instance, in the approval of a loan this could involve consideration of whether a human decision maker overrides algorithmic recommendations differently for white and non-white customers. Angelova, Dobbie, and Yang (2023) find in a baildecision context that algorithmic overrides increase the disparity between black and white defendants in release probabilities. Whilst, for the purposes of this review, we focused on model bias in a supervised machine learning context, it is important to note

that the biases that can be introduced through human input into decision-making can also be significant.

One critical point is that there may be observed baseline differences in outcomes between groups which do not by themselves suggest unfair or discriminatory outcomes once we account for other factors. For instance, if one group lives in predominantly rural areas and another in predominantly urban areas this may have justified implications for outcomes in the context of insurance pricing. Similarly, there may be either affordability or business reasons why, for instance, income level might be associated with different outcomes in relation to lending decisions, but it may be of interest to understand why these occur and if they are justified.

#### What contributes to model bias?


[p. 10]

In this section, we refer to supervised machine learning models and note that the situation would be somewhat distinct in an unsupervised (e.g., clustering) case.

In this review, we found in the literature documentation of how bias can be introduced into the predictive algorithms built using a supervised machine learning approach throughout the building process from problem framing to production i.e., building and employing the algorithm. These findings demonstrate how bias may arise at distinct stages of the modelling process and may therefore need to be measured at multiple stages, given changes over time. That can occur, as Ferrara (2024) points out because machine learning models can exhibit ‘Butterfly Effects’, where small changes to initial inputs cause large changes in model outputs due to shifts in market or consumer behaviour or model instability. Feast (2020) suggests that bias might be measured at:

- the time of data collection or model building

- after human intervention (as human overrides of model predictions could either reduce or increase bias)

- on an ongoing basis, as if new applicants are not similar to historical training data, then bias might change on this basis also.

Measuring bias at multiple stages might then, as Feast discusses, point to whether it can be mitigated, and whether there is a good justification for the bias that results.

The following section will discuss literature on how bias can be introduced into an algorithm during the problem-framing, data collection and algorithm-building steps.

##### Problem-framing


[pp. 10-11]

The first challenge of any algorithm’s creation is how to frame the problem that requires solving. This involves considering the problem, any available inputs, and the output. During this step, one could consider the bias arising from using particular features (also known as covariates or independent variables), as they could be associated with demographic characteristics or characteristics of vulnerability.

In the financial industry an example could be creating an algorithm to predict which cash machines can be removed. An input could be the amount of money that individuals withdraw from the machine where each transaction with a lower amount suggests the machine is more likely to be removed. This might negatively impact low-income areas,

potentially also correlating with demographic characteristics such as race, age or health, given disparities in income (ONS, 2023).

That is because, for example, lower-income individuals, old age pensioners, or disabled persons on benefits might only withdraw enough for each week or shop using cash to manage their budget. An alternative input could be the number of withdrawals or the number of individuals using the machine. This could allow a company to remove underused machines and not disproportionally affect lower-income, older, or disabled individuals. When framing the problem, a data practitioner must consider how different input sources could introduce bias into the algorithm.

Similarly, seemingly unrelated characteristics might be close proxies for demographic characteristics or characteristics of vulnerability, especially when sophisticated predictive algorithms such as supervised machine learning models are used. This should be thought about carefully. For example, Kusner et al. (2019) discuss the examples of living in a high-crime region or area with poor exam results which might correlate with socioeconomic status or race.

As part of the problem framing a data practitioner may also consider what supervised learning method or model would be most appropriate, given what target the modeller is trying to predict and the features they have available to them.

##### Data collection


[pp. 11-12]

After having framed the problem and chosen the data sources, the next step is data collection for algorithm training and testing. Algorithms are trained to find and replicate patterns in the dataset by looking at how different variables link to the outcome. Without intervention by modellers, biases in the dataset are likely to be reproduced by the algorithm. Practically, a dataset can exhibit two different biases: representation and past beliefs.

Firstly, if the data does not accurately represent the population covered in the problem this can lead to some groups being underrepresented or overrepresented, which is termed “representation bias” in the literature (see e.g. Shabhazi et al. 2023). Underrepresentation of a group can lead to large generalisations and inaccurate predictions leading to worse outcomes for some groups. For instance, there has been analysis of the issues with past data that some facial recognition algorithms rely upon (though it is worth noting that these rely on deep learning, rather than supervised machine learning). Buolamwini and Gebru (2018) found that of three facial recognition algorithms, the worst inaccurately recognised 0.8% of lighter-skinned males compared to almost 35% of women with darker skin. This inaccuracy in some groups is due to the underrepresentation of those with darker skin in the dataset compared to those with lighter skin.

For the finance industry, a hypothetical example of a representation problem could occur if spending data were used from an open-banking app with mainly male customers. If the algorithm generalised the spending of men across the entire population, it may be unlikely to be able to predict female spending patterns with the same accuracy. Data that does not accurately represent the population to whom the algorithm will be applied can lead to negative outcomes for some groups when used to make decisions about them. For instance, Blattner and Nelson (2021), find that credit scores are noisier estimates of

default risk for minority applicants as they are more likely to have shorter or no credit histories.

It could also happen due to selection problems of the type first explored, where for example in credit scoring only those who get credit form part of the training dataset. If certain groups of applicants get more expensive or no credit historically, then they may be denied credit or get more expensive credit in the future. This is exacerbated by the fact that past data represents the noisy judgments of human decision-makers, which may encodes attendant biases (Cowgill and Tucker, 2019).

[p. 12]

Secondly, a dataset can propagate existing social biases or biases in the data collection process itself. Examples of documented existing biases in financial services outside a UK context include female investors being given lower quality investment advice than males (Bucher-Koenen et al., 2021) and higher interest rates on mortgages for some ethnicities (Bayer, Ferreira, and Ross, 2014). Using the investment advice example, if a supervised machine learning model was trained on the types of advice that had been previously given to customers, biases might result even if the customer’s sex was not used in the model (a strategy Kusner et al. 2019 term “fairness through unawareness”).

More broadly, a hidden assumption that training on past data embodies is that the datagenerating process is invariant, that is it does not change over time. An example of a data collection bias might be that certain customers are more likely to give permission for their data to be retained, which might lead to a highly imbalanced dataset.

##### Algorithm training


[pp. 12-13]

Having framed the problem and collected the data for training the next step is to begin training the algorithm. The process of model training encompasses various stages, each with the potential to introduce or perpetuate bias, starting from pre-processing of data to the model's deployment.

Pre-processing techniques such as weighting and handling missing data (Zhang and Long 2023) are pivotal stages where biases can seep in. Of course, this is also part of generally good practice for model risk management, even outside AI assurance or AI debiasing procedures. In a supervised machine learning context, the weighting of each data input is done either manually or by using different searching algorithms. A higherweighted data point will have a greater impact on the algorithm output than a lowerweighted one. Usually, these weights are picked to maximise the accuracy of the model, but as Chouldechova (2017) showed in the context of recidivism in criminal justice, this can lead to biases along racial lines even when race is not explicitly considered.

Further along the model building pipeline, dimensionality reduction and feature selection can inadvertently remove important context that might be crucial for making fair or unbiased predictions. An example of this is Amazon’s roll out of same-day delivery across cities in America (Bloomberg, 2016), where ZIP codes were selected with high concentrations of Prime members for the same day delivery access. While ostensibly a neutral selection criterion, lower concentrations of Prime members in majority-Black neighbourhoods then meant that these were less likely to be chosen for same-day delivery access. This then meant for those customers in majority-black areas they were likely to be paying the same price as customers in majority-white areas but receiving a lower quality service. The choice of model is also critical; reusing old models can perpetuate existing biases, while more complex models, although potentially more

accurate, are harder to interpret, making it challenging to identify and address biases within them.

Lastly, model drift refers to changes in the data or context that a model is applied to over time. Without careful monitoring and updating, models can become biased as the world changes around them, underscoring the utility of continuous oversight and re-evaluation of model performance and fairness. For example, this can occur if there are what Ensign et al. (2018) term “feedback loops” when algorithms that learn from human biases then alter future human decisions made with the algorithms, in this case that certain groups of applicants do not get credit and therefore might continue to be missing from the data.

To recap, bias can be introduced into algorithms from sources throughout the modelbuilding process: from the way data is collected, generated, processed, weighted, or used.


---

[source overview](overview.md) | [next part](text-002.md)

[^original]: Financial Conduct Authority, "A Literature Review on Bias in Supervised Machine Learning" (2024-12-11). https://www.fca.org.uk/publication/research-notes/literature-review-bias-in-supervised-machine-learning.pdf
