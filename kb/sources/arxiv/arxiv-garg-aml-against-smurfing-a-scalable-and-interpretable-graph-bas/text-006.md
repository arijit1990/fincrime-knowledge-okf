---
type: Source Text
title: 'GARG-AML against Smurfing: A Scalable and Interpretable Graph-Based Framework for Anti-Money Laundering - part 6 of 10 (pp. 25-29)'
description: 'Verbatim extracted text, pp. 25-29: 6 Limitations > 6.1 Limitations in the Data; 6 Limitations > 6.2 Limitations in the Methodology; 7 Conclusion; and 3 more sections'
resource: https://arxiv.org/abs/2506.04292
tags:
- academic_finding
- explainability
- global_academic
- network_graph
- preprint
- typologies
status: stable
source_id: arxiv-garg-aml-against-smurfing-a-scalable-and-interpretable-graph-bas
issuer: arxiv
issuer_name: arXiv
jurisdictions:
- GLOBAL_ACADEMIC
tier: 3
instrument_type: preprint
normative_force: academic_finding
publication_date: '2025-04-06'
legal_status: unknown
part: 6
parts_total: 10
content_mode: full_text
generated:
  by: process:fincrime-kb-build
  at: '2026-11-16T16:23:02Z'
verified:
- by: process:kb-validate/verbatim-coverage
  at: '2026-11-16T16:23:02Z'
sources:
- id: original
  resource: https://arxiv.org/abs/2506.04292
  title: 'GARG-AML against Smurfing: A Scalable and Interpretable Graph-Based Framework for Anti-Money Laundering'
  author: org:arxiv
  last_modified: '2025-04-06T00:00:00Z'
---

# GARG-AML against Smurfing: A Scalable and Interpretable Graph-Based Framework for Anti-Money Laundering

[previous part](text-005.md) | [source overview](overview.md) | [next part](text-007.md)

> Verbatim text extracted from the original (arXiv, 2025-04-06), part 6 of 10, pp. 25-29. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **academic finding**.[^original]

## 6 Limitations


### 6.1 Limitations in the Data


[p. 25]

GARG-AML assumes full visibility of all transactions, which is rarely the case in practice (Altman et al., 2023; Tariq and Hassani, 2025; Dumitrescu et al., 2022). Banks only have access to transactions that involve their own clients, and the sender and receiver account numbers. Transactions between two external accounts remain hidden, which makes second-order neighbourhoods incomplete (see Figure 11). This can obscure smurfing structures or lead to incorrect classification. D reports a sensitivity analysis that mimics this limited view on transactions: a single bank sees on average only 7% of its clients’ second-order neighbourhoods and shows no reliable detection performance, whereas pooling the 50 largest simulated banks (42% visible on average) retains the (modest) performance obtained on the full network.

Initiatives are needed that allow linking transactions on an inter-bank and international level. However, sharing all transaction data is often not possible because of privacy and/or commercial reasons. Federated learning (McMahan et al., 2017) could provide a solution, albeit adapted to network data where links are shared among parties.

### 6.2 Limitations in the Methodology


There are three main limitations to the presented methodology. The first concerns the use of only one layer of smurfs. It is likely that criminal organisations utilise multiple layers of smurfs to launder their money. While multi-layered schemes exist, they impose a deterrent risk-reward trade-off: bypassing the core organisation increases the risk of funds disappearing and requires greater trust in intermediaries. Furthermore, incremental smurf fees reduce the total illicit reward. Consequently, single-layer analysis already captures a meaningful portion of standard smurfing operations.

The second limitation is that relying on a single score is restrictive; it may miss complex, real-world smurfing operations (Bekkers et al., 2025; Raza et al., 2020; Leukfeldt and Jansen, 2015). An improvement would already be to use business rules on the values of the densities and sizes of the blocks. However, this requires extensive expert knowledge on diverse smurfing topologies. This is outside the scope of this paper.

The third methodological limitation is that GARG-AML uses unweighted graph structures, ignoring transaction volume and timing. While these are simplifications, the resulting smurfing score remains interpretable and useful in downstream AML systems. Timing issues can be addressed by restricting analysis to shorter time windows, applying sliding windows, or comparing scores across time.

