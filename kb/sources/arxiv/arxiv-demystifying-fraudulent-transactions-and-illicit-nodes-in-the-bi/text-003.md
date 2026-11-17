---
type: Source Text
title: Demystifying Fraudulent Transactions and Illicit Nodes in the Bitcoin Network for Financial Forensics - part 3 of 4 (pp. 8-11)
description: 'Verbatim extracted text, pp. 8-11: Addresses per User: Max 14, 885; Addresses per User: Max 14, 885 > LSTMEC 0.665 0.350 0.459 0.946; Addresses per User: Max 14, 885 > RF+MLP+XGBAR 0.933 0.572 0.709 0.983; and 7 more sections'
resource: https://arxiv.org/abs/2306.06108
tags:
- academic_finding
- datasets_benchmarks
- global_academic
- network_graph
- preprint
- virtual_assets
status: stable
source_id: arxiv-demystifying-fraudulent-transactions-and-illicit-nodes-in-the-bi
issuer: arxiv
issuer_name: arXiv
jurisdictions:
- GLOBAL_ACADEMIC
tier: 3
instrument_type: preprint
normative_force: academic_finding
publication_date: '2023-05-25'
legal_status: unknown
part: 3
parts_total: 4
content_mode: full_text
generated:
  by: process:fincrime-kb-build
  at: '2026-11-17T12:21:45Z'
verified:
- by: process:kb-validate/verbatim-coverage
  at: '2026-11-17T12:21:45Z'
sources:
- id: original
  resource: https://arxiv.org/abs/2306.06108
  title: Demystifying Fraudulent Transactions and Illicit Nodes in the Bitcoin Network for Financial Forensics
  author: org:arxiv
  last_modified: '2023-05-25T00:00:00Z'
---

# Demystifying Fraudulent Transactions and Illicit Nodes in the Bitcoin Network for Financial Forensics

[previous part](text-002.md) | [source overview](overview.md) | [next part](text-004.md)

> Verbatim text extracted from the original (arXiv, 2023-05-25), part 3 of 4, pp. 8-11. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **academic finding**.[^original]

## Addresses per User: Max 14, 885


[p. 8] [ref: 5.2]

5.2 Model Evaluation and Analysis

have comparable precision and recall performance, 𝑅𝐹𝑇𝑋is better as the MCC values are 0.83 vs 0.81. Table 7 also shows the results of 2−and 3−classifier ensembles by selecting the top 3 models (RF, XGB, MLP). The best performing 2−and 3−classifier ensembles are those using Elliptic++. In comparison, the 𝐿𝑅, 𝑀𝐿𝑃𝐸𝐶, and 𝐿𝑆𝑇𝑀 models are ineffective with < 50% precision/recall (highlighted in red). Table 8 shows the results for the actors dataset. It is observed that 𝑅𝐹𝐴𝑅is the best-performing model (followed by 𝑋𝐺𝐵𝐴𝑅and 𝑀𝐿𝑃𝐴𝑅) with a precision of 91.1% and recall of 78.9%. Also, the best 2−and 3−classifier ensembles (𝑅𝐹+𝑋𝐺𝐵𝐴𝑅and 𝑅𝐹+𝑀𝐿𝑃+𝑋𝐺𝐵𝐴𝑅) show increases in precision (95.9%,93.3% vs 91.1%), but decreases in recall (53.0%,57.2% vs 78.9%), indicating the member models of 2−and 3−classifier ensembles are not complimentary and have high negative correlation [43]. The 𝐿𝑅𝐴𝑅and 𝐿𝑆𝑇𝑀𝐴𝑅models are ineffective with extremely low recall (highlighted in red).

5.3 EASY, HARD, and AVERAGE cases Analysis

Table 7 and Table 8 show the results of all models trained on the transactions dataset and the actors dataset respectively. From Ta- ble 7, the results for the transactions dataset in Elliptic++ (labelled TX) show an increase in performance in most of the metrics for all of the models, compared to the Elliptic dataset (labelled EC). This can be attributed to our addition of 17 augmented features to each transaction, which in turn improves the generalization performance and the explainability of both the transaction dataset and the fraud- ulent transaction detection models. It is observed that 𝑅𝐹𝑇𝑋is the

