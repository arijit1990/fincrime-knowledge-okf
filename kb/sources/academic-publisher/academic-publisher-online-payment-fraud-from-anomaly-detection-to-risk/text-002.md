---
type: Source Text
title: 'Online payment fraud: from anomaly detection to risk management - part 2 of 3 (pp. 9-19)'
description: 'Verbatim extracted text, pp. 9-19: Online payment fraud: from anomaly detection to risk management > Open Access'
resource: https://link.springer.com/article/10.1186/s40854-023-00470-w
tags:
- academic_finding
- academic_paper
- global_academic
- model_governance
- model_validation
status: stable
source_id: academic-publisher-online-payment-fraud-from-anomaly-detection-to-risk
issuer: academic_publisher
issuer_name: Academic publisher / repository
jurisdictions:
- GLOBAL_ACADEMIC
tier: 3
instrument_type: academic_paper
normative_force: academic_finding
publication_date: '2023-03-12'
legal_status: unknown
part: 2
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
  resource: https://link.springer.com/article/10.1186/s40854-023-00470-w
  title: 'Online payment fraud: from anomaly detection to risk management'
  author: org:academic_publisher
  last_modified: '2023-03-12T00:00:00Z'
---

# Online payment fraud: from anomaly detection to risk management

[previous part](text-001.md) | [source overview](overview.md) | [next part](text-003.md)

> Verbatim text extracted from the original (Academic publisher / repository, 2023-03-12), part 2 of 3, pp. 9-19. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **academic finding**.[^original]

## Online payment fraud: from anomaly detection to risk management


### Open Access


#### Online payment fraud anomaly detection


##### _Base learner: bagged decision tree_


[pp. 9-10]

The decision function in BDT base learners is the probability that an observation, a planned transaction _x_ , is a “non-customer behavior.” This value is equal to the average probability observed for all decision trees in the forest.

where _M_ is the number of trees in the bagged forest, cj is the corresponding customer behavior class, and Pi(Y = cj|X = x) is the probability that observation _x_ is a “non-customer behavior” as predicted by the _i_ th tree. Customer behavior class cj consists of the collected sessions and transactions, excluding potential fraud. The model was fitted as follows:

- For each customer cj , we collect the associated sessions, excluding the potential fraud cases. This set represents the “behavior of customer cj.”

- From the pool of all customer sessions C−j (excluding cj ) we draw a uniform sample of observations to generate a set representing the class “behavior of customer cj not,” cj for short, and equal in size to the cj set. Equal sampling is performed to ensure that none of the other customers are overrepresented in ̸ cj.

- Each bagged forest in the ensemble is trained on a matching feature subspace utilizing all these observations. The forests consist of 100 decision trees each.

BDTs provide variable selection as an additional benefit, owing to the large amount of data involved in supervised classification. Therefore, they can be utilized to estimate the importance of variables and adequacy of feature engineering. We achieve this by calculating the Gini impurity decreases at each split point within each tree for each feature. Gini impurity is a measure of the likelihood that a randomly selected observation would be incorrectly classified by a specific node _m_ :

where pmi is the portion of samples classified as _i_ at node _m_ . These impurity decreases were averaged across all decision trees and outputs to estimate the importance of each input variable. The greater the decrease in impurity, the greater the importance. Utilizing these results, we can identify the relevant subsets of input variables.

Relying on the concept of transfer learning (if the problem described in ?? is sufficiently like fraud detection), we use BDT to select a subset of N = 147 features. Particularly important were features measuring the deviation from the typical time required to complete a two-step verification process during login. Features that encode the relative time between _n_ -grams and specific user request sequences are important. The following additional base model was built using the features selected by BDT.

##### _Base learner: local outlier factor_


[p. 10]

The Local Outlier Factor (LOF) detection method assigns an outlier level to each observation based on its distance from the nearest cluster of neighboring observations (Breunig et al. 2000). The general intent of the LOF model is to identify outliers in the interior region of data, for which classical global outlier methods and the other considered algorithm, isolation forest, usually do not provide satisfactory results. The LOF decision function is as follows:

