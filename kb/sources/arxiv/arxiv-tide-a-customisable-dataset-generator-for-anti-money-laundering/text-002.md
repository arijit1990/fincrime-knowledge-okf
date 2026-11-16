---
type: Source Text
title: 'Tide: A Customisable Dataset Generator for Anti-Money Laundering Research - part 2 of 5 (pp. 9-19)'
description: Verbatim extracted text, pp. 9-19
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
part: 2
parts_total: 5
content_mode: full_text
generated:
  by: process:fincrime-kb-build
  at: '2026-11-16T16:31:16Z'
verified:
- by: process:kb-validate/verbatim-coverage
  at: '2026-11-16T16:31:16Z'
sources:
- id: original
  resource: https://arxiv.org/abs/2603.01863
  title: 'Tide: A Customisable Dataset Generator for Anti-Money Laundering Research'
  author: org:arxiv
  last_modified: '2026-02-03T00:00:00Z'
---

# Tide: A Customisable Dataset Generator for Anti-Money Laundering Research

[previous part](text-001.md) | [source overview](overview.md) | [next part](text-003.md)

> Verbatim text extracted from the original (arXiv, 2026-02-03), part 2 of 5, pp. 9-19. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **academic finding**.[^original]

[p. 9] [ref: 4.2]

over the graph’s overall size and fraud ratio, the specific parameters of each laundering pattern, and the characteristics

of the legitimate background activity.

Reproducibility. To facilitate benchmark comparisons, the generation process must be deterministic, producing

identical datasets when provided with the same configuration and random seed.

4.2 Graph Data Model

We model the financial network as a directed, heterogeneous graph 𝐺= (𝑉, 𝐸). This structure supports distinct entity

types and directed financial flows.

4.2.1 Entity and Attribute Design. The nodes 𝑣∈𝑉in the graph represent four distinct entity types: individuals,

businesses, accounts, and financial institutions. Each node has a set of common attributes (Table 2) and type-specific

attributes that define its characteristics (Tables 8-11 in the Appendix).

Attribute Description Type

node_id Unique identifier for each node. String node_type The type of the entity. Categorical country_code Country where the entity is based. String is_fraudulent Label indicating whether node is part of a fraud pattern. Boolean risk_score Value in [0, 0.9] expressing the probability of an entity being fraudulent. Float

Table 2. Common attributes for all node types.

To model cash-based activities, two mechanisms were implemented. First, each individual and business has a dedicated

‘cash‘ account for withdrawals. Second, a special global ‘cash‘ node (𝑣cash) acts as a source for cash deposits where the

origin is unknown.

Risk Scoring Framework. To systematically model the likelihood of an entity’s involvement in illicit activity, a risk

scoring function was developed. This risk-scoring function is used to select entities for fraudulent patterns in the

later stage of the generation process. Note that risk scores are excluded from the feature set provided to machine

learning models during training and evaluation, ensuring that detection performance reflects learned patterns rather

than direct access to ground-truth selection criteria. For individuals and businesses, the score is calculated as a weighted

combination of known risk factors:

!

∑︁

risk(𝑣) = min

base risk +

𝑤𝑖· 𝑓𝑖(𝑣), 0.9

(2)

𝑖

In this function, 𝑤𝑖is the weight for risk factor 𝑖, and 𝑓𝑖(𝑣) is an indicator function (1 if the factor is present, 0 otherwise).

The default weights were calibrated based on their reported prevalence in literature [1], with factors like operating a

cash-intensive business or being located in a high-risk jurisdiction assigned higher weights (See Table 12).

Entity Clustering. To support efficient entity selection for pattern injection in a large graph, we define a clustering

function that groups individual and business entities based on their risk profiles:

cluster : 𝑉entities →2C \ {∅} (3)

[p. 10] [ref: 4.2.2]

where 𝑉entities ⊆𝑉contains only individuals and businesses (excluding accounts and institutions), and C represents

a predefined set of clusters which consists of both single clusters (single risk factors such as geographic, demographic,

occupational, and behavioural factors) and composite clusters that combine specific risk factors. Entities are by default

assigned to the ‘legit’ cluster (and removed if they are part of a fraud pattern), so each entity is assigned to at least one

cluster, and can belong to multiple clusters simultaneously. This clustering lets Tide select entities that match specific

pattern requirements.

4.2.2 Edge Representation. Edges 𝑒∈𝐸represent the interactions between nodes. They are defined as a tuple 𝑒=

