---
type: Source Text
title: 'Tide: A Customisable Dataset Generator for Anti-Money Laundering Research - part 4 of 5 (pp. 26-33)'
description: 'Verbatim extracted text, pp. 26-33: LI (0.10%) HI (0.19%)'
resource: https://arxiv.org/abs/2603.01863
tags:
- academic_finding
- datasets_benchmarks
- global_academic
- network_graph
- preprint
status: stable
source_id: arxiv-tide-a-customisable-dataset-generator-for-anti-money-laundering
issuer: arxiv
issuer_name: arXiv
jurisdictions:
- GLOBAL_ACADEMIC
tier: 3
instrument_type: preprint
normative_force: academic_finding
publication_date: '2026-02-03'
legal_status: unknown
part: 4
parts_total: 5
content_mode: full_text
generated:
  by: process:fincrime-kb-build
  at: '2026-11-21T23:42:13Z'
verified:
- by: process:kb-validate/verbatim-coverage
  at: '2026-11-21T23:42:13Z'
sources:
- id: original
  resource: https://arxiv.org/abs/2603.01863
  title: 'Tide: A Customisable Dataset Generator for Anti-Money Laundering Research'
  author: org:arxiv
  last_modified: '2026-02-03T00:00:00Z'
---

# Tide: A Customisable Dataset Generator for Anti-Money Laundering Research

[previous part](text-003.md) | [source overview](overview.md) | [next part](text-005.md)

> Verbatim text extracted from the original (arXiv, 2026-02-03), part 4 of 5, pp. 26-33. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **academic finding**.[^original]

## LI (0.10%) HI (0.19%)


[pp. 26-27]

LightGBM 78.05 ± 3.61 70.47 ± 27.91 XGBoost 72.01 ± 0.50 85.12 ± 0.52

6 Conclusion

We presented Tide, a synthetic dataset generator that addresses the scarcity of accessible financial transaction data for

Anti-Money Laundering research. Unlike existing generators that model network topology while neglecting temporal

dynamics, Tide explicitly captures the interdependence between structural patterns and temporal characteristics,

enabling injection of complex typologies including high-frequency bursts, synchronised transactions, and U-turn flows.

The system produces deterministic, reproducible outputs through seed-based generation, and we release both the

generator and reference datasets as open-source resources for the research community.

Our evaluation across two dataset variants with differing illicit ratios (LI: 0.10%, HI: 0.19%) revealed condition-

dependent model rankings. LightGBM achieved the highest PR-AUC (78.05) in the low illicit ratio condition, while

XGBoost performed best (85.12) at higher fraud prevalence. The +GFP variants consistently underperformed their base

models, likely because generic graph features do not align with Tide’s specific fraud patterns. These divergent rankings

demonstrate that the reference datasets can meaningfully differentiate model capabilities across operational conditions.

Limitations. The current work has several limitations that should be acknowledged. First, we did not disaggregate

performance by pattern type, so it remains unclear whether certain typologies (e.g., U-turn vs. rapid fund movement)

favour different architectures or present varying levels of detection difficulty.

Second, while Tide addresses key gaps in existing generators, the implemented pattern library covers only five

laundering typologies. Real-world money laundering encompasses a broader, and more complex spectrum of schemes,

including trade-based laundering, real estate manipulation, and cryptocurrency mixing, and more, which are not yet

modelled.

Third, our transaction amount and frequency calibrations are derived primarily from U.S. sources (Federal Reserve

Payments Study, Bureau of Labor Statistics), which may limit generalisability to financial systems with substantially

different transaction profiles. Similarly, the risk scoring weights, while grounded in regulatory literature, represent

simplified approximations of the complex factors that determine actual laundering risk.

Fourth, the absence of ground-truth validation against real financial data (an inherent constraint given privacy and

legal barriers) means we cannot directly verify that the synthetic patterns reflect the statistical signatures of actual

laundering schemes. The evaluation relies on the assumption that patterns derived from regulatory typologies are

representative.

Future Work. Several directions merit further investigation. Extending the pattern library to include additional

laundering typologies would broaden Tide’s applicability. Disaggregating model performance by pattern type would

clarify which architectures are best suited for detecting specific laundering behaviours.

The integration of Temporal Graph Networks (TGNs), which explicitly model time-evolving graph structure, rep-

[p. 27]

resents a promising avenue given Tide’s emphasis on temporal dynamics. Additionally, incorporating adversarial

