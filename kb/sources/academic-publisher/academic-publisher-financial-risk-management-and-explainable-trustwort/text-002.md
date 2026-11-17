---
type: Source Text
title: Financial Risk Management and Explainable, Trustworthy, Responsible AI - part 2 of 3 (pp. 6-12)
description: 'Verbatim extracted text, pp. 6-12: Financial Risk Management and Explainable, Trustworthy, Responsible AI > Technologies for Explainability and Transparency; Financial Risk Management and Explainable, Trustworthy, Responsible AI > Optimizing Trustworthy AI With Multiple Objectives; Financial Risk Management and Explainable, Trustworthy, Responsible AI > Open-Source Data Science; and 2 more sections'
resource: https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2022.779799/full
tags:
- academic_finding
- academic_paper
- global_academic
- ml_statistics
- model_development
status: stable
source_id: academic-publisher-financial-risk-management-and-explainable-trustwort
issuer: academic_publisher
issuer_name: Academic publisher / repository
jurisdictions:
- GLOBAL_ACADEMIC
tier: 3
instrument_type: academic_paper
normative_force: academic_finding
publication_date: '2022-02-28'
legal_status: unknown
part: 2
parts_total: 3
content_mode: full_text
generated:
  by: process:fincrime-kb-build
  at: '2026-11-17T17:21:51Z'
verified:
- by: process:kb-validate/verbatim-coverage
  at: '2026-11-17T17:21:51Z'
sources:
- id: original
  resource: https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2022.779799/full
  title: Financial Risk Management and Explainable, Trustworthy, Responsible AI
  author: org:academic_publisher
  last_modified: '2022-02-28T00:00:00Z'
---

# Financial Risk Management and Explainable, Trustworthy, Responsible AI

[previous part](text-001.md) | [source overview](overview.md) | [next part](text-003.md)

> Verbatim text extracted from the original (Academic publisher / repository, 2022-02-28), part 2 of 3, pp. 6-12. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **academic finding**.[^original]

## Financial Risk Management and Explainable, Trustworthy, Responsible AI


### Technologies for Explainability and Transparency


[pp. 6-7]

There are many technologies that support the development of transparent and explainable AI (XAI). XAI can help to explain the ways in which less transparent AI models (“black boxes”) function to a certain extent. One approach to achieve model explainability of course is to use an interpretable model by design. However, easy to interpret models are often (multi-)linear models. The problem with this approach is that the level of simplification with which a reality is represented in the model is often very high, which means that model accuracy is frequently less than optimal. This is simply because complex higher-order relationships in the underlying data are not seen by the model.

According to AIRS (Artificial Intelligence/Machine Learning Risk and Security Working Group) (2020), examples of newer and perhaps relatively more accurate and sophisticated types of interpretable AI/ML systems include scalable Bayesian rule lists, Explainable Boosting Machines (EBMs), monotonic Gradient Boosting Machines (GBMs), various Bayesian or constrained variants of traditional AI/ML systems or other novel interpretable-by-design systems.

There is also a variety of model agnostic post-hoc approaches to model explainability. Well-known representatives are LIME (Local Interpretable Model-agnostic Explanations) and SHAP (SHapley Additive exPlanations). The latter is a game theoretic approach to explain the output of any machine learning model. It revalues an entire dataset (“global”) or individual instances (“local”) after removing features (“Explaining by Removing”). A sound introduction to responsible machine learning workflow with a focus on interpretable models, post-hoc explanation, and discrimination testing can be found in Gill et al. (2020).

The publication of Deutsche Bundesbank (2020) helps to assess the benefit and downsides of XAI: “There is a fundamental conflict between the implementation of ML, with its potentially highly non-linear behavior, and the demand for comprehensible linear explanations. Explanations put forward by XAI seem to be appealing and convenient, but they only show a limited picture of model behavior, from which it is hard to draw general conclusions. Thus, ML combined with an XAI approach cannot make the black box fully transparent, merely less opaque. Nonetheless, it seems to be helpful to use XAI to provide more reliable risk metrics for control processes. We propose a balanced approach with XAI methods to be tailored to the use case and to the stakeholders’ demands. Further limitations of XAI methods should not be overlooked. Some methods require high computational power or only deliver minor insights into algorithms’ behavior. XAI methods should support established and used risk control processes and be able to demonstrate effectiveness. If not applying XAI methods, control processes should be in place to compensate for limited transparency.”

