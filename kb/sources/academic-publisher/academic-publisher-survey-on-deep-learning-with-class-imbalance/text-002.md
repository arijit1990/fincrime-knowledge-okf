---
type: Source Text
title: Survey on deep learning with class imbalance - part 2 of 9 (pp. 5-14)
description: 'Verbatim extracted text, pp. 5-14: TPR × TNR; 2 × (TPR + TNR)'
resource: https://link.springer.com/article/10.1186/s40537-019-0192-5
tags:
- academic_finding
- academic_paper
- fraud_screening_synergies
- global_academic
- ml_statistics
status: stable
source_id: academic-publisher-survey-on-deep-learning-with-class-imbalance
issuer: academic_publisher
issuer_name: Academic publisher / repository
jurisdictions:
- GLOBAL_ACADEMIC
tier: 3
instrument_type: academic_paper
normative_force: academic_finding
publication_date: '2019-03-19'
legal_status: unknown
part: 2
parts_total: 9
content_mode: full_text
generated:
  by: process:fincrime-kb-build
  at: '2026-11-22T04:56:05Z'
verified:
- by: process:kb-validate/verbatim-coverage
  at: '2026-11-22T04:56:05Z'
sources:
- id: original
  resource: https://link.springer.com/article/10.1186/s40537-019-0192-5
  title: Survey on deep learning with class imbalance
  author: org:academic_publisher
  last_modified: '2019-03-19T00:00:00Z'
---

# Survey on deep learning with class imbalance

[previous part](text-001.md) | [source overview](overview.md) | [next part](text-003.md)

> Verbatim text extracted from the original (Academic publisher / repository, 2019-03-19), part 2 of 9, pp. 5-14. Markers: `[p. N]` = page in the original; `[ref: X]` = paragraph/provision reference. Normative force of this document: **academic finding**.[^original]

## TPR × TNR


[pp. 5-6]

(9) Balanced Accuracy =1

The F-Measure (Eq. 7), or F1-score, combines precision and recall using the harmonic mean, where coefficient β is used to adjust the relative importance of precision versus recall. The G-Mean (Eq. 8) measures performance by combining both the TPR and the TNR metrics using the square root of their product. Similar to the G-Mean, the Bal- anced Accuracy (Eq. 9) metric also combines TPR and TNR values to compute a metric that is more sensitive to the minority group [18]. Although F-Measure, G-Mean, and Balanced Accuracy are improvements over Accuracy and Error Rate, they are still not entirely effective when comparing performance between classifiers and various distribu- tions [28].

## 2 × (TPR + TNR)


[pp. 6-7]

The receiver operating characteristics (ROC) curve, first presented by Provost and Faw- cett [32], is another popular assessment which plots true positive rate over false posi- tive rate, creating a visualization that depicts the trade-off between correctly classified positive samples and incorrectly classified negative samples. For models which produce continuous probabilities, thresholding can be used to create a series of points along ROC space [28]. From this a single summary metric, the area under the ROC curve (AUC), can be computed and is often used to compare performance between models. A weighted- AUC​ metric, which takes cost biases into consideration when calculating the area, was introduced by Weng and Poon [33].

According to Davis and Goadrich [34], ROC curves can present overly optimis- tic results on highly skewed data sets and Precision–Recall (PR) curves should be used instead. The authors claim that a curve can only dominate in ROC space if it also domi- nates in PR space. This is justified by the fact that the false positive rate used by ROC, FPR = FP FP+TN , will be less sensitive to changes in FP as the size of the negative class grows.

According to Seliya et al. [35], learners should be evaluated with a set of complemen- tary performance metrics, where each individual metric captures a different aspect of performance. In their comprehensive study, 22 different performance metrics were used to evaluate two classifiers across 35 unique data sets. Common factor analysis was then used to group the metrics, identifying sets of unrelated performance metrics that can be used in tandem to reduce redundancy and improve performance interpretation. One example set of complementary performance metrics discovered by Seliya et al. is AUC, Brier Inaccuracy [36], and accuracy.

