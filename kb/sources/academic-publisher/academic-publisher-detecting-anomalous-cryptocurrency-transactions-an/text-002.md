---
type: Source Text
title: 'Detecting anomalous cryptocurrency transactions: An AML/CFT application of machine learning-based forensics - part 2 of 4 (pp. 6-12)'
description: 'Verbatim extracted text, pp. 6-12: Detecting anomalous cryptocurrency transactions: An AML/CFT application of machine learning‑based forensics > Related work; Detecting anomalous cryptocurrency transactions: An AML/CFT application of machine learning‑based forensics > Anomaly detection approaches; Detecting anomalous cryptocurrency transactions: An AML/CFT application of machine learning‑based forensics > Experimenting with machine learning; and 1 more sections'
resource: https://link.springer.com/article/10.1007/s12525-023-00654-3
tags:
- academic_finding
- academic_paper
- global_academic
- network_graph
- typologies
status: stable
source_id: academic-publisher-detecting-anomalous-cryptocurrency-transactions-an
issuer: academic_publisher
issuer_name: Academic publisher / repository
jurisdictions:
- GLOBAL_ACADEMIC
tier: 3
instrument_type: academic_paper
normative_force: academic_finding
publication_date: '2023-07-26'
legal_status: unknown
part: 2
parts_total: 4
content_mode: full_text
generated:
  by: process:fincrime-kb-build
  at: '2026-11-22T04:42:14Z'
verified:
- by: process:kb-validate/verbatim-coverage
  at: '2026-11-22T04:42:14Z'
sources:
- id: original
  resource: https://link.springer.com/article/10.1007/s12525-023-00654-3
  title: 'Detecting anomalous cryptocurrency transactions: An AML/CFT application of machine learning-based forensics'
  author: org:academic_publisher
  last_modified: '2023-07-26T00:00:00Z'
---

# Detecting anomalous cryptocurrency transactions: An AML/CFT application of machine learning-based forensics

[previous part](text-001.md) | [source overview](overview.md) | [next part](text-003.md)

> Verbatim text extracted from the original (Academic publisher / repository, 2023-07-26), part 2 of 4, pp. 6-12. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **academic finding**.[^original]

## Detecting anomalous cryptocurrency transactions: An AML/CFT application of machine learning‑based forensics


### Related work


[p. 6]

|Work|Methodology|Algorithms|Results|
|---|---|---|---|
|Reid and Harrigan (2013)|Network analysis|Flow analysis + off-network infor-mation|Associate addresses with each otherand with external identifyinginformation|
|Fleder et al. (2015)|Network analysis|Flow analysis + web scraping|Link illicit activities to online identi-ties|
|Wu et al. (2021)|Network analysis|Safe Petri Net-based cluster analysis|Find suspected addresses|
|Al Jawaheri et al. (2020)|Network analysis|Wallet-closure analysis|Infer links between Bitcoin users andhidden services|
|Harrigan and Fretter (2016)|Network analysis|Address-clustering analysis|Identify super-clusters|
|Sun et al. (2021)|Graph analysis|Flow-based graphs analysis withcoupled tensorsl|Anomalous transactions detectionFAUC metric 0.94|
|Li et al. (2020)|Graph analysis|Theoretical flow-based multipartitegraphs analysis|Anomalous transactions detectionFAUC metric 0.96i|
|Yin et al. (2019)|Machine learning|Supervised learning-based (base-line)|Predict type of yet-unidentified entityF1score 0.796 (GradientBoosting)|
|Weber et al. (2019)|Machine learning + Graph analysis|Supervised learning-based (base-line + GCN)|Predict illicit transactions F1score0.796 (Random Forest)|
|Eddin et al. (2021)|Machine learning + Graph analysis|Supervised learning-based (base-line + triage model)|Reduce the number of false positivesby 80%|
|Oliveira et al. (2021)|Machine learning + Graph analysis|Supervised learning-based (base-line + GuiltyWalker)|Predict illicit transactions F1score0.85 (Random Forest)|
|Ours|Machine learning + Graph analysis|Supervised learning-based (base-line + GCN + GAT)|Predict illicit transactions F1score0.844 (GCN)|

