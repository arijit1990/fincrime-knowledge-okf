---
type: Source Text
title: 'The effect of anti-money laundering policies: an empirical network analysis - part 3 of 5 (pp. 16-24)'
description: Verbatim extracted text, pp. 16-24
resource: https://link.springer.com/article/10.1140/epjds/s13688-022-00328-8
tags:
- academic_finding
- academic_paper
- effectiveness
- global_academic
- regulation
status: stable
source_id: academic-publisher-the-effect-of-anti-money-laundering-policies-an-emp
issuer: academic_publisher
issuer_name: Academic publisher / repository
jurisdictions:
- GLOBAL_ACADEMIC
tier: 3
instrument_type: academic_paper
normative_force: academic_finding
publication_date: '2022-03-18'
legal_status: unknown
part: 3
parts_total: 5
content_mode: full_text
generated:
  by: process:fincrime-kb-build
  at: '2026-11-17T02:21:50Z'
verified:
- by: process:kb-validate/verbatim-coverage
  at: '2026-11-17T02:21:50Z'
sources:
- id: original
  resource: https://link.springer.com/article/10.1140/epjds/s13688-022-00328-8
  title: 'The effect of anti-money laundering policies: an empirical network analysis'
  author: org:academic_publisher
  last_modified: '2022-03-18T00:00:00Z'
---

# The effect of anti-money laundering policies: an empirical network analysis

[previous part](text-002.md) | [source overview](overview.md) | [next part](text-004.md)

> Verbatim text extracted from the original (Academic publisher / repository, 2022-03-18), part 3 of 5, pp. 16-24. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **academic finding**.[^original]

[pp. 16-17] [ref: 4.4]

Figure 2 shows the development of a single cluster with known money laundering ac- tivities over time, starting from 2005 (left top) until 2019 (right bottom), biannually. Each node represents either a natural person, male or female (blue or pink) or a legal person (yellow, emerging in 2009). The orange and red nodes that appear in 2017 and 2019 iden-

Figure 3 Number of clusters detected per year per crime type. This ﬁgure shows a line chart that shows the number of money-laundering, criminal and not-criminal clusters are detected in each annual snapshot of the entire network

tify police actions and court rulings, respectively. The size of each node is related to its degree centrality. The ties between the nodes are based on family relations (green), pro- fessional ties (yellow) and a shared bank account that emerged in 2013 (orange).

4.4 Summary statistics We merge the ﬁve retrieved random samples into a single dataset. To avoid having a biased dataset that emphasizes data collected for nodes and clusters that have been retrieved in multiple samples, the data is cleaned of duplicates by removing any duplicated cluster with associated nodes that contains a repeated individual. In the case of duplicate clusters with diﬀerent levels of retrieved criminal activity, the money laundering cluster is retained. When there is no money laundering record in the cluster, the case with most levels of crime is kept. This process is chosen to maximize the amount of crime in the dataset because criminal data is least represented.

The available data covers the years 2005 to 2019, for which the number of clusters and their criminal activity is displayed in Fig. 3. The number of money laundering related clus- ters ranges between 7 and 17, criminal activity without money laundering ranges from 39 to 42 clusters, and those with no form of crime range between 87 and 124 clusters.

The summary statistics in Table 2 are recorded at the cluster level6 and in Table 3 at individual level.7

5 Results Our results aim to provide insight into the extent of collaboration and competition be- tween criminals and money launderers as observed in their respective network structures before and after AML-IV was announced. Since intensiﬁed anti-money laundering poli- cies should make money laundering more complex, we expect those who provide such services professionally will have to specialize and collaborate with each other. The crimi- nal networks that use professional money laundering services will collaborate with some

6To avoid confusion, the deﬁnition of a cluster in this paper requires a minimal size of 5 connected nodes as shown in the “Node Count” in Table 2. The minimum people and company count is 0 since there are clusters with no people or no companies involved.

[pp. 17-18]

7The betweenness and closeness centralities are normalized to avoid combining very large and very small numbers in the regression equations that results rounding the coeﬃcients to a value 0.0000.

Table 2 Cluster-level summary statistics

Statistic N Mean St. dev. Min Max

