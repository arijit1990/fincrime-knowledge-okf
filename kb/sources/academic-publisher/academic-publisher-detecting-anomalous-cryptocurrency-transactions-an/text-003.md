---
type: Source Text
title: 'Detecting anomalous cryptocurrency transactions: An AML/CFT application of machine learning-based forensics - part 3 of 4 (pp. 12-16)'
description: 'Verbatim extracted text, pp. 12-16: Detecting anomalous cryptocurrency transactions: An AML/CFT application of machine learning‑based forensics > Results; Detecting anomalous cryptocurrency transactions: An AML/CFT application of machine learning‑based forensics > Discussion; Detecting anomalous cryptocurrency transactions: An AML/CFT application of machine learning‑based forensics > Conclusions; and 1 more sections'
resource: https://link.springer.com/article/10.1007/s12525-023-00654-3
tags:
- academic_finding
- academic_paper
- global_academic
- network_graph
- typologies
status: stable
source_id: academic-publisher-detecting-anomalous-cryptocurrency-transactions-an
issuer: academic_publisher
issuer_name: Academic publisher / repository
jurisdictions:
- GLOBAL_ACADEMIC
tier: 3
instrument_type: academic_paper
normative_force: academic_finding
publication_date: '2023-07-26'
legal_status: unknown
part: 3
parts_total: 4
content_mode: full_text
generated:
  by: process:fincrime-kb-build
  at: '2026-11-22T10:06:32Z'
verified:
- by: process:kb-validate/verbatim-coverage
  at: '2026-11-22T10:06:32Z'
sources:
- id: original
  resource: https://link.springer.com/article/10.1007/s12525-023-00654-3
  title: 'Detecting anomalous cryptocurrency transactions: An AML/CFT application of machine learning-based forensics'
  author: org:academic_publisher
  last_modified: '2023-07-26T00:00:00Z'
---

# Detecting anomalous cryptocurrency transactions: An AML/CFT application of machine learning-based forensics

[previous part](text-002.md) | [source overview](overview.md) | [next part](text-004.md)

> Verbatim text extracted from the original (Academic publisher / repository, 2023-07-26), part 3 of 4, pp. 12-16. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **academic finding**.[^original]

## Detecting anomalous cryptocurrency transactions: An AML/CFT application of machine learning‑based forensics


### Results


#### _Precision_ = _TP_ + _FP_ .


[p. 12]

|Model|Precision|Recall|F1 score|M.A. F1|
|---|---|---|---|---|
|Random Forest classifier (tx)i|0.909|0.648|0.757|0.974|
|Random Forest classifier (tx + agg)|0.981|0.651|0.782|0.977|
|Logistic regression (tx)|0.515|0.646|0.573|0.939|
|Logistic regression (tx + agg)|0.456|0.630|0.529|0.929|
|MLP (tx)|0.897|0.593|0.714|0.970|
|MLP (tx + agg)i|0.817|0.623|0.707|0.968|
|k-NN classifier (tx)i|0.762|0.629|0.689|0.964|
|k-NN classifier (tx + agg)|0.730|0.576|0.644|0.960|
|iSVC (tx)|0.842|0.604|0.703|0.968|
|SVC (tx + agg)i|0.862|0.588|0.699|0.968|
|Decision Tree classifier (tx)i|0.986|0.573|0.725|0.973|
|Decision Tree classifier (tx + agg)|0.986|0.573|0.725|0.973|
|iAdaBoost classifier (tx)|0.793|0.615|0.693|0.966|
|iAdaBoost classifier (tx + agg)|0.945|0.567|0.708|0.971|
|iGCN (tx)|0.906|0.790|0.844|0.973|
|GAT (tx)|0.897|0.605|0.723|0.971|

Best results are highlighted in bold

but still provides better performances than all the rests, i.e., 0 _._ 906. For what concerns the Micro Average F1-score, all approaches fit in the range of 0 _._ 960 to 0 _._ 977. These results are in contrast with the results in Weber et al. (2019), where Random Forests provided the best performance. The cause of such improvement might be due to the different architectures we exploited to build the neural network.

