---
type: Source Text
title: Machine learning in UK financial services - part 3 of 5 (pp. 16-27)
description: 'Verbatim extracted text, pp. 16-27: 4 Firms’ perception of benefits, risks and constraints > 4.1 Respondents already see benefits from machine learning and expect these to increase; 4 Firms’ perception of benefits, risks and constraints > 4.2 Firms recognise model validation and governance need to keep pace with machine learning developments; 4 Firms’ perception of benefits, risks and constraints > 4.3 Constraints to deployment of machine learning are mostly internal to firms; and 8 more sections'
resource: https://www.fca.org.uk/publication/research/research-note-on-machine-learning-in-uk-financial-services.pdf
tags:
- empirical_observation
- explainability
- model_validation
- responsible_ai
- statistical_report
- uk
status: stable
source_id: fca-machine-learning-in-uk-financial-services
issuer: fca
issuer_name: Financial Conduct Authority
jurisdictions:
- UK
tier: 1
instrument_type: statistical_report
normative_force: empirical_observation
publication_date: 2019-10
legal_status: current
part: 3
parts_total: 5
content_mode: full_text
generated:
  by: process:fincrime-kb-build
  at: '2026-11-22T04:56:05Z'
verified:
- by: process:kb-validate/verbatim-coverage
  at: '2026-11-22T04:56:05Z'
sources:
- id: original
  resource: https://www.fca.org.uk/publication/research/research-note-on-machine-learning-in-uk-financial-services.pdf
  title: Machine learning in UK financial services
  author: org:fca
---

# Machine learning in UK financial services

[previous part](text-002.md) | [source overview](overview.md) | [next part](text-004.md)

> Verbatim text extracted from the original (Financial Conduct Authority, 2019-10), part 3 of 5, pp. 16-27. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **empirical observation**.[^original]

## 4 Firms’ perception of benefits, risks and constraints


### 4.1 Respondents already see benefits from machine learning and expect these to increase


[p. 16]

Respondents in all sectors think ML already benefits their business. Furthermore, and in line with firms’ expectation that the number of ML applications they use will grow, respondents estimate the benefits will increase significantly over the next three years (Chart 8). The survey asked participating firms to score some of the current benefits of using ML applications, from small benefit to large benefit.(21)

Chart 8 The highest perceived benefits are in fraud detection and anti-money laundering, followed by operational efficiency gains and new analytical insights

Current benefitExpected benefit (in three years)Large benefitImproved Increasedcombatting of fraud operationaland anti-money efficiencylaunderingNew typesof productMedium benefit New offeringsanalyticalBetter Improved insightspersonlisation compliancefor customersSmall benefit

Firms currently consider improved AML, fraud detection and overall efficiency gains (with the associated cost savings) as the biggest and most immediate benefits of using ML. There is a correlation between these benefits and the high number of ML applications in AML and fraud detection (Chart 4). Moreover, some firms mention they use ML in business areas where they identify clear efficiency gains and cost savings because they can persuasively demonstrate the benefits relative to traditional techniques. However, firms expect that increased benefits will also come from better personalisation of products for customers, new analytical insights and improved services over the next three years, all of which they consider could be revenue-generating (Chart 8).

### 4.2 Firms recognise model validation and governance need to keep pace with machine learning developments


[pp. 16-17]

Respondents recognise a range of risks that might arise from the application of ML in financial services. The survey responses suggest that ML applications can increase the technical complexity of models, and thus risk management and controls processes will need to keep pace. Firms do not think the use of ML necessarily generates new risks. Rather, they consider it as a potential amplifier of existing risks.

(21) Small benefit was allocated a score of 1, medium benefit was 2 and large benefit was 3.

Respondents explained that risks could be caused by a lack of ML model explainability meaning that the inner working of a model cannot always be easily understood and summarised. This forms part of more general questions around validating the design and performance of ML models. Another concern raised by firms is that models may perform poorly when applied to a situation that they have not encountered before or where human experience, institutional knowledge and judgement is required.