Node Count 29,733 26.491 26.596 5 145 People Count 29,733 12.552 10.953 0 56 Company Count 29,733 13.939 18.882 0 91 Cluster Diameter 29,733 4.500 1.806 2 10 Cluster Density 29,733 0.305 0.263 0.025 1.900

Criminal Diversity 9810 0.313 0.252 0.000 0.720 Criminal Dis-proportionality 9810 0.493 0.130 0.238 0.645 Nationality Diversity 29,733 0.359 0.166 0.000 0.720 Nationality Dis-proportionality 29,733 0.208 0.138 0.000 0.464

Degree Assortativity 29,733 –0.479 0.310 –1.000 0.499 Crime Assortativity 4472 –0.098 0.215 –1.000 0.466 Nationality Assortativity 26,637 –0.119 0.349 –1.000 0.783

Table 3 Individual-level summary statistics

Statistic N Mean St. dev. Min Max

Degree Centrality 29,733 3.697 5.552 1 134 Betweenness Centrality 29,733 0.002 0.016 0.000 1.000 Closeness Centrality 29,733 0.455 0.264 0.001 1.000 Transitivity 29,733 0.043 0.164 0.000 1.000 Constraint 29,733 0.809 0.287 0.022 1.382

criminal clusters to maximize access to money laundering professionals and at the same time compete with other criminal clusters to protect their access to these services.

In all models, the R2 and adjusted R2 metrics are fairly low, but given the invisible nature of covert criminal activities, this is expected and does not invalidate the model’s goodness- of-ﬁt.8

[pp. 18-19] [ref: 5.1]

5.1 Cluster size Cluster size is represented by the number of nodes that form the cluster, i.e. people and companies. This indicates the potential magnitude of the cluster or the amount of inﬂu- ence it could have on a population. Additionally, the cluster size is assessed by its diame- ter, which is the shortest distance between the two nodes that are furthest away from each other.

Although there is volatility in money laundering related clusters due to fewer observa- tions, as visually depicted in Fig. 4, it seems that the size of all clusters (all lines), while dif- ferent, follow a similar growing trend. The number of people involved in money launder- ing clusters (the dotted line) suddenly grows after 2014, while corporate presence dropped steeply during the ﬁnancial crisis but is also growing steadily after 2015, in contrast with the criminal clusters without money laundering activities. The average diameter of all types of clusters slowly increases over time and remains higher for the criminal clusters.

8According to Shalizi [87], either a small variance in the dependent variable or a larger error-term causes the R2 to approach near zero. This potentially precludes the use of this measure for the goodness-of-ﬁt, as demonstrated in a theoretical proof where a low R2 is reported while the model predictions are 100% accurate [87]. Our data has a large representation of non- criminal clusters; the money laundering and criminal clusters are relatively sparse. This makes the dependent variable’s variance and the total sum-of-squares small when non-criminal clusters have a relatively small variance. It makes the model as a whole insensitive to variance within the criminal clusters, thus tailoring the goodness-of-ﬁt assumption merely towards non-crime clusters. 4Our goal is not to explain the cluster- and node-based measures but to analyze changes after AML intensiﬁcations. The F-value shows the signiﬁcance of all models, indicating that our models have predictive capacity.

Figure 4 Cluster measures of size. This ﬁgure shows 4 line charts that show the development for each cluster type on average cluster size, average cluster size (people), average cluster size (companies) and the average cluster diameter

Table 4 Results of random eﬀects regressions on cluster size

Dependent variable

Node count People count Company count Diameter

Laundry 3.911 2.731∗∗ 0.393 1.086∗∗∗

(2.547) (1.107) (2.025) (0.270) No Laundry 2.081 2.473∗∗∗ –0.215 1.051∗∗∗

[p. 19]

(1.680) (0.729) (1.486) (0.177) After AML4 2.776∗∗∗ 2.062∗∗∗ 0.610∗∗ 0.501∗∗∗

(0.357) (0.214) (0.272) (0.051) Laundry: After AML4 5.555∗∗∗ 1.458∗∗ 4.607∗∗∗ –0.038 (1.044) (0.614) (0.781) (0.149) No Laundry: After AML4 4.087∗∗∗ 2.742∗∗∗ 1.914∗∗∗ 0.270∗∗∗

