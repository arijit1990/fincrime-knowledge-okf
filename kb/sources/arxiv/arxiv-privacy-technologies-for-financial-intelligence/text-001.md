---
type: Source Text
title: Privacy Technologies for Financial Intelligence - part 1 of 4 (pp. 1-16)
description: 'Verbatim extracted text, pp. 1-16: Privacy Technologies for Financial Intelligence; Privacy Technologies for Financial Intelligence > Abstract; Privacy Technologies for Financial Intelligence > 1. Introduction; and 8 more sections'
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
  resource: https://arxiv.org/abs/2408.09935
  title: Privacy Technologies for Financial Intelligence
  author: org:arxiv
  last_modified: '2024-08-19T00:00:00Z'
---

# Privacy Technologies for Financial Intelligence

[source overview](overview.md) | [next part](text-002.md)

> Verbatim text extracted from the original (arXiv, 2024-08-19), part 1 of 4, pp. 1-16. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **academic finding**.[^original]

## Privacy Technologies for Financial Intelligence


[p. 1]

Yang Lia,_∗_ , Thilina Ranbadugeb , Kee Siong Ngc

> _aSchool of Information Technology, Deakin University, VIC, Australia_

> _bData61, CSIRO, ACT, Australia_

> _cSchool of Computing, Australian National University, ACT, Australia_

Financial crimes like money laundering and terrorism financing can have significant impacts on society, including loss of trust in the integrity of the financial system, misuse and mismanagement of public funds, increase in societal problems like drug trafficking and illicit gambling, and loss of innocent lives due to terrorism activities. Effective detection of complex financial crimes remains a formidable challenge for regulators and financial institutions because the critical data needed to establish patterns and criminality are often dispersed across multiple organisations and cannot be linked due to privacy constraints around large-scale data matching. Recent advances in privacy and confidential computing technologies, which enable private and secure data analysis across organisations, offer a promising opportunity for regulators and the financial industry to come together to enhance their collaborative risk detection while maintaining privacy standards. This paper, through a survey of the financial intelligence ecosystem, seeks to identify opportunities for the utilisation of privacy technologies to improve the stateof-the-art in financial-crime detection.

### Abstract


[pp. 1-2]

_Keywords:_ Financial intelligence, Anti-money laundering, Privacy technology

> _∗_ Corresponding author: Yang Li

> _Email addresses:_ `kelvin.li@deakin.edu.au` (Yang Li),

`thilina.ranbaduge@data61.csiro.au` (Thilina Ranbaduge), `keesiong.ng@anu.edu.au` (Kee Siong Ng)

A robust and trustworthy banking and financial system is essential for the stability and proper functioning of any mature economy. However, in recent years, the reputation and integrity of several major financial institutions have been seriously undermined as organised criminal networks have exploited loopholes and systemic vulnerabilities to launder vast sums of money, some of which have even been linked to terrorist financing [1, 2]. Beyond the reputational harm inflicted on financial institutions, sophisticated financial crimes like money laundering and terrorism financing have profound societal consequences, including:

### 1. Introduction


[pp. 2-3]

- mismanagement and

misuse of public funds;

- financial losses for institutions due to increased compliance costs and regulatory penalties;

- escalation of societal issues such as drug trafficking, human smuggling, and illegal gambling, which carry significant economic burdens;

- the tragic loss of innocent lives in the case of terrorist activities.

Globally important cases like Binance’s $4 billion fine1 for failing to maintain an effective anti-money-laundering (AML) program and other violations against the US Bank Secrecy Act, UBS’s $4.2 billion fine by Swiss, US and French regulators for facilitating tax evasion and inadequate AML controls, and Goldman Sachs’s $2.9 billion fine2 for the 1MDB money-laundering and bribery violations, have certainly brought these issues into the public consciousness and discourse. In Australia, the government’s successful court proceedings against the Commonwealth Bank of Australia, Westpac Banking Corporation, and Crown Casinos for serious breaches of the AML/CTF Act, and their ongoing legal actions against the operators of the Star Casinos and online betting sites like Ladbrokes and Neds highlight the continued challenges faced by regulators and financial intelligence agencies in combating financial crimes.3

In response to these challenges, AUSTRAC, Australia’s Financial Intelligence Agency, established the Fintel Alliance4 in 2016 to foster collaboration

> 1Binance’s $4 billion fine

> 2Goldman Sachs’s $2.9 billion fine

> 3Lists of enforcement actions taken

