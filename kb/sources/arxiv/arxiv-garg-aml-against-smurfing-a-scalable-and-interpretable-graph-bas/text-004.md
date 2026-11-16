---
type: Source Text
title: 'GARG-AML against Smurfing: A Scalable and Interpretable Graph-Based Framework for Anti-Money Laundering - part 4 of 10 (pp. 16-20)'
description: 'Verbatim extracted text, pp. 16-20: 5 Results and Discussion > 5.1 Scalability; 5 Results and Discussion > 5.2.1 Synthetic Data; 5 Results and Discussion > 5.2.2 IBM Data'
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
part: 4
parts_total: 10
content_mode: full_text
generated:
  by: process:fincrime-kb-build
  at: '2026-11-16T16:31:16Z'
verified:
- by: process:kb-validate/verbatim-coverage
  at: '2026-11-16T16:31:16Z'
sources:
- id: original
  resource: https://arxiv.org/abs/2506.04292
  title: 'GARG-AML against Smurfing: A Scalable and Interpretable Graph-Based Framework for Anti-Money Laundering'
  author: org:arxiv
  last_modified: '2025-04-06T00:00:00Z'
---

# GARG-AML against Smurfing: A Scalable and Interpretable Graph-Based Framework for Anti-Money Laundering

[previous part](text-003.md) | [source overview](overview.md) | [next part](text-005.md)

> Verbatim text extracted from the original (arXiv, 2025-04-06), part 4 of 10, pp. 16-20. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **academic finding**.[^original]

## 5 Results and Discussion


### 5.1 Scalability


[pp. 16-17]

Figure 6 and Figure 7 show the calculation times across the various network sizes of the synthetic and IBM datasets, respectively. The time in Figure 6 is shown on a logarithmic scale, to provide a better distinction across dataset sizes. These results indicate that FlowScope is the fastest method, although GARG-AML seems to scale well to larger datasets, contrary to what we expected from the theoretical worst-case time complexity. In contrast, AutoAudit, although quite fast in the beginning, has difficulties with the largest networks. The distribution of the calculation time of AutoAudit is much wider with more outliers, indicating a high sensitivity to the network topology.

Additionally, AutoAudit consistently runs out of time, exceeding 16 hours, on Watts-Strogatz networks of size 10,000. We set the out-of-time results equal to 16 hours (57,600 seconds) in Figure 6, resulting in the observed outliers. For the larger networks, i.e., the synthetic network of size 100,000 and the IBM datasets, AutoAudit exceeds the available memory. Hence, AutoAudit is omitted from Figure 7.

Figure 7 also shows that the GraphSAGE models have the smallest calculation time on the HI-Small dataset, and give great scalability on the LI-Large dataset as well. Training with additional node features takes substantially longer. This calculation speed is, however, only possible due to the deployment of GPU resources.

Calculation Time by Method and Network Size10 5methodflowscope10 4autoauditgargaml_undir10 3gargaml_dir10 210 110 010 1100 10000 100000Number of ObservationsTime (seconds)

Figure 6: Box plot of the run time on a logarithmic scale across network sizes. From left to right: FlowScope, AutoAudit, undirected GARG-AML and directed GARG-AML scores. The out-of-time results of AutoAudit on the dataset of size 10,000 are capped at 16 hours (57,600 seconds). AutoAudit is not included for the size-100,000 datasets as it runs out of memory on these datasets.

[p. 17]

Calculation Time by Method and Network (GraphSAGE: preprocessing + one fit + inference, cut-off 0.0)6000 FlowScoGARG-AML Undirectedpe 6,102GARG-AML DirectedGraphSAGE (topology)5000 GraphSAGE (+ attributes)4,293400030002,576+20001,1121000442 472 298+0 99 37 88HI-Small LI-LargeDatasetHardware: GARG-AML on CPU (up to 4 worker processes); GraphSAGE on one NVIDIA A100 GPU; FlowScope hardware not recorded.GraphSAGE inference is one full-graph pass on HI-Small but neighbour-sampled (batch 4096) on LI-Large, so that segment is notcomparable across the two datasets. '+': preprocessing is a lower bound (cold build time of a cached step is missing).Time (seconds)