(0.626) (0.371) (0.521) (0.089) Constant 8.153∗∗∗ 4.573∗∗∗ 4.496∗∗∗ 2.723∗∗∗

(0.746) (0.335) (0.617) (0.080)

Observations 2411 2320 1850 2411 R2 0.112 0.136 0.042 0.121 Adjusted R2 0.110 0.134 0.039 0.120 F Statistic 59.878∗∗∗ 70.139∗∗∗ 15.590∗∗∗ 62.212∗∗∗

(df = 5;2405) (df = 5;2314) (df = 5;1844) (df = 5;2405)

Note: ∗p < 0.1; ∗∗p < 0.05; ∗∗∗p < 0.01.

[pp. 19-20] [ref: 5.2]

The models related to cluster size, presented in Table 4, statistically conﬁrm that both types of criminal clusters have signiﬁcantly more people involved (β1 = 2.731, σ¯l = 1.107, p < 0.05 for money laundering and β2 = 2.473, σ¯c = 0.729, p < 0.01 for criminal clusters without money laundering) compared to non-criminal clusters. After 2015, when AML- IV was announced, all clusters grew in size (β3 = 2.776, σ¯a = 0.357, p < 0.01), but money laundering (δ1 = 5.555, σ ¯la = 1.044, p < 0.01) and criminal (δ2 = 4.087, σ ¯ca = 0.626, p < 0.01)

clusters grew even stronger. Especially the corporate involvement in the money laundering clusters increased (δ1 = 4.607, σ ¯la = 0.781, p < 0.01).

Figure 4 shows a corporate decline in money laundering clusters that started during the ﬁnancial crisis but is recovering to its previous level since AML-IV was announced (δ1 = 4.607, σ ¯la = 0.781, p < 0.01). The statistics demonstrate a signiﬁcant impact of AML-IV on the diameter of clusters for both types of criminal activity (β3 = 0.501, σ¯a = 0.052, p < 0.01), in which criminal clusters are aﬀected signiﬁcantly (δ1 = 0.270, σ ¯ca = 0.089, p < 0.01).

5.2 Representation Cluster representation is measured in terms of the representation of crime and national- ities. Figure 5 shows the development of the average true diversity [88] and the average (dis)proportionality of representation [89] within each cluster for both criminal activities and the presence of nationalities. In the ﬁrst two visualizations, criminal clusters without money laundering activities are the control group instead of clusters with no crime.

Money laundering clusters are more diverse concerning the prevalent types of crime, i.e. the number of diﬀerent crime types is higher and less disproportionally represented). For the representation of diversity in involved countries (measured by nationality), money laundering clusters are more diverse although criminal clusters that have no detected money laundering activities are catching up. Representation was less proportional for money laundering clusters but a decrease in dis-proportionality around the announce- ment of AML-IV is observable for criminal networks with and without money laundering activities.

[pp. 20-21]

The models shown in Table 5 demonstrate the signiﬁcance of the overall larger crime diversity of money laundering clusters (β1 = 0.228, σ¯l = 0.060, p < 0.01) and their more pro-

Figure 5 Cluster measures of representation. This ﬁgure shows 4 line charts that show the development for each cluster type on average criminal diversity, average criminal proportionality, average country diversity and average country proportionality

Table 5 Results of random eﬀects regressions on cluster representation

Dependent variable

Crime based Nationality based

True diversity Dis-proportionality True diversity Dis-proportionality

Laundry 0.228∗∗∗ –0.120∗∗∗ 0.035 0.054∗∗

(0.060) (0.030) (0.034) (0.026) No Laundry –0.032 –0.011 (0.022) (0.017) After AML4 0.037∗∗∗ –0.018∗∗∗ 0.038∗∗∗ 0.002 (0.009) (0.004) (0.006) (0.006) Laundry: After AML4 –0.027 0.016∗ 0.045∗∗∗ –0.028 (0.019) (0.010) (0.017) (0.018) No Laundry: After AML4 0.088∗∗∗ 0.019∗

