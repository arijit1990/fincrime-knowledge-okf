---
type: Source Text
title: A Literature Review on Bias in Supervised Machine Learning - part 2 of 3 (pp. 13-25)
description: 'Verbatim extracted text, pp. 13-25: Research Note > 2 What is bias and how does it come about?; Research Note > 3 De-biasing algorithms where data on demographic characteristics or characteristics of vulnerability are available; Research Note > 4 Mitigating bias when data on demographic characteristics or characteristics of vulnerability cannot be collected or proxied; and 1 more sections'
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
part: 2
parts_total: 3
content_mode: full_text
generated:
  by: process:fincrime-kb-build
  at: '2026-11-17T02:21:50Z'
verified:
- by: process:kb-validate/verbatim-coverage
  at: '2026-11-17T02:21:50Z'
sources:
- id: original
  resource: https://www.fca.org.uk/publication/research-notes/literature-review-bias-in-supervised-machine-learning.pdf
  title: A Literature Review on Bias in Supervised Machine Learning
  author: org:fca
  last_modified: '2024-12-11T00:00:00Z'
---

# A Literature Review on Bias in Supervised Machine Learning

[previous part](text-001.md) | [source overview](overview.md) | [next part](text-003.md)

> Verbatim text extracted from the original (Financial Conduct Authority, 2024-12-11), part 2 of 3, pp. 13-25. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **academic finding**.[^original]

## Research Note


### 2 What is bias and how does it come about?


#### Bias metrics and what they measure


[pp. 13-14]

In this sub-section, we focus on measuring bias in a binary prediction context, for example whether a person will default on a loan or not, or whether they will make an insurance claim or not. Binary prediction is important because many financial decisions are binary, such as whether a person will buy a product or not, or whether they will fall behind on payments, or whether they will make an insurance claim. It is also the simplest outcome type to consider bias in, which is likely why it has garnered the most attention in the academic literature.

There are generalisations of the notions discussed here to look at continuous outcomes like claim or loan sizes, for example looking at differences in means, differences in quantiles (Liu et al., 2022), differences in entire distributions (Mary, Calauzenes, and Karoui, 2019), and finally a specific literature on different notions of what constitutes fair pricing (see e.g. in an ML context Cohen, Elmachtoub, and Lei, 2020, and the FCA’s publication Starks et al., 2018).

Further, for any chosen metric, Lum, Zhang, and Bower (2022) show that especially if some groups are very small, then the statistical estimate of group bias in a given dataset may be significantly different from the “true” bias. The authors provide a corrected variance estimator that allows for more rigorous quantification of the uncertainty around estimates of bias.

We concentrate on two metrics for bias in a supervised machine learning context here for illustration, but it is worth noting that there are substantially more, each with their own advocates. We take the example of a hypothetical loan provider who wants to model whether an applicant is likely to default or not, given information on their past credit history and then examine bias based on gender. Explanations here are based on this example and in words, for more mathematical details please see e.g., Castelnovo et al. (2022).

Our first metric is demographic parity (Barocas, Hardt and Narayanan, 2023), which involves enforcing equality of outcomes across groups. Here that means the same proportion of men and women will be predicted to not default on a loan by the predictive model, and therefore the same proportion qualify for a loan. This metric is simple and

intuitive, but it does not adjust for individual characteristics such as income or past credit history, and therefore may not be considering legitimate differences in circumstances.

[p. 14]

An alternative is conditional demographic parity, which produces a conditional quality of outcomes on relevant characteristics of people and will account for historical biases in the data. It was invented in Kamiran, Žliobaitė, and Calders (2013), and has been advocated for by Wachter, Mittelstadt, and Russell (2020). It means that the same proportion of male and female applicants qualify for loans given a set of characteristics, such as that they are employed, or have an income over £50,000, or have equal credit histories. It does adjust for individual characteristics and is outcomes focussed. However, there are always more possible variables to adjust for, and so this requires careful consideration of what features to “condition” on or put more simply what characteristics of a person are legitimate to term it a like-for-like comparison.

Conditional demographic parity treats any individual characteristics that it accounts for as having developed free of other forms of bias, or at least outside of the control of the modeller. That may not be a socially reasonable assumption, for instance women see poorer employment outcomes on average for a range of reasons (see e.g., in a UK context ONS 2018). However, wider structural inequalities or biases are outside the modeller’s control and are not taken into account for the purposes of this metric of bias provided they are justified to take into account.

