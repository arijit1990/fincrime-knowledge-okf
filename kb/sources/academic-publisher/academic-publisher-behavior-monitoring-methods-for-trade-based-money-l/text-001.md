---
type: Source Text
title: 'BEHAVIOR MONITORING METHODS FOR TRADE-BASED MONEY LAUNDERING INTEGRATING MACRO AND MICRO PRUDENTIAL REGULATION: A CASE FROM CHINA - part 1 of 3 (pp. 1-10)'
description: 'Verbatim extracted text, pp. 1-10: BEHAVIOR MONITORING METHODS FOR TRADE-BASED MONEY LAUNDERING INTEGRATING MACRO AND MICRO PRUDENTIAL REGULATION: A CASE FROM CHINA; BEHAVIOR MONITORING METHODS FOR TRADE-BASED MONEY LAUNDERING INTEGRATING MACRO AND MICRO PRUDENTIAL REGULATION: A CASE FROM CHINA > Introduction; BEHAVIOR MONITORING METHODS FOR TRADE-BASED MONEY LAUNDERING INTEGRATING MACRO AND MICRO PRUDENTIAL REGULATION: A CASE FROM CHINA > 1. Literature reviews; and 2 more sections'
resource: https://journals.vilniustech.lt/index.php/TEDE/article/view/9383
tags:
- academic_finding
- academic_paper
- global_academic
- trade_based_ml
- typologies
status: stable
source_id: academic-publisher-behavior-monitoring-methods-for-trade-based-money-l
issuer: academic_publisher
issuer_name: Academic publisher / repository
jurisdictions:
- GLOBAL_ACADEMIC
tier: 3
instrument_type: academic_paper
normative_force: academic_finding
publication_date: '2019-05-08'
legal_status: unknown
part: 1
parts_total: 3
content_mode: full_text
generated:
  by: process:fincrime-kb-build
  at: '2026-11-21T13:42:33Z'
verified:
- by: process:kb-validate/verbatim-coverage
  at: '2026-11-21T13:42:33Z'
sources:
- id: original
  resource: https://journals.vilniustech.lt/index.php/TEDE/article/view/9383
  title: 'BEHAVIOR MONITORING METHODS FOR TRADE-BASED MONEY LAUNDERING INTEGRATING MACRO AND MICRO PRUDENTIAL REGULATION: A CASE FROM CHINA'
  author: org:academic_publisher
  last_modified: '2019-05-08T00:00:00Z'
---

# BEHAVIOR MONITORING METHODS FOR TRADE-BASED MONEY LAUNDERING INTEGRATING MACRO AND MICRO PRUDENTIAL REGULATION: A CASE FROM CHINA

[source overview](overview.md) | [next part](text-002.md)

> Verbatim text extracted from the original (Academic publisher / repository, 2019-05-08), part 1 of 3, pp. 1-10. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **academic finding**.[^original]

[p. 1]

Technological and Economic Development of Economy ISSN: 2029-4913 / eISSN: 2029-4921 2019 Volume 25 Issue 6: 1081–1096 https://doi.org/10.3846/tede.2019.9383

Xiangrui CHAO1 , Gang KOU2* , Yi PENG1 , Fawaz E. ALSAADI3

_1School of Management and Economics, University of Electronic Science and Technology of China, No. 2006, Xiyuan Ave, West Hi-Tech Zone, Chengdu, 611731, China_

## BEHAVIOR MONITORING METHODS FOR TRADE-BASED MONEY LAUNDERING INTEGRATING MACRO AND MICRO PRUDENTIAL REGULATION: A CASE FROM CHINA


_2School of Business Administration, Southwestern University of Finance and Economics, No. 555, Liutai Ave, Wenjiang Zone, Chengdu, 611130, China_

_3Department of Information Technology, Faculty of Computing and IT, King Abdulaziz University, Jeddah, Saudi Arabia_

Received 11 June 2018; accepted 16 December 2018

Abstract. Trade-based Money Laundering, a new form of money laundering using international trade as a signboard, always appears along with speculative capital movement which has been accepted as the most concerned and consensus incentive giving rise to the collapse of the financial market. Unfortunately, preventing money laundering is very difficult since money laundering always has a plausible trade characterization. To reach this goal, supervision for regulator and financial institutions aims to effectively monitor micro entities’ behavior in financial markets. The main purpose of this paper is to establish a monitoring method including accurate recognition and classified supervision for Trade-based Money Laundering by means of knowledge-driven multi-class classification algorithms associated with macro and micro prudential regulation, such that the model can forecast the predicted class from the concerned management areas. Based on empirical data from China, we demonstrate the application and explain how the monitor method can help to improve management efficiency in the financial market.