pattern generation, where laundering schemes evolve in response to detection models, could produce more challenging

benchmarks that better simulate the adaptive nature of financial crime.

Future work could also explore cross-institutional scenarios with multiple financial networks, enabling research on

information-sharing protocols and federated detection approaches. Finally, establishing a community-driven pattern

repository, where researchers contribute new typologies with formal structural and temporal specifications, would

extend the generator’s utility beyond the patterns we have implemented.

References

[1] 2014. Typologies and Case Studies Report 2014. Technical Report. Australian Transaction Reports and Analysis Centre (AUSTRAC), Canberra,

Australia. https://www.austrac.gov.au/sites/default/files/2019-07/typologies-report-2014.pdf Accessed: 2025-05-19. [2] 2022. National Money Laundering Risk Assessment. Technical Report. U.S. Department of the Treasury. https://home.treasury.gov/system/files/136/

2022-National-Money-Laundering-Risk-Assessment.pdf Published February 2022. [3] 2023. Money Laundering Typologies. Technical Report. Joint Financial Crimes Unit and Financial Intelligence Unit. https://www.jerseyfsc.org/

media/6419/typologies-booklet-2023.pdf Accessed: 2025-05-23. [4] ADP, LLC. 2025. ADP PAY History Dataset (U.S. Wage Data). https://adp-ri-nrip-static.adp.com/artifacts/us_wage/20251203/ADP_PAY_history.zip.

Accessed: 2025-06-15; dataset containing U.S. wage history. [5] Ismail Alarab, Simant Prakoonwit, and Mohamed Ikbal Nacer. 2020. Competence of Graph Convolutional Networks for Anti-Money Laundering in

Bitcoin Blockchain. https://www.researchgate.net/publication/343301363_Competence_of_Graph_Convolutional_Networks_for_Anti-Money_ Laundering_in_Bitcoin_Blockchain. Accessed: 2025-06-15. [6] Erik Altman et al. 2023. Realistic Synthetic Financial Transactions for Anti-Money Laundering Models. In Proceedings of the 37th International

Conference on Neural Information Processing Systems. arXiv:2306.16424. [7] Australian Transaction Reports and Analysis Centre (AUSTRAC). 2019. Typologies Paper: AUSTRAC Money Laundering and Terrorism Financing

Indicators. https://www.austrac.gov.au/business/how-comply-guidance-and-resources/guidance-resources/typologies-paper-austrac-money- laundering-and-terrorism-financing-indicators Accessed: 2025-05-20.

[p. 28]

[8] Marco Bee. 2022. On discriminating between lognormal and Pareto tail: an unsupervised mixture-based approach. Advances in Data Analysis and

Classification (2022). doi:10.1007/s11634-022-00497-4 [9] Abdullahi Usman Bello and Jackie Harvey. 2017. From a Risk-Based to an Uncertainty-Based Approach to Anti-Money Laundering Compliance.

Security Journal 30, 1 (2017), 24–38. doi:10.1057/s41284-016-0002-0 Published online 9 June 2016. [10] Board of Governors of the Federal Reserve System. 2023. The Federal Reserve Payments Study: 2022 Triennial Initial Data Release. Technical Report.

Federal Reserve System. https://www.federalreserve.gov/paymentsystems/2023-April-The-Federal-Reserve-Payments-Study.htm [11] David R. Burton and Norbert J. Michel. 2021. Proposals to Foster Economic Growth and Capital Formation. Policy Submission to the U.S. Senate

Banking Committee. The Heritage Foundation, Washington, DC. https://www.banking.senate.gov/imo/media/doc/David%20Burton%20and% 20Norbert%20Michel%20-%202021-3-18.pdf Submitted in response to Ranking Member Toomey’s request for proposals. [12] Gabriele Corso, Luca Cavalleri, Dominique Beaini, Pietro Liò, and Petar Veličković. 2020. Principal Neighbourhood Aggregation for Graph Nets. In

Advances in Neural Information Processing Systems (NeurIPS 2020). https://arxiv.org/pdf/2004.05718 arXiv:2004.05718. [13] Bruno Deprez, Wei Wei, Wouter Verbeke, Bart Baesens, Kevin Mets, and Tim Verdonck. 2025. Advances in Continual Graph Learning for Anti-Money

