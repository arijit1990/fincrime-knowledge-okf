---
type: Source Text
title: Privacy Technologies for Financial Intelligence - part 3 of 4 (pp. 29-41)
description: 'Verbatim extracted text, pp. 29-41: Privacy Technologies for Financial Intelligence > 5. Real-World Case Studies; Privacy Technologies for Financial Intelligence > 6. Discussion; Privacy Technologies for Financial Intelligence > 7. Conclusion; and 1 more sections'
resource: https://arxiv.org/abs/2408.09935
tags:
- academic_finding
- global_academic
- preprint
- privacy_data_protection
- public_private_partnership
status: stable
source_id: arxiv-privacy-technologies-for-financial-intelligence
issuer: arxiv
issuer_name: arXiv
jurisdictions:
- GLOBAL_ACADEMIC
tier: 3
instrument_type: preprint
normative_force: academic_finding
publication_date: '2024-08-19'
legal_status: unknown
part: 3
parts_total: 4
content_mode: full_text
generated:
  by: process:fincrime-kb-build
  at: '2026-11-17T02:21:50Z'
verified:
- by: process:kb-validate/verbatim-coverage
  at: '2026-11-17T02:21:50Z'
sources:
- id: original
  resource: https://arxiv.org/abs/2408.09935
  title: Privacy Technologies for Financial Intelligence
  author: org:arxiv
  last_modified: '2024-08-19T00:00:00Z'
---

# Privacy Technologies for Financial Intelligence

[previous part](text-002.md) | [source overview](overview.md) | [next part](text-004.md)

> Verbatim text extracted from the original (arXiv, 2024-08-19), part 3 of 4, pp. 29-41. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **academic finding**.[^original]

## Privacy Technologies for Financial Intelligence


### 5. Real-World Case Studies


[p. 29]

|Project|Participants|Use cas|e|
|---|---|---|---|
|EnveilZeroRevealInter-Bank Secure andPrivate Data Collabo-ration [4]|An EU-based financial institu-tionandathird-partydataprovider|Transactiontracing and ogy matching|flow typol-|
|DualitySecurePlusQuery [4]|UK and Canadian Banks|Transactiontracing and ogy matching|flow typol-|
|DANIE consortium [4]|UK-based consortium of banks|Suspicious plist|ersons|
|Privitar SecureLink [4]|Public and private Institutes inan EU member state|Suspicious plist|ersons|
|BNY Mellon and In-pher XOR [48]|BNY Mellon|Collaborativelearning||
|UKTri-bankinitia-tive [49]|Three UK banks|Transactiontracing|flow|
|AUSTRAC’sFintelAllianceAlertingProject [50, 51]|Led by AUSTRAC Australia anddelivered by the public-privatepartnership Fintel Alliance|Transactiontracing|flow|
|AMLBridgePlat-form [52]|Ten banks and several non-banksin Estonia|Transactiontracing and ogy matching|flow typol-|
|TransactionMoni-toringNetherlands(TMNL) [53]|Five banks in Netherlands|Transactiontracing|flow|
|DeepProtect [54]|Five banks in Japan|Collaborativelearning||
|Project Aurora [55]|Led by Bank for InternationalSettlements and participated by29 financial institutions in sixEuropean countries|Collaborativelearning||
|COSMIC [52, 56]|OwnedandoperatedbytheMonetary Authority of Singa-pore(MAS).Theisaco-development with the Commer-cial Affairs Department (CAD)of the Singapore Police Force,and six major banks (Citibank,DBS, HSBC, OCBC, StandardChartered Bank and UOB).|Transactiontracing and ogy matching|flow typol-|

[pp. 30-31]

encryption to provide secure and automated multiparty collaboration which allows banks to query about higher risk customers. Since that FCA TechSprint, the Enveil suite of solutions have developed in maturity and are now used in multiple sensitive domains.8

_Duality SecurePlus__TM_ _Query on Financial Data [4]._ The product Duality SecurePlusTM Query enables financial crime and compliance teams to carry out collaborative investigations across groups, institutions and borders by keeping sensitive data encrypted throughout the process. This product allows cross-border collaboration between financial crime and compliance teams. The product allows participant to query distributed data silos while keeping the sensitive data encrypted throughout the querying process. A case study between several banks in the UK and Canada demonstrated the capability of banks to match customers that includes external data sets, without disclosing their original query to the data owner. This allows different financial intelligence teams to securely query each other’s data. The system also supports to reduce false positives, improve outcomes, increase efficiency, and most importantly effectively expose financial crime networks.9

