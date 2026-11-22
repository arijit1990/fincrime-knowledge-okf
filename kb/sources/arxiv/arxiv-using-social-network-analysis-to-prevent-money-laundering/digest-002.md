---
type: Source Digest
title: Using social network analysis to prevent money laundering - part 2 of 3 (pp. 14-25)
description: 'Verified paraphrased digest, pp. 14-25: Using Social Network Analysis to Prevent Money Laundering > 3.2. Network and Control Variables; Using Social Network Analysis to Prevent Money Laundering > 4. Results; Using Social Network Analysis to Prevent Money Laundering > 5. Discussion and Conclusions; and 2 more sections'
resource: https://arxiv.org/abs/2105.05793
tags:
- academic_finding
- global_academic
- network_graph
- preprint
- typologies
status: stable
source_id: arxiv-using-social-network-analysis-to-prevent-money-laundering
issuer: arxiv
issuer_name: arXiv
jurisdictions:
- GLOBAL_ACADEMIC
tier: 3
instrument_type: preprint
normative_force: academic_finding
publication_date: '2016-09-20'
legal_status: unknown
part: 2
parts_total: 3
content_mode: digest
generated:
  by: claude-code-subagent/claude-sonnet-5-5
  at: '2026-11-22T14:46:06Z'
verified:
- by: process:kb-digest-check/anchor-match
  at: '2026-11-22T14:46:06Z'
- by: claude-code-judge-agent/claude-opus-5-5
  at: '2026-11-22T14:46:06Z'
sources:
- id: original
  resource: https://arxiv.org/abs/2105.05793
  title: Using social network analysis to prevent money laundering
  author: org:arxiv
  last_modified: '2016-09-20T00:00:00Z'
digest_points: 40
---

# Using social network analysis to prevent money laundering (digest)

