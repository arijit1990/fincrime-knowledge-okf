---
type: Source Text
title: 'Graph-Based LSTM for Anti-money Laundering: Experimenting Temporal Graph Convolutional Network with Bitcoin Data - part 1 of 2 (pp. 1-11)'
description: 'Verbatim extracted text, pp. 1-11: Graph-Based LSTM for Anti-money Laundering: Experimenting Temporal Graph Convolutional Network with Bitcoin Data > 1 Introduction; Graph-Based LSTM for Anti-money Laundering: Experimenting Temporal Graph Convolutional Network with Bitcoin Data > 2 Overview of Related Work; Graph-Based LSTM for Anti-money Laundering: Experimenting Temporal Graph Convolutional Network with Bitcoin Data > 3 Model Uncertainty: MC-Dropout Versus MC-AA; and 2 more sections'
resource: https://link.springer.com/article/10.1007/s11063-022-10904-8
tags:
- academic_finding
- academic_paper
- datasets_benchmarks
- global_academic
- network_graph
- virtual_assets
status: stable
source_id: academic-publisher-graph-based-lstm-for-anti-money-laundering-experime
issuer: academic_publisher
issuer_name: Academic publisher / repository
jurisdictions:
- GLOBAL_ACADEMIC
tier: 3
instrument_type: academic_paper
normative_force: academic_finding
publication_date: '2022-06-15'
legal_status: unknown
part: 1
parts_total: 2
content_mode: full_text
generated:
  by: process:fincrime-kb-build
  at: '2026-11-22T14:32:20Z'
verified:
- by: process:kb-validate/verbatim-coverage
  at: '2026-11-22T14:32:20Z'
sources:
- id: original
  resource: https://link.springer.com/article/10.1007/s11063-022-10904-8
  title: 'Graph-Based LSTM for Anti-money Laundering: Experimenting Temporal Graph Convolutional Network with Bitcoin Data'
  author: org:academic_publisher
  last_modified: '2022-06-15T00:00:00Z'
---

# Graph-Based LSTM for Anti-money Laundering: Experimenting Temporal Graph Convolutional Network with Bitcoin Data

[source overview](overview.md) | [next part](text-002.md)

> Verbatim text extracted from the original (Academic publisher / repository, 2022-06-15), part 1 of 2, pp. 1-11. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **academic finding**.[^original]

[p. 1]

Neural Processing Letters (2023) 55:689–707 https://doi.org/10.1007/s11063-022-10904-8

Ismail Alarab1 · Simant Prakoonwit1

Accepted: 25 May 2022 / Published online: 16 June 2022 © The Author(s) 2022

Elliptic data—one of the largest Bitcoin transaction graphs—has admitted promising results in many studies using classical supervised learning and graph convolutional network models for anti-money laundering. Despite the promising results provided by these studies, only few have considered the temporal information of this dataset, wherein the results were not very satisfactory. Moreover, there is very sparse existing literature that applies active learning to this type of blockchain dataset. In this paper, we develop a classification model that combines long-short-term memory with GCN—referred to as temporal-GCN—that classifies the illicit transactions of Elliptic data using its transaction’s features only. Subsequently, we present an active learning framework applied to the large-scale Bitcoin transaction graph dataset, unlike previous studies on this dataset. Uncertainties for active learning are obtained using Monte-Carlo dropout (MC-dropout) and Monte-Carlo based adversarial attack (MC-AA) which are Bayesian approximations. Active learning frameworks with these methods are compared using various acquisition functions that appeared in the literature. To the best of our knowledge, MC-AA method is the first time to be examined in the context of active learning. Our main finding is that temporal-GCN model has attained significant success in comparison to the previous studies with the same experimental settings on the same dataset. Moreover, we evaluate the performance of the provided acquisition functions using MC-AA and MC-dropout and compare the result against the baseline random sampling model.

Keywords Temporal GCN · Uncertainty estimation · Active learning · Bitcoin data · Anti-money laundering

> B Ismail Alarab ialarab@bournemouth.ac.uk Simant Prakoonwit sprakoonwit@bournemouth.ac.uk

1 Bournemouth, UK

## Graph-Based LSTM for Anti-money Laundering: Experimenting Temporal Graph Convolutional Network with Bitcoin Data


### 1 Introduction


[p. 2]