Keywords: financial risk monitor, Trade-based Money Laundering, macro- and micro- prudential regulation, machine learning, Reg-tech.

JEL Classification: C80, G18.

### Introduction


[pp. 1-2]

Cross-border capital frequent flow, which is used as arbitrage in financial markets, is most harmful to the financial market and economics of emerging markets and developing economics (EMDEs). Many accelerating global capital flows and financial market failures require financial market regulation for reasons of export reduced, unemployment and economic stagnation in developing countries.

*Corresponding author. E-mail: _kou.gang@qq.com_

Copyright © 2019 The Author(s). Published by VGTU Press

This is an Open Access article distributed under the terms of the Creative Commons Attribution License (http://creativecommons. org/licenses/by/4.0/), which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.

To cope with speculative capital, short-term capital control remains an effective tool to protect financial markets in EMDEs from disorderly shock. Therefore, cross-border money transferring accompanied by trade background has become one of the capital flow channels, which will cause cross-border capital flow and result in foreign exchange market turbulence (Naheem, 2016a, 2016b; Yousefi et al., 2018; Asongu, Akpan, & Isihak, 2018). Transferring capital with trade background has been declared Trade-based Money Laundering (TBML) by the Financial Action Task Force on Money Laundering (FATF, 2006), which means the illegal or speculative capital transferring along with international trades by means of overand under- true value of goods and services. The TBML is seriously concerned by emerging markets and developing economics (EMDEs) and has turned into a dominating issue because of laundering funds with higher frequent cross-border capital fluctuations, which have been acknowledged as being the cause of the Southeast Asia financial crisis in 1998.

To detect TBML behavior, several methods have been developed to recognize abnormal capital mixed with good payments. Firstly, a statistical approach aims to discover the average price of goods and trace customs declaration with higher or lower prices. Secondly, the econometric method is used to find isolated points considered to be TBML in a regression process of price and payments for all trade markets. The main insight of these methods is established in the comparison model between individual and total features.

Many rule-based strategic tools including macro- and micro-prudential have been implemented to respond to capital shock from TBML. Macro-prudential tools aim to mitigate the positive impact of capital by means of counter-cyclical supervision, such as concern regulation of inflow capital in a growth period. Micro-prudential tools, such as ongoing and expost regulation, self-discipline mechanism against operation risk, executive interviews and currency intervention, etc. are also widely implemented in EMDEs.

[pp. 2-3]

However, the existing methods also have many shortages when applied to fit the current trend of TBML management. First, these methods focus on statistical properties of uni-source data such as the customs declaration price, and bank transaction data and detect outlier or deviation to average value. The methods cannot capture new trends of TBML behavior such as unmatched money transferring along with true trade background, which haven’t always had false trade behavior such as using fake invoices or shipping merchandise lower than the true value. Secondly, the detection needs to integrate multi-source data to test micro market behavior. Thus, the TBML behavior is characterized by high dimensionality of features, often with high frequency, wholesale and combined monitor index of current and capital accounts. Therefore, developing a machine learning method to discover abnormal behavior in international trade is urgently required. Lastly, targeted and effective methods for macro-and micro- prudential regulation in the financial market in order to decrease human resources and increase management efficiency must also be urgently developed. Recently, Reg-tech, which simply means financial regulation using modern intelligent technologies, has become a popular tool to detect financial risk and is partly employed to regulate (Larsen & Gilani, 2017; Pishdar, Ghasemzadeh, Antucheviciene, & Saparauskas, 2018). Thus, it can provide an effective approach based on information technology, which is associated with marco- and micro- policy instruments responding to TBML, although it is very difficult to be implemented due to the lack of clue detection and intelligent technologies.

_Technological and Economic Development of Economy, 2019, 25(6): 1081–1096_

This paper aims to develop a framework for managing TBML based on data mining which begins by constructing data feature selection, and multi-class labels which are designed by means of knowledge-driven experiences under macro and micro-prudential management. A multi-class classification algorithm is employed to build a pre-warning model and forecast entities’ behavior, as well as an evaluation index to assess such an algorithm’s performance.

The possible contributions of this paper are to fill the gap of detecting Trade-based Money Laundering behavior using machine learning (ML) methods, and build a novel framework for TBML regulations with Reg-tech. The data used in this paper has been extracted from real-life practice and management cases. Throughout our research, a good theoretical basis will be set up for financial market management responding TBML in EMDEs.

The remainder of this paper is orgasnized as follows: in Section 1, we overview the main methods for TBML monitoring and cross border capital flow control. Feature extraction and algorithm frameworks will be proposed in Section 2. The experiments demonstrate the effectiveness of ML algorithms using real-world data in Section 3. We conclude this article in last section.

### 1. Literature reviews


[pp. 3-4]

Capital transferring has many financial variables and other institutional factors including financial markets and capital control (Giovanni, 2005; Aglietta & Scialom, 2010). In EMDEs, capital control still has a response policy to protect from financial crisis (Johnson & Mitton, 2001). However, global investment and trade liberalization is still an irreversible trend. Thus, managing global capital flows requires global and national efforts to maintain their stability and growth (Gallagher, 2012). In sum, under the background of the orderly opening of capital markets in EMDEs, capital transferring hidden in trade is widely accepted as one of the most dangerous behaviors for capital flow and the most important area of financial regulation. The amount of economic and financial damage caused by international unlawful acts in recent years leaves little doubt that the financial institutions and multinational corporations (Mcskimming, 2010), even customs (Xue & Zhang, 2016) and noncompliant banks (McIntosh, 2016), are becoming severely afflicted areas in global business activities. To summarize, this paper conducts empirical analysis on TBML detection using intelligent algorithm in China and theoretical arguments on feature engineering and algorithm conversion in the Reg-tech areas.

Many questions regarding current forms of money laundering have sprung up and today TBML are becoming more and more popular (Unger & den Hertog, 2012; Ferwerda et al., 2013; Delston & Walls, 2009; Liao & Acharya, 2011; Thanasegaran & Shanmugam, 2007). For this reason, regulation is becoming more important (Deng, Joseph, Sudjianto, & Wu, 2012). However, the challenge will bring a new trend for money-laundering from the traditional banks sector to the financial market along with electronic payments, trade and real estate. There are existing methods for monitoring TBML behavior with different insight and technologies.

First, the usual method used to manage TBML is implemented by the comparison of a customs declaration price and the average price of the goods, which is built from cus-

tom merchandises data. Zdanowicz (2009) illustrated many forms of Trade-based Money Laundering and proposed a statistical method to detect this behavior which is based on price deviation between the mean price of the goods and single trade. His research built an average price database of export goods based on the U.S. Merchandise trade database. By means of his study, the abnormal trades are those prices which are sharply higher than the average price. The same method is also used in China Customs (Cassara, 2011). Gao and Weng (2006) also proposed an artificial transfer pricing paradigm to test money laundering. Moreover, capital flight and tax evasion were added to the model and the impact on the money laundering pool was tested.

[p. 4]

Second, many econometric methods in economics attempt to measure TBML behavior. Ferwerda _et al._ (2013) claimed that when using traditional methods in economic literature TBML was difficult to access since the TBML is hidden in licit trade and thus proposed an updated gravity model, which means a regression of exports and Gross Domestic Product (GDP), population, border dummy, common language, colonial background and distance of two countries, as opposed to the Walker (1995) and Unger (2007) prototype model. Their basic idea of the normal value of exports matches the inherent scale of two countries. Thus, they detected TBML flow to be an existing deviation between money transferring and the normal scale of trade based on national GDP and other trade factors. Their results verified that TBML can escape the stricter anti-money laundering regulations of financial markets. Melvin (2014) asserted that the TBML definition of FATF is seriously flawed since trade data used to detect TBML is not valid. Thus, their viewpoint on the context of TBML has always been established with the true value, quality and quantity of the shipment. Therefore, their concerns regarding cash payment should be considered when detecting TBML in trade. From the above literature, there is no doubt that trade and payment are two factors for TBML detection regardless of the type of TBML detection.

Lastly, Reg-tech technologies which try to use machine learning methods in money laundering are also a new trend to detect money laundering behavior. For example, Outlier Detection is regarded as abnormal behavior in financial transaction data including clustering and regression algorithms (Rohit & Patel, 2015; Kannan & Somasundaram, 2015). Kannan and Somasundaram (2017) employed the autoregressive-based outlier algorithm to detect money laundering behavior and their model aimed to compute the mean value of financial transaction data and then obtain deviation between individual data and mean data. Based on the proposed distance, abnormal data can be detected in terms of pre-set distance parameters.

[pp. 4-5]

However, we must point out that the methods proposed in current papers are based on price comparison and statistical methods under the assumption that the TBML have fake trade which is not the case for the new trend of TBML (Melvin, 2014), or the data mining using outlier algorithms in order to detect abnormal data. The money laundering regulation should adopt integrated macro- and micro-policy and global regulation mixed local regulation to protect from systemic risk caused by speculative local capital flow under international trade in financial markets (Borio, 2003, 2011; Wymeersch, 2010; Kashif, S. F. Iftikhar, & K. Iftikhar, 2016; Song, Wang, & Zhu, 2018; Chen, He, & Li, 2017; Zavadskas et al., 2018). Macro-prudential regulation can be simply divided into two main folds: on the one hand, a countercyclical operation used to alleviate cyclical capital flow which causes harmful economic shock. On the other hand, ‘too big to fail’ institutions should be discerned and

_Technological and Economic Development of Economy, 2019, 25(6): 1081–1096_

managed in order to respond to the risk spread (Allen, Goldstein, Jagtiani, & Lang, 2016; Arnold, Borio, Ellis, & Moshirian, 2012; Milne, 2009; Arthur, 2017; Ahmed, Socci, Severini, Yasser, & Pretaroli, 2018; Hamdi, Hakimi, & Zaghdoudi, 2017). Micro- prudential regulation evaluates asset and risk response for micro-companies. Therefore, an effective Reg-tech for TBML should consider data feature engineering based on micro-prudential, knowledgedriven based macro-prudential regulation. That is, the classification labels can be assigned with different periods in terms of the countercyclical direction with the current and further trend. In addition, classification features can be designed on basis of the metrics of asset-debt and risk exposures of micro-companies.

Therefore, in our paper, the monitoring direction of capital flow is determined according to macro-prudential regulation tasks, and a payments-goods based TBML framework will be constructed and knowledge-driven classification methods will be used to detect proposed behavior based on Chinese data.

### 2. Framework, feature selection and machine learning algorithms


[p. 5]

In this section, a monitoring framework will be presented according to the following Figure 1.

The rule of TBML studied in our paper is the aforementioned payment-trade principle1 which provides a new insight for TBML based on the true value, quality and quantity of the shipment (Melvin, 2014). The TBML should identify the flow of money corresponding to trade and the deviation of the value between money and goods, even frequency and amount. The behavior should be described by many features using machine learning tools. The detail can be found in Subsection 3.3.

#### 2.2. Monitoring process and data resource


The monitoring model is constructed on the basis of payments and goods of entities (individuality and enterprises) in the market. The class label will be assigned referring to countercyclical and management cases. At the bottom of Figure 1 are the machine learning methods used for behavior monitoring. In this paper, a classification method will be presented to illustrate the detection of TBML.

The features are constructed as a combination of time frequency, rate of flow and deviation of trade and money (detail can be found in the Appendix 1). Table 1 shows the main features in monitoring models and the index is computed within a period of 12 months using dynamic recursion calculation. Parts of the index are collected from the State Administration of Foreign Exchange (SAFE) in China.

#### 2.3. Feature extraction


[pp. 5-6]

> 1 Payment-trade principle means the detection of TBML is established at a money transferring and goods value match.

Framework of arbitrage behavior monitoringData sourceInternational Selling and Current andbalance ofpayments foreignbuying accountCapital … declarationCustoms TariffexchangeMacro prudential Micro prudentialdirection Behavior monitoring (Knowledge-driven(Machine learning)(Countcyclical) Cases)OutlierFeatures Class labels Clasification EvaluationdetectionDeviationindex Managementcases Bayesiannet clustring regression ImbalanceIndexFrequencyindex assignmentLabel SupervisedMLAmountindex Flow IndexMoney Cost unsupervisedlearningNon Geomean AUCsensitivelearning

Figure 1. Framework of behavior monitoring

#### 2.4. Machine learning algorithms


[pp. 6-7]

Machine learning (ML) algorithms used in our model are based on knowledge-driven multiclass classification technology. In the real world, the distribution of different class label data is different, and the numbers also have an unbalanced ratio in the production and collection of data, especially it is the case in financial regulation. The ratio of normal and abnormal institutions becomes larger since only small group arbitrage institutions are forecasted and detected. Cost sensitive learning is one of the representative algorithms for imbalanced data (Lomax & Vadera, 2013; Masnadi-Shiraziet, Vasconcelos, & Iranmehr, 2015; Huang & Kou, 2014; Huang, Kou, & Peng, 2017; Kou, Peng, & Wang, 2014; Kou, Lu, Peng, & Shi, 2012; Chao, Kou, Li, & Peng, 2018). In some specific data sets, the accuracy rate proved to be higher than standard classifiers (Liu & Zhou, 2006). Recently Chao and Peng (2017) have developed a new cost-sensitive classification algorithm.

_Technological and Economic Development of Economy, 2019, 25(6): 1081–1096_

Table 1. Features selection in monitoring model

|Total Transactions ofpurchasing currency|Export|Actual domestic forexloan more than 90 days|Total payment|
|---|---|---|---|
|Whether or notinspect|Income|Balance of domestic forexloan more than 90 days|Purchasing/payment|
|Licensing status|Expense|Whether or not top 30purchasing|Purchasing and paymentat remote bank|
|Management level|Purchasingcurrency|Mean days ofpurchasing|Payment/import|
|Local sample|Exchange Settlement|Numbers of top 30purchasing|Credit trade/total trade|
|Special assignment ofSAFE|Account purchasing|Mean amount ofpurchasing|Payment of creditpayment|
|Total deviation ofmoneyandgoods|Account settlement|Whether or notindividual large-amount|Setllement + income –purchasing– expense|
|Credit trade|Cash purchasing|Total amount ofpurchasing|Import + income –export – expense|
|Import|Cash settlement|Single payment|Settlement + import –purchasing– export|

(Import + income – export – expense)/(Import + income + export + expense)

Using our methods, Bayes net (BN) based on Bayesian network is employed as a base classifier and used to handle imbalanced data in financial markets. The main ideas of this algorithm are shown as follows:

[pp. 7-8]

First, BN is a set including a directed acyclic graph _G_ and a conditional probability table. Let _G_ = ( _I_ , _E_ ) represent nodes set _I_ which is random variable and edges set _E_ which is conditional probability.

The joint probability can be obtained using the product of local conditional probability as follows:

For a node (random variable) _x_ , the joint probability can be denoted as follows:

where _Parents_ ( _xi_ ) is set of _i_ -th farther node of _x_ .

In fact, the building of Bayesian net is a solution process of parameters of network structure and probability distribution on the basis of the given data. The probability distribution of root nodes has always determined prior probability. The Bayesian network is used as a classifier if the output node is a class label and the feature is a node. The network and conditional probability will be computed in terms of training data and used to forecast the model.

The main step in BN classification is building the network structure and finding the conditional probability tables of the BN.

First, network structure always uses a heuristic-search algorithm for maximum conditional probability from parent nodes to child nodes. The representative algorithm is K2 established by Cooper and Herskovits (1992). The process can be employed to design max parent nodes, initially a naïve bays network, and then use a hill climbing algorithm restricted by variable ordering.

Second, an estimator is used for parameter estimation for the conditional probability tables of the BN, based on Bayesian conditional probability. The common estimator includes Maximum likelihood estimation, Maximum a posteriori estimation and Bayes estimator, etc. (Cooper & Herskovits, 1992).

Finally, measures including Minimum Description Length, Akaike Information Criterion, and Entropy, etc. are employed to detect quality of established net.

The advantages of Bayesian net are that the network does not require mutual independence and relatively higher accuracy can be acquired by dynamic adjustment along with posterior probability. In our paper, we use K2 and Bayes estimator without adding the ADTree structure.

### 3. Empirical experiments


[p. 8]

Gathering information about entities from the balance of payments and international trade data of Qinghai province, Ningbo city and Shenzhen city gives data which is representative of western, eastern and southern China. The TBML detection is implemented by local government and bank sectors and the different data will be trained as an adaptive forecast model suited to different markets. Therefore, it is stated that the model is not fixed and will not be used in all areas, rather, a different model will be set to test various data under the proposed framework and algorithm.

Data ranges from March 2016 to Feb 2017 and there are 8837 instances with 37 features. The panel data was selected with a sample period of 12 months for two reasons. Firstly, TBML should be detected in a reasonable amount of time so as to promptly identify abnormal behavior rules. A longer time period impacts management time-effectiveness and shorter time periods decrease detection accuracy. Secondly, in management practice data features such as computing and implementation recirculate every month based on past 12 months.

In this section, experiments are implemented using WEKA 3.7.8 (Hall et al., 2009) which is a popular computer software tool widely used in data mining in scientific research.

#### 3.1.1. Evaluation index


[pp. 8-9]

When testing classification performances, TP-rate, FP-rate, AUC, Geomean, F-measure and ROC are used to evaluate the forecasting model:

_Technological and Economic Development of Economy, 2019, 25(6): 1081–1096_

where _P_ is number of positive instances.

The ROC curve is drawn having TP-rate and FP-rate values that compares proposed criterions with various thresholds.

Classification is a supervised data mining algorithm, and the class labels should be assigned a training set in advance. Then, the trained model will be used to handle the testing dataset. Therefore, non-label data items will be labeled by the trained classification model. When monitoring TBML in our model, the labels are ascertained by macro-and micro prudential regulation. First, direction of capital flow is a central factor in assuring that the model can be used to counter-cycle cross-border capital flow. For instance, net outflow entities should be focused on capital flowing to other countries. Second, we should regard micro-behavior considering administrative penalty, low credit, money laundering concern, business cases and arbitrage institution, etc. to obtain general results so that the model can be extensively applied to all areas. However, abnormal entities always exist in small amounts in financial markets, for example, the ratio of normal and abnormal entities is less than 10000:1, thus, imbalance learning should be used to classify the forecasting model. We adopt the Relief feature selection to retain 40 features from the Appendix 1 in order to decrease the correction of two indexes and increase performance of the algorithm. The training data will be assigned a different cost in the sampling process for higher classification accuracy.

#### 3.1.3. Label assignment


[p. 9]

We divided data into five classes: net inflow, small outflow, offshore re-export trade and export without income, respectively. The detail can be seen in Table 2.

Table 2. Class labels

|Label|Numbers|Ratio|Remark|
|---|---|---|---|
|Net inflow|7224|81.7%|Annotation in capital outflow stage|
|Small net outflow|330|3.7%|within the tolerance range in capital outflow stage|
|Concerned net outflow|1188|13.4%|Local samples|
|Offshore re-export trade|36|0.4%|Administrativepenalty|
|Export without income|59|0.7%|Concerned bySAFE and China Customs|

#### 3.1.4. Results


[pp. 9-10]

Table 3 shows the confusion matrix of classification using BN. The minority classes such as offshore re-export trade can be classed correctly, and export without income can almost be correctly recognized. This demonstrates that classification can be used to distinguish ab-

normal entities in financial markets. However, small net outflow and concerned net outflow have confusion in two areas which include small net outflow being classed into concerned net outflow and concerned net outflow into net inflow. The former has no impact on actual management and the latter should be handled for more management targets. The offshore re-export trade and export without income will be regarded as TBML and further inspected by the local government and bank sector.

Table 3. Confusion matrix

|||||Hyp|othesis||
|---|---|---|---|---|---|---|
|||Netinflow|Small netoutflow|Concernednet outflow|Offshorere-export trade|Export withoutincome|
||Net inflow|7159|0|0|36|29|
||Small net outflow|18|312|0|0|0|
|Ture|Concerned net Outflow|115|0|1031|0|42|
||Offshore re-export trade|0|0|0|36|0|
||Export without income|7|0|0|0|52|

Therefore, the two classes should be recognized as the same class on application in order to improve the accuracy of the model, or net flow should adjust many delicate classes so as to fit to different situations.

Table 4 shows the results of classification performance. It is highlighted that our model aims to separate offshore re-export trade and export without income so that the model can be used to detect abnormal behavior predefined by management application.

Table 4. Performance of classification

||TP|FP|AUC|GM|F|ROC|
|---|---|---|---|---|---|---|
|Net inflowl|0.991|0. 087|0.952|0.951|0.986|0.995|
|Small net outflowl|0.945|0.000|0.972|0.972|0.972|1.000|
|Concerned net outflowf|0.868|0.000|0.934|0.932|0.929|1.000|
|Offshore re-export trade|1.000|0.004|0.998|0.998|0.667|1.000|
|Export without income|0.881|0.008|0.937|0.935|0.571|0.926|


---

[source overview](overview.md) | [next part](text-002.md)

[^original]: Xiangrui Chao, Gang Kou, Yi Peng, Fawaz E. Alsaadi, "BEHAVIOR MONITORING METHODS FOR TRADE-BASED MONEY LAUNDERING INTEGRATING MACRO AND MICRO PRUDENTIAL REGULATION: A CASE FROM CHINA" (2019-05-08). https://journals.vilniustech.lt/index.php/TEDE/article/view/9383