Laundering Systems: A Comprehensive Review. arXiv preprint arXiv:2503.24259 (2025). https://arxiv.org/pdf/2503.24259 Preprint. [14] Martin Ester, Hans-Peter Kriegel, Jörg Sander, and Xiaowei Xu. 1996. A Density-Based Algorithm for Discovering Clusters in Large Spatial

Databases with Noise. In Proceedings of the Second International Conference on Knowledge Discovery and Data Mining (KDD-96). AAAI Press, 226–231. https://www.aaai.org/Papers/KDD/1996/KDD96-037.pdf [15] Ronen Fluss, David Faraggi, and Benjamin Reiser. 2005. Estimation of the Youden Index and its associated cutoff point. Biometrical Journal: Journal

of Mathematical Methods in Biosciences 47, 4 (2005), 458–472. [16] Forrester Consulting. 2023. True Cost of Financial Crime Compliance Study, 2023: United States and Canada. Technical Report. LexisNexis Risk

Solutions. https://risk.lexisnexis.com/insights-resources/research/true-cost-of-financial-crime-compliance-study-for-the-united-states-and- canada Commissioned study conducted by Forrester Consulting on behalf of LexisNexis Risk Solutions. [17] Oscar M. Granados and Andrés Vargas. 2022. The Geometry of Suspicious Money Laundering Activities in Financial Networks. EPJ Data Science 11,

6 (2022). doi:10.1140/epjds/s13688-022-00318-w Open Access. [18] Jing He, Jiao Tian, Yuanyuan Wu, Xinyi Cia, Kai Zhang, Mengjiao Guo, Hui Zheng, Junfeng Wu, and Yimu Ji. 2021. An Efficient Solution to Detect

Common Topologies in Money Launderings Based on Coupling and Connection. IEEE Intelligent Systems 36, 1 (2021), 64–74. doi:10.1109/MIS.2021. 3057590 [19] Angela Samantha Maitland Irwin, Kim-Kwang Raymond Choo, and Lin Liu. 2012. Modelling of Money Laundering and Terrorism Financing

Typologies. Journal of Money Laundering Control 15, 3 (2012), 316–335. doi:10.1108/13685201211238061 Published July 2012. [20] Rasmus Jensen and Alexandros Iosifidis. 2022. Fighting Money Laundering with Statistics and Machine Learning. arXiv preprint arXiv:2201.04207

(2022). https://arxiv.org/abs/2201.04207 Peer-reviewed literature survey. [21] Rasmus Ingemann Tuffveson Jensen, Joras Ferwerda, Kristian Sand Jørgensen, Erik Rathje Jensen, Martin Borg, Morten Persson Krogh, Jonas Brun-

holm Jensen, and Alexandros Iosifidis. 2023. A synthetic data set to benchmark anti-money laundering methods. Scientific Data 10, 1 (sep 2023), 661. doi:10.1038/s41597-023-02569-2 Published: 28 September 2023. [22] Michael Levi and Peter Reuter. 2006. Money Laundering. Crime and Justice 34, 1 (2006), 289–375. doi:10.1086/501508 [23] Xiangfeng Li, Shenghua Liu, Zifeng Li, Xiaotian Han, Chuan Shi, Bryan Hooi, He Huang, and Xueqi Cheng. 2020. FlowScope: Spotting Money

Laundering Based on Graphs. In Proceedings of the Thirty-Fourth AAAI Conference on Artificial Intelligence (AAAI-20). 4731–4738. doi:10.1609/aaai. v34i04.5906 [24] Sara Makki, Zainab Assaghir, Yehia Taher, Rafiqul Haque, Mohand-Saïd Hacid, and Hassan Zeineddine. 2019. An Experimental Study With

Imbalanced Classification Approaches for Credit Card Fraud Detection. IEEE Access 7 (2019), 104856–104867. doi:10.1109/ACCESS.2019.2927266 Received June 3, 2019; accepted June 27, 2019; published July 8, 2019; current version July 29, 2019. [25] James Meldrum, Basem Suleiman, Fethi Rabhi, and Muhammad Johan Alibasa. 2025. New Money: A Systematic Review of Synthetic Data Generation

for Finance. arXiv preprint arXiv:2510.26076 (2025). https://arxiv.org/pdf/2510.26076v1 Posted October 2025. [26] Soroor Motie and Bijan Raahemi. 2023. Financial fraud detection using graph neural networks: A systematic review. Expert Systems with Applications