with _K_ a _k_ -neighborhood and _LD_ ( _x_ ) the local reachability distance density from _x_ to its _k_ -th nearest neighbor. We fit the model for each customer by collecting the first associated sessions or transactions, excluding potential fraud. Each LOF in the ensemble is created utilizing all these observations on a subspace of the relevant features selected by BDT and the sampled hyper-parameter. Finally, each time a new observation is available, its decision function value is computed regarding the observations from the training set.

##### _Base learner: isolation forest_


[pp. 10-11]

The IF algorithm recursively splits the data into two parts based on a random threshold, until each data point is isolated. The algorithm randomly selects a feature at each step, and then randomly selects a division value between its minimum and maximum

values. The algorithm filters out data points that require fewer steps to be isolated from the entire dataset. In our case, IF separates one observation from the rest of a randomly selected subsample of the original dataset (Fei Tony et al. 2008). Anomalies are instances with short average isolation path lengths. The IF decision function is

where _E_ ( _H_ ( _x_ )) is the average number of edges traversed to isolate the node and _C_ is the average number of edges traversed in an unsuccessful search. To fit the model, we first collected each client’s associated sessions or transactions, excluding potential fraud cases. In step two, each isolation forest in the ensemble was created utilizing all these observations in a matching feature subspace. Each forest consisted of 100 isolated trees. Finally, each time a new observation was available, its decision function value was computed regarding the isolation trees created based on the training set.

##### _Base learner scores combination_


[pp. 11-12]

The decision functions of the base learners produced by our ensembles must be combined into a single fraud score. As these are in different ranges and scales to render the decision functions comparable, we first replace the original scores by their ranks, regarding the non-fraudulent training scores. Rank normalization is more robust and numerical stable as opposed to z-scores, for example. Therefore, we replaced the original scores with their ranks regarding the non-fraudulent training scores for each base learner:

where _V_ is the set of all δBase(p) over all observations p′ in the learners’ training subsample, with Base being LOF, IF, or BDT.

Owing to the few fraud cases, our model largely consists of unsupervised procedures. However, we introduced supervision utilizing scarce labelled data to readjust the importance of particular base learners in the voting scheme, ultimately deciding whether an observation is fraudulent.

The following score combination procedure was established. First, a training set comprises all fraud cases in the sample, along with healthy transactions uniformly sampled over customers from the ensemble training data. Second, a logistic regression is trained to classify observations as fraudulent or not utilizing the 6 _N_ normalized decision function features and the known fraud status on past transactions as the label.

The following binary-class penalized cost function is minimized:

where yi is the fraud label of transaction _i_ , Xi′ is a row of 6_N_decision functions describ- ing transaction _i_ , _R_ is the regularization factor, and ( _w_ , _c_ ) is a set of weights defining the decision boundary between the two classes: fraud and non-fraud. To account for the imbalance between fraud and non-fraud transactions in our sample, we assign asymmetric penalties for fraud misclassification, as opposed to non-fraud classification.

Choosing logistic regression to optimize the weights of the base learners ensures that the final score combination x′ w represents the log-odds of an observation to be fraudulent.

where δ(x) is the probability that the observation _x_ is fraudulent. Finally, to assign a fraud label to a session _x_ , we compare the output combined score, or equivalently, the probability δ(x) , to a threshold _y_ , which is chosen based on ROC curve analysis such that the defined maximum allowed false positive rate is not exceeded. The decision boundary of logistic regression is linear, where each base learner is assigned a weight wi to determine its relative importance for fraud classification. This structure simplifies the interpretation of the model because these weights can be utilized to identify the base learners, feature subsets, and sample subsets, which are particularly useful in detecting a particular type of fraud associated with a high weight wi . Appendix A provides a detailed description of the ensemble design.

##### Normal customer behavior model


[pp. 12-13]

In summary, we created an ensemble model for each client, which is re-trained with new data at regular intervals and can be described by the following steps:

