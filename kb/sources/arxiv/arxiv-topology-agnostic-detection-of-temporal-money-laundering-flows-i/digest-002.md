---
type: Source Digest
title: Topology-Agnostic Detection of Temporal Money Laundering Flows in Billion-Scale Transactions - part 2 of 3 (pp. 7-15)
description: 'Verified paraphrased digest, pp. 7-15: 4 The Method; 4 The Method > 4.1 Temporal Graph Creation; 4 The Method > 4.2 2_nd_ Order Graph Creation; and 6 more sections'
resource: https://arxiv.org/abs/2309.13662
tags:
- academic_finding
- advanced_analytics
- global_academic
- network_graph
- preprint
- transaction_behaviour
status: stable
source_id: arxiv-topology-agnostic-detection-of-temporal-money-laundering-flows-i
issuer: arxiv
issuer_name: arXiv
jurisdictions:
- GLOBAL_ACADEMIC
tier: 3
instrument_type: preprint
normative_force: academic_finding
publication_date: '2023-09-24'
legal_status: unknown
part: 2
parts_total: 3
content_mode: digest
generated:
  by: claude-code-subagent/claude-sonnet-5-5
  at: '2026-11-22T14:46:05Z'
verified:
- by: process:kb-digest-check/anchor-match
  at: '2026-11-22T14:46:05Z'
- by: claude-code-judge-agent/claude-opus-5-5
  at: '2026-11-22T14:46:05Z'
sources:
- id: original
  resource: https://arxiv.org/abs/2309.13662
  title: Topology-Agnostic Detection of Temporal Money Laundering Flows in Billion-Scale Transactions
  author: org:arxiv
  last_modified: '2023-09-24T00:00:00Z'
digest_points: 50
---

# Topology-Agnostic Detection of Temporal Money Laundering Flows in Billion-Scale Transactions (digest)