## 7 Conclusion


[p. 26]

This paper introduces Graph-Aided Risk Grading for Anti-Money Laundering (GARG-AML), which is a novel approach for detecting smurfing by quantifying the structural similarity of nodes’ neighbourhoods to known money laundering patterns via density-based features in the adjacency matrix.

We validated GARG-AML on several synthetic datasets and compared it to state-of-the-art detection methods. The results of the experiments show that GARG-AML achieves strong detection power, with competitive performance, and excellent scalability for large networks. Unlike approaches that are based on complex optimisation techniques or machine learning models, GARG-AML relies on domain expertise and straightforward density-based calculations. We also showed that in cases where labels are very scarce, GARG-AML is competitive with GNNs.

While GARG-AML is not a complete solution for smurfing detection, it offers two key advantages over existing methods: (1) it produces interpretable features, either as separate densities or a single composite score, that can be seamlessly integrated into AML systems, and (2) it is computationally efficient, with parallel and memory-light calculations, thus enabling practical deployment in real-world settings.

These key properties allow financial institutions to adopt our method easily and strengthen their role as capable guardians. Blocking simple smurfing tactics forces criminals into riskier, less profitable schemes. Ultimately, if the cost and danger of laundering money outweigh the rewards, regulators can effectively put criminal syndicates out of business.

Future work will explore (i) treating individual densities as features in classification models to identify distinct smurfing and money mule topologies, (ii) extending the methodology to incorporate transaction timing and volume possibly by integrating it as a baseline in the SMoTeF pipeline, as well as generalising it to other anomalous transaction patterns, and (iii) constructing a federated learning framework to alleviate the limited visibility of network data across banks.

Detecting smurfs is also an important research area for network security and intrusion detection (Yang et al., 2009; Shadrooh and Nørv˚ag, 2024). Further research could analyse whether similar featurisation of the patterns is possible for denial of service (DoS) or similar attacks.

## Acknowledgements


This work was supported by the Research Foundation – Flanders (FWO) [grant number 1SHEN24N and G015020N] and by the BNP Paribas Fortis Chair in Fraud Analytics. The resources and services used in this work were provided by the VSC (Flemish Supercomputer Center), funded by the Research Foundation - Flanders (FWO) and the Flemish Government.

Bruno Deprez: Conceptualization, Data Curation, Methodology, Formal Analysis, Software, Visualization, Writing—Original Draft.

Bart Baesens: Conceptualization, Supervision, Writing—Review & Editing. Tim Verdonck: Conceptualization, Supervision, Writing—Review & Editing. Wouter Verbeke: Conceptualization, Project administration, Supervision, Writing—Review & Editing.

## Declaration of Competing Interest


The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

- Ismail Alarab, Simant Prakoonwit, and Mohamed Ikbal Nacer. Competence of graph convolutional networks for anti-money laundering in Bitcoin blockchain. In _Proceedings of the 2020 5th International Conference on Machine Learning Technologies_ , ICMLT ’20, pages 23–27, New York, NY, USA, 2020. Association for Computing Machinery. ISBN 9781450377645. doi: 10.1145/3409073.3409080.

## References


[p. 27]

- Erik Altman, Jovan Blanuˇsa, Luc von Niederh¨ausern, Beni Egressy, Andreea Anghel, and Kubilay Atasu. Realistic synthetic financial transactions for anti-money laundering models. In A. Oh, T. Naumann, A. Globerson, K. Saenko, M. Hardt, and S. Levine, editors, _Advances in Neural Information Processing Systems_ , volume 36, pages 29851– 29874. Curran Associates, Inc., 2023.

- Albert-L´aszl´o Barab´asi and R´eka Albert. Emergence of scaling in random networks. _Science_ , 286(5439):509–512, 1999. ISSN 0036-8075.

- Luuk Bekkers, Remco Spithoven, Ynze Van Houten, and Eric Rutger Leukfeldt. The involvement mechanisms of cybercrime: Explaining previous exposure of young people to money mule recruiters. _European Journal of Criminology_ , 22(4):487–507, 2025. doi: 10.1177/14773708251323349.