- We consider the disjoint sets of behavioral features on session observations and transactional features on transaction observations.

- For each of the two features/observations-pairs, we define N = 1000 learners for each of the three model categories as follows.

- We fix _N_ random sub-samples of features from the feature set. Each sub-sample remains fixed for all customers.

- For each customer, we fix _N_ random observation samples from the customerspecific sessions or transactions observations.

- For each of the three model categories, for each customer, and for i = 1, ..., N , a base learner is defined by applying the model algorithm to the _i_ -th features sub-sample and _i_ -th observations sub-sample. Thus, this results in 6 _N_ base learners per customer, 3 _N_ for sessions, and another 3 _N_ for transaction data.

- The decisions for the three base learners are aggregated utilizing supervision, where the knowledge obtained from existing fraud cases is utilized to adjust the base learner weights.

Utilizing this representation, we train a model that (i) outputs an indicator of how likely a scheduled transaction is fraudulent, (ii) aggregates the overall provided decision functions to derive the unified hypothesis, while assigning more importance to

learners that showcase the capability to better distinguish between fraud and nonfraud, and (iii) deals with a large imbalance in class representation.

##### Validation results


[p. 13]

The training, test, and validation sets consisted of data collected from July to October 2017, as dictated by the availability of online session log files. Around 900’000 sessions formed the dataset.

Raw data were processed using ETL to derive customer-specific feature representations of each recorded online session. The data were then split into non-fraud and fraud sets. The fraud set was not utilized to train the unsupervised base learners. Non-fraudulent (“healthy”) sessions were separated into training and test sets utilizing a 3-fold cross-validation split. We then sequentially trained the models on each derived training fold and computed the scores for observations in the corresponding test folds. Following, we obtained an out-of-sample decision function value for each healthy session and each base learner. We then assigned base learner scores to each fraudulent session utilizing base learners trained on all healthy data.

The out-of-sample logistic regression decision function values were aggregated by averaging within their respective ensembles (LOFs, IFs, and BDTs). This step yields a 3-dimensional representation of each customer’s online session. Finally, we utilized leave-one-out cross-validation to report the ROC curve measures. Hence, the logistic regression model is consecutively trained on an all-but-one observation, followed by computing the probability of an observation that was left out. Thus, we again obtain an out-of-sample fraud probability for each observation in the sample. We opted for leaveone-out cross-validation to maximize the number of fraudulent observations in each training set, because these are particularly scarce. Once we have obtained the aforementioned out-of-sample probabilities for each observation, we construct an ROC curve to display the FPR and TPR relationship depending on the decision threshold.

Resultantly, when utilizing no transaction data, the detection rate of the machine learning model was in a realistic range of 18% true positives. These primary results can be easily optimized to increase the TPR and simultaneously reduce the FPR utilizing different measures. This led to an increase in true positives by up to 45%, see Table 1.

Overall, LOF seems to perform best over the entire dataset compared to IF and BDT. However, BDT has a slightly steeper ROC curve at the beginning, thus showing better pure outlier detection capabilities. Furthermore, because BDT seems to detect frauds, as discussed below, involving larger amounts than those detected by LOF, we cannot conclude that LOF outperforms the other approaches considered. Aggregating the decision functions of the ensembles utilizing simple means outperformed supervised aggregation. Through analysis of logistic regression weights assigned to each ensemble of learners, we determined that significantly higher weights were assigned to the LOF ensemble, most likely due to its best performance over the whole dataset. This dampened the input from the other two ensembles. However, this is not the case when the mean for aggregation is utilized. The results were affected by the small number of frauds and the size of the sample analyzed.

[pp. 13-14]

