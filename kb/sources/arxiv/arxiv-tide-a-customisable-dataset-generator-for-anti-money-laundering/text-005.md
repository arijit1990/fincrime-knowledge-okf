---
type: Source Text
title: 'Tide: A Customisable Dataset Generator for Anti-Money Laundering Research - part 5 of 5 (pp. 33-36)'
description: 'Verbatim extracted text, pp. 33-36: LI (0.10%) HI (0.19%)'
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
part: 5
parts_total: 5
content_mode: full_text
generated:
  by: process:fincrime-kb-build
  at: '2026-11-21T23:42:13Z'
verified:
- by: process:kb-validate/verbatim-coverage
  at: '2026-11-21T23:42:13Z'
sources:
- id: original
  resource: https://arxiv.org/abs/2603.01863
  title: 'Tide: A Customisable Dataset Generator for Anti-Money Laundering Research'
  author: org:arxiv
  last_modified: '2026-02-03T00:00:00Z'
---

# Tide: A Customisable Dataset Generator for Anti-Money Laundering Research

[previous part](text-004.md) | [source overview](overview.md)

> Verbatim text extracted from the original (arXiv, 2026-02-03), part 5 of 5, pp. 33-36. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **academic finding**.[^original]

## LI (0.10%) HI (0.19%)


[p. 33]

GIN 5.95 ± 1.27 3.07 ± 0.67 94.33 ± 2.62 69.86 ± 6.55 670.63 ± 62.91 90.66 ± 3.38 97.64 ± 1.05 GIN+EU 4.45 ± 3.09 2.31 ± 1.66 87.55 ± 7.82 39.43 ± 20.99 378.46 ± 201.54 80.91 ± 10.56 94.66 ± 3.99 PNA 69.90 ± 0.00 57.86 ± 0.00 88.26 ± 0.00 69.20 ± 0.00 664.30 ± 0.00 88.19 ± 0.00 98.44 ± 0.00 LightGBM+GFP 12.13 ± 7.18 6.64 ± 4.20 92.81 ± 8.64 21.45 ± 13.23 205.95 ± 127.04 90.12 ± 10.92 96.60 ± 5.38 XGBoost+GFP 10.19 ± 2.04 5.38 ± 1.15 99.31 ± 0.40 35.45 ± 2.59 340.28 ± 24.88 97.17 ± 0.20 99.77 ± 0.02 LightGBM 8.01 ± 2.21 4.20 ± 1.20 95.73 ± 3.50 78.05 ± 3.61 749.19 ± 34.64 92.80 ± 3.16 98.80 ± 1.75 XGBoost 4.22 ± 0.38 2.16 ± 0.20 97.04 ± 0.56 72.01 ± 0.50 691.22 ± 4.82 91.81 ± 0.22 99.42 ± 0.05

Table 21. Comparison of model performance on fraud detection. Homophily index: 0.0035. Class imbalance of 0,19%. Lift = PR-AUC / fraud_rate (times better than random). All metrics (F1, Precision, Recall) computed at Youden’s optimal threshold. Results reported as mean ± std over 5 runs.

Model F1 Precision Recall PR-AUC Lift Youden’s J ROC-AUC

[ref: 6.6]

GIN 9.83 ± 2.35 5.20 ± 1.29 91.65 ± 5.28 71.14 ± 8.70 378.40 ± 46.29 87.98 ± 6.14 96.71 ± 1.90 GIN+EU 4.88 ± 2.05 2.52 ± 1.09 86.59 ± 5.20 48.42 ± 17.05 257.56 ± 90.71 78.49 ± 7.27 93.61 ± 2.85 PNA 31.67 ± 13.94 20.20 ± 10.83 91.42 ± 1.34 75.63 ± 5.85 402.30 ± 31.14 90.31 ± 0.57 98.61 ± 0.22 LightGBM+GFP 20.98 ± 10.06 12.13 ± 6.46 97.35 ± 1.84 64.40 ± 24.36 342.56 ± 129.57 95.28 ± 2.21 99.11 ± 0.94 XGBoost+GFP 12.46 ± 0.65 6.65 ± 0.37 97.90 ± 0.28 32.20 ± 1.68 171.26 ± 8.93 95.06 ± 0.12 99.53 ± 0.03 LightGBM 28.59 ± 8.68 17.04 ± 5.72 96.69 ± 2.31 70.47 ± 27.91 374.85 ± 148.46 95.51 ± 2.97 99.45 ± 0.68 XGBoost 21.82 ± 1.78 12.30 ± 1.13 97.48 ± 0.17 85.12 ± 0.52 452.78 ± 2.76 96.03 ± 0.04 99.80 ± 0.01

