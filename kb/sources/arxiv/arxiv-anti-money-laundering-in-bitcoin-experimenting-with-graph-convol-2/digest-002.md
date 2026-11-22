---
type: Source Digest
title: 'Anti-Money Laundering in Bitcoin: Experimenting with Graph Convolutional Networks for Financial Forensics - part 2 of 2 (pp. 6-7)'
description: 'Verified paraphrased digest, pp. 6-7: Anti-Money Laundering in Bitcoin: Experimenting with Graph Convolutional Networks for Financial Forensics > 6 GRAPH VISUALIZATION; Anti-Money Laundering in Bitcoin: Experimenting with Graph Convolutional Networks for Financial Forensics > 6.1 Visual Investigation of the Elliptic Data Set; Anti-Money Laundering in Bitcoin: Experimenting with Graph Convolutional Networks for Financial Forensics > 7 SUMMARY; and 2 more sections'
resource: https://arxiv.org/abs/1908.02591
tags:
- academic_finding
- datasets_benchmarks
- global_academic
- network_graph
- preprint
- virtual_assets
status: stable
source_id: arxiv-anti-money-laundering-in-bitcoin-experimenting-with-graph-convol-2
issuer: arxiv
issuer_name: arXiv
jurisdictions:
- GLOBAL_ACADEMIC
tier: 3
instrument_type: preprint
normative_force: academic_finding
publication_date: '2019-07-31'
legal_status: unknown
part: 2
parts_total: 2
content_mode: digest
generated:
  by: claude-code-subagent/claude-sonnet-5-5
  at: '2026-11-22T14:46:03Z'
verified:
- by: process:kb-digest-check/anchor-match
  at: '2026-11-22T14:46:03Z'
- by: claude-code-judge-agent/claude-opus-5-5
  at: '2026-11-22T14:46:03Z'
sources:
- id: original
  resource: https://arxiv.org/abs/1908.02591
  title: 'Anti-Money Laundering in Bitcoin: Experimenting with Graph Convolutional Networks for Financial Forensics'
  author: org:arxiv
  last_modified: '2019-07-31T00:00:00Z'
digest_points: 36
---

# Anti-Money Laundering in Bitcoin: Experimenting with Graph Convolutional Networks for Financial Forensics (digest)