Figure 7: Bar plot of the run time for the two IBM datasets. From left to right: FlowScope, undirected GARG-AML and directed GARG-AML scores. AutoAudit is not included as it runs out of memory on these datasets.

### 5.2.1 Synthetic Data


[pp. 17-18]

The results are presented according to the injected patterns in Table 10, with more detailed results given in B. The results indicate that, on average, the undirected GARG-AML scores show competitive performance. This performance is boosted when combining the GARG-AML scores with the tree-based learners. In comparison, the performance of the baselines, FlowScope and AutoAudit, is less stable.

A major concern for transaction monitoring is the high false positive rate. The precision shows that more than half of the alerts from FlowScope and AutoAudit were false positives. GARG-AML scores combined with tree-based learners result in around 70% of alerts being actual laundering accounts, except for the ‘existing mules’ pattern. The results for P@10 show that half of the top ranked nodes by the base undirected GARG-AML score are laundering money. This goes up to more than 9 out of 10 for the tree-based models. This points to a strong efficiency gain for financial institutions. No P@10 results are reported for FlowScope and AutoAudit. The definition of the scores for these two methods results in many ties, giving a ‘top 10’ that consists of more than ten observations. This would skew the comparison to the other methods.

Table 10: Performance comparison across patterns. For the two GARG-AML score rows, Precision and F1 use the rule score _>_ 0 _._ 5; AUC-ROC, AUC-PR and P@10 do not depend on a cut. Entries are the mean _±_ standard deviation over the synthetic datasets.

[p. 18]