> 4Fintel Alliance

between government agencies, financial institutions, and law enforcement. A number of similar initiatives have also emerged globally, including the UK’s Joint Money Laundering Intelligence Task Force5 and the U.S. Financial Crime Enforcement Network Exchange6 . These partnerships have proven effective in addressing known threats, but they still face formidable challenges in detecting complex financial crimes because the critical data needed to establish patterns and criminality are often dispersed across multiple organisations and cannot be linked due to privacy constraints around large-scale data matching [3]. The problem is further compounded by the growing complexity of emerging value-transfer mechanisms such as cryptocurrencies and real-time payment systems.

Recent innovations in Privacy-Preserving Data Matching and Machine Learning, which enable private and secure data analysis across organisations, offer a promising opportunity for regulators and the financial industry to come together to enhance their collaborative risk detection while maintaining privacy standards. This paper, through a survey of the financial intelligence ecosystem, seeks to identify opportunities for the utilisation of privacy technologies to improve the state-of-the-art in financial-crime detection. Our paper complements the material covered in [4], which explored global case studies of public and private sectors employing privacy technologies to foster collaborative financial intelligence.

### 2. Financial Intelligence


[p. 3]

Financial intelligence is a highly specialised field that is not well understood by many. This section provides an introduction to the financial intelligence ecosystem, including a description of the current state, some existing limitations and opportunities.

Financial Intelligence Units (FIUs) around the world are governed by anti-money laundering and counter-terrorism financing (AML/CTF) regimes that are quite similar in nature [5, 6]. Reporting Entities (REs) are companies that provide designated financial services that are regulated under AML/CTF laws and typically include banks, money remitters, digital currency

> 5UK’s Joint Money Laundering Intelligence Task Force

### _2.1. The Financial Intelligence Ecosystem_


[pp. 3-5]

> 6U.S. Financial Crime Enforcement Network Exchange

Figure 1: The figure shows a simplified schematic view of a financial intelligence ecosystem.

exchanges, casinos, and increasingly law firms and real-estate companies. (In a country the size of Australia, there are about 10,000 REs in the financial system.) These REs are required by law to maintain know-your-customer (KYC) and anti-money laundering programs to make sure they can verify their customers’ identities and prevent their designated services from being used for illicit purposes. Certain types of customer transaction data, including threshold transaction reports (TTRs) for cash transactions exceeding $10k and all international fund transfer instructions (IFTIs) regardless of amount, are automatically sent to the relevant FIUs on a regular basis. In addition, REs can also submit suspicious matter reports (SMRs) or suspicious activity reports (SARs) to FIUs if they detect suspicious customer activities through their internal controls. Adding to all these data from REs, FIUs may also get reports about specific individuals or entities of interest from lawenforcement agencies and partner FIUs in other countries. Using all these collected data, analysts in FIUs produce intelligence products that either report on specific threats that can be actioned by law enforcement agents, or describe macro threats and mitigation strategies that financial institutions should adopt in their internal controls. Figure 1 shows the information flow from reporting entities to FIUs and, from there, to law-enforcement agencies and the limited feedback loops in the system.

As we can see, there are risk-monitoring and risk-reduction mechanisms built into many different parts of the financial intelligence ecosystem, both within reporting entities in a distributed way and more centrally within the FIU. Many of these organisations also have large-scale automated transactionmonitoring systems that are augmented by manual analyst investigations and formal governance oversight. The parts of Figure 1 coloured in brown represent areas of the financial intelligence ecosystem where artificial intelligence and machine learning can have a significant impact. This is primarily because the sheer quantity of data that must be processed in these locations is immense, and the connections and relationships that need to be distilled and understood, including causal and deliberately hidden linkages, are often complex and intricate.

[pp. 5-6]

Broadly speaking, all data received by an FIU are typically first processed through an entity-resolution step to identify and consolidate records that are highly probable to relate to the same underlying entity [7]. The aim is to produce a dataset like that shown in Figure 2, where each row represents an entity (either persons, corporations, or clusters of related individuals/companies) and the columns illustrate their activities within the financial ecosystem as observed through the lens of the financial institutions whose services they engage with. A small set of such entities would also have explicit risk indicators flagged against them based on, for example, suspicious matter reports, sanctions list and other criminal intelligence data. Given a dataset like Figure 2, an FIU equipped with appropriate technical expertise and advanced data-analytics platforms can employ profiling and statistical machine learning methodologies, both supervised and unsupervised, at varying levels of granularity from individual transactions to single entities and networks of entities, to try to uncover potential risks in the financial system and take appropriate action. Examples of such work include [8, 9, 10].