- Vincent D Blondel, Jean-Loup Guillaume, Renaud Lambiotte, and Etienne Lefebvre. Fast unfolding of communities in large networks. _Journal of Statistical Mechanics: Theory and Experiment_ , 2008(10):P10008, October 2008. doi: 10.1088/1742-5468/2008/10/P10008.

- Richard J. Bolton and David J. Hand. Statistical Fraud Detection: A Review. _Statistical Science_ , 17(3):235 – 255, 2002. doi: 10.1214/ss/1042727940.

- M´ario Cardoso, Pedro Saleiro, and Pedro Bizarro. LaundroGraph: Self-supervised graph representation learning for anti-money laundering. In _Proceedings of the Third ACM International Conference on AI in Finance_ , ICAIF ’22, pages 130–138, New York, NY, USA, 2022. Association for Computing Machinery. ISBN 9781450393768. doi: 10.1145/3533271.3561727.

- Zhiyuan Chen, Le Dinh Van Khoa, Ee Na Teoh, Amril Nazir, Ettikan Kandasamy Karuppiah, and Kim Sim Lam. Machine learning techniques for anti-money laundering (AML) solutions in suspicious transaction detection: a review. _Knowledge and Information Systems_ , 57(2):245–285, 2018. doi: 10.1007/s10115-017-1144-z.

- Lawrence E. Cohen and Marcus Felson. Social change and crime rate trends: A routine activity approach. _American Sociological Review_ , 44(4):588–608, 1979. ISSN 00031224. URL `http://www.jstor.org/stable/2094589` .

- Data World. Czech financial dataset, 1999. URL `https://data.world/lpetrocelli/ czech-financial-dataset-real-anonymized-transactions` .

- Jesse Davis and Mark Goadrich. The relationship between precision-recall and roc curves. In _Proceedings of the 23rd International Conference on Machine Learning_ , ICML ’06, pages 233–240, New York, NY, USA, 2006. Association for Computing Machinery. ISBN 1595933832. doi: 10.1145/1143844.1143874.

- Janez Demˇsar. Statistical comparisons of classifiers over multiple data sets. _Journal of Machine Learning Research_ , 7 (1):1–30, 2006. URL `http://jmlr.org/papers/v7/demsar06a.html` .

- Bruno Deprez, Toon Vanderschueren, Bart Baesens, Tim Verdonck, and Wouter Verbeke. Network analytics for anti-money laundering—a systematic literature review and experimental evaluation. _INFORMS Journal on Data Science_ , 5(2):119–154, 2026. doi: 10.1287/ijds.2024.0042.

- Rafał Dre˙zewski, Jan Sepielak, and Wojciech Filipkowski. The application of social network analysis algorithms in a system supporting money laundering detection. _Information Sciences_ , 295:18–32, 2015. ISSN 0020-0255. doi: 10.1016/j.ins.2014.10.015.

- Bogdan Dumitrescu, Andra B˘altoiu, and S¸tefania Budulan. Anomaly detection in graphs of bank transactions for anti money laundering applications. _IEEE Access_ , 10:47699–47714, 2022. doi: 10.1109/ACCESS.2022.3170467.

- B´eni Egressy, Luc von Niederh¨ausern, Jovan Blanuˇsa, Erik Altman, Roger Wattenhofer, and Kubilay Atasu. Provably powerful graph neural networks for directed multigraphs. _Proceedings of the AAAI Conference on Artificial Intelligence_ , 38(10):11838–11846, Mar. 2024. doi: 10.1609/aaai.v38i10.29069.

[pp. 27-28]

- Paul Erd˝os and Alfr´ed R´enyi. On random graphs I. _Publicationes Mathematicae Debrecen_ , 6:290–297, 1959.

- Ehi Eric Esoimeme. Identifying and reducing the money laundering risks posed by individuals who have been unknowingly recruited as money mules. _Journal of Money Laundering Control_ , 24(1):201–212, June 2020. ISSN 1368-5201. doi: 10.1108/JMLC-05-2020-0053.