account (or a group of) is a node, and a single transaction between two accounts is an edge. An edge’s weight is then defined as the aggregate transaction volume over a period of time. The latter is the predominant crypto-related forensic method seen in the “AML/CFT and blockchain forensics” section (Weber et al., 2018). Relatedly, Weber et al. (2019) benchmarked GCN against various supervised methods. In contrast, Eddin et al. (2021) extended their work to reduce false alerts through supervised learning methods in a context not related to the Internet of Money. They call the machine learning component the “triage model,” tasked to process the rule-generated alerts: the generated score enables alert suppression or prioritization. The GuiltyWalker (Oliveira et al., 2021) leverages random walks on a crypto-transaction graph to characterize distances to previous suspicious activity.

Table 1 shows a summary of the most influential research cited in this section. In this work, we aim to enhance the performance of classifier methods based on machine learning and graph analysis. To this end, we (i) adopt a novel scheme for transaction classification based on GAT; and (ii) resort to an updated implementation of GCN with respect to related works. As pointed out in the results section, this configuration improves state-of-the-art performance. Our methodology is backed up by an analysis of crypto-specific AML/CFT issues and anomaly detection approaches addressed in the next section. In particular, we consider the set of transactions

and their inherent characteristics, i.e. the fact that to spend cryptocurrencies, a user needs to have received them from previous transactions. These dependencies allow the creation of a graph whose structure can help identify illicit transactions. However, the need arises to identify the criteria that can inform a proper transactions classification—e.g., defining how it is possible to state that if a transaction is illicit, its neighbor transactions are also illicit, or if any graph-specific patterns represent suspicious activities. To confront these issues, it is essential to have a clear understanding of anomaly detection approaches in the RegTech field.

### Anomaly detection approaches


[pp. 6-7]

The process of anomaly/outlier detection involves processing data to detect behavior patterns that may indicate a change in system operations. The goal is to single out rare or suspicious events/items—i.e., those significantly different from the dataset (Kamišalić et al., 2021). While collective anomaly detection methods target groups of data points that differ from most of the data, point anomaly detection also considers single data points (Li et al., 2022; Shayegan et al., 2022). AML/CFT-regulated entities, especially in the financial industry, deploy RegTech solutions to screen their operations and detect anomalous activities in an automated

1 3

way. Their effort is based on the risk indicators provided by regulators usually in a rulebased format—i.e., templates of sequences of actions that suggest a suspicion in a way that is self-explainable and interpretable. Indeed, compliance decisions must be explainable and traceable for auditing. For this reason, the preliminary review of a flagged account relies on suspiciousness heuristics (e.g _._ , political exposure, geographic location, transaction type, users’ behavior) (Weber et al., 2018). This is the case of the mentioned FATF’s indicators, developed from analyzing 100 + case studies from 2017 to 2020 (FATF, 2020). Rule-based red flags can pertain to transaction patterns, such as “incoming transactions from many unrelated wallets in relatively small amounts (accumulation of funds) with subsequent transfer to another wallet or full exchange for fiat currency,” or to anonymity, such as “moving a VA that operates on a public, transparent blockchain, such as Bitcoin, to a centralized exchange and then immediately trading it for an AEC or privacy coin” (FATF, 2020). In particular, indicators related to anonymity include cases of enhanced obfuscation (e.g., AECs) and disintermediation (e.g., unhosted wallets).

In this context, a lot of time and resources are needed to investigate alerts generated by rule-matching processes and decide when to report a transaction as suspicious. An alert can be a true or a false positive, and arguably the simplicity of rule-based systems, despite guaranteeing interpretability, produces an estimate of around 95–98% false positives (Eddin et al., 2021).

[p. 7]

Indeed, classifying entities and discovering patterns in massive time-series transaction datasets that are dynamic, high dimensional, combinatorially complex, non-linear, often fragmented, inaccurate, or inconsistent is a challenging task. Moreover, the difficulty of automating the synthesis of information from multi-modal data streams thrusts the task onto human analysts. This adds to a vicious circle of a compliance approach that stimulates over-reporting due to the cost asymmetry between false positives and false negatives and overburdens law enforcement agencies (Weber et al., 2018). Hence, the automation of an increasing array of processes has been suggested (Oad et al., 2021).