A crucial aspect to understand about financial intelligence is that financial crimes cannot be definitively identified solely from financial transaction data. Here, at a high level, are the types of anomalies we can infer from financial transaction data [5, 11]:

1. the origin of funds cannot be explained or is obscure;

2. there are rapid transfers of money through various channels, potentially indicating an attempt to obscure the money trail;

3. the financial transaction patterns are inconsistent with a customer’s anticipated personal or business profile.

Figure 2: The entity-resolved data and risk indicators available to a typical financial intelligence agency.

It is important to note that these activities, in isolation, are not inherently illegal. Criminality can only be established and addressed when these activities are linked to a predicate crime, such as tax evasion, welfare-payment fraud, drug trafficking, or similar crimes. To ensure the entire system functions effectively, law enforcement presence is essential throughout the financial intelligence ecosystem to provide leads and supply appropriate risk contexts. Specifically, pure discovery work within financial transaction data presents considerable challenges, but commercial databases of entities of interest, such as LSEG World-Check, and external datasets like company registration information can prove valuable in adding context to financial data.

[pp. 6-8]

That is the current state. The overall system is not perfect by any means. Nevertheless the regime is reasonably effective in deterring, detecting, and disrupting financial crimes, as demonstrated by the many successful prosecutions listed in Section 1. The main limitation of the current state is in the links that are there in the physical financial system but remain missing in the financial intelligence ecosystem. To begin with, a lot of financial transaction data, including domestic interbank transfers and crypto currency transactions, are not reported by default to an FIU and that is a major blind spot for analysts. Compounding the issue, the many thousands of reporting entities in a mature economy like Australia are heavily handicapped in their ability to share intelligence and data with each other because of legal

impediments and risks around accidental tip-offs. One can also argue that there is simply not enough feedback loops built into the system, including that between reporting entities and an FIU, and that between an FIU and its partner law-enforcement agencies and foreign FIUs.

In summary, the key limitations in the current state of financial intelligence can be traced to the following issues:

- Sophisticated and complex financial crimes typically involve transactions that span multiple financial institutions in multiple geographies, going through multiple payment channels, some of which remain unregulated.

- Criminality cannot be established through analysis of financial transaction data alone; actual links to predicate crimes are necessary.

- FIUs, reporting entities, and law-enforcement agencies are all mostly working within data silos and it is hard for any one organisation to get a complete view of financial and criminal activities across the entire system.

- _2.2. A Way Forward using Privacy Technologies_

To overcome the key limitations of the current state of financial intelligence, Figure 3 outlines a potential solution that leverages distributed confidential computing technologies. The assumption is that FIUs, reporting entities and law-enforcement agencies are willing to collaborate in good faith without requiring sweeping changes to AML/CTF legislation globally.

In the proposed approach, rather than traditional entity resolution, data from all participating organisations are first matched using privacy-preserving record linkage (PPRL) algorithms [12]. These algorithms identify records across different databases that correspond to the same entity in a manner that safeguards privacy, ensuring no plaintext values are disclosed to any party involved.

Once the records are matched, the data are encrypted using either homomorphic encryption (Section 3.2) or secure multiparty computation schemes (Section 3.1). These encryption methods allow mathematical operations to be performed directly on encrypted data, resulting in a table similar to those discussed earlier but with two key differences:

- All values in the table are encrypted, and the columns are distributed across multiple databases managed by different agencies.

Figure 3: Privacy-enhanced version of Figure 2. LEAs = Law Enforcement Agencies; PAs = Partner Agencies; EOI = Entities of Interest

[pp. 8-9]

- AI and machine learning algorithms for detecting risks and suspicious entities can still be run on the encrypted data using homomorphic encryption or secure multiparty computation. When a small set of entities of interest is identified, their data can be decrypted without compromising the privacy of the broader population.

Distributing encrypted data across multiple organisations and databases does introduce some complexity to AML/CTF risk-modelling workflows, but the approach offers a pathway for collaboration while addressing privacy concerns and ensuring compliance with existing legal frameworks.

To help us navigate the opportunities offered by privacy technologies for financial intelligence, it is essential to understand that there are three fundamental computational problems to address in AML/CTF risk modelling, in increasing order of technical complexity:

