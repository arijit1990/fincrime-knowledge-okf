---
type: Source Text
title: 'Detecting anomalous cryptocurrency transactions: An AML/CFT application of machine learning-based forensics - part 1 of 4 (pp. 1-6)'
description: 'Verbatim extracted text, pp. 1-6: Detecting anomalous cryptocurrency transactions: An AML/CFT application of machine learning‑based forensics; Detecting anomalous cryptocurrency transactions: An AML/CFT application of machine learning‑based forensics > Abstract; Detecting anomalous cryptocurrency transactions: An AML/CFT application of machine learning‑based forensics > Introduction; and 2 more sections'
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
part: 1
parts_total: 4
content_mode: full_text
generated:
  by: process:fincrime-kb-build
  at: '2026-11-21T18:42:19Z'
verified:
- by: process:kb-validate/verbatim-coverage
  at: '2026-11-21T18:42:19Z'
sources:
- id: original
  resource: https://link.springer.com/article/10.1007/s12525-023-00654-3
  title: 'Detecting anomalous cryptocurrency transactions: An AML/CFT application of machine learning-based forensics'
  author: org:academic_publisher
  last_modified: '2023-07-26T00:00:00Z'
---

# Detecting anomalous cryptocurrency transactions: An AML/CFT application of machine learning-based forensics

[source overview](overview.md) | [next part](text-002.md)

> Verbatim text extracted from the original (Academic publisher / repository, 2023-07-26), part 1 of 4, pp. 1-6. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **academic finding**.[^original]

[p. 1]

Electronic Markets (2023) 33:37 https://doi.org/10.1007/s12525-023-00654-3

RESEARCH PAPER

Nadia Pocher1 · Mirko Zichichi2 · Fabio Merizzi2 · Muhammad Zohaib Shafiq2 · Stefano Ferretti3

## Detecting anomalous cryptocurrency transactions: An AML/CFT application of machine learning‑based forensics


Received: 29 September 2022 / Accepted: 30 May 2023 / Published online: 26 July 2023 © The Author(s) 2023

In shaping the Internet of Money, the application of blockchain and distributed ledger technologies (DLTs) to the financial sector triggered regulatory concerns. Notably, while the user anonymity enabled in this field may safeguard privacy and data protection, the lack of identifiability hinders accountability and challenges the fight against money laundering and the financing of terrorism and proliferation (AML/CFT). As law enforcement agencies and the private sector apply forensics to track crypto transfers across ecosystems that are socio-technical in nature, this paper focuses on the growing relevance of these techniques in a domain where their deployment impacts the traits and evolution of the sphere. In particular, this work offers contextualized insights into the application of methods of machine learning and transaction graph analysis. Namely, it analyzes a real-world dataset of Bitcoin transactions represented as a directed graph network through various techniques. The modeling of blockchain transactions as a complex network suggests that the use of graph-based data analysis methods can help classify transactions and identify illicit ones. Indeed, this work shows that the neural network types known as Graph Convolutional Networks (GCN) and Graph Attention Networks (GAT) are a promising AML/CFT solution. Notably, in this scenario GCN outperform other classic approaches and GAT are applied for the first time to detect anomalies in Bitcoin. Ultimately, the paper upholds the value of public–private synergies to devise forensic strategies conscious of the spirit of explainability and data openness.

### Abstract


Keywords Blockchain technology · Financial technology · Network forensics · Graph analysis · AML/CFT

JEL Classification G18 · O33

|Responsible Editor: Gilbert Fridgen|
|---|

- Stefano Ferretti stefano.ferretti@uniurb.it Nadia Pocher nadia.pocher@uab.cat Mirko Zichichi mirko.zichichi2@unibo.it Fabio Merizzi fabio.merizzi@studio.unibo.it Muhammad Zohaib Shafiq muhammad.shafiq6@studio.unibo.it

### Introduction


[pp. 1-2]

- 1 Universitat Autònoma de Barcelona, Bellaterra, Spain 2 University of Bologna, Bologna, Italy

> 3 University of Urbino, Piazza Della Repubblica, 13, 61029 Urbino, Italy