Firms also mention potential risks associated with data quality issues (including biased data). As firms note, these risks can have a negative impact on consumers’ ability to use products and services, or even engage with firms. This can, in turn, damage the firm’s reputation and lead to operational costs, service breakdowns and losses.

Overall, respondents think the top five risks that might occur because of ML applications relate to: lack of explainability; biases in data and algorithms; poor performance for clients/customers and associated reputational damage; inadequate controls, validation or governance; and inaccurate predictions resulting in poor decisions. In Chart 9 we summarise these into three overall categories: model performance, staff and governance, and data quality.

Chart 9 Firms consider issues related to model performance the biggest amplifiers of existing risks

Number of times raised140120100806040200Model performance Staff and governance Data quality

Firms highlight that there are a number of ways these risks could be managed, including through sound model validation and implementing safeguards. For example, certain methods can help mitigate risks when ML models do not work as intended, whilst others help identify potential errors and risks during the development phase. These are summarised in Figure 1 and explained in detail in the following chapter.

Figure 1 Examples of risks and possible ways to address these

[pp. 17-18]

Model validation Staff and governance Data quality'Black box' ML models are Staff may be insufficiently Poor quality data, limitedharder to explain and trained to understand and training data or biasesExample make decisions outside address risks related to may produce unintendedtheir original parameters ML models and negative resultsEvolve model validation Ensure employees have Apply data qualityPossible ways to approaches — the right skill sets — validation framework —address the risksee section 5.4 see section 3.2 see section 5.2 and 5.4Safeguards Alert systems, ‘guardrails’, human-in-the-loop before execution, kill switches and back-up systems— see section 5.5

The survey also included a question on firms’ perception of potential ethical issues arising from the deployment of ML applications (Chart 10).

Firms interpreted this question in different ways. Some respondents understood this question to be about individual ethical issues, while others instead focused on how the firm is dealing with the potential ethical implication of the application of ML in financial services. The emerging picture represents again a wide range of opinions about how risk and harm might derive from firms applying ML.

Chart 10 Firms’ perception of possible ethical implications arising from machine learning deployment(a)

ML ethics aligned with firm conductand technology use rulesML and data specific policy establishedML ethics aligned with firm data ethics rulesBiasDon't know/NANo ethical issuesPotential generic ML specific ethicalissues and rulesModel accuracy0 5 10 15 20 25 30 35Per cent of firms that responded(a) This chart does not include all responses. It only shows the survey responses for firms using ML.

### 4.3 Constraints to deployment of machine learning are mostly internal to firms


[pp. 18-19]

Firms were asked to rank potential constraints that slow or stop them from deploying ML (Chart 11). The responses suggest the largest constraints are internal to firms. Aside from strategic decisions, namely ML is not a top priority, the three most cited are: legacy systems that are not conducive to ML, lack of access to sufficient data and the difficulty of integrating ML into existing business processes.

Chart 11 Legacy systems are the largest constraint to machine learning deployment(a)

Legacy systemsInsufficient dataML not top priorityDifficulty of integrating ML into business processesInstitutional appetiteData privacy regulationLack of data standardsLack of explainabilityPRA/FCA regulationsInsufficient talentInternal data governance processesPoor data qualityOther regulations (not PRA/FCA)Small Medium Largeconstraints constraints constraints(a) Small constraint was allocated a score of 1, medium was 2 and large was 3.

However, it is important to note that, overall, respondents do not perceive there to be major constraints to ML deployment. The highest scoring constraint has been ranked only slightly above medium. This suggests firms do not consider the constraints, for example associated with older IT systems, to be insurmountable.