1. Private Intersection Identification: How can two FIUs, each maintaining its own list of suspicious entities, securely exchange overlapping data points without exposing their full datasets with each other? How might this process scale across multiple FIUs?

2. Cross-Institutional Pattern Detection: Given a criminal typology defined as a graph pattern (where nodes represent entities and edges denote relationships), how can we identify all entities matching this

pattern when the underlying graph pattern spans multiple financial institutions?

3. Federated Model Learning: How can supervised or unsupervised machine learning models be trained on behavioural and transactional data distributed across multiple financial institutions, where no single entity holds complete datasets?

These three computational problems are distilled from the authors’ experience working both directly and indirectly with Australia’s financial intelligence and banking communities over an extended period of time, and backed up by literature review.

In the rest of this paper, we will first survey some key privacy technologies in § 3 before providing in § 4 illustrative examples and detailed pointers to how such privacy technologies can be used to address the three computational problems listed above. Solutions to these three computational problems can be, and are often, used as building blocks to develop more complete systems to address challenging real-world financial intelligence problems, some of which we survey in § 5.

### 3. Privacy Technologies


[pp. 9-10]

In the above, we highlighted a central challenge in multiparty financial intelligence, how can multiple parties work together effectively when none of them can be assumed to be fully trusted? We also noted that privacy technologies can serve as a technological means to enable such collaboration, allowing multiple parties to jointly combat financial crime under specific cooperation models. We refer to this form of multiparty financial intelligence conducted under explicit data privacy and security constraints as privacypreserving financial intelligence.

Privacy-preserving financial intelligence should be understood as a system level concept rather than a single method. Different privacy technologies play different roles within this system, but they share a common objective of enabling analysis and modelling, while maintaining data security and privacy guarantees.

This section begins with secure multiparty computation (MPC), as it is one of the most widely adopted mechanisms for protecting data in collaborative settings. MPC enables multiple parties to jointly perform computations without revealing their private inputs. Building on this foundation, we intro-

duce homomorphic encryption (HE), which supports MPC by enabling computation over encrypted data and is therefore often used as a cryptographic primitive in MPC designs. We then move beyond MPC centric settings and discuss several problem scenarios where MPC is not the primary solution. For these cases, we introduce privacy technologies that are widely used in practice, namely hashing, federated learning (FL), and differential privacy (DP), each addressing privacy risks from a different perspective.

### _3.1. Secure Multiparty Computation_


[pp. 10-11]

The goal of secure multiparty computation (MPC) is to enable multiple parties to jointly evaluate a pre-agreed function without revealing their individual private inputs. At its core, MPC removes the need to trust the computation process itself. Under an MPC protocol, each participant learns only the final output (or an authorised share of it) and cannot infer additional information about other parties’ inputs beyond what is inherently revealed by that output. In doing so, MPC shifts cross-institutional collaboration away from data centralisation or reliance on a trusted third party, and instead enforces privacy and correctness directly at the protocol level through cryptographic mechanisms.

More generally, MPC can be viewed as a general-purpose framework for privacy-preserving computation. Whenever a collaborative task can be formalised as a function, MPC provides a mechanism for jointly evaluating that function without requiring participants to share their raw data.

Because MPC is a strict security framework, its practical deployment depends on clearly defined security guarantees. In particular, privacy ensures that an adversary learns nothing about an honest party’s input beyond what follows from the output itself. Correctness guarantees that the protocol produces the correct result, even in the presence of adversarial behaviour. Stronger notions may also be required in certain settings: guaranteed output (or robustness) ensures that adversaries cannot prevent honest parties from obtaining the result by aborting the protocol, while fairness requires that an adversary receives the output if and only if the honest parties do.

In addition to these properties, MPC protocols are analysed under explicit adversarial models. In the semi-honest (honest-but-curious) model, adversaries follow the protocol specification but attempt to extract additional information from the execution. In the malicious model, adversaries may deviate arbitrarily from the protocol, for example by sending malformed messages, aborting prematurely, or manipulating inputs and outputs. The

assumed adversarial model directly influences both the strength of the security guarantees and the complexity of the resulting protocol.

In the context of financial intelligence, these capabilities can be illustrated through a common investigative scenario (discussed further in Section 4.1). Different financial institutions (FIs) maintain their own customer lists, while a financial intelligence unit (FIU) may need to determine which entities on its watchlist have relationships with which banks. Here, the FIU and the banks act as participating parties, their private inputs are their respective customer lists, and the agreed computation is the intersection between the FIU’s list and those of the banks. MPC enables this joint analysis to be conducted without exposing any party’s complete customer list.