Blockchain intelligence and forensics company CipherTrace have reported a global amount of $US 4.5 billion in 2019 of Bitcoin crime related to illicit services [1]. Money launderers exploit the pseudonym of Bitcoin ledgers by transforming the illegally obtained money from serious crimes into legitimate funds via Bitcoin network. On the other hand, Bitcoin blockchain has attracted intelligence companies and financial regulators who transact on the blockchain to be aware of its risks, such as technical developments in and societal adoption of the cryptocurrency Bitcoin [2]. The arising of illegal services and the public availability of Bitcoin data have urged the need to develop intelligent methods that exploit the transparency of the blockchain records [3]. Such methods can boost anti-money laundering (AML) in Bitcoin and enhance safeguarding cryptocurrency ecosystems. In the past few years, Elliptic company—a cryptocurrency intelligence company focusing on safeguarding cryptocurrency systems—has released a graph network of Bitcoin transactions, known as Elliptic data. This data has been a great support to the research and AML community in order to develop machine learning methods. Elliptic data acquires a graph of Bitcoin transactions that spans handcrafted local features (associated with transactions itself) and aggregated features (associated with neighbouring transactions) with partially labelled nodes. Furthermore, the labelled nodes denote licitly-transacted payments (e.g. miners) and illicit transactions (e.g. theft, scams). Previous researchers have attempted to apply this dataset to classical supervised learning methods [3, 4], graph convolutional network (GCN) [3, 5], EvolveGCN for dynamic graphs [6], signature vectors in blockchain transactions (SigTran) model [7] and uncertainty estimation with multi-layer perceptron (MLP) model [8]. Despite the promising results achieved by these studies, the highest accuracy achieved considering only the set of local features is about 97.4% and _f_ 1-score of 77.3%. Furthermore, only a few have considered the temporal information of this dataset. On the other hand, Bitcoin blockchain is a large-scale data in which the labelling process of this data is very hard and time-consuming. Active learning (AL) approach tackles this problem by querying the labels of the most informative data points that attain high performance with less labelled examples. Using Elliptic data, the only work by Lorenz et al. [9] has presented an active learning solution which has shown the capability of matching the performance of a fully supervised model by using 5% of the labelled data. However, the preceded framework has been presented with classical supervised learning methods which do not consider the graph topology or temporal sequence of Elliptic data. In this paper, we aim:

- To present a model in a novel way that considers the graph structure and temporal sequence of Elliptic data to predict illicit transactions that belong to illegal services in Bitcoin blockchain network.

[pp. 2-3]

- To perform active learning on Bitcoin blockchain data that mimics a real-life situation, since Bitcoin blockchain is a massively growing technology and its data is time-consuming to label.

The presented classification model comprises long short-term memory (LSTM) and GCN models, wherein the overall model attains an accuracy of 97.7% and _f_ 1-score of 80% which outperform previous studies with the same experimental settings. On the other hand, the presented active learning framework requires an acquisition function that relies on model’s uncertainty to query the most informative data. In this paper, the model’s uncertainty estimates are obtained using two comparable methods based Bayesian approximations which are named Monte-Carlo dropout (MC-dropout) [10] and Monte-Carlo adversarial attack

(MC-AA) [11]. We examine these two uncertainty methods due to their simplicity and efficiency where MC-AA method is the first time to be applied in the context of active learning. Hence, we use a variety of acquisition functions to test the performance of the active learning framework using Elliptic data. For each acquisition function, we evaluate the active learning performance that relies on each of MC-AA and MC-dropout uncertainty estimates. We compare the performance of the presented active learning framework against the random sampling acquisition as a baseline model.

This paper is structured as follows: Section 2 describes the related work. Section 3 demonstrates the uncertainty estimation methods used by the active learning framework. Section 4 provides various acquisition functions to be examined in the experiments. Section 5 provides the methods used to perform the classification task. Experiments are detailed in Sect. 6 followed by the results and discussions in Sect. 7. An ablation study of the proposed model is given in Sect. 8. Section 9 states the conclusion to wrap up the whole methodology.

### 2 Overview of Related Work


[p. 3]