_DANIE Consortium [4]._ Project DANIE is a collaborative initiative involving multiple financial institutions from EU Member States, aimed at enhancing banking data quality through the utilisation of privacy technologies. The project employs a combination of secure hardware and software components, along with secure multiparty computation and homomorphic encryption. The primary objective of DANIE is to improve data quality by matching datasets across participating organisations to identify discrepancies and outliers, while simultaneously preserving the anonymity and security of the matched data through these technologies. In addition to its application in enhancing data reconciliation and subsequently improving the Know Your Customer (KYC) process, DANIE has the potential to be adapted for addressing the Suspicious Person List (SPL) cases discussed in Section 4.1. This can be achieved by encrypting an SPL and uploading it to the DANIE platform to request confirmation of each individual’s presence within the participating financial institutions.

> 8Enveil Wins Army Linchpin Contract to Deliver Secure AI

> 9Leverage Secure Data Sharing to Fight Money Laundering

_BNY Mellon and Inpher XOR [48]._ The Bank of New York Mellon Corporation uses machine-learning (ML) based fraud detection algorithms to find hidden patterns in money laundering networks. Together with the Inpher’s XOR platform, BNY Mellon built a novel collaborative fraud detection framework leveraging Secure Multiparty Computation. Inpher’s technology enabled BNY Mellon to access sensitive data across borders or jurisdictional silos for training ML algorithms such as linear and logistic regression as well as XGBoost. The solution achieved a high level of precision, computing models identically as if they were computed in clear text. BNY Mellon’s project demonstrated that the number of false positives was reduced by 20% and the number of true positives was increased by 20%. The solution thus reduced investigation workload and increased fraud detection efficiency.

[pp. 31-32]

_UK Tri-bank initiative [49]._ This is a proof-of-concept (POC) system developed by three UK banks to analyse historical data on small and medium sized corporate client datasets. The system used the FutureFlow CrossBank Financial Crime Analytics Platform to analyse transaction data between banks. In their POC study, banks analysed approximately 200,000 accounts for money laundering risk. In this system, the transaction data is encrypted to protect sensitive data before using to identify links between the transactions. This allowed the banks to identify potential money laundering networks based on the patterns in the transaction data.

_AUSTRAC’s Fintel Alliance Alerting Project [50]._ The FINTEL Alliance comprises representatives from both public and private partner organizations that collaborate to address complex or emerging crimes affecting the community, necessitating a joint public-private approach. The aim of this project is to develop different approaches which would allow the identification of complex money transferring networks used by criminal gangs. The project used a federated platform with homomorphic encryption technologies where entities could report or provide access to the agreed dataset via an API. The project was tested in a simulated federated architecture using a sample of real data, covering more than 100 million accounts.

_AML Bridge Platform [52]._ AML Bridge is a secure platform provided by Salv. The platform uses an end-to end encryption technique which allows financial institutions to securely exchange of pseudonymised transaction data. The platform was first tested as a POC on four of Estonia’s largest banks and later expanded to all Estonian banks. In their POC data owners can

also limit what queries it allows from its own data sources while the requesting party is not revealed to the data owner. In their querying protocol, the platform first encrypts the data at the source. Next data is aggregated with other parties’ and stored in three trusted hosts using secure multiparty computation. Finally, within the requesting party’s trusted environment, the platform aggregates the data results without revealing the original data source(s).

_Transaction Monitoring Netherlands (TMNL) [53]._ This is an initiative consists of five Dutch banks including ABN AMRO, ING, Rabobank, Triodos Bank and De Volksbank. The main aim of this initiative is to combine transaction data of business accounts from these banks to gain a complete view of money flows by criminal networks. The initiative uses a central trusted data store where each bank could upload their data. The data could then aggregate by combining these transactions and the consortium (the group of banks) could monitor and report potentially suspicious patterns to the others. central data store where the consortium combines these transactions, monitors them, and reports potentially suspicious patterns. The central data store encrypts data at rest, which can only be viewed when when suspicions of money laundering or terrorist financing arise Sensitive information is encrypted and viewed only when suspicions of money laundering or terrorist financing arise.

[pp. 32-33]