222 (2023), 119756. [27] Bryan Richardson, Dan Williams, and Daniel Mikkelsen. 2019. Network analytics and the fight against money laundering. McKinsey – Banking &

Securities Matters blog. https://www.mckinsey.com/industries/financial-services/our-insights/banking-matters/network-analytics-and-the-fight- against-money-laundering Accessed: 2025-06-15. [28] David Savage, Qingmai Wang, Pauline Chou, Xiuzhen Zhang, and Xinghuo Yu. 2016. Detection of money laundering groups using supervised

[pp. 28-29]

learning in networks. arXiv preprint arXiv:1608.00708 (2 Aug. 2016). https://arxiv.org/abs/1608.00708 Preprint; version v1 submitted 2 August 2016. [29] Shiva Shadrooh and Kjetil Nørvåg. 2024. SMoTeF: Smurf Money Laundering Detection Using Temporal Order and Flow Analysis. Applied Intelligence

54 (2024), 7461–7478. doi:10.1007/s10489-024-05545-4 Published online 7 June 2024. [30] Kishore Singh and Peter Best. 2019. Anti-Money Laundering: Using Data Visualization to Identify Suspicious Activity. International Journal of

Accounting Information Systems 34 (Sept. 2019), 100418. doi:10.1016/j.accinf.2019.06.001 Published online 19 July 2019. [31] Juan J. Soria, Rodrigo Loayza Abal, and Lidia Segura Peña. 2024. Machine Learning Models for Money Laundering Detection in Financial Institutions:

A Systematic Literature Review. In Proceedings of the 22nd LACCEI International Multi-Conference for Engineering, Education, and Technology. San Jose, Costa Rica. https://laccei.org/LACCEI2024-CostaRica/full-papers/Contribution_1682_final_a.pdf Hybrid conference, July 17–19, 2024; preprint

available on arXiv. [32] Toyotaro Suzumura and Hiroki Kanezashi. 2021. Anti-Money Laundering Datasets: InPlusLab Anti-Money Laundering DataDatasets. http:

//github.com/IBM/AMLSim/. [33] Haseeb Tariq and Marwan Hassani. 2023. Topology-Agnostic Detection of Temporal Money Laundering Flows in Billion-Scale Transactions.

In Machine Learning and Principles and Practice of Knowledge Discovery in Databases: International Workshops of ECML PKDD 2023, Turin, Italy, September 18–22, 2023, Revised Selected Papers, Part V (Communications in Computer and Information Science, Vol. 2137), Rosa Meo and Fabrizio Silvestri (Eds.). Springer, 402–419. doi:10.1007/978-3-031-74643-7_29 [34] United Nations Office on Drugs and Crime. n.d.. Money Laundering: Overview. https://www.unodc.org/unodc/en/money-laundering/overview.html.

[p. 29]

Accessed: 2025-05-13. [35] U.S. Bureau of Labor Statistics. 2025. Usual Weekly Earnings of Wage and Salary Workers. https://www.bls.gov/news.release/wkyeng.nr0.htm.

Accessed: 2025-06-15. [36] Petar Veličković, Guillem Cucurull, Arantxa Casanova, Adriana Romero, and Pietro Liò. 2018. Graph Attention Networks. In Proceedings of the

International Conference on Learning Representations (ICLR). https://arxiv.org/pdf/1710.10903 Published as a conference paper at ICLR 2018. [37] D. Wilson and A. Azmani. 2025. Generative Adversarial Networks: A Systematic Review of Characteristics, Applications, and Challenges in Financial

Data Generation and Market Modeling: 2019–2024. International Journal of Engineering (2025). Received 12 March 2025; Accepted 04 April 2025. [38] Keyulu Xu, Weihua Hu, Jure Leskovec, and Stefanie Jegelka. 2019. How Powerful Are Graph Neural Networks?. In Proceedings of the International

Conference on Learning Representations (ICLR). https://arxiv.org/pdf/1810.00826 Published as a conference paper at ICLR 2019. [39] Keyulu Xu, Weihua Hu, Jure Leskovec, and Stefanie Jegelka. 2019. How Powerful Are Graph Neural Networks?. In Proceedings of the International

Conference on Learning Representations (ICLR 2019). https://arxiv.org/pdf/1810.00826 Presented at ICLR 2019; also available as arXiv preprint. [40] Lei Xu, Maria Skoularidou, Alfredo Cuesta-Infante, and Kalyan Veeramachaneni. 2019. Modeling Tabular Data using Conditional GAN. In Advances