Table 7: Illicit transactions results using individual/ensemble of classifiers. EC refers to classification on Elliptic dataset [40], TX is on our Elliptic++ transactions dataset.

Model Precision Recall F1 Score Micro-F1

To further understand the performance of RF models against other models, and the performance results of their best performing 2− and 3−classifier ensembles, we analyze their performance in terms of the EASY, HARD, and AVERAGE cases as defined in Section 4.3. Table 9 (shown on the next page) provides a temporal split of the classification results across the test time steps of 35 to 49 for the EASY case, HARD case, and AVERAGE case respectively. It is important to note that AVERAGE cases present the opportunities for further optimizations. For the AVERAGE cases (correct classification by 1 ≤ 𝑥≤4 models), all combinations are shown for each individual model, for the 2/3 models scenario we show top 2 combinations, and for the 4 models scenario we show top 1 combination. First, the case where the 4 models RF, MLP, XGB, and LR correctly classify the transaction accounts for 71% of the AVERAGE cases. Second, the cases where RF classifies incorrectly only make up for < 1% of the AVERAGE cases. This motivates us to focus on optimization of the RF model with feature refinement.

### LSTMEC 0.665 0.350 0.459 0.946


[pp. 8-9]

Table 8: Illicit actors results using individual/ensemble of classifiers. AR is classification on our Elliptic++ actors dataset.

Model Precision Recall F1 Score Micro-F1

2 classifiers ensemble, selecting top 3 classifiers

2 classifiers ensemble, selecting top 3 classifiers

3 classifiers ensemble, selecting top 3 classifiers

3 classifiers ensemble, selecting top 3 classifiers

Demystifying Fraudulent Transactions and Illicit Nodes in the Bitcoin Network for Financial Forensics KDD ’23, August 6–10, 2023, Long Beach, CA, USA

Table 9: Classification results on the testing dataset showing distributions of EASY, HARD, AVERAGE cases among time steps 35 to 49. Total of each case is 49, 243, and 791 respectively. For the AVERAGE case, distributions are shown for cases where only 1 model (all shown), only 2 models (top 2 shown), only 3 models (top 2 shown), and only 4 models (top 1 shown) classified correctly.

### RF+MLP+XGBAR 0.933 0.572 0.709 0.983


[p. 9]

Time Step 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 TOTAL

Figure 11: Top 10 and bottom 10 features for the transactions dataset (left) and actors dataset (right).

Addr Interactions (total)

Local feature 53 Local feature 55

Block First Sent

Fees (median)

Fees (max) Fees (mean)

size Local feature 47 Local feature 76 Local feature 14 Aggregate feature 39

Block Last Block First

Local feature 49 num output addresses

Local feature 52

### RF,MLP,XGB,LR 124 24 12 57 45 55 81 159 0 1 0 1 0 0 0


[ref: 5.4]

Fees (min) Fees (total) Block First Receive

Blocks Input (median) Addr Interactions (mean)

Blocks Output (mean)

Local feature 36 Local feature 51 Local feature 34 Local feature 69 Aggregate feature 42

Blocks Input (total) Addr Interactions (max)

Blocks Input (median)

Local feature 38 Local feature 39

Importance

Importance

Local feature 7 Local feature 70 Local feature 15

Blocks Input (min) Blocks Output (min) Addr Interactions (min) Addr Interactions (median)

0 0.01 0.02 0.03 0.04 0.05 0.06

0 0.01 0.02 0.03 0.04 0.05 0.06 0.07 0.08 0.09 0.1

(a) Transactions dataset.

(b) Actors dataset.

5.4 Model Optimization by Feature Refinement

Table 10: Illicit transactions classification results using se- lected features, labelled as𝜓, Micro-F1 denotes Micro-Avg F1.

Model Precision Recall F1 Score Micro-F1

### RFTX 0.975 0.719 0.828 0.980


RFTX𝜓 0.986 0.727 0.836 0.981

RF+XGBTX𝜓 0.987 0.717 0.826 0.980

RF+MLP+XGBTX𝜓 0.968 0.729 0.834 0.980