_DeepProtect [54]._ This is research project by National Institute of Information and Communications Technology (NICT) in Japan. In this project, NICT collaborated with five banks in Japan including Chiba Bank, Ltd., MUFG Bank, Ltd., the Chugoku Bank, Ltd., Sumitomo Mitsui Trust Bank, Ltd., and the Iyo Bank, Ltd. The aim of this project was to build models for detecting criminals’ bank accounts and fraudulent transactions in customers accounts. DeepProtect employs a FL framework which enables each bank to run a local model using its own data while collaboratively train a global model with data from other banks. For privacy preservation, the implementation used a homomorphic encryption scheme in a symmetric key environment.

_Project Aurora [55]._ This is an initiative led by the Bank for International Settlements (BIS). The aim of this project is to identify money laundering between banks and cross-border financial institutions by analysing the connected payment data. The project uses different privacy and security

techniques with ML and network analysis methods for identifying potential suspicious transactions. Phase 1 of the project demonstrated that the combinations of these technologies provides more effective identification of money laundering networks compared to traditional siloed and rules-based approaches. In their experimental setting, consisting 29 financial institutions in six different European countries, the project detected potentially up to 3 times more money laundering involved complex schemes and reduced false positives by up to 80%.

_COSMIC [56]._ COSMIC is a secure digital platform co-developed by Monetary Authority of Singapore (MAS) and six major commercial banks in Singapore including DBS, OCBC, UOB, Citibank, HSBC and Standard Chartered. Released in 2024, COSMIC allows financial institutions to securely share transaction data and information about suspicious accounts with one another. The initial aim of COSMIC is to provide a easier and efficient data sharing platform for FIs to detect and thereby deter criminal activity. Currently, information sharing in COSMIC is voluntary. The platform currently supports three key financial crime risks, (1) misuse of legal persons, (2) misuse of trade finance for illicit purposes and (3) proliferation financing. COSMIC is owned and operated by the MAS.

The above shortlist of projects is quite compelling and is demonstrative of the increasing global interest in the adoption of maturing privacy technologies by major financial institutions, both public and private, to combat financial crimes.

### 6. Discussion


[pp. 33-34]

_Legislative Reform and Privacy Technologies._ Financial intelligence equips law enforcement and financial institutions with sophisticated analytical tools and data-driven methodologies to proactively detect and prevent financial crimes. While financial intelligence plays a crucial role in supporting AntiMoney Laundering (AML) and Counter-Terrorist Financing (CTF) regimes by delivering actionable intelligence and insights, it may present challenges in relation to data privacy regulations such as Australia’s Privacy Act and European Union’s General Data Protection Regulation (GDPR). These challenges arise particularly when there is a discrepancy between the initial purpose for which data was collected by financial institutions and its subsequent use in

various financial intelligence applications. While public and private sectors, industry associations and regulatory bodies are actively working to harmonise AML/CTF and data privacy regulations, such changes often involve lengthy and uncertain political approval and implementation processes.

From the practical perspective of being able to do something about complex financial crimes _today_ , we advocate for the integration of privacy-preserving technologies within financial intelligence tools, not just as a mitigation strategy while waiting for legal experts to navigate the complex AML/CTF reform landscape [57], but also to inform those AML/CTF reform discussions. This approach offers several benefits. First, privacy-preserving technologies can be swiftly implemented, allowing financial institutions and financial intelligence units to address data privacy concerns while fulfilling AML/CTF obligations. Second, adopting privacy-preserving methods helps institutions build trust with customers and stakeholders by demonstrating a commitment to both data protection and effective financial crime prevention. Finally, privacy-preserving solutions offer a flexible framework that can adapt to evolving regulatory requirements, helping institutions stay compliant as laws and regulations are updated to address new financial technologies and emerging criminal threats.

_Trade-offs and Practical Considerations._ In practical financial intelligence applications, selecting the most appropriate privacy techniques is crucial for ensuring data security, regulatory compliance, and maintaining user trust at sustainable costs. There are often trade-offs involved in such choices. With the increasing industry focus on responsible AI practices [58, 59], there is also an emerging need to understand the possible interactions between privacy requirements and related issues like explainability and fairness [60, 61, 62]. Scholars and practitioners must look ahead to how AI itself may transform AML/CTF, potentially enabling new, automated, or hybrid methods especially when combined with emerging technologies such as decentralised autonomous organisations [63]. Strategic foresight and scenario-based methodologies may therefore be essential to anticipate and prepare for the future evolution of AI-enabled AML/CTF. To inform those broader issues, we offer here a few observations on how privacy-utility trade-offs are usually handled for the different privacy technologies.