Different ensembles detected different types of fraud, and by observing figures depicting money saved per raised alarm, we see that different ensembles (LOF and

Table 1 The zero percentage TPR in the benchmark model is due to the fact that the static rule based model of the bank was not able to identify a single true positive case

|Model|TPR|FPR|
|---|---|---|
|Benchmark model|0%|1% and 2%|
|500 LOF|18%|1%|
|500 LOF|45%|2%|
|500 BDT|18%|1%|
|500 BDT|27%|2%|
|500 IF|0%|1%|
|500 IF|27%|2%|
|Mean decision function|36%|1%|
|Mean decision function|36%|2%|
|Supervised decision function|18 %|1%|
|Supervised decision function|18%|2%|

The results of the mean aggregation approach derived from an aggregation of three standalone ensembles consisting of 500 LOF, 500 BDT and 500 IF base learners, where aggregation was performed by taking the mean value of decision functions from three different types of base learners

Table 2 Comparing the performance of different anomaly fraud detection models

|Paper|TPR|FPR|Remark|
|---|---|---|---|
|Wei et al. (2013)|49%-60%|NA|–|
|Carminati et al. (2015)|98.26%|0.19%|Scenario I+II|
|Carminati et al. (2015)|70%|14%|Scenario III|
|Vanini et al. (2022)|45%|1%|–|
|Vanini et al. (2022)|62%|3.5%|–|

TPR means True Positive Rate and FPR the False Positive Rate

BDT) detect different types of fraud cases, displayed by a large difference in saved money per trigger. Logistic regression supervision alarms were affected mainly by LOF, thus making it miss large embezzlement detected by the BDT ensemble. This motivates the triage model described in the next section. As of the restriction of the FPR to no greater than 2%, the entire ROC curve is of less interest. The ROC AUC values for the LOF ensemble is 0.93, for the BDT ensemble 0.82, and for the mean decision function ensemble 0.91.

[pp. 14-15]

We compared our results with those of Wei et al. (2013), and Carminati et al. (2015). These are two of the few studies dealing with online fraud detection that use real-world data, at least in part. Wei et al. (2013) utilized an unsupervised approach, whereas Carminati et al. (2015) utilized a semi-supervised approach. Table 2 compares the performance of our model with those of Wei et al. (2013) and Carminati et al. (2015). The results of this table should be interpreted with caution. First, different payment channels were considered. Second, the data of Carminati et al. (2015) were anonymized and did not include fraud cases. These are artificially added to tune 1% of the data volume, compared to 0.018% in Wei et al. (2013) and 0.0012% in our dataset. Third, Wei et al. (2013) did not report the FPR. Finally, Carminati et al. (2015) published an almost perfect error detection for scenarios I + II, but in scenario III,

the false positives are too high; they generate too much manual work for the bank. The former scenarios are simple fraud scenarios that would be blacklisted and filtered out in our data before machine learning engages.

#### Fraud detection triage model


##### Formalization


[pp. 15-16]

We formalize the triage model and denote by � the set of all transactions with ω as a single transaction, T (ω) as the transaction amount function, and χF (ω) as the fraud indicator function, where χF (ω) = 1 represents fraud. Space � is attributed to a probability distribution _P_ with _p_ ( _x_ ) as the density function of the transaction amounts. The threshold value _L_ of the fraud score function _S_ is a function of the transaction amount _x_ . We define:

If we assume stochastic independence of the transaction amount _T_ , score _S_ and fraud indicator χF , we obtain the following interpretation:

Note that the assumptions of independence are strong, as transaction sizes are utilized as the input of the machine-learning model underlying the score. Conversely, the independence of χf and _T_ implies that the transaction amounts of fraudulent transactions have the same distribution as those of non-fraudulent transactions. In the context of the value-at-risk model in the next section, we argue that there is little evidence to support this. This considered, the assumption of independence is theoretically difficult to uphold, but in practice quite necessary to obtain our results.

We formulate our optimization problem as follows:

under the constraint of the _integrated FPR_

The expectation in (11) is the average cumulated sum of fraudulent transaction amounts detected by the detection model. By letting q0 := E(χF ) and utilizing (10), we can rewrite it as

The constant q0 is irrelevant to the optimization. Setting g(x) = FPR(L(x)) , we reformulate the optimization problem in terms of the ROC curve as