With the appearance of illicit services in the public blockchain systems, intelligent methods have undoubtedly become a necessary need for AML regulations with the rapidly increasing amount of blockchain data. Many studies have adopted the machine learning approach in detecting illicit activities in the public blockchain. Harlev et al. [2] have tested the performance of classical supervised learning methods to predict the type of the unidentified entity in Bitcoin. Farrugia et al. [12] have applied XGBoost classifier to detect fraudulent accounts using the Ethereum dataset. Weber et al. [3] have introduced Elliptic data—a large-scale graph-structured dataset of a Bitcoin transaction graph with partially labelled nodes—to predict licit and illicit Bitcoin transactions. This dataset has been introduced by Weber et al. [3] who have discussed the outperformance of the random forest model against graph convolutional network (GCN) in classifying the licit and illicit transactions derived from the Bitcoin blockchain. Subsequently, the classification results using ensemble learning model in [4] have revealed a significant success over other benchmark methods to classify illicit transactions of Elliptic data. Also, Pareja et al. [6] have introduced EvolveGCN which is formed of GCN with a recurrent neural network such as Gated-Recurrent-Unit (GRU) and LSTM. This study has revealed the outperformance of EvolveGCN over the GCN model used by Weber et al. [3] on the same dataset. Another work in [5] has considered the neighbouring information of the Bitcoin transaction graph of Elliptic data using GCN accompanied by linear hidden layers. Without utilising any temporal information from this dataset, the latter reference has achieved an accuracy of 97.4% outperforming the GCN based models that were presented in [3, 6].

Active learning, a subfield of machine learning, is a way to make the learning algorithm choose the data to be trained on [13]. Active learning mitigates the bottleneck of the manual labelling process, such that the learning model queries the labels of the most informative data. Since it is so expensive to obtain labels, active learning has witnessed a resurgence with the appearance of big data where large-scale datasets exist [14]. Lorenz et al. [9] have presented an active learning framework in an attempt to reduce the labelling process of the large-scale Elliptic data of Bitcoin. The presented active learning solution has shown its capability in matching the performance of a fully supervised model with only 5% of the labels. The authors have focused on querying strategies based on uncertainty sampling [13, 15] and expected model change [13, 16]. For instance, the used uncertainty sampling strategy is based on

[p. 4]

the predicted probabilities provided by the random forest in [9]. Yet, no study presents an active learning framework that utilises the recent advances in Bayesian methods on Bitcoin data. On the other hand, Gal et al. [17] have presented active learning frameworks on image data where the authors have combined the recent advances in Bayesian methods into the active learning framework. This study has performed MC-dropout to produce the model’s uncertainty which is utilised by a given acquisition function to choose the most informative queries for labelling. Concisely, the authors in [18] have applied the entropy [19], mutual information [20], variation ratios [21], and mean standard deviation (Mean STD) [22, 23] acquisition functions which are compared against the random acquisition.

In this study, we conduct experiments using a classification model that exploits the graph structure and the temporal sequence of Elliptic data derived from the Bitcoin blockchain. Motivated by the studies in [9, 17], we perform the active learning frameworks, using pool based-based scenario [13] in which the classifier iteratively samples the most informative instances for labelling from an initially unlabelled pool. For each iteration, the classifier samples a batch of unlabelled data points according to their uncertainty estimates from Bayesian models using the sampling acquisition function.

### 3 Model Uncertainty: MC-Dropout Versus MC-AA


The two major types of uncertainty in a machine learning model are epistemic and aleatoric uncertainties [24]. Epistemic, also known as model uncertainty [10], is induced from the uncertainty in the parameters of the trained model. This uncertainty is reducible by training the model on enough data. Aleatoric uncertainty is the uncertainty tied with the noisy instances that lie on the decision boundary or in the overlapping region for class distributions, and therefore it is irreducible. MC-dropout has gained popularity as a prominent method in producing the two types of uncertainties [10]. Although MC-dropout is easy to perform and efficient, this method has failed, to some extent, to capture data points lying in the overlapping region of different classes where noisy instances reside [11]. The latter reference has provided an uncertainty method that is capable to reach noisy instances with high uncertainty estimates. This method is so-called MC-AA which targets mainly the instances that fall in the neighbourhood of a decision boundary. Although MC-dropout and MC-AA are both simple and promising methods, MC-AA has provided more reliable uncertainty estimates in [11]. In the light of these studies, we utilise these uncertainty methods as a part of the active learning process.

#### 3.1 MC-Dropout: Monte-Carlo Dropout


[pp. 4-5]

Initially, dropout has been provided as a simple regularisation technique that reduces the overfitting of the model [25]. The work in [10] has MC-dropout as a probabilistic approach basedonBayesianapproximationtoproduceuncertaintyestimates.MC-dropoutusesdropout after every weight layer in a neural network. Uncertainty estimates are produced by activating dropout during the testing phase by multiple stochastic forward passes wherein uncertainty measurement (e.g., mutual information) is computed.