First of all, it is worth noting that the use of homomorphic encryption (HE) and secure multiparty computation (MPC) in financial-intelligence algorithms like private set intersection, graph pattern matching, and statistical

[p. 35]

model learning do not usually result in any change to the output of those algorithms. This is because HE and MPC allow an algorithm to be evaluated in an encrypted space but they do not otherwise change the nature of a given algorithm. The primary consideration when using HE and MPC is thus whether the specific algorithm and parameters chosen provide, at reasonable organisational and monetary costs, sufficient provable security against adversaries with access to potentially large computational resources and arbitrary background and side information.

In contrast, the use of differential privacy (DP) and federated learning (FL) to privatise a financial-intelligence algorithm can result in actual changes to the output of the algorithm. There are rich and well-established frameworks [64, 65, 19] to study trade-offs between privacy and utility when using DP, and these frameworks work well in conjunction with standard techniques for model evaluation and selection [66] in both federated learning and more typical setups. Addressing these questions will be central to future research in this field.

### 7. Conclusion


We hope this paper enhances public understanding of privacy-preserving financial intelligence through the various AML/CTF use cases we explore. The use cases highlight the evolving nature of financial crimes and the necessity for ongoing innovation in privacy technologies to address emerging threats effectively. Having said that, for financial institutions and regulatory bodies, adopting privacy technologies involves careful consideration of both technological and operational aspects. Effective implementation strategies must balance the trade-offs between data privacy and the quality and efficiency of analysis. While these technologies address immediate challenges, they are not a substitute for comprehensive regulatory reforms. Further and continuous refinement of regulations is essential to align financial crime prevention efforts with data privacy goals.

_Acknowledgements._ We thank the many former colleagues in AUSTRAC and financial crime units in major Australian financial institutions who spent many hours teaching us the intricacies of the financial intelligence business. We are grateful to many of them for continuing to play an important role to keep our financial system and our country safe.

### References


[pp. 36-37]

- [1] N. Lynch, The Lucky Laundry, Harper Collins, Syndey, NSW, 2022.

- [2] C. Leuprecht, J. Ferrill (Eds.), Dirty Money: Financial Crime in Canada, McGill-Queen’s University Press, Kingston, ON, 2023.

- [3] C. Leuprecht, A. Crockfield, P. Simpson, M. Haseeb, Tracking transnational terrorist resourcing nodes and networks, Florida State University Law Review (2019).

- [4] N. Maxwell, Innovation and discussion paper: Case studies of the use of privacy preserving analysis to tackle financial crime, Future of Financial Intelligence Sharing (FFIS) research programme (2021).

- [5] J. Madinger, Money laundering: A guide for criminal investigators, CRC Press, Boca Raton, Florida, 2011.

- [6] W. C. Gilmore, Dirty Money: The Evolution of International Measures to Counter Money Laundering and the Financing of Terrorism, 3rd Edition, Council of Europe Publishing, Strasbourg, 2004.

- [7] Y. Zhang, K. S. Ng, T. Churchill, P. Christen, Scalable entity resolution using probabilistic signatures on parallel databases, in: Proceedings of the 27th ACM International Conference on Information and Knowledge Management, 2018, pp. 2213–2221.

- [8] D. Savage, Q. Wang, P. Chou, X. Zhang, X. Yu, Detection of money laundering groups using supervised learning in networks, arXiv:1608.00708 (2016).

- [9] D. Savage, Q. Wang, X. Zhang, P. L. Chou, X. Yu, Detection of money laundering groups: Supervised learning on small networks, in: AI and OR for Social Good, Papers from the AAAI Workshop, 2017.

- [10] D. Savage, X. Zhang, P. Chou, X. Yu, Q. Wang, Distributed mining of contrast patterns, IEEE Trans. Parallel Distributed Syst. 28 (7) (2017) 1881–1890.

- [11] P. Reuter, E. M. Truman, Chasing Dirty Money: The Fight Against Money Laundering, Institute for International Economics, Washington, 2004.

- [12] P. Christen, T. Ranbaduge, R. Schnell, Linking Sensitive Data: Methods and Techniques for Practical Privacy-Preserving Information Sharing, Springer, 2020.

- [13] C. Gentry, Fully homomorphic encryption using ideal lattices, in: Proceedings of the 41st Annual ACM Symposium on Theory of Computing, 2009, pp. 169–178.

[pp. 37-38]

- [14] G. Alagic, et al., Status report on the third round of the NIST post-quantum cryptography standardization process, Tech. rep., NIST (2022).