(0.010) (0.011) Constant 0.209∗∗∗ 0.546∗∗∗ 0.315∗∗∗ 0.183∗∗∗

(0.031) (0.015) (0.010) (0.008)

Observations 610 610 2320 2411 R2 0.076 0.264 0.175 0.027 Adjusted R2 0.071 0.260 0.173 0.025 F Statistic 16.534∗∗∗ 72.473∗∗∗ 98.281∗∗∗ 13.037∗∗∗

(df = 3; 606) (df = 3; 606) (df = 5; 2314) (df = 5; 2405)

Note: ∗p < 0.1; ∗∗p < 0.05; ∗∗∗p < 0.01.

[p. 21] [ref: 5.3]

portional representation of these countries (β1 = –0.120, σ¯l = 0.030, p < 0.01). Although crime diversity continues to increase for all criminal clusters after AML-IV is announced (β3 = 0.037, σ¯l = 0.009, p < 0.01), the money laundering related clusters do not show a signiﬁcant diﬀerence (δ1 = –0.027, σ ¯la = 0.019, p ≥0.1). While a similar trend continues for criminal proportionality, after the AML-IV announcement, money laundering clusters have been aﬀected by a decreasing proportionality of criminal representation (δ1 = 0.016, σ ¯la = 0.010, p < 0.1). The involvement of diﬀerent nationalities increased for all clusters after the announcement of AML-IV (β3 = 0.038, σ¯a = 0.006, p < 0.01), and even more for both money laundering (δ1 = 0.045, σ ¯la = 0.017, p < 0.01) and criminal clusters without money laundering (δ2 = 0.088, σ ¯ca = 0.010, p < 0.01). A signiﬁcant lower proportionality for money laundering clusters is observed (β1 = 0.054, σ¯l = 0.026, p < 0.05), but only for criminal clusters a somewhat signiﬁcant decrease of the proportionality (increase of dis- proportionality) for national representation is observed (δ2 = 0.019, σ ¯ca = 0.011, p < 0.1).

5.3 Cluster connections Analyzing the connections within clusters is based on the measures of cluster density, i.e. the number of connections in relation to the maximum possible connections [67] and av- erage assortativity, i.e. the extent to which nodes with certain properties connect to other nodes with similar characteristics [78]. Both measures indicate collaboration within the cluster, namely the extent of and preferences towards collaboration, respectively. When new nodes are allocated to clusters and they are not connected to other nodes within that cluster, the cluster density decreases.

As shown in Fig. 6, both money laundering and criminal clusters show a similar trend in decreasing density, which seems much less for non-criminal clusters. While highly con- nected individuals would typically connect with less connected individuals (which is in- dicated with a negative value), this correlation diminishes over time. After AML-IV was announced, money laundering related clusters connected more to the same nationality.

[p. 22]

Figure 6 Cluster measures of connectivity. This ﬁgure shows 4 line charts that show the development for each cluster type on average cluster density, average degree assortativity, average crime assortativity and average country assoertativity

Table 6 Results of random eﬀect regressions on cluster connections

Dependent variable

Density Assortativity measures

Degree Crime type Nationality

Laundry –0.005 0.274∗∗∗ –0.294∗ 0.079 (0.055) (0.063) (0.176) (0.076) No Laundry 0.035 0.254∗∗∗ 0.179∗∗∗

(0.036) (0.042) (0.053) After AML4 –0.049∗∗∗ 0.089∗∗∗ 0.049 0.035∗∗∗

(0.009) (0.010) (0.032) (0.010) Laundry: After AML4 –0.076∗∗∗ –0.056∗ 0.194 0.010 (0.025) (0.029) (0.188) (0.027) No Laundry: After AML4 –0.154∗∗∗ 0.026 –0.016 (0.015) (0.018) (0.018) Constant 0.474∗∗∗ –0.735∗∗∗ –0.201∗∗∗ –0.300∗∗∗

(0.016) (0.019) (0.052) (0.024)

Observations 2411 2411 210 1955 R2 0.165 0.189 0.059 0.037 Adjusted R2 0.163 0.187 0.045 0.034 F Statistic 94.876∗∗∗ 109.422∗∗∗ 4.229∗∗∗ 14.326∗∗∗