Therefore, a possibility would be to causally model the relationship between the outcome, features, and the demographic characteristic. We would then consider what biases result as compared to a person who instead lived in the counterfactual universe where they were born as the opposite sex (Kusner et al. 2017). However, this is subject to two key problems.

- first, writing down such a causal model is likely infeasible for most relevant scenarios, especially as most human behaviours have a range of determinants, and their causes are not known sufficiently well.

- second, it in effect transfers social responsibility for issues entirely outside the person or firm control to the person or firm.

In general, if there is thought to be no selection bias or historical patterns of discrimination, then sufficiency or separation (see Glossary) could be considered as metrics for bias. However, conditional demographic disparity is likely preferrable given selection bias is present for many modelling contexts and because it adjusts for important characteristics to compare “like-for-like” persons without requiring complex or infeasible causal models to be constructed.

### 3 De-biasing algorithms where data on demographic characteristics or characteristics of vulnerability are available


#### What is de-biasing in a supervised machine learning context in the current academic literature?


[pp. 15-16]

When we refer to "de-biasing" methods from the academic literature, this term does not imply achieving a completely fair predictive algorithm resulting from a supervised machine learning modelling process without any kind of bias because that is generally impossible. Therefore, oversight and a human-in-the-loop are considered to be important checks on the bias of models. Following the work of Balayn & Gürses (2021), what we mean is that a method has been implemented to guarantee adequate "statistical parity" based on one or more bias measures outlined in Section 2. This involves ensuring that different demographic groups have approximately equal predictions, after any adjustments control for characteristics that can justifiably be taken into account.

It is important to emphasise at the outset that, at least in the current literature, there is no one-size-fits-all strategy to debiasing, and that any process could carefully think through why bias might be occurring and whether a particular strategy will therefore be likely to mitigate any sources of bias. Further, mitigating bias against one group may reduce the accuracy of the model, potentially reducing the overall benefits to society of having the model and/or leading to bias on other demographic characteristics or characteristics of vulnerability.

In this section, we review de-biasing strategies from the academic literature which rely on collecting or proxying data on demographic characteristics or characteristics of vulnerability alongside model training data. Most of these methods do not rely on the availability of data on demographic characteristics or characteristics of vulnerability or proxied data for new customers to which a model might be applied to generate new predictions. However, they do rely on data on demographic characteristics or characteristics of vulnerability (or proxies) in the training data.

To implement the methods of measuring bias, outlined in Section 2, and mitigating bias, outlined in this section, organisations need access to demographic data pertinent to the bias they are seeking to test. Debiasing methods require collection of demographic characteristic data on at least the sample used to train the model, and some require collection for all consumers.

However, organisations may face several practical, legal, and technical challenges in obtaining data of this nature, which is often sensitive. Driven by an increasing need for high-quality demographic data to assess biases, there is growing interest and research into ways of overcoming these challenges. We have considered in Section 4 some of the techniques that may be available where the relevant data cannot be obtained.

In the next section, we consider the case when such data or proxied data is not available.

#### De-biasing techniques


[p. 16]

Corrales-Barquero, Marín-Raventós, and Barrantes (2021) classify methods of de-biasing into three stages:

- pre-processing methods which de-bias the data directly,

- in-processing methods that attempt to de-bias model construction, and

- post-processing methods that mitigate bias after model building or during model deployment.

The authors note that there might be more than one demographic characteristic to account for, with many methods and metrics not accounting for all of these. A more complete list of techniques can be found in that paper or in Leslie et al. (2023), we concentrate here on a selection of the main types of techniques.

It is worth noting at the outset that these solutions are all partial and come with important limitations which we discuss here in some detail. However, in some circumstances they may represent better solutions to the problem of model bias than realistic alternatives, such as either not using predictive models or omitting using model features based on intuition.

##### Pre-processing


[pp. 16-17]

Pre-processing techniques seek to address issues around bias before a classifier is built using a supervised machine learning process. A first way this can occur is by focussing on individual features that may be associated with a demographic characteristic and therefore to bias against a particular group. In general, the techniques around individual features have significant limitations under most reasonable scenarios.

Individual features can be “suppressed” or more simply excluded from a predictive model construction if there is a strong association between that feature and a demographic characteristic (Kamiran and Calders, 2012). This is often ineffective as unless all potentially biased features are excluded—which may lead to a sharp loss in accuracy— bias may just transfer onto other included features.