Table 3 Moments and quantiles of the fitted lognormal distributions in CHF for the online and mobile banking channel transactions

||Mean|Std. Dev.|90%|99%|99.9%|
|---|---|---|---|---|---|
|Online banking|2’355|11’290|4’722|30’304|118’663|
|Mobile banking|774|2499|1’699|8’565|27’954|

Table 4 Support points for the cubic spline construction of the ROC curve

[p. 16]

|FPR|00.0020.0040.008|0.01|0.02|0.03|0.05|0.1|1|
|---|---|---|---|---|---|---|---|
|TPR|00.10.180.28|0.31|0.4|0.45|0.5|0.55|1|
||maxg�∞0xROC(g(x))p(x)dx||||||(14)|
|und|er the constraint:�∞0g(x)p(x)dx≤constant.||||||(15)|

To account for the recovery, we introduce a recovery function θ : � →[0, 1] . This function changes the objective function in the optimization problem, as follows:

whereas this constraint does not change.

##### Optimization


[pp. 16-17]

To put our formal model into practice, we need to fix a distribution for transaction amounts. Utilizing approximately 12 million transactions from online banking and 1.2 million from mobile banking, we approximated the distribution for both channels utilizing lognormal distributions. Although this choice does not particularly focus on the distribution’s tails, it will be seen that the optimal model still places strong emphasis on the detection of anomalies with large transaction amounts. Some basic statistics of the fitted distributions are given in Table 3.

The ROC curve is conceptually the output of the detection model described in the previous section. However, owing to the limited number of actual fraud cases available, the TPR values for the given FPR levels are tainted with considerable uncertainty. The ROC curve utilized in our optimization was obtained by fitting a cubic spline function to the base points, as presented in Table 4. The support points were adjusted to avoid unwanted spikes in the cubic interpolation.

