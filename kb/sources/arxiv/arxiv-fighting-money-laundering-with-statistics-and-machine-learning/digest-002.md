---
type: Source Digest
title: Fighting Money Laundering with Statistics and Machine Learning - part 2 of 5 (pp. 8-13)
description: 'Verified paraphrased digest, pp. 8-13: Fighting Money Laundering with Statistics and Machine Learning > 4 Suspicious Behavior Flagging; Fighting Money Laundering with Statistics and Machine Learning > 5 Future Research Directions'
resource: https://arxiv.org/abs/2201.04207
tags:
- academic_finding
- customer_risk
- datasets_benchmarks
- global_academic
- ml_statistics
- preprint
status: stable
source_id: arxiv-fighting-money-laundering-with-statistics-and-machine-learning
issuer: arxiv
issuer_name: arXiv
jurisdictions:
- GLOBAL_ACADEMIC
tier: 3
instrument_type: preprint
normative_force: academic_finding
publication_date: '2022-11-01'
legal_status: unknown
part: 2
parts_total: 5
content_mode: digest
generated:
  by: claude-code-subagent/claude-sonnet-5-5
  at: '2026-11-22T14:46:04Z'
verified:
- by: process:kb-digest-check/anchor-match
  at: '2026-11-22T14:46:04Z'
- by: claude-code-judge-agent/claude-opus-5-5
  at: '2026-11-22T14:46:04Z'
sources:
- id: original
  resource: https://arxiv.org/abs/2201.04207
  title: Fighting Money Laundering with Statistics and Machine Learning
  author: org:arxiv
  last_modified: '2022-11-01T00:00:00Z'
digest_points: 75
---

# Fighting Money Laundering with Statistics and Machine Learning (digest)

[previous part](digest-001.md) | [source overview](overview.md) | [next part](digest-003.md)

> **Digest, not the original wording.** The licence of this source does not permit reproducing its text, so this part (pp. 8-13) is a paraphrased digest of every material point. Each point was machine-checked: its anchor phrase occurs verbatim in the original, and an independent reviewing agent confirmed the point is supported by the text. Labels: normative strength / kind. Quote the original, not this digest, when exact wording matters (see `resource`). Normative force of this document: **academic finding**.

## 4.2 Supervised Suspicious Behavior Flagging

- **descriptive / method**: Deng et al. combine logistic regression, stochastic approximation and sequential D-optimal design for active learning, deciding sequentially which observations to inquire about and use in estimation. (p. 8)[^original]  
  <sub>anchor: "Deng _et al._ [66] combine logistic regression, stochastic approximation, and sequential _D_ -optimal design for active learning."</sub>
- **descriptive / data or feature**: Deng et al. use a data set with 92 inquired accounts and two highly engineered features: one capturing velocity and size of transactions, and one capturing peer comparisons. (p. 8)[^original]  
  <sub>anchor: "The authors employ a data set with 92 inquired accounts and two highly engineered features."</sub>
- **descriptive / method**: Deng et al. define a synthetic variable as a weighted combination of the two features, with weight between 0 and 1, and fit a univariate logistic regression on it. (p. 8)[^original]  
  <sub>anchor: "the authors further define a synthetic variable _z_ ( _c,a_ ) = _ωx_(1) ( _c,a_ )+ (1_−ω_)_x_(2) ( _c,a_ )for_ω∈_[0_,_1]."</sub>
- **descriptive / finding or result**: The Deng et al. active selection approach significantly outperforms random selection and is reported as robust to underlying data distributions in simulations. (p. 8)[^original]  
  <sub>anchor: "The approach significantly outperforms random selection. Furthermore, simulations show that it is robust to underlying data distributions."</sub>
- **descriptive / method**: Borrajo et al. argue AML models may benefit from information beyond transaction statistics, such as behaviour traces covering account creation and company ownership, and apply K-nearest neighbours with custom distance functions. (p. 8)[^original]  
  <sub>anchor: "Borrajo _et al._ [69] argue that AML models may benefit from other types of information than simple transaction statistics."</sub>