Against this backdrop, in this section, we explore the anomaly detection methods that relate to our experiments. Hence, we focus on machine learning and graph analysis. We take an on-chain data analytic perspective, although we acknowledge the value of tools that target off-chain data, such as Natural Language Processing and sentiment analysis, that also leverage graph methods (Weber et al., 2018). Indeed, while cryptocurrency transactional data is often analyzed through a combination of on-chain and off-chain techniques, thus including information not recorded on the blockchain or recorded on a different blockchain, in this work, we focus on on-chain data.

#### Machine learning


Machine learning is a part of artificial intelligence that exploits data and algorithms to imitate human learning processes with gradual accuracy improvements. This helps us find solutions to problems in many fields, e.g., vision, speech recognition, robotics (Alpaydin, 2020). In the most diverse contexts, it provides tools that can learn and improve automatically leveraging the vast amount of data available in our age (Kamiˇsali´c et al., 2021). In the compliance domain, advances in these algorithms show great promise, and their deployment in AML/CFT RegTech solutions can improve the efficiency of these applications (Weber et al., 2019). For instance, they can mitigate the shortcomings of rules-based systems and infer patterns from historical data, increasing detection rates and limiting false positives (Lorenz, 2021). In other cases, a more proactive approach is deployed to map and predict illicit transactions (Koshy et al., 2014; Weber et al., 2019).

One of the main distinctions in machine learning is between unsupervised methods, where the model works on its own to discover patterns and information previously undetected, and supervised techniques, where labeled datasets are used to train algorithms. While applying both methods for anomaly detection is possible, most systems deploy unsupervised techniques due to a lack of relevant real-world labeled datasets. In the AML/CFT sphere, this scarcity mainly derives from difficulties in labeling real cases timely and comprehensively. Indeed, manual labels are costly in terms of time and effort, and the nature of the entities involved is complex and ever-evolving (Lorenz, 2021). Hence, analytic companies play a key role in labeling crypto transactions. In order to address the overall lack of data, various strategies have been proposed (Eddin et al., 2021): generate a fully synthetic dataset, simulate only unusual accounts within a real-world dataset, and localize rare events within a peer group. However, better validations of the systems were obtained using analyst feedback or real-labeled data. Parallelly, the dataset shortage has driven the deployment of active learning (i.e., few labels) (Lorenz, 2021).

##### Supervised baseline techniques


[pp. 7-8]

Supervised learning techniques are leveraged for their labeled training data. For instance, they are used to classify anomalies based on association rules to detect suspicious events (Luo, 2014). In the AML/CFT context, the label of each transaction could indicate whether it was identified as money laundering or not (Lorenz, 2021). Recent RegTech solutions deploy widespread supervised learning methods to perform anomaly detection (Yin et al., 2019):

1 3

- Decision tree —It is one of the base algorithms used in machine learning, with a name derived from a hierarchical model formed visually as a tree where nodes are decisions with specific criteria. The training data is subdivided into subsets following the tree branches. The node decision criteria are determined variables that can be defined as explanatory. The algorithm tries to apply the most significant feature to perform the best division among the training data. The best division can be measured by the information gain, mathematically derived from a decrease in entropy (Alpaydin, 2020).

- Random forests —It is an extension of Decision Trees in which an algorithm approaches the classification task by constructing a multitude of trees. Introduced by Breiman (2001), it is an ensemble method applied to sample random subsets of the training data for each Decision Tree. It aims to improve the predictive accuracy of a classifier by combining multiple individual weak learners, i.e., trees.

- Boosting algorithms —They are another ensemble method that fits weak learners’ sequences. A boosting algorithm tries to boost a Decision Tree by recursively selecting a subset of the training data. AdaBoost (Adaptive Boosting) assigns weights to the data samples based on the weak learners’ ability to predict the individual training sample. Thus, the sample weights are individually computed for each iteration, and the successive learner is applied to the new data subset (Yin et al., 2019).

- Logistic regression —It is a multiple regression suitable for binary classification, which assesses the relationship between the binary dependent variable (target) and a set of independent categorical or continuous variables (predictors) (Hilbe, 2009). It can be seen as measuring the probability of an event happening, where the probability consists of the ratio between the probability that an event will occur and the probability that it will not.

[p. 8]