Over the last 15 years, the application of blockchain and distributed ledger technologies (DLTs) to the financial domain has generated an enthusiastic hype (Ali et al., 2020). Building on years of research in distributed systems and cryptography, the launch of Bitcoin (Nakamoto, 2008) showed it is possible to reliably record information (e.g., transactions) without trusting a centralized party. This opened the way to peer-to-peer transfers and direct participation in a digital global economy. However, the features of disintermediation and perceived anonymity of this Internet of Money (Antonopoulos, 2017) cause regulatory unease.1 Indeed, they defy accountability and fuel

> 1 The Internet of Money is neither a legal nor a technical definition; in this work, the term refers to the entire set of cryptocurrency ecosystems, thus including the part of the Internet of Value (Tapscott and Euchner (2019)) that relates to payment tokens.

Vol.:(0123456789)1 3

fears of exploitation for illicit purposes (Chang et al., 2020). As confirmed by industry estimates, in 2022, the volume of crypto-related illicit activity hit USD 20.6 billion and increasingly involves decentralized finance (DeFi) (Chainalysis Team, 2023). This challenges the fight against money laundering and the financing of terrorism and proliferation (AML/CFT).

The AML/CFT framework consists of a set of laws, regulations and procedures that aim to protect the integrity of the financial system mainly by making the concealment of the origin of illicit profits significantly troublesome (Pocher & Zichichi, 2022). Since the identification of customers and counterparties is a key part of AML/CFT compliance for entities such as financial institutions and cryptoasset service providers, some features of the Internet of Money that hinder identifiability emerge as problematic. However, cryptorelated laundering appears heavily concentrated: most value originating from illicit addresses is seemingly sent to few services, often built for criminal purposes (Chainalysis Team, 2023). This suggests the key role of effective, and possibly efficient, classification of transactions performed by/received from specific entities to detect and investigate illicit activities in the sphere at hand.

[p. 2]

In this context, the picture of untraceable cryptocurrency transfers and individual freedom from governmental control warrants a two-fold interpretation: while user anonymity can safeguard privacy and data protection, lack of identifiability hampers investigation, enforcement, and accountability. Two sets of mutually influencing socio-technical events emerged: law enforcement agencies and private sector providers of RegTech solutions started exploring techniques to “follow the money” across blockchain ecosystems (Bartoletti et al., 2020; Biryukov & Tikhomirov, 2019; Chen et al., 2019; Lischke & Fabian, 2016; Meiklejohn et al., 2016; MorenoSanchez et al., 2016), while the unveiled insufficiency in Bitcoin’s anonymity spurred altcoin projects (e.g., Monero, ZCash) to implement advanced cryptographic methods that require new analytical tools.2

Against this backdrop, in this paper, we focus on the value of intelligence techniques to provide insights into the Internet of Money’s ecosystems, with specific regard to machine learning techniques, network, and transaction graph analysis (Fleder et al., 2015; Ober et al., 2013; Weber et al., 2019; Wu et al., 2021). We first provide a background on a notion of anonymity that is specific to the Internet of Money and on the interplay of AML/CFT and blockchain forensics. Consequently, we focus on the anomaly detection approaches that led to our experiments. In particular, we employed a dataset obtained from a set of Bitcoin transactions, represented as

> 2 The term “RegTech”, short for “regulatory technology”, refers to the use of new technologies to aid regulatory and compliance processes, mainly through FinTech software applications.

a directed graph network (Weber et al., 2019). The modeling of Bitcoin transactions as a complex network fosters the use of specific graph-related analysis techniques, which usually help identify peculiar nodes of a network (Pocher & Zichichi, 2022). As per our central hypothesis, since money laundering involves transaction flow relationships between entities creating a graph structure, AML/CFT analytics could benefit from novel graph analysis techniques in machine learning, namely Graph Convolutional Networks (GCN) and Graph Attention Networks (GAT).

[pp. 2-3]