in Neural Information Processing Systems (NeurIPS), Vol. 32. [41] Yan Yang, Bin Lian, Lian Li, Chen Chen, and Pu Li. 2014. DBSCAN Clustering Algorithm Applied to Identify Suspicious Financial Transactions.

In Proceedings of the 2014 International Conference on Cyber-Enabled Distributed Computing and Knowledge Discovery (CyberC ’14). IEEE, 60–65. doi:10.1109/CyberC.2014.89 [42] Jiong Zhu, Ryan A. Rossi, Anup Rao, Tung Mai, Nedim Lipka, Nesreen K. Ahmed, and Danai Koutra. 2021. Graph Neural Networks with Heterophily.

[pp. 29-30] [ref: 6.1]

In Proceedings of the Thirty-Fifth AAAI Conference on Artificial Intelligence (AAAI ’21). Association for the Advancement of Artificial Intelligence. https://ojs.aaai.org/index.php/AAAI/article/view/17332 [43] Wei Zhuo, Zemin Liu, Bryan Hooi, Bingsheng He, Guang Tan, Rizal Fathony, and Jia Chen. 2024. Partitioning Message Passing for Graph Fraud

Detection. In Proceedings of the International Conference on Learning Representations (ICLR 2024). https://proceedings.iclr.cc/paper_files/paper/2024/ file/9251fa7fcc356bbfc16c040f4c030d83-Paper-Conference.pdf Published as a conference paper at ICLR 2024.

Appendix

6.1 Entity Attribute Specifications

This section provides detailed attribute definitions for each entity type in the Tide graph model. Tables 8–11 specify the

type-specific attributes that complement the common attributes defined in Section 4.2.

Attribute Description Type

Name An individual’s full name. String Age group The individual’s age group. Categorical Occupation The individual’s occupation. Categorical Gender The individual’s gender. Categorical

Table 8. Specific attributes for nodes with the individual entity type.

6.2 Risk Scoring and Pattern Parameters

This section documents the default parameters used for entity risk scoring and pattern generation. Table 12 presents

the risk factor weights used in the entity risk scoring framework described in Section 4.2.1. Tables 13 and 14 provide an

overview of the implemented laundering and background activity patterns, respectively.

Attribute Description Type

business_category The primary sector or type of business activity. Categorical incorporation_year The year the business was legally incorporated. Integer number_of_employees Approximate number of people employed by the business. Integer is_high_risk_category Flag for businesses in a high-risk category. Boolean

Table 9. Specific attributes for nodes with the business entity type.

Attribute Description Type

account_category Type of account (e.g., Current, Savings, Cash). Categorical currency The currency used by the account. String owner_id ID of the Individual or Business that owns this account. String institution_id ID of the Financial Institution that hosts this account. String

Table 10. Specific attributes for nodes with the account entity type.

Attribute Description Type

institution_name Name of the financial institution. String country Country of legal registration or regulation. String

Table 11. Specific attributes for nodes with the financial institution entity type.

Table 12. Default risk factor weights used in entity risk scoring.

Entity Type Risk Factor Weight (𝑤𝑖)

Individual

Base risk 0.05 High-risk age group 0.15 High-risk occupation 0.12

Business

Base risk 0.10 Cash-intensive business category 0.25 Very small company (≤5 employees) 0.10

Both High-risk jurisdiction 0.20

[pp. 30-31] [ref: 6.3]

6.3 Feature Engineering and Export

This section details the features included in exported datasets and the preprocessing configurations used for baseline

models. Table 15 lists all node and edge features available in the exported dataset, with categorical features one-hot

encoded. Internal generation attributes (e.g., risk_score, occupation, is_high_risk_category) are excluded to

prevent data leakage. Table 16 presents the Graph Feature Preprocessor (GFP) configuration adopted from Altman et

al. [6].

Table 13. Overview of implemented laundering patterns.

Pattern Topology Timing Additional layering

Overseas Transfers 1 →n overseas (n=2–5) Periodic (7/14/30d) ✓ Rapid Movement n →1 →cash-out (n=2–7) Burst (1–24h delay) ✓ Front Business Cash →business →overseas Paired (0.5–6h) ✓ U-Turn Source →chain →return Sequential (1–5d/hop) Inherent Synchronised n →1 recipient (n=3–8) Coordinated (2h window) —