- Support vector classification (SVC) —Given a set of data for training, each labeled with the class to which it belongs among the two possible classes, a training algorithm for Support Vector Machines builds a model that assigns the new data to one of the two classes. This generates a nonprobabilistic binary linear classifier. This model represents data as points in space, mapped in a way that a space separates data belonging to the two categories as ample as possible. New data is then mapped in the same space, and the prediction of the category to which they belong is made based on the side in which they fall (Alpaydin, 2020).

- K-nearest neighbors (k-NN) —It is a supervised learning algorithm used in pattern recognition for object classification based on the characteristics of the objects close to the considered one. The model represents data as

points in space, i.e., the feature space. Given a notion of distance between data objects, the input is the k nearest training data in the feature space. The underlying idea is that the more similar the instances, the more likely they belong to the same class (Alpaydin, 2020).

##### Graph analysis


In recent years, a portion of machine learning research focused on real-world datasets that come in graphs or networks—e.g., social networks, knowledge graphs—to generalize learning models to such structured datasets. Graph analytics is becoming increasingly important for AML/ CFT, because money laundering involves flow relationships between entities that create graph structures. Some approaches for supervised learning work with graph-structured data based on a variant of neural networks which operate directly on graphs, i.e., graph neural network (You et al., 2020; Kipf & Welling, 2016). Convolutional neural networks, for instance, offer an efficient architecture to extract significant statistical patterns in large-scale and high-dimensional datasets and can be generalized to graphs (Defferrard et al., 2016; Kipf & Welling, 2016). In this work, we use two specific graph-based neural networks, i.e., Graph Convolutional Networks (GCN) and Graph Attention Networks (GAT). These techniques are described in the next section.

### Experimenting with machine learning


As contextualized above, AML/CFT analytics benefit from deploying machine learning-based techniques for transaction classification. However, in new techniques, there is the need to balance interpretability and explainability with the reduction of false positives and over-reporting. Accordingly, this section outlines the experimental setup of our study and the relevant results. After describing the dataset, we consider the evaluation method and the implementation of the anomaly detection approaches. Subsequently, we compare the results of our experiments, where state-of-the-art machine learning techniques and graph-based neural networks are employed in an AML/CFT context.

It is worth noting that, in developing this work, we heed several assumptions. Although we have already discussed these throughout the text, we provide the following summary. In our paper, (i) the term Internet of Money refers to the entire set of cryptocurrency ecosystems; (ii) we do not offer a comprehensive review of crypto forensic techniques; (iii) we focus on on-chain data; and (iv) we perform inevitable simplifications when addressing explainability and interpretability of AI applications and relevant legal impacts.

1 3

#### Methodology


[p. 9]

Our experimentation is grounded on a seminal work by Weber et al. (2019). Most of the techniques deployed in the study correspond to the standard supervised models mentioned above—i.e., Decision Trees, Logistic Regression, k-NN, SVC, AdaBoost, Random Forests—used as benchmark methods for classification. However, the two graphbased models GCN and GAT deserve close attention in this context. This is for three main reasons: (i) these types of neural networks take into account the graph nature of our dataset; (ii) as the evaluation shows, our application of GCN outperforms benchmark approaches and improves the state of the art; and (iii) to the best of our knowledge, this is the first attempt to deploy the GAT model in the AML/CFT context.

##### Transaction graph analysis


Graphs represent a typical mathematical tool to model interactions among different entities: humans, elements of a biological system, computing nodes in a distributed system, and others (Pocher & Zichichi, 2022). In a blockchain, transactions are linked by nature since money spent in a transaction originates from previous transfers (Pocher & Zichichi, 2022). This allows the creation of a graph of transactions that can help the classification process. In fact, given a transaction _t_ , it is possible to collect all the connected transactions and recursively search for other ones up to a certain depth level. Given such a connected graph centered at _t_ , an inspection of the neighboring transactions and their classified value can aid the classification of _t_ . Each node of the graph (transaction) has thus a set of neighbors that will influence its classification. Moreover, each node has a set of features associated with the corresponding transaction (see below for the details of the dataset).