- [15] L. Chi, X. Zhu, Hashing techniques: A survey and taxonomy, ACM Computing Surveys 50 (1) (2017) 1–36.

- [16] M. Aledhari, R. Razzak, R. M. Parizi, F. Saeed, Federated learning: A survey on enabling technologies, protocols, and applications, IEEE Access 8 (2020) 140699–140725.

- [17] D. C. Nguyen, M. Ding, P. N. Pathirana, A. Seneviratne, J. Li, H. V. Poor, Federated learning for internet of things: A comprehensive survey, IEEE Communications Surveys & Tutorials 23 (3) (2021) 1622–1658.

- [18] Z. Zhao, M. Luo, W. Ding, Deep leakage from model in federated learning (2022).

- [19] K. Nissim, Privacy: From database reconstruction to legal theorems, in: Principles of Database Systems, 2021, pp. 33–41.

- [20] Y. Li, M. Purcell, T. Rakotoarivelo, D. Smith, T. Ranbaduge, K. S. Ng, Private graph data release: A survey, ACM Computing Surveys 55 (11) (2023) 1–39.

- [21] M. J. Freedman, K. Nissim, B. Pinkas, Efficient private matching and set intersection, in: International Conference on the Theory and Applications of Cryptographic Techniques, Springer, 2004, pp. 1–19.

- [22] P. Balboni, M. Macenaite, Privacy by design and anonymisation techniques in action: Case study of Ma3tch technology, Computer Law & Security Review 29 (4) (2013) 330–340.

- [23] F. Mouzakiti, Cooperation between financial intelligence units in the EU: Stuck in the middle between the GDPR and the police data protection directive, New Journal of European Criminal Law (2020).

- [24] H. Chen, K. Laine, P. Rindal, Fast private set intersection from homomorphic encryption, in: Proceedings of the ACM SIGSAC Conference on Computer and Communications Security, 2017, pp. 1243–1255.

[pp. 38-39]

- [25] M. Rosulek, N. Trieu, Compact and malicious private set intersection for small sets, in: Proceedings of the ACM SIGSAC Conference on Computer and Communications Security, 2021, pp. 1166–1181.

- [26] M. Chase, P. Miao, Private set intersection in the internet setting from lightweight oblivious PRF, in: Annual International Cryptology Conference, Springer, 2020, pp. 34–63.

- [27] M. Purcell, Y. Li, K. S. Ng, Split, count, and share: a differentially private set intersection cardinality estimation protocol, in: Uncertainty in Artificial Intelligence, PMLR, 2023, pp. 1684–1694.

- [28] M. Brand, H. Ivey-Law, T. Churchill, FinTracer: A privacy-preserving mechanism for tracing electronic money, Cryptology ePrint Archive (2023).

- [29] AUSTRAC, National disability insurance scheme fraud prevention financial crime guide, `https://www.austrac.gov.au/sites/default/ files/2020-12/NDIS%20Fraud%20Prevention%20Financial% 20Crime%20Guide.pdf` (2020).

- [30] P. Burkhardt, Optimal algebraic breadth-first search for sparse graphs, ACM Transactions on Knowledge Discovery from Data 15 (5) (2021) 1–19.

- [31] T. ElGamal, A public key cryptosystem and a signature scheme based on discrete logarithms, IEEE Transactions on Information Theory 31 (4) (1985) 469–472.

- [32] D. J. Bernstein, Curve25519: new Diffie-Hellman speed records, in: 9th International Conference on Theory and Practice in Public-Key Cryptography, Springer, 2006, pp. 207–228.

- [33] M. Kearns, A. Roth, Z. S. Wu, G. Yaroslavtsev, Private algorithms for the protected in social network search, Proceedings of the National Academy of Sciences 113 (4) (2016) 913–918.

- [34] I. Molloy, S. Chari, U. Finkler, M. Wiggerman, C. Jonker, T. Habeck, Y. Park, F. Jordens, R. van Schaik, Graph analytics for real-time scoring of cross-channel transactional fraud, in: 20th International Conference on Financial Cryptography and Data Security, Springer, 2017, pp. 22– 40.

[pp. 39-40]

- [35] A. Sangers, M. van Heesch, T. Attema, T. Veugen, M. Wiggerman, J. Veldsink, O. Bloemen, D. Worm, Secure multiparty pagerank algorithm for collaborative fraud detection, in: Financial Cryptography and Data Security: 23rd International Conference, Springer, 2019, pp. 605– 623.