As the triage model aims to prevent large losses with a higher probability than smaller ones, the optimal FPR will be an increasing function of the transaction size. To avoid possible optimization problems, we choose a simple form for FPR as a function of transaction size, namely, a piecewise linear function satisfying g(0) = 0 , g(T1) = a , g(T2) = 1 for the parameters a > 0 and 0 
FPR-Curve Online Banking (Total FPRTransac�on Amount in CHF Transac�on Amount in CHFFPR TPR

Fig. 1 Panel Left: False positive rate as a function of the transaction amount under the constraint that the total false positive rate is smaller than 0.4 percent. Right Panel: True positive rate as a function of the transaction amount. The total effectiveness is 39 percent

The optimization problem can be simplified by assuming equality in (12) and solving _a_ as a function of T1 and T2 . For a target integrated FPR of 0.4%, we obtained the solutions listed in Table 5.

[p. 17]

Figure 1 illustrates the results for an online banking channel. The concave shape of the FPR curve up to T2 shows that the optimal solution emphasizes the detection of large transaction fraud cases, accepting, in turn, the less rigorous testing of small and moderate transactions up to T1 . For transaction amounts larger than T2 , FPR and TPR are equal to 1 by construction. Hence, all such transactions are automatically flagged as anomalies. _Total Effectiveness_

is the average percentage of integrated fraudulent transaction amounts detected as anomalies. In our optimized case, the rate was 39%.

Compound Poisson processes were utilized as basic building blocks. We utilize beta marginal distributions for modelling bounded transaction amounts and generalized Pareto marginal distributions (GPD) for unbounded ones. The so-called mass-attack model is formulated as a nested compound Poisson process with a marginal beta distribution. All subprocesses are aggregated independently. Loss statistics, such as value-at-risk or other quantiles of the distribution, are obtained by running Monte Carlo simulations.

#### Risk model


##### The model


[pp. 17-18]

Utilizing the limited available fraud data and drawing on discussions with practitioners, we develop the following model for online banking fraud:

- Isolated attacks with a moderate transaction size of up to CHF 70’000 are modelled by a compound Poisson process with beta marginal distribution.

- Isolated attacks with transaction amounts larger than CHF 70’000 are modelled by a compound Poisson process with GPD marginal.

- “Mass attacks” are modelled as a nested compound Poisson process, where the inner Poisson process simulates the individual transactions triggered by the mass attack. The inner process has a beta marginal distribution and generates transaction amounts up to CHF 20’000.

The intensities of the Poisson processes constituting the submodels vary. In our case, isolated attacks of moderate size were by far the most frequent, followed by isolated attacks of large size. Mass attacks were the least frequent.

Mobile banking fraud is modelled analogously, albeit with transaction sizes only up to CHF 20’000, because larger amounts were inadmissible on this channel during our investigation. Hence, there is no Poisson process with GPD marginal in this case. Contrastingly, in the EBICS channel, which is an internet-based payment channel between banks, only the possibility of large fraudulent transactions was of interest. Hence, this model consists of a single compound Poisson process with GPD marginals above CHF 100’000. The details of the parametrization are given in Appendix A.

Countermeasures against fraud and recovery measures after fraud events play an essential role in determining risk potential. Therefore, they were integrated into the risk models. Countermeasures against online fraud fall into two categories: those that strengthen general infrastructure of the payment process to make it harder for attackers to find a weak spot, and those that are geared towards fighting off actual attacks. The first type is conceptually part of the base model described above, as it affects the frequency and possibly the transaction size of attacks. However, the second type is better understood in the context of recovery.

A recovery variable is introduced in the triage model, which accounts for it often being possible to recover money even after it has been transferred to another bank through fraudulent transactions. Conversely, by monitoring transactions utilizing the fraud detection and triage model, a certain percentage of attacks can be identified even before the transactions are released. The ROC curve of the detection model’s ROC curve, in combination with the triage model, allows us to infer the probability of detection from the transaction size: such that this component of the recovery process is readily integrated into the stochastic framework.

Owing to the nonlinearity of the risk statistics, the aggregation of the models was performed at the level of individual scenarios. Thus, for each scenario, si , the loss of the overall model for one-year was calculated from the simulated loss events of the channel models:

[p. 19]

Table 6 Simulated moments and quantiles for online banking based on 100’000 Monte Carlo simulations

|in CHF 1’000|Mean|Std. Dev.|90%|99%|99.9%|
|---|---|---|---|---|---|
|Total no detection|2’023|1’056|3’443|5’083|6’505|
|Total FPR 0.4 Pct|1’659|892|2’865|4’258|5’524|
|Total FPR Opt 0.4 Pct|800|535|1’518|2’403|3’114|
|Beta no detection|358|89|475|588|679|
|Beta FPR 0.4 Pct|293|81|400|504|585|
|Beta FPR Opt 0.4 Pct|206|65|291|376|442|
|GPD no detection|773|537|1’455|2’512|4’000|
|GPD FPR 0.4 Pct|634|484|1’251|2’248|3’450|
|GPD FPR Opt 0.4 Pct|81|91|207|361|489|
|Mass attack no detection|892|903|2’029|3’635|4’826|
|Mass attack FPR 0.4 Pct|732|743|1’690|2’983|3’920|
|Mass attack FPR Opt 0.4 Pct|514|523|1’199|2’100|2’799|

Total represents the risk figures for all three distributions generalised Pareto (GPD), Beta and mass attack

For each sub-model, the loss is calculated by pulling the event frequency for the year according to the Poisson intensity, loss magnitude according to the marginal distribution, and stochastic recovery:

where Rec denotes recovery function. Simulated loss figures were obtained by simulating the nested overall model, from which the risk statistics could be calculated empirically. Juniper Research (2020) estimated the recovery rate as 18%.


---

[previous part](text-001.md) | [source overview](overview.md) | [next part](text-003.md)

[^original]: Paolo Vanini, Sebastiano Rossi, Ermin Zvizdic, Thomas Domenig, "Online payment fraud: from anomaly detection to risk management" (2023-03-12). https://link.springer.com/article/10.1186/s40854-023-00470-w