The ranking of constrains differs by sector, as shown in Chart 12.(22) Legacy systems are viewed by firms in all sectors as a major constraint to the deployment of ML applications, especially so in banking and insurance. This might be due to the sample being skewed towards larger and more established firms, which often cite legacy systems as a key barrier to innovation. Conversely, newer firms tend to have more agile IT architecture, which means they can to use ML applications more easily. Respondents indicate the difficulty of integrating ML into existing business processes as constraints of medium severity. Insurance firms and investment and capital market firms note the lack of data standards as a constraint.

Chart 12 Firms report constraints across a number of issues, but none are perceived as big

Banking Legacy systemsInsurance Other regulationsInvestment and (not PRA/FCA) ML not top prioritycapital marketsNon-bank lendingPayments, FMIand otherPRA/FCAregulations Insufficient dataLargeconstraintMediumconstraintPoor data Small Difficulty of integrating MLquality constraint into business processesInternal data Lack of datagovernance processes standardsInsufficient talent Institutional appetiteData privacy Lack ofregulation explainability

### 4.4 Regulation is not seen as an unjustified barrier


[pp. 19-20]

The majority of respondents (75%) do not consider PRA/FCA regulations to be an unjustified barrier when deploying ML. As shown in Chart 11 and Chart 12, firms’ stated that regulation is only a small barrier. It is also important to note that well-judged regulation is intended — by design — to be a barrier to certain practices in order to maintain financial stability or protect consumers. Therefore, this finding could indicate that in future regulation may need to be updated or adjusted to account for developments in ML.

Of the respondents that do consider PRA/FCA regulations to be a constraint, the most common issues cited are around model risk management and the need to adapt processes and systems to cover ML-based models. Some firms note the challenges of meeting regulatory requirements to explain decision making when using so-called ‘black box’ ML models (Chart 13)(23) . Also, some firms mention a lack of clarity and uncertainty around how existing regulations apply to ML, but did not further specify which regulations in particular.

Some firms stated that more clarity around ML deployment could serve as an enabler. Additional guidance could potentially help firms design controls, model risk management frameworks and policies for ML applications, as well as understand regulatory expectations for specific use cases.

> (22) Small constraint was allocated a score of 1, medium constraint was 2 and large constraint was 3. inance: an application to default risk analysis’,

> (23) Bracke, P, Datta, A, Jung, C and Sen, S (2019), ‘Machine learning explainability in finance: an application to default risk analysis’, _Bank of England Staff Working Paper No. 816_ .

Chart 13 Firms identify model risk management as the one where regulatory constraints are most significant

Model risk managementGeneral uncertaintyExplainability/accountabilityCustomer protection/communicationMiFID II/Market abuse regulation0 10 20 30 40 50Per cent of firms that gave a specific answer to this question

## 5 How machine learning works


### 5.1 Machine learning applications consist of a pipeline of processes


[p. 21]

ML applications often consist of multi-step processes in which a number of distinct computational steps feed into each other(24) (Figure 2). The different stages of the ML pipeline are:

- Data acquisition and ingestion (section 5.2);

- Feature selection and engineering: Choosing the most relevant variables and creating derived ones (including for example through dimensionality reduction) (section 5.2);

- Model engineering and performance metrics (section 5.3): Model selection, optimisation of model parameters and model analysis (evaluation of model performance);

- Model validation (section 5.4): Testing if the model works as expected, which includes among other things the interpretation of how the model works;

- Deployment and safeguards (section 5.6): Implementing the model in the business and setting up safeguards to manage potential risks.

Figure 2 The machine learning pipeline

Eg creatingSection 5.2 summary variablesFeature engineeringSemi-structured &unstructured dataImplementing the modelTesting if the model works as expected in the businessData processingStructuredfinancial data Section 5.2 Section 5.4Data accquisition Eg splitting training Validation Deploymentdata and test dataSection 5.6Third party Safeguardsprovider data Section 5.3Establishing mechanisms and controlsModel engineering to manage risks, in case the model doesDetermining which model is most not work as intendedappropriate for the task (eg neuralnetworks or random forests).Often a back and forth with featureengineering process.Performance metrics