|Method|Precision|F1-score|AUC-ROC|AUC-PR|P@10|
|---|---|---|---|---|---|
|_All laundering_||||||
|FlowScope|0_._417_±_0_._348 |0_._192_±_0_._182 |0_._547_±_0_._097 |0_._272_±_0_._290|–|
|AutoAudit|0_._219_±_0_._312 |0_._194_±_0_._268 |0_._374_±_0_._314 |0_._336_±_0_._334|–|
|GARG-AML Undirected|0_._536_±_0_._456|0_._464_±_0_._369|0_._721_±_0_._140|0_._435_±_0_._375|0_._529_±_0_._470|
|GARG-AML Directed|0_._316_±_0_._363|0_._148_±_0_._162|0_._598_±_0_._147|0_._280_±_0_._334|0_._295_±_0_._316|
|GARG-AML Undir. Tree|0_._935_±_0_._079 |0_._797_±_0_._129 |0_._892_±_0_._074 |0_._806_±_0_._129 |0_._977_±_0_._060|
|GARG-AML Undir. Boost|0_._901_±_0_._184|0_._805_±_0_._176|0_._887_±_0_._108|0_._789_±_0_._220|0_._942_±_0_._184|
|GARG-AML Dir. Tree|0_._894_±_0_._105|0_._721_±_0_._189|0_._877_±_0_._075|0_._732_±_0_._198|0_._926_±_0_._129|
|GARG-AML Dir. Boost|0_._866_±_0_._176|0_._734_±_0_._222|0_._863_±_0_._115|0_._718_±_0_._272|0_._902_±_0_._198|
|_Separate_||||||
|FlowScope|0_._174_±_0_._313|0_._165_±_0_._286|0_._584_±_0_._200|0_._196_±_0_._274|–|
|AutoAudit|0_._113_±_0_._171 |0_._158_±_0_._236 |0_._509_±_0_._442 |0_._453_±_0_._447|–|
|GARG-AML Undirected|0_._293_±_0_._276|0_._383_±_0_._334|0_._875_±_0_._115|0_._372_±_0_._377|0_._327_±_0_._351|
|GARG-AML Directed|0_._107_±_0_._187|0_._077_±_0_._089|0_._768_±_0_._117|0_._161_±_0_._146|0_._100_±_0_._101|
|GARG-AML Undir. Tree|0_._865_±_0_._207|0_._852_±_0_._213|0_._975_±_0_._046|0_._872_±_0_._177|0_._782_±_0_._188|
|GARG-AML Undir. Boost|0_._867_±_0_._222|0_._863_±_0_._219|0_._938_±_0_._193|0_._874_±_0_._216|0_._776_±_0_._228|
|GARG-AML Dir. Tree|0_._848_±_0_._242|0_._705_±_0_._218|0_._950_±_0_._066|0_._747_±_0_._199|0_._723_±_0_._206|
|GARG-AML Dir. Boost|0_._770_±_0_._284|0_._747_±_0_._261|0_._883_±_0_._226|0_._712_±_0_._298|0_._683_±_0_._261|
|_Existing mules_||||||
|FlowScope|0_._223_±_0_._203|0_._206_±_0_._196|0_._596_±_0_._114|0_._152_±_0_._152|–|
|AutoAudit|0_._062_±_0_._094|0_._087_±_0_._129|0_._318_±_0_._271|0_._071_±_0_._090|–|
|GARG-AML Undirected|0_._036_±_0_._084|0_._056_±_0_._126|0_._405_±_0_._188|0_._064_±_0_._096|0_._032_±_0_._101|
|GARG-AML Directed|0_._077_±_0_._137|0_._083_±_0_._142|0_._554_±_0_._146|0_._087_±_0_._129|0_._076_±_0_._127|
|GARG-AML Undir. Tree|0_._330_±_0_._373|0_._276_±_0_._315|0_._738_±_0_._185|0_._332_±_0_._288|0_._339_±_0_._282|
|GARG-AML Undir. Boost|0_._362_±_0_._378|0_._293_±_0_._316|0_._705_±_0_._215|0_._326_±_0_._284|0_._323_±_0_._276|
|GARG-AML Dir. Tree|0_._289_±_0_._368|0_._204_±_0_._260|0_._692_±_0_._180|0_._260_±_0_._236|0_._262_±_0_._237|
|GARG-AML Dir. Boost|0_._371_±_0_._375|0_._274_±_0_._270|0_._670_±_0_._199|0_._284_±_0_._277|0_._286_±_0_._273|
|_New mules_||||||
|FlowScope|0_._020_±_0_._051|0_._014_±_0_._030|0_._458_±_0_._066|0_._069_±_0_._098|–|
|AutoAudit|0_._043_±_0_._072|0_._059_±_0_._094|0_._241_±_0_._221|0_._056_±_0_._082|–|
|GARG-AML Undirected|0_._242_±_0_._231|0_._317_±_0_._286|0_._755_±_0_._182|0_._216_±_0_._210|0_._197_±_0_._247|
|GARG-AML Directed|0_._118_±_0_._164|0_._115_±_0_._141|0_._436_±_0_._170|0_._129_±_0_._169|0_._124_±_0_._156|
|GARG-AML Undir. Tree|0_._781_±_0_._292|0_._613_±_0_._263|0_._936_±_0_._064|0_._690_±_0_._197|0_._653_±_0_._199|
|GARG-AML Undir. Boost|0_._730_±_0_._273|0_._685_±_0_._275|0_._911_±_0_._128|0_._706_±_0_._264|0_._673_±_0_._240|
|GARG-AML Dir. Tree|0_._683_±_0_._323|0_._603_±_0_._294|0_._944_±_0_._069|0_._643_±_0_._245|0_._632_±_0_._239|
|GARG-AML Dir. Boost|0_._756_±_0_._285|0_._682_±_0_._295|0_._873_±_0_._214|0_._650_±_0_._317|0_._617_±_0_._285|

[p. 19]

Table 11: Results for the Friedman test for the eight different configurations ( _α_ = 0 _._ 05).

|Metric|Pattern|_χ_27|_p_|Reject_H_0|
|---|---|---|---|---|
|AUC-ROC|laundering|303.99|8.5e-62|True|
|AUC-ROC|separate|212.54|2.5e-42|True|
|AUC-ROC|new mules|345.30|1.2e-70|True|
|AUC-ROC|existing mules|150.18|3.7e-29|True|
|AUC-PR|laundering|303.86|9.1e-62|True|
|AUC-PR|separate|224.27|8.2e-45|True|
|AUC-PR|new mules|379.42|6.2e-78|True|
|AUC-PR|existing mules|179.33|2.7e-35|True|