- FATF. _International Standards on Combating Money Laundering and the Financing of Terrorism & Proliferation_ . FATF, Paris, France, 2012-2023. URL `https://www.fatf-gafi.org/en/publications/ Fatfrecommendations/Fatf-recommendations.html` .

- Santo Fortunato and Marc Barth´elemy. Resolution limit in community detection. _Proceedings of the National Academy of Sciences_ , 104(1):36–41, 2007. doi: 10.1073/pnas.0605965104.

- Milton Friedman. The use of ranks to avoid the assumption of normality implicit in the analysis of variance. _Journal of the American Statistical Association_ , 32(200):675–701, 1937. doi: 10.1080/01621459.1937.10503522.

- Milton Friedman. A comparison of alternative tests of significance for the problem of m rankings. _The Annals of Mathematical Statistics_ , 11(1):86–92, 1940. ISSN 00034851. URL `http://www.jstor.org/stable/2235971` .

- Andrea Fronzetti Colladon and Elisa Remondi. Using social network analysis to prevent money laundering. _Expert Systems with Applications_ , 67:49–58, 2017. ISSN 0957-4174. doi: 10.1016/j.eswa.2016.09.029.

- Aric Hagberg, Daniel A. Schult, and Pieter J. Swart. Exploring network structure, dynamics, and function using NetworkX. In _Proceedings of the 7th Python in Science Conference (SciPy2008)_ , pages 11–15, 2008. URL `https: //www.osti.gov/biblio/960616` .

[p. 28]

- Eric Halford, Ian Gibson, Mark Newfield, and Mufazzal Dhanwala. Developing a scoring model for managing money laundering transactions using machine learning. _Journal of Money Laundering Control_ , 28(7):30–49, March 2025. ISSN 1368-5201. doi: 10.1108/JMLC-09-2024-0152.

- Will Hamilton, Zhitao Ying, and Jure Leskovec. Inductive representation learning on large graphs. In I. Guyon, U. Von Luxburg, S. Bengio, H. Wallach, R. Fergus, S. Vishwanathan, and R. Garnett, editors, _Advances in Neural Information Processing Systems_ , volume 30. Curran Associates, Inc., 2017. URL `https://proceedings.neurips.cc/ paper_files/paper/2017/file/5dd9db5e033da9c6fb5ba83c7a7ebea9-Paper.pdf` .

- Martin Jullum, Anders Løland, Ragnar Bang Huseby, Geir Anonsen,˚ and Johannes Lorentzen. Detecting money laundering transactions with machine learning. _Journal of Money Laundering Control_ , 23(1):173–186, January 2020. ISSN 1368-5201. doi: 10.1108/JMLC-07-2019-0055.

- Dattatray Vishnu Kute, Biswajeet Pradhan, Nagesh Shukla, and Abdullah Alamri. Deep learning and explainable artificial intelligence techniques applied for detecting money laundering–a critical review. _IEEE Access_ , 9:82300– 82317, 2021.

- Andrea Lancichinetti and Santo Fortunato. Community detection algorithms: A comparative analysis. _Phys. Rev. E_ , 80:056117, 2009. doi: 10.1103/PhysRevE.80.056117.

- Meng-Chieh Lee, Yue Zhao, Aluna Wang, Pierre Jinghong Liang, Leman Akoglu, Vincent S Tseng, and Christos Faloutsos. AutoAudit: Mining accounting and time-evolving graphs. In _2020 IEEE International Conference on Big Data (Big Data)_ , pages 950–956. IEEE, 2020. doi: 10.1109/BigData50022.2020.9378346.

- Kevin J. Leonard. The development of a rule based expert system model for fraud alert in consumer credit. _European Journal of Operational Research_ , 80(2):350–356, 1995. ISSN 0377-2217. doi: 10.1016/0377-2217(93)E0249-W.

- Rutger Leukfeldt and Jurjen Jansen. Cyber criminal networks and money mules: An analysis of low-tech and high-tech fraud attacks in the netherlands. _International Journal of Cyber Criminology_ , 9(2), 2015.

- Michael Levi and Peter Reuter. Money laundering. _Crime and justice_ , 34(1):289–375, 2006. doi: 10.1086/501508.