### _3.2. Homomorphic Encryption_


[pp. 11-12]

Within the MPC framework, privacy protection is not achieved by simply hiding the output, but by ensuring that computation itself can be performed without exposing sensitive inputs. For this reason, MPC protocols typically rely on multiple cryptographic mechanisms rather than a single technique. Homomorphic encryption (HE) is one such foundational capability.

The defining feature of HE is that it allows certain computations to be performed directly on encrypted data, producing results that, once decrypted, are equivalent to those obtained from computations on plaintext. In MPC settings, this property enables parts of a computation to be executed without revealing intermediate values, thereby reducing direct data exposure between participants.

Dec(secret key _,_ Enc(public key _, m_ 1) _◦_ Enc(public key _, m_ 2)) = _m_ 1 _⋄ m_ 2 _,_ (1)

From this perspective, HE is not a replacement for MPC, but rather one of its supporting building blocks. In practice, HE is often combined with other mechanisms, such as secret sharing or oblivious transfer, to securely encapsulate specific computation steps while balancing privacy guarantees, communication overhead, and system complexity. At the same time, HE can also be used independently of a full MPC framework. In scenarios where the computation structure is relatively simple, for example, when one party holds the data and another performs the computation, HE allows encrypted data to be processed externally without revealing the underlying inputs. This enables analysis or evaluation without requiring raw data sharing.

HE schemes are commonly classified according to the types of operations they support and the number of operations that can be performed before decryption becomes unreliable. The most general form is Fully Homomorphic Encryption (FHE), which supports an unbounded number of operations on encrypted data. The practical feasibility of FHE was established following Gentry’s breakthrough construction [13], which sparked significant research interest, particularly in lattice-based cryptography, a field now widely regarded as central to quantum-resistant encryption [14].

It is also important to note that HE schemes are inherently probabilistic, which means encrypting the same plaintext multiple times produces different ciphertexts. This property ensures semantic security, which prevents adversaries from inferring information about the plaintext from ciphertext patterns.

In financial intelligence applications, such standalone use of HE may arise in outsourced computation of sensitive transaction features, risk metrics, or aggregate statistics. Financial institutions can retain full control over their data while leveraging external compute resources or cross-organisational collaboration, without disclosing plaintext information.

Despite its strong privacy guarantees, the applicability of HE remains constrained by performance considerations, supported computation types, and overall system complexity. As such, HE is best understood either as a specialised independent capability within the privacy-preserving toolkit, or as a key component within more complex MPC-based solutions.

### _3.3. Hashing Techniques_


[pp. 12-13]

In cross-institutional data collaboration, a fundamental but often overlooked problem is how to preserve matchability between entities or relationships while avoiding direct exposure of sensitive identifiers. At this level, hashing provides a lightweight yet practical solution. Hashing works by applying a one-way mapping to original identifiers such as customer IDs, transforming them into fixed length representations. For example,

Hash: Hello _→_ 2CF24DBA5FB0A30E26E83B2AC5B9E

While the original identifiers cannot be recovered, consistent hashing allows entities or relationships across different datasets to be matched. In other words, hashing does not hide whether two records refer to the same entity, it hides who that entity is.

From a functional standpoint, hashing is not a joint computation mechanism and does not attempt to provide comprehensive protocol level privacy guarantees. Its primary value lies in reducing direct exposure of sensitive identifiers during data exchange and comparison, thereby offering a baseline level of privacy protection. This makes hashing widely used in practice for identity alignment, relationship linking, and preliminary data filtering.

In financial intelligence contexts, hashing is commonly applied as a preprocessing step for customer or account identifiers. This allows financial institutions and regulators or investigators to assess potential overlaps or business relationships without sharing plaintext identity information. While such approaches do not eliminate all privacy risks, they can significantly reduce unnecessary data exposure when computation goals are well defined and trust boundaries are controlled.

As suggested by Chi et al. [15], properties such as uniform distribution of hash outputs, consistency of mapping, computational efficiency, and appropriate handling of input and output domains are important when selecting a hash function for practical applications. More broadly, the effectiveness of hashing depends on several underlying assumptions, including the size of the input space, the consistency of hashing rules across participants, and resilience against auxiliary information attacks. In higher-risk or more complex multiparty collaboration settings, hashing alone may be insufficient; it is therefore typically combined with stronger privacy-preserving mechanisms rather than deployed as a standalone solution.