- **descriptive / limitation**: Borrajo et al. report excellent results, but these were obtained on simulated data. (p. 8)[^original]  
  <sub>anchor: "While the authors report excellent results, these are, notably, obtained on simulated data."</sub>
- **descriptive / method**: Zhang and Trubey employ six machine learning models to predict the outcome of AML alarm inquiries, and the setup can be used both to qualify existing alarms and raise new ones under appropriate assumptions. (p. 8)[^original]  
  <sub>anchor: "Zhang and Trubey [72] employ six machine learning models to predict the outcome of AML alarm inquiries."</sub>
- **descriptive / method**: Zhang and Trubey assume the traditional AML flag and the true label are conditionally independent given the features. (p. 8)[^original]  
  <sub>anchor: "Assuming that _sc_ and _yc_ are conditionally independent given x _c_ , we have that"</sub>
- **descriptive / method**: A support vector machine seeks to maximise the margin between the feature observations of the two classes and a class separating hyperplane, possibly in transformed space. (p. 8)[^original]  
  <sub>anchor: "This model seeks to maximize the margin between feature observations of the two classes and a class separating hyperplane"</sub>
- **descriptive / method**: If the flagging probability is positive for all feature vectors in the support of the true-label probability, a model trained only on previously flagged clients can be used to raise new alarms. (p. 9)[^original]  
  <sub>anchor: "we can use a model, only trained on previously flagged clients, to raise new alarms."</sub>
- **descriptive / data or feature**: Zhang and Trubey use a data set of 6,113 alarms from a United States financial institution, of which 34 were reported to authorities, with ten non-disclosed features. (p. 9)[^original]  
  <sub>anchor: "The authors use a data set with 6,113 alarms from a financial institution in the United States. Of these, 34 alarms were reported to authorities."</sub>
- **descriptive / finding or result**: Random over- and undersampling, used to address class imbalance, increased the performance of a support vector machine; a feedforward neural network robust to both sampling techniques performed best in Zhang and Trubey. (p. 9)[^original]  
  <sub>anchor: "Both techniques, in particular, increase the performance of a support vector machine [73]."</sub>
- **descriptive / method**: Jullum et al. use gradient boosted trees implemented with XGBoost, additively combining K regression trees, to model AML alarms. (p. 9)[^original]  
  <sub>anchor: "The approach additively combines _f_ 1 _, . . . , fK_ regression trees (i.e., decision trees with continuous outputs) and is implemented with XGBoost [75]."</sub>
- **descriptive / data or feature**: Jullum et al. use Norwegian bank data with 16,192 non-flagged transactions, 14,932 flagged transactions dismissed after brief inquiries, 1,260 flagged transactions thoroughly inquired but dismissed, and 750 flagged and reported transactions. (p. 9)[^original]  
  <sub>anchor: "16,192 non-flagged transactions,"</sub>
- **descriptive / method**: In Jullum et al., transactions of types one to three are treated as licit and type four as illicit in the primary binary classification. (p. 9)[^original]  
  <sub>anchor: "Here, transactions in (1)-(3) are treated as licit; transactions in (4) are treated as illicit."</sub>
- **descriptive / method**: Jullum et al. propose the metric 'proportion of positive predictions' (PPP), which records the share of positive predictions when thresholds are set to obtain a pre-specified true positive rate, to compare with traditional AML systems. (p. 9)[^original]  
  <sub>anchor: "the authors propose an evaluation metric called “proportion of positive predictions” (PPP)."</sub>
- **descriptive / finding or result**: Jullum et al. results indicate that including type (1) non-flagged transactions improves performance. (p. 9)[^original]  
  <sub>anchor: "Results, in particular, indicate that the inclusion of type (1) transactions improve performance."</sub>