- Xiangfeng Li, Shenghua Liu, Zifeng Li, Xiaotian Han, Chuan Shi, Bryan Hooi, He Huang, and Xueqi Cheng. FlowScope: Spotting money laundering based on graphs. _Proceedings of the AAAI Conference on Artificial Intelligence_ , 34(04):4731–4738, 2020. doi: 10.1609/aaai.v34i04.5906. URL `https://ojs.aaai.org/index.php/AAAI/ article/view/5906` .

- Xiao Fan Liu, Xin-Jian Jiang, Si-Hao Liu, and Chi Kong Tse. Knowledge discovery in cryptocurrency transactions: A survey. _IEEE Access_ , 9:37229–37254, 2021. doi: 10.1109/ACCESS.2021.3062652.

- Wai Weng Lo, Gayan K. Kulatilleke, Mohanad Sarhan, Siamak Layeghy, and Marius Portmann. Inspection-L: selfsupervised GNN node embeddings for money laundering detection in bitcoin. _Applied Intelligence_ , 53(16):19406– 19417, 2023. doi: 10.1007/s10489-023-04504-9.

- Mark Eshwar Lokanan. Enhancing AML compliance: a machine learning approach to suspicious activity detection through routine activity theory. _Journal of Money Laundering Control_ , 28(4-5):680–698, September 2025. ISSN 1368-5201. doi: 10.1108/JMLC-07-2024-0114.

- John Madinger. _Money laundering: a guide for criminal investigators._ CRC Press, Boca Raton, third edition, 2012. ISBN 978-1-4398-6912-3.

[pp. 28-29]

- Yusarina Mat Isa, Zuraidah Mohd Sanusi, Hendi Yogi Prabowo, and Tarjo Tarjo. Routine activity theory and the dynamics of money laundering: reassessing emerging threats in banking operations. _Journal of Money Laundering Control_ , 28(6):764–775, October 2025. ISSN 1368-5201. doi: 10.1108/JMLC-06-2025-0106.

- Bill McCarthy and Ali Chaudhary. Rational choice theory. In _Encyclopedia of Criminology and Criminal Justice_ , pages 4307–4315. Springer New York, New York, NY, 2014. doi: 10.1007/978-1-4614-5690-2 ~~3~~ 96.

- Brendan McMahan, Eider Moore, Daniel Ramage, Seth Hampson, and Blaise Aguera y Arcas. CommunicationEfficient Learning of Deep Networks from Decentralized Data. In Aarti Singh and Jerry Zhu, editors, _Proceedings of the 20th International Conference on Artificial Intelligence and Statistics_ , volume 54 of _Proceedings of Machine_

_Learning Research_ , pages 1273–1282. PMLR, 20–22 Apr 2017. URL `https://proceedings.mlr.press/v54/ mcmahan17a.html` .

Peter Bjorn Nemenyi. _Distribution-free multiple comparisons._ Princeton University, 1963.

- Mark EJ Newman and Michelle Girvan. Finding and evaluating community structure in networks. _Physical review E_ , 69(2):026113, 2004. URL `https://doi.org/10.1103/PhysRevE.69.026113` .

- Brice Ozenne, Fabien Subtil, and Delphine Maucort-Boulch. The precision–recall curve overcame the optimism of the receiver operating characteristic curve in rare diseases. _Journal of clinical epidemiology_ , 68(8):855–859, 2015.

- Berkan Oztas, Deniz Cetinkaya, Festus Adedoyin, Marcin Budka, Gokhan Aksu, and Huseyin Dogan. Transaction monitoring in anti-money laundering: A qualitative analysis and points of view from industry. _Future Generation Computer Systems_ , 159:161–171, 2024.

[p. 29]

- Mario Alfonso Prado-Romero, Christian Doerr, and Andr´es Gago-Alonso. Discovering Bitcoin mixing using anomaly detection. In Marcelo Mendoza and Sergio Velast´ın, editors, _Progress in Pattern Recognition, Image Analysis, Computer Vision, and Applications_ , pages 534–541, Cham, 2018. Springer International Publishing. ISBN 978-3319-75193-1.