[p. 7]

The game-theoretic foundations, the supervisory attention on this particular approach (e.g., through publications by Bank of England) plus some other favorable features surely establish SHAP as one the standard approaches to understand and communicate feature importance at a global and local level. But it still is a compensation for missing transparency with ambitious control processes. The implementation of a SHAP approach itself establishes another model added to the workflow, with additional risks and costs. For example, it is known that strongly correlated features and other effects cause instabilities in SHAP evaluations, and SHAP can theoretically, at an additional effort, be “gamed” with the help of so-called scaffolding techniques, in the sense that the technique can be led to produce erroneous results. Also, as any other statistical model based on whichever type of co-incidental statistics, it does not explain causal relationships.

The downside of requiring time-consuming computations for SHAP revaluations, especially for large data sets, can be compensated by highly parallel processing, e.g., by HighPerformance Computing (HPC) environments using GPUs. According to the IFC-BIS publication “Computing platforms for big data analytics and artificial intelligence” (see Bruno et al., 2020) “Central banks’ experience shows that HPC platforms are primarily developed to ensure that computing resources are used in the most efficient way, so that analytical processes can be completed as rapidly as possible. [...] A processor core (or “core”) is a single processing unit. Today’s computers— or CPUs (central processing units)—have multiple processing units, with each of these cores able to focus on a different

task. Depending on the analytical or statistical problem at hand, clusters of GPUs (graphics processing units, which have a highly parallel structure and were initially designed for efficient image processing) might also be embedded in computers, for instance to support mass calculations.” In real life, the superb computing power of GPU clusters can be read off the fact that the market for high performance GPUs is influenced both by crypto miners and the high-performance gaming community even in the retail sector. Industry corporates have long since been exploring GPU computing to solve high computing power demand situations.

An example for using interpretable machine learning techniques is a use case developed by Munich Re Markets, published in Jaeger et al. (2021). It is a robust, fast, and interpretable machine learning approach to diversified portfolio construction. The approach is useful for overcoming a profoundly serious problem in investment management: backtest overfitting and replication crisis. This is due to the few decades of historical data available in capital markets. The approach helps in developing robust correlation-dependent investment strategies as well as financial products. HPC platforms can accelerate the training and post-hoc interpretation tasks associated with this approach from days to minutes.

The model training quality and its interpretability can be amplified by artificially creating future market data scenarios that have never been observed before but nevertheless carry the statistical footprints of financial market behavior. An example of such a procedure is given in Papenbrock et al. (2021) who use an alternative approach to GAN to produce correlated market data. The approach is based on an evolutionary search heuristic which can be parameterized in a way that allows the adoption of normal as well as extreme scenarios, both unobserved in the past.

The evolutionary approach is surprisingly analogous and thus perfectly suitable for HPC platforms as well. With the help of Matrix Evolutions, it is possible to synthetically generate correlation scenarios that seem real(istic) but have not yet been observed during the short actual history of financial markets.

Like in a wind tunnel for airplanes, millions of scenarios can be tested, reflecting all kinds of wind turbulences that could occur before the plane gets certified for take-off and air travel. The same can now be applied to test and explain investment strategies. The approach is called “Matrix Evolutions” and basically creates synthetic correlation matrices in a controlled way to amplify the XAI model to be able to construct more robust investment portfolios or perform advanced market risk management operations3 .

### Optimizing Trustworthy AI With Multiple Objectives


[pp. 7-8]

The previously presented application of Evolutionary Algorithms can be extended to optimize trustworthy AI. The idea is to formulate a number of objectives for AI/ML models that are supposed to be measurable characteristics of trustworthy AI models.