Furthermore, the comparison with the other graph-based approach, i.e., GAT, also sees the GCN outperforming. GAT performs better than a simple dense network but cannot reach the results of GCN and Random Forest classifiers. The motivation is probably due to the na¨ıve structure of the neural network, and its optimization is currently under investigation.

So far, we have focused on the classification of illicit transactions. Since the dataset is unbalanced—i.e., it contains more licit than illicit transactions in a ratio of more or less 1 to 10—the problem becomes relatively trivial. For the sake of transparency, however, the final performance results related to licit transactions are reported in Table 5. All the models perform very well and are very similar to each other. In this case, graph-based approaches do not perform better than Random Forest classifiers, but the difference is not outstanding.

### Discussion


[pp. 12-13]

When interpreted through the lens of the AML/CFT remarks outlined in the previous sections, our findings inspire multilayered considerations. Accordingly, in this section, our reasoning is threefold. First, we discuss the results of our experiments vis-`a-vis the approaches used as benchmarks.

Secondly, we broaden the perspective of the analysis to consider not only the impacts of crypto-related RegTech methodologies on the evolution of the Internet of Money, but also the interplay between the latter and the prospective role of forensics. Finally, we pinpoint a few associated challenges.

From the first perspective, to the best of our knowledge, the experiment described in this paper is the first attempt to implement GAT models to detect anomalies in Bitcoin transactions for AML/CFT purposes. The final results are on par with the state of the art of GCN networks, with GAT marginally worse than GCN. This could be explained by the “simpler” implementation of GAT and the possibility that the dataset responds better to non-spectral methods. Nonetheless, we argue that the novelty of this application could be helpful for general research on GAT anomaly detection techniques. In addition, the results show that the GCN neural network typology is a promising solution for AML/CFT, as it performs better than other approaches.

In this context, it is essential to consider that GCN and GAT classifiers only have access to transaction features, which means that all information about aggregated nodes comes from the graph structure itself. Since the performance of GCN is in line with Random Forest (with aggregated features), we can claim that our graph networks can obtain the same amount of information as the creator of the dataset (Weber et al., 2019). However, choosing one method over another carries additional implications that must be carefully weighed. For example, the performance of Random Forests falls slightly behind GCN’s, but there is no sacrifice in explainability because the detectors are derived from Random Forests’ rules (Eddin et al., 2021). Given the size and dynamism of real-world information, explainability of the results is challenging to provide, both in

1 3

Table 5 Table showing the results for licit transaction classification with the F1-score, Micro Average F1-score, precision, and recall metrics for all models

[p. 13]

|Model|Precision|Recall|F1 Score|M.A. F1|
|---|---|---|---|---|
|Random Forest classifier (tx)i|0.977|0.995|0.986|0.973|
|Random Forest classifier (tx + agg)|0.977|0.999|0.988|0.978|
|Logistic regression (tx)|0.976|0.959|0.967|0.939|
|Logistic regression (tx + agg)|0.975|0.949|0.962|0.929|
|MLP (tx)|0.973|0.995|0.984|0.970|
|MLP (tx + agg)|0.974|0.994|0.984|0.970|
|k-NN (tx)|0.978|0.967|0.972|0.949|
|k-NN (tx + agg)|0.975|0.965|0.970|0.944|
|SVC (tx)|0.974|0.992|0.983|0.968|
|SVC (tx + agg)i|0.973|0.994|0.983|0.968|
|Decision Tree classifier (tx)i|0.972|0.999|0.986|0.973|
|Decision Tree classifier (tx + agg)|0.972|0.999|0.986|0.973|
|iAdaBoost classifier (tx)|0.975|0.989|0.982|0.966|
|iAdaBoost classifier (tx + agg)|0.972|0.998|0.985|0.971|
|iGCN (tx)|0.975|0.994|0.984|0.971|
|GAT (tx)|0.973|0.992|0.982|0.967|

Best results are highlighted in bold

this context and in the broader AI field. Even in our specific narrow instance—i.e., transaction graphs that model illicit activity over time—it is challenging to apply efficient methods whose results can be understood by humans. Although this appears to be a crucial aspect, the literature still lacks some research on the application of explainable AI techniques for AML/CFT anomaly detection (Kute et al., 2021).

From the second perspective, the choice of the forensic approach(es) to deploy must be made taking into consideration the evolution of the Internet of Money, with specific regard to peer-to-peer transfers and DeFi protocols. Indeed, while its developments warrant the application of increasingly sophisticated yet explainable compliance and investigation techniques, we see how the implementation of the crypto travel rule has already prompted the industry to denounce the lack of global standards and technical solutions to underpin effective and affordable compliance. It follows that, while the great quantity and complexity of transaction data to be processed suggests that machine learning will continue to be a part of the solution—with marginal performance differences possibly bearing significant weight when various approaches are combined—it is crucial to back the relevant research with a constructive dialog between the stakeholders involved. In this context, we point out to the increase in the laundering-related use DeFi protocols of 1.964% between 2020 and 2021. In 2021, centralized exchanges received 47% of funds originating from illicit addresses and DeFi protocols 17%, vis-`a-vis 2% in 2020. Likewise, in 2021 funds derived from cryptocurrency thefts were increasingly sent to DeFi platforms (51%) or risky services (25%), while only 15% went to centralized exchanges, possibly due to AML/ CFT (Chainalysis Team, 2022). In 2022, almost half of illicit