An example of this procedure is displayed in Fig. 1, where a connected component—i.e., a subgraph in which each pair of nodes is connected via a path—is obtained from an initial transaction (Fig. 1, top). In the figure, the _red_ nodes represent transactions labeled as illicit in the starting dataset, the _green_ ones licit transactions and the _grey_ ones are still unknown/unlabeled. To show the output of a machine learning classification problem, the bottom part of Fig. 1 shows the output of the process employing a specific classification algorithm, which in this case is Random Forest. In essence, the idea is that knowing the labels of certain transactions aids the classification of the remaining (unknown/unlabeled) ones. Hence, learning methods could pinpoint illicit transactions based on the graph topology and the features of the transactions.

Fig. 1 Connected graph of a considered transaction before and after classification

#### Dataset


[pp. 9-10]

In our work, we experimented with the publicly available Elliptic transactions dataset provided in the context of Weber et al. (2019). For details on the dataset, the reader can refer to the latter and to the description provided on Kaggle

1 3

together with the dataset.7 This dataset contains real Bitcoin transactions represented as a directed graph network, where transactions are nodes, and the directed edges between these transactions represent fund flows from the source address to the destination address. The dataset contains 203,769 transaction nodes connected by 234,355 edges. For each transaction, 167 features are available, of which the first 94 relate to the transaction itself and thus directly extracted from the blockchain—e.g., the number of inputs of a transaction or the number of outputs—while the other 73 features relate to the graph network itself and are extracted from the neighboring transactions of a node. The features do not have any associated descriptions—indeed, Weber et al. (2019) claim that they cannot describe these features due to intellectual property issues. Tests were carried out with transaction features (tx) and transaction features plus aggregated features (tx + agg). Such aggregated features are obtained by aggregating transaction information one-hop backward/forward from the center transaction node. This means obtaining the features of the nodes that share an edge with that transaction node.

Each transaction in the dataset is labeled as illicit, licit, or unknown: 4545 are labeled as illicit, 42,019 are labeled as licit, and the remaining 157205 are unknown. The transactions also contain temporal data. In particular, this is grouped into 49 distinct time steps, evenly spaced the interval of 2 weeks. Each time step contains a connected graph that includes all the transactions verified on the blockchain in the span of 3 h (Weber et al., 2019).

The dataset was pre-processed as follows: (i) the features were merged with the classes; (ii) class values were renamed to integer values; (iii) transaction identifiers were swapped for a sorted index; (iv) only the part of the dataset labeled licit or illicit was selected; and (v) all the edges between unknown transactions were removed. After the pre-processing, our cleaned dataset encompassed 46,564 transactions and 36,624 edges.

#### Graph convolutional network model architecture


[p. 10]

The objective of a GCN model is to learn a function of signals/features on a data set structured as a graph. The model takes as input (i) a graph with nodes and edges between nodes and (ii) a feature description for each node. The key idea is that each node receives and aggregates features from its neighbors to represent and compute its local state. The GCN then usually produces an output feature matrix at the node level (Kipf & Welling, 2016). The GCN model is used for transaction classification because it is a deep

7 Elliptic dataset: https:// www. kaggle. com/ datas ets/ ellip ticco/ ellip ticdata- set.

neural network that allows capturing the relation among the nodes and their neighborhoods. In other words, it creates a node embedding in a latent vector space that captures the characteristics of the node neighborhood in the graph. This information comes in the form of a look-up table mapping nodes to a vector of numbers. GCNs have been developed using the Keras framework, following the recommendations introduced in You et al. (2020).

The general structure of our graph convolution layer is made of three steps. First, the input node representations are processed using a Feed Forward Network to produce a message. Second, the messages of the neighbors of each node are aggregated using a permutation invariant pooling unsorted segment sum operation. Third, the node representations and aggregated messages are combined and processed to produce the new state of the node representations (node embeddings) via concatenation and Feed Forward Network processing.

Our network architecture consists of a sequential workflow of the model that we display in Table 2 and summarized as follows:

1. Apply pre-processing using Feed Forward Network to the node features to generate initial node representations;

2. Apply two graph convolutional layers, with skip connections, to the node representation to produce node embeddings;

3. Apply post-processing using Feed Forward Network to the node embeddings to generate the final node embeddings;

4. Feed the node embeddings in a Softmax layer to predict the node class.

#### Graph attention network model architecture


