---
type: Source Text
title: 'GARG-AML against Smurfing: A Scalable and Interpretable Graph-Based Framework for Anti-Money Laundering - part 10 of 10 (pp. 40-41)'
description: 'Verbatim extracted text, pp. 40-41: D Limited Transaction View'
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
part: 10
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

[previous part](text-009.md) | [source overview](overview.md)

> Verbatim text extracted from the original (arXiv, 2025-04-06), part 10 of 10, pp. 40-41. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **academic finding**.[^original]

## D Limited Transaction View


[p. 40]

We analyse two set-ups. The first is to consider the largest bank in the dataset, called bank 012. This shows the performance when a bank only has access to transactions involving their own clients. The second is to consider the collection of transactions at the 50 largest banks. This shows the performance when banks share information, e.g., through a specialised collaboration or because they are part of the same banking group. Table D.1 summarises the resulting datasets.

Table D.1: How much of the HI-Small network one institution observes. Percentages are shares of the full network.

|Bank|Clie|nts|Transact|ions|Launde|ring tx.|
|---|---|---|---|---|---|---|
||_n_|%|_n_|%|_n_|%|
|012|2,639|0.51|99,452|1.96|146|2.82|
|top-50|55,423|10.76|1,592,556|31.36|1,722|33.26|

For each case, we compare the original GARG-AML scores, where full visibility of the network is assumed, with the scores computed on the limited view of the institution. The change in performance is given in Figure D.1 for the label cut-offs 0 and 0.1, with 87 and 16 positive clients for bank 012 and 1,315 and 379 for the top-50 banks. Louvain pre-processing is switched off in both views, so the full-network values differ from those in the main text.

The performance of the GARG-AML scores is low in most settings. At cut-off 0, the AUC-ROC is below 0.5 for both institutions, for the undirected and the directed score, on the full network (0.39–0.47) as well as on the institution’s view. Only the top-50 banks at cut-off 0.1 reach a clearly better-than-random AUC-ROC (0.67 for the undirected and 0.57 for the directed score), with an AUC-PR of 1.5–1.6 times (undirected) and 1.3 times (directed) the prevalence. Limiting the view does not reduce the performance in the settings with at least 30 positives. For bank 012 at cut-off 0, the AUC-ROC of the undirected score changes from 0.39 to 0.46 and that of the directed score is unchanged (0.43), and for the top-50 banks all changes in AUC-ROC are at most 0.03 (e.g., 0.669 to 0.670 for the undirected score at cut-off 0.1). The only large change is the undirected score of bank 012 at cut-off 0.1 (AUC-ROC from 0.70 to 0.50), but this rests on only 16 positives and is not interpretable. Hence, we find no evidence that the limited view deteriorates performance, but for the single bank there is also no reliable signal to begin with. A possible explanation for the slight improvements is that many of the laundering patterns are one-hop patterns, which remain visible to the institution, while the limited view removes the noise of subsequent transactions.

Figure D.2 shows that in the single bank view, almost all second-order neighbours are invisible to the bank (on average 7% visible, median 1%). For the larger banking group consisting of the top-50 banks, the shares are more spread out, with on average 42% (median 33%) of the second-order neighbourhood visible. A banking group with a substantial market share (here 31% of all transactions) therefore observes a considerable part of its clients’ second-order neighbourhoods, even when fraudsters spread their transactions over several banks. For most clients, however, a large part of the neighbourhood is still missing, so these results are encouraging but not conclusive: they rely on a single simulated dataset, in which the distribution of clients over banks is not realistic.

[p. 41]

Undirected Directed full network institution's viewBank 012 · cut-off 0(87 positives)Bank 012 · cut-off 0.1(16 positives)Top-50 banks · cut-off 0(1315 positives)Top-50 banks · cut-off 0.1(379 positives)0.40 0.45 0.50 0.55 0.60 0.65 0.70 0.8 1.0 1.2 1.4 1.6 1.8AUC-ROC AUC-PR / prevalencefaded: fewer than 30 positives, not interpretable

Figure D.1: AUC-ROC (left) and AUC-PR relative to prevalence (right) of the GARG-AML score for the clients of an institution, on the full network (open markers) and on the institution’s view (filled markers), for the undirected and directed score at label cut-offs 0 and 0.1. The number of positive clients is given per row. Louvain pre-processing is switched off in both views, so the full-network values differ from those in the main text. Faded rows have fewer than 30 positives and are not interpretable. Dotted lines mark a random ranking (AUC-ROC of 0.5; AUC-PR equal to the prevalence).

Bank 012 Top-50 banks0.6 mean 0.07 mean 0.42median 0.010 median 0.3330.50.40.30.20.10.00.0 0.2 0.4 0.6 0.8 1.0 0.0 0.2 0.4 0.6 0.8 1.0share of N 2 still visible share of N 2 still visibleshare of clients

Figure D.2: Share of each client’s second-order neighbourhood that is still visible in the institution’s view of HI-Small: bank 012 (left) and the 50 largest banks pooled (right). The dashed line is the mean. Clients with no second-order neighbourhood on the full network are not shown.


---

[previous part](text-009.md) | [source overview](overview.md)

[^original]: arXiv, "GARG-AML against Smurfing: A Scalable and Interpretable Graph-Based Framework for Anti-Money Laundering" (2025-04-06). https://arxiv.org/abs/2506.04292