Given that the RF is the best performing model, we explore fea- ture refinement to further optimize RF. By examining the results from decision trees, we combine feature importance, permutation feature importance, and drop column feature importance to show the top 10 and bottom 10 features by importance on both transac- tions dataset and actors dataset, as shown in Figure 11a for TX and Figure 11b for AR. For the transactions dataset, the 17 augmented features produced a collective 12% importance, with the transaction size feature alone responsible for 4.1%. For the actors dataset, 35% of the features were responsible for 80% of the importance, with the total address interaction as the most important feature. Inter- estingly, a connection can be made to the set of top and bottom 10 features with the features highlighted in Figure 8. It can be seen that there is a link from the green highlight to the top 10 features, and likewise with the red highlight and bottom 10 features. This solidifies that features providing visual proof of the risk attribute to a larger classification importance, and vice versa. The top and bottom 2 of each feature type in both datasets are included in the Appendix Section A.5 for reference. Using this analysis, we run

### RF+MLP+XGBTX 0.962 0.723 0.826 0.980


[pp. 9-10]

the best 1−/2−/3−classifiers ensembles with selected features in- stead of the full set of features. Tables 10 and 11 show the model performance results for transactions and wallet addresses (actors) respectively. Interestingly, the feature refined models show an av- erage improvement of 0.92%, 1.17%, and 0.89% for precision, recall, and F1 score respectively on the transactions dataset, and similarly 1.07%, 3.1%, and 1.13% on the actors dataset.

Table 11: Illicit actors classification results using selected fea- tures, labelled as 𝜓and compared with AR. Micro-F1 denotes Micro-Avg F1.

Model Precision Recall F1 Score Micro-F1

### RFAR 0.911 0.789 0.845 0.990


[p. 10]

RFAR𝜓 0.921 0.802 0.858 0.990

The increase in recall is also evident in the RF trees voting. Fig- ures 12a and 12b show the cumulative votes of 50 RF trees for 9 cho- sen transactions/addresses before (left) and after (right) selecting im- portant features for both the transactions and actors datasets respec- tively. This demonstrates a trend that when some non-contributing features are dropped, those transactions/addresses that are close to the correct manifold in classification will in turn be classified correctly by more trees, increasing in the number of correct votes.

### RF+XGBAR 0.959 0.530 0.682 0.982


RF+XGBAR𝜓 0.967 0.543 0.686 0.982

Figure 12: Cumulative votes for 50 RF trees for (a) chosen transactions and (b) addresses before (left) and after (right) feature selection and refinement.

Correct Incorrect

RF+MLP+XGBAR𝜓 0.945 0.601 0.718 0.984

22 28

29 21

21 29

28 22

16 34

26 24

15 35

21 29

14 36

21 29

### RF+MLP+XGBAR 0.933 0.572 0.709 0.983


13 37

13 37

time series of selected transaction features, and the time series of account features over the time steps of the Elliptic++ dataset.

Transaction ID

11 39

23 27

10 40

21 29

8 42

6 44

0 10 20 30 40 50

Number of RF tree votes

0 10 20 30 40 50 Number of RF tree votes

(a) Transactions dataset.

Correct Incorrect

112dD...

23 27

34 16

12Utp...

22 28

29 21

1BBpn...

22 28

29 21

1BEfK...

20 30

26 24

1EhxE...

17 34

24 26

1Q25N...

15 35

22 28

Wallet Address

1Ptt2...

14 36

24 26

18AN3...

13 37

17 33

14snt...

13 37

12 38

0 10 20 30 40 50

Number of RF tree votes

0 10 20 30 40 50 Number of RF tree votes

(b) Actors dataset.

### 6 CONCLUDING REMARKS


Third, to further improve the accuracy of the ML algorithms for detecting fraudulent transactions and illicit accounts, we employ ensemble methods to improve the generalization performance of individual ML algorithms. We study ensemble learning with two and three member models, with detailed analysis on the effective- ness of ensemble methods through EASY, HARD and AVERAGE cases. Motivated by our ensemble learning analysis, we show that model training using selective features instead of all extracted features of transactions and of addresses can further improve RF precision and recall performance by 0.92% and 1.17% respectively for the transac- tions dataset, and 1.07% and 3.1% respectively for the actors dataset. The combination of ensembles and importance-based feature prun- ing not only demonstrates the utility of the Elliptic++ dataset for fraud detection in Bitcoin network, but also showcases the im- portance of root cause analysis of fraudulent activities through semantic and statistical explainability of ML algorithms.