### _3.4. Federated Learning_


[pp. 13-15]

In some collaborative settings, privacy risks arise not from a single joint computation, but from long term, iterative model training processes. In such cases, participants seek to collaboratively build and update models over time while keeping their data within local domains, rather than jointly evaluating a fixed function. Federated learning (FL) is designed for precisely this type of collaboration.

The core idea of federated learning is that data remains local to each participant, model training is performed independently on local datasets, and only model updates are shared with a coordinating entity for aggregation into a global model as shown in Figure 4. From a collaboration perspective, FL does not require sharing raw data or encrypting an entire joint computation. Instead, it follows a local computation and global aggregation paradigm.

Aggregationwn Serverlocal model nSendinglocal model global modelupdatesw2local model 2W = w1 + w2+ ..... + wnw1Sendinglocal model 1 global modelupdatesData Owner n.....Data Owner 2Data Owner 1

Figure 4: An example federated learning (FL) architecture with _n_ data owners. In the setting, data owners only exchange the model gradient ( _w_ ) with the aggregation server. In each training iteration, each data owner _i_ trains its own model with their local data and send the corresponding local model updates _wi_ to the aggregation server. After aggregating all the received local model updates, the aggregations server returns the new global model updates ( _W_ ) to each data owner.

This leads to a fundamental structural difference between FL and MPC. While MPC focuses on securely evaluating a predefined function, FL is concerned with the continuous evolution of a model over time. In large scale, long running, and frequently updated training tasks, attempting to replicate FL using MPC would be impractical due to excessive system complexity, communication overhead, and reduced training efficiency.

It should be noted, however, that although FL avoids direct data sharing, privacy risks do not disappear entirely. Model parameters or gradient updates may, under certain conditions, leak statistical properties or even individual level information about local datasets [16, 17, 18]. Consequently, FL is often combined with additional privacy technologies, such as homomorphic encryption or differential privacy, to mitigate information leakage during the training process.

Within financial intelligence, FL is particularly well suited to scenarios where multiple institutions wish to jointly train models for risk detection, anomaly identification, or behavioural analysis without centralising sensitive data. Participants retain control over their data while benefiting from improved model performance through collaboration. In such settings, the key challenge is not how to securely compute a single result, but how to balance model utility and privacy risk over sustained collaboration, a challenge for

which FL offers distinct advantages over MPC.

### _3.5. Differential Privacy_


[pp. 15-16]

Across the privacy technologies discussed so far, the primary focus has been on protecting input data and ensuring trustworthy computation. However, in many real world applications, the results themselves can still leak sensitive information, even when inputs and computation processes are fully protected. Differential privacy (DP) addresses this class of risks directly.

The core principle of DP is to introduce carefully calibrated randomness into statistical outputs or model results, ensuring that the presence or absence of any single individual’s data does not have a distinguishable impact on the output.

Definition 1. _A randomised algorithm A is ϵ-differentially private if for all databases_ D _and_ D_′_ _that differ in at most one record, and for all sets O outputs, we have_

_where Pr_ [ _·_ ] _denotes the probability of an event._

Rather than hiding raw data or computation steps, DP explicitly constrains how much information can be inferred from released results.

This positioning fundamentally distinguishes DP from MPC. Even in a fully trusted joint computation environment, repeated queries or downstream inference based on exact outputs can gradually expose individual level information. DP mitigates this risk by limiting the sensitivity of outputs to individual data points, something that MPC, HE, or FL cannot achieve on their own.

In financial intelligence applications, DP is commonly used when publishing aggregate statistics, analytical reports, or model outputs. For example, when sharing risk distributions, trend analyses, or group level behavioural insights, DP mechanisms can preserve the overall analytical value while substantially reducing the risk of re-identifying individual customers or accounts. In these contexts, the primary privacy concern is not who performed the computation, but what can be inferred once the results are released or reused [19, 20].

It is important to emphasise that differential privacy is not a zero cost solution. Introducing randomness to limit information leakage necessarily involves a trade-off between privacy guarantees and result accuracy. As such, DP is best understood as an output level privacy governance mechanism, complementing rather than replacing input level and computation level privacy technologies.


---

[source overview](overview.md) | [next part](text-002.md)

[^original]: arXiv, "Privacy Technologies for Financial Intelligence" (2024-08-19). https://arxiv.org/abs/2408.09935