The results of our experiments show that GCN and GAT neural network typologies are promising solutions for AML/ CFT. This is in opposition to a state-of-the-art work in which a baseline supervised learning algorithm, i.e., non-graphbased, such as the Random Forest, provided the best performances (Weber et al., 2019). Thus, we underline the value of experimenting with techniques based on machine learning and transaction graph analysis and their combinations. We contextualize our argument vis-`a-vis the amount and complexity of crypto transaction data and the specifics of AML/CFT anomaly indicators. We do so by considering the need to mitigate the shortcomings of rule-based regimes, explainability aspects, and the urgency to engage in research informed by an interdisciplinary methodology.

To summarize, the main contribution of this work is twofold:

- We show how modeling blockchain transactions as complex networks is conducive to the subsequent application of specific graph-based learning approaches for anomaly detection purposes. In particular, our experiments show how the GCN model generates better results than other machine learning methods. Notably, it seems to outperform state-of-the-art implementations in classifying illicit transactions;

- Our work heeds a compound of technical, operational, and regulatory viewpoints when considering the benefits of machine learning for AML/CFT anomaly detection. This allows us to account for the need for interpretability and explainability, as well as the effectiveness and efficiency of the deployed approaches.3 This methodology displays the value of cross-disciplinary models to improve accuracy, significantly aiding compliance and investigation, reducing false positives and over-reporting.

The remainder is structured as follows. The “Background” section provides a conceptual background on

> 3 Research into the regulatory impacts of the explainability and interpretability of AI applications is vast and detailed; in light of the scope of this work, we perform inevitable simplifications.

1 3

Bitcoin’s pseudonymity and insights into the relationship between AML/CFT and forensics. The “Related work” section explores related work. The “Anomaly detection approaches” section takes a context-specific approach to outline anomaly detection techniques. In the “Experimenting with machine learning” sections and the “Discussion” sections, we present and discuss our study on machine learningbased AML/CFT classification methods. The “Conclusions” section concludes the paper.

### Background


[p. 3]

In this section, we discuss key aspects related to pseudonymity and deanoymization, followed by a discussion on AML/ CFT and blockchain forensics.

Preliminarily, we point out that in this work, the terms DLT and blockchain are used as synonyms. As is known, while the term DLT refers to a generic idea of distributed ledger, regardless of its implementation, a blockchain is a specific form of DLT in which transactions are stored as a sequence of blocks. Even if the term blockchain is more specific, it is more popular and often used in a wider sense. In this work, the way the DLT stores transactions in the ledger does not influence our model. Indeed, our approach considers the graph generated by transactions, i.e., a direct link from a transaction, say _t_ 1, to another _t_ 2, exists if the money earned in _t_ 1 is spent in _t_ 2. Thus, our study focuses on a layer that is higher than the ledger where transactions are stored.

#### Pseudonymity and de‑anonymization


Untraceability of payments was among the goals of the Internet of Money (Filippi & Wright, 2018). However, in concrete terms, the latter is populated by many socio-technical notions of anonymity and transparency (Pocher & Zichichi, 2022). Following a holistic interpretation, cryptocurrencies are generated and exchanged within socio-technical systems that, as such, comprise of interdependent technology and human systems (Baxter & Sommerville, 2011; Desmond et al., 2019). Hence, their characteristics are influenced by social and technical aspects. Since a literature review (Amarasinghe et al., 2019) falls outside the scope of our work, we heed the specific understanding that anonymity in the Internet of Money “means being able to conduct a financial transaction without anyone besides the sender and the receiver being able to identify the parties involved” (Edmunds, 2020). Indeed, it is a common blockchain goal to combine user anonymity and transparency of operations (i.e., ledger transparency), and a public blockchain is structurally designed to enable anonymous peer-to-peer transfers (Quiniou, 2019).

There is wide agreement that Bitcoin is pseudonymous, and not anonymous (Berg, 2019; Biryukov & Tikhomirov,

2019; Li et al., 2019). Pseudonymity refers to the use of pseudonyms as identifiers, and a pseudonym is a subject’s identifier other than the subject’s real name (Pfitzmann & Hansen, 2010). In most blockchain systems, public–private key pairs uniquely identify wallet holders (Wang & De Filippi, 2020). Hence, in a crypto transaction, addresses (i.e., public keys) perform the function of usernames. It follows that senders and recipients are pseudonymous, not anonymous, when their address identifies them. However, this is not sufficient from a regulatory perspective because pseudonyms alone do not ensure accountability. Indeed, when AML/CFT rules require identification, they refer to real-world identities.

In principle, a currency scheme aims to prevent that the transaction history of its units can be retraced. If it is possible to associate a coin with its past exchanges, the currency’s fungibility is threatened, and its nominal value is affected. Because Bitcoin’s features seemed insufficient, new techniques have been embedded into anonymity-enhanced currencies (AECs), also known as “privacy coins”, to bypass regulatory constraints and surveillance. They deploy privacy-enhancing technologies such as zero-knowledge proofs (ZKPs). Concurrently, even if the most common way to buy and exchange cryptocurrencies still relies on centralized exchanges, the Internet of Money is witnessing the emergence of DeFi applications,4 such as stablecoin projects (e.g., DAI), lending platforms (e.g., Aave, Compound), decentralized exchanges (e.g., Uniswap, Pancakeswap) (Amler et al., 2023; Aramonte et al., 2021; Katona, 2021). The total value of DeFi projects reportedly amounted to USD 1 billion in January 2020, USD 27 billion in January 2021, USD 60 billion in April 2021, and USD 40 billion in November 2022 (Chainalysis Team, 2022).

Meanwhile, the private sector and law enforcement professionals have devised strategies to trace transfers in the Internet of Money. The end goal of these intelligence methods is to match users, definitively or statistically, to transactions performed by crypto-addresses—i.e., to connect pseudonyms to real-world identities—leveraging unique identifiers. These techniques were originally labeled “blockchain forensics”, as they were informed by the specificities of blockchains and defined as the use of science and technology for the sake of investigation and fact-establishment in a court of law, primarily dealing with recovering and analyzing the evidence on blockchain ledgers (Phan, 2021). Later, analytic solutions started to be requested by regulated entities. Although they have been mostly tested on the Bitcoin

> 4 DeFi was defined as an “ecosystem of financial services realized through smart contracts deployed on public distributed ledgers” (Amler et al., 2023), where the role of intermediaries is replaced by self-executing computer code (Katona, 2021). Nonetheless, the levels of decentralization of the relevant projects vary and are debated (Barbereau et al., 2023).

1 3

[p. 4]

network, data-exploitation strategies have been deployed on Ethereum (Bartoletti et al., 2020; Chen et al., 2019; Li et al., 2021; Moreno-Sanchez et al., 2016), and on non-blockchain DLTs (Ince et al., 2018; Tennant, 2017). Evidently, both obfuscation and traceability are not only endeavors pursued by actors belonging to the crypto sphere, but also activities that influence the overall anonymous or transparent sociotechnical character of the domain.

Since identifiers (i.e., addresses/public keys) can be leveraged to connect transactions to their history, Bitcoin’s pseudonymity generates an inherent tension between anonymity and accountability (Yin et al., 2019). However, unless they are associated with additional data, identifiers do not reveal personally identifying information (Wang & De Filippi, 2020). Hence, pseudonymity does not imply identifiability, which is subjective: a pseudonymous subject is identifiable only if a specific actor can discover its real-world identity. This is crucial because, in the Internet of Money, there are both (a) actors, such as authorities and cryptoasset service providers, that seek to achieve identification, and (b) strategies employed at various levels to avert it, e.g., advanced cryptography and virtual private networks. This is an example of how technology can both foster new pathways to accountability and disrupt data retrievability. In this context, the transparent nature of (public) blockchains makes them vulnerable to insufficient data privacy, de-anonymization attacks, and surveillance. While de-anonymization is often perceived negatively, it can be applied for investigative purposes and to comply with rules that aim to mitigate specific risks, such as AML/CFT.

#### AML/CFT and blockchain forensics


The first concern of cryptocurrency misuse originated from transactions on the dark web. While a range of technologies aids darknet operations, cryptocurrencies, mainly Bitcoin and Monero, play a crucial role by facilitating payments (Akhgar et al., 2021). While Bitcoin is still the major player, used by 93% of darknet markets, the adoption of Monero is increasing: 67% of platforms supported it in 2021 vis-`a-vis 45% in 2020, and some support it on an exclusive basis (Chainalysis Team, 2022). Nonetheless, the public perception of cryptorelated laundering is likely inflated. Indeed, even if the value of illicit crypto transactions reached an all-time high in 2022, hitting USD 20.6 billion, it accounts only for 0.24% of crypto activity (Chainalysis Team, 2023), and remains small when compared with criminal activities involving fiat currencies (CipherTrace, 2021; Goforth, 2020).5