Individual features can also be modified, for example through the Disparate Impact Remover of Feldman et al. (2015), who provide a method for shifting the distributions of features of different groups under a demographic characteristic like between different racial groups or income levels. This does have the advantage that it means important features can be retained, and the “unbiased portion” of them still contribute to the model. However, it has three key disadvantages:

- it is likely to impair the explainability of the subsequent model as explanation will be in terms of adjusted features.

- it is likely to be seen as procedurally unfair given it uses different inputs for different groups.

- unlike most de-biasing methods, it requires knowledge of the demographic characteristic in subsequent model deployment to continue to adjust features.

A second way is to reweight or resample the data to fix differences in how accurate predictions are made for minority groups (Kamiran and Calders, 2012). These techniques are broadly applicable and do not suffer from the issues around adjusting or removing individual features.

One simple weighting scheme is choosing weights to ensure that the training sample is representative of the population that the classifier applies to, for example for a general use product, this could be the population of British adults. This is likely to be effective if the problems stem from insufficient minority individuals in a training sample, for example if certain groups of applicants tended not to be successful or even apply for certain products. If certain groups of applicants had different paths to say become in arrears, then the overall model reflecting their experiences might be important. It is worth noting that this assumes that observed individuals are reasonably representative of any demographic characteristic groups they are a member of, for example that observed disabled adults in the data are representative of disabled adults in the population.

[p. 17]

Kamiran and Calders (2009) instead propose reweighting samples by taking any disadvantaged subgroup and up-weighting cases where those individuals are successful in achieving an outcome, while down-weighting successful cases from advantaged subgroups. One issue with any weighting scheme is that not all machine learning estimators are designed to work with weighted data. An alternative proposed by Kamiran and Calders, 2012 is to change the sampling of the data, for example to up-sample cases where applicants from disadvantaged subgroups are successful, that is by replicating those data points.

##### In-processing


In-processing techniques aim to mitigate biases during model training, with two principal techniques that are primarily used to achieve this: adversarial debiasing and regularisation. Adversarial debiasing stems from Zhang, Lemoine and Mitchell (2018). The idea is to imagine an adversary who is trying to learn the demographic characteristics or wider life circumstances of individuals from the predictions of your model. If the modelling process is set up so that the model tries to minimise the adversary’s ability to do this while maximising accuracy, then this should de-bias a model’s predictions. Berk et. al. (2017) demonstrate a general method for regularisation (a term which means altering an optimisation problem to add a penalty for complexity), which similarly attempts to trade-off bias and accuracy by adding a tuning parameter to the model building process.

Both these techniques tend to work by adjusting the relationships between features and the outcome that are learned from the data through imposing a form of penalty for producing biased models in addition to the usual task of maximising a chosen accuracy metric. They are likely to be effective or useable in a range of contexts, and the resulting model can be interpreted as it would be normally. This is unlike, say, the Disparate Impact Remover. That said, it might be useful to interpret a model constructed both with and without an in-processing technique to understand its effects – for example, by comparing importance plots or average local effects plots (see Molnar, 2022 especially Chapter 8).

##### Post-processing


[p. 18]

Post-processing techniques aim to mitigate bias after model construction. One method is similar to in-processing in spirit but adjusts the outputted probabilities after modelling has occurred. A method that performs this adjustment is Chzhen et al. (2020), who transform the output of a regression to satisfy demographic parity. They demonstrate that their method performs well in terms of reducing bias while minimising the loss of accuracy across distinct problem domains. In principle, this need not lead to a loss of interpretability if measures like feature importance are calculated on the transformed model.

A second method of post-processing is to highlight cases where the model is uncertain about the prediction it makes or bias risk is high such as in Kamiran, Karim, and Zhang’s (2012) method of reject option classification, which could then be used to either adjust predictions or to flag cases for human review. However, it is important to note that human review itself may need auditing, as otherwise prejudice or subconscious bias against groups may worsen the bias in the decision system.

#### Considerations


[pp. 18-19]