crypto funds passed through a set of intermediary services primarily populated by mixers, illicit services, and DeFi protocols. However, 67% of illicit funds received by exchanges went to only five centralized exchanges, in comparison to 56.7% of 2021 (Chainalysis Team, 2023).

In the near future, regulated entities, law enforcement and supervisors will increasingly need to monitor and analyze crypto transactions to which multilayered obfuscation techniques have been applied. In addition, given the rise in the use of unhosted wallets and decentralized platforms, they will frequently operate without the assistance of centralized counterparty entities. For these reasons, we wish to highlight the value of not only researching innovative machine learning-based forensic applications, but also to adopt an interdisciplinary approach to devise compliance tools that adequately consider the way regulatory regimes are conceived and enforced. For instance, we point to the importance of reconciling the duties placed on regulated entities, the available and prospective intelligence tools, and an AML/CFT regime that is so far inherently and explicitly intermediary-based, with compliance efforts guided by rule-based risk indicators. It is for this reason that our work contextualizes forensic methods into the specifics of risk indicators. Building on these arguments, we emphasize that AML/CFT hurdles cannot be solved by simply resorting to a sophisticated transaction classification scheme. On the contrary, this process needs to be nested into a broader framework to be effective.

[pp. 13-14]

Indeed, our analysis of machine learning methods was anchored to the mitigation of the drawbacks of current rule-based systems in terms of false positives and over-reporting. Relatedly, we find that the value of

1 3

experimenting with machine learning algorithms for RegTech purposes appears dependent mainly on the relationship between the given approach and the regulatory environment within which it is deployed. In other words, the efficiency of a specific algorithm can be assessed per se, but its effectiveness in an AML/CFT context heavily depends on the extent to which the structure of the model correctly mirrors the regulatory framework—e.g., it generates alerts that are deemed relevant by regulators and mitigates the current trends of over-reporting.

From the third perspective, the supervised classification analysis we conducted could be in theory applied to other types of blockchain and cryptocurrencies, being the analysis constrained on the high-level perspective of the cryptocurrency transactions’ graph. However, there is the need for a labeled transaction dataset to build such a transaction graph. And the lack of open data further complicates the task. Indeed, we point out a few challenges identified during our investigation, related to the openness and availability of the datasets being discussed and the explainability of the results. We find it is overarching to confront these open issues and devise appropriate solutions or mitigating measures. On the one hand, our analysis suggests that it is difficult to address efficiency evaluations of machine learning-based AML/CFT tools for anomaly detection and transaction classification, since this feature appears to be increasing to the detriment of interpretability and explainability. On the other hand, it is evident from our studies that the labeled transaction datasets on which supervised learning algorithms are trained are largely proprietary. This does not only impact the development of new methods, but possibly also the transparency of the activity of supervisory bodies. That is, if the activity of the latter, just as the compliance effort of regulated entities, can be based only on the intelligence findings of solutions deploying proprietary algorithms. The interplay between the lack of explainability and the proprietary nature of the datasets suggests worrisome scenarios that call for further research. Hence, it is crucial to foster public–private synergies that can consider the AML/CFT context from a socio-technical, operational, and regulatory viewpoint.