With the rapid growth of the cryptocurrency ecosystem, there is a growing demand for robust financial forensics on the blockchain networks. This paper makes three original contributions.

First, we collect and contribute the Elliptic++ dataset, combining over 203k transactions and 822k addresses, and providing four graph representations (Money Flow Transaction Graph, Actor Interaction Graph, Address-Transaction Graph, User Entity Graph) that allow for mining and visualizations of connections for anomaly detection. This enables the detection of both illicit transactions and illicit accounts in Bitcoin networks.

The Bitcoin blockchain is the first and the largest cryptocur- rency network, boasting as the most widely used cryptocurrency. We believe that the methodology used for collecting the Elliptic++ dataset and the approach developed to exhibit the utilities of this dataset for fraud detection in Bitcoin network can be leveraged to analyze other types of currencies and blockchain networks, includ- ing Monero, ZCash, and Ethereum, to name a few. Moreover, the graph representations and the use of time series representations of transaction/account features over the time steps provides guidelines for developing financial forensics models that can be beneficial to other blockchains with high performance and explainability.

The Elliptic++ dataset and its tutorials are made publicly avail- able at https://www.github.com/git-disl/EllipticPlusPlus. We conjecture that making this dataset publicly available will enable the applied data science researchers to conduct financial forensics on the Bitcoin cryptocurrency network and develop more effective fraud detection models and algorithms.

[pp. 10-11]

Second, we leverage the four unique graph representations to showcase the fraud detection of illicit transactions, illicit actors (wallet addresses), and the risks of de-anonymization of users using clustering of addresses. We demonstrate the utility of the Elliptic++ dataset for detecting fraudulent transactions and illicit accounts using representative machine learning approaches, including Ran- dom Forest, Logistic Regression, Multilayer Perceptrons, LSTM, and Extreme Gradient Boosting. We analyze why Random Forest (RF) is the best-performing model for fraud detection, achieving 97.5% precision and 71.9% recall on the transactions dataset, and 91.1% precision and 78.9% recall on the actors dataset. We also provide comparative analysis of their performance and provide the explainability of the ML algorithms through visualization of all four types of graphs. In addition, we also provide explainability of the performance comparison through detailed analysis on the

Acknowledgement. This research is partially sponsored by the NSF CISE grants 2302720 and 2038029, an IBM faculty award (002114), and a CISCO edge AI grant (001927). Any opinions, findings, and conclusions or recommendations expressed in this material are those of the author(s) and do not necessarily reflect the views of the National Science Foundation or other funding agencies and companies mentioned above.

Demystifying Fraudulent Transactions and Illicit Nodes in the Bitcoin Network for Financial Forensics KDD ’23, August 6–10, 2023, Long Beach, CA, USA

[25] Joana Lorenz, Maria Inês Silva, David Aparício, João Tiago Ascensão, and Pedro

### REFERENCES


[p. 11]

[1] Rachit Agarwal, Shikhar Barve, and Sandeep Kumar Shukla. 2021. Detecting ma-

Bizarro. 2020. Machine learning methods to detect money laundering in the bitcoin blockchain in the presence of label scarcity. In Proceedings of the First ACM International Conference on AI in Finance. 1–8. [26] Sarah Meiklejohn, Marjori Pomarole, Grant Jordan, Kirill Levchenko, Damon

licious accounts in permissionless blockchains using temporal graph properties. Applied Network Science 6, 1 (2021), 1–30. [2] Ismail Alarab and Simant Prakoonwit. 2022. Graph-based lstm for anti-money

laundering: Experimenting temporal graph convolutional network with bitcoin data. Neural Processing Letters (2022), 1–19. [3] Ismail Alarab, Simant Prakoonwit, and Mohamed Ikbal Nacer. 2020. Comparative

McCoy, Geoffrey M Voelker, and Stefan Savage. 2013. A fistful of bitcoins: characterizing payments among men with no names. In Proceedings of the 2013 conference on Internet measurement conference. 127–140. [27] Patrick Monamo, Vukosi Marivate, and Bheki Twala. 2016. Unsupervised learning