- **descriptive / method**: Tertychnyi et al. propose a two-layer approach: logistic regression first filters out clients with clearly non-illicit transaction patterns, then CatBoost gradient boosted trees classify the remaining clients. (p. 9)[^original]  
  <sub>anchor: "In the first layer, a logistic regression is used to filter out clients with transaction patterns that are clearly non-illicit."</sub>
- **descriptive / data or feature**: Tertychnyi et al. use data from an undisclosed bank with approximately 330,000 clients from three countries, about 0.004% reported for money laundering, with demographic and transaction statistic features. (p. 9)[^original]  
  <sub>anchor: "This contains approximately 330,000 clients from three countries. About 0.004% of the clients have been reported for money laundering."</sub>
- **descriptive / finding or result**: In Tertychnyi et al., performance varies significantly across the three countries, and performance decreases when each country is modelled separately. (p. 9)[^original]  
  <sub>anchor: "Model performance varies significantly over the three countries in the authors’ data set. However, the performance decreases when each country is modeled separately."</sub>
- **descriptive / data or feature**: Eddin et al. use a non-disclosed bank data set of 500,000 flagged transactions over 400,000 accounts, 3% of which are labelled suspicious, modelled as a graph with accounts as nodes and transactions as directed edges. (p. 9)[^original]  
  <sub>anchor: "This contains 500,000 flagged transactions distributed over 400,000 accounts (3% of which are deemed truly suspicious and labeled as positives)."</sub>
- **descriptive / finding or result**: Eddin et al. find that GuiltyWalker random-walk graph features, capturing distances to illicit nodes, increase model performance; models compared were random forest, GLM and LightGBM. (p. 9)[^original]  
  <sub>anchor: "Results indicate that the inclusion of GuiltyWalker features [81], using random walks to capture the distances between a given node and illicit nodes, increases model performance."</sub>
- **descriptive / method**: Charitou et al. combine a sparse autoencoder, used to obtain higher-dimensional latent encodings that increase separation of illicit and licit observations, with a generative adversarial network to flag money laundering in online gambling. (p. 9)[^original]  
  <sub>anchor: "Charitou _et al._ [82] combine a sparse autoencoder and a generative adversarial network to flag money laundering in online gambling."</sub>
- **descriptive / data or feature**: The most relevant Charitou et al. data set on online gambling money laundering contains 4,700 observations, of which 1,200 were flagged. (p. 9)[^original]  
  <sub>anchor: "This data set contains 4,700 observations (1,200 of which were flagged for potential money laundering)."</sub>
- **descriptive / method**: Weber et al. use graph convolutional neural networks on the open Elliptic bitcoin transaction graph provided by a private cryptocurrency analytics company. (p. 9)[^original]  
  <sub>anchor: "An open data set is provided by Elliptic, a private cryptocurrency analytics company."</sub>
- **descriptive / data or feature**: The Elliptic graph has 203,769 nodes (bitcoin transactions) and 234,355 directed payment-flow edges; about 21% of nodes are labelled licit and 2% illicit, with 166 features per node (94 local, 72 one-hop). (p. 9)[^original]  
  <sub>anchor: "The data set contains a transaction graph _G_ = ( _V, E_ ) with _|V|_ = 203 _,_ 769 nodes and _|E|_ = 234 _,_ 355 edges."</sub>
- **descriptive / data or feature**: The Elliptic labels were assigned with a heuristic approach: 21% of nodes labelled licit and 2% illicit. (p. 9)[^original]  
  <sub>anchor: "Using a heuristic approach, 21% of the nodes are labeled as licit; 2% as illicit."</sub>
- **descriptive / data or feature**: Each node in the Elliptic data has 166 recorded features; 94 record local information and 72 record one-hop information. (p. 9)[^original]  
  <sub>anchor: "For all nodes, 166 features are recorded. Of these, 94 record local information, while the remaining 72 record one-hop information."</sub>