(𝑖, 𝑗,𝑟,𝑎,𝑡,𝛿,𝛾, 𝜆), where each component captures a key piece of information about the interaction (see Table 3). This

detailed structure allows for modelling both static ownership relationships and time-sensitive transaction events.

Component Description Type

𝑖, 𝑗 Source and target node IDs. String 𝑟 Relationship type: transaction or ownership. Categorical 𝑎 Transaction amount. Float 𝑡 Timestamp of the interaction. Timestamp 𝛿 Time since the source node’s last transaction. Timedelta 𝛾 Transaction category. Categorical 𝜆 Fraud flag. Boolean

Table 3. Attributes of an edge tuple 𝑒= (𝑖, 𝑗,𝑟,𝑎,𝑡,𝛿,𝛾, 𝜆).

4.3 Generator Architecture and Workflow

Tide uses a generation algorithm to construct the synthetic financial graph. The core logic of this pattern injection is

illustrated in Figure 2 and described below. Note that the fraud pattern depicted in the figure is a simplified representation

intended to visualise the concept.

(1) Entity Creation and Clustering (Figure 2a): The process begins by populating the graph with financial

entities, which are individuals, businesses, accounts, and financial institutions. Each entity is created with a set

of attributes as defined in Section 4.2. After this, these entities are grouped into various clusters based on their

characteristics (Section 4.2.1). These clusters are used for quick targeted selection of nodes in the following

pattern injection phases, so they can operate in near-constant time relative to the total graph size. Low-risk

entities form the general population of the graph.

(2) Entity Selection for Patterns (Figure 2b): For each specific money laundering pattern that needs to be

injected into the graph, the generator first identifies the roles required by the pattern’s structure. For example,

the repeated overseas transfer needs a high risk source (because of their occupation, business, country, or age),

with multiple destination nodes in high risk jurisdictions overseas.

[pp. 10-12] [ref: 4.4]

(3) Transaction Sequence Generation (Figure 2c): Once the entities for a pattern instance are selected, the

temporal component of that pattern generates a sequence of financial transactions between them. This involves

defining the timing, frequency, amounts, and types of these transactions to reflect the specific laundering

pattern being modelled. For instance, funds might flow from the primary actor to an intermediary, and then

from the intermediary to an entity in a high-risk jurisdiction, as depicted by the red arrows.

(4) Pattern Aggregation (Figure 2d): The process of selecting entities and generating transaction sequences

(steps 2 and 3) is repeated for every money laundering pattern instance that the user configures to be injected.

Each pattern generates its own set of fraudulent transactions. These individual pattern sub-graphs are then

merged into the main graph. Alongside these illicit activities, legitimate background transactions (represented

by black dotted arrows) are also simulated. The final output is a single graph containing both legitimate and

fraudulent activities.

(a) Step 1: Different entities are created, and then clustered based on attributes.

(b) Step 2: Entities are selected for a pattern; the source actor is highlighted in red.

(c) Step 3: Transactions sequences are created between selected entities.

(d) Step 4: Multiple patterns and background activity are merged into a single graph.

Fig. 2. The four main steps of the Tide graph generation process: (a) Entity creation and clustering, (b) Entity selection, (c) Transaction sequence generation, and (d) Pattern aggregation.

4.4 Fraudulent Pattern Injection

This section details the money laundering typologies that Tide injects during steps 2 and 3 of the generation workflow

(Section 4.3). Each pattern defines a structural component, specifying which entities to select from the pre-computed

clusters and how they relate, as well as a temporal component governing transaction timing and amounts. Table 13

summarises the five implemented typologies.

Temporal profiles. We distinguish two temporal profiles for transaction sequences {𝑒1, ...,𝑒𝑛} with timestamps

{𝑡1, ...,𝑡𝑛}: (1) burst patterns, where all transactions occur within a bounded window (max(𝑡𝑖−𝑡𝑗) ≤Δburst), and (2)

periodic patterns, where transactions recur at regular intervals (|𝑡𝑖+1 −𝑡𝑖−Δperiod| ≤𝜖).

4.4.1 Layering. Four of the five patterns optionally insert intermediate layering hops between the source and destination

of each fraudulent transfer. When enabled, each transfer is routed through ℎrandomly selected intermediary accounts,

[pp. 12-13] [ref: 4.4.2]