for robust Bitcoin fraud detection. In 2016 Information Security for South Africa (ISSA). IEEE, 129–134. [28] Patrick M Monamo, Vukosi Marivate, and Bhesipho Twala. 2016. A multifaceted

analysis using supervised learning methods for anti-money laundering in bitcoin. In Proceedings of the 2020 5th International Conference on Machine Learning Technologies. 11–17. [4] Elli Androulaki, Ghassan O Karame, Marc Roeschlin, Tobias Scherer, and Srdjan

Capkun. 2013. Evaluating user privacy in bitcoin. In International conference on financial cryptography and data security. Springer, 34–51. [5] John O Awoyemi, Adebayo O Adetunmbi, and Samuel A Oluwadare. 2017. Credit

approach to Bitcoin fraud detection: Global and local outliers. In 2016 15th IEEE International Conference on Machine Learning and Applications (ICMLA). IEEE, 188–194. [29] Satoshi Nakamoto. 2008. Bitcoin: A peer-to-peer electronic cash system. Decen-

tralized Business Review (2008), 21260. [30] Catarina Oliveira, João Torres, Maria Inês Silva, David Aparício, João Tiago

card fraud detection using machine learning techniques: A comparative analysis. In 2017 international conference on computing networking and informatics (ICCNI). IEEE, 1–9. [6] Massimo Bartoletti, Barbara Pes, and Sergio Serusi. 2018. Data mining for de-

Ascensão, and Pedro Bizarro. 2021. GuiltyWalker: Distance to illicit nodes in the Bitcoin network. arXiv preprint arXiv:2102.05373 (2021). [31] Thai Pham and Steven Lee. 2016. Anomaly detection in bitcoin network using

tecting bitcoin ponzi schemes. In 2018 Crypto Valley Conference on Blockchain Technology (CVCBT). IEEE, 75–84. [7] Alex Biryukov, Dmitry Khovratovich, and Ivan Pustogarov. 2014. Deanonymisa-

unsupervised learning methods. arXiv preprint arXiv:1611.03941 (2016). [32] Thai Pham and Steven Lee. 2016. Anomaly detection in the bitcoin system-a

network perspective. arXiv preprint arXiv:1611.03942 (2016). [33] D. Dziubaltowska R. Michalski and P. Macek. 2020. Revealing the character of

tion of clients in Bitcoin P2P network. In Proceedings of the 2014 ACM SIGSAC Conference on Computer and Communications Security. 15–29. [8] Alex Biryukov and Sergei Tikhomirov. 2019. Deanonymization and linkability of

nodes in a blockchain with supervised learning. IEEE Access (2020). [34] Fergal Reid and Martin Harrigan. 2013. An analysis of anonymity in the bitcoin

cryptocurrency transactions based on network analysis. In 2019 IEEE European symposium on security and privacy (EuroS&P). IEEE, 172–184. [9] Christopher M Bishop and Nasser M Nasrabadi. 2006. Pattern recognition and

system. In Security and privacy in social networks. Springer, 197–223. [35] Jie Shen, Jiajun Zhou, Yunyi Xie, Shanqing Yu, and Qi Xuan. 2021. Identity

machine learning. Vol. 4. Springer. [10] Leo Breiman. 2001. Random forests. Machine learning 45, 1 (2001), 5–32. [11] Huiping Chen, Grigorios Loukides, Robert Gwadera, and Solon P Pissis. 2023.

inference on blockchain using graph neural network. In International Conference on Blockchain and Trustworthy Systems. Springer, 3–17. [36] Bingqiao Luo Shengliang Lu Bingsheng He Sihao Hu, Zhen Zhang and Ling

Liu. 2023. BERT4ETH: Pre-training of Transformer Encoder Representation for Ethereum Fraud Detection. In The Web Conference. May 2-4, 2023, Austin, TX). [37] Ka Ho Chow Fatih Ilhan Selim Tekin Sihao Hu, Tiansheg Huang and Ling Liu.

Heavy Nodes in a Small Neighborhood: Algorithms and Applications. In Pro- ceedings of the 2023 SIAM International Conference on Data Mining (SDM). SIAM, 307–315. [12] Tianqi Chen and Carlos Guestrin. 2016. Xgboost: A scalable tree boosting system.