### 5.2 Data acquisition and feature engineering are evolving with the advent of machine learning


#### Different types of data


[pp. 21-22]

ML models learn from data of which there are three main types: (i) structured; (ii) semi-structured and (iii) unstructured.(25) Figure 3 summarises the different features of these types of data.

In the case of structured data, each piece of information has a relatively narrowly defined meaning. For example, this could be data in standard relational databases and spreadsheets, such as a person’s account balance.

> (25) www.bigdataframework.org/data-types-structured-vs-unstructured-data/.

(24) www.gartner.com/binaries/content/assets/events/keywords/catalyst/catus8/preparing_and_architecting_for_machine_learning.pdf.

Figure 3 Firms make use of three types of data

|Data type|Description|Example|
|---|---|---|
|Structured data|Highly organisedi•|Standard financial database|
||Data objects have fixed meaningEg Relational databases or dataorganised in tabular format••|FirstnameSecondnameAgeAccountbalance|
|||AB57334|
|||XY285,536|
|Semi-structured data|Less organised than structureddata, some hierarchy (tags,structure) presentSome data objects without fixedmeaningEg HTML, JSON, XML•••|WebsitePage TitleYour text / button here”Your Text Here|
|Unstructured data|Least organisedInformation that does not followa pre-existing data modelRequires analytical techniques totransform it into meaningfulinformation•••|Images or text|

[p. 22]

Semi-structured data are less pre-organised. For instance, the code behind a website structures contents into certain types of information (eg the sites’ colour scheme or heading) but leaves room for less clearly pre-defined information.(26) Unstructured data has the fewest pre-defined fields. For instance, pixels in an image do not have a pre-defined meaning. It has to be inferred after the data is collected. It is this aspect that makes unstructured data harder to manage and analyse, requiring ML algorithms to extract (structured) meaning from the (unstructured) source.(27) This also makes data validation — making sure the data is accurate and reliable — more complex, as it may be ambiguous what the ‘right’ interpretation of the data is.

According the survey responses, structured data is used in more than 80% of ML use cases (Chart 14). This is unsurprising given most financial data is structured, as historically other types of data have not been collected and it was difficult to process with traditional linear models, frequently used in finance.(28) However, firms also use semi-structured or unstructured data in more than two thirds of cases, often in conjunction with structured data.

Chart 14 Structured data sources are still most popular, but firms are increasingly using novel data sources(a)(b)

Data usedStructuredUnstructuredSemi-structured0 20 40 60 80 100Per cent of cases(a) Firms often use more than one type of data at a time which is why the percentages add to more than 100.(b) The underlying data is based on the use cases provided by survey respondents.

> (26) www.datamation.com/big-data/semi-structured-data.html.

> (27) www.mckinsey.com/~/media/McKinsey/Business%20Functions/McKinsey%20Analytics/Our%20Insights/The%20age%20of%20analytics%20 Competing%20in%20a%20data%20driven%20world/MGI-The-Age-of-Analytics-Full-report.ashx.

(28) eprints.lse.ac.uk/63017/1/Kallinikos_New%20Games%20New%20Rules.pdf.

[p. 23]

Unlike more traditional models, ML is capable of processing semi-structured and unstructured data. Hence, firms use ML to transform text and image data into interpretable information. This also means that previously less used sources are now being analysed for important and potentially profitable uses. The increasing use of unstructured and semi-structured data also raises new questions for firms, consumers and regulators alike.(29) For instance, it increases the importance of data validation, both before and after deploying ML applications live in the market (Chart 16). And raises questions around ethics, fair use and privacy.

#### Feature engineering


In several use cases, survey respondents use thousands of variables in their ML models. However, these variables are often part of the pre-processing phase, which includes standard data cleaning techniques (like dealing with outliers) as well as ‘funnelling’ numerous different variables into composite ones. Importantly, ML algorithms are used to perform this task, including dimensionality reduction methods and clustering methods, which we cover in section 5.3.