- **descriptive / method**: Graph convolutional neural networks are neural networks designed to work on graph data. (p. 9)[^original]  
  <sub>anchor: "Graph convolutional neural networks [85] are neural networks designed to work on graph data."</sub>
- **descriptive / method**: Lorenz et al. test seven unsupervised anomaly detection techniques, including local outlier factor, K-nearest neighbours, principal component analysis, one-class SVM, cluster-based outlier factor, angle-based outlier detection and isolation forest; all perform substantially worse than a supervised random forest benchmark on F1-score. (p. 9)[^original]  
  <sub>anchor: "The authors try seven different techniques: local outlier factor [90],"</sub>
- **descriptive / finding or result**: In Weber et al., the best performance was achieved by a random forest, while the graph convolutional network was competitive; a temporal graph convolutional network outperformed the simple version but still fell short of the random forest. (p. 10)[^original]  
  <sub>anchor: "While the best performance is achieved by a random forest model, the graph convolutional neural network proved competitive."</sub>
- **descriptive / finding or result**: Alarab et al. concatenate graph convolutional embeddings with linear embeddings of original features in a neural network, which significantly increases performance on the Elliptic data. (p. 10)[^original]  
  <sub>anchor: "Alarab _et al._ [87] propose a neural network structure where graph convolutional embeddings are concatenated with linear embeddings of the original features."</sub>
- **descriptive / finding or result**: Vassallo et al. find gradient boosted trees outperform random forests on the Elliptic data and propose an adapted XGBoost to reduce the impact of concept drift. (p. 10)[^original]  
  <sub>anchor: "Results, in particular, indicate that gradient boosted trees outperform random forests."</sub>
- **descriptive / finding or result**: Lorenz et al. test seven unsupervised anomaly detection techniques on Elliptic data, and all seven perform substantially worse than a supervised random forest benchmark, contrary to earlier literature on unsupervised flagging. (p. 10)[^original]  
  <sub>anchor: "Strikingly, all seven unsupervised methods perform substantially worse than a supervised random forest benchmark."</sub>
- **descriptive / limitation**: Lorenz et al. suggest one possible explanation for the contrast with earlier unsupervised results is that Elliptic bitcoin data is qualitatively different from bank transaction data. (p. 10)[^original]  
  <sub>anchor: "One possible explanation is that the Elliptic data, constructed over bitcoin transactions, is qualitatively different from bank transaction data."</sub>
- **descriptive / method**: Lorenz et al. evaluate with the F1-score, the harmonic mean of precision and recall, and also test four active learning strategies, two unsupervised (elliptic envelope, isolation forest) and two supervised (uncertainty sampling, expected model change), with random forest, gradient boosting and logistic regression. (p. 10)[^original]  
  <sub>anchor: "The remaining two build on supervised techniques: uncertainty sampling [94] and expected model change [95]."</sub>
- **descriptive / finding or result**: In the active learning experiments on Elliptic data, the supervised strategies performed best. (p. 10)[^original]  
  <sub>anchor: "Results show that the"</sub>

## 5 Future Research Directions

- **descriptive / finding or result**: The review finds class imbalance and the lack of publicly available data sets to be central challenges to AML research, which may motivate synthetic data. (p. 10)[^original]  
  <sub>anchor: "Our review reveals that class imbalance and the lack of publicly available data sets are central challenges to AML research."</sub>
- **descriptive / context**: Banks hold large amounts of high-dimensional and unlabeled data, which may motivate dimension reduction and semi-supervised learning. (p. 10)[^original]  
  <sub>anchor: "We also note how banks hold vast amounts of high-dimensional and unlabeled data [96]."</sub>
- **descriptive / definition**: The ROC curve plots true positive against false positive rates for varying thresholds; the area under it (ROC-AUC) measures separability, equal to 1 for perfect and 0.5 for naive classifiers. (p. 10)[^original]  
  <sub>anchor: "The area under a ROC curve, called ROCAUC (or sometimes just AUC), is a measure of separability; equal to 1 for perfect classifiers and 0.5 for naive classifiers."</sub>