where ℎ∈[ℎmin,ℎmax] is drawn uniformly (by default ℎ∈[2, 5]). At each hop, the amount decays by a factor

𝛿∼U(0.95, 0.99) to simulate fees or conversion losses, and a delay of 1–48 hours is added between consecutive hops.

Intermediary accounts are selected either uniformly at random from the existing account population, or from a clustered

pool of high-risk entities to increase edge-label homophily. The only pattern that does not use this mechanism is

the Synchronised Transactions pattern, whose structure involves direct deposits to a common recipient. All layering

parameters are configurable; disabling layering reduces each pattern to its base two-party topology.

4.4.2 Repeated overseas transfers. This pattern models the transfer pattern, where individuals frequently send large

transfers to overseas entities.

Fig. 3. Visualisation of the overseas transfer pattern. Individual_1 owns Account_1.

Structural component. Tide identifies a source individual from a high-risk cluster. The entity should have at least one

domestic bank account. It then selects multiple international destination accounts. High-risk jurisdictions have the

highest priority in the destination selection, but other overseas accounts can be selected if no entities are available in

the cluster.

Temporal component. The implementation of this pattern consists of two different behavioural profiles observed in

the literature. The first is a burst pattern, where transactions occur within a small timeframe or with small intervals

between transactions, defined by a parameterised distribution to avoid mechanical-like timing. The second is a periodic

pattern, where transactions occur at regular intervals such as weekly or monthly over a longer time period, as described

in Section 2.2.1. The periodic variant mimics legitimate recurring payments but differs in destination, amount, or lack

of clear economic purpose compared to the entity’s profile.

The source entity first gets cash deposits under the user-defined reporting threshold, which are then, shortly thereafter,

sent to the overseas entities.

4.4.3 Rapid fund movement. In this pattern, accounts receive high volumes of incoming transfers followed by frequent

cash withdrawals.

Fig. 4. Visualisation of the rapid fund movement pattern. Individual_1 owns Account_1 and Account_2.

Structural component. Tide selects a high-risk individual that owns multiple bank accounts. This is the individual

that receives the funds and withdraws money. It also selects multiple overseas entities, again prioritised from high-risk

jurisdictions.

Temporal component. The implementation of this pattern follows a two-phase structure:

(1) Inflow: Multiple incoming wire transfers from the selected external sources, all in the user-defined timeframe,

with a default of 24 hours.

(2) Dispersal: Following a small delay period, we generate cash withdrawal transactions. The individuals’ cash

[pp. 13-14] [ref: 4.4.4]

holdings are modelled as a separate account (next to, for example, current and savings accounts). These

withdrawals also happen with a varying interval in a specified time period. To account for hypothetical

operational cost, the total outflow amount is typically 85-95% of the total inflow amount.

4.4.4 Front business activity. This pattern implements the use of front business behaviour described in Section 2.2.2,

where businesses deposit large amounts of cash, across accounts at different institutions, and immediately transfer the

funds to overseas business accounts.

Fig. 5. Visualisation of the front business pattern. Business_1 owns Account_1 and Account_2.

Structural component. Tide identifies business entities from the high risk cluster that control multiple accounts across

different banks. Additionally, it selects overseas business accounts where each account is in a different country and

owned by another business entity.

Temporal component. The implementation of this pattern consists of two phases:

(1) Deposit phase: Cash deposits occur across multiple accounts in a short timeframe. This cash comes from the

global cash account in our financial system.

(2) Transfer phase: Following deposits with delays of 0.5 to 6 hours, transfers go to the overseas business accounts.

The transfer amounts are 80-100% of the total deposited amount, so transfers appear more as legitimate

international business transfers.

4.4.5 Synchronised transactions. This pattern implements the synchronised transaction behaviour described in the

literature, where multiple seemingly unrelated entities perform coordinated transactions that suggest collusion.

Structural component. Tide selects multiple coordinating entities with diverse characteristics to appear unrelated. For

example, different age group, occupation, or different country. We also select a recipient entity, typically from high-risk

jurisdiction clusters, that will receive the coordinated transfers.

Temporal component. The implementation of this pattern generates the coordinated activity described in the literature

within tight time windows:

(1) Synchronised deposits: Each coordinating entity receives cash deposits at nearly the same time. These deposits

are distributed within an n-hour synchronisation window.

(2) Aggregation: After delays of 1-6 hours, coordinating entities transfer 85-95% of deposited amounts to the