Model engineering includes the selection of the most appropriate algorithm and training of the model, all of which is an iterative process (see Box 4 for an explanation of different ML methods). For instance, in some contexts — especially those where the amount of available data is limited — simple linear regression techniques may be most effective. In other contexts — for instance those where a large amount of complex, unstructured data are available — neural networks may be most effective.(30)

### 5.3 Model engineering and performance evaluation decide which models are deployed


#### Types of machine learning algorithms


According to firms’ responses, the ML methods most often used are on the more complex end of the current spectrum.(31) The most common ML methods are tree-based models; natural language processing approaches and neural networks (Chart 15). Models in the ‘other’ category included Bayesian approaches or image recognition.

Chart 15 Tree-based methods are the most popular techniques reported by firms(a)(b)

Methods usedTree-based modelsNatural language processingOtherNeural networksData clusteringDimensionality reduction techniquesPenalised regressionSupport vector machinesReinforcement learning0 10 20 30 40 50 60Per cent of cases

(a) Firms often use more than one method at a time which is why the percentages add to more than 100.

(b) The underlying data is based on the use cases provided by survey respondents.

> (29) www.fsb.org/wp-content/uploads/P011117.pdf.

(30) www.imf.org/en/Publications/WP/Issues/2019/05/17/FinTech-in-Financial-Inclusion-Machine-Learning-Applications-in-Assessing-Credit-Risk-46883. (31) www.d2l.ai/chapter_multilayer-perceptrons/underfit-overfit.html#model-complexity.

### Machine learning methods(1)


[p. 24]

Penalised regression methods are standard regression methods, in which an algorithm picks the variables that are contained in the model. This is usually done by dropping variables that are not needed for prediction. These models are at the least complex and most interpretable end of the spectrum.

Tree-based models consist of a multitude of (often large) decision trees whose individual predictions are averaged. It works for both categorical and continuous input and output variables. Unlike linear models, tree-based models can map non-linear relationships.

Neural networks are algorithms modelled loosely on aspects of the brain’s neurons, designed to recognise patterns and make predictions. Modern neural networks often involve estimating a large number of weights, which increase in number as more ‘layers’ are introduced.

Natural language processing involves the application of algorithms — often neural networks — to identify and extract the natural language rules such that unstructured language data is converted into a form that computers can understand.

Dimensionality reduction techniques reduce the number of variables under consideration by obtaining a set of principal variables. Approaches can be divided into feature selection and feature extraction.

Support vector machines (SVM) are supervised learning models that analyse data used for classification and (continuous) regression analysis. Given a set of training examples, each marked as belonging to two categories, a SVM training algorithm builds a model that assigns new examples to one category or the other, making it a non-probabilistic binary linear classifier.

Reinforcement learning methods are concerned with how virtual agents choose their actions in order to maximise a reward function as defined by a human. These methods do not require labelled input/output pairs and sub-optimal actions need not be explicitly corrected. Instead the focus is finding a balance between exploration (of uncharted territory) and exploitation (of current knowledge).

- (1) James _et al_ (2017), ‘An introduction to statistical learning’. Goodfellow, I, Bengio, Y, and Courville, A (2016), ‘Deep learning’, MIT Press. Abu-Mostafa, Y, Magdon-Ismail, M, and Lin, H-T (2012) ‘Learning from data: a short course’.

Firms often use tree-based approaches, such as ‘random forests’. These consist of a multitude of (often large) decision trees whose individual predictions are averaged. These methods have been shown to be relatively successful for prediction in traditional financial data analysis contexts (such as price forecasting).(32) Natural language processing models are able to analyse unstructured text data, which lends itself well to customer service and insurance claims management use cases(33) (see the case studies in the Appendix for more information). Neural networks are used, among other things, to make forecasts based on historical information and find complex relations between variables. Most respondent firms’ applications use, on average, a combination of three ML methods. In one use case, a firm uses eight separate ML techniques in a single application.