> 5 It is worth noting that in 2022 the share of crypto activity associated with illicit activity rose for the first time since 2019. However, 43% of the illicit transaction volume is linked to sanctioned entities. Notably, for the most part, to the crypto exchange Garantex (Chainalysis Team, 2023).

Since the risk-based approach informs AML/CFT obligations, regulated entities must tune compliance efforts: stricter measures if risk factors are higher. The end goal is to draw authorities’ attention when suspicions of illicit activities arise by filing a report when the entity knows, suspects, or has reasonable ground to suspect the given funds are the proceeds of a criminal activity or are related to terrorist financing (Directive (EU) 2018/843, 2018; FATF, 2022). Generally, AML/CFT duties apply to crypto-transactions, and cryptoasset service providers are increasingly regulated. In the EU, the 5th AML Directive (EU) 2018/843 (2018) first targeted these activities, and the regime is evolving with the AML Package (European Commission, 2021).

[pp. 4-5]

Even if the ledger transparency featured by public blockchains mitigates the risk of fraudulent behavior, the technology is vulnerable to unpredictable exploitation methods (Shayegan et al., 2022; Xu, 2016). This prompted the development of specific techniques of anomaly detection. In this field, the Internet of Money’s opaque reputation appears paradoxical since it provides a huge amount of opensource intelligence—e.g., it is possible to extract data from a given transaction and retrieve the history of an address, while methods using networks created by transactions (i.e., “transaction flow analysis”) can define patterns to pinpoint suspected addresses (Wu et al., 2021). Different analytic techniques have been refined over time (Yin et al., 2019), and mostly rely on statistical approaches—e.g., the re-use of an account for more transactions or the co-use of more accounts for a single transaction can lead to matching more accounts to the same user (Li et al., 2021).