### Conclusions


[p. 14]

Elaborating on the enthusiasm for the financial application of blockchain and DLTs that surged in the wake of Bitcoin’s launch, today the Internet of Money comprises a diverse set of socio-technical systems under constant evolution—e.g _._ , recently, DeFi schemes. Over the years, forensic techniques have been deployed to connect crypto addresses/transactions to real-world identities. This

responds to the regulatory quest to ensure accountability through identification, a concept that sits at the core of AML/CFT compliance. Meanwhile, institutions and authorities drafted anomaly indicators to help with the identification of suspicious transfers in compliance with the risk-based approach. In this context, law enforcement agencies and supervisors, often supported by the private sector, began to apply forensic methods to track relevant transfers, as well as regulated entities started benefiting from innovative RegTech solutions that partially automate the detection of anomalous activities.

In this paper, we focused on these techniques from an on-chain data analytic perspective, with a specific focus on approaches based on machine learning and graph analysis. The use of these algorithms in AML/CFT RegTech solutions shows great promise to improve the efficiency of the latter and mitigate the significant drawbacks of current rule-based methodologies. To the best of our knowledge, what we described in this work is the first experiment with GAT models for AML/CFT anomaly detection in Bitcoin. The application of this type of neural network falls in line with the recent focus on deploying machine learning techniques that leverage the inherent structure of many real-world datasets that come in the form of graphs or networks. GCN and GAT models are informed by the idea of creating generalized learning models for these structured datasets, and indeed the one we analyzed consists of (real) Bitcoin transactions represented as a directed graph network.

To conclude, we provide three levels of considerations. From an operational standpoint, our results show that the mentioned graph-based methods perform better than the baseline approaches—e.g., GCN performs better than Random Forests, with GAT being marginally worse than GCN. This encourages further experimentations with the use of GCN neural networks for AML/CFT purposes, while the novelty of our approach could spur further research into GAT-based anomaly detection techniques. From a related methodological perspective, we argue that a constant experimentation with various forensic methods, possibly leveraging the value added by transaction graphs, is crucial to reap the full benefits of analytics in an ever-evolving context of application such as the Internet of Money. These explorations, however, must be backed by serious efforts to foster constructive public–private dialog regarding the openness and the availability of labeled transaction datasets.

From a final conceptual viewpoint, we emphasize that a holistic interpretation of the interplay between AML/CFT measures and the Internet of Money—i.e., one that heeds in a comprehensive fashion socio-technical, operational, and regulatory dynamics when defining the object of the analysis—is crucial to devise effective and possibly efficient

1 3

[p. 15]

RegTech solutions. Indeed, the efficiency of a specific algorithm may not guarantee its effectiveness in an AML/CFT context, which depends on the extent to which the model responds to regulatory needs and generates relevant alerts. This relevance is influenced by regulatory, compliance, and supervisory needs, as affected by the evolution of the features of the Internet of Money. This holistic approach is especially valuable when it comes to transaction classification and anomaly detection, where a main challenge is the need to balance interpretability and explainability with the goal to reduce the share of false positives and over-reporting.

Funding Open access funding provided by Università degli Studi di Urbino Carlo Bo within the CRUI-CARE Agreement.

Data Availability The software and data is available at the following link: https:// github. com/ fmeri zzi/ GCN_ detect_ bitco in_ money_ laund ering.

Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http:// creat iveco mmons. org/ licen ses/ by/4. 0/.

### References


- Akhgar, B., Gercke, M., Vrochidis, S., & Gibson, H. (2021). _Dark Web Investigation_ . Springer. https:// doi. org/ 10. 1007/ 978-3- 030- 55343-2

- Al Jawaheri, H., Al Sabah, M., Boshmaf, Y., Erbad, A. (2020). Deanonymizing Tor hidden service users through Bitcoin transactions analysis. _Computers and Security_ , _89_ . https:// doi. org/ 10. 1016/j. cose. 2019. 101684.