- Syahril Ramadhan. Harnessing machine learning for money laundering detection: a criminological theory-centric approach. _Journal of Money Laundering Control_ , 28(1):184–201, December 2024. ISSN 1368-5201. doi: 10.1108/ JMLC-04-2024-0083.

- Muhammad Subtain Raza, Qi Zhan, and Sana Rubab. Role of money mules in money laundering and financial crimes a discussion through case studies. _Journal of Financial Crime_ , 27(3):911–931, June 2020. ISSN 1359-0790. doi: 10.1108/JFC-02-2020-0028.

- Daniel S´anchez, MA Vila, L Cerda, and Jos´e-Maria Serrano. Association rules applied to credit card fraud detection. _Expert Systems with Applications_ , 36(2, Part 2):3630–3640, 2009. doi: 10.1016/j.eswa.2008.02.001.

- Ted E Senator, Henry G Goldberg, Jerry Wooton, Matthew A Cottini, AF Umar Khan, Christina D Klinger, Winston M Llamas, Michael P Marrone, and Raphael WH Wong. Financial crimes enforcement network AI system (FAIS) identifying potential money laundering from reports of large cash transactions. _AI Magazine_ , 16(4):21, 1995. doi: 10.1609/aimag.v16i4.1169.

- Shiva Shadrooh and Kjetil Nørv˚ag. SMoTeF: Smurf money laundering detection using temporal order and flow analysis. _Applied Intelligence_ , 2024. doi: 10.1007/s10489-024-05545-4.

- Michele Starnini, Charalampos E. Tsourakakis, Maryam Zamanipour, Andr´e Panisson, Walter Allasia, Marco Fornasiero, Laura Li Puma, Valeria Ricci, Silvia Ronchiadin, Angela Ugrinoska, Marco Varetto, and Dario Moncalvo. Smurf-based anti-money laundering in time-evolving transaction networks. In Yuxiao Dong, Nicolas Kourtellis, Barbara Hammer, and Jose A. Lozano, editors, _Machine Learning and Knowledge Discovery in Databases. Applied Data Science Track_ , pages 171–186, Cham, 2021. Springer International Publishing. ISBN 978-3-030-86514-6. URL `https://doi.org/10.1007/978-3-030-86514-6_11` .

- Toyotaro Suzumura and Hiroki Kanezashi. Anti-Money Laundering Datasets: InPlusLab anti-money laundering datasets. `http://github.com/IBM/AMLSim/` , 2021.

- Haseeb Tariq and Marwan Hassani. Topology-agnostic detection of temporal money laundering flows in billionscale transactions. In Rosa Meo and Fabrizio Silvestri, editors, _Machine Learning and Principles and Practice of Knowledge Discovery in Databases_ , pages 402–419, Cham, 2025. Springer Nature Switzerland. doi: 10.1007/ 978-3-031-74643-7 _\_ ~~2~~ 9.

- V. A. Traag, L. Waltman, and N. J. van Eck. From Louvain to Leiden: guaranteeing well-connected communities. _Scientific Reports_ , 9(1):5233, 2019. doi: 10.1038/s41598-019-41695-z.

- United Nations Office on Drugs and Crime. Estimating illicit financial flows resulting from drug trafficking and other transnational organized crimes. Research report, United Nations Office on Drugs and Crime, Vienna, 2011.

- Rafa¨el Van Belle, Bart Baesens, and Jochen De Weerdt. CATCHM: A novel network-based credit card fraud detection method using node representation learning. _Decision Support Systems_ , 164:113866, 2023. ISSN 0167-9236. doi: 10.1016/j.dss.2022.113866.

- Duncan J. Watts and Steven H. Strogatz. Collective dynamics of ‘small-world’ networks. _Nature_ , 393(6684):440–442, 1998. doi: 10.1038/30918.


---

[previous part](text-005.md) | [source overview](overview.md) | [next part](text-007.md)

[^original]: arXiv, "GARG-AML against Smurfing: A Scalable and Interpretable Graph-Based Framework for Anti-Money Laundering" (2025-04-06). https://arxiv.org/abs/2506.04292