[pp. 10-11]

While the GCN model averages the node states from source nodes to the target node, the GAT model gives different importance to each node’s edge by using an attention mechanism to aggregate information from neighboring nodes

Table 2 GCN model architecture. Total parameters = 18,774, trainable parameters = 17,756, non-trainable = 1018

|Layer (type)|Output shape|Num.|parameters|
|---|---|---|---|
|Preprocess (Sequential)|(46,564, 32)|4564||
|Convolution 1 (GraphConvLayer)|multiple|5888||
|Convolution 2 (GraphConvLayer)|multiple|5888||
|Postprocess (Sequental)|(46,564, 32)|2368||
|Logits (Dense)|multiple|66||

1 3

(Veličković et al., 2017). In other words, instead of simply averaging/summing node states from source nodes to the target node, as we do in the GCN model, GAT, on the other hand, first applies normalized attention scores to each source node state and then sums (Veličković et al., 2017).

Our model is built using the Keras framework that, through a graph attention layer that computes pairwise attention scores, aggregates and applies the scores to the node’s neighbors. A multi-head attention layer concatenates multiple graph attention layer outputs. Our design choice is to use a single attention layer with multiple heads, enabling the network to jointly attend multiple positions (Liyuan Liu and Liu, 2021). The multi-head layer is then inserted into a general model that implements dense pre-processing/postprocessing layers with dropout regularization, as shown in Table 3. The training proved to be subjected to overfitting, and heavy regularization was necessary, which was achieved by dropout layers and using RMSprop optimizer with momentum (Philipp et al., 2017).

### Results


[p. 11]

For the discussion of the results, we firstly consider the illicit class as, due to the nature of the dataset (less labeled illicit transactions) and of the problem, its classification is more complex. To compare the results, we use the F1-score, a metric obtained from Precision and Recall. These metrics are usually defined for a binary classifier (as in this case) where some special instances need to be identified, e.g., positive cases to a particular test. Precision is the number of true positive (TP) predictions, i.e., how many of the positive predictions made are correct over the sum of TP and false positives (FP). In other words, precision says how many of the identified illicit transactions were illicit.

#### _Precision_ = _TP_ + _FP_ .


[pp. 11-12]

Recall measures how many positive cases the classifier correctly predicted over all the positive cases in the data, i.e.,

Table 3 GAT model architecture. Total parameters = 59,952, trainable parameters = 59,952, non-trainable = 0

|Layer (type)|Output shape|Num. parameters|
|---|---|---|
|Dense 9 (Dense)|Multiple|10,340|
|Dropout 6 (Dropout)|Multiple|0|
|Graph attention (MultiHead-GraphAttention)|Multiple|12,320|
|Dense 10 (Dense)|Multiple|36,630|
|Dropout 7 (Dropout)|Multiple|0|
|Dense 11 (Dense)|Multiple|662|

TP and false negatives (FN). In our context, for instance, it allows us to understand how many illicit transactions the classifier identified over the real considered set of illicit transactions.

The F1-score represents the harmonic mean of Recall and Precision and is thus calculated as:

We also use the Micro Average F1-score for evaluating the methods. It measures the F1-score of the aggregated contributions of all classes.

The final performance results are reported in Fig. 2 and Table 4. It is possible to observe how GCN outperforms other approaches. In particular, the GCN approach provides the best results in terms of recall, i.e., 0 _._ 790, and F1-score, i.e., 0 _._ 844. In terms of precision, it slightly deviates from the Decision Tree (0 _._ 986) and Random Forest (0 _._ 981) approaches

Fig. 2 Barplot aggregating F1-score, micro average F1-score, precision, and recall for all the approaches experimented

1 3

Table 4 Table showing the results for illicit transaction classification with the F1-score, Micro Average F1-score, precision, and recall metrics for all models


---

[previous part](text-001.md) | [source overview](overview.md) | [next part](text-003.md)

[^original]: Nadia Pocher, Mirko Zichichi, Fabio Merizzi, Muhammad Zohaib Shafiq, Stefano Ferretti, "Detecting anomalous cryptocurrency transactions: An AML/CFT application of machine learning-based forensics" (2023-07-26). https://link.springer.com/article/10.1007/s12525-023-00654-3