- **descriptive / definition**: The precision-recall curve plots precision against true positive rate for varying thresholds and is particularly relevant when class imbalance is severe and true positive rates matter. (p. 10)[^original]  
  <sub>anchor: "This curve is particularly relevant when class imbalance is severe and true positive rates are of high importance."</sub>
- **descriptive / definition**: Cohen's kappa is suggested for multi-class models; it measures agreement between two labelings while accounting for chance agreement. (p. 10)[^original]  
  <sub>anchor: "For multi-class models, Cohen’s _κ_ [99] is appealing."</sub>
- **descriptive / limitation**: None of the metrics presented consider calibration, that is whether model outputs reflect true likelihoods. (p. 10)[^original]  
  <sub>anchor: "Finally, note that none of the presented metrics introduced above consider calibration, i.e., if model outputs reflect true likelihoods."</sub>

## 5.1 Class Imbalance, Evaluation Metrics, and Synthetic Data

- **descriptive / method**: Simple class imbalance remedies include under- and oversampling; SMOTE generates convex combinations of minority class observations for vector data. (p. 10)[^original]  
  <sub>anchor: "Synthetic minority oversampling (SMOTE) by Chawla _et al._ [40] is another option for vector data."</sub>
- **descriptive / method**: Borderline-SMOTE and borderline-SMOTE-SVM generate observations along estimated decision boundaries; ADASYN generates observations according to data densities. (p. 10)[^original]  
  <sub>anchor: "Extensions include borderline-SMOTE [101] and borderline-SMOTE-SVM [102]."</sub>
- **descriptive / context**: There is relatively little literature on data augmentation for time series data such as transaction sequences. (p. 10)[^original]  
  <sub>anchor: "For time series data (e.g., transaction sequences), there is relatively little literature on data augmentation [104]."</sub>
- **descriptive / method**: Basic time series augmentations listed are window cropping, window warping (compressing or extending slices), flipping (multiplying signs by -1), and noise injection (typically Gaussian). (p. 10)[^original]  
  <sub>anchor: "window cropping, where random time series slices are extracted,"</sub>
- **descriptive / method**: Teng et al. propose a wavelet transformation that preserves low-frequency patterns while adding noise to high-frequency patterns. (p. 10)[^original]  
  <sub>anchor: "Teng _et al._ [105] propose a wavelet transformation to preserve low-frequency time series patterns while noise is added to high-frequency patterns."</sub>
- **descriptive / method**: Cubuk et al. propose combining transformations at random, and Fons et al. propose two adaptive schemes based on model loss and prediction-loss rankings. (p. 10)[^original]  
  <sub>anchor: "Cubuk _et al._ [107] propose to combine transformations at random."</sub>
- **descriptive / context**: Simulating known or hypothesised money laundering patterns may be the only option for researchers without data; combined with private data it may ensure some reproducibility and generalisability. (p. 10)[^original]  
  <sub>anchor: "Simulating known or hypothesized money laundering patterns from scratch may be the only option for researchers with no available data."</sub>
- **descriptive / data or feature**: PaySim is a simulator for mobile phone transfers developed by Lopez-Rojas and Axelsson; Weber et al. and Suzumura and Kanezashi augment it toward a classic bank setting. (p. 10)[^original]  
  <sub>anchor: "The authors develop a simulator, PaySim, for mobile phone transfers."</sub>
- **descriptive / method**: Iwana and Uchida use dynamic time warping element alignment to mix patterns, wrapping sample pattern features to match reference pattern time steps. (p. 11)[^original]  
  <sub>anchor: "Iwana and Uchida [106] utilize the element alignment properties of dynamic time wrapping to mix patterns;"</sub>