[previous part](digest-001.md) | [source overview](overview.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (pp. 6-7) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **academic finding**.

## 6 GRAPH VISUALIZATION

- **descriptive / context**: The paper presents a visualization prototype called Chronograph, intended to support analysis and explainability, which the paper describes as important for AML compliance. (p. 6)[^original]  
  <sub>anchor: "we have created a visualization prototype called _Chronograph_ . Visualizing a high-dimensional graph imposes a layer"</sub>
- **descriptive / method**: In Chronograph, transactions are shown as graph nodes, with edges representing the flow of BTC from one transaction to the next. (p. 6)[^original]  
  <sub>anchor: "transactions are visualized as nodes of a graph with edges representing the flow of BTC from one transaction to the next"</sub>
- **descriptive / method**: Node coordinates are computed simultaneously across all time steps using the UMAP projection technique, which the paper says makes layouts comparable across time. (p. 6)[^original]  
  <sub>anchor: "Node coordinates are computed simultaneously across all time steps using the projection technique UMAP [15]. This global computation makes layouts comparable across time."</sub>
- **descriptive / method**: A time step slider lets the user navigate through time by rendering only the nodes in the selected time step. (p. 6)[^original]  
  <sub>anchor: "The time step slider control at the top of the interface allows the user to navigate through time by rendering only nodes in the selected time step."</sub>
- **descriptive / method**: Illicit transactions are coloured red, licit transactions blue, and unclassified transactions are not coloured. (p. 6)[^original]  
  <sub>anchor: "Illicit transactions are dyed red; licit ones are blue. Unclassified transactions are not colored."</sub>

## 6.1 Visual Investigation of the Elliptic Data Set

- **descriptive / method**: Clicking a transaction node, or entering a transaction ID (filtered as a substring), highlights the selected transaction(s) in orange and all neighbouring in- or out-flowing transactions in green. (p. 6)[^original]  
  <sub>anchor: "When clicking a transaction node, or entering a transaction ID in the control on the left (filters as substring) the visualization highlights the selected transaction(s) in orange"</sub>
- **descriptive / context**: The interface shows general graph statistics and a table of transfer numbers between transaction classes on the left. (p. 6)[^original]  
  <sub>anchor: "the user can see general statistics on the graph and a table about transfer numbers between different transaction classes"</sub>
- **descriptive / method**: The prototype is said to enable exploration of clusters and their existence over time, conspicuous transfer patterns, and outliers or other deviations. (p. 6)[^original]  
  <sub>anchor: "Chronograph enables simple exploration scenarios to visually inspect clusters and their existence over time"</sub>
- **descriptive / method**: The UMAP input can be altered: raw transaction feature data or neuron activations of the last network layer are presented as two alternatives. (p. 6)[^original]  
  <sub>anchor: "raw transaction feature data (Figure 4a), as well as neuron activations of the last layer of the network (Figure 4b) seem to be two interesting alternatives"</sub>
- **descriptive / expectation**: The authors postulate that shifts in similarities among the data can indicate which underlying features matter to the model. (p. 6)[^original]  
  <sub>anchor: "we postulate shifts in similarities among the data can be indicative to explain which underlying features matter to the model"</sub>
- **descriptive / finding or result**: In the model-based (activation) layout, illicit nodes are less scattered and more concentrated, which the authors regard as a desirable property, though they are not perfectly collapsed into one location. (p. 6)[^original]  
  <sub>anchor: "In the model-based layout illicit nodes are less scattered but more concentrated, which seems to be a desirable property"</sub>
- **descriptive / finding or result**: The visualization can reveal where the model fails to detect illicit nodes; multiple erroneous predictions in a nearby area could hint at systemic underperformance. (p. 6)[^original]  
  <sub>anchor: "The visualizations further reveals where exactly the model is unable to detect illicit nodes. In case of multiple erroneous predictions in a nearby area"</sub>
- **descriptive / finding or result**: Figure 4 shows results for the two alternative inputs for a single time step, with raw features in the top row and model activations in the bottom row, coloured by actual labels (left) and GCN-predicted labels (right), giving four network visualizations. (p. 6)[^original]  
  <sub>anchor: "Figure 4 shows the results from the two alternative inputs for a single time step, with raw feature data in the top and model activations in the bottom row"</sub>
- **descriptive / expectation**: The authors state that studying the characteristics of mis-predicted transactions in detail could inspire new angles and lead to further model improvements. (p. 6)[^original]  
  <sub>anchor: "Studying the characteristics of such transactions in detail could inspire the discussion from new angles and lead to further model improvements."</sub>
- **descriptive / context**: The authors note that the illicit nodes in the layout are not perfectly collapsed, which they suggest makes it plausible that there are qualitative differences within the illicit set. (p. 6)[^original]  
  <sub>anchor: "it is quite plausible there are qualitative differences within the set of illicit nodes"</sub>

## 7 SUMMARY

- **descriptive / context**: The authors present cryptocurrency forensics, specifically Bitcoin, as a unique ecosystem for crowdsourcing new methods to fight criminal activity. (p. 6)[^original]  
  <sub>anchor: "we have set forth cryptocurrency forensics, and specifically Bitcoin, as a unique ecosystem for crowdsourcing the development of new methods"</sub>
- **descriptive / data or feature**: The authors state they contributed a large, labelled transaction data set to the AML community, which they describe as never before publicly available. (p. 6)[^original]  
  <sub>anchor: "We have contributed a large, labelled transaction data set to the AML community, the likes of which has never before been publicly available."</sub>

## 6 GRAPH VISUALIZATION

- **descriptive / data or feature**: The authors created a visualization prototype called Chronograph to support analysis and explainability, which they describe as important for AML compliance. (p. 6)[^original]  
  <sub>anchor: "we have created a visualization prototype called _Chronograph_ . Visualizing a high-dimensional graph imposes"</sub>
- **descriptive / data or feature**: In Chronograph, transactions are nodes and edges represent the flow of BTC from one transaction to the next, with node coordinates computed across all time steps using UMAP so layouts are comparable over time. (p. 6)[^original]  
  <sub>anchor: "Node coordinates are computed simultaneously across all time steps using the projection technique UMAP [15]."</sub>
- **descriptive / data or feature**: A time step slider lets the user navigate time by rendering only nodes in the selected time step; illicit transactions are coloured red, licit blue, and unclassified transactions are uncoloured. (p. 6)[^original]  
  <sub>anchor: "Illicit transactions are dyed red; licit ones are blue. Unclassified transactions are not colored."</sub>

## 6.1 Visual Investigation of the Elliptic Data Set

- **descriptive / data or feature**: Selecting a transaction, or filtering by transaction ID, highlights the selected transaction(s) in orange and their in- or out-flowing neighbours in green; general graph statistics and a transfer table between transaction classes appear on the left. (p. 6)[^original]  
  <sub>anchor: "the visualization highlights the selected transaction(s) in orange, and all neighboring transactions (in-or-out-flowing) in green."</sub>
- **descriptive / finding or result**: The prototype enables exploration of clusters and their existence over time, conspicuous transfer patterns, and outliers. (p. 6)[^original]  
  <sub>anchor: "Chronograph enables simple exploration scenarios to visually inspect clusters and their existence over time,"</sub>
- **descriptive / method**: The authors postulate that shifts in similarities among the data can indicate which underlying features matter to the model. (p. 6)[^original]  
  <sub>anchor: "we postulate shifts in similarities among the data can be indicative to explain which underlying features matter to the model."</sub>
- **descriptive / finding or result**: Figure 4 shows results from the two alternative inputs for one time step, with raw features in the top row and model activations in the bottom row, coloured by actual labels (left) and GCN-predicted labels (right), giving four visualizations. (p. 6)[^original]  
  <sub>anchor: "Figure 4 shows the results from the two alternative inputs for a single time step, with raw feature data in the top"</sub>
- **descriptive / finding or result**: In the model-based layout illicit nodes are less scattered and more concentrated, which the authors consider a desirable property since similar nodes lie closer together. (p. 6)[^original]  
  <sub>anchor: "In the model-based layout illicit nodes are less scattered but more concentrated, which seems to be a desirable property"</sub>
- **descriptive / finding or result**: Illicit nodes do not collapse into one location, so the authors consider qualitative differences within the illicit set plausible. (p. 6)[^original]  
  <sub>anchor: "it is quite plausible there are qualitative differences within the set of illicit nodes."</sub>
- **descriptive / typology or red flag**: The visualization reveals where the model fails to detect illicit nodes; multiple erroneous predictions in a nearby area could hint at systemic underperformance of the model. (p. 6)[^original]  
  <sub>anchor: "In case of multiple erroneous predictions in a nearby area this could further hint to a systemic underperformance of the the model."</sub>
- **descriptive / finding or result**: Studying such mispredicted transactions in detail could inspire discussion from new angles and lead to further model improvements. (p. 6)[^original]  
  <sub>anchor: "Studying the characteristics of such transactions in detail could inspire the discussion from new angles and lead to further model improvements."</sub>

## 7 SUMMARY

- **descriptive / finding or result**: The authors set forth cryptocurrency forensics, specifically Bitcoin, as a unique ecosystem for crowdsourcing new methods to fight criminal activity. (p. 6)[^original]  
  <sub>anchor: "we have set forth cryptocurrency forensics, and specifically Bitcoin, as a unique ecosystem for crowdsourcing the development"</sub>
- **descriptive / data or feature**: The authors contributed a large, labelled transaction data set to the AML community, which had never before been publicly available. (p. 6)[^original]  
  <sub>anchor: "We have contributed a large, labelled transaction data set to the AML community, the likes of which has never before been publicly available."</sub>
- **descriptive / finding or result**: The authors report sharing early experimental results using a variety of methods, including Graph Convolutional Networks, and discussing possible next steps for algorithmic advances. (p. 7)[^original]  
  <sub>anchor: "shared early experimental results using a variety of methods including Graph Convolutional Networks, and discussed possible next steps"</sub>
- **descriptive / context**: The authors provide a visualization prototype for augmenting human analysis and explainability of such data and models. (p. 7)[^original]  
  <sub>anchor: "We have provided a prototype for visualization of such data and models for augmenting human analysis and explainability."</sub>
- **descriptive / finding or result**: The authors shared early experimental results using a variety of methods, including Graph Convolutional Networks, and discussed possible next steps for algorithmic advances. (p. 7)[^original]  
  <sub>anchor: "shared early experimental results using a variety of methods including Graph Convolutional Networks, and discussed possible next steps"</sub>
- **descriptive / data or feature**: The authors provided a visualization prototype for augmenting human analysis and explainability of such data and models. (p. 7)[^original]  
  <sub>anchor: "We have provided a prototype for visualization of such data and models for augmenting human analysis and explainability."</sub>
- **descriptive / context**: The authors close by hoping to have inspired others to work on making financial systems safer and more inclusive. (p. 7)[^original]  
  <sub>anchor: "we hope to have inspired others to work on this societally important challenge of making our financial systems safer and more inclusive"</sub>

## ACKNOWLEDGMENTS

- **descriptive / context**: The work was funded by the MIT-IBM Watson AI Lab, and data and domain expertise were provided by Elliptic.[^original]  
  <sub>anchor: "This work was funded by the MIT-IBM Watson AI Lab (mitibm.mit.edu)"</sub>

---

[previous part](digest-001.md) | [source overview](overview.md)

[^original]: arXiv, "Anti-Money Laundering in Bitcoin: Experimenting with Graph Convolutional Networks for Financial Forensics" (2019-07-31). https://arxiv.org/abs/1908.02591