6.6 Scalability Analysis

To evaluate the scalability of Tide’s graph generation, we conducted experiments across six different graph sizes,

ranging from 1,000 to 12,000 individuals. The results demonstrate good scalability, with all configurations successfully

generating the specified patterns. However, an analysis of memory usage reveals that while the system scales efficiently

from a complexity standpoint, absolute memory consumption becomes a practical bottleneck on resource-constrained

systems, which impacts the overall generation time.

[p. 34]

Table 22. Performance comparison of PNA and XGBoost models on the classification task on the HI dataset. Precision-Recall curves show Average Precision (AP) and F1 scores at optimal thresholds.

Table 23 presents the performance metrics for these experiments, including the peak memory usage for each

configuration.

Table 23. Aggregated generation performance across different graph scales on an M2 MacBook Air with 8 GB of RAM. Results are presented as mean ± standard deviation over 3 runs.

Configuration Transactions Total (𝑁) Wall-time Peak Memory [millions] [millions] [s] [MB]

Test-1k 0.372 ± 0.004 0.377 ± 0.004 2.3 ± 0.3 490 ± 30 Test-2k 0.948 ± 0.005 0.957 ± 0.005 5.2 ± 0.3 1090 ± 30 Test-3.5k 1.99 ± 0.01 2.00 ± 0.01 11.0 ± 0.9 2200 ± 50 Test-5k 3.28 ± 0.03 3.30 ± 0.03 18 ± 1 2700 ± 200 Test-8k 5.99 ± 0.02 6.03 ± 0.02 43 ± 3 3600 ± 40 Test-12k 10.17 ± 0.04 10.23 ± 0.04 120 ± 10 3700 ± 100

Figure 11 illustrates the performance characteristics of the generator across the different scales.

As shown in Table 24, all metrics for the generation time met their predefined success thresholds. We calculated a

scaling exponent of 𝛼= 1.164, which indicates a near-linear time complexity of 𝑂(𝑁1.164) with graph size 𝑁. This value

is well within our success criterion of 𝛼≤1.5. The coefficient of determination 𝑅2 = 0.976 shows that the system’s

performance remains predictable across different scales. This strong, near-linear relationship between graph size and

generation time is also supported by a Pearson correlation of 𝑟= 0.970 and a statistically significant 𝑝-value of 0.00137.

The analysis of peak memory usage reveals a scaling behaviour of 𝑂(𝑁0.627). This indicates that the memory required

per element decreases as the graph grows. Figure 11d shows the additional memory required per graph element,

confirming this trend.

The generator’s throughput, shown in Figure 11b, further illustrates the practical performance characteristics.

Throughput peaks for moderately-sized graphs at around 185 kElements/s before declining as the graph size grows.

[pp. 34-36]

This trend indicates that beyond a certain point, the overhead associated with memory pressure begins to outpace the

(a) Generation time vs total graph elements (𝑁). (b) Throughput in kElements/s vs total graph elements.

(c) Peak memory usage vs total graph elements (𝑁). (d) Additional memory per graph element.

Fig. 11. Performance analysis of the graph generator. (a) Log-log plot showing generation time versus total graph elements with near-linear scaling (exponent 𝛼= 1.164, 𝑅2 = 0.976). (b) Average throughput in kElements/s. (c) Peak memory usage scaling with sub-linear exponent of 0.627. (d) Memory efficiency showing additional memory required per element. Gray dotted lines in (a) and (c) represent O(𝑁) for reference.

Table 24. Statistical metrics from scalability analysis.

Metric Value Target

Pearson correlation (𝑟) 0.970 > 0.9 𝑝-value 0.00137 0.9

raw processing capability, which reinforces the conclusion that memory access, rather than computation, becomes the

primary bottleneck for larger-scale generation on resource-constrained systems.

The experiments were run on a machine with only 8 GB of RAM, where the operating system itself consumes around

5 GB. This leaves limited memory for the generation process. As the graph size increases, the system experiences

increased pressure on memory resources, likely leading to swapping and other overhead that inflates the wall-clock

time.

Despite the sub-linear memory scaling, the 𝑂(𝑁1.164) scaling in generation time is still affected by a memory

bottleneck in practice. As seen in Table 23, the absolute memory required for generation is significant, reaching

approximately 3.7 GB for a graph with over 10 million transactions.


---

[previous part](text-004.md) | [source overview](overview.md)

[^original]: arXiv, "Tide: A Customisable Dataset Generator for Anti-Money Laundering Research" (2026-02-03). https://arxiv.org/abs/2603.01863