Starting from 2020, a surge of ransomware attacks highlighted regulatory shortcomings concerning the complex development of the Internet of Money. Indeed, as the latter becomes populated by AECs and other services that increase obfuscation, the risks of fraud increase. More recently, in 2022, hackers stole USD 3.1 billion from DeFi protocols, exploiting their transparency—i.e., typically, DeFi transactions happen on-chain and the smart contract code is publicly viewable. This amount accounts for 82% of all crypto funds stolen by hackers. In the same year, crypto mixers processed USD 7.8 billion, 24% of which originated from illicit addresses (Chainalysis Team, 2023).

To guide regulated entities in the management of their exposures, several authorities publish red flag/risk indicators to guide compliance and supervision. Notably, in the indicators published by the global AML/CFT standard-setter Financial Action Task Force (FATF) there is a section on anonymity risks (FATF, 2020),6 updated in 2021 (FATF, 2021).

> 6 The report targets six types of indicators, relating to (i) transactions, (ii) transaction patterns, (iii) anonymity, (iv) senders/recipients, (v) funding/wealth at source, (vi) geographic risks.

1 3

Although a transaction’s anonymity level is insufficient to suggest the transfer is suspicious, the FATF underlined inherent issues of privacy-enhancing technologies implemented by privacy coins, such as ZKPs (FATF, 2020). At the same time, a range of institutions highlighted the risks caused by unhosted wallets (Chainalysis Team, 2023; Europol, 2020).

[p. 5]

Against this backdrop, forensic methods provide a wide range of information that emerges as pivotal for investigation, compliance, and supervision. Their value is displayed by the debate on the crypto travel rule, pursuant to which regulated entities must identify originators and recipients of cryptotransfers to guarantee traceability. In principle, this is just an expansion of data sharing measures previously applicable only to wire transfers, as required by the FATF Standards and by EU measures part of the AML Package. However, the reactions to the crypto travel rule exemplify the tension between the Internet of Money and an intermediary-based regulatory framework that still has to capture the specifics of peer-to-peer transfers and decentralized platforms. Accordingly, the industry denounces the absence of global standards and technical solutions to underpin effective and affordable compliance.

### Related work