recipient account. As noted in the literature, these transactions often involve amounts structured below reporting

thresholds and similar transaction values.

4.4.6 U-Turn Transactions. This pattern implements a round-trip transaction structure, where funds are transferred

out through intermediaries before returning to accounts linked to the original sender.

Structural component. Tide selects a high-risk source entity with at least two accounts, intermediaries, and a

destination account in a high-risk jurisdiction. Nodes are clustered as intermediaries based on some demographic

and operational characteristics; our algorithm targets young adults, so people between 18–24 years old, who are

often recruited as money mules due to financial vulnerability, and elderly people who are over 65 years old, who

[pp. 14-15] [ref: 4.5]

may be exploited. Next to age, we look at individuals with occupations that provide access to financial systems or

are traditionally associated with high money laundering risks. For this, we look at the occupations that partake in

cases of [1], and extrapolate on that to other high paid occupations, or other occupations in the financial industry.

Geographic location also influences selection, with preference given to individuals in high-risk jurisdictions where

regulatory oversight may be weaker. For front business entities, the approach focuses on small companies with ten or

fewer employees operating in a cash intensive business category.

Temporal component. The implementation of this pattern constructs transaction paths from the source, to at least

one account in a high-risk jurisdiction, through the set of intermediaries. Each transaction occurs with one to five day

delays, with amounts decreasing by 1-3% fees at each step.

Fig. 6. Visualisation of the U-turn transaction pattern.

4.5 Simulating Legitimate Background Activity

The simulation of background financial activity represents the normal, legitimate transactions that occur in a financial

network. These transactions form the baseline behaviour against which suspicious patterns can be detected. We split

different types of background activity into various patterns, where, like the fraudulent patterns, each pattern is composed

of a structural and temporal aspect. We implement four types of base background activity: random everyday payments

in a lower range, higher range payments, salary payments, and fraudster background activity. We also implement

specific background patterns to counterbalance the very specific fraud patterns.

4.5.1 Transaction Amount Calibration. To prevent amount-based data leakage, all transaction amounts are drawn

from log-normal distributions calibrated to the 2022 Federal Reserve Payments Study (FRPS, 8th Triennial) [10], the

Bureau of Labor Statistics Usual Weekly Earnings report [35], and ADP payroll microdata [4], following a similar

methodology as Altman et al. [6]. Many stochastic models in economics and finance are described by distributions with

a log-normal body and Pareto tail [8]; we approximate this using clipping to type-specific [min, max] bounds. For each

transaction type we set 𝜇= ln 𝑀where 𝑀is the target median, and select 𝜎large enough to produce realistic heavy

tails (𝜎≥0.6), accepting that theoretical means may deviate from source averages. Table 4 lists the base log-normal

parameters alongside the generated statistics. Structuring overlays and pattern-specific behaviour shift the aggregate

means above the theoretical values. Three types are calibrated to FRPS averages (Payment, Transfer, Withdrawal);

Deposit (marked †) is a modelling assumption, as we were not able to find a public source that reports typical deposit

amounts directly.

Structuring deposits use a uniform distribution over $7,000–9,999, or its equivalent in other currencies, to model

[pp. 15-16] [ref: 4.5.2]

deliberate sub-threshold clustering; 3–5% of legitimate background transactions also fall in this range to prevent

structuring from becoming a pure fraud signal.

4.5.2 Transaction Frequency Calibration. Table 17 reports noncash payment volumes from the 2022 Federal Reserve

Payments Study [10]. Card and ACH debit payments dominate U.S. noncash transactions (∼91%), while ACH credit

Table 4. Log-normal amount parameters and generated statistics per transaction type in LI dataset.

Type 𝜇 𝜎 Source Avg Gen. Median Gen. Mean

Payment 3.8 1.2 $60 (FRPS) $46 $218 Transfer 5.5 2.0 $1,634 (FRPS) $221 $1,863 Withdrawal 4.8 0.9 $198 (FRPS) $130 $546 Deposit† 5.3 1.5 — $220 $977

transfers and ATM withdrawals account for ∼7% and ∼2%, respectively. However, our included fraud patterns primarily

exploit transfers, deposits, and cash withdrawals rather than card purchases. We therefore over-represent these

transaction types to ensure the generated data contains sufficient instances of the payment flows targeted by our

money-laundering patterns (Table 5). Note that FRPS tracks outgoing payments; deposits (incoming flows) are not

