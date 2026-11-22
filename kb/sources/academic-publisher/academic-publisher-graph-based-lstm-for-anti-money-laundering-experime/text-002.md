---
type: Source Text
title: 'Graph-Based LSTM for Anti-money Laundering: Experimenting Temporal Graph Convolutional Network with Bitcoin Data - part 2 of 2 (pp. 11-19)'
description: 'Verbatim extracted text, pp. 11-19: Graph-Based LSTM for Anti-money Laundering: Experimenting Temporal Graph Convolutional Network with Bitcoin Data > 6 Experiments; Graph-Based LSTM for Anti-money Laundering: Experimenting Temporal Graph Convolutional Network with Bitcoin Data > 7 Results and Discussion; Graph-Based LSTM for Anti-money Laundering: Experimenting Temporal Graph Convolutional Network with Bitcoin Data > 8 Ablation Study; and 2 more sections'
resource: https://link.springer.com/article/10.1007/s11063-022-10904-8
tags:
- academic_finding
- academic_paper
- datasets_benchmarks
- global_academic
- network_graph
- virtual_assets
status: stable
source_id: academic-publisher-graph-based-lstm-for-anti-money-laundering-experime
issuer: academic_publisher
issuer_name: Academic publisher / repository
jurisdictions:
- GLOBAL_ACADEMIC
tier: 3
instrument_type: academic_paper
normative_force: academic_finding
publication_date: '2022-06-15'
legal_status: unknown
part: 2
parts_total: 2
content_mode: full_text
generated:
  by: process:fincrime-kb-build
  at: '2026-11-22T09:50:18Z'
verified:
- by: process:kb-validate/verbatim-coverage
  at: '2026-11-22T09:50:18Z'
sources:
- id: original
  resource: https://link.springer.com/article/10.1007/s11063-022-10904-8
  title: 'Graph-Based LSTM for Anti-money Laundering: Experimenting Temporal Graph Convolutional Network with Bitcoin Data'
  author: org:academic_publisher
  last_modified: '2022-06-15T00:00:00Z'
---

# Graph-Based LSTM for Anti-money Laundering: Experimenting Temporal Graph Convolutional Network with Bitcoin Data

[previous part](text-001.md) | [source overview](overview.md)

> Verbatim text extracted from the original (Academic publisher / repository, 2022-06-15), part 2 of 2, pp. 11-19. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **academic finding**.[^original]

## Graph-Based LSTM for Anti-money Laundering: Experimenting Temporal Graph Convolutional Network with Bitcoin Data


### 6 Experiments


#### 6.1 Experimental Setup


[pp. 11-12]

Using the Elliptic data, we split the data following the temporal split as in [3], so that the first 35 graphs (i.e., _t_ = 1 → _t_ = 35) account for the train set and the remaining are kept for testing. Since this dataset comprises partially labelled nodes, we only use the labelled nodes which add up for 29,894/16,670 transactions in the train/test sets, respectively. To train temporal-GCN, we use Pytorch Geometric (PyG) package [39] which is built on the top of Pytorch (version 1.11.0) enabled-CUDA (version 11.3) in Python programming language. At each time-step _t_ , we feed the relevant graph network with its node feature matrix (i.e., local features excluding timestep) to the temporal-GCN model that is summarised in Eq. 16. LSTM layer uses only the nodes features without any graph-structural information to provide the output matrix _H__(_1_)_ _._ This matrix is then forwarded to 2-TAGCN layers (in _H__(_2_)_ and _H__(_3_)_ ) that consider the graph-structured data of the top-K influential nodes in the graph, where _K_ is kept by default equal to 3. Hence, a _Softmax_ function provides the final class predictions as licit/illicit transactions. We choose _NLLLoss_ function and Adam optimiser in order to compute the loss and update the model’s parameters. Using the same hyper-parameters from [5], the widths of the hidden layers are set to 50, the number of epochs is set to 50 and the learning rate is fixed at 0.001. Furthermore, we empirically opt 0.7 for the dropout ratio to avoid overfitting. The classification results of the temporal-GCN model are provided in Table 1.

Table 1 Classification results of Elliptic data using local features

[p. 12]