Machine learning techniques for class imbalanced data Addressing class imbalance with traditional machine learning techniques has been stud- ied extensively over the last two decades. The bias towards the majority class can be alle- viated by altering the training data to decrease imbalance, or by modifying the model’s underlying learning or decision process to increase sensitivity towards the minority group. As such, methods for handling class imbalance are grouped into data-level tech- niques, algorithm-level methods, and hybrid approaches. This section summarizes some of the more popular traditional machine learning methods for handling class imbalance.

Data‑level methods Data-level methods for addressing class imbalance include over-sampling and under- sampling. These techniques modify the training distributions in order to decrease the level of imbalance or reduce noise, e.g. mislabeled samples or anomalies. In their sim- plest forms, random under-sampling (RUS) discards random samples from the majority group, while random over-sampling (ROS) duplicates random samples from the minor- ity group [37].

[p. 7]

Under-sampling voluntarily discards data, reducing the total amount of information the model has to learn from. Over-sampling will cause an increased training time due to the increased size of the training set, and has also been shown to cause over-fitting [38]. Over-fitting, characterized by high variance, occurs when a model fits too closely to the training data and is then unable to generalize to new data. A variety of intelligent sam- pling methods have been developed in an attempt to balance these trade-offs.

Intelligent under-sampling methods aim to preserve valuable information for learning. Zhang and Mani [39] present several Near-Miss algorithms that use a K-nearest neigh- bors (K-NN) classifier to select majority samples for removal based on their distance from minority samples. One-sided selection was proposed by Kubat and Matwin [40] as a method for removing noisy and redundant samples from the majority class as they are discovered through a 1-NN rule and Tomek links [41]. Barandela et al. [42] use Wilson’s editing [43], a K-NN rule that removes misclassified samples from the training set, to remove majority samples from class boundaries.

A number of informed over-sampling techniques have also been developed to strengthen class boundaries, reduce over-fitting, and improve discrimination. Chawla et al. [44] introduced the Synthetic Minority Over-sampling Technique (SMOTE), a method that produces artificial minority samples by interpolating between existing minority samples and their nearest minority neighbors. Several variants to SMOTE, e.g. Borderline-SMOTE [45] and Safe-Level-SMOTE [46], improve upon the original algo- rithm by also taking majority class neighbors into consideration. Borderline-SMOTE limits over-sampling to the samples near class borders, while Safe-Level-SMOTE defines safe regions to prevent over-sampling in overlapping or noise regions.

Supervised learning systems usually define a concept with several disjuncts, where each disjunct is a conjunctive definition describing a subconcept [47]. The size of a dis- junct corresponds to the number of samples that the disjunct correctly classifies. Small disjuncts, often corresponding to rare cases in the domain, are learned concepts that correctly classify only a few data samples. These small disjuncts are problematic, as they often contain much higher error rates than large disjuncts, and they cannot be removed without compromising performance [48].

Jo and Japkowicz [49] proposed cluster-based over-sampling to address the presence of small disjuncts in the training data. Minority and majority groups are first clustered using the K-means algorithm, then over-sampling is applied to each cluster separately. This improves both within-class imbalance and between-class imbalance.

[pp. 7-8]

Van Hulse et al. [37] compared seven different sampling techniques with 11 com- monly-used machine learning algorithms. Each model was evaluated with 35 bench- mark data sets using six different performance metrics to compare results. It was shown that sampling results were highly dependent on both the learner and the evaluation

performance metric. Experiments revealed that RUS resulted in good performance over- all, outperforming ROS and intelligent sampling methods in most cases. The results sug- gest that, although RUS performs well in most cases, no sampling method is guaranteed to perform best in all problem domains, and multiple performance metrics should be used when evaluating results.

Algorithm‑level methods Unlike data sampling methods, algorithmic methods for handling class imbalance do not alter the training data distribution. Instead, the learning or decision process is adjusted in a way that increases the importance of the positive class. Most commonly, algorithms are modified to take a class penalty or weight into consideration, or the decision thresh- old is shifted in a way that reduces bias towards the negative class.