These results are an average over widely different label distributions (see Table 4). The precision, F1-scores and the AUC-PR are highly sensitive to the label imbalance. Their baselines depend on the ratio of positive labels to the total number of labels, which changes with each dataset. The AUC-ROC baseline on the other hand is always equal to 0.5. This makes all but the AUC-ROC values in Table 10 hard to compare.

To mitigate this, we analyse the average rank of each model’s AUC-ROC and AUC-PR for a more robust evaluation. The results are shown in Figure 8 and Figure 9 for the AUC-ROC and AUC-PR, respectively. We find that the treebased learners score better than the other methods, even when applying a simple decision tree.

Table 11 illustrates that the Friedman test rejects the null hypothesis for each case, which indicates that significant differences between the ranks are present. The post hoc Nemenyi test indicates that the tree-based methods differ significantly from most other methods. The undirected scores on their own already obtain strong performance. For the existing mules patterns, however, it seems that the best performing models do not differ significantly from FlowScope.

One caveat to be noted is that the underlying hypotheses of the Friedman and Nemenyi statistical tests assume independence amongst the datasets. This is not strictly the case for the synthetic datasets, as they share generators and parameters. However, given the magnitude of the _p_ -values and the heterogeneity in the graph topology, the main conclusions remain valid.

### 5.2.2 IBM Data


Table 12 and Table 13 present the results for the smurfing patterns, i.e., gather-scatter and scatter-gather, and the full ‘Is Laundering’ label. The cut-offs for binary label definition presented here are 0.1, 0.5 and 0.9. The results for all patterns and cut-offs are provided in C. Missing results indicate that there were too few labels for the model to learn from. The tree-based and GraphSAGE models could not be trained on the scatter-gather label of the HI-Small dataset with cut-off 0.9 (Table 12). No positive gather-scatter and scatter-gather labels were present in the LI-Large dataset for cut-off 0.9 (Table 13). Likewise, the tree-based and GraphSAGE models could not be trained on the scatter-gather label of the LI-Large dataset with cut-off 0.5 (Table 13).

The precision and F1-scores are often (close) to zero. This is a result of the choice of the widely used threshold value of 0.5. Almost no observations get a score of 0.5 or higher, meaning that almost all observations are classified as normal. This highlights that careful tuning is needed for these thresholds, but also that comparing models on just a few thresholds can be problematic. Therefore, we decide to rely mostly on the threshold-independent metrics (AUC-ROC and AUC-PR) to form our conclusions.

In most cases, GraphSAGE performs best. The AUC-PR and P@1000 are substantially higher when the GraphSAGE model incorporates the node features. This might indicate that the node features on their own already carry a large laundering signal. We note that the comparison is not purely like-for-like. The GraphSAGE results on a given pattern are of the model trained on that specific pattern, while the GARG-AML scores are constructed purely on gather-scatter and scatter-gather patterns. GARG-AML can also not distinguish between the two, so any scatter-gather pattern picked up during the gather-scatter evaluation results in additional false positives. This puts GraphSAGE at a small advantage from the start.

Among the GARG-AML variants, the boosted extensions give the best AUC-ROC at cut-offs 0.1 and 0.5, whereas at cut-off 0.9 the base undirected score is best. GraphSAGE has the highest AUC-ROC overall in most cases. The undirected GARG-AML scores reach a moderate AUC-ROC for the general laundering cases (55–68% at cut-offs 0.1 and 0.5), which include more patterns than just smurfing, but remain well below GraphSAGE with attributes (96–97%).

[p. 20]