- Ali, O., Ally, M., Dwivedi, Y., et al. (2020). The state of play of blockchain technology in the financial services sector: A systematic literature review. _International Journal of Information Management, 54_ , 102199.

- Alpaydin, E. (2020). _Introduction to machine learning_ . MIT press.

- Amarasinghe, N., Boyen, X., & McKague, M. (2019). A survey of anonymity of cryptocurrencies. _Acm International Conference Proceeding Series. Sydney: Association for Computing Machinery._ https:// doi. org/ 10. 1145/ 32906 88. 32906 93

- Amler, H., Eckey, L., Faust, S., Kaiser, M., Schlosser, B. (2023). DeFining DeFi : Challenges and Pathway, 2021–2024. _2021 3rd Conference on Blockchain Research & Applications for Innovative Networks and Services (BRAINS)._ https:// doi. org/ 10. 1109/ BRAIN S52497. 2021. 95697 95

- Androulaki, E., Karame, G. O., Roeschlin, M., Scherer, T., & Capkun, S. (2013). Evaluating User Privacy in Bitcoin. _LNCS, 7859_ , 34–51. https:// doi. org/ 10. 1007/ 978-3- 642- 39884- 14

- Antonopoulos, A. M. (2017). _The internet of money - two_ . Merkle Boom LLC.

Aramonte, S., Huang, W., Schrimpf, A. (2021). DeFi risks and the decentralisation illusion. _BIS Quarterly Review_ (Dec), 21–36.

Barbereau, T., Smethurst, R., Papageorgiou, O., Sedlmeir, J., & Fridgen, G. (2023). Decentralised finance’s timocratic governance: The distribution and exercise of tokenised voting rights. _Technology in Society, 73_ , 102251.

- Bartoletti, M., Carta, S., Cimoli, T., & Saia, R. (2020). Dissecting Ponzi schemes on Ethereum: Identification, analysis, and impact. _Future Generation Computer Systems, 102_ , 259–277. https:// doi. org/ 10. 1016/j. future. 2019. 08. 014

- Baxter, G., & Sommerville, I. (2011). Socio-technical systems: From design methods to systems engineering. _Interacting with Computers, 23_ (1), 4–17. https:// doi. org/ 10. 1016/j. intcom. 2010. 07. 003

- Berg, A. (2019). The identity, fungibility and anonymity of money. _Economic Papers_ (November), 1–16. https:// doi. org/ 10. 1111/ 1759- 3441. 12273.

- Biryukov, A., & Tikhomirov, S. (2019). Deanonymization and linkability of cryptocurrency transactions based on network analysis. _Proceedings - 4th IEEE European Symposium on Security and Privacy, 2019_ , 172–184. https:// doi. org/ 10. 1109/ EuroSP. 2019. 00022

- Breiman, L. (2001). Random Forests. _Machine Learning, 45_ (1), 5–32. https:// doi. org/ 10. 1023/A: 10109 33404 324

- Chainalysis Team (2022). _The 2022 Crypto Crime Report._

- Chainalysis Team (2023). _The 2023 Crypto Crime Report._

- Chang, V., Baudier, P., Zhang, H., Xu, Q., Zhang, J., & Arami, M. (2020). How blockchain can impact financial services–The overview, challenges and recommendations from expert interviewees. _Technological Forecasting and Social Change, 158_ , 120166. https:// doi. org/ 10. 1016/j. techf ore. 2020. 120166

- Chen, W., Zheng, Z., Ngai, E. C., Zheng, P., & Zhou, Y. (2019). Exploiting Blockchain Data to Detect Smart Ponzi Schemes on Ethereum. _IEEE Access, 7_ (c), 37575–37586. https:// doi. org/ 10. 1109/ ACCESS. 2019. 29057 69

- CipherTrace (2021). _Cryptocurrency crime and anti-money laundering report._ ciphertrace. https:// ciphe rtrace. com/ crypt ocurr encycrime- and- anti- money- laund ering- report- august- 2021/

- Defferrard, M., Bresson, X., Vandergheynst, P. (2016). Convolutional neural networks on graphs with fast localized spectral filtering. _Advances in neural information processing systems_ , _29_ .