In cost-sensitive learning, penalties are assigned to each class through a cost matrix. Increasing the cost of the minority group is equivalent to increasing its importance, decreasing the likelihood that the learner will incorrectly classify instances from this group [10]. The cost matrix of a binary classification problem is shown in Table 2 [50]. A given entry of the table, cij , is the cost associated with predicting class i when the true class is j. Usually, the diagonal of the cost matrix, where i = j , is set to 0. The costs corre- sponding to false positive and false negative errors are then adjusted for desired results.

Ling and Sheng [51] categorize cost-sensitive methods as either a direct method, or a meta-learning method. Direct methods are methods that have cost-sensitive capabilities within themselves, achieved through modification of the learner’s underlying algorithm such that costs are taken into consideration during learning. The optimization process changes from one of minimizing total error, to one of minimizing total cost. Meta-learn- ing methods utilize a wrapper to convert cost-insensitive learners into cost-sensitive systems. If a cost-insensitive classifier produces posterior probability estimates, the cost matrix can be used to define a new threshold p∗ such that:

(10) p∗= c10 c10 + c01

Usually, thresholding methods use p∗ (Eq. 10) to redefine the output decision threshold when classifying samples [51]. Threshold moving, or post-processing the output class probabilities using Eq. 10, is one meta-learning approach that converts a cost-insensitive learner into a cost-sensitive system.

[pp. 8-9]

One of the biggest challenges in cost-sensitive learning is the assignment of an effec- tive cost matrix. The cost matrix can be defined empirically, based on past experiences, or a domain expert with knowledge of the problem can define them. Alternatively, the false negative cost can be set to a fixed value while the false positive cost is varied, using a validation set to identify the ideal cost matrix. The latter has the advantage of exploring

Table 2 Cost matrix

Actual positive Actual negative

Predicted positive C(1, 1) = c11 C(1, 0) = c10 Predicted negative C(0, 1) = c01 C(0, 0) = c00

a range of costs, but can be expensive and even impractical if the size of the data set or number of features is too large.

Hybrid methods Data-level and algorithm-level methods have been combined in various ways and applied to class imbalance problems [10]. One strategy includes performing data sam- pling to reduce class noise and imbalance, and then applying cost-sensitive learning or thresholding to further reduce the bias towards the majority group. Several techniques which combine ensemble methods with sampling and cost-sensitive learning were pre- sented in [28]. Liu et al. [52] proposed two algorithms, EasyEnsemble and BalanceCas- cade, that learn multiple classifiers by combining subsets of the majority group with the minority group, creating pseudo-balanced training sets for each individual classifier. SMOTEBoost [53], DataBoost-IM [54], and JOUS-Boost [55] all combine sampling with ensembles. Sun [56] introduced three cost-sensitive boosting methods, namely AdaC1, AdaC2, and AdaC3. These methods iteratively increase the impact of the minority group by introducing cost items into the AdaBoost algorithm’s weight updates. Sun showed that the cost-sensitive boosted ensembles outperformed plain boosting methods in most cases.

Deep learning background This section reviews the basic concepts of deep learning, including descriptions of the neural network architectures used throughout the surveyed works and the value of representation learning. We also touch on several important milestones that have con- tributed to the success of deep learning. Finally, the rise of big data analytics and its challenges are introduced along with a discussion on the role of deep learning in solving these challenges.

Introduction to deep learning Deep learning is a sub-field of machine learning that uses artificial neural networks (ANNs) containing two or more hidden layers to approximate some function f ∗ , where

[pp. 9-10]

f ∗ can be used to map input data to new representations or make predictions. The ANN, inspired by the biological neural network, is a set of interconnected neurons, or nodes, where connections are weighted and each neuron transforms its input into a single out- put by applying a non-linear activation function to the sum of its weighted inputs. In a feedforward network, input data propagates through the network in a forward pass, each hidden layer receiving its input from the previous layer’s output, producing a final output that is dependent on the input data, the choice of activation function, and the weight parameters [1]. Gradient descent optimization is then used to adjust the net- work’s weight parameters in order to minimize the loss function, i.e. the error between expected output and actual output.