[pp. 24-25]

(32) www.researchgate.net/publication/333409685_Stock_Market_Analysis_A_Review_and_Taxonomy_of_Prediction_Techniques. (33) www2.deloitte.com/us/en/insights/industry/financial-services/artificial-intelligence-ai-financial-services-frontrunners.html.

ML methods are more difficult to interpret than traditional linear regression models. The reason is that many ML models are ‘non-parametric’(34) , which makes them more difficult to explain — essentially more complex. As highlighted in section 4.2, firms think that this increased complexity makes model validation harder, which can translate into a potential risk. Validation methods, highlighted below, can address this, but new methods will likely be required, as ML techniques develop.

#### Performance metrics have multiple purposes


[p. 25]

Performance metrics serve at least three purposes in the ML pipeline:

- They are used to pick the best model, which can be either a human led or automated process.

- These metrics are key for understanding how well the model is likely going to perform once deployed.

- They can be used to track the performance of the model over time. Checking the performance over time can be important for detecting structural changes that make the model less accurate.

At the core of the ML pipeline is making sure that the application works as intended in practice. This is the issue of software validation. In Table 3, we use the aggregated survey responses to explain how firms do this in practice, with their own ML applications. Any of these methods might be used in the pre-deployment phase (where the application is being tested) or post-deployment (where the application is live in the market), as a way to continuously assess if the model works as intended.

### 5.4 Model validation is key to ensuring machine learning models work as intended


Table 3 Firms use a variety of model validation techniques to assess machine learning model robustness

|Validation method|Description|
|---|---|
|Outcome monitoringagainst a benchmark|Decisions or actions associated with the ML system are monitored using one or multiple metrics. Performance isassessed against a certain benchmark value of those metrics.|
|Outcome monitoringagainst non-ML model/A-B testing|Decisions or actions associated with the ML system are monitored using one or multiple metrics. Performance isassessed by comparing it to the performance of a separate, non-ML model. The same approach is used in A-Btesting (also known as split testing).|
|‘Black box’ testing|Input-output testing without reference to the internal structure of the ML application. The developer ‘experiments’with the model, feeding it different data inputs to better understand how the model makes its predictions.|
|Explainability tools|Tools aimed at explaining the inner workings of the ML model (going beyond input-output testing).|
|Validation ofengineered features|Engineered features used in the ML application are scrutinised, including potential impacts on model performance.|
|Data quality validation|One or more techniques are used to ensure potential issues with data (such as class imbalances, missingor erroneous data) are understood and considered in the model development and deployment process.Examples of these include data certification, source-to-source verification or data issues tracking.|

In Chart 16, we summarise which ML model validation techniques and frameworks are most frequently used (as described in Table 3). The most common method is outcome-focussed monitoring and testing against benchmarks, both before and after deployment. This enables firms to scrutinise how ML models would have performed historically in terms of profitability, customer satisfaction or pricing, for example. Data quality validation — including detecting errors, biases and risks in the data — is the next most frequently used method. Overall, these methods were used by two thirds of respondents. In about half the cases outcomes were benchmarked against a non-ML model. Explainability techniques(35) were used in less than half of the cases. However, many firms emphasise that validation frameworks still need to evolve to address challenges associated with the nature, scale and complexity of ML applications. Therefore the use of some validation techniques may increase in the future.

> (34) In non-parametric models, the data is not required to fit a normal distribution and does not rely on numbers, but rather on a ranking or order of sorts. wwwf.imperial.ac.uk/~nsjones/TalkSlides/GhahramaniSlides.pdf. inance: an application to default risk analysis’,

[pp. 25-26]