- Desmond, D. B., Lacey, D., & Salmon, P. (2019). Evaluating cryptocurrency laundering as a complex socio-technical system: A systematic literature review. _Journal of Money Laundering Control, 22_ (3), 480–497. https:// doi. org/ 10. 1108/ JMLC- 10- 2018- 0063

- Directive (EU) 2018/843 (2018). _Directive (EU) 2018/843 of the European Parliament and of the Council of 30 May 2018 amending Directive (EU) 2015/849 on the prevention of the use of the financial system for the purposes of money laundering or terrorist financing, and amending Directives 2009/138/EC and 2013/36/ EU._

- Eddin, A.N., Bono, J., Aparício, D., Polido, D., Ascensão, J.T., Bizarro, P., & Ribeiro, P. (2021). Anti-money laundering alert optimization using machine learning with graphs _. Arxiv._ https:// doi. org/ 10. 48550/ ARXIV. 2112. 07508.

- Edmunds, J.C. (2020). _Rogue money and the underground economy. an encyclopedia of alternative and cryptocurrencies_ . ABC-CLIO.

- European Commission (2021). _Anti-money laundering and countering the financing of terrorism legislative package._ Retrieved from https:// ec. europa. eu/. Accessed Nov 2022

- Europol (2020). _Internet Organised Crime Threat Assessment 2020._ Retrieved from https:// www. europ ol. europa. eu/. Accessed Nov 2022

[pp. 15-16]

- FATF (2020). _Virtual assets red flag indicators of money laundering and terrorist financing._ Retrieved from http:// www. fatf- gafi. org/. Accessed Nov 2022

- FATF (2021). _Second 12-month review of the revised fatf standards on virtual assets and virtual asset service providers._ Retrieved from https:// www. fatf- gafi. org/. Accessed Nov 2022

1 3

- FATF (2022). _International standards on combating money laundering and the financing of terrorism & proliferation: The FATF recommendations._ Retrieved from https:// www. fatf- gafi. org/. Accessed Nov 2022

- Filippi, P. D., & Wright, A. (2018). _Blockchain and the law: The rule of code_ . Harvard University Press.

- Fleder, M., Kester, M.S., & Pillai, S. (2015). Bitcoin transaction graph analysis. _Arxiv_ . https:// arxiv. org/ abs/ 1502. 01657. Accessed Nov 2022

- Goforth, C.R. (2020). Crypto assets: A Fintech forecast. (September), 5–25.

- Harrigan, M., & Fretter, C. (2016). The unreasonable effectiveness of address clustering. _2016 IEEE conferences on ubiquitous intelligence & computing, advanced and trusted computing, scalable computing and communications, cloud and big data computing, internet of people, and smart world congress._ IEEE.

- Hilbe, J. M. (2009). _Logistic regression models_ . Chapman and hall/CRC. Ince, P., Liu, J. K., & Zhang, P. (2018). Adding confidential transactions to cryptocurrency IOTA with bulletproofs. _Springer_ . https:// doi. org/ 10. 1007/ 978-3- 030- 02744- 53

- Kamišalić, A., Kramberger, R., & Fister, I. (2021). Synergy of blockchain technology and data mining techniques for anomaly detection. _Applied Sciences (Switzerland), 11_ (17), 7987. https:// doi. org/ 10. 3390/ app11 177987

- Katona, T. (2021). Decentralized finance: The possibilities of a blockchain “Money Lego” system. _Financial and Economic Review_ , _20_ (1), 74–102. https:// doi. org/ 10. 33893/ fer. 20.1. 74102.

- Kipf, T.N., & Welling, M. (2016). Semi-supervised classification with graph convolutional networks. https:// arxiv. org/ abs/ 1609. 02907. Accessed Nov 2022


---

[previous part](text-002.md) | [source overview](overview.md) | [next part](text-004.md)

[^original]: Nadia Pocher, Mirko Zichichi, Fabio Merizzi, Muhammad Zohaib Shafiq, Stefano Ferretti, "Detecting anomalous cryptocurrency transactions: An AML/CFT application of machine learning-based forensics" (2023-07-26). https://link.springer.com/article/10.1007/s12525-023-00654-3