- [36] M. B. van Egmond, V. Dunning, S. van den Berg, T. Rooijakkers, A. Sangers, T. Poppe, J. Veldsink, Privacy-preserving anti-money laundering using secure multi-party computation, Cryptology ePrint Archive (2024).

- [37] M. Brand, T. Churchill, C. Friedrich, Nonlinear computations on FinTracer tags, Cryptology ePrint Archive (2023).

- [38] I. Dinur, K. Nissim, Revealing information while preserving privacy, in: Proceedings of the ACM Symposium on Principles of Database Systems, 2003, pp. 202–210.

- [39] C. Dwork, F. McSherry, K. Talwar, The price of privacy and the limits of LP decoding, in: ACM symposium on Theory of Computing, 2007, pp. 85–94.

- [40] R. A. Popa, C. M. Redfield, N. Zeldovich, H. Balakrishnan, CryptDB: Protecting confidentiality with encrypted query processing, in: Proceedings of the 23rd ACM Symposium on Operating Systems Principles, 2011, pp. 85–100.

- [41] H. Yousuf, S. Salloum, A. Aburayya, M. Al-Emran, K. Shaalan, A systematic review of CryptDB: Implementation, challenges, and future opportunities, J. Manag. Inf. Decis. Sci 24 (1) (2021) 1–16.

- [42] V. Mothukuri, R. M. Parizi, S. Pouriyeh, Y. Huang, A. Dehghantanha, G. Srivastava, A survey on security and privacy of federated learning, Future Generation Computer Systems 115 (2021) 619–640.

- [43] T. Suzumura, Y. Zhou, R. Kawahara, N. Baracaldo, H. Ludwig, Federated learning for collaborative financial crimes detection, in: Federated learning: A comprehensive overview of methods and applications, Springer, 2022, pp. 455–466.

[pp. 40-41]

- [44] S. Dhiman, S. Nayak, G. K. Mahato, A. Ram, S. K. Chakraborty, Homomorphic encryption based federated learning for financial data security, in: 4th International Conference on Computing and Communication Systems, IEEE, 2023, pp. 1–6.

- [45] S. Hardy, W. Henecka, H. Ivey-Law, R. Nock, G. Patrini, G. Smith, B. Thorne, Private federated learning on vertically partitioned data via entity resolution and additively homomorphic encryption, arXiv:1711.10677 (2017).

- [46] D. Byrd, A. Polychroniadou, Differentially private secure multi-party computation for federated learning in financial applications, in: Proceedings of the First ACM International Conference on AI in Finance, 2020, pp. 1–9.

- [47] Y. Zhang, T. Churchill, K. S. Ng, Exploiting redundancy, recurrency and parallelism: How to link millions of addresses with ten lines of code in ten minutes, in: Australasian Conference on Data Mining, Springer, 2017, pp. 107–122.

- [48] Inpher, New approaches to tackling financial crimes: Secure data collaboration with XOR, Tech. rep., BNY Mellon (2021).

- [49] N. Maxwell, Paper 1: The case for national policy-makers to unleash the potential of payments infrastructure to identify economic crime risk, Future of Financial Intelligence Sharing (FFIS) research programme (2024).

- URL `https://www.future-fis.com/uploads/3/7/9/4/3794525/ ffis_-_payments_policy_discussion_paper_1_-_unleashing_the_ potential_of_payments_infrastructure_to_identify_economic_ crime_risk.pdf`

- [50] P. Chadderton, S. Norton, Public-private partnerships to disrupt financial crime: An exploratory study of Australia’s Fintel Alliance, Tech. rep., SWIFT Institute Working Paper (2019).

- [51] B. Scott, M. Webster, Anti-money laundering/counter-terrorism financing tranche 2 reform in Australia - An opportunity for intelligence to lead the way, International Journal of Contemporary Intelligence Issues 1 (1) (2024) 3–19.

- [52] FATF, Partnering in the fight against financial crime: Data protection, technology and private sector information sharing, The Financial Action Task Force (FATF) (2022). URL `https://www.fatf-gafi.org/content/dam/fatf-gafi/ guidance/Partnering-int-the-fight-against-financialcrime.pdf`


---

[previous part](text-002.md) | [source overview](overview.md) | [next part](text-004.md)

[^original]: arXiv, "Privacy Technologies for Financial Intelligence" (2024-08-19). https://arxiv.org/abs/2408.09935