> (35) Bracke, P, Datta, A, Jung, C and Sen, S (2019), ‘Machine learning explainability in finance: an application to default risk analysis’, _Bank of England Staff Working Paper No. 816._ Joseph, A (2019), ‘Shapley regressions: a framework for statistical inference on machine learning models’, _Bank of England Staff Working Paper No. 784_ .

Validation method usedPre: Outcome vs benchmarkPost: Outcome vs benchmarkPre: Data quality validationPost: Data quality validationPre: Validation of engineered featuresPre: Outcome vs non-MLPost: Outcome vs non-MLPre: ExplainabilityPost: Validation of engineered featuresPre: Black box testingPost: ExplainabilityPost: Black box testing0 10 20 30 40 50 60 70 80Per cent of cases

#### Chart 16 Outcome-based validation methods are the most common(a)(b)(c)


[p. 26]

(a) ‘Pre’ indicates pre-deployment use of the validation method. ‘Post’ indicates post-deployment use of the validation method.

(b) Firms often use more than one validation method at a time which is why the percentages add to more than 100.

(c) The underlying data is based on the use cases provided by survey respondents.

We asked firms a range of questions about the complexity of their ML applications. We did so because complexity, in principle, can influence a firm’s risk profile and therefore the supervisory approach (Box 3, Section 3.3).

Firms often mention that it is difficult to clearly define what ‘complexity’ means but attempt to make an assessment based on the number of components, number of data sources and algorithms in the ML model. Based on this, respondents gave their best estimates of the complexity which were then grouped in three main categories (‘Low’, ‘Medium’, and ‘High’). In cases where ML models were provided by a third-party, firms stated that it made it more difficult to assess the degree of complexity. As summarised in Chart 17, more than half of applications are considered to be of medium to high complexity.

### 5.5 Complexity can increase due to deployment of machine learning


[pp. 26-27]

Chart 17 More than half of applications are considered to be of medium to high complexity(a)

LowMediumHighUnspecified0 10 20 30 40Per cent of firms who answered the question

(a) The underlying data is based on the use cases provided by survey respondents.

A minority — about one tenth — of firms report having ML systems that comprise at least three separate components. This can add to both the size of the overall ML pipeline (see Figure 2 in section 5.1) and the complexity of the application. Such components can include separate data processing, analytics and decision-making engines. Generally these components are developed in-house and some others provided by third parties, which might create additional complexity when it comes to ensuring the smooth and robust interplay between different components of a ML system.

In addition, firms report using a large number of data sources and it is not uncommon to feed more than 100 different variables into a ML application.

### 5.6 Firms use a range of safeguards to address risks


[p. 27]

Firms use a range of mechanisms and controls to manage the risks associated with ML applications. However, the additional complexity, issues with explainability and the continuous lifecycle of ML introduces new challenges, which require safeguards. Overall, the most common controls among survey respondents are alert systems and so-called ‘human-in-the-loop’ mechanisms (Chart 18). The former are systems that flag unusual or unexpected actions to employees. The latter are systems where decisions made by the ML application are only executed after review or approval from a human. 40% of use cases have ‘guardrails’ in place which switch off the model automatically if it produces undesired outputs. This is intended to mitigate the potential for model drift, which can occur as ML algorithms self-teach and make decisions that are outside their original parameters.

Chart 18 Alert systems and human-in-the-loop are the most common safeguards(a)(b)

Safeguard usedAlert systemHuman-in-the-loopBack-up system‘Guardrails’Kill switches0 10 20 30 40 50 60 70Per cent of cases

(a) Firms often use more than one type of safeguard at a time which is why the percentages add to more than 100.

(b) The underlying data is based on the use cases provided by survey respondents.


---

[previous part](text-002.md) | [source overview](overview.md) | [next part](text-004.md)

[^original]: Financial Conduct Authority, "Machine learning in UK financial services" (2019-10). https://www.fca.org.uk/publication/research/research-note-on-machine-learning-in-uk-financial-services.pdf