The multilayer perceptron (MLP) is a fully-connected feedforward neural network containing at least one hidden layer. A shallow and deep MLP are illustrated in Fig. 1. The deep MLP is the simplest deep learning model in terms of implementation, but it quickly becomes very resource intensive as the number of weighted connections quickly increases.

Fig. 1 Shallow MLP vs deep MLP [57]

Fig. 2 LeNet-5 CNN architecture of 1998 [58]

[pp. 10-11]

The convolutional neural network (CNN) is a specialized feedforward neural net- work that was designed to process multi-dimensional data, e.g. images [58]. It was inspired by the brain’s visual cortex and its origins date back to the Neocognitron presented by Fukushima in 1980 [59]. A CNN architecture is typically comprised of convolutional layers, pooling (subsampling) layers, and fully-connected layers. Fig- ure 2 illustrates the LeNet-5 CNN architecture proposed by LeCun et al. [58] in 1998 for the purpose of character recognition. Unlike fully-connected layers, a single unit of a convolutional layer is only connected to a small receptive field of its input, where the weights of its connections define a filter bank [11]. The convolution operation is used to slide the filter bank across the input, producing activations at each recep- tive field that combine to form a feature map [60]. In other words, the same set of weights are used to detect a specific feature, e.g. a horizontal line, at each receptive field of the input, and the output feature map indicates the presence of this feature at each location. The concept of local connections and shared weights take advantage of the fact that input signals in close proximity of each other are usually highly cor- related, and that input signals are often invariant to location. By combining multiple filter banks in a single convolutional layer, the layer can learn to detect multiple fea- tures in the input, and the resulting feature maps become the input of the next layer. Pooling layers are added after one or more convolutional layers in order to merge semantically similar features and reduce dimensionality [11]. After the convolutional and pooling layers, the multi-dimensional output is flattened and fed to fully-con- nected layers for classification. Similar to the MLP, output activations are fed from

one layer to the next in a forward pass, and the weights are updated through gradi- ent descent.

The MLP and CNN are just two of many alternative DNN architectures that have been developed over the years. Recurrent neural networks (RNNs), autoencoders, and stochastic networks are explained thoroughly in [1, 60, 61]. They also present advanced optimization techniques that have been shown to improve training time and performance, e.g. regularization methods, parameter initialization, improved optimizers and activation functions, and normalization techniques.

Representation learning The success of a conventional machine learning algorithm is highly dependent on the representation of the input data, making feature engineering a critical step in the machine learning workflow. This is very time consuming and for many complex prob- lems, e.g. image recognition, it can be extremely difficult to determine which features will yield the best results. Deep learning offers a solution to this problem by building upon the concept of representation learning [11].

[pp. 11-12]

Representation learning is the process of using machine learning to map raw input data features into a new representation, i.e. a new feature space, for the purpose of improving detection and classification tasks. This mapping from raw input data to new representations is achieved through non-linear transformations of the input data. Com- posing multiple non-linear transformations creates hierarchical representations of the input data, increasing the level of abstraction through each transformation. This auto- matic generation of new features saves valuable time by removing the need for experts to manually hand engineer features, and improves overall performance in many complex problem domains, such as image and speech, where it is otherwise difficult to determine the best features. As data passes through the hidden layers of a DNN, it is transformed by each layer into a new representation. Given sufficient data, DNNs are able to learn high-level feature representations of inputs through the composition of multiple hidden layers. These learned representations amplify components of the input which are impor- tant for discrimination, while suppressing those that are unimportant [11]. Deep learn- ing architectures achieve their power through this composition of increasingly complex abstract representations [60]. This approach to problem solving intuitively makes sense, as composing simple concepts into complex concepts is analogous to many real-world problem domains.