|ML score rows, Precision and F1 use the ruleresult excluding GraphSAGE is underlined.|ut-off 0.9AUC-ROCAUC-PRP@100050.00.0130.00081.70.0410.00163.30.0300.00069.50.0470.00080.00.0470.00054.10.0490.00266.30.0390.00185.10.0600.00197.07.0050.02550.00.0010.00083.40.0040.00065.70.0030.00049.60.0010.00057.60.0590.00250.00.0010.00058.30.0190.00099.40.1020.00099.90.6360.00650.00.0000.00086.00.0010.00047.20.0000.000––––––––––––––––––|
|---|---|
|G-Ae best|CF10.0000.0010.0010.0000.0000.0000.0030.0010.0050.0000.0000.0000.0000.0000.0000.0000.0000.0060.0000.0000.000––––––|
|GARold; th|Preci-sion0.0000.0000.0000.0000.0000.0000.0020.0010.0030.0000.0000.0000.0000.0000.0000.0000.0000.0030.0000.0000.000––––––|
|he twos in b|P@10000.0010.0010.0000.0050.0050.0070.0020.0040.0380.0000.0000.0000.0000.0020.0020.0040.0000.0080.0010.0000.0000.0020.0040.0040.0050.0010.007|
|. For tlumn i|.5AUC-PR0.0200.0370.0280.1510.1680.6480.0900.1163.7590.0030.0030.0030.0030.0900.2480.2900.0331.0790.0030.0020.0021.1290.19811.4160.4100.0662.904|
|atasetper co|Cut-off 0AUC-ROC50.066.253.061.374.655.170.081.596.150.053.548.849.663.957.757.189.395.350.041.331.557.172.064.373.386.488.7|
|HI-Small dbest result|Preci-sionF10.0000.0000.0000.0010.0000.0010.0000.0000.0220.0130.0000.0000.0000.0000.0000.0010.0030.0060.0000.0000.0000.0000.0000.0000.0000.0000.0000.0000.0000.0000.0060.0100.0000.0000.0030.0050.0000.0000.0000.0000.0000.0000.0000.0000.0060.0120.0000.0000.0100.0200.0000.0000.0000.000|
|or the. The|P@10000.0040.0160.0060.1630.1350.1750.1440.0400.7170.0000.0040.0010.0560.0540.0780.0760.0270.2470.0010.0010.0000.1220.0980.1010.0250.0210.153|
|-offs fn a cut|.1AUC-PR0.4450.5590.3983.9893.8404.6645.0501.44041.6980.0560.0820.0575.0064.9834.9364.9862.68849.2640.0360.0400.03032.40918.70424.8862.6680.81326.451|
|nd cutend o|ut-off 0AUC-ROC50.061.245.563.677.258.780.077.596.850.065.749.671.484.167.783.994.599.250.057.341.982.187.777.382.594.298.7|
|rns at dep|CF10.0000.0120.0090.0430.0240.0490.0410.0160.0780.0000.0020.0010.0000.0830.0330.0890.0070.1360.0000.0010.0000.3190.2940.3270.0710.0040.050|
|h pattedo no|Preci-sion0.0000.0060.0040.5150.4180.4840.5700.0080.0400.0000.0010.0010.0000.1970.2630.1730.0040.0730.0000.0010.0000.5380.4360.5000.0410.0020.025|
|Table 12: Performance comparison across grapscore_>_0_._5; AUC-ROC, AUC-PR and P@1000|Model_Is Laundering_FlowScopeGARG-AML UndirectedGARG-AML DirectedGARG-AML Undir. TreeGARG-AML Undir. BoostGARG-AML Dir. TreeGARG-AML Dir. BoostGraphSAGE (topology)GraphSAGE (+ attributes)_Gather-scatter_FlowScopeGARG-AML UndirectedGARG-AML DirectedGARG-AML Undir. TreeGARG-AML Undir. BoostGARG-AML Dir. TreeGARG-AML Dir. BoostGraphSAGE (topology)GraphSAGE (+ attributes)_Scatter-gather_FlowScopeGARG-AML UndirectedGARG-AML DirectedGARG-AML Undir. TreeGARG-AML Undir. BoostGARG-AML Dir. TreeGARG-AML Dir. BoostGraphSAGE (topology)GraphSAGE (+ attributes)|


---

[previous part](text-003.md) | [source overview](overview.md) | [next part](text-005.md)

[^original]: arXiv, "GARG-AML against Smurfing: A Scalable and Interpretable Graph-Based Framework for Anti-Money Laundering" (2025-04-06). https://arxiv.org/abs/2506.04292