[previous part](digest-001.md) | [source overview](overview.md) | [next part](digest-003.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (pp. 14-25) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **academic finding**.

## 3.2. Network and Control Variables

- **descriptive / method**: The graph is represented by a sociomatrix in which an element is greater than zero only if an arc runs from one node to another; positive values give arc weights, and unweighted arcs are represented by a dichotomized 0/1 matrix. (p. 14)[^original]  
  <sub>anchor: "If arcs are not weighted, we consider a dichotomized sociomatrix where each element can only assume the value 0 or 1."</sub>
- **descriptive / definition**: Weighted in-degree counts incoming ties, i.e. the number of times a client acts as a seller, with incoming arc values summed to capture the risk of the total number of operations. (p. 14)[^original]  
  <sub>anchor: "This measure counts the number of incoming ties, i.e. the number of times a client acts as a seller."</sub>
- **descriptive / method**: The study uses common centrality measures (in-degree, out-degree, all-degree, closeness and betweenness) to identify relevant social actors, chosen to make the method easier to understand and replicate. (p. 14)[^original]  
  <sub>anchor: "we referred to some of the most common measures of centrality"</sub>
- **descriptive / definition**: Weighted out-degree counts outgoing ties, i.e. the number of times a client acts as a debtor, and can be weighted in the same way as in-degree. (p. 15)[^original]  
  <sub>anchor: "This measure counts the number of outgoing ties, i.e. the number of times a client acts as a debtor"</sub>
- **descriptive / definition**: Weighted all-degree counts ties to a node regardless of direction, with the risk factor being the sum of weights of all arcs connected to the node; it replaces in-degree and out-degree on undirected networks. (p. 15)[^original]  
  <sub>anchor: "This measure substitutes in-degree and out-degree on undirected networks."</sub>
- **descriptive / definition**: Closeness is the inverse of a node's distance from all others, based on shortest paths, and is used as a proxy for how quickly a social actor can reach others; it can be standardised by multiplying by g minus 1. (p. 15)[^original]  
  <sub>anchor: "It is often used as a proxy of the speed by which a social actor can reach the others."</sub>
- **descriptive / definition**: Betweenness is higher when a node lies more often between the shortest paths connecting other pairs of nodes; it can be standardised by dividing by the number of pairs of actors not including the node. (p. 15)[^original]  
  <sub>anchor: "This measure is higher when a node is more frequently in-between the shortest paths that connect every other couple of nodes."</sub>
- **descriptive / definition**: Network constraint, introduced by Burt (1995) in relation to structural holes, measures how constrained each node is by its ego-network; the fewer the structural holes, the more the node is constrained to group rules. (p. 16)[^original]  
  <sub>anchor: "The less the structural holes in an ego-network, the more the node is constrained to the group rules."</sub>
- **descriptive / context**: The paper illustrates structural holes with three nodes A, B and C where A is linked to both B and C but B and C are not linked; A can mediate and benefit from the missing link, and Burt (2004) is cited that brokerage across structural holes brings advantages. (p. 16)[^original]  
  <sub>anchor: "It has been proved that brokerage across structural holes can have several advantages"</sub>
- **descriptive / definition**: The missing-identifier control variable counts the number of times a seller is associated with financial operations where the owner, representative or debtor is missing; the authors examine whether missing data follows a recognisable pattern. (p. 17)[^original]  
  <sub>anchor: "It counts the number of times a seller is associated to financial operations where the owner, the representative, or the debtor are missing."</sub>
- **descriptive / limitation**: Age and size of seller and debtor companies could not be controlled for because this information was not recorded in the database; the authors propose it for future research. (p. 17)[^original]  
  <sub>anchor: "Nonetheless, we could not collect such information, as it was not recorded in our database."</sub>
- **descriptive / definition**: The dependent variable High Risk is binary: one if the owner or representatives were involved in anti-money laundering investigations or trials at data collection or in the previous three years according to Italian court records, zero otherwise. (p. 17)[^original]  
  <sub>anchor: "we created a binary dependent variable (named High Risk ) that has the value of one if either the owner or the representatives were involved in legal trials"</sub>
- **descriptive / limitation**: Complete court data were obtained for 288 cases of the total sample, because collecting court data required recombining fragmented sources and missing owner or representative data reduced complete observations; network metrics used the full sample. (p. 17)[^original]  
  <sub>anchor: "thus having the possibility to gather complete data for 288 cases over the total sample"</sub>
- **descriptive / requirement**: The authors hypothesise that more central nodes, with more connections, more frequent economic transactions and a larger presence on paths, have a higher risk profile, and that nodes with lower network constraint carry higher risk. (p. 17)[^original]  
  <sub>anchor: "We hypothesize that more central nodes with a higher number of connections"</sub>
- **descriptive / finding or result**: Correlation coefficients of the predictors with the High Risk dependent variable are reported in Table 1, covering network metrics for geographical area, transactions and economic sector networks plus missing identifier. (p. 18)[^original]  
  <sub>anchor: "Correlation coefficients of our predictors with the dependent variable are presented in Table 1."</sub>

## 4. Results

- **descriptive / finding or result**: Table 1 correlations with High Risk: Missing Id .166; geographical in-degree .249; geographical out-degree .312; geographical all-degree .257; geographical closeness .049; geographical betweenness .296; geographical network constraint -.108; weighted transaction in-degree .240; transaction out-degree .203; transaction all-degree .314; transaction closeness -.053; transaction betweenness .254; transaction network constraint -.220. (p. 18)[^original]  
  <sub>anchor: "Missing Id|.166|1"</sub>
- **descriptive / finding or result**: Table 1 correlations with High Risk for economic sector networks: in-degree .236; out-degree .326; all-degree .259; closeness .088; betweenness .254; network constraint -.270. Several table cells are garbled and some values are marked with asterisks in the extracted text. (p. 18)[^original]  
  <sub>anchor: "In-degree EconomicSector|.236|-.013|.213|.394"</sub>
- **descriptive / finding or result**: Clients associated with transactions with missing information about the owner, representative or counterpart are more likely to have a high-risk profile. (p. 20)[^original]  
  <sub>anchor: "clients associated to transactions with missing information – about the owner, the representative, or the counterpart – are more likely to have a high-risk profile"</sub>
- **descriptive / finding or result**: Three networks play a major role in assessing risk profiles: those built on economic sector, geographical areas of activity, and total amount of financial operations. (p. 20)[^original]  
  <sub>anchor: "three networks play a major role when assessing risk profiles"</sub>
- **descriptive / finding or result**: Degree centrality, closeness centrality and network constraint proved significant; betweenness centrality was significant in correlations but lost its importance in predictive models. (p. 20)[^original]  
  <sub>anchor: "By contrast, we surprisingly notice a marginal role of betweenness centrality"</sub>
- **descriptive / finding or result**: In Model 2, companies that more frequently buy from firms in high-risk geographical areas are more likely to be involved in illicit operations. (p. 20)[^original]  
  <sub>anchor: "companies that more frequently buy products or services from firms operating in high risk geographical areas are more probably involved in illicit operations"</sub>
- **expected / recommendation**: The authors state that companies with lower network constraint spanning riskier economic sectors should be considered more suspicious and deserve more attention. (p. 20)[^original]  
  <sub>anchor: "companies with a lower network constraint, spanning their activities between riskier economic sectors, should be considered more suspicious"</sub>
- **descriptive / finding or result**: In Model 3, a higher total amount of transactions is associated with higher risk of fraud, while higher closeness is associated with lower risk, a result the authors say partially contrasts their hypothesis; the closeness effect is rather small. (p. 20)[^original]  
  <sub>anchor: "the higher the total amount of transactions, the higher the risk of fraud"</sub>
- **descriptive / finding or result**: The final model combining predictors has a McFadden R-squared of 0.327 with significant reductions in AIC and BIC, which the authors interpret as good predictive power validating their approach. (p. 20)[^original]  
  <sub>anchor: "obtaining a Mc Fadden’s R-Squared of 0.327 and significant reductions in AIC and BIC scores"</sub>
- **expected / recommendation**: The authors maintain that financial operations of clients with higher risk profiles should be signalled to local authorities for more in-depth investigation at national level. (p. 20)[^original]  
  <sub>anchor: "the financial operations of those clients who can be associated to higher risk profiles should be signaled to the local authorities"</sub>
- **descriptive / data or feature**: The Tacit Link Network analysed comprised 90 non-isolate nodes; it is fairly sparse with few links but shows well-separated clusters, so no clustering algorithms were needed. (p. 20)[^original]  
  <sub>anchor: "we analyzed the non-isolate 90 nodes in the Tacit Link Network"</sub>
- **descriptive / finding or result**: Blue nodes (clients involved in AML or crime financing trials) are almost perfectly clustered in the Tacit Link Network. (p. 21)[^original]  
  <sub>anchor: "Blue nodes are those clients who were involved in AML or crime financing trials."</sub>
- **descriptive / limitation**: Involvement of one company in a cluster does not always imply that all other companies in that cluster will be involved, as some may operate in different sectors with independent activities even when sharing an owner. (p. 21)[^original]  
  <sub>anchor: "the fact that a company in a cluster gets involved in criminal proceedings does not always imply that all the other companies in that cluster will be involved"</sub>

## 5. Discussion and Conclusions

- **descriptive / context**: The key contribution is emphasising social network metrics and new network mapping techniques not traditionally associated with anti-money laundering; the authors argue relational data is more informative than single attributes of social units. (p. 21)[^original]  
  <sub>anchor: "The key contribution of this paper is to emphasize the role of social network metrics"</sub>
- **descriptive / data or feature**: The case study uses the central database of a medium-large factoring company operating in Italy, from which four kinds of relational graphs were mapped: economic sector, geographical area, transaction amount, and tacit links between companies sharing an owner or representatives. (p. 22)[^original]  
  <sub>anchor: "we analyzed the central database of a medium-large factoring company operating in Italy"</sub>
- **expected / recommendation**: The authors propose using the tacit link network as an alarm trigger, suggesting all nodes in a cluster be checked carefully once one becomes involved in suspicious or illicit operations. (p. 22)[^original]  
  <sub>anchor: "we propose using this network as an alarm trigger, suggesting to carefully check all the nodes in a cluster"</sub>
- **descriptive / finding or result**: Higher-risk clients are less central in the transactions network (closeness) and usually deal with larger financial amounts; this partially contrasts Ferrara et al. (2014), who pointed to higher centrality for criminals. (p. 22)[^original]  
  <sub>anchor: "clients with higher risk profiles are less central in the transactions network (closeness centrality)"</sub>
- **descriptive / finding or result**: Because honest nodes predominate, the authors argue that honest nodes are more closely connected while criminals sit on more peripheral positions, possibly because new companies enter and leave the network quickly without acquiring central positions. (p. 22)[^original]  
  <sub>anchor: "criminals lie on more peripheral positions"</sub>
- **descriptive / finding or result**: A larger in-degree centrality on the geographical area network and a lower network constraint on the business sector graph increase the probability of dealing with a subject involved in court trials. (p. 22)[^original]  
  <sub>anchor: "a larger in-degree centrality on the Geographical Area Network and a lower network constraint on the business sector graph prove to increase the probability"</sub>
- **expected / recommendation**: The authors suggest focusing attention on clients operating in riskier sectors and who are less constrained, spreading connections across several regions and countries posing greater threat to financial stability. (p. 22)[^original]  
  <sub>anchor: "we suggest to focus the attention on those clients who operate in more risky sectors and who are less constrained"</sub>
- **descriptive / context**: Drezewski et al. (2015) also apply social network analysis to money laundering detection but focus on criminal social roles, whereas this study focuses on network mapping and risk profiles of companies in factoring business. (p. 23)[^original]  
  <sub>anchor: "even if their primary focus is on criminal social roles, whereas ours is on network mapping"</sub>
- **descriptive / limitation**: The dependent variable is based on past event data, which is a main limitation of the study. (p. 23)[^original]  
  <sub>anchor: "A main limitation of our dependent variable is the fact of being based on past events data."</sub>
- **recommended / recommendation**: Future research could study behaviours of leavers and newcomers in networks, test other dependent variables, classify risky sectors and regions differently, and use stochastic actor based models to explain network evolution over time. (p. 23)[^original]  
  <sub>anchor: "stochastic actor based models could be used to explain the mechanisms that drive the evolution of networks over time"</sub>
- **recommended / recommendation**: The authors suggest the network metrics should be combined with other tools, such as machine learning algorithms and national-level data, to allow quick detection of suspicious nodes and prevent money laundering. (p. 23)[^original]  
  <sub>anchor: "should be combined with other tools – based, for instance, on machine learning algorithms"</sub>
- **permissive / limitation**: A larger sample could be analysed, including different financial institutions, to test whether the findings generalise or are more effective when related to factoring businesses. (p. 23)[^original]  
  <sub>anchor: "a bigger sample could be analyzed, also involving different financial institutions"</sub>

---

[previous part](digest-001.md) | [source overview](overview.md) | [next part](digest-003.md)

[^original]: Andrea Fronzetti Colladon, Elisa Remondi, "Using social network analysis to prevent money laundering" (2016-09-20). https://arxiv.org/abs/2105.05793