reported. Salary payments are modelled as incoming transfers from employer accounts and subsumed under the Transfer

category.

Table 5. Transaction type frequencies: FRPS reference vs. generated data in LI dataset.

Type FRPS Share† Generated Share

Payment ∼91% 68% Transfer ∼7% 12% Withdrawal ∼2% 8% Deposit — 11%

† FRPS tracks outgoing payments only; deposits (incoming flows) are not measured. Our generated distribution includes deposits, which reduces the relative share of other types accordingly.

4.5.3 Random everyday transactions. This transaction category captures the baseline of legitimate background activity

within the network. It encompasses low-value payments intended to simulate routine consumer purchases and recurring

expenses, constrained within value ranges defined by the configuration parameters. The frequency of these interactions

is governed by a user-specified rate, denoting the average daily transaction volume per account.

Like the fraud patterns, this pattern also consists of a structural component that selects legitimate accounts from

pre-computed clusters, and a temporal component that generates transaction sequences over the specified time period.

The structural component selects legit entities from our pre-computed cluster (As explained in Section 4.2.1). The

temporal component generates transactions using a memory-efficient streaming approach. The total number of expected

transactions is calculated as:

Total random transactions = ⌊𝑟× 𝑑× |𝐴|⌋ (4)

[pp. 16-17] [ref: 4.5.4]

Where 𝑟is the transaction rate per account per day, 𝑑is the total number of days in the simulation period, and

where |𝐴| is the number of active accounts, including both legitimate and a subset of fraudulent accounts to prevent

topological isolation. The count may be further capped by a configurable transaction budget.

Transaction types are selected probabilistically with configurable weights for wire transfers to other individuals,

payments to businesses, deposits, and withdrawals. Transaction amounts are sampled from the log-normal distributions

in Table 4, with type-specific parameters for payments, transfers, deposits, and withdrawals.

4.5.4 High-value transactions. We define ‘high-value transactions’ as legitimate transfers of significant magnitude that

occur considerably less frequently than standard background activity.. These payments are meant to model transactions

like luxury purchases, house purchases, and business transactions.

The pattern generates transactions between individuals and businesses. It identifies entities from two main sources:

individuals with high-paid occupations and medium to large businesses (which we define as having more than 10

employees).

The total number of transactions to generate is calculated using the formula:

Total high-value transactions = ⌊𝑟𝑚𝑜𝑛𝑡ℎ𝑙𝑦× 𝑀𝑡𝑜𝑡𝑎𝑙× |𝐴ℎ𝑖𝑔ℎ|⌋ (5)

Where 𝑟𝑚𝑜𝑛𝑡ℎ𝑙𝑦is the monthly transaction rate per high-value account (configured by the user), 𝑀𝑡𝑜𝑡𝑎𝑙is the total

number of months in the simulation period, and |𝐴ℎ𝑖𝑔ℎ| is the number of identified high-value accounts.

Transaction amounts are sampled from the high-value log-normal distribution (Table 4) and rounded to the nearest

$100. All transactions are scheduled during business hours (9 AM to 5 PM) with random dates distributed throughout

the simulation period.

4.5.5 Salary payments. The salary payments pattern models recurring compensation from businesses to individuals.

The system designates legitimate business entities as payers and specific individuals as recipients. Each business is

linked to 1–3 individual recipients; this simulates employer-employee relationships while preventing unrealistic density

in the transaction graph.

The temporal component generates schedules based on standard payroll intervals: bi-weekly, monthly, or user-defined

custom periods. For monthly cycles, payments align with specific calendar days (defaulting to the 1st, 15th, and 30th).

Payment dates are calculated iteratively across the full simulation duration. Transaction amounts are sampled from the

salary distribution (Table 4), with minor random variations applied to simulate overtime or bonuses. All transactions

[pp. 17-18] [ref: 4.5.6]

occur during business hours, and the established employer-employee links remain static throughout the simulation.

4.5.6 Fraudster background activity. As established in Section 2.2.1, a common sign of fraudulent activity is a deviation

from past transactional behaviour. To prevent classifiers from exploiting the absence of prior activity as a trivial

fraud signal, entities that partake in fraudulent patterns also maintain a transactional history that is statistically

indistinguishable from legitimate users.

The structural component selects fraudulent entities from our pre-computed cluster and pairs them with legitimate

entities to serve as transaction counterparts (as explained in Section 4.2.1). Unlike earlier iterations of this system, the