> 3This example shows that “The Future of Explainable AI rests upon Synthetic Data” (https://mostly.ai/2021/03/25/the-future-of-explainable-ai-restsupon-synthetic-data/).

For example, we measure the explainability and fairness of a model with certain metrics and define those as two objectives of an optimization program. We also measure model accuracy as well as prediction speed (efficiency) as two additional objectives4 . In the end, we have four objectives, which as a portfolio of objectives would typically contradict each other: for example, explainability and accuracy are often in conflict. This optimization program is quite complex as we are looking for a solution that finds the best compromise between several conflicting objectives. Mathematically, we need to search the efficient Pareto frontier in a multi-objective optimization problem. The real-world solution space is non-smooth and nonconvex, whence we need a smart search strategy to heuristically solve this challenging problem. Only a heuristic optimization like an Evolutionary Algorithm can support this—a task which luckily lends itself very well to parallel processing. Only an HPC environment can support the solution finding process of such a setting in a reasonable amount of time. It will create a large number of models and will systematically adapt model parameters to develop a high-quality efficient Pareto frontier.

In the next step, each point in that frontier is displayed as a single line in a parallel-coordinate plot5 . The coordinates correspond to the multiple objectives. The user can now decide which line to pick, which results in a model choice with certain levels in the objective functions. The user has the knowledge that this model choice exhibits specific levels of accuracy, explainability, efficiency, and fairness and that it is Pareto-optimal, meaning that it is the best compromise solution.

### Open-Source Data Science


[p. 8]

Data science offers a powerful toolbox to approach the implementation of trustworthy AI, building its strategic technological foundation. Data engineering is a key step and involves data gathering, data preparation and preprocessing, data analytics, feature engineering, machine learning and data visualization. Also, an architectural infrastructure is needed to build, manage, and monitor models through their entire lifecycle. When an algorithm is ready to be launched, MLOps is practiced between Data Scientists, DevOps, and Machine Learning engineers to transition the algorithm to production systems. Financial Data Science and MLOps can be very time consuming, with the risk of ineffective utilization of expensive expert resources. Therefore, it is particularly important to build an infrastructure and software stack that leverages those resources to the best possible efficiency.

Python is the most-used language in Data Science today. Libraries like NumPy, Scikit-Learn, and Pandas have changed how we think about accessibility in Data Science and Machine Learning.

> 4This is similar to the example in https://medium.com/turintech/optimising-aiwith-multiple-objectives-why-ai-efficiency-is-critical-for-scaling-ai-turintech6638f3d77dc6.

> 5See for example https://en.wikipedia.org/wiki/Parallel_coordinates or https:// plotly.com/python/parallel-coordinates-plot/.

However, while great for experimentation, PyData tools still lack the power that is necessary for enterprise-scale workloads. This leads to substantial refactoring to handle the size of modern problems, increasing cycle time, overhead, and time to insight. Quintessentially, to keep up with the forefront of development, an end-to-end accelerated infrastructure is needed that saves time and fully supports the capabilities of the Data Science and model management teams. Suites of open source software libraries exist that exploit parallelism in computation, node cluster scaling and high-bandwidth memory speed to power through big data processes and combine them with user-friendly Python interfaces6 .

Unsupervised learning like clustering, graph network analysis and visualization are especially useful tools as they require no expensive data labeling. They reveal the hidden relationships and links within the data sets and can visualize and interactively analyze the data, using the human superpower of visual analytics.

The increasing size of graphs to be visualized calls for tools outside the classical desktop visualization paradigm. To this end, parallel and distributed computing can help a pre-computation phase for open source software libraries multiscale visualization or graph drawing.

### Further Reading and Resources for This Chapter


[pp. 8-9]

The topics model risk management, trustworthy AI, AI governance, AI certification and AI incident management are currently being discussed in the industry and at regulators/supervisors. Some institutions are developing digital platforms that address these issues technologically7 .

The area of “algorithmic auditing” is quickly emerging and becoming an important aspect in the adoption of machine learning and AI products in enterprises. Companies are now incorporating formal ethics reviews, model validation exercises as well as internal and external algorithmic auditing to ensure that the adoption of AI is transparent and has gone through thorough vetting and formal validation processes. However, the area is new, and organizations are realizing that there is an implementation gap on how algorithmic auditing best practices can be adopted within an organization.

One important notion for the adoption of AI algorithms into operational decision processes is the concept of assurance. According to Batarseh et al. (2021), this is “a process that is applied at all stages of the AI engineering lifecycle ensuring that any intelligent system is producing outcomes that are valid, verified, data-driven, trustworthy and explainable to a layman, ethical in the context of its deployment, unbiased in its learning, and fair to its users.” The paper further delivers an overview of the AI assurance landscape, a method review and some recommendations and outlook on the field, highlighting the need for multi-disciplinary collaborations.

> 6Example are Spark, Dask, and RAPIDS.ai.

> 7See for example https://www.quantuniversity.com/publications.html and https:// www.bnh.ai/public-resources.

The Frankfurt Institute for Risk Management and Regulation is also engaged in several GAIA-X8 projects in the Finance & Insurance Data Space. They are related to addressing Trustworthy AI with technology, among other objectives. The project FAIC (Financial AI Cluster) is focused on the implementation of technologies to support trustworthy, explainable AI, as well as algorithmic auditing and sandboxes/experimentation facilities9 . FAIC activates an ecosystem and an entire tech industry around trust-creating technologies for AI model building, controlling, and auditing with innovative algorithms and HPC/AI computational infrastructure, e.g., for synthetic data generation, federated learning, and confidential computing. An industry with new services and applications for AI risk management and MLOps, supporting the implementation of trustworthy AI, will emerge, and platforms will be built for “Computational Trustworthy AI’ and “Computational AI Assurance”10 . The project’s foundations had been laid out in the European Union’s Horizon 2020 research and innovation program called FIN-TECH11 .

### A EUROPEAN USE CASE FOR EXPLAINABLE AI IN CREDIT RISK MANAGEMENT


[p. 9]

The purpose of this chapter is to walk the reader through the steps of a practical post-hoc SHAP-value-based XAI example that enhances the Credit Risk Management process. We demonstrate its capabilities, value adds, and effectiveness.

The example is based on the best rated use case of the EU Horizon2020 project FIN-TECH on Explainable AI. FIN-TECH is a FINancial supervision and TECHnology compliance training program, which draws on contributions of

- Fintechs and fintech hubs who have a detailed understanding of business models based on financial technologies;

- Regulators and supervisors who have a detailed understanding of the regulations and risks that concern financial technologies;

- Universities and research centers which have a detailed understanding of the risk management models that can be applied to financial technologies.

> 8Gaia-X represents the next generation of data infrastructure: an open, transparent, and secure digital ecosystem, where data and services can be made available, collated, and shared in an environment of trust (https://www.gaia-x.eu/).

> 9The blog article “The innovation potential of GAIA-X: Technologies for the trusted use of artificial intelligence in the finance sector” has more details.

> 10This development could be confirmed in the Global Webinar Series: “AI, Explainability, and Trustworthiness in Financial Services” presented by World Economic Forum (WEF), World Alliance of International Financial Centers (WAIFC), and NVIDIA.

https://waifc.finance/news/new-global-webinar-series-on-artificial-intelligencein-finance/.

> 11The project has received funding from the European Union’s Horizon 2020 research and innovation program under grant agreement no. 825215 (topic ICT35-2018, Type of action: CSA).This content reflects only the author’s view and the Commission is not responsible for any use that may be made of the information it contains (https://fintech-ho2020.eu/).

One key focus area was to analyze what inhibits AI from scaling across Europe’s financial services industry. Several supervisors and central banks had expressed their concern about black box AI models and the related impending inability to control them. The FIN-TECH project identified that this could be a potential inhibitor of industry growth, investment, and innovation in AI. It therefore took the opportunity to search for ways to overcome the explainability gap of AI models, and to produce standard use cases on explainable AI.

One FIN-TECH use case addresses a credit risk management example and uses SHAP values to identify the most important variables for decision making in a trained AI/ML model. This use case is inspired by a model published by Bracke et al. (2019) from the Bank of England. Above that, the approach further explores the similarity of explanatory data of the credit portfolio constituents using unsupervised learning approaches like clustering in graph analytics. The purpose is to not only be able to analyze the explanatory data either locally or globally, but also in groups or clusters, where every cluster consists of portfolio constituents with very similar explanatory data. In this way it is possible to get an in-depth understanding of the functional details of a trained model, to potentially debug it, and to control it, as we will demonstrate in this section.

We call the approach “SHAP clustering” (the concept is explained below and in the references), it was published as Bussmann et al. (2020) and was included in the FIN-TECH workshop series with supervisory authorities, central banks and the financial service companies and fintechs all across Europe. The project evaluation system identified that this AI/ML use case was among the most successful and popular ones. It is very straightforward to use and the workflow and combination of algorithms could be applied to a number of AI/ML applications. The target area of application of the proposed workflow and approach are risk management, assessment and scoring of credit portfolios in traditional banks, as well as in “fintech” platforms for p2p lending/crowdfunding, but also in constructing diversified investment portfolios. Figure 2 has an overview of the steps:

The specialty and added value of this approach is that the post-hoc explainability information is arranged into clusters of similarity (or user-defined groups), and that these data can be aggregated on each cluster/group level. Further, the data can be correlated with the input features and predictions. Lastly, all this information can be made available in huge interactive dashboards to slice, dice, and correlate all data as the user requires and finds useful. Below, we will discuss some use case scenarios.

Another added value is that each of the steps is GPUaccelerated, and the entire computation can be performed in GPU memory, avoiding costly copying steps between CPU and GPU. This makes the approach very efficient for large, enterprisescale data sets and workloads. Explainable AI needs to be quickly available for consumer fintech applications. Explanations about different factors may be needed within milliseconds, depending on the use cases12 . GPU-acceleration enables customer service representatives to explain automated financial decisions—like

12See this blog by Fiddler Labsi: https://blogs.nvidia.com/blog/2020/08/04/fiddlerlabs-ai-model-explainability.

[pp. 10-11]

FIGURE 2 | Description of the end-to-end workflow for an application to interactively analyse post-hoc explainable AI information. The dashboards have been produced with Plotly.

loan acceptances—and build trust with transparency about the process. In summary, the case presented is relevant for companies and enterprises that want to implement explainable AI at the enterprise level—for a XAI-effective Credit Risk Management process, for example.

The original data set used in the FIN-TECH project was rather small compared to the real-life data sets of some financial institutions. It was reasonable to test the model on a larger data set to understand the implications in production environments at a realistic scale. A team implemented the entire workflow in RAPIDS13 to be able to process large amounts of data within

a reasonable time. RAPIDS is a suite of open-source Python libraries that can speed up data science workflows using GPU acceleration. The team picked a Fannie Mae data set similar to a related blog on explaining and accelerating machine learning for loan delinquencies14 .

The presented machine-learning-based and visual procedure proposed in the approach is generally capable of processing the outcomes of any given (arbitrary) AI/ML model in a posthoc explainability approach. Thus, it provides more insight,

> 14The blogs can be viewed at: https://developer.nvidia.com/blog/author/ jochenpapenbrock/. The GPU-accelerated Python code is available at: https:// github.com/NVIDIA/fsi-samples/tree/main/credit_default_risk.

13http://www.rapids.ai/.

control, and transparency to any trained, potentially black box machine learning model. It utilizes a model-agnostic method aiming at identifying the decision-making criteria of an AI system in the form of variable importance (individual input variable contributions) with applications in credit risk assessment and management as well as in other (financial) areas. A key concept is the Shapley value decomposition of a model, a pay-off concept from cooperative game theory. So far, the Shapley value decomposition is the only XAI (explainable AI) approach rooted in an economic foundation. The approach offers a breakdown of the contributions of individual variables to the forecast outcome, typically some predicted probability. This means that after application of the method, every data point (e.g., a credit or loan customer in a portfolio) is not only represented by input features (the input of the machine learning model) but also by variable contributions to the prediction of the trained machine learning model. Practitioners usually analyse a local data point looking at the Shapley values or they aggregate Shapley values by averaging globally to learn something about the total model in terms of its feature importance.

[p. 11]

The explanation values are also used for visual mapping based on dimensionality reduction techniques [such as Principal Component Analysis, Multidimensional Scaling, t-SNE (t-Distributed Stochastic Neighbor Embedding)], or for representation learning like clustering and graph-analytics (such as community detection). This enables to analyse the data on an intermediate level between local and global. Those data-driven, learned representations reveal segmentations of data points (customers), where each of the segments (or clusters) represents a group with very similar decision making information (i.e., similar importance of similar features) whereas data points in other clusters exhibit comparatively different, but again homogeneous decision making structures. (Hierarchical) Clustering and especially graph theory and network analytics are very well-suited to study these kinds of complex systems based on the decision making data of an AI/ML model. These systems are characterized by emergent, self-organizing properties.

The approach treats the variable contribution outcome of a (black box) machine learning model as a complex system, and further analyses its properties by graph theory and cluster analysis. In this way, the user gets a better and deeper understanding of what exactly a black box machine learning algorithm has learned. The following phenomena inside the black box model can be analyzed and understood: trends, anomalies, hot spots, emergent effects, and tipping points. Since the methodology is model agnostic, it can be applied to any machine learning model. This also enables a comparison of several machine learning models trained on the same data. The complex system of decision-making mechanisms that belong to a series of machine learning models can be compared to each other. The proposed SHAP clustering approach enables a better understanding of model explanation information. Here are some use case scenarios:

- Groups or clusters of data points express “similar” decision making of the underlying, to-be-explained ML/AI model.

- These clusters summarize the mechanics of the model and represent types of decision making of the model, thereby effectively introducing a topology (i.e., a notion for proximity and distance) on the space of decision-making structures used by the non-linear model in view. Users get a better understanding of what the model has learned, to verify it, and to check plausibility.

- Data points at the intersect between clusters point to fuzzy decision making, which can be further investigated.

- A cluster with almost equal amounts of predictions for default and non-default could point to bugs or problems in the machine learning model. It could be checked whether or not the corresponding data points are actually indifferent, or whether the model exhibits buggy decision making on the corresponding data subset or “region” (in the sense of the above loosely mentioned intuitive notion of a topology) of the model.

[pp. 11-12]

- Customer segmentation: taking this technique as a means to segment portfolio data would render a novel approach to portfolio segmentation. Namely, the data points (credit customers and loans) could not only be clustered by their input variables (representing clusters of similarity of the customers) but also by their variable contributions in the decision making (representing the way in which they lend themselves to distinct types of decision making). This new clustering incorporates the “intelligence” of the machine learning model (the mapping of input variables to the default labels). Customers in the same cluster provoke similar decision making by the underlying, tobe-explained, machine learning model, e.g., about how and whether they default or not. In that sense, one could use a black-box model to learn a prediction on the portfolio, then use our XAI technique to find sub-portfolios where there is large similarity in decision making by the original machine learning model, and then train simpler (possibly even linear, or transparent-by-design) models on each such segment to maximize explainability.

The decisions of any reliable model must be informed decisions, and there must be a human-in-the-loop oversight that assigns accountability to a clearly defined function in the organization of the corporate that deploys the model. The SHAP clustering approach enables its user to understand why a particular decision was made. The “why” is not causal, but is expressed as a set of numeric contributions of input variables (which variables are responsible for the result). The user can look at a specific data point in the portfolio and see the corresponding input variables, the contributions of these variables to the prediction as well as the prediction itself. As one effect, a more humanbased, plausible explanation can arise to reconcile the machinebased decision with a human narrative “this makes sense.” The model can be better controlled, as it delivers feedback on how it reaches each singular decision, and thus all decisions both on global level (global variable importance) and on a local level (data points). The clustering step even delivers the variable contributions for the members of that specific cluster, i.e., there is an intermediate level between the global and the local, which corresponds to a partition of the input portfolio of customers.

The user could identify properties of this group of customers based on the input variables to understand how the decisionmaking works for this group of customers. All these analytics capabilities and tools plus the interactive visual exploration enable the user to better understand the outcome of an otherwise entirely black box model. Better understanding leads to more effective control.


---

[previous part](text-001.md) | [source overview](overview.md) | [next part](text-003.md)

[^original]: Sebastian G. Fritz-Morgenthal, Bernhard Hein, Jochen Papenbrock, "Financial Risk Management and Explainable, Trustworthy, Responsible AI" (2022-02-28). https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2022.779799/full