Table 14. Overview of background activity patterns. Baseline patterns model routine financial behaviour; counter-leakage patterns introduce legitimate activity that shares features with fraud patterns.

Pattern Group Fraud feature countered

Random everyday payments Baseline — High-value transactions Baseline — Salary payments Baseline — Fraudster background Baseline Behavioural anomaly

Legitimate bursts Counter-leakage Temporal clustering Legitimate periodic Counter-leakage Periodic timing Legitimate chains Counter-leakage Multi-hop topology Legitimate rapid flow Counter-leakage Inflow–outflow sequences Legitimate cash operations Counter-leakage Cash transaction types Legitimate structuring Counter-leakage Near-threshold amounts High-risk entity activity Counter-leakage Risk-score correlation

Table 15. Node and edge features included in the exported dataset. Categorical features are one-hot encoded. Internal generation attributes (risk_score, occupation, is_high_risk_category, etc.) are excluded.

(a) Node features.

(b) Edge features (transaction edges).

Feature Type Encoding

Feature Type Encoding

amount Num. Raw timestamp Num. Unix seconds time_since_prev Num. Seconds transaction_type Cat. One-hot (5) currency Cat. One-hot

node_type Cat. One-hot (4) country_code Cat. One-hot (top 30) account_category Cat. One-hot (5) gender Cat. One-hot (2) age_group Cat. One-hot (5) business_category Cat. One-hot (top 20) incorporation_year Num. Raw creation_year Num. Raw

6.4 Calibration Data Sources

Transaction amount and frequency distributions in Tide were calibrated using publicly available reference data. Table 17

presents the noncash payment volumes from the 2022 Federal Reserve Payments Study [10], which informed our

transaction type frequency distributions as described in Section 4.5.2.

[pp. 32-33] [ref: 6.5]

Table 16. Graph Feature Preprocessor (GFP) configuration, adopted from Altman et al. [6].

Parameter Value

Batch size 128 Patterns Scatter-gather, temporal cycles, simple cycles, vertex statistics Scatter-gather window 6 hours Cycle / vertex stats window 1 day Max simple cycle length 10 Vertex statistics fields Amount, Timestamp

Table 17. FRPS 2021 noncash payment volumes by category.

FRPS Category Volume (B) Share

Non-prepaid debit cards 87.8 42.2% Credit cards 51.1 24.6% ACH debit transfers 20.3 9.8% Prepaid debit cards 18.1 8.7% ACH credit transfers 15.9 7.6% Checks 11.2 5.4% ATM withdrawals 3.7 1.8%

Total 208.1 100%

Table 18. Hyperparameter configuration for GBT models.

Parameter LightGBM XGBoost

n_estimators 1000 1000 max_depth 6 6 num_leaves 64 – learning_rate 0.01 0.01 reg_lambda (L2) 5.0 5.0 reg_alpha (L1) 1.5 0.5 subsample 0.8 0.8 colsample_bytree 0.8 0.8 min_child_samples/weight 50 5 class weighting† balanced 200 gamma – 0.2

† LightGBM: class_weight=’balanced’ (auto-computed); XGBoost: scale_pos_weight=200.

6.5 Extended Experimental Results

This section provides the full performance metrics that complement the summary results presented in Section 5.2.3.

Table 22 reports detailed results for the primary experimental condition (low illicit ratio, 0.10% class imbalance). All

metrics are computed at Youden’s optimal threshold, with results reported as mean ± standard deviation over 5 runs.

Table 22 compares the performance of PNA and XGBoost models.

Table 19. Hyperparameter configuration for GNN models.

Parameter GIN GIN+EU PNA

hidden dimension 64 64 64 number of layers 4 4 2 dropout 0.2 0.2 0.1 final dropout 0.5 0.5 0.5 learning rate 0.001 weight decay 0.0005 minority class weight 50

Table 20. Comparison of model performance on fraud detection. Homophily index: 0.0023. Class imbalance of 0.10%. Lift = PR-AUC / fraud_rate (times better than random). All metrics (F1, Precision, Recall) computed at Youden’s optimal threshold. Results reported as mean ± std over 5 runs.

Model F1 Precision Recall PR-AUC Lift Youden’s J ROC-AUC


---

[previous part](text-003.md) | [source overview](overview.md) | [next part](text-005.md)

[^original]: arXiv, "Tide: A Customisable Dataset Generator for Anti-Money Laundering Research" (2026-02-03). https://arxiv.org/abs/2603.01863