- **descriptive / finding or result**: The Elliptic data set is described as the only public data set found in the AML literature, containing a graph over bitcoin transactions. (p. 11)[^original]  
  <sub>anchor: "We have found only one public data set within the AML literature: the Elliptic data set [84]."</sub>
- **descriptive / limitation**: Graph-based approaches may be difficult to implement in a bank setting, since a bank only knows transactions going to or from its own clients; they may be more relevant for authorities' treatment of AML reports. (p. 11)[^original]  
  <sub>anchor: "Indeed, any bank only knows about transactions going to or from its own clients."</sub>
- **descriptive / method**: t-SNE, and its parametric counterpart, embeds observations in 2 or 3 dimensions by building pairwise similarity probabilities and minimising Kullback-Leibler divergence to a lower-dimensional distribution. (p. 11)[^original]  
  <sub>anchor: "Next, we seek projections that minimize the Kullback-Leibler divergence [116] to a distribution in a lower-dimensional space."</sub>
- **descriptive / method**: ISOMAP extends multidimensional scaling using shortest paths between observations to capture intrinsic similarity. (p. 11)[^original]  
  <sub>anchor: "Another option is ISOMAP [117]. This extends multidimensional scaling [118], using the shortest path between observations to capture intrinsic similarity."</sub>

## 5.2 Visualization, Dimension Reduction, and Semi-supervised Learning

- **descriptive / method**: Autoencoders can be used for dimension reduction, synthetic data generation and semi-supervised learning: an autoencoder trained on all observations has its lower layers reused in a classifier for labelled data. (p. 11)[^original]  
  <sub>anchor: "Indeed, we may train an autoencoder with all the observations. Lower layers can then be reused in a network trained to classify labeled observations."</sub>
- **descriptive / definition**: The variational autoencoder is a probabilistic generative model whose loss has a reconstruction error part and a Kullback-Leibler divergence part pushing latent representations toward a Gaussian. (p. 11)[^original]  
  <sub>anchor: "The second part employs the Kullback-Leibler divergence to push latent feature representations toward a Gaussian distribution."</sub>
- **descriptive / method**: Conditional variational autoencoders and conditional GANs take class labels into account, allowing generation of class-specific observations; in conditional GANs labels feed both discriminator and generator. (p. 11)[^original]  
  <sub>anchor: "Specifically, class labels are fed as inputs to both the discriminator and generator."</sub>
- **descriptive / context**: Most GAN methods were designed for visual data, while methods for time-series data have recently been proposed. (p. 11)[^original]  
  <sub>anchor: "While most generative adversarial network methods have been designed to work with visual data, methods applicable to time-series data have recently been proposed"</sub>

## 5.3 Neural Networks, Deep Learning, and Transfer Learning

- **descriptive / context**: Neural networks used in current AML research are generally small and shallow; deep networks use multiple layers to derive higher-level features and have succeeded in vision, language and high-frequency financial time series. (p. 11)[^original]  
  <sub>anchor: "The neural networks used in current AML research are generally small and shallow."</sub>
- **descriptive / context**: Some authors propose deep networks to check KYC image information such as driver's licences, or to ease alarm inquiries with sentiment analysis. (p. 11)[^original]  
  <sub>anchor: "Some authors have also proposed to use the approach to check KYC image information (e.g., driver’s licenses) [131, 132] or ease alarm inquiries with sentiment analysis [133]."</sub>
- **descriptive / method**: State-of-the-art deep networks combat unstable gradients using rectified and exponential linear units, Xavier, He or LeCun weight initialisation, batch normalisation, gradient clipping and layer normalisation for recurrent networks, and residual or skip connections. (p. 11)[^original]  
  <sub>anchor: "State-of-the-art deep neural networks use multiple methods to combat unstable gradients."</sub>
- **descriptive / method**: Regularisation adds penalty terms to a model's loss function to limit network weights, as one technique used against overfitting. (p. 11)[^original]  
  <sub>anchor: "Regularization [148] limits network weights by adding penalty terms to a model’s loss function."</sub>