|Model|% Accuracy|% Precision|% Recall|%_F_1 Score|
|---|---|---|---|---|
|Temporal-GCN|97.7|92.7|71.3|80.6|
|GCN+MLP [5]|97.4|89.9|67.8|77.3|
|Evolve-GCN [3]|96.8|85.0|62.4|72.0|
|Skip-GCN [3]|96.6|81.2|62.3|70.5|
|Random Forest [3]|96.6|80.3|61.1|69.4|
|GCN [3]|96.1|81.2|51.2|62.8|
|MLP [3]|95.8|63.7|66.2|64.9|
|Logistic regression [3]|92.0|34.8|66.8|45.7|

This table shows comparison between the presented model “Temporal-GCN” and previous studies using same features and train/test split

#### 6.2 Active Learning


Active learning has a significant impact to alleviate the bottleneck of labelling especially with this type of data. The main goal of active learning is to use less-training data with achieving acceptable performance. Here, we initially assume the train set as a pool of unlabelled data _D pool_ and we consider _Dtrain_ as an empty set to be appended after the querying process. First, the process starts by randomly querying the first batch size for manual labelling, which is arbitrarily assigned to 2000 instances. Afterwards, we append the selected queries to _Dtrain_ from _D pool_ to train the temporal-GCN model that is evaluated using the test set at each iteration. Subsequently, the same process is repeated using the uncertainty sampling strategy until we reach an adequate accuracy. However, we query for all instances in _D pool_ . The uncertainty sampling is performed by using one of the acquisition functions demonstrated earlier. These acquisition functions require as input the uncertainty estimates derived by the uncertainty estimation methods. To imitate manual labelling, we append the labels to the queried instances. This experiment is performed using MC-dropout and MC-AA. We compare the performance of the active learning frameworks that use various acquisition functions on the two distinct uncertainty estimation methods. Regarding the hyper-parameters for producing uncertainty estimates, we arbitrarily set _T_ = 50 for multiple stochastic forward passes on the unlabelled pool for MC-dropout. With MC-AA, we arbitrarily choose _εT_ = 0 _._ 1 and _T_ = 10.

Inaddition,weperformrandomsamplingasabaselinewhichuniformlyqueriesdatapoints at random from the pool. The process of performing active learning with the temporal-GCN model is schematised in Fig. 2. The required time to perform the active learning process in an end-to-end fashion using parallel processing, referring to Fig. 2, is provided in Table 2 using various acquisition functions under the given uncertainty methods.

### 7 Results and Discussion


[pp. 12-13]

We discuss the results of the temporal-GCN model in the light of the previous studies using the same dataset. Subsequently, we provide and discuss the results provided by various active learning frameworks. Then we apply a non-parametric statistical method to discuss

Fig. 2 Schematic representation of the active learning framework using the proposed temporal-GCN model. This frame is a pool-based scenario where annotator queries the data points labels from a pool of unlabelled instances, _D pool_ using an acquisition function. For each iteration, the queried batch is appended to the train set _Dtrain_

Table 2 Time required to perform the active learning process in an end-to-end fashion using the proposed temporal-GCN model

|Acquisitionfunction|Runtime (mins) usingMC-AA|Runtime (mins)using MC-dropout|
|---|---|---|
|BALD|t_MC_−_AA_ =28.07|t_MC_ −_dropout_=27.1|
|Entropy|t_MC_−_AA_ =28.9|t_MC_ −_dropout_=27.3|
|Variation ratio|t_MC_−_AA_ =28.9|t_MC_ −_dropout_=28.3|
|Mean STD|t_MC_−_AA_ =28.68|t_MC_ −_dropout_=27.09|

The time is provided for each experiment that uses the corresponding acquisition function which relies on a given uncertainty estimation method

the significant difference between MC-AA and MC-dropout in performing active learning in comparison to the random sampling strategy.

#### 7.1 Performance of Temporal-GCN


[pp. 13-14]

Temporal-GCN has outperformed all previous studies on this dataset that uses local features under the same train/test split settings. The presented model has leveraged temporal sequence and the graph structure of the Bitcoin transaction graph, wherein the classification model can detect illicit transactions with accuracy and _f_ 1-score equal to 97.77% and 80.60%, respectively. In previous studies, Evolve-GCN has attained an accuracy of 96.8%. The latter model has exploited the dynamicity of the graph by performing LSTM on the weights of the GCN layer, which outperformed GCN and skip-GCN without any temporal information. Whereas

Fig. 3 Illicit transactions distribution in test set over the time-steps. The blue curve represents the actual illicit labels, whereas the red curve represents the illicit predictions that are actually illicit labels by temporal-GCN