2023. Etherum Account Profiling and De-anonymization via Pseudo-Siamese BERT. Technical Report, Georgia Tech (2023). [38] Xiaobing Sun, Wenjie Feng, Shenghua Liu, Yuyang Xie, Siddharth Bhatia, Bryan

In Proceedings of the 22nd acm sigkdd international conference on knowledge discovery and data mining. 785–794. [13] Weili Chen, Xiongfeng Guo, Zhiguang Chen, Zibin Zheng, and Yutong Lu. 2020.

Phishing Scam Detection on Ethereum: Towards Financial Security for Blockchain Ecosystem.. In IJCAI. 4506–4512. [14] Jason Hirshman, Yifei Huang, and Stephen Macke. 2013. Unsupervised ap-

Hooi, Wenhan Wang, and Xueqi Cheng. 2022. MonLAD: Money laundering agents detection in transaction streams. In Proceedings of the Fifteenth ACM International Conference on Web Search and Data Mining. 976–986. [39] Petar Veličković, Guillem Cucurull, Arantxa Casanova, Adriana Romero, Pietro

proaches to detecting anomalous behavior in the bitcoin transaction network. Technical report, Stanford University (2013). [15] Sepp Hochreiter and Jürgen Schmidhuber. 1997. Long short-term memory. Neural

Lio, and Yoshua Bengio. 2017. Graph attention networks. arXiv preprint arXiv:1710.10903 (2017). [40] Mark Weber, Giacomo Domeniconi, Jie Chen, Daniel Karl I Weidele, Claudio

computation 9, 8 (1997), 1735–1780. [16] David W Hosmer Jr, Stanley Lemeshow, and Rodney X Sturdivant. 2013. Applied

logistic regression. Vol. 398. John Wiley & Sons. [17] Yining Hu, Suranga Seneviratne, Kanchana Thilakarathna, Kensuke Fukuda,

Bellei, Tom Robinson, and Charles E Leiserson. 2019. Anti-money laundering in bitcoin: Experimenting with graph convolutional networks for financial forensics. arXiv preprint arXiv:1908.02591 (2019). [41] Jiajing Wu, Jieli Liu, Weili Chen, Huawei Huang, Zibin Zheng, and Yan Zhang.

and Aruna Seneviratne. 2019. Characterizing and detecting money laundering activities on the bitcoin network. arXiv preprint arXiv:1912.12060 (2019). [18] Thomas N Kipf and Max Welling. 2016. Semi-supervised classification with graph

2021. Detecting mixing services via mining bitcoin transaction network with hybrid motifs. IEEE Transactions on Systems, Man, and Cybernetics: Systems 52, 4 (2021), 2237–2249. [42] Jiajing Wu, Qi Yuan, Dan Lin, Wei You, Weili Chen, Chuan Chen, and Zibin

convolutional networks. arXiv preprint arXiv:1609.02907 (2016). [19] Philip Koshy, Diana Koshy, and Patrick McDaniel. 2014. An analysis of anonymity

Zheng. 2020. Who are the phishers? phishing scam detection on ethereum via network embedding. IEEE Transactions on Systems, Man, and Cybernetics: Systems (2020). [43] Yanzhao Wu, Ling Liu, Zhongwei Xie, Ka-Ho Chow, and Wenqi Wei. 2021. Boost-

in bitcoin using p2p network traffic. In International Conference on Financial Cryptography and Data Security. Springer, 469–485. [20] Oliver Kramer. 2016. Machine learning for evolution strategies. Vol. 20. Springer. [21] Sijia Li, Gaopeng Gou, Chang Liu, Chengshang Hou, Zhenzhen Li, and Gang

ing ensemble accuracy by revisiting ensemble diversity metrics. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 16469– 16477. [44] Masoumeh Zareapoor, Pourya Shamsolmoali, et al. 2015. Application of credit


---

[previous part](text-002.md) | [source overview](overview.md) | [next part](text-004.md)

[^original]: arXiv, "Demystifying Fraudulent Transactions and Illicit Nodes in the Bitcoin Network for Financial Forensics" (2023-05-25). https://arxiv.org/abs/2306.06108