Let _y_ ˆ be an output of an input _x_ mapped by a neural network, trained on set _Dtrain,_ with layers L and learnable weights _w_ = { _Wi_ } _i__L_ =1. Consider_y_as an observed output associated with _x_ . Then, we can express the predictive distribution as:

where _p(y_ | _x, w)_ is the model’s likelihood and _p(w_ | _Dtrain)_ is the posterior over the weights. Since the posterior distribution is analytically intractable [10], the posterior is replaced by _q_ ( _w_ ), an approximation of variational distribution. _q_ ( _w_ ) is obtained from the minimisation of Kullback–Leibler divergence (KL) to approximately match _p(w_ | _Dtrain)_ as follows referring to:

Hence, the variational inference leads to an approximated predictive distribution as:

The work in [10] has chosen _q_ ( _w_ ) to be the distribution over the matrices whose columns are randomly set to zero for posterior approximation. Then, _q_ ( _w_ ) can be defined as:

where _zi,j_ ∼ Bernoulli( _pi_ ), as realisation from Bernoulli distribution, for _i_ = 1 _,_ … _, L_ and _j_ = 1 _,_ … _K i_ −1, with _K i_ x _K i_ −1 the dimension of matrix _W i_ .

Thus, drawing T samples from Bernoulli distribution produces � _W_ 1_t, ..., W t_ _L_ � _tT_ =1. These are obtained from T stochastic forward passes with active dropout during the testing phase of the input data. Then, the predictive mean can be expressed as:

To obtain uncertainty, mutual information (MI) identifies the information gain of the outputs derived from Monte-Carlo samples over the predictions. Data points that reside near the decision boundary are more likely to acquire high mutual information referring to [8]. We can express mutual information as follows, referring to [10]:

where c is the class label, and

[pp. 5-6]

MC-dropout method can be viewed as an ensemble of multiple decision functions derived from the multiple stochastic forward passes. Precisely, it is an ensemble of multiple perturbed decisionboundaries.Asthismethodcapturesdatapointsbetweendifferentclassdistributions, a noisy point that falls in the wrong class cannot be captured by MC-dropout, since the latter method influences only the points with weak confidence. This is tackled in MC-AA method that is stated in the next part.

Initially, adversarial attacks are introduced as crafted perturbations of the input in order to produce incorrect predictions [26], which affect the integrity of the model by the attackers. These attacks fall are categorised between white-box and black-box attacks. The former is when the attacker has access to the model’s parameters, wherein the latter type accounts for using the model as a black box. White-box attacks are designed by adding perturbations to the inputs in the direction of the decision boundary formed by the model. These guided perturbations are the gradients of the loss function with respect to the input such that the input is assumed to belong to different class distribution. One of the methods used to compute the perturbations is known as FGSM (Fast Gradient Sign Method). Primarily, FGSM is proposed in[27]forattackingdeepneuralnetworks.Thismethodisbasedonmaximisingalossfunction _J_ ( _x, y_ ) in a neural network model with respect to a given input _x_ and its label _y_ . The aim of this method is to make the classifier perform poorly on the perturbed inputs as worse as possible. The perturbation of input by FGSM can be reformulated as follows:

#### 3.2 MC-AA: Monte-Carlo Based Adversarial Attack


[pp. 6-7]

with

where _xε_ is the adversarial example, _ε_ is a small number and ∇ _x_ is the gradient with respect to the input _x_ . This method perturbs the given input in the opposite direction of the initial class towards the decision boundary. MC-AA is based on the idea of FGSM by computing multiple perturbed versions of an input in a small range [11]. This leads to multiple outputs that allow obtaining uncertainty. MC-AA can be viewed as ensemble learning of multiple decisions derived from the perturbed versions of an input in a back-and-forth manner in the direction of the decision boundary. Thus, any point falling on the decision boundary will reflect a high uncertainty. In MC-AA, the noisy labels are triggered to move in a small range, so that they are more likely to escape from their wrong class. Thus, the noisy labels will be assigned with some uncertainty. Moreover, this will further increase the number of correctly classified data points to be uncertain, which does not affect the model performance. More formally, consider a discrete interval _I_ that is evenly spaced by _β_ and symmetric at zero, then it can be expressed as follows:

where _εT_ = _εmax_ that is the maximum value in the interval I as a tunable hyper-parameter to perturb an input by FGSM. T is a pre-chosen interval size, and it is also the number of ensembles to be performed via MC-AA. Consider a neural network of weights _w_ with function approximation as _f_ : _x_ →ˆ _y_ . Let _y_ be the associated observation of _x_ . Since the perturbations by MC-AA over _x_ are applied on a very small range, we can use Taylor expansion up to order 1 to make approximations as follows:

To compute the predictive mean _pMC_ − _AA_ ( _y_ | _x_ ), we find the average of the predictions of a given input as follows:

This equation boils down to:

Hence, we obtain an unbiased predictive mean by MC-AA, whereas several perturbations can be used to compute mutual information as the predictive uncertainty. Similarly, to Eq. 5, we estimate uncertainty of _x_ using mutual information as follows:

where c is the class label, and

### 4 Acquisition Functions for Active Learning


[p. 7]

Pool-based active learning is a prominent scenario [13, 28] that assumes a set of labelled data available for initial training _Dtrain_ and a set of unlabelled pool _D pool_ in a Bayesian model M with model parameters _w_ ∼ _p_ ( _w_ | _Dtrain_ ) and output predictions _p(y_ | _w, Dtrain)_ for _y_ ∈ {0 _,_ 1} in binary classification tasks. Then, the Bayesian model M that is already trained on _Dtrain_ queries the labels—from the unlabelled set _D pool_ —of an informative batch with size _b_ by an oracle in order to obtain an acceptable performance with less training data. Consider an acquisition function _a_ ( _x,_ M) that measures the score of a batch of unlabelled data { _xi_ } _i__b_ =1∈_Dpool._Let {_x_∗} _i__b_ =1be the informative batch by the acquisition function which can be expressed as follows [29]:

In what follows, we demonstrate various acquisition functions which are detailed in [24].

#### 4.1 BALD: Bayesian Active Learning by Disagreement


[pp. 7-8]

BayesianActiveLearningbyDisagreement(BALD)[20]isanacquisitionmethodthatutilises the uncertainty estimates via mutual information between the model predictions and model parameters. Hence, the learning algorithm queries the data points with the highest mutual information measurements. The highest mutual information measurements are produced when the predictions by Monte-Carlo samples are assigned with the highest probabilities where the samples are associated with different classes.

In this paper, we desire to acquire a batch of size _b_ at each sampling iteration.

Using BALD, this can be expressed as:

where _I_ˆ is derived from Eq. 5 for MC-dropout and Eq. 11 for MC-AA. Furthermore, the optimal batch is the one with b-highest scoring data points to reduce the bottleneck of acquiring a single data point at each acquisition step.

#### 4.2 Entropy


[p. 8]

This acquisition method computes the entropy using the uncertainty estimates from Eqs. 6 and 12. During the active learning process, we choose the batch size with the maximum predictive entropy [19] which can be written as:

The maximum entropy explains the lack of confidence within the obtained predictions which are typically near 0.5.

Similarly, we choose the batch with the maximum variation ratios [21] where the variation ratio is expressed as:

The maximum variation ratios correspond to the lack of confidence in the samples’ predictions.

Likewise, we sample a batch that maximise the mean standard deviation (Mean STD) [22, 23]. The predictive standard deviation can be computed as:

#### 4.4 Mean Standard Deviation


[pp. 8-9]

where _E_ corresponds to the expected mean. The _σ c_ measurement computes the standard deviation between the predictions obtained by Monte-Carlo samples on every data point. Consequently, the mean standard deviation is averaged over all _c_ classes which can be derived from:

This acquisition function uniformly draws data points from the unlabelled pool at random.

Fig. 1 Representative graph structure of Elliptic data. This dataset incorporates 49 directic acyclic graphs. Each graph is associated with a timestep _t_ . The colours of the nodes denote the labels provided by this dataset

In this section, we provide a detailed description of Elliptic data. Then we demonstrate temporal-GCN which is the proposed classification model to classify the illicit transactions in this dataset.

### 5 Methods


#### 5.1 Dataset Description


[p. 9]

We use the Bitcoin dataset launched by Elliptic company that is renowned for detecting illicit services in cryptocurrencies [3]. This dataset is formed of 49 directed acyclic graphs wherein each is extracted on a specific period of time represented as time-step _t_ , referring to Fig. 1. Each fully connected graph network incorporates nodes as transactions and edges as the flow of payments. In total, this dataset is formed of 203,769 partially labelled transactions, where 21% are labelled as licit (e.g., wallet providers, miners) and 2% are labelled as illicit (e.g. scams, malware, PonziSchemes, …). Each transaction node acquires 166 features such that the first 94 belongs to local features and the remaining as global features. Local features are derived from the transactions’ information on each node (e.g. time-step, number of outputs/inputs addresses, number of outputs/inputs unique addresses …). Meanwhile, global features are extracted from the graph network structure between each node and its neighbourhood by using the information of the one-hop backward/forward step for each transaction. In this study, we use the local features which count to 93 features (i.e. excluding time-step) without any graph-related features.