First, it can be the case that debiasing worsens predictive accuracy because it may remove genuinely predictive relationships between a feature and the outcome in the process of removing bias. Empirical evidence on this point is mixed. Kingsman (2021) finds that attempting to ensure no bias across multiple different demographic characteristics and ways of measuring bias tends to worsen accuracy. However, this relationship is not a simple, linear one and it does not occur in all the datasets they studied. Rodolfa, Lamba, and Ghani (2021) find negligible trade-offs from using bias mitigation methods across educational, criminal justice, and housing safety domains. Lee and Floridi (2021) find that for four of the five classes of machine learning models they studied, more complex models with generally higher accuracy rates in a U.S. context disadvantaged black mortgage borrowers compared to models with generally lower accuracy rates. In practice, this trade-off must be tested for a given model, given that evidence is ambiguous, often from the substantially different U.S. context, and dependent on modelling choices and chosen accuracy metrics.

A second important consideration is that reducing bias present on one demographic characteristic such as race can worsen bias on a different demographic characteristic such as sex. For example, if a loan approval model is adjusted to ensure equal approval rates across racial groups, the model might overcorrect by relying more heavily on other factors, like income or employment status, which may correlate with gender. This could lead to more men being approved for loans than women, thus increasing gender bias. It is important in the modelling process then to consider which demographic characteristics or characteristics of vulnerability are prioritised for mitigation efforts, based on the risk of bias arising based on those characteristics.

Unfortunately, most of the techniques we reviewed for mitigating bias in supervised machine learning models work based on a single characteristic, and some of them assume that characteristic is binary. Therefore, further academic research in this area would be welcome, as often more than one characteristic needs to be balanced against each other. One exception is Singh et. al (2021), who propose a generalisation of this

idea called DualFair to mitigate bias and handle considerations of how bias and accuracy can be in tension and a new metric called Alternative World Index (AWI) to measure it. DualFair works by subsetting a dataset into different combinations of demographic characteristics, and either oversampling and under sampling from each outcome within this subset to get a class-balanced dataset with no selection bias. Next, it uses situation testing, which will test all combinations of these protected attributes on the results from the ML models and will remove any value where the prediction in that data subset is different from the others’ subsets.

[p. 19]

Finally, there will also be privacy considerations to take into account when seeking to reduce bias in modelling. As mentioned, these techniques rely on having access to data on individuals’ demographic characteristics and wider life circumstances. Organisations would need to navigate data protection law requirements when collecting and processing personal data for this purpose. There is also the relatively theoretical risk of “privacy attacks” where someone’s race or sex is inferred from the predictions given by a biasmitigated model (see e.g., Chang and Shokri, 2021), but in practice this requires access to model predictions, which for privately held models then becomes more of a cybersecurity than data science concern.

In conclusion, there are a variety of techniques to debias supervised machine learning algorithms provided that per the previous section demographic characteristic data is available or can be accurately proxied. Some of the most promising techniques here are adversarial debiasing which try to make a demographic characteristic hard to predict using the output of the original model, and post-processing techniques which apply changes to predictions to ensure they are not biased after a model is initially developed. There are important considerations which model developers would need to consider around the effects of debiasing a model while trying to maintain accuracy, on how addressing bias on one characteristic may worsen bias on other demographic characteristics or characteristics of vulnerability, and on data privacy.

### 4 Mitigating bias when data on demographic characteristics or characteristics of vulnerability cannot be collected or proxied


[p. 20]

In this section, we review two imperfect substitutes suggested by Veale and Binns (2017) for measuring and mitigating bias that can be used even when data on demographic characteristics or characteristics of vulnerability cannot be collected or proxied for, notably exploratory bias analysis, and collaborative online platforms for sharing insights into fair algorithms.

They are imperfect because they involve judgments rather than direct measurement, and as should be clear from the discussion in Section 2, bias can result from quite nuanced, seemingly neutral technical decisions. At their heart, these strategies involve trying to either remove features or modify algorithms to remove relationships that are suspected to cause bias. Where they vary is in terms of how insights or tentative hypotheses as to how to do this are shared.

The reason for the reliance on a single paper here is that this scenario, despite how common it is likely to be due to trust and other considerations, is not to our knowledge analysed elsewhere in academic work on AI. That is because any solutions here would need to be indirect, and it is difficult to measure how effective they would be. As will be highlighted in the conclusion, more concrete proposals for bias-mitigation strategies in the absence of data on demographic characteristics or characteristics of vulnerability are therefore crucial.