While we do not aim to offer a review of the techniques of cryptocurrency forensics, in this section, we describe a few works that provided an application to the concepts introduced above. In blockchain analytics, various methods aim to link pools of addresses and transactions. They can deploy clustering techniques to group addresses owned by the same user (Ince et al., 2018; Neudecker & Hartenstein, 2017; Wu et al., 2021) and also leverage transaction graphs to explore the features of the network (Al Jawaheri et al., 2020; Fleder et al., 2015; Ober et al., 2013; Weber et al., 2019). Some of these approaches aim to identify idioms of use in the network that can erode anonymity (Meiklejohn et al., 2016), while others screen transactions to/from crypto-wallets to classify transactions as licit or illicit (Weber et al., 2019). In principle, these tools do not directly try to link addresses and transactions to real-world identities. However, if one of them is de-anonymized (in other ways), they allow to deanonymize the whole cluster, as the cluster database allows fast correlation. Likewise, the goal usually is not to identify transaction patterns, but to allow that when an addresses is suspected other addresses of the same cluster can be suspected as well (Wu et al., 2021).

Clustering methodologies are based on heuristic models (Lischke & Fabian, 2016; Reid & Harrigan, 2013), such as: if two/more addresses are inputs to the same transaction, they are controlled by the same user (Meiklejohn et al.,

2016). In wallet-closure analysis the heuristics are applied to establish a unique mapping between addresses and an identity (Al Jawaheri et al., 2020). In behavior-based clustering (Yin et al., 2019), addresses are grouped based on patterns such as transaction values (Amarasinghe et al., 2019). Androulaki et al. (2013) showed this could unveil the profiles of 40% of Bitcoin users despite privacy measures.

[pp. 5-6]

On the application level, analytic techniques can exploit the possibility to correlate transactions with users’ information on social media. Frequently, users post their addresses (e.g., to receive donations) but also reveal personal information (e.g _._ , contact information, age, location) (Al Jawaheri et al., 2020). In this respect, transaction fingerprinting methods can make use of off-network data (Reid & Harrigan, 2013), which is also leveraged by web-scraping and Open Source Intelligence tools. Fleder et al. (2015) annotated the transaction graph by linking user pseudonyms to online identities collected from social media and developed a graphanalysis framework to summarize and cluster users’ activity to link identities and transactions.

Specific methods target mixing services (Wu et al., 2020), i.e., the ones that shuffle coins by sending them to different addresses to obfuscate the flow. Although third-party services act as centralization points, thus aiding traceability, new disintermediated methods such as CoinJoin (Al Jawaheri et al., 2020) deploy more sophisticated shuffling approaches. In this context, an important role is played by peer-to-peer cross-chain transfers, and a relatively new subset of analytic efforts aims to trace cross-currency transfers through exchanges such as ShapeShift (Al Jawaheri et al., 2020). Harrigan and Fretter (2016) clustered the addresses of the whole Bitcoin blockchain to show that the methodology remains effective despite mixed transactions.

Another line of forensic research, further discussed in the “Anomaly detection approaches” section, is based on machine learning. Yin et al. (2019) presented a supervised learning-based approach to de-anonymize the Bitcoin blockchain to predict the type of entities yet not identified. They built classifiers concerning 12 categories and concluded that it is possible to predict the type of an entity. To do so, they collaborated with the analytic company Chainalysis that provided the data and had previously clustered, identified, and categorized a considerable number of addresses manually or through clustering techniques. They show two examples, one where they predict a set of 22 clusters suspected to be related to criminal activities, and another where they classify 153,293 clusters to provide an estimation of Bitcoin activity. Furthermore, they concluded it is possible to predict if a cluster belongs to predefined categories such as exchange, gambling, merchant services, mining pool, mixing, ransomware, and scam.

Machine learning solutions benefit from constructing multiple graph types from blockchain data, e.g., a blockchain

1 3

Table 1 Summary of the features and comparison of related works with our work


---

[source overview](overview.md) | [next part](text-002.md)

[^original]: Nadia Pocher, Mirko Zichichi, Fabio Merizzi, Muhammad Zohaib Shafiq, Stefano Ferretti, "Detecting anomalous cryptocurrency transactions: An AML/CFT application of machine learning-based forensics" (2023-07-26). https://link.springer.com/article/10.1007/s12525-023-00654-3