#### 5.2 Temporal Modelling


[pp. 9-10]

We refer to the presented model by temporal-GCN. This model is a combination of LSTM and GCN models which are detailed in what follows.

Initially, LSTM is proposed by [30] as a special category of recurrent neural networks (RNNs) in order to prevent the vanishing gradient problem. LSTM has proven its efficacy in many general-purpose sequence modelling applications [31–33].

Given a graph network of Bitcoin transactions as _G_ = ( _V, E_ ) with its adjacency matrix _A_ ∈ R_n_×_n_ , degree matrix _D_ ∈ R_n_×_n_ , where _V_ and _E_ are the sets of nodes as Bitcoin transactions and edges as payments flow, respectively, with | _V_ |= _n_ being the total number of nodes. Consider _xt_ ∈ R_dx_ as the node feature vector with _dx_ -dimensional features and layer output _ht_ ∈[− 1 _,_ 1]_dh_ as and states _ct_ ∈ R_dh_ ∈ R _dh_ with _dh_ -dimensional embedding features.

#### 5.2.1 Long Short-Term Memory (LSTM)


[p. 10]

Then, the fully connected LSTM layer, referring to [34], can be expressed as:

where ⊙ is the Hadamard product, _σ_ ( _._ ) is the sigmoid function and tanh( _._ ) is the hyperbolic tangent function. The remaining notations refer to LSTM layer parameters as follows: _it, f t, ot_ ∈ [0 _,_ 1]_dh_ are the input, forget, and output gates, respectively. The weights _Wx._ ∈ R_dh,dx_ , _Wh._ ∈ R_dh,dx_ , _wc._ ∈ R_dh_ and biases _bi, bf , bc, bo_ express the parameters of the LSTM model.

#### 5.2.2 Topology Adaptive Graph Convolutional Network: TAGCN


[pp. 10-11]

In @@this paper, we use a graph learning algorithm called TAGCN as introduced in [35] which stems from the GCN model. Generally, GCNs are neural networks that are fed with graph-structured data, wherein the node features with a learnable kernel undergo convolutional computation to induce new node embeddings. The kernel can be viewed as a filter of the graph signal (node), wherein the work in [36] suggested the localisation of kernel parameters using Chebyshev polynomials to approximate the graph spectra. Also, the study in [37] has introduced an efficient algorithm for node classification using first-order localised kernel approximations of the graph convolutions.

where _A_ˆ is the normalization of _A_ defined by:

_A_ ˜ is the adjacency matrix of the graph _G_ with the added self-loops. _σ_ denotes the typical activation function such as _ReLU_ ( _._ ) = _max_ (0 _,._ ). _H__(l)_ is the input node embedding matrix at _l__th_ layer. W(_l_) is a trainable weight matrix used to update the output embeddings _H__(l_+1_)_ .

On the other hand, the work in [35] has introduced TAGCN which is based on GCN but with fixed-size learnable filters and adaptive to the topology of the graph to perform

convolutions in the vertex domain. Consequently, TAGCN can be expressed as follows:

where _�k_ is a learnable weight matrix at _k_ -hop from the node of interest.

#### 5.2.3 Overall Model: Temporal-GCN


[p. 11]

Since TAGCN in [35] requires no approximations in comparison to GCN by [37], we exploit the performance of TAGCN in Bitcoin data. Motivated by the work in [38] that has suggested feeding LSTM inputs with GCN node embeddings, temporal-GCN seeks to perform LSTM that learns the temporal sequence in which after is forwarded non-linearly to 2-TAGCN layers to exploit the graph structure of Bitcoin transaction graph. The temporal-GCN model can be expressed as:

where _X_ is the node feature matrix. LSTM(.) and TAGCN(.,.) are layers mapping a given input to an output from Eqs. 14 and 15, respectively. Softmax function is defined as Softmax(x) = 1 exp( _xi_ ), where Z = _Z_ =� _i_exp_(xi)_.


---

[source overview](overview.md) | [next part](text-002.md)

[^original]: Ismail Alarab, Simant Prakoonwit, "Graph-Based LSTM for Anti-money Laundering: Experimenting Temporal Graph Convolutional Network with Bitcoin Data" (2022-06-15). https://link.springer.com/article/10.1007/s11063-022-10904-8