(df = 5; 2405) (df = 5; 2405) (df = 3; 206) (df = 5; 1949)

Note: ∗p < 0.1; ∗∗p < 0.05; ∗∗∗p < 0.01.

Due to the small number of individual crime observations before 2014, assortativity mea- sures for crime could not be calculated.

[pp. 22-24] [ref: 5.4]

The statistical results in Table 6 show that the announcement of AML-IV is corre- lated with a signiﬁcant decrease in cluster density of both money laundering related (δ1 =

Figure 7 Cluster average of individual centrality measures. This ﬁgure shows 6 line charts that show the development for individual nodes within a cluster type on average degree centrality, average degree centrality and average closeness centrality, separated into people and companies

–0.076, σ ¯la = 0.025, p < 0.01) and non-money laundering related (δ2 = –0.154, σ ¯ca = 0.015, p < 0.01) criminal clusters.

Although the data on crime assortativity is limited, compared to criminal clusters, peo- ple in money laundering related clusters seem to have somewhat weaker connections (β1 = –0.294, σ¯l = 0.176, p < 0.1) to other people with a potential criminal history.

5.4 Individual centrality Changing from a cluster-level analysis to a node-level analysis, individual centrality mea- sures provide insights into how clusters are connected. The degree centrality provides information about the average number of connections per entity. The shape of the cluster is better deﬁned by the betweenness centrality in which average higher values indicate a larger periphery and a stronger central group. The distance between the periphery and the central players can be indicated by the closeness centrality.

Visually analyzing the centrality of nodes within the network shows (see Fig. 7) that money laundering related individuals have decreased their human connections since AML-IV was announced but increased their corporate degree. After the announcement

Table 7 Results of random eﬀects regressions on individual centrality and position for people and companies combined

Dependent variable

Centrality measures Transitivity Constraint

Degree Betweenness Closeness

Laundry 1.934∗ 0.0002 –0.235∗∗∗ 0.015 –0.197∗∗∗

(1.072) (0.003) (0.052) (0.031) (0.057) No Laundry 0.541∗∗∗ 0.00004 0.012 0.002 –0.039∗∗∗

(0.191) (0.0005) (0.009) (0.005) (0.010) After AML4 0.721∗∗∗ 0.003∗∗∗ –0.103∗∗∗ 0.001 –0.015∗∗∗

[p. 24]

(0.029) (0.0002) (0.001) (0.001) (0.001) Laundry: After AML4 1.038∗∗∗ 0.004∗∗∗ 0.046∗∗∗ –0.029∗∗ –0.085∗∗∗

(0.304) (0.002) (0.012) (0.012) (0.013) No Laundry: After AML4 0.270∗∗∗ 0.0002 –0.009∗∗∗ –0.001 0.001 (0.049) (0.0003) (0.002) (0.002) (0.002) Constant 2.586∗∗∗ 0.0003 0.487∗∗∗ 0.032∗∗∗ 0.864∗∗∗

(0.079) (0.0002) (0.004) (0.002) (0.004)

Observations 29,733 29,733 29,733 29,733 29,733 R2 0.021 0.011 0.251 0.00001 0.224 Adjusted R2 0.021 0.011 0.251 –0.0002 0.224 F Statistic (df = 5; 29727) 117.640∗∗∗ 65.900∗∗∗ 1994.087∗∗∗ –7.179 1663.129∗∗∗

Note: ∗p < 0.1; ∗∗p < 0.05; ∗∗∗p < 0.01.

of AML-IV, they continuously increase their brokerage position given the observed be- tweenness centralities, especially the corporate forms. In general, the distance between the core and periphery of all clusters (as indicated by the closeness centrality) increased and after 2015 decreased again for both people and corporate centralities.


---

[previous part](text-002.md) | [source overview](overview.md) | [next part](text-004.md)

[^original]: Peter Gerbrands, Brigitte Unger, Michael Getzner, Joras Ferwerda, "The effect of anti-money laundering policies: an empirical network analysis" (2022-03-18). https://link.springer.com/article/10.1140/epjds/s13688-022-00328-8