temporal component now generates transactions at the same rate as legitimate background activity, rather than at a

reduced rate. The expected number of transactions for each fraudster account is calculated as:

Fraudster transactions per account = max(1, ⌊𝑟× 𝑑⌋) (6)

Where 𝑟is the per-account daily transaction rate (identical to the rate used for legitimate random payments), and 𝑑is

the total number of days in the simulation period. The max function ensures each fraudster generates at least minimal

activity.

Transaction amounts are drawn from the same log-normal distributions as legitimate payments, so that amount

distributions do not distinguish fraudulent from legitimate accounts. Transaction direction is randomly determined

with equal probability for incoming and outgoing payments. All transactions are executed during business hours.

4.5.7 Counter-leakage background patterns. A naïve approach to background activity generation can introduce data

leakage: if certain transaction types, temporal signatures, or amount ranges appear exclusively in fraudulent patterns,

classifiers can exploit these artefacts rather than learning genuine structural indicators of money laundering. For

example, if cash deposits only occur in fraud patterns, then any deposit becomes a trivial fraud signal; similarly, if

periodic transfers or multi-hop chains are exclusively fraudulent, temporal and topological features leak the label.

To address this, we introduce seven additional background patterns that inject legitimate activity overlapping with

fraud signatures along three dimensions.

Temporal overlap. Legitimate bursts generate tight clusters of 5–15 transactions within minutes, modelling shopping

sprees or bill-payment runs, so that high-frequency activity is no longer exclusive to fraud.

Structural overlap. Legitimate transaction chains create multi-hop paths (𝐴→𝐵→𝐶→𝐷) of length 2–5, modelling

group expenses, family support flows, and business supply chains. These are topologically similar to layering hops but

are labelled as legitimate. Legitimate rapid fund flows generate inflow–outflow sequences resembling the rapid fund

movement pattern, based on scenarios such as account consolidation, emergency expenses, or event funding.

Feature overlap. Legitimate cash operations inject deposits and withdrawals sampled from the calibrated log-normal

[pp. 18-19] [ref: 4.6]

distributions (Table 4), so that cash transaction types are not exclusive to fraud. A rapid-deposit mode generates

3–5 deposits within hours, mimicking small-business cash handling. Legitimate structuring generates deposits in

the $7,500–$9,999 range for legitimate reasons (house savings, freelance income, small-business cash handling), with

an optional burst timing mode that clusters deposits within hours, matching the temporal signature of fraudulent

structuring. Unlike other transaction types, structuring amounts remain uniformly distributed in this sub-threshold

range, as this deliberate clustering is the behavioral signal AML systems must detect.

Legitimate high-risk entity activity ensures that entities with high risk scores, from high-risk jurisdictions, or

in high-risk business categories also engage in normal transaction activity, preventing the risk score from being a

near-perfect fraud predictor. All counter-leakage patterns also include fraudulent accounts among their participants

(typically 50–90% of fraud accounts are mixed in), ensuring that fraudulent entities are not topologically isolated from

legitimate activity.

Beyond structural and temporal overlap, all counter-leakage patterns sample transaction amounts from the same

log-normal distributions as standard background activity, preventing amount-based leakage. Table 14 summarises all

background patterns.

4.6 Framework Configurations and Additional Features

The data generation pipeline manages configuration, feature processing, and data export through a unified workflow.

4.6.1 Parameterization and Reproducibility. The system is controlled by two YAML configuration files. The first file

manages general graph-level parameters, such as the total number of entities and the simulation timeframe. The second

file defines pattern-specific parameters that specify the structural and transactional properties of the money-laundering

topologies. To ensure reproducibility, a random seed is applied at every step of the pipeline, making the graph structure,

attribute assignment, and transaction sequence fully deterministic.

4.6.2 Feature Selection and Data Splitting. To simulate a blind detection scenario, internal attributes used during

generation (e.g., risk_score, occupation, business_category) are excluded from the final dataset. The exported

Table 6. Published dataset variants. Both share the same base graph (8,000 individuals, 12-month simulation).

Variant Nodes Edges Illicit ratio Imbalance


---

[previous part](text-001.md) | [source overview](overview.md) | [next part](text-003.md)

[^original]: arXiv, "Tide: A Customisable Dataset Generator for Anti-Money Laundering Research" (2026-02-03). https://arxiv.org/abs/2603.01863