in temporal-GCN, LSTM has exploited the temporal sequence of Elliptic data itself before using any graph information in which the new transformed features are mapped non-linearly into the graph-based approach to perform graph convolutions in the vertex domain. Thus, the obtained input features of TAGCN model are enriched with the relevant temporal information. Similarly to [3], we also realise that the presented model performs poorly with the black market shutdown at time-step 43 as shown in Fig. 3. Regarding the time-complexity, the complexity of LSTM is about _O_ (4 _ndh_ ( _dx_ + 3 + _dh_ ), whereas 2-TAGCN layers have a linear complexity which is _O_ ( _n_ ). Consequently, the time-complexity of the temporal-GCN model becomes _O_ ( _n_ (4 _dh dx_ + 3 _dh_ + _dh_2+ 1)) at every epoch.

#### 7.2 Evaluation of Active Learning Frameworks


[pp. 14-15]

Referring to Fig. 4, we plot the results of various active learning frameworks using various acquisition functions (BALD, Entropy, Mean STD, Variation Ratio) which in turn utilise MCdropout and MC-AA uncertainty estimation methods. Moreover, we plot the performance of the baseline model using a random sampling strategy. In the first subplot, BALD has revealed a significant success under MC-AA and MC-dropout uncertainty estimates which active learning is effectively better than the random sampling model. With the remaining acquisition functions, MC-dropout has remarkably achieved a significant outperformance over MC-dropout and the random sampling model.

MC-AA that is utilised in entropy and variation ratio acquisition function has not performed better than random sampling. Furthermore, the active learning framework using the BALD acquisition function in Fig. 4 is capable of matching the performance of a fully supervised model after using 20% of the queried data. This amount of queried data belongs to the second iteration. In our experiments, MC-AA has been revealed to be a viable method as an uncertainty sampling strategy in an active learning approach with BALD and Mean STD acquisition functions. This is reasonable since the latter two methods estimate the uncertainty based on the severe fluctuations of the model’s predictions on a given input wherein MC-AA suits this type of uncertainty.

Fig. 4 Results of active learning using BALD via MC-dropout in comparison to BALD via MC-AA

Referring to Table 2, BALD acquisition has recorded the shortest time among other acquisition functions using MC-AA, where this framework has been processed in 28.07 minutes using parallel processing. Whereas the longest time by MC-AA is recorded by the entropy and variation ratio. For MC-dropout, the shortest time is recorded by Mean STD acquisition which is 27.09 min. Whereas the framework using variation ratio has revealed the longest time which is 28.3 min. We also note that the frameworks using MC-AA require more time than the ones using the MC-dropout method. This is due to the adversaries computed by MC-AA which requires more time.

#### 7.3 Wilcoxon Hypothesis Test


[pp. 15-16]

To show the statistical significance of the various acquisition functions that appeared in Fig. 4, we perform the non-parametric Wilcoxon signed-rank test [40]. It is used to test the null hypothesis between two paired samples based on the difference between their scores. Given two paired samples P = { _p_ 1 _,_ … _, pm_ } and Q = { _q_ 1 _,_ … _, qm_ }, then the absolute value of the difference between the samples.

This can be expressed as:

where _m_ is the number of samples of each set. In summary, this test accounts for the statistical difference between the sets P and Q. The Wilcoxon test compares a test statistic T to _Student’s t-distribution_ . To perform this test, we use the Wilcoxon function in sklearn [41]. Referring to

|Table 3Wilcoxon statistical testbetween the accuracy derived by|Acquisition|Wilcoxon (MC-AA,|Wilcoxon|
|---|---|---|---|
|MC-AA/MC-dropout withrespect to the random sampling|function|random sampling)|(MC-dropout,random sampling)|
|model using various acquisition||||
|functions|BALD|0.0009|0.0217|
||Entropy|0.2552|0.309|
||Variation ratio|0.266|0.0071|
||Mean STD|0.5507|0.0112|

The values correspond to the _p_ values by the test statistic

Fig. 4, we apply the Wilcoxon test for each subplot twice. The first one studies the difference between MC-AA and random sampling curves. Likewise, the second one accounts for the differences between MC-dropout and random sampling curves. For instance, we will refer to the Wilcoxon test applied between MC-AA and random sampling pairs as follows:

p - value = Wilcoxon _(_ MC − AA _,_ Random Sampling _),_

where _p value_ is a statistical measurement that is used to validate how likely the difference of the paired samples is given by the null hypothesis. Let _H_ 0 be the null hypothesis and _H_ 1 be the alternative one. Then they can be written as:

[p. 16]

We opt for 0.05 for the significance level _α_ where we test against the null hypothesis. The smaller the _p_ value by the Wilcoxon function output, the evidence we have against the null hypothesis. Precisely, the test statistic is statistically significant if _p_ value is less than the significance level. Subsequently, we provide the statistical results ( _p_ values) of the various acquisition functions against the baseline random sampling. The results are provided in Table 3. The _p_ values—which are lower than the significance level _α_ —from BALD acquisition function are statistically significant against the null hypothesis in which there is statistical evidence about the difference between each of MC-AA and MC-dropout in comparison to random sampling acquisition. Moreover, MC-dropout against random sampling has shown a statistical significance against the null hypothesis using the variation ratio and Mean STD acquisitions where the _p_ values are 0.071 and 0.0112, respectively. There is no evidence against the null hypothesis for the entropy where the _p_ values are 0.2552 and 0.309 are greater than _α_ .

### 8 Ablation Study


[pp. 16-17]

In this section, we present the ablation studies performed on the proposed temporal-GCN model. Referring to Table 4, we have studied the importance of using LSTM and TAGCN layers. The Model-0 corresponds to the model performed in the experiments. Subsequently, we have applied a combination of replacing each of the given layers with a linear layer (Model-1, Model2, Model-3). We have also studied the case in which we remove one of the first two layers from the original model (Model-6, Model-7). Furthermore, we have shown the performance of the models using either LSTM (Model-4) with linear layers. In Model-2, the replacement of the second layer with a linear layer has attained the highest

Table 4 Ablation study over the layers of the proposed model

|Model number|Layer-1|Layer-2|Layer-3|% Accuracy|
|---|---|---|---|---|
|Model-0 (ours)|LSTM|TAGConv|TAGConv|97.77|
|Model-1|Linear|TAGConv|TAGConv|97.66|
|Model-2|LSTM|Linear|TAGConv|97.76|
|Model-3|LSTM|TAGConv|Linear|97.57|
|Model-4|LSTM|Linear|Linear|97.44|
|Model-5|Linear|Linear|Linear|97.51|
|Model-6|LSTM|TAGConv|None|97.63|
|Model-7|TAGConv|TAGConv|None|96.65|

Each model number is provided by its architecture by changing the layers into linear layer or removing one of the layers. The term’None’ in the cells correspond to the model having one of its layers removed

|Table 5Ablation study bychanging the number of K-hops|TAGCN K-hops|% Accuracy|
|---|---|---|
|in TAGCN layers of the|||
|temporal-GCN model as given in|K=3|97.77|
|Eq.16|K=2|97.71|
||K=1|97.75|

[p. 17]

accuracy in comparison to Model-0. The removal of LSTM in all cases has provided a drop in the model’s performance, especially in Model-7 which reveals the lowest accuracy. On the other hand, using LSTM without the graph learning algorithms in Model-2 has recorded the second-lowest accuracy in this study. We have also tweaked the K hyper-parameter that appeared in TAGCN referring to Eq. 15. The original model uses, by default, K=3 which means that neighbourhood information is aggregated up to 3-hops. Then we have checked the performance for K ∈ {1, 2} as provided in Table 5. The highest accuracy has been recorded for using _K_ = 3 and the second one for _K_ = _1_ . Surprisingly, the drop in accuracy is not consistent between the different _K-_ values. This might be due to the informative features derived from neighbouring nodes up to 1-hop and 3-hops.

### 9 Conclusion


[pp. 17-18]

For anti-money laundering in Bitcoin, we have presented temporal-GCN, as a combination of LSTMandGCNmodels,todetectillicittransactionsintheBitcointransactiongraphknownas Elliptic data. Also, we have provided active learning using two promising methods to compute uncertainties called MC-dropout and MC-AA. For the active learning frameworks, we have studied various acquisition functions to query the labels from the pool of unlabelled data points. The main finding is that the proposed model has revealed a significant outperformance incomparisontothepreviousstudieswithanaccuracyof97.77%underthesameexperimental settings. LSTM takes into consideration the temporal sequence of Bitcoin transaction graphs, whereas TAGCN considers the graph-structured data of the top-K influential nodes in the graph. Regarding active learning, we are able to achieve an acceptable performance by only

considering 20% of the labelled data with the BALD acquisition function. Moreover, a nonparametric statistical method, the so-called Wilcoxon test, is performed to test whether there is a difference between the type of uncertainty estimation method used in the active learning frameworks under the same acquisition function. Furthermore, an ablation study is provided to highlight the effectiveness of the proposed temporal-GCN.

In future work, we foresee performing different active learning frameworks which utilise different acquisition functions. Furthermore, we seek to extend the temporal-GCN model to other graph-structured datasets for anti-money laundering in blockchain.

Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by/4.0/.

### References


[p. 18]

1. Ciphertrace (2020) spring 2020 cryptocurrency crime and anti-money laundering report. https:// ciphertrace.com/spring-2020-cryptocurrency-anti-money-laundering-report/. Accessed 2021-09-01

2. Harlev MA, Sun Yin H, Langenheldt KC, Mukkamala R, Vatrapu R (2018) Breaking bad: de-anonymising entity types on the bitcoin blockchain using supervised machine learning. In: Proceedings of the 51st Hawaii International Conference on System Sciences

3. Weber M, Domeniconi G, Chen J, Weidele DKI, Bellei C, Robinson T, Leiserson CE (2019) Anti-money laundering in bitcoin: experimenting with graph convolutional networks for financial forensics. arXiv preprint arXiv:1908.02591

4. Alarab I, Prakoonwit S, Nacer MI (2020) Comparative analysis using supervised learning methods for anti-money laundering in bitcoin. In: Proceedings of the 2020 5th international conference on machine learning technologies, pp 11–17

5. Alarab I, Prakoonwit S, Nacer MI (2020) Competence of graph convolutional networks for anti-money laundering in bitcoin blockchain. In: Proceedings of the 2020 5th international conference on machine learning technologies, pp 23–27

6. Pareja A, Domeniconi G, Chen J, Ma J, Suzumura T, Kanezashi H, Kaler T, Schardl T, Leiserson C (2020) Evolvegcn: evolving graph convolu- tional networks for dynamic graphs. In: Proceedings of the AAAI conference on artificial intelligence, vol 34, pp 5363–5370

7. Poursafaei F, Rabbany R, Zilic Z (20201) Sigtran: signature vectors for detecting illicit activities in blockchain transaction networks. In: PAKDD (1). Springer, pp 27–39

8. Alarab I, Prakoonwit S, Nacer MI (2021) Illustrative discussion of mc-dropout in general dataset: uncertainty estimation in bitcoin. Neural Process Lett 53(2):1001–1011

9. Lorenz J, Silva MI, Apar´ ıcio D, Ascens˜ao JT, Bizarro P (2020) Machine learning methods to detect money laundering in the bitcoin blockchain in the presence of label scarcity. arXiv preprint arXiv:2005. 14635

10. Gal Y, Ghahramani Z (2016) Dropout as a bayesian approximation: represent ing model uncertainty in deep learning. In: international conference on machine learning. PMLR, pp 1050–1059

[pp. 18-19]

11. Alarab I, Prakoonwit S (2021) Adversarial attack for uncertainty estimation: identifying critical regions in neural networks. arXiv:2107.07618

12. Farrugia S, Ellul J, Azzopardi G (2020) Detection of illicit accounts over the ethereum blockchain. Expert Syst Appl 150:113318

13. Settles B (2009) Active learning literature survey

14. Qiu J, Wu Q, Ding G, Xu Y, Feng S (2016) A survey of machine learning for big data processing. EURASIP J Adv Signal Process 2016(1):1–16

15. Lewis DD, Catlett J (1994) Heterogeneous uncertainty sampling for supervised learning. In: Machine learning proceedings 1994. Elsevier, pp 148–156

16. Settles B, Craven M, Ray S (2007) Multiple-instance active learning. In: Advances in neural information processing systems, vol 20

17. Gal Y, Islam R, Ghahramani Z (2017) Deep Bayesian active learning with image data. In: International conference on machine learning. PMLR, pp 1183–1192

18. Gal Y, Hron J, Kendall A (2017) Concrete dropout. arXiv preprint arXiv:1705.07832 19. Shannon CE (1948) A mathematical theory of communication. Bell Syst Tech J 27(3):379–423 20. Houlsby N, Husz´ar F, Ghahramani Z, Lengyel M (2011) Bayesian active learning for classification and preference learning. arXiv preprint arXiv:1112.5745

21. Johnson EH (1966) Freeman: elementary applied statistics: for students in behavioral science (book review). Soc Forces 44(3):455

22. KendallA,BadrinarayananV,CipollaR(2015)Bayesiansegnet:modeluncer-taintyindeepconvolutional encoder-decoder architectures for scene under- standing. arXiv preprint arXiv:1511.02680

23. Kampffmeyer M, Salberg A-B, Jenssen R (2016) Semantic segmentation of small objects and modeling of uncertainty in urban remote sensing images using deep convolutional neural networks. In: Proceedings of the IEEE conference on computer vision and pattern recognition workshops, pp 1–9

24. Gal Y (2016) Uncertainty in deep learning. Univ Camb 1(3):4 25. Srivastava N, Hinton G, Krizhevsky A, Sutskever I, Salakhutdinov R (2014) Dropout: a simple way to prevent neural networks from overfitting. J Mach Learn Res 15(1):1929–1958

[p. 19]

26. Chakraborty A, Alam M, Dey V, Chattopadhyay A, Mukhopadhyay D (2018) Adversarial attacks and defences: a survey. arXiv preprint arXiv:1810.00069

27. GoodfellowIJ,ShlensJ,SzegedyC(2014)Explainingandharnessingadversarialexamples.arXivpreprint arXiv:1412.6572

28. Lewis DD, Gale WA (1994) A sequential algorithm for training text classifiers. CoRR abs/cmplg/9407020. arXiv:cmp-lg/9407020. http://arxiv.org/abs/cmp-lg/9407020

29. Kirsch A, Van Amersfoort J, Gal Y (2019) Batchbald: Efficient and diverse batch acquisition for deep Bayesian active learning. Adv Neural Inf Process Syst 32:7026–7037

30. Hochreiter S, Schmidhuber J (1997) Long short-term memory. Neural Comput 9(8):1735–1780 31. Graves A, Mohamed A, Hinton G (2013) Speech recognition with deep recur- rent neural networks. In: 2013 IEEE international conference on acoustics, speech and signal processing. IEEE, pp 6645–6649

32. Srivastava N, Mansimov E, Salakhudinov R (2015) Unsupervised learning of video representations using lstms. In: International conference on machine learning. PMLR, pp 843–852

33. Sutskever I, Vinyals O, Le QV (2014) Sequence to sequence learning with neural networks. In: Advances in neural information processing systems, pp 3104–3112

34. Graves A (2013) Generating sequences with recurrent neural networks. arXiv preprint arXiv:1308.0850 35. Du J, Zhang S, Wu G, Moura JM, Kar S (2017) Topology adaptive graph convolutional networks. arXiv preprint arXiv:1710.10370

36. Defferrard M, Bresson X, Vandergheynst P (2016) Convolutional neural networks on graphs with fast localized spectral filtering. Adv Neural Inf Process Syst 29:3844–3852

37. Kipf TN, Welling M (2016) Semi-supervised classification with graph convolu tional networks. arXiv preprint arXiv:1609.02907

38. Seo Y, Defferrard M, Vandergheynst P, Bresson X (2018) Structured sequence modeling with graph convolutional recurrent networks. In: International conference on neural information processing. Springer, pp 362–373

39. Fey M, Lenssen JE (2019) Fast graph representation learning with pytorch geometric. arXiv preprint arXiv:1903.02428

40. Wilcoxon F (1945) Individual comparisons by ranking methods. Biom Bull 1(6):80–83 41. Pedregosa F, Varoquaux G, Gramfort A, Michel V, Thirion B, Grisel O, Blondel M, Prettenhofer P, Weiss R, Dubourg V et al (2011) Scikit-learn: machine learning in python. J MACH LEARN RES 12:2825–2830

Publisher’s Note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.


---

[previous part](text-001.md) | [source overview](overview.md)

[^original]: Ismail Alarab, Simant Prakoonwit, "Graph-Based LSTM for Anti-money Laundering: Experimenting Temporal Graph Convolutional Network with Bitcoin Data" (2022-06-15). https://link.springer.com/article/10.1007/s11063-022-10904-8