Deep learning milestones The first DNNs date back to the 1960’s, but they were largely abandoned in favor of tra- ditional machine learning methods due to difficulties in training and inadequate per- formance [62]. In 1986, Rumelhart et al. [63] presented backpropagation, a method for efficiently updating neural network weight parameters by propagating the gradient of the loss function through multiple layers. It was believed by most, however, that gradient descent would be unable to escape poor local minima during optimization, preventing neural networks from converging to a global acceptable solution. Today, we believe this to be untrue, as theoretical results suggest that local minima are generally not an issue

and that systems nearly always reach solutions of similar quality [11]. Despite some early successes in the late 1980s [64] and 1990s [58], DNNs were mostly forsaken in practice and research due to these challenges.

In 2006, interests in deep learning were revived as research groups presented methods for sensibly initializing DNN weights with an unsupervised layer-wise pre-training pro- cedure [65, 66]. These pre-trained Deep Belief Networks (DBNs) can then be efficiently fine-tuned through supervised learning. They proved to be very effective in image and speech tasks, and led to record breaking results on a speech recognition task in 2009 and the deployment of deep learning speech systems in Android mobile devices by 2012 [11].

[p. 12]

In 2012, Krizhevsky et al. [17] submitted a deep CNN to the Large Scale Visual Recog- nition Challenge (LSVRC) [67] that nearly halved the top-5% error rate, reducing from the previous year’s 26% down to just 16%. The work by Krizhevsky et al. included several crucial methods which have since become common practice in deep learning work. The CNN was implemented on multiple graphics processing units (GPUs). The drastic speed- up provided by parallel GPU computing allows for the training of deeper networks with larger data sets, and increased research productivity. A new non-saturating activation function, the rectified linear unit (ReLU), alleviated the vanishing gradient problem and allowed for faster training. Dropout was introduced as a regularization method to decrease over fitting in high capacity networks with many layers. Dropout simulates the ensembling of many models by randomly disabling neurons with a probability P ∈[0, 1] during each iteration, forcing the model to learn more robust features. Data augmenta- tion, artificially enlarging the data set by applying transformations to data samples, was also applied as a regularization technique. This event marked a major turning point and sparked new interest in deep learning and computer vision.

This newfound interest in deep learning drove leading technological companies to increase research efforts, producing many advances in deep learning and pushing the state-of-the-art in deep learning to new levels. Deep learning frameworks which abstract tensor computation [12–15] and GPU compatibility libraries [16] have been made avail- able to the community through open source software [68] and cloud services [69, 70]. Combined with an increasing amount of available data and public attention, deep learn- ing is growing at a faster pace than ever before.

Deep learning with big data Many organizations are being faced with the challenges of big data, as they are explor- ing large volumes of data to extract value and guide decisions [71]. Big data refers to data which exceeds the capabilities of standard data storage and data processing systems [72]. This forces practitioners to adopt new techniques for storing, manipulating, and analyzing data. The rise of big data can be attributed to improvements in hardware and software, increased internet and social media activity, and a growing abundance of sen- sor-enabled interconnected devices, i.e. the internet of things (IoT).

More specifically, big data can be characterized by the four Vs: volume, variety, veloc- ity, and veracity [72, 73]. The large volumes of data being collected require highly scala- ble hardware and efficient analysis tools, often demanding distributed implementations. In addition to adding architecture and network overhead, distributed systems have been

[p. 13]

shown to exacerbate the negative effects of class imbalanced data [74]. Advanced tech- niques for quickly processing incoming data streams and maintaining appropriate turna- round times are required to keep up with the rate at which data is being generated, i.e. data velocity. The variety of big data corresponds to the mostly unstructured, diverse, and inconsistent representations that arise as data is consumed from multiple sources over extended periods of time. This variety further increases the computational com- plexity of data preprocessing and machine learning. Finally, the veracity of big data, i.e. its accuracy and trustworthiness, must be regularly validated to ensure results do not become corrupted by invalid input. Some additional machine learning challenges that are magnified by big data include high-dimensionality, distributed infrastructures, real- time requirements, feature engineering, and data cleansing [75].