- **descriptive / method**: Max-norm regularisation restricts network weights directly during training, as a further technique against overfitting. (p. 11)[^original]  
  <sub>anchor: "Finally, max-norm regularization [149] restricts network weights directly during training."</sub>
- **descriptive / method**: Transfer learning trains a network on a source problem, then transfers (usually lower-layer) weights to a new network fine-tuned on a target problem. (p. 12)[^original]  
  <sub>anchor: "One common approach starts by training a neural network on some source problem."</sub>
- **descriptive / method**: Domain adaptation tries to alleviate distributional differences across domains; Ganin and Lempitsky use a gradient reversal layer, and Tzeng et al. use a semi-supervised setup with few labelled target observations. (p. 12)[^original]  
  <sub>anchor: "Ganin and Lempitsky [152] propose an unsupervised technique that employs a gradient reversal layer and backpropagation to learn shift invariant features."</sub>
- **descriptive / recommendation**: Hedegaard et al. critique the generic test setup used in supervised domain adaptation literature and propose a fair evaluation protocol. (p. 12)[^original]  
  <sub>anchor: "we refer to the work by Hedegaard _et al._ [154] for a discussion and critique of the generic test setup"</sub>
- **descriptive / method**: Recurrent neural networks model sequential data; a basic RNN layer with m neurons uses input and output weight matrices, a bias vector and an activation function. (p. 12)[^original]  
  <sub>anchor: "where W _x ∈_ R_d×m_ is an input weight matrix, W _y ∈_ R_m×m_ is an output weight matrix"</sub>
- **descriptive / method**: Cho et al. propose a simpler architecture based on gated recurrent units (GRUs). (p. 12)[^original]  
  <sub>anchor: "Cho _et al._ [158] propose a simpler architecture based on gated recurrent units (called GRUs)."</sub>
- **descriptive / method**: The temporal neural bag-of-features architecture, an alternative to RNNs, uses a radial basis function layer with K neurons and an accumulation layer to give a constant-length representation; it has proved successful for financial time series classification. (p. 12)[^original]  
  <sub>anchor: "An alternative to recurrent neural networks, the temporal neural bag-of-features architecture has proved successful for financial time series classification [159]."</sub>
- **descriptive / method**: A temporal bilinear layer with m neurons uses W1 to model feature interactions at fixed time points and W2 to model feature changes over time. (p. 13)[^original]  
  <sub>anchor: "Notably, W 1 models feature interactions at fixed time points while W 2 models feature changes over time."</sub>
- **descriptive / method**: Attention mechanisms allow networks to focus dynamically on relevant sequence elements; Bahdanau et al. propose additive attention with an alignment model normalised by softmax, and Luong attention uses dot-product similarity between encoder and decoder states. (p. 13)[^original]  
  <sub>anchor: "Attention mechanisms have recently become state-of-the-art. These allow neural networks to dynamically focus on relevant sequence elements."</sub>
- **descriptive / method**: The transformer applies self-attention with query, key and value matrices derived from the input, row-wise softmax, masking of future elements in the decoder, multi-head attention, positional encoding, residual connections and layer normalisation. (p. 13)[^original]  
  <sub>anchor: "Vaswani _et al._ [163] propose the seminal transformer architecture."</sub>
- **descriptive / method**: The temporal attention augmented bilinear layer is highlighted as a further attention mechanism; E expresses the relative importance of temporal feature instances learned through W, while A holds the attention scores, and a scalar lambda in [0,1] allows soft attention. (p. 13)[^original]  
  <sub>anchor: "In particular, E is used to express the relative importance of temporal feature instances"</sub>

---

[previous part](digest-001.md) | [source overview](overview.md) | [next part](digest-003.md)

[^original]: arXiv, "Fighting Money Laundering with Statistics and Machine Learning" (2022-11-01). https://arxiv.org/abs/2201.04207