[previous part](digest-001.md) | [source overview](overview.md) | [next part](digest-003.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (pp. 7-15) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **academic finding**.

## 4 The Method

- **descriptive / method**: The FaSTM∀N framework is implemented in Spark and its Graphframes engine, which make its computations highly distributable and scalable. (p. 7)[^original]  
  <sub>anchor: "The entire framework is implemented in Spark [8] and its Graphframes [14] engine, which make the different computations"</sub>
- **descriptive / method**: The temporal graph of sequential transactions is built by inner joins on the dataset, processed iteratively one day at a time, to minimise the join memory footprint and allow the output graph to be saved and retrieved by time queries from the distributed file system. (p. 7)[^original]  
  <sub>anchor: "The transactions are processed iteratively, one day at a time. This ensures that 1) the memory footprint of the inner joins is minimized"</sub>
- **descriptive / context**: Illustrative example: account B may have passed only part of the money received from account A on to account C, but this will not hold in many other cases; insignificant relationships are removed in Section 4.3. (p. 7)[^original]  
  <sub>anchor: "account B might have only sent (a part of) the money to account C because it had earlier received (a part of) it from account A"</sub>

## 4.1 Temporal Graph Creation

- **descriptive / definition**: Definition 1: the temporal graph of sequential transactions is a static, attributed, directed graph with a node set of unique transaction identifiers (n transactions) and an edge set of directed source-destination pairs. (p. 7)[^original]  
  <sub>anchor: "A static, attributed, and directed graph T = {V, E, X} comprises 1) a node set V"</sub>
- **descriptive / definition**: Each node has an attribute vector containing the from account, the beneficiary account, the transaction timestamp and the transaction amount. (p. 8)[^original]  
  <sub>anchor: "vector xi = [ fi, bi, ti, ai ]. For vector xi, fi is the from account that sends the amount"</sub>
- **descriptive / definition**: An edge exists from node s to node d if the beneficiary account of s equals the from account of d and the timestamp of d falls after that of s and within a look-ahead window of length Δw. (p. 8)[^original]  
  <sub>anchor: "There exists an edge es,d iff : i) bs = fd, and ii) ts < td < ( ts + ∆w )"</sub>
- **descriptive / method**: Files are partitioned by source and destination dates so that any moment of the graph can be accessed instantly. (p. 8)[^original]  
  <sub>anchor: "The file partitioning is based on source and destination nodes’ dates, which makes it possible to time travel to any moment in the graph instantly."</sub>
- **descriptive / method**: The Δw parameter limits the number of edges; for most typologies a trail becomes uninteresting if the gap between consecutive transactions exceeds Δw days. (p. 8)[^original]  
  <sub>anchor: "any trail would become uninteresting if the time interval between consecutive transactions is longer than _∆w_ days."</sub>
- **descriptive / finding or result**: The Δw value used is very conservative and undisclosed; it yields around 25 billion edges in the temporal graph. (p. 8)[^original]  
  <sub>anchor: "therefore, we end up with around 25 billion edges."</sub>

## 4.2 2nd Order Graph Creation

- **descriptive / method**: The second-order graph S is derived from the temporal graph T, with nodes represented as the concatenation of from account and beneficiary account pairs, to quantify how dependent sequential transactions are on each other. (p. 8)[^original]  
  <sub>anchor: "the nodes in this graph will be represented by the concatenation of ( fi, →, bi )"</sub>

## 4.3 Weight Calculation

- **descriptive / definition**: Definition 2: the co-occurrence weight between a source edge A→B and destination edge B→C is the maximum of a source-perspective weight P and a destination-perspective weight P′. (p. 9)[^original]  
  <sub>anchor: "W ( A → B, B → C ) = max ( P ( A → B, B → C ) , P′ ( A → B, B → C ))"</sub>
- **descriptive / finding or result**: P reaches its maximum value of 1 when every time A sends money to B, B moves at least some of it exclusively to C; P′ reaches 1 when every receipt by C from B followed money B had received exclusively from A. (p. 9)[^original]  
  <sub>anchor: "every time A sends money to B; B moves (at least some of) the money exclusively to C."</sub>
- **descriptive / limitation**: The authors describe the weighting as very conservative; taking the maximum gives edges every chance to have a decent weight, and only extremely infrequent co-recurring behaviour yields low weights. (p. 9)[^original]  
  <sub>anchor: "It can be noticed here that again this is a very conservative calculation."</sub>
- **descriptive / method**: Weights are computed over the entire available dataset and then applied to the temporal graph T; edges with very low weight (threshold undisclosed) are filtered out to reduce the search space. (p. 9)[^original]  
  <sub>anchor: "we filter out all the edges with a very low undisclosed (see Reason 1 in Section 5) value."</sub>

## 4.4 Community Detection

- **descriptive / method**: The weighted, directed edges of T are passed to the Leiden algorithm, which guarantees better quality communities and accounts for edge direction and weight. (p. 9)[^original]  
  <sub>anchor: "In addition to guaranteeing better quality communities, the algorithm also takes into account the"</sub>
- **descriptive / method**: A max community size parameter in the Leiden library limits the number of transactions in a single flow; this is the final step of FaSTM∀N, producing communities of significant and interdependent money flows. (p. 10)[^original]  
  <sub>anchor: "we can also limit the number of transactions we want to include in a single flow (or community)."</sub>

## 4.5 Anomalous Communities Detection

- **descriptive / method**: Suspicious networks can be identified by traditional anomaly detection on summarised vector representations of flows, or by deep learning graph-level anomaly detection (GLAD) methods; this step is not strictly part of the framework. (p. 10)[^original]  
  <sub>anchor: "we can identify the suspicious networks by either applying 1) traditional anomaly detection methods"</sub>
- **descriptive / definition**: AML risk criterion C1: the dispense and sink accounts should belong to certain undisclosed segments. (p. 10)[^original]  
  <sub>anchor: "The dispense and sink accounts should belong to certain ( undisclosed ) segments, and"</sub>
- **descriptive / definition**: AML risk criterion C2: the percentage of dispensed amount that has been sunk should be within a certain undisclosed range. (p. 10)[^original]  
  <sub>anchor: "The percentage of dispensed amount that has been sunk should be within a certain ( undisclosed ) range"</sub>
- **descriptive / definition**: AML risk criterion C3: the maximum flow of money, respecting temporal order, should exceed an undisclosed threshold. (p. 10)[^original]  
  <sub>anchor: "The maximum flow, respecting the temporal order, of money should be greater than a certain ( undisclosed ) threshold"</sub>

## 5 Experimental Evaluation

- **descriptive / context**: The paper claims superiority of FaSTM∀N over FlowScope and DBJ in scalability and effectiveness; the implementation is shared publicly but the AML risk calculation is not. (p. 10)[^original]  
  <sub>anchor: "The part that has not been shared is the AML risk calculation (Section 4.5)."</sub>
- **descriptive / context**: Authors withhold risk calculation details (Reason 1) because criminals could work around a known calculation, and withhold flow details such as amounts and bank names (Reason 2) because they could alert criminals. (p. 10)[^original]  
  <sub>anchor: "By learning about the details of a specific risk calculation, criminals can try to work around it to avoid detection."</sub>

## 5.1 Experimental Setting

- **descriptive / context**: The authors claim the temporal graph can detect all 2-hop flows found by DBJ and can extend traversal to more hops, making it a more scalable version of DBJ, referred to as DBJ*. (p. 10)[^original]  
  <sub>anchor: "With graph T we can detect all the 2-hop flows detected by DBJ."</sub>
- **descriptive / limitation**: The authors could not obtain the dataset used for the DBJ results even after contacting its authors. (p. 11)[^original]  
  <sub>anchor: "We were unable to obtain the dataset used for generating the results in DBJ, even after contacting the authors."</sub>
- **descriptive / method**: The motif chosen for evaluating DBJ is type 2: one dispense account sending to multiple intermediate accounts that sink the money into one bank account; for 3 hops it is 1→[*]→[*]→1. (p. 11)[^original]  
  <sub>anchor: "1 dispense account sending money to multiple [*] intermediate accounts; which then sink the money to 1 bank account."</sub>
- **descriptive / limitation**: Type 1 motif was not chosen because for more than 2 hops it can be configured in numerous ways. (p. 11)[^original]  
  <sub>anchor: "We did not choose type 1 as, for hops greater than 2, the motif could be configured in numerous ways."</sub>
- **descriptive / limitation**: The authors describe a design flaw in FlowScope: its k-partite graphs are built around middle accounts of a pass-through bank, so with data from 5 banks there are 31 possible pass-through bank combinations, and extending the design would need substantial effort. (p. 11)[^original]  
  <sub>anchor: "if you have data from 5 banks, you can have 31 different combinations of banks you can assign as the pass-through bank(s)."</sub>
- **descriptive / finding or result**: The authors assume FlowScope could produce all flows found by FaSTM∀N if run multiple times with different k values, and argue some flows would still go undetected after the risk score is applied (see Fig. 12). (p. 11)[^original]  
  <sub>anchor: "We will assume that it can produce all the flows detected by FaSTM ∀ N , after running it multiple times with different values of k ."</sub>
- **descriptive / method**: Pre-processing removes the extremely highly connected accounts, the top 0.0001% by connectedness, in the most conservative manner. (p. 11)[^original]  
  <sub>anchor: "We only do that for the top 0.0001% accounts."</sub>
- **descriptive / finding or result**: Pre-processing reduces the dataset from 1.1 billion transactions to around 510 million transactions. (p. 11)[^original]  
  <sub>anchor: "This results in a reduction of the actual dataset of 1.1 billion transactions, to around 510 million transactions."</sub>
- **descriptive / finding or result**: DBJ's pre-processing keeps only about 0.002% of its original transactions, which the authors say leaves many interesting flows undetected even for smurfing. (p. 11)[^original]  
  <sub>anchor: "They merely keep around 0.002% of their original transactions."</sub>
- **descriptive / finding or result**: Even when covering 100% of the smurfing cases, the extensive DBJ filtering makes DBJ infeasible for detecting other AML typologies, according to the authors. (p. 11)[^original]  
  <sub>anchor: "Even when covering 100% of the smurfing cases, such extensive filtering makes DBJ infeasible"</sub>
- **descriptive / limitation**: The authors argue DBJ's naive grouping of flows causes investigators to review many cases with overlapping bank accounts, and those cases still miss accounts that should have been flagged. (p. 12)[^original]  
  <sub>anchor: "because of its na¨ıve grouping of the flows 1) an AML investigator will have to go through a lot of cases with overlapping bank accounts"</sub>

## 5.2 Results

- **descriptive / data or feature**: Table 2 reports space explosion and implosion: initial state 1.1 billion transactions; pre-processing 510 million; T creation 475 million transactions and 25 billion T edges; removing weak edges 325 million transactions and 2.3 billion T edges. (p. 12)[^original]  
  <sub>anchor: "Table 2 shows how different stages of FaSTM ∀ N explodes and then implodes the search space."</sub>
- **descriptive / finding or result**: The authors state that the number of edges in the final T is about twice the number of transactions. (p. 12)[^original]  
  <sub>anchor: "we merely doubled that quantity for the (final) number of edges in T."</sub>
- **descriptive / method**: Most of the framework is distributed join and aggregate operations; the most complex step is the Leiden algorithm, described as empirically close to linear in the number of edges, and it can be parallelised per window. (p. 12)[^original]  
  <sub>anchor: "For most applications, the algorithm is said to be (empirically) close to linear time with respect to the number of edges."</sub>
- **descriptive / finding or result**: All steps except the final risk-scoring and suspicious-community selection are described as model and typology agnostic, so one run can feed many models covering several risks. (p. 13)[^original]  
  <sub>anchor: "All the steps in FaSTM ∀ N except the last one, for (risk) scoring and picking the suspicious communities, are model and typology agnostic."</sub>
- **descriptive / finding or result**: In a batch experiment where each new batch was appended to earlier output, the runtime of each step is almost linear in the number of transactions per batch, and cumulative processing does not show a compounding effect on total runtime. (p. 13)[^original]  
  <sub>anchor: "It can be seen in Fig. 8 that the runtime of each step is (almost) linear with respect to the number of transactions in a batch."</sub>
- **descriptive / method**: For time complexity, the authors compare only the community detection runtime of FaSTM∀N against the motif searching runtime of DBJ*, and then compare results after applying the same risk scoring. (p. 13)[^original]  
  <sub>anchor: "we are therefore, only going to compare the runtimes for the community detection part"</sub>
- **descriptive / finding or result**: Fig. 9 shows the number of DBJ* flows explodes with each additional hop, producing mostly flows with overlapping transactions, whereas FaSTM∀N detects disjoint communities and detects communities once regardless of hop count. (p. 13)[^original]  
  <sub>anchor: "This is not the case with FaSTM ∀ N , as the Leiden algorithm detects disjoint communities."</sub>
- **descriptive / finding or result**: After hop 5 the DBJ* search space becomes exponentially large, which affects its runtime. (p. 13)[^original]  
  <sub>anchor: "After hop 5, the search space starts to become exponentially large for DBJ*."</sub>
- **descriptive / finding or result**: Runtime for flagging suspicious flows rises with hops for DBJ*, while for FaSTM∀N it is very low because only flows containing the segments in criterion C1 need flagging and fewer flows are generated. (p. 13)[^original]  
  <sub>anchor: "Fig. 10(a) shows how with more hops, the runtime of DBJ* for flagging the flows increases."</sub>
- **descriptive / definition**: Coverage is defined as the percentage of suspicious bank accounts found by a method out of all suspicious accounts found by all three methods. (p. 14)[^original]  
  <sub>anchor: "Coverage of a method is defined as the percentage of suspicious bank accounts found by that method"</sub>
- **descriptive / finding or result**: Including weights improves FaSTM∀N case coverage from 55% to 70% with nearly the same number of cases compared with the version without weights (FaSTM∀N-w). (p. 14)[^original]  
  <sub>anchor: "is able to improve case coverage from 55% to 70% with nearly the same number of cases."</sub>
- **descriptive / finding or result**: The authors argue DBJ* would need numerous motif configurations to approach FaSTM∀N coverage, producing astronomically many flows that would be practically impossible to investigate because most flows have repeated accounts and transactions. (p. 14)[^original]  
  <sub>anchor: "This would result in astronomically high number of flows."</sub>
- **descriptive / finding or result**: Topological diversity (Fig. 11) shows FaSTM∀N is parameter-free and detects flows with varying path lengths, supporting the claim that complex laundering involves more than 2 hops; diverse diameter values and numbers of dispense and sink accounts are observed for detected and suspicious flows. (p. 14)[^original]  
  <sub>anchor: "we observe a diverse range of values for diameter;"</sub>
- **descriptive / case example**: Fig. 12 shows two real flows that FlowScope would miss even after multiple configurations; FaSTM∀N detected the complete flows including all relevant bank accounts, while FlowScope needed 2 configurations of k for case 1 and 3 for case 2. (p. 15)[^original]  
  <sub>anchor: "To detect the same flows using FlowScope, it has to be run with 2 configurations of k for the first case; and 3 for the second case."</sub>
- **descriptive / case example**: In case 1, both flows go undetected by FlowScope because neither individually meets criterion C3, as the maximum flow does not reach the minimum threshold. (p. 15)[^original]  
  <sub>anchor: "both flows will go undetected because individually neither of them qualify for C3"</sub>
- **descriptive / case example**: In case 2, the flow FlowScope detects with k=4 goes undetected while the other two qualify, leaving 2 additional suspicious accounts in that flow undetected, which lowers case quality. (p. 15)[^original]  
  <sub>anchor: "the flow detected by FlowScope with k=4 will go undetected; the other two would qualify."</sub>
- **descriptive / limitation**: The authors cannot show or summarise all cases because of Reason 2 about revealing flow details. (p. 15)[^original]  
  <sub>anchor: "We can not further show or (even) summarize all the cases because of Reason 2"</sub>

---

[previous part](digest-001.md) | [source overview](overview.md) | [next part](digest-003.md)

[^original]: arXiv, "Topology-Agnostic Detection of Temporal Money Laundering Flows in Billion-Scale Transactions" (2023-09-24). https://arxiv.org/abs/2309.13662