However, Veale and Binns’ proposals are certainly more widely applicable than what Kusner et al. (2017) term “fairness through unawareness”, that is the claim that an algorithm is unbiased simply because it does not include a demographic characteristic as a predictor. That is unlikely to be a tenable strategy to prevent bias, because it would require that an algorithm designer (who may have their own cognitive biases in thinking about the modelling process) is strongly convinced that none of the issues described in Section 2 apply.

#### Collaborative online platforms


[pp. 20-21]

Veale and Binns (2017) call for the establishment of online fora to share experiential knowledge about the construction of more ethical algorithmic systems, especially given the likely relative comfort of data scientists in using collaborative tools like StackExchange and wikis, and more broadly research summarisation initiatives like The Cochrane Collaboration in health. The establishment of knowledge sharing fora seems especially important given the ever-expanding and often highly technical literature on bias, and related questions on accuracy, explainability, and transparency. The depth and difficulty of this literature is likely to cause barriers to entry to new data scientists seeking to understand and implement solutions to these issues.

Information this could contain includes research on human behaviour in a given field (such as retail insurance, payments, or credit), common features and associations with demographic characteristics or characteristics of vulnerability, and the effect of model complexity on bias.

##### Summarising contextual research


[p. 21]

A knowledge sharing forum could summarise research about how human behaviour in a given field is likely to determine outcomes, and how these vary across demographic characteristics or characteristics of vulnerability. For example, this could include information on how disability status might have affected financial product choice, or how historic housing discrimination might change patterns of where non-white people live.

Summarising social scientific research here would need to take into account research gaps, potential contradictions between different studies, the issues with failed replications in research findings (for a lucid summary within psychology, see Korbmacher et. al., 2023), and issues with peer review processes.

However, there is a significant volume of this kind of research, much of it in the only partially analogous US context. This would require a significant amount of human effort to summarise, although appropriate use of technologies such as Large Language Models (LLMs) may to a degree mitigate this problem.

##### Common features and their associations with demographic characteristics or characteristics of vulnerability


[pp. 21-22]

Further, a knowledge sharing forum could include common features in each domain (for example, location for motor insurance or payment history variables for credit) and how they might influence the bias of models. This could occur using publicly available aggregated datasets such as survey data, where available, or where a third-party has published their modelling results on a privately held dataset. The list of features could be used to consider omitting some features from a model that are strongly associated with a demographic characteristic, or their replacement by potentially less strongly associated alternatives. That would be particularly true if those features were not key to making business or affordability decisions but had been included merely as extra training data without a clear justification. The optimal approach here is likely to be demonstrating which variables influence the bias of a predictive model the most, for instance what variables most influence the racial bias of a credit risk model. Recent innovations such as feature influence functions (Ghosh, Basu, and Meel, 2023) allow quantification of the marginal influence of features on model bias.

However, this may not be feasible for two reasons. First, the findings on the bias attributable to any specific feature within a given model will depend heavily on the specific customer base and to the features chosen, and so therefore may not generalise well. Second, there may not be data available which contains all of the potentially biased features, the demographic characteristics or characteristics of vulnerability, and the target variable for prediction. More commonly, publicly available data will only contain information on potentially biased features and demographic characteristics or characteristics of vulnerability. For instance, the published aggregated data on the UK census only has information on local-area ethnicity statistics (ONS, 2021b) which could be associated with apparently unrelated information like local-area deprivation published

in the IMD (CDRC, 2024). But neither the census nor the IMD have credit information available. Further, as noted previously historical datasets may have been biased in terms of their data collection practices.

Therefore, an alternative would be to look at the association between a feature and a demographic characteristic, which might be more commonly available. However, in the context of this note, any feature which causes bias must be associated with a demographic characteristic or characteristic of vulnerability, but this is not sufficient for contributing to bias as it must also be included in and important to a model’s predictions. Further, another limitation is that associations which exist in aggregated data (for example, between local-area ethnicity and local-area vehicle accidents) may not exist in individual data or in other levels of aggregation due to Simpson’s Paradox.

##### Model complexity


[p. 22]

Finally, these databases could include information on the impact of model complexity, like the choice of gradient-boosted regression trees instead of logistic regressions, on bias issues in related applications. This might subsequently affect the best model from a de-biasing perspective. As noted in the introduction, in a credit scoring context, recent empirical research has found more complex models tend to disadvantage minority borrowers in a US context (Fuster et al., 2022). That said, reducing model complexity may not be the best way to achieve debiasing. For instance, Blattner, Nelson, and Spiess (2023), find that targeting specific variables that cause misalignment between accuracy and bias is more effective than only using simpler models.