Najafabadi et al. [75] discuss the use of deep learning in solving big data challenges. The ability of DNNs to extract meaningful features from large sets of unlabeled data is particularly important, as this is commonly encountered in big data analytics. The auto- matic extraction of features from mostly unstructured and diverse data, e.g. image, text and audio data, is therefore extremely useful. With abstract features extracted from big data through deep learning methods, simple linear models can often be used to com- plete machine learning tasks more efficiently. Advanced semantic-based information storage and retrieval systems, e.g. semantic indexing and hashing [76, 77], are also made possible with these high-level features. In addition, deep learning has been used to tag incoming data streams, helping to group and organize fast-moving data [75]. In general, high-capacity DNNs are well suited for learning from the large volumes of data encoun- tered in big data analytics.

As the presence of big data within organizations continues to increase, new methods will be required to keep up with the influx of data. Despite being relatively immature, deep learning methods are proving effective in solving many big data challenges. We believe that advances in deep learning, especially in learning from unsupervised data, will play a critical role in the future of big data analytics.

Deep learning methods for class imbalanced data Anand et al. [78] explored the effects of class imbalance on the backpropagation algo- rithm in shallow neural networks in the 1990’s. The authors show that in class imbal- anced scenarios, the length of the minority class’s gradient component is much smaller than the length of the majority class’s gradient component. In other words, the major- ity class is essentially dominating the net gradient that is responsible for updating the model’s weights. This reduces the error of the majority group very quickly during early iterations, but often increases the error of the minority group and causes the network to get stuck in a slow convergence mode.

[pp. 13-14]

This section analyzes a number of deep learning methods for addressing class imbal- ance, organized by data-level, algorithm-level, and hybrid methods. For each surveyed work, we summarize the implementation details and the characteristics of the data sets used to evaluate the method. We then discuss various strengths and weaknesses, con- sidering topics such as class imbalance levels, interpretation of results, relative perfor- mance, difficulty of use, and generalization to other architectures and problem domains. Known limitations are highlighted and suggestions for future work are offered. For

consistency, class imbalance is presented as the maximum between-class ratio, ρ (Eq. 1), for all surveyed works.

Data‑level methods This section includes four papers that explore data-level methods for addressing class imbalance with DNNs. Hensman and Masko [79] first show that balancing the training data with ROS can improve the classification of imbalanced image data. Then RUS and augmentation methods are used by Lee et al. [20] to decrease class imbalance for the purpose of pre-training a deep CNN. Pouyanfar et al. [21] introduce a new dynamic sam- pling method that adjusts sampling rates according to class-wise performance. Finally, Buda et al. [23] compare RUS, ROS, and two-phase learning across multiple imbalanced image data sets.

Balancing training data with ROS Hensman and Masko [79] explored the effects of class imbalance and ROS using deep CNNs. The CIFAR-10 [80] benchmark data set, comprised of 10 classes with 6000 images per class, was used to generate 10 imbalanced data sets for testing. These 10 gen- erated data sets contained varying class sizes, ranging between 6% and 15% of the total data set, producing a max imbalance ratio ρ = 2.3 . In addition to varying the class size, the different distributions also varied the number of minority classes, where a minority class is any class smaller than the largest class. For example, a major 50–50 split (Dist. 3) reduced five of the classes to 6% of the data set size and increased five of the classes to 14%. As another example, a major singular over-representation (Dist. 5) increased the size of the airplane class to 14.5%, reducing the other nine classes slightly to 9.5%.

A variant of the AlexNet [17] CNN, which has proven to perform well on CIFAR- 10, was used for all experiments by Hensman and Masko. The baseline performance was defined by training the CNN on all distributions with no data sampling. The ROS method being evaluated consisted of randomly duplicating samples from the minority classes until all classes in the training set had an equal number of samples.


---

[previous part](text-001.md) | [source overview](overview.md) | [next part](text-003.md)

[^original]: Justin M. Johnson, Taghi M. Khoshgoftaar, "Survey on deep learning with class imbalance" (2019-03-19). https://link.springer.com/article/10.1186/s40537-019-0192-5