#### Exploratory bias analysis


[pp. 22-23]

What Veale and Binns (2017) term “exploratory fairness analysis” (in our language, exploratory bias analysis) involves considering how a model was made and its outputs and thinking through whether that process might induce forms of bias. Necessarily, this involves an exercise combining statistics and intuitive judgment, and is not a full replacement for other forms of analysis. However, exploratory bias analysis may be the only option if demographic characteristics or characteristics of vulnerability can be collected for no published datasets in each market. This area is not well established in the literature, but the authors provide two possible examples.

First, clustering individuals together and investigating the bias according to those cluster assignments. Based on other information, it might be possible to roughly proxy for demographic characteristics or characteristics of vulnerability based on other variables. This could give an indication of potential bias issues, but this kind of analysis seems fraught with the potential for inaccurate guesswork, and there has been no empirical validation of whether it does remove bias.

Second, creating interpretable models and thinking through which decision rules might be likely to cause bias, based on research about the relationship between different variables and demographic characteristics or characteristics of vulnerability. This could potentially be more promising, as engaging with the logic of the model is likely to be important for model assurance, and there might be more possibility of spotting obvious cases of rules that cause potential biases.

Therefore, while the non-availability of individual level data containing the model’s features, target/outcome variable, and the demographic characteristic (or an accurate proxy) does impair bias mitigation there are partial alternatives around either establishing knowledge fora which may be sector-specific on debiasing and exploratory bias analysis.

### 5 Conclusion


[pp. 24-25]

We have aimed to provide a literature review on AI bias in the context of supervised machine learning. In this review, as a reminder, bias means unjustified differences by demographic characteristics or characteristics of vulnerability in predictions and subsequently in decisions made in either an automated or algorithm-assisted way. The literature shows that this can result from a variety of sources, notably human inputs, data collection practices, or modelling choices. It is important to note that so-called “raw” differences in outcomes for different groups, that is those without adjusting for appropriately justified risk or economic characteristics, may give a misleading impression of bias.

The literature then suggests these questions to consider in supervised machine learning model construction and deployment for bias measurement and mitigation:

- _What demographic characteristics or characteristics of vulnerability could be studied?_ This could be based on considering intuitively and possibly with regard to academic research what biases might exist in the model development pipeline.

- - _What metric/s could be used to measure any bias?_ Based on the current existing literature, one useful metric highlighted in the literature is conditional demographic parity/disparity, because it accounts for other differences between people and focusses on final outcomes. However, choice of metrics requires consideration of context, and this area is ever evolving.

- _Is it feasible and appropriate to collect or proxy data on demographic characteristics or characteristics of vulnerability on an individual level, either for some or all our customers?_ Here, there are a range of considerations including data protection law, the accuracy of the data collected, and whether direct or proxy (sex and race only) are the appropriate alternatives if data is collected.

- - _Is it feasible to mitigate biases and if so, how?_ There are several methods in the pre-, mid-, and post-processing stages to mitigate bias. The literature suggests modellers could consider what is most feasible, and trade-offs with the explainability of any resulting model.

- _If demographic characteristics or characteristics of vulnerability cannot be measured or proxied, are there any realistic alternatives?_ We outline two possibilities: creating industry-wide knowledge bases, and exploratory bias analysis. These have the drawback that they do not provide the same guarantees as mitigation techniques where measuring or proxying the actual demographic characteristics or characteristics of vulnerability of consumers is possible, but they do provide some possibilities of addressing bias issues.

For researchers including academics, some important considerations are likely to be:

1. Do the strategies that Veale and Binns (2017) propose for debiasing in the absence of data on demographic characteristics or characteristics of vulnerability work (or other such plausible strategies)? One possible strategy for testing this would be first to construct a suitable knowledge forum, and then conduct a

randomised controlled trial on the levels of bias from models built by developers with and without access to that knowledge forum.

2. Information on practical case studies of debiasing models and decision processes, especially beyond the well-studied case of credit scoring to include cases like general insurance and retail investments.


---

[previous part](text-001.md) | [source overview](overview.md) | [next part](text-003.md)

[^original]: Financial Conduct Authority, "A Literature Review on Bias in Supervised Machine Learning" (2024-12-11). https://www.fca.org.uk/publication/research-notes/literature-review-bias-in-supervised-machine-learning.pdf
